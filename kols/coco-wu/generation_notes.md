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
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, small rounded chin, sweet cute features, big round bright eyes with a slightly sleepy charm (NOT narrow, sharp, or almond-shaped — standard mainstream beauty, school-beauty-tier good looks), dark brown long wavy hair with wispy bangs, petite 158cm frame, 89cm bust (E cup, natural and full), 56cm waist, 86cm hips — soft curvy figure worn naturally and comfortably in her own body (not deliberately sexualized, not hidden or minimized either), visible skin pores, subtle natural skin texture, unretouched but flattering skin detail, [SCENE], wearing [OUTFIT — color-coordinated pieces in her established cream / baby-pink / mint / lilac palette, not generic mismatched basics], [DYNAMIC CANDID POSE/ANGLE — caught mid-laugh, mid-motion, or mid-reaction, NOT a stiff posed-for-camera stance], [AGE-APPROPRIATE CAMPUS ACCESSORY — hair clip, phone with a cute character case, canvas tote bag, or canvas badminton bag as a natural detail, not a focal point], [LIGHTING — see indoor vs. outdoor/lifestyle recipe split below], shot on iPhone 15 Pro [front/rear per scene] camera with scene-specific device quirks, crisp sharp focus, well-exposed high-quality modern smartphone photo — NOT degraded, grainy, or dim regardless of indoor or outdoor setting, film grain, candid lifestyle photo, soft pastel warm tones, natural color grading, shot on 35mm, phone-camera casual feel, Instagram style
```

**注意事項**：
- 角色臉部與身材設定需維持一致；場景與穿搭多做變化
- Prompt 中避免任何會讓她看起來比實際年齡更年幼的詞彙（例如 childlike, tiny body 等），必要時可加入 `mature 20-year-old proportions` 強化成年感
- 身材數字（89-56-86cm，E罩杯，詳見 `profile.json` 的 `measurements`）直接寫進 prompt 本體，不要只用「soft curvy figure」這種模糊形容詞帶過
- 光線依場景類型分兩套配方（見 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉2026-07-25 修正）：宿舍室內場景（賴床／衛浴／居家耍廢）用「混合、不均勻但溫暖」邏輯；戶外／生活風格場景（穿搭出門、羽球社、校園散步、飯店旅遊）用「討喜自然光＋淺景深＋清晰高畫質」邏輯。**兩者都不等於畫質差／偏暗／顆粒過重**——「真實感」跟「拍得普通」是兩件事
- 不論室內或戶外，畫質方向都是清晰、曝光正常、現代手機拍照質感，**絕對不要**寫成 degraded / grainy / dim
- 自拍視角描述的是照片本身的輸出視角，不是「她在拍自拍」的動作：
  - ❌ 錯誤：`taking a selfie holding phone up`
  - ✅ 正確：`close-up front-facing selfie shot, slightly overhead angle looking down at camera, looks like a photo taken by her own phone front camera`
- 服裝與姿勢維持 SFW 尺度上限：camis、睡衣、居家服、校園穿搭，不出現裸露或性暗示動作

**⚠️ 2026-07-25 燈光/身材數字校準**：比照 Vicky Lin 案例的使用者回饋修正經驗，主動對 Coco 的核心 prompt 與六個計畫批次做同等級校準，避免同樣的問題在她身上重演——(1) 原本的核心 prompt 用「soft curvy figure」帶過身材，沒有把 `profile.json` 裡的三圍數字（89-56-86cm，E罩杯）寫進 prompt 本體，這次直接寫進去，取代模糊形容詞；(2) 檢查臉部描述（圓臉娃娃臉、大圓眼、梨渦、小巧下巴）本身已經是「標準大眾審美」方向，沒有出現細長/銳利/上揚眼型之類的風險字眼，**維持不變**，只在後面加註「NOT narrow, sharp, or almond-shaped」把方向講死，避免生成模型自行偏移；(3) 光線邏輯依 `SEXY_SCENE_LIBRARY.md` 2026-07-25 修正後的兩套配方，重新分類六個計畫批次——宿舍室內場景（批次1賴床、批次3衛浴、批次4居家耍廢）維持原本「混合不均勻」邏輯，但明確加註是溫暖柔和的光，不是刻意調暗/做舊；戶外與生活風格場景（批次2校園走路、批次5飯店旅遊、批次6羽球社——依 `SEXY_SCENE_LIBRARY.md` 的分類，「旅遊」「健身」都屬於戶外/生活風格類別，即使實際場景在室內飯店房或體育館內）改用「討喜自然光＋淺景深背景虛化＋crisp high dynamic range」邏輯，並在每張 prompt 明講 `NOT degraded, grainy, or dim`；(4) 服裝從一般性描述（如「a simple sleep tank top」）改為指定她既有的奶油白/嬰兒粉/薄荷綠/淺紫丁香同色系穿搭，呼應 `content_style.md` 視覺美學的色調設定；(5) 姿勢語言從單純「候著鏡頭」補強為明確的動態抓拍描述（大笑中、走動中、跌坐中、反應中）；(6) 補上符合年齡與場景的校園配件（髮夾、手機殼、帆布托特包、羽球袋）作為自然生活細節，取代批次6原本的通用「gym bag」。以下六個計畫批次的 prompt 已依此全部重寫。

---

## 計畫批次 Prompt 規劃

> 以下為計畫中的訓練圖批次構想，尚未執行生成，僅作為未來操作時的草稿參考。批次數量、模型選擇與最終 prompt 措辭在實際執行時可能調整。
>
> **每個草稿 Prompt 已依 `SEXY_SCENE_LIBRARY.md`「降低『AI 感』的技術要點」五項檢查清單改寫**：(1) 皮膚質感關鍵字、(2) 逐場景具體的拍攝裝置/鏡頭破綻描述、(3) 依場景類型（室內／戶外-生活風格）對應的正確光源配方、(4) 宿舍/場景專屬的生活雜物細節、(5) 完整明確且同色系協調的服裝描述。實際執行時仍可微調措辭，但五項要點應保留。
>
> **⚠️ 2026-07-25 校準**：本節六個批次已依上方「核心 Prompt 結構」的 2026-07-25 校準全部重寫——三圍數字（89-56-86cm，E罩杯）直接寫進每張 prompt、光線依室內／戶外-生活風格正確分類、服裝改為同色系描述、姿勢改為動態抓拍語言、補上校園配件細節，並在每張 prompt 明講畫質方向 `NOT degraded, grainy, or dim`。

### 計畫批次 1 — 宿舍房間早晨（Dorm Room Morning）

**場景構想**：早八鬧鐘剛響，她還窩在宿舍單人床上，頭髮亂糟糟，棉被拉到胸口，宿舍窗簾縫透進晨光。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, small rounded chin, big round bright sleepy eyes (NOT narrow or sharp — standard mainstream beauty), dark brown long wavy hair messy from sleep, petite 158cm frame, 89cm bust (E cup, natural and full), 56cm waist, 86cm hips, soft curvy figure comfortable in her own skin, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, lying in a dorm room single bed with rumpled white bedding, a phone with a cute character case on a charger cable trailing off the nightstand, a half-drunk water bottle and yesterday's textbook left on the floor beside the bed, an alarm clock glowing on the desk, wearing a cream-colored oversized soft pajama top slipping off one shoulder, drowsy half-smile toward camera, close-up front-facing selfie shot, slightly overhead angle looking down at camera, looks like a photo taken by her own phone front camera, shot on iPhone 15 Pro front camera, slight autofocus softness on the rumpled bedding in the background, natural highlight clipping where morning window light hits the pillow, subtle motion blur on her hand pushing hair from her face, faint JPEG compression at the high-contrast window-curtain edge, mixed color temperature — cool blue morning window light blending with the warm glow of her desk lamp left on overnight, uneven light falloff across the bed, soft but visible shadow edges — a naturally warm and soft morning glow, NOT dim, degraded, or grainy, crisp clear detail and true-to-life skin tones, film grain, candid lifestyle photo, soft pastel warm tones, natural color grading, Instagram style
```

