# Batch 3 臉部規劃 — R7：你的手工分配我用解算器複核過，最後缺 4 張

## §0 給審閱者

**你只需要讀這一個檔案。**

你 R6 交的 26 配 13 BLOCK，我把它當成一個約束滿足問題重跑了一次（§1）。
**結論是你手工排的已經接近最優**——不是排差了。13 個 BLOCK 裡只有 1 個是純排程問題
（就是你自己已經指出的 `kanon-komori／NOSE` 搬移），其餘是真的缺幾何。

把剩下的缺口去重之後是 11 種幾何，而 **4 張新來源就能全部關上**，
我已經用程式驗證加入之後 76/76 全滿、四來源互異與 slot cap 全過（§3、§4）。

**回覆方式**：寫在本檔案最下方 §6 回覆區（自成一行的 `REPLIES BELOW` 之後），然後 commit。

- 目前 commit：`5464578`
- 議題編號從 **L-01** 起跳
- 這一輪要你做兩件事：生那 4 張、核 §5 的完整 76 格分配表

---

## §1 解算結果：你排的接近最優

我把「相容」限定成兩個來源，**沒有自己發明任何相容性**：

- (a) 你曾經指派過的 `(persona, slot, ref)`；
- (b) 你在 K-02 的 BLOCK 理由裡明講「相符／同幾何」但因為被佔用或 cap 滿而不能用的
  （例如「`ref_28` 是唯一瘦長六角方向，但已供她的寬薄 MOUTH」＝ `ref_28` 相容於 jia-seo 的 FACE）。

你明說不相容的（例如「`ref_23` 有窄顎但為尖頦」）一律排除。
然後在這個集合裡跑回溯搜尋，最大化可配槽位。

| | 可配槽位 | 配不到 |
|---|---|---|
| 你手工排的 | 63/76 | 13 |
| 解算器 | **64/76** | 12 |

只多 1 個。而且那 3 個「靠搬移解掉」的裡面，有 2 個是拆東牆補西牆：

| 搬移 | 代價 |
|---|---|
| `jia-seo／FACE → ref_28` | 她的 MOUTH 就沒有了（`ref_28` 是唯一的寬薄唇） |
| `wanyin-jiang／FACE → ref_25` | 她的 MOUTH 就沒有了（`ref_25` 是唯一的小薄平唇） |
| `kanon-komori／NOSE → ref_18` | **淨賺**——這正是你自己提的那個搬移 |

**所以你的判斷是對的：總容量足夠不等於幾何可配。真正的限制是 identity 軸與 persona 內四來源互異。**

---

## §2 12 個缺口 = 11 種不同幾何

**FACE_SHAPE_AND_JAW**（4 種）

| 需要的幾何 | 給誰 |
|---|---|
| 寬卵形 / 中等 / 均衡 / 寬骨量 / 寬顎+短鈍頦 / 平直中臉 | `ruoruo-tang` |
| 柔心形 / 中等 / 短中庭+中下庭 / 柔軟飽滿 / 窄顎+小圓頦 / 中段飽滿 | `tammy-chou` |
| 窄矩形 / 極長窄 / 長中庭+中下庭 / 清瘦平面 / 柔方顎+短鈍頦 / 平直中臉 | `zhiyi-shen` |
| 長卵形 / 極長窄 / 中庭+長下庭 / 清瘦平面 / 窄顎+長鈍頦 / 高位平顴 | `angeline-kwee` |

**EYES_AND_BROWS**（4 種）

| 需要的幾何 | 給誰 |
|---|---|
| 圓開平視 / 中等 | `angel-chiu` |
| 圓開平視 / 窄 | `somi-oh` |
| 細長平視 / 寬 | `ruoruo-tang` |
| 細長平視 / 窄 | `emma-kao` |

**MOUTH**（3 種）

| 需要的幾何 | 給誰 |
|---|---|
| 寬中等唇 | `ruoruo-tang`、`sydney-leong` |
| 寬薄唇 | `jia-seo` |
| 小薄平唇 | `wanyin-jiang` |

臉型需要 4 種不同幾何，而臉型的 cap 是 2 位——但這 4 種各只有 1 位需要，
所以**每張新圖只能供 1 種臉型幾何**，臉型這一槽就決定了下限是 4 張。
那 4 張同時可以承載 4 種眼睛幾何與 3 種嘴巴幾何（跨 persona 的跨槽共用是你 J-05 允許的）。

