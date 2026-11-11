#!/usr/bin/env python3
"""Build separate self-contained English and Traditional Chinese text packs."""
from pathlib import Path
import argparse
import hashlib
import json
import re
import posixpath
from urllib.parse import quote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ('zh-TW', 'en')
SOURCE_REPOSITORY = 'https://github.com/contentincubator2-ops/SoWork-Brainstorm-Kit'


def pin_relative_links(text, source_path, version, root=ROOT):
    """Retain source-file context when embedding Markdown in a detached TXT."""
    source_path = Path(source_path)

    def replace(match):
        label, target = match.groups()
        if target.startswith(('https://', 'http://', 'mailto:', '#')):
            return match.group(0)
        parts = urlsplit(target)
        resolved = posixpath.normpath((source_path.parent / parts.path).as_posix())
        if parts.scheme or parts.netloc or resolved.startswith(('../', '/')) or resolved == '..':
            raise ValueError(f'Unsafe embedded link: {target}')
        if not (root / resolved).is_file():
            raise ValueError(f'Unresolved embedded link: {source_path}: {target}')
        pinned = f'{SOURCE_REPOSITORY}/blob/v{version}/{quote(resolved, safe="/")}'
        if parts.fragment:
            pinned += '#' + quote(parts.fragment, safe='-')
        return f'[{label}]({pinned})'

    return re.sub(r'\[([^\]]+)\]\(([^)]+)\)', replace, text)


def render_bundle(root=ROOT, language='zh-TW'):
    if language not in LANGUAGES:
        raise ValueError(f'Unsupported language: {language}')
    locale = root if language == 'zh-TW' else root / 'locales/en'
    catalog = json.loads((locale / 'methods/catalog.json').read_text(encoding='utf-8'))
    people = json.loads((locale / 'personas/catalog.json').read_text(encoding='utf-8'))
    packs = json.loads((locale / 'personas/packs.json').read_text(encoding='utf-8'))
    version = json.loads((root / 'version.json').read_text(encoding='utf-8'))['version']

    def include(path):
        return pin_relative_links(path.read_text(encoding='utf-8'), path.relative_to(root), version, root)
    if language == 'en':
        opening = [
            'Default: LAZY_COUNCIL. The user supplies a topic; the AI picks a fictional famous-persona cast and a method, proposes ideas, cross-improves them, and recommends a direction. No idea-list homework is required.',
            'Text-only public preview. End-to-end ChatGPT web testing remains incomplete. This is not a native plugin.',
            '## Activation\nWhen the user explicitly asks to use this pack, follow the facilitator protocol. With a usable topic, pick the cast and start ideating in the same response. Ask one short topic question only when no topic is available. Characters are fictional interpretations, not real people or historical quotations. TEACHING applies only to an explicit request for human brainstorming practice. Use English unless the user requests another language.',
        ]
        pack_heading = '# Cast definitions'
        people_heading = '# Editorial persona profiles'
        teaching_heading = '# TEACHING: human practice only when explicitly selected'
        teaching_summary = 'Only an explicit request to practice brainstorming or run a real-human workshop activates TEACHING. Clarify the practice, recommend a method and wait for agreement, give one human task at a time, preserve real input, then compare and summarize. Full teaching guidance remains in the repository; the reference cards below supply the individual exercises.'
        card_guard = 'Mode guard: this is a reference card. In LAZY_COUNCIL, the AI cast performs the ideation; human homework and waiting apply only to explicitly selected TEACHING.'
        license_heading = '# License | MIT'
        closing = '## Final reminder\nLAZY_COUNCIL is the default. Human-homework wording in reference cards applies only to TEACHING. Do not ask the ordinary council user to write five or ten ideas first. Generate character proposals, cross-improvements, and a synthesis, then offer low-effort controls.'
    else:
        opening = [
            '預設 LAZY_COUNCIL：用戶出題，AI 選名人、選方法、自己先提案並交叉改進。用戶只需選方向或說繼續，不必先交點子。',
            '文字試用版；尚未完成 ChatGPT 網頁端端對端驗收，不是原生插件。',
            '## 啟動任務\n使用者明確要求採用本檔時，依下方主持規約工作。有題目就直接選組並讓角色開想，不先要求用戶列點或反覆批准；沒有題目才問一句。角色是 AI 虛構演繹，非本人或史實引言。只有用戶明確說要自己練習動腦，才啟用 TEACHING。預設使用繁體中文，除非用戶指定其他語言。',
        ]
        pack_heading = '# 組合資料'
        people_heading = '# 具名角色設定'
        teaching_heading = '# TEACHING 教學模式（僅明確選用時生效）'
        teaching_summary = '只有明確要求練習動腦或帶真人工作坊才啟用：確認練習題目，推薦並等真人同意，一次給一個真人任務，保存真實輸入，再比較與收尾。完整教學規約保留在 repo；以下參考卡提供各項練習。普通懶人模式不可因此要求用戶交點子作業。'
        card_guard = '模式標示：這是方法參考卡。LAZY_COUNCIL 由 AI 角色執行發想；只有明確選擇 TEACHING 才套用真人作業與等待。'
        license_heading = '# 授權｜MIT（原創內容；第三方素材不在此授權範圍）'
        closing = '## 最後提醒\n以 LAZY_COUNCIL 為預設，方法卡的人類作業措辭只適用 TEACHING；不要退回要求用戶先列五至十個點子。有題目就用角色提案、交叉接球並整合，最後讓用戶輕鬆選擇。'
    parts = [
        f'# SoWork-Brainstorm-Kit | v{version} preview | {language}',
        *opening,
        include(locale / 'FACILITATOR.md'),
        include(locale / 'personas/README.md'),
        pack_heading + '\n\n' + json.dumps(packs, ensure_ascii=False, indent=2),
        people_heading + '\n\n' + json.dumps(people, ensure_ascii=False, indent=2),
        teaching_heading + '\n\n' + teaching_summary,
        include(locale / 'methods/index.md'),
    ]
    for card in catalog:
        path = root / card['path']
        body = include(path).split('\n## Sources\n', 1)[0].rstrip()
        parts.append(card_guard + '\n\n' + body)
    parts.append(include(locale / 'SOURCES.md'))
    parts.append(license_heading + '\n\n' + (root / 'LICENSE').read_text(encoding='utf-8'))
    parts.append(closing)
    return '\n\n---\n\n'.join(part.strip() for part in parts) + '\n'


def build(language='zh-TW', output=None):
    default_name = 'START-HERE.txt' if language == 'zh-TW' else 'START-HERE.en.txt'
    output = output or ROOT / default_name
    content = render_bundle(language=language)
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(content, encoding='utf-8')
    locale = ROOT if language == 'zh-TW' else ROOT / 'locales/en'
    return {'artifact': output.name, 'language': language,
            'bytes': len(content.encode('utf-8')),
            'sha256': hashlib.sha256(content.encode('utf-8')).hexdigest(),
            'method_cards': len(re.findall(r'(?m)^## [AB]\d{2}(?:｜| \| )', content)),
            'persona_count': len(json.loads((locale / 'personas/catalog.json').read_text(encoding='utf-8'))),
            'default_mode': 'LAZY_COUNCIL'}


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--lang', choices=('all', *LANGUAGES), default='all')
    parser.add_argument('--output', type=Path)
    args = parser.parse_args()
    if args.lang == 'all' and args.output is not None:
        parser.error('--output requires a single --lang')
    languages = LANGUAGES if args.lang == 'all' else (args.lang,)
    print(json.dumps([build(lang, args.output) for lang in languages], ensure_ascii=False, indent=2))
