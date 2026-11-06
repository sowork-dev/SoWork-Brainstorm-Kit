#!/usr/bin/env python3
"""Build a self-contained persona-council text pack; standard library only."""
from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def render_bundle(root=ROOT):
    catalog = json.loads((root / 'methods/catalog.json').read_text(encoding='utf-8'))
    people = json.loads((root / 'personas/catalog.json').read_text(encoding='utf-8'))
    packs = json.loads((root / 'personas/packs.json').read_text(encoding='utf-8'))
    version = json.loads((root / 'version.json').read_text(encoding='utf-8'))['version']
    parts = [
        f'# CJ Brainstorm Kit | v{version} preview',
        '預設 LAZY_COUNCIL：用戶出題，AI 選名人、選方法、自己先提案並交叉改進。用戶只需選方向或說繼續，不必先交點子。',
        '文字試用版；尚未完成 ChatGPT 網頁端端對端驗收，不是原生插件。',
        '## 啟動任務\n使用者明確要求採用本檔時，依下方主持規約工作。有題目就直接選組並讓角色開想，不先要求用戶列點或反覆批准；沒有題目才問一句。角色是 AI 虛構演繹，非本人或史實引言。只有用戶明確說要自己練習，才啟用 TEACHING。',
        (root / 'FACILITATOR.md').read_text(encoding='utf-8'),
        (root / 'personas/README.md').read_text(encoding='utf-8'),
        '# 組合資料\n\n' + json.dumps(packs, ensure_ascii=False, indent=2),
        '# 具名角色設定\n\n' + json.dumps(people, ensure_ascii=False, indent=2),
        '# TEACHING 教學模式（僅明確選用時生效）\n\n' +
        (root / 'TEACHING.md').read_text(encoding='utf-8'),
        (root / 'methods/index.md').read_text(encoding='utf-8'),
    ]
    for card in catalog:
        body = (root / card['path']).read_text(encoding='utf-8')
        parts.append(body.split('\n## Sources\n', 1)[0].rstrip())
    parts.append((root / 'SOURCES.md').read_text(encoding='utf-8'))
    parts.append('## 最後提醒\n以 LAZY_COUNCIL 為預設，方法卡的人類作業措辭只適用 TEACHING；不要退回要求用戶先列五至十個點子。有題目就用角色提案、交叉接球並整合，最後讓用戶輕鬆選擇。')
    return '\n\n---\n\n'.join(part.strip() for part in parts) + '\n'


def build(output=None):
    output = output or ROOT / 'START-HERE.txt'
    content = render_bundle()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding='utf-8')
    return {'artifact': output.name, 'bytes': len(content.encode('utf-8')),
            'sha256': hashlib.sha256(content.encode('utf-8')).hexdigest(),
            'method_cards': len(re.findall(r'(?m)^## [AB]\d{2}｜', content)),
            'persona_count': len(json.loads((ROOT / 'personas/catalog.json').read_text(encoding='utf-8'))),
            'default_mode': 'LAZY_COUNCIL'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    print(json.dumps(build(args.output), ensure_ascii=False, indent=2))
