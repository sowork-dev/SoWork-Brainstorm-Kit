# Persona Packs and Role Definitions

**Keep historical references separate from fictional role design.** Every persona is a fictional workshop perspective written for this project, not the real person's statements, a personality assessment, a historical conclusion, or an endorsed digital counterpart. Names, limited background references, and fictional capabilities are stored in separate fields. Neither the people referenced nor their estates, associated organizations, or brands are presented as endorsing the project or its proposals.

Start with three personas only when no size or lineup is specified. Preserve a complete requested lineup; add people only when the user delegates filling the team. The catalog is a starting point, not a limit on whom users may request. If a requested person cannot be verified, label the perspective as unverified fiction; do not invent a biography.

## OPEN_CAST: create your own group

Ask for “Ocean Explorers,” “five architects,” or “only Yang Guifei and Qin Shi Huang.” The four casts and nine profiles are starting examples, not category or cast-size limits. A swap retains the topic and constraints. See the [facilitator protocol](../FACILITATOR.md).

## Four starting examples

- **Across the Ages**: Qin Shi Huang, Yang Guifei, and David Bowie. Shared rules, memorable experiences, and identity-led narratives complement one another. An optional example rather than the fallback for every topic.
- **Rock Legends**: David Bowie, Freddie Mercury, and Joan Jett. Breaking conventions, crowd participation, and low-cost pilots. The name is not a current chart or a factual popularity ranking.
- **The Glamour Council**: Yang Guifei, Cleopatra VII, and Coco Chanel. Sensory experience, reciprocal alliances, and precise simplification. This is not a beauty ranking, and the personas' capabilities are not reduced to appearance.
- **The Ruthless Strategists**: Qin Shi Huang, Genghis Khan, and Napoleon. Sharp resource trade-offs, distributed expansion, and stress-testing. The name does not praise cruelty; never produce plans based on violence or coercion.

These are localized, playful theme labels, not factual rankings or endorsements. `packs.json` retains each original Chinese pack name and its original aliases alongside English aliases. Pack IDs and the three members in each pack remain unchanged.

## More Than a Name Swap

Each persona has a distinct mechanism, proposal shape, and way of challenging other ideas. Those differences should remain recognizable even with the names removed. Actual generation tests are needed to assess that quality; the existence of the fields alone does not establish that it passes.

For example, the Qin Shi Huang persona turns a process into reusable rules; the Yang Guifei persona redesigns the moment that makes people stay and remember; the Bowie persona changes the participant's identity. These are editorial definitions, not historically established personality traits.

On first use, give a brief notice: "These are AI-generated fictional personas collaborating on ideas, not the real people or quotations from historical sources." After that, respond naturally without repeating the disclaimer in every sentence.

### Plain-English Follow-Ups

Users can express the next step in ordinary English, for example:

- **Continue**: build on the current exchange.
- **Swap cast**: request any new theme or lineup, retaining the topic and constraints.
- **Swap member**: ask to replace one persona.
- **Bolder**: ask for a more adventurous idea, within the same safety boundaries.
- **More practical**: ask for a more workable version.
- **You decide**: choose and develop a direction using the current topic and cast. If the user is explicitly delegating cast selection, select a suitable cast then; do not reset an ongoing session to the default trio.

These are suggested conversational phrasings, not new schema fields or a claim that this catalog implements a command parser.

## Evidence Boundaries

The `evidence_status` values preserve the source catalog's reported review scope; this English localization does not claim a fresh source review:

- `official-body-reviewed`: relevant official source text was obtained and read.
- `official-search-excerpt-only`: only a search excerpt for an official source was checked. Access to the full text was blocked; this does not mean a complete biography was read.
- `museum-api-title-verified`: only an artwork title in the museum API was checked. An artwork's subject does not establish that the historical person had modern professional capabilities.

`reference_context` contains the limited background reference and its qualifications. All `fictional_lens`, `mechanism`, `proposal_shape`, `challenge_pattern`, and `voice_rule` content is authored for this project. The workshop mechanisms must not be treated as findings from the historical sources. Improvised persona dialogue is not historical evidence. Do not invent quotations, personal experiences, or endorsements, and do not use song lyrics or realistic voice imitation to impersonate a person.

See [SOURCES.md](SOURCES.md) for the background references and their limits.
