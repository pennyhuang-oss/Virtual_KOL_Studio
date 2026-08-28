# Nico Pilot — Phase C 20 段 prompt 覆核（生成前最後一關）

## §0 給審閱者

**你只需要讀這一個檔案。** 不要用 GitHub 連接器去抓 repo 裡的其他檔案——
背景、規則、判斷所需的一切都在這份檔案裡。

**回覆方式**：把意見寫在本檔案最下方 §7 回覆區（`REPLIES BELOW` 那行以下），然後 commit。
那一段不會被自動產生覆蓋。

- 目前 commit：`a2f7807`
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

### 3-2 outfit_01：採納你的意見，換成明顯不同的衣服

`nico_outfit_01` 原本就是錨點圖身上那件炭灰高領羅紋針織。依 §2-4，20 張裡有 5 張用這件
（`a01`／`a02`／`a03`／`a07`／`c07`，其中 4 張是 clean anchor），那 5 張一定會帶出
錨點那兩道窄露肩開口。

上一輪我的處置是把開口寫進衣櫃定義，讓文字與必然出圖一致。**你（C-41）指出那沒有處理**
**訓練目的**——高辨識度的開口出現在 4/8 clean anchor，容易與 identity 綁在一起，
正好違反 Soul 訓練「去服裝綁定」的目的；而 B2 已實測證明「明顯不同的衣服」可以保住臉
又服從換裝。**我採納你的意見**，改成顏色、織法、領型三者都與錨點不同的一件：

> a fitted off-white fine-gauge knit long-sleeve top with a plain round crew neckline that lies flat against her collarbones

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

**20 段裡重複出現的樣板**，抽出來只印一次；下面各段以 `[[名稱]]` 代替，
**實際送進模型時是完整文字**。這樣做只是為了控制這份檔案的體積。
（代號改為語意固定的名稱——上一輪用長度排序的流水號，每次重新產生都會變，
你 C-43 指出的 `[[S8]]`/`[[S5]]` 對不上就是這個原因。）

- `[[BODY-1]]`（8 段共用）：Her build: a slim narrow frame with narrow shoulders about as wide as her hips, a long torso, and a full rounded bust that reads clearly against how slight the rest of her is. Visible collarbone, slim, smooth upper arms, a flat lower abdomen, a narrow waist, long straight legs. The contrast between the small waist and the fuller chest is part of her shape. She is 167cm and slight.
- `[[BODY-2]]`（10 段共用）：Her build: a slim narrow frame with narrow shoulders about as wide as her hips, a long torso, and a full rounded bust that reads clearly against how slight the rest of her is. Visible collarbone, slim, smooth upper arms, a narrow waist. The contrast between the small waist and the fuller chest is part of her shape.
- `[[CAMERA-1]]`（18 段共用）：Shot on the rear camera of a phone. Straight lens geometry: vertical lines in the room stay vertical. Deep depth of field: her face, her body and the background all stay in focus together, and her body outline reads sharp against what is behind her.
- `[[CLOSED-SET-1]]`（18 段共用）：Real skin texture with visible pores and fine flyaway hairs. Everything in this picture is accounted for: the only person in it is her, and every visible hand connects to one of her own arms. Whoever is taking the photo, and the phone they are holding, are beyond the edge of the frame. The only light in the room comes from the fixtures and windows named above.
- `[[FACE-BARE-1]]`（20 段共用）：Her face is bare: her lips are the same soft pinkish-beige as the skin around them, matte, with a soft undefined edge; her eyebrows are soft and natural; her lashes are her own and unmade. Light neutral-to-cool skin with natural tonal variation and visible pores.
- `[[FACING-1]]`（9 段共用）：Her body is angled so one hip is nearer the lens, but the camera still sees the front of her chest: both collarbones are visible and the far shoulder is only a little further from the camera than the near one.
- `[[FACING-2]]`（3 段共用）：The camera sees the front of her body: her navel and the front of both shoulders point toward the lens, and both of her collarbones are visible.
- `[[FACING-3]]`（4 段共用）：The camera sees the front of her upper body: her chest and both shoulders face the lens and both collarbones are visible.
- `[[FRAME-1]]`（4 段共用）：The whole of her is inside the picture, from the top of her head down to her shoes, with a margin of empty ground below her feet and a little space above her head. Her legs and shoes are clearly visible.
- `[[FRAME-2]]`（6 段共用）：The bottom edge of the picture cuts across her chest, a little below her armpits. Her head, shoulders and upper chest fill the frame. Her waist, hips, legs and feet are outside the picture.
- `[[FRAME-3]]`（4 段共用）：The bottom edge of the picture cuts across her waist at about the level of her navel. Her head, shoulders, chest and waist fill the frame. Her hips, legs and feet are outside the picture.
- `[[FRAME-4]]`（4 段共用）：The bottom edge of the picture cuts across her legs just below the knees. Her head, torso, hips and thighs are all inside the frame. Her lower legs and feet are outside the picture.
- `[[HAIR-COLOUR-1]]`（5 段共用）：Her hair is a chin-length bob in a cool-toned medium chestnut brown — a muted mushroom brown with a soft grey undertone. One narrow band of silver-grey runs through the hair at her left temple, the way a deliberate salon highlight sits in otherwise evenly dyed hair. Apart from that one band the colour is a single flat dye reaching the scalp: her roots are the same brown as her ends. It is parted down the middle and blow-dried smooth, the ends tucked slightly under — tidier than she usually wears it.
- `[[HAIR-COLOUR-2]]`（3 段共用）：Her hair is a chin-length bob in a cool-toned medium chestnut brown — a muted mushroom brown with a soft grey undertone. One narrow band of silver-grey runs through the hair at her left temple, the way a deliberate salon highlight sits in otherwise evenly dyed hair. Apart from that one band the colour is a single flat dye reaching the scalp: her roots are the same brown as her ends. The ends are flicked outward with a curling iron, and a thin silver hair clip holds the hair back on her right side.
- `[[HAIR-COLOUR-3]]`（5 段共用）：Her hair is a chin-length bob in a cool-toned medium chestnut brown — a muted mushroom brown with a soft grey undertone. One narrow band of silver-grey runs through the hair at her left temple, the way a deliberate salon highlight sits in otherwise evenly dyed hair. Apart from that one band the colour is a single flat dye reaching the scalp: her roots are the same brown as her ends. All of it is tucked back behind both ears, so both ears and the nape of her neck are exposed.
- `[[HAIR-COLOUR-4]]`（5 段共用）：Her hair is a chin-length bob in a cool-toned medium chestnut brown — a muted mushroom brown with a soft grey undertone. One narrow band of silver-grey runs through the hair at her left temple, the way a deliberate salon highlight sits in otherwise evenly dyed hair. Apart from that one band the colour is a single flat dye reaching the scalp: her roots are the same brown as her ends. It is worn down, with one side tucked behind her ear and the ends curving inward.
- `[[HEAD-1]]`（4 段共用）：Her head is turned a little toward her own left, so the camera sees slightly more of the right side of her face; her far cheek and both eyes are still fully visible.
- `[[HEAD-2]]`（5 段共用）：Her head is turned a little toward her own right, so the camera sees slightly more of the left side of her face; her far cheek and both eyes are still fully visible.
- `[[WHO-SHOOTS-1]]`（18 段共用）：Someone standing near her is holding the phone and taking this photo of her.

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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
The bottom edge of the picture sits just below her collarbones. Her face fills most of the frame, from the top of her hair down to the base of her neck. Her shoulders are only barely in the picture; everything below them is outside it.

