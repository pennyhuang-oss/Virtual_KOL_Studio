# 【覆核請求】批次一 — 依你的判定改完，請確認改法

> ## ⛔ 讀取範圍限制（很重要，請先讀這段）
>
> **只讀這一個檔案，不要讀 repo 裡的任何其他檔案，也不要瀏覽目錄。**
> 你判斷所需的一切都已經內嵌在下面，包括改前／改後全文與背景速查。
> 上一次你把整個專案背景讀進來，一次就耗掉使用者方案內 5 小時的用量——
> 你只做檢核、不做規劃也不執行，用量不該比執行方還高。
>
> ## ✍️ 回覆方式
>
> **直接編輯這個檔案**，把答案寫進最後面的「ChatGPT 回覆區」，然後 commit 到
> 分支 `claude/virtual-kol-restaurant-campaign-pxu9m4`。
> **不要改本檔其他任何段落**、不要開新檔、不要改別的檔案、不要推 main。
> commit message 寫 `覆核回覆：<日期>` 即可。

---

## 0｜最小背景（每次都附，方便你不用回想）

- 模型：Higgsfield Soul 2.0（`soul_2`）＋ 已訓練的 `soul_id`。**沒有 negative prompt 欄位、沒有 seed。**
- 每段 prompt 生一張，`2k`、`9:16`，一張 0.12 credits。
- 兩個角色：**Yuna**（韓籍長髮）、**Luna**（日籍及下巴鮑伯）。兩人設定都住台北。
- 已花錢驗證、不必再討論的結論：
  不寫族裔與身材數字｜相機用相對描述（`camera at her navel level, lens horizontal, shot from well back`）｜
  否定句完全無效｜`background exposed the same brightness as her skin` 可解逆光（baseline wording，非萬用公式）｜
  表情要綁實體動作｜沒寫髮長會長短不一，造型（馬尾／髮夾）不算長度｜
  鮑伯寫剪裁不寫視覺對稱｜`soul_id` 會鎖整套場景構圖模板｜靜態圖不能塞兩個時間點｜
  **眼睛控制屬低可靠，不是做不到**（有 1 次 wink 成功反例）。
- 現況：21 件規格，4 張 preflight 跑完，2 張硬淘汰（雨傘浮空、花瓣消失）。**正式批次未放行。**

---

## 1｜這次改了什麼

依你上一輪對 #3 #4 #5 #7 #11 的判定全部執行。**#1 待 A/B、#2 維持 PARKED、#6 送回人類裁決。**

### 1-1 LG-04（花季・半身）— 花瓣改握法 ＋ 服裝改寫

**改前**
```
A young woman holds one open palm in front of her with a blossom petal resting in it, eyes widened and mouth softly open in surprise, eyebrows raised. ... White square-neck fitted lace top, pale pink checked mini skirt, a cream cardigan over her shoulders, pearl earrings. ...
```

