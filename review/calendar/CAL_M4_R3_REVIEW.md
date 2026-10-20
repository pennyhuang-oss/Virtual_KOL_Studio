TASK-CAL-001／M-4／R3｜精簡檢視頁與展示首試照片｜送審報告

# M-4／R3 送審紀錄

**直接看照片（免登入、站內提供）：https://cal2027-decision-production.up.railway.app/shoot.html**

- 原圖下載：https://cal2027-decision-production.up.railway.app/img/review/V-iris-chen_m4r2_first_test.png
- 已定稿企劃／歷史紀錄：https://cal2027-decision-production.up.railway.app/history.html
- **固定成果 SHA**：`c6c6d98e93e44837ec9da2bbcd7710e86b4aa932`（基準：成果 `32fec1df14071be27858d038b88304eaff67a31a`、送審 `20b5ee89d0c354362bb2f78bcb4eb4ce23c9b7e3`）
- **部署**：Railway 只更新 `cal2027-decision`，固定到 `c6c6d98`，deployment `f179055d-971e-4b97-b15b-4a07ab445de6`（SUCCESS）。其他 service 未動、沒有新增付費服務、未合併 main、未開 PR。
- **本輪**：生成 0、修圖 0、生成 credits 0、訓練 0、上傳到生成平台 0。
- 以下驗證是執行者自測，不是主管覆核；部署不等於核准；套框預覽不是印刷核准。

## 1. 頁面精簡前後（同一量測腳本，線上）

| 項目 | 精簡前（`32fec1d` shoot.html） | 精簡後（`c6c6d98` shoot.html） |
|---|---|---|
| 桌機 1366×900 頁高 | 48,995 px（54.4 屏） | 2,181 px（2.4 屏） |
| 手機 390×844 頁高 | 106,198 px（125.8 屏） | 2,870 px（3.4 屏） |
| 可見文字（去空白） | 52,809 字 | 827 字 |
| 表格／表格列 | 80／589 | 0／0 |
| 段落／可展開區塊 | 22／113 | 5／1（只有「要複製的文字」） |
| 圖片 | 83 | 3（首試、套框、反光板裁切） |
| 第一屏看到首試照片 | 沒有 | 桌機、手機都有 |

主頁只剩 5 段：首試照片（標「首試樣張，尚未定稿」，點開大圖、「原尺寸」看原圖、可下載）→ 工作照片框預覽（標「不是印刷核准」）→ 本次待處理（反光板及支架：主管判定必修；人物與身材呈現：待Penny看圖回饋）→ 回饋（接受／想修改、備註、儲存、複製）→「已定稿企劃／歷史紀錄」連結。24 套企劃卡、修改前後表、owner 原文、月份、照片框決策、模型核查與費用流水帳都不在主頁，移到 `history.html`（另一頁，不是在主頁折疊）。

截圖：`m4_r3/before_*_first_screen.jpg`（精簡前第一屏）、`m4_r3/after_*`（精簡後第一屏、整頁、大圖、原尺寸、回饋、歷史頁）。

## 2. 照片與檔案（站內提供，不連私有 GitHub）

| 公開檔 | 來源 | 處理 | sha256 |
|---|---|---|---|
| `img/review/V-iris-chen_m4r2_first_test.png`（下載） | `32fec1d:kols/iris-chen/images/calendar_2027_m4_r2/V-iris-chen_m4r2_first_test.png`（sha256 `fe1391d9…`） | 只移除一個 tEXt 文字區塊；IHDR／IDAT／IEND 逐位元組相同，解碼像素相同；4,665,969 → 4,665,911 bytes | `90ef6c01…` |
| `img/review/V-iris-chen_m4r2_view.jpg`（頁面與大圖） | 同上 | 等比縮小到 1200×1600（JPEG q88，不帶中繼資料） | `52e2a550…` |
| `img/review/V-iris-chen_m4r2_frame_V_120x160.jpg` | `20b5ee8:review/calendar/m4_r2/frame_preview_V_120x160.jpg` | 位元組不變複製 | `1926d363…` |
| `img/review/V-iris-chen_m4r2_reflector_crop.jpg` | 原圖 | 只裁切 [0, 580, 400, 880]（JPEG q95），標「只裁切，未修圖」 | `01914099…` |

- **為什麼下載檔不是原檔位元組**：原圖 PNG 檔內有一個 tEXt 區塊，內容就是生成平台的工作 ID。依「工作ID不得公開」，下載檔只移除這個區塊；影像資料沒有改動，不是修圖。頁面與資料檔都寫明這點。
- 不修圖、不調身材、不重新生成。來源 commit 與 sha256 記在 `docs/calendar/data/cal_review_current.json`；建置器 `--check` 會從來源重做 4 個檔並逐位元組比對。

## 3. 清除展示、保留證據

