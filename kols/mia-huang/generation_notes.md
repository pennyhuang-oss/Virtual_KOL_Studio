# Mia Huang — AI 生成規劃

> **狀態：✅ Soul 訓練已完成（`status: ready`），soul_id `e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4` 已可用於 `model: soul_2` 正式生成內容**

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
| AI 生成狀態 | **Soul 訓練已送出，訓練中（尚未 ready）。使用者已核准 4 張候選圖並明確授權送訓；已選定 `candidate_02.png` 建立 Reference Element（`element_id: 92ffbd80-32c7-495f-91ed-f109b419bb41`）並生成 13 張完整訓練圖集（`kols/mia-huang/images/training_v1/`），13 張已重新上傳並送入 `show_characters(action='train')`，取得 `soul_id: e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4`（已驗證伺服器端真實存在，目前狀態 queued/training，尚未 ready）。`profile.json` 已寫入此 soul_id，狀態標記為 `training`，待下個 session 確認完成後更新為 `ready`。** |

---

## 核心 Prompt 結構

> 沿用 Iris Chen 的驗證結論：亞洲臉孔生成建議優先測試 Seedream 4.5（`seedream_v4_5`），Recraft 系列對亞洲臉孔容易生成路人臉。Mia 尚未實測，此為根據既有經驗的建議起點，非已驗證結果。

> **降低「AI 感」要求（2026-07-24 起適用）**：以下所有批次 prompt 均已依照 `SEXY_SCENE_LIBRARY.md` 的「降低『AI 感』的技術要點」五項檢查清單重寫——皮膚質感關鍵字、逐場景明確指定的拍攝裝置/鏡頭破綻、符合場景類型的光源配方、具體的生活雜物背景、完整明確的服裝描述。之後新增批次也必須比照同一份清單逐項檢查再定稿。

> **⚠️ 2026-07-25 燈光/身材數字校準**：比照 Vicky Lin 的二次修正（見 `kols/vicky-lin/generation_notes.md` 與 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉第 3 點 2026-07-25 修正）套用同一組修正到 Mia 身上，細節見本節下方說明與批次 prompt 的實際改動。

**基礎 prompt 模板**（所有批次共用，只替換 `[SCENE]` / `[OUTFIT]` / `[POSE/ANGLE]` / `[LIGHTING]` / `[DEVICE]` / `[CLUTTER]`）：

