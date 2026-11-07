# CJ Brainstorm Kit

### Your topic. A council of famous perspectives. Ideas without the homework.

**English · [繁體中文](README.zh-TW.md)**

Give the AI a topic and let it pick a fictional cast, choose a brainstorming method, develop proposals, challenge them, and turn them into useful options. You can simply say **“Continue,” “Swap the cast,” or “You decide.”**

> **Public preview—not a validated production release.** Includes 31 method cards with overlapping variants, nine editorial persona profiles, and four themed casts. These are fictional interpretations within one AI conversation, not real people, authentic quotations, endorsements, or independently running agents. End-to-end ChatGPT web testing is still incomplete. A repository-wide reuse license is still pending; see [LICENSE](LICENSE).

## Start in one minute

1. Download **[START-HERE.en.txt — English](https://github.com/contentincubator2-ops/cj-brainstorm-kit/releases/download/v0.3.0/START-HERE.en.txt)** or **[START-HERE.txt — 繁體中文](https://github.com/contentincubator2-ops/cj-brainstorm-kit/releases/download/v0.3.0/START-HERE.txt)**.
2. Upload the chosen file to an AI tool that can actually read text attachments.
3. Paste this:

```text
Use the attached kit in LAZY_COUNCIL mode.
Pick a complementary cast of fictional famous-persona perspectives, choose a method, and start generating proposals. Let the characters challenge and improve one another, then recommend a direction.
Do not ask me to write five or ten ideas first. If you need a noncritical detail, state a reasonable assumption and keep going.
My topic is: ____. Pick the cast for me and begin.
```

No topic yet? Say **“Start.”** The intended first response is one short topic question—not a questionnaire.

**Already using v0.1.0 or v0.2.0?** Download the new attachment and start a fresh conversation, or explicitly replace the old attachment and instructions. Publishing a new release does not update a file already loaded in your chat.

## Pick a cast—or let the AI choose

| Cast | Starting lineup | Editorial jobs |
| --- | --- | --- |
| **Across the Ages** · 古今綜合組 | Qin Shi Huang · Yang Guifei · David Bowie | Repeatable rules · memorable experiences · identity reframing |
| **Rock Legends** · 熱門搖滾組 | David Bowie · Freddie Mercury · Joan Jett | Reinvention · shared participation · DIY execution |
| **The Glamour Council** · 美美女組 | Yang Guifei · Cleopatra VII · Coco Chanel | Sensory moments · reciprocal alliances · precise editing |
| **The Ruthless Strategists** · 殘暴組 | Qin Shi Huang · Genghis Khan · Napoleon | Hard trade-offs · distributed nodes · focused stress tests |

These English cast labels are proposed localizations for the preview; the original Chinese aliases and machine IDs are retained. These are playful workshop themes, not popularity charts, beauty rankings, historical personality claims, or approval of violence. Each profile separates its limited public reference context from its author-created thinking mechanism.

Want someone else? Name a famous figure—or a combination such as **Yang Guifei and Qin Shi Huang**. The bundled nine are a starting library, not the limit. Unknown background claims must be labeled rather than invented.

## What a round should look like

1. A named cast with different jobs—not three copies of the same adviser.
2. One or two specific proposals per character.
3. At least two concrete cross-improvements: one character revises a specific part of another's idea.
4. Three comparable directions, with an AI recommendation and its assumptions.
5. A few low-effort controls so you can keep going without producing ideas yourself.

See the **[English fictional example](locales/en/examples/persona-council.md)** or **[中文示例](examples/persona-council.md)**. They are authored demonstrations, **not platform test transcripts**.

## Keep it effortless

- **Continue** — take the recommended direction further.
- **Swap the cast / replace a member** — keep the topic, change the perspectives.
- **Go bolder** — change the mechanism, not just the adjectives.
- **Make it practical** — cut dependencies, cost, and steps.
- **You decide** — let the facilitator choose and expand a direction.

Want to practice brainstorming yourself? Explicitly ask for **TEACHING** mode. Human exercises are opt-in; ordinary council users should not be sent away to write idea lists.

## Use a repository URL instead?

Ask the AI to read the appropriate facilitator protocol, persona catalog, cast definitions, and selected method card. **It must confirm it actually retrieved the needed content.** If it cannot, use the complete text attachment. Pasting a repository URL is not installation and does not guarantee that every file will be fetched.

## English and Chinese editions

Use one runtime language pack at a time. The paired documents and stable method IDs make comparison possible without doubling the prompt with two complete languages.

- [English core protocol](locales/en/FACILITATOR.md) · [中文主持規約](FACILITATOR.md)
- [English method index](locales/en/methods/index.md) · [中文方法索引](methods/index.md)
- [English persona guide](locales/en/personas/README.md) · [中文人物指南](personas/README.md)
- [Bilingual comparison map](docs/bilingual-map.md)
- [Public-launch review / 公開前逐項檢查](docs/public-launch-review.zh-en.md)

## What is—and is not—verified

The build and validation scripts check packaging, IDs, references, language coverage, and common sensitive-data patterns. **They do not measure brainstorming quality or prove ChatGPT behavior.** Platform access, actual file retrieval, persona differentiation, low-effort controls, and multi-turn results need real testing.

This kit is a text workflow, not a native plugin, external tool authorization, background timer, live meeting room, or real-person invitation service. Do not put private client or participant information in public Issues or pull requests.

## Maintain the kit

Python 3.10 or later; standard library only:

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

The build creates separate English and Traditional Chinese text packs from their corresponding source files. See [setup](SETUP.md), [compatibility](locales/en/docs/compatibility.md), [public-material policy](locales/en/docs/sanitization-policy.md), [contributing](CONTRIBUTING.md), [security](SECURITY.md), and the [changelog](CHANGELOG.md).

## Credits and reuse

Concept and product direction: **CJ Wang**. The methods and source materials are credited separately in [method sources](locales/en/SOURCES.md) and [persona sources](locales/en/personas/SOURCES.md). Editorial role-play is not a claim that these figures actually held the proposed views.

**Publicly readable does not yet mean openly licensed.** No project-wide redistribution or commercial reuse license has been selected. Do not describe this preview as MIT-licensed, CC-licensed, officially certified, or endorsed by the cited people and institutions. See [LICENSE](LICENSE).
