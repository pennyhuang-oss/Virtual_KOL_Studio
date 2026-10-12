# 第二階段：為入選人設挑照片——送審（TASK-CAL-001｜2027 KOL 桌曆決策頁）

- **狀態**：依 Penny 最新決定，名單已確認、取消登入，主入口改成第二階段挑照片，已部署。等待主管覆核與 Penny 選素材。沒有執行 R4 技術收尾，沒有製作交印包。
- **頁面**：https://cal2027-decision-production.up.railway.app（公開可讀，不需登入）
  - 第二階段挑照片：`/`
  - 第一階段選角（參考）：`/cast.html`
  - 原推薦方案參考（舊版決策頁）：`/plan.html`
- **成果 commit**：`5cd6c23fcdfa5becc62a976599dc4459adcd5ee0`
- **部署版本**：Railway service `cal2027-decision`，deployment `824dad25-fd61-473a-ad57-56bf175092e1`（SUCCESS；刪除帳密變數後自動重部署同一 commit），來源固定在 `5cd6c23`
- **素材基準 SHA**：`4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45`
- 以下驗證全部是 **Claude 自測**（Playwright 自動化＋截圖），**不是主管的獨立驗證**。

## 1. Owner 決策紀錄

- 文件：`docs/calendar/CAL_17_OWNER_ROSTER_DECISION.md`；資料：`docs/calendar/data/cal_m1_owner_roster.json`（version `roster-v1`）。
- 內容：
  - 12 位由 Penny 在對話中確認（「我選完了」）：iris-chen、luna-tanaka、somi-oh、coco-wu、mia-huang、yuna-kim、tammy-chou、rin-ayase、rainie-hsu、miu-shiraishi、jia-seo、yerin-han。順序不是月份順序。
  - 相對原推薦：移除 Kanon、Angel、Vicky；加入 Miu、Jia、Yerin。
  - 名單確認**不等於**照片、月份、版面或交印核准。
  - 取消帳密由 Penny 授權，她同意展示頁公開可讀。
  - 相似度疑慮照錄、不否決名單：Miu–Jia 0.01219、Miu–Somi 0.01894、Jia–Somi 0.01986、Yerin–Rin 0.02085（≤0.0220）；Somi–Tammy、Iris–Rainie 為 R2 目視提示；Iris、Luna、Coco、Mia、Yuna、Rainie 沒有量測。
  - 另記一項待版面階段處理的風險：`PERSONA_CANON.md` 原則七 C-2「有碰撞關係的兩位不得同框」。若封面用 12 人格，上面 4 組會同框。只提出，不決定版面。
- 頁面「Penny 已確認的 12 位」由這份紀錄產生，不看 localStorage。之後改名單只能另建新版本，不覆寫 `roster-v1`。
- 第一階段選角頁的複製文字仍標「草稿」，依指示不要求 Penny 回頁面重新確認。

## 2. 取消登入

- `server.js`：移除 HTTP Basic（驗證、401、失敗次數限制、沒設帳密回 503）。保留 `X-Robots-Tag: noindex…`、`robots.txt` 全站 Disallow、CSP（`connect-src 'none'` 等）、路徑穿越檢查。
- 頁面與 README 寫明：noindex／robots 只是請搜尋引擎不要收錄，**不能保證**沒有人搜尋到或打開。
- Railway：`DECISION_USER`、`DECISION_PASS` 從 `cal2027-decision` 移除（見第 7 節操作紀錄）。其他 service 沒有改。
- 公開內容只有本案展示照片與選擇資料。自動檢查：公開的 `data.js` 不含 `job_id`、`hf:`、`soul_id`、`kols/` 路徑；頁面不含帳密字樣。

## 3. 第二階段頁面

- 主入口 `index.html`：「第二階段：為入選人設挑照片」。頁首有名單版本、素材基準 SHA、頁面版本與流程（① 選人、② 確認名單已完成）。不問月份、版面、品牌、Logo、QR。
- 「Penny 已確認的 12 位」：12 張頭像與逐人進度（橫／直／備選數、狀態），點了跳到該位。
  - 可展開的相似度疑慮說明。
  - 如果瀏覽器裡有第一階段選角或舊版決策資料，只顯示提示：說明它與名單是否相同、保留在原頁、不算照片核准。從不寫入、轉換或刪除。
- 每位一個素材區：
  - 姓名、本名、辨識頭像（與選角頁同一張，標「不是素材」）；
  - 主要候選，以及可展開的「更多素材」；
  - 每張卡片：
    - 固定素材 ID（例 `iris-01`）；
    - 版本標籤（原圖・未修圖／R3 局部清理版）；
    - 低解析標籤、R3 舊推薦（參考）標籤；
    - 表情／造型／場景、來源類別與原圖尺寸；
    - 待修或注意事項、檢查方式；
    - 「選作橫式照片」「選作直式照片」「列為備選」三個按鈕。
  - 可展開的素材說明：缺口、未列出張數（依理由分類）、這位的相似度紀錄。
  - 這位的備註欄。
