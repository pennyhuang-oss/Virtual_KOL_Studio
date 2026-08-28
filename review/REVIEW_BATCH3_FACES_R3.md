# Batch 3 臉部規劃 — R3：你的 F-02 與 F-03 互相衝突，還有 9 組配對過不了

## §0 給審閱者

**你只需要讀這一個檔案。**

你在 R2（`REVIEW_BATCH3_FACES_R2.md` §7）對四項意見全部給了「同意」，並指定了新的參考來源分配、
新的分離 gate、新的第一批名單。我已經把**能機械執行的部分全部套用**（§1）。

套用之後跑 gate，**171 組配對裡有 9 組過不了**，其中 3 組是**你的 F-02 修正自己製造出來的**。
另外有 8 位的參考來源改變，你說過「改來源後不能只換陣列，五個欄位都要依新來源重建」，
但 R2 只給了其中 3 位的方向，沒有給任何一位的重建文字。

這一輪要你補完這兩件事，**補完就可以開始生成第一批 8 位**。

**回覆方式**：寫在本檔案最下方 §6 回覆區（自成一行的 `REPLIES BELOW` 之後），然後 commit。

- 目前 commit：`55d6b3e`
- 議題編號從 **G-01** 起跳
- §5 有嚴格輸出格式，我會直接拿去生成

---

## §1 我已經照你的裁決做完的事

| 項目 | 狀態 |
|---|---|
| **F-01 措辭** | 已套用你指定的 `Image 1 / Image 2 / Image 3 / Image 4` 版本，19/19 位改寫完成。我提的 `first/second/third/fourth` 已捨棄。原句留存為 `face_en_v1_filename_form` 供比對。 |
| **F-01 附圖順序與 manifest** | 陣列順序固定 `[FACE_SHAPE_AND_JAW, EYES_AND_BROWS, NOSE, MOUTH]`；送出前寫入 persona-id、四槽位、實際路徑、陣列索引，順序不符 HARD FAIL。 |
| **F-01 備案** | 已記錄：第一批若穩定成立的部件低於 3/4，改用部件裁切輸入；再失敗才走兩階段生成，不得直接展開 19 位。 |
| **F-02 來源分配** | 你的 19 位臉型分配與 5 項鼻子改動已存為 `refs_v2`。驗證通過：臉型上限 2 位、鼻子上限 3 位、每位四槽都是四張不同圖。 |
| **F-03 gate** | 三條規則已實作為 `tools/check_face_gate.py`，原粗分群 gate 作廢。 |
| **F-04 第一批** | 已設為你指定的 8 位。 |
| **年齡族裔真理來源** | 已標記 `fixed` 為唯一真理來源，validator 逐字核對 FACE_EN 與 fixed 一致。 |

**我刻意沒做的一件事**：沒有把 `refs_v2` 直接覆蓋 `refs`。
因為你說過來源一改、五個欄位都要重建，而重建需要你對那些照片的骨相判讀。
現在直接換掉會變成「文字描述的是舊照片、附圖卻是新照片」的靜默不一致。
所以新來源存在 `refs_v2` 並標記 `needs_rebuild`，等你的重建文字到位才合併。

---

## §2 你的兩項修正互相衝突

F-02 讓 5 組人共用同一張 `FACE_SHAPE_AND_JAW`：

| 共用的圖 | 哪兩位 | 套上 F-03 的較嚴規則（總 ≥7、主導 ≥3）後 |
|---|---|---|
| `ref_15` | angel-chiu、cheryl-soh | ✅ 通過 |
| `ref_11` | emma-kao、wendy-yeo | ❌ **不過**（總 6／需 7，主導 3／需 3） |
| `ref_04` | zoey-yeh、kanon-komori | ❌ **不過**（總 5／需 7，主導 3／需 3） |
| `ref_05` | miu-shiraishi、somi-oh | ❌ **不過**（總 6／需 7，主導 3／需 3） |
| `ref_02` | jia-seo、angeline-kwee | ✅ 通過 |

**5 組裡有 3 組不過。** 這 3 組在你 R2 之前是通過的——是 F-02 把它們配成共用來源，
才觸發 F-03 的較嚴門檻。你的兩項修正在這裡打架。

**G-01｜請裁決**：
1. 這 3 組要怎麼處理？把其中一位的臉型來源換掉（但 15 張已經排滿，換誰去哪）？
   還是調整它們的軸值把距離拉到 7/3？
2. 或者「共用臉型來源就要 7/3」這條規則本身要放寬？
   如果放寬，放寬到多少、理由是什麼？

---

