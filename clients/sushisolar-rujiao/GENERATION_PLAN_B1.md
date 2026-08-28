# 批次 1 生成規格（逐件細節・待核准）

> 2026-08-25。**這份是給 Penny 逐件核准用的——確認後才送 Higgsfield 生成。**
> 可預覽版本（v2）：<https://claude.ai/code/artifact/07834065-b6e5-4f59-bab2-49d8e601f3ef>
>
> 每件都寫齊 **妝容／髮型／穿著／場景環境／拍攝角度／光線／情境／Caption**，
> 目的是讓你在生成之前就能想像出畫面，不用靠生成結果去猜。

---

## ⚠️ 2026-08-27 全面改版（v2）：以實測結果重寫

這一版不是憑推論改的，是跑完 6 張控制變因測試之後改的。
完整測試記錄見 `CALIBRATION_TEST.md`，以下是直接影響這 21 件的四條。

### 1. 刪掉共用身分（族裔＋身材數字）

6 張測試的 prompt 裡**完全沒寫**族裔、身高、三圍、罩杯，
臉、身材、童顏都正確。`soul_id` 鎖得住，寫了只是多一組干擾關鍵字。

### 2. 機位改成相對描述，不寫公分也不寫焦段

`camera at her navel level, lens horizontal, shot from well back` 這組寫法
在 6 張裡都拿到正確比例——沒有頭大腿短，也沒有俯拍。
**絕對公分數與固定焦段全部刪掉**（`85mm`／`101cm`／`4 公尺` 那些）。

### 3. 光線從「五段」改成「四段」，刪掉「曝光取捨」

原本第 ④ 段「哪裡過曝」等於在指示模型把背景燒白——
**前幾輪每張都逆光，這是主因之一**，而且 `character.md` 寫的其實是
「冷白均勻、幾乎沒有陰影」，逆光只是偶爾的特效。

新的第 ④ 段一律是 **`背景曝光與她的膚色相當`**。
這是**正向描述**——實測確認 `soul_2` 沒有 negative 欄位，
`no blown-out highlights` 這種否定寫法會被完全無視。

### 4. 表情一律綁在一個實體動作上

實測規律很乾淨：**綁著物件或手勢的表情做得出來，純臉部的做不出來**，
跟寫得細不細無關。已把 8 件純臉部的改寫成綁物件的版本
（回眸→扶髮簪＋舉蘋果糖、鼓臉頰→咬毛巾角、嘟嘴→手機舉在臉側…），
每件後面都標了**掛載動作**是什麼。詳見 `SEXY_SCENE_LIBRARY.md` 第 23 點。

### 5. 每件多了一行「生成 prompt」

這是最大的結構改變。以前是十個中文欄位寫完，再由我當場翻譯成英文送出去——
上一輪就是這樣翻出 330 字的失敗 prompt。
現在**每件都預先寫好一段 70–110 字的英文 prompt**，欄位是給人看的，prompt 是給模型看的，
兩者分開。你核准的時候可以直接看那一行，那一行就是實際會送出去的東西。

### 6. YG-06 換掉

原本的「巷弄・被叫住的那一秒」實測確認生不出來——Yuna 的 `soul_id` 對巷弄街拍
有固定畫面慣性，文字改不動。換成「汗蒸幕・甜米露」，那是她 `character.md` 裡
本來就有的場景，同時補回一個 C 級地點。

---

## 這批的兩個方向修正

### Luna 改成東京可愛系（不再是京都老東西）

先前的規劃照 `character.md` 原本的「京都侘寂／老木頭／舊陶器／褪色」去推，
生出來的畫面不精緻、偏老舊。**已在 `kols/luna-tanaka/character.md` 加上視覺方向修正並改寫相關段落。**

| | 停用 | 改成 |
|---|---|---|
| 調性 | 侘寂、褪色、老舊、暗 | **可愛、精緻、明亮、乾淨** |
| 場景 | 二手書店、老陶器店、苔蘚庭院 | **甜點店、可愛系街區、遊樂園、花季、白色系房間** |
| 色調 | 低飽和＋haze＋舊照片感 | **乾淨明亮、奶白＋淺粉、通透**（不要霧、不要髒、不要暗） |

**新增浴衣祭典（LG-10）**——這是她身分最好用、視覺變化最大的一組。

> 順帶撤回我上一版寫的「Luna 結構性不可能有 A 級」——那句話本身就是把美學設死的錯誤。
> 新方向下遊樂園、祭典、花季都是很自然的 A 級。

### 表情寫法換掉：先有名字，再有細節

上一版寫的是「左嘴角比右邊高一點、右眉微抬」這種**微小偏差**——
那套來自 `emotion-director`，但**它是為影片設計的**（影片裡臉會動，
不對稱是為了避免面具臉）。**靜態圖一張照片就是一個表情**，
只寫偏差沒有主體，想像不出來、生成出來就是面無表情。

**新寫法：表情名稱在前，細節修飾在後。**
21 件已重新指派，每人 10 種完全不重複——回眸一笑、吐舌＋眨眼、鼓臉頰、
上目遣い、憋笑破功、雙手托腮、嘟嘴、挑眉微笑…
完整表情庫見 `SEXY_SCENE_LIBRARY.md` 第 20 點。

### 生成方式：一個 spec 只生一張

上一輪 `count=2` 生出來的兩張構圖姿勢幾乎一樣，**第二張沒有任何新資訊**。
改成一個 spec 一張；不滿意就**改 prompt 再生**，改動本身才是資訊。
要變體就**寫成不同的 spec**，不靠 count 複製。見第 21 點。

### 穿搭校正：不要把她們穿成路人

**上一版整批穿搭被評「太樸素、看起來很像路人」——這個問題出在我身上，而且錯在最要命的地方。**

回頭對原設定才發現漏掉的是這些：

| | 原設定寫的 | 上一版我給的 |
|---|---|---|
| **受眾** | `DAILY_VIDEO_SOP.md` 必讀第一條：**受眾都是男性，服裝要展示身材曲線、腰線** | 大學T、寬鬆襯衫、長裙 |
| **Yuna** | 168cm、**腿長 82cm（佔身高 48.8%）**、腰臀比 0.65，高挑纖細是她的賣點 | **卡其工裝寬褲**——直接把腿藏起來 |
| **Luna** | **童顏巨乳 E cup（88-56-87）**，`character.md` 用粗體寫「反差是她的核心」 | oversized 針織（袖子過長）、長袖睡衣、及膝長裙——**把最重要的特徵整批蓋掉** |

**根本錯誤：我把「C 級不美的日常**場景**」誤讀成「不美的**造型**」。**
C 級講的是地點層級，不是造型層級——競品 Sherry 敢發 Costco，
但她在 Costco 裡穿的不是路人裝。**地點可以土，人不能土**，
那個反差正是「她是個剛好很好看的真人」的效果來源。

**這一版全部改成顯身材、有造型感**：高腰、短版、貼身針織、迷你裙、細肩帶、方領、收腰。
oversized 只當外層披著，裡面一定合身。兩人的 `character.md` 服裝公式也加了補記。

### Yuna 的妝容改成 2026 韓系實況

初版寫的「番茄紅唇釉」是 **2020 年前後**那波韓妝的特徵，現在已經不是主流。
查了 2026 的實際趨勢後改寫——**現在的韓系核心是 diffused、low-contrast**，
跟當年那種高飽和唇＋銳利眼線幾乎是相反的方向。

| 項目 | 改成 |
|---|---|
| **唇** | **blurred lips（멀멀妝／toasty）**——霧化暈開的奶茶米棕帶灰調；或 glazed lavender 淡紫裸唇；或粉色唇釉 |
| **腮紅** | **橫過鼻樑的 nose blush**，或打在眼下；淡淡一層不集中 |
| **眼頭** | **精準的小 V 字打亮** ← 2026 最好認的一個細節 |
| **眼線** | 極細內眼線，**眼尾不刻意上揚**（不是當年的銳利感） |
| **髮色** | 深棕帶 **mocha／mushroom brown** 調，不是純黑 |
| **髮型** | see-through 空氣瀏海、側分側撥（明顯回歸）、sleek 光澤直順、柔化層次 |
| **穿搭** | Acubi 韓系（短版上衣＋低腰丹寧＋迷你包）、奶油色 tonal layering、機能休閒 gorpcore |

`YG-10` 另外用一次 **Y3K 金屬光眼影**（銀白／丁香紫）——那是 2026 的另一條線，跟她的冷白調很合。

### Yuna 補上「精緻」那一面

她原本的設定偏日常，這批加了 **YG-10 百貨美妝櫃**——全妝、精品感，
補上她「美妝女生」的另一面，也讓版面不會全是素顏與日常。

### 🔴 這些是範圍，不是模板

