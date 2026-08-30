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
| **場景環境** | 明亮咖啡廳靠窗座位。**白牆＋窗光虛化**。<br>（**2026-08-28 刪掉桌面的拿鐵與手機**——臉＋肩膀近景根本看不到桌面，寫了會逼模型拉遠景別；也不再帶窗外街景，避免文字） |
| **機位與構圖** | **臉部＋肩膀近景。**<br>**機位**：在她的眼睛高度，鏡頭保持水平。<br>**距離**：坐在她對面的距離，不要湊太近。<br>**構圖**：臉佔畫面約 45%，留白留在她視線的方向。 |
| **光線** | ① 落地窗自然光從她左前方進來，**打在臉上**｜② 白色桌面把光反回下巴與頸部｜③ 窗光冷白 vs 店內暖黃軌道燈落在她身後牆面｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（白牆回柔和冷色填光到陰影側）｜曝光：取捨（窗外街景失細節）｜色溫：不適用（單一窗光） |
| **表情** | **撥髮回眸。**一手正把頭髮撥到耳後，同時轉頭看鏡頭；嘴角單邊上揚的淺笑；頭往撥髮的那一側微傾。<br>**硬驗收＝一手把頭髮撥到耳後＋轉頭看鏡頭。臉部細節（眼型／嘴型／眉毛／臉頰）一律列 soft observation，不作淘汰依據。** |
| **肢體與重心** | 坐姿，上半身微向前傾靠著桌緣；**右手正把頭髮撥到耳後——動作中，不是撥完**；左手托著杯子；肩膀一高一低。；**撥開的那撮頭髮還垂在指縫間晃動**。 |
| **情境** | 剛坐下，把頭髮撥到耳後，看向鏡頭 |
| **生成 prompt** | `A young woman tucks a strand of hair behind her ear and turns to look at the camera, one corner of her mouth lifted, head tilted toward that hand. Close-up of face and shoulders, camera at her eye level, lens horizontal. Collarbone-length soft wavy mocha brown hair with see-through wispy bangs. Cream fitted fine-knit tee, thin gold necklace, small gold hoops. Bright cafe window seat, a plain white wall and soft window light blurred behind her. Soft cool daylight from her front-left landing on her face, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.` |
| **覆核指紋** | sha1:e71845f523c7（已核准成品，prompt 凍結） |
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
| **光學設定** | 反射面：具名（淺木地板把晨光反回下巴）｜曝光：取捨（窗外壓成無細節）｜色溫：分裂（窗光冷白 vs 室內暖） |
| **表情** | **端著杯子瞇眼笑。**單手把馬克杯舉到嘴邊喝一口；另一手扠在腰上；眼睛還沒完全張開、嘴角鬆鬆揚起。<br>**硬驗收＝單手舉杯到嘴邊＋另一手有明確位置。臉部細節列 soft observation。**<br>（**2026-08-28 修正**：原本寫「雙手捧杯」＋「舉到嘴邊」，**兩者物理上矛盾**——喝水是單手動作，捧在下巴前才是雙手動作（YG-06 那樣）。兩張都單手，是規格自己不成立。<br>**已收 _b；prompt 文字已對齊實際採用的畫面。若日後重跑，需先送覆核。**） |
| **肢體與重心** | 赤腳走路有重量感；端杯子的手指自然彎曲；喝一口時肩膀微微下沉（吐氣）；**針織外套從單肩滑下一點**。；**左手把滑下肩的針織外套往上拉了一下**。；**右手端著馬克杯、左手把滑下肩的針織外套往上拉了一下——兩手都有事做**。 |
| **情境** | 她端著馬克杯走到窗邊，站定，看窗外，喝一口，轉頭看鏡頭 |
| **生成 prompt** | `A young woman stands at the window lifting a mug to her mouth with one hand, her other hand resting on her hip, eyes still narrowed from sleep, a loose easy smile. Three-quarter body, camera at her navel level, lens horizontal, shot from well back. Collarbone-length mocha brown hair, sleep-mussed, see-through bangs flattened with one tuft sticking up. White fitted camisole, high-waisted grey cotton shorts, beige cardigan slipping off one shoulder. Small bright apartment, white walls, pale wood floor, unmade white bed. Soft morning light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **覆核指紋** | sha1:c21375fbd1b6（已核准成品，prompt 凍結） |
| **Caption 草稿** | 台北的早上☀️<br>光剛好照到腳 |

### YG-03｜陽台・收乾淨的衣服
`圖`　·　對應 **Y-05**　·　地點層級 **C**

> **2026-08-28 換件。**原本是「超商」，**停損觸發後撤下**——
> 兩張都出現清楚韓文，而且來源不是背景招牌（那些我已經拿掉了），
> 是**她手上那個印字的紙杯**與層架上的商品盒。
> **超商這個場所的定義就是「賣有包裝的商品」，不適合這個 `soul_id`。**
>
> 換成陽台收衣服：**毛巾與襯衫都是素面織品，整個場景沒有任何印刷品或包裝**，
> 同時保住原本的兩個功能——**半身自拍**（全批只有兩件）與 **C 級日常地點**。

| | |
|---|---|
| **妝容** | 淡妝。透明感薄底妝、淡眉、nose blush 很淡、粉色潤色護唇。戴黑框眼鏡。 |
| **髮型** | 低馬尾，see-through 瀏海留著，鬢角兩撮碎髮垂下。（沿用原 YG-03，維持角色連續性） |
| **穿著** | 上身：**短版**灰色短袖上衣（露一截腰）｜下身：黑色**高腰**短褲｜鞋：畫面外｜首飾：黑色細框眼鏡（沿用原 YG-03） |
| **道具** | 毛巾（素面白）**core-visible**｜黑細框眼鏡 **core-visible**｜手機 **off-frame**（自拍前提，佔一隻手但不入鏡）｜晾衣桿與素面襯衫 場景物件 |
| **場景環境** | 老公寓的窄陽台。白色油漆牆、**鐵窗花**、不鏽鋼晾衣桿上掛著**素面**毛巾與襯衫、對街公寓外牆虛化。<br>**整個場景不放任何有印刷、包裝、標籤的東西。** |
| **機位與構圖** | **半身自拍。**<br>**機位**：手機伸直手臂舉在略高於眼睛的位置。<br>**構圖**：晾衣桿與鐵窗花在她身後，對街虛化。 |
| **光線** | ① 陰天均勻天光**正面打亮臉**｜② 白牆整體補光｜③ 全場冷白｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（白牆回冷色填光）｜曝光：低反差（有遮蔽陽台、霧面窗板）｜色溫：不適用（單一天光） |
| **人物入鏡** | 私密場景（自家陽台）——只有本人 |
| **多樣性** | 姿勢：**A 動作中**（正在把毛巾從晾衣桿上取下）｜相機：**1 自拍**｜視線：看鏡頭｜手在臉旁：否 |
| **不可刪除措辭** | `The frame contains exactly one visible hand; her phone and her camera-holding hand stay outside the frame.`（R8a 封住自拍手與手機入鏡）<br>`high crew neckline`（R13 領口尺度橫向規則，2026-08-29 補掃） |
| **凍結瞬間** | 伸手把一條白毛巾從晾衣桿上拉下來的那一瞬間，手臂還舉著，轉頭對鏡頭笑。 |
| **手部任務** | 拍攝手／鏡外手：持手機自拍，**off-frame**（仍佔一隻解剖學的手）<br>可見手 A：舉起、正把白毛巾從晾衣桿上拉下<br>可見手 B：**N/A**——兩隻手已用完 |
| **表情** | 對鏡頭笑，眼睛自然。**全列 soft observation。** |
| **肢體與重心** | 站著，重心在一腳；上半身微轉向手機那一側。 |
| **硬驗收** | ① 自拍構圖成立且**手機不入鏡** ② **只有一隻可見手**，且**手臂是舉起的、正在取毛巾**（不是抱在胸前）③ 畫面無任何印刷文字 ④ 半身比例 ⑤ **高圓領、不露胸線**（2026-08-29 補：R13 的領口橫向規則當時只套用在判 REVISE 的件，已放行的沒有回頭重掃） |
| **創意備註（不送模型／不驗收）** | 無（本件原本就沒有飄動描述） |
| **整併紀錄（2026-08-29）** | **2026-08-29 改姿勢**：原本是「毛巾已抱在胸前」＝靜止站定。改成取下的動作中。<br>（先前把「取下」刪掉是因為與「抱著」並存＝兩個時間點；現在只留取下這一個瞬間，不違反 D-11）<br><br>—— 以下為先前紀錄 ——<br>刪掉「取毛巾的手臂抬起」（與『抱在胸前』是兩個時間點，且是重複的手部指派） |
| **生成 prompt** | `In a phone selfie, a young woman pulls a plain white towel down off the drying pole, arm still raised, smiling at the camera. The frame contains exactly one visible hand; her phone and her camera-holding hand stay outside the frame. Close half-body framing, camera just above her eye level, the balcony behind her falling out of focus. Collarbone-length mocha brown hair in a low ponytail, see-through bangs. An opaque grey fitted cropped cotton tee with a high crew neckline, high-waisted black shorts, black-rimmed glasses. A narrow covered balcony, a white painted wall, an iron window grille, plain towels on the pole. Flat overcast daylight on her face, her face evenly exposed, the white wall bouncing cool fill onto her jaw, staying slightly darker than her skin. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 曬乾的味道✨<br>今天終於記得收 |
| 附註 | ⚠️ **這是新寫的 spec，尚未送覆核、尚未生成。**<br>設計重點：**沒有任何印刷品來源**——毛巾與襯衫寫明 `plain unprinted`，場景不放商品、招牌、包裝。<br>🔴 **未驗證的假設**：`iron window grille`（鐵窗花）在 LG-03 上讀起來像台灣，但那是 **Luna 的 `soul_id`**——**跨角色不能當證據**，Yuna 身上會不會一樣未知。 |

