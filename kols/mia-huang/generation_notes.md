# Mia Huang — AI 生成規劃

> **狀態：PENDING — 尚未執行任何實際生成**。本文件只是訓練圖與後續生成的規劃草案，尚未上傳任何圖片、尚未建立 Soul 模型、尚未產出任何成品。所有「批次」都是計畫中的拍攝方向，不是已完成的記錄。實際執行後應比照 `kols/iris-chen/generation_notes.md` 的格式，把每個批次替換成真實的 job ID、實際生成張數與篩選結果。

---

## 人物設定

| 欄位 | 設定 |
|------|------|
| 名字 | Mia Huang（黃米亞） |
| 年齡 | 22 歲 |
| 國籍 | 台灣（新竹） |
| 臉型 | 圓潤柔和的娃娃臉，年輕、親近感強，沒有銳利的雜誌感角度。純粹外型描述，不參考任何真實藝人或公眾人物 |
| 妝容 | 微動漫風格眼妝：柔和眼線微上揚、水潤唇彩、圓潤腮紅位置 |
| 髮型 | 灰棕色染髮，長髮微捲，臉側一撮粉色挑染（她最好認的視覺記號，每批次都必須維持一致） |
| 眼睛 | 大而有神，眼周妝感偏濃，是反應臉哏圖的表情主力 |
| 眼鏡 | 深夜直播偶爾配戴透明藍光眼鏡，其餘時候不戴 |
| 身材 | 身高 160cm，嬌小、曲線柔和，能撐起寬鬆帽T也能撐起削肩背心 |
| 穿衣風格 | 電競品牌寬鬆帽T + 短褲、削肩背心配耳機、cosplay-lite（大腿襪、貓耳頭飾）、深夜居家睡衣風格戰袍 |
| AI 生成狀態 | **尚未建立 Soul 模型。尚未生成任何訓練圖或成品。以下 soul_id、image_media_id、job_id 一律留白，實際執行後才填入真實值。** |

---

## 核心 Prompt 結構

> 沿用 Iris Chen 的驗證結論：亞洲臉孔生成建議優先測試 Seedream 4.5（`seedream_v4_5`），Recraft 系列對亞洲臉孔容易生成路人臉。Mia 尚未實測，此為根據既有經驗的建議起點，非已驗證結果。

> **降低「AI 感」要求（2026-07-24 起適用）**：以下所有批次 prompt 均已依照 `SEXY_SCENE_LIBRARY.md` 的「降低『AI 感』的技術要點」五項檢查清單重寫——皮膚質感關鍵字、逐場景明確指定的拍攝裝置/鏡頭破綻、混合不均勻的光源配方、具體的生活雜物背景、完整明確的服裝描述。之後新增批次也必須比照同一份清單逐項檢查再定稿。

**基礎 prompt 模板**（所有批次共用，只替換 `[SCENE]` / `[OUTFIT]` / `[POSE/ANGLE]` / `[LIGHTING]` / `[DEVICE]` / `[CLUTTER]`）：

```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, visible skin pores, subtle natural skin texture, unretouched skin detail, natural skin imperfections, petite figure with soft curves, ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING — mixed RGB gaming light + monitor glow + warm lamp, uneven falloff], [CLUTTER — specific lived-in streaming-room detail], [DEVICE — specific camera/webcam spec with autofocus softness / highlight clipping / motion blur / compression artifacts], film grain, candid lifestyle photo, streaming-room aesthetic
```

**一致性重點**：
- 臉型、眼妝風格、粉色挑染的位置與髮色必須每批次保持一致
- 場景與服裝細節可以自由變化（這是她的內容多樣性來源）
- 光線幾乎不用純自然光——RGB 燈光與螢幕藍光是她的招牌，即使是「下午甦醒」場景也應帶一點桌燈或待機螢幕的冷光，而非單純溫暖晨光，且光源必須是「混合、不均勻」（RGB + 螢幕光 + 暖色桌燈互相疊加），不可寫成乾淨棚拍三點打光
- 皮膚質感必須主動寫入 `visible skin pores` / `subtle natural skin texture` / `unretouched skin detail` 等關鍵字，避免 `smooth`、`flawless`、`airbrushed`、`porcelain skin` 這類會推向塑膠感的字
- 拍攝裝置與鏡頭要逐場景明確指定（前鏡頭自拍 / 後鏡頭 / 直播用 webcam 各自的破綻與色偏），不要只寫「shot on iPhone」交給模型自己猜
- 背景雜物必須具體到她的電競/直播間場景（RGB 燈條纜線、能量飲料罐、耳機架、charging cable、零食包裝、貓玩具等），不要只寫地點名稱

---

## 計畫批次 Prompt 規劃（尚未執行）

> 以下六個批次為建議拍攝方向，涵蓋她最核心的視覺場景與尚未涵蓋的內容支柱（浴室保養、飯店旅遊）。每批次建議先生成 2 張測試臉部與場景一致性，確認可用後再決定是否擴充張數。**目前皆未執行、無 job ID、無實際生成圖。**

### 批次 1（計畫）— 電競椅設定照（建立基礎一致性）

