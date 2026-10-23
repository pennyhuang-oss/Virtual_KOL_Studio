TASK-CAL-001／M-4／R5｜Railway 選片與回饋頁部署收尾｜送審報告

# M-4 R5 送審紀錄

- **選片頁網址**：https://cal2027-decision-production.up.railway.app/shoot.html（**已上線**：2026-10-23 13:26 UTC 部署成功，線上 page-commit＝`f04bc3d`，見 §6）
- **部署成果 SHA**：`f04bc3d06c28ece44983f2f7ddd740021c33aa33`（選片頁；照片固定成果 `a95e52feb0858f28de7ffbd6a105215d8f961f87`；原圖與私有紀錄 `b7784f697883b99c28aaf85b9c36c2c3b3415415`；基準：成果 `b5cbe1c563df4a6252cc842ceeaccc2d358e2e6b`、送審 `d09975652a751dd17a45d2aaf5c83b4dc4b18f5c`）
- **集中紀錄**：`docs/calendar/CAL_22_M4_BATCH1_RESULTS.md`（最終送出文字、差異、驗收、像素與 ppi、逐筆扣款）。資料：`docs/calendar/data/cal_m4_batch1_run.json`；主管指令逐字：`docs/calendar/data/cal_m4_auth_r5.json`；私有執行紀錄（含工作 ID）：`review/calendar/m4_r5/execution_log.json`。
- 以下是執行者自測，不是主管覆核；部署不等於核准；照片接受與否由 Penny 在審圖頁決定。

## 1. 各角色請求與結果

| # | 套別 | 請求 | 結果 | 原圖（私有 repo） | 像素 | 套框有效 ppi |
|---|---|---|---|---|---|---|
| 1 | V-tammy-chou | 1 次（06:59 送出） | 完成 07:00 | `kols/tammy-chou/images/calendar_2027_batch1/V-tammy-chou_m4r5.png` | 1536×2048 | 325 |
| 2 | V-rin-ayase | 1 次（07:01） | 完成 07:01 | `kols/rin-ayase/images/calendar_2027_batch1/V-rin-ayase_m4r5.png` | 1536×2048 | 325 |
| 3 | V-somi-oh | 1 次（07:04） | 完成 07:05 | `kols/somi-oh/images/calendar_2027_batch1/V-somi-oh_m4r5.png` | 1536×2048 | 325 |
| 4 | H-yerin-han | 1 次（07:08） | 完成 07:09 | `kols/yerin-han/images/calendar_2027_batch1/H-yerin-han_m4r5.png` | 2048×1152 | 271（低於 300 工作目標） |
| 5 | H-jia-seo | 1 次（07:29） | 完成 07:30 | `kols/jia-seo/images/calendar_2027_batch1/H-jia-seo_m4r5.png` | 2048×1152 | 271（低於 300 工作目標） |

- 共 5 次請求、0 次重試、0 次失敗；修圖 0、放大 0、訓練 0。本批請求已用完，不再送。
- 送出前：5 個 Soul 都是 ready、與各自 profile.json 一致；偏好 auto_create_project false，不建專案、不指定資料夾；設定 soul_2、2k、count 1、use_unlim false、無參考圖、不傳 style_id。
- 中斷：第 5 張寫下提交意圖後執行環境重啟。送出前查過私有紀錄沒有工作 ID、帳號生成紀錄沒有新的 soul_2 任務、交易沒有新的 Soul V2 列，確認沒有重複提交後重新報價（0.12）並只送 1 次。

## 2. 最終送出文字

- 只改 V-Rin 一句：`Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees,` → `Shot: framed from a little above her head down to her upper shins just below the knees,`；中文標示「拍至膝下小腿上段，不切膝關節」。
- 其餘 4 份逐字等於 CAL_21 送審版。5 份全文在 CAL_22 §2；文件產生器逐字比對送出文字＝CAL_21 原文（＋V-Rin 授權修正），sha256 也和送出前寫下的提交意圖相同。

## 3. 驗收摘要（完整逐項見 CAL_22 §4）

| 套別 | 主管指定重點 | 和企劃最明顯的落差 |
|---|---|---|
| Tammy | 提把與手指正常；雙手都在框內；暖光下膚色不偏黃 | 手提包外型接近某精品經典款（無標誌）；深 V 比企劃低；下緣到小腿、髮頂留白約 14%；花旁小立牌有模糊字樣 |
| Rin | 臉可辨識；扶柱手正常；開衩到大腿上段、遮蔽完整 | 看鏡頭（企劃側臉看港口）；拍成全身赤腳（企劃膝下裁切）；低馬尾（企劃低髮髻） |
| Somi | 眼睛睜開、五官清楚；接雪手不遮臉；大衣敞開 | 右靴鞋頭超出原圖下緣（靴底不完整）；燈籠與招牌有字樣、有交通標誌；天色偏傍晚 |
| Yerin | 雙膝併攏、沒有裙下構圖；雙腳完整；帽簷陰影淡；球車素面（一個看不出字的小徽章） | 雙腳放在踏板上（企劃腳踝交叉點地）；帽頂離上緣約 2.3%；樹沒有葉子 |
| Jia | 交疊腿完整；露肩背與腰線清楚；臉清楚不暗 | 回頭看鏡頭（企劃看湖面）；沒有逆光輪廓；雙手都在膝上；上下留白很緊；皮膚偏光滑 |

