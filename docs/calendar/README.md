# docs/calendar — 2027 KOL 雙款桌曆試做專案

- **任務**：TASK-CAL-001｜R1 規格與選角 → R2 證據修正與樣張 → **R3 修正 R2 證據與量測、統一版型、清理草稿、精簡決策包**
- **角色**：Penny 拍板；ChatGPT 規劃與獨立覆核；Claude 執行
- **狀態**：R3 交付，等待覆核。所有選圖、版型、樣張都是**暫定草稿**：未經 Penny 核准、未經廠商確認；Penny 未回答前 owner 核准狀態維持「待決」。
- **R1–R3 都沒有**：生成圖片、外擴、AI 增強、花 credits、重新訓練、下單、上傳到廠商、聯絡廠商、接受新條款、發布網站、合併 main、修改任何人設 canon／Soul ID／訓練集／Higgsfield 紀錄。

## 先看這些（R3）

| 檔案 | 內容 |
|---|---|
| [`CAL_12_R2_FIX_TABLE.md`](CAL_12_R2_FIX_TABLE.md) | 主管 R2 結論的逐項處理表（完成／部分／未完成＋證據） |
| [`CAL_10_OWNER_DECISIONS.md`](CAL_10_OWNER_DECISIONS.md) | **Penny 決策包**：四題、各一推薦、一行回覆；廠商詢問稿（未發送） |
| [`CAL_14_LAYOUT_R3.md`](CAL_14_LAYOUT_R3.md) | 統一版型（橫 A＋直式統一框 120×128）、實際裁切量測、橫 B 逐張、Kanon 直式重查 |
| [`CAL_14b_LAYOUT_TABLE.generated.md`](CAL_14b_LAYOUT_TABLE.generated.md) | 50 個樣張頁的逐框量測與文字邊界檢查（程式產生） |
| [`CAL_13_PAGE_MODEL.md`](CAL_13_PAGE_MODEL.md)、[`CAL_13b_PAGE_MODEL.generated.md`](CAL_13b_PAGE_MODEL.generated.md) | 完整頁序（28／32 面）與紙張模型核算 |
| [`CAL_16_CLEANUP.md`](CAL_16_CLEANUP.md) | 主推薦圖的本機清理：完成、部分、撤回 |
| [`CAL_08_DATES_2027.md`](CAL_08_DATES_2027.md)、[`CAL_15b_DATE_OUTPUT_CHECK.generated.md`](CAL_15b_DATE_OUTPUT_CHECK.generated.md) | 官方日期、廠商素材已核／抽查／未核、自繪日期的輸出頁核對 |
| [`CAL_06_FACES.md`](CAL_06_FACES.md) | 臉部比較（R3：既有數字與目視觀察分列） |
| [`CAL_07_PICKS_RETRIEVAL.md`](CAL_07_PICKS_RETRIEVAL.md)、[`CAL_07b_HF_RETRIEVAL.generated.md`](CAL_07b_HF_RETRIEVAL.generated.md) | 取回紀錄（R3：完整 sha256、本機快取核對、他線圖移出） |

主管與 Penny 轉交的執行要求原文：`review/calendar/CAL_R2_EXEC_PROMPT_FROM_PENNY.md`、`review/calendar/CAL_R3_EXEC_PROMPT_FROM_PENNY.md`（都不是主管完整的覆核對話原文，那份 Claude 沒有取得）。

## R3 圖片（每張預覽 < 1 MB；`_hires` 或 `hires/` 為可放大版本）

| 資料夾 | 內容 |
|---|---|
| `r3/decisions/` | 決策包：A 名單、B 尺度與造型、C 版面、D 品牌、各月選項附表 |
| `r3/sheets/` | 24 面總覽（橫 1–6、7–12；直 1–6、7–12）、封面＋大格面＋年曆、原直 A vs 統一框、橫 B 逐張、Kanon 重查 |
| `r3/pages/` | 每一頁（`hires/` 300 dpi、`guides/` 參考線版：紅＝線圈區、藍＝裁切線、綠＝安全區、橘＝照片框與圖片 ID） |
| `r3/compare/`、`r3/checks/` | 比較樣張（原直 A、橫 B）、Kanon 重查頁 |
| `r3/previews/` | 100% 實際像素預覽（不是印刷證明） |
| `r3/cleanup/` | 清理修前／修後／版面實際大小對照 |
| `r3/pagemodel/` | 紙張模型圖 |
| `r2/audit_otherline/` | 他線 headshot 觀察頁（**只留稽核，不作任何依據**） |

