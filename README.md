# Virtual KOL Studio — Character Database

虛擬 KOL 角色設定資料庫。每個 KOL 為一個獨立目錄，包含結構化 JSON 資料、完整角色 Bible 與內容風格指南。

---

## 內容方向

本專案以模仿日本 AV 女優公開社群帳號的風格為核心方向，打造具有強烈**寄生親密感（parasocial intimacy）**的虛擬創作者。

### 核心哲學

- 不是生活美食博主，不是時尚 influencer
- 讓粉絲感覺「偷窺到她的私下生活」
- 身體存在感自然、高頻、不刻意表演
- 直視鏡頭是標誌性動作

### 內容柱（六大類型）

| 類型 | 比重 | 說明 |
|------|------|------|
| 晨間 / 剛睡醒 | 20% | 床上、睡衣、凌亂的頭髮、慵懶晨間能量 |
| 穿搭 / 換裝 | 20% | 鏡前自拍、試穿、內衣到成套的揭曉 |
| 浴室 / 洗澡後 | 15% | 浴巾、護膚、濕髮、浴室鏡子 |
| 居家放鬆 | 20% | 沙發、地板、衣物最少、吃東西、滑手機、什麼都不做 |
| 飯店 / 旅遊 | 15% | 飯店房間、泳池、床、浴室、窗景 |
| 健身 / 活動 | 10% | 運動服、健身房、伸展、運動後 |

### Benchmark 風格參考

三上悠亞、明日花綺羅、JULIA（日本）及各國同類型帳號的公開 SFW 社群帳號風格。

---

## KOL 陣容

| ID | 名字 | 城市 | 定位 | Soul ID | 狀態 |
|----|------|------|------|---------|------|
| [iris-chen](kols/iris-chen/) | **Iris Chen** 陳芯語 | 台北 | 台北 IT Girl / 生活風格 | `5fe3b6ba-1277-4822-9141-fb06eb3b93a0` | active |
| [luna-tanaka](kols/luna-tanaka/) | **Luna Tanaka** 田中ひな | 京都 | 日系美學 / 生活攝影 | `1bfab2ce-cfa5-4026-93fa-e5c91b469c7a` | active |
| [ananya-kapoor](kols/ananya-kapoor/) | **Ananya Kapoor** | 孟買 | 瑜伽 / 舞蹈 / 生活 | `fac82296-8c69-4c34-b352-1b398c8b8e1c` | active |
| [yuna-kim](kols/yuna-kim/) | **Yuna Kim** 김하은 | 首爾 | K-beauty / 彩妝 / 生活 | `235794a5-2eff-45fb-91b4-3232910afefa` | active |
| [aaliya-okonkwo](kols/aaliya-okonkwo/) | **Aaliya Rivera** | 洛杉磯 | 拉丁裔 LA 生活 / 穿搭 | `97f5c6cd-1c0c-4432-83d0-dd42210ecada` | active |
| [camille-dupont](kols/camille-dupont/) | **Camille Dupont** | 巴黎 | 法式慢生活 / 美食 / 葡萄酒 | `f19dafcc-5bc8-4d8f-af1d-ee48084ac398` | active |
| [vicky-lin](kols/vicky-lin/) | **Vicky Lin** 林薇淇 | 高雄 | 健身 / 重訓 / 健身正妹 | `bdb1d879-da36-4c1a-bc63-9f5b49a3e94e`（訓練中） | active |
| [coco-wu](kols/coco-wu/) | **Coco Wu** 吳可可 | 台中 | 校園甜心 / 宿舍生活 | `cf7045dc-4e69-4c56-9621-aa8c40bf39b4` | active |
| [rainie-hsu](kols/rainie-hsu/) | **Rainie Hsu** 許雷妮 | 台北 | 派對女王 / 夜生活 | `994e33d2-7df1-47da-8478-7a6fd849fa33` | active |
| [sophia-tseng](kols/sophia-tseng/) | **Sophia Tseng** 曾詩妃 | 台北信義 | 貴婦名媛 / 精品生活 | `192562bb-ca64-4615-9515-13d34807857c` | active |
| [mia-huang](kols/mia-huang/) | **Mia Huang** 黃米亞 | 新竹 | 直播主播 / 電競生活 | `e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4` | active |
| [zoe-lai](kols/zoe-lai/) | **Zoe Lai** 賴柔伊 | 花蓮/墾丁 | 陽光海島 / 衝浪女孩 | `27f750e6-0d32-43ce-8249-cce94ef835cd` | active |

> 注意：Aaliya Rivera 的資料夾名稱為 `aaliya-okonkwo`（歷史原因，人格已改為 LA 拉丁裔設定）。

---

## 目錄結構

