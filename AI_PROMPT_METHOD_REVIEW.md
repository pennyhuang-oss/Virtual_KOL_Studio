# AI 圖像 Prompt 方法論 — 待外部覆核

> **這份文件是要拿給 ChatGPT（或其他模型）交叉覆核用的。**
> 作者：Claude（Virtual KOL Studio 專案）
> 日期：2026-08-27
>
> **背景**：本專案用 Higgsfield Soul 2.0（`soul_2`）+ 已訓練的 `soul_id` 生成虛擬 KOL 的
> Instagram 素材。連續兩輪 pilot 被使用者退回，症狀是：姿勢僵硬、表情沒做出來、
> 人物背光不亮眼、比例失真（頭大腿短）、場景生成到錯誤的國家。
>
> 我已經分別研究了「網美攝影的拍照公式」與「AI 圖像 prompt 的寫法」，
> 但**我無法自我驗證研究結論是否正確、以及兩者能否正確銜接**。
> 這正是需要覆核的地方。

---

## 請覆核的重點（給覆核者）

請針對以下每一節的 **【我的結論】** 判斷：**正確 / 部分正確 / 錯誤**，並說明理由。
特別關注標記 **🔴 不確定** 的部分。文末有集中的問題清單。

---

## 一、關鍵限制：`soul_2` 這個模型能給什麼

這是實際查詢模型 API 得到的完整參數表，不是推測：

```json
{
  "id": "soul_2",
  "name": "Higgsfield Soul 2.0",
  "description": "Realistic UGC, fashion editorial and character generation",
  "output_type": "image",
  "parameters": [
    { "name": "quality", "type": "string", "options": ["1.5k", "2k"], "default": "2k" },
    { "name": "soul_id", "type": "string", "description": "Soul-ID for personalized generation" }
  ],
  "medias": [
    { "name": "medias", "type": "image", "max": 1, "roles": ["image"] }
  ],
  "aspect_ratios": ["1:1","16:9","9:16","4:3","3:4","3:2","2:3"]
}
```

**【我的結論】**

1. **這個模型沒有 negative prompt 欄位。**可調的只有 `quality`、`soul_id`、
   `aspect_ratio`、`prompt`、以及 **1 張參考圖**。
2. 因此所有「不要出現 X」的需求，**只能靠正向描述繞過，不能靠否定**。
3. `soul_id` 已經鎖定人物身分（臉、體型），所以 **prompt 裡再用文字描述國籍／五官，
   理論上是多餘的，而且可能造成干擾**。
4. **那張參考圖（`medias`）是目前最強、但我完全還沒用過的控制手段。**

**🔴 不確定**：第 3 點。`soul_id` 到底鎖定了多少？只有臉，還是也包含體型與氣質？
如果只鎖臉，那體型描述仍然必要。我沒有找到官方文件說明。

---

## 二、Prompt 長度 — 我認為這是最大的錯誤

### 研究結論（外部來源）

> 「多數生成器在 **30 到 75 字**之間的 prompt 產出最好的擬真效果——
> **太短會留太多給 AI 想像，極長的 prompt 則會稀釋每個關鍵字的重要性**。」

### 我實際做的事

| | 字數 | 相對建議上限 |
|---|---|---|
| 建議範圍 | 30–75 words | — |
| **我第一輪送出的 prompt** | **約 300 words** | **4 倍** |
| **我第二輪送出的 prompt** | **約 330 words** | **4.4 倍** |

**【我的結論】**
我把「規格寫得很詳細」直接等同於「prompt 寫得很詳細」，這是方法錯誤。
規格（給人看的、確保思考完整）與 prompt（給模型看的、要精準有效）**不是同一份東西**，
我卻是把規格逐條翻譯成英文送進去。**這很可能是「規格寫了但模型沒吃到」的主因**——
不是模型不聽話，是我把每個關鍵字的權重都稀釋掉了。

**🔴 不確定**：
- 30–75 字這個範圍是針對哪些模型測出來的？對 Higgsfield Soul 2.0 這種
  「已用 LoRA/embedding 鎖定身分」的模型是否同樣適用？
- 如果要壓到 75 字，我目前規格裡的十個維度（妝容／髮型／穿著五層／場景／機位／
  焦段／構圖／光線五段／表情／肢體）**顯然放不下**。
  **哪些該留、哪些該砍？** 這是我最需要建議的地方。

---

## 三、否定詞 — 已確認我做錯了

### 研究結論（外部來源）