一個真正像活人的帳號會有主要基調，但素材一定是多元的。
**如果每張都嚴格照設定走，版面會單調，而且一看就假。**
所以這批刻意混了：全妝 ↔ 素顏、精緻 ↔ 隨便、室內 ↔ 街頭 ↔ 玩樂。

兩人的 `content_style.md` 也已加上「這份文件的規則怎麼讀」一節，
把規定分成兩類：**技術性**（`porcelain skin`、`high dynamic range` 等 AI 生成的技術問題，
要遵守）與**風格偏好**（妝容、穿搭、場景、色調——是預設值與範圍，不是鐵律）。
看到「不要 X」時讀成「這不是她的主軸」，不是「絕對禁止」。

---

## Caption 語言：中文為主

兩人都在台灣生活、逛台灣的店、代言台灣的餐廳——**觀眾看不懂韓文／日文就沒有意義**。

| 形式 | 比例 |
|---|---|
| **純中文** | 約 50% |
| **中文 ＋ 一句母語** | 約 35%（她們的招牌，母語當簽名） |
| 純母語 | 約 15%（回國時、特別心情） |

**語氣**：可愛但不做作，有小抱怨、小失敗、自嘲。
Emoji **1–2 個不堆疊**——Yuna 常用 🍒☺️🥹😮‍💨✨，Luna 常用 🌙🍓☔️🐈✨。
完整規則已寫進兩人的 `content_style.md`。

---

## 配額檢查

| | A 級（嚮往） | B 級（有質感的日常） | C 級（完全不美的日常，硬性 ≥2） | 不重複場景 |
|---|---|---|---|---|
| **Yuna** | 2 | 5 | **3** ✅ | 10 / 10 |
| **Luna** | 2 | 6 | **2** ✅ | 10 / 10 |

**髮型每件都不同**、**妝容從全妝到素顏都有**、**自拍與他拍混合**（Yuna 自拍 2 件）。

---


## Yuna Kim｜10 件

**模型**：`soul_2` ＋ soul_id `235794a5-2eff-45fb-91b4-3232910afefa`

**共用身分**：**不寫**。族裔、身高、三圍、罩杯一律不進 prompt——`soul_id` 已經鎖住臉與體型，
實測 6 張都沒寫這些，身分與身材都正確。寫了反而多一組會干擾的關鍵字。


### YG-01｜咖啡廳靠窗・臉部近景
`圖`　·　對應 **頭貼**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | 透明感水光底妝，看得到毛孔；平直淡眉；奶茶色低對比暈染眼影；**眼頭小 V 字打亮**；極細內眼線、眼尾不上揚；**nose blush 淡淡橫過鼻樑**；**blurred lips**——奶茶米棕霧化暈開。 |
| **髮型** | **mocha brown** 長軟波浪及鎖骨，**see-through 空氣瀏海**，右側撥到耳後露出耳環。 |
| **穿著** | 上身：奶油白色**合身**細針織短袖（貼身，鎖骨與肩線清楚）｜下身：畫面外｜鞋：—｜外層：—｜首飾：金色小圓耳環＋細鎖骨鍊 |
| **場景環境** | 明亮咖啡廳靠窗座位。白牆、淺木桌面、桌上一杯拿鐵與她的手機（透明殼）、窗外是台北街景（招牌、機車、行道樹）。 |
| **機位與構圖** | **臉部＋肩膀近景。**<br>**機位**：在她的眼睛高度，鏡頭保持水平。<br>**距離**：坐在她對面的距離，不要湊太近。<br>**構圖**：臉佔畫面約 45%，留白留在她視線的方向。 |
| **光線** | ① 落地窗自然光從她左前方進來，**打在臉上**｜② 白色桌面把光反回下巴與頸部｜③ 窗光冷白 vs 店內暖黃軌道燈落在她身後牆面｜④ **背景曝光與她的膚色相當** |
| **表情** | **撥髮回眸。**一手正把頭髮撥到耳後，同時轉頭看鏡頭；嘴角單邊上揚的淺笑；頭往撥髮的那一側微傾。 |
| **肢體與重心** | 坐姿，上半身微向前傾靠著桌緣；**右手正把頭髮撥到耳後——動作中，不是撥完**；左手托著杯子；肩膀一高一低。；**撥開的那撮頭髮還垂在指縫間晃動**。 |
| **情境** | 剛坐下，把頭髮撥到耳後，看向鏡頭 |
| **生成 prompt** | `A young woman tucks a strand of hair behind her ear and turns to look at the camera, one corner of her mouth lifted, head tilted toward that hand. Close-up of face and shoulders, camera at her eye level, lens horizontal. Collarbone-length soft wavy mocha brown hair with see-through wispy bangs. Cream fitted fine-knit tee, thin gold necklace, small gold hoops. Bright cafe window seat, white wall, pale wood table, a latte and her phone. Soft cool daylight from her front-left landing on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.` |
| **Caption 草稿** | —（頭貼用） |

### YG-02｜台北公寓窗邊晨光
`影片 10s ＋ start frame`　·　對應 **Y-03**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | 幾乎素顏。保留淡眉與一點粉色潤色護唇，其餘乾淨。 |
| **髮型** | mocha brown，剛睡醒的微亂，see-through 瀏海被壓扁翹起一撮。 |
| **穿著** | 上身：白色**細肩帶貼身**針織背心（腰線明顯）｜下身：淺灰**高腰**棉質短褲｜鞋：赤腳｜外層：米色開襟針織鬆垮掛在單肩（只披不穿）｜首飾：無 |
| **場景環境** | 台北老公寓翻新的小套房。白牆、淺木地板、白色床組（床沒整理）、地上一雙拖鞋、床邊小桌上放著沒收的馬克杯。窗外可見鏽蝕鐵窗花、對街舊公寓磁磚外牆、冷氣室外機、糾纏電線。 |
| **機位與構圖** | **3/4 身（膝上）。**<br>**機位**：在她的肚臍高度，鏡頭保持水平。<br>**距離**：站遠一點拍，不要靠近。<br>**構圖**：人物落在三分線偏左，右側留出窗光的空間。 |
| **光線** | ① 晨光從窗戶斜射進來，**打在臉上**，在木地板留下長條光影｜② 淺木地板把暖光反回下巴與小腿｜③ 窗外冷白 vs 地板反射暖黃｜④ **背景曝光與她的膚色相當** |
| **表情** | **端著杯子瞇眼笑。**雙手捧著馬克杯舉到嘴邊喝一口，眼睛還沒完全張開、瞇成細細的；嘴角鬆鬆揚起。<br>（掛載動作＝馬克杯） |
| **肢體與重心** | 赤腳走路有重量感；端杯子的手指自然彎曲；喝一口時肩膀微微下沉（吐氣）；**針織外套從單肩滑下一點**。；**左手把滑下肩的針織外套往上拉了一下**。；**右手端著馬克杯、左手把滑下肩的針織外套往上拉了一下——兩手都有事做**。 |
| **情境** | 她端著馬克杯走到窗邊，站定，看窗外，喝一口，轉頭看鏡頭 |
| **生成 prompt** | `A young woman stands at the window holding a mug with both hands and lifts it to her mouth, eyes still narrowed from sleep, a loose easy smile. Three-quarter body, camera at her navel level, lens horizontal, shot from well back. Collarbone-length mocha brown hair, sleep-mussed, see-through bangs flattened with one tuft sticking up. White fitted camisole, high-waisted grey cotton shorts, beige cardigan slipping off one shoulder, bare feet. Small bright apartment, white walls, pale wood floor, unmade white bed. Soft morning light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 台北的早上☀️<br>光剛好照到腳 |

### YG-03｜超商・「今天學到一個字」
`影片 10–15s ＋ start frame`　·　對應 **Y-05**　·　地點層級 **C**

| | |
|---|---|
| **妝容** | 淡妝。透明感薄底妝、淡眉、眼影幾乎沒有、nose blush 很淡、粉色潤色護唇。戴黑框眼鏡。 |
| **髮型** | 低馬尾，see-through 瀏海留著，鬢角兩撮碎髮垂下。 |
| **穿著** | 上身：**短版**灰色短袖上衣（露一截腰）｜下身：黑色**高腰**短褲｜鞋：白色低筒球鞋｜外層：—｜首飾：黑色細框眼鏡＋手腕上的黑色髮圈 |
| **場景環境** | 超商內。天花板日光燈管、關東煮機台冒著熱氣、飲料冷藏櫃。**貨架與所有招牌一律失焦**——這件不要有需要讀字的東西。 |
| **機位與構圖** | **半身自拍。**<br>**機位**：手機伸直手臂舉在略高於眼睛的位置（自拍的真實高度）。<br>**構圖**：人在畫面偏右，左側帶到關東煮機台。 |
| **光線** | ① 天花板日光燈管**均勻打亮整張臉**｜② 冷藏櫃玻璃反一層冷光在她側臉｜③ 全場冷白，關東煮機台一小塊暖黃｜④ **背景曝光與她的膚色相當** |
| **表情** | **舉著關東煮紙杯對鏡頭笑。**一手拿自拍手機，另一手把紙杯舉到臉頰旁；下巴微收、對鏡頭笑。<br>（掛載動作＝紙杯；**「摀嘴」與「指標示牌」都拿掉了**——自拍只剩一隻空手，兩個都要就是三隻手） |
| **肢體與重心** | 一手舉手機自拍、**手臂有輕微晃動**；另一手指著標示牌；重心在單腳、身體微側。；**低馬尾在她轉頭時甩了一下**。 |
| **情境** | 買了關東煮，站在機台旁自拍；「今天學到一個字」由 Caption 承擔，不靠畫面 |
| **生成 prompt** | `In a phone selfie, a young woman holds a paper cup of hot broth up beside her cheek with her free hand, smiling at the camera with her chin tucked. Half-body phone selfie, camera just above her eye level, the shelves behind her thrown completely out of focus. Collarbone-length mocha brown hair in a low ponytail with see-through bangs and loose strands at her temples. Cropped grey tee, high-waisted black shorts, black-rimmed glasses. A convenience store interior, fluorescent ceiling tubes, a steaming hot-food counter, blurred shelves of packaged snacks. Flat even fluorescent light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 今天學到一個新的字！<br>可是我念錯 店員笑了🥲 |
| 附註 | **背景路人 1–2 人**：背向、不看鏡頭、失焦、外型與她明顯區隔 |

