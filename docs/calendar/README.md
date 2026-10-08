# docs/calendar — 2027 KOL 雙款桌曆試做專案

- **任務**：TASK-CAL-001｜R1 規格確認與 12 位人設選角盤點 → **R2 修正 R1 證據與選圖，製作可供 owner 拍板的臉部比較及桌曆樣張**
- **角色**：Penny 拍板；ChatGPT 規劃與獨立覆核；Claude 執行
- **狀態**：R2 交付，等待覆核。所有推薦、選圖、樣張都是草稿，未經 Penny 拍板。
- **R1、R2 都沒有**：生成圖片、花 credits、重新訓練、下單、上傳素材到廠商、聯絡廠商、發布新公開網站、修改任何人設 canon／Soul ID／生成紀錄／素材原檔。
- R2 以唯讀方式從 Higgsfield 取回既有原圖（記錄在 `CAL_07`）；原圖只放本機快取，不進 repo。

## 先看這些（R2）

| 檔案 | 內容 |
|---|---|
| [`CAL_05_R1_FIX_TABLE.md`](CAL_05_R1_FIX_TABLE.md) | 主管 R1 覆核的逐項處理表（主管原文在 `review/calendar/CAL_R1_SUPERVISOR_REVIEW.md`） |
| [`CAL_10_OWNER_DECISIONS.md`](CAL_10_OWNER_DECISIONS.md) | **Penny 決策板**（4 個決策，每個附圖）＋技術預設＋廠商詢問稿（未發送） |
| [`CAL_06_FACES.md`](CAL_06_FACES.md) | 十二人辨識比較：A 完整頭像、B 遮髮比較、重點配對、一致性、既有碰撞值照錄 |
| [`CAL_07_PICKS_RETRIEVAL.md`](CAL_07_PICKS_RETRIEVAL.md) | 逐位替代選圖、Higgsfield 取回範圍與方式、Ananya／Wendy 補圖 |
| [`CAL_07b_HF_RETRIEVAL.generated.md`](CAL_07b_HF_RETRIEVAL.generated.md) | 取回的 82 張逐張紀錄（job_id、尺寸、狀態；程式產生） |
| [`CAL_08_DATES_2027.md`](CAL_08_DATES_2027.md) | 2027 日期與台灣假日：官方來源、適用範圍、廠商素材逐月比對、農曆 |
| [`CAL_09_MOCKUPS.md`](CAL_09_MOCKUPS.md) | 本機桌曆樣張（Iris、Vicky、Rin × 橫直、配對月曆面、橫式大照片比較、兩款封面） |
| [`CAL_11_ASSET_QUALITY.md`](CAL_11_ASSET_QUALITY.md) | 素材品質分欄摘要、203 ppi 處理、橫式大照片逐張結果 |
| [`CAL_11b_ASSET_TABLE.generated.md`](CAL_11b_ASSET_TABLE.generated.md) | 52 張候選逐張分欄（技術欄程式現算；程式產生） |

## R1 檔案（R2 已在原檔標出修正處）

| 檔案 | 內容 |
|---|---|
| [`CAL_01_SPEC_EVIDENCE.md`](CAL_01_SPEC_EVIDENCE.md) | 兩款商品規格、頁面結構（§3.3 翻頁已改為假設）、印刷參數、條款（已拆成內容限制／製作上傳／評論上傳） |
| [`CAL_02_CASTING.md`](CAL_02_CASTING.md) | 選角方法、18 位比較、12＋2 工作名單、替換組合 |
| [`CAL_02b_CANDIDATES.generated.md`](CAL_02b_CANDIDATES.generated.md) | 18 位的客觀欄位（程式產生） |
| [`CAL_03_ASSET_AUDIT_ROUTE.md`](CAL_03_ASSET_AUDIT_ROUTE.md) | 素材可用性與製作路線（R1 的「可直接用」標籤已作廢，改看 CAL_11） |
| [`CAL_03b_PRINT_TABLE.generated.md`](CAL_03b_PRINT_TABLE.generated.md) | R1 的 24 張主視覺候選像素／ppi（程式產生） |
| [`CAL_04_MONTHS_DECISIONS.md`](CAL_04_MONTHS_DECISIONS.md) | 暫定月份、CAL- 議題（決策部分改看 CAL_10） |
| [`casting_board.html`](casting_board.html)、[`sheets/`](sheets/) | R1 選角板與縮圖總覽 |

