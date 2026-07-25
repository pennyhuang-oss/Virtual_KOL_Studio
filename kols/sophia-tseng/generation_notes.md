# Sophia Tseng — AI 生成規劃（Generation Notes）

> **status: PENDING — 這是規劃文件，不是生產紀錄。** 目前尚未執行任何實際 AI 生成（無訓練圖、無 Soul 訓練、無正式產出影像或影片）。以下 prompt 與批次規劃為「準備開始生成時」的參考草稿，實際執行後請依真實結果更新本檔，並補上真實的 job id / soul id / 生成日期。

---

## 人物設定

| 欄位 | 設定 | 狀態 |
|------|------|------|
| 名字 | Sophia Tseng（曾詩妃） | — |
| 年齡 | 28 歲 | — |
| 國籍 | 台灣 | — |
| 臉型參考 | 成熟精緻鵝蛋臉：眼神沉靜篤定、鼻梁挺直、唇形飽滿帶慵懶弧度、膚況無瑕有光澤。**純粹描述性特徵，不參考任何真實名人臉型或身材。** | — |
| 身材 | Slim-hourglass：168cm，88-58-89cm（D 罩杯），腰臀比約 0.65，腿長 82cm——身形修長，腰臀曲線分明但含蓄不誇張，肩頸線條優雅，站姿坐姿永遠挺直 | — |
| 髮型 | 深色髮絲，俐落直髮或柔和大波浪，永遠像剛從沙龍出來，不顯凌亂 | — |
| 穿衣風格 | Quiet luxury：絲質睡袍、剪裁俐落的西裝外套、設計師洋裝、喀什米爾家居服，色調偏 ivory／香檳米／深炭灰 | — |
| 眼鏡 | 平時不戴；度假或機場造型偶爾配戴太陽眼鏡 | — |
| 氣質關鍵字 | 沉靜、篤定、從容、不費力、有距離的優雅、克制的性感 | — |
| **Soul 訓練** | 尚未開始 | **PENDING** |
| **訓練圖張數** | 0（尚未生成） | **PENDING** |
| **Soul ID** | 無（尚未建立） | **PENDING** |

---

## 訓練圖生成流程規劃（尚未執行）

> 以下沿用工作室既有的生成流程慣例（參考 `iris-chen/generation_notes.md`），實際平台與模型待正式開始生成時確認與記錄。

### 平台與模型（提案，待確認）

- **平台**：Higgsfield.ai（工作室既定平台）
- **模型**：提案沿用 Seedream 4.5（`seedream_v4_5`），因其對亞洲臉孔生成品質穩定；實際是否採用需在首批測試後確認並記錄結果
- **理由**：Sophia 的美學是「成熟、精緻、克制」，需要模型在光線與皮膚質感上表現乾淨、低對比，避免過度銳化或棚拍感——但「克制」指的是色調與構圖，**不是**畫質或光線刻意調差，這點在 2026-07-25 校準後尤其重要（見下方修正記錄）

### 批次規劃（提案）

- 提案共 6 個批次，對應六個核心場景（見下方「計畫批次 Prompt 規劃」），涵蓋人物設定中六大內容支柱（早晨／穿搭／浴室／居家／飯店旅遊／健身）
- 每批次提案生成 2 張（同場景多張差異有限，不需要 4 張）
- **總計畫張數：待實測後決定，此處不預設具體數字**
- 每個批次的 prompt 均依 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五點檢查清單撰寫（皮膚質感／拍攝裝置感／符合場景類型的光源配方／背景生活雜物／完整明確服裝），詳見下方各批次 prompt

### 待辦事項

1. 依下方核心 prompt 結構與批次規劃，於 Higgsfield 進行首批測試生成
2. 確認臉型、身材比例、氣質是否符合設定，必要時調整 prompt 用詞
3. 挑選訓練圖，送入 Soul 訓練流程
4. 訓練完成後，將真實 Soul ID、訓練圖路徑、生成日期回填本檔案

