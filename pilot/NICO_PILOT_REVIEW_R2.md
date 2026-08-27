# Nico Pilot — 第二輪覆核包（回應 ChatGPT 對抗性複核）

> 給外部審閱者：這是 Claude 對 ChatGPT 第一輪複核的回應與修正。自帶背景，不需存取 repo 其他檔案。
> 產出：2026-08-27　|　狀態：**尚未生成任何圖片**

---

## 0. 先講結論

ChatGPT 的**可驗證主張我全部實測過，全部成立**，而且有兩項比它measured 的更嚴重。
我接受它 90% 的診斷，但對最核心的「結論 1」有一項事實補充與一項方法上的不同意見（見 §4）。

我沒有做它明確警告不要做的事——沒有把 20 位 260 列全部改一遍再宣稱 PASS。
這一輪只動方法層，資料層只做 Nico 一位。其餘 19 位維持 v1 凍結，等 pilot 結果再決定要不要遷移。

---

## 1. ChatGPT 主張的實測驗證結果

| ChatGPT 的主張 | 我實測的結果 | 判定 |
|----------------|-------------|------|
| scene 與 outfit_id 衝突「大量存在」 | **12 / 260 列**確認衝突，它舉的 5 個例子全部正確 | ✅ 成立（但比例應精確為 4.6%，不是「大量」）|
| scene 與 hair_id 衝突 | **14 / 260 列**確認衝突 | ✅ 成立 |
| 15/20 位是 B=9，違反文件的 B 7–8 | 實測 **B=9 有 15 位、B=8 有 5 位**，與它說的完全一致 | ✅ 成立 |
| Cheryl 的 hair #5 沒進訓練集 | 實測全批**只有 Cheryl 一位**未用滿 5 種髮型，就是缺 #5 | ✅ 成立 |
| row fingerprint（同列位置跨 20 位雷同）| 實測**比它說的更嚴重**：Row 1 是 100% meitu ＋ 100% 自拍；Row 13 是 100% iPhone ＋ 100% 他拍 ＋ 90% A 級；Row 3 有 19/20 是同一個 outfit 編號 | ✅ 成立，且低估 |
| A 級被硬湊 | 成立。而且我可以指出**確切的程式碼原因**（見下） | ✅ 成立 |

### 這些缺陷的共同來源：是我的自動修正器造成的

第一輪我寫了一支 rebalancer 去修 validator 抓到的 130 個違規。它做了三件事：

1. **只改 outfit / hair 的數字，完全沒動 scene 文字** → 12 + 14 列的雙重真理來源衝突，全部是這樣來的。
2. **A 級補位的 fallback 是「把最後一個非職業的 B 場景升成 A」** → 所以「早上煮咖啡」「清晨四點開烤箱」變成嚮往感場景。這是字面意義上的 quota 硬湊。
3. **濾鏡與視角用位置指派**（`others[:2]` 給 CCD、`selfs[0]` 給 meitu）→ 直接製造出 row fingerprint。

所以 ChatGPT 的第二層盲點診斷是對的，但更精確的說法是：

> **不是我「太相信 validator PASS」，是我寫了一支為了讓 validator PASS 而改資料的程式，
> 而那支程式本身沒有語意概念。**

---

## 2. 我這一輪改了什麼

### 2-1 schema v2：positional array → named object

v1 一列是 `["支柱","場景","B",3,2,"props","light","他拍","iphone"]`——
看不出第 4 個數字是 outfit 還是 hair，加欄位就會 off-by-one。

v2 改為 named object，並新增：

- **身分覆蓋欄位**：`framing` / `head_yaw` / `head_pitch` / `expression` / `eye_gaze` /
  `body_pose` / `face_visibility` / `camera.distortion` / `camera.depth_of_field`
- **光線拆成 5 個具名欄位**：`light.family` / `key` / `bounce` / `bounce_type` /
  `secondary_source`（**可為 null**）/ `exposure_choice` / `occlusion`
- **`bounce_type`**：區分 diffuse（白牆/床單/淺色地板）與 specular（鏡面/玻璃/金屬/烤漆）。
  v1 把不鏽鋼、鏡面、車身都當成「把光柔和補回臉」的填光，物理上錯了。
- **`imperfection_profile`**：構圖歪斜／手震／白平衡偏移／背景雜亂／高光溢出
- **`signature_family` 與 `career_related`**：招牌世界換衣服也逃不掉

