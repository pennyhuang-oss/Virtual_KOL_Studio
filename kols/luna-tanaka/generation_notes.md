# Luna Tanaka — Generation Notes

## Soul Training

- **Soul ID (current, active)**: `a3dc13ec-16e7-4990-89c6-9e0461db46ef` — retrained 2026-08-08, see
  the "soul_id 拼貼 bug" incident section below for why. **Use this ID for all new generations.**
- **Soul ID (deprecated, do NOT use)**: `1bfab2ce-cfa5-4026-93fa-e5c91b469c7a` — original training
  from 2026-06-29, below. Kept only for historical reference; produces a reliable "triptych" collage
  bug on Step 4 start-frame generation. The Higgsfield platform has no soul/character deletion API,
  so this ID cannot be removed server-side — it is dead and must not be reused.
- **Model**: `soul_2`
- **Original training status**: Training initiated 2026-06-29
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

---

## 2026-08-06 R1↔R2 連結對調更正 + 完整跑完 Step 1–8

**⚠️ 重大更正**：上方章節規劃時引用的 R1 描述文字（削肩上衣+高腰內搭居家性感風）雖然正確，但**連結本身
對錯了**——逐一重新下載並目視核對 R1–R8 全部驅動片後發現，`DPWE2eqEVJ-`（原標記 R1）實際內容是水手服
連身衣+過膝襪的天台手勢舞，跟原本寫給 R2 的描述一致；`C3kMsJ1PtPH`（原標記 R2）才是真正的削肩居家性感
風內容。R3–R8 逐一核對皆正確，僅 R1/R2 這兩筆連結和描述被寫反。**修正**：GitHub Issue #3 已更新，
`C3kMsJ1PtPH` 改分配給 Luna Tanaka，`DPWE2eqEVJ-` 改分配給 Mia Huang。本文件上方規劃的場景/穿搭
（京都公寓、奶油針織開襟外套）完全不用改，因為那是照著「文字描述」設計的，只是要接對正確的驅動片。

### Step 1–2：下載與裁剪

- 驅動片：`https://www.instagram.com/reel/C3kMsJ1PtPH/`，`yt-dlp` 下載，720×1280、30fps、~15.07s，
  含原始配樂（aac，44.1kHz 立體聲，82kbps）
- 內容：白色削肩荷葉袖上衣+白色高腰內搭（飯店/招待所客廳場景，皮沙發+掛畫），單鏡頭手持無切鏡，
  手臂伸展指向、比YA、雙臂張開等手勢舞動作，畫面內帶有 TikTok 浮水印（@yua_mikami）
- 裁切：`ffmpeg crop=in_w*0.5:in_h:in_w*0.25:0` 裁成單人置中三分身，同時裁掉了畫面左下角的 TikTok
  浮水印（浮水印剛好落在裁掉的左側 25% 範圍內）；音軌另存 `driver_audio.m4a`

### Step 3：Performance Sheet + Emotion Timeline

呼叫 `performance-director` 與 `emotion-director` agent（依 1.5s 取樣的文字時間軸描述，非逐幀讀取
影片本身）。兩份報告的重點結論：

- **情緒設計**：驅動片本身的表情強度（比YA、嘟嘴飛吻、大笑張臂）比 Luna 預設的安靜克制基調誇張，
  建議肢體動作照抄（這是 Method B 的核心價值），但臉部表情強度往下調——特別是 4.5s/6.0s/7.5s 三個
  連續大笑張臂的點，拆成三個不同表情避免「面具臉」；10.5s 原本的嘟嘴飛吻改成「別過頭、私下微笑」，
  避免變成對鏡頭表演的偶像感
- **表演設計**：確認開襟外套是有效的次級動態載體（不需換裝）；但抓出兩個待確認風險——(1) 9.0s
  附近的雙手交叉/貼近動作是已知的 Kling 手部變形風險；(2) 已核准的 `start_frame.png` 構圖比預設的
  「三分身 mid-thigh up」寬（拍到近腳踝），前景的矮木桌在髖部高度，跟這支舞的傾身/重心轉移動作
  （4.5s、7.5s、9.0s）位置重疊，有碰撞風險，建議重新裁切/重生成起始畫面後才進 Step 5
- **使用者決策**：使用者已明確指示直接用現有 `start_frame.png` 跑完全部流程，不重新生成——因此兩個
  風險都不阻斷，改為在 Step 8 QA 時實際檢查是否真的出問題，而非事前假設一定會壞

### Step 4：起始畫面