**場景說明**：她的直播間主場景——坐在電競椅上，RGB 燈條在背景，桌上有耳機和飲料，這是後續大部分素材的核心背景設定，優先用來確認臉部與場景風格的一致性。

**草稿 Prompt**（已依降低 AI 感檢查清單重寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, visible skin pores, subtle natural skin texture with slight oil sheen on the T-zone, unretouched skin detail, natural skin imperfections, petite figure with soft curves, ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, sitting in gaming chair in home streaming room, wearing an oversized black gaming-brand hoodie (fully zipped) with a screen-printed logo patch on the chest and matching black shorts underneath, hood down, relaxed 3/4 angle looking toward camera, RGB LED light strips cycling purple-to-pink glowing on the wall behind her mixed with cool blue monitor glow on her face and a warm desk lamp glow bleeding in from the corner of the frame, uneven light falloff with soft visible shadow edges where the RGB and lamp light overlap, gaming desk cluttered with a tangled RGB cable, a half-empty energy drink can, a phone lying face-down next to the keyboard, a headset stand, and a small cat plush toy on the shelf behind her, shot on iPhone 14 back camera, slight autofocus softness on the RGB light strips in the background, natural highlight clipping on the monitor's bright edge, subtle motion blur on her hand near the headset, faint JPEG compression artifacts visible in the shadow areas, film grain, candid lifestyle photo, streaming-room aesthetic
```

---

### 批次 2（計畫）— Cosplay-lite 換裝近景

**場景說明**：鏡前試穿今晚戰袍的近景，貓耳頭飾 + 削肩背心的 cosplay-lite 組合，用來確認她「換裝」支柱的服裝與構圖風格。

**草稿 Prompt**（已依降低 AI 感檢查清單重寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, visible skin pores, subtle natural skin texture, slight oil sheen on the T-zone, unretouched skin detail, natural skin imperfections, petite figure with soft curves, ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, standing in front of a full-length mirror in her bedroom, wearing an off-the-shoulder cropped black tank top, a soft grey plush cat-ear headband, white thigh-high socks pulled to mid-thigh, and denim shorts, cosplay-lite styling, close-up upper-body mirror reflection shot, head slightly tilted assessing the outfit, warm bedroom lamp light mixed with a faint pink-purple RGB spill leaking in from the streaming room down the hall, uneven mixed color temperature across the frame, bedroom background shows a pile of half-tried-on cosplay pieces on the unmade bed, a phone charging cable snaking across the floor, and makeup scattered on the vanity edge, front-facing selfie framing reflected in the mirror, iPhone 14 Pro front camera, slight autofocus softness on the mirror's edges, screen-glow highlight clipping visible in the mirror's corner, subtle motion blur on the hem of her top as she turns, faint compression artifacts near the mirror's glare, film grain, candid lifestyle photo, streaming-room aesthetic
```

---

### 批次 3（計畫）— 深夜直播桌前場景（反應臉素材）

**場景說明**：直播中的近景反應臉，直視鏡頭、像在跟彈幕講話，是她最具代表性、互動感最強的內容類型，用來確認近距離表情捕捉的效果。

**草稿 Prompt**（已依降低 AI 感檢查清單重寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, visible skin pores, subtle natural skin texture with a slight oil sheen catching the monitor light, unretouched skin detail, natural skin imperfections, petite figure with soft curves, ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, sitting at her streaming desk wearing a gaming headset resting around her neck, wearing a fitted cropped white tank top with thin straps, exaggerated playful reaction expression looking directly at camera as if talking to chat, close-up face-to-chest crop, cool blue monitor glow as the key light on one side of her face mixed with pink RGB backlight behind her and a warm desk lamp glow providing uneven fill from the corner, visible soft shadow edges where the light sources overlap, desk cluttered with a drink can, a tissue box, and her phone propped against the monitor showing a blurred chat overlay, framed as a streaming webcam capture mounted above the monitor, slight autofocus softness around loose hair strands, cool-toned highlight clipping where the monitor backlight hits her cheek, faint webcam compression artifacts and mild frame judder typical of streaming capture, subtle motion blur on her hand gesturing near her face, faint cool blue-purple color-cast across the frame from the webcam's auto white balance, late-night streaming atmosphere, film grain, candid lifestyle photo, streaming-room aesthetic
```

---

### 批次 4（計畫）— 寬鬆帽T居家隨性照（下午甦醒版本）

**場景說明**：她的「早晨」——下午剛醒，帽T連著頭髮亂翹，沒有進入主播模式的最沒防備狀態，用來確認離線、卸下表演感時的視覺風格。

**草稿 Prompt**（已依降低 AI 感檢查清單重寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes, minimal smudged eye makeup left over from the night before, visible skin pores, subtle natural skin texture, slight under-eye puffiness, unretouched skin detail, natural skin imperfections, petite figure with soft curves, ash-brown hair loosely disheveled from sleep with the pastel-pink money-piece highlight visible through messy strands, slumped at her streaming desk just woken up, wearing an oversized grey gaming-brand hoodie with a faded logo print, hood up, sleeves pulled down over her hands, worn over sleep shorts, no makeup touch-up, half-lidded sleepy expression, dim afternoon light filtering through closed curtains mixed with the cool dormant standby glow of the monitor and a single warm desk lamp left on from the night before, heavy uneven light falloff with soft shadow edges, desk covered with snack wrappers, a spilled bubble-tea cup lid, tangled charger cables on the floor, her phone lying face-down amid the crumbs, and her cat curled up asleep on the desk mat, shot on iPhone 14 back camera propped near the desk, slight autofocus softness in the dim ambient light, gentle highlight clipping from the standby monitor glow on her cheek, subtle motion blur as she shifts her hoodie sleeve, visible JPEG compression noise in the darker corners of the frame, film grain, candid lifestyle photo, streaming-room aesthetic
```