---

### 計畫批次 2 — 校園走路 3/4 身（Campus Walk, Three-Quarter Shot）

**場景構想**：走在校園步道上準備去上課，敞開穿的針織開襟外套配百褶裙與過膝襪，陽光普通的白天校園日常感。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, sweet cute features, big round bright eyes (NOT narrow or sharp — standard mainstream beauty), dark brown long wavy hair with wispy bangs half tied up with a small hair clip, petite 158cm frame, 89cm bust (E cup, natural and full), 56cm waist, 86cm hips, soft curvy figure comfortable in her own skin, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, walking mid-stride on a university campus pathway past bike racks and a flyer-covered notice board, dropped leaves scattered on the cracked pavement, blurred students softly out of focus in the background, laughing at something a friend off-frame just said, holding a half-finished bubble tea cup, a canvas tote bag swinging from her shoulder, wearing a cream open-knit cardigan over a baby-pink camisole top, a cream pleated mini skirt, white over-the-knee socks — fully coordinated in her established pastel palette, three-quarter angle candid walking shot caught mid-laugh, shot on iPhone 15 Pro rear camera held by a roommate walking beside her, slight autofocus hunting on foreground foliage, subtle motion blur on her swinging hair and tote bag from the walking pace, faint JPEG compression on high-contrast building edges, golden hour sunlight or bright clear daylight, natural directional light with soft flattering falloff, shallow depth of field with blurred bokeh background on the bike racks and passing students, crisp sharp focus on her, high dynamic range, natural color grading — NOT degraded, dim, or muddy, film grain, candid lifestyle photo, soft pastel warm tones, Instagram style
```

---

### 計畫批次 3 — 宿舍衛浴 GRWM（Dorm Bathroom Get-Ready-With-Me）

**場景構想**：宿舍公共衛浴間鏡前刷牙洗臉，鏡子偏小、燈光普通，帶點真實宿舍質感而非精緻美妝棚拍。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, small rounded chin, big round bright eyes (NOT narrow or sharp — standard mainstream beauty), dark brown long wavy hair clipped up loosely with a small hair clip, petite 158cm frame, 89cm bust (E cup, natural and full), 56cm waist, 86cm hips, soft curvy figure comfortable in her own skin, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, standing at a small shared dorm bathroom mirror brushing teeth, toothbrush cups cluttered on the counter, damp towels hanging on hooks behind her, a half-empty shampoo bottle and tangled hairbrush on the sink edge, water spots visible on the mirror glass, wearing a mint-green simple cotton sleep tank top, playful expression making a face at the mirror, close-up mirror reflection angle, shot on iPhone 15 Pro front camera reflected in the mirror, slight autofocus hunting on the mirror's glass surface, subtle motion blur on her hand moving the toothbrush, faint compression artifacts around the mirror's edge glare, mixed lighting — flat overhead fluorescent tube light blending with warm hallway light spilling through the half-open door, uneven color temperature with a slightly cool fluorescent cast on her skin, visible soft shadow under the chin from the overhead angle — the fluorescent cast is a real dorm-bathroom detail, not a sign of bad photo quality: the image stays crisp, clearly exposed and true-to-life, NOT dim, grainy, or degraded, film grain, candid lifestyle photo, soft pastel warm tones, natural color grading, Instagram style
```

