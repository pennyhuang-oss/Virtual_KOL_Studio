# 批次一 20 段 Prompt — 送生成前的外部覆核

> **這份文件是要請 ChatGPT（或其他模型）覆核用的。生成前的最後一道關卡。**
> 專案：Virtual KOL Studio｜模型：Higgsfield Soul 2.0（`soul_2`）＋ 已訓練的 `soul_id`
> 日期：2026-08-27

## 給覆核者：請幫我看什麼

下面有 20 段英文 prompt，是兩個虛擬 KOL 的 Instagram 素材，**核准後就會直接送去生成，每張約 0.12 credits。**
先前已經連續三輪被退，使用者的原話是：「你一直出錯，我完全就是一直在燒 credit。」
所以這一關的目的很明確——**在花錢之前把錯抓出來。**

請針對每一段（或整體）指出：

1. **會生錯的地方**——哪一句模型大概率不會執行，或會執行成別的東西
2. **漏掉的必要資訊**——像「沒寫髮長」這種，少了就會被模型自由發揮的欄位
3. **互相衝突的指令**——同一段裡打架的描述
4. **多餘的字**——會稀釋關鍵字權重、可以刪掉的部分
5. **順序問題**——哪些資訊應該往前挪

**特別請注意第三節「還沒驗證的假設」——那幾條是我猜的，最需要被質疑。**

---

## 一、模型的硬限制（實測參數表，不是推測）

```json
{
  "id": "soul_2",
  "parameters": [
    { "name": "quality", "options": ["1.5k", "2k"] },
    { "name": "soul_id", "description": "Soul-ID for personalized generation" }
  ],
  "medias": [ { "name": "medias", "type": "image", "max": 1 } ],
  "aspect_ratios": ["1:1","16:9","9:16","4:3","3:4","3:2","2:3"]
}
```

可調的只有：`quality`、`soul_id`、`aspect_ratio`、`prompt`、1 張參考圖。

- **沒有 negative prompt 欄位**
- **沒有 seed 欄位**（所以同一段 prompt 送兩次結果就不一樣，無法完全重現）
- `soul_id` 已經鎖住臉與體型

---

## 二、今天實測驗證過的結論（6 張，0.72 credits）

**這一節是已經花錢驗過的，不需要再討論，列出來是讓覆核者知道基準線在哪。**

| 結論 | 證據 |
|---|---|
| **不寫族裔與身材數字也 OK** | 6 段 prompt 都沒寫族裔、身高、三圍、罩杯，臉與身材都正確。`soul_id` 鎖得住 |
| **相機用相對描述有效** | `camera at her navel level, lens horizontal, shot from well back` → 6/6 比例正確，沒有頭大腿短、沒有俯拍。**先前寫絕對公分數（101cm）反而失敗** |
| **否定句完全無效** | 明寫 `no open sky`、`no distant vanishing point` → 生出來照樣是開闊天空。要排除什麼只能改成正面描述 |
| **正向的曝光描述有效** | `background exposed the same brightness as her skin` → 室內 3 張都不逆光。先前用「曝光取捨（哪裡過曝）」的寫法，每張都燒白背景 |
| **表情必須綁實體動作** | 比 V ✅／捧杯遮嘴＋眨眼 ✅／回眸一笑 ❌／單眼瞇起＋嘴巴微張 ❌。**跟寫得細不細無關，只跟有沒有物件可掛有關** |
| **身體姿勢做得出來，純臉部表情做不出來** | 同一段裡「側身回眸」的身體扭轉成功，同一句的「笑到眼睛彎」失敗 |
| **`soul_id` 會鎖住整套場景模板** | 其中一個角色只要 prompt 提到「巷弄街拍」，就生出同一條街、同一個機位、同一個消失點，連明寫「背景不要有天空」都無效。**已因此換掉一件 spec** |
| **「會飄的元素」做不出來** | 3/3 失敗——薄襯衫兩次整件消失、裙子沒被風掀起。靜態圖大概無法表現「正在飄」 |
| **沒寫髮長就會生出長短不一的頭髮** | 一段沒提頭髮的 prompt，把及下巴的鮑伯生成一邊到肩、另一邊長到腰 |

