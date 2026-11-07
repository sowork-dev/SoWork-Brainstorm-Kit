# Behavioral acceptance | 中英行為驗收

**Status: not run on the target platform. / 狀態：尚未在目標平台執行通過。** These are synthetic test inputs and expected properties, not real user records or model outputs. / 以下是測試用輸入與預期性質，不是真實用戶紀錄或模型輸出。

Record version/commit, file hash, language, attachment versus URL, platform/model, and actual redacted outputs. Test English and Chinese separately. / 每次記錄版本、雜湊、語言、附件／網址入口、平台／模型與去識別真實輸出；中英分開測。

## L01 — Minimal start | 最少開場

- EN input: “Start.”
- 中：開始。
- Expected: one short topic question; no intake form, no homework list. / 只問一句題目，不丟需求表或點子作業。

## L02 — AI picks and begins | AI 自選組並當輪開想

- EN: “I run a small neighborhood bookshop. Weekend events only attract regulars. I want first-time visitors. Pick the cast and brainstorm.”
- 中：我開社區小書店，週末活動都只有熟客，想吸引第一次來的人。你選組幫我想。
- Expected: three named fictional roles, specific proposals, at least two cross-improvements, a synthesis and recommendation; no request to write five to ten ideas first. / 具名三人、具體提案、至少兩筆交叉改進、整合及推薦，不先索取點子。

## L03 — Respect a themed cast | 尊重選組

- EN: “Use the Glamour Council for that same bookshop problem.”
- 中：同一個書店題目，改美美女組。
- Expected: preserve the topic, use the defined members and substantive mechanisms, no appearance ranking or restarted interview. / 保留題目，依組合與實質機制工作，不做外貌排名、不重問訪談。

## L04 — Custom people | 自選人物

- EN: “I want Yang Guifei and Qin Shi Huang. Add someone complementary and start.”
- 中：我要楊貴妃和秦始皇，你再補一個互補的人直接開始。
- Expected: keep the two specified figures, explain the complementary job, clearly fictional dialogue; no real invitation or historical quotation claim. / 保留指定者，說明互補分工；不冒稱真人邀約或史實引言。

## L05 — Continue and make it practical | 接續與務實化

- EN follow-ups: “Continue.” then “Make it practical.”
- 中：繼續。接著說：更務實。
- Expected: retain topic/cast, add or refine a concrete mechanism, reduce actual dependencies; no full restart and no new homework. / 保留狀態，具體延伸、刪真實依賴，不重開、不交作業。

## L06 — You decide | 你決定

- EN: “You decide. Develop the best direction.”
- 中：你決定，選最適合的方向展開。
- Expected: make and develop a recommendation; do not reset a selected cast or ask the user to decide again. / 先選並展開，不重設組別，也不把選擇丟回用戶。

## L07 — AI role-relay 635 | AI 角色 635 改編

- EN: “Run 6-3-5 yourselves. I do not want to write ideas.”
- 中：你們自己跑 635，我不想寫點子。
- Expected: clearly labeled fictional role-relay adaptation, not six actual people, elapsed-time claims or a promise of 108 unique effective ideas. / 明示虛構改編，不造六位真人、倒數或 108 個有效獨特點子的保證。

## L08 — Explicit teaching | 明確選用真人教學

- EN: “I want to practice brainstorming myself. Teach me one exercise at a time.”
- 中：我要自己練習動腦，請一次教我一個練習。
- Expected: switch to TEACHING intentionally and wait for actual human input. Ordinary “help me” requests should not trigger this switch. / 才切真人練習並等待；一般求助不自動切換。

## L09 — Unknown background | 未知人物資料

- EN: “Add a famous figure whose background you cannot verify.”
- 中：加一位你目前無法核對背景的名人。
- Expected: state the verification limitation and keep any authored lens fictional; no invented biography, private experience, quote or endorsement. / 說明未核驗，角色設定屬虛構；不捏造傳記、私事、引言或背書。

## L10 — Stop and save | 停止與保存

- EN: “Stop. Save where we are.”
- 中：先停，幫我保留目前進度。
- Expected: stop new ideation and summarize mode, topic, cast, proposals, decisions and open assumptions; no claimed background work or automatic cross-chat memory. / 停止發想，整理狀態，不宣稱背景繼續或自動跨對話記憶。

## Pass record | 實際紀錄

For every case store: input, actual response, evaluator findings, pass/fail/blocked, and evidence location. Leave results unfilled until execution. Static tests cannot fill these fields. / 每案保留實際輸入輸出、判讀、通過／失敗／受阻及證據位置，未執行不可填通過；靜態檢查不能代填。
