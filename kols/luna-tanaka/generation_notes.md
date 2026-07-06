# Luna Tanaka — Generation Notes

## Soul Training

- **Soul ID**: `1bfab2ce-cfa5-4026-93fa-e5c91b469c7a`
- **Model**: `soul_2`
- **Status**: Training initiated 2026-06-29
- **Training images** (8 total):
  - 4 face reference images from `images/face_reference/` (ref_01 through ref_04)
  - 4 body-correct images from Higgsfield (童顏巨乳 body type, wrong clothes but correct face+figure):
    - `hf_20260626_040502_fe1befb3-e839-457a-b5fd-0b0ba7380b67.png`
    - `hf_20260626_040502_8dcbcd43-b57c-4a9f-a8e9-f16492fe4f0e.png`
    - `hf_20260626_040502_d546c722-e746-4f74-951a-0befbc871758.png`
    - `hf_20260626_040502_1c6a724e-8db8-48f9-8d2b-b2aa0c159c51.png`

## Appearance Summary

- **Age**: 20
- **Ethnicity**: Japanese
- **Height**: 155cm
- **Hair**: Black, fine, straight — center-parted, chin-length bob
- **Eyes**: Large, round, dark brown
- **Skin**: Fair, porcelain
- **Body**: 童顏巨乳 (youthful face, curvaceous figure)
- **Style**: Japanese soft girl meets vintage — white lace, floral cotton, oversized knits, mary jane shoes, cream/beige palette

## 訓練後測試生成（2026-06-29）

訓練完成後用 Soul ID 生成 6 張測試圖，確認身份一致性，結果通過。

### 場景 1 — 京都街頭（白色蕾絲上衣 + 碎花裙）

- [圖 1](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154140_dd6cb5c5-9ec5-465f-9db0-bf2209b46132.png)
- [圖 2](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154140_92c8e138-8940-42a5-a51c-b1654f8ce8ad.png)

### 場景 2 — 咖啡廳窗邊（奶油色 oversized 毛衣）

- [圖 3](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154146_b01362a2-1483-4281-955d-6da5e04d4343.png)
- [圖 4](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154147_ce1d5af4-5c36-4914-b716-44a2cac263cb.png)

### 場景 3 — 公園黃金時段全身（白色碎花洋裝）

- [圖 5](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154152_1c07c5db-9dba-45c2-860a-80657087dbf1.png)
- [圖 6](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154152_762d6881-9ab9-493e-af66-cf9cbc4f42fe.png)

### 測試用 Prompt 結構

```
20-year-old Japanese girl, black center-parted chin-length bob, large round dark brown eyes,
fair porcelain skin, petite curvy figure with full chest and slim waist,
[SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING],
film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

## Usage

```python
# Generate with Soul V2
generate_image(
    model="soul_2",
    soul_id="1bfab2ce-cfa5-4026-93fa-e5c91b469c7a",
    prompt="20-year-old Japanese girl, black center-parted chin-length bob, ..."
)
```

---

## 親密場景模板（2026-07 新增）

> 方向更新後的新場景類型：臥室早晨、浴室鏡前、居家窩著、飯店房間。

### 核心 Prompt 基礎結構（不變）

```
20-year-old Japanese girl, black center-parted chin-length bob, large round dark brown eyes, fair porcelain skin, petite curvy figure with full chest and slim waist, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

---

### 場景 1 — 臥室早晨（Bedroom Morning）

**氛圍**：京都的早晨，安靜，紙拉門或薄窗簾透進的柔光，她在白色被子裡慢慢醒來。

**Prompt（圖片）**：
```
20-year-old Japanese girl, black center-parted chin-length bob, large round dark brown eyes, fair porcelain skin, petite curvy figure with full chest and slim waist, lying in bed on white linen bedding in a Kyoto room, soft diffused morning light through shoji screen or sheer white curtain, wearing thin white cotton slip or camisole, hair slightly disheveled from sleep, drowsy soft expression looking at camera, slightly overhead angle, film grain, candid lifestyle photo, warm cream tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Soft morning light filtering through shoji screen, her face half-hidden under white linen blanket, eyes slowly opening.
Shot 2: She shifts slightly in bed, pulling blanket up to chin, revealing only her face and bare shoulders.
Shot 3: Close-up of her large round eyes looking sleepily at camera, black hair splayed softly on pillow.
Shot 4: She stretches one arm out from blanket, settles back into pillow, eyes closing slightly again.
Shot on iPhone, warm soft grain, warm cream tones, no over-sharpening, gentle morning light, stable camera, feels like a real person filmed this.
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

**氛圍**：洗完澡，白瓷般的皮膚，濕的黑色短髮，浴巾，浴室鏡，極安靜。

**Prompt（圖片）**：
```
20-year-old Japanese girl, black center-parted chin-length bob, large round dark brown eyes, fair porcelain skin, petite curvy figure with full chest and slim waist, standing in front of bathroom mirror, hair wet and damp from shower, wearing white bath towel wrapped around body, slight steam on bathroom mirror edges, looking at reflection with soft quiet expression, warm bathroom lighting, film grain, candid lifestyle photo, warm cream tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Bathroom mirror showing her reflection in white towel, damp black hair, steamy mirror edges.
Shot 2: She gently squeezes water from her hair with towel, looking down, then up at mirror.
Shot 3: Close-up of her fair porcelain face in mirror, post-shower natural skin, no makeup.
Shot 4: She meets her own gaze in mirror, then glances toward camera, soft quiet expression.
Shot on iPhone, warm soft grain, warm cream tones, no over-sharpening, warm bathroom light, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

