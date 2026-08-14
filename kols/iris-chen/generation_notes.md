# Iris Chen — AI 生成記錄

> 只記錄確認有效的版本和步驟。錯誤嘗試已略去。

---

## 人物設定

| 欄位 | 設定 |
|------|------|
| 名字 | Iris Chen（陳芯語） |
| 年齡 | 22歲 |
| 國籍 | 台灣 |
| 臉型參考 | 熊熊（台灣藝人）：圓臉、大雙眼皮、精緻鼻梁、飽滿嘴唇、小下巴 |
| 身材 | 嬌小前凸後翹，hourglass，胸部飽滿、腰細 |
| 穿衣風格 | Hot girl casual：平口上衣、細肩帶、mini skirt、黑色短褲、crop hoodie |
| 眼鏡 | 無 |
| 髮型 | 黑色直髮自然放下 |

---

## 訓練圖生成流程（training_v1）

### 平台與模型

- **平台**：Higgsfield.ai
- **模型**：Seedream 4.5（`seedream_v4_5`）
- **為何選 Seedream**：Recraft V4.1 對亞洲臉孔效果差（生成路人臉），Seedream 4.5 預設就能生成網紅等級的亞洲美女臉

### 核心 prompt 結構

```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

### 批次設定

- 每批次生成 **2張**（不用4張：同場景同 prompt 下4張差異太小）
- 共4個場景，總計14張

---

## 各批次 Prompt 記錄

### 批次 1 — 台北街頭 3/4 身（4張）

```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, standing on Taipei street, wearing white spaghetti strap crop top and high-waist denim mini skirt, slight smile looking at camera, 3/4 angle, natural daylight, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

### 批次 2 — 咖啡廳窗邊正面近景（4張）

```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, sitting by cafe window, wearing light pink tube top, looking at camera with warm natural smile, front view close-up, golden afternoon light through window, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

### 批次 3 — 公園黃金時段全身（4張）

```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, standing in park during golden hour, wearing black mini shorts and fitted white crop hoodie, full body shot, looking back at camera over shoulder, warm golden backlight through trees, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

### 批次 4 — 車內自拍視角（2張）

```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, close-up front-facing selfie shot, slightly overhead angle looking down at camera, natural relaxed smile, sitting in car interior background, wearing casual black spaghetti strap top, warm sunny light, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

**⚠️ 自拍視角重要規則**：prompt 描述的是照片本身的輸出視角，不是描述「她在拍自拍」的動作。
- ❌ 錯誤：`taking a selfie holding phone up` → 會生成第三人視角、手機出現在畫面中
- ✅ 正確：`close-up front-facing selfie shot, slightly overhead angle looking down at camera, looks like a photo taken by her own phone front camera`

---

## Higgsfield 操作方式（localStorage 法）

在 Higgsfield 更換 prompt 最可靠的方式：

```javascript
var raw = localStorage.getItem('hf:image-form-upd');
var data = JSON.parse(raw);
data.prompt = "NEW PROMPT HERE";
data.lastSelectedModel = "seedream_v4_5";
localStorage.setItem('hf:image-form-upd', JSON.stringify(data));
// 然後導航至：https://higgsfield.ai/ai/image?model=seedream_v4_5
```

---

## 下一步：Soul 訓練

1. 前往 Higgsfield.ai → Soul 訓練
2. 上傳這14張訓練圖
3. 等待訓練完成（Soul 2.0）
4. 用訓練好的 Soul 角色生成後續大量生活照

訓練圖路徑：`kols/iris-chen/images/training_v1/`

---

## 模型選擇結論

| 模型 | 結果 |
|------|------|
| Recraft V4.1 | ❌ 亞洲臉孔效果差，生成路人臉，不適合 |
| Seedream 4.5 | ✅ 預設生成網紅級亞洲美女臉，照片風格自然 |

---

## 照片風格原則

生成目標是「網紅在 Instagram 發的生活照」，不是「雜誌大片」：
- 要有 film grain / 35mm 感
- 場景要自然（街頭、咖啡廳、公園、車內）
- 不要過度打光或過於精緻的構圖
- 身材曲線要明顯但風格要 casual，不是刻意擺姿勢

---

## 親密場景模板（2026-07 新增）

> 方向更新後的新場景類型：臥室早晨、浴室鏡前、居家沙發、飯店房間。

### 核心 Prompt 基礎結構（不變）

```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure, 87cm bust, D cup, 58cm waist, 90cm hips, black silky straight hair naturally down, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

**2026-07-25 新增：身材數字 + 風格參考** — 核心 prompt 已補上明確身材數字（87cm bust, D cup, 58cm waist, 90cm hips，取自 `profile.json` 的 `identity.appearance.measurements`），取代單純用「curvy/hourglass」等形容詞，避免生成結果與人設數字對不上（此問題在 Vicky Lin 的用戶回饋中被發現）。未來新批次 prompt 請沿用上面帶數字的版本。另外，光源指示請參考 `SEXY_SCENE_LIBRARY.md` 「光源」章節的 2026-07-25 修正：Iris 的內容以台北戶外/街頭/咖啡廳生活場景為主，屬於新版「自然光 + 淺景深 + 清晰高畫質」配方（而非舊版刻意不完美/混合光源的室內親密場景配方），寫新 prompt 時請對應套用。此為前瞻性補充，不影響已批准的訓練圖與影片紀錄。

---

### 場景 1 — 臥室早晨（Bedroom Morning）

**氛圍**：剛睡醒，床上，台北早晨的窗光，頭髮散亂，被子，自然素顏。

**Prompt（圖片）**：
```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair loosely disheveled from sleep, lying in bed on white cotton bedding, morning light filtering through sheer curtains, wearing thin white cotton camisole sleep top, slightly drowsy gaze toward camera, slightly overhead angle looking down, soft warm morning sunlight, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Close-up of her face on white pillow, eyes slowly opening, morning light filtering through curtains, hair disheveled from sleep.
Shot 2: She slowly sits up in bed, white bedding sliding, stretching arms slightly, drowsy expression.
Shot 3: Close-up of her hand reaching for phone on bedside table, morning light casting soft shadows.
Shot 4: She glances at camera with a sleepy half-smile, still nestled in white bedding.
Shot on iPhone, warm soft grain, warm faded tones, no over-sharpening, natural lighting, stable camera, feels like a real person filmed this.
```

**參數**：
```python
model = "cinematic_studio_video_v2"
multi_shots = True
multi_shot_mode = "auto"
genre = "intimate"
mode = "pro"
sound = "on"
aspect_ratio = "9:16"
duration = 12
```

---

### 場景 2 — 浴室鏡前（Bathroom Mirror）

**氛圍**：洗完澡，浴巾，濕髮，浴室鏡前，霧氣，素顏。

**Prompt（圖片）**：
```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black hair wet and slightly damp from shower, standing in front of bathroom mirror, wearing white towel wrapped around body, slight steam on mirror edges, looking at reflection with relaxed natural expression, bathroom warm lighting, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Bathroom mirror reflection showing her in white towel, damp black hair, wiping mirror condensation with hand.
Shot 2: She tilts head slightly, running fingers through wet hair, looking at her reflection.
Shot 3: Close-up of her face in mirror, natural skin with slight post-shower flush, no makeup.
Shot 4: She glances from mirror to camera, relaxed soft expression, bathroom warm light.
Shot on iPhone, warm soft grain, warm faded tones, no over-sharpening, natural bathroom lighting, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

### 場景 3 — 沙發居家（Sofa/Home Lounging）

**氛圍**：家裡最放鬆的狀態，沙發上，家居服，台北公寓的下午光。

**Prompt（圖片）**：
```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, sitting curled up on sofa in Taipei apartment, wearing black cotton short shorts and fitted white crop tee, phone in hand, relaxed casual pose, warm afternoon light from window, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Wide shot of her curled up on sofa in cozy Taipei apartment, afternoon light through window, scrolling phone.
Shot 2: Medium shot of her pulling knees to chest, glancing up from phone toward camera.
Shot 3: Close-up of her face and shoulders, warm afternoon light on skin, relaxed expression.
Shot 4: She shifts slightly, tucking legs under, looking out the window, unaware of camera.
Shot on iPhone, warm soft grain, warm faded tones, no over-sharpening, natural afternoon lighting, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

### 場景 4 — 飯店房間（Hotel Room）

**氛圍**：飯店床，飯店浴室，落地窗，旅行的陌生感。台灣出發到日本或其他城市。