---

### 批次 5（計畫）— 深夜卸妝／保養場景（浴室鏡前）

**場景說明**：凌晨下播後在浴室鏡前卸妝的流程，捕捉她卸下「主播人設」後最不設防的一面，對應人物設定中的「浴室 / 深夜保養」內容支柱（10%）——目前四個既有批次完全沒有涵蓋這個場景類型，優先用來補齊她內容支柱的視覺覆蓋率。

**草稿 Prompt**（已依降低 AI 感檢查清單撰寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with only one side of winged liner still on and the other side wiped away mid-routine, visible skin pores, subtle natural skin texture with slight redness where makeup was just removed, unretouched skin detail, natural skin imperfections, petite figure with soft curves, ash-brown hair pulled up messily into a loose bun with the pastel-pink money-piece highlight strand hanging loose, standing at the bathroom mirror at 3am after finishing her stream, wearing the same fitted cropped tank top from the stream with one strap slipping off her shoulder, holding a makeup-removal cotton pad mid-wipe across one cheek, tired unglamorous expression, cool white bathroom vanity light mixed with warm hallway light bleeding through the half-open door and a faint pink RGB glow reflected from the streaming room down the hall, mixed color temperature, uneven falloff across the mirror, sink counter cluttered with skincare bottles, used makeup wipes, a damp towel hung crooked on the hook, and her phone propped against the toothbrush holder showing a paused stream chat, front-facing selfie shot, iPhone 14 Pro front camera, slightly below eye-level angle toward the fogged mirror, natural autofocus softness on the mirror's steamed edges, highlight clipping from the vanity light bouncing off the mirror, subtle motion blur on the cotton pad mid-wipe, faint compression artifacts around the bright vanity bulb halo, film grain, candid lifestyle photo, streaming-room aesthetic
```

---

### 批次 6（計畫）— 展會後飯店房間（旅遊支柱）

**場景說明**：電競展或創作者聚會後回到飯店房間，還沒換下戰袍就窩在床上滑手機，是她內容中極少出現（10%）、但發生時反而最有「事件感」的場景類型，對應人物設定中的「飯店 / 旅遊」內容支柱——目前四個既有批次完全沒有涵蓋這類場景。

**草稿 Prompt**（已依降低 AI 感檢查清單撰寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with slightly worn-off winged liner from a long expo day, visible skin pores, subtle natural skin texture, slight oil sheen after a long day, unretouched skin detail, natural skin imperfections, petite figure with soft curves, ash-brown hair with loose waves slightly flattened from wearing a lanyard all day, pastel-pink money-piece highlight framing one side of her face, sitting cross-legged on a hotel bed still in her expo outfit, wearing a fitted cropped hoodie with her own streamer logo screen-printed on the front, denim shorts, and her expo lanyard with badge still hanging around her neck, sneakers kicked off on the floor nearby, scrolling her phone with an exhausted-but-happy expression, mixed harsh fluorescent-toned hotel ceiling downlight overhead blending with a warm bedside lamp and the cool blue glow of her phone screen lighting her face from below, uneven unflattering light falloff typical of real hotel lighting, an open suitcase overflowing with clothes on one side of the bed, expo merchandise (a lanyard, a small plushie, a rolled poster tube) piled on the other side, a phone charger snaking to the wall outlet, and a half-drunk convenience-store drink and room-service menu on the nightstand, shot on iPhone 14 back camera, slightly low angle across the hotel room, natural autofocus softness on the patterned bedspread in the background, highlight clipping from the harsh ceiling downlight overhead, subtle motion blur on her hand scrolling the phone screen, visible compression artifacts along the high-contrast window curtain edge, film grain, candid lifestyle photo, out-of-town event atmosphere
```

---

## 下一步（待執行）

1. 選定生成平台與模型（建議先測試 Seedream 4.5，比照 Iris Chen 的模型選擇結論）
2. 依批次 1–6 各生成 2 張測試圖，確認臉部特徵與挑染位置一致性
3. 篩選可用訓練圖，若一致性不足則調整 prompt 措辭後重新生成
4. 確認訓練圖集後，前往 Soul 訓練流程，建立 Mia Huang 專屬 Soul 模型
5. Soul 訓練完成後，才開始用訓練好的角色生成後續大量生活照與影片素材

**目前尚未有任何一步被執行。所有 soul_id、image_media_id、job_id、生成日期欄位均應留待實際生成後才填入，禁止在文件中預先填入未發生的資料。**