### YG-04｜梳妝台護膚・素顏
`圖`　·　對應 **Y-06**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | **完全素顏。**皮膚要看得到毛孔與 T 字部位的自然油光，眉毛保留原生形狀，唇是自然色。 |
| **髮型** | 全部往後用鯊魚夾夾起，額前留幾根碎髮垂下。 |
| **穿著** | 上身：白色**細肩帶貼身**背心（鎖骨、肩線、胸型自然可見——這是護膚照的重點）｜下身：畫面外｜鞋：—｜外層：—｜首飾：手腕上的黑色髮圈 |
| **場景環境** | 浴室洗手台／梳妝台。白色大理石台面、方形鏡、白色磁磚牆。護膚品瓶**不刻意排整齊**、化妝刷插在小杯裡、用過的化妝棉、白毛巾掛在旁邊的桿子上。 |
| **機位與構圖** | **臉部＋上半身近景，拍鏡中反射。**<br>**機位**：在她的眼睛高度，鏡頭保持水平。<br>**構圖**：鏡框帶進畫面，台面上的瓶罐入鏡下緣。 |
| **光線** | ① 浴室頂燈＋鏡側光**均勻打在臉上，幾乎沒有陰影**｜② 白色大理石台面把光反回下巴｜③ 全場冷白｜④ **背景曝光與她的膚色相當** |
| **表情** | **閉眼享受。**眼睛完全閉起、眉頭鬆開；嘴角放鬆地微揚；下巴微抬（把精華液按進臉頰的那一下）。 |
| **肢體與重心** | **雙手掌心貼著臉頰往上按**；手肘抬起；上半身微前傾靠近鏡子；肩膀放鬆下沉。 |
| **情境** | 用手掌把精華液按進臉頰，眼睛微閉 |
| **生成 prompt** | `A young woman presses serum into her cheek with her fingertips, eyes closed, chin lifted, mouth relaxed into a small smile. Close-up of her face and shoulders reflected in the mirror, camera at her eye level, lens horizontal. Collarbone-length mocha brown hair clipped back with a claw clip, a few strands loose at her forehead. White fitted camisole. White marble bathroom counter, square mirror, white tiled wall, skincare bottles and brushes left unarranged. Broad diffuse frontal light with very low shadow contrast, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.` |
| **Caption 草稿** | 洗完澡最舒服☺️<br>씻고 나서 |

### YG-05｜捷運月台・隨手自拍
`圖`　·　對應 **Y-07**　·　地點層級 **C**

| | |
|---|---|
| **妝容** | 日常妝。透明感底妝、淡眉、奶茶色暈染眼影、眼頭 V 字打亮、nose blush、blurred lips 米棕。 |
| **髮型** | **側分 sleek 直順**（2026 明顯回歸的一條線），髮尾帶微層次。 |
| **穿著** | 上身：黑色**貼身短袖針織**（腰線清楚）｜下身：**卡其色高腰短裙**｜鞋：白色球鞋｜外層：—｜首飾：銀色細手鍊＋米色迷你方包斜背 |
| **場景環境** | 捷運站月台。黃色警示線、月台門玻璃、路線圖燈箱、候車座椅、天花板的燈管。 |
| **機位與構圖** | **半身自拍。**<br>**機位**：手機伸直手臂舉在略高於眼睛的位置。<br>**構圖**：人在畫面偏左，右側帶到月台門與路線圖燈箱。 |
| **光線** | ① 月台天花板燈管**均勻打亮臉部**｜② 月台門玻璃反一層冷光｜③ 冷白為主，路線圖燈箱一小塊彩色｜④ **背景曝光與她的膚色相當** |
| **表情** | **看著手機鏡頭嘟嘴。**看進手機鏡頭，另一手把瀏海撥開；韓系無聊嘟嘴，眼神平淡。<br>（掛載動作＝撥瀏海；**手機是拍攝者，不會出現在畫面裡**） |
| **肢體與重心** | 重心在一腳、**另一腳腳尖外開**；一手舉手機、一手勾著包帶；肩線傾斜。；**月台的通風把她的髮尾往一側吹動**。 |
| **情境** | 等車，順手拍一張，表情有點無聊 |
| **生成 prompt** | `A young woman looks into her phone camera while pushing her fringe aside with her free hand, lips softly pursed, a bored flat gaze. Half-body phone selfie, camera just above her eye level. Collarbone-length sleek straight mocha brown hair, side-parted. Fitted black short-sleeve knit, a khaki high-waisted pleated A-line mini skirt forming one continuous hem around her thighs, a beige mini box bag. Metro platform, yellow safety line, platform screen doors, a route map lightbox thrown out of focus, ceiling tubes. Flat even station light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 捷運等好久喔😮‍💨<br>但我很乖有排隊 |
| 附註 | **背景路人 2–3 人**：背向、失焦 |

### YG-06｜汗蒸幕・甜米露
`圖`　·　對應 **Y-08**　·　地點層級 **C**

> **這件是換掉的。**原本是「巷弄・被叫住的那一秒」，2026-08-27 實測確認
> Yuna 的 `soul_id` 對「巷弄街拍」有固定的畫面慣性（同一條街、同一個機位、
> 同一個燒白的天空），文字改不動——見 `CALIBRATION_TEST.md` 第 10–11 節。
> 改成她 `character.md` 裡本來就寫著的「去汗蒸幕的週末」，同時補回一個 C 級地點。

| | |
|---|---|
| **妝容** | 幾乎素顏。乾淨薄底、淡眉、一點粉色潤色護唇，臉上有一點蒸過的紅。 |
| **髮型** | mocha brown 全部往後綁成低丸子，鬢角垂下兩撮被蒸氣打濕貼著臉。 |
| **穿著** | 上身：灰色汗蒸幕短袖上衣（寬鬆但短，坐下時腰線露出來）｜下身：同色系短褲（腿完整露出）｜鞋：赤腳｜頭上：**毛巾折成羊角**｜首飾：無 |
| **場景環境** | 汗蒸幕的休息大廳。淺色木地板、矮桌、幾個坐墊、遠處的睡眠區與販賣機、牆上的韓文告示。乾淨明亮，不是陰暗的澡堂。 |
| **機位與構圖** | **全身（坐姿）。**<br>**機位**：在她坐著時的眼睛高度，鏡頭保持水平。<br>**距離**：站遠一點拍。<br>**構圖**：她盤腿坐在木地板上，身後帶到休息大廳的縱深。 |
| **光線** | ① 休息大廳的暖色頂燈**均勻打在臉上**｜② 木地板把暖光反回下巴｜③ 全場暖黃，這件刻意跳出她的冷白區間｜④ **背景曝光與她的膚色相當** |
| **表情** | **上目遣い。**雙手捧著甜米露的紙杯擋在下巴前，只露出眼睛越過杯緣往上看鏡頭；眼睛彎起來。<br>（掛載動作＝紙杯） |
| **肢體與重心** | 盤腿坐在地上，背微駝、放鬆；**雙手都在紙杯上**；一邊肩膀比另一邊低。 |
| **情境** | 蒸完出來坐在休息區喝甜米露，抬眼看鏡頭 |
| **生成 prompt** | `A young woman sits cross-legged on a heated wooden floor holding a paper cup of sweet rice punch with both hands in front of her chin, her eyes peeking over the rim toward the camera, crinkled into crescents. Full body, camera at her seated eye level, lens horizontal, shot from well back. Collarbone-length mocha brown hair gathered into a low bun with two damp strands at her temples. Grey jjimjilbang tee and shorts, a towel folded into sheep horns on her head, bare feet. Korean sauna rest hall, wooden floor, low tables. Warm ceiling light on her face, the warm room behind her keeping visible detail. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 蒸完整個人都軟掉了🫠<br>甜米露是最好喝的部分 |
| 附註 | 這是這批唯一的暖光場景，刻意跳出她的冷白區間。<br>**⚠️ 這件的場景在韓國，是刻意的**——歸為「回韓國的時候」類型內容（對應 Luna 的「回日本的時候」）。**其餘 Yuna 的件全部是台北，畫面裡不應出現可辨識的韓文招牌。** |

