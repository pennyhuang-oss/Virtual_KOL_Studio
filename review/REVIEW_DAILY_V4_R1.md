# 複核請求 daily_v4 R1 — 這 80 格「量身定做」是真的量身定做，還是同一個骨架複製了 16 次？

**日期**：2026-09-11
**送出者**：Claude Code
**分支**：`claude/20-female-personas-planning-i20mo1`
**狀態**：80 格 prompt 已建好、audit 全過、尚未送生成。成本 80 × 0.12 = **9.6 credits**。
**我在花這 9.6 credits 之前，自己稽核了一次產出，發現五個數字不太對。這份就是拿那五個數字來問你。**

---

## 零、你必須直接當前提、不要重新討論的事

使用者原話：「這個專案是我在做，所以還是要以我的決策為主。」

| # | 已定案 | 出處 |
|---|---|---|
| U1 | **已經生成過的場景一律作廢**，不再重新審一次 | 2026-09-10 裁決 |
| U2 | **工作場域每位最多 1 格**（5 格中），其餘要是私下生活 | 「網美經營社群不會放自己工作那麼多素材」 |
| U3 | **要逐人設量身定做**，不要共用大池＋不重複約束 | 「為什麼不能做個別人設都是量身定做的規劃」 |
| U4 | **日夜各半** | 「為什麼夜間的占比這麼大？我覺得要各半吧」 |
| U5 | **有路人的格數不用多，但不是要取消路人** | 「有路人的，沒有那麼多沒關係」 |
| U6 | **尺度（露出程度）一律由使用者決定**，不要評論尺度 | 2026-09-09 裁決 |
| U7 | **美貌是第一驗收條件** | 長期 |

還有一條 v2 時期經使用者拍板、盲測過的規則，**跟這次的產出直接衝突**，見下面 §2-5：

> **D3｜膚質寫「均勻膚色＋修飾＋光澤＋眼神光」，不寫「紋理」。**
> 理由：「紋理」在素顏調性的 Soul 上會被讀成斑點。

---

## 一、v4 改了什麼

前兩版（v2 100 格、v3）的根本錯誤，是 `grep` 證實的：**`plan/daily_v2/*.py` 與 `plan/daily_v3/*.py` 對
`character.md` / `content_style.md` 的引用次數是 0。** 每一格都從全域共用池抽，再加不重複約束。
使用者的判語是：「都是一樣的動作、一樣的表情和類似的場景。」

v4 的三項結構性改動：

1. **每一個欄位都要有出處。** spec 的每一格都帶 `action_src` / `outfit_src` / `light_src` / `face_src`，
   指回那位人設自己 `character.md` 的哪一欄（色盤／氛圍／後製／語氣／小習慣／標誌性配額／身分背景）。
2. **全域 GLOW 句廢除，改成 16 句各自的膚質／影調句**（`skin.json`），翻自各自的「後製」欄。
3. **場域配額變硬規則**：工作場域 ≤1 格、她自己的空間 ≥3 格、標誌性配額 ≤1 格；
   80 個場域跨全批零重複，且與 v2 那 100 格零重疊。

`validate_v4.py` 全過：16 位 · 80 格 · 場域 80 個零重複。
`build_v4.py` 全過：80 格、平均 285 字、鏡位 near 17 / selfie 17 / knee 19 / floor 14 / full 13。

**問題是：稽核全過，不代表它不同質。以下是我自己數出來的。**

---

## 二、我在送生成之前，自己稽核產出數出來的五個數字

### 2-1　16/16 位都有一格浴室，13/16 位還在同一個順位

| | |
|---|---|
| 有浴室格的人設 | **16 / 16** |
| 浴室落在第 3 格 | **13 / 16**（其餘落第 2、第 4） |
| 其中是「剛洗完澡／水氣／霧鏡」 | **9 格** |

實際的句子長這樣（不同人設）：

- `A2` 她租屋處的浴室，剛洗完澡，鏡子上還有水氣
- `J3` 她家的浴室，剛練完澡，鏡子有水氣
- `M3` 公寓那間很小的浴室，剛洗完澡
- `S3` 她的浴室，剛洗完澡，鏡子有水氣
- `Z3` 她公寓的浴室，玻璃隔間起霧，鏡子只擦出一塊