- 規則：
  - 每位橫式、直式各最多一張主照片，可以同一張。再按一次就取消。
  - 備選不限張數。已選作主照片的那張不能同時是備選；把備選選成主照片時，它會自動離開備選。
- 照片能否滿版、裁切後 ppi 夠不夠，頁面寫明要排版時才判斷，不下結論。R3 樣張只在參考頁，不限制選擇。

## 4. 素材盤點與篩選

- 範圍：只看 12 位的 calendar 紀錄、`kols/<12 位>/images/`、daily140 縮圖與既有快取。
  - R2 取回原圖：Somi、Tammy、Rin 的 daily_v2。
  - R3 清理輸出：iris_V、coco_H、coco_alt01、rin_V、rainie_H。
- 篩選標準：
  - 臉與定案人設一致；
  - 手、肢體、服裝沒有重大異常；
  - 表情、角度、造型、場景要有差異；
  - 近似重複只留一張。
- 檢查方式在每張卡片上標明，分三種：
  - 「R2 原圖已查」：沿用 R2 紀錄；
  - 「本輪目視（縮小檢視，未逐張 100%）」；
  - 「縮圖目視（360×480）」。
- 人寫清單：`docs/calendar/data/cal_m1_materials.json`。每位都有 `items`（發佈），以及 `excluded`（每張未發佈照片的理由，**不上公開頁**）。

| # | 人設 | 主要候選 | 更多素材 | 來源 | 缺口 | 未列出（理由） |
|---|---|---|---|---|---|---|
| 1 | Iris | 10（含清理版 1） | 12 | repo 21、R3 清理 1 | — | 66：尺度 56、近似重複 8、瑕疵／不宜公開 2 |
| 2 | Luna | 10 | 12 | repo 22 | — | 20：近似重複 17、臉不符 2、瑕疵 1 |
| 3 | Somi | 8 | 2 | repo 5、R2 取回 5 | — | 2：近似重複 |
| 4 | Coco | 12（含清理版 2） | 7 | repo 17、R3 清理 2 | — | 7：第一輪退回臉 4、尺度 2、退件檔 1 |
| 5 | Mia | 10 | 5 | repo 15 | — | 7：第一輪退回臉 4、近似重複 3 |
| 6 | Yuna | 10 | 10 | repo 20 | — | 23：近似重複 20、檔名標示失敗 2、頭部傾斜 1 |
| 7 | Tammy | 8 | 3 | repo 5、R2 取回 6 | — | 1：近似重複 |
| 8 | Rin | 9（含清理版 1） | 2 | repo 5、R2 取回 5、R3 清理 1 | — | 2：近似重複 |
| 9 | Rainie | 11（含清理版 1） | 3 | repo 13、R3 清理 1 | — | 35：非定案臉（training_v1、face_reference、舞蹈起始畫面） |
| 10 | Miu | 8 | 0 | repo 5、縮圖 3 | daily 032／034／035 原圖未取回 | 2：近似重複（原圖也未取回） |
| 11 | Jia | 9 | 1 | repo 5、縮圖 5 | daily 021／022／023／024／025 原圖未取回 | 2：近似重複 |
| 12 | Yerin | 9 | 0 | repo 5、縮圖 4 | daily 086／087／089／090 原圖未取回 | 8：選角前期臉 4＋身形失敗 1、肢體變形 1、近似重複 2 |

合計發佈 171 張：
- 高解析預覽 159 張：repo 原圖 138、R2 取回 16、R3 清理 5。原圖等比縮小，長邊 1600 px，JPEG q88。
- 低解析縮圖 12 張：位元組不變複製。

### 4.1 需要主管知道的剔除與判斷

- **Iris 的內衣／泳裝／暗示裸露系列不上公開頁**（56 張）：
  - 涵蓋 `daily_sexy_night_v1–v4`、`drive_v1`（同一批的重複檔）、`selfie_expression_v6`、`lingerie_mirror_r1`、`onsen_bucket_r1`、`dance_clone_r15`（泳裝）、`daily_expression_v5` 的內衣張。
  - 理由：`CAL_04` D2 把這級列為 C（只作參考、要用需先問廠商），而且本頁已經公開。
  - 同系列中屬於 B 級的照片仍列在「更多素材」：緞面睡裙、運動內衣、米白短洋裝。
  - 另有 `06_bathroom_counter` 一張，原圖放大後可見裙下內褲，不放。
  - **若 Penny 要用這一級，需另外決定是否放上公開頁。**
