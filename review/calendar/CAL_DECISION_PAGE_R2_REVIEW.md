# 決策頁第二版送審（TASK-CAL-001｜2027 KOL 桌曆決策頁）

- **狀態**：已依主管覆核修正並重新部署；等待主管覆核與 Penny 看圖決策。R4 技術收尾沒有執行。
- **頁面**：https://cal2027-decision-production.up.railway.app（HTTP Basic；帳密與上一版相同、未變更，不寫在這裡）
- **頁面成果 commit**：`84aba09ee007d66de555222cf75604bf63b90b79`（上一版 `e8f76d3`）
- **部署版本**：Railway service `cal2027-decision`，deployment `359fbd74`，來源固定在 `84aba09`
- **素材基準 SHA**：`4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45`
- 下列驗證全部是 **Claude 自測**（Playwright 自動化＋截圖），**不是主管的獨立驗證**。

## 1. 逐項修正

| 覆核 | 要求 | 本版做法 | 檔案 |
|---|---|---|---|
| Q1 PASS | 簡單存取保護可接受 | 不變（HTTP Basic，帳密只在 Railway Variables） | `server.js` |
| 必做 1 | 變更即撤銷確認，改回舊值仍是草稿 | 確認存成 `{v, at}`；任何選擇或文字變更都刪掉該項確認，要再按確認。補充意見標為「自由文字，不屬於確認項目」 | `public/app.js`（`setVal`、`status`） |
| Q5／必做 2 | 預覽與選擇不混淆 | 每月卡片分兩欄：左「主管推薦｜固定樣張（不隨選擇改變）」，右「目前選擇」。目前選擇依「所選版面｜月份｜圖片 ID」找現成樣張：相同顯示「＝ 上面的推薦樣張」；有其他樣張就顯示（例：橫 B、原直 A 4 位、女僕直式統一框）；沒有就顯示「此選擇尚未排版」並附原照片。沒有為此製作新組合 | `public/app.js`（`MOCK`、`curSideHtml`） |
| Q5／必做 3 | 主流程與減少負擔 | 頁首新增「決策摘要與步驟」：步驟、三個按鈕（套用推薦為草稿／確認目前已選的項目／複製決策結果）、目前選擇摘要表、與推薦不同的地方、未回答清單。各月替代選項收進「修改這個月」。32 個細項保留。不自動核准、不填收件對象／品牌／Logo／QR；品牌未填不阻擋複製 | `public/app.js`（`sQuick`、`summaryRows`、`changeList`） |
| Q4／必做 4 | 9b 主管推薦 | 9b 加「主管推薦」，理由照覆核文字；套用推薦時填入 9b，仍是草稿 | `public/app.js`（`GRID9`） |
| Q2／必做 5 | 低解析標示、高解析預覽 | 拼圖裁切（8 張：尺度例圖、kanon_V 參考、名單 12 人格與 5 月頭像）一律標「低解析選圖參考；細節與印刷採用待原圖／排版覆核」，放大說明不寫 300 dpi。替代照片改用 11 張高解析預覽（見第 2 節）。9b 改用固定 commit 既有的小框 100% 預覽。放大說明依類型寫明：300 dpi 樣張原檔／100% 預覽／比較圖／低解析／高解析預覽（原圖等比縮小、未排版） | `public/app.js`（`fig`、`viewerNote`）、`tools/build_cal_decision_site.py` |
| Q3 PASS | 5c、10c、12b 由 Penny 指定橫／直 | 不變；對照表註明「仍須後續排版覆核」 | `public/app.js` |
| Q6／必做 6 | 碰撞數字收進展開區 | 主畫面只放並排照片與簡短觀察（含「沒有量測過的人不能說不會撞臉」）；既有數字、門檻與限制移到「技術說明」展開區 | `public/app.js`（`s2`） |

另外：名單選 A1 時，5 月卡片改顯示 Ananya 的目視觀察與 A1 選項；摘要表在手機改成直排。