**Prompt（圖片）**：
```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, sitting on hotel bed with crisp white bedding, city view through floor-to-ceiling window, wearing black spaghetti strap pajama top, looking toward window with relaxed expression, hotel room warm lighting mixed with city glow, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Wide shot of hotel room, she sits on white bed, city view through large window behind her, golden evening light.
Shot 2: She walks to floor-to-ceiling window, looks out at city below, back to camera.
Shot 3: Close-up of her face reflected in dark window glass, city lights behind her reflection.
Shot 4: She turns from window to look at camera, soft hotel room light on her face.
Shot on iPhone, warm soft grain, warm faded tones, no over-sharpening, hotel ambient lighting, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

## 舞蹈影片記錄（2026-07-03）

### Soul ID
`5fe3b6ba-1277-4822-9141-fb06eb3b93a0`

### Start Frame 方法

所有舞蹈影片使用以下步驟生成 start frame：
1. `generate_image(model="soul_2", soul_id="5fe3b6ba-1277-4822-9141-fb06eb3b93a0", ...)`
2. 從回傳的 `rawUrl` 呼叫 `media_import_url` 取得 `image_media_id`
3. 傳入 `seedance_2_0` 的 `start_image` 參數

**⚠️ 構圖規則（舞蹈專用）**：Start frame 必須是 **THREE QUARTER SHOT（mid-thigh up, no shoes shown）**，避免影片在膝蓋處截斷。

### 服裝與 Prompt 記錄

#### 版本 1–2：黑色 crop top + 騎車短褲

**Start frame prompt**（供參考）：
```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes,
delicate high nose bridge, soft full lips, small defined chin, glowing skin,
petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down,
standing in confident pose ready to dance,
wearing black crop top and high-waist black biker shorts,
THREE QUARTER SHOT, mid-thigh up, no shoes shown,
plain white studio background,
film grain, candid lifestyle photo, warm tones, shot on 35mm
```

**Dance video prompt**：
```
22-year-old Taiwanese girl, petite curvy hourglass figure with full chest and slim waist,
black silky straight hair naturally down,
wearing black crop top and high-waist black biker shorts,
THREE QUARTER BODY SHOT, mid-thigh up, no shoes shown,
chest bounce and jiggle physics,
energetic hip-hop dance, body rolling, hip sway, powerful rhythmic movement,
synced to Vietnamese drum beat, dynamic energy,
plain white studio background,
synced to the music beat and rhythm, dynamic dance movement, confident sensual energy,
shot on iPhone, natural lighting, warm tones
```

#### 版本 3：淡藍色 V 領洋裝

**音樂**：Sugar on my tongue  
**Dance video prompt（服裝部分）**：`light blue V-neck mini dress`  
**舞蹈風格**：fluid body wave, sensual groove, dress flowing with movement

### 已生成影片清單

| 版本 | 時長 | 服裝 | 音樂 | Job ID | generate_audio | 狀態 |
|------|------|------|------|--------|---------------|------|
| dance_v1 | 10s | 黑色 crop top + 騎車短褲 | 越南鼓 | `1b0aee3d` | false | ✅ 批准 |
| dance_v2 | 15s | 黑色 crop top + 騎車短褲 | 越南鼓 | `1b767b3b` | false | ✅ 保留 |
| dance_v3 | 15s | 淡藍色 V 領洋裝 | Sugar on my tongue | `3d3ac1b2` | false | ✅ 批准 |
| dance_v4 | 15s | 淡藍色 V 領洋裝（cl3） | AI 生成（Veo 2 / seedance generate_audio:true 測試） | `dc8c2f4d` | **true（測試用）** | 臉部鎖定差，卡點無改善 |
| dance_v5 | 15s | 淡藍色 V 領洋裝（cl3） | AI 生成（第二次測試，用已驗證 start_image `7cc36b0b`） | `1d60614a` | **true（測試用）** | 卡點效果與 false 相同，無改善 |

### ⚠️ generate_audio: true 測試結論（2026-07-06）

**測試目的**：讓 seedance 自行生成音樂，期望 AI 音樂與舞蹈動作同步生成能讓卡點更精準。

**測試結果**：
- 卡點效果與上傳音樂 + generate_audio: false 版本相同，沒有任何改善
- 第一次測試（job `dc8c2f4d`）：臉部鎖定品質明顯下降（臉型不一致）
- 第二次測試（job `1d60614a`）：改用已驗證 start_image（`7cc36b0b`），臉部好一點，但卡點仍無改善

**結論：永遠使用上傳的熱門音樂 + generate_audio: false**。AI 生成音樂額外缺點是無法控制歌曲，無法在後製換歌。

其他本 session 影片（非舞蹈）：

| 版本 | 場景 | 模型 | Job ID | 狀態 |
|------|------|------|--------|------|
| 浴室鏡前 v1 | 浴室鏡前，start_image: `89010b47` | kling3_0 | `a6231909` | ✅ 保留 |
| 浴室+音樂 | 浴室場景 | kling3_0 | `5bcbb94b` | 待確認 |

---

## 日常自拍影片記錄（2026-07-07）

> 方向：男性受眾，手機自拍感，展示身材曲線和乳溝，非廣告感。
> 模型：`kling3_0`（單鏡頭，臉部鎖定）
> 完整 SOP 見 `DAILY_VIDEO_SOP.md`

### Start Frame（日常服裝）

| Job ID | 說明 | 已選 | Media ID |
|--------|------|------|----------|
| `98d13de0` | 浴室，黑色細肩帶背心，俯角自拍，微微低頭 | ✅ 已選 | `b8078a7d` |
| `8e23ac81` | 同場景，第二張備選 | — | — |

**Start Frame Prompt（已驗證）**：
```
24-year-old Taiwanese woman, strikingly beautiful face, double eyelids, delicate features,
long straight black hair, fit slim figure with natural curves,
standing in bathroom, wearing black spaghetti strap tank top no bra,
slightly tilting head down looking up at camera with soft smile,
phone selfie angle from slightly above angled down toward face and chest,
natural cleavage visible from above angle, soft warm bathroom light,
candid self-portrait feel, shot on iPhone front camera,
close crop from collarbone to top of head, warm tones, film grain
```

### 日常影片

| 版本 | 場景 | 服裝 | Job ID | 模型 | 狀態 |
|------|------|------|--------|------|------|
| daily_v1 | 浴室手機俯角自拍，微微低頭展示乳溝 | 黑色細肩帶背心 | `b68ac46c` | kling3_0 | ✅ 批准 |

**影片 Prompt（已驗證）**：
```
24-year-old Taiwanese woman, strikingly beautiful face, double eyelids, long straight black hair,
fit slim figure with natural curves,
standing in bathroom, wearing black spaghetti strap tank top no bra,
holding phone selfie slightly above looking down at camera with soft smile,
phone selfie angle from above showing face and natural cleavage, slightly tilting head,
bathroom background with warm soft lighting,
single continuous shot, casual selfie feel, warm tones
```

**參數**：
```python
model = "kling3_0"
medias = [{"role": "start_image", "value": "b8078a7d"}]
sound = "on"
aspect_ratio = "9:16"
duration = 10
```

---

## 影片生成記錄與規則（2026-06-30）

### 使用模型

| 模型 | 特性 | 適用場景 |
|------|------|---------|
| `kling3_0` | 臉部鎖定（start_image），單鏡頭，支援 sound:on | 親密場景影片 |
| `seedance_2_0` | 身份一致性最強（start_image + audio_references），單鏡頭 | **舞蹈影片（首選）**、近景情緒 |
| `cinematic_studio_video_v2` | 原生 multi-shot，鏡頭切換自然（臉部可能漂移） | 需要多鏡頭剪輯感的日常內容 ✅ 首選 |

### 測試結果（咖啡廳場景，`cafe_test_v1`）

| 版本 | 模型 | 時長 | 解析度 | 評價 | 檔案 |
|------|------|------|--------|------|------|
| v1 | seedance_2_0 | 8s | 720p | 普通。內容太短，動作單一，AI 銳化感重 | `v1_seedance_8s_720p.mp4` |
| v2 | seedance_2_0 | 12s | 480p | 不錯，保留。自然感提升，但 480p 畫質太低 | `v2_seedance_12s_480p.mp4` |
| v3 | cinematic_studio_video_v2 | 12s | 720p | **最佳。** 多鏡頭剪切自然，有真實影片感 | `v3_cinematic_multishot_12s_720p.mp4` |

**Start frame 圖片**：`images/video_startframes_v1/frame01_cafe_seated.png`（Soul V2，job `b596e95e`）

### 影片生成注意事項（從測試中學到）

**模型參數規則**

1. **`cinematic_studio_video_v2` 的 multi-shot 必須用 `auto` 模式**
   - `multi_shot_mode: custom` + 空白 `multi_prompt` 會導致任務卡死無法完成
   - 正確做法：`multi_shots: true, multi_shot_mode: auto`，把各鏡頭描述寫進主 prompt

2. **解析度**：統一用 **720p**
   - 480p 畫質太低（現代手機不會只有 480p）
   - 「手機感」靠 prompt 關鍵詞達成，不靠降解析度

**Prompt 關鍵詞規則**

3. **要加入的手機感關鍵詞**（讓影片不像 AI 棚拍）：
   `shot on iPhone, warm soft grain, warm faded tones, no over-sharpening, natural lighting, feels like a real person filmed this`

4. **禁止加入鏡頭晃動關鍵詞**：
   - ❌ `handheld casual filming, natural slight camera movement, NOT tripod perfect, motion blur`
   - 這些關鍵詞會產生鏡頭晃動感，不符合需求
   - ✅ 鏡頭要穩定，不要有任何 camera shake

5. **內容要有完整敘事**，不能只描述一個動作：
   - ❌ 錯誤：`she picks up coffee cup and takes a sip`（太短，8 秒就結束）
   - ✅ 正確：描述 3–4 個連續動作，有起伏（如：看手機→抬頭→喝咖啡→望窗外）

6. **時長**：日常內容影片建議 **12 秒**，最短不低於 10 秒

### 最佳 Prompt 模板（cinematic_studio_video_v2）

```
Shot 1: [場景進入動作，全身或中景]
Shot 2: [主要行為，中景]
Shot 3: [特寫細節，手/道具/表情]
Shot 4: [收尾情緒鏡頭，側臉或望遠]
Shot on iPhone, warm soft grain, warm faded tones, no over-sharpening,
natural lighting, stable camera, feels like a real person filmed this.
```

```python
# 對應 API 參數
model = "cinematic_studio_video_v2"
multi_shots = True
multi_shot_mode = "auto"
genre = "intimate"
mode = "pro"
sound = "on"
aspect_ratio = "9:16"
duration = 12
resolution = "720p"  # cinematic v2 不直接支援此參數，走預設
```

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
| Soul ID | `5fe3b6ba-1277-4822-9141-fb06eb3b93a0` |
| 場景 | 台北老公寓巷弄（芒果冰店外／巷內回眸） |
| 穿搭（A/B 共用） | 白色羅紋細肩帶背心 + 淺藍丹寧短裙 + 白色低筒球鞋 + 米色小肩包 |
| Job ID（A） | `b7f5d29c-9e39-4b97-8bbb-9ff6b619d6bc` |
| Job ID（B） | `7e57ab06-5aed-454f-ae61-3410fef19d1e` |
| 評定 | ✅ 通過 |

巷弄質感非常強（鏽蝕鐵窗花、糾纏電線、手寫招牌、緊貼牆邊的機車、冷氣滴水痕）。背景路人 2–3 人全部背向、失焦、無撞臉。A/B 兩張服裝配件完整延續，B 張改為午後低斜陽、長影，讀起來確實是同一天稍晚。**唯一落差**：prompt 寫「芒果剉冰」，生成出來是叉在竹籤上的炸物——道具指定未被吃到，但不影響整體可用性。

### 本批次共同結論（全 7 位角色適用）

- ✅ **背景路人：14/14 全部成功，且無任何配角撞臉主角。** 四條件措辭（背向／不看鏡頭／失焦／外型與主角區隔）有效，成本為零。原「預設只有本人入鏡」規則對公共場景已反轉。
- ✅ **同穿搭一日敘事：7/7 成功。** 服裝配件完整延續且狀態自然演變。
- ⚠️ **地點：環境元素清單成功，點名地標全部失敗。** 「愛河」生出墨爾本天際線、「台北 101」生出通用摩天樓群。
- ⚠️ **中文招牌全部亂碼**（與競品同等程度），本批次接受此取捨。
- 🔴 **打光尚未套用新公式。** 本批次仍使用舊的「品質形容詞」寫法（`crisp`／`high dynamic range`／`well-exposed`）。2026-08-05 拆解競品後已改寫 `SEXY_SCENE_LIBRARY.md` 第 3 點為五段式物理光線公式，**下一批次應以驗證該公式為首要目標**。

---

## 2026-08-07 R6 舞蹈克隆完整跑完 Step 1–8（動作驅動複製法 Method B）

**背景**：舞蹈批次分配（見 `DANCE_CLONE_SOP.md`、GitHub Issue #3）R6 分配給 Iris Chen。驅動片：`https://www.instagram.com/reel/DKBwq88xaOG/`（黑色蕾絲吊帶睡裙手勢舞，室內純色背景）。Step 1–4（下載裁剪、Performance/Emotion 分析、起始畫面單張生成）已於同日較早完成，`start_frame.png` 已核准。

### Step 5：Motion Control（兩種 `scene_control` 對照）

- `image_id`: `af777fa3-9f14-400c-b336-fb19f2d88dfc`，`motion_video_id`: `7778c399-d8d0-41cb-9e83-0fcd24f5f246`
- **`scene_control: "image"`**（原版）：job `01435d5c-5b9e-4b53-8b30-feeb4f815bbb`，750×1400 輸入、輸出 1072×1936、30fps、~9.87s，✅ 一次成功，花費 27 credit
- **`scene_control: "video"`**（背景動態實驗，見下方「背景動態問題」）：連續兩次嘗試皆失敗——第一次 job `03fa4b5c` 狀態 `failed`（無錯誤訊息），重跑一次 job `f1558de2` 狀態 `nsfw`（明確內容審核標記）。**兩次均全額退款，零淨成本**。同一張起始畫面用 `image` 模式完全正常，只有 `video` 模式被標記，判斷是「合成到真實街景/室內真實背景」讓畫面更接近真實拍攝，疑似跟本批的性感貼身穿搭組合更容易觸發審核。Yuna Kim R7 做了同樣的對照測試，結果同樣失敗（見其 `generation_notes.md`），確認這是 `scene_control: "video"` 在目前這批穿搭尺度下的結構性問題，非單一角色個案，**已放棄這條路線**。

