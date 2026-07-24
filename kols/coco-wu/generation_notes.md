# Coco Wu — AI 生成規劃

> **狀態：PENDING — 尚未執行任何 AI 生成**
> 本檔案只是規劃文件，記錄未來 AI 生成的角色設定、核心 prompt 結構與計畫批次。目前尚未進行任何訓練圖生成、Soul 訓練或影片生成，**沒有 soul_id、沒有已生成圖片、沒有生成日期**。所有 job ID / 圖片數量 / 訓練完成狀態等欄位待實際執行後才會補上，本文件不預先捏造。

---

## 人物設定

| 欄位 | 設定 |
|------|------|
| 名字 | Coco Wu（吳可可） |
| 年齡 | **20 歲，法定成年人**，大二在讀。生成時務必維持成年大學生的情境感，不得出現任何降低年齡感的元素（幼態化表情、兒童化道具或用語） |
| 國籍 | 台灣（台中） |
| 臉型 | 圓臉娃娃臉，笑起來兩邊有明顯梨渦（酒窩），下巴小巧圓潤，五官甜美可愛。純粹描述性外型設定，**不對應任何真實公眾人物** |
| 身材 | 158cm 嬌小身形，軟嫩帶曲線的圓潤體態，胸部與臀部自然豐滿但不刻意展示，整體是舒服自在的體態感，不是刻意擺出的性感姿勢 |
| 眼睛 | 大而圓，眼神亮，笑起來瞇成一條線，帶點沒睡飽的可愛感 |
| 眼鏡 | 念書或趕作業時偶爾戴圓框眼鏡，平常出門不戴 |
| 髮型 | 黑棕色長波浪捲髮，帶蓬鬆落散劉海，日常常隨手夾起或綁半丸子頭 |
| 穿衣風格 | 敞開穿的針織開襟外套配削肩小可愛、百褶迷你裙、過膝襪；居家服偏小一號、舒適隨性的校園休閒感 |
| 場景基調 | 台中大學宿舍、校園日常，不是精緻攝影棚場景 |

---

## 核心 prompt 結構

> 所有生成統一使用以下基礎結構，僅替換場景、服裝、姿勢角度與光線描述部分。角色描述全程為純物理外型描述，不引用任何真實藝人或公眾人物。

```
20-year-old Taiwanese university student, legal adult, round baby face with soft dimples when smiling, small rounded chin, sweet cute features, big round bright eyes with a slightly sleepy charm, dark brown long wavy hair with wispy bangs, petite 158cm frame with soft curvy figure, natural relaxed body comfortable in her own skin (not deliberately sexualized), [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], film grain, candid lifestyle photo, soft pastel warm tones, shot on 35mm, phone-camera casual feel, Instagram style
```

**注意事項**：
- 角色臉部與身材設定需維持一致；場景與穿搭多做變化
- Prompt 中避免任何會讓她看起來比實際年齡更年幼的詞彙（例如 childlike, tiny body 等），必要時可加入 `mature 20-year-old proportions` 強化成年感
- 自拍視角描述的是照片本身的輸出視角，不是「她在拍自拍」的動作：
  - ❌ 錯誤：`taking a selfie holding phone up`
  - ✅ 正確：`close-up front-facing selfie shot, slightly overhead angle looking down at camera, looks like a photo taken by her own phone front camera`
- 服裝與姿勢維持 SFW 尺度上限：camis、睡衣、居家服、校園穿搭，不出現裸露或性暗示動作

---

## 計畫批次 Prompt 規劃

> 以下為計畫中的訓練圖批次構想，尚未執行生成，僅作為未來操作時的草稿參考。批次數量、模型選擇與最終 prompt 措辭在實際執行時可能調整。
>
> **每個草稿 Prompt 已依 `SEXY_SCENE_LIBRARY.md`「降低『AI 感』的技術要點」五項檢查清單改寫**：(1) 皮膚質感關鍵字、(2) 逐場景具體的拍攝裝置/鏡頭破綻描述、(3) 混合不均勻光源配方、(4) 宿舍/場景專屬的生活雜物細節、(5) 完整明確的服裝描述。實際執行時仍可微調措辭，但五項要點應保留。

### 計畫批次 1 — 宿舍房間早晨（Dorm Room Morning）

