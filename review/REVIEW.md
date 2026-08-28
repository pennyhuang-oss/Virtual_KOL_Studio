# Nico Pilot — 覆核檔案（自給自足，只讀這一份就夠）

## §0 給審閱者

**你只需要讀這一個檔案。** 不要用 GitHub 連接器去抓 repo 裡的其他檔案——
這個專案光 `.md` 就約 500KB，爬完會把使用者的方案用量燒光，而你真正需要的內容全在這裡。

**回覆方式**：把你的意見**直接寫在本檔案最下方 §9 回覆區**（在 `REPLIES BELOW` 那行以下）。
那一段不會被自動產生覆蓋。Claude 會讀你寫的內容並修正。

- 目前 commit：`5a30842`
- 檔案角色：本檔 §0–§8 由 `tools/gen_review_file.py` 從 `pilot/nico_pilot.json` 自動產生，所有數字都是程式算的，不是人工抄的

---

## §1 這個專案在做什麼

**Virtual KOL Studio** 是一個虛擬 KOL（AI 生成的網紅角色）資料庫。每個角色有完整人設，
用 AI 生圖平台 Higgsfield 產生素材，發布到 Instagram / TikTok / X。

內容方向是模仿日本 AV 女優公開社群帳號的風格，強調**寄生親密感**——讓粉絲感覺
「偷窺到她的私下生活」。所有素材維持 SFW（不露骨、不涉及未成年）。

### 什麼是「建模照」

要讓同一個虛擬角色在不同素材裡長得像同一個人，必須先訓練一個專屬的身分模型
（Higgsfield **Soul V2**）。訓練完成得到一個 `soul_id`，之後所有生成都掛這個 id。
**建模照**就是拿去訓練這個模型的那組照片。

**關鍵技術限制**：Soul V2 不繼承訓練圖的髮型與髮色，每次生成都要在 prompt 裡重寫。

### 目前進度

- repo 裡已有 **6 個角色的 Soul 訓練完成**並在生產環境用了數週
- 現在要新增 20 位（Batch 3），**Nico Tsai 是第一個 pilot**，走完整流程驗證方法
- **尚未生成任何一張圖**。這份規劃通過覆核才會開始花錢

### 為什麼挑 Nico 當 pilot

26 歲台灣籍美甲師，**短鮑伯 + 冷灰奶茶漂色 + C 罩杯纖細身材**——
是全批 20 位裡最容易失敗的組合（模型傾向把所有人畫成豐滿、把漂色畫成銀白、把短髮加長）。
而且她在第一輪已經失敗過一次，有前後對照價值。

---

## §2 流程：四個階段

| 階段 | 內容 | 張數 | 目的 |
|------|------|------|------|
| **A 選角** | 4 個候選 identity | 4 | 挑出「臉＋上半身輪廓」成立的那一個 |
| **B 錨定驗證** | Reference Element + B1/B2 | 2 | B1 驗能不能重現、B2 驗能不能輕度外推。身材比例的最終把關在這裡 |
| **C 訓練集** | 正式建模照 | 20 | 送進 Soul 訓練 |
| **D 壓力測試** | 訓練後的漂移測試 | 13 | 這個 repo 從來沒做過的一步 |

### Phase A 為什麼是「4 個候選人」不是「同一人的 4 個視角」

這個 repo 自己的歷史證實：另一個角色 Rainie 的 4 張候選圖是**各自獨立生成的 4 個人**，
身材差異大到後來必須換錨點、整批 13 張訓練圖與一個 soul_id 全部作廢重做。
所以不可假設「4 次無錨定呼叫會得到同一個人」。

### 訓練張數的實際限制

直接讀本專案實際呼叫的 API 工具 schema（`show_characters(action='train')`），逐字內容：

```
train (needs `name` + 5-20 ref images, ~10 min, non-blocking) / Required with medias to total 5-20 images for action=train
```

→ **5–20 張**。（官網 Help Center 寫 minimum 20，那是 Web UI 規格，與本專案使用的 API 不同。）

---

## §3 這個專案的既有規則（判斷時請以這些為準）

### 3-1 人設憲章

1. **反差公式**：檯面上是公開面貌（日常、得體）；私底下在自己的私人平台展現性感的一面。
   **不是**「回家就鬆垮邋遢」。**檯面 ≠ 職業**——不公開職業本身就是成立的設定。
2. **標誌性場景配額**：泳池、和服、女僕裝、直播間等高辨識度場景不得成為主支柱或超過 25%。
   判斷法：「如果這個設定成立，她一年 365 天會不會有 300 天都長這樣？」
3. **造型可變**：髮色髮型是現階段設定，不是永久鎖定。
4. **不寫絕對禁令**：用「預設、多數時候」「不常見（不是不可能）」。
5. **單一真理來源**：支柱以 JSON 為準，全檔同步。

### 3-2 造型差異化四轉盤

來自拆解一個競品帳號（全 AI 生成的虛擬 KOL，57 萬粉，抽樣 60 則貼文 109 張圖）。
核心診斷：**把「造型」綁死在「內容主題」上，每個角色會被自己的人設關進一個房間。**

| 轉盤 | 規則 |
|------|------|
| 穿搭 | 每位至少 8 種明顯不同的風格區間；連續兩則不得同區間；招牌風格 ≤30% |
| 髮型 | 至少 5 種變體，**每則明確指定**，不可讓模型自己決定 |
| 地點層級 | 每 10 則：A 級 2–3、B 級 4–5、**C 級至少 2（硬性下限）** |
| 微物件 | 每則至少換 2 樣，**prompt 中必須具體點名** |

**地點三層級**：**A**＝一般人做不到的（遊艇、五星飯店套房、豪華 villa）；
**B**＝偶爾會去的（咖啡廳、餐酒館、自宅、工作場所）；
**C**＝天天在做且完全不美的（賣場、超商、加油站、洗衣店、藥妝店、車站月台、早餐店）。

> **C 級是整套系統的靈魂。** 全部都是 A 級的帳號讀起來像型錄。
> 競品敢在 57 萬粉的帳號上發 Costco 推推車、麥當勞飲料杯——
> 正是這些一點都不美的地方，讓觀眾相信「她是個剛好很有錢的真人」。

