TASK-CAL-001／M-3｜12 位人設專業寫真拍攝規劃｜送審報告

# M-3 寫真拍攝企劃｜送審紀錄

- **範圍**：只做研究、企劃、prompt 草稿與決策展示。**本輪生成 0 張（含測試圖、示意圖）、credits 0、訓練 0**；沒有改 canon、Soul ID 或人設；沒有聯絡廠商、上傳廠商編輯器、下單或製作交印包。
- **成果 commit**：`256859b3d6bb77b7647837ccdcc14428dcdb7744`（企劃主體 `2a59332`＋公開資料措辭修正 `256859b`；上一版 `5cd303a`；素材頁 `b8108eb`；桌曆基準 `4fd3995`）
- **部署**：Railway `cal2027-decision`，來源固定在 `256859b`，deployment `8c249dad-f10a-4559-895c-b0d73118f6df`（SUCCESS）。中間版 `2a59332` 的 deployment `8cd2d1c1` 已被取代（見 §6）。
- **企劃頁**：https://cal2027-decision-production.up.railway.app/shoot.html（免登入；素材頁 `/` 照舊）
- 以下驗證全部是 **Claude 自測**，不是主管的獨立驗證；部署不等於核准。

## 1. 交付物

| 交付 | 位置 |
|---|---|
| 完整企劃（Aaliya 證據表、12 位差異表、每位主／替代方向、prompt 草稿、構圖策略、成本與試拍提案、問題） | `docs/calendar/CAL_18_M3_SHOOT_PLAN.md` |
| 企劃資料（人寫，頁面與文件都由它產生） | `docs/calendar/data/cal_m3_shoot_plan.json`（shoot-plan-v1） |
| 文件產生器（`--check` 核對文件與資料一致） | `docs/calendar/tools/build_cal_m3_plan_doc.py` |
| 決策頁新頁 | `docs/calendar/decision_site/public/shoot.html`、`shoot.js`、`shoot.css` |
| 建置程式（新增 Aaliya 預覽與 m3 資料） | `docs/calendar/tools/build_cal_decision_site.py` |
| 截圖與測試結果 | `review/calendar/m3_shoot_plan/` |

## 2. 讀了什麼（定向，不掃整個 repo）

- 名單與素材：`docs/calendar/data/cal_m1_owner_roster.json`、`cal_m1_materials.json`、`CAL_17_OWNER_ROSTER_DECISION.md`。
- 12 位的 `kols/<id>/profile.json`（外型、髮色、身材、支柱、配色、brand_dont）；`PERSONA_CANON.md`、`SEXY_SCENE_LIBRARY.md` 的規則段。
- Aaliya：`kols/aaliya-okonkwo/`（profile、README、generation_notes、images）；型錄分支 `claude/kol-dashboard-catalog-gqw9jz` @ `d3fb91ab87547bfa04ee46cf4cfddd6750fcfe52` 的 `catalog/data/selection.json`；型錄頁 HTML。三個版本的圖片 git blob 逐一相同，沒有混用不同版本。
- 成本：`review/soul_training/FINAL_REPORT.md`（交易明細）與既有 generation_notes 的預檢紀錄。
- 模型：Higgsfield `models_explore(get, soul_2)` 唯讀查詢 1 次。

## 3. Aaliya 研究的重點

- 資料夾 `aaliya-okonkwo`、profile id `aaliya-rivera`；README 寫明是歷史原因。本輪不改。
- 型錄頁 12 張＝repo 的 soul_test_v1 8 張＋face_reference 4 張。
- **紀錄缺口（照實寫）**：soul_test_v1 的紀錄明寫「生成記錄遺失」——模型、prompt、Soul 使用都只能推定；face_reference 是 Soul 訓練輸入，模型只有他人筆記的轉述（seedream_v4_5，未確認）。所有檔案沒有中繼資料；後製／裁切／增強無紀錄，列為未知。
- 入選 5 張（不同形式）：黃金時段逆光斜倚、側光插腰、夜間暖燈坐姿、戶外硬光全身、坐姿遠景留白。自拍 2 張刻意不用。
- 移植的是方法（主光／補光、背景層次、人物比例、服裝材質、表情、姿態、鏡頭感、色彩與皮膚），**不用 Aaliya 的臉當任何人的身分參考**，也不複製她的服裝、場景或 prompt。

## 4. 企劃摘要

- 12 位都有主方向＋替代方向、與人設核對、甜美與性感元素、風險與處理、橫直兩段 prompt 草稿（未執行）。
- 對主管起始方向的調整：
  - Somi：純棚拍會失去吃播人設 → 復古小吃店棚景＋手拿炸雞（保留暖色棚拍）。
  - Luna：童顏＋花園＋小洋裝容易顯小 → 合身腰線、低跟涼鞋、首飾，不用白襪與娃娃裝。
  - Tammy：與 Rainie 同為貼身洋裝 → 白天、熱粉、白色建築的型錄外拍。
  - Rainie：brand_dont 不呈現飲酒 → 畫面不放酒杯酒瓶。
  - 其餘 8 位沿用起始方向，補足細節。
- 首批試拍建議：Iris、Rin、Miu、Mia。
- 仍然接近的地方（窗光 3 位、大笑 5 位、棚拍 3 位、既有碰撞配對）照實列出，**不宣稱已消除**。

## 5. 頁面