**場景構想**：早八鬧鐘剛響，她還窩在宿舍單人床上，頭髮亂糟糟，棉被拉到胸口，宿舍窗簾縫透進晨光。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, small rounded chin, big round sleepy eyes, dark brown long wavy hair messy from sleep, petite 158cm frame with soft curvy figure, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, lying in a dorm room single bed with rumpled white bedding, a phone charger cable trailing off the nightstand, a half-drunk water bottle and yesterday's textbook left on the floor beside the bed, an alarm clock glowing on the desk, wearing an oversized soft pajama top slipping off one shoulder, drowsy half-smile toward camera, close-up front-facing selfie shot, slightly overhead angle looking down at camera, looks like a photo taken by her own phone front camera, shot on iPhone 15 Pro front camera, slight autofocus softness on the rumpled bedding in the background, natural highlight clipping where morning window light hits the pillow, subtle motion blur on her hand pushing hair from her face, faint JPEG compression at the high-contrast window-curtain edge, mixed color temperature — cool blue morning window light blending with the warm glow of her desk lamp left on overnight, uneven light falloff across the bed, soft but visible shadow edges, film grain, candid lifestyle photo, soft pastel warm tones, Instagram style
```

---

### 計畫批次 2 — 校園走路 3/4 身（Campus Walk, Three-Quarter Shot）

**場景構想**：走在校園步道上準備去上課，敞開穿的針織開襟外套配百褶裙與過膝襪，陽光普通的白天校園日常感。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, sweet cute features, big round bright eyes, dark brown long wavy hair with wispy bangs half tied up, petite 158cm frame with soft curvy figure, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, walking on a university campus pathway past bike racks and a flyer-covered notice board, dropped leaves scattered on the cracked pavement, blurred students in the background, holding a half-finished bubble tea cup, wearing an open knit cardigan over a camisole top, pleated mini skirt, over-the-knee socks, three-quarter angle candid walking shot, shot on iPhone 15 Pro rear camera held by a roommate walking beside her, slight autofocus hunting on foreground foliage, natural highlight clipping on direct sunlight patches across the pathway, subtle motion blur on her swinging hair and tote bag from the walking pace, faint JPEG compression on high-contrast building edges, mixed lighting — bright uncovered daylight overexposing one side of the frame while the building's shadow cools the other side, dappled tree-shadow falloff across the pathway, uneven light patches, film grain, candid lifestyle photo, soft pastel warm tones, Instagram style
```

---

### 計畫批次 3 — 宿舍衛浴 GRWM（Dorm Bathroom Get-Ready-With-Me）

**場景構想**：宿舍公共衛浴間鏡前刷牙洗臉，鏡子偏小、燈光普通，帶點真實宿舍質感而非精緻美妝棚拍。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, small rounded chin, big round eyes, dark brown long wavy hair clipped up loosely, petite 158cm frame with soft curvy figure, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, standing at a small shared dorm bathroom mirror brushing teeth, toothbrush cups cluttered on the counter, damp towels hanging on hooks behind her, a half-empty shampoo bottle and tangled hairbrush on the sink edge, water spots visible on the mirror glass, wearing a simple sleep tank top, playful expression making a face at the mirror, close-up mirror reflection angle, shot on iPhone 15 Pro front camera reflected in the mirror, slight autofocus hunting on the mirror's glass surface, greenish highlight clipping from the overhead fluorescent tube reflecting off the mirror, subtle motion blur on her hand moving the toothbrush, faint compression artifacts around the mirror's edge glare, mixed lighting — flat overhead fluorescent tube light blending with warm hallway light spilling through the half-open door, uneven color temperature with a slightly greenish fluorescent cast on her skin, visible shadow under the chin from the overhead angle, film grain, candid lifestyle photo, soft pastel warm tones, Instagram style
```

---

### 計畫批次 4 — 室友聚會 / 宿舍耍廢（Roommate Hangout in Dorm）

**場景構想**：晚自習後窩在宿舍床上跟室友聊天耍廢，抱著抱枕大笑，書桌上堆著課本和珍奶杯，宿舍檯燈暖黃光。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, big round bright eyes, dark brown long wavy hair down and slightly messy, petite 158cm frame with soft curvy figure, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, sitting on a dorm bed hugging a pillow laughing with a roommate off-frame, desk nearby stacked haphazardly with textbooks, a bubble tea cup leaving a condensation ring, tangled phone charging cables, a half-eaten instant noodle cup and snack wrappers, laundry draped over the desk chair, fairy lights strung along the wall, wearing an oversized soft home outfit slipping off one shoulder with a camisole visible underneath, relaxed candid laughing expression, casual angle as if a roommate took the photo, shot on iPhone 15 Pro rear camera held by the roommate sitting nearby, slight autofocus softness on the cluttered desk in the background, warm amber highlight clipping from the desk lamp bulb, subtle motion blur from her laughing movement, faint compression noise visible in the darker corners of the room, mixed lighting — a single warm desk lamp as the main light source blending with the cool blue glow of a laptop screen left open nearby, strong uneven falloff bright near the lamp and deep shadow in the room's corners, soft shadow edges across her face, film grain, candid lifestyle photo, soft pastel warm tones, Instagram style
```

