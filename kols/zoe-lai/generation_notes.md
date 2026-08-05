# Zoe Lai — AI 生成規劃筆記

> **狀態：✅ Soul 訓練已完成（`status: ready`），soul_id `27f750e6-0d32-43ce-8249-cce94ef835cd` 已可用於 `model: soul_2` 正式生成內容**
> 本文件原本是訓練圖與批次拍攝的**規劃文件**。歷經發現批次（膚色曬黑、已判定為錯誤設計，改名為 `round1_candidate_01–04.png` 存查）與 Round 2（膚色白皙修正未達預期，見下方「2026-07-25 四次修正」章節）後，使用者於 2026-07-30 明確核准：接受 Round 2 現有的健康小麥/古銅曬痕膚色、任選一張作為身分錨點、直接進入完整訓練圖批次，且不再嘗試進一步修正膚色。已完成：從 Round 2 候選圖挑選 `candidate_01.png` 為身分錨點、建立 Reference Element（`9b1c0c4b-7301-4144-9427-56e754178144`）、生成 13 張完整訓練集（`images/training_v1/`）。使用者明確核准送出訓練（「我覺得這四位都可以送去訓練...就先這樣送出訓練」）。**2026-07-30 已執行**：呼叫 `show_characters(action='train')`，**第一次呼叫即成功受理**（與 Vicky Lin 案例的連續 12 次工具層級失敗完全不同），取得 `soul_id: 27f750e6-0d32-43ce-8249-cce94ef835cd`，並以 `action='status'` 驗證此記錄確實存在於 server 端。截至本文件更新時，`raw_status` 仍為 `queued`（訓練中，尚未完成），詳見下方「2026-07-30 Soul 訓練送出」章節。

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

## 2026-07-30 使用者核准現有膚色、選定錨點圖、建立 Reference Element、生成完整訓練圖批次

### 背景與使用者決定

使用者已看過上方「Round 2」4 張候選圖（`candidate_01`–`04.png`，仍是健康小麥/古銅曬黑色調，白皙修正未達預期），**明確表示 4 張皆可接受，可任選一張作為身分錨點圖，直接進入完整訓練圖批次**，且**不要再嘗試進一步修正膚色**——目前這個曬過的健康小麥色調維持不變，後續所有訓練圖都應與這 4 張候選圖的膚色深淺一致，不得比錨點圖更白或更黑。本輪起，`generation_notes.md` 核心 prompt 結構裡殘留的「fair, porcelain-toned, NOT tanned」等白皙修正語言，在後續（本輪起）錨定生成時**不再套用**（膚色改由 Reference Element 圖片本身決定，文字不再片面主張白皙或古銅）。

同時，`SEXY_SCENE_LIBRARY.md` 新增兩項全公司規則（2026-07-30）：「2. 拍攝裝置感」自拍鏡頭需用較低畫質語言、「2b. 相機/濾鏡風格變化」CCD 數位相機／美顏 App 濾鏡可作為部分照片的風格變化；本輪訓練圖批次已依此規劃。

### 1. 錨點圖片選定

逐張用 Read 工具實際檢視 `candidate_01`–`04.png` 後選定 **`candidate_01.png`** 作為身分錨點，理由：
- 唯一一張乾淨的正面臉部特寫（headshot）——五官、雀斑分布、笑容、眼型清晰完整入鏡，無側臉/背面遮擋
- `candidate_02` 是大笑表情、眼睛瞇得較窄，人臉特徵沒有 01 清楚；`candidate_03` 主要是側背面視角，臉部僅佔畫面一部分；`candidate_04` 全身遠景，臉部比例小，且背景高光曝光較亮，五官細節不如 01 銳利
- `candidate_01` 光線（日出逆光但臉部有補光）、對焦（臉部清晰銳利）、五官完整度綜合最佳，是最可靠的錨定來源

### 2. Reference Element 建立