### 2-2 單一真理來源（硬性）

`scene` 只能寫「她在做什麼、在哪裡」。**禁止**出現服裝、髮型、濾鏡、身材。
validator 用正則直接擋。實測有效——我自己新寫的 pilot 資料就被它抓到一列
（scene 寫「把送洗的白襯衫抱出來」，`襯衫` 觸發服裝詞攔截），已改掉。

濕髮改為正式的髮型變體 `nico_hair_06`，不再靠 scene 描述。

### 2-3 地點層級改由 registry 決定

不再每列自由判斷。建立 `location_registry.json`，A/B/C 由表決定；
要覆寫必須填 `location_tier_override_reason`。

### 2-4 validator v2：語意 + 反作弊

新增的檢查：

- scene ↔ outfit / hair / filter 衝突（正則）
- 影片語言偵測（一鏡到底／連換／縮時）
- 一列多時空偵測（另一天／同行程）
- 光線五段是否真的五段、`bounce_type` 是否誤用 specular 當填光
- `full_body` 不可用 shallow DOF、CCD 不可用在 `full_body`
- 身分覆蓋矩陣（yaw / framing / body_pose / expression / face_visibility）
- 髮型變體是否全覆蓋
- `signature_family` ≤25%、`career_related` ≤40%
- **lighting family 至少 4 種**——防止每張都是同一種漂亮的物理光配方
- **`imperfection_profile` 不可 13 張全部相同**

### 2-5 Phase A 重做：4 個候選 identity，不是 4 個視角

**這一點 ChatGPT 是對的，而且 repo 自己的歷史就是證據。**
`rainie-hsu` 的紀錄寫著：

> candidate_01–04 是各自獨立生成的 4 個人，身材本來就不是同一套——
> 問題是當初選錨點只核對了臉部/妝容，沒有人核對過身材是否符合三圍規格。

結果是整批 13 張訓練圖與一個 soul_id 作廢重做。我第一輪還是寫成「同一人的 4 種景別」，
等於把已經害過一次的假設又寫進方法文件。

v2 的 Phase A：4 張**完全同規格**（同 framing / 同姿勢 / 同衣服 / 同髮型 / 同場景 / 同光線），
只有 identity 不同。framing 統一為 `knee_up`＋`left_30`，臉與身材同時可判。

選角服新增硬性條件：`body_readable: true`、明寫 `neckline`、
不可 oversized／寬版襯衫／睡袍／外套罩身體、`depth_of_field` 一律 `adequate`、
**不寫 `candid moment`**（Phase A 是 calibration，需要可比較可重複）。

---

## 3. 我不同意 ChatGPT 的地方（一項事實補充、一項方法分歧）

### 3-1 事實補充：不是「沒有 Soul V2 的實驗證據」

ChatGPT 結論 1 寫：

> 目前文件沒有提供 Soul V2 的實驗證據，證明「社群貼文的多樣化配額」同樣就是「Soul 最佳訓練集配額」。

**這句話一半對一半不對。** 我查了 repo：

- 目前有 **6 位角色的 Soul 已訓練完成並 status=ready**
  （iris-chen / coco-wu / mia-huang / rainie-hsu / sophia-tseng / vicky-lin）
- 這些 soul_id 已經在生產環境用了數週，跨場景、跨造型生成過大量內容：
  2026-08-05 的競品對標批次（7 位各 2 張，全新場景與全新穿搭）、多支舞蹈克隆影片、
  溫泉短片、內衣鏡前自拍短片。這些的場景與服裝**都不在訓練集裡**。
- 那批的評定是「✅ 通過」，14/14 背景路人成功、7/7 同穿搭一日敘事成功。

所以現行方法**不是零證據**，它有數週的生產環境弱陽性證據。

**但 ChatGPT 的核心指控仍然成立，而且是重要的：**
那些評定的判準是「巷弄質感、背景路人、穿搭延續、打光」——
**沒有任何一項是明確評估 identity 漂移**（臉與身材相對於錨點的穩定度）。

> 精確的說法應該是：**現行方法有『沒出事』的證據，但沒有『測過』的證據。**

這正是我這一輪新增 Phase D stress test 與 Soul QA rubric 的理由——
那是這個 repo 從來沒做過的一步。

### 3-2 方法分歧：我不採用「7 張 identity core close-up」的結構

ChatGPT 建議把 13 張改成：7 張正面/左右 3/4 close-up ＋ 3 張 pose ＋ 3 張環境。

