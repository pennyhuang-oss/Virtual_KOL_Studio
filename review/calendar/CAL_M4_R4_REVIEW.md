TASK-CAL-001／M-4／R4｜Iris定案與5位角色批次生成準備｜送審報告

# M-4／R4 送審紀錄

- **集中送審文件**：`docs/calendar/CAL_21_M4_BATCH1_PREP.md`。5 份完整 prompt、中文摘要、修改前後、Soul 證據、設定、報價、停止條件與交易核對都在這份文件，主管不必翻其他檔。資料來源是 `docs/calendar/data/cal_m4_batch1_prep.json`。
- **固定成果 SHA**：`b5cbe1c563df4a6252cc842ceeaccc2d358e2e6b`（基準：成果 `c6c6d98e93e44837ec9da2bbcd7710e86b4aa932`、送審 `ab775cf80343ff17458da2934a4bd6d420e8f946`）
- **部署**：只更新 `cal2027-decision`，固定在 `b5cbe1c`；deployment `8116b9c3-578b-424d-baee-5da6500ce147`（SUCCESS）。其他 service 未動、沒有新增付費服務、未合併 main、未開 PR。
- **頁面**：https://cal2027-decision-production.up.railway.app/shoot.html
- **本輪**：新增生成 0、修圖 0、訓練 0、扣 credits 0。唯讀查詢 10 次，其中不扣款報價預檢 5 次。
- 以下是執行者自測，不是主管覆核；部署不等於核准；第一批尚未取得生成指令。

## 1. Iris 定案

- Penny 的回饋（主管轉述）逐字存於 `docs/calendar/data/cal_m4_owner_r4.json`，同一檔也逐字保存主管 R4 指令。這份回饋取代主管 M-4 R3「反光板及支架必修」的判定。
- 企劃升為 `shoot-plan-v10`（M-4 R4）：`status.iris_first` 改為 accepted-by-owner；進度為 24 套定稿、已生成 1、已接受 1、其餘 23 套待製作。24 套內容、月份與 M-4 R1／R2 紀錄都不變（測試逐欄比對）。
- 不修圖、不重生、不再詢問是否接受。
- 文件同步：CAL_18 狀態與版本列、CAL_20 新增「R4. Penny 定案」，R2 狀態改標「R2 當時」。CAL_19 位元組不變。

## 2. 主頁與歷史

- 主頁 `shoot.html` 只剩四項：
  - 已接受的照片（綠色「已接受（Penny）」，可開大圖、看原尺寸、下載原圖）；
  - 目前進度：下一批 5 位，準備中，待主管覆核，只列名字、月份與橫直；
  - 套框預覽；
  - 歷史連結。
- 主頁已拿掉：回饋題、任何輸入欄位、反光板裁切、prompt 與費用。主頁高度：桌機 1,399 px（1.6 屏）、390px 寬手機 2,155 px（2.6 屏）。
- M-4 R3 的回饋題移到 `docs/calendar/data/cal_review_history.json` 與歷史頁「目前檢視頁的歷次紀錄」。Penny 留在瀏覽器裡的那一題回饋，歷史頁只讀顯示，不寫入、不清除。
- 歷史頁的 V-Iris 卡片、狀態列與首試紀錄都已改成「Penny 已接受（M-4 R4）」。R3 的「反光板必修」保留，標為歷史。

## 3. 第一批 5 位（摘要；完整內容見 CAL_21）

| # | 角色 | 套別 | 月份 | 比例 | 光線 | 視線 |
|---|---|---|---|---|---|---|
| 1 | Tammy | V-tammy-chou | 1 月 | 3:4 | 室內水晶吊燈 | 看鏡頭 |
| 2 | Rin | V-rin-ayase | 10 月 | 3:4 | 陰天柔光 | 三分之二側臉、不看鏡頭 |
| 3 | Somi | V-somi-oh | 12 月 | 3:4 | 雪夜燈籠 | 三分之二側臉、不看鏡頭 |
| 4 | Yerin | H-yerin-han | 5 月 | 16:9 | 晴朗晨光 | 看鏡頭 |
| 5 | Jia | H-jia-seo | 9 月 | 16:9 | 傍晚逆光 | 三分之二側臉、不看鏡頭 |

- **選人**：只從 6 位 production_ready Soul 裡選。這 6 位在 2026-09-07 做過 6 張驗證，臉部門檻 6/6 通過。Miu 延到下一批（兩套都是有道具的坐姿，另有「童顏顯小」風險）。Coco、Mia、Yuna、Luna、Rainie 的 Soul 沒有 6 張驗證紀錄。
- **修改**：每份 prompt 只改一處光線句，把畫面外器材（reflector、key light）改寫成畫面效果，其餘逐字等於已接受原文。產生器逐張核對過：器材字 0、8 個攝影欄位英文句都在、描述順序與 V-Iris 相同。
- **報價**：2026-10-21 用不扣款預檢查了 5 張，每張 credits 1／credits_exact 0.12，合計 0.60。建議整批預算上限 1 credit。工具沒有強制上限，靠一次送一張、每張查交易來控制。
- **預檢前後的交易**：沒有新增 Soul V2 列。新增 1 列 GPT Image 2.5 −1（05:12:22Z），經唯讀查生成紀錄確認是帳號上他人的 gpt_image_2_5 任務；同一段時間沒有任何 soul_2 任務。紀錄：`m4_r4/readonly_queries_2026-10-21.json`。

## 4. 驗證

| 項目 | 結果 | 檔案 |
|---|---|---|
| M-4 R4 定向驗證，涵蓋：Iris 定案紀錄；企劃 v10 與 24 套不變；證據不刪不改；5 位資料（Soul、prompt＝原文＋改寫、器材字、攝影欄位、設定、報價）；CAL_21；公開內容（無私有 ID、無交易原始資料、主頁無 prompt）；桌機與 390px 主頁與歷史頁；三筆 localStorage 不變；溢出；JS 錯誤 | 線上 65/65、本機 65/65 PASS | `m4_r4/live_m4r4_tests.tsv`、`m4_r4/local_m4r4_tests.tsv` |
| 部署前後保留（同一測試瀏覽器設定檔） | 部署前 6/6、部署後 6/6 PASS | `m4_r4/live_upgrade_m4r3_to_m4r4.tsv` |
| 線上檔案 sha256 | 672 檔不符 0；5 個 HTML 頁與本機相同 | `m4_r4/live_bytes_check.txt` |
| 網站建置器 `--check` | PASS 657 檔（目前檢視頁 3 檔；反光板裁切已不再發佈）；公開檔無私有識別碼、無交易原始資料 | — |
| 企劃文件產生器 `--check` | PASS（含 CAL_21 逐張核對；CAL_19 不變） | — |
| kol-catalog 首頁 | 與存檔相同（44,801 bytes） | `m4_r4/live_bytes_check.txt` |

## 5. 剩餘阻礙

1. 主管覆核 5 份 prompt、設定與費用；通過後另發整批生成指令。本輪不生成。
2. 16:9 的實際輸出像素未知。若輸出是 2048×1152，套進 192×104 mm 約 271 ppi，低於本案 300 ppi 工作目標。要等 H-Yerin、H-Jia 生成後實測。
3. 碰撞紀錄：Jia–Somi、Yerin–Rin 都在本批，各自一張。之後的頁面與送審資料不並排展示這兩組（C-2）。