```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored), visible skin pores, subtle natural skin texture, unretouched skin detail, natural skin imperfections, petite 160cm frame with soft curves, 91cm bust (F cup, full and lifted), 57cm waist (soft flat stomach with a gentle inward curve), 88cm hips (rounded), ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, [SCENE], wearing [OUTFIT — fully coordinated, color-matched styling], [POSE/ANGLE — playful, reactive, caught mid-expression], [LIGHTING — for indoor streaming-room scenes: vibrant layered RGB gaming light + crisp monitor glow + warm desk-lamp accent, colorful, sharply lit and well-exposed, NOT dim/muddy/degraded; for daytime/outdoor life-theme scenes (meetups, outings, family visits): golden hour or bright natural daylight, shallow depth of field with soft blurred background, crisp and clear], [CLUTTER — specific lived-in scene detail, e.g. streaming-room RGB cabling / snack wrappers, or scene-appropriate outdoor/indoor detail for life-theme scenes], [DEVICE — specific camera/webcam spec with autofocus softness / highlight clipping / motion blur / compression artifacts], crisp high-quality photography, vibrant true-to-life color, sharp focus on subject, film grain, candid lifestyle photo, streaming-room aesthetic (or natural lifestyle aesthetic for daytime/outdoor scenes)
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

**產出位置（原始檔名，已於三次修正時改名）**：`kols/mia-huang/images/face_reference/candidate_01.png` ～ `candidate_04.png`（新建目錄）。**2026-07-25 三次修正更新**：這 4 張第一輪圖片已改名為 `round1_candidate_01.png`～`round1_candidate_04.png`，保留作為「膚色偏古銅、身分不一致」問題的歷史紀錄；`candidate_01.png`～`candidate_04.png` 這組檔名現在指向用 `seedream_v4_5` 重新生成的第二輪修正版，詳見文末章節。

**生成後目視檢查**：已用 Read 工具實際開圖檢視 `candidate_01`（正面特寫）與 `candidate_04`（正面全身）——兩張都呈現圓潤柔和娃娃臉、灰棕髮色帶粉色挑染、RGB 燈光電競椅場景、黑色帽T戰袍，風格與人設吻合；但如預期，兩張彼此的五官細節不是同一張臉（因為尚未用 Element 錨定身分，這正是本批次要解決的問題——先選出使用者最喜歡的那一張臉，再進入錨定階段）。

**⚠️ 下一步（不可跳過）**：
1. 等待使用者實際看過 `candidate_01` ～ `candidate_04` 這 4 張圖，明確指出最喜歡哪一張的臉／風格
2. 使用者核准某一張後，比照 Vicky Lin 第四輪流程：`media_upload` 上傳核准圖 → `media_confirm` → `show_reference_elements(action='create', category='character', ...)` 建立 Mia 專屬 Reference Element
3. 用該 Element 錨定身分，擴充生成完整訓練圖集（比照本文件「計畫批次 1–7」的場景規劃，逐批次在 prompt 中內嵌 `<<<element_id>>>`）
4. 訓練圖集確認一致後，才前往 `show_characters(action='train')` 建立 Mia 專屬 Soul 模型

本輪結束時，`profile.json` 完全未修改，soul_id 仍為空白，Soul 訓練**尚未**啟動，整體狀態維持 **PENDING**。

---

## 2026-07-25 三次修正：改用 Seedream 4.5 並補上膚色 prompt 本體

**觸發原因**：使用者對第一輪發現用候選圖的回饋是「Mia 還可以，但是 4 張圖片也長得不太一樣」——臉/風格本身可接受，但身分一致性不夠。回顧第一輪的兩個實際問題：

1. **模型問題**：第一輪用的是 `soul_2`。`soul_2` 在沒有訓練好的 `soul_id` 時，每次獨立呼叫都是重新想像一張全新的臉，這正是本次任務要修正的根本原因——比照 `kols/iris-chen/generation_notes.md` 記載的驗證結論，`seedream_v4_5`（Seedream 4.5）在同一段文字 prompt 下重複生成時，臉部一致性高到「4 張會長得太像，所以一批只生成 2 張」的程度，這才是本工作室唯一驗證過能在沒有 soul_id 的情況下維持人臉一致性的模型。
2. **膚色問題**：`profile.json` 的 `identity.appearance.face_type` 與 `character.md` 都已經補上「Fair, luminous porcelain-toned skin（NOT tanned, bronzed, olive, or deep golden/wheat-colored）／膚色白皙透亮」這句話，但**本文件「核心 Prompt 結構」章節的基礎 prompt 模板本體，實際上從未真的加上這句話**——模板裡原本只有 `visible skin pores, subtle natural skin texture, unretouched skin detail, natural skin imperfections` 這些描述皮膚質感（毛孔/紋理）的字，完全沒有描述膚色本身的字。第一輪的 4 張候選圖就是用這個「漏了膚色」的模板 + `soul_2` 生成的，這才是膚色偏古銅/曬黑色調的真正原因。

**這輪的具體改動**：

1. **base prompt 模板本體**（`kols/mia-huang/generation_notes.md`「核心 Prompt 結構」章節）：在 `rounded soft blush,` 之後、`visible skin pores` 之前，插入 `fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored),`——用字與 `profile.json` 的 `face_type` 完全一致，不新增也不刪減任何其他臉部/人格描述。
2. **模型**：由 `soul_2` 改為 `seedream_v4_5`，`aspect_ratio: 9:16`，`quality: basic`。
3. **檔案改名**：第一輪 4 張圖（原 `candidate_01.png`～`candidate_04.png`）用 `git mv` 改名為 `round1_candidate_01.png`～`round1_candidate_04.png`，保留作歷史紀錄。
4. **重新生成**：沿用本文件「計畫批次 1」（電競椅設定照）已核准的場景/服裝/光線/雜物/裝置破綻描述，套用上面補好膚色的核心外觀描述，**逐字不變，只變化姿勢/角度/景別**——與第一輪相同的四種取景邏輯：正面特寫／正面半身／四分之三側半身／正面全身（坐姿全身含電競椅與書桌背景）。

**費用**：`get_cost: true` 對完整 prompt 文字預檢，回傳每張 1 credit。比對 `transactions` 交易紀錄的時間戳與各 job 的 `createdAt`，這 4 張圖各自對應一筆 `Seedream 4.5 -1 credit` 的扣款，共 **4 credits**，與預檢數字完全吻合（與第一輪 `soul_2` 預檢/實際不一致的狀況不同）。帳號餘額本身在同一時段內另有下降（`11.35 → 0.35`），但這是共用帳號下其他並行任務造成的（同時間 `git status` 也顯示 `rainie-hsu`／`sophia-tseng`／`zoe-lai`／`coco-wu` 等其他 KOL 檔案被修改，屬於別的並行工作，非本次任務所生成），非本次 4 張圖的實際花費。

**新一輪 Job ID 與檔名對照**：

| 檔名 | 角度／景別 | Job ID | Seed | 狀態 |
|------|-----------|--------|------|------|
| `candidate_01.png` | 正面．臉部特寫（肩頸以上） | `7be6df74-5c4a-4048-9bb4-2d22e6b4f498` | 597421 | ✅ completed |
| `candidate_02.png` | 正面．半身（腰部以上） | `8b370f9a-fcc0-4986-a473-8eb7068d655e` | 523549 | ✅ completed |
| `candidate_03.png` | 四分之三側．半身，回望鏡頭 | `758ab28b-b330-4e02-a28f-2834511d8f47` | 839129 | ✅ completed |
| `candidate_04.png` | 正面．全身，坐姿含電競椅／書桌背景 | `6a5821a8-8e5b-43b7-890a-e0c2e5e65134` | 859828 | ✅ completed |

**產出位置**：`kols/mia-huang/images/face_reference/candidate_01.png` ～ `candidate_04.png`（覆蓋為修正後版本；第一輪原圖見上方改名後的 `round1_candidate_*.png`）。

**生成後目視檢查與誠實評估**：已用 Read 工具實際開圖檢視全部 4 張。

- **膚色**：4 張皮膚都清楚偏白皙、透亮的粉色調，沒有出現古銅／小麥／曬黑色調，`fair, luminous porcelain-toned skin` 這句話生效——膚色問題確認修正成功。
- **臉部一致性**：4 張的圓潤娃娃臉、深棕色眼睛、灰棕髮色配臉側粉色挑染的位置、臉頰兩側淡淡雀斑、上揚眼線、水潤唇彩妝感，在 4 張之間明顯比第一輪（`soul_2`）更接近同一個人——第一輪使用者形容「4 張長得不太一樣」的落差，在這一輪有實質改善。誠實地說，4 張並非像素級的同一張臉：`candidate_04`（正面全身）瀏海分法比其他 3 張更貼齊額頭、臉型在特寫鏡頭下顯得略圓一些；`candidate_03`（四分之三側臉）因為角度關係五官比例看起來也有些微差異。但核心可辨識特徵（挑染位置、眼型與眼妝風格、唇色唇形、雀斑分布、髮色）在 4 張間相當一致，比第一輪的「4 張根本是不同人」的落差有明顯進步，符合 Iris Chen 用 Seedream 4.5「同 prompt 重複生成臉部高度一致」的既有結論。
- **場景/服裝一致性**：4 張的黑色連帽外套、電競椅、RGB 紫粉燈條、螢幕藍光、貓玩具擺設、耳機掛頸等場景細節都維持一致，符合「只變化角度取景」的設計目標。

**未變更項目**：`profile.json`、`character.md` 均未再修改（膚色描述在先前修正已到位，本輪未動）；臉型、三圍、人格設定、批次 1–7 的計畫 prompt 文字內容不變，僅補了「核心 Prompt 結構」模板本體的膚色字句。

**⚠️ 下一步（不可跳過，本輪未執行）**：
1. 等待使用者實際看過這輪修正後的 `candidate_01`～`candidate_04`，確認臉部一致性與膚色是否已達可接受標準
2. 使用者核准某一張臉後，才比照 Vicky Lin 第四輪流程建立 Reference Element 錨定身分
3. 本輪**未**建立 Reference Element、**未**呼叫 `show_characters(action='train')`，`profile.json` 的 `soul_id` 仍為空白，整體狀態維持 **PENDING**

**本次任務執行到此為止，等待使用者查看結果並回覆，暫不進行任何進一步生成或錨定操作。**

---

## 2026-07-30 訓練圖集生成（Element 錨定）

**狀態：⚠️ 使用者已回覆 4 張候選圖皆可接受，並授權挑選任一張作為身分錨定圖、建立完整訓練圖集。本輪已完成 Element 建立與 13 張訓練圖生成，等待使用者審核這組訓練圖後才能進行 Soul 訓練。`show_characters(action='train')` 本輪**未**呼叫，`profile.json` 完全未修改。**

### 1. 錨定圖挑選

使用 Read 工具實際開圖檢視全部 4 張候選圖（`candidate_01.png`～`candidate_04.png`）後，選定 **`candidate_02.png`**（正面·半身）作為身分錨定圖，理由：
- 正面直視鏡頭、五官左右對稱、無 3/4 側臉角度造成的比例失真（`candidate_03` 為側臉角度）
- 無明顯動態模糊（`candidate_01` 手部靠近臉部有動態模糊、且景別較緊，部分臉部被陰影遮擋）
- 無俯角造成的臉部透視畸變（`candidate_04` 為由上往下的坐姿全身角度，下巴/嘴部比例因俯角而放大）
- 光線均勻、雙眼與挑染細節清晰可辨，是 4 張中最乾淨、最具代表性的臉部特寫

### 2. Reference Element 建立

- 上傳流程：`media_upload`（filename `mia_huang_anchor_candidate_02.png`）→ 取得 presigned S3 URL 與 `media_id: c059ba58-79d0-4cc6-a585-69f019625585` → `curl -X PUT` 上傳 `candidate_02.png` 原始檔案位元組（HTTP 200）→ `media_confirm(media_id, type='image')` 確認上傳完成（status: uploaded）
- `show_reference_elements(action='create', category='character', name='mia-huang-anchor', medias=[{id, url}])` 建立成功
- **Element ID：`92ffbd80-32c7-495f-91ed-f109b419bb41`**（name: `mia-huang-anchor`）

### 3. 模型選擇與費用

- 沿用 Vicky Lin 第四輪已驗證的做法：Element 內嵌僅支援 `nano_banana_2`、`nano_banana_flash`、`gpt_image_2`、`seedream_v4_5`、`seedream_v5_lite`、`cinematic_studio_2_5`（`soul_2` 不支援）；採用 **`seedream_v4_5`**，`aspect_ratio: 9:16`，`quality: basic`
- `get_cost: true` 預檢（完整 prompt 文字）回傳每張 **1 credit**
- 生成過程中多次遇到 `429 rate_limit_reached`（同時併發送出多張請求時），改為逐張序列送出（每張間隔數秒~數十秒、必要時用 `job_display` 查詢前一張狀態順便讓速率限制冷卻）後全部 13 張成功送出且完成
- 帳號餘額：生成前 **2766.7 credits**，生成後 **2722.7 credits**（共下降 44 credits）；比對 `transactions` 交易紀錄，同一時段（09:51–09:56 UTC）內的 `Seedream 4.5 -1 credit` 扣款筆數明顯超過本次任務的 13 張，代表這段時間帳號內有其他並行工作同時在跑（比照 Mia 稍早候選圖批次與 Vicky Lin 案例中都出現過的「共用帳號並行任務」現象）。**本次任務本身依 `get_cost` 預檢與 13 次成功生成，可歸屬成本為 13 credits（每張 1 credit × 13 張）**，餘額總降幅不能全部算在本次任務頭上

### 4. 產出檔案（`kols/mia-huang/images/training_v1/`，比照 Iris Chen `training_v1/` 目錄與編號慣例）

全部 13 張使用 `<<<92ffbd80-32c7-495f-91ed-f109b419bb41>>>` 錨定同一身分，僅變化場景、姿勢、服裝、光線、視角（自拍／候拍）：

| 檔名 | 內容支柱 | 視角 | 風格變體 | Job ID |
|------|---------|------|---------|--------|
| 01_gaming_chair_candid.png | 居家/直播間 (30%) | 候拍（固定 webcam） | 標準 HD | `def757c2-df0a-40a2-b8b2-80cbd223efb8` |
| 02_gaming_chair_selfie.png | 居家/直播間 | 自拍（前鏡頭） | 前鏡頭較軟焦 | `08a23903-3a29-44a0-943a-bbc258e66b64` |
| 03_cosplay_mirror_selfie.png | 穿搭/換裝 (20%) | 自拍（鏡前） | 前鏡頭較軟焦 | `478840a8-369d-467f-8b89-3eb5876399f4` |
| 04_outfit_decision_selfie.png | 穿搭/換裝 | 自拍（衣櫃前） | 前鏡頭較軟焦 | `445c1c62-9337-43f8-8c75-bdca56b2fcf8` |
| 05_cosplay_candid_doorway.png | 穿搭/換裝 | 候拍（他拍視角） | 標準 HD | `ab73ef8e-6608-4c3d-bb10-327586fd83cb` |
| 06_stream_reaction_webcam.png | 居家/直播間 | 候拍（固定 webcam） | 標準 HD | `017f4501-ef84-4933-a72a-c1fbfe46f02d` |
| 07_stream_break_selfie.png | 居家/直播間 | 自拍（前鏡頭） | 前鏡頭較軟焦 | `1feead0b-9bfb-452b-9d11-49234cdbcea6` |
| 08_afternoon_wakeup_selfie_ccd.png | 下午甦醒 (20%) | 自拍 | **CCD 數位相機質感** | `392bdc67-2dd4-49f1-89e6-b3df331528ec` |
| 09_afternoon_wakeup_candid_couch.png | 下午甦醒 | 候拍（他拍視角） | 標準 HD | `fc37d6a6-4ad2-4f22-8b26-2e04dcab90be` |
| 10_skincare_bathroom_selfie.png | 浴室/深夜保養 (10%) | 自拍（鏡前） | 前鏡頭較軟焦 | `bbf83143-c8b7-4507-932e-8244ad385d1d` |
| 11_hotel_expo_selfie_meitu.png | 飯店/展會旅遊 (10%) | 自拍 | **美圖濾鏡質感** | `19225714-5aaf-4cbf-b011-d5d4386f890e` |
| 12_daytime_outing_candid_cafe.png | 面基日（生活主題加碼） | 候拍（朋友幫拍） | 標準 HD、自然日光 | `f48c6a16-d550-4613-b41a-d0e166581c84` |
| 13_stretch_break_candid.png | 健身/伸展 (10%) | 候拍（手機立在桌上） | 標準 HD | `69c8d0b0-51a9-4a17-ad60-7a77ceee8051` |

**視角比例**：自拍 7 張（02, 03, 04, 07, 08, 10, 11）／候拍 6 張（01, 05, 06, 09, 12, 13），符合 `SEXY_SCENE_LIBRARY.md` 第 7 點「自拍與他拍比例」要求，不偏廢單一視角。

**內容支柱比例（13 張近似對應權重）**：居家/直播間 4 張（31%，目標 30%）、穿搭/換裝 3 張（23%，目標 20%）、下午甦醒 2 張（15%，目標 20%，略低）、浴室/深夜保養 1 張（8%，目標 10%）、飯店/展會旅遊 1 張（8%，目標 10%）、健身/伸展 1 張（8%，目標 10%）、面基日（生活主題加碼，不占既定支柱比例）1 張。整體大致依權重分佈，未來若擴充下一輪訓練圖可優先補足下午甦醒支柱的張數。

**風格變體**：依 `SEXY_SCENE_LIBRARY.md` 2b「相機/濾鏡風格變化」新規則，本輪納入 2 張變體（各 1 張，符合「至少 1–2 張」要求）：
- `08_afternoon_wakeup_selfie_ccd.png`：CCD 數位相機懷舊質感，搭配「剛睡醒、手持復古隨身數位相機自拍」的场景，符合 Mia 電競/直播主人設中偶爾走 Y2K 復古周邊/收藏風格的調性
- `11_hotel_expo_selfie_meitu.png`：美圖/美顏類 App 濾鏡質感，搭配「展會後在飯店床上發 IG 限動」的場景——這類濾鏡在華語圈電競/實況圈社群自拍中很常見，符合她「電競少女」人設，屬於刻意選用的加分風格變化而非預設套用

**自拍畫質規則**：依 `SEXY_SCENE_LIBRARY.md` 第 2 點 2026-07-30 新增規則，7 張自拍（02, 03, 04, 07, 08, 10, 11）全部使用 `front camera quality, slightly softer focus than a rear camera shot, mild natural grain, slightly lower dynamic range, gentle noise in low light, NOT ultra-crisp or overly HD` 或對應的 CCD/美圖濾鏡語言，**取代**候拍鏡頭慣用的 `crisp high-quality photography ... sharp focus on subject` 結尾；候拍/webcam 視角（01, 05, 06, 09, 12, 13）維持原本的 crisp/HD 結尾語氣。

### 5. 生成後目視檢查與誠實評估

已用 Read 工具實際開圖檢視 8 張跨支柱/跨視角樣本（`01`、`03`、`05`、`08`、`09`、`10`、`11`、`12`），比對錨定圖 `candidate_02.png`：

- **(a) 身分是否與錨定圖一致**：核心可辨識特徵——圓潤娃娃臉、大眼、灰棕髮色配臉側粉色挑染、上揚眼線妝感、水潤唇色——在全部 8 張樣本中都清楚可辨，與錨定圖是同一個人，比核准前「4 張各自獨立生成、彼此是不同人」的候選圖批次有本質上的進步，Reference Element 機制確實有效。**但誠實地說，並非像素級的同一張臉**：`03_cosplay_mirror_selfie`、`05_cosplay_candid_doorway` 這兩張的髮型呈現略短的鮑伯捲髮，比 `01`、`09`、`12` 呈現的及肩長捲髮略短；臉頰雀斑在不同光線/角度下的可見度也有落差（`01`、`08` 雀斑明顯，`03`、`11`、`12` 較不明顯）。這屬於同一身分在不同角度/濾鏡/光線下的正常變異範圍，但不是「逐張零落差」，比照 Vicky Lin 第四輪的誠實評估標準如實記錄。
- **(b) 自拍是否比候拍更柔焦**：明顯成立。自拍樣本（`03`、`08`、`10`、`11`）呈現前鏡頭/CCD/美圖濾鏡各自對應的柔和感（`03` 前鏡頭自然稍軟、`08` CCD 復古顆粒與偏低動態範圍、`11` 美圖濾鏡明顯的柔焦+均勻膚色提亮），候拍樣本（`01`、`05`、`09`、`12`）則維持乾淨銳利的高畫質語氣，兩者對比清楚可辨，未出現「自拍跟候拍一樣銳利」的假感問題。
- **(c) 場景/穿搭是否有實際多樣性**：13 張橫跨電競椅直播間、cosplay-lite 換裝（鏡前試穿、門口全身）、下午甦醒（CCD 自拍、沙發抱貓候拍）、浴室卸妝保養、飯店展會 IG 限動自拍、面基日白天咖啡廳外拍、直播間伸展候拍——確實對應 `content_style.md` 列出的六大內容支柱＋面基日生活主題，服裝也對應變化（黑色連帽外套/短褲、cosplay-lite 貓耳+大腿襪、灰色帽T、深色細肩帶背心、深藍色戰袍帽T、白T恤牛仔短褲），不是單一穿搭重複套用。
- **(d) 膚色是否維持白皙**：8 張樣本膚色都清楚維持白皙透亮的粉色調，沒有出現古銅/小麥/曬黑色調，`fair, luminous porcelain-toned skin` 規則持續生效，符合 `SEXY_SCENE_LIBRARY.md` 第 6 點對台灣籍角色的膚色基調要求。

**總結**：這組訓練圖集在身分一致性、自拍/候拍畫質分層、場景多樣性、膚色基調四項檢查上都達到可用標準，**唯一需要誠實指出的落差是髮型長度/雀斑可見度在少數幾張之間有輕微變異**，如果使用者對這點要求嚴格到「逐張完全一致」，建議先個別重新生成 `03`、`05` 這兩張再送訓練；若可接受同一身分在不同角度/場景下的自然變異範圍（比照 Vicky Lin 已核准訓練集的先例），現有 13 張可視為堪用的訓練素材。

### 6. 未變更項目

`profile.json`、`character.md`、`content_style.md` 均未修改；`README.md`、`KOL_TRAINING_SOP.md` 進度表本輪未觸碰。既有的 `kols/mia-huang/images/face_reference/candidate_01.png`～`candidate_04.png`、`round1_candidate_01.png`～`round1_candidate_04.png` 原封不動保留。

---

## 2026-07-30 Soul 訓練送出（第一次呼叫成功）

**觸發原因**：使用者明確回覆「我覺得這四位都可以送去訓練...就先這樣送出訓練」，核准將 `kols/mia-huang/images/training_v1/` 這 13 張訓練圖送入 Soul 訓練。

**背景風險提醒**：比照 Vicky Lin 的前例（`kols/vicky-lin/generation_notes.md`）——用原始生成 job_id 直接呼叫 `show_characters(action='train')` 曾連續失敗，即使重新上傳取得全新 media_id 後仍跨兩個 session、累計 12 次呼叫全部失敗（工具層級錯誤），且每次都仍被扣款。本次執行前已知有這個風險，因此依照任務指示：全部 13 張圖重新上傳取得全新 media_id、訓練呼叫上限 2 次、每次呼叫後立即查 `transactions` 確認是否被扣款。

### 1. 重新上傳 13 張訓練圖

對 `training_v1/` 目錄下全部 13 個 PNG 檔案，逐一執行 `media_upload`（取得 presigned S3 URL + media_id）→ `curl -X PUT` 上傳原始檔案位元組 → `media_confirm(type='image')` 確認上傳完成。13 次 curl PUT 全部回傳 HTTP 200，13 個 media_id 的 `media_confirm` 全部回傳 `status: "uploaded"`。

| 檔名 | 新 media_id |
|------|-------------|
| 01_gaming_chair_candid.png | `dbd13092-c79d-4474-ad28-427c476f5cff` |
| 02_gaming_chair_selfie.png | `53ae44a9-9f51-4534-81b7-d16a85a70160` |
| 03_cosplay_mirror_selfie.png | `16d27a64-a5f0-4873-8447-c5b3d9cf465d` |
| 04_outfit_decision_selfie.png | `ba0d589b-f736-4567-8953-ffae053fa246` |
| 05_cosplay_candid_doorway.png | `b069ca85-ce0c-4c6f-b985-d8d8f709406d` |
| 06_stream_reaction_webcam.png | `063701f0-7a7a-490c-83aa-ad517cbf8f10` |
| 07_stream_break_selfie.png | `d97362ac-b784-4cb9-b4f8-4797b3f4db1e` |
| 08_afternoon_wakeup_selfie_ccd.png | `b5f59bfc-f022-46b0-811d-2d033886f3ca` |
| 09_afternoon_wakeup_candid_couch.png | `df423e1b-2ab2-4f96-86fc-fca37ce6a407` |
| 10_skincare_bathroom_selfie.png | `e5c6a74d-84b4-44e1-b4e7-d36eb18f8c28` |
| 11_hotel_expo_selfie_meitu.png | `d3bc7c0a-b70d-4945-9cb4-701da8b71c33` |
| 12_daytime_outing_candid_cafe.png | `07f8e886-d0ea-4fa6-9c33-71d3aadcbf60` |
| 13_stretch_break_candid.png | `c694b728-dd42-4184-8225-e768718f025d` |

### 2. `show_characters(action='train')` 呼叫

呼叫 `show_characters(action='train', name='Mia Huang', images=[上表 13 個 media_id])`——**第一次呼叫（1/2 次上限）即成功**，不需要用到第二次備用參數形狀嘗試，回傳：

```json
{"id":"e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4","name":"Mia Huang","type":"soul_2","status":"training","raw_status":"queued", ...}
{"training_id":"e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4","trained":true,"note":"Training started. The widget will refresh until the character is ready."}
```

**Soul ID：`e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4`**

### 3. 費用確認

呼叫後立即查 `transactions`，最新一筆為：
```
{"display_name":"Soul ID","credits":-25,"action":"spend","created_at":"2026-07-30T10:21:50.993178Z"}
```
確認本次訓練呼叫扣款 **25 credits**，與呼叫本身直接對應，沒有出現「扣款但失敗」的情形（Vicky Lin 案例中的核心風險）。

### 4. 伺服器端存在性驗證

分別用 `show_characters(action='status', soul_id='e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4')` 與 `show_characters(action='list', status='training')` 查詢：
- `action='status'`：回傳單一筆 `id`/`soul_id` 均為 `e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4`、`name: "Mia Huang"`、`status: "training"`、`raw_status: "queued"`
- `action='list', status='training'`：回傳列表中包含 Mia Huang（同一個 soul_id）以及 Zoe Lai、Rainie Hsu 等其他角色的真實訓練任務並列——確認這不是孤立的假資料，而是伺服器端真實排隊中的訓練任務

**⚠️ 誠實記錄：截至本次 session 結束為止，多次間隔輪詢（約 10:22–10:25 UTC）`raw_status` 始終維持 `queued`，尚未變成 `ready`**。`show_characters` 工具說明本身也指出訓練「約需 10 分鐘，non-blocking」，本次 session 的輪詢間隔未必涵蓋完整 10 分鐘等待窗口。**下一個 session 應優先執行**：`show_characters(action='status', soul_id='e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4')`，若 `raw_status` 已變成 `completed`/`status` 變成 `ready`，才可將 `profile.json`、`README.md`、`KOL_TRAINING_SOP.md` 的訓練狀態從「training」更新為「ready / 完成」，並開始用 `generate_image(model='soul_2', soul_id=...)` 實際生成內容。

### 5. 未變更項目

`character.md`、`content_style.md` 本輪未修改。`kols/mia-huang/images/training_v1/` 13 張圖檔案本身未變動（僅重新上傳取得新 media_id 用於本次訓練呼叫，圖檔內容不變）。本輪未執行任何 `git add`/`commit`/`push`。

---

## ⚠️ 下一步（不可跳過，待下個 session 執行）

1. **優先事項**：呼叫 `show_characters(action='status', soul_id='e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4')` 確認訓練是否已完成（`status` 變成 `ready`）
2. 若已 `ready`：更新 `profile.json` 的 `ai_assets.training_images_v1.soul_training.status` 為 `ready` 並填入 `completed_at`；`README.md`「KOL 陣容」表格 Mia Huang 列的 Soul ID 改為實際 ID（移除訓練中註記）；`KOL_TRAINING_SOP.md` 進度表同步更新為 ✅
3. 若仍在 `training`/`queued`：不需要重新呼叫 `show_characters(action='train')`（已成功送出、正在背景處理中，重複呼叫只會像 Vicky Lin 案例一樣徒增風險與費用），單純再等待、再查詢狀態即可
4. Soul 訓練確認 `ready` 後，才開始用 `generate_image(model='soul_2', soul_id='e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4')` 生成後續大量生活照與影片素材

**本次任務執行到此為止：Soul 訓練呼叫已成功送出且驗證為伺服器端真實任務，但尚未確認完成（ready）。**

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
| Soul ID | `e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4` |
| 場景 | 購物中心（扭蛋機前蹲姿／手扶梯自拍） |
| 穿搭（A/B 共用） | 寬鬆黑色電競帽 T（含小型隊徽刺繡）+ 黑色短褲 + 黑色過膝襪 + 厚底白球鞋 + 推到頭頂的透明藍光眼鏡 |
| Job ID（A） | `507a609d-45e5-44e9-bdcf-f64f63282c38` |
| Job ID（B） | `1681177a-aa34-4954-a377-a2addd6f7829` |
| 評定 | ✅ 通過 |

粉色挑染位置、眼妝風格、過膝襪等辨識特徵全部一致。B 張刻意指定「前鏡頭畫質」（較柔焦、輕微顆粒、較低動態範圍，且不寫 ultra-crisp），成功做出與 A 張後鏡頭的質感差異——**這個自拍／他拍的裝置差異寫法有效，值得推廣到其他角色**。背景路人 4 人以上正常。**落差**：扭蛋機內容物生成為食物狀物件而非扭蛋、她手上拿的是扁平包裝而非扭蛋殼；髮色偏鉑金而非設定的灰棕。

### 本批次共同結論（全 7 位角色適用）

- ✅ **背景路人：14/14 全部成功，且無任何配角撞臉主角。** 四條件措辭（背向／不看鏡頭／失焦／外型與主角區隔）有效，成本為零。原「預設只有本人入鏡」規則對公共場景已反轉。
- ✅ **同穿搭一日敘事：7/7 成功。** 服裝配件完整延續且狀態自然演變。
- ⚠️ **地點：環境元素清單成功，點名地標全部失敗。** 「愛河」生出墨爾本天際線、「台北 101」生出通用摩天樓群。
- ⚠️ **中文招牌全部亂碼**（與競品同等程度），本批次接受此取捨。
- 🔴 **打光尚未套用新公式。** 本批次仍使用舊的「品質形容詞」寫法（`crisp`／`high dynamic range`／`well-exposed`）。2026-08-05 拆解競品後已改寫 `SEXY_SCENE_LIBRARY.md` 第 3 點為五段式物理光線公式，**下一批次應以驗證該公式為首要目標**。

---

## 2026-08-07 R1 舞蹈影片 — 動作驅動複製法（Method B，見 `DANCE_CLONE_SOP.md`）

**狀態：✅ 已完成，內部驗證用。對外發佈前需先完成 Step 7 授權檢查。**

**觸發背景**：舞蹈批次分配（見 `DANCE_CLONE_SOP.md` 大量選片 SOP）原本把 `DPWE2eqEVJ-`（水手服天台手勢舞）誤標給 Luna Tanaka，經逐一重新下載核對後發現連結與描述被寫反，已於 `kols/luna-tanaka/generation_notes.md` 2026-08-06 章節更正——`DPWE2eqEVJ-` 正確應分配給 Mia Huang（GitHub Issue #3 已同步更新）。

### Step 1–2：下載與裁剪

- 驅動片：`https://www.instagram.com/reel/DPWE2eqEVJ-/`，`yt-dlp` 下載，576×1024（已是 9:16），30fps、~9.8s，含原始配樂（aac，44.1kHz 立體聲）
- 內容：深藍水手服連身衣+白色水手帽+灰色過膝襪+高跟鞋，戶外樓梯間/天台場景，固定機位無切鏡，走位+張臂+比手勢的活潑舞蹈
- 人物本來就置中、無浮水印，**未做寬度裁切**（跟 Luna 那支不同，這支不需要）