### YG-04｜梳妝台護膚・素顏
`圖`　·　對應 **Y-06**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | **完全素顏。**皮膚要看得到毛孔與 T 字部位的自然油光，眉毛保留原生形狀，唇是自然色。 |
| **髮型** | 全部往後用鯊魚夾夾起，額前留幾根碎髮垂下。 |
| **穿著** | 上身：白色**細肩帶貼身**背心（鎖骨、肩線、胸型自然可見——這是護膚照的重點）｜下身：畫面外｜鞋：—｜外層：—｜首飾：手腕上的黑色髮圈 |
| **場景環境** | 白色大理石梳妝台面、白色磁磚牆。護膚品瓶與化妝刷**虛化在她身後**，不刻意排整齊。**不放鏡子。** |
| **機位與構圖** | **臉部＋上半身近景，直接拍。**<br>**機位**：在她的眼睛高度，鏡頭保持水平。<br>**構圖**：台面上的瓶罐虛化在她身後。<br>（**2026-08-28 取消鏡面反射**——`soul_2` 沒有 negative prompt，**無法穩定排除拍攝設備入鏡**；鏡面不是這件的核心，不值得為它承擔 Hard Reject 風險） |
| **光線** | ① 浴室頂燈＋鏡側光**均勻打在臉上，幾乎沒有陰影**｜② 白色大理石台面把光反回下巴｜③ 全場冷白｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（白色大理石檯面微弱中性回彈，只抬陰影）｜曝光：低反差（白牆室內柔光）｜色溫：不適用（單一柔光源） |
| **表情** | **閉眼享受。**眼睛完全閉起、眉頭鬆開；嘴角放鬆地微揚；下巴微抬（把精華液按進臉頰的那一下）。 |
| **肢體與重心** | **雙手掌心貼著臉頰往上按**；手肘抬起；上半身微前傾靠近鏡子；肩膀放鬆下沉。 |
| **情境** | 用手掌把精華液按進臉頰，眼睛微閉 |
| **生成 prompt** | `A young woman presses serum into her cheek with her fingertips, eyes closed, chin lifted, mouth relaxed into a small smile. Close-up of her face and shoulders, camera at her eye level, lens horizontal. Collarbone-length mocha brown hair clipped back with a claw clip, a few strands loose at her forehead. White fitted camisole. A white marble vanity counter, white tiled wall, skincare bottles and brushes softly blurred behind her. Broad diffuse frontal light with very low shadow contrast, background exposed the same brightness as her skin. Visible skin pores, natural skin texture, subtle film grain.` |
| **覆核指紋** | sha1:0cbb5a24ec11（已核准成品，prompt 凍結） |
| **Caption 草稿** | 洗完澡最舒服☺️<br>씻고 나서 |

### YG-05｜捷運月台・隨手自拍
`圖`　·　對應 **Y-07**　·　地點層級 **C**