---

## 三、還沒驗證的假設 —— 🔴 **最需要覆核的部分**

| # | 我的假設 | 為什麼不確定 |
|---|---|---|
| 1 | 加 `both sides exactly the same length` 可以修好鮑伯長短不一 | **完全沒測過。**而且這是「用正面描述表達一個對稱性約束」，不確定模型讀不讀得懂 |
| 2 | `almost no shadows` 可以留著 | 它字面上是否定句，但實測用它的那張確實生出平光。我判斷它是「光質描述」不是「排除指令」——**這個判斷對嗎？** |
| 3 | 92–128 字是合理長度 | 實測成功的都在 80–110 字，但沒有做過長度的對照實驗（原計畫有，被跳過了） |
| 4 | 動作／瞬間放在第一句比較好 | 測了一組（用字完全相同、只換順序），差 1 分，**低於預設門檻，未分出勝負** |
| 5 | 另一個角色沒有場景模板問題 | 只測 1 張，n=1 不能下定論 |
| 6 | 服裝清單排最後的品項容易被丟掉 | 觀察到但沒有單獨測過 |

---

## 四、20 段 Prompt 全文

**共用設定**：`model: soul_2`、`quality: 2k`、`aspect_ratio: 9:16`、一段 prompt 生一張。
**兩人的 `soul_id` 不同**，prompt 裡都不寫族裔與身材。


### Yuna Kim（韓籍，長髮）｜10 件

主場是室內冷白光——咖啡廳、梳妝台、公寓窗邊、超商、早餐店、汗蒸幕。
**先前把她排成街拍，實測撞上 `soul_id` 的場景模板，已全數改成室內或有遮蔽的場所。**

#### YG-01｜咖啡廳靠窗・臉部近景

- 景別：臉部＋肩膀近景
- 表情設計：撥髮回眸。一手正把頭髮撥到耳後，同時轉頭看鏡頭；嘴角單邊上揚的淺笑；頭往撥髮的那一側微傾。

```
A young woman tucks a strand of hair behind her ear and turns to look at the camera, a one-sided smile, head tilted toward that hand. Close-up of face and shoulders, camera at her eye level, lens horizontal. Collarbone-length soft wavy mocha brown hair with see-through wispy bangs, one side tucked behind her ear. Cream fitted fine-knit tee, thin gold necklace, small gold hoops. Bright cafe window seat, white wall, pale wood table, a latte and her phone. Soft cool daylight from her front-left landing on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### YG-02｜台北公寓窗邊晨光

- 景別：3/4 身（膝上）
- 表情設計：端著杯子瞇眼笑。雙手捧著馬克杯舉到嘴邊喝一口，眼睛還沒完全張開、瞇成細細的；嘴角鬆鬆揚起。

```
A young woman stands at the window holding a mug with both hands and lifts it to her mouth, eyes still narrowed from sleep, a loose easy smile. Three-quarter body, camera at her navel level, lens horizontal, shot from well back. Collarbone-length mocha brown hair, sleep-mussed, see-through bangs flattened with one tuft sticking up. White fitted camisole, high-waisted grey cotton shorts, beige cardigan slipping off one shoulder, bare feet. Small bright apartment, white walls, pale wood floor, unmade white bed. Soft morning light on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### YG-03｜超商・「今天學到一個字」

- 景別：半身自拍
- 表情設計：憋笑破功。念錯字後抿著嘴想忍住，忍不住笑出來、眼睛瞇成一條線；一手摀在嘴前。

