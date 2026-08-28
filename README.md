# Virtual KOL Studio — Character Database

虛擬 KOL 角色設定資料庫。每個 KOL 為一個獨立目錄，包含結構化 JSON 資料、完整角色 Bible 與內容風格指南。

---

## 內容方向

> ## ⚠️ 交叉覆核制度（2026-08-27 起）
>
> **任何規劃在 [`review/LEDGER.md`](review/LEDGER.md) 全部議題結案之前，不得進入生成階段。**
> 本專案採 Claude ⇄ ChatGPT 互相檢核：Claude 規劃 → ChatGPT 覆核 → Claude 修正 → 直到雙方同意。
> 操作方式見 [`review/README.md`](review/README.md)。

> **開始任何人設或素材規劃前，先讀 [`PERSONA_CANON.md`](PERSONA_CANON.md)。**
> 那份文件定義了反差公式、標誌性場景的配額原則、造型可變性與「不寫絕對禁令」四條規則，
> 適用於全體 KOL，優先於以下敘述與各角色既有檔案。

本專案以模仿日本 AV 女優公開社群帳號的風格為核心方向，打造具有強烈**寄生親密感（parasocial intimacy）**的虛擬創作者。

### 核心哲學

- 不是生活美食博主，不是時尚 influencer
- 讓粉絲感覺「偷窺到她的私下生活」
- 身體存在感自然、高頻、不刻意表演
- 直視鏡頭是標誌性動作

### 內容柱（通用骨架）

> 這是**通用骨架**，不是每位都必須照抄的模板。
> 每一位實際的支柱名稱與比重以她自己的 `kols/{id}/profile.json` 為準。

| 類型 | 參考比重 | 說明 |
|------|---------|------|
| **私下 / 她自己的空間** | **25%** | 憲章原則一指定的最大支柱。她卸下公開面貌之後、只給自己和特定的人看的樣子——貼身／性感服裝、房間的光、鏡子與床。**不是**「鬆垮邋遢、癱著什麼都不做」。 |
| 穿搭 / 換裝 | 20% | 鏡前自拍、試穿、內衣到成套的揭曉 |
| **外出 / 她的日常** | **15%** | 房間以外的地方。存在的目的是避免素材永遠困在同一個空間，**與她有沒有職業無關**。 |
| 晨間 / 剛睡醒 | 15% | 床上、睡衣、凌亂的頭髮、慵懶晨間能量 |
| 浴室 / 洗澡後 | 12% | 浴巾、護膚、濕髮、浴室鏡子 |
| 飯店 / 旅遊 | 10% | 飯店房間、床、浴室、窗景。屬配額支柱，上限 25%。 |
| 身體 / 活動 | 3–10% | 運動服、伸展、運動後 |

> 標誌性場景（泳池、和服、女僕裝、直播間、健身房、五星飯店等）一律受憲章原則二的配額限制，
> 不得成為主支柱或超過 25%。

### Benchmark 風格參考

三上悠亞、明日花綺羅、JULIA（日本）及各國同類型帳號的公開 SFW 社群帳號風格。

---

## KOL 陣容

| ID | 名字 | 城市 | 定位 | Soul ID | 狀態 |
|----|------|------|------|---------|------|
| [iris-chen](kols/iris-chen/) | **Iris Chen** 陳芯語 | 台北 | 台北 IT Girl / 生活風格 | `5fe3b6ba-1277-4822-9141-fb06eb3b93a0` | active |
| [luna-tanaka](kols/luna-tanaka/) | **Luna Tanaka** 田中ひな | 京都 | 日系美學 / 生活攝影 | `a3dc13ec-16e7-4990-89c6-9e0461db46ef` | active |
| [ananya-kapoor](kols/ananya-kapoor/) | **Ananya Kapoor** | 孟買 | 瑜伽 / 舞蹈 / 生活 | `fac82296-8c69-4c34-b352-1b398c8b8e1c` | active |
| [yuna-kim](kols/yuna-kim/) | **Yuna Kim** 김하은 | 首爾 | K-beauty / 彩妝 / 生活 | `235794a5-2eff-45fb-91b4-3232910afefa` | active |
| [aaliya-okonkwo](kols/aaliya-okonkwo/) | **Aaliya Rivera** | 洛杉磯 | 拉丁裔 LA 生活 / 穿搭 | `97f5c6cd-1c0c-4432-83d0-dd42210ecada` | active |
| [camille-dupont](kols/camille-dupont/) | **Camille Dupont** | 巴黎 | 法式慢生活 / 美食 / 葡萄酒 | `f19dafcc-5bc8-4d8f-af1d-ee48084ac398` | active |
| [vicky-lin](kols/vicky-lin/) | **Vicky Lin** 林薇淇 | 高雄 | 健身 / 重訓 / 健身正妹 | `bdb1d879-da36-4c1a-bc63-9f5b49a3e94e` | active |
| [coco-wu](kols/coco-wu/) | **Coco Wu** 吳可可 | 台中 | 校園甜心 / 宿舍生活 | `cf7045dc-4e69-4c56-9621-aa8c40bf39b4` | active |
| [rainie-hsu](kols/rainie-hsu/) | **Rainie Hsu** 許雷妮 | 台北 | 派對女王 / 夜生活 | `a4a000fe-fd96-4c36-97ff-0df9358a9b47`（v2，訓練完成；舊 `994e33d2-...` 因身材不符規格已棄用，見 generation_notes.md） | active |
| [sophia-tseng](kols/sophia-tseng/) | **Sophia Tseng** 曾詩妃 | 台北信義 | 貴婦名媛 / 精品生活 | `192562bb-ca64-4615-9515-13d34807857c` | active |
| [mia-huang](kols/mia-huang/) | **Mia Huang** 黃米亞 | 新竹 | 直播主播 / 電競生活 | `e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4` | active |

