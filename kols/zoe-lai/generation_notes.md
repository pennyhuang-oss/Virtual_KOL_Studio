# Zoe Lai — AI 生成規劃筆記

> **狀態：PENDING — 第一輪「發現批次」候選圖（膚色曬黑、已判定為錯誤設計）已改名為 `round1_candidate_01–04.png` 存查；膚色規則已全面修正為白皙基調，並改用 `seedream_v4_5` 規劃 Round 2，但 Round 2 實際生成因帳戶 credits 不足（僅 0.35，需至少 4）而失敗，尚無任何 Round 2 圖片、尚未錨定身分、尚未進入 Soul 訓練**
> 本文件是訓練圖與批次拍攝的**規劃文件**。目前沒有 soul_id、沒有 Reference Element、沒有已生成影片。2026-07-25 已生成 4 張獨立的「發現批次」候選參考圖（見下方「2026-07-25 發現批次」章節）供使用者挑選喜歡的臉孔/風格方向——**這 4 張圖彼此之間不共享同一身分**（獨立生成，跟 Vicky Lin 的經驗一致：獨立生成不會自動保持同一張臉），僅供風格/臉孔挑選用途。使用者選定一張後，下一步才會建立 Reference Element 錨定該身分，再展開完整訓練圖批次。除此之外的批次規劃（下方 6 個批次）皆仍為草稿，所有 soul_id、完整訓練圖數量、生成日期、Job ID 待實際執行後才會補上，本檔案不預先捏造。

---

## 人物設定

| 欄位 | 設定 |
|------|------|
| 名字 | Zoe Lai（賴柔伊） |
| 年齡 | 26 歲 |
| 國籍 | 台灣（花蓮出身，衝浪季移動到墾丁） |
| 臉型 | 白皙、溫潤有光澤的橢圓臉、笑容自然大方，直眉，鼻樑和上頰有淡淡雀斑，眼神因常年面對海面反光而有輕微瞇眼、警覺又放鬆。無修飾感，健康、白皙的耐看（不是曬黑/古銅色調） |
| 身材 | 游泳選手/衝浪者體態——肩背因划水結實，腰腹精瘦有線條，腿部有力，臀部天生曲線，白皙細緻的肌膚（即使常年戶外活動、認真防曬也維持白皙，不是深色年曬肌膚）。強壯、實用型身材，不是健身房雕塑出來的樣子 |
| 髮型 | 海浪波浪捲長髮，深棕色髮尾被鹽和陽光曬淺，幾乎總是鹽風吹亂或鬆散編成的辮子 |
| 眼鏡 | 無 — 偶爾把太陽眼鏡推到頭髮上，不戴著 |
| 穿衣風格 | 比基尼是日常打底；外面隨手套寬大男裝襯衫或素T，牛仔短褲，大多數時候光腳 |

---

## 核心 Prompt 結構

> 純物理描述，不參照任何真實名人或藝人臉型。

```
26-year-old Taiwanese woman, strikingly beautiful, warm, radiant oval face with a gorgeous wide smile,
fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored),
gorgeous beach-influencer good looks (NOT a stern, athlete's, or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint
from years facing open water, athletic swimmer/surfer build with soft feminine curves, toned shoulders
and upper back from paddling (never blocky, vascular, or heavily muscled), 88cm bust (D cup, full and
naturally curvy), 59cm waist (lean with only a subtle soft hint of core tone), 90cm hips (naturally
curvy, shapely thighs), strong but shapely legs, fair, porcelain-toned skin that stays fair despite her beach lifestyle, only the faintest natural warmth from time outdoors, NOT deeply tanned or bronzed,
visible skin pores, subtle natural skin texture, true-to-life unretouched skin texture,
long beachy wave dark brown hair lightened at the ends from sun and salt, salt-tousled or in a loose undone braid,
[SCENE], wearing [OUTFIT — bikini as daily basewear, natural beach-appropriate color coordination, not
overly styled or fashion-shoot posed], [MINIMAL ACCESSORY — a simple watch, sunglasses pushed up into
her hair, or a thin anklet; never more than one], [DYNAMIC CANDID POSE/ANGLE — walking, paddling,
mid-laugh, teaching, caught mid-motion, NOT a static posed beach-model stance],
[NATURAL FLATTERING LIGHT — golden hour dawn patrol, bright midday sun, or sunset backlight; shallow
depth of field with soft blurred bokeh background],
high dynamic range, crisp sharp focus on subject, high natural contrast, slightly overexposed highlights,
natural color grading — NOT degraded, grainy, or dim, true-to-life unretouched skin texture,
candid outdoor lifestyle photo, shot on iPhone or action camera with crisp high-quality output, Instagram style
```

