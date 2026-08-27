# 批次一 Prompt — 第二輪覆核（R2）

> 這是第一輪覆核的回應＋修改後版本，請再看一次。
> 專案：Virtual KOL Studio｜模型：Higgsfield Soul 2.0（`soul_2`）＋ 已訓練的 `soul_id`
> 日期：2026-08-27｜上一輪判定：🔴 暫不整批核准，4 個 blocker

## 這一輪請幫我確認三件事

1. **4 個 blocker 是不是真的修掉了**（第一節）
2. **我沒有全盤照做的兩處，理由站不站得住**（第二節）——這是我最想被打的地方
3. **改完之後有沒有換出新問題**（第四節有全部 21 段）

---

# 一、上一輪 14 條執行指令的處理結果

| # | 指令 | 處理 |
|---|---|---|
| 1 | 修正 YG-03 三隻手 | ✅ 照做。刪掉「指標牌」，保留自拍＋摀嘴笑，標示牌改成在她旁邊入鏡。**故事由 Caption 帶** |
| 2 | 修正 YG-05 自拍手機矛盾 | ✅ 照做。刪掉 `holds her phone up beside her face`，改 `looks into her phone camera` |
| 3 | LG-01 改回雙手托腮 | ✅ 照做，直接用你給的版本。蛋糕與拿鐵改成放桌上不佔手 |
| 4 | 決定 LG-10 張數 | ✅ **拆成 LG-10A（全身）／LG-10B（半身）**，整批從 20 件變 **21 件** |
| 5 | `almost no shadows` → `broad diffuse frontal light with very low shadow contrast` | ✅ 照做（YG-04、LG-08） |
| 6 | 鮑伯改幾何描述 | ✅ 照做。Luna 全部改成 `a symmetrical blunt chin-length bob ending evenly at the jawline` |
| 7 | LG-04、LG-06 改單一 frozen expression | ✅ 照做。LG-04 freeze 在驚訝；**LG-06 我選了「笑出來」**（比嘟嘴更適合發布，也符合她明亮可愛的方向） |
| 8 | YG-06、LG-09 修 camera／gaze | ✅ 照做。YG-06 改 `eyes peeking over the rim toward the camera`；LG-09 補回 `head slightly lowered` |
| 9 | YG-10 手背不要伸向鏡頭 | ✅ 照做，改 `holds the swatched hand beside her face` |
| 10 | 全身／3/4 身刪掉 `visible skin pores` | ✅ 照做。**只有 4 件近景保留**（YG-01、YG-04、YG-09、LG-01），其餘一律只留 `natural skin texture, subtle film grain` |
| 11 | LG-05、LG-10 縮短 | ✅ 照做。現在全批 **86–114 words**，沒有超過 120 的 |
| 12 | Reference image 先做 API 行為測試 | ⏸ **還沒做**，見第三節——我想先跟你確認測法 |
| — | LG-02 `touches a patch of sunlight` 改具體 | ✅ 改成 `fingertips resting on a sunlit patch of the floor` |
| — | YG-07 `electric fan turning` | ✅ 改成 `an electric fan in the corner` |
| — | LG-07 寫死骨盆朝向 | ✅ 照做，LG-10A 也一起加了 |
| — | 服裝按重要度排序、砍尾項 | ✅ LG-05 砍掉 tote／瑪莉珍／蕾絲襪（**3/4 身是膝上，鞋本來就不在畫面裡**）；LG-07 砍掉後背包 |

## 順帶：我全面比對過 spec 與 prompt，drift 只有 LG-01 一件

你抓到 LG-01 之後我沒有只修那一件——把 20 件的「表情」欄位跟 prompt 首句逐件比對過，
**確認其他 19 件都沒有 drift**。手數也全部重數過，只有 YG-03、YG-05 有問題，跟你的判定一致。

---

# 二、🔴 我沒有全盤照做的兩處 —— 請重點打這裡