**我採用它的意圖，但不採用它的形式。** 理由：

1. 那個結構會讓訓練集變成一組**證件照式的素材**。本專案的目標不只是
   「模型認得這張臉」，而是「模型認得這個**活在特定生活裡的人**」——
   若訓練集全是乾淨 close-up，後續生成生活場景時反而要外推。
2. 現行的六大支柱結構有 6 位角色的生產證據（見 3-1），把它整個換掉是拿
   有弱證據的方法去換完全沒有證據的方法。
3. 真正缺的不是「換結構」，是「**沒有人追蹤覆蓋率**」。

**我的做法是混合**：保留她真實生活的 13 個場景，但每一張都掛上身分覆蓋 metadata，
並讓 validator 強制覆蓋率達標。Nico 的 13 張現在同時滿足：

- head_yaw：front×4、left_30×3、right_30×3、left_60×1、right_60×1、profile_left×1
- framing：face_closeup×2、chest_up×2、waist_up×4、knee_up×3、full_body×2
- body_pose 5 種、expression 13 種、臉部無遮擋 11 張
- 而且全部發生在她真實的生活場景裡，不是棚拍 close-up

**這是一個需要被實驗判定的分歧，不是我單方面說了算。**
如果 Nico pilot 的 stress test 失敗，就回頭採用 ChatGPT 的結構。

---

## 4. 我接受並執行的 ChatGPT 建議

| 建議 | 執行狀況 |
|------|---------|
| Identity Training 與 Social Content Diversity 拆開 | ✅ Phase C 配額移除 A 級硬性要求與 B 7–8；A/B/C 只保留 C≥2 |
| Phase A 改成 4 個候選 identity | ✅ 已重做 |
| Phase A 全部改成身材可讀的標準 framing | ✅ knee_up + body_readable 硬性欄位 |
| Phase A 增加 explicit neckline | ✅ 每個 outfit 都有 `neckline` 欄位 |
| scene 移除 outfit / hair 描述 | ✅ validator 正則強制 |
| 修正 A/B/C 誤分類 | ✅ 改由 location_registry 決定 |
| 一鏡到底改 frozen moment | ✅ validator 偵測影片語言 |
| 拆掉一列多時空 | ✅ validator 偵測 |
| light 改 5 個 named fields | ✅ 並新增 `bounce_type` 區分 diffuse/specular |
| 第二色溫不強制 | ✅ `secondary_source` 可為 null；Nico 13 張有 4 張是 null |
| Lighting Family | ✅ 8 種 L1–L8，validator 要求至少 4 種 |
| 第一輪 meitu=0、降低 CCD 與前鏡頭畸變 | ✅ meitu=0、CCD 只 2 張且不用在 full_body、自拍 3 張 |
| 身材差異不能只靠三圍數字 | ✅ 新增 `body_visual` 敘述性比例，數字降為 metadata |
| 臉部增加身分 marker | ✅ Nico 有 3 個（眉尾高低差、鼻翼小痣、唇峰偏平）|
| 膚色 NOT 清單過長 | ✅ 改為正向物理描述為主，NOT 清單縮短 |
| shallow DOF 不應全套 | ✅ full_body 強制 adequate，validator 擋 |
| candid 不適合 Phase A | ✅ 移除 |
| imperfection_profile | ✅ 已加，且 validator 要求不可全部相同 |
| row fingerprint | ✅ 禁止任何欄位與列號綁定 |
| Vertical Slice 只跑 1 位 | ✅ 只做 Nico，其餘 19 位凍結 |
| Soul QA rubric | ✅ 9 項 × 0–2 分，含 hard_fail 條件 |
| Stress test 10 張 | ✅ 已規格化 |

---

## 5. Nico Pilot 完整規格

### 5-1 身分規格

- 年齡／族裔：26 / Taiwanese
- 膚色（正向）：light neutral-to-cool skin tone, natural tonal variation across face and body, subtle normal redness at cheeks, elbows and knuckles, not overexposed
- 膚色（排除）：NOT tanned, NOT bronzed, NOT olive, NOT deep golden or wheat-colored
- 臉部基底：fine elongated phoenix eyes, cool composed expression, delicate features
- **身分 marker**：
  - 左眉尾比右眉尾略高約 2mm，笑起來更明顯
  - 右側鼻翼旁一顆很淡的小痣
  - 唇峰偏平，上唇中線幾乎沒有明顯的 M 形
