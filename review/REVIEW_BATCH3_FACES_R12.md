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
## ChatGPT R12 覆核回覆

### S-01｜P0｜批准方案 A：跨槽總上限 6 → 7；其餘身份防撞規則不動

§1 的反例成立。R11 只逐槽相加，漏算同一 ref 跨四槽合計最多 6 次的全域限制；在 ref_12=0、ref_11=2、ref_13=2、ref_09=4 的情況下，總容量只有 74，原本「現有規則足夠」的結論撤回。

批准方案 A，理由是：

1. 「每個 (ref, slot) 最多供 2 位」比「同一 ref 跨槽總計 6 次」更直接控制身份重複。方案 A 不增加任何一個具體五官被複製的次數。
2. 方案 B／C 會讓同一個鼻或口直接供 3 位；即使鼻口辨識權重較低，也比讓同一 ref 在不同槽位多出 1 次更容易形成可見重複。
3. §3 草案仍符合：每人四個不同 ref、每個 (ref, slot) ≤2、任兩位最多共用一個相同 (ref, slot)，且沒有重複的臉型＋眼眉組合。
4. ref_12 四槽都不適合作直接 donor；為了補 2 格特地做中介照，比把一條啟發式總上限由 6 調到 7 更昂貴，也引入新的生成誤差。

但方案 A 的批准範圍只到 **總上限 7**，不是取消總上限。ref_01、03、05、06、14、15 各 7 次可接受；任何 ref 不得升到 8。後續若重排，仍須同時滿足每槽≤2、每人四來源、pairwise overlap≤1。

### S-02｜P0｜ref_11／眼與眉排除；不以放大或 prompt 補救

同意 Claude 的處置。ref_11 眼部原始短邊 42px，屬 C 級；我在 R11 把它列為條件式是自相矛盾，該格應從 donor pool 移除。

4K 放大只增加輸入尺寸，不會恢復原圖不存在的眼皮、眼角與眉毛細節；把它送入 production probe 只是在測模型如何猜。除非未來另經使用者批准生成中介照，否則 ref_11 只能供臉型顎線，不能供眼眉。

### S-03｜P0｜76 格沒有非法來源，但草案不可原樣進生成，需按「待驗證密度」重排

我逐列核對 §3：

- 76 格全部落在 R11 裁定的可用或條件式集合內，沒有使用 ref_12，也沒有使用 ref_11／眼眉。
- 19 位每列都是四個不同 ref。
- 每個 (ref, slot) 使用 1–2 次，沒有超過 2。
- 每個 ref 總使用 2–7 次，符合本輪批准的方案 A。
- 任兩位最多只共用一個相同 (ref, slot)，沒有重複高辨識的臉型＋眼眉組合。

因此沒有哪一格因「來源不准供該槽」而必須單獨刪除。但草案把技術風險排得過密，以下列不能照現狀進早期生成：

- ruoruo-tang：眼、鼻、口三格待驗證；
- somi-oh：眼、鼻、口三格待驗證；
- sydney-leong：眼、鼻、口三格待驗證；
- tammy-chou：眼、鼻、口三格待驗證；
- wanyin-jiang：眼、鼻、口三格待驗證；
- wendy-yeo：眼、鼻、口三格待驗證；
- yerin-han：眼、鼻、口三格待驗證；
- zhiyi-shen：眼、鼻、口三格待驗證；
- zoey-yeh：四格全是條件式或 B。

這不是部件配錯，而是實驗設計不具可歸因性。請解算器保留方案 A 與所有身份防撞規則，增加下列目標：

1. pilot 必須 0 個待驗證格；
2. pilot 後的 calibration wave，每位最多 1 個待驗證格；
3. 待某個 (ref, slot) 通過 production probe 後，該格在後續人物中改記為 validated，不再占待驗證額度；
4. 正式批次每位最多 2 個尚未 validated 的格，禁止 3 或 4 格同時未知；
5. 若「全表靜態計算每位≤2」無解，允許依生成順序動態解鎖；不得為了靜態排表重新放寬來源規則。

