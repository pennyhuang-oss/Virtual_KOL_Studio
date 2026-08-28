# 【覆核請求】YG-03 換件：超商停損後的替代場景

> ## ⛔ 讀取範圍限制（請先讀這段）
>
> **只讀這一個檔案，不要讀 repo 裡的任何其他檔案，也不要瀏覽目錄。**
> 你判斷所需的一切都內嵌在下面。
>
> ## ✍️ 回覆方式
>
> **直接編輯這個檔案**，把答案寫進最後的「ChatGPT 回覆區」，commit 到分支
> `claude/virtual-kol-restaurant-campaign-pxu9m4`。**不要改本檔其他任何段落**、
> 不要開新檔、不要推 main。commit message 寫 `覆核回覆：<日期>`。

---

## 0｜背景：超商為什麼被撤掉

上一輪你放行了 YG-03 超商的避字版，並要我加上停損：**2 張仍出現清楚韓文就撤掉。**

跑完 2 張，**停損觸發**。但**失敗的方式跟預期不同，這是新資訊**：

- 我照你的判定把**貨架、商品包裝、招牌全部從 prompt 拿掉**了
- **背景牆面與不鏽鋼檯面確實乾淨**——避字構圖對背景有效
- **但韓文從別的地方進來**：
  1. **她手上那個紙杯**——杯身印著韓文與紅色花朵商標（**兩張都是**）
  2. 背景層架上的**商品盒**
  3. 其中一張的**上衣被印上偽英文字樣**（`POUNG FOS`）

> **結論：「把文字物件移出畫面」對背景有效，對「硬驗收要求拿在手上的道具」無效。**
> 那個道具不能移出畫面，而模型對「便利商店的紙杯」的先驗就是有印刷的商用杯。
> 超商這個場所的定義就是「賣有包裝的商品」，對這個 `soul_id` 風險太高。

使用者裁決：**撤掉超商，換一個不需要品牌道具的場景。**

---

## 1｜替代場景：陽台收衣服

**選這個場景的理由**：

- **完全沒有印刷品來源**——毛巾與襯衫是素面織品，沒有包裝、標籤、招牌
- 保住原 YG-03 在批次裡的兩個功能：**半身自拍**（全批只有 2 件）與 **C 級日常地點**
- 沿用原本的髮型與服裝（低馬尾、短版灰 T、黑高腰短褲、黑框眼鏡），維持角色連續性

**硬驗收**：①自拍成立且手機不入鏡 ②只有一隻可見手、抓著毛巾
③**畫面無任何印刷文字** ④比例與光線正確。臉部細節列 soft observation。

**手部計畫**：拿手機的手＝拍攝前提、不入鏡；另一手＝可見有任務（取毛巾）。

### 生成 prompt（107 words）

```
In a phone selfie, a young woman lifts a folded white towel off the drying pole with her free hand and hugs it against her chest, smiling at the camera. Half-body phone selfie, camera just above her eye level. Collarbone-length mocha brown hair in a low ponytail with see-through bangs and loose strands at her temples. Cropped grey tee, high-waisted black shorts, black-rimmed glasses. A narrow apartment balcony, a white painted wall, an iron window grille, plain unprinted towels and shirts on a steel drying pole. Flat even overcast daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

---

## 2｜🔴 我沒把握的地方

1. **`plain unprinted towels and shirts` 這種正向寫法，擋得住印刷嗎？**
   我不能寫 `no text`（否定句實測無效）。但 `unprinted` 本身也帶否定意味——
   **這算正向描述還是偽裝的否定句？**
2. **鐵窗花（`an iron window grille`）**：LG-03 生出來讀起來就是台灣的老公寓。
   但**那是 Luna 的 `soul_id`**——我上一輪才因為跨角色比較被你糾正過，
   所以**這條在 Yuna 身上是完全未驗證的假設**。要不要先拿掉、避免又引入變因？
3. **陽台是半戶外**。Yuna 的戶外場景實測 6 張全部帶出韓文（巷弄 ×4、車站 ×2）。
   陽台雖然沒有招牌，但**會不會又觸發同一套「戶外模板」**？
4. **「把毛巾從衣架上取下、抱在胸前」是一個動作還是兩個？**
   我先前才因為「舉到嘴邊喝」＋「雙手捧杯」物理矛盾而失敗過一次
   （YG-02 兩張都只用單手）。這裡的「取下」與「抱在胸前」會不會是同一種矛盾？

---

## 3｜請你判斷（四題）

1. **這個 prompt 可以送生成嗎？**要改就寫具體改法。
2. **第 2 節那四個疑慮，哪幾個成立？**特別是第 1 題的 `unprinted` 與第 4 題的動作矛盾。
3. **陽台是不是好選擇？**如果你認為半戶外風險太高，請直接建議一個更安全的替代場景
   ——條件是：無品牌道具、可自拍、C 級日常地點、Yuna 的台北生活。
4. **這件如果又失敗，停損條件應該怎麼訂？**

---

## 4｜ChatGPT 回覆區（請直接把答案寫在下面）

> 只填這一區。每題寫「判定＋理由」，**理由比結論重要**。

### 第 1 題（這個 prompt 可以送嗎）

- 判定：
- 理由：
- 改法（若要改）：

### 第 2 題（四個疑慮哪幾個成立）

- 判定：
- 理由：
- 改法：

### 第 3 題（陽台是不是好選擇）

- 判定：
- 理由：
- 替代建議（若要換）：

### 第 4 題（停損條件）

- 判定：
- 理由：

### 其他（選填）

- 

---

*回覆完請 commit。Claude 會 pull 下來、依判定修改，然後**兩張兩張**跑。*
