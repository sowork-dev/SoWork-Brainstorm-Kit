#!/usr/bin/env python3
"""Build a self-contained text facilitation bundle; Python standard library only."""
from pathlib import Path
import argparse
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]


def render_bundle(root=ROOT):
    catalog = json.loads((root / 'methods/catalog.json').read_text(encoding='utf-8'))
    parts = [
        '# CJ Brainstorm Kit | v0.1.0 preview',
        '使用方式：將本檔交給 AI，並明確要求依本檔主持；不是只要求摘要。',
        '文字試用版；尚未完成 ChatGPT 網頁端端對端驗收，不是原生插件。',
        '## 啟動任務\n請先確認使用者目的，再推薦適合的方法；等使用者確認後逐輪引導。每次只問一個關鍵問題並等待回覆。現在先問今天要處理的具體題目；不要直接列完所有方法或代寫完整答案。',
        (root / 'FACILITATOR.md').read_text(encoding='utf-8'),
        (root / 'methods/index.md').read_text(encoding='utf-8'),
    ]
    for card in catalog:
        # Paths are from the committed, validated catalog, never user input.
        path = root / card['path']
        body = path.read_text(encoding='utf-8')
        parts.append(body.split('\n## Sources\n', 1)[0].rstrip())
    parts.append((root / 'SOURCES.md').read_text(encoding='utf-8'))
    parts.append('## 最後提醒\n現在開始與使用者對話，不要摘要全部方法。先讀使用者已提供的資訊，僅詢問下一個必要缺口。')
    return '\n\n---\n\n'.join(part.strip() for part in parts) + '\n'


def build(output=None):
    output = output or ROOT / 'START-HERE.txt'
    content = render_bundle()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding='utf-8')
    return {'artifact': output.name, 'bytes': len(content.encode('utf-8')),
            'sha256': hashlib.sha256(content.encode('utf-8')).hexdigest(),
            'method_cards': len(re.findall(r'(?m)^## [AB]\d{2}｜', content))}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    print(json.dumps(build(args.output), ensure_ascii=False, indent=2))
