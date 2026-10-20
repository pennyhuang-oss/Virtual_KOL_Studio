TASK-CAL-001／M-3／R7｜V-Iris 首試準備（M-4 前置作業；未生成、未授權）

# CAL_20 — V-Iris 首試準備（M-4 前置作業）

> 資料檔：`data/cal_m3_shoot_plan.json`（shoot-plan-v7，R7）的 `m4_prep` 與 `V-iris-chen`。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。
> **準備文件：只整理既有資料與首張驗收條件。沒有生成、沒有花 credits、沒有呼叫 Higgsfield、沒有做報價預檢；不是生成授權、不是費用核准，也不是印刷驗收。**
> 本輪：生成 0、credits 0、Higgsfield 呼叫 0、報價預檢 0。

## 1. 已接受的 V-Iris 企劃

| 項目 | 內容 |
|---|---|
| 接受狀態 | 已接受（R4 owner 紀錄；R5 主管核可補上英文妝感句；R6、R7 維持）。Penny 不需要再選企劃。 |
| 月份與款式 | 直式款 9 月，生成比例 3:4（直式） |
| 主題 | 黃金時段的河濱草地，白色方領短上衣配牛仔迷你裙，正面站著甜笑（Penny 指定的穿搭）。 |
| 場景 | 台北河濱公園的開闊草地，傍晚太陽低，遠處柔綠樹林與低矮公寓，草地與小徑空無一人。 |
| 服裝 | 上身：白色貼身羅紋方領短袖短上衣（露腰）；下身：淺藍高腰牛仔迷你裙；鞋：白色低筒帆布鞋（不入鏡）；配件：小金色圈耳環 |
| 姿態與手 | 站在草地上。一手插腰，一手輕碰太陽穴旁的頭髮。 |
| 表情與視線 | 明亮溫暖的笑；看鏡頭 |
| 攝影 | 大腿中段以上｜正面｜臉正面・看鏡頭｜胸口高度・平視；85mm、約 2.9 公尺；人物置中；頭頂上方少量留白，兩側是柔焦的草地與樹林，夕陽輪廓光落在頭髮與肩線 |
| 光線 | 主光：她身後側方的低角度夕陽，頭髮與肩線一圈暖色輪廓光；補光：畫面外前方的大反光板加柔光，臉與身體均勻 |
| 妝髮 | 黑色柔順直髮自然垂放過肩。乾淨的日常妝、自然唇色。 |
| 身材設定 | 162 cm／87-58-90／D；貼身方領短上衣清楚呈現 D 罩杯胸型、露出細腰；高腰牛仔迷你裙強調腰臀比與腿長。 |
| 已知風險 | 逆光臉暗（寫明反光板與柔光補臉）；膚色被夕陽拍偏（只寫一次她原本的白皙膚色）；碰頭髮的手指融合（生成後放大檢查；不行改成兩手插腰） |

## 2. 身分參考

| 項目 | 內容 | 來源檔 |
|---|---|---|
| 身分來源 | Iris 既有的 Soul（狀態見「真正生成前仍需確認」）。Soul ID 不寫進企劃、頁面或本文件；生成時從專案既有紀錄取用，並由主管指令核對。 |  |
| 人設外貌（設定，不改） | 22 歲台灣女生；圓臉甜美型、大雙眼皮深棕色眼睛、精緻鼻梁、飽滿嘴唇、小下巴；黑色柔順直髮自然放下；162 cm、87-58-90、D 罩杯，嬌小沙漏比例。 | `kols/iris-chen/profile.json（identity.appearance）` |
| prompt 開頭的身分句 | A 22-year-old adult Taiwanese woman with her natural fair skin tone, a round sweet face with large bright double-eyelid eyes and full lips, black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, a full chest, a slim waist and rounded hips. |  |
| Soul V2 不繼承的部分 | 髮型、髮色與身材不從 Soul 繼承，已在身分句寫明黑色直髮過肩與身材數字（Soul V2 不繼承髮型與髮色：每張 prompt 都要寫她自己的髮色髮型（原則七 C-1）。Soul V2 不繼承身材：身材要用 prompt 句子補（數字直接寫）。） |  |
| 企劃參考照片（只用於企劃，不送進生成） | iris-04（場景）：草地、夕陽光線氛圍（Penny 喜歡的照片）；不採用回頭姿勢；iris-06（服裝材質）：白短上衣＋牛仔短裙的穿搭方向。首試不掛參考圖、不掛 Reference Element。 |  |