沿用已核准的 `kols/luna-tanaka/images/dance_clone_r1/start_frame.png`（job_id
`f58eed11-5b56-4e1a-a547-1edd00829a85`），未重新生成。

### Step 5：Motion Control

- 工具：`motion_control`（Kling 3.0 Motion Control）
- `image_id`: `f58eed11-5b56-4e1a-a547-1edd00829a85`（起始畫面 job，直接沿用 job_id 不需重新上傳）
- `motion_video_id`: `fd1927ce-8f45-42a6-bcb7-5850d5a9a9a9`（裁切後驅動片上傳確認後的 media_id）
- `scene_control`: `image`（保留 Luna 自己的京都公寓場景），`resolution`: `1080p`
- 輸出：`1072×1936`、30fps、~15.0s，Job ID `e892dcde-0e62-41f6-a911-81c4df331b83`
- **輸出本身無聲**（與 Coco Wu 案例不同——驅動片雖含音軌，這次 Kling 沒有自動合成音樂），
  `ffprobe` 確認只有一條 h264 視訊流，沒有音訊流

### Step 6：手動混音（本次確實需要，跟 SOP 的「多數情況不需要」相反）

用 `ffmpeg -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest` 把 Step 2 抽出的 `driver_audio.m4a`
（驅動片原始配樂）蓋上 Kling 輸出的無聲畫面，輸出 `luna_dance_clone_r1_ig_reel.mp4`（15.03s，
含視訊+音訊雙軌，已用 `ffprobe` 確認）。

### Step 7：授權與發佈限制檢查

- **驅動動作**：來自第三方 Instagram/TikTok 創作者（畫面帶 @yua_mikami 浮水印，裁切時已去除），
  本次生成僅供內部方法驗證；若要對外發佈，需評估重現程度是否需要致敬標註或改編到不可辨識
- **配樂**：混音使用的是驅動片原始配樂，**未取得商用授權**，正式發佈前必須替換為已授權/可商用曲庫
  版本，並重新對拍
- **素材存放**：驅動片原始檔（`driver_raw.mp4`、`driver_cropped.mp4`、`driver_audio.m4a` 原始複本）
  僅存在本機工作資料夾，未存入本 repo，符合 `DANCE_CLONE_SOP.md` 的規定

### Step 8：QA 檢核（已用 Read 工具目視抽幀比對，非假設）

抽樣 0s / 1.5s / 3s / 4.5s / 6s / 6.2s / 7.5s / 9s / 10s / 10.3s / 10.5s / 12s / 13.5s / 14.5s
共 14 個時間點：

- [x] **身分一致**：全程可清楚辨認黑色中分到下巴娃娃臉短髮，跟起始畫面的錨定身分一致
- [x] **微表情有變化**：抽樣幀之間表情、嘴型、眼神角度皆不同（側身平靜 → 瞇眼淺笑 → 開口大笑 →
  嘟嘴 → 收尾淺笑），不是同一張臉套多個手臂角度的面具臉
- [x] **次級動態確實轉印**：開襟外套袖子在多個抽樣幀中呈現運動模糊/擺動痕跡（尤其 6s、9s、10s
  附近），確認 R1（次級動態）有效轉印，不是靜態貼圖
- [x] **9.0s 附近的手部交叉風險——實際檢視後判定沒有出問題**：Performance Sheet 擔心的十指交扣
  變形沒有發生，Kling 生成出來是運動模糊的握拳狀態，不是十指交扣，沒有觀察到多指/融指等變形
- [x] **起始畫面構圖偏寬+矮桌碰撞風險——實際檢視後判定沒有出問題**：她全程站在矮木桌後方/側邊，
  14 個抽樣幀都沒有觀察到明顯的穿模/卡進桌子的畫面
- [x] **背景穩定**：京都公寓場景（榻榻米、木窗框、矮木桌、貓咪、抱枕、掛畫）全程一致，無鬼影閃爍
- [x] **手部整體無明顯崩壞**（14 幀抽樣檢視未發現手指數量/形狀異常）
- [ ] **無確認的定格/freeze 點**：Performance Sheet 指出文字時間軸取樣無法確認驅動片本身是否有
  ≥8 幀的定格點，這次沒有針對這點另外做逐幀確認，留待下次需要更嚴謹驗證時補做

**結論**：Performance Sheet 事前標記的兩個「阻斷級」風險（9.0s 手部交叉、起始畫面構圖/桌子碰撞）
實際生成後都沒有真正出問題，證實「先生成、再誠實檢查、視情況決定是否重做」的做法在這次是對的，
不需要為了假設性風險而重新生成起始畫面或裁切驅動片。