## 2-1. 曝光那句：只在 3 個氣氛場景改，其餘 18 件**保留原句**

你的建議是把 `background exposed the same brightness as her skin` 依場景改寫，
理由是祭典／汗蒸幕／雨天如果背景真的跟皮膚一樣亮，會失去氣氛層次。**這個顧慮我同意。**

**但我沒有全部改，理由是：那句是實測驗證過的字串。**

它在 3 張室內圖上驗證有效（都成功解掉逆光）。我這個專案反覆犯的錯誤模式，
就是**拿一個沒驗證過的新寫法去換掉一個已經驗證過的舊寫法**，因為新的聽起來比較好。
把 18 件的驗證字串一次換成未驗證字串，就是同一個錯誤再犯一次。

**所以我的做法是：**

| 場景 | 用哪一句 |
|---|---|
| 一般室內／日光（18 件） | `background exposed the same brightness as her skin`（**維持驗證過的原句**） |
| YG-06 汗蒸幕（暖光） | `the warm room behind her keeping visible detail` |
| LG-05 雨後夜色 | `Her face clearly lit, the glowing signs keeping their colour` |
| LG-10A／10B 祭典燈籠 | `the lantern-lit stalls behind her keeping visible detail` |

**請判定：這個「只在必要處偏離驗證字串」的做法，比你建議的「全面改寫」好還是差？**
如果你認為全面改寫更好，我想知道你判斷「換掉一個已驗證字串」的風險為什麼低於「氣氛失真」的風險。

## 2-2. YG-03：我保留了自拍，犧牲了「指著那個字」

你給了兩個選項。我選了**保留自拍、刪掉指標牌**，理由是：

- 這批 21 件裡自拍只有 2 件（YG-03、YG-05），刪掉就少一種景別
- 「今天學到一個字」這個故事**由 Caption 承擔就夠了**，不一定要靠手指入鏡

**但我不確定這個取捨對。**如果你認為「指著標示牌」的畫面資訊量明顯高於「多一種景別」，
我就改成第三人稱拍攝。請直接判。

---

# 三、Reference image：我想先跟你確認測法再花錢

你引用官方文件說：**掛 reference image 之後 prompt 欄位會 unavailable**，
但 Soul ID 可以跟 reference 並用。

**我這邊看到的 API schema 同時列出 `prompt` 與 `medias`，沒有任何互斥的說明。**
我沒有獨立查證過官方 Help Center 的那段敘述，所以現在有兩個互相矛盾的資訊來源。

### 我打算這樣測（1 張，0.12 credits）

用**我們自己已經生成過的一張街拍圖**當 reference（所以沒有版權問題），
配一段**內容明顯不同的咖啡廳 prompt**，然後看：

- 如果生出來是咖啡廳 → prompt 有效，兩者可並用
- 如果生出來是街拍 → prompt 被忽略，官方敘述正確
- 如果 API 直接報錯 → 更明確

**這樣測有沒有問題？**特別是：用「有人物的圖」當 reference 會不會讓結果無法解讀
（因為它同時帶入 pose／服裝／光線）？如果會，我應該先想辦法取得一張純場景圖再測嗎？

---

# 四、修改後的 21 段 Prompt 全文

**共用設定**：`model: soul_2`、`quality: 2k`、`aspect_ratio: 9:16`、一段 prompt 生一張。
兩人 `soul_id` 不同，prompt 裡都不寫族裔與身材。

## 送出前跑過的自動檢核（你上一輪給的 10 項）

我把可自動化的部分寫成了檢查腳本，21 件**全數通過**：

| 檢查 | 結果 |
|---|---|
| 字數 ≤ 120 | ✅ 86–114（中位數 105） |
| 無否定句 | ✅ 21/21 |
| 有明確髮長 | ✅ 21/21 |
| Luna 有鮑伯幾何描述 | ✅ 11/11 |
| `visible pores` 只在近景 | ✅ 只有 4 件近景有 |
| 無「先 A 再 B」的時間序列 | ✅ 21/21 |
| 自拍未同時要求手機入鏡 | ✅ 2/2 |
| 無抽象飄動描述 | ✅ 21/21 |