### 3-3 五段式物理光線公式

拆解競品 31 張素材後的結論：**她做對的不是把光線寫得更漂亮，
而是把光線寫成「物理規格」而不是「品質形容詞」。**
寫 `golden hour`、`crisp`、`well-exposed` 只告訴模型「要好看」，
沒告訴它「光從哪來、被什麼反射回來、哪裡該暗」——**這正是 AI 感的主要來源**。

每個 prompt 的光線要寫滿五段：

| 段 | 內容 |
|----|------|
| ① KEY | 具名、畫面內可指認的光源＋方向＋高度 |
| ② BOUNCE | **具名的物理反射面**＋它把什麼顏色的光丟回主體（最大的缺口）|
| ③ 色溫分裂 | 畫面裡同時存在的兩個色溫（**可為 null，不強制**）|
| ④ 曝光取捨 | 相機對什麼測光，因此什麼被允許過曝或壓黑 |
| ⑤ 遮擋/框架 | 鏡頭與主體之間形塑光線的實體 |

**bounce 要區分**：`diffuse`（白牆／床單／淺色地板，能整體補亮）
vs `specular`（鏡面／玻璃／金屬／烤漆，只產生高光，不能當柔和填光）。

### 3-4 其他硬規則

- **服裝五層**：上身（單品＋材質＋顏色＋**領型**）＋下身＋鞋＋包或外套＋首飾髮飾。
  只寫 `casual top and shorts` 一律退回。不寫領型模型會自補低胸，導致身材判讀失真。
- **自拍/他拍混合**：自拍要寫 `front camera quality, slightly softer focus, NOT ultra-crisp`；
  他拍才用 `crisp sharp focus`。
- **皮膚質感**：每個 prompt 加 `visible skin pores, natural skin imperfections`，
  **避免** `smooth`／`flawless`／`airbrushed`／`porcelain skin`。
- **膚色**：全批一律白皙瓷感，明確排除 `tanned`／`bronzed`／`olive`／`deep golden`。
- **模型選擇**：選角階段用 `seedream_v4_5`。**不可用 `soul_2`**——
  沒有 soul_id 錨定時它每次呼叫都會重新想像一張臉。

---

## §4 前四輪覆核發生過什麼（你的前任意見與 Claude 犯過的錯）

| 輪次 | 發現的主要問題 |
|------|---------------|
| R1 | Claude 自己發明「攝影棚定裝照」，違反 6 條 repo 早就寫好的規則。實際出圖把泡棉板、棚燈、門框、相機全畫進畫面；景別指令失效（指定臉部特寫出成全身）；髮色從冷灰奶茶變銀白 |
| R2 | Claude 寫了一支「為了讓 validator PASS 而改資料」的程式，它只改 outfit/hair 數字沒動 scene 文字 → 12 列服裝衝突、14 列髮型衝突；濾鏡與視角用列位置指派 → 20 位的第 1 列全是 meitu＋自拍 |
| R3 | 覆核包統計與 JSON 漂移（寫 5 種 lighting 實際 6 種、寫 L1×3 實際 ×5、寫 4+4 場景實際 3+3）。原因是人工抄寫 |
| R4 | `schema_v2.json` 根本沒被執行（對抗測試：注入非法 enum 仍 PASS）；anchor 的 scene 寫「坐著」但欄位是 `standing`；label override 可用一個理由同時放行兩欄 |

**共同模式**：Claude 反覆犯的是同一類錯——**改了一個欄位，沒有同步改另一個**，
以及**把規則形式化之後，對規則本身過度擬合**（為了湊 quota 把普通場景標成 A 級）。

目前這一版是 R4 的 11 條全部處理完之後的結果。

---

## §5 現行規格（全部由 JSON 計算）

### 5-1 身分規格

- 年齡／族裔：26 / Taiwanese
- 膚色：light neutral-to-cool skin tone, natural tonal variation across face and body, subtle normal redness at cheeks, elbows and knuckles, not overexposed
- 排除：NOT tanned, NOT bronzed, NOT olive, NOT deep golden or wheat-colored
- 臉部基底：fine elongated phoenix eyes, cool composed expression, delicate features
- **身分 marker**（讓模型學到「某一個具體的人」而不是 generic beautiful East Asian woman）：
  - left eyebrow tail sits subtly higher than the right, most visible when she smiles
  - a very small pale mole beside her right nostril
  - flat cupid's bow — the upper lip has almost no M-shaped peak
  - slightly wider-than-average inter-eye distance
  - narrow rounded nose tip with a soft, undefined bridge break
- 註：前三項在自拍／鏡像生成時可能左右翻轉，因此後兩項刻意選用**不依賴左右方向的骨相特徵**（眼距、鼻頭形狀），確保翻轉後身分仍可辨識。不寫 `2mm` 這種模型無法穩定執行的幾何單位。
- 身材數字（metadata）：{'height_cm': 167, 'weight_kg': 49, 'bust_cm': 86, 'waist_cm': 59, 'hip_cm': 88, 'cup': 'C', 'leg_cm': 82}
- **身材視覺比例（prompt 實際使用）**：narrow shoulders roughly equal to hip width, long torso, small natural bust with a shallow curve, visible collarbone and sternum, slim upper arms with no muscle definition, long straight legs, flat lower abdomen; overall silhouette is narrow and elongated
- 排除：NOT voluptuous, NOT heavy-chested, NOT curvy, NOT athletic-muscular

### 5-2 造型庫

