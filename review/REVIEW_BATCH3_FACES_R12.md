# Batch 3 臉部 — R12：76 格草案排好了，但你的 Q-02 容量結論不成立

## §0 給審閱者

**你只需要讀這一個檔案。** 回覆寫在檔案最末 `REPLIES BELOW` 那一行底下
（那一行要獨立成行），commit 回 main。倉庫 commit `60e4f64`。

R11 我照做了，Q-05 第 1 步（0 credits 的 76 格草案）完成。過程中發現**你的
Q-02 有一個算漏的地方，結論因此不成立**，需要你裁決。

**這一輪沒有花任何 credits，也沒有送出任何生成。**

---

## §1 P0：Q-02 的容量結論不成立，現有規則排不滿 76 格

你 Q-02 逐槽檢查容量（臉型 22、眼 20、鼻 20、口 20），結論是「現有 15 張足夠」。
逐槽確實都夠，但**漏了 P-02 的另一條全域上限：同一 ref 跨四槽合計最多供 6 次。**

每張的最大供給是 `min(6, 2 × 可服務槽位數)`：

| ref | 可服務槽位 | 最大供給 |
|---|---|---|
| ref_01、02、03、05、06、08、10、14、15 | 四槽 | 6 |
| ref_04 | 臉、眼、鼻 | 6 |
| ref_07 | 臉、眼、口 | 6 |
| ref_09 | 臉、眼 | **4** |
| ref_11 | 臉 | **2** |
| ref_13 | 口 | **2** |
| ref_12 | 你四槽全排除 | **0** |

**總供給 74，需求 76，差 2 格。** 我用回溯解算器確認過：在現行規則下無解，不是排法問題。

### 最小放寬的實測結果

| 方案 | 總供給 | 解算結果 |
|---|---|---|
| 現行（ref ≤6、各槽 ≤2） | 74 | ✗ 供給不足 |
| **A. ref 跨槽上限 6 → 7** | **83** | **✓ 可解，需驗證 40 格** |
| B. 只把鼻／口的 (ref,slot) 上限 2→3（你 Q-02 第 3 步） | 78 | 超過搜尋預算，未確認 |
| C. 四槽 (ref,slot) 上限全部 2→3 | 78 | ✓ 可解，需驗證 40 格 |

**我用方案 A 排了草案**，理由是它完全不動你想保留的「臉型／眼眉每格最多 2 位」——
你說那兩槽對身份辨識影響最大。**但這是待批准的假設，不是我的決定。**

---

## §2 P0：你的 Q-01 裁定與自己的 C 級規則衝突一處

你把 **ref_11 / 眼與眉**列為「條件式」，但它的眼部裁切在原圖上只有 **42px**，
是你自己定義的 C 級（<48px），而你也寫了「C 級仍排除」。

我依你自己的規則把它移除了。如果你認為該保留，請說明怎麼處理 42px 的問題。

---

## §3 76 格分配草案（方案 A，待批准）

`(條件)` = 你 Q-01 列為條件式　`(B)` = 解析度 B 級 48–95px　兩者都要走 Q-04 的 production probe

| persona | 臉型顎線 | 眼與眉 | 鼻 | 口 |
|---|---|---|---|---|
| angel-chiu | ref_11 | ref_05 | ref_03 | ref_07 (54px B) |
| angeline-kwee | ref_04 | ref_15 | ref_06 | ref_03 |
| cheryl-soh | ref_08 | ref_06 | ref_14 | ref_03 |
| emma-kao | ref_10 | ref_14 | ref_03 | ref_13 (140px A) |
| jia-seo | ref_01 | ref_03 | ref_06 | ref_10 (212px A) |
| kanon-komori | ref_02 | ref_05 | ref_14 | ref_01 (61px B) |
| miu-shiraishi | ref_05 | ref_15 | ref_01 (77px B) | ref_02 (94px B) |
| nanami-fujiwara | ref_15 | ref_03 | ref_04 (55px B) | ref_06 (81px B) |
| peggy-lee | ref_03 | ref_06 | ref_05 (73px B) | ref_14 (79px B) |
| rin-ayase | ref_06 | ref_14 | ref_15 (82px B) | ref_05 (56px B) |
| ruoruo-tang | ref_14 | ref_09 (106px A) | ref_02 (116px A) | ref_15 (69px B) |
| somi-oh | ref_10 | ref_04 (60px B) | ref_08 (88px B) | ref_07 (54px B) |
| sydney-leong | ref_11 | ref_07 (100px A) | ref_10 (260px A) | ref_08 (52px B) |
| tammy-chou | ref_04 | ref_08 (160px A) | ref_01 (77px B) | ref_13 (140px A) |
| wanyin-jiang | ref_08 | ref_01 (89px B) | ref_04 (55px B) | ref_10 (212px A) |
| wendy-yeo | ref_15 | ref_10 (491px A) | ref_05 (73px B) | ref_01 (61px B) |
| yerin-han | ref_01 | ref_09 (106px A) | ref_15 (82px B) | ref_02 (94px B) |
| zhiyi-shen | ref_05 | ref_04 (60px B) | ref_02 (116px A) | ref_06 (81px B) |
| zoey-yeh | ref_09 (346px A) | ref_02 (140px A) | ref_08 (88px B) | ref_14 (79px B) |