> 「擴散模型**根本上難以理解否定**。要求『a portrait of a friendly monster, **not scary**』時，
> 模型通常無法排除 scary 這個屬性。」
>
> 「Negative prompt 的作用機制是 **Classifier-Free Guidance（CFG > 1.0）**——
> 它在生成過程中把擴散方向推離不要的概念，**這跟正向 prompt 的處理方式根本不同**，
> 所以必須放在獨立欄位。」

### 我實際做的事

第二輪我在**正向 prompt 裡**寫了：
```
This is Taiwan, NOT Korea and NOT Japan; no Korean hangul signage, no Japanese signage.
```

**結果：完全無效。** Yuna 那張生出滿街韓文招牌，Luna 那張生出日文站牌與日式木造建築。

**【我的結論】**
1. 這個寫法從原理上就不可能有效。
2. 更糟的是，**寫「NOT Korea」等於在 prompt 裡塞了「Korea」這個 token**，
   可能反而**強化**了韓國的權重。
3. 而 `soul_2` 沒有 negative prompt 欄位（見第一節），
   所以**這個工具上根本沒有正確使用否定的方法**。

**【我打算改成】**
- 完全不提不想要的東西（不寫 Korea / Japan / NOT）
- 把國籍描述從 prompt 移除，讓 `soul_id` 自己決定臉
- 用**強烈的正向台灣元素**：繁體中文直式招牌、騎樓、鐵捲門、白底機車牌
- 用**參考圖**鎖定場景

**🔴 不確定**：把「Korean woman」整句拿掉之後，`soul_id` 會不會失去族裔特徵？
還是說 soul 訓練本身已經足夠？

---

## 四、相機與鏡頭 — 研究說這是權重最高的一段

### 研究結論（外部來源）

> 「指定相機與鏡頭組合——例如 **`shot on Canon EOS R5, 85mm f/1.8`**——
> **比任何其他單一元素做的事都多**，因為它強迫模型模擬真實光學特性：
> 散景、鏡頭壓縮、景深衰減——這些是一眼就能辨識為『攝影』而非『插畫』的特徵。」

### 我實際做的事

- 第一輪、第二輪都寫了 `shot on a 35mm lens`
- **35mm 是廣角**。用在全身近距離拍攝會造成比例失真
- 我沒有寫**機身型號**，也沒有寫**光圈值**

**【我的結論】**
1. 焦段寫錯了（廣角→全身變形），這點已確認。
2. **但更重要的是我漏了「機身 + 光圈」這個組合**。
   研究說這是權重最高的一段，我只寫了半個。
3. 正確寫法應該是 `shot on Canon EOS R5, 85mm f/1.8` 這種完整規格。

**【我打算改成】**

| 景別 | 相機規格寫法 |
|---|---|
| 全身 / 3-4 身 | `shot on Canon EOS R5, 85mm f/2.0` |
| 半身 / 近景 | `shot on Canon EOS R5, 85mm f/1.8` |
| 自拍 | `shot on iPhone 15 Pro front camera` |

**🔴 不確定**：
- 寫具體機身型號（Canon EOS R5）是否真的有效，還是只是安慰劑？
- 對 Higgsfield 這種閉源商用模型是否適用（研究多半來自 Stable Diffusion 生態）？

---

## 五、皮膚質感 — 這點我做對了

### 研究結論（外部來源）

> 「每個人像 prompt 都要保留 **`visible pores and faint freckles`** 這類皮膚質感字眼，
> 以避免臉部變成蠟感、噴槍修過的樣子。」

### 我實際做的事
每張都寫了 `fair skin with visible skin pores, subtle natural skin texture,
slight oil sheen on T-zone, unretouched skin detail`，
並且明確禁用 `smooth` / `flawless` / `porcelain` / `airbrushed`。

**【我的結論】**：這一項方向正確，維持。

**🔴 不確定**：這些字在 300 字的長 prompt 裡是否還有效？
如果長度稀釋是真的，那**壓縮 prompt 時這一段應該優先保留**——請確認這個優先順序對不對。

---

## 六、我研究出的「網美攝影公式」— 需要覆核是否正確、以及能否轉成 prompt

以下是我從中文與英文攝影教學查到的結論。**請一併覆核這些攝影結論本身是否正確。**

### 6-1 機位高度

> 「很多人誤以為**鏡位越低越能拍出長腿，但其實這樣只會顯得腳大頭小**，呈現古怪的比例。
> 中鏡位（**鏡位高度約在肚臍處**）能讓身體比例最真實還原。」

