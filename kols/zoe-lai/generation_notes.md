# Zoe Lai — AI 生成規劃筆記

> **狀態：PENDING — 尚未執行任何生成**
> 本文件是訓練圖與批次拍攝的**規劃文件**，不是生產紀錄。目前沒有 soul_id、沒有已生成圖片、沒有已生成影片。所有數字、日期、Job ID 待實際執行後才會補上，本檔案不預先捏造。

---

## 人物設定

| 欄位 | 設定 |
|------|------|
| 名字 | Zoe Lai（賴柔伊） |
| 年齡 | 26 歲 |
| 國籍 | 台灣（花蓮出身，衝浪季移動到墾丁） |
| 臉型 | 曬過的橢圓臉、笑容自然大方，直眉，鼻樑和上頰有淡淡雀斑，眼神因常年面對海面反光而有輕微瞇眼、警覺又放鬆。無修飾感，健康、有點風霜的耐看 |
| 身材 | 游泳選手/衝浪者體態——肩背因划水結實，腰腹精瘦有線條，腿部有力，臀部天生曲線，均勻深色年曬肌膚。強壯、實用型身材，不是健身房雕塑出來的樣子 |
| 髮型 | 海浪波浪捲長髮，深棕色髮尾被鹽和陽光曬淺，幾乎總是鹽風吹亂或鬆散編成的辮子 |
| 眼鏡 | 無 — 偶爾把太陽眼鏡推到頭髮上，不戴著 |
| 穿衣風格 | 比基尼是日常打底；外面隨手套寬大男裝襯衫或素T，牛仔短褲，大多數時候光腳 |

---

## 核心 Prompt 結構

> 純物理描述，不參照任何真實名人或藝人臉型。

```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint
from years facing open water, athletic swimmer/surfer build with toned shoulders and upper back,
lean defined core, strong legs, naturally curvy hips, deep even golden tan,
long beachy wave dark brown hair lightened at the ends from sun and salt, salt-tousled or in a loose undone braid,
[SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING],
high natural contrast, slightly overexposed highlights, true-to-life unretouched skin texture with visible tan lines,
candid outdoor lifestyle photo, shot on phone or action camera, Instagram style
```

**風格關鍵詞備註**：
- 一定要保留 `true-to-life unretouched skin texture` 和 `visible tan lines`——這是 Zoe 美學的核心，跟其他角色的「精緻磨皮感」相反
- 光線永遠是自然光關鍵詞（`morning light` / `harsh midday sun` / `golden hour backlight`），不要出現任何棚燈、環形燈相關詞
- 禁止出現裸露或性暗示相關詞彙；服裝上限是比基尼/泳裝，符合海灘網紅帳號的主流尺度
- **每個 prompt 均須落實 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五項checklist**（2026-07-24 新增）：具體皮膚質感關鍵字（毛孔、非磨皮、自然瑕疵、曬痕）、逐場景明確的裝置/鏡頭破綻（前鏡頭自拍 vs. 後鏡頭 vs. 運動相機、對焦軟化、高光爆掉、鏡頭上的水珠、動態模糊、壓縮痕跡）、混合不均勻的自然光配方（正午硬光、黃金時段、冷暖混色，不是乾淨棚拍）、具體生活雜物背景（沙子、蠟塊、隨手丟的毛巾、板具、防曬乳）、完整明確的服裝描述

---

## 計畫批次 Prompt 規劃

> 以下為**計畫中**的訓練圖批次，尚未執行生成。實際執行後應在此文件補上：使用的平台/模型、實際生成張數、選用結果、圖片路徑。目前僅記錄場景規劃與草稿 prompt。

### 批次規劃 1 — 晨間衝浪，日出前走向海邊（計畫 2 張）

