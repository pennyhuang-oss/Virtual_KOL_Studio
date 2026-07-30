# Virtual KOL Studio — Sexy Scene Library

> 親密生活風格場景庫。所有場景以 SFW 為前提，強調身體存在感、自然親密感與寄生社交效果。
> 生成前請依各角色的 `character.md` 調整 outfit 細節、光線偏好與鏡頭公式。

---

## 使用原則

- **視角是輸出照片的視角，不是拍攝動作**：不要描述「她拿著手機自拍」，而是描述「close-up front-facing selfie shot, slightly overhead angle looking down at camera」
- **真實感優先**：加入 `candid moment`、`slightly off-center composition`、`film grain`，避免完美置中構圖
- **光線是主角**：每個場景的光線描述比服裝描述更重要，光線決定氛圍
- **Prompt 結尾標配**：所有場景在 prompt 末尾加入 `film grain, candid lifestyle photo, shot on 35mm, warm tones, slightly off-center composition`

---

## 降低「AI 感」的技術要點（2026-07-24 新增）

> 真正決定生成結果精準度與真實感的是這些技術參數寫得夠不夠具體——不是靠對標哪個真人帳號。以下五項是常見反饋「還是看得出 AI 感」的主因，每個場景 prompt 都應該檢查是否涵蓋。

### 1. 皮膚質感
多數生成模型預設會往「打磨過、無瑕疵」的方向走。**每個 prompt 都要主動加入**：
```
visible skin pores, subtle natural skin texture, slight oil sheen on T-zone,
unretouched skin detail, natural skin imperfections
```
**避免使用**會把畫面推向塑膠感的字：`smooth`、`flawless`、`glossy skin`、`airbrushed`、`porcelain skin`。

### 2. 拍攝裝置感
只寫 `shot on iPhone` 不夠，需要具體到裝置的實際破綻：
```
shot on iPhone 15 Pro front camera, slight autofocus softness on background elements,
natural highlight clipping near window light, subtle motion blur on hair/hands,
faint JPEG compression at high-contrast edges
```
拍攝裝置與鏡頭必須逐場景明確指定（前鏡頭自拍 vs. 後鏡頭 vs. 單眼淺景深），不要讓模型自己猜。

### 3. 光源
> **⚠️ 2026-07-25 修正**：這條原本寫「真實光線是混亂、不均勻的」，結果實際套用在 Vicky Lin 身上時被使用者反饋「濾鏡、光線、畫質都非常差」。問題是把「真實感」跟「拍得普通/畫質差」劃上等號了——這是錯的，兩者是獨立的兩件事。真人使用者提供的實際健身網紅參考截圖顯示：真實感來自皮膚質感和生活細節，**不是**靠調暗、調糊、做舊光線。現代手機攝影的「討喜」光線（黃金時段斜陽、戶外強光、樹蔭斑駁光）配合淺景深背景虛化，一樣可以清晰漂亮又有真實感。

**室內親密場景**（晨起/浴室/居家等）維持原本的「混合、不均勻」邏輯：
```
mixed color temperature — cool daylight from window blending with warm indoor lamp,
uneven light falloff across the frame, soft but visible shadow edges,
slight lens flare or glare on skin/glass surfaces
```

**戶外/生活風格場景**（健身、旅遊、日常外出等）改用「討喜自然光」邏輯，不要刻意做舊：
```
golden hour sunlight or bright clear daylight, natural directional light with soft flattering falloff,
shallow depth of field with blurred bokeh background, crisp sharp focus on subject,
high dynamic range, natural color grading — NOT degraded, dim, or muddy
```
兩種邏輯都要保留皮膚質感關鍵字（見第 1 點）和裝置破綻（見第 2 點），差別只在「整體畫面美不美、亮不亮」，不是在「像不像真的」。

### 4. 背景場景具體度
避免「乾淨、對稱、沒有雜物」的背景，主動寫入生活感細節（皺褶床單、地上的充電線、喝到一半的水瓶、隨手放的手機），而不是只寫地點名稱。

### 5. 聲音與環境音（影片專用）
乾淨的 BGM-only 音軌會讀起來像「後製過」。需要在環境音層加入：
```
room tone / air conditioning hum, fabric rustle, soft footsteps, faint distant background noise
```
疊在 BGM 底下（`generate_audio` 設定與音樂上傳流程見 `DAILY_VIDEO_SOP.md` / `DANCE_VIDEO_SOP.md`）。

### 6. 膚色基調（臺灣籍角色專用，2026-07-25 新增）
> **背景**：Coco Wu、Rainie Hsu、Sophia Tseng、Mia Huang、Zoe Lai 的第一輪探索批次生成後，使用者明確反饋膚色整體偏「健康小麥/古銅曬黑」，並指出臺灣觀眾對「漂亮性感」的審美偏好是**白幼瘦**——白皙皮膚、精緻年輕的五官、纖細身形，「健康古銅膚色」通常不是主流受眾偏好的類型。

