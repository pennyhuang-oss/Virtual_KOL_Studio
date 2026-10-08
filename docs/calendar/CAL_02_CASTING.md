# CAL_02 — 選角比較與推薦名單（TASK-CAL-001／R1，R2 修正版）

> **R2 狀態**：R1 的 12 位保留為**工作名單，不是定案**。R2 的修正以「R2 修正」標出；臉部比較見 `CAL_06_FACES.md`，替代選圖見 `CAL_07_PICKS_RETRIEVAL.md`。

> **建議稿，未經 Penny 拍板。** 人選、月份、美術方向都還沒定案。
> 客觀欄位（年齡、族裔原文、型錄連結、Soul ID、碰撞距離）見程式產生的 [`CAL_02b_CANDIDATES.generated.md`](CAL_02b_CANDIDATES.generated.md)；
> 圖片請直接看 [`casting_board.html`](casting_board.html) 或 [`sheets/CAL_R1_candidates_18.jpg`](sheets/CAL_R1_candidates_18.jpg)。

## 1. 來源與方法

| 來源 | 用途 | 查證結果 |
|---|---|---|
| 型錄 `https://kol-catalog-production.up.railway.app/kols.html` | 現有收錄名單 | 2026-10-08 抓下的線上 `kols.html` 與 repo `catalog/public/kols.html` **逐位元組相同**；38 位 |
| `kols/{id}/profile.json` | 年齡、族裔、出身地（亞洲背景依據）、Soul ID | 本 repo 31 位有設定檔；型錄另外 7 位屬 showgame-kol／Buildup_KOL，本 repo 沒有設定檔 |
| `review/soul_training/SOUL_IDS.json` | Batch 3 Soul ID 交叉核對 | 主角與備選中的 Batch 3 全部一致 |
| `review/soul_pilot/_screen19_v1/screen19_pairs.json` | 臉部碰撞距離（遮髮量測，171 組） | 只涵蓋 Batch 3 的 19 位；原 11 位與 Nico 沒有 |
| `review/soul_training/RULING_collision_accepted.md` | 規則 C-2：有碰撞關係（≤0.0220）的兩位不得出現在同一則內容 | 一本桌曆把 12 位放在一起，視同同一則內容處理 |
| 實際圖片 | 個別與整組比較 | 每位至少看過型錄精選圖；入圍 18 位再看 repo 全部原圖（不含失敗稿） |

**沒有用的判斷依據**：名字、簡介、國籍配額、圖片張數。張數只用來判斷「素材夠不夠、要不要補」。

## 2. 篩選漏斗

| 階段 | 人數 | 說明 |
|---|---|---|
| 型錄收錄 | 38 | |
| 排除非亞洲設定 | 36 | camille-dupont（法國）、aaliya-okonkwo（拉丁裔） |
| 排除型錄圖為男性形象 | 33 | xiaoxiao-tan、loima-cheung、leon-lim（xiaoxiao-tan 是否設定錯置，未確認） |
| 亞洲女性、成年 | 33 | 全部設定 ≥ 20 歲 |
| 依設定＋圖片初篩 → 入圍比較 | **18** | 排除理由見 §6 |
| 推薦 | **12 主角＋2 備選** | 另 4 位落選但列入比較，方便 Penny 對照 |

## 3. 個別比較（18 位）

> 用「高／中／低」描述，不用分數。每格都是看圖後的主觀判斷，依據寫在 `casting_board.html` 各人卡片。