```
Virtual_KOL_Studio/
├── README.md
├── KOL_TRAINING_SOP.md          # 訓練流程 SOP + 當前進度總覽
├── BENCHMARK_ACCOUNTS.md        # 原始 6 位 KOL 的 benchmark 帳號整體彙整（新 6 位不採用此法，見各自 content_style.md）
├── CLAUDE_HANDOFF.md            # Claude session 交接文件
├── SEXY_SCENE_LIBRARY.md        # 共用場景庫 + 降低「AI 感」技術要點（12 位共用）
├── DAILY_VIDEO_SOP.md           # 日常自拍影片生成流程
├── DANCE_VIDEO_SOP.md           # TikTok 舞蹈影片生成流程
├── music/                       # 舞蹈/影片配樂素材
├── .claude/workflows/           # 可重複執行的 Workflow 腳本
│   ├── kol_content_qa_pipeline.js    # 生成前審核→生成→生成後審核→存檔的 QA 流程
│   └── weekly_content_planner.js     # 單一 KOL 的每週企劃 + 防重複審核
└── kols/
    ├── index.json               # 所有 KOL 的主索引
    ├── schema.json              # 標準欄位定義（JSON Schema）
    └── {kol-id}/
        ├── profile.json         # 結構化角色資料（含 soul_id、身材數據、帳號資訊）
        ├── character.md         # 完整角色 Bible
        ├── content_style.md     # 內容方向與風格指南
        ├── generation_notes.md  # AI 生成記錄（prompt、soul_id、測試圖連結；未執行前明確標示 PENDING）
        └── images/ videos/      # 生成素材（尚未執行生成的 KOL 無此資料夾）
```

---

## AI 生成技術設定

### Higgsfield Soul V2

- 平台：[Higgsfield.ai](https://higgsfield.ai)
- 圖片生成：`model: soul_2` + `soul_id` 參數
- 影片生成：`model: cinematic_studio_video_v2`（首選）

### 重要規則

1. **每次生成必須在 prompt 裡說明髮色和髮型**（Soul V2 不繼承訓練圖的髮型）
2. **構圖多樣性**：一組圖必須主動規劃不同景別（wide / 3/4 / close-up）和角度
3. **服裝必須明確寫出**：不寫服裝模型會往最少衣物方向生成
4. **影片使用 `multi_shot_mode: auto`**（不可用 custom）

---

## 平台策略

| 平台 | 內容形式 | 重點 |
|------|---------|------|
| TikTok | 15–30s 短影片 | 身體前景內容、晨間/夜間 routine、trending 音頻 |
| Instagram Reels | 15–45s | 稍精緻、換裝揭曉、旅遊/飯店 |
| X (Twitter) | 隨手自拍、超短影片 | 直接個人 caption（1–2 句）、無 hashtag 堆疊 |

---

## 新增 KOL 流程

1. 在 `kols/` 下建立新目錄，命名規則：`{firstname}-{lastname}`（kebab-case）
2. 按照 `kols/schema.json` 建立 `profile.json`
3. 撰寫 `character.md`（角色 Bible）與 `content_style.md`（內容指南）
4. 在 `kols/index.json` 新增對應紀錄
5. **⚠️（2026-07-25 新增，強制規則）生成任何參考圖之前，必須先讀過至少一個已驗證成功的既有角色的 `generation_notes.md` 當範本**（預設參考 `kols/iris-chen/generation_notes.md`——這是目前唯一有完整記錄「一次生成基本就對、身分穩定」成功經驗的案例）。**不可以只憑生成工具本身的預設建議（例如工具說明文字建議的模型）直接決定要用哪個模型或做法**——工具的通用建議不知道這個專案過去實際驗證過什麼，一定要先比對過去成功案例，才能決定沿用或是有充分理由才偏離。
   - **預設模型**：訓練圖／Discovery 批次的生成，預設使用 `seedream_v4_5`（同 prompt 重複生成的身分一致性明顯優於 `soul_2` 未錨定時的表現，見 `kols/iris-chen/generation_notes.md` 的模型選擇記錄與 2026-07-25 的事後檢討）。**只有**當該角色已經有成功訓練出來的 `soul_id` 時，才用 `soul_2` + 該 `soul_id` 做後續生成——那是完全不同的、已錨定身分的情境，不是本條規則要避免的「無錨點一次性生成」。
   - 此規則的起因：2026-07-25 曾發生連續多個新角色（Coco Wu、Rainie Hsu、Sophia Tseng、Mia Huang、Zoe Lai）的 Discovery 批次因為選用 `soul_2` 無錨點生成，導致同一批次 4 張圖臉孔不一致，且完全沒有先比對過已驗證成功的 Iris Chen 模型選擇記錄——詳見這幾位角色 `generation_notes.md` 的相關修正記錄。
6. 生成至少 5 張臉部參考圖存入 `images/face_reference/`
7. **停下來，等使用者實際看過這批參考圖並明確確認滿意後，才可以進入下一步**——參考圖是主觀判斷，訓練是要花時間和額度的動作，兩者中間一定要有人工確認這個關卡，不可以在同一輪自動接著做完
8. 使用者確認後，才執行 Higgsfield Soul V2 訓練，記錄 soul_id 至 `profile.json` 和 `generation_notes.md`

---

## 工作分支

- **GitHub Repo**：`pennyhuang-oss/Virtual_KOL_Studio`
- **工作 Branch**：`claude/kol-personality-training-9otdaw`
- **完整交接文件**：見 `CLAUDE_HANDOFF.md`