## 3. 最終 prompt 與生成比例

**生成比例：** 3:4 直式；R6 已接受的直式工作照片框 120×160 mm（3:4 放入 3:4 框不裁切）。

prompt（已接受版本，3:4，尚未執行；與企劃頁「prompt 草稿」逐字相同）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a round sweet face with large bright double-eyelid eyes and full lips, black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, a full chest, a slim waist and rounded hips. Fresh, light everyday makeup with a natural lip colour. She wears a fitted white ribbed square-neck short-sleeve crop top that shows the shape of her chest and her bare waist, a high-waisted light-blue denim mini skirt and small gold hoop earrings. Setting: an open riverside lawn in a Taipei park in the late afternoon, soft green trees and low distant apartment blocks far behind her, the lawn and the path empty. One hand rests on her hip and the other lightly touches her hair at her temple; she smiles brightly and warmly. Shot: a mid-thigh-up shot, from a little above her head down to mid-thigh, well above the knees, showing the square-neck crop top, her bare waist, the whole denim mini skirt and her upper thighs, one hand on her hip and the other at her hair. Body: standing with her weight on one leg, her body square to the camera, shoulders level and relaxed, her hips shifted slightly to one side. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 2.9 metres, camera at her chest height, level, natural perspective without distortion. Composition: she is centred with a little space above her head and the soft lawn and trees on both sides. Emphasis: Penny's chosen outfit up close, the crop top on her chest, her bare waist and the denim mini skirt, with her bright smile. Lighting: the low sun behind her and to one side draws a warm rim along her hair and shoulders; a large white reflector and a soft fill light just out of frame in front of her light her face and body evenly; warm golden tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

## 4. 工作流（依既有專案資料；前提未滿足前不執行）

| 步驟 | 內容 | 來源檔 |
|---|---|---|
| 0. 前提 | Penny 核定這套造型與費用，再由主管另發 M-4 指令；沒有這兩件事之前，下面所有步驟都不做。 | `docs/calendar/data/cal_m3_shoot_plan.json（execution.cost.iris_first.plan「前提」）` |
| 1. 核對工具當下的參數 | 生成前以工具當下的說明為準，核對 soul_2 的可用參數與比例。上一次唯讀紀錄：2026-10-12 唯讀查詢 Higgsfield models_explore(get, soul_2)：參數只有 quality（1.5k／2k，預設 2k）、Soul ID、1 張參考圖；比例 1:1、16:9、9:16、4:3、3:4、3:2、2:3；沒有 seed、沒有 negative prompt；回傳沒有價格。與 AI_PROMPT_METHOD_REVIEW.md（2026-09-03）記錄一致。 | `docs/calendar/data/cal_m3_shoot_plan.json（meta.aaliya_sources.model_check）` |
| 2. prompt 送出前檢查 | 用下方「送生成前檢查」逐項核對（SEXY_SCENE_LIBRARY.md §25 的 10 項＋PHOTO_DIRECTION_STANDARD.md §七）；R7 已預先核對一次，結果見表。prompt 用企劃頁的 V-iris-chen 原文，一字不改。 |  |
| 3. 送出前查交易明細 | 送出前查一次交易明細，記下最後一筆；不用餘額對帳（帳號同時有其他人在用）。 |  |
| 4. 送出 1 個請求 | 設定照企劃：soul_2＋Iris 既有 Soul、quality 2k、aspect 3:4、count 1、不掛參考圖、use_unlim false；一次只送一個請求。 | `docs/calendar/data/cal_m3_shoot_plan.json（execution.cost.iris_first.plan「設定」）` |
| 5. 取得結果並實際看圖 | status=completed 不等於成功：每一張都要實際打開看（SEXY_SCENE_LIBRARY.md QA-2）；小區域（手指、眼睛）判讀不用插值放大（QA-1）。 |  |
| 6. 送出後查交易明細 | 記錄這一張的實際扣款（逐筆）；失敗也可能扣款，一樣記錄。 |  |
| 7. 不自動重試 | 無論結果好壞、成功或失敗，都先停下回報（企劃「重試」規則；優先於 SEXY_SCENE_LIBRARY.md §10-a「瑕疵可直接重生」的一般做法）。 |  |
| 8. 依驗收條件逐項判定 | 下方首張驗收條件；記錄實際像素、套框結果與有效 ppi。 |  |
| 9. 回報 | 把圖、設定、實扣與逐項驗收結果交主管覆核，再給 Penny 看；設定落差（環境、服裝、道具）不自行重生，交 Penny 判斷（SEXY_SCENE_LIBRARY.md §10-a）。 |  |

