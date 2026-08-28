# Nico Pilot — Phase C 20 段 prompt 覆核（生成前最後一關）

## §0 給審閱者

**你只需要讀這一個檔案。** 不要用 GitHub 連接器去抓 repo 裡的其他檔案——
背景、規則、判斷所需的一切都在這份檔案裡。

**回覆方式**：把意見寫在本檔案最下方 §7 回覆區（`REPLIES BELOW` 那行以下），然後 commit。
那一段不會被自動產生覆蓋。

- 目前 commit：`40e7a3f`
- 議題編號請從 **C-34** 起跳，每條標 **P0**（必須先修才能生成）／**P1**／**P2**

---

## §1 現在在哪一步

**Virtual KOL Studio** 是虛擬 KOL 資料庫。要讓同一個角色在不同素材裡長得像同一個人，
必須先用一組**建模照**訓練身分模型（Higgsfield Soul V2）。Nico Tsai 是 Batch 3 的 pilot。

你（ChatGPT）已經覆核過九輪，那九輪針對的是**計畫**：結構、配額、欄位矛盾、
物理一致性、gate 設計。結果：

- `tools/validate_shoot_plan_v2.py` exit 0
- 20 列九欄語意逐列覆核 **20/20**（你在 R8/R9 簽核）
- 對抗測試 26/26

**然後我們第一次真的去生成，結果全錯。** 這是本輪的關鍵背景——
計畫層的 QA 管的是「這個計畫成不成立」，管不到「這段文字送進模型會被怎麼解讀」。

目前進度：

| 階段 | 狀態 |
|------|------|
| A 選角（4 個候選 identity）| ✅ 使用者選定 candidate_03 |
| Reference Element 錨點 | ✅ `nico-tsai-anchor` 已建立 |
| B1 驗重現 | ✅ 臉完全重現 |
| B2 驗輕度外推（全身＝身材最終把關）| ✅ 第一次失敗、修正後通過 |
| **C 訓練集 20 張** | **← 本輪覆核的對象，尚未生成** |
| Soul 訓練 → D 壓力測試 | 未開始 |

**尚未生成任何一張訓練圖。你放行才會開始花這 20 張的 credit。**

---

## §2 實測得到的模型行為規則（判斷 prompt 時請以這些為準）

這些不是理論，是前三輪燒掉 13 張換來的。**每一條都有前後對照。**

### 2-1 這個模型不執行否定句

首批 4 張同時出現五個缺陷，全部源自否定句被忽略：

| 失效寫法（否定）| 有效寫法（正面描述目標狀態）|
|----------------|---------------------------|
| `nothing below the knee is visible` | `the bottom edge of the picture cuts straight across her thighs` |
| `NOT a crop top, no exposed midriff` | `the hem is long and tucked into her trouser waistband` |
| `no ombré, no dark roots, no lightened tips` | `a single flat salon dye job done right down to the scalp: the hair at her roots is exactly the same brown as the ends` |
| `NOT a full-length shot` | （刪除，改由「下緣切在哪裡」承擔）|

**顏色排除仍然有效**（`not tanned` 有效），**構圖與服裝結構的否定完全無效**。

### 2-2 身體朝向不能寫角度

`turned about 30 degrees toward her own left` 連續**三次**被畫成背影
（Round 2 首批、Round 3 的 c01、B2 第一次）。`her back is not toward the camera` 無效。

有效寫法是描述**相機看得到哪些身體正面特徵**：

> Her navel and the front of both shoulders point toward the camera. Both of her collarbones are
> visible. The camera sees the front of her jeans — the fly, the button and the front pockets —
> not the back pockets.

一次就對。**因此本批 20 段的朝向一律用這個寫法，不出現任何角度數字。**

### 2-3 景別指令要放最前面，而且要說「下緣切在哪裡」

景別失效在本 repo 已經發生三次（rainie R1、nico R1、nico Round 2），
R1 記的修法「放第一行＋排他措辭」實測**無效**。有效的是把畫面下緣的位置講出來。

### 2-4 Reference Element 會把「同一件衣服」整件複製

B1 指定與錨點同一件炭灰高領毛衣 → 錨點那件衣服的**兩道窄露肩開口**原封不動跟著出現，
即使 prompt 明寫 `unbroken and continuous over both shoulders, a complete shoulder seam on each side`。
B2 指定完全不同的衣服 → 開口消失。

**→ 指定同一件衣服時，錨點的版本會覆蓋 prompt；指定不同衣服時 prompt 才有效。**

### 2-5 錨點的髮色細節蓋不掉

candidate_03 左側髮際有一段銀灰挑染。c03 → B1 → B2 三張全部保留，
三次 prompt 都明寫「單一平染、任何一段都沒有較淺的部分」。**已經是身分的一部分。**

---

## §3 錨點與使用者已裁決的兩件事

### 3-1 銀灰挑染：保留

使用者裁決（2026-08-28）保留為 Nico 的造型。理由：美業從業者染這個完全合理，
而且三次明確指令都蓋不掉，重建錨點不保證做得掉。

**因此 20 段 prompt 一律把它寫成刻意的挑染**，而不是每次徒勞地要求消除：

> Her hair is a chin-length bob in a cool-toned medium chestnut brown — a muted mushroom brown with a soft grey undertone. One narrow band of silver-grey runs through the hair at her left temple, the way a deliberate salon highlight sits in otherwise evenly dyed hair. Apart from that one band the colour is a single flat dye reaching the scalp: her roots are the same brown as her ends.

### 3-2 outfit_01：衣櫃定義改為誠實描述錨點實際的樣子

`nico_outfit_01` 就是錨點圖身上那件。依 §2-4，20 張裡有 5 張用這件
（`a01`／`a02`／`a03`／`a07`／`c07`，其中 4 張是 clean anchor），
那 5 張一定會帶出兩道窄露肩開口。

**我的處置**：把開口寫進衣櫃定義，讓它變成刻意的款式，而不是讓 prompt 與出圖永遠對不上。

> A fitted charcoal-grey ribbed knit long-sleeve top with a high mock neck that sits close against her throat, and a narrow open slit cut across the top of each shoulder that shows a sliver of skin. Black high-waisted straight-leg tailored trousers. Black leather loafers. A beige canvas tote. One thin silver ring and small silver hoop earrings.

**這是 §6 第 3 題要請你判斷的事。**

### 3-3 身材設定變更

使用者裁決把胸型由 C 放寬為 D（90-59-88）。原本的 `small natural bust with a shallow curve`
＋ `NOT heavy-chested` 與使用者偏好不符，而且那組否定詞正是把身形往平板推的原因。

### 3-4 臉部骨架改版

使用者看到第一輪出圖就指出「五官跟庫裡既有角色 rainie-hsu 太像」。
比對確認屬實——那是模型的預設美女臉。骨架改為**少女短臉型**：
下半臉短、下巴小而窄、額頭寬、雙頰圓潤、大而圓的眼睛、顴骨低、鼻短鼻頭微翹、人中短小嘴。

**這一類判斷不在你的職責範圍**——它不是對錯問題而是「這個角色該長什麼樣」，
已列入 `review/README.md` 的「必須由使用者拍板」清單。列在這裡只是讓你知道背景。

---

## §4 這 20 段 prompt 是怎麼產生的

**不是手寫的。** `tools/build_phase_c_prompts.py` 從 `pilot/nico_pilot.json` 的結構欄位組出來，
欄位改了 prompt 就跟著改。理由：R3 已經證實人工抄寫必然漂移。

組裝順序（固定）：

```
錨點引用 → 景別（下緣切在哪裡）→ 動作 → 身體朝向（正面特徵）→ 頭部角度 → 俯仰
→ 視線 → 表情 → 臉部遮擋 → 誰在拍 → 左手 → 右手 → 其他入鏡物件
→ 素顏/膚色 → 髮色＋髮型 → 服裝五層 → 場所 → 光線五段 → 相機 → 濾鏡與不完美 → 排除清單
```

中文欄位（scene／手部註記／道具名／光線五段）有一層對應的英文，
存在 `pilot/phase_c_actions_en.json`。**這層中英對應正是 §6 第 2 題要請你核的。**

服裝與髮型的英文已移進 `nico_pilot.json` 本身（原本放在 builder 裡，
那會構成第二份真理來源——也就是你 R1 開的 C-01 那個病）。

---

## §5 20 段 prompt 全文

**20 段裡逐字重複的樣板**，抽出來只印一次；下面各段以 `[[Sn]]` 代替，
**實際送進模型時是完整文字**。這樣做只是為了控制這份檔案的體積。

