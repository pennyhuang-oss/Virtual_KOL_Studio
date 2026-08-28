# Virtual KOL Studio — 人格訓練 SOP

> ⚠️ **人設層以 [`PERSONA_CANON.md`](PERSONA_CANON.md) 為準。**本檔案中任何與憲章四條原則相衝突的敘述，一律以憲章優先。


> 每次換裝置或開新 session 時，請讓 Claude 讀取這份文件，它會知道完整的執行方式與注意事項。

---

## 目前進度總覽

### 原始 6 位

| KOL | Soul ID | Soul 訓練 | 測試圖 | 自介素材 | 狀態 |
|-----|---------|----------|--------|---------|------|
| Iris Chen | `5fe3b6ba-1277-4822-9141-fb06eb3b93a0` | ✅ | ✅ 14 張 | ✅ 影片 v3 通過；舞蹈影片 v1-v3 通過 | ✅ 完成 |
| Luna Tanaka | `a3dc13ec-16e7-4990-89c6-9e0461db46ef`（v2，2026-08-08 重訓練） | ✅ | ✅ 6 張 | ❌ 待生成 | 🔄 進行中 |
| Ananya Kapoor | `fac82296-8c69-4c34-b352-1b398c8b8e1c` | ✅ | ✅ 6 張（場景 1+3 已重生成） | ❌ 待生成 | 🔄 進行中 |
| Yuna Kim | `235794a5-2eff-45fb-91b4-3232910afefa` | ✅ | ✅ 6 張 | ❌ 待生成 | 🔄 進行中 |
| Aaliya Rivera | `97f5c6cd-1c0c-4432-83d0-dd42210ecada` | ✅ | ✅ 8 張 | ❌ 待生成 | 🔄 進行中 |
| Camille Dupont | `f19dafcc-5bc8-4d8f-af1d-ee48084ac398` | ✅ | ✅ 12 張 | ✅ 4 張通過 | ✅ 完成（影片素材待生成）|

訓練順序：Ananya Kapoor → Yuna Kim → Aaliya Rivera → Camille Dupont

### 新增 5 位（2026-07-24，台灣籍）

| KOL | Soul ID | Soul 訓練 | 測試圖 | 狀態 |
|-----|---------|----------|--------|------|
| Vicky Lin | `bdb1d879-da36-4c1a-bc63-9f5b49a3e94e`（`status: ready`，訓練完成） | ✅ 完成 | ✅ 12 張（第四輪 `v4_anchored_01`–`12`，Element 錨定身分一致，使用者已核准；第一～三輪僅供對照） | ✅ 前兩次 session 累計 12 次呼叫失敗後，2026-07-31 使用者要求重試，改用先前已確認的 media_id，第一次呼叫即成功受理並於同日確認 `raw_status: completed`；可用 `model: soul_2` + 此 soul_id 生成後續內容，詳見 `kols/vicky-lin/generation_notes.md` |
| Coco Wu | `cf7045dc-4e69-4c56-9621-aa8c40bf39b4`（`status: ready`，訓練完成） | ✅ 完成 | ✅ 12 張（Reference Element `4b6c659c-786b-43de-87af-87cea3cc99dd` 錨定，`training_v1/`） | ✅ 2026-07-31 確認訓練完成，`show_characters(action='train')` 回傳的 `items` 列表確認 `raw_status: completed`；可用 `model: soul_2` + 此 soul_id 生成後續內容，詳見 `kols/coco-wu/generation_notes.md` |
| Rainie Hsu | `a4a000fe-fd96-4c36-97ff-0df9358a9b47`（v2，`status: ready`，訓練完成） | ✅ 完成 | ✅ 13 張（Reference Element `a469f98d-11ae-42f3-8580-220d94cd473a` 錨定，`training_v2/`） | ✅ 2026-08-05 換錨點重訓：舊 `soul_id`（`994e33d2-...`，`training_v1/`）因身材（94-59-92cm/F罩杯）未吃到、錨點選角時只核對臉部未核對身材而已棄用；新錨點改用同一輪 `candidate_02.png`（沙漏身型與設定吻合）。同時首次套用 `SEXY_SCENE_LIBRARY.md` 新版五段式物理光線公式。`show_characters(action='status')` 已確認 `raw_status: completed`；可用 `model: soul_2` + 此 soul_id 生成後續內容，詳見 `kols/rainie-hsu/generation_notes.md`「2026-08-05 換錨點與訓練集重製」章節 |
| Sophia Tseng | `192562bb-ca64-4615-9515-13d34807857c`（`status: ready`，訓練完成） | ✅ 完成 | ✅ 13 張（Reference Element `980f8414-7709-47ff-9c88-fdc30b54d03d` 錨定，第三輪五官重新設計後的身分，`training_v1/`） | ✅ 2026-07-31 確認訓練完成，`show_characters(action='status')` 確認 `raw_status: completed`；可用 `model: soul_2` + 此 soul_id 生成後續內容，詳見 `kols/sophia-tseng/generation_notes.md` |
| Mia Huang | `e2f562ba-2c3f-4e50-b9be-f8854dcb6ab4`（`status: ready`，訓練完成） | ✅ 完成 | ✅ 13 張（Reference Element `92ffbd80-32c7-495f-91ed-f109b419bb41` 錨定，`training_v1/`） | ✅ 2026-07-30 訓練完成，可用 `model: soul_2` + 此 soul_id 生成後續內容，詳見 `kols/mia-huang/generation_notes.md` |
> ✅ 截至 2026-07-31，這 5 位全數完成 Reference Element 錨定訓練圖批次並成功完成 Soul 訓練（`status: ready`），可用 `model: soul_2` + 各自 soul_id 生成正式內容。Vicky Lin 先前累計兩次 session、12 次呼叫皆為工具層級失敗，2026-07-31 重試後第一次呼叫即成功受理（`soul_id: bdb1d879-da36-4c1a-bc63-9f5b49a3e94e`），同日確認訓練完成。
>
> **⚠️ 2026-08-05：Zoe Lai 人設已移除。** 原第 6 位台灣籍角色，因人設調整過程中反覆出現臉部辨識問題（跟其他角色撞臉、眼型修正後仍不理想）與其他設計反覆，使用者決定不建立此人格，`kols/zoe-lai/` 目錄與所有相關資料已從 repo 刪除，目前台灣籍角色為 5 位。