---

### 計畫批次 4 — 室友聚會 / 宿舍耍廢（Roommate Hangout in Dorm）

**場景構想**：晚自習後窩在宿舍床上跟室友聊天耍廢，抱著抱枕大笑，書桌上堆著課本和珍奶杯，宿舍檯燈暖黃光。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, big round bright eyes (NOT narrow or sharp — standard mainstream beauty), dark brown long wavy hair down and slightly messy, petite 158cm frame, 89cm bust (E cup, natural and full), 56cm waist, 86cm hips, soft curvy figure comfortable in her own skin, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, sitting on a dorm bed hugging a pillow laughing hard with a roommate off-frame, desk nearby stacked haphazardly with textbooks and a corkboard of idol photocards, a bubble tea cup leaving a condensation ring, tangled phone charging cables, a half-eaten instant noodle cup and snack wrappers, laundry draped over the desk chair, fairy lights strung along the wall, wearing a lilac oversized soft home top slipping off one shoulder with a cream camisole visible underneath, relaxed candid laughing expression caught mid-laugh, casual angle as if a roommate took the photo, shot on iPhone 15 Pro rear camera held by the roommate sitting nearby, slight autofocus softness on the cluttered desk in the background, warm amber highlight clipping from the desk lamp bulb, subtle motion blur from her laughing movement, mixed lighting — a single warm desk lamp as the main light source blending with the cool blue glow of a laptop screen left open nearby, uneven falloff brighter near the lamp and softly shadowed in the room's corners — a cozy warm glow, NOT degraded, dim, or grainy, crisp clear detail throughout, soft shadow edges across her face, film grain, candid lifestyle photo, soft pastel warm tones, natural color grading, Instagram style
```

---

### 計畫批次 5 — 週末飯店小旅行（Weekend Trip, Hotel Check-in）

**場景構想**：跟室友衝墾丁週末小旅行，剛抵達飯店房間，行李箱都還沒打開就先興奮地倒在床上。此為 character.md「飯店旅遊 / 週末出遊」（10%）內容支線，目前尚未有對應批次，狀態同全文件為 PENDING，尚未執行生成。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, sweet cute features, big round bright eyes (NOT narrow or sharp — standard mainstream beauty), dark brown long wavy hair slightly tousled from travel, petite 158cm frame, 89cm bust (E cup, natural and full), 56cm waist, 86cm hips, soft curvy figure comfortable in her own skin, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, flopping backward excitedly onto an unfamiliar hotel bed with the suitcase still zipped shut on the floor, a room key card and hotel brochure left on the nightstand, a phone with a cute character case and its charger cable draped over the lamp, a half-drunk bottled water and kicked-off sneakers near the bed, a roommate's jacket tossed over a chair, wearing a cream oversized cotton t-shirt over denim shorts (travel outfit), one sneaker still half on, arms thrown open in excitement, candid mid-motion moment caught mid-fall, shot on iPhone 15 Pro rear camera held by a roommate capturing the moment as she flops onto the bed, slight autofocus softness on the gauzy hotel curtains in the background, subtle motion blur on her arms and hair mid-fall onto the mattress, faint JPEG compression artifacts along the suitcase's high-contrast edges, warm afternoon sunlight through the hotel curtains, natural directional light with soft flattering falloff, shallow depth of field with soft blur on the curtains and suitcase in the background, crisp high dynamic range, sharp focus on her, natural color grading — NOT degraded, dim, or muddy, film grain, candid lifestyle photo, soft pastel warm tones, Instagram style
```