### YG-07｜客廳地板・什麼都沒發生
`影片 10s ＋ start frame`　·　對應 **Y-09**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | 素顏到淡妝之間。只有眉毛與粉色潤色護唇。 |
| **髮型** | 鯊魚夾隨手夾一半，下半放下（與 YG-04 的全夾起區隔）。 |
| **穿著** | 上身：米色**細肩帶**家居背心｜下身：同色系**短版**棉質短褲｜鞋：赤腳｜外層：—｜首飾：無 |
| **場景環境** | 小套房的客廳地板。矮沙發、地上攤開的雜誌、旁邊拆開的零食袋、電風扇在角落轉。 |
| **機位與構圖** | **半身坐姿。**<br>**機位**：與她坐在地上時的臉同高，鏡頭保持水平。<br>**構圖**：地上的雜誌與零食袋入鏡下緣。 |
| **光線** | ① 窗戶漫射光從側面**打在臉上**｜② 淺色地板反光補下巴｜③ 窗光冷白 vs 角落一盞暖黃立燈｜④ **背景曝光與她的膚色相當** |
| **表情** | **邊吃邊被拍到。**嘴裡還有零食、一邊臉頰鼓著；眼睛圓睜看鏡頭，眉毛抬起像在說「幹嘛拍我」。 |
| **肢體與重心** | 盤腿側坐、一手撐地；另一手拿零食送到嘴邊；**背微駝**（真實的放鬆姿勢，不是挺直）。；**角落的電風扇把她垂下的髮絲吹得輕輕飄動**。 |
| **情境** | 坐在地上滑手機，伸手拿零食吃，什麼都沒發生 |
| **生成 prompt** | `A young woman sits on the living room floor scrolling her phone and reaching into a snack bag, caught mid-chew with one cheek full, eyebrows raised at the camera. Half body, camera level with her face as she sits on the floor, lens horizontal. Collarbone-length mocha brown hair, the top half clipped up and the lower half loose. Beige camisole, matching short cotton shorts, bare feet. Small apartment living room, low sofa, magazines open on the floor, an electric fan in the corner. Soft window light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 今天不想出門<br>아무것도 안 함 |

### YG-08｜台式早餐店・第一則吃
`圖`　·　對應 **Y-10**　·　地點層級 **C**

| | |
|---|---|
| **妝容** | 日常妝。薄透底妝、淡眉、淡奶茶眼影、nose blush、粉色唇釉。 |
| **髮型** | 側分長軟波浪，左側夾一個珍珠小髮夾。 |
| **穿著** | 上身：淺藍色短袖襯衫，**下擺在腰際打結**（露一截腰）｜下身：白色**高腰**短褲｜鞋：白色球鞋｜首飾：小珍珠耳環＋珍珠髮夾<br>（**已刪掉「前兩顆解開」**——`top buttons open` 是把領口拉低的高風險字，LG-05 已因此出過事） |
| **場景環境** | 早餐店。不鏽鋼餐檯、紅色塑膠椅、鐵盤上的蛋餅、玻璃杯裝的冰紅茶。**牆面與手寫菜單失焦**。 |
| **機位與構圖** | **半身，人＋食物同框。**<br>**機位**：與她的胸口同高，鏡頭保持水平。<br>**構圖**：鐵盤與冰紅茶在前景下緣，牆上手寫菜單在她身後。 |
| **光線** | ① 店門口的自然光從側前方**打在臉上**｜② 不鏽鋼餐檯把光反回下巴｜③ 門口冷白 vs 店內日光燈｜④ **背景曝光與她的膚色相當** |
| **表情** | **吃到好吃的。**咬一口後眼睛彎成月牙、鼻子微微皺起；空著的手對鏡頭比大拇指。 |
| **肢體與重心** | 雙手捧著蛋餅；手肘靠在桌上；上半身前傾；肩膀微聳。；**捲起的襯衫袖口與垂下的髮絲隨著前傾晃了一下**。 |
| **情境** | 咬了一口蛋餅，抬眼看鏡頭 |
| **生成 prompt** | `A young woman bites into an egg crepe and throws a thumbs up with her free hand, nose slightly scrunched, smiling. Half body with the food in frame, camera level with her chest, lens horizontal, the wall behind her thrown out of focus. Collarbone-length soft wavy mocha brown hair, side-parted, a small pearl clip on one side. A light blue short-sleeve shirt knotted at the waist, white high-waisted shorts. A breakfast shop, a stainless steel counter, red plastic stools, a metal tray, iced tea in a tall glass. Daylight from the doorway on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 蛋餅真的很好吃🥹<br>這個冰紅茶也太甜 |

### YG-09｜飯店窗邊・皮膚特寫
`圖`　·　對應 **Y-13**　·　地點層級 **A**

| | |
|---|---|
| **妝容** | **素顏，剛洗完澡。**皮膚微微泛紅、有水感，眉毛保留，唇是自然色。 |
| **髮型** | 濕髮往後撥，髮尾滴著水。 |
| **穿著** | 上身：白色浴袍，領口鬆開露出鎖骨與肩線｜下身：—｜鞋：—｜外層：—｜首飾：無 |
| **場景環境** | 飯店房間窗邊。白色床單、落地窗、窗外是城市高樓與河景。床頭放著水杯。 |
| **機位與構圖** | **臉部大特寫。**<br>**機位**：在她的眼睛高度，鏡頭保持水平。<br>**構圖**：臉佔滿畫面，窗外城市只留一小塊虛化。 |
| **光線** | ① 落地窗漫射光**正面均勻打亮臉**｜② 白色床單把光反回下巴｜③ 全場冷白｜④ **背景曝光與她的膚色相當** |
| **表情** | **放空側臉。**眼睛看著窗外遠處、不看鏡頭；嘴唇自然放鬆；睫毛半垂——這件刻意不做表情。 |
| **肢體與重心** | 側身靠著窗框；一手扶著浴袍領口；另一手垂著；肩膀一高一低。；左手鬆鬆搭在窗框上；**浴袍的腰帶末端垂著微微擺動**。 |
| **情境** | 剛洗完澡，靠著窗看外面 |
| **生成 prompt** | `A young woman leans against the window frame gazing out at the city, her eyes following something far outside the glass, lashes lowered, lips relaxed. Tight close-up of her face, camera at her eye level, lens horizontal. Wet mocha brown hair pushed straight back, collarbone-length, water still beading at the ends. White bathrobe with the collar loosened. Hotel room, white bedding, floor-to-ceiling window, city towers and a river blurred outside. Soft even daylight full on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.` |
| **Caption 草稿** | 皮膚今天狀態超好☺️<br>이거 진짜 좋아 |

### YG-10｜百貨美妝櫃・精緻的一面
`圖`　·　對應 **機動**　·　地點層級 **A**