> 注意：Aaliya Rivera 的資料夾名稱為 `aaliya-okonkwo`（歷史原因，人格已改為 LA 拉丁裔設定）。

### Batch 3（2026-08-27 建檔，20 位）

> **Nico Tsai 是 pilot，正在走完整流程**（選角 → 錨定 → 訓練集 → Soul → 壓力測試）。
> 她的規格真理來源是 [`pilot/nico_pilot.json`](pilot/nico_pilot.json)，不是 `MODELING_SHOOT_PLAN.md`。
> **其餘 19 位凍結中**（`blocked_pending_v2_pilot`，v1 validator 會 HARD FAIL exit 2），
> 等 Nico 走完才解凍。


> 全部依 [`PERSONA_CANON.md`](PERSONA_CANON.md) 五條原則建立。`generation_notes.md` 皆為 PENDING，尚未執行任何生成。
> 規劃全文見 [`NEW_20_PERSONAS_PLAN.md`](NEW_20_PERSONAS_PLAN.md)。

| ID | 名字 | 城市 | 檯面設定 | Soul ID | 狀態 |
|----|------|------|----------|---------|------|
| [angel-chiu](kols/angel-chiu/) | **Angel Chiu** 邱安晴 | 台北 | 護理師 | 待訓練 | draft |
| [nico-tsai](kols/nico-tsai/) | **Nico Tsai** 蔡妮可 | 台北大安 | 美甲師 / 個人工作室 | **選角＋錨定完成，20 張訓練集待覆核放行** | in_progress |
| [tammy-chou](kols/tammy-chou/) | **Tammy Chou** 周語彤 | 台北五分埔 | 網拍老闆娘 / 服飾電商 | 待訓練 | draft |
| [emma-kao](kols/emma-kao/) | **Emma Kao** 高映真 | 台南 | 新聞主播 | 待訓練 | draft |
| [zoey-yeh](kols/zoey-yeh/) | **Zoey Yeh** 葉芷妍 | 宜蘭 | 花藝師 | 待訓練 | draft |
| [miu-shiraishi](kols/miu-shiraishi/) | **Miu Shiraishi** 白石美羽 | 東京中目黑 | 咖啡店員 | 待訓練 | draft |
| [rin-ayase](kols/rin-ayase/) | **Rin Ayase** 綾瀨凜 | 東京銀座 | 高級會員制酒店小姐 | 待訓練 | draft |
| [nanami-fujiwara](kols/nanami-fujiwara/) | **Nanami Fujiwara** 藤原七海 | 箱根 | 溫泉旅館女將見習 | 待訓練 | draft |
| [kanon-komori](kols/kanon-komori/) | **Kanon Komori** 小森花音 | 東京秋葉原 | 女僕咖啡廳店員 | 待訓練 | draft |
| [jia-seo](kols/jia-seo/) | **Jia Seo** 서지아 | 首爾江南 | K-pop 舞蹈老師 | 待訓練 | draft |
| [yerin-han](kols/yerin-han/) | **Yerin Han** 한예린 | 首爾 | 高爾夫教練 / 練習場 | 待訓練 | draft |
| [somi-oh](kols/somi-oh/) | **Somi Oh** 오소미 | 釜山 | 美食帳號經營者 / 吃播 | 待訓練 | draft |
| [zhiyi-shen](kols/zhiyi-shen/) | **Zhiyi Shen** 沈知意 | 上海陸家嘴 | 金融業 OL | 待訓練 | draft |
| [wanyin-jiang](kols/wanyin-jiang/) | **Wanyin Jiang** 江晚吟 | 蘇州 | 旗袍店店主 / 古典舞背景 | 待訓練 | draft |
| [ruoruo-tang](kols/ruoruo-tang/) | **Ruoruo Tang** 唐苡若 | 成都 | 皮拉提斯教練 | 待訓練 | draft |
| [cheryl-soh](kols/cheryl-soh/) | **Cheryl Soh** 蘇思穎 | 新加坡（華裔） | 空服員 | 待訓練 | draft |
| [wendy-yeo](kols/wendy-yeo/) | **Wendy Yeo** 楊薇伊 | 新加坡丹戎巴葛 | 調酒師 | 待訓練 | draft |
| [peggy-lee](kols/peggy-lee/) | **Peggy Lee** 李珮甄 | 吉隆坡（華裔） | 汽車改裝店行銷企劃 | 待訓練 | draft |
| [sydney-leong](kols/sydney-leong/) | **Sydney Leong** 梁欣妮 | 檳城喬治市（華裔） | 甜點師 / 烘焙工作室 | 待訓練 | draft |
| [angeline-kwee](kols/angeline-kwee/) | **Angeline Kwee** 郭慧恩 | 雅加達（華裔） | 精品選物店主理人 | 待訓練 | draft |


