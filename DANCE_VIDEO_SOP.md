# Dance Video SOP — TikTok 舞蹈影片生成流程

> 標準工作流程：為任何 KOL 生成 TikTok 舞蹈影片（音樂同步，臉部鎖定）。
> 本流程於 2026-07-03 透過 Iris Chen 舞蹈影片測試確立。

---

## 完整五步驟流程

### Step 1：上傳音樂檔案

```python
# 1a. 取得 presigned URL
media_upload(file_name="song_name.mp3", media_type="audio")
# → 回傳 presigned_url 和 upload_id

# 1b. 用 curl 上傳 mp3
# curl -X PUT "<presigned_url>" \
#   -H "Content-Type: audio/mpeg" \
#   --data-binary @"/path/to/song.mp3"

# 1c. 確認上傳完成
media_confirm(upload_id="<upload_id>", media_type="audio")
# → 回傳 audio_media_id
```

**結果**：取得 `audio_media_id`（之後用於 audio_references）

---

### Step 2：用 Soul V2 生成 Start Frame（舞蹈服裝靜態圖）

```python
generate_image(
  model="soul_2",
  soul_id="<KOL_SOUL_ID>",
  prompt="[年齡] [國籍] girl, [臉部特徵], [身材描述], [黑色直髮或對應髮型], "
         "standing in confident pose, wearing [OUTFIT], "
         "THREE QUARTER SHOT, mid-thigh up, no shoes shown, "
         "[背景描述], "
         "film grain, candid lifestyle photo, warm tones, shot on 35mm",
  aspect_ratio="9:16",
  count=2
)
```

**關鍵規則**：
- **THREE QUARTER SHOT（mid-thigh up, no shoes shown）**：必須寫明，避免全身圖導致後續舞蹈影片腿部截斷
- Start frame 決定整支舞蹈影片的外觀和服裝，要在這裡確定好
- 生成 2 張，選最好的一張繼續

**結果**：取得 start frame 的 `rawUrl`

---

### Step 3：匯入 Start Frame 為 Media

```python
media_import_url(url="<rawUrl_from_step2>")
# → 回傳 image_media_id
```

**注意**：必須先 import 才能在影片生成中使用，不能直接用 rawUrl。

**結果**：取得 `image_media_id`

---

### Step 4：生成舞蹈影片

```python
generate_video(
  model="seedance_2_0",
  prompt="[KOL 描述], wearing [OUTFIT], "
         "THREE QUARTER BODY SHOT, mid-thigh up, no shoes shown, "
         "chest bounce and jiggle physics, "
         "[舞蹈風格描述，如：energetic hip-hop dance, body rolling, hip sway, arm movements], "
         "[背景描述], "
         "synced to the music beat and rhythm, "
         "dynamic dance movement, confident sensual energy, "
         "shot on iPhone, natural lighting, warm tones",
  start_image={"id": "<image_media_id>"},          # 鎖定臉部身份
  audio_references=[{"id": "<audio_media_id>"}],   # 音樂同步舞蹈動作
  generate_audio=False,                             # 不生成 AI 音效，只用 audio_reference
  duration=15,                                      # 最大時長
  aspect_ratio="9:16"
)
```

**關鍵參數說明**：

| 參數 | 值 | 說明 |
|------|-----|------|
| `start_image` | `{"id": image_media_id}` | 鎖定臉部身份，整支影片保持一致 |
| `audio_references` | `[{"id": audio_media_id}]` | 讓舞蹈動作跟著音樂節拍同步 |
| `generate_audio` | `False` | **必須關閉**，否則會用 AI 生成音效蓋掉你的音樂 |
| `duration` | `15` | 最大可用時長 |

**重要：audio_reference 只控制動作節拍，不會把音樂嵌入影片。** 影片輸出是無聲的（或有 AI 環境音），需要後製步驟加入音樂。

**結果**：生成舞蹈影片（無音樂嵌入）

---

### Step 5：後製（CapCut）

1. 將生成的影片匯入 CapCut
2. 將原始 mp3 拖曳到音軌，對齊到影片開頭
3. 導出 — 由於舞蹈動作已根據音樂節拍生成，節拍同步是自然的

---

## Prompt 模板（含佔位符）

### Start Frame Prompt（Step 2）

```
[AGE]-year-old [NATIONALITY] girl, strikingly beautiful sweet face, [FACE_FEATURES],
[BODY_DESCRIPTION], [HAIR_DESCRIPTION],
standing in confident pose ready to dance,
wearing [OUTFIT_DESCRIPTION],
THREE QUARTER SHOT, mid-thigh up, no shoes shown,
[BACKGROUND_DESCRIPTION],
film grain, candid lifestyle photo, warm tones, shot on 35mm
```