## 圖片（每張總覽 < 1 MB；高解析版本另存 `_hires` 或 `hires/`）

| 資料夾 | 內容 |
|---|---|
| `r2/decisions/` | 決策板用圖：人選與照片（1–4、5–8、9–12 月）、備選、比較、尺度 |
| `r2/faces/` | A 頭像總覽、B 遮髮總覽、重點比較、一致性；`heads/`、`masked/` 是單張 |
| `r2/assets/` | 每位的裁切預覽＋原圖細節、候選 vs 參考臉；`crops/`、`details/`、`consistency/` 是單張 |
| `r2/mockups/` | 桌曆樣張（含參考線版）；`hires/` 是 300 dpi 原尺寸 |
| `r2/dates/` | 官方 vs 廠商日期素材逐月比對、廠商年曆 |
| `r2/papermodel/` | 紙張模型（兩種拼版假設） |

## 資料與程式

| 檔案 | 內容 |
|---|---|
| `data/cal_r2_judgments.json` | **人寫**的逐張判斷（一致性、美感、瑕疵、動作、採用層級、細節框） |
| `data/cal_r2_face_pairs.json` | **人寫**的臉部比較選圖 |
| `data/cal_r2_hf_retrieved.json`、`data/cal_r2_daily140_jobs.json` | Higgsfield 取回紀錄、daily140 縮圖 ↔ job_id 對照 |
| `data/sources/dgpa_116_calendar_downloaded_2026-10-08.xlsx` | 人事總處 116 年辦公日曆表原檔 |
| `data/cal_r2_official_2027_dgpa.json`、`cal_r2_asset_metrics.json`、`cal_r2_face_geometry.json`、`cal_r2_mockup_report.json` | 程式產生 |
| `tools/` | R1：`build_cal_r1.py`。R2：見下方重建 |

## 重建

```bash
# R1（只讀 repo）
python3 docs/calendar/tools/build_cal_r1.py

# R2：不需原圖
python3 docs/calendar/tools/parse_cal_r2_dgpa.py          # 官方 xlsx → data/cal_r2_official_2027_dgpa.json
python3 docs/calendar/tools/build_cal_r2_papermodel.py     # 紙張模型
python3 docs/calendar/tools/build_cal_r2_retrieval.py      # CAL_07b

# R2：需要 Higgsfield 取回的原圖（本機快取資料夾，不在 repo）
python3 docs/calendar/tools/build_cal_r2_faces.py     --hf-dir <快取>
python3 docs/calendar/tools/build_cal_r2_assets.py    --hf-dir <快取>
python3 docs/calendar/tools/build_cal_r2_mockups.py   --hf-dir <快取>
python3 docs/calendar/tools/build_cal_r2_decisions.py --hf-dir <快取>

# R2：需要廠商日期素材（本機下載，不在 repo）
python3 docs/calendar/tools/build_cal_r2_datecheck.py <廠商素材資料夾>
```

- 只讀既有素材；不呼叫生成服務。臉部量測用 mediapipe FaceLandmarker（模型檔 `~/.cache/mediapipe/face_landmarker.task`）。
- `*.generated.md` 與程式產生的 JSON **不要手改**——要改判斷就改 `data/cal_r2_judgments.json` 或 `cal_r2_face_pairs.json` 再重跑。
- 快取資料夾的檔名與 sha256 前 16 碼記在 `data/cal_r2_hf_retrieved.json`；換機器重建時，依 job_id 從 Higgsfield 唯讀取回同一批檔案即可。

## 怎麼看

- **GitHub 網頁**：直接點 `r2/` 底下的 JPG；Markdown 檔裡的路徑都相對於 `docs/calendar/`。
- **本機**：R1 的 `casting_board.html` 可用瀏覽器直接開。
- 刻意沒有發佈到任何新的網頁服務（避免把原圖或私人連結公開出去）。
