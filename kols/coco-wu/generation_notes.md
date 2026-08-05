# Coco Wu — AI 生成規劃

> **狀態：✅ Soul 訓練已完成（`status: ready`），soul_id `cf7045dc-4e69-4c56-9621-aa8c40bf39b4` 已可用於 `model: soul_2` 正式生成內容**
> 本文件原本是生成前的規劃文件。2026-07-30 使用者核准候選圖批次並明確授權送出訓練（「我覺得這四位都可以送去訓練...就先這樣送出訓練」），已用 Reference Element `4b6c659c-786b-43de-87af-87cea3cc99dd`（錨點來源 candidate_01.png）建立完整 12 張訓練集（`images/training_v1/`），並呼叫 `show_characters(action='train')` 成功受理，取得 `soul_id: cf7045dc-4e69-4c56-9621-aa8c40bf39b4`。2026-07-31 確認 `raw_status: completed`，訓練正式完成。

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
20-year-old Taiwanese university student, legal adult, mature 20-year-old proportions, round baby face with soft dimples when smiling, small rounded chin, sweet cute features, big round bright eyes with a slightly sleepy charm (NOT narrow, sharp, or almond-shaped — standard mainstream beauty, school-beauty-tier good looks), dark brown long wavy hair with wispy bangs, petite 158cm frame, 89cm bust (E cup, natural and full), 56cm waist, 86cm hips — soft curvy figure worn naturally and comfortably in her own body (not deliberately sexualized, not hidden or minimized either), fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored), visible skin pores, subtle natural skin texture, unretouched but flattering skin detail, [SCENE], wearing [OUTFIT — color-coordinated pieces in her established cream / baby-pink / mint / lilac palette, not generic mismatched basics], [DYNAMIC CANDID POSE/ANGLE — caught mid-laugh, mid-motion, or mid-reaction, NOT a stiff posed-for-camera stance], [AGE-APPROPRIATE CAMPUS ACCESSORY — hair clip, phone with a cute character case, canvas tote bag, or canvas badminton bag as a natural detail, not a focal point], [LIGHTING — see indoor vs. outdoor/lifestyle recipe split below], shot on iPhone 15 Pro [front/rear per scene] camera with scene-specific device quirks, crisp sharp focus, well-exposed high-quality modern smartphone photo — NOT degraded, grainy, or dim regardless of indoor or outdoor setting, film grain, candid lifestyle photo, soft pastel warm tones, natural color grading, shot on 35mm, phone-camera casual feel, Instagram style
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

## 2026-07-25 Discovery 批次 — 臉部/風格候選圖（已生成，等待使用者挑選，尚未錨定、尚未訓練）

**⚠️ 本節已被下方「2026-07-25 三次修正：改用 Seedream 4.5 重新生成 Discovery 批次」取代（superseded）**——本節記錄的 `soul_2` 批次已被使用者判定「4 張臉不一致」而退回，`candidate_01.png`–`candidate_04.png` 這 4 個檔名已重新命名為 `round1_candidate_01.png`–`round1_candidate_04.png`（詳見下方新章節）。以下內容純粹保留作為歷史記錄，**不代表目前檔案系統的實際檔名對應**。

**狀態：⚠️ PENDING —— 這不是訓練圖批次，只是「選臉/選風格」用的探索性候選圖。尚未建立 Reference Element、尚未呼叫 `show_characters(action='train')`、`profile.json` 沒有 soul_id。**

**觸發背景**：比照 Vicky Lin 案例學到的教訓——獨立文字生成（無身分錨點）每次都會讓模型重新「想像」一張符合描述但不是同一個人的臉，直接拿來訓練會導致多人臉部特徵平均/混合。因此這次採用兩階段流程：**先**用少量獨立生成的候選圖給使用者選出最喜歡的一張臉/風格，**再**用該張圖建立 Reference Element 錨定身分，之後才擴展成完整訓練圖批次。本輪僅執行第一階段。