- **Coco 的比基尼兩張**（dance_clone_r12／r13）：同上，不上公開頁。
- **Yerin `casting_v1` a01–a04 臉不符**：
  - 這是選角前期圖，早於 2026-09-01 定案的 identity master。目視臉與 identity master 及 Soul 訓練集 `training_v1` 不同。
  - 第一階段選角頁的 Yerin 卡片用的是 `training_v1` 與驗證圖，不受影響。
- **Rainie**：只用定案臉 `training_v2`（`CAL_02`：舊資料夾是另一張臉，不可混用）。
- **Coco／Mia `round1_candidate_*`**：被退回的第一輪臉部候選。
- **Luna dance_clone_r16／r17**：目視臉不一致。人設紀錄也記載這兩支的起始畫面有身分落差。
- **Yerin daily 088**：daily 審查標記「肢體變形」，不放主候選。原圖也未取回。

### 4.2 待修項（摘要；全部在卡片上標示）

- 背景 AI 假字：
  - Iris 街拍招牌（iris-01；iris-02 是清理版，「完成，但近看看得出」）；
  - Luna 爆米花桶與假 IG 介面；
  - Somi 紙袋（R3 試修撤回，未處理）；
  - Yuna 毛衣字樣（必修）；
  - Mia 帽 T 字樣。
- 背景路人：
  - Somi #063／#065、Tammy 頂樓與白襯衫、Rin #053（rin-03 是清理版）；
  - Jia、Miu、Yerin 的 daily 照片（daily 審查標記）。
- 牆上人像是本人的臉：Tammy #072、Miu #032、Jia #025。
- 可辨識角色：Coco 的 Hello Kitty 手機殼。
  - coco-03 原圖，coco-04 清理版；
  - 清理版狀態「部分完成」，頁面寫明**修補不完全自然**：修補區紋理較平，左緣與下緣在 100% 下看得出。
- 其他：Rainie 假日期戳（rainie-01；rainie-02 清理版完成）、手機閃光、雜亂背景、他人入鏡（Coco 宿舍系列、Mia 咖啡座）。
- 版本區分：原圖一律標「原圖・未修圖」；R3 清理版另有 ID、標「R3 局部清理版」與狀態。目前**沒有**任何正式修圖版。

## 5. 互動與輸出

- 選擇只存在 localStorage（`cal2027-materials-v1:<SHA>`），不送伺服器。
  - 與 `cal2027-casting-v1:<SHA>`、`cal2027-decision-v1:<SHA>` 分開。
  - 「重設全部素材選擇」只清自己的 key。
- 「確認目前已選素材」：確認視窗列出每位的橫／直照片與備選，**完全沒選的人標「未選（不會被確認）」**。
- 確認後只要改這位的任何一張（即使改回原樣），這位就回到草稿，其他人不受影響。備註是自由文字，不屬於確認項目。
- 可分批選、隨時複製。複製文字含：
  - 名單版本 `roster-v1` 與紀錄檔路徑、素材基準 SHA、素材清單 git blob、頁面版本；
  - 每位的橫式／直式主照片 ID（附標註，低解析的會註明）、備選、狀態、備註；
  - 整體補充意見；
  - 「月份、版面、修圖與印刷可用性都還沒決定」「品牌、Logo、QR 本輪不需要」「不是主管核准」。

## 6. 驗收（Claude 自測）

線上部署 `824dad25`（commit `5cd6c23`），Playwright 桌機 1366 px＋手機 390 px（isMobile、3x）：**123／123 PASS**（`review/calendar/materials_stage2/live_test_results.txt`）。本機也是 123／123。

