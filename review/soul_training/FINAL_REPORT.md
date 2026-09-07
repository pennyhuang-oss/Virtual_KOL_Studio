# Soul V2 訓練最終報告：19/19 完成（2026-09-07）

## 一、結果

**19 位全部 `status: ready`。零失敗、零重複扣款、零「扣款但失敗」。**

帳號上唯一 `failed` 的角色是 `sofia-hsu-v4`，本 session 之前就存在，不屬於本批。

| 人設 | soul_id | 訓練張數 |
|---|---|---|
| cheryl-soh | `6d4c90b5-bd40-4c2c-9c1d-c689702863e1` | 5 |
| zhiyi-shen | `8b1e0a44-1c7b-4b65-b878-be428d00e4b8` | 5 |
| angel-chiu | `6e638286-be57-45fa-961e-51bde6cba87f` | 5 |
| angeline-kwee | `a1802330-65a7-43d7-89d3-84aacca67bfa` | 5 |
| emma-kao | `4374a074-fb89-45be-b80f-30cd78fea451` | 5 |
| jia-seo | `ecf19246-c697-419c-b978-fe9373586c19` | 5 |
| kanon-komori | `642ba554-6f87-4be9-9aa7-4b66529b4995` | **6** |
| miu-shiraishi | `270c31fa-afd4-4609-b9d5-7302745f137c` | 5 |
| nanami-fujiwara | `78761266-69ba-47fa-8aeb-39f0aa95998e` | 5 |
| peggy-lee | `3e3f4f72-2a89-4f05-af61-0c6701c97a5c` | 5 |
| rin-ayase | `34b7fd71-c8dd-4d6a-983e-881b1d012219` | 5 |
| ruoruo-tang | `4dc2bf79-0098-4c2a-b529-2b2b74117c81` | 5 |
| somi-oh | `c7915888-e566-4c9d-bc26-4bf40ab35c4c` | 5 |
| sydney-leong | `a41d8aab-fe2e-44c0-9d6a-c068565ac800` | 5 |
| tammy-chou | `5069a35a-dd85-4161-8d0f-952bccbe676d` | 5 |
| wanyin-jiang | `2e7de3f8-63ee-4302-a684-2245f6c54ea1` | 5 |
| wendy-yeo | `cb91c63f-0fa2-4c8f-94b2-a70a00acdbaf` | 5 |
| yerin-han | `8c447a79-769f-4520-a538-cfb48fef6163` | 5 |
| zoey-yeh | `feb5f196-a60e-4ef9-9f8e-5daabbdacb52` | 5 |

機器可讀版本：`SOUL_IDS.json`

## 二、成本

| 項目 | credits |
|---|---|
| 訓練集生成（96 張圖，19 位） | 118 |
| Soul 訓練（19 × 25） | 475 |
| 試點驗證圖（12 張 × 0.12） | 1.44 |
| **合計** | **≈ 594** |

`SOUL_TRAINING_PLAN.md` 的 v2 估算是「光訓練集就約 1,100」。實際訓練集 118。

## 三、狀態欄位的意思

- `trained_face_validated`（2 位）：cheryl-soh、zhiyi-shen。已跑 6 張驗證，臉 6/6 通過。
- `ready_unvalidated`（17 位）：訓練成功，**尚未跑 6 張驗證圖**。
- **沒有任何一位標成 `approved`。** 升級條件見 `ACCEPTANCE_LOCKED.md` §六 第 10 步。

17 位若要補驗證：17 × 6 × 0.12 ≈ **12.2 credits**。使用者尚未決定跑幾位。

## 四、本批確立的事實

### 1. 5 張訓練集足夠訓出穩定的臉

此帳號先前每一個成功的 soul 都用 12–13 張（Vicky Lin 12、Coco Wu 12、
Rainie Hsu 13、Sophia Tseng 13、Mia Huang 13），**5 張從未被驗證過**。

cheryl-soh 的 6 張驗證圖**完全不掛 Reference Element、prompt 裡零五官描述、
零三圍數字**，臉在正面／左前四分之三／大笑／暖色弱光素顏束髮四種條件下
與 `identity_master.jpg` 一致，年齡感 6 張都落在 24–27。