臺灣籍角色（不論人設是居家、辦公室、健身、還是海邊/衝浪這類戶外活躍角色）的膚色基調都要維持**白皙透亮**，最多只能有極淡的自然日曬痕跡，**不可**整體呈現古銅色、小麥色、深咖啡色調。每個臺灣籍角色的核心 prompt 都必須明確寫入：
```
fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored)
```
同時保留第 1 點的毛孔/自然質感關鍵字——**白皙不等於無瑕疵磨皮**，兩者要同時成立。此規則對已核准的既有生成圖片（例如 Vicky Lin 已核准的 v4_anchored 訓練集）不追溯套用，只適用於尚未核准／尚未生成的新批次。

### 7. 自拍與他拍比例（2026-07-30 新增）
> **背景**：使用者反饋 Rainie Hsu 第二輪候選圖「風格都很像棚拍，很不自然、蠻刻意的」，並指出所有角色的素材不能只侷限在「像第三者幫她拍」的一種視角——女生本來就常常自拍，早期驗證成功的 Iris Chen 範本（`kols/iris-chen/generation_notes.md`）本來就包含 `close-up front-facing selfie shot, slightly overhead angle looking down at camera` 這類自拍視角批次，不是每張都是「編輯/攝影棚」語氣的第三人稱攝影。

每個角色的**完整素材組合（不只是單一場景/單一批次）**都必須混合以下至少兩種視角，不能全數採用同一種：
- **自拍視角**：`close-up front-facing selfie shot`、鏡子前自拍（`mirror selfie, phone visible in reflection`）、手臂伸展自拍角度——描述的是「照片本身呈現的視角」，不是「她正在自拍的動作」（見 Iris Chen 案例「自拍視角重要規則」：❌ `taking a selfie holding phone up` 會讓模型生成第三人視角+手機入鏡；✅ 直接寫出照片視角本身）
- **他拍/生活抓拍視角**：朋友幫忙拍、隨手抓拍、路人視角等，重點是自然不做作
- 避免整批次全部使用「editorial photography」「high-production-value」「dramatic and moody」這類會把畫面推向棚拍/雜誌大片感的語氣——這類語氣本身沒有錯（有些場景就是需要，例如換裝定裝照），但**不能是唯一的視角**，否則會讀起來刻意、失去「真實生活分享」的親近感

### 生成前檢查清單
每個 prompt 送出生成前，逐項確認：
- [ ] **（2026-07-25 新增，第一優先）是否已經先讀過既有已驗證成功的角色範本，而不是直接採用生成工具本身的預設建議？** 預設參考 `kols/iris-chen/generation_notes.md`（模型 `seedream_v4_5`，已證實同 prompt 重複生成身分一致性高）。訓練圖／Discovery 批次的預設模型是 `seedream_v4_5`，不是 `soul_2`——`soul_2` 只在角色已經有 `soul_id` 時才用於後續生成。2026-07-25 事故：多個角色的 Discovery 批次因為跳過這一步、直接沿用工具建議的 `soul_2` 無錨點生成，導致同批次 4 張圖臉孔不一致。
- [ ] 裝置/鏡頭是否具體指定
- [ ] 皮膚質感關鍵字是否存在
- [ ] 光線配方是否符合場景類型：室內親密場景用「混合不均勻」，戶外/生活風格場景用「討喜自然光+淺景深」——**兩者都不等於「畫質差/調暗調糊」**
- [ ] 身材數據（三圍/罩杯，見 `profile.json` 的 measurements）是否直接寫進 prompt，不要只用模糊形容詞
- [ ] 背景是否有具體生活雜物細節
- [ ] 服裝是否完整明確寫出（不留給模型自己猜）
- [ ] （影片）環境音層是否有指定，`generate_audio` 設定是否正確
- [ ] **（運動/健身類角色專用）是否偏向健美選手/男性化方向**：任何帶有「運動員」「健身」「肌肉線條」設定的角色，prompt 都必須明確寫「漂亮性感」「柔和曲線」「淡淡若隱若現」這類字眼，並且**明確排除**「塊狀肌肉」「血管紋理」「銳利強勢的臉」「健美比賽站姿」。2026-07-24：Vicky Lin 第一輪試跑因未做這個排除，實際生成結果變成健美選手體態，使用者明確否決、已重新生成描述——這是每個運動類角色都要檢查的固定項目，不是個案。
- [ ] **（臺灣籍角色專用）膚色是否為白皙基調**：即使是戶外/海邊/健身類人設，也不可整體呈現古銅/小麥/曬黑色調——見上方第 6 點
- [ ] **（2026-07-30 新增）整組素材是否混合自拍與他拍視角**，不是全部都用同一種「棚拍/編輯攝影」語氣——見上方第 7 點
- [ ] **（建立實際 Soul 訓練集專用，非探索性預覽）是否用 Reference Element 錨定身分，而不是每張獨立文字生成**：2026-07-25 Vicky Lin 案例發現，用同一組文字 prompt 各自獨立呼叫 8 次生成（無身分錨點），每次生成模型都會重新「想像」一個符合描述但**不是同一個人**的臉/身形——8 張圖風格看起來一致，但實際上是 8 個不同的人，不是同一人的 8 個角度。若把這種身分不一致的圖直接送進 Soul 訓練，訓練結果會是多人特徵的平均/混合，而非使用者想要的單一穩定身分。**正確流程**：(1) 先生成或從既有圖中選出**一張**使用者核准的參考圖；(2) 用 `media_upload` → PUT 位元組 → `media_confirm` → `show_reference_elements(action='create')` 把這張圖轉成可重複使用的 Reference Element，取得 `element_id`；(3) 之後每張訓練圖的 prompt 都內嵌 `<<<element_id>>>` 取代文字描述五官/身形，只變化角度、景別、姿勢、場景、穿搭——這樣後端會把同一張參考圖直接注入生成，確保臉部/身形真正共享同一身分。此流程適用於**任何角色**建立正式 Soul 訓練集之前，不只是 Vicky Lin 的個案；純探索性的一次性風格預覽（不打算送訓練）則不受此限制。

