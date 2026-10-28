TASK-CAL-001／M-4／R6｜主管覆核 REVISE｜修正重審規則與構圖矛盾｜送審報告

# CAL_21 — 第一批 5 位角色生成準備（M-4 R4 準備；M-4 R5 已依本文件生成）

> **M-4 R5：主管覆核 PASS，已依本文件每位送出 1 次（共 5 次、無重試）；V-Rin 只改授權的景別用語，其餘 4 份逐字照送。結果、最終送出文字與差異、驗收與扣款見 `CAL_22_M4_BATCH1_RESULTS.md`。以下保留 M-4 R4 準備時的內容與數字，不回改。**

> 資料檔：`data/cal_m4_batch1_prep.json`（batch1-prep-v1，2026-10-21）與 `data/cal_m3_shoot_plan.json`（shoot-plan-v12）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準；5 份 prompt 由產生器核對「已接受企劃原文＋下列光線句改寫」後才排版。
> **本輪生成 0、修圖 0、訓練 0、扣 credits 0；唯讀查詢 10 次（含不扣款報價預檢 5 次）。**

## 0. 依據與範圍

- Penny 要求加快製作、不再逐位首試，並同意下一步採 5 位角色批次製作（主管轉述，docs/calendar/data/cal_m4_owner_r4.json）。名單由執行者推薦，不要求 Penny 再選。
- 本輪不生成；5 份 prompt、設定與費用待主管覆核，通過後另發整批生成指令。
- V-Iris：Penny 接受，照片直接採用（M-4 R4；取代主管 M-4 R3「反光板及支架必修」的判定；反光板保留）。目前進度：24 套＝已接受 22＋已選定待確認修改 1＋待 Penny 選片 1＋退回待重規劃 0＋尚未生成 0；待完成合計 2（累計已生成 83 張，另計；構圖底稿另計 2 張，不是月面照片）。

## 1. 5 位總覽（依送出順序）

| # | 角色 | 套別 | 月份 | 比例 | 景別（企劃） | 推薦理由 | 選這一款的理由 |
|---|---|---|---|---|---|---|---|
| 1 | Tammy | V-tammy-chou | 1 月 | 3:4 | 大腿中段以上｜正面｜臉正面・看鏡頭｜腰部高度・輕仰 | 室內夜間暖色人工光（水晶吊燈）、大腿中段以上近景、正面看鏡頭，加上小手提包道具；這三項是 V-Iris（戶外逆光、站姿）沒有測過的條件。 | 選直式：大腿中段以上的近景與室內暖光是本批唯一的室內條件；橫式款（花園露台全身、白天）與 H-Yerin 同屬白天戶外，資訊重複。 |
| 2 | Rin | V-rin-ayase | 10 月 | 3:4 | 膝上｜約45度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側港口的出口與海面｜腰部高度・平視 | 陰天大面積柔光、膝上景別、斜側 45 度倚靠道具、三分之二側臉不看鏡頭；測試不看鏡頭時的身分辨識。 | 選直式：橫式款是側躺在貴妃椅上的斜躺全身，是 24 套裡肢體結構最複雜的一張，留到第一批結果出來後再做；直式款站姿單純、條件不同。 |
| 3 | Somi | V-somi-oh | 12 月 | 3:4 | 全身｜正面｜三分之二側臉・不看鏡頭：看畫面右上方燈籠旁飄落的雪｜臀部高度・平視 | 冬夜室外、飄雪與燈籠、全身入鏡（含靴）、抬眼看雪不看鏡頭；夜景與全身是 V-Iris 沒有測過的條件。 | 選直式：雪夜全身是本批唯一的夜間室外與全身站姿；橫式款是搭景的小吃店（室內暖光、食物道具有假字風險），室內暖光已由 V-Tammy 測。 |
| 4 | Yerin | H-yerin-han | 5 月 | 16:9 | 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 | 第一張 16:9：晴朗晨光、坐在球車上的坐姿全身與長腿；同時驗證 16:9 的實際輸出像素與套框 ppi（企劃記為未知）。 | 選橫式：需要 16:9 的實際輸出來確認像素與 ppi；直式款是日落海灘逆光、膝上站姿看鏡頭，和已接受的 V-Iris（逆光黃金時段、戶外站姿、看鏡頭）太接近，資訊少。 |
| 5 | Jia | H-jia-seo | 9 月 | 16:9 | 坐姿全身｜側面（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側的湖面與遠岸｜坐姿時的腰部高度・平視 | 第二張 16:9：傍晚逆光、側面坐姿、三分之二側臉看湖；逆光正是 V-Iris 反光板入鏡的情境，用來驗證改成效果描述後臉仍清楚、且不出現器材。 | 選橫式：提供第二個 16:9 樣本（光線、姿勢與 H-Yerin 不同），16:9 的像素與構圖不只靠一張判斷；直式款溫室全身風險較低，可放在下一批。 |

## 2. 怎麼選的

**範圍：** Iris 以外的 11 位已定稿角色（每位兩套，24 套企劃全部定稿）。

**規則：** 先看 Soul 證據：只從 2026-09-07 跑過 6 張驗證、臉部門檻 6/6 通過（production_ready）的 6 位裡選；再看企劃完整度與場景、服裝、景別、外觀差異；每位只選一套，不把同一人的橫直款算兩位。

**本批差異：**

| 面向 | 本批 |
|---|---|
| 比例 | 直式 3 張（V-Tammy、V-Rin、V-Somi）＋橫式 2 張（H-Yerin、H-Jia） |
| 光線 | 室內水晶吊燈、陰天柔光、雪夜燈籠、晴朗晨光、傍晚逆光 |
| 景別 | 大腿中段以上、膝上、全身站姿、坐姿全身 ×2 |
| 視線 | 看鏡頭 2（Tammy、Yerin）、三分之二側臉不看鏡頭 3（Rin、Somi、Jia） |
| 外觀 | 奶茶金棕大波浪、深酒紅棕低髮髻、蜜橘棕狼尾、亞麻棕金挑染低馬尾＋球帽、冷灰藍黑長髮＋薄荷綠內層；身高 160–170 cm |

**沒有選的人與原因：**

| 角色 | 原因 |
|---|---|
| Miu（miu-shiraishi，production_ready） | 兩套都是有道具的坐姿（床上半倚、吊床邊緣），加上企劃標記的「童顏顯小」風險，需要額外注意；先看第一批的坐姿與手部結果再做。她與 Jia、Somi 有碰撞紀錄，本批已含這兩位。 |
| Coco、Mia、Yuna（ready） | 較早訓練的 Soul，profile 沒有 6 張驗證紀錄；身分證據比 production_ready 弱，不放第一批。 |
| Luna（ready，v2 Soul） | 2026-08 重訓的 v2 Soul，沒有 6 張驗證紀錄；她的 H 款是「依owner指示修訂，主管覆核通過」、Penny 沒有看過修訂版。 |
| Rainie（ready，v2 Soul） | v1 Soul 已 deprecated、只能用 v2，沒有 6 張驗證紀錄。 |
| Iris | V-Iris 已接受；本批不含 Iris。 |

