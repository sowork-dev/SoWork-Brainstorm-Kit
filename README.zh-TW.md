# SoWork-Brainstorm-Kit｜AI 名人動腦團

### 你出題，AI 組任何主題的名人團。點子先來，不必交作業。

**[English](README.md) · 繁體中文**

[![Validate text bundle](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/actions/workflows/validate.yml/badge.svg)](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/actions/workflows/validate.yml)
**v0.4.0 · 公開試用稿 · 純文字工作流程**

丟一句題目，讓 AI 主持一場動腦會議。你可以要求**任何主題或組別**、指定想找的人，也可以全部交給 AI 配組。它負責提案、讓不同視角互相挑戰改進，再推薦方向；你只需說**「繼續」「換組」「你決定」**。

**不是只能從九人、四組裡選。** 內附人物與組別只是起手範例。要一人、兩人、五人、六人以上都可以指定；**三人是預設，不是上限**。新增人物採虛構的編輯視角，不代表新增了已查證傳記。實際人數與展開深度仍受 AI 工具的上下文及回覆長度限制。

[直接開始](#直接開始) · [可以拿來做什麼](#可以拿來做什麼) · [示例與實測證據](#示例與實測證據) · [常見問題](#常見問題) · [發展路線](docs/roadmap.zh-en.md)

> 角色是同一 AI 對話中的虛構演繹，非本人、史實引言、背書或獨立部署的代理。這不是原生插件。授權為 [MIT](LICENSE)（第三方素材除外）；ChatGPT 網頁端驗收尚未完成。

## 目錄

- [為什麼用這套](#為什麼用這套)
- [直接開始](#直接開始)
- [可以拿來做什麼](#可以拿來做什麼)
- [自己組團，不必先知道完整名單](#自己組團不必先知道完整名單)
- [一句話控制會議](#一句話控制會議)
- [一輪應該拿到什麼](#一輪應該拿到什麼)
- [示例與實測證據](#示例與實測證據)
- [常見問題](#常見問題)
- [檔案導覽](#檔案導覽)
- [貢獻與驗證](#貢獻與驗證)
- [來源、致謝與權利](#來源致謝與權利)

## 為什麼用這套

- **先解題，不先研究怎麼寫提示詞。** 給題目後，AI 選方法並直接提案，不把需求表丟回來。
- **不是換名字講同一套話。** 各人有不同任務，得針對具體方案提出質疑、接球與改版。
- **換人不重開會。** 更換主題組或成員時，保留題目、限制與已有進展。
- **不只發散，也幫你判斷。** 比較方向、說明推薦與假設，再展開一個可試的小步驟。
- **中英分包，不讓提示詞加倍。** 英文、繁體中文各有完整文字包，以穩定 ID 對照方法與人物。

內附 **31 張方法參考卡**，包含相近變體，不是 31 種完全獨立理論。預設 **LAZY_COUNCIL** 由 AI 自己執行發想；只有你明確要求練習，才進入 **TEACHING** 真人教學模式。

## 直接開始

**試用文字包不用本機安裝、Python 或 API key。** 你需要一個確實能讀取文字附件的 AI 工具／帳號；該工具本身的存取條件仍適用。

1. 下載一份 v0.4.0 語言包：
   - **[繁體中文 · START-HERE.txt](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/releases/download/v0.4.0/START-HERE.txt)**
   - **[English · START-HERE.en.txt](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/releases/download/v0.4.0/START-HERE.en.txt)**
   - [版本說明與下載檔](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/releases/tag/v0.4.0)
2. 新開 AI 對話，上傳**一份**完整語言包，請 AI 確認真的讀到內容，而不只是看到檔名。
3. 貼下方這段，換成你的題目：

```text
請使用附件 SoWork-Brainstorm-Kit 的 LAZY_COUNCIL 懶人名人動腦模式。
我的題目：社區書店怎麼在小預算下，讓客人願意持續回來？
請你配具名且互補的人物、選方法，直接提案，
讓角色針對彼此的具體點子質疑改進，再推薦一個方向。
非關鍵缺口先標示合理假設；不要叫我先寫五到十個點子。
```

還沒有題目？只說**「開始」**，AI 應只問一個簡短的題目問題，不讓你先填表。

**用過舊版？** 請重新下載，另開對話或明確取代舊附件與指令。Repo 更新不會自動替換已載入的檔案。[使用說明](SETUP.zh-TW.md)另列附件與網址路徑。若版本下載檔尚未上架，可先取 repo 內的[繁中文字包](START-HERE.txt)或[英文文字包](START-HERE.en.txt)，並檢查檔頭版本。

## 可以拿來做什麼

以下是**示範輸入**，不是宣稱已產生的成果：

| 想解的問題 | 可以這樣開場 |
| --- | --- |
| 行銷活動 | 「幫我組太空科學家組，想低預算補充包活動。你選五位具名人物。」 |
| 產品構想 | 「請 Ada Lovelace 和達文西開虛構設計會議，想不看螢幕的親子遊戲，只要兩人。」 |
| 內容角度 | 「組文藝復興藝術家團，發想日常創意系列，你決定人選。」 |
| 體驗設計 | 「組台灣主廚團，設計平價、容易參與的社區美食活動。」 |
| 方案壓力測試 | 「用六個虛構視角挑戰這份上市計畫，保留我的預算與期限。」 |
| 單人動腦 | 「只用 David Bowie 的虛構再造視角，自己提案、自我質疑再改進。」 |

不必先認識整個領域的人物。AI 應替你選具名且互補的人，不把組名單的作業交回來；安全與事實不確定性仍須如實處理。

## 自己組團，不必先知道完整名單

指定**主題、人物、人數**，或任意組合：

```text
幫我組女性科學家團，人物你挑，直接處理剛剛的題目。
只要楊貴妃和秦始皇，不要再補第三人。
我要五位電影導演，不是內附預設組。
擴成六人，保留我已經指定的人。
換成建築師組，但題目、預算和期限不變。
```

內附名單以外的人物，採清楚標示的**虛構編輯思考角色**。不可因此編造名言、研究成果、生平或本人立場。無法查證時，只能當工作坊虛構設定，不能包裝成有來源的傳記；身分有歧義才需釐清。

### 四組起手範例，不是完整菜單

| 組別 | 起手人物 | 工作視角 |
| --- | --- | --- |
| **古今綜合組** · Across the Ages | 秦始皇 · 楊貴妃 · David Bowie | 規則 · 體驗 · 身份重構 |
| **熱門搖滾組** · Rock Legends | David Bowie · Freddie Mercury · Joan Jett | 再造 · 群眾參與 · DIY 啟動 |
| **美美女組** · The Glamour Council | 楊貴妃 · Cleopatra VII · Coco Chanel | 感官 · 互惠結盟 · 精準刪減 |
| **殘暴組** · The Ruthless Strategists | 秦始皇 · 成吉思汗 · 拿破崙 | 尖銳取捨 · 分散節點 · 壓力測試 |

英文組名是試用版在地化命名；保留繁中別名與穩定 ID。這些是編輯式主題，不是即時人氣榜、外貌排名、歷史人格定論，也不倡導暴力或脅迫。[人物指南](personas/README.md) · [中英對照](docs/bilingual-map.md)

## 一句話控制會議

| 你說 | AI 應該做什麼 |
| --- | --- |
| **繼續** | 沿推薦方向新增機制或具體細節，不只重講。 |
| **換組／換掉某人** | 更換指定人物，保留題目和限制，直接接續發想。 |
| **改成五人／只要兩人** | 尊重指定人數，不自動補回三人。 |
| **更大膽** | 改核心假設或互動機制，不只加浮誇形容詞。 |
| **更務實** | 縮減成本、依賴和步驟。 |
| **第 2 個** | 展開該方向，不重開需求訪談。 |
| **你決定** | 直接選方向並具體展開，不重設人物或把選擇丟回來。 |
| **教我練習動腦** | 明確切入 TEACHING，才等待真人練習。 |

一般使用不需要先交五到十個點子。簡短追問後，題目、已知限制、選定方向與現有名單都應保留下來。

## 一輪應該拿到什麼

預期流程：**組團 → 提案 → 具體質疑與改版 → 可比較方向 → 推薦**。

- 具名且分工不同的人物，不是每人一篇傳記。
- 每位一至兩個具體點子，說清楚機制。
- 多人回合至少兩則針對具體提案的交叉改進，不只是「我同意」。單人要求則改用自我質疑、修訂，不虛構額外發言者。
- 通常整理三個可比較方向、推薦一個，標出尚未查證假設。
- 留幾個簡單指令，讓你不必再交新點子也能接續。

人數增加時，可能需要縮短每人發言或分輪處理。這不是無限上下文、無限輸出、已驗證商業成效或真人專家共識的承諾。

## 示例與實測證據

**作者示範與實際執行紀錄分開看：**

- **作者編寫的虛構示例：** [繁中共創示例](examples/persona-council.md) · [English walkthrough](locales/en/examples/persona-council.md)。用來說明預期格式，不是模型執行逐字稿。
- **模型執行紀錄：** [繁中開放組隊實測](examples/test-runs/open-cast-zh.md) · [English open-cast run](examples/test-runs/open-cast-en.md)。引擎為 **GPT-6.1-sol，透過 Hermes provider 執行提示評估**，不是 ChatGPT 網頁版或附件上傳驗收。精確輸入、輸出、來源版本與限制以各紀錄為準；有紀錄不等於全面通過。
- **驗收條件與範圍：** [測試說明](tests/README.zh-TW.md) · [行為案例](tests/BEHAVIORAL-ACCEPTANCE.zh-en.md) · [公開前檢查](docs/public-launch-review.zh-en.md)。

本次小樣本由另一個AI任務判讀：七輪符合預期；中文最後一輪部分符合，方案具體，但未顯示五人姓名，且稿件仍偏密。這不是真人評分或通用成功率。[完整判讀](examples/test-runs/review.zh-en.md)。

頁首徽章反映 repo 的**靜態驗證流程**，不是 AI 品質評分。**ChatGPT 瀏覽器驗收仍未完成：存取卡在人機驗證。** 模型提示評估不能證明網頁附件讀取、repo 擷取或其他產品／帳號上的等同行為。

## 常見問題

**這是 ChatGPT／Claude 原生插件或代理框架嗎？**

不是。這是可攜式純文字工作流程。上傳指引不等於安裝插件、授權外部工具或建立背景工作程序。見[相容性](docs/compatibility.md)。

**角色是獨立代理，或真的找來本人嗎？**

都不是。同一個 AI 在同一對話模擬不同虛構視角，不是各自部署的代理、真人與會、真實投票或本人背書。

**只能九人、四組或三人嗎？**

不是。任何主題都可提出，其他人物可以指定，也可以讓 AI 選。要一、二、五、六人以上都可以；三人只是預設。實際上下文、回覆長度、安全限制與資訊不確定性，可能需要縮小或分輪，但不代表只有四個選項。

**會不會又叫我自己想點子？**

預設 LAZY_COUNCIL 不會；AI 負責提案與改進。只有明確選用 [TEACHING](TEACHING.md)，才做真人練習。

**只貼 GitHub 網址可以嗎？**

必須是 AI 真能取到必要檔案，並確認實際讀過哪些內容。首頁不等於完整工具包；取不到就改上傳完整附件。見[使用說明](SETUP.zh-TW.md)。

**我的對話保密嗎？**

工具包不能替 AI 供應商保證保密、保存設定或帳號政策。優先用虛構、匿名題目；不要在公開 Issue 或 PR 放客戶資料、個資、私人網址、帳密或原始私人對話。見[安全與隱私](SECURITY.zh-TW.md)。

**可以再散布、商用嗎？**

可以。原創內容採 [MIT 授權](LICENSE)；第三方方法名稱、商標、網站與原教案仍屬各自權利人，來源見 [SOURCES.md](SOURCES.md)。虛構角色只是編輯用的思考視角，不代表或背書所指涉的真實人物。

## 檔案導覽

| 區域 | 繁體中文 | English／共用 |
| --- | --- | --- |
| 開始與設定 | [文字包](START-HERE.txt) · [使用說明](SETUP.zh-TW.md) | [Text pack](START-HERE.en.txt) · [Setup](SETUP.md) |
| 主持規約 | [主持規約](FACILITATOR.md) | [Protocol](locales/en/FACILITATOR.md) |
| 方法 | [索引](methods/index.md) · [來源](SOURCES.md) | [Index](locales/en/methods/index.md) · [Sources](locales/en/SOURCES.md) |
| 人物與起手組 | [指南](personas/README.md) · [組合](personas/packs.json) · [來源](personas/SOURCES.md) | [Guide](locales/en/personas/README.md) · [Sources](locales/en/personas/SOURCES.md) |
| 會議模板 | [準備](templates/meeting-brief.md) · [狀態](templates/session-state.md) · [成果](templates/outcome.md) | [Brief](locales/en/templates/meeting-brief.md) · [State](locales/en/templates/session-state.md) · [Outcome](locales/en/templates/outcome.md) |
| 品質與方向 | [測試](tests/README.zh-TW.md) · [更新紀錄](CHANGELOG.zh-TW.md) | [中英對照](docs/bilingual-map.md) · [發展路線](docs/roadmap.zh-en.md) · [公開呈現研究](docs/repository-presentation.zh-en.md) |

## 貢獻與驗證

歡迎**可重現的小型行為回報、翻譯修訂、有來源的方法更正與聚焦測試**。先看[貢獻方式](CONTRIBUTING.zh-TW.md)、[社群守則](CODE_OF_CONDUCT.md)，或[開一張 Issue](https://github.com/sowork-dev/SoWork-Brainstorm-Kit/issues/new/choose)。用虛構案例即可，不要上傳私人工作會議。

本機維護使用 Python 3.10+，標準函式庫即可：

```sh
python3 scripts/build.py
python3 scripts/validate.py
```

建置會分別產出兩個語言包；驗證檢查包與來源一致性、ID、連結、語言涵蓋及常見敏感模式，**不代表 AI 品質或平台驗收通過**。實際行為證據應另行記錄。[發展路線](docs/roadmap.zh-en.md)列優先順序與驗收門檻，不是交付日期承諾。

## 來源、致謝與權利

概念與產品方向：**CJ Wang**。[方法來源](SOURCES.md)與[人物來源](personas/SOURCES.md)分別列示。公開背景資料與作者創造的思考機制不同；即興對話不是歷史證據。不可編名言、大量模仿受版權保護作品，也不能把提案寫成已發生的活動或成果。

[公開資料政策](docs/sanitization-policy.md) · [安全](SECURITY.zh-TW.md) · [MIT 授權](LICENSE)
