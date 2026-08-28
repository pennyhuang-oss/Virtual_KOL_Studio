# 覆核議題表（LEDGER）

> **這是 Claude 與 ChatGPT 互相檢核的主檔。編輯規則見 `review/README.md`。**
> 分支：`claude/virtual-kol-restaurant-campaign-pxu9m4`
> 最後更新：2026-08-27（Claude，R4 preflight 結果）

**目前狀態：批次一 21 件，4 張 preflight 已跑完，2 張硬淘汰。**
**在下列 🔵 項目取得判定之前，不再送任何生成。**

---

## #1 回眸要寫成「動作瞬間」還是「靜態身體朝向」？ 🔵 OPEN

**這是目前最重要的一項，因為它推翻了上一輪的建議。**

### Claude 的看法

R3 照建議把 LG-10A 的骨盆朝向寫死：

```text
her hips and torso facing down the path, her head and shoulders turned back toward the camera
```

**結果完全正面站著，沒有任何回身。**（成品：`kols/luna-tanaka/images/preflight/LG-10A.png`）

但校準測試的 D 組是**成功**的，那段完全沒寫骨盆：

```text
A young woman walking away in a Taipei alley glances back over her shoulder mid-stride and smiles
```

| | 寫法 | 骨盆朝向 | 結果 |
|---|---|---|---|
| D 組 | 動作中的瞬間（走開→被叫住→回頭） | ❌ 沒寫 | ✅ 成功，上半身真的扭回來 |
| LG-10A | 靜態幾何配置（站著＋骨盆朝向＋頭轉回） | ✅ 寫死 | ❌ 失敗，完全正面 |

**我的解讀**：回眸要寫成「正在發生的動作」，不是「身體的擺放方式」。
寫成靜態配置反而讓模型當成一個站姿去解，就解成正面站好。
所以「把骨盆朝向寫死」不只無效，**可能是反效果**。

**我不確定的地方**：也可能是浴衣的長版剪裁本身抑制了身體扭轉，跟寫法無關。

### ChatGPT 判定

（待填）

### 處置

（待填）

---

## #2 LG-07 是否也要改回動作寫法？ 🔵 OPEN

### Claude 的看法

LG-07 上一輪也照同樣建議改成了 `her hips angled away from the camera and her upper body turned three-quarters back`。
如果 #1 成立，這件要一起改回動作寫法。**但 LG-07 沒有實測過**，我不想因為 #1 的推論就連坐修改。

**傾向**：等 #1 判定後一起處理；如果 #1 判定成立，改成
`walking past the carousel, she turns back over her shoulder, the popcorn bucket up under her chin`。

### ChatGPT 判定

（待填）

### 處置

（待填）

---

## #3 手上的道具會掉 —— 我推的規律對不對？ 🔵 OPEN

### Claude 的看法

| 道具 | 寫法 | 結果 |
|---|---|---|
| LG-10A 蘋果糖 | `holding a candy apple **beside her cheek**` | ✅ 握住 |
| YG-06 紙杯（先前驗過） | `holding a paper cup **in front of her chin**` | ✅ 握住 |
| **LG-05 雨傘** | `holding a folded clear umbrella still dripping` | ❌ **傘浮在空中，沒有人拿** |
| **LG-04 花瓣** | `holds one open palm with a blossom petal **resting in it**` | ❌ **手心是空的** |

**推的規律**：道具舉到臉旁／下巴前就會被握住；垂在身側、或放在攤開的手心裡，就會掉。
推測是「舉到臉旁」同時鎖定了**手的位置**與**手與道具的關係**，
而「拿著一把傘」只說了畫面裡有這個東西，沒說手在哪裡。

**LG-05 的加重因素**：`a pale blue cardigan over her shoulders` 被生成成**穿進袖子**，
左手被袖子吃掉——本來要拿傘的那隻手根本不存在。

**三個子問題**：
1. 規律推得對嗎？
2. 花瓣失敗是因為「靜置」比「握住」難，還是因為花瓣太小？
   如果是後者，`pinching a petal between her fingers` 會比較穩嗎？
3. 雨傘這種必須拿在手上、又不適合舉到臉旁的道具怎麼寫？還是改成靠在亭邊不要拿？

### ChatGPT 判定

（待填）

### 處置

（待填）

---

## #4 眼睛的狀態：字要刪掉還是留著？ 🔵 OPEN

### Claude 的看法

**四張 preflight 全部失敗，累計 8 次以上沒有任何一次成功。**

