# Ananya Kapoor — Generation Notes

## Soul Training

- **Soul ID**: `fac82296-8c69-4c34-b352-1b398c8b8e1c`
- **Model**: `soul_2`
- **Status**: Training completed 2026-06-29
- **Training images** (6 total):
  - 4 face reference images from `images/face_reference/` (ref_01 through ref_04)
  - 2 supplementary images generated with `seedream_v4_5` (natural lashes, no dramatic false lashes):
    - Job ID: `(supplementary images generated during training prep session)`

## Appearance Summary

- **Age**: 23
- **Ethnicity**: Indian (Punjabi)
- **Height**: 165cm
- **Hair**: Dark brown, long, naturally wavy-curly, loose or loose braid
- **Eyes**: Large, deep brown, natural lashes (not dramatic)
- **Skin**: Warm golden-brown, glowing
- **Body**: Curvy and toned — dancer/yogi physique, graceful and strong
- **Style**: Yoga sets, kurta, flowy harem pants, jewel tones, midriff-baring co-ords

## 訓練後測試生成（2026-06-29）

訓練完成後用 Soul ID 生成 6 張測試圖，確認身份一致性。

### 場景 1 — 孟買街頭（flowy floral kurta + wide-leg trousers）

- [圖 1](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162345_49900939-b0dd-450f-8d9d-cfc91e458eda.png)
- [圖 2](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162345_a511c9e8-36fa-4d52-b057-fcfc6798d7d6.png)

### 場景 2 — 咖啡廳窗邊（white cotton salwar with embroidery）

- [圖 3](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162355_5c7f246d-883d-4766-b5de-003190c3ce49.png)
- [圖 4](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162356_b2c137ba-4694-4a39-a590-bfbea287bd52.png)

### 場景 3 — 公園黃金時段（sage green saree styled contemporary）

- [圖 5](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162358_3c7d4d2e-dd21-4839-b749-ac061e86c9ff.png)
- [圖 6](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162358_c58e00c3-b3d1-425c-bda4-9b0acfe5112d.png)

> ✅ 測試圖已上傳至 `images/soul_test_v1/`（共 6 張）。

## 使用者回饋（2026-06-30）

### 場景 1（孟買街頭）— ❌ 穿搭不滿意
- `flowy floral kurta + wide-leg trousers` 這類造型**以後不要再用**，很不好看
- Ananya 的穿搭應以 yoga set、crop top、midriff-baring co-ords、緊身褲/棉質短裙為主，保持身材線條可見

### 場景 2（咖啡廳窗邊）— ✅ 可以

### 場景 3（公園黃金時段）— ⚠️ 構圖雷同（已廢棄，見下方重生成版本）
- 兩張圖拍攝角度、人物比例幾乎相同，看起來像同一套圖
- 同一場景的兩張圖必須刻意安排不同構圖（例如：一張廣角/一張近景，或一張正面/一張側面回眸）
- 參見 [[feedback-image-composition-variety]]

---

## 重生成批次（2026-06-30）

### 場景 1 v2 — 孟買咖啡廳（深寶石藍 wrap dress）✅ 通過

**穿搭**：deep jewel blue fitted wrap dress with V-neckline

| 構圖 | Job ID | CDN URL |
|------|--------|---------|
| 3/4 身，窗邊坐姿，面朝鏡頭 | `c9d7cc37-be7f-4bd8-a4e9-c17434173bdc` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260630_131514_c9d7cc37-be7f-4bd8-a4e9-c17434173bdc.png |
| 臉部近景，側臉望窗，bokeh 背景 | `64e02c03-a868-4b08-87ed-0fe9bb417f13` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260630_131518_64e02c03-a868-4b08-87ed-0fe9bb417f13.png |