### Batch 3 pilot（2026-08-28 進行中）

| 階段 | 狀態 |
|------|------|
| 規劃覆核（ChatGPT R1–R9）| ✅ 全數結案；validator exit 0、語意逐列覆核 20/20、對抗測試 26/26 |
| A 選角（4 個候選 identity）| ✅ 使用者選定 candidate_03 |
| Reference Element 錨點 | ✅ `68ff990e-1862-4003-bfe3-fe288275cdd4`（`nico-tsai-anchor`）|
| B1 驗重現 | ✅ |
| B2 驗輕度外推（全身＝身材最終把關）| ✅ 第一次拍成背影作廢，修正後通過 |
| C 訓練集 20 張 | ⏸ prompt 已產生，待 ChatGPT 覆核（`review/REVIEW_PHASE_C.md`）|
| Soul 訓練 → D 壓力測試 | 未開始 |

> **其餘 19 位仍凍結**（`blocked_pending_v2_pilot`），等 Nico 這條 vertical slice 走完才解凍。
> Nico 的規格真理來源是 `pilot/nico_pilot.json`，不是 `MODELING_SHOOT_PLAN.md`。

---

## 這個模型的實測行為（seedream_v4_5，2026-08-28 建立）

> **這一節是燒掉 13 張 credit 換來的，不是推測。每一條都有前後對照。**
> 出處：`kols/nico-tsai/generation_notes.md` Round 2 / Round 3 / Phase B。
> 下一位角色開始生成前**必讀**，不要重新試錯。

### 1. 這個模型不執行否定句

構圖與服裝結構的否定句**完全無效**。有效的是正面描述目標狀態：

| 失效寫法（否定）| 有效寫法（正面描述）|
|----------------|-------------------|
| `nothing below the knee is visible` | `the bottom edge of the picture cuts straight across her thighs, roughly a hand's width above the knee` |
| `NOT a crop top, no exposed midriff` | `the hem is long and tucked into her trouser waistband` |
| `no ombré, no dark roots, no lightened tips` | `a single flat salon dye job done right down to the scalp: the roots are exactly the same brown as the ends` |
| `her back is not toward the camera` | 見第 2 條 |

**顏色排除仍然有效**（`not tanned`、`not olive` 有效）。**構圖與服裝結構的否定一律無效。**

### 2. 身體朝向不能寫角度

