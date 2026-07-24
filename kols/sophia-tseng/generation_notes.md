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
| 身材 | Slim-hourglass：身形修長，腰臀曲線分明但含蓄不誇張，肩頸線條優雅，站姿坐姿永遠挺直 | — |
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
- **理由**：Sophia 的美學是「成熟、精緻、克制」，需要模型在光線與皮膚質感上表現乾淨、低對比，避免過度銳化或棚拍感

### 批次規劃（提案）

- 提案共 6 個批次，對應六個核心場景（見下方「計畫批次 Prompt 規劃」），涵蓋人物設定中六大內容支柱（早晨／穿搭／浴室／居家／飯店旅遊／健身）
- 每批次提案生成 2 張（同場景多張差異有限，不需要 4 張）
- **總計畫張數：待實測後決定，此處不預設具體數字**
- 每個批次的 prompt 均依 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五點檢查清單撰寫（皮膚質感／拍攝裝置感／混合不均勻光源／背景生活雜物／完整明確服裝），詳見下方各批次 prompt

### 待辦事項

1. 依下方核心 prompt 結構與批次規劃，於 Higgsfield 進行首批測試生成
2. 確認臉型、身材比例、氣質是否符合設定，必要時調整 prompt 用詞
3. 挑選訓練圖，送入 Soul 訓練流程
4. 訓練完成後，將真實 Soul ID、訓練圖路徑、生成日期回填本檔案

---

## 核心 Prompt 結構

> 以下為可重複使用的基礎描述，維持五官、身材比例、氣質的一致性；場景、服裝、拍攝裝置、光源、背景雜物依批次變化，依 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五點檢查清單撰寫。全部為純物理／氣質描述詞，**不引用任何真實名人姓名或臉型**。

```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek straight or softly waved dark hair with a polished salon finish, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [DEVICE/CAMERA SPEC], [LIGHTING RECIPE], [BACKGROUND CLUTTER DETAIL], clean low-contrast warm ivory color grade, quiet luxury editorial photo, minimal film grain, Instagram style
```

**用詞備註**：
- 刻意避免 iris-chen 系列常用的 `candid casual`／重顆粒 `film grain` 語感——Sophia 的美學是「乾淨、精緻、克制」，不是隨手感，但「乾淨」指的是**色調與構圖**，不是光源本身——實際光線仍須依檢查清單寫成混合、不均勻的真實光源，避免棚拍三點打光感
- `poised`、`composed`、`quiet self-assured` 等詞用來維持她「不費力」的氣質，避免生成出誇張表情或用力擺拍
- 五官與身材描述詞需在每個批次中保持一致，場景、服裝、裝置、光源、背景雜物部分才做變化
- 皮膚質感一律使用 `visible pores`、`natural texture`、`unretouched`、`natural imperfections` 等詞，**避免** `flawless`、`smooth`、`glossy skin`、`airbrushed`、`porcelain skin`（會推向塑膠感）
- 每個批次必須具體指定拍攝裝置與鏡頭（前鏡頭自拍 / 後鏡頭 / 腳架），不留給模型自己猜

---

## 計畫批次 Prompt 規劃（規劃中，尚未生成）

> 以下 6 個批次涵蓋人物設定中六大內容支柱（早晨／穿搭／浴室／居家／飯店旅遊／健身）。每個批次的 prompt 為草稿，均依 `SEXY_SCENE_LIBRARY.md` 的降低「AI 感」五點檢查清單撰寫（皮膚質感關鍵字／具體裝置與鏡頭破綻／混合不均勻光源配方／具體生活雜物背景／完整明確服裝），正式生成前可能需要微調用詞。**狀態一律為「規劃中」，尚無任何實際輸出。**

### 批次 1 — 設計師公寓早晨（規劃中）