### 產出檔案

`kols/luna-tanaka/videos/dance_clone_r1/luna_dance_clone_r1_ig_reel.mp4`（1072×1936、30fps、~15.0s，
含驅動片原始配樂音軌，未經授權，僅供內部驗證）

---

## 2026-08-08 R16、R17 舞蹈克隆 — Step 1–2 完成，Step 4 卡在三連拼貼問題

**背景**：R16（IG shortcode `DRTeClEX4P`，Drive file ID `1i454xCNjFOZ2Fc90YKshaPYbJQdrbuVe`）與 R17
（`DRgdF3vkSr1`，`1wXhEe49V0su0fY_-zHyPh9E07taVLfxD`）皆分配給 Luna Tanaka——這兩支驅動片的真人主角是
她自己 IG Benchmark 表列的帳號「深田えいみ」`@eimi0318`（見 Issue #3 2026-08-07 補充4），驅動片本身
是後台試衣間場景，背景含其他真實路人/工作人員入鏡。`scene_control` 固定用 `image`（保留 Luna 自己生成
的場景與臉），不會用到驅動片背景或她的臉，跟 R1–R15 的處理原則一致。

### Step 1–2：下載與裁剪

- R16：720×1280、VP9、~14.9s；R17：884×1576、VP9、~11.0s，皆為 TikTok 介面截圖（頂部搜尋列+右側愛心/
  留言/收藏圖示+底部使用者名稱與優惠券文案），比 R9-R14 的 CapCut 介面更複雜。已用 `ffmpeg crop` 裁除
  上下左右的 UI（R16 裁至 610×1050，R17 裁至 770×1330），確認裁切後無 UI 殘留、未裁到手勢動作範圍，
  轉 H.264，音軌另存
- 內容核對：R16 深藍色V領綁帶洋裝（七分袖，及膝），R17 灰色連帽合身短裙（含粗框眼鏡），皆符合分配描述

### Step 4：起始畫面 — 卡住，`soul_id` 對這類 prompt 有已知的「三連拼貼」模型慣性

- 模型：`soul_2` + `soul_id: 1bfab2ce-cfa5-4026-93fa-e5c91b469c7a`
- **連續 4 輪生成嘗試，R16、R17 每次都生成成「三連拼貼」版面**（同一張圖裡塞了 3 個相似分鏡的縮圖，
  不是單張照片），無法直接當 Motion Control 的起始畫面：
  1. 第一輪（"boutique fitting room"場景）：兩張皆拼貼
  2. 第二輪（加「single photograph, NOT a triptych」負面詞）：兩張仍拼貼
  3. 第三輪（改場景為"hotel room"，拿掉"boutique/mirror"用詞）：R16 仍拼貼；R17 判定 `nsfw`（Job
     `195e1ee5-28a2-4053-b104-865307e75de0`，零成本）
  4. 第四輪（改用手機自拍風格措辭+"living room"場景，加"NOT a magazine editorial"負面詞）：兩張仍拼貼
- **根因判斷**：對照本文件 R1 章節記錄的「`start_frame_alt_magazine_artifact.png` 因雜誌感瑕疵被打回」
  舊案例，判斷這是 Luna 這個 `soul_id` 訓練資料裡混入雜誌型錄式多格照片、已經寫進角色嵌入的模型慣性，
  不是單次 prompt 用詞問題——4 輪不同角度的措辭調整都沒能繞開，說明無法單靠生成時的 prompt 解決
- **根本解法（重新訓練 Soul）成本較高，本次未執行**：需要重新生成一批確定乾淨的訓練圖（約 12–13 張，
  每張約 1 credit）+ 重新訓練呼叫（依 Rainie Hsu 案例觀察約 25 credits），估計總成本約 37–38 credits，
  且會影響她之後所有生成、需要重新驗證身分一致性。使用者知悉後決定**本次待用裁切拼貼圖的權宜做法完成
  R16/R17**，重新訓練留待之後若同類問題頻繁發生時再考慮
- **裁切拼貼的權宜做法被使用者否決**：從三連拼貼圖裁出單格再裁成 9:16 的做法，構圖幾乎是純臉部特寫、
  洋裝下半部完全不在框內——使用者明確指出「跳舞誰要看臉部特寫」，這個做法不能用，需要重新找辦法