`turned about 30 degrees toward her own left` **連續三次**被畫成背影
（Nico Round 2 首批、Round 3 的 candidate_01、Phase B 的 B2 第一次）。

→ 一律描述**相機看得到哪些身體正面特徵**：

> Her navel and the front of both shoulders point toward the camera. Both of her collarbones are
> visible. The camera sees the front of her jeans — the fly, the button and the front pockets —
> not the back pockets.

一次就對。**全身圖是身材比例的最終把關點，拍成背影等於這一關白做。**

### 3. 景別：說「畫面下緣切在哪裡」

各景別的有效寫法見 `tools/build_phase_c_prompts.py` 的 `FRAMING` 表。例如 knee_up：

> The bottom edge of the picture cuts across her legs just below the knees. Her head, torso, hips
> and thighs are all inside the frame. Her lower legs and feet are outside the picture.

### 4. Reference Element 會把「同一件衣服」整件複製

指定與錨點圖**同一件**衣服時，錨點那件衣服的細節會原封不動出現，
prompt 明寫相反的描述也蓋不掉（Nico B1：錨點毛衣的兩道露肩開口，
prompt 寫 `unbroken and continuous over both shoulders` 無效）。
指定**不同**衣服時 prompt 才有效（B2 換成另一件，開口消失）。

→ **選角圖穿的那一套，之後在訓練集裡再用時，衣櫃定義必須誠實描述錨點實際的樣子**，
或乾脆換一件明顯不同的衣服。

### 5. 錨點的髮色細節蓋不掉

錨點圖上的挑染／不均勻髮色會被一路帶下去，三次明確的「單一平染」指令都無效。
→ **選角階段就要把髮色看清楚**；發現後只有兩條路：接受它成為角色造型，或換錨點。

### 6. 臉部骨架不寫死就會收斂到預設美女臉

見 `PERSONA_CANON.md` 原則六。本 repo 的預設臉約等於 `rainie-hsu`，
已經害 `sophia-tseng` 與 `nico-tsai` 各重做一次。

---

---

## 訓練集 vs 日常素材：兩套不同的規則（2026-08-28 建立）

> **背景**：Nico 的 Phase C 訓練集完成後，使用者的評語是「臉沒問題、可以送訓練，但**還是少了一點真人感**」，
> 並問「怎麼都沒參考小雪莉那個帳號的分析？」。查證後發現：20 張裡有 14 張是公共場所
> （超商、藥妝店、洗衣店、月台、早餐店、街道、公園、咖啡廳），**全部寫成「畫面裡只有她一個人」，
> 0 張有背景路人**——而 `SEXY_SCENE_LIBRARY.md` §9 早在 2026-08-05 就用 14 張實測反轉過這條規則，
> 明寫「空景的公共場所本身就是最強的合成訊號」。

**根因不是規則不存在，是我沒有分清這兩件事的規則不一樣，於是用同一套邏輯做完了全部。**

| | **Soul 訓練集** | **日常素材** |
|---|---|---|
| 目的 | 讓模型學一個穩定的身分 | 讓觀眾相信她是真人 |
| 公共場景的背景路人 | **不要**——第二個人可能被學進身分 | **必須有**——見 `SEXY_SCENE_LIBRARY.md` §9(b) |
| 畫面收尾 | 正面封閉集合（只有她、每隻手都連到她的手臂）| 反過來：人多、雜、有生活痕跡 |
| 光線 | 五段式物理光，**乾淨可讀優先** | 五段式物理光，**曝光犧牲可以更狠** |
| 濾鏡 | 幾乎不用（pilot 第一輪 meitu=0、CCD ≤2）| 自由，CCD／美圖都是真人感的一部分 |
| 視角 | 以他拍為主，自拍少量 | **大量混合**——自拍／他拍／背後跟拍／俯拍／找到的鏡面 |
| 構圖 | 身分優先，框架物克制 | **刻意讓「用什麼拍的」入鏡**：車門框、百葉簾、路口凸面鏡 |

**訓練集看起來比日常素材假，是刻意的取捨，不是做壞。**
但 **Soul 訓練一完成，日常素材必須立刻切回右欄**——否則那個「空無一人的台北」會變成
這個角色所有素材的共同特徵，而那正是我們要避免的東西。

### 下一個角色開始生成日常素材前，必讀

