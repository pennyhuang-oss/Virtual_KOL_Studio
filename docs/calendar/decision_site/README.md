# 2027 KOL 桌曆決策頁（decision_site）

讓 Penny 直接看圖、比較、選擇，並把決策文字複製回 ChatGPT。**不是**主管核准、印刷核准或廠商確認。

- **基準成果**：固定 commit `4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45`（R3）。頁面上的名單、月份、圖片 ID、ppi 與所有圖片都從這個 commit 讀出，不用分支頭的其他版本。
- **選擇只存在瀏覽器 localStorage**，不送到伺服器；沒有表單送出、沒有追蹤或分析、沒有外部字型或第三方服務（CSP `connect-src 'none'`）。
- **公開可讀、不需登入**：Penny 2026-10-12 要求取消帳號密碼並同意此展示頁公開（`docs/calendar/CAL_17_OWNER_ROSTER_DECISION.md`）。頁面不在型錄導覽裡；`robots.txt` 全站 Disallow，回應帶 `X-Robots-Tag: noindex`——這只是請搜尋引擎不要收錄，**不能保證**沒有人搜尋到或打開。
- 公開內容只限本案展示照片與必要選擇資料；不發布帳號資料、Soul ID、job_id、訓練集整包或內部工作紀錄。

## 檔案

| 檔案 | 內容 |
|---|---|
| `server.js` | 只提供 `public/` 的靜態檔（不需登入；noindex、robots、CSP 等標頭） |
| `public/index.html`、`mat.js`、`mat.css` | **第二階段：為 Penny 已確認的 12 位挑照片**（主入口；人寫） |
| `public/cast.html`、`cast.js`、`cast.css` | 第一階段：自由選 12 位人設（已完成，保留作參考；人寫） |
| `public/plan.html`、`app.js`、`app.css` | 原推薦方案參考（舊版決策頁：照片、尺度、版面、品牌；第一階段不必填；人寫） |
| `public/data.js`、`public/img/` | **程式產生**，不要手改（產生方式見下方） |
| `ASSET_MANIFEST.json` | 每個發佈檔的來源（固定 commit 的路徑與 git blob）、處理方式（位元組不變複製／純裁切／高解析預覽／等比縮圖）與 sha256；不對外提供（不在 `public/`） |

## 圖片的來源與處理

- **複製**（舊版決策頁）：R3 的 300 dpi 樣張頁、橫 B 與原直 A 比較頁、Kanon 重查頁、清理對照、年曆與 9 月小框的 100% 預覽、R2 的撞臉比較圖與備選人選圖。與固定 commit 位元組相同。頁面標「300 dpi 樣張」「100% 預覽」或「比較圖」。
- **第二階段素材**（171 張，12 位）：高解析預覽 159 張（repo 原圖 138、R2 已取回原圖 16、R3 清理輸出 5），來源核對方式同下一條；Miu、Jia、Yerin 的 daily 照片 12 張只有 repo 的 360×480 縮圖（位元組不變複製，標「低解析」）。manifest 每筆記錄素材 ID、來源、hash 與處理方式；頁面資料沒有來源路徑或 job_id。
- **高解析預覽（舊版決策頁）**（11 張）：有實際替代選項的照片（kanon_H、angel_alt004、ananya_2、somi_H、somi_alt065、coco_alt01、tammy_H、tammy_alt075、rin_altR1V、rainie_alt02），加上名單比較用的 somi_V。來源只限可核對的既有檔：固定 commit 的 repo 檔（git blob）、R2 已取回的 Higgsfield 快取（`data/cal_r2_hf_retrieved.json` 的 sha256）、R3 清理輸出（`data/cal_r3_cleanup_report.json` 的 clean_sha256；coco_alt01 用清理版）。只做等比縮小（長邊 1600 px，JPEG q88，不帶原檔中繼資料）；頁面標「高解析預覽（未排版）」。頁面資料只有圖片 ID，沒有 job_id、來源路徑或帳號資料。
- **裁切**（8 張）：從 R3 決策拼圖純裁切（尺度例圖、kanon_V 參考、名單 12 人格與 5 月頭像）。頁面一律標「低解析選圖參考；細節與印刷採用待原圖／排版覆核」。
- **縮圖**（每張一個）：卡片顯示用的等比縮小。
- 沒有生成、外擴、AI 增強、修圖或重新下載。**不發佈**：原始訓練集、Soul ID、job_id、帳號資料、完整工作紀錄、他線 headshot（`r2/audit_otherline/`）、R2 逐人素材表（`r2/assets/CAL_R2_assets_*`，圖上印有 job_id）。
- 產生：`python3 docs/calendar/tools/build_cal_decision_site.py --hf-dir <R2 取回快取> --clean-dir <R3 清理輸出>`（兩個快取都不在 repo）。
- 核對：`python3 docs/calendar/tools/build_cal_decision_site.py --check [--hf-dir … --clean-dir …]`（複製檔與固定 commit 同一 blob、裁切與高解析預覽可重現、沒有 manifest 以外的圖片；沒給快取時，來自快取的高解析預覽只核對 sha256）。