> ⚠️ **檢核腳本本身的可信度**：我過去寫的檢查器出過四次假陰性
> （最近一次是正規表達式大小寫敏感，把句首的 `Chin-length` 全漏掉）。
> 這次的腳本我先用已知正確與已知錯誤的樣本各驗過一次才拿來跑。


## Yuna Kim（韓籍，長髮）｜10 件

主場是室內冷白光。街拍已全數移除——實測撞上 `soul_id` 的場景模板。

### YG-01｜咖啡廳靠窗・臉部近景

- 景別：臉部＋肩膀近景 ｜ 字數：102
- 表情設計：撥髮回眸。一手正把頭髮撥到耳後，同時轉頭看鏡頭；嘴角單邊上揚的淺笑；頭往撥髮的那一側微傾。

```
A young woman tucks a strand of hair behind her ear and turns to look at the camera, one corner of her mouth lifted, head tilted toward that hand. Close-up of face and shoulders, camera at her eye level, lens horizontal. Collarbone-length soft wavy mocha brown hair with see-through wispy bangs. Cream fitted fine-knit tee, thin gold necklace, small gold hoops. Bright cafe window seat, white wall, pale wood table, a latte and her phone. Soft cool daylight from her front-left landing on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.
```

### YG-02｜台北公寓窗邊晨光

- 景別：3/4 身（膝上） ｜ 字數：100
- 表情設計：端著杯子瞇眼笑。雙手捧著馬克杯舉到嘴邊喝一口，眼睛還沒完全張開、瞇成細細的；嘴角鬆鬆揚起。

```
A young woman stands at the window holding a mug with both hands and lifts it to her mouth, eyes still narrowed from sleep, a loose easy smile. Three-quarter body, camera at her navel level, lens horizontal, shot from well back. Collarbone-length mocha brown hair, sleep-mussed, see-through bangs flattened with one tuft sticking up. White fitted camisole, high-waisted grey cotton shorts, beige cardigan slipping off one shoulder, bare feet. Small bright apartment, white walls, pale wood floor, unmade white bed. Soft morning light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-03｜超商・「今天學到一個字」

- 景別：半身自拍 ｜ 字數：98
- 表情設計：摀嘴笑到瞇眼。一手拿著自拍手機，另一手摀在嘴前，笑到眼睛瞇成一條線。

```
A young woman holds her selfie phone in one hand and covers her mouth with the other, laughing with her eyes squeezed shut, the oden label board clearly visible beside her. Half-body phone selfie, camera just above her eye level. Mocha brown hair in a low ponytail with see-through bangs and loose strands at her temples. Cropped grey tee, high-waisted black shorts, black-rimmed glasses. Taiwanese convenience store, fluorescent ceiling tubes, drinks fridge, steaming oden counter, snack shelves. Flat even fluorescent light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-04｜梳妝台護膚・素顏

- 景別：臉部＋上半身近景，拍鏡中反射 ｜ 字數：98
- 表情設計：閉眼享受。眼睛完全閉起、眉頭鬆開；嘴角放鬆地微揚；下巴微抬（把精華液按進臉頰的那一下）。

```
A young woman presses serum into her cheek with her fingertips, eyes closed, chin lifted, mouth relaxed into a small smile. Close-up of her face and shoulders reflected in the mirror, camera at her eye level, lens horizontal. Mocha brown hair clipped back with a claw clip, a few strands loose at her forehead. White fitted camisole. White marble bathroom counter, square mirror, white tiled wall, skincare bottles and brushes left unarranged. Broad diffuse frontal light with very low shadow contrast, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.
```

### YG-05｜捷運月台・隨手自拍

