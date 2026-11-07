# Public-launch review | 公開前調整清單

> Historical v0.3.0 review. The repository has since been renamed **SoWork-Brainstorm-Kit**. See the [v0.4.0 open-cast trial record](../tests/OPEN-CAST-TRIALS.zh-en.md) for new model evidence. Prior findings and the 60-file frozen baseline are preserved. / 本文為v0.3.0歷史檢查；新命名與實測另見連結，不回寫原稽核。

**Review baseline / 稽核基準：** v0.2.0, commit `81d8720c9a6258a42ad86deb5dd59ad501531176`.

**Coverage / 範圍：** All 60 tracked baseline files were inspected and their hashes independently matched. This includes the complete generated text pack, all 31 method cards, nine persona profiles, four casts, templates, examples, build/validation code, and repository policies. The sanitized [per-file record](reviewed-files.json) retains paths, hashes, line ranges and findings. / 已逐檔檢查基準版全部 60 個追蹤檔案，並獨立核對雜湊；不是只看 README。逐檔紀錄保留相對路徑、雜湊、行號與發現，不包含本機操作資訊。

## Executive recommendation | 先說結論

**Share this as an English/Traditional Chinese public preview—not as a production-validated or fully licensed open-source product.** The bilingual edition and confirmed packaging defects have been addressed in v0.3.0. The remaining priorities are a clear owner-selected reuse license, real-platform acceptance, and final approval of branding/persona scope and A01. / **可以用「中英公開試用稿」分享，但不要宣稱已通過正式平台驗收或已完成開源授權。** v0.3.0 補齊英文版並修正已確認的封裝缺陷；接下來優先處理授權、實際平台驗收、正式命名／人物範圍，以及 A01 核稿。

This review distinguishes verified defects, packaging mitigations, unrun behavior tests, recommendations and owner decisions. It is not a legal opinion, a comprehensive security audit, or proof of model quality. / 本清單將已確認缺陷、封裝緩解、未執行的行為驗收、建議與作者決策分開；不是法律意見、完整安全認證或模型品質證明。

## 1. Completed in this edition | 本次已調整

### D01 — Complete English coverage | 完整英文體驗

**Status: addressed in the source package.** Added an English landing page and Chinese counterpart, complete English facilitator/teaching guides, all 31 method cards, nine personas, four casts, examples and templates. Stable IDs, source URLs, evidence statuses and cast membership are checked across languages. / **狀態：已補齊來源與封裝。** 不只是翻 README；主持、教學、方法、人物、組合、例子、模板均有英文對應，並核對 ID、來源、證據標籤與成員一致性。

Use separate runtime downloads: `START-HERE.en.txt` and `START-HERE.txt`. Use the [bilingual map](bilingual-map.md) for comparison rather than pasting two complete language packs into one prompt. / 運行包分成英文與繁中兩份，中英對照看索引文件，不把完整指令雙份堆在同一對話。

**Boundary:** translation/structural checks do not prove that either language behaves well in a model. / **界線：** 翻譯和結構核對不等於模型行為已通過。

### D02 — License notice travels with the download | 授權狀態隨附件保留

**Status: information omission fixed; licensing decision still open.** Both generated packs now include the existing LICENSE notice. No new MIT, CC, commercial-use or redistribution permission has been invented. / **狀態：補上遺漏說明；授權本身仍未定案。** 兩份包均附既有 LICENSE 內容，未擅自增加 MIT、CC、商用或再散布授權。

### D03 — Detached links retain their context | 單檔連結保留來源位置

**Status: path-generation defect fixed.** Relative links from persona and method documents are rewritten to correctly located, version-pinned repository files. Generated `.txt` packs—not just `.md` sources—are checked for unresolved relative Markdown links. / **狀態：已修正路徑生成。** 人物來源不再誤指到方法來源，方法索引也不再錯落到 repo 根目錄；產出的 TXT 也納入檢查。

These links are supplemental: all method and persona content needed for the ordinary session remains inside the language pack. A specific AI platform's URL retrieval is still unverified. / 連結是補充，普通會議所需的方法與人設仍在單檔內；不因此宣稱某個 AI 平台一定能讀取網址。

### R01 — Reduce human-homework bleed | 降低教學指令滲回懶人模式

**Status: packaging mitigated; behavior still requires testing.** The default packs no longer embed the entire human-teaching protocol. They contain a compact opt-in teaching summary and a mode guard before every reference card. Full teaching documents remain in the repo. / **狀態：已降低封裝風險，實際行為待測。** 預設包移除整份真人教學規約，只保留明確選用摘要，每張參考卡前加模式標示；完整教學檔仍保留。

