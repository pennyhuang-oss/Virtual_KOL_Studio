# Luna Tanaka — Generation Notes

## Soul Training

- **Soul ID**: `1bfab2ce-cfa5-4026-93fa-e5c91b469c7a`
- **Model**: `soul_2`
- **Status**: Training initiated 2026-06-29
- **Training images** (8 total):
  - 4 face reference images from `images/face_reference/` (ref_01 through ref_04)
  - 4 body-correct images from Higgsfield (童顏巨乳 body type, wrong clothes but correct face+figure):
    - `hf_20260626_040502_fe1befb3-e839-457a-b5fd-0b0ba7380b67.png`
    - `hf_20260626_040502_8dcbcd43-b57c-4a9f-a8e9-f16492fe4f0e.png`
    - `hf_20260626_040502_d546c722-e746-4f74-951a-0befbc871758.png`
    - `hf_20260626_040502_1c6a724e-8db8-48f9-8d2b-b2aa0c159c51.png`

## Appearance Summary

- **Age**: 20
- **Ethnicity**: Japanese
- **Height**: 155cm
- **Hair**: Black, fine, straight — center-parted, chin-length bob
- **Eyes**: Large, round, dark brown
- **Skin**: Fair, porcelain
- **Body**: 童顏巨乳 (youthful face, curvaceous figure)
- **Style**: Japanese soft girl meets vintage — white lace, floral cotton, oversized knits, mary jane shoes, cream/beige palette

## 訓練後測試生成（2026-06-29）

訓練完成後用 Soul ID 生成 6 張測試圖，確認身份一致性，結果通過。

### 場景 1 — 東京街頭（白色蕾絲上衣 + 碎花裙）

- [圖 1](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154140_dd6cb5c5-9ec5-465f-9db0-bf2209b46132.png)
- [圖 2](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154140_92c8e138-8940-42a5-a51c-b1654f8ce8ad.png)

### 場景 2 — 咖啡廳窗邊（奶油色 oversized 毛衣）

- [圖 3](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154146_b01362a2-1483-4281-955d-6da5e04d4343.png)
- [圖 4](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154147_ce1d5af4-5c36-4914-b716-44a2cac263cb.png)

### 場景 3 — 公園黃金時段全身（白色碎花洋裝）

- [圖 5](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154152_1c07c5db-9dba-45c2-860a-80657087dbf1.png)
- [圖 6](https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_154152_762d6881-9ab9-493e-af66-cf9cbc4f42fe.png)

### 測試用 Prompt 結構

```
20-year-old Japanese girl, black center-parted chin-length bob, large round dark brown eyes,
fair porcelain skin, petite curvy figure with full chest and slim waist,
[SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING],
film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

## Usage

```python
# Generate with Soul V2
generate_image(
    model="soul_2",
    soul_id="1bfab2ce-cfa5-4026-93fa-e5c91b469c7a",
    prompt="20-year-old Japanese girl, black center-parted chin-length bob, ..."
)
```
