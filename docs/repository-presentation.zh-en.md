# Repository presentation research｜公開呈現研究

[English README](../README.md) · [繁中首頁](../README.zh-TW.md) · [Roadmap／發展路線](roadmap.zh-en.md)

## Scope｜範圍

A concise presentation study for the v0.4.0 public preview—not a product benchmark, popularity ranking, or endorsement. The references below are primary repository/documentation pages. Observations describe their presentation; decisions describe what this project adopts.

這是 v0.4.0 公開試用稿的呈現研究，不是產品效能比較、人氣排名或第三方背書。下列均為第一方 repo／官方文件；「觀察」與「本站採用決策」分開。

## Patterns worth adapting｜值得採用的模式

### 1. Lead with a use case and an action｜先說用途，立刻給入口

**Observed:** prompts.chat opens with a clear product category and direct browsing/self-hosting links, then explains the collection and contribution route.[1]

**觀察：** prompts.chat 先交代產品類別，提供瀏覽／自架入口，再說明內容與貢獻方式。[1]

**Our decision:** Put “Your topic. Any cast. Ideas without the homework.” above implementation details. Offer one-language downloads and a copyable first prompt before the file map. Do not borrow another project's superlatives, star counts, testimonials, privacy claims, or platform support claims.

**採用：** 用「出題、任意組團、不交作業」說明價值，先給單語下載與可貼上的開場指令，再談檔案。不搬用他站的最高級形容、星數、證言、保密或平台支援承諾。

### 2. Show the structure and the evidence boundary｜結構清楚，證據不混用

**Observed:** anthropics/skills defines its instruction-folder format, links examples/specification/template, and separates demonstration caveats from platform-specific usage instructions.[2]

**觀察：** anthropics/skills 先解釋指引資料夾格式，導向範例、規格與模板，也區分示範限制和平台使用方式。[2]

**Our decision:** Explain that this kit is a text workflow, not that repository's native Skill/plugin integration. Separate authored fictional walkthroughs from model-run transcripts, static CI, and pending browser acceptance. Keep the exact engine and execution environment in each evidence record.

**採用：** 說清楚本套件是文字流程，不套用對方的原生 Skill／插件安裝說法。作者示範、模型紀錄、靜態 CI 與待完成的瀏覽器驗收分開；每份證據保留實際引擎與執行環境。

### 3. Make participation predictable｜讓參與規則可預期

**Observed:** GitHub recommends README-based navigation and expectations communicated through licensing, contribution guidance, and a code of conduct. Its security guidance also recommends a security policy and considers private vulnerability reporting.[3]

**觀察：** GitHub 建議 README 協助導覽，搭配授權、貢獻指引與社群守則交代期待；安全建議包含安全政策與私人弱點回報選項。[3]

**Our decision:** Add friendly bilingual issue forms, a PR checklist, a concise conduct policy, FAQ, and a phased roadmap. Keep the license decision explicitly pending. Refer sensitive reports to the existing security policy without inventing a private inbox or claiming private reporting is enabled.

**採用：** 補雙語 Issue 表單、PR 清單、簡明守則、FAQ 與分階段路線。授權明列待決；敏感事件依現有安全政策，不捏造私人信箱或聲稱已啟用私密回報。

## Positioning decision｜定位決策

The differentiator to demonstrate is not the size of the persona catalog: it is **open-ended cast assembly + concrete cross-improvement + low-effort multi-turn control**. Four starter groups are discoverability shortcuts, not the product boundary. Three people is a default, not a maximum. Neither larger casts nor source references imply unlimited context or verified biographical expertise.

要展示的差異不是人物庫有多大，而是**開放組團＋具體交叉改進＋低負擔多輪控制**。四組是入口，不是產品邊界；三人是預設，不是上限。多人或附來源不等於無限上下文，也不等於每個即興角色都有已查證傳記。

## Presentation checks｜呈現檢查

- A first-time visitor can find the topic prompt, downloads, and language switch.／新訪客能找到開場指令、下載與語言切換。
- An arbitrary-theme example and an explicit two-/five-/six-person request are visible.／看得到任意主題及二／五／六人指定案例。
- Cast changes preserve the existing topic and constraints.／換組保留原題與限制。
- The badge links to the actual workflow; no static “tests passed” or fabricated adoption claims.／徽章連到實際流程，不寫死「測試通過」或捏造採用成績。
- Every evidence claim names its scope; [acceptance criteria](../tests/BEHAVIORAL-ACCEPTANCE.zh-en.md) remain distinct from completed runs.／各項證據標明範圍，[驗收條件](../tests/BEHAVIORAL-ACCEPTANCE.zh-en.md)不冒充執行紀錄。

## Sources

[1] https://github.com/f/prompts.chat — prompts.chat README
[2] https://github.com/anthropics/skills — Anthropic Skills README
[3] https://docs.github.com/en/repositories/creating-and-managing-repositories/best-practices-for-repositories — GitHub repository best practices