“Teach me” is not a universal mode switch: it must mean practicing brainstorming or facilitating a real-human workshop. Ordinary help requests remain AI-led co-creation. / 「教我」必須明確指練習動腦或帶真人工作坊，一般求助不自動變作業模式。

### R03, R08 — Native-English controls and consistent examples | 指令與例子一致

**Status: source fixes applied.** Removed the English `you decide` cast alias that could conflict with choosing a direction in an existing session. The command should continue the current topic/cast unless the user explicitly delegates cast selection. Templates are optional/AI-prefilled, and the “more practical” example no longer deletes recording that was never proposed. / **狀態：已修正文字來源。** 「你決定」不應突然重設人物；準備表是可選、由 AI 先填；例子只刪前文真的存在的依賴，不憑空加入錄音再刪掉。

### R06 — Safety does not depend on teaching mode | 安全規則不依賴教學模式

**Status: shared guidance added.** Both facilitator protocols now treat source text, attachments and role dialogue as data rather than new authority; minimize sensitive information; and require authorization before actual external sending, publishing, inviting or data transfer. No provider-confidentiality guarantee is implied. / **狀態：已補入兩版共用主持規約。** 不把來源或角色台詞當成新授權，不索取不必要敏感資料，實際外部操作需先確認範圍並取得同意；不保證 AI 供應商的保密條件。

## 2. Highest-priority remaining work | 公開前最重要待辦

### P0 / O01 — Choose the reuse terms | 決定授權與可用範圍

**Owner decision—not automatically changed.** LICENSE still says the project-wide reuse terms are pending. Decide what people may do with original instructions, translations and code: use, modify, redistribute, and use commercially. Credit and third-party exclusions also need clear treatment. / **需要作者決定，這次未擅自更改。** 要明確說自撰指令、翻譯與程式碼可否使用、修改、再散布、商用，以及署名和第三方排除範圍。

GitHub explains that a publicly visible repository is not automatically an open-source license grant; see [GitHub licensing guidance](https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/licensing-a-repository). / GitHub 官方文件說明，公開可讀不自動等於已選定開源授權。這裡只標示決策缺口，不代替法律判斷。

**Until settled:** say “public preview,” retain the notice in downloads, and do not advertise MIT/CC, unrestricted reuse or rights clearance. / **未定案前：** 用公開試用稿定位，附件保留聲明，不宣稱 MIT／CC、無限制再利用或已完成權利清查。

### P0 / R02 — Run actual multi-turn acceptance | 完成真實多輪驗收

**Not passed.** Prior ChatGPT access stopped at human verification. Static tests, translated documents, fictional examples and a sandbox response cannot establish successful ChatGPT web behavior. / **尚未通過。** 先前 ChatGPT 存取停在人機驗證；CI、文件、虛構示例或沙盒不能取代網頁端實際對話。

Freeze the release, record the attachment/URL entry, platform/model and actual outputs, then test both languages against [the acceptance cases](../tests/BEHAVIORAL-ACCEPTANCE.zh-en.md). At minimum check start, automatic cast, custom people, cross-improvements, continue, more practical, you decide, 635 adaptation, explicit teaching, and stop. / 固定版本與入口、平台／模型及真實輸出；至少驗證開始、自動組人、自選人物、交叉接球、繼續、更務實、你決定、635 改編、真人教學與停止。

Do not publish a success percentage from a handful of cases or describe packaging checks as an AI quality score. / 不用少量案例推整體成功率，也不把封裝測試說成 AI 品質分數。

### P1 / O02 — Approve the English cast names | 核准英文組名

The preview uses these proposed localizations, with Chinese names and IDs retained. They are editorial names, not factual rankings. / 本試用稿先採下列英文命名提案，保留繁中名稱與 ID；不是人氣或美貌排名。

| 中文 | English preview label | 重點 / Intent |
|---|---|---|
| 古今綜合組 | Across the Ages | 跨時代互補 / Cross-era perspectives |
| 熱門搖滾組 | Rock Legends | 反常規與參與 / Reinvention and participation |
| 美美女組 | The Glamour Council | 體驗、結盟、編輯 / Experience, alliances, editing |
| 殘暴組 | The Ruthless Strategists | 犀利取捨，不是暴力 / Sharp trade-offs, not violence |

If changing labels later, keep stable IDs and existing aliases so examples and catalogs do not drift. / 日後改名時保留穩定 ID 與舊別名，避免例子和資料失去對應。

### P1 / O03, R05 — Decide persona scope and preserve evidence limits | 人物範圍與證據界線