### Step 3：Performance Sheet + Emotion Timeline

呼叫 `performance-director` 與 `emotion-director` agent（依 1s 取樣的文字時間軸描述）。重點結論：

- **情緒設計**：Mia 的人設本來就鼓勵對鏡頭喊話的誇張能量，這次的校準方向跟 Luna 相反——**表情強度可以往上推，但「停留時長」與「對稱性」仍然要克制**。5.0s（雙臂對稱張開）與 6.0s（張嘴唱歌/大笑）這兩個相鄰動作，靠眼神狀態（閉眼淺笑 vs 睜眼大笑）、嘴型（微笑 vs 張嘴）、頭部角度做出區隔，避免面具臉
- **表演設計**：character.md 記載她的髮型是黑棕染髮**放下的長微捲**（非短髮），這是比服裝更好的次級動態載體，Step 4 prompt 必須讓頭髮露在水手帽外面；水手服的領巾要明確寫成「鬆鬆打結、未塞入、垂在胸前」，否則模型可能生成沒有次級動態的死板領口
- **構圖建議**：三分身（mid-thigh up），比 waist-up 寬以保留步伐/髖部重心轉移動作，但比全身窄以維持臉部可讀性
- **場景風險**：她慣用的直播間場景通常桌椅緊貼、雜物多，跟這支舞 2.0s 的走位/甩手動作會有碰撞風險，Step 4 構圖需刻意留一側走位空間，桌椅移到後方/側邊不擋動線；建議這次不要讓貓咪 GG 入鏡（牠沒有對應的動作骨架來源，硬生成會增加 AI 感風險）