## 3. 描述方法（沿用 V-Iris 首試的組織方式）

順序：身分與外觀 → 服裝 → 場景 → 姿態及表情 → 景別與畫面上下界（Shot） → 身體朝向（Body） → 臉與視線（Face and gaze） → 相機（Camera） → 配置與展示目的（Composition、Emphasis） → 光線與質感（Lighting、texture）。

5 份已接受的 prompt 本來就照這個順序（R3 起 24 套統一攝影欄位），本輪沒有調整順序；這是沿用描述方法，不是把 Iris 的臉、身材、笑容、姿勢或光線套到其他人。每位的身分、髮色髮型與三圍照各自 canon 與已接受企劃。

**唯一的修改：** 5 份 prompt 唯一的修改是光線句：把畫面外器材（反光板、key light）改寫成畫面效果。

## 4. 共同設定、報價與費用

| 項目 | 設定 |
|---|---|
| 工具 | generate_image（一次一個請求，不用 generate_image_batch） |
| 模型 | soul_2 |
| Soul | 各人設既有 Soul（見逐張）；ID 只在 profile.json，不寫出 |
| quality | 2k |
| count | 1（每次請求 1 張；共 5 次請求） |
| use_unlim | false（用 credits） |
| 參考圖 | 不用參考圖 |
| style_id | 不傳 |
| 送出方式 | 依順序一張一張送：送出一次 → 輪詢到終態 → 下載原圖 → 查交易 → 才送下一張。不同時送多張，讓每一筆扣款都能單獨對上。 |
| 重試 | 不自動重試。失敗、逾時或結果不明都不重送該張。 |
| 明確失敗且未扣款 | 若一張明確失敗、且沒有扣款或已同額退款，記錄後繼續下一張；該張不重送，留給主管決定。 |
| 存放 | kols/<人設>/images/calendar_2027_batch1/（私有 repo）；生成後照 V-Iris 首試的驗收方式逐張檢查。 |

**報價（2026-10-21；generate_image get_cost:true，5 張各查一次，設定與 prompt 與預定送出相同；工具說明為只回傳費用、不送出工作）：**

| # | 套別 | 比例 | 顯示值 | 精確報價（credits_exact） |
|---|---|---|---|---|
| 1 | V-tammy-chou | 3:4 | 1 | 0.12 |
| 2 | V-rin-ayase | 3:4 | 1 | 0.12 |
| 3 | V-somi-oh | 3:4 | 1 | 0.12 |
| 4 | H-yerin-han | 16:9 | 1 | 0.12 |
| 5 | H-jia-seo | 16:9 | 1 | 0.12 |

**合計（精確報價）：0.60 credits**（5 次 × 0.12）。

**建議整批預算：** 建議整批預算上限 1 credit：5 × 0.12 = 0.60 為預期，另留 0.40 餘量；餘量小於一次以顯示值（1 credit）計費的扣款，所以若平台改以顯示值扣款，第一筆就會觸發停止條件。

工具沒有強制費用上限；預算靠一次一張與逐張查交易控制，不是平台保證。精確報價與實扣分列，實扣以交易明細為準。

**預檢前後的交易：** 預檢前後各查一次交易明細：期間沒有新增 Soul V2 列；新增 1 列 GPT Image 2.5 −1（05:12:22Z），唯讀查生成紀錄（只看模型與時間）確認是帳號上他人的 gpt_image_2_5 任務，同一段時間沒有任何 soul_2 任務。

**參考：** M-4 R2 V-Iris 首試：精確報價 0.12、實扣 0.12（依時窗及唯一任務推定）。

**停止條件（任一成立就停，不補送）：**

- 任一筆 Soul V2 扣款高於該張精確報價 0.12
- 同一張的時窗裡出現兩筆以上 Soul V2 扣款、或有其他 soul_2 任務，無法唯一對上
- 累計扣款達到整批預算上限
- 請求逾時或結果不明（任務可能仍在跑，會混淆下一張的歸屬）
- 任何無法解釋的扣款

停下、照實回報交易原始列（只在私有紀錄）與已完成的張數；不自行補送。

**交易核對：**

- 沿用 M-4 R1／R2 已接受的方法與證據層級：送出前記下交易明細最新一列；送出一次並記下工作 ID（只寫私有執行紀錄）；輪詢到終態；查交易到涵蓋送出前最新一列，並唯讀查帳號生成紀錄（只看模型、狀態、時間）。
- 每張時窗裡新增的 Soul V2 列恰好一筆扣款（可另有一筆同額退款），同一時窗只有本次這一個 soul_2 任務，金額等於精確報價：標「依時窗及唯一任務推定」；交易明細沒有工作 ID，不標成直接對帳確認。
- 第 5 張終態後 15 分鐘，再查一次整批時窗，看有沒有遲到的扣款或退款。

## 5. 生成前核對

- 中英文：每套 8 個攝影欄位（景別、上下界、身體、臉、視線、相機、配置、目的）的英文句仍逐字在 prompt 裡（產生器程式核對）；中文摘要依已接受企劃欄位整理，只有光線句隨英文改寫。
- 服裝與手部：中英文的服裝件數、顏色與雙手位置一致；沒有新增或刪除服飾、道具。
- 景別與比例：直式 3:4、橫式 16:9，與各自工作照片框（V 120×160 mm、H 192×104 mm）相同；景別上下界照企劃。
- 器材字：改寫後 5 份 prompt 都不含 reflector、softbox、key light、fill light、ring light、strobe、light stand、out of frame 等字樣（程式核對）。
- 身分句：年齡、膚色、五官、髮色髮型、身高三圍與罩杯逐字沿用已接受 prompt（Soul V2 不繼承髮型與身材）。

**程式核對結果（產生器）：**

| 套別 | prompt 來源 | 中英攝影欄位 | 描述順序 | 器材字 | 比例／張數 |
|---|---|---|---|---|---|
| V-tammy-chou | ✓ 原文＋1 處光線改寫 | ✓ 8 個攝影欄位英文句都在 | ✓ 依序 | ✓ 沒有 | ✓ 3:4／count 1 |
| V-rin-ayase | ✓ 原文＋1 處光線改寫 | ✓ 8 個攝影欄位英文句都在 | ✓ 依序 | ✓ 沒有 | ✓ 3:4／count 1 |
| V-somi-oh | ✓ 原文＋1 處光線改寫 | ✓ 8 個攝影欄位英文句都在 | ✓ 依序 | ✓ 沒有 | ✓ 3:4／count 1 |
| H-yerin-han | ✓ 原文＋1 處光線改寫 | ✓ 8 個攝影欄位英文句都在 | ✓ 依序 | ✓ 沒有 | ✓ 16:9／count 1 |
| H-jia-seo | ✓ 原文＋1 處光線改寫 | ✓ 8 個攝影欄位英文句都在 | ✓ 依序 | ✓ 沒有 | ✓ 16:9／count 1 |