| 人設 | 角色 | 臉部吸引力／甜美 | 性感表現／親近感 | 既有模型臉部一致性 | 橫／直構圖可用性 | 素材與補生成需求 |
|---|---|---|---|---|---|---|
| iris-chen | 主角 1 月 | 高／高 | 中高／高（現成圖從街拍到內衣都有） | 高（Seedream 訓練集與 Soul 後的圖是同一張臉） | 橫半版、直滿版都成立 | 充足，不需補 |
| kanon-komori | 主角 2 月 | 高／高 | 高／中 | 高（Soul 驗證 6/6） | 都成立（全身照人物太小已剔除） | 只有 12 張，夠用 |
| luna-tanaka | 主角 3 月 | 高／高 | 中／高 | 高 | 都成立，但原圖 1152 px 寬 | 解析度邊緣、1 張要修假介面字 |
| angel-chiu | 主角 4 月 | 中高／中 | 中高／中 | 高 | 都成立 | 只有訓練圖，夠用 |
| somi-oh | 主角 5 月 | 中高／高 | 中／高 | 高 | 都成立 | 直式那張偏「吃播」不偏甜；可取回 daily_v2 原圖替換 |
| vicky-lin | 主角 6 月 | 中高／中 | 高（體態）／中 | 中（v3/v4 錨定後才穩） | 都成立 | 1 張要修 Nike 勾勾 |
| coco-wu | 主角 7 月 | 高／高 | 中高／最高 | 中（各輪 face_reference 略有差異） | 都成立 | 充足 |
| mia-huang | 主角 8 月 | 中高／高 | 中／高 | 中（只用 training_v1） | 都成立 | 充足；紫光色偏需打樣 |
| yuna-kim | 主角 9 月 | 高／中 | 中／中 | 高 | 都成立，直式原圖 1152 px 寬 | 直式那張要修花紋、解析度邊緣 |
| tammy-chou | 主角 10 月 | 中高／中 | 中高／中 | 高 | 直式成立；**橫式沒有合格圖** | 橫式需取回 daily_v2 原圖或補生成 1 張 |
| rin-ayase | 主角 11 月 | 高／中 | 最高（不靠暴露）／低 | 高 | 都成立（直式臉偏小） | 只有訓練圖，夠用 |
| rainie-hsu | 主角 12 月 | 中高／低 | 高／低 | 中（只有 training_v2 那組是同一張臉） | 都成立（直式人物偏小） | 橫式那張要修假日期戳 |
| wanyin-jiang | 備選 | 中高／中 | 中／中 | 高 | 都成立 | 夠用 |
| sophia-tseng | 備選 | 中高／中 | 中高／中 | 中（只能用 training_v1） | 橫式成立；直式候選是背影 → 換圖 | training_v1 還有 12 張可挑 |
| miu-shiraishi | 落選 | 高／高 | 中／高 | 高 | 都成立 | 落選原因是碰撞，不是素材 |
| jia-seo | 落選 | 中高／低 | 中／中 | 高 | — | 碰撞＋偏冷 |
| peggy-lee | 落選 | 中高／中 | 中高／中 | 高 | — | 碰撞＋與 rin 撞色 |
| yerin-han | 落選 | 中高／中 | 中／中 | 高 | — | 碰撞＋與 vicky 路線重疊 |

## 4. 推薦名單：12 主角＋2 備選

| 月 | 人設 | 一句話推薦理由 | 最大缺點 |
|---|---|---|---|
| 1 | **iris-chen** 陳芯語 | 最甜的鄰家圓臉，素材最多，適合當開場 | 長直黑髮與 rainie 同路線 |
| 2 | **kanon-komori** 小森花音 | 粉紫長髮＋女僕咖啡廳，甜與性感兼具 | 女僕裝的尺度要 Penny 確認 |
| 3 | **luna-tanaka** 田中ひな | 黑色齊瀏海鮑伯，辨識度最高的髮型 | 原圖解析度邊緣 |
| 4 | **angel-chiu** 邱安晴 | 高瘦窄臉、棕金漸層，碰撞表中最乾淨 | 與原 11 位沒量測 |
| 5 | **somi-oh** 오소미 | 銅橘短髮、爽朗暖色 | 現有直式圖不夠甜 |
| 6 | **vicky-lin** 林薇淇 | 唯一深膚色與運動體態 | 早期圖臉不穩，只用錨定後的 |
| 7 | **coco-wu** 吳可可 | 笑得最開、親近感最強 | 背景人像牆會分散注意（見 CAL_11）；是否用校園／制服造型屬 Penny 的尺度選擇，不是預設禁止（R2 修正） |
| 8 | **mia-huang** 黃米亞 | 灰金挑粉短髮＋霓虹電競房 | 臉在不同批次之間會飄 |
| 9 | **yuna-kim** 김하은 | 韓系素顏清透 | 直式圖要修花紋 |
| 10 | **tammy-chou** 周語彤 | 蜜金大波浪，整組最亮的髮色 | 橫式沒有合格現成圖 |
| 11 | **rin-ayase** 綾瀨凜 | 酒紅長捲髮、成熟性感 | 直式圖臉偏小 |
| 12 | **rainie-hsu** 許雷妮 | 濃妝立體、年末派對感 | 舊資料夾是另一張臉，不可混用 |
| 備選 1 | **wanyin-jiang** 江晚吟 | 旗袍古典，可替 iris 或 rainie | 與 rin 0.02234，接近門檻；差異部分來自造型 |
| 備選 2 | **sophia-tseng** 曾詩妃 | 28 歲貴婦感，可替 rin 或 yuna | 只能用 training_v1；直式要換圖 |