### 背景動態問題與後製解決方案

使用者發現 `scene_control: "image"` 模式的背景完全靜止，逐幀比對跟真人拍攝有落差（像把人 P 在一張照片前面）。嘗試用 `scene_control: "video"` 借用驅動片真實背景動態，但如上所述被內容審核擋下。改用**零額外 credit 的本機後製方案**：對 `image` 模式的最終輸出做全幀緩慢漂移平移（`ffmpeg` `crop` 濾鏡搭配 `18*sin(2*PI*t/11)` / `10*cos(2*PI*t/16)` 兩個不同週期的正弦位移，模擬手持呼吸感），角色動作/表情不做任何更動。**使用者比對原版與後製版後認為差異不大，但同意直接採用後製版當正式版**，不再追加疊圖等更複雜的處理（例如燈飾閃爍）——本輪場景是室內純色背景，本身就沒有風吹草動可模擬，後製主要意義是打破絕對靜止感。

### Step 6：手動混音

`scene_control: "image"` 原始輸出無聲（純 h264 視訊流），用 `ffmpeg -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest` 把 Step 2 抽出的 `driver_audio.m4a` 蓋上後製漂移處理後的無聲畫面，輸出 `iris_dance_clone_r6_ig_reel.mp4`（1072×1936、30fps、~9.87s，含視訊+音訊雙軌）。

### Step 7：授權與發佈限制檢查

- **驅動動作**：來自第三方 Instagram 創作者，僅供內部方法驗證；對外發佈前需評估重現程度
- **配樂**：驅動片原始配樂，**未取得商用授權**，正式發佈前必須替換
- **背景**：最終採用 `scene_control: "image"`（+後製漂移），未借用驅動片真實場景，不涉及第三方場景識別性問題
- **素材存放**：驅動片原始檔僅存本機工作資料夾，未存入本 repo

### Step 8：QA 檢核

已用 Read 工具目視抽幀比對後製版（`f_01`/`f_03` 對應約 0s／3s）：身分一致、手部無明顯崩壞、後製漂移未裁到角色肢體或造成明顯抖動/鬼影。背景動態評定為「打破靜止感的攝影機微動」，非真實環境動態，記錄在案，使用者已審閱並核准接受。

### 產出檔案

- `kols/iris-chen/images/dance_clone_r6/start_frame.png`（已核准起始畫面）
- `kols/iris-chen/videos/dance_clone_r6/iris_dance_clone_r6_ig_reel.mp4`（1072×1936、30fps、~9.87s，`scene_control: image` + 本機後製漂移運鏡，含驅動片原始配樂音軌，未經授權，僅供內部驗證）

---

## 2026-08-08 R15、R18 舞蹈克隆 — Step 1–4 完成，Step 5 待生成

**背景**：R15（IG shortcode `DPDTvczkep4`，Drive file ID `1NvmxZE7UXSeJ3lxyo-WQEiz5SY6QxPmT`，第2支，原
mia-huang 因尺度超出上限改分配）與 R18（`DRjp2qfkTk5`，`1CPDvqRzcy2VGA7F9xwRdcVArZL5jYfjv`）皆分配給
Iris Chen（見 Issue #3 2026-08-07 補充4）。批次處理 R12–R18，**跳過逐支 Performance Sheet/Emotion
Timeline（Step 3）**，會在進 Step 5 前補做。

### Step 1–2：下載與裁剪

- R15：870×1546、VP9、~14.8s，含編輯 App UI，已裁除（裁至 710×1406），轉 H.264
- R18：1080×1920、VP9、~14.7s，**畫面本身乾淨無 UI 疊加**，直接轉 H.264，未額外裁切
- 內容核對：R15 PLAYBOY 品牌挖空連身泳裝+粗框眼鏡+熱帶海灘（原始驅動片腰腹部有大片挖空，見下方 Step 4
  服裝調整說明）；R18 黑白條紋長袖上衣+灰色短褲，居家浴室鏡前跳舞，皆符合分配描述

### Step 4：起始畫面（已生成，待使用者核准）

- 模型：`soul_2` + `soul_id: 5fe3b6ba-1277-4822-9141-fb06eb3b93a0`
- **R15（Job ID `c4dcbf1a-1db9-4d5f-822d-4fe60f2253e4`）**：**服裝主動調整，記取 R10 教訓**——驅動片原始
  挖空範圍很大（品牌字樣下方一大片橢圓鏤空露出腹部），直接照抄有很高的 `nsfw` 風險，改為完整包覆軀幹的
  連身運動背心款式，保留粗框眼鏡+熱帶海灘場景。**已知瑕疵**：背心上的品牌文字生成為亂碼（"HLIE NORRA"／
  "VNSTRUSI"），是 AI 生成文字的常見缺陷，不影響辨識度但不美觀，待使用者確認是否需要重生成
- **R18（Job ID `3c28c398-af7e-40d8-8b6b-86589ca1f57c`）**：黑白條紋長袖上衣+灰色短褲，雙臂舉起behind head
  的動態手勢，居家浴室場景，單張乾淨圖，無問題
- 依 `DANCE_CLONE_SOP.md` 人工核准關卡規則，生成後停在這裡等使用者核准——**兩支皆已核准**（R15 帶已知
  文字亂碼瑕疵，使用者接受不需重生成）

### Step 3：Performance Sheet + Emotion Timeline（`performance-director` + `emotion-director` agent）

**R15**：
- **⚠️ 身分風險預先標記（事後證實未發生）**：驅動片本人是齊肩捲髮+旁分瀏海，起始畫面是更長的直髮+
  齊瀏海，跟 R12 同一類風險，風險集中在 ~8s、~14s 兩次摸頭髮動作。**使用者裁決：直接跑跑看**——
  結果見 Step 8，長直髮身分保住了
- **驅動片定性**：14.8s 純表情/手勢展示（推眼鏡、比手勢、甩髮），非全身舞蹈，框架幾乎全程胸上景
- **不對稱錨點（新建立，供 R18 沿用）**：以「眼睛」為主要識別特徵而非嘴角——左眼皮持續略重/慵懶，
  右眼相對清醒；次要為右嘴角先動、左眉獨立微揚、頭部左傾

**R18**：
- **⚠️ 身分風險預先標記（事後證實未發生）**：驅動片本人是蓬鬆大波浪捲髮+齊瀏海，起始畫面是較直較貼
  合的髮型，風險集中在開頭(0-2s)、結尾(12-14.7s)兩次甩髮動作。**使用者裁決：直接跑跑看**
- **驅動片定性**：14.7s 居家鏡前跳舞，兩次高能量甩髮動作（開頭+結尾）包夾中段較低能量的轉身/摸嘴手勢，
  結構前後呼應
- **不對稱錨點**：沿用 R15 新建立的錨點（左眼瞼較重、右嘴角先動、左眉獨立微揚、頭部左傾）
- **背景備註**：場景含鏡子（居家浴室鏡前），比照 R10 發現，`scene_control: image` 下鏡中倒影可能隨
  本人動作出現局部反射動態，屬已知現象非背景鎖定失敗

### Step 5：Motion Control（2026-08-08 完成）

- **R15**：`image_id`（已核准起始畫面）+ `scene_control: image`、`resolution: 1080p`，
  Job ID `ffcf0d82-55b3-4bdd-976b-07f7ddad8aca`，`status: completed`（一次通過），輸出 H.264、
  ~14.77s，無聲軌
- **R18**：`image_id`（已核准起始畫面）+ `scene_control: image`、`resolution: 1080p`，
  Job ID `df3d98ce-9ef4-4374-a1d7-c13cfbbd8149`，`status: completed`（一次通過），輸出 H.264、
  ~14.67s，無聲軌

### Step 6：手動混音

分別混上各自的 `driver_audio.m4a`，輸出 `iris_dance_clone_r15_ig_reel.mp4`（H.264/AAC、~14.77s）與
`iris_dance_clone_r18_ig_reel.mp4`（H.264/AAC、~14.67s）。

### Step 7：授權與發佈限制檢查

同前例：驅動動作僅供內部驗證；配樂未取得商用授權；`scene_control: image` 未借用驅動片背景（R18 鏡子
反射現象已於 Step 3 記錄為預期內）。

### Step 8：QA 檢核

**R15**：抽取 1.0s、8.0s、14.0s 幀跟已核准起始畫面並排比對：
- [x] **身分一致，風險未成真**：三幀的臉型、長直髮、粗框眼鏡皆與起始畫面吻合，摸頭髮動作沒有觸發
  驅動片本人捲髮特徵的覆蓋
- [x] **規格**：H.264/AAC、~14.77s

**R18**：抽取 1.0s、8.0s、14.0s 幀跟已核准起始畫面並排比對：
- [x] **身分一致，風險未成真**：三幀的臉型、直髮髮型皆與起始畫面吻合，開頭/結尾甩髮動作沒有觸發
  驅動片本人大波浪捲髮特徵的覆蓋
- [x] **鏡子背景**：確認為預期內的局部反射動態，非背景鎖定失敗
- [x] **規格**：H.264/AAC、~14.67s

**結論**：兩支皆 Step 1–8 完成，儘管 Step 3 都標記了跟 R12 同類的身分風險，實際生成結果都沒有發生，
QA 全數通過。

### 產出檔案

- `kols/iris-chen/videos/dance_clone_r15/iris_dance_clone_r15_ig_reel.mp4`（H.264/AAC、~14.77s，
  含驅動片原始配樂音軌，未經授權，僅供內部驗證）
- `kols/iris-chen/videos/dance_clone_r18/iris_dance_clone_r18_ig_reel.mp4`（H.264/AAC、~14.67s，
  含驅動片原始配樂音軌，未經授權，僅供內部驗證）

---

## 2026-08-12 日常性感短片（非舞蹈克隆，僅借用參考片音樂與氛圍）

**背景**：使用者指定一支 IG reel 當音樂來源（非動作驅動來源——這支不是舞蹈影片，是日常性感展示類型），
要求用 Iris 的人設做一支同調性的「日常」影片，服裝/場景不需要對標參考片，只要維持「性感展示」的方向。
`yt-dlp` 對該連結回報「內容不是所有人都能看」無法直接下載，使用者改為直接上傳影片檔案，已從中抽出音軌
（AAC，~8.6s）供後製混音使用。

**方法選擇**：使用者原本問「能不能用 Motion Control 的 `scene_control: video` 模式」來解決之前跳舞
克隆常見的「臉跟著驅動片本人跑掉」問題。已說明這個參數只決定背景來源、跟身分鎖定無關，且
`DANCE_CLONE_SOP.md` 已有 R6/R7 案例證實 `scene_control: video` 對這類貼身性感穿搭+真實背景合成
容易觸發審核失敗。**改用完全不同的方法**：不透過 Motion Control 逐幀轉印動作，而是用 Iris 自己的
`soul_id` 生成全新起始畫面+全新（非逐幀模仿）的輕微動態影片，只借參考片的氛圍/情緒，不進行動作克隆。

### Step 1：起始畫面（生成 3 次才成功，記錄拼貼bug新案例）

- 模型：`soul_2` + `soul_id: 5fe3b6ba-1277-4822-9141-fb06eb3b93a0`
- **第一次**（前傾靠近鏡頭姿勢，prompt 含 `THREE QUARTER SHOT` 與 `close intimate framing` 兩個互相
  矛盾的景別指令，另含 `film grain`／`shot on iPhone`）：拼貼（三連），跟 Rainie Hsu R5 案例類似但這次
  是不同的 soul_id，確認拼貼bug不是單一 soul 專屬問題