- `[[S1]]`（出現 20 次）：Her hair is a chin-length bob in a cool-toned medium chestnut brown — a muted mushroom brown with a soft grey undertone. One narrow band of silver-grey runs through the hair at her left temple, the way a deliberate salon highlight sits in otherwise evenly dyed hair. Apart from that one band the colour is a single flat dye reaching the scalp: her roots are the same brown as her ends.
- `[[S2]]`（出現 5 次）：She is wearing: A fitted charcoal-grey ribbed knit long-sleeve top with a high mock neck that sits close against her throat, and a narrow open slit cut across the top of each shoulder that shows a sliver of skin. Black high-waisted straight-leg tailored trousers. Black leather loafers. A beige canvas tote. One thin silver ring and small silver hoop earrings.
- `[[S3]]`（出現 19 次）：Real skin texture with visible pores and fine flyaway hairs. She is the only person in the picture — no other people and no one else's hands. No phone is in the picture. No photography equipment of any kind: no softbox, no reflector, no foam board, no light stand, no tripod, no backdrop.
- `[[S4]]`（出現 20 次）：Her face is bare: her lips are the same soft pinkish-beige as the skin around them, matte, with a soft undefined edge; her eyebrows are soft and natural; her lashes are her own and unmade. Light neutral-to-cool skin with natural tonal variation and visible pores.
- `[[S5]]`（出現 11 次）：Her body is angled so one hip is nearer the lens, but the camera still sees the front of her chest: both collarbones are visible and the far shoulder is only a little further from the camera than the near one. Her back is not toward the camera.
- `[[S6]]`（出現 18 次）：Shot on the rear camera of a phone. No lens distortion. Adequate depth of field — her face, her body and the background are all in reasonable focus. This is not a shallow blurred-background portrait; her body outline stays sharp and readable.
- `[[S7]]`（出現 5 次）：She is wearing: A cream cropped knit top with a plain round crew neckline, the hem ending at her natural waist. High-waisted light-wash straight-leg jeans. White canvas sneakers. A small dark-brown box bag. Silver hoop earrings.
- `[[S8]]`（出現 4 次）：The whole of her is inside the picture, from the top of her head down to her shoes, with a margin of empty ground below her feet and a little space above her head. Her legs and shoes are clearly visible.
- `[[S9]]`（出現 6 次）：The bottom edge of the picture cuts across her chest, a little below her armpits. Her head, shoulders and upper chest fill the frame. Her waist, hips, legs and feet are outside the picture.
- `[[S10]]`（出現 4 次）：The bottom edge of the picture cuts across her waist at about the level of her navel. Her head, shoulders, chest and waist fill the frame. Her hips, legs and feet are outside the picture.
- `[[S11]]`（出現 4 次）：The bottom edge of the picture cuts across her legs just below the knees. Her head, torso, hips and thighs are all inside the frame. Her lower legs and feet are outside the picture.
- `[[S12]]`（出現 4 次）：Her head is turned a little toward her own left, so the camera sees slightly more of the right side of her face; her far cheek and both eyes are still fully visible.
- `[[S13]]`（出現 5 次）：Her head is turned a little toward her own right, so the camera sees slightly more of the left side of her face; her far cheek and both eyes are still fully visible.
- `[[S14]]`（出現 4 次）：The camera sees the front of her upper body: her chest and both shoulders face the lens and both collarbones are visible.
- `[[S15]]`（出現 4 次）：Setting: a paved path through an ordinary neighbourhood park in Taipei, low shrubs and a row of trees.
- `[[S16]]`（出現 8 次）：Her eyes are directed off past the camera at something in the distance, not at the lens.
- `[[S17]]`（出現 18 次）：Someone standing near her is holding the phone and taking this photo of her.
- `[[S18]]`（出現 5 次）：Her chin is dipped, so her face tilts downward and her eyelids read lower.
- `[[S19]]`（出現 20 次）：A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
- `[[S20]]`（出現 4 次）：Her chin is raised a little, so her face tilts slightly upward.

下面每一段：左邊是該列的結構欄位（真理來源），右邊是產生出來的 prompt。

### 1. `nico_a01` — identity_core／anchor

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **咖啡廳靠窗的位子坐著，正對鏡頭，沒有在做任何事** |
| framing / view | `face_closeup` / `third_person` |
| head_yaw / pitch / gaze | `front` / `neutral` / `camera` |
| body_pose / expression | `seated` / `neutral_relaxed` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_01` / `nico_hair_01` |
| location（層級）| `local_cafe`（B）|
| hands | L `free`（放在桌面上，在裁切外）／ R `free`（放在桌面上，在裁切外）|
| props | `window_mist` 窗玻璃上凝結的水氣（background・zone=background）；`bar_dripper` 身後吧台上的手沖濾杯架（background・zone=background） |
| light | `L2_single_window_daylight`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`centered`・motion=`none`・wb=`neutral`・clutter=`clean`・highlight=`none` |

```text
[[S19]]
The bottom edge of the picture sits just below her collarbones. Her face fills most of the frame, from the top of her hair down to the base of her neck. Her shoulders are only barely in the picture and none of her torso, arms or hands is in it.

She is sitting at the window seat of a cafe, not doing anything in particular, just facing the camera.

[[S14]]
Her head is straight on to the camera.
Her chin is level.
She looks directly into the lens.
Her expression is relaxed and neutral, mouth closed and soft.
Her whole face is unobstructed.
[[S17]]

Her left hand is resting on the table, outside the crop.
Her right hand is resting on the table, outside the crop.
Also in the picture: condensation misting the window glass, visible behind her; a pour-over dripper stand on the bar counter behind her, visible behind her.

[[S4]]
[[S1]] It is worn down, with one side tucked behind her ear and the ends curving inward.
[[S2]]

Setting: a small neighbourhood cafe, wooden tables and a bar counter behind her.
Light: daylight comes through the cafe's large window from her front-left, about 45 degrees off and a little above eye level; the white wall and pale floor bounce it back evenly into the shadow side of her face, so there is no strong shadow on her. Exposure: the exposure is set for her face, so the view through the window blows out to white and the far end of the room falls into soft shadow.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits centred in the frame. The background behind her is uncluttered.
[[S3]]
```

### 2. `nico_a02` — identity_core／anchor

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **同一個位子，身體轉向左邊，臉轉回鏡頭，手上端著咖啡杯** |
| framing / view | `chest_up` / `third_person` |
| head_yaw / pitch / gaze | `left_30` / `neutral` / `camera` |
| body_pose / expression | `seated` / `soft_smile` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_01` / `nico_hair_01` |
| location（層級）| `local_cafe`（B）|
| hands | L `free`（放在桌面上）／ R `holding`→`cup_a02`（端在胸前）|
| props | `cup_a02` 白瓷咖啡杯（held_right・zone=chest）；`menu_board` 身後牆上的木質菜單板（background・zone=background） |
| light | `L2_single_window_daylight`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`off_center`・motion=`none`・wb=`neutral`・clutter=`clean`・highlight=`none` |

```text
[[S19]]
[[S9]]

Still at the same seat, her torso angled toward her own left while her face comes back to the camera, a coffee cup held up near her chest.

[[S5]]
[[S12]]
Her chin is level.
She looks directly into the lens.
A small closed-mouth smile, the corners barely lifted.
Her whole face is unobstructed.
[[S17]]

Her left hand is resting on the table.
Her right hand holds a white porcelain coffee cup (held up at chest height).
Also in the picture: a wooden menu board on the wall behind her, visible behind her.

[[S4]]
[[S1]] It is worn down, with one side tucked behind her ear and the ends curving inward.
[[S2]]

Setting: a small neighbourhood cafe, wooden tables and a bar counter behind her.
Light: daylight comes through the cafe's large window from her front-left, about 45 degrees off and a little above eye level; the white wall and pale floor bounce it back evenly into the shadow side of her face, so there is no strong shadow on her. Exposure: the exposure is set for her face, so the view through the window blows out to white and the far end of the room falls into soft shadow.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits off to one side of the frame rather than centred. The background behind her is uncluttered.
[[S3]]
```