---

## 場景庫

---

### 一、Morning / Waking Up（晨起系列）20%

#### Scene M-1：床上晨起，直視鏡頭

**場景描述**：剛醒來的樣子，躺在白色棉麻床單上，枕頭有壓過的痕跡，頭髮略亂但好看。
**服裝**：oversized 白色棉T or 絲質細肩帶睡衣（米白 / 淡粉）
**燈光**：早晨窗邊側光（7–9am），漫射、柔和，不強烈直射
**鏡頭角度**：臉部至上半身，從略高俯角向下拍（床上視角），直視鏡頭
**情緒**：慵懶、剛醒、眼神半睜、不用力

```
lying on white linen bed, morning sunlight streaming softly through window,
wearing oversized white cotton t-shirt, sleepy half-lidded eyes looking directly at camera,
hair slightly messy on pillow, one arm stretched above head, close-up chest-to-face,
slightly overhead angle, warm diffused morning light, intimate bedroom atmosphere
```

---

#### Scene M-2：鏡前晨間，梳整頭髮

**場景描述**：早晨站在衛浴或臥室鏡前，梳頭髮或撥頭髮，半側面，沒有意識到被拍。
**服裝**：薄棉細肩帶背心 + 短褲，或只穿細肩帶睡衣上身
**燈光**：冷白浴室自然光 or 暖黃臥室晨光，取決於角色
**鏡頭角度**：從側後方拍，鏡子裡能看到她的正面，形成雙重視角
**情緒**：自然、不表演、沉浸在自己的事情裡

```
standing in front of large bedroom mirror in the morning, wearing thin cotton cami top and shorts,
hands lifting hair to tie it up or letting it fall, looking at her own reflection not at camera,
soft warm morning light from window casting gentle shadow, 3/4 angle from behind showing mirror reflection,
candid unposed moment, natural relaxed posture
```

---

#### Scene M-3：窗邊發呆，手拿咖啡杯

**場景描述**：早晨靠著窗邊，捧著咖啡杯，望向窗外，什麼都不想。
**服裝**：oversized 男友款針織毛衣（下身若隱若現）or 薄紗睡袍
**燈光**：早晨窗邊強逆光（backlit silhouette 感）or 側光打在臉部輪廓
**鏡頭角度**：從室內平視拍向窗邊，半身或全身，逆光讓輪廓發光
**情緒**：靜止、思緒飄遠、沉浸在自己的早晨

```
standing by window in morning, holding ceramic coffee mug with both hands,
wearing oversized knit sweater that barely covers, gazing out at the view not at camera,
strong backlit window light creating soft glowing outline, 3/4 body shot from inside the room,
dreamy quiet morning energy, slightly soft focus on background
```

---

#### Scene M-4：床上坐起，剛睡醒的懶散

**場景描述**：坐起來但還沒真正醒，腿收在胸前，頭靠在膝蓋上，或者撐著床頭板。
**服裝**：短版睡衣套裝（棉質細肩帶 + 短褲）或單穿細肩帶
**燈光**：窗簾沒完全拉開，漫射的柔和室內光，有點昏暗但溫暖
**鏡頭角度**：從床腳方向平視拍，全身，她在畫面一角
**情緒**：剛醒、軟、有一點可愛的困惑感

```
sitting up on bed with knees pulled to chest, wearing cotton cami and shorts set,
head tilted to one side, eyes slightly unfocused just woken up, morning light filtering through curtains,
full body shot from end of bed, off-center composition with negative space,
rumpled white bedding around her, intimate domestic atmosphere
```

---

### 二、Outfit / Changing（換裝系列）20%

#### Scene O-1：鏡前試穿，檢視全身