- 不從照片宣稱量測出三圍或罩杯。
- 套框：直式 3:4 放滿 120×160 mm、不裁切。H-Yerin 帽頂太靠上緣，4 mm 全部從下緣裁（帽頂約 2.4%、鞋底約 3.9%）。H-Jia 平均裁會切到鞋底，所以上裁約 3.2 mm、下裁約 0.8 mm；髮頂與鞋底都沒切到，但各只剩約 1 mm，任何放法都達不到 4%／3% 工作參考。預覽在 `m4_r5/*_frame_*.jpg`。

## 4. 逐筆扣款、退款與歸屬

| 套別 | 精確報價 | Soul V2 扣款列（UTC） | 金額 | 退款 | 歸屬 |
|---|---|---|---|---|---|
| V-tammy-chou | 0.12 | 2026-10-21T06:59:20.966716Z | −0.12 | 無 | 依時窗及唯一任務推定 |
| V-rin-ayase | 0.12 | 2026-10-21T07:00:57.479119Z | −0.12 | 無 | 依時窗及唯一任務推定 |
| V-somi-oh | 0.12 | 2026-10-21T07:04:27.362109Z | −0.12 | 無 | 依時窗及唯一任務推定 |
| H-yerin-han | 0.12 | 2026-10-21T07:08:16.694715Z | −0.12 | 無 | 依時窗及唯一任務推定 |
| H-jia-seo | 0.12 | 2026-10-21T07:29:31.883249Z | −0.12 | 無 | 依時窗及唯一任務推定 |

- 合計實扣 0.60、退款 0；核准額度 0.60。每張時窗只有一筆 Soul V2 扣款、同一時窗只有本次這一個 soul_2 任務；時窗內其他列是他人其他模型（Nano Banana Pro、Seedream 4.5），不是 Soul V2。
- 15 分鐘複查（07:46 UTC）：本批沒有遲到扣款或退款。07:43:51Z 另有一筆 Soul V2 −0.12，對應帳號上另一個 soul_2 任務（07:43:51Z 建立，不是本批 5 個工作 ID 之一）；本批最後一次送出是 07:29:37Z，之後沒有提交，判定不屬本批。帳號任務只看模型、狀態、時間與 ID，沒有開啟他人作品。
- 工具沒有強制扣款上限；不以整數顯示值當實扣、不以餘額差推算。

## 5. 審圖頁

- 主頁：一行進度、5 位導覽（只有名字、月份與直橫，沒有縮圖），一次只顯示一位：照片、大圖與原尺寸、下載原圖、工作套框、3–4 條看圖提醒、接受／想修改／備註；「複製本批回饋」一次複製 5 張，未回覆標「不算接受」。沒有 5 張並排或接觸表（C-2）。
- V-Iris 移到「已接受紀錄」（看大圖、下載），不再要求回覆；之前的套框預覽不再發佈。
- 回饋存在 Penny 的瀏覽器，一張一個鍵 `cal2027-batch1-v1:<套別>`；打開頁面不寫入，選了或寫了才存；不讀、不寫、不刪舊鍵。
- 公開副本：原圖 PNG 只移除帶工作 ID 的 tEXt 區塊（影像位元組不變）、顯示版長邊 1600、套框預覽位元組不變。主頁沒有 prompt、費用或交易資料；實扣與工作 ID 只在私有紀錄。

## 6. 部署與驗證

**狀態：已部署成功（2026-10-23）。** deployment `3bfa145c-3276-47a4-86c3-548aa8ee04a5`，SUCCESS，來源 `f04bc3d06c28ece44983f2f7ddd740021c33aa33`，線上 page-commit 相符。之前 10-21～10-22 的 7 次部署都因 Railway 平台事故被拒（下表）。

（歷史）只更新 `cal2027-decision`，5 次部署呼叫都被 Railway 拒絕，錯誤訊息相同：`Deploys have been paused temporarily`。