---

### 計畫批次 5 — 週末飯店小旅行（Weekend Trip, Hotel Check-in）

**場景構想**：跟室友衝墾丁週末小旅行，剛抵達飯店房間，行李箱都還沒打開就先興奮地倒在床上。此為 character.md「飯店旅遊 / 週末出遊」（10%）內容支線，目前尚未有對應批次，狀態同全文件為 PENDING，尚未執行生成。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, sweet cute features, big round bright eyes, dark brown long wavy hair slightly tousled from travel, petite 158cm frame with soft curvy figure, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, flopping backward excitedly onto an unfamiliar hotel bed with the suitcase still zipped shut on the floor, a room key card and hotel brochure left on the nightstand, a phone charger cable draped over the lamp, a half-drunk bottled water and kicked-off sneakers near the bed, a roommate's jacket tossed over a chair, wearing a loose oversized cotton t-shirt over denim shorts (travel outfit), one sneaker still half on, arms thrown open in excitement, candid mid-motion moment, shot on iPhone 15 Pro rear camera held by a roommate capturing the moment as she flops onto the bed, slight autofocus softness on the gauzy hotel curtains in the background, natural highlight clipping where the afternoon window light hits the white bedspread, subtle motion blur on her arms and hair mid-fall onto the mattress, faint JPEG compression artifacts along the suitcase's high-contrast edges, mixed color temperature — warm afternoon sun through the hotel curtains blending with the cooler fluorescent hallway light spilling in from the propped-open door, uneven light falloff leaving one side of the bed brighter than the other, soft but visible shadow edges across the bedspread, film grain, candid lifestyle photo, soft pastel warm tones, Instagram style
```

---

### 計畫批次 6 — 羽球社練球後場邊（Badminton Club, Court-side After a Match）

**場景構想**：系上羽球社練球剛結束，坐在球場邊喝水休息，額頭有點汗，分享今天贏了一局的興奮。此為 character.md「健身 / 校園散步與羽球社」（5%）內容支線，目前尚未有對應批次，狀態同全文件為 PENDING，尚未執行生成。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, big round bright eyes, dark brown long wavy hair pulled back in a slightly messy ponytail with damp flyaway strands stuck to her forehead and neck, petite 158cm frame with soft curvy figure, visible skin pores, subtle natural skin texture, faint sheen of sweat on her collarbone and hairline, unretouched skin detail, natural skin imperfections, sitting court-side on a gymnasium bench right after a badminton match, racket resting across her lap, a water bottle sweating condensation beside her, a gym bag with clothes spilling out, a discarded towel and scattered shuttlecocks visible on the court floor behind her, a blurred scoreboard in the background, wearing a fitted moisture-wicking tank top with sports bra straps visible, athletic shorts, still catching her breath with an excited grin, shot on iPhone 15 Pro front camera held slightly below eye level as she snaps a court-side selfie, noticeable autofocus hunting between her face and the blurred gymnasium background, natural highlight clipping where the overhead gym lights reflect off her damp forehead, subtle motion blur on her hand still gripping the racket as it shifts, faint compression artifacts across the shiny reflective court floor, mixed lighting — harsh overhead fluorescent gym tubes combined with warmer light spilling in from the corridor windows, uneven light falloff creating a slightly darker patch behind her, visible shadow under her chin from the overhead angle, film grain, candid lifestyle photo, soft pastel warm tones, Instagram style
```

---

## 下一步（待執行）

實際生成執行時需依序記錄：使用的平台/模型、實際生成的 job ID、選定的訓練圖、Soul 訓練狀態與完成日期。本文件目前不包含這些內容，待生成流程實際跑過後再補充於本檔案或另立記錄章節。