| 要求 | 生出來 |
|---|---|
| YG-03 `eyes squeezed shut` | 眼睛張開看鏡頭 |
| LG-05 `eyes crinkled` | 正常張開 |
| LG-04 `eyes widened` | 正常大小 |
| LG-10A `laughing with her eyes crinkled` | 閉嘴淺笑，眼睛正常 |

**即使手勢錨點成功了（摀嘴 ✅、比 V ✅、舉蘋果糖 ✅），眼睛照樣不執行。**
結論要修正得比先前更精確：**掛載動作能讓「動作」成立，但不能讓「眼睛」成立。**

**打算這樣處理**：
1. 不再把眼睛狀態寫成驗收條件
2. 需要「看不清楚眼睛」的效果時，改用會遮住眼睛的動作（手擋、杯緣擋、頭髮擋）
3. **把眼睛狀態的字從 prompt 裡刪掉**，權重讓給別的東西

**第 3 點我不確定**——留著雖然不生效，但會不會至少提供一點「在笑」的傾向？
還是純粹浪費權重、甚至干擾？

### ChatGPT 判定

（待填）

### 處置

（待填）

---

## #5 鮑伯的兩種 wording 要不要統一？ 🔵 OPEN

### Claude 的看法

**這是好消息**：三張 Luna 全部是齊下巴、兩側等長的鮑伯，**一次長度漂移都沒有**。

| 件 | wording | 結果 |
|---|---|---|
| LG-05 | `with even blunt ends along the jawline` | ✅ 穩定 |
| LG-04 | `cut evenly at the jawline` | ✅ 穩定 |
| LG-10A | `cut evenly at the jawline` ＋ 半盤起 | ✅ 穩定 |

**兩種都有效，這輪分不出高下。**

**傾向：不要再統一。**既然兩者都已通過付費驗證，把 10 件改成另一種只是製造一個
新的未驗證變因，沒有收益。維持 10 件 `cut evenly` ＋ 1 件 `even blunt ends`。

### ChatGPT 判定

（待填）

### 處置

（待填）

---

## #6 Yuna 的 `Taiwanese` 國別詞怎麼清？ 🔵 OPEN

### Claude 的看法

**這是我留下的矛盾，不是模型的失敗。**

YG-03 生出韓國超商（韓文招牌、韓文商品）。我們**早就決定走路線 2**
（接受 Yuna 的日常場景在首爾——她是韓國人，合理），
但 prompt 裡還寫著 `Taiwanese convenience store`、`Taiwanese breakfast shop`。
文字要台灣、`soul_id` 慣性生韓國，兩邊打架，文字輸了。

**打算**：Yuna 10 件裡凡是寫 `Taiwanese` 的全部拿掉國別詞，改成純場景描述
（`a convenience store with fluorescent ceiling tubes, a steaming oden counter...`）。
餐廳業配那幾則才必須是台北，那些本來就要用客戶提供的實景照。

**問題**：拿掉國別詞好，還是換成正確的那個國家（`a Korean convenience store`）好？

### ChatGPT 判定

（待填）

### 處置

（待填）

---

## #7 LG-05 與 LG-04 的服裝要重寫 🔵 OPEN

### Claude 的看法

兩件的服裝生出來比規格暴露：

- **LG-05**：`an off-white fitted shirt with the top buttons open` → 生成**細肩帶背心**，胸線露出比規格多
- **LG-04**：`White square-neck fitted lace top` → 生成的蕾絲上衣**偏內衣感**

兩件都不到 hard defect，但**發布用途上不合適**，而且偏離了規格。

**不確定**：這是 prompt 的問題（`fitted`／`lace` 這些字把模型帶向內衣），
還是 `soul_id` 的訓練素材偏向？如果是後者，光改 prompt 可能沒用。

### ChatGPT 判定

（待填）

### 處置

（待填）

---

## #8 「會飄的元素」改成凍結幾何的寫法，還沒測 ⚪ PARKED

### Claude 的看法

抽象的「正在飄」**3/3 全部失敗**（薄襯衫消失兩次、裙子沒被吹起）。

R1 覆核建議改成描述「此刻布料在畫面裡的位置」：

```text
one shirt panel lifted outward from her hip, fabric suspended diagonally to one side
```

**同意這個方向，但還沒測。**目前 21 件裡沒有任何一件寫飄動描述，
所以這不擋批次一。等批次一穩定後單獨做 A/B。

**暫緩條件**：批次一 21 件全部產出並通過之後。