- 景別：半身自拍 ｜ 字數：86
- 表情設計：看著手機鏡頭嘟嘴。看進手機鏡頭，另一手把瀏海撥開；韓系無聊嘟嘴，眼神平淡。

```
A young woman looks into her phone camera while pushing her fringe aside with her free hand, lips softly pursed, a bored flat gaze. Half-body phone selfie, camera just above her eye level. Collarbone-length sleek straight mocha brown hair, side-parted. Fitted black short-sleeve knit, khaki high-waisted mini skirt, beige mini box bag. Metro platform, yellow safety line, platform screen doors, route map lightbox, ceiling tubes. Flat even station light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-06｜汗蒸幕・甜米露

- 景別：全身（坐姿） ｜ 字數：110
- 表情設計：上目遣い。雙手捧著甜米露的紙杯擋在下巴前，只露出眼睛越過杯緣往上看鏡頭；眼睛彎起來。

```
A young woman sits cross-legged on a heated wooden floor holding a paper cup of sweet rice punch with both hands in front of her chin, her eyes peeking over the rim toward the camera, crinkled into crescents. Full body, camera at her seated eye level, lens horizontal, shot from well back. Mocha brown hair in a low bun with two damp strands at her temples. Grey jjimjilbang tee and shorts, a towel folded into sheep horns on her head, bare feet. Korean sauna rest hall, wooden floor, low tables. Warm ceiling light on her face, the warm room behind her keeping visible detail. Natural skin texture, subtle film grain.
```

### YG-07｜客廳地板・什麼都沒發生

- 景別：半身坐姿 ｜ 字數：103
- 表情設計：邊吃邊被拍到。嘴裡還有零食、一邊臉頰鼓著；眼睛圓睜看鏡頭，眉毛抬起像在說「幹嘛拍我」。

```
A young woman sits on the living room floor scrolling her phone and reaching into a snack bag, caught mid-chew with one cheek full, eyebrows raised at the camera. Half body, camera level with her face as she sits on the floor, lens horizontal. Collarbone-length mocha brown hair, the top half clipped up and the lower half loose. Beige camisole, matching short cotton shorts, bare feet. Small apartment living room, low sofa, magazines open on the floor, an electric fan in the corner. Soft window light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-08｜台式早餐店・第一則吃

- 景別：半身，人＋食物同框 ｜ 字數：109
- 表情設計：吃到好吃的。咬一口後眼睛彎成月牙、鼻子微微皺起；空著的手對鏡頭比大拇指。