| | |
|---|---|
| **妝容** | 日常妝。透明感底妝、淡眉、奶茶色暈染眼影、眼頭 V 字打亮、nose blush、blurred lips 米棕。 |
| **髮型** | **側分 sleek 直順**（2026 明顯回歸的一條線），髮尾帶微層次。 |
| **穿著** | 上身：黑色**貼身短袖針織**（腰線清楚）｜下身：**卡其色高腰短裙**｜鞋：白色球鞋｜外層：—｜首飾：銀色細手鍊＋米色迷你方包斜背 |
| **場景環境** | **地點刻意不可辨。**背景是灰色平面隔板鋪滿畫面，**不放任何招牌、路線圖、站名牌**。<br>（2026-08-28 定案：捷運月台的識別度換掉錯國風險——Penny 已接受。等車的情境由 Caption 承擔，畫面不必證明是捷運） |
| **機位與構圖** | **半身自拍。**<br>**機位**：手機伸直手臂舉在略高於眼睛的位置。<br>**構圖**：人在畫面偏左，右側帶到月台門與路線圖燈箱。 |
| **光線** | ① 月台天花板燈管**均勻打亮臉部**｜② 月台門玻璃反一層冷光｜③ 冷白為主，路線圖燈箱一小塊彩色｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：不適用（灰隔板無明顯色彩或亮度回彈）｜曝光：低反差（均勻站體燈）｜色溫：不適用 |
| **表情** | **看著手機鏡頭嘟嘴。**看進手機鏡頭，另一手把瀏海撥開；韓系無聊嘟嘴，眼神平淡。<br>（掛載動作＝撥瀏海；**手機是拍攝者，不會出現在畫面裡**）<br>**硬驗收＝自拍構圖＋另一手撥瀏海。臉部細節（眼型／嘴型／眉毛／臉頰）一律列 soft observation，不作淘汰依據。** |
| **肢體與重心** | 重心在一腳、**另一腳腳尖外開**；一手舉手機、一手勾著包帶；肩線傾斜。；**月台的通風把她的髮尾往一側吹動**。 |
| **情境** | 等車，順手拍一張，表情有點無聊 |
| **生成 prompt** | `In a phone selfie, a young woman pushes her fringe aside with her free hand, lips softly pursed, a bored flat gaze. Close half-body phone selfie from just above her eye level. Collarbone-length sleek straight mocha brown hair, side-parted. Fitted black short-sleeve knit, a khaki high-waisted pleated A-line mini skirt forming one continuous hem around her thighs. Smooth grey platform screen doors with repeating vertical seams fill the soft background edge to edge. Flat even station light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **覆核指紋** | sha1:d48066b54295（已核准成品，prompt 凍結） |
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
| **道具** | 甜米露紙杯 **core-visible**（掛載動作）｜頭上毛巾折成羊角 **core-visible**｜矮桌與坐墊 場景物件 |
| **場景環境** | 汗蒸幕的休息大廳。淺色木地板、矮桌、幾個坐墊、遠處的睡眠區與販賣機、牆上的韓文告示。乾淨明亮，不是陰暗的澡堂。 |
| **機位與構圖** | **全身（坐姿）。**<br>**機位**：在她坐著時的眼睛高度，鏡頭保持水平。<br>**距離**：站遠一點拍。<br>**構圖**：她盤腿坐在木地板上，身後帶到休息大廳的縱深。 |
| **光線** | ① 休息大廳的暖色頂燈**均勻打在臉上**｜② 木地板把暖光反回下巴｜③ 全場暖黃，這件刻意跳出她的冷白區間｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（木地板把暖光反回下巴）｜曝光：低反差（室內均勻頂燈）｜色溫：不適用（全場暖色） |
| **人物入鏡** | 公共場景——必寫背景路人（汗蒸幕休息大廳） |
| **多樣性** | 姿勢：**D 非站坐體位**（盤腿坐地、上身後仰）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否 |
| **不可刪除措辭** | `with one hand planted on the floor behind her and her other hand relaxed on one knee`（R10/R11 具名接觸面＋補上原本漏寫的第二隻手）<br>`both bare feet are visible`（R13 景別：Full body 有裁腳反例，改列具體可見部位） |
| **凍結瞬間** | 盤腿坐在木地板上，蒸完澡整個人鬆掉，上半身往後仰、單手撐在身後地板上，臉朝上笑出來，紙杯放在身旁地上。 |
| **手部任務** | 可見手 A：撐在身後的木地板上，支撐後仰的上半身<br>可見手 B：自然放在膝上<br>紙杯**放在地上**，不佔手 |
| **表情** | 上目遣い——眼睛越過杯緣往上看鏡頭、彎成月牙。**眼型與嘴型列 soft observation。** |
| **肢體與重心** | 盤腿坐在地上，背微駝、放鬆；一邊肩膀比另一邊低。 |
| **硬驗收** | ① **完整頭部、盤腿與雙腳都可見，坐姿周圍保留地板** ② 上半身後仰、一手撐地 ③ **雙眼閉起、臉朝上，不看鏡頭**<br>（**2026-08-29 依 R12 改為閉眼**——原本只寫「臉朝上」沒有畫面內視線目標，會像 LG-01 一樣退回直視鏡頭。閉眼直接消除畫外對焦問題，比虛構一個畫外目標自然）④ 頭上毛巾羊角可見 |
| **創意備註（不送模型／不驗收）** | 無 |
| **整併紀錄（2026-08-29）** | **2026-08-29 改姿勢**：原本「雙手捧杯在下巴前＋越過杯緣看鏡頭」與 LG-09、LG-06 三件幾乎同構圖。改成把杯子放下、身體後仰的放鬆姿態——**這才是「蒸完整個人都軟掉」的樣子**。表情錨點由物件改為**動作**（後仰撐地）<br><br>—— 以下為先前紀錄 ——<br>「雙手都在紙杯上」由肢體列移入手部任務列（原本兩列重複宣告同一件事） |
| **生成 prompt** | `A young woman sits cross-legged on a heated floor, leaning back with one hand planted on the floor behind her and her other hand relaxed on one knee, shoulders dropped, face tilted upward in a loose open-mouthed laugh with her eyes squeezed shut, a paper cup resting on the floor beside her. Her complete head, crossed legs, and both bare feet are visible, with floor visible around her seated body, shot from her three-quarter back at her seated eye level, shot from well back. Collarbone-length mocha brown hair in a low bun, damp strands at her temples. A grey crew-neck sauna tee and shorts, a towel folded into sheep horns on her head, bare feet. A bright sauna rest hall. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm ceiling light on her face, the wooden floor bouncing warm fill up onto her chin, the hall behind her staying readable and slightly darker. Natural skin texture, subtle film grain.` |
| **Caption 草稿** | 蒸完整個人都軟掉了🫠<br>甜米露是最好喝的部分 |
| 附註 | 這是這批唯一的暖光場景，刻意跳出她的冷白區間。<br>**⚠️ 這件的場景在韓國，是刻意的**——歸為「回韓國的時候」類型內容（對應 Luna 的「回日本的時候」）。**其餘 Yuna 的件全部是台北，畫面裡不應出現可辨識的韓文招牌。** |

### YG-07｜客廳地板・什麼都沒發生
`影片 10s ＋ start frame`　·　對應 **Y-09**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | 素顏到淡妝之間。只有眉毛與粉色潤色護唇。 |
| **髮型** | 鯊魚夾隨手夾一半，下半放下（與 YG-04 的全夾起區隔）。 |
| **穿著** | 上身：米色**細肩帶**家居背心｜下身：同色系**短版**棉質短褲｜鞋：**畫面外**（原寫赤腳，2026-08-29 依 R8a 移出——半身坐姿寫赤腳會誘使模型拉遠或硬把腳塞進構圖，而赤腳不是本件硬驗收）｜外層：—｜首飾：無 |
| **道具** | 手機 **core-visible**（她在滑，入鏡）｜零食袋 **core-visible**｜地上攤開的雜誌 場景物件｜角落電風扇 場景物件 |
| **場景環境** | 小套房的客廳地板。矮沙發、地上攤開的雜誌、旁邊拆開的零食袋、電風扇在角落轉。 |
| **機位與構圖** | **半身坐姿。**<br>**機位**：與她坐在地上時的臉同高，鏡頭保持水平。<br>**構圖**：地上的雜誌與零食袋入鏡下緣。 |
| **光線** | ① 窗戶漫射光從側面**打在臉上**｜② 淺色地板反光補下巴｜③ 窗光冷白 vs 角落一盞暖黃立燈｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（淺色地板回彈補下巴）｜曝光：取捨（窗邊失細節）｜色溫：分裂（窗光冷白 vs 角落暖立燈） |
| **人物入鏡** | 私密場景（自家客廳）——只有本人 |
| **多樣性** | 姿勢：**D 非站坐體位**（坐地板）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否 |
| **不可刪除措辭** | `Exactly two hands are visible.`（R8a 鎖定可見手數） |
| **凍結瞬間** | 坐在地板上專心滑手機，一手伸進零食袋裡摸，嘴裡還在嚼、一邊臉頰鼓著，完全沒注意到有人在拍。 |
| **手部任務** | 可見手 A：拿著手機在滑（手機入鏡，這件不是自拍）<br>可見手 B：伸進零食袋<br>無第三個手部任務 |
| **表情** | 嘴裡還有零食、一邊臉頰鼓著；眉毛抬起看鏡頭。**眼型與嘴型列 soft observation。** |
| **肢體與重心** | 盤腿側坐在地板上，**背微駝**（真實的放鬆姿勢，不是挺直）。 |
| **硬驗收** | ① 坐在地上 ✅ ② 一手滑手機、一手伸進零食袋（**可見手剛好兩隻**）✅ ③ **視線在手機上、不看鏡頭** ✅ ④ ~~一邊臉頰鼓著~~ → **改列 soft observation**（Penny 2026-08-29 裁決）<br>（**這一項當初分類就錯了**：臉頰鼓著是臉部表情細節，本專案慣例是「臉部細節一律列 soft observation」，D-06 也說臉部指令低可靠。2/2 未達成不是生成失敗，是驗收標準訂錯。）<br>**造型漂移（記錄，非驗收）**：髮型「上半束起」2/2 全部放下。prompt 寫 `the top half clipped up`，**沒有寫出髮夾這個實體物件**——對照 YG-04 的 `clipped back with a claw clip` 2/2 成功。<br>**本件 prompt 自此凍結**（成品用現行版本產出） |
| **創意備註（不送模型／不驗收）** | 角落電風扇把垂下的髮絲吹得輕輕飄動——**靜態圖無法表現，不送模型、不驗收** |
| **整併紀錄（2026-08-29）** | **2026-08-29 改視線**：原本抬眉看鏡頭。「什麼都沒發生」這個主題，**她沒在理鏡頭才成立**<br><br>—— 以下為先前紀錄 ——<br>刪掉「一手撐地」（與滑手機＋零食袋合計為三隻手）。原本表情列與肢體列各自指派了不同的兩隻手 |
| **生成 prompt** | `A young woman sits on the floor absorbed in her phone held in one hand, her other hand reaching into a snack bag, one cheek full mid-chew, her eyes down on the screen. Exactly two hands are visible. Half body, camera level with her face as she sits. Collarbone-length mocha brown hair, the top half clipped up. A beige camisole and short cotton shorts. A living room floor, a low sofa, magazines. Cool window light on her face, a warm lamp glowing behind her, the pale floor bouncing fill onto her chin. Her face is clearly exposed with natural skin texture; the window is the brightest area, only its smallest highlights reaching white. Subtle film grain.` |
| **覆核指紋** | sha1:f42571155f50（R12 逐件 PASS） |
| **Caption 草稿** | 今天不想出門<br>아무것도 안 함 |

### YG-08｜台式早餐店・第一則吃
`圖`　·　對應 **Y-10**　·　地點層級 **C**

| | |
|---|---|
| **妝容** | 日常妝。薄透底妝、淡眉、淡奶茶眼影、nose blush、粉色唇釉。 |
| **髮型** | 側分長軟波浪，左側夾一個珍珠小髮夾。 |
| **穿著** | 上身：淺藍色短袖襯衫，**下擺在腰際打結**（露一截腰）｜下身：白色**高腰**短褲｜鞋：白色球鞋｜首飾：小珍珠耳環＋珍珠髮夾<br>（**已刪掉「前兩顆解開」**——`top buttons open` 是把領口拉低的高風險字，LG-05 已因此出過事） |
| **道具** | 蛋餅 **core-visible**（掛載動作）｜冰紅茶玻璃杯 **core-visible**（前景下緣）｜鐵盤 **core-visible**｜珍珠髮夾 **core-visible**｜珍珠耳環 optional |
| **場景環境** | 早餐店。不鏽鋼餐檯、紅色塑膠椅、鐵盤上的蛋餅、玻璃杯裝的冰紅茶。**牆面與手寫菜單失焦**。 |
| **機位與構圖** | **3/4 身到大腿中段，人＋食物同框。**（**2026-08-29 依 R12 由半身放寬**——半身要同時看見低處的凳面側緣、抓凳的手與上方托盤，模型只能裁掉凳手或自行拉遠。保留無背塑膠凳是因為那是這個場景的真實樣貌）<br>**機位**：與她的胸口同高，鏡頭保持水平。<br>**構圖**：騎樓柱在單側最外緣，鐵盤與凳子在中央區。 |
| **光線** | ① 店門口的自然光從側前方**打在臉上**｜② 不鏽鋼餐檯把光反回下巴｜③ 門口冷白 vs 店內日光燈｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（不鏽鋼餐檯回彈補下巴）｜曝光：取捨（門口天光失細節）｜色溫：分裂（門口冷白 vs 店內日光燈） |
| **人物入鏡** | 公共場景——必寫背景路人（早餐店） |
| **多樣性** | 姿勢：**A 動作中**（端著盤子走到座位、正拉開椅子）｜相機：**6 框架物取景**（從騎樓柱旁拍進店裡）｜視線：不看鏡頭｜手在臉旁：否 |
| **不可刪除措辭** | `confined to the far outer edge`（R11 限制框架物寬度）<br>`clearly visible in the central area`（R11 劃定中央安全區）<br>`both hand-object contact points`（R13 景別：down to mid-thigh 屬已證實失效的同類句）<br>`upper chest covered`（R13 領口尺度） |
| **凍結瞬間** | 一手端著裝了蛋餅的鐵盤，另一手正把紅色塑膠椅往外拉開，低頭看著要坐的位置。 |
| **手部任務** | 可見手 A：端著裝了蛋餅的鐵盤<br>可見手 B：抓著紅色塑膠凳的**凳面側緣**往外拉<br>無第三個手部任務<br>（**2026-08-29 由「椅背」改為「凳面側緣」**——台式早餐店的紅色塑膠凳沒有靠背，抓椅背的接觸點不成立。保留無背塑膠凳是因為那是這個場景的真實樣貌） |
| **表情** | 咬一口後眼睛彎成月牙、鼻子微微皺起。**眼型與嘴型列 soft observation。** |
| **肢體與重心** | 手肘靠在桌上；上半身前傾；肩膀微聳。 |
| **硬驗收** | ① 一手端鐵盤、另一手抓凳面側緣往外拉（**身體正在移動中**）② **視線朝下、不看鏡頭** ③ 人與食物同框（蛋餅在盤上）④ **騎樓柱只佔單側最外緣，不與人、盤、凳重疊** ⑤ **上半身與雙腿到大腿中段可見，兩個接觸點、托盤、食物、凳面都在中央區** ⑥ **襯衫有領、上方鈕扣扣上、上胸被覆蓋** |
| **創意備註（不送模型／不驗收）** | 捲起的襯衫袖口與垂下的髮絲隨著前傾晃動——**不送模型、不驗收** |
| **整併紀錄（2026-08-29）** | **2026-08-29 改視線與相機關係**：原本「咬蛋餅＋對鏡頭比大拇指」——比讚是最典型的擺拍手勢，而且手又在臉旁。改成端盤走向座位、正拉開椅子的動作中，並加入框架物（騎樓柱）作為前景遮擋<br><br>—— 以下為先前紀錄 ——<br>**解掉硬衝突**：肢體列寫「雙手捧著蛋餅」、表情列寫「空著的手比大拇指」——雙手捧著就不存在空手。依 R7 二選一，取「一手蛋餅、一手比讚」 |
| **生成 prompt** | `A young woman carries a metal tray with an egg crepe in one hand while her other hand grips the side edge of a red plastic stool and pulls it out, eyes down on the seat. Her upper body and both thighs through mid-thigh are visible, with both hand-object contact points, the tray, food, and stool seat clearly visible in the central area, shot from her side in profile at chest level, a narrow concrete pillar confined to the far outer edge. Collarbone-length soft wavy mocha brown hair, side-parted. A light-blue collared button-front shirt knotted at the waist, its upper buttons fastened and upper chest covered, white high-waisted shorts. A breakfast shop, a steel counter. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.` |
| **Caption 草稿** | 蛋餅真的很好吃🥹<br>這個冰紅茶也太甜 |

### YG-09｜飯店窗邊・皮膚特寫
`圖`　·　對應 **Y-13**　·　地點層級 **A**

| | |
|---|---|
| **妝容** | **素顏，剛洗完澡。**皮膚微微泛紅、有水感，眉毛保留，唇是自然色。 |
| **髮型** | 頭髮往後撥順、露出額頭（**乾髮**）。<br>（**2026-08-29 依 R8b 移除濕髮**——LG-08 的濕髮 4/4 全失敗雖屬另一角色、不能證明本角色必敗，但「已是同一生成流程下足以採取避險措施的負面證據」。<br>**濕髮不是放棄，是改成單獨的單變因 preflight**：同一段 prompt 只比乾髮／濕髮各 2 張，在濕髮能保住髮長、髮色與臉部一致性前不併入正式批次） |
| **穿著** | 上身：白色浴袍，領口鬆開露出鎖骨與肩線｜下身：—｜鞋：—｜外層：—｜首飾：無 |
| **道具** | 浴袍 **core-visible**｜床頭水杯 **removed**（臉部大特寫看不到，留著只會讓人以為 prompt 漏寫） |
| **場景環境** | 飯店房間窗邊。白色床單、落地窗、窗外是城市高樓與河景。床頭放著水杯。 |
| **機位與構圖** | **臉部大特寫。**<br>**機位**：在她的眼睛高度，鏡頭保持水平。<br>**構圖**：臉佔滿畫面，窗外城市只留一小塊虛化。 |
| **光線** | ① 落地窗漫射光**正面均勻打亮臉**｜② 白色床單把光反回下巴｜③ 全場冷白｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（白色床單回彈補下巴）｜曝光：取捨（窗外城市失細節）｜色溫：不適用（單一窗光） |
| **人物入鏡** | 私密場景（飯店房內）——只有本人 |
| **多樣性** | 姿勢：**B 支撐姿勢**（靠窗框）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否（無手） |
| **不可刪除措辭** | `with both arms and hands below the frame`（R8b 正面寫法鎖定裁切，取代否定句）<br>`filling the visible strip of window beside her face`（R13 視線：目標要夠大、必然被畫出來）<br>`closed securely at the collarbone`（R13 領口尺度：大特寫下更容易把胸線帶進下緣） |
| **凍結瞬間** | 臉部大特寫，側身靠著窗框，臉旁保留一條窄幅窗景、裡面有一棟清楚可見的遠方高樓，**她的眼睛對焦在那棟高樓上**，睫毛半垂、嘴唇放鬆——這件刻意不做表情。 |
| **手部任務** | 可見手 A：**N/A**（臉部大特寫，裁切外）<br>可見手 B：**N/A**（裁切外）<br>**本件沒有任何手部任務** |
| **表情** | 眼睛看著窗外遠處、**不看鏡頭**；睫毛半垂；嘴唇自然放鬆。**這件刻意不做表情。** |
| **肢體與重心** | 側身靠著窗框；肩膀一高一低（僅畫面內可見的部分）。 |
| **硬驗收** | ① 臉部大特寫比例，臉佔滿畫面 ② **視線落在填滿臉旁窗景的鄰近建築立面上**（**2026-08-29 依 R13 修正**——「窄幅窗景中的遠塔」同時受大特寫與窄窗限制，模型可能只畫成模糊小形狀甚至省略，不符合「夠大、必然被畫出來」的條件）<br>（**2026-08-29 依 R12 修正**——原本寫「視線在畫面外」是已知失敗型：列出 `city towers` 不等於讓其中一棟成為可對焦目標。不能一邊要求畫面內目標、一邊保留「視線在畫面外」）③ **畫面內沒有任何手** ④ 光線正面均勻、無逆光 ⑤ **浴袍衣襟交疊閉合到鎖骨、不露胸線** |
| **創意備註（不送模型／不驗收）** | 浴袍的腰帶末端垂著微微擺動——**不送模型、不驗收** |
| **整併紀錄（2026-08-29）** | **維持不變**——本件原本就是 13 件裡唯一「不看鏡頭、無手、非正面擺拍」的一件<br><br>—— 以下為先前紀錄 ——<br>肢體列原本指派了三隻手（扶領口／垂著／搭窗框），但這是**臉部大特寫，一隻都看不到**。全部改為 N/A。<br>⚠️ **濕髮風險**：本件髮型列要求「濕髮往後撥、髮尾滴水」，但 LG-08 的濕髮**連續 4/4 失敗已被移除**。本件維持濕髮設定，但**不列入硬驗收**，只記 soft observation |
| **生成 prompt** | `A young woman leans against the window frame, a nearby building facade filling the visible strip of window beside her face, her lowered eyes focused on that broad facade, lips relaxed. Tight close-up of her face, camera at her eye level, shallow depth of field with only her face sharp. The crop contains only her face, hair, neck, and bathrobe collar, with both arms and hands below the frame. Collarbone-length mocha brown hair pushed back off her face. An opaque white bathrobe with overlapping lapels closed securely at the collarbone. A hotel room, white bedding, a floor-to-ceiling window, city towers outside. Soft window light full on her face, the white bedding bouncing fill up under her jaw. Her face is clearly exposed with natural skin texture; the city outside is the brightest area, only its smallest highlights reaching white. Visible skin pores, subtle film grain.` |
| **Caption 草稿** | 皮膚今天狀態超好☺️<br>이거 진짜 좋아 |

### YG-10｜百貨美妝櫃・精緻的一面
`圖`　·　對應 **機動**　·　地點層級 **A**

| | |
|---|---|
| **妝容** | **這批最精緻的一張。**透明感水光底妝拉到最亮；**Y3K 金屬光眼影**——細緻的銀白或丁香紫（2026 的另一條線，跟她的冷白調很合）；眼頭 V 字打亮明確；nose blush ＋ 眼下腮紅；**glazed lavender 淡紫調裸唇**。 |
| **髮型** | **sleek 光澤直順側分**，髮尾微微內彎，mocha brown 的髮色在燈下很明顯。 |
| **穿著** | 上身：奶油色**短版貼身**針織上衣｜下身：**同色系米白高腰西裝直筒褲**（tonal layering，高腰拉腿長）｜鞋：尖頭平底鞋｜外層：卡其色風衣掛在手臂上｜首飾：金色圈形耳環＋細手錶＋小方包 |
| **道具** | 試色的手背 **core-visible**（掛載動作）｜卡其風衣掛在前臂 **core-visible**（前臂承重，**不佔手部任務**）｜金色圈耳環 **core-visible**｜口紅 **removed**｜小方包 **removed**｜細手錶 optional |
| **場景環境** | 百貨公司一樓的美妝樓層。玻璃櫃、排列整齊的口紅與粉盒、**光澤淺色立柱**、天花板的嵌燈、櫃檯的白色檯面。<br>（**2026-08-29 鏡面柱改成非鏡面**——鏡面會複製手與人物，直接威脅「臉旁只有一隻手」的驗收，而鏡面**不是本件硬驗收的一部分**。沿用 YG-04 取消鏡面的同一條判準：不是硬驗收、卻帶來無法用 prompt 控制的 Hard Reject 風險，就拿掉那個效果，不要想辦法馴服它） |
| **機位與構圖** | **半身。**<br>**機位**：與她的胸口同高，鏡頭保持水平。<br>**構圖**：試色的手背舉在畫面中段，身後帶到玻璃櫃與鏡面柱。 |
| **光線** | ① 天花板嵌燈＋櫃檯打光**均勻打亮臉**｜② 白色檯面與鏡面柱把光反回下巴｜③ 冷白為主，玻璃櫃內一點暖黃重點光｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（白檯面與鏡面柱回彈）｜曝光：低反差（百貨均勻嵌燈）｜色溫：分裂（嵌燈冷白 vs 玻璃櫃內暖重點光） |
| **人物入鏡** | 公共場景——必寫背景路人（百貨美妝樓層） |
| **多樣性** | 姿勢：**B 支撐姿勢**（前傾靠櫃檯）｜相機：**4 過肩**｜視線：不看鏡頭｜手在臉旁：否 |
| **不可刪除措辭** | `high crew neckline`（R13 領口尺度橫向規則，2026-08-29 補掃） |
| **凍結瞬間** | 從她身後越過肩膀拍：她低頭把口紅在手背上劃一道，注意力全在手背的顏色上。 |
| **手部任務** | 可見手 A：手背朝上攤平，承接試色<br>可見手 B：拿著口紅，正在手背上劃<br>無第三個手部任務（**這件的兩隻手在腰腹高度、遠離臉部，不會與臉部區域競爭**） |
| **表情** | 抬眼、一邊眉毛挑起、同側嘴角上揚。**眉型與嘴型列 soft observation。** |
| **肢體與重心** | 上半身微側向櫃檯；重心在一腳。 |
| **硬驗收** | ① **過肩視角**：她的肩膀或後腦在前景，櫃檯與手背在畫面中段 ② 一手攤平、一手拿口紅劃在其上 ③ **視線在手背上、不看鏡頭** ④ 半身比例 ⑤ **高圓領、不露胸線**（2026-08-29 補：R13 的領口橫向規則當時只套用在判 REVISE 的件，已放行的沒有回頭重掃） |
| **創意備註（不送模型／不驗收）** | 無 |
| **整併紀錄（2026-08-29）** | **2026-08-29 改相機關係**：原本「手背舉在臉旁＋抬眼看鏡頭」——又是手在臉旁＋看鏡頭。改成過肩視角的專注瞬間。<br>**口紅回到手上**：先前因「與試色手背在同一區、手指融合風險」移除；現在兩手都在腰腹高度、不在臉旁，那個風險大幅降低，而口紅是這個動作成立的必要道具<br><br>—— 以下為先前紀錄 ——<br>刪掉「另一手拿著口紅」——口紅與試色手背在畫面同一區，是手指與小物件融合的高風險組合；且 prompt 原本就沒寫。風衣依 R7「肩／臂承重不算手部任務」保留 |
| **生成 prompt** | `Seen from behind over her shoulder, a young woman leans toward the counter and draws a lipstick stripe across the back of her other hand, her eyes down on the swatch. Half body, camera behind her shoulder at chest level. Sleek glossy collarbone-length mocha brown hair, side-parted, ends curving slightly inward. An opaque cream cropped fitted knit top with a high crew neckline, off-white high-waisted straight trousers, gold hoop earrings. A department store beauty floor, glass counters, rows of lipsticks, glossy pale columns. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool recessed ceiling light on her, warm accent light inside the glass cases, the white counter bouncing fill onto her jaw, the floor behind her slightly darker. Natural skin texture, subtle film grain.` |
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
| **道具** | 草莓蛋糕 **removed**｜拿鐵 **removed**｜珍珠小耳環 **core-visible**（近景看得到）｜窗邊乾燥花 場景物件<br>（**2026-08-29 依 R8b 改為近景優先**——臉佔 45%＋雙肘落桌＋雙手完整托腮之後，下緣空間不足以穩定辨識兩件物品；`at the lower edge` 只指定位置，沒有解決容量衝突。**YG-01 已出過同型失敗，不應只換位置詞重試**。甜點店仍由桌面、磁磚牆與窗邊座位成立） |
| **場景環境** | 明亮的甜點店靠窗座位。白牆或淺色磁磚、淺木桌、桌上一塊草莓蛋糕與一杯拿鐵、窗邊有一小束乾燥花。 |
| **機位與構圖** | **臉部＋肩膀近景。**<br>**機位**：在她的眼睛高度，鏡頭保持水平。<br>**距離**：坐在她對面的距離。<br>**構圖**：臉佔畫面約 45%，桌上的蛋糕入鏡下緣。 |
| **光線** | ① 窗光從她側前方**打在臉上**｜② 淺木桌面把光反回下巴｜③ 窗光冷白 vs 店內暖黃｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（淺木桌面回彈補下巴）｜曝光：取捨（窗外失細節）｜色溫：不適用（單一窗光） |
| **人物入鏡** | 公共場景但景別排除——臉＋肩膀近景，背景只有磁磚牆，路人不可辨識且會與「臉佔 45%」的容量競爭（比照本件已移除蛋糕與拿鐵的同一理由） |
| **多樣性** | 姿勢：**B 支撐姿勢**（手肘撐桌托腮）｜相機：**6 框架物取景**（從店外透過窗玻璃拍）｜視線：**看鏡頭**（2026-08-29 依成品更正，原記不看鏡頭）｜手在臉旁：**是**（配額內 1/3） |
| **不可刪除措辭** | `to one side of the camera`（R11 視線參照系必須是相機）<br>`clear through the glass`（R10 臉與雙手不被玻璃遮住） |
| **凍結瞬間** | 從店外隔著窗玻璃拍：她坐在窗邊，雙手托著兩頰，眼睛看著窗外街上，笑到一半。 |
| **手部任務** | 可見手 A＋B：**共同**托腮（左右各托一頰，兩手一個任務）<br>無第三個手部任務 |
| **表情** | 頭往一側傾約 20 度；眼睛彎起來笑；臉頰被擠得更圓（**擠的動作寫在手部任務列，這裡只寫臉的結果**）。**眼型與嘴型列 soft observation。** |
| **肢體與重心** | 坐姿前傾；手肘撐在桌上；肩膀微聳。 |
| **硬驗收** | ① 雙手托兩頰 ✅ ② ~~視線落在鏡頭一側、不看鏡頭~~ **核准豁免** ③ 單側窗框邊緣構成框架，臉與雙手隔著玻璃清楚可見 ✅ ④ 鮑伯及下巴、剪裁齊平 ✅<br>（**2026-08-29 Penny 核准 `LG01_a`，捨棄 B**。② 視線 2/2 直視鏡頭，屬 D-06 已知的低可靠維度，列為核准豁免。<br>**本件 prompt 自此凍結**——成品是用現行版本產出的，不得事後改寫） |
| **創意備註（不送模型／不驗收）** | 垂在臉側的髮尾隨動作晃動——**不送模型、不驗收** |
| **整併紀錄（2026-08-29）** | **2026-08-29 改相機關係與視線**：托腮保留（列入「手在臉旁」配額 1/3），但改成從店外隔窗拍、她看向窗外。<br>**這同時解掉近景容量問題**——蛋糕與拿鐵不必入鏡，甜點店由窗框與店內環境成立<br><br>—— 以下為先前紀錄 ——<br>刪掉「雙手放在桌上、指尖靠近盤子」（與托腮互斥，同一雙手不能同時在桌上與臉頰上）<br>⚠️ **景別風險**：YG-01 曾因「近景放不下桌上物件」出過事。本件構圖明寫臉佔 45%（不是大特寫），蛋糕在下緣，尚有空間；若生成時被迫拉遠，改為移除桌上物件 |
| **生成 prompt** | `Shot through the window glass, a young woman rests both elbows on the table, cupping both cheeks in her palms, eyes following passing traffic to one side of the camera, half smiling. Close-up of her face and shoulders, camera at her eye level, a dark window frame on one outer side, her face and both hands clear through the glass. A blunt chin-length black bob cut evenly at the jawline. A cream square-neck puff-sleeve top. A dessert shop, a white tiled wall, a pale wood table bouncing fill onto her chin under soft side window light. Her face is clearly exposed with natural skin texture; the window is the brightest area, only its smallest highlights reaching white. Visible skin pores, subtle film grain.` |
| **覆核指紋** | sha1:e4ab38b3321a（已核准成品，prompt 凍結） |
| **Caption 草稿** | —（頭貼用） |

### LG-02｜房間晨光・第一則「她在台北」
`影片 10–15s ＋ start frame`　·　對應 **L-03**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | 幾乎素顏。保留一點粉色唇，其餘乾淨。 |
| **髮型** | 剛睡醒的微亂鮑伯，一側壓扁。 |
| **穿著** | 上身：白色**細肩帶貼身**蕾絲滾邊睡衣上衣｜下身：同色系**短版**睡褲｜鞋：赤腳｜外層：—｜首飾：無 |
| **道具** | 地板光斑 **core-visible**（掛載動作）｜白瓷杯 **removed**｜窗邊小植物與絨毛玩偶 場景物件｜書桌上的相機 場景物件｜未拆完的紙箱 場景物件（剛搬家的痕跡） |
| **場景環境** | **明亮乾淨的小套房**。白牆、淺木地板、白色床組（蕾絲滾邊）、窗邊一盆小植物與一隻絨毛玩偶、書桌上放著相機。角落有一個還沒拆完的紙箱（剛搬家的痕跡）。 |
| **機位與構圖** | **完整蹲姿全身**（**2026-08-29 依 R12 由膝上放寬**——裁切停在膝上時，地板與觸地指尖落在裁切線下方，模型只能犧牲接觸點或自行拉遠。與 LG-05 傘尖、YG-08 凳面是同一型的「景別 vs 接觸點」垂直衝突）。<br>**機位**：與她蹲下時的臉同高，鏡頭保持水平。<br>**距離**：站遠一點拍。<br>**構圖**：地板上的光斑與她的指尖同框。 |
| **光線** | ① 晨光從窗戶進來、地板有光斑，**同時打在臉上**｜② 白牆與淺木地板整體補光｜③ 乾淨明亮的冷白｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（白牆與淺木地板整體回彈）｜曝光：取捨（窗外壓白）｜色溫：不適用 |
| **人物入鏡** | 私密場景（自家房間）——只有本人 |
| **多樣性** | 姿勢：**A 動作中 ＋ D 非站坐體位**（正在蹲下）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：**是**（2026-08-29 更正——揉眼在物理上就是手在臉旁，先前誤記為否，使整批統計失真。**不因此改姿勢**，只把指標如實記錄） |
| **不可刪除措辭** | `her open eye lowered`（R10 沒被揉的那隻眼不可看鏡頭）<br>`the box opening`（R13 視線：光斑是照明效果不是實體）<br>`high-neck sleeveless cotton pyjama top`（R13 領口尺度：camisole 是天然低領高風險款） |
| **凍結瞬間** | 蹲下來，一手的指尖停在地板的光斑上，另一手揉著一隻眼睛，嘴巴打呵欠打到一半。 |
| **手部任務** | 可見手 A：指尖停在地板光斑上<br>可見手 B：揉一隻眼睛<br>無第三個手部任務 |
| **表情** | 打呵欠打到一半；被揉的那隻眼閉著、另一眼半睜；整張臉是鬆的。**眼型與嘴型列 soft observation。** |
| **肢體與重心** | 蹲下，膝蓋併攏；赤腳踩在木地板上；重心壓在腳掌。 |
| **硬驗收** | ① **完整蹲姿、雙膝、雙手都可見** ② 一手指尖在地板光斑上 ③ 另一手揉眼 ④ **沒被揉的那隻眼睛朝下看向紙箱開口**（**2026-08-29 依 R13 改目標**——光斑是照明效果、不是必然獨立成形的實體，模型可能整片照亮而不畫出邊界）⑤ **指尖與光斑的接觸點在畫面內** ⑥ **高領睡衣、不露胸線** |
| **創意備註（不送模型／不驗收）** | 睡衣下襬與髮尾在蹲下的動作裡垂落晃動——**不送模型、不驗收** |
| **整併紀錄（2026-08-29）** | 姿勢原本就合格（蹲＋動作中）。**2026-08-29 只補明視線**：打呵欠揉眼時本來就不會看鏡頭<br><br>—— 以下為先前紀錄 ——<br>**本件原本最亂**：肢體列用「；」串接了三次不同時間的增補，累積出「指尖點光斑／撐地／再一次撐地／矮桌上的白瓷杯」四段互相打架的敘述，與硬驗收（點光斑＋揉眼）完全對不上。依硬驗收保留兩件，其餘刪除 |
| **生成 prompt** | `A young woman crouches, knees together, the fingertips of one hand on a sunlit patch of floor while her other hand rubs one eye, her open eye lowered toward the opening of a large open cardboard box sitting in the sunlit patch, mouth mid-yawn. Her complete crouching pose, both knees, both hands, the fingertip-floor contact, the sunlit patch and the box opening are visible. Shot from her three-quarter front-left and slightly above, looking down at her, shot from well back. A blunt chin-length black bob cut evenly at the jawline, sleep-mussed, one side flattened. An opaque high-neck sleeveless cotton pyjama top with subtle lace trim, and shorts. A bright clean room, white walls, a pale wood floor. Soft morning light on her face, the white walls bouncing fill back. Her face is clearly exposed with natural skin texture; the window is the brightest area, only its smallest highlights reaching white. Subtle film grain.` |
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
| **光學設定** | 反射面：具名（白牆回彈補陰影側）｜曝光：取捨（窗外對街失細節）｜色溫：不適用 |
| **表情** | **臉靠近貓瞇眼笑。**臉貼近貓的頭、眼睛瞇成月牙；嘴角上揚；完全不看鏡頭，注意力全在貓身上。<br>**硬驗收＝一手搔貓頭＋另一手扶窗台。臉部細節（眼型／嘴型／眉毛／臉頰）一律列 soft observation，不作淘汰依據。** |
| **肢體與重心** | 側坐或半跪；一手伸過去摸貓頭、**手指彎曲**；另一手撐在窗台；上半身向貓傾。。<br>（**2026-08-28 刪除「過長的針織袖口垂在手腕外」**——與穿著列「不是袖子過長的 oversized」直接矛盾，且屬抽象飄動，本就不進 prompt） |
| **情境** | 貓趴在窗台，她的手伸過去摸牠的頭，貓瞇著眼 |
| **生成 prompt** | `A young woman leans in close to an orange cat on the windowsill and scratches its head with one hand, her other hand resting on the sill, her eyes crinkled shut in a smile, her attention entirely on the cat. Half body with the cat in frame, camera level with her face as she sits, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, one side tucked behind her ear. Off-white fitted fine-knit top, light shorts. Bedroom windowsill, small potted plants, an iron window grille and the apartment across the street outside. Soft window light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **覆核指紋** | sha1:2d1ef56dec50（已核准成品，prompt 凍結） |
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
| **光學設定** | 反射面：具名（淺色步道地面回彈補下巴）｜曝光：取捨（花季天光失細節）｜色溫：不適用（單一天光） |
| **表情** | **接到花瓣的驚訝。**攤開的掌心裡停著一片花瓣，眼睛睜大、嘴呈小 O 形、眉毛抬高。<br>（掛載動作＝掌心的花瓣；**原本寫「然後笑出來」是兩個時間點，靜態圖只 freeze 驚訝那一刻**）<br>**硬驗收＝拇指食指捏住花瓣在臉頰旁。臉部細節（眼型／嘴型／眉毛／臉頰）一律列 soft observation，不作淘汰依據。** |
| **肢體與重心** | **一手伸起接花瓣、手指張開**；另一手提著開衫；重心在後腳；**裙襬與肩上開衫的下襬被風帶起**。 |
| **情境** | 伸手接住一片落下的花瓣 |
| **生成 prompt** | `A young woman pinches a single pink blossom petal between her thumb and index finger beside her cheek, her free arm relaxed at her side, mouth softly open in surprise, eyebrows raised. Half body, camera level with her chest, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, a cream ribbon headband. An opaque white cotton blouse with a structured square neckline, short puff sleeves and a fitted waist, a pale pink checked pleated A-line mini skirt forming one continuous hem around her thighs, pearl earrings. A park path under blossoming branches, petals on her shoulder. Soft daylight on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **覆核指紋** | sha1:753ea01e6c5c（已核准成品，prompt 凍結） |
| **Caption 草稿** | 花開了🌸<br>今天走了好久才找到這裡 |
| 附註 | **背景路人 1–2 人**：遠處、背向、失焦 |

### LG-05｜公車站・雨停前
`圖　🔬 pilot v2`　·　對應 **L-06**　·　地點層級 **C**

| | |
|---|---|
| **妝容** | 日系可愛妝。明亮輕薄底妝；粉色眼影暈在眼窩與下眼瞼；**下睫毛根根分明**；細內眼線；**曬傷妝腮紅橫過鼻樑與兩頰上方**；粉色漸層水潤唇。 |
| **髮型** | 黑色中分及下巴鮑伯。**髮尾被亭外的風吹得往同一側揚起、有一撮貼在臉頰上**（動勢來源之一）。 |
| **穿著** | 上身：**高領口**米白色收腰短袖襯衫，**扣到鎖骨**（2026-08-29：兩張成品領口都過低、胸線外露，`fastened through the chest` 無效，改用正面指定領口高度）｜**外層：淺藍色薄針織開襟外套，只掛在肩上沒穿進袖子，下襬被風掀起一角**（← **會飄的元素**）｜下身：淺藍色格紋短裙｜鞋：白色瑪莉珍＋蕾絲短襪｜首飾：珍珠小耳環、米色帆布托特包、**透明雨傘收起來拿在手上、傘尖還在滴水** |
| **道具** | 收起的透明雨傘 **core-visible**（掛載動作，傘尖朝下）｜珍珠小耳環 optional｜米色帆布托特包 **removed**｜淺藍薄針織開襟外套 **removed** |
| **場景環境** | **雨天也要好看，不能灰撲撲。**候車亭：**彩色路線圖燈箱**、玻璃側板上的雨珠、金屬亭架；亭外：**對街店家亮著的暖色招牌與透出來的燈光**、紅色郵筒、路邊盆栽、濕亮的柏油路映著這些顏色。**明亮通透的雨天，不是陰鬱的雨天。** |
| **機位與構圖** | **景別到小腿中段**（2026-08-29 由膝上放寬，理由見硬驗收）。<br>**機位**：在她的肚臍高度，鏡頭保持水平。<br>**距離**：站遠一點拍。<br>**構圖**：她站在亭子邊緣，整把收起的傘垂在腿側，亭外的暖色招牌與濕柏油在她身後虛化。 |
| **光線** | ① 雨後亮起來的天光從亭外**打在臉上**｜② **濕柏油與積水**把對街招牌的顏色反上來｜③ 亭外冷白 vs 對街暖色招牌｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（濕柏油把對街招牌的暖色反上來）｜曝光：取捨（招牌高光失細節）｜色溫：分裂（雨後冷天光 vs 對街暖招牌） |
| **人物入鏡** | 公共場景——必寫背景路人（公車站） |
| **多樣性** | 姿勢：**A 動作中**（正要走出亭子、撐開傘）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否 |
| **不可刪除措辭** | `palm turned up to feel for rain`（R10 取代沒有功能的拎裙襬）<br>`the upper chest fully covered by fabric`（R13 領口尺度：fastened through the chest 無效，2/2 胸線外露）<br>`Her calves and the wet pavement are visible in the bottom third`（R13 景別：Framed down to X 無效，改列什麼必須看得見） |
| **凍結瞬間** | 雨還沒完全停，她正要走出候車亭，一手把透明傘撐開舉到頭頂上，另一手伸到亭外、掌心朝上試雨還下不下，**抬眼看著頭頂那面透明傘的內側**。<br>（**2026-08-29 改視線目標**——原本寫「看掌心那幾滴雨」，但雨滴根本沒被畫出來，2/2 退回直視鏡頭。傘面又大又一定在畫面內） |
| **手部任務** | 可見手 A：舉在頭頂、握著撐開的透明傘的傘柄<br>可見手 B：伸到亭外、掌心朝上試雨<br>無第三個手部任務<br>（**2026-08-29 由「拎裙襬」改為「試雨」**——拎一般短裙走進雨裡沒有實際功能，是偶像式擺拍，還會造成裙長漂移。試雨與「雨還沒停」有清楚因果，且不新增物件） |
| **表情** | 頭往比 V 的那一側傾；眼睛彎成月牙——雨天也很開心的那種笑。**眼型與嘴型列 soft observation。** |
| **肢體與重心** | 站著等，重心壓在右腳；左腳膝蓋微彎、腳尖點地，骨盆因此微傾（不是雙腳平均站的死板站姿）；肩膀一高一低。 |
| **硬驗收** | ① **傘是撐開的**，傘柄握在手中、傘面在她頭頂上方 **✅ 2/2 已驗證** ② 另一手伸到亭外、掌心朝上 **✅ 2/2** ③ **視線抬起看向頭頂的傘面內側、不看鏡頭** ④ **小腿與濕地面在畫面下方 1/3 內可見** ⑤ **高圓領扣到鎖骨、上胸完全被不透明布料覆蓋、不露胸線** |
| **創意備註（不送模型／不驗收）** | 髮尾被亭外的風吹得往同一側揚起、有一撮貼在臉頰上；肩上的開襟外套下襬被風掀起一角——**兩者都不送模型、不驗收** |
| **整併紀錄（2026-08-29）** | **2026-08-29 改姿勢**：原本「站著比 V ＋看鏡頭」——比 V 是最典型的擺拍手勢。改成正要走出去撐傘的動作中。<br>**防浮空錨點更強了**：撐開的傘有「手握傘柄」與「傘面在頭頂」兩個接觸關係，比收起的傘垂在腿側更難生錯<br><br>—— 以下為先前紀錄 ——<br>**解掉右手的雙重指派**：肢體列同時寫「右手勾著托特包帶」與表情列的「右手比 V」。依 R7，托特包若不是核心就移除，不要改成掛肩（斜背帶會切過襯衫、破壞服裝辨識）。<br>開襟外套一併移除：只掛肩不穿進袖子的鬆散外層是浮空與變形的高風險件，且 prompt 原本就沒寫 |
| **生成 prompt** | `A young woman steps out from the bus shelter, one hand raised holding the handle of a clear umbrella opened above her head, her other hand reaching out with the palm turned up to feel for rain, her eyes lifted to the underside of the clear canopy above her. Her calves and the wet pavement are visible in the bottom third of the frame. Shot from her side in profile as she steps out, camera at her navel level, shot from well back. A blunt chin-length black bob with even blunt ends along the jawline. An opaque off-white button-front blouse with a high round neckline at the collarbone, all upper buttons fastened, the upper chest fully covered by fabric, a pale blue checked skirt. A route map lightbox. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool overcast daylight falls on her face, while wet asphalt bounces a small amount of warm sign colour upward. Her face clearly exposed with natural skin texture; the signs are the brightest area, only their smallest highlights reaching white. Subtle film grain.` |
| **Caption 草稿** | 台北下雨了☔️<br>雨の台北、こういう日が好き |
| 附註 | 🔬 **preflight**：這件是**鮑伯剪裁幾何的受測件**——頭髮自然垂放、沒有塞耳後／濕髮／半盤，是唯一能乾淨測出底層剪裁的一件。用 `with even blunt ends along the jawline`；**其餘 10 件暫時維持 `cut evenly at the jawline`，等這張驗過再決定要不要全面沿用** |

### LG-06｜可愛系街區・扭蛋機前
`影片 10–15s ＋ start frame`　·　對應 **L-07**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | 標準可愛妝。 |
| **髮型** | 鮑伯，用兩個小髮夾把兩側瀏海別起。 |
| **穿著** | 上身：淺粉色**短版**針織上衣（露一截腰）｜下身：白色**高腰**短褲｜鞋：白色球鞋＋短襪｜外層：牛仔外套繫在腰上｜首飾：珍珠小耳環＋米色小圓包 |
| **道具** | 打開的扭蛋殼 **core-visible**（掛載動作）｜牛仔外套繫在腰上 **core-visible**｜珍珠小耳環 optional｜米色小圓包 **removed**｜整排扭蛋機 場景物件 |
| **場景環境** | 可愛系街區的扭蛋店門口。一整排彩色扭蛋機、櫥窗、彩色招牌、乾淨的人行道。 |
| **機位與構圖** | **半身。**<br>**機位**：與她的胸口同高，鏡頭保持水平。<br>**構圖**：手上的扭蛋在畫面中段，整排扭蛋機在她身後。 |
| **光線** | ① 街上的柔和天光**均勻打在臉上**｜② 扭蛋機的彩色面板反一點顏色在她身上｜③ 天光冷白 vs 店招暖黃｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（扭蛋機彩色面板回一點顏色）｜曝光：低反差（街上柔和天光）｜色溫：不適用 |
| **人物入鏡** | 公共場景——必寫背景路人（扭蛋店門口人行道） |
| **多樣性** | 姿勢：**C 靜止站定**｜相機：**1 自拍**｜視線：看鏡頭（手機）｜手在臉旁：否 |
| **不可刪除措辭** | `The frame contains exactly one visible hand; her phone and her camera-holding hand stay outside the frame.`（R8a 封住自拍手與手機入鏡） |
| **凍結瞬間** | 轉到扭蛋之後在扭蛋機前自拍一張，一手把打開的扭蛋殼舉到胸前給鏡頭看，笑到眼睛瞇起來。 |
| **手部任務** | 拍攝手／鏡外手：持手機自拍，**off-frame**（仍佔一隻解剖學的手）<br>可見手 A：舉著打開的扭蛋殼在胸前<br>可見手 B：**N/A**——兩隻手已用完 |
| **表情** | 頭朝著扭蛋低下去，笑到眼睛瞇起來。<br>**寫「頭的朝向」不寫「眼睛在看」**——閉著眼就不可能同時在看鏡頭，那是語意矛盾。 |
| **肢體與重心** | 半彎腰在扭蛋機前；重心在一腳。 |
| **硬驗收** | ① 自拍構圖成立且**手機不入鏡** ② **只有一隻可見手**，舉著扭蛋殼在胸前 ③ 整排扭蛋機在她身後 ④ 半身比例 |
| **創意備註（不送模型／不驗收）** | 髮尾甩動——**不送模型、不驗收** |
| **整併紀錄（2026-08-29）** | **2026-08-29 改相機關係**：原本「雙手捧扭蛋低頭閉眼」與 YG-06、LG-09 三件同構圖。改成自拍（轉到扭蛋後自拍是這個場景最自然的行為），並補足自拍配額<br><br>—— 以下為先前紀錄 ——<br>**解掉語意矛盾**：肢體列寫「轉頭看鏡頭時髮尾甩動」，與表情列的「頭朝扭蛋、閉眼」直接衝突——而這正是本件當初特地註記過要避免的那種矛盾。<br>另刪「手指轉動蛋殼」（雙手已捧著蛋殼，這是同一雙手的第二個任務）。<br>**情境列原本是四拍**（轉扭蛋→蛋掉下→打開→失望→又笑了），違反 D-11，已凍結為單一瞬間 |
| **生成 prompt** | `In a phone selfie, a young woman holds an opened gachapon capsule up at chest level, laughing with her eyes crinkled. The frame contains exactly one visible hand; her phone and her camera-holding hand stay outside the frame. Half body, camera just above her eye level. A blunt chin-length black bob cut evenly at the jawline, two small clips holding her fringe back. A pale pink cropped knit top, white high-waisted shorts, a denim jacket at her waist. A row of colourful gachapon machines behind her, signage well out of focus. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Soft daylight on her face, evenly exposed, the coloured panels throwing colour onto her arms, the machines behind her staying slightly darker. Natural skin texture, subtle film grain.` |
| **覆核指紋** | sha1:9af94aad30c8（R12 逐件 PASS） |
| **Caption 草稿** | 這個扭蛋轉了五次才轉到😭<br>但很可愛所以沒關係 |
| 附註 | **背景路人 1–2 人**：背向、失焦 |

### LG-07｜遊樂園・旋轉木馬
`圖`　·　對應 **L-08**　·　地點層級 **A**

| | |
|---|---|
| **妝容** | 標準可愛妝，唇色稍亮一階。 |
| **髮型** | 鮑伯，戴一個**貓耳造型髮箍**。（**2026-08-28 定案**——原本寫「貓耳或蝴蝶結」，規格不該留二選一；prompt 早已自行定為 cat-ear，以 prompt 為準） |
| **穿著** | 上身：白色**方領**泡泡袖上衣（收腰）｜下身：淺藍色**吊帶短裙**｜鞋：白色瑪莉珍鞋＋蕾絲短襪｜外層：—｜首飾：造型髮箍＋小後背包 |
| **道具** | 爆米花桶 **core-visible**（掛載動作）｜貓耳造型髮箍 **core-visible**｜白色瑪莉珍鞋＋蕾絲短襪 **core-visible**（全身景別）｜小後背包 optional（背部承重，不佔手）｜彩色氣球與旋轉木馬 場景物件 |
| **場景環境** | 遊樂園。旋轉木馬、彩色氣球、爆米花桶、遠處的遊行街道與裝飾。 |
| **機位與構圖** | **全身。**<br>**機位**：在她的肚臍高度，鏡頭保持水平。<br>**距離**：站遠一點拍，全身不要靠近拍。<br>**構圖**：腳貼近畫面下方 1/3，旋轉木馬在她身後。 |
| **光線** | ① 遊樂園的柔和天光**均勻打在臉上**｜② 淺色地面把光反回下巴｜③ 天光為主，旋轉木馬燈泡的暖黃在背景｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（淺色地面回彈補下巴）｜曝光：低反差（遊樂園柔和天光）｜色溫：分裂（天光冷白 vs 旋轉木馬燈泡暖黃） |
| **人物入鏡** | 公共場景——必寫背景路人（遊樂園） |
| **多樣性** | 姿勢：**A 動作中**（走向旋轉木馬）｜相機：**4 背後跟拍**｜視線：回頭一瞥｜手在臉旁：否 |
| **不可刪除措辭** | `wrapped around its upper side`（R10 紙桶無提把，改環握）<br>`glowing ahead in the background`（R10 解掉木馬在前、燈泡在後的空間矛盾） |
| **凍結瞬間** | 從她身後跟著拍：她往旋轉木馬走過去，一手環握著爆米花桶的上半部、桶靠在髖側，走到一半回頭看了鏡頭一眼。 |
| **手部任務** | 可見手 A：環握爆米花桶的上半部，桶靠在髖側<br>可見手 B：隨步伐自然擺動<br>無第三個手部任務<br>（**2026-08-29 改持法**——紙製爆米花桶沒有提把，裝著爆米花時單手拎上緣走動既不穩也像為 prompt 安排的動作，且容易生出變形桶口） |
| **表情** | 越過桶緣看鏡頭，帶著玩心的笑意。**眼型與嘴型列 soft observation。** |
| **肢體與重心** | **溫和的四分之三背側站姿**：骨盆斜向離開鏡頭，肩線轉向鏡頭；重心在一腳、另一腳腳尖點地。<br>（**2026-08-29 依 R8b 降低扭轉幅度**——原本的大幅轉體要求軀幹極限扭轉，模型容易用腰部變形、肩臂錯位或多手來完成；且 `turned three-quarters back` 可能被理解成上身仍背對鏡頭） |
| **硬驗收** | ① **背後跟拍視角**：她的背與後腦在畫面中，正在往前走 ✅ ② 一手環握爆米花桶、桶靠在髖側 ✅ ③ 回頭看鏡頭 ✅ ④ ~~全身比例~~ **核准豁免**<br>（**2026-08-29 Penny 核准 `LG07_v2_b`，不重跑本場景**。④ 小腿以下被裁未達成，屬非核心，列為核准豁免。<br>⚠️ **本件 prompt 自此凍結**——依 R7 Q1「核准後以成品控制交付紀錄」，先前為修正腳部而還原的 `her complete feet visible within the bottom third of the frame` **已撤回**，因為成品是用沒有該句的版本產出的，留著會讓文件聲稱一段從未產出該圖的 prompt 是來源） |
| **創意備註（不送模型／不驗收）** | 無 |
| **整併紀錄（2026-08-29）** | **2026-08-29 全面改寫**——上一輪 2 張硬驗收三項同方向失敗（轉體沒發生、桶在胸前不在下巴下、腳被裁）。<br>放棄「大幅轉體＋桶抵下巴＋全身收腳」這組互相拉扯的要求。<br>改用**已驗證成功的寫法**：LG-10A 的「走開→回頭」在校準測試 D 組是成功的，而且它天然就是背後跟拍視角<br><br>—— 以下為先前紀錄 ——<br>髮箍由「貓耳**或**蝴蝶結」定案為貓耳（規格不該留二選一）。小後背包依 R7「背部承重不算手部任務」保留為 optional，不進 prompt<br>⚠️ **難度偏高**：全身＋回身＋桶子抵下巴三件事疊在一起，是 13 件裡構圖最複雜的。建議排在後段跑 |
| **生成 prompt** | `Following her from behind, a young woman walks toward the carousel carrying the popcorn bucket against her hip with one hand wrapped around its upper side, her other arm swinging with her stride, and glances back over her shoulder at the camera. Full body, camera at her navel level, shot from well back. A blunt chin-length black bob cut evenly at the jawline, a cat-ear headband. A white square-neck puff-sleeve top, a pale blue pinafore skirt. A carousel and coloured balloons ahead of her. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight on her, warm carousel bulbs glowing ahead in the background, the pale ground bouncing fill onto her chin. Natural skin texture, subtle film grain.` |
| **覆核指紋** | sha1:e0c54fec90bb（已核准成品，prompt 凍結） |
| **Caption 草稿** | 今天玩得好開心✨<br>爆米花吃了兩桶 |
| 附註 | **背景路人 2–3 人**：背向、失焦、外型與她區隔 |

### LG-08｜浴室鏡前・洗完臉
`圖`　·　對應 **L-09**　·　地點層級 **B**

| | |
|---|---|
| **妝容** | **素顏，剛洗完臉**。皮膚微微泛紅有水感，保留一點唇色。 |
| **髮型** | 及下巴鮑伯，一側撥到耳後。<br>（**2026-08-28：濕髮 4/4 全部生成失敗，已拿掉這個要求**——依分流規則，同方向連續失敗就停，不再抽卡） |
| **穿著** | 上身：白色浴巾裹身（胸線與腰身自然呈現）｜下身：—｜鞋：赤腳｜外層：—｜首飾：無 |
| **場景環境** | **乾淨明亮的浴室**。白色方形磁磚牆（看得到磁磚縫的質感）、木框鏡、鏡角有一點霧氣、掛著的白毛巾、洗手台上的護膚品。 |
| **機位與構圖** | **半身，拍鏡中反射。**<br>**機位**：在她的眼睛高度，鏡頭保持水平。<br>**構圖**：木框鏡邊入鏡，洗手台上的瓶罐在下緣。 |
| **光線** | ① 浴室頂燈＋鏡側光**均勻打在臉上，幾乎沒有陰影**｜② 白色磁磚牆整體補光｜③ 全場冷白｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（白色磁磚牆整體回彈）｜曝光：低反差（浴室平光）｜色溫：不適用（單一頂燈） |
| **表情** | **把小毛巾按在臉頰上、閉眼笑。**單手拿一條**小方巾**按在一邊臉頰；另一手平放檯面；肩膀微抬、身體前傾。<br>**硬驗收＝單手按毛巾＋另一手扶檯面＋前傾抬肩。閉眼與笑容只記 soft observation。**<br>（**2026-08-28 移除「濕髮可見」**——髮型列已於同日刪掉濕髮要求，硬驗收卻還留著，是同一件內的自我矛盾。本件成品即是無濕髮版且已核准，依覆核 Q1「核准後以成品控制交付紀錄」處理）<br>（**原本的「咬毛巾＋鼓臉頰」兩張全失敗，已刪**；雙手同時靠近臉會增加手指重疊與融合風險，所以維持已驗證的一手一事分工） |
| **肢體與重心** | 一手拿毛巾擦頭髮、**手肘抬起**；另一手扶著洗手台；上半身微前傾；肩膀一高一低。 |
| **情境** | 洗完臉，把小方巾按在臉頰上，閉著眼笑 |
| **生成 prompt** | `A young woman leans toward the bathroom mirror, pressing a small folded white hand towel against one cheek with one hand, her other hand resting flat on the counter, shoulders lifted, eyes gently closed in a smile. Half body reflected in the mirror, camera at her eye level. A blunt chin-length black bob cut evenly at the jawline, one side tucked back behind her ear. A large white bath towel wrapped around her torso. Clean bright bathroom, white square tiles, a wooden-framed mirror with steam at one corner. Broad diffuse frontal light with very low shadow contrast, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.` |
| **覆核指紋** | sha1:fe6d4ffe115e（已核准成品，prompt 凍結） |
| **Caption 草稿** | 洗完臉的這一秒最舒服🫧 |

### LG-09｜台式早餐店・豆漿
`圖`　·　對應 **L-13**　·　地點層級 **C**

| | |
|---|---|
| **妝容** | 淡妝。輕底妝、粉色眼影、曬傷妝腮紅、粉色唇。 |
| **髮型** | 中分鮑伯自然放下（與其他件的別耳後、髮夾、髮箍明確區隔）。 |
| **穿著** | 上身：奶油色**合身**薄針織短袖（腰線清楚）｜下身：淺色短裙（**畫面外**）｜鞋：畫面外｜外層：—｜首飾：帆布托特包（已 removed）<br>（**2026-08-29 依 R8b 把裙子移出 prompt**——半身寫 `mini skirt with one continuous hem` 等於要求模型展示裁切外的裙襬，容易把半身拉成膝上景；裙裝也不在本件硬驗收內。<br>⚠️ `one continuous hem` 是驗證過 4/4 的**防短褲錨點**，只在裙子真的入鏡的件才寫） |
| **道具** | **一次性透明塑膠杯裝的豆漿、杯口有封膜** **core-visible**（掛載動作）｜鐵盤與紅色塑膠椅 場景物件｜帆布托特包 **removed**<br>（**2026-08-29 由玻璃杯改為塑膠杯**——早餐店的熱封膜封在一次性塑膠杯上，玻璃杯配封膜物理不成立，會讓畫面看起來像生成錯誤） |
| **場景環境** | 早餐店。不鏽鋼餐檯、鐵盤、玻璃杯裝的豆漿、紅色塑膠椅。**牆上手寫菜單失焦**（見場景國別驗收規則）。 |
| **機位與構圖** | **半身，人＋食物同框。**<br>**機位**：**在她的眼睛高度或略高**，鏡頭保持水平。<br>**構圖**：豆漿杯捧在下巴前，牆上手寫菜單在她身後。<br>（上目遣い是這件的核心驗收點，機位放在眼睛高度模型比較直接做得到） |
| **光線** | ① 店門口自然光從側前方**打在臉上**｜② 不鏽鋼餐檯反光補下巴｜③ 門口冷白 vs 店內日光燈｜④ **背景曝光與她的膚色相當** |
| **光學設定** | 反射面：具名（不鏽鋼餐檯回彈補下巴）｜曝光：取捨（門口天光失細節）｜色溫：分裂（門口冷白 vs 店內日光燈） |
| **人物入鏡** | 公共場景——必寫背景路人（早餐店） |
| **多樣性** | 姿勢：**B 支撐姿勢**（手肘靠桌前傾）｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否 |
| **不可刪除措辭** | `clear disposable plastic cup`（R10 玻璃杯配熱封膜物理不成立）<br>`sealed film lid`（R10 封膜是插吸管動作的接觸對象）<br>`crew-neck`（R13 領口尺度：thin-knit top 未定義領型） |
| **凍結瞬間** | 低頭把吸管插進豆漿杯的封膜，一手扶杯、一手捏吸管往下插，注意力全在那個動作上。 |
| **手部任務** | 可見手 A：扶住**透明塑膠豆漿杯**<br>可見手 B：捏著吸管往下插<br>無第三個手部任務<br>（**2026-08-29 依 R12 統一容器名稱**——本列殘留「玻璃杯」，與 prompt 及硬驗收的塑膠杯不一致。**前臂支撐不算第三個手部任務**：前臂是支撐，不是抓握） |
| **表情** | 上目遣い——頭略低、眼睛往上看鏡頭；嘴角微揚。**眼型與嘴型列 soft observation。** |
| **肢體與重心** | 手肘靠在桌上；上半身前傾；肩膀微聳。 |
| **硬驗收** | ① 一手扶**塑膠豆漿杯**、一手捏吸管往下插 ② **視線在杯子上、不看鏡頭** ③ 人與豆漿杯同框 ④ 半身比例 ⑤ **高圓領上衣、不露胸線** |
| **創意備註（不送模型／不驗收）** | 薄針織的袖口與髮尾隨著前傾垂下晃動——**不送模型、不驗收** |
| **整併紀錄（2026-08-29）** | **2026-08-29 改姿勢與視線**：原本「雙手捧杯在下巴前＋上目遣い」與 YG-06、LG-06 三件同構圖，且手在臉旁。改成插吸管的動作瞬間<br><br>—— 以下為先前紀錄 ——<br>**統一杯子位置**：表情列寫「下巴前」、肢體列寫「胸前」，差一個頭的高度。上目遣い是本件核心驗收點，胸前會讓視線關係不成立，**取下巴前** |
| **生成 prompt** | `A young woman leans forward over the counter with both forearms supported near its edge, holding a clear disposable plastic cup of soy milk steady with one hand while her other hand pushes a straw down through its sealed film lid, her eyes down on the cup. Half body with the cup in frame, shot from her three-quarter front-right at her eye level, on a short telephoto with the shop behind her compressed and softly out of focus. A blunt chin-length black bob cut evenly at the jawline, centre-parted. An opaque cream fitted crew-neck knit top with a clear waistline. A breakfast shop, a steel counter, the wall menu out of focus. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.` |
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
| **光學設定** | 反射面：具名（參道石板地面把燈籠暖光反回下巴）｜曝光：取捨（燈籠高光失細節）｜色溫：分裂（燈籠暖橘 vs 天空殘藍） |
| **表情** | **走著被叫住、回頭笑。**寫成**動作中的瞬間**（走開→回頭），不是靜態的身體擺放；一手舉蘋果糖在臉頰旁，另一手自然垂放。<br>（掛載動作＝蘋果糖；**2026-08-28 改用 A/B 的 A 版**——理由是 A 在 4 張裡沒有 hard defect，屬較低風險，**不是已證實動作寫法較優**） |
| **肢體與重心** | 重心在後腳；骨盆朝參道深處；上半身與頭轉回鏡頭；一手舉蘋果糖。 |
| **情境** | 走在參道上回頭 |
| **生成 prompt** | `Walking away down the festival approach, a young woman glances back over her shoulder mid-stride, holding a candy apple beside her cheek with one hand, her free arm relaxed at her side, laughing. Full body, camera at her navel level, shot from well back. A blunt chin-length black bob cut evenly at the jawline, half-pinned up with a Japanese hairpin. A pale-blue floral Japanese yukata, an ankle-length wrap robe with the left panel crossed over the right, a wide flat navy obi sash, wooden geta. A wooden torii, paper lanterns overhead, food stalls. Her face clearly lit, the lantern-lit stalls keeping visible detail. Natural skin texture, subtle film grain.` |
| **覆核指紋** | sha1:d01e08642e91（已核准成品，prompt 凍結） |
| **Caption 草稿** | 夏祭り🎐<br>蘋果糖比想像中大顆 |
| 附註 | 這是 Luna 視覺變化最大的一組。<br>**⚠️ 這件的場景在日本，是刻意的**——歸為「回日本的時候」類型（對應 Yuna 的 YG-06 汗蒸幕）。**其餘 Luna 的件全部是台北。**<br>戶外件，第一張出來要跟 LG-04／06／07 互相比對有沒有出現同一個場景模板 |

### LG-10B｜浴衣・蘋果糖（半身）
`圖`　·　對應 **L-21**　·　地點層級 **A**

| | |
|---|---|
| **妝容** | 標準可愛妝，唇色帶一點紅，祭典燈光下顯色。 |
| **髮型** | 鮑伯盤起一半，插一支和風髮簪，鬢角留兩撮。 |
| **穿著** | 上身＋下身：**淺藍底白色朝顏花紋浴衣**，深藍色半幅帶**綁緊收腰**、衣襟自然貼合（浴衣是靠腰帶與衣襟呈現線條的）｜鞋：木屐＋白足袋｜首飾：和風髮簪＋巾着小提包 |
| **道具** | 蘋果糖 **core-visible**（掛載動作）｜和風髮簪 **core-visible**｜巾着小提包 **removed**｜紙燈籠與攤位 場景物件 |
| **場景環境** | 夏日祭典的神社參道。**乾淨明亮的木造鳥居**（不是斑駁老舊）、兩側掛著的紙燈籠、祭典攤位（金魚撈、蘋果糖、章魚燒）、遠處的人群。 |
| **機位與構圖** | **半身。**<br>**機位**：與她的胸口同高，鏡頭保持水平。<br>**構圖**：蘋果糖在臉頰旁，紙燈籠在她身後虛化。 |
| **光線** | ① 紙燈籠的暖光**打在臉上**｜② 參道地面反光補下巴｜③ 全場暖色｜④ **臉清楚受光、背景燈籠保留細節** |
| **光學設定** | 反射面：具名（參道地面回彈暖光）｜曝光：取捨（燈籠高光失細節）｜色溫：分裂（燈籠暖橘 vs 天空殘藍） |
| **人物入鏡** | 公共場景——必寫背景路人（祭典參道，規格表原本就寫了「遠處的人群」） |
| **多樣性** | 姿勢：**C 靜止站定**｜相機：**6 框架物取景**（透過攤位布簾之間）｜視線：看鏡頭｜手在臉旁：**是**（配額內 2/3） |
| **不可刪除措辭** | `with her face, candy apple, hands, and obi clearly visible in the centre`（R11 刪掉 hands 後布簾可遮住握糖接觸點）<br>`eyes toward the camera`（R10 metadata 說看鏡頭，prompt 必須明寫） |
| **凍結瞬間** | 透過祭典攤位垂下的布簾之間拍過去：她站在攤子前，一手把蘋果糖舉在臉頰旁，笑到眼睛彎起來。 |
| **手部任務** | 可見手 A：把蘋果糖舉在臉頰旁<br>可見手 B：輕放在腰帶正面<br>無第三個手部任務<br>（**2026-08-29 依 R12 改放腰帶正面**——半身裁切下垂在身側的手通常落在腰線以下被裁掉，但硬驗收②與不可刪除措辭都要求 `hands` 複數在中央區清楚可見。**這個內部衝突是組裝成完整 prompt 之後才看得出來的**） |
| **表情** | 笑到眼睛彎起來。**眼型與嘴型列 soft observation。** |
| **肢體與重心** | 站定，重心在一腳。 |
| **硬驗收** | ① 一手舉蘋果糖在臉頰旁、**眼睛看鏡頭** ② **素面布簾只在左右最外緣形成窄條**，臉、蘋果糖、雙手與腰帶都在清楚的中央區<br>（**2026-08-29 改為素面窄條**——有圖案的布簾容易生出可讀或亂碼文字，未限寬的前景可能遮住蘋果糖或腰帶）③ 浴衣**左襟在上**、半幅帶綁緊收腰 ④ 半身比例 |
| **創意備註（不送模型／不驗收）** | 無 |
| **整併紀錄（2026-08-29）** | **2026-08-29 改相機關係，並拿掉扶髮簪**：兩手都在頭部附近是手指融合的風險組合（上一輪已標註）。<br>改成單手舉糖、另一手垂放，並用布簾當框架物製造天然遮擋與縱深<br><br>—— 以下為先前紀錄 ——<br>巾着包移除（半身景別、且會在手腕再多一個物件）。<br>⚠️ **兩手都在頭部附近**（臉頰旁＋髮簪）是手指融合的風險組合，但兩者都是核心創意，保留並列入硬驗收逐項檢查 |
| **生成 prompt** | `A young woman holds a candy apple beside her cheek, her other hand resting lightly on the front of her obi, laughing, eyes toward the camera. Half body, camera level with her chest, shot on a short telephoto with the stalls behind her compressed, plain hanging cloth curtains forming narrow blurred strips at the far left and right edges, with her face, candy apple, hands, and obi clearly visible in the centre. A blunt chin-length black bob cut evenly at the jawline, half-pinned with a hairpin. A pale-blue floral yukata, the wearer's left panel over the right, a flat navy obi. Paper lanterns overhead. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm lantern light on her face, the approach underfoot bouncing warm fill up. Her face is clearly exposed with natural skin texture; the lanterns are the brightest area, only their smallest highlights reaching white. Subtle film grain.` |
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