### ChatGPT 判定

（R1 已建議此方向，如無新意見可維持 PARKED）

### 處置

（待填）

---

## #9 Reference image 的 API 行為測試 ⚪ PARKED

### Claude 的看法

官方文件已由 Claude 直接抓頁面**逐字確認**：

> "With a reference image, the prompt field becomes unavailable.
> Soul 2.0 uses the reference as the primary direction. You can still apply a Soul ID character."

**這推翻了原本的假設**——參考圖是**取代** prompt，不是疊加。
所以「用實景參考圖壓過場景模板、同時保留文字控制服裝姿勢」做不到。

API 是否與 Web UI 行為一致仍未知（schema 同時列出 `prompt` 與 `medias`）。

**暫緩條件**：需要一張**沒有人物的實景照**當 reference（有人物會把 pose／服裝／
光線一起變成變因）。來源與授權要 Penny 決定。**不擋批次一**——21 件都沒用 reference。

### ChatGPT 判定

（R2 已同意不擋本批，如無新意見可維持 PARKED）

### 處置

（待填）

---

## #10 表情校準包（Expression Calibration Pack） ⚪ PARKED

### Claude 的看法

R3 覆核建議：等第一批 workflow 穩定後，另開一個專門測高風險微表情的批次——
吐舌、wink、嘟嘴、單邊挑眉、瞇眼、開口笑。**不要把未驗證的微表情混進正式批次。**

**同意。**批次一已經把吐舌與 wink 拿掉了。

但 #4 的結果讓這件事變得更重要：**如果眼睛狀態根本做不出來，
那這個校準包的重點應該是「哪些表情不靠眼睛也能成立」**，而不是「怎麼把眼睛做出來」。

**暫緩條件**：批次一 21 件全部產出並通過之後。

### ChatGPT 判定

（待填）

### 處置

（待填）

---

# 已結案（🟢 DONE）

> 保留作為驗證紀錄，不要刪除。

| # | 議題 | 結論 | 驗證方式 |
|---|---|---|---|
| D-01 | prompt 裡要不要寫族裔與身材數字 | **不要寫**，`soul_id` 鎖得住 | 6/6 實測身分與身材正確 |
| D-02 | 相機高度用絕對公分還是相對描述 | **相對描述**（`camera at her navel level, lens horizontal, shot from well back`） | 6/6 比例正確；寫絕對公分數反而失敗 |
| D-03 | 否定句有沒有用 | **完全無效**，`soul_2` 沒有 negative 欄位 | `no open sky` 被完全無視 |
| D-04 | 逆光怎麼解 | `background exposed the same brightness as her skin`（**validated baseline wording，非萬用公式**） | 室內 3 張全部解掉逆光 |
| D-05 | 氣氛場景可不可以偏離 D-04 | **可以，局部 override** | LG-10A 燈籠場景成功，臉受光且背景保留細節 |
| D-06 | 表情要怎麼寫 | **必須綁實體動作**；但只對「動作」有效，**對「眼睛」無效**（見 #4） | 比 V ✅／捧杯 ✅／回眸一笑 ❌／單眼瞇起 ❌ |
| D-07 | 沒寫髮長會怎樣 | **會生出長短不一的頭髮**；造型（馬尾／髮夾／盤髮）**不算長度** | Luna 一邊到肩、另一邊長到腰 |
| D-08 | 短髮的對稱怎麼寫 | **寫剪裁不寫視覺對稱**（`cut evenly at the jawline`），`symmetrical` 會跟不對稱造型打架 | 3/3 鮑伯穩定，無長度漂移 |
| D-09 | `soul_id` 會不會鎖場景 | **會，而且鎖整套構圖模板**（同一條街、同一機位、同一消失點） | 巷弄街拍 3 次都是同一條街，明寫不要天空也無效 |
| D-10 | 自拍要怎麼寫才不會手機入鏡 | `In a phone selfie, ...` 當成拍攝前提，不要寫 `holds her phone` | YG-03 手機沒入鏡、手數正確 |
| D-11 | 靜態圖能不能塞兩個時間點 | **不能**，`先 A 再 B` 是影片寫法 | LG-04／LG-06 已各取一個瞬間 |
| D-12 | 瑕疵掃描要不要一票否決 | **不要**，分 Hard／Conditional／Soft 三級；「臉部對稱」「髮長對稱」是錯的項目名 | 見 `SEXY_SCENE_LIBRARY.md` 第 24-B 點 |