### 3. `nico_a03` — identity_core／anchor

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **白天的人行道上站著，身體轉向右邊，臉轉回鏡頭，手上端著外帶杯** |
| framing / view | `chest_up` / `third_person` |
| head_yaw / pitch / gaze | `right_30` / `neutral` / `camera` |
| body_pose / expression | `standing` / `neutral_relaxed` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_01` / `nico_hair_02` |
| location（層級）| `city_street`（B）|
| hands | L `free`（自然垂在身側）／ R `holding`→`togo_a03`（端在胸前）|
| props | `togo_a03` 外帶咖啡杯（held_right・zone=chest）；`scooter_mirror` 身後路邊停放的機車後照鏡（background・zone=background） |
| light | `L6_soft_overcast`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`centered`・motion=`none`・wb=`neutral`・clutter=`clean`・highlight=`none` |

```text
[[S19]]
[[S9]]

She is standing on a pavement in daylight, her torso angled toward her own right while her face comes back to the camera, a takeaway cup held up near her chest.

[[S5]]
[[S13]]
Her chin is level.
She looks directly into the lens.
Her expression is relaxed and neutral, mouth closed and soft.
Her whole face is unobstructed.
[[S17]]

Her left hand is hanging naturally at her side.
Her right hand holds a takeaway coffee cup (held up at chest height).
Also in the picture: the wing mirror of a scooter parked at the kerb behind her, visible behind her.

[[S4]]
[[S1]] All of it is tucked back behind both ears, so both ears and the nape of her neck are exposed.
[[S2]]

Setting: an ordinary back lane in the Da'an district of Taipei, scooters parked along the wall.
Light: a thin overcast sky, the daylight diffuse and coming from everywhere at once, with no hard shadow anywhere; the pale pavement bounces it back evenly into the shadow on the right side of her face. Exposure: the exposure is set for her face, so the sky goes slightly blank and her face keeps full detail.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits centred in the frame. The background behind her is uncluttered.
[[S3]]
```

### 4. `nico_a04` — identity_core／anchor

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **同一段人行道，身體較大幅度轉向左側，手上端著外帶杯** |
| framing / view | `chest_up` / `third_person` |
| head_yaw / pitch / gaze | `left_60` / `neutral` / `away` |
| body_pose / expression | `standing` / `listening_attentive` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_03` / `nico_hair_01` |
| location（層級）| `city_street`（B）|
| hands | L `free`（自然垂在身側）／ R `holding`→`togo_a04`（端在胸前）|
| props | `togo_a04` 外帶咖啡杯（held_right・zone=chest）；`rent_flyer` 騎樓柱子上的租屋紅單（background・zone=background） |
| light | `L6_soft_overcast`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`off_center`・motion=`none`・wb=`slightly_warm_auto`・clutter=`moderate`・highlight=`allowed` |

```text
[[S19]]
[[S9]]

The same stretch of pavement, her torso turned further toward her own left, a takeaway cup held up near her chest.

[[S5]]
Her head is turned well toward her own left, so the camera mostly sees the right side of her face; the far eye is still visible but the far cheek is mostly hidden.
Her chin is level.
[[S16]]
She is listening to someone, attentive, mouth closed.
Her whole face is unobstructed.
[[S17]]

Her left hand is hanging naturally at her side.
Her right hand holds a takeaway coffee cup (held up at chest height).
Also in the picture: a red rental flyer pasted on an arcade pillar, visible behind her.

[[S4]]
[[S1]] It is worn down, with one side tucked behind her ear and the ends curving inward.
[[S7]]

Setting: an ordinary back lane in the Da'an district of Taipei, scooters parked along the wall.
Light: a thin overcast sky, the daylight diffuse and coming from everywhere at once, with no hard shadow anywhere; the pale pavement bounces it back evenly into the shadow on the left side of her face. Exposure: the exposure is set for her face, so the sky goes slightly blank and her face keeps full detail.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits off to one side of the frame rather than centred. The phone's auto white balance has gone a touch warm. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[S3]]
```

### 5. `nico_a05` — identity_core／anchor

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **公園長椅上坐著，身體較大幅度轉向右側，手上拿著保溫瓶** |
| framing / view | `chest_up` / `third_person` |
| head_yaw / pitch / gaze | `right_60` / `neutral` / `away` |
| body_pose / expression | `seated` / `mid_conversation` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_03` / `nico_hair_02` |
| location（層級）| `park`（B）|
| hands | L `supporting`（撐在長椅椅面上）／ R `holding`→`bottle_a05`（拿在胸前）|
| props | `bottle_a05` 保溫瓶（held_right・zone=chest）；`park_lamp` 身後的公園路燈桿（background・zone=background） |
| light | `L6_soft_overcast`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`centered`・motion=`none`・wb=`slightly_warm_auto`・clutter=`moderate`・highlight=`allowed` |

```text
[[S19]]
[[S9]]

She is sitting on a park bench, her torso turned further toward her own right, a vacuum flask held up near her chest.

[[S5]]
Her head is turned well toward her own right, so the camera mostly sees the left side of her face; the far eye is still visible but the far cheek is mostly hidden.
Her chin is level.
[[S16]]
Her mouth is slightly open mid-sentence, caught talking.
Her whole face is unobstructed.
[[S17]]

Her left hand is braced on the seat of the bench.
Her right hand holds a vacuum flask (held up at chest height).
Also in the picture: a park lamp post behind her, visible behind her.

[[S4]]
[[S1]] All of it is tucked back behind both ears, so both ears and the nape of her neck are exposed.
[[S7]]

[[S15]]
Light: a thin overcast sky, the daylight diffuse and coming from everywhere at once, with no hard shadow anywhere; the pale pavement bounces it back evenly into the shadow on the right side of her face. Exposure: the exposure is set for her face, so the sky goes slightly blank and her face keeps full detail.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits centred in the frame. The phone's auto white balance has gone a touch warm. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[S3]]
```

### 6. `nico_a06` — body_pose_coverage／anchor

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **公園步道上站著，正對鏡頭，雙手自然垂下** |
| framing / view | `full_body` / `third_person` |
| head_yaw / pitch / gaze | `front` / `neutral` / `camera` |
| body_pose / expression | `standing` / `neutral_relaxed` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_03` / `nico_hair_01` |
| location（層級）| `park`（B）|
| hands | L `free`（自然垂在身側）／ R `free`（自然垂在身側）|
| props | `bottle_a06` 腳邊步道上放著的保溫瓶（surface・zone=floor）；`yellow_post` 步道旁的黃色分隔柱（background・zone=background） |
| light | `L6_soft_overcast`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`centered`・motion=`none`・wb=`neutral`・clutter=`moderate`・highlight=`allowed` |

```text
[[S19]]
[[S8]]

She is standing on a park path facing the camera, both arms hanging naturally at her sides.

The camera sees the front of her body: her navel and the front of both shoulders point toward the lens, and both of her collarbones are visible.
Her head is straight on to the camera.
Her chin is level.
She looks directly into the lens.
Her expression is relaxed and neutral, mouth closed and soft.
Her whole face is unobstructed.
[[S17]]

Her left hand is hanging naturally at her side.
Her right hand is hanging naturally at her side.
Also in the picture: a vacuum flask standing on the path by her feet; a yellow bollard beside the path, visible behind her.

[[S4]]
[[S1]] It is worn down, with one side tucked behind her ear and the ends curving inward.
[[S7]]

[[S15]]
Light: a thin overcast sky, the daylight diffuse and coming from everywhere at once, with no hard shadow anywhere; the pale paving bounces it back evenly over the whole of her, so her legs and torso read clearly. Exposure: the whole of her sits on one exposure, the sky goes slightly blank, and her proportions are fully readable.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits centred in the frame. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[S3]]
```

### 7. `nico_a07` — body_pose_coverage／anchor

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **同一條步道，身體轉向右側四分之三，臉轉回鏡頭** |
| framing / view | `full_body` / `third_person` |
| head_yaw / pitch / gaze | `right_30` / `neutral` / `camera` |
| body_pose / expression | `standing` / `soft_smile` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_01` / `nico_hair_04` |
| location（層級）| `park`（B）|
| hands | L `free`（自然垂在身側）／ R `holding`→`bottle_a07`（垂在身側提著）|
| props | `bottle_a07` 保溫瓶（held_right・zone=hip）；`trash_bin` 步道邊的鐵製垃圾桶（background・zone=background） |
| light | `L6_soft_overcast`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`off_center`・motion=`none`・wb=`neutral`・clutter=`moderate`・highlight=`allowed` |

```text
[[S19]]
[[S8]]

The same path, her torso turned three-quarters toward her own right while her face comes back to the camera.

[[S5]]
[[S13]]
Her chin is level.
She looks directly into the lens.
A small closed-mouth smile, the corners barely lifted.
Her whole face is unobstructed.
[[S17]]