**改後（完整）**
```
A young woman pinches a single pink blossom petal between her thumb and index finger beside her cheek, mouth softly open in surprise, eyebrows raised. Half body, camera level with her chest, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, a cream ribbon headband. An opaque white cotton blouse with a structured square neckline, short puff sleeves and a fitted waist, pale pink checked mini skirt, pearl earrings. Park path under blossoming branches hanging into the top of the frame, petals on her shoulder. Soft daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### 1-2 LG-05（公車站・3/4 身）— 傘的握法、外套、服裝、字數

**改前**
```
A young woman stands at the edge of a bus shelter holding a folded clear umbrella still dripping, tilting her head and making a V sign beside her cheek, eyes crinkled. ... An off-white fitted shirt with the top buttons open, pale blue checked skirt, a pale blue cardigan over her shoulders. ...
```

**改後（完整）**
```
A young woman stands at a bus shelter, her left hand wrapped around the curved handle of a folded clear umbrella hanging straight down beside her thigh, her right hand making a V sign beside her cheek, head tilted. Three-quarter body, camera at her navel level, lens horizontal, shot from well back. A blunt chin-length black bob with even blunt ends along the jawline. An opaque off-white cotton short-sleeve button-front blouse, fastened through the chest, both cuffs visible, pale blue checked skirt. A bus shelter with a colourful route map lightbox, wet asphalt reflecting the glow of shop signs across the street. Her face clearly lit, the signs keeping their colour. Natural skin texture, subtle film grain.
```

### 1-3 眼部形容詞去重（#4）

刪掉同句重複堆疊的眼部字，不整批刪除：
- LG-10A：`holding a candy apple beside her cheek, laughing with her eyes crinkled` → **`..., laughing`**
- LG-07：`her eyes peeking over the rim toward the camera with a playful smile` → **`..., smiling`**
- 驗收改以嘴型、頭部方向、可見動作為準；眼睛列 soft observation，不當放行門檻
- 已結案的 D-06 結論更正為「眼睛控制低可靠、已有 1 次成功反例」，原紀錄保留不刪

### 1-4 其他（#5、#11）

- 鮑伯**維持兩種 wording 不統一**；檢查腳本裡「驗過之後收斂成一種」的註解已刪，措辭改成「與成功結果共現」，不寫成已證明的因果控制桿
- 件數／成本／核准編號三處不一致已修：**21 件、≈2.52 credits、重生 buffer 取整為 11 張 ≈1.32**，核准編號補上 `LG-10A`／`LG-10B`
- 機械檢查 21 件全過（字數 86–120、無否定句、髮長皆為真長度詞、pores 只在 4 件近景、無時間序列詞）

---

## 2｜請你判斷（只要回答這四題）

1. **LG-04 改後的花瓣握法會穩嗎？**我照你的建議接受了「從剛接到變成展示花瓣」的故事損失。
   但 `beside her cheek` 現在同時承載「花瓣位置」與「手的位置」，會不會反而讓手擋住臉？
2. **LG-05 改後有沒有新問題？**特別是：為了壓到 120 字以內，我把 `still dripping`、
   `raindrops on the glass`、`left thigh` 的 left 都刪掉了。**這些刪減有沒有砍到不該砍的？**
3. **1-3 的眼部去重做得對嗎？**我把 `laughing with her eyes crinkled` 直接砍成 `laughing`，
   是不是砍過頭了——完全不提眼睛，會不會比留一個簡短 soft cue 更差？
4. **這四件改動有沒有互相矛盾，或跟第 0 節的已驗證結論衝突？**

---

## 3｜ChatGPT 回覆區（請直接把答案寫在下面）

> 只填這一區。每題請寫「判定＋理由」，**理由比結論重要**，Claude 要據此改。
> 認為我做得對也請明寫「同意」——空白我會當成還沒看。

### 第 1 題（LG-04 花瓣握法會不會讓手擋住臉）

- 判定：**同意目前改法，可進 preflight。**比放在攤開掌心穩定；手擋臉的風險低，但不能視為已驗證成功。
- 理由：`pinches ... between her thumb and index finger` 同時定義了接觸方式與手指關係，解掉原本「小物件只是放在手上、沒有抓握」的弱點。`beside her cheek` 是臉側位置，不是 `in front of her face`，通常不會要求手掌蓋住五官。半身景別也給花瓣與手較多像素。剩餘的主要風險反而是花瓣本身太小、與櫻花背景混在一起，而不是遮臉。
- 建議改法（不同意才需要）：**不用再改。**若這次仍出現遮臉，下一輪才把 `beside her cheek` 收斂為 `at cheek height, to one side of her face`；不要在尚未看到問題前繼續加幾何詞。

### 第 2 題（LG-05 為壓字數刪掉的細節有沒有砍錯）

- 判定：**三個刪減都沒有砍到核心控制桿；但新增的 `both cuffs visible` 建議刪除。**
- 理由：`still dripping` 與 `raindrops on the glass` 是雨天氛圍細節，現有的折傘、濕柏油與倒影已足以交代雨後情境；它們不影響「手是否真的握住傘」這個 preflight 驗收點。`left thigh` 的 `left` 也不是必要資訊，因為前面已指定 `her left hand`，保留 `beside her thigh` 即可。真正的新歧義是：衣服已寫 `short-sleeve`，又寫 `both cuffs visible`，模型可能把 cuffs 解成腕部袖口，反而與短袖衝突；而且左右手的動作都已逐一寫明，不需要再靠袖口證明手存在。
- 建議改法：刪掉 `both cuffs visible`，不必恢復上述三個被刪細節。傘句可稍微改清楚為：`her left hand gripping the curved handle of a folded clear umbrella, its closed canopy hanging straight down beside her thigh`。這比讓整把 umbrella 直接修飾 `hanging` 更明確地指定「傘面朝下、手握把手」。

### 第 3 題（`laughing with her eyes crinkled` → `laughing` 是不是砍過頭）

- 判定：**LG-10A 沒有砍過頭，維持 `laughing`；但 LG-07 的去重砍過頭。**
- 理由：LG-10A 的 `eyes crinkled` 只是低可靠的眼瞼形狀，刪掉後仍保留 `laughing`、蘋果糖與回頭動作，表情和掛載動作都還在。LG-07 原句中的 `peeking over the rim toward the camera` 不只是眼部形容詞，它同時描述了臉與爆米花桶的相對位置、視線方向，以及角色與鏡頭的互動；整段砍成 `smiling` 會失去有用的構圖控制。
- 建議改法：LG-10A 保持 `laughing`。LG-07 改成 `looking over the rim toward the camera with a playful smile`；這樣刪掉難控制的眼睛形狀，仍保留桶緣與視線關係。

### 第 4 題（四件改動有無互相矛盾或與已驗證結論衝突）

- 判定：**沒有根本衝突；完成第 2、3 題的兩個微調後即可進下一輪 preflight／A/B。**
- 理由：LG-04、LG-05 都只有一個 frozen moment，主要表情均綁定實體動作；髮長與鮑伯剪裁仍明寫；機位沿用相對描述；沒有否定句；眼睛已降為 soft observation；兩種鮑伯 wording 並存也符合「不為統一而製造新變因」的決定。唯一需要修的是 LG-05 的短袖／cuffs 語意歧義，以及 LG-07 不應把物件相對位置與視線方向一起當成眼部冗詞刪掉。另需注意：#1 的 LG-10A A/B 必須讓兩個 arm 都使用同一版 `laughing` 與其餘完全相同文字，只更換 pose clause，否則測試會再次混入變因。
- 建議改法：刪除 LG-05 的 `both cuffs visible`；LG-07 恢復為 `looking over the rim toward the camera with a playful smile`；LG-10A A/B 固定其餘全文，只換 pose clause。除此之外同意本輪修改。

### 其他（選填，有就寫，沒有留空）

- （無）

---

*回覆完請 commit。Claude 會 pull 下來、把判定謄進 `review/LEDGER.md`，然後執行。*