**模型選擇**：呼叫 `models_explore(action='recommend')` 查詢「無 soul_id 的一次性角色參考圖」用途，回傳結果最高分為 `soul_cast`（但僅支援 16:9 橫幅，不適合直式人像/半身/全身構圈），故延續 Vicky Lin 第二、三輪已驗證的做法，改用 `soul_2`（因 Coco 尚未有 soul_id，符合 `generate_image` 工具說明中「soul_2 for one-off character refs」的預設建議），`aspect_ratio: 9:16`，`quality: 2k`。

**Prompt 設計**：全部 4 張使用 `generation_notes.md` 上方「核心 prompt 結構」2026-07-25 校準後的核心外型描述（三圍 89-56-86cm／E罩杯直接寫入、大圓眼睛「NOT narrow, sharp, or almond-shaped」、圓臉娃娃臉＋梨渦），身分描述逐字保持一致；僅變化角度/景別與對應的姿勢細節（不是完整訓練批次的場景多樣性，純粹是選臉用）：

| 檔名 | 角度 / 景別 | Job ID |
|------|------|--------|
| candidate_01.png | 正面臉部特寫（front headshot） | `837fd5c0-c89c-460c-b673-709f8a7039b7` |
| candidate_02.png | 正面半身（front half-body） | `afed4d18-5eee-49b5-9905-158df4b25dbc` |
| candidate_03.png | 四分之三側半身（3/4 half-body） | `59e9b179-a9d3-4810-9e21-a178ad3b681c` |
| candidate_04.png | 正面全身（front full-body） | `6b18d669-af54-4e64-9c8e-1417326da964` |

統一場景為宿舍素色奶油色牆面（背景可見追星小卡佈告欄與書桌一角，符合她的追星支線與宿舍場景設定）、統一穿搭為奶油色開襟外套配嬰兒粉削肩小可愛（candidate_04 全身圖另加百褶迷你裙與過膝襪以展示全身穿搭），統一光線邏輯（室內自然窗光混合暖色檯燈光）。已依 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉檢查皮膚質感關鍵字、iPhone 15 Pro 前/後鏡頭具體破綻、混合不均勻光源、宿舍雜物細節（追星小卡、充電線）、完整服裝描述。

**費用**：`get_cost` 預估每張約 1 credit（0.12 credits_exact）；生成過程中第一次呼叫遇到 `rate_limit_reached`（ultra 方案 8 個並發上限），等待既有任務完成後重試成功，4 張全數送出並完成，未產生失敗重複扣款。實際餘額由生成前 18.23 credits 降至生成後 **15.83 credits**，本輪共花費 **2.40 credits**（4 張）。

**產出檔案**：`kols/coco-wu/images/face_reference/candidate_01.png` – `candidate_04.png`，已用 Read 工具目視檢查 candidate_01（臉部特寫）與 candidate_04（全身），確認呈現圓臉娃娃臉、梨渦、大圓眼、黑棕色長波浪捲髮、奶油色開襟外套＋嬰兒粉小可愛的宿舍校園風格，符合人物設定方向。**注意**：這 4 張是各自獨立生成（無 Reference Element 錨定），彼此的臉可能不是同一個人，只是同一種類型/風格——這是預期中的行為，因為本階段的目的就是讓使用者從中「選一張最喜歡的臉」，而不是產出身分一致的訓練圖。

**⚠️ 下一步（不可跳過，且不可自動接續）**：
1. 等待使用者從 4 張候選圖中挑出最喜歡的一張臉/風格
2. 使用者選定後，才將該張圖上傳並透過 `show_reference_elements(action='create')` 建立 Reference Element 作為身分錨點（比照 Vicky Lin 第四輪做法）
3. 用該 Element 錨定，重新生成完整的訓練圖批次（六個計畫批次，見上方「計畫批次 Prompt 規劃」章節），確保所有訓練圖為同一身分
4. 使用者確認錨定後的訓練圖批次滿意後，才呼叫 `show_characters(action='train')` 執行 Soul 訓練
5. 本輪**沒有**建立 Reference Element、**沒有**呼叫 `show_characters(action='train')`，`profile.json` 未變更，訓練狀態維持 **PENDING**

---

## 2026-07-25 三次修正：改用 Seedream 4.5 重新生成 Discovery 批次

**狀態：⚠️ PENDING —— 仍是「選臉/選風格」的探索性候選圖，尚未建立 Reference Element、尚未呼叫 `show_characters(action='train')`、`profile.json` 沒有 soul_id、沒有訓練圖批次。**