---

### 計畫批次 6 — 羽球社練球後場邊（Badminton Club, Court-side After a Match）

**場景構想**：系上羽球社練球剛結束，坐在球場邊喝水休息，額頭有點汗，分享今天贏了一局的興奮。此為 character.md「健身 / 校園散步與羽球社」（5%）內容支線，目前尚未有對應批次，狀態同全文件為 PENDING，尚未執行生成。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, big round bright eyes (NOT narrow or sharp — standard mainstream beauty), dark brown long wavy hair pulled back in a slightly messy ponytail with damp flyaway strands stuck to her forehead and neck, petite 158cm frame, 89cm bust (E cup, natural and full), 56cm waist, 86cm hips, soft curvy figure comfortable in her own skin, visible skin pores, subtle natural skin texture, faint sheen of sweat on her collarbone and hairline, unretouched skin detail, natural skin imperfections, sitting court-side on a gymnasium bench right after a badminton match, racket resting across her lap, a water bottle sweating condensation beside her, a canvas badminton bag with a racket cover and shuttlecock tube spilling out, a discarded towel and scattered shuttlecocks visible on the court floor behind her, a blurred scoreboard in the background, wearing a cream and mint-green two-tone fitted moisture-wicking tank top with matching athletic shorts, still catching her breath with an excited grin, shot on iPhone 15 Pro front camera held slightly below eye level as she snaps a court-side selfie, noticeable autofocus hunting between her face and the blurred gymnasium background, subtle motion blur on her hand still gripping the racket as it shifts, bright natural daylight flooding in through the gymnasium's large windows and skylights, mixing with the gym's overhead lights, natural directional light with soft flattering falloff, shallow depth of field softly blurring the scoreboard and bleachers behind her, crisp sharp focus on her, high dynamic range, natural color grading — NOT degraded, dim, or grainy, film grain, candid lifestyle photo, soft pastel warm tones, Instagram style
```

---

## 下一步（待執行）

實際生成執行時需依序記錄：使用的平台/模型、實際生成的 job ID、選定的訓練圖、Soul 訓練狀態與完成日期。本文件目前不包含這些內容，待生成流程實際跑過後再補充於本檔案或另立記錄章節。