## 6. Tammy｜V-tammy-chou｜1 月｜3:4

**企劃來源：** docs/calendar/data/cal_m3_shoot_plan.json（shoot-plan-v10）sets[V-tammy-chou]；owner R6 接受（CAL_18）

**為什麼選她：** 室內夜間暖色人工光（水晶吊燈）、大腿中段以上近景、正面看鏡頭，加上小手提包道具；這三項是 V-Iris（戶外逆光、站姿）沒有測過的條件。

**為什麼是這一款：** 選直式：大腿中段以上的近景與室內暖光是本批唯一的室內條件；橫式款（花園露台全身、白天）與 H-Yerin 同屬白天戶外，資訊重複。

**canon 摘要：** 160 cm／90-57-89／E；髮：奶茶金棕大波浪長捲髮，臉側淺色 money piece 挑染（Soul V2 不繼承髮型與身材，prompt 逐字寫明）。

### 中文拍攝摘要

| 項目 | 內容 |
|---|---|
| 場景 | 夜晚大飯店的大廳：拋光大理石地板與柱子、頭頂溫暖的水晶吊燈、背景圓桌上一大盆白花，大廳沒有其他人。 |
| 服裝 | 白色合身西裝外套式迷你洋裝（深 V 翻領、金色扣子、繫腰帶）、金色垂墜耳環、素面黑色亮面小手提包（無任何標誌、不仿特定品牌）；黑色尖頭細高跟鞋不入鏡。 |
| 髮妝 | 奶茶金棕大波浪長捲髮，臉側淺色 money piece 挑染；閃粉眼影、果凍唇。 |
| 姿態與雙手 | 站在大理石柱旁，重心在一隻腳，身體正對鏡頭、肩膀打開，臀部隨重心微微偏向拎包的一側；一手拎著小手提包的短提把、包停在臀側稍微離開身體，另一手插腰，兩手都在框內。 |
| 表情 | 自信的笑容。 |
| 視線 | 臉正面，看鏡頭。 |
| 光線 | 水晶吊燈的暖色光充滿空間；右前方的柔光均勻落在臉上（R4 改寫，原為畫面外 key light）；白、金與暖色大理石色調。 |
| 景別 | 大腿中段以上｜正面｜臉正面・看鏡頭｜腰部高度・輕仰 |
| 畫面上下界 | 完整髮頂，上緣少量留白；下緣在大腿中段，不切在膝蓋。入鏡：深 V 翻領、金扣與腰帶、迷你裙擺與大腿上段；拎在臀側的小手提包與插腰的手，兩手都在框內 |

### Soul 與設定

| 項目 | 內容 |
|---|---|
| Soul | tammy-chou-soul-v1-5img-20260904（指紋 sha256 前 8 碼 `4be2d365`；ID 不寫出） |
| 紀錄位置 | kols/tammy-chou/profile.json → ai_assets.training_images_v1.soul_training.soul_id |
| 專案狀態 | production_ready；訓練圖 5 張 |
| 既有驗證 | 2026-09-07 6 張驗證：臉 6/6 通過（門檻 1、2、4）（review/soul_pilot/VERIFY_REMAINING_12.md；圖 review/soul_pilot/tammy-chou/verify_v1/） |
| 帳號查詢 | 唯讀 show_characters：同名 Soul、status ready（raw completed）；ID 與 profile 相同（程式比對，ID 不寫出） |
| 限制 | 身材不從 Soul 繼承（門檻 3 未通過，以 prompt 數字補）；碰撞門檻 5 未通過、經使用者裁決接受，須遵守 C-1（每張寫自己的髮色髮型）與 C-2（有碰撞關係者不得同框／同一組內容並排） |
| 設定 | model soul_2｜quality 2k｜aspect_ratio 3:4｜count 1｜use_unlim false｜不用參考圖｜style_id 不傳（後台套用預設 General，M-4 R2 已觀察到） |
| 存放位置 | 送出前唯讀查 get_preferences；auto_create_project 為 false 時不建專案、不指定資料夾 |
| 報價 | 顯示值 1／精確 0.12（2026-10-21（UTC 約 05:10–05:14）） |

### 相對已定稿 prompt 的修改

前：

```text
a soft key light from front-right just out of frame lights her face evenly;
```

後：

```text
soft light from the front-right falls evenly on her face;
```

理由：光線改寫成畫面效果，不再點名畫面外器材：V-Iris 首試 prompt 寫「just out of frame」的反光板仍出現在畫面裡（SEXY_SCENE_LIBRARY.md §3-F 點名物件就會出現）；主管 R4 要求光線優先描述效果。Penny 接受 Iris 的反光板不代表其他照片可以出現器材。其他字句不變。

### 完整英文 prompt（可直接送出）

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, round almond eyes with visible aegyo-sal, shimmer eyeshadow and jelly-glossy lips, long voluminous big-wave hair in milk-tea golden brown with light money-piece highlights at the front. Curvy figure, 160 cm tall, bust 90 cm, waist 57 cm, hips 89 cm, E cup, a full chest and a slim waist. She wears a white tailored blazer mini dress with a deep V lapel, gold buttons and a belted waist that defines her full chest and slim waist, gold drop earrings and a small plain black patent top-handle bag without any logos. Setting: the lobby of a grand hotel at night, polished marble floor and columns, a warm crystal chandelier overhead, a large arrangement of white flowers on a round table in the background, the lobby empty. One hand holds the short handle of the small bag at her hip, slightly away from her body, and the other rests on her waist; she smiles confidently. Shot: a mid-thigh-up shot, from a little above her head down to mid-thigh, well above the knees, showing the deep V lapel, the gold buttons and belted waist, the mini skirt hem and her upper thighs, the small bag held at her hip and the other hand on her waist, both hands inside the frame. Body: standing beside a marble column with her weight on one leg, her body square to the camera, shoulders open, her hips shifted slightly toward the side holding the bag. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with a 70mm lens from about 2.3 metres, camera at her waist height, tilted slightly upward, natural perspective without distortion. Composition: she is centred, the warm crystal chandelier glowing above her head, a marble column at one side and the white flowers soft in the background. Emphasis: a closer frame with a slightly low camera that shows her confidence, how the blazer dress defines her chest and waist, and a small plain bag. Lighting: warm chandelier light fills the space; soft light from the front-right falls evenly on her face; white, gold and warm marble tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 最重要的驗收重點