**場景描述**：信義區高樓層公寓，落地窗晨光灑入客廳或臥室，她剛醒，穿著絲質睡袍，手捧咖啡杯，望向窗外城市天際線。強調「安靜的富裕感」，不是刻意擺拍的晨間 routine。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair with a polished salon finish, standing by floor-to-ceiling window in a high-floor Taipei Xinyi apartment, city skyline visible through the window in soft morning haze, wearing an ivory silk robe with a shawl collar loosely tied at the waist, one shoulder line slightly exposed, hem falling just above the knee, holding a ceramic coffee cup with both hands, gazing calmly out the window not at camera, shot on iPhone 15 Pro back camera, slight autofocus softness on the city skyline in the background, natural highlight clipping where morning sun hits the window glass, subtle motion blur on the hand holding the coffee cup, faint JPEG compression artifacts along the window frame's high-contrast edge, mixed color temperature — cool blue morning daylight through the window blending with a warm ambient lamp left on from the night before, uneven light falloff across the room, soft but visible shadow edge along her jawline, faint lens flare where the sun catches the window glass, a phone charging cable coiled loosely on the floor near the window ledge, yesterday's water glass half-full on the console table, a cashmere throw left slightly rumpled on the reading chair, her phone lying face-down on the kitchen island in the background, clean low-contrast warm ivory color grade, quiet luxury editorial photo, minimal film grain, Instagram style
```

---

### 批次 2 — 絲質洋裝鏡前換裝（規劃中）

**場景描述**：全身鏡前，試穿設計師絲質洋裝，調整肩帶或衣領，頭微側評估合身度與剪裁，動作是評估而非展示。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek softly waved dark hair with a polished salon finish, standing in front of a full-length mirror in a minimalist bedroom, wearing a champagne-beige silk slip dress with adjustable thin straps, a soft cowl neckline, bias-cut skirt falling mid-calf, adjusting the shoulder strap while assessing her reflection, head slightly tilted, calm evaluating expression not performing for camera, shot on iPhone 15 Pro back camera on a tripod framing a candid mirror moment, slight autofocus softness on the mirror frame and edges of the reflection, natural highlight clipping where daylight reflects off the mirror glass, subtle motion blur on her fingers adjusting the strap, faint JPEG compression artifacts at the mirror's high-contrast edge, mixed color temperature — cool window daylight blending with a warm vanity lamp beside the mirror, uneven light falloff across the room, soft visible shadow under her jaw, slight glare on the mirror glass, an open walk-in closet rail visible at the edge of frame with a few empty hangers, a pair of heels kicked off near the mirror, a phone and half-finished cup of coffee left on the dresser, a garment bag draped over a chair in the background, full body 3/4 angle mirror shot, clean low-contrast warm ivory color grade, quiet luxury editorial photo, minimal film grain, Instagram style
```

---

### 批次 3 — 五星飯店套房（規劃中）

**場景描述**：剛 check-in 的飯店套房，行李尚未完全打開，坐在大床邊，落地窗外是城市天際線，情緒是從容抵達而非興奮打卡。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair with a polished salon finish, sitting on the edge of a five-star hotel bed with slightly rumpled crisp white linens, floor-to-ceiling window with sheer curtains showing a city skyline behind her, an open suitcase with clothes half-unpacked at the foot of the bed, wearing a tailored travel dress in charcoal wool-crepe, fitted through the waist, cap sleeves, hem at the knee, calm composed expression looking toward the window not at camera, shot on iPhone 15 Pro back camera, autofocus softness on the sheer curtains and skyline in the background, natural highlight clipping on the window's daylight, subtle motion blur on a strand of hair moved by the air conditioning breeze, faint JPEG compression artifacts along the window frame's high-contrast edge, mixed color temperature — warm amber hotel lamp light mixing with cool daylight through the sheer curtains, uneven light falloff across the bed linens, soft visible shadow beneath the luggage, slight glare on the glass water carafe on the nightstand, a room-service tray with a half-eaten pastry and coffee cup on the side table, a luggage tag still attached to the suitcase handle, slippers placed unevenly by the bed, a phone charging cable draped over the nightstand, medium shot from the side, clean low-contrast warm ivory color grade, quiet luxury editorial photo, minimal film grain, Instagram style
```

---

### 批次 4 — 大理石浴室保養儀式（規劃中）

**場景描述**：大理石浴室台面前，專注地進行保養步驟，動作精確不匆忙，不看鏡頭，光線乾淨冷靜。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair pulled back neatly, standing at a marble bathroom vanity, wearing an ivory silk robe with a notched shawl collar, loosely tied at the waist, sleeves pushed up to the forearm, applying skincare product to her face with precise unhurried movements, focused on her own reflection in the mirror not on camera, shot on iPhone 15 Pro front camera propped against the vanity mirror, autofocus softness on the marble reflections in the background, natural highlight clipping from the vanity light bulbs around the mirror, subtle motion blur on her fingertips applying the product, faint JPEG compression artifacts at the mirror's high-contrast edge, mixed color temperature — cool daylight from a small bathroom window blending with the warm vanity bulb lights around the mirror, uneven light falloff across the marble countertop, soft visible shadow under her chin, slight glare reflecting off the marble surface and glass skincare bottles, a row of half-used skincare bottles and jars with faint fingerprint smudges on the counter, a damp hand towel draped over the faucet, a stray hair tie left on the counter, the mirror edge slightly fogged from earlier shower steam, medium close-up mirror shot, clean low-contrast warm ivory color grade, quiet luxury editorial photo, minimal film grain, Instagram style
```