- 身材數字（metadata）：{'height_cm': 167, 'weight_kg': 49, 'bust_cm': 86, 'waist_cm': 59, 'hip_cm': 88, 'cup': 'C', 'leg_cm': 82}
- **身材視覺比例（prompt 用）**：narrow shoulders roughly equal to hip width, long torso, small natural bust with a shallow curve, visible collarbone and sternum, slim upper arms with no muscle definition, long straight legs, flat lower abdomen; overall silhouette is narrow and elongated
- 身材排除：NOT voluptuous, NOT heavy-chested, NOT curvy, NOT athletic-muscular
- 註：三圍數字保留在 metadata 供人核對，但 prompt 以 body_visual 的視覺比例為主——模型不會把 86-59-88 精確解讀成幾何。最終 identity 錨定仍以 reference image 為準，數字寫了不等於身材就對了。

### 5-2 造型庫

| ID | 區間 | 領型 | 上身 | 下身 | 鞋 | 包/外套 | 首飾 | 身材可讀 |
|----|------|------|------|------|----|---------|------|---------|
| `nico_outfit_01` | ★極簡職人 | high mock neck | 炭灰色合身羅紋針織長袖，高領貼頸 | 黑色高腰直筒西裝褲 | 黑色皮革樂福鞋 | 米色帆布托特 | 銀色細戒指＋銀色小圈耳環 | ✅ |
| `nico_outfit_02` | 極休閒 | straight neckline spaghetti strap | 米白色棉質細肩帶背心，一字平口 | 灰色棉質及膝短褲 | 赤腳 | 薄針織開襟外套（脫下搭在椅背） | 銀色細項鍊 | ✅ |
| `nico_outfit_03` | 日常有型 | crew neck | 奶油色短版針織上衣，圓領 | 高腰淺色直筒牛仔褲 | 白色球鞋 | 深棕小方包 | 銀色圈形耳環 | ✅ |
| `nico_outfit_04` | 學院感 | collared button-down, top two buttons open | 白色寬版襯衫 | 黑色百褶短裙 | 黑色瑪莉珍鞋 | 灰色及膝襪 | 銀色髮夾 | ❌ |
| `nico_outfit_05` | 街頭 | crew neck, cropped hem | 黑色短版帽T | 灰色工裝寬褲 | 厚底球鞋 | 黑色斜背小包 | 銀色耳骨夾 | ❌ |
| `nico_outfit_06` | 上班正式 | square neckline camisole under blazer | 燕麥色西裝外套＋白色絲質方領背心 | 同色系直筒寬褲 | 尖頭平底鞋 | 結構皮革包 | 銀色細手鐲 | ❌ |
| `nico_outfit_07` | 派對夜間 | straight neckline, open back | 黑色細肩帶絲質長洋裝（露背） | （連身） | 銀色細跟涼鞋 | 金屬扣手拿包 | 銀色手環 | ✅ |
| `nico_outfit_08` | 居家貼身 | modest scoop neck | 灰色貼身棉質長袖上衣 | 黑色棉質貼身長褲 | 室內拖鞋 | 無 | 無 | ✅ |
| `nico_outfit_09` | 雨天機能 | high round neck | 深灰防潑水連帽外套＋內搭黑色高領 | 黑色直筒長褲 | 黑色短雨靴 | 防水肩背包 | 無 | ❌ |

**髮型變體**

- `nico_hair_01`：短鮑伯自然放下，一側塞耳後，髮尾內彎
- `nico_hair_02`：短鮑伯全部塞到雙耳後，露出雙耳與後頸
- `nico_hair_03`：鯊魚夾把後半部夾起，前側留兩撮碎髮（工作時）
- `nico_hair_04`：中分吹整、髮尾微內扣，比平時整齊
- `nico_hair_05`：髮尾用電棒外翹，右側夾一支銀色細髮夾
- `nico_hair_06`：剛洗完澡的濕髮，自然往後貼，髮尾滴水

### 5-3 Phase A — 4 個候選 identity

**概念**：4 個候選 identity，不是同一人的 4 個視角

> 本 repo 自己的紀錄已證實：rainie-hsu 的 candidate_01–04 是各自獨立生成的 4 個人，身材差異大到後來必須換錨點重做 13 張。因此不可假設 4 次無錨定呼叫是同一個人。4 張改為同規格的 4 個候選人，使用者挑出『臉＋身材一起成立』的那一個。