**[`COMPETITOR_sherry_digitalp510.md`](COMPETITOR_sherry_digitalp510.md)** —— 這份是花了大量時間
逐張拆解一個全 AI、58 萬粉、生成品質極高的競品帳號得到的，是本 repo 目前最接近「怎麼做出真人感」
的答案。它的結論已經分散寫進 `SEXY_SCENE_LIBRARY.md`（五段式光線、背景路人、環境元素式地點、
同穿搭一日敘事）與 `WARDROBE_SYSTEM.md`（四轉盤、A/B/C 三層地點），
**但分散之後就容易在單一批次裡被整段略過——Nico 這次就是。**

日常素材開跑前，逐項對照這五條：

1. **公共場景有沒有背景路人**（四條件：背向／不看鏡頭／失焦／外型區隔）
2. **每張的光有沒有一個「具名的反射面」**——白沙、白色船身、池水、濕柏油、燈箱
3. **曝光有沒有犧牲一邊**——真實相機一次只能對一個亮度測光，兩邊都對就是假
4. **一個畫面裡有沒有兩個色溫**
5. **C 級「完全不美」的地點有沒有達到硬性下限**，以及「用什麼拍的」有沒有入鏡

---

## 各步驟的實際 credit 單價（2026-08-28 從 transactions 帳實測）

**這張表的用途是防止「我覺得很貴」式的誤判。** 過去在規劃時是用「幾張圖」在估成本，
但不同階段用的模型單價差 8 倍，用張數估會得到完全錯誤的結論。

| 項目 | 模型 / 動作 | 單價 |
|------|------------|------|
| 選角、錨定、訓練集 | `seedream_v4_5` | **1 credit / 張** |
| Soul 訓練 | `show_characters(action='train')` | **25 credits / 次**（一次性） |
| 訓練後的所有生成 | `soul_2` + soul_id | **0.12 credits / 張** |

**推論**：
- Nico 的 Phase A+B+C 共 35 張 seedream ＝ 35 credits，訓練 25 credits，合計 **60 credits**。
  這是「建一個角色」的實際造價。
- **Soul 訓練完成之後，出圖幾乎不要錢**（0.12/張，100 張才 12 credits）。
  所以「訓練後的壓力測試 / QA / 日常素材」不該用張數當阻力——阻力只剩人工覆核的時間。
- 貴的一律在訓練「之前」：每一張 seedream 都是 1 credit，
  所以**選角與訓練集的 prompt 必須先過 lint 與覆核再送生成**，這條規則的成本理由在這裡。

---

## ⚡ 新 Session 啟動時，立刻做這件事

> 讀完這份文件後，直接照以下清單執行，不用等使用者再說明。

### 現在的待辦（依優先順序）

> 最後更新：2026-07-24

0. **⚠️ 強制規則（2026-07-24 新增，優先於以下所有事項）**：任何 KOL 生成臉部參考圖後，**必須停下來等使用者實際看過並明確確認滿意，才可以送進 Soul 訓練**——不可以在同一輪自動接著做完。這是因為 Vicky Lin 第一輪試跑沒有這個關卡，結果生成方向錯了才發現，浪費了生成額度。詳見 README.md「新增 KOL 流程」步驟 6，以及 `.claude/workflows/kol_content_qa_pipeline.js` 的審核流程。

1. **Vicky Lin — 重新生成臉部參考圖**
   - 外型描述已修正（見 `character.md`/`profile.json`/`generation_notes.md` 的 2026-07-24 修正記錄）：核心是「漂亮性感健身網紅」，明確禁止健美選手/男性化方向
   - 生成後停下來，等使用者確認滿意才能繼續（見上方第 0 點）

2. **Coco Wu / Rainie Hsu / Sophia Tseng / Mia Huang / Zoe Lai — 臉部參考圖生成**
   - 都還沒開始，人設文件都已完整，可以直接照 `generation_notes.md` 裡的規劃批次執行
   - 同樣適用第 0 點的強制確認關卡

3. **Luna Tanaka — 自我介紹素材圖生成**
   - Soul 訓練 ✅，測試圖 ✅，尚未生成自介素材（參考 Camille 的 `self_intro_v1` 流程）
   - 生成前先確認場景與穿搭，每個場景兩張，構圖必須不同

4. **Yuna Kim — 自我介紹素材圖生成**
   - Soul 訓練 ✅，測試圖 ✅（selfie、江南咖啡廳、弘大街頭各 2 張）
   - 同上流程

5. **Aaliya Rivera — 自我介紹素材圖生成**
   - Soul 訓練 ✅，測試圖 ✅（poolside、restaurant、selfie 共 8 張）
   - 同上流程

