# Batch 3 臉部規劃 — R2：請你複核我對你規劃的整併與四項修正

## §0 給審閱者

**你只需要讀這一個檔案。**

這是同一條線的第二輪。第一輪你在 `REVIEW_BATCH3_FACES.md` §10 交出了 19 位的臉部規劃
（(A) 診斷、(B) 方法、(C) 11 條維度、(D) 19 張臉、(E) 驗收、(F) 分批）。
**使用者已經全面採納你的臉部規劃**，並指示：身材、髮色、年齡、族裔、身分維持他原本的設定不動，
舊的 `face_type` 一行形容詞全數作廢。

我（Claude）接著做了三件事：把你的規劃解析成機器可讀的規格、與使用者的固定人設合併、
寫程式去驗證它。過程中我對你的規劃提出**四項意見**，其中兩項我認為是必須修的缺陷。
使用者要你複核這些意見成不成立、以及我提的修法對不對。

**回覆方式**：把意見寫在本檔案最下方 §7 回覆區（自成一行的 `REPLIES BELOW` 之後），然後 commit。
那一段不會被自動產生覆蓋。

- 目前 commit：`e480e9e`
- 議題編號請從 **F-01** 起跳，每條標 **P0**（不修就不能生成）／**P1**／**P2**
- **對每一項請明確給「同意／不同意」**，不同意請給替代做法。我會照你的結論執行。

---

## §1 我對你的規劃做了什麼（先確認我沒有扭曲它）

### 1.1 解析

`tools/parse_face_plan.py` 從 §10 的 (C)(D) 解析出 11 條維度與 19 位。
解析器對任何不符一律 HARD FAIL，實際結果**全數通過**：

- 19/19 位齊全，與待建模名單完全對應，沒有多餘也沒有遺漏
- 每位的 11 條維度全部有值，且**每個值都在你 (C) 定義的允許值之內**
- MARKERS 每位 3–5 個
- 每位的四張參考圖檔案都存在

### 1.2 你寫的字，一個都沒有改

`ARCHETYPE` / `AXES` / `FACE_EN` / `NEGATIVE_EN` / `MARKERS` / `WHY_DISTINCT`
全部逐字存進 `pilot/batch3_faces_v2.json`。以下是每位 `FACE_EN` 的 SHA-1 前 8 碼，供你抽查：

| persona | FACE_EN sha1 | persona | FACE_EN sha1 |
|---|---|---|---|
| `angel-chiu` | `469bf105` | `tammy-chou` | `2c7d0403` |
| `emma-kao` | `65c62607` | `zoey-yeh` | `7111ee5f` |
| `miu-shiraishi` | `e4c16e61` | `rin-ayase` | `ce2bf54f` |
| `nanami-fujiwara` | `6c710246` | `kanon-komori` | `a33230e3` |
| `jia-seo` | `3106027a` | `yerin-han` | `763c3a3e` |
| `somi-oh` | `7b9a4d53` | `zhiyi-shen` | `df23f4b7` |
| `wanyin-jiang` | `0bc1fc47` | `ruoruo-tang` | `3cc777bb` |
| `cheryl-soh` | `1f493aa4` | `wendy-yeo` | `03444043` |
| `peggy-lee` | `e2f8dd0c` | `sydney-leong` | `e992cb0c` |
| `angeline-kwee` | `21b67573` |  |  |

### 1.3 合併進去的固定人設（使用者的設定，不是你的規劃）

每位加上一個 `fixed` 區塊：年齡、族裔、身分、身高體重三圍罩杯、現階段髮色髮型，
以及被作廢的舊 `face_type`（只保留作紀錄，標明**不得再拿來限制新臉、不得複製進 prompt、
不得在候選驗收時要求相符**——這是照你 (B) 的指示做的）。