- 身分：Tammy 的臉（杏眼、臥蠶）與奶茶金棕大波浪、money piece 挑染
- 小手提包素面、不像任何品牌，沒有標誌或文字
- 兩手都在框內；提把與手指結構
- 下緣在大腿中段、不切膝；髮頂上方留白 ≥4%
- 室內暖光下膚色不過黃、臉亮度足夠

### 已知風險

- 包包像特定品牌（企劃已寫素面、圓角、細短提把）
- 包遮住腰線
- 大廳出現其他人或招牌
- 輕仰角造成腿或臉變形
- 暖光讓膚色偏黃

### 工作照片框

- 直式 3:4 工作照片框（R6 已接受）（120×160 mm）
- V 3:4：原生 1536×2048（已知）
- 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準
- 上緣：規劃髮頂留白約 6%
- 下緣：規劃裁切線在大腿中段

## 7. Rin｜V-rin-ayase｜10 月｜3:4

**企劃來源：** docs/calendar/data/cal_m3_shoot_plan.json（shoot-plan-v10）sets[V-rin-ayase]；owner R6 接受（CAL_18）

**為什麼選她：** 陰天大面積柔光、膝上景別、斜側 45 度倚靠道具、三分之二側臉不看鏡頭；測試不看鏡頭時的身分辨識。

**為什麼是這一款：** 選直式：橫式款是側躺在貴妃椅上的斜躺全身，是 24 套裡肢體結構最複雜的一張，留到第一批結果出來後再做；直式款站姿單純、條件不同。

**canon 摘要：** 166 cm／92-58-90／F；髮：深酒紅棕長髮，鬆鬆挽起的低髮髻，幾縷髮絲落在臉旁（Soul V2 不繼承髮型與身材，prompt 逐字寫明）。

### 中文拍攝摘要

| 項目 | 內容 |
|---|---|
| 場景 | 秋天午後安靜的小港灣：石砌碼頭邊一根粗木繫船柱與盤起的麻繩，平靜海面停著幾艘素面白色帆船，柔和的銀灰天光；站位在碼頭內側、離岸邊有距離，碼頭上沒有其他人。 |
| 服裝 | 深墨綠仿麂皮裹身洋裝（深 V 領、繫帶收腰、及膝、前側開衩到大腿中段）、細金耳環、細金手鍊；深棕色尖頭短跟踝靴不入鏡。 |
| 髮妝 | 深酒紅棕長髮，鬆鬆挽起的低髮髻，幾縷髮絲落在臉旁；乾淨底妝、精準眼線、豆沙紅唇。 |
| 姿態與雙手 | 背靠粗木繫船柱，身體朝畫面左轉約 45 度，重心在靠柱的那隻腳、另一膝微彎、腳尖點地，肩膀放鬆往後靠；一手往後輕扶在繫船柱上，一手輕放在腰間的繫帶上。 |
| 表情 | 平靜、帶點距離感的淺笑。 |
| 視線 | 三分之二側臉，看向畫面左側港口的出口與海面（不看鏡頭）。 |
| 光線 | 柔和的秋日午後陰天光（大面積柔光），臉均勻清楚、陰影柔和（R4 改寫，原為畫面外前方反光板）；水面銀灰反光；墨綠、銀灰與柔金色調。 |
| 景別 | 膝上｜約45度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側港口的出口與海面｜腰部高度・平視 |
| 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：裹身洋裝的深 V 領、繫帶收出的胸腰線、前開衩露出的大腿到膝蓋下方；往後扶柱的手與放在繫帶上的手 |

### Soul 與設定

| 項目 | 內容 |
|---|---|
| Soul | rin-ayase-soul-v1-5img-20260904（指紋 sha256 前 8 碼 `da07468e`；ID 不寫出） |
| 紀錄位置 | kols/rin-ayase/profile.json → ai_assets.training_images_v1.soul_training.soul_id |
| 專案狀態 | production_ready；訓練圖 5 張 |
| 既有驗證 | 2026-09-07 6 張驗證：臉 6/6 通過（門檻 1、2、4）（review/soul_pilot/VERIFY_REMAINING_12.md；圖 review/soul_pilot/rin-ayase/verify_v1/） |
| 帳號查詢 | 唯讀 show_characters：同名 Soul、status ready（raw completed）；ID 與 profile 相同（程式比對，ID 不寫出） |
| 限制 | 身材不從 Soul 繼承（門檻 3 未通過，以 prompt 數字補）；碰撞門檻 5 未通過、經使用者裁決接受，須遵守 C-1（每張寫自己的髮色髮型）與 C-2（有碰撞關係者不得同框／同一組內容並排） |
| 設定 | model soul_2｜quality 2k｜aspect_ratio 3:4｜count 1｜use_unlim false｜不用參考圖｜style_id 不傳（後台套用預設 General，M-4 R2 已觀察到） |
| 存放位置 | 送出前唯讀查 get_preferences；auto_create_project 為 false 時不建專案、不指定資料夾 |
| 報價 | 顯示值 1／精確 0.12（2026-10-21（UTC 約 05:10–05:14）） |

### 相對已定稿 prompt 的修改

前：

```text
as one large gentle source, a white reflector just out of frame in front lighting her face evenly;
```

後：

```text
as one large gentle source, her face evenly and clearly lit with soft, gentle shadows;
```

理由：光線改寫成畫面效果，不再點名畫面外器材：V-Iris 首試 prompt 寫「just out of frame」的反光板仍出現在畫面裡（SEXY_SCENE_LIBRARY.md §3-F 點名物件就會出現）；主管 R4 要求光線優先描述效果。Penny 接受 Iris 的反光板不代表其他照片可以出現器材。其他字句不變。

### 完整英文 prompt（可直接送出）

