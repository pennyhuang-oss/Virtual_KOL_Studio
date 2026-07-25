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

> **降低「AI 感」要求（2026-07-24 起適用）**：以下所有批次 prompt 均已依照 `SEXY_SCENE_LIBRARY.md` 的「降低『AI 感』的技術要點」五項檢查清單重寫——皮膚質感關鍵字、逐場景明確指定的拍攝裝置/鏡頭破綻、符合場景類型的光源配方、具體的生活雜物背景、完整明確的服裝描述。之後新增批次也必須比照同一份清單逐項檢查再定稿。

> **⚠️ 2026-07-25 燈光/身材數字校準**：比照 Vicky Lin 的二次修正（見 `kols/vicky-lin/generation_notes.md` 與 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉第 3 點 2026-07-25 修正）套用同一組修正到 Mia 身上，細節見本節下方說明與批次 prompt 的實際改動。

**基礎 prompt 模板**（所有批次共用，只替換 `[SCENE]` / `[OUTFIT]` / `[POSE/ANGLE]` / `[LIGHTING]` / `[DEVICE]` / `[CLUTTER]`）：

```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, visible skin pores, subtle natural skin texture, unretouched skin detail, natural skin imperfections, petite 160cm frame with soft curves, 91cm bust (F cup, full and lifted), 57cm waist (soft flat stomach with a gentle inward curve), 88cm hips (rounded), ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, [SCENE], wearing [OUTFIT — fully coordinated, color-matched styling], [POSE/ANGLE — playful, reactive, caught mid-expression], [LIGHTING — for indoor streaming-room scenes: vibrant layered RGB gaming light + crisp monitor glow + warm desk-lamp accent, colorful, sharply lit and well-exposed, NOT dim/muddy/degraded; for daytime/outdoor life-theme scenes (meetups, outings, family visits): golden hour or bright natural daylight, shallow depth of field with soft blurred background, crisp and clear], [CLUTTER — specific lived-in scene detail, e.g. streaming-room RGB cabling / snack wrappers, or scene-appropriate outdoor/indoor detail for life-theme scenes], [DEVICE — specific camera/webcam spec with autofocus softness / highlight clipping / motion blur / compression artifacts], crisp high-quality photography, vibrant true-to-life color, sharp focus on subject, film grain, candid lifestyle photo, streaming-room aesthetic (or natural lifestyle aesthetic for daytime/outdoor scenes)
```

**一致性重點**：
- 臉型、眼妝風格、粉色挑染的位置與髮色必須每批次保持一致；臉部描述只使用 `soft round youthful face` / `large expressive eyes` 這類語言，**絕對不要**混入 `sharp`、`angular`、`stern`、`narrow/almond-shaped eyes` 等會把臉推向銳利凌厲方向的字（已逐批次檢查，目前所有草稿都乾淨，之後新增批次也要比照這條檢查）
- 三圍與罩杯數字（91-57-88cm，F 罩杯，見 `profile.json` 的 `measurements`）已直接寫進基礎 prompt 本體，取代原本只靠「petite figure with soft curves」這種模糊形容詞帶過的寫法，之後所有批次都必須保留這幾個數字，不可省略
- 場景與服裝細節可以自由變化（這是她的內容多樣性來源），但服裝必須寫成同色系/同風格的**成套協調穿搭**，不要讓上下身各自散落搭配
- **光線分兩套配方，依場景類型選用**（比照 `SEXY_SCENE_LIBRARY.md` 2026-07-25 修正後的邏輯）：
  - **室內直播間場景（她的大多數內容）**：RGB 燈光與螢幕藍光仍是她的招牌視覺記號，不要換成自然光或乾淨棚拍三點打光；但光源要寫成「多層次、色彩鮮明、曝光清楚」——colorful RGB / 螢幕光可以混合多個光源、有色溫差異，這是真實感的來源，但**不等於刻意調暗、調糊、做舊**。舊版寫法（`uneven falloff`、`heavy uneven light falloff` 單獨使用）容易被生成模型解讀成「畫質差」，之後統一在光源描述後面加上 `vibrant`、`crisp`、`well-exposed`、`NOT dim/muddy/degraded` 這類字，確保色彩鮮明但畫面清楚
  - **白天/戶外生活主題場景（面基日、跟婷婷逛街、家庭聚餐、展會窗外白天景等「新增生活主題」內容）**：改用黃金時段或明亮自然日光 + 淺景深背景虛化的配方，**不要**沿用 RGB 直播間的光線邏輯——這類場景本來就是她少數離開直播間的時刻，光線也應該對應轉換