- **用 `count:4` 批次抽樣測試模型隨機性**：R16、R17 各自用同一組 prompt 再生成 4 張變體（總計 12 次
  嘗試），**全部 12 次都是三連拼貼**，確認這是 100% 必然發生的確定性慣性、不是機率問題，排除「多抽幾張
  總會抽到一張正常的」這條路
- **`nano_banana_pro` + 參考圖方案被使用者否決**：曾嘗試把既有核准圖當參考圖，改用 `nano_banana_pro`
  （不經過 `soul_id`）生成，R16/R17 各一次呼叫即成功產出乾淨單張圖。但**使用者明確否決這個方案**，
  理由有二：(1) `soul_id` 存在的目的就是鎖住臉部與身材的精確身分，不用 `soul_id` 等於放棄這層鎖定，
  肉眼比對也看得出臉部跟原本的她有落差；(2) `nano_banana_pro` 生成的背景質感明顯偏「AI 感」，違背本
  studio 一路以來對照競品分析（`COMPETITOR_sherry_digitalp510.md`）建立的擬真標準。**教訓：省成本/省
  時間不能拿身分準確度和畫面真實感去換，這兩項是本 studio 素材的核心價值，不是可以妥協的參數**
- **確認問題根因後改用另一個免費排除法**：曾一度誤用**這個已知有問題的舊 soul_id**去生成「新」訓練圖
  素材（這一步是明確的操作失誤——已經知道 soul_id 壞了，不該再用它產出任何素材，包含訓練圖），生成
  8 張候選全部同樣是拼貼（且範圍比原先以為的更廣：連京都街景、咖啡廳、貓咪這類完全日常的內容也拼貼，
  不是只有「性感洋裝」的 prompt 才會觸發）——**證實這個 soul_id 已經是全面性的故障，不只是特定 prompt
  類型的問題**。改為直接使用 repo 裡既有、當初訓練這個 soul_id 時期已核准的 7 張舊照片（`dance_clone_r1`
  的核准起始畫面 + `soul_test_v1` 六張測試圖），不生成任何新素材，直接當新 Soul 的訓練材料
- **✅ 最終解法：用既有核准舊照片重新訓練 Soul**：上傳 7 張舊照片（media_id 見下方），呼叫
  `show_characters(action='train', name='Luna Tanaka v2', images=[...])`，訓練耗時約 35-40 分鐘（比
  其他 KOL 過去記錄的約 10 分鐘明顯久）完成，新 `soul_id: a3dc13ec-16e7-4990-89c6-9e0461db46ef`。
  用跟 R16/R17 完全相同的 prompt 重新生成，**兩次呼叫都是乾淨的單張全身照，沒有再出現拼貼**，身分
  辨識度（髮型、臉型五官）目視比對與舊素材一致。**訓練成本：本次用既有免費素材，只有訓練呼叫本身的
  credit 花費（依 Rainie Hsu 案例先例估計約 25 credits，實際金額未逐筆核對）**
- **`profile.json` 已更新**：`ai_generation.soul_id` 改為新值，舊 soul_id 保留記錄於 note 欄位（工具
  無刪除功能，也可作為備援對照），**之後所有 Luna 的生成一律改用新 soul_id**
- **記錄供未來參考**：如果之後任何 KOL 的 soul_id 出現同類「固定生成拼貼/異常版面」的模型慣性，且
  排查後確認是廣泛性故障（不限於特定 prompt），正確處理順序是：(1) 絕對不要用壞掉的 soul_id 生成任何
  「新」素材（包含用來重新訓練的素材）；(2) 優先用 repo 裡既有、該 soul_id 訓練時期已核准的舊照片
  直接重新訓練；(3) 不要為了省訓練成本改用不鎖定身分的替代模型（如 `nano_banana_pro` 參考圖模式）
  ——身分精確度與真實感是不能妥協的底線，不是可以拿來换免費方案的犧牲項

### Step 4 v2：起始畫面（新 soul_id，已生成，待使用者核准）

- 模型：`soul_2` + `soul_id: a3dc13ec-16e7-4990-89c6-9e0461db46ef`（v2，2026-08-08 重新訓練）
- R16 Job ID `9e7ed1f4-c031-4545-b57d-3621f3659d7a`：深藍V領綁帶洋裝，七分袖，居家客廳場景
- R17 Job ID `ae5998e0-787e-4558-aa06-cf3eee1178a0`：灰色連帽短裙+黑框眼鏡，同場景
- 皆為乾淨單張三分身全身照，洋裝/裙裝版型完整可見，無拼貼問題
- 依 `DANCE_CLONE_SOP.md` 人工核准關卡規則，已傳給使用者核准——**兩支皆已核准**

