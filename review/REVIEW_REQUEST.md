# 【覆核請求】批次一 — 依你的判定改完，請確認改法

> **這封訊息是自足的，不需要讀 GitHub、不需要開任何檔案。**
> 需要的背景全部在下面。請直接就這些文字判斷。

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

## 3｜回覆方式

**請直接用純文字回，不要動 GitHub。**每題格式：

```
題號｜判定（同意／不同意／有條件同意）
理由：（一到三句，理由比結論重要，我要據此改）
建議改法：（若不同意才需要）
```

如果你認為某題我做得對，也請明寫「同意」——沉默我會當成還沒看。