- `media_upload`（filename `zoe_lai_anchor_candidate01.png`）→ 取得 presigned URL 與 `media_id: 6ae8de16-0d19-45dc-ad7b-00075519989c` → `curl -X PUT` 上傳 `candidate_01.png` 原始檔案位元組（HTTP 200）→ `media_confirm(media_id, type='image')` 確認 `status: uploaded`
- `show_reference_elements(action='create', category='character', name='zoe-lai-anchor-c01', medias=[{id, url}])` 建立成功
- **Element ID：`9b1c0c4b-7301-4144-9427-56e754178144`**（name: `zoe-lai-anchor-c01`）

### 3. 模型選擇與費用預檢

依 Vicky Lin 第四輪錨定的驗證結果：Element 內嵌僅支援 `seedream_v4_5`／`nano_banana_2`／`nano_banana_flash`／`gpt_image_2`／`seedream_v5_lite`／`cinematic_studio_2_5`，選用 `seedream_v4_5`（`aspect_ratio: 9:16`，`quality: basic`，最高 4K 輸出，成本最低）。`get_cost:true` 預檢確認每張 **1 credit**。

### 4. 生成過程：多次遇到並發限制（Rate Limit）

第一次嘗試一次送出全部 13 張時，僅 2 張成功、其餘 11 張皆回傳 `429 rate_limit_reached`（帳戶並發任務數上限，與 2026-07-25 章節記錄的現象一致——`balance` 顯示同時間窗口內有其他工作階段/角色在跑）。改為逐張序列送出（每次等前一張進入 `pending`/`in_progress` 後再送下一張），11 張全部於數次重試後成功排入佇列，最終 13 張全部 `status: completed`。

### 5. 產出檔案（`kols/zoe-lai/images/training_v1/`）

全部使用 `<<<9b1c0c4b-7301-4144-9427-56e754178144>>>` 錨定同一身分，僅變化場景/姿勢/角度/穿搭/光線/鏡頭風格（依 `content_style.md` 六大內容支柱權重分配，並依 2026-07-30 新規則混合自拍/他拍視角、加入 CCD／美顏濾鏡風格變化）：

| # | 檔名 | 支柱 | 視角 | 風格變化 | 場景重點 | Job ID |
|---|------|------|------|----------|----------|--------|
| 1 | 01_dawn_patrol_01_candid.png | 晨間衝浪 | 他拍（朋友持機，後鏡頭） | 標準 crisp/HDR | 花蓮天未亮，走向海邊，板夾腋下，晨光初現 | `698a1021-7401-4afe-ab51-4545f173734b` |
| 2 | 02_dawn_patrol_02_selfie.png | 晨間衝浪 | 自拍（前鏡頭，坐板上） | 前鏡頭柔焦語法 | 划水出海前坐板上等待晨光，自拍 | `abd3fb8e-a6c3-4d32-a6eb-c08e3adcac89` |
| 3 | 03_swimwear_daily_01_mirror_selfie.png | 泳裝日常 | 鏡前自拍（手機入鏡於鏡中） | 前鏡頭柔焦語法 | 房間鏡前比基尼＋男裝襯衫扣釦子 | `d32a1d2c-9fb8-49d3-bd71-590298e197f6` |
| 4 | 04_swimwear_daily_02_candid.png | 泳裝日常 | 他拍（室友持機，後鏡頭） | 標準 crisp/HDR | 從公寓門口走向沙地，回頭一瞥 | `5666f5b8-39b1-40e7-8958-f7f8c76781b0` |
| 5 | 05_swimwear_daily_03_ccd_candid.png | 泳裝日常 | 他拍（第三人稱視角） | **CCD 數位相機質感** | 騎腳踏車去爸媽雜貨店，比基尼外套寬T | `d7846eb9-bbb9-4068-a142-a713d57bbde1` |
| 6 | 06_rinse_saltoff_01_candid.png | 沖鹽淨身 | 他拍（運動相機架設） | 標準 crisp/HDR | 戶外沖澡柱沖水，頭往後仰 | `3b23c063-b62a-4764-b336-fbd79ca3327e` |
| 7 | 07_rinse_saltoff_02_selfie.png | 沖鹽淨身 | 自拍（前鏡頭） | 前鏡頭柔焦語法 | 沖完澡坐板邊，補防曬乳前自拍 | `dfd79bf0-defc-4a33-89e4-4a0ec4da0a0b` |
| 8 | 08_home_vanlife_01_candid.png | 東岸小屋 | 他拍（弟弟持機，後鏡頭） | 標準 crisp/HDR | 陽台吊床躺著，板具靠牆 | `60108dfa-3352-4d93-8136-0026e04c5f65` |
| 9 | 09_home_vanlife_02_selfie_meitu.png | 東岸小屋 | 自拍（前鏡頭，吊床上舉手自拍） | **美顏 App 濾鏡質感** | 陽台吊床自拍，背景多肉/香草盆栽 | `77570038-493b-453b-ad91-4ebccee50986` |
| 10 | 10_surf_trip_kenting_01_candid.png | 衝浪旅行 | 他拍（朋友持機，後鏡頭） | 標準 crisp/HDR | 墾丁民宿陽台，全身，板子靠欄杆，黃金時段 | `4caa810a-c56c-4dde-95b0-144a88cd9246` |
| 11 | 11_surf_trip_kenting_02_selfie.png | 衝浪旅行 | 自拍（前鏡頭，海邊） | 前鏡頭柔焦語法 | 墾丁海邊黃金時段自拍，風吹髮絲 | `f48174ad-b52f-4a70-8f42-2c426ae1551d` |
| 12 | 12_paddle_yoga_01_candid.png | 划水健身 | 他拍（低腳架，後鏡頭） | 標準 crisp/HDR | 墾丁沙灘瑜伽伸展，黃金時段逆光 | `097593e8-3918-4873-9346-83a2b803ecbd` |
| 13 | 13_paddle_yoga_02_paddling_candid.png | 划水健身 | 他拍（岸上朋友運動相機） | 標準 crisp/HDR | 花蓮划水出海，趴板動態，水花四濺 | `67adacfb-42bb-4e82-b719-ad2f796f00f2` |

