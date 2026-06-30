# Claude Handoff Document

> **給下一個 Claude session 的交接文件。**
> 讀完這份文件後你應該能完整掌握這個專案的背景、已完成的工作、以及接下來要做什麼。

---

## 這個專案是什麼

**Virtual KOL Studio** — 一個虛擬 KOL（Key Opinion Leader）創作者工作室。

這個 repo 包含 6 個完整設計的虛構 KOL 人格。每個人格都有：
- 詳細的角色設定（個性、外型、生活背景、社交圈）
- 內容策略（帳號定位、發文方向）
- Benchmark 帳號（Instagram / TikTok / X）
- AI 圖像生成設定（Higgsfield Soul V2 的 soul_id）
- 視覺生成指南（表情、服裝、鏡頭公式）

這些人格被用來在社群媒體上運作，並透過 AI 工具生成圖片/影片素材。

---

## 6 個 KOL 人格

| KOL | 所在城市 | 定位 | Soul ID |
|-----|---------|------|---------|
| **Iris Chen** | 台北 | 台灣時尚/生活風格 | 見 `kols/iris-chen/profile.json` |
| **Luna Tanaka** | 京都 | 日本靜物/藝術/美學 | 見 `kols/luna-tanaka/profile.json` |
| **Ananya Kapoor** | 孟買 | 印度舞蹈/瑜珈/生活風格 | 見 `kols/ananya-kapoor/profile.json` |
| **Yuna Kim** | 首爾 | 韓國護膚/美妝/日常 | 見 `kols/yuna-kim/profile.json` |
| **Aaliya Rivera** | 洛杉磯 | 拉丁裔 LA 生活/穿搭/性感 | Soul ID: `97f5c6cd-1c0c-4432-83d0-dd42210ecada` |
| **Camille Dupont** | 巴黎 | 法式慢生活/美食/巴黎場景 | Soul ID: `f19dafcc-5bc8-4d8f-af1d-ee48084ac398` |

每個人格的完整資料在 `kols/<name>/character.md`。

---

## 重要操作規則（生成圖片時必讀）

### Higgsfield Soul V2
- 使用 `model: soul_2` + `soul_id` 參數
- Soul V2 **不會**自動繼承訓練照片的髮型 — **每次生成都必須在 prompt 裡說明髮色和髮型**
- 例如 Camille：`long straight blonde hair, natural honey golden color`

### 構圖多樣性規則（重要）
生成一組圖片時，**必須主動規劃每張的差異**：
1. 拍照角度與人物比例（wide shot / 3/4 身 / close-up / 仰角 / 俯角）
2. 濾鏡與相機感（film grain、色調偏向）
3. 不要每張都是同樣的 3/4 全身正面

Wide shot 雖然有場景感，但人物比例小、身材細節少 — **需要和特寫/半身鏡頭平衡**。

### ⚠️ 同一場景兩張圖構圖必須不同（所有人格適用）
同場景、同衣服、同環境，兩張圖的景別和角度必須明顯不同（例如 3/4 身 vs 臉部近景；廣角遠景 vs 特寫；正面 vs 側面）。

### ⚠️ 肢體動作多元化（所有人格適用）
**禁止單一擺拍正面看鏡頭。** 每張圖前先設定「這張照片的姿勢故事是什麼」，讓她在做某件事、有某種情緒，再寫 prompt。

- 姿勢：看向遠方、撩髮/調整衣服/拿杯子等中途動作被捕捉、側身或背影回眸、行走中側拍、坐姿變化（翹腳/前傾/下巴靠手）、與場景互動（靠牆/扶窗框/靠欄杆）
- 表情：自然微笑、若有所思、被逗笑的瞬間感、放鬆閉眼享受
- 構圖配合姿勢：廣角遠景時人物要有動態感；3/4 身時側身或斜角；近景時搭配表情或手部動作

### 服裝原則
- Ananya：禁止寬鬆遮身的穿搭（如 flowy floral kurta + wide-leg trousers）；應使用時尚展示曲線的穿搭（fitted wrap dress、crop top、midriff co-ords 等）
- 各 KOL 的詳細服裝公式見各自的 `character.md` → `## 視覺生成指南` → `服裝公式`

---

## 檔案結構