```text
A 25-year-old adult Japanese woman with her natural fair, cool-toned skin, an oval face with long narrow eyes and a straight nose, a clean base with precise eyeliner and a muted rose-red lip, long deep wine-red brown hair pinned in a loose, soft low chignon with a few strands framing her face. Curvy figure, 166 cm tall, bust 92 cm, waist 58 cm, hips 90 cm, F cup, a full chest, a slim waist and long legs. She wears a deep forest-green faux-suede wrap dress with a deep V neckline, a tie at the waist that defines her full chest and slim waist, a knee-length hem and a front slit to mid-thigh, thin gold earrings and a thin gold bracelet. Setting: a quiet small harbour on an autumn afternoon, an old stone quay with a thick wooden mooring post and a coiled rope, a few plain white sailboats moored on calm water, soft silver-grey overcast light, standing well back from the quay edge, the quay empty. One hand reaches back to rest on the mooring post and the other rests at the tie on her waist; she has a calm, slightly distant half-smile. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the deep V neckline of the wrap dress, the tie that defines her chest and waist, and her thigh through the front slit down to just below the knee, one hand reaching back to the post and the other at the tie on her waist. Body: leaning back against a thick wooden mooring post, her body turned about 45 degrees toward camera-left, her weight on the leg nearer the post and the other knee softly bent with the toes touching the ground, shoulders relaxed against the post. Face and gaze: her face in a three-quarter view, looking out toward the harbour mouth on camera-left, away from the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.6 metres, camera at her waist height, level, natural perspective without distortion. Composition: she stands just right of centre, her body and gaze turned toward the harbour mouth on the left, the water and moored white sailboats filling the space on the left, the mooring post behind her. Emphasis: leaning on the post at an angle shows both the chest and waist line of the wrap dress and the leg through the slit, and the three-quarter face toward the harbour brings a mature, quiet distance. Lighting: soft overcast autumn afternoon light as one large gentle source, her face evenly and clearly lit with soft, gentle shadows; silver-grey reflections on the water; deep green, silver-grey and soft gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 最重要的驗收重點

- 身分：三分之二側臉仍可辨識是 Rin；深酒紅棕低髮髻
- 陰天下臉不發灰
- 開衩只到大腿中段、裹身完整遮蔽
- 下緣在膝蓋下方的小腿上段、不切膝關節；髮頂上方留白 ≥4%
- 帆船與碼頭沒有文字；站位不在碼頭邊緣
- 往後扶柱的手與放在繫帶上的手

### 已知風險

- 陰天臉發灰（已改寫成「臉均勻清楚」的效果描述）
- 帆船或碼頭出現文字
- 開衩遮蔽
- 站在碼頭邊緣的危險站位
- 碰撞紀錄 Yerin–Rin（本批兩位都有，各自一張；以髮色髮型區分，不改臉）

### 工作照片框

- 直式 3:4 工作照片框（R6 已接受）（120×160 mm）
- V 3:4：原生 1536×2048（已知）
- 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準
- 上緣：規劃髮頂留白約 7%
- 下緣：規劃裁切線在膝蓋下方的小腿上段

## 8. Somi｜V-somi-oh｜12 月｜3:4

**企劃來源：** docs/calendar/data/cal_m3_shoot_plan.json（shoot-plan-v10）sets[V-somi-oh]；owner R6 接受（CAL_18）

**為什麼選她：** 冬夜室外、飄雪與燈籠、全身入鏡（含靴）、抬眼看雪不看鏡頭；夜景與全身是 V-Iris 沒有測過的條件。

**為什麼是這一款：** 選直式：雪夜全身是本批唯一的夜間室外與全身站姿；橫式款是搭景的小吃店（室內暖光、食物道具有假字風險），室內暖光已由 V-Tammy 測。

**canon 摘要：** 161 cm／91-58-90／F；髮：明亮蜜橘棕的韓式狼尾層次剪（Soul V2 不繼承髮型與身材，prompt 逐字寫明）。

### 中文拍攝摘要

| 項目 | 內容 |
|---|---|
| 場景 | 小型溫泉小鎮的街道，冬夜飄雪；低矮木造旅館掛著暖色紙燈籠、路旁石溝冒出薄薄的蒸氣，地上一層薄雪，街上沒有人。 |
| 服裝 | 象牙白貼身羅紋針織迷你洋裝（高圓領）、紅色羊毛長大衣（敞開）、白色及膝長靴、小珍珠耳環。 |
| 髮妝 | 明亮蜜橘棕的韓式狼尾層次剪；淡妝、亮澤唇釉、凍紅的臉頰。 |
| 姿態與雙手 | 站在薄雪上，重心在後腳、前腳微微向前，身體正對鏡頭、下巴微抬、肩線放鬆，敞開的大衣自然垂下；一手插在大衣口袋裡把大衣撐開，另一手在肩高攤開掌心接雪（不遮臉）。 |
| 表情 | 自然、帶點驚喜的笑，眼睛睜開。 |
| 視線 | 三分之二側臉，看向畫面右上方燈籠旁飄落的雪（不看鏡頭）。 |
| 光線 | 前左方柔和的暖光均勻落在臉上（R4 改寫，原為畫面外 key light）；背後紙燈籠的暖琥珀光、雪地上的冷藍夜色；紅、象牙白與暖琥珀色調。 |
| 景別 | 全身｜正面｜三分之二側臉・不看鏡頭：看畫面右上方燈籠旁飄落的雪｜臀部高度・平視 |
| 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到靴底完整；敞開的紅色長大衣、貼身白色針織洋裝的胸腰臀線條、白色及膝長靴；插在口袋的手與在肩高接雪的手（不遮臉） |

### Soul 與設定

| 項目 | 內容 |
|---|---|
| Soul | somi-oh-soul-v1-5img-20260904（指紋 sha256 前 8 碼 `2f7675e1`；ID 不寫出） |
| 紀錄位置 | kols/somi-oh/profile.json → ai_assets.training_images_v1.soul_training.soul_id |
| 專案狀態 | production_ready；訓練圖 5 張 |
| 既有驗證 | 2026-09-07 6 張驗證：臉 6/6 通過（門檻 1、2、4）（review/soul_pilot/VERIFY_REMAINING_12.md；圖 review/soul_pilot/somi-oh/verify_v1/） |
| 帳號查詢 | 唯讀 show_characters：同名 Soul、status ready（raw completed）；ID 與 profile 相同（程式比對，ID 不寫出） |
| 限制 | 身材不從 Soul 繼承（門檻 3 未通過，以 prompt 數字補）；碰撞門檻 5 未通過、經使用者裁決接受，須遵守 C-1（每張寫自己的髮色髮型）與 C-2（有碰撞關係者不得同框／同一組內容並排） |
| 設定 | model soul_2｜quality 2k｜aspect_ratio 3:4｜count 1｜use_unlim false｜不用參考圖｜style_id 不傳（後台套用預設 General，M-4 R2 已觀察到） |
| 存放位置 | 送出前唯讀查 get_preferences；auto_create_project 為 false 時不建專案、不指定資料夾 |
| 報價 | 顯示值 1／精確 0.12（2026-10-21（UTC 約 05:10–05:14）） |

### 相對已定稿 prompt 的修改

前：

```text
Lighting: a soft warm key light from front-left just out of frame lights her face evenly;
```

後：

```text
Lighting: soft warm light from the front-left falls evenly on her face;
```

理由：光線改寫成畫面效果，不再點名畫面外器材：V-Iris 首試 prompt 寫「just out of frame」的反光板仍出現在畫面裡（SEXY_SCENE_LIBRARY.md §3-F 點名物件就會出現）；主管 R4 要求光線優先描述效果。Penny 接受 Iris 的反光板不代表其他照片可以出現器材。其他字句不變。

### 完整英文 prompt（可直接送出）

```text
A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. Light makeup with a glossy lip, her cheeks flushed pink from the cold. She wears a fitted ivory ribbed knit mini dress with a high round neck that follows her full chest, slim waist and hips, a long red wool coat worn open, white knee-high boots and small pearl earrings. Setting: a quiet street in a small hot-spring town on a snowy winter evening, low wooden inns with warm paper lanterns, thin steam rising from a stone channel at the roadside, a light layer of snow on the ground, the street empty. One hand is in the pocket of the open coat holding it back so the fitted dress shows, and the other is raised at shoulder height with the palm up catching snowflakes, away from her face; her chin lifts slightly and she smiles with natural delight, eyes open, a few snowflakes in the air. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to boots, the open red coat, the fitted ivory knit dress over her chest, waist and hips, and the white knee-high boots, one hand in a coat pocket and the other raised at shoulder height catching snow, away from her face. Body: standing on the thin snow with her weight on her back leg and her front foot slightly forward, her body square to the camera, her chin lifted slightly and shoulders relaxed, the open coat falling naturally. Face and gaze: her face in a three-quarter view, looking up toward the snow falling beside a lantern at the upper right, away from the camera. Camera: vertical 3:4 frame, full-frame camera with a 70mm lens from about 4.2 metres, camera at her hip height, level, natural perspective without distortion; she fills about 85% of the frame height. Composition: she stands slightly left of centre, the glowing paper lanterns and falling snow at the upper right where she is looking, the street receding behind her to the right. Emphasis: her natural smile as she looks up at the snow makes the picture feel like a captured moment, and the full figure keeps the whole winter look and the curves of the dress. Lighting: soft warm light from the front-left falls evenly on her face; the paper lanterns behind her glow warm amber against the cool blue evening light on the snow; red, ivory and warm amber tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 最重要的驗收重點

