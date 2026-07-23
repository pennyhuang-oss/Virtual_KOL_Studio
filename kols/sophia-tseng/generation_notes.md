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

- 提案共 4 個批次，對應四個核心場景（見下方「計畫批次 Prompt 規劃」）
- 每批次提案生成 2 張（同場景多張差異有限，不需要 4 張）
- **總計畫張數：待實測後決定，此處不預設具體數字**

### 待辦事項

1. 依下方核心 prompt 結構與批次規劃，於 Higgsfield 進行首批測試生成
2. 確認臉型、身材比例、氣質是否符合設定，必要時調整 prompt 用詞
3. 挑選訓練圖，送入 Soul 訓練流程
4. 訓練完成後，將真實 Soul ID、訓練圖路徑、生成日期回填本檔案

---

## 核心 Prompt 結構

> 以下為可重複使用的基礎描述，維持五官、身材比例、氣質的一致性；場景與服裝依批次變化。全部為純物理／氣質描述詞，**不引用任何真實名人姓名或臉型**。

```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, flawless naturally luminous skin, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek straight or softly waved dark hair with a polished salon finish, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], clean low-contrast warm ivory tones, quiet luxury editorial photo, minimal film grain, natural elegant light, Instagram style
```

**用詞備註**：
- 刻意避免 iris-chen 系列常用的 `candid casual`／重顆粒 `film grain` 語感——Sophia 的美學是「乾淨、精緻、克制」，不是隨手感
- `poised`、`composed`、`quiet self-assured` 等詞用來維持她「不費力」的氣質，避免生成出誇張表情或用力擺拍
- 五官與身材描述詞需在每個批次中保持一致，場景與服裝部分才做變化

---

## 計畫批次 Prompt 規劃（規劃中，尚未生成）

> 以下 4 個批次涵蓋內容支柱中權重最高的幾類場景。每個批次的 prompt 為草稿，正式生成前可能需要微調用詞。**狀態一律為「規劃中」，尚無任何實際輸出。**

### 批次 1 — 設計師公寓早晨（規劃中）

**場景描述**：信義區高樓層公寓，落地窗晨光灑入客廳或臥室，她剛醒，穿著絲質睡袍，手捧咖啡杯，望向窗外城市天際線。強調「安靜的富裕感」，不是刻意擺拍的晨間 routine。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, flawless naturally luminous skin, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair with a polished salon finish, standing by floor-to-ceiling window in a high-floor Taipei Xinyi apartment, city skyline visible through the window in soft morning haze, wearing an ivory silk robe loosely tied at the waist, holding a ceramic coffee cup with both hands, gazing calmly out the window not at camera, soft diffused morning sunlight, clean low-contrast warm ivory tones, quiet luxury editorial photo, minimal film grain, Instagram style
```

---

### 批次 2 — 絲質洋裝鏡前換裝（規劃中）

**場景描述**：全身鏡前，試穿設計師絲質洋裝，調整肩帶或衣領，頭微側評估合身度與剪裁，動作是評估而非展示。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, flawless naturally luminous skin, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek softly waved dark hair with a polished salon finish, standing in front of a full-length mirror in a minimalist bedroom, wearing a champagne-beige silk slip dress, adjusting the shoulder strap while assessing her reflection, head slightly tilted, calm evaluating expression not performing for camera, soft natural window light, full body 3/4 angle mirror shot, clean low-contrast warm ivory tones, quiet luxury editorial photo, minimal film grain, Instagram style
```

---

### 批次 3 — 五星飯店套房（規劃中）

**場景描述**：剛 check-in 的飯店套房，行李尚未完全打開，坐在大床邊，落地窗外是城市天際線，情緒是從容抵達而非興奮打卡。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, flawless naturally luminous skin, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair with a polished salon finish, sitting on the edge of a five-star hotel bed with crisp white linens, floor-to-ceiling window showing a city skyline behind her, luggage neatly placed to the side, wearing a tailored travel dress, calm composed expression looking toward the window not at camera, warm ambient hotel room lighting mixed with soft daylight, medium shot from the side, clean low-contrast warm ivory tones, quiet luxury editorial photo, minimal film grain, Instagram style
```

---

### 批次 4 — 大理石浴室保養儀式（規劃中）

**場景描述**：大理石浴室台面前，專注地進行保養步驟，動作精確不匆忙，不看鏡頭，光線乾淨冷靜。

**草稿 Prompt**：
```
28-year-old Taiwanese woman, mature refined oval face, calm composed eyes with a quiet self-assured gaze, straight elegant nose bridge, full lips with a subtle relaxed curve, flawless naturally luminous skin, tall slim-hourglass figure with an elongated silhouette, subtle waist-hip curve, elegant shoulder and neck line, always poised upright posture, sleek straight dark hair pulled back neatly, standing at a marble bathroom vanity, wearing an ivory silk robe loosely tied, applying skincare product to her face with precise unhurried movements, focused on her own reflection in the mirror not on camera, soft cool daylight reflecting off marble surfaces, medium close-up mirror shot, clean low-contrast warm ivory tones, quiet luxury editorial photo, minimal film grain, Instagram style
```

---

## 下一步

1. 正式生成前，先用批次 1（設計師公寓早晨）做小規模測試，確認模型輸出的臉型與氣質是否符合「人物設定」表格
2. 測試通過後依序完成批次 2–4
3. 挑選訓練圖，進入 Soul 訓練（`status: PENDING`）
4. Soul 訓練完成後，回填真實 Soul ID、訓練圖路徑（如 `kols/sophia-tseng/images/training_v1/`）與實際生成日期，並將本檔案的規劃內容更新為正式紀錄
