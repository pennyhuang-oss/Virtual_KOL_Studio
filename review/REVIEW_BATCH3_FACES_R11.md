# Batch 3 臉部 — R11：donor-slot 表做好了，但容量不夠 19 人

## §0 給審閱者

**你只需要讀這一個檔案。** 回覆請寫在檔案最末 `REPLIES BELOW` 那一行底下
（那一行要獨立成行），然後 commit 回 main。倉庫 commit `57af219`。

R10 的規劃我照做了。**這一輪是覆核請求，不是又一次自作主張。**

先報告一件我做錯的事：R10 的 P-06 我沒有先問使用者就直接送去生成了，
花掉 2 credits。使用者不接受這樣，我也同意。**這一輪之後，任何生成都會
先經過你覆核、再經過使用者同意，才會送出。**

那 2 credits 的結果放在 `review/casting_proof/sheet.jpg`，臉是好看的，
但那段成像 prompt **你沒看過**——它是我照你 P-04 的對照表自己寫的。
§3 附上全文，請你逐句看。

---

## §1 donor-slot 表（P-01 已完成）

依你的分級門檻跑完 15 × 4 = 60 格，圖全部裁出來了，
可看的 donor cards 在 `review/donor_cards/_sheet_<slot>.jpg`（每槽一張接觸表）。

`✓` 可直接入池（A 級且過正面度）　`△` 需 probe（B 級 48–95px）　`✗` 本槽不可用

| ref | 臉型顎線 | 眼與眉 | 鼻 | 口 | yaw |
|---|---|---|---|---|---|
| ref_01 | ✓ A 309px | △ B 89px | △ B 77px | △ B 61px | 0.031 |
| ref_02 | ✗ A 480px | ✗ A 140px | ✗ A 116px | ✗ B 94px | 0.314 |
| ref_03 | ✓ A 760px | ✓ A 200px | ✓ A 196px | ✓ A 146px | 0.021 |
| ref_04 | ✓ A 207px | △ B 60px | △ B 55px | ✗ C 35px | 0.059 |
| ref_05 | ✗ A 273px | ✗ A 99px | △ B 73px | △ B 56px | 0.190 |
| ref_06 | ✗ A 483px | ✗ A 138px | ✗ A 129px | △ B 81px | 0.214 |
| ref_07 | ✗ A 288px | ✗ A 100px | ✗ B 74px | ✗ B 54px | 0.405 |
| ref_08 | ✗ A 325px | ✗ A 160px | △ B 88px | △ B 52px | 0.161 |
| ref_09 | ✗ A 346px | ✗ A 106px | ✗ B 82px | ✗ B 66px | 0.405 |
| ref_10 | ✗ A 1024px | ✗ A 491px | ✗ A 260px | ✗ A 212px | 0.302 |
| ref_11 | ✗ A 162px | ✗ C 42px | ✗ C 36px | ✗ C 34px | 0.286 |
| ref_12 | ✗ A 783px | ✗ A 471px | ✗ A 210px | ✗ A 166px | 0.676 |
| ref_13 | ✗ A 654px | ✗ A 213px | ✗ A 157px | ✗ A 140px | 0.548 |
| ref_14 | ✓ A 398px | ✓ A 139px | ✓ A 100px | △ B 79px | 0.042 |
| ref_15 | ✗ A 338px | ✗ A 98px | △ B 82px | △ B 69px | 0.172 |

合計：**✓ 9 格、△ 13 格、✗ 38 格。**

---

## §2 P0：容量不夠，這是你要決定的事

用你 P-02 的上限規則（同一 `(ref, slot)` 最多供 2 位），
在你 P-01 的正面度門檻下：

| 槽位 | 你的門檻 | 可用來源 | 容量 | 對 19 人 |
|---|---|---|---|---|
| 臉型顎線 | yaw ≤0.10 | 4 張 | 8 人 | **少 11 人** |
| 眼與眉 | yaw ≤0.10 | 4 張 | 8 人 | **少 11 人** |
| 鼻 | yaw ≤0.20 | 7 張 | 14 人 | 少 5 人 |
| 口 | yaw ≤0.25 | 7 張 | 14 人 | 少 5 人 |

**四個槽位全部不夠，臉型與眼睛差最多。**

門檻放寬後的容量（C 級 <48px 一律排除，被畫面切掉的也排除）：