**這正是使用者當初否決 v2 的那句話**：「單看一個人設可能覺得還好，但如果一次看很多人設，
就會發現他們全部都是一樣的動作、一樣的表情和類似的場景。」

### 2-2　打光句型高度收斂

| 句型 | 命中 |
|---|---|
| 「一盞燈在她（正／側）前方」 | **49 / 80** |
| 「房間／浴室其餘部分暗、深處落暗」 | **37 / 80** |
| 兩句同時出現 | **20 / 80** |

我在 v4 的 README 裡**正式撤回了全域暗背景規則**，理由是它是 20 位人設平均出來的假象。
結果逐人設重寫之後，**它又自己長回來了。**

### 2-3　0 / 80 格有路人

使用者的原始抱怨不是「不要路人」，是「路人穿著跟場景不合、靠太近、私密場所不該有路人」（U5）。
而且競品 小雪莉 帳號的街景素材，正是靠路人才讀起來像真的。
**我把它修成了 80 格全部沒有任何人。** 13 格全身照全部是「打烊後／入夜／雨後的空街」。

### 2-4　日夜沒有各半（U4 沒有被執行）

v3 時代有一條硬配額驅動場景選擇。**v4 把全域燈光規則拿掉的時候，日夜配額跟著被拿掉了，
而且沒有任何一份文件記錄這個取捨。**
用中文光線欄位分類：明確夜 26 / 明確日 18 / 其餘 36 格是「室內一盞燈、其餘落暗」——
這 36 格在成像上會讀成暗場。實際比例大約是 **6 : 2**，不是 U4 要的 1 : 1。

### 2-5　16 句膚質裡，有 7 句直接違反已拍板的 D3

D3 說：不要寫「紋理」，Soul 會讀成斑點。v4 的 skin 句卻是從 character.md 的「後製」欄翻過來的，
於是出現：

- `angel-chiu`：*Real skin texture, not smoothed: pores, a little unevenness and the tiredness around her eyes are all left in…*
- `zoey-yeh`：*…her skin left completely unretouched — no smoothing and no evening out of tone.*
- `ruoruo-tang`：*…low contrast with real skin texture…*

共 **7 / 16** 位命中（angel-chiu、emma-kao、wanyin-jiang、somi-oh、ruoruo-tang、sydney-leong、zoey-yeh）。
**這是 v4 用 character.md 覆蓋掉了一條經盲測、經使用者拍板的規則，而且沒有人決定過要覆蓋。**

---

## 三、prompt 長什麼樣（完整一格，`A1` angel-chiu）

```
A photograph of a beautiful adult East Asian woman in her twenties, from the waist up.
Her hair is dark brown with honey-tea gold lightened ends, just let down out of a tight tie, the lightened honey-tea ends showing.
She is slim with a soft, full curve at the bust that clearly shapes whatever she wears, above a narrow waist.
She wears a nude-pink silk nightdress with one strap down on her arm.
She is sitting on the edge of the bed in her rented room after a night shift, the curtains still drawn against the morning.
She has just taken her hair down and one hand is still up behind her head.
The tiredness of a finished night shift is not hidden; she is looking at the lens without smiling.
One warm lamp at the bedside is in front of her and the rest of the room is dark, the grain left in the picture.
Real skin texture, not smoothed: pores, a little unevenness and the tiredness around her eyes are all left in, and the warm light keeps its grain and its shadows.
Shot from about a metre and a half away at her own eye level, a short portrait lens, the background falling into soft blur behind her.
Every wall, panel and screen behind her carries only plain surfaces and printed text — notices, labels and signage lettering — and no framed pictures, posters or displays of any kind hang on them.
She is the only person in the photograph; no other people are visible anywhere in the frame.
Everything in this picture is accounted for: the only person in it is her, and every visible hand connects to one of her own arms.
```