---

## 目錄結構

```
Virtual_KOL_Studio/
├── README.md
├── review/                      # Claude ⇄ ChatGPT 交叉覆核工作區
│   ├── README.md                #   雙方的操作規則與狀態流轉
│   ├── LEDGER.md                #   議題帳本（覆核狀態的唯一真理來源）
│   └── rounds/                  #   歷次覆核的完整論述（唯讀存查）
├── pilot/                       # Nico Vertical Slice（規格的真理來源）
│   ├── nico_pilot.json          #   Phase A–D 完整規格
│   ├── schema_v2.json           #   資料結構定義
│   └── location_registry.json   #   地點層級 + signature/career 預設值
├── MODELING_SHOOT_PLAN.md       # Batch 3 建模照完整規劃（選角/錨定/訓練集，含配額驗證器）
├── PERSONA_CANON.md             # 人設憲章：全體 KOL 適用的四條原則（反差公式/場景配額/造型可變/不寫禁令）
├── KOL_TRAINING_SOP.md          # 訓練流程 SOP + 當前進度總覽
├── BENCHMARK_ACCOUNTS.md        # 原始 6 位 KOL 的 benchmark 帳號整體彙整（新 6 位不採用此法，見各自 content_style.md）
├── CLAUDE_HANDOFF.md            # Claude session 交接文件
├── SEXY_SCENE_LIBRARY.md        # 共用場景庫 + 降低「AI 感」技術要點（11 位共用）
├── WARDROBE_SYSTEM.md           # 造型差異化引擎：穿搭/髮型/地點層級/微物件四轉盤（11 位共用）
├── REELS_AND_STRUCTURE_SYSTEM.md # 短影音剪接密度/情境設計 + Carousel「1 setup × N 表情」結構
├── COMPETITOR_sherry_digitalp510.md  # 競品視覺與打光拆解（@sherry_digitalp510）
├── DAILY_VIDEO_SOP.md           # 日常自拍影片生成流程
├── DANCE_VIDEO_SOP.md           # TikTok 舞蹈影片生成流程（Method A：AI 自主編舞）
├── DANCE_CLONE_SOP.md           # 熱門舞蹈複製流程（Method B：動作驅動，複製真人舞步+音樂卡點）
├── DANCE_METHOD_COMPARISON.md   # 與 firekou/Buildup_KOL 動作驅動法的對比與整合建議
├── music/                       # 舞蹈/影片配樂素材
├── .claude/agents/               # 表演設計 subagent（身體/臉部兩層，DANCE_VIDEO_SOP.md 與 DANCE_CLONE_SOP.md 共用）
│   ├── performance-director.md      # 身體表演層：次級動態、鏡頭關係、段落結構
│   └── emotion-director.md          # 臉部表演層：微表情時間軸、眼神腳本、不對稱指令
├── .claude/workflows/           # 可重複執行的 Workflow 腳本
│   ├── kol_content_qa_pipeline.js    # 生成前審核→生成→生成後審核→存檔的 QA 流程
│   └── weekly_content_planner.js     # 單一 KOL 的每週企劃 + 防重複審核
├── tools/
│   ├── validate_shoot_plan_v2.py     # 語意+反作弊驗證器（Phase A–D gate、身分覆蓋、registry 推導）
│   ├── gen_pilot_review.py           # 由 JSON 自動計算覆核包統計（防止文件層漂移）
│   ├── validate_shoot_plan.py        # v1 配額驗證（僅供 19 位 v1 資料，已凍結）
│   ├── shoot_plan.json               # 20 位 × 13 張的結構化規劃資料
│   ├── assign_dance_batch.py         # 舞蹈候選清單核准後，平均分配給各 KOL（見 DANCE_CLONE_SOP.md）
│   ├── parse_dance_issue.py          # 把 GitHub Issue #3 的候選清單解析成 assign_dance_batch.py 吃得懂的 CSV
│   └── apply_dance_assignment_to_issue.py  # 把分配結果套回 Issue #3 內文（待篩選→已分配）
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

0. **人設層一律以 [`PERSONA_CANON.md`](PERSONA_CANON.md) 為準**——與各角色既有檔案衝突時，憲章優先
1. **每次生成必須在 prompt 裡說明髮色和髮型**（Soul V2 不繼承訓練圖的髮型）
   → 也代表**髮色可以隨時改，不需要重訓 Soul**，見憲章原則三
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