**場景描述**：天還沒亮，Zoe 走向花蓮海邊，板夾在腋下，天色剛開始從深藍轉紫，第一道光還沒出現。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with toned shoulders and upper back, lean defined core, strong legs,
naturally curvy hips, deep even golden tan, long beachy wave dark brown hair in a loose undone braid,
visible skin pores, subtle natural skin texture, faint tan line at swimsuit strap edge, slight oil sheen on T-zone,
unretouched skin detail, natural skin imperfections,
walking toward the beach before sunrise carrying a surfboard under one arm, wearing a black one-piece swimsuit,
walking pose mid-stride viewed from the side,
wet sand footprints trailing behind her, a half-buried surf wax tin near a clump of dry seaweed,
a distant fishing boat silhouette faint on the horizon,
pre-dawn deep blue-purple sky with faint first amber light on the horizon, mixed color temperature —
cool blue ambient sky light blending with warm faint horizon glow, uneven light falloff leaving her front
in soft shadow with a thin warm rim light from the horizon,
shot on iPhone 15 Pro rear camera handheld while walking, slight autofocus hunting softness on the dark
rocks in the background, faint high-ISO grain in shadow areas, subtle motion blur on swaying arm and
loose braid, light JPEG compression banding visible in the deep blue sky gradient,
high natural contrast, candid outdoor lifestyle photo, Instagram style
```

---

### 批次規劃 2 — 泳裝日常，鏡前穿搭確認（計畫 2 張）

**場景描述**：站在花蓮公寓的小房間鏡子前，決定今天穿哪件比基尼，外面披一件寬大男裝襯衫，隨手扣兩顆扣子。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with toned shoulders and upper back, lean defined core, strong legs,
naturally curvy hips, deep even golden tan, long beachy wave dark brown hair salt-tousled and loose,
visible skin pores, subtle natural skin texture, faint tan lines at shoulder and hip from bikini straps,
slight oil sheen on T-zone from morning humidity, unretouched skin detail, natural skin imperfections,
standing in front of a small bedroom mirror, wearing a black triangle bikini with an oversized faded
men's button-down shirt worn fully open over it, hands buttoning two buttons at the chest,
looking at her own reflection not at camera,
an unmade bed with rumpled sheets visible in the corner behind her, a damp beach towel draped over a
wooden chair, sandy flip-flops kicked off near the door, a phone charging cable coiled loose on the
nightstand, a salt-crusted rash guard hanging on the door hook,
bright natural morning window light mixed with the warmer tone of an overhead room lamp left on,
uneven falloff with a soft shadow edge cast by the window frame across the mirror,
shot on iPhone 15 Pro front camera held at chest height for the mirror reflection, slight autofocus
softness at the mirror's edge, natural highlight clipping where window light hits the mirror glass,
faint compression artifacts along the reflection border,
full body mirror shot, candid unposed moment, high natural contrast, Instagram style
```

---

### 批次規劃 3 — 沖鹽淨身，衝浪後戶外沖水（計畫 2 張）

**場景描述**：衝完浪後在戶外沙灘沖澡柱下沖掉鹽分和沙子，頭往後仰,陽光直射,水珠飛濺。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with toned shoulders and upper back, lean defined core, strong legs,
naturally curvy hips, deep even golden tan, wet long beachy wave dark brown hair slicked back from rinsing,
visible skin pores on wet skin, subtle natural skin texture, faint tan lines where the bikini sits,
unretouched skin detail, natural skin imperfections,
standing under an outdoor beach rinse shower, wearing a black bikini, head tilted back with eyes closed,
water droplets visible in bright sunlight running down shoulders and arms,
sandy concrete rinse platform underfoot, a surf wax tin resting on the shower's concrete ledge, a coiled
garden hose nearby, a used towel tossed over a plastic beach chair just outside the shower, flip-flops
and a half-squeezed sunscreen bottle on the ground,
harsh midday natural sunlight directly overhead, hard-edged shadow cast by the rinse pole, water droplets
catching the sun as tiny flares and glare on wet skin,
shot on an action camera mounted nearby, faint water droplets and light mist speckled directly on the
lens creating soft blur halos, slight motion blur as she tilts her head back, natural highlight clipping
where direct sun hits wet skin and water spray,
medium shot from the side, candid post-surf moment, high natural contrast, slightly overexposed highlights,
Instagram style
```

---

### 批次規劃 4 — 衝浪旅行，墾丁黃金時段全身（計畫 2 張）

**場景描述**：墾丁海邊民宿陽台，傍晚黃金時段，板子晾在欄杆上，Zoe 站著看向海景，全身入鏡。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with toned shoulders and upper back, lean defined core, strong legs,
naturally curvy hips, deep even golden tan, long beachy wave dark brown hair down and windblown,
visible skin pores, subtle natural skin texture, faint tan lines visible at bikini edges, slight oil
sheen from the day's heat, unretouched skin detail, natural skin imperfections,
standing on a beachside guesthouse balcony in Kenting, a surfboard with visible wax residue resting
against the peeling-paint railing beside her, wearing a bikini with denim cutoff shorts,
full body shot, looking out toward the ocean not at camera,
a damp towel tossed over a plastic chair on the balcony, flip-flops kicked off near the railing, a
half-empty water bottle and a tube of sunscreen left on the balcony ledge,
warm golden hour backlight from the setting sun over the water mixed with cooler ambient shade under
the balcony roof overhang, uneven light falloff with a soft warm rim light on her hair and shoulders,
shot on iPhone 15 Pro rear camera handheld by a friend, slight autofocus softness on the distant ocean
horizon, warm highlight bloom and faint lens flare from the low sun, subtle motion blur on windblown
hair, light JPEG compression artifacts in the gradient sky,
high natural contrast, candid travel lifestyle photo, Instagram style
```

