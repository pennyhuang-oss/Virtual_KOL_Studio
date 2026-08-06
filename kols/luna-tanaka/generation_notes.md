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
20-year-old Japanese girl, black center-parted chin-length bob, large round dark brown eyes, fair porcelain skin, petite curvy figure, 88cm bust (E cup) - 56cm waist - 87cm hip, full chest and slim waist, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

> 身材數字直接取自 `profile.json` → `identity.appearance.measurements`（bust_cm 88 / waist_cm 56 / hip_cm 87 / cup_size E），比之前只寫「full chest and slim waist」這種模糊形容詞更精準對齊角色設定。舊場景（場景 1–4、舞蹈影片、日常自拍影片）已生成並通過確認，維持原樣不動；此數字更新僅套用於之後的新生成批次。

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

---

## 日常自拍影片記錄（2026-07-07）

> 方向：男性受眾，手機自拍感，童顏巨乳反差，床上自拍，展示胸口，非廣告感。
> 模型：`kling3_0`（單鏡頭，臉部鎖定）
> 完整 SOP 見 `DAILY_VIDEO_SOP.md`

### Start Frame（日常服裝）

| Job ID | 說明 | 已選 | Media ID |
|--------|------|------|----------|
| `970cf52f` | 床上仰拍，白色薄棉睡衣領口微開，俯角自拍，露胸口 | ✅ 已選 | `81d7442e` |
| `7da38bb4` | 同場景，第二張備選 | — | — |

**Start Frame Prompt（已驗證）**：
```
20-year-old Japanese woman, cute youthful face, large expressive eyes,
long straight dark hair, petite figure with full bust,
lying on bed looking up at camera, wearing white thin cotton pajama top with slightly open neckline,
phone selfie angle from above looking down at her face and chest,
soft smile looking at camera, bedroom with soft warm lighting,
candid self-portrait feel, shot on iPhone front camera,
face and chest visible in frame, warm tones, film grain
```

### 日常影片

| 版本 | 場景 | 服裝 | Job ID | 模型 | 狀態 |
|------|------|------|--------|------|------|
| daily_v1 | 床上仰拍，手機俯角，童顏巨乳反差，看鏡頭微笑 | 白色薄棉睡衣，領口微開 | `c2cfc025` | kling3_0 | ✅ 批准 |

**影片 Prompt（已驗證）**：
```
20-year-old Japanese woman, cute youthful face, large expressive eyes, black hair,
petite figure with full bust,
lying on bed looking up at camera held above her,
wearing white thin cotton pajama top with slightly open neckline showing natural cleavage,
soft smile looking up at camera,
overhead phone selfie angle from above showing face and chest,
bedroom with soft warm lighting, single continuous shot, casual selfie feel, warm tones
```

**參數**：
```python
model = "kling3_0"
medias = [{"role": "start_image", "value": "81d7442e"}]
sound = "on"
aspect_ratio = "9:16"
duration = 10
```

---

## 2026-07-25 新增：身材數字 + 風格參考

- 核心 Prompt 已補上具體身材數字（見上方「核心 Prompt 基礎結構」），取自 `profile.json` measurements，之後新場景請沿用數字版本，不要退回模糊形容詞。
- 光線配方請參考 `SEXY_SCENE_LIBRARY.md` 中「3. 光源」的最新修正：室內親密場景（晨起/浴室/居家/飯店）維持原本的混合、不均勻光邏輯；Luna 的內容以京都戶外街頭、咖啡廳、庭園等生活風格攝影為主，這類場景應改用新的「討喜自然光（黃金時段/戶外強光）+ 淺景深 + 清晰高畫質」配方，不要再套用刻意做舊/調暗調糊的舊邏輯。
- 以上僅為之後新生成批次的補充指引，不影響已核准的訓練圖與既有場景記錄。

---

## 2026-08-06 R1 舞蹈影片起始畫面（動作驅動複製法 Method B，Step 4）

**觸發背景**：舞蹈批次分配（見 `DANCE_CLONE_SOP.md` 大量選片 SOP）R1 指定給 Luna Tanaka。驅動片：
`https://www.instagram.com/reel/DPWE2eqEVJ-/`（削肩上衣+高腰內搭，居家性感風，~129 BPM，單鏡頭手持無切鏡）。
場景/穿搭依人設哲學更正後的規劃（主軸風格允許她「性感的那一面」偶爾出現）重新設計：京都公寓榻榻米房間，
晨光透過舊木窗框，奶油針織開襟外套滑落一側肩膀+同色系削肩內搭+奶油高腰棉短褲。

**模型**：`soul_2` + `soul_id: 1bfab2ce-cfa5-4026-93fa-e5c91b469c7a`，`aspect_ratio: 9:16`，`quality: 2k`（預設）

**Prompt**：
```
20-year-old Japanese woman, black center-parted chin-length bob slightly tousled, large round dark
brown eyes, fair porcelain skin, petite curvy figure with full chest and slim waist (88-56-87cm, E
cup), standing in a relaxed confident pose facing camera in her small Kyoto apartment tatami room,
low wooden table and an old wooden window frame behind her, her cat Mochi's cushion softly visible
in the corner, wearing an oversized cream knit cardigan slipping off one shoulder over a matching
thin cream camisole, cream high-waisted cotton shorts, THREE QUARTER SHOT, mid-thigh up, no shoes
shown, soft diffused morning light streaming through the old wooden window frame across the tatami
mat, film grain, candid lifestyle photo, warm cream tones, shot on 35mm, Instagram style
```

**⚠️ 本輪生成了 2 張候選（`count=2`）而不是 1 張**——事後被使用者指出這樣浪費：起始畫面只有一張會真的
拿去跑 Motion Control，生兩張再選等於白花一半的生成成本。**已修正 `DANCE_CLONE_SOP.md` Step 4 的預設
`count` 為 1**，之後所有 KOL 的起始畫面生成一次只出一張，把場景/服裝/光線在 prompt 裡一次寫到位，不要
用「多生幾張再選」取代想清楚 prompt。

**兩張候選的誠實評估**（已用 Read 工具目視檢查）：
- 身分辨識度：兩張都清楚是她的黑色中分到下巴娃娃臉短髮，跟錨定身分一致
- 場景/穿搭：兩張都符合規劃——榻榻米房間、木窗框、奶油針織開襟外套+削肩內搭+高腰短褲，開襟外套提供
  跳舞用的次級動態載體
- **構圖偏差**：兩張都拍到小腿甚至接近腳，比 SOP 要求的「三分身、mid-thigh up」寬，跟驅動片的三分身
  裁切不完全對齊——留到 Step 5 Motion Control 時再視覺確認是否需要處理，暫不視為阻斷問題
- **B 張有明顯瑕疵**：邊框、打孔記號、右側直排日文字——讀起來像寫真雜誌內頁掃描，不是她一貫的 iPhone
  candid 隨拍質感，跟人設風格無關，是純粹的生成瑕疵

**使用者決定**：兩張都可接受，不需重生成。**選定 `start_frame.png`（原 candidate A）作為 Step 5 Motion
Control 的正式起始畫面**，因為沒有 B 張的雜誌掃描感；`start_frame_alt_magazine_artifact.png`（原
candidate B）保留存查，不會被拿去跑 Motion Control。

**產出檔案**：`kols/luna-tanaka/images/dance_clone_r1/start_frame.png`（正式採用）、
`start_frame_alt_magazine_artifact.png`（保留存查，不採用）

**下一步（待執行）**：Step 1–3（下載驅動片、裁剪、Performance Sheet + Emotion Timeline）尚未執行；
Step 5 Motion Control 待這些完成後才能跑。