She is sitting at the window seat of a cafe, simply facing the camera with her hands still and her attention on the lens.

[[FACING-3]]
Her head is straight on to the camera.
Her chin is level.
She looks directly into the lens.
Her expression is relaxed and neutral, mouth closed and soft.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Also in the picture: condensation misting the window glass; a pour-over dripper stand on the bar counter behind her.

[[FACE-BARE-1]]
Her frame is slight: narrow shoulders and a slender neck, with the collarbone visible where it enters the frame.
[[HAIR-COLOUR-4]]
She is wearing a fitted off-white fine-gauge knit long-sleeve top with a plain round crew neckline that lies flat against her collarbones; small silver hoop earrings.

Setting: a small neighbourhood cafe, wooden tables and a bar counter behind her.
Light: daylight comes through the cafe's large window from her front-left, about 45 degrees off and a little above eye level; the white wall and pale floor bounce it back evenly into the shadow side of her face, keeping every shadow on her broad and shallow. Exposure: the exposure is set for her face, so the view through the window blows out to white and the far end of the room falls into soft shadow.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. She is positioned centrally in the frame. The background behind her is uncluttered.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-2]]

Still at the same seat, her torso angled toward her own left while her face comes back to the camera, a coffee cup held up near her chest.

[[FACING-1]]
[[HEAD-1]]
Her chin is level.
She looks directly into the lens.
A small closed-mouth smile, the corners barely lifted.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her right hand holds a white porcelain coffee cup (held up at chest height).
Also in the picture: a wooden menu board on the wall behind her.

[[FACE-BARE-1]]
[[BODY-2]]
[[HAIR-COLOUR-4]]
She is wearing a fitted off-white fine-gauge knit long-sleeve top with a plain round crew neckline that lies flat against her collarbones; small silver hoop earrings.

Setting: a small neighbourhood cafe, wooden tables and a bar counter behind her.
Light: daylight comes through the cafe's large window from her front-left, about 45 degrees off and a little above eye level; the white wall and pale floor bounce it back evenly into the shadow side of her face, keeping every shadow on her broad and shallow. Exposure: the exposure is set for her face, so the view through the window blows out to white and the far end of the room falls into soft shadow.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. Her figure is positioned off-centre in the frame. The background behind her is uncluttered.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-2]]

She is standing on a pavement in daylight, her torso angled toward her own right while her face comes back to the camera, a takeaway cup held up near her chest.

[[FACING-1]]
[[HEAD-2]]
Her chin is level.
She looks directly into the lens.
Her expression is relaxed and neutral, mouth closed and soft.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her right hand holds a takeaway coffee cup (held up at chest height).
Also in the picture: the wing mirror of a scooter parked at the kerb behind her.

[[FACE-BARE-1]]
[[BODY-2]]
[[HAIR-COLOUR-3]]
She is wearing a fitted off-white fine-gauge knit long-sleeve top with a plain round crew neckline that lies flat against her collarbones; small silver hoop earrings.

Setting: an ordinary back lane in the Da'an district of Taipei, scooters parked along the wall.
Light: a thin overcast sky, the daylight arriving evenly from the whole sky at once, so every shadow edge on her is broad and soft; the pale pavement bounces it back evenly into the shadow on the right side of her face. Exposure: the exposure is set for her face, so the sky goes slightly blank and her face keeps full detail.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. She is positioned centrally in the frame. The background behind her is uncluttered.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-2]]

The same stretch of pavement, her torso turned further toward her own left, a takeaway cup held up near her chest.

[[FACING-1]]
Her head is turned well toward her own left, so the camera mostly sees the right side of her face; the far eye is still visible but the far cheek is mostly hidden.
Her chin is level.
Her eyes rest on something in the distance, off past the camera.
She is listening to someone, attentive, mouth closed.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her right hand holds a takeaway coffee cup (held up at chest height).
Also in the picture: a red rental flyer pasted on an arcade pillar.

[[FACE-BARE-1]]
[[BODY-2]]
[[HAIR-COLOUR-4]]
She is wearing a cream cropped knit top with a plain round crew neckline, its hem ending at her natural waist; silver hoop earrings.