## R2、R1 檔案（以 R3 為準；被推翻處都有標註）

| 檔案 | 內容 |
|---|---|
| `CAL_05_R1_FIX_TABLE.md` | R1 必改項處理表（R2） |
| `CAL_09_MOCKUPS.md`、`r2/mockups/` | R2 樣張（R3 以 `CAL_14` 為準） |
| `CAL_11_ASSET_QUALITY.md`、`CAL_11b_ASSET_TABLE.generated.md`、`r2/assets/` | R2 素材分欄（H_wide＝R2 探索框 204×112） |
| `CAL_01`–`CAL_04`、`CAL_02b`、`CAL_03b`、`casting_board.html`、`sheets/` | R1 規格、選角、素材、月份 |
| `r2/faces/`、`r2/decisions/`、`r2/dates/`、`r2/papermodel/` | R2 臉部比較、決策板、日期比對、紙張模型 |

## 資料與程式

| 檔案 | 內容 |
|---|---|
| `data/cal_r3_picks.json` | **人寫**：R3 主推薦、甜美／性感描述、選項與決策代碼、人工目視紀錄 |
| `data/cal_r3_cleanup.json` | **人寫**：清理規格（區域、方法、理由） |
| `data/cal_r2_judgments.json`、`data/cal_r2_face_pairs.json` | **人寫**：逐張判斷、臉部比較選圖 |
| `data/cal_r3_layout_report.json`、`cal_r3_date_check.json`、`cal_r3_cleanup_report.json`、`cal_r3_pagemodel.json` | 程式產生 |
| `data/cal_r2_hf_retrieved.json`、`cal_r2_daily140_jobs.json` | Higgsfield 取回紀錄（R3 補完整 sha256 與快取核對） |
| `data/sources/dgpa_116_calendar_downloaded_2026-10-08.xlsx` | 人事總處 116 年辦公日曆表原檔 |

## 重建

```bash
# 不需原圖
python3 docs/calendar/tools/parse_cal_r2_dgpa.py          # 官方 xlsx → data/cal_r2_official_2027_dgpa.json
python3 docs/calendar/tools/build_cal_r3_pagemodel.py     # 頁序與紙張模型
python3 docs/calendar/tools/build_cal_r2_retrieval.py     # CAL_07b

# 需要 Higgsfield 取回的原圖快取（不在 repo）與清理輸出資料夾
python3 docs/calendar/tools/verify_cal_r3_hfcache.py --hf-dir <快取>
python3 docs/calendar/tools/build_cal_r3_cleanup.py   --hf-dir <快取> --cache <清理輸出>
python3 docs/calendar/tools/build_cal_r3_pages.py     --hf-dir <快取> --cache <清理輸出>
python3 docs/calendar/tools/build_cal_r3_sheets.py    --hf-dir <快取> --cache <清理輸出>
python3 docs/calendar/tools/build_cal_r3_decisions.py --hf-dir <快取> --cache <清理輸出>
python3 docs/calendar/tools/test_cal_r3_datecheck.py      # 日期核對的負向測試

# R1／R2（歷史）
python3 docs/calendar/tools/build_cal_r1.py
python3 docs/calendar/tools/build_cal_r2_faces.py  --hf-dir <快取>
python3 docs/calendar/tools/build_cal_r2_assets.py --hf-dir <快取>
```

- 模型檔（都在 `~/.cache/mediapipe/`，不進 repo）：`face_landmarker.task`（臉部特徵點）、`selfie_multiclass_256x256.tflite`（主角保護遮罩與髮頂判定；分類模型，不生成內容）。
- `*.generated.md` 與程式產生的 JSON **不要手改**；要改判斷就改人寫的 JSON 再重跑。R3 全部程式連跑兩次輸出逐位元組相同。
- 快取資料夾的檔名與完整 sha256 記在 `data/cal_r2_hf_retrieved.json`；換機器時依 job_id 從 Higgsfield 唯讀取回同一批檔案即可（`verify_cal_r3_hfcache.py` 會核對）。

## 怎麼看

- GitHub 網頁：直接點 `r3/` 底下的 JPG；Markdown 裡的路徑都相對於 `docs/calendar/`。
- 刻意沒有發佈到任何新的網頁服務。