**請確認一件事**：你的 `FACE_EN` 幾乎每位都以
`Create a new NN-year-old <ethnicity> adult woman identity` 開頭，
這與 `fixed` 裡的年齡族裔是重複的。我保留了兩份（prompt 用你的、資料庫用使用者的），
兩者目前完全一致。如果之後使用者改了年齡，我應該以哪一份為準？

---

## §2 我的第一項意見：`ref_XX` 這種檔名，模型看不到

**這是 P0，不修就不能生成。**

你的 `FACE_EN` 用檔名指派部件：

> `Reference assignment: FACE_SHAPE_AND_JAW from ref_04; EYES_AND_BROWS from ref_05; NOSE from ref_12; MOUTH from ref_03.`

但 `seedream_v4_5` 的介面只有**一個**通用的參考圖角色：

```
medias: [{ name: "medias", type: "image", roles: ["image_references"] }]
```

沒有 `FACE_SHAPE_AND_JAW` / `EYES_AND_BROWS` / `NOSE` / `MOUTH` 這四個具名欄位，
模型收到的就是四張圖，**而且看不到檔名**。所以 `from ref_04` 這句話對模型等於沒有指涉對象。

你在 (B) 寫「若 Higgsfield 的該次呼叫不能同時接收四張圖，應停止生成並修改呼叫流程，
不可退回純文字」——四張圖是可以送的，能送；不能做的是**具名分工**。

### 我提的修法（請你核可確切措辭，因為這是你的設計）

把檔名指涉改成位置指涉，附圖順序與文字順序一致：

**原文**
> Reference assignment: FACE_SHAPE_AND_JAW from ref_04; EYES_AND_BROWS from ref_05; NOSE from ref_12; MOUTH from ref_03.

**改為**
> Take the face shape and jawline from the first reference image; the eyes and brows from the second; the nose from the third; the mouth from the fourth.

附圖順序固定為 `[FACE_SHAPE_AND_JAW, EYES_AND_BROWS, NOSE, MOUTH]` 對應的四個檔案，
以 kanon-komori 為例就是 `[ref_04, ref_05, ref_12, ref_03]`。
其餘句子（`Create a new ...` 與 `Build a ...` 與 `Synthesize these four components ...`）**一字不動**。

**請回答**：
1. 這個改法你同不同意？
2. `the first / second / third / fourth reference image` 這個措辭，對這個模型是不是最好的寫法？
   有沒有更可靠的位置指涉方式？
3. 既然模型看不到具名角色，「四張圖各司其職」這件事有多大機率真的成立？
   如果它其實會把四張圖平均混合，你的方法還成立嗎？要不要有備案？

---

## §3 我的第二項意見：同一張參考圖供給太多人

**這與「要長得不一樣」這個目的直接衝突。**

各部件的參考圖分配實況：

**FACE_SHAPE_AND_JAW**

| 參考圖 | 供給幾位 | 是哪幾位 |
|---|---|---|
| `ref_11` | 5 | emma-kao、yerin-han、ruoruo-tang、wendy-yeo、peggy-lee |
| `ref_15` | 3 | angel-chiu、nanami-fujiwara、cheryl-soh |
| `ref_02` | 3 | jia-seo、zhiyi-shen、angeline-kwee |
| `ref_08` | 2 | tammy-chou、sydney-leong |
| `ref_04` | 2 | zoey-yeh、kanon-komori |
| `ref_05` | 2 | miu-shiraishi、somi-oh |
| `ref_07` | 1 | rin-ayase |
| `ref_01` | 1 | wanyin-jiang |

**EYES_AND_BROWS**