```
/
├── README.md
├── KOL_TRAINING_SOP.md          # 所有 KOL 的訓練狀態總覽表
├── BENCHMARK_ACCOUNTS.md        # 6 個 KOL 的 benchmark 帳號整體彙整
├── CLAUDE_HANDOFF.md            # 本文件
└── kols/
    ├── iris-chen/
    │   ├── character.md         # 完整人格描述（含視覺生成指南）
    │   ├── profile.json         # 結構化資料（含 soul_id）
    │   ├── generation_notes.md  # 生成筆記（提示詞規則、已生成清單）
    │   └── images/
    │       └── soul_test_v1/    # Soul V2 測試圖
    ├── luna-tanaka/             # 同上結構
    ├── ananya-kapoor/           # 同上結構
    ├── yuna-kim/                # 同上結構
    ├── aaliya-okonkwo/          # 同上結構
    └── camille-dupont/          # 同上結構（含兩批測試圖共 12 張）
```

---

## 已完成工作（截至 2026-06-30）

### Soul V2 訓練與測試圖生成

| KOL | 訓練狀態 | 測試圖 | 備註 |
|-----|---------|--------|------|
| Iris Chen | ✅ 完成 | ✅ 上傳 | |
| Luna Tanaka | ✅ 完成 | ✅ 上傳 | |
| Ananya Kapoor | ✅ 完成 | ✅ 上傳 | 有問題（見下方） |
| Yuna Kim | ✅ 完成 | ✅ 上傳 | |
| Aaliya Rivera | ✅ 完成 | ✅ 上傳 | |
| Camille Dupont | ✅ 完成 | ✅ 上傳（共 12 張，兩批） | |

**Ananya Kapoor 測試圖問題記錄（已存 `kols/ananya-kapoor/generation_notes.md`）**：
- 場景一：穿了 flowy floral kurta + wide-leg trousers → 禁止此類穿搭，以後不用
- 場景三：構圖角度雷同，一成不變
- 以上 6 張仍保留，但下一批生成時必須修正

### character.md 強化（6 個人格全部完成）

- [x] `## 社群平台 & Benchmark 帳號` — Instagram / TikTok / X 的 benchmark 表格 + 效仿原因
- [x] `## 她的帳號是什麼` — 全面改寫，從一句話變成詳細的帳號視覺願景描述（含 benchmark 引用）
- [x] `## 視覺生成指南` — 三個子章節：
  - **表情與肢體語言習慣**（含 prompt 關鍵詞）
  - **服裝公式**（場景對應穿搭 + 禁忌清單）
  - **鏡頭公式**（各內容類型的景別/角度/視線/背景 + 後製風格）

### BENCHMARK_ACCOUNTS.md

根目錄新增整體 benchmark 文件，6 個 KOL 各有 Instagram / TikTok / X 的帳號清單及效仿理由。

---

## 接下來要做的工作（按優先順序）

### ✅ Benchmark 帳號全面更新（已完成，2026-06-30）

**更新方向**：將 5 個 KOL 的 benchmark 帳號從明星/Idol 類型，全面替換為「性感身材展示型」的真實網紅帳號（依各自國籍/市場精準對標）。

**變更摘要**：
- **Iris Chen**：原帳號保留（用戶滿意），新增素材生成規則 preamble
- **Luna Tanaka**：換成日本 AV 女優 IG 帳號（@yua_mikami、@asukakiraran、@kana_momonogi、@eimi0318）
- **Ananya Kapoor**：換成印度性感身材展示網紅（@poonampandeyreal、@sherlynchopra）
- **Yuna Kim**：移除全部彩妝師帳號，換成韓國性感身材系（@euddeume_、@nana.un、@lucypark.official 等）
- **Aaliya Rivera**：精簡為核心性感身材帳號（@dollycastro、@danielabelmo、@alexisren）
- **Camille Dupont**：換成歐美性感白人女性帳號（@lanarhoades、@dangershewrote、@instavalentinanappi、@theevaelfie）

**新增全局規則**：所有素材生成（圖片+影音）必須參考該 KOL 的 Benchmark 帳號（詳見 `KOL_TRAINING_SOP.md` 及各 `character.md`）

---

### ✅ Step 1 — 最高優先（已完成）
為全部 6 個 KOL 新增 `## 視覺生成指南`（表情與肢體語言 + 服裝公式 + 鏡頭公式）。