**Prompts：**
```
# 圖1（3/4 身）
23-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves, large expressive dark eyes, natural lashes, elegant facial features, graceful curvy figure, sitting by large window in upscale Mumbai café, wearing deep jewel blue fitted wrap dress with V-neckline that hugs her curves, 3/4 body shot, slight smile looking at camera, soft natural window light, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style

# 圖2（臉部近景）
23-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves, large expressive dark eyes, natural lashes, elegant facial features, graceful curvy figure, inside upscale Mumbai café, wearing deep jewel blue fitted wrap dress with V-neckline, close-up portrait shot from shoulders up, slightly turned profile gazing toward window light, warm ambient bokeh background, confident relaxed expression, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

---

### 場景 3 v2 — Marine Drive 海岸散步道（鏽紅 crop top + 白色闊腿褲）✅ 通過

**穿搭**：rust terracotta fitted crop top + high-waist white wide-leg trousers

| 構圖 | Job ID | CDN URL |
|------|--------|---------|
| 廣角，人物小，海岸線天際線為主 | `abd00952-004c-480d-bb92-cc9223f54775` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260630_131744_abd00952-004c-480d-bb92-cc9223f54775.png |
| 臉部近景，海景 bokeh，黃金時段側光 | `4e00d579-15c3-488f-839f-5ff802078d13` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260630_131750_4e00d579-15c3-488f-839f-5ff802078d13.png |

**Prompts：**
```
# 圖1（廣角）
23-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves, large expressive dark eyes, natural lashes, graceful curvy figure, standing on Marine Drive promenade Mumbai, wearing rust terracotta fitted crop top and high-waist white wide-leg trousers, wide angle shot with person relatively small in frame, Mumbai skyline and Arabian Sea in background, golden hour warm light, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style

# 圖2（臉部近景）
23-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves, large expressive dark eyes, natural lashes, graceful curvy figure, on Marine Drive promenade Mumbai, wearing rust terracotta fitted crop top and high-waist white wide-leg trousers, close-up portrait from shoulders up, relaxed confident expression slightly looking away, Arabian Sea soft bokeh background, golden hour warm light, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

### 測試用 Prompt 結構

```
22-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves,
large expressive dark eyes, natural lashes (not dramatic), elegant facial features,
slender graceful figure, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING],
film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

## Usage

```python
# Generate with Soul V2
generate_image(
    model="soul_2",
    soul_id="fac82296-8c69-4c34-b352-1b398c8b8e1c",
    prompt="22-year-old Indian woman, warm golden-brown skin, long dark black hair, ..."
)
```

---

## 親密場景模板（2026-07 新增）

> 方向更新後的新場景類型：臥室早晨、浴室鏡前、居家放鬆、飯店房間。

### 核心 Prompt 基礎結構（不變）

```
22-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves, large expressive dark eyes, natural lashes (not dramatic), elegant facial features, curvy dancer/yogi figure — 86cm bust (D cup), 60cm waist, 91cm hips, toned strong legs, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

**身材數字**（來自 `profile.json` → `identity.appearance.measurements`）：bust 86cm / waist 60cm / hip 91cm / cup D / height 165cm。以後寫 prompt 時直接帶入這些具體數字，不要只用「slender」「graceful」這類模糊形容詞（現有已通過的舊圖不受影響，僅供未來生成批次參考）。

**穿搭禁止**：`flowy floral kurta + wide-leg trousers` 類型不再使用。改以 yoga set、crop top、midriff-baring co-ords、緊身褲 / 棉質短裙為主。

---

### 場景 1 — 臥室早晨（Bedroom Morning）

**氛圍**：孟買的早晨是熱的，她在薄被子裡醒來，吊扇在轉，深色皮膚在晨光下的金色感。

**Prompt（圖片）**：
```
22-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves, large expressive dark eyes, natural lashes, elegant facial features, slender graceful figure, lying in bed on white cotton bedding in Mumbai apartment, thin ceiling fan visible above, warm tropical morning light from window, wearing thin cotton sleeveless top and light cotton sleep shorts, hair loosely spread on pillow, drowsy relaxed expression looking at camera, slightly overhead angle, film grain, candid lifestyle photo, warm golden tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Warm Mumbai morning light, she lies in bed under thin white sheet, ceiling fan slowly turning, long dark hair on pillow.
Shot 2: She stretches her arms above her head, arching slightly, then settles back into bed.
Shot 3: Close-up of her face, warm golden-brown skin catching morning light, eyes half-open, no makeup.
Shot 4: She rolls to her side, looks directly at camera with a slow confident gaze, completely at ease.
Shot on iPhone, warm soft grain, warm golden tones, no over-sharpening, tropical morning light, stable camera, feels like a real person filmed this.
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

**氛圍**：洗完澡，深色皮膚在浴室暖燈下的自然光澤感，濕的長捲髮，浴巾，完全自在。

**Prompt（圖片）**：
```
22-year-old Indian woman, warm golden-brown skin, long dark black hair wet and damp from shower, large expressive dark eyes, natural lashes, elegant facial features, slender graceful figure with visible curves, standing in front of bathroom mirror, wearing white bath towel wrapped around body, slight steam on mirror edges, looking at reflection with confident relaxed expression, warm bathroom lighting highlighting skin's natural glow, film grain, candid lifestyle photo, warm golden tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Bathroom mirror showing her in white towel, long dark wavy hair wet and heavy, steamy edges.
Shot 2: She gathers her wet hair to one side, glancing at her reflection, unhurried.
Shot 3: Close-up of her face in mirror, warm golden-brown skin with natural post-shower glow, completely bare of makeup.
Shot 4: She meets her own eyes in mirror confidently, then looks toward camera with a subtle smile.
Shot on iPhone, warm soft grain, warm golden tones, no over-sharpening, warm bathroom light, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

