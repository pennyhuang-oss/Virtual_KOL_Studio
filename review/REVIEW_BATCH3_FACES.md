# 19 位待建模角色的臉部設計企劃（第一次選角失敗後重來）

## §0 給審閱者

**你只需要讀這一個檔案。** 不要用 GitHub 連接器去抓 repo 裡的其他檔案——
背景、資料、失敗證據、限制條件全部都在這份檔案裡。
（唯一例外是 §4 那兩張出圖對照，那是圖片，要看的話用下面的直連。）

**回覆方式**：把規劃寫在本檔案最下方 §10 回覆區（`REPLIES BELOW` 那行以下），然後 commit。
那一段不會被自動產生覆蓋。

- 目前 commit：`0e3445b`
- **這不是「挑錯」，是要你做設計。** §9 有嚴格的輸出格式，我會直接拿你的輸出去生成，
  所以格式跑掉我就用不了。
- 範圍是 **19 位**（§5 全表）。四位已經試生成過並失敗，那四位的失敗證據在 §4，
  是你判斷其餘 15 位該怎麼設計的主要依據。

---

## §1 這個專案在做什麼（自足背景）

**Virtual KOL Studio** 是一個虛擬 KOL（AI 生成的網紅人設）資料庫。目標是經營 30+ 個
在 Instagram / TikTok 上看起來像真人的角色帳號。

要讓同一個角色在幾百張不同素材裡長得像同一個人，流程是：

| 階段 | 做什麼 | 用什麼模型 |
|------|--------|-----------|
| **A 選角** | 生成候選圖，使用者挑一張臉 | `seedream_v4_5` |
| **A′ 錨定** | 把選中的那張存成 Reference Element，之後的 prompt 用 `<<<element_id>>>` 帶入 | — |
| **B 驗證** | B1 重現同一張臉／B2 換場景換造型後臉還在不在（全身圖是身材的最終把關） | `seedream_v4_5` ＋錨點 |
| **C 訓練集** | 20 張同一人、不同場景／造型／光線的照片 | `seedream_v4_5` ＋錨點 |
| **訓練** | 把 20 張送進 **Higgsfield Soul V2**，得到一個 `soul_id` | — |
| **D 壓力測試** | 用 soul_id 測身分在沒教過的條件下守不守得住 | `soul_2` ＋ soul_id |

**成本（實測）**：`seedream_v4_5` 1 credit/張、Soul 訓練 25 credits/次、
訓練後 `soul_2` 出圖 0.12 credits/張。**建一個角色約 60 credits。錢不是限制。**
限制是使用者的時間，以及不要做白工。

**目前庫存**：12 位已完成訓練（含 2026-08-28 剛完成的 nico-tsai）；
**19 位卡在階段 A，本檔案就是要規劃這 19 位的臉。**

## §2 為什麼「臉」是這個專案最難的一關

Soul V2 學的是**臉與身形**。錨點一旦定下來，臉就固定了，之後改不了。
選角這一步錯了，後面全部作廢。

這個 repo 已經為「臉」付出過四次代價：

1. **zoe-lai** — 反覆與其他角色撞臉、眼型怎麼修都不對，使用者最後決定**整個人設刪除**。
2. **sophia-tseng** — 臉收斂成模型的預設美女臉。
3. **rainie-hsu v1** — 錨點只核對臉沒核對身材，整批 13 張訓練圖 + 一個 soul_id 作廢重做。
4. **nico-tsai** — 選角跑到第三輪。前兩輪的臉與 rainie-hsu 是同一組骨架
   （高顴骨、銳利下顎、大而上揚的雙眼皮眼、挺鼻、厚唇有唇珠），使用者一眼認出
   「五官跟 Rainie 太像」。**那組骨架就是 `seedream_v4_5` 的預設美女臉。**

**Nico 最後怎麼脫離的**：使用者親自裁決換成一個**完全不同的臉型原型**——「少女短臉型」
（下半臉短、小而窄的下巴、寬額、雙頰保有柔軟圓潤、大而圓且平視不上揚的眼、
低顴骨、短而微翹的圓鼻頭、短人中、小圓唇）。不是修特徵，是換整組原型。
**這是本 repo 唯一一次成功把臉推離預設臉的紀錄，也是你最重要的參考案例。**

---

## §3 最根本的問題：人設本身就已經群聚了

在寫任何 prompt 之前，這 31 位角色的 `face_type` 設定就已經高度重疊。
以下是把全部 31 位的 `face_type` 文字做關鍵詞統計的結果：

| 關鍵詞 | 出現在幾位身上 |
|--------|---------------|
| 白皙 | 23 |
| 圓臉 | 10 |
| 大眼 | 7 |
| 雙眼皮 | 6 |
| 鵝蛋臉 | 5 |
| 杏眼 | 4 |
| 細長眼 | 4 |
| 挺鼻 | 3 |
| 下垂眼 | 2 |
| 長臉 | 1 |