### 為什麼要重做

上一輪（見上方「2026-07-25 Discovery 批次」章節）用 `soul_2`（無 soul_id 錨點）生成了 4 張候選圖，使用者檢視後判定**4 張臉根本不是同一個人**，予以退回。舊的 4 張圖已改名為 `round1_candidate_01.png`–`round1_candidate_04.png` 保留存查。

根本原因：選 `soul_2` 之前沒有先檢查本專案自己已經驗證成功的範本。`kols/iris-chen/generation_notes.md` 明確記錄了 Iris Chen 這 6 位初代 KOL 的參考圖是用 `seedream_v4_5`（Seedream 4.5）生成的，且該檔案特別註記：**同一段文字 prompt 重複生成時，Seedream 4.5 生成的臉孔一致性高到「同 prompt 生 4 張會太像，所以每批次只生 2 張」**。這與 `soul_2` 在沒有 soul_id 錨點時「每次獨立呼叫都重新想像一張不同臉」正好相反——後者正是 Coco Wu 第一輪、以及同期 Rainie Hsu、Sophia Tseng、Mia Huang、Zoe Lai 等新角色 Discovery 批次翻車的共同原因。此教訓已寫入 `README.md`〈新增 KOL 流程〉第 5 點與 `SEXY_SCENE_LIBRARY.md` 檢查清單，訂為固定規則：**Discovery／訓練圖批次一律先用 `seedream_v4_5`，只有角色已有成功訓練出的 `soul_id` 時才改用 `soul_2` + 該 soul_id**。

### 模型確認

呼叫 `models_explore(action='get', model_id='seedream_v4_5')` 確認：
- `quality`：`basic`（預設，最高 4K）或 `high`（最高約 6K）
- `aspect_ratios`：包含 `9:16`（直式人像適用）
- 無 `soul_id` 相關參數，純文字 prompt 生成

### 本輪生成參數

- 模型：`seedream_v4_5`
- `aspect_ratio`: `9:16`
- `quality`: `basic`（比照 Iris Chen 訓練圖先例，Discovery 探索階段不需要 4K/high）
- `count`: 1（4 次獨立呼叫，非同一次呼叫的 batch，因每張角度/構圖不同）
- Prompt：沿用本文件上方「核心 prompt 結構」已校準（含 89-56-86cm／E罩杯身材數字、fair porcelain-toned skin 修正、NOT narrow/sharp/almond-shaped 眼型註記）的身分描述逐字保持一致，僅替換角度/景別/姿勢細節，維持與舊 `soul_2` 批次相同的角度變化模式：正面臉部特寫／正面半身／四分之三側半身／正面全身
- 場景延續舊批次設定：宿舍素色奶油牆面、追星小卡佈告欄、書桌一角、暖色檯燈與窗光混合；穿搭統一為奶油色開襟外套＋嬰兒粉削肩小可愛（candidate_04 全身圖加上奶油色百褶迷你裙與白色過膝襪）

### Job ID 與費用

`get_cost:true` 預飛檢查：每張約 1 credit（basic quality, 9:16, 1440×2560）。生成前餘額 15.35 credits。

| 檔名 | 角度 / 景別 | Job ID | Seed |
|------|------|--------|------|
| candidate_01.png | 正面臉部特寫（front headshot） | `64cf63f0-c842-4886-88d5-907e63006e27` | 144539 |
| candidate_02.png | 正面半身（front half-body） | `ae2bce14-df07-40cc-b661-02bcbc7d1940` | 468673 |
| candidate_03.png | 四分之三側半身（3/4 half-body） | `486dbfe9-7f89-486b-bc9f-6813957ae4de` | 279915 |
| candidate_04.png | 正面全身（front full-body） | `76d297f3-0987-400e-8c02-95005e8987c2` | 722641 |

4 張皆一次生成成功，無 rate limit 或失敗重試，共花費約 4 credits。

**產出檔案**：`kols/coco-wu/images/face_reference/candidate_01.png` – `candidate_04.png`（**覆蓋了同名的舊 `soul_2` 檔案**——舊檔已在生成前改名為 `round1_candidate_01.png`–`round1_candidate_04.png`，不會被覆蓋遺失）。