| # | 時間（UTC，約） | 部署來源 | 結果 |
|---|---|---|---|
| 1 | 07:59 | `a95e52f` | 拒絕：Deploys have been paused temporarily |
| 2 | 08:11 | `a95e52f` | 同上 |
| 3 | 08:13 | `a95e52f` | 同上 |
| 4 | 08:41 | `f04bc3d` | 同上 |
| 5 | 09:01 | `f04bc3d` | 同上（之前有限等待 20 分鐘，每 2 分鐘看一次狀態頁，仍未恢復） |
| 6 | 10-22 04:58 | `f04bc3d` | 同上。部署前先查：沒有進行中或新的部署（最新仍是 8116b9c3 SUCCESS／b5cbe1c、pendingWork 空）；連接器已重新連上同一帳號（pennyhuang-oss）與同一 project／service。被拒後停止重試 |
| 7 | 10-22 06:50 | `f04bc3d` | 拒絕，錯誤訊息改為：`Deploys have been paused due to an upstream issue`。部署前先查：帳號 pennyhuang-oss、同一 project／service；沒有進行中或新的部署（最新仍是 8116b9c3 SUCCESS／b5cbe1c、pendingWork 空）；線上 page-commit＝b5cbe1c。狀態頁 06:29 UTC 公告 Pro 與 Enterprise 已可建置，但本次仍被拒；工作區類型為 personal，工具查不到方案別。被拒後停止重試，沒有背景監看 |
| 8 | 10-23 13:13 | `f04bc3d` | **成功**。部署前先查：沒有進行中或新的部署（最新仍是 8116b9c3 SUCCESS／b5cbe1c、pendingWork 空），線上＝b5cbe1c。建立 deployment `3bfa145c-3276-47a4-86c3-548aa8ee04a5`（13:13:20 建立，BUILDING 約 13 分鐘），13:26:41 SUCCESS；舊部署 8116b9c3 隨後轉為 REMOVED。只部署這一次 |

- 平台狀態（10-22 04:57 UTC）：事故升級為「Railway Platform Outage — Major Outage」；Railway 依安全揭露作廢所有 API token（04:17）；建置只先開放 Enterprise（04:00 起），其他方案分批恢復中，04:52 公告「持續為其他方案恢復建置，05:30 UTC 前再更新」。
- 平台狀態（10-21）：status.railway.com「Builds are temporarily paused — Partial Outage」，Builds（US West、EU West、Southeast Asia、US East）、API、Support 都列為受影響；07:24 UTC 開始調查，08:28 UTC 更新「後端也有問題，仍在調查」。不是本專案設定或程式錯誤。
- Railway 狀態查詢（09:0x）：`cal2027-decision` 最新部署仍是 `8116b9c3-578b-424d-baee-5da6500ce147`（SUCCESS，`b5cbe1c`），沒有排隊中的工作；其他 service 沒有動。線上 `shoot.html` 的 page-commit 是 `b5cbe1c`。
- 沒有改存取設定、沒有新增登入或付費服務、沒有另做替代網站。
- **已完成（本機，Claude 自測）**：`--check` 兩個產生器 PASS（網站 671 檔，公開檔無私有識別碼、無交易原始資料）；本機桌機與 390px 定向驗證 80/80（`m4_r5/local_m4r5_tests.tsv`）；部署前保留測試（線上 `b5cbe1c`）6/6（`m4_r5/upgrade_predeploy_b5cbe1c.tsv`）；kol-catalog 首頁與存檔相同（44,801 bytes）。
- **f04bc3d 相對 a95e52f 的差異**：「複製本批回饋」第一行加上照片版本（M-4 R5 第一批 5 張，照片固定成果 a95e52f），合計行明列「已回覆 n／5、未回覆 m」。照片、回饋鍵與已存回饋都不變。

- **原因確認（10-22 06:53 UTC）**：Penny 提供 Railway 後台截圖，本工作區是 **Hobby 方案**。Railway 狀態頁 06:29 UTC 起只開放 Enterprise 與 Pro 建置，公告的恢復順序是 Pro → Hobby → Free／Trial，所以第 7 次被拒是因為 Hobby 尚未開放，不是設定或程式問題。不升級付費方案（本輪限制），等 Railway 對 Hobby 開放後再部署 f04bc3d。

**接續步驟（Railway 恢復後）：**

1. `connect-service-source`（project `d8312837-74c9-40b0-99fc-08cbf0b3faf5`、service `06e24e36-80db-4a26-a02f-51c42ae8722e`、commitSha `f04bc3d06c28ece44983f2f7ddd740021c33aa33`）。
2. 等線上 `shoot.html` 的 page-commit 變成 `f04bc3d`，`list-deployments` 記下 deployment ID 與狀態。
3. 線上驗收：5 張照片實際載入（naturalWidth）、放大與原尺寸、接受／想修改與備註、重新整理保留、複製內容與畫面一致、桌機與 390px 無水平溢出、舊資料不變（同一測試設定檔）、公開檔無私有 ID。
4. 更新本節與送審報告。

### 6a. 線上驗收（2026-10-23，Claude 自測；不是主管獨立覆核，也不是 Penny 接受）