- **第二次**（拿掉矛盾景別指令與 `film grain`，改用 Iris 自己 `character.md` 既有的生成關鍵詞，姿勢
  仍是前傾靠近鏡頭）：仍是拼貼（三連）——排除了「film grain 用詞」這個變因，確認觸發點更可能是
  「上身前傾＋下巴微低＋靠近鏡頭」這個動態姿勢組合本身
- **第三次**（改成她招牌的「坐姿靜態床上自拍」姿勢，不再前傾靠近鏡頭）：**一次成功，乾淨單張圖**
  （1152×2048），Job ID `bfd49bac-831b-42ae-886e-7e1d9e96d72c`。**已請使用者核對，尚待核准。**
- **教訓（待日後驗證是否為通則）**：拼貼bug可能不只跟特定 soul_id 或特定字眼有關，「動態前傾+近距離
  直視鏡頭」這類姿勢描述本身也可能是觸發因子之一，之後遇到類似bug可以優先嘗試換成更靜態的姿勢描述。

**起始畫面已核准。**

### Step 2：動態短片生成（非 Motion Control，用 `generate_video` + 參考圖）

- 模型：`seedance_2_5`，`mode: omni_reference`（`start_image` 角色僅在這個 mode 下接受，`t2v`
  預設 mode 不接受參考圖，第一次呼叫因此被 422 擋下，補上 `mode` 參數後成功）
- 參考圖：`start_frame.png` 上傳後的 `media_id: 53e7565d-75ce-4e24-bb76-5e8f8b3fab3a`
- Prompt 設計原則：只描述**輕微、自然的動作**（頭部慢慢側傾、髮絲飄動、眨眼、把草莓送到嘴邊咬一口、
  毯子隨姿勢微微移動、鏡頭幾乎靜止只帶一點手持感、窗光自然閃動），刻意不描述任何舞蹈/大幅度動作——
  這是這次方法跟 Motion Control 逐幀動作克隆的本質差異：沒有驅動片可以逐幀模仿，也不需要
- `duration: 8`（對齊音樂長度 ~8.6s），`aspect_ratio: "9:16"`
- Job ID `e28d218c-255b-48fb-b0e3-ed41750a7d91`，輸出 720×1280、h264、~8.06s，**含模型自帶的 AAC 音軌**
  （非我方指定的音樂，推測是模型預設生成的環境音/靜音填充，直接被 Step 3 混音覆蓋掉，不影響最終成品）
- 抽 5 個時間點（0.5s/2.0s/4.0s/6.0s/7.5s）目視核對：身分穩定、動作自然（草莓吃入嘴的動作有連貫進展，
  不是瞬間跳接）、無拼貼問題

### Step 3：混音

用 `ffmpeg -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest` 把使用者提供影片抽出的原始音軌
（`reference_audio.m4a`，~8.6s）蓋上 Step 2 輸出的畫面軌，取兩者較短的長度（畫面 8.06s），輸出
`iris_daily_reel_r1.mp4`（720×1280、h264/aac 44.1kHz、~8.04s）。

### 授權提醒

這支音樂來自使用者提供的第三方影片，**內部驗證用，未取得商用授權**——正式對外發佈前需替換成已授權的
版本或取得原曲授權，比照 `DANCE_CLONE_SOP.md` Step 7 對驅動片配樂的同一套規則。這支影片本身沒有動作
克隆或場景借用的問題（因為完全是原創生成，不是 Motion Control），唯一的授權缺口只在音樂本身。

### 產出檔案

- `kols/iris-chen/images/daily_reel_music_r1/start_frame.png`（已核准起始畫面）
- `kols/iris-chen/videos/daily_reel_music_r1/iris_daily_reel_r1.mp4`（720×1280、h264/aac、~8.04s，
  含使用者提供的第三方音樂音軌，未經授權，僅供內部驗證）

### 2026-08-12 v2 重做：多鏡頭切換感 + 加長時長（使用者反饋後）

**使用者反饋**：「做到像原驅動片一樣，有不同的切換鏡頭跳來跳去的那種感覺。因為它動作太慢了，然後看
起來就是很沒有 feel，而且為什麼只有 8 秒？」——v1 的問題：(1) 單鏡頭到底，沒有切鏡感；(2) 動作幅度
太保守、太慢；(3) 長度只對齊到參考音樂的 8.6s，沒有做到參考片本身的節奏感。

**改法**：換成 `kling3_0`（`generate_video`，非 Motion Control，延續 v1 的「不逐幀克隆動作」原則），
理由是 SOP 已記錄 `kling3_0` 比 `seedance_2_5` 更適合多鏡頭切換與這類非線性運鏡需求。

- 參考圖：同一張已核准起始畫面（`media_id: 53e7565d-75ce-4e24-bb76-5e8f8b3fab3a`），角色 `start_image`
- `get_cost: true` 預檢：30 credits；`mode: "omni_reference"` 對 `kling3_0` 不是合法值，被系統靜默改回
  模型預設 `"std"`（回應中的 `params.mode.reason: "not in [std, pro, 4k]; using model default"`）——
  正式生成時直接不帶 `mode` 參數，讓它預設
- Prompt 明確描述 **4 個不同鏡頭的快速切換**（近距離微笑 → 側身後仰靠床、手撐床面的較廣鏡位 → 低角度
  仰拍咬草莓/眨眼 → 近距離撥髮大笑），刻意用「鏡頭切換」的語言而非「持續動作」，對應使用者要的
  「跳來跳去」剪接感
- `duration: 15`、`aspect_ratio: "9:16"`
- Job ID `ea0e5146-f94d-4220-aa04-605f702512fc`，輸出 720×1280、h264/aac、~15.04s
- 抽 8 個時間點（0.5s/3.0s/4.0s/7.0s/8.0s/11.0s/12.0s/14.5s）目視核對，全數通過：
  - 身分穩定，跟已核准起始畫面一致（髮型、臉型、五官皆吻合）
  - 確認達成「多鏡頭切換」效果：近景微笑、側身後仰廣角、低角度仰拍咬草莓眨眼、近景撥髮大笑，四種
    明顯不同的取景/角度自然分布在時間軸上，不是同一鏡頭的連續運鏡
  - 無拼貼bug、無手部變形

**音樂長度落差的處理**：使用者提供的參考音樂只有 ~8.6s，但新影片是 ~15.04s，兩者不吻合。採用
`ffmpeg -stream_loop -1` 讓音軌循環播放以蓋滿全長，並在片尾（14.5s–15.0s，0.5s）加 `afade=out`
避免循環接點在片尾處生硬卡斷。**這是取捨後的暫時解法，不是真正的完整編曲**——循環點在音軌內部
（~8.6s 處迴圈重啟）可能仍會被敏感的耳朵聽出接縫。若使用者對接縫感不滿意，正式解法應是取得
更長版本的音樂或找人另外編一段配樂，而不是持續依賴迴圈。

### v2 產出檔案

- `kols/iris-chen/videos/daily_reel_music_r1/iris_daily_reel_r1_v2_multishot.mp4`（720×1280、h264/aac、
  ~15.04s，音軌為使用者提供的第三方音樂迴圈+淡出，未經授權，僅供內部驗證）
- v1（`iris_daily_reel_r1.mp4`，8s、單鏡頭）保留供比對，非正式棄用

**使用者驗收反饋（2026-08-12）**：「這個還行，但以後要避開一些奇怪的鏡頭角度，由下往上拍這種怪角度」
——v2 已核准，但其中「低角度仰拍咬草莓/眨眼」這個鏡頭被明確指出構圖怪異。已將此規則寫進
`SEXY_SCENE_LIBRARY.md` 第 16 點與生成前檢查清單，之後任何角色的多鏡頭 prompt 都要避開「由下往上」
的低角度仰拍，不限於 Iris。

---

## 2026-08-12 溫泉木桶梗短片（同一套「借氛圍不逐幀模仿」方法，第二支參考片）

**背景**：使用者換了一支新的參考片（Yua Mikami 戶外露天溫泉夜景，經典「頭頂木桶」搞笑梗），要求
「照一樣的思路再做一支」——沿用上面「日常性感短片」的方法：不用 Motion Control 逐幀模仿動作，只借
參考片的音樂/氛圍，用 Iris 自己的 `soul_id` 重新生成全新場景+全新動態。

### Step 1：起始畫面（一次成功，套用已知的安全姿勢與收尾規則）

- 模型：`soul_2` + `soul_id: 5fe3b6ba-1277-4822-9141-fb06eb3b93a0`，`aspect_ratio: "9:16"`
- 場景改為戶外露天溫泉夜景：木桶頂在頭上、蒸氣、暖色燈籠光、遠處日式旅館建築、深色夜空
- 沿用她已核准有效的核心 prompt 結構（身材數字+膚質+風格字尾），姿勢用**正面平視靜態坐姿**
  （避開她已知的拼貼bug觸發姿勢「前傾靠近鏡頭」），也遵守新增的第 16 點規則——全程平視角度，
  無低角度仰拍
- 尺度處理：描述穿著「與膚色同色系的無肩帶泳衣，在水面下與肌膚融為一體」，讓畫面達到跟參考片
  同等的「疑似裸浴但被水/蒸氣完全遮蔽」效果，同時保持在 SFW 範圍內（沒有裸露到不能發佈的程度）
- Job ID `f33f2141-10aa-4a63-ab3c-3678fbe4c432`，一次成功，乾淨單張圖（1152×2048），無拼貼、無變形

**起始畫面已核准。**

### Step 2：動態短片（`kling3_0`，多鏡頭切換，特別處理木桶物理）

**使用者特別提醒**：「因為他的木桶生成在他的頭上，所以可能要注意影片裡木桶有一些奇怪的動作，要自然
一點」——木桶是頭頂上的剛體道具，如果 prompt 沒有明確描述誰在控制它的動作，模型很容易生成「木桶自己
飄浮/晃動/穿模」這類不自然的物理錯誤。

**設計對策**：把木桶的動作拆成「先靜止、再由雙手主動控制」兩階段，全程不讓木桶自己運動：
- Shot 1（近景靜態）：她完全靜止不動，木桶穩定停在頭頂不晃動，只有表情變化
- Shot 2（中景）：她**雙手主動抓住木桶邊緣**，緩慢平順地把木桶整個抬離頭頂——木桶的移動全部由
  雙手的抓握動作驅動，不能自己浮動或旋轉
- Shot 3（3/4 側角，較廣景）：她把抬起的木桶抱在胸前，開懷大笑
- Shot 4（近景）：木桶已完全移出畫面，只剩放鬆自然的笑容，收尾鏡頭

四個鏡頭皆為平視或微俯角，沒有低角度仰拍。

- 模型：`kling3_0`，`duration: 15`、`aspect_ratio: "9:16"`，參考圖 `media_id: 6b75e61e-2643-4769-ba0f-aacefa1d6e0e`
- 系統一度判定 prompt 符合內建 preset「ELEVATE」，選擇不用 preset、按原字面生成（`declined_preset_id`）
- Job ID `5cde486a-be33-45f8-a8c5-64a97dc27242`，輸出 720×1280、h264/aac、~15.04s
- 抽 11 個時間點（0.5s/2.0s/3.5s/4.5s/6.0s/7.5s/9.0s/10.5s/12.0s/13.5s/14.5s）目視核對，全數通過：
  - **木桶物理完全符合預期**：Shot 1 木桶靜止不動；Shot 2–3 木桶只在雙手明確抓握時才移動，抬起、
    水滴落下的動作自然，沒有出現飄浮/穿模/自己旋轉等問題
  - 全片皆平視或微俯角，沒有出現低角度仰拍（對應上一支影片的使用者反饋，這次主動避開）
  - 身分穩定、無拼貼、無手部變形