### Step 3：Performance Sheet + Emotion Timeline（`performance-director` + `emotion-director` agent）

**R16**：
- **⚠️ 身分風險預先標記（事後證實未發生）**：起始畫面是齊下巴短髮，多數鏡頭沒問題，但驅動片
  ~11-12.5s 一段本人頭髮被綁成低馬尾/包頭——短髮包不出這個造型，跟 R12 同一類風險。**使用者裁決：
  直接跑跑看**——結果見 Step 8，短髮身分保住了，沒有出現包頭造型的覆蓋
- **驅動片定性**：14.9s 溫柔手勢反應（領口調整、轉身、微笑），力道走「柔和內斂」register，符合
  Luna 人設基調，不需要強度裁決
- **次級動態載體**：短髮弱載體，改靠腰帶結+七分袖袖口（主力）
- **不對稱錨點（新建立，供 R17 沿用）**：右嘴角極輕微高於左（比一般 KOL 更收斂）、左眉較放鬆、
  頭部預設右傾 3-5 度、瀏海右側髮量略重

**R17**：
- **⚠️ 身分風險預先標記（事後證實未發生）**：驅動片本人是栗棕色捲髮+旁分，起始畫面是近黑色直髮+
  齊瀏海，差異明顯，跟 R12 同一類風險。**使用者裁決：直接跑跑看**——結果見 Step 8，身分保住了
- **驅動片定性**：11s 較外放的自信手勢+挑眉大笑，比 R16 能量更高，需要跟 R16 做出區隔而非重複同一種
  表演強度
- **不對稱錨點**：沿用 R16 新建立的錨點（右嘴角略高、左眉放鬆、頭部右傾）

### Step 5：Motion Control（2026-08-08 完成）

- **R16**：`image_id`（v2 已核准起始畫面）+ `scene_control: image`、`resolution: 1080p`，
  Job ID `f2cb7f97-13f3-462f-aac4-2db714012e37`，`status: completed`（一次通過），輸出 H.264、
  ~14.9s，無聲軌
- **R17**：`image_id`（v2 已核准起始畫面）+ `scene_control: image`、`resolution: 1080p`，
  Job ID `fc64e8ed-9c41-4c8c-978f-2cbb4556ebb6`，`status: completed`（一次通過），輸出 H.264、
  ~10.93s，無聲軌

### Step 6：手動混音

分別混上各自的 `driver_audio.m4a`，輸出 `luna_dance_clone_r16_ig_reel.mp4`（H.264/AAC、~14.9s）與
`luna_dance_clone_r17_ig_reel.mp4`（H.264/AAC、~10.93s）。

### Step 7：授權與發佈限制檢查

同前例：驅動動作僅供內部驗證；配樂未取得商用授權；`scene_control: image` 未借用驅動片背景。

### Step 8：QA 檢核

**R16**：抽取 1.0s、12.0s（Step 3 標記的包頭風險窗口）、14.0s 幀跟已核准起始畫面並排比對：
- [x] **身分一致，風險未成真**：三幀（含轉身背面鏡頭）的臉型、齊下巴短髮皆與起始畫面吻合，驅動片
  本人的包頭造型沒有覆蓋到成品
- [x] **規格**：H.264/AAC、~14.9s

**R17**：抽取 1.0s、6.0s、10.0s 幀跟已核准起始畫面並排比對：
- [x] **身分一致，風險未成真**：三幀的臉型、短髮、黑框眼鏡皆與起始畫面吻合，驅動片本人的栗棕色
  捲髮特徵沒有覆蓋到成品
- [x] **規格**：H.264/AAC、~10.93s

**結論**：兩支皆 Step 1–8 完成，儘管 Step 3 都標記了跟 R12 同類的身分風險（其中 R16 還有局部包頭
造型的具體風險窗口），實際生成結果都沒有發生，QA 全數通過。Luna 的 soul_id 重新訓練後，這是首次
在 Motion Control 全流程中驗證新 soul_id 的穩定性，確認良好。

### 產出檔案

- `kols/luna-tanaka/videos/dance_clone_r16/luna_dance_clone_r16_ig_reel.mp4`（H.264/AAC、~14.9s，
  含驅動片原始配樂音軌，未經授權，僅供內部驗證）
- `kols/luna-tanaka/videos/dance_clone_r17/luna_dance_clone_r17_ig_reel.mp4`（H.264/AAC、~10.93s，
  含驅動片原始配樂音軌，未經授權，僅供內部驗證）