| 項目 | 結果 | 證據 |
|---|---|---|
| 部署狀態與版本 | deployment `3bfa145c-3276-47a4-86c3-548aa8ee04a5` SUCCESS（13:26:41 UTC）；來源 `f04bc3d`；5 個 HTML 頁的 page-commit 都是 `f04bc3d06c28ece44983f2f7ddd740021c33aa33` | `m4_r5/live_bytes_check_f04bc3d.txt` |
| 線上檔案 | 686 個檔與本機（同一版本）sha256 相同，不符 0 | 同上 |
| 線上定向驗收（獨立測試瀏覽器，不是 Penny 的瀏覽器） | 80/80 PASS：5 位導覽（姓名、月份、直橫）；一次一位、5 張實際載入、完整不裁切；放大、原尺寸、下載；接受／想修改、備註、未回覆狀態；重新整理保留；複製內容與畫面一致（任務、頁面版本 f04bc3d、照片版本、已回覆／未回覆數）；未回覆不算接受；桌機 1366 與 390px 無水平溢出；舊三筆 localStorage 不變、V-Iris 已接受紀錄保留；公開內容無 Soul ID、工作 ID、交易原始資料；無 JS 錯誤 | `m4_r5/live_m4r5_tests_f04bc3d.tsv` |
| 部署前後保留（同一個舊測試設定檔） | 部署前（b5cbe1c）6/6、部署後（f04bc3d）6/6；打開新頁不寫任何新鍵 | `m4_r5/upgrade_predeploy_b5cbe1c.tsv`、`m4_r5/upgrade_postdeploy_f04bc3d.tsv` |
| kol-catalog | 首頁與存檔相同（44,801 bytes）；Railway 上最新部署仍是 2026-09-24 的 eabb3a25 | `m4_r5/live_bytes_check_f04bc3d.txt` |
| 截圖 | 桌機第一屏、390px 第一屏、回饋與複製後的桌機與 390px 全頁 | `m4_r5/live_desktop_first_screen.jpg`、`m4_r5/live_mobile390_first_screen.jpg`、`m4_r5/live_desktop_after_feedback.jpg`、`m4_r5/live_mobile390_full_after_feedback.jpg` |

- 驗收用的「接受／想修改／備註」只寫進測試瀏覽器，Penny 的瀏覽器沒有任何回饋；5 張照片仍待 Penny 選片，沒有任何一張標為接受。
- 其他 service 未動；未改存取設定、未新增登入或付費服務、未另建網站、未合併 main。生成 0、修圖 0、訓練 0。

## 7. 主管覆核：部署停止點（來源：Penny 轉交的主管回覆，2026-10-21）

逐字：

```text
TASK-CAL-001／M-4／R5｜主管覆核與部署停止點

主管已核對送審紀錄、shoot.html、review.js、review-data.js
及 f04bc3d 的修改差異。

結論：
- 程式與資料可進入部署。
- 線上交付 BLOCK：Railway 平台故障。
- 本機80/80仍標為Claude自測；尚未完成主管線上驗收。
- 5張照片仍待Penny選片，不得標為接受。

請將本結論保存於本輪送審紀錄，標明來源是Penny轉交的主管回覆。
保留待部署成果：
f04bc3d06c28ece44983f2f7ddd740021c33aa33

現在停止部署重試與持續輪詢，結束本次工作。
不修改既有照片、不新增生成、不修圖，不啟動下一批。
不另建網站、不更改存取設定、不合併main。

Railway恢復、接續本輪時：
1. 先確認服務現況，避免重複部署。
2. 只部署cal2027-decision到上述固定成果。
3. 確認deployment SUCCESS及線上page-commit相符。
4. 完成既定線上定向驗收，不重跑無關全套測試。
5. 先交付可直接選片的網址，再用單一程式碼框回報
   deployment ID、版本、驗收證據與未完成事項。

維持M-4／R5，不另開新輪次。
本指令不要求你在背景持續等待或自動監看。
```

執行者處理：

- 狀態記為：程式與資料可進入部署；**線上交付 BLOCK（Railway 平台故障）**；本機 80/80 為 Claude 自測，主管線上驗收未完成；5 張照片待 Penny 選片，沒有任何一張標為接受。
- 待部署成果保留為 `f04bc3d06c28ece44983f2f7ddd740021c33aa33`。已停止部署重試與狀態輪詢，沒有背景監看。
- 本輪停在這裡：照片不改、不生成、不修圖、不啟動下一批；不另建網站、不改存取設定、不合併 main；仍屬 M-4／R5。
- 接續時依上列 1–5 與 §6 的接續步驟執行。另註：本工作環境的 Railway 連接器目前已斷線、需要重新授權（claude.ai 的 connector 設定），授權恢復前無法查詢服務或部署。