| ID | 區間 | 領型 | 上身 | 下身 | 鞋 | 包/外套 | 首飾 | 身材可讀 |
|----|------|------|------|------|----|---------|------|---------|
| `01` | ★極簡職人 | high mock neck | 炭灰色合身羅紋針織長袖，高領貼頸 | 黑色高腰直筒西裝褲 | 黑色皮革樂福鞋 | 米色帆布托特 | 銀色細戒指＋銀色小圈耳環 | ✅ |
| `02` | 極休閒 | straight neckline spaghetti strap | 米白色棉質細肩帶背心，一字平口 | 灰色棉質及膝短褲 | 赤腳 | 薄針織開襟外套（脫下搭在椅背） | 銀色細項鍊 | ✅ |
| `03` | 日常有型 | crew neck | 奶油色短版針織上衣，圓領 | 高腰淺色直筒牛仔褲 | 白色球鞋 | 深棕小方包 | 銀色圈形耳環 | ✅ |
| `04` | 學院感 | collared button-down, top two buttons open | 白色寬版襯衫 | 黑色百褶短裙 | 黑色瑪莉珍鞋 | 灰色及膝襪 | 銀色髮夾 | ❌ |
| `05` | 街頭 | crew neck, cropped hem | 黑色短版帽T | 灰色工裝寬褲 | 厚底球鞋 | 黑色斜背小包 | 銀色耳骨夾 | ❌ |
| `06` | 上班正式 | square neckline camisole under blazer | 燕麥色西裝外套＋白色絲質方領背心 | 同色系直筒寬褲 | 尖頭平底鞋 | 結構皮革包 | 銀色細手鐲 | ❌ |
| `07` | 派對夜間 | straight neckline, open back | 黑色細肩帶絲質長洋裝（露背） | （連身） | 銀色細跟涼鞋 | 金屬扣手拿包 | 銀色手環 | ✅ |
| `08` | 居家貼身 | modest scoop neck | 灰色貼身棉質長袖上衣 | 黑色棉質貼身長褲 | 室內拖鞋 | 無 | 無 | ✅ |
| `09` | 雨天機能 | high round neck | 深灰防潑水連帽外套＋內搭黑色高領 | 黑色直筒長褲 | 黑色短雨靴 | 防水肩背包 | 無 | ❌ |

**髮型變體**

- `01`：短鮑伯自然放下，一側塞耳後，髮尾內彎
- `02`：短鮑伯全部塞到雙耳後，露出雙耳與後頸
- `03`：鯊魚夾把後半部夾起，前側留兩撮碎髮（工作時）
- `04`：中分吹整、髮尾微內扣，比平時整齊
- `05`：髮尾用電棒外翹，右側夾一支銀色細髮夾
- `06`：剛洗完澡的濕髮，自然往後貼，髮尾滴水

### 5-3 Phase A — 4 個候選 identity

**4 張完全相同**：framing `knee_up`／yaw `left_30`／pose `standing`／view `third_person`／outfit `01`／hair `01`／location `workplace_own_studio`／DOF `adequate`

**唯一變數**：identity（每次獨立生成，得到 4 個不同的人）

**選角服硬性規則**：
- 必須 body_readable=true：軀幹、腰線、肩寬、臀線都要看得出來
- 必須明寫 neckline（此處為 high mock neck）
- 不可用 oversized、寬版襯衫、寬鬆針織、睡袍、浴衣、外套罩住身體
- 必須是日常款，不是招牌極端造型
- 不寫 candid moment——Phase A 是 calibration，需要可比較、可重複的 neutral natural pose
- depth_of_field 一律 adequate，不可 shallow（否則身體輪廓變糊）

**範圍修正**：Phase A 用 knee_up 判的是**臉＋上半身／腰臀輪廓的初選**，不能完整判 leg-to-torso ratio。完整身材比例的 final gate 在 Phase B 的全身驗證圖。先前寫成『Phase A 已完整確認臉＋身材』並不準確。

### 5-4 Phase B

- **B1**（錨點能不能重現）：framing `face_closeup`／yaw `front`／location 同 Phase A 場景／outfit nico_outfit_01／hair nico_hair_01／light 同 Phase A 的乾淨窗光
- **B2**（錨點能不能輕度 generalize（不是 stress test，是中度變量））：framing `full_body`／yaw `right_30`／location park（不同但普通的 B 級場景）／outfit nico_outfit_03（不同但普通的日常穿搭）／hair nico_hair_02／light L6 薄雲天散射光（正常自然光）
- B1/B2 若同場景同服裝同光線，只驗到『能不能重現』，驗不到『能不能輕度外推』。
- B2 的全身圖是身材比例的最終把關點，不是 Phase A。

### 5-5 Phase C — 20 張訓練集（8 clean anchor + 12 lifestyle）