**4 張完全相同的部分**：
- framing `knee_up`／head_yaw `left_30`／body_pose `standing`／view `third_person`
- outfit `nico_outfit_01`／hair `nico_hair_01`／location `workplace_own_studio`
- camera：{'type': 'phone_rear', 'distortion': 'none', 'depth_of_field': 'adequate'}
- light：family `L2_single_window_daylight`
  - key：午後日光從她左前方 45 度、略高於視線高度的落地窗進來
  - bounce（diffuse）：她右側的白牆與白色美甲桌面把光柔和地補回臉的暗面
  - secondary_source：None
  - exposure_choice：相機對她臉測光，窗外整片過曝成白，工作室深處落入柔和陰影
- **唯一變數**：identity（每次獨立生成，得到 4 個不同的人）

**Phase A 選角服硬性規則**：
- 必須 body_readable=true：軀幹、腰線、肩寬、臀線都要看得出來
- 必須明寫 neckline（此處為 high mock neck）
- 不可用 oversized、寬版襯衫、寬鬆針織、睡袍、浴衣、外套罩住身體
- 必須是日常款，不是招牌極端造型
- 不寫 candid moment——Phase A 是 calibration，需要可比較、可重複的 neutral natural pose
- depth_of_field 一律 adequate，不可 shallow（否則身體輪廓變糊）

**prompt 段落順序**：SHOT/FRAMING 放第一行 → IDENTITY → BODY → HAIR → OUTFIT(含 neckline) → PLACE → LIGHT → CAMERA → REALISM

### 5-4 Phase B

1. 使用者從 4 個候選挑 1 個（同時看臉與身材）
1. media_upload → curl PUT → media_confirm → show_reference_elements(action='create')
1. 用新 element 生成 2 張驗證圖：①正面 face_closeup ②right_30 full_body
1. Read 逐張確認：臉是否同一人、身材是否符合 body_visual、膚色是否維持
1. 驗證不過就換候選人重來（成本 2 張，不是 13 張）

### 5-5 Phase C — 13 張訓練集

> **配額變更說明**：移除 A 級硬配額與 B 級 7–8 的規定（見 review packet §4）。identity training 的第一優先是身分覆蓋，不是社群內容的地點嚮往感配比。

| # | 目的 | 場景 | 地點 | 層級 | outfit | hair | framing | yaw | pitch | 表情 | 姿態 | 視角 | 臉部遮擋 | 濾鏡 | 招牌世界 | 職業 |
|---|------|------|------|------|--------|------|---------|-----|-------|------|------|------|---------|------|---------|------|
| 01 | identity_core | 鐵門拉下後，坐在工作椅上轉過來看窗外，手還搭在椅背 | `workplace_own_studio` | B | `01` | `03` | face_closeup | front | neutral | neutral_composed | seated | third_person | unobstructed | none | nail_studio | — |
| 02 | identity_core | 蹲在地上拆剛到的材料紙箱，抬頭看向門口 | `workplace_own_studio` | B | `01` | `03` | chest_up | left_30 | up_10 | mildly_surprised | crouching | third_person | unobstructed | none | nail_studio | 是 |
| 03 | identity_core | 站在流理台前等水滾，一手撐著檯面 | `own_kitchen` | B | `08` | `01` | waist_up | right_30 | down_15 | tired_soft | standing | third_person | unobstructed | none | — | — |
| 04 | identity_core | 床邊坐著，剛醒還沒站起來，低頭看手機 | `own_bedroom` | B | `08` | `06` | waist_up | front | down_15 | just_woken_blank | seated | selfie_front | partial_hair | none | — | — |
| 05 | body_pose_coverage | 玄關穿鞋，一手扶著牆 | `own_entryway` | B | `03` | `01` | knee_up | left_60 | down_15 | focused | leaning | third_person | unobstructed | none | — | — |
| 06 | body_pose_coverage | 大安區巷子裡走路，剛越過一台停在牆邊的機車 | `city_street` | B | `03` | `01` | full_body | right_60 | neutral | neutral_walking | walking_frozen | third_person | unobstructed | none | — | — |
| 07 | identity_core | 低頭替客人上膠，側臉朝向鏡頭 | `workplace_own_studio` | B | `01` | `03` | chest_up | profile_left | down_15 | focused | seated | third_person | unobstructed | none | nail_studio | 是 |
| 08 | body_pose_coverage | 浴室鏡前修眉，另一手撐著洗手台 | `own_bathroom` | B | `08` | `02` | waist_up | left_30 | up_10 | concentrating_slight_frown | leaning | selfie_mirror | partial_hand | none | — | — |
| 09 | body_pose_coverage | 蹲在床邊伸手到床底下找充電線，回頭 | `own_bedroom` | B | `08` | `02` | knee_up | left_30 | up_10 | mildly_annoyed | crouching | third_person | unobstructed | none | — | — |
| 10 | environment_stress | 自助洗衣店裡把烘好的衣物從滾筒抱出來，站在機台前 | `laundromat` | C | `09` | `04` | full_body | right_30 | neutral | neutral_composed | standing | third_person | unobstructed | none | — | — |
| 11 | environment_stress | 藥妝店貨架前拿護手霜比較成分 | `pharmacy` | C | `05` | `05` | knee_up | front | down_15 | reading_focused | standing | third_person | unobstructed | ccd | — | — |
| 12 | environment_stress | 捷運月台等車，看著對面的到站顯示 | `train_platform` | C | `06` | `04` | waist_up | right_30 | up_10 | blank_waiting | standing | third_person | unobstructed | ccd | — | — |
| 13 | identity_core | 深夜坐在床上，燈都關了只剩手機的光 | `own_bedroom` | B | `07` | `05` | face_closeup | front | up_10 | quiet_self_aware | seated | selfie_front | unobstructed | none | — | — |