**為什麼備選是這兩位**：備選要能直接頂替某位主角而不製造新碰撞。wanyin 與 5 位 Batch 3 主角的既有碰撞值都 > 0.0220（照錄，**未觸發門檻不等於辨識度已通過**）；sophia 屬原 11 位，**沒有被量測過**——R1 寫成「不在碰撞表內」容易被讀成「不會碰撞」，R2 更正：**未量測不等於不碰撞**，她與 12 位的臉部差異只能看 R2 的遮髮比較圖（`r2/faces/CAL_R2_faces_B_extra.jpg`）目視判斷。
相反地，miu-shiraishi 雖然個人吸引力高，卻同時與 kanon、somi 碰撞——**她沒辦法單獨頂替任何一位**，所以不當備選。

## 5. 整組比較：12 位放在一起能不能看出是 12 個不同的人

### 5.1 差異從哪裡來

| 維度 | 12 位的分佈 | 判斷 |
|---|---|---|
| 髮色 | 黑：iris、rainie、luna、vicky｜深棕：coco、yuna｜粉紫：kanon｜灰金挑粉：mia｜銅橘：somi｜蜜金：tammy｜酒紅：rin｜棕金漸層：angel | 分散；黑髮 4 位但髮型各不同 |
| 髮長／髮型 | 長直：iris、rainie、angel｜長捲：coco、tammy、rin｜長髮瀏海：kanon｜及肩微捲：yuna｜齊瀏海短鮑伯：luna｜短捲：mia｜短髮：somi｜高馬尾：vicky | 分散 |
| 臉型（目視，未量測） | 圓臉：iris、luna、coco｜窄臉尖下巴：angel、rainie｜鵝蛋：yuna、rin、tammy、kanon｜運動型：vicky｜圓潤：somi、mia | 圓臉 3 位，但髮型完全不同 |
| 膚色 | 白皙 11、小麥 1（vicky） | 集中 |
| 身形 | 嬌小：luna、coco、mia｜高瘦：angel、rin｜運動：vicky｜豐滿：kanon、iris｜其餘一般 | 分散 |
| 氣質 | 鄰家甜、偶像甜、清純、元氣、俏皮、清透、時髦、爽朗、運動、知性性感、夜晚成熟、派對濃豔 | 分散 |
| 場景（以選定的 24 張計） | 街頭：iris、luna、yuna 的直式｜咖啡／餐飲：iris、luna、kanon 的橫式、somi 直式｜臥室／飯店：angel、rin、somi、coco｜職場：angel（醫院）、tammy（網拍倉庫）｜霓虹房：mia｜球場：vicky | 室內偏多 |
| 拍攝方式 | 選定 24 張中自拍約 4 張（rainie、mia、coco 橫式；tammy 橫式已判不採用）；但各人 repo 全部素材裡自拍與鏡子自拍比例高 | 自拍偏多是現有素材的共同弱點 |

### 5.2 已知的集中與風險（不只寫優點）

1. **差異有相當比例靠髮色承擔。** 這是 repo 已知事實：Batch 3 碰撞量測是遮髮做的，裁決後規則 C-1 明訂「髮型是身分區分要件」。本名單在 Batch 3 內已避開所有 ≤0.0220 的配對，但**原 11 位彼此、以及原 11 位與 Batch 3 之間沒有量測**。
   → 建議下一輪做一次 0 credits 的「12 人遮髮並排」目視檢查（同 repo 對 19 位做過的方法），確認拿掉髮色後臉仍不同。
2. **iris 與 rainie** 同為長直黑髮的台灣女生，是 12 人中目視最可能被說「像」的一對（臉型與妝感不同，但沒有量測）。若 Penny 並排後覺得像，備選 wanyin 不能解決（她也是長直黑髮），應改用 sophia 或從落選中重挑。
3. **台灣設定 7／12。** 國籍不是配額，這裡只是記錄：國籍集中不等於長相集中，但若收件對象在意「跨國陣容」，可用備選或 miu 組合調整。
4. **現有素材的質感不一致**：iris、luna、yuna 的圖是 Seedream 底片感，Batch 3 是 Soul V2 數位感；日夜、室內外也是隨機。這不影響「12 個不同的人」，但會影響整本的完成度，處理方式見 CAL_03 製作路線。
5. **性感的來源差異**：rin、rainie 靠氣質與服裝質感；vicky 靠體態；kanon、coco、iris 有明顯胸型展示。若 Penny 選較保守的尺度（見 CAL_04），kanon 與 coco 的現成圖要換。