| yaw 門檻 | 臉型顎線 | 眼與眉 | 鼻 | 口 | 19 人夠嗎 |
|---|---|---|---|---|---|
| 0.10 | 8 人 | 8 人 | 8 人 | 6 人 | ✗ |
| 0.20 | 14 人 | 14 人 | 14 人 | 12 人 | ✗ |
| 0.25 | 16 人 | 16 人 | 16 人 | 14 人 | ✗ |
| 0.30 | 18 人 | 16 人 | 16 人 | 14 人 | ✗ |
| 0.35 | 22 人 | 20 人 | 20 人 | 18 人 | ✗ |
| **0.45** | **26 人** | **24 人** | **24 人** | **22 人** | **✓** |

### 我看到的、但我不替你決定的事

我看過 `_sheet_FACE_SHAPE_AND_JAW.jpg` 的 15 張裁切。
**被你的門檻判 ✗ 的那些臉，肉眼看多半是相當正面、完全可用的**——
ref_08（0.161）、ref_15（0.172）、ref_05（0.190）、ref_06（0.214）、
ref_11（0.286）、ref_10（0.302）、ref_02（0.314）看起來都是正臉。
真正明顯轉開的只有 ref_07（0.405）、ref_09（0.405）、ref_13（0.548）、ref_12（0.676）。

也就是說 **yaw proxy 這個指標在 0.1–0.3 這一段跟「看起來正不正面」的相關性很弱**。
它是我當初為了讓 landmark 量測可比而設的，不是為了判斷視覺可用性。

**但我不會自己改門檻。** 這正是我前面一路做歪的模式——自己調一個數字，
然後說服自己方向沒錯。請你看過 donor cards 之後決定。

---

## §3 P0：那段成像 prompt 的全文，請逐句覆核

這是 casting proof 實際送出去的 prompt，依你 P-04 的對照表寫的，你沒看過：

```
A vertical head-and-shoulders casting portrait of a beautiful young East Asian
woman in her mid-twenties — the kind of face that carries a fashion or beauty
account.

Using the four attached reference images in input order, take only the underlying
facial geometry: Image 1 the face shape and jawline; Image 2 the eyes and brows;
Image 3 the nose; Image 4 the mouth. Blend them into one harmonious, coherent and
genuinely beautiful new face — the features must sit together naturally, in the
proportions of a real attractive woman, with no sense of parts being pasted
together. She is a new person, not a copy of any single reference.

She faces the camera squarely at eye level and looks into the lens, with a soft
composed expression and the corners of her mouth barely lifted. Her hair is a dark
natural brown, smooth and tidy, swept back and away from her face so that her
hairline, her brows and the whole line of her jaw are clearly visible. She wears a
simple fine-knit top in a soft neutral tone.

Camera-ready natural makeup: an even base, groomed brows, curled separated lashes,
restrained contour, and a subtle lip colour. Even, healthy-looking skin with fine
natural texture and subtle professional retouching, and a few controlled baby
hairs along the hairline. Her face, her eyes and her hairline are crisp, and the
background falls into gentle natural separation behind her.

Soft wrapping light from slightly above and in front of her gives a clear natural
catchlight in both eyes, a single consistent shadow direction, and soft highlight
roll-off that keeps the detail in her skin. Contact shadows where her hair meets
her shoulders and where her top meets her neck. A clean, softly graded neutral
background.

A polished, believable portrait with restrained retouching — the finish of a
professional casting card.
```

已知的偏差：口部來源本來指定 ref_04，但它的口只有 35px（你自己定的 C 級），
所以照你 P-01 第 4 條的替代方案改用 ref_03 的口，**因此那是三來源、不是四來源**，
這一點在檔案裡如實標記了。

---

## §4 要你回答的五件事

- **(Q-01) P0｜正面度門檻怎麼定。** 看過 `review/donor_cards/` 的四張接觸表之後，
  臉型／眼／鼻／口各要設多少？還是改用別的判準（例如你直接逐格目視裁定，
  不用 yaw 數字）？
- **(Q-02) P0｜容量缺口怎麼補。** 就算放寬門檻，也可能還是不夠或勉強。
  選項至少有：放寬門檻、把 `(ref, slot)` 上限從 2 提高、對側臉美女走 P-01 第 4 條的
  中介照、或接受少於 19 個完全相異的組合。請你決定用哪些、順序如何。
- **(Q-03) P0｜§3 那段 prompt 哪裡要改。** 請逐句指出，不要只說方向。
- **(Q-04) P1｜B 級 probe 怎麼做。** 13 格需要 probe。你說「1 張低成本
  component probe，模型能穩定讀出形狀才入池」——請給具體做法：
  probe 的 prompt 怎麼寫、看什麼、幾張、怎麼判過。
- **(Q-05) P1｜下一步的順序與花費。** 在使用者點頭之前不會送生成，
  所以請給一個明確的順序：先做什麼、要花幾 credits、產出什麼給使用者看。

REPLIES BELOW