**風格關鍵詞備註**：
- 一定要保留 `true-to-life unretouched skin texture`、`visible skin pores`——這是 Zoe 美學的核心（毛孔、自然瑕疵等「質感真實」），跟其他角色的「精緻磨皮感」相反；**但「visible tan lines」與任何實際曬黑的膚色描述已於 2026-07-25 移除**——質感真實（毛孔、非磨皮）跟膚色深淺是兩件事，Zoe 的膚色設定改為白皙，只有質感維持不磨皮
- **三圍數字（88cm bust／D cup、59cm waist、90cm hips，見 `profile.json` 的 `measurements`）已直接寫進核心 prompt 本體**，不再只靠「naturally curvy」這種模糊形容詞帶過
- **光線預設為新版「討喜自然光」配方**：黃金時段晨光（dawn patrol）、正午亮光、日落逆光，均搭配淺景深背景虛化 + crisp high dynamic range；只有極少數室內公寓/小貨車場景（見下方批次規劃 2）可以保留舊版「混合不均勻」配方，其餘場景一律不得使用「uneven/degraded/dim/muddy」這類把畫質往下拉的字——真實感來自皮膚質感、生活雜物與鏡頭裝置破綻，不是靠調暗調糊
- 禁止出現裸露或性暗示相關詞彙；服裝上限是比基尼/泳裝，符合海灘網紅帳號的主流尺度；配件維持極簡（手錶、推上頭頂的墨鏡、細腳鍊，符合她低維護的人設，不要堆疊配件變成刻意造型）
- 姿勢預設為動態抓拍（走路、划水、教學互動中的笑場），避免靜態擺拍的「網紅拍照姿勢」感
- **每個 prompt 均須落實 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五項checklist**（2026-07-24 新增，2026-07-25 光源項修正，2026-07-25 膚色基調項修正）：具體皮膚質感關鍵字（毛孔、非磨皮、自然瑕疵——不含曬痕，膚色基調需為白皙）、逐場景明確的裝置/鏡頭破綻（前鏡頭自拍 vs. 後鏡頭 vs. 運動相機、對焦軟化、高光爆掉、鏡頭上的水珠、動態模糊、壓縮痕跡）、對應場景類型的正確光源配方（戶外用討喜自然光+淺景深，室內例外場景才用混合不均勻）、具體生活雜物背景（沙子、蠟塊、隨手丟的毛巾、板具、防曬乳）、完整明確的服裝描述、三圍數字是否直接寫入而非模糊帶過

**⚠️ 2026-07-25 燈光/身材數字校準**：使用者在 Vicky Lin 身上驗證過「真實感 ≠ 畫質差」之後，回頭檢查 Zoe 的草稿發現同樣的舊思路殘留：(1) 核心 prompt 只寫「naturally curvy hips」等模糊詞，沒有把 `profile.json` 裡已經確認的三圍數字（88-59-90cm，D 罩杯）寫進去；(2) 部分批次沿用「uneven light falloff」「film grain」「compression banding」把整體畫面往「做舊/偏暗」的方向拉，即使場景本身是黃金時段海邊或正午豔陽這種本來就該明亮清晰的光線；(3) 身材描述裡的「lean defined core」用詞有跟 Vicky 第一輪犯的「健美選手」錯誤同樣的風險，需要比照 `profile.json` 已修正版本明確排除「blocky / vascular / heavily muscled」。這次校準：三圍數字直接寫入核心 prompt 與全部 6 個批次；除了批次規劃 2（室內小房間鏡前）保留原本的室內混合光源配方外，其餘 5 個批次全部改用「黃金時段/正午豔陽/日落逆光 + 淺景深虛化 + crisp high dynamic range」的新配方，並在每個 prompt 明講 `NOT degraded, grainy, or dim`；臉部與身材描述統一比照 `profile.json` 已修正的「gorgeous beach-influencer, NOT athlete/masculine」語言，移除「lean defined core」之類有風險的字眼。`character.md`／`profile.json` 的外型描述本身不變動，只是把已經確認的設定確實寫進實際會送出生成的 prompt 字串裡。