Setting: an ordinary back lane in the Da'an district of Taipei, scooters parked along the wall.
Light: a thin overcast sky, the daylight arriving evenly from the whole sky at once, so every shadow edge on her is broad and soft; the pale pavement bounces it back evenly into the shadow on the left side of her face. Exposure: the exposure is set for her face, so the sky goes slightly blank and her face keeps full detail.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. Her figure is positioned off-centre in the frame. The phone's auto white balance has gone a touch warm. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-2]]

She is sitting on a park bench, her torso turned further toward her own right, a vacuum flask held up near her chest.

[[FACING-1]]
Her head is turned well toward her own right, so the camera mostly sees the left side of her face; the far eye is still visible but the far cheek is mostly hidden.
Her chin is level.
Her eyes rest on something in the distance, off past the camera.
Her mouth is slightly open mid-sentence, caught talking.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her right hand holds a vacuum flask (held up at chest height).
Also in the picture: a park lamp post behind her.

[[FACE-BARE-1]]
[[BODY-2]]
[[HAIR-COLOUR-3]]
She is wearing a cream cropped knit top with a plain round crew neckline, its hem ending at her natural waist; silver hoop earrings.

Setting: a paved path through an ordinary neighbourhood park in Taipei, low shrubs and a row of trees.
Light: a thin overcast sky, the daylight arriving evenly from the whole sky at once, so every shadow edge on her is broad and soft; the pale pavement bounces it back evenly into the shadow on the right side of her face. Exposure: the exposure is set for her face, so the sky goes slightly blank and her face keeps full detail.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. She is positioned centrally in the frame. The phone's auto white balance has gone a touch warm. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-1]]

She is standing on a park path facing the camera, both arms hanging naturally at her sides.

[[FACING-2]]
Her head is straight on to the camera.
Her chin is level.
She looks directly into the lens.
Her expression is relaxed and neutral, mouth closed and soft.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her left hand is hanging naturally at her side.
Her right hand is hanging naturally at her side.
Also in the picture: a vacuum flask standing on the path by her feet; a yellow bollard beside the path.

[[FACE-BARE-1]]
[[BODY-1]]
[[HAIR-COLOUR-4]]
She is wearing a cream cropped knit top with a plain round crew neckline, its hem ending at her natural waist; high-waisted light-wash straight-leg jeans; white canvas sneakers; silver hoop earrings; a small dark-brown box bag hangs from her shoulder.

Setting: a paved path through an ordinary neighbourhood park in Taipei, low shrubs and a row of trees.
Light: a thin overcast sky, the daylight arriving evenly from the whole sky at once, so every shadow edge on her is broad and soft; the pale paving bounces it back evenly over the whole of her, so her legs and torso read clearly. Exposure: the whole of her sits on one exposure, the sky goes slightly blank, and her proportions are fully readable.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. She is positioned centrally in the frame. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-1]]

The same path. The camera sees the front of her body from slightly to one side; her face is turned to the lens.

The camera sees the front of her body: the front of her chest and both collarbones are visible, the waistband of her trousers faces the lens, and one hip is a little nearer the camera than the other.
[[HEAD-2]]
Her chin is level.
She looks directly into the lens.
A small closed-mouth smile, the corners barely lifted.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her left hand is hanging naturally at her side.
Her right hand holds a vacuum flask (carried down at her side).
Also in the picture: a metal litter bin at the edge of the path.

[[FACE-BARE-1]]
[[BODY-1]]
[[HAIR-COLOUR-1]]
She is wearing a fitted off-white fine-gauge knit long-sleeve top with a plain round crew neckline that lies flat against her collarbones; black high-waisted straight-leg tailored trousers; black leather loafers; small silver hoop earrings; one thin silver ring; a beige canvas tote hangs from her shoulder.

Setting: a paved path through an ordinary neighbourhood park in Taipei, low shrubs and a row of trees.
Light: a thin overcast sky, the daylight diffuse; the pale paving fills evenly, so her side outline and leg-to-torso proportion read clearly. Exposure: the whole of her sits on one exposure and the sky goes slightly blank.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. Her figure is positioned off-centre in the frame. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
The bottom edge of the picture sits just below her collarbones. Her face fills most of the frame, from the top of her hair down to the base of her neck. Her shoulders are only barely in the picture; everything below them is outside it.

After closing up, with the roller shutter down, she has swivelled round on her work chair to look out of the side window.

[[FACING-3]]
Her head is straight on to the camera.
Her chin is level.
Her eyes rest on something in the distance, off past the camera.
Her expression is composed and neutral, mouth closed.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Also in the picture: a small potted plant on the window ledge; an opening-hours sign hanging on the wall.

[[FACE-BARE-1]]
Her frame is slight: narrow shoulders and a slender neck, with the collarbone visible where it enters the frame.
[[HAIR-COLOUR-4]]
She is wearing a close-fitting grey cotton long-sleeve top with a modest scoop neckline, the hem long and tucked in.

Setting: her own small nail studio in Taipei — a white manicure desk, a task lamp clamped to its edge, shelves of gel colour bottles on the wall.
Light: afternoon daylight comes in from her front-left through the high side window that the shutter leaves clear, a little above eye level; the white manicure desk and white wall bounce it back into the shadow side of her face. Exposure: the exposure is set for her face, so the window blows out to white and the far end of the room falls into shadow.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. Her figure is positioned off-centre in the frame. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-4]]

She is crouched on the floor opening a carton of supplies that has just arrived, head lifted toward the doorway.

[[FACING-1]]
[[HEAD-1]]
Her chin is raised a little, so her face tilts slightly upward.
Her eyes rest on something in the distance, off past the camera.
Her eyebrows are lifted a little, mildly caught off guard.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her left hand is braced steadying the edge of the carton.
Her right hand holds the box cutter (holding the box cutter).
Also in the picture: a half-opened carton whose top edge and folded-back flaps rise from the bottom of the picture to about her knee.