- 皮膚質感必須主動寫入 `visible skin pores` / `subtle natural skin texture` / `unretouched skin detail` 等關鍵字，避免 `smooth`、`flawless`、`airbrushed`、`porcelain skin` 這類會推向塑膠感的字
- 拍攝裝置與鏡頭要逐場景明確指定（前鏡頭自拍 / 後鏡頭 / 直播用 webcam 各自的破綻與色偏），不要只寫「shot on iPhone」交給模型自己猜——這些裝置級的細微破綻（對焦稍軟、highlight clipping、動態模糊、壓縮痕跡）跟「整體畫質差」是兩回事，前者要保留，後者要避免
- 背景雜物必須具體到場景本身（直播間場景：RGB 燈條纜線、能量飲料罐、耳機架、charging cable、零食包裝、貓玩具；生活主題場景：對應的戶外/聚會生活細節），不要只寫地點名稱
- 姿勢維持俏皮、反應式、抓拍到表情正中間的瞬間——她的喜感在臉部表情，這是她人格的核心視覺呈現，每批次都要保留
- 配件（電競耳機、控制器/手把、貓耳頭飾）如果場景合理就要明確逐場景寫出，不要只靠「gaming accessories」這種籠統詞帶過
- 收尾統一加上 `crisp high-quality photography, vibrant true-to-life color, sharp focus on subject` 這類畫質保證字，明確排除 `degraded`、`muddy`、`grainy`——即使 RGB 燈光本身很鮮豔多彩，畫面本身仍應該乾淨清晰，不是「刻意拍差」

---

## 計畫批次 Prompt 規劃（尚未執行）

> 以下七個批次為建議拍攝方向，涵蓋她最核心的視覺場景與尚未涵蓋的內容支柱（浴室保養、飯店旅遊、白天生活主題）。每批次建議先生成 2 張測試臉部與場景一致性，確認可用後再決定是否擴充張數。**目前皆未執行、無 job ID、無實際生成圖。**（批次 7 為 2026-07-25 校準時新增，用來示範戶外/白天生活主題場景該用的光線配方，見文末「2026-07-25 燈光/身材數字校準」。）

### 批次 1（計畫）— 電競椅設定照（建立基礎一致性）

**場景說明**：她的直播間主場景——坐在電競椅上，RGB 燈條在背景，桌上有耳機和飲料，這是後續大部分素材的核心背景設定，優先用來確認臉部與場景風格的一致性。