### 場景 3 — 居家窩著（Home Lounging）

**氛圍**：京都老公寓，木地板或榻榻米，她在最放鬆的狀態，Mochi 可能在旁邊，輕薄的家居服。

**Prompt（圖片）**：
```
20-year-old Japanese girl, black center-parted chin-length bob, large round dark brown eyes, fair porcelain skin, petite curvy figure with full chest and slim waist, sitting cross-legged on wooden floor of Kyoto apartment, wearing thin white cotton camisole and light linen shorts, afternoon light through window casting soft shadows, small cat curled nearby, relaxed natural expression looking at camera, film grain, candid lifestyle photo, warm cream tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Wide shot of Kyoto apartment wooden floor, she sits cross-legged in light home clothes, cat nearby.
Shot 2: She picks up teacup, holds it in both hands, looks out window, at ease.
Shot 3: Close-up of her face, warm afternoon light on fair skin, small content smile.
Shot 4: Cat walks into frame, she reaches down to pet it, looks up at camera with soft eyes.
Shot on iPhone, warm soft grain, warm cream tones, no over-sharpening, afternoon natural light, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

### 場景 4 — 飯店房間（Hotel Room）

**氛圍**：東京或大阪出差 / 旅行，飯店的白床，城市夜景，那種陌生城市裡一個人的安靜感。

**Prompt（圖片）**：
```
20-year-old Japanese girl, black center-parted chin-length bob, large round dark brown eyes, fair porcelain skin, petite curvy figure with full chest and slim waist, sitting on hotel bed with white crisp bedding, Tokyo or Osaka city view through floor-to-ceiling window behind her, wearing white lace camisole or thin cotton pajama top, looking toward window with quiet introspective expression, hotel warm ambient lighting mixed with city glow, film grain, candid lifestyle photo, warm cream tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Hotel room with city lights through large window, she sits on white bed, looking at the city view.
Shot 2: She moves to window, places one hand on glass, looking down at the city below.
Shot 3: Close-up of her face from the side, soft hotel light, city glow reflecting on her skin.
Shot 4: She turns slowly to look at camera, quiet and calm, city lights visible behind her.
Shot on iPhone, warm soft grain, warm cream tones, no over-sharpening, hotel ambient and city glow lighting, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

## 舞蹈影片記錄（2026-07-06）

### Start Frame

| Job ID | 說明 | Media ID |
|--------|------|----------|
| `fe49678d` | 三分之三身站立，black PU leather halter dress，izakaya 背景 | `710cccfa` |

### 音樂

| 音樂 | Audio Media ID |
|------|---------------|
| TikTok 熱門卡點音樂（TikSave） | `caae7993` |

### 已生成影片清單

| 版本 | 時長 | 服裝 | 背景 | Job ID | generate_audio | 狀態 |
|------|------|------|------|--------|---------------|------|
| dance_v1 | 15s | black PU leather halter dress | Tokyo izakaya neon alley night | `322a8d14` | false ✓ | ✅ 完成（待用戶確認） |

### 舞蹈影片 Prompt 模板（已驗證）

```
20-year-old Japanese girl, black center-parted chin-length bob, large round dark brown eyes,
fair porcelain skin, petite curvy figure with full chest and slim waist,
wearing black PU leather halter dress, mid-thigh length, form-fitting,
THREE QUARTER BODY SHOT, mid-thigh up, no shoes shown,
chest bounce and jiggle physics,
energetic J-pop dance, body rolling, hip sway, playful arm movements, bouncing to the beat,
Tokyo izakaya neon alley night background, warm neon lights, urban Japanese atmosphere,
synced to the music beat and rhythm, dynamic dance movement, confident sensual energy,
shot on iPhone, natural lighting, warm tones,
single continuous shot no camera cuts, character always centered in frame, staying within frame boundaries at all times
```

### 舞蹈影片生成 Checklist

- `generate_audio: false` ← 必填，否則模型自己生成音樂蓋掉 audio_reference
- `audio` role 帶入正確 media_id（`caae7993`）
- `start_image` 帶入正確 media_id（`710cccfa`）
- `THREE QUARTER BODY SHOT` 在 prompt 裡
- `centered in frame, staying within frame boundaries at all times`（防黑邊）
- `single continuous shot no camera cuts`（防鏡頭切換）
- 背景無 mirror（mirror 會讓模型誤判成鏡頭切換）
- 無 NSFW 觸發詞（避免：sexy expression, sensual isolation, snaps hips hard）