6. **Camille Dupont — 自我介紹影片素材生成**
   - 自介圖 4 張已通過，剪輯時間軸已完成，影片素材（10 個 shot）尚未生成

### 注意事項（每次生成前必讀）
- **Iris Chen 是所有 KOL 的標準範本**：她是第一個完成的人格，後續每一個 KOL 的訓練規格、文件規模、步驟流程，全部以她為基準。不確定某個步驟怎麼做、某份文件要寫到什麼程度，就去看 `kols/iris-chen/` 的結構和內容對齊。
- **生成測試圖前，必須先列出預計場景讓使用者確認**，同意後才執行
- 圖片無法從雲端 session 下載 Higgsfield CDN，需使用者先上傳到 GitHub，再由 Claude 用 `raw.githubusercontent.com` 搬到正確資料夾
- 所有 push 都在 branch：`claude/kol-personality-training-9otdaw`
- **⚠️ 素材生成必須參考 Benchmark 帳號（所有人格適用）**：
  - **圖片素材**：生成前先查閱該 KOL `character.md` 的 Benchmark 帳號，以對應帳號的圖文風格、構圖方式、身材展示角度作為 prompt 方向依據
  - **影音素材**：生成前先查閱該 KOL Benchmark 帳號發布的影片，以其拍攝方式、剪輯節奏、出場方式作為腳本/生成方向
  - 當不知道該給什麼 prompt 或腳本方向時，**優先查閱 Benchmark 帳號最近發布的內容找靈感**，讓素材風格對標這些帳號
  - 各 KOL 的 Benchmark 帳號詳見各自 `character.md` → 「社群平台 & Benchmark 帳號」章節
- **⚠️ 肢體動作多元化（所有人格適用）**：每次生成任何 KOL 的圖片，必須主動設計多元的姿勢、構圖與表情，禁止單一擺拍正面看鏡頭。規劃每張圖前先決定「這張照片的姿勢故事是什麼」，讓她在做某件事、有某種情緒，再寫 prompt。
  - 姿勢方向：看向遠方、中途動作被捕捉（撩髮/調整衣服/拿杯子）、側身或背影回眸、行走中側拍、坐姿變化（翹腳/前傾/下巴靠手）、與場景互動（靠牆/扶窗框/靠欄杆）
  - 表情方向：自然微笑、若有所思、被逗笑的瞬間感、放鬆閉眼享受
  - 構圖配合姿勢：廣角遠景時人物要有動態感；3/4 身時側身或斜角；近景時搭配表情或手部動作細節
- **⚠️ 同一場景兩張圖構圖必須不同（所有人格適用）**：同場景、同衣服、同環境，但兩張圖的景別和角度必須明顯不同（例如 3/4 身 vs 臉部近景；廣角遠景 vs 特寫；正面 vs 側面）
- **⚠️ 降低「AI 感」檢查清單（2026-07-24 新增，所有人格適用）**：送出生成前對照 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉逐項檢查（皮膚質感、裝置/鏡頭規格、混合不均勻光源、背景雜物細節、服裝完整度）；運動類角色（Vicky Lin）額外檢查是否偏向健美選手/男性化方向。有 `.claude/workflows/kol_content_qa_pipeline.js` 可以自動跑這套審核流程，不用每次手動對照。

---

## 工具與連接

- **AI 生圖平台**：Higgsfield（透過 MCP 連接）
- **MCP 連接方式**：Claude Connectors → higgs
- **GitHub repo**：`pennyhuang-oss/Virtual_KOL_Studio`
- **工作 branch**：`claude/kol-personality-training-9otdaw`
- **資料位置**：每個 KOL 的資料夾在 `kols/<kol-id>/`

---

## 完整訓練流程（每個 KOL 的標準步驟）

### 第一步：確認外型設定

1. 讀取該 KOL 的 `character.md` 和 `profile.json`
2. 確認以下欄位都清楚定義：
   - 臉型、髮型、眼睛、膚色
   - 身材（例如 Luna 是「童顏巨乳」）
   - 穿搭風格
3. 查看 `images/face_reference/` 裡的參考圖（每個 KOL 應有 4 張）

### 第二步：確認臉部參考圖