**我的換算**：機位 = 身高 × 0.60。Luna 155cm → 93cm；Yuna 168cm → 101cm。

**🔴 不確定**：
- 「肚臍高度」這個說法在專業人像攝影裡是否成立？
- **這種指令要怎麼寫進 prompt 才有效？**
  我目前寫 `camera positioned about 100cm above the ground with the lens kept strictly horizontal`——
  **模型真的理解「離地 100 公分」這種絕對數值嗎？**
  還是應該改寫成相對描述（`camera at the subject's navel level`）？
  這是我最沒把握的一點。

### 6-2 顯腿長站姿

> 一腳自然往前伸出、重心往後腳偏移、一手插腰平衡身體、身體 3/4 側向鏡頭。

**🔴 不確定**：這種多部位、有因果關係的身體指令，在 75 字的限制下要怎麼寫？

### 6-3 破解僵硬：拿道具互動、不直視鏡頭

> 「覺得單純擺姿勢太僵硬，可以**拿點小道具互動**（書、咖啡、花束、手機），
> **不直視鏡頭**，假裝翻書、喝咖啡或看手機，瞬間拍出日常生活感。」
> 「**正面直視鏡頭會很僵硬**」，應改為「側身 ＋ 微笑回望」。

**【我的結論】**：這條解釋了我第二輪 Yuna 那張為什麼怪——她正面站著直視鏡頭。

### 6-4 表情的寫法

我發現一個現象：同一輪生成裡，
- Luna 的「**比 V ＋歪頭**」→ **成功做出來了**
- Yuna 的「**回眸一笑**」→ **完全沒做出來**（生成結果是面無表情正面站立）

**【我的推測】**：
- 「比 V」是**手勢**，是明確的視覺物件，模型容易抓
- 「回眸」是**身體與頭的相對關係**，需要模型理解 pose 的語義，難度高得多
- 而且我把 `EXPRESSION:` 和 `POSE:` 寫成**兩個獨立段落**，模型可能各吃一半

**🔴 不確定**：這個推測對嗎？如果對，**難以生成的姿勢（回眸、側身回望）
有沒有已知的有效寫法？**

---

## 七、我打算改用的新做法（最需要覆核的部分）

### 7-1 把「規格」與「prompt」徹底分開

| | 規格（給人看） | Prompt（給模型看） |
|---|---|---|
| 目的 | 確保思考完整、供人審核 | 精準有效地驅動模型 |
| 長度 | 不限，越詳細越好 | **30–75 字** |
| 內容 | 十個維度全寫 | **只留權重最高的幾項** |

### 7-2 Prompt 的優先順序（我的提案，請覆核）

在 75 字的限制下，我打算按這個順序留：

1. **相機 + 鏡頭 + 光圈**（研究說權重最高）
2. **皮膚質感關鍵字**（研究說每張必留）
3. **表情 + 姿勢，寫成一個連續動作**（不分兩段）
4. **主光的方向 + 一個具名的反射面**（五段式壓縮成兩段）
5. **服裝的關鍵三件**（不是五層）
6. **場景的三個識別元素**（不是一整串清單）
7. 構圖（景別 + 機位）

**砍掉**：身材數字（`soul_id` 應該已包含）、國籍、妝容細節、髮型細節、
場景的完整元素清單、光線的完整五段、微物件。

**🔴 這個取捨對嗎？** 特別是：
- 砍掉妝容細節會不會導致每張妝不一樣？
- 砍掉身材數字會不會讓體型跑掉？
- 光線壓縮成兩段還夠不夠？

### 7-3 改用參考圖控制場景

`soul_2` 支援 1 張參考圖。我打算用它來解決「場景生成到錯誤國家」的問題——
餵一張台灣街景照當參考，而不是用文字硬拗。

**🔴 不確定**：
- 當 `soul_id`（鎖人）與 `medias` 參考圖（鎖場景）同時使用時，兩者會衝突嗎？
- 參考圖會不會把裡面的**人物**也帶進來？
- 有沒有辦法只取參考圖的**場景與構圖**，不取人物？

---

## 八、兩個實際的 Prompt — 請直接批改

### 8-1 我第二輪實際送出的（約 330 字，失敗）