All persona capabilities are editorial fiction. Some short background references were checked only through official search excerpts; Yang Guifei's museum API supports an artwork title, not modern professional expertise. Do not promote those tags into full biographical verification. / 人設能力全屬編輯虛構，部分背景只核對官方檢索摘要；楊貴妃的 API 只核對畫作題名，不證明現代專長。不可把證據標籤升級成完整傳記驗證。

Approve the roster and commercial positioning before broader promotion. Non-endorsement notices clarify presentation; this review does not decide legal rights or replace qualified advice when needed. / 擴大推廣前確認人物與商業定位的可接受範圍；非背書聲明只釐清呈現方式，本稽核不判定權利是否合法或充分。

### P1 / O04 — Confirm A01 | 核對「1 分鐘想十個策展人」

A01 is still a draft adaptation based on the exercise name; the original workshop was not fully recovered. Confirm what “curators” means and the intended flow, keep the draft label, or exclude it from a future formal edition. / A01 仍是依名稱整理的草稿，沒有完整還原原課程。需核對策展人的意思與流程；未確認前保留草稿標示，或不放入未來正式版。

## 3. Next improvements, not launch guarantees | 後續優化，不是本次保證

- **R04 — Release integrity:** anonymously download both release assets and compare their hashes at publication; provide clear filenames and checksums. Source URL strings alone are insufficient. / 發佈時匿名下載兩份資產並比對雜湊；不能只看 README 字串。
- **R05 — Claim-level provenance:** replace repeated seven-source lists with more precise per-card claims when the author reviews the methods. Preserve original URLs and caveats. / 作者核稿時再細化逐卡主張與來源對應，不只是每卡重列相同七筆來源。
- **R07 — CI/security hardening:** consider commit-pinned Actions, independent secret scanning and Git-history checks. Existing CI is static packaging verification, not comprehensive security certification. / 可再固定 Actions commit、加入獨立秘密與歷史掃描；現有 CI 不是全面安全認證。
- **Authorship/account:** the repo is currently hosted at `contentincubator2-ops/cj-brainstorm-kit`. A collaborator invitation is not an ownership transfer. If the long-term public URL should use `cj-wang-sowork`, separately authorize and complete an owner transfer before finalizing permanent campaign links; sharing a clearly labeled preview does not require doing that immediately. See [GitHub transfer guidance](https://docs.github.com/en/repositories/creating-and-managing-repositories/transferring-a-repository). / repo 目前不在 CJ 帳號名下；協作邀請不等於轉移。若要用 CJ 的永久網址，需另行授權轉移，不在本次自動執行。

## 4. What to say publicly | 公開時怎麼說

**Safe preview framing:** “A text kit for fictional famous-persona brainstorming, with separate English and Traditional Chinese editions. The AI does the first round; users can continue with short controls. Platform behavior is still being tested.” / **適合試用稿的說法：** 「虛構名人視角動腦文字包，提供中英兩版，由 AI 先想，用戶用簡短指令接著走；平台行為持續驗證。」

**Avoid:** “nine autonomous agents,” “historically accurate minds,” “official celebrity collaboration,” “works on every AI tool,” “31 independent creativity theories,” “fully open source,” or “ChatGPT tested and approved” without the corresponding evidence/decision. / **不要說：** 九個自主代理、歷史本人思想、官方名人合作、所有 AI 都可用、31 種獨立理論、已正式開源、ChatGPT 已驗收，除非有相應證據或決策。

A paired [sharing-copy draft](launch-copy.zh-en.md) is included. It is draft text, not a post already published. / 已附中英分享文案草稿，不代表已發文。

## 5. Evidence boundary | 證據範圍

- **Verified baseline:** 60 paths and hashes matched; the frozen source's 10 static checks passed and its rebuilt text pack matched the committed artifact. / 基準版 60 檔路徑與雜湊已核對，10 項靜態檢查通過，重建包與原包一致。
- **This edition:** added English counterparts and structural regression checks, a detached licensing notice, version-pinned links, mode-scoped cards and shared safety guidance. Build/CI and anonymous asset integrity are recorded at publication; none establishes model quality. / 本次新增英文與結構回歸檢查、授權聲明、固定版本連結、模式標示與安全規則；建置／CI 和匿名下載完整性在發佈時核對，不等於模型品質。
- **Not established:** real ChatGPT multi-turn acceptance, other-platform compatibility, comprehensive rights clearance, all external reference pages' current availability, or an exhaustive security/history audit. / 尚未證明真實平台多輪相容、完整權利清查、所有外部來源目前可讀，或全面安全／歷史掃描。