**佔位符說明**：
- `[OUTFIT_DESCRIPTION]`：完整服裝描述（例如：black crop top and high-waist biker shorts）
- `[BACKGROUND_DESCRIPTION]`：背景（例如：plain studio background, white seamless）
- `[HAIR_DESCRIPTION]`：髮色+髮型（Soul V2 每次都要明確描述，不會自動繼承）

---

### Dance Video Prompt（Step 4）

```
[AGE]-year-old [NATIONALITY] girl, [BODY_DESCRIPTION], [HAIR_DESCRIPTION],
wearing [OUTFIT_DESCRIPTION],
THREE QUARTER BODY SHOT, mid-thigh up, no shoes shown,
chest bounce and jiggle physics,
[DANCE_STYLE_DESCRIPTION],
[BACKGROUND_DESCRIPTION],
synced to the music beat and rhythm,
dynamic dance movement, confident sensual energy,
shot on iPhone, natural lighting, warm tones
```

**舞蹈風格範例**：
- `energetic hip-hop dance, body rolling, hip sway, arm wave movements`
- `Vietnamese drum beat inspired dance, powerful rhythmic stomping, traditional meets street style`
- `pop dance routine, body wave, bouncing to the beat, playful hip movements`
- `K-pop style choreography, sharp arm movements, fluid body rolls`

---

## 模型對比參考表

| 模型 | 臉部鎖定 | 多鏡頭 | 音樂同步 | 最大時長 | 最適用場景 |
|------|---------|--------|---------|---------|-----------|
| `kling3_0` | ✅ start_image | ❌（非自動） | ✅ sound:on | 15s | 親密場景、臉部鎖定單鏡頭 |
| `seedance_2_0` | ✅ start_image | ❌ | ✅ audio_references | 15s | **舞蹈影片（首選）** |
| `cinematic_studio_video_v2` | ❌（會漂移） | ✅ multi_shots | ✅ sound:on | 12s | 多鏡頭電影感（臉部可能漂移） |
| `soul_2` | ✅ soul_id | N/A | N/A | N/A | 僅用於生成靜態 start frame |

**重要**：`soul_id` 只能用於 `soul_2` 的靜態圖片生成，**不能用於影片生成**。影片生成的臉部鎖定靠 `start_image` 參數。

---

## 已驗證可用的音樂類型

| 音樂類型 | 舞蹈效果 | 備註 |
|---------|---------|------|
| 越南鼓（Vietnamese drum beat） | ✅ 強烈節拍同步，動作有力 | 2026-07-03 Iris v1+v2 使用 |
| Sugar on my tongue（流行） | ✅ 流暢身體波動，性感節奏感 | 2026-07-03 Iris v3 使用 |

---

## 已知問題與注意事項

| 問題 | 說明 | 解法 |
|------|------|------|
| 全身圖導致腿部截斷 | 如果 start frame 是全身圖，影片可能在膝蓋處截斷 | 務必使用 THREE QUARTER SHOT（mid-thigh up） |
| 影片無音樂 | audio_reference 控制動作節拍，但不嵌入音樂 | 後製（CapCut）加入 mp3 |
| start_image 未 import | 直接使用 rawUrl 會失敗 | 必須先 media_import_url 取得 image_media_id |
| generate_audio 未關閉 | AI 生成的音效會蓋掉 audio_reference 效果 | 一定要設 generate_audio=False |

---

## Iris Chen 實際使用案例（2026-07-03）

### 舞蹈 v1（10s，黑色 crop top + 騎車短褲，越南鼓）

- Soul ID：`5fe3b6ba-1277-4822-9141-fb06eb3b93a0`
- 音樂：越南鼓（Vietnamese drum beat）
- Start frame job：（圖片 job，以 soul_2 生成）
- Start frame media ID：`89010b47`（浴室場景 start frame，先借用測試）
- Video job：`1b0aee3d`
- 結果：✅ 用戶批准（動作自然，節拍同步）

### 舞蹈 v2（15s，黑色 crop top + 騎車短褲，越南鼓）

- 同 v1 設定，加長至 15s
- Video job：`1b767b3b`
- 結果：✅ 用戶保留

### 舞蹈 v3（15s，淡藍色 V 領洋裝，Sugar on my tongue）

- 換服裝和音樂測試效果
- Video job：`3d3ac1b2`
- 結果：✅ 用戶批准

---

*建立日期：2026-07-03*
*適用平台：Higgsfield（透過 MCP 連接）*