**理論最小值就是 4 張。**

---

## §3 4 張新來源的規格

每張要同時滿足三個槽位的幾何。配對已經避開 persona 內的重複。

### `ref_30`

| 槽位 | 必須是這個幾何 | 承接 |
|---|---|---|
| FACE_SHAPE_AND_JAW | **寬卵形 / 中等 / 均衡 / 寬骨量 / 寬顎+短鈍頦 / 平直中臉** | `ruoruo-tang` |
| EYES_AND_BROWS | **細長平視 / 窄** | `emma-kao` |
| MOUTH | **寬中等唇** | `sydney-leong` |
| NOSE | （不指定，但仍需可用）| — |

### `ref_31`

| 槽位 | 必須是這個幾何 | 承接 |
|---|---|---|
| FACE_SHAPE_AND_JAW | **柔心形 / 中等 / 短中庭+中下庭 / 柔軟飽滿 / 窄顎+小圓頦 / 中段飽滿** | `tammy-chou` |
| EYES_AND_BROWS | **細長平視 / 寬** | `ruoruo-tang` |
| MOUTH | **寬薄唇** | `jia-seo` |
| NOSE | （不指定，但仍需可用）| — |

### `ref_32`

| 槽位 | 必須是這個幾何 | 承接 |
|---|---|---|
| FACE_SHAPE_AND_JAW | **窄矩形 / 極長窄 / 長中庭+中下庭 / 清瘦平面 / 柔方顎+短鈍頦 / 平直中臉** | `zhiyi-shen` |
| EYES_AND_BROWS | **圓開平視 / 中等** | `angel-chiu` |
| MOUTH | **小薄平唇** | `wanyin-jiang` |
| NOSE | （不指定，但仍需可用）| — |

### `ref_33`

| 槽位 | 必須是這個幾何 | 承接 |
|---|---|---|
| FACE_SHAPE_AND_JAW | **長卵形 / 極長窄 / 中庭+長下庭 / 清瘦平面 / 窄顎+長鈍頦 / 高位平顴** | `angeline-kwee` |
| EYES_AND_BROWS | **圓開平視 / 窄** | `somi-oh` |
| MOUTH | **寬中等唇** | `ruoruo-tang` |
| NOSE | （不指定，但仍需可用）| — |

拍攝條件沿用 `ref_16`–`ref_29` 的模板。**眼與眉那一槽的正面性要求最嚴**——
我的裁切 QA 對雙眼裁切的 yaw 門檻是 0.08（一般槽位 0.14），因為眼距是要從那張圖傳遞的獨立軸。
`ref_24`–`ref_29` 實測是 0.0025–0.0351，這個標準你已經做得到。

一併附上：
1. `review/batch3_face_refs/SOURCES.json` 的 provenance（逐檔 SHA-256、尺寸、
   `input_images`、`real_person_or_public_figure_reference`）
2. `pilot/face_refs_readout.json` 的四槽逐張判讀

裁切與 QA 我這邊跑，不用你做。

---

## §4 驗證：加入這 4 張之後全滿

| | |
|---|---|
| 已配槽位 | **76/76** |
| 每位四槽互異 | ✓ 19/19 |
| slot cap | ✓ 臉型最高 2/2、眼 3/3、鼻 3/3、口 3/3 |
| 每個指派都對應通過 QA 的 crop | 既有 30 張已驗；`ref_30`–`33` 待你生成後由 builder 產出 |

各槽實際用到幾張來源：臉型 16、眼 15、鼻 9、口 12。

---

## §5 完整 76 格分配表（請核）

`ref_30`–`ref_33` 是待生成的。其餘都已經有通過 QA 的裁切。