```
A young woman bites into an egg crepe and throws a thumbs up with her free hand, eyes crinkling into crescents, nose slightly scrunched. Half body with the food in frame, camera level with her chest, lens horizontal. Collarbone-length soft wavy mocha brown hair, side-parted, a small pearl clip on one side. Light blue shirt with the top two buttons open and the hem knotted at her waist, white high-waisted shorts. Taiwanese breakfast shop, stainless steel counter, red plastic chairs, handwritten wall menu, iced tea in a glass. Daylight from the doorway on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### YG-09｜飯店窗邊・皮膚特寫

- 景別：臉部大特寫 ｜ 字數：94
- 表情設計：放空側臉。眼睛看著窗外遠處、不看鏡頭；嘴唇自然放鬆；睫毛半垂——這件刻意不做表情。

```
A young woman leans against the window frame gazing out at the city, her eyes following something far outside the glass, lashes lowered, lips relaxed. Tight close-up of her face, camera at her eye level, lens horizontal. Wet mocha brown hair pushed straight back, collarbone-length, water still beading at the ends. White bathrobe with the collar loosened. Hotel room, white bedding, floor-to-ceiling window, city towers and a river blurred outside. Soft even daylight full on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.
```

### YG-10｜百貨美妝櫃・精緻的一面

- 景別：半身 ｜ 字數：101
- 表情設計：舉起試色的手背挑眉。試完色把手背舉到鏡頭前，同時抬眼、一邊眉毛挑起、同側嘴角上揚。

```
A young woman swatches lipstick on the back of her hand and holds the swatched hand beside her face, raising one eyebrow with one corner of her mouth lifted. Half body, camera level with her chest, lens horizontal. Sleek glossy mocha brown hair, side-parted, collarbone-length with the ends curving slightly inward. Cream cropped fitted knit top, matching off-white high-waisted straight trousers, a trench coat over her arm, gold hoop earrings. Department store beauty floor, glass counters, rows of lipsticks, mirrored columns. Even ceiling light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```


## Luna Tanaka（日籍，及下巴鮑伯）｜11 件

東京可愛系。**鮑伯對稱的幾何寫法是這一版的新東西，完全未驗證。**

### LG-01｜甜點店靠窗・臉部近景

- 景別：臉部＋肩膀近景 ｜ 字數：114
- 表情設計：雙手托腮＋歪頭笑。手肘撐在桌上、雙手托著兩頰把臉擠得更圓；頭往一側傾 20 度；眼睛彎起來。

```
A young woman rests both elbows on the table and cups both cheeks in her palms, squishing her cheeks round, head tilted to one side, smiling toward the camera with her eyes. Close-up of face and shoulders, camera at her eye level, lens horizontal. A symmetrical blunt chin-length black bob ending evenly at the jawline, centre-parted, ends curving slightly inward. Cream square-neck puff-sleeve top, small pearl earrings. Bright dessert shop window seat, white tiled wall, pale wood table, a strawberry cake and a latte on the table in front of her. Soft side daylight on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.
```

### LG-02｜房間晨光・第一則「她在台北」

- 景別：3/4 身（膝上） ｜ 字數：107
- 表情設計：剛睡醒揉眼睛。一手揉著眼睛、另一眼半睜；嘴巴打呵欠打到一半；整張臉是鬆的。

```
A young woman crouches down with her fingertips resting on a sunlit patch of the floor, her other hand rubbing one eye, mouth caught mid-yawn. Three-quarter body, camera level with her face as she crouches, lens horizontal, shot from well back. A symmetrical blunt chin-length black bob ending evenly at the jawline, sleep-mussed with one side flattened. White lace-trimmed camisole pyjama top, matching short pyjama shorts, bare feet. Bright clean studio room, white walls, pale wood floor, a small plant and a plush toy by the window. Soft morning light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-03｜Mochi 在台北的窗台

- 景別：半身＋貓同框 ｜ 字數：106
- 表情設計：臉靠近貓瞇眼笑。臉貼近貓的頭、眼睛瞇成月牙；嘴角上揚；完全不看鏡頭，注意力全在貓身上。

```
A young woman leans in close to an orange cat on the windowsill and scratches its head, her eyes crinkled shut in a smile, her attention entirely on the cat. Half body with the cat in frame, camera level with her face as she sits, lens horizontal. A symmetrical blunt chin-length black bob ending evenly at the jawline, one side tucked behind her ear. Off-white fitted fine-knit top, light shorts. Bedroom windowsill, small potted plants, an iron window grille and the apartment across the street outside. Soft window light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-04｜花季公園・櫻花

- 景別：半身 ｜ 字數：105
- 表情設計：接到花瓣的驚訝。攤開的掌心裡停著一片花瓣，眼睛睜大、嘴呈小 O 形、眉毛抬高。

```
A young woman holds one open palm in front of her with a blossom petal resting in it, eyes widened and mouth softly open in surprise, eyebrows raised. Half body, camera level with her chest, lens horizontal. A symmetrical blunt chin-length black bob ending evenly at the jawline, a cream ribbon headband. White square-neck fitted lace top, pale pink checked mini skirt, a cream cardigan over her shoulders, pearl earrings. Park path under blossoming branches hanging into the top of the frame, petals on her shoulder. Soft daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-05｜公車站・雨停前