**場景描述**：站在全身鏡前，正在看自己的穿搭，頭微側，表情是在評估。
**服裝**：今天的穿搭（依角色的服裝公式選擇），上衣或洋裝
**燈光**：室內自然光 or 窗邊側光，讓穿搭的細節和身材比例清晰
**鏡頭角度**：鏡面正面拍（從鏡子裡看她），或從側面拍她看鏡子，雙版本各有效果
**情緒**：自我評估、安靜的自信、沒有為鏡頭表演

```
standing in front of full-length mirror looking at her reflection, head slightly tilted assessing the outfit,
wearing [outfit], natural indoor light from nearby window,
mirror selfie shot — camera visible in mirror reflection held casually at chest height,
slightly off-center, neutral expression with hint of satisfaction, body visible from head to toe
```

---

#### Scene O-2：換裝中途，只穿內搭

**場景描述**：換衣服換到一半，只穿內搭（細肩帶或運動背心），下一件衣服還拿在手上。
**服裝**：棉質細肩帶或 bralette（SFW），手上拿著還沒穿的外衣
**燈光**：臥室窗邊自然光，柔和直接
**鏡頭角度**：3/4 身，平視，她側對著鏡頭
**情緒**：隨意、自然，不是在表演性感，就是在換衣服

```
mid-outfit-change, wearing just a cotton cami or bralette, holding a shirt in one hand not yet put on,
turning slightly to grab something off the bed, 3/4 body angle, casual and unaware,
bedroom natural light, clothes visible on bed in background suggesting she's been trying things on,
natural relaxed posture, candid moment
```

---

#### Scene O-3：坐在床邊穿鞋，低頭綁鞋帶

**場景描述**：快要出門，坐在床邊穿鞋或綁鞋帶，低頭，整套穿搭清晰可見。
**服裝**：完整的當日穿搭，腿部可見（短裙 / 短褲 / 緊身褲）
**燈光**：室內暖光 or 窗邊午前光
**鏡頭角度**：從斜前方平視，全身坐姿，腿部比例清楚
**情緒**：準備出門的最後一刻，專心、不看鏡頭

```
sitting on edge of bed putting on sneakers, wearing [full outfit] showing legs clearly,
leaning forward to tie laces, focused on shoes not camera,
bedroom ambient light, full body sitting shot from slightly in front and to the side,
outfit fully visible, candid getting-ready moment before going out
```

---

#### Scene O-4：衣服掛滿，站在衣櫃前考慮

**場景描述**：站在打開的衣櫃前，手放在衣架上，思考今天要穿什麼。只穿著睡衣或內搭。
**服裝**：晨間睡衣或細肩帶，背對或側對鏡頭
**燈光**：臥室窗光或衣櫃燈的暖黃光
**鏡頭角度**：從床側拍她的背影或側面，衣櫃填滿背景
**情緒**：日常選擇的糾結，安靜、不為人看的狀態

```
standing in front of open wardrobe in morning, wearing cami and shorts or silk slip,
hand resting on hanging clothes looking at options, back or side profile facing the wardrobe,
warm soft light from bedside lamp or window, full body or 3/4 shot,
intimate domestic scene, clothes clearly hanging in background, no awareness of camera
```

---

### 三、Bathroom / After Shower（浴後系列）15%

#### Scene B-1：浴後白巾，浴室鏡前

**場景描述**：洗完澡，白色浴巾包裹身體，站在浴室鏡前，頭髮濕潤，皮膚微紅。
**服裝**：白色浴巾（從胸部包到大腿），或浴袍
**燈光**：浴室柔和燈光（不是刺眼白光），或窗邊透進的自然光，有蒸氣感
**鏡頭角度**：平視，半身或全身，可以是鏡中反射
**情緒**：剛洗完澡的放鬆、皮膚有水份的光澤、不刻意

```
standing in bathroom after shower, wrapped in white towel tucked at chest,
damp hair, skin slightly flushed, facing bathroom mirror with relaxed expression,
soft warm bathroom light with faint steam in air, medium shot mirror reflection visible,
natural post-shower state, one hand touching damp hair, calm and unhurried
```

---

#### Scene B-2：護膚例行，棉T站在浴室

**場景描述**：洗完澡換上棉T短褲，站在浴室或梳妝台前做護膚，拍眼霜或塗乳液。
**服裝**：短版棉T + 短褲，或細肩帶背心，皮膚剛洗完澡的狀態
**燈光**：浴室冷白自然光（Yuna 類型）或暖黃窗邊光（Camille 類型）
**鏡頭角度**：臉部至上半身近景，她看向鏡子而不是鏡頭
**情緒**：專注、護膚中、沉浸在自己的事情

```
standing at bathroom vanity doing skincare, wearing cotton cami and shorts,
applying moisturizer with fingertips, eyes focused on mirror reflection not camera,
clean bathroom light, close-up chest to face, skin visibly clean and freshly washed,
peaceful skincare routine moment, minimal products visible on counter
```

