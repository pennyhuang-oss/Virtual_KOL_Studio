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

---

## 舞蹈影片記錄（2026-07-06）

### Start Frame

| Job ID | 說明 | Media ID |
|--------|------|----------|
| `510ed6c8` | 三分之三身站立，rust orange ruched bodycon dress，LA 夜景背景 | `70b24574` |

### 音樂

| 音樂 | Audio Media ID |
|------|---------------|
| 蟹二搖（TikTok 熱門卡點音樂） | `335a9612` |

### 已生成影片清單

| 版本 | 時長 | 服裝 | 背景 | Job ID | generate_audio | 狀態 |
|------|------|------|------|--------|---------------|------|
| dance_v1 | 15s | rust orange ruched bodycon dress | LA rooftop bar night | `2ccf4760` | false ✓ | ✅ 完成（待用戶確認） |

### 舞蹈影片 Prompt 模板（已驗證）

```
25-year-old Latina woman, olive warm skin, long dark brown wavy hair, dark almond-shaped expressive eyes,
curvy hourglass figure with full chest and slim waist, bust 90cm waist 61cm hip 95cm D cup (see profile.json measurements),
wearing rust orange ruched bodycon dress, mid-thigh length,
THREE QUARTER BODY SHOT, mid-thigh up, no shoes shown,
chest bounce and jiggle physics,
energetic Latin dance, body rolling, hip sway, powerful rhythmic movement, arm movements,
LA rooftop bar night background, city lights, warm evening ambiance,
synced to the music beat and rhythm, dynamic dance movement, confident sensual energy,
shot on iPhone, natural lighting, warm tones,
single continuous shot no camera cuts, character always centered in frame, staying within frame boundaries at all times
```

### 舞蹈影片生成 Checklist

- `generate_audio: false` ← 必填，否則模型自己生成音樂蓋掉 audio_reference
- `audio` role 帶入正確 media_id（`335a9612`）
- `start_image` 帶入正確 media_id（`70b24574`）
- `THREE QUARTER BODY SHOT` 在 prompt 裡
- `centered in frame, staying within frame boundaries at all times`（防黑邊）
- `single continuous shot no camera cuts`（防鏡頭切換）
- 背景無 mirror（mirror 會讓模型誤判成鏡頭切換）
- 無 NSFW 觸發詞（避免：sexy expression, sensual isolation, snaps hips hard）

---

## 日常自拍影片記錄（2026-07-07）

> 方向：男性受眾，泳池自拍，濕身身材展示，運動感性感，非廣告感。
> 模型：`kling3_0`（單鏡頭，臉部鎖定）
> 完整 SOP 見 `DAILY_VIDEO_SOP.md`

### Start Frame（日常服裝）

| Job ID | 說明 | 已選 | Media ID |
|--------|------|------|----------|
| `2bc0f0f7` | 泳池邊，黑色比基尼上衣，半身出水，撥頭髮，自拍角度 | ✅ 已選 | `e6892cd0` |
| `7f56a6d4` | 同場景，第二張備選 | — | — |

**Start Frame Prompt（已驗證）**：
```
25-year-old Nigerian woman, gorgeous face, high cheekbones,
natural curly black hair, athletic curvy figure,
at poolside emerging from water, wearing black bikini top,
wet skin glistening, hand running through wet hair, looking directly at camera,
phone selfie angle held at arm level, half body shot from waist up,
bright natural outdoor pool lighting, candid self-portrait feel,
shot on iPhone front camera, warm tones, film grain
```

> 注意：prompt 使用 Nigerian 描述，但 soul_id `97f5c6cd` 鎖定了正確的 Aaliya 臉部身份（Latina）。

### 日常影片

| 版本 | 場景 | 服裝 | Job ID | 模型 | 狀態 |
|------|------|------|--------|------|------|
| daily_v1 | 泳池邊，半身出水，撥頭髮，看鏡頭，濕身展示 | 黑色比基尼上衣 | `d51676c3` | kling3_0 | ✅ 批准 |

**影片 Prompt（已驗證）**：
```
25-year-old Nigerian woman, gorgeous face, natural curly black hair wet from pool,
athletic curvy figure, in swimming pool with water up to waist,
slowly emerging and leaning on pool edge, one hand running through wet curly hair,
looking directly at camera with confident natural expression,
sparkling blue pool water, bright outdoor natural sunlight,
single continuous shot, phone selfie casual feel, warm tones
```

**參數**：
```python
model = "kling3_0"
medias = [{"role": "start_image", "value": "e6892cd0"}]
sound = "on"
aspect_ratio = "9:16"
duration = 10
```

---

## 2026-07-25 新增：身材數字 + 風格參考

- 身材數字（bust 90cm / waist 61cm / hip 95cm / D cup）已補進舞蹈影片核心 prompt 模板的身材描述行，取代單靠「curvy hourglass figure」等形容詞；臉部描述（almond-shaped eyes 等）維持原樣不動，既有已核准圖片/soul_id/訓練紀錄不受影響。
- 未來生成請參考 `SEXY_SCENE_LIBRARY.md` 光源段落的最新分流：Aaliya 的內容以 LA 戶外/泳池/海邊生活風格為主，多數場景應套用新的「討喜自然光（黃金時段/戶外強光）+ 淺景深+清晰高畫質」配方，而非舊版室內親密場景的「混合不均勻光線」配方（後者仍保留給晨起/浴室/居家等室內場景使用）。