## 2. 高解析預覽的來源（11 張）

只用可核對的既有檔，**沒有重新下載、沒有呼叫 Higgsfield、沒有生成或增強**；只做等比縮小（長邊 1600 px，JPEG q88，不帶原檔中繼資料）。頁面資料只有圖片 ID，沒有 job_id、來源路徑或帳號資料；來源描述只在不對外提供的 `docs/calendar/decision_site/ASSET_MANIFEST.json`。

| 圖片 ID | 用途 | 來源與核對 |
|---|---|---|
| kanon_H | B-K2 女僕 | repo 檔 @4fd3995（git blob） |
| angel_alt004 | B-N2 河岸 | R2 已取回的 Higgsfield 快取（`cal_r2_hf_retrieved.json` sha256） |
| ananya_2 | A1 | repo 檔 @4fd3995 |
| somi_V | 5 月 Somi／Ananya 對照 | R2 Higgsfield 快取 |
| somi_H | 5b | repo 檔 @4fd3995 |
| somi_alt065 | 5c | R2 Higgsfield 快取 |
| coco_alt01 | 7b（用 R3 清理版） | R3 清理輸出（`cal_r3_cleanup_report.json` clean_sha256） |
| tammy_H | 10b | repo 檔 @4fd3995 |
| tammy_alt075 | 10c | R2 Higgsfield 快取 |
| rin_altR1V | 11b | repo 檔 @4fd3995 |
| rainie_alt02 | 12b | repo 檔 @4fd3995 |

- 7 張 repo 來源位在各人設的訓練或參考資料夾（kanon_H、somi_H、tammy_H、rin_altR1V、rainie_alt02 在 training 資料夾；ananya_2 在 face_reference）。發佈的是這幾張候選照片的縮小預覽，不是資料夾或原檔；請主管確認這樣是否符合「不公開訓練集」的界線。
- `--check` 會重算：repo 來源與裁切從 git 重算；快取來源在提供快取時重算，沒提供時只核對 sha256。

## 3. 實際驗證（Claude 自測；正式網址；Chromium 桌機 1366 px 與手機 390 px；全部 PASS）

- 存取：沒帶帳密或密碼錯誤，頁面、資料與高解析預覽都回 401。robots.txt 全站 Disallow；回應帶 X-Robots-Tag noindex。
- 帳密與 job_id：送到前端的 HTML、JS、CSS、data.js 都查不到帳密、job_id 或「hf:」字樣；repo 裡也沒有帳密。
- 線上 151 個檔案的 sha256 與 repo、manifest 一致；頁首顯示部署版本 `84aba09`。
- 136 張卡片圖都載入；73 張放大圖都回 200。低解析 8 處、高解析預覽 14 處、300 dpi 樣張的標示都正確，放大說明也對（低解析與高解析預覽都不寫 300 dpi）。
- 兩種寬度都沒有水平捲動；展開全部「修改這個月」後，也沒有元素超出畫面寬。
- 12 個月的姓名、推薦圖片 ID、選項圖片 ID，與 4fd3995 的 `cal_r3_picks.json` 逐一相符。
- 套用推薦：全部是草稿，已確認 0 項。9b 是「主管推薦〔草稿・未確認〕」。收件對象、品牌、Logo、QR 都維持未回答。
- 確認狀態：
  - 確認 → 尺度改成 B-S1 → 再改回 B-S2：仍是草稿。
  - 品牌文字確認後改了又改回：仍是草稿；清空後變回未回答。
  - 補充意見輸出時標為自由文字。
- 預覽與選擇：
  - 推薦照片顯示「＝ 上面的推薦樣張」。
  - 5b 顯示「此選擇尚未排版」並附原照片。
  - 版面改成橫 B：1 月顯示橫 B 樣張；5b 仍是尚未排版。
  - 版面改成原直 A：6 月顯示原直 A 樣張；3 月尚未排版。
  - 女僕（B-K2）：橫式與原直 A 都尚未排版；換回直式統一框時，顯示既有的女僕樣張。
  - 河岸（B-N2）：尚未排版。
  - 名單選 A1：5 月變成 Ananya 的題目；選 ananya_2 後顯示尚未排版。
  - 輸出文字與修改清單都會標「（尚未排版）」。