[[FACE-BARE-1]]
[[BODY-1]]
[[HAIR-COLOUR-1]]
She is wearing an oatmeal tailored blazer over a white silk camisole with a square neckline; matching oatmeal straight wide-leg trousers; a thin silver bangle.

Setting: her own small nail studio in Taipei — a white manicure desk, a task lamp clamped to its edge, shelves of gel colour bottles on the wall.
Light: daylight from the floor-to-ceiling window comes in from behind her right shoulder; white packing paper scattered on the floor bounces it back up under her jaw. Exposure: the exposure is set for her face, so the area by the window blows out and the shadow inside the carton goes black.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. The horizon runs very slightly off level, the way a hand-held snapshot does. Her moving hand is very slightly blurred, though her face stays sharp. The phone's auto white balance has gone a touch cool. The background is busy with the ordinary mess of the place.
[[CLOSED-SET-1]]
```

### 10. `nico_c03` — identity_core／私下 / 早餐店

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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-3]]

She is waiting for her order on a stool in a breakfast shop, one elbow resting on the edge of the table.

[[FACING-3]]
[[HEAD-2]]
Her chin is dipped, so her face tilts downward and her eyelids read lower.
Her eyes are lowered toward what is in front of her.
She looks tired: eyelids a little heavy, face soft and unguarded.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her left hand is open, the elbow resting on the table edge.
Also in the picture: soy milk in a plastic cup; a numbered order tag on the table.

[[FACE-BARE-1]]
[[BODY-2]]
[[HAIR-COLOUR-1]]
She is wearing a cream cropped knit top with a plain round crew neckline, its hem ending at her natural waist; high-waisted light-wash straight-leg jeans; silver hoop earrings.

Setting: a Taiwanese breakfast shop, stainless-steel tables and plastic stools, the shutter door open to the street.
Light: morning light comes through the shop's open doorway from her front-left; the stainless-steel table throws a hard glint of it back up under her jaw. At the same time, the shop's cool white ceiling fluorescents fall on the top of her head and her shoulders. Exposure: the exposure is set for her face, so the whole doorway blows out and the back of the shop goes black. The door frame cuts into the right edge of the picture.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. She is positioned centrally in the frame. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
```

### 11. `nico_c04` — identity_core／私下 / 剛洗完澡

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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-3]]

Freshly out of the shower, she is sitting on the edge of her bed with the phone raised, looking straight into it.

[[FACING-3]]
Her head is straight on to the camera.
Her chin is dipped, so her face tilts downward and her eyelids read lower.
She looks directly into the lens.
Calm and freshly washed, her face relaxed and a little damp.
A few strands of hair fall across one side of her face.
The picture is what her phone's own front camera sees: she holds it herself at arm's length, and the device sits just past the edge of the frame.

Her left hand holds the phone that is taking this picture (raised, holding the phone).
Her right hand is braced on the edge of the bed.
Also in the picture: an unfolded thin quilt beside her; a glass of water on the bedside table.

[[FACE-BARE-1]]
[[BODY-2]]
Her hair is a chin-length bob in a cool-toned medium chestnut brown — a muted mushroom brown with a soft grey undertone. One narrow band of silver-grey runs through the hair at her left temple, the way a deliberate salon highlight sits in otherwise evenly dyed hair. Apart from that one band the colour is a single flat dye reaching the scalp: her roots are the same brown as her ends. It is wet from the shower, lying flat against her head, the ends still dripping.
She is wearing a close-fitting grey cotton long-sleeve top with a modest scoop neckline, the hem long and tucked in; black close-fitting cotton trousers.

Setting: her own bedroom, the bed unmade behind her.
Light: the curtain hangs a hand's width open, and one slant of morning light falls across the bed; the white sheet is a large reflector, bouncing it back into the lower half of her face. Exposure: the exposure is set for her face, so the slit of light at the curtain blows out to a white band and the rest of the room goes dark.

Shot on the front camera of a phone, held at arm's length. The slight wide-angle stretch a phone lens gives at close range. Deep depth of field: her face, her body and the background all stay in focus together, and her body outline reads sharp against what is behind her.
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. Her figure is positioned off-centre in the frame. The phone's auto white balance has gone a touch warm. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
Real skin texture with visible pores and fine flyaway hairs. Everything in this picture is accounted for: the image is what her phone's front camera sees, so the phone itself sits just beyond the edge of the frame. The only person in it is her, and every visible hand connects to one of her own arms. The only light comes from the sources named above.
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-4]]

She is leaning against the wall in her entryway, head down, putting her keys away in her pocket.

[[FACING-1]]
Her head is turned well toward her own left, so the camera mostly sees the right side of her face; the far eye is still visible but the far cheek is mostly hidden.
Her chin is dipped, so her face tilts downward and her eyelids read lower.
Her eyes are lowered toward what is in front of her.
She is concentrating on what her hands are doing; her mouth is closed and her brow is still.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her left hand is braced flat against the wall.
Her right hand holds her keys (holding her keys).
Also in the picture: a small succulent on the shoe cabinet.

[[FACE-BARE-1]]
[[BODY-1]]
[[HAIR-COLOUR-2]]
She is wearing a loose white button-down shirt with a collar and the top two buttons open; a black pleated mini skirt with grey knee-high socks; a thin silver chain bracelet; a navy shoulder satchel hangs from her shoulder.