**每張的光線五段**

- **01** `L2_single_window_daylight`
  - ① KEY：午後日光從她左前方落地窗、略高於視線
  - ② BOUNCE（diffuse）：白色美甲桌面與白牆把光補回臉的暗面
  - ③ 第二色溫：**無**（刻意留白，不是每張都要有暖冷分裂）
  - ④ 曝光取捨：對臉測光，窗外過曝成白，室內深處落入陰影
  - ⑤ 遮擋：無
  - 不完美變數：構圖 off_center／動態 none／白平衡 neutral／背景 moderate／高光 allowed
- **02** `L2_single_window_daylight`
  - ① KEY：落地窗日光從她右後方進來
  - ② BOUNCE（diffuse）：地上散落的白色包裝紙把光反射回她下顎
  - ③ 第二色溫：**無**（刻意留白，不是每張都要有暖冷分裂）
  - ④ 曝光取捨：對臉測光，窗邊過曝，紙箱陰影壓黑
  - ⑤ 遮擋：無
  - 不完美變數：構圖 slightly_tilted／動態 minor_hand_blur／白平衡 slightly_cool_auto／背景 heavy／高光 none
- **03** `L1_single_ugly_overhead`
  - ① KEY：廚房天花板一盞冷白 LED 直打在她頭頂
  - ② BOUNCE（diffuse）：淺色流理台面把一點光反射回下巴，但補得不多
  - ③ 第二色溫：**無**（刻意留白，不是每張都要有暖冷分裂）
  - ④ 曝光取捨：對臉測光，眼窩與鎖骨下方留下明顯陰影，這張刻意不好看
  - ⑤ 遮擋：無
  - 不完美變數：構圖 centered／動態 none／白平衡 slightly_cool_auto／背景 moderate／高光 none
- **04** `L2_single_window_daylight`
  - ① KEY：窗簾沒拉緊，一道晨光斜落在床上
  - ② BOUNCE（diffuse）：白色床單是大面反射，把光補回她臉的下半
  - ③ 第二色溫：**無**（刻意留白，不是每張都要有暖冷分裂）
  - ④ 曝光取捨：對臉測光，窗簾縫那道光過曝成白帶，房間其餘壓黑
  - ⑤ 遮擋：無
  - 不完美變數：構圖 off_center／動態 none／白平衡 slightly_warm_auto／背景 moderate／高光 allowed
- **05** `L3_mixed_warm_cool_practical`
  - ① KEY：玄關一盞暖黃嵌燈從正上方
  - ② BOUNCE（diffuse）：白色玄關牆把暖光反射回她側臉
  - ③ 第二色溫：門外樓梯間的冷白日光燈從門縫進來，落在她肩線
  - ④ 曝光取捨：對臉測光，門縫那條冷光過曝，鞋櫃下方壓黑
  - ⑤ 遮擋：門框切掉畫面左緣
  - 不完美變數：構圖 slightly_tilted／動態 none／白平衡 neutral／背景 clean／高光 allowed
