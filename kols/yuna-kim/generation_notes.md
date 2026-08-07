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
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black hair with wispy ends, 168cm, bust 84cm/waist 58cm/hip 89cm, C cup, slender tall figure with defined waist-hip ratio, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

> 身材數字取自 `profile.json` → `identity.appearance.measurements`（height_cm 168 / bust_cm 84 / waist_cm 58 / hip_cm 89 / cup_size C）。直接寫進 prompt 的具體數字，取代單純「tall and slender」這類模糊形容詞。

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

---

## 日常自拍影片記錄（2026-07-07）

> 方向：男性受眾，手機自拍感，展示身材曲線和身材比例，非廣告感。
> 模型：`kling3_0`（單鏡頭，臉部鎖定）
> 完整 SOP 見 `DAILY_VIDEO_SOP.md`

### Start Frame（日常服裝）

| Job ID | 說明 | 已選 | Media ID |
|--------|------|------|----------|
| `fd8b7c1d` | 飯店房間，白色緊身 crop top + 低腰牛仔短褲，鏡子自拍站立 | ✅ 已選 | `9e7d8009` |
| `1f4935eb` | 同場景，第二張備選 | — | — |

**Start Frame Prompt（已驗證）**：
```
22-year-old Korean woman, beautiful face, sharp elegant features,
long straight black hair, slim figure with curves,
standing near hotel room door, wearing white fitted crop top and low-rise denim shorts,
holding phone selfie from front, turning from side to face camera,
showing waist and chest ratio, warm hotel room lighting,
candid self-portrait feel, shot on iPhone front camera,
half body shot from waist up, warm tones, film grain
```

### 日常影片

| 版本 | 場景 | 服裝 | Job ID | 模型 | 狀態 |
|------|------|------|--------|------|------|
| daily_v1 | 飯店房間，從側面轉正面展示身材比例，看鏡頭 | 白色 crop top + 低腰牛仔短褲 | `2aca7a9e` | kling3_0 | ✅ 批准 |

**影片 Prompt（已驗證）**：
```
22-year-old Korean woman, beautiful face, long straight black hair, slim figure with curves,
standing in hotel room, wearing white fitted crop top and low-rise denim shorts,
slowly turning from side profile to face camera directly,
side profile shows slim waist and chest ratio, then turns to face camera with natural confident gaze,
warm hotel room lighting, single continuous shot, phone selfie mirror casual feel, warm tones
```

**參數**：
```python
model = "kling3_0"
medias = [{"role": "start_image", "value": "9e7d8009"}]
sound = "on"
aspect_ratio = "9:16"
duration = 10
```

---

## 2026-07-25 新增：身材數字 + 風格參考

- 核心 prompt 基礎結構已補上具體身材數字（bust 84cm / waist 58cm / hip 89cm / C cup，來自 `profile.json`），取代模糊形容詞，未來生成請沿用上方更新後的模板。
- 光線邏輯請參考 `SEXY_SCENE_LIBRARY.md` 「2026-07-25 修正」一節（光源）：Yuna 的內容混合首爾室內美妝保養場景與戶外咖啡廳/街拍場景，兩者光線配方不同——
  - **室內場景**（浴室鏡前、居家慵懶、臥室早晨等）維持原本的「混合、不均勻暖光」配方不變。
  - **戶外/生活風格場景**（江南咖啡廳、弘大街頭等）改用新的「討喜自然光（黃金時段/明亮日光）+ 淺景深 + 清晰高畫質」配方，不要刻意調暗調糊。
- 此為未來批次的生成指引，不影響已批准的 soul_test_v1 圖片與現有 soul_id 訓練紀錄。

---

## 2026-08-07 R7 舞蹈克隆完整跑完 Step 1–8（動作驅動複製法 Method B）

**背景**：舞蹈批次分配（見 `DANCE_CLONE_SOP.md`、GitHub Issue #3）R7 分配給 Yuna Kim。驅動片：`https://www.instagram.com/reel/DEq7fsPPBr8/`（白色 crop top + 牛仔短褲手勢舞，室內走廊場景）。Step 1–4（下載裁剪、Performance/Emotion 分析、起始畫面單張生成）已於同日較早完成，`start_frame.png` 已核准。

### Step 5：Motion Control（兩種 `scene_control` 對照）

- `image_id`: `4c687699-5dd8-401c-a255-3a874f372e43`，`motion_video_id`: `fa827729-b003-4a43-b689-6e14c6fe24ce`
- **`scene_control: "image"`**（原版）：job `4945b0ad-3830-4bc0-9c37-a54b4bb0e57a`，680×1280 輸入、輸出 1072×1936、30fps、~13.7s，✅ 一次成功，花費 37 credit
- **`scene_control: "video"`**（背景動態實驗）：job `97e108b0` 狀態 `failed`（無錯誤訊息），對照重跑 job `725afb05` 同樣 `failed`。**兩次均全額退款，零淨成本**。跟 Iris Chen R6 的測試結果一致（該輪甚至出現明確 `nsfw` 標記），確認 `scene_control: "video"` 在目前這批性感貼身穿搭風格下有結構性的內容審核相容性問題，**已放棄這條路線**，詳細分析見 `kols/iris-chen/generation_notes.md` 同日章節。

### 背景動態問題與後製解決方案