### ⚠️ 誠實的臉部一致性評估（已實際目視比對 4 張圖，非假設）

用 Read 工具實際打開並比對全部 4 張圖後的結論：**這次明顯是同一個人，四張圖具備高度一致的臉部識別特徵**，具體比對如下：

- **臉型**：4 張都是圓潤的娃娃臉，臉頰飽滿度一致
- **眼睛**：4 張都是大而圓的雙眼皮眼睛、深棕色眼珠、眼型走向一致（都不是細長/上揚），符合「NOT narrow, sharp, or almond-shaped」的要求
- **鼻子/嘴唇**：鼻梁高度與嘴唇形狀（微豐滿、珊瑚橘色唇膏）在 4 張圖中辨識度一致
- **髮型**：黑棕色長波浪捲髮＋蓬鬆劉海的分線位置、捲度、髮色在 4 張圖中幾乎相同
- **梨渦/笑容**：candidate_01、candidate_03、candidate_04 微笑/大笑時梨渦位置一致；candidate_03 因為是大笑張嘴的動態表情，五官被拉開比例略有變化，但整體臉部結構（尤其是眼睛與髮際線）仍可辨認是同一人，不是換了一張臉
- **場景/服裝延續性**：4 張圖共用同一個宿舍場景（同一個追星小卡佈告欄、同一盞暖黃檯燈、同一張書桌）、同一件奶油色開襟外套與嬰兒粉小可愛，這本身雖非身分判斷依據，但強化了「這是同一次拍攝、同一個人」的視覺敘事一致性

**結論**：`seedream_v4_5` 在本輪 4 張獨立生成中確實展現了遠優於 `soul_2`（無錨點）的臉部一致性，印證了 `kols/iris-chen/generation_notes.md` 記載的模型特性。這 4 張已經是「同一人不同角度」的合格候選圖，可以進入下一步的使用者選臉流程；不像上一輪 `soul_2` 那樣是「同類型但不同人」的 4 張圖。

### ⚠️ 下一步（不可跳過，且不可自動接續）

1. 等待使用者從 4 張候選圖中挑出最喜歡的一張臉/風格
2. 使用者選定後，才將該張圖上傳並透過 `show_reference_elements(action='create')` 建立 Reference Element 作為身分錨點
3. 用該 Element 錨定，重新生成完整的訓練圖批次（六個計畫批次，見上方「計畫批次 Prompt 規劃」章節），確保所有訓練圖為同一身分
4. 使用者確認錨定後的訓練圖批次滿意後，才呼叫 `show_characters(action='train')` 執行 Soul 訓練
5. 本輪**沒有**建立 Reference Element、**沒有**呼叫 `show_characters(action='train')`，`profile.json` 未變更，訓練狀態維持 **PENDING**

---

## 2026-07-30 使用者核准候選圖，建立 Reference Element 並生成完整訓練圖批次（已生成，等待使用者確認，尚未送入 Soul 訓練）

**狀態：⚠️ 等待使用者審核 —— 尚未執行 Soul 訓練，`profile.json` 沒有 soul_id，訓練狀態維持 PENDING。**

**觸發背景**：使用者已明確表示 4 張候選圖（`candidate_01.png`–`candidate_04.png`，`seedream_v4_5` 生成，已於 2026-07-25 確認同一人）全數可接受，授權挑選其中一張作為身分錨點並建立完整訓練圖批次。同時 `SEXY_SCENE_LIBRARY.md` 新增兩條 2026-07-30 永久規則：「2. 拍攝裝置感」新增自拍前鏡頭需使用較低畫質語言（不可無腦套用 crisp/HDR）；「2b. 相機/濾鏡風格變化」新增 CCD 數位相機質感與美圖類 App 濾鏈作為部分照片的風格變化；另外「7. 自拍與他拍比例」與「8. Discovery 參考錨定圖穿搭要日常」也適用於本次批次規劃。

### 1. 錨點候選圖選定

