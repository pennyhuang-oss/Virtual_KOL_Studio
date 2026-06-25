# Iris Chen — AI 生成記錄

> 只記錄確認有效的版本和步驟。錯誤嘗試已略去。

---

## 人物設定

| 欄位 | 設定 |
|------|------|
| 名字 | Iris Chen（陳芯語） |
| 年齡 | 22歲 |
| 國籍 | 台灣 |
| 臉型參考 | 熊熊（台灣藝人）：圓臉、大雙眼皮、精緻鼻梁、飽滿嘴唇、小下巴 |
| 身材 | 嬌小前凸後翹，hourglass，胸部飽滿、腰細 |
| 穿衣風格 | Hot girl casual：平口上衣、細肩帶、mini skirt、黑色短褲、crop hoodie |
| 眼鏡 | 無 |
| 髮型 | 黑色直髮自然放下 |

---

## 訓練圖生成流程（training_v1）

### 平台與模型

- **平台**：Higgsfield.ai
- **模型**：Seedream 4.5（`seedream_v4_5`）
- **為何選 Seedream**：Recraft V4.1 對亞洲臉孔效果差（生成路人臉），Seedream 4.5 預設就能生成網紅等級的亞洲美女臉

### 核心 prompt 結構

```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

### 批次設定

- 每批次生成 **2張**（不用4張：同場景同 prompt 下4張差異太小）
- 共4個場景，總計14張

---

## 各批次 Prompt 記錄

### 批次 1 — 台北街頭 3/4 身（4張）

```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, standing on Taipei street, wearing white spaghetti strap crop top and high-waist denim mini skirt, slight smile looking at camera, 3/4 angle, natural daylight, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

### 批次 2 — 咖啡廳窗邊正面近景（4張）

```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, sitting by cafe window, wearing light pink tube top, looking at camera with warm natural smile, front view close-up, golden afternoon light through window, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

### 批次 3 — 公園黃金時段全身（4張）

```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, standing in park during golden hour, wearing black mini shorts and fitted white crop hoodie, full body shot, looking back at camera over shoulder, warm golden backlight through trees, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

### 批次 4 — 車內自拍視角（2張）

```
22-year-old Taiwanese girl, strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge, soft full lips, small defined chin, glowing skin, photogenic idol-level beauty, petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down, close-up front-facing selfie shot, slightly overhead angle looking down at camera, natural relaxed smile, sitting in car interior background, wearing casual black spaghetti strap top, warm sunny light, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

**⚠️ 自拍視角重要規則**：prompt 描述的是照片本身的輸出視角，不是描述「她在拍自拍」的動作。
- ❌ 錯誤：`taking a selfie holding phone up` → 會生成第三人視角、手機出現在畫面中
- ✅ 正確：`close-up front-facing selfie shot, slightly overhead angle looking down at camera, looks like a photo taken by her own phone front camera`

---

## Higgsfield 操作方式（localStorage 法）

在 Higgsfield 更換 prompt 最可靠的方式：

```javascript
var raw = localStorage.getItem('hf:image-form-upd');
var data = JSON.parse(raw);
data.prompt = "NEW PROMPT HERE";
data.lastSelectedModel = "seedream_v4_5";
localStorage.setItem('hf:image-form-upd', JSON.stringify(data));
// 然後導航至：https://higgsfield.ai/ai/image?model=seedream_v4_5
```

---

## 下一步：Soul 訓練

1. 前往 Higgsfield.ai → Soul 訓練
2. 上傳這14張訓練圖
3. 等待訓練完成（Soul 2.0）
4. 用訓練好的 Soul 角色生成後續大量生活照

訓練圖路徑：`kols/iris-chen/images/training_v1/`

---

## 模型選擇結論

| 模型 | 結果 |
|------|------|
| Recraft V4.1 | ❌ 亞洲臉孔效果差，生成路人臉，不適合 |
| Seedream 4.5 | ✅ 預設生成網紅級亞洲美女臉，照片風格自然 |

---

## 照片風格原則

生成目標是「網紅在 Instagram 發的生活照」，不是「雜誌大片」：
- 要有 film grain / 35mm 感
- 場景要自然（街頭、咖啡廳、公園、車內）
- 不要過度打光或過於精緻的構圖
- 身材曲線要明顯但風格要 casual，不是刻意擺姿勢