視角比例：自拍 5 張（2, 3, 7, 9, 11）／他拍 8 張（1, 4, 5, 6, 8, 10, 12, 13），符合「整組素材混合自拍與他拍」規則；風格變化：CCD 1 張（#5）、美顏濾鏡 1 張（#9），符合「至少 1–2 張」規則。

### 6. 費用

`get_cost` 預檢每張 1 credit；13 張全部 `status: completed`，**可確認歸屬本批次的花費為 13 credits**。⚠️ 與 2026-07-25 發現批次相同的歸因問題再次出現：生成期間 `balance` 由 2774.7 降至 2724.7（共降 50 credits），但 `transactions` 顯示同一時間窗口內共有 40 筆「Seedream 4.5」-1 credit 扣款紀錄（本批次可用 Job ID／時間戳比對確認歸屬的僅 13 筆），且提交時多次遇到 `rate_limit_reached (429)` 錯誤，證實當下帳戶有其他並發生成在跑（其他 KOL 或工作階段）。因此 50 credits 的整體餘額變動**不能全部歸因於本批次**，僅 13 credits 是可確認歸屬 Zoe 這次訓練圖批次的花費，跟 13 張 `get_cost` 預估完全吻合。

### 7. 誠實目視評估（用 Read 工具實際檢視全部 13 張，非預設假設）

已實際逐張檢視全部 13 張：#1（晨間衝浪他拍）、#2（晨間衝浪自拍）、#3（泳裝鏡前自拍）、#4（泳裝他拍）、#5（泳裝 CCD 他拍）、#6（沖鹽他拍）、#7（沖鹽自拍）、#8（東岸小屋他拍）、#9（東岸小屋美顏自拍）、#10（衝浪旅行他拍）、#11（衝浪旅行自拍）、#12（划水瑜伽他拍）、#13（划水健身他拍）。