Her left hand is hanging naturally at her side.
Her right hand holds a vacuum flask (carried down at her side).
Also in the picture: a metal litter bin at the edge of the path, visible behind her.

[[S4]]
[[S1]] It is parted down the middle and blow-dried smooth, the ends tucked slightly under — tidier than she usually wears it.
[[S2]]

[[S15]]
Light: a thin overcast sky, the daylight diffuse; the pale paving fills evenly, so her side outline and leg-to-torso proportion read clearly. Exposure: the whole of her sits on one exposure and the sky goes slightly blank.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits off to one side of the frame rather than centred. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[S3]]
```

### 8. `nico_c01` — identity_core／私下 / 收工後

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **收工後鐵門拉下，坐在工作椅上轉過來看側窗外** |
| framing / view | `face_closeup` / `third_person` |
| head_yaw / pitch / gaze | `front` / `neutral` / `away` |
| body_pose / expression | `seated` / `neutral_composed` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_08` / `nico_hair_01` |
| location（層級）| `workplace_own_studio`（B）|
| hands | L `free`（搭在椅背上，在裁切外）／ R `free`（放在大腿上，在裁切外）|
| props | `window_plant` 窗台上的一盆小綠植（background・zone=background）；`hours_sign` 牆上掛的營業時間牌（background・zone=background） |
| light | `L2_single_window_daylight`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`off_center`・motion=`none`・wb=`neutral`・clutter=`moderate`・highlight=`allowed` |

```text
[[S19]]
The bottom edge of the picture sits just below her collarbones. Her face fills most of the frame, from the top of her hair down to the base of her neck. Her shoulders are only barely in the picture and none of her torso, arms or hands is in it.

After closing up, with the roller shutter down, she has swivelled round on her work chair to look out of the side window.

[[S14]]
Her head is straight on to the camera.
Her chin is level.
[[S16]]
Her expression is composed and neutral, mouth closed.
Her whole face is unobstructed.
[[S17]]

Her left hand is draped over the chair back, outside the crop.
Her right hand is resting on her thigh, outside the crop.
Also in the picture: a small potted plant on the window ledge, visible behind her; an opening-hours sign hanging on the wall, visible behind her.

[[S4]]
[[S1]] It is worn down, with one side tucked behind her ear and the ends curving inward.
She is wearing: A close-fitting grey cotton long-sleeve top with a modest scoop neckline, the hem long and tucked in. Black close-fitting cotton trousers. Indoor slippers.

Setting: her own small nail studio in Taipei — a white manicure desk, a task lamp clamped to its edge, shelves of gel colour bottles on the wall.
Light: afternoon daylight comes in from her front-left through the high side window the shutter does not cover, a little above eye level; the white manicure desk and white wall bounce it back into the shadow side of her face. Exposure: the exposure is set for her face, so the window blows out to white and the far end of the room falls into shadow.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits off to one side of the frame rather than centred. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[S3]]
```

### 9. `nico_c02` — identity_core／工作室 / 進貨

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **蹲在地上拆剛到的材料紙箱，抬頭看向門口** |
| framing / view | `knee_up` / `third_person` |
| head_yaw / pitch / gaze | `left_30` / `up_10` / `away` |
| body_pose / expression | `crouching` / `mildly_surprised` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_06` / `nico_hair_04` |
| location（層級）| `workplace_own_studio`（B）|
| hands | L `supporting`（扶著紙箱邊緣）／ R `holding`→`box_cutter`（拿著美工刀）|
| props | `box_cutter` 美工刀（held_right・zone=knee）；`open_box` 地上拆開一半的紙箱（surface・zone=knee） |
| light | `L2_single_window_daylight`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`slightly_tilted`・motion=`minor_hand_blur`・wb=`slightly_cool_auto`・clutter=`heavy`・highlight=`none` |

```text
[[S19]]
[[S11]]

She is crouched on the floor opening a carton of supplies that has just arrived, head lifted toward the doorway.

[[S5]]
[[S12]]
[[S20]]
[[S16]]
Her eyebrows are lifted a little, mildly caught off guard.
Her whole face is unobstructed.
[[S17]]

Her left hand is braced steadying the edge of the carton.
Her right hand holds the box cutter (holding the box cutter).
Also in the picture: a half-opened carton on the floor.

[[S4]]
[[S1]] It is parted down the middle and blow-dried smooth, the ends tucked slightly under — tidier than she usually wears it.
She is wearing: An oatmeal tailored blazer over a white silk camisole with a square neckline. Matching oatmeal straight wide-leg trousers. Pointed flat shoes. A structured leather handbag. A thin silver bangle.

Setting: her own small nail studio in Taipei — a white manicure desk, a task lamp clamped to its edge, shelves of gel colour bottles on the wall.
Light: daylight from the floor-to-ceiling window comes in from behind her right shoulder; white packing paper scattered on the floor bounces it back up under her jaw. Exposure: the exposure is set for her face, so the area by the window blows out and the shadow inside the carton goes black.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. The horizon is very slightly tilted, the way a hand-held snapshot is. Her moving hand is very slightly blurred, though her face stays sharp. The phone's auto white balance has gone a touch cool. The background is busy with the ordinary mess of the place.
[[S3]]
```

### 10. `nico_c03` — identity_core／私下 / 廚房

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **早餐店的板凳上等餐，手肘擱在桌沿** |
| framing / view | `waist_up` / `third_person` |
| head_yaw / pitch / gaze | `right_30` / `down_15` / `down` |
| body_pose / expression | `seated` / `tired_soft` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_03` / `nico_hair_04` |
| location（層級）| `breakfast_shop`（C）|
| hands | L `free`（手肘擱在桌沿，手掌鬆開）／ R `free`（放在膝上）|
| props | `soy_milk` 塑膠杯裝的豆漿（surface・zone=waist）；`number_tag` 桌上的號碼牌（surface・zone=waist） |
| light | `L2_single_window_daylight`・bounce=`specular` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`centered`・motion=`none`・wb=`neutral`・clutter=`moderate`・highlight=`allowed` |

```text
[[S19]]
[[S10]]

She is waiting for her order on a stool in a breakfast shop, one elbow resting on the edge of the table.

[[S14]]
[[S13]]
[[S18]]
Her eyes are lowered toward what is in front of her.
She looks tired: eyelids a little heavy, face soft and unguarded.
Her whole face is unobstructed.
[[S17]]

Her left hand is open, the elbow resting on the table edge.
Her right hand is resting on her knee.
Also in the picture: soy milk in a plastic cup; a numbered order tag on the table.

[[S4]]
[[S1]] It is parted down the middle and blow-dried smooth, the ends tucked slightly under — tidier than she usually wears it.
[[S7]]

Setting: a Taiwanese breakfast shop, stainless-steel tables and plastic stools, the shutter door open to the street.
Light: morning light comes through the shop's open doorway from her front-left; the stainless-steel table throws a hard glint of it back up under her jaw. At the same time, the shop's cool white ceiling fluorescents fall on the top of her head and her shoulders. Exposure: the exposure is set for her face, so the whole doorway blows out and the back of the shop goes black. The door frame cuts into the right edge of the picture.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits centred in the frame. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[S3]]
```

### 11. `nico_c04` — identity_core／私下 / 剛醒

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **剛洗完澡坐在床邊，舉起手機直視鏡頭** |
| framing / view | `waist_up` / `selfie_front` |
| head_yaw / pitch / gaze | `front` / `down_15` / `camera` |
| body_pose / expression | `seated` / `post_shower_calm` |
| face_visibility | `partial_hair` |
| outfit / hair | `nico_outfit_08` / `nico_hair_06` |
| location（層級）| `own_bedroom`（B）|
| hands | L `camera`（舉著手機（拍攝裝置））／ R `free`（撐在床沿）|
| props | `quilt` 身旁沒疊好的薄被（surface・zone=waist）；`water_glass` 床頭櫃上的玻璃水杯（surface・zone=waist） |
| light | `L2_single_window_daylight`・bounce=`diffuse` |
| filter / camera | `none` / `phone_front`・distortion=`mild`・dof=`adequate` |
| imperfection | composition=`off_center`・motion=`none`・wb=`slightly_warm_auto`・clutter=`moderate`・highlight=`allowed` |