| | |
|---|---|
| **妝容** | **這批最精緻的一張。**透明感水光底妝拉到最亮；**Y3K 金屬光眼影**——細緻的銀白或丁香紫（2026 的另一條線，跟她的冷白調很合）；眼頭 V 字打亮明確；nose blush ＋ 眼下腮紅；**glazed lavender 淡紫調裸唇**。 |
| **髮型** | **sleek 光澤直順側分**，髮尾微微內彎，mocha brown 的髮色在燈下很明顯。 |
| **穿著** | 上身：奶油色**短版貼身**針織上衣｜下身：**同色系米白高腰西裝直筒褲**（tonal layering，高腰拉腿長）｜鞋：尖頭平底鞋｜外層：卡其色風衣掛在手臂上｜首飾：金色圈形耳環＋細手錶＋小方包 |
| **場景環境** | 百貨公司一樓的美妝樓層。玻璃櫃、排列整齊的口紅與粉盒、鏡面立柱、天花板的嵌燈、櫃檯的白色檯面。 |
| **機位與構圖** | **半身。**<br>**機位**：與她的胸口同高，鏡頭保持水平。<br>**構圖**：試色的手背舉在畫面中段，身後帶到玻璃櫃與鏡面柱。 |
| **光線** | ① 天花板嵌燈＋櫃檯打光**均勻打亮臉**｜② 白色檯面與鏡面柱把光反回下巴｜③ 冷白為主，玻璃櫃內一點暖黃重點光｜④ **背景曝光與她的膚色相當** |
| **表情** | **舉起試色的手背挑眉。**試完色把手背舉到鏡頭前，同時抬眼、一邊眉毛挑起、同側嘴角上揚。<br>（掛載動作＝試色手背） |
| **肢體與重心** | 一手手背朝上展示試色；另一手拿著口紅；上半身微側向櫃檯；**風衣掛在手臂上、下襬垂著**。 |
| **情境** | 在手背上試色，抬頭看鏡頭 |
| **生成 prompt** | `A young woman holds her swatched hand beside her face, her free arm relaxed at her side, raising one eyebrow with one corner of her mouth lifted. Half body, camera level with her chest, lens horizontal. Sleek glossy mocha brown hair, side-parted, collarbone-length with the ends curving slightly inward. Cream cropped fitted knit top, matching off-white high-waisted straight trousers, a trench coat over her arm, gold hoop earrings. Department store beauty floor, glass counters, rows of lipsticks, mirrored columns. Even ceiling light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 這個顏色好漂亮✨<br>但我已經有三支很像的了 |


## Luna Tanaka｜11 件

**模型**：`soul_2` ＋ soul_id `a3dc13ec-16e7-4990-89c6-9e0461db46ef`

**共用身分**：**不寫**。同 Yuna——`soul_id` 已經鎖住臉與體型。
2026-08-27 實測那張甜點店，prompt 裡完全沒寫族裔與身材，童顏與身材比例都正確。

> ⚠️ **英文絕對不要寫 `porcelain skin`**——「白皙如瓷」直譯會把皮膚推成塑膠感。


### LG-01｜甜點店靠窗・臉部近景
`圖`　·　對應 **頭貼**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | 日系可愛妝。明亮輕薄底妝（保留毛孔質感）、平緩淺眉、**粉色系眼影**暈染眼窩與下眼瞼、細內眼線不上揚、**下睫毛看得出來**、**曬傷妝腮紅橫跨鼻樑與兩頰上方**、粉色漸層水潤唇。 |
| **髮型** | 中分及下巴鮑伯，自然垂下，髮尾微微內彎。 |
| **穿著** | 上身：奶油白色**方領**泡泡袖上衣（方領最能呈現胸線又保持可愛感）｜下身：畫面外｜鞋：—｜外層：—｜首飾：珍珠小耳環 |
| **場景環境** | 明亮的甜點店靠窗座位。白牆或淺色磁磚、淺木桌、桌上一塊草莓蛋糕與一杯拿鐵、窗邊有一小束乾燥花。 |
| **機位與構圖** | **臉部＋肩膀近景。**<br>**機位**：在她的眼睛高度，鏡頭保持水平。<br>**距離**：坐在她對面的距離。<br>**構圖**：臉佔畫面約 45%，桌上的蛋糕入鏡下緣。 |
| **光線** | ① 窗光從她側前方**打在臉上**｜② 淺木桌面把光反回下巴｜③ 窗光冷白 vs 店內暖黃｜④ **背景曝光與她的膚色相當** |
| **表情** | **雙手托腮＋歪頭笑。**手肘撐在桌上、雙手托著兩頰把臉擠得更圓；頭往一側傾 20 度；眼睛彎起來。 |
| **肢體與重心** | 坐姿前傾；雙手放在桌上、指尖靠近盤子；肩膀微聳；**頭略歪**。；**垂在臉側的髮尾隨著低頭抬眼的動作晃了一下**。 |
| **情境** | 雙手托腮撐在桌上，對鏡頭笑；蛋糕與拿鐵放桌上，不佔手 |
| **生成 prompt** | `A young woman rests both elbows on the table and cups both cheeks in her palms, squishing her cheeks round, head tilted to one side, smiling toward the camera with her eyes. Close-up of face and shoulders, camera at her eye level, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, centre-parted, ends curving slightly inward. Cream square-neck puff-sleeve top, small pearl earrings. Bright dessert shop window seat, white tiled wall, pale wood table, a strawberry cake and a latte on the table in front of her. Soft side daylight on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.` |
| **Caption 草稿** | —（頭貼用） |

### LG-02｜房間晨光・第一則「她在台北」
`影片 10–15s ＋ start frame`　·　對應 **L-03**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | 幾乎素顏。保留一點粉色唇，其餘乾淨。 |
| **髮型** | 剛睡醒的微亂鮑伯，一側壓扁。 |
| **穿著** | 上身：白色**細肩帶貼身**蕾絲滾邊睡衣上衣｜下身：同色系**短版**睡褲｜鞋：赤腳｜外層：—｜首飾：無 |
| **場景環境** | **明亮乾淨的小套房**。白牆、淺木地板、白色床組（蕾絲滾邊）、窗邊一盆小植物與一隻絨毛玩偶、書桌上放著相機。角落有一個還沒拆完的紙箱（剛搬家的痕跡）。 |
| **機位與構圖** | **3/4 身（膝上）。**<br>**機位**：與她蹲下時的臉同高，鏡頭保持水平。<br>**距離**：站遠一點拍。<br>**構圖**：地板上的光斑從畫面下緣延伸到她手邊。 |
| **光線** | ① 晨光從窗戶進來、地板有光斑，**同時打在臉上**｜② 白牆與淺木地板整體補光｜③ 乾淨明亮的冷白｜④ **背景曝光與她的膚色相當** |
| **表情** | **剛睡醒揉眼睛。**一手揉著眼睛、另一眼半睜；嘴巴打呵欠打到一半；整張臉是鬆的。 |
| **肢體與重心** | 赤腳踩木地板；蹲下時膝蓋併攏、**睡褲與髮尾垂下**；伸手摸光斑的手指張開。；**睡衣的下襬與髮尾在蹲下的動作裡垂落晃動**。；**另一手撐在木地板上支撐蹲下的重心**。；**矮桌上放著她的白瓷杯，蹲下時另一手撐在木地板上**。 |
| **情境** | 光斑在地板上，她赤腳走進畫面，蹲下來，用手摸了一下那道光 |
| **生成 prompt** | `A young woman crouches down with her fingertips resting on a sunlit patch of the floor, her other hand rubbing one eye, mouth caught mid-yawn. Three-quarter body, camera level with her face as she crouches, lens horizontal, shot from well back. A blunt chin-length black bob cut evenly at the jawline, sleep-mussed with one side flattened. White lace-trimmed camisole pyjama top, matching short pyjama shorts, bare feet. Bright clean studio room, white walls, pale wood floor, a small plant and a plush toy by the window. Soft morning light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 台北の朝。<br>光は同じだった。 |