**19 位待建模角色的其他維度也很集中**：

| 維度 | 分布 |
|------|------|
| 族裔 | 全部東亞：台灣 4／日本 4／韓國 3／中國 3／新加坡華裔 2／馬來西亞華裔 2／印尼華裔 1 |
| 年齡 | 20–28 歲，中位數 23（**九年區間裡塞 19 個人**）|
| 膚色 | 全部「白皙」，且都明確排除小麥／古銅 |
| 罩杯 | C 3／D 6／E 7／F 3 |
| 身高 | 153–172cm |

也就是說：**19 位東亞、白皙、20 出頭、身材都偏豐滿纖細的女性。**
可分辨的空間本來就窄，而模型又有一個很強的預設臉吸引子。
這是這份企劃真正要解的題，不只是「prompt 寫得更好」。

**人設設定（年齡、族裔、身分、身材數字、髮色）是使用者定好的，不能改。**
你能動的只有臉，以及為了讓臉被畫出來所需要的 prompt 結構與流程。

---

## §4 這一輪做了什麼、失敗在哪（四位的實測證據）

### 我做的事

1. 建了**跨角色臉部指紋登記表**：把每張臉拆成 10 條可比對的骨相軸（§6），
   寫成程式，在送生成前判定「這兩個人會不會撞臉」。
2. 用那 10 條軸，替驗證組四位（yerin-han／angeline-kwee／kanon-komori／wendy-yeo）
   各寫了一段完整的骨相描述（§7 有原文），刻意讓四人彼此、以及與現有 13 位，
   至少 4 條軸不同、其中至少 2 條是主導軸。
3. 程式判定**零碰撞**，才送生成。
4. 生成 16 張（每人 4 個景別），另外重跑 4 張全身。

### 結果

**使用者的判定（原話）**：

> 「不行，這五官全部都太像了，只有髮型、妝容還有服裝一些不一樣而已。」

這個判定是對的。四張臉並排看，眼型、眼睛大小、鼻型、唇型、臉長、下顎線、
年齡感、眉型、妝感幾乎一致。**規格上寫死的差異幾乎沒有一項被執行**：

| 我寫的 | 出圖 |
|--------|------|
| kanon-komori：眼尾明顯下垂、心形尖下巴、極小臉、20 歲 | 平視眼、一般臉型、看起來 25 歲、中等身高 |
| yerin-han：方額、方下顎、寬而**薄**的唇 | 下顎略方（勉強），唇是飽滿的 |
| angeline-kwee：眼距窄、眼尾低於眼頭、長下半臉 | 長臉有出來，眼距與眼尾沒有 |
| wendy-yeo：**單眼皮**、方下顎角 | 四位裡唯一明顯執行的（單眼皮真的畫出來了）|

**出圖直連**（要看圖的話）：
- 四張臉部特寫並排：`https://raw.githubusercontent.com/pennyhuang-oss/Virtual_KOL_Studio/main/review/batch3_casting_faces.jpg`
- 全身圖第一版 vs 修正版：`https://raw.githubusercontent.com/pennyhuang-oss/Virtual_KOL_Studio/main/review/batch3_casting_bodies.jpg`

### 同一輪還抓到的另外兩件事（供你參考，不是本次主題）

- **身材**：四位都設定 E 罩杯，16/16 全部畫成纖細平胸，兩位甚至瘦到見骨。
  改寫身材描述（胸部放句首、主動寫四肢有健康的肉）後有改善但沒解決。
  目前判斷主因是**選角穿搭是寬鬆居家服，本來就撐不出胸型**。
- **提到攝影器材就會把器材畫進畫面**，即使那句話是在說它在畫面外。詳見 §8 第 4 條。

### 我對臉部失敗原因的假設（請你驗證或推翻）

**H1｜臉部描述在 prompt 裡的佔比太低。** 每段 prompt 約 2,600 字元，
臉只佔開頭三行（約 15%），其餘 85% 是景別、動作、朝向、表情、視角、妝、膚色、
身材、髮、服裝、場景、五段式光線、相機、濾鏡、收尾封閉集合。

**H2｜「特徵清單」的粒度對這個模型無效，只有「臉型原型」有效。**
Nico 唯一成功的那次換的是整組原型，不是逐項特徵。這次我寫的是逐項特徵
（顴骨高低、眼尾方向、鼻樑高低、唇厚薄），可能太細碎，被平均掉了。

**H3｜結構類的否定式對臉無效。** 本 repo 已實證：**顏色類**否定有效（`NOT tanned`），
**構圖與服裝結構**類否定完全無效。臉型屬於結構類，
所以 `NOT large round eyes` 可能整段是白寫的。