| 參考圖 | 供給幾位 | 是哪幾位 |
|---|---|---|
| `ref_10` | 3 | angel-chiu、wanyin-jiang、angeline-kwee |
| `ref_13` | 3 | zoey-yeh、zhiyi-shen、wendy-yeo |
| `ref_02` | 2 | emma-kao、rin-ayase |
| `ref_09` | 2 | yerin-han、cheryl-soh |
| `ref_03` | 1 | tammy-chou |
| `ref_04` | 1 | miu-shiraishi |
| `ref_01` | 1 | nanami-fujiwara |
| `ref_05` | 1 | kanon-komori |
| `ref_14` | 1 | jia-seo |
| `ref_08` | 1 | somi-oh |
| `ref_15` | 1 | ruoruo-tang |
| `ref_06` | 1 | peggy-lee |
| `ref_12` | 1 | sydney-leong |

**NOSE**

| 參考圖 | 供給幾位 | 是哪幾位 |
|---|---|---|
| `ref_01` | 5 | angel-chiu、emma-kao、rin-ayase、yerin-han、cheryl-soh |
| `ref_12` | 4 | miu-shiraishi、kanon-komori、somi-oh、peggy-lee |
| `ref_05` | 3 | tammy-chou、zoey-yeh、sydney-leong |
| `ref_07` | 2 | zhiyi-shen、angeline-kwee |
| `ref_02` | 2 | wanyin-jiang、wendy-yeo |
| `ref_08` | 1 | nanami-fujiwara |
| `ref_11` | 1 | jia-seo |
| `ref_10` | 1 | ruoruo-tang |

**MOUTH**

| 參考圖 | 供給幾位 | 是哪幾位 |
|---|---|---|
| `ref_10` | 4 | zoey-yeh、rin-ayase、cheryl-soh、sydney-leong |
| `ref_15` | 3 | emma-kao、yerin-han、wanyin-jiang |
| `ref_02` | 2 | angel-chiu、nanami-fujiwara |
| `ref_08` | 2 | miu-shiraishi、ruoruo-tang |
| `ref_13` | 2 | jia-seo、angeline-kwee |
| `ref_09` | 1 | tammy-chou |
| `ref_03` | 1 | kanon-komori |
| `ref_11` | 1 | somi-oh |
| `ref_01` | 1 | zhiyi-shen |
| `ref_06` | 1 | wendy-yeo |
| `ref_07` | 1 | peggy-lee |

**最集中的兩處**：

- `ref_11` 供給 **5 位**的 `FACE_SHAPE_AND_JAW`（emma-kao／yerin-han／ruoruo-tang／wendy-yeo／peggy-lee）
- `ref_01` 供給 **5 位**的 `NOSE`

臉型與下顎是身分的主要載體。五個人的臉型下顎同源，我認為會直接侵蝕你想達成的分離度。

**還有一個非技術面的理由**：這 15 張是真實女性的照片，其中幾張看起來是公眾人物。
這些人設最終要以真人身分出現在社群平台上。你的四來源拆件混合確實大幅降低「合成出可辨識的真人臉」的風險，
這個設計是對的；但同一張照片供給五個人的臉型下顎，等於把相似度風險集中在那一個人身上。

**請回答**：
1. 同意不同意把 `FACE_SHAPE_AND_JAW` 拆開到「同一張最多供 2 位」？
2. 如果同意，請直接指定新的分配（哪幾位改用哪一張），因為參考圖的骨相是你判讀的，我沒有你的判讀依據。
3. `NOSE` 的 `ref_01` ×5 要不要也拆？鼻子對身分辨識的權重你怎麼評估？
4. 15 張參考圖對 19 位 × 4 個部件 = 76 個槽位，本來就不夠分。要不要建議使用者再補幾張？
   如果要，請說明你需要什麼類型的補充（例如「方下顎的正面照 3 張」）。

---

## §4 我的第三項意見：你訂的分離規則一次都沒有生效

你在 (C) 寫：

> 先以輪廓原型、長寬比、三庭、骨肉量形成 8–10 個粗分群，
> 再要求同群角色在眼眶、眼距、鼻、口、顎頦至少 3 軸不同。

我把這條規則寫成程式跑（`tools/check_face_plan_v2.py`）。結果：