---

## 計畫批次 Prompt 規劃

> 以下為**計畫中**的訓練圖批次，尚未執行生成。實際執行後應在此文件補上：使用的平台/模型、實際生成張數、選用結果、圖片路徑。目前僅記錄場景規劃與草稿 prompt。

### 批次規劃 1 — 晨間衝浪，日出前走向海邊（計畫 2 張）

**場景描述**：天還沒亮，Zoe 走向花蓮海邊，板夾在腋下，天色剛開始從深藍轉紫，第一道光還沒出現。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, strikingly beautiful, warm, radiant oval face with a gorgeous wide smile,
fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored),
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, fair, porcelain-toned skin that stays fair despite her beach lifestyle, only the faintest natural warmth from time outdoors, NOT deeply tanned or bronzed, long beachy wave dark brown hair in a loose undone braid,
visible skin pores, subtle natural skin texture, slight oil sheen on T-zone,
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
26-year-old Taiwanese woman, strikingly beautiful, warm, radiant oval face with a gorgeous wide smile,
fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored),
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, fair, porcelain-toned skin that stays fair despite her beach lifestyle, only the faintest natural warmth from time outdoors, NOT deeply tanned or bronzed, long beachy wave dark brown hair salt-tousled and loose,
visible skin pores, subtle natural skin texture,
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
26-year-old Taiwanese woman, strikingly beautiful, warm, radiant oval face with a gorgeous wide smile,
fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored),
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, fair, porcelain-toned skin that stays fair despite her beach lifestyle, only the faintest natural warmth from time outdoors, NOT deeply tanned or bronzed, wet long beachy wave dark brown hair slicked back from rinsing,
visible skin pores on wet skin, subtle natural skin texture,
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
26-year-old Taiwanese woman, strikingly beautiful, warm, radiant oval face with a gorgeous wide smile,
fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored),
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, fair, porcelain-toned skin that stays fair despite her beach lifestyle, only the faintest natural warmth from time outdoors, NOT deeply tanned or bronzed, long beachy wave dark brown hair down and windblown,
visible skin pores, subtle natural skin texture, slight oil
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
26-year-old Taiwanese woman, strikingly beautiful, warm, radiant oval face with a gorgeous wide smile,
fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored),
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, fair, porcelain-toned skin that stays fair despite her beach lifestyle, only the faintest natural warmth from time outdoors, NOT deeply tanned or bronzed, long beachy wave dark brown hair loose and slightly damp from the day's heat,
visible skin pores, subtle natural skin texture, slight
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
26-year-old Taiwanese woman, strikingly beautiful, warm, radiant oval face with a gorgeous wide smile,
fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored),
gorgeous beach-influencer good looks (NOT a stern or masculine look), straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with soft feminine curves, toned shoulders and upper back from paddling
(never blocky or heavily muscled), 88cm bust (D cup, full and naturally curvy), 59cm waist (lean with
only a subtle soft hint of core tone), 90cm hips (naturally curvy, shapely thighs), strong but shapely
legs, fair, porcelain-toned skin that stays fair despite her beach lifestyle, only the faintest natural warmth from time outdoors, NOT deeply tanned or bronzed, long beachy wave dark brown hair pulled back loosely,
visible skin pores, subtle natural skin texture showing muscle definition without excess gloss,
slight sweat sheen on shoulders and lower back, unretouched skin detail,
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

## 2026-07-25 發現批次（Discovery Batch）— 已生成，等待使用者挑選喜歡的臉/風格

**狀態：⚠️ 僅供臉孔/風格挑選 —— 未執行 Soul 訓練，未建立 Reference Element，`profile.json` 沒有 soul_id。這 4 張圖是各自獨立生成，彼此不共享同一身分，不能直接當作訓練圖使用。**