| # | id | 目的 | 場景 | 地點 | 層級 | outfit | hair | framing | yaw | pitch | 表情 | 姿態 | 視線 | 視角 | 臉部 | 光線家族 | bounce | 濾鏡 | 招牌 | 職業 |
|---|----|------|------|------|------|--------|------|---------|-----|-------|------|------|------|------|------|---------|--------|------|------|------|
| 01 | `a01` | identity_core | 咖啡廳靠窗的位子坐著，正對鏡頭，沒有在做任何事 | `local_cafe` | B | `01` | `01` | face_closeup | front | neutral | neutral_relaxed | seated | camera | third_person | unobstructed | L2_single_window_daylight | diffuse | none | — | — |
| 02 | `a02` | identity_core | 同一個位子，身體轉向左邊，臉轉回鏡頭 | `local_cafe` | B | `01` | `01` | chest_up | left_30 | neutral | soft_smile | seated | camera | third_person | unobstructed | L2_single_window_daylight | diffuse | none | — | — |
| 03 | `a03` | identity_core | 白天的人行道上站著，身體轉向右邊，臉轉回鏡頭 | `city_street` | B | `01` | `02` | chest_up | right_30 | neutral | neutral_relaxed | standing | camera | third_person | unobstructed | L6_soft_overcast | diffuse | none | — | — |
| 04 | `a04` | identity_core | 同一段人行道，身體較大幅度轉向左側 | `city_street` | B | `03` | `01` | chest_up | left_60 | neutral | listening_attentive | standing | away | third_person | unobstructed | L6_soft_overcast | diffuse | none | — | — |
| 05 | `a05` | identity_core | 公園長椅上坐著，身體較大幅度轉向右側 | `park` | B | `03` | `02` | chest_up | right_60 | neutral | mid_conversation | seated | away | third_person | unobstructed | L6_soft_overcast | diffuse | none | — | — |
| 06 | `a06` | body_pose_coverage | 公園步道上站著，正對鏡頭，雙手自然垂下 | `park` | B | `03` | `01` | full_body | front | neutral | neutral_relaxed | standing | camera | third_person | unobstructed | L6_soft_overcast | diffuse | none | — | — |
| 07 | `a07` | body_pose_coverage | 同一條步道，身體轉向右側四分之三，臉轉回鏡頭 | `park` | B | `01` | `04` | full_body | right_30 | neutral | soft_smile | standing | camera | third_person | unobstructed | L6_soft_overcast | diffuse | none | — | — |
| 08 | `c01` | identity_core | 鐵門拉下後，坐在工作椅上轉過來看窗外，手還搭在椅背 | `workplace_own_studio` | B | `08` | `01` | face_closeup | front | neutral | neutral_composed | seated | away | third_person | unobstructed | L2_single_window_daylight | diffuse | none | nail_studio | 是 |
| 09 | `c02` | identity_core | 蹲在地上拆剛到的材料紙箱，抬頭看向門口 | `workplace_own_studio` | B | `06` | `04` | chest_up | left_30 | up_10 | mildly_surprised | crouching | away | third_person | unobstructed | L2_single_window_daylight | diffuse | none | nail_studio | 是 |
| 10 | `c03` | identity_core | 早餐店的板凳上等餐，手肘擱在桌沿 | `breakfast_shop` | C | `03` | `04` | waist_up | right_30 | down_15 | tired_soft | seated | down | third_person | unobstructed | L2_single_window_daylight | specular | none | — | — |
| 11 | `c04` | identity_core | 床邊坐著，剛醒還沒站起來，低頭看手機 | `own_bedroom` | B | `08` | `06` | waist_up | front | down_15 | just_woken_blank | seated | camera | selfie_front | partial_hair | L2_single_window_daylight | diffuse | none | — | — |
| 12 | `c05` | body_pose_coverage | 玄關穿鞋，一手扶著牆 | `own_entryway` | B | `04` | `05` | knee_up | left_60 | down_15 | focused | leaning | down | third_person | unobstructed | L3_mixed_warm_cool_practical | diffuse | none | — | — |
| 13 | `c06` | body_pose_coverage | 大安區巷子裡走路，剛越過一台停在牆邊的機車 | `city_street` | B | `03` | `05` | full_body | right_60 | neutral | neutral_walking | walking_frozen | away | third_person | unobstructed | L6_soft_overcast | diffuse | none | — | — |
| 14 | `c07` | identity_core | 低頭替客人上膠，側臉朝向鏡頭 | `workplace_own_studio` | B | `01` | `03` | chest_up | profile_left | down_15 | focused | seated | down | third_person | unobstructed | L3_mixed_warm_cool_practical | diffuse | none | nail_studio | 是 |
| 15 | `c08` | body_pose_coverage | 浴室鏡前修眉，另一手撐著洗手台 | `own_bathroom` | B | `08` | `02` | waist_up | left_30 | up_10 | concentrating_slight_frown | leaning | mirror | selfie_mirror | partial_hand | L8_bathroom_fluorescent | diffuse | none | — | — |
| 16 | `c09` | body_pose_coverage | 便利商店的雜誌架前蹲下來看最下層，回頭 | `convenience_store` | C | `05` | `02` | knee_up | left_30 | up_10 | mildly_annoyed | crouching | camera | third_person | unobstructed | L1_single_ugly_overhead | diffuse | none | — | — |
| 17 | `c10` | environment_stress | 自助洗衣店裡把烘好的衣物從滾筒抱出來，站在機台前 | `laundromat` | C | `09` | `04` | full_body | right_30 | neutral | neutral_composed | standing | away | third_person | unobstructed | L1_single_ugly_overhead | specular | none | — | — |
| 18 | `c11` | environment_stress | 藥妝店貨架前拿護手霜比較成分 | `pharmacy` | C | `05` | `05` | knee_up | front | down_15 | reading_focused | standing | down | third_person | unobstructed | L1_single_ugly_overhead | diffuse | ccd | — | — |
| 19 | `c12` | environment_stress | 捷運月台等車，看著對面的到站顯示 | `train_platform` | C | `06` | `04` | waist_up | right_30 | up_10 | blank_waiting | standing | away | third_person | unobstructed | L3_mixed_warm_cool_practical | diffuse | ccd | — | — |
| 20 | `a08` | identity_core | 公園步道旁站著，整個身體與臉都轉向右側，看著遠處 | `park` | B | `02` | `02` | chest_up | profile_right | neutral | calm_distant | standing | away | third_person | unobstructed | L6_soft_overcast | diffuse | none | — | — |

**每張的光線五段**

- **01 `a01`** ① 咖啡廳的大面窗日光從她左前方 45 度、略高於視線高度進來｜② （diffuse）白牆與淺色地面把光柔和平均地補回她臉的暗面，臉部沒有明顯陰影｜③ **無**（刻意留白）｜④ 對她的臉測光，窗外過曝成白，室內深處落入柔和陰影｜⑤ 無
  - 不完美變數：構圖 centered／動態 none／白平衡 neutral／背景 clean／高光 none／identity_safe True
- **02 `a02`** ① 咖啡廳的大面窗日光從她左前方 45 度、略高於視線高度進來｜② （diffuse）白牆與淺色地面把光柔和平均地補回她臉的暗面，臉部沒有明顯陰影｜③ **無**（刻意留白）｜④ 對她的臉測光，窗外過曝成白，室內深處落入柔和陰影｜⑤ 無
  - 不完美變數：構圖 off_center／動態 none／白平衡 neutral／背景 clean／高光 none／identity_safe True
- **03 `a03`** ① 薄雲天的散射光，沒有硬陰影｜② （diffuse）淺色人行道地面把光均勻補回她右側臉的暗面｜③ **無**（刻意留白）｜④ 對臉測光，天空略過曝，臉部細節完整｜⑤ 無
  - 不完美變數：構圖 centered／動態 none／白平衡 neutral／背景 clean／高光 none／identity_safe True