### 5.3 若 Penny 想調整的替換組合（已先算過碰撞）

| 想要 | 建議組合 | 代價 |
|---|---|---|
| 放 miu（白金鮑伯） | **出 2 位**（kanon、somi，兩人都與 miu 有既有碰撞值 ≤0.0220）→ **進 2 位**：miu＋另一位（候選如 wanyin：與 miu 0.0255、與 rin 0.02234；或 ananya、wendy、sophia——後三位與 miu 的距離沒有量測或未觸發門檻，仍需目視）。R2 更正：R1 只寫「補一位」，容易被讀成 11 人 | 少了粉色與銅橘兩個髮色 |
| 降低台灣比例 | wanyin 替 rainie（或 iris） | 長直黑髮問題不變 |
| 想要一位冷感反差 | wendy-yeo（銀灰鮑伯）替 yuna | 甜美度下降；wendy 與 5 位 Batch 3 主角的既有碰撞值都 > 0.0220（照錄；與原 11 位沒有量測）。R2 已補 3 張既有圖比較（`r2/assets/CAL_R2_assets_wendy-yeo.jpg`） |
| 想加入 ananya-kapoor | ~~替任一位~~ **R2 撤回「可替任意人」的承諾**：她沒有任何臉部量測，素材只有 repo 的 10 張（1152 或 1728 px），月份與版面要另評估。R2 已補 3 張既有圖比較（`r2/assets/CAL_R2_assets_ananya-kapoor.jpg`、`r2/faces/CAL_R2_faces_A_extra.jpg`） | 屬 Penny 的人選決策 |

## 6. 篩選前即排除（與落選理由）

| 人設 | 理由 |
|---|---|
| nico-tsai | 灰棕短鮑伯、冷調時髦，不屬甜美方向；Phase D 待裁決；未納入碰撞篩檢 |
| zoey-yeh、zhiyi-shen、nanami-fujiwara、cheryl-soh | 都是長直黑髮，與 iris／rainie 同類；nanami 9 組碰撞（含 kanon 0.01741），cheryl、zhiyi 各 6 組 |
| ruoruo-tang、sydney-leong | 碰撞組數最多（11、10），最不利於展示差異 |
| emma-kao | 主播知性成熟路線；與 rin 0.01863 碰撞 |
| angeline-kwee | 奶茶灰棕長捲髮與 tammy、angel 髮色區間重疊；與 peggy 0.01788 |
| wendy-yeo | 銀灰鮑伯辨識度很高，但冷酷中性、不符甜美方向（保留為反差選項） |
| ananya-kapoor | ~~本輪以東亞甜美方向為準未入選~~ **R2 修正：刪除「東亞」限制（Penny 沒有指定）**。她是亞洲（印度旁遮普）設定、成年，深膚色與長捲髮在 12 人中差異最大。R1 未入選的真正原因只剩「沒有臉部量測、可用素材少」，不是族裔。R2 已補 3 張既有圖，列入 Penny 人選決策（CAL_10） |
| faye-tan、rachel-ong、kai-luo | 本 repo 無設定文件與 Soul ID；型錄圖為紀實／冷調（設定 30、34、27 歲），不符「漂亮、性感、甜美」 |
| nova-lin | 型錄族裔欄為空、設定是 AI 數位人，亞洲背景無法以設定文件查證；Soul ID 未確認 |
| miu-shiraishi、jia-seo、peggy-lee、yerin-han | 入圍比較後落選，理由見 §3 與 `casting_board.html` |

## 7. Soul ID 查證狀態（摘要）

- 12 主角＋2 備選全部在 `kols/{id}/profile.json` 有 Soul ID；其中屬 Batch 3 的 6 位（rin、kanon、tammy、somi、angel、wanyin）與 `SOUL_IDS.json` 一致，狀態 `production_ready`；屬原 11 位的 8 位（iris、luna、yuna、rainie、coco、mia、vicky、sophia）狀態 `ready`（`SOUL_IDS.json` 只收 Batch 3，無從交叉核對）。
- rainie-hsu 有兩組：`994e33d2…`（deprecated，身材不符被棄用）與 `a4a000fe…`（ready，v2）。**只有 v2 能用**，素材也只用 `training_v2/`。
- **本輪沒有在 Higgsfield 端查驗任何 Soul ID**（只核對 repo 紀錄），所以「平台上仍存在且可用」標為未確認。
- 完整 ID 見 `CAL_02b_CANDIDATES.generated.md`。