**目的**：依照 Vicky Lin 案例確立的兩階段流程——先產出一小批獨立生成的候選圖讓使用者挑出喜歡的臉/風格，使用者核准某一張後，才把那張圖做成 Reference Element 錨定身分，再展開完整訓練圖批次。本輪即為 Zoe 的第一階段「發現批次」。

**模型選擇**：呼叫 `models_explore(action='recommend')` 確認適合「無 soul_id 情況下生成一致角色參考圖」的模型後，選用 `soul_2`（Higgsfield Soul 2.0，無 soul_id，作為一次性角色參考圖生成，與 Vicky Lin 第二輪的選擇一致），`aspect_ratio: 9:16`，`quality: 2k`。`get_cost:true` 預估每張 1 credit（0.12 credits_exact）。

**Prompt 內容**：4 張圖皆使用本文件「核心 Prompt 結構」的完整外型描述本體（26 歲台灣女性、曬過的橢圓臉、直眉、雀斑、瞇眼、游泳選手/衝浪者體態、88cm 胸/D罩杯/59cm 腰/90cm 臀、深色海浪捲長髮），一字不改地在 4 張圖之間保持一致，僅變化場景中的角度/景別/光線/服裝細節，符合 `SEXY_SCENE_LIBRARY.md` 五項降低「AI 感」技術要點（皮膚質感關鍵字、裝置/鏡頭具體破綻、對應場景類型的光源配方、生活雜物背景、完整服裝描述）。

**費用**：`get_cost` 預估每張 1 credit（0.12 credits_exact）；`transactions` 紀錄確認 4 筆本批次生成各扣款 0.12 credits，本批次可歸因花費共 **0.48 credits**（4 張 × 0.12）。⚠️ 生成期間帳戶餘額由 18.23 credits 降至 15.83 credits（共降 2.4 credits），但 `transactions` 顯示同一時間窗口內共有 20 筆「Higgsfield Soul V2」扣款紀錄（本批次僅為其中 4 筆）——判斷帳戶內同時有其他工作階段/角色的生成在跑（提交時也確實遇到過 3 次 `Rate limit reached: max 8 concurrent job(s)` 錯誤，證實當下有其他並發工作），因此 2.4 credits 的整體餘額變動**不能全部歸因於本批次**，僅本批次 4 筆交易、共 0.48 credits 是可確認歸屬 Zoe 這次發現批次的花費。

**產出檔案**（`kols/zoe-lai/images/face_reference/`）：

| 檔名 | 角度/景別 | 場景重點 | Job ID |
|------|-----------|----------|--------|
| candidate_01.png | 正面臉部特寫（headshot） | 花蓮海邊，晨光 dawn patrol，黑色比基尼上衣，墨鏡推上頭髮 | `bd84b5a1-bbc7-448a-9a77-5aa3298b9f87` |
| candidate_02.png | 正面半身（half-body） | 花蓮海邊，黃金時段，黑色比基尼＋寬大男裝襯衫，板具在旁 | `5507b251-a4e6-4910-8a0c-89e5190d32ae` |
| candidate_03.png | 四分之三側半身（3/4 half-body） | 花蓮海邊，正午豔陽，回頭一笑，黑色比基尼＋寬大男裝襯衫 | `2d781876-fbe1-44da-afdc-481407cd1a85` |
| candidate_04.png | 正面全身（full-body） | 墾丁海邊，日落黃金時段，黑色比基尼＋牛仔短褲，板具立在沙裡 | `4d73b98e-90dd-4a5e-8db2-1860f1b354d4` |

**生成後目視檢查**（已用 Read 工具逐張開啟檢視全部 4 張）：4 張皆呈現曬過的健康小麥膚色、雀斑、自然膚質（非磨皮），整體風格與亮度符合「討喜自然光」配方（明亮清晰，非做舊/偏暗）。同時記錄兩個需要使用者留意的觀察點，供挑選時參考，不預先下判斷：
- **身形觀察**：candidate_03、candidate_04 兩張的腰腹線條讀起來偏纖細/緊實，跟 profile.json 設定的 88-59-90cm（D罩杯，豐滿上圍）相比，視覺上豐滿度不如預期明顯，candidate_04 甚至可見到輕微肋骨輪廓——這跟 Vicky Lin 第二輪犯過的「身材與三圍數字對不上」問題屬同一類型風險，需要使用者看圖後確認是否要在下一階段的 prompt 中進一步強化胸型/曲線描述。
- **裝置介面破綻**：candidate_04 生成結果意外把「Instagram style」關鍵字讀成了實際的 Instagram 限時動態介面截圖（畫面上緣出現使用者頭像、帳號名稱「Hualiuen」、觀看數「20」、進度條與關閉按鈕），這是不需要的 UI 疊加物，並非單純的「手機直出質感」，若使用者选中這張風格但介意此瑕疵，下一階段錨定生成時需要調整 prompt 避免再次觸發真實 App 介面渲染。