- 參考圖已放在 GitHub 各 KOL 的 `images/face_reference/` 資料夾
- GitHub raw URL 格式：
  ```
  https://raw.githubusercontent.com/pennyhuang-oss/Virtual_KOL_Studio/<commit-sha>/kols/<kol-id>/images/face_reference/ref_01.webp
  ```
- 這些 URL 可以直接被 Higgsfield MCP 讀取，不需要先下載

### 第三步：送進 Soul 訓練

呼叫 Higgsfield MCP 的 `show_characters` 工具：

```
show_characters(
  action='train',
  name='<KOL 英文名>',
  type='soul_2',
  images=[
    <ref_01 URL>,
    <ref_02 URL>,
    <ref_03 URL>,
    <ref_04 URL>,
    ... 其他補充圖（如有）
  ]
)
```

**最低需要 5 張圖**（Soul 要求 5–20 張）。如果只有 4 張臉部參考圖，需要額外補充至少 1 張。

訓練時間：約 10 分鐘。

### 第四步：確認訓練完成

```
show_characters(action='status', soul_id='<soul_id>')
```

回傳 `"status": "ready"` 即為完成。

### 第五步：生成測試圖確認成果

> ⚠️ **重要規則：訓練完成後，必須先向使用者確認場景，待使用者同意後才能開始生成。**
> 
> 確認項目：
> - 場景名稱（例如：街頭、咖啡廳、公園、海邊、室內等）
> - 穿搭描述（每個場景分別確認）
> - 角度與構圖（全身、3/4、特寫等）
>
> 確認過後再執行以下生成步驟。

訓練完成後，用 Soul ID 生成至少 6 張不同場景的測試圖，確認身份一致性：

```
generate_image(
  model='soul_2',
  soul_id='<soul_id>',
  prompt='...',
  aspect_ratio='9:16',
  count=2
)
```

建議場景：依使用者確認的場景為準（每個場景 2 張，至少 3 個場景共 6 張）。

Prompt 結構：
```
<年齡> <國籍> girl, <臉部特徵>, <身材描述>, <場景>, wearing <服裝>, <角度>, <光線>, film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style
```

用 `job_display(id='<job_id>')` 顯示結果。

### 第六步：更新文件並 push 到 GitHub

1. 更新 `character.md`：在外型欄位加上 Soul ID
2. 更新 `profile.json`：加上 `ai_generation` 欄位（soul_id、model、trained_at）
3. 新增 `generation_notes.md`：記錄 Soul ID、訓練圖來源、測試圖連結、prompt 結構
4. 將測試圖存入 `images/soul_test_v1/`
5. Commit 並 push 到 `claude/kol-personality-training-9otdaw`

---

## 已知問題與解法

### 問題 1：soul_2 模型無法鎖定臉部

**症狀**：傳入參考圖後，生成出來的臉完全不同。  
**原因**：`soul_2` 模型的參考圖只影響「風格」，不影響人臉身份。唯一能固定臉的方式是做 Soul 訓練（把臉訓練進 Soul ID 裡）。  
**正確做法**：不要在 `generate_image` 裡傳入臉部參考圖作為 medias，應該使用 `soul_id` 參數搭配已訓練好的 Soul。

---

### 問題 2：`show_characters` 只顯示列表，沒有啟動訓練 UI

**症狀**：呼叫 `show_characters(action='train', ...)` 後，只回傳現有角色列表，沒有啟動訓練。  
**原因（已解決）**：之前曾中途打斷過 `show_characters` 的呼叫，導致系統鎖住，之後的重試都被擋掉。  
**解法**：
- 重新整理 Claude 頁面，或開新 session 再試
- 確認 Connectors 裡的 higgs 工具都有啟用（display result 也要勾選）

---

### 問題 3：生成圖無法在 Claude 顯示

**症狀**：生成圖只有文字連結，沒有圖片預覽。  
**解法**：
1. 打開 Claude 設定 → Connectors → higgs
2. 把所有可以勾的選項全部勾起來，包括「Display Result」
3. 重新呼叫 `job_display(id='<job_id>')`

---

### 問題 3b：選角/訓練圖的四個重複犯過的 prompt 錯誤（2026-08-27 新增）

> 這四項全部在 `rainie-hsu` 或本 repo 其他文件記錄過，但沒寫成可執行的修法，
> 導致 2026-08-27 的 `nico-tsai` Round 1 又踩了一次。修法寫在這裡。