## §3 9 組配對過不了 gate

| 總相異／需 | 主導軸／需 | 組合 | 共用臉型來源 | 在第一批 | R2 有給方向嗎 |
|---|---|---|---|---|---|
| 4／6 | 2／2 | miu-shiraishi vs sydney-leong |  | 兩位都在 | ✅ 有 |
| 4／6 | 3／2 | yerin-han vs peggy-lee |  | 兩位都在 | ✅ 有 |
| 4／6 | 4／2 | tammy-chou vs sydney-leong |  | 兩位都在 | ✅ 有 |
| 5／6 | 2／2 | angel-chiu vs yerin-han |  | 一位在 | ❌ **沒有** |
| 5／6 | 2／2 | wanyin-jiang vs angeline-kwee |  | 一位在 | ❌ **沒有** |
| 5／6 | 4／2 | ruoruo-tang vs peggy-lee |  | 一位在 | ❌ **沒有** |
| 5／7 | 3／3 | zoey-yeh vs kanon-komori | 是 | 一位在 | ❌ **沒有** |
| 6／7 | 3／3 | emma-kao vs wendy-yeo | 是 | 一位在 | ❌ **沒有** |
| 6／7 | 3／3 | miu-shiraishi vs somi-oh | 是 | 一位在 | ❌ **沒有** |

**R2 只給了 3 組的調整方向**（Sydney 重建、Yerin 改 ref_12、Peggy 改 ref_14），
而且那 3 組的方向是文字描述，沒有具體的軸值。**另外 6 組完全沒有處理。**

其中 **3 組完整落在第一批 8 位裡**（miu↔sydney、yerin↔peggy、tammy↔sydney）——
那正是你刻意把它們放進第一批的原因。這 3 組不解決，第一批就不能跑。

**G-02｜請給出具體的軸值調整**。這 9 組每一組都要處理，格式見 §5。

---

## §4 8 位的參考來源改了，文字還沒重建

你在 F-02 寫：「改來源後不能只換陣列：ARCHETYPE、AXES、FACE_EN、MARKERS、WHY_DISTINCT
與 hash 都必須依新來源同步重建。」

以下 8 位的來源確實改了：

| persona | 槽位 | 舊來源 → 新來源 | 在第一批 |
|---|---|---|---|
| `cheryl-soh` | NOSE | `ref_01` → `ref_06` |  |
| `nanami-fujiwara` | FACE_SHAPE_AND_JAW | `ref_15` → `ref_03` |  |
| `peggy-lee` | FACE_SHAPE_AND_JAW | `ref_11` → `ref_14` | **是** |
| `peggy-lee` | NOSE | `ref_12` → `ref_11` | **是** |
| `rin-ayase` | NOSE | `ref_01` → `ref_14` |  |
| `ruoruo-tang` | FACE_SHAPE_AND_JAW | `ref_11` → `ref_10` |  |
| `ruoruo-tang` | NOSE | `ref_10` → `ref_14` |  |
| `sydney-leong` | FACE_SHAPE_AND_JAW | `ref_08` → `ref_06` | **是** |
| `yerin-han` | FACE_SHAPE_AND_JAW | `ref_11` → `ref_12` | **是** |
| `yerin-han` | NOSE | `ref_01` → `ref_03` | **是** |
| `zhiyi-shen` | FACE_SHAPE_AND_JAW | `ref_02` → `ref_09` |  |

**其中 3 位在第一批**（yerin-han、peggy-lee、sydney-leong），所以第一批同樣卡在這裡。

**G-03｜請給出這 8 位重建後的完整欄位**，格式見 §5。

---

### 這 8 位目前的規格（供你對照）

**`cheryl-soh`**（25 歲・新加坡華裔（Chinese-Singaporean）・空服員）
來源變動：NOSE ref_01→ref_06
- ARCHETYPE: 長卵形、下庭略長、五官垂直舒展的專業成人臉
- AXES: 輪廓原型=長卵形; 臉長寬比=長窄; 三庭配置=中庭+長下庭; 骨肉量=骨肉均衡; 五官場=垂直舒展; 顎頦=窄顎+長鈍頦; 眼眶結構=圓開平視; 眼距=寬; 鼻部量體=長直細鼻; 口部幾何=小中等唇; 頰部=低位柔頰
- MARKERS: long oval canvas; vertically spaced features; wide-set open eyes; low cheek volume; long blunt chin
- WHY_DISTINCT: 她比最接近的 nanami 下庭更長、眼距更寬且五官更垂直舒展，也沒有 rainie 的高顴與短尖頦。