- 身分：抬眼的三分之二側臉仍可辨識是 Somi；蜜橘棕狼尾
- 眼睛睜開、五官清楚，接雪的手不遮臉
- 全身含靴底、腳下留白 ≥3%、髮頂 ≥4%
- 貼身針織洋裝的胸腰臀線；大衣敞開
- 燈籠與街道沒有文字或招牌

### 已知風險

- 仰頭看不清五官（只微抬下巴）
- 接雪的手遮臉
- 雪夜臉暗或發灰
- 燈籠或招牌出現文字
- 碰撞紀錄 Jia–Somi（本批兩位都有，各自一張；以髮色髮型區分）

### 工作照片框

- 直式 3:4 工作照片框（R6 已接受）（120×160 mm）
- V 3:4：原生 1536×2048（已知）
- 比例計算：若輸出 1536×2048，約 325 ppi（1536 px／120 mm）；300 ppi 是本案工作目標、廠商門檻未知；以實際輸出為準
- 上緣：規劃髮頂留白約 10%
- 下緣：規劃雙腳與鞋下方留白約 5%

## 9. Yerin｜H-yerin-han｜5 月｜16:9

**企劃來源：** docs/calendar/data/cal_m3_shoot_plan.json（shoot-plan-v10）sets[H-yerin-han]；owner R6 接受（CAL_18）

**為什麼選她：** 第一張 16:9：晴朗晨光、坐在球車上的坐姿全身與長腿；同時驗證 16:9 的實際輸出像素與套框 ppi（企劃記為未知）。

**為什麼是這一款：** 選橫式：需要 16:9 的實際輸出來確認像素與 ppi；直式款是日落海灘逆光、膝上站姿看鏡頭，和已接受的 V-Iris（逆光黃金時段、戶外站姿、看鏡頭）太接近，資訊少。

**canon 摘要：** 170 cm／90-60-93／E（健康曲線）；髮：亞麻棕長髮、臉側金色挑染，低馬尾從球帽後方穿出（Soul V2 不繼承髮型與身材，prompt 逐字寫明）。

### 中文拍攝摘要

| 項目 | 內容 |
|---|---|
| 場景 | 晴朗春日早晨的高爾夫球場：一台素面白色球車停在車道旁，旁邊是亮綠的球道，遠方柔和的樹林，球場上沒有其他人。 |
| 服裝 | 白色無袖貼身針織高爾夫 polo、淺天空藍百褶高爾夫迷你裙、白色高爾夫鞋、素面白色球帽、小金色耳針。 |
| 髮妝 | 亞麻棕長髮、臉側金色挑染，低馬尾從球帽後方穿出；防曬淡妝、亮色唇。 |
| 姿態與雙手 | 側坐在球車前座的邊緣、身體微微往後靠，身體朝畫面左轉約 45 度；伸出車外的長腿斜向畫面左下，雙膝併攏、腳踝交叉、腳尖點地；後方的手撐在臀部後方的座椅上，前方的手輕放在併攏的膝上。 |
| 表情 | 俏皮、明亮的笑。 |
| 視線 | 臉正面，看鏡頭。 |
| 光線 | 左前上方的晴朗晨光；帽簷落在臉上的陰影柔和淺淡，眼睛與臉清楚（R4 改寫，原為畫面外大反光板）；亮綠、天空藍與白色色調。 |
| 景別 | 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 |
| 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，坐姿的雙腿與雙腳完整。入鏡：完整坐姿；白色無袖 polo 的胸型與手臂線條、百褶迷你裙、併攏交叉的長腿與白色高爾夫鞋；撐在座椅上的手與放在膝上的手 |

### Soul 與設定

| 項目 | 內容 |
|---|---|
| Soul | yerin-han-soul-v1-5img-20260904（指紋 sha256 前 8 碼 `a7d2dd33`；ID 不寫出） |
| 紀錄位置 | kols/yerin-han/profile.json → ai_assets.training_images_v1.soul_training.soul_id |
| 專案狀態 | production_ready；訓練圖 5 張 |
| 既有驗證 | 2026-09-07 6 張驗證：臉 6/6 通過（門檻 1、2、4）（review/soul_pilot/VERIFY_REMAINING_12.md；圖 review/soul_pilot/yerin-han/verify_v1/） |
| 帳號查詢 | 唯讀 show_characters：同名 Soul、status ready（raw completed）；ID 與 profile 相同（程式比對，ID 不寫出） |
| 限制 | 身材不從 Soul 繼承（門檻 3 未通過，以 prompt 數字補）；碰撞門檻 5 未通過、經使用者裁決接受，須遵守 C-1（每張寫自己的髮色髮型）與 C-2（有碰撞關係者不得同框／同一組內容並排） |
| 設定 | model soul_2｜quality 2k｜aspect_ratio 16:9｜count 1｜use_unlim false｜不用參考圖｜style_id 不傳（後台套用預設 General，M-4 R2 已觀察到） |
| 存放位置 | 送出前唯讀查 get_preferences；auto_create_project 為 false 時不建專案、不指定資料夾 |
| 報價 | 顯示值 1／精確 0.12（2026-10-21（UTC 約 05:10–05:14）） |

