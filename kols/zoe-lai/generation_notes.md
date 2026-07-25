# Zoe Lai — AI 生成規劃筆記

> **狀態：PENDING — 已生成第一輪「發現批次」候選圖，等待使用者選出喜歡的臉/風格，尚未錨定身分、尚未進入 Soul 訓練**
> 本文件是訓練圖與批次拍攝的**規劃文件**。目前沒有 soul_id、沒有 Reference Element、沒有已生成影片。2026-07-25 已生成 4 張獨立的「發現批次」候選參考圖（見下方「2026-07-25 發現批次」章節）供使用者挑選喜歡的臉孔/風格方向——**這 4 張圖彼此之間不共享同一身分**（獨立生成，跟 Vicky Lin 的經驗一致：獨立生成不會自動保持同一張臉），僅供風格/臉孔挑選用途。使用者選定一張後，下一步才會建立 Reference Element 錨定該身分，再展開完整訓練圖批次。除此之外的批次規劃（下方 6 個批次）皆仍為草稿，所有 soul_id、完整訓練圖數量、生成日期、Job ID 待實際執行後才會補上，本檔案不預先捏造。

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
26-year-old Taiwanese woman, strikingly beautiful sun-warmed oval face with a gorgeous wide smile,
gorgeous beach-influencer good looks (NOT a stern, athlete's, or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint
from years facing open water, athletic swimmer/surfer build with soft feminine curves, toned shoulders
and upper back from paddling (never blocky, vascular, or heavily muscled), 88cm bust (D cup, full and
naturally curvy), 59cm waist (lean with only a subtle soft hint of core tone), 90cm hips (naturally
curvy, shapely thighs), strong but shapely legs, deep even golden tan,
visible skin pores, subtle natural skin texture, true-to-life unretouched skin texture with visible tan lines,
long beachy wave dark brown hair lightened at the ends from sun and salt, salt-tousled or in a loose undone braid,
[SCENE], wearing [OUTFIT — bikini as daily basewear, natural beach-appropriate color coordination, not
overly styled or fashion-shoot posed], [MINIMAL ACCESSORY — a simple watch, sunglasses pushed up into
her hair, or a thin anklet; never more than one], [DYNAMIC CANDID POSE/ANGLE — walking, paddling,
mid-laugh, teaching, caught mid-motion, NOT a static posed beach-model stance],
[NATURAL FLATTERING LIGHT — golden hour dawn patrol, bright midday sun, or sunset backlight; shallow
depth of field with soft blurred bokeh background],
high dynamic range, crisp sharp focus on subject, high natural contrast, slightly overexposed highlights,
natural color grading — NOT degraded, grainy, or dim, true-to-life unretouched skin texture with visible tan lines,
candid outdoor lifestyle photo, shot on iPhone or action camera with crisp high-quality output, Instagram style
```

**風格關鍵詞備註**：
- 一定要保留 `true-to-life unretouched skin texture`、`visible skin pores`、`visible tan lines`——這是 Zoe 美學的核心，跟其他角色的「精緻磨皮感」相反
- **三圍數字（88cm bust／D cup、59cm waist、90cm hips，見 `profile.json` 的 `measurements`）已直接寫進核心 prompt 本體**，不再只靠「naturally curvy」這種模糊形容詞帶過
- **光線預設為新版「討喜自然光」配方**：黃金時段晨光（dawn patrol）、正午亮光、日落逆光，均搭配淺景深背景虛化 + crisp high dynamic range；只有極少數室內公寓/小貨車場景（見下方批次規劃 2）可以保留舊版「混合不均勻」配方，其餘場景一律不得使用「uneven/degraded/dim/muddy」這類把畫質往下拉的字——真實感來自皮膚質感、生活雜物與鏡頭裝置破綻，不是靠調暗調糊
- 禁止出現裸露或性暗示相關詞彙；服裝上限是比基尼/泳裝，符合海灘網紅帳號的主流尺度；配件維持極簡（手錶、推上頭頂的墨鏡、細腳鍊，符合她低維護的人設，不要堆疊配件變成刻意造型）
- 姿勢預設為動態抓拍（走路、划水、教學互動中的笑場），避免靜態擺拍的「網紅拍照姿勢」感
- **每個 prompt 均須落實 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五項checklist**（2026-07-24 新增，2026-07-25 光源項修正）：具體皮膚質感關鍵字（毛孔、非磨皮、自然瑕疵、曬痕）、逐場景明確的裝置/鏡頭破綻（前鏡頭自拍 vs. 後鏡頭 vs. 運動相機、對焦軟化、高光爆掉、鏡頭上的水珠、動態模糊、壓縮痕跡）、對應場景類型的正確光源配方（戶外用討喜自然光+淺景深，室內例外場景才用混合不均勻）、具體生活雜物背景（沙子、蠟塊、隨手丟的毛巾、板具、防曬乳）、完整明確的服裝描述、三圍數字是否直接寫入而非模糊帶過

**⚠️ 2026-07-25 燈光/身材數字校準**：使用者在 Vicky Lin 身上驗證過「真實感 ≠ 畫質差」之後，回頭檢查 Zoe 的草稿發現同樣的舊思路殘留：(1) 核心 prompt 只寫「naturally curvy hips」等模糊詞，沒有把 `profile.json` 裡已經確認的三圍數字（88-59-90cm，D 罩杯）寫進去；(2) 部分批次沿用「uneven light falloff」「film grain」「compression banding」把整體畫面往「做舊/偏暗」的方向拉，即使場景本身是黃金時段海邊或正午豔陽這種本來就該明亮清晰的光線；(3) 身材描述裡的「lean defined core」用詞有跟 Vicky 第一輪犯的「健美選手」錯誤同樣的風險，需要比照 `profile.json` 已修正版本明確排除「blocky / vascular / heavily muscled」。這次校準：三圍數字直接寫入核心 prompt 與全部 6 個批次；除了批次規劃 2（室內小房間鏡前）保留原本的室內混合光源配方外，其餘 5 個批次全部改用「黃金時段/正午豔陽/日落逆光 + 淺景深虛化 + crisp high dynamic range」的新配方，並在每個 prompt 明講 `NOT degraded, grainy, or dim`；臉部與身材描述統一比照 `profile.json` 已修正的「gorgeous beach-influencer, NOT athlete/masculine」語言，移除「lean defined core」之類有風險的字眼。`character.md`／`profile.json` 的外型描述本身不變動，只是把已經確認的設定確實寫進實際會送出生成的 prompt 字串裡。

---

## 計畫批次 Prompt 規劃

> 以下為**計畫中**的訓練圖批次，尚未執行生成。實際執行後應在此文件補上：使用的平台/模型、實際生成張數、選用結果、圖片路徑。目前僅記錄場景規劃與草稿 prompt。

### 批次規劃 1 — 晨間衝浪，日出前走向海邊（計畫 2 張）

**場景描述**：天還沒亮，Zoe 走向花蓮海邊，板夾在腋下，天色剛開始從深藍轉紫，第一道光還沒出現。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, strikingly beautiful sun-warmed oval face with a gorgeous wide smile,
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, deep even golden tan, long beachy wave dark brown hair in a loose undone braid,
visible skin pores, subtle natural skin texture, faint tan line at swimsuit strap edge, slight oil sheen on T-zone,
unretouched skin detail, natural skin imperfections,
walking toward the beach before sunrise carrying a surfboard under one arm, wearing a black one-piece swimsuit,
dynamic candid walking pose mid-stride viewed from the side, caught in natural motion not posed for camera,
wet sand footprints trailing behind her, a half-buried surf wax tin near a clump of dry seaweed,
a distant fishing boat silhouette faint on the horizon,
pre-dawn sky just beginning to turn from deep blue to the first warm amber of first light on the horizon,
natural directional light with soft flattering falloff even in the low pre-dawn glow, a thin warm rim
light catching her shoulder and profile from the horizon, shallow depth of field with the dark rocks
and distant shoreline softly blurred behind her,
shot on iPhone 15 Pro rear camera handheld while walking, slight natural autofocus softness on the
blurred background rocks, subtle motion blur on swaying arm and loose braid from the walking motion,
crisp sharp focus on her face and figure, high dynamic range, natural color grading — NOT degraded,
grainy, or dim, even in the pre-dawn light the image reads bright, clean, and crisp,
high natural contrast, candid outdoor lifestyle photo, Instagram style
```

---

### 批次規劃 2 — 泳裝日常，鏡前穿搭確認（計畫 2 張）

**場景描述**：站在花蓮公寓的小房間鏡子前，決定今天穿哪件比基尼，外面披一件寬大男裝襯衫，隨手扣兩顆扣子。

**草稿 Prompt**：

> **⚠️ 唯一保留室內混合光源配方的批次**：這是小房間室內鏡前場景，符合 `SEXY_SCENE_LIBRARY.md` 2026-07-25 修正後允許的「室內公寓例外」，維持原本的「混合、不均勻」光源邏輯，但同樣不能整體偏暗/偏糊——依然要清晰明亮，只是光源組成是室內窗光+燈光混色，而不是戶外討喜自然光配方。

```
26-year-old Taiwanese woman, strikingly beautiful sun-warmed oval face with a gorgeous wide smile,
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, deep even golden tan, long beachy wave dark brown hair salt-tousled and loose,
visible skin pores, subtle natural skin texture, faint tan lines at shoulder and hip from bikini straps,
slight oil sheen on T-zone from morning humidity, unretouched skin detail, natural skin imperfections,
standing in front of a small bedroom mirror, wearing a black triangle bikini with an oversized faded
men's button-down shirt worn fully open over it, natural beach-appropriate color coordination not
overly styled, hands buttoning two buttons at the chest, a simple watch on one wrist,
looking at her own reflection not at camera, relaxed candid unposed body language,
an unmade bed with rumpled sheets visible in the corner behind her, a damp beach towel draped over a
wooden chair, sandy flip-flops kicked off near the door, a phone charging cable coiled loose on the
nightstand, a salt-crusted rash guard hanging on the door hook,
bright natural morning window light mixed with the warmer tone of an overhead room lamp left on,
uneven falloff with a soft shadow edge cast by the window frame across the mirror, still reading bright
and clean overall — NOT degraded, grainy, or dim,
shot on iPhone 15 Pro front camera held at chest height for the mirror reflection, slight autofocus
softness at the mirror's edge, natural highlight clipping where window light hits the mirror glass,
faint compression artifacts along the reflection border, crisp sharp focus on her figure,
full body mirror shot, candid unposed moment, high natural contrast, Instagram style
```

---

### 批次規劃 3 — 沖鹽淨身，衝浪後戶外沖水（計畫 2 張）

**場景描述**：衝完浪後在戶外沙灘沖澡柱下沖掉鹽分和沙子，頭往後仰,陽光直射,水珠飛濺。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, strikingly beautiful sun-warmed oval face with a gorgeous wide smile,
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, deep even golden tan, wet long beachy wave dark brown hair slicked back from rinsing,
visible skin pores on wet skin, subtle natural skin texture, faint tan lines where the bikini sits,
unretouched skin detail, natural skin imperfections,
standing under an outdoor beach rinse shower, wearing a black bikini, head tilted back with eyes closed,
candid unposed moment caught mid-motion not performing for camera,
water droplets visible in bright sunlight running down shoulders and arms,
sandy concrete rinse platform underfoot, a surf wax tin resting on the shower's concrete ledge, a coiled
garden hose nearby, a used towel tossed over a plastic beach chair just outside the shower, flip-flops
and a half-squeezed sunscreen bottle on the ground,
bright harsh midday natural sunlight directly overhead, crisp hard-edged shadow cast by the rinse pole,
shallow depth of field with the background beach chairs and hose softly blurred, water droplets catching
the sun as tiny sparkling flares on wet skin, high dynamic range, natural color grading — NOT degraded,
grainy, or dim, the whole frame reads bright, clean, and sun-drenched,
shot on an action camera mounted nearby, faint water droplets speckled directly on the lens creating
soft blur halos, slight motion blur as she tilts her head back, natural highlight clipping where direct
sun hits wet skin and water spray, crisp sharp focus on her face and figure,
medium shot from the side, candid post-surf moment, high natural contrast, slightly overexposed highlights,
Instagram style
```

---

### 批次規劃 4 — 衝浪旅行，墾丁黃金時段全身（計畫 2 張）

**場景描述**：墾丁海邊民宿陽台，傍晚黃金時段，板子晾在欄杆上，Zoe 站著看向海景，全身入鏡。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, strikingly beautiful sun-warmed oval face with a gorgeous wide smile,
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, deep even golden tan, long beachy wave dark brown hair down and windblown,
visible skin pores, subtle natural skin texture, faint tan lines visible at bikini edges, slight oil
sheen from the day's heat, unretouched skin detail, natural skin imperfections,
standing on a beachside guesthouse balcony in Kenting, a surfboard with visible wax residue resting
against the peeling-paint railing beside her, wearing a bikini with denim cutoff shorts, natural
beach-appropriate color coordination not overly styled, sunglasses pushed up into her hair,
full body shot, looking out toward the ocean not at camera, relaxed candid stance not posed for camera,
a damp towel tossed over a plastic chair on the balcony, flip-flops kicked off near the railing, a
half-empty water bottle and a tube of sunscreen left on the balcony ledge,
warm golden hour backlight from the setting sun over the water, natural directional light with soft
flattering falloff, shallow depth of field with the balcony overhang and horizon softly blurred behind
her, a soft warm rim light on her hair and shoulders, high dynamic range, natural color grading —
NOT degraded, grainy, or dim, the whole scene reads bright, warm, and crisp,
shot on iPhone 15 Pro rear camera handheld by a friend, slight natural autofocus softness on the distant
ocean horizon, warm highlight bloom and faint lens flare from the low sun, subtle motion blur on
windblown hair, crisp sharp focus on her face and figure,
high natural contrast, candid travel lifestyle photo, Instagram style
```

---

### 批次規劃 5 — 東岸小屋，公寓陽台吊床（計畫 2 張）

**場景描述**：花蓮公寓的小陽台，午後，Zoe 躺在吊床上放空，板子隨手靠在牆邊，衝浪裝備散落，室內時間本來就不多，這裡只是放裝備跟休息的地方。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, strikingly beautiful sun-warmed oval face with a gorgeous wide smile,
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, deep even golden tan, long beachy wave dark brown hair loose and slightly damp from the day's heat,
visible skin pores, subtle natural skin texture, faint tan lines at the collar and sleeve edge, slight
oil sheen on T-zone from the afternoon humidity, unretouched skin detail, natural skin imperfections,
lying in a hammock on a small apartment balcony, one leg draped over the side, wearing an oversized
faded grey cotton t-shirt with a black bikini visible at the collar, no bra line showing, bare legs,
relaxed candid unposed body language, not looking at camera, caught in a natural moment of rest,
a surfboard with visible wax residue resting against the wall, a coiled leash on the tile floor, a damp
rash guard drying over the balcony railing, flip-flops kicked off near the hammock, a phone charging
cable dangling off a low table, fine sand tracked in across the tile floor,
bright natural balcony daylight — open sky light blending with a warm patch of direct afternoon sun
cutting across the hammock fabric, soft flattering falloff, shallow depth of field with the surfboard
and railing softly blurred in the background, high dynamic range, natural color grading — NOT degraded,
grainy, or dim, the scene reads bright and crisp even in its relaxed low-key mood,
shot on iPhone 15 Pro front camera held at arm's length, slight autofocus softness on the background
board and railing, natural highlight clipping where the direct sun patch hits the hammock fabric,
faint motion blur from the hammock's gentle sway, crisp sharp focus on her face and figure,
high natural contrast, candid unposed lifestyle photo, Instagram style
```

---

### 批次規劃 6 — 划水健身，沙灘瑜伽日落伸展（計畫 2 張）

**場景描述**：傍晚金色時段，衝完浪後在沙灘上做瑜伽伸展，動作專注，板子插在一旁沙裡，沒有健身房、沒有器材，只有海跟她的身體。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, strikingly beautiful sun-warmed oval face with a gorgeous wide smile,
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, deep even golden tan, long beachy wave dark brown hair pulled back loosely,
visible skin pores, subtle natural skin texture showing muscle definition without excess gloss, faint
tan lines at bikini edges, slight sweat sheen on shoulders and lower back, unretouched skin detail,
natural skin imperfections,
doing a focused standing beach yoga stretch on the sand, full body, wearing a black sport bikini,
eyes closed or gaze downward, absorbed in the stretch not performing for camera, dynamic candid
movement caught mid-stretch not a static posed shot,
a surfboard stuck upright in the sand nearby with a wax comb sticking out of its bag, a beach towel
tossed haphazardly beside her mat, a half-full water bottle, bare footprints trailing behind her in
the sand,
low golden hour sun creating strong warm directional backlight with soft flattering falloff, shallow
depth of field with the shoreline and waves softly blurred behind her, a crisp hard-edged shadow of
her body stretching long across the sand, high dynamic range, natural color grading — NOT degraded,
grainy, or dim, the whole frame reads bright, golden, and crisp,
shot on iPhone 15 Pro rear camera on a low tripod set in the sand, slight autofocus softness on the
background waves, natural highlight clipping and lens flare from the direct low sun behind her, fine
sand grains kicked up near her feet with subtle motion blur, crisp sharp focus on her face and figure,
high natural contrast, candid outdoor lifestyle photo, Instagram style
```

---

## 下一步（待執行）

1. 選定生成平台與模型（尚未決定 — 需先確認亞洲臉孔生成效果，可參考 Iris Chen 案例中 Seedream 4.5 優於 Recraft V4.1 的結論，但仍需針對 Zoe 的曬痕/雀斑/健康膚況做效果測試）
2. 依上述 6 個批次規劃生成訓練圖，每批次先生成 2 張比較效果
3. 訓練圖確認後，執行 Soul 訓練流程
4. 訓練完成後，才開始规划後續生活照與影片批次（本文件屆時需新增「已生成」章節，並記錄實際 soul_id、Job ID、圖片路徑）

**目前無**：soul_id、已生成圖片數量、生成日期、Job ID。以上欄位皆待實際執行後填入，禁止在此階段預先填寫。