## 第二階段：挑照片（index.html）

- 名單只依 owner 決定紀錄 `docs/calendar/data/cal_m1_owner_roster.json`（`roster-v1`），不依瀏覽器資料；之後改名單只能另建新版本。
- 素材清單（人寫）：`docs/calendar/data/cal_m1_materials.json`。每張照片有固定素材 ID（例 `iris-01`）、主要候選／更多素材、簡短標註、待修處、檢查方式；逐張剔除理由（近似重複、尺度、臉不符、瑕疵）只記在這個檔案，不上公開頁。
- 圖片：repo 原圖與 R2 已取回原圖、R3 清理輸出 → 等比縮小的高解析預覽（長邊 1600 px，JPEG q88）；Miu、Jia、Yerin 的 daily 照片沒有取回原圖 → 只發佈 repo 的 360×480 縮圖（位元組不變），頁面標「低解析」並列為缺口。R3 清理版與原圖分開、各有 ID；沒有正式修圖版。
- 每位：橫式照片、直式照片各一（可同一張），備選不限張數。狀態存在 `localStorage` 的 `cal2027-materials-v1:<SHA>`，與 `cal2027-casting-v1:<SHA>`、`cal2027-decision-v1:<SHA>` 分開；舊資料只讀來顯示提示，從不寫入、轉換或刪除，也不算照片核准。
- 「確認目前已選素材」只確認有選照片的人；之後這位任何更動（即使改回原樣）都回到草稿。未選的人在複製文字裡寫「未選（不算核准）」。
- 複製文字含名單版本、素材基準、素材清單 blob、頁面版本、每位的橫直主照片 ID、備選、狀態與備註，並註明月份、版面、修圖與印刷可用性都未決定。

## 第一階段選角（cast.html，參考）

- 候選：R1 入圍比較 18 位（`CAL_02_CASTING.md` §3、`data/cal_r1_candidates.json`）＋R2 追加比較 2 位（Ananya、Wendy；`CAL_02` §5.3、§6），分開列出。
- 每位一張卡：姓名（英文＋本名）、ID、正臉（R2 臉部比較頭像；Miu、Jia、Peggy、Yerin 沒有 R2 頭像，用 R1 選角板的正面圖）、另 2 張 R1 選角板圖、一句外型／氣質（取自 R1／R2 文件）、量測狀態、既有相似度紀錄（照錄）。圖都是低解析辨識用圖，只用來認人，不代表桌曆素材。
- 名單狀態存在 `localStorage` 的 `cal2027-casting-v1:<SHA>`，與舊版決策頁的 `cal2027-decision-v1:<SHA>` 分開；選角頁只讀舊版資料來顯示提示，從不寫入或轉換。
- 恰好 12 位才能確認；確認前顯示 12 位照片與姓名。確認後名單有任何更動（即使換回原名單）都回到草稿，要重新確認。
- 超過 12 位只提示，不自動刪人；相似度紀錄只提示，不停用按鈕、不自動換人。
- 「複製選角結果」不需要素材、月份、版面或品牌。

## 確認狀態的規則（原推薦方案參考頁）

- 每項有三種狀態：未回答、草稿・待 Penny 確認、Penny 已確認。
- 按「確認目前已選的項目」只確認已回答的項目；之後只要再改（即使改回原值），該項就回到草稿。
- 補充意見是自由文字，不屬於確認項目。
- 「套用推薦為草稿」只填未回答且有推薦的項目（含 9b），不填收件對象、品牌、Logo、QR。

## 本機執行

```bash
cd docs/calendar/decision_site
PORT=8787 node server.js
```

## 部署（Railway）

- 獨立 service（不是型錄 `kol-catalog`），Root Directory `/docs/calendar/decision_site`，來源固定在單一 commit（不跟分支自動更新）。
- 不需要任何帳號密碼變數（舊的 `DECISION_USER`、`DECISION_PASS` 已從該 service 移除）。
- 沒有 build 步驟、沒有相依套件、沒有資料庫或其他附加服務。