**草稿 Prompt**（已依降低 AI 感檢查清單重寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, visible skin pores, subtle natural skin texture with slight oil sheen on the T-zone, unretouched skin detail, natural skin imperfections, petite 160cm frame with soft curves, 91cm bust (F cup, full and lifted), 57cm waist (soft flat stomach with a gentle inward curve), 88cm hips (rounded), ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, sitting in gaming chair in home streaming room, wearing an oversized black gaming-brand hoodie (fully zipped) with a screen-printed logo patch on the chest and matching black shorts underneath — coordinated black-on-black set, hood down, a gaming headset resting around her neck, relaxed 3/4 angle looking toward camera, playful mid-expression as if reacting to something on screen, vibrant layered RGB LED light strips cycling purple-to-pink glowing on the wall behind her mixed with crisp cool blue monitor glow on her face and a warm desk lamp accent bleeding in from the corner of the frame, colorful and sharply lit, well-exposed with soft natural shadow edges where the RGB and lamp light overlap — NOT dim, muddy, or degraded, gaming desk cluttered with a tangled RGB cable, a half-empty energy drink can, a phone lying face-down next to the keyboard, a headset stand, and a small cat plush toy on the shelf behind her, shot on iPhone 14 back camera, slight autofocus softness on the RGB light strips in the background, natural highlight clipping on the monitor's bright edge, subtle motion blur on her hand near the headset, faint JPEG compression artifacts visible in the shadow areas, crisp high-quality photography, vibrant true-to-life color, sharp focus on subject, film grain, candid lifestyle photo, streaming-room aesthetic
```

---

### 批次 2（計畫）— Cosplay-lite 換裝近景

**場景說明**：鏡前試穿今晚戰袍的近景，貓耳頭飾 + 削肩背心的 cosplay-lite 組合，用來確認她「換裝」支柱的服裝與構圖風格。

**草稿 Prompt**（已依降低 AI 感檢查清單重寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, visible skin pores, subtle natural skin texture, slight oil sheen on the T-zone, unretouched skin detail, natural skin imperfections, petite 160cm frame with soft curves, 91cm bust (F cup, full and lifted), 57cm waist (soft flat stomach with a gentle inward curve), 88cm hips (rounded), ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, standing in front of a full-length mirror in her bedroom, wearing a color-coordinated black-and-white cosplay-lite set — off-the-shoulder cropped black tank top, a soft grey plush cat-ear headband, white thigh-high socks pulled to mid-thigh, and denim shorts, cosplay-lite styling, close-up upper-body mirror reflection shot, head slightly tilted assessing the outfit with a playful half-smile, warm bedroom lamp light mixed with a vibrant pink-purple RGB spill leaking in from the streaming room down the hall, colorful and crisply lit, well-exposed mixed color temperature across the frame — NOT dim or muddy, bedroom background shows a pile of half-tried-on cosplay pieces on the unmade bed, a phone charging cable snaking across the floor, and makeup scattered on the vanity edge, front-facing selfie framing reflected in the mirror, iPhone 14 Pro front camera, slight autofocus softness on the mirror's edges, screen-glow highlight clipping visible in the mirror's corner, subtle motion blur on the hem of her top as she turns, faint compression artifacts near the mirror's glare, crisp high-quality photography, vibrant true-to-life color, sharp focus on subject, film grain, candid lifestyle photo, streaming-room aesthetic
```

---

### 批次 3（計畫）— 深夜直播桌前場景（反應臉素材）

**場景說明**：直播中的近景反應臉，直視鏡頭、像在跟彈幕講話，是她最具代表性、互動感最強的內容類型，用來確認近距離表情捕捉的效果。

**草稿 Prompt**（已依降低 AI 感檢查清單重寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, visible skin pores, subtle natural skin texture with a slight oil sheen catching the monitor light, unretouched skin detail, natural skin imperfections, petite 160cm frame with soft curves, 91cm bust (F cup, full and lifted), 57cm waist (soft flat stomach with a gentle inward curve), 88cm hips (rounded), ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, sitting at her streaming desk wearing a gaming headset resting around her neck, wearing a fitted cropped white tank top with thin straps, exaggerated playful reaction expression looking directly at camera as if talking to chat, close-up face-to-chest crop, cool blue monitor glow as the key light on one side of her face mixed with vibrant pink RGB backlight behind her and a warm desk lamp glow providing bright, colorful, crisply-lit fill from the corner — well-exposed with soft shadow edges where the light sources overlap, NOT dim or muddy, desk cluttered with a drink can, a tissue box, and her phone propped against the monitor showing a blurred chat overlay, framed as a streaming webcam capture mounted above the monitor, slight autofocus softness around loose hair strands, cool-toned highlight clipping where the monitor backlight hits her cheek, faint webcam compression artifacts and mild frame judder typical of streaming capture, subtle motion blur on her hand gesturing near her face, faint cool blue-purple color-cast across the frame from the webcam's auto white balance, late-night streaming atmosphere, crisp high-quality photography, vibrant true-to-life color, sharp focus on subject, film grain, candid lifestyle photo, streaming-room aesthetic
```

---

### 批次 4（計畫）— 寬鬆帽T居家隨性照（下午甦醒版本）

**場景說明**：她的「早晨」——下午剛醒，帽T連著頭髮亂翹，沒有進入主播模式的最沒防備狀態，用來確認離線、卸下表演感時的視覺風格。

**草稿 Prompt**（已依降低 AI 感檢查清單重寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes, minimal smudged eye makeup left over from the night before, visible skin pores, subtle natural skin texture, slight under-eye puffiness, unretouched skin detail, natural skin imperfections, petite 160cm frame with soft curves, 91cm bust (F cup, full and lifted), 57cm waist (soft flat stomach with a gentle inward curve), 88cm hips (rounded), ash-brown hair loosely disheveled from sleep with the pastel-pink money-piece highlight visible through messy strands, slumped at her streaming desk just woken up, wearing an oversized grey gaming-brand hoodie with a faded logo print, hood up, sleeves pulled down over her hands, worn over matching grey sleep shorts, no makeup touch-up, half-lidded sleepy expression, muted low-key afternoon light filtering through closed curtains mixed with the cool dormant standby glow of the monitor and a single warm desk lamp left on from the night before — moody and dim in mood but still crisply shot and well-exposed in the lit areas, soft natural shadow edges, NOT muddy or degraded, desk covered with snack wrappers, a spilled bubble-tea cup lid, tangled charger cables on the floor, her phone lying face-down amid the crumbs, and her cat curled up asleep on the desk mat, shot on iPhone 14 back camera propped near the desk, slight autofocus softness in the dim ambient light, gentle highlight clipping from the standby monitor glow on her cheek, subtle motion blur as she shifts her hoodie sleeve, faint JPEG compression texture in the darker corners of the frame, crisp high-quality photography, sharp focus on subject despite the low-key mood, film grain, candid lifestyle photo, streaming-room aesthetic
```