```
A young woman points at the oden label board with one hand and claps the other over her mouth, laughing until her eyes squeeze shut. Half-body selfie, phone held out at arm’s length just above her eye level. Mocha brown hair in a low ponytail with see-through bangs and loose strands at her temples. Cropped grey tee showing a sliver of waist, high-waisted black shorts, black-rimmed glasses. Taiwanese convenience store, fluorescent ceiling tubes, drinks fridge, steaming oden counter, snack shelves. Flat even fluorescent light on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### YG-04｜梳妝台護膚・素顏

- 景別：臉部＋上半身近景，拍鏡中反射
- 表情設計：閉眼享受。眼睛完全閉起、眉頭鬆開；嘴角放鬆地微揚；下巴微抬（把精華液按進臉頰的那一下）。

```
A young woman presses serum into her cheek with her fingertips, eyes closed, chin lifted, mouth relaxed into a small smile. Close-up of her face and shoulders reflected in the mirror, camera at her eye level, lens horizontal. Mocha brown hair clipped back with a claw clip, a few strands loose at her forehead. White fitted camisole. White marble bathroom counter, square mirror, white tiled wall, skincare bottles and brushes left unarranged. Cool white even light on her face with almost no shadows, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### YG-05｜捷運月台・隨手自拍

- 景別：半身自拍
- 表情設計：手機舉在臉側嘟嘴。一手把手機舉在臉頰旁，另一手把瀏海撥開；韓系無聊嘟嘴，眼神平淡。

```
A young woman holds her phone up beside her face and pushes her fringe aside with her free hand, pouting flatly at the lens. Half-body selfie, phone held out at arm’s length just above her eye level. Collarbone-length sleek straight mocha brown hair, side-parted. Fitted black short-sleeve knit, khaki high-waisted mini skirt, beige mini box bag. Metro platform, yellow safety line, platform screen doors, route map lightbox, ceiling tubes. Flat even station light on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### YG-06｜汗蒸幕・甜米露

- 景別：全身（坐姿）
- 表情設計：上目遣い。雙手捧著甜米露的紙杯擋在下巴前，只露出眼睛越過杯緣往上看鏡頭；眼睛彎起來。

```
A young woman sits cross-legged on a heated wooden floor holding a paper cup of sweet rice punch with both hands in front of her chin, looking up at the camera over the rim, eyes crinkled into crescents. Full body, camera at her seated eye level, lens horizontal, shot from well back. Mocha brown hair in a low bun with two damp strands at her temples. Grey jjimjilbang tee and shorts, a towel folded into sheep horns on her head, bare feet. Korean sauna rest hall, wooden floor, low tables, warm ceiling light on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### YG-07｜客廳地板・什麼都沒發生

- 景別：半身坐姿
- 表情設計：邊吃邊被拍到。嘴裡還有零食、一邊臉頰鼓著；眼睛圓睜看鏡頭，眉毛抬起像在說「幹嘛拍我」。

```
A young woman sits on the living room floor scrolling her phone and reaching into a snack bag, caught mid-chew with one cheek full, eyebrows raised at the camera. Half body, camera level with her face as she sits on the floor, lens horizontal. Collarbone-length mocha brown hair, the top half clipped up and the lower half loose. Beige camisole, matching short cotton shorts, bare feet. Small apartment living room, low sofa, magazines open on the floor, an electric fan turning in the corner. Soft window light on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### YG-08｜台式早餐店・第一則吃

- 景別：半身，人＋食物同框
- 表情設計：吃到好吃的。咬一口後眼睛彎成月牙、鼻子微微皺起；空著的手對鏡頭比大拇指。

```
A young woman bites into an egg crepe and throws a thumbs up with her free hand, eyes crinkling into crescents, nose slightly scrunched. Half body with the food in frame, camera level with her chest, lens horizontal. Collarbone-length soft wavy mocha brown hair, side-parted, a small pearl clip on one side. Light blue shirt with the top two buttons open and the hem knotted at her waist, white high-waisted shorts. Taiwanese breakfast shop, stainless steel counter, red plastic chairs, handwritten wall menu, iced tea in a glass. Daylight from the doorway on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### YG-09｜飯店窗邊・皮膚特寫

