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

### 服裝原則
- Ananya：禁止寬鬆遮身的穿搭（如 flowy floral kurta + wide-leg trousers）；應使用瑜珈套裝、crop top、midriff co-ords 等展現身材的穿搭
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

### ✅ Step 1 — 最高優先（已完成）
為全部 6 個 KOL 新增 `## 視覺生成指南`（表情與肢體語言 + 服裝公式 + 鏡頭公式）。

---

### 🔲 Step 2 — 次高優先（尚未開始）

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

### 🔲 Step 3 — 補充優先（Step 2 完成後）

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

- [ ] **Ananya Kapoor** — 需要重新生成場景一（正確穿搭）和場景三（修正構圖多樣性）
- [ ] **Yuna Kim / Aaliya Rivera** — `KOL_TRAINING_SOP.md` 的狀態確認測試圖 approved 後改為 ✅
- [ ] **Aaliya Rivera `generation_notes.md`** — 尚未建立，需要補上（參考 `kols/camille-dupont/generation_notes.md` 的格式）

---

## 重要技術備忘

### Git 操作
- **一律用 Bash tool 執行 git 指令**（不要用 PowerShell）
- repo 本地路徑：`C:\Users\User\AppData\Local\Temp\claude\Virtual_KOL_Studio`
- 目前使用分支：`claude/kol-personality-training-9otdaw`
- user.email: `penny.huang@insight-software.com` / user.name: `Penny Huang`

### 檔案操作規則
- 用 Edit tool 修改檔案前，**必須先用 Read tool 讀取**
- 多個 KOL 的相同操作可以並行執行（同時 Read 6 個檔案，同時 Edit 6 個檔案）

### Higgsfield MCP
- `show_generations` → 取得完整 UUID（不要用短 ID）
- `job_display` → 顯示已生成的圖片
- `generate_image` with `model: soul_2` + `soul_id` 參數
- Higgsfield CloudFront 圖片在 Windows 本機可讀；雲端 session 需用 `raw.githubusercontent.com`

### 工作方式偏好
- 一次更新全部 6 個人格，不要一個個做
- 每個 Step 完成後 commit & push，再繼續下一步
- 不需要問確認就可以繼續下一個 Step，除非有需要用戶決策的事項
- 圖片生成完後再請用戶審閱，不要提前做過多假設