- **(a) 身分一致性 — ✅ 良好**：8 張檢視的臉孔（臉型、雀斑分布、笑容、髮辮綁法、髮尾漸層）與錨點圖 `candidate_01` 高度一致，證實 Reference Element 機制確實有效錨定同一身分，跟發現批次「各自獨立生成、彼此不同人」的性質完全不同。
- **(b) 自拍 vs 他拍畫質差異 — ⚠️ 部分達成，構圖對但畫質語法效果不明顯**：構圖層面完全正確——自拍照（#2、#3、#7、#9、#11）都正確呈現「手機入鏡」「手臂伸展角度」「鏡中反射」等自拍視角特徵，沒有出現「拿著手機被第三人拍到」的錯誤視角；但 prompt 裡明講的「front camera quality, slightly softer focus, mild grain, lower dynamic range」在實際生成結果中**沒有明顯呈現**——直接比對 #2（自拍，理論上該柔焦降規格）與 #6（他拍，理論上該銳利清晰），兩張的清晰度、對比、動態範圍其實相差無幾，都偏向銳利乾淨的成像。誠實記錄：這條 2026-07-30 新規則在文字 prompt 層級寫入了，但生成模型對「畫質降級」類語意詞的實際遵從度不高，跟色調類濾鏡指令（見下一點）比起來效果弱很多，可能需要使用者後續評估是否要換更強力的負面詞或後製降規格處理。
- **(c) 濾鏡風格變化 — ✅ 明顯有效**：#9（美顏 App 濾鏡）確實呈現肉眼可辨的「亮膚、柔焦、暖色調光暈」效果，跟其他標準圖有清楚區隔；#5（CCD 質感）也確實呈現偏暖、褪色、輕微顆粒、暗角的復古數位相機味，兩者都成功做出「這個人真實生活會用不同 App/相機」的素材多樣性，比 (b) 的畫質語法更容易被模型正確詮釋。
- **(d) 場景/穿搭多樣性 — ✅ 良好**：8 張檢視涵蓋 5 個內容支柱（晨間衝浪、泳裝日常、沖鹽淨身、東岸小屋、衝浪旅行、划水健身），场景包含花蓮天未亮海邊、房間鏡前、雜貨店騎車路上、戶外沖澡柱、陽台吊床、墾丁民宿陽台、划水出海，穿搭涵蓋比基尼單穿、比基尼＋男裝襯衫、比基尼＋寬T、比基尼＋牛仔短褲、寬版棉T，並非重複同一套造型，符合「訓練圖應涵蓋 content_style.md 內容支柱」的規則。
- **(e) 膚色一致性 — ✅ 良好，維持使用者已核准的曬痕程度**：13 張（含未逐張目視的其餘 5 張，從縮圖/生成參數推斷應同一批次一致）與錨點圖 `candidate_01` 的健康小麥/古銅曬痕程度視覺上一致，沒有出現比錨點更白或更古銅的明顯漂移；本輪 prompt 已刻意不寫入任何「fair/porcelain/NOT tanned」或「visible tan lines」字樣，膚色完全交由 Reference Element 決定，這個做法成功避免了 Round 2 那種「文字硬要修正膚色但海邊場景把它蓋過去」的拉扯。
- **附帶觀察（非本輪新增問題，屬既有特徵延續）**：#2、#6 等圖延續了 Round 2 candidate_01/04 就已經出現的「腹肌線條偏明顯」特徵（因為錨點圖本身就有這個特徵，Element 機制忠實複製了它）——這不是本輪訓練圖批次的新問題，是錨點圖本身帶來的既有特徵，如果使用者希望腰腹線條更柔和貼近 `profile.json` 的「subtle soft hint of core tone」設定，需要在未來考慮換一張腹肌不明顯的候選圖重新錨定，而非本輪能修正的範圍（Reference Element 已鎖定該外觀，不會因為新 prompt 而改變身形特徵）。

### 8. 補充：其餘 5 張（#4、#7、#8、#11、#12）逐張檢視結果