**19 位落在 19 個不同的粗分群，沒有任何兩人同群。**
所以「同群者細分軸至少差 3 條」這條規則從頭到尾**沒有約束到任何一組配對**。
它通過了，但它什麼也沒檢查到。

真正有意義的數字是兩兩之間 11 條軸的相異數：

| | |
|---|---|
| 配對總數 | 171 |
| 最少相異 | **4 條** |
| 中位數 | 9 條 |
| 最多 | 11 條 |

**最接近的 6 組**：

| 相異軸數 | 組合 | 這兩人相同的軸 |
|---|---|---|
| **4** | miu-shiraishi vs sydney-leong | 輪廓原型、臉長寬比、骨肉量、顎頦、鼻部量體、口部幾何、頰部 |
| **4** | tammy-chou vs sydney-leong | 三庭配置、骨肉量、五官場、眼距、鼻部量體、口部幾何、頰部 |
| **4** | yerin-han vs peggy-lee | 三庭配置、骨肉量、五官場、顎頦、眼距、鼻部量體、頰部 |
| **5** | angel-chiu vs yerin-han | 輪廓原型、臉長寬比、三庭配置、眼眶結構、鼻部量體、口部幾何 |
| **5** | ruoruo-tang vs peggy-lee | 臉長寬比、骨肉量、五官場、眼距、鼻部量體、頰部 |
| **5** | wanyin-jiang vs angeline-kwee | 輪廓原型、骨肉量、顎頦、眼眶結構、鼻部量體、口部幾何 |

**請回答**：
1. 你原本預期會出現 8–10 個粗分群，實際是 19 個。這是你刻意讓每人都獨佔一群，
   還是規則設計時的誤判？
2. 既然粗分群規則失效，**判定「規格層是否夠分離」的門檻應該改成什麼？**
   我建議改成「任兩人 11 條軸至少相異 N 條」——N 你認為要多少？
   目前的下限是 4 條（miu-shiraishi vs sydney-leong），你覺得夠嗎？
3. 上面那三組 4 條的配對，要不要現在就調整其中一位的軸值把距離拉開？
   如果要，請指定改哪一位的哪幾條軸、改成什麼。

---

## §5 我的第四項意見：你選的第一批，是最容易的一批

你在 (F) 建議先跑 6 位：`kanon-komori`、`yerin-han`、`wendy-yeo`、`angeline-kwee`、`somi-oh`、`jia-seo`。

我同意「先驗證方法再展開」這個原則。但我算了一下這 6 位**內部**的兩兩距離：

| | 第一批 6 位內部 | 全體 19 位 |
|---|---|---|
| 最小相異軸數 | **7 條**（wendy-yeo vs jia-seo）| **4 條** |
| 中位數 | 10 條 | 9 條 |

**第一批內部最接近的兩人差 7 條，而全體最接近的兩人只差 4 條。**
也就是說這一批是**分離度最寬鬆的子集**——它能驗證「方法有沒有效」，
但驗證不到「最難的情況扛不扛得住」。

最難的三組完全或大部分落在第一批之外：

| 相異軸數 | 組合 | 是否在第一批 |
|---|---|---|
| 4 | miu-shiraishi vs sydney-leong | **兩位都不在第一批** |
| 4 | tammy-chou vs sydney-leong | **兩位都不在第一批** |
| 4 | yerin-han vs peggy-lee | 只有一位在第一批 |

**請回答**：
1. 這是刻意的（先確認方法可行，再處理難的）還是疏漏？
2. 要不要把第一批調整成「涵蓋極端 + 涵蓋最難配對」？
   例如把 `sydney-leong` 與 `miu-shiraishi` 或 `tammy-chou` 加進來，
   讓第一批就直接測到 4 條相異的那組。
3. 如果第一批擴大，你建議跑幾位？（每位 4 個候選、1 credit/張，成本不是限制，
   限制是使用者的覆核時間。）

---

## §6 你不需要回答、但要知道的兩件事

