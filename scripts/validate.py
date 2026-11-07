#!/usr/bin/env python3
"""Static packaging checks, NOT an LLM/ChatGPT behavioral test."""
from pathlib import Path
import json
import re
import sys
import unittest
from build import ROOT, render_bundle, pin_relative_links


class PackageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / 'methods/catalog.json').read_text(encoding='utf-8'))

    def test_exact_card_ids_and_source_order(self):
        expected = ['A01', 'A02'] + [f'B{i:02d}' for i in range(1, 30)]
        self.assertEqual([c['id'] for c in self.catalog], expected)
        self.assertEqual(len({c['path'] for c in self.catalog}), len(expected))

    def test_cards_have_guidance_and_resolved_sources(self):
        for card in self.catalog:
            with self.subTest(card=card['id']):
                path = ROOT / card['path']
                self.assertTrue(path.resolve().is_relative_to((ROOT / 'methods').resolve()))
                text = path.read_text(encoding='utf-8')
                self.assertIn(f"## {card['id']}｜{card['name']}", text)
                headings = {
                    component
                    for heading in re.findall(r'\*\*([^*]+)\*\*', text)
                    for component in heading.split('／')
                }
                for field in ('開場', '流程', '追問', '產出'):
                    self.assertIn(field, headings)
                cited = set(re.findall(r'\[(\d+)\](?![(:])', text.split('## Sources')[0]))
                declared = set(re.findall(r'(?m)^\[(\d+)\] https://', text))
                self.assertTrue(cited <= declared)

    def test_coordinator_covers_confirmation_and_human_boundaries(self):
        text = (ROOT / 'FACILITATOR.md').read_text(encoding='utf-8')
        for field in ('LAZY_COUNCIL', 'TEACHING', 'DISCOVER', 'CAST', 'CO_CREATE',
                      'CONVERGE', 'HANDOFF', '不把發想作業丟回用戶',
                      '先產出再提供選項', '使用者沒有選組', '不重問已知項目',
                      '只有明確要求教學', '不杜撰真人'):
            self.assertIn(field, text)
        ids = set(re.findall(r'\b[AB]\d{2}\b', text))
        self.assertTrue(ids <= {c['id'] for c in self.catalog})

    def test_bundle_is_current_and_self_contained(self):
        text = (ROOT / 'START-HERE.txt').read_text(encoding='utf-8')
        self.assertEqual(text, render_bundle())
        self.assertEqual(len(re.findall(r'(?m)^## [AB]\d{2}｜', text)), 31)
        self.assertIn('## Sources', text)
        self.assertIn('尚未完成 ChatGPT', text)
        self.assertIn('LAZY_COUNCIL', text)
        self.assertLess(text.index('LAZY_COUNCIL'), text.index('## A01｜'))
        for persona in json.loads((ROOT / 'personas/catalog.json').read_text()):
            self.assertIn(persona['name'], text)
            self.assertIn(persona['mechanism'], text)

    def test_personas_separate_reference_and_editorial_fiction(self):
        people = json.loads((ROOT / 'personas/catalog.json').read_text())
        self.assertGreaterEqual(len(people), 9)
        self.assertEqual(len({p['id'] for p in people}), len(people))
        lenses = []
        for persona in people:
            for field in ('id', 'name', 'reference_context', 'reference_url', 'evidence_status',
                          'fictional_lens', 'mechanism', 'proposal_shape', 'challenge_pattern', 'voice_rule'):
                self.assertTrue(persona.get(field), (persona['id'], field))
            self.assertTrue(persona['reference_url'].startswith('https://'))
            self.assertEqual(persona['persona_status'], 'editorial-fiction')
            lenses.append(persona['fictional_lens'])
        self.assertEqual(len(lenses), len(set(lenses)))
        self.assertIn('歷史事實與角色設定分開', (ROOT / 'personas/README.md').read_text())

    def test_four_user_requested_packs_resolve(self):
        packs = json.loads((ROOT / 'personas/packs.json').read_text())
        people = json.loads((ROOT / 'personas/catalog.json').read_text())
        ids = {p['id'] for p in people}
        self.assertEqual([p['name'] for p in packs], ['古今綜合組', '熱門搖滾組', '美美女組', '殘暴組'])
        for pack in packs:
            self.assertEqual(len(pack['members']), 3)
            self.assertEqual(len(set(pack['members'])), 3)
            self.assertTrue(set(pack['members']) <= ids)
        self.assertTrue({'楊貴妃', '秦始皇'} <= {p['name'] for p in people})

    def test_lazy_controls_available(self):
        text = (ROOT / 'FACILITATOR.md').read_text()
        for command in ('繼續', '換組', '換人', '更大膽', '更務實', '你決定'):
            self.assertIn(command, text)

    def test_release_version_is_consistent(self):
        version = json.loads((ROOT / 'version.json').read_text())['version']
        self.assertIn('v' + version, (ROOT / 'START-HERE.txt').read_text())
        self.assertIn('/v' + version + '/START-HERE.txt', (ROOT / 'README.md').read_text())

    def test_english_method_ids_and_source_closure(self):
        english = json.loads((ROOT / 'locales/en/methods/catalog.json').read_text())
        self.assertEqual([c['id'] for c in english], [c['id'] for c in self.catalog])
        for en, zh in zip(english, self.catalog):
            self.assertEqual(en['status'], zh['status'])
            path = ROOT / en['path']
            self.assertTrue(path.resolve().is_relative_to((ROOT / 'locales/en/methods').resolve()))
            body = path.read_text()
            self.assertIn(f"## {en['id']} | {en['name']}", body)
            labels = {part.strip() for heading in re.findall(r'\*\*([^*]+)\*\*', body)
                      for part in heading.split('/')}
            for field in ('Opening', 'Process', 'Follow-up', 'Output'):
                self.assertIn(field, labels)
            en_urls = set(re.findall(r'https://[^\s)]+', body))
            zh_urls = set(re.findall(r'https://[^\s)]+', (ROOT / zh['path']).read_text()))
            self.assertEqual(en_urls, zh_urls)

    def test_english_persona_and_cast_identity_parity(self):
        zh_people = json.loads((ROOT / 'personas/catalog.json').read_text())
        en_people = json.loads((ROOT / 'locales/en/personas/catalog.json').read_text())
        self.assertEqual([p['id'] for p in en_people], [p['id'] for p in zh_people])
        for en, zh in zip(en_people, zh_people):
            self.assertEqual(set(en), set(zh))
            for key in ('id', 'persona_status', 'reference_url', 'evidence_status', 'verification_url'):
                self.assertEqual(en.get(key), zh.get(key), (en['id'], key))
        zh_packs = json.loads((ROOT / 'personas/packs.json').read_text())
        en_packs = json.loads((ROOT / 'locales/en/personas/packs.json').read_text())
        self.assertEqual([p['id'] for p in en_packs], [p['id'] for p in zh_packs])
        for en, zh in zip(en_packs, zh_packs):
            self.assertEqual(en['members'], zh['members'])
            self.assertIn(zh['name'], en['aliases'])

    def test_english_bundle_is_current_and_separate(self):
        text = (ROOT / 'START-HERE.en.txt').read_text()
        self.assertEqual(text, render_bundle(language='en'))
        self.assertEqual(len(re.findall(r'(?m)^## [AB]\d{2} \| ', text)), 31)
        self.assertIn('Default: LAZY_COUNCIL', text)
        self.assertNotIn('# 主持規約', text)
        self.assertIn('End-to-end ChatGPT web testing remains incomplete', text)
        for persona in json.loads((ROOT / 'locales/en/personas/catalog.json').read_text()):
            self.assertIn(persona['name'], text)
            self.assertIn(persona['mechanism'], text)
        with self.assertRaises(ValueError):
            render_bundle(language='not-a-language')

    def test_parallel_landing_and_launch_review_exist(self):
        for path in ('README.zh-TW.md', 'docs/bilingual-map.md',
                     'docs/public-launch-review.zh-en.md', 'docs/reviewed-files.json'):
            self.assertTrue((ROOT / path).is_file(), path)
        readme = (ROOT / 'README.md').read_text()
        self.assertIn('START-HERE.en.txt', readme)
        self.assertIn('README.zh-TW.md', readme)
        inventory = json.loads((ROOT / 'docs/reviewed-files.json').read_text())
        self.assertEqual(inventory['baseline_commit'], '81d8720c9a6258a42ad86deb5dd59ad501531176')
        self.assertEqual(inventory['file_count'], 60)
        self.assertEqual(len({row['path'] for row in inventory['files']}), 60)
        self.assertTrue(all(row['inspected'] for row in inventory['files']))

    def test_detached_bundles_keep_license_and_resolve_relative_links(self):
        notice = (ROOT / 'LICENSE').read_text().strip()
        for filename in ('START-HERE.txt', 'START-HERE.en.txt'):
            text = (ROOT / filename).read_text()
            self.assertIn(notice, text)
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
                self.assertTrue(target.startswith(('https://', 'http://', 'mailto:', '#')), target)
        english = (ROOT / 'START-HERE.en.txt').read_text()
        self.assertIn('/locales/en/personas/SOURCES.md', english)

    def test_embedded_link_pinning_preserves_file_context(self):
        version = json.loads((ROOT / 'version.json').read_text())['version']
        for directory in ('personas', 'locales/en/personas'):
            result = pin_relative_links('[Sources](SOURCES.md)', Path(directory) / 'README.md', version)
            self.assertIn(f'/blob/v{version}/{directory}/SOURCES.md', result)
        with self.assertRaises(ValueError):
            pin_relative_links('[Bad](../../../../../outside.md)', Path('methods/index.md'), version)

    def test_you_decide_does_not_reset_an_existing_cast(self):
        packs = json.loads((ROOT / 'locales/en/personas/packs.json').read_text())
        aliases = {alias.casefold() for pack in packs for alias in pack['aliases']}
        self.assertNotIn('you decide', aliases)
        self.assertIn('do not reset an ongoing session', (ROOT / 'locales/en/personas/README.md').read_text())

    def test_default_bundles_do_not_embed_full_human_teaching_protocol(self):
        zh = (ROOT / 'START-HERE.txt').read_text()
        en = (ROOT / 'START-HERE.en.txt').read_text()
        self.assertNotIn('# 主持規約｜先確認目的，再推薦方法', zh)
        self.assertNotIn('# TEACHING | Opt-in human practice', en)
        self.assertEqual(zh.count('模式標示：這是方法參考卡。'), 31)
        self.assertEqual(en.count('Mode guard: this is a reference card.'), 31)

    def test_no_internal_runtime_or_credential_artifacts(self):
        prohibited = [r'/Users/', r'/home/azureuser', r'\.hermes/', r'\.openclaw/',
                      r'-----BEGIN (?:RSA |OPENSSH )?PRIVATE KEY-----',
                      r'gh[pousr]_[A-Za-z0-9]{25,}', r'xox[baprs]-[A-Za-z0-9-]{12,}',
                      r'sk-[A-Za-z0-9_-]{25,}', r'\b(?:10|192\.168)\.[0-9]+\.[0-9]+\.[0-9]+\b']
        # The checker itself contains signatures, not actual internal artifacts.
        for path in ROOT.rglob('*'):
            if not path.is_file() or any(p in ('.git', '__pycache__') for p in path.parts):
                continue
            if path == Path(__file__):
                continue
            if path.suffix not in ('.md', '.txt', '.json', '.py', '.yml', '.yaml') and path.name != 'LICENSE':
                continue
            text = path.read_text(encoding='utf-8')
            for signature in prohibited:
                with self.subTest(file=str(path.relative_to(ROOT)), signature=signature):
                    self.assertIsNone(re.search(signature, text))

    def test_documentation_links_resolve_locally(self):
        for path in ROOT.rglob('*.md'):
            if '.git' in path.parts:
                continue
            text = path.read_text(encoding='utf-8')
            for target in re.findall(r'\[[^\]]+\]\(([^)]+)\)', text):
                if target.startswith(('https://', 'http://', '#', 'mailto:')):
                    continue
                target = target.split('#', 1)[0]
                self.assertTrue((path.parent / target).exists(), f'{path}: {target}')


if __name__ == '__main__':
    unittest.main(verbosity=2)