---

#### Scene B-3：浴缸邊，腿伸出來

**場景描述**：泡澡中，側躺在浴缸邊緣，腿伸出來，手臂放在浴缸邊，眼睛閉著或望向上方。
**服裝**：無（泡泡浴遮蓋），或薄棉睡袍放在浴缸邊
**燈光**：蠟燭暖光 or 浴室晨光，整體昏暗而溫暖
**鏡頭角度**：從浴缸側面拍，半身，腿部清晰可見
**情緒**：完全放鬆、奢侈的獨處時刻、慵懶而滿足

```
lying in bathtub with foam bubbles, one leg resting on the edge of the tub,
arm draped over the side, eyes closed or looking upward with relaxed expression,
warm candlelight or soft bathroom window light, medium shot from the side showing profile and leg,
steamy intimate bathroom atmosphere, small candles or greenery visible in background
```

---

### 四、Home Lounging（居家閒躺系列）20%

#### Scene L-1：沙發上的懶散，滑手機

**場景描述**：窩在沙發上，腿搭在扶手上或橫躺著，滑手機，完全不在意被拍。
**服裝**：oversized 棉T + 短褲，或細肩帶 + 短褲，光腳
**燈光**：午後客廳自然光（窗簾沒完全拉），或傍晚落地燈的暖光
**鏡頭角度**：從沙發正前方或斜前方平視，全身可見，偏側臥姿
**情緒**：完全放鬆、無聊但自在、這是她家她最隨意的樣子

```
lying on sofa with legs up over the armrest, scrolling phone held above face,
wearing oversized cotton tee and shorts, barefoot, hair loose and casual,
afternoon living room light through curtains, full body side-lying shot from in front of couch,
comfortable domestic laziness, zero performance for camera, phone screen slightly glowing
```

---

#### Scene L-2：地板坐著，吃零食看電視

**場景描述**：坐在客廳地板上，背靠沙發，吃零食，面前可能有筆電或電視。
**服裝**：短版棉T + 緊身短褲，或運動短褲，光腳
**燈光**：電視 / 螢幕的藍光 + 室內暖燈，兩種光同時存在
**鏡頭角度**：從斜側面平視，半身至全身，她面對螢幕而非鏡頭
**情緒**：完全在自己的世界裡、有點懶、有點放空

```
sitting on living room floor with back against sofa, eating snacks from a bowl,
wearing crop tee and tight shorts, legs stretched out or crossed,
TV or laptop screen light mixing with warm lamp in background,
3/4 shot from the side, completely absorbed in screen, natural domestic scene
```

---

#### Scene L-3：臥室地板，看書或發呆

**場景描述**：坐在臥室地板上，背靠床，腿伸直，手拿一本書或什麼都不做，望向遠處。
**服裝**：細肩帶背心 + 短褲，光腳，頭髮鬆散
**燈光**：午後臥室窗邊散射光，整體柔和暖黃
**鏡頭角度**：從正前方或斜前方平視，全身，腿部比例清楚
**情緒**：沉靜、一個人的時光、完全不需要表演

```
sitting on bedroom floor leaning against the bed, legs stretched out, reading a book or looking into distance,
wearing cami top and shorts, barefoot, hair loosely tied or down,
soft afternoon light from window, full body front-facing shot showing long legs,
quiet introspective mood, entirely alone in her own world
```

---

#### Scene L-4：床上捲縮，抱枕頭，電話中

**場景描述**：側躺在床上，抱著枕頭，講電話或聽音樂，身體捲縮但放鬆。
**服裝**：絲質細肩帶睡衣 or 棉質短版睡衣套裝
**燈光**：傍晚臥室暖燈光，溫柔而昏黃
**鏡頭角度**：從床側拍，全身側躺，她面對另一個方向
**情緒**：放鬆、溫暖、像好朋友偷偷拍到的她

```
lying on side on bed hugging pillow, on phone or listening to music with earphones,
wearing silk slip or cotton pajama set, knees slightly bent, body curled comfortably,
warm evening bedroom lamp light, full body shot from side of bed,
she's facing away from camera or turned slightly, intimate cozy evening at home
```

---

### 五、Hotel / Travel（飯店旅行系列）15%

#### Scene H-1：飯店大床，剛到房間

**場景描述**：剛到飯店，直接倒在大床上，仰躺或趴著，行李還放在旁邊。
**服裝**：出門的當日穿搭（不用特別換），或剛換上飯店睡袍
**燈光**：飯店房間的暖黃燈光，或窗外的城市光線透進來
**鏡頭角度**：從床腳方向拍，全身，她倒在床上，城市窗景在背景
**情緒**：旅行抵達的放鬆感、終於可以倒下、有點興奮

```
just arrived at hotel room, flopped on the large bed face-up or face-down,
wearing travel outfit still, arms out to the sides, shoes possibly still on one foot,
warm hotel room lighting with city view visible through window,
full body shot from foot of bed looking toward the window, bags visible to the side,
arrival relief energy, genuine exhausted-but-happy
```

