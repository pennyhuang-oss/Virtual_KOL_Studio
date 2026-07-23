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

**基礎 prompt 模板**（所有批次共用，只替換 `[SCENE]` / `[OUTFIT]` / `[POSE/ANGLE]` / `[LIGHTING]`）：

```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, petite figure with soft curves, ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], RGB ambient glow, cool neon purple and cotton-candy pink color accents, film grain, candid lifestyle photo, shot on 35mm, streaming-room aesthetic
```

**一致性重點**：
- 臉型、眼妝風格、粉色挑染的位置與髮色必須每批次保持一致
- 場景與服裝細節可以自由變化（這是她的內容多樣性來源）
- 光線幾乎不用純自然光——RGB 燈光與螢幕藍光是她的招牌，即使是「下午甦醒」場景也應帶一點桌燈或待機螢幕的冷光，而非單純溫暖晨光

---

## 計畫批次 Prompt 規劃（尚未執行）

> 以下四個批次為建議拍攝方向，涵蓋她最核心的視覺場景。每批次建議先生成 2 張測試臉部與場景一致性，確認可用後再決定是否擴充張數。**目前皆未執行、無 job ID、無實際生成圖。**

### 批次 1（計畫）— 電競椅設定照（建立基礎一致性）

**場景說明**：她的直播間主場景——坐在電競椅上，RGB 燈條在背景，桌上有耳機和飲料，這是後續大部分素材的核心背景設定，優先用來確認臉部與場景風格的一致性。

**草稿 Prompt**：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, petite figure with soft curves, ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, sitting in gaming chair in home streaming room, wearing oversized gaming-brand hoodie and shorts, relaxed 3/4 angle looking toward camera, RGB LED light strips glowing purple and pink behind her, screen glow reflecting softly on face, film grain, candid lifestyle photo, shot on 35mm, streaming-room aesthetic
```

---

### 批次 2（計畫）— Cosplay-lite 換裝近景

**場景說明**：鏡前試穿今晚戰袍的近景，貓耳頭飾 + 削肩背心的 cosplay-lite 組合，用來確認她「換裝」支柱的服裝與構圖風格。

**草稿 Prompt**：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, petite figure with soft curves, ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, standing in front of full-length mirror in bedroom, wearing off-shoulder crop top with cat-ear headband accessory and thigh-high socks, cosplay-lite styling, close-up upper body mirror shot, head slightly tilted assessing the outfit, warm bedroom lamp light mixed with faint RGB spill from adjacent room, film grain, candid lifestyle photo, shot on 35mm, streaming-room aesthetic
```

---

### 批次 3（計畫）— 深夜直播桌前場景（反應臉素材）

**場景說明**：直播中的近景反應臉，直視鏡頭、像在跟彈幕講話，是她最具代表性、互動感最強的內容類型，用來確認近距離表情捕捉的效果。

**草稿 Prompt**：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, petite figure with soft curves, ash-brown hair with loose waves and a pastel-pink money-piece highlight framing one side of her face, sitting at streaming desk wearing gaming headset, wearing cropped tank top, exaggerated playful reaction expression looking directly at camera as if talking to chat, close-up face-to-chest crop, cool blue monitor glow mixed with pink RGB light on face, late-night streaming atmosphere, film grain, candid lifestyle photo, shot on 35mm, streaming-room aesthetic
```

---

### 批次 4（計畫）— 寬鬆帽T居家隨性照（下午甦醒版本）

**場景說明**：她的「早晨」——下午剛醒，帽T連著頭髮亂翹，沒有進入主播模式的最沒防備狀態，用來確認離線、卸下表演感時的視覺風格。

**草稿 Prompt**：
```
22-year-old Taiwanese girl, soft round youthful face with approachable features, large expressive eyes with soft anime-inspired eye makeup and subtle winged liner, glossy tinted lips, rounded soft blush, petite figure with soft curves, ash-brown hair loosely disheveled from sleep with pastel-pink money-piece highlight visible, slumped at streaming desk just woken up wearing oversized hoodie with hood up, half-lidded sleepy expression, dim afternoon light mixed with dormant monitor standby glow, messy desk with snack wrappers in soft background blur, film grain, candid lifestyle photo, shot on 35mm, streaming-room aesthetic
```

---

## 下一步（待執行）

1. 選定生成平台與模型（建議先測試 Seedream 4.5，比照 Iris Chen 的模型選擇結論）
2. 依批次 1–4 各生成 2 張測試圖，確認臉部特徵與挑染位置一致性
3. 篩選可用訓練圖，若一致性不足則調整 prompt 措辭後重新生成
4. 確認訓練圖集後，前往 Soul 訓練流程，建立 Mia Huang 專屬 Soul 模型
5. Soul 訓練完成後，才開始用訓練好的角色生成後續大量生活照與影片素材

**目前尚未有任何一步被執行。所有 soul_id、image_media_id、job_id、生成日期欄位均應留待實際生成後才填入，禁止在文件中預先填入未發生的資料。**
