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

### 場景 3（公園黃金時段）— ⚠️ 構圖雷同
- 兩張圖拍攝角度、人物比例幾乎相同，看起來像同一套圖
- 同一場景的兩張圖必須刻意安排不同構圖（例如：一張廣角/一張近景，或一張正面/一張側面回眸）
- 參見 [[feedback-image-composition-variety]]

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