Setting: the entryway of her flat, a shoe cabinet against the wall and the front door beside her.
Light: a single warm-yellow recessed light in the entryway ceiling, directly overhead; the white entryway wall bounces that warm light back onto the side of her face. At the same time, cool white stairwell fluorescent light comes through the gap at the door and lands along her shoulder line. Exposure: the exposure is set for her face, so the cool strip at the door gap blows out and the space under the shoe cabinet goes black. The door frame cuts into the left edge of the picture.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. The horizon runs very slightly off level, the way a hand-held snapshot does. The background behind her is uncluttered. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-1]]

She is walking down a back lane in Da'an, caught a step past a scooter parked against the wall.

[[FACING-1]]
Her head is turned well toward her own right, so the camera mostly sees the left side of her face; the far eye is still visible but the far cheek is mostly hidden.
Her chin is level.
Her eyes rest on something in the distance, off past the camera.
A neutral everyday face, caught mid-walk.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her left hand is swinging naturally as she walks.
Her right hand holds a bubble-tea cup (carried down at her side).
Also in the picture: an electricity meter box at the mouth of the lane.

[[FACE-BARE-1]]
[[BODY-1]]
[[HAIR-COLOUR-2]]
She is wearing a cream cropped knit top with a plain round crew neckline, its hem ending at her natural waist; high-waisted light-wash straight-leg jeans; white canvas sneakers; silver hoop earrings; a small dark-brown box bag is worn across her body.

Setting: an ordinary back lane in the Da'an district of Taipei, scooters parked along the wall.
Light: flat overcast skylight arriving evenly from the whole sky; the pale tiled wall fills it back evenly over the whole of her. Exposure: the whole frame is low contrast, the sky blows out to white, and one single colour temperature covers everything.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. Her figure is positioned off-centre in the frame. There is a trace of motion blur where she is moving, though her face stays sharp. The phone's auto white balance has gone a touch cool. The background is busy with the ordinary mess of the place. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-2]]

Head down at her desk, she is testing a new gel colour on a display stick, the side of her face toward the camera.

The camera is beside her, level with her shoulder, seeing the side of her body: the near shoulder is toward the lens and the far one directly behind it.
Her head is turned all the way to her own left, so the camera sees her profile: the outline of her forehead, nose, lips and chin reads clearly against the background, and only the near eye is visible.
Her chin is dipped, so her face tilts downward and her eyelids read lower.
Her eyes are lowered toward what is in front of her.
She is concentrating on what her hands are doing; her mouth is closed and her brow is still.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her left hand holds a nail-tip display stick (steadying the display stick).
Her right hand holds the gel applicator brush (holding the gel applicator).
Also in the picture: a gel colour swatch board on the wall behind her.

[[FACE-BARE-1]]
[[BODY-2]]
Her hair is a chin-length bob in a cool-toned medium chestnut brown — a muted mushroom brown with a soft grey undertone. One narrow band of silver-grey runs through the hair at her left temple, the way a deliberate salon highlight sits in otherwise evenly dyed hair. Apart from that one band the colour is a single flat dye reaching the scalp: her roots are the same brown as her ends. The back half is clipped up in a claw clip, with two loose strands left down at the front.
She is wearing a fitted off-white fine-gauge knit long-sleeve top with a plain round crew neckline that lies flat against her collarbones; small silver hoop earrings.

Setting: her own small nail studio in Taipei — a white manicure desk, a task lamp clamped to its edge, shelves of gel colour bottles on the wall.
Light: an adjustable task lamp points down at close range onto her hands and the desk; the white desktop bounces it back up onto her jaw and neck. At the same time, the cool white ceiling fluorescent falls on the back of her head and her shoulders. Exposure: the exposure is set for her hands, so her face sits slightly dark and the curtain behind her goes black.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. She is positioned centrally in the frame. The background behind her is uncluttered. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-3]]

At the bathroom mirror she is tidying an eyebrow, her other hand holding the phone up at the mirror.

[[FACING-2]]
[[HEAD-1]]
Her chin is raised a little, so her face tilts slightly upward.
She looks at her own reflection in the mirror.
She is concentrating hard enough that her brows draw very slightly together.
The hand she is working with crosses in front of part of her face.
She is photographing her own reflection in the mirror. The phone she is holding is visible in the reflection.

Her left hand holds the phone that is taking this picture (raised, holding the phone up at the mirror).
Her right hand holds the brow razor (holding the brow razor up near the tail of her eyebrow).
Also in the picture: a tube of face wash lying on its side on the counter.

[[FACE-BARE-1]]
[[BODY-2]]
[[HAIR-COLOUR-3]]
She is wearing a close-fitting grey cotton long-sleeve top with a modest scoop neckline, the hem long and tucked in; black close-fitting cotton trousers.

Setting: her own small bathroom, white tiled walls and a basin.
Light: a full strip of cool white tube light above the bathroom mirror points straight at her; the white tiled walls bounce it back from every side, so what shadow there is stays broad and very shallow. Exposure: the exposure is set for her face, the tube itself blows out to a white bar, and the light in this one is flat and unflattering.