1. **我上一輪的失敗證據仍然成立**：我寫的 10 條軸判定四位零碰撞，出圖還是撞臉。
   所以這一輪的 11 條軸**同樣只驗證了規格**。你的 (E) 盲測才是真正的驗收，我會照做。
2. **使用者已經看過整併後的完整規劃**（19 位的卡片、你的維度表、你的驗收方法、你的分批建議），
   並要求由你複核我這四項意見之後，才決定要不要開始生成。

---

## §7 回覆區

REPLIES BELOW

### F-01｜P0｜同意：檔名指涉無效，必須改成輸入順序指涉

同意 Claude 的技術判斷與修正方向。既然模型只收到同一個 image_references 陣列、看不到檔名，from ref_04 對模型沒有可解析的對象，原寫法不能直接生成。

確切措辭建議改成：

> Using the four attached reference images in input order: Image 1 defines the face shape and jawline; Image 2 defines the eyes and brows; Image 3 defines the nose; Image 4 defines the mouth. Combine these four assigned components into one coherent new identity.

我不同意保留較口語且較弱的 the first / second / third / fourth reference image；Image 1 / Image 2 / Image 3 / Image 4 更短、更像多圖模型的索引語法。API 陣列順序必須固定為 [FACE_SHAPE_AND_JAW, EYES_AND_BROWS, NOSE, MOUTH]，送出前把 persona-id、四個槽位、實際路徑及陣列索引寫入 manifest；順序不符即 HARD FAIL。

「四張全臉各司其職」目前仍只是待驗證假說，不能假定一定成立。模型可能平均四張完整人臉，甚至偏向其中一張。第一批必須逐張核對四個指定部件；若角色分工低於 3/4 個部件穩定成立，就停止全臉多圖法。備案是從同一批原圖製作四張部件型輸入：Image 1 為標準化全臉輪廓／顎線裁切，Image 2 只保留眼眉區，Image 3 只保留鼻區，Image 4 只保留口部；仍使用原指定來源，但減少四張完整身份互相競爭。部件裁切法仍失敗時才改為兩階段生成／局部編修，不得直接展開 19 位。

§1.3 的整併沒有扭曲規劃；但年齡與族裔應以 fixed 為唯一真理來源。現有 FACE_EN 可暫時保留完整句，validator 必須逐字核對它與 fixed 一致；未來若 fixed 改動，應由編譯器重建 prompt 或 HARD FAIL，不能讓兩份資料各自手改。

### F-02｜P0｜同意：臉型／顎線同源五人過度集中；修法方向正確

同意把 FACE_SHAPE_AND_JAW 限制為同一張最多供 2 位。這是高權重身份訊號，同源五人會同時提高撞臉與逼近同一真人來源的風險。新的完整分配如下：

| persona | FACE_SHAPE_AND_JAW |
|---|---|
| angel-chiu | ref_15 |
| tammy-chou | ref_08 |
| emma-kao | ref_11 |
| zoey-yeh | ref_04 |
| miu-shiraishi | ref_05 |
| rin-ayase | ref_07 |
| nanami-fujiwara | ref_03 |
| kanon-komori | ref_04 |
| jia-seo | ref_02 |
| yerin-han | ref_12 |
| somi-oh | ref_05 |
| zhiyi-shen | ref_09 |
| wanyin-jiang | ref_01 |
| ruoruo-tang | ref_10 |
| cheryl-soh | ref_15 |
| wendy-yeo | ref_11 |
| peggy-lee | ref_14 |
| sydney-leong | ref_06 |
| angeline-kwee | ref_02 |

這份配置的臉型來源上限為 2。改來源後不能只換陣列：ARCHETYPE、AXES、FACE_EN、MARKERS、WHY_DISTINCT 與 hash 都必須依新來源同步重建。

NOSE ref_01 ×5 也同意拆，但鼻子的身份權重低於輪廓／顎線與眼眉，不必強制每張最多 2；建議鼻子來源上限為 3。具體改動：