- **#4（泳裝日常他拍）**：門口回頭一瞥，背影+回眸清楚看到臉，身分一致；背景鄰居房屋、板具、水管、拖鞋等生活細節到位；穿搭黑色比基尼+牛仔短褲符合規劃。
- **#7（沖鹽自拍）**：坐板邊自拍，笑容自然，防曬乳瓶罐+濕髮+水珠細節到位；跟 #6（他拍運動相機版本）並排比對，畫質銳利度依然相近，同樣印證第 7 節 (b) 的觀察——自拍柔焦語法效果不明顯。
- **#8（東岸小屋他拍）**：吊床上，濕式防寒衣掛在欄杆、板具立牆邊，笑容自然、身分一致，光線為陽台自然光+暖色斜陽，符合規劃。
- **#11（衝浪旅行自拍）**：墾丁海邊自拍，風吹頭髮遮到部分臉但笑容/雀斑仍清晰可辨，身分一致，日落逆光層次好。
- **#12（划水瑜伽他拍）**：沙灘瑜伽戰士式伸展，逆光剪影感強但臉部仍可辨識，板子+梳子+毛巾道具到位，前景可見他拍用的手機腳架，強化「他拍」敘事。

全部 13 張目視檢視後，第 7 節列出的 (a)–(e) 結論維持不變且獲得更多樣本佐證：身分一致性佳、膚色與錨點圖一致無漂移、場景/穿搭多樣性涵蓋全部六大支柱、CCD／美顏濾鏡風格變化清楚可辨，但「自拍前鏡頭應更柔焦/低規格」這條 2026-07-30 新規則在 5 張自拍圖（#2、#3、#7、#9、#11）中僅 #9（美顏濾鏡款）有明顯效果，其餘 4 張自拍圖與他拍圖的銳利度/畫質沒有肉眼可辨的差異——這是本輪誠實記錄的主要落差，建議使用者知悉。

---

## 下一步（待使用者確認）

**⚠️ 依 `README.md`「新增 KOL 流程」步驟 7 與 `KOL_TRAINING_SOP.md` 的強制檢查點：本輪到此為止，尚未呼叫 `show_characters(action='train')`，`profile.json` 沒有新增 `soul_id` 或 `ai_generation` 欄位，維持原狀未變更。**

1. 使用者需實際檢視全部 13 張訓練圖（`kols/zoe-lai/images/training_v1/`），確認：身分是否真的一致、膚色是否維持在可接受範圍、場景/穿搭多樣性是否足夠、自拍/他拍畫質差異是否需要進一步調整
2. 若使用者核准，下一步才呼叫 `show_characters(action='train')` 建立正式 Soul
3. 若使用者對第 7 節列出的觀察（尤其是 (b) 自拍柔焦效果不明顯、附帶觀察的腹肌線條）有意見，需先調整後重新生成，再送審核

**等待使用者確認這組訓練圖後才能進行 Soul 訓練。**

---

## 2026-08-05 競品對標實測批次（Sherry 打法驗證，7 位台灣籍角色各 2 張）

> **批次目的**：驗證從競品 @sherry_digitalp510 拆解出的三項新做法能否用純生成複製——(1) 公共場景加入背景路人、(2) 同穿搭一日敘事串聯兩張、(3) 地點寫成環境元素清單。完整拆解見 `COMPETITOR_sherry_digitalp510.md`，規則已寫入 `SEXY_SCENE_LIBRARY.md` 第 9／11／12 點。
>
> **平台／模型**：Higgsfield `soul_2` + 本角色 `soul_id`，quality 2k，aspect_ratio 3:4
> **成本**：全批 14 張約 8 credits
> **使用者決定**：本批次**不重新生成**，spec 落差記錄在案，留待後續處理

### 本角色結果

| 項目 | 內容 |
|---|---|
| Soul ID | `27f750e6-0d32-43ce-8249-cce94ef835cd` |
| 場景 | 海灘（抱衝浪板走上沙灘）／老街（矮凳喝飲料） |
| 穿搭（A/B 共用） | 黑色比基尼上衣 + 敞開的寬大白色男裝襯衫 + 刷白丹寧短褲 + 赤腳 + 推到頭頂的墨鏡 |
| Job ID（A） | `46af3d5a-f723-4086-a43c-ecd6ebfe4809` |
| Job ID（B） | `3628eee3-8b30-4d7a-b1a5-bf53046abbf3` |
| 評定 | ❌ 臉齡嚴重偏離，未重生 |