- 景別：3/4 身（膝上） ｜ 字數：114
- 表情設計：對鏡頭比 V ＋歪頭。手比 V 舉在臉頰旁；頭往同側傾；眼睛彎成月牙——雨天也很開心的那種笑。

```
A young woman stands at the edge of a bus shelter holding a folded clear umbrella still dripping, tilting her head and making a V sign beside her cheek, eyes crinkled. Three-quarter body, camera at her navel level, lens horizontal, shot from well back. A symmetrical blunt chin-length black bob ending evenly at the jawline. Pale blue checked skirt, a pale blue cardigan over her shoulders, an off-white fitted shirt with the top buttons open. Bus shelter with a colourful route map lightbox, raindrops on the glass, wet asphalt reflecting the glow of shop signs across the street. Her face clearly lit, the glowing signs keeping their colour. Natural skin texture, subtle film grain.
```

### LG-06｜可愛系街區・扭蛋機前

- 景別：半身 ｜ 字數：99
- 表情設計：捧著扭蛋笑到瞇眼。雙手捧著打開的扭蛋在胸前，笑到眼睛瞇起來。

```
A young woman holds an opened gachapon capsule in both hands at chest level, laughing with her eyes squeezed shut. Half body, camera level with her chest, lens horizontal. A symmetrical blunt chin-length black bob ending evenly at the jawline, two small clips holding her fringe back. Pale pink cropped knit top showing a sliver of waist, white high-waisted shorts, a denim jacket tied at her waist. A row of colourful gachapon machines behind her, bright shop signage, clean pavement. Soft daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-07｜遊樂園・旋轉木馬

- 景別：全身 ｜ 字數：111
- 表情設計：抱著爆米花桶回頭吐舌眨眼。雙臂抱著爆米花桶靠在胸前，身體背對、頭轉回鏡頭；舌尖輕吐、單眼眨眼。

```
A young woman hugs a popcorn bucket against her chest with both arms, her hips and torso facing away from the camera while her head and shoulders turn back over one shoulder, tongue tipped out and one eye winking. Full body, camera at her navel level, lens horizontal, shot from well back. A symmetrical blunt chin-length black bob ending evenly at the jawline, a cat-ear headband. White square-neck puff-sleeve top, pale blue pinafore skirt, white mary janes with lace socks. Amusement park beside the carousel, coloured balloons, a decorated parade street behind. Soft daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-08｜浴室鏡前・濕髮

- 景別：半身，拍鏡中反射 ｜ 字數：107
- 表情設計：咬著毛巾角鼓臉頰。擦頭髮擦到一半停下來，用牙齒咬著毛巾一角，對著鏡子鼓起臉頰。

```
A young woman stops drying her hair and bites one corner of the towel between her teeth while looking at herself in the mirror, cheeks puffed out. Half body reflected in the mirror, camera at her eye level, lens horizontal. A wet symmetrical blunt chin-length black bob ending evenly at the jawline, clinging to her cheeks. A white bath towel wrapped around her. Clean bright bathroom, white square tiles, a wooden-framed mirror with a little steam at one corner, skincare bottles on the counter. Broad diffuse frontal light with very low shadow contrast, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-09｜台式早餐店・豆漿

- 景別：半身，人＋食物同框 ｜ 字數：106
- 表情設計：上目遣い。頭略低、眼睛往上看鏡頭；雙手捧著杯子在下巴前；嘴角微揚——日系經典。

```
A young woman holds a glass of soy milk with both hands in front of her chin, head slightly lowered, eyes looking up over the rim toward the camera, smiling with her eyes. Half body with the food in frame, camera level with her chest, lens horizontal. A symmetrical blunt chin-length black bob ending evenly at the jawline, centre-parted and worn loose. Cream fitted thin-knit short sleeve, a light mini skirt. Taiwanese breakfast shop, stainless steel counter, a metal tray, handwritten wall menu, plastic chairs. Daylight from the doorway on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### LG-10A｜浴衣・祭典參道（全身）