### LG-03｜Mochi 在台北的窗台
`圖`　·　對應 **L-04**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | 淡妝。輕底妝、粉色眼影、曬傷妝腮紅、粉色唇。 |
| **髮型** | 鮑伯，一側別到耳後。 |
| **穿著** | 上身：米白色**合身**細針織上衣（不是袖子過長的 oversized）｜下身：淺色短褲｜鞋：赤腳｜外層：—｜首飾：無 |
| **場景環境** | 房間的窗台。橘色短毛貓趴在窗台上，旁邊有小盆栽。窗外可見鐵窗花與對街公寓。 |
| **機位與構圖** | **半身＋貓同框。**<br>**機位**：與她坐著時的臉同高，鏡頭保持水平。<br>**構圖**：貓在畫面右側窗台上，她從左側探過去。 |
| **光線** | ① 窗光從她側面**打在臉上**｜② 白牆補光｜③ 窗光冷白 vs 室內暖黃｜④ **背景曝光與她的膚色相當** |
| **表情** | **臉靠近貓瞇眼笑。**臉貼近貓的頭、眼睛瞇成月牙；嘴角上揚；完全不看鏡頭，注意力全在貓身上。 |
| **肢體與重心** | 側坐或半跪；一手伸過去摸貓頭、**手指彎曲**；另一手撐在窗台；上半身向貓傾。；**過長的針織袖口垂在手腕外、隨著伸手的動作晃動**。 |
| **情境** | 貓趴在窗台，她的手伸過去摸牠的頭，貓瞇著眼 |
| **生成 prompt** | `A young woman leans in close to an orange cat on the windowsill and scratches its head with one hand, her other hand resting on the sill, her eyes crinkled shut in a smile, her attention entirely on the cat. Half body with the cat in frame, camera level with her face as she sits, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, one side tucked behind her ear. Off-white fitted fine-knit top, light shorts. Bedroom windowsill, small potted plants, an iron window grille and the apartment across the street outside. Soft window light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | Mochi 也搬家了！<br>花了兩個月才習慣🐈 |

### LG-04｜花季公園・櫻花
`圖`　·　對應 **L-05**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | 標準日系可愛妝。粉色眼影、下睫毛明顯、曬傷妝腮紅、粉色漸層唇。 |
| **髮型** | 鮑伯，戴一個奶油色緞帶髮箍。 |
| **穿著** | 上身：白色**方領收腰**蕾絲短袖｜下身：淺粉色格紋**短裙**｜鞋：白色瑪莉珍鞋＋白色短襪｜外層：奶油色開襟針織**披在肩上不穿**｜首飾：緞帶髮箍＋珍珠小耳環 |
| **場景環境** | 花季的公園步道。開滿花的枝條垂在畫面上緣、花瓣落在她肩上、遠處有模糊的公園長椅與行人。 |
| **機位與構圖** | **半身。**<br>**機位**：與她的胸口同高，鏡頭保持水平。<br>**構圖**：開花的枝條垂在畫面上緣，她伸手的動作往畫面上方延伸。 |
| **光線** | ① 花季的柔和天光**均勻打在臉上**｜② 淺色步道地面把光反回下巴｜③ 全場乾淨明亮｜④ **背景曝光與她的膚色相當** |
| **表情** | **接到花瓣的驚訝。**攤開的掌心裡停著一片花瓣，眼睛睜大、嘴呈小 O 形、眉毛抬高。<br>（掛載動作＝掌心的花瓣；**原本寫「然後笑出來」是兩個時間點，靜態圖只 freeze 驚訝那一刻**） |
| **肢體與重心** | **一手伸起接花瓣、手指張開**；另一手提著開衫；重心在後腳；**裙襬與肩上開衫的下襬被風帶起**。 |
| **情境** | 伸手接住一片落下的花瓣 |
| **生成 prompt** | `A young woman pinches a single pink blossom petal between her thumb and index finger beside her cheek, her free arm relaxed at her side, mouth softly open in surprise, eyebrows raised. Half body, camera level with her chest, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, a cream ribbon headband. An opaque white cotton blouse with a structured square neckline, short puff sleeves and a fitted waist, a pale pink checked pleated A-line mini skirt forming one continuous hem around her thighs, pearl earrings. A park path under blossoming branches, petals on her shoulder. Soft daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 花開了🌸<br>今天走了好久才找到這裡 |
| 附註 | **背景路人 1–2 人**：遠處、背向、失焦 |

### LG-05｜公車站・雨停前
`圖　🔬 pilot v2`　·　對應 **L-06**　·　地點層級 **C**

| | |
|---|---|
| **妝容** | 日系可愛妝。明亮輕薄底妝；粉色眼影暈在眼窩與下眼瞼；**下睫毛根根分明**；細內眼線；**曬傷妝腮紅橫過鼻樑與兩頰上方**；粉色漸層水潤唇。 |
| **髮型** | 黑色中分及下巴鮑伯。**髮尾被亭外的風吹得往同一側揚起、有一撮貼在臉頰上**（動勢來源之一）。 |
| **穿著** | 上身：米白色收腰短袖襯衫，前兩顆解開露鎖骨｜**外層：淺藍色薄針織開襟外套，只掛在肩上沒穿進袖子，下襬被風掀起一角**（← **會飄的元素**）｜下身：淺藍色格紋短裙｜鞋：白色瑪莉珍＋蕾絲短襪｜首飾：珍珠小耳環、米色帆布托特包、**透明雨傘收起來拿在手上、傘尖還在滴水** |
| **場景環境** | **雨天也要好看，不能灰撲撲。**候車亭：**彩色路線圖燈箱**、玻璃側板上的雨珠、金屬亭架；亭外：**對街店家亮著的暖色招牌與透出來的燈光**、紅色郵筒、路邊盆栽、濕亮的柏油路映著這些顏色。**明亮通透的雨天，不是陰鬱的雨天。** |
| **機位與構圖** | **3/4 身（膝上）。**<br>**機位**：在她的肚臍高度，鏡頭保持水平。<br>**距離**：站遠一點拍。<br>**構圖**：她站在亭子邊緣，亭外的暖色招牌與濕柏油在她身後虛化。 |
| **光線** | ① 雨後亮起來的天光從亭外**打在臉上**｜② **濕柏油與積水**把對街招牌的顏色反上來｜③ 亭外冷白 vs 對街暖色招牌｜④ **背景曝光與她的膚色相當** |
| **表情** | **對鏡頭比 V ＋歪頭。**手比 V 舉在臉頰旁；頭往同側傾；眼睛彎成月牙——雨天也很開心的那種笑。 |
| **肢體與重心** | **站著等，重心是活的。**重心壓在右腳，**左腳膝蓋微彎、腳尖點地**；骨盆因此微傾（不是雙腳平均站的死板站姿）；左手垂著握傘柄、傘尖朝下滴水；右手勾著托特包帶、手指自然彎曲；肩膀一高一低；**肩上的開襟外套與髮尾被風帶著往同一側動**。 |
| **情境** | 雨快停了，她站在亭子邊緣看外面，正在判斷要不要走 |
| **生成 prompt** | `A young woman stands at a bus shelter, her left hand gripping the curved handle of a folded clear umbrella, its closed canopy hanging straight down beside her thigh, her right hand making a V sign beside her cheek, head tilted. Three-quarter body, camera at her navel level, lens horizontal, shot from well back. A blunt chin-length black bob with even blunt ends along the jawline. An opaque off-white cotton short-sleeve button-front blouse, fastened through the chest, pale blue checked skirt. A bus shelter with a colourful route map lightbox, wet asphalt reflecting the glow of shop signs across the street. Her face clearly lit, the signs keeping their colour. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 台北下雨了☔️<br>雨の台北、こういう日が好き |
| 附註 | 🔬 **preflight**：這件是**鮑伯剪裁幾何的受測件**——頭髮自然垂放、沒有塞耳後／濕髮／半盤，是唯一能乾淨測出底層剪裁的一件。用 `with even blunt ends along the jawline`；**其餘 10 件暫時維持 `cut evenly at the jawline`，等這張驗過再決定要不要全面沿用** |

### LG-06｜可愛系街區・扭蛋機前
`影片 10–15s ＋ start frame`　·　對應 **L-07**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | 標準可愛妝。 |
| **髮型** | 鮑伯，用兩個小髮夾把兩側瀏海別起。 |
| **穿著** | 上身：淺粉色**短版**針織上衣（露一截腰）｜下身：白色**高腰**短褲｜鞋：白色球鞋＋短襪｜外層：牛仔外套繫在腰上｜首飾：珍珠小耳環＋米色小圓包 |
| **場景環境** | 可愛系街區的扭蛋店門口。一整排彩色扭蛋機、櫥窗、彩色招牌、乾淨的人行道。 |
| **機位與構圖** | **半身。**<br>**機位**：與她的胸口同高，鏡頭保持水平。<br>**構圖**：手上的扭蛋在畫面中段，整排扭蛋機在她身後。 |
| **光線** | ① 街上的柔和天光**均勻打在臉上**｜② 扭蛋機的彩色面板反一點顏色在她身上｜③ 天光冷白 vs 店招暖黃｜④ **背景曝光與她的膚色相當** |
| **表情** | **頭朝著扭蛋笑到瞇眼。**雙手捧著打開的扭蛋在胸前，頭朝它低下去，笑到眼睛瞇起來。<br>（掛載動作＝扭蛋；**寫「頭的朝向」不寫「眼睛在看」——閉著眼就不可能同時在看，那是語意矛盾**） |
| **肢體與重心** | 半彎腰在扭蛋機前；雙手捧著扭蛋、手指轉動蛋殼；**轉頭看鏡頭時髮尾甩動**。 |
| **情境** | 轉扭蛋，蛋掉下來，打開一看不是想要的，露出失望的表情，然後又笑了 |
| **生成 prompt** | `A young woman holds an opened gachapon capsule in both hands at chest level, her head angled down toward it as she laughs with her eyes squeezed shut. Half body, camera level with her chest, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, two small clips holding her fringe back. Pale pink cropped knit top showing a sliver of waist, white high-waisted shorts, a denim jacket tied at her waist. A row of colourful gachapon machines behind her, bright shop signage, clean pavement. Soft daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 這個扭蛋轉了五次才轉到😭<br>但很可愛所以沒關係 |
| 附註 | **背景路人 1–2 人**：背向、失焦 |