## 5. 送生成前檢查（R7 預先核對；送出當下要再核一次）

依 `SEXY_SCENE_LIBRARY.md` §25（Prompt Preflight Lint 10 項）與 `PHOTO_DIRECTION_STANDARD.md` §七（送生成前的稽核）。能機械判斷的項目由產生企劃資料的程式核對。

| 檢查 | 結果 | 說明 |
|---|---|---|
| §25-1 需要幾隻手（≤2） | 符合 | 兩隻：一手插腰、一手輕碰太陽穴旁的頭髮；沒有自拍手機。 |
| §25-2 自拍手機是否入鏡 | 不適用 | 不是自拍；prompt 沒有 phone／selfie。 |
| §25-3 中文規格的姿勢與表情是否真的在英文 prompt 裡 | 符合 | 「一手插腰，一手輕碰太陽穴旁的頭髮」「明亮溫暖的笑」都在英文句裡（程式比對）。 |
| §25-4 只描述一個靜止表情 | 符合 | 沒有 then／breaking into／just starting to。 |
| §25-5 動態衣物或髮絲 | 不適用 | 沒有寫飄動；頭髮自然垂放。 |
| §25-6 髮長有明確幾何描述 | 符合 | black silky straight hair worn down past her shoulders。 |
| §25-7 主要服裝 ≤3–4 件，最不能錯的在前 | 符合 | 入鏡 3 件：白色方領短上衣（第一）、淺藍高腰牛仔迷你裙、小金色圈耳環；白色帆布鞋不入鏡、不寫進 prompt。 |
| §25-8 visible pores 只用在看得到臉部細節的景別 | 符合 | 大腿中段以上、85mm，臉部細節可見；不是全身遠景。 |
| §25-9 機位高度、視線、頭部朝向一致 | 符合 | 相機在胸口高度平視；臉正面、看鏡頭。 |
| §25-10 一段 prompt 只對應一張 | 符合 | 只有一個景別（大腿中段以上），count 1。 |
| §七 機位寫離地公分數 | 與稽核表不同（已接受版本照舊） | prompt 寫「camera at her chest height」，沒有寫公分；企劃參考值約 1.19 公尺（胸口高度）。R7 不改已接受的 prompt。 |
| §七 鏡頭水平 | 符合 | level，俯仰換算約 −0.1 度。 |
| §七 焦段與距離 | 符合 | 85mm、約 2.9 公尺（不是全身照；全身 3–5 公尺的條目不適用）。 |
| §七 腳在下 1/3、上方留白 | 不適用（腳不入鏡） | 大腿中段以上；規劃髮頂留白約 8%。 |
| §七 兩隻手分別在哪 | 符合 | 插腰、碰頭髮；沒有僵直垂在身側。 |
| §七 道具互動或側身回望，不正面直視鏡頭 | 與稽核表不同（依 Penny 指定） | Penny 指定 Iris 身體面向鏡頭、有笑容、不要背部回眸或轉頭；所以正面看鏡頭。 |
| §七 表情與姿勢是同一個連續動作 | 符合 | 站定、插腰碰髮、明亮的笑。 |
| §七 主光打在臉上、背景光與臉部光一致 | 與稽核表不同（企劃選擇，列驗收） | 主光是她身後側方的低角度夕陽（輪廓光），臉靠前方大反光板與柔光；風險「逆光臉暗」已列，出圖後檢查臉部亮度與光向一致。 |
| §七 皮膚寫毛孔與質感，沒有 smooth／flawless／porcelain | 符合 | Natural skin texture with visible pores, unretouched。 |