**(1) 五段式物理光公式不能用在攝影棚設定。**
該公式（`SEXY_SCENE_LIBRARY.md` 第 3 點）是為**真實生活場景**設計的——具名光源是窗、水面、霓虹燈這種
「場景本來就有的東西」。若場景寫成攝影棚，`white foam board`、`tungsten practical lamp`、`doorframe`
會被模型當成**畫面內的道具畫出來**（Round 1 連相機都入鏡）。
→ **選角圖一律用她自己的日常空間，不用攝影棚**（也符合使用者對 Rainie 第二輪「很像棚拍」的否決）。

**(2) 景別指令要放最前面——但「排他性措辭」這個修法本身是錯的（2026-08-28 實測推翻）。**
放在結尾的 `[CAMERA] tight headshot` 會被忽略（`rainie-hsu` Round 1 全身出成半身，`nico-tsai`
Round 1 headshot 出成全身）。
2026-08-27 這裡曾寫「改用排他性措辭 `Nothing below the collarbone is visible.` 放第一行」——
**2026-08-28 實測：這個修法無效**，指定 knee_up 的 4 張全部出成含鞋全身。
→ **正確寫法是描述「畫面下緣切在哪裡」**，見上方〈這個模型的實測行為〉第 1 條。

**(3) `bleached` 會把任何髮色推到白金——但拿掉它只解決一半。**
「冷灰奶茶」寫成 `cool greige milk-tea bleached hair` 出圖是銀白色。拿掉 `bleached` 之後
不再整頭銀白，**但改成了有深色髮根的漸層 ombré**，而且 `no ombré, no dark roots` 這種否定完全無效。
→ 有效的是正面描述染髮這件事本身：
`a single flat salon dye job done right down to the scalp: the hair at her parting and roots is
exactly the same medium brown as the hair at the ends`。見〈這個模型的實測行為〉第 1 條。

**(4) 服裝沒寫領型，模型會自補低胸，導致身材判讀失真。**
→ 服裝必須寫滿五層（上身含**領型**／下身／鞋／包或外套／首飾髮飾），
見 `WARDROBE_SYSTEM.md` 與各 `content_style.md` 的「服裝 prompt 必須寫滿五層」。

**完整的選角與訓練集規格見 [`MODELING_SHOOT_PLAN.md`](MODELING_SHOOT_PLAN.md)，
配額可用 `python3 tools/validate_shoot_plan_v2.py` 自動驗證（v1 的 `validate_shoot_plan.py` 已凍結，會 HARD FAIL exit 2）。**

---

### 問題 4：CDN 圖片（Higgsfield CloudFront）無法從雲端 session 下載

> **⚠️ 2026-08-27 更新：本條已過期，不要再照抄。**
> 本日在雲端 session 實測 `curl` 直接下載 `d8j0ntlcm91z4.cloudfront.net` 的生成結果，
> **四張全部 HTTP 200 成功**，下載後用 Read 工具可以正常目視檢查。
> 目前的正常流程就是：`generate_image_batch` → `jobs_wait` 取 `result_url`
> → `curl` 下載到 `kols/{id}/images/...` → Read 逐張檢查 → commit。
> 以下舊記錄保留存查，但**不應再作為「雲端 session 看不到圖」的依據**——
> 那會讓 Claude 誤以為自己無法自行審圖，把該做的品質把關丟回給使用者。

**（歷史記錄）症狀**：在雲端 Claude Code session 裡用 `curl` 下載 `d8j0ntlcm91z4.cloudfront.net` 的圖片，收到 403 Forbidden。  
**原因**：Higgsfield CDN 會擋伺服器端的未授權請求。  
**當時解法**：改用 `raw.githubusercontent.com` 來存取已經 push 到 GitHub 的圖片：
```
https://raw.githubusercontent.com/pennyhuang-oss/Virtual_KOL_Studio/<commit-sha>/kols/<kol-id>/images/...
```

---

### 問題 5：圖片上傳到 GitHub 的錯誤位置

**症狀**：圖片上傳後跑到 `images/` 根目錄，而不是 `images/soul_test_v1/` 子資料夾。  
**正確資料夾結構**：
```
kols/<kol-id>/images/
├── face_reference/     ← 臉部參考圖（4 張）
└── soul_test_v1/       ← Soul 訓練後測試圖（6 張以上）
```
**解法**：從雲端 session 下載 raw.githubusercontent.com 的圖片，然後用 git 搬移並重新 push：
```bash
# 下載圖片
curl -s -o "/tmp/img.png" "https://raw.githubusercontent.com/..."

# 搬到正確位置
mkdir -p kols/<kol-id>/images/soul_test_v1/
cp /tmp/img.png kols/<kol-id>/images/soul_test_v1/

# 刪掉錯誤位置
git rm kols/<kol-id>/images/img.png

# commit & push
git add kols/<kol-id>/images/soul_test_v1/
git commit -m "..."
git push origin claude/kol-personality-training-9otdaw
```

