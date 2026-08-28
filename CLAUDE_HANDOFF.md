# Claude Handoff Document

> **給下一個 Claude session 的交接文件。**
> 讀完這份文件後你應該能完整掌握這個專案的背景、已完成的工作、以及接下來要做什麼。

---

## ⚠️ 專案治理原則（每次 session 開始必讀，優先於下面所有歷史記錄）

### 1. 人設是活生生的人，不是硬性規則的集合（2026-08-06 起訂，2026-08-07 全面落實）

每位 KOL 的 `character.md` 裡描述的風格、穿搭、場景、情緒範圍，都是她**預設、多數時候**的樣子，用來建立清楚的識別度——**不是她絕對不能跨出的框**。真人會有例外、會嘗試新風格、會在不同場合展現不同的自己。寫人設或審核生成內容時：

- **不要用「絕對不會」「永遠不出現」「禁止」這類詞去鎖死風格/穿搭/場景/情緒選擇**。改寫成「主軸風格＋允許例外」——即「這是她多數時候的樣子，不是她的招牌，但不是不可能」。各 `character.md` 裡的「視覺行為光譜」章節就是這個寫法的範本。
- **唯一真正不能鬆動的界線是內容尺度**：SFW、不露骨、不涉及未成年化、不做真人身分冒用。這條對所有人設一律適用，不分風格設定，且必須維持絕對——這不是風格偏好，是內容安全底線。
- **2026-08-07 教訓**：2026-08-06 的 commit `21b8ebfd` 已經把這個原則寫入 6 位人設，但漏改了 Mia Huang 的「不出現的視覺元素」章節，且從未套用到 Coco Wu、Sophia Tseng、Rainie Hsu、Vicky Lin。結果是：舞蹈克隆 R9 案例裡，Sophia Tseng 的驅動片服裝（貼身比基尼）直接撞上她 `character.md` 裡「不出現：貼身緊繃的 bodycon」這條硬性描述，逼著 Claude 在生成階段做了一次原本不必要的服裝改寫。**教訓是：發現規則後要把所有相關檔案的舊敘述都改掉，不能只加一條新規則、放著舊的硬性語言不管**——不然新 session 或審核時還是會讀到那條硬性語言，繼續產生衝突。目前 11 位人設的 `character.md` 已於 2026-08-07 全面檢查並改寫完成。

### 2. 文件衝突時的判斷依據：以最新修改的檔案為準，但要主動修，不要只依賴這條規則

如果讀到兩份文件（例如 `character.md` 跟這份 `CLAUDE_HANDOFF.md`，或新舊 session 留下的記錄）對同一件事的敘述互相矛盾，**以 git 記錄裡最近一次修改該內容的檔案為準**（`git log -1 --format=%ai -- <path>` 可查）。但這條規則是**事後排查用的判斷依據，不是長期共存的解法**——發現衝突之後，應該直接把舊檔案裡過時/衝突的敘述改掉或補齊，而不是永遠留著矛盾、每次都要靠這條規則去猜哪個是對的。舊有、過時的敘述如果沒有被清掉，會一直被新 session 讀到，反覆造成同樣的衝突。

---

## 這個專案是什麼

**Virtual KOL Studio** — 一個虛擬 KOL（Key Opinion Leader）創作者工作室。

這個 repo 包含 11 個完整設計的虛構 KOL 人格（原始 6 位 + 2026-07-24 新增的台灣 5 位）。每個人格都有：
- 詳細的角色設定（個性、外型、生活背景、社交圈）
- 內容策略（帳號定位、發文方向）
- Benchmark 帳號（Instagram / TikTok / X）
- AI 圖像生成設定（Higgsfield Soul V2 的 soul_id）
- 視覺生成指南（表情、服裝、鏡頭公式）

這些人格被用來在社群媒體上運作，並透過 AI 工具生成圖片/影片素材。

---

## 11 個 KOL 人格

### 原始 6 位

| KOL | 所在城市 | 定位 | Soul ID |
|-----|---------|------|---------|
| **Iris Chen** | 台北 | 台灣時尚/生活風格 | 見 `kols/iris-chen/profile.json` |
| **Luna Tanaka** | 京都 | 日本靜物/藝術/美學 | 見 `kols/luna-tanaka/profile.json` |
| **Ananya Kapoor** | 孟買 | 印度舞蹈/瑜珈/生活風格 | 見 `kols/ananya-kapoor/profile.json` |
| **Yuna Kim** | 首爾 | 韓國護膚/美妝/日常 | 見 `kols/yuna-kim/profile.json` |
| **Aaliya Rivera** | 洛杉磯 | 拉丁裔 LA 生活/穿搭/性感 | Soul ID: `97f5c6cd-1c0c-4432-83d0-dd42210ecada` |
| **Camille Dupont** | 巴黎 | 法式慢生活/美食/巴黎場景 | Soul ID: `f19dafcc-5bc8-4d8f-af1d-ee48084ac398` |

### 新增 5 位（2026-07-24，台灣籍）

> **⚠️ 2026-08-05**：原本這裡還有第 6 位「Zoe Lai 賴柔伊」，因人設調整過程中反覆出現臉部辨識問題（跟其他角色撞臉、眼型修正後仍不理想），使用者決定不建立此人格，`kols/zoe-lai/` 已從 repo 完整刪除。

| KOL | 所在城市 | 定位 | Soul ID |
|-----|---------|------|---------|
| **Vicky Lin** 林薇淇 | 高雄 | 健身 / 重訓 / 健身正妹 | 未訓練——臉部參考圖第一輪試跑因偏向健美選手體態被否決並移除，外型描述已修正，尚未重新生成 |
| **Coco Wu** 吳可可 | 台中 | 校園甜心 / 宿舍生活 | 未訓練 |
| **Rainie Hsu** 許雷妮 | 台北 | 派對女王 / 夜生活 | 未訓練 |
| **Sophia Tseng** 曾詩妃 | 台北信義 | 貴婦名媛 / 精品生活 | 未訓練 |
| **Mia Huang** 黃米亞 | 新竹 | 直播主播 / 電競生活 | 未訓練 |