**每張的使用次數**：ref_01=7、ref_02=6、ref_03=7、ref_04=6、ref_05=7、ref_06=7、ref_07=3、ref_08=6、ref_09=3、ref_10=6、ref_11=2、ref_12=0、ref_13=2、ref_14=7、ref_15=7

**完全沒用到**：ref_12（你 Q-01 把它四槽全排除）

---

## §4 P0：需驗證的格數是 40／76，超過一半

草案裡有 **40 格**是條件式或 B 級，都要走你 Q-04 的 production probe。
你 Q-04 的設計是「B crop 混進正式候選，同一對 A/B 同時當 probe」，不額外花錢——
但 40 格分散在 19 位身上，代表**幾乎每一位的候選裡都帶著待驗證的部件**。

如果某位的兩張候選裡有兩三個待驗證部件同時失敗，會分不清是哪一個的問題。
請你決定：是接受這個密度、還是要先把某些格子換成免驗證的組合（會讓使用次數更不平均）。

---

## §5 P1：pilot 用哪一位

草案裡**四槽全部免驗證**的只有兩位：

| persona | 臉型顎線 | 眼與眉 | 鼻 | 口 | 年齡／族裔 |
|---|---|---|---|---|---|
| angeline-kwee | ref_04 | ref_15 | ref_06 | ref_03 | 23 歲／印尼華裔 |
| cheryl-soh | ref_08 | ref_06 | ref_14 | ref_03 | 25 歲／新加坡華裔 |

用這兩位之一做 Q-05 的 2-credit pilot，可以把「prompt 對不對」跟「B crop 傳不傳形」
分開測。**我建議 cheryl-soh**，因為她四槽的部件像素都是 A 級最高的一批
（325／138／100／146px）。請你確認或改指定。

---

## §6 Q-03 的 prompt，變數已展開（以 cheryl-soh 為例）

依你 Q-03 的十段修正逐段改寫，四個變數展開成實際值：

```
A vertical head-and-shoulders beauty-casting portrait of one 25-year-old
Chinese-Singaporean woman, created as the identity master for cheryl-soh.

Build one original, coherent identity from the four attached isolated component
crops in input order. Image 1 defines the face silhouette, jawline and chin.
Image 2 defines the eyes, eyelids and brows. Image 3 defines the nose bridge, tip
and alar shape. Image 4 defines the mouth width, lip contour and upper-to-lower
lip balance. Integrate the four regions with continuous anatomy, aligned facial
midlines, natural transitions and one consistent age.

She faces forward at eye level and looks directly into the lens. Her expression is
calm and composed, with relaxed closed lips.

Her long black hair is neatly styled away from the central face, with the
hairline, both brows, both cheek edges and the full jawline visible.

She wears a simple fine-knit top in a soft neutral tone.

Camera-ready natural makeup: an even lightweight base, softly groomed brows that
preserve their source shape, curled separated lashes, and subtle lip colour that
preserves the source lip contour.

Even, healthy-looking skin with fine natural texture and subtle professional
retouching. The face, eyes, brows and hairline are cleanly resolved, while the
background falls into gentle natural separation.

Soft wrapping light from slightly above and in front shapes the face evenly,
creates a small natural catchlight in both eyes, and preserves detail through
smooth highlight roll-off and gentle facial shadows.

A clean, softly graded neutral background.

A polished, believable beauty-casting portrait suitable for a premium
social-media KOL profile.
```

`HAIR_COLOR` 我用她 profile 裡的「現階段是黑色長髮」展開成 `long black`。

---

## §7 要你回答的四件事

- **(S-01) P0｜§1 的容量缺口怎麼補。** 批准方案 A、改用 B 或 C、
  或用別的方式（例如把 ref_12 救回某一槽、或對 ref_09／11／13 做中介照）？
- **(S-02) P0｜§2 的 ref_11／眼與眉衝突怎麼處理。**
- **(S-03) P0｜§3 的 76 格草案有沒有哪一格你認為不該這樣配。**
  這張表是解算器在你的裁定表內排的，你沒看過。
- **(S-04) P1｜§4 的 40 格待驗證密度可否接受；§5 的 pilot 人選；
  §6 的 prompt 還有沒有要改的。**

三者都確認後，我會把 §6 的 prompt 與 pilot 人選一起交使用者，
**取得他明確同意才送出那 2 credits**。

REPLIES BELOW
