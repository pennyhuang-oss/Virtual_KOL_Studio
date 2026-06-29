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

## 測試圖（soul_test_v1）

生成日期：2026-06-30，共 6 張，3 個場景各 2 張。

### 場景 1 — 自拍（Selfie）
**檔案:** `selfie_01.png`, `selfie_02.png`
**Prompt:**
```
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black hair with wispy ends and cherry hair clips, 168cm, close-up front-facing selfie shot, slightly overhead angle looking down at camera, natural relaxed smile, wearing oversized cream university sweater, soft indoor lighting with ring light glow in background, looks like a photo taken by her own phone front camera, warm tones, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

### 場景 2 — 江南咖啡廳（Gangnam Café）
**檔案:** `cafe_01.png`, `cafe_02.png`
**Prompt:**
```
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black wavy hair, 168cm, sitting by window in Gangnam café Seoul, both hands resting on table, slightly turning head to look out the window, wearing mini skirt and oversized cardigan with chunky chain necklace, natural window light casting soft shadows, clean table with no drinks, full body sitting pose, warm tones, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

### 場景 3 — 弘大街頭（Hongdae Street）
**檔案:** `street_01.png`, `street_02.png`
**Prompt:**
```
21-year-old Korean woman, fair porcelain skin, large double-lidded eyes, dark brown-to-black wavy hair, 168cm, walking on Hongdae outdoor pedestrian street Seoul, golden hour evening light, wearing Y2K style plaid mini skirt and white fitted top with vintage small shoulder bag, 3/4 body candid street shot, warm orange golden light, background with blurred street scenery, film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

### Prompt 結構模板

```
[age]-year-old Korean woman, [skin], [eyes], [hair], [height], [scene], [outfit], [angle/composition], [lighting], film grain, candid lifestyle photo, shot on 35mm, Instagram style
```

### 注意事項

- 自拍 prompt 描述「輸出視角」而非「拍照動作」，避免手機入鏡或第三人稱角度
- 參考 Iris Chen 自拍 prompt 結構（`kols/iris-chen/generation_notes.md`）

## Usage

```python
# Generate with Soul V2
generate_image(
    model="soul_2",
    soul_id="235794a5-2eff-45fb-91b4-3232910afefa",
    prompt="21-year-old Korean woman, fair porcelain skin, large double-eyelid eyes, ..."
)
```