```
Candid street photograph taken in a narrow residential alley in Taipei, Taiwan. The subject is a
21-year-old woman of Korean descent living in Taipei, 168cm tall with a slim figure, bust 84 waist
58 hip 89, C cup, long legs at 82cm which is 48.8 percent of her height. Fair skin with visible skin
pores, subtle natural skin texture, slight oil sheen on her T-zone, unretouched skin detail. Mocha
brown hair in soft loose waves with see-through wispy bangs; her hair is mid-swing from turning, one
strand sweeping across her cheek. Korean 2026 makeup: sheer luminous base, soft straight brows,
low-contrast diffused milk-tea and apricot eyeshadow, a tiny V-shaped highlight in each inner eye
corner, ultra-thin inner eyeliner that is not winged, soft nose blush drifting across the bridge of
her nose, blurred diffused lips in muted greige-beige. EXPRESSION: she is caught mid
glance-back-and-smile — her eyes crinkle into crescents, lips slightly parted as if a laugh is just
escaping, chin tucked slightly. POSE: she was walking away and someone called her name, so her
weight is settled on her back foot with the front heel already lifted off the ground, her hips still
square to the direction she was walking while her upper body twists 30 degrees back toward the
camera, her right hand resting on the shoulder strap of her bag, her left arm hanging loose with
relaxed curved fingers; the open front panels of her long shirt and her hair are still trailing in
the momentum of the turn. WEARING: a white cropped fitted short-sleeve tee showing a sliver of
waist, an unbuttoned sheer off-white long-line open shirt worn as a layer over it with the hem
falling to mid-thigh and lifting in the movement, a low-rise light indigo denim mini skirt, black
mary jane shoes with white ankle socks, a thin gold necklace, small pearl earrings, a small black
mini box bag on a crossbody strap. ENVIRONMENT: a bright and pretty old Taiwanese alley, not a
run-down one — pale green and cream vintage tile walls, a long row of potted plants along the wall
base, warm-toned fabric awnings, a small shop with a wooden-framed glass door, a bicycle leaning
against the wall, bougainvillea trailing down from above. Vertical hanging shop signs in traditional
Chinese characters, rolling metal shutters, a covered arcade walkway, scooters with white Taiwanese
licence plates. This is Taiwan, NOT Korea and NOT Japan; no Korean hangul signage, no Japanese
signage. Two background pedestrians far down the alley facing away from camera, not looking at
camera, out of focus, visually distinct from her. LIGHTING: the key light is the late afternoon low
sun coming from the direction she is facing, striking her face from 45 degrees front-side, so her
face is one of the brightest areas in the frame; the pale tile wall behind her bounces a soft warm
rim of light along her hair and shoulder line, acting only as rim light and never as the key; split
colour temperature with warm gold sunlight against the cool blue shade under the awnings; exposure
is metered for her face so the far end of the alley and the sky clip out to white while her face
stays bright; the edge of a fabric awning cuts a soft shadow line across the top of the frame.
FRAMING: full body three-quarter view, camera positioned about 100cm above the ground at her waist
height with the lens kept strictly horizontal, neither tilted up nor angled down. Crisp sharp focus,
fine detail, natural colour grading, subtle film grain, shot on a 35mm lens.
```

**實際生成結果的問題**：
1. 場景是首爾（滿街韓文招牌），不是台北
2. 表情完全沒做出來——規格要「回眸一笑」，生成是面無表情正面站立
3. 姿勢也沒做出來——規格要「走路被叫住回頭」，生成是正面站著單腳抬起
4. 服裝部分跑掉（迷你裙變成短褲）

### 8-2 我打算改成的（約 70 字，未測試）

```
Full-body candid street photo, shot on Canon EOS R5, 85mm f/2.0 from 4 metres, camera at her navel
level, lens horizontal. A young woman glances back over her shoulder mid-stride and smiles, eyes
crinkling, one hand on her bag strap, sheer open shirt trailing in the turn. White cropped tee,
denim mini skirt, mary janes. Bright Taipei alley: pale green tile walls, potted plants, traditional
Chinese vertical shop signs. Low sun in front of her lighting her face. Visible skin pores, natural
skin texture, film grain.
```

**請批改這一版：**
- 這樣的壓縮合理嗎？砍掉的東西會不會出問題？
- 順序對嗎？（我把相機放最前面）
- 「camera at her navel level」這種相對描述，比「100cm above the ground」有效嗎？
- 「glances back over her shoulder mid-stride」這個寫法能生出回眸嗎？
- 還有什麼明顯的錯誤？

---

## 九、集中的問題清單

請逐題回答：

1. **30–75 字的建議對 Higgsfield Soul 2.0 這類「已鎖定身分」的商用模型適用嗎？**
   若不適用，合理長度是多少？