---

### 批次 5（計畫）— 深夜卸妝／保養場景（浴室鏡前）

**場景說明**：凌晨下播後在浴室鏡前卸妝的流程，捕捉她卸下「主播人設」後最不設防的一面，對應人物設定中的「浴室 / 深夜保養」內容支柱（10%）——目前四個既有批次完全沒有涵蓋這個場景類型，優先用來補齊她內容支柱的視覺覆蓋率。

**草稿 Prompt**（已依降低 AI 感檢查清單撰寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with only one side of winged liner still on and the other side wiped away mid-routine, visible skin pores, subtle natural skin texture with slight redness where makeup was just removed, unretouched skin detail, natural skin imperfections, petite 160cm frame with soft curves, 91cm bust (F cup, full and lifted), 57cm waist (soft flat stomach with a gentle inward curve), 88cm hips (rounded), ash-brown hair pulled up messily into a loose bun with the pastel-pink money-piece highlight strand hanging loose, standing at the bathroom mirror at 3am after finishing her stream, wearing the same fitted cropped tank top from the stream with one strap slipping off her shoulder, holding a makeup-removal cotton pad mid-wipe across one cheek, tired unglamorous expression, crisp cool white bathroom vanity light mixed with warm hallway light bleeding through the half-open door and a vibrant faint pink RGB glow reflected from the streaming room down the hall, colorful mixed color temperature, well-exposed and clearly lit across the mirror — NOT dim or muddy, sink counter cluttered with skincare bottles, used makeup wipes, a damp towel hung crooked on the hook, and her phone propped against the toothbrush holder showing a paused stream chat, front-facing selfie shot, iPhone 14 Pro front camera, slightly below eye-level angle toward the fogged mirror, natural autofocus softness on the mirror's steamed edges, highlight clipping from the vanity light bouncing off the mirror, subtle motion blur on the cotton pad mid-wipe, faint compression artifacts around the bright vanity bulb halo, crisp high-quality photography, vibrant true-to-life color, sharp focus on subject, film grain, candid lifestyle photo, streaming-room aesthetic
```

---

### 批次 6（計畫）— 展會後飯店房間（旅遊支柱）

**場景說明**：電競展或創作者聚會後回到飯店房間，還沒換下戰袍就窩在床上滑手機，是她內容中極少出現（10%）、但發生時反而最有「事件感」的場景類型，對應人物設定中的「飯店 / 旅遊」內容支柱——目前四個既有批次完全沒有涵蓋這類場景。

**草稿 Prompt**（已依降低 AI 感檢查清單撰寫）：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with slightly worn-off winged liner from a long expo day, visible skin pores, subtle natural skin texture, slight oil sheen after a long day, unretouched skin detail, natural skin imperfections, petite 160cm frame with soft curves, 91cm bust (F cup, full and lifted), 57cm waist (soft flat stomach with a gentle inward curve), 88cm hips (rounded), ash-brown hair with loose waves slightly flattened from wearing a lanyard all day, pastel-pink money-piece highlight framing one side of her face, sitting cross-legged on a hotel bed still in her expo outfit, wearing a color-coordinated fitted cropped hoodie with her own streamer logo screen-printed on the front and matching denim shorts, her expo lanyard with badge still hanging around her neck, sneakers kicked off on the floor nearby, scrolling her phone with an exhausted-but-happy expression, warm bedside lamp as the main light blending with cooler hotel ceiling downlight and the cool blue glow of her phone screen lighting her face from below, mixed indoor color temperature with soft visible shadow edges — crisply lit and well-exposed, NOT dim, muddy, or degraded despite the ordinary hotel-room lighting, an open suitcase overflowing with clothes on one side of the bed, expo merchandise (a lanyard, a small plushie, a rolled poster tube) piled on the other side, a phone charger snaking to the wall outlet, and a half-drunk convenience-store drink and room-service menu on the nightstand, shot on iPhone 14 back camera, slightly low angle across the hotel room, natural autofocus softness on the patterned bedspread in the background, highlight clipping from the ceiling downlight overhead, subtle motion blur on her hand scrolling the phone screen, faint compression artifacts along the high-contrast window curtain edge, crisp high-quality photography, vibrant true-to-life color, sharp focus on subject, film grain, candid lifestyle photo, out-of-town event atmosphere
```