- `shoot.html` 改為目前檢視頁（`review.js`、`review.css`、`review-data.js`）；原長頁連同程式與樣式改名為 `history.html`、`history.js`、`history.css`（只讀，內容照舊）。
- 歷史頁只更新過時的話：首試照片改指向目前檢視頁；R2 狀態標「R2 當時」；加上主管 R3 結論（反光板必修、人物與身材待 Penny）。
- repo 證據不刪不改：`cal_m3_shoot_plan.json`、授權與主管紀錄、CAL_18／19／20、`review/calendar/`、`kols/` 與送審 commit `20b5ee8` 相同（只新增）。主管 R3 指令逐字存於 `docs/calendar/data/cal_m4_supervisor_r3.json`。
- 之後每輪只改 `docs/calendar/data/cal_review_current.json`（當前照片＋待決事項），完成項目移到歷史頁。
- 瀏覽器既有資料：企劃回饋 `cal2027-shoot-v1:<SHA>`、素材選擇 `cal2027-materials-v1:<SHA>` 不讀寫、不刪除、不重設。

## 4. 公開內容不含私有識別碼與交易紀錄

- 建置器 `--check` 掃描整個 `public/`（含圖片位元組），找 Iris 的 Soul ID 與私有執行紀錄裡的工作 ID（含去掉連字號的寫法），結果 0 筆；線上 673 檔與本機逐位元組相同，定向驗證另外直接下載線上 15 個頁面、程式與圖片再查，也是 0 筆。
- **交易原始資料**：歷史頁的公開資料原本有交易時間、送出前邊界列、他人的交易與任務、帳號交易統計。本輪由建置器移除，只留摘要（扣款 1 筆、退款 0 筆、淨額 −0.12、精確報價、預算、歸屬層級），並寫明「交易明細原始列不公開（保存在私有 repo）」。repo 內的企劃資料不變。
- 目前檢視頁的資料沒有 UUID、repo 路徑、job／soul 字樣，也沒有扣款或交易字樣。

## 5. 回饋

- 新鍵 `cal2027-review-v1:V-iris-chen-m4r2`，只在使用者選擇、輸入或按「儲存」時寫入，重新整理後保留。
- 「複製回饋」輸出：標題、照片與標示、人物與身材呈現的選擇、備註、反光板必修、儲存時間，以及「只存在這個瀏覽器，沒有自動通知主管」。範例見 `m4_r3/copy_feedback_example.txt`（測試文字）。
- 頁面寫明回饋只存在這個瀏覽器，不會自動傳給主管。不重開企劃問卷；歷史頁仍沒有填寫欄位。

## 6. 驗證

| 項目 | 結果 | 檔案 |
|---|---|---|
| M-4 R3 定向驗證（桌機 1366 與 390px）：精簡與照片優先、大圖與原尺寸、下載（檔案位元組）、套框、待處理、回饋保存／重整／複製、舊資料不變、歷史頁、公開內容無私有識別碼與交易紀錄、溢出、JS 錯誤 | 線上 80/80、本機 80/80 PASS | `m4_r3/live_m4r3_tests.tsv`、`m4_r3/local_m4r3_tests.tsv` |
| 部署前後保留（同一測試瀏覽器設定檔，R6 填過 v6，經 R7、M-4 R1、R2 頁） | 部署前（32fec1d）5/5、部署後（c6c6d98）6/6 PASS | `m4_r3/live_upgrade_m4r2_to_m4r3.tsv`（部署後） |
| 線上檔案 sha256 與本機比對 | 673 檔不符 0；5 個 HTML 頁與本機相同（頁面版本 c6c6d98） | `m4_r3/live_bytes_check.txt` |
| 網站建置器 `--check` | PASS 658 檔（copy 122、crop 11、高解析預覽 194、thumbnail 327、目前檢視頁 4），公開檔無私有識別碼、無交易原始資料 | — |
| 企劃文件產生器 `--check` | PASS（CAL_19 位元組不變） | — |
| kol-catalog 首頁 | 與存檔相同（44,801 bytes） | `m4_r3/live_bytes_check.txt` |

## 7. 交主管與 Penny

1. 反光板及支架：主管已判定必修，處理方式（修圖或重拍）待主管另行決定；本輪沒有修圖、沒有重新生成。
2. 人物與身材呈現：等 Penny 在 shoot.html 看圖後填寫並複製回饋。

## 8. 檔案

- `docs/calendar/decision_site/public/shoot.html`、`review.js`、`review.css`、`review-data.js`、`img/review/`（4 檔）
- `docs/calendar/decision_site/public/history.html`、`history.js`、`history.css`（由 shoot.* 改名；文字小改）
- `docs/calendar/decision_site/public/index.html`、`mat.js`（入口連結文字）、`data.js`（歷史頁公開資料移除交易原始資料）
- `docs/calendar/tools/build_cal_decision_site.py`（首試照片發佈、交易資料移除、`--check` 掃描）、`docs/calendar/decision_site/README.md`、`ASSET_MANIFEST.json`
- `docs/calendar/data/cal_review_current.json`（目前檢視內容）、`docs/calendar/data/cal_m4_supervisor_r3.json`（主管 R3 指令逐字）
- `review/calendar/m4_r3/`（測試結果、位元組比對、精簡前後量測、截圖、複製範例）