---

## 核心 Prompt 結構

> 以下為可重複使用的基礎描述，維持五官、身材比例、氣質的一致性；場景、服裝、拍攝裝置、光源、背景雜物依批次變化，依 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五點檢查清單撰寫。全部為純物理／氣質描述詞，**不引用任何真實名人姓名或臉型**。

```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture with natural unforced elegant movement (never a stiff standing pose), sleek straight or softly waved dark hair with a polished salon finish, minimal fine jewelry — a single delicate gold ring, a thin bracelet, or a quality watch where scene-appropriate, never stacked or costume-looking, [SCENE], wearing [OUTFIT — tastefully color-coordinated within her ivory / champagne-beige / deep charcoal / muted gold palette], [POSE/ANGLE — natural elegant gesture such as adjusting a cuff, looking out a window, mid-conversation, NOT a stiff standing pose], [DEVICE/CAMERA SPEC], [LIGHTING RECIPE — indoor quiet-luxury recipe or outdoor/work-site recipe, see below], [BACKGROUND CLUTTER DETAIL], crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

**⚠️ 2026-07-25 燈光／身材數字校準**：參照 `vicky-lin/generation_notes.md` 的二次修正經驗與 `SEXY_SCENE_LIBRARY.md` 2026-07-25 針對〈光源〉的修正，對本檔案做了以下校準（詳細改動另見下方「用詞備註」與各批次 prompt）：

1. **身材數字直接寫入**：核心 prompt 與全部 6 個批次的身材描述，從原本「tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve」這類模糊形容詞，改成直接寫入 `profile.json` 的實際三圍數字——168cm、88cm 胸（D 罩杯）、58cm 腰、89cm 臀、腰臀比約 0.65。避免身材跟人物設定對不上的問題（Vicky Lin 就是因為這個問題被使用者明確反饋過）。
2. **臉部／眼睛用詞檢查**：逐一檢查後，本檔案原本的批次 prompt 並未使用 `almond-shaped`、`narrow`、`sharp intense` 這類會被模型解讀成瞇眼/銳利的字眼（`character.md` 在更早一輪已修正過），但為了保險起見，仍在核心 prompt 明確加上 `(rounded and warm, NOT narrow or almond-shaped)` 作為額外防呆，避免未來任何批次不小心加回類似字眼。
3. **光源拆成兩套配方**：Sophia 的內容幾乎全是室內場景（公寓／飯店／浴室大理石／Pilates 個人工作室），過去 6 個批次全部沿用同一套「mixed color temperature、uneven light falloff、natural highlight clipping、faint JPEG compression artifacts、high-ISO noise」語言——這套語言原本是為了模擬「真實但不完美」的室內光源，但套用在 Sophia 身上風險很高：她的品牌核心就是「安靜的奢華感」，畫面必須乾淨、精緻、光線好，一旦被模型解讀成偏暗/偏灰/顆粒感重，就會直接違反她「quiet luxury 是很有質感的」這個定位（`character.md` 明講「不出現的視覺元素」包含「凌亂、沒整理過的場景」與棚拍痕跡，但沒有一句話說她的照片可以看起來畫質差）。校準後拆成兩套配方（詳見下方「用詞備註」）：
   - **室內奢華場景配方**（批次 1–5：公寓早晨／鏡前換裝／飯店套房／大理石浴室／居家夜晚）：保留自然窗光＋暖燈的混合光源邏輯（這是真實室內光的樣子，不是刻意做舊），但移除會讀成「偏暗、偏糊、畫質差」的字眼（拿掉 `uneven light falloff`、`high-ISO noise`，`highlight clipping` 僅保留在窗邊逆光這種合理情境），改用「evenly diffused, elegant well-lit, polished」等字眼明講這是精緻有質感的室內光，不是刻意不完美。
   - **戶外／工作現場配方**（批次 6：Pilates 工作室，大窗自然光＋動態訓練中）：改用 `SEXY_SCENE_LIBRARY.md` 「戶外/生活風格場景」配方——黃金時段或明亮日光＋淺景深背景虛化＋crisp high dynamic range，因為這個場景本身就是大窗日光灌入＋身體在動態訓練中，適合套用討喜自然光邏輯而非室內混合光邏輯。同樣的配方也保留給未來若新增「詹師傅工班現場」「客戶現場勘查」「巷口麵館」「永和爸媽家」等 `content_style.md` / `character.md` 提到但目前尚無批次草稿的生活主題場景使用。
4. **配件明確化**：原本 6 個批次都沒有明講首飾，只在人物設定文字裡籠統帶過「首飾極簡，只一件但是真品」。校準後每個批次都直接寫出該場景該有的具體配件（一枚戒指、一條細手鍊、一支質感手錶，或明講「不戴首飾」），不留給模型自己猜。
5. **服裝配色語言強化**：把「tastefully color-coordinated」的語言更明確地寫進核心 prompt 與各批次，確保同色系（ivory／香檳米／深炭灰／霧金）成套感被模型讀到。
6. **姿態自然度強化**：保留「篤定、從容、不費力」的方向，但每個批次都加強「自然的小動作」描述（調整袖口、望向窗外、手指劃過布料等），明確排除「stiff pose」，避免讀起來像制式站定擺拍。
7. **畫質結尾強化**：結尾統一改成「editorial-magazine-level production quality... NOT degraded, grainy, dim, or moody-dark」，因為 Sophia 的定位是全部 12 位角色裡製作質感最精緻的一位，任何一批次都不該出現偏暗/顆粒感重/做舊濾鏡的結果。

**用詞備註**：
- 刻意避免 iris-chen 系列常用的 `candid casual`／重顆粒 `film grain` 語感——Sophia 的美學是「乾淨、精緻、克制」，不是隨手感，但「乾淨」指的是**色調與構圖**，也包含光線本身——2026-07-25 校準前這裡曾寫「光源仍須依檢查清單寫成混合、不均勻的真實光源」，這個說法已修正：真實光源可以混合（窗光＋燈光），但**不等於**偏暗/偏糊/顆粒感重，見下方兩套光線配方
- `poised`、`composed`、`quiet self-assured` 等詞用來維持她「不費力」的氣質，避免生成出誇張表情或用力擺拍；同時每個批次都應包含至少一個自然的小動作（調整袖口、望向窗外、手指劃過布料、隨手摸貓），避免讀成制式站定擺拍
- 五官與身材描述詞需在每個批次中保持一致（含三圍數字），場景、服裝、裝置、光源、背景雜物、配件部分才做變化
- 皮膚質感一律使用 `visible pores`、`natural texture`、`unretouched`、`natural imperfections` 等詞，**避免** `flawless`、`smooth`、`glossy skin`、`airbrushed`、`porcelain skin`（會推向塑膠感）
- 每個批次必須具體指定拍攝裝置與鏡頭（前鏡頭自拍 / 後鏡頭 / 腳架），不留給模型自己猜
- 配件（首飾／手錶）必須逐場景明講，不能只靠「首飾極簡」這種籠統形容詞帶過

**光線配方一：室內奢華場景**（公寓／飯店／浴室大理石／Pilates 個人工作室等——她大部分的內容）：
```
soft ambient warm light — natural window daylight blending gently with warm lamp glow or marble-reflected light,
evenly diffused and flattering across her face, gentle directional falloff without harsh or heavy shadow,
elegant well-lit interior photography, polished and clear — NOT intentionally dim, imperfect, or grainy;
quiet luxury photography is well-lit and polished, not moody-dark
```

**光線配方二：戶外／工作現場／生活主題場景**（Pilates 工作室大窗日光、未來的詹師傅工班現場、客戶現場勘查、巷口麵館、永和爸媽家等）：
```
golden hour sunlight or bright clear daylight, natural directional light with soft flattering falloff,
shallow depth of field with blurred bokeh background, crisp sharp focus on subject,
high dynamic range, natural color grading — NOT degraded, dim, or muddy
```

---

## 計畫批次 Prompt 規劃（規劃中，尚未生成）

> 以下 6 個批次涵蓋人物設定中六大內容支柱（早晨／穿搭／浴室／居家／飯店旅遊／健身）。每個批次的 prompt 為草稿，均依 `SEXY_SCENE_LIBRARY.md` 的降低「AI 感」五點檢查清單撰寫（皮膚質感關鍵字／具體裝置與鏡頭破綻／符合場景類型的光源配方／具體生活雜物背景／完整明確服裝），正式生成前可能需要微調用詞。**狀態一律為「規劃中」，尚無任何實際輸出。**

### 批次 1 — 設計師公寓早晨（規劃中）

**場景描述**：信義區高樓層公寓，落地窗晨光灑入客廳或臥室，她剛醒，穿著絲質睡袍，手捧咖啡杯，望向窗外城市天際線。強調「安靜的富裕感」，不是刻意擺拍的晨間 routine。光線配方：室內奢華場景。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair with a polished salon finish, wearing a single thin gold bracelet on one wrist and no other jewelry, standing by floor-to-ceiling window in a high-floor Taipei Xinyi apartment, city skyline visible through the window in soft morning haze, wearing an ivory silk robe with a shawl collar loosely tied at the waist, tonal ivory-on-ivory color coordination, one shoulder line slightly exposed, hem falling just above the knee, holding a ceramic coffee cup with both hands, gazing calmly out the window not at camera, natural unhurried body language mid-thought, weight settled gently onto one hip rather than standing stiffly straight, shot on iPhone 15 Pro back camera, slight autofocus softness on the city skyline in the background, subtle natural motion blur on the hand holding the coffee cup, soft ambient warm light — natural window daylight blending gently with the residual warm glow of a lamp left on from the night before, evenly diffused and flattering across her face, gentle directional falloff without harsh shadow, elegant well-lit interior photography, polished and clear, a phone charging cable coiled loosely on the floor near the window ledge, yesterday's water glass half-full on the console table, a cashmere throw left slightly rumpled on the reading chair, her phone lying face-down on the kitchen island in the background, crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

---

### 批次 2 — 絲質洋裝鏡前換裝（規劃中）

**場景描述**：全身鏡前，試穿設計師絲質洋裝，調整肩帶或衣領，頭微側評估合身度與剪裁，動作是評估而非展示。光線配方：室內奢華場景。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek softly waved dark hair with a polished salon finish, wearing a single delicate gold ring, no other jewelry so the outfit itself is the focus, standing in front of a full-length mirror in a minimalist bedroom, wearing a champagne-beige silk slip dress with adjustable thin straps, a soft cowl neckline, bias-cut skirt falling mid-calf, tonal champagne-on-neutral color coordination, adjusting the shoulder strap with a natural unhurried gesture while assessing her reflection, head slightly tilted, weight shifted onto one hip, calm evaluating expression not performing for camera, shot on iPhone 15 Pro back camera on a tripod framing a candid mirror moment, slight autofocus softness on the mirror frame and edges of the reflection, subtle natural motion blur on her fingers adjusting the strap, soft ambient warm light — natural window daylight blending gently with a warm vanity lamp beside the mirror, evenly diffused and flattering, gentle directional falloff without harsh shadow, elegant well-lit interior photography, polished and clear, an open walk-in closet rail visible at the edge of frame with a few empty hangers, a pair of heels kicked off near the mirror, a phone and half-finished cup of coffee left on the dresser, a garment bag draped over a chair in the background, full body 3/4 angle mirror shot, crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

---

### 批次 3 — 五星飯店套房（規劃中）

**場景描述**：剛 check-in 的飯店套房，行李尚未完全打開，坐在大床邊，落地窗外是城市天際線，情緒是從容抵達而非興奮打卡。光線配方：室內奢華場景。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair with a polished salon finish, wearing a slim gold watch and a thin gold necklace tucked beneath her collar, sitting on the edge of a five-star hotel bed with slightly rumpled crisp white linens, floor-to-ceiling window with sheer curtains showing a city skyline behind her, an open suitcase with clothes half-unpacked at the foot of the bed, wearing a tailored travel dress in charcoal wool-crepe, fitted through the waist, cap sleeves, hem at the knee, monochromatic charcoal-on-charcoal tailoring, calm composed expression looking toward the window not at camera, one hand resting lightly on the bed adjusting the cuff of her sleeve, natural unhurried arrival posture rather than a stiff sitting pose, shot on iPhone 15 Pro back camera, slight autofocus softness on the sheer curtains and skyline in the background, subtle natural motion blur on a strand of hair moved by the air conditioning breeze, soft ambient warm light — warm amber hotel lamp light blending gently with cool daylight through the sheer curtains, evenly diffused and flattering across the bed linens, gentle directional falloff without harsh shadow, elegant well-lit interior photography, polished and clear, a room-service tray with a half-eaten pastry and coffee cup on the side table, a luggage tag still attached to the suitcase handle, slippers placed unevenly by the bed, a phone charging cable draped over the nightstand, medium shot from the side, crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

---

### 批次 4 — 大理石浴室保養儀式（規劃中）

**場景描述**：大理石浴室台面前，專注地進行保養步驟，動作精確不匆忙，不看鏡頭，光線乾淨冷靜。光線配方：室內奢華場景。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair pulled back neatly, no jewelry during her skincare routine, standing at a marble bathroom vanity, wearing an ivory silk robe with a notched shawl collar, loosely tied at the waist, sleeves pushed up to the forearm, tonal ivory-on-marble color coordination, applying skincare product to her face with precise unhurried movements, focused on her own reflection in the mirror not on camera, shot on iPhone 15 Pro front camera propped against the vanity mirror, slight autofocus softness on the marble reflections in the background, subtle natural motion blur on her fingertips applying the product, soft ambient warm light — cool daylight from a small bathroom window blending gently with the warm vanity bulb lights around the mirror, evenly diffused and flattering, gentle directional falloff without harsh shadow, elegant well-lit interior photography, polished and clear, a row of half-used skincare bottles and jars neatly arranged with faint fingerprint smudges on the counter, a damp hand towel draped over the faucet, a stray hair tie left on the counter, the mirror edge slightly fogged from earlier shower steam, medium close-up mirror shot, crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

---

### 批次 5 — 居家信義區公寓夜晚（規劃中）

**場景描述**：沙發上，喀什米爾家居服，手裡一杯紅酒，望向落地窗外信義區城市夜景。安靜的一個人的夜晚，姿態放鬆但依然挺直，不是刻意擺拍的放鬆時刻。光線配方：室內奢華場景。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek straight or softly waved dark hair with a polished salon finish, wearing a single thin gold ring, no other jewelry for her evening at home, sitting on a sofa in a Taipei Xinyi apartment living room at night, floor-to-ceiling window behind her showing the city skyline lit up in the dark, wearing an oversized cashmere cardigan in deep charcoal over a silk camisole, wide-leg cashmere lounge pants, monochromatic charcoal-on-charcoal tonal coordination, bare feet tucked beneath her, holding a wine glass loosely by the stem, gazing toward the window at the city lights not at camera, a grey British shorthair cat named Ink resting quietly against the sofa arm beside her, one hand idly resting near the cat, natural unhurried evening posture rather than a stiff pose, shot on iPhone 15 Pro back camera, slight autofocus softness on the city night lights bokeh through the window, subtle natural motion blur on the wine glass as she tilts it slightly, soft ambient warm light — a warm reading lamp beside the sofa blending gently with the cool glow of city lights through the window at night, evenly diffused and flattering, gentle directional falloff without harsh shadow, elegant well-lit interior photography, polished, glowing, and clear even at night, a cashmere throw blanket neatly folded at the end of the sofa, an open book placed face-down on the coffee table, a half-empty wine bottle with the cork resting beside it, her phone screen dimly lit on the side table, a candle burned down partway on the console, medium wide shot, crisp sharp focus, high dynamic range, editorial-magazine-level production quality, clean low-contrast warm ivory color grade, quiet luxury editorial photo — NOT degraded, grainy, dim, or moody-dark, natural true-to-life color and skin tones, Instagram style
```