### 相對已定稿 prompt 的修改

前：

```text
Lighting: clear morning sun from high front-left, a large white reflector just out of frame softening the shadow of the cap on her face;
```

後：

```text
Lighting: clear morning sun from high front-left; the shadow of the cap brim on her face is soft and light, her eyes and face clearly lit;
```

理由：光線改寫成畫面效果，不再點名畫面外器材：V-Iris 首試 prompt 寫「just out of frame」的反光板仍出現在畫面裡（SEXY_SCENE_LIBRARY.md §3-F 點名物件就會出現）；主管 R4 要求光線優先描述效果。Penny 接受 Iris 的反光板不代表其他照片可以出現器材。其他字句不變。

### 完整英文 prompt（可直接送出）

```text
A 26-year-old adult Korean woman with her natural fair skin tone, bright defined features and a wide open smile, light sun-protective makeup and a bright lip, long flax-brown hair with golden face-framing highlights in a low ponytail pulled through the back of a plain white cap. Curvy athletic figure with soft feminine lines, 170 cm tall, bust 90 cm, waist 60 cm, hips 93 cm, E cup, long legs and a slim waist. She wears a white fitted sleeveless knit golf polo that follows her full chest and slim waist, a pale sky-blue pleated golf mini skirt, white golf shoes, a plain white cap and small gold stud earrings. Setting: a golf course on a clear spring morning, a plain white golf cart parked on the cart path beside a bright green fairway, soft trees in the distance, the course empty. Her back hand is braced on the seat behind her hip and her front hand rests lightly on her knees; she gives a playful, bright smile. Shot: a full-length seated shot, her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the sleeveless polo over her full chest and her toned arms, the pleated mini skirt, her long legs together with ankles crossed and the white golf shoes, one hand braced on the seat and the other on her knees. Body: sitting sideways on the edge of the golf cart front seat and leaning back slightly, her body turned about 45 degrees toward camera-left, her long legs reaching out of the cart toward the lower left with her knees together, ankles crossed and toes touching the ground, shoulders relaxed. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 4.5 metres, camera at her seated waist height, level, natural perspective without distortion; she fills about 83% of the frame height. Composition: the white golf cart sits at an angle across the frame with its front toward the left; she sits just right of centre in the open side of the cart, her long legs reaching diagonally toward the lower left, the bright green fairway behind. Emphasis: the diagonal of the cart carries her long legs into the frame and the slight lean back relaxes her body lines; the focus is her smile and leg length. Lighting: clear morning sun from high front-left; the shadow of the cap brim on her face is soft and light, her eyes and face clearly lit; bright green, sky blue and white tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 最重要的驗收重點

- 16:9 實際輸出像素；套進 192×104 mm 的有效 ppi（若 2048×1152 約 271 ppi，低於本案 300 ppi 工作目標）
- 身分：Yerin 的臉與亞麻棕金挑染低馬尾（戴帽時仍可辨識）
- 坐姿腿部結構：雙膝併攏、腳踝交叉、腳尖點地；不以裙下為構圖目的
- 帽簷陰影不遮眼睛
- 球車、衣帽沒有商標或文字
- 雙腳與鞋完整、腳下 ≥3%、髮頂 ≥4%（套框後）

### 已知風險

- 16:9 原生尺寸未知，可能低於 300 ppi 工作目標
- 裙下構圖（企劃已寫雙膝併攏、坐姿腰高平視）
- 帽簷陰影遮臉（改寫為效果描述後仍需確認）
- 球車或衣帽出現品牌標誌
- 碰撞紀錄 Yerin–Rin（本批兩位都有）

### 工作照片框

- 橫式工作照片框（R6 已接受）（192×104 mm）
- H 16:9：原生尺寸未知（推測 2048×1152，未驗證）
- 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證
- 上緣：規劃髮頂留白約 10%（套框後理論約 8.4%）
- 下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%）

## 10. Jia｜H-jia-seo｜9 月｜16:9

**企劃來源：** docs/calendar/data/cal_m3_shoot_plan.json（shoot-plan-v10）sets[H-jia-seo]；owner R7 接受（CAL_18）

**為什麼選她：** 第二張 16:9：傍晚逆光、側面坐姿、三分之二側臉看湖；逆光正是 V-Iris 反光板入鏡的情境，用來驗證改成效果描述後臉仍清楚、且不出現器材。

**為什麼是這一款：** 選橫式：提供第二個 16:9 樣本（光線、姿勢與 H-Yerin 不同），16:9 的像素與構圖不只靠一張判斷；直式款溫室全身風險較低，可放在下一批。

**canon 摘要：** 168 cm／85-58-90／C（直角肩、長腿）；髮：冷灰藍黑長髮，一側塞在耳後露出薄荷綠內層（Soul V2 不繼承髮型與身材，prompt 逐字寫明）。

### 中文拍攝摘要

| 項目 | 內容 |
|---|---|
| 場景 | 初秋傍晚安靜的湖畔：延伸到水面上的淺色木平台、一張簡潔的木製長椅，平靜湖面映著低斜的陽光，遠岸是開始轉黃的樹林，畫面沒有其他人。 |
| 服裝 | 深酒紅細針織繞頸合身短洋裝（露肩與上背、腰部明確收窄、裙長大腿中段；細緻針織，沒有運動元素或大型圖案）、黑色細帶低跟涼鞋、小銀色圈耳環。 |
| 髮妝 | 冷灰藍黑長髮，一側塞在耳後露出薄荷綠內層；水光無妝感、淡棕眼線、漸層唇。 |
| 姿態與雙手 | 側坐在長椅上，身體側面朝畫面左；雙腿交疊、伸向畫面左側，直角肩與背脊挺直；靠鏡頭的手輕放在交疊的膝上，另一手臂搭在長椅椅背上（不遮腰線）。 |
| 表情 | 冷靜、若有所思的淺笑。 |
| 視線 | 三分之二側臉，看向畫面左側的湖面與遠岸（不看鏡頭）。 |
| 光線 | 她身後偏低的初秋傍晚陽光，在頭髮與肩線勾出一圈暖色輪廓；臉從前方被柔和、清楚地照亮，不在陰影裡（R4 改寫，原為畫面外前方大反光板）；深酒紅、湖水灰藍與暖金色調。 |
| 景別 | 坐姿全身｜側面（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側的湖面與遠岸｜坐姿時的腰部高度・平視 |
| 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，坐姿的雙腿與雙腳完整。入鏡：完整坐姿；繞頸剪裁露出的直角肩與上背、收腰的合身針織、大腿中段的裙襬、交疊的長腿與黑色細帶涼鞋；放在膝上的手與搭在椅背上的手臂，不遮腰線 |

### Soul 與設定

| 項目 | 內容 |
|---|---|
| Soul | jia-seo-soul-v1-5img-20260904（指紋 sha256 前 8 碼 `6fc9be8a`；ID 不寫出） |
| 紀錄位置 | kols/jia-seo/profile.json → ai_assets.training_images_v1.soul_training.soul_id |
| 專案狀態 | production_ready；訓練圖 5 張 |
| 既有驗證 | 2026-09-07 6 張驗證：臉 6/6 通過（門檻 1、2、4）（review/soul_pilot/VERIFY_REMAINING_12.md；圖 review/soul_pilot/jia-seo/verify_v1/） |
| 帳號查詢 | 唯讀 show_characters：同名 Soul、status ready（raw completed）；ID 與 profile 相同（程式比對，ID 不寫出） |
| 限制 | 身材不從 Soul 繼承（門檻 3 未通過，以 prompt 數字補）；碰撞門檻 5 未通過、經使用者裁決接受，須遵守 C-1（每張寫自己的髮色髮型）與 C-2（有碰撞關係者不得同框／同一組內容並排） |
| 設定 | model soul_2｜quality 2k｜aspect_ratio 16:9｜count 1｜use_unlim false｜不用參考圖｜style_id 不傳（後台套用預設 General，M-4 R2 已觀察到） |
| 存放位置 | 送出前唯讀查 get_preferences；auto_create_project 為 false 時不建專案、不指定資料夾 |
| 報價 | 顯示值 1／精確 0.12（2026-10-21（UTC 約 05:10–05:14）） |

### 相對已定稿 prompt 的修改

前：

```text
a large white reflector just out of frame in front keeps her face clear;
```

後：

```text
her face stays softly and clearly lit from the front, not in shadow;
```

理由：光線改寫成畫面效果，不再點名畫面外器材：V-Iris 首試 prompt 寫「just out of frame」的反光板仍出現在畫面裡（SEXY_SCENE_LIBRARY.md §3-F 點名物件就會出現）；主管 R4 要求光線優先描述效果。Penny 接受 Iris 的反光板不代表其他照片可以出現器材。其他字句不變。

### 完整英文 prompt（可直接送出）

```text
A 22-year-old adult Korean woman with her natural fair, cool-toned skin, a small face, straight shoulders and long narrow upturned eyes, dewy no-makeup makeup with a soft brown liner and gradient lips, long cool blue-black hair tucked behind one ear so its mint-green inner layer shows. Slim, long-legged figure with soft feminine curves, 168 cm tall, bust 85 cm, waist 58 cm, hips 90 cm, C cup, a slim waist and long legs. She wears a deep wine-red fine-knit fitted halter mini dress that leaves her shoulders and upper back bare, drawn in clearly at the waist, the hem at mid-thigh, a smooth fine knit with no athletic details and no large patterns, black strappy low-heeled sandals and small silver hoop earrings. Setting: a quiet lakeside on an early-autumn evening, a pale wooden deck reaching over the water, a simple wooden bench at its edge, calm water holding the low sunlight, a far shore of trees just turning yellow, nobody else in sight. One hand rests lightly on her crossed knee and the other arm lies along the bench back, clear of her waist; she has a cool, thoughtful half-smile. Shot: a full-length seated shot, her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the bare shoulders and upper back of the halter cut, the fitted knit drawn in at her waist, the hem at mid-thigh, her long crossed legs and the black strappy sandals, one hand on her knee and the other arm along the bench back, nothing covering her waist. Body: sitting sideways on the bench, her body side-on to the camera, facing camera-left, her legs crossed and reaching toward camera-left, her straight shoulders and back upright, one arm along the bench back. Face and gaze: her face in a three-quarter view, looking out over the lake toward the far shore on camera-left, away from the camera. Camera: horizontal 16:9 frame, full-frame camera with a 70mm lens from about 5.4 metres, camera at her seated waist height, level, natural perspective without distortion; she fills about 85% of the frame height. Composition: she sits just right of centre facing the lake on the left, leaving space on the left for the water and her gaze, the deck and the far tree line soft on the right. Emphasis: sitting sideways draws her straight shoulders, bare upper back, cinched waist and long crossed legs into clean lines, and the three-quarter face toward the lake carries a calm early-autumn mood. Lighting: low early-autumn evening sun behind her draws a warm rim along her hair and shoulders; her face stays softly and clearly lit from the front, not in shadow; deep wine red, soft lake blue-grey and warm gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 最重要的驗收重點