## 6. 現在能準備的

- V-iris-chen 的企劃內容與最終 prompt（已接受版本，R7 不改）。
- 生成比例 3:4 與直式工作照片框 120×160 mm（R6 已接受）。
- 身分句與身材數字（寫在 prompt 開頭）；Soul 使用方式（ID 不公開）。
- 送生成前檢查的預先核對結果（第 5 節）。
- 首張驗收條件與套框、有效 ppi 的計算方式。
- 送出前後查交易明細的對帳步驟與回報格式。

## 7. 真正生成前仍需確認（不猜測）

| 項目 | 目前狀態 | 來源檔 |
|---|---|---|
| 生成與費用授權 | 目前沒有：需要 Penny 核定造型與費用，再由主管另發 M-4 指令。 |  |
| 模型與參數 | 上一次唯讀紀錄是 2026-10-12（soul_2：quality 1.5k／2k、Soul ID、1 張參考圖、比例含 3:4、沒有 seed 與 negative prompt）。生成當下是否相同，未確認。 |  |
| Iris 的 Soul 狀態 | ready（較早訓練；R1 紀錄寫這幾位不在 Soul 總表內，是否跑過同樣的 6 張驗證未知）。 |  |
| 輸出尺寸 | 歷史紀錄：Iris 先前用 soul_2＋Soul、2k、3:4 生成 7 次，輸出皆 1536×2048。這一張的實際像素要出圖後確認，不預先當成事實。 | `kols/iris-chen/generation_notes.md 第 971–973 行` |
| 費用 | 2026-10-13 的預檢回傳 credits 1／credits_exact 0.12（soul_2＋Iris Soul、2k、3:4、count 1），是一週前的報價、不是實扣；生成前要不要重新預檢由主管決定（R7 不做）。歷史紀錄互相不一致：Soul V2 的交易明細每筆 −0.12；但 Iris 的生成筆記記錄 2026-08-05 一批「全批 14 張約 8 credits」（7 位角色各 2 張，「約」數，沒寫怎麼算）。實扣只能用送出前後的交易明細確認。 | `kols/iris-chen/generation_notes.md 第 448–453 行`、`docs/calendar/data/cal_m3_shoot_plan.json（execution.cost）` |
| 免費額度 | 企劃設定 use_unlim false（查詢時帳號沒有可用的免費額度）；生成當下的狀態未確認。 |  |
| 失敗與上限 | 失敗也可能扣款；企劃是只送 1 個請求、不自動重試。若要允許重試或設定累計上限，需要主管另外指示。 |  |
| 已接受 prompt 與稽核表的差異 | 機位沒寫公分數、正面直視鏡頭、逆光主光三項與稽核表不同；前兩項是已接受內容與 Penny 指定，第三項是企劃選擇並列入驗收。R7 不改 prompt；若主管要調整，需另行指示。 |  |

## 8. 首張驗收條件

### 身分與身材