| 要求 | 結果 |
|---|---|
| 1. 無帳密可進頁面、看圖、讀資料 | 不帶任何憑證：`/`、`/index.html`、`/mat.js`、`/data.js`、`/cast.html`、`/plan.html` 與素材圖片都是 200，沒有 `WWW-Authenticate`。`X-Robots-Tag: noindex…`、CSP、`robots.txt` Disallow 都保留。`/%2e%2e/server.js` 回 404 |
| 2. 恰好顯示 owner 確認的 12 位 | 名單區與逐位區都恰好 12 位，順序與 `roster-v1` 相同；沒有 Kanon、Angel、Vicky |
| 3. 橫、直、備選各自獨立，不連動其他人 | 測過：Iris 橫 iris-03／直 iris-01／備 iris-04＋iris-12；Luna 橫直同一張 luna-02；Yerin 只選直式（低解析縮圖）。其他 9 位維持未選。已選主照片的「列為備選」停用；把備選選成主照片時自動離開備選 |
| 4. ID、姓名、來源一致，沒有破圖 | 171 張卡片的 ID、所屬人、標註、圖片檔、主要／更多分區都與 `cal_m1_materials.json` 逐一一致。展開「更多素材」後所有縮圖載入。低解析標示只在 Miu／Jia／Yerin 的 12 張縮圖。R3 清理版 5 張分開標示。Coco 清理版寫明「修補不完全自然」 |
| 5. 放大、保存、重新整理、確認撤銷、複製 | 放大顯示高解析預覽，標題有 ID、來源、原圖尺寸、「未排版」；可切原尺寸，按鈕或 Esc 關閉。重新整理後選擇、確認、備註都保留。確認後取消一張備選回到草稿，改回原樣仍是草稿，且只影響那一位；改備註不撤銷確認。複製文字內容完整（範例 `live_copy_example.txt`） |
| 6. 未回答仍是未回答；舊選角不算照片核准 | 先放入第一階段選角資料（已確認的舊 12 人）與舊版決策資料：頁面只顯示提示，素材全部「未選」。複製文字裡未選的 9 位寫「未選（不算核准）」。操作、開選角頁與參考頁、重設全部後，兩份舊資料都沒有被改寫 |
| 7. 無水平捲動；型錄未受影響 | 兩種寬度、展開全部、有「已確認」狀態時都沒有橫向捲動（本機自測時抓到手機版名單卡的狀態標籤撐寬 10 px，已改成短標籤並重測）。型錄 https://kol-catalog-production.up.railway.app/ 回 200、44801 bytes，與部署前位元組相同；`kol-catalog`（eabb3a25）與 `897-audition`（90a81d86）的 deployment 沒變 |
| 線上檔案與 commit 一致 | 不帶憑證抓 614 個檔：manifest 列出的 606 個加上頁面 JS／CSS，與 commit 內容 sha256 全部相同。3 個 HTML 注入的頁面版本都是 `5cd6c23…` |
| 產生物可重現 | `build_cal_decision_site.py --check --hf-dir … --clean-dir …`：PASS，606 檔（copy 122、crop 11、高解析預覽 170、thumbnail 303），問題 0 |
| 沒有 console 錯誤、沒有失敗請求 | 兩種寬度都 0 |

## 7. 實際外部操作紀錄

| 時間（UTC） | 操作 | 對象 |
|---|---|---|
| 09:34 | commit 並 push `5cd6c23` 到 `claude/epic-carson-n5w0qu` | GitHub（未合併 main、沒有開 PR） |
| 10:04 | `connect-service-source`：來源固定到 commit `5cd6c23` | Railway `cal2027-decision`；deployment `9ff22cff` SUCCESS（10:11） |
| 10:12 | 確認新版線上不需登入（`/mat.js` 200） | 唯讀 |
| 10:13 | 刪除變數 `DECISION_USER`、`DECISION_PASS`（Railway agent 代為執行，只限這兩個變數）；觸發同一 commit 重部署 `824dad25`，10:19 SUCCESS | Railway `cal2027-decision`。之後用 `list-variables` 確認兩個變數已不存在，其他設定未變 |
| 10:12–10:21 | 線上驗收：byte 比對、Playwright 兩輪、型錄唯讀比對；重部署期間每 20 秒檢查一次，沒有非 200 | 唯讀 |

- 沒有修改其他 Railway service（kol-catalog、897-audition），沒有新增付費附加服務。
- 沒有呼叫 Higgsfield，沒有重新下載外部素材；只用 repo 檔、R2 已取回快取（sha256 核對）與 R3 清理輸出（clean_sha256 核對）。
- 沒有生成、沒有花 credits、沒有聯絡廠商、沒有上傳廠商編輯器、沒有下單。

## 8. 覆核檔案

- Owner 決策：`docs/calendar/CAL_17_OWNER_ROSTER_DECISION.md`、`docs/calendar/data/cal_m1_owner_roster.json`
- 素材清單（含剔除理由）：`docs/calendar/data/cal_m1_materials.json`
- 頁面：`docs/calendar/decision_site/public/index.html`、`mat.js`、`mat.css`；`server.js`；`README.md`
- 產生與核對：`docs/calendar/tools/build_cal_decision_site.py`（`--check`）；`docs/calendar/decision_site/ASSET_MANIFEST.json`（來源、hash、處理；不對外提供）
- 截圖：`review/calendar/materials_stage2/`（線上部署，桌機 1366 px 與手機 390 px）

## 9. 請主管確認

1. Iris 的內衣／泳裝／暗示裸露系列（及 Coco 比基尼）不上公開頁，是否同意？若 Penny 要看，要另行決定呈現方式。
2. Yerin `casting_v1` 4 張判定為臉不符而剔除，是否同意？
3. Miu、Jia、Yerin 的 daily 照片只有 360×480 縮圖（共 12 張）。若 Penny 選中，之後是否取回原圖由主管決定，本輪沒有取回。
