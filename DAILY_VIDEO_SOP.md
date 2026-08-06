# Daily Selfie Video SOP — 日常自拍影片生成流程

> 標準工作流程：為任何 KOL 生成 TikTok / Instagram 日常自拍風格影片。
> 本流程於 2026-07-07 透過 6 個 KOL 批次生成後確立。

---

## 核心方向與目的

### 受眾設定（必讀）

**所有 12 個 KOL 的受眾都是男性。**（本流程 2026-07-07 建立時studio 只有 6 位 KOL，2026-07-24 新增 6 位後，此設計原則同樣適用於全部 12 位）

這是日常影片所有決策的前提：

- 服裝選擇 → 要展示身材曲線、乳溝、腰線
- 鏡頭角度 → 手機自拍的俯角（可天然呈現胸口視角）
- 場景選擇 → 居家、浴室、泳池、飯店——私密感 > 廣告感
- 整體氛圍 → 性感但不刻意，真實感 > 完美感

### 社群氛圍定位

目標：讓看到影片的人感覺「她在對著我一個人說話/展示」。

**應該做到的感覺**：
- 她自己拿著手機在拍，就是現在這個時刻
- 鏡頭偶爾晃動或旋轉，真實有手持感
- 不像廣告，不像 MV，不像棚拍
- BGM 是日常流行歌，不是戲劇性配樂

**絕對不能做的事**：
- 多鏡頭敘事切換（有劇情的影片是廣告，不是日常）
- 腳本化的 shot 設計（Shot 1: 走進來... Shot 2: 她坐下... 這種 = 廣告）
- 使用 `cinematic_studio_video_v2`（這個模型就是生成廣告感）
- 使用 `genre: cinematic` 或 `multi_shots: true`

### 標竿帳號（Benchmark）

分析以下帳號的日常影片風格後確立此 SOP：
- **@yua_mikami**（日本，Instagram/TikTok）
- **@asuka.kirara**（日本，Instagram）
- **@eimi0318**（日本，Instagram/TikTok）

**這些帳號日常影片的共同特徵**：
1. 單鏡頭，不剪輯，5–15 秒
2. 手機自拍角度，略高俯角
3. 展示身材（胸口、腰線、臀線）自然流露，不刻意擺姿勢
4. 表情自然，有時對鏡頭笑，有時低頭再抬頭
5. 背景簡單（浴室、飯店、家裡）
6. BGM 是現成流行歌，後製加入，不是影片生成時帶的音效

> **⚠️ 2026-08-05 數據驗證與修正**（完整分析見 `REELS_AND_STRUCTURE_SYSTEM.md`）
>
> 對競品 @sherry_digitalp510 的 30 支 Reels 做場景切點偵測 × 觀看數交叉比對，**第 1 點「單鏡頭不剪輯」獲得數據強力支持**：
>
> | | 平均切點 | 平均秒數 | 單鏡頭長度 | 平均觀看 |
> |---|---|---|---|---|
> | 前 8 名 | **3.0 刀** | 13.6 秒 | **5.79 秒** | 781,917 |
> | 後 8 名 | **5.9 刀** | 13.4 秒 | **3.84 秒** | 47,538 |
>
> 長度幾乎一樣，**差別在切點密度**。切 23 刀的快剪蒙太奇只有 5.7 萬觀看；完全不切的單鏡頭 14.7 秒拿到 74.6 萬。**畫面運動量不是差異因子**（14.0% vs 12.7%）。→ **正式訂為：預設 0–3 刀、單一鏡頭 ≥4 秒，禁止快剪蒙太奇。**
>
> **第 6 點需要修正**：競品 30 支裡有 **26 支使用她自己帳號的 `Original audio`（每支 audio_id 都不同）**，只有 4 支用授權曲，而**唯一一支用熱門 Nightcore 曲的排在倒數第二**。→ **不需要為了追熱門音檔調整內容**；BGM 用不用現成流行歌不是成效關鍵。
>
> **新增第 7 點——情境 > 美貌**：她觀看數前 3 名都不是「美女展示」，而是有情境、有第三方反應的微敘事（後座睡著＋標題點出 Uber 司機的反應／手扶梯上前方男子一再回頭／車內偷喝珍奶被抓到的三拍）。**情境必須由畫面演出來**——把故事做成文字字卡的那支只拿到 5.3 萬觀看。
>
> **新增第 8 點——不追畫質**：30 支裡 26 支是 720×1280，位元率 0.48–1.17 Mbps。手機原始檔的質感本身就是真實感的一部分。
7. 整體像是「隨手一拍」而非「精心製作」

---

## 完整四步驟流程

### Step 1：為每個 KOL 生成日常服裝 Start Frame