- [ ] 臉與 Iris 人設一致：圓臉甜美、大雙眼皮深棕眼、飽滿嘴唇、小下巴；不像另一個人。
- [ ] 膚色是她原本的白皙自然，沒有被夕陽拍偏或過飽和（風險：膚色被夕陽拍偏）。
- [ ] 黑色柔順直髮自然垂放過肩；成人樣貌。
- [ ] 身材比例符合 162 cm、87-58-90、D：胸部飽滿、腰細、臀部有形；不是童顏或身材縮水。

### 服裝

- [ ] 白色貼身羅紋方領短袖短上衣，露出腰；呈現胸型但不走光。
- [ ] 淺藍高腰牛仔迷你裙，整條入鏡。
- [ ] 小金色圈耳環；鞋不入鏡。
- [ ] 衣服上沒有亂碼文字、品牌或多餘配件。

### 姿態與手指

- [ ] 身體正對鏡頭站立，重心在一腳、臀部微偏；沒有回頭或轉身。
- [ ] 一手插腰、一手輕碰太陽穴旁的頭髮；兩隻手各五指，沒有融合、黏連或多指（風險：碰頭髮的手指融合）。
- [ ] 沒有多餘肢體；掃過畫面四角與背景（SEXY_SCENE_LIBRARY.md §10）。
- [ ] 手指判讀用原生解析度或零插值放大（QA-1）。若手指壞掉，只記錄、停下回報；改成兩手插腰要另外的指令。

### 表情與視線

- [ ] 明亮溫暖的笑，只有一個表情。
- [ ] 看鏡頭；眼睛對焦清楚。

### 場景

- [ ] 台北河濱公園開闊草地、傍晚低太陽、遠處柔綠樹林與低矮公寓。
- [ ] 草地與小徑沒有可辨識臉的路人；若遠處有失焦、認不出臉的人形，依 SEXY_SCENE_LIBRARY.md §3-F 第三次補正不算瑕疵，但與企劃「空無一人」有落差，要記錄回報。
- [ ] 沒有招牌或亂碼文字；背景不像拼貼、沒有糊掉的區塊。
- [ ] 光向一致：夕陽在她身後側方形成頭髮與肩線輪廓光，臉由前方補光照亮、不暗（風險：逆光臉暗）。

### 構圖

- [ ] 直式 3:4；大腿中段以上，下緣在大腿中段、明顯高於膝蓋。
- [ ] 人物置中、頭頂上方少量留白（規劃約 8%）；兩側是柔焦的草地與樹林。
- [ ] 雙手都在畫面內；85mm 自然透視、沒有廣角變形；水平不歪。

### 質感

- [ ] 自然皮膚紋理、看得到毛孔，不過度光滑或蠟感。
- [ ] 專業寫真質感，不是手機自拍感。

### 生成後套框與有效 ppi

- [ ] 記錄實際輸出像素（預期 1536×2048，以實際為準）。
- [ ] 套進直式工作照片框 120×160 mm：3:4 放入 3:4 不裁切；若實際不是 3:4，記錄裁切量與位置。
- [ ] 套框後髮頂上方 ≥4%，臉與雙手都在框內。
- [ ] 有效 ppi＝實際寬度像素 ÷（120 mm ÷ 25.4）；1536 px 約 325 ppi。300 ppi 是本案工作目標，不是廠商已確認的門檻。
- [ ] 不靠放大補像素；這是工作版型核對，不是印刷驗收（廠商規格與實際套版仍未知）。

### 判定與回報

- [ ] 逐項寫「符合／不符合／待 Penny 判斷」，附實圖與實際扣款。
- [ ] 通過也好、不通過也好，都先停下交主管覆核；不自動重試。

## 9. 這份文件不代表

- 不代表已生成：本輪生成 0 張。
- 不代表費用核准：credits 0、Higgsfield 呼叫 0、報價預檢 0。
- 不代表印刷驗收：照片框是本案工作版型，不是廠商規格或印刷安全。
- 不重新請 Penny 選企劃：V-iris-chen 已接受。