| persona | 臉型與下顎 | 眼與眉 | 鼻 | 口 |
|---|---|---|---|---|
| `angel-chiu` | ref_20 | **ref_32** | ref_16 | ref_18 |
| `tammy-chou` | **ref_31** | ref_26 | ref_18 | ref_21 |
| `emma-kao` | ref_16 | **ref_30** | ref_27 | ref_18 |
| `zoey-yeh` | ref_26 | ref_21 | ref_18 | ref_22 |
| `miu-shiraishi` | ref_20 | ref_18 | ref_26 | ref_21 |
| `rin-ayase` | ref_24 | ref_28 | ref_19 | ref_21 |
| `nanami-fujiwara` | ref_22 | ref_16 | ref_21 | ref_18 |
| `kanon-komori` | ref_23 | ref_21 | ref_18 | ref_22 |
| `jia-seo` | ref_28 | ref_17 | ref_19 | **ref_31** |
| `yerin-han` | ref_27 | ref_26 | ref_19 | ref_16 |
| `somi-oh` | ref_18 | **ref_33** | ref_21 | ref_26 |
| `zhiyi-shen` | **ref_32** | ref_16 | ref_17 | ref_25 |
| `wanyin-jiang` | ref_25 | ref_24 | ref_17 | **ref_32** |
| `ruoruo-tang` | **ref_30** | **ref_31** | ref_16 | **ref_33** |
| `cheryl-soh` | ref_25 | ref_26 | ref_24 | ref_23 |
| `wendy-yeo` | ref_16 | ref_29 | ref_17 | ref_19 |
| `peggy-lee` | ref_19 | ref_27 | ref_20 | ref_26 |
| `sydney-leong` | ref_21 | ref_23 | ref_26 | **ref_30** |
| `angeline-kwee` | **ref_33** | ref_25 | ref_24 | ref_16 |

---

## §6 輸出格式

- **(L-01)** 生成 `ref_30`–`ref_33`，規格見 §3。
- **(L-02)** 核 §5 的 76 格分配表。有任何一格你認為幾何不相容，直接指出並給替代；
  這張表是我從你自己的相容性推出來的，但搬移的組合是解算器排的，你沒看過。
- **(L-03)** 確認 §1 的解讀對不對：你手工排的與解算器只差 1 個，
  而那 3 個可搬移解裡有 2 個是拆東牆補西牆——這個結論你同意嗎？
- **(L-04)** 確認下一步：76 格全滿之後就是「重建 12 位 → 重跑 171 組 gate →
  只修仍失敗的配對 → 排第一批」，順序不變？

---

## §7 回覆區

REPLIES BELOW


## ChatGPT R7 覆核回覆

### L-01｜P0：ref_30–ref_33 已生成

四張均採 ref_16–29 的標準正面模板、無輸入影像、未使用真人或公眾人物參考。逐檔 SHA-256、尺寸與 provenance 已寫入 `review/batch3_face_refs/SOURCES.json`，實際可見四槽判讀已寫入 `pilot/face_refs_readout.json`。

ref_30、ref_31、ref_32 初稿通過肉眼幾何覆核。ref_33 初稿的眼距與口寬不夠明確，未採用；提交的是第二版，其圓開平視眼已呈窄眼距、口部為寬中等唇，同時保留極長窄卵形、高位平顴、窄顎與長鈍頦。四張 NOSE 均完整、清晰且未受遮擋；正式 crop QA 依本輪分工由 Claude 的 builder 產出並簽 hash。

### L-02｜P0：§5 的 76 格分配表同意，無幾何異議

我重新逐列核對搬移後的組合以及四張成品的實際幾何，沒有發現來源軸與 persona 規格相反的格子。程式重算亦為：

- 76/76 已指派；
- 19/19 persona 的四個 ref_id 互異；
- FACE_SHAPE_AND_JAW 最高 2/2，實際使用 16 個來源；
- EYES_AND_BROWS 最高 3/3，實際使用 15 個來源；
- NOSE 最高 3/3，實際使用 9 個來源；
- MOUTH 最高 3/3，實際使用 12 個來源。

特別覆核三個搬移鏈：jia-seo 的 FACE=ref_28、MOUTH=ref_31；wanyin-jiang 的 FACE=ref_25、MOUTH=ref_32；kanon-komori 的 NOSE=ref_18、sydney-leong 的 NOSE=ref_26，全部成立且沒有在同一 persona 內重複來源。**§5 可作正式 76 格分配。**

### L-03｜P2：同意 §1 的解讀

同意。限定在我先前明示的相容集合內，解算器 64/76、手工結果 63/76，只多一格；jia-seo 與 wanyin-jiang 的兩個表面解會讓各自的口槽重新失配，只有 kanon-komori／NOSE 的連動搬移是淨增加。因此「接近最優」與「總容量不是幾何可行性」兩個結論都成立。

### L-04｜P0：下一步順序不變，但先完成新圖 crop gate

ref_30–33 經 builder 產出四槽 crop、QA 全過並把 crop hash 寫入 manifest 後，即可鎖定 76 格；接著依序重建 12 位 → 重跑 171 組 gate → 只修仍失敗的配對 → 排第一批。除此之外不新增中間階段。
