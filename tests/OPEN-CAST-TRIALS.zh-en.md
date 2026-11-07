# Open-cast model trials | 自由組隊實測

## What actually ran | 實際做了什麼

On November 7, 2026, two scripted conversations were run against `gpt-6.1-sol` through the Hermes `openai-codex` provider adapter. Each conversation has four real user/assistant turns: **8 completed model responses**, not eight independent user studies. The full corresponding text pack was placed in the first user message; later calls replayed the actual previous outputs. No external tools were supplied.

2026年11月7日，使用 Hermes 的 `openai-codex` provider 呼叫 `gpt-6.1-sol`，執行繁中、英文各一段四輪對話，共 **8 次真實模型回覆**，不是8場獨立使用者研究。第一輪帶入完整對應語言包，後續重送實際對話歷史；模型沒有外部工具。

- [繁中完整紀錄](../examples/test-runs/open-cast-zh.md) · [English complete transcript](../examples/test-runs/open-cast-en.md)
- [Frozen cases and expectations / 預先固定輸入及預期](open-cast-cases.json)
- [Runner / 可重跑程式](../scripts/run_open_cast_trials.py)
- Raw machine-readable results: [中文](../examples/test-runs/open-cast-zh.json) · [English](../examples/test-runs/open-cast-en.json)
- [Separate assessment / 獨立判讀](../examples/test-runs/review.zh-en.md)

No assistant messages were written by hand or replaced after execution. The readable transcript preserves the exact assistant text; surrounding headings, metadata, and assessment are editorial. The conversations concern a synthetic library activity; no real library, participant, invitation, purchase, pilot, or outcome is implied.

未人工補寫或替換 AI 回覆；可讀版保留實際文字，僅另加標題、執行資料與評估。題目為測試用圖書館情境，不代表真實客戶、青年參加者、邀約、採購或已辦活動。

## Coverage | 覆蓋範圍

| Conversation | Executed sequence | What it probes |
| --- | --- | --- |
| 繁中 | 自選海洋探險組 → 僅兩位指定者 → 加入三位成為五人 → 你決定、務實一頁方案 | New theme, outside-catalog casting, exact two, exact five, addition, topic/constraint retention, low-effort continuation |
| English | Five named Quiet Rebels → replace one member → five new Ocean Explorers → You decide | Five outside-catalog people, single-member replacement, whole-group swap, retained constraints, practical recommendation |

The four starter themes and nine stored profiles are not the allowed set. These trials test a small set of open-cast requests; they cannot prove that every possible theme, person, cast size, model, language, or conversation length works. “Open cast” is not a claim of unlimited model context.

四組與九位只是範例，並非允許清單。本次覆蓋少量自由組隊請求，不保證所有主題、人數、人名、語言、模型或長對話皆正確；也不承諾無限 context。

## Evaluation method | 如何判讀

Expectations were stored before generation. Review each actual turn for the requested roster change, topic and budget/time/staff constraints, meaningful idea mechanisms, concrete cross-improvements, low user burden, and fictional/non-endorsement boundaries. Mark **pass / partial / fail / not observable** with reasons; do not score usefulness by counting keywords. Do not infer hidden persona state from a response that does not expose it. No independent human user acceptance or blind human quality rating was collected.

先固定每輪預期，再閱讀實際回覆判斷名單、限制、具體玩法、交叉改進、操作負擔與虛構界線。採 **通過／部分／失敗／不可觀測** 並附原因，不以關鍵字數量充作品質分數；回覆未呈現的內部角色狀態不可推論。尚無獨立真人驗收或盲評。

## Setup attempts and blockers | 前置嘗試與受阻紀錄

- Standalone Codex CLI `0.133.0` was tried with `gpt-5.5`, then a model present in the local catalog, `gpt-6.1-sol`. Both requests were rejected as unsupported for that CLI/ChatGPT-account route. They produced **no brainstorming outputs** and are not counted among the eight completed turns. No CLI update or credential copying was performed.
- A separate tiny smoke request through the installed Hermes provider adapter returned `READY` on `gpt-6.1-sol`. The eight trials then used that working adapter, not the rejected CLI route. One initial helper invocation had an interpreter-path error before a model call; it is not a model trial.
- ChatGPT website preflight reached a Cloudflare human-verification screen. No attachment upload or conversation occurred. See the [preflight screenshot](../examples/test-runs/chatgpt-preflight-blocked.png). No attempt was made to bypass the challenge.

- 獨立 Codex CLI 的兩個模型請求均被該路由拒絕，沒有產生動腦內容，未算入8輪；未升級CLI、未搬移憑證。
- 改用已安裝 Hermes provider 後，極小 smoke 回覆 `READY`，再用同一路由跑完整案例。另有一次 helper 路徑錯誤，發生在模型呼叫之前，不算模型試驗。
- ChatGPT 網頁仍停在人機驗證，沒有上傳附件或進入對話，不以 provider 試跑冒稱網頁端驗收。

## Reproduce safely | 如何重跑

Normal kit usage requires only a text-reading AI chat. The live-trial runner is optional maintainer tooling and additionally requires an installed Hermes Python environment with authorized credentials. It does not install or modify that environment. Credentials must remain in the provider's secure configuration, never in the repository, CLI arguments, screenshots, Issues, or trial files.

一般使用只需能讀文字的 AI 工具；重跑程式是可選維護工具，另需已安裝的 Hermes Python 環境與有效授權。程式不安裝或改寫該環境；憑證不寫入 repo、命令參數、截圖、Issue 或實測檔。

```sh
# In an existing authorized Hermes Python environment:
python scripts/run_open_cast_trials.py --output-dir ./trial-output
```

Use a fresh output directory: the script refuses to overwrite previous trials. Model access, latency, price, and outputs can change. The runner records pack hashes, frozen-case hash, model/provider, UTC timestamps, token usage reported by the adapter, wall time, and exact outputs. Token usage is adapter-reported, not an invoice; monetary cost is unmeasured. Preserve failures and do not silently replace unfavorable outputs. Do not publish transport logs that contain credentials or local runtime information.

使用新的輸出資料夾，程式拒絕覆寫舊紀錄。模型權限、延遲、價格與結果都可能改變。保留套件雜湊、固定案例雜湊、模型／路由、UTC時間、provider回傳token、耗時與完整輸出。token非帳單，未測量金額；失敗亦須保留，不挑好看的回覆取代。

## Separate evidence classes | 不混淆驗收

1. Static package checks: file structure, IDs, links, hashes and prompt markers.
2. These model trials: actual text-generation behavior with full text supplied directly.
3. Native-platform acceptance: ChatGPT website upload, repository retrieval, account permissions and conversation behavior—**still unpassed**.
4. Human usefulness and real activity outcomes—**not measured**.

The [older ten-case platform suite](BEHAVIORAL-ACCEPTANCE.zh-en.md) remains unexecuted as a complete target-platform suite. These new eight responses do not retroactively mark those ten cases passed.