逐一用 Read 工具目視檢視 `candidate_01.png`–`candidate_04.png` 後選定 **`candidate_01.png`（正面臉部特寫 / front headshot）** 作為身分錨點，理由：四張圖中構圖最乾淨、正面直視鏡頭、五官完整無遮擋、無動態模糊或大笑張嘴等會拉伸臉部比例的表情，是最能代表她基礎臉部特徵的一張（candidate_02 手臂遮擋部分肩頸、candidate_03 是大笑張嘴的動態表情且側身角度、candidate_04 是全身遠景臉部占比小）。

### 2. Reference Element 建立

- 上傳流程：`media_upload`（filename `coco_wu_anchor_candidate_01.png`）→ 取得 presigned URL 與 `media_id: 16464630-0d51-49e6-b4fa-39c8939be651` → `curl -X PUT` 上傳 `candidate_01.png` 原始檔案位元組（HTTP 200）→ `media_confirm(media_id, type='image')` 確認上傳完成
- `show_reference_elements(action='create', category='character', name='coco-wu-anchor-c01', medias=[{id, url}])` 建立成功
- **Element ID：`4b6c659c-786b-43de-87af-87cea3cc99dd`**（name: `coco-wu-anchor-c01`）

### 3. 模型與費用預飛檢查

- 模型：`seedream_v4_5`（唯一支援 Element embedding 且延續已驗證的臉部一致性紀錄），`aspect_ratio: 9:16`，`quality: basic`
- `get_cost:true` 預檢：每張 1 credit（basic quality, 9:16, 1440×2560）
- 生成前餘額：2774.7 credits

### 4. 內容支柱佔比對應（12 張圖，依 `content_style.md` 六大支柱權重比例分配）

| 支柱 | 權重 | 分配張數 |
|------|------|----------|
| 早晨 / 宿舍賴床 | 25% | 3 |
| 穿搭 / 今天穿什麼去上課 | 20% | 2 |
| 浴室 / 宿舍衛浴 GRWM | 15% | 2 |
| 居家 / 宿舍耍廢 | 25% | 3 |
| 飯店旅遊 / 週末出遊 | 10% | 1 |
| 健身 / 校園散步 & 羽球社 | 5% | 1 |

### 5. 產出檔案（`kols/coco-wu/images/training_v1/`）

全部使用 `<<<4b6c659c-786b-43de-87af-87cea3cc99dd>>>` 錨定同一身分，僅變化場景、姿勢、角度、穿搭、光線、濾鏡風格：

| 檔名 | 支柱 | 場景 | 視角類型 | 濾鏡/裝置變化 | Job ID |
|------|------|------|----------|----------------|--------|
| 01_morning_wake_selfie.png | 早晨賴床 | 鬧鐘剛響，床上自拍 | 自拍（前鏡頭） | 前鏡頭較軟畫質語言 | `0850d104-060f-435c-9ec8-34ff3d0d3374` |
| 02_morning_blanket_pull.png | 早晨賴床 | 室友拉棉被，兩人大笑 | 他拍（後鏡頭） | 標準，crisp | `ec40c355-1a42-489e-a6a1-f8a5843d667b` |
| 03_morning_ccd_getting_ready.png | 早晨賴床 | 床邊整理頭髮準備上課 | 他拍（室友隨手拍） | **CCD 數位相機質感** | `6c33f32c-c4c3-4944-a95e-c00f38fe3def` |
| 04_outfit_mirror_selfie.png | 穿搭 | 鏡前試穿開襟外套+百褶裙 | 自拍（鏡子/後鏡頭） | 標準，crisp（鏡面自拍例外，見下方說明） | `3f0a96ae-6ddb-42c6-8a58-3a01b8cb3a3c` |
| 05_outfit_twirl_candid.png | 穿搭 | 出門前門邊轉圈 | 他拍（室友隨手拍） | 標準，crisp | `6dece6e6-48de-48c1-b9be-1448409e9bb1` |
| 06_bathroom_grwm_meitu_selfie.png | 浴室GRWM | 刷牙後鏡前比讚 | 自拍（前鏡頭） | **美圖類 App 濾鏡** + 前鏡頭軟畫質 | `39fddb31-4c9d-4082-a298-8400b8c9fd78` |
| 07_bathroom_grwm_candid.png | 浴室GRWM | 擦保養品，室友門口抓拍 | 他拍（室友隨手拍） | 標準，crisp | `71059033-6031-40eb-8a18-3e2bd06032a7` |
| 08_home_hangout_laugh.png | 居家耍廢 | 抱抱枕大笑，室友旁拍 | 他拍（室友隨手拍） | 標準，crisp | `8402a5f4-f0be-4dab-a7ed-5317201988fe` |
| 09_home_snacks_ccd.png | 居家耍廢 | 地板吃洋芋片追劇 | 他拍（室友隨手拍） | **CCD 數位相機質感** | `ef20d655-c653-44b9-9dad-d5864119e62a` |
| 10_home_late_night_selfie.png | 居家耍廢 | 深夜棉被裡自拍 | 自拍（前鏡頭） | 前鏡頭較軟畫質語言，低光 | `50e48bf5-e407-48b2-b0cb-d320d478f9cf` |
| 11_hotel_arrival_flop.png | 飯店旅遊 | 抵達飯店倒床 | 他拍（室友隨手拍） | 標準，crisp，戶外/生活風格光線邏輯 | `190e3ae4-e945-4ac1-8ff0-5bc80eb23a8c` |
| 12_badminton_courtside_selfie.png | 健身/羽球 | 練球後場邊自拍 | 自拍（前鏡頭） | 前鏡頭較軟畫質語言 | `1cfd1104-f7dd-44b3-8305-d47fa1a0b1d8` |