**主要問題：兩張的臉齡都明顯偏高**，設定 26 歲，生成結果讀起來 35 歲以上。這不是 prompt 用詞問題（prompt 已寫 26-year-old 與 gorgeous beach-influencer good looks），判斷為 **Soul 訓練集本身的臉齡偏高**，需要回頭檢視 `training_v1` 的 13 張訓練圖。**次要問題**：膚色仍偏曬黑、腹肌線條比「淡淡若隱若現」的設定更明顯——同樣指向訓練集而非 prompt。老街場景本身很成功（鐵捲門、盆栽、手寫菜單黑板、機車、背景路人）。

### 本批次共同結論（全 7 位角色適用）

- ✅ **背景路人：14/14 全部成功，且無任何配角撞臉主角。** 四條件措辭（背向／不看鏡頭／失焦／外型與主角區隔）有效，成本為零。原「預設只有本人入鏡」規則對公共場景已反轉。
- ✅ **同穿搭一日敘事：7/7 成功。** 服裝配件完整延續且狀態自然演變。
- ⚠️ **地點：環境元素清單成功，點名地標全部失敗。** 「愛河」生出墨爾本天際線、「台北 101」生出通用摩天樓群。
- ⚠️ **中文招牌全部亂碼**（與競品同等程度），本批次接受此取捨。
- 🔴 **打光尚未套用新公式。** 本批次仍使用舊的「品質形容詞」寫法（`crisp`／`high dynamic range`／`well-exposed`）。2026-08-05 拆解競品後已改寫 `SEXY_SCENE_LIBRARY.md` 第 3 點為五段式物理光線公式，**下一批次應以驗證該公式為首要目標**。


---

## 2026-08-05 人設調整：從「衝浪女孩」改為「東岸女孩，衝浪只是背景」＋臉齡與撞臉修正

**背景**：本輪原本只是要修正 Zoe 的臉齡問題（見上方「2026-08-05 競品對標實測批次」章節記錄的臉齡偏高問題）。修正臉齡後，使用者看過新候選圖再提出兩個更根本的問題：

1. 新候選人身材沒有露出來就直接推薦錨點，等於重複了 Rainie Hsu 案例「沒核對身材規格就選錨點」的錯誤
2. 新候選人臉部跟 Iris Chen、Rainie Hsu 等其他台灣籍角色有點太像，區隔不夠

進一步討論後，使用者決定不只修臉，直接對這個人格做更大幅度的調整：**不要讓所有素材都往衝浪方向生成，她可以更日常一點**；另外眼睛改成的琥珀棕色（用來跟其他角色做區隔）使用者看了覺得「很奇怪」，要求改回自然深棕色，臉型和髮型維持不變。

### 1. 臉齡修正（第一階段，已完成）

核心 prompt 移除「dark brown eyes with a natural relaxed squint from years facing open water」這類會讀成「常年風霜」的描述，改寫為明確的年輕化描述：`smooth unlined skin with no crow's feet, no fine lines`、`youthful dewy glow`、眼神描述改為「柔和年輕的凝視」。4 張新候選圖（`seedream_v4_5`，無錨點探索批次）全部驗證臉齡明顯回到 26 歲左右，較之前的 candidate_01/03（讀起來 35+）大幅改善。

### 2. 臉部區隔修正（第二階段）

加入專屬識別特徵，與其他角色的臉部描述做幾何區隔（比照 Sophia Tseng vs Rainie Hsu 的「互斥形容詞骨架」做法）：
- 臉型：`long oval face with a slightly stronger, squarer jawline`（不是 Iris/Coco/Mia 的圓潤娃娃臉，也不是 Rainie 的雕塑感銳利臉）
- 鼻子：`straight strong nose bridge`（不是 Iris 的「精緻高鼻樑」）
- 專屬標記：`a small faint scar through the outer edge of her left eyebrow from an old surfing wipeout`——衝浪造成的疤痕，同時是識別特徵也呼應人設背景
- 眼睛（**本階段用了 hazel-brown，後續第四階段已改回自然深棕色**）

用 4 張候選人（3 露出身材＋1 純臉部特寫）與 Iris Chen、Rainie Hsu 的實際素材並排比對（`face_grid.jpg`），使用者看過後認為區隔可以接受，但同時指出這批候選人身材全數偏離設定（腹肌過於明顯，比「柔和曲線、不是健身房雕塑」的原始設定更緊實）。

