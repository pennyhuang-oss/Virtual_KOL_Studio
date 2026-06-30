# Aaliya Rivera — Generation Notes

## Soul Training

- **Soul ID**: `97f5c6cd-1c0c-4432-83d0-dd42210ecada`
- **Model**: `soul_2`
- **Status**: Training completed 2026-06-29
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

## 訓練後測試生成（2026-06-29）

> ⚠️ 生成記錄遺失：測試圖已上傳至 `images/soul_test_v1/`，但生成時未即時記錄 Job ID 和 prompt。以下為依現有圖片回溯的記錄。

共 8 張，3 個場景：

### 場景 1 — 泳池邊坐姿（Poolside）× 4 張
**檔案**：`poolside_01_v1.png`、`poolside_01_v2.png`、`poolside_02_v1.png`、`poolside_02_v2.png`
> ✅ 泳池邊場景已通過驗證（見 `SEXY_SCENE_LIBRARY.md`：泳池邊坐姿 Aaliya 已驗證）

### 場景 2 — 餐廳（Restaurant）× 2 張
**檔案**：`restaurant_01.png`、`restaurant_02.png`

### 場景 3 — 自拍（Selfie）× 2 張
**檔案**：`selfie_01.png`、`selfie_02.png`

---

> 📋 後續生成請參考 Iris Chen 的自拍 prompt 規則（`kols/iris-chen/generation_notes.md`）：描述「輸出視角」而非「拍照動作」，避免手機入鏡。
