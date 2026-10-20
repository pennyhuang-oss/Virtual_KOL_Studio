TASK-CAL-001／M-4／R1｜V-Iris首試前核查｜送審報告

# M-4／R1 送審紀錄

- **固定成果 SHA**：`706618f66707087e9a27dbb94f9ee3b9d256fd6f`（基準：成果 `f694e1b0a070942cad5ac247dfd3af7c17efb5b4`、送審 `88e394421aec1221b1704793d0ab2b9ed3b8bd0b`）
- **部署**：Railway 只更新 `cal2027-decision`，固定到 `706618f66707087e9a27dbb94f9ee3b9d256fd6f`，deployment `215e1521-34c3-4991-a36b-446fe6d6141e`（SUCCESS）；其他 service 未動、未合併 main、未開 PR、免登入不變
- **頁面**：https://cal2027-decision-production.up.railway.app/shoot.html（首試前核查在 `#prep`）
- **首試準備與核查文件**：`docs/calendar/CAL_20_M4_IRIS_FIRST_TEST_PREP.md`；唯讀查詢紀錄：`review/calendar/m4_r1/readonly_queries_2026-10-20.json`
- **本輪計數**：生成 0、生成任務 0、扣 credits 0、重試 0、訓練 0、上傳 0、取回新原圖 0；唯讀查詢 7 次（含不扣款的報價預檢 1 次）。
- 以下驗證是執行者自測，不是主管覆核；部署不等於核准。

## 1. 主管結論與 M-3 完成

- 新檔 `docs/calendar/data/cal_m4_supervisor_r1.json`：逐字保存主管結論與 8 項指示。
- 企劃升為 shoot-plan-v8：M-3 complete；23 套已接受；H-luna-tanaka 狀態改為「依owner指示修訂，主管覆核通過」，資料與頁面都寫明 Penny 沒有看過修訂後的版本；沒有待決問題，不再要求 owner 填企劃問卷。
- 24 套與 `f694e1b` 逐欄比對：只有 H-Luna 多了狀態與 M-4 R1 註記；24 段 prompt 逐字相同（V-Iris 已接受 prompt 不變）。
- v1–v6 回饋與素材選擇：頁面只讀、不寫入；部署前後 localStorage 位元組相同。

## 2. 過期前提修正與檢查表差異

- CAL_20 工作流與費用段的前提改為：V-Iris 造型已接受（R4 owner 紀錄；M-3 已完成），不再等待造型核准。生成與費用尚未授權：需要費用核准與主管另發的 M-4 生成指令；在那之前什麼都不送出。
- 主管接受的三項差異（胸口高度不補寫公分、正面看鏡頭、夕陽輪廓光配前方補光）在檢查表標為「與稽核表不同（主管 M-4 R1 接受）」；prompt 不變，出圖後依驗收條件判定。

## 3. Soul 證據

| 項目 | 內容 | 來源檔 |
|---|---|---|
| 身分對應 | 專案內 12 處紀錄指向同一個 Soul（程式比對，ID 不公開）；2026-10-20 唯讀查詢回傳名稱 Iris Chen、類型 soul_2、狀態 ready（completed）。 | `kols/iris-chen/profile.json（ai_assets.training_images_v1.soul_training）`、`kols/iris-chen/generation_notes.md 第 244–1188 行（11 處）`、`review/LEDGER.md 第 94、128–134 行（U-01）` |
| 訓練來源 | 2026-06-25 用 14 張 Seedream 4.5 訓練圖（1920×2560）訓練。不在 2026-09 的 19 位 Soul 總表內，那批另有 6 張驗證協定。 | `kols/iris-chen/profile.json（ai_assets.training_images_v1）`、`review/soul_training/SOUL_IDS.json`、`review/soul_training/FINAL_REPORT.md` |
| 驗證證據 | 沒有 6 張驗證紀錄。以 Iris 為 GOOD 基準的 Retroactive Benchmark 有設計，但沒有執行紀錄。依指示不重訓、不補生 6 張。 | `review/LEDGER.md（U-01、C-08）`、`review/REVIEW.md 第 398 行` |
| 既有成圖 | 本機 Iris 的 soul_2 輸出 73 張：3:4 1536×2048 59 張、9:16 1152×2048 14 張（其中 3:4 的 drive_v1 15 張沒有生成紀錄）。生成筆記明寫 soul_2＋此 Soul、2k、3:4 輸出 1536×2048；6 批有逐張生成後檢查紀錄（手部、規格落差、瑕疵重生）。 | `kols/iris-chen/generation_notes.md 第 969–1014、1042–1101、1176–1248、1261–1453 行` |
| 生產中已知的行為 | 身材還原不穩：部分成圖胸型小於 87 cm／D（第 1007–1010 行）；嘴型多鎖在微笑／笑（第 1436–1446 行），V-Iris 要的是明亮的笑，相容；上身前傾＋靠近鏡頭的姿勢曾觸發拼貼（第 617–628 行），V-Iris 是正面站定，不屬此類。使用者曾裁決 Iris 為 GOOD 基準：「訓練後在生產環境跨場景跨造型使用最久」。 | `kols/iris-chen/generation_notes.md`、`review/LEDGER.md 第 132 行` |
| 目視（縮小檢視，不是量測） | 3 張訓練圖與 6 張不同日期的 Soul 輸出並排：臉型、雙眼皮大眼、唇形與黑色長直髮一致；身材在部分輸出偏纖細。接觸表只存在本機暫存，沒有放進 repo。 |  |
| 結論 | 身分對應確認；沒有正式驗證，但既有生產紀錄支持用「單張首試＋首張驗收」判定。不重訓、不補生 6 張；身材與逆光臉部列入首張驗收。 |  |