---

### ✅ Step 2 — 次高優先（已完成，2026-06-30）

為全部 6 個 KOL 的 `character.md` 新增以下三個章節。**一次更新 6 個人格，完成後 commit & push，再繼續 Step 3。**

#### 2a. 簽名式重複內容系列
她固定會做的系列內容，有名字、有節奏、粉絲能預期：
- 系列名稱（例如「週三市場」「月亮系列」）
- 發文頻率（週更/雙週/月更）
- 固定出現的視覺元素是什麼
- 為什麼這個系列符合她的人格

#### 2b. 主場場景細節
她最常出現的地點的具體描述，不只是籠統的「巴黎咖啡廳」：
- 具體場所類型（老舊石牆咖啡廳？玻璃帷幕健身房？泳池邊的躺椅？）
- 燈光條件（早晨窗邊光？黃金時段戶外？暖燈餐廳？）
- 常出現的道具/背景元素
- 目的：讓生成圖片時有具體的場景參考

#### 2c. 後製風格具體描述（獨立章節）
目前各 KOL 的鏡頭公式裡有一列後製風格，但需要更完整的獨立描述：
- 具體的色調感覺（「像 VSCO A4」「像 iPhone 底片模式」「像 2000 年代雜誌掃描」）
- 高光/陰影/對比/飽和的具體設定感
- 皮膚處理方式（磨皮程度、膚色偏向）
- 什麼樣的圖讓人一眼認出是這個 KOL 的風格

---

### ✅ Step 4 — 文件修正（已完成，2026-06-30）

修正 4 個人格的文件，使其與當前人格設定一致：

- **Iris Chen**：全面改寫（`content_style.md`、`script_self_intro.md`、`edit_timeline_self_intro.md`、`profile.json`），從科技評測人格改為台北 IT Girl 生活風格。
- **Aaliya Rivera**（原資料夾名 `aaliya-okonkwo`）：改寫 `content_style.md`、`script_self_intro.md`、`edit_timeline_self_intro.md`，移除奈及利亞/Afrobeats 元素，改為 LA 拉丁裔設定。
- **Camille Dupont**：修正 `profile.json` 髮色（brown wavy → long straight honey blonde）；改寫 `edit_timeline_self_intro.md` 使其與 script（切洋蔥版）一致，移除原本的 tart 場景。
- **Yuna Kim**：修正 `content_style.md`，移除環形燈，改為冷白自然光（首爾窗邊日光）。

已 commit：`df004dd`（10 個檔案）

---

### ✅ Camille 自我介紹圖片 v1（已完成，2026-06-30）

生成 4 張通過圖片，存於 `kols/camille-dupont/images/self_intro_v1/`：

| 檔案 | 場景 | 狀態 |
|------|------|------|
| `shot01_kitchen_chop_onion.png` | 廚房切洋蔥，不看鏡頭 | ✅ 通過 |
| `shot02_taste_sauce.png` | 嚐醬汁，側臉 | ✅ 通過 |
| `shot03_cafe_terrace.png` | 咖啡廳露台，望向街道 | ✅ 通過 |
| `shot04_window_gaze.png` | 窗邊，下巴靠手，看窗外 | ✅ 通過 |

本批生成共 3 輪（Batch 1–3），各有問題需修正後才通過：
- Batch 1 問題：未指定服裝 → 只穿內衣；紅酒杯浮空
- Batch 2 問題：所有圖都看鏡頭、構圖雷同
- Batch 3：修正後通過（加 candid 關鍵詞、指定服裝、場景多元化）

**新規則詳情見 `kols/camille-dupont/generation_notes.md`**

---

### ✅ Step 3 — 補充優先（已完成，2026-06-30）

為全部 6 個 KOL 的 `character.md` 新增以下三個章節：

#### 3a. 情緒範圍
- 她能展現的情緒光譜（快樂、安靜、偶爾的脆弱或壞心情）
- 這些情緒在帳號上如何呈現（會發嗎？發的話什麼形式？）

#### 3b. 絕對不做的視覺行為
比服裝禁忌更廣的視覺 red line：
- 哪些姿勢/表情/場景永遠不出現
- 哪些構圖 or 後製風格是她的帳號不會有的