---

#### Scene H-2：飯店浴袍，窗邊看夜景

**場景描述**：穿著飯店白色浴袍，站在落地窗前，一手拿著酒杯或咖啡，看著城市夜景。
**服裝**：白色飯店浴袍，寬鬆，腰帶輕繫
**燈光**：室內暖燈 + 窗外城市燈光，對比鮮明
**鏡頭角度**：從房間內側拍，半身或全身，她面對窗戶背對鏡頭，或側面
**情緒**：有點孤獨也有點自在、城市在腳下、這個夜晚是她自己的

```
wearing white hotel robe loosely belted, standing at floor-to-ceiling window holding a wine glass,
looking out at city lights below, back or profile to camera,
warm amber room lighting contrasting with blue-lit city outside,
full body or 3/4 shot from inside the room, cinematic quiet night energy
```

---

#### Scene H-3：飯店泳池，躺椅邊

**場景描述**：飯店屋頂泳池，坐或躺在白色躺椅上，腿垂入水或晒太陽，有飲料在旁邊。
**服裝**：一件式泳衣 or 比基尼（依角色選擇），太陽眼鏡
**燈光**：下午陽光（3–5pm），直射或城市天際線背景
**鏡頭角度**：從旁邊平視拍，全身或半身，腿部比例清楚
**情緒**：vacation mode、陽光、完全不想事情

```
sitting on poolside lounger at hotel rooftop pool, legs dangling in turquoise water,
wearing one-piece swimsuit [or bikini], sunglasses on, hand resting on armrest with drink nearby,
afternoon sun casting warm shadows, city skyline visible in background,
3/4 body shot from poolside, relaxed confident vacation energy, slightly squinting in the sun
```

---

#### Scene H-4：飯店床上，深夜獨處

**場景描述**：飯店房間深夜或清晨，在床上吃簡單的東西或喝東西，手機在旁邊，燈光很暗。
**服裝**：飯店睡袍 or 自帶的細肩帶睡衣
**燈光**：床頭燈的暖黃光，只有一個光源，整體很暗但溫暖
**鏡頭角度**：從床側拍，半身，她看著手機或看向食物，不看鏡頭
**情緒**：旅行時的那種「不想睡」、獨自在陌生城市的夜晚感

```
late night in hotel room sitting on bed eating room service snacks or drinking tea,
wearing silk slip or hotel robe, phone lit beside her on the bed,
only bedside lamp on creating warm intimate pool of light in otherwise dark room,
medium shot from beside the bed, she's focused on her phone not camera,
quiet solo traveler night energy, city outside the window dark and distant
```

---

### 六、Daily Selfie Video（手機自拍日常影片）— 主力內容

> **定位**：男性受眾的核心日常內容。手機自拍感，真實不刻意，展示身材但不像廣告。
> **模型**：`kling3_0`（單鏡頭，透過 `start_image` 鎖定臉部身份）
> **Benchmark 帳號**：@yua_mikami、@asuka.kirara、@eimi0318
> **完整 SOP 見**：`DAILY_VIDEO_SOP.md`

#### 核心方向

- **不是廣告**：不要 multi-shot 剪輯，不要旁白，不要 CTA，就是她在自拍
- **手機自拍角度**：slightly overhead angle（從上方俯拍臉和胸），或 arm-level selfie（正面平視）
- **鏡頭真實感**：適時加入輕微 camera rotation / movement，讓影片看起來像真人拿著手機拍
- **BGM 後製**：聲音在 CapCut 後製加入，生成時 `sound = "on"` 但 prompt 不提音樂

#### 已驗證場景（2026-07-07 全部批准）

| KOL | 場景 | 服裝 | 重點 | Start Frame Media ID | Video Job ID |
|-----|------|------|------|----------------------|-------------|
| Iris Chen | 浴室鏡前，手持手機自拍，微微低頭露乳溝 | 黑色細肩帶背心 | 乳溝，浴室燈光 | `b8078a7d` | `b68ac46c` |
| Yuna Kim | 飯店房間門邊慢慢轉身，側面到正面展示胸腰比 | 白色 crop top + 低腰牛仔短褲 | 胸腰比，身材線條 | `9e7d8009` | `2aca7a9e` |
| Luna Tanaka | 床上仰拍，俯角，臉到胸口，微笑看鏡頭 | 白色薄棉睡衣，領口微開 | 童顏巨乳反差 | `81d7442e` | `c2cfc025` |
| Aaliya Rivera | 泳池邊，半身出水，撥頭髮，看鏡頭 | 黑色比基尼上衣 | 濕身，運動感性感 | `e6892cd0` | `d51676c3` |
| Camille Dupont | 臥室窗邊逆光，轉頭看鏡頭，側面輪廓 | 白色絲質（實際生成：crop top + bikini bottom） | 逆光側面輪廓 | `5c868b09` | `c70f6307` |
| Ananya Kapoor | 浴室出來，濕髮，毛巾裹身，露鎖骨露肩 | 白色浴巾，微開露肩 | 濕髮，鎖骨，肩膀 | `d94c27c9` | `59dcbb98` |