## 4. 當前參數、單次請求設定與報價

| 項目 | 內容 |
|---|---|
| 模型 | soul_2（Higgsfield Soul 2.0；說明：Realistic UGC, fashion editorial and character generation） |
| 參數 | quality（1.5k／2k，預設 2k）、Soul ID（選填）、style_id（選填，Soul 風格預設；首試不用）、參考圖最多 1 張（首試不用） |
| 比例 | 1:1、16:9、9:16、4:3、3:4、3:2、2:3 |
| 沒有的參數 | 沒有 seed、沒有 negative prompt、沒有費用上限參數 |
| 免費無限額度 | soul_2 支援，但這個帳號目前不可用（available false、剩餘 null） |
| Soul 狀態 | Iris Chen｜soul_2｜ready（completed） |
| 帳號 | Plus 方案；餘額只作參考（多人共用，不用來對帳） |

| 設定 | 值 |
|---|---|
| 工具 | generate_image（一次一個請求；不用 generate_image_batch） |
| 模型 | soul_2 |
| Soul | Iris 既有 Soul（Iris Chen、ready；ID 依專案紀錄，不公開） |
| quality | 2k |
| aspect_ratio | 3:4 |
| count | 1 |
| use_unlim | false（用 credits 付費） |
| 參考圖／style_id | 不用 |
| prompt | V-iris-chen 已接受 prompt 原文，一字不改（2095 字元） |
| 存放位置 | 依工具規則：送出前先唯讀查 get_preferences 決定是否需要專案資料夾；不自行建立專案（需要時由主管指示） |
| 重試 | 不重試；傳輸逾時也不重送，先確認原請求結果 |

| 報價 | 回傳 | 依據 |
|---|---|---|
| 當前報價（2026-10-20） | credits 1／credits_exact 0.12 | 不扣款的報價預檢，設定與 prompt 和首試完全相同；工具說明：「return the cost in credits for this generation without submitting any job」；預檢前後交易明細相同，沒有新增。 |
| 上一輪報價（2026-10-13） | credits 1／credits_exact 0.12 | 同設定的報價預檢（R4 紀錄） |

**歷史紀錄（另列，不拿來估算本次）：**

| 紀錄 | 數值 | 說明 |
|---|---|---|
| Soul V2 交易明細（2026-09） | 每筆 −0.12 | Soul 訓練報告：驗證圖 114 張約 13.7 credits，交易明細為重複的 Soul V2 −0.12。 |
| 帳號交易明細（2026-10-19） | Soul V2 −0.12 後 32 秒 +0.12 退款 | 非本案、歸屬不明；說明 Soul V2 目前在交易明細仍以 0.12 記帳，且失敗可能退款。 |
| Iris 生成筆記（2026-08-05） | 「全批 14 張約 8 credits」 | 7 位角色各 2 張的約數，沒有寫怎麼算；與 0.12 不一致，只列為歷史，不拿來估算。 |

**計價單位：**

- 報價以「每次請求」回傳；本案每次只送 count 1，所以一個請求就是一張。
- credits 1 是整數顯示值、credits_exact 0.12 是精確值；交易明細的 Soul V2 列以 0.12 記帳（歷史紀錄）。這些都不等於本次實扣，實扣以送出後的交易明細為準。
- 不把 0.12 推測為實扣；也不以餘額前後差額推算。