**自拍/他拍比例**：4 張明確前鏡頭自拍（01、06、10、12，套用新版較軟畫質語言）+ 1 張鏡面自拍（04，鏡面自拍實務上多為後鏡頭對鏡子拍攝，畫質仍維持 crisp）+ 7 張他拍/室友隨手拍（02、03、05、07、08、09、11），符合「不能全數同一視角」的規則。
**濾鏡風格變化**：2 張 CCD 數位相機質感（03、09）+ 1 張美圖類 App 濾鏡（06），其餘 9 張維持標準 iPhone 直出質感，符合「部分照片變化，非全組套用」的規則。
**穿搭變化**：奶油色睡衣（01）、薄荷綠居家服（02）、淺紫居家服（03）、薄荷綠削肩+奶油百褶裙（04）、淺紫外套+嬰兒粉小可愛+奶油裙（05）、嬰兒粉細肩帶（06）、薄荷綠小可愛（07）、淺紫居家上衣+奶油內搭（08）、薄荷綠短T（09）、奶油細肩帶（10）、奶油上衣+牛仔短褲旅行穿搭（11）、奶油薄荷雙色運動背心（12）——對應 `content_style.md` 的奶油白/嬰兒粉/薄荷綠/淺紫丁香色調，同一件外套/單品不重複超過一次。

### 6. 費用（誠實記錄，含異常情形）

- `get_cost` 預估：12 張 × 1 credit ≈ 12 credits
- **實際情形明顯偏高**：生成前餘額 2774.7 credits，全部生成流程結束後餘額 **2724.7 credits**，實際共扣款 **50 credits**，遠高於預估的 12 credits
- 用 `transactions` 核對本次生成時間窗（2026-07-30 09:49:19–09:55:51 UTC）內共有 **50–51 筆 `Seedream 4.5 -1 credit`** 扣款紀錄，但只成功取得 **12 個**可下載結果的 job（見上表）
- 生成過程中共遇到約 8–9 次 `rate_limit_reached (429)` 工具層級錯誤（ultra 方案並發上限），每次都以單張重試後成功；但 `transactions` 顯示的扣款筆數（50–51 筆）遠多於「12 次成功 + 8–9 次失敗重試」的呼叫總數（約 20 次上下），代表**部分回傳 429 錯誤給呼叫端的請求，實際上仍在伺服器端被計費**——這與 `kols/vicky-lin/generation_notes.md` 記載的 Soul 訓練「呼叫失敗但仍計費」異常情形屬於同一類問題，這次確認同樣的現象也發生在 `generate_image`（不只是 `show_characters(action='train')`）
- 誠實結論：本輪訓練圖批次的**實際成本是 50 credits**，不是天真估計的 12 credits；多出的約 38 credits 對應到我們沒有拿到任何可用產出的失敗/幽靈請求。餘額仍然充足（2724.7 credits，ultra 方案），不影響後續操作，但記錄於此供未來核對，並提醒：`generate_image` 遇到 429 時的重試不應被視為「零成本重試」

