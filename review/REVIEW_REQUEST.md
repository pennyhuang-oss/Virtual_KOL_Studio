# 【覆核請求】接下來 4 件的 prompt — 送生成前逐件覆核

> ## ⛔ 讀取範圍限制（請先讀這段）
>
> **只讀這一個檔案，不要讀 repo 裡的任何其他檔案，也不要瀏覽目錄。**
> 你判斷所需的一切都內嵌在下面。你只做檢核、不規劃也不執行，
> 用量不該比執行方還高。
>
> ## ✍️ 回覆方式
>
> **直接編輯這個檔案**，把答案寫進最後的「ChatGPT 回覆區」，commit 到分支
> `claude/virtual-kol-restaurant-campaign-pxu9m4`。**不要改本檔其他任何段落**、
> 不要開新檔、不要推 main。commit message 寫 `覆核回覆：<日期>`。

---

## 0｜新規矩（使用者 2026-08-28 定）

1. **每一段 prompt 送出生成前都要經你覆核**——不是「沒把握才送」，**是每一段都送**。
   你說不行，我就改，改完再送。
2. **生成一次只跑一件 spec × 2 張**，看完結果再跑下一件。**不會一次跑一大批。**
3. 為了少讓使用者轉傳，**覆核可以一次放幾件**（本檔 4 件）；
   但**生成仍然一件一件、兩張兩張跑**。

---

## 1｜最小背景

- Higgsfield Soul 2.0（`soul_2`）＋ 已訓練 `soul_id`。**無 negative prompt、無 seed。**
- 一段 prompt 一次生成、`2k`、`9:16`、0.12 credits／張。
- 這 4 件都是 **Yuna**（韓籍、及鎖骨長髮、設定住台北）。
- **已驗證有效**（你先前的建議，都已實測）：
  不寫族裔身材數字｜相對機位描述｜否定句無效｜
  `background exposed the same brightness as her skin` 解逆光｜
  服裝用「品名＋2–3 個可見結構特徵」（迷你裙 `continuous hem` 4/4 正確）｜
  空手寫 `her free arm relaxed at her side`（5/5 沒有多手）｜
  `In a phone selfie,` 前置讓手機不入鏡且自拍幾何成立｜
  **硬驗收只放巨觀動作／手—物件接觸／構圖／服裝結構／髮長；眼型嘴型一律 soft**。
- **已知風險**：Yuna 的**戶外／公共空間場景會帶出韓文招牌**（實測 4 張）。
  對策是把會出現文字的東西移出畫面；YG-05 這樣做之後韓文消失，
  但場景識別度也消失——使用者已接受「地點不可辨」的取捨。

---

## 2｜這 4 件的 prompt

### YG-01｜咖啡廳靠窗・臉部近景

- 景別：臉部＋肩膀近景 ｜ 字數：102
- **硬驗收＝一手把頭髮撥到耳後＋轉頭看鏡頭**（臉部細節一律 soft）

```
A young woman tucks a strand of hair behind her ear and turns to look at the camera, one corner of her mouth lifted, head tilted toward that hand. Close-up of face and shoulders, camera at her eye level, lens horizontal. Collarbone-length soft wavy mocha brown hair with see-through wispy bangs. Cream fitted fine-knit tee, thin gold necklace, small gold hoops. Bright cafe window seat, white wall, pale wood table, a latte and her phone. Soft cool daylight from her front-left landing on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.
```

### YG-02｜台北公寓窗邊晨光

- 景別：3/4 身（膝上） ｜ 字數：100
- **硬驗收＝雙手捧馬克杯舉到嘴邊**（臉部細節一律 soft）

```
A young woman stands at the window holding a mug with both hands and lifts it to her mouth, eyes still narrowed from sleep, a loose easy smile. Three-quarter body, camera at her navel level, lens horizontal, shot from well back. Collarbone-length mocha brown hair, sleep-mussed, see-through bangs flattened with one tuft sticking up. White fitted camisole, high-waisted grey cotton shorts, beige cardigan slipping off one shoulder, bare feet. Small bright apartment, white walls, pale wood floor, unmade white bed. Soft morning light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-03｜超商・「今天學到一個字」

- 景別：半身自拍 ｜ 字數：110
- **硬驗收＝（未標註）**（臉部細節一律 soft）

```
In a phone selfie, a young woman holds a paper cup of hot broth up beside her cheek with her free hand, smiling at the camera with her chin tucked. Half-body phone selfie, camera just above her eye level, the shelves behind her thrown completely out of focus. Collarbone-length mocha brown hair in a low ponytail with see-through bangs and loose strands at her temples. Cropped grey tee, high-waisted black shorts, black-rimmed glasses. A convenience store interior, fluorescent ceiling tubes, a steaming hot-food counter, blurred shelves of packaged snacks. Flat even fluorescent light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-04｜梳妝台護膚・素顏

- 景別：臉部＋上半身近景，拍鏡中反射 ｜ 字數：99
- **硬驗收＝（未標註）**（臉部細節一律 soft）

```
A young woman presses serum into her cheek with her fingertips, eyes closed, chin lifted, mouth relaxed into a small smile. Close-up of her face and shoulders reflected in the mirror, camera at her eye level, lens horizontal. Collarbone-length mocha brown hair clipped back with a claw clip, a few strands loose at her forehead. White fitted camisole. White marble bathroom counter, square mirror, white tiled wall, skincare bottles and brushes left unarranged. Broad diffuse frontal light with very low shadow contrast, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.
```

---

## 3｜請你逐件判斷

對**每一件**回答：**可以送生成 / 要先改**。要改的話寫出具體改法。

特別請看這幾點：

1. **YG-03 是超商、YG-01 是咖啡廳窗邊**——都是**會出現文字招牌**的場所。
   依 Yuna 的已知風險，這兩件會不會重蹈 YG-05 的覆轍？現在的寫法夠不夠？
2. **YG-02、YG-04 是室內**（公寓窗邊、浴室鏡前）。
   浴室鏡前那件——LG-08 的鏡面構圖成功了，但**拍攝設備入鏡**是鏡面的已知風險，
   YG-04 需不需要比照處理？
3. **手部可見性**：每件的兩隻手分別屬於「可見有任務／可見但休息／依裁切不入鏡」哪一類？
   有沒有哪一件的空手沒有交代、可能誘發模型自行補姿勢？
4. **有沒有哪一件的硬驗收點還是依賴臉部細節？**（應該都已改掉，請幫我確認）
5. **有沒有共通問題？**

---

## 4｜ChatGPT 回覆區（請直接把答案寫在下面）

> 只填這一區。每件寫「可以送 / 要先改」＋理由；要改就寫具體改法。
> 認為某件沒問題也請明寫「可以送」——空白我會當成還沒看。

### YG-01 咖啡廳靠窗・臉部近景

- 判定：
- 理由：
- 改法（若要改）：

### YG-02 台北公寓窗邊晨光

- 判定：
- 理由：
- 改法：

### YG-03 超商

- 判定：
- 理由：
- 改法：

### YG-04 梳妝台護膚・素顏

- 判定：
- 理由：
- 改法：

### 共通問題（第 3–5 題）

- 

---

*回覆完請 commit。Claude 會 pull 下來、依判定修改，然後**一件一件、兩張兩張**跑。*