---

### 批次規劃 5 — 東岸小屋，公寓陽台吊床（計畫 2 張）

**場景描述**：花蓮公寓的小陽台，午後，Zoe 躺在吊床上放空，板子隨手靠在牆邊，衝浪裝備散落，室內時間本來就不多，這裡只是放裝備跟休息的地方。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with toned shoulders and upper back, lean defined core, strong legs,
naturally curvy hips, deep even golden tan, long beachy wave dark brown hair loose and slightly damp
from the day's heat,
visible skin pores, subtle natural skin texture, faint tan lines at the collar and sleeve edge, slight
oil sheen on T-zone from the afternoon humidity, unretouched skin detail, natural skin imperfections,
lying in a hammock on a small apartment balcony, one leg draped over the side, wearing an oversized
faded grey cotton t-shirt with a black bikini visible at the collar, no bra line showing, bare legs,
relaxed unposed body language, not looking at camera,
a surfboard with visible wax residue resting against the wall, a coiled leash on the tile floor, a damp
rash guard drying over the balcony railing, flip-flops kicked off near the hammock, a phone charging
cable dangling off a low table, fine sand tracked in across the tile floor,
mixed natural light — cool shaded ambient light under the balcony roof blending with a warm patch of
direct afternoon sun cutting across the hammock fabric, uneven falloff, soft shadow edges from the
railing bars,
shot on iPhone 15 Pro front camera held at arm's length, slight autofocus softness on the background
board and railing, natural highlight clipping where the direct sun patch hits the hammock fabric,
faint motion blur from the hammock's gentle sway,
high natural contrast, candid unposed lifestyle photo, Instagram style
```

---

### 批次規劃 6 — 划水健身，沙灘瑜伽日落伸展（計畫 2 張）

**場景描述**：傍晚金色時段，衝完浪後在沙灘上做瑜伽伸展，動作專注，板子插在一旁沙裡，沒有健身房、沒有器材，只有海跟她的身體。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with toned shoulders and upper back, lean defined core, strong legs,
naturally curvy hips, deep even golden tan, long beachy wave dark brown hair pulled back loosely,
visible skin pores, subtle natural skin texture showing muscle definition without excess gloss, faint
tan lines at bikini edges, slight sweat sheen on shoulders and lower back, unretouched skin detail,
natural skin imperfections,
doing a focused standing beach yoga stretch on the sand, full body, wearing a black sport bikini,
eyes closed or gaze downward, absorbed in the stretch not performing for camera,
a surfboard stuck upright in the sand nearby with a wax comb sticking out of its bag, a beach towel
tossed haphazardly beside her mat, a half-full water bottle, bare footprints trailing behind her in
the sand,
low golden hour sun creating strong warm directional backlight mixed with cooler blue tones reflected
off the wet sand near the shoreline, uneven light with a hard-edged shadow of her body stretching
long across the sand,
shot on iPhone 15 Pro rear camera on a low tripod set in the sand, slight autofocus softness on the
background waves, natural highlight clipping and lens flare from the direct low sun behind her, fine
sand grains kicked up near her feet with subtle motion blur, faint JPEG compression artifacts along
the bright horizon line,
high natural contrast, candid outdoor lifestyle photo, Instagram style
```

---

## 下一步（待執行）

1. 選定生成平台與模型（尚未決定 — 需先確認亞洲臉孔生成效果，可參考 Iris Chen 案例中 Seedream 4.5 優於 Recraft V4.1 的結論，但仍需針對 Zoe 的曬痕/雀斑/健康膚況做效果測試）
2. 依上述 6 個批次規劃生成訓練圖，每批次先生成 2 張比較效果
3. 訓練圖確認後，執行 Soul 訓練流程
4. 訓練完成後，才開始规划後續生活照與影片批次（本文件屆時需新增「已生成」章節，並記錄實際 soul_id、Job ID、圖片路徑）

**目前無**：soul_id、已生成圖片數量、生成日期、Job ID。以上欄位皆待實際執行後填入，禁止在此階段預先填寫。