#### Start Frame 生成原則

- **角度**：描述「phone selfie angle from above」或「arm-level selfie」，而非「她拿著手機」
- **服裝**：日常服裝（睡衣、泳衣、浴巾等），不能用舞蹈 start frame 代替
- **服裝避雷**：crop top 露腹、belly dance bra 等 revealing 服裝 → `status: "failed"`（pixel-level filter）
- **Soul ID 流程**：`soul_2` 生成圖 → `media_import_url` 匯入 → `image_media_id` → 帶入 `kling3_0` 的 `start_image`

#### 影片 Prompt 核心元素

```
[年齡+民族+身材特徵],
[場景描述 — 浴室/床/泳池/飯店],
[服裝] + [關鍵身體焦點 — cleavage/collarbone/waist ratio],
[動作 — 轉身/撥頭髮/看鏡頭],
[鏡頭角度 — phone selfie / overhead / arm-level],
[光線描述],
single continuous shot, phone selfie casual feel, warm tones
```

#### 鏡頭真實感規則

- 日常自拍影片應加入輕微 camera rotation / subtle hand movement
- 讓影片看起來像真人手拿手機拍，而非三腳架固定的靜態畫面
- 在 prompt 加入：`slight natural camera movement as if hand-held, subtle rotation`

#### 各 KOL 日常自拍推薦方向

| KOL | 場景方向 | 服裝方向 | 身體焦點 |
|-----|---------|---------|---------|
| **Iris Chen** 台北熱辣 | 浴室、健身後、臥室 | 黑色細肩帶、運動背心 | 乳溝、腰線 |
| **Luna Tanaka** 京都安靜 | 床上、榻榻米、浴室後 | 白色薄棉睡衣、浴巾 | 童顏巨乳反差、鎖骨 |
| **Ananya Kapoor** 孟買舞者 | 浴室後、瑜伽後、泳池 | 浴巾、瑜伽服 | 鎖骨、肩線、纖腰 |
| **Yuna Kim** 首爾美妝 | 飯店、臥室、護膚時 | crop top、睡衣 | 胸腰比、高挑身材 |
| **Aaliya Rivera** LA 拉丁 | 泳池、海邊、健身後 | 比基尼上衣、運動服 | 曲線、濕身效果 |
| **Camille Dupont** 巴黎慢活 | 臥室窗邊、飯店、浴後 | 絲質睡衣、浴袍 | 側面輪廓、逆光 |

---

### 七、TikTok Dance（舞蹈影片系列）

> 完整生成流程見 `DANCE_VIDEO_SOP.md`。本節僅記錄場景庫和服裝參考。

**核心氛圍**：跟著 TikTok 熱門歌曲跳舞，性感有活力，節拍感強。三段式：進場→主舞→收尾。

#### 服裝選擇原則

| 類型 | 服裝範例 | 效果 |
|------|---------|------|
| 緊身運動風 | black crop top + high-waist biker shorts | 腰線和臀線清晰，動作自然 |
| 性感休閒 | light blue V-neck mini dress | 飄逸感，裙擺隨動作飛起 |
| 派對風 | silver metallic mini skirt + crop top | 反光，在燈光下效果好 |
| 街頭風 | oversized hoodie（crop）+ tight shorts | 年輕感，臀部線條突出 |

**構圖規則**：所有舞蹈影片使用 **THREE QUARTER SHOT（mid-thigh up, no shoes shown）**，避免腿部截斷。

#### 背景選擇

| 背景 | 氛圍 | 適合 |
|------|------|------|
| Plain white/gray studio | 簡潔，突出舞者 | 首選（不分散注意力） |
| Urban rooftop, city at dusk | 城市感，台北/首爾 | 有場景感的版本 |
| Club/neon lighting background | 夜店感，強燈光 | 派對主題 |
| Bedroom/living room | 居家隨性感 | 模仿真實 TikTok 風格 |

#### 音樂類型與舞蹈效果

| 音樂類型 | 適合舞蹈 prompt 描述 |
|---------|-------------------|
| 越南鼓（Vietnamese drum） | `powerful rhythmic stomping, traditional meets street style, hip drops` |
| K-pop（流行/電音） | `K-pop choreography, sharp arm movements, body roll, bouncing to beat` |
| 拉丁（reggaeton/cumbia） | `hip-hop reggaeton moves, waist rolls, confident swagger` |
| 西方流行（pop/R&B） | `body wave, chest bounce, fluid arm movements, sensual groove` |

#### 各 KOL 舞蹈推薦