## 5. 失敗扣款規則與建議上限

- 失敗可能退款：2026-10-19 帳號交易明細有 Soul V2 −0.12 後同額退款（非本案）；其他模型也常見扣款後退款。
- 失敗也可能扣款不退：Soul 訓練協定記錄過「呼叫失敗但仍計費」的 Soul V2 −0.12（Vicky Lin 模式）。
- 傳輸逾時時結果未知：工具說明要求不要自動重送，先確認原請求結果。
- 規則：任何扣款（含失敗未退）都算進上限；失敗就停下回報，不重試。

**建議：單次核准上限 1 credit（1 個請求、count 1、不重試）。** 當前報價 0.12；整數顯示值是 1。上限 1 credit 涵蓋顯示值計費的情況，但只允許一次請求；預期實扣 0.12。

停止條件：

- 交易明細出現高於 0.12 的 Soul V2 扣款
- 同一視窗出現兩筆以上 Soul V2 扣款、無法分辨哪一筆是本次
- 出現任何無法解釋的扣款
- 請求失敗、逾時或結果不明（無論是否扣款）

任一停止條件成立：不再送出，照實回報交易明細原始列與判斷。

## 6. 交易核對（多人共用帳號）

1. 送出前：查交易明細，記下最新一列的時間，以及這一頁內所有 Soul V2 列。
2. 送出：只呼叫一次；記下回傳的工作 ID（只寫進送審紀錄，不放公開頁）與回傳時間；若回應含費用欄位一併記錄。
3. 等待：輪詢到終態（完成、失敗或審核拒絕）；不重送。
4. 送出後：查交易明細，直到涵蓋送出前的最新一列；終態後 15 分鐘再查一次，看有沒有遲到的扣款或退款。
5. 關聯判準（全部符合才算「已關聯」）：(1) 視窗內（送出前最新一列之後，到終態後 15 分鐘）新增的 Soul V2 列恰好一筆扣款，另可有一筆同額退款；(2) 帳號生成紀錄（唯讀，含進行中）在同一視窗只有本次這一個 soul_2 任務；(3) 金額與報價一致，或差異已說明。
6. 任一不符（0 筆、2 筆以上、或視窗內有其他 soul_2 任務）：記為「無法唯一關聯」，只回報視窗內 Soul V2 列的原始資料；不以時間相近或餘額差額歸屬，停止並回報。

限制：

- 交易明細每列只有模型名稱、金額、動作（扣款／退款）與時間，沒有工作 ID，所以無法直接用 ID 對上；只能用「模型名稱＋時間視窗＋生成紀錄一對一」排除。
- 第 (2) 項要讀取帳號的生成紀錄（唯讀，但會看到帳號上其他人的作品），需要主管同意生成時使用。
- 2026-10-18 02:15 到 10-20 08:57（UTC）共 120 筆交易裡，Soul V2 只有 2 筆（10-19 一扣一退）；視窗內撞到他人 Soul V2 的機會低，但不能排除。

## 7. 剩餘阻礙

| 阻礙 | 說明 | 誰決定 |
|---|---|---|
| 生成與費用授權 | 需要費用核准（建議上限 1 credit）與主管另發的 M-4 生成指令。 | 主管／Penny（費用） |
| 交易關聯判準 | 交易明細沒有工作 ID；請主管接受「交易核對」一節的排除法判準，並同意生成時唯讀查看帳號生成紀錄。不接受時，實扣只能記為「視窗內的 Soul V2 列」，不能歸屬。 | 主管 |
| Soul 沒有正式 6 張驗證 | 依指示不重訓、不補生；請主管接受以既有生產紀錄＋首張驗收判定。 | 主管 |

**已不是阻礙：** V-Iris 造型（已接受）、已接受 prompt（不變）、三項檢查表差異（主管已接受）、模型參數與 Soul 狀態（已核對；生成當下再核一次）、報價（已取得 0.12）。

**首張驗收要特別看的風險：** 身材還原不穩（胸型可能小於 D）、逆光臉暗、碰頭髮的手指、戶外公園背景可能出現路人。

## 8. 驗證

