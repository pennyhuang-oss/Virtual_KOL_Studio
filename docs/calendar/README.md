# docs/calendar — 2027 KOL 雙款桌曆試做專案

- **任務**：TASK-CAL-001｜R1 規格確認與 12 位人設選角盤點
- **角色**：Penny 拍板；ChatGPT 規劃與獨立覆核；Claude 執行
- **狀態**：R1 交付，等待覆核。所有推薦都是建議稿，未經 Penny 拍板。
- **本輪沒有**：生成圖片、花 credits、下單、上傳素材、聯絡廠商、修改任何人設 canon／Soul ID／生成紀錄／網站／素材原檔。

## 檔案

| 檔案 | 內容 |
|---|---|
| [`CAL_01_SPEC_EVIDENCE.md`](CAL_01_SPEC_EVIDENCE.md) | 兩款商品規格、頁面結構、2027 支援、印刷參數、試做範圍（含查證方法與證據） |
| [`CAL_02_CASTING.md`](CAL_02_CASTING.md) | 選角方法、18 位比較、12＋2 推薦、整組差異檢查、排除理由 |
| [`CAL_02b_CANDIDATES.generated.md`](CAL_02b_CANDIDATES.generated.md) | 18 位的客觀欄位（程式產生） |
| [`CAL_03_ASSET_AUDIT_ROUTE.md`](CAL_03_ASSET_AUDIT_ROUTE.md) | 素材可用性、缺口、製作路線、數量與成本依據 |
| [`CAL_03b_PRINT_TABLE.generated.md`](CAL_03b_PRINT_TABLE.generated.md) | 24 張主視覺候選的像素、有效 ppi、判定（程式產生） |
| [`CAL_04_MONTHS_DECISIONS.md`](CAL_04_MONTHS_DECISIONS.md) | 暫定月份、封面與其他頁建議、待 Penny 決策、CAL- 議題 |
| [`casting_board.html`](casting_board.html) | HTML 選角板（本機開啟；圖片都在 `img/`） |
| [`sheets/`](sheets/) | 縮圖總覽 JPG（GitHub 網頁可直接看） |
| `img/cand/` `img/crop/` `img/vendor/` | 候選縮圖、裁切預覽、廠商證據圖 |
| `data/cal_r1_casting.json` | 人寫的判斷（推薦理由、缺點、判定） |
| `data/cal_r1_candidates.json` `data/cal_r1_crop_report.json` | 程式產生的合併資料與裁切報告 |
| `data/vendor_editor_config_2026-10-08.json` | 廠商編輯器設定擷取 |
| `tools/build_cal_r1.py` | 產生以上圖片、表格與 HTML |

## 重建

```bash
python3 docs/calendar/tools/build_cal_r1.py
```

只讀 repo 既有素材，不呼叫任何外部服務。`*.generated.md` 與 `data/cal_r1_candidates.json`、`data/cal_r1_crop_report.json` 是輸出，**不要手改**——要改判斷就改 `data/cal_r1_casting.json` 再重跑。

## 怎麼看選角板

- **本機**：下載或 clone 這個分支後，直接用瀏覽器開 `docs/calendar/casting_board.html`（圖片用相對路徑）。
- **GitHub 網頁**：HTML 不會被渲染；請改看 `sheets/` 底下三張 JPG，內容與選角板一致。
- 刻意沒有發佈到任何新的網頁服務（避免把原圖或私人連結公開出去）。
