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

---

## 影片生成記錄與規則（2026-06-30）

### 使用模型

| 模型 | 特性 | 適用場景 |
|------|------|---------|
| `seedance_2_0` | 身份一致性最強（接受 start_image），單鏡頭 | 近景情緒鏡頭、細節特寫 |
| `cinematic_studio_video_v2` | 原生 multi-shot，鏡頭切換自然 | 需要多鏡頭剪輯感的日常內容 ✅ 首選 |

### 測試結果（咖啡廳場景，`cafe_test_v1`）

| 版本 | 模型 | 時長 | 解析度 | 評價 | 檔案 |
|------|------|------|--------|------|------|
| v1 | seedance_2_0 | 8s | 720p | 普通。內容太短，動作單一，AI 銳化感重 | `v1_seedance_8s_720p.mp4` |
| v2 | seedance_2_0 | 12s | 480p | 不錯，保留。自然感提升，但 480p 畫質太低 | `v2_seedance_12s_480p.mp4` |
| v3 | cinematic_studio_video_v2 | 12s | 720p | **最佳。** 多鏡頭剪切自然，有真實影片感 | `v3_cinematic_multishot_12s_720p.mp4` |

**Start frame 圖片**：`images/video_startframes_v1/frame01_cafe_seated.png`（Soul V2，job `b596e95e`）

### 影片生成注意事項（從測試中學到）

**模型參數規則**

1. **`cinematic_studio_video_v2` 的 multi-shot 必須用 `auto` 模式**
   - `multi_shot_mode: custom` + 空白 `multi_prompt` 會導致任務卡死無法完成
   - 正確做法：`multi_shots: true, multi_shot_mode: auto`，把各鏡頭描述寫進主 prompt

2. **解析度**：統一用 **720p**
   - 480p 畫質太低（現代手機不會只有 480p）
   - 「手機感」靠 prompt 關鍵詞達成，不靠降解析度

**Prompt 關鍵詞規則**

3. **要加入的手機感關鍵詞**（讓影片不像 AI 棚拍）：
   `shot on iPhone, warm soft grain, warm faded tones, no over-sharpening, natural lighting, feels like a real person filmed this`

4. **禁止加入鏡頭晃動關鍵詞**：
   - ❌ `handheld casual filming, natural slight camera movement, NOT tripod perfect, motion blur`
   - 這些關鍵詞會產生鏡頭晃動感，不符合需求
   - ✅ 鏡頭要穩定，不要有任何 camera shake

5. **內容要有完整敘事**，不能只描述一個動作：
   - ❌ 錯誤：`she picks up coffee cup and takes a sip`（太短，8 秒就結束）
   - ✅ 正確：描述 3–4 個連續動作，有起伏（如：看手機→抬頭→喝咖啡→望窗外）

6. **時長**：日常內容影片建議 **12 秒**，最短不低於 10 秒

### 最佳 Prompt 模板（cinematic_studio_video_v2）

```
Shot 1: [場景進入動作，全身或中景]
Shot 2: [主要行為，中景]
Shot 3: [特寫細節，手/道具/表情]
Shot 4: [收尾情緒鏡頭，側臉或望遠]
Shot on iPhone, warm soft grain, warm faded tones, no over-sharpening,
natural lighting, stable camera, feels like a real person filmed this.
```

```python
# 對應 API 參數
model = "cinematic_studio_video_v2"
multi_shots = True
multi_shot_mode = "auto"
genre = "intimate"
mode = "pro"
sound = "on"
aspect_ratio = "9:16"
duration = 12
resolution = "720p"  # cinematic v2 不直接支援此參數，走預設
```