### LG-07｜遊樂園・旋轉木馬
`圖`　·　對應 **L-08**　·　地點層級 **A**

| | |
|---|---|
| **妝容** | 標準可愛妝，唇色稍亮一階。 |
| **髮型** | 鮑伯，戴一個造型髮箍（貓耳或蝴蝶結）。 |
| **穿著** | 上身：白色**方領**泡泡袖上衣（收腰）｜下身：淺藍色**吊帶短裙**｜鞋：白色瑪莉珍鞋＋蕾絲短襪｜外層：—｜首飾：造型髮箍＋小後背包 |
| **場景環境** | 遊樂園。旋轉木馬、彩色氣球、爆米花桶、遠處的遊行街道與裝飾。 |
| **機位與構圖** | **全身。**<br>**機位**：在她的肚臍高度，鏡頭保持水平。<br>**距離**：站遠一點拍，全身不要靠近拍。<br>**構圖**：腳貼近畫面下方 1/3，旋轉木馬在她身後。 |
| **光線** | ① 遊樂園的柔和天光**均勻打在臉上**｜② 淺色地面把光反回下巴｜③ 天光為主，旋轉木馬燈泡的暖黃在背景｜④ **背景曝光與她的膚色相當** |
| **表情** | **爆米花桶抵在下巴、越過桶緣看鏡頭。**雙臂把爆米花桶抱到下巴下方，身體背對、頭與肩轉回；眼睛越過桶緣看鏡頭，帶著玩心的笑意。<br>（掛載動作＝爆米花桶抵下巴；**原本的「吐舌＋單眼眨眼」是純臉部，與已知失敗的類型相同，已換掉**） |
| **肢體與重心** | 雙臂把爆米花桶抱到下巴下方；**骨盆朝離開鏡頭的方向、上半身轉回四分之三**（不寫完全背對——完全背對的話桶子會跑到身體遠側，鏡頭看不到桶緣）；重心在一腳、另一腳腳尖點地。 |
| **情境** | 捧著爆米花桶，回頭看鏡頭 |
| **生成 prompt** | `A young woman hugs a popcorn bucket up under her chin, her hips angled away from the camera and her upper body turned three-quarters back, looking over the rim toward the camera with a playful smile. Full body, camera at her navel level, lens horizontal, shot from well back. A blunt chin-length black bob cut evenly at the jawline, a cat-ear headband. White square-neck puff-sleeve top, pale blue pinafore skirt, white mary janes with lace socks. Amusement park beside the carousel, coloured balloons, a decorated parade street behind. Soft daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 今天玩得好開心✨<br>爆米花吃了兩桶 |
| 附註 | **背景路人 2–3 人**：背向、失焦、外型與她區隔 |

### LG-08｜浴室鏡前・濕髮
`圖`　·　對應 **L-09**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | **素顏，剛洗完澡**。皮膚微微泛紅有水感，保留一點唇色。 |
| **髮型** | 濕髮鮑伯，貼著臉頰。 |
| **穿著** | 上身：白色浴巾裹身（胸線與腰身自然呈現）｜下身：—｜鞋：赤腳｜外層：—｜首飾：無 |
| **場景環境** | **乾淨明亮的浴室**。白色方形磁磚牆（看得到磁磚縫的質感）、木框鏡、鏡角有一點霧氣、掛著的白毛巾、洗手台上的護膚品。 |
| **機位與構圖** | **半身，拍鏡中反射。**<br>**機位**：在她的眼睛高度，鏡頭保持水平。<br>**構圖**：木框鏡邊入鏡，洗手台上的瓶罐在下緣。 |
| **光線** | ① 浴室頂燈＋鏡側光**均勻打在臉上，幾乎沒有陰影**｜② 白色磁磚牆整體補光｜③ 全場冷白｜④ **背景曝光與她的膚色相當** |
| **表情** | **咬著毛巾角鼓臉頰。**擦頭髮擦到一半停下來，用牙齒咬著毛巾一角，對著鏡子鼓起臉頰。<br>（掛載動作＝毛巾） |
| **肢體與重心** | 一手拿毛巾擦頭髮、**手肘抬起**；另一手扶著洗手台；上半身微前傾；肩膀一高一低。 |
| **情境** | 用毛巾擦頭髮，停下來看鏡子裡的自己 |
| **生成 prompt** | `A young woman holds a towel to her hair with one hand and bites one corner of it between her teeth while looking at herself in the mirror, her other hand resting on the counter, cheeks puffed out. Half body reflected in the mirror, camera at her eye level, lens horizontal. A wet blunt chin-length black bob cut evenly at the jawline, clinging to her cheeks. A white bath towel wrapped around her. Clean bright bathroom, white square tiles, a wooden-framed mirror with a little steam at one corner, skincare bottles on the counter. Broad diffuse frontal light with very low shadow contrast, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | お風呂上がり🛁<br>最喜歡的時間 |

### LG-09｜台式早餐店・豆漿
`圖`　·　對應 **L-13**　·　地點層級 **C**

| | |
|---|---|
| **妝容** | 淡妝。輕底妝、粉色眼影、曬傷妝腮紅、粉色唇。 |
| **髮型** | 中分鮑伯自然放下（與其他件的別耳後、髮夾、髮箍明確區隔）。 |
| **穿著** | 上身：奶油色**合身**薄針織短袖（腰線清楚）｜下身：淺色**短裙**｜鞋：米色平底鞋｜外層：—｜首飾：帆布托特包 |
| **場景環境** | 早餐店。不鏽鋼餐檯、鐵盤、玻璃杯裝的豆漿、紅色塑膠椅。**牆上手寫菜單失焦**（見場景國別驗收規則）。 |
| **機位與構圖** | **半身，人＋食物同框。**<br>**機位**：**在她的眼睛高度或略高**，鏡頭保持水平。<br>**構圖**：豆漿杯捧在下巴前，牆上手寫菜單在她身後。<br>（上目遣い是這件的核心驗收點，機位放在眼睛高度模型比較直接做得到） |
| **光線** | ① 店門口自然光從側前方**打在臉上**｜② 不鏽鋼餐檯反光補下巴｜③ 門口冷白 vs 店內日光燈｜④ **背景曝光與她的膚色相當** |
| **表情** | **上目遣い。**頭略低、眼睛往上看鏡頭；雙手捧著杯子在下巴前；嘴角微揚——日系經典。 |
| **肢體與重心** | 雙手捧著玻璃杯在胸前；手肘靠桌；上半身前傾；肩膀微聳。；**薄針織的袖口與髮尾隨著前傾垂下晃動**。 |
| **情境** | 雙手捧著豆漿杯，正要喝 |
| **生成 prompt** | `A young woman holds a glass of soy milk with both hands in front of her chin, head slightly lowered, eyes looking up over the rim toward the camera, smiling with her eyes. Half body with the food in frame, camera at her eye level or slightly above. A blunt chin-length black bob cut evenly at the jawline, centre-parted. Cream fitted thin-knit short sleeve, a light pleated A-line mini skirt with one continuous hem around her thighs. A breakfast shop, a stainless steel counter, red plastic stools, the wall menu behind her out of focus. Daylight from the doorway on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 早餐吃這個🥛<br>好喝…真的很好喝 |

### LG-10A｜浴衣・祭典參道（全身）
`圖`　·　對應 **L-20**　·　地點層級 **A**

> **2026-08-27 拆件。**原本 LG-10 的景別寫「全身＋半身各一」，
> 但共用規則是一段 prompt 生一張——規格自己對不上。拆成 A／B 兩件，
> 整批從 20 件變成 **21 件**。

| | |
|---|---|
| **妝容** | 標準可愛妝，唇色帶一點紅，祭典燈光下顯色。 |
| **髮型** | 鮑伯盤起一半，插一支和風髮簪，鬢角留兩撮。 |
| **穿著** | 上身＋下身：**淺藍底白色朝顏花紋浴衣**，深藍色半幅帶**綁緊收腰**、衣襟自然貼合（浴衣是靠腰帶與衣襟呈現線條的）｜鞋：木屐＋白足袋｜首飾：和風髮簪＋巾着小提包 |
| **場景環境** | 夏日祭典的神社參道。**乾淨明亮的木造鳥居**（不是斑駁老舊）、兩側掛著的紙燈籠、祭典攤位（金魚撈、蘋果糖、章魚燒）、遠處的人群。 |
| **機位與構圖** | **全身。**<br>**機位**：在她的肚臍高度，鏡頭保持水平。<br>**距離**：站遠一點拍。<br>**構圖**：腳貼近畫面下方 1/3，鳥居在她身後。 |
| **光線** | ① 攤位與紙燈籠的暖色光**打在臉上**｜② 參道地面把暖光反回下巴｜③ 全場暖色，天空還留一點藍｜④ **臉清楚受光、背後的燈籠攤位保留細節**（這件不用「背景與膚色等亮」，會失去夜祭的層次） |
| **表情** | **走著被叫住、回頭笑。**寫成**動作中的瞬間**（走開→回頭），不是靜態的身體擺放；一手舉蘋果糖在臉頰旁，另一手自然垂放。<br>（掛載動作＝蘋果糖；**2026-08-28 改用 A/B 的 A 版**——理由是 A 在 4 張裡沒有 hard defect，屬較低風險，**不是已證實動作寫法較優**） |
| **肢體與重心** | 重心在後腳；骨盆朝參道深處；上半身與頭轉回鏡頭；一手舉蘋果糖。 |
| **情境** | 走在參道上回頭 |
| **生成 prompt** | `Walking away down the festival approach, a young woman glances back over her shoulder mid-stride, holding a candy apple beside her cheek with one hand, her free arm relaxed at her side, laughing. Full body, camera at her navel level, shot from well back. A blunt chin-length black bob cut evenly at the jawline, half-pinned up with a Japanese hairpin. A pale-blue floral Japanese yukata, an ankle-length wrap robe with the left panel crossed over the right, a wide flat navy obi sash, wooden geta. A wooden torii, paper lanterns overhead, food stalls. Her face clearly lit, the lantern-lit stalls keeping visible detail. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 夏祭り🎐<br>蘋果糖比想像中大顆 |
| 附註 | 這是 Luna 視覺變化最大的一組。<br>**⚠️ 這件的場景在日本，是刻意的**——歸為「回日本的時候」類型（對應 Yuna 的 YG-06 汗蒸幕）。**其餘 Luna 的件全部是台北。**<br>戶外件，第一張出來要跟 LG-04／06／07 互相比對有沒有出現同一個場景模板 |