> ⚠️ 必須用**日常服裝**生成 start frame，不能用舞蹈服裝或宴會服裝。
> Start frame 的服裝會影響影片的服裝輸出。

```python
generate_image(
    model="soul_2",
    soul_id="<KOL_SOUL_ID>",
    prompt="[年齡] [國籍] woman, [臉部特徵], [身材描述], [髮型描述], "
           "[場景或背景], wearing [日常服裝], "
           "phone selfie angle from slightly above angled down toward face and chest, "
           "[natural cleavage visible from above angle, 若服裝允許], "
           "[背景描述], [光線描述], "
           "candid self-portrait feel, shot on iPhone front camera, "
           "half body shot showing face and chest, warm tones, film grain",
    aspect_ratio="9:16",
    count=2  # 生成兩張選一張
)
```

**自拍角度關鍵詞**（必須包含）：
```
phone selfie angle from slightly above angled down toward face and chest,
candid self-portrait feel, shot on iPhone front camera
```

**服裝選擇原則**：
| 場景 | 推薦服裝 |
|------|---------|
| 浴室自拍 | 黑色/白色細肩帶背心（no bra 感）、白色浴巾裹身 |
| 床上自拍 | 白色薄棉睡衣、領口微開或寬鬆 |
| 泳池 | 黑色比基尼上衣、一件式泳衣 |
| 飯店/家裡 | 緊身 crop top + 低腰短褲、白色絲質睡衣 |

**服裝禁忌**：
- ❌ 不能直接用舞蹈服裝的 start frame（pink bodycon、PU leather halter、gold metallic 等）
- ❌ 完全遮蓋身材的服裝（oversized T-shirt、flowy 長裙）
- ❌ 過度 revealing 導致 Higgsfield 過濾：belly dance bra、完全露腹的 sports bra midriff——這類服裝會讓生成任務直接 `status: "failed"`

---

### Step 2：Import Start Frame 為 Media

```python
media_import_url(url="<rawUrl_from_step1>")
# → 回傳 image_media_id
```

---

### Step 3：生成日常自拍影片

```python
generate_video(
    model="kling3_0",
    prompt="[年齡] [國籍] woman, [臉部特徵], [身材描述], [髮型描述], "
           "[場景描述], wearing [服裝], "
           "[動作描述：如 tilting head, looking at camera, running hand through hair], "
           "[鏡頭角度：phone selfie angle 或 overhead phone selfie angle from above], "
           "showing face and [chest/natural cleavage] naturally, "
           "[光線描述], "
           "single continuous shot, casual selfie feel, warm tones",
    aspect_ratio="9:16",
    duration=10,
    medias=[{"role": "start_image", "value": "<image_media_id>"}],
    sound="on"
)
```

**關鍵參數**：
| 參數 | 值 | 說明 |
|------|-----|------|
| `model` | `kling3_0` | 臉部鎖定單鏡頭，適合日常內容 |
| `medias role` | `start_image` | 鎖定臉部和身份 |
| `sound` | `on` | 帶入環境聲（後製可換 BGM） |
| `duration` | `10` | 10 秒，手機自拍的自然長度 |
| `multi_shots` | 不設定（預設 false） | 絕對不用多鏡頭 |

---

### Step 4：後製加入 BGM

1. 將生成的影片匯入 CapCut 或其他剪輯工具
2. 加入適合的流行歌曲作為 BGM（音量控制讓 BGM 不蓋掉環境聲）
3. 可在影片開頭或結尾加入細微的鏡頭晃動或旋轉感（模擬手持自拍）

---

## Prompt 模板（含占位符）

### Start Frame Prompt

```
[AGE]-year-old [NATIONALITY] woman, [FACE_FEATURES], [BODY_DESCRIPTION], [HAIR_DESCRIPTION],
standing/sitting/lying in [SCENE],
wearing [OUTFIT_DESCRIPTION],
phone selfie angle from slightly above angled down toward face and chest,
[natural cleavage visible from above angle — 只在服裝允許時加],
[BACKGROUND_DESCRIPTION], [LIGHTING_DESCRIPTION],
candid self-portrait feel, shot on iPhone front camera,
half body shot showing face and chest, warm tones, film grain
```

### 影片 Prompt

```
[AGE]-year-old [NATIONALITY] woman, [FACE_FEATURES], [BODY_DESCRIPTION], [HAIR_DESCRIPTION],
[SCENE_DESCRIPTION], wearing [OUTFIT_DESCRIPTION],
[ACTION_DESCRIPTION],
[CAMERA_ANGLE_DESCRIPTION],
[CLEAVAGE/BODY_DISPLAY — 描述要自然，不要太明確],
[LIGHTING_DESCRIPTION],
single continuous shot, casual selfie feel, warm tones
```