4 張圖彼此為**獨立生成、不共享同一身分**——這是設計上的預期行為（發現批次的目的就是每張各自嘗試，讓使用者比較臉孔/風格差異），不是錯誤。

**⚠️ 下一步（不可跳過）**：**必須停下來，等使用者實際看過這 4 張候選圖並明確指出最喜歡哪一張臉/風格之後**，才可以：(1) 把使用者選定的那一張圖上傳建立 Reference Element；(2) 用該 element_id 錨定生成完整訓練圖批次。本輪**未**呼叫 `show_characters(action='train')`，也未建立任何 Reference Element，`profile.json` 沒有新增 soul_id 或任何 `ai_generation` 欄位，維持原狀未變更。

**⚠️ 這一批（candidate_01–04）檔案已於 2026-07-25 第二次修正時改名為 `round1_candidate_01.png`–`round1_candidate_04.png`（見下方章節），原因是這批圖的膚色（曬過的健康小麥膚色）已被判定為錯誤設計，保留檔案但不再是目前使用中的候選圖。**

---

## 2026-07-25 四次修正：膚色由深色曬黑徹底改為白皙基調，改用 Seedream 4.5 重新生成

### 背景與推翻的設計決策

使用者直接指示：Zoe 原本的「Deep, even, year-round sun tan」「小麥膚色」人設是**錯誤的設計選擇，必須整個推翻**，改為主流台灣審美偏好的「白幼瘦」（白皙、精緻五官、纖細身形）路線——**即使 Zoe 是海島/衝浪系人設，膚色基調也不能是「健康古銅曬黑」，而應該是「認真防曬、維持白皙」**。這不是單一角色的個案調整，而是與此同時新增的**全公司永久規則**：

- `README.md`「新增 KOL 流程」步驟 5：新增膚色基調審核提醒
- `SEXY_SCENE_LIBRARY.md` 降低「AI 感」checklist 第 6 項「膚色基調」：明確要求主流台灣審美的白皙路線，而非「healthy tan」

問題最早浮現於 Zoe 的「發現批次」（見上方章節）：4 張圖用的是 `soul_2`（無 soul_id，每次獨立重新想像臉孔），使用者反饋除了 4 張臉孔本身不一致之外，還直接指出「膚色都太黑了」——這暴露了 Zoe 人設草稿裡「曬黑」被誤當成她的美學核心的問題。經釐清：**皮膚「質感」的真實感（毛孔、非磨皮、自然瑕疵）跟皮膚「顏色」的深淺是兩件完全獨立的事**——前者應該保留（這才是原本 `generation_notes.md` 論證「不修飾膚況」的真正用意），後者則是設計錯誤，必須改為白皙。

### 已完成的文件修正

1. **`profile.json`**
   - `identity.appearance.figure`：`"Deep, even, year-round sun tan."` → 改為白皙但仍認真防曬維持的描述（"Fair, porcelain-toned skin that stays fair despite her beach lifestyle...NOT deeply tanned or bronzed..."），其餘身材描述不變
   - `identity.appearance.face_type`：`"sun-warmed oval face"` → `"warm, radiant oval face"`，並新增白皙皮膚描述（"fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored)"），燦爛笑容/雀斑/直眉/不陽剛的語言維持不變
   - 註：`content.aesthetic`（`color_palette` 內的 `"deep tan skin tones"`、`mood` 文字裡的「皮膚是曬過的顏色」）、`persona.archetype` 裡的 "her body and tan"、`social.community_name`（"曬黑的我們"）**本輪未修改**——這些屬於品牌敘事/社群命名層級的措辭，不在本次交辦的明確修改範圍內，但同樣包含「曬黑」語言，與新規則有衝突，建議使用者確認是否也要一併調整