### LG-10B｜浴衣・蘋果糖（半身）
`圖`　·　對應 **L-21**　·　地點層級 **A**

| | |
|---|---|
| **妝容** | 標準可愛妝，唇色帶一點紅，祭典燈光下顯色。 |
| **髮型** | 鮑伯盤起一半，插一支和風髮簪，鬢角留兩撮。 |
| **穿著** | 上身＋下身：**淺藍底白色朝顏花紋浴衣**，深藍色半幅帶**綁緊收腰**、衣襟自然貼合（浴衣是靠腰帶與衣襟呈現線條的）｜鞋：木屐＋白足袋｜首飾：和風髮簪＋巾着小提包 |
| **場景環境** | 夏日祭典的神社參道。**乾淨明亮的木造鳥居**（不是斑駁老舊）、兩側掛著的紙燈籠、祭典攤位（金魚撈、蘋果糖、章魚燒）、遠處的人群。 |
| **機位與構圖** | **半身。**<br>**機位**：與她的胸口同高，鏡頭保持水平。<br>**構圖**：蘋果糖在臉頰旁，紙燈籠在她身後虛化。 |
| **光線** | ① 紙燈籠的暖光**打在臉上**｜② 參道地面反光補下巴｜③ 全場暖色｜④ **臉清楚受光、背景燈籠保留細節** |
| **表情** | **舉著蘋果糖笑。**一手把蘋果糖舉在臉頰旁、另一手扶著髮簪；笑到眼睛彎。<br>（掛載動作＝蘋果糖＋扶髮簪） |
| **肢體與重心** | 站定，重心在一腳；兩手都有事做（舉糖、扶簪）。 |
| **情境** | 停下來給鏡頭看手上的蘋果糖 |
| **生成 prompt** | `A young woman holds a candy apple up beside her cheek with one hand and steadies the Japanese hairpin in her half-up bob with the other, laughing with her eyes crinkled. Half body, camera level with her chest, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, half-pinned up with a Japanese hairpin, two strands left at her temples. A pale-blue floral Japanese yukata, an ankle-length wrap robe with the left front panel crossed over the right, secured by a wide flat navy obi sash. Paper lanterns strung overhead behind her, a blurred food stall. Her face clearly lit, the lantern-lit background keeping visible detail. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 這個顏色好可愛🍎 |
| 附註 | 與 LG-10A 同一天同一套，**拆兩則發沒問題**（景別與構圖差異夠大）。同屬「回日本的時候」類型。 |

## ⚠️ 場景國別的驗收規則（2026-08-28 定案）

**兩人的設定都是住台北**（`character.md`、`CAMPAIGN_PLAN.md` 皆然），
而且 `GENERATION_PLAN_B1.md` 自己就寫著「觀眾看不懂韓文／日文就沒有意義」。
先前一度打算「接受場景生成在首爾」，**已撤回**——那跟企劃前提衝突。

| 項目 | 規則 |
|---|---|
| **prompt 裡的國別詞** | **不寫**。`Taiwanese` 這種抽象詞實測無效（YG-03 照樣生出韓國），寫了只是佔字數 |
| **改用什麼** | **具體的食物與店內物件**（蛋餅、冰紅茶、關東煮機台、不鏽鋼餐檯、紅色塑膠椅） |
| **背景文字** | **一律失焦**。招牌、菜單、路線圖都不要成為需要讀字的元素 |
| **驗收** | 畫面裡出現**清楚可辨的韓文／日文招牌或商品牆** → **Hard Reject** |
| **例外** | YG-06 汗蒸幕是刻意的韓國場景，歸「回韓國的時候」類型 |
| **文字硬撞無效時** | 改走 production route（局部換背景／改成地點不可辨但敘事合理的室內近景），**不要重寫人設** |

---

## 執行順序

### 光線公式那一輪已經跑完了

原本這裡寫的是「先用 YG-06 巷弄與 LG-05 公車站驗證五段光線公式（2 張，≈16 credits）」。
**那一輪已經跑完，而且結論是公式本身有問題**——第 ④ 段「曝光取捨」正是逆光的主因之一。
成本估算也錯了兩個數量級：2K 一張實際是 **0.12 credits**，不是 8。

已驗證與待驗證的整理如下。

### 已經驗證過的（6 張，0.72 credits）

| 項目 | 狀態 |
|---|---|
| 不寫族裔與身材數字 | ✅ 6/6 身分與身材都正確 |
| `camera at her navel level, lens horizontal, shot from well back` | ✅ 6/6 比例正確，沒有頭大腿短、沒有俯拍 |
| `背景曝光與膚色相當`（正向寫法） | ✅ 室內 3 張都不逆光 |
| 表情綁實體動作 | ✅ 綁了的成功，沒綁的失敗（4 個案例一致） |
| 否定句 | ❌ 實測無效，已從全部 spec 刪除 |
| 巷弄街拍 | ❌ Yuna 的 `soul_id` 有固定畫面慣性，已換掉 YG-06 |

### 還沒驗證的（生成時要注意）

| 項目 | 說明 |
|---|---|
| **「會飄的元素」** | 3/3 沒有被執行——Yuna 的薄襯衫兩次整件消失、Luna 的裙子沒被風掀起。**靜態圖大概做不出「正在飄」**。各 spec 的「肢體與重心」欄還留著這類描述，但**不要把它當成驗收標準** |
| **服裝清單排最後的品項** | 街拍那幾張排最後的會被丟掉；室內那幾張全中。可能跟品項數量有關，還沒單獨測 |
| Luna 有沒有同樣的畫面慣性 | 只測了 1 張（甜點店），畫面乾淨、沒有重複跡象，但 n=1 不能下定論。她的戶外件（LG-04／06／07／10）**每件第一張出來要比對有沒有變成同一條街** |

### 往下怎麼跑

1. 你核准 spec → **一件生兩張**（兩次獨立生成，不是 `count=2`），用該件的「生成 prompt」那一行
2. **一張成功就選片**；**兩張同方向失敗 = 系統性偏差，立刻停這件、改 prompt 再跑**，不要用原句繼續抽
3. 圖確認 → 影片 start frame → 影片（`kling3_0`，單鏡頭，`sound=on`）
4. 每批記一行 `cost-log.md`，**用 `transactions` 逐筆對帳，不要用餘額差**

**成本估算**：圖 **21 件 × 2 張 = 42 張 ≈ 5.04 credits**（2026-08-28 改成一件生兩張選一張，見 `SEXY_SCENE_LIBRARY.md` 第 21 點）｜系統性 drift 需改 prompt 重跑的 buffer **取 6 件 × 2 張 = 12 張 ≈ 1.44**｜影片另計

---

## 核准方式

直接講編號：`YG-01`～`YG-10`、`LG-01`～`LG-09`、`LG-10A`、`LG-10B`（**共 21 件**）。
單項要改也可以指名欄位——例如「LG-07 的穿著換掉」「YG-10 妝容再淡一點」。
