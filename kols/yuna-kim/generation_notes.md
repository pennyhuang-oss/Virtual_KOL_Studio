# Yuna Kim — Generation Notes

## Soul Training

- **Soul ID**: `235794a5-2eff-45fb-91b4-3232910afefa`
- **Model**: `soul_2`
- **Status**: Training completed 2026-06-29
- **Training images** (5 total):
  - 4 face reference images from `images/face_reference/` (ref_01 through ref_04)
  - 1 supplementary image generated during training prep

## Appearance Summary

- **Age**: 21
- **Ethnicity**: Korean
- **Height**: 168cm
- **Hair**: Dark brown to black, natural wavy with airy volume, collarbone-length
- **Eyes**: Large, double eyelid, bright — focal point of every look
- **Skin**: Fair, porcelain, well-maintained
- **Body**: Tall and slender
- **Style**: K-sweet meets Y2K — mini skirts, oversized cardigans, platform shoes. Always one unexpected element.

## 測試圖（soul_test_v1）

生成日期：2026-06-30，共 6 張，3 個場景各 2 張。

### 場景 1 — 自拍（Selfie）
**檔案:** `selfie_01.png`, `selfie_02.png`
**Prompt:**
```
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black hair with wispy ends and cherry hair clips, 168cm, close-up front-facing selfie shot, slightly overhead angle looking down at camera, natural relaxed smile, wearing oversized cream university sweater, soft indoor lighting with ring light glow in background, looks like a photo taken by her own phone front camera, warm tones, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

### 場景 2 — 江南咖啡廳（Gangnam Café）
**檔案:** `cafe_01.png`, `cafe_02.png`
**Prompt:**
```
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black wavy hair, 168cm, sitting by window in Gangnam café Seoul, both hands resting on table, slightly turning head to look out the window, wearing mini skirt and oversized cardigan with chunky chain necklace, natural window light casting soft shadows, clean table with no drinks, full body sitting pose, warm tones, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

### 場景 3 — 弘大街頭（Hongdae Street）
**檔案:** `street_01.png`, `street_02.png`
**Prompt:**
```
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black wavy hair, 168cm, walking on Hongdae outdoor pedestrian street Seoul, golden hour evening light, wearing Y2K style plaid mini skirt and white fitted top with vintage small shoulder bag, 3/4 body candid street shot, warm orange golden light, background with blurred street scenery, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

### Prompt 結構模板

```
[age]-year-old Korean woman, [skin], [eyes], [hair], [height], [scene], [outfit], [angle/composition], [lighting], film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

### 注意事項

- 自拍 prompt 描述「輸出視角」而非「拍照動作」，避免手機入鏡或第三人稱角度
- 參考 Iris Chen 自拍 prompt 結構（`kols/iris-chen/generation_notes.md`）

## Usage

```python
# Generate with Soul V2
generate_image(
    model="soul_2",
    soul_id="235794a5-2eff-45fb-91b4-3232910afefa",
    prompt="21-year-old Korean woman, fair porcelain skin, large double-eyelid eyes, ..."
)
```

---

## 親密場景模板（2026-07 新增）

> 方向更新後的新場景類型：臥室早晨、浴室鏡前、居家慵懶、飯店房間。

### 核心 Prompt 基礎結構（不變）

```
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black hair with wispy ends, 168cm, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

---

### 場景 1 — 臥室早晨（Bedroom Morning）

**氛圍**：首爾的早晨，她還在床上，tall slender 身材在白色寢具裡，cherry hair clips 散落在枕頭邊，有點賴床的少女感。

**Prompt（圖片）**：
```
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black hair with wispy ends, 168cm, lying in bed on white fluffy bedding in Seoul apartment, morning soft light from window, wearing oversized white cotton sleep top, hair loosely spread on pillow with a few small hair clips tangled in, drowsy half-awake expression, slightly overhead angle looking down at camera, warm tones, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Seoul apartment bedroom, she lies under white fluffy bedding, morning light soft through curtains, dark hair spread on pillow.
Shot 2: She stirs, pulls blanket up to cover chin, eyes slowly opening, still half-asleep.
Shot 3: Close-up of her large double-lidded eyes blinking, fair skin with slight sleep flush, totally natural.
Shot 4: She reaches up to touch her hair absently, then notices camera and gives a lazy half-smile.
Shot on iPhone, warm soft grain, warm tones, no over-sharpening, soft morning light, stable camera, feels like a real person filmed this.
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

**氛圍**：洗完澡，K-beauty skincare 程序，浴室鏡前，濕髮，白瓷皮膚，那種韓國女生洗完澡很認真保養的感覺。