### Step 3：混音

同上一支的做法：參考片音軌只有 ~11.19s，短於影片的 ~15.04s，用 `ffmpeg -stream_loop -1` 循環音軌
蓋滿全長，片尾 14.5s–15.0s 加 `afade=out` 避免接點卡斷。輸出 `iris_onsen_reel_r1.mp4`
（720×1280、h264/aac、~15.04s）。**同樣的授權限制**：音樂來自使用者提供的第三方影片，內部驗證用，
未取得商用授權。

### 產出檔案

- `kols/iris-chen/images/onsen_bucket_r1/start_frame.png`（已核准起始畫面）
- `kols/iris-chen/videos/onsen_bucket_r1/iris_onsen_reel_r1.mp4`（720×1280、h264/aac、~15.04s，
  音軌為使用者提供的第三方音樂迴圈+淡出，未經授權，僅供內部驗證）

---

## 2026-08-12 日常性感照片批次 `daily_sexy_night_v1`（5 張，室內夜晚，首次驗證五段式物理光線公式）

**使用者需求**：「多生成一些 Iris 的日常照片，各種不同的穿搭和造型，但都性感一點」——場景限室內家裡
（房間／浴室／客廳），偏夜晚氛圍，穿性感內衣或同等級的性感居家服；拍攝感要**自拍與他拍混合**，角度
要多樣。先做 5 張不一樣的。

**這批的定位**：這 5 張**不是一則 carousel**（不適用第 14 點「1 個 setup × 5–6 種表情」），而是 5 則
不同貼文各自的錨定素材——所以刻意每張都換掉穿搭／髮型／場景／光線，正是第 13 點「造型與地點是獨立
變數」要的輪替。之後要做 carousel，是挑其中一張的 setup 再延伸 5–6 種表情。

### 平台與參數

- 模型：`soul_2` + `soul_id: 5fe3b6ba-1277-4822-9141-fb06eb3b93a0`
- `quality: "2k"`、`aspect_ratio: "3:4"`（IG 動態牆比例），輸出皆 1536×2048
- 共 7 次生成（5 張初版 + 2 張重生），全部一次成功，無 `failed`／`nsfw`／拼貼bug
- 姿勢全部採**靜態**（坐姿／站姿），主動避開 2026-08-12 已記錄的拼貼bug觸發姿勢「上身前傾＋靠近鏡頭」

### 五張的變數配置（四個轉盤各自獨立轉）

| # | 場景 | 穿搭（五層） | 髮型 | 視角 | 光線配方（① 主光 → ② 反射面 → ③ 第二色溫 → ④ 犧牲處 → ⑤ 遮擋框架） | Job ID |
|---|---|---|---|---|---|---|
| 01 | 臥室床上／床頭板 | 黑蕾絲三角胸衣 + 同款蕾絲內褲 + 光腳 + 灰針織開襟外套滑落單肩 + 細金鎖骨鍊＋銀戒 | 長直髮放下、一側塞耳後 | **自拍**（前鏡頭微俯角） | 床頭鎢絲燈（畫右、床墊高度）→ 米白床單＋淺色牆 → 窗簾縫的城市藍光 → 燈罩過曝純白／房角壓黑 → 床頭板＋垂下的充電線 | `d9f9c510-7f68-44b0-95db-88fb6bf5be19` |
| 02 | 浴室洗手台鏡前 | 米白絲質蕾絲邊細肩帶睡裙（單肩帶滑落）+ 白毛巾掛肩 + 光腳 + 黑髮圈在手腕 + 金色小耳扣 | **濕髮**、手擰髮尾 | **鏡子自拍**（手機入鏡） | 鏡側暖白 LED 燈條 → 白磁磚＋起霧鏡面 → 走廊冷白頂燈自門縫 → 燈條過曝成白塊／門後壓黑 → 門框＋鏡框 | `b1d258c0-7dd4-4e1f-ab26-7f2af6354595` |
| 03 | 客廳沙發 | 酒紅緞面細肩帶短睡裙 + 灰色羅紋過膝襪 + 燕麥色粗針織開襟外套（搭在沙發背）+ 細金手鍊＋銀戒 | 鯊魚夾盤髮、碎髮垂落 | **他拍**（朋友視角，平視） | 畫面外電視冷藍白光 → 燕麥色沙發布＋淺木地板 → 房間深處琥珀檯燈 → 迎光面高光過曝／後半房壓黑 → 沙發扶手＋毯子邊 | `2660388a-220f-4a9e-956e-742c94452359` |
| 04 | 臥室全身鏡前（換衣中） | 象牙白絲質內衣套組（bralette + 高腰內褲）+ 敞開的oversized白襯衫（袖子推起）+ 光腳 + 黑色髮圈 + 金色小圈耳環 | 低馬尾、臉側留碎髮 | **鏡子自拍**（全身，手機入鏡） | 衣櫃旁暖琥珀立燈（右後方）→ 白衣櫃門板＋鏡面玻璃 → 對街綠色霓虹招牌透紗簾 → 燈泡過曝／房間左側壓黑 → 鏡框＋半開衣櫃門 | `2acfc614-46d5-494d-ba85-ae250d8d5359` |
| 05 | 臥室地板窗邊（伸展後） | 黑色細肩運動內衣 + 炭灰高腰單車短褲 + 光腳 + 淺灰連帽外套丟在地上 + 細金腳鍊＋黑髮圈 | 高馬尾、鬢角碎髮 | **他拍**（3/4 側身，平視） | 窗外冷藍城市夜光（前左）→ 淺木地板＋白色床單 → 身後琥珀鹽燈 → 窗外與對面樓的燈過曝純白／床後房角壓黑 → 窗框＋半拉紗簾 | `4921501b-ec52-43ed-8747-d3af91ab4c3b` |

**自拍：他拍 = 3:2**（01/02/04 自拍，03/05 他拍），符合第 7 點。自拍張全部改用低畫質語氣
（`front camera quality, slightly softer focus, NOT ultra-crisp`／鏡子自拍用後鏡頭語氣），他拍張才用
`crisp sharp focus, fine detail`。

**私密場景（臥室／浴室／自家客廳）依第 9 點維持只有本人入鏡，無背景路人。**

### 生成後逐張檢查（第 10 點，含放大裁切檢視手部）

用 Read 逐張看過全圖，並用 PIL 對每一隻入鏡的手／關節做 2–3 倍放大裁切檢視：

| # | 結果 | 細節 |
|---|---|---|
| 01 | ✅ 通過 | 放在大腿上的手指數正確、無融合；生活雜物（零食袋、寶特瓶、手機、充電線、亂丟的衣服）到位 |
| 02（初版） | ⚠️ **spec 落差，已重生** | 手部與畫質沒問題，但 prompt 寫的「剛洗完澡的濕髮」**沒有生出來**（生成結果是乾髮綁起），睡裙也偏合身連身裙而非絲質睡裙——「剛洗完澡」的敘事沒有成立。留檔於 `alternates/02_alt_bathroom_dryhair_mirror.png` |
| 02（重生） | ✅ 通過 | 加強濕髮描述（`soaking wet, darkened with water, slicked flat back, droplets running down her collarbone`）並把姿勢改成「手擰髮尾」後成功；抓髮的手與持機的手放大檢視皆為正常五指 |
| 03（初版） | 🔴 **AI 瑕疵，已重生** | 抬起的膝蓋上那隻手**與膝蓋融合**（手指沒有分界、掌腕連接不清）。全圖尺寸下不明顯，但符合第 10 點「不能因為整體看起來還可以就略過」的退件標準。留檔於 `alternates/03_alt_sofa_hand_defect.png` |
| 03（重生） | ✅ 通過 | 修法：把姿勢從「手放在抬起的膝蓋上」改成「一手平放沙發墊、五指張開分明，一手搭沙發背懸空」，並明寫 `both hands well clear of her legs, no hand overlapping her knees` + `anatomically correct hands with exactly five fingers each`。放大檢視兩隻手皆為正確五指、指節比例正常 |
| 04 | ✅ 通過 | 本批**身材數字還原度最好**的一張；持機手與拉內褲腰邊的手皆正常。霓虹招牌的中文是亂碼（維持既有取捨）|
| 05 | ✅ 通過 | 皮膚毛孔質感本批最佳；扶地的手、折疊的腿無變形 |

**已知取捨／可再優化**：
- **身材還原度不穩**：01、02 生成結果的胸圍明顯小於人設的 87cm/D cup，體態偏纖細；04、05 較接近。
  prompt 已照規則寫入三圍數字，`soul_2` 仍會被 soul 本身的訓練分布拉走。若要穩定還原，下一步可試在
  數字之外補寫體感形容（如 `full rounded bust filling the bralette`），或改用 Reference Element 錨定。
- **臉部皮膚偏光滑**：01/02 的臉部毛孔質感弱於 05，`visible skin pores` 這組字在近距離自拍張的效果
  不如中景他拍張明顯。
- **地點層級全部落在 B 級**（自家臥室／浴室／客廳）。這批因使用者明確指定「室內家裡」而不適用第 13 點
  的 C 級配額；C 級（賣場、超商、路口）留給之後的外出批次補回，不要因為這批而讓整體配額掛零。

### 五段式物理光線公式首次全面套用的結論（回應 2026-08-05 記錄的「🔴 打光尚未套用新公式」）

- ✅ **公式可執行**：五張的 `[LIGHTING]` 都寫滿五段，全部禁用 `high dynamic range`／`well-exposed`／
  `evenly lit`。生成結果確實出現了「指得出光從哪來」的空間感——02 的鏡側燈條過曝成白塊、04 的立燈
  燈泡過曝＋房間左側壓黑、05 的窗外過曝純白，**「哪裡被犧牲」這一段確實被模型吃到了**，這是舊版
  「品質形容詞」寫法生不出來的效果。
- ✅ **兩個色溫並存**成功率高：03（電視冷藍 + 琥珀檯燈）、04（暖立燈 + 窗外綠霓虹）、05（窗外冷藍 +
  鹽燈暖光）三張都清楚讀得出畫面裡有兩種色溫各自落在不同區域。
- ⚠️ **反射面的效果最難目視驗證**：寫了具名反射面（床單／磁磚／沙發布／衣櫃門／木地板）後，暗部確實
  有柔和填光而不是死黑，但無法斷定是這句話的功勞還是模型本來就會這樣打。維持照寫，成本為零。
- ⚠️ **夜晚場景仍偏亮**：01 讀起來比預期的「深夜臥室」亮一些。下一批可在 `[LIGHTING]` 再明確指定
  主體與背景的曝光差（例如 `the room two stops darker than her face`）。

### 產出檔案

- `kols/iris-chen/images/daily_sexy_night_v1/01_bedroom_black_lace_selfie.png`
- `kols/iris-chen/images/daily_sexy_night_v1/02_bathroom_wethair_mirror.png`
- `kols/iris-chen/images/daily_sexy_night_v1/03_sofa_wine_satin_candid.png`
- `kols/iris-chen/images/daily_sexy_night_v1/04_fulllength_mirror_ivory_silk.png`
- `kols/iris-chen/images/daily_sexy_night_v1/05_floor_window_sportsbra_candid.png`
- `kols/iris-chen/images/daily_sexy_night_v1/alternates/02_alt_bathroom_dryhair_mirror.png`（乾髮版，spec 落差留檔）
- `kols/iris-chen/images/daily_sexy_night_v1/alternates/03_alt_sofa_hand_defect.png`（手部融合瑕疵留檔，不可使用）