- 景別：臉部大特寫
- 表情設計：放空側臉。眼睛看著窗外遠處、不看鏡頭；嘴唇自然放鬆；睫毛半垂——這件刻意不做表情。

```
A young woman leans against the window frame gazing out at the city, her eyes following something far outside the glass, lashes lowered, lips relaxed. Tight close-up of her face, camera at her eye level, lens horizontal. Wet mocha brown hair pushed straight back, collarbone length, water still beading at the ends. White bathrobe with the collar loosened. Hotel room, white bedding, floor-to-ceiling window, city towers and a river blurred outside. Soft even daylight full on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### YG-10｜百貨美妝櫃・精緻的一面

- 景別：半身
- 表情設計：舉起試色的手背挑眉。試完色把手背舉到鏡頭前，同時抬眼、一邊眉毛挑起、同側嘴角上揚。

```
A young woman swatches lipstick on the back of her hand and lifts it toward the camera, raising one eyebrow with a one-sided smile. Half body, camera level with her chest, lens horizontal. Sleek glossy mocha brown hair, side-parted, collarbone-length with the ends curving slightly inward. Cream cropped fitted knit top, matching off-white high-waisted straight trousers, a trench coat over her arm, gold hoop earrings. Department store beauty floor, glass counters, rows of lipsticks, mirrored columns. Even ceiling light on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```


### Luna Tanaka（日籍，及下巴鮑伯）｜10 件

東京可愛系方向：明亮、乾淨、甜點店、花季、遊樂園、浴衣祭典。
**她的髮型是鮑伯，就是出現長短不一瑕疵的那位——每段都加了兩側等長的描述，但那個修法還沒驗證過。**

#### LG-01｜甜點店靠窗・臉部近景

- 景別：臉部＋肩膀近景
- 表情設計：雙手托腮＋歪頭笑。手肘撐在桌上、雙手托著兩頰把臉擠得更圓；頭往一側傾 20 度；眼睛彎起來。

```
A young woman looks down at a strawberry cake then lifts her eyes to the camera, both hands cupping a latte in front of her chin, smiling with her eyes. Close-up of face and shoulders, camera at her eye level, lens horizontal. Chin-length blunt black bob, centre-parted, both sides exactly the same length, ends curving slightly inward. Cream square-neck puff-sleeve top, small pearl earrings. Bright dessert shop window seat, white tiled wall, pale wood table, a small bunch of dried flowers. Soft daylight from her side landing on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### LG-02｜房間晨光・第一則「她在台北」

- 景別：3/4 身（膝上）
- 表情設計：剛睡醒揉眼睛。一手揉著眼睛、另一眼半睜；嘴巴打呵欠打到一半；整張臉是鬆的。

```
A young woman crouches down and touches a patch of sunlight on the floor with her fingertips, her other hand rubbing one eye, mouth caught mid-yawn. Three-quarter body, camera level with her face as she crouches, lens horizontal, shot from well back. Chin-length black bob, both sides exactly the same length, sleep-mussed with one side flattened. White lace-trimmed camisole pyjama top, matching short pyjama shorts, bare feet. Bright clean studio room, white walls, pale wood floor, a small plant and a plush toy by the window, a half-unpacked box in the corner. Soft morning light on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### LG-03｜Mochi 在台北的窗台

- 景別：半身＋貓同框
- 表情設計：臉靠近貓瞇眼笑。臉貼近貓的頭、眼睛瞇成月牙；嘴角上揚；完全不看鏡頭，注意力全在貓身上。

```
A young woman leans in close to an orange cat on the windowsill and scratches its head, her eyes crinkled shut in a smile, attention entirely on the cat. Half body with the cat in frame, camera level with her face as she sits, lens horizontal. Chin-length black bob, both sides exactly the same length, one side tucked behind her ear. Off-white fitted fine-knit top, light shorts. Bedroom windowsill, small potted plants, an iron window grille and the apartment across the street outside. Soft window light on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### LG-04｜花季公園・櫻花