---

### 批次 7（計畫）— 面基日白天外出（生活主題，新增示範批次）

**場景說明**：對應 `content_style.md`／`character.md` 的「面基日」與「難得白天出門」生活主題——跟阿光和朋友白天外出聚會，或跟婷婷逛街。這是她少數真的離開直播間、離開 RGB 光源的時刻，2026-07-25 校準前本文件完全沒有涵蓋這類場景的草稿 prompt。新增本批次作為「戶外/生活風格場景改用自然光配方」的具體示範，往後任何白天/戶外生活主題批次都應比照這裡的光線寫法，而不是沿用直播間 RGB 配方。

**草稿 Prompt**：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft everyday makeup (lighter than her streaming look), glossy tinted lips, rounded soft blush, visible skin pores, subtle natural skin texture, unretouched skin detail, natural skin imperfections, petite 160cm frame with soft curves, 91cm bust (F cup, full and lifted), 57cm waist (soft flat stomach with a gentle inward curve), 88cm hips (rounded), ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, sitting at an outdoor café table with a friend group mid-laugh, wearing a color-coordinated plain white T-shirt and light-wash denim shorts — the "trying to look like a normal person" outfit she picks for daytime outings, not her usual streaming fits, playful candid laugh caught mid-expression, looking slightly off-camera toward her friends rather than posed, bright clear daytime sunlight, soft natural directional light with flattering falloff, shallow depth of field with a softly blurred café-street background, crisp sharp focus on her face, table cluttered with iced drinks, a phone face-up next to her, and a shopping bag hooked over the chair, shot on iPhone 15 handheld by a friend across the table, slight natural autofocus softness on the background bokeh, natural highlight rendering in the bright daylight, subtle motion blur on her hand mid-gesture while laughing, faint compression texture at the high-contrast sunlit edges, crisp high-quality photography, vibrant true-to-life color, sharp focus on subject — NOT degraded, muddy, or grainy, natural color grading, film grain, candid lifestyle photo, natural daytime lifestyle aesthetic (deliberately not the streaming-room aesthetic — this is one of her rare off-duty daylight scenes)
```

---

## 下一步（待執行）

1. 選定生成平台與模型（建議先測試 Seedream 4.5，比照 Iris Chen 的模型選擇結論）
2. 依批次 1–7 各生成 2 張測試圖，確認臉部特徵與挑染位置一致性
3. 篩選可用訓練圖，若一致性不足則調整 prompt 措辭後重新生成
4. 確認訓練圖集後，前往 Soul 訓練流程，建立 Mia Huang 專屬 Soul 模型
5. Soul 訓練完成後，才開始用訓練好的角色生成後續大量生活照與影片素材

**目前尚未有任何一步被執行。所有 soul_id、image_media_id、job_id、生成日期欄位均應留待實際生成後才填入，禁止在文件中預先填入未發生的資料。**

---

## 2026-07-25 燈光/身材數字校準

**觸發原因**：比照 Vicky Lin 同一輪修正（見 `kols/vicky-lin/generation_notes.md` 的「2026-07-25 二次修正」與 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉第 3 點的 2026-07-25 修正）——真實使用者反饋指出，把「真實感」寫成「刻意不完美、混亂不均勻的光源」，很容易被生成模型理解成「畫質很差」，這是錯的因果關係。真實感應該來自皮膚質感、生活雜物細節與裝置級的具體破綻，不是靠調暗、調糊、做舊整體畫面。同時三圍等身材數據如果只靠模糊形容詞帶過，容易跟 `profile.json` 設定的實際數字對不上。

**這輪對 Mia 的具體改動**：
- **身材數字**：核心 prompt 模板與全部 6 個既有批次（現為 7 個批次）的「petite figure with soft curves」都改成「petite 160cm frame with soft curves, 91cm bust (F cup, full and lifted), 57cm waist (soft flat stomach with a gentle inward curve), 88cm hips (rounded)」——三圍與罩杯數字直接取自 `profile.json` 的 `identity.appearance.measurements`（91-57-88cm，F 罩杯），不再只靠模糊形容詞
- **臉部**：檢查了本文件所有草稿 prompt 字串，確認沒有殘留 Vicky Lin 曾出現過的 `almond-shaped`／`angular`／`stern`／`sharp features` 這類會把臉推向銳利凌厲方向的舊字眼——Mia 的臉部描述本來就一直是 `soft round youthful face` / `large expressive eyes`，這條檢查結果是「乾淨、不需修改」，僅在「一致性重點」補上一條明講排除項的說明，避免之後新增批次不小心引入
- **光線**：這是本輪修正的重點。RGB / 螢幕藍光仍然是她的招牌，**不取消、不改成自然光**——但所有批次的光線描述從「uneven falloff」、「heavy uneven light falloff」、「uneven unflattering light falloff」這種容易被解讀成「畫質差」的寫法，改成「vibrant」、「colorful」、「crisply lit」、「well-exposed」+ 明講 `NOT dim/muddy/degraded`。裝置級的細微破綻（autofocus softness、highlight clipping、motion blur、compression artifacts）全部保留，因為那些是「降低 AI 感」需要的真實感來源，跟「整體畫質故意調差」是兩回事，不能混為一談
- **新增批次 7**：既有 6 個批次全部是室內直播間場景，完全沒有涵蓋 `content_style.md`／`character.md` 已經寫入的「面基日」「難得白天出門」這類生活主題场景。新增批次 7 作為示範，改用 `SEXY_SCENE_LIBRARY.md` 2026-07-25 修正後的「戶外/生活風格場景」配方（黃金時段或明亮自然日光 + 淺景深背景虛化 + crisp high dynamic range），不沿用 RGB 直播間光線邏輯——之後任何白天/戶外生活主題批次都應比照這個示範
- **服裝**：既有批次的穿搭本來就已經算完整明確，這輪額外補上「color-coordinated」/「coordinated」這類字眼，確保成套穿搭而非上下身各自散落配色
- **姿勢與配件**：俏皮反應式的抓拍姿勢維持不變（這是她人格的核心視覺呈現）；電競耳機、貓耳頭飾等配件在各批次中已存在，這輪確認並保留其明確描述，未刪減
- **畫質收尾**：每個批次結尾統一加上 `crisp high-quality photography, vibrant true-to-life color, sharp focus on subject`，並在光線描述中明講 `NOT dim/muddy/degraded`，確保即使是 RGB 多彩光源，畫面本身依然乾淨清晰，不是「刻意拍差」

**未變更項目**：`profile.json` 完全未修改；臉型、三圍原始設定值、髮型/挑染、穿搭品項、直播主播人格與內容支柱設定全部保持不變——這輪只調整技術執行層面的 prompt 措辭，不改變角色設定本身。

---

## 2026-07-25 發現用候選圖批次（已生成 4 張，等待使用者挑選喜歡的臉／風格 — ⚠️ PENDING，尚未錨定 Element、尚未送入 Soul 訓練）

**狀態：⚠️ PENDING — 這只是「發現批次」（discovery batch），目的是讓使用者從少量候選圖中挑一張最喜歡的臉/風格，之後才會把核准的那一張透過 Reference Element 錨定身分，再擴充成完整訓練圖集。比照 Vicky Lin 的兩階段流程經驗（見 `kols/vicky-lin/generation_notes.md` 第二～四輪）——獨立生成的圖彼此身分不保證一致，所以本輪 4 張**還沒有**用 Element 錨定，每張都是各自獨立生成，臉部細節預期會有落差，這是正常現象，不是錯誤。本輪**未**建立 Reference Element、**未**呼叫 `show_characters(action='train')`，`profile.json` 的 soul_id 維持原狀（空白）。

**模型選擇**：呼叫 `models_explore(action='recommend', query='generating consistent character reference images for a new persona without an existing soul_id...')`，結果列出 `soul_cast`、`seedance_2_0`、`soul_2`（match_reason 含 `character-intent: preferred-model+120`）、及兩個語音相關模型。因 Mia 尚未有 `soul_id`，採用 `soul_2`——同時符合 `generate_image` 工具說明中「`soul_2`/`nano_banana_pro` for one-off character refs」的預設建議，也與 Vicky Lin 第二、三輪的模型選擇一致。`aspect_ratio: 9:16`，`quality: 2k` 請求送出（但實際回傳的生成參數顯示 `quality: "1080p"`，可能是 `soul_2` 內部對 2k 檔位的實際輸出標示，非請求本身有誤）。

**費用**：`get_cost: true` 預檢（prompt 為簡短測試字串）回傳每張約 1 credit（0.12 credits_exact）。實際生成 4 張完整 prompt 後，餘額由生成前 **18.23 credits** 降至生成後 **15.83 credits**，共花費 **2.4 credits**（平均每張 0.6 credits）——比預檢數字高，可能是完整 prompt 長度/解析度與預檢測試字串不同所致，之後若要精算預算建議用完整 prompt 文字重新 `get_cost` 一次。

**內容設計**：4 張都直接沿用本文件「計畫批次 1」（電競椅設定照）已核准的核心外觀描述（臉型、妝容、髮色/粉色挑染、三圍數字、場景、穿搭、RGB 光線配方、裝置破綻、雜物細節）逐字不變，**只變化姿勢/角度/景別**，符合本次任務「核心外觀描述在 4 張之間保持一致，只變化角度/取景」的要求：

| 檔名 | 角度／景別 | 說明 | Job ID | 狀態 |
|------|-----------|------|--------|------|
| `candidate_01.png` | 正面．臉部特寫 | 正面直視鏡頭，肩頸以上特寫 | `9ea22aed-5908-483e-a833-b3a274a9115b` | ✅ completed |
| `candidate_02.png` | 正面．半身 | 正面直視鏡頭，腰部以上取景 | `d3f7ee59-1ca6-4767-8374-84c5915c417b` | ✅ completed |
| `candidate_03.png` | 四分之三側．半身 | 側身回望鏡頭，腰部以上取景 | `950e91af-6fef-49a1-9f72-48fa57d9e24e` | ✅ completed |
| `candidate_04.png` | 正面．全身 | 正面直視鏡頭，坐姿全身入鏡含電競椅與書桌背景 | `5d3057d6-fc1f-4586-9324-7a4dab2808c7` | ✅ completed |

**產出位置**：`kols/mia-huang/images/face_reference/candidate_01.png` ～ `candidate_04.png`（新建目錄）。

**生成後目視檢查**：已用 Read 工具實際開圖檢視 `candidate_01`（正面特寫）與 `candidate_04`（正面全身）——兩張都呈現圓潤柔和娃娃臉、灰棕髮色帶粉色挑染、RGB 燈光電競椅場景、黑色帽T戰袍，風格與人設吻合；但如預期，兩張彼此的五官細節不是同一張臉（因為尚未用 Element 錨定身分，這正是本批次要解決的問題——先選出使用者最喜歡的那一張臉，再進入錨定階段）。

**⚠️ 下一步（不可跳過）**：
1. 等待使用者實際看過 `candidate_01` ～ `candidate_04` 這 4 張圖，明確指出最喜歡哪一張的臉／風格
2. 使用者核准某一張後，比照 Vicky Lin 第四輪流程：`media_upload` 上傳核准圖 → `media_confirm` → `show_reference_elements(action='create', category='character', ...)` 建立 Mia 專屬 Reference Element
3. 用該 Element 錨定身分，擴充生成完整訓練圖集（比照本文件「計畫批次 1–7」的場景規劃，逐批次在 prompt 中內嵌 `<<<element_id>>>`）
4. 訓練圖集確認一致後，才前往 `show_characters(action='train')` 建立 Mia 專屬 Soul 模型

本輪結束時，`profile.json` 完全未修改，soul_id 仍為空白，Soul 訓練**尚未**啟動，整體狀態維持 **PENDING**。