**狀態：5 張皆通過內部 QA，待使用者核准。** 尚未上傳 Google Drive（等核准後再歸檔）。

---

## 2026-08-12 情趣內衣批次 `daily_sexy_night_v2_lingerie`（5 張，全自拍視角）

**使用者需求**：接續 `daily_sexy_night_v1`，「換一組衣服，可能是情趣內衣？然後都生成自拍角度的」。
所以本批兩個硬條件：(1) 服裝全部升級為情趣內衣等級（babydoll／teddy／吊襪帶＋絲襪／蕾絲連身），
(2) **五張全部是自拍視角**（不再有他拍）——這是刻意打破第 7 點「混合自拍與他拍」的一次單批例外，
因為使用者明確指定；第 7 點講的是**角色的完整素材組合**要混合，v1 批次已提供他拍張，整體仍成立。

### 平台與參數

- 模型：`soul_2` + `soul_id: 5fe3b6ba-1277-4822-9141-fb06eb3b93a0`，`quality: "2k"`、`aspect_ratio: "3:4"`
- 共 7 次生成（5 張初版 + 2 張重生），全部一次成功，無 `failed`／`nsfw`／拼貼bug
- 尺度控制：維持 SFW——蕾絲／薄紗有透感但關鍵部位皆有不透明襯裡，無裸露

### 五張的變數配置（全自拍，但自拍**類型**刻意分成三種）

| # | 場景 | 情趣內衣（五層） | 髮型 | 自拍類型 | 光線配方 | Job ID |
|---|---|---|---|---|---|---|
| 01 | 臥室床上 | 黑蕾絲 babydoll（前中緞帶蝴蝶結、蕾絲下襬）+ 黑蕾絲內褲 + 光腳 + 細金鎖骨鍊 + 金耳釘 | 長直髮放下微亂 | **前鏡頭微俯角近景** | 床頭鎢絲燈 → 米白床單 → **自己的手機螢幕冷光**打在臉上 → 燈側牆過曝／房間暗兩級 | `78183e61-d889-42ff-b66e-d736284d5d9c` |
| 02 | 臥室全身鏡 | 酒紅緞面 teddy（蕾絲罩杯）+ 黑色薄紗短罩衫敞開 + 黑色薄紗大腿襪 + 金手鍊 + 金圈耳環 | 半盤髮＋酒紅緞帶 | **全身鏡自拍**（手機入鏡） | 鏡框上緣暖色圓燈泡排 → 白衣櫃門板＋鏡面 → 窗外冷白街燈 → 燈泡過曝成白圓／房間左半壓黑 | `83f5624d-4033-4673-a4d5-d26b1d1ad7cc` |
| 03 | 浴室洗手台 | 粉色緞面蕾絲邊 babydoll 內衣套組 + 粉蕾絲內褲 + 光腳 + 黑髮圈 + 金耳扣 | 高馬尾、鬢角濕髮 | **浴室鏡自拍** | **只開淋浴間的燈**，光從玻璃門縫切出硬邊光斑 → 對面白磁磚 → 門邊藍色小夜燈 → 淋浴門口過曝／浴室右半深黑 | `468d9e7e-01bb-4786-a9b3-ab93250e7e16` |
| 04 | 臥室床上（躺姿） | 深藍蕾絲連身 bodysuit（蕾絲腰片）+ 米色針織外套滑落單肩 + 細金項鍊 + 金耳釘 | 長髮散在枕頭上 | **躺著由上往下的前鏡頭自拍** | 枕邊琥珀小夜燈側掃 → 米色枕頭＋白床單 → 天花板上的藍白投影機光 → 夜燈過曝／床外暗兩級壓黑 | `9902aa8d-b65c-44ec-af54-affd8e2236f4` |
| 05 | 臥室梳妝台 | 象牙白蕾絲長版 bralette + 高腰蕾絲內褲 + **蕾絲吊襪帶＋象牙白大腿襪** + 灰針織外套雙肩滑落 + 銀戒＋金腳鍊 | 鯊魚夾高盤髮 | **前鏡頭微俯角 3/4 身** | 桌燈（桌面高度前側，**非仰角**）→ 淺色桌面＋梳妝鏡 → 窗外綠色霓虹 → 燈泡過曝純白／身後房間暗兩級 | `16652b29-3e11-4797-8553-3a4b33abe767` |

雖然五張都是自拍，但**自拍類型分成三種**（前鏡頭手持／鏡子反射／躺姿俯拍），避免整批看起來是同一個
機位重複五次。全部平視或微俯角，無低角度仰拍（第 16 點）。

### 生成後逐張檢查（第 10 點，含放大裁切檢視每一隻手）

| # | 結果 | 細節 |
|---|---|---|
| 01 | ✅ 通過 | 撐在床單上的左右兩隻手放大後皆為正確五指；床上雜物（充電線、亂丟衣物、床頭小物）到位 |
| 02（初版） | 🔴 **AI 瑕疵，已重生** | 垂在身側的左手**手指糊成一片**，中指無名指小指融合，根數數不出來。光線是本批最好的一張（鏡框燈泡過曝、色溫分裂明確），但手必須退。留檔 `alternates/02_alt_mirror_vanitybulbs_hand_defect.png` |
| 02（重生） | ✅ 通過 | 把該手改成「舉到臉旁撥髮、塞碎髮到耳後」，手在畫面中變大後結構正確、五指分明。**代價**：重生版的鏡子變成一般門邊鏡，沒有再生出燈泡排，光線比初版平——這是本批唯一「修好了手但光線退步」的取捨 |
| 03（初版） | 🔴 **AI 瑕疵，已重生** | 同樣是垂在身側的手，手指融合成三根塊狀。留檔 `alternates/03_alt_bathroom_hand_defect.png` |
| 03（重生） | ✅ 通過 | 改成「平放在白色洗手檯上、五指分明」後正確；淋浴間硬邊光斑與過曝門口保留得很好 |
| 04 | ✅ 通過 | 放在胸前的手五指分明、指甲細節正確；本批**身材還原度最好**的一張 |
| 05 | ✅ 通過 | 撐在桌面的手五指分明（含戒指）；吊襪帶＋大腿襪的結構正確，梳妝台雜物（眼影盤、離子夾、蠟燭、收據）到位 |

### 本批最重要的方法論修正：**「讓手懸空」是錯的，已推翻並改寫 SEXY_SCENE_LIBRARY 第 10-c 點**

v1 批次寫下的 10-c 建議「另一隻手讓它懸空（`hanging free in open air`），背景單純最不容易出錯」。
本批用這個寫法實測 **2/2 全部失敗**（02、03 兩張站姿全身自拍的垂手都糊掉）。

**真正的變因不是背景單純，是這隻手在畫面裡佔多大、離臉多遠。** 站姿全身鏡自拍中，垂在身側的手位於
畫面下緣、尺寸很小，模型就把手指糊成一團。修正後的兩個做法都已在本批實測成功：

1. **給這隻手一件事做，而且要靠近臉**（撥髮／塞耳後）→ 手變大，結構就對（02 重生版驗證）
2. **平放在對比色的實體表面上**（白色洗手檯／床單／桌面）→ 有支撐面就對（03 重生版、01、05 驗證）

一句話：**手要嘛大、要嘛有支撐面；小又懸空的手一定糊。** 已同步改寫 `SEXY_SCENE_LIBRARY.md` 第 10-c 點。

### 其他觀察

- ✅ **`full rounded bust clearly filling out the lingerie` 有效**：v1 記錄的「胸圍小於人設」問題，這批
  補上體感形容後，04、05、02 的還原度明顯改善（01 仍偏保守）。這句話成本為零，建議之後固定加進核心 prompt。
- ✅ **「暗兩級」的寫法有效**：v1 記錄「夜晚場景仍偏亮」，這批在 `[LIGHTING]` 明寫
  `the room two stops darker than her face`，03、04 的夜感明顯比 v1 深。
- ⚠️ **中文字仍亂碼**：02 牆上海報、05 桌上收據的中文皆為亂碼字形，維持既有取捨。

### 產出檔案

- `kols/iris-chen/images/daily_sexy_night_v2_lingerie/01_bed_black_lace_babydoll_selfie.png`
- `kols/iris-chen/images/daily_sexy_night_v2_lingerie/02_mirror_burgundy_teddy_selfie.png`
- `kols/iris-chen/images/daily_sexy_night_v2_lingerie/03_bathroom_pink_babydoll_selfie.png`
- `kols/iris-chen/images/daily_sexy_night_v2_lingerie/04_lyingbed_navy_lace_bodysuit_selfie.png`
- `kols/iris-chen/images/daily_sexy_night_v2_lingerie/05_dressingtable_ivory_garter_selfie.png`
- `alternates/02_alt_mirror_vanitybulbs_hand_defect.png`（手部瑕疵，不可使用；但光線可當範例參考）
- `alternates/03_alt_bathroom_hand_defect.png`（手部瑕疵，不可使用）

**狀態：5 張皆通過內部 QA，待使用者核准。** 尚未上傳 Google Drive。

---

## 2026-08-12 遮擋式「零裸露」批次 `daily_sexy_night_v3_implied`（5 張，暗示裸體但完全無裸露）

**使用者需求**：「有沒有辦法做那種，其實完全沒穿衣服，但可能用一些物品遮擋住重要部位，其實完全沒有
裸露的性感生活照，想要氛圍是晚上在房間那種曖昧的感覺，自拍或他拍都有」。

**方法沿用溫泉木桶那支已驗證的作法**（見上方 2026-08-12 溫泉批次）：**不要在 prompt 裡寫「裸體」**
——那會踩審核，也不好控制。改成兩段式描述：

1. **`COVERAGE:` 獨立欄位**，明寫「她穿著一件**與膚色同色的無肩帶內衣，完全藏在遮蔽物後面、畫面中
   永遠看不到**，所以這張讀起來像是裡面什麼都沒穿，但鎖骨以下全部被遮蔽物完整覆蓋」，並補一句
   `no exposed chest, fully SFW`
2. **遮蔽物本身寫進 `WARDROBE VISIBLE IN FRAME:`**，當成一件「畫面上真正存在的衣服」來寫

結果：**5/5 一次成功，零審核失敗、零裸露**。這組措辭建議固定成模板，之後任何角色要做這類素材直接沿用。

### 五張的遮蔽物設計（刻意五種不同物件，不重複同一招）