Shot on the rear camera of a phone aimed at a mirror. The slight wide-angle stretch a phone lens gives at close range. Deep depth of field: her face, her body and the background all stay in focus together, and her body outline reads sharp against what is behind her.
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. The horizon runs very slightly off level, the way a hand-held snapshot does. The phone's auto white balance has gone a touch cool. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
Real skin texture with visible pores and fine flyaway hairs. Everything in this picture is accounted for: the mirror holds her and the single phone in her raised hand, and that is the whole of what it holds. Every visible hand connects to one of her own arms. The only light comes from the fixtures named above.
```

### 16. `nico_c09` — body_pose_coverage／外出 / 便利商店

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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-4]]

She has crouched down at the magazine rack in a convenience store to see the bottom shelf. Her body is angled toward the shelving and her head is turned to the camera.

The camera sees the front of her upper body: the front of her chest and both collarbones are visible, and her knees come toward the lens as she crouches.
[[HEAD-1]]
Her chin is raised a little, so her face tilts slightly upward.
She looks directly into the lens.
A faint flicker of irritation, mouth set.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her left hand is braced on the lower shelf of the magazine rack.
Her right hand holds a rice ball (holding the rice ball).
Also in the picture: a shopping basket standing against her bent knee, entering the picture at its bottom edge.

[[FACE-BARE-1]]
[[BODY-1]]
[[HAIR-COLOUR-3]]
She is wearing a black cropped hoodie with a plain crew neckline; grey wide-leg cargo trousers; a silver ear cuff; a small black crossbody pouch is worn across her body.

Setting: the inside of a Taiwanese convenience store, magazine racks and shelves of goods.
Light: cool white fluorescent ceiling light in the convenience store, straight down from overhead; magazine covers and the white shelving bounce it back up under her chin. Exposure: the exposure is set for her face, the tubes blow out, and the bottom shelf goes black.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. Her figure is positioned off-centre in the frame. Her moving hand is very slightly blurred, though her face stays sharp. The background is busy with the ordinary mess of the place.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-1]]

She has just taken the dried laundry out of the drum and now stands in front of the open machine, the bundle held against her chest.

[[FACING-1]]
[[HEAD-2]]
Her chin is level.
Her eyes rest on something in the distance, off past the camera.
Her expression is composed and neutral, mouth closed.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Both of her hands together are holding an armful of dried laundry — carrying it against her chest.
Also in the picture: a coin tray on top of the machine.

[[FACE-BARE-1]]
[[BODY-1]]
[[HAIR-COLOUR-1]]
She is wearing a dark-grey water-repellent hooded jacket over a black high-neck top; black straight-leg trousers; short black rain boots.

Setting: a self-service laundromat, a row of front-loading machines along the wall.
Light: a whole row of cool white fluorescent tubes in the laundromat ceiling; the stainless-steel machine fronts throw it back as hard specular glints rather than soft fill. Exposure: the exposure is set for her face, so the tubes and the steel glints blow right out and the corner of the room goes black.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. She is positioned centrally in the frame. The phone's auto white balance has gone a touch cool. The background is busy with the ordinary mess of the place. The brightest parts of the frame are blown right out to white.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-4]]

At a drugstore shelf she is comparing the ingredients on two hand creams.

[[FACING-2]]
Her head is straight on to the camera.
Her chin is dipped, so her face tilts downward and her eyelids read lower.
Her eyes are lowered toward what is in front of her.
She is reading something and concentrating on it.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Both of her hands together are holding two tubes of hand cream — holding one tube each.
Also in the picture: the shopping basket hooked over her elbow.

[[FACE-BARE-1]]
[[BODY-1]]
[[HAIR-COLOUR-2]]
She is wearing a black cropped hoodie with a plain crew neckline; grey wide-leg cargo trousers; a silver ear cuff; a small black crossbody pouch is worn across her body.

Setting: the aisle of a Taiwanese drugstore, shelves of boxed products.
Light: cool white fluorescent ceiling light in the drugstore, straight down from overhead; the white packaging on the shelves bounces it back onto her chest and chin. Exposure: the exposure is set for her face, the tubes blow out, and the depth of the shelving goes black.

[[CAMERA-1]]
It has the look of an old CCD compact camera: slightly soft, a little grain, colours very slightly off from true. Her figure is positioned off-centre in the frame. The surroundings throw a visible colour cast across her. The background is busy with the ordinary mess of the place. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-3]]

She is waiting for a train on the MRT platform, watching the arrivals display across the tracks.

[[FACING-1]]
[[HEAD-2]]
Her chin is raised a little, so her face tilts slightly upward.
Her eyes rest on something in the distance, off past the camera.
Her face is blank, the way a face goes when someone is simply waiting.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her right hand holds her transit card (holding her transit card).
Also in the picture: the arrivals display board on the platform.

[[FACE-BARE-1]]
[[BODY-2]]
[[HAIR-COLOUR-1]]
She is wearing an oatmeal tailored blazer over a white silk camisole with a square neckline; matching oatmeal straight wide-leg trousers; a thin silver bangle; a structured leather handbag hangs from her shoulder.

Setting: an MRT platform in Taipei, tiled floor and the track edge behind her.
Light: cool white fluorescent light in the platform ceiling; the terrazzo floor bounces a weak amount of it back up. At the same time, the warm white glow of a platform advertising lightbox falls flatly on her shoulder line from behind. Exposure: the exposure is set for her face, so her shoulder line on the lightbox side goes slightly blown and the far end of the platform goes black.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. Her figure is positioned off-centre in the frame. There is a trace of motion blur where she is moving, though her face stays sharp. The phone's auto white balance has gone a touch cool. The background is busy with the ordinary mess of the place. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
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
A vertical photograph of <<<68ff990e-1862-4003-bfe3-fe288275cdd4>>>.
[[FRAME-2]]

She is standing beside the park path with her whole body and her face turned to her own right, looking at something far off.

The camera is beside her, level with her shoulder, seeing the side of her body: the near shoulder is toward the lens and the far one directly behind it.
Her head is turned all the way to her own right, so the camera sees her profile: the outline of her forehead, nose, lips and chin reads clearly against the background, and only the near eye is visible.
Her chin is level.
Her eyes rest on something in the distance, off past the camera.
Calm and a little distant, thinking about something else.
Her whole face is unobstructed.
[[WHO-SHOOTS-1]]

Her left hand is hanging naturally at her side.
Her right hand is hanging naturally at her side.
Also in the picture: a wooden bench beside the path behind her; a single leaf falling behind her shoulder.

[[FACE-BARE-1]]
[[BODY-2]]
[[HAIR-COLOUR-3]]
She is wearing a cream cotton camisole with thin straps and a straight horizontal neckline; a thin silver necklace; a fine-knit open cardigan hangs from her shoulder.

Setting: a paved path through an ordinary neighbourhood park in Taipei, low shrubs and a row of trees.
Light: a thin overcast sky, the daylight arriving evenly from the whole sky at once, so every shadow edge on her is broad and soft; the pale paving fills it back evenly along the outline of her profile. Exposure: the exposure is set for her profile, the sky goes slightly blank, and the line from her jaw to her neck reads completely.

[[CAMERA-1]]
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. Her figure is positioned off-centre in the frame. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
[[CLOSED-SET-1]]
```