另外，R12 沒有列 19 位的 11 條骨相軸與 15 張部件的語意標籤，因此我能確認的是來源合法性、容量與防撞結構，不能誠實宣稱每個 ref 都是該 persona 的最佳美感／骨相配對。交使用者前，草案還需附每格的一句相容理由；不能只因解算器可解就視為美感配對完成。

### S-04｜P1｜40/76 的「未知」定義需修正；批准 cheryl-soh pilot，prompt 再改三處

#### 1. 不接受 40/76 同時作未知，但 B 級不再自動等於待驗證失敗源

40 格密度不可直接接受，使用者指出的因果混淆成立。同時，我也修正 R11 Q-04：原始 crop 短邊 48–95px 只是風險標籤，不應在看過 4K donor card 後仍自動等同「模型讀不到」。

四張 cards 中，13 個原 △ B 格的指定形狀都可肉眼辨識。它們保留 B 標籤與兩個預登記簽名，但不再僅因像素數被算成獨立未知；真正需要 production probe 的是：

- R11 表中標為「條件式」的角度／透視格；
- 表情已改變口形的格；
- card 上部件邊界或形狀仍模糊、無法預先寫出兩個簽名的 B 格。

Claude 應逐格寫出兩個簽名；寫不出來的才維持 provisional。能清楚寫出、兩位審閱者都在 card 上看得到的 B 格可標為 usable-B，第一次生成仍記錄傳遞結果，但不占「同一人最多 1 個未知」的額度。

這樣不是假定 B 一定成功，而是把所有 crop 都應有的生成後觀察，與真正需要單變量驗證的風險格分開。

#### 2. pilot 人選批准 cheryl-soh

批准 cheryl-soh，不改成 angeline-kwee。她四槽 ref_08／06／14／03 均為 A 級，像素 325／138／100／146，可把第一個 2-credit 實驗集中在 prompt、四槽融合與美感，不混入解析度問題。

這項批准只是把「人選＋prompt」交給使用者決定，**不是生成授權**。只有使用者明確同意後才能花 2 credits。

#### 3. §6 prompt 尚需三處修改

其餘段落符合 R11 裁決，但以下三處要改：

**首句**

`one 25-year-old Chinese-Singaporean woman` 不自然，且 `created as the identity master for cheryl-soh` 是內部 metadata，對畫面沒有幫助，可能誘發文字／casting-card 排版。

改為：

> A vertical head-and-shoulders beauty-casting portrait of a beautiful 25-year-old Singaporean Chinese woman.

persona ID 留在 job metadata，不送進圖像 prompt。

**四槽融合段末句**

`one consistent age` 語意不自然，改成正向的年齡一致性：

> Integrate the four regions with continuous anatomy, aligned facial midlines, natural transitions, and facial maturity appropriate for a 25-year-old woman.

**妝容段**

`softly groomed brows that preserve their source shape` 與 `subtle lip colour that preserves the source lip contour` 是必要的正向約束，可保留；但第一次 pilot 應把完整四個實際輸入檔名與順序列在 job manifest，不只依賴「input order」，避免掛圖順序錯一格就整張作廢。

其餘句子不改。`long black hair` 正確展開 profile；閉唇中性表情、無 contour、包覆光、乾淨背景與 KOL 完成度均可保留。

#### 4. 下一步

1. 0 credits：依上述分類把 B 與真正 provisional 拆開，重跑分配，使 pilot=0 未知、calibration wave 每位≤1 未知、後續每位≤2 未驗證格；補上每格相容理由與 job manifest 的四張輸入順序。
2. ChatGPT 再覆核重排表與最終 prompt。
3. 只把 cheryl-soh 的 donor sheet、完整 prompt、2-credit A/B 計畫交使用者。
4. 使用者明確回答同意後才生成；沒有同意就停在 0 credits。

本輪放行的是方案 A、ref_11／眼眉排除、cheryl-soh 作候選 pilot 與 prompt 修訂方向；**尚未放行生成，也尚未批准 §3 原草案直接作為 19 人正式執行表。**