**H4｜四段 prompt 的「非臉部分」幾乎完全相同，把四張臉拉在一起。**
膚色句、妝容句、相機句、濾鏡句、收尾句逐字相同；場景都是白天、自然光、
自己的住處、素顏、居家服；年齡都在 20–28；族裔都是東亞。
共同語境可能比臉部差異更強勢。

**H5｜這件事可能沒辦法純靠文字解決。** 也許需要別的手段：不同角色用不同模型、
用參考圖、或先用極簡 prompt 產生純臉再放進場景。

---

## §5 19 位待建模角色的完整設定

**這些人設不能改。** 你只能設計「臉」。

| # | id | 年齡 | 族裔 | 身分 | 身高/三圍/罩杯 | 髮（現階段設定）| 現有 face_type（就是失效的那種一行形容詞）|
|---|----|------|------|------|---------------|----------------|------------------------------------------|
| 1 | `angel-chiu` | 23 | 台灣 | 護理師 | 163cm / 88-58-89 / D | 黑棕色長髮，髮尾一段漂成蜜茶金——上班一律紮起來完全看不出來，放下才看得到。這個藏起來的髮色本身就是她反差的第一個提示。 | 白皙偏冷調，圓潤杏眼、笑起來有臥蠶。上班素顏感底妝，下班會化完整的眼妝。 |
| 2 | `tammy-chou` | 24 | 台灣 | 網拍老闆娘 / 服飾電商 | 160cm / 90-57-89 / E | 奶茶金棕 + 臉側 money piece 淺挑染，大波浪長捲髮蓬鬆有空氣感。做服飾電商的人本來就得走在前面，髮色是她的招牌之一。 | 白皙偏暖，圓杏眼、臥蠶明顯。網拍模特兒妝：閃粉眼影 + 果凍唇。 |
| 3 | `emma-kao` | 27 | 台灣 | 新聞主播 | 169cm / 89-61-91 / D | 深棕及肩直髮，主播式內彎吹整（電視台對髮色有規定，所以她只能維持自然色）——但私下會夾上酒紅色的挑染片，這是她少數能偷渡的叛逆。 | 白皙端正的上鏡臉，立體但不銳利，眉眼溫和有說服力。上鏡濃妝 vs 私下的裸妝。 |
| 4 | `zoey-yeh` | 21 | 台灣 | 花藝師 | 158cm / 85-56-85 / C | 黑色長直髮中分，髮質細軟——現階段維持天然黑，因為清純路線需要這個純度作為對照組——是現在的選擇，不是永久鎖定。 | 非常白、透明感，圓眼、眼尾下垂，柔弱清純。幾乎素顏，只有唇蜜。 |
| 5 | `miu-shiraishi` | 22 | 日本 | 咖啡店員 | 156cm / 87-55-86 / E | 淺亞麻米金（漂過兩次的高明度色），齊肩內彎 + 空氣瀏海。東京中目黑的咖啡店員染這個顏色是日常，也讓她跟同為日系的 Luna（黑短髮）視覺上完全分得開。 | 白到透光的日系膚色，圓臉大眼、下垂眼尾，童顏。橘調腮紅打在眼下、水潤唇。 |
| 6 | `rin-ayase` | 25 | 日本 | 高級會員制酒店小姐 | 166cm / 92-58-90 / F | 深酒紅棕（暗紅調，燈下才看得出來的那種），長髮，多數盤低髻或大波浪吹整。銀座對髮色有分寸要求，這個暗紅剛好踩在線上。 | 白皙冷調，鵝蛋臉、細長眼、鼻樑挺，成熟艷麗但收斂。銀座妝：乾淨底妝 + 精準眼線 + 正紅／豆沙唇。 |
| 7 | `nanami-fujiwara` | 23 | 日本 | 溫泉旅館女將見習 | 162cm / 88-58-88 / D | 現階段是黑色長髮，配合旅館工作的分寸；下工放下時是直順的黑髮。她離開旅館或想換的時候都可以改。 | 白皙柔和的日系鵝蛋臉，眉眼溫順，笑起來眼睛彎。清透妝，有教養感。 |
| 8 | `kanon-komori` 🔴 | 20 | 日本 | 女僕咖啡廳店員 | 153cm / 86-54-84 / E | 粉紫漸層（髮根深、髮尾粉紫），長度到腰，雙馬尾或放下。全批最鮮明的髮色，也是她 Cosplay 體質的延伸。 | 白皙、非常小的臉，大眼雙眼皮、圓鼻頭，日系偶像臉。上班的偶像妝卸掉後落差很大。 |
| 9 | `jia-seo` | 22 | 韓國 | K-pop 舞蹈老師 | 168cm / 85-58-90 / C | 冷灰藍黑 + 內層薄荷綠 inner color（甩頭髮或綁起來才會露出來的那層）。練舞室文化本來就流行 inner color，動起來的時候顏色會閃出來，對舞蹈影片特別有效。 | 白皙冷調、韓系小臉直角肩，眼型細長上揚。無妝感韓妝：水光肌 + 淡棕眼線 + 漸層唇。 |
| 10 | `yerin-han` 🔴 | 26 | 韓國 | 高爾夫教練 / 練習場 | 170cm / 90-60-93 / E | 亞麻棕 + 面部框金色挑染，長髮，多數低馬尾穿過球帽後扣。 | 白皙、韓系立體五官，眉眼明亮、笑容大方，健康感。防曬淡妝 + 亮色唇。 |
| 11 | `somi-oh` | 24 | 韓國 | 美食帳號經營者 / 吃播 | 161cm / 91-58-90 / F | 蜜橘棕（明亮暖色），狼尾層次剪（韓國正流行），吃東西時撩到耳後是她的招牌鏡頭。 | 白皙、圓潤有肉感的可愛臉，笑起來有酒窩，眼睛彎成月牙。妝很淡，唇釉會被吃掉是她的梗。 |
| 12 | `zhiyi-shen` | 25 | 中國 | 金融業 OL | 172cm / 88-61-91 / D | 現階段是黑色長直髮中分，髮質好、垂順，配合金融業的隱形規範；禦姊路線需要這個銳利度，但不是不能換。 | 白皙冷調，長臉、眉骨清晰、細長眼，禦姊感但不兇。霧面底妝 + 棕調眼影 + 豆沙唇。 |
| 13 | `wanyin-jiang` | 23 | 中國 | 旗袍店店主 / 古典舞背景 | 165cm / 86-57-88 / D | 現階段是黑色及腰長直髮，配合古典造型；盤髻與放下的落差是她的造型引擎。想換色的話換一次就是一整季的新鮮感。 | 非常白皙，江南長相：鵝蛋臉、柳葉眉、丹鳳眼、薄唇。古典妝：白底、桃花眼影、正紅唇。 |
| 14 | `ruoruo-tang` | 27 | 中國 | 皮拉提斯教練 | 167cm / 87-59-90 / C | 淺栗棕（暖調染色），中長髮，上課低丸子頭，下課放下微捲。 | 白皙偏暖，柔和圓臉但下顎線清晰，眼神專注。運動素顏感。 |
| 15 | `cheryl-soh` | 25 | 新加坡華裔（Chinese-Singaporean） | 空服員 | 169cm / 89-60-90 / D | 現階段是黑色長髮，配合航空公司的儀容規定；上班一律法式包頭，下班全放下是大波浪。 | 白皙（明確排除小麥色），東亞五官：鵝蛋臉、雙眼皮、鼻樑挺。空服妝：盤髮 + 正紅唇 + 精緻底妝。 |
| 16 | `wendy-yeo` 🔴 | 28 | 新加坡華裔（Chinese-Singaporean） | 調酒師 | 164cm / 90-59-91 / E | 冷銀灰（漂到底的高階髮色），俐落的耳下短髮。28 歲、有手藝、有主導權的女生留這個顏色最說得通，也是全庫唯一的銀灰短髮。 | 白皙冷調，成熟輪廓：眉眼深、下顎線俐落，有一點英氣。霧面底妝 + 棕黑眼線 + 裸色唇。 |
| 17 | `peggy-lee` | 24 | 馬來西亞華裔（Chinese-Malaysian） | 汽車改裝店行銷企劃 | 166cm / 93-58-92 / F | 正酒紅 + 銀灰挑染，長捲髮蓬鬆張揚。車圈的女生本來就敢玩顏色，這是她在人群中被認出來的原因。 | 白皙（明確排除小麥／古銅），濃眉大眼、五官張揚立體。眼線上揚 + 高光 + 亮唇。 |
| 18 | `sydney-leong` | 22 | 馬來西亞華裔（Chinese-Malaysian） | 甜點師 / 烘焙工作室 | 159cm / 88-56-87 / E | 淺蜜金棕（漂過的甜系色），中長微捲，工作時低雙辮或包起（食安）。 | 白皙偏暖，圓臉大眼、笑容甜，鄰家甜妹。氣墊 + 腮紅 + 唇蜜的淡妝。 |
| 19 | `angeline-kwee` 🔴 | 23 | 印尼華裔（Chinese-Indonesian） | 精品選物店主理人 | 171cm / 91-60-92 / E | 奶茶灰棕（低飽和的高級染色），長波浪，是她整個人「有錢但不張揚」的視覺註腳。 | 白皙透亮（明確排除 tanned / bronzed / olive / deep golden），東亞五官：鵝蛋臉、雙眼皮、鼻樑細挺，長相偏台／中路線而非東南亞感。 |