| # | 遮蔽物 | 場景 | 髮型 | 視角 | 光線配方 | Job ID |
|---|---|---|---|---|---|---|
| 01 | **白棉被抱在胸前**（雙臂交叉壓住上緣） | 臥室床上 | 長直髮放下 | **自拍**（前鏡頭微俯角） | 床頭鎢絲燈 → 白棉被大反射面 → 窗縫城市藍光 → 燈罩過曝／房角壓黑 | `609903a3-417b-4202-9d99-4e5125a58cc2` |
| 02 | **俯臥＋棉被蓋到腰下**（胸口整個貼床，正面完全不入鏡） | 臥室床上 | 鯊魚夾盤髮 | **他拍**（床邊平視） | 枕邊琥珀夜燈側掃背部 → 白棉被＋床單 → 紗簾外冷白街燈 → 夜燈過曝／床外壓黑 | `67289a47-a216-440d-8f6f-e9f597bf4e7a` |
| 03 | **大抱枕抱在身前**＋灰針織毯蓋腿 | 臥室地板、背靠床沿 | 低馬尾撥到單肩 | **他拍**（朋友視角平視） | 身後暖琥珀立燈 → 米色亞麻抱枕 → **半開筆電的冷藍螢幕光**由下前方打 → 燈泡過曝／左半房壓黑三級 | `56c63c8a-be47-4456-8a0a-6e3997e5b1aa` |
| 04 | **泡泡浴的白色泡沫**（覆蓋到鎖骨） | 浴室浴缸 | 頭頂丸子頭 | **自拍**（前鏡頭微俯角） | 缸沿單支蠟燭低前側光 → 白泡沫大反射面 → 門邊藍色小夜燈 → 燭焰過曝／浴室遠端壓黑 | `913596cc-ea4f-4685-9791-bfa5ab40a327` |
| 05 | **白色床單裹身**（腋下裹到膝上，單手抓住胸口） | 臥室落地窗前 | 大波浪長髮 | **他拍**（3/4 背身回眸） | 窗外冷藍城市光正面 → 身上白床單 → 身後房內琥珀床頭燈暖邊光 → 窗外過曝／房內壓黑 | `3dffe549-511e-4571-a4f4-aac4975eb402` |

**自拍 2（01、04）／他拍 3（02、03、05）**，符合使用者「自拍或他拍都有」。全部平視或微俯角，無仰拍。

### 生成後逐張檢查（第 10 點，逐隻手放大裁切）

| # | 結果 | 細節 |
|---|---|---|
| 01 | ✅ 通過 | 交叉在被子上的兩隻手結構正確；遮蔽完整。**唯一小瑕疵**：膚色內衣的上緣在胸口露出一小段米色布邊，看得出是「白布下面還有一層」，稍微削弱「什麼都沒穿」的錯覺——不影響使用，但下次可把內衣寫成「與白色遮蔽物同色」而非「與膚色同色」 |
| 02 | ✅ 通過 | 本批最成功的一張——俯臥背影完全沒有正面裸露問題，疊在下巴下的雙手放大後五指分明、指甲細節正確；暖夜燈打在肩胛骨的質感很好 |
| 03（初版） | ⚠️ **spec 落差，已重生** | 遮擋、手部都沒問題，但**光線讀起來像白天的平光**——沒有可指認的夜間光源、沒有暗部，完全不是使用者要的「晚上曖昧感」。留檔 `alternates/03_alt_floor_cushion_daylight_mood.png` |
| 03（重生） | ✅ 通過 | 在 `[LIGHTING]` 明寫「房間主燈關掉、全室黑暗、畫面裡只有兩個光源」＋「左半房與天花板暗三級壓死無細節」＋`no daylight anywhere in frame`，夜感立刻正確：黑掉的窗、對面樓的燈、空調機、暗部大面積壓黑。兩隻手放大後皆五指分明 |
| 04 | ✅ 通過 | 泡沫覆蓋線穩定停在鎖骨下方；泡沫裡的手五指分明、指尖沒入泡沫的層次自然 |
| 05 | ✅ 通過 | 貼在窗玻璃上的手五指張開分明；回眸角度自然。床單裹身讀起來偏向「白色平口洋裝」，暗示感比預期弱一點，但仍成立 |

### 方法論記錄（建議固定沿用）

1. **`COVERAGE:` 欄位是這批成功的關鍵。** 把「遮蔽邏輯」獨立成一段寫清楚（穿了什麼隱形的、被什麼遮住、
   哪些部位可見、哪些絕對不可見），比在服裝段落裡夾帶一句有效得多，而且**完全不需要用到任何裸露字眼**。
2. **膚色內衣 vs 同色內衣**：01 露出米色布邊的問題顯示，當遮蔽物是白色時，隱形內衣應該指定成**與遮蔽物
   同色**（白色），而不是與膚色同色——這樣即使露出邊緣也讀成遮蔽物本身的一部分。
3. **「夜晚」不能只寫 `late at night`。** 03 初版寫了 `late at night` 但生出白天平光。有效的寫法是把
   **黑暗本身當成要生成的東西**來描述：主燈關掉、全室黑暗、畫面裡只有哪兩個光源、哪一大塊要暗三級
   壓死無細節、`no daylight anywhere in frame`。這條補充第 3 點五段式光線公式的「④ 犧牲處」。

### 產出檔案

- `kols/iris-chen/images/daily_sexy_night_v3_implied/01_bed_duvet_selfie.png`
- `kols/iris-chen/images/daily_sexy_night_v3_implied/02_prone_bareback_candid.png`
- `kols/iris-chen/images/daily_sexy_night_v3_implied/03_floor_cushion_hug_candid.png`
- `kols/iris-chen/images/daily_sexy_night_v3_implied/04_bubblebath_candle_selfie.png`
- `kols/iris-chen/images/daily_sexy_night_v3_implied/05_window_bedsheet_wrap_candid.png`
- `alternates/03_alt_floor_cushion_daylight_mood.png`（光線落差版，留檔）

**狀態：5 張皆通過內部 QA，待使用者核准。** 尚未上傳 Google Drive。

---

## 2026-08-12 加大尺度批次 `daily_sexy_night_v4_bolder`（5 張，露膚面積顯著提高）

**使用者需求**：「有沒有辦法做得更性感煽情一點，露更多乳溝、大腿之類的，身體肌膚要露出來多一點，
若隱若現的，甚至整個身體只有乳頭、下體等重要部位被擋住，目前看起來還是過於保守，有些甚至比穿著內衣
擋的還多」——明確指出 v3 遮擋批次太保守（尤其 v3-05 床單裹身比 v2 內衣批次遮更多）。

**執行範圍**：這批把露膚面積拉高到「布料面積很小的衣著」等級——深 V 到胸骨、高衩露整條腿、微型蕾絲
內衣、浴巾只裹到胸口上緣、背面全裸。**未執行**使用者提到的「全裸只用物件擋住重點部位」那一階：
該階等同於生成裸體影像，助理端已說明不做，改以上述「小面積衣著」達到接近的視覺強度，使用者可再評估。

### 平台與參數

- 模型：`soul_2` + `soul_id: 5fe3b6ba-1277-4822-9141-fb06eb3b93a0`，`quality: "2k"`、`aspect_ratio: "3:4"`
- 共 9 次生成（5 張初版 + 4 張重生），**全部通過平台審核，零 `nsfw`、零 `failed`**

### 五張的配置

| # | 露膚設計 | 場景 | 視角 | Job ID（採用版） |
|---|---|---|---|---|
| 01 | 黑絲質吊帶睡裙，V 領深至胸骨、單肩帶滑落、高衩露整條大腿 | 臥室床上 | 自拍（微俯角） | `8ffa3cbf-be33-4d9e-b462-1a24d91717cd` |
| 02 | 微型黑蕾絲三角內衣＋高衩蕾絲內褲＋蕾絲邊大腿襪＋金色腰鍊，肩、胸、肋、腰腹、髖全裸露 | 臥室全身鏡 | 鏡子自拍 | `c38b0ac2-a088-4850-b8e2-8f19f16c68e6` |
| 03 | 浴巾裹成平口，上緣壓在胸口最上方，另一條浴巾裹髖，腰腹與整條腿全露、帶水珠 | 浴室鏡前 | 鏡子自拍 | `9db9cf93-7762-460f-af3d-96c312a892e8` |
| 04 | **背面全裸**（側坐背對鏡頭，正面由白床單擋住），黑蕾絲內褲，背脊、腰窩、腿線全入鏡 | 臥室床上 | 他拍（平視） | `7eda9df3-86c4-4329-a1d1-57bd2bbccf18` |
| 05 | 黑色平口小可愛＋高腰內褲＋敞開的針織外套滑落雙肩，腰腹與雙腿全露 | 臥室落地窗前地板 | 他拍（平視） | `ccaa8f36-44d3-4bfc-b270-60b7b1a21abf` |

自拍 3／他拍 2。全部平視或微俯角，無仰拍。

### 生成後逐張檢查

**手部：9 張全數通過**（每一隻入鏡的手都做 3 倍放大裁切檢視，五指分明、無融合）。v2 記錄的 10-c 修法
（手放對比色表面／舉到臉旁）這批全程沿用，沒有再出現任何手部瑕疵——該規則可視為穩定。

**但這批出現一個新的系統性問題：🔴 身體描述一變長，夜晚光線就失守。**

初版 5 張裡有 3 張（01、02、04）的夜感不合格：畫面整體偏亮、沒有壓黑區，**02 右側甚至直接生出窗外
日光**，明確違反 prompt 裡寫的 `no daylight anywhere in frame`。03、05 則正常。

**原因判斷**：這批為了加大尺度，`SUBJECT`／`OUTFIT` 段落比前幾批長很多，把原本放在 prompt 尾端的
`[LIGHTING]` 稀釋掉了——模型優先執行前段的身體/服裝描述，尾端的光線指令權重下降。

**修法（已驗證有效）：把夜晚光線指令整段搬到 prompt 最前面**，在描述人物之前就先把「這是一張什麼光線
條件下拍的照片」講完：

```
A photo taken late at night in a dark bedroom with the ceiling light switched off.
The room is genuinely dark: the only light in the entire frame is [具名光源].
Everything more than a metre from that lamp falls three stops darker and crushes to
near black with no detail ... there is no daylight anywhere in frame.
SUBJECT: ...（人物描述接在後面）
```

01、04 各重生一次即完全正確（深黑背景、單一暖燈可見、壓黑區大面積）。**這條補充第 3-D 點：夜景指令
不只要寫得具體，還要放在 prompt 的最前面，不能放結尾。**

| # | 結果 | 細節 |
|---|---|---|
| 01（初版） | ⚠️ 夜感不合格，已重生 → `alternates/01_alt_bright_room.png` |
| 01（重生） | ✅ 通過 | 深黑房間、單一暖燈入鏡、天花板全黑；胸線與大腿如需求呈現 |
| 02（初版） | ⚠️ **生出窗外日光**，已重生 → `alternates/02_alt_daylight_window.png` |
| 02（重生1） | 🔴 **構圖bug**：畫面左側三分之一是整條純黑色塊，並出現一個亂生的 ⚠ 圖示（疑似把「左半壓黑」literal 執行成黑色矩形）。留檔 `alternates/02_alt_black_bar_framing_bug.png` |
| 02（重生2） | ✅ 通過 | 加寫 `subject centred and filling the frame edge to edge, no black bars, no borders, no letterboxing, no screen UI or icons` 後正常；鏡框燈泡排＋床頭藍色 LED 燈帶兩個色溫都到位。**唯一落差**：手機沒有入鏡，鏡子自拍的敘事弱化成一般站姿 |
| 03 | ✅ 通過 | 一次成功，夜感與露膚度皆達標；髖上的手五指分明 |
| 04（初版） | ⚠️ 夜感不合格，已重生 → `alternates/04_alt_bright_room.png` |
| 04（重生） | ✅ 通過 | 本批夜感最好的一張（大面積純黑、單一暖桌燈）；背面裸露、正面由白床單擋住，畫面中無任何裸露部位 |
| 05 | ✅ 通過 | 一次成功，蠟燭＋窗外城市光雙色溫、房內壓黑都正確 |

### 尺度備註（供發佈前判斷）

- **04 是本批最外顯的一張**（背面全裸、僅穿內褲）。畫面中沒有任何裸露部位，屬各平台普遍可接受的背影
  範圍，但仍是這五張裡尺度最高的，發佈前建議依平台政策與帳號調性再確認一次。