| 項目 | 結果 | 檔案 |
|---|---|---|
| M-4 R1 定向驗證（資料：主管結論、v8 狀態、24 套不變、Penny 未看過、過期前提、檢查表差異、核查內容、Soul ID 未寫入；頁面桌機＋390px：M-3 完成、無必填欄位、H-Luna 主管覆核通過、首試前核查區、歷史保存、複製、無溢出、重新整理後 localStorage 不變、素材頁、無 JS 錯誤） | 線上 57/57（本機 57/57） | /home/user/Virtual_KOL_Studio/review/calendar/m4_r1/live_m4r1_tests.tsv |
| 部署前後（測試瀏覽器在 R6 頁填 v6、經過 R7 頁，再開 M-4 R1 頁） | 5/5 | /home/user/Virtual_KOL_Studio/review/calendar/m4_r1/live_upgrade_r7_to_m4r1.tsv |
| 線上檔案 sha256 與本機比對 | 666 檔不符 0；四個 HTML 頁版本 706618f | /home/user/Virtual_KOL_Studio/review/calendar/m4_r1/live_bytes_check.txt |
| 網站建置器 --check | PASS 654 檔；圖片與素材清單不變 | — |
| 企劃文件產生器 --check | PASS（CAL_18、CAL_20 更新；CAL_19 位元組不變） | — |
| kol-catalog 首頁 | 與存檔相同（44801 bytes） | /home/user/Virtual_KOL_Studio/review/calendar/m4_r1/live_bytes_check.txt |
| 唯讀查詢與報價預檢 | 預檢前後交易明細相同、沒有新增；沒有建立生成任務 | /home/user/Virtual_KOL_Studio/review/calendar/m4_r1/readonly_queries_2026-10-20.json |

過程中的修正（照實記錄）：頁面新變數名稱與既有函式撞名，第一次本機測試頁面沒有顯示，改名後通過；「Penny 看過」的檢查原本會誤抓主管原文裡的否定句「不虛構Penny已看過…」，改為排除這個否定句。

## 9. 檔案（完整路徑）

- `/home/user/Virtual_KOL_Studio/docs/calendar/data/cal_m4_supervisor_r1.json`
- `/home/user/Virtual_KOL_Studio/docs/calendar/data/cal_m3_shoot_plan.json`（m4r1.changes 有全部舊／新文字；m4_prep.r1 是首試前核查）
- `/home/user/Virtual_KOL_Studio/docs/calendar/CAL_20_M4_IRIS_FIRST_TEST_PREP.md`
- `/home/user/Virtual_KOL_Studio/docs/calendar/CAL_18_M3_SHOOT_PLAN.md`
- `/home/user/Virtual_KOL_Studio/docs/calendar/decision_site/public/shoot.js`、`shoot.html`、`data.js`
- `/home/user/Virtual_KOL_Studio/docs/calendar/tools/build_cal_decision_site.py`、`build_cal_m3_plan_doc.py`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/copy_example_progress.txt`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/desktop_card_H-luna_verified.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/desktop_iris_first_check.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/desktop_m3_complete_decisions.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/desktop_progress_copy.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/desktop_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/live_bytes_check.txt`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/live_m4r1_tests.tsv`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/live_upgrade_r7_to_m4r1.tsv`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/local_m4r1_tests.tsv`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/mobile390_card_H-luna_verified.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/mobile390_iris_first_check.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/mobile390_m3_complete_decisions.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/mobile390_progress_copy.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/mobile390_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m4_r1/readonly_queries_2026-10-20.json`

## 10. 操作紀錄

| # | 動作 | 性質 |
|---|---|---|
| 1 | 定向讀 Iris 的 profile、生成筆記、Soul 訓練報告與總表、LEDGER／REVIEW 的基準紀錄；本機既有成圖只讀尺寸，並做一張縮小接觸表目視（只存在本機暫存） | 唯讀 |
| 2 | Higgsfield 唯讀查詢 7 次：模型參數、Soul 狀態、交易明細 3 次、帳號餘額、不扣款的報價預檢（工具說明保證不送出工作；前後交易明細相同） | 唯讀 |
| 3 | 本機：主管結論紀錄；企劃 v8；CAL_18、CAL_20；頁面；建置與 --check；定向驗證與截圖 | 本機 |
| 4 | commit 706618f、push；Railway 只把 cal2027-decision 固定到 706618f（215e1521-34c3-4991-a36b-446fe6d6141e） | 其他 service 未動 |
| 5 | 部署後驗證、定向驗證、檔案比對、截圖、讀 kol-catalog 首頁 | 唯讀 |
| 6 | 寫本送審紀錄並 commit、push | — |

**本輪數字：** 生成 0、生成任務 0、扣 credits 0、重試 0、訓練 0、上傳 0、取回新原圖 0；唯讀查詢 7（含不扣款的報價預檢 1）。