### 7. 誠實的視覺一致性評估（已用 Read 工具實際目視檢查 7 張跨支柱/跨視角圖，非假設）

實際打開並比對 `01`、`02`、`04`、`06`、`09`、`11`、`12` 共 7 張圖後的結論：

**(a) 身分是否與錨點圖一致** —— **整體高度一致，Element 錨定確實有效**：圓潤娃娃臉、明顯梨渦、大而圓的眼睛、黑棕色長波浪捲髮＋蓬鬆劉海、甜美五官在 7 張圖中都能清楚辨認是同一人，包括在遠景全身動態抓拍（11 飯店flop）與運動流汗場景（12 羽球）中也維持一致。**唯一的例外**：06（浴室美圖濾鏡自拍）套用美圖 App 濾鏡後，臉頰比例讀起來稍微更瘦削、嘴唇顏色偏淡粉而非其他圖的珊瑚紅唇色，是可辨認但有輕微身分漂移的一張——這是美圖濾鏡本身「磨皮/五官微調」效果的預期副作用，不是 Element 錨定失效，但如果之後要送 Soul 訓練，建議評估是否要保留這張或替換成無濾鏡版本以確保訓練集身分純度。
另外要誠實指出：02（室友拉棉被）與 09（地板吃零食）兩張圖裡，作為配角出現的「室友」因為 prompt 沒有給她獨立的外型描述，長相與 Coco 本人相當接近（同樣的長黑髮、圓臉），畫面裡出現兩張很相似的臉。這不影響 Coco 本人的身分錨定（她本人前景臉孔仍清楚吻合錨點），但如果這兩張要當作最終素材使用，建議之後生成室友角色時额外加一兩個區隔特徵（例如不同髮型/瀏海）避免「像雙胞胎」的觀感。

**(b) 自拍是否讀起來比他拍更軟/畫質較低** —— **部分成功，不是全部**：01（床上自拍）與 06（浴室美圖自拍）確實呈現比他拍圖更柔和、對比略低的畫面質感，跟 02、11 等他拍圖的銳利對比有可辨識的差異。但 **12（羽球場邊自拍）視覺上幾乎跟他拍圖一樣銳利清晰**，前鏡頭「較軟畫質」的文字指令在這張沒有被模型明顯體現出來——這是文字提示對最終渲染影響力有限的已知局限，誠實記錄，不宜宣稱「規則 100% 生效」。

**(c) 場景/穿搭是否真的有變化，對應內容支柱** —— **符合**：12 張橫跨全部六大支柱且比例對應權重，場景從床上、浴室、衣櫃鏡前、宿舍地板、飯店房間到體育館球場都有具體且不重複的生活雜物細節（追星小卡佈告欄、充電線、洋芋片包裝袋、行李箱、羽球拍與羽球筒等），穿搭 12 張沒有重複同一件單品，奶油/嬰兒粉/薄荷綠/淺紫丁香色調有落實。CCD 濾鏡（03、09）效果偏含蓄，色調略為柔和降低對比，但沒有達到「明顯復古數位相機」的強烈風格差異，是可以接受但不算搶眼的一種變化；美圖濾鏡（06）風格辨識度較高，皮膚更均勻明亮、對焦更柔和，符合 prompt 描述方向。

**總結**：Element 錨定機制在這一輪 12 張跨場景/跨支柱訓練圖上證實有效，身分一致性遠優於先前 `soul_2` 無錨點的獨立生成結果，可視為合格的訓練圖候選批次；但自拍/他拍畫質差異與 CCD 濾鏡強度這兩項新規則的實際生成效果只能算「部分達成」，並非每張都精準體現文字指令，建議使用者審核時特別留意 06（濾鏡導致的輕微身分漂移）與 12（自拍畫質差異不明顯）這兩張的可用性。

### 8. ✅ 使用者核准並送出 Soul 訓練（2026-07-30）