### 場景 3 — 居家放鬆（Home Lounging）

**氛圍**：孟買公寓，瑜伽墊旁，最少的衣服，最真實的狀態，她在這裡完全是自己。

**Prompt（圖片）**：
```
22-year-old Indian woman, warm golden-brown skin, long dark black hair loosely tied or down, large expressive dark eyes, natural lashes, elegant facial features, slender graceful figure, sitting cross-legged on yoga mat or wooden floor in Mumbai apartment, wearing black sports bra and cotton high-waist shorts, afternoon light from window, relaxed natural expression, looking at camera with easy confidence, film grain, candid lifestyle photo, warm golden tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Mumbai apartment floor, she sits cross-legged on yoga mat, natural afternoon light, wearing crop top and shorts.
Shot 2: She leans back on her hands, legs stretched out, looking up at ceiling, completely relaxed.
Shot 3: Close-up of her face, warm golden light on skin, a quiet confident expression.
Shot 4: She glances at camera directly, unhurried, completely comfortable in her own space.
Shot on iPhone, warm soft grain, warm golden tones, no over-sharpening, afternoon natural light, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

### 場景 4 — 飯店房間（Hotel Room）

**氛圍**：Goa、Bali 或出差城市，飯店的白床和她深色皮膚的天然對比，窗外是海或城市。

**Prompt（圖片）**：
```
22-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves, large expressive dark eyes, natural lashes, elegant facial features, slender graceful figure, sitting on hotel bed with crisp white bedding, tropical resort or city hotel setting, floor-to-ceiling window with sea view or city view behind her, wearing black cotton sleeveless crop top, looking toward window with relaxed expression, hotel warm lighting, film grain, candid lifestyle photo, warm golden tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Hotel room, she sits on white bed, tropical light through large window, deep contrast of her skin against white bedding.
Shot 2: She moves to window, leans against frame, looking out at sea or city, confident and unhurried.
Shot 3: Close-up of her face in profile, warm light on golden-brown skin, city or ocean visible behind.
Shot 4: She turns from window, makes eye contact with camera, easy and direct.
Shot on iPhone, warm soft grain, warm golden tones, no over-sharpening, hotel ambient and natural light, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

## 舞蹈影片記錄（2026-07-06）

### 音樂

| 音樂 | Audio Media ID |
|------|---------------|
| TikTok 熱門卡點音樂（同 Camille） | `a7d47bd0` |

### ⚠️ 失敗分析：Start Image 含露膚服裝導致生成 Failed

**根本原因**：Higgsfield seedance_2_0 在影片生成前會對 start_image 進行像素層級的內容審核。如果 start_image 含有露腹、露胸等 revealing 服裝，生成任務會直接返回 `status: "failed"`（非 `status: "nsfw"`）。

**失敗嘗試記錄**：

| Start Frame 服裝 | Start Frame Job/Media | 影片 Job | 狀態 | 原因 |
|-----------------|----------------------|---------|------|------|
| 肚皮舞服裝（belly dance bra top） | 直接用 CDN URL | `f62d5caa` | ❌ failed | 露腹/露胸服裝被過濾 |
| 瑜伽 crop top（midriff 外露） | `18d6c40a` / `b2715eb2` | `3066d9c4` | ❌ failed | crop top 露腰被過濾 |
| 保守 T-shirt start frame | 新生成 | `e549fc90` | ❌ failed | 仍失敗（原因未明） |

