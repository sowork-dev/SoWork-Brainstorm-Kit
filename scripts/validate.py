#!/usr/bin/env python3
"""Static packaging checks, NOT an LLM/ChatGPT behavioral test."""
from pathlib import Path
import json
import re
import sys
import unittest
from build import ROOT, render_bundle


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