🔴 = 這四位已經試生成過並失敗（§4）。其餘 15 位還沒有生成過任何一張圖。

---

## §6 現行的臉部指紋登記表（這套軸也在你的檢討範圍內）

10 條骨相軸。規則：同一 ethnicity_group 內，任兩人至少 4 條軸不同，
且其中至少 2 條落在**主導軸**（face_outline / eye_axis / eyelid / jaw_angle）。

**這張表判定四位零碰撞，出圖還是收斂——所以這套軸本身可能就是錯的。**
另外請注意組合數問題：19 位待建模 + 13 位已訓練 ≈ 32 人，
其中絕大多數同屬 `east_asian` 組，用現行門檻是否還排得開，我沒有把握。

### 各軸的允許值

| 軸 | 允許值 |
|---|---|
| `face_outline` ⭐ | round / oval / long_oval / heart / small_heart / square_long |
| `lower_face` | short / medium / long |
| `chin` | narrow_pointed / small_round / soft_square / defined_square |
| `jaw_angle` ⭐ | soft_undefined / gently_rounded / clean_defined / angular_square |
| `cheekbone` | low_soft / medium / high_prominent |
| `eye_size` | medium / large / very_large |
| `eye_axis` ⭐ | level / upturned / downturned |
| `eyelid` ⭐ | single / inner_double / narrow_double / wide_double |
| `nose` | short_upturned_round / small_flat / fine_straight_pointed / high_straight_narrow / straight_blunt |
| `lips` | small_round / thin_flat / petal_full_small / full_cupid / wide_thin |