**動作描述範例（自然感）**：
- `tilting head slightly while looking at camera with soft smile`
- `slowly turning from side profile to face camera directly`
- `running hand through hair, then looking at camera`
- `looking down then raising gaze to camera`
- `lying on bed looking up at phone camera held above her`

---

## 自拍鏡頭動態規則

> ⚠️ 2026-07-07 用戶新增規則：日常自拍影片要有真實感，需要讓鏡頭有自然晃動或旋轉。

**在 Prompt 中加入動態描述**：
```
slight natural camera movement as if held by hand,
camera rotates slightly or pans during the shot for realistic selfie feel
```

**或描述她的動作讓鏡頭感覺在移動**：
```
she slowly turns and adjusts angle showing different profile
```

**注意**：kling3_0 的 prompt 控制鏡頭動態效果有限，主要靠描述她的動作（如轉身、撥髮）來製造鏡頭動態感。過度強調鏡頭晃動可能讓模型產生奇怪的視角跳動。

---

## 模型對比（日常影片）

| 模型 | 適合日常影片嗎 | 原因 |
|------|------------|------|
| `kling3_0` | ✅ **首選** | 單鏡頭，臉部鎖定（start_image），phone selfie 感自然 |
| `seedance_2_0` | ⚠️ 次選 | 更適合舞蹈（audio_references 音樂節拍同步）；日常也可以但沒特別優勢 |
| `cinematic_studio_video_v2` | ❌ **禁止** | 多鏡頭電影感，生成出來像廣告，完全不日常 |

---

## 已知問題

| 問題 | 說明 | 解法 |
|------|------|------|
| 用舞蹈 start frame 生成日常影片 | 服裝衝突，影片出來的服裝可能跑偏 | 必須先生成日常服裝 start frame，不能借用舞蹈 start frame |
| Start frame 服裝過度 revealing 導致 failed | 露腹、belly dance bra 等被像素過濾 | 使用 tank top、浴巾裹身、比基尼上衣（不露腹）等 |
| 影片鏡頭沒有自拍感 | kling3_0 預設是穩定鏡頭，沒有手持感 | 在 prompt 中加入動作描述（轉頭、撥髮）製造自然動態感 |
| BGM 不能直接嵌入 | kling3_0 的 sound:on 只帶環境音 | 後製（CapCut）加入 BGM |

---

## 6 個 KOL 日常自拍影片設定（2026-07-07 批次）

| KOL | 場景 | 服裝 | Start Frame Media ID | 影片 Job ID |
|-----|------|------|---------------------|------------|
| Iris Chen | 浴室，手機俯角，微微低頭看鏡頭 | 黑色細肩帶背心 | `b8078a7d` | `b68ac46c` |
| Yuna Kim | 飯店房間，從側面轉向鏡頭，展示身材比 | 白色緊身 crop top + 低腰牛仔短褲 | `9e7d8009` | `2aca7a9e` |
| Luna Tanaka | 床上仰拍，俯角自拍，看鏡頭微笑 | 白色薄棉睡衣，領口微開 | `81d7442e` | `c2cfc025` |
| Aaliya Rivera | 泳池邊，半身出水，撥頭髮，看鏡頭 | 黑色比基尼上衣 | `e6892cd0` | `d51676c3` |
| Camille Dupont | 臥室窗邊逆光，轉頭看鏡頭，展示側面輪廓 | 白色絲質睡衣 | `5c868b09` | `c70f6307` |
| Ananya Kapoor | 浴室出來，站鏡前，濕髮，毛巾裹身，看鏡頭 | 白色浴巾裹身，露鎖骨 | `d94c27c9` | `59dcbb98` |

---

## Start Frame 生成記錄（2026-07-07）

所有 start frame 使用 `soul_2` 模型 + 自拍角度 prompt，生成 2 張選 1 張。

| KOL | 兩張 Job ID | 已選 Job ID | 已選 Media ID |
|-----|-----------|------------|--------------|
| Iris Chen | `98d13de0`, `8e23ac81` | `98d13de0` | `b8078a7d` |
| Yuna Kim | `fd8b7c1d`, `1f4935eb` | `fd8b7c1d` | `9e7d8009` |
| Luna Tanaka | `970cf52f`, `7da38bb4` | `970cf52f` | `81d7442e` |
| Aaliya Rivera | `2bc0f0f7`, `7f56a6d4` | `2bc0f0f7` | `e6892cd0` |
| Camille Dupont | `f461c0af`, `4b0cc194` | `f461c0af` | `5c868b09` |
| Ananya Kapoor | `7797c1d9`, `1527bfbf` | `7797c1d9` | `d94c27c9` |

---

*建立日期：2026-07-07*
*適用平台：Higgsfield（透過 MCP 連接）*