---

### 批次 5 — 居家信義區公寓夜晚（規劃中）

**場景描述**：沙發上，喀什米爾家居服，手裡一杯紅酒，望向落地窗外信義區城市夜景。安靜的一個人的夜晚，姿態放鬆但依然挺直，不是刻意擺拍的放鬆時刻。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek straight or softly waved dark hair with a polished salon finish, sitting on a sofa in a Taipei Xinyi apartment living room at night, floor-to-ceiling window behind her showing the city skyline lit up in the dark, wearing an oversized cashmere cardigan in deep charcoal over a silk camisole, wide-leg cashmere lounge pants, bare feet tucked beneath her, holding a wine glass loosely by the stem, gazing toward the window at the city lights not at camera, shot on iPhone 15 Pro back camera in low ambient light, autofocus softness on the city night lights bokeh through the window, natural highlight clipping on the distant building lights, subtle motion blur on the wine glass as she tilts it slightly, faint high-ISO noise and compression artifacts in the darker shadow areas of the room, mixed color temperature — warm lamp light from a reading lamp beside the sofa blending with cool blue city light through the window at night, uneven light falloff leaving parts of the room in soft shadow, slight lens flare from the distant building lights reflected in the window glass, a cashmere throw blanket bunched at the end of the sofa, an open book placed face-down on the coffee table, a half-empty wine bottle with the cork resting beside it, her phone screen dimly lit on the side table, a candle burned down partway on the console, medium wide shot, clean low-contrast warm ivory color grade, quiet luxury editorial photo, minimal film grain, Instagram style
```

---

### 批次 6 — Pilates／Reformer 訓練室（規劃中）

**場景描述**：私人 Pilates 工作室，reformer 訓練中的專注瞬間，安靜的自律，不看鏡頭，線條乾淨。強調姿態與線條的維持，不是揮汗如雨的強度展示，符合她「不費力」的整體氣質。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, naturally luminous skin with visible pores and subtle natural texture, faint natural sweat sheen on collarbone and temples, unretouched skin detail, natural skin imperfections, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek dark hair pulled back in a low bun with a few loose flyaways, on a reformer machine in a private Pilates studio, mirror wall and large studio windows in the background, wearing fitted high-waist charcoal leggings and a fitted seamless sports bra in an ivory-champagne tone, mid-movement in a controlled reformer exercise, focused expression not looking at camera, shot on iPhone 15 Pro back camera positioned on a tripod across the studio, autofocus softness on the reformer's springs and straps in the foreground, natural highlight clipping where the studio's large window light hits the mirror wall, subtle motion blur on her extended leg mid-movement, faint JPEG compression artifacts along the high-contrast mirror wall edge, mixed color temperature — bright cool daylight flooding through the studio's large windows blending with the warm tone of the wood flooring reflecting light upward, uneven light falloff toward the back of the studio, soft visible shadow cast by the reformer frame, a rolled yoga mat leaning imperfectly against the mirror wall, a water bottle with condensation beads on the floor beside the reformer, a folded towel with slight wrinkles on the bench, her phone and a spare hair tie left on the windowsill, medium wide shot, clean low-contrast warm ivory color grade, quiet luxury editorial photo, minimal film grain, Instagram style
```

---

## 下一步

1. 正式生成前，先用批次 1（設計師公寓早晨）做小規模測試，確認模型輸出的臉型與氣質是否符合「人物設定」表格
2. 測試通過後依序完成批次 2–6
3. 挑選訓練圖，進入 Soul 訓練（`status: PENDING`）
4. Soul 訓練完成後，回填真實 Soul ID、訓練圖路徑（如 `kols/sophia-tseng/images/training_v1/`）與實際生成日期，並將本檔案的規劃內容更新為正式紀錄