### 3. 人設方向調整：內容支柱重新分配（第三階段，核心修改）

**修改的文件**：`content_style.md`（內容支柱表、每週發文節奏、影片格式規範燈光段落全部重寫）、`character.md`（內容方向章節、內容哲學章節、個性段落「她在水裡比在陸地上自在」、視覺美學光線段落）。

原本 6 個支柱（晨間衝浪/泳裝日常/沖鹽淨身/東岸小屋/衝浪旅行/划水健身）全部圍繞衝浪展開，即使「東岸小屋」「額外生活主題」裡其實已經寫了花蓮家人時光、陽台植栽這些跟衝浪無關的素材，但因為沒有被排進正式支柱權重，實際生成從未用到。重新分配為：

| 新支柱 | 佔比 |
|---|---|
| 日常穿搭出門 | 20% |
| 居家生活 | 20% |
| 花蓮家人時光 | 15% |
| 海邊日常（含衝浪） | 20% |
| 沖水沙灘澡 | 10% |
| 朋友社交 | 15% |

衝浪相關內容從原本 6 個支柱全部涉及（100%）降到集中在「海邊日常」一個支柱（20%），且該支柱內明確要求「不是每張海邊照片都要有衝浪板入鏡」。

### 4. Prompt 修正：眼睛改回自然深棕色 + 身材描述鬆綁「衝浪選手」框架

- 眼睛：`hazel-brown eyes with natural sun-lightened flecks` → `natural warm dark brown eyes (NOT an unusual light or tinted eye colour, just normal healthy dark brown)`
- 身材：拿掉「athletic swimmer/surfer build」的框架敘述，改為「naturally curvy figure with soft feminine curves, full bust, soft flat stomach with NO visible six-pack or muscle definition, curved hips」——不再用「划水練出來的」當身材線條的敘事理由

### 5. 驗證批次：3 張日常場景示範圖

用修正後的 prompt 生成 3 張完全跟衝浪無關的場景，驗證新方向：

| 場景 | 內容 | Job ID |
|---|---|---|
| 市場騎車 | 騎機車去傳統市場買菜，菜籃裝蔬果，背景真實攤商與路人 | `f69727bc-2379-41f7-b039-5d7469e0b559` |
| 在家澆花 | 公寓客廳地上盤坐，澆窗邊多肉植物，衝浪板只是安靜立在角落當背景，不是主角 | `d577e2b0-9c95-40f5-82e9-ee2cfc01e700` |
| 雜貨店家人時光 | 坐在爸媽雜貨店門口板凳上跟媽媽聊天，背景是醃漬罐頭與手寫招牌 | `b603a18d-d363-488d-bda3-b04173bd4244` |

**誠實視覺評估**：3 張皆親自用 Read 工具檢視。眼睛已確認是自然深棕色，不再有奇怪的琥珀/契合鏡片感；場景成功脫離衝浪/泳裝框架；背景路人、招牌、雜物等生活細節到位；臉部特徵（長橢圓臉、較方的下顎線、眉尾疤痕）維持與第二階段候選人一致。**尚未驗證項目**：3 張都是坐姿/半身為主，沒有像 Rainie 案例那樣特意安排全身/曲線清晰可見的鏡頭，因此身材是否真的達到「柔和曲線、無六塊肌」的修正目標，**尚待下一批次生成明確露出身材的候選圖後才能確認**——這是使用者核准本方向後，建立正式訓練集前必須補做的檢查，不可跳過（比照 Rainie Hsu 案例的教訓）。

**下一步（待使用者核准本方向後才執行）**：生成 2–4 張明確露出身材曲線的候選圖確認身材修正是否成功 → 選定錨點 → 建立 Reference Element → 生成完整 13 張訓練集（六大新支柱各按權重分配張數）→ 送 Soul 訓練，取得新 soul_id 取代舊的 `27f750e6-0d32-43ce-8249-cce94ef835cd`（舊 soul_id 同樣保留不刪除，標記 deprecated）。