- **04 `a04`** ① 薄雲天的散射光，沒有硬陰影｜② （diffuse）淺色人行道地面把光均勻補回她左側臉的暗面｜③ **無**（刻意留白）｜④ 對臉測光，天空略過曝，臉部細節完整｜⑤ 無
  - 不完美變數：構圖 off_center／動態 none／白平衡 slightly_warm_auto／背景 moderate／高光 allowed／identity_safe True
- **05 `a05`** ① 薄雲天的散射光，沒有硬陰影｜② （diffuse）淺色人行道地面把光均勻補回她右側臉的暗面｜③ **無**（刻意留白）｜④ 對臉測光，天空略過曝，臉部細節完整｜⑤ 無
  - 不完美變數：構圖 centered／動態 none／白平衡 slightly_warm_auto／背景 moderate／高光 allowed／identity_safe True
- **06 `a06`** ① 薄雲天的散射光，沒有硬陰影｜② （diffuse）淺色步道地面把光均勻地補回她全身，腿與軀幹輪廓清楚｜③ **無**（刻意留白）｜④ 全身在同一個曝光值上，天空略過曝，身體比例完整可讀｜⑤ 無
  - 不完美變數：構圖 centered／動態 none／白平衡 neutral／背景 moderate／高光 allowed／identity_safe True
- **07 `a07`** ① 薄雲天的散射光｜② （diffuse）淺色步道地面均勻補光，側面輪廓與腿身比例清楚｜③ **無**（刻意留白）｜④ 全身同一曝光值，天空略過曝｜⑤ 無
  - 不完美變數：構圖 off_center／動態 none／白平衡 neutral／背景 moderate／高光 allowed／identity_safe True
- **08 `c01`** ① 午後日光從她左前方落地窗、略高於視線｜② （diffuse）白色美甲桌面與白牆把光補回臉的暗面｜③ **無**（刻意留白）｜④ 對臉測光，窗外過曝成白，室內深處落入陰影｜⑤ 無
  - 不完美變數：構圖 off_center／動態 none／白平衡 neutral／背景 moderate／高光 allowed／identity_safe True
- **09 `c02`** ① 落地窗日光從她右後方進來｜② （diffuse）地上散落的白色包裝紙把光反射回她下顎｜③ **無**（刻意留白）｜④ 對臉測光，窗邊過曝，紙箱陰影壓黑｜⑤ 無
  - 不完美變數：構圖 slightly_tilted／動態 minor_hand_blur／白平衡 slightly_cool_auto／背景 heavy／高光 none／identity_safe True
- **10 `c03`** ① 早餐店敞開的門口透進來的晨光從她左前方進來｜② （specular）不鏽鋼桌面把晨光反射回她的下顎｜③ 店內天花板的冷白日光燈落在她的頭頂與肩｜④ 對臉測光，門口整片過曝，店內深處壓黑｜⑤ 門框切掉畫面右緣
  - 不完美變數：構圖 centered／動態 none／白平衡 neutral／背景 moderate／高光 allowed／identity_safe True
- **11 `c04`** ① 窗簾沒拉緊，一道晨光斜落在床上｜② （diffuse）白色床單是大面反射，把光補回她臉的下半｜③ **無**（刻意留白）｜④ 對臉測光，窗簾縫那道光過曝成白帶，房間其餘壓黑｜⑤ 無
  - 不完美變數：構圖 off_center／動態 none／白平衡 slightly_warm_auto／背景 moderate／高光 allowed／identity_safe True
- **12 `c05`** ① 玄關一盞暖黃嵌燈從正上方｜② （diffuse）白色玄關牆把暖光反射回她側臉｜③ 門外樓梯間的冷白日光燈從門縫進來，落在她肩線｜④ 對臉測光，門縫那條冷光過曝，鞋櫃下方壓黑｜⑤ 門框切掉畫面左緣
  - 不完美變數：構圖 slightly_tilted／動態 none／白平衡 neutral／背景 clean／高光 allowed／identity_safe True
- **13 `c06`** ① 陰天的天空散射光，沒有明確方向｜② （diffuse）淺色磁磚牆面把光平均補回她全身｜③ **無**（刻意留白）｜④ 整體低反差，天空過曝成白，這張沒有第二色溫｜⑤ 無
  - 不完美變數：構圖 off_center／動態 subject_motion／白平衡 slightly_cool_auto／背景 heavy／高光 allowed／identity_safe True
- **14 `c07`** ① 可調角度的工作燈近距離直打在手部與桌面｜② （diffuse）白色桌面把光反射回她的下顎與頸｜③ 室內天花板的冷白日光燈落在她後腦與肩｜④ 對手部測光，所以她的臉略暗，背景布簾壓黑｜⑤ 無
  - 不完美變數：構圖 centered／動態 none／白平衡 neutral／背景 clean／高光 allowed／identity_safe True
- **15 `c08`** ① 浴室鏡上方一整條冷白燈管直打｜② （diffuse）白色磁磚牆把光四面反射，幾乎沒有陰影｜③ **無**（刻意留白）｜④ 對臉測光，燈管本身過曝成白條，這張的光很平、不好看｜⑤ 無
  - 不完美變數：構圖 slightly_tilted／動態 none／白平衡 slightly_cool_auto／背景 moderate／高光 allowed／identity_safe True
- **16 `c09`** ① 超商天花板冷白日光燈頂光｜② （diffuse）雜誌封面與白色貨架把光反射回她的下巴｜③ **無**（刻意留白）｜④ 對臉測光，燈管過曝，貨架最下層壓黑｜⑤ 無
  - 不完美變數：構圖 off_center／動態 minor_hand_blur／白平衡 neutral／背景 heavy／高光 none／identity_safe True
- **17 `c10`** ① 洗衣店天花板一整排冷白日光燈管｜② （specular）不鏽鋼機身把光以高光的形式打回來，不是柔和填光｜③ **無**（刻意留白）｜④ 對臉測光，燈管與不鏽鋼高光整片過曝，牆角壓黑｜⑤ 無
  - 不完美變數：構圖 centered／動態 none／白平衡 slightly_cool_auto／背景 heavy／高光 heavy／identity_safe True