⭐ = 主導軸

### 已登記的 16 位（13 位已訓練 + 3 位回溯登記 + 選角中四位）

| 角色 | 狀態 | 族裔組 | face_outline | lower_face | chin | jaw_angle | cheekbone | eye_size | eye_axis | eyelid | nose | lips |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| rainie-hsu | 已訓練 | east_asian | oval | medium | narrow_pointed | clean_defined | high_prominent | large | upturned | wide_double | high_straight_narrow | full_cupid |
| nico-tsai | 已訓練 | east_asian | round | short | narrow_pointed | soft_undefined | low_soft | large | level | wide_double | short_upturned_round | small_round |
| iris-chen | 已訓練 | east_asian | round | medium | narrow_pointed | gently_rounded | medium | large | level | wide_double | fine_straight_pointed | full_cupid |
| coco-wu | 已訓練 | east_asian | round | short | small_round | gently_rounded | low_soft | very_large | level | wide_double | short_upturned_round | full_cupid |
| mia-huang | 已訓練 | east_asian | round | medium | small_round | soft_undefined | low_soft | very_large | upturned | wide_double | short_upturned_round | petal_full_small |
| sophia-tseng | 已訓練 | east_asian | oval | medium | small_round | gently_rounded | medium | medium | level | inner_double | fine_straight_pointed | full_cupid |
| vicky-lin | 已訓練 | east_asian | oval | medium | soft_square | clean_defined | high_prominent | large | level | narrow_double | high_straight_narrow | full_cupid |
| yuna-kim | 已訓練 | east_asian | oval | short | narrow_pointed | clean_defined | medium | large | upturned | narrow_double | fine_straight_pointed | petal_full_small |
| luna-tanaka | 已訓練 | east_asian | oval | medium | small_round | soft_undefined | low_soft | large | level | narrow_double | small_flat | petal_full_small |
| ananya-kapoor | 已訓練 | south_asian | oval | medium | narrow_pointed | clean_defined | high_prominent | very_large | level | wide_double | high_straight_narrow | full_cupid |
| aaliya-okonkwo | 已訓練 | black | oval | medium | soft_square | clean_defined | high_prominent | large | level | narrow_double | straight_blunt | full_cupid |
| camille-dupont | 已訓練 | european | long_oval | long | narrow_pointed | clean_defined | high_prominent | medium | downturned | wide_double | high_straight_narrow | thin_flat |
| yerin-han | **選角中** | east_asian | square_long | medium | soft_square | clean_defined | medium | medium | level | inner_double | straight_blunt | wide_thin |
| angeline-kwee | **選角中** | east_asian | long_oval | long | narrow_pointed | gently_rounded | high_prominent | medium | downturned | narrow_double | fine_straight_pointed | thin_flat |
| kanon-komori | **選角中** | east_asian | small_heart | short | narrow_pointed | soft_undefined | low_soft | very_large | downturned | narrow_double | small_flat | petal_full_small |
| wendy-yeo | **選角中** | east_asian | square_long | long | defined_square | angular_square | high_prominent | medium | upturned | single | high_straight_narrow | thin_flat |

### 已訓練角色之間的既成碰撞（改不了，僅供避讓）

這 8 組是**已訓練並在生產環境使用**的角色之間，
骨相距離低於門檻的組合。臉無法回溯修改，登記為既成事實。
**這同時是本 repo 臉部同質化的量化證據。**

