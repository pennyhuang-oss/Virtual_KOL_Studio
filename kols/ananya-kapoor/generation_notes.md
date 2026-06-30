# Ananya Kapoor — Generation Notes

## Soul Training

- **Soul ID**: `fac82296-8c69-4c34-b352-1b398c8b8e1c`
- **Model**: `soul_2`
- **Status**: Training completed 2026-06-29
- **Training images** (6 total):
  - 4 face reference images from `images/face_reference/` (ref_01 through ref_04)
  - 2 supplementary images generated with `seedream_v4_5` (natural lashes, no dramatic false lashes):
    - Job ID: `(supplementary images generated during training prep session)`

## Appearance Summary

- **Age**: 23
- **Ethnicity**: Indian (Punjabi)
- **Height**: 165cm
- **Hair**: Dark brown, long, naturally wavy-curly, loose or loose braid
- **Eyes**: Large, deep brown, natural lashes (not dramatic)
- **Skin**: Warm golden-brown, glowing
- **Body**: Curvy and toned — dancer/yogi physique, graceful and strong
- **Style**: Yoga sets, kurta, flowy harem pants, jewel tones, midriff-baring co-ords

## 訓練後測試生成（2026-06-29）

訓練完成後用 Soul ID 生成 6 張測試圖，確認身份一致性。

### 場景 1 — 孟買街頭（flowy floral kurta + wide-leg trousers）

- [圖 1](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162345_49900939-b0dd-450f-8d9d-cfc91e458eda.png)
- [圖 2](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162345_a511c9e8-36fa-4d52-b057-fcfc6798d7d6.png)

### 場景 2 — 咖啡廳窗邊（white cotton salwar with embroidery）

- [圖 3](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162355_5c7f246d-883d-4766-b5de-003190c3ce49.png)
- [圖 4](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162356_b2c137ba-4694-4a39-a590-bfbea287bd52.png)

### 場景 3 — 公園黃金時段（sage green saree styled contemporary）

- [圖 5](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162358_3c7d4d2e-dd21-4839-b749-ac061e86c9ff.png)
- [圖 6](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162358_c58e00c3-b3d1-425c-bda4-9b0acfe5112d.png)

> ✅ 測試圖已上傳至 `images/soul_test_v1/`（共 6 張）。

## 使用者回饋（2026-06-30）

### 場景 1（孟買街頭）— ❌ 穿搭不滿意
- `flowy floral kurta + wide-leg trousers` 這類造型**以後不要再用**，很不好看
- Ananya 的穿搭應以 yoga set、crop top、midriff-baring co-ords、緊身褲/棉質短裙為主，保持身材線條可見

### 場景 2（咖啡廳窗邊）— ✅ 可以

### 場景 3（公園黃金時段）— ⚠️ 構圖雷同（已廢棄，見下方重生成版本）
- 兩張圖拍攝角度、人物比例幾乎相同，看起來像同一套圖
- 同一場景的兩張圖必須刻意安排不同構圖（例如：一張廣角/一張近景，或一張正面/一張側面回眸）
- 參見 [[feedback-image-composition-variety]]

---

## 重生成批次（2026-06-30）

### 場景 1 v2 — 孟買咖啡廳（深寶石藍 wrap dress）✅ 通過

**穿搭**：deep jewel blue fitted wrap dress with V-neckline

| 構圖 | Job ID | CDN URL |
|------|--------|---------|
| 3/4 身，窗邊坐姿，面朝鏡頭 | `c9d7cc37-be7f-4bd8-a4e9-c17434173bdc` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260630_131514_c9d7cc37-be7f-4bd8-a4e9-c17434173bdc.png |
| 臉部近景，側臉望窗，bokeh 背景 | `64e02c03-a868-4b08-87ed-0fe9bb417f13` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260630_131518_64e02c03-a868-4b08-87ed-0fe9bb417f13.png |

**Prompts：**
```
# 圖1（3/4 身）
23-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves, large expressive dark eyes, natural lashes, elegant facial features, graceful curvy figure, sitting by large window in upscale Mumbai café, wearing deep jewel blue fitted wrap dress with V-neckline that hugs her curves, 3/4 body shot, slight smile looking at camera, soft natural window light, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style

# 圖2（臉部近景）
23-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves, large expressive dark eyes, natural lashes, elegant facial features, graceful curvy figure, inside upscale Mumbai café, wearing deep jewel blue fitted wrap dress with V-neckline, close-up portrait shot from shoulders up, slightly turned profile gazing toward window light, warm ambient bokeh background, confident relaxed expression, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

---

### 場景 3 v2 — Marine Drive 海岸散步道（鏽紅 crop top + 白色闊腿褲）✅ 通過

**穿搭**：rust terracotta fitted crop top + high-waist white wide-leg trousers

| 構圖 | Job ID | CDN URL |
|------|--------|---------|
| 廣角，人物小，海岸線天際線為主 | `abd00952-004c-480d-bb92-cc9223f54775` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260630_131744_abd00952-004c-480d-bb92-cc9223f54775.png |
| 臉部近景，海景 bokeh，黃金時段側光 | `4e00d579-15c3-488f-839f-5ff802078d13` | https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260630_131750_4e00d579-15c3-488f-839f-5ff802078d13.png |

**Prompts：**
```
# 圖1（廣角）
23-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves, large expressive dark eyes, natural lashes, graceful curvy figure, standing on Marine Drive promenade Mumbai, wearing rust terracotta fitted crop top and high-waist white wide-leg trousers, wide angle shot with person relatively small in frame, Mumbai skyline and Arabian Sea in background, golden hour warm light, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style

# 圖2（臉部近景）
23-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves, large expressive dark eyes, natural lashes, graceful curvy figure, on Marine Drive promenade Mumbai, wearing rust terracotta fitted crop top and high-waist white wide-leg trousers, close-up portrait from shoulders up, relaxed confident expression slightly looking away, Arabian Sea soft bokeh background, golden hour warm light, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

### 測試用 Prompt 結構

```
22-year-old Indian woman, warm golden-brown skin, long dark black hair with subtle waves,
large expressive dark eyes, natural lashes (not dramatic), elegant facial features,
slender graceful figure, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING],
film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

## Usage

```python
# Generate with Soul V2
generate_image(
    model="soul_2",
    soul_id="fac82296-8c69-4c34-b352-1b398c8b8e1c",
    prompt="22-year-old Indian woman, warm golden-brown skin, long dark black hair, ..."
)
```