**已嘗試繞過方式**：
- 換成保守 T-shirt — 仍失敗
- 不使用 start_image（無臉部鎖定） — 可生成，但臉部品質差，不推薦

### 新 Start Frame（2026-07-06 新生成，待確認）

| Job ID | 說明 | 狀態 |
|--------|------|------|
| `0bf0eb63` | gold metallic deep-V dress（相對保守的 revealing 測試） | 待確認 |

### 待辦事項

- Ananya 舞蹈影片：start_image revealing 服裝問題未完全解決，下次嘗試使用保守 tank top + leggings 的 start frame

### 舞蹈影片生成 Checklist

- `generate_audio: false` ← 必填
- `audio` role 帶入正確 media_id（`a7d47bd0`）
- `start_image` 必須使用非 revealing 服裝（無露腹、無露胸 bra top）
- `THREE QUARTER BODY SHOT` 在 prompt 裡
- `centered in frame, staying within frame boundaries at all times`（防黑邊）
- `single continuous shot no camera cuts`（防鏡頭切換）
- 背景無 mirror
- 無 NSFW 觸發詞

---

## 日常自拍影片記錄（2026-07-07）

> 方向：男性受眾，浴室剛洗完澡，濕髮，毛巾裹身展示鎖骨和肩膀，非廣告感。
> 模型：`kling3_0`（單鏡頭，臉部鎖定）
> 完整 SOP 見 `DAILY_VIDEO_SOP.md`

### Start Frame（日常服裝）

| Job ID | 說明 | 已選 | Media ID |
|--------|------|------|----------|
| `7797c1d9` | 浴室，白色浴巾裹身，濕髮，露鎖骨和肩膀，自然看鏡頭 | ✅ 已選 | `d94c27c9` |
| `1527bfbf` | 同場景，第二張備選 | — | — |

**Start Frame Prompt（已驗證）**：
```
23-year-old Indian woman, beautiful face, dark expressive eyes,
long dark hair wet and damp from shower, light brown warm skin, slim figure with curves,
standing in bathroom after shower, wrapped in white bath towel around body,
towel slightly loose at top showing collarbone and shoulders,
looking at camera with natural expression, phone selfie angle,
soft warm bathroom lighting, candid self-portrait feel,
shot on iPhone front camera, half body from waist up, warm tones, film grain
```

### 日常影片

| 版本 | 場景 | 服裝 | Job ID | 模型 | 狀態 |
|------|------|------|--------|------|------|
| daily_v1 | 浴室鏡前，剛洗完澡，濕髮，毛巾裹身，看鏡頭 | 白色浴巾，露鎖骨 | `59dcbb98` | kling3_0 | ✅ 批准 |

**影片 Prompt（已驗證）**：
```
23-year-old Indian woman, beautiful face, dark expressive eyes,
long dark wavy hair wet from shower, warm light brown skin,
standing in bathroom after shower, wrapped in white bath towel,
towel slightly loose showing collarbone and bare shoulders,
one hand holding towel near chest, looking directly at camera with natural confident expression,
soft warm bathroom lighting,
single continuous shot, phone selfie casual feel, warm tones
```

**參數**：
```python
model = "kling3_0"
medias = [{"role": "start_image", "value": "d94c27c9"}]
sound = "on"
aspect_ratio = "9:16"
duration = 10
```

---

## 2026-07-25 新增：身材數字 + 風格參考

- 核心 prompt 模板（見上方「核心 Prompt 基礎結構」）已補上實際身材數字（bust 86cm / waist 60cm / hip 91cm / cup D），取代模糊的 slender/graceful 形容詞。此為未來生成批次的補充，不影響現有已核准圖像、soul_id 或訓練紀錄。
- 光源配方請參照 `SEXY_SCENE_LIBRARY.md`「3. 光源」的最新修正：室內親密場景（晨起/浴室/居家）維持原本「混合不均勻光」邏輯；戶外/生活風格場景改用新的「討喜自然光（黃金時段/戶外強光）+ 淺景深虛化 + 清晰高畫質」配方。
- Ananya 的內容以孟買瑜伽、舞蹈、戶外生活風格為主，多數場景屬於戶外/明亮自然光類型，因此新配方適用於她大部分的內容（Marine Drive 海岸、公園黃金時段、健身/舞蹈等場景）；僅浴室、臥室晨起等室內親密場景沿用舊的混合光配方。