---

## §6 本輪請你判斷

### 6-1 上一輪你開的 10 條，處置如下

| ID | 你的判定 | 我做了什麼 |
|----|---------|-----------|
| C-34 | 20 段漏掉身材 | **屬實**。實測確認 0/20 提到 bust 或 silhouette。已用 B2 第二次成功的字串，依 framing 分三版（`[[BODY-1]]` 全身／`[[BODY-2]]` 軀幹／臉部特寫用短版）|
| C-35 | 仍大量使用否定式 | **多數屬實，已全部清掉**。現在 20 段的否定詞數是 **0**（`tools/lint_prompts.py` 逐段掃）。**但有一處我不同意，見 6-2** |
| C-36 | `She sits` 會改寫姿態 | **屬實，而且是我自己的模板害的**。實測 10 段 body_pose 非 seated 卻寫 `She sits`。改為 `She is positioned centrally／off-centre`，並加機器檢查禁止任何姿態動詞與 body_pose 衝突 |
| C-37 | 沒依 framing 過濾裁切外資訊 | **屬實**。服裝英文改為分層（top/bottom/shoes/bag/jewelry/rings），由 framing 決定輸出哪幾層；裁切外的手不再描述；包新增 `bag_state`（worn_shoulder／worn_crossbody／set_down／outside_frame）逐列指定 |
| C-38 | a07／c09 有誘發背影的語句 | **屬實**。a07 刪掉 `three-quarters`，c09 刪掉 `over her shoulder`，兩者都改成可見正面地標 |
| C-39 | c09 的 basket 翻譯破壞 zone | **屬實**。改為「靠在她彎曲的膝旁、從畫面下緣進入構圖」；c02 的紙箱也依你的建議具體化 |
| C-40 | c10 動作時點不一致 | **屬實**，已改為你建議的句子 |
| C-41 | outfit_01 應換成明顯不同的衣服 | **採納**。你的理由比我的處置好：高辨識度開口出現在 4/8 clean anchor 會與 identity 綁定，正好違反去服裝綁定的訓練目的。已換成米白細針織圓領（顏色、織法、領型三者都不同）|
| C-42 | 排除清單不足 | **屬實**。改為三種 view 各自的正面封閉集合（見 `[[CLOSED-SET-1]]`）|
| C-43 | 標題與模板編號漂移 | **屬實**。三個 pillar 標籤實測確認與 location／scene 不符，已修；樣板代號改為語意固定名稱（原本依長度排序的流水號每次重新產生都會變，這就是 `[[S8]]`/`[[S5]]` 對不上的原因）|

### 6-2 一處我不同意，請你裁決

你把景別句尾的 `Her waist, hips, legs and feet are outside the picture` 也算成
「§2-1 已證實無效的構圖否定」。**我認為這一句與失效的那種否定不同，而且有實測支持**：

- **失效的**是 `nothing below the knee is visible`——它只說「看不到什麼」，沒有說邊界在哪。
- **有效的**是 probe_v2 / probe_v3 / B2 第二次那三段，它們**都包含**
  `Her knees, lower legs, feet and shoes are outside the picture entirely` 這一句，
  而且景別三張全部正確。

差別在於前面有沒有先給出「畫面下緣切在哪裡」這個**位置事實**。
有位置事實在前，後面點名哪些部位落在界外是**在描述同一件事的另一半**，不是純排除。

我已經刪掉真正純排除的那半句（臉部特寫原本還接 `none of her torso, arms or hands is in it`）。
**剩下的這半句要不要也刪？** 我傾向保留，因為那是唯一有實測成功紀錄的寫法，
而全刪等於把三次成功的配方改掉、又沒有新的實測支持。你怎麼看？

### 6-3 這一輪請你做的事

**1. 上表 10 條可否結案？** 特別是 C-37 的分層邏輯（§5 每列的「framing → 看得見哪些層」）
   有沒有漏掉或砍過頭——例如 waist_up 我留了 `rings` 但砍了 `shoes`，這樣對嗎？

**2. 重審 3 列的語意覆核。** 修 C-43 的 pillar 標籤改動了資料，逐列 hash gate 因此讓
   `nico_c03`／`nico_c04`／`nico_c09` 的舊核可失效（validator 現在會擋）。
   請重新確認這三列的欄位與 prompt 是否同時成立。其餘 17 列的核可仍有效。

**3. 新展開的 20 段有沒有新問題？** 這一輪動了身材段、服裝分層、手部過濾、
   封閉集合、composition 模板——改動面很大，可能引入新的矛盾。

**4. 放行判定**：可以開始生成這 20 張，還是仍有 P0？

**現在有機器擋的規則**（`tools/lint_prompts.py`，20/20 通過）：
否定詞為 0、姿態動詞與 body_pose 一致、每段都有身材描述、
不得描述該景別看不見的服裝層、裁切外的手不得描述、
`expected_visible=false` 的道具不得出現、每段都有正面封閉集合收尾。

---

## §7 你的回覆區

把意見寫在下面這行以下。

<!-- ===== REPLIES BELOW — 本行以下不會被自動產生覆蓋 ===== -->


## ChatGPT R11 覆核回覆

### §6-2 裁決

**同意保留景別句尾的 `... are outside the picture`。**