| 組合 | 相異軸數 | 其中主導軸 |
|---|---|---|
| rainie-hsu vs vicky-lin | 3 | 2 |
| rainie-hsu vs yuna-kim | 5 | 1 |
| iris-chen vs nico-tsai | 5 | 1 |
| coco-wu vs nico-tsai | 4 | 1 |
| mia-huang vs nico-tsai | 5 | 1 |
| coco-wu vs iris-chen | 5 | 0 |
| vicky-lin vs yuna-kim | 6 | 1 |
| luna-tanaka vs vicky-lin | 5 | 1 |

---

## §7 四位失敗的臉部描述原文

這是實際送進模型、而使用者判定「全部太像」的那四段。

### Yerin Han 한예린（`yerin-han`）

**FACE**：an athletic-looking Korean woman of 26 with a long face built on straight lines: a broad squarish forehead, and a jaw that runs down in a clean straight line to a chin that is squared off rather than pointed. Her cheekbones are moderate and sit flat rather than lifted. Medium-sized eyes set level and wide open, with a narrow inner-fold eyelid crease that shows only as a thin line close to the lashes. A straight nose of ordinary height with a slightly blunt, rounded tip. A wide mouth with thin, evenly shaped lips.

**NEGATIVE**：`NOT a small pointed chin, NOT large upswept cat-like eyes, NOT a deep wide double eyelid crease, NOT full lips with a pronounced cupid's bow, NOT high sculpted cheekbones, NOT a delicate heart-shaped face, NOT a glamour-model face.`

**MARKERS**：a chin that is squared off rather than pointed；a wide mouth relative to the width of her face；an inner-fold eyelid that shows only as a thin crease close to the lashes；a blunt rounded nose tip；a broad flat forehead

### Angeline Kwee 郭慧恩（`angeline-kwee`）

**FACE**：a Chinese-Indonesian woman of 23 with a long narrow face: the distance from her nose to her chin is longer than average, her forehead is high and narrow, and her jawline curves down to a narrow pointed chin in one continuous unbroken line. Her cheekbones are high and read as bone under the skin rather than as soft padding. Medium-sized eyes set closer together than average, the outer corner of each eye sitting slightly lower than the inner corner, which makes her gaze read cool and a little unhurried. A narrow double eyelid crease running close to the lash line. A fine, high, straight nose ending in a small pointed tip. A small mouth with thin lips whose upper edge runs almost straight across.

**NEGATIVE**：`NOT a round face, NOT a short lower face, NOT large round eyes, NOT upswept eyes, NOT a wide deep double eyelid crease, NOT full lips, NOT soft padded cheeks, NOT a baby-faced look.`

**MARKERS**：a long lower face — the distance from her nose to her chin is noticeably longer than average；eyes set closer together than average；outer eye corners that sit lower than the inner corners；an upper lip that runs almost straight across, with the cupid's bow flattened；cheekbones that read as bone under the skin

### Kanon Komori 小森花音（`kanon-komori`）

**FACE**：a very small-faced Japanese woman of 20: her face is a small heart shape — a narrow rounded forehead above wide-set temples, tapering down to a narrow pointed chin, with the lower half of her face very short. The line from her ear to her chin is one continuous soft curve. Her cheekbones sit low and read as soft padding. Very large round eyes whose outer corners droop noticeably downward, with a narrow double eyelid crease close to the lashes. A very small nose whose bridge sits so low it is almost flat, ending in a soft small tip. A small mouth with thick, softly rounded petal-shaped lips.

**NEGATIVE**：`NOT a round face outline, NOT an oval face, NOT a soft rounded chin, NOT level eyes, NOT upswept eyes, NOT a wide deep double eyelid crease, NOT a defined jawline, NOT an upturned nose tip, NOT thin lips.`

**MARKERS**：outer eye corners that droop distinctly downward；a narrow pointed chin below a very short lower face；thick petal-shaped lips on a small mouth；a nose bridge so low it is almost flat；a narrow rounded forehead above wide-set temples

### Wendy Yeo 楊薇伊（`wendy-yeo`）

**FACE**：a Chinese-Singaporean woman of 28 with a striking androgynous face: a long face with a genuinely square jaw — below each ear the corner of the jaw shows as a visible angle, and the chin beneath it is broad and squared off. High prominent cheekbones and a strong straight browbone above the eyes. Medium-sized narrow eyes whose outer corners lift upward, set under a smooth single eyelid: the skin runs unbroken from her lashes up to her brow. A high, narrow, straight nose. A thin mouth with a sharply drawn lip line and level corners.

**NEGATIVE**：`NOT a soft round face, NOT a heart-shaped face, NOT a small pointed chin, NOT large round eyes, NOT a double eyelid crease of any width, NOT full lips, NOT a baby-faced or sweet look, NOT a glamour-model face.`

**MARKERS**：a visible square jaw angle below each ear；a smooth single eyelid, unbroken from lash to brow；narrow eyes whose outer corners lift upward；a sharply drawn lip line on a thin mouth；a long lower face

