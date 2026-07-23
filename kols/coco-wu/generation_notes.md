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

### 計畫批次 1 — 宿舍房間早晨（Dorm Room Morning）

**場景構想**：早八鬧鐘剛響，她還窩在宿舍單人床上，頭髮亂糟糟，棉被拉到胸口，宿舍窗簾縫透進晨光。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, round baby face with soft dimples when smiling, small rounded chin, big round sleepy eyes, dark brown long wavy hair messy from sleep, petite 158cm frame with soft curvy figure, lying in a dorm room single bed with rumpled white bedding, morning light filtering through dorm curtains, wearing an oversized soft pajama top, drowsy half-smile toward camera, slightly overhead angle from bedside, soft warm morning light, film grain, candid lifestyle photo, soft pastel warm tones, shot on 35mm, phone-camera casual feel, Instagram style
```

---

### 計畫批次 2 — 校園走路 3/4 身（Campus Walk, Three-Quarter Shot）

**場景構想**：走在校園步道上準備去上課，敞開穿的針織開襟外套配百褶裙與過膝襪，陽光普通的白天校園日常感。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, round baby face with soft dimples when smiling, sweet cute features, big round bright eyes, dark brown long wavy hair with wispy bangs half tied up, petite 158cm frame with soft curvy figure, walking on a university campus pathway, wearing an open knit cardigan over a camisole top, pleated mini skirt, over-the-knee socks, three-quarter angle candid walking shot, natural daytime campus sunlight, film grain, candid lifestyle photo, soft pastel warm tones, shot on 35mm, phone-camera casual feel, Instagram style
```

---

### 計畫批次 3 — 宿舍衛浴 GRWM（Dorm Bathroom Get-Ready-With-Me）

**場景構想**：宿舍公共衛浴間鏡前刷牙洗臉，鏡子偏小、燈光普通，帶點真實宿舍質感而非精緻美妝棚拍。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, round baby face with soft dimples when smiling, small rounded chin, big round eyes, dark brown long wavy hair clipped up loosely, petite 158cm frame with soft curvy figure, standing at a small dorm bathroom mirror brushing teeth, wearing a simple sleep tank top, playful expression making a face at the mirror, close-up mirror reflection angle, plain dorm bathroom lighting, film grain, candid lifestyle photo, soft pastel warm tones, shot on 35mm, phone-camera casual feel, Instagram style
```

---

### 計畫批次 4 — 室友聚會 / 宿舍耍廢（Roommate Hangout in Dorm）

**場景構想**：晚自習後窩在宿舍床上跟室友聊天耍廢，抱著抱枕大笑，書桌上堆著課本和珍奶杯，宿舍檯燈暖黃光。

**草稿 Prompt**：
```
20-year-old Taiwanese university student, legal adult, round baby face with soft dimples when smiling, big round bright eyes, dark brown long wavy hair down and slightly messy, petite 158cm frame with soft curvy figure, sitting on a dorm bed hugging a pillow laughing with a roommate off-frame, wearing an oversized soft home outfit, relaxed candid laughing expression, casual angle as if a roommate took the photo, warm evening dorm lamp light, cluttered dorm desk with textbooks and a bubble tea cup visible in background, film grain, candid lifestyle photo, soft pastel warm tones, shot on 35mm, phone-camera casual feel, Instagram style
```

---

## 下一步（待執行）

實際生成執行時需依序記錄：使用的平台/模型、實際生成的 job ID、選定的訓練圖、Soul 訓練狀態與完成日期。本文件目前不包含這些內容，待生成流程實際跑過後再補充於本檔案或另立記錄章節。