**`nanami-fujiwara`**（23 歲・日本・溫泉旅館女將見習）
來源變動：FACE_SHAPE_AND_JAW ref_15→ref_03
- ARCHETYPE: 寬卵形、低骨感、下巴短鈍的端莊成人臉
- AXES: 輪廓原型=寬卵形; 臉長寬比=中等; 三庭配置=均衡; 骨肉量=骨肉均衡; 五官場=均衡; 顎頦=窄顎+小圓頦; 眼眶結構=細長平視; 眼距=中等; 鼻部量體=短寬軟鼻; 口部幾何=小中等唇; 頰部=低位柔頰
- MARKERS: broad oval outline; balanced facial thirds; medium level eyes; low soft cheeks; small rounded chin
- WHY_DISTINCT: 她比最接近的 angel 臉更長更卵形、眼裂較細且下顎不方，也沒有 rainie 的高顴與尖銳下巴。

**`peggy-lee`**（24 歲・馬來西亞華裔（Chinese-Malaysian）・汽車改裝店行銷企劃）
來源變動：FACE_SHAPE_AND_JAW ref_11→ref_14；NOSE ref_12→ref_11
- ARCHETYPE: 窄額寬顎、五官偏大的梯形張力成人臉
- AXES: 輪廓原型=梯形; 臉長寬比=中等; 三庭配置=短中庭+中下庭; 骨肉量=寬骨量; 五官場=橫向分散; 顎頦=寬方顎+方頦; 眼眶結構=窄長上揚; 眼距=寬; 鼻部量體=中等直鼻+鈍鼻頭; 口部幾何=寬飽滿下唇; 頰部=平直中臉
- MARKERS: narrow forehead with broad jaw; wide-set elongated eyes; restrained lid height; square chin; wide full lower lip
- WHY_DISTINCT: 她比最接近的 wendy 臉較短、額窄顎寬且眼距更大；雖有上揚眼，梯形寬下臉使她不會落入 rainie 的倒三角尖顎。

**`rin-ayase`**（25 歲・日本・高級會員制酒店小姐）
來源變動：NOSE ref_01→ref_14
- ARCHETYPE: 窄長鑽石型、顴區清楚、眼裂細長的成熟臉
- AXES: 輪廓原型=窄長鑽石; 臉長寬比=長窄; 三庭配置=長中庭+中下庭; 骨肉量=清瘦平面; 五官場=均衡; 顎頦=窄顎+長鈍頦; 眼眶結構=細長平視; 眼距=中等; 鼻部量體=中等直鼻+鈍鼻頭; 口部幾何=寬中等唇; 頰部=高位平顴
- MARKERS: long diamond outline; narrow level eyes; high planar cheeks; medium straight nose; long blunt chin
- WHY_DISTINCT: 她比最接近的 angeline 顴部更寬、嘴更寬而下巴較鈍；窄平視眼也切斷 rainie 的大上揚眼預設。

**`ruoruo-tang`**（27 歲・中國・皮拉提斯教練）
來源變動：FACE_SHAPE_AND_JAW ref_11→ref_10；NOSE ref_10→ref_14
- ARCHETYPE: 寬中臉、鈍下巴、骨肉均衡的運動成人臉
- AXES: 輪廓原型=寬卵形; 臉長寬比=中等; 三庭配置=均衡; 骨肉量=寬骨量; 五官場=橫向分散; 顎頦=寬顎+短鈍頦; 眼眶結構=細長平視; 眼距=寬; 鼻部量體=中等直鼻+鈍鼻頭; 口部幾何=寬中等唇; 頰部=平直中臉
- MARKERS: broad middle face; wide-set level eyes; straight cheek planes; broad jaw; short blunt chin
- WHY_DISTINCT: 她比最接近的 angel 臉更長、骨量更大且眼裂較細，寬顎鈍頦也與 rainie 的窄尖下顎不同。

**`sydney-leong`**（22 歲・馬來西亞華裔（Chinese-Malaysian）・甜點師 / 烘焙工作室）
來源變動：FACE_SHAPE_AND_JAW ref_08→ref_06
- ARCHETYPE: 短寬圓角方形、雙頰中段飽滿的甜感成人臉
- AXES: 輪廓原型=短寬圓角方; 臉長寬比=短寬; 三庭配置=短中庭+中下庭; 骨肉量=柔軟飽滿; 五官場=橫向分散; 顎頦=柔方顎+短鈍頦; 眼眶結構=圓開下垂; 眼距=寬; 鼻部量體=短寬軟鼻; 口部幾何=寬中等唇; 頰部=中段飽滿
- MARKERS: short rounded-square outline; wide-set downturned eyes; full middle cheeks; short broad nose; short blunt chin
- WHY_DISTINCT: 她比最接近的 tammy 下顎更方、額部較不寬且雙頰更集中，並以鈍顎下垂眼避開 rainie 的尖顎上揚眼。

