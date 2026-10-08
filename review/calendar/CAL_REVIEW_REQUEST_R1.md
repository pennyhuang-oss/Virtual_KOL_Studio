# CAL_REVIEW_REQUEST_R1 — 2027 KOL 雙款桌曆｜R1 送審請求

- **任務**：TASK-CAL-001／R1（規格確認與 12 位人設選角盤點）
- **Repo**：`pennyhuang-oss/Virtual_KOL_Studio`
- **分支**：`claude/epic-carson-n5w0qu`（未合併 main）
- **固定成果 commit**：`d44360b3043a6b622b6d76f8951e9503c39e4ad2`
- **覆核者**：ChatGPT（規劃主管、獨立覆核）｜**拍板**：Penny｜**執行**：Claude

## 0. 讀取規則

- 只讀下面 §1 列出的檔案，**不要爬整個 repo**（本 repo 有 500KB 以上的歷史文件，2026-08-27 曾一次燒光使用者方案用量）。
- 以 commit `d44360b` 為準；同一分支之後的 commit 只會是本請求檔或你回覆後的修正。
- 請直接在對話裡回覆，由 Penny 轉回給 Claude；不需要寫回 GitHub。

## 1. 要讀的檔案（精確路徑）

| 順序 | 路徑 | 內容 |
|---|---|---|
| 1 | `docs/calendar/README.md` | 檔案地圖、怎麼看選角板 |
| 2 | `docs/calendar/CAL_01_SPEC_EVIDENCE.md` | 規格與證據表 |
| 3 | `docs/calendar/CAL_02_CASTING.md` | 選角比較、12＋2 推薦、整組差異 |
| 4 | `docs/calendar/CAL_02b_CANDIDATES.generated.md` | 18 位客觀欄位（程式產生） |
| 5 | `docs/calendar/CAL_03_ASSET_AUDIT_ROUTE.md` | 素材可用性、缺口、製作路線 |
| 6 | `docs/calendar/CAL_03b_PRINT_TABLE.generated.md` | 24 張主視覺候選的像素／ppi／判定（程式產生） |
| 7 | `docs/calendar/CAL_04_MONTHS_DECISIONS.md` | 暫定月份、待決策、CAL- 議題 |

## 2. 要看的圖（請實際打開看，不要只讀文字）

| 路徑 | 看什麼 |
|---|---|
| `docs/calendar/sheets/CAL_R1_overview_12.jpg` | **12 位主角同版面**（月份順序；每格上＝直式候選、下＝橫式半版候選）→ 判斷整組長相與氣質差異 |
| `docs/calendar/sheets/CAL_R1_candidates_18.jpg` | 18 位候選各 3 張既有圖（含素材 ID）→ 判斷個人吸引力、推薦與落選是否合理 |
| `docs/calendar/sheets/CAL_R1_crops_12.jpg` | 12＋2 位的三種裁切（橫式滿版／橫式半版／直式滿版）＋線圈區（紅）與日期條（藍）→ 判斷裁切、留白、解析度 |
| `docs/calendar/img/vendor/H_2027tpl_xiangyang_28pages.jpg`、`V_2027tpl_xiangyang_32pages.jpg` | 廠商 2027 範本逐頁 → 核對頁序 |
| `docs/calendar/img/vendor/H_2027_feb_grid_TW_holidays.jpg` | 廠商 2027 年 2 月日期素材 → 核對地區與假日 |
| `docs/calendar/casting_board.html`（選讀） | 與上面三張 JPG 同內容的互動版；GitHub 網頁不渲染 HTML，需下載後本機開啟 |

GitHub 網頁看圖的網址格式：`https://github.com/pennyhuang-oss/Virtual_KOL_Studio/blob/d44360b3043a6b622b6d76f8951e9503c39e4ad2/<上表路徑>`

## 3. 已由需求或 Penny 確定、不需再討論的事

- 製作 2027 年桌曆；橫式、直式兩款都做；合作廠商提供免費試做。
- 12 個月份各一位不同的既有人設（不採 6 位各負責兩個月）。
- 人選以亞洲女性人設為主，形象漂亮、性感、甜美；可用現有圖，也可之後用既有 Soul ID 補生成。
- 本輪只盤點：不生成、不花 credits、不下單、不聯絡廠商。

## 4. 已確認事實（摘要）

- 兩款規格與主管基準一致：橫式 200×151 mm、14 張／28 頁；直式 140×200 mm、16 張／32 頁；兩款最後一頁都是不可編輯的條碼頁。
- 編輯器設定：出血四邊 2 mm；橫式安全框上 10 mm，直式安全框 0；不可增減頁；可放 QR code。
- 編輯器已有 2027 範本與 2027 日期素材；日期素材是廠商預製的點陣圖，採台灣假日＋農曆。
- 廠商 2027 範本的頁序：封面 → 每月「照片面＋大格月曆面」×12 → MEMO（橫 2 面／直 5 面，直式含 1 面年曆）→ 條碼頁。
- repo 內 12 主角＋2 備選的原圖**全部是直幅**；沒有任何橫幅原圖。

## 5. 推薦方案（摘要）