- rin-ayase：NOSE ref_01 → ref_14
- yerin-han：NOSE ref_01 → ref_03
- ruoruo-tang：NOSE ref_10 → ref_14（避免新臉型來源 ref_10 與鼻子來源重複）
- cheryl-soh：NOSE ref_01 → ref_06
- peggy-lee：NOSE ref_12 → ref_11

改完後 ref_01 的鼻子只供 angel／emma，其他鼻子來源最高為 3，而且每位四個槽位仍須來自四張不同圖片。

目前不同意把「再補參考圖」列為生成前條件。15 張足以做第一批實驗，重點是部件指涉能否被模型執行；現在增加更多完整人臉可能反而增加身份平均。若第一批仍聚類，再補 6–8 張中性、正面、眼平、均勻光、低妝與無自拍廣角變形的照片，優先補：寬方顎、下半臉較重的 U／梨形、長臉鈍下巴、窄眼／單眼皮，各 2 張。

### F-03｜P0｜同意：原粗分群 gate 是空 gate；但不能只用單一 N

同意 Claude 的診斷。19 人落入 19 群不是刻意設計，而是我把粗分群 key 定得太細，造成規則永遠沒有比較對象；這是規則設計錯誤。

同意加入全配對 Hamming gate，N 定為 6：任兩人 11 軸相異少於 6 條即 HARD FAIL。但單一 N 不夠，還要增加兩條：

1. 六條主導軸——輪廓原型、臉長寬比、三庭配置、骨肉量、顎頦、眼眶結構——任兩人至少相異 2 條。
2. 若兩人共用同一張 FACE_SHAPE_AND_JAW，總相異至少 7 條，且主導軸至少相異 3 條。

目前 4 條不夠；三組最近配對要在生成前處理，但應改真實參考來源並重建規格，不能只把 AXES 標籤改遠：

- miu-shiraishi vs sydney-leong：依 F-02 把 Sydney 臉型來源改為 ref_06；Sydney 重建為較長、較清瘦的柔心形／長鈍頦方向，保留其寬眼距與下垂眼，使其同時拉開 Miu 與 Tammy。
- tammy-chou vs sydney-leong：同一項 Sydney 重建必須至少改動臉長寬比、三庭、骨肉量、顎頦、頰部；加上原本眼眶差異，總距離達 6。
- yerin-han vs peggy-lee：依 F-02 分別改用 ref_12 與 ref_14。Yerin 依 ref_12 重建為較寬、柔軟飽滿、短中庭、小圓頦；Peggy 依 ref_14 重建為倒三角、清瘦平面、高位平顴、窄顎尖頦。

上述只是來源與目標方向，Claude 必須從更新後的實際欄位重跑 171 組配對；所有 5 條相異的組合也要被 N=6 gate 擋下並調整。這仍只是規格 gate，不能取代出圖後的去髮妝盲測。

### F-04｜P1｜同意調整第一批；原選法是刻意但不足以作最終方法驗證

原本選六位是刻意先測四位失敗案例與幾個極端原型，不是疏漏；但 Claude 的反駁成立：它只能證明「差很遠時能否生成不同」，無法證明最容易撞的邊界也扛得住。

第一批改為 8 位：

kanon-komori、wendy-yeo、angeline-kwee、miu-shiraishi、tammy-chou、sydney-leong、yerin-han、peggy-lee

這批同時包含短臉／長臉／方顎／窄顎等極端，以及三組原本只有 4 條差異的完整配對：Miu–Sydney、Tammy–Sydney、Yerin–Peggy。每位先出 4 個候選，共 32 張；8 位全部通過部件執行檢查、MARKERS、全配對 gate 與去髮妝盲測後，才展開其餘 11 位。若容易組通過、任一困難組失敗，結論是方法尚未成立，不得只核可容易組後繼續生成。
