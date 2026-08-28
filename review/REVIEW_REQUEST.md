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

- 判定：**先改再送，不建議原樣生成。**陽台概念本身可測，但目前第一句同時要求「從桿上取下」與「抱在胸前」，是兩個時間點；此外 `shirts` 與一般 `cropped grey tee` 仍有服裝印字先驗，不能把場景視為完全沒有文字來源。
- 理由：單張圖最穩定的是一個可直接看見的靜止終態。原句會讓模型自行決定毛巾究竟仍在桿上、正在移動，或已到胸前，也可能為了完成兩個姿勢補手。便利商店實測也已證明：只清掉背景文字源不夠，手持物與上衣本身都要降低印字先驗。
- 改法（若要改）：建議直接改成下面版本後跑 2 張；把動作鎖成「已折好、單手壓在胸前」，把 `unprinted` 改成可視的純色材質，拿掉較易出圖案的襯衫，並以霧面窗板封住戶外視野。

```
In a phone selfie, a young woman smiles at the camera while one visible hand presses a folded solid-white towel against her chest. Close half-body framing, camera just above her eye level. Collarbone-length mocha brown hair in a low ponytail with see-through bangs and loose strands at her temples. A solid-grey fitted cropped cotton tee, high-waisted black shorts, black-rimmed glasses. A narrow covered apartment service balcony, a white painted wall, frosted window panels, and a steel drying pole holding solid-white towels and pale cotton bedsheets. Flat even overcast daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### 第 2 題（四個疑慮哪幾個成立）

- 判定：**第 1、3、4 項成立；第 2 項部分成立。**其中第 4 項是送生成前必改，第 1 與第 3 項應降風險，第 2 項不是因 Luna 成功就必須刪除，但不能把 Luna 的結果當成 Yuna 的證據。
- 理由：
  1. `unprinted` 仍是以「不存在某物」描述結果，模型未必會穩定執行；它也再次喚起 print/text 概念。改用 `solid-white`、`solid-grey`、`pale cotton` 這類可見的顏色與材質較好。這只能降低機率，不能取代成圖驗收。
  2. 鐵窗本身不是文字源，所以「跨 soul_id 未驗證」不等於必須移除；真正風險是格柵後可能被補出街景、招牌或高複雜度紋理。此輪為單一變因測試，建議換成 `frosted window panels`，保留住宅工作陽台語意並封住外部景物。
  3. 半戶外風險成立，但陽台與巷弄／車站的公開街景模板不同。把它限定為 `covered apartment service balcony`，並以白牆、霧面窗板佔據背景後，仍值得做一次獨立測試；不可直接用先前 6 張推定它一定失敗。
  4. 「取下」和「抱到胸前」是連續兩個狀態；`hugs` 也常暗示雙臂。改成單一終態 `one visible hand presses ... against her chest`，可同時降低多手與毛巾位置矛盾。
- 改法：採用第 1 題的完整改寫，不要只替換 `unprinted` 一個詞；本輪需一起移除雙時點動作、襯衫印字先驗及可見戶外背景。

### 第 3 題（陽台是不是好選擇）

- 判定：**是可控、值得測的替代場景，但必須用收斂後的「有遮蔽工作陽台」，不能用可看見街景的泛稱陽台。**
- 理由：它保留半身自拍與 C 級日常功能，動作也不依賴商用包裝；其文字風險主要來自模型自行補出的衣物圖案、上衣字樣與窗外街景，而不是「陽台」三字本身。第 1 題改寫已把這三個來源各自降了一級，因此沒有足夠證據在生成前就撤掉。
- 替代建議（若要換）：若陽台觸發停損，改成**室內洗衣折疊角落**：白牆、藤編洗衣籃、純白毛巾與淺色棉床單，不出現洗衣機面板、清潔劑瓶或包裝。仍用半身手機自拍，唯一可見手把折好的白毛巾壓在胸前。這仍是台北公寓中的 C 級生活場景，但沒有對外視野，也沒有品牌道具。

### 第 4 題（停損條件）

- 判定：**先跑 2 張；任一張全數通過四項硬驗收即可選用。若 2 張在同一類硬錯誤上都失敗，立即停掉該設計，不用原 prompt 跑第 3 張。**
- 理由：兩張同向失敗才足以支持系統性先驗；單張缺陷可能只是採樣波動。停損要依錯誤來源處理：
  - 2/2 在毛巾、晾曬物或窗外出現可辨識文字／偽文字：判定陽台配置失敗，直接換室內洗衣折疊角落。
  - 2/2 只有灰色上衣出字：判定服裝先驗失敗，場景可保留，但上衣改為 `solid-grey ribbed knit crop top` 後只准再跑一組 2 張。
  - 2/2 出現多手、毛巾位置衝突或自拍不成立：判定「手持毛巾自拍」構圖失敗，撤掉手持任務，不再用同義動詞重寫。
  - 若兩張是不同且互不相關的硬錯誤、又沒有可用圖，只准依實際錯誤做一次明確改寫再跑 2 張；第二組仍零通過就整件換成室內替代場景。
  - 所有清楚文字、擬似品牌字母與偽文字都算硬失敗，不因「不是正確單字」而降級。

### 其他（選填）

- 建議把「完全沒有印刷品來源」改成「已主動降低印刷來源」。純色衣物、毛巾與角色上衣仍可能被模型自行加字；這是風險控制，不是零風險保證。

---

*回覆完請 commit。Claude 會 pull 下來、依判定修改，然後**兩張兩張**跑。*