跟 R6 採用同一套零額外 credit 的本機後製方案：對 `scene_control: "image"` 的最終輸出做全幀緩慢漂移平移（`ffmpeg` `crop` 濾鏡，`18*sin(2*PI*t/11)` / `10*cos(2*PI*t/16)` 正弦位移模擬手持呼吸感），角色動作/表情不做任何更動。使用者比對 R6 的原版/後製版後認為差異不大但同意採用，本輪直接沿用同一處理套用到 R7，不再重複產出對照版。

### Step 6：手動混音

`scene_control: "image"` 原始輸出無聲，用 `ffmpeg -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest` 把 Step 2 抽出的 `driver_audio.m4a` 蓋上後製漂移處理後的無聲畫面，輸出 `yuna_dance_clone_r7_ig_reel.mp4`（1072×1936、30fps、~13.7s，含視訊+音訊雙軌）。

### Step 7：授權與發佈限制檢查

- **驅動動作**：來自第三方 Instagram 創作者，僅供內部方法驗證；對外發佈前需評估重現程度
- **配樂**：驅動片原始配樂，**未取得商用授權**，正式發佈前必須替換
- **背景**：最終採用 `scene_control: "image"`（+後製漂移），未借用驅動片真實場景，不涉及第三方場景識別性問題
- **素材存放**：驅動片原始檔僅存本機工作資料夾，未存入本 repo

### Step 8：QA 檢核（第一版）

已用 Read 工具目視抽幀比對後製版（約 0.7s／6.7s／12.7s）：身分一致、白色 crop top + 牛仔短褲穿搭清楚可辨、手部無明顯崩壞、後製漂移未裁到角色肢體或造成明顯抖動。背景動態評定同 R6，為打破靜止感的攝影機微動，非真實環境動態，記錄在案。**此輪抽樣間距過大（間隔約 6 秒），漏掉了中間時段的構圖問題，見下方重跑記錄。**

### ⚠️ 重跑：構圖偏移問題

使用者複核第一版成品後發現**角色在影片中段（約 6 秒附近）整個人偏移到畫面左側、身體被裁掉一半**，回報要求重做。用密集抽幀（每秒一幀，覆蓋全部 13.7 秒）比對後確認：這個裁切問題**存在於後製處理之前的原始 Kling 輸出本身**（比對 `kling_output_image_mode.mp4` 同一時間點，同樣被裁到左邊），確認不是本機後製漂移濾鏡造成的，是 Motion Control 生成本身的構圖問題——驅動片本身的運鏡/角色位移，在 `scene_control: "image"` 模式下沒有被適當地重新置中。

**處理方式**：用同一組 `image_id`／`motion_video_id`／`scene_control: "image"` 重新呼叫一次 `motion_control`（新 job `6ce5d1a9-4b66-4104-bcb0-84a7d70ef8df`，生成本身有隨機性，重跑有機會避開原本的構圖問題）。重跑版本用每秒一幀密集抽樣重新檢查全部 13.7 秒：角色多數時間偏向畫面左側/中左，但**沒有再出現整個人被裁到畫面外的情況**，偶爾手部動作伸到左邊緣（4s、6s、11s 附近）在真實手持拍攝中也是正常現象，判定為合格。

### Step 8：QA 檢核（重跑版，最終採用）

每秒一幀密集抽樣覆蓋全部 13.7 秒：身分一致、白色 crop top + 牛仔短褲穿搭清楚可辨、手部無明顯崩壞、無角色整體被裁出畫面的問題。套用同一套後製漂移運鏡＋混音後即為最終版本。背景動態評定同 R6，為打破靜止感的攝影機微動，非真實環境動態，記錄在案，使用者已審閱並核准接受。

### ⚠️ 構圖偏左問題：嘗試後製置中，確認不可行

使用者複核重跑版後仍認為角色整體偏向畫面左側，構圖不夠居中，要求嘗試後製解決。用每秒一幀密集量測全片 14 個時間點後確認：**她的軀幹全程穩定貼在畫面左側約 15–25% 寬度處，但手臂動作會用到幾乎整個畫面範圍**——舉手過頭時指尖幾乎頂到畫面最上緣（約第 5 秒），伸展手臂時最遠到畫面約 70% 寬度處（約第 3、9 秒），腳在多個時間點也幾乎踩到畫面最下緣。這代表任何等比例縮放置中的裁切都會裁到某個時刻的動作（上緣裁到舉高的手、下緣裁到腳），不裁切、只單方向拉寬畫面則會讓身形比例橫向失真。**結論：這支素材沒有安全邊界可供後製重新置中，技術上不可行，已放棄嘗試**，不引入變形或新的裁切風險。

**使用者決定**：不追加任何處理，保留現有版本（重跑版 + 後製漂移運鏡）。此非正式旗艦版本，構圖偏左的落差記錄在案，接受現狀。

### 產出檔案

- `kols/yuna-kim/images/dance_clone_r7/start_frame.png`（已核准起始畫面）
- `kols/yuna-kim/videos/dance_clone_r7/yuna_dance_clone_r7_ig_reel.mp4`（1072×1936、30fps、~13.7s，重跑版 job `6ce5d1a9`，`scene_control: image` + 本機後製漂移運鏡，含驅動片原始配樂音軌，未經授權，僅供內部驗證）