```text
[[S19]]
[[S10]]

Freshly out of the shower, she is sitting on the edge of her bed with the phone raised, looking straight into it.

[[S14]]
Her head is straight on to the camera.
[[S18]]
She looks directly into the lens.
Calm and freshly washed, her face relaxed and a little damp.
A few strands of hair fall across one side of her face.
She is holding the phone herself, arm extended, shooting with the front camera. The phone is the camera and is not itself in the picture.

Her left hand holds the phone that is taking this picture (raised, holding the phone).
Her right hand is braced on the edge of the bed.
Also in the picture: an unfolded thin quilt beside her; a glass of water on the bedside table.

[[S4]]
[[S1]] It is wet from the shower, lying flat against her head, the ends still dripping.
She is wearing: A close-fitting grey cotton long-sleeve top with a modest scoop neckline, the hem long and tucked in. Black close-fitting cotton trousers. Indoor slippers.

Setting: her own bedroom, the bed unmade behind her.
Light: the curtain is not quite drawn, and one slant of morning light falls across the bed; the white sheet is a large reflector, bouncing it back into the lower half of her face. Exposure: the exposure is set for her face, so the slit of light at the curtain blows out to a white band and the rest of the room goes dark.

Shot on the front camera of a phone, held at arm's length. The slight wide-angle stretch a phone lens gives at close range. Adequate depth of field — her face, her body and the background are all in reasonable focus. This is not a shallow blurred-background portrait; her body outline stays sharp and readable.
Straight out of the phone, no filter and no beauty retouching. She sits off to one side of the frame rather than centred. The phone's auto white balance has gone a touch warm. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[S3]]
```

### 12. `nico_c05` — body_pose_coverage／外出 / 出門前

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **玄關靠著牆，低頭把鑰匙收進口袋** |
| framing / view | `knee_up` / `third_person` |
| head_yaw / pitch / gaze | `left_60` / `down_15` / `down` |
| body_pose / expression | `leaning` / `focused` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_04` / `nico_hair_05` |
| location（層級）| `own_entryway`（B）|
| hands | L `supporting`（撐在牆上）／ R `holding`→`keys`（拿著鑰匙）|
| props | `keys` 鑰匙（held_right・zone=waist）；`succulent` 鞋櫃上的一盆多肉（surface・zone=waist） |
| light | `L3_mixed_warm_cool_practical`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`slightly_tilted`・motion=`none`・wb=`neutral`・clutter=`clean`・highlight=`allowed` |

```text
[[S19]]
[[S11]]

She is leaning against the wall in her entryway, head down, putting her keys away in her pocket.

[[S5]]
Her head is turned well toward her own left, so the camera mostly sees the right side of her face; the far eye is still visible but the far cheek is mostly hidden.
[[S18]]
Her eyes are lowered toward what is in front of her.
She is concentrating on what her hands are doing; her mouth is closed and her brow is still.
Her whole face is unobstructed.
[[S17]]

Her left hand is braced flat against the wall.
Her right hand holds her keys (holding her keys).
Also in the picture: a small succulent on the shoe cabinet.

[[S4]]
[[S1]] The ends are flicked outward with a curling iron, and a thin silver hair clip holds the hair back on her right side.
She is wearing: A loose white button-down shirt with a collar and the top two buttons undone. A black pleated mini skirt with grey knee-high socks. Black Mary Jane shoes. A navy shoulder satchel. A thin silver chain bracelet.

Setting: the entryway of her flat, a shoe cabinet against the wall and the front door beside her.
Light: a single warm-yellow recessed light in the entryway ceiling, directly overhead; the white entryway wall bounces that warm light back onto the side of her face. At the same time, cool white stairwell fluorescent light comes through the gap at the door and lands along her shoulder line. Exposure: the exposure is set for her face, so the cool strip at the door gap blows out and the space under the shoe cabinet goes black. The door frame cuts into the left edge of the picture.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. The horizon is very slightly tilted, the way a hand-held snapshot is. The background behind her is uncluttered. A few highlights are allowed to blow out to white.
[[S3]]
```

### 13. `nico_c06` — body_pose_coverage／外出 / 台北的日常

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **大安區巷子裡走路，剛越過一台停在牆邊的機車** |
| framing / view | `full_body` / `third_person` |
| head_yaw / pitch / gaze | `right_60` / `neutral` / `away` |
| body_pose / expression | `walking_frozen` / `neutral_walking` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_03` / `nico_hair_05` |
| location（層級）| `city_street`（B）|
| hands | L `free`（自然擺動）／ R `holding`→`drink_c06`（提在身側）|
| props | `drink_c06` 手搖杯（held_right・zone=hip）；`meter_box` 巷口的電表箱（background・zone=background） |
| light | `L6_soft_overcast`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`off_center`・motion=`subject_motion`・wb=`slightly_cool_auto`・clutter=`heavy`・highlight=`allowed` |

```text
[[S19]]
[[S8]]

She is walking down a back lane in Da'an, caught a step past a scooter parked against the wall.

[[S5]]
Her head is turned well toward her own right, so the camera mostly sees the left side of her face; the far eye is still visible but the far cheek is mostly hidden.
Her chin is level.
[[S16]]
A neutral everyday face, caught mid-walk.
Her whole face is unobstructed.
[[S17]]

Her left hand is swinging naturally as she walks.
Her right hand holds a bubble-tea cup (carried down at her side).
Also in the picture: an electricity meter box at the mouth of the lane, visible behind her.

[[S4]]
[[S1]] The ends are flicked outward with a curling iron, and a thin silver hair clip holds the hair back on her right side.
[[S7]]

Setting: an ordinary back lane in the Da'an district of Taipei, scooters parked along the wall.
Light: flat overcast skylight with no clear direction; the pale tiled wall fills it back evenly over the whole of her. Exposure: the whole frame is low contrast, the sky blows out to white, and there is no second colour temperature in this one.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits off to one side of the frame rather than centred. There is a trace of motion blur where she is moving, though her face stays sharp. The phone's auto white balance has gone a touch cool. The background is busy with the ordinary mess of the place. A few highlights are allowed to blow out to white.
[[S3]]
```

### 14. `nico_c07` — identity_core／工作室 / 手部

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **低頭在展示棒上試新的色膠，側臉朝向鏡頭** |
| framing / view | `chest_up` / `third_person` |
| head_yaw / pitch / gaze | `profile_left` / `down_15` / `down` |
| body_pose / expression | `seated` / `focused` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_01` / `nico_hair_03` |
| location（層級）| `workplace_own_studio`（B）|
| hands | L `holding`→`tip_stick`（固定著甲片展示棒）／ R `holding`→`gel_brush`（拿著上膠筆）|
| props | `tip_stick` 甲片展示棒（held_left・zone=chest）；`color_board` 身後牆上的美甲色卡板（background・zone=background）；`gel_brush` 上膠筆（held_right・zone=chest） |
| light | `L3_mixed_warm_cool_practical`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`centered`・motion=`none`・wb=`neutral`・clutter=`clean`・highlight=`allowed` |

```text
[[S19]]
[[S9]]

Head down at her desk, she is testing a new gel colour on a display stick, the side of her face toward the camera.

The camera is beside her, level with her shoulder, seeing the side of her body: the near shoulder is toward the lens and the far one directly behind it.
Her head is turned all the way to her own left, so the camera sees her profile: the outline of her forehead, nose, lips and chin reads clearly against the background, and only the near eye is visible.
[[S18]]
Her eyes are lowered toward what is in front of her.
She is concentrating on what her hands are doing; her mouth is closed and her brow is still.
Her whole face is unobstructed.
[[S17]]

Her left hand holds a nail-tip display stick (steadying the display stick).
Her right hand holds the gel applicator brush (holding the gel applicator).
Also in the picture: a gel colour swatch board on the wall behind her, visible behind her.

[[S4]]
[[S1]] The back half is clipped up in a claw clip, with two loose strands left down at the front.
[[S2]]

Setting: her own small nail studio in Taipei — a white manicure desk, a task lamp clamped to its edge, shelves of gel colour bottles on the wall.
Light: an adjustable task lamp points down at close range onto her hands and the desk; the white desktop bounces it back up onto her jaw and neck. At the same time, the cool white ceiling fluorescent falls on the back of her head and her shoulders. Exposure: the exposure is set for her hands, so her face sits slightly dark and the curtain behind her goes black.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits centred in the frame. The background behind her is uncluttered. A few highlights are allowed to blow out to white.
[[S3]]
```

### 15. `nico_c08` — body_pose_coverage／私下 / 浴室

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **浴室鏡前修眉，另一手舉著手機對著鏡子拍** |
| framing / view | `waist_up` / `selfie_mirror` |
| head_yaw / pitch / gaze | `left_30` / `up_10` / `mirror` |
| body_pose / expression | `standing` / `concentrating_slight_frown` |
| face_visibility | `partial_hand` |
| outfit / hair | `nico_outfit_08` / `nico_hair_02` |
| location（層級）| `own_bathroom`（B）|
| hands | L `camera`（舉著手機對鏡子（拍攝裝置））／ R `holding`→`brow_razor`（拿著修眉刀靠近眉尾）|
| props | `brow_razor` 修眉刀（held_right・zone=head）；`cleanser` 台面上倒著的洗面乳（surface・zone=waist） |
| light | `L8_bathroom_fluorescent`・bounce=`diffuse` |
| filter / camera | `none` / `mirror_phone`・distortion=`mild`・dof=`adequate` |
| imperfection | composition=`slightly_tilted`・motion=`none`・wb=`slightly_cool_auto`・clutter=`moderate`・highlight=`allowed` |

```text
[[S19]]
[[S10]]

