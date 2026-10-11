# 2027 KOL 桌曆決策頁（decision_site）

讓 Penny 直接看圖、比較、選擇，並把決策文字複製回 ChatGPT。**不是**主管核准、印刷核准或廠商確認。

- **基準成果**：固定 commit `4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45`（R3）。頁面上的名單、月份、圖片 ID、ppi 與所有圖片都從這個 commit 讀出，不用分支頭的其他版本。
- **選擇只存在瀏覽器 localStorage**，不送到伺服器；沒有表單送出、沒有追蹤或分析、沒有外部字型或第三方服務（CSP `connect-src 'none'`）。
- 頁面不在型錄導覽裡；`robots.txt` 全站 Disallow，回應帶 `X-Robots-Tag: noindex`。**noindex 不等於存取保護**：存取保護是 HTTP Basic（下方）。

## 檔案

| 檔案 | 內容 |
|---|---|
| `server.js` | 只提供 `public/` 的靜態檔；HTTP Basic 存取保護；沒設定帳密就一律回 503 |
| `public/index.html`、`app.js`、`app.css` | 頁面（人寫） |
| `public/data.js`、`public/img/` | **程式產生**，不要手改（產生方式見下方） |
| `ASSET_MANIFEST.json` | 每個發佈檔的來源（固定 commit 的路徑與 git blob）、處理方式（位元組不變複製／純裁切／高解析預覽／等比縮圖）與 sha256；不對外提供（不在 `public/`） |

## 圖片的來源與處理

- **複製**（54 張）：R3 的 300 dpi 樣張頁、橫 B 與原直 A 比較頁、Kanon 重查頁、清理對照、年曆與 9 月小框的 100% 預覽、R2 的撞臉比較圖與備選人選圖。與固定 commit 位元組相同。頁面標「300 dpi 樣張」「100% 預覽」或「比較圖」。
- **高解析預覽**（11 張）：有實際替代選項的照片（kanon_H、angel_alt004、ananya_2、somi_H、somi_alt065、coco_alt01、tammy_H、tammy_alt075、rin_altR1V、rainie_alt02），加上名單比較用的 somi_V。來源只限可核對的既有檔：固定 commit 的 repo 檔（git blob）、R2 已取回的 Higgsfield 快取（`data/cal_r2_hf_retrieved.json` 的 sha256）、R3 清理輸出（`data/cal_r3_cleanup_report.json` 的 clean_sha256；coco_alt01 用清理版）。只做等比縮小（長邊 1600 px，JPEG q88，不帶原檔中繼資料）；頁面標「高解析預覽（未排版）」。頁面資料只有圖片 ID，沒有 job_id、來源路徑或帳號資料。
- **裁切**（8 張）：從 R3 決策拼圖純裁切（尺度例圖、kanon_V 參考、名單 12 人格與 5 月頭像）。頁面一律標「低解析選圖參考；細節與印刷採用待原圖／排版覆核」。
- **縮圖**（每張一個）：卡片顯示用的等比縮小。
- 沒有生成、外擴、AI 增強、修圖或重新下載。**不發佈**：原始訓練集、Soul ID、job_id、帳號資料、完整工作紀錄、他線 headshot（`r2/audit_otherline/`）、R2 逐人素材表（`r2/assets/CAL_R2_assets_*`，圖上印有 job_id）。
- 產生：`python3 docs/calendar/tools/build_cal_decision_site.py --hf-dir <R2 取回快取> --clean-dir <R3 清理輸出>`（兩個快取都不在 repo）。
- 核對：`python3 docs/calendar/tools/build_cal_decision_site.py --check [--hf-dir … --clean-dir …]`（複製檔與固定 commit 同一 blob、裁切與高解析預覽可重現、沒有 manifest 以外的圖片；沒給快取時，來自快取的高解析預覽只核對 sha256）。

## 確認狀態的規則

- 每項有三種狀態：未回答、草稿・待 Penny 確認、Penny 已確認。
- 按「確認目前已選的項目」只確認已回答的項目；之後只要再改（即使改回原值），該項就回到草稿。
- 補充意見是自由文字，不屬於確認項目。
- 「套用推薦為草稿」只填未回答且有推薦的項目（含 9b），不填收件對象、品牌、Logo、QR。

## 本機執行

```bash
cd docs/calendar/decision_site
DECISION_USER=<帳號> DECISION_PASS=<密碼> PORT=8787 node server.js
```

## 部署（Railway）

- 獨立 service（不是型錄 `kol-catalog`），Root Directory `/docs/calendar/decision_site`，來源固定在單一 commit（不跟分支自動更新）。
- 帳號密碼只放在該 service 的 Railway Variables：`DECISION_USER`、`DECISION_PASS`。不寫進前端、不寫進 repo。
- 沒有 build 步驟、沒有相依套件、沒有資料庫或其他附加服務。