**`yerin-han`**（26 歲・韓國・高爾夫教練 / 練習場）
來源變動：FACE_SHAPE_AND_JAW ref_11→ref_12；NOSE ref_01→ref_03
- ARCHETYPE: 寬額寬顎、短中庭的直線方臉
- AXES: 輪廓原型=短寬圓角方; 臉長寬比=短寬; 三庭配置=短中庭+中下庭; 骨肉量=寬骨量; 五官場=橫向分散; 顎頦=寬方顎+方頦; 眼眶結構=圓開平視; 眼距=寬; 鼻部量體=中等直鼻+鈍鼻頭; 口部幾何=小中等唇; 頰部=平直中臉
- MARKERS: equal-width forehead and jaw; short midface; wide-set level eyes; broad square chin; compact restrained lips
- WHY_DISTINCT: 她比最接近的 wendy 更短更寬、眼睛更開且眼距更大，寬方顎與小口也直接偏離 rainie 的窄尖顎厚唇。

**`zhiyi-shen`**（25 歲・中國・金融業 OL）
來源變動：FACE_SHAPE_AND_JAW ref_02→ref_09
- ARCHETYPE: 高額長中庭、窄矩形輪廓的冷靜骨感成人臉
- AXES: 輪廓原型=窄矩形; 臉長寬比=極長窄; 三庭配置=長中庭+中下庭; 骨肉量=清瘦平面; 五官場=集中; 顎頦=柔方顎+短鈍頦; 眼眶結構=低眉窄眼; 眼距=窄; 鼻部量體=長直細鼻; 口部幾何=小薄平唇; 頰部=平直中臉
- MARKERS: very long narrow rectangle; high forehead; close-set low-brow eyes; long narrow nose; blunt narrow jaw
- WHY_DISTINCT: 她比最接近的 emma 更窄更長、眉眼更低更集中；平直中臉與薄平唇排除 rainie 的高顴厚唇吸引子。

---

## §5 兩件小事 ＋ 輸出格式

**G-04｜P2｜你的新指派句與原有的收尾句重複了。** 套用後每段 FACE_EN 現在同時有：

> ... Combine these four assigned components into one coherent new identity. Build a ... **Synthesize these four components into one new coherent identity**; each reference contributes its assigned geometry rather than a complete likeness.

兩句在講同一件事。後半句的「each reference contributes its assigned geometry rather than a complete likeness」
是有意義的、不重複，但「Synthesize these four components into one new coherent identity」與你新句的
「Combine these four assigned components into one coherent new identity」是同義重複。
prompt 冗贅正是稀釋訊號的成因之一。要刪哪一句？還是兩句都留？

**G-05｜P2｜`ref_13` 現在沒有任何人拿它當臉型來源了。** 這是刻意的（它的輪廓不適合當骨架來源），
還是重新分配時的副作用？它仍被用在眼眉與口部。

### 輸出格式

**(G-01) 共用來源衝突的裁決** — 明確講三組各怎麼處理。

**(G-02+G-03) 需要改動的角色** — 每位一段，**只列出你實際要改的角色**。
§4 的 8 位是一定要重建的（來源已經換了）；§3 的 9 組配對牽涉到 18 位，但你不必全改——
每組只要動其中一位就能把距離拉開，請自己判斷動誰代價最小。格式與 R1 完全相同，欄位要給全：

```
### <persona-id>
ARCHETYPE: <中文一句話原型>
AXES: <11 條全給，分號分隔，值必須在原維度表的允許值內>
FACE_EN: <完整英文段落。參考指派句用你 R2 指定的 Image 1..4 版本，不要再寫檔名>
NEGATIVE_EN: <否定清單或 NONE>
MARKERS: <3–5 個，英文，分號分隔，左右翻轉後仍成立>
WHY_DISTINCT: <中文一句話>
```

**(G-04)(G-05)** — 各一句話回答。

**最後請確認一句**：改完之後，第一批 8 位是否就可以開始生成？
還是你認為要先跑更小的技術探針（例如只跑 1 位、4 張，先確認「四張圖各司其職」這個假說成不成立）？
我傾向後者——你在 F-01 自己也說那仍是待驗證假說，而 32 張全跑下去如果假說不成立就是全廢。

---

## §6 回覆區

REPLIES BELOW