- 選擇在重新整理後保留；重設會清空（重新整理後也是空的）；載入時不會自動複製。
- 品牌未填也能複製，輸出維持〔未回答〕。輸出含固定 SHA 與全部必要欄位。
- 放大後按關閉或返回鍵都回到原位置。沒有 console 錯誤；只有「放大圖還在載入就關閉」造成的中止載入，不是壞圖。
- 型錄 `kol-catalog`：首頁仍回 200；部署紀錄仍是 2026-09-24 的 `eabb3a25`。`897-audition` 也沒有變更。

## 4. 截圖（`review/calendar/decision_page_r2/`）

截圖中的選擇是 Claude 的示範操作，**不是 Penny 的決定**：先按「套用推薦為草稿」，再示範改 5b、B-K2、橫 B。截完已按重設。

| 檔案（mobile_／desktop_） | 內容 |
|---|---|
| `01_top_unanswered` | 頁首與摘要區，全部未回答 |
| `02_summary_after_apply_rec` | 套用推薦後的摘要：全部草稿；品牌等仍未回答 |
| `03_month1_rec_equals_sample` | 推薦照片＝推薦樣張 |
| `04_month2_maid_not_laid_out` | B-K2 女僕：橫 B 尚未排版（附高解析預覽）；直式統一框有既有樣張 |
| `05_month5_alt_not_laid_out` | 5b：此選擇尚未排版；直式仍＝推薦樣張 |
| `06_month1_current_HB_sample` | 版面改橫 B 後，1 月「目前選擇」顯示橫 B 樣張 |
| `07_summary_with_exceptions` | 摘要表、修改清單、未回答清單 |
| `08_viewer_lowres` | 低解析圖的放大說明 |
| `09_viewer_hires` | 高解析預覽的放大說明 |

## 5. 已知限制

- 存取保護是單一共用帳密，沒有個人帳號、到期或存取紀錄。
- 替代照片只有原照片的高解析預覽，沒有版面樣張。原直 A 只有 4 位有樣張；女僕橫式、河岸、Ananya 都沒有樣張。
- 名單 12 人格、尺度例圖、kanon_V 參考仍是低解析拼圖裁切（有標示）。
- 選擇存在單一瀏覽器：換裝置或用無痕模式不會保留。
- 本頁不能證明印刷色彩、字體可讀性或正反面方向；線圈區 12 mm 是本專案的假設。

## 6. 外部操作紀錄（本版）

1. GitHub：push `84aba09`（頁面）與本送審檔所在的 commit 到 `claude/epic-carson-n5w0qu`。沒有開 PR，沒有合併 main。
2. Railway：
   - describe-environment（部署前後各一次）。
   - connect-service-source：只針對 `cal2027-decision`，改固定到 `84aba09`，觸發部署 `359fbd74`（SUCCESS）。
   - 沒有改變數、網域、其他設定或其他 service，也沒有新增資源。
3. HTTP：部署前後各 GET 一次型錄首頁；對新網址跑自動驗收與截圖。
4. 本機：讀取 R2 取回快取與 R3 清理輸出（都在工作環境的 scratchpad，不在 repo），核對 sha256 後產生縮小預覽。
- 沒有呼叫 Higgsfield、沒有重新下載、沒有生成、沒有聯絡廠商。

## 7. 請主管覆核

1. 7 張高解析預覽的來源在 training 或 face_reference 資料夾（第 2 節）。發佈候選照片的縮小預覽是否可接受？
2. 「目前選擇」在版面未回答時，以推薦版面判斷有沒有樣張（頁面與輸出都有註明）。這樣是否清楚？
3. 「確認目前已選的項目」是一次確認全部已回答的項目，不是逐項確認。這樣是否足夠？