- 一、Aaliya 參考 5 張＋警語＋方法；二、Penny 喜歡的 4 張（仍是備選，沒有轉成主照片）；三、12 位企劃卡；四、橫直構圖；五、試拍與成本；六、回饋與複製。
- 每張卡：辨識用正臉、2 張既有照片參考（標「既有照片參考：不是新成品，不會照抄」）、橫 3:2／直 3:4 兩個「尚未生成」框、白話企劃；技術細節與 prompt 收在展開區。
- 回饋：每位「接受主方向／改用替代方向／想修改」＋備註；橫直構圖、首批試拍兩題；整體備註；「複製回饋」。存在新的 `cal2027-shoot-v1:<SHA>`。
- 素材頁（`/`）只加了兩個連結；素材選擇的 localStorage 不讀、不寫、不刪。
- 公開資料不含 Soul ID、job_id 或 repo 路徑（建置時檢查）。Aaliya 預覽是固定 commit 原圖等比縮小（長邊 1600、JPEG q88），沒有生成或修圖。
- 先前發佈的 644 個檔案位元組完全不變；新增 10 個（Aaliya 5 張×預覽／縮圖），共 654 個；`--check` PASS。

## 6. 自測結果

全部是 Claude 自測。線上＝https://cal2027-decision-production.up.railway.app（`256859b`）。

| 項目 | 結果 | 檔案 |
|---|---|---|
| 企劃頁（桌機 1366＋手機 390）：免登入、noindex／CSP、公開資料無 Soul ID／job_id／repo 路徑、生成數 0、第一行輪次字串、5 張 Aaliya＋4 張 Penny 參考、12 張卡（各 2 張既有參考＋2 個「尚未生成」框）、prompt 收合且標示未執行、57 張圖全部載入、收合與全部展開都沒有水平溢出、回饋儲存／重新整理保留／複製內容、放大檢視、清除單人與全部、素材頁 localStorage 位元組不變、無 JS 錯誤 | 線上 74/74 PASS（本機同為 74/74） | `m3_shoot_plan/live_shoot_page_tests.tsv` |
| 素材頁回歸（第二階段原測試，依修正輪更新兩條過時的期望值） | 線上 123/123 PASS；同一份測試在上一版 `b8108eb` 本機也是 123/123 | `m3_shoot_plan/live_materials_page_tests.tsv` |
| 升版保留：同一個瀏覽器設定檔在 `5cd6c23` 時寫入的素材選擇與確認，升到 `256859b` 後位元組相同、狀態不變（桌機＋手機） | 44/44 PASS | `m3_shoot_plan/live_upgrade_preservation_tests.txt` |
| 線上 664 個檔案（manifest 654＋頁面腳本）與本機逐一比對 sha256；4 個 HTML 只差注入的 commit | 不符 0 | `m3_shoot_plan/live_bytes_check.txt` |
| 型錄站 kol-catalog 首頁 | 與本輪開始前位元組相同（200，44801 bytes）；其他 service 沒有新部署 | — |

**過程中發現並處理的問題（照實記錄）：**

1. `2a59332` 上線後，跑第二階段原有測試，「公開資料沒有 soul_id」這條失敗。原因：企劃文字寫了 soul_2 的**參數名稱** `soul_id` 與一個 Soul 總表的檔名，**沒有任何 ID 外流**。已改寫措辭，建置程式也加上同樣的檢查（`256859b`），重新部署後通過。
2. 同一份原有測試另有 2 條失敗：泳裝分區、Coco 清理版措辭。這兩條在上一版 `b8108eb` 本機也同樣失敗，是上一輪依主管指示改了分區與措辭、測試沒跟著更新。已在測試副本中更新期望值，原測試檔保留不動。
3. 企劃頁的放大檢視在線上第一次測試失敗：測試在點開後立刻檢查大圖，線上載入需要時間。改成等待載入（30 秒內）後通過，頁面程式沒有改。

**截圖**（線上、乾淨瀏覽器、隱藏底部列）：`review/calendar/m3_shoot_plan/live_desktop_top.jpg`、`live_desktop_aaliya.jpg`、`live_desktop_owner_picks.jpg`、`live_desktop_people_overview.jpg`、`live_desktop_card_iris.jpg`、`live_desktop_card_iris_expanded.jpg`、`live_desktop_card_somi.jpg`、`live_desktop_card_miu.jpg`、`live_desktop_composition.jpg`、`live_desktop_cost.jpg`、`live_desktop_feedback_example.jpg`（回饋為示範輸入，未儲存到任何人的瀏覽器）、`live_mobile390_top.jpg`、`live_mobile390_card_rin.jpg`、`live_mobile390_owner_picks.jpg`。

## 7. 操作紀錄

| # | 動作 | 性質 |
|---|---|---|
| 1 | `git fetch` 型錄分支 `claude/kol-dashboard-catalog-gqw9jz`，讀 `catalog/data/selection.json`（`d3fb91a`） | 唯讀 |
| 2 | `curl` 型錄 Aaliya 頁、型錄首頁（前後比對） | 唯讀 |
| 3 | Higgsfield `models_explore(get, soul_2)` 1 次 | 唯讀查詢；沒有 get_cost、生成、上傳、訓練 |
| 4 | 本機建置：`build_cal_decision_site.py`（只縮小既有圖片）、`build_cal_m3_plan_doc.py` | 本機 |
| 5 | commit `2a59332`、`256859b`，push 到 `claude/epic-carson-n5w0qu` | 沒有合併 main、沒有開 PR |
| 6 | Railway `cal2027-decision` 來源固定到 `2a59332`（deployment `8cd2d1c1`），再固定到 `256859b`（deployment `8c249dad`，SUCCESS） | 只動這個 service |
| 7 | 本機另開上一版 `b8108eb` 的暫時 checkout 跑同一份測試，完成後刪除 | 本機 |
| 8 | Playwright 本機與線上測試、截圖 | 不寫入任何人的瀏覽器資料 |

**本輪數字：** 生成 0、credits 0、訓練 0、Higgsfield 寫入類呼叫 0、聯絡廠商 0。
