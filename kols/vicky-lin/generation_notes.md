# Vicky Lin — AI 生成規劃

> **狀態：PENDING（尚未執行）**
> 本文件只是生成前的規劃筆記——尚未進行任何 Soul 訓練、尚未生成任何訓練圖或影片，也尚未選定最終使用的模型版本。所有 prompt 為草稿，需要實際跑過並確認效果後才能標記為已驗證。文件中不含任何 soul_id、job_id、圖片張數或生成日期，因為目前都還不存在。

---

## 人物設定

| 欄位 | 設定 | 狀態 |
|------|------|------|
| 名字 | Vicky Lin（林薇淇） | — |
| 年齡 | 25 歲 | — |
| 國籍 / 出身地 | 台灣，高雄 | — |
| 臉型 | 銳利分明的五官——線條明顯的下顎、突出的顴骨、濃直眉、直視帶強勢感的眼神，不是圓臉可愛系，臉部本身要有「訓練感」的稜角 | 純外型描述，非參考真人 |
| 身材 | 運動型 hourglass——肩背有重訓線條、腹肌明顯、臀腿因深蹲和功能性訓練而有形，身材要讀出「有練過」而不是單純纖瘦 | — |
| 膚色 | 因戶外訓練而略帶古銅色，非白皙 | — |
| 髮型 | 長黑髮，訓練時綁高馬尾或編髮，休息時自然放下 | — |
| 穿衣風格 | 運動內衣、緊身高腰褲、crop tank、練後帽 T（拉鏈半開或滑落一邊肩膀） | — |
| 眼鏡 | 無 | — |
| Soul 模型 | 尚未建立 | **PENDING** |
| 訓練圖 | 尚未生成 | **PENDING** |
| 已生成圖片數量 | 0 | **PENDING** |
| 已生成影片數量 | 0 | **PENDING** |

**⚠️ 生成一致性注意**：肌肉線條、腹肌、古銅膚色是她的核心視覺特徵，任何批次的 prompt 都不能把這些修掉或磨平；場景、穿搭、光線可以依批次變化，但體態特徵需維持一致。

---

## 核心 Prompt 結構（規劃草稿，未驗證）

以下為預計用於後續訓練圖 / 生活照生成的**可重複使用基礎 prompt**。全部使用純外觀描述詞，不引用任何真實藝人或公眾人物姓名。

```
25-year-old Taiwanese woman, sharp striking features, angular jawline, defined cheekbones, straight thick eyebrows, direct confident gaze, athletic toned hourglass figure with visible muscle definition, strong shoulders and back, defined core and abs, curvy trained glutes and thighs, sun-tanned skin, long black hair, [HAIRSTYLE], [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], slightly high-contrast true-to-skin color grading, visible sweat sheen where relevant, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

**待決定事項（需在實際測試後補上結論）**：
- 使用哪個模型（Seedream / Recraft / 其他）對亞洲運動型女性身材與汗水質感還原度最好，需要實測比較
- `[HAIRSTYLE]` 依場景切換：`high ponytail pulled back tight`（訓練中）／`natural loose down`（居家、浴室、飯店）
- 是否需要額外關鍵詞強化「肌肉線條」而不被模型預設磨皮抹平（例如 `visible muscle striation, no skin smoothing`），需要實測驗證效果

---

## 計畫批次 Prompt 規劃（尚未執行）

以下 4 個批次為**規劃中的訓練圖 / 首波生活照場景**，用於之後建立 Soul 模型或直接生成生活照。批次順序、每批次張數、實際模型選擇都待執行時決定，這裡只先把場景與 prompt 草稿定下來。

### 批次 1（規劃）— 健身房鏡前，訓練中全身

**場景描述**：深蹲架前或自由重量區的落地鏡前，正在準備或剛完成一組訓練，全身入鏡展示動作與身材線條，健身房日光燈或大窗自然光。

**草稿 Prompt**：
```
25-year-old Taiwanese woman, sharp striking features, angular jawline, defined cheekbones, direct confident gaze, athletic toned hourglass figure with visible muscle definition, strong shoulders and back, defined core and abs, sun-tanned skin, long black hair in high tight ponytail, standing in front of gym mirror near squat rack, wearing black sports bra and high-waist fitted leggings, full body shot, confident direct gaze at mirror reflection, hard gym fluorescent lighting mixed with daylight through windows, visible sweat sheen, slightly high-contrast true-to-skin color grading, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

---

### 批次 2（規劃）— 戶外訓練，黃金時段

**場景描述**：戶外空地或河濱訓練場景（高雄常見的戶外功能性訓練環境），黃昏黃金時段逆光或側光，動作中或組間喘氣的瞬間。

**草稿 Prompt**：
```
25-year-old Taiwanese woman, sharp striking features, angular jawline, defined cheekbones, athletic toned hourglass figure with visible muscle definition, strong shoulders and back, defined core and abs, sun-tanned skin, long black hair in tight braid, training outdoors on open concrete court during golden hour, wearing black crop tank and high-waist leggings, mid-action pose or catching breath between sets, warm golden backlight, visible sweat sheen on skin, slightly high-contrast true-to-skin color grading, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

---

### 批次 3（規劃）— 練後居家恢復

**場景描述**：高雄公寓客廳地板，練後伸展或滾筒放鬆,運動服未換,身體仍帶著訓練後的疲憊與泵感,自然居家光線。

**草稿 Prompt**：
```
25-year-old Taiwanese woman, sharp striking features, angular jawline, defined cheekbones, athletic toned hourglass figure with visible muscle definition, defined core and abs, sun-tanned skin, long black hair naturally down loosened from training, sitting on living room floor doing post-workout stretch, wearing black sports bra and short shorts, oversized hoodie unzipped slipping off one shoulder nearby, relaxed tired expression, natural warm afternoon light through apartment window, slightly high-contrast true-to-skin color grading, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

---

### 批次 4（規劃）— 賽前備賽飯店

**場景描述**：出差或賽前訓練營住宿的飯店房間，行李與比賽裝備並存,對著鏡子確認狀態或坐在床邊查看飯店健身房資訊,帶一點出差的緊繃感而非度假感。

**草稿 Prompt**：
```
25-year-old Taiwanese woman, sharp striking features, angular jawline, defined cheekbones, direct confident gaze, athletic toned hourglass figure with visible muscle definition, strong shoulders and back, defined core and abs, sun-tanned skin, long black hair in high ponytail, sitting on hotel bed with luggage and competition gear visible nearby, checking phone for hotel gym hours, wearing black sports bra and leggings, focused slightly tense expression, hotel room warm lighting mixed with window daylight, slightly high-contrast true-to-skin color grading, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

---

## 下一步（待執行，非已完成）

1. 選定圖片生成模型並小規模測試亞洲運動型女性身材／肌肉線條／汗水質感的還原效果
2. 依測試結果調整核心 prompt 結構中的關鍵詞（特別是肌肉線條與膚色是否被模型過度磨皮）
3. 依批次規劃產出實際訓練圖，確認滿意後才進入 Soul 訓練流程
4. Soul 訓練完成後才回頭補上 soul_id、訓練圖路徑與實際批次記錄
5. 影片生成流程（模型選擇、prompt 模板、剪輯節奏對應）待圖片流程確認後另行規劃，目前尚未展開
