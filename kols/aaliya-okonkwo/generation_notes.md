# Aaliya Rivera — Generation Notes

## Soul Training

- **Soul ID**: `97f5c6cd-1c0c-4432-83d0-dd42210ecada`
- **Model**: `soul_2`
- **Status**: Training initiated 2026-06-29
- **Training images** (5 total):
  - 4 face reference images from `images/face_reference/` (ref_01 through ref_04)
  - 1 supplementary image generated with `seedream_v4_5` (Latina portrait, natural makeup):
    - Job ID: `96199478-3a73-4cf6-81cf-183750071cb8`
    - CDN URL: `https://d8j0ntlcm91z4.cloudfront.net/user_3EwEMQfGwzQsWNyf2tb24nCPjXS/hf_20260629_162211_96199478-3a73-4cf6-81cf-183750071cb8.png`

## Appearance Summary

- **Age**: 25
- **Ethnicity**: Latina (Mexican-American)
- **Height**: 170cm
- **Hair**: Long, dark brown wavy hair
- **Eyes**: Dark, almond-shaped, expressive
- **Skin**: Olive warm skin
- **Body**: Hourglass figure — curvy, confident
- **Style**: LA Latina — crop tops, high-waisted denim, fitted dresses, strappy heels

## Usage

```python
# Generate with Soul V2 (after training completes ~10 min)
generate_image(
    model="soul_2",
    soul_id="97f5c6cd-1c0c-4432-83d0-dd42210ecada",
    prompt="25-year-old Latina woman, olive warm skin, long dark brown wavy hair, ..."
)
```

> ⚠️ 測試圖待訓練完成後生成，需等 Soul 訓練完畢（約 10 分鐘）。