---

## §8 這個模型的實測行為（`seedream_v4_5`，全部有出圖佐證）

這些是用作廢的圖換來的，**不是文案偏好**。你的規劃必須相容於這些規則。

1. **不執行否定句。** 景別、服裝結構、朝向一律要寫「畫面裡有什麼、邊界切在哪裡」。
   `nothing below the knee is visible` → 無效；
   `the bottom edge of the picture cuts across her thighs` → 有效。
2. **顏色類否定是例外，有效。** `NOT tanned, NOT bronzed` 會被執行。
3. **身體朝向不能寫角度。** `turned about 30 degrees` 連續三次被畫成**背影**。
   要寫「鏡頭看得到哪些身體正面特徵」（肚臍、鎖骨、褲子前面的釦子）。
4. **提到攝影器材就會把器材畫進畫面——即使那句話是在說它在畫面外。**
   `white foam board just out of frame` → 泡棉板被畫出來；
   `the imaging device and whoever holds it beyond the frame edge` → 三腳架單眼入鏡、
   另一隻手拿手機入鏡（等於畫面裡有第二個人）。
5. **光線要寫成房間裡真實存在的表面**（窗、白牆、木地板、軌道燈），
   不能寫器材名稱。五段式：主光／反射面／第二色溫／曝光取捨／遮擋。
6. **構圖模板不得出現姿態動詞。** `She sits centred in the frame` 會把站姿改成坐姿。
7. **Reference Element 在「指定同一件衣服」時會把該件衣服的細節整件複製**；
   髮色的特殊挑染會變成身分的一部分，prompt 蓋不掉。
8. **景別會往鬆的方向漂。** 指定 face_closeup（切在鎖骨下）幾乎必然出成 chest_up。5/5 次。

### 完整 prompt 範例（讓你看清楚臉在整段裡的比重）

這是 `kanon-komori/a01`（臉部特寫、自拍）實際送出去的全文：

```
A vertical photograph of a very small-faced Japanese woman of 20: her face is a small heart shape — a narrow rounded forehead above wide-set temples, tapering down to a narrow pointed chin, with the lower half of her face very short. The line from her ear to her chin is one continuous soft curve. Her cheekbones sit low and read as soft padding. Very large round eyes whose outer corners droop noticeably downward, with a narrow double eyelid crease close to the lashes. A very small nose whose bridge sits so low it is almost flat, ending in a soft small tip. A small mouth with thick, softly rounded petal-shaped lips.
NOT a round face outline, NOT an oval face, NOT a soft rounded chin, NOT level eyes, NOT upswept eyes, NOT a wide deep double eyelid crease, NOT a defined jawline, NOT an upturned nose tip, NOT thin lips.
Her face carries these recognisable features: outer eye corners that droop distinctly downward; a narrow pointed chin below a very short lower face; thick petal-shaped lips on a small mouth; a nose bridge so low it is almost flat; a narrow rounded forehead above wide-set temples.

The bottom edge of the picture sits just below her collarbones. Her face fills most of the frame, from the top of her hair down to the base of her neck. Her shoulders are only barely in the picture; everything below them is outside it.

She has just picked up her phone and is taking a photograph of herself.

Her chest and both shoulders face the camera squarely.
Her head is straight on to the camera.
She looks directly into the lens.
Her expression is relaxed and neutral, mouth closed and soft.
Her whole face is unobstructed.
The picture is what her phone's own front camera sees, taken at arm's length.

Her face is bare: her lips are close to the natural colour of her own mouth, matte, with a soft undefined edge; her eyebrows are soft and natural; her lashes are her own and unmade.
Fair, luminous, porcelain-toned skin with natural tonal variation and visible pores — NOT tanned, NOT bronzed, NOT olive, NOT deep golden or wheat-coloured.
Her neck is short and her shoulders are narrow and sloping, with the collarbone visible where it enters the frame.
Her hair is a pink-lilac gradient: dark at the roots for the first hand's width, then blending down through a dusty lilac into a clear cotton-candy pink at the ends. It is very long, worn down with a loose wave through the lower half.
She is wearing a loose oversized pale pink cotton T-shirt, the neckline stretched wide and soft with wear; a small tortoiseshell claw clip holding a section of hair at the back of her head.

Setting: her small studio flat in Akihabara — a sewing machine on a desk against the wall, folded fabric stacked on the floor, and a whole wall of soft toys on shelves behind her.
Light: afternoon daylight comes through the window on her right and is the main light on her face; the white wall and the pale fabric stacked on the floor throw that light back into the shadow side of her face. At the same time, a small pink night light still switched on behind her left shoulder puts a second, cooler pink colour into that side of the room. Exposure: the camera meters for her face, so the window blows out to flat white. The depth of the shelves behind her falls away into shadow.

Shot on the front camera of a phone, held at arm's length. The slight wide-angle stretch a phone lens gives at close range. Deep depth of field: every visible part of her and the background stay in focus together, and her outline reads sharp against what is behind her.
The picture is straight out of the phone's camera roll, exactly as the sensor recorded it. She is positioned centrally in the frame. There is ordinary everyday clutter in the background. A few highlights are allowed to blow out to white.
Real skin texture with visible pores and fine flyaway hairs. Everything in this picture is accounted for: she is the only person present, and every visible hand connects to one of her own arms. The room holds only the furnishings named above. Illumination comes exclusively from the natural or architectural light sources named above.
```