- **06** `L6_soft_overcast`
  - ① KEY：陰天的天空散射光，沒有明確方向
  - ② BOUNCE（diffuse）：淺色磁磚牆面把光平均補回她全身
  - ③ 第二色溫：**無**（刻意留白，不是每張都要有暖冷分裂）
  - ④ 曝光取捨：整體低反差，天空過曝成白，這張沒有第二色溫
  - ⑤ 遮擋：無
  - 不完美變數：構圖 off_center／動態 subject_motion／白平衡 slightly_cool_auto／背景 heavy／高光 allowed
- **07** `L3_mixed_warm_cool_practical`
  - ① KEY：可調角度的工作燈近距離直打在手部與桌面
  - ② BOUNCE（diffuse）：白色桌面把光反射回她的下顎與頸
  - ③ 第二色溫：室內天花板的冷白日光燈落在她後腦與肩
  - ④ 曝光取捨：對手部測光，所以她的臉略暗，背景布簾壓黑
  - ⑤ 遮擋：無
  - 不完美變數：構圖 centered／動態 none／白平衡 neutral／背景 clean／高光 allowed
- **08** `L8_bathroom_fluorescent`
  - ① KEY：浴室鏡上方一整條冷白燈管直打
  - ② BOUNCE（diffuse）：白色磁磚牆把光四面反射，幾乎沒有陰影
  - ③ 第二色溫：**無**（刻意留白，不是每張都要有暖冷分裂）
  - ④ 曝光取捨：對臉測光，燈管本身過曝成白條，這張的光很平、不好看
  - ⑤ 遮擋：無
  - 不完美變數：構圖 slightly_tilted／動態 none／白平衡 slightly_cool_auto／背景 moderate／高光 allowed
- **09** `L1_single_ugly_overhead`
  - ① KEY：房間天花板一盞冷白吸頂燈
  - ② BOUNCE（diffuse）：木地板反射回一點暖色，但很弱
  - ③ 第二色溫：**無**（刻意留白，不是每張都要有暖冷分裂）
  - ④ 曝光取捨：對臉測光，床底下全黑
  - ⑤ 遮擋：無
  - 不完美變數：構圖 off_center／動態 minor_hand_blur／白平衡 neutral／背景 heavy／高光 none
- **10** `L1_single_ugly_overhead`
  - ① KEY：洗衣店天花板一整排冷白日光燈管
  - ② BOUNCE（specular）：不鏽鋼機身把光以高光的形式打回來，不是柔和填光
  - ③ 第二色溫：**無**（刻意留白，不是每張都要有暖冷分裂）
  - ④ 曝光取捨：對臉測光，燈管與不鏽鋼高光整片過曝，牆角壓黑
  - ⑤ 遮擋：無
  - 不完美變數：構圖 centered／動態 none／白平衡 slightly_cool_auto／背景 heavy／高光 heavy
- **11** `L1_single_ugly_overhead`
  - ① KEY：藥妝店冷白日光燈頂光
  - ② BOUNCE（diffuse）：貨架上的白色包裝把光反射回她胸口與下巴
  - ③ 第二色溫：**無**（刻意留白，不是每張都要有暖冷分裂）
  - ④ 曝光取捨：對臉測光，燈管過曝，貨架深處壓黑
  - ⑤ 遮擋：無
  - 不完美變數：構圖 off_center／動態 none／白平衡 color_cast_from_environment／背景 heavy／高光 allowed
- **12** `L1_single_ugly_overhead`
  - ① KEY：月台天花板冷白日光燈
  - ② BOUNCE（diffuse）：磨石子地面把光微弱地反射回來
  - ③ 第二色溫：列車進站時車頭燈從右側掃過，短暫在她臉上留下一道更亮的光
  - ④ 曝光取捨：對臉測光，車頭燈那側過曝，月台深處壓黑
  - ⑤ 遮擋：無
  - 不完美變數：構圖 off_center／動態 subject_motion／白平衡 slightly_cool_auto／背景 heavy／高光 allowed
- **13** `L4_night_signage`
  - ① KEY：手機螢幕本身是唯一主光，從她臉的正下方往上打
  - ② BOUNCE（diffuse）：白色床單把一點光反射回下顎
  - ③ 第二色溫：窗外街燈的橘光落在她的左肩與髮尾
  - ④ 曝光取捨：對臉測光，手機螢幕邊緣過曝，房間全黑
  - ⑤ 遮擋：無
  - 不完美變數：構圖 off_center／動態 none／白平衡 slightly_cool_auto／背景 clean／高光 allowed

