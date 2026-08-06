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