---

### 問題 6：換裝置後 git 指令無法執行（Windows PowerShell）

**症狀**：在 PowerShell 執行 git 指令，出現「無法辨識 'git'」錯誤。  
**原因**：Windows PowerShell 預設不一定能找到 git；或目前所在目錄不是 git repo 的根目錄。  
**解法**：
- 不需要在本機執行 git，全部透過 Claude（雲端 session）操作
- Claude 在雲端 session 已有完整的 repo clone，可以直接 commit 和 push
- 如果需要在本機操作，使用「Git Bash」（Windows 安裝 Git for Windows 後會有）而不是 PowerShell

---

### 問題 7：雲端 session vs 本機 session 的差異

| 功能 | 雲端 session | 本機 session |
|------|-------------|-------------|
| 呼叫 Higgsfield MCP | ✅ | ✅ |
| 顯示生成圖片 | ✅（需開啟 Display Result） | ✅ |
| 啟動 Soul 訓練 UI | ✅（直接 API 呼叫） | ✅ |
| 下載 Higgsfield CDN 圖片 | ❌（403 Forbidden） | ✅ |
| 下載 raw.githubusercontent.com | ✅ | ✅ |
| git commit & push | ✅（透過 repo clone） | ✅ |

**結論**：訓練流程可以全部在雲端 session 完成。唯一限制是無法直接下載 Higgsfield CDN 圖片，但可以繞過（先 push 到 GitHub 再用 raw URL 讀取）。

---

## 每個 KOL 的資料夾結構

```
kols/<kol-id>/
├── character.md              ← 人格設定（含 Soul ID）
├── profile.json              ← 結構化資料（含 ai_generation）
├── content_style.md          ← 內容風格指南
├── script_self_intro.md      ← 自我介紹腳本
├── edit_timeline_self_intro.md ← 剪輯時間軸
├── generation_notes.md       ← AI 生成記錄（Soul ID、prompt、圖片連結）
└── images/
    ├── face_reference/       ← 臉部確認圖（4 張）
    └── soul_test_v1/         ← Soul 訓練後測試圖（6 張以上）
```

---

## 新裝置上手步驟

1. 打開 Claude（網頁版 claude.ai 或 Claude Code）
2. 確認 Connectors 裡 higgs 已連接且所有選項已勾選
3. 讓 Claude 讀取這份文件：
   ```
   請讀取 https://github.com/pennyhuang-oss/Virtual_KOL_Studio/blob/claude/kol-personality-training-9otdaw/KOL_TRAINING_SOP.md 並繼續訓練下一個 KOL
   ```
4. Claude 會自動知道進度、下一個要做誰、以及所有注意事項

---

## Higgsfield Soul V2 使用規則

- 模型名稱：`soul_2`（generate_image 裡用 `model: 'soul_2'`）
- 參數：`soul_id: '<soul_id>'`
- **不要**另外傳入 medias 作為臉部參考——Soul ID 本身就是身份
- 支援 aspect_ratio：`9:16`（直式）、`1:1`、`16:9`（橫式）
- 每次最多生成 4 張（count: 1–4）
- **⚠️ soul_id 只能用於靜態圖片生成**，影片生成中的臉部鎖定靠 `start_image` 參數（見下方舞蹈影片 SOP）

---

## 舞蹈影片生成流程（TikTok 熱梗舞）

> 完整 SOP 見 `DANCE_VIDEO_SOP.md`

**使用模型**：`seedance_2_0`（音樂同步，臉部鎖定）

**快速流程**：

```
1. media_upload + media_confirm → audio_media_id
2. soul_2 生成 start frame（THREE QUARTER SHOT）→ rawUrl
3. media_import_url → image_media_id
4. seedance_2_0（start_image + audio_references + generate_audio=False）→ 舞蹈影片
5. CapCut 後製：拖入 mp3，對齊開頭，導出
```

**適用所有 KOL**，每個 KOL 只需替換 soul_id 和服裝描述。