> ⚠️ **新流程規則（2026-07-24 新增）**：臉部參考圖生成後，必須停下來等使用者實際看過並明確確認滿意，才可以送進 Soul 訓練——不可以在同一輪自動接著做完。詳見 README.md「新增 KOL 流程」步驟 6。

每個人格的完整資料在 `kols/<name>/character.md`。

---

## 2026-07-24 Session 摘要（給下一個 Claude session 讀）

這次 session 做了大量結構性變更，如果你在讀這份文件時發現跟其他文件（`README.md`、`KOL_TRAINING_SOP.md`）對不上，以最新的那次 git commit 為準。這次 session 的工作內容：

1. **新增 6 位台灣籍 KOL**（Vicky Lin、Coco Wu、Rainie Hsu、Sophia Tseng、Mia Huang、Zoe Lai）——各自建立 `profile.json` / `character.md` / `content_style.md` / `generation_notes.md`，尚未生成任何素材、尚未訓練 Soul。
2. **全部 12 位補齊標準化身材數據**：`profile.json` 新增 `identity.appearance.measurements`（身高/體重/三圍/罩杯/腿長/比例備註），`kols/schema.json` 同步更新。
3. **全部 12 位補齊帳號註冊相關欄位**：`social.display_name`（公開顯示名稱）、`social.bio`（簡短、保留神秘感，不是落落長自介）、`social.account_username`（信箱/平台註冊用，刻意做出不同的命名慣例，避免看起來像同一批次建立的水軍帳號）、`identity.date_of_birth`（跟 age 對齊，用於平台年齡驗證）、`social.creator_category`（平台創作者類別）。
4. **建了兩個可重複使用的 Workflow**（`.claude/workflows/`）：
   - `kol_content_qa_pipeline.js` — 生成前 prompt 審核 → 生成（圖片/影片）→ 生成後品質審核（重試機制）→ 核准/待人工後製的素材上傳 Google Drive → 更新 generation_notes.md。目前只跑過零成本空跑驗證，還沒有實際跑過真的生成。
   - `weekly_content_planner.js` — 單一 KOL 的每週企劃，會比對 `kols/{id}/content_history.json`（如果存在）避免場景重複，經審核 agent 檢查支柱比例/文案雷同/checklist 後才定案。
5. **`SEXY_SCENE_LIBRARY.md` 新增「降低 AI 感的技術要點」章節** + 生成前檢查清單（皮膚質感/裝置規格/混合光源/背景雜物/服裝完整/運動類角色防健美選手化），12 位共用。
6. **重大教訓（務必記住）**：Vicky Lin 的第一輪臉部參考圖試跑，因為 `character.md`/`profile.json`/`generation_notes.md` 裡寫了「銳利分明的五官⋯不是圓臉可愛系」+「肌肉線條、腹肌明顯」，實際生成結果變成健美選手/男性化體態，使用者明確否決。已經：(a) 停止該次背景任務、刪除 6 張被否決的圖片（Soul 訓練從未啟動，只浪費了圖片生成額度）；(b) 重寫 Vicky Lin 的外型描述為「漂亮性感健身網紅，絕對不是健美選手」；(c) 同步加強 Zoe Lai（另一個運動系角色）的描述；(d) 在 `SEXY_SCENE_LIBRARY.md` 加入永久性防呆檢查項目，未來任何運動類角色都要檢查這一條。
7. **修正「內容太單一無聊」的問題**：新 6 位原本完全照 studio 的 6 支柱模板打造，每個支柱都硬套進單一人設（例如 Vicky 的「居家」支柱只有練後癱沙發），沒有社交圈、沒有跟人設無關的生活。已比照原始 6 位的格式，幫新 6 位都加上「## 社交圈」（有名有姓的朋友/家人/寵物）和 2-3 個不佔權重的額外生活主題，並把既有 6 支柱裡的場景範例做多樣化。**六大支柱的權重數字完全沒有變動**，這只是幫「人」補血肉，不是改生成排程結構。
8. **Metricool API 串接研究結論**：Metricool 官方有發布 MCP Server（`github.com/metricool/servers`），但這個工作環境是雲端 session，不是本機安裝 Claude Desktop 那種可以直接掛 stdio MCP 的情境，所以無法直接用連接器。替代方案：Metricool 本身是標準 REST API（`X-Mc-Auth` header + `userId`/`blogId`），可以直接用 Bash + curl 呼叫，不需要等連接器裝好——但需要使用者先在各平台建好 KOL 的社群帳號、拿到 Metricool 的 API Token 才能實際測試。
9. **新增強制規則**：臉部參考圖生成完畢後，**必須停下來等使用者確認滿意才能送進 Soul 訓練**，不可以自動接續執行（見 README.md「新增 KOL 流程」步驟 6）。

新 6 位目前狀態：全部**未訓練**，沒有 images/videos 資料夾，`generation_notes.md` 裡的批次都明確標示 PENDING（沒有捏造任何 soul_id 或生成紀錄）。下一步是重新生成 Vicky Lin 的參考圖（用修正後的描述）並走過人工確認關卡。

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
- Ananya：她的招牌穿搭是展示曲線的款式（fitted wrap dress、crop top、midriff co-ords 等），寬鬆遮身的穿搭（如 flowy floral kurta + wide-leg trousers）不是她的主軸，但不是絕對禁止——家族場合或特定情境穿上也合理（2026-08-06 更正，見上方「人設哲學更正」）
- 各 KOL 的詳細服裝公式見各自的 `character.md` → `## 視覺生成指南` → `服裝公式`

---

## 檔案結構