- 逆光下臉清楚、不暗
- 畫面裡沒有反光板、燈具或任何拍攝器材
- 身分：三分之二側臉仍可辨識是 Jia；冷灰藍黑長髮與薄荷綠內層
- 交疊的腿與涼鞋完整、腳下 ≥3%；手臂不遮腰線
- 針織是細緻合身，不變成厚毛衣或運動感
- 16:9 實際像素與套框 ppi

### 已知風險

- 逆光臉暗（原 prompt 用反光板處理；本輪改寫為效果描述）
- 器材入鏡（原 prompt 點名過反光板）
- 短裙坐下時遮蔽不明（企劃已寫裙長大腿中段、雙腿交疊）
- 16:9 原生尺寸未知，可能低於 300 ppi 工作目標
- 碰撞紀錄 Jia–Somi（本批兩位都有）

### 工作照片框

- 橫式工作照片框（R6 已接受）（192×104 mm）
- H 16:9：原生尺寸未知（推測 2048×1152，未驗證）
- 規劃估算：若輸出 2048×1152，約 271 ppi，低於本案 300 ppi 工作目標（不是已確認的廠商最低標準）；16:9 實際輸出尺寸未知，待驗證
- 上緣：規劃髮頂留白約 8%（套框後理論約 6.7%）
- 下緣：規劃雙腳與鞋下方留白約 7%（套框後理論約 5.3%）

## 11. 生成後（主管另發整批生成指令之後）

- 逐張驗收：身分、髮色髮型、身材、服裝、姿態與手指、表情與視線、場景（含沒有器材與文字）、景別與上下界、質感、套框與有效 ppi。
- 16:9 兩張記錄實際像素與套進 192×104 mm 的有效 ppi；不放大補像素。
- 有碰撞紀錄的兩位（Jia–Somi、Yerin–Rin）在頁面與送審資料裡不並排展示（C-2）。
- 不修圖、不重生；有落差照實回報，交主管與 Penny 判斷。