2. 在長度限制下，**十個規格維度應該保留哪幾個、砍掉哪幾個**？我第 7-2 節的排序對嗎？
3. **`soul_id` 鎖定的範圍**是只有臉，還是也含體型？prompt 裡還需不需要寫身材數字與族裔？
4. 既然 `soul_2` **沒有 negative prompt 欄位**，處理「不要出現 X」有沒有其他有效手段？
5. **絕對數值的相機指令（「離地 100 公分」）模型讀得懂嗎？**
   還是相對描述（「在她肚臍高度」）比較有效？
6. **寫具體機身型號**（Canon EOS R5）對閉源商用模型是否有效，還是安慰劑？
7. **「回眸」這類需要身體配合的姿勢，有沒有已知有效的寫法？**
   為什麼同一輪裡「比 V」成功而「回眸」失敗？
8. **同時使用 `soul_id`（鎖人）與參考圖（鎖場景）會衝突嗎？**
   能不能只取參考圖的場景不取人物？
9. 我研究出的**攝影公式本身**（機位＝肚臍高度、全身用 85mm、腳貼下 1/3、
   一腳前伸＋重心後腳＋插腰）**有沒有錯的地方？**
10. **有沒有我完全沒想到、但對這個任務很關鍵的東西？**

---

## 十、附錄：本專案目前的完整規格結構

供覆核者理解我目前一件素材寫到多細。以 `YG-06` 為例，規格有這些欄位：

| 欄位 | 內容範例 |
|---|---|
| 妝容 | 透明感水光底妝；奶茶＋杏桃低對比暈染；眼頭小 V 字打亮；極細內眼線不上揚；nose blush 橫過鼻樑；blurred lips 帶灰調的米棕 |
| 髮型 | mocha brown 長軟波浪，see-through 空氣瀏海，轉身時髮尾被帶起、一撮掃過臉頰 |
| 穿著 | 上身／外層／下身／鞋／首飾 五層，每層具體到單品＋材質＋顏色，並要求至少一個「會飄的元素」 |
| 場景環境 | 淺綠與米色老磁磚牆、整排盆栽、暖色遮陽棚、木框玻璃門小店、腳踏車、九重葛 |
| 機位與構圖 | 全身；機位離地 101cm（肚臍高度），鏡頭水平、地平線不歪；85mm，距離 4 公尺；腳貼下 1/3，上方留 1/4，三分線偏左 |
| 光線（五段） | ① 具名主光＋方向 ② 具名反射面 ③ 色溫分裂 ④ 曝光取捨（哪裡過曝） ⑤ 遮擋框架 |
| 表情 | 回眸一笑——轉頭瞬間眼睛彎成月牙，嘴唇微開像正要笑出聲，髮尾還在甩動軌跡上 |
| 肢體與重心 | 重心壓後腳，前腳腳跟離地；骨盆朝前進方向、上半身轉 30 度；右手扶包帶；左手垂放；襯衫下襬與髮尾在慣性裡飄 |
| 情境 | 走在巷子裡，有人在後面叫她，轉頭的那一秒 |
| Caption | 這條巷子很好走✨／每天都繞過來 |

**這十個維度是為了「人審核時思考完整」而設計的。
問題是我把它們原封不動翻譯成英文送進模型，變成 330 字的 prompt。**

---

## 十一、來源

攝影：
- <https://www.marieclaire.com.tw/entertainment/news/56064>（IU 長腿拍照技巧）
- <https://blog.magipea.com/photography003/>（顯腿長拍照技巧）
- <https://www.daf-shoes.com/product/pageSet/3111>（四大拍照技巧）
- <https://hahow.in/contents/articles/663b7047c9a50c25581f0167>（網美拍照姿勢教學）
- <https://gofunit.com/拍照姿勢/>（30 個網美 POSE）
- <https://www.theartistgallery.art/post/best-focal-length-for-street-photography>

Prompt 方法：
- <https://artsmart.ai/blog/ai-image-prompts-photorealistic/>（30–75 字、相機規格權重）
- <https://aivideobootcamp.com/blog/photorealistic-ai-prompts-guide-2026/>
- <https://stable-diffusion-art.com/how-to-use-negative-prompts/>
- <https://arxiv.org/pdf/2406.02965>（Understanding the Impact of Negative Prompts）
- <https://kawaiipromptlab.com/en/tips/negative-prompt-guide/>（CFG > 1.0 機制）

模型參數：Higgsfield `models_explore(action='get', model_id='soul_2')` 實際回傳