我撤回 R10 對這一小段的判定。它前面已有明確的裁切線位置，後句是在陳述各部位相對於該邊界的空間位置；它不等同於單獨用 `nothing below...` 要模型自行推導裁切位置。更重要的是，probe_v2、probe_v3、B2 第二次已有三次同配方成功的實測。現階段保留已驗證配方，比為了形式上的「零排除句」改動它更合理。

因此 C-35 在其餘否定式均已移除的前提下可結案；lint 也不應把 `outside the picture` 這種有明確邊界前件的 locative statement 當成失效否定。

### C-44｜P0｜身材、朝向與相機模板仍未真正依 framing 分層

C-34 的身材內容已補回，但目前三版實際仍跨用了不可見區域：

- `[[BODY-1]]` 同時用於 full_body 與 knee_up；`nico_c02／c05／c09／c11` 在 lower legs／feet 位於畫面外時，仍要求 `long straight legs`。
- `[[BODY-2]]` 同時用於 chest_up 與 waist_up；`nico_a02／a03／a04／a05／c07／a08` 在腰位於畫面外時，仍要求 `a narrow waist`。
- `[[CAMERA-1]]` 對 face_closeup 也寫 `her face, her body and the background all stay in focus`，會重新要求模型容納不存在於畫面的 body。
- `nico_a01／c01` 的 face_closeup 後接 `[[FACING-3]]`，其中 `The camera sees ... her chest`，但畫面下緣只到鎖骨附近。
- outfit 分層也還有少數殘留：`nico_c01` 的 face_closeup 仍寫 `the hem long and tucked in`；`nico_a04／a05` 的 chest_up 仍寫上衣下擺位於 natural waist。

請至少拆成 face_closeup／chest_up／waist_up／knee_up／full_body 五種可見性模板。相機句可統一改成 `all visible parts of her and the background stay in focus together`，避免逐景別另列 body。這項未修前，C-34 與 C-37 都不能結案。

### C-45｜P0｜第三人稱封閉集合在戶外產生光源與場景矛盾

`[[CLOSED-SET-1]]` 固定寫：

> The only light in the room comes from the fixtures and windows named above.

它也套在公園、街道等戶外列；戶外沒有 room、fixture 或 window，真正光源是 sky。這會直接與前面的 overcast skylight 衝突。

建議改成跨場景成立的：

> Illumination comes exclusively from the natural or architectural light sources named above.

另外，mirror 版的 `the mirror holds her and the single phone ... that is the whole of what it holds` 容易被理解成鏡中沒有浴室背景。應把封閉範圍限縮為人物與裝置，例如「鏡中浴室場景內只有 Nico 與她手上的一支手機」。

C-42 目前不能結案。

### C-46｜P0｜`WHO-SHOOTS-1` 又把第二個人顯式帶回 prompt

18 段都先寫 `Someone standing near her...`，最後才要求唯一人物是 Nico。這兩句在語意上可以靠「攝影者在畫外」解釋，但對曾經生成別人的手與手機的模型而言，前一句仍是強烈的人物 cue，正好抵消 C-42 的目的。

改成不引入 person token 的相機位置敘述，例如：

> The camera viewpoint is nearby at eye level, with the imaging device and its operator beyond the frame edge.

如此仍能表達 third-person view，又不先要求模型想像 `Someone`。

### C-47｜P1｜ring 的可見性不能只由 framing 決定

C-37 的服裝分層整體方向正確，鞋子在 waist_up／knee_up 被砍掉也正確；但戒指應由「配戴在哪隻手＋該手是否入鏡」決定，而不是只看 framing。

outfit_01 有一枚銀戒；目前 `nico_a02／a03／c07` 都有手在胸前入鏡，prompt 卻把 ring 砍掉，反而 full_body 的 `nico_a07` 有輸出。請補 ring laterality，或明定該列不配戴；不要以 chest_up 一律刪除。這不必單獨阻擋 Nico，但應與本輪 P0 一起修。

### C-34～C-43 結案判定

| ID | 判定 |
|---|---|
| C-34 | **不同意結案**：身材已補回，但 framing 分版仍不完整，見 C-44 |
| C-35 | **同意結案**：並同意保留有明確裁切線前件的 `outside the picture` |
| C-36 | **同意結案** |
| C-37 | **不同意結案**：主要修正成立，但仍有不可見身材／衣服細節與 ring 過濾問題，見 C-44、C-47 |
| C-38 | **同意結案** |
| C-39 | **同意結案** |
| C-40 | **同意結案** |
| C-41 | **同意結案**：新 outfit 與錨點在顏色、織法、領型上已明顯區隔 |
| C-42 | **不同意結案**：見 C-45、C-46 |
| C-43 | **同意結案** |

### 三列重審

- **`nico_c03`**：結構欄位彼此成立；早餐店 pillar、scene、坐姿、視線、雙手、桌面道具、混合光與 waist_up 相容。**列本身無異議**。其 prompt 仍受 C-44／C-46 共用模板影響，模板修正後再簽 prompt hash。
- **`nico_c04`**：結構欄位彼此成立；洗澡後濕髮、平靜表情、床邊坐姿、front selfie、雙手、道具與晨光相容。**列本身無異議**。其 prompt 仍受 C-44 的 camera 可見性措辭影響。
- **`nico_c09`**：C-38／C-39 的兩處修正正確；蹲姿仍呈現胸前正面、轉頭看鏡頭、購物籃靠彎曲膝並從下緣入鏡，物理上成立。**列本身無異議**。其 prompt 仍受 C-44 的 knee_up 身材模板及 C-45／C-46 共用模板影響。

### 放行判定

**目前仍不放行生成。** 先修 C-44、C-45、C-46；C-47 可同輪處理。修正後不必重掃未受影響的內容，但需要重審所有被修改共用模板展開到的列，並重新簽 prompt hash。