```
/
├── README.md
├── KOL_TRAINING_SOP.md          # 所有 KOL 的訓練狀態總覽表
├── BENCHMARK_ACCOUNTS.md        # 原始 6 位 KOL 的 benchmark 帳號整體彙整（新 6 位不採用此法）
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

## 已完成工作（截至 2026-07-03）

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

#### 3b. 視覺行為光譜（原稱「絕對不做的視覺行為」，2026-08-06 已更正）
比服裝公式更廣的視覺傾向，描述**她的主軸風格／簽名感**：
- 哪些姿勢/表情/場景是她的招牌、多數時候會出現
- 哪些構圖 or 後製風格是她的帳號少見的

#### 3c. 光線配方
每個 KOL 的「光線公式」：
- 自然光的時間（黃金時段？早晨？陰天？）
- 室內人工光的類型（暖燈？霓虹？日光燈？）
- 特定光線效果（逆光剪影？窗邊漫射？強側光？）
- 她的光線範圍之外——少用的光線類型

> **⚠️ 2026-08-06 人設哲學更正（重要，套用新 KOL 時務必遵守）**：使用者指出 3a–3c 原本的寫法（「絕對不會有」「永遠不出現」「絕對不用」）把每個人設寫得太死。真人 KOL 的素材理應出現在各種環境、服裝、光線裡，不可能永遠鎖在單一形象——這正是這幾個月拆解競品 @sherry_digitalp510（見 `COMPETITOR_sherry_digitalp510.md`、`WARDROBE_SYSTEM.md`）得到的核心結論：造型與地點必須獨立於人設之外自由輪替，C 級「完全不美的日常」場景才是讓帳號讀起來像真人的關鍵。
> **正確做法**：先定調一個**主軸風格**（例如：遊戲主播、時尚博主、學生網紅），描述她多數時候、預設會出現的樣子——這部分維持詳細具體，仍然有用。但不要把「主軸風格之外」的一切寫成絕對禁止；改成「不典型／少見，但不是不可能」，讓她可以在合理情境下偶爾跳出框架，就像真人一樣。
> **唯一維持真正硬性的界線**：內容尺度（SFW，不露骨、不涉及未成年化、不冒用真實公眾人物）。這條不受本次更正影響，任何人設都不能鬆動。
> 已依此原則重寫 6 位第一代人格（Iris/Luna/Ananya/Yuna/Aaliya/Camille）的 `character.md` 對應章節，未來新增 KOL 或修訂既有人設時，3a–3c 一律套用這個「主軸風格＋允許例外」的寫法，不要再寫「絕對」「永遠」「禁止」這類詞。

---

## 影片生成狀態總覽（截至 2026-07-07）

### 舞蹈影片（seedance_2_0）

| KOL | 版本 | 服裝 | 音樂 | Job ID | 狀態 |
|-----|------|------|------|--------|------|
| Iris Chen | dance_v1 | 黑色 crop top + 騎車短褲 | 越南鼓 | `1b0aee3d` | ✅ 批准 |
| Iris Chen | dance_v2 | 黑色 crop top + 騎車短褲 | 越南鼓 | `1b767b3b` | ✅ 保留 |
| Iris Chen | dance_v3 | 淡藍色 V 領洋裝 | Sugar on my tongue | `3d3ac1b2` | ✅ 批准 |
| Iris Chen | dance_v4 | 淡藍色 V 領洋裝 | AI 生成（generate_audio:true 測試） | `dc8c2f4d` | ❌ 臉部差，結論：AI 音樂無改善 |
| Iris Chen | dance_v5 | 淡藍色 V 領洋裝 | AI 生成（第二次測試） | `1d60614a` | ❌ 卡點無改善，結論確認 |
| Yuna Kim | dance_v1 | 粉色 bodycon dress | Pump It Up | `7194b553` | ✅ 保留 |
| Yuna Kim | dance_v2 | 粉色 bodycon dress | Pump It Up | `42e42771` | ✅ 保留 |
| Aaliya Rivera | dance_v1 | rust orange ruched bodycon | 蟹二搖 | `2ccf4760` | ✅ 完成（待確認） |
| Luna Tanaka | dance_v1 | black PU leather halter dress | TikTok 卡點 | `322a8d14` | ✅ 完成（待確認） |
| Camille Dupont | dance_v1 | gold metallic deep-V bodycon | TikTok 卡點 | `34337f72` | ✅ 完成（待確認） |
| Ananya Kapoor | 所有嘗試 | 多次失敗 | — | 見 generation_notes | ❌ start_image revealing 被過濾 |

### 日常自拍影片（kling3_0）— 2026-07-07 新增

> 完整 SOP 見 `DAILY_VIDEO_SOP.md`。

| KOL | 場景 | 服裝 | Start Frame Media ID | 影片 Job ID | 狀態 |
|-----|------|------|---------------------|------------|------|
| Iris Chen | 浴室，俯角自拍，微微低頭 | 黑色細肩帶背心 | `b8078a7d` | `b68ac46c` | ✅ 批准 |
| Yuna Kim | 飯店，側面轉正面展示身材 | 白色 crop top + 低腰牛仔短褲 | `9e7d8009` | `2aca7a9e` | ✅ 批准 |
| Luna Tanaka | 床上仰拍，俯角自拍 | 白色薄棉睡衣 | `81d7442e` | `c2cfc025` | ✅ 批准 |
| Aaliya Rivera | 泳池邊，半身出水，撥頭髮 | 黑色比基尼上衣 | `e6892cd0` | `d51676c3` | ✅ 批准 |
| Camille Dupont | 臥室窗邊逆光，轉頭看鏡頭 | 白色絲質睡衣 | `5c868b09` | `c70f6307` | ✅ 批准 |
| Ananya Kapoor | 浴室，濕髮，毛巾裹身 | 白色浴巾，露鎖骨 | `d94c27c9` | `59dcbb98` | ✅ 批准 |

### 圖片生成
- [x] **Ananya Kapoor** — 孟買咖啡廳（深寶石藍 wrap dress）✅；Marine Drive（鏽紅 crop top）✅（2026-06-30）
- [ ] **Luna Tanaka / Yuna Kim / Aaliya Rivera** — 自我介紹圖片尚未生成

### 文件補齊
- [ ] **Iris Chen** — `character.md` benchmark 帳號需更新（現有 4 個帳號是靜音美學型，不符合新方向）
- [x] **KOL_TRAINING_SOP.md 狀態表** — 已全面更新至最新進度（2026-06-30）✅

---

## 舞蹈影片技術規則（2026-07-06 新增）

> 以下規則從 Yuna Kim / Aaliya / Luna / Ananya / Camille 舞蹈影片生成中學到，所有 KOL 適用。

### 絕對必要參數（每次必確認）

| 參數 | 正確值 | 錯誤後果 |
|------|--------|---------|
| `generate_audio` | `False` | AI 自動生成背景音效，蓋掉 audio_reference，舞蹈對著錯誤音樂跑 |
| prompt 含 `single continuous shot no camera cuts` | 必須有 | 鏡頭一直切換 |
| prompt 含 `centered in frame, staying within frame boundaries at all times` | 必須有 | 黑邊出現 |
| start_image 服裝 | 非 revealing（無肚皮露出、無 bra top） | 生成 status: "failed"（非 nsfw） |

### NSFW 觸發詞（避免）

- `sexy expression` → 改用 `confident sensual energy`
- `sensual isolation`
- `snaps hips hard`
- `chest bouncing/jiggling`（直接描述）→ 可用 `chest bounce and jiggle physics`

### 背景規則

- **禁止 mirror**：背景有鏡子 → 模型產生反射鏡頭，看起來像鏡頭切換

### generate_audio: true 測試結論（2026-07-06）

**測試**：用 Iris Chen（job `dc8c2f4d` 和 `1d60614a`）測試 AI 生成音樂是否能讓卡點更精準。  
**結果**：卡點效果完全相同，沒有改善。  
**結論**：永遠使用上傳熱門音樂 + `generate_audio: False`。

### Ananya Kapoor 特殊問題

start_image 含有 revealing 服裝（belly dance costume、crop top showing midriff）會導致 `status: "failed"`（非 `status: "nsfw"`）。這是像素層級的影片生成前處理過濾，需使用保守服裝的 start_image。

---

## 影片生成技術規範（2026-07-07 更新）

### 內容類型

目前確立三類影片生成方向：

1. **日常自拍影片**（kling3_0，手機自拍感，單鏡頭）→ 詳見 `DAILY_VIDEO_SOP.md` ⭐ **最重要**
2. **TikTok 舞蹈影片**（seedance_2_0，音樂同步）→ 詳見 `DANCE_VIDEO_SOP.md`
3. **多鏡頭電影感影片**（cinematic_studio_video_v2）→ **已確認不適合日常內容，不推薦**

---

### 模型對比表（完整版）

| 模型 | 臉部鎖定 | 多鏡頭 | 音樂同步 | 最大時長 | 最適用場景 |
|------|---------|--------|---------|---------|-----------|
| `kling3_0` | ✅ start_image | ❌（非自動） | ✅ sound:on | 15s | **日常自拍影片（首選）**、親密場景、單鏡頭 |
| `seedance_2_0` | ✅ start_image | ❌ | ✅ audio_references | 15s | **舞蹈影片（首選）** |
| `cinematic_studio_video_v2` | ❌（會漂移） | ✅ multi_shots | ✅ sound:on | 12s | 多鏡頭電影感 — **不適合日常內容，會生成廣告感** |
| `soul_2` | ✅ soul_id | N/A | N/A | N/A | 僅用於靜態 start frame 生成 |

**⚠️ 重要**：`soul_id` 只能用於 `soul_2` 靜態圖片生成，**不能用於任何影片生成**。影片生成的臉部鎖定靠 `start_image` 參數。

**⚠️ cinematic_studio_video_v2 教訓**：用此模型生成日常影片時，因為是多鏡頭敘事式，產出的感覺像廣告，完全不符合 KOL 日常自拍的要求。正確選擇是 `kling3_0` 單鏡頭。

---

### ❌ cinematic_studio_video_v2 不適合日常內容（重要教訓）

**問題**：cinematic_studio_video_v2 的 multi_shots 特性讓它天生就是「電影感敘事」，生成的影片有多個鏡頭切換、有劇情arc，看起來像品牌廣告。

**解決**：日常自拍內容一律用 `kling3_0` 單鏡頭。cinematic_studio_video_v2 僅保留給有特別需要多鏡頭電影感的少數場景。

---

### 日常自拍影片：`kling3_0`（2026-07-07 確立）

```
model: kling3_0
medias: [{"role": "start_image", "value": "<image_media_id>"}]
sound: on
aspect_ratio: 9:16
duration: 10
```

**Prompt 原則**：
- 描述單一場景和自然動作，不要描述多個鏡頭
- 包含 `phone selfie` 或 `overhead selfie angle` 角度描述
- 包含 `single continuous shot, casual selfie feel`
- 讓她有自然的動態（轉頭、撥髮、低頭再抬頭）製造真實手持感

詳細 SOP 見 `DAILY_VIDEO_SOP.md`。

---

### 舞蹈影片：`seedance_2_0` 完整工作流程

> 完整 SOP 見 `DANCE_VIDEO_SOP.md`

**五步驟摘要**：

```
Step 1: media_upload → curl PUT → media_confirm → audio_media_id
Step 2: soul_2 生成 start frame（THREE QUARTER SHOT, mid-thigh up, no shoes）
Step 3: media_import_url（rawUrl → image_media_id）
Step 4: seedance_2_0 生成（start_image + audio_references + generate_audio=False）
Step 5: CapCut 後製（拖入 mp3，對齊開頭，導出）
```

**關鍵注意**：
- `audio_references` 控制動作節拍同步，但**不嵌入音樂**，必須後製加入
- `generate_audio=False` 必須關閉，否則 AI 音效會蓋掉節拍同步效果
- THREE QUARTER SHOT（mid-thigh up, no shoes）避免腿部截斷問題

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

---

## 2026-08-07 進度記錄與待辦（使用者要求暫停點）

### 這次 session 完成的事

1. **人設哲學鬆綁**（已 push 到 `main`）：使用者指出 6 位人格（Iris/Ananya/Camille/Luna/Yuna/Aaliya）+ Mia Huang 的
   `character.md` 把服裝/場景/光線/表情寫成絕對禁止（「絕對不會有」「永遠不出現」「絕對不用」），不符合「像真人」的設計目標。
   已全部改寫成「主軸風格／招牌傾向，多數時候如此，但不是不可能」的框架，唯一維持真正硬性的界線是內容尺度（SFW、
   成年角色設定、不冒用真實公眾人物）。同步更正了本文件 3b/3c 段的範本指令（原文就是造成這個問題的源頭），避免未來
   新增角色再重複同樣的錯誤。詳見各角色 `character.md`／`content_style.md` 的對應章節。
2. **舞蹈批次 R1/R2 連結↔描述對調修正**：逐一重新下載並目視核對 GitHub Issue #3 的 R1–R8 全部驅動片後，發現最早
   分析時 R1、R2 的連結和文字描述被寫反了。已修正為：`DPWE2eqEVJ-`（水手服天台手勢舞）→ Mia Huang；
   `C3kMsJ1PtPH`（削肩居家性感風）→ Luna Tanaka。R3（Zoe Lai 已停用）改分配給 Vicky Lin。R4–R8 核對皆正確。
3. **Luna Tanaka R1、Mia Huang R1 兩支舞蹈影片已完整跑完 Method B 全流程**（Step 1–8，見各自
   `generation_notes.md` 對應章節），已 push 到 `main`。過程中發現並修正一個新 bug：**Motion Control 的驅動片
   輸入若保留 Instagram 原始 VP9 編碼會反覆失敗且無錯誤訊息**，已寫進 `DANCE_CLONE_SOP.md` Step 2 為必查項目。
4. `DANCE_CLONE_SOP.md` Step 4 的起始畫面生成預設從 `count=2` 改為 `count=1`（避免生兩張選一張浪費成本）。

### 待辦（下一個 session 或下一輪對話接續）

- **R3–R8 六支舞蹈影片尚未開始生成**（GitHub Issue #3「已分配」區塊可查目前對應）：
  - R3 → Vicky Lin（婚紗禮服快手勢舞，試衣間場景）
  - R4 → Coco Wu（黑色蕾絲高領+牛仔短褲，夜間街拍）
  - R5 → Rainie Hsu（桃紅貼身crop top+牛仔短褲，戶外白天）
  - R6 → Iris Chen（黑色蕾絲吊帶睡裙，室內）
  - R7 → Yuna Kim（白色crop top+牛仔短褲，室內走廊）
  - R8 → Sophia Tseng（白色長袖crop top+黑色運動褲，越南街頭）
  - 流程照 `DANCE_CLONE_SOP.md` Method B 全走一次：下載驅動片 → **先確認 H.264 編碼** → performance-director
    + emotion-director 出時間軸分析 → 生成起始畫面（`count=1`）→ Motion Control → 若無聲則手動混音 → QA 抽幀 →
    寫 `generation_notes.md` → commit push → 更新 Issue #3
- **當前分支狀態**：`main` 與 `claude/kol-dance-video-workflow-t57kou` 目前同步（都在 `555b4e5`），沒有落後的
  commit 需要補推。下次直接在 `main` 或此 feature branch 上繼續即可，不需要額外合併動作。
- 兩支已完成的影片音軌都是驅動片原始配樂，**未取得商用授權**，8 支全部做完後、真正要對外發佈前，需統一處理配樂授權
  （見 `DANCE_CLONE_SOP.md` Step 7）。

---

## 2026-08-07 進度更新（延續上面「進度記錄與待辦」，同日 session 後段，已 push 到 `main`）

### 這段完成的事

1. **R1–R8 + IG1 全部完成生成**（Step 1–8），詳見各 KOL `generation_notes.md`，GitHub Issue #3 已同步標記完成。
2. **使用者把最初提供的 18 支模板影片全部上傳**（先前只有 8 支能用 `yt-dlp` 抓到）。依檔名內嵌的 Instagram shortcode
   逐一比對，確認 R1–R8 對應這 18 支裡的哪 8 支，其餘 10 支編為 **R9–R18**，寫入 GitHub Issue #3「已分配」區塊。
3. **R9–R18 內容逐支抽幀目視核對**，發現多支跟隨機分配到的 KOL 人設調性有明顯落差（尺度、風格能量都不合），改為
   **依內容本身的調性重新指定 KOL，刻意不要求平均分配**（使用者明確同意這個做法）。目前分配：
   - `sophia-tseng`：R9、R11
   - `rainie-hsu`：R10、R14
   - `coco-wu`：R12、R13
   - `iris-chen`：R15、R18
   - `luna-tanaka`：R16、R17（兩支都是同一位真人網紅「深田えいみ」，剛好是 Luna 自己 IG Benchmark 表列的帳號）
   - `mia-huang`、`vicky-lin`、`yuna-kim`：這批完全沒分配到——不是遺漏，是這 10 支內容跟這三位人設不合，
     已在 Issue #3 寫明原因
   - 詳細改分配理由見 GitHub Issue #3 2026-08-07 補充 3／補充 4
4. **`DANCE_CLONE_SOP.md` 新增人工核准關卡規則**：Step 4 起始畫面生成後必須停下來給使用者看，核准後才能進 Step 5
   Motion Control——這件事之前 R1/R4/R5/R8 實際執行時都有做，但沒寫成文字規則，這次補上（見文件開頭「怎麼觸發」
   補充段落 + Step 4 段落）。
5. **人設哲學鬆綁「補完」**：2026-08-06 那次修正（上面第 1 條記錄的那次）漏改了 Mia Huang 的一部分，且完全沒套用到
   Coco Wu、Sophia Tseng、Rainie Hsu、Vicky Lin——這次全部補齊，11 位人設的 `character.md` 現在統一是「視覺行為
   光譜（她的主軸風格，不是絕對禁止）」的寫法。**同時把這條原則、以及「文件衝突以最新修改檔案為準」這條，寫成
   `CLAUDE_HANDOFF.md` 開頭的永久治理原則章節**，不再只是埋在某次 session 記錄裡。
   - ⚠️ **這條原則不影響內容尺度（SFW、不露骨、不涉及未成年化）**——這條界線本身沒有被鬆動，鬆動的是「風格/穿搭/
     場景」層面的硬性描述。使用者已確認理解這個區分（「性感」跟「露骨」是兩件不同的事）。

### R1–R18 驅動片原始檔的存放位置（2026-08-07 已解決存取問題）

R1–R8 的驅動片是用 `yt-dlp` 直接從 Instagram 貼文連結下載的，連結永久記錄在 GitHub Issue #3，**任何 session 隨時都能重新對著同一個連結重跑 `yt-dlp` 取得**，不需要保存檔案本身。

R9–R18 這 10 支不一樣——這是使用者最初提供的 18 支模板影片裡，`yt-dlp` 一直抓不下來的那 10 支，唯一取得方式是使用者直接上傳檔案，而檔案上傳綁在對話的暫存空間，新 session 讀不到。**已解決**：使用者把全部 18 支都上傳到 Google Drive 資料夾，資料夾已設定「知道連結的人可檢視」，可以直接用 `curl` 下載到本機硬碟（**不要**用 `mcp__Google_Drive__download_file_content` 這類工具讀取內容——那會把整個檔案的 base64 編碼塞進對話，1–6MB 的影片編碼後是幾百萬字元，遠超單次回合能輸出的 token 量，2026-08-07 已用 6 個平行 subagent 實測撞牆確認過，不要重複犯這個錯）：

```bash
curl -sSL "https://drive.google.com/uc?export=download&id=<FILE_ID>" -o <本機檔名>.mp4
```

Drive 資料夾：https://drive.google.com/drive/folders/12TBocSCqtEhSPgepOjo3yBIypeSbLba9

| R# | IG shortcode | 分配 KOL | Drive file ID |
|---|---|---|---|
| R1 | `DPWE2eqEVJ-` | mia-huang | `1R6yYI3J9FffzukVxtonqw7Zo6joB1o8p` |
| R2 | `C3kMsJ1PtPH` | luna-tanaka | `1tIP2rI4p_ajla5tAq_2TxjbnLKlRU_50` |
| R3 | `C2zOi2uPdxn` | vicky-lin | `115zH8obRurYjxaeOzQwglqOmktvwqHee` |
| R4 | `DRB_TBDESZl` | coco-wu | `1q4WJdSUjKvtHJvvRhbizhLwwOTjWfEX5` |
| R5 | `DNb8doNyCfH` | rainie-hsu | `1hot6rju0rro91HMUijKUTehRdvUlPf21` |
| R6 | `DKBwq88xaOG` | iris-chen | `1KL_fotR2VzD9qCELDg0f9dVBarNCcxb9` |
| R7 | `DEq7fsPPBr8` | yuna-kim | `1D-ae7TiW8x7N9UMu7nlwIOOB6Q_Vp7Vw` |
| R8 | `DVnFmlVEcre` | sophia-tseng | `10iB7x4YA1ztQY_es4B4bPI43p3TJdzQY` |
| R9 | `DB2yTeEv7LG` | sophia-tseng | `1CxjE-0H2nXyAH8E5QVX8REVBiS9H0Pqz` |
| R10 | `DDgvg5iPUft` | rainie-hsu | `13HnSlsOzC9I2Qpa9fBXlvOGyzDCVXqY_` |
| R11 | `DHI2Xhvr1b` | sophia-tseng | `1ChRPXiz-G3sJrN_xYGp4KgPqAMKOIxUo` |
| R12 | `DH2qaw1RSr2` | coco-wu | `1qbIjpBA6vE653slFj3Snd33Ry3xtS2FQ` |
| R13 | `DIAxR2RuUO` | coco-wu | `15ZjhnTtPq59iBa7uA_19TIwhr-uNyNa9` |
| R14 | `DNhxC7xJQqx` | rainie-hsu | `1f-tSBCjKoNIMP-pJkoisialzboMcmT0x` |
| R15 | `DPDTvczkep4` | iris-chen | `1NvmxZE7UXSeJ3lxyo-WQEiz5SY6QxPmT` |
| R16 | `DRTeClEX4P` | luna-tanaka | `1i454xCNjFOZ2Fc90YKshaPYbJQdrbuVe` |
| R17 | `DRgdF3vkSr1` | luna-tanaka | `1wXhEe49V0su0fY_-zHyPh9E07taVLfxD` |
| R18 | `DRjp2qfkTk5` | iris-chen | `1CPDvqRzcy2VGA7F9xwRdcVArZL5jYfjv` |

（2026-08-07 已用 R9 的檔案實測 `curl` 下載，下載回來的檔案大小跟原檔位元組數完全一致，方法確認可行。）

⚠️ **這些都是原始驅動片，只當內部動作參考用，不進 git**（見 `DANCE_CLONE_SOP.md` Step 7）——上面這個 Drive 資料夾是唯一持久保存的地方，用完不要刪除，之後每一支的 Step 1 都是從這裡 `curl` 下載，不是重新問使用者要檔案。

### 待辦（下一個 session 或下一輪對話接續）

- **R9（Sophia Tseng）Step 1–8 已全部完成（2026-08-08）**：
  - 原始驅動片畫面含 CapCut 編輯 App UI 圖示（跟 R8、Mia Huang R1 同類狀況），已裁掉並排除、確認 VP9→H.264 重編碼
  - `performance-director`/`emotion-director` 出了完整 Performance Sheet/Emotion Timeline（詳見
    `kols/sophia-tseng/generation_notes.md` R9 章節），新建了 Sophia 的不對稱識別錨點（右嘴角先動）、
    識別痣呈現指令（頭傾方向偏右）、5–7s 防面具設計
  - 兩位 agent 都把驅動片 4.0s「雙手舉高撥髮+張嘴大笑+身體晃動」標成需使用者裁決的阻斷級風險（跟 Sophia
    「沉靜克制」人設基調落差最大）——**使用者裁決採方案A，比照 R8 保留原始強度**
  - Step 5 Motion Control、Step 6 混音、Step 8 QA 一次到位，未出現重生成，QA 全數通過（身分一致、次級動態、
    面具臉、手部、肩帶穩定性皆合格）。成品：`kols/sophia-tseng/videos/dance_clone_r9/sophia_dance_clone_r9_ig_reel.mp4`
  - GitHub Issue #3 已同步標記完成
- **R10（Rainie Hsu）Step 1–8 已全部完成（2026-08-08）**：
  - 起始畫面第一版腰腹部鏤空範圍過大，Motion Control 連續兩次判定 `nsfw`（零成本），對照
    `DANCE_VIDEO_SOP.md` 既有的「start_image 只用保守服裝」修正原則，改用保留視覺辨識度但腰腹部完整
    包覆的 v2 版本後一次通過
  - Performance Sheet／Emotion Timeline 判斷這支驅動片的外放大笑跟 Rainie「張揚自信」人設契合，
    沒有像 R9 Sophia 那樣的阻斷級強度裁決
  - 次級動態載體從計畫的敞開絲質罩袍，變成實際生成裡由長髮承擔（罩袍效果未明顯呈現），QA 判定技術
    要求仍滿足
  - 成品：`kols/rainie-hsu/videos/dance_clone_r10/rainie_dance_clone_r10_ig_reel.mp4`，QA 全數通過
  - GitHub Issue #3 已同步標記完成
- **R11（Sophia Tseng）Step 1–8 已全部完成（2026-08-08）**：
  - 驅動片本身表情近乎靜止（將近 5 秒維持同一表情），Performance/Emotion Sheet 事前評估這是本批次面具臉
    風險最高的一支，需要 emotion-director 主動設計獨立於手勢動作之外的微表情演變
  - 實際生成結果的表情漸進變化優於事前擔心的程度，QA 全數通過，Step 1–8 一次到位，未發生像 R10 那樣
    需要重生成的環節
  - 場景改定位在 Pilates 工作室更衣室（呼應 Sophia 既有健身/Pilates 支柱），加了一件敞開罩衫當次級動態
    載體（比基尼+運動長褲本身沒有垂墜元素）
  - 過程中使用者發現 R10 成品裡化妝鏡反射會隨動作變化，確認是模型對鏡子的強訓練關聯性、非一般背景動態
    的通則，已記錄進 `DANCE_CLONE_SOP.md`
  - 成品：`kols/sophia-tseng/videos/dance_clone_r11/sophia_dance_clone_r11_ig_reel.mp4`
  - GitHub Issue #3 已同步標記完成
- **R12（Coco Wu）Step 1–8 已全部完成，含一次身分跑掉的重大修正（2026-08-08）**：
  - 依使用者指示採批次流程：Step 1–2（下載/裁剪）與 Step 4（起始畫面）先跟 R13–R18 一起批次做完，
    Step 3（Performance Sheet/Emotion Timeline）在進 Step 5 前補做
  - Step 3 判定驅動片是「誇張可愛手勢展示」而非傳統編舞，跟 Coco 人設高度契合，不需阻斷級強度裁決；
    最高風險點是 13s 頭部快速甩動造成的動態模糊，設計了降速 15-20%+眨眼掩護的因應方案
  - **v1 成品經使用者目視發現「臉完全變不一樣」**：根因是 Motion Control 的臉部/髮型鎖定完全依賴
    `image_id` 參考錨點（無 `soul_id` 等級的強制鎖定），v1 起始畫面的髮型輪廓（單馬尾+散髮）跟驅動片
    本人實際的雙馬尾差異太大，模型合成雙馬尾甩動動態時借用了驅動片本人的臉/髮型頂替。QA 當時誤判身分
    一致，是因為只憑 Step 3 筆記文字核對、沒有用 Read 工具跟起始畫面圖檔本身並排比對——**已列入教訓，
    往後 Step 8 一律要圖檔對圖檔核對**。曾評估改用 Seedance 2.0 Mini 取代 Motion Control（理論上身分
    鎖定更獨立），`get_cost` preflight 顯示完整規格下比 Motion Control 便宜（37.5 vs 49 credit），但
    5 秒短版測試判定 `nsfw` 失敗（12.5 credit 已退款），使用者裁決暫緩、改回正規修復路徑：重新生成
    髮型輪廓正確貼合驅動片的 v2 起始畫面，用同一支驅動片重跑 Motion Control 後身分穩定，QA 14 幀
    全數通過。完整事件記錄見 `kols/coco-wu/generation_notes.md`，通則已寫入 `DANCE_CLONE_SOP.md`
    （Motion Control 身分覆蓋風險章節）
  - 最終成品：`kols/coco-wu/videos/dance_clone_r12/coco_dance_clone_r12_ig_reel.mp4`（v2，已覆蓋 v1）
  - GitHub Issue #3 已同步標記完成
- **R13–R18 這 6 支：Step 1–8 已全部完成（2026-08-08）**：
  - 起始畫面全部核准（R13/R14/R16/R17 逐一補問後核准；R15/R18 先前已核准，R15 有已知 LOGO 文字亂碼
    小瑕疵，使用者接受不需重生成）
  - **Step 3 分析發現系統性髮型輪廓風險**：批次生成起始畫面時沒有逐支核對驅動片本人的髮型，結果
    R14/R15/R16/R17/R18 五支全部被 performance-director agent 標記出跟 R12 同一類「起始畫面髮型
    跟驅動片本人髮型輪廓不匹配」的身分覆蓋風險（R14：短髮 vs 長髮；R15：捲髮 vs 直髮；R16：短髮
    包不出驅動片局部的包頭造型；R17：栗棕捲髮 vs 近黑直髮；R18：大波浪 vs 較直髮型）。使用者在看過
    完整風險報告後明確裁決**「不用，就這樣直接去跑看看」**——不預先修正起始畫面，直接跑 Motion Control
  - **結果：5 支風險全部沒有實際發生**，Step 8 QA 逐支跟已核准起始畫面圖檔並排比對，身分全數保住。
    這說明 R12 的髮型輪廓不匹配不是每次都會導致身分覆蓋，只是升高風險，不是必然失敗——但仍建議
    Step 4 設計起始畫面時盡量貼近驅動片髮型以降低風險，不應以本次結果當作可以忽略此風險的通則
  - **R16/R17（Luna Tanaka）soul_id 拼貼 bug 修復後首次完整驗證**：新 `soul_id`（重訓練版）在
    Motion Control 全流程中身分穩定，確認修復有效
  - 成品：`kols/coco-wu/videos/dance_clone_r13/`、`kols/rainie-hsu/videos/dance_clone_r14/`、
    `kols/iris-chen/videos/dance_clone_r15/`、`kols/luna-tanaka/videos/dance_clone_r16/`、
    `kols/luna-tanaka/videos/dance_clone_r17/`、`kols/iris-chen/videos/dance_clone_r18/`
  - GitHub Issue #3 已同步標記完成
  - **R16/R17（Luna Tanaka）soul_id 拼貼 bug 已修復**：舊 `soul_id`（`1bfab2ce-cfa5-4026-93fa-e5c91b469c7a`）
    對特定 prompt（尤其低胸/精品風格描述）有近乎 100% 重現的「三連拼貼」模型慣性（訓練資料疑似混入雜誌
    型錄式多格照片），14 次不同措辭/長寬比/count 嘗試皆未能繞開。使用者**明確否決**兩個技術上可行的替代
    方案：(1) 緊裁成大特寫迴避拼貼構圖——「跳舞誰要看臉部特寫啊？」；(2) 改用 `nano_banana_pro`+參考圖
    （不需訓練 Soul）——因為會失去 `soul_id` 的身分/身材鎖定保證，且該模型生成的背景「一看就覺得像 AI」，
    違反工作室對照 `COMPETITOR_sherry_digitalp510.md` 建立的真實感標準。**正確修復**：用她既有 7 張已核准
    舊照片（不透過壞掉的舊 soul_id 生成新素材）重新訓練 Soul，新 `soul_id: a3dc13ec-16e7-4990-89c6-9e0461db46ef`
    已寫入 `profile.json`，訓練耗時約 35-40 分鐘（明顯長於一般 KOL ~10 分鐘的常態），用相同曾失敗的 prompt
    重新生成確認已解決。R16/R17 已用新 soul_id 生成新版起始畫面（Job ID `9e7ed1f4-c031-4545-b57d-3621f3659d7a`
    / `ae5998e0-787e-4558-aa06-cf3eee1178a0`），詳見 `kols/luna-tanaka/generation_notes.md` 完整事件記錄
  - 分配結果、每支的內容摘要與改分配理由，都已經寫在 GitHub Issue #3
- **R1–R18 + IG1 全部 19 支已完成 Step 1–8**——R1–R18 driver-clone 批次到此全數做完
- **所有已完成影片的音軌都是驅動片原始配樂，未取得商用授權**，真正要對外發佈前，需統一處理配樂授權
  （見 `DANCE_CLONE_SOP.md` Step 7）

---

## ⚠️ 2026-08-27 起：所有規劃都要經過 ChatGPT 覆核才能執行

Penny 的規則：**不是 Claude 規劃好就直接執行，一定要經過 ChatGPT 覆核通過才繼續。**

工作方式已改成在 GitHub 上直接來回，不再下載 md 檔轉交：

- **主檔**：`review/LEDGER.md`——一張活的議題表，狀態流 🔵 OPEN → 🟡 ANSWERED → 🟢 DONE
- **協定**：`review/README.md`——雙方各自的編輯規則
- **歷史**：`review/history/`——R1–R4 的往返，唯讀

**Claude 每次動工前先 `git pull`**（ChatGPT 可能已經改過）；
拿捏不準或覺得可能有盲點的地方，**當下就往 LEDGER 加一項 🔵**，不要留在腦袋裡；
**不要自己把 🔵 改成 🟢**——沒有經過判定就執行違反規則。

**觸發覆核的條件（2026-08-28 Penny 定）**：**只要對「這段 prompt 送出去會不會成功」沒有把握，
就必須整理成覆核請求，不要自己賭、不要先跑跑看。**判準見 `review/README.md` 開頭。

**生成節奏（2026-08-28 Penny 定）**：**一次只跑一件 spec × 2 張，絕不一次跑一大批。**
**每一段 prompt 送出前都要經 ChatGPT 覆核**（不是沒把握才送，是每段都送）；覆核可批次、生成不可批次。
