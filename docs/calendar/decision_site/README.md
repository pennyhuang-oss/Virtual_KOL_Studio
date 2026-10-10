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
| `public/data.js`、`public/img/` | **程式產生**，不要手改：`python3 docs/calendar/tools/build_cal_decision_site.py` |
| `ASSET_MANIFEST.json` | 每個發佈檔的來源（固定 commit 的路徑與 git blob）、處理方式（位元組不變複製／純裁切／等比縮圖）與 sha256；不對外提供 |

## 圖片的來源與處理

- **複製**（53 張）：R3 的 300 dpi 樣張頁、橫 B 與原直 A 比較頁、Kanon 重查頁、清理對照、年曆 100% 預覽、R2 的撞臉比較圖與備選人選圖。與固定 commit 位元組相同。
- **裁切**（23 張）：替代選項只存在於 R3 決策拼圖裡，所以從 `CAL_R3_decide_B_scale_style`、`CAL_R3_decide_options`、`CAL_R3_decide_A_roster` 與 R2 `CAL_R2_decide_people_compare` 純裁切出單張（四邊內縮 2 px 避開拼貼邊界；重新存成 JPEG q95）。
- **縮圖**（每張一個）：卡片顯示用的等比縮小；點開放大一律看上面的原檔或裁切檔。
- 沒有生成、外擴、AI 增強或修圖。**不發佈**：原始訓練集、Soul ID、job_id、帳號資料、完整工作紀錄、他線 headshot（`r2/audit_otherline/`）、R2 逐人素材表（`r2/assets/CAL_R2_assets_*`，圖上印有 job_id）。
- 核對：`python3 docs/calendar/tools/build_cal_decision_site.py --check`（複製檔與固定 commit 同一 blob、裁切可重現、沒有 manifest 以外的圖片）。

## 本機執行

```bash
cd docs/calendar/decision_site
DECISION_USER=<帳號> DECISION_PASS=<密碼> PORT=8787 node server.js
```

## 部署（Railway）

- 獨立 service（不是型錄 `kol-catalog`），Root Directory `/docs/calendar/decision_site`，來源固定在單一 commit（不跟分支自動更新）。
- 帳號密碼只放在該 service 的 Railway Variables：`DECISION_USER`、`DECISION_PASS`。不寫進前端、不寫進 repo。
- 沒有 build 步驟、沒有相依套件、沒有資料庫或其他附加服務。