### 5-6 Phase D — Stress Test 10 張

> Soul 訓練完成後，測 identity 在訓練集沒教過的條件下是否還守得住。這是本 repo 從來沒做過的一步——過去只評估訓練圖本身的一致性，沒有測訓練後的漂移。

| ID | 測什麼 | 規格 |
|----|--------|------|
| st01 | 基準 | 正面 face_closeup，室內窗光，nico_outfit_01，nico_hair_01 |
| st02 | 左 3/4 | left_30 chest_up，同上 |
| st03 | 右 3/4 | right_30 chest_up，同上 |
| st04 | 全身比例 | full_body 站姿，adequate DOF——驗身材沒有被放大成豐滿 |
| st05 | 坐姿 | seated waist_up，驗坐下時軀幹比例是否穩定 |
| st06 | 戶外散射光 | 陰天街上 knee_up——訓練集沒有強戶外光 |
| st07 | 夜間混光 | 夜間街邊招牌光 waist_up——測色偏下的膚色穩定度 |
| st08 | C 級醜光線 | 超商冷白日光燈頂光 waist_up——最容易讓臉崩的條件 |
| st09 | 換髮型 | 完全不同髮型（長髮接髮或高馬尾），驗 identity 是否綁在短鮑伯上 |
| st10 | 換穿搭 | nico_outfit_07 派對長洋裝，驗 identity 是否綁在極簡職人造型上 |

**已知風險**：訓練集 13 張有 4 張在她自己的工作室、4 張在她房間。若 st01–st10 出現『把工作室或房間烙進人物』（換場景時背景仍冒出美甲桌或她的床），代表訓練集的場景集中度過高，需回頭調整。

### 5-7 Soul QA Rubric

每項 0–2 分。0=明顯失敗，1=輕微漂移，2=穩定。

- face_identity 臉部同一性
- body_identity 身材比例同一性
- apparent_age 年齡感
- skin_tone 膚色（不因場景色溫崩掉）
- hair_independence 換髮型後仍是同一人
- outfit_independence 換穿搭後仍是同一人
- environment_independence 換場景後仍是同一人
- no_scene_burn_in 沒有把訓練場景烙進人物
- no_outfit_burn_in 沒有把訓練服裝烙進人物

**通過門檻**：總分 ≥ 14 / 18，每項 ≥ 1

**硬性失敗**：face_identity 或 body_identity 任一為 0，整批不通過，直接回頭改訓練集

> 門檻先訂在這裡，但這是第一次做，數字本身也是待驗證的假設。第一位跑完後應回頭檢討門檻是否合理。

---

## 6. 給第二輪審閱者：請幫我檢查什麼

1. **§3-2 的方法分歧我判斷得對嗎？** 保留生活場景 + 掛身分覆蓋 metadata，
   vs. 改成 7 張 identity core close-up。我用「有 6 位生產證據」當理由，這個理由夠強嗎？
2. **Nico 的 13 張身分覆蓋真的夠嗎？** 有沒有哪個角度、姿態、遮擋情境是訓練 Soul 必要但我漏掉的？
3. **13 張裡有 4 張在工作室、4 張在她房間**，這個場景集中度會不會造成場景烙印？
   我在 stress test 的 known_risk 標記了，但沒有降低集中度——這樣處理夠嗎？
4. **lighting family 我用了 5 種**（L1 醜頂光×3、L2 窗光×2、L3 混光×2、L4 夜間×1、L6 陰天×1、L8 浴室×1）。
   ChatGPT 上一輪指出「每張都寫成漂亮物理光」是問題，我刻意讓 3 張是難看的冷白頂光。
   這個比例合理嗎？還是應該更多？
5. **Soul QA rubric 的門檻（總分 14/18）是我憑空訂的**，沒有基準。有沒有更合理的訂法？
6. **`imperfection_profile` 這一層是新加的**，但目前只寫在 metadata，還沒決定怎麼轉成 prompt 語言。
   有沒有已知的寫法會讓模型真的產生「手機隨手拍」而不是「刻意做舊」？
7. **其餘 19 位目前凍結在 v1**，那份資料有 12+14 列的語意衝突與 row fingerprint。
   等 pilot 通過後再遷移，還是應該現在就先把明顯錯誤修掉？
