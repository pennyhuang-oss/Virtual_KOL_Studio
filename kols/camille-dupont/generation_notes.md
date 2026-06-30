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
5. **服裝必須明確寫出**：不寫服裝 = 模型往最少衣服方向走。Camille 的標準在家服裝：`loose cream linen button-down shirt with sleeves rolled up, high-waist straight trousers`。
6. **道具物理位置**：道具必須明確說位置，例如「wine glass placed and resting ON THE COUNTER surface」，否則容易浮空。
7. **自然感關鍵詞**：要呈現不擺拍的感覺，加入 `NOT looking at camera`、`candid unposed moment`、`completely absorbed in [activity]`、`unaware of being photographed`。
8. **場景多元化**：不要所有 shots 都在廚房——主動規劃不同場景（廚房、咖啡廳露台、市場、窗邊、客廳）。

---

## 自我介紹素材 v1（self_intro_v1）— 2026-06-30 通過

**路徑：** `images/self_intro_v1/`  
**本批通過 4 張，放棄 2 張（市場、沙發看書）。**

| 圖片檔案 | 場景 | 她的狀態 | Higgsfield Job ID |
|---------|------|---------|-----------------|
| `shot01_kitchen_chop_onion.png` | 廚房，切洋蔥 | 看向砧板，不看鏡頭，專注 | `5acafb87-88c8-40c0-93ff-4365d6780e98` |
| `shot02_taste_sauce.png` | 廚房爐邊，嚐醬汁 | 側臉，木匙到嘴邊，眉頭微皺在判斷味道 | `04918350-d8a6-4a6e-bc7a-5996a921aedd` |
| `shot03_cafe_terrace.png` | 巴黎咖啡廳露台 | 望向街上行人，有一個自己的小微笑 | `0e02bbad-3967-4ab7-8d52-86188531c6a7` |
| `shot04_window_gaze.png` | 公寓窗邊，下巴靠手 | 看向窗外巴黎，完全沉浸在自己的思緒裡 | `6761b6ae-ad56-42c5-abb3-64d64ca9f83a` |

### 通過的 Prompt 公式

```
22-year-old French woman, long straight blonde hair natural honey golden color,
light fair skin, warm hazel light brown eyes, slender figure,
wearing [具體服裝],
[場景描述], [具體動作],
[表情/狀態], NOT looking at camera, [吸收在什麼事情上],
candid unposed moment, [景別], [光線],
Fuji 400H film grain, warm cream tones, shot on 35mm
```