2. **`character.md`**：五處修正——開場「誰是 Zoe」段落移除「曬到黑」、外型表格「曬得均勻的健康小麥膚色」改為白皙描述、內容哲學「不修飾的膚況」移除「曬痕」改為「毛孔」、視覺美學「色調」段落「膚色和曬痕」改為「白皙膚色與自然膚質」、結尾「她的帳號是什麼」段落「傍晚曬得更黑一點」改為「認真防曬讓肌膚維持白皙」
3. **`generation_notes.md`**（本檔案，也是實際送進生成模型的 prompt 字串本體）：
   - 人物設定表格「臉型」「身材」兩列移除小麥膚色/深色年曬描述，改為白皙
   - 核心 Prompt 結構本體：`sun-warmed oval face` → `warm, radiant oval face` + 新增白皙描述句；`deep even golden tan` → 白皙描述句（全文出現 7 次，含核心 prompt + 全部 6 個批次規劃，已用 replace_all 一次性修正）；`true-to-life unretouched skin texture with visible tan lines` → 移除 `visible tan lines`，只保留質感真實的 `unretouched skin texture`（出現 2 次）
   - 6 個批次規劃 prompt 逐一移除各自的 `faint tan line(s) at...` 片語（批次 1–6 各一處）
   - 風格關鍵詞備註：移除「一定要保留...`visible tan lines`」的錯誤論證，改為明講「質感真實 ≠ 膚色深淺」，膚色改白皙、質感仍不磨皮
   - checklist 條目備註同步更新，加註「2026-07-25 膚色基調項修正」

### 模型切換：soul_2 → Seedream 4.5

依照 `kols/iris-chen/generation_notes.md` 記錄的唯一已驗證成功模板：Iris Chen（以及原始 6 位 KOL）的參考圖都是用 `seedream_v4_5`（Seedream 4.5）生成，該模型在同一文字 prompt 下重複生成時臉孔一致性極高（高到「4 張會太像，所以只生 2 張」的程度）。這與 `soul_2`（無 soul_id 時每次獨立重新想像臉孔，這正是 Zoe 發現批次 4 張臉孔彼此不一致的原因）形成直接對比。本輪呼叫 `models_explore(action='get', model_id='seedream_v4_5')` 確認模型可用：4K 輸出（`quality: basic` 上限 4K，`high` 上限約 6K），支援 `9:16` 等多種長寬比。本輪 Round 2 改用 `seedream_v4_5` 取代 `soul_2`。

### Round 1 檔案改名（保留不刪除）

`git mv` 將原本的 `candidate_01.png`–`candidate_04.png`（`soul_2` 生成、膚色過黑、彼此臉孔不一致的批次）改名為 `round1_candidate_01.png`–`round1_candidate_04.png`，保留在 `kols/zoe-lai/images/face_reference/` 中作為錯誤示範存查，**未刪除**。

### ⚠️ Round 2 生成結果（2026-07-30 帳戶儲值後補跑）：圖已生成，但膚色修正**未達預期**——誠實記錄失敗

**背景**：Round 2 的 4 個 prompt 因額度不足延遲到 2026-07-30 執行（使用者告知帳戶已重新儲值，`balance` 確認 2976.5 credits）。沿用原規劃的 4 組場景/角度（晨光大頭照 / 黃金時段半身 / 正午 3/4 半身 / 日落全身），核心外型描述已包含白皙膚色修正句與 `candid phone-photo aesthetic`（避免重現 Instagram UI 介面問題）。

| 檔名 | 場景 | Job ID | 狀態 |
|------|------|--------|------|
| candidate_01.png | 晨光大頭照，日出前海邊 | `f1d6a44e-9d32-49c5-82f6-15959b6c6f97` | ✅ 生成完成 |
| candidate_02.png | 黃金時段半身，白襯衫外搭比基尼 | `9fbae21b-ea13-464f-bcc5-eb54e9cc9ace` | ✅ 生成完成 |
| candidate_03.png | 正午 3/4 半身，回頭看鏡頭 | `fde51e6b-4e2a-4142-9b81-fdad7b065f25` | ✅ 生成完成 |
| candidate_04.png | 日落全身，比基尼＋牛仔短褲 | `e60b3bb7-c3af-4305-8eae-4c4a1cd2a1eb` | ✅ 生成完成 |