- 景別：半身
- 表情設計：驚訝張嘴＋笑。花瓣落到手上的瞬間眼睛睜大、嘴呈小 O 形，然後笑出來；眉毛抬高。

```
A young woman reaches up with an open palm to catch a falling petal, eyes wide and mouth in a small O, eyebrows lifted, just breaking into a laugh. Half body, camera level with her chest, lens horizontal. Chin-length blunt black bob, both sides exactly the same length. White square-neck fitted lace top, pale pink checked mini skirt, a cream cardigan over her shoulders, a cream ribbon headband, pearl earrings. Park path under blossoming branches hanging into the top of the frame, petals on her shoulder. Soft daylight on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### LG-05｜公車站・雨停前

- 景別：3/4 身（膝上）
- 表情設計：對鏡頭比 V ＋歪頭。手比 V 舉在臉頰旁；頭往同側傾；眼睛彎成月牙——雨天也很開心的那種笑。

```
A young woman stands at the edge of a bus shelter holding a folded clear umbrella still dripping, tilts her head and makes a V sign beside her cheek, eyes crinkled. Three-quarter body, camera at her navel level, lens horizontal, shot from well back. Chin-length centre-parted black bob, both sides exactly the same length. Off-white fitted shirt with the top buttons open, pale blue checked skirt, pale blue cardigan over her shoulders, white mary janes with lace socks, canvas tote. Bus shelter with a colourful route map lightbox, raindrops on the glass, warm shop signs glowing across the street, wet asphalt reflecting the colours. Bright clear light after rain on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### LG-06｜可愛系街區・扭蛋機前

- 景別：半身
- 表情設計：捧著扭蛋嘟嘴笑出來。雙手捧著打開的扭蛋，眉毛垮下、嘴嘟起來，下一秒忍不住笑出來、眼睛瞇起。

```
A young woman holds an opened gachapon capsule in both hands, her eyebrows dropping into a pout and breaking into a laugh, eyes squeezed shut. Half body, camera level with her chest, lens horizontal. Chin-length black bob, both sides exactly the same length, two small clips holding her fringe back. Pale pink cropped knit top showing a sliver of waist, white high-waisted shorts, a denim jacket tied at her waist. A row of colourful gachapon machines behind her, bright shop signage, clean pavement. Soft daylight on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### LG-07｜遊樂園・旋轉木馬

- 景別：全身
- 表情設計：抱著爆米花桶回頭吐舌眨眼。雙臂抱著爆米花桶靠在胸前，身體背對、頭轉回鏡頭；舌尖輕吐、單眼眨眼。

```
A young woman hugs a popcorn bucket against her chest with both arms and turns back to the camera over her shoulder, tongue tipped out and one eye winking. Full body, camera at her navel level, lens horizontal, shot from well back. Chin-length black bob, both sides exactly the same length, a cat-ear headband. White square-neck puff-sleeve top, pale blue pinafore skirt, white mary janes with lace socks, a small backpack. Amusement park beside the carousel, coloured balloons, a decorated parade street behind. Soft daylight on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### LG-08｜浴室鏡前・濕髮

- 景別：半身，拍鏡中反射
- 表情設計：咬著毛巾角鼓臉頰。擦頭髮擦到一半停下來，用牙齒咬著毛巾一角，對著鏡子鼓起臉頰。