#### 3c. 光線配方
每個 KOL 的「光線公式」：
- 自然光的時間（黃金時段？早晨？陰天？）
- 室內人工光的類型（暖燈？霓虹？日光燈？）
- 特定光線效果（逆光剪影？窗邊漫射？強側光？）
- 她絕對不用的光線

---

## 其他待辦

### 影片生成（目前進行中）
- [ ] **Iris Chen** — `cafe_test_v1` 完成（3 支），下一步：製作其他場景日常影片（非自我介紹）
- [ ] **其他 5 個 KOL** — 影片生成尚未開始，待 Iris 工作流程穩定後依序執行

### 圖片生成
- [x] **Ananya Kapoor** — 場景一（孟買咖啡廳，深寶石藍 wrap dress）✅ 通過；場景三（Marine Drive，鏽紅 crop top + 白色闊腿褲）✅ 通過（2026-06-30）
- [ ] **Luna Tanaka / Yuna Kim / Aaliya Rivera** — 自我介紹圖片尚未生成

### 文件補齊
- [ ] **Iris Chen** — `character.md` 的 benchmark 帳號區塊需更新（現有的 4 個帳號都是靜音美學型，不符合 Iris 新的說話+多元內容方向）
- [x] **Luna Tanaka** — `edit_timeline_self_intro.md` 已存在 ✅
- [x] **Yuna Kim** — `edit_timeline_self_intro.md` 已存在 ✅
- [x] **Aaliya Rivera `generation_notes.md`** — 已補上測試圖記錄（2026-06-30）✅

### 其他
- [x] **KOL_TRAINING_SOP.md 狀態表** — 已全面更新至最新進度（2026-06-30）✅

---

## 影片生成技術規範（2026-06-30 確立）

### 工作流程

```
Step 1: Soul V2 生成 start frame 靜態圖（臉部鎖定）
Step 2: cinematic_studio_video_v2 動態化（多鏡頭）
Step 3: 後製疊加 BGM + 環境音（CapCut）
Step 4: （未來）疊加中文 VO（ElevenLabs 或 Azure TTS）
```

### 推薦模型：`cinematic_studio_video_v2`

這是目前測試結果最好的影片模型（Iris `cafe_test_v1` v3 通過）。

```
model: cinematic_studio_video_v2
multi_shots: true
multi_shot_mode: auto        ← 必須 auto，不能 custom（custom+空prompt會卡死）
genre: intimate
mode: pro
sound: on
aspect_ratio: 9:16
duration: 12                 ← 最短 10s，建議 12s
```

### Prompt 模板

```
Shot 1: [場景進入動作，全身或中景]
Shot 2: [主要行為，中景]
Shot 3: [特寫細節，手/道具/表情]
Shot 4: [收尾情緒鏡頭，側臉或望遠]
Shot on iPhone, warm soft grain, warm faded tones, no over-sharpening,
natural lighting, stable camera, feels like a real person filmed this.
```

### 影片生成注意事項

| 項目 | 規則 |
|------|------|
| 解析度 | **720p**（480p 太低，手機感靠 prompt 不靠降解析度） |
| 時長 | **12 秒**，最短不低於 10 秒 |
| 鏡頭穩定 | **禁止** `handheld`, `camera shake`, `motion blur`, `NOT tripod perfect` |
| 手機感 | 用 `shot on iPhone, warm soft grain, no over-sharpening` |
| 內容 | 必須有 3–4 個連續動作，有敘事起伏，不能只有一個動作 |
| multi-shot | `multi_shot_mode: auto`，把各鏡頭描述寫進主 prompt |

---

## 聲音生成技術限制（重要）

### Higgsfield TTS — 不適合中文 ❌

Higgsfield 的所有 preset 聲音都是英語聲音（Tallulah、Skye、Chloe 等西方名字）。
測試過 `minimax`、`seed_speech`、`elevenlabs` 三個引擎，全部結論：**聽起來像外國人說中文，語調、語氣完全不自然，不可使用。**

### 解決方案（尚未執行）

| 工具 | 狀態 | 說明 |
|------|------|------|
| **Azure TTS** | 需要 Azure 訂閱（目前無） | `zh-TW-HsiaoChenNeural` 是最接近台灣 22 歲女生的聲音 |
| **ElevenLabs** | 有免費額度但有限 | 支援中文 clone 聲音，月費後續考慮 |
| **暫時方案** | ✅ 目前採用 | 先做純視覺影片，聲音問題延後解決 |

