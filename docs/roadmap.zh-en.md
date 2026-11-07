# Roadmap｜發展路線

[English README](../README.md) · [繁中首頁](../README.zh-TW.md) · [Presentation research／呈現研究](repository-presentation.zh-en.md)

**Direction, not a delivery schedule.** This roadmap distinguishes the public-preview contract from work that still needs evidence or an owner decision. An item here is not a claim that it shipped or passed testing.

**這是方向，不是交期承諾。** 以下區分公開試用的產品要求、仍需證據的工作與作者待決事項；列在此處不代表已上線或已驗收。

## Public-preview contract｜公開試用的產品要求

- One topic starts AI-led proposals; no idea-list homework unless TEACHING is explicitly selected.／一句題目啟動 AI 提案；未明確選 TEACHING 就不交點子作業。
- Any requested theme or group can be assembled with named, complementary fictional perspectives, including people outside the starter catalog.／任意主題可配具名互補的虛構視角，不限內附人物。
- Explicit counts such as one, two, five, or six-plus are respected; three is only the default, subject to actual context/output limits.／尊重一、二、五、六人以上的指定；三人僅預設，仍受實際上下文與輸出限制。
- Cast swaps preserve the topic, constraints, and useful session state.／換組保留題目、限制與有效進度。
- Public background references and fictional editorial roles stay separate; no invented quotations or endorsements.／公開背景與虛構編輯角色分開，不編名言或背書。

## Priority 1 — Make the preview reproducible｜讓試用可重現

**Next evidence work, not a blanket pass claim.／後續證據工作，不是全面通過聲明。**

- Keep English/Traditional Chinese source and built-pack versions aligned, with release assets and matching checksums.／對齊雙語來源、文字包、版本下載檔與校驗碼。
- Evaluate non-starter themes and people, explicit small/large counts, cast replacement, “Continue,” and “You decide” using the [behavioral cases](../tests/BEHAVIORAL-ACCEPTANCE.zh-en.md).／依[行為案例](../tests/BEHAVIORAL-ACCEPTANCE.zh-en.md)檢查非預設主題與人物、指定人數、換人、繼續與你決定。
- Retain sanitized actual outputs, source version, engine/provider, entry route, and failures. Label prompt evaluation separately from browser/file-upload acceptance.／保留去識別化實際輸出、來源版本、引擎／供應商、進入路徑及失敗；提示評估與瀏覽器／附件驗收分開標示。

**Exit gate:** Locally reproducible package checks plus inspectable model-run evidence for the stated cases. Document omissions and failures instead of calculating an unsupported universal success rate.

**門檻：** 可重跑的靜態檢查，加上可檢視的對應模型紀錄；缺測與失敗明列，不推算無依據的整體成功率。

## Priority 2 — Verify real entry paths｜驗證真實使用入口

- Complete a browser attachment session when human verification allows access; do not bypass access controls.／待可正常通過人機驗證後，補瀏覽器附件對話，不繞過存取控制。
- Test repository-URL retrieval separately: record which files were actually read and whether attachment fallback works.／另測網址擷取，記錄真正讀到的檔案與附件替代路徑。
- Add platform-specific compatibility notes only after observing actual behavior.／實際觀察後才新增平台相容性結論。

**Exit gate:** Each supported route has a source version, real outputs, observed limitations, and reproducible steps. ChatGPT web remains unverified until its own route is exercised; model prompt evaluation cannot substitute for it.

**門檻：** 各支援路徑有版本、真實輸出、限制與重現步驟；ChatGPT 網頁路徑未自行實測前，不用模型提示評估代替驗收。

## Priority 3 — Improve useful output, not roster size｜改進成果，不只堆人物

- Collect synthetic reports where roles collapse into generic advice or fail to improve specific proposals.／用虛構案例收集角色同質化、未針對具體提案改進的問題。
- Strengthen count-aware rounds: self-critique for one person, distinct roles for pairs, staged output for larger groups.／改進人數適配：單人自我質疑、雙人明確分工、大組分輪。
- Review bilingual semantic parity, source accuracy, attribution, and the session-state handoff templates.／檢查雙語語意、來源、歸屬及會議狀態交接模板。

**Exit gate:** Targeted before/after cases show the intended improvement without losing topic constraints, increasing user homework, or inventing facts. No performance promise follows from one improved example.

**門檻：** 聚焦的前後案例呈現改進，且不遺失限制、不增加用戶作業、不編事實；單例改善不等於效果保證。

## Owner decisions｜作者待決

- **License:** Choose project-wide redistribution/commercial terms and review third-party boundaries before describing the project as openly licensed. [Current notice](../LICENSE).／**授權：** 決定全庫再散布與商用條款，檢查第三方權利後，才可宣稱開放授權。[現況](../LICENSE)。
- **Community operations:** Confirm a private reporting route before advertising one. Do not publish a response-time SLA without operational capacity.／**社群營運：** 先確認私人通報入口才對外公告；沒有維運能力就不承諾回應時效。
- **Future packaging:** Consider native integrations only after a separate implementation, permission review, and platform acceptance test.／**未來包裝：** 原生整合必須另有實作、權限審查與平台驗收，不能只靠改名。

## Not promised｜目前不承諾

Unlimited context or cast size in one response; real-person participation; autonomous background agents; automatic cross-chat memory; verified historical dialogue; business outcomes; a native plugin; or an MIT/CC license before an explicit decision.

單次無限上下文或人數、真人參與、自主背景代理、自動跨對話記憶、查證過的歷史對話、商業成效、原生插件，以及決定前的 MIT／CC 授權，均不是目前承諾。

## Help move this forward｜如何協助

Read [contribution guidance](../CONTRIBUTING.md)／[繁中貢獻方式](../CONTRIBUTING.zh-TW.md), submit a focused synthetic reproduction or source correction, and identify evidence scope. See [testing](../tests/README.md) and [security](../SECURITY.md). No private client data, account credentials, or raw private sessions are needed.

先看貢獻方式，提交聚焦的虛構重現案例或來源更正，並標明證據範圍。無需客戶資料、帳密或原始私人對話。