- 02 的蕾絲為半透材質，放大檢視確認為圖案密度足夠的蕾絲，無透出細節。

### 產出檔案

- `kols/iris-chen/images/daily_sexy_night_v4_bolder/01_bed_deepv_silkslip_selfie.png`
- `kols/iris-chen/images/daily_sexy_night_v4_bolder/02_mirror_micro_lace_stockings_selfie.png`
- `kols/iris-chen/images/daily_sexy_night_v4_bolder/03_bathroom_towel_wet_selfie.png`
- `kols/iris-chen/images/daily_sexy_night_v4_bolder/04_sidelying_bareback_candid.png`
- `kols/iris-chen/images/daily_sexy_night_v4_bolder/05_window_open_cardigan_candid.png`
- `alternates/` 內 4 張留檔（01/04 亮版、02 日光版、02 黑邊 bug 版）

**狀態：5 張皆通過內部 QA，待使用者核准。** 尚未上傳 Google Drive。

---

## 【規劃中，尚未生成】`daily_expression_v5` — 表情系統首次驗證批次（6 張，v2 規劃）

**狀態：⬜ 已規劃、待使用者核准後生成。本節不含任何實際生成結果。**

**背景**：外部觀看者指出 v1–v4 共 20 張「表情都是一號表情」，根因分析與解法見 `EXPRESSION_SYSTEM.md`
（同日建立，全 11 位角色適用）。本批是該系統的第一次實際驗證。

### ⚠️ 第一版規劃已被使用者退回，原因記錄在案

**第一版**（半夜開冰箱／書桌看筆電／玄關脫鞋／陽台曬衣服講電話／床尾／浴缸邊）被使用者退回：

> 「你規劃的這 6 個場景，都沒有讓我看文字的時候，會覺得生成出來有什麼展示性感的想像。」

**根因**：為了讓表情有可信的動機，第一版把場景全部推向「她在做一件日常瑣事、沒意識到鏡頭」——
開冰箱、看筆電、曬衣服、脫鞋。**表情層解決了，但展示層整個崩掉。** 對照 v4 就很明顯：v4 在文字階段
就讀得出性感（「V 領深至胸骨」「浴巾上緣壓在胸口最上方」「背面全裸」），v5 第一版卻是超大 T 恤、
針織背心、睡袍、格紋襯衫——全部是**舒適感**，不是**展示感**。

**教訓（已寫入 `EXPRESSION_SYSTEM.md` 第 3-b 節）**：**表情層與展示層是兩個獨立的層，不可互相犧牲。**
規劃時要分開檢查：這張圖的表情動機是什麼？這張圖的展示機制是什麼？兩個都要答得出來。

### 展示機制的三種類型（每張至少用一種，最好兩種）

| 類型 | 內容 | 例 |
|---|---|---|
| **A. 動作把身體拉長／彎折／打開** | 伸懶腰、後仰、手舉高、跨坐、趴姿翹腿、坐上檯面 | 跪坐後仰＝胸口打開＋腰線拉長 |
| **B. 衣服「正在發生什麼事」** | 濕透貼身、肩帶滑落中、下襬掀起、只扣一顆、綁帶鬆開 | 白背心被水淋濕貼在身上 |
| **C. 接觸點（觸覺聯想）** | 皮膚壓著玻璃／絲綢／檯面／水／地板 | 背貼落地窗、手撐淋浴間玻璃 |

**寫 prompt 時，展示機制要寫成畫面上看得到的物理事實**，不是形容詞——不要寫 `sexy pose`，
要寫 `both arms raised and pressed flat against the glass, which lifts her ribcage and lengthens her torso`。

### 六張的完整配置（v2）

| # | 場景（全新） | **展示機制** | 服裝 | 髮型 | 表情 | 象限 | 視角 |
|---|---|---|---|---|---|---|---|
| 01 | **淋浴間玻璃內側**（全新場景，前四批只到洗手台與浴缸） | **B＋C**：白色薄棉背心被水淋到全濕貼身、單手手掌與額頭壓在起霧的玻璃上、水從玻璃流下 | 濕透的白色薄棉細肩帶背心＋黑色高衩內褲 | H-1 濕髮全部往後撥 | **E-2 挑眉**（動機：隔著玻璃對外面拍她的人「幹嘛」） | 意識×低 | 他拍（隔玻璃） |
| 02 | **廚房流理台上坐著**（全新） | **A＋B**：坐上檯面雙腿交疊往前伸長、腳跟勾著櫃門；男友襯衫只扣中間兩顆，下襬因坐姿掀到大腿根 | 男友版白襯衫（只扣中間兩顆）＋光腳＋細金鎖骨鍊 | H-2 隔夜亂髮、一邊壓翹＋**中分空氣瀏海** | **E-5 抿嘴憋笑**（動機：半夜偷吃冰淇淋被室友抓到，忍住不笑） | 意識×高 | 自拍 |
| 03 | **沙發扶手上後仰伸懶腰**（沙發只用過一次，姿勢全新） | **A**：上身橫過扶手往後仰、頭往後垂、雙臂舉過頭伸展——整條身體線條被拉開；薄毯從身上滑落一半 | 黑色蕾絲三角內衣套組＋薄毯（滑落中） | H-3 鯊魚夾隨手盤 | **E-9 打呵欠／剛睡醒**（動機：真的想睡，伸懶腰打呵欠） | 無意識×低 | 他拍 |
| 04 | **落地窗玻璃前、背貼著玻璃**（v3-05 只是站在窗前，沒有接觸） | **A＋C**：背整個貼上冰的玻璃、雙手舉高手掌貼在玻璃上——抬高手臂拉開肋廓與腰線；身後是城市夜景 | 酒紅色微型蕾絲三角內衣＋同款高衩內褲＋蕾絲邊大腿襪＋金色腰鍊 | H-4 吹整滑順＋**深旁分** | **E-1 半瞇微笑**（招牌，本批唯一 1 張） | 意識×低 | 他拍 |
| 05 | **地毯上趴著、雙腿往後翹交疊晃**（全新姿勢） | **A**：趴姿使腰臀曲線最明顯、雙腿往後翹起交疊；上身以手肘撐起 | 黑色高衩連身緊身衣（bodysuit）＋光腳＋細金腳鍊 | H-5 低雙辮 | **E-8 專注做事**（動機：在擦腳指甲油，完全沒意識到鏡頭） | 無意識×低 | 自拍（手機立在地毯上） |
| 06 | **浴室洗手台上坐著、上身後仰用手撐鏡子**（前四批都是站在洗手台前） | **A＋B**：坐上檯面、上身往後仰用雙手撐住鏡面——胸口打開、頸線拉長；絲質睡裙肩帶滑落一邊 | 米白絲質細肩帶超短睡裙（一邊肩帶滑落）＋光腳＋金色小圈耳環 | H-4 變體：半盤＋**旁分長瀏海垂在兩頰** | **E-4 開口大笑**（動機：室友在門口講了一句很好笑的話）⚠️ 前 20 張零出現 | 意識×高 | 自拍 |

### 分配規則自檢（對照 `EXPRESSION_SYSTEM.md` 第七節）

- [x] 招牌 E-1 只有 1 張（04）
- [x] 至少 1 張沒在看鏡頭 → 03（E-9）、05（E-8）
- [x] 至少 1 張嘴巴打開看得到牙齒 → 06（E-4 大笑）、03（E-9 打呵欠）
- [x] 連續兩張不同象限 → 意低／意高／無低／意低／無低／意高，相鄰全部不同
- [x] 髮型 5 種狀態（H-1～H-5 全用上），且動了 3 次瀏海／分線（02 空氣瀏海、04 深旁分、06 旁分長瀏海）
- [x] 對照 Iris 禁用欄（「對鏡頭比 pose 的甜笑」「誇張驚訝」）→ 本批不用 E-6 驚訝，改用 E-5 抿嘴憋笑
      承接「被抓到」的情境，符合她 `character.md` 的內斂幽默
- [x] 自拍 3（02/05/06）／他拍 3（01/03/04）
- [x] **每張都有明確的展示機制**（A/B/C 各至少出現兩次）
- [x] 6 個場景、6 套服裝全部是 v1–v4 沒出現過的

**E-10 講話講到一半**這次沒排進來（6 個位置排不下），留給下一批——它跟 E-4、E-8 同屬前 20 張零出現、
價值高的類型。

### 使用者對本批的其他指示（2026-08-12）

1. **不重做舊素材**——「那些素材沒有不好，還是可以使用」，本批不沿用 v1–v4 任何一組 setup
2. **氛圍延續 v4**：性感、露膚；場景以夜晚、房間或室內居多
3. **異常確認機制**：只有環境或服裝跟設定稍有不同、但表情正常時，先給使用者看，不要自動重生
   （見 `SEXY_SCENE_LIBRARY.md` 第 10-a 點）

> **方法上的取捨（記錄在案）**：`SEXY_SCENE_LIBRARY.md` 第 14 點建議用「1 個 setup × 6 種表情」測，
> 那樣表情是唯一變因、實驗最乾淨。使用者選擇全部換新，所以本批同時變動場景/服裝/髮型/表情四個變數
> ——換得 6 張可各自成為貼文的素材，代價是表情效果無法與其他變因完全隔離。

### Prompt 撰寫規則（生成時必須遵守）

1. **夜間光線段落放 prompt 最前面**（`SEXY_SCENE_LIBRARY.md` 3-D）——v4 因服裝描述變長把光線擠到尾端，
   5 張有 3 張夜感失守
2. **表情寫滿三層**（`BROW:` / `EYES:` / `MOUTH:`）＋ 動機 ＋ 不對稱點 ＋ 眼睛落點
3. **展示機制寫成物理事實**，不要用 `sexy pose` 這種形容詞
4. **服裝寫滿五層**（上身／下身／鞋／外套或包／首飾）
5. **手**：放對比色表面上或舉到臉旁，不可小又懸空（10-c）——01 的手壓玻璃、04 的手貼玻璃、
   06 的手撐鏡面都天然符合
6. 全程平視或微俯角，無低角度仰拍（第 16 點）
7. 私密場景不加背景路人（第 9 點）

### 各張的夜間光線配方（放 prompt 最前面）

| # | 配方 |
|---|---|
| 01 | 淋浴間內的暖黃防水崁燈是畫面唯一光源，蒸氣散射成光暈，濕玻璃與白磁磚當反射面，浴室其他區域全黑 |
| 02 | 打開的冰箱門射出的冷白光是主光，由側前方打在她的腿與襯衫下襬；抽油煙機下的暖黃小燈為第二色溫；廚房其餘壓黑三級 |
| 03 | 電視冷藍白光從畫面外打在她後仰的臉與胸口；角落琥珀立燈為第二色溫；客廳後半全黑 |
| 04 | 窗外城市夜景的冷藍光是主光（從她背後穿過玻璃，形成邊緣光與半剪影）；房內床頭暖燈為第二色溫；地板與天花板壓黑 |
| 05 | 地毯旁的暖黃地燈低角度打在她的背與腿；手機螢幕的冷白光打在她低頭的臉；房間其餘全黑 |
| 06 | 鏡台兩側暖白 LED 燈條過曝成白塊；白磁磚當反射面；走廊冷白頂燈從半開的門切進來；浴室右半深黑 |

### 預估成本

6 張初版 ≈ 6 次生成；若有 AI 瑕疵需重生，預估 +1～3 次。以 v1–v4 實績推估總計 7–9 次。