At the bathroom mirror she is tidying an eyebrow, her other hand holding the phone up at the mirror.

The camera sees the front of her body: her navel and the front of both shoulders point toward the lens, and both of her collarbones are visible.
[[S12]]
[[S20]]
She looks at her own reflection in the mirror.
She is concentrating hard enough that her brows draw very slightly together.
The hand she is working with crosses in front of part of her face.
She is photographing her own reflection in the mirror. The phone she is holding is visible in the reflection.

Her left hand holds the phone that is taking this picture (raised, holding the phone up at the mirror).
Her right hand holds the brow razor (holding the brow razor up near the tail of her eyebrow).
Also in the picture: a tube of face wash lying on its side on the counter.

[[S4]]
[[S1]] All of it is tucked back behind both ears, so both ears and the nape of her neck are exposed.
She is wearing: A close-fitting grey cotton long-sleeve top with a modest scoop neckline, the hem long and tucked in. Black close-fitting cotton trousers. Indoor slippers.

Setting: her own small bathroom, white tiled walls and a basin.
Light: a full strip of cool white tube light above the bathroom mirror points straight at her; the white tiled walls bounce it back from every side, leaving almost no shadow. Exposure: the exposure is set for her face, the tube itself blows out to a white bar, and the light in this one is flat and unflattering.

Shot on the rear camera of a phone aimed at a mirror. The slight wide-angle stretch a phone lens gives at close range. Adequate depth of field — her face, her body and the background are all in reasonable focus. This is not a shallow blurred-background portrait; her body outline stays sharp and readable.
Straight out of the phone, no filter and no beauty retouching. The horizon is very slightly tilted, the way a hand-held snapshot is. The phone's auto white balance has gone a touch cool. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
Real skin texture with visible pores and fine flyaway hairs. She is the only person in the picture — no other people and no one else's hands. The only phone in the picture is the one she is holding up at the mirror. No photography equipment of any kind: no softbox, no reflector, no foam board, no light stand, no tripod, no backdrop.
```

### 16. `nico_c09` — body_pose_coverage／私下 / 房間

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **便利商店的雜誌架前蹲下來看最下層，回頭** |
| framing / view | `knee_up` / `third_person` |
| head_yaw / pitch / gaze | `left_30` / `up_10` / `camera` |
| body_pose / expression | `crouching` / `mildly_annoyed` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_05` / `nico_hair_02` |
| location（層級）| `convenience_store`（C）|
| hands | L `supporting`（扶著雜誌架下層）／ R `holding`→`onigiri`（拿著飯糰）|
| props | `basket_c09` 放在腳邊的購物籃（surface・zone=knee）；`onigiri` 飯糰（held_right・zone=chest） |
| light | `L1_single_ugly_overhead`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`off_center`・motion=`minor_hand_blur`・wb=`neutral`・clutter=`heavy`・highlight=`none` |

```text
[[S19]]
[[S11]]

She has crouched down at the magazine rack in a convenience store to see the bottom shelf, and has looked back over her shoulder.

[[S5]]
[[S12]]
[[S20]]
She looks directly into the lens.
A faint flicker of irritation, mouth set.
Her whole face is unobstructed.
[[S17]]

Her left hand is braced on the lower shelf of the magazine rack.
Her right hand holds a rice ball (holding the rice ball).
Also in the picture: a shopping basket set down by her feet.

[[S4]]
[[S1]] All of it is tucked back behind both ears, so both ears and the nape of her neck are exposed.
She is wearing: A black cropped hoodie with a plain crew neckline. Grey wide-leg cargo trousers. Chunky-soled sneakers. A small black crossbody pouch. A silver ear cuff.

Setting: the inside of a Taiwanese convenience store, magazine racks and shelves of goods.
Light: cool white fluorescent ceiling light in the convenience store, straight down from overhead; magazine covers and the white shelving bounce it back up under her chin. Exposure: the exposure is set for her face, the tubes blow out, and the bottom shelf goes black.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits off to one side of the frame rather than centred. Her moving hand is very slightly blurred, though her face stays sharp. The background is busy with the ordinary mess of the place.
[[S3]]
```

### 17. `nico_c10` — environment_stress／外出 / 台北的日常

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **自助洗衣店裡把烘好的衣物從滾筒抱出來，站在機台前** |
| framing / view | `full_body` / `third_person` |
| head_yaw / pitch / gaze | `right_30` / `neutral` / `away` |
| body_pose / expression | `standing` / `neutral_composed` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_09` / `nico_hair_04` |
| location（層級）| `laundromat`（C）|
| hands | L `holding`→`laundry`（與另一手一起抱著）／ R `holding`→`laundry`（與另一手一起抱著）|
| props | `laundry` 抱在懷裡烘好的衣物（held_both・zone=chest）；`coin_tray` 機台上的零錢盤（surface・zone=waist） |
| light | `L1_single_ugly_overhead`・bounce=`specular` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`centered`・motion=`none`・wb=`slightly_cool_auto`・clutter=`heavy`・highlight=`heavy` |

```text
[[S19]]
[[S8]]

In a laundromat she is lifting an armful of dried laundry out of the drum, standing at the machine.

[[S5]]
[[S13]]
Her chin is level.
[[S16]]
Her expression is composed and neutral, mouth closed.
Her whole face is unobstructed.
[[S17]]

Both of her hands together are holding an armful of dried laundry — carrying it against her chest.
Also in the picture: a coin tray on top of the machine.

[[S4]]
[[S1]] It is parted down the middle and blow-dried smooth, the ends tucked slightly under — tidier than she usually wears it.
She is wearing: A dark-grey water-repellent hooded jacket over a black high-neck top. Black straight-leg trousers. Short black rain boots. A waterproof shoulder bag.

Setting: a self-service laundromat, a row of front-loading machines along the wall.
Light: a whole row of cool white fluorescent tubes in the laundromat ceiling; the stainless-steel machine fronts throw it back as hard specular glints rather than soft fill. Exposure: the exposure is set for her face, so the tubes and the steel glints blow right out and the corner of the room goes black.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits centred in the frame. The phone's auto white balance has gone a touch cool. The background is busy with the ordinary mess of the place. The brightest parts of the frame are blown right out to white.
[[S3]]
```

### 18. `nico_c11` — environment_stress／外出 / 台北的日常

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **藥妝店貨架前拿護手霜比較成分** |
| framing / view | `knee_up` / `third_person` |
| head_yaw / pitch / gaze | `front` / `down_15` / `down` |
| body_pose / expression | `standing` / `reading_focused` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_05` / `nico_hair_05` |
| location（層級）| `pharmacy`（C）|
| hands | L `holding`→`hand_creams`（拿著一罐）／ R `holding`→`hand_creams`（拿著另一罐）|
| props | `hand_creams` 兩罐護手霜（held_both・zone=chest）；`basket_c11` 掛在手肘的購物籃（worn・zone=waist） |
| light | `L1_single_ugly_overhead`・bounce=`diffuse` |
| filter / camera | `ccd` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`off_center`・motion=`none`・wb=`color_cast_from_environment`・clutter=`heavy`・highlight=`allowed` |

