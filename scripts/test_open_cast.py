#!/usr/bin/env python3
"""Static open-cast contract tests. Not model-quality assertions."""
import json
from pathlib import Path
import unittest
from build import ROOT, render_bundle


class OpenCastContractTests(unittest.TestCase):
    def test_both_protocols_explicitly_allow_new_themes_and_exact_casts(self):
        for locale in (ROOT, ROOT / 'locales/en'):
            text = (locale / 'FACILITATOR.md').read_text()
            for marker in ('OPEN_CAST', 'custom_theme', 'explicit_members', 'cast_size', 'session_state'):
                self.assertIn(marker, text)

    def test_open_cast_protocol_survives_detached_download(self):
        for language in ('zh-TW', 'en'):
            text = render_bundle(language=language)
            for marker in ('OPEN_CAST', 'custom_theme', 'explicit_members', 'cast_size', 'session_state'):
                self.assertIn(marker, text)

    def test_automatic_commands_are_not_starter_pack_aliases(self):
        for locale in (ROOT, ROOT / 'locales/en'):
            packs = json.loads((locale / 'personas/packs.json').read_text())
            aliases = {a.casefold() for p in packs for a in p['aliases']}
            for command in ('自動', '你選', '你決定', 'you decide', 'automatic', 'auto', 'pick for me'):
                self.assertNotIn(command, aliases)

    def test_recorded_trials_match_current_frozen_inputs_and_exact_history(self):
        import hashlib
        suite_bytes = (ROOT / 'tests/open-cast-cases.json').read_bytes()
        suite = json.loads(suite_bytes)
        for case in suite['cases']:
            data = json.loads((ROOT / 'examples/test-runs' / (case['id'] + '.json')).read_text())
            bundle_bytes = (ROOT / case['bundle']).read_bytes()
            self.assertEqual(data['bundle_sha256'], hashlib.sha256(bundle_bytes).hexdigest())
            self.assertEqual(data['suite_sha256'], hashlib.sha256(suite_bytes).hexdigest())
            self.assertEqual(len(data['turns']), len(case['turns']))
            self.assertEqual(data['external_tools'], [])
            self.assertFalse(data['chatgpt_web_acceptance'])
            attachment = data['activation_prefix'] + '<attachment filename="' + case['bundle'] + '">\n' + bundle_bytes.decode('utf-8') + '\n</attachment>'
            messages = [{'role': 'system', 'content': data['system_message']}]
            readable = (ROOT / 'examples/test-runs' / (case['id'] + '.md')).read_text()
            for index, (actual, expected) in enumerate(zip(data['turns'], case['turns'])):
                self.assertEqual(actual['user'], expected['prompt'])
                self.assertEqual(actual['expectations'], expected['expectations'])
                self.assertEqual(actual['status'], 'completed')
                messages.append({'role': 'user', 'content': (attachment + '\n\n' if index == 0 else '') + actual['user']})
                message_bytes = json.dumps(messages, ensure_ascii=False, separators=(',', ':')).encode('utf-8')
                self.assertEqual(actual['messages_sha256'], hashlib.sha256(message_bytes).hexdigest())
                self.assertIn(actual['assistant'], readable)
                self.assertEqual(actual['effective_provider'], data['requested_provider'])
                self.assertEqual(actual['effective_model'], data['requested_model'])
                messages.append({'role': 'assistant', 'content': actual['assistant']})

    def test_product_name_and_canonical_source(self):
        for language in ('zh-TW', 'en'):
            self.assertIn('# SoWork-Brainstorm-Kit |', render_bundle(language=language))
        source = (ROOT / 'scripts/build.py').read_text()
        self.assertIn('https://github.com/contentincubator2-ops/SoWork-Brainstorm-Kit', source)


if __name__ == '__main__':
    unittest.main(verbosity=2)