**Prompt（圖片）**：
```
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black hair wet and damp, 168cm, standing in front of bathroom mirror, wearing white bath towel wrapped around slender body, applying skincare or toner to face with hand, slight steam on mirror, bathroom warm light, relaxed concentrated expression looking at reflection, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Bathroom mirror, she stands in white towel, damp dark hair, patting skincare product onto face.
Shot 2: She tilts head slightly, checking her reflection, smoothing product along jawline.
Shot 3: Close-up of her face in mirror, porcelain skin post-shower, no makeup, large eyes clear and relaxed.
Shot 4: She catches her own gaze in mirror, then glances toward camera with a natural small smile.
Shot on iPhone, warm soft grain, warm tones, no over-sharpening, warm bathroom light, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

### 場景 3 — 居家慵懶（Home Lounging）

**氛圍**：首爾公寓，Y2K 風格家居，沙發上，oversized 衣服，高挑的身材窩在沙發裡的反差感。

**Prompt（圖片）**：
```
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black hair with wispy ends, 168cm, curled up on sofa in Seoul apartment, wearing oversized pastel cardigan and mini shorts, knees pulled to chest, phone in hand, warm afternoon light from window, relaxed unguarded expression, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Seoul apartment sofa, she curls up with knees to chest, oversized cardigan, scrolling phone, afternoon light.
Shot 2: She shifts to lean sideways, long legs tucked, looking toward window with dreamy expression.
Shot 3: Close-up of her face, soft light on fair skin, large eyes slightly unfocused, at ease.
Shot 4: She notices camera, tucks hair behind ear, gives a natural unposed look.
Shot on iPhone, warm soft grain, warm tones, no over-sharpening, afternoon natural light, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

### 場景 4 — 飯店房間（Hotel Room）

**氛圍**：首爾以外的城市——東京、上海——飯店的現代感，白床，她的高挑身材在乾淨的飯店空間裡。

**Prompt（圖片）**：
```
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black hair with wispy ends, 168cm, sitting on hotel bed with crisp white bedding, modern hotel room with large window showing city view, wearing white fitted cotton sleep top, looking toward window with thoughtful expression, hotel room ambient warm lighting, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

**Prompt（影片，cinematic_studio_video_v2）**：
```
Shot 1: Modern hotel room, she sits on white bed looking out large window, city skyline visible, elegant and composed.
Shot 2: She moves to window, stands looking out, tall slender figure against floor-to-ceiling glass.
Shot 3: Profile close-up of her face, city lights or daylight on fair skin, hair slightly falling forward.
Shot 4: She turns to camera slowly, natural expression, the kind of look she gives when she forgets anyone is watching.
Shot on iPhone, warm soft grain, warm tones, no over-sharpening, hotel and city light, stable camera, feels like a real person filmed this.
```

**參數**：同場景 1。

---

## 舞蹈影片記錄（2026-07-06）

### Start Frame

| Job ID | 說明 | Media ID |
|--------|------|----------|
| `eff381cd` | 全身站立，粉色 bodycon dress，韓國公寓背景（已批准） | `5749da05-7dd9-46f8-bce1-ffde14635e93` |

### 音樂

| 音樂 | Audio Media ID |
|------|---------------|
| Pump It Up | `eff67fee-adf6-4846-b983-21e08acd2fa9` |

### 已生成影片清單

| 版本 | 時長 | 服裝 | 背景 | Job ID | generate_audio | 狀態 |
|------|------|------|------|--------|---------------|------|
| dance_v1 | 15s | 粉色 bodycon dress | plain white studio | `7194b553` | false（未帶入） | 保留 |
| dance_v2 | 15s | 粉色 bodycon dress | aesthetic bedroom, LED lighting | `42e42771` | false ✓ | 保留 |

### 舞蹈影片 Prompt 模板（已驗證）

```
23-year-old Korean girl, beautiful face with large bright double-eyelid eyes, delicate nose, soft full lips, glowing skin, full glam makeup, petite curvy figure with full chest and slim waist, dark brown wavy hair collarbone-length, wearing [OUTFIT], THREE QUARTER BODY SHOT, mid-thigh up, no shoes shown, energetic hip-hop dance, body rolling, hip sway, powerful rhythmic movement, synced to pop beat, dynamic energy, [BACKGROUND], synced to the music beat and rhythm, dynamic dance movement, confident sensual energy, shot on iPhone, natural lighting, warm tones, single continuous shot no camera cuts, character always centered in frame, staying within frame boundaries at all times
```

### 舞蹈影片生成 Checklist（每次送出前必須確認）

- `generate_audio: false` ← 必填，否則模型自己生成音樂蓋掉 audio_reference
- `audio` role 帶入正確 media_id
- `start_image` 帶入正確 media_id
- `THREE QUARTER BODY SHOT` 在 prompt 裡
- `centered in frame, staying within frame boundaries at all times`（防黑邊）
- `single continuous shot no camera cuts`（防鏡頭切換）
- 背景無 mirror（mirror 會讓模型誤判成鏡頭切換）
- 無 NSFW 觸發詞（避免：sexy expression, sensual isolation, snaps hips hard, chest bouncing/jiggling）
