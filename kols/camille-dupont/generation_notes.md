# Camille Dupont — Generation Notes

## Soul V2

**Soul ID:** `f19dafcc-5bc8-4d8f-af1d-ee48084ac398`  
**Model:** `soul_2`

### 外型設定（生成時必帶）
- 年齡：22 歲
- 膚色：light fair skin
- 眼睛：warm hazel light brown eyes
- 髮型：**long straight blonde hair, natural honey golden color**（每次必寫，Soul V2 不繼承訓練圖）
- 身高/身材：169cm slender figure with curves

---

## 測試圖 v1（soul_test_v1）

### 場景設計

| 場景 | 圖片 | 構圖 | 說明 |
|------|------|------|------|
| Seine riverbank golden hour | `seine_01.png` | 3/4 全身站姿 | 靠在石欄杆，望向遠方，cream knit top + midi skirt |
| Seine riverbank golden hour | `seine_02.png` | 3/4 全身站姿 | 同場景第 2 張 |
| Paris apartment morning light | `window_01.png` | 全身/3/4 逆光 | 落地窗前，白色 silk slip dress，晨光透入 |
| Paris apartment morning light | `window_02.png` | 全身/3/4 逆光 | 同場景第 2 張 |
| Parisian rooftop terrace dusk | `rooftop_01.png` | 3/4 全身 | 屋頂露台，巴黎天際線，低胸洋裝，側身或回眸 |
| Parisian rooftop terrace dusk | `rooftop_02.png` | 3/4 全身 | 同場景第 2 張 |

### 構圖多樣性版（soul_test_v1）

| 場景 | 圖片 | 構圖 | 說明 |
|------|------|------|------|
| Seine riverbank | `seine_wide_01.png` | **廣角全景，人物小** | 人在遠處，塞納河與奧斯曼建築為主體 |
| Seine riverbank | `seine_portrait_01.png` | **臉部近景** | 只有臉和肩膀，側光，bokeh 河岸背景 |
| Paris apartment morning | `window_silhouette_01.png` | **全身逆光剪影，從房間遠端拍** | 暗室+窗外逆光，全身剪影 |
| Paris apartment morning | `window_lowangle_01.png` | **半身仰角** | 從略低角度往上拍，窗光從上打下 |
| Rooftop terrace dusk | `rooftop_wide_01.png` | **廣角，人物小，天際線為主** | 人站在露台遠處，巴黎屋頂為主要畫面 |
| Rooftop terrace dusk | `rooftop_shoulder_01.png` | **肩部後方回眸特寫** | 從她肩後拍，她回頭看鏡頭，天際線在肩後虛化 |

---

## 生成規則

1. **髮色/髮型**：每個 prompt 必須寫 `long straight blonde hair, natural honey golden color`，Soul V2 不會自動繼承。
2. **構圖多樣**：一組多張圖要明確設定不同的 shot size（wide/3/4/close-up）和角度（正面/側面/仰角/俯角）。
3. **性感身材**：廣角或遠景構圖時，人物比例小，身材細節不明顯——需在場景比例和身材展示之間取得平衡。
4. **真實感**：加入 `film grain, shot on 35mm, slightly off-center composition` 等避免過於 CGI。