```text
[[S19]]
[[S11]]

At a drugstore shelf she is comparing the ingredients on two hand creams.

The camera sees the front of her body: her navel and the front of both shoulders point toward the lens, and both of her collarbones are visible.
Her head is straight on to the camera.
[[S18]]
Her eyes are lowered toward what is in front of her.
She is reading something and concentrating on it.
Her whole face is unobstructed.
[[S17]]

Both of her hands together are holding two tubes of hand cream — holding one tube each.
Also in the picture: the shopping basket hooked over her elbow.

[[S4]]
[[S1]] The ends are flicked outward with a curling iron, and a thin silver hair clip holds the hair back on her right side.
She is wearing: A black cropped hoodie with a plain crew neckline. Grey wide-leg cargo trousers. Chunky-soled sneakers. A small black crossbody pouch. A silver ear cuff.

Setting: the aisle of a Taiwanese drugstore, shelves of boxed products.
Light: cool white fluorescent ceiling light in the drugstore, straight down from overhead; the white packaging on the shelves bounces it back onto her chest and chin. Exposure: the exposure is set for her face, the tubes blow out, and the depth of the shelving goes black.

[[S6]]
It has the look of an old CCD compact camera: slightly soft, a little grain, colours very slightly off from true. She sits off to one side of the frame rather than centred. The surroundings throw a visible colour cast across her. The background is busy with the ordinary mess of the place. A few highlights are allowed to blow out to white.
[[S3]]
```

### 19. `nico_c12` — environment_stress／外出 / 台北的日常

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **捷運月台等車，看著對面的到站顯示** |
| framing / view | `waist_up` / `third_person` |
| head_yaw / pitch / gaze | `right_30` / `up_10` / `away` |
| body_pose / expression | `standing` / `blank_waiting` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_06` / `nico_hair_04` |
| location（層級）| `train_platform`（C）|
| hands | L `free`（自然垂在身側）／ R `holding`→`easycard`（拿著悠遊卡）|
| props | `easycard` 悠遊卡（held_right・zone=waist）；`arrival_board` 月台上的到站顯示器（background・zone=background） |
| light | `L3_mixed_warm_cool_practical`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`off_center`・motion=`subject_motion`・wb=`slightly_cool_auto`・clutter=`heavy`・highlight=`allowed` |

```text
[[S19]]
[[S10]]

She is waiting for a train on the MRT platform, watching the arrivals display across the tracks.

[[S5]]
[[S13]]
[[S20]]
[[S16]]
Her face is blank, the way a face goes when someone is simply waiting.
Her whole face is unobstructed.
[[S17]]

Her left hand is hanging naturally at her side.
Her right hand holds her transit card (holding her transit card).
Also in the picture: the arrivals display board on the platform, visible behind her.

[[S4]]
[[S1]] It is parted down the middle and blow-dried smooth, the ends tucked slightly under — tidier than she usually wears it.
She is wearing: An oatmeal tailored blazer over a white silk camisole with a square neckline. Matching oatmeal straight wide-leg trousers. Pointed flat shoes. A structured leather handbag. A thin silver bangle.

Setting: an MRT platform in Taipei, tiled floor and the track edge behind her.
Light: cool white fluorescent light in the platform ceiling; the terrazzo floor bounces a weak amount of it back up. At the same time, the warm white glow of a platform advertising lightbox falls flatly on her shoulder line from behind. Exposure: the exposure is set for her face, so her shoulder line on the lightbox side goes slightly blown and the far end of the platform goes black.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits off to one side of the frame rather than centred. There is a trace of motion blur where she is moving, though her face stays sharp. The phone's auto white balance has gone a touch cool. The background is busy with the ordinary mess of the place. A few highlights are allowed to blow out to white.
[[S3]]
```

### 20. `nico_a08` — identity_core／anchor

| 欄位 | 值 |
|------|----|
| 中文 scene（真理來源）| **公園步道旁站著，整個身體與臉都轉向右側，看著遠處** |
| framing / view | `chest_up` / `third_person` |
| head_yaw / pitch / gaze | `profile_right` / `neutral` / `away` |
| body_pose / expression | `standing` / `calm_distant` |
| face_visibility | `unobstructed` |
| outfit / hair | `nico_outfit_02` / `nico_hair_02` |
| location（層級）| `park`（B）|
| hands | L `free`（自然垂在身側）／ R `free`（自然垂在身側）|
| props | `wood_bench` 身後步道旁的木製長椅（background・zone=background）；`falling_leaf` 肩線後方一片正在飄落的葉子（background・zone=background） |
| light | `L6_soft_overcast`・bounce=`diffuse` |
| filter / camera | `none` / `phone_rear`・distortion=`none`・dof=`adequate` |
| imperfection | composition=`off_center`・motion=`none`・wb=`neutral`・clutter=`moderate`・highlight=`allowed` |

```text
[[S19]]
[[S9]]

She is standing beside the park path with her whole body and her face turned to her own right, looking at something far off.

The camera is beside her, level with her shoulder, seeing the side of her body: the near shoulder is toward the lens and the far one directly behind it.
Her head is turned all the way to her own right, so the camera sees her profile: the outline of her forehead, nose, lips and chin reads clearly against the background, and only the near eye is visible.
Her chin is level.
[[S16]]
Calm and a little distant, thinking about something else.
Her whole face is unobstructed.
[[S17]]

Her left hand is hanging naturally at her side.
Her right hand is hanging naturally at her side.
Also in the picture: a wooden bench beside the path behind her, visible behind her; a single leaf falling behind her shoulder, visible behind her.

[[S4]]
[[S1]] All of it is tucked back behind both ears, so both ears and the nape of her neck are exposed.
She is wearing: A cream cotton camisole with thin straps and a straight horizontal neckline. Grey cotton knee-length shorts. Off-white canvas sneakers. A fine-knit open cardigan. A thin silver necklace.

[[S15]]
Light: a thin overcast sky, the daylight diffuse and coming from everywhere at once, with no hard shadow anywhere; the pale paving fills it back evenly along the outline of her profile. Exposure: the exposure is set for her profile, the sky goes slightly blank, and the line from her jaw to her neck reads completely.