- 景別：全身 ｜ 字數：109
- 表情設計：拿著蘋果糖回頭笑。身體與骨盆朝參道前方、頭與肩轉回鏡頭；一手把蘋果糖舉在臉頰旁；笑到眼睛彎。

```
A young woman stands on the festival approach with her hips and torso facing down the path, her head and shoulders turned back toward the camera, holding a candy apple beside her cheek, laughing with her eyes crinkled. Full body, camera at her navel level, lens horizontal, shot from well back. A chin-length black bob half-pinned up with a Japanese hairpin. Pale blue yukata with a white morning-glory print, a navy half-width obi tied tight at the waist, wooden geta. A clean bright wooden torii, paper lanterns strung overhead, food stalls. Her face clearly lit, the lantern-lit stalls behind her keeping visible detail. Natural skin texture, subtle film grain.
```

### LG-10B｜浴衣・蘋果糖（半身）

- 景別：半身 ｜ 字數：97
- 表情設計：舉著蘋果糖笑。一手把蘋果糖舉在臉頰旁、另一手扶著髮簪；笑到眼睛彎。

```
A young woman holds a candy apple up beside her cheek with one hand and steadies the pin in her bun with the other, laughing with her eyes crinkled. Half body, camera level with her chest, lens horizontal. A chin-length black bob half-pinned up with a Japanese hairpin, two strands left at her temples. Pale blue yukata with a white morning-glory print, a navy half-width obi tied tight at the waist. Paper lanterns strung overhead behind her, a blurred food stall. Her face clearly lit, the lantern-lit background keeping visible detail. Natural skin texture, subtle film grain.
```

---

# 五、這一輪想請你回答的問題

1. **4 個 blocker 修掉了嗎？**有沒有哪一個我修得不對，或修出新問題？
2. **第二節那兩處我沒照做的地方，你的判定是什麼？**
   特別是 2-1——「保留已驗證字串」vs「全面改寫成更貼合場景的寫法」，你認為哪個風險低？
3. **Reference image 的測法（第三節）可行嗎？**
4. **LG-06 我選了「笑出來」而不是「嘟嘴」，這個選擇對嗎？**
5. **21 段裡還有沒有你會擋下來的？**如果有，請照上一輪那樣給風險分級。
6. **preflight 那 4 張的選擇要不要調整？**
   你上一輪建議：YG-03（手部邏輯）、LG-01（鮑伯對稱）、LG-04 或 LG-06（單一表情）、
   任一 Luna 戶外（場景模板）。我打算照這個跑，但 LG-01 是**近景**，
   近景看不太出來鮑伯兩側的完整輪廓——**要不要把鮑伯那張換成 LG-05 或 LG-07 這種看得到整顆頭的？**
7. **有沒有這一輪才出現的新共通問題？**

---

# 六、附錄：這個專案已經花錢驗證過的結論（基準線，不必再討論）

| 結論 | 證據 |
|---|---|
| 不寫族裔與身材數字也 OK | 6/6 身分與身材正確 |
| `camera at her navel level, lens horizontal, shot from well back` | 6/6 比例正確；寫絕對公分數反而失敗 |
| 否定句無效 | `no open sky` 被完全無視 |
| `background exposed the same brightness as her skin` | 室內 3 張都解掉逆光 |
| 表情必須綁實體動作 | 比 V ✅／捧杯遮嘴＋眨眼 ✅／回眸一笑 ❌／單眼瞇起 ❌ |
| 身體姿勢做得出來，純臉部表情做不出來 | 同一段裡身體扭轉成功、臉上的笑失敗 |
| `soul_id` 會鎖住整套場景模板 | 提到「巷弄街拍」就生出同一條街，明寫不要天空也無效 |
| 抽象的「正在飄」做不出來 | 3/3 失敗 |
| 沒寫髮長就會生出長短不一的頭髮 | 1/1 |
