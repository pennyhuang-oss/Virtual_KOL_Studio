TASK-CAL-001／M-4／R6｜全套寫真企劃重審｜送審報告

# CAL_18 — M-3 24 套雙款寫真企劃、攝影設計與印刷構圖（shoot-plan-v12）

> 資料檔：`data/cal_m3_shoot_plan.json`（shoot-plan-v12，M-4 R6，2026-10-21）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。
> **M-3 企劃沒有生成任何圖片；M-4 R2 生成 V-Iris 首試 1 張，M-4 R4 Penny 接受；M-4 R5 生成第一批 5 張，M-4 R6 Penny 全數退回（想修改 5、接受 0），24 套企劃重審中（提案待主管覆核）；沒有上傳、訓練、修圖，也沒有改 canon 或 Soul ID。** 生成數 6、credits 0.72、訓練數 0（M-3 企劃階段生成 0；M-4 R2 依授權生成 V-Iris 首試 1 張（實扣 0.12，依時窗及唯一任務推定）。M-4 R4：Penny 接受這張、直接採用（已生成 1、已接受 1、其餘 23 套待製作）；下一批 5 位只做準備，生成 0、扣款 0。 M-4 R5：第一批 5 位各生成 1 張（5 次請求、實扣 0.60，依時窗及唯一任務推定），待 Penny 看圖；累計生成 6、credits 0.72。 M-4 R6：第一批 5 張 Penny 全數退回（不是品質驗收通過）；本輪生成 0、扣款 0。）
> R4 狀態（歷史）：8 套已接受、16 套修訂待 Penny 定案；兩本月份人選排序已確認；版面（照片框）尚未定案；生成與費用都未授權。R2 的 Owner 決策逐字紀錄見 `CAL_19_M3_R2_OWNER_DECISION.md`。
> R5：只修資料一致性與措辭（見 0b），沒有攝影方向變更。
> R6 狀態（歷史）：22 套已接受；H-jia-seo、H-luna-tanaka 兩套新推薦待 Penny 定案；兩本月份與工作照片框已接受（工作版型，不是廠商規格、印刷安全或成品核准）。
> R7 狀態（歷史）：23 套已接受（加上 H-jia-seo）；H-luna-tanaka 依 Penny 指定只把手部改為雙手輕捧日式小香袋，當時記為「依owner指定修訂，待主管核對落實」。
> M-4 R1 狀態（歷史）：主管結論 M-3／R7 PASS，M-3 完成——23 套 owner 接受＋H-Luna 依 owner 指示修訂、主管覆核通過（Penny 沒有看過修訂後的版本）；不再要求 owner 填企劃問卷。
> M-4 R2 狀態（歷史）：已生成 1 張，待主管覆核；照片只在私有 repo 送審，不放公開頁。部分通過：身分、服裝、姿態與手指、表情、構圖、套框與有效 ppi 都符合；一項不符合——左側草地上出現白色反光板（prompt 寫在畫面外）；兩項待判斷——胸型目視比人設保守、臉部皮膚偏光滑；遠處有失焦人形的小落差。依指示不重送、不再生成，交主管覆核；反光板與身材屬設定落差，由 Penny 判斷。
> M-4 R4 狀態（歷史）：Penny 接受，照片直接採用（取代主管 M-4 R3「反光板及支架必修」的判定；反光板保留）；首試紀錄見 `CAL_20_M4_IRIS_FIRST_TEST_PREP.md`。
> M-4 R5 狀態（歷史）：第一批 5 位各生成 1 張並上線審圖；生成準備見 `CAL_21_M4_BATCH1_PREP.md`，結果與扣款見 `CAL_22_M4_BATCH1_RESULTS.md`。
> **M-4 R6 狀態：M-4 R6：Penny 已全數退回（想修改 5、接受 0；逐張「Penny 退回／待重規劃」）。M-4 R5 是「生成與部署完成；第一批照片 Owner 全數退回」，不是品質驗收通過。重審與重建提案見 `CAL_23_M4_R6_REPLAN.md`（待主管覆核）。 已生成 6 張、已接受 1 張、退回 5 張、其餘 23 套待製作。以下 24 套是採用重審提案前的原文。**

## 0. 版本

| 項目 | 內容 |
|---|---|
| 名單 | roster-v1（docs/calendar/data/cal_m1_owner_roster.json）；不換人 |
| 上一版企劃 | shoot-plan-v11（commit `4bc31d35ca2981c3d48583ddc9ebbd770f6176af`） |
| 這一版 | 依 M-4 R6（Penny 決定，主管轉交）：第一批 5 張全部「想修改」、接受 0，逐張記為「Penny 退回／待重規劃」；V-Iris 已接受保留。M-4 R5 記為「生成與部署完成；第一批照片 Owner 全數退回」，不是品質驗收通過。24 套企劃全面重審（執行者提案見 data/cal_m4_r6_replan.json 與 CAL_23，待主管覆核）；採用前 24 套原文不改。進度：已生成 6、已接受 1、退回 5、其餘 23 套待製作。企劃版本升為 shoot-plan-v12。 |
| M-4 R2（歷史） | 依 M-4 R2 指令：同步主管對 R1 的覆核（歸屬用語、刪除顯示值推論、預算不是平台上限），保存 Penny 的限定授權，並記錄 V-Iris 單張首試結果（部分通過，待主管覆核；照片不放公開頁）。24 套拍攝內容與 prompt 不變；企劃版本升為 shoot-plan-v9。（基準 commit `706618f66707087e9a27dbb94f9ee3b9d256fd6f`） |
| M-4 R1（歷史） | 依主管 M-4 R1 結論：M-3 完成（23 套 owner 接受＋H-Luna 依 owner 指示修訂、主管覆核通過；Penny 沒有看過修訂後的版本）。修正首試準備的過期前提（造型已接受，生成與費用未授權）；主管接受三項檢查表差異；加上 V-Iris 首試前核查結果。24 套拍攝內容與 prompt 不變；企劃版本升為 shoot-plan-v8。（基準 commit `f694e1b0a070942cad5ac247dfd3af7c17efb5b4`） |
| R7（歷史） | 依 R7 owner 決策：H-jia-seo 接受（共 23 套已接受，拍攝內容與 prompt 不變）；H-luna-tanaka 依 Penny 指定只把手部改為雙手輕捧日式小香袋，記為「依owner指定修訂，待主管核對落實」；月份與工作照片框維持；另整理 V-Iris 首試準備（不生成）。企劃版本升為 shoot-plan-v7；本輪沒有必填決策，v1–v6 的回饋保留為歷史。（基準 commit `c47b91192ca1c76abfec9a93f1e183f7c3fd11f9`） |
| R6（歷史） | 依 R6 owner 決策：22 套已接受（拍攝內容與 prompt 不變）、H-jia-seo 換穿搭、H-luna-tanaka 改為日式宅邸庭院的和服外景；兩本月份與工作照片框已接受。企劃版本升為 shoot-plan-v6，回饋另存 v6；v1–v5 的回饋保留為歷史。（基準 commit `9434b839f589c19832a88e36975fbb31527b7284`） |
| R5 資料修訂 | R5 只修資料一致性與措辭：月份理由與過時的交叉引用改成目前企劃；撤回「橫直服裝差太多就拿第一張當參考圖」的策略；依主管核可替已接受的 V-iris-chen、H-coco-wu、V-coco-wu 補英文妝感句；印刷結論分成已知尺寸、比例計算、規劃目標、生成後待驗證，並改成條件句。24 套方向、月份人選、8 套已接受／16 套待決都不變；企劃版本仍是 shoot-plan-v5，Penny 的回饋延續、不需重填。（基準 commit `4f1591790d0e04cd58b93d95be470c2ff602e63b`） |
| 素材頁版本 | `b8108eb648a46a57e3bb4dc2158cf878c23d7963` |
| 桌曆基準 | `4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45` |

**參考照片：** 參考照片都是既有照片，只按標示的用途參考（表情／場景／服裝材質／身分），不是新企劃的成品，也不會照抄；身材一律以設定數字為準。既有照片也不是新構圖的成品。

## 0a. M-4 R2 修改（差異）

依 M-4 R2 指令：同步主管對 R1 的覆核（歸屬用語、刪除顯示值推論、預算不是平台上限），保存 Penny 的限定授權，並記錄 V-Iris 單張首試結果（部分通過，待主管覆核；照片不放公開頁）。24 套拍攝內容與 prompt 不變；企劃版本升為 shoot-plan-v9。

| 類別 | 位置 | 舊 | 新 |
|---|---|---|---|
| R1 覆核同步 | m4_prep.r1.cap.why | 當前報價 0.12；整數顯示值是 1。上限 1 credit 涵蓋顯示值計費的情況，但只允許一次請求；預期實扣 0.12。 | 1 credit 是 Penny 同意的本次核准預算（V-Iris 1 張）。工具沒有強制費用上限，不能宣稱平台保證不超扣；精確報價（0.12）與實扣分列，實扣以交易明細為準。 |
| R1 覆核同步 | m4_prep.r1.recon[歸屬判準] | 關聯判準（全部符合才算「已關聯」）：(1) 視窗內（送出前最新一列之後，到終態後 15 分鐘）新增的 Soul V2 列恰好一筆扣款，另可有一筆同額退款；(2) 帳號生成紀錄（唯讀，含進行中）在同一視窗只有本次這一個 soul_2 任務；(3) 金額與報價一致，或差異已說明。 | 歸屬判準（全部符合才標「依時窗及唯一任務推定」；交易明細沒有工作 ID，所以不標成直接對帳確認）：(1) 視窗內（送出前最新一列之後，到終態後 15 分鐘）新增的 Soul V2 列恰好一筆扣款，另可有一筆同額退款；(2) 帳號生成紀錄（唯讀，含進行中）在同一視窗只有本次這一個 soul_2 任務；(3) 金額與報價一致，或差異已說明。 |
| R1 覆核同步 | m4_prep.r1.blockers | 3 項剩餘阻礙 | 3 項都已解除（M-4 R2） |
| R1 覆核同步 | m4_prep.tbc[生成與費用授權] | 待決定 | 已授權（M-4 R2，限 1 張） |
| 首試結果 | m4_prep.r2 | （無） | 設定、報價、終態、像素、套框與 ppi、逐項驗收（部分通過）、扣款 0.12 與歸屬層級（依時窗及唯一任務推定） |
| 首試結果 | execution.cost.iris_first.status_m4r2 | （無） | M-4 R2：依授權生成 V-Iris 首試 1 張（精確報價 0.12、實扣 0.12，依時窗及唯一任務推定）；部分通過，待主管覆核；沒有重送。 |
| 計數 | counts | {"generated": 0, "credits": 0, "trainings": 0} | {"generated": 1, "credits": 0.12, "trainings": 0} |
| 計數 | meta.status | 僅規劃：沒有生成任何圖片（含測試圖、示意圖），沒有花 credits，沒有上傳，沒有訓練，沒有改 canon 或 Soul ID | M-3 企劃沒有生成任何圖片；M-4 R2 依授權生成 V-Iris 首試 1 張（照片只在私有 repo 送審，不放公開頁）；沒有上傳、訓練，也沒有改 canon 或 Soul ID |

## 0b. M-4 R1 修改（差異，歷史）

依主管 M-4 R1 結論：M-3 完成（23 套 owner 接受＋H-Luna 依 owner 指示修訂、主管覆核通過；Penny 沒有看過修訂後的版本）。修正首試準備的過期前提（造型已接受，生成與費用未授權）；主管接受三項檢查表差異；加上 V-Iris 首試前核查結果。24 套拍攝內容與 prompt 不變；企劃版本升為 shoot-plan-v8。

| 類別 | 位置 | 舊 | 新 |
|---|---|---|---|
| M-3 完成（主管結論） | sets[H-luna-tanaka].status | owner_revised（依owner指定修訂，待主管核對落實） | supervisor_verified（依owner指示修訂，主管覆核通過；Penny 未看過修訂後版本） |
| M-3 完成（主管結論） | photo.summary | H-Luna 是「依owner指定修訂，待主管核對落實」，Penny 還沒有看過修訂後的版本。 | R1 主管結論：M-3 完成；H-Luna 依 owner 指示修訂、主管覆核通過（Penny 沒有看過修訂後的版本）。 |
| 過期前提修正 | execution.cost.iris_first.plan[前提] | 需要 Penny 核定這套造型與費用，再由主管另發 M-4 指令；本輪什麼都不送出。 | V-Iris 造型已接受（R4 owner 紀錄；M-3 已完成），不再等待造型核准。生成與費用尚未授權：需要費用核准與主管另發的 M-4 生成指令；在那之前什麼都不送出。 |
| 過期前提修正 | m4_prep.workflow[0. 前提] | Penny 核定這套造型與費用，再由主管另發 M-4 指令；沒有這兩件事之前，下面所有步驟都不做。 | V-Iris 造型已接受（R4 owner 紀錄；M-3 已完成），不再等待造型核准。生成與費用尚未授權：需要費用核准與主管另發的 M-4 生成指令；在那之前什麼都不送出。 |
| 首試準備（工作流） | m4_prep.workflow[1／3／6] | 核對參數與對帳的一般說明 | 指向 M-4 R1 的核查結果與關聯判準 |
| 檢查表差異（主管接受） | m4_prep.lint[§七 機位寫離地公分數] | 與稽核表不同（已接受版本照舊） | 與稽核表不同（主管 M-4 R1 接受） |
| 檢查表差異（主管接受） | m4_prep.lint[§七 道具互動或側身回望，不正面直視鏡頭] | 與稽核表不同（依 Penny 指定） | 與稽核表不同（主管 M-4 R1 接受） |
| 檢查表差異（主管接受） | m4_prep.lint[§七 主光打在臉上、背景光與臉部光一致] | 與稽核表不同（企劃選擇，列驗收） | 與稽核表不同（主管 M-4 R1 接受） |
| 待確認事項 | m4_prep.tbc | 8 項（R7 狀態） | 8 項逐項標 M-4 R1 狀態：已核對 5、已提出建議 1、主管已接受 1、待決定 1 |
| 首試前核查 | m4_prep.r1 | （無） | Soul 證據、當前參數、單次請求設定、報價、計價、失敗扣款、建議上限 1 credit、交易核對方法、剩餘阻礙 |

## 0c. R7 修改（差異，歷史）

依 R7 owner 決策：H-jia-seo 接受（共 23 套已接受，拍攝內容與 prompt 不變）；H-luna-tanaka 依 Penny 指定只把手部改為雙手輕捧日式小香袋，記為「依owner指定修訂，待主管核對落實」；月份與工作照片框維持；另整理 V-Iris 首試準備（不生成）。企劃版本升為 shoot-plan-v7；本輪沒有必填決策，v1–v6 的回饋保留為歷史。

| 類別 | 位置 | 舊 | 新 |
|---|---|---|---|
| R7 依 owner 指定修訂 | sets[H-luna-tanaka] | 一手輕扶腰帶側邊、一手自然放下 | 雙手在腰帶下方輕捧小巧的日式布製香袋（手部、姿態、道具、入鏡、攝影目的、英文 prompt 三段、風險與參考備註） |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].hands | 一手輕扶腰帶側邊，另一手自然放下；袖子不遮臉。 | 雙手在腰帶下方、下腹前自然輕捧一個小巧的日式布製香袋；肩膀放鬆、手肘自然微彎，手腕不交叉，手指自然貼著香袋；袖子自然垂落，不遮臉，也不完全蓋住雙手與香袋，腰帶清楚可見。 |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].pose | 站在緣側旁的石板路上，身體斜側、臉轉向鏡頭。 | 站在緣側旁的石板路上，身體斜側、臉轉向鏡頭，雙手在腰帶下方輕捧小香袋。 |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].theme | 秋日午後當代日式宅邸的庭院，藕粉秋草紋和服配深梅色腰帶，站在緣側旁的石板路上，身體斜側、轉頭對鏡頭甜美淺笑。 | 秋日午後當代日式宅邸的庭院，藕粉秋草紋和服配深梅色腰帶，雙手在腰帶下方輕捧一個小巧的日式香袋，站在緣側旁的石板路上，身體斜側、轉頭對鏡頭甜美淺笑。 |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].why | 依 Penny 指示：她是「住在美麗白日夢裡的人」，秋天的日式庭院、看得到和室的建築與正式和服，讓 Luna 的日式氣質最完整；人物站在室外，建築與紅葉只是陪襯。 | 依 Penny 指示：她是「住在美麗白日夢裡的人」，秋天的日式庭院、看得到和室的建築與正式和服，讓 Luna 的日式氣質最完整；人物站在室外，建築與紅葉只是陪襯。R7 依 Penny 指定：雙手輕捧一個日式小香袋，增加典雅氣質。 |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].prompt | A 20-year-old adult Japanese woman with her natural fair skin tone, large round dark-brown eyes and soft natural makeup with a rosy lip, black fine straight hair in a centre-parted, chin-length bob. Petite figure with a noticeably full chest and a slim waist, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup. She wears a properly dressed silk kimono in a soft, muted dusty lotus-pink with a fine, small autumn-grass pattern, the left side wrapped over the right with a neat white under-collar, a deep plum Nagoya obi tied in a neat drum knot with a pale-gold obijime cord and a cream obiage, white tabi socks and low zori sandals, and a small pearl hair pin above one ear. Setting: the stone-paved garden path of a contemporary Japanese residence on an autumn afternoon, a wide wooden engawa veranda beside her and open sliding shoji doors revealing a clean, new tatami room with crisp light-wood details, raked white gravel and a few neatly pruned pines, one maple with red leaves at the edge of the frame and a few red leaves on the stones, everything new and well kept, nobody else in the garden. One hand rests lightly at the side of her obi and the other hangs naturally, her sleeves falling clear of her face; she gives a sweet, gentle smile. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to her zori sandals, the dusty-pink kimono with its small autumn-grass pattern, the deep plum obi and its cord, the white tabi socks and zori, one hand resting at the side of the obi and the other hanging naturally, her sleeves clear of her face. Body: standing on the stone path with her weight on her back foot and her front foot slightly forward, her body turned about 30 degrees toward camera-left, her shoulders relaxed and her back straight, the line of the obi clear. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 4.6 metres, camera at her hip height, level, natural perspective without distortion; she fills about 84% of the frame height. Composition: she stands right of centre on the stone path, the wooden veranda and the open shoji with the clean tatami room behind her on the left, a red maple at the upper-right edge, the building kept as a backdrop. Emphasis: the full standing figure shows the whole kimono, where the obi sits and her proportions, the oblique stance adding shape while her face turns to the camera with a sweet smile. Lighting: soft, slanting autumn afternoon sun from front-left, a large white reflector just out of frame on the right keeping her face soft and clear; muted lotus pink, plum, warm wood and a few maple reds against white gravel, with a gentle film-like finish. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph. | A 20-year-old adult Japanese woman with her natural fair skin tone, large round dark-brown eyes and soft natural makeup with a rosy lip, black fine straight hair in a centre-parted, chin-length bob. Petite figure with a noticeably full chest and a slim waist, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup. She wears a properly dressed silk kimono in a soft, muted dusty lotus-pink with a fine, small autumn-grass pattern, the left side wrapped over the right with a neat white under-collar, a deep plum Nagoya obi tied in a neat drum knot with a pale-gold obijime cord and a cream obiage, white tabi socks and low zori sandals, and a small pearl hair pin above one ear. Setting: the stone-paved garden path of a contemporary Japanese residence on an autumn afternoon, a wide wooden engawa veranda beside her and open sliding shoji doors revealing a clean, new tatami room with crisp light-wood details, raked white gravel and a few neatly pruned pines, one maple with red leaves at the edge of the frame and a few red leaves on the stones, everything new and well kept, nobody else in the garden. Both hands rest together just below her obi in front of her lower abdomen, lightly holding a small, palm-sized Japanese fabric sachet in soft cream with a fine pale-gold woven texture and a short drawstring cord, plain and without any logos; her shoulders are relaxed, her elbows softly bent and her wrists uncrossed, her fingers resting naturally on the sachet, her sleeves falling naturally; she gives a sweet, gentle smile. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to her zori sandals, the dusty-pink kimono with its small autumn-grass pattern, the deep plum obi and its cord, the white tabi socks and zori, both hands just below the obi holding the small sachet, the obi left clear above them, her sleeves clear of her face, her hands and the sachet. Body: standing on the stone path with her weight on her back foot and her front foot slightly forward, her body turned about 30 degrees toward camera-left, her shoulders relaxed and her back straight, the line of the obi clear. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 4.6 metres, camera at her hip height, level, natural perspective without distortion; she fills about 84% of the frame height. Composition: she stands right of centre on the stone path, the wooden veranda and the open shoji with the clean tatami room behind her on the left, a red maple at the upper-right edge, the building kept as a backdrop. Emphasis: the full standing figure shows the whole kimono, where the obi sits and her proportions, both hands holding the small sachet below the obi for a graceful, elegant air, the oblique stance adding shape while her face turns to the camera with a sweet smile. Lighting: soft, slanting autumn afternoon sun from front-left, a large white reflector just out of frame on the right keeping her face soft and clear; muted lotus pink, plum, warm wood and a few maple reds against white gravel, with a gentle film-like finish. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph. |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].outfit.道具 | （無） | 小巧的日式布製香袋（掌心大小；低飽和奶油色帶淡金細緻織紋、短束口繩；不是手提包，沒有品牌、文字或誇張吊飾） |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].cam.bounds | {"zh": "完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到草履完整；藕粉秋草紋和服、深梅色腰帶與帶締、白足袋與草履；輕扶腰帶側邊的手與自然放下的手，袖子不遮臉", "en": "from a little above her head to just below her feet, both feet whole, showing her whole figure from head to her zori sandals, the dusty-pink kimono with its small autumn-grass pattern, the deep plum obi and its cord, the white tabi socks and zori, one hand resting at the side of the obi and the other hanging naturally, her sleeves clear of her face"} | {"zh": "完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到草履完整；藕粉秋草紋和服、深梅色腰帶與帶締、白足袋與草履；雙手在腰帶下方輕捧的小香袋，腰帶露出，袖子不遮臉、也不完全蓋住雙手與香袋", "en": "from a little above her head to just below her feet, both feet whole, showing her whole figure from head to her zori sandals, the dusty-pink kimono with its small autumn-grass pattern, the deep plum obi and its cord, the white tabi socks and zori, both hands just below the obi holding the small sachet, the obi left clear above them, her sleeves clear of her face, her hands and the sachet"} |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].cam.purpose | {"zh": "站姿全身呈現完整的和服、腰帶位置與身形比例；身體斜側帶出線條，臉轉向鏡頭的甜美淺笑", "en": "the full standing figure shows the whole kimono, where the obi sits and her proportions, the oblique stance adding shape while her face turns to the camera with a sweet smile"} | {"zh": "站姿全身呈現完整的和服、腰帶位置與身形比例；雙手在腰帶下方輕捧小香袋，典雅端莊；身體斜側帶出線條，臉轉向鏡頭的甜美淺笑", "en": "the full standing figure shows the whole kimono, where the obi sits and her proportions, both hands holding the small sachet below the obi for a graceful, elegant air, the oblique stance adding shape while her face turns to the camera with a sweet smile"} |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].cam.focus | "完整和服與腰帶、身形比例、甜美淺笑" | "完整和服與腰帶、雙手輕捧的小香袋、身形比例、甜美淺笑" |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].cam.change | "依 Penny 指示：由室內旅宿的緞面斜坐，改為站在當代日式宅邸庭院（緣側旁石板路）的和服寫真；背景透過敞開的拉門看得到整潔嶄新的和室；服裝改為低飽和藕粉秋草紋正式和服＋深梅色名古屋帶、白足袋與草履；姿勢改為站姿全身、約30度斜側、臉轉向鏡頭甜美淺笑，一手輕扶腰帶側邊、一手自然放下；相機改為臀部高度平視。" | "依 Penny 指定（R7）：只把手部由「一手輕扶腰帶側邊、一手自然放下」改為雙手在腰帶下方、下腹前輕捧一個小巧的日式布製香袋（低飽和奶油色帶淡金細緻織紋、短束口繩）；肩膀放鬆、手肘微彎、手腕不交叉，袖子不遮臉、不完全蓋住雙手與香袋，腰帶清楚可見。和服、庭院、月份、表情、身體方向與相機設定都不變。" |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].risks | 6 項 | 10 項（新增香袋、手指、遮擋、沒有香袋參考圖） |
| R7 依 owner 指定修訂 | sets[H-luna-tanaka].refs[luna-03].note | 既有照片是夏季祭典浴衣（淺藍棉質＋深藍腰帶），不是本套的秋季正式和服；只參考她穿日式服裝、繫腰帶時的整體比例與笑容；浴衣、顏色、蘋果與神社街景都不採用；沒有正式和服的參考圖；不作身材參考：既有照片的身材不符合設定（Penny） | 既有照片是夏季祭典浴衣（淺藍棉質＋深藍腰帶），不是本套的秋季正式和服；只參考她穿日式服裝、繫腰帶時的整體比例與笑容；浴衣、顏色、蘋果與神社街景都不採用；沒有正式和服的參考圖；也沒有香袋的參考圖（R7 香袋外觀只靠文字）；不作身材參考：既有照片的身材不符合設定（Penny） |
| R7 依 owner 指定修訂 | adjust[H-luna-tanaka].change | 依 Penny 指示：由室內旅宿的緞面斜坐，改為站在當代日式宅邸庭院（緣側旁石板路）的和服寫真；背景透過敞開的拉門看得到整潔嶄新的和室；服裝改為低飽和藕粉秋草紋正式和服＋深梅色名古屋帶、白足袋與草履；姿勢改為站姿全身、約30度斜側、臉轉向鏡頭甜美淺笑，一手輕扶腰帶側邊、一手自然放下；相機改為臀部高度平視。 | 依 Penny 指定（R7）：只把手部由「一手輕扶腰帶側邊、一手自然放下」改為雙手在腰帶下方、下腹前輕捧一個小巧的日式布製香袋（低飽和奶油色帶淡金細緻織紋、短束口繩）；肩膀放鬆、手肘微彎、手腕不交叉，袖子不遮臉、不完全蓋住雙手與香袋，腰帶清楚可見。和服、庭院、月份、表情、身體方向與相機設定都不變。 |
| 攝影總覽 | photo.summary／photo.checks | R6 文字 | R7 說明與檢查 |
| 印刷文字 | printing.accepted_impact.summary | 依已接受的工作照片框與規劃構圖，22 套已接受暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。H-somi-oh、H-coco-wu、H-rainie-hsu 是橫式膝上：套框後下緣理論上會往上移（依規劃構圖估算約 2–3 cm），若實圖接近膝蓋，4 mm 改由頭頂留白多裁——這是後製裁切位置，不改服裝、場景、表情或 prompt，不列待確認。 | 依已接受的工作照片框與規劃構圖，23 套已接受暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。H-somi-oh、H-coco-wu、H-rainie-hsu 是橫式膝上：套框後下緣理論上會往上移（依規劃構圖估算約 2–3 cm），若實圖接近膝蓋，4 mm 改由頭頂留白多裁——這是後製裁切位置，不改服裝、場景、表情或 prompt，不列待確認。H-luna-tanaka（依 owner 指定修訂）只改雙手與香袋：畫面上下界、人物佔比與印刷判斷都與 R6 相同。 |
| 月份規則 | month_rules[0] | 月份人選排序已確認（R4 owner 紀錄，R6 維持），不再請 Penny 重新核准；服裝與場景配合既定月份。 | 月份人選排序已確認（R4 owner 紀錄，R6、R7 維持），不再請 Penny 重新核准；服裝與場景配合既定月份。 |
| 待決問題 | questions | ["H-jia-seo、H-luna-tanaka 兩套新推薦：各選「接受」或「想修改」，想修改的寫在備註。未回覆不算接受。（其他 22 套、兩本月份與工作照片框都已接受，不需再回覆。）"] | （清空：本輪沒有要 Penny 回覆的企劃決策） |
| V-Iris 首試準備 | m4_prep | （無） | 首試準備：企劃、身分、prompt、比例、工作流、待確認、驗收條件、送生成前檢查（只整理，未生成） |

狀態：1 套由「R6 待決」改為「已接受」（R7 owner 紀錄：H-jia-seo）；H-luna-tanaka 記為「依owner指定修訂，待主管核對落實」。

## 0d. R6 修改（差異，歷史）

依 R6 owner 決策：22 套已接受（拍攝內容與 prompt 不變）、H-jia-seo 換穿搭、H-luna-tanaka 改為日式宅邸庭院的和服外景；兩本月份與工作照片框已接受。企劃版本升為 shoot-plan-v6，回饋另存 v6；v1–v5 的回饋保留為歷史。

| 類別 | 位置 | 舊 | 新 |
|---|---|---|---|
| R6 新推薦 | sets[H-luna-tanaka] | 新穎整潔的當代日式旅宿房間，香檳色斜裁緞面細肩洋裝，在榻榻米上單手撐地慵懶斜坐、望向窗外的紅葉。｜席地坐姿全身｜約45度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側窗外的紅葉庭院｜坐姿時的胸口高度・平視 | 秋日午後當代日式宅邸的庭院，藕粉秋草紋和服配深梅色腰帶，站在緣側旁的石板路上，身體斜側、轉頭對鏡頭甜美淺笑。｜全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・平視 |
| R6 新推薦 | sets[H-jia-seo] | 初秋傍晚的湖畔木平台，黑色單肩貼身中長洋裝帶腰側鏤空與側開衩，側坐在臨水長椅上望向湖面。｜坐姿全身｜側面（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側的湖面與遠岸｜坐姿時的腰部高度・平視 | 初秋傍晚的湖畔木平台，深酒紅合身繞頸細針織短洋裝露肩與上背，側坐在臨水長椅上、雙腿交疊望向湖面。｜坐姿全身｜側面（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側的湖面與遠岸｜坐姿時的腰部高度・平視 |
| R6 比較文字（不是拍攝內容） | sets[V-jia-seo].vs_other | 橫式款是初秋湖畔、黑色單肩洋裝、側坐長椅、望向湖面；這款是溫室綠意、白色短上衣＋薄荷緞面高腰窄裙、斜側站姿看鏡頭。 | 橫式款是初秋湖畔、深酒紅細針織繞頸短洋裝、側坐長椅、望向湖面；這款是溫室綠意、白色短上衣＋薄荷緞面高腰窄裙、斜側站姿看鏡頭。 |
| R6 比較文字（不是拍攝內容） | sets[V-luna-tanaka].vs_other | 橫式款是室內當代日式旅宿、香檳色緞面、榻榻米上慵懶斜坐；這款是戶外庭院、綠色馬甲洋裝、站姿全身。 | 橫式款是秋天的當代日式宅邸庭院、藕粉秋草紋和服、約30度斜側站姿、臀部高度平視；這款是初夏的京都老町家後院、白色紫陽花、綠色馬甲洋裝、正面站姿全身、膝蓋高度輕仰。 |
| R6 比較文字（不是拍攝內容） | sets[H-rin-ayase].vs_other | 直式款是秋日港灣、墨綠仿麂皮裹身洋裝、倚著繫船柱；這款是室內套房夕陽、酒紅緞面、側躺。與 3 月 Miu（床上靠枕半倚）、10 月 Luna（榻榻米單手撐地斜坐）分開：Rin 是全身側躺在貴妃椅上。 | 直式款是秋日港灣、墨綠仿麂皮裹身洋裝、倚著繫船柱；這款是室內套房夕陽、酒紅緞面、側躺。與 3 月 Miu（床上靠枕半倚）分開：Rin 是全身側躺在貴妃椅上（10 月 Luna 在 R6 改為站姿和服）。 |
| R6 理由文字（不是拍攝內容） | sets[H-miu-shiraishi].cam.why | 從端坐改成床上靠枕的自然半倚，與 Rin 的貴妃椅側躺、Luna 的榻榻米斜坐都不同；小公寓空間有限，35mm 約 2.6 公尺、人物在中央不貼邊，避免廣角變形。 | 從端坐改成床上靠枕的自然半倚，與 Rin 的貴妃椅側躺不同（Luna 在 R6 改為站姿和服）；小公寓空間有限，35mm 約 2.6 公尺、人物在中央不貼邊，避免廣角變形。 |
| R6 理由文字（不是拍攝內容） | sets[V-luna-tanaka].cam.why | 嬌小的 Luna 用膝蓋高度輕仰拍全身，比例更修長；雙手在身後讓胸腰線完全不被遮住。與橫式款的席地斜側、看窗光完全不同。 | 嬌小的 Luna 用膝蓋高度輕仰拍全身，比例更修長；雙手在身後讓胸腰線完全不被遮住。與橫式款的秋季和服（約30度斜側、臀部高度平視）不同。 |
| 月份理由 | months[9月].why_h | 初秋傍晚的湖畔木平台 | 初秋傍晚湖畔的深酒紅細針織 |
| 月份理由 | months[10月].why_h | 秋日傍晚前的當代日式旅宿與窗外紅葉 | 秋日午後日式宅邸庭院的藕粉和服 |
| 攝影總覽（重新統計） | photo.counts | {"H": {"shot": {"大腿中段以上": 2, "膝上": 3, "全身": 2, "坐姿全身": 3, "席地坐姿全身": 1, "斜躺全身": 1}, "body": {"正面": 2, "約45度斜側": 3, "約30度斜側": 5, "側面斜躺": 1, "側面": 1}}, "V": {"shot": {"胸上": 1, "大腿中段以上": 2, "膝上": 3, "全身": 4, "坐姿全身": 1, "坐姿到水面": 1}, "body": {"正面": 5, "約30度斜側": 5, "約45度斜側": 2}}} | {"H": {"shot": {"大腿中段以上": 2, "膝上": 3, "全身": 3, "坐姿全身": 3, "斜躺全身": 1}, "body": {"正面": 2, "約30度斜側": 6, "側面斜躺": 1, "約45度斜側": 2, "側面": 1}}, "V": {"shot": {"胸上": 1, "大腿中段以上": 2, "膝上": 3, "全身": 4, "坐姿全身": 1, "坐姿到水面": 1}, "body": {"正面": 5, "約30度斜側": 5, "約45度斜側": 2}}} |
| 攝影總覽（重新統計） | photo.rhythm | {"H": "橫式款：大腿中段以上 2、膝上 3、全身 2、坐姿全身 3、席地坐姿全身 1、斜躺全身 1。戶外 8 套、室內 4 套；坐或躺的 5 套（Miu、Yerin、Jia、Luna、Rin）姿勢各不相同：床上靠枕半倚、球車座椅邊緣後靠、湖畔長椅側坐、榻榻米單手撐地斜坐、貴妃椅全身側躺。", "V": "直式款：胸上 1、大腿中段以上 2、膝上 3、全身 4、坐姿全身 1、坐姿到水面 1。戶外 10 套、室內 2 套；站姿置中只有 Tammy、Iris、Jia 三張，景別或角度各不相同。", "near": "近景：V-mia-huang 胸上；大腿中段以上 4 張（H-mia-huan | {"H": "橫式款：大腿中段以上 2、膝上 3、全身 3、坐姿全身 3、斜躺全身 1。戶外 9 套、室內 3 套；坐或躺的 4 套（Miu、Yerin、Jia、Rin）姿勢各不相同：床上靠枕半倚、球車座椅邊緣後靠、湖畔長椅側坐、貴妃椅全身側躺；Luna 在 R6 改為站姿全身的和服外景。", "V": "直式款：胸上 1、大腿中段以上 2、膝上 3、全身 4、坐姿全身 1、坐姿到水面 1。戶外 10 套、室內 2 套；站姿置中只有 Tammy、Iris、Jia 三張，景別或角度各不相同。", "near": "近景：V-mia-huang 胸上；大腿中段以上 4 張（H-mia-huang、 |
| 攝影總覽（重新統計） | photo.sequence | {"H": "1月 大腿中段以上（Yuna）→2月 斜躺全身（Rin）→3月 坐姿全身（Miu）→4月 全身（Tammy）→5月 坐姿全身（Yerin）→6月 膝上（Coco）→7月 大腿中段以上（Mia）→8月 全身（Iris）→9月 坐姿全身（Jia）→10月 席地坐姿全身（Luna）→11月 膝上（Somi）→12月 膝上（Rainie）", "V": "1月 大腿中段以上（Tammy）→2月 全身（Jia）→3月 胸上（Mia）→4月 坐姿全身（Miu）→5月 膝上（Rainie）→6月 全身（Luna）→7月 坐姿到水面（Coco）→8月 膝上（Yerin）→9月 大腿中段以上（Ir | {"H": "1月 大腿中段以上（Yuna）→2月 斜躺全身（Rin）→3月 坐姿全身（Miu）→4月 全身（Tammy）→5月 坐姿全身（Yerin）→6月 膝上（Coco）→7月 大腿中段以上（Mia）→8月 全身（Iris）→9月 坐姿全身（Jia）→10月 全身（Luna）→11月 膝上（Somi）→12月 膝上（Rainie）", "V": "1月 大腿中段以上（Tammy）→2月 全身（Jia）→3月 胸上（Mia）→4月 坐姿全身（Miu）→5月 膝上（Rainie）→6月 全身（Luna）→7月 坐姿到水面（Coco）→8月 膝上（Yerin）→9月 大腿中段以上（Iris）→ |
| 攝影總覽 | photo.summary／photo.checks | R4／R5 文字 | R6 說明與檢查 |
| 照片框已接受（標示） | printing.frames.H.name | 橫式大照片框（暫定） | 橫式工作照片框（R6 已接受） |
| 照片框已接受（標示） | printing.frames.V.name | 直式 3:4 照片框（暫定） | 直式 3:4 工作照片框（R6 已接受） |
| 照片框已接受（標示） | sets[*].print.frame／verdict | 暫定照片框；依暫定框與規劃構圖… | 工作照片框（R6 已接受）；依已接受的工作照片框與規劃構圖…（24 套只改標示，拍攝內容不變） |
| 照片框已接受（標示） | printing.assumed[暫定照片框] | 暫定照片框／版面還沒有 Penny 定案 | R6 Penny 接受為本案工作版型（H 192×104 mm 生成 16:9；V 120×160 mm 生成 3:4）；不是廠商規格、印刷安全或成品核准。照片框整個在安全區內、避開假設線圈區，所以照片本身不碰出血與裁切線。 |
| 照片框已接受（標示） | printing.unknown | 最後選哪個版面（橫式大照片框或半版、直式 3:4 或統一框）——待 Penny 定案 | （移除：照片框已在 R6 接受為工作版型；廠商實際套版與輸出仍待驗證，見其他未知項） |
| 照片框已接受（標示） | printing.iris_first.condition | 前提是直式採 3:4 照片框。若改用 R3 直式統一框（120×128），3:4 原圖高度要裁掉 20%（比例事實）；會不會切到髮頂、手或下緣，要看實圖與裁切位置，可能需要重新規劃留白——所以建議 M-4 首試前先確認直式照片框。 | 直式 3:4 工作照片框已在 R6 由 Penny 接受（120×160 mm），所以 V-Iris 依目前企劃不需要為照片框重排構圖；120×128 等其他框不再是現行方案。實際裁切仍要用實圖確認。 |
| 照片框已接受（標示） | printing.accepted_impact.summary | 依暫定框與規劃構圖，8 套已接受暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。H-coco-wu、H-rainie-hsu 是橫式膝上：套框後下緣理論上會往上移（依規劃構圖估算約 2–3 cm），若實圖接近膝蓋，4 mm 改由頭頂留白多裁——這是後製裁切位置，不改服裝、場景、表情或 prompt，不列待確認。 | 依已接受的工作照片框與規劃構圖，22 套已接受暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。H-somi-oh、H-coco-wu、H-rainie-hsu 是橫式膝上：套框後下緣理論上會往上移（依規劃構圖估算約 2–3 cm），若實圖接近膝蓋，4 mm 改由頭頂留白多裁——這是後製裁切位置，不改服裝、場景、表情或 prompt，不列待確認。 |
| 照片框已接受（標示） | composition.recommend[橫式款（H）] | 暫定照片框：橫式大照片框 192×104 mm（畫布 6,14–198,118）。生成用 16:9（原生尺寸未知）：比例上要裁掉高度 4 mm，規劃上下各約 2 mm。版面待 Penny 定案，見「印刷構圖」。 | 工作照片框（R6 已接受）：橫式大照片框 192×104 mm（畫布 6,14–198,118）。生成用 16:9（原生尺寸未知）：比例上要裁掉高度 4 mm，規劃上下各約 2 mm。這是本案工作版型，不是廠商規格或印刷安全；見「印刷構圖」。 |
| 照片框已接受（標示） | composition.recommend[直式款（V）] | 暫定照片框：直式 3:4 框 120×160 mm（畫布 12,16–132,176）。生成用 3:4：比例上不裁切；若輸出 1536×2048，約 325 ppi（比例計算，以實際輸出為準）。版面待 Penny 定案。 | 工作照片框（R6 已接受）：直式 3:4 框 120×160 mm（畫布 12,16–132,176）。生成用 3:4：比例上不裁切；若輸出 1536×2048，約 325 ppi（比例計算，以實際輸出為準）。這是本案工作版型，不是廠商規格或印刷安全。 |

狀態：14 套由「修訂」改為「已接受」（R6 owner 紀錄）。

## 0e. R5 資料修訂（差異，歷史）

**不變：** 24 套的服裝、場景、表情、姿態、攝影七欄位（已接受 3 套只多一句妝感）；兩本月份人選與排序；8 套已接受／16 套待決；shoot-plan-v5 回饋欄位與既有瀏覽器資料。

| 類別 | 位置 | 舊 | 新 |
|---|---|---|---|
| 月份理由 | months[1月].why_h | 冬日的明亮咖啡館，用清透的奶油黃開場 | 雪後清晨的白樺林，用雪白與霧玫瑰的冬日寫真開場 |
| 月份理由 | months[4月].why_h | 春天逛精品店的熱粉洋裝 | 春日花園露台的熱粉洋裝 |
| 月份理由 | months[4月].why_v | 暮春運河新綠 | 春日別墅木平台與開滿白花的果樹 |
| 月份理由 | months[8月].why_h | 夏末午後的紅磚騎樓 | 盛夏上午的岩岸海灣與向日葵黃 |
| 月份理由 | months[9月].why_h | 初秋美術館的冷調 | 初秋傍晚的湖畔木平台 |
| 月份理由 | months[10月].why_h | 秋日清晨的和室柔光 | 秋日傍晚前的當代日式旅宿與窗外紅葉 |
| 月份理由 | months[10月].why_v | 秋夜的金色酒吧 | 秋日午後的安靜港灣 |
| 交叉引用（已接受套數的比較文字，不是服裝場景表情） | sets[V-iris-chen].vs_other | 橫式款在紅磚騎樓、米杏針織套裝、側光；這款在河濱草地、白上衣＋牛仔迷你裙、逆光。 | 橫式款在夏日上午的岩岸海灣、向日葵黃馬甲短上衣＋低腰迷你裙、正面全身；這款在河濱草地、白上衣＋牛仔迷你裙、逆光。 |
| 交叉引用（已接受套數的比較文字，不是服裝場景表情） | sets[V-luna-tanaka].vs_other | 橫式款是室內和室、象牙白緞面、席地坐；這款是戶外庭院、綠色馬甲洋裝、站姿全身。 | 橫式款是室內當代日式旅宿、香檳色緞面、榻榻米上慵懶斜坐；這款是戶外庭院、綠色馬甲洋裝、站姿全身。 |
| 過時規則 | photo.rules[0] | Rin 的及地長禮服蓋住雙腳，她的坐姿全身下緣寫在禮服下襬下方。 | （刪除：R4 起 V-Rin 改為港灣膝上，不再有及地長禮服） |
| 撤回策略 | execution.model.multi_stage | 不規劃多階段（先生成再換臉、外擴、放大）。若首批發現橫直兩張服裝差太多，才考慮把第一張當唯一的參考圖餵第二張——這可能把構圖或身分一起帶過去，要另外測、另外批准。 | 不規劃多階段（先生成再換臉、外擴、放大）。H／V 本來就是兩套獨立的服裝與場景，兩張只需要共同維持人設身分（同一個 Soul 與身分句）與設定身材；不得為了讓服裝或環境相同而把一款的成品當參考圖餵給另一款。任何未來使用參考圖的方案都要另外提出、另外批准，本輪不執行。（R5 撤回先前「橫直服裝差太多就把第一張當參考圖餵第二張」的寫法。） |
| 已接受妝感中英同步（主管核可） | sets[V-iris-chen].prompt | （身分句後、She wears 前無妝感句） | Fresh, light everyday makeup with a natural lip colour. |
| 已接受妝感中英同步（主管核可） | sets[H-coco-wu].prompt | （身分句後、She wears 前無妝感句） | Sweet, light makeup with a pink lip. |
| 已接受妝感中英同步（主管核可） | sets[V-coco-wu].prompt | （身分句後、She wears 前無妝感句） | Sweet, light makeup. |
| 印刷措辭 | printing.fit.H.crop | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 比例計算：高度共裁 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm（各約 1.9%），實際分配依實圖 |
| 印刷措辭 | printing.fit.V.crop | 不裁切 | 比例計算：不裁切 |
| 印刷措辭 | printing.note | 以下分成「已知」「假設」「未知」。已知值來自廠商編輯器設定與商品頁（R1 查證，本輪只重讀既有證據、沒有重查網站）；假設值是本案為了規劃先定的數字，不是廠商規格；未知要等廠商回覆或實際打樣。只有構圖方框不代表印刷安全。 | 以下分成「已知」「假設」「未知」。已知值來自廠商編輯器設定與商品頁（R1 查證，本輪只重讀既有證據、沒有重查網站）；假設值是本案為了規劃先定的數字，不是廠商規格；未知要等廠商回覆或實際打樣。只有構圖方框不代表印刷安全。印刷數字再分成四類：已知尺寸、比例計算、prompt 規劃目標、生成後待驗證；表中的髮頂留白、腳下留白與「套框後約 x%」都是依規劃構圖推算的理論／規劃預估，不是實圖量測。 |
| 印刷措辭 | printing.categories | （無） | 新增四類說明 |
| 印刷措辭 | printing.rules | （無） | 限制：線圈／裝訂區 12 mm 是假設；16:9 實際輸出尺寸未知；300 ppi 是本案工作目標，不是已確認的廠商最低標準。 |
| 印刷措辭（並更正比例數字） | printing.compare[橫 A 半版] | 16:9 橫幅照片不適用（要裁掉約七成寬度），必須另拍直幅——不從 16:9 硬裁。 | 比例計算：16:9 照片要裁掉約 62% 寬度才放得進這個直幅框（原文誤寫「約七成」），所以不建議從 16:9 硬裁，要另外規劃直幅照片。 |
| 印刷措辭 | printing.compare[直式統一框] | 3:4 照片上下共要裁掉 32 mm（20%）：大腿中段以上會切到髮頂或腿、全身會切到腳——12 套直式款都要重排構圖。 | 比例計算：3:4 原圖放進 120×128 要裁掉高度 20%（160→128 mm）。裁在哪裡、會不會切到髮頂、腳或其他部位，要看實圖與裁切位置，不是必然；直式款可能要重新規劃上下留白。 |
| 印刷措辭（並更正數字） | printing.iris_first.answer | 不需要構圖微調：直式 3:4 照片放進暫定的 3:4 框不裁切，髮頂留白約 7%、下緣在大腿中段，人物置中、雙手都在框內；prompt 不改。 | 依暫定 3:4 框與規劃構圖，暫無須為印刷調整 V-Iris 的拍攝方向：3:4 照片放進 3:4 框在比例上不裁切；髮頂留白約 8%、下緣在大腿中段、雙手在框內是 prompt 規劃目標，不是實圖量測（R4 文字誤寫髮頂約 7%，依逐張表更正為約 8%）。 |
| 印刷措辭 | printing.iris_first.condition | 前提是直式採 3:4 照片框。若 Penny 最後選 R3 的直式統一框（120×128，約 0.94:1），3:4 照片上下要共裁 20%，這張的髮頂與下緣都會被切到，需要重排構圖；所以建議在 M-4 首試前先確認直式照片框。 | 前提是直式採 3:4 照片框。若改用 R3 直式統一框（120×128），3:4 原圖高度要裁掉 20%（比例事實）；會不會切到髮頂、手或下緣，要看實圖與裁切位置，可能需要重新規劃留白——所以建議 M-4 首試前先確認直式照片框。 |
| 印刷措辭 | printing.iris_first.verify | 首試出圖後要用實圖確認：實際像素（預期 1536×2048）、髮頂與雙手是否在框內、有效 ppi（120 mm 寬約 325 ppi）。 | 首試出圖後用實圖確認：實際輸出像素（預期 1536×2048，以實際輸出為準）、套框後髮頂與雙手是否在框內、有效 ppi（若 1536 px／120 mm 約 325 ppi；300 是本案工作目標，不是廠商已確認的最低標準）。 |
| 印刷措辭 | printing.accepted_impact.summary | 8 套已接受的企劃內容都不需要為印刷改動；H-coco-wu、H-rainie-hsu 是橫式膝上，放入框後下緣會再往上移約 2–3 cm，生成後若接近膝蓋，4 mm 的裁切改由頭頂留白多取——這是後製裁切位置，不改服裝、場景、表情或 prompt，不列待確認。 | 依暫定框與規劃構圖，8 套已接受暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。H-coco-wu、H-rainie-hsu 是橫式膝上：套框後下緣理論上會往上移（依規劃構圖估算約 2–3 cm），若實圖接近膝蓋，4 mm 改由頭頂留白多裁——這是後製裁切位置，不改服裝、場景、表情或 prompt，不列待確認。 |
| 印刷措辭 | composition.recommend[H] | 暫定照片框：橫式大照片框 192×104 mm（畫布 6,14–198,118）。生成用 16:9（原生尺寸未知）：放入後上下各裁約 2 mm。版面待 Penny 定案，見「印刷構圖」。 | 暫定照片框：橫式大照片框 192×104 mm（畫布 6,14–198,118）。生成用 16:9（原生尺寸未知）：比例上要裁掉高度 4 mm，規劃上下各約 2 mm。版面待 Penny 定案，見「印刷構圖」。 |
| 印刷措辭 | composition.recommend[V] | 暫定照片框：直式 3:4 框 120×160 mm（畫布 12,16–132,176）。生成用 3:4（原生 1536×2048，已知）：放入不裁切、約 325 ppi。版面待 Penny 定案。 | 暫定照片框：直式 3:4 框 120×160 mm（畫布 12,16–132,176）。生成用 3:4：比例上不裁切；若輸出 1536×2048，約 325 ppi（比例計算，以實際輸出為準）。版面待 Penny 定案。 |
| 印刷措辭 | composition.eval[近方形框] | 直式款若最後用近方形框（約 0.94:1），3:4 要上下共裁約 20%：膝上變大腿以上、全身會切到腳。所以建議直式款的照片區至少 3:4。 | 直式款若最後用近方形框（120×128，約 0.94:1），3:4 原圖高度要裁掉約 20%（比例事實）；會不會切到髮頂或腳要看實圖與裁切位置。所以建議直式款的照片區至少 3:4。 |
| 印刷措辭 | composition.eval[人物大小] | 避免人物縮小到背景裡：全身與坐姿的人物佔畫面高度約 85%（斜躺的 Rin 佔畫面寬度約 87%）；裁切景別保留完整髮頂、上緣約 4–10% 留白。 | 避免人物縮小到背景裡（以下是 prompt 規劃目標，不是實圖量測）：全身與坐姿的人物佔畫面高度約 85%（斜躺的 Rin 佔畫面寬度約 87%）；裁切景別保留完整髮頂、上緣約 4–10% 留白。 |

另有 24 套逐張印刷文字的措辭修訂（共 25 套），新文字見 3c；舊文字保留在資料檔 `r5.changes`。

## 1. 授權與主管覆核（M-4 R2，逐字）

> 資料檔：`data/cal_m4_authorization_r2.json`（2026-10-20）。主管（ChatGPT）的 M-4／R2 任務單「TASK-CAL-001／M-4／R2｜V-Iris單張首試｜執行指令」【授權，已生效】與【一、同步R1覆核結論】；成果基準 706618f、送審基準 f511887。逐字保存 Penny 同意的授權條件（主管轉述）與主管的 R1 覆核結論。授權只限 V-Iris 1 張、預算最多 1 credit、送出前精確報價須 ≤0.12 credits、只送一次，失敗或逾時都不重送；不擴大為 24 套生成、訓練或重試授權，也不是無限制授權。1 credit 是本次核准預算，工具沒有強制費用上限，不能宣稱平台保證不超扣。

```text
Penny已同意主管提出的具體條件：
V-Iris試拍1張，預算最多1 credit；送出前精確報價須≤0.12 credits，只送一次，失敗或逾時均不重送。
本指令即主管M-4生成指令，不再要求相同授權。
不擴大為24套生成、訓練或重試授權。
```

**主管對 R1 的覆核（逐字）：**

```text
1. M-4 R1首試準備PASS。
2. 接受以既有生產紀錄＋單張首試驗收；不補生6張、不重訓。
3. 交易歸屬只標「依時窗及唯一任務推定」；沒有工作ID的帳單不得標成直接對帳確認。
4. 刪除「credits 1足以證明會扣1 credit」的推論；精確報價與實扣分列。
5. 工具沒有強制費用上限；1 credit是本次核准預算，不能宣稱平台保證不超扣。
6. 保存Penny本次授權與上下文，不寫成無限制授權。
```

## 1a. 主管結論（M-4 R1，歷史，逐字）

> 資料檔：`data/cal_m4_supervisor_r1.json`（2026-10-20）。主管（ChatGPT）的 M-4／R1 任務單「TASK-CAL-001／M-4／R1｜V-Iris首試前核查（不生成）」：【主管結論】與【直接執行】。成果基準 f694e1b、送審基準 88e3944。逐字保存主管結論與本輪指示。這是主管的覆核結論，不是 Penny 的新回饋；H-Luna 是「依 owner 指示修訂、主管覆核通過」，不寫成 Penny 看過修訂後的版本。不再要求 owner 填企劃問卷。

```text
M-3／R7 PASS，M-3完成。
23套owner接受＋H-Luna依owner指示修訂、主管覆核通過。
不要把Luna寫成Penny看過新版本；不再要求owner填企劃問卷。
```

**本輪指示（逐字）：**

```text
1. 保存本次主管結論，同步資料、文件與頁面為M-3完成，保留歷史與localStorage。
2. 修正CAL_20及其來源資料中「Penny核定這套造型與費用」的過期前提：
V-Iris造型已接受，不再等待造型核准；生成與費用尚未授權。
3. 定向查既有Iris紀錄，確認Soul身分對應、驗證證據及既有成圖可否支持首試。不因缺少6張驗證紀錄就自行重新訓練或補生6張。
4. 本輪允許不扣credits、不建立生成任務的唯讀查詢，核對當前模型參數、Soul狀態及可取得的費用資訊。報價預檢只在工具明確保證不扣款、不生成時執行；否則列待確認。
5. 整理首試單次請求的確切設定、報價與計價單位、失敗扣款規則，以及建議費用上限。歷史約數與當前報價分列，不把0.12推測為實扣。
6. 交易核對須能關聯本次請求與扣款；多人共用帳號時，不能只憑時間相近或前後差額認定。
7. V-Iris已接受prompt保持不變。主管接受本次檢查表差異：胸口高度不補寫公分、正面看鏡頭、夕陽輪廓光配前方補光；出圖後依驗收條件判定。
8. 不生成、不重試、不訓練、不上傳、不取回新原圖、不扣credits。
```

## 1b. R7：owner 決策（歷史，逐字，主管轉述）

> 資料檔：`data/cal_m3_owner_feedback_r7.json`（2026-10-20）。主管（ChatGPT）在 R7 任務單「【Penny 最新指示，直接落實】」轉述的 Penny 決策與一則原文；企劃版本是 shoot-plan-v6、頁面版本是 c47b911（R6 部署）。逐字保存主管轉述的 Penny 決策與 H-luna-tanaka 的原文。只有引號內那一句是 Penny 原話；香袋的位置、顏色、材質、大小與手勢細節是主管在 R7 任務單「一、H-Luna 局部修訂」的補充，另列在 supervisor，不是 Penny 原話。Penny 還沒有看過修訂後的 H-Luna，這裡不記為已接受；也不是生成或費用授權。

```text
1. H-jia-seo 接受，連同原22套，共23套明確接受。
2. H-luna-tanaka 唯一修改：
「讓她雙手拿一個日式小香包，小香袋那種，很典雅氣質的感覺」
3. Penny 已要求小幅修訂後直接往後執行，不再回來詢問相同企劃決策。
4. 月份、照片框與其餘23套維持。
5. 這次仍不是生成或費用授權。
```

**Penny 原文（R7）：**

- H-luna-tanaka（10 月）：「讓她雙手拿一個日式小香包，小香袋那種，很典雅氣質的感覺」

**主管的收尾指示（逐字，不是 Penny 原話）：**

```text
- H-Jia 記為本次已接受。
- H-Luna 記為「依owner指定修訂，待主管核對落實」。
- 不虛構Penny已看過並接受修改後版本。
- 主管核對符合指示後即可完成M-3，不再要求Penny回覆香袋顏色、手勢或整套企劃。
- 頁面改為定稿進度與內容查閱，取消本輪必填決策。
- 保留v1–v6回饋、素材選擇與localStorage，不重設舊資料。
```

**可執行摘要（整理，不是 Penny 原話）：**

- 已接受 23 套（R4 的 8 套＋R6 的 14 套＋R7 的 H-jia-seo）：H-coco-wu、H-mia-huang、H-rainie-hsu、V-iris-chen、V-luna-tanaka、V-coco-wu、V-mia-huang、V-yerin-han、H-iris-chen、H-somi-oh、H-yuna-kim、H-tammy-chou、H-rin-ayase、H-miu-shiraishi、H-yerin-han、V-somi-oh、V-yuna-kim、V-tammy-chou、V-rin-ayase、V-rainie-hsu、V-miu-shiraishi、V-jia-seo、H-jia-seo——拍攝內容與 prompt 不變，不再要求回覆。
- H-luna-tanaka：依owner指定修訂，待主管核對落實（見第 3 節）。
- Penny 已要求小幅修訂後直接往後執行：不再請 Penny 回覆香袋顏色、手勢或整套企劃；主管核對 H-Luna 落實後即完成 M-3。
- 月份：維持（R4 已確認）
- 照片框：維持（R6 已接受的工作照片框）
- 首試：方向已接受（R6）；R7 只做首試準備，生成與費用仍未授權
- 尚未核准：生成、費用（credits）、Higgsfield 呼叫與報價預檢、M-4 執行、廠商規格或印刷安全。

## 1c. R6：owner 決策（歷史，逐字，主管轉述）

> 資料檔：`data/cal_m3_owner_feedback_r6.json`（2026-10-20）。主管（ChatGPT）轉述 Penny 在企劃頁（shoot-plan-v5，頁面版本 9434b83，R5 部署）填寫並複製的回饋。Penny 複製的文字第一行沿用頁面當時的「M-3／R4」標題，但企劃版本是 shoot-plan-v5、頁面版本是 9434b83，所以這是本輪（R6）最新回饋，不是舊決策。逐字保存主管轉述的 Penny 決策與兩則原文回饋；Penny 頁面上複製的完整原文沒有直接提供給執行者，所以這裡不是頁面 radio 統計，也沒有把舊版回饋當成新回饋。主管的修訂推薦另列，不是 Penny 原話。

```text
1. 原16套修訂中，14套接受。
2. 加上先前8套，共22套接受。
3. 只有 H-jia-seo、H-luna-tanaka 待修改。
4. 兩本月份維持既定排序。
5. 印刷構圖示意與暫定照片框接受：
   H 192×104 mm，生成比例16:9；
   V 120×160 mm，生成比例3:4。
   這是本案工作版型的接受，不是廠商規格、印刷安全或成品核准。
6. V-Iris 首試方向已接受；生成與費用仍未授權。
```

**Penny 對兩套的原文回饋：**

- H-jia-seo（9 月）：「他這個衣服跟場景有搭嗎？」
- H-luna-tanaka（10 月）：「這樣的場景，你不如讓他穿和服，很日式那種感覺，也不是一定要在和室內，可以在日式建築的庭院內，看得到建築內是和室，但他是站在室外，穿著和服」

**可執行摘要（整理，不是 Penny 原話）：**

- 已接受 22 套（R4 的 8 套＋R6 的 14 套）：H-coco-wu、H-mia-huang、H-rainie-hsu、V-iris-chen、V-luna-tanaka、V-coco-wu、V-mia-huang、V-yerin-han、H-iris-chen、H-somi-oh、H-yuna-kim、H-tammy-chou、H-rin-ayase、H-miu-shiraishi、H-yerin-han、V-somi-oh、V-yuna-kim、V-tammy-chou、V-rin-ayase、V-rainie-hsu、V-miu-shiraishi、V-jia-seo——拍攝內容與 prompt 不變，不再要求回覆。
- 待決 2 套：H-luna-tanaka、H-jia-seo（R6 新推薦，見第 3 節）。
- 月份：兩本月份人選排序維持既定排序（已確認），不再提問。
- 照片框：印刷構圖示意與工作照片框已接受：H 192×104 mm（生成 16:9）、V 120×160 mm（生成 3:4）。這是本案工作版型的接受，不是廠商規格、印刷安全或成品核准。
- 首試：V-Iris 首試方向已接受；生成與費用仍未授權，不執行 M-4。
- 尚未核准：H-jia-seo、H-luna-tanaka 的 R6 新推薦（待 Penny 看頁面決定）、任何生成與費用、廠商規格、印刷安全與成品。

## 1d. R4：owner 決策（歷史，逐字，主管轉述）

> 資料檔：`data/cal_m3_owner_feedback_r4.json`（2026-10-19）。M-3／R4 owner 決策與逐套修改要求逐字紀錄。來源是主管（ChatGPT）轉述的本輪指令；Penny 在頁面複製的原始回饋文字沒有直接提供給執行者，所以這裡保存的是主管轉述的原文，不是頁面 radio 統計，也不是舊版回饋。

```text
【最新 owner 決策】
1. 8套接受、16套修改。
   H-Jia 雖未勾選，但文字明確要求換場景，列為修改。
2. H與V兩本的月份人選排序已確認。
   不要求Penny重新核准排序；服裝與場景配合既定月份。
3. 整體偏好更多戶外、更加性感，表情與姿態都要有寫真感。
4. 已接受的8套不因整體偏好而擅自重設。
5. V-Iris首試方向已同意；費用與生成仍未授權。
```

```text
【一、紀錄與狀態】
逐字保存本次Penny回饋，另列可執行摘要。
不要只憑頁面radio統計。
不要把舊版回饋冒充最新決定。

已接受、保留8套：
H-coco-wu
H-mia-huang
H-rainie-hsu
V-iris-chen
V-luna-tanaka
V-coco-wu
V-mia-huang
V-yerin-han

若發現印刷構圖問題，另列必要技術調整；
不能暗中改掉已接受的服裝、場景或表情。
```

**可執行摘要（整理，不是 Penny 原話）：**

- 已接受 8 套：H-coco-wu、H-mia-huang、H-rainie-hsu、V-iris-chen、V-luna-tanaka、V-coco-wu、V-mia-huang、V-yerin-han——服裝、場景、表情與攝影照 v4，不因整體偏好重設。
- 修訂 16 套：H-yuna-kim、H-rin-ayase、H-miu-shiraishi、H-tammy-chou、H-yerin-han、H-iris-chen、H-jia-seo、H-luna-tanaka、H-somi-oh、V-tammy-chou、V-jia-seo、V-miu-shiraishi、V-rainie-hsu、V-rin-ayase、V-yuna-kim、V-somi-oh。H-jia-seo 頁面上沒有勾選，但文字明確要求換場景，依 owner 紀錄列為修改。
- 月份：兩本月份人選排序已確認（R4），不再請 Penny 重新核准；服裝與場景配合既定月份。
- 整體：整體偏好更多戶外、更加性感，表情與姿態都要有寫真感；已接受的 8 套不因整體偏好而重設。
- 首試：V-iris-chen 首試方向已同意；費用與生成仍未授權，不執行 M-4。
- 尚未核准：16 套的新主推薦（主管推薦的修訂起點，尚未經 Penny 批准）、暫定照片框與印刷安全構圖（只是示意，不是印刷安全證明）、生成與費用。

## 1e. R3：Penny 的攝影設計要求（逐字，仍適用）

> 資料檔：`data/cal_m3_owner_feedback_r3.json`（2026-10-19）。M-3／R3 Penny 最新要求逐字紀錄（主管轉述）。只保存需求原文；本輪執行的攝影設計是推薦，不是 owner 核准。

```text
【Penny 最新要求】
每張寫真必須明確規劃景別、拍攝角度與構圖。
可以安排半身、全身、較近的臉部特寫、大腿以上等不同景別，
並細緻規劃正面、側面等角度。
不能只說服裝、場景、姿態，讓模型自行決定怎麼拍。

現有技術區雖有部分景別，但不夠直觀，整組也過度集中正面膝上。
本輪補齊攝影設計，不全面推翻已規劃的服裝與場景。

維持：
- 12 位、24 套獨立拍攝。
- 同人 H／V 的服裝與場景不同。
- 兩本月份排序不同，仍待 Penny 定案。
- 專業美女寫真，以人物魅力與設定身材為核心。
- Iris 兩款身體正面、有笑容，不改回背部回眸。
- 生成與費用尚未授權。
```

```text
三、尊重既有要求
Iris：
兩款身體正面、有笑容。
可以透過景別、相機高度、手部與畫面配置做差異，
不能再變成背部回眸。

Luna、Miu：
取景與手部不能把胸型、腰線全部遮住。
身材依設定，不照抄舊圖錯誤比例。

Yerin：
性感可愛的高爾夫形象寫真，不打球、不展示球技。

Mia、Jia：
維持去電競、去運動工作照；Jia 不改回棚拍。

其他已接受方向保持，只有構圖確有衝突才調整，
並明確列出調整原因。
```

```text
Penny 尚未批准其餘人物的具體角度。
你可以提出推薦，不能寫成 owner 已核准。
```

**落實方式：** R7：23 套已接受（R4 的 8 套＋R6 的 14 套＋R7 的 H-jia-seo），拍攝內容與 prompt 不變；H-luna-tanaka 依 Penny 指定只把手部改為雙手輕捧日式小香袋，其他攝影欄位不變，中文與英文 prompt 由同一份設定產生並檢查。M-4 R1 主管結論：M-3 完成；H-Luna 依 owner 指示修訂、主管覆核通過（Penny 沒有看過修訂後的版本）。

**共同規則：**

- 景別依 Penny 指定的名稱：胸上／腰上／大腿中段以上／膝上／全身，坐姿與斜躺另寫「坐姿全身」「席地坐姿全身」「斜躺全身」，池邊坐姿寫「坐姿到水面」。不用含糊的「半身」。
- 裁切不落在關節：膝上切在膝蓋下方的小腿上段；大腿中段以上切在膝蓋上方很遠；腰上切在腰線下方、臀部上方；胸上切在胸線下方、手肘上方。所有景別都保留完整髮頂。
- 鞋只在腳會入鏡的景別（全身、坐姿全身、席地坐姿全身、斜躺全身）寫進 prompt；其他景別的鞋在中文服裝欄標「不入鏡」，不當成這張照片的賣點。
- 身體朝向、臉部朝向、相機高度分開寫：身體用「正面／約30度斜側／約45度斜側／側面」，臉用「臉正面／三分之二側臉」，相機寫「她的哪個高度＋平視／輕俯／輕仰」。
- 俯仰由「畫面中心高度」與「相機高度」換算：差距小於約 2.5 度寫平視，2.5–8.5 度寫輕俯或輕仰，超過就讓建置失敗；也檢查相機到臉的仰角不超過 15 度，避免由下往上拍到鼻孔。
- 身體與頭部的扭轉不超過約 60 度（側身站姿、臉轉成三分之二側臉約 55 度）；完整側臉不能同時寫看鏡頭。24 套都沒有背面或回眸。
- 焦段與距離只是給模型的合理參考，比例換算不是生成保證。本輪不新增固定的日期區，也不做未確認的印刷承諾。

## 2. 兩本攝影總覽（月份已確認；M-3 完成：23 套已接受＋H-Luna 主管覆核通過）

### 2.1 橫式款（16:9）

| 月份（已確認） | 人物 | 狀態 | 景別 | 身體方向 | 臉部方向 | 視線 | 相機角度 | 人物位置 | 主要展示重點 |
|---|---|---|---|---|---|---|---|---|---|
| 1 月 | Yuna（H-yuna-kim） | 已接受 | 大腿中段以上 | 約30度斜側（朝畫面右） | 臉正面 | 看鏡頭 | 胸口高度・平視 | 略偏左（右側小徑延伸） | 水光妝感、冬日穿搭的胸腰線 |
| 2 月 | Rin（H-rin-ayase） | 已接受 | 斜躺全身 | 側面斜躺（朝畫面右） | 三分之二側臉 | 看向畫面右側窗外的夕陽（不看鏡頭） | 略高於她斜躺時頭部的高度・輕俯 | 橫跨中央（頭在左、腳在右） | 側躺 S 形曲線、長腿、望向夕陽 |
| 3 月 | Miu（H-miu-shiraishi） | 已接受 | 坐姿全身 | 約45度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 坐姿時的腰部高度・平視 | 中央偏右（床成對角線） | 胸型、細腰、腿線、甜笑 |
| 4 月 | Tammy（H-tammy-chou） | 已接受 | 全身 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 膝蓋高度・輕仰 | 略偏左（長椅在右側） | 合身洋裝全身線條、高跟鞋與腿長 |
| 5 月 | Yerin（H-yerin-han） | 已接受 | 坐姿全身 | 約45度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 坐姿時的腰部高度・平視 | 中央偏右（球車與長腿成對角線） | 長腿、俏皮笑容、高爾夫裝扮 |
| 6 月 | Coco（H-coco-wu） | 已接受 | 膝上 | 約30度斜側（朝畫面右） | 臉正面 | 看鏡頭 | 胸口高度・平視 | 置中（花壟對稱收攏） | 大笑、V 領胸型與收腰 |
| 7 月 | Mia（H-mia-huang） | 已接受 | 大腿中段以上 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 胸口高度・平視 | 置中（摩天輪光點在右肩後） | 馬甲胸腰比例、俏皮眨眼 |
| 8 月 | Iris（H-iris-chen） | 已接受 | 全身 | 正面 | 臉正面 | 看鏡頭 | 膝蓋高度・輕仰 | 略偏左（右側海灣） | 胸腰臀線、腿長、燦笑 |
| 9 月 | Jia（H-jia-seo） | 已接受 | 坐姿全身 | 側面（朝畫面左） | 三分之二側臉 | 看向畫面左側的湖面與遠岸（不看鏡頭） | 坐姿時的腰部高度・平視 | 中央偏右（左側湖面） | 直角肩、上背、收腰、交疊的長腿 |
| 10 月 | Luna（H-luna-tanaka） | 依owner指示修訂，主管覆核通過 | 全身 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 臀部高度・平視 | 右側約六成（左側緣側與和室） | 完整和服與腰帶、雙手輕捧的小香袋、身形比例、甜美淺笑 |
| 11 月 | Somi（H-somi-oh） | 已接受 | 膝上 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 腰部高度・平視 | 偏左（吧台往右延伸） | 敞開開襟下的胸型、腰臀曲線、月牙眼大笑 |
| 12 月 | Rainie（H-rainie-hsu） | 已接受 | 膝上 | 正面 | 臉正面 | 直視鏡頭 | 腰部高度・平視 | 偏右（左側城市燈海） | 氣場、馬甲胸腰線、高衩腿線 |

**景別：** 大腿中段以上 2、膝上 3、全身 3、坐姿全身 3、斜躺全身 1；**身體方向：** 正面 2、約30度斜側 6、側面斜躺 1、約45度斜側 2、側面 1。

**節奏：** 橫式款：大腿中段以上 2、膝上 3、全身 3、坐姿全身 3、斜躺全身 1。戶外 9 套、室內 3 套；坐或躺的 4 套（Miu、Yerin、Jia、Rin）姿勢各不相同：床上靠枕半倚、球車座椅邊緣後靠、湖畔長椅側坐、貴妃椅全身側躺；Luna 在 R6 改為站姿全身的和服外景。

**依推薦月份的景別順序：** 1月 大腿中段以上（Yuna）→2月 斜躺全身（Rin）→3月 坐姿全身（Miu）→4月 全身（Tammy）→5月 坐姿全身（Yerin）→6月 膝上（Coco）→7月 大腿中段以上（Mia）→8月 全身（Iris）→9月 坐姿全身（Jia）→10月 全身（Luna）→11月 膝上（Somi）→12月 膝上（Rainie）

### 2.2 直式款（3:4）

| 月份（已確認） | 人物 | 狀態 | 景別 | 身體方向 | 臉部方向 | 視線 | 相機角度 | 人物位置 | 主要展示重點 |
|---|---|---|---|---|---|---|---|---|---|
| 1 月 | Tammy（V-tammy-chou） | 已接受 | 大腿中段以上 | 正面 | 臉正面 | 看鏡頭 | 腰部高度・輕仰 | 置中（吊燈在頭頂上方） | 自信姿態、深 V 翻領與腰帶的胸腰比例、素面小包 |
| 2 月 | Jia（V-jia-seo） | 已接受 | 全身 | 約45度斜側（朝畫面右） | 臉正面 | 看鏡頭 | 臀部高度・平視 | 置中（葉子框住兩側） | 腰臀輪廓、開衩腿線、細腰 |
| 3 月 | Mia（V-mia-huang） | 已接受 | 胸上 | 約30度斜側（朝畫面右） | 三分之二側臉 | 看鏡頭 | 眼睛高度・輕俯 | 略偏左（花枝框住右上） | 臉與甜笑、露肩領口與胸型 |
| 4 月 | Miu（V-miu-shiraishi） | 已接受 | 坐姿全身 | 約30度斜側（朝畫面右） | 三分之二側臉 | 看向畫面右側開滿白花的果樹（不看鏡頭） | 坐姿時的腰部高度・平視 | 中央偏左（右側開花果樹） | 心形領胸型、細腰、腿線、自然的笑 |
| 5 月 | Rainie（V-rainie-hsu） | 已接受 | 膝上 | 約30度斜側（朝畫面左） | 三分之二側臉 | 看向畫面左側前方的街燈（不看鏡頭） | 腰部高度・平視 | 右側約六成（左側街燈） | 沉思神情、胸臀曲線、長風衣直線 |
| 6 月 | Luna（V-luna-tanaka） | 已接受 | 全身 | 正面 | 臉正面 | 看鏡頭 | 膝蓋高度・輕仰 | 略偏左（約四成） | 整件洋裝、胸腰比例、腿長 |
| 7 月 | Coco（V-coco-wu） | 已接受 | 坐姿到水面 | 正面 | 臉正面 | 看鏡頭 | 坐姿時的胸口高度・平視 | 置中（水面在下） | 比基尼胸腰線條、歪頭大笑 |
| 8 月 | Yerin（V-yerin-han） | 已接受 | 膝上 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 臀部高度・輕仰 | 略偏右（天空在上方與左側） | 修長身形、健康的胸腰臀曲線 |
| 9 月 | Iris（V-iris-chen） | 已接受 | 大腿中段以上 | 正面 | 臉正面 | 看鏡頭 | 胸口高度・平視 | 置中 | Penny 指定穿搭：短上衣胸型、露腰、牛仔迷你裙；笑容 |
| 10 月 | Rin（V-rin-ayase） | 已接受 | 膝上 | 約45度斜側（朝畫面左） | 三分之二側臉 | 看向畫面左側港口的出口與海面（不看鏡頭） | 腰部高度・平視 | 中央偏右（左側港口與帆船） | 裹身洋裝胸腰線、開衩腿線、成熟側臉 |
| 11 月 | Yuna（V-yuna-kim） | 已接受 | 全身 | 約30度斜側（朝畫面右） | 三分之二側臉 | 看向畫面右側銀杏大道的深處（不看鏡頭） | 臀部高度・平視 | 略偏左（右側大道延伸） | 腿長、毛呢套裝與長靴、自然神情 |
| 12 月 | Somi（V-somi-oh） | 已接受 | 全身 | 正面 | 三分之二側臉 | 看向畫面右上方燈籠旁飄落的雪（不看鏡頭） | 臀部高度・平視 | 略偏左（右上方燈籠與雪） | 看雪的自然笑容、冬季整體造型 |

**景別：** 胸上 1、大腿中段以上 2、膝上 3、全身 4、坐姿全身 1、坐姿到水面 1；**身體方向：** 正面 5、約30度斜側 5、約45度斜側 2。

**節奏：** 直式款：胸上 1、大腿中段以上 2、膝上 3、全身 4、坐姿全身 1、坐姿到水面 1。戶外 10 套、室內 2 套；站姿置中只有 Tammy、Iris、Jia 三張，景別或角度各不相同。

**依推薦月份的景別順序：** 1月 大腿中段以上（Tammy）→2月 全身（Jia）→3月 胸上（Mia）→4月 坐姿全身（Miu）→5月 膝上（Rainie）→6月 全身（Luna）→7月 坐姿到水面（Coco）→8月 膝上（Yerin）→9月 大腿中段以上（Iris）→10月 膝上（Rin）→11月 全身（Yuna）→12月 全身（Somi）

**近景：** 近景：V-mia-huang 胸上；大腿中段以上 4 張（H-mia-huang、H-yuna-kim、V-iris-chen、V-tammy-chou）。沒有純臉部特寫，身材展示優先。

**角度與視線：** 不看鏡頭 7 套（H-rin-ayase、H-jia-seo、V-somi-oh、V-yuna-kim、V-rin-ayase、V-rainie-hsu、V-miu-shiraishi），每套都有明確的視線目標；其餘看鏡頭。正面膝上站姿只剩 H-rainie-hsu（已接受）。側面 2 套（H-jia-seo 側坐、H-rin-ayase 側躺）。

**同一位的兩款：** 12 位中有 9 位的 H／V 景別不同；Rainie 兩款都是膝上（正面直視 vs 斜側看街燈），Miu 兩款都是坐姿全身（室內床上半倚看鏡頭 vs 戶外吊床邊看果樹），Luna 兩款都是全身（秋季和服、約30度斜側、臀部高度平視 vs 初夏洋裝、正面、膝蓋高度輕仰）。每位的兩款在身體方向、相機高度或視線上至少一項不同。

**戶外與重複：** 整組戶外 19 套（R3 是 14 套）：室內改戶外 5 套（H-luna-tanaka、H-yuna-kim、H-tammy-chou、H-jia-seo、V-rin-ayase）；原本就在戶外、換了場景 2 套（H-iris-chen、V-miu-shiraishi）；庭園類 5 套（Coco 花田、V-Luna 町家後院、H-Luna 日式宅邸庭院、H-Tammy 花園露台、V-Miu 度假木平台；Luna 兩款都在日式庭院，用季節、建築新舊、服裝、身體方向與相機高度區分）、海景類 4 套（H-Iris 夏日上午岩岸、H-Mia 黃昏遊樂碼頭、V-Yerin 夕陽沙灘、V-Rin 秋日陰天港灣）時間與環境都不同；針織服裝 7 套（H-somi-oh、H-yuna-kim、H-tammy-chou、H-jia-seo、H-yerin-han、V-somi-oh、V-mia-huang），其中 H-yuna-kim（R4）與 H-jia-seo（R6）的針織是新選，其餘是已接受或 Penny 指定保留的服裝。

### 2.3 prompt 一致性檢查（產生資料時逐套執行，不通過就無法建置）

- 24 套都有七個攝影欄位，中文與英文成對；每個英文句都逐字出現在該套 prompt 裡（各一次）。
- 景別、焦段、距離、相機高度互相換算：裁切景別頭頂留白 4–10%，全身與坐姿人物佔畫面高度 82–90%，斜躺佔畫面寬度 80–90%；俯仰標示與換算結果一致。
- 沒有同時寫正面臉與完整側臉；完整側臉不看鏡頭的規則成立（本輪沒有用到完整側臉）。
- 非全身景別的 prompt 不含任何鞋、赤腳或腳鍊字樣；全身景別寫明腳與鞋完整。
- 胸上與腰上不寫放在膝上、腿旁或插腰的手；大腿中段以上不寫垂在身側或放在膝上的手（會落在邊緣）。
- 姿勢句不寫朝向（facing、toward the camera、at the camera 等），朝向只寫在 Body 與 Face 句，避免相機角度、身體方向、臉部方向混寫。
- 身體與頭部扭轉在 0–55 度；Iris 兩款身體正面、臉正面、看鏡頭、笑，沒有回眸字樣。
- 沿用 v3 的禁字檢查（Mia 去電競、Jia 不棚拍不運動、Yerin 不打球、Yuna 不靠地標文字等）、膚色只寫一次、adult。
- 同一位兩款服裝、場景仍不同；已接受方向（H-somi-oh、V-coco-wu、H-rainie-hsu、V-rin-ayase）的場景與光線原文不動；月份不變，且同一本相鄰月份不出現相同景別＋相同身體方向。
- R4：已接受 8 套的 prompt、攝影設計與服裝和 v4 逐字相同（程式比對）。R5：其中 V-iris-chen、H-coco-wu、V-coco-wu 依主管核可在 prompt 補一句妝感，其餘欄位仍與 v4 相同；另 5 套 prompt 仍與 v4 逐字相同。
- R4：16 套各有 owner 回饋原文（逐字）與「改了什麼」；兩本月份與 v4 相同。
- R4：整組禁字新增 sexy、girl、teen、schoolgirl、childlike、uniform、kawaii、Korean aesthetic、luxury brand；逐位新增：Yuna 不寫 café、Tammy 不寫 boutique／泥地／碎石／沙、Miu 不寫運河與欄杆、Jia 不寫美術館與畫作、Rin 不寫吧台與長禮服、Yerin 不寫 upskirt。
- R4：24 套的場景（env）彼此都不同；同一本相鄰月份不出現相同景別＋相同身體方向。
- R4：16 套修訂的中文「妝感」都寫進英文 prompt（人設身分句沒有妝感的 H-iris、H-somi、V-somi 另加一句；身分句本身不改）；已接受的 V-iris、H-coco、V-coco 在 R5 依主管核可補上妝感句。
- R6：H-jia-seo、H-luna-tanaka 用 R4 的同一套產生與檢查程式（禁字、鞋與腳、手、扭轉、俯仰、景別、prompt 片段各出現一次）；Luna 另加禁字 yukata、oiran、geisha、headdress、tiara、cleavage、antique、shabby 等，Jia 另加 gown、sequin、cut-out、one-shoulder。
- R6：其他 22 套由同一程式重新產生後，與 R5 版本逐欄相同（程式比對）；兩套的身分句（臉、膚色、髮、妝、身材）與 R5 相同。
- R6：不看鏡頭 7 套（H-Luna 依 Penny 指示改為看鏡頭）；戶外 19 套；同一位兩款同景別：Rainie、Miu、Luna（身體方向與相機高度不同）。
- R7：H-luna-tanaka 用 R6 的同一套產生與檢查程式重新產生（禁字、鞋與腳、手、遮擋、景別、prompt 片段各出現一次）；與 R6 產生器的輸出比對，只有手部、姿態、道具、入鏡、攝影目的、主要展示重點、英文 prompt 的三段、風險與參考備註不同。
- R7：其他 23 套由同一程式重新產生後與 R6 逐欄相同；企劃檔裡 23 套除了狀態與 R7 註記，整套資料與 R6 逐欄相同（程式比對）。

## 3. R7：H-Luna 依 owner 指定修訂（M-4 R1 主管覆核通過）

只改手部與香袋；主管 M-4 R1 覆核通過，M-3 完成。Penny 指定了這個修改，但沒有看過修訂後的版本；不再請 Penny 回覆香袋顏色、手勢或整套企劃。

### H-luna-tanaka｜10 月｜Luna｜依owner指示修訂，主管覆核通過

**M-4 R1：** 主管 M-4 R1 結論：M-3／R7 PASS，M-3 完成。Penny 指定了這個修改，但沒有看過修訂後的版本；不再要求 Penny 回覆。

**Penny 原文（R7）：**「讓她雙手拿一個日式小香包，小香袋那種，很典雅氣質的感覺」

**主管補充的落實細節（逐字，不是 Penny 原話）：**

```text
保留R6和服、庭院、月份、表情、身體朝向及攝影設定。
只將原本「一手扶腰帶、一手放下」改為：
- 雙手在腰帶下方、下腹前自然輕捧一個小巧日式布製香袋。
- 香袋採低飽和奶油色或淡金色、細緻織紋與短束口繩，與藕粉和服及深梅色腰帶協調。
- 尺寸小巧，不做成手提包；不加品牌、文字或誇張吊飾。
- 肩膀放鬆、手肘自然微彎，手腕不交叉，手指與香袋接觸合理。
- 袖子自然垂落，不遮臉、不完全蓋住雙手或香袋；腰帶仍清楚可見。
同步中文、英文prompt、道具欄、姿態與必要構圖說明。
若沒有香袋參考圖，照實標示；不新增生成。
```

- **改了什麼：** 依 Penny 指定（R7）：只把手部由「一手輕扶腰帶側邊、一手自然放下」改為雙手在腰帶下方、下腹前輕捧一個小巧的日式布製香袋（低飽和奶油色帶淡金細緻織紋、短束口繩）；肩膀放鬆、手肘微彎、手腕不交叉，袖子不遮臉、不完全蓋住雙手與香袋，腰帶清楚可見。和服、庭院、月份、表情、身體方向與相機設定都不變。
- **不變：** 保留 R6 的和服、庭院、月份（10 月）、表情（甜美的淺笑、看鏡頭）、身體方向（約30度斜側）與攝影設定（全身、50mm 約 4.6 公尺、臀部高度平視、人物佔畫面高度約 84%）；印刷判斷不變。
- **參考圖：** 既有照片都沒有香袋，也沒有正式和服；香袋外觀只靠文字描述，本輪不新增任何生成或示意圖。
- **R7 當時的狀態：** Penny 指定了這個修改，但還沒有看過修訂後的版本；主管核對落實後即完成 M-3，不再請 Penny 回覆香袋顏色、手勢或整套企劃。
- **攝影（不變）：** 全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・平視

**修改前（R6）→ 修改後（R7）：**

| 欄位 | 修改前（R6） | 修改後（R7） |
|---|---|---|
| 手 | 一手輕扶腰帶側邊，另一手自然放下；袖子不遮臉。 | 雙手在腰帶下方、下腹前自然輕捧一個小巧的日式布製香袋；肩膀放鬆、手肘自然微彎，手腕不交叉，手指自然貼著香袋；袖子自然垂落，不遮臉，也不完全蓋住雙手與香袋，腰帶清楚可見。 |
| 姿態 | 站在緣側旁的石板路上，身體斜側、臉轉向鏡頭。 | 站在緣側旁的石板路上，身體斜側、臉轉向鏡頭，雙手在腰帶下方輕捧小香袋。 |
| 道具 | （無） | 小巧的日式布製香袋（掌心大小；低飽和奶油色帶淡金細緻織紋、短束口繩；不是手提包，沒有品牌、文字或誇張吊飾） |
| 主題 | 秋日午後當代日式宅邸的庭院，藕粉秋草紋和服配深梅色腰帶，站在緣側旁的石板路上，身體斜側、轉頭對鏡頭甜美淺笑。 | 秋日午後當代日式宅邸的庭院，藕粉秋草紋和服配深梅色腰帶，雙手在腰帶下方輕捧一個小巧的日式香袋，站在緣側旁的石板路上，身體斜側、轉頭對鏡頭甜美淺笑。 |
| 畫面上下界（入鏡） | 入鏡：從髮頂到草履完整；藕粉秋草紋和服、深梅色腰帶與帶締、白足袋與草履；輕扶腰帶側邊的手與自然放下的手，袖子不遮臉 | 入鏡：從髮頂到草履完整；藕粉秋草紋和服、深梅色腰帶與帶締、白足袋與草履；雙手在腰帶下方輕捧的小香袋，腰帶露出，袖子不遮臉、也不完全蓋住雙手與香袋 |
| 攝影目的 | 站姿全身呈現完整的和服、腰帶位置與身形比例；身體斜側帶出線條，臉轉向鏡頭的甜美淺笑 | 站姿全身呈現完整的和服、腰帶位置與身形比例；雙手在腰帶下方輕捧小香袋，典雅端莊；身體斜側帶出線條，臉轉向鏡頭的甜美淺笑 |
| 主要展示重點 | 完整和服與腰帶、身形比例、甜美淺笑 | 完整和服與腰帶、雙手輕捧的小香袋、身形比例、甜美淺笑 |
| 英文 prompt：姿勢與手 | One hand rests lightly at the side of her obi and the other hangs naturally, her sleeves falling clear of her face; she gives a sweet, gentle smile. | Both hands rest together just below her obi in front of her lower abdomen, lightly holding a small, palm-sized Japanese fabric sachet in soft cream with a fine pale-gold woven texture and a short drawstring cord, plain and without any logos; her shoulders are relaxed, her elbows softly bent and her wrists uncrossed, her fingers resting naturally on the sachet, her sleeves falling naturally; she gives a sweet, gentle smile. |
| 英文 prompt：畫面上下界 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to her zori sandals, the dusty-pink kimono with its small autumn-grass pattern, the deep plum obi and its cord, the white tabi socks and zori, one hand resting at the side of the obi and the other hanging naturally, her sleeves clear of her face | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to her zori sandals, the dusty-pink kimono with its small autumn-grass pattern, the deep plum obi and its cord, the white tabi socks and zori, both hands just below the obi holding the small sachet, the obi left clear above them, her sleeves clear of her face, her hands and the sachet |
| 英文 prompt：攝影目的 | the full standing figure shows the whole kimono, where the obi sits and her proportions, the oblique stance adding shape while her face turns to the camera with a sweet smile | the full standing figure shows the whole kimono, where the obi sits and her proportions, both hands holding the small sachet below the obi for a graceful, elegant air, the oblique stance adding shape while her face turns to the camera with a sweet smile |
| 風險（新增 4 項） | （R6 的 6 項不變） | 香袋畫成手提包、太大，或出現品牌、文字、誇張吊飾→寫明掌心大小的布製香袋、短束口繩、without any logos；生成後檢查大小與表面；雙手或手指錯誤（手指數量、交纏、手腕交叉）→寫明雙手輕捧、手肘微彎、手腕不交叉；生成後逐指檢查；手或袖子遮住腰帶，香袋被袖子蓋住→寫明雙手在腰帶下方、腰帶露出、袖子自然垂落、不完全蓋住雙手與香袋；沒有香袋參考圖→既有照片都沒有香袋；外觀只靠文字，生成後檢查顏色、大小、束口繩與手的接觸 |
| 參考照片備註（luna-03） | 既有照片是夏季祭典浴衣（淺藍棉質＋深藍腰帶），不是本套的秋季正式和服；只參考她穿日式服裝、繫腰帶時的整體比例與笑容；浴衣、顏色、蘋果與神社街景都不採用；沒有正式和服的參考圖；不作身材參考：既有照片的身材不符合設定（Penny） | 既有照片是夏季祭典浴衣（淺藍棉質＋深藍腰帶），不是本套的秋季正式和服；只參考她穿日式服裝、繫腰帶時的整體比例與笑容；浴衣、顏色、蘋果與神社街景都不採用；沒有正式和服的參考圖；也沒有香袋的參考圖（R7 香袋外觀只靠文字）；不作身材參考：既有照片的身材不符合設定（Penny） |
| 為何符合她 | 依 Penny 指示：她是「住在美麗白日夢裡的人」，秋天的日式庭院、看得到和室的建築與正式和服，讓 Luna 的日式氣質最完整；人物站在室外，建築與紅葉只是陪襯。 | 依 Penny 指示：她是「住在美麗白日夢裡的人」，秋天的日式庭院、看得到和室的建築與正式和服，讓 Luna 的日式氣質最完整；人物站在室外，建築與紅葉只是陪襯。R7 依 Penny 指定：雙手輕捧一個日式小香袋，增加典雅氣質。 |

### R6 的 2 套新推薦（歷史：當時的 Penny 原文與改動）

| ID | R6 Penny 原文 | R6 改了什麼 | 目前 |
|---|---|---|---|
| H-luna-tanaka | 這樣的場景，你不如讓他穿和服，很日式那種感覺，也不是一定要在和室內，可以在日式建築的庭院內，看得到建築內是和室，但他是站在室外，穿著和服 | 依 Penny 指示：由室內旅宿的緞面斜坐，改為站在當代日式宅邸庭院（緣側旁石板路）的和服寫真；背景透過敞開的拉門看得到整潔嶄新的和室；服裝改為低飽和藕粉秋草紋正式和服＋深梅色名古屋帶、白足袋與草履；姿勢改為站姿全身、約30度斜側、臉轉向鏡頭甜美淺笑，一手輕扶腰帶側邊、一手自然放下；相機改為臀部高度平視。 | 依owner指示修訂，主管覆核通過 |
| H-jia-seo | 他這個衣服跟場景有搭嗎？ | 依 Penny「他這個衣服跟場景有搭嗎？」與主管判斷：湖畔木平台、臨水長椅、側坐、雙腿交疊、看湖面與相機都保留；偏晚宴的黑色單肩鏤空中長洋裝改為深酒紅細針織繞頸合身短洋裝（露肩與上背、收腰、裙長大腿中段、沒有運動元素或大型圖案）；鞋與配件維持簡單。 | 已接受（R7） |

### 23 套已接受（拍攝內容與 prompt 不變）

| ID | 月份 | 接受輪次 | 主題 | 攝影 | 印刷判斷 |
|---|---|---|---|---|---|
| H-iris-chen | 8 月 | R6 | 夏日上午的淺色平坦岩岸海灣，向日葵黃有骨架的平口馬甲短上衣配同色低腰迷你裙，身體正面燦笑。 | 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| H-somi-oh | 11 月 | R6 | Penny 已接受的方向（R4 只改上衣穿法）：暖橘復古小吃店棚景，敞開的奶油色短開襟＋鏽橘貼身細肩小可愛＋高腰針織短裙，輕靠吧台大笑。 | 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜腰部高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。膝上的下緣套框後理論上會略往上移；若實圖接近膝蓋，4 mm 改由頭頂留白多裁（後製裁切位置，不改拍攝方向）。 |
| H-coco-wu | 6 月 | R4 | 初夏傍晚的薰衣草花田，白色細肩亞麻洋裝，拿著草帽大笑。 | 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。膝上的下緣套框後理論上會略往上移；若實圖接近膝蓋，4 mm 改由頭頂留白多裁（後製裁切位置，不改拍攝方向）。 |
| H-mia-huang | 7 月 | R4 | 夏日黃昏的海邊遊樂碼頭，粉色緞面馬甲上衣配白色迷你裙，拿著棉花糖俏皮眨眼。 | 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| H-yuna-kim | 1 月 | R6 | 雪後清晨的白樺林小徑，霧玫瑰粉貼身方領針織上衣＋淺灰高腰羊毛迷你裙，外披敞開的白色短版羊羔毛外套。 | 大腿中段以上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| H-tammy-chou | 4 月 | R6 | 春日花園露台的平整石板步道，熱粉色方領貼身針織洋裝配白色露跟高跟鞋，站在庭園長椅旁明亮地笑。 | 全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜膝蓋高度・輕仰 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| H-rin-ayase | 2 月 | R6 | 夕陽中的高樓飯店套房，酒紅緞面垂墜領細肩長洋裝，側躺在深綠絲絨貴妃椅上望向窗外的夕陽。 | 斜躺全身｜側面斜躺（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側窗外的夕陽｜略高於她斜躺時頭部的高度・輕俯 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| H-rainie-hsu | 12 月 | R4 | Penny 已接受的方向：頂樓夜景，血紅緞面馬甲高衩迷你洋裝，背靠玻璃欄杆直視鏡頭。 | 膝上｜正面｜臉正面・看鏡頭｜腰部高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。膝上的下緣套框後理論上會略往上移；若實圖接近膝蓋，4 mm 改由頭頂留白多裁（後製裁切位置，不改拍攝方向）。 |
| H-miu-shiraishi | 3 月 | R6 | 晨光灑進的一人公寓，象牙白蕾絲緞面細肩小可愛與短褲，背靠床頭的枕頭堆自然半倚、歪頭甜笑。 | 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| H-jia-seo | 9 月 | R7 | 初秋傍晚的湖畔木平台，深酒紅合身繞頸細針織短洋裝露肩與上背，側坐在臨水長椅上、雙腿交疊望向湖面。 | 坐姿全身｜側面（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側的湖面與遠岸｜坐姿時的腰部高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| H-yerin-han | 5 月 | R6 | 春日球場的白色球車，白色無袖針織 polo＋淺藍百褶高爾夫迷你裙，坐在座椅邊緣微微後靠、伸長雙腿的俏皮笑容。 | 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-iris-chen | 9 月 | R4 | 黃金時段的河濱草地，白色方領短上衣配牛仔迷你裙，正面站著甜笑（Penny 指定的穿搭）。 | 大腿中段以上｜正面｜臉正面・看鏡頭｜胸口高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-luna-tanaka | 6 月 | R4 | 紫陽花盛開的町家庭院，鼠尾草綠馬甲感洋裝，正面站在石板路上。 | 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-somi-oh | 12 月 | R6 | 下雪的溫泉小鎮夜晚，象牙白貼身針織洋裝外披紅色長大衣，抬眼看著燈籠旁飄落的雪，自然地笑開。 | 全身｜正面｜三分之二側臉・不看鏡頭：看畫面右上方燈籠旁飄落的雪｜臀部高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-coco-wu | 7 月 | R4 | Penny 已接受的方向：週末飯店泳池，薄荷綠比基尼＋淺紫透膚罩衫，坐在池邊大笑。 | 坐姿到水面｜正面｜臉正面・看鏡頭｜坐姿時的胸口高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-mia-huang | 3 月 | R4 | 春夜的櫻花河岸步道，淺紫貼身露肩針織洋裝，站在花枝下甜笑。 | 胸上｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜眼睛高度・輕俯 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-yuna-kim | 11 月 | R6 | 深秋的銀杏大道，奶油色毛呢短外套套裝配黑色長靴，停下腳步望向大道深處、手裡拿著一片銀杏葉。 | 全身｜約30度斜側（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側銀杏大道的深處｜臀部高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-tammy-chou | 1 月 | R6 | 夜晚的大飯店大廳，白色西裝外套洋裝配素面黑色小手提包，一手拎包、一手插腰的自信笑容。 | 大腿中段以上｜正面｜臉正面・看鏡頭｜腰部高度・輕仰 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-rin-ayase | 10 月 | R6 | 秋日午後的安靜港灣石砌碼頭，墨綠仿麂皮裹身洋裝，倚著木頭繫船柱望向港口。 | 膝上｜約45度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側港口的出口與海面｜腰部高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-rainie-hsu | 5 月 | R6 | 雨後的夜晚街道，黑色緞面繞頸迷你洋裝外搭黑色長皮風衣，看向前方的街燈，放鬆、微啟唇的沉思神情。 | 膝上｜約30度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側前方的街燈｜腰部高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-miu-shiraishi | 4 月 | R6 | 春日度假別墅的木平台，杏桃色有骨架的細肩短洋裝，坐在白色帆布吊床邊，笑著看向開花的果樹。 | 坐姿全身｜約30度斜側（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側開滿白花的果樹｜坐姿時的腰部高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-jia-seo | 2 月 | R6 | 明亮的玻璃溫室，白色無袖立領短上衣配薄荷綠緞面高腰貼臀窄裙，斜側站在大葉植物之間，臀腰曲線清楚。 | 全身｜約45度斜側（朝畫面右）｜臉正面・看鏡頭｜臀部高度・平視 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |
| V-yerin-han | 8 月 | R4 | 日落的白沙海灘，白色圓領貼身針織背心洋裝，赤腳站在淺浪邊的燦笑。 | 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・輕仰 | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 |

### R4 的 16 套修訂（歷史：當時的 owner 原文與改動，見第 8 節各套）

| ID | R4 改了什麼（歷史） |
|---|---|
| H-iris-chen | 全面換掉紅磚騎樓與米杏針織套裝：改成夏日上午的淺色平坦岩岸海灣、向日葵黃有骨架的平口馬甲短上衣＋同色低腰迷你裙；身體正面、笑容不變；手改成雙手放在低腰裙腰頭兩側；相機改為膝蓋高度輕仰。 |
| H-luna-tanaka | 房間改成新穎整潔的當代日式旅宿（新榻榻米、乾淨木作、白色寢具），不再是古舊和室；服裝改為香檳色斜裁緞面細肩洋裝（仍是貼身緞面方向）；姿勢由端正側坐、雙手放腿上改為單手撐地的慵懶斜坐；視線看窗外紅葉。 |
| H-somi-oh | 短開襟不再全扣：改成「敞開的奶油色短開襟（全部不扣、從肩上垂下）＋鏽橘貼身方領細肩小可愛」兩層，衣物結構寫明；場景、光線、姿勢、大笑與構圖照 v4，不新增吃東西的動作。 |
| H-yuna-kim | 撤回咖啡館與奶油黃開襟＋淺藍裙：改成雪後白樺林小徑的戶外冬日寫真，霧玫瑰貼身方領針織＋淺灰高腰迷你裙＋敞開的白色羊羔毛短外套；景別由腰上改為大腿中段以上。主管推薦是雪後庭園／冬日花園露台，因整組庭園類場景已有 4 個，改提白樺林（理由見選擇理由）。 |
| H-tammy-chou | 取消精品店：改成春日花園露台的平整石板步道（不踩泥地、碎石或沙灘），熱粉合身洋裝＋白色高跟鞋保留；手改為一手扶白色庭園長椅、一手插腰；拿掉手提包（素面小包放到直式款）。 |
| H-rin-ayase | 保留酒紅緞面與斜躺；改為不看鏡頭、望向窗外夕陽；姿勢寫清楚：下方前臂撐椅墊、肩頸放鬆往後、腰側下凹臀線抬高、上方腿微彎搭在伸直的下方腿上、上方手放在大腿上。 |
| H-miu-shiraishi | 從端坐床邊、雙膝併攏雙手撐床，改為背靠枕頭的自然半倚（一膝立起、一腿伸直、手肘搭膝、另一手放床上），床改成斜放的對角線；服裝與晨光不變。 |
| H-jia-seo | 撤回美術館與畫作背景：改為初秋傍晚的湖畔木平台與臨水長椅；黑色單肩鏤空洋裝保留，加側開衩、鞋改低跟細帶涼鞋（木平台上較合理）；姿勢由側身站改為側坐、雙腿交疊；景別由全身改為坐姿全身；視線看向湖面。 |
| H-yerin-han | 保留高爾夫迷你裙裝與球車；坐姿改為坐在座椅邊緣、身體微微後靠、後手撐座椅、前手放膝上，雙膝併攏、腳踝交叉、腳尖點地；相機維持坐姿腰部高度平視，不俯拍、不低角度。 |
| V-somi-oh | 保留雪夜溫泉小鎮與冬季穿搭；改為不看鏡頭：抬眼看向右上方燈籠旁飄落的雪，一手攤開接雪，笑容由情境帶出；臉是三分之二側臉、眼睛睜開，不仰頭到看不清五官；人物改到略偏左。 |
| V-yuna-kim | 保留銀杏大道與毛呢套裝；改為不看鏡頭：停下腳步望向右側大道深處，柔和若有所思的微笑；另一手改成指尖輕拿一片銀杏葉在腰側；不擺打卡姿勢。 |
| V-tammy-chou | 加入素面黑色小手提包（不仿特定品牌）：一手拎包在臀側、一手插腰，包不遮胸腰；文案改正：這張是大腿中段以上，不再稱「全身照」；場景、服裝、景別、相機不變。 |
| V-rin-ayase | 撤回黑金高級吧台（最新意見取代先前選擇）：改成秋日午後的安靜港灣石砌碼頭，服裝改為墨綠仿麂皮裹身洋裝（深 V、繫帶收腰、前開衩）＋深棕踝靴；髮型改為鬆低髮髻；景別由坐姿全身改為膝上；不看鏡頭、望向港口。 |
| V-rainie-hsu | 保留雨後夜街與黑色服裝；改為不看鏡頭：看向前方街燈，表情改成放鬆、微啟唇、帶點沉思（不是橫式款的自信壞笑），臉不改；身體由側面改為約30度斜側；人物改到右側約六成，左側留給街燈。 |
| V-miu-shiraishi | 撤回運河與奶油 V 領針織裙：改為春日度假別墅木平台與白色帆布吊床，杏桃色有骨架的細肩短洋裝（配色與其他 23 套比較後選定）；姿勢由欄杆站姿改為坐在吊床邊、雙手抓布邊、微微前傾；不看鏡頭、看向開花的果樹；景別由大腿中段以上改為坐姿全身。 |
| V-jia-seo | 保留玻璃溫室；薄荷緞面中長裙改為高腰貼臀窄裙（腰頭在肚臍上方、貼臀往膝下收窄、左前側開衩到大腿中段）；景別由膝上改為全身、身體改為約45度斜側並把臀部往後側，讓輪廓真的看得出曲線；白色細帶涼鞋因全身入鏡寫回 prompt。 |

依已接受的工作照片框與規劃構圖，23 套已接受暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。H-somi-oh、H-coco-wu、H-rainie-hsu 是橫式膝上：套框後下緣理論上會往上移（依規劃構圖估算約 2–3 cm），若實圖接近膝蓋，4 mm 改由頭頂留白多裁——這是後製裁切位置，不改服裝、場景、表情或 prompt，不列待確認。H-luna-tanaka（依 owner 指定修訂）只改雙手與香袋：畫面上下界、人物佔比與印刷判斷都與 R6 相同。

**已接受套數的中英同步（已套用（R5，主管核可的中英同步））：** V-iris-chen、H-coco-wu、V-coco-wu 的中文「妝感」原本沒有寫進英文 prompt（Iris 與 Coco 的人設身分句沒有妝感）。R5 依主管核可，只在英文 prompt 的身分句後補一句妝感；服裝、場景、表情、姿態、攝影與身分都不變，接受狀態沿用。因此這 3 套的 prompt 不再與 v4 逐字相同；其他 5 套已接受的 prompt 仍與 v4 相同。

| ID | 中文妝感（已接受） | 已補進英文 prompt 的一句 |
|---|---|---|
| V-iris-chen | 乾淨的日常妝、自然唇色。 | `Fresh, light everyday makeup with a natural lip colour.` |
| H-coco-wu | 甜美淡妝、粉色唇。 | `Sweet, light makeup with a pink lip.` |
| V-coco-wu | 甜美淡妝。 | `Sweet, light makeup.` |

## 3b. 印刷規格與安全構圖（已知／假設／未知）

以下分成「已知」「假設」「未知」。已知值來自廠商編輯器設定與商品頁（R1 查證，本輪只重讀既有證據、沒有重查網站）；假設值是本案為了規劃先定的數字，不是廠商規格；未知要等廠商回覆或實際打樣。只有構圖方框不代表印刷安全。印刷數字再分成四類：已知尺寸、比例計算、prompt 規劃目標、生成後待驗證；表中的髮頂留白、腳下留白與「套框後約 x%」都是依規劃構圖推算的理論／規劃預估，不是實圖量測。R6：Penny 接受了兩款的工作照片框（H 192×104 mm 生成 16:9、V 120×160 mm 生成 3:4）；這是本案工作版型的接受，不是廠商規格、印刷安全或成品核准。

**四類數字：**

| 類別 | 內容 |
|---|---|
| 已知尺寸 | 成品 H 200×151、V 140×200 mm；出血四邊 2 mm；含出血畫布 H 204×155、V 144×204 mm；編輯器安全框 H 上 10、其餘 2 mm，V 0 mm（廠商編輯器設定與商品頁，見「已知」表）。 |
| 比例計算 | 由已知尺寸與照片比例算出的事實：16:9 放進 192×104 要裁掉高度 4 mm（約 3.7%）；3:4 放進 120×160 不裁；3:4 放進 120×128 要裁掉高度 20%；16:9 放進 104×155 要裁掉約 62% 寬度；1536 px 放在 120 mm 寬約 325 ppi、2048 px 放在 192 mm 寬約 271 ppi（像素數本身待驗證）。 |
| prompt 規劃目標 | 企劃寫給生成的構圖：髮頂留白、下緣位置、人物佔畫面比例、左右邊距。逐張表中的百分比與「套框後約 x%」都是依規劃構圖推算的理論／規劃預估，不是實圖量測。 |
| 生成後待驗證 | 實際輸出像素、套框後髮頂／臉／手／腳與關鍵服裝是否都在框內、有效 ppi、色彩與暗部——都要用實圖逐張確認。 |

**已知：**

| 項目 | 橫式 | 直式 | 來源 |
|---|---|---|---|
| 成品尺寸（裁切線） | 200×151 mm | 140×200 mm | docs/calendar/CAL_01_SPEC_EVIDENCE.md §5；商品頁規格、編輯器狀態列 |
| 出血 | 四邊各 2 mm | 四邊各 2 mm | docs/calendar/data/vendor_editor_config_2026-10-08.json（bleedMargin） |
| 含出血畫布 | 204×155 mm | 144×204 mm | docs/calendar/CAL_01_SPEC_EVIDENCE.md §5（範本 SVG 尺寸換算） |
| 編輯器安全框 | 裁切線內 上 10、右 2、下 2、左 2 mm | 0 mm（四邊） | docs/calendar/data/vendor_editor_config_2026-10-08.json（safeMargin） |
| 編輯器影像解析度設定 | imageDPI 300 | imageDPI 300 | docs/calendar/data/vendor_editor_config_2026-10-08.json |
| 裝訂 | 黑色雙環線圈（在上緣） | 黑色雙環線圈（在上緣） | docs/calendar/CAL_01_SPEC_EVIDENCE.md §5；商品頁規格 |

**假設（本案規劃用，不是廠商規格）：**

| 項目 | 橫式 | 直式 | 為什麼 |
|---|---|---|---|
| 線圈／裝訂區（規劃用） | 畫布上緣 0–12 mm | 畫布上緣 0–12 mm | 橫式＝出血 2＋廠商安全框 10；直式安全框是 0，不代表沒有裝訂區，所以沿用同一個 12 mm 假設（CAL_14 §1）。編輯器的線圈示意圖量得約 8.9 mm（橫）、9.7 mm（直），是量測值、不是廠商書面規格。 |
| 工作照片框（R6 Penny 已接受） | 畫布 (6,14)–(198,118)，192×104 mm | 畫布 (12,16)–(132,176)，120×160 mm | R6 Penny 接受為本案工作版型（H 192×104 mm 生成 16:9；V 120×160 mm 生成 3:4）；不是廠商規格、印刷安全或成品核准。照片框整個在安全區內、避開假設線圈區，所以照片本身不碰出血與裁切線。 |
| 日期區（暫定） | 畫布 (6,122)–(198,149) | 畫布 (12,180)–(132,200) | 只是示意位置；日期素材是廠商提供的點陣圖（CAL_01 §4）。 |
| 有效 ppi 工作目標 | 300 | 300 | 本專案自訂的工作目標，不是廠商門檻（廠商只公開「好／標準／差」三級，數字未知）。 |

**未知：**

- 實際線圈尺寸、打孔位置與裝訂區（廠商書面規格）
- 廠商「好／標準／差」三級對應的 ppi 門檻
- soul_2 16:9 的實際輸出像素（推測 2048×1152，未驗證）
- 上傳 RGB 是否自動轉 CMYK、色差與暗部表現（要打樣）
- 拼版與背面是否自動旋轉（影響立架兩側看到哪兩面，CAL_01 §3.3）

**暫定照片框與照片比例：**

| 款 | 暫定照片框 | 畫布座標（mm） | 來源 | 照片比例 | 放入後（比例計算） | 日期區（暫定） |
|---|---|---|---|---|---|---|
| 橫式款 | 橫式工作照片框（R6 已接受） 192×104 mm（約 1.85:1） | (6,14)–(198,118) | R3 版型的「橫 B」192×104（CAL_14 §1）；M-3 企劃一直建議的橫式大照片框 | 16:9（192×108 mm） | 比例計算：高度共裁 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm（各約 1.9%），實際分配依實圖 | (6,122)–(198,149) |
| 直式款 | 直式 3:4 工作照片框（R6 已接受） 120×160 mm（3:4） | (12,16)–(132,176) | 本輪提出：與 R3「直式統一框」同寬、同左右與上緣留白（12／16 mm），只把高度改成 3:4；月曆大格面另有一面 | 3:4（120×160 mm） | 比例計算：不裁切 | (12,180)–(132,200) |

**如果改用其他框：**

- 若橫式改用 R3「橫 A 半版」104×155（直幅）：比例計算：16:9 照片要裁掉約 62% 寬度才放得進這個直幅框（原文誤寫「約七成」），所以不建議從 16:9 硬裁，要另外規劃直幅照片。
- 若直式改用 R3「直式統一框」120×128（約 0.94:1）：比例計算：3:4 原圖放進 120×128 要裁掉高度 20%（160→128 mm）。裁在哪裡、會不會切到髮頂、腳或其他部位，要看實圖與裁切位置，不是必然；直式款可能要重新規劃上下留白。
- 若改成滿版出血照片：照片會進入假設線圈區（上緣 12 mm）與 2 mm 出血；背景延伸到出血區是正常的，但臉、髮頂、手腳與關鍵服裝要離開裁切線與線圈區，需要另外規劃餘量。

**示意圖：** 橫式 `decision_site/public/print/layout_H.svg`、直式 `decision_site/public/print/layout_V.svg`（只有方框與尺寸，不含照片；不是印刷安全證明）。

**原則：**

- 背景延伸到出血區是正常需求；臉、髮頂、手腳與關鍵服裝細節才要避開裁切與裝訂風險。
- 本輪的暫定照片框整個在安全區內，所以照片不碰出血線；真正會裁掉的只有「照片比例≠框比例」的部分（橫式 16:9→約 1.85:1，上下各約 2 mm）。
- 16:9 放進橫式框的 4 mm 裁切，原則上上下平均；若頭頂留白不足 4%，改從下緣多裁，反之亦然——以髮頂留白 ≥3%、下緣不落在膝或肘為準，生成後用實圖決定。
- 生成後仍須用實圖逐張確認裁切與有效 ppi；不預設 AI 放大或外擴已獲授權；不為安全餘量把人物縮小。
- 限制：線圈／裝訂區 12 mm 是假設；16:9 實際輸出尺寸未知；300 ppi 是本案工作目標，不是已確認的廠商最低標準。

### 3c. 24 套逐張印刷構圖判斷（依已接受的工作照片框）

百分比與「套框後約 x%」都是依規劃構圖推算的理論／規劃預估，不是實圖量測。

| ID | 狀態 | 照片框 | 比例計算 | 邊緣（規劃預估） | 不能切／規劃目標 | 印刷判斷（條件） | 生成後待驗證 | 原生尺寸 | 有效 ppi |
|---|---|---|---|---|---|---|---|---|---|
| H-iris-chen | 已接受 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 9%（套框後理論約 7.6%）；下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%） | 髮頂、臉、入鏡的雙手、雙腳與鞋／規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| H-luna-tanaka | 依owner指示修訂，主管覆核通過 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 9%（套框後理論約 7.1%）；下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%） | 髮頂、臉、入鏡的雙手、雙腳與鞋／規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| H-somi-oh | 已接受 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 8%（套框後理論約 6.4%）；下緣：規劃裁切線在膝蓋下方的小腿上段（套框後理論上往上移約 2 cm） | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。膝上的下緣套框後理論上會略往上移；若實圖接近膝蓋，4 mm 改由頭頂留白多裁（後製裁切位置，不改拍攝方向）。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| H-coco-wu | 已接受 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 7%（套框後理論約 5.0%）；下緣：規劃裁切線在膝蓋下方的小腿上段（套框後理論上往上移約 2 cm） | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。膝上的下緣套框後理論上會略往上移；若實圖接近膝蓋，4 mm 改由頭頂留白多裁（後製裁切位置，不改拍攝方向）。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| H-mia-huang | 已接受 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 8%（套框後理論約 5.9%）；下緣：規劃裁切線在大腿中段（套框後理論上往上移約 2 cm） | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| H-yuna-kim | 已接受 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 9%（套框後理論約 7.3%）；下緣：規劃裁切線在大腿中段（套框後理論上往上移約 2 cm） | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| H-tammy-chou | 已接受 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 9%（套框後理論約 7.2%）；下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%） | 髮頂、臉、入鏡的雙手、雙腳與鞋／規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| H-rin-ayase | 已接受 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 24%（套框後理論約 22.9%）；左右：規劃頭與腳離左右邊緣各約 7% | 髮頂、臉、入鏡的雙手、頭與腳／規劃目標（套框後）：髮頂上方 ≥4%、左右各 ≥5% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、頭與腳是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| H-rainie-hsu | 已接受 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 8%（套框後理論約 6.1%）；下緣：規劃裁切線在膝蓋下方的小腿上段（套框後理論上往上移約 3 cm） | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。膝上的下緣套框後理論上會略往上移；若實圖接近膝蓋，4 mm 改由頭頂留白多裁（後製裁切位置，不改拍攝方向）。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| H-miu-shiraishi | 已接受 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 9%（套框後理論約 7.5%）；下緣：規劃雙腳下方留白約 7%（套框後理論約 5.3%） | 髮頂、臉、入鏡的雙手、雙腳／規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| H-jia-seo | 已接受 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 8%（套框後理論約 6.7%）；下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%） | 髮頂、臉、入鏡的雙手、雙腳與鞋／規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| H-yerin-han | 已接受 | 橫式工作照片框（R6 已接受）（192×104 mm） | 比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖 | 上緣：規劃髮頂留白約 10%（套框後理論約 8.4%）；下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%） | 髮頂、臉、入鏡的雙手、雙腳與鞋／規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| V-iris-chen | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 8%；下緣：規劃裁切線在大腿中段 | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| V-luna-tanaka | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 9%；下緣：規劃雙腳與鞋下方留白約 5% | 髮頂、臉、入鏡的雙手、雙腳與鞋／規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| V-somi-oh | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 10%；下緣：規劃雙腳與鞋下方留白約 5% | 髮頂、臉、入鏡的雙手、雙腳與鞋／規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| V-coco-wu | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 11%；下緣：規劃水面下方留白約 8% | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| V-mia-huang | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 9%；下緣：規劃裁切線在胸線下方 | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| V-yuna-kim | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 8%；下緣：規劃雙腳與鞋下方留白約 5% | 髮頂、臉、入鏡的雙手、雙腳與鞋／規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| V-tammy-chou | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 6%；下緣：規劃裁切線在大腿中段 | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| V-rin-ayase | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 7%；下緣：規劃裁切線在膝蓋下方的小腿上段 | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| V-rainie-hsu | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 8%；下緣：規劃裁切線在膝蓋下方的小腿上段 | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| V-miu-shiraishi | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 8%；下緣：規劃雙腳與鞋下方留白約 5% | 髮頂、臉、入鏡的雙手、雙腳與鞋／規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| V-jia-seo | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 9%；下緣：規劃雙腳與鞋下方留白約 5% | 髮頂、臉、入鏡的雙手、雙腳與鞋／規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| V-yerin-han | 已接受 | 直式 3:4 工作照片框（R6 已接受）（120×160 mm） | 比例計算：3:4 放入 3:4 框不裁切 | 上緣：規劃髮頂留白約 7%；下緣：規劃裁切線在膝蓋下方的小腿上段 | 髮頂、臉、入鏡的雙手／規劃目標（套框後）：髮頂上方 ≥4% | 依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。 | 生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi | V 3:4：原生 1536×2048（已知） | 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |

### 3d. V-Iris 首試是否需要構圖微調

- 依暫定 3:4 框與規劃構圖，暫無須為印刷調整 V-Iris 的拍攝方向：3:4 照片放進 3:4 框在比例上不裁切；髮頂留白約 8%、下緣在大腿中段、雙手在框內是 prompt 規劃目標，不是實圖量測（R4 文字誤寫髮頂約 7%，依逐張表更正為約 8%）。
- 直式 3:4 工作照片框已在 R6 由 Penny 接受（120×160 mm），所以 V-Iris 依目前企劃不需要為照片框重排構圖；120×128 等其他框不再是現行方案。實際裁切仍要用實圖確認。
- 首試出圖後用實圖確認：實際輸出像素（預期 1536×2048，以實際輸出為準）、套框後髮頂與雙手是否在框內、有效 ppi（若 1536 px／120 mm 約 325 ppi；300 是本案工作目標，不是廠商已確認的最低標準）。
- R7：首張驗收條件（含套框與有效 ppi）見 `CAL_20_M4_IRIS_FIRST_TEST_PREP.md`。

## 4. R2 Penny 回饋落實表（歷史紀錄；最新決定見第 1、3 節）

| 人設 | Penny 回饋（逐字） | 當時（R2）怎麼落實（歷史，部分場景已在 R4 撤回） | 目前橫式款 | 目前直式款 |
|---|---|---|---|---|
| Iris | Iris： - 更顯身材的上衣，搭牛仔迷你裙。 - 身體面向鏡頭，專業寫真姿態、有笑容。 - 不要背部回眸或轉頭看鏡頭。 | 更顯身材的上衣：V 白色貼身方領短上衣（露腰）；H 貼身羅紋針織平口；牛仔迷你裙：V 淺藍高腰牛仔迷你裙；身體面向鏡頭、專業姿態、有笑容：兩款都正面站定（扶柱／插腰／碰髮）並微笑；不要背部回眸或轉頭：兩款 prompt 經程式檢查，不含回頭、轉身字樣 | 夏日上午的淺色平坦岩岸海灣，向日葵黃有骨架的平口馬甲短上衣配同色低腰迷你裙，身體正面燦笑。 | 黃金時段的河濱草地，白色方領短上衣配牛仔迷你裙，正面站著甜笑（Penny 指定的穿搭）。 |
| Luna | Luna： - 衣服要顯身材。 - 既有參考照片的身材不符合設定。 - 只能借表情／環境，不能當身材標準。 | 衣服顯身材：H 貼身緞面細肩洋裝；V 心形領有骨架的貼身洋裝；既有照片身材不符：所有 Luna 參考照片都標「不作身材參考」，身材依設定數字；只借表情／環境：參考用途只標「表情」與「場景」 | 秋日午後當代日式宅邸的庭院，藕粉秋草紋和服配深梅色腰帶，雙手在腰帶下方輕捧一個小巧的日式香袋，站在緣側旁的石板路上，身體斜側、轉頭對鏡頭甜美淺笑。 | 紫陽花盛開的町家庭院，鼠尾草綠馬甲感洋裝，正面站在石板路上。 |
| Somi | Somi：接受新版暖橘復古棚景主方向。（以上各保留為其中一款，再另設完全不同的一款。） | 接受暖橘復古棚景：H-somi-oh 沿用 v2 原文（含炸雞只在橫幅邊緣）；另一款完全不同：V 雪夜溫泉小鎮、白色針織洋裝＋紅色長大衣 | Penny 已接受的方向（R4 只改上衣穿法）：暖橘復古小吃店棚景，敞開的奶油色短開襟＋鏽橘貼身細肩小可愛＋高腰針織短裙，輕靠吧台大笑。 | 下雪的溫泉小鎮夜晚，象牙白貼身針織洋裝外披紅色長大衣，抬眼看著燈籠旁飄落的雪，自然地笑開。 |
| Coco | Coco：接受泳池主方向。（以上各保留為其中一款，再另設完全不同的一款。） | 接受泳池：V-coco-wu 沿用 v2 原文；另一款完全不同：H 初夏薰衣草花田、白色亞麻洋裝 | 初夏傍晚的薰衣草花田，白色細肩亞麻洋裝，拿著草帽大笑。 | Penny 已接受的方向：週末飯店泳池，薄荷綠比基尼＋淺紫透膚罩衫，坐在池邊大笑。 |
| Mia | Mia： - 場景、服裝全面去電競化。 - 原咖啡座替代方案太普通，兩款重新設計。 - 不放電競椅、耳機、RGB房間等職業符號。 | 全面去電競化：兩款都沒有電競椅、耳機、RGB 房間或霓虹（程式檢查）；咖啡座太普通、兩款重設：H 夏日黃昏遊樂碼頭；V 春夜櫻花步道 | 夏日黃昏的海邊遊樂碼頭，粉色緞面馬甲上衣配白色迷你裙，拿著棉花糖俏皮眨眼。 | 春夜的櫻花河岸步道，淺紫貼身露肩針織洋裝，站在花枝下甜笑。 |
| Yuna | Yuna： - 普通白色公寓不足。 - 需要更具韓系氛圍的專業寫真。 - 用服裝、妝髮、色調、場景與攝影建立韓系美感，   不靠文字標籤、國旗或隨意塞韓國地標。 | 普通白色公寓不足：兩款都不在公寓；韓系氛圍：H 通透的咖啡館（水光肌、奶油黃＋淺藍）；V 銀杏大道（毛呢短外套套裝＋長靴、柔和底片感）；不靠文字、國旗、地標：prompt 不含國旗、韓文、地名或招牌（程式檢查） | 雪後清晨的白樺林小徑，霧玫瑰粉貼身方領針織上衣＋淺灰高腰羊毛迷你裙，外披敞開的白色短版羊羔毛外套。 | 深秋的銀杏大道，奶油色毛呢短外套套裝配黑色長靴，停下腳步望向大道深處、手裡拿著一片銀杏葉。 |
| Tammy | Tammy： - 已提的合身洋裝與高跟鞋方向可保留。 - 重新安排與穿搭匹配的高級場景。 - 不是任意白牆或普通階梯。 | 保留合身洋裝＋高跟鞋：H 熱粉方領針織洋裝＋白色露跟高跟鞋；高級場景：H 精品店；V 大飯店大廳（白色西裝洋裝＋黑色細高跟）；不是白牆或普通階梯：prompt 不含階梯與白牆（程式檢查） | 春日花園露台的平整石板步道，熱粉色方領貼身針織洋裝配白色露跟高跟鞋，站在庭園長椅旁明亮地笑。 | 夜晚的大飯店大廳，白色西裝外套洋裝配素面黑色小手提包，一手拎包、一手插腰的自信笑容。 |
| Rin | Rin：採用 shoot-plan-v2 的替代方向。 先精確讀出原替代內容，不猜測或自行替換。 作為其中一款，另一款另設不同服裝與場景。 | v2 替代方向逐字讀出：「出勤前的銀座：黑色絲絨細肩帶長禮服，坐在金色燈光的吧台邊（不拿酒杯）。」→ V-rin-ayase 依原文（黑色絲絨細肩帶長禮服、金色燈光吧台、不拿酒杯）；另一款不同服裝與場景：H 夕陽飯店套房、酒紅緞面垂墜領洋裝、斜躺 | 夕陽中的高樓飯店套房，酒紅緞面垂墜領細肩長洋裝，側躺在深綠絲絨貴妃椅上望向窗外的夕陽。 | 秋日午後的安靜港灣石砌碼頭，墨綠仿麂皮裹身洋裝，倚著木頭繫船柱望向港口。 |
| Rainie | Rainie：接受頂樓夜景血紅洋裝主方向。（以上各保留為其中一款，再另設完全不同的一款。） | 接受頂樓夜景血紅洋裝：H-rainie-hsu 沿用 v2 原文；另一款完全不同：V 雨後夜街、黑色緞面繞頸洋裝＋長皮風衣 | Penny 已接受的方向：頂樓夜景，血紅緞面馬甲高衩迷你洋裝，背靠玻璃欄杆直視鏡頭。 | 雨後的夜晚街道，黑色緞面繞頸迷你洋裝外搭黑色長皮風衣，看向前方的街燈，放鬆、微啟唇的沉思神情。 |
| Miu | Miu： - 服裝要呈現設定身材，尤其胸型與腰線。 - 不再以厚重寬鬆毛衣、圍裙遮住身材。 - 性感與甜美並存，不把她只拍成咖啡店工作照。 | 呈現胸型與腰線：H 貼身緞面細肩小可愛；V V 領合身針織洋裝＋細腰帶；不用厚重寬鬆毛衣、圍裙：程式檢查不含 apron、chunky、oversized；性感與甜美並存、不是咖啡店工作照：H 一人公寓晨光；V 運河步道 | 晨光灑進的一人公寓，象牙白蕾絲緞面細肩小可愛與短褲，背靠床頭的枕頭堆自然半倚、歪頭甜笑。 | 春日度假別墅的木平台，杏桃色有骨架的細肩短洋裝，坐在白色帆布吊床邊，笑著看向開花的果樹。 |
| Jia | Jia： - 服裝與場景重新設計。 - 不運動風、不舞蹈工作照。 - 不在攝影棚拍。 - 專業攝影質感可在實景完成，不需要棚景才成立。 | 服裝與場景重設：H 美術館黑色單肩洋裝；V 玻璃溫室白色短上衣＋薄荷綠緞面開衩裙；不運動、不舞蹈、不棚拍：程式檢查不含 studio、dance、sport、sneakers；兩款都是實景 | 初秋傍晚的湖畔木平台，深酒紅合身繞頸細針織短洋裝露肩與上背，側坐在臨水長椅上、雙腿交疊望向湖面。 | 明亮的玻璃溫室，白色無袖立領短上衣配薄荷綠緞面高腰貼臀窄裙，斜側站在大葉植物之間，臀腰曲線清楚。 |
| Yerin | Yerin： - 可穿高爾夫迷你裙裝。 - 性感、可愛、漂亮是拍攝重點。 - 不打球、不收桿、不拿球桿展示球技。 - 如高爾夫形象寫真，不把她改成啦啦隊職業。 | 高爾夫迷你裙裝：H 淺藍百褶高爾夫迷你裙＋白色針織 polo＋球帽；性感、可愛、漂亮：H 坐在球車上的可愛笑容；V 日落海灘的貼身白洋裝；不打球、不收桿、不拿球桿：程式檢查不含 club、driver、swing；不改成啦啦隊：不含 cheer、pom | 春日球場的白色球車，白色無袖針織 polo＋淺藍百褶高爾夫迷你裙，坐在座椅邊緣微微後靠、伸長雙腿的俏皮笑容。 | 日落的白沙海灘，白色圓領貼身針織背心洋裝，赤腳站在淺浪邊的燦笑。 |

## 5. 橫式款 12 套總覽

| 月份（已確認） | ID | 狀態 | 主題 | 環境 | 服裝 | 色彩 | 姿態 | 表情 | 性感程度 | 攝影方法 | 景別｜身體方向｜臉與視線｜拍攝角度 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 月 | H-yuna-kim | 已接受 | 雪後清晨的白樺林小徑，霧玫瑰粉貼身方領針織上衣＋淺灰高腰羊毛迷你裙，外披敞開的白色短版羊羔毛外套。 | 雪後白樺林（戶外） | 外套：白色短版羊羔毛外套（敞開）；上身：霧玫瑰粉細羅紋貼身方領長袖針織上衣；下身：淺灰高腰羊毛迷你裙；鞋：淺灰麂皮及膝長靴（不入鏡）；配件：細銀耳環 | 雪白・灰・霧玫瑰 | 站在雪後的林間小徑上。一手拉住敞開外套的衣襟停在腰側，一手把一縷頭髮撥到耳後。 | 清淡溫柔的微笑 | 中 | 雪地反光的偏亮通透曝光＋柔光 | 大腿中段以上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視 |
| 2 月 | H-rin-ayase | 已接受 | 夕陽中的高樓飯店套房，酒紅緞面垂墜領細肩長洋裝，側躺在深綠絲絨貴妃椅上望向窗外的夕陽。 | 飯店套房（室內夕陽） | 洋裝：深酒紅真絲緞面垂墜領細肩中長洋裝；鞋：赤腳；配件：細金鍊項鍊、金色小耳針 | 酒紅・深綠・柔金 | 側躺在貴妃椅上：下方的前臂平放在椅子抬高的一端撐起上身，上方那條腿膝蓋微彎、往前搭在伸直的下方腿上。下方手的前臂撐在椅墊上，上方的手輕放在臀側的大腿上。 | 平靜、帶一點慵懶的淺笑 | 高 | 夕陽窗光＋柔光補光 | 斜躺全身｜側面斜躺（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側窗外的夕陽｜略高於她斜躺時頭部的高度・輕俯 |
| 3 月 | H-miu-shiraishi | 已接受 | 晨光灑進的一人公寓，象牙白蕾絲緞面細肩小可愛與短褲，背靠床頭的枕頭堆自然半倚、歪頭甜笑。 | 一人公寓（室內早晨） | 上身：象牙白緞面細肩小可愛（細蕾絲滾邊）；下身：同色緞面短褲；鞋：赤腳；配件：細金耳針、細金手鍊 | 象牙白・奶油・暖木 | 坐在床上、背靠床頭堆起的枕頭半倚：一膝立起、另一條腿沿著床伸直。一手手肘輕搭在立起的膝蓋上、手腕自然垂下，另一手放在身旁的床單上。 | 歪頭、帶一點慵懶的甜笑 | 高 | 紗簾晨光＋反光 | 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 |
| 4 月 | H-tammy-chou | 已接受 | 春日花園露台的平整石板步道，熱粉色方領貼身針織洋裝配白色露跟高跟鞋，站在庭園長椅旁明亮地笑。 | 春日花園露台（戶外） | 洋裝：熱粉色方領羅紋針織貼身迷你洋裝（保留 Penny 同意的方向）；鞋：白色尖頭露跟高跟鞋；配件：金色圈耳環、細金手鍊 | 熱粉・白・新綠 | 站在石板步道上、白色庭園長椅旁。一手輕扶在長椅椅背上，一手插腰。 | 明亮的笑容 | 中 | 午後春陽＋反光板 | 全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜膝蓋高度・輕仰 |
| 5 月 | H-yerin-han | 已接受 | 春日球場的白色球車，白色無袖針織 polo＋淺藍百褶高爾夫迷你裙，坐在座椅邊緣微微後靠、伸長雙腿的俏皮笑容。 | 高爾夫球場（戶外） | 上身：白色無袖貼身針織高爾夫 polo；下身：淺天空藍百褶高爾夫迷你裙；鞋：白色高爾夫鞋；配件：素面白色球帽、小金色耳針 | 亮綠・天空藍・白 | 側坐在球車前座的邊緣，身體微微往後靠。後方的手撐在臀部後方的座椅上，前方的手輕放在併攏的膝上。 | 俏皮、明亮的笑 | 中高 | 晴朗晨光＋反光板 | 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 |
| 6 月 | H-coco-wu | 已接受 | 初夏傍晚的薰衣草花田，白色細肩亞麻洋裝，拿著草帽大笑。 | 花田（戶外） | 洋裝：白色亞麻細肩洋裝，抓皺貼身上身、柔和 V 領、收腰、微蓬迷你裙；鞋：白色平底涼鞋（不入鏡）；配件：白色雛菊髮夾、腳踝細金鍊（不入鏡）、草帽（拿在手上） | 薰衣草紫・白・暖金 | 站在花壟之間。一手把草帽拿在身側，一手把頭髮塞到耳後。 | 瞇眼大笑、深酒窩 | 中 | 傍晚逆光＋反光板 | 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視 |
| 7 月 | H-mia-huang | 已接受 | 夏日黃昏的海邊遊樂碼頭，粉色緞面馬甲上衣配白色迷你裙，拿著棉花糖俏皮眨眼。 | 海邊遊樂碼頭（戶外黃昏） | 上身：粉色緞面馬甲上衣（心形領）；下身：白色高腰 A 字迷你裙；鞋：白色厚底涼鞋（不入鏡）；配件：小珍珠耳環、細銀手鍊、一支粉色棉花糖 | 棉花糖粉・薰衣草紫・柔金 | 站在木棧道上。一手插腰，一手把棉花糖拿在肩高、離開臉。 | 俏皮眨眼、挑逗的半笑 | 中 | 黃昏天光＋柔光主光 | 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視 |
| 8 月 | H-iris-chen | 已接受 | 夏日上午的淺色平坦岩岸海灣，向日葵黃有骨架的平口馬甲短上衣配同色低腰迷你裙，身體正面燦笑。 | 夏日岩岸海灣（戶外） | 上身：向日葵黃有骨架的平口馬甲短上衣（棉質府綢、細肩帶，收出胸型與腰線）；下身：同色低腰迷你裙（腰頭在肚臍下方、側邊小開衩）；鞋：白色平底繫帶涼鞋；配件：細金鍊項鍊、小金色耳針 | 向日葵黃・湖水綠・淺岩灰 | 站在平坦的岩石平台上。雙手輕放在低腰裙的腰頭兩側（胯骨上）。 | 燦爛溫暖的笑容 | 中高 | 上午斜光＋大反光板 | 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰 |
| 9 月 | H-jia-seo | 已接受 | 初秋傍晚的湖畔木平台，深酒紅合身繞頸細針織短洋裝露肩與上背，側坐在臨水長椅上、雙腿交疊望向湖面。 | 湖畔木平台（戶外） | 洋裝：深酒紅細針織繞頸合身短洋裝（露肩與上背、腰部明確收窄、裙長大腿中段；細緻針織，沒有運動元素或大型圖案）；鞋：黑色細帶低跟涼鞋；配件：小銀色圈耳環 | 深酒紅・湖水灰藍・暖金 | 側坐在湖畔長椅上，雙腿交疊。靠鏡頭的手輕放在交疊的膝上，另一手手臂搭在長椅椅背上（不遮腰線）。 | 冷靜、若有所思的淺笑 | 中 | 傍晚逆光＋反光板 | 坐姿全身｜側面（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側的湖面與遠岸｜坐姿時的腰部高度・平視 |
| 10 月 | H-luna-tanaka | 依owner指示修訂，主管覆核通過 | 秋日午後當代日式宅邸的庭院，藕粉秋草紋和服配深梅色腰帶，雙手在腰帶下方輕捧一個小巧的日式香袋，站在緣側旁的石板路上，身體斜側、轉頭對鏡頭甜美淺笑。 | 日式宅邸庭院與緣側（戶外） | 和服：低飽和藕粉色正絹和服（小紋，細緻的秋草紋；左襟壓右襟、白色半襟，正式穿法）；腰帶：深梅色名古屋帶（太鼓結），淡金色帶締、奶油色帶揚；襪履：白足袋、低跟草履；配件：耳上一支小珍珠髮夾（不加大型頭飾）；道具：小巧的日式布製香袋（掌心大小；低飽和奶油色帶淡金細緻織紋、短束口繩；不是手提包，沒有品牌、文字或誇張吊飾） | 藕粉・深梅・木色・紅葉 | 站在緣側旁的石板路上，身體斜側、臉轉向鏡頭，雙手在腰帶下方輕捧小香袋。雙手在腰帶下方、下腹前自然輕捧一個小巧的日式布製香袋；肩膀放鬆、手肘自然微彎，手腕不交叉，手指自然貼著香袋；袖子自然垂落，不遮臉，也不完全蓋住雙手與香袋，腰帶清楚可見。 | 甜美的淺笑 | 低（正式和服，不強調身體曲線） | 午後斜光＋大反光板 | 全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・平視 |
| 11 月 | H-somi-oh | 已接受 | Penny 已接受的方向（R4 只改上衣穿法）：暖橘復古小吃店棚景，敞開的奶油色短開襟＋鏽橘貼身細肩小可愛＋高腰針織短裙，輕靠吧台大笑。 | 復古小吃店棚景（棚內） | 外搭：奶油色合身羅紋針織短開襟（全部不扣、敞開，從肩上自然垂下）；上身：鏽橘色貼身羅紋方領細肩小可愛（包覆胸型）；下身：高腰鏽橘色針織迷你裙；鞋：棕色有跟皮革樂福鞋（不入鏡）；配件：紅色琺瑯小愛心耳環 | 暖橘・奶油・紅 | 站著，一側臀部輕靠磁磚吧台，重心在後腳、前腳輕交叉。一手放在吧台邊緣，一手把頭髮塞到耳後。 | 月牙眼大笑、露出酒窩 | 中高 | 暖色柔光箱棚拍 | 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜腰部高度・平視 |
| 12 月 | H-rainie-hsu | 已接受 | Penny 已接受的方向：頂樓夜景，血紅緞面馬甲高衩迷你洋裝，背靠玻璃欄杆直視鏡頭。 | 頂樓露台（戶外夜晚） | 洋裝：血紅緞面馬甲迷你洋裝（大腿高衩）；鞋：黑色細帶高跟涼鞋（不入鏡）；配件：大型銀色垂墜耳環、細銀手環 | 血紅・黑・銀・深藍 | 背靠玻璃欄杆，一腳從高衩往前。雙手放在身後的欄杆上；不拿任何杯子。 | 自信又帶點壞的笑 | 高 | 夜景柔光箱主光＋城市散景 | 膝上｜正面｜臉正面・看鏡頭｜腰部高度・平視 |

## 6. 直式款 12 套總覽

| 月份（已確認） | ID | 狀態 | 主題 | 環境 | 服裝 | 色彩 | 姿態 | 表情 | 性感程度 | 攝影方法 | 景別｜身體方向｜臉與視線｜拍攝角度 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 月 | V-tammy-chou | 已接受 | 夜晚的大飯店大廳，白色西裝外套洋裝配素面黑色小手提包，一手拎包、一手插腰的自信笑容。 | 飯店大廳（室內夜晚） | 洋裝：白色合身西裝外套式迷你洋裝（深 V 翻領、金色扣子、繫腰帶）；鞋：黑色尖頭細高跟鞋（不入鏡）；配件：金色垂墜耳環、素面黑色亮面小手提包（無任何標誌、不仿特定品牌） | 白・金・暖大理石 | 站在大理石柱旁。一手拎著小手提包的短提把、包停在臀側稍微離開身體，另一手插腰。 | 自信的笑容 | 中 | 吊燈環境光＋柔光主光 | 大腿中段以上｜正面｜臉正面・看鏡頭｜腰部高度・輕仰 |
| 2 月 | V-jia-seo | 已接受 | 明亮的玻璃溫室，白色無袖立領短上衣配薄荷綠緞面高腰貼臀窄裙，斜側站在大葉植物之間，臀腰曲線清楚。 | 玻璃溫室（室內實景） | 上身：白色無袖立領貼身短上衣（露腰）；下身：薄荷鼠尾草綠緞面高腰窄裙（腰頭在肚臍上方、貼著臀線往膝下收窄、左前側開衩到大腿中段）；鞋：白色細帶涼鞋；配件：細銀耳針 | 白・薄荷・深綠 | 站在植物之間的石板路上，斜側站著、臀部隨重心往後側。一手插在高腰裙的腰頭上，一手輕觸身旁的大片龜背芋葉。 | 冷靜柔和的微笑 | 中 | 溫室漫射天光＋柔光 | 全身｜約45度斜側（朝畫面右）｜臉正面・看鏡頭｜臀部高度・平視 |
| 3 月 | V-mia-huang | 已接受 | 春夜的櫻花河岸步道，淺紫貼身露肩針織洋裝，站在花枝下甜笑。 | 櫻花河岸（戶外夜晚） | 洋裝：淺紫細針織貼身露肩迷你洋裝；鞋：白色及膝長靴（不入鏡）；配件：一側小珍珠髮夾、細銀耳環 | 粉櫻・淺紫・夜藍 | 站在低垂的花枝下。一手輕觸肩旁的花枝，另一手自然垂下、不入鏡。 | 甜甜的微笑 | 中 | 夜景柔光主光＋燈籠 | 胸上｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜眼睛高度・輕俯 |
| 4 月 | V-miu-shiraishi | 已接受 | 春日度假別墅的木平台，杏桃色有骨架的細肩短洋裝，坐在白色帆布吊床邊，笑著看向開花的果樹。 | 度假別墅木平台（戶外） | 洋裝：杏桃色棉緞細肩短洋裝（有骨架的貼身上身、心形領、收腰、裙長大腿中段微蓬）；鞋：白色細帶平底涼鞋；配件：小珍珠耳環 | 杏桃・白花・新綠 | 側坐在白色帆布吊床的邊緣，雙腳踩在木平台上，上身微微前傾。雙手抓著身旁吊床的布邊（在臀側，不遮胸腰）。 | 開心、自然的笑 | 中 | 春日柔光＋反光板 | 坐姿全身｜約30度斜側（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側開滿白花的果樹｜坐姿時的腰部高度・平視 |
| 5 月 | V-rainie-hsu | 已接受 | 雨後的夜晚街道，黑色緞面繞頸迷你洋裝外搭黑色長皮風衣，看向前方的街燈，放鬆、微啟唇的沉思神情。 | 雨後夜街（戶外夜晚） | 洋裝：黑色緞面繞頸迷你洋裝；外套：黑色長版皮革風衣（敞開）；鞋：黑色細跟尖頭短靴（不入鏡）；配件：大型銀色垂墜耳環 | 黑・銀・深藍・琥珀 | 站在濕亮的人行道上，看向前方的街燈。一手拉著敞開的風衣衣襟在腰間，一手自然垂在大腿旁。 | 放鬆、微啟唇、帶點沉思 | 中高 | 夜景柔光主光＋濕路面倒影 | 膝上｜約30度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側前方的街燈｜腰部高度・平視 |
| 6 月 | V-luna-tanaka | 已接受 | 紫陽花盛開的町家庭院，鼠尾草綠馬甲感洋裝，正面站在石板路上。 | 町家庭院（戶外） | 洋裝：淺鼠尾草綠棉質洋裝，心形領、有骨架的貼身上身、微蓬迷你裙；鞋：米色低跟繫帶涼鞋；配件：細金手鍊 | 鼠尾草綠・白・青苔綠 | 站在石板小徑上。雙手輕輕交握在身後。 | 溫柔的微笑 | 中 | 陰天柔光＋反光板 | 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰 |
| 7 月 | V-coco-wu | 已接受 | Penny 已接受的方向：週末飯店泳池，薄荷綠比基尼＋淺紫透膚罩衫，坐在池邊大笑。 | 飯店泳池（戶外） | 泳裝：薄荷綠羅紋三角比基尼上衣與同色側綁下著（完整遮蔽）；外搭：敞開的淺紫透膚短袖罩衫（落在肩後）；配件：白色雛菊髮夾、腳踝細金鍊（不入鏡） | 薄荷綠・淺紫・湖水綠 | 坐在池邊、兩條小腿泡在水裡，身體往後。雙手撐在身後地上。 | 歪頭、瞇眼大笑、酒窩 | 高 | 晴天高光＋反光板 | 坐姿到水面｜正面｜臉正面・看鏡頭｜坐姿時的胸口高度・平視 |
| 8 月 | V-yerin-han | 已接受 | 日落的白沙海灘，白色圓領貼身針織背心洋裝，赤腳站在淺浪邊的燦笑。 | 海灘夕陽（戶外） | 洋裝：白色圓領羅紋貼身背心迷你洋裝；鞋：赤腳（不入鏡）；配件：小金色圈耳環、腳踝細金鍊（不入鏡） | 暖金・蜜桃・白・淡藍 | 站在淺浪邊。一手輕放在鎖骨，一手自然垂放。 | 大方燦爛的笑 | 中 | 夕陽逆光＋反光板 | 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・輕仰 |
| 9 月 | V-iris-chen | 已接受 | 黃金時段的河濱草地，白色方領短上衣配牛仔迷你裙，正面站著甜笑（Penny 指定的穿搭）。 | 河濱草地（戶外） | 上身：白色貼身羅紋方領短袖短上衣（露腰）；下身：淺藍高腰牛仔迷你裙；鞋：白色低筒帆布鞋（不入鏡）；配件：小金色圈耳環 | 米白・淺牛仔藍・暖金 | 站在草地上。一手插腰，一手輕碰太陽穴旁的頭髮。 | 明亮溫暖的笑 | 中 | 黃金時段逆光＋反光板 | 大腿中段以上｜正面｜臉正面・看鏡頭｜胸口高度・平視 |
| 10 月 | V-rin-ayase | 已接受 | 秋日午後的安靜港灣石砌碼頭，墨綠仿麂皮裹身洋裝，倚著木頭繫船柱望向港口。 | 秋日港灣碼頭（戶外） | 洋裝：深墨綠仿麂皮裹身洋裝（深 V 領、繫帶收腰、及膝、前側開衩到大腿中段）；鞋：深棕色尖頭短跟踝靴（不入鏡）；配件：細金耳環、細金手鍊 | 墨綠・銀灰・帆白・柔金 | 背靠粗木繫船柱、斜側站著，一膝微彎、腳尖點地。一手往後輕扶在繫船柱上，一手輕放在腰間的繫帶上。 | 平靜、帶點距離感的淺笑 | 中高 | 陰天柔光＋反光板 | 膝上｜約45度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側港口的出口與海面｜腰部高度・平視 |
| 11 月 | V-yuna-kim | 已接受 | 深秋的銀杏大道，奶油色毛呢短外套套裝配黑色長靴，停下腳步望向大道深處、手裡拿著一片銀杏葉。 | 銀杏大道（戶外） | 上身：奶油色毛呢短外套（無領、扣起、合身）；下身：同色高腰毛呢迷你裙；鞋：黑色及膝皮長靴；配件：小珍珠耳環、小黑色肩背包 | 銀杏金黃・奶油・黑 | 站在落葉人行道上，停下腳步望向大道深處。一手拉著肩上的包包背帶，另一手指尖輕拿一片銀杏葉停在腰側。 | 柔和、若有所思的微笑 | 低中 | 午後逆光＋反光板 | 全身｜約30度斜側（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側銀杏大道的深處｜臀部高度・平視 |
| 12 月 | V-somi-oh | 已接受 | 下雪的溫泉小鎮夜晚，象牙白貼身針織洋裝外披紅色長大衣，抬眼看著燈籠旁飄落的雪，自然地笑開。 | 溫泉小鎮雪夜（戶外） | 洋裝：象牙白貼身羅紋針織迷你洋裝（高圓領）；外套：紅色羊毛長大衣（敞開）；鞋：白色及膝長靴；配件：小珍珠耳環 | 紅・象牙白・燈籠琥珀・雪夜藍 | 站在雪地上，抬眼看向燈籠旁飄落的雪。一手插在大衣口袋裡把大衣撐開，另一手在肩高攤開掌心接雪（不遮臉）。 | 自然、帶點驚喜的笑，眼睛睜開 | 低中 | 夜景暖色主光＋燈籠 | 全身｜正面｜三分之二側臉・不看鏡頭：看畫面右上方燈籠旁飄落的雪｜臀部高度・平視 |

## 7. 兩本月份（已確認）

| 月份 | 橫式款 | 理由 | 直式款 | 理由 |
|---|---|---|---|---|
| 1 月 | H-yuna-kim（Yuna） | 雪後清晨的白樺林，用雪白與霧玫瑰的冬日寫真開場 | V-tammy-chou（Tammy） | 新年的大飯店大廳，白金色開場 |
| 2 月 | H-rin-ayase（Rin） | 夕陽套房的酒紅緞面，冬季的溫暖華麗 | V-jia-seo（Jia） | 冬末溫室的新綠 |
| 3 月 | H-miu-shiraishi（Miu） | 早春晨光的一人公寓 | V-mia-huang（Mia） | 春夜櫻花 |
| 4 月 | H-tammy-chou（Tammy） | 春日花園露台的熱粉洋裝 | V-miu-shiraishi（Miu） | 春日別墅木平台與開滿白花的果樹 |
| 5 月 | H-yerin-han（Yerin） | 春日球場的清新綠 | V-rainie-hsu（Rainie） | 梅雨季的雨後夜街 |
| 6 月 | H-coco-wu（Coco） | 初夏薰衣草花田 | V-luna-tanaka（Luna） | 紫陽花季的庭院 |
| 7 月 | H-mia-huang（Mia） | 盛夏黃昏的遊樂碼頭 | V-coco-wu（Coco） | 盛夏泳池 |
| 8 月 | H-iris-chen（Iris） | 盛夏上午的岩岸海灣與向日葵黃 | V-yerin-han（Yerin） | 夏日夕陽海灘 |
| 9 月 | H-jia-seo（Jia） | 初秋傍晚湖畔的深酒紅細針織 | V-iris-chen（Iris） | 夏末黃金時段草地 |
| 10 月 | H-luna-tanaka（Luna） | 秋日午後日式宅邸庭院的藕粉和服 | V-rin-ayase（Rin） | 秋日午後的安靜港灣 |
| 11 月 | H-somi-oh（Somi） | 晚秋的暖橘棚景 | V-yuna-kim（Yuna） | 深秋銀杏大道 |
| 12 月 | H-rainie-hsu（Rainie） | 年末頂樓夜景的派對感收尾 | V-somi-oh（Somi） | 冬天下雪的溫泉小鎮 |

- 月份人選排序已確認（R4 owner 紀錄，R6、R7 維持），不再請 Penny 重新核准；服裝與場景配合既定月份。
- 每本 12 位各出現一次；同一月份兩本是不同的人。
- 既有碰撞配對（Miu–Jia、Miu–Somi、Jia–Somi、Yerin–Rin）與 R2 目視相似（Somi–Tammy、Iris–Rainie）：不放同一月份，也不放在同一本的相鄰月份。這不是同框規則（每頁只有一人），只是避免翻頁時直接並排比較。
- 先看季節（花田、紫陽花、櫻花、銀杏、雪景、海灘、泳池這些有季節的場景放在對的月份），再讓前後月份的色調交替；不為了季節改動已接受的企劃。

## 8. 24 套企劃

### 8.1 H-iris-chen｜Iris｜橫式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 夏日上午的淺色平坦岩岸海灣，向日葵黃有骨架的平口馬甲短上衣配同色低腰迷你裙，身體正面燦笑。

**攝影：** 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到涼鞋完整；馬甲短上衣、露出的腰、低腰迷你裙、雙腿與白色平底涼鞋；放在腰頭兩側的雙手 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to sandals, the structured bustier top, her bare waist, the low-rise mini skirt, her legs and the flat white sandals, both hands resting at the waistband on her hips |
| 3. 身體朝向 | 正面：站在平坦的岩石平台上，重心在左腳、右膝微彎；身體正對鏡頭，肩線放平放鬆，臀部隨重心微微偏移 | standing on the flat rock shelf with her weight on her left leg and her right knee softly bent, her body square to the camera, shoulders level and relaxed, her hips shifted slightly with her weight |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她膝蓋高度，輕仰（參考：50mm 鏡頭、約 4.8 公尺；畫面中心與相機高度差換算俯仰約 +4.4 度） | camera at her knee height, tilted slightly upward |
| 6. 畫面配置 | 人物略偏左（約四成）；海灣與遠處岬角在右側，海平線壓低在她膝蓋後方，上方是乾淨的藍天；人物佔畫面高度約八成四，不被海景縮小 | she stands slightly left of centre, the bay and a distant headland on the right, the horizon low behind her knees and clean blue sky above her |
| 7. 攝影目的 | 正面全身展示馬甲短上衣與低腰裙勾出的胸、腰、臀線與腿長；燦笑清楚 | the full figure from the front shows the chest, waist and hip lines drawn by the bustier top and low-rise skirt, and her long legs, with her smile clear |

**選擇理由：** Iris 依 Penny 要求身體正面、有笑容；橫式用全身＋膝蓋高度輕仰拉長腿，直式是大腿中段以上＋胸口高度，景別與相機高度都不同。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 全面換掉紅磚騎樓與米杏針織套裝：改成夏日上午的淺色平坦岩岸海灣、向日葵黃有骨架的平口馬甲短上衣＋同色低腰迷你裙；身體正面、笑容不變；手改成雙手放在低腰裙腰頭兩側；相機改為膝蓋高度輕仰。

| 項目 | 內容 |
|---|---|
| 場景 | 夏天上午的海灣：一大片平坦、乾燥的淺色岩石平台，前方是透明的湖水綠海灣與遠處的綠色岬角，晴朗藍天；站位在平台中央、離水邊有距離，岩岸上沒有其他人。 |
| 服裝 | 上身：向日葵黃有骨架的平口馬甲短上衣（棉質府綢、細肩帶，收出胸型與腰線）；下身：同色低腰迷你裙（腰頭在肚臍下方、側邊小開衩）；鞋：白色平底繫帶涼鞋；配件：細金鍊項鍊、小金色耳針 |
| 髮型 | 黑色柔順直髮自然垂放過肩。 |
| 妝感 | 清透的日常妝、自然唇色、帶光澤的肌膚。 |
| 身材設定（數字） | 162 cm／87-58-90／D |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 有骨架的平口馬甲收出 D 罩杯胸型與細腰；低腰迷你裙露出腰線到胯骨，呈現腰臀比與腿長。 |
| 主光 | 左前上方晴朗的上午陽光（偏斜、不是正午頂光） |
| 補光 | 畫面外大白色反光板，柔化臉上與身上的陰影 |
| 姿態 | 站在平坦的岩石平台上。 |
| 手的位置 | 雙手輕放在低腰裙的腰頭兩側（胯骨上）。 |
| 表情 | 燦爛溫暖的笑容 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，50mm，約 4.8 公尺，視野 3.46×1.94 公尺；人物約佔畫面高度 84%（規劃）；相機約 0.46 公尺高、畫面中心約 0.84 公尺高，俯仰約 +4.4 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 9%（套框後理論約 7.6%）；下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%）；不能切：髮頂、臉、入鏡的雙手、雙腳與鞋；規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | 她是台北的日常生活者，夏天就去海邊：亮黃與湖水綠讓她的甜美與身材都更外放；身體正面、有笑容是 Penny 的要求。 |
| 與同一人另一款的差異 | 直式款是河濱草地、白色方領短上衣＋牛仔迷你裙、黃金時段逆光；這款是夏日上午的岩岸海灣、向日葵黃馬甲套裝、正面全身。與 Coco 泳池（比基尼、坐池邊）、Yerin 夕陽沙灘（白色背心洋裝）的時間、地面與服裝都不同；與 7 月 Mia 的粉色緞面馬甲（黃昏碼頭、眨眼、大腿以上）用顏色、材質、時間與景別拉開。 |
| 參考照片（用途） | iris-01：身分（認臉與甜笑；服裝不同）；iris-12：表情（開心的笑） |
| 月份（已確認） | 8 月（盛夏） |

| 風險 | 處理 |
|---|---|
| 岩石邊緣的危險站位 | 寫明站在平坦乾燥的岩石平台中央、離水邊有距離，不安排攀爬 |
| 正午頂光讓眼窩陰影重 | 寫上午偏斜的陽光＋大反光板 |
| 低腰裙遮蔽不明 | 寫明腰頭在肚臍下、裙長到大腿上段，完整遮蔽 |
| 海面反光讓臉發灰 | 反光板補光、測光給臉 |

prompt 草稿（16:9，尚未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a round sweet face with large bright double-eyelid eyes and full lips, black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, a full chest, a slim waist and rounded hips. Fresh, light everyday makeup with a natural lip colour and softly glowing skin. She wears a sunflower-yellow structured cotton bustier crop top with thin straps and light boning that shapes her chest and narrow waist, a matching low-rise mini skirt sitting below her navel with a small side slit, flat white strappy sandals, a thin gold chain necklace and small gold stud earrings. Setting: a summer bay in the late morning, a wide, flat and dry pale rock shelf well back from the water, clear turquoise water and a distant green headland, a clean blue sky, the shore empty. Both hands rest lightly on her hips at the low waistband of the skirt; she smiles brightly and warmly. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to sandals, the structured bustier top, her bare waist, the low-rise mini skirt, her legs and the flat white sandals, both hands resting at the waistband on her hips. Body: standing on the flat rock shelf with her weight on her left leg and her right knee softly bent, her body square to the camera, shoulders level and relaxed, her hips shifted slightly with her weight. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 4.8 metres, camera at her knee height, tilted slightly upward, natural perspective without distortion; she fills about 84% of the frame height. Composition: she stands slightly left of centre, the bay and a distant headland on the right, the horizon low behind her knees and clean blue sky above her. Emphasis: the full figure from the front shows the chest, waist and hip lines drawn by the bustier top and low-rise skirt, and her long legs, with her smile clear. Lighting: bright late-morning sun from high front-left, not overhead; a large white reflector just out of frame softens the shadows on her face and body; sunny yellow, turquoise and pale stone tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.2 H-luna-tanaka｜Luna｜橫式款（新企劃｜依owner指示修訂，主管覆核通過）

**一句話：** 秋日午後當代日式宅邸的庭院，藕粉秋草紋和服配深梅色腰帶，雙手在腰帶下方輕捧一個小巧的日式香袋，站在緣側旁的石板路上，身體斜側、轉頭對鏡頭甜美淺笑。

**攝影：** 全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到草履完整；藕粉秋草紋和服、深梅色腰帶與帶締、白足袋與草履；雙手在腰帶下方輕捧的小香袋，腰帶露出，袖子不遮臉、也不完全蓋住雙手與香袋 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to her zori sandals, the dusty-pink kimono with its small autumn-grass pattern, the deep plum obi and its cord, the white tabi socks and zori, both hands just below the obi holding the small sachet, the obi left clear above them, her sleeves clear of her face, her hands and the sachet |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：站在石板步道上，重心在後腳、前腳微微向前；身體朝畫面左轉約30度，肩線放鬆、背脊挺直，腰帶位置清楚 | standing on the stone path with her weight on her back foot and her front foot slightly forward, her body turned about 30 degrees toward camera-left, her shoulders relaxed and her back straight, the line of the obi clear |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她臀部高度，平視（參考：50mm 鏡頭、約 4.6 公尺；畫面中心與相機高度差換算俯仰約 -0.3 度） | camera at her hip height, level |
| 6. 畫面配置 | 人物在右側約六成處；她身後左側是木造緣側與敞開的拉門、看得到整潔的和室，右上角是一棵紅葉；建築只作背景，人物佔畫面高度約八成四 | she stands right of centre on the stone path, the wooden veranda and the open shoji with the clean tatami room behind her on the left, a red maple at the upper-right edge, the building kept as a backdrop |
| 7. 攝影目的 | 站姿全身呈現完整的和服、腰帶位置與身形比例；雙手在腰帶下方輕捧小香袋，典雅端莊；身體斜側帶出線條，臉轉向鏡頭的甜美淺笑 | the full standing figure shows the whole kimono, where the obi sits and her proportions, both hands holding the small sachet below the obi for a graceful, elegant air, the oblique stance adding shape while her face turns to the camera with a sweet smile |

**選擇理由：** 依 Penny 指示改為站在室外的和服寫真：站姿全身讓和服與腰帶完整；身體約30度斜側、臉轉向鏡頭，扭轉約30度；相機在臀部高度平視（直式款是膝蓋高度輕仰），不讓建築壓過人物。

**R7 改了什麼：** 依 Penny 指定（R7）：只把手部由「一手輕扶腰帶側邊、一手自然放下」改為雙手在腰帶下方、下腹前輕捧一個小巧的日式布製香袋（低飽和奶油色帶淡金細緻織紋、短束口繩）；肩膀放鬆、手肘微彎、手腕不交叉，袖子不遮臉、不完全蓋住雙手與香袋，腰帶清楚可見。和服、庭院、月份、表情、身體方向與相機設定都不變。

**R6 改了什麼（歷史）：** 依 Penny 指示：由室內旅宿的緞面斜坐，改為站在當代日式宅邸庭院（緣側旁石板路）的和服寫真；背景透過敞開的拉門看得到整潔嶄新的和室；服裝改為低飽和藕粉秋草紋正式和服＋深梅色名古屋帶、白足袋與草履；姿勢改為站姿全身、約30度斜側、臉轉向鏡頭甜美淺笑，一手輕扶腰帶側邊、一手自然放下；相機改為臀部高度平視。

**R4 改了什麼（歷史）：** 房間改成新穎整潔的當代日式旅宿（新榻榻米、乾淨木作、白色寢具），不再是古舊和室；服裝改為香檳色斜裁緞面細肩洋裝（仍是貼身緞面方向）；姿勢由端正側坐、雙手放腿上改為單手撐地的慵懶斜坐；視線看窗外紅葉。

| 項目 | 內容 |
|---|---|
| 場景 | 當代日式宅邸的庭院，秋天午後：她站在室外的石板步道上，身旁是寬敞的木造緣側，敞開的紙拉門後看得到整潔嶄新的和室（新榻榻米、乾淨淺色木作）；庭院鋪白砂、幾株修剪整齊的松，畫面邊緣一棵紅葉、石板上幾片落葉；建築新穎整潔、不是古舊老宅，庭院裡沒有其他人。 |
| 服裝 | 和服：低飽和藕粉色正絹和服（小紋，細緻的秋草紋；左襟壓右襟、白色半襟，正式穿法）；腰帶：深梅色名古屋帶（太鼓結），淡金色帶締、奶油色帶揚；襪履：白足袋、低跟草履；配件：耳上一支小珍珠髮夾（不加大型頭飾）；道具：小巧的日式布製香袋（掌心大小；低飽和奶油色帶淡金細緻織紋、短束口繩；不是手提包，沒有品牌、文字或誇張吊飾） |
| 髮型 | 黑色細直髮，中分下巴長度的鮑伯，梳理整齊、一側以小珍珠髮夾固定（依人設的鮑伯長度，不改成盤髮）。 |
| 妝感 | 柔和自然妝、玫瑰色唇、微微的光澤肌。 |
| 身材設定（數字） | 155 cm／88-56-87／E（童顏與曲線的反差） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 傳統和服不強調貼身曲線：用腰帶位置收出腰線，身體約30度斜側與自然站姿呈現嬌小、勻稱的比例（身材設定數字不變；不要求和服同時呈現胸腰曲線）。 |
| 主光 | 畫面左前方秋天午後偏斜的柔和陽光 |
| 補光 | 畫面外右前方大反光板，臉均勻清楚 |
| 姿態 | 站在緣側旁的石板路上，身體斜側、臉轉向鏡頭，雙手在腰帶下方輕捧小香袋。 |
| 手的位置 | 雙手在腰帶下方、下腹前自然輕捧一個小巧的日式布製香袋；肩膀放鬆、手肘自然微彎，手腕不交叉，手指自然貼著香袋；袖子自然垂落，不遮臉，也不完全蓋住雙手與香袋，腰帶清楚可見。 |
| 表情 | 甜美的淺笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，50mm，約 4.6 公尺，視野 3.31×1.86 公尺；人物約佔畫面高度 84%（規劃）；相機約 0.83 公尺高、畫面中心約 0.8 公尺高，俯仰約 -0.3 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 9%（套框後理論約 7.1%）；下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%）；不能切：髮頂、臉、入鏡的雙手、雙腳與鞋；規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | 依 Penny 指示：她是「住在美麗白日夢裡的人」，秋天的日式庭院、看得到和室的建築與正式和服，讓 Luna 的日式氣質最完整；人物站在室外，建築與紅葉只是陪襯。R7 依 Penny 指定：雙手輕捧一個日式小香袋，增加典雅氣質。 |
| 與同一人另一款的差異 | 直式款是初夏京都老町家後院、白色紫陽花與木籬笆、鼠尾草綠馬甲洋裝、正面站姿、膝蓋高度輕仰；這款是秋天的當代日式宅邸庭院、緣側與敞開拉門後的和室、藕粉和服、約30度斜側、臀部高度平視。兩款都在日式庭院，所以用季節、建築新舊、服裝（和服對西式洋裝）、身體方向與相機高度拉開。 |
| 參考照片（用途） | luna-03：服裝材質（既有照片是夏季祭典浴衣（淺藍棉質＋深藍腰帶），不是本套的秋季正式和服；只參考她穿日式服裝、繫腰帶時的整體比例與笑容；浴衣、顏色、蘋果與神社街景都不採用；沒有正式和服的參考圖；也沒有香袋的參考圖（R7 香袋外觀只靠文字）；不作身材參考：既有照片的身材不符合設定（Penny））；luna-12：表情（甜美的淺笑與鮑伯髮型；街景與服裝不採用；不作身材參考：既有照片的身材不符合設定（Penny）） |
| 月份（已確認） | 10 月（秋） |

| 風險 | 處理 |
|---|---|
| 和服穿法錯誤（右襟壓左、浴衣化、露胸改造、花魁裝） | 寫明正式和服、左襟壓右襟、白色半襟、名古屋帶太鼓結；不寫浴衣、花魁或改造 |
| 大型頭飾或花紋搶臉 | 只用小珍珠髮夾；花紋是細小、低飽和的秋草紋 |
| 建築與紅葉搶戲、人物變小 | 人物佔畫面高度約八成四；建築在背景，紅葉只在畫面邊緣 |
| 和室或建築顯得古舊 | 寫明當代宅邸、嶄新榻榻米、乾淨木作 |
| 童顏顯小 | 寫明 adult、正式穿法與成熟配色 |
| 沒有和服參考圖 | 既有照片只有夏季浴衣（luna-03），只參考比例與笑容；和服細節靠文字，生成後逐項檢查衣襟、腰帶與襪履 |
| 香袋畫成手提包、太大，或出現品牌、文字、誇張吊飾 | 寫明掌心大小的布製香袋、短束口繩、without any logos；生成後檢查大小與表面 |
| 雙手或手指錯誤（手指數量、交纏、手腕交叉） | 寫明雙手輕捧、手肘微彎、手腕不交叉；生成後逐指檢查 |
| 手或袖子遮住腰帶，香袋被袖子蓋住 | 寫明雙手在腰帶下方、腰帶露出、袖子自然垂落、不完全蓋住雙手與香袋 |
| 沒有香袋參考圖 | 既有照片都沒有香袋；外觀只靠文字，生成後檢查顏色、大小、束口繩與手的接觸 |

prompt 草稿（16:9，尚未執行）：

```text
A 20-year-old adult Japanese woman with her natural fair skin tone, large round dark-brown eyes and soft natural makeup with a rosy lip, black fine straight hair in a centre-parted, chin-length bob. Petite figure with a noticeably full chest and a slim waist, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup. She wears a properly dressed silk kimono in a soft, muted dusty lotus-pink with a fine, small autumn-grass pattern, the left side wrapped over the right with a neat white under-collar, a deep plum Nagoya obi tied in a neat drum knot with a pale-gold obijime cord and a cream obiage, white tabi socks and low zori sandals, and a small pearl hair pin above one ear. Setting: the stone-paved garden path of a contemporary Japanese residence on an autumn afternoon, a wide wooden engawa veranda beside her and open sliding shoji doors revealing a clean, new tatami room with crisp light-wood details, raked white gravel and a few neatly pruned pines, one maple with red leaves at the edge of the frame and a few red leaves on the stones, everything new and well kept, nobody else in the garden. Both hands rest together just below her obi in front of her lower abdomen, lightly holding a small, palm-sized Japanese fabric sachet in soft cream with a fine pale-gold woven texture and a short drawstring cord, plain and without any logos; her shoulders are relaxed, her elbows softly bent and her wrists uncrossed, her fingers resting naturally on the sachet, her sleeves falling naturally; she gives a sweet, gentle smile. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to her zori sandals, the dusty-pink kimono with its small autumn-grass pattern, the deep plum obi and its cord, the white tabi socks and zori, both hands just below the obi holding the small sachet, the obi left clear above them, her sleeves clear of her face, her hands and the sachet. Body: standing on the stone path with her weight on her back foot and her front foot slightly forward, her body turned about 30 degrees toward camera-left, her shoulders relaxed and her back straight, the line of the obi clear. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 4.6 metres, camera at her hip height, level, natural perspective without distortion; she fills about 84% of the frame height. Composition: she stands right of centre on the stone path, the wooden veranda and the open shoji with the clean tatami room behind her on the left, a red maple at the upper-right edge, the building kept as a backdrop. Emphasis: the full standing figure shows the whole kimono, where the obi sits and her proportions, both hands holding the small sachet below the obi for a graceful, elegant air, the oblique stance adding shape while her face turns to the camera with a sweet smile. Lighting: soft, slanting autumn afternoon sun from front-left, a large white reflector just out of frame on the right keeping her face soft and clear; muted lotus pink, plum, warm wood and a few maple reds against white gravel, with a gentle film-like finish. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.3 H-somi-oh｜Somi｜橫式款（Penny 已接受的 v2 主方向｜已接受（R6 owner 紀錄））

**一句話：** Penny 已接受的方向（R4 只改上衣穿法）：暖橘復古小吃店棚景，敞開的奶油色短開襟＋鏽橘貼身細肩小可愛＋高腰針織短裙，輕靠吧台大笑。

**攝影：** 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：敞開的短開襟框住小可愛下的胸型、腰線、高腰針織迷你裙與交叉的雙腿到膝蓋下方；扶吧台的手與塞頭髮的手 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the open cardigan framing the camisole over her chest, her waistline, the high-waisted knit mini skirt and her crossed legs down to just below the knees, one hand on the counter and the other at her ear |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：站姿，左側臀部輕靠在畫面右側的吧台上，身體朝畫面左轉約30度；重心在後腳、前腳輕輕交叉，肩線放鬆 | standing with her hip leaning on the counter on camera-right, her body turned about 30 degrees toward camera-left, weight on her back leg with the front leg crossed, shoulders relaxed |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她腰部高度，平視（參考：70mm 鏡頭、約 4.6 公尺；畫面中心與相機高度差換算俯仰約 +0.7 度） | camera at her waist height, level |
| 6. 畫面配置 | 人物偏左；暖橘吧台與紅色高腳椅往右延伸，一小盤失焦的炸雞在右緣（已接受的構圖） | left of centre with the orange counter running to the right and a small plate of golden fried chicken resting soft and out of focus at the right edge |
| 7. 攝影目的 | 斜側倚靠讓腰臀曲線與交叉的腿更明顯，敞開的開襟露出胸型；臉正對鏡頭保留月牙眼大笑 | the oblique lean shows her waist-to-hip curve and crossed legs, the open cardigan shows her chest line, and her face stays toward the camera for the crescent-eyed laugh |

**選擇理由：** 已接受方向：場景、光線、姿勢、取景與「人物偏左、吧台往右、炸雞在右緣」都照 v4；只改上衣的穿法與入鏡描述。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 短開襟不再全扣：改成「敞開的奶油色短開襟（全部不扣、從肩上垂下）＋鏽橘貼身方領細肩小可愛」兩層，衣物結構寫明；場景、光線、姿勢、大笑與構圖照 v4，不新增吃東西的動作。

| 項目 | 內容 |
|---|---|
| 場景 | 搭景的韓式復古小吃店：暖橘色磁磚吧台、一排紅色皮面高腳椅、一盞暖色吊燈；橫幅右緣有一小盤失焦的炸雞。 |
| 服裝 | 外搭：奶油色合身羅紋針織短開襟（全部不扣、敞開，從肩上自然垂下）；上身：鏽橘色貼身羅紋方領細肩小可愛（包覆胸型）；下身：高腰鏽橘色針織迷你裙；鞋：棕色有跟皮革樂福鞋（不入鏡）；配件：紅色琺瑯小愛心耳環 |
| 髮型 | 明亮蜜橘棕的韓式狼尾層次剪。 |
| 妝感 | 淡妝、亮澤唇釉。 |
| 身材設定（數字） | 161 cm／91-58-90／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 敞開的短開襟在兩側框住貼身小可愛，清楚呈現 F 罩杯胸型與腰線；高腰短裙與交叉的腿呈現腰臀比。 |
| 主光 | 前右方頭部高度的大型暖色柔光箱 |
| 補光 | 畫面外左側柔光；吊燈在頭髮上加暖光 |
| 姿態 | 站著，一側臀部輕靠磁磚吧台，重心在後腳、前腳輕交叉。 |
| 手的位置 | 一手放在吧台邊緣，一手把頭髮塞到耳後。 |
| 表情 | 月牙眼大笑、露出酒窩 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，70mm，約 4.6 公尺，視野 2.37×1.33 公尺；頭頂上方留白約 8%（規劃）；相機約 1.03 公尺高、畫面中心約 1.08 公尺高，俯仰約 +0.7 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 8%（套框後理論約 6.4%）；下緣：規劃裁切線在膝蓋下方的小腿上段（套框後理論上往上移約 2 cm）；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。膝上的下緣套框後理論上會略往上移；若實圖接近膝蓋，4 mm 改由頭頂留白多裁（後製裁切位置，不改拍攝方向）。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | Penny 接受的 v2 主方向；R4 只把「全扣的短開襟」改成明確的兩層穿法，讓胸型露出來。場景、光線、姿勢與大笑都照舊，不新增吃東西的動作。 |
| 與同一人另一款的差異 | 直式款在雪夜溫泉小鎮、象牙白針織洋裝＋紅色長大衣、抬眼看雪；這款是棚內暖橘、敞開短開襟＋小可愛＋短裙、對鏡頭大笑。 |
| 參考照片（用途） | somi-02：表情（Penny 喜歡的笑容與暖色調）；somi-01：身分（認臉） |
| 月份（已確認） | 11 月（秋） |

| 風險 | 處理 |
|---|---|
| 開襟與小可愛層次被畫錯或又扣起 | prompt 寫明兩層、開襟全部不扣、從肩上垂下 |
| 炸雞搶戲或出現包裝假字 | 只在橫幅右緣、失焦、放在盤子上，不新增吃東西的動作 |
| 棚景雜物多 | 寫明整齊 |

prompt 草稿（16:9，尚未執行）：

```text
A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. Light makeup with a glossy lip. She wears a fitted cream rib-knit cropped cardigan worn fully unbuttoned and open, hanging from her shoulders over a fitted rust-orange ribbed square-neck camisole with thin straps that follows her full chest, a high-waisted rust-orange knit mini skirt and small red enamel heart earrings. Setting: a studio-built retro Korean snack-bar set with a warm orange tiled counter, a row of red vinyl bar stools and a warm pendant lamp, everything tidy. She stands leaning one hip lightly against the tiled counter, weight on her back leg with the front leg crossed in front, one hand resting on the counter edge and the other tucking her hair behind her ear, laughing openly with her eyes curved into crescents and dimples showing. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the open cardigan framing the camisole over her chest, her waistline, the high-waisted knit mini skirt and her crossed legs down to just below the knees, one hand on the counter and the other at her ear. Body: standing with her hip leaning on the counter on camera-right, her body turned about 30 degrees toward camera-left, weight on her back leg with the front leg crossed, shoulders relaxed. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 70mm lens from about 4.6 metres, camera at her waist height, level, natural perspective without distortion. Composition: left of centre with the orange counter running to the right and a small plate of golden fried chicken resting soft and out of focus at the right edge. Emphasis: the oblique lean shows her waist-to-hip curve and crossed legs, the open cardigan shows her chest line, and her face stays toward the camera for the crescent-eyed laugh. Lighting: a large warm softbox key from the front right at head height and a soft fill from the left just out of frame light her face evenly; the pendant lamp adds a warm glow on her hair; warm orange and cream tones throughout. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.4 H-coco-wu｜Coco｜橫式款（新企劃｜已接受（R4 owner 紀錄））

**一句話：** 初夏傍晚的薰衣草花田，白色細肩亞麻洋裝，拿著草帽大笑。

**攝影：** 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：抓皺貼身上身與 V 領、收腰、微蓬迷你裙到膝蓋下方；拿在身側的草帽與塞頭髮的手 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the ruched bodice and soft V neckline, the cinched waist and the flared mini skirt down to just below her knees, the straw hat held at her side and the other hand at her ear |
| 3. 身體朝向 | 約30度斜側（朝畫面右）：站在花壟之間，重心在後腳、前膝放鬆；身體朝畫面右轉約30度，肩與臀同向 | standing between the lavender rows with her weight on her back leg and her front knee relaxed, her body turned about 30 degrees toward camera-right, shoulders and hips turned together |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她胸口高度，平視（參考：85mm 鏡頭、約 5.4 公尺；畫面中心與相機高度差換算俯仰約 -1.2 度） | camera at her chest height, level |
| 6. 畫面配置 | 人物置中；薰衣草花壟從畫面下緣往地平線收攏到她身後，形成對稱的引導線 | she is centred, the lavender rows converging from the bottom edge to the horizon behind her as symmetrical leading lines |
| 7. 攝影目的 | 置中構圖與花壟引導線把視線集中在她的大笑；膝上保留 V 領胸型、收腰與裙長 | the centred frame and converging rows lead the eye to her laugh, while the knee-up framing keeps the V neckline, cinched waist and skirt length |

**選擇理由：** 橫式改用置中＋對稱引導線，避免又是「人在一側、另一側空景」；身體約30度斜側讓收腰的線條更明顯，臉正對鏡頭大笑。直式款是池邊坐姿，景別完全不同。

**R7：** 已接受（R4 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R5：** 主管核可的中英同步（R5）：英文 prompt 在身分句後補一句中文「妝感」已寫的內容；服裝、場景、表情、姿態、攝影與身分都不變，接受狀態沿用。補上的句子：`Sweet, light makeup with a pink lip.`

| 項目 | 內容 |
|---|---|
| 場景 | 初夏傍晚一大片薰衣草花田，紫色花壟延伸到遠方，地平線上幾棵柔綠樹，花田裡沒有其他人。 |
| 服裝 | 洋裝：白色亞麻細肩洋裝，抓皺貼身上身、柔和 V 領、收腰、微蓬迷你裙；鞋：白色平底涼鞋（不入鏡）；配件：白色雛菊髮夾、腳踝細金鍊（不入鏡）、草帽（拿在手上） |
| 髮型 | 深棕長波浪捲髮、蓬鬆空氣瀏海。 |
| 妝感 | 甜美淡妝、粉色唇。 |
| 身材設定（數字） | 158 cm／89-56-86／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 抓皺貼身上身與 V 領呈現 E 罩杯胸型，收腰線清楚；迷你裙長露出腿。 |
| 主光 | 她身後的低角度傍晚陽光，頭髮與肩膀暖色輪廓光 |
| 補光 | 畫面外前方大反光板與柔光 |
| 姿態 | 站在花壟之間。 |
| 手的位置 | 一手把草帽拿在身側，一手把頭髮塞到耳後。 |
| 表情 | 瞇眼大笑、深酒窩 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，85mm，約 5.4 公尺，視野 2.29×1.29 公尺；頭頂上方留白約 7%（規劃）；相機約 1.15 公尺高、畫面中心約 1.03 公尺高，俯仰約 -1.2 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 7%（套框後理論約 5.0%）；下緣：規劃裁切線在膝蓋下方的小腿上段（套框後理論上往上移約 2 cm）；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。膝上的下緣套框後理論上會略往上移；若實圖接近膝蓋，4 mm 改由頭頂留白多裁（後製裁切位置，不改拍攝方向）。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | 她的配色有淺紫丁香與奶油白；週末出遊的花田讓她的大笑與甜美成立，不需要校園元素。 |
| 與同一人另一款的差異 | 直式款是飯店泳池、薄荷綠比基尼、坐姿；這款是花田、白色亞麻洋裝、站姿。 |
| 參考照片（用途） | coco-08：身分（認臉與身形比例）；coco-15：表情（大笑） |
| 月份（已確認） | 6 月（初夏） |

| 風險 | 處理 |
|---|---|
| 花田出現遊客或標示牌 | 寫明花田空無一人 |
| 逆光臉暗 | 寫明反光板補臉 |
| 甜美＋洋裝顯小 | 寫明 adult、成熟剪裁 |

prompt 草稿（16:9，尚未執行）：

```text
A 20-year-old adult Taiwanese woman with her natural fair skin tone, a doll-like round face with big sweet eyes and deep dimples when she smiles, dark-brown long wavy hair with soft wispy bangs. Petite curvy figure, 158 cm tall, bust 89 cm, waist 56 cm, hips 86 cm, E cup, full chest and slim waist. Sweet, light makeup with a pink lip. She wears a white linen sundress with thin straps, a fitted ruched bodice with a soft V neckline that shapes her full chest, a cinched waist and a flared mini skirt, and a white daisy hair clip. Setting: a wide lavender field in early summer in the late afternoon, long purple rows running into the distance, a few soft green trees on the horizon, the field empty. She holds a straw sun hat loosely at her side with one hand and tucks her hair behind her ear with the other, laughing with her eyes squeezed into crescents and deep dimples showing. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the ruched bodice and soft V neckline, the cinched waist and the flared mini skirt down to just below her knees, the straw hat held at her side and the other hand at her ear. Body: standing between the lavender rows with her weight on her back leg and her front knee relaxed, her body turned about 30 degrees toward camera-right, shoulders and hips turned together. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with an 85mm lens from about 5.4 metres, camera at her chest height, level, natural perspective without distortion. Composition: she is centred, the lavender rows converging from the bottom edge to the horizon behind her as symmetrical leading lines. Emphasis: the centred frame and converging rows lead the eye to her laugh, while the knee-up framing keeps the V neckline, cinched waist and skirt length. Lighting: the low late-afternoon sun behind her draws a warm rim along her hair and shoulders; a large white reflector and a soft fill just out of frame light her face evenly; soft lilac, white and warm gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.5 H-mia-huang｜Mia｜橫式款（新企劃｜已接受（R4 owner 紀錄））

**一句話：** 夏日黃昏的海邊遊樂碼頭，粉色緞面馬甲上衣配白色迷你裙，拿著棉花糖俏皮眨眼。

**攝影：** 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 大腿中段以上 | a mid-thigh-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在大腿中段，不切在膝蓋。入鏡：心形領馬甲上衣、細腰、整條白色 A 字迷你裙與大腿上段；插腰的手與拿在肩高的棉花糖 | from a little above her head down to mid-thigh, well above the knees, showing the sweetheart corset top, her slim waist and the whole white A-line mini skirt with her upper thighs, one hand on her hip and the cotton candy held at shoulder height |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：站在木棧道上，重心在後腳；身體朝畫面左轉約30度，肩與臀同向，插腰那側的臀部自然往外 | standing on the boardwalk with her weight on her back leg, her body turned about 30 degrees toward camera-left, shoulders and hips turned together, the hip on her hand-on-hip side pushed out slightly |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她胸口高度，平視（參考：85mm 鏡頭、約 4.5 公尺；畫面中心與相機高度差換算俯仰約 -0.1 度） | camera at her chest height, level |
| 6. 畫面配置 | 人物置中；亮燈的摩天輪光點在她右肩後方（畫面右），粉紫晚霞與海面橫在背景 | she is centred, the lit Ferris wheel glowing as bokeh behind her shoulder on camera-right and the pink and lavender sunset sea across the background |
| 7. 攝影目的 | 大腿中段以上把馬甲塑出的胸腰比例放大，正對鏡頭的俏皮眨眼是主角 | a closer frame that enlarges the chest-to-waist shape of the corset top, with her playful wink as the focal point |

**選擇理由：** Mia 的魅力在表情與 F 罩杯曲線：大腿中段以上讓臉與身形都夠大；斜側＋插腰做出腰臀曲線。橫式改置中，背景光點只作氛圍。

**R7：** 已接受（R4 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

| 項目 | 內容 |
|---|---|
| 場景 | 夏天黃昏的海邊遊樂碼頭：遠處亮燈的摩天輪與串燈化成柔和光點、粉紫色晚霞映在海上，木棧道上沒有其他人。 |
| 服裝 | 上身：粉色緞面馬甲上衣（心形領）；下身：白色高腰 A 字迷你裙；鞋：白色厚底涼鞋（不入鏡）；配件：小珍珠耳環、細銀手鍊、一支粉色棉花糖 |
| 髮型 | 灰棕色長髮鬆散大波浪，左側臉旁粉紅 money piece 挑染。 |
| 妝感 | 柔和動漫感眼妝、上揚眼線、圓形腮紅、水光唇。 |
| 身材設定（數字） | 160 cm／91-57-88／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 心形領馬甲上衣塑出 F 罩杯胸型與細腰；高腰 A 字短裙讓腰臀比與腿長清楚。 |
| 主光 | 畫面外右前方的大型柔光，臉乾淨、膚色自然明亮 |
| 補光 | 黃昏天光與遠處遊樂設施的粉紫光點只當背景色 |
| 姿態 | 站在木棧道上。 |
| 手的位置 | 一手插腰，一手把棉花糖拿在肩高、離開臉。 |
| 表情 | 俏皮眨眼、挑逗的半笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，85mm，約 4.5 公尺，視野 1.91×1.07 公尺；頭頂上方留白約 7%（規劃）；相機約 1.2 公尺高、畫面中心約 1.19 公尺高，俯仰約 -0.1 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 8%（套框後理論約 5.9%）；下緣：規劃裁切線在大腿中段（套框後理論上往上移約 2 cm）；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | 她的配色是棉花糖粉與紫；把「被看、被反應」的俏皮放進夏夜遊樂碼頭，不需要任何直播或電競符號。 |
| 與同一人另一款的差異 | 直式款是春夜櫻花步道、淺紫露肩針織洋裝；這款是夏日黃昏碼頭、粉色緞面馬甲＋白裙。 |
| 參考照片（用途） | mia-08：表情（戶外大笑；畫面裡的白 T 不採用）；mia-12：身分（認臉與髮色挑染；不採用畫面裡的帽 T） |
| 月份（已確認） | 7 月（盛夏） |

| 風險 | 處理 |
|---|---|
| 棉花糖遮臉 | 寫明拿在肩高、離開臉 |
| 遊樂設施招牌字 | 只寫摩天輪與串燈光點 |
| 出現電競元素 | 程式檢查 prompt 不含 gaming、headset、RGB、neon |

prompt 草稿（16:9，尚未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a soft round face with big expressive eyes, softly winged liner, rounded blush and glossy tinted lips, long ash-brown hair in loose waves with a pastel-pink money-piece highlight framing the left side of her face. Curvy figure, 160 cm tall, bust 91 cm, waist 57 cm, hips 88 cm, F cup, a full chest and a slim waist. She wears a pastel-pink satin corset top with a sweetheart neckline that shapes her full chest and slim waist, a white high-waisted A-line mini skirt, small pearl earrings and a thin silver bracelet. Setting: a seaside amusement pier at dusk in summer, a lit Ferris wheel and string lights far behind her softening into bokeh, a pink and lavender sunset sky over the sea, the wooden boardwalk empty. One hand rests on her hip and the other holds a small pink cotton candy at shoulder height, away from her face; she gives a playful wink with a teasing half-smile. Shot: a mid-thigh-up shot, from a little above her head down to mid-thigh, well above the knees, showing the sweetheart corset top, her slim waist and the whole white A-line mini skirt with her upper thighs, one hand on her hip and the cotton candy held at shoulder height. Body: standing on the boardwalk with her weight on her back leg, her body turned about 30 degrees toward camera-left, shoulders and hips turned together, the hip on her hand-on-hip side pushed out slightly. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with an 85mm lens from about 4.5 metres, camera at her chest height, level, natural perspective without distortion. Composition: she is centred, the lit Ferris wheel glowing as bokeh behind her shoulder on camera-right and the pink and lavender sunset sea across the background. Emphasis: a closer frame that enlarges the chest-to-waist shape of the corset top, with her playful wink as the focal point. Lighting: a large soft key light from front-right just out of frame lights her face cleanly with natural, bright skin tones; the dusk sky and the distant ride lights add pink and lavender colour behind her; cotton-candy pink, lavender and soft gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.6 H-yuna-kim｜Yuna｜橫式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 雪後清晨的白樺林小徑，霧玫瑰粉貼身方領針織上衣＋淺灰高腰羊毛迷你裙，外披敞開的白色短版羊羔毛外套。

**攝影：** 大腿中段以上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 大腿中段以上 | a mid-thigh-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在大腿中段，不切在膝蓋。入鏡：敞開的白色羊羔毛短外套、霧玫瑰方領針織上衣的胸型、細腰、整條灰色迷你裙與大腿上段；拉外套衣襟的手與撥頭髮的手 | from a little above her head down to mid-thigh, well above the knees, showing the open white shearling jacket, the dusty-rose square-neck knit top over her chest, her narrow waist, the whole grey mini skirt and her upper thighs, one hand holding the jacket edge at her waist and the other tucking her hair behind her ear |
| 3. 身體朝向 | 約30度斜側（朝畫面右）：站在林間小徑上，重心在後腳；身體朝畫面右轉約30度，肩與臀同向，腰線自然拉長 | standing on the snowy path with her weight on her back leg, her body turned about 30 degrees toward camera-right, shoulders and hips turned together, her waist lengthened |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她胸口高度，平視（參考：85mm 鏡頭、約 4.8 公尺；畫面中心與相機高度差換算俯仰約 +0.0 度） | camera at her chest height, level |
| 6. 畫面配置 | 人物略偏左；細白的樺樹幹在兩側形成直線節奏，右側林間小徑往深處延伸，背景柔焦 | she stands slightly left of centre, slim white birch trunks making a vertical rhythm on both sides and the snowy path receding softly on the right |
| 7. 攝影目的 | 大腿中段以上放大水光肌、凍紅臉頰與冬日穿搭勾出的胸腰線，雪地反光讓整體通透 | a closer frame that brings forward her dewy skin, flushed cheeks and the curves of the winter outfit, the snow light keeping the picture airy |

**選擇理由：** 主管推薦雪後庭園或冬日花園露台；整組已有 Coco 花田、V-Luna 紫陽花庭院、H-Tammy 春日花園露台、V-Miu 花園木平台四個庭園類場景，所以改提同樣安靜、但不是庭園的雪後白樺林。大腿中段以上讓韓系妝感與身形都夠大；直式款是全身銀杏大道、不看鏡頭，兩款景別與視線都不同。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 撤回咖啡館與奶油黃開襟＋淺藍裙：改成雪後白樺林小徑的戶外冬日寫真，霧玫瑰貼身方領針織＋淺灰高腰迷你裙＋敞開的白色羊羔毛短外套；景別由腰上改為大腿中段以上。主管推薦是雪後庭園／冬日花園露台，因整組庭園類場景已有 4 個，改提白樺林（理由見選擇理由）。

| 項目 | 內容 |
|---|---|
| 場景 | 雪後清晨安靜的白樺林：細白的樹幹整齊排列，林間小徑覆著一層平整的新雪，淡淡的薄霧與柔和晨光，林中沒有其他人。 |
| 服裝 | 外套：白色短版羊羔毛外套（敞開）；上身：霧玫瑰粉細羅紋貼身方領長袖針織上衣；下身：淺灰高腰羊毛迷你裙；鞋：淺灰麂皮及膝長靴（不入鏡）；配件：細銀耳環 |
| 髮型 | 深棕自然波浪、鎖骨長度、空氣感八字瀏海。 |
| 妝感 | 水光肌、以眼妝為重點、珊瑚漸層唇、凍紅的臉頰。 |
| 身材設定（數字） | 168 cm／84-58-89／C（纖細長腿） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身方領針織清楚勾出胸型與 58 cm 細腰（C 罩杯，寫成纖細）；高腰迷你裙收出腰臀；敞開的短外套只在兩側，不遮胸腰。 |
| 主光 | 林間柔和的清晨散射光，加上雪地反光（整體偏亮） |
| 補光 | 畫面外前方柔光，臉均勻、膚色清透 |
| 姿態 | 站在雪後的林間小徑上。 |
| 手的位置 | 一手拉住敞開外套的衣襟停在腰側，一手把一縷頭髮撥到耳後。 |
| 表情 | 清淡溫柔的微笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，85mm，約 4.8 公尺，視野 2.03×1.14 公尺；頭頂上方留白約 9%（規劃）；相機約 1.25 公尺高、畫面中心約 1.25 公尺高，俯仰約 +0.0 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 9%（套框後理論約 7.3%）；下緣：規劃裁切線在大腿中段（套框後理論上往上移約 2 cm）；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | 韓系冬日寫真落在具體元素上：妝髮（水光肌、凍紅臉頰、八字瀏海）、穿搭（白、灰、霧玫瑰的柔和配色）、光（雪地反光的偏亮通透曝光）與低對比色調；白樺林乾淨安靜，沒有文字或地標。 |
| 與同一人另一款的差異 | 直式款是深秋銀杏大道、奶油色毛呢套裝＋黑色長靴、望向大道深處；這款是雪後白樺林、霧玫瑰針織＋灰色迷你裙＋白色羊羔毛短外套、看鏡頭。與 12 月 V-Somi 的雪夜燈籠溫泉街不同：白天、森林、冷柔色調。 |
| 參考照片（用途） | yuna-05：表情（柔和、手撥頭髮的近照；室內背景不採用）；yuna-02：身分（認臉與身形比例；街景不採用） |
| 月份（已確認） | 1 月（冬） |

| 風險 | 處理 |
|---|---|
| 雪地過曝吃掉臉 | 測光給臉、前方補光 |
| 外套蓋住身形 | 寫明敞開、只在兩側 |
| 冬裝顯厚 | 貼身方領針織＋迷你裙 |
| 林中出現路牌或文字 | 只寫樹與小徑 |

prompt 草稿（16:9，尚未執行）：

```text
A 21-year-old adult Korean woman with her natural fair skin tone, large bright double-eyelid eyes as the focus of her makeup, a dewy glass-skin finish and soft coral gradient lips, dark-brown natural wavy hair at collarbone length with airy curtain bangs. Slim, long-legged figure, 168 cm tall, bust 84 cm, waist 58 cm, hips 89 cm, C cup, a narrow waist and long legs. She wears an open white cropped shearling jacket, a fitted dusty-rose fine-rib square-neck long-sleeve knit top that follows her chest and narrow waist, a high-waisted pale-grey wool mini skirt and thin silver earrings. Setting: a quiet birch forest on a winter morning after fresh snow, slim white trunks in even rows, a path covered with a smooth layer of new snow, a little soft mist, the forest empty. One hand holds the edge of the open jacket at her waist and the other tucks a strand of hair behind her ear; she gives a soft, gentle smile. Shot: a mid-thigh-up shot, from a little above her head down to mid-thigh, well above the knees, showing the open white shearling jacket, the dusty-rose square-neck knit top over her chest, her narrow waist, the whole grey mini skirt and her upper thighs, one hand holding the jacket edge at her waist and the other tucking her hair behind her ear. Body: standing on the snowy path with her weight on her back leg, her body turned about 30 degrees toward camera-right, shoulders and hips turned together, her waist lengthened. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with an 85mm lens from about 4.8 metres, camera at her chest height, level, natural perspective without distortion. Composition: she stands slightly left of centre, slim white birch trunks making a vertical rhythm on both sides and the snowy path receding softly on the right. Emphasis: a closer frame that brings forward her dewy skin, flushed cheeks and the curves of the winter outfit, the snow light keeping the picture airy. Lighting: soft diffused morning light through the trees with bright bounce from the snow, a soft fill just out of frame in front keeping her face clear; an airy, slightly bright exposure with clean snow-white, ash-grey and dusty-rose tones and soft contrast. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.7 H-tammy-chou｜Tammy｜橫式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 春日花園露台的平整石板步道，熱粉色方領貼身針織洋裝配白色露跟高跟鞋，站在庭園長椅旁明亮地笑。

**攝影：** 全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜膝蓋高度・輕仰

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到鞋底完整；熱粉色貼身針織洋裝的胸腰臀線、雙腿與白色尖頭露跟高跟鞋；扶椅背的手與插腰的手 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to heels, the fitted hot-pink knit dress over her chest, waist and hips, her legs and the white slingback heels, one hand on the bench back and the other on her hip |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：站在平整的石板步道上，重心在後腳、前腳尖朝鏡頭輕點，雙腿一前一後；身體朝畫面左轉約30度，肩與臀同向 | standing on the smooth stone path with her weight on her back leg and her front foot pointed toward the camera, legs one in front of the other, her body turned about 30 degrees toward camera-left, shoulders and hips turned together |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她膝蓋高度，輕仰（參考：70mm 鏡頭、約 6.9 公尺；畫面中心與相機高度差換算俯仰約 +2.7 度） | camera at her knee height, tilted slightly upward |
| 6. 畫面配置 | 人物略偏左；白色庭園長椅在她身旁右側，花木與鬱金香在兩側與背景柔焦；人物佔畫面高度約八成四 | she stands slightly left of centre with the white garden bench just beside her on the right, the blossoms and tulips soft on both sides and behind |
| 7. 攝影目的 | 保留合身洋裝＋高跟鞋：全身、斜側與輕仰讓腿與高跟鞋修長，春日花園帶出自然的質感 | the fitted dress and heels shown head to toe with an oblique stance and a slightly low camera that lengthens her legs, the spring garden giving a natural, refined feel |

**選擇理由：** Penny 說合身洋裝＋高跟鞋可保留，所以橫式款用全身讓高跟鞋入鏡；膝蓋高度輕仰拉長腿。直式款是大腿中段以上，兩款景別不同。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 取消精品店：改成春日花園露台的平整石板步道（不踩泥地、碎石或沙灘），熱粉合身洋裝＋白色高跟鞋保留；手改為一手扶白色庭園長椅、一手插腰；拿掉手提包（素面小包放到直式款）。

| 項目 | 內容 |
|---|---|
| 場景 | 四月晴朗午後的私人花園露台：平整的淺色石板步道、兩側修剪整齊的綠籬、盛開的白色花木與鬱金香花圃、一張白色鐵藝庭園長椅，花園沒有其他人。 |
| 服裝 | 洋裝：熱粉色方領羅紋針織貼身迷你洋裝（保留 Penny 同意的方向）；鞋：白色尖頭露跟高跟鞋；配件：金色圈耳環、細金手鍊 |
| 髮型 | 奶茶金棕大波浪長捲髮，臉側淺色 money piece 挑染。 |
| 妝感 | 閃粉眼影、果凍唇。 |
| 身材設定（數字） | 160 cm／90-57-89／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身針織洋裝完整勾出 E 罩杯胸型、細腰與臀線；斜側站姿與高跟鞋拉長腿。 |
| 主光 | 左前方偏低的柔和午後春陽 |
| 補光 | 畫面外右前方大反光板 |
| 姿態 | 站在石板步道上、白色庭園長椅旁。 |
| 手的位置 | 一手輕扶在長椅椅背上，一手插腰。 |
| 表情 | 明亮的笑容 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，70mm，約 6.9 公尺，視野 3.55×2.0 公尺；人物約佔畫面高度 84%（規劃）；相機約 0.53 公尺高、畫面中心約 0.86 公尺高，俯仰約 +2.7 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 9%（套框後理論約 7.2%）；下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%）；不能切：髮頂、臉、入鏡的雙手、雙腳與鞋；規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | 合身洋裝＋高跟鞋保留；平整的石板步道讓高跟鞋站得穩、合理，春天的白花與鬱金香讓熱粉色更亮眼，是自然、有質感的高級感，不靠店面或商標。 |
| 與同一人另一款的差異 | 直式款是夜晚大飯店大廳、白色西裝洋裝、大腿中段以上、拿素面小包；這款是白天春日花園露台、熱粉針織洋裝、全身與高跟鞋。 |
| 參考照片（用途） | tammy-02：服裝材質（貼身洋裝的線條）；tammy-05：身分（認臉與柔和的笑；室內不採用） |
| 月份（已確認） | 4 月（春） |

| 風險 | 處理 |
|---|---|
| 高跟鞋踩在泥地或碎石 | 寫明站在平整石板步道上 |
| 花木遮住腿 | 花木只在兩側與背景 |
| 長椅搶戲 | 長椅只在身旁、人物佔畫面高度約八成四 |
| 洋裝或鞋出現商標 | 寫素面 |

prompt 草稿（16:9，尚未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, round almond eyes with visible aegyo-sal, shimmer eyeshadow and jelly-glossy lips, long voluminous big-wave hair in milk-tea golden brown with light money-piece highlights at the front. Curvy figure, 160 cm tall, bust 90 cm, waist 57 cm, hips 89 cm, E cup, a full chest and a slim waist. She wears a fitted hot-pink square-neck rib-knit mini dress that follows her full chest, slim waist and hips, white pointed slingback heels, gold hoop earrings and a thin gold bracelet. Setting: a private garden terrace on a clear April afternoon, a smooth pale stone-paved path, neatly trimmed hedges, white flowering trees and beds of tulips on both sides, a white wrought-iron garden bench, the garden empty. One hand rests lightly on the back of the garden bench and the other on her hip; she smiles brightly. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to heels, the fitted hot-pink knit dress over her chest, waist and hips, her legs and the white slingback heels, one hand on the bench back and the other on her hip. Body: standing on the smooth stone path with her weight on her back leg and her front foot pointed toward the camera, legs one in front of the other, her body turned about 30 degrees toward camera-left, shoulders and hips turned together. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 70mm lens from about 6.9 metres, camera at her knee height, tilted slightly upward, natural perspective without distortion; she fills about 84% of the frame height. Composition: she stands slightly left of centre with the white garden bench just beside her on the right, the blossoms and tulips soft on both sides and behind. Emphasis: the fitted dress and heels shown head to toe with an oblique stance and a slightly low camera that lengthens her legs, the spring garden giving a natural, refined feel. Lighting: soft, slightly low spring afternoon sun from front-left with a large white reflector just out of frame on the right lighting her face evenly; hot pink against white blossoms and fresh green tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.8 H-rin-ayase｜Rin｜橫式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 夕陽中的高樓飯店套房，酒紅緞面垂墜領細肩長洋裝，側躺在深綠絲絨貴妃椅上望向窗外的夕陽。

**攝影：** 斜躺全身｜側面斜躺（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側窗外的夕陽｜略高於她斜躺時頭部的高度・輕俯

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 斜躺全身 | a full-length reclining shot |
| 2. 畫面上下界 | 左右包含頭到腳的完整身長；頭部上方留白，下緣在椅面下方。入鏡：垂墜領緞面洋裝貼著胸腰、抬高的臀線、交疊的長腿與赤腳；撐在椅墊上的前臂與放在大腿上的手 | her whole reclining length from her head to her feet, with space above her head and the frame bottom below the seat, showing the cowl-neck satin dress over her chest and waist, her raised hip, her long crossed legs and bare feet, the supporting forearm on the cushion and the other hand resting on her thigh |
| 3. 身體朝向 | 側面斜躺（朝畫面右）：側躺在貴妃椅上，雙腿側面朝畫面右、上身轉向鏡頭約45度；下方的前臂撐起上身，肩頸放鬆往後，腰側下凹、臀線抬高，上方那條腿微彎往前搭在伸直的下方腿上 | lying on her side along the chaise, her legs in side view toward camera-right and her upper body turned about 45 degrees toward the camera, propped on her lower forearm with her shoulders and neck relaxed and drawn back, her waist dipping and her hip raised, her top leg softly bent forward over her straight lower leg |
| 4. 臉部朝向與視線 | 三分之二側臉，看向畫面右側窗外的夕陽（不看鏡頭） | her face in a three-quarter view, looking out of the window toward the sunset on camera-right, away from the camera |
| 5. 相機高度與俯仰 | 相機在略高於她斜躺時頭部的高度，輕俯（參考：50mm 鏡頭、約 2.6 公尺；畫面中心與相機高度差換算俯仰約 -7.1 度） | camera at a height slightly above her head as she reclines, tilted slightly downward |
| 6. 畫面配置 | 人物沿貴妃椅橫跨畫面中央，頭在左、赤腳在右，成一條水平的 S 形曲線；她順著身體望向右側窗外的夕陽，落地窗與天際線在後方 | she lies across the centre of the frame along the chaise, her head on the left and her bare feet on the right in a long horizontal S-curve, gazing along her body toward the sunset in the window on the right, the skyline behind her |
| 7. 攝影目的 | 側躺的腰臀曲線與長腿是畫面主線；望向窗外夕陽的三分之二側臉讓她更慵懶、成熟 | her side-lying waist and hip curve and long legs are the main line of the picture, and the three-quarter face toward the sunset makes her languid and mature |

**選擇理由：** 保留酒紅緞面與斜躺；不看鏡頭、視線有明確目標（窗外夕陽）。相機略高於她的頭、輕俯，讓 S 形完整，不從椅面高度仰拍。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 保留酒紅緞面與斜躺；改為不看鏡頭、望向窗外夕陽；姿勢寫清楚：下方前臂撐椅墊、肩頸放鬆往後、腰側下凹臀線抬高、上方腿微彎搭在伸直的下方腿上、上方手放在大腿上。

| 項目 | 內容 |
|---|---|
| 場景 | 日落時的高級飯店套房：落地窗邊一張深綠絲絨貴妃椅，窗外遠方城市天際線籠罩在暖色暮靄，房間整齊。 |
| 服裝 | 洋裝：深酒紅真絲緞面垂墜領細肩中長洋裝；鞋：赤腳；配件：細金鍊項鍊、金色小耳針 |
| 髮型 | 深酒紅棕長髮，柔和大波浪撥到一側肩上。 |
| 妝感 | 乾淨底妝、精準眼線、豆沙紅唇。 |
| 身材設定（數字） | 166 cm／92-58-90／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 垂墜領緞面貼著 F 罩杯胸型流動；側躺時腰側下凹、臀線抬高，上方那條腿微彎往前搭在伸直的下方腿上，形成一條長的 S 形曲線。 |
| 主光 | 相機右側落地窗進來的低角度夕陽 |
| 補光 | 畫面外左側柔光 |
| 姿態 | 側躺在貴妃椅上：下方的前臂平放在椅子抬高的一端撐起上身，上方那條腿膝蓋微彎、往前搭在伸直的下方腿上。 |
| 手的位置 | 下方手的前臂撐在椅墊上，上方的手輕放在臀側的大腿上。 |
| 表情 | 平靜、帶一點慵懶的淺笑 |
| 視線 | 看向畫面右側窗外的夕陽（不看鏡頭） |
| 焦段／距離／視野（參考） | 16:9，50mm，約 2.6 公尺，視野 1.87×1.05 公尺；人物約佔畫面寬度 87%（規劃）；相機約 1.02 公尺高、畫面中心約 0.69 公尺高，俯仰約 -7.1 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 24%（套框後理論約 22.9%）；左右：規劃頭與腳離左右邊緣各約 7%；不能切：髮頂、臉、入鏡的雙手、頭與腳；規劃目標（套框後）：髮頂上方 ≥4%、左右各 ≥5%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、頭與腳是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | 她是成熟艷麗但收斂的性感：不看鏡頭、望向窗外夕陽，比直視更有寫真感；姿勢靠側躺的腰臀曲線與長腿，不靠高難度扭轉，也不靠「性感」這個字。 |
| 與同一人另一款的差異 | 直式款是秋日港灣、墨綠仿麂皮裹身洋裝、倚著繫船柱；這款是室內套房夕陽、酒紅緞面、側躺。與 3 月 Miu（床上靠枕半倚）分開：Rin 是全身側躺在貴妃椅上（10 月 Luna 在 R6 改為站姿和服）。 |
| 參考照片（用途） | rin-05：服裝材質（緞面開衩洋裝的質感）；rin-01：身分（盤髮與妝感） |
| 月份（已確認） | 2 月（冬） |

| 風險 | 處理 |
|---|---|
| 側躺肢體結構錯誤 | 寫明下方前臂撐椅墊、上方腿往前搭在下方腿上 |
| 不看鏡頭時臉太側 | 三分之二側臉、臉朝窗光 |
| 緞面遮蔽 | 中長洋裝、細肩帶 |

prompt 草稿（16:9，尚未執行）：

```text
A 25-year-old adult Japanese woman with her natural fair, cool-toned skin, an oval face with long narrow eyes and a straight nose, a clean base with precise eyeliner and a muted rose-red lip, long deep wine-red brown hair styled in soft big waves over one shoulder. Curvy figure, 166 cm tall, bust 92 cm, waist 58 cm, hips 90 cm, F cup, a full chest, a slim waist and long legs. She wears a deep wine-red silk satin cowl-neck slip midi dress with thin straps that drapes over her full chest and slim waist, a thin gold chain necklace and small gold stud earrings; her feet are bare. Setting: a luxury hotel suite at sunset, a deep green velvet chaise longue beside a floor-to-ceiling window, the city skyline far below in warm evening haze, the room tidy. She is propped on her lower forearm flat on the raised end of the chaise, her other hand resting lightly on her thigh near her hip, with a calm, slightly languid half-smile. Shot: a full-length reclining shot, her whole reclining length from her head to her feet, with space above her head and the frame bottom below the seat, showing the cowl-neck satin dress over her chest and waist, her raised hip, her long crossed legs and bare feet, the supporting forearm on the cushion and the other hand resting on her thigh. Body: lying on her side along the chaise, her legs in side view toward camera-right and her upper body turned about 45 degrees toward the camera, propped on her lower forearm with her shoulders and neck relaxed and drawn back, her waist dipping and her hip raised, her top leg softly bent forward over her straight lower leg. Face and gaze: her face in a three-quarter view, looking out of the window toward the sunset on camera-right, away from the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 2.6 metres, camera at a height slightly above her head as she reclines, tilted slightly downward, natural perspective without distortion; she fills about 87% of the frame width. Composition: she lies across the centre of the frame along the chaise, her head on the left and her bare feet on the right in a long horizontal S-curve, gazing along her body toward the sunset in the window on the right, the skyline behind her. Emphasis: her side-lying waist and hip curve and long legs are the main line of the picture, and the three-quarter face toward the sunset makes her languid and mature. Lighting: warm low sunset light through the window from camera-right as the key, a soft fill just out of frame on the left keeping her face clear; wine red, deep green and soft gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.9 H-rainie-hsu｜Rainie｜橫式款（Penny 已接受的 v2 主方向｜已接受（R4 owner 紀錄））

**一句話：** Penny 已接受的方向：頂樓夜景，血紅緞面馬甲高衩迷你洋裝，背靠玻璃欄杆直視鏡頭。

**攝影：** 膝上｜正面｜臉正面・看鏡頭｜腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：馬甲塑出的胸型與細腰、高衩露出的大腿到膝蓋下方；放在身後欄杆上的雙手 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the corset bodice over her chest and slim waist and her leg through the thigh-high slit down to just below the knee, both hands on the rail behind her |
| 3. 身體朝向 | 正面：背靠玻璃欄杆站著，重心在後腳、一腿從高衩往前；身體正對鏡頭，肩膀輕靠玻璃 | leaning back against the glass balustrade with her weight on her back leg and one leg forward through the slit, her body square to the camera, her shoulders resting lightly on the glass |
| 4. 臉部朝向與視線 | 臉正面，直視鏡頭 | her face toward the camera, looking straight into the camera |
| 5. 相機高度與俯仰 | 相機在她腰部高度，平視（參考：85mm 鏡頭、約 5.7 公尺；畫面中心與相機高度差換算俯仰約 +0.5 度） | camera at her waist height, level |
| 6. 畫面配置 | 人物偏右；左側是城市燈海散景（已接受的構圖） | right of centre with the glowing city bokeh on the left |
| 7. 攝影目的 | 正面直視呈現她的氣場，膝上保留馬甲胸腰線與高衩腿線 | her direct gaze carries her presence while the knee-up frame keeps the corset lines and the slit leg |

**選擇理由：** 已接受方向：姿勢、取景、焦段與「人物偏右、左側燈海」都照舊；24 套中只剩這一張是正面膝上站姿，因為背靠欄杆的姿勢本來就正對鏡頭。

**R7：** 已接受（R4 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

| 項目 | 內容 |
|---|---|
| 場景 | 高樓頂層露台的夜晚：玻璃欄杆、腳下城市燈光化成柔和散景、平滑深色石材地面，露台上沒有其他東西。 |
| 服裝 | 洋裝：血紅緞面馬甲迷你洋裝（大腿高衩）；鞋：黑色細帶高跟涼鞋（不入鏡）；配件：大型銀色垂墜耳環、細銀手環 |
| 髮型 | 長直黑髮，光滑有光澤，深側分。 |
| 妝感 | 柔和魅惑妝、貼近睫毛的淡棕眼線。 |
| 身材設定（數字） | 165 cm／94-59-92／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 馬甲塑出 F 罩杯胸型與細腰；高衩露出的腿呈現臀腿比例。 |
| 主光 | 左前方頭部高度的大型明亮柔光箱 |
| 補光 | 畫面外右側柔光；背後深藍夜空與暖金城市散景 |
| 姿態 | 背靠玻璃欄杆，一腳從高衩往前。 |
| 手的位置 | 雙手放在身後的欄杆上；不拿任何杯子。 |
| 表情 | 自信又帶點壞的笑 |
| 視線 | 直視鏡頭 |
| 焦段／距離／視野（參考） | 16:9，85mm，約 5.7 公尺，視野 2.41×1.36 公尺；頭頂上方留白約 8%（規劃）；相機約 1.12 公尺高、畫面中心約 1.17 公尺高，俯仰約 +0.5 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 8%（套框後理論約 6.1%）；下緣：規劃裁切線在膝蓋下方的小腿上段（套框後理論上往上移約 3 cm）；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。膝上的下緣套框後理論上會略往上移；若實圖接近膝蓋，4 mm 改由頭頂留白多裁（後製裁切位置，不改拍攝方向）。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | Penny 接受的 v2 主方向；城市燈海是橫向展開的景，最適合橫式款。 |
| 與同一人另一款的差異 | 直式款是雨後夜街、黑色緞面繞頸洋裝＋黑色長皮風衣；這款是頂樓城市燈海、血紅馬甲洋裝。 |
| 參考照片（用途） | rainie-06：場景（飯店窗邊的城市景）；rainie-10：服裝材質（緞面長洋裝的光澤） |
| 月份（已確認） | 12 月（年末） |

| 風險 | 處理 |
|---|---|
| 出現酒杯或酒瓶 | 手放在欄杆上，場景只寫欄杆與地面 |
| 高衩遮蔽 | 生成後逐張檢查 |
| 玻璃反射出另一個人 | 寫明玻璃只反射城市燈光 |

prompt 草稿（16:9，尚未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, high cheekbones and a sculpted jaw, soft-glam makeup with a soft brown liner close to the lash line, long straight jet-black hair worn sleek and glossy with a deep side part. Curvy figure, 165 cm tall, bust 94 cm, waist 59 cm, hips 92 cm, F cup, full chest and slim waist. She wears a blood-red satin corset mini dress with a thigh-high slit, large silver statement drop earrings and a slim silver cuff. Setting: a high-rise penthouse terrace at night, a glass balustrade with the city lights far below spread into soft bokeh, a smooth dark stone floor, nothing else on the terrace, the glass reflecting only city lights. She leans back against the glass balustrade with both hands resting on the rail behind her and one leg forward through the slit, with a confident, slightly mischievous smirk. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the corset bodice over her chest and slim waist and her leg through the thigh-high slit down to just below the knee, both hands on the rail behind her. Body: leaning back against the glass balustrade with her weight on her back leg and one leg forward through the slit, her body square to the camera, her shoulders resting lightly on the glass. Face and gaze: her face toward the camera, looking straight into the camera. Camera: horizontal 16:9 frame, full-frame camera with an 85mm lens from about 5.7 metres, camera at her waist height, level, natural perspective without distortion. Composition: right of centre with the glowing city bokeh on the left. Emphasis: her direct gaze carries her presence while the knee-up frame keeps the corset lines and the slit leg. Lighting: a large bright softbox key from front-left at head height lights her face and catches crisp red highlights on the satin; a soft fill from the right just out of frame; deep navy night sky and warm gold city bokeh behind her. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.10 H-miu-shiraishi｜Miu｜橫式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 晨光灑進的一人公寓，象牙白蕾絲緞面細肩小可愛與短褲，背靠床頭的枕頭堆自然半倚、歪頭甜笑。

**攝影：** 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 坐姿全身 | a full-length seated shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，坐姿的雙腿與雙腳完整。入鏡：完整半倚坐姿；緞面小可愛的胸型與很細的腰、短褲、立起的膝蓋與伸長的腿、赤腳；搭在膝上的手與放在床上的手，不遮胸腰 | her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole half-reclining figure, the satin camisole over her full chest and very slim waist, the shorts, her raised knee, her stretched leg and her bare feet, one arm resting on her knee and the other hand on the bed, nothing covering her chest or waist |
| 3. 身體朝向 | 約45度斜側（朝畫面左）：坐在床上、背靠床頭堆起的枕頭半倚，身體朝畫面左轉約45度；一膝立起、另一條腿沿床伸直，肩膀放鬆、腰側拉長 | sitting on the bed and leaning back against a pile of pillows at the headboard, her body turned about 45 degrees toward camera-left, one knee raised and the other leg stretched out along the bed, shoulders relaxed and her waist lengthened |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她坐姿時的腰部高度，平視（參考：35mm 鏡頭、約 2.7 公尺；畫面中心與相機高度差換算俯仰約 -1.0 度） | camera at her seated waist height, level |
| 6. 畫面配置 | 床沿在畫面斜放成對角線，她在中央偏右的枕頭堆前；左側是透著晨光的白紗窗，右側是木製床邊架 | the bed runs diagonally across the frame and she sits just right of centre against the pillows, the sheer-curtained window glowing on the left and the wooden bedside shelf on the right |
| 7. 攝影目的 | 自然半倚把胸型、很細的腰與腿線同時打開，歪頭甜笑看鏡頭；平視高度不俯拍，避免顯小 | the relaxed half-recline opens up her chest, very slim waist and legs at once, with a sweet head-tilted smile to the camera; a level camera keeps her looking like an adult |

**選擇理由：** 從端坐改成床上靠枕的自然半倚，與 Rin 的貴妃椅側躺不同（Luna 在 R6 改為站姿和服）；小公寓空間有限，35mm 約 2.6 公尺、人物在中央不貼邊，避免廣角變形。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 從端坐床邊、雙膝併攏雙手撐床，改為背靠枕頭的自然半倚（一膝立起、一腿伸直、手肘搭膝、另一手放床上），床改成斜放的對角線；服裝與晨光不變。

| 項目 | 內容 |
|---|---|
| 場景 | 早晨陽光灑進的東京小公寓：鋪奶油色亞麻床單的整齊床鋪、木製床邊架上一小盆植物、窗上白紗簾，房間整齊。 |
| 服裝 | 上身：象牙白緞面細肩小可愛（細蕾絲滾邊）；下身：同色緞面短褲；鞋：赤腳；配件：細金耳針、細金手鍊 |
| 髮型 | 淺亞麻米金，齊肩內彎鮑伯、空氣瀏海。 |
| 妝感 | 眼下橘調腮紅、水潤唇。 |
| 身材設定（數字） | 156 cm／87-55-86／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 背靠枕頭、一膝立起，緞面小可愛貼著 E 罩杯胸型、露出很細的腰；伸長的那條腿與立起的膝蓋呈現腿線；雙手不擋胸腰。 |
| 主光 | 相機左側白紗簾透進的溫暖晨光 |
| 補光 | 畫面外右側白色反光 |
| 姿態 | 坐在床上、背靠床頭堆起的枕頭半倚：一膝立起、另一條腿沿著床伸直。 |
| 手的位置 | 一手手肘輕搭在立起的膝蓋上、手腕自然垂下，另一手放在身旁的床單上。 |
| 表情 | 歪頭、帶一點慵懶的甜笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，35mm，約 2.7 公尺，視野 2.78×1.56 公尺；人物約佔畫面高度 84%（規劃）；相機約 0.72 公尺高、畫面中心約 0.67 公尺高，俯仰約 -1.0 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 9%（套框後理論約 7.5%）；下緣：規劃雙腳下方留白約 7%（套框後理論約 5.3%）；不能切：髮頂、臉、入鏡的雙手、雙腳；規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | 她的支柱是「私下／一人公寓」：自然半倚比端坐更放鬆，胸腰與腿線都出來，仍是甜美的成人氣質（成熟的緞面與金飾、不用娃娃裝元素）。 |
| 與同一人另一款的差異 | 直式款是春日度假木平台、杏桃色細肩短洋裝、坐在吊床邊看向一旁；這款是室內晨光、緞面小可愛＋短褲、床上半倚看鏡頭。與 2 月 Rin 的貴妃椅全身側躺不同：Miu 是背靠枕頭的坐姿半倚，床是斜放的對角線。 |
| 參考照片（用途） | miu-06：身分（米白背心＋短裙的身形比例）；miu-01：表情（坐姿的甜美表情；厚毛衣不採用） |
| 月份（已確認） | 3 月（冬末初春） |

| 風險 | 處理 |
|---|---|
| 童顏顯小 | 寫明 adult、成熟緞面與金飾；不用娃娃裝與制服元素 |
| 居家服尺度 | 細肩小可愛＋短褲，完整遮蔽 |
| 立膝角度 | 短褲完整遮蔽、相機在側前方平視 |
| 碰撞紀錄（Jia、Somi） | 暖白奶油色、甜美、淺亞麻短髮；不改臉、不宣稱能消除 |

prompt 草稿（16:9，尚未執行）：

```text
A 22-year-old adult Japanese woman with her natural very fair skin tone, a round face with big soft downturned eyes, orange-toned blush under the eyes and glossy lips, light flaxen beige-blonde hair in a shoulder-length bob curled inward with airy see-through bangs. Petite curvy figure, 156 cm tall, bust 87 cm, waist 55 cm, hips 86 cm, E cup, a full chest and a very slim waist. She wears an ivory satin camisole with thin straps and fine lace trim that follows her full chest, matching ivory satin shorts, small gold stud earrings and a thin gold bracelet; her feet are bare. Setting: a small sunlit Tokyo apartment in the morning, a neatly made bed with cream linen, a wooden bedside shelf with a small potted plant, sheer white curtains at the window, the room tidy. One elbow rests lightly on her raised knee with the wrist relaxed and her other hand lies on the sheet beside her hip; she tilts her head with a soft, slightly lazy sweet smile. Shot: a full-length seated shot, her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole half-reclining figure, the satin camisole over her full chest and very slim waist, the shorts, her raised knee, her stretched leg and her bare feet, one arm resting on her knee and the other hand on the bed, nothing covering her chest or waist. Body: sitting on the bed and leaning back against a pile of pillows at the headboard, her body turned about 45 degrees toward camera-left, one knee raised and the other leg stretched out along the bed, shoulders relaxed and her waist lengthened. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 35mm lens from about 2.7 metres, camera at her seated waist height, level, natural perspective without distortion; she fills about 84% of the frame height. Composition: the bed runs diagonally across the frame and she sits just right of centre against the pillows, the sheer-curtained window glowing on the left and the wooden bedside shelf on the right. Emphasis: the relaxed half-recline opens up her chest, very slim waist and legs at once, with a sweet head-tilted smile to the camera; a level camera keeps her looking like an adult. Lighting: warm morning sunlight through the sheer curtains from camera-left as a soft key, a white bounce just out of frame on the right so her face is evenly lit; cream, ivory and warm wood tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.11 H-jia-seo｜Jia｜橫式款（新企劃｜已接受（R7 owner 紀錄））

**一句話：** 初秋傍晚的湖畔木平台，深酒紅合身繞頸細針織短洋裝露肩與上背，側坐在臨水長椅上、雙腿交疊望向湖面。

**攝影：** 坐姿全身｜側面（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側的湖面與遠岸｜坐姿時的腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 坐姿全身 | a full-length seated shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，坐姿的雙腿與雙腳完整。入鏡：完整坐姿；繞頸剪裁露出的直角肩與上背、收腰的合身針織、大腿中段的裙襬、交疊的長腿與黑色細帶涼鞋；放在膝上的手與搭在椅背上的手臂，不遮腰線 | her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the bare shoulders and upper back of the halter cut, the fitted knit drawn in at her waist, the hem at mid-thigh, her long crossed legs and the black strappy sandals, one hand on her knee and the other arm along the bench back, nothing covering her waist |
| 3. 身體朝向 | 側面（朝畫面左）：側坐在長椅上，身體側面朝畫面左；雙腿交疊、伸向畫面左側，直角肩與背脊挺直，一手臂搭在椅背上 | sitting sideways on the bench, her body side-on to the camera, facing camera-left, her legs crossed and reaching toward camera-left, her straight shoulders and back upright, one arm along the bench back |
| 4. 臉部朝向與視線 | 三分之二側臉，看向畫面左側的湖面與遠岸（不看鏡頭） | her face in a three-quarter view, looking out over the lake toward the far shore on camera-left, away from the camera |
| 5. 相機高度與俯仰 | 相機在她坐姿時的腰部高度，平視（參考：70mm 鏡頭、約 5.4 公尺；畫面中心與相機高度差換算俯仰約 -0.1 度） | camera at her seated waist height, level |
| 6. 畫面配置 | 人物在中央偏右；身體與交疊的腿朝左、面向湖面，左側留給湖面與視線，右側是延伸的木平台與遠岸樹林，背景簡潔 | she sits just right of centre facing the lake on the left, leaving space on the left for the water and her gaze, the deck and the far tree line soft on the right |
| 7. 攝影目的 | 側坐把直角肩、上背、收腰與交疊的長腿拉成乾淨的線條；看向湖面的三分之二側臉帶出初秋的冷靜感 | sitting sideways draws her straight shoulders, bare upper back, cinched waist and long crossed legs into clean lines, and the three-quarter face toward the lake carries a calm early-autumn mood |

**選擇理由：** Penny 只問衣服和場景有沒有搭：湖畔木平台、臨水長椅、側坐、雙腿交疊、看湖面與相機都照 R4；只把晚宴感的黑色單肩鏤空洋裝換成適合湖畔傍晚的深酒紅細針織繞頸短洋裝。頭轉回約55度成三分之二側臉，仍能認人。

**R7：** 已接受（R7 owner 紀錄）：服裝、場景、表情、姿態、攝影與 prompt 照 R6 版本，不再要求回覆。

**R6 改了什麼（歷史）：** 依 Penny「他這個衣服跟場景有搭嗎？」與主管判斷：湖畔木平台、臨水長椅、側坐、雙腿交疊、看湖面與相機都保留；偏晚宴的黑色單肩鏤空中長洋裝改為深酒紅細針織繞頸合身短洋裝（露肩與上背、收腰、裙長大腿中段、沒有運動元素或大型圖案）；鞋與配件維持簡單。

**R4 改了什麼（歷史）：** 撤回美術館與畫作背景：改為初秋傍晚的湖畔木平台與臨水長椅；黑色單肩鏤空洋裝保留，加側開衩、鞋改低跟細帶涼鞋（木平台上較合理）；姿勢由側身站改為側坐、雙腿交疊；景別由全身改為坐姿全身；視線看向湖面。

| 項目 | 內容 |
|---|---|
| 場景 | 初秋傍晚安靜的湖畔：延伸到水面上的淺色木平台、一張簡潔的木製長椅，平靜的湖面映著低斜的陽光，遠岸是開始轉黃的樹林，畫面沒有其他人。 |
| 服裝 | 洋裝：深酒紅細針織繞頸合身短洋裝（露肩與上背、腰部明確收窄、裙長大腿中段；細緻針織，沒有運動元素或大型圖案）；鞋：黑色細帶低跟涼鞋；配件：小銀色圈耳環 |
| 髮型 | 冷灰藍黑長髮，一側塞在耳後露出薄荷綠內層。 |
| 妝感 | 水光無妝感、淡棕眼線、漸層唇。 |
| 身材設定（數字） | 168 cm／85-58-90／C（直角肩、長腿） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 繞頸剪裁露出直角肩與上背，合身細針織在腰部明確收窄；側坐、雙腿交疊，裙長在大腿中段，呈現 168 cm 的長腿線條（C 罩杯，寫成纖細）。 |
| 主光 | 她身後偏低的初秋傍晚陽光，頭髮與肩線一圈暖色輪廓 |
| 補光 | 畫面外前方大反光板，臉清楚 |
| 姿態 | 側坐在湖畔長椅上，雙腿交疊。 |
| 手的位置 | 靠鏡頭的手輕放在交疊的膝上，另一手手臂搭在長椅椅背上（不遮腰線）。 |
| 表情 | 冷靜、若有所思的淺笑 |
| 視線 | 看向畫面左側的湖面與遠岸（不看鏡頭） |
| 焦段／距離／視野（參考） | 16:9，70mm，約 5.4 公尺，視野 2.78×1.56 公尺；人物約佔畫面高度 85%（規劃）；相機約 0.69 公尺高、畫面中心約 0.67 公尺高，俯仰約 -0.1 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 8%（套框後理論約 6.7%）；下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%）；不能切：髮頂、臉、入鏡的雙手、雙腳與鞋；規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | 主管判斷原本的黑色單肩鏤空中長洋裝偏晚宴感，和普通湖畔長椅不夠搭；改成日常外出也合理的深酒紅細針織繞頸短洋裝：秋天的材質與顏色和湖畔傍晚更協調，露肩、上背與收腰仍保留她俐落的線條。實景、不棚拍、不運動、不晚宴。 |
| 與同一人另一款的差異 | 直式款是玻璃溫室、白色立領短上衣＋薄荷綠緞面高腰窄裙、斜側站姿看鏡頭；這款是戶外湖畔、深酒紅細針織繞頸短洋裝、側坐長椅、望向湖面。和 2 月 H-Rin 的酒紅緞面同色系，但材質（針織對緞面）、場景（湖畔對飯店套房）、姿勢（側坐對斜躺）與月份都分開。 |
| 參考照片（用途） | jia-08：身分（夜晚穿搭與認臉；回頭姿勢不採用；沒有這件深酒紅針織洋裝的參考圖）；jia-02：表情（冷靜的表情；室內背景不採用） |
| 月份（已確認） | 9 月（初秋） |

| 風險 | 處理 |
|---|---|
| 長椅與湖景搶戲 | 人物佔畫面主要高度、背景只有水面與遠樹 |
| 逆光臉暗 | 前方大反光板 |
| 短裙坐下時遮蔽不明 | 寫明裙長在大腿中段、雙腿交疊、完整遮蔽 |
| 細高跟卡進木板縫 | 低跟細帶涼鞋 |
| 針織變成厚毛衣或運動感 | 寫明細針織、合身、沒有運動元素或大型圖案 |
| 與 H-Rin 酒紅撞色 | 材質、場景、姿勢與月份分開 |
| 碰撞紀錄（Miu、Somi） | 冷色髮與薄荷內層；不改臉、不宣稱能消除 |

prompt 草稿（16:9，尚未執行）：

```text
A 22-year-old adult Korean woman with her natural fair, cool-toned skin, a small face, straight shoulders and long narrow upturned eyes, dewy no-makeup makeup with a soft brown liner and gradient lips, long cool blue-black hair tucked behind one ear so its mint-green inner layer shows. Slim, long-legged figure with soft feminine curves, 168 cm tall, bust 85 cm, waist 58 cm, hips 90 cm, C cup, a slim waist and long legs. She wears a deep wine-red fine-knit fitted halter mini dress that leaves her shoulders and upper back bare, drawn in clearly at the waist, the hem at mid-thigh, a smooth fine knit with no athletic details and no large patterns, black strappy low-heeled sandals and small silver hoop earrings. Setting: a quiet lakeside on an early-autumn evening, a pale wooden deck reaching over the water, a simple wooden bench at its edge, calm water holding the low sunlight, a far shore of trees just turning yellow, nobody else in sight. One hand rests lightly on her crossed knee and the other arm lies along the bench back, clear of her waist; she has a cool, thoughtful half-smile. Shot: a full-length seated shot, her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the bare shoulders and upper back of the halter cut, the fitted knit drawn in at her waist, the hem at mid-thigh, her long crossed legs and the black strappy sandals, one hand on her knee and the other arm along the bench back, nothing covering her waist. Body: sitting sideways on the bench, her body side-on to the camera, facing camera-left, her legs crossed and reaching toward camera-left, her straight shoulders and back upright, one arm along the bench back. Face and gaze: her face in a three-quarter view, looking out over the lake toward the far shore on camera-left, away from the camera. Camera: horizontal 16:9 frame, full-frame camera with a 70mm lens from about 5.4 metres, camera at her seated waist height, level, natural perspective without distortion; she fills about 85% of the frame height. Composition: she sits just right of centre facing the lake on the left, leaving space on the left for the water and her gaze, the deck and the far tree line soft on the right. Emphasis: sitting sideways draws her straight shoulders, bare upper back, cinched waist and long crossed legs into clean lines, and the three-quarter face toward the lake carries a calm early-autumn mood. Lighting: low early-autumn evening sun behind her draws a warm rim along her hair and shoulders; a large white reflector just out of frame in front keeps her face clear; deep wine red, soft lake blue-grey and warm gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.12 H-yerin-han｜Yerin｜橫式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 春日球場的白色球車，白色無袖針織 polo＋淺藍百褶高爾夫迷你裙，坐在座椅邊緣微微後靠、伸長雙腿的俏皮笑容。

**攝影：** 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 坐姿全身 | a full-length seated shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，坐姿的雙腿與雙腳完整。入鏡：完整坐姿；白色無袖 polo 的胸型與手臂線條、百褶迷你裙、併攏交叉的長腿與白色高爾夫鞋；撐在座椅上的手與放在膝上的手 | her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the sleeveless polo over her full chest and her toned arms, the pleated mini skirt, her long legs together with ankles crossed and the white golf shoes, one hand braced on the seat and the other on her knees |
| 3. 身體朝向 | 約45度斜側（朝畫面左）：側坐在球車前座的邊緣、身體微微往後靠，身體朝畫面左轉約45度；伸出車外的長腿斜向畫面左下，雙膝併攏、腳踝交叉、腳尖點地，肩線放鬆 | sitting sideways on the edge of the golf cart front seat and leaning back slightly, her body turned about 45 degrees toward camera-left, her long legs reaching out of the cart toward the lower left with her knees together, ankles crossed and toes touching the ground, shoulders relaxed |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她坐姿時的腰部高度，平視（參考：50mm 鏡頭、約 4.5 公尺；畫面中心與相機高度差換算俯仰約 -0.7 度） | camera at her seated waist height, level |
| 6. 畫面配置 | 白色球車斜放在畫面中、車頭朝左；她坐在中央偏右的車門開口，伸出的長腿沿對角線指向左下，後方是亮綠球道 | the white golf cart sits at an angle across the frame with its front toward the left; she sits just right of centre in the open side of the cart, her long legs reaching diagonally toward the lower left, the bright green fairway behind |
| 7. 攝影目的 | 球車的對角線把 170 公分的長腿帶進畫面，微微後靠的坐姿讓身體線條更放鬆；重點是笑容與腿長，不打球 | the diagonal of the cart carries her long legs into the frame and the slight lean back relaxes her body lines; the focus is her smile and leg length |

**選擇理由：** 保留高爾夫迷你裙裝與球車；坐姿寫清楚身體與腿的方向、腳踝、雙手支撐；相機在坐姿腰部高度平視，不俯拍縮腿、不用胯下仰拍。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 保留高爾夫迷你裙裝與球車；坐姿改為坐在座椅邊緣、身體微微後靠、後手撐座椅、前手放膝上，雙膝併攏、腳踝交叉、腳尖點地；相機維持坐姿腰部高度平視，不俯拍、不低角度。

| 項目 | 內容 |
|---|---|
| 場景 | 晴朗春日早晨的高爾夫球場：一台素面白色球車停在車道旁，旁邊是亮綠的球道，遠方柔和的樹林，球場上沒有其他人。 |
| 服裝 | 上身：白色無袖貼身針織高爾夫 polo；下身：淺天空藍百褶高爾夫迷你裙；鞋：白色高爾夫鞋；配件：素面白色球帽、小金色耳針 |
| 髮型 | 亞麻棕長髮、臉側金色挑染，低馬尾從球帽後方穿出。 |
| 妝感 | 防曬淡妝、亮色唇。 |
| 身材設定（數字） | 170 cm／90-60-93／E（健康曲線） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 無袖貼身 polo 呈現 E 罩杯胸型與手臂線條；坐在座椅邊緣微微後靠，伸出車外的長腿斜向畫面左下，雙膝併攏、腳踝交叉，呈現 170 cm 的腿長。 |
| 主光 | 左前上方的晴朗晨光 |
| 補光 | 畫面外大反光板，柔化帽簷下臉上的陰影 |
| 姿態 | 側坐在球車前座的邊緣，身體微微往後靠。 |
| 手的位置 | 後方的手撐在臀部後方的座椅上，前方的手輕放在併攏的膝上。 |
| 表情 | 俏皮、明亮的笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，50mm，約 4.5 公尺，視野 3.24×1.82 公尺；人物約佔畫面高度 83%（規劃）；相機約 0.84 公尺高、畫面中心約 0.78 公尺高，俯仰約 -0.7 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 印刷（工作照片框） | 橫式工作照片框（R6 已接受）（192×104 mm）；比例計算：16:9 放入要裁掉高度 4 mm（約 3.7%），左右不裁；規劃上下各約 2 mm，實際分配依實圖；上緣：規劃髮頂留白約 10%（套框後理論約 8.4%）；下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%）；不能切：髮頂、臉、入鏡的雙手、雙腳與鞋；規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi；規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證 |
| 為何符合人設 | 性感可愛的高爾夫形象寫真：重點是坐姿伸長的腿與笑容；雙膝併攏、相機在側前方的坐姿腰部高度平視，不從低處往上拍，也不以裙下為構圖目的；不拿球桿、不打球。 |
| 與同一人另一款的差異 | 直式款是日落海灘、白色背心洋裝、赤腳站在浪花邊；這款是球場球車、polo＋百褶裙＋球帽、坐姿伸長雙腿。 |
| 參考照片（用途） | yerin-01：服裝材質（白帽＋白 polo 的高爾夫穿搭）；yerin-05：服裝材質（polo＋百褶球裙的比例；俯身動作不採用） |
| 月份（已確認） | 5 月（春） |

| 風險 | 處理 |
|---|---|
| 裙下構圖 | 雙膝併攏、相機在側前方的坐姿腰部高度平視，不用低角度 |
| 俯拍把腿縮短 | 相機不高於她的坐姿腰部、平視 |
| 球車或衣帽出現品牌標誌 | 寫素面 |
| 帽簷陰影遮臉 | 反光板補光 |
| 碰撞紀錄（Rin） | 明亮戶外清新色 vs Rin 的深色；不改臉 |

prompt 草稿（16:9，尚未執行）：

```text
A 26-year-old adult Korean woman with her natural fair skin tone, bright defined features and a wide open smile, light sun-protective makeup and a bright lip, long flax-brown hair with golden face-framing highlights in a low ponytail pulled through the back of a plain white cap. Curvy athletic figure with soft feminine lines, 170 cm tall, bust 90 cm, waist 60 cm, hips 93 cm, E cup, long legs and a slim waist. She wears a white fitted sleeveless knit golf polo that follows her full chest and slim waist, a pale sky-blue pleated golf mini skirt, white golf shoes, a plain white cap and small gold stud earrings. Setting: a golf course on a clear spring morning, a plain white golf cart parked on the cart path beside a bright green fairway, soft trees in the distance, the course empty. Her back hand is braced on the seat behind her hip and her front hand rests lightly on her knees; she gives a playful, bright smile. Shot: a full-length seated shot, her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the sleeveless polo over her full chest and her toned arms, the pleated mini skirt, her long legs together with ankles crossed and the white golf shoes, one hand braced on the seat and the other on her knees. Body: sitting sideways on the edge of the golf cart front seat and leaning back slightly, her body turned about 45 degrees toward camera-left, her long legs reaching out of the cart toward the lower left with her knees together, ankles crossed and toes touching the ground, shoulders relaxed. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 4.5 metres, camera at her seated waist height, level, natural perspective without distortion; she fills about 83% of the frame height. Composition: the white golf cart sits at an angle across the frame with its front toward the left; she sits just right of centre in the open side of the cart, her long legs reaching diagonally toward the lower left, the bright green fairway behind. Emphasis: the diagonal of the cart carries her long legs into the frame and the slight lean back relaxes her body lines; the focus is her smile and leg length. Lighting: clear morning sun from high front-left, a large white reflector just out of frame softening the shadow of the cap on her face; bright green, sky blue and white tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.13 V-iris-chen｜Iris｜直式款（新企劃｜已接受（R4 owner 紀錄））

**一句話：** 黃金時段的河濱草地，白色方領短上衣配牛仔迷你裙，正面站著甜笑（Penny 指定的穿搭）。

**攝影：** 大腿中段以上｜正面｜臉正面・看鏡頭｜胸口高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 大腿中段以上 | a mid-thigh-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在大腿中段，不切在膝蓋。入鏡：白色方領短上衣、露出的腰、整條牛仔迷你裙與大腿上段；插腰的手與碰頭髮的手 | from a little above her head down to mid-thigh, well above the knees, showing the square-neck crop top, her bare waist, the whole denim mini skirt and her upper thighs, one hand on her hip and the other at her hair |
| 3. 身體朝向 | 正面：站姿，重心在一隻腳；身體正對鏡頭，肩線放平放鬆，臀部隨重心微微偏向一側 | standing with her weight on one leg, her body square to the camera, shoulders level and relaxed, her hips shifted slightly to one side |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她胸口高度，平視（參考：85mm 鏡頭、約 2.9 公尺；畫面中心與相機高度差換算俯仰約 -0.1 度） | camera at her chest height, level |
| 6. 畫面配置 | 人物置中；頭頂上方少量留白，兩側是柔焦的草地與樹林，夕陽輪廓光落在頭髮與肩線 | she is centred with a little space above her head and the soft lawn and trees on both sides |
| 7. 攝影目的 | 放大 Penny 指定的穿搭：短上衣的胸型、露腰與牛仔迷你裙，加上明亮的笑容 | Penny's chosen outfit up close, the crop top on her chest, her bare waist and the denim mini skirt, with her bright smile |

**選擇理由：** 直式是首張試拍候選：大腿中段以上讓穿搭與笑容最清楚，又保留腰臀比例；胸口高度平視不變形。

**R7：** 已接受（R4 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R5：** 主管核可的中英同步（R5）：英文 prompt 在身分句後補一句中文「妝感」已寫的內容；服裝、場景、表情、姿態、攝影與身分都不變，接受狀態沿用。補上的句子：`Fresh, light everyday makeup with a natural lip colour.`

| 項目 | 內容 |
|---|---|
| 場景 | 台北河濱公園的開闊草地，傍晚太陽低，遠處柔綠樹林與低矮公寓，草地與小徑空無一人。 |
| 服裝 | 上身：白色貼身羅紋方領短袖短上衣（露腰）；下身：淺藍高腰牛仔迷你裙；鞋：白色低筒帆布鞋（不入鏡）；配件：小金色圈耳環 |
| 髮型 | 黑色柔順直髮自然垂放過肩。 |
| 妝感 | 乾淨的日常妝、自然唇色。 |
| 身材設定（數字） | 162 cm／87-58-90／D |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身方領短上衣清楚呈現 D 罩杯胸型、露出細腰；高腰牛仔迷你裙強調腰臀比與腿長。 |
| 主光 | 她身後側方的低角度夕陽，頭髮與肩線一圈暖色輪廓光 |
| 補光 | 畫面外前方的大反光板加柔光，臉與身體均勻 |
| 姿態 | 站在草地上。 |
| 手的位置 | 一手插腰，一手輕碰太陽穴旁的頭髮。 |
| 表情 | 明亮溫暖的笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 2.9 公尺，視野 0.82×1.09 公尺；頭頂上方留白約 8%（規劃）；相機約 1.19 公尺高、畫面中心約 1.18 公尺高，俯仰約 -0.1 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 8%；下緣：規劃裁切線在大腿中段；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | Penny 的回饋：更顯身材的上衣＋牛仔迷你裙、身體面向鏡頭、專業姿態、有笑容；保留她喜歡的 iris-04 夕陽草地氛圍。 |
| 與同一人另一款的差異 | 橫式款在夏日上午的岩岸海灣、向日葵黃馬甲短上衣＋低腰迷你裙、正面全身；這款在河濱草地、白上衣＋牛仔迷你裙、逆光。 |
| 參考照片（用途） | iris-04：場景（草地、夕陽光線氛圍（Penny 喜歡的照片）；不採用回頭姿勢）；iris-06：服裝材質（白短上衣＋牛仔短裙的穿搭方向） |
| 月份（已確認） | 9 月（夏末初秋） |

| 風險 | 處理 |
|---|---|
| 逆光臉暗 | 寫明反光板與柔光補臉 |
| 膚色被夕陽拍偏 | 只寫一次她原本的白皙膚色 |
| 碰頭髮的手指融合 | 生成後放大檢查；不行改成兩手插腰 |

prompt 草稿（3:4，尚未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a round sweet face with large bright double-eyelid eyes and full lips, black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, a full chest, a slim waist and rounded hips. Fresh, light everyday makeup with a natural lip colour. She wears a fitted white ribbed square-neck short-sleeve crop top that shows the shape of her chest and her bare waist, a high-waisted light-blue denim mini skirt and small gold hoop earrings. Setting: an open riverside lawn in a Taipei park in the late afternoon, soft green trees and low distant apartment blocks far behind her, the lawn and the path empty. One hand rests on her hip and the other lightly touches her hair at her temple; she smiles brightly and warmly. Shot: a mid-thigh-up shot, from a little above her head down to mid-thigh, well above the knees, showing the square-neck crop top, her bare waist, the whole denim mini skirt and her upper thighs, one hand on her hip and the other at her hair. Body: standing with her weight on one leg, her body square to the camera, shoulders level and relaxed, her hips shifted slightly to one side. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 2.9 metres, camera at her chest height, level, natural perspective without distortion. Composition: she is centred with a little space above her head and the soft lawn and trees on both sides. Emphasis: Penny's chosen outfit up close, the crop top on her chest, her bare waist and the denim mini skirt, with her bright smile. Lighting: the low sun behind her and to one side draws a warm rim along her hair and shoulders; a large white reflector and a soft fill light just out of frame in front of her light her face and body evenly; warm golden tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.14 V-luna-tanaka｜Luna｜直式款（新企劃｜已接受（R4 owner 紀錄））

**一句話：** 紫陽花盛開的町家庭院，鼠尾草綠馬甲感洋裝，正面站在石板路上。

**攝影：** 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到涼鞋完整；有骨架的心形領上身、微蓬迷你裙、雙腿與米色低跟涼鞋；雙手交握在身後，胸腰線完整露出 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to sandals, the boned sweetheart bodice, the flared mini skirt and her legs, with both hands clasped behind her back so her chest and waist stay clear |
| 3. 身體朝向 | 正面：站在石板小徑上，重心在一隻腳、另一膝微彎；身體正對鏡頭，雙手在身後讓肩膀自然往後打開 | standing on the stone path with her weight on one leg and the other knee softly bent, her body square to the camera, her shoulders drawn gently back by her hands behind her |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她膝蓋高度，輕仰（參考：85mm 鏡頭、約 4.9 公尺；畫面中心與相機高度差換算俯仰約 +4.2 度） | camera at her knee height, tilted slightly upward |
| 6. 畫面配置 | 人物略偏左（約四成處）；石板路從她腳邊往右後方彎進庭院、經過紫陽花，楓枝橫過上緣；人物佔畫面高度約八成五 | she stands slightly left of centre, the stone path curving away behind her to the right past the hydrangeas, maple branches across the top edge |
| 7. 攝影目的 | 較低的相機輕仰讓 155 公分的她腿更修長；全身呈現有骨架上身塑出的胸腰比例與整件洋裝 | a slightly low camera lengthens her petite legs, and the full figure shows how the boned bodice shapes her chest and waist and the whole dress |

**選擇理由：** 嬌小的 Luna 用膝蓋高度輕仰拍全身，比例更修長；雙手在身後讓胸腰線完全不被遮住。與橫式款的秋季和服（約30度斜側、臀部高度平視）不同。

**R7：** 已接受（R4 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

| 項目 | 內容 |
|---|---|
| 場景 | 京都風老町家的後院：青苔地、石板小徑、木籬笆旁一整排白色紫陽花，頭上有楓樹枝。 |
| 服裝 | 洋裝：淺鼠尾草綠棉質洋裝，心形領、有骨架的貼身上身、微蓬迷你裙；鞋：米色低跟繫帶涼鞋；配件：細金手鍊 |
| 髮型 | 黑色細直髮，中分下巴長度的鮑伯。 |
| 妝感 | 柔和自然妝、玫瑰色唇。 |
| 身材設定（數字） | 155 cm／88-56-87／E（童顏與曲線的反差） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 心形領與有骨架的上身塑出飽滿胸型與細腰；雙手放身後讓胸腰線完整露出。 |
| 主光 | 明亮陰天的大面積柔光 |
| 補光 | 畫面外白色反光板；光斑只落在背景 |
| 姿態 | 站在石板小徑上。 |
| 手的位置 | 雙手輕輕交握在身後。 |
| 表情 | 溫柔的微笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 4.9 公尺，視野 1.38×1.84 公尺；人物約佔畫面高度 86%（規劃）；相機約 0.47 公尺高、畫面中心約 0.83 公尺高，俯仰約 +4.2 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 9%；下緣：規劃雙腳與鞋下方留白約 5%；不能切：髮頂、臉、入鏡的雙手、雙腳與鞋；規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | 保留 Penny 沒有否定的紫陽花庭院，換成真正顯身材的剪裁。 |
| 與同一人另一款的差異 | 橫式款是秋天的當代日式宅邸庭院、藕粉秋草紋和服、約30度斜側站姿、臀部高度平視；這款是初夏的京都老町家後院、白色紫陽花、綠色馬甲洋裝、正面站姿全身、膝蓋高度輕仰。 |
| 參考照片（用途） | luna-10：表情（Penny 喜歡的表情與柔光；不作身材參考：既有照片的身材不符合設定（Penny））；luna-01：場景（京都巷弄氛圍；不作身材參考：既有照片的身材不符合設定（Penny）） |
| 月份（已確認） | 6 月（初夏（梅雨季紫陽花）） |

| 風險 | 處理 |
|---|---|
| 童顏＋花園顯小 | 寫明 adult、成熟剪裁與首飾 |
| 光斑落在臉上 | 寫明光斑只在背景 |
| 地名生出錯的地標 | 只寫環境元素 |

prompt 草稿（3:4，尚未執行）：

```text
A 20-year-old adult Japanese woman with her natural fair skin tone, large round dark-brown eyes and soft natural makeup with a rosy lip, black fine straight hair in a centre-parted, chin-length bob. Petite figure with a noticeably full chest and a slim waist, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup. She wears a pale sage-green cotton sundress with a sweetheart neckline, a fitted boned bodice that shapes her full chest and narrow waist and a softly flared mini skirt, cream low block-heel strappy sandals and a thin gold bracelet. Setting: a quiet garden behind an old wooden Kyoto-style townhouse, moss ground, a stone path, white hydrangeas in bloom along a low wooden fence, maple branches overhead. Both hands are clasped lightly behind her back; she smiles gently. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to sandals, the boned sweetheart bodice, the flared mini skirt and her legs, with both hands clasped behind her back so her chest and waist stay clear. Body: standing on the stone path with her weight on one leg and the other knee softly bent, her body square to the camera, her shoulders drawn gently back by her hands behind her. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 4.9 metres, camera at her knee height, tilted slightly upward, natural perspective without distortion; she fills about 86% of the frame height. Composition: she stands slightly left of centre, the stone path curving away behind her to the right past the hydrangeas, maple branches across the top edge. Emphasis: a slightly low camera lengthens her petite legs, and the full figure shows how the boned bodice shapes her chest and waist and the whole dress. Lighting: bright overcast daylight as one large soft source, with a white reflector just out of frame so her face is clean and evenly lit; soft dappled light falls only on the hydrangeas and path behind her; fresh green, white and sage tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.15 V-somi-oh｜Somi｜直式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 下雪的溫泉小鎮夜晚，象牙白貼身針織洋裝外披紅色長大衣，抬眼看著燈籠旁飄落的雪，自然地笑開。

**攝影：** 全身｜正面｜三分之二側臉・不看鏡頭：看畫面右上方燈籠旁飄落的雪｜臀部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到靴底完整；敞開的紅色長大衣、貼身白色針織洋裝的胸腰臀線條、白色及膝長靴；插在口袋的手與在肩高接雪的手（不遮臉） | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to boots, the open red coat, the fitted ivory knit dress over her chest, waist and hips, and the white knee-high boots, one hand in a coat pocket and the other raised at shoulder height catching snow, away from her face |
| 3. 身體朝向 | 正面：站在薄雪上，重心在後腳、前腳微微向前；身體正對鏡頭，下巴微抬、肩線放鬆，敞開的大衣自然垂下 | standing on the thin snow with her weight on her back leg and her front foot slightly forward, her body square to the camera, her chin lifted slightly and shoulders relaxed, the open coat falling naturally |
| 4. 臉部朝向與視線 | 三分之二側臉，看向畫面右上方燈籠旁飄落的雪（不看鏡頭） | her face in a three-quarter view, looking up toward the snow falling beside a lantern at the upper right, away from the camera |
| 5. 相機高度與俯仰 | 相機在她臀部高度，平視（參考：70mm 鏡頭、約 4.2 公尺；畫面中心與相機高度差換算俯仰約 -0.0 度） | camera at her hip height, level |
| 6. 畫面配置 | 人物略偏左（約四成）；右上方是發光的紙燈籠與飄落的雪，留給她的視線，溫泉街往右後方延伸；人物佔畫面高度約八成五 | she stands slightly left of centre, the glowing paper lanterns and falling snow at the upper right where she is looking, the street receding behind her to the right |
| 7. 攝影目的 | 不看鏡頭、抬眼看雪的自然笑容讓畫面像抓拍的寫真；全身保留冬季整體造型與洋裝曲線 | her natural smile as she looks up at the snow makes the picture feel like a captured moment, and the full figure keeps the whole winter look and the curves of the dress |

**選擇理由：** 保留雪夜溫泉小鎮與冬季穿搭；視線改成看向右上方燈籠旁的雪，人物移到略偏左，右上方留給視線與燈籠。臉只微抬、三分之二側臉、眼睛睜開。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 保留雪夜溫泉小鎮與冬季穿搭；改為不看鏡頭：抬眼看向右上方燈籠旁飄落的雪，一手攤開接雪，笑容由情境帶出；臉是三分之二側臉、眼睛睜開，不仰頭到看不清五官；人物改到略偏左。

| 項目 | 內容 |
|---|---|
| 場景 | 小型溫泉小鎮的街道，冬夜飄雪；低矮木造旅館掛著暖色紙燈籠、路旁石溝冒出薄薄的蒸氣，地上一層薄雪，街上沒有人。 |
| 服裝 | 洋裝：象牙白貼身羅紋針織迷你洋裝（高圓領）；外套：紅色羊毛長大衣（敞開）；鞋：白色及膝長靴；配件：小珍珠耳環 |
| 髮型 | 明亮蜜橘棕的韓式狼尾層次剪。 |
| 妝感 | 淡妝、亮澤唇釉、凍紅的臉頰。 |
| 身材設定（數字） | 161 cm／91-58-90／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身羅紋針織洋裝清楚勾出 F 罩杯胸型、細腰與臀線；一手插口袋把大衣撐開，讓洋裝線條露出來。 |
| 主光 | 畫面外前左方的柔和暖色主光 |
| 補光 | 背後燈籠的暖光；雪地上的冷藍夜色 |
| 姿態 | 站在雪地上，抬眼看向燈籠旁飄落的雪。 |
| 手的位置 | 一手插在大衣口袋裡把大衣撐開，另一手在肩高攤開掌心接雪（不遮臉）。 |
| 表情 | 自然、帶點驚喜的笑，眼睛睜開 |
| 視線 | 看向畫面右上方燈籠旁飄落的雪（不看鏡頭） |
| 焦段／距離／視野（參考） | 3:4，70mm，約 4.2 公尺，視野 1.44×1.92 公尺；人物約佔畫面高度 85%（規劃）；相機約 0.87 公尺高、畫面中心約 0.86 公尺高，俯仰約 -0.0 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 10%；下緣：規劃雙腳與鞋下方留白約 5%；不能切：髮頂、臉、入鏡的雙手、雙腳與鞋；規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | 她的配色有「蒸氣白」與紅；不看鏡頭、抬眼看雪的笑容由情境自然帶出，比對鏡頭大笑更像寫真；臉是三分之二側臉、眼睛睜開，仍認得出她。 |
| 與同一人另一款的差異 | 橫式款是棚內暖橘小吃店、敞開短開襟＋小可愛＋短裙、對鏡頭大笑；這款是戶外雪夜、白色針織洋裝＋紅大衣＋長靴、看雪。 |
| 參考照片（用途） | somi-08：服裝材質（外套穿搭與身分）；somi-02：表情（月牙眼的笑） |
| 月份（已確認） | 12 月（冬） |

| 風險 | 處理 |
|---|---|
| 仰頭看不清五官 | 只微抬下巴、三分之二側臉、眼睛睜開 |
| 接雪的手遮臉 | 手在肩高、離開臉 |
| 雪夜臉暗或發灰 | 柔和暖色主光 |
| 燈籠或招牌出現文字 | 只寫素面紙燈籠、不寫招牌 |

prompt 草稿（3:4，尚未執行）：

```text
A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. Light makeup with a glossy lip, her cheeks flushed pink from the cold. She wears a fitted ivory ribbed knit mini dress with a high round neck that follows her full chest, slim waist and hips, a long red wool coat worn open, white knee-high boots and small pearl earrings. Setting: a quiet street in a small hot-spring town on a snowy winter evening, low wooden inns with warm paper lanterns, thin steam rising from a stone channel at the roadside, a light layer of snow on the ground, the street empty. One hand is in the pocket of the open coat holding it back so the fitted dress shows, and the other is raised at shoulder height with the palm up catching snowflakes, away from her face; her chin lifts slightly and she smiles with natural delight, eyes open, a few snowflakes in the air. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to boots, the open red coat, the fitted ivory knit dress over her chest, waist and hips, and the white knee-high boots, one hand in a coat pocket and the other raised at shoulder height catching snow, away from her face. Body: standing on the thin snow with her weight on her back leg and her front foot slightly forward, her body square to the camera, her chin lifted slightly and shoulders relaxed, the open coat falling naturally. Face and gaze: her face in a three-quarter view, looking up toward the snow falling beside a lantern at the upper right, away from the camera. Camera: vertical 3:4 frame, full-frame camera with a 70mm lens from about 4.2 metres, camera at her hip height, level, natural perspective without distortion; she fills about 85% of the frame height. Composition: she stands slightly left of centre, the glowing paper lanterns and falling snow at the upper right where she is looking, the street receding behind her to the right. Emphasis: her natural smile as she looks up at the snow makes the picture feel like a captured moment, and the full figure keeps the whole winter look and the curves of the dress. Lighting: a soft warm key light from front-left just out of frame lights her face evenly; the paper lanterns behind her glow warm amber against the cool blue evening light on the snow; red, ivory and warm amber tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.16 V-coco-wu｜Coco｜直式款（Penny 已接受的 v2 主方向｜已接受（R4 owner 紀錄））

**一句話：** Penny 已接受的方向：週末飯店泳池，薄荷綠比基尼＋淺紫透膚罩衫，坐在池邊大笑。

**攝影：** 坐姿到水面｜正面｜臉正面・看鏡頭｜坐姿時的胸口高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 坐姿到水面 | a seated shot down to the waterline |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在水面下一點，膝蓋與小腿上段入鏡。入鏡：比基尼上衣與下著、細腰、膝蓋與入水的小腿上段；撐在身後的雙手 | from a little above her head down to just below the waterline, her knees and the upper part of her lower legs showing, showing the bikini top and bottoms, her slim waist, her knees and the upper part of her lower legs in the water, with both hands braced behind her |
| 3. 身體朝向 | 正面：坐在池邊，兩條小腿泡在水裡；上身往後靠在撐地的雙手上，身體正對鏡頭，肩膀自然打開 | sitting on the pool edge with both lower legs in the water, leaning back on her hands, her body square to the camera, her shoulders open |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她坐姿時的胸口高度，平視（參考：70mm 鏡頭、約 2.7 公尺；畫面中心與相機高度差換算俯仰約 -0.8 度） | camera at her seated chest height, level |
| 6. 畫面配置 | 人物置中；池水橫在畫面下方，池畔石磚與收起的白色陽傘在後方（已接受的構圖） | she is centred, with the water across the bottom of the frame and the pool deck and folded umbrellas behind her |
| 7. 攝影目的 | 坐姿＋下方水面讓身體在直幅裡又大又完整，正面呈現比基尼的胸腰線條與大笑 | the seated pose and the water below keep her body large and complete in the vertical frame, showing the bikini, her chest and waist, and her laugh |

**選擇理由：** 已接受方向：姿勢、取景與焦段距離都照 v3；只把身體正面、臉正面、相機在坐姿胸口高度平視寫明。

**R7：** 已接受（R4 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R5：** 主管核可的中英同步（R5）：英文 prompt 在身分句後補一句中文「妝感」已寫的內容；服裝、場景、表情、姿態、攝影與身分都不變，接受狀態沿用。補上的句子：`Sweet, light makeup.`

| 項目 | 內容 |
|---|---|
| 場景 | 週末早上的度假飯店泳池：淺米色石材地磚、清澈的湖水綠池水、遠處收起的白色陽傘，池畔無人。 |
| 服裝 | 泳裝：薄荷綠羅紋三角比基尼上衣與同色側綁下著（完整遮蔽）；外搭：敞開的淺紫透膚短袖罩衫（落在肩後）；配件：白色雛菊髮夾、腳踝細金鍊（不入鏡） |
| 髮型 | 深棕長波浪捲髮、蓬鬆空氣瀏海，髮尾微濕。 |
| 妝感 | 甜美淡妝。 |
| 身材設定（數字） | 158 cm／89-56-86／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 比基尼呈現 E 罩杯胸型與細腰；往後撐的坐姿拉長身體線條。 |
| 主光 | 晚上午的陽光從左前上方 |
| 補光 | 畫面外大反光板；池水在腿上留下淡淡水光 |
| 姿態 | 坐在池邊、兩條小腿泡在水裡，身體往後。 |
| 手的位置 | 雙手撐在身後地上。 |
| 表情 | 歪頭、瞇眼大笑、酒窩 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，70mm，約 2.7 公尺，視野 0.93×1.23 公尺；人物約佔畫面高度 81%（規劃）；相機約 0.36 公尺高、畫面中心約 0.32 公尺高，俯仰約 -0.8 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 11%；下緣：規劃水面下方留白約 8%；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | Penny 接受的 v2 主方向；坐姿與下方水面在直幅裡讓身體更大、更清楚，所以建議放直式款。 |
| 與同一人另一款的差異 | 橫式款是花田、白色亞麻洋裝、站姿；這款是泳池、比基尼、坐姿。 |
| 參考照片（用途） | coco-21：表情（泳裝照的大笑；尺度同第二階段泳裝參考）；coco-20：身分（認臉與身形） |
| 月份（已確認） | 7 月（盛夏） |

| 風險 | 處理 |
|---|---|
| 泳裝遮蔽與走光 | 寫明完整遮蔽；交印前需確認廠商接受範圍 |
| 水下腳掌與撐地手指變形 | 生成後檢查 |

prompt 草稿（3:4，尚未執行）：

```text
A 20-year-old adult Taiwanese woman with her natural fair skin tone, deep dimples when she smiles and dark-brown long wavy hair with soft wispy bangs, the ends slightly wet. Petite curvy figure, 158 cm tall, bust 89 cm, waist 56 cm, hips 86 cm, E cup, full chest and slim waist. Sweet, light makeup. She wears a mint-green ribbed triangle bikini top with matching side-tie bottoms that fully cover, an open sheer lilac short-sleeve cover-up shirt resting off her shoulders and a white daisy hair clip. Setting: a resort hotel pool on a weekend morning, pale cream stone tiles, clear turquoise water, white umbrellas folded in the distance, the pool deck empty. She sits on the pool edge with both lower legs in the water, leaning back on her hands, head tilted, laughing with her eyes squeezed into crescents and dimples showing. Shot: a seated shot down to the waterline, from a little above her head down to just below the waterline, her knees and the upper part of her lower legs showing, showing the bikini top and bottoms, her slim waist, her knees and the upper part of her lower legs in the water, with both hands braced behind her. Body: sitting on the pool edge with both lower legs in the water, leaning back on her hands, her body square to the camera, her shoulders open. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with a 70mm lens from about 2.7 metres, camera at her seated chest height, level, natural perspective without distortion; she fills about 81% of the frame height. Composition: she is centred, with the water across the bottom of the frame and the pool deck and folded umbrellas behind her. Emphasis: the seated pose and the water below keep her body large and complete in the vertical frame, showing the bikini, her chest and waist, and her laugh. Lighting: bright late-morning sun from high front-left; a large white reflector just out of frame fills the shadows on her face and body so her face is evenly lit; the turquoise water adds soft aqua reflections on her legs; clear, fresh summer colours. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.17 V-mia-huang｜Mia｜直式款（新企劃｜已接受（R4 owner 紀錄））

**一句話：** 春夜的櫻花河岸步道，淺紫貼身露肩針織洋裝，站在花枝下甜笑。

**攝影：** 胸上｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜眼睛高度・輕俯

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 胸上 | a chest-up portrait |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在胸線下方、手肘上方。入鏡：露肩針織領口、肩頸線、鎖骨與胸型；碰花枝的手在肩旁，另一手自然垂下、不入鏡（裁在上臂，不在手肘） | from a little above her head down to just below her bust, above the elbows, showing the off-shoulder knit neckline, her shoulders, collarbones and chest, one hand touching a blossom branch beside her shoulder and the other arm relaxed below the frame |
| 3. 身體朝向 | 約30度斜側（朝畫面右）：站在低垂的花枝下，身體朝畫面右轉約30度，肩線放鬆、露肩領口平整 | standing under a low blossom branch, her body turned about 30 degrees toward camera-right, shoulders relaxed so the off-shoulder neckline sits evenly |
| 4. 臉部朝向與視線 | 三分之二側臉，看鏡頭 | her face in a three-quarter view, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她眼睛高度，輕俯（參考：85mm 鏡頭、約 1.5 公尺；畫面中心與相機高度差換算俯仰約 -4.5 度） | camera at her eye level, tilted slightly downward |
| 6. 畫面配置 | 人物略偏左；上緣與右上角有櫻花枝框住畫面，燈籠化成柔和光點；臉在畫面上三分之一 | she is slightly left of centre, blossom branches framing the top and upper right, the lanterns softened into warm bokeh, her face in the upper third |
| 7. 攝影目的 | 全組最近的一張：放大她的柔和眼妝、甜笑與露肩領口，櫻花與燈籠只作氛圍 | the closest shot of the set: her soft eye makeup, sweet smile and off-shoulder neckline, with blossoms and lanterns only as mood |

**選擇理由：** 24 套中唯一的胸上近景，放在表情最豐富的 Mia；她的身形由橫式款的大腿中段以上負責，所以這張不會大幅減少身材展示。眼睛高度輕俯是常見的美顏角度，不會變形。

**R7：** 已接受（R4 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

| 項目 | 內容 |
|---|---|
| 場景 | 春天夜晚的河岸步道，盛開的櫻花樹在頭上交錯，步道旁掛著柔和紙燈籠，步道空無一人。 |
| 服裝 | 洋裝：淺紫細針織貼身露肩迷你洋裝；鞋：白色及膝長靴（不入鏡）；配件：一側小珍珠髮夾、細銀耳環 |
| 髮型 | 灰棕色長髮鬆散大波浪，左側臉旁粉紅 money piece 挑染。 |
| 妝感 | 柔和動漫感眼妝、圓形腮紅、水光唇。 |
| 身材設定（數字） | 160 cm／91-57-88／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 露肩貼身針織洋裝勾出 F 罩杯胸型、細腰與臀線；及膝靴拉長腿部。 |
| 主光 | 畫面外左前方柔和暖色主光 |
| 補光 | 燈籠讓櫻花透出暖粉色，背後深藍夜空 |
| 姿態 | 站在低垂的花枝下。 |
| 手的位置 | 一手輕觸肩旁的花枝，另一手自然垂下、不入鏡。 |
| 表情 | 甜甜的微笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 1.5 公尺，視野 0.42×0.56 公尺；頭頂上方留白約 9%（規劃）；相機約 1.52 公尺高、畫面中心約 1.4 公尺高，俯仰約 -4.5 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 9%；下緣：規劃裁切線在胸線下方；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | 她是夜貓子，夜晚的櫻花與燈籠延續她的粉紫配色與「深夜」氣質，但完全是寫真場景。 |
| 與同一人另一款的差異 | 橫式款是夏日黃昏海邊碼頭、粉色緞面馬甲＋白裙；這款是春夜櫻花、淺紫針織洋裝＋長靴。 |
| 參考照片（用途） | mia-08：表情（開朗的笑）；mia-06：身分（認臉；畫面裡的帽 T 與貓不採用） |
| 月份（已確認） | 3 月（春） |

| 風險 | 處理 |
|---|---|
| 燈籠上出現文字 | 寫素面紙燈籠 |
| 夜景臉暗 | 寫明柔和主光 |
| 碰花枝的手指變形 | 生成後檢查 |

prompt 草稿（3:4，尚未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a soft round face with big expressive eyes, softly winged liner, rounded blush and glossy tinted lips, long ash-brown hair in loose waves with a pastel-pink money-piece highlight framing the left side of her face. Curvy figure, 160 cm tall, bust 91 cm, waist 57 cm, hips 88 cm, F cup, a full chest and a slim waist. She wears a lilac fitted fine-knit off-shoulder mini dress that follows her full chest, small pearl hair clips on one side and thin silver earrings. Setting: a riverside promenade at night in spring, cherry trees in full bloom arching overhead, soft plain paper lanterns hanging along the path, the path empty. One hand lightly touches a blossom branch beside her shoulder; she smiles sweetly. Shot: a chest-up portrait, from a little above her head down to just below her bust, above the elbows, showing the off-shoulder knit neckline, her shoulders, collarbones and chest, one hand touching a blossom branch beside her shoulder and the other arm relaxed below the frame. Body: standing under a low blossom branch, her body turned about 30 degrees toward camera-right, shoulders relaxed so the off-shoulder neckline sits evenly. Face and gaze: her face in a three-quarter view, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 1.5 metres, camera at her eye level, tilted slightly downward, natural perspective without distortion. Composition: she is slightly left of centre, blossom branches framing the top and upper right, the lanterns softened into warm bokeh, her face in the upper third. Emphasis: the closest shot of the set: her soft eye makeup, sweet smile and off-shoulder neckline, with blossoms and lanterns only as mood. Lighting: a soft warm key light from front-left just out of frame lights her face evenly; the lanterns give the blossoms a warm pink glow against a deep blue night sky; pink, lilac and deep blue tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.18 V-yuna-kim｜Yuna｜直式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 深秋的銀杏大道，奶油色毛呢短外套套裝配黑色長靴，停下腳步望向大道深處、手裡拿著一片銀杏葉。

**攝影：** 全身｜約30度斜側（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側銀杏大道的深處｜臀部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到靴底完整；毛呢短外套、高腰迷你裙、雙腿與黑色及膝長靴；拉包帶的手與拿銀杏葉的手 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to boots, the cropped tweed jacket, the high-waisted mini skirt, her legs and the black knee-high boots, one hand on the bag strap and the other holding a ginkgo leaf at her waist |
| 3. 身體朝向 | 約30度斜側（朝畫面右）：站在落葉人行道上，重心在後腳、前腳朝畫面右側輕踏；身體朝畫面右轉約30度，肩與臀同向 | standing on the leaf-covered sidewalk with her weight on her back leg and her front foot stepping lightly toward camera-right, her body turned about 30 degrees toward camera-right, shoulders and hips turned together |
| 4. 臉部朝向與視線 | 三分之二側臉，看向畫面右側銀杏大道的深處（不看鏡頭） | her face in a three-quarter view, looking down the avenue toward camera-right, away from the camera |
| 5. 相機高度與俯仰 | 相機在她臀部高度，平視（參考：85mm 鏡頭、約 5.3 公尺；畫面中心與相機高度差換算俯仰約 -0.3 度） | camera at her hip height, level |
| 6. 畫面配置 | 人物略偏左（約四成）；身體、腳步與視線都朝右，右側留出銀杏大道往遠方延伸的空間，兩側金黃銀杏框住畫面 | she stands slightly left of centre, her body, step and gaze toward the right where the ginkgo avenue recedes into the distance, golden trees framing both sides |
| 7. 攝影目的 | 全身斜側、看向大道深處的自然神情，讓毛呢套裝與長靴的造型像電影的一格，而不是打卡街拍 | the full-length oblique stance and her faraway look down the avenue make the tweed set and boots feel like a film still rather than a posed street snap |

**選擇理由：** 保留銀杏大道與毛呢套裝；視線改為看向右側大道深處，與身體、腳步同一個方向，右側留給視線；三分之二側臉仍能認人。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 保留銀杏大道與毛呢套裝；改為不看鏡頭：停下腳步望向右側大道深處，柔和若有所思的微笑；另一手改成指尖輕拿一片銀杏葉在腰側；不擺打卡姿勢。

| 項目 | 內容 |
|---|---|
| 場景 | 深秋安靜的住宅大道，兩旁金黃銀杏，人行道鋪滿落葉，低矮的現代建築在背景失焦，街上沒有人。 |
| 服裝 | 上身：奶油色毛呢短外套（無領、扣起、合身）；下身：同色高腰毛呢迷你裙；鞋：黑色及膝皮長靴；配件：小珍珠耳環、小黑色肩背包 |
| 髮型 | 深棕自然波浪、鎖骨長度、空氣感八字瀏海。 |
| 妝感 | 水光肌、眼妝為重點、珊瑚漸層唇。 |
| 身材設定（數字） | 168 cm／84-58-89／C（纖細長腿） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 合身短外套收在腰上、高腰迷你裙與及膝長靴拉長 168 cm 的腿部比例；斜側的腳步讓身形更修長。 |
| 主光 | 銀杏樹後方的低角度午後陽光，頭髮上一圈暖色輪廓 |
| 補光 | 畫面外前方大反光板 |
| 姿態 | 站在落葉人行道上，停下腳步望向大道深處。 |
| 手的位置 | 一手拉著肩上的包包背帶，另一手指尖輕拿一片銀杏葉停在腰側。 |
| 表情 | 柔和、若有所思的微笑 |
| 視線 | 看向畫面右側銀杏大道的深處（不看鏡頭） |
| 焦段／距離／視野（參考） | 3:4，85mm，約 5.3 公尺，視野 1.5×2.0 公尺；人物約佔畫面高度 87%（規劃）；相機約 0.92 公尺高、畫面中心約 0.9 公尺高，俯仰約 -0.3 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 8%；下緣：規劃雙腳與鞋下方留白約 5%；不能切：髮頂、臉、入鏡的雙手、雙腳與鞋；規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | 毛呢套裝、長靴、水光妝與銀杏的金黃——韓系美感落在穿搭、妝髮、逆光金黃與柔和底片色調上；看向大道深處的自然神情像電影的一格，不是打卡擺拍。 |
| 與同一人另一款的差異 | 橫式款是雪後白樺林、霧玫瑰針織＋灰色迷你裙＋白色羊羔毛短外套、看鏡頭；這款是深秋銀杏大道、毛呢套裝＋長靴、望向大道深處。 |
| 參考照片（用途） | yuna-11：場景（首爾街頭夕陽光線；回頭姿勢不採用）；yuna-03：表情（柔和近照與妝感） |
| 月份（已確認） | 11 月（深秋） |

| 風險 | 處理 |
|---|---|
| 背景出現招牌或文字 | 寫明低矮建築失焦、不寫店面 |
| 逆光臉暗 | 反光板 |
| 包包出現標誌 | 寫素面小包 |
| 不看鏡頭時臉太側 | 三分之二側臉 |

prompt 草稿（3:4，尚未執行）：

```text
A 21-year-old adult Korean woman with her natural fair skin tone, large bright double-eyelid eyes as the focus of her makeup, a dewy glass-skin finish and soft coral gradient lips, dark-brown natural wavy hair at collarbone length with airy curtain bangs. Slim, long-legged figure, 168 cm tall, bust 84 cm, waist 58 cm, hips 89 cm, C cup, a narrow waist and long legs. She wears a cream tweed cropped jacket, collarless and buttoned, fitted close to her chest and waist, a matching high-waisted tweed mini skirt, black knee-high leather boots, small pearl earrings and a small plain black shoulder bag. Setting: a quiet residential avenue in late autumn lined with golden ginkgo trees, fallen yellow leaves covering the sidewalk, low modern buildings softly out of focus, the street empty. One hand holds the strap of the bag at her shoulder and the other lightly holds a golden ginkgo leaf at her waist; her head tilts slightly with a soft, faraway smile. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to boots, the cropped tweed jacket, the high-waisted mini skirt, her legs and the black knee-high boots, one hand on the bag strap and the other holding a ginkgo leaf at her waist. Body: standing on the leaf-covered sidewalk with her weight on her back leg and her front foot stepping lightly toward camera-right, her body turned about 30 degrees toward camera-right, shoulders and hips turned together. Face and gaze: her face in a three-quarter view, looking down the avenue toward camera-right, away from the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 5.3 metres, camera at her hip height, level, natural perspective without distortion; she fills about 87% of the frame height. Composition: she stands slightly left of centre, her body, step and gaze toward the right where the ginkgo avenue recedes into the distance, golden trees framing both sides. Emphasis: the full-length oblique stance and her faraway look down the avenue make the tweed set and boots feel like a film still rather than a posed street snap. Lighting: low afternoon sun behind the ginkgo trees lights the leaves and draws a warm rim on her hair; a large white reflector just out of frame lights her face evenly; golden yellow, cream and black tones with a soft film-like finish. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.19 V-tammy-chou｜Tammy｜直式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 夜晚的大飯店大廳，白色西裝外套洋裝配素面黑色小手提包，一手拎包、一手插腰的自信笑容。

**攝影：** 大腿中段以上｜正面｜臉正面・看鏡頭｜腰部高度・輕仰

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 大腿中段以上 | a mid-thigh-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在大腿中段，不切在膝蓋。入鏡：深 V 翻領、金扣與腰帶、迷你裙擺與大腿上段；拎在臀側的小手提包與插腰的手，兩手都在框內 | from a little above her head down to mid-thigh, well above the knees, showing the deep V lapel, the gold buttons and belted waist, the mini skirt hem and her upper thighs, the small bag held at her hip and the other hand on her waist, both hands inside the frame |
| 3. 身體朝向 | 正面：站在大理石柱旁，重心在一隻腳；身體正對鏡頭，肩膀打開，臀部隨重心微微偏向拎包的一側 | standing beside a marble column with her weight on one leg, her body square to the camera, shoulders open, her hips shifted slightly toward the side holding the bag |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她腰部高度，輕仰（參考：70mm 鏡頭、約 2.3 公尺；畫面中心與相機高度差換算俯仰約 +3.5 度） | camera at her waist height, tilted slightly upward |
| 6. 畫面配置 | 人物置中；水晶吊燈的暖光在她頭頂上方，大理石柱在一側、白花在背景失焦 | she is centred, the warm crystal chandelier glowing above her head, a marble column at one side and the white flowers soft in the background |
| 7. 攝影目的 | 大腿中段以上加上輕仰，呈現她的自信、西裝洋裝勾出的胸腰比例與一只素面小包 | a closer frame with a slightly low camera that shows her confidence, how the blazer dress defines her chest and waist, and a small plain bag |

**選擇理由：** 大腿中段以上剛好收進拎在臀側的小包與插腰的手；正面配腰部高度輕仰，拍出大飯店夜晚的氣場。高跟鞋由橫式款全身呈現。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 加入素面黑色小手提包（不仿特定品牌）：一手拎包在臀側、一手插腰，包不遮胸腰；文案改正：這張是大腿中段以上，不再稱「全身照」；場景、服裝、景別、相機不變。

| 項目 | 內容 |
|---|---|
| 場景 | 夜晚大飯店的大廳：拋光大理石地板與柱子、頭頂溫暖的水晶吊燈、背景圓桌上一大盆白花，大廳沒有其他人。 |
| 服裝 | 洋裝：白色合身西裝外套式迷你洋裝（深 V 翻領、金色扣子、繫腰帶）；鞋：黑色尖頭細高跟鞋（不入鏡）；配件：金色垂墜耳環、素面黑色亮面小手提包（無任何標誌、不仿特定品牌） |
| 髮型 | 奶茶金棕大波浪長捲髮，臉側淺色 money piece 挑染。 |
| 妝感 | 閃粉眼影、果凍唇。 |
| 身材設定（數字） | 160 cm／90-57-89／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 深 V 翻領與腰帶勾出 E 罩杯胸型與細腰；小包拎在臀側、稍微離開身體，不遮胸腰。 |
| 主光 | 畫面外右前方柔光 |
| 補光 | 水晶吊燈的暖色環境光 |
| 姿態 | 站在大理石柱旁。 |
| 手的位置 | 一手拎著小手提包的短提把、包停在臀側稍微離開身體，另一手插腰。 |
| 表情 | 自信的笑容 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，70mm，約 2.3 公尺，視野 0.79×1.05 公尺；頭頂上方留白約 6%（規劃）；相機約 1.08 公尺高、畫面中心約 1.22 公尺高，俯仰約 +3.5 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 6%；下緣：規劃裁切線在大腿中段；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | 合身洋裝的高級感延續到夜晚飯店；加上一只素面小包讓造型更完整，也讓手有自然的事做；不仿任何品牌。 |
| 與同一人另一款的差異 | 橫式款是白天春日花園露台、熱粉針織洋裝、全身與高跟鞋；這款是夜晚飯店大廳、白色西裝洋裝、大腿中段以上、拎著小包。 |
| 參考照片（用途） | tammy-01：服裝材質（貼身洋裝的線條）；tammy-03：表情（較柔的表情） |
| 月份（已確認） | 1 月（年末） |

| 風險 | 處理 |
|---|---|
| 包包像特定品牌 | 寫素面、圓角、細短提把，不寫菱格、鏈條或任何金屬標誌 |
| 包遮住腰 | 拎在臀側、稍微離開身體 |
| 大廳出現其他人或招牌 | 寫明大廳無人、不寫招牌 |

prompt 草稿（3:4，尚未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, round almond eyes with visible aegyo-sal, shimmer eyeshadow and jelly-glossy lips, long voluminous big-wave hair in milk-tea golden brown with light money-piece highlights at the front. Curvy figure, 160 cm tall, bust 90 cm, waist 57 cm, hips 89 cm, E cup, a full chest and a slim waist. She wears a white tailored blazer mini dress with a deep V lapel, gold buttons and a belted waist that defines her full chest and slim waist, gold drop earrings and a small plain black patent top-handle bag without any logos. Setting: the lobby of a grand hotel at night, polished marble floor and columns, a warm crystal chandelier overhead, a large arrangement of white flowers on a round table in the background, the lobby empty. One hand holds the short handle of the small bag at her hip, slightly away from her body, and the other rests on her waist; she smiles confidently. Shot: a mid-thigh-up shot, from a little above her head down to mid-thigh, well above the knees, showing the deep V lapel, the gold buttons and belted waist, the mini skirt hem and her upper thighs, the small bag held at her hip and the other hand on her waist, both hands inside the frame. Body: standing beside a marble column with her weight on one leg, her body square to the camera, shoulders open, her hips shifted slightly toward the side holding the bag. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with a 70mm lens from about 2.3 metres, camera at her waist height, tilted slightly upward, natural perspective without distortion. Composition: she is centred, the warm crystal chandelier glowing above her head, a marble column at one side and the white flowers soft in the background. Emphasis: a closer frame with a slightly low camera that shows her confidence, how the blazer dress defines her chest and waist, and a small plain bag. Lighting: warm chandelier light fills the space; a soft key light from front-right just out of frame lights her face evenly; white, gold and warm marble tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.20 V-rin-ayase｜Rin｜直式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 秋日午後的安靜港灣石砌碼頭，墨綠仿麂皮裹身洋裝，倚著木頭繫船柱望向港口。

**攝影：** 膝上｜約45度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側港口的出口與海面｜腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：裹身洋裝的深 V 領、繫帶收出的胸腰線、前開衩露出的大腿到膝蓋下方；往後扶柱的手與放在繫帶上的手 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the deep V neckline of the wrap dress, the tie that defines her chest and waist, and her thigh through the front slit down to just below the knee, one hand reaching back to the post and the other at the tie on her waist |
| 3. 身體朝向 | 約45度斜側（朝畫面左）：背靠粗木繫船柱站著，身體朝畫面左轉約45度；重心在靠柱的那隻腳，另一膝微彎、腳尖點地，肩膀放鬆往後靠 | leaning back against a thick wooden mooring post, her body turned about 45 degrees toward camera-left, her weight on the leg nearer the post and the other knee softly bent with the toes touching the ground, shoulders relaxed against the post |
| 4. 臉部朝向與視線 | 三分之二側臉，看向畫面左側港口的出口與海面（不看鏡頭） | her face in a three-quarter view, looking out toward the harbour mouth on camera-left, away from the camera |
| 5. 相機高度與俯仰 | 相機在她腰部高度，平視（參考：85mm 鏡頭、約 3.6 公尺；畫面中心與相機高度差換算俯仰約 +0.7 度） | camera at her waist height, level |
| 6. 畫面配置 | 人物在中央偏右，身體與視線朝左側的港口出口，左側留給海面與停泊的帆船，繫船柱在她身後 | she stands just right of centre, her body and gaze turned toward the harbour mouth on the left, the water and moored white sailboats filling the space on the left, the mooring post behind her |
| 7. 攝影目的 | 倚柱的斜側站姿讓裹身洋裝的胸腰線與開衩腿線同時成立；望向港口的三分之二側臉帶出成熟、安靜的距離感 | leaning on the post at an angle shows both the chest and waist line of the wrap dress and the leg through the slit, and the three-quarter face toward the harbour brings a mature, quiet distance |

**選擇理由：** 最新意見取代先前選擇：撤回黑金吧台，改戶外秋日港灣，時間（秋天午後陰天）、環境（石砌碼頭與帆船）、服裝（墨綠麂皮）與角度（約45度斜側倚柱、看港口）都和其他海景拉開；膝上讓人物夠大。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 撤回黑金高級吧台（最新意見取代先前選擇）：改成秋日午後的安靜港灣石砌碼頭，服裝改為墨綠仿麂皮裹身洋裝（深 V、繫帶收腰、前開衩）＋深棕踝靴；髮型改為鬆低髮髻；景別由坐姿全身改為膝上；不看鏡頭、望向港口。

| 項目 | 內容 |
|---|---|
| 場景 | 秋天午後安靜的小港灣：石砌碼頭邊一根粗木繫船柱與盤起的麻繩，平靜的海面停著幾艘素面白色帆船，柔和的銀灰天光，站位在碼頭內側、離岸邊有距離，碼頭上沒有其他人。 |
| 服裝 | 洋裝：深墨綠仿麂皮裹身洋裝（深 V 領、繫帶收腰、及膝、前側開衩到大腿中段）；鞋：深棕色尖頭短跟踝靴（不入鏡）；配件：細金耳環、細金手鍊 |
| 髮型 | 深酒紅棕長髮，鬆鬆挽起的低髮髻，幾縷髮絲落在臉旁。 |
| 妝感 | 乾淨底妝、精準眼線、豆沙紅唇。 |
| 身材設定（數字） | 166 cm／92-58-90／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 裹身剪裁與繫帶收出 F 罩杯胸型與細腰；倚靠繫船柱時一膝微彎，前開衩露出大腿線條。 |
| 主光 | 柔和的秋日午後陰天光（大面積柔光） |
| 補光 | 畫面外前方反光板；水面的銀灰反光 |
| 姿態 | 背靠粗木繫船柱、斜側站著，一膝微彎、腳尖點地。 |
| 手的位置 | 一手往後輕扶在繫船柱上，一手輕放在腰間的繫帶上。 |
| 表情 | 平靜、帶點距離感的淺笑 |
| 視線 | 看向畫面左側港口的出口與海面（不看鏡頭） |
| 焦段／距離／視野（參考） | 3:4，85mm，約 3.6 公尺，視野 1.02×1.36 公尺；頭頂上方留白約 7%（規劃）；相機約 1.07 公尺高、畫面中心約 1.12 公尺高，俯仰約 +0.7 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 7%；下緣：規劃裁切線在膝蓋下方的小腿上段；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | 秋天的港灣與墨綠麂皮是她「深綠、酒紅、金」配色的戶外版本：成熟、安靜的性感，和橫式款的室內夕陽套房完全不同；不是酒吧、不是長禮服。 |
| 與同一人另一款的差異 | 橫式款是室內飯店套房夕陽、酒紅緞面、側躺；這款是戶外秋日港灣、墨綠麂皮裹身洋裝、倚柱站姿、望向港口。與其他海景拉開：Iris 是夏日上午的岩岸、Yerin 是夕陽沙灘、Mia 是黃昏遊樂碼頭；Rin 是秋天陰天的石砌港口與帆船。 |
| 參考照片（用途） | rin-04：表情（Penny 喜歡的成熟氣質）；rin-11：身分（戶外坐姿的身形比例；背景不採用） |
| 月份（已確認） | 10 月（秋） |

| 風險 | 處理 |
|---|---|
| 站在碼頭邊緣的危險站位 | 寫明站在碼頭內側、離岸邊有距離 |
| 帆船或碼頭出現文字 | 素面帆船、不寫船名與標示 |
| 陰天臉發灰 | 前方反光板 |
| 開衩遮蔽 | 開衩到大腿中段、裹身完整遮蔽 |
| 碰撞紀錄（Yerin） | 成熟深色 vs Yerin 的明亮清新；不改臉 |

prompt 草稿（3:4，尚未執行）：

```text
A 25-year-old adult Japanese woman with her natural fair, cool-toned skin, an oval face with long narrow eyes and a straight nose, a clean base with precise eyeliner and a muted rose-red lip, long deep wine-red brown hair pinned in a loose, soft low chignon with a few strands framing her face. Curvy figure, 166 cm tall, bust 92 cm, waist 58 cm, hips 90 cm, F cup, a full chest, a slim waist and long legs. She wears a deep forest-green faux-suede wrap dress with a deep V neckline, a tie at the waist that defines her full chest and slim waist, a knee-length hem and a front slit to mid-thigh, thin gold earrings and a thin gold bracelet. Setting: a quiet small harbour on an autumn afternoon, an old stone quay with a thick wooden mooring post and a coiled rope, a few plain white sailboats moored on calm water, soft silver-grey overcast light, standing well back from the quay edge, the quay empty. One hand reaches back to rest on the mooring post and the other rests at the tie on her waist; she has a calm, slightly distant half-smile. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the deep V neckline of the wrap dress, the tie that defines her chest and waist, and her thigh through the front slit down to just below the knee, one hand reaching back to the post and the other at the tie on her waist. Body: leaning back against a thick wooden mooring post, her body turned about 45 degrees toward camera-left, her weight on the leg nearer the post and the other knee softly bent with the toes touching the ground, shoulders relaxed against the post. Face and gaze: her face in a three-quarter view, looking out toward the harbour mouth on camera-left, away from the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.6 metres, camera at her waist height, level, natural perspective without distortion. Composition: she stands just right of centre, her body and gaze turned toward the harbour mouth on the left, the water and moored white sailboats filling the space on the left, the mooring post behind her. Emphasis: leaning on the post at an angle shows both the chest and waist line of the wrap dress and the leg through the slit, and the three-quarter face toward the harbour brings a mature, quiet distance. Lighting: soft overcast autumn afternoon light as one large gentle source, a white reflector just out of frame in front lighting her face evenly; silver-grey reflections on the water; deep green, silver-grey and soft gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.21 V-rainie-hsu｜Rainie｜直式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 雨後的夜晚街道，黑色緞面繞頸迷你洋裝外搭黑色長皮風衣，看向前方的街燈，放鬆、微啟唇的沉思神情。

**攝影：** 膝上｜約30度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側前方的街燈｜腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：繞頸緞面洋裝貼著胸腰臀、敞開的長風衣到膝蓋下方；拉著衣襟的手在腰間、另一手垂在大腿旁 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the satin halter dress over her chest, waist and hips and the long open coat down to just below the knees, one hand holding the coat edge at her waist and the other relaxed beside her thigh |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：站在濕亮的人行道上，身體朝畫面左轉約30度；重心在後腳、肩膀放鬆微微下沉，敞開的長風衣從肩線垂成直線 | standing on the wet pavement, her body turned about 30 degrees toward camera-left, her weight on her back leg and her shoulders relaxed and slightly lowered, the open coat falling in a straight line from her shoulders |
| 4. 臉部朝向與視線 | 三分之二側臉，看向畫面左側前方的街燈（不看鏡頭） | her face in a three-quarter view, looking ahead toward the street lights on camera-left, away from the camera |
| 5. 相機高度與俯仰 | 相機在她腰部高度，平視（參考：85mm 鏡頭、約 3.6 公尺；畫面中心與相機高度差換算俯仰約 +0.8 度） | camera at her waist height, level |
| 6. 畫面配置 | 人物在右側約六成處、身體與視線朝左，左側留給延伸的濕亮街道與街燈光點 | she stands right of centre with her body and gaze toward the left, the wet street and its glowing street lights receding on the left |
| 7. 攝影目的 | 不看鏡頭、微啟唇的放鬆神情與橫式款的自信壞笑完全不同；斜側讓胸臀曲線與長風衣的直線同時成立 | the relaxed, parted-lip look away from the camera is the opposite of her confident smirk in the horizontal set, and the oblique stance keeps both her curves and the straight line of the coat |

**選擇理由：** 保留雨後夜街與黑色服裝；改不看鏡頭、看向前方街燈，人物移到右側、左側留給視線與街燈；身體改為約30度斜側，比側身更好認臉。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 保留雨後夜街與黑色服裝；改為不看鏡頭：看向前方街燈，表情改成放鬆、微啟唇、帶點沉思（不是橫式款的自信壞笑），臉不改；身體由側面改為約30度斜側；人物改到右側約六成，左側留給街燈。

| 項目 | 內容 |
|---|---|
| 場景 | 夜晚剛下過雨的城市街道：濕亮的路面倒映暖色櫥窗光與冷色路燈，店面已打烊、只有素面霧玻璃，街上沒有人。 |
| 服裝 | 洋裝：黑色緞面繞頸迷你洋裝；外套：黑色長版皮革風衣（敞開）；鞋：黑色細跟尖頭短靴（不入鏡）；配件：大型銀色垂墜耳環 |
| 髮型 | 長直黑髮，光滑有光澤，深側分。 |
| 妝感 | 柔和魅惑妝、貼近睫毛的淡棕眼線。 |
| 身材設定（數字） | 165 cm／94-59-92／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 繞頸緞面洋裝貼合 F 罩杯胸型、細腰與臀線；斜側讓胸臀曲線與敞開長風衣的直線同時成立。 |
| 主光 | 畫面外左前方大型柔光，臉清楚 |
| 補光 | 濕路面上暖琥珀與冷藍的倒影 |
| 姿態 | 站在濕亮的人行道上，看向前方的街燈。 |
| 手的位置 | 一手拉著敞開的風衣衣襟在腰間，一手自然垂在大腿旁。 |
| 表情 | 放鬆、微啟唇、帶點沉思 |
| 視線 | 看向畫面左側前方的街燈（不看鏡頭） |
| 焦段／距離／視野（參考） | 3:4，85mm，約 3.6 公尺，視野 1.02×1.36 公尺；頭頂上方留白約 7%（規劃）；相機約 1.09 公尺高、畫面中心約 1.14 公尺高，俯仰約 +0.8 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 8%；下緣：規劃裁切線在膝蓋下方的小腿上段；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | 她的配色是黑、煙灰、金屬銀；雨夜街燈下放鬆、微啟唇的沉思神情，是和橫式款自信壞笑完全不同的另一面；臉不改。 |
| 與同一人另一款的差異 | 橫式款是頂樓燈海、血紅馬甲洋裝、正面直視鏡頭的自信壞笑；這款是雨夜街道、黑色緞面＋長皮風衣、看向街燈的沉思神情。 |
| 參考照片（用途） | rainie-01：表情（只參考妝感與氣場；表情改成放鬆的沉思）；rainie-11：服裝材質（黑色細肩帶洋裝的線條） |
| 月份（已確認） | 5 月（春末梅雨） |

| 風險 | 處理 |
|---|---|
| 店面出現招牌文字 | 寫明打烊的素面霧玻璃 |
| 夜景臉暗 | 大型柔光主光 |
| 不看鏡頭時臉太側 | 三分之二側臉 |
| 為改表情而改臉 | 只改表情與視線，臉維持設定 |

prompt 草稿（3:4，尚未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, high cheekbones and a sculpted jaw, soft-glam makeup with a soft brown liner close to the lash line, long straight jet-black hair worn sleek and glossy with a deep side part. Curvy figure, 165 cm tall, bust 94 cm, waist 59 cm, hips 92 cm, F cup, full chest and slim waist. She wears a black satin halter mini dress that follows her full chest, slim waist and hips, a long black leather trench coat worn open and large silver statement drop earrings. Setting: a city street at night just after rain, the wet pavement reflecting warm amber light from closed shopfronts with plain frosted glass and cool blue street lights, the street empty. One hand holds the edge of the open coat at her waist and the other is relaxed beside her thigh; her expression is relaxed and thoughtful, her lips slightly parted. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the satin halter dress over her chest, waist and hips and the long open coat down to just below the knees, one hand holding the coat edge at her waist and the other relaxed beside her thigh. Body: standing on the wet pavement, her body turned about 30 degrees toward camera-left, her weight on her back leg and her shoulders relaxed and slightly lowered, the open coat falling in a straight line from her shoulders. Face and gaze: her face in a three-quarter view, looking ahead toward the street lights on camera-left, away from the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.6 metres, camera at her waist height, level, natural perspective without distortion. Composition: she stands right of centre with her body and gaze toward the left, the wet street and its glowing street lights receding on the left. Emphasis: the relaxed, parted-lip look away from the camera is the opposite of her confident smirk in the horizontal set, and the oblique stance keeps both her curves and the straight line of the coat. Lighting: a large soft key light from front-left just out of frame lights her face clearly; warm amber and cool blue reflections shimmer on the wet street behind her; black, silver and deep blue tones with a hint of amber. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.22 V-miu-shiraishi｜Miu｜直式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 春日度假別墅的木平台，杏桃色有骨架的細肩短洋裝，坐在白色帆布吊床邊，笑著看向開花的果樹。

**攝影：** 坐姿全身｜約30度斜側（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側開滿白花的果樹｜坐姿時的腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 坐姿全身 | a full-length seated shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，坐姿的雙腿與雙腳完整。入鏡：完整坐姿；心形領貼身上身的胸型、細腰、微蓬的裙襬、併攏的雙腿與白色細帶涼鞋；抓著吊床布邊的雙手（在臀側） | her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the sweetheart boned bodice over her chest, her very slim waist, the softly flared skirt, her legs together and the white strappy sandals, both hands holding the hammock edge beside her hips |
| 3. 身體朝向 | 約30度斜側（朝畫面右）：坐在吊床邊緣，身體朝畫面右轉約30度；雙腳踩在木平台上、雙膝併攏斜向畫面左側，上身微微前傾、背部自然 | sitting on the edge of the hammock, her body turned about 30 degrees toward camera-right, both feet on the deck with her knees together and angled toward camera-left, her upper body leaning slightly forward |
| 4. 臉部朝向與視線 | 三分之二側臉，看向畫面右側開滿白花的果樹（不看鏡頭） | her face in a three-quarter view, looking toward the blossoming fruit tree on camera-right, away from the camera |
| 5. 相機高度與俯仰 | 相機在她坐姿時的腰部高度，平視（參考：70mm 鏡頭、約 3.3 公尺；畫面中心與相機高度差換算俯仰約 -0.7 度） | camera at her seated waist height, level |
| 6. 畫面配置 | 人物在中央偏左；白色吊床從左上斜到右下形成對角線，右側是開白花的果樹（她的視線方向），背景新綠柔焦 | she sits just left of centre, the white hammock running diagonally across the frame, the blossoming fruit tree on the right where she is looking, fresh green soft behind |
| 7. 攝影目的 | 坐在吊床邊微微前傾、看向一旁的自然笑容，讓胸型、細腰與腿線都清楚，又保留甜美的度假感 | sitting forward on the hammock edge with a natural smile toward the tree shows her chest, very slim waist and legs clearly while keeping a sweet holiday mood |

**選擇理由：** 吊床邊的坐姿和橫式款的床上半倚都是坐姿，但身體方向（約30度斜側 vs 約45度）、視線（看果樹 vs 看鏡頭）、場景（戶外 vs 室內）都不同。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 撤回運河與奶油 V 領針織裙：改為春日度假別墅木平台與白色帆布吊床，杏桃色有骨架的細肩短洋裝（配色與其他 23 套比較後選定）；姿勢由欄杆站姿改為坐在吊床邊、雙手抓布邊、微微前傾；不看鏡頭、看向開花的果樹；景別由大腿中段以上改為坐姿全身。

| 項目 | 內容 |
|---|---|
| 場景 | 春天上午的度假別墅木平台：兩根木柱間掛著白色帆布吊床，平台邊是開滿白花的果樹與新綠樹籬，柔和明亮的天光，平台上沒有其他人。 |
| 服裝 | 洋裝：杏桃色棉緞細肩短洋裝（有骨架的貼身上身、心形領、收腰、裙長大腿中段微蓬）；鞋：白色細帶平底涼鞋；配件：小珍珠耳環 |
| 髮型 | 淺亞麻米金，齊肩內彎鮑伯、空氣瀏海。 |
| 妝感 | 眼下橘調腮紅、水潤唇。 |
| 身材設定（數字） | 156 cm／87-55-86／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 有骨架的心形領上身塑出 E 罩杯胸型與 55 cm 細腰；坐在吊床邊、上身微微前傾，裙長到大腿中段，併攏斜放的雙腿呈現腿線。 |
| 主光 | 明亮柔和的春日上午天光（薄雲） |
| 補光 | 畫面外前方反光板 |
| 姿態 | 側坐在白色帆布吊床的邊緣，雙腳踩在木平台上，上身微微前傾。 |
| 手的位置 | 雙手抓著身旁吊床的布邊（在臀側，不遮胸腰）。 |
| 表情 | 開心、自然的笑 |
| 視線 | 看向畫面右側開滿白花的果樹（不看鏡頭） |
| 焦段／距離／視野（參考） | 3:4，70mm，約 3.3 公尺，視野 1.13×1.51 公尺；人物約佔畫面高度 87%（規劃）；相機約 0.72 公尺高、畫面中心約 0.68 公尺高，俯仰約 -0.7 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 8%；下緣：規劃雙腳與鞋下方留白約 5%；不能切：髮頂、臉、入鏡的雙手、雙腳與鞋；規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | Miu 的「外出」支柱換成春日度假：杏桃色是 24 套裡沒有用過的顏色（整組已有薄荷、淺紫、粉、熱粉、白、鼠尾草綠、向日葵黃、紅黑、墨綠、霧玫瑰、奶油、酒紅、淺藍），有骨架的上身直接呈現胸型與很細的腰；不是奶油針織、不是欄杆站姿。 |
| 與同一人另一款的差異 | 橫式款是室內晨光公寓、象牙白緞面小可愛＋短褲、床上半倚看鏡頭；這款是戶外春日木平台、杏桃色細肩短洋裝、坐在吊床邊看向果樹。 |
| 參考照片（用途） | miu-04：服裝材質（細肩帶洋裝的線條；紫色花紋與室內背景不採用）；miu-05：身分（認臉與髮型；運河場景不採用） |
| 月份（已確認） | 4 月（春） |

| 風險 | 處理 |
|---|---|
| 吊床不穩、坐姿不合理 | 雙腳踩在平台上、只坐在吊床邊緣 |
| 童顏顯小 | 寫明 adult、成熟剪裁；不用蝴蝶結與娃娃裝 |
| 裙下走光 | 雙膝併攏斜放、裙長到大腿中段 |
| 吊床繩結與手指 | 生成後檢查 |
| 碰撞紀錄（Jia、Somi） | 暖杏桃色、甜美、淺亞麻短髮；不改臉、不宣稱能消除 |

prompt 草稿（3:4，尚未執行）：

```text
A 22-year-old adult Japanese woman with her natural very fair skin tone, a round face with big soft downturned eyes, orange-toned blush under the eyes and glossy lips, light flaxen beige-blonde hair in a shoulder-length bob curled inward with airy see-through bangs. Petite curvy figure, 156 cm tall, bust 87 cm, waist 55 cm, hips 86 cm, E cup, a full chest and a very slim waist. She wears an apricot cotton-sateen mini dress with thin straps, a fitted boned bodice with a sweetheart neckline that shapes her full chest and very slim waist and a softly flared skirt to mid-thigh, white strappy flat sandals and small pearl earrings. Setting: a wooden deck at a holiday villa on a spring morning, a white canvas hammock hung between two wooden posts, fruit trees in white blossom and fresh green hedges beside the deck, soft bright daylight, the deck empty. Both hands hold the edge of the hammock beside her hips; she laughs naturally with a bright, happy smile. Shot: a full-length seated shot, her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the sweetheart boned bodice over her chest, her very slim waist, the softly flared skirt, her legs together and the white strappy sandals, both hands holding the hammock edge beside her hips. Body: sitting on the edge of the hammock, her body turned about 30 degrees toward camera-right, both feet on the deck with her knees together and angled toward camera-left, her upper body leaning slightly forward. Face and gaze: her face in a three-quarter view, looking toward the blossoming fruit tree on camera-right, away from the camera. Camera: vertical 3:4 frame, full-frame camera with a 70mm lens from about 3.3 metres, camera at her seated waist height, level, natural perspective without distortion; she fills about 87% of the frame height. Composition: she sits just left of centre, the white hammock running diagonally across the frame, the blossoming fruit tree on the right where she is looking, fresh green soft behind. Emphasis: sitting forward on the hammock edge with a natural smile toward the tree shows her chest, very slim waist and legs clearly while keeping a sweet holiday mood. Lighting: soft bright spring daylight under thin cloud as a large gentle key, a white reflector just out of frame in front lighting her face evenly; apricot, blossom white and fresh green tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.23 V-jia-seo｜Jia｜直式款（新企劃｜已接受（R6 owner 紀錄））

**一句話：** 明亮的玻璃溫室，白色無袖立領短上衣配薄荷綠緞面高腰貼臀窄裙，斜側站在大葉植物之間，臀腰曲線清楚。

**攝影：** 全身｜約45度斜側（朝畫面右）｜臉正面・看鏡頭｜臀部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到涼鞋完整；白色立領短上衣與露出的細腰、高腰窄裙貼著臀線收窄的輪廓、開衩打開的前腿與白色細帶涼鞋；插在腰頭的手與碰葉子的手 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to sandals, the white mock-neck crop top and her bare slim waist, the line of the high-waisted pencil skirt hugging her hips and narrowing below, the slit opening over her front leg and the white strappy sandals, one hand on the waistband and the other touching a monstera leaf |
| 3. 身體朝向 | 約45度斜側（朝畫面右）：站在石板路上，身體朝畫面右轉約45度；重心在後腳、臀部隨重心往後側，開衩那側的前腳往前一小步，肩膀放鬆 | standing on the stone path, her body turned about 45 degrees toward camera-right, her weight on her back leg with her hip shifted back and to the side, the front leg on the slit side stepping slightly forward, shoulders relaxed |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她臀部高度，平視（參考：85mm 鏡頭、約 5.3 公尺；畫面中心與相機高度差換算俯仰約 -0.1 度） | camera at her hip height, level |
| 6. 畫面配置 | 人物置中；兩側大片龜背芋葉框住畫面邊緣，白色鋼骨溫室結構在上方；葉子只在兩側、不遮身體 | she is centred on the path, large monstera leaves framing both side edges and the white steel frames of the greenhouse above, the leaves never covering her body |
| 7. 攝影目的 | 全身約45度斜側讓高腰窄裙的腰臀輪廓與開衩腿線完整看得出曲線，短上衣露出細腰 | the full figure at about 45 degrees shows the waist-to-hip outline of the high-waisted pencil skirt and the leg through the slit, with the crop top showing her slim waist |

**選擇理由：** 保留玻璃溫室；窄裙改成高腰貼臀並寫明開衩位置，景別改全身、身體約45度斜側、臀部往後側，輪廓才看得出曲線。橫式款是坐姿、看湖面，兩款景別與視線都不同。

**R7：** 已接受（R6 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

**R4 改了什麼（歷史）：** 保留玻璃溫室；薄荷緞面中長裙改為高腰貼臀窄裙（腰頭在肚臍上方、貼臀往膝下收窄、左前側開衩到大腿中段）；景別由膝上改為全身、身體改為約45度斜側並把臀部往後側，讓輪廓真的看得出曲線；白色細帶涼鞋因全身入鏡寫回 prompt。

| 項目 | 內容 |
|---|---|
| 場景 | 玻璃溫室：白色鋼骨結構、茂密的熱帶植物與大片龜背芋葉、石板小徑，溫室裡沒有其他人。 |
| 服裝 | 上身：白色無袖立領貼身短上衣（露腰）；下身：薄荷鼠尾草綠緞面高腰窄裙（腰頭在肚臍上方、貼著臀線往膝下收窄、左前側開衩到大腿中段）；鞋：白色細帶涼鞋；配件：細銀耳針 |
| 髮型 | 冷灰藍黑長髮，一側塞在耳後露出薄荷綠內層。 |
| 妝感 | 水光無妝感、淡棕眼線、漸層唇。 |
| 身材設定（數字） | 168 cm／85-58-90／C（直角肩、長腿） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 短上衣露出細腰；高腰窄裙從腰頭貼著臀線往膝下收窄，約45度斜側、臀部往後側，讓 90 cm 臀線與腰臀比清楚；左前側開衩在往前的那條腿上打開。 |
| 主光 | 玻璃屋頂的大面積明亮漫射光 |
| 補光 | 畫面外前方柔光 |
| 姿態 | 站在植物之間的石板路上，斜側站著、臀部隨重心往後側。 |
| 手的位置 | 一手插在高腰裙的腰頭上，一手輕觸身旁的大片龜背芋葉。 |
| 表情 | 冷靜柔和的微笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 5.3 公尺，視野 1.5×2.0 公尺；人物約佔畫面高度 86%（規劃）；相機約 0.9 公尺高、畫面中心約 0.9 公尺高，俯仰約 -0.1 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 9%；下緣：規劃雙腳與鞋下方留白約 5%；不能切：髮頂、臉、入鏡的雙手、雙腳與鞋；規劃目標（套框後）：髮頂上方 ≥4%、腳下 ≥3%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手、雙腳與鞋是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | 薄荷綠是她的髮色內層與配色；溫室的綠與白延伸她的冷調。高腰貼臀窄裙＋斜側站姿讓曲線真的看得出來，實景、無運動感。 |
| 與同一人另一款的差異 | 橫式款是初秋湖畔、深酒紅細針織繞頸短洋裝、側坐長椅、望向湖面；這款是溫室綠意、白色短上衣＋薄荷緞面高腰窄裙、斜側站姿看鏡頭。 |
| 參考照片（用途） | jia-03：身分（白色上衣與認臉）；jia-07：服裝材質（白色綁結上衣的露腰比例） |
| 月份（已確認） | 2 月（冬末） |

| 風險 | 處理 |
|---|---|
| 只換裙子名稱、輪廓沒變 | prompt 寫明腰頭位置、貼臀收窄與開衩位置，並改全身斜側站姿 |
| 植物遮住身體 | 葉子只在兩側 |
| 開衩遮蔽 | 開衩到大腿中段 |

prompt 草稿（3:4，尚未執行）：

```text
A 22-year-old adult Korean woman with her natural fair, cool-toned skin, a small face, straight shoulders and long narrow upturned eyes, dewy no-makeup makeup with a soft brown liner and gradient lips, long cool blue-black hair tucked behind one ear so its mint-green inner layer shows. Slim, long-legged figure with soft feminine curves, 168 cm tall, bust 85 cm, waist 58 cm, hips 90 cm, C cup, a slim waist and long legs. She wears a white sleeveless mock-neck fitted crop top that shows her slim waist, a high-waisted mint-sage satin pencil skirt that sits above her navel, hugs her hips and narrows to just below the knee with a front-left slit to mid-thigh, white strappy sandals and small silver stud earrings. Setting: a glass greenhouse conservatory with white steel frames, lush tropical plants and large monstera leaves, a stone path, the greenhouse empty. One hand rests on her hip at the high waistband and the other lightly touches a large monstera leaf beside her, the slit opening over her front leg; she has a cool, soft smile. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to sandals, the white mock-neck crop top and her bare slim waist, the line of the high-waisted pencil skirt hugging her hips and narrowing below, the slit opening over her front leg and the white strappy sandals, one hand on the waistband and the other touching a monstera leaf. Body: standing on the stone path, her body turned about 45 degrees toward camera-right, her weight on her back leg with her hip shifted back and to the side, the front leg on the slit side stepping slightly forward, shoulders relaxed. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 5.3 metres, camera at her hip height, level, natural perspective without distortion; she fills about 86% of the frame height. Composition: she is centred on the path, large monstera leaves framing both side edges and the white steel frames of the greenhouse above, the leaves never covering her body. Emphasis: the full figure at about 45 degrees shows the waist-to-hip outline of the high-waisted pencil skirt and the leg through the slit, with the crop top showing her slim waist. Lighting: bright diffused daylight through the glass roof as a large soft key, a soft fill just out of frame in front; white, mint and deep green tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.24 V-yerin-han｜Yerin｜直式款（新企劃｜已接受（R4 owner 紀錄））

**一句話：** 日落的白沙海灘，白色圓領貼身針織背心洋裝，赤腳站在淺浪邊的燦笑。

**攝影：** 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・輕仰

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：貼身羅紋背心洋裝的胸型、細腰與臀線、裙擺下的大腿到膝蓋下方；放在鎖骨的手與自然垂放的手 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the fitted ribbed tank dress over her full chest, slim waist and hips and her legs down to just below the knees, one hand at her collarbone and the other relaxed at her side |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：站在淺浪邊，重心在後腳、前膝微彎；身體朝畫面左轉約30度，肩與臀同向 | standing at the water's edge with her weight on her back leg and her front knee softly bent, her body turned about 30 degrees toward camera-left, shoulders and hips turned together |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她臀部高度，輕仰（參考：85mm 鏡頭、約 3.7 公尺；畫面中心與相機高度差換算俯仰約 +3.4 度） | camera at her hip height, tilted slightly upward |
| 6. 畫面配置 | 人物略偏右；海平線壓低在她臀部高度，金色與蜜桃色的夕陽天空佔滿上方與左側，夕陽在她身後形成頭髮輪廓光 | she stands slightly right of centre, the horizon low behind her hips and the gold and peach sunset sky filling the space above and to the left |
| 7. 攝影目的 | 輕仰與低海平線讓 170 公分的身形更修長，斜側呈現臀線的健康曲線 | the slightly low camera and low horizon make her tall figure look longer, and the oblique stance shows the healthy curve of her hips |

**選擇理由：** 海灘夕陽用臀部高度輕仰，讓天空成為乾淨背景、身形更長；斜側呈現 93 公分臀線的健康曲線。與橫式款的坐姿全身不同。

**R7：** 已接受（R4 owner 紀錄，R7 維持）：服裝、場景、表情、姿態、攝影與 prompt 照目前版本，不再要求回覆。

| 項目 | 內容 |
|---|---|
| 場景 | 日落時寬闊的白沙海灘，平靜的淺水、海上金色與蜜桃色的天空，海灘上沒有其他人。 |
| 服裝 | 洋裝：白色圓領羅紋貼身背心迷你洋裝；鞋：赤腳（不入鏡）；配件：小金色圈耳環、腳踝細金鍊（不入鏡） |
| 髮型 | 亞麻棕長髮、臉側金色挑染，放下的鬆散波浪。 |
| 妝感 | 防曬淡妝、亮色唇。 |
| 身材設定（數字） | 170 cm／90-60-93／E（健康曲線） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身羅紋背心洋裝勾出 E 罩杯胸型、細腰與 93 cm 的臀線；赤腳站立讓長腿比例自然。 |
| 主光 | 她身後的低角度夕陽，頭髮與肩膀暖色輪廓光 |
| 補光 | 畫面外前方大反光板與柔光 |
| 姿態 | 站在淺浪邊。 |
| 手的位置 | 一手輕放在鎖骨，一手自然垂放。 |
| 表情 | 大方燦爛的笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 3.7 公尺，視野 1.04×1.39 公尺；頭頂上方留白約 7%（規劃）；相機約 0.88 公尺高、畫面中心約 1.1 公尺高，俯仰約 +3.4 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 印刷（工作照片框） | 直式 3:4 工作照片框（R6 已接受）（120×160 mm）；比例計算：3:4 放入 3:4 框不裁切；上緣：規劃髮頂留白約 7%；下緣：規劃裁切線在膝蓋下方的小腿上段；不能切：髮頂、臉、入鏡的雙手；規劃目標（套框後）：髮頂上方 ≥4%；判斷：依已接受的工作照片框與規劃構圖，暫無須為印刷更改拍攝方向；生成後仍須實圖套框、檢查重要部位與有效 ppi。生成後待驗證：實際輸出像素、套框後髮頂、臉、入鏡的雙手是否都在框內、有效 ppi；比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準 |
| 為何符合人設 | 她的支柱「旅遊／球場遠征」的另一面：度假海灘的夕陽，健康又性感，和球場完全不同。 |
| 與同一人另一款的差異 | 橫式款是春日球場、polo＋百褶裙＋球帽、坐球車；這款是日落海灘、白色背心洋裝、赤腳站在水邊。 |
| 參考照片（用途） | yerin-07：服裝材質（白色平口＋白短裙的清爽穿搭）；yerin-08：表情（燦爛的大笑） |
| 月份（已確認） | 8 月（盛夏） |

| 風險 | 處理 |
|---|---|
| 逆光臉暗 | 寫明反光板與柔光 |
| 白色洋裝濕透透光 | 寫明站在淺浪邊、洋裝是乾的 |
| 膚色被曬成小麥色 | 只寫一次她原本的白皙膚色 |

prompt 草稿（3:4，尚未執行）：

```text
A 26-year-old adult Korean woman with her natural fair skin tone, bright defined features and a wide open smile, light sun-protective makeup and a bright lip, long flax-brown hair with golden face-framing highlights worn down in loose waves. Curvy athletic figure with soft feminine lines, 170 cm tall, bust 90 cm, waist 60 cm, hips 93 cm, E cup, long legs and a slim waist. She wears a white fitted ribbed scoop-neck tank mini dress that follows her full chest, slim waist and hips, and small gold hoop earrings; the dress is dry. Setting: a wide white-sand beach at sunset, calm shallow water and a soft gold and peach sky over the sea, the beach empty. One hand rests lightly at her collarbone and the other is relaxed at her side; she smiles brightly. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the fitted ribbed tank dress over her full chest, slim waist and hips and her legs down to just below the knees, one hand at her collarbone and the other relaxed at her side. Body: standing at the water's edge with her weight on her back leg and her front knee softly bent, her body turned about 30 degrees toward camera-left, shoulders and hips turned together. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.7 metres, camera at her hip height, tilted slightly upward, natural perspective without distortion. Composition: she stands slightly right of centre, the horizon low behind her hips and the gold and peach sunset sky filling the space above and to the left. Emphasis: the slightly low camera and low horizon make her tall figure look longer, and the oblique stance shows the healthy curve of her hips. Lighting: the low sun behind her draws a warm rim along her hair and shoulders; a large white reflector and a soft fill just out of frame in front light her face evenly; warm gold, peach and soft blue tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

## 9. 構圖與生成提案

| 款式 | 建議 |
|---|---|
| 橫式款（H） | 工作照片框（R6 已接受）：橫式大照片框 192×104 mm（畫布 6,14–198,118）。生成用 16:9（原生尺寸未知）：比例上要裁掉高度 4 mm，規劃上下各約 2 mm。這是本案工作版型，不是廠商規格或印刷安全；見「印刷構圖」。 |
| 直式款（V） | 工作照片框（R6 已接受）：直式 3:4 框 120×160 mm（畫布 12,16–132,176）。生成用 3:4：比例上不裁切；若輸出 1536×2048，約 325 ppi（比例計算，以實際輸出為準）。這是本案工作版型，不是廠商規格或印刷安全。 |

**評估：**

- 橫式款的價值在於「人＋環境」的寬畫面：大照片框比半版適合。半版直幅框比較適合直式照片，而直式款已經另有 12 套直幅照片。
- 若 Penny 最後選擇橫式款用半版直幅框：這 12 套 16:9 不適用，要另外規劃與生成直幅版本——不從 16:9 硬裁成直幅。
- 直式款若最後用近方形框（120×128，約 0.94:1），3:4 原圖高度要裁掉約 20%（比例事實）；會不會切到髮頂或腳要看實圖與裁切位置。所以建議直式款的照片區至少 3:4。
- 避免人物縮小到背景裡（以下是 prompt 規劃目標，不是實圖量測）：全身與坐姿的人物佔畫面高度約 85%（斜躺的 Rin 佔畫面寬度約 87%）；裁切景別保留完整髮頂、上緣約 4–10% 留白。

**限制：**

- 16:9 原生尺寸未知（推測 2048×1152，未驗證）；3:2 也未知。3:4 已知 1536×2048。
- 換算只做比例，不承諾 ppi，也不判斷線圈安全；廠商尺寸與印刷門檻還沒問。
- 外擴與 AI 放大不列為必要步驟。

換算方法：全片幅 36×24 mm。橫式款 16:9 取 36×20.25 mm，視野高＝20.25 mm×距離÷焦段；直式款 3:4 直拿裁成 24×32 mm，視野高＝32 mm×距離÷焦段。每套依景別算出畫面上下界、距離與畫面中心高度，再和相機高度比較得出平視／輕俯／輕仰；數字矛盾會讓建置失敗。焦段與距離只是參考，不是生成保證。

## 10. 費用（本輪不變；分開精確報價、歷史實扣、未知）

**狀態：** 仍未授權：沒有生成授權、沒有費用核准。下面的數字分成「精確報價」「歷史實扣」「未知」，情境試算不是預算。

**模型：** soul_2＋各人設既有 Soul，quality 2k，每次請求 1 張（count 1）；橫式款 16:9、直式款 3:4；不掛 Reference Element、不用參考圖。

**多階段與參考圖（R5 更正）：** 不規劃多階段（先生成再換臉、外擴、放大）。H／V 本來就是兩套獨立的服裝與場景，兩張只需要共同維持人設身分（同一個 Soul 與身分句）與設定身材；不得為了讓服裝或環境相同而把一款的成品當參考圖餵給另一款。任何未來使用參考圖的方案都要另外提出、另外批准，本輪不執行。（R5 撤回先前「橫直服裝差太多就把第一張當參考圖餵第二張」的寫法。）

### 10.1 精確報價（generate_image 的 get_cost 預檢，不送出工作）

| 設定 | 回傳 |
|---|---|
| soul_2＋Soul（Iris）、2k、3:4、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、2k、3:2、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、2k、2:3、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、1.5k、3:4、count 1 | credits 1／credits_exact 0.12 |
| soul_2、不帶 Soul、2k、3:4、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、2k、3:4、count 4 | credits 1／credits_exact 0.12（與 count 1 相同） |
| soul_2＋Soul（Iris）、2k、16:9、count 1（2026-10-13，本輪查詢） | credits 1／credits_exact 0.12 |

2026-10-13 用 generate_image 的 get_cost 預檢查詢 6 次（工具說明：只回傳費用、不送出工作）；查詢前後交易明細沒有新增任何一筆。回傳有兩個欄位：credits（整數顯示值 1）與 credits_exact（0.12）。不把 1 解讀成 0.12，也不把 0.12 當成已證實的實扣：0.12 與歷史 Soul V2 交易明細一致，但 3:2、2:3、1.5k 這幾種設定從沒有實扣紀錄。 本輪另查 16:9 一次，回傳相同；查詢前後交易明細沒有新增。

### 10.2 歷史實扣與紀錄

| 項目 | 數值 | 依據 | 等級 | 來源檔 |
|---|---|---|---|---|
| Soul V2 實際扣款（交易明細） | 每筆 −0.12 | Soul 訓練總報告（2026-09-08）：驗證圖 114 張約 13.7 credits，交易明細為重複的「Higgsfield Soul V2 −0.12」；驗證紀錄寫明「每 spec 只生一張」，所以是一次請求 1 張。這批的比例與畫質沒有寫在讀到的文件裡。 | 歷史實扣（交易明細） | `review/soul_training/FINAL_REPORT.md`、`review/soul_pilot/VERIFY_REMAINING_12.md` |
| 2026-10-13 帳號交易明細 | 今天也有 Soul V2 −0.12 的扣款 | 唯讀查詢 transactions：這些是帳號上其他人的工作，不是本案；只說明 Soul V2 目前仍以 −0.12 一筆扣款。 | 歷史實扣（他人工作，只作參考） |  |
| Iris 先前的 Soul 生成 | 費用未逐筆記錄 | Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 共 7 次生成成功、輸出 1536×2048，但沒有逐筆扣款。 | 無費用紀錄 | `kols/iris-chen/generation_notes.md` |
| 失敗也可能扣款 | 有紀錄 | Soul 訓練總報告的對帳判準：曾出現「重複的 Soul V2 −0.12 扣款但工作失敗」的情況（Vicky Lin 案例），所以重試也要算進上限。 | 歷史紀錄 | `review/soul_training/FINAL_REPORT.md` |

### 10.3 計價方式、張數、上限、異常

| 項目 | 說明 | 來源檔 |
|---|---|---|
| 計價單位 | 工具報價以「每次請求」回傳；count 4 的報價與 count 1 完全相同，所以無法判斷報價是每張還是每次請求。本案只用 count 1，不推算多張的費用。 |  |
| 每次請求產生幾張 | generate_image：count 1–4（同一 prompt 的變體）；generate_image_batch：最多 12 個請求、每個固定 1 張，而且批次不支援費用預檢。本案每次只送 1 個請求、count 1。 |  |
| 能不能限制總費用 | generate_image 與 generate_image_batch 都沒有「費用上限」參數（只有 AI Influencer 工具有，不適用）。只能靠流程控制：一次一個請求、每次之後查交易明細、累計達上限就停。餘額不能用來對帳——帳號同時有其他人在用。 |  |
| 異常扣款 | 原因未知。另一位人設的生成筆記記錄過三次「實扣高於預檢」：seedream_v4_5 4 張扣 50、seedream_v4_5 4 張扣 8、soul_2（不帶 Soul）4 張扣 2.16。三次都是用帳戶餘額前後相減算的，而帳號同時有其他人在用；沒有用交易明細逐筆核對，所以不能歸因，也不能排除。其中兩次是不同模型（seedream_v4_5）。 | `kols/sophia-tseng/generation_notes.md`、`review/soul_training/FINAL_REPORT.md` |

### 10.4 24 套獨立拍攝的情境試算（不是預算）

| 情境 | 請求數 | 依 credits_exact 報價 | 若實扣是顯示值（每次 1） |
|---|---|---|---|
| 每套 1 次請求 | 24 | 約 2.88 | 24 |
| 每套 2 次請求 | 48 | 約 5.76 | 48 |
| 每套 3 次請求 | 72 | 約 8.64 | 72 |

只是用今天的報價換算的情境，不是預算、不保證能做完幾張。「依 credits_exact」是工具的精確報價欄位；「若實扣是顯示值」是假設每次請求扣 1 credit 的上界情境。實扣是哪一個，要等第一張試拍用交易明細確認。失敗與重試都可能扣款。

**未知：** 16:9 與 3:2 的實際輸出像素、16:9、3:4 在這些企劃下的實際扣款（只有報價）、count 大於 1 時的費用、ready 狀態的 Soul 在逆光、夜景、室內暖光下的身分穩定度、24 套獨立造型各自需要幾次才能成功

### 10.5 Iris 首張試拍

**V-iris-chen**　M-4 R4：Penny 接受，照片直接採用（歷史：M-4 R2：依授權生成 V-Iris 首試 1 張（精確報價 0.12、實扣 0.12，依時窗及唯一任務推定）；部分通過，待主管覆核；沒有重送。；M-4 R1：V-Iris 造型已接受；首試前核查完成（唯讀查詢與不扣款的報價預檢）；生成與費用仍未授權，不執行生成。；R7：只整理 V-Iris 首試準備（見首試準備文件），沒有生成、沒有花 credits、沒有呼叫 Higgsfield、沒有做報價預檢；生成與費用仍未授權，不執行 M-4。；R6：V-Iris 首試方向已接受；生成與費用仍未授權，不執行 M-4。）

首試準備（工作流、待確認事項、首張驗收條件）見 `CAL_20_M4_IRIS_FIRST_TEST_PREP.md`。

- 直式 3:4 的原生尺寸已知（1536×2048）、報價已查，第一張只需要驗證「寫真質感、身分、身材與實際扣款」，少一個未知數。
- 直幅大腿中段以上最能看清 Penny 這次指定的穿搭與姿態：更顯身材的上衣＋牛仔迷你裙、身體面向鏡頭、笑容。
- 保留她喜歡的 iris-04 草地夕陽氛圍，又是全組最難的逆光，先驗證補光是否足夠。
- 橫式款（H-iris-chen，16:9 原生尺寸未知）放在之後，等第一張結果與費用確認再測。

| 項目 | 內容 |
|---|---|
| 範圍 | 只做 1 張：V-iris-chen 的 prompt 草稿（本頁「prompt 草稿」原文，不沿用上一輪被 Penny 修改的 Iris prompt）。 |
| 設定 | soul_2＋Iris 既有 Soul、quality 2k、aspect 3:4、count 1、不掛參考圖；use_unlim 設為 false（用 credits 付費；查詢時帳號沒有可用的免費額度）。 |
| 報價 | 今天的預檢：credits 1／credits_exact 0.12；實扣未確認。 |
| 重試 | 不自動重試。無論結果好壞、成功或失敗，都先停下回報。 |
| 對帳 | 送出前後各查一次交易明細，記錄這一張的實際扣款；不用餘額對帳（帳號有他人同時使用）。 |
| 前提 | V-Iris 造型已接受（R4 owner 紀錄；M-3 已完成），不再等待造型核准。生成與費用尚未授權：需要費用核准與主管另發的 M-4 生成指令；在那之前什麼都不送出。 |

**授權：** 本輪沒有任何花費授權。任何試拍都要 Penny 批准，再由主管另發 M-4 指令。

## 11. 要請 Penny 決定的事

沒有要請 Penny 決定的企劃事項：M-3 已完成（主管 M-4 R1 結論），不再要求 owner 填企劃問卷。V-Iris 首試 Penny 已接受（M-4 R4，含反光板），不再詢問；第一批 5 張 Penny 已全數退回（M-4 R6）；24 套重審與重建提案見 `CAL_23_M4_R6_REPLAN.md`，其中需要 Penny 決定的事項列在該文件第 8 節。

## 12. 共同的皮膚與質感句（每段 prompt 結尾都加）

```text
Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```