四張皆一次生成成功，`get_cost` 預估與實際扣款相符（每張 1 credit）。

**誠實目視評估（用 Read 工具逐張實際檢查，非預設假設）**：

- **臉型一致性 — ✅ 良好**：四張圖是同一張臉——相同臉型輪廓、笑容、雀斑分布、髮辮綁法，與 Rainie Hsu、Coco Wu 等其他角色的 Seedream 4.5 結果一致，證實模型在無 soul_id 情況下同 prompt 重複生成確實能維持臉型一致。
- **膚色 — ❌ 修正失敗，仍是古銅曬黑色調，不是白皙**：儘管核心 prompt 已明確寫入兩次「fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored)」與「porcelain-toned skin that stays fair despite her beach lifestyle...NOT deeply tanned or bronzed」，**四張圖實際呈現的膚色仍然是明顯的健康古銅/小麥曬黑色調**，跟 Round 1（`soul_2`）被使用者否決的膚色深淺程度相去不遠，跟 Rainie Hsu／Coco Wu 等角色在室內棚拍場景下明顯轉為白皙的效果形成強烈對比。推測原因（非確定，僅為觀察）：「海邊」「衝浪」「dawn patrol」「years facing open water」這類場景/人設敘述本身在生成模型的訓練分布裡與古銅膚色高度綁定，文字層級的膚色否定指令（"NOT tanned"）在強戶外情境下的實際壓制力不如室內棚拍場景——這與 Rainie／Coco 的室內棚拍/宿舍場景形成的對照，暗示「場景强度」可能會蓋過單純的膚色形容詞修正。
- **次要問題 — ⚠️ 腹肌線條偏明顯**：candidate_01、candidate_04 可見清晰的六塊腹肌輪廓，跟 `profile.json` 已修正版「lean waist with only a subtle soft hint of core tone (never blocky or heavily muscled)」的設定有落差，跟 Vicky Lin 第一輪「健美選手」問題屬同一類風險，尚未完全排除。

**結論：本輪未能解決使用者最初反饋的「膚色都太黑了」問題。** 不可視為修正完成，也不建議直接進入 Reference Element 錨定階段——需要使用者看過這 4 張後決定下一步（例如：是否接受這個「海島曬痕」介於健康與古銅之間的程度、或需要更激進的 prompt 干預如移除海邊/衝浪場景詞彙做純棚拍臉部測試、或改用其他模型/negative prompt 機制）。

### 下一步

1. **待使用者看過本輪 4 張圖後決定**：(a) 接受目前膚色程度、(b) 要求再次嘗試更強力的膚色修正（例如拿掉場景敘述做室內棚拍純測試，或明確要求「立可白／室內辦公室膚色」等更極端錨點）、或 (c) 重新考慮 Zoe 的人設方向是否要保留海邊/衝浪強敘事。
2. 在使用者明確回覆之前，**不建立 Reference Element、不呼叫 `show_characters(action='train')`**，`profile.json` 沒有新增 soul_id 或 `ai_generation` 欄位。

---

## 下一步（待執行）

1. **【本輪已完成的前置步驟】** 已生成 4 張發現批次候選圖（見上方章節），等待使用者從中選出喜歡的臉孔/風格
2. 使用者選定後，將該張圖上傳並建立 Reference Element，取得 element_id
3. 用該 element_id 錨定，依上述 6 個批次規劃重新生成完整訓練圖（每張 prompt 內嵌 element_id 而非僅靠文字描述），確保同一身分
4. 訓練圖確認後，執行 Soul 訓練流程
5. 訓練完成後，才開始规划後續生活照與影片批次（本文件屆時需新增「已生成」章節，並記錄實際 soul_id、Job ID、圖片路徑）

**目前無**：soul_id、Reference Element、完整訓練圖批次、已生成影片數量。以上欄位皆待實際執行後填入，禁止在此階段預先填寫。