- **18 `c11`** ① 藥妝店冷白日光燈頂光｜② （diffuse）貨架上的白色包裝把光反射回她胸口與下巴｜③ **無**（刻意留白）｜④ 對臉測光，燈管過曝，貨架深處壓黑｜⑤ 無
  - 不完美變數：構圖 off_center／動態 none／白平衡 color_cast_from_environment／背景 heavy／高光 allowed／identity_safe True
- **19 `c12`** ① 月台天花板冷白日光燈｜② （diffuse）磨石子地面把光微弱地反射回來｜③ 列車進站時車頭燈從右側掃過，短暫在她臉上留下一道更亮的光｜④ 對臉測光，車頭燈那側過曝，月台深處壓黑｜⑤ 無
  - 不完美變數：構圖 off_center／動態 subject_motion／白平衡 slightly_cool_auto／背景 heavy／高光 allowed／identity_safe True
- **20 `a08`** ① 薄雲天的散射光，沒有硬陰影｜② （diffuse）淺色步道地面把光均勻補回她的側臉輪廓｜③ **無**（刻意留白）｜④ 對側臉測光，天空略過曝，下顎到頸的輪廓線完整可讀｜⑤ 無
  - 不完美變數：構圖 off_center／動態 none／白平衡 neutral／背景 moderate／高光 allowed／identity_safe True

### 5-6 現行分布（程式計算）

- **光線家族**：`L6_soft_overcast`×7（35%）、`L2_single_window_daylight`×6（30%）、`L3_mixed_warm_cool_practical`×3（15%）、`L1_single_ugly_overhead`×3（15%）、`L8_bathroom_fluorescent`×1（5%）
- **景別**：`chest_up`×7、`full_body`×4、`waist_up`×4、`knee_up`×3、`face_closeup`×2
- **頭部角度**：`front`×5、`right_30`×5、`left_30`×4、`left_60`×2、`right_60`×2、`profile_left`×1、`profile_right`×1
- **身體姿態**：`standing`×8、`seated`×7、`crouching`×2、`leaning`×2、`walking_frozen`×1
- **視角**：`third_person`×18、`selfie_front`×1、`selfie_mirror`×1
- **濾鏡**：`none`×18、`ccd`×2
- **地點層級**：`B`×15、`C`×5
- **地點**：`park`×4、`city_street`×3、`workplace_own_studio`×3、`local_cafe`×2、`breakfast_shop`×1、`own_bedroom`×1、`own_entryway`×1、`own_bathroom`×1、`convenience_store`×1、`laundromat`×1、`pharmacy`×1、`train_platform`×1
- **穿搭**：`nico_outfit_01`×5（25%）、`nico_outfit_03`×5（25%）、`nico_outfit_08`×3（15%）、`nico_outfit_06`×2（10%）、`nico_outfit_05`×2（10%）、`nico_outfit_04`×1（5%）、`nico_outfit_09`×1（5%）、`nico_outfit_02`×1（5%）
- **髮型**：`nico_hair_01`×5、`nico_hair_02`×5、`nico_hair_04`×5、`nico_hair_05`×3、`nico_hair_06`×1、`nico_hair_03`×1
- **表情種類**：15 種
- **乾淨臉部特寫 / 乾淨 body-readable 全身 / 乾淨右側**：2 / 3 / 2
- **home+work**：全體 6/20（30%）、lifestyle 子集 6/12（50%）、**anchor 落在住處或職業空間 0/8**
- **career_related**：3/20（上限 40%）｜**signature_family**：3/20（上限 25%）

### 5-7 Phase D — 壓力測試

Soul 訓練完成後，測 identity 在訓練集沒教過的條件下是否還守得住。這是本 repo 從來沒做過的一步——過去只評估訓練圖本身的一致性，沒有測訓練後的漂移。

**固定基準**：{'outfit_id': 'nico_outfit_01', 'hair_id': 'nico_hair_01', 'location': 'own_living_room', 'light_family': 'L2_single_window_daylight', 'filter': 'none', '_note': '除了各 shot 標示的 test_variable 之外，全部沿用這組基準。'}

**seed 政策**：st00–st05 與 st10 各跑 3 次 replicate（平台若支援固定 seed 則固定，否則以重複樣本取代）。單張輸出無法區分 soul 品質與抽樣波動——這是 C-08 第 4 點的要求。

| id | 測什麼（唯一變數）| 期望不變的是 | 適用 rubric | 固定 framing/yaw | replicates | 依賴 |
|----|------------------|-------------|------------|-----------------|-----------|------|
| `st00` | （無，基準線） | 這張定義該 soul 的『正常長相』，其餘所有 shot 與它比對 | face_identity、body_identity、apparent_age、skin_tone | chest_up/front | 3 | — |
| `st01` | head_yaw = front + face_closeup | 五官比例與 identity marker 應與 st00 一致 | face_identity、apparent_age | face_closeup/front | 3 | — |
| `st02` | head_yaw = left_30 | 左側輪廓下的臉仍是同一人 | face_identity | chest_up/left_30 | 3 | — |
| `st03` | head_yaw = right_30 | 右側可見的 identity marker（右鼻翼小痣）應出現 | face_identity | chest_up/right_30 | 3 | — |
| `st04` | framing = full_body | 身材比例符合 body_visual，未被放大成豐滿 | body_identity | full_body/front | 3 | — |
| `st05` | body_pose = seated | 坐姿下軀幹與腿身比例仍穩定 | body_identity | waist_up/front | 3 | — |
| `st06` | location = 戶外散射光 | 換到戶外自然光後臉與膚色不漂 | skin_tone、environment_independence、no_scene_burn_in | knee_up/front | 1 | — |
| `st07` | light_family = 夜間招牌混光 | 強色偏下膚色與臉仍穩定 | skin_tone、environment_independence | waist_up/front | 1 | — |
| `st08` | light_family = C 級冷白頂光 | 最容易讓臉崩的條件下仍是同一人 | face_identity、skin_tone、environment_independence | waist_up/front | 1 | — |
| `st08b` | camera = 手機由下往上的極端打光 | 骨相不被打光扭曲成另一個人 | face_identity、apparent_age | face_closeup/front | 1 | — |
| `st09a` | hair_id = nico_hair_06（濕髮，中度變化） | 換髮型後仍是同一人 | hair_independence、face_identity | chest_up/front | 1 | — |
| `st09b` | hair_id = 長髮接髮（極端變化） | 極端髮長變化下 identity 是否仍守住 | hair_independence | chest_up/front | 1 | 只有 st09a 通過才執行。一次跳到極端，失敗時分不清是 hair independence 不足還是變量太大。 |
| `st10` | outfit_id = nico_outfit_07（派對長洋裝） | 換裝後臉與身材不漂，且不帶出訓練服裝 | outfit_independence、no_outfit_burn_in、body_identity | full_body/front | 3 | — |