組裝順序固定：身分 → 髮 → 體態 → 服裝 → 場域 → 動作 → 表情 → 光 → **膚質（16 句之一）** →
鏡位 → 鏡面守則（僅在場景含反射面時插入） → 牆面守則 → 路人 → 收束句。

**最後四句是每一格都一樣的固定守則，合計約 60 字，占 285 字的 21%。**
它們是為了修掉已驗證的三個缺陷：背景牆上長出人設的臉（v1 12/138）、對鏡自拍手機螢幕顯示人設的臉、
憑空多出第三隻手。

---

## 四、請你複核的六件事

**Q1（最重要）**　拿 §2-1 到 §2-4 的數字看，v4 的同質性到底有沒有比 v2 低？
還是我只是把樣板從「共用池」搬到了「同一套 5 格骨架複製 16 次」（臥室／浴室／她的工作場域／
另一個私人空間／一格夜間外出）？如果是後者，**真正的修法是什麼**——
是把 5 格骨架拆掉、讓每位人設的格位結構本身就不一樣，還是別的？

**Q2**　0/80 路人是不是矯枉過正？依 U5 與競品分析，合理的路人格數區間是多少、應該落在哪一類場域？
（注意：v1 已驗證「背景人臉會被 Soul 拉成人設本人」是真缺陷，所以路人不是零成本的。）

**Q3**　§2-2 的打光收斂——我逐人設重寫之後它又長回來了。
這是「這些人設的 character.md 真的都寫著暗場」的證據，還是「我是同一隻手寫的 16 份 spec」的證據？
你能從我給的句型分布分辨嗎？分辨不了的話，要用什麼方法分辨？

**Q4**　§2-5 的 D3 衝突怎麼解？三個選項：
(a) D3 優先，把 7 句「真實膚質」改寫成 D3 的寫法，犧牲 character.md 的個性；
(b) character.md 優先，D3 降級為「預設值，人設檔另有規定時以人設檔為準」；
(c) 先拿 2 位（angel-chiu、zoey-yeh）各 2 格做 A/B（0.48 credits），用結果決定。
**這題最後由使用者裁決，我要的是你的推薦與理由。**

**Q5**　§3 的四句固定守則占每格 21% 的字數。它們稀釋主體描述的風險，跟它們修掉的缺陷相比，划算嗎？
有沒有更短的寫法能守住同樣三個缺陷？

**Q6**　該一次拍 80 格，還是先拍 16 格（每位 1 格）當探針？
使用者已經核准「80 格全拍」，理由是「整組風格才會一致」。
如果你認為應該先探針，請明確說出**探針能提早發現、而 80 格全拍會讓我多燒多少 credits** 的那個具體缺陷是什麼；
講不出具體缺陷就不要建議探針。

---

## 五、你可以直接讀的檔案（同一個 repo、同一個分支）

| 路徑 | 內容 |
|---|---|
| `plan/daily_v4/README.md` | v3 為何作廢、全域暗背景規則的撤回、場域配額硬規則 |
| `plan/daily_v4/specs/*.json` | 16 份中文規劃稿，每格帶四個 `_src` 出處欄 |
| `plan/daily_v4/skin.json` | 16 句膚質／影調句 |
| `plan/daily_v4/build_v4.py` | 英文 prompt 組裝器與 audit 規則 |
| `plan/daily_v4/prompts_v4.json` | 80 格成品 |
| `plan/daily_v4/validate_v4.py` | 場域配額稽核 |
| `PERSONA_CANON.md` | 治理憲章，原則二是 25% 上限那條 |
| `review/soul_pilot/FINDING_pose_module.md` | v1 140 張的姿勢同質性量化 |
| `review/soul_pilot/FINDING_scene_plausibility.md` | 路人／場景合理性的三個結構性錯誤 |

---

## 六、回覆方式

**請把你的回覆 commit 回這個 repo 的 `review/REVIEW_DAILY_V4_R1_GPT.md`，分支 `claude/20-female-personas-planning-i20mo1`。**
格式：第一行先用一句話講你對 **Q1** 的結論（這是最重要的一題），然後 Q1–Q6 依序回答。
不確定的地方請直接寫「我看不出來」，不要補平。
