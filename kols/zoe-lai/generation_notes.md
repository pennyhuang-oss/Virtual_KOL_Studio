# Zoe Lai — AI 生成規劃筆記

> **狀態：PENDING — 尚未執行任何生成**
> 本文件是訓練圖與批次拍攝的**規劃文件**，不是生產紀錄。目前沒有 soul_id、沒有已生成圖片、沒有已生成影片。所有數字、日期、Job ID 待實際執行後才會補上，本檔案不預先捏造。

---

## 人物設定

| 欄位 | 設定 |
|------|------|
| 名字 | Zoe Lai（賴柔伊） |
| 年齡 | 26 歲 |
| 國籍 | 台灣（花蓮出身，衝浪季移動到墾丁） |
| 臉型 | 曬過的橢圓臉、笑容自然大方，直眉，鼻樑和上頰有淡淡雀斑，眼神因常年面對海面反光而有輕微瞇眼、警覺又放鬆。無修飾感，健康、有點風霜的耐看 |
| 身材 | 游泳選手/衝浪者體態——肩背因划水結實，腰腹精瘦有線條，腿部有力，臀部天生曲線，均勻深色年曬肌膚。強壯、實用型身材，不是健身房雕塑出來的樣子 |
| 髮型 | 海浪波浪捲長髮，深棕色髮尾被鹽和陽光曬淺，幾乎總是鹽風吹亂或鬆散編成的辮子 |
| 眼鏡 | 無 — 偶爾把太陽眼鏡推到頭髮上，不戴著 |
| 穿衣風格 | 比基尼是日常打底；外面隨手套寬大男裝襯衫或素T，牛仔短褲，大多數時候光腳 |

---

## 核心 Prompt 結構

> 純物理描述，不參照任何真實名人或藝人臉型。

```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint
from years facing open water, athletic swimmer/surfer build with toned shoulders and upper back,
lean defined core, strong legs, naturally curvy hips, deep even golden tan,
long beachy wave dark brown hair lightened at the ends from sun and salt, salt-tousled or in a loose undone braid,
[SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING],
high natural contrast, slightly overexposed highlights, true-to-life unretouched skin texture with visible tan lines,
candid outdoor lifestyle photo, shot on phone or action camera, Instagram style
```

**風格關鍵詞備註**：
- 一定要保留 `true-to-life unretouched skin texture` 和 `visible tan lines`——這是 Zoe 美學的核心，跟其他角色的「精緻磨皮感」相反
- 光線永遠是自然光關鍵詞（`morning light` / `harsh midday sun` / `golden hour backlight`），不要出現任何棚燈、環形燈相關詞
- 禁止出現裸露或性暗示相關詞彙；服裝上限是比基尼/泳裝，符合海灘網紅帳號的主流尺度

---

## 計畫批次 Prompt 規劃

> 以下為**計畫中**的訓練圖批次，尚未執行生成。實際執行後應在此文件補上：使用的平台/模型、實際生成張數、選用結果、圖片路徑。目前僅記錄場景規劃與草稿 prompt。

### 批次規劃 1 — 晨間衝浪，日出前走向海邊（計畫 2 張）

**場景描述**：天還沒亮，Zoe 走向花蓮海邊，板夾在腋下，天色剛開始從深藍轉紫，第一道光還沒出現。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with toned shoulders and upper back, lean defined core, strong legs,
naturally curvy hips, deep even golden tan, long beachy wave dark brown hair in a loose undone braid,
walking toward the beach before sunrise carrying a surfboard under one arm, wearing a black one-piece swimsuit,
walking pose mid-stride viewed from the side, pre-dawn deep blue-purple sky with faint first light on the horizon,
high natural contrast, true-to-life unretouched skin texture, candid outdoor lifestyle photo,
shot on phone or action camera, Instagram style
```

---

### 批次規劃 2 — 泳裝日常，鏡前穿搭確認（計畫 2 張）

**場景描述**：站在花蓮公寓的小房間鏡子前，決定今天穿哪件比基尼，外面披一件寬大男裝襯衫，隨手扣兩顆扣子。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with toned shoulders and upper back, lean defined core, strong legs,
naturally curvy hips, deep even golden tan, long beachy wave dark brown hair salt-tousled and loose,
standing in front of a small bedroom mirror, wearing a bikini with an oversized men's button-down shirt
worn open over it, hands buttoning two buttons, looking at her own reflection not at camera,
bright natural morning window light, full body mirror shot, candid unposed moment,
high natural contrast, true-to-life unretouched skin texture, shot on phone, Instagram style
```

---

### 批次規劃 3 — 沖鹽淨身，衝浪後戶外沖水（計畫 2 張）

**場景描述**：衝完浪後在戶外沙灘沖澡柱下沖掉鹽分和沙子，頭往後仰,陽光直射,水珠飛濺。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with toned shoulders and upper back, lean defined core, strong legs,
naturally curvy hips, deep even golden tan, wet long beachy wave dark brown hair slicked back from rinsing,
standing under an outdoor beach rinse shower, wearing a black bikini, head tilted back with eyes closed,
water droplets visible in bright sunlight running down shoulders and arms, harsh midday natural sunlight,
medium shot from the side, candid post-surf moment, high natural contrast, slightly overexposed highlights,
true-to-life unretouched wet skin texture, shot on phone or action camera, Instagram style
```

---

### 批次規劃 4 — 衝浪旅行，墾丁黃金時段全身（計畫 2 張）

**場景描述**：墾丁海邊民宿陽台，傍晚黃金時段，板子晾在欄杆上，Zoe 站著看向海景，全身入鏡。

**草稿 Prompt**：
```
26-year-old Taiwanese woman, sun-warmed oval face with an easy wide smile, straight dark brows,
light dusting of freckles across nose and upper cheeks, dark brown eyes with a natural relaxed squint,
athletic swimmer/surfer build with toned shoulders and upper back, lean defined core, strong legs,
naturally curvy hips, deep even golden tan, long beachy wave dark brown hair down and windblown,
standing on a beachside guesthouse balcony in Kenting, a surfboard resting against the railing beside her,
wearing a bikini with denim cutoff shorts, full body shot, looking out toward the ocean not at camera,
warm golden hour backlight from the setting sun over the water, high natural contrast,
true-to-life unretouched skin texture, candid travel lifestyle photo, shot on phone, Instagram style
```

---

## 下一步（待執行）

1. 選定生成平台與模型（尚未決定 — 需先確認亞洲臉孔生成效果，可參考 Iris Chen 案例中 Seedream 4.5 優於 Recraft V4.1 的結論，但仍需針對 Zoe 的曬痕/雀斑/健康膚況做效果測試）
2. 依上述 4 個批次規劃生成訓練圖，每批次先生成 2 張比較效果
3. 訓練圖確認後，執行 Soul 訓練流程
4. 訓練完成後，才開始规划後續生活照與影片批次（本文件屆時需新增「已生成」章節，並記錄實際 soul_id、Job ID、圖片路徑）

**目前無**：soul_id、已生成圖片數量、生成日期、Job ID。以上欄位皆待實際執行後填入，禁止在此階段預先填寫。