### 聲音一致性機制（待執行）

每個 KOL 只需設定一次聲音 → 存入 `profile.json` 的 `voice_id` → 之後每支 VO 都用同一個 ID，聲音永遠一致。確定工具後再執行。

---

## KOL 內容方向更新：Iris Chen

### 原始設定 vs 更新後

**原始 benchmark 帳號**（@lalaochh、@syusyu21、@yuyustudio\_、@tzuyu\_hair）：
- 全部都是**靜音美學型**創作者——無 VO、無對鏡說話、純視覺 montage + BGM
- 這個風格不符合實際需求

**更新後的 Iris 內容方向**：
1. **日常剪輯影片**（多鏡頭，搭配不同場景和腳本，有時會說話）
2. **熱門短影音舞蹈**（偶爾跟跳 trending dance）
3. **純視覺美學 clip**（穿搭、街頭，無 VO，搭 BGM）

→ `character.md` 的 benchmark 帳號區塊需要更換成符合這個多元方向的帳號（**待辦**）。

---

## 工作流程規範（用戶要求）

### 每個段落結束後的固定動作

每完成一個工作段落，**必須執行以下步驟再繼續**：

1. **全檔案一致性確認**：push 前必須確認以下所有文件都已同步到最新狀態，不允許只改其中一個：
   - `CLAUDE_HANDOFF.md`（整體進度、待辦、已完成工作）
   - `KOL_TRAINING_SOP.md`（狀態總覽表、新 Session 待辦清單）
   - 涉及的各 KOL `generation_notes.md`（生成記錄）
   - 涉及的各 KOL `character.md` / `profile.json`（如有修改）
   > ⚠️ 不同文件之間的狀態描述若有衝突，Claude 在下一個 session 讀取時會產生錯誤判斷，執行出不符合預期的結果。這是嚴重的工作流程問題。
2. **更新 CLAUDE_HANDOFF.md**：把本段落的決策、規則、待辦都記錄進來
3. **Git commit & push**：所有變更一次推上去

### 檔案一致性原則

**每次更新人格設定，必須同步檢查並更新以下所有檔案**：
- `character.md`
- `profile.json`
- `content_style.md`
- `script_self_intro.md`
- `edit_timeline_self_intro.md`
- `generation_notes.md`（如果存在）

**已知衝突案例**：Aaliya Rivera（資料夾名稱仍是 `aaliya-okonkwo`，人格已改為 LA 拉丁裔）。這是人格中途更換但只有部分檔案同步的結果。每次更新必須全檔案掃描，不能只改一個檔案。

---

## 重要技術備忘

### Git 操作
- **一律用 Bash tool 執行 git 指令**（不要用 PowerShell）
- repo 本地路徑：`/Users/huangpinxuan/Virtual_KOL_Studio`
- 目前使用分支：`claude/kol-personality-training-9otdaw`
- user.email: `penny.huang@insight-software.com` / user.name: `Penny Huang`

### 檔案操作規則
- 用 Edit tool 修改檔案前，**必須先用 Read tool 讀取**
- 多個 KOL 的相同操作可以並行執行（同時 Read 6 個檔案，同時 Edit 6 個檔案）
- **每個段落結束都要做全檔案一致性確認再 push**

### Higgsfield MCP
- `show_generations` → 取得完整 UUID（不要用短 ID）
- `job_display` → 顯示已生成的圖片/影片
- `generate_image` with `model: soul_2` + `soul_id` 參數
- `generate_video` with `model: cinematic_studio_video_v2` → 影片生成首選
- Higgsfield CloudFront 圖片在 macOS 本機可直接 `curl` 下載

### 工作方式偏好
- 一次更新全部 6 個人格，不要一個個做
- 每個 Step 完成後 commit & push，再繼續下一步
- 不需要問確認就可以繼續下一個 Step，除非有需要用戶決策的事項
- 圖片/影片生成完後再請用戶審閱，不要提前做過多假設
- **每個段落結束 = 一致性檢查 + 更新 CLAUDE_HANDOFF.md + push，這是固定流程**