### Step 4：起始畫面

- 模型：`soul_2` + `soul_id: e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4`，`aspect_ratio: 9:16`，`quality: 2k`（預設），`count: 1`（依 2026-08-06 更正後的預設，不再生兩張選一張）
- 場景：她的 RGB 直播間（霓虹燈牆、電競椅移到後側、螢幕光暈、公仔架），刻意留出走位空間，不含貓咪
- 穿搭：深藍水手服上衣（明確指定領巾鬆鬆打結垂胸前，未塞入未融合）+ 深藍百褶短裙（模型自行詮釋成裙裝而非連身衣，仍屬 cosplay-lite 類別，可接受）+ 灰色過膝襪+黑色瑪莉珍高跟鞋，水手帽戴得微歪，頭髮放下露在帽子外
- Job ID：`ae6bf363-9b06-43d0-b1d3-04f2314a5fa4`（一次生成，未重新生成）

### Step 5：Motion Control

- 工具：`motion_control`（Kling 3.0 Motion Control）
- **第一、二次呼叫皆失敗**（`status: failed`，無明確錯誤訊息）：`image_id: ae6bf363-9b06-43d0-b1d3-04f2314a5fa4`，`motion_video_id` 為驅動片直接複製未重新編碼的版本
- **排查與修正**：用 `ffprobe` 檢查失敗版驅動片編碼，發現是 **VP9**（Instagram 這次給的格式跟 Luna 那支的 H.264 不同）。Luna 那支因為有裁切步驟被 ffmpeg 強制轉成 H.264 才意外避開這個問題，Mia 這支因為不需要裁切，直接複製原始檔案保留了 VP9 編碼。用 `ffmpeg -c:v libx264 -pix_fmt yuv420p` 重新編碼成 H.264 後**第三次呼叫成功**
- **⚠️ 新規則**：Motion Control 的驅動片輸入**一律要確認/轉成 H.264**，不能假設 yt-dlp 下載下來的檔案編碼一致——不同貼文、不同時間下載，Instagram 給的 dash 串流編碼格式會不一樣，直接複製未裁切的檔案有 VP9 風險。已建議補進 `DANCE_CLONE_SOP.md` Step 2（見下方 SOP 更新）
- 修正後 `image_id`: `ae6bf363-9b06-43d0-b1d3-04f2314a5fa4`，`motion_video_id`: `80384c14-eb0d-4a24-a493-93f9fa7403c1`（H.264 版），`scene_control: image`，`resolution: 1080p`
- 輸出：`1072×1936`、30fps、~9.8s，Job ID `529eeb08-0ba6-490b-bb5b-3c273e68cd18`
- **輸出本身無聲**（與 Luna 那支相同狀況，跟 Coco Wu 案例不同）