```
A young woman stops drying her hair and bites one corner of the towel between her teeth while looking at herself in the mirror, cheeks puffed out. Half body reflected in the mirror, camera at her eye level, lens horizontal. Wet chin-length black bob clinging to her cheeks, both sides exactly the same length. A white bath towel wrapped around her. Clean bright bathroom, white square tiles, a wooden-framed mirror with a little steam at one corner, a hanging white towel, skincare bottles on the counter. Cool white even light on her face with almost no shadows, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### LG-09｜台式早餐店・豆漿

- 景別：半身，人＋食物同框
- 表情設計：上目遣い。頭略低、眼睛往上看鏡頭；雙手捧著杯子在下巴前；嘴角微揚——日系經典。

```
A young woman holds a glass of soy milk with both hands in front of her chin and looks up over the rim at the camera, smiling with her eyes. Half body with the food in frame, camera level with her chest, lens horizontal. Chin-length centre-parted black bob worn loose, both sides exactly the same length. Cream fitted thin-knit short sleeve, a light mini skirt, a canvas tote on the chair back. Taiwanese breakfast shop, stainless steel counter, a metal tray, handwritten wall menu, plastic chairs. Daylight from the doorway on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

#### LG-10｜浴衣・夏日祭典

- 景別：全身＋半身各一
- 表情設計：拿著蘋果糖回頭笑。一手把蘋果糖舉在臉頰旁、另一手扶著髮簪，身體背對參道、頭轉回鏡頭；笑到眼睛彎。

```
A young woman turns back over her shoulder holding a candy apple up beside her cheek, laughing with her eyes crinkled, her free hand steadying the pin in her bun. Full body, camera at her navel level, lens horizontal, shot from well back. Chin-length black bob half-pinned up with a Japanese hairpin, two strands left at her temples. Pale blue yukata with a white morning-glory print, a navy half-width obi tied tight at the waist, wooden geta and white tabi, a small drawstring pouch. Festival approach to a shrine, a clean bright wooden torii, paper lanterns strung overhead, food stalls, a blurred crowd. Warm lantern light on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, film grain.
```

---

## 五、具體想請教的問題

1. **第三節那六條假設，哪幾條你認為是錯的？**
2. **`both sides exactly the same length` 這種對稱性約束，有沒有更可靠的寫法？**
   （模型沒有 negative 欄位，不能寫 `not asymmetric`）
3. **`almost no shadows` 該留還是該改？**如果該改，改成什麼？
4. **這 20 段裡，哪幾段最可能生錯？** 請指名並說明會錯在哪。
5. **有沒有哪一段的資訊順序明顯不對？**
6. **有沒有共通的、20 段都犯的問題？**（像「沒寫髮長」那種——這次已經修了，但可能還有別的同類漏洞）
7. **既然 `soul_id` 會鎖住場景模板，有沒有辦法在不重訓的前提下換掉場景？**
   那張唯一的參考圖（`medias`）是目前完全還沒用過的手段。
8. **靜態圖真的做不出「衣服正在飄」嗎？**
   有沒有已知有效的寫法（例如描述成「已經被吹起的狀態」而不是「正在飄」）？
9. **有沒有我完全沒想到、但對這個任務很關鍵的東西？**

---

## 六、附錄：一個已知失敗的反例（供對照）

這是先前失敗的寫法，約 330 字。生出來的問題：場景在錯誤的國家、指定的表情完全沒做出來、
指定的姿勢沒做出來、迷你裙變成短褲。**列在這裡是讓覆核者看到「壞的長什麼樣」。**

```
Candid street photograph taken in a narrow residential alley in Taipei, Taiwan. The subject is a
21-year-old woman of Korean descent living in Taipei, 168cm tall with a slim figure, bust 84 waist
58 hip 89, C cup, long legs at 82cm which is 48.8 percent of her height. ... EXPRESSION: she is
caught mid glance-back-and-smile — her eyes crinkle into crescents ... This is Taiwan, NOT Korea and
NOT Japan; no Korean hangul signage, no Japanese signage. ... FRAMING: full body three-quarter view,
camera positioned about 100cm above the ground at her waist height ... shot on a 35mm lens.
```

已知的四個病灶：**太長**、**寫了族裔與身材數字**、**用否定句排除國家**、**寫絕對公分數與廣角焦段**。
第四節那 20 段是在避開這四點的前提下寫的——**請確認我有沒有避開，以及有沒有換出新的問題。**