### 2. 對帳判準經實戰驗證

`Soul ID -25` = 訓練真的受理；重複 `Higgsfield Soul V2 -0.12` = 扣款但失敗
（Vicky Lin 模式）。**`balance` 全程未使用**。

這在本批是必要的，不是形式：帳號全程被另一位使用者並行使用，本 session
觀察到非本專案的 `Seed Audio 1.0`、`Seedream 4.5`、`GPT Image 2.0` 等扣款。
若用餘額對帳，19 次送訓的帳一次都對不起來。

### 3. 兩次 train 呼叫失敗，都因協定而零損失

sydney-leong 與 zoey-yeh 各遇一次 `Something went wrong`。兩次都是
**沒扣款、沒建角色記錄**的乾淨失敗，不是 Vicky Lin 模式。

兩次都照 `ACCEPTANCE_LOCKED.md` §六 第 6 步處理：先查 `transactions` 與
`action='list'`，確認無扣款無記錄，**等滿 15 分鐘**，再發唯一一次重送。
**兩次都只被扣一次款。** 若當時盲目重試，兩人各有可能多付 25。

**假設（未證實，n=2）**：兩次失敗都是連續三次 train 呼叫裡的第三次，間隔約
8–10 秒。但批次 1–3 也各送三次、間隔相近卻沒失敗，所以「第三次」本身解釋不了；
兩次失敗當時帳號都正被另一位使用者重度使用，這個解釋至少同樣合理。
**緩解措施**（不論成因都便宜）：train 呼叫拉開間隔或一批最多送 2 個，
且重送前一律先對帳。

### 4. 上傳完整性 96/96

每一位送訓前都重新上傳取新 `media_id`，並逐張以 SHA-256 比對伺服器端 bytes。
**96 張全部相符，0 個不符，所有 hash 互異**——無靜默毀損、無錯人混入。

### 5. 訓練時間與張數相關

kanon-komori（唯一 6 張）明顯比同批兩個 5 張的慢完成。
zoey-yeh 最慢（約 35 分鐘），與帳號被並行重度使用一致。

## 五、未通過但經使用者裁決接受的事

**碰撞門檻實測未通過。** 遮髮盲測 6/8（V6 那一對完全對調），量化交叉檢查也 6/8
但錯在不同圖上。19 位裡 17 位至少牽涉一組 ≤0.0220 的配對；只有 angel-chiu、
zoey-yeh 乾淨。共同成因是 20 份 profile 共用同一段**同時鎖住膚色與五官族裔**的
`appearance.skin` 硬規格。

使用者親自肉眼複核後裁定接受。**測量結果照實保留，未塗改**；變更的是處置。
詳見 `../soul_pilot/VERDICT_collision_v1.md`、`../soul_pilot/SCREEN19_ROOT_CAUSE.md`、
`RULING_collision_accepted.md`。

由此衍生兩條**強制**規則：

- **C-1**：髮型從自由變數升級為**身分區分要件**。Soul V2 不繼承髮型，
  所以每次出圖必須寫該位自己的髮色髮型；有碰撞關係者不得換成對象的髮型。
- **C-2**：有碰撞關係的兩位**不得出現在同一則內容**。

## 六、待辦

1. **17 位的驗證圖要跑幾位**（全跑 ≈12.2 / 抽驗 5 位 ≈3.6 / 不跑 0）——待使用者決定。
2. **身材補正實測**。依決策 (B)，`profile.json` 的 `bust_cm 89 / cup_size D`
   維持不動，靠正式出圖的 prompt 補。**但這個補法尚未實測**，而
   `SEXY_SCENE_LIBRARY.md` 已載明「覆蓋度無法用 prompt 可靠控制」。
   若實測證明身材補不動，本決策須退回使用者重新裁決。
   見 `DECISION_body_spec_B.md`。
3. C-1／C-2 需寫進 `PERSONA_CANON.md` 與出圖 SOP，不能只留在本目錄。