[[S6]]
Straight out of the phone, no filter and no beauty retouching. She sits off to one side of the frame rather than centred. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[S3]]
```

---

## §6 本輪請你判斷

**1. 有沒有任何一段 prompt 用了 §2 已證實無效的寫法？**
   特別是：構圖或服裝結構用否定句；朝向寫成角度；景別沒有說清楚下緣切在哪裡。
   這是最重要的一題——這 20 段是要花 credit 的。

**2. 每一段 prompt 有沒有忠實編碼它左邊的結構欄位？**
   中文 scene → 英文動作句是否等價（沒有漏掉或加油添醋）？
   手部註記、道具名、光線五段的中英是否對得上？
   `head_yaw`／`pitch`／`gaze`／`expression`／`face_visibility` 有沒有被寫進去？

**3. §3-2 的處置對不對？**
   `outfit_01` 是錨點身上那件，實測會被整件複製。我把兩道露肩開口寫進衣櫃定義，
   讓它變成刻意的款式。替代方案是把 outfit_01 改成明顯不同的衣服（例如換顏色），
   讓錨點的版本不被複用。**你認為哪個對？** 這影響 20 張裡的 5 張。

**4. 有沒有哪一段在真實世界不成立、或會產生不可能的畫面？**
   你在 R7 抓到 9 列（微物件在裁切外、雙手不夠用、時間狀態與髮型衝突）——
   那些是在結構欄位上抓的。現在同樣的東西被展開成散文，可能露出新的矛盾。

**5. 我自己看到一個不一致，想聽你的判斷**：`[[S8]]`（11 段在用）在正面描述之後
   還留了一句 `Her back is not toward the camera.`——依 §2-1 這種否定句本來就會被忽略，
   留著理論上無害，但與「不要用否定句」的原則不一致。
   B2 第二次成功的那段 prompt **沒有**這句，只有正面描述。
   該刪掉、還是留著當保險？

**6. 排除清單（每段結尾那段）夠不夠？**
   前幾輪出過：棚燈與泡棉板入鏡、別人的手拿手機入鏡、訓練圖裡出現第二個人的手指。

**7. 放行判定**：可以開始生成這 20 張，還是仍有 P0 必須先修？

**判斷原則**：所有數字與欄位都是程式從 JSON 算出來的。
你若認為某個數字或某段對應不對，直接指出——我會實測驗證。
前九輪你提的每一條我都實跑驗證過，數值主張全部屬實。

---

## §7 你的回覆區

把意見寫在下面這行以下。

<!-- ===== REPLIES BELOW — 本行以下不會被自動產生覆蓋 ===== -->



## ChatGPT 覆核回覆（Phase C prompts）

### C-34｜P0｜20 段都漏掉身材 identity 描述

§3-3 說明 B2 是在修正身材設定後才通過，但 §5 的 20 段 prompt 沒有任何一段寫入 Nico 的胸型、肩腰臀比例、長軀幹或窄長輪廓；只有服裝與 framing。Reference Element 能固定臉，不等於會固定全身，第一次 B2 失敗已經是反證。請把 **B2 第二次實測成功的正面身材字串**設成共用模板，至少寫入所有會讀到胸、腰、臀或全身比例的列；不要再使用 `NOT heavy-chested` 之類否定式。這項未修前不可生成。

### C-35｜P0｜仍大量使用 §2 已證實無效的否定式

第 1 題答案是「有」，而且不是只有 §6-5 指出的那一句：

- face close-up、`[[S9]]`、`[[S10]]`、`[[S11]]` 在正確的下緣句之後，又用 `none ... is in it`／`... are outside the picture` 排除身體區域；這正是 §2-1 已證實無效的構圖否定。
- `[[S5]]` 的 `Her back is not toward the camera` 無效，應刪除。§6-5 把它誤寫成 `[[S8]]`；實際是 `[[S5]]`，出現 11 次。
- `[[S6]]` 的 `No lens distortion`、`This is not a shallow blurred-background portrait` 是相機／構圖否定。
- 多段光線仍寫 `with no hard shadow anywhere`；結尾的 `no filter and no beauty retouching` 也依賴否定。
- `nico_a01` 的 `not doing anything in particular`、`nico_c04` 的 `The phone ... is not itself in the picture` 同樣依賴模型忽略已知不可靠的否定。

修法是保留「畫面下緣切在哪裡」與可見區域的正面描述，刪掉後續排除句；相機改寫成「straight geometry／background remains recognisable and reasonably sharp」；柔光改寫成「only broad, soft-edged tonal transitions」；自拍寫成「the viewpoint is the phone’s front-camera feed, with the device immediately beyond the image boundary」。若 API 有獨立 negative prompt，排除詞應放到該欄，不要混在主 prompt 當作硬控制。

### C-36｜P0｜composition 英文會把站姿／走姿／蹲姿改成 seated

`She sits centred in the frame`／`She sits off to one side...` 的 `sits` 對模型是明確動作，不只是英文慣用語。它與下列結構欄位直接衝突：

- `nico_a03`、`nico_a04`、`nico_a06`、`nico_a07`
- `nico_c06`、`nico_c09`、`nico_c10`、`nico_c11`、`nico_c12`
- `nico_a08`

統一改成 `She is positioned centrally in the frame`／`Her figure is positioned off-centre`。不要讓 composition 模板使用任何姿態動詞。

### C-37｜P0｜builder 沒有依 framing 過濾裁切外資訊

景別雖然放在最前面，但後文又要求模型畫出裁切外的手、鞋和包，會與景別競爭：

- 應省略裁切外 hand action：`nico_a01` 雙手、`nico_a02` 左手、`nico_a03` 左手、`nico_a04` 左手、`nico_a05` 左手、`nico_c01` 雙手、`nico_c03` 右手、`nico_c12` 左手、`nico_a08` 雙手。
- face/chest/waist/knee-up 仍逐件描述裁切外的褲、鞋或拖鞋。請讓 outfit renderer 只輸出該 framing 可能看見的層；例如 chest-up 不應再提示鞋，knee-up 不應提示鞋。
- wardrobe 裡的包也沒有落點。最明顯是 `nico_c07`：兩手都拿美甲工具，prompt 卻另要求 beige canvas tote；`nico_a07`、`nico_c12` 也指定雙手狀態卻沒有說包是肩背、放下或在裁切外。這已把 C-32 從未來 schema 問題變成當前 prompt 歧義。Nico 不必等完整新 schema，但本批每列至少要把包的 `worn／set_down／outside_frame` 寫清楚。

原則應是：**只輸出預期可見的內容；不是以「outside the crop」否定其可見性。**

### C-38｜P0｜兩段仍含會誘發背影的高風險朝向語句

- `nico_a07`：`her torso turned three-quarters toward her own right` 仍是角度概念，與 §2-2 的失敗模式相同；而後面的 `[[S5]]` 又只允許輕微斜身，兩句彼此程度不一致。刪除 `three-quarters`，只保留相機看得到的正面肩線、鎖骨、褲頭正面等地標。
- `nico_c09`：`looked back over her shoulder` 是非常強的背向鏡頭提示，卻又接 `[[S5]]` 要求胸前可見。改成「她蹲著面向貨架斜側，頭轉向鏡頭」，並以可見正面地標鎖定身體，不要使用 `over her shoulder`。

`nico_a08` 是刻意的純側身 profile，現有「近肩遮住遠肩」的正面描述足夠，無異議。

### C-39｜P0｜`nico_c09` 的 basket 翻譯破壞結構欄位

結構把 `basket_c09` 定位為 crouching 姿態下的 `zone=knee`，目的是讓 knee-up 看得到；英文卻寫 `set down by her feet`，而同段 framing 又明說 feet 在畫面外。請改成購物籃位於她彎曲膝蓋旁、從畫面下緣進入構圖，避免模型為了畫腳邊籃子自行拉成全身。

`nico_c02` 的紙箱也建議同樣具體化為「紙箱上緣與打開的箱瓣從畫面下緣升到膝線」，不要只寫 `on the floor`。

### C-40｜P1｜`nico_c10` 的動作時點不一致

前句是 `lifting ... out of the drum`，後句卻是雙手已把衣物抱在胸前。兩個都是合理畫面，但不是同一瞬間。改成 `She has just removed the dried laundry and now stands in front of the open drum, holding the bundle against her chest with both hands.`，可避免模型同時生成伸進滾筒與抱胸兩組手臂。

### C-41｜P0｜outfit_01 應改成「明顯不同的衣服」，不建議把露肩開口正式化

§3-2 的處置能讓文字與必然出圖一致，但沒有處理訓練目的：這件帶兩道辨識度很高的開口會出現在 5/20，且集中於 4/8 clean anchors，容易與 identity 綁定。B2 已實測證明「明顯不同的衣服」可以保臉並服從換裝，因此應利用這個已驗證行為，將 outfit_01 改成與錨點明顯不同的顏色與上身結構，而不是只做很細微的改色。修改後重建這 5 段並重查 framing、包與手部。這比接受 Reference Element 的衣服複製更符合 Soul 訓練的去服裝綁定目的。

### C-42｜P0｜現行排除清單不足以防止已發生的污染

第 6 題答案是「不夠」。`[[S3]]` 幾乎全靠 `no other people／No phone／No photography equipment`，但 §2 已說模型不可靠地執行否定，而且這三類正是先前真的生成過的錯誤。建議改為正面封閉集合：

- third-person：畫面主體只有 Nico；每一隻可見的手都連接到 Nico 的手臂；攝影者與拍攝裝置位於畫面邊界之外；場內照明只來自該列列出的建築燈具／窗光。
- front selfie：畫面就是手機前鏡頭的輸出，拍攝裝置在影像邊界外；可見手臂數與 hands 欄一致。
- mirror selfie：鏡中只有 Nico 與她左手持有的一支手機；右手持修眉刀；每隻可見手都能連回她的手臂。

棚燈、泡棉板、第二人的手若 API 支援獨立 negative prompt，可再放入該欄作輔助，但不能把它當唯一 gate。

### C-43｜P2｜覆核檔的標題與模板編號有殘留漂移

不影響 prompt 本文，但會妨礙後續人工稽核：

- `nico_c03` 標題仍寫「廚房」，實際是早餐店。
- `nico_c04` 標題仍寫「剛醒」，實際是洗澡後。
- `nico_c09` 標題仍寫「房間」，實際是便利商店。
- §6-5 指稱 `[[S8]]` 出現 11 次，實際含 `Her back is not...` 的是 `[[S5]]`。

### 對 §6 七題的直接裁決

1. **有。** C-35、C-38 所列文字命中已證實失效／高風險寫法。
2. **不是全部忠實。** 多數 yaw／pitch／gaze／expression／light 對得上；但 C-36 改壞 body pose，C-39 改壞 prop zone，C-40 混合兩個動作時點，且所有列漏掉全域身材 identity（C-34）。
3. **選替代方案：把 outfit_01 換成明顯不同的衣服。** 理由見 C-41。
4. **有。** 主要是裁切外資訊、包的 carry state、`c09` 背影 cue 與腳邊 basket、`c10` 動作時點。
5. **刪掉。** 而且實際是 `[[S5]]`，不是 `[[S8]]`；正面地標才是有效控制。
6. **不夠。** 改為 C-42 的正面封閉集合；獨立 negative prompt 只能當輔助。
7. **目前不放行。** C-34／C-35／C-36／C-37／C-38／C-39／C-41／C-42 修正並重新展開 20 段後，需再做一次 prompt 層覆核；C-40 可同輪修。修完前不要開始生成。