**已知風險**：家 5 張 + 工作室 3 張 = 8/19（42%）。**7 張 clean identity anchor 全部不在家或工作室**，所以最強的身分訊號沒有跟這兩個空間綁在一起。若 st06–st08 仍出現固定背景烙印，代表 lifestyle 那 12 張的世界集中度仍需再降。

### 5-8 Soul QA Rubric

每項 0–2 分。0=明顯失敗，1=輕微漂移，2=穩定。　9 個項目：face_identity、body_identity、apparent_age、skin_tone、hair_independence、outfit_independence、environment_independence、no_scene_burn_in、no_outfit_burn_in

**Hard gates（總分無法掩蓋的關鍵失敗）**：
- face_identity 在任一 identity_core 測項（st00–st05）為 0 → 整批 fail
- body_identity 在 st04（全身）或 st05（坐姿）為 0 → 整批 fail
- 出現明顯固定背景烙印（換場景仍冒出工作室或她的房間）→ 直接 fail
- 換裝後仍固定帶出 training garment → 直接 fail

**總分門檻**：**待 Retroactive Benchmark 跑完後訂**（GOOD=Iris Chen，KNOWN_BAD=Rainie v1）

**訂定方法：Retroactive Benchmark**
- **_why**：上一版寫 14/18 是我憑空訂的。而且 9 項每項至少 1 分時，4 項給 1 分 + 5 項給 2 分 = 14 剛好 PASS——四個維度都有可見漂移仍會通過，門檻太鬆。
- **ground_truth**：`body_identity` 評的是「與該 persona 的**核准身材目標／核准 reference**是否相符」，**不是**「同一個 soul 自己是否前後自洽」。這一條專門針對 KNOWN_BAD：Rainie v1 若拿自己的錯誤 anchor 當真理，它的 body consistency 會很高——但它的失敗正是身材不符 94-59-92/F 罩杯設定，所以必須對目標評分。
- **persona_adaptation**：Phase D 的 13 個 shot 目前寫的是 Nico 的 outfit / marker / 身材敘述，**不可原字套到 Iris 或 Rainie**。跑 benchmark 時**固定的是測試難度與變量類型**（yaw / framing / pose / 光線 / 髮型 / 換裝），各 persona 換成自己的 approved outfit、自己的 identity marker、自己的 body target。
- **scoring_aggregation**：每個 rubric item 逐 shot 評分（只評該 shot 的 applicable_rubric_items），同一 item 取所有適用 shot 的**最低分**作為該 item 的最終分（最低分制，避免平均掩蓋單點失敗），9 個 item 加總得 0–18。hard gate 則是 per-shot 判定，任一 shot 觸發即整批 fail，不進加總。
- **replicates**：st00–st05、st10 各 3 次。同一 shot 的 replicate 之間若判定不一致，該 item 取最低分。
- **cost**：2 個 soul × 13 張 = 26 張。比訓練完才發現門檻訂錯便宜太多。

**baseline**（由使用者裁決）：
- **GOOD** Iris Chen（`5fe3b6ba`，ready）：使用者指定。她是本 repo 第一個完成的人格，KOL_TRAINING_SOP.md 明寫「Iris Chen 是所有 KOL 的標準範本」，且訓練後在生產環境跨場景跨造型使用最久（競品對標批次、舞蹈克隆、溫泉短片、內衣鏡前自拍短片）。
- **KNOWN_BAD** Rainie Hsu（v1 已棄用）（`994e33d2`，deprecated）：使用者指定。這個 soul 的錨點圖只核對了臉部與妝容、沒有核對身材，實際身型偏纖細平板、與 94-59-92 / F 罩杯設定不符，整批 13 張訓練圖與此 soul_id 因此作廢重做（v2 為 a4a000fe）。它是本 repo 唯一有明確失敗原因記錄的 soul，適合當下限對照。
  - 預期訊號：body_identity 這一項應該明顯低分。若 rubric 跑出來 body_identity 仍拿高分，代表 rubric 本身測不出這個已知缺陷，rubric 要先修。

---

## §6 驗證器做了什麼

`tools/validate_shoot_plan_v2.py`，只用標準函式庫。目前的檢查：

- **schema 執行**：從頂層驗，`phase_c_shots` 透過 `$ref` 綁到 shot 定義；required／enum／minItems／未定義欄位／shot_id 唯一性
- **語意衝突**：scene 不得出現服裝／髮型／濾鏡詞（單一真理來源）、影片語言、一列多時空、**scene 描述的姿態與 `body_pose` 不符**
- **光線**：五段完整性、`specular` 誤當柔和填光、lighting family ≥4 種、L1 醜頂光上限
- **身分覆蓋**：yaw／framing／pose／expression／face_visibility 覆蓋率、髮型變體全覆蓋、乾淨錨點下限（臉部特寫／body-readable 全身／右側高資訊角度）
- **世界集中度**：home+work 全體與 lifestyle 子集雙層上限、`location+outfit+hair` 三重固定組合重複（anchor 之間豁免，那是控制組）
- **標籤**：`signature_family`／`career_related` 由 registry 推導，兩欄各自獨立 override 且需理由，quota 以 effective value 計算
- **Phase gate**：A 四候選必須固定 10 個欄位且唯一變數是 identity；B2 必須真的換場景/穿搭/髮型/光線；D 的 fixed／rubric item 存在性／depends_on 指向／rubric 全覆蓋
- **反漂移**：禁止內嵌人工宣告的衍生統計，並反算 `structure`／`shots` 的宣告值
- **訓練安全**：`identity_safe`／`face_motion_blur`／`face_detail_preserved`；`full_body` 禁 shallow DOF；CCD 禁用於 `full_body`
- **語意覆核 gate**：機器 lint 通過後仍需逐列人／LLM 覆核，紀錄用 hash 綁資料，改資料自動失效