---

## §9 要你做什麼

### 目標

替 **19 位**設計出**真正會被 `seedream_v4_5` 畫成不同人的臉**。
判準是使用者把任意幾張臉部特寫並排看時，會認為那是不同的人——
不是靠髮色、妝容、服裝分辨，而是**五官本身**。

### 硬限制

1. **人設不能改**：年齡、族裔、身分、身材數字、髮色都是使用者定好的（§5）。
2. **不能像現有 13 位已訓練角色**（§6），尤其不能像 rainie-hsu 那組
   「高顴骨＋銳利下顎＋大而上揚雙眼皮眼＋挺鼻＋厚唇有唇珠」——那是模型的預設臉。
3. **臉必須是 Soul V2 學得起來的**：不能靠極端角度、遮擋、濃妝、特效製造差異，
   因為訓練集要 20 張不同場景，妝髮都會換。差異必須在**骨相**。
4. **不要用會被模型忽略的寫法**（§8）。
5. 全部是**成年女性**（20–28 歲），描述不得使用任何與孩童連結的措辭。

### 我需要你回答的問題

**Q1｜§4 的 H1–H5 哪幾個是真的？** 特別是：臉部描述佔比是不是主因？
「原型」比「特徵清單」有效嗎？加上你自己發現的原因。

**Q2｜選角階段要不要把場景拿掉？**
我的想法是選角先出「純臉」——極簡背景、統一光線、不寫服裝不寫場景，
讓臉佔 prompt 的 80%，確定臉不同之後，再把選中的臉存成錨點帶進有場景的圖。
這樣有效嗎？副作用是什麼（純臉圖當錨點會不會讓後續出圖僵硬）？

**Q3｜19 張臉的差異要建立在哪幾個維度上？**
我這次用的 10 條軸全在「五官形狀」層級，失敗了。是不是該改用更粗、更難忽略的維度？
例如臉的長寬比、骨量（骨感 vs 肉感）、五官密度（集中 vs 分散）、上中下庭比例、
年齡感差距、輪廓的軟硬。**請給出你認為對這個模型真正有效的維度清單，並說明理由。**
同時請回答：19 + 13 = 32 人幾乎全屬東亞，用你提出的維度排得開嗎？
如果排不開，你建議怎麼處理（放寬門檻？接受分群但強化組內差異？建議使用者砍角色？）。

**Q4｜否定清單要不要留？** 如果留，怎麼寫才有作用？

**Q5｜要不要分批？** 19 位一次全部定案，還是先用少數幾位驗證方法有效再推開？
如果分批，先做哪幾位、為什麼。

### 輸出格式（我會直接拿去生成，請嚴格照這個結構）

在 §10 回覆區依序寫：

**(A) 診斷** — H1–H5 的判定 + 你自己發現的原因。400 字內。

**(B) 方法** — 你建議的選角 prompt 結構（臉部佔比、要不要有場景、段落順序）。
如果你認為要改流程（例如先純臉再進場景），在這裡把步驟寫清楚。

**(C) 維度表** — 你提出的骨相維度，以及每個維度的允許值。
格式：`維度名稱 | 允許值1 / 允許值2 / ...  | 為什麼這個維度對這個模型有效`

**(D) 19 張臉** — 每位一段，格式固定，`<persona-id>` 用 §5 表格裡的 id：

```
### <persona-id>
ARCHETYPE: <一句話的臉型原型，中文，「少女短臉型」那種層級>
AXES: <用你 (C) 的維度，逐項給值，分號分隔>
FACE_EN: <要直接送進模型的英文臉部描述，一段連續文字，不要條列>
NEGATIVE_EN: <否定清單；若你判定否定無效就寫 NONE>
MARKERS: <3–5 個辨識特徵，英文，分號分隔；必須是左右翻轉後仍成立的特徵>
WHY_DISTINCT: <中文一句話：這張臉與最接近的那一位、以及與 rainie-hsu 預設臉的關鍵分野>
```

**(E) 驗收方式** — 出圖後怎麼判定這些臉真的不同？
給一個具體可執行的檢查方法（不要「看起來不一樣」這種）。

**(F) 分批建議** — Q5 的答案，明確列出第一批要跑哪幾位。

---

## §10 回覆區

REPLIES BELOW
