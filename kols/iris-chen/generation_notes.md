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

## 2026-08-12 黑色蕾絲內衣鏡前自拍短片（同一套方法，第三支參考片）

**背景**：使用者換第三支參考片（Yua Mikami 黑色蕾絲內衣鏡前自拍，工業風 loft 場景），一樣是「照一樣
的思路再做一支」——沿用不逐幀模仿動作、只借音樂/氛圍的方法。

### Step 1：起始畫面（兩次，第一次胸型不夠豐滿被打回）

- 模型：`soul_2` + `soul_id: 5fe3b6ba-1277-4822-9141-fb06eb3b93a0`，`aspect_ratio: "9:16"`
- 場景：工業風 loft 臥室，裸露水泥牆，落地窗，站立鏡前自拍，黑色蕾絲內衣（bra+內褲），姿勢維持
  正面站立、平視/微俯角自拍角度（避開她已知的拼貼bug觸發姿勢與新增的低角度仰拍禁令）
- **第一次**（Job ID `7016b842-4313-4a8a-98b3-e18fecfe179a`）：乾淨單張圖，但使用者反饋「胸太小了」
- **第二次**（Job ID `37874e4b-5f55-4669-bc2c-20f9a7e9b5bf`）：prompt 加強胸部描述——從單純寫
  `87cm bust, D cup` 數字改成額外加上「a very full, voluptuous bust」「deep prominent cleavage」
  「push-up lace bra that lifts and emphasizes her full chest」這類具體視覺強化字眼，同時保留原本
  的數字設定不變。使用者核准這一版。
- **教訓**：光寫身材數字（cm/cup）不保證模型會忠實呈現到位——尤其配上某些內衣剪裁（如三角軟罩杯款）
  視覺上會顯得比數字本身更小。之後這類需要強調豐滿胸型的場景，除了寫數字，也要疊加具體的視覺強化
  描述（豐滿/深乳溝/聚攏托高罩杯款式），不能只依賴 `profile.json` 的 measurements 數字。

**起始畫面（第二版）已核准。**

### Step 2：動態短片（`kling3_0`，多鏡頭切換）

- 參考圖：核准版 `media_id: 20547602-2cda-4520-9504-3e68e001f78c`
- 四個鏡頭設計（呼應參考片的鏡前自拍+近距離美妝手勢+側身輪廓構圖）：Shot 1 鏡前自拍中景，微重心
  轉換；Shot 2 近景，手指靠近嘴唇的沉思手勢，微俯角；Shot 3 側身 3/4 角度，手撥頭髮；Shot 4 近景
  正面，回頭微笑收尾。全程平視或微俯角，明確排除低角度仰拍
- 手機道具處理：prompt 明確要求「手機自然穩定地被手握住，不會有飄浮或不自然的移動」，避免類似木桶
  案例的道具物理問題
- 模型：`kling3_0`，`duration: 15`、`aspect_ratio: "9:16"`；系統再次判定符合 preset「ELEVATE」，
  選擇按原字面生成
- Job ID `2ac4b577-74bd-4881-b0e1-3d3620586505`，輸出 720×1280、h264/aac、~15.04s
- 抽 11 個時間點目視核對，全數通過：身分穩定、四種鏡頭/構圖明顯不同、手機握持自然無飄浮、無拼貼、
  無手部變形、全片無低角度仰拍

### Step 3：混音

同前兩支的做法：參考片音軌只有 ~11.05s，短於影片的 ~15.04s，用 `ffmpeg -stream_loop -1` 循環音軌
蓋滿全長，片尾 14.5s–15.0s 加 `afade=out`。輸出 `iris_lingerie_reel_r1.mp4`
（720×1280、h264/aac、~15.04s）。**同樣的授權限制**：音樂來自使用者提供的第三方影片，內部驗證用，
未取得商用授權。

### 產出檔案

- `kols/iris-chen/images/lingerie_mirror_r1/start_frame.png`（已核准起始畫面，胸型加強版）
- `kols/iris-chen/videos/lingerie_mirror_r1/iris_lingerie_reel_r1.mp4`（720×1280、h264/aac、~15.04s，
  音軌為使用者提供的第三方音樂迴圈+淡出，未經授權，僅供內部驗證）
