# Setup

**English · [繁體中文](SETUP.zh-TW.md)**

## Recommended: a complete text attachment

Download `START-HERE.en.txt` for English or `START-HERE.txt` for Traditional Chinese. Upload one language pack to an AI tool that can read it and explicitly request **LAZY_COUNCIL** mode. Give it a topic; the AI should choose the cast and do the first round. The launch prompt is in [README](README.md).

You do not need Python, a Git checkout, an API key, or a native plugin to try the text attachment. Whether a particular account/tool reads and follows it still needs verification.

## Replacing an older version

v0.1.0 used a human-practice flow. v0.2.0 introduced AI-led persona councils. v0.3.0 added parallel English and Traditional Chinese editions and a launch review. v0.4.0 renames the kit to SoWork-Brainstorm-Kit, clarifies open themes/exact lineups, and adds recorded model trials.

An old attachment will not update when the repository changes. Download the new file and use a fresh conversation or explicitly replace old instructions. Do not mix two complete runtime language packs unless you intentionally want bilingual output.

## No attachment support

Paste content only within the tool's actual capabilities. If a complete pack is too long, provide the facilitator protocol and persona/cast data first, then the selected method card. Never claim the full repository was read when only its landing page was retrieved.

## Repository URL entry

For English, the needed sources are under `locales/en/`; for Traditional Chinese, they remain at the root and in `methods/` and `personas/`. Ask the AI to read the facilitator protocol, persona catalog, cast definitions, and selected method card. Use the complete attachment if retrieval fails.

The repository-URL route and complete ChatGPT web interaction have **not** passed end-to-end acceptance testing.

## Modes

- **LAZY_COUNCIL:** the AI proposes and refines ideas. You can just say “Continue” or “You decide.”
- **TEACHING:** explicitly selected human brainstorming practice or a real human workshop. Here the facilitator waits for real participant input.

This version is not a native Skill/Plugin installation. It does not grant external tool access or promise automatic cross-chat memory, background work, timers, or real participants.