- **12 主角（暫定月份）**：1 iris-chen、2 kanon-komori、3 luna-tanaka、4 angel-chiu、5 somi-oh、6 vicky-lin、7 coco-wu、8 mia-huang、9 yuna-kim、10 tammy-chou、11 rin-ayase、12 rainie-hsu。**備選**：wanyin-jiang、sophia-tseng。
- Batch 3 主角之間沒有任何碰撞配對（最近 rin↔kanon 0.02302 > 門檻 0.0220）。
- **製作路線：現有素材為主**——直式滿版＋橫式「半版直幅照片框＋另一半放日期」。24 個主視覺：可直接用 18、需修圖 5、需補生成或取回 1（tammy 橫式）。
- 橫式滿版用現有直幅圖一律不成立（有效 143–239 ppi，只剩頭到胸）。

## 6. 未確認事項

- 免費試做的數量、款式、紙材、截止日、交件方式、可否對外展示（公開頁面沒有任何資訊）。
- 背面是否旋轉 180° 印刷；面 2k−1／2k 是否同一張紙（頁序搭配的前提）。
- 印刷品質「好／標準／差」的數字門檻；RGB 是否自動轉 CMYK；單檔上限（300MB vs 30）。
- 2027 台灣假日逐日核對（例：2/28 週日是否 3/1 補假）。
- 原 11 位之間、原 11 位與 Batch 3 之間沒有臉部量測（iris 與 rainie 需並排目視）。
- Soul ID 只核對 repo 紀錄，未在 Higgsfield 端查驗。
- daily_v2 原圖在 Higgsfield、repo 只有縮圖；是否屬「留用 64 張」未記錄。

## 7. 本輪實際操作與驗證

| 做了什麼 | 結果 |
|---|---|
| 抓兩個商品頁、編輯說明、客製編輯說明、服務條款 | 全部可讀，無受阻 |
| headless 瀏覽器開公開編輯器頁，只讀 GraphQL 回應 | 取得兩款的頁數、出血、安全框、DPI 設定、2027 日期素材清單 |
| 下載並渲染範本 SVG（橫 8385、8364；直 8404） | 讀出實際頁序 |
| 比對線上型錄 `kols.html` 與 repo 副本 | 逐位元組相同（38 位） |
| 讀 31 份 `profile.json`、`SOUL_IDS.json`、碰撞表 | Batch 3 的 Soul ID 交叉一致 |
| 目視 36 位的型錄圖（非亞洲設定的 camille、aaliya 只依設定排除、未看圖）、入圍 18 位的 repo 全部原圖 | 剔除 8 張有瑕疵或不合適的候選圖，另 2 張判「需補生成」（tammy 橫式、sophia 直式）；原因寫在 `docs/calendar/data/cal_r1_casting.json` |
| `tools/build_cal_r1.py` 現算像素、裁切、有效 ppi，產生表格、縮圖、選角板 | 重跑後 git diff 為 0（可重現） |
| headless 瀏覽器開 `casting_board.html`（桌機與 390 px 手機寬） | 120 張圖 0 張破圖、無水平捲動 |
| **沒有做** | 生成圖片、花 credits、下單、登入、上傳、存檔、加購物車、聯絡廠商、接受條款、修改任何人設 canon／Soul ID／生成紀錄／網站／素材原檔 |

## 8. 請你回答（每項給 PASS／REVISE／BLOCK＋一句理由）

**Q1 規格與頁面結構**：CAL_01 的查證方法與結論是否站得住？哪一項把推論寫成了事實？（特別是 §3.3 的翻頁推論）

**Q2 十二位的個人吸引力**：請實際看 `CAL_R1_overview_12.jpg` 與 `CAL_R1_candidates_18.jpg`，逐位判斷是否符合「漂亮、性感、甜美」。有不符合的請點名。

**Q3 整組差異**：十二位放在一起，是否能清楚看出是 12 個不同的人？差異是否主要只靠髮色或服裝？最像的是哪幾對？（CAL_02 §5 已自列 iris↔rainie）

**Q4 落選與備選是否合理**：特別是 miu-shiraishi 因碰撞落選、ananya-kapoor 未入選、wendy-yeo 未入選。

**Q5 素材品質**：看 `CAL_R1_crops_12.jpg`，逐位的橫式半版與直式滿版裁切是否成立？有沒有我漏掉的臉、手、肢體、服裝、背景瑕疵？「可直接用／需修圖／需補生成」的判定是否過寬？

**Q6 製作路線**：「現有素材為主＋橫式半版」是否合理？或你認為應改「混合補生成」？請說明成本與完成度的取捨。

**Q7 月份分配**：節奏與調性是否合理？有沒有相鄰月份看起來太像？

**Q8 待決策清單**：CAL_04 §3 的 D1–D6 是否都是 Penny 必須決定、且推薦選項合理？有沒有該由執行者自己處理卻丟給 Penny 的？

**Q9 下一輪**：請根據你的覆核結論，提供**下一輪（R2）的完整執行 prompt**，可直接貼給 Claude。

## 9. 回覆格式

```
Q1: PASS|REVISE|BLOCK — 理由
...
Q8: PASS|REVISE|BLOCK — 理由
必改項（若有）：
可選項（若有）：
R2 執行 prompt：
（完整文字）
```