### Step 6：手動混音（跟 Luna 那支一樣需要）

用 `ffmpeg -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest` 把 Step 2 抽出的驅動片原始配樂蓋上 Kling 輸出的無聲畫面，輸出 `mia_dance_clone_r1_ig_reel.mp4`（~9.73s，含視訊+音訊雙軌）。

### Step 7：授權與發佈限制檢查

- **驅動動作**：來自第三方 Instagram/TikTok 創作者，本次生成僅供內部方法驗證；若要對外發佈，需評估重現程度是否需要致敬標註或改編到不可辨識
- **配樂**：混音使用的是驅動片原始配樂，**未取得商用授權**，正式發佈前必須替換為已授權/可商用曲庫版本
- **素材存放**：驅動片原始檔（`driver_raw.mp4`、H.264 轉檔版、`driver_audio.m4a`）僅存在本機工作資料夾，未存入本 repo

### Step 8：QA 檢核（已用 Read 工具目視抽幀比對，非假設）

抽樣 0s / 1s / 2s / 3s / 4s / 4.5s / 5s / 5.5s / 6s / 6.5s / 7s / 7.5s / 8s / 8.5s / 9s / 9.5s 共 16 個時間點：

- [x] **身分一致**：全程可清楚辨認粉色挑染的灰棕色波浪長髮、娃娃臉，跟起始畫面的錨定身分一致
- [x] **微表情有變化，通過面具臉檢查**：Emotion Timeline 事前標記 5.0s/6.0s 兩個連續張臂動作的面具臉風險，實際檢視兩幀——5.0s 是閉眼淺笑的「亮相」表情，6.0s 是睜眼張嘴大笑的「釋放」表情，眼神/嘴型/頭部角度都明顯不同，不是同一張臉套兩個手臂角度
- [x] **次級動態確實轉印**：白色領巾在多個抽樣幀呈現擺動/運動模糊（尤其 2s、5s 附近），百褶裙也隨動作擺動——比原規劃預期更好，裙裝意外提供了額外的次級動態載體
- [x] **手部整體無明顯崩壞**：4.0s 雙手扶帽、8.0s 手部動作等 Performance Sheet 標記的中高風險時刻，抽樣檢視皆未發現手指數量/形狀異常
- [x] **場景碰撞風險——實際檢視後判定沒有出問題**：2.0s 走位甩手動作全程沒有觀察到穿模/卡進桌椅的畫面，Step 4 刻意留出的走位空間有效
- [x] **背景穩定**：RGB 直播間場景（霓虹燈牆、電競椅、螢幕光暈、公仔架）全程一致，無鬼影閃爍
- [ ] **無確認的定格/freeze 點**：跟 Luna 那支一樣，這次沒有針對驅動片本身逐幀確認是否有 ≥8 幀的定格點，留待下次需要更嚴謹驗證時補做

**結論**：Performance Sheet 事前標記的「條件式阻斷」風險（次級動態載體需明確寫進 prompt）在 Step 4 有落實，效果良好；Motion Control 前兩次失敗的根本原因（VP9 編碼）已找到並修正，是這次流程中唯一真正的阻斷級問題，且是技術性的（非人設/構圖問題）。

### 產出檔案

`kols/mia-huang/images/dance_clone_r1/start_frame.png`（起始畫面）、
`kols/mia-huang/videos/dance_clone_r1/mia_dance_clone_r1_ig_reel.mp4`（1072×1936、30fps、~9.7s，含驅動片原始配樂音軌，未經授權，僅供內部驗證）

### ⚠️ SOP 更新建議（待補進 `DANCE_CLONE_SOP.md`）

Step 2（裁剪驅動片）應新增一條：**不論是否需要裁切畫面，都要用 `ffprobe` 確認驅動片編碼是否為 H.264；不是的話一律用 `ffmpeg -c:v libx264 -pix_fmt yuv420p` 重新編碼**，不能因為「這支不需要裁切」就跳過編碼正規化這一步，否則 Motion Control 可能會無明確錯誤訊息地反覆失敗。