使用者明確表示 12 張訓練圖皆可接受，並授權直接送出訓練（「我覺得這四位都可以送去訓練...就先這樣送出訓練。最主要是要先輔助他們的臉。」），不需先處理 06/12 的細節瑕疵。呼叫 `show_characters(action='train', name='Coco Wu', images=[...12張訓練圖的 media_id])`，**第一次呼叫即成功受理**，取得 `soul_id: cf7045dc-4e69-4c56-9621-aa8c40bf39b4`，`raw_status: queued`。`profile.json` 已補上 `ai_assets.training_images_v1.soul_training` 欄位。

**2026-07-31 確認完成**：透過 `show_characters(action='train')`（呼叫 Sophia Tseng 訓練時的 `items` 列表副作用）確認 Coco Wu 的 `status: ready`、`raw_status: completed`。`profile.json`、`README.md`、`KOL_TRAINING_SOP.md` 已同步更新為訓練完成狀態，可用 `model: soul_2` + 此 soul_id 生成後續正式內容。

---

## 下一步（待執行）

1. ~~生成 4 張獨立候選圖供使用者選臉~~ 已完成（2026-07-25，`seedream_v4_5`，確認同一人）
2. ~~等待使用者從候選圖選定身分錨點~~ 已完成：使用者確認 4 張皆可接受，授權任選一張——已選定 `candidate_01.png`
3. ~~建立 Reference Element 並生成完整訓練圖批次~~ 已完成（2026-07-30，`element_id: 4b6c659c-786b-43de-87af-87cea3cc99dd`，12 張跨六大支柱訓練圖，見上方章節）
4. ~~等待使用者審核 12 張訓練圖並明確確認滿意~~ 已完成（2026-07-30，使用者核准並授權直接送訓練）
5. ~~執行 `show_characters(action='train')`，記錄 soul_id~~ 已完成（`soul_id: cf7045dc-4e69-4c56-9621-aa8c40bf39b4`，2026-07-31 確認 `status: ready`）
6. 影片生成流程（模型選擇、prompt 模板、剪輯節奏對應）待圖片流程確認後另行規劃，目前尚未展開

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
| Soul ID | `cf7045dc-4e69-4c56-9621-aa8c40bf39b4` |
| 場景 | 夜市主通道（手持珍奶／章魚燒攤前） |
| 穿搭（A/B 共用） | 奶油色針織開襟 + 淺粉細肩帶內搭 + 薄荷綠百褶短裙 + 白帆布托特包 + 髮夾 |
| Job ID（A） | `1d47a307-96cf-45e9-94c5-845536badecb` |
| Job ID（B） | `33440242-af5d-4754-8762-ba897e9e83b9` |
| 評定 | ✅ 通過 |

夜市人流密度、層疊 LED 價目燈箱、塑膠椅、濕反光地面都到位，背景路人與攤商多人且全部處理得當。B 張加入章魚燒鐵板火光作為第二光源，同穿搭延續成功。**落差 1**：A 張構圖消失點正中央、過度對稱，是典型 AI 構圖 tell，之後應在 prompt 指定偏離中心。**落差 2**：臉齡讀起來略高於 20 歲設定。

### 本批次共同結論（全 7 位角色適用）

- ✅ **背景路人：14/14 全部成功，且無任何配角撞臉主角。** 四條件措辭（背向／不看鏡頭／失焦／外型與主角區隔）有效，成本為零。原「預設只有本人入鏡」規則對公共場景已反轉。
- ✅ **同穿搭一日敘事：7/7 成功。** 服裝配件完整延續且狀態自然演變。
- ⚠️ **地點：環境元素清單成功，點名地標全部失敗。** 「愛河」生出墨爾本天際線、「台北 101」生出通用摩天樓群。
- ⚠️ **中文招牌全部亂碼**（與競品同等程度），本批次接受此取捨。
- 🔴 **打光尚未套用新公式。** 本批次仍使用舊的「品質形容詞」寫法（`crisp`／`high dynamic range`／`well-exposed`）。2026-08-05 拆解競品後已改寫 `SEXY_SCENE_LIBRARY.md` 第 3 點為五段式物理光線公式，**下一批次應以驗證該公式為首要目標**。