---

### 批次 6 — Pilates／Reformer 訓練室（規劃中）

**場景描述**：私人 Pilates 工作室，reformer 訓練中的專注瞬間，安靜的自律，不看鏡頭，線條乾淨。強調姿態與線條的維持，不是揮汗如雨的強度展示，符合她「不費力」的整體氣質。光線配方：戶外／工作現場（大窗日光灌入＋動態訓練中，改用討喜自然光邏輯而非室內混合光邏輯）。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, breathtaking elegant mature beauty, calm composed eyes with a quiet self-assured gaze (rounded and warm, NOT narrow or almond-shaped), straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, faint natural sweat sheen on collarbone and temples, unretouched skin detail, natural skin imperfections, 168cm tall slim-hourglass figure, 88cm bust (D cup, full and lifted), 58cm narrow defined waist, 89cm rounded hips, waist-to-hip ratio approximately 0.65, long elegant legs, elongated graceful silhouette, elegant shoulder and neck line, always poised upright posture, sleek dark hair pulled back in a low bun with a few loose flyaways, small gold stud earrings only, no watch or bracelet during training, on a reformer machine in a private Pilates studio, mirror wall and large studio windows in the background, wearing fitted high-waist charcoal leggings and a fitted seamless sports bra in an ivory-champagne tone, tonal charcoal-and-ivory color coordination, mid-movement in a controlled reformer exercise, focused expression not looking at camera, natural fluid motion through the exercise rather than a static held pose, shot on iPhone 15 Pro back camera positioned on a tripod across the studio, slight autofocus softness on the reformer's springs and straps in the foreground, subtle natural motion blur on her extended leg mid-movement, bright daylight flooding through the studio's large windows, natural directional light with soft flattering falloff across her form, shallow depth of field with soft blurred bokeh on the mirror wall and studio background behind her, crisp sharp focus on her form, high dynamic range, natural color grading, a rolled yoga mat leaning against the mirror wall, a water bottle with condensation beads on the floor beside the reformer, a folded towel on the bench, her phone and a spare hair tie left on the windowsill, medium wide shot, editorial-magazine-level production quality, clean low-contrast natural color grade, quiet luxury editorial photo — NOT degraded, dim, grainy, or muddy, natural true-to-life color and skin tones, Instagram style
```

---

## 下一步

1. 正式生成前，先用批次 1（設計師公寓早晨）做小規模測試，確認模型輸出的臉型、身材數字比例與氣質是否符合「人物設定」表格，並確認室內奢華光線配方是否讀出「乾淨精緻」而非「偏暗/顆粒感重」
2. 測試通過後依序完成批次 2–6，批次 6 額外確認戶外/工作現場光線配方（淺景深＋明亮日光）是否與其餘 5 批次的室內奢華配方在同一套 Soul 身分下仍保持一致的臉部與身材識別度
3. 挑選訓練圖，進入 Soul 訓練（`status: PENDING`）
4. Soul 訓練完成後，回填真實 Soul ID、訓練圖路徑（如 `kols/sophia-tseng/images/training_v1/`）與實際生成日期，並將本檔案的規劃內容更新為正式紀錄
5. 若未來新增「詹師傅工班現場」「客戶現場勘查」「巷口麵館」「永和爸媽家」等 `content_style.md` / `character.md` 已提及但尚無批次草稿的生活主題場景，其光線配方應套用本檔案「光線配方二：戶外／工作現場」，而非批次 1–5 的室內奢華配方