| KOL | 推薦服裝 | 推薦音樂 | 背景 |
|-----|---------|---------|------|
| **Iris Chen** 台北熱辣 | 黑色 crop top + 騎車短褲，或 mini dress | 越南鼓、Sugar on my tongue | 白色背景或城市夜景 |
| **Luna Tanaka** 京都安靜 | 白色短版和服領上衣 + 黑色緊身褲 | 輕柔 J-pop 或 city pop | 日式簡潔室內 |
| **Ananya Kapoor** 孟買舞者 | 印度傳統 crop top + 露腰半裙 | Bollywood remixes | 金色燈光背景 |
| **Yuna Kim** 首爾美妝 | 韓系短版外套 + 短褲 | K-pop | 首爾都市感背景 |
| **Aaliya Rivera** LA 拉丁 | 性感拉丁裙或緊身褲 | Reggaeton/Latin pop | 城市夜景 |
| **Camille Dupont** 巴黎慢活 | 法式休閒 + 緊身褲 | 法語流行 or 歐洲電音 | 簡潔白背景 |

---

### 七、Fitness / Active（運動系列）10%

#### Scene F-1：瑜伽後躺在地墊上

**場景描述**：瑜伽做完，仰躺在瑜伽墊上，手臂張開，閉眼放鬆，做最後的攤屍式。
**服裝**：瑜伽套裝（高腰緊身褲 + 運動背心 or sports bra）
**燈光**：室內瑜伽空間的自然漫射光，或晨間木地板上的斜射光
**鏡頭角度**：從正上方俯拍（鳥瞰），全身，她在地墊上
**情緒**：運動後的完全放鬆、什麼都不想、身體在地板上融化

```
lying flat on yoga mat after practice in savasana pose, arms slightly out to sides, eyes closed,
wearing high-waist yoga leggings and sports bra, visible muscle definition,
soft natural light on wooden floor, overhead bird's eye shot looking down at her on the mat,
complete post-workout surrender, slight sheen of sweat, peaceful exhaustion
```

---

#### Scene F-2：鏡前伸展，側面線條

**場景描述**：對著大鏡子做伸展，側面拍到她的身體線條，表情專注，沒有對鏡頭。
**服裝**：高腰緊身瑜伽褲 + 細肩帶運動上衣，光腳
**燈光**：健身空間的自然光 or 大窗側光，強調身體線條的立體感
**鏡頭角度**：側面拍，全身，身體的伸展線條是主角
**情緒**：專注、身體的力量感、完全沉浸在動作裡

```
stretching in front of large mirror, side profile showing full body extension,
wearing high-waist leggings and fitted sports top, barefoot on wood floor,
strong natural side light from window accentuating muscle lines and curves,
full body side shot, expression focused and absorbed in the stretch, not looking at camera
```

---

#### Scene F-3：運動後，坐在地板喝水

**場景描述**：健身或跑步完，坐在地板上，腿伸直，大口喝水，頭髮有些凌亂，臉上有汗。
**服裝**：運動套裝（緊身褲 + 運動背心），可能有外套半脫在腰上
**燈光**：戶外黃金時段光 or 室內健身空間自然光
**鏡頭角度**：從斜前方平視，半身至全身，她正在喝水，不看鏡頭
**情緒**：運動完的真實疲憊感、有汗有氣、這個狀態比刻意擺拍更吸引人

```
sitting on floor after workout, legs stretched out, drinking from water bottle,
wearing athletic set, hair slightly disheveled, light sweat visible on skin,
golden hour outdoor light or gym window light, 3/4 body shot from slightly in front,
looking at something off-frame not camera, genuine post-exercise fatigue and satisfaction,
sports jacket or hoodie loosely around waist
```

---

## 各角色推薦組合

| KOL | 最適配場景（按角色美學） |
|-----|----------------------|
| **Iris Chen** 台北熱辣 | O-1 鏡前穿搭、M-1 床上晨起直視鏡頭、H-3 飯店泳池、Dance 六 舞蹈影片 |
| **Luna Tanaka** 京都安靜 | M-3 窗邊發呆、B-3 浴缸邊、L-3 臥室地板看書 |
| **Ananya Kapoor** 孟買舞者 | F-1 瑜伽後躺墊、F-2 鏡前伸展、M-3 窗邊（晨間海邊版） |
| **Yuna Kim** 首爾美妝 | B-2 護膚例行、M-2 鏡前梳整、O-1 鏡前穿搭 |
| **Aaliya Rivera** LA 拉丁 | H-3 飯店泳池、O-2 換裝中途、L-1 沙發懶散 |
| **Camille Dupont** 巴黎慢活 | M-3 窗邊（薄紗睡袍版）、H-2 浴袍看夜景、B-3 浴缸泡澡 |

---

## Prompt 通用結尾模板

所有場景加上以下結尾效果更佳：

```
film grain, candid lifestyle photo, shot on 35mm, warm tones,
slightly off-center composition, natural imperfect framing like a friend took the photo
```

---

*最後更新：2026-07-07*
