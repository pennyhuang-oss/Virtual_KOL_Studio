# Yuna Kim — Generation Notes

## Soul Training

- **Soul ID**: `235794a5-2eff-45fb-91b4-3232910afefa`
- **Model**: `soul_2`
- **Status**: Training completed 2026-06-29
- **Training images** (5 total):
  - 4 face reference images from `images/face_reference/` (ref_01 through ref_04)
  - 1 supplementary image generated during training prep

## Appearance Summary

- **Age**: 21
- **Ethnicity**: Korean
- **Height**: 168cm
- **Hair**: Dark brown to black, natural wavy with airy volume, collarbone-length
- **Eyes**: Large, double eyelid, bright — focal point of every look
- **Skin**: Fair, porcelain, well-maintained
- **Body**: Tall and slender
- **Style**: K-sweet meets Y2K — mini skirts, oversized cardigans, platform shoes. Always one unexpected element.

## 測試圖（待生成）

> ⏳ 訓練完成，等使用者確認場景後生成測試圖。

### 測試用 Prompt 結構

```
21-year-old Korean woman, fair porcelain skin, large double-eyelid eyes,
dark brown wavy hair with airy volume, tall slender figure,
[SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING],
film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

## Usage

```python
# Generate with Soul V2
generate_image(
    model="soul_2",
    soul_id="235794a5-2eff-45fb-91b4-3232910afefa",
    prompt="21-year-old Korean woman, fair porcelain skin, large double-eyelid eyes, ..."
)
```