**對抗測試結果**：注入 7 個違規（拿掉 Phase A 必固定欄位、B2 場景設同 B1、rubric 引用不存在項目、塞回人工統計、structure 宣告 99+1、無理由的雙欄 override），**7/7 全數抓到**。
另一次注入 4 個 schema 違規（非法 framing／非法 yaw／空 props／非法 DOF），**4/4 全數抓到**。

**目前輸出**：

```
驗證 nico-tsai（schema v2.1.0）
  ⚠  語意覆核未完成：0/20 列，尚未覆核 ['nico_a01', 'nico_a02', 'nico_a03', 'nico_a04', 'nico_a05']…（生成前必須完成，見 pilot/semantic_review.md）
  ✓ 全數通過
```

---

## §7 議題帳本現況

| ID | 議題 | 提出者 | 狀態 | 備註 |
|----|------|--------|------|------|
| C-07 | 覆核包統計與 JSON 漂移 | ChatGPT | 🔵 Claude已修正 | 移除人工宣告的 `dominant_training_outfit`；validator 反算 `structure`／`shots` 宣告值，並禁止內嵌衍生統計 |
| C-08 | QA 門檻 14/18 憑空訂且偏鬆 | ChatGPT | 🔵 Claude已修正 | 四項封口全補：ground_truth 對 persona 目標評分（非 soul 自洽）、persona-adapted 等價測項、最低分制聚合、st00–st05/st10 各 3 replicate |
| C-09 | validator 沒驗 Phase A / B / D | ChatGPT | 🔵 Claude已修正 | A 四候選必須固定 10 個欄位且 varies_only=identity；B2 必須真的換場景/穿搭/髮型/光線；D 驗 fixed、rubric item 存在性、depends_on 指向、rubric 全覆蓋 |
| C-13 | identity marker 的 `2mm` 不是模型能穩定執行的單位 | ChatGPT | 🔵 Claude已修正 | `2mm` 改為相對可視語句，並補 2 個不依賴左右方向的骨相 marker（眼距、鼻頭形狀） |
| C-14 | 19 位只是文件上凍結，沒有機制阻擋 | ChatGPT | 🔵 Claude已修正 | v1 資料標 `blocked_pending_v2_pilot`，v1 validator HARD FAIL exit 2；另建 `pilot/v1_known_issues_report.json` |
| C-15 | `schema_v2.json` 未被實際執行，validator 可放過非法 enum / 空 props | ChatGPT | 🔵 Claude已修正 | schema v2.1 補頂層 + `$ref` 綁 shots + shot_id 唯一性 + additionalProperties；validator 從頂層驗。對抗測試 7/7 抓到 |
| C-16 | clean anchors `nico_a01` / `nico_a02` 的 scene 與 body_pose 衝突 | ChatGPT | 🔵 Claude已修正 | a01/a02 body_pose 改 seated；新增姿態衝突檢查，且在後續改動中又抓到 c03 |
| C-17 | Phase D stress spec 仍是不可重現的自然語言選單 | ChatGPT | 🔵 Claude已修正 | Phase D 改結構化單一變量：每 shot 有 test_variable / expected_invariant / applicable_rubric_items / fixed / replicates / depends_on |
| C-18 | label override 可繞過 registry 推導並壓低 quota 計數 | ChatGPT | 🔵 Claude已修正 | signature 與 career 各自獨立 override reason；quota 一律以 effective value 計算 |
| K-01 | validator 的 scene 衝突是 keyword guard 不是語意理解 | Claude | 🔵 Claude已修正 | 新增 `tools/gen_semantic_checklist.py` 逐列覆核清單 + hash 新鮮度 gate，資料一改舊核可自動失效 |
| K-02 | `nico_outfit_01` 佔 7/19（37%），比 R2 被指出的 30.8% 更高 | Claude | 🔵 Claude已修正 | 拆掉工作室三張的四重綁定（c01→outfit_08/hair_01、c02→outfit_06/hair_04）；最高佔比降到 5/20=25%，共 8 種 |
| K-03 | 家＋工作室仍佔 42%，但 anchor 全在外面 | Claude | 🔵 Claude已修正 | c03→早餐店、c09→超商；全體 30%、lifestyle 子集 50%；validator 加雙層比例上限與三重固定組合檢查 |
| K-04 | 19 張是否應補滿 20 | Claude | 🔵 Claude已修正 | 新增第 20 張 `nico_a08`：profile_right + outfit_02（未用過）+ 公園中性外部 B |
| K-05 | 跨 persona row fingerprint 檢查未實作 | Claude | 🟡 待處理 | ChatGPT 同意延後，但列為 persona #2 的前置 gate |

狀態圖例：🔵 Claude已修正（待你確認）　🟡 待處理　⚪ 待回應　🔴 有爭議

---

## §8 本輪請你判斷

1. **上表所有 🔵 的項目**：修正是否到位、可否結案？
2. **新發現**：以 §3 的規則為判準，這一版還有什麼問題？特別是：
   - 20 張的身分覆蓋是否真的足夠訓練一個穩定的 Soul
   - 有沒有哪個場景／服裝／光線組合在現實中不成立
   - C 級場景（早餐店、超商、洗衣店、藥妝店、月台）夠不夠「不美」，還是仍被美化
   - Phase D 的 13 個 shot 是否真的可重現、變量是否單一
3. **放行判定**：可以開始生成，還是仍有 P0 必須先修？

**判斷原則**：§5 的數字都是程式算的。如果你認為某個數字不對，直接指出——
Claude 會實測驗證。前四輪你的數值主張全部正確，但也發生過你引用的官方規格
與本專案實際 API endpoint 不同（見 §2 訓練張數）。

---

## §9 你的回覆區

把意見寫在下面這行以下。Claude 會讀這一段。

<!-- ===== REPLIES BELOW — 本行以下不會被自動產生覆蓋 ===== -->
