TASK-CAL-001／M-3｜12 位人設專業寫真拍攝規劃｜送審報告

# CAL_18 — M-3 12 位人設專業寫真拍攝企劃

> 資料檔：`data/cal_m3_shoot_plan.json`（shoot-plan-v1，2026-10-12）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。
> **僅規劃：沒有生成任何圖片（含測試圖、示意圖），沒有花 credits，沒有訓練，沒有改 canon 或 Soul ID。** 本輪生成數 0、credits 0、訓練數 0。
> 這是企劃，不是核准：每一項都要 Penny 拍板，之後由主管另發執行指令。

## 0. 版本與範圍

| 項目 | 內容 |
|---|---|
| 名單 | roster-v1（docs/calendar/data/cal_m1_owner_roster.json）；不換人，順序不是月份 |
| 素材頁版本 | `b8108eb648a46a57e3bb4dc2158cf878c23d7963` |
| 桌曆基準 | `4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45` |
| Aaliya 圖片來源 | repo `4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45`；型錄分支 `claude/kol-dashboard-catalog-gqw9jz` @ `d3fb91ab87547bfa04ee46cf4cfddd6750fcfe52` |
| 型錄頁 | https://kol-catalog-production.up.railway.app/p/aaliya-okonkwo.html |
| 模型查詢 | 2026-10-12 唯讀查詢 Higgsfield models_explore(get, soul_2)：參數只有 quality（1.5k／2k，預設 2k）、Soul ID、1 張參考圖；比例 1:1、16:9、9:16、4:3、3:4、3:2、2:3；沒有 seed、沒有 negative prompt；回傳沒有價格。與 AI_PROMPT_METHOD_REVIEW.md（2026-09-03）記錄一致。 |

## 1. Penny 喜歡的 4 張（審美參考）

Penny 在第二階段素材頁把下列 4 張列為備選，沒有指定橫式／直式。記錄為 owner 喜歡的既有候選與審美參考；不轉成主照片、不清空瀏覽器裡的選擇。其餘 8 位沒有選中照片，不代表可以套用舊推薦。

| 素材 ID | 照片 | 可借用的特徵 |
|---|---|---|
| iris-04 | Iris｜公園夕陽、白色連帽短上衣＋黑短褲、回頭 | 黃金時段逆光、戶外草地、身形完整的 3/4 身 |
| luna-10 | Luna｜公園夕陽、白色小碎花洋裝、全身 | 柔和暖光、淺色洋裝、乾淨的戶外背景 |
| somi-02 | Somi｜深夜炸雞、握罐甜笑 | 人設本業（吃）＋暖色、笑容、生活感 |
| rin-04 | Rin｜緞面晨袍、回頭背影 | 緞面質感、裸肩回眸、成熟性感 |

四張共同點：光線有方向（夕陽、暖燈）、人物是主角、服裝或材質好看（連帽短上衣、碎花洋裝、緞面）、表情自然；不是手機自拍。這和 Penny 這輪要的「專業寫真質感」一致，企劃直接沿用這些特徵。

## 2. Aaliya 研究

**身分對應：** repo 資料夾名稱是 aaliya-okonkwo，profile.json 的 id 是 aaliya-rivera、姓名 Aaliya Rivera。README.md 註明「資料夾名稱為 aaliya-okonkwo（歷史原因，人格已改為 LA 拉丁裔設定）」。本輪不改人設、不改資料夾。

**來源一致性：** 型錄頁的 12 張圖（catalog/data/selection.json 的 aaliya-okonkwo）＝repo 裡 Aaliya 資料夾的 soul_test_v1 8 張＋face_reference 4 張；三個版本（本分支 HEAD、型錄分支 d3fb91a、素材基準 4fd3995）git blob 逐一相同。

**⚠ Aaliya 的臉不能當其他人設的身分參考。下面只移植拍攝方法：光線、構圖、姿態、服裝材質；不複製她的服裝、場景、燈光組合或 prompt。**

### 2.1 紀錄（有寫的 vs 沒寫的）

- face_reference：generation_notes.md 只記載這 4 張是 Soul 訓練輸入（ref_01–ref_04）；沒有逐張的模型、prompt 或 job。Coco 的 generation_notes.md 轉述初代 6 位（含 Aaliya）的參考圖用 seedream_v4_5——這是轉述，不是 Aaliya 逐張紀錄，列為「推定、未確認」。Soul ID：不適用（這 4 張是訓練前的輸入）。
- soul_test_v1：generation_notes.md「訓練後測試生成（2026-06-29）」：明寫「生成記錄遺失：未即時記錄 Job ID 和 prompt」。章節位置與 Usage 範例（soul_2＋該人設的 Soul ID）推定為 soul_2＋該 Soul ID，但逐張未確認；quality、aspect_ratio 都沒有紀錄。
- 後製／中繼資料：檔案沒有 EXIF、PNG 文字區塊或其他中繼資料；repo 是淺層 clone，加入這些檔案的 commit 不在可見歷史內。沒有任何紀錄提到後製、裁切或增強——「沒有紀錄」不等於「沒有做」，列為未知。

### 2.2 入選 5 張的證據表

| # | 檔案（repo 路徑） | 尺寸 | 類別 | 模型 | 原始 prompt | Soul ID | 後製／裁切／增強 | 拍攝形式（目視） |
|---|---|---|---|---|---|---|---|---|
| 1 | `kols/aaliya-okonkwo/images/face_reference/ref_02.webp` | 1728×2304 | face_reference（Soul 訓練輸入） | 未逐張記錄（推定 seedream_v4_5，依他人筆記轉述，未確認） | 未知（無紀錄） | 不適用（訓練前） | 未知 | 黃金時段逆光・斜倚 3/4 身 |
| 2 | `kols/aaliya-okonkwo/images/face_reference/ref_03.webp` | 1728×2304 | face_reference（Soul 訓練輸入） | 未逐張記錄（同上，推定、未確認） | 未知（無紀錄） | 不適用（訓練前） | 未知 | 側光・插腰站姿 3/4 身 |
| 3 | `kols/aaliya-okonkwo/images/soul_test_v1/restaurant_02.png` | 1152×2048 | soul_test_v1（Soul 訓練後測試） | 推定 soul_2＋該 Soul ID（紀錄遺失，未確認） | 未知（紀錄明寫遺失） | 推定使用，未確認 | 未知 | 夜間室內暖燈・坐姿 3/4 身 |
| 4 | `kols/aaliya-okonkwo/images/soul_test_v1/poolside_02_v1.png` | 1152×2048 | soul_test_v1（Soul 訓練後測試） | 推定 soul_2＋該 Soul ID（紀錄遺失，未確認） | 未知（紀錄明寫遺失） | 推定使用，未確認 | 未知 | 戶外硬光・全身正面站姿 |
| 5 | `kols/aaliya-okonkwo/images/soul_test_v1/poolside_02_v2.png` | 1152×2048 | soul_test_v1（Soul 訓練後測試） | 推定 soul_2＋該 Soul ID（紀錄遺失，未確認） | 未知（紀錄明寫遺失） | 推定使用，未確認 | 未知 | 坐姿・遠景城市留白 |

「尺寸」是本輪讀檔所得（實測）；「模型／prompt／Soul ID／後製」只照錄紀錄，紀錄沒有的寫「未知」或「推定」。

### 2.3 目視觀察（不是紀錄）

1. **黃金時段逆光・斜倚 3/4 身**：太陽在她身後斜上方，頭髮與肩線有一圈暖色輪廓光；臉部靠前方的環境反光補亮，沒有死黑；背景是失焦的綠樹與天空，只有一個主體；身體斜倚形成對角線；服裝單純（素色短 T＋牛仔褲），讓身形與光線成為重點。
2. **側光・插腰站姿 3/4 身**：低角度暖陽從側面打來，臉的受光面清楚、陰影面柔和；一手插腰、身體 3/4 側、重心在後腳——典型顯身形的站姿；背景樹叢失焦，地面與天空都乾淨。
3. **夜間室內暖燈・坐姿 3/4 身**：光源是畫面裡看得到的暖色串燈，背景整片暖色散景、遠處較暗；貼身針織洋裝的材質與曲線清楚；坐在木椅上、身體微側，一手放在腿上；直視鏡頭、表情收斂——是「拍照」的姿態，不是隨拍。
4. **戶外硬光・全身正面站姿**：晴天高角度陽光，泳池水面把青綠色反光打回腿與身體下側；全身置中、腳在畫面下緣、上方留天空——全身照沒有變形；長版針織罩衫垂到小腿，拉長身形線條；背景只有棕櫚樹與泳池，沒有人。
5. **坐姿・遠景城市留白**：人物只占畫面約三分之一，大片城市遠景與天空當留白——這種構圖最容易改成橫式；坐在池邊、雙腿入水，身體形成 S 形；白天柔和的自然光；缺點：人物偏小，臉的細節不足，桌曆用要更靠近。

未採用：自拍 2 張（selfie_01／02）是手機自拍角度，正是 Penny 這輪要避免的形式，不列為參考；restaurant_01、poolside_01_v1／v2 與入選的同場景，不重複列。

### 2.4 可移植的方法（移植方法，不複製內容）

| 項目 | 做法 |
|---|---|
| 主光／補光 | 主光要有名字和方向（夕陽在身後左上、窗在右側、吊燈在前右）；補光來自畫面裡看得到的反射面（淺色地面、白牆、泳池水、亮面磁磚）。臉必須是畫面最亮的區域之一，背後的光只當輪廓光。 |
| 背景層次 | 前景乾淨、主體清楚、背景失焦（85mm 左右、遠距離）。場景寫「有什麼」而不是「沒有什麼」：例如「草地與小徑空無一人」。 |
| 人物比例 | 全身／3/4 身用 70–85mm、相機在肚臍高度、拍攝距離 3–5 公尺；腳在下 1/3，頭上留白。避免低角度仰拍。 |
| 服裝材質 | 每位寫滿五層（上身、下身、鞋、外套或包、首飾髮飾），具體到材質與顏色；至少一件會在風裡或動作中飄動的東西。 |
| 表情 | 先給一個有名字的表情（回眸一笑、眨眼、月牙眼大笑、收斂的半笑），再寫視線；表情與姿勢寫成同一個連續動作。 |
| 姿態 | 寫清楚重心在哪隻腳、兩手各在哪、上身與骨盆是否扭轉；不只寫「站著」「回頭」。 |
| 鏡頭感 | 他拍、全片幅相機、指定焦段與距離；不寫手機前鏡頭、不寫自拍。 |
| 色彩與皮膚 | 每張兩個色溫（暖陽對冷陰影、暖燈對冷窗光）；皮膚寫毛孔與自然質感，臺灣與東亞人設維持白皙膚色基調。 |

## 3. 12 位差異總表

| 人設 | 企劃名稱 | 時段 | 光線 | 配色 | 場景 | 服裝類型 | 姿勢 | 表情 | 取景 | 首批 |
|---|---|---|---|---|---|---|---|---|---|---|
| Iris Chen（陳芯語，22） | 河濱草地的黃金時段 | 傍晚 | 戶外逆光（夕陽輪廓光＋步道反光） | 米白・淺藍・暖橘 | 河濱草地 | 平口短上衣＋牛仔短褲＋開襟 | 走向鏡頭時回頭 | 回頭張口大笑 | 大腿以上 | 是 |
| Luna Tanaka（田中ひな，20） | 京都老宅後院的紫陽花 | 白天（陰天） | 大面積柔光＋葉縫光斑 | 鼠尾草綠・白 | 町家後院紫陽花 | 蕾絲迷你洋裝 | 站姿、按住被風吹的裙襬 | 垂眼後抬眼的安靜微笑 | 膝上 |  |
| Somi Oh（오소미，24） | 暖橘色的復古小吃店棚景 | 棚內 | 暖鎢絲主光＋磁磚反光 | 暖橘・紅・奶油 | 復古小吃店棚景 | 短版針織＋格紋百褶迷你裙 | 側坐高腳椅、舉炸雞 | 月牙眼大笑、酒窩 | 膝上 |  |
| Coco Wu（吳可可，20） | 週末飯店泳池的薄荷綠 | 上午 | 晴天高光＋池水反光 | 薄荷綠・淺紫・湖水綠 | 飯店泳池 | 比基尼＋透膚罩衫 | 池邊坐姿、踢水 | 歪頭瞇眼大笑、酒窩 | 全身坐姿 |  |
| Mia Huang（黃米亞，22） | 粉紫霓虹的電競時尚棚 | 棚內 | 中性柔光箱主光＋霓虹輪廓 | 洋紅・紫・黑 | 電競棚景 | 短版帽 T＋背心＋短褲＋過膝襪 | 電競椅上勾腿側坐 | 眨眼、挑逗半笑 | 全身坐姿 | 是 |
| Yuna Kim（김하은，21） | 首爾公寓的極簡窗光 | 早晨 | 紗簾漫射窗光（冷白） | 冷白・柔灰・象牙 | 極簡白色公寓 | 針織開襟＋緞面中長裙 | 窗邊長凳側坐 | 平靜淺笑 | 膝上 |  |
| Tammy Chou（周語彤，24） | 都會白色建築的熱粉色洋裝（型錄外拍） | 晴天白天 | 硬光＋白牆反光 | 熱粉・白・藍灰 | 白色建築階梯 | 貼身針織迷你洋裝＋高跟鞋 | 走下階梯、插腰撥髮 | 明亮露齒笑 | 全身 |  |
| Rin Ayase（綾瀨凜，25） | 黎明公寓的祖母綠緞袍 | 黎明 | 冷色窗光＋暖色檯燈 | 祖母綠・金・象牙 | 高樓公寓臥室 | 緞面晨袍 | 背影 3/4、越肩回眸 | 心照不宣的半笑 | 大腿以上 | 是 |
| Rainie Hsu（許雷妮，24） | 頂樓夜景的血紅緞面馬甲洋裝 | 夜晚 | 大面積明亮主光＋城市散景 | 血紅・黑・銀・深藍 | 頂樓露台 | 緞面馬甲高衩迷你洋裝 | 背靠欄杆、撥髮 | 直視、自信壞笑 | 膝上 |  |
| Miu Shiraishi（白石美羽，22） | 開店前的奶油色咖啡館 | 早晨 | 低角度暖色直射窗光 | 奶油・橡木・淺棕 | 開店前咖啡館 | 露肩粗針織＋麂皮短裙＋圍裙 | 吧台後正面捧杯 | 歪頭柔和甜笑 | 腰上 | 是 |
| Jia Seo（서지아，22） | 灰色無縫棚的舞者時尚 | 棚內 | 冷白柔光箱＋背後條燈輪廓 | 黑・灰・木色・薄荷綠 | 灰色無縫棚 | 單肩連身衣＋透膚襯衫＋寬褲 | 舞蹈動作停格 | 冷靜自信半笑 | 全身 |  |
| Yerin Han（한예린，26） | 清晨霧中的球道 | 清晨 | 晨光逆光＋霧與草地補光 | 天空藍・白・草綠 | 高爾夫球道 | 無袖針織 polo＋百褶短裙＋球帽 | 球桿橫掛肩後 | 大方明亮的笑 | 全身 |  |

**仍然接近、需要 Penny 判斷的地方（不宣稱已消除）：**

- 早晨窗光有三位：Yuna（冷白漫射、極簡、正面坐姿）、Miu（暖色直射、咖啡館木頭、捧杯）、Rin（黎明冷光＋暖燈、暗色、背影回眸）。光的方向與色溫不同，但都是「窗邊」；若 Penny 覺得太接近，可把其中一位改用替代方向。
- 開懷大笑有五位：Iris、Somi、Coco、Tammy、Yerin（各自的人設都是外向、愛笑）。用不同動作綁在一起（回頭、咬前停頓、踢水、走下階梯、球桿掛肩），但整本來看笑的比例偏高；安靜或挑逗表情的有 Luna、Yuna、Rin、Rainie、Mia、Miu、Jia。
- 棚拍有三位：Somi（暖橘搭景）、Mia（霓虹電競）、Jia（灰色無縫）。色彩與道具完全不同。
- 碰撞配對（Miu–Jia、Miu–Somi、Jia–Somi、Yerin–Rin）與 R2 目視相似（Somi–Tammy、Iris–Rainie）：只用拍攝調性拉開，不改臉、不換人；不宣稱調性差異能消除碰撞。每張照片只有一位，不違反 C-2 同框規則；封面或拼貼若要放 12 人，另案處理。

## 4. 每位企劃

每位一個主推薦、一個替代方向。「參考照片」是第二階段素材頁既有的照片 ID，只用來認人與看氣質，**不是新成品、不會照抄**；新企劃的照片**尚未生成**。
prompt 是可直接使用的草稿，**尚未執行**；兩段（橫／直）只差取景句。

### 4.1 Iris Chen（陳芯語，22）｜河濱草地的黃金時段（首批建議）

- **與人設核對：** 主管方向「金色戶外、短上衣＋短褲、自然甜笑」與人設一致（台北 It Girl、平口與短上衣、台北午後自然光），也正是 Penny 喜歡的 iris-04。不調整。
- **為什麼適合她：** 她的魅力是「不費力的好看」：台北午後的陽光、隨手穿的平口上衣與牛仔短褲。把 iris-04 的感覺拍成正式寫真，而不是換成另一種人。
- **參考照片（既有）：** iris-04、iris-03

| 項目 | 內容 |
|---|---|
| 場景 | 台北河濱公園的開闊草地，傍晚太陽低，遠處一排柔綠樹與低矮公寓，草地與小徑空無一人。 |
| 服裝 | 米白羅紋平口短上衣、淺藍刷色高腰牛仔短褲（毛邊）、燕麥色薄針織開襟滑落一側肩、白色低筒帆布鞋。 |
| 髮型／髮色 | 黑色柔順直髮自然垂放過肩，幾縷被風吹起。 |
| 配件 | 小金色圈耳環。 |
| 光線（主光／補光） | 主光：低角度夕陽在她身後左上，頭髮與肩線一圈暖橘輪廓光。補光：她前方的淺色水泥步道把暖光反回臉上，臉保持畫面最亮。 |
| 背景與色彩 | 遠景樹與天空失焦；兩個色溫：背上暖橘陽光對樹蔭裡的冷藍綠。測光給臉，太陽旁的天空允許過曝。 |
| 表情與視線 | 走向鏡頭時回頭，自然張口大笑；視線看鏡頭。 |
| 姿勢與雙手 | 前腳往前一步、重心在後腳，回頭時上身扭轉；右手把頭髮塞到耳後，左手自然垂放；針織外套下襬隨轉身擺動。 |
| 橫構圖 | 3:2，85mm、約 4 公尺、相機在肚臍高度；大腿中段以上，人物在左三分線，右側是暖光草地。 |
| 直構圖 | 3:4，同機位；大腿中段以上置中，頭頂留白。 |
| 甜美元素 | 大笑與回頭的動作、陽光、米白與淺藍的乾淨配色。 |
| 性感元素 | 平口上衣露肩、露出腰線與長腿；外套滑落一側肩。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：頭頂留白，臉不進線圈區。身形：大腿中段以上，橫直都保得住。日期區：橫式右側草地、直式下方草地可放小月曆。 |
| 替代方向 | 午後窗光的白色公寓：米白針織小可愛＋牛仔迷你裙，坐在窗邊木地板上，側逆光，甜而慵懶（她的「私下」支柱）。 |

| 風險 | 處理 |
|---|---|
| 逆光導致臉暗 | 寫明前方步道反光補光、測光給臉、「臉是最亮區域之一」 |
| 黃金光把膚色拍成小麥色 | 寫明白皙膚色基調（臺灣籍角色規則） |
| 塞頭髮的手指融合 | 生成後放大檢查手；不行就改成手扶開襟外套 |
| 太陽眩光蓋住臉 | 太陽放在左上、臉在右側 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 22-year-old adult Taiwanese woman with fair, luminous porcelain-toned skin and black silky straight hair worn down past her shoulders, a few strands lifting in the breeze. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, full chest and slim waist. She wears an off-white fitted ribbed tube top, high-waisted faded light-blue denim shorts with a frayed hem, a thin oatmeal knit cardigan slipping off one shoulder and swinging as she turns, white low canvas sneakers and small gold hoop earrings. Setting: an open riverside lawn in a Taipei park at late afternoon, a line of soft green trees and low distant apartment blocks far behind her, the grass and the path empty and clean. She walks toward the camera with her weight on the back foot as the front foot steps forward, turns her head back over her shoulder and breaks into a natural open-mouthed laugh, right hand tucking hair behind her ear, left hand loose at her side. Horizontal 3:2 frame shot on a full-frame camera with an 85mm lens from about four metres, camera at her navel height, framed from mid-thigh up and placed on the left third, the warm lawn and soft out-of-focus trees filling the right two thirds, generous space above her head. Lighting: the low sun sits behind her and to the upper left, painting a warm orange rim along her hair and shoulder line; the pale concrete path in front of her bounces soft warm light back onto her face, so her face stays one of the brightest areas of the frame; warm amber sunlight on her back against cool blue-green shade under the trees; exposure is metered for her face, so the sky beside the sun clips to white and the far trees fall slightly dark. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 22-year-old adult Taiwanese woman with fair, luminous porcelain-toned skin and black silky straight hair worn down past her shoulders, a few strands lifting in the breeze. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, full chest and slim waist. She wears an off-white fitted ribbed tube top, high-waisted faded light-blue denim shorts with a frayed hem, a thin oatmeal knit cardigan slipping off one shoulder and swinging as she turns, white low canvas sneakers and small gold hoop earrings. Setting: an open riverside lawn in a Taipei park at late afternoon, a line of soft green trees and low distant apartment blocks far behind her, the grass and the path empty and clean. She walks toward the camera with her weight on the back foot as the front foot steps forward, turns her head back over her shoulder and breaks into a natural open-mouthed laugh, right hand tucking hair behind her ear, left hand loose at her side. Vertical 3:4 frame shot on a full-frame camera with an 85mm lens from about four metres, camera at her navel height, framed from mid-thigh up and centred, clear space above her head and soft lawn below her. Lighting: the low sun sits behind her and to the upper left, painting a warm orange rim along her hair and shoulder line; the pale concrete path in front of her bounces soft warm light back onto her face, so her face stays one of the brightest areas of the frame; warm amber sunlight on her back against cool blue-green shade under the trees; exposure is metered for her face, so the sky beside the sun clips to white and the far trees fall slightly dark. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.2 Luna Tanaka（田中ひな，20）｜京都老宅後院的紫陽花

- **與人設核對：** 主管方向「花園清新、淺色小洋裝、柔和日光」與人設一致（京都、白蕾絲與碎花、柔焦窗光）。調整：她 20 歲、童顏，花園＋小洋裝容易顯小。改用合身腰線、低跟涼鞋、細金項鍊等成人線索；不用白襪、瑪莉珍鞋、泡泡袖娃娃裝。
- **為什麼適合她：** 她是「住在美麗白日夢裡的人」：安靜、會注意光線。用老宅庭院的柔光與淺色蕾絲，把 luna-10 的清新感拍得更講究，同時維持成人的線條。
- **參考照片（既有）：** luna-10、luna-01

| 項目 | 內容 |
|---|---|
| 場景 | 京都風老木造町家的後院：青苔地、石板小徑、低矮木籬笆旁一整排白色紫陽花，頭上有楓樹枝。 |
| 服裝 | 淺鼠尾草綠棉質蕾絲迷你洋裝（方領、短袖、合身腰線，裙襬被風微微掀起）、米色低跟繫帶涼鞋。 |
| 髮型／髮色 | 黑色細直髮，中分下巴長度的鮑伯，髮尾貼著下顎。 |
| 配件 | 細金鍊項鍊、耳上一支珍珠髮夾。 |
| 光線（主光／補光） | 主光：明亮陰天的大面積柔光從前上方；楓葉縫隙在肩上與小徑留下斑駁光點。補光：白紫陽花與淺色石板把柔和中性光反回臉上。 |
| 背景與色彩 | 庭院深處是冷綠色陰影，對比暖一點的膚色；測光給臉，葉縫裡的天空柔和過曝。 |
| 表情與視線 | 先垂眼，再抬眼看鏡頭，帶一點安靜的微笑。 |
| 姿勢與雙手 | 站在石板路上，重心在右腳、左膝微彎；一手輕按大腿處的裙襬（風在吹），另一手放在鎖骨。 |
| 橫構圖 | 3:2，85mm、約 4 公尺、肚臍高度；膝上，人物在右三分線，左側是紫陽花小徑引導線。 |
| 直構圖 | 3:4，同機位；膝上置中，上緣有楓樹枝、頭頂留白。 |
| 甜美元素 | 垂眼後抬眼的安靜笑、淺綠與白色、花。 |
| 性感元素 | 方領與合身腰線、她的身材比例（童顏與曲線的反差）、被風掀起又被按住的裙襬。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：短髮、頭頂留白容易保住。身形：膝上。日期區：橫式左側小徑、直式下方石板可放小月曆。 |
| 替代方向 | 雨後的木造緣側：白色蕾絲細肩睡裙＋薄針織外套，坐在木廊邊、腳垂向庭院，晨間柔光（她的「早晨」支柱）。 |

| 風險 | 處理 |
|---|---|
| 童顏＋花園＋小洋裝顯得未成年 | 寫明 adult、合身腰線、低跟涼鞋與首飾；不用白襪與娃娃裝元素（全體不可鬆動的界線） |
| 裙襬被風掀起造成走光 | 寫明手按住裙襬、裙襬只微微掀起 |
| 斑駁光點落在臉上變成花臉 | 寫明光點在肩與小徑，臉在柔和的開放陰影裡 |
| 地名寫「京都」生出錯的地標 | 只寫環境元素（町家木造、青苔、石燈），不點名地標 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 20-year-old adult Japanese woman with fair, luminous skin and black fine straight hair in a centre-parted, chin-length bob, the ends brushing her jaw. Petite curvy figure, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup, full chest and slim waist. She wears a pale sage-green cotton lace mini dress with a square neckline, short sleeves and a fitted waist, the skirt hem lifting slightly in a breeze, cream low block-heel strappy sandals, a thin gold chain necklace and a pearl hair pin above one ear. Setting: a quiet garden behind an old wooden Kyoto-style townhouse, moss ground, a stone path, white hydrangeas in bloom along a low wooden fence, maple branches overhead. She stands on the stone path with her weight on her right leg and the left knee softly bent, one hand lightly holding the skirt at her thigh as the wind lifts it, the other hand resting at her collarbone; her eyes lower, then lift to the camera with a small, quiet smile. Horizontal 3:2 frame shot on a full-frame camera with an 85mm lens from about four metres, camera at her navel height, framed from the knees up and placed on the right third, the hydrangea-lined path leading in from the left, clear space above her head. Lighting: a bright overcast sky acts as one huge soft source from above and in front, dappled spots of light through the maple leaves fall across her shoulders and the path while her face stays in soft open shade; the white hydrangeas and pale stone path bounce soft neutral light onto her face, keeping it the brightest part of the frame; cool green shade deeper in the garden against her warmer skin; exposure is set for her face, so the sky gaps between the leaves clip softly. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 20-year-old adult Japanese woman with fair, luminous skin and black fine straight hair in a centre-parted, chin-length bob, the ends brushing her jaw. Petite curvy figure, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup, full chest and slim waist. She wears a pale sage-green cotton lace mini dress with a square neckline, short sleeves and a fitted waist, the skirt hem lifting slightly in a breeze, cream low block-heel strappy sandals, a thin gold chain necklace and a pearl hair pin above one ear. Setting: a quiet garden behind an old wooden Kyoto-style townhouse, moss ground, a stone path, white hydrangeas in bloom along a low wooden fence, maple branches overhead. She stands on the stone path with her weight on her right leg and the left knee softly bent, one hand lightly holding the skirt at her thigh as the wind lifts it, the other hand resting at her collarbone; her eyes lower, then lift to the camera with a small, quiet smile. Vertical 3:4 frame shot on a full-frame camera with an 85mm lens from about four metres, camera at her navel height, framed from the knees up and centred, maple branches across the top edge and clear space above her head. Lighting: a bright overcast sky acts as one huge soft source from above and in front, dappled spots of light through the maple leaves fall across her shoulders and the path while her face stays in soft open shade; the white hydrangeas and pale stone path bounce soft neutral light onto her face, keeping it the brightest part of the frame; cool green shade deeper in the garden against her warmer skin; exposure is set for her face, so the sky gaps between the leaves clip softly. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.3 Somi Oh（오소미，24）｜暖橘色的復古小吃店棚景

- **與人設核對：** 主管方向「暖色復古棚拍、針織＋高腰短裙、活潑表情」與人設部分衝突：Somi 的身分是吃播（海鮮市場、路邊攤、深夜炸雞），純棚拍會失去人設；Penny 喜歡的 somi-02 也是炸雞。調整：保留「暖色復古棚」，但把棚景做成乾淨的復古小吃店，手上拿食物。另外避開格紋裙＋白襪＋樂福鞋的學生感。
- **為什麼適合她：** 她「吃得比誰都香」。在搭好的乾淨棚景裡拿著炸雞大笑，同時保留食物、暖色與市場的熱度，又是受控的專業打光。
- **參考照片（既有）：** somi-02、somi-01

| 項目 | 內容 |
|---|---|
| 場景 | 搭景的韓式復古小吃店：暖橘色磁磚吧台、一排紅色皮面高腳椅、身後玻璃櫃裡擺著金黃炸雞，所有東西整齊。 |
| 服裝 | 奶油色麻花針織短版開襟（扣到胸前）、高腰焦橘紅格紋百褶迷你裙、光腿、棕色皮質低跟樂福鞋（有跟、不配白襪）。 |
| 髮型／髮色 | 明亮蜜橘棕的韓式狼尾層次剪，一側撥到耳後（她的招牌鏡頭）。 |
| 配件 | 紅色琺瑯小愛心耳環。 |
| 光線（主光／補光） | 主光：大面積暖鎢絲燈從前右、頭部高度，臉最亮；吧台上方吊燈在頭髮上加一點光。補光：亮面橘色磁磚把暖光反到臉的陰影面。 |
| 背景與色彩 | 吧台與高腳椅是暖琥珀色，後牆是偏冷的藍綠灰；測光給臉，吊燈燈泡過曝、角落柔和變暗。 |
| 表情與視線 | 月牙眼大笑、露出酒窩，咬下去前的停頓（嘴裡沒有食物）。 |
| 姿勢與雙手 | 側坐高腳椅、雙腿在膝上交疊，一手肘靠在吧台；另一手把一隻炸雞腿舉在臉頰旁；百褶裙在椅面上散開。 |
| 橫構圖 | 3:2，70mm、約 3 公尺、肚臍高度；膝上，人物在左三分線，右側延伸暖色吧台與發光的玻璃櫃。 |
| 直構圖 | 3:4，同機位；膝上置中，吊燈剛好在上緣內，頭頂留白。 |
| 甜美元素 | 月牙眼與酒窩的大笑、舉著炸雞的俏皮。 |
| 性感元素 | 短版針織露出腰線、交疊的腿與迷你裙、她的曲線身材。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：吊燈在頭頂上方，人物要往下一點，確保頭頂不進線圈區。身形：膝上。日期區：橫式右側吧台、直式下方吧台面。 |
| 替代方向 | 釜山港邊的黃昏碼頭：白色寬襯衫在腰間打結＋牛仔短褲，坐在碼頭繫纜樁旁，手拿一串魚板，夕陽逆光（她的「美食遠征」支柱）。 |

| 風險 | 處理 |
|---|---|
| 吃東西時嘴型與食物變形 | 寫「咬下去前的停頓」，嘴裡沒有食物 |
| 格紋裙＋白襪＋樂福鞋像學生制服 | 改光腿與有跟樂福鞋、成熟的針織 |
| 櫃子或包裝出現假字 | 炸雞直接放在玻璃櫃的盤子上，不寫包裝、招牌、菜單 |
| 與 Miu、Jia 的碰撞紀錄 | 用暖橘高飽和、吃播道具、蜜橘狼尾拉開差異；不改臉，也不宣稱差異能消除碰撞 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 24-year-old adult Korean woman with fair, luminous porcelain-toned skin and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut with one side tucked behind her ear. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a cream cable-knit cropped cardigan buttoned to the chest, a high-waisted burnt-orange and red tartan pleated mini skirt, bare legs, brown leather heeled loafers and small red enamel heart earrings. Setting: a studio-built retro Korean snack-bar set with a warm orange tiled counter, a row of red vinyl bar stools and a glass display of golden fried chicken on plates behind her, everything tidy and evenly arranged. She sits sideways on a bar stool with her legs crossed at the knee, one elbow leaning on the counter, holding a crispy fried chicken drumstick up beside her cheek and laughing with her eyes curved into crescents and dimples showing, pausing just before a bite, the pleated skirt fanning over the stool. Horizontal 3:2 frame shot on a full-frame camera with a 70mm lens from about three metres, camera at her navel height, framed from the knees up and placed on the left third, the warm counter and glowing display stretching to the right. Lighting: a large warm tungsten key from the front right at head height lights her face as the brightest area, a warm pendant lamp above the counter adds a glow on her hair, and the glossy orange tiles bounce warm orange fill onto the shadow side of her face; the counter and stools glow warm amber against a cooler teal-grey back wall; exposure is set for her face, so the lamp bulb clips and the far corners fall into soft shadow. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 24-year-old adult Korean woman with fair, luminous porcelain-toned skin and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut with one side tucked behind her ear. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a cream cable-knit cropped cardigan buttoned to the chest, a high-waisted burnt-orange and red tartan pleated mini skirt, bare legs, brown leather heeled loafers and small red enamel heart earrings. Setting: a studio-built retro Korean snack-bar set with a warm orange tiled counter, a row of red vinyl bar stools and a glass display of golden fried chicken on plates behind her, everything tidy and evenly arranged. She sits sideways on a bar stool with her legs crossed at the knee, one elbow leaning on the counter, holding a crispy fried chicken drumstick up beside her cheek and laughing with her eyes curved into crescents and dimples showing, pausing just before a bite, the pleated skirt fanning over the stool. Vertical 3:4 frame shot on a full-frame camera with a 70mm lens from about three metres, camera at her navel height, framed from the knees up and centred, the pendant lamp just inside the top edge and space above her head. Lighting: a large warm tungsten key from the front right at head height lights her face as the brightest area, a warm pendant lamp above the counter adds a glow on her hair, and the glossy orange tiles bounce warm orange fill onto the shadow side of her face; the counter and stools glow warm amber against a cooler teal-grey back wall; exposure is set for her face, so the lamp bulb clips and the far corners fall into soft shadow. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.4 Coco Wu（吳可可，20）｜週末飯店泳池的薄荷綠

- **與人設核對：** 主管方向「夏日泳池、泳裝＋罩衫、清透水光」可以成立：她的支柱有「旅遊／週末出遊」，配色是薄荷綠、嬰兒粉、淺紫。風險：她 20 歲、人設是大學生——不用任何校園或制服元素，寫明成人。
- **為什麼適合她：** 她的魅力是「對自己柔軟曲線毫不設防的自在」與大笑。週末出遊的泳池，配上她的薄荷綠與淺紫，清透、甜、會笑。
- **參考照片（既有）：** coco-21、coco-08

| 項目 | 內容 |
|---|---|
| 場景 | 週末早上的度假飯店泳池：淺米色石材地磚、清澈的湖水綠池水、遠處收起的白色陽傘，池畔乾淨無人。 |
| 服裝 | 薄荷綠羅紋三角比基尼上衣與同色側綁下著、敞開的淺紫透膚短袖罩衫（滑落雙肩）、腳踝細金鍊。 |
| 髮型／髮色 | 深棕長波浪捲髮、蓬鬆空氣瀏海，髮尾微濕。 |
| 配件 | 白色雛菊髮夾。 |
| 光線（主光／補光） | 主光：晚上午的陽光從左前上方。補光：湖水綠池水把冷綠反光與波紋光斑打在腿與手臂下側，淺色地磚把白光補到臉上，臉亮而均勻。 |
| 背景與色彩 | 暖色日照的皮膚對比冷色池水；測光給臉，水面閃光允許過曝。 |
| 表情與視線 | 歪頭、瞇成一條線的大笑、露出酒窩。 |
| 姿勢與雙手 | 坐在池邊、兩條小腿泡在水裡，身體往後用雙手撐地；一腳踢水濺起水花；透膚罩衫被風掀起。 |
| 橫構圖 | 3:2，70mm、約 3 公尺、相機在她坐姿的胸口高度；全身坐姿，人物在左三分線，右側是開闊池面。 |
| 直構圖 | 3:4，同機位；全身坐姿置中，下方是池水。 |
| 甜美元素 | 瞇眼大笑、酒窩、雛菊髮夾、粉嫩配色。 |
| 性感元素 | 比基尼與透膚罩衫、往後撐的姿勢展現曲線、濕髮與水光。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：坐姿人物位置低，頭頂留白充足。身形：全身坐姿，腳在水裡不必完整。日期區：橫式右側池面、直式下方水面。 |
| 替代方向 | 清晨的乾淨房間：奶油白針織開襟＋淺紫細肩小可愛＋百褶迷你裙，坐在床邊，窗光（她的「私下」支柱，但背景整理乾淨、不是宿舍雜亂感）。 |

| 風險 | 處理 |
|---|---|
| 泳裝遮蔽與走光 | 寫明比基尼完整遮蔽、坐姿；生成後逐張檢查，比照第二階段的遮蔽規則 |
| 水下腳掌與手指變形 | 小腿入水、腳掌不必看清；檢查撐地的手 |
| 校園甜心＋泳裝顯小 | 寫明 adult、不用校園元素，配飾選成人款 |
| 湖水綠反光讓膚色發綠 | 寫明淺色地磚的白色補光打在臉上 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 20-year-old adult Taiwanese woman with fair, luminous porcelain-toned skin, deep dimples when she smiles and dark-brown long wavy hair with soft wispy bangs, the ends slightly wet. Petite curvy figure, 158 cm tall, bust 89 cm, waist 56 cm, hips 86 cm, E cup, full chest and slim waist. She wears a mint-green ribbed triangle bikini top with matching side-tie bottoms that fully cover, an open sheer lilac short-sleeve cover-up shirt slipping off her shoulders, a white daisy hair clip and a thin gold anklet. Setting: a resort hotel pool on a weekend morning, pale cream stone tiles, clear turquoise water and white umbrellas folded in the distance, the pool deck clean and empty. She sits on the pool edge with both lower legs in the water, leaning back on her hands, kicking one foot so water splashes up, head tilted, laughing with her eyes squeezed into crescents and dimples showing, the sheer shirt lifting in the breeze. Horizontal 3:2 frame shot on a full-frame camera with a 70mm lens from about three metres, camera at her seated chest height, framed full body seated and placed on the left third, the open turquoise pool filling the right side. Lighting: bright late-morning sun from high front-left; the turquoise water bounces cool aqua light and moving caustic patterns onto her legs and the underside of her arms, while the pale tiles throw a soft white fill up onto her face so her face is evenly bright; warm sunlit skin against the cool aqua water; exposure is metered for her face, so the sparkles on the water clip to white. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 20-year-old adult Taiwanese woman with fair, luminous porcelain-toned skin, deep dimples when she smiles and dark-brown long wavy hair with soft wispy bangs, the ends slightly wet. Petite curvy figure, 158 cm tall, bust 89 cm, waist 56 cm, hips 86 cm, E cup, full chest and slim waist. She wears a mint-green ribbed triangle bikini top with matching side-tie bottoms that fully cover, an open sheer lilac short-sleeve cover-up shirt slipping off her shoulders, a white daisy hair clip and a thin gold anklet. Setting: a resort hotel pool on a weekend morning, pale cream stone tiles, clear turquoise water and white umbrellas folded in the distance, the pool deck clean and empty. She sits on the pool edge with both lower legs in the water, leaning back on her hands, kicking one foot so water splashes up, head tilted, laughing with her eyes squeezed into crescents and dimples showing, the sheer shirt lifting in the breeze. Vertical 3:4 frame shot on a full-frame camera with a 70mm lens from about three metres, camera at her seated chest height, framed full body seated and centred, the pool water filling the lower part of the frame. Lighting: bright late-morning sun from high front-left; the turquoise water bounces cool aqua light and moving caustic patterns onto her legs and the underside of her arms, while the pale tiles throw a soft white fill up onto her face so her face is evenly bright; warm sunlit skin against the cool aqua water; exposure is metered for her face, so the sparkles on the water clip to white. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.5 Mia Huang（黃米亞，22）｜粉紫霓虹的電競時尚棚（首批建議）

- **與人設核對：** 主管方向「電競風時尚棚拍、受控粉紫輪廓光」與人設一致（實況主、霓虹紫與棉花糖粉、cosplay-lite）。不調整；把她的雜亂直播間換成乾淨的棚景。
- **為什麼適合她：** 她的工作就是被看、被反應。把直播間的 RGB 光拿來當專業棚拍的佈景光，臉用乾淨的白光打，保留俏皮與挑逗。
- **參考照片（既有）：** mia-11、mia-02

| 項目 | 內容 |
|---|---|
| 場景 | 乾淨的攝影棚，布置成電競場景：一張白色電競椅、一張只有一把發光鍵盤的桌子、深炭灰牆上幾支直立霓虹燈管，桌上沒有其他東西。 |
| 服裝 | 黑色短版拉鍊帽 T（敞開）、淺紫羅紋短版背心、黑色高腰短褲、白色過膝襪、白色厚底球鞋。 |
| 髮型／髮色 | 灰棕色長髮鬆散大波浪，左側臉旁一片粉紅 money piece 挑染（她最有辨識度的特徵）。 |
| 配件 | 白色電競耳機掛在脖子上、細銀手鍊。 |
| 光線（主光／補光） | 主光：大型中性偏暖柔光箱從相機左側，臉最亮。輪廓：洋紅與紫色霓虹燈管洗亮後牆，並在頭髮與肩膀邊緣留下彩色輪廓光。補光：白色電競椅把柔和中性光補到腿上。 |
| 背景與色彩 | 彩色背景對中性膚色——兩種色溫同框；測光給臉，燈管中心過曝、地面沉到深藍黑。 |
| 表情與視線 | 俏皮眨眼、挑逗的半笑。 |
| 姿勢與雙手 | 橫坐在電競椅上，一腳勾在扶手、另一腳踩地，上身扭向鏡頭；一手把耳機從脖子上拉開，另一手放在膝上；帽 T 下襬擺動。 |
| 橫構圖 | 3:2，70mm、約 3 公尺、坐姿胸口高度；全身坐姿，人物在左三分線，右側延伸霓虹牆與桌子。 |
| 直構圖 | 3:4，同機位；全身坐姿置中，最上面一支燈管在上緣內，頭頂留白。 |
| 甜美元素 | 眨眼、二次元感的眼妝、粉紅挑染。 |
| 性感元素 | 短版背心露腰、過膝襪與短褲、勾在扶手上的腿。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：坐姿頭頂留白充足。身形：全身坐姿，勾腿的姿勢要檢查腿的數量與連接。日期區：橫式右側霓虹牆、直式下方地面。 |
| 替代方向 | 白天的新竹咖啡座：白色短版 T＋牛仔短褲＋灰色帽 T 綁在腰間，戶外座位、午後側光，去電競化（她的「白天的新竹」支柱）。 |

| 風險 | 處理 |
|---|---|
| 霓虹讓臉變紫、變髒 | 寫明中性臉光是最亮的來源，霓虹只當背景與輪廓 |
| 鍵盤或耳機出現假字與品牌 | 鍵盤只寫發光、不寫字；耳機寫素白 |
| 勾腿姿勢肢體錯誤 | 生成後放大檢查腿與手；不行就改成雙腳踩地的側坐 |
| 過膝襪＋cosplay 感顯小 | 寫明 adult，不加貓耳等過度幼化道具 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 22-year-old adult Taiwanese woman with fair, luminous porcelain-toned skin and big expressive eyes with soft anime-inspired makeup, softly winged liner and glossy tinted lips, long ash-brown hair in loose waves with a pastel-pink money-piece highlight framing the left side of her face. Curvy figure, 160 cm tall, bust 91 cm, waist 57 cm, hips 88 cm, F cup, full chest and slim waist. She wears a black cropped zip-up hoodie left open over a lilac ribbed crop tank, black high-waisted shorts, white thigh-high socks, chunky white sneakers, a plain white gaming headset resting around her neck and a thin silver chain bracelet. Setting: a clean photo studio styled as a gaming set, a white gaming chair, a sleek desk with one softly glowing keyboard, and vertical neon light tubes on a dark charcoal wall behind, nothing else on the desk. She sits sideways across the gaming chair with one leg hooked over the armrest and the other foot on the floor, twisting her upper body toward the camera, one hand pulling the headset band away from her neck and the other resting on her knee, giving a playful wink with a teasing half-smile, the hoodie hem swinging. Horizontal 3:2 frame shot on a full-frame camera with a 70mm lens from about three metres, camera at her seated chest height, framed full body seated and placed on the left third, the neon-lined wall and desk extending to the right. Lighting: magenta and violet neon tubes wash the back wall and rim the edges of her hair and shoulders as the scene colour, while a separate large neutral-warm softbox key from camera-left lights her face cleanly as the brightest area; the white chair bounces soft neutral fill onto her legs; coloured background against neutral skin; exposure is set for her face, so the neon tubes clip to white cores and the floor falls to deep blue-black. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 22-year-old adult Taiwanese woman with fair, luminous porcelain-toned skin and big expressive eyes with soft anime-inspired makeup, softly winged liner and glossy tinted lips, long ash-brown hair in loose waves with a pastel-pink money-piece highlight framing the left side of her face. Curvy figure, 160 cm tall, bust 91 cm, waist 57 cm, hips 88 cm, F cup, full chest and slim waist. She wears a black cropped zip-up hoodie left open over a lilac ribbed crop tank, black high-waisted shorts, white thigh-high socks, chunky white sneakers, a plain white gaming headset resting around her neck and a thin silver chain bracelet. Setting: a clean photo studio styled as a gaming set, a white gaming chair, a sleek desk with one softly glowing keyboard, and vertical neon light tubes on a dark charcoal wall behind, nothing else on the desk. She sits sideways across the gaming chair with one leg hooked over the armrest and the other foot on the floor, twisting her upper body toward the camera, one hand pulling the headset band away from her neck and the other resting on her knee, giving a playful wink with a teasing half-smile, the hoodie hem swinging. Vertical 3:4 frame shot on a full-frame camera with a 70mm lens from about three metres, camera at her seated chest height, framed full body seated and centred, the top neon tube just inside the top edge and space above her head. Lighting: magenta and violet neon tubes wash the back wall and rim the edges of her hair and shoulders as the scene colour, while a separate large neutral-warm softbox key from camera-left lights her face cleanly as the brightest area; the white chair bounces soft neutral fill onto her legs; coloured background against neutral skin; exposure is set for her face, so the neon tubes clip to white cores and the floor falls to deep blue-black. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.6 Yuna Kim（김하은，21）｜首爾公寓的極簡窗光

- **與人設核對：** 主管方向「極簡窗光、針織＋緞面裙、安靜氣質」與人設一致（冷白、乾淨灰、首爾早晨、臉永遠是主角），也和 Rin 的緞面晨袍分得開（Yuna 是白天、極簡、坐姿正面）。保留她的櫻桃髮夾小重點。
- **為什麼適合她：** 她的氣質是「清冷、乾淨、刻意但不做作」。大窗、白紗簾、一張長凳，讓臉成為畫面的全部重點。
- **參考照片（既有）：** yuna-06、yuna-01

| 項目 | 內容 |
|---|---|
| 場景 | 極簡白色首爾公寓：大窗配白色薄紗簾、淺橡木地板、一張低矮白色長凳，房間裡沒有其他東西。 |
| 服裝 | 柔灰細針織短版開襟（扣中間一顆、滑落一側肩）、象牙白緞面斜裁中長裙（會反光）、赤腳。 |
| 髮型／髮色 | 深棕到黑的自然波浪、鎖骨長度、空氣感、八字瀏海。 |
| 配件 | 耳上一支紅色櫻桃髮夾、細銀鍊。 |
| 光線（主光／補光） | 主光：早晨日光透過白紗簾，從相機右側大面積柔光。補光：白牆與淺地板把乾淨的中性光補進臉的陰影面。 |
| 背景與色彩 | 冷白窗光對橡木地板的淡暖色；測光給臉，窗戶本身接近純白。 |
| 表情與視線 | 平靜、幾乎看不出來的微笑，眼神穩定看鏡頭。 |
| 姿勢與雙手 | 側坐在窗邊長凳，雙膝併攏朝向鏡頭；一手放在緞面裙上，另一手輕碰窗簾邊緣；窗簾在微風中飄動。 |
| 橫構圖 | 3:2，85mm、約 3 公尺、坐姿胸口高度；膝上，人物在右三分線，左側是明亮的窗與飄動的紗簾。 |
| 直構圖 | 3:4，同機位；膝上置中，窗框上緣在畫面頂部附近，頭頂留白。 |
| 甜美元素 | 櫻桃髮夾、溫柔的微笑、柔軟的針織。 |
| 性感元素 | 開襟滑落露肩、緞面裙的光澤與身體線條。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：坐姿頭頂留白充足。身形：膝上。日期區：橫式左側窗光、直式下方地板。 |
| 替代方向 | 清晨的空屋頂：白色細肩背心＋灰色迷你格紋裙＋短版外套，站在欄杆邊，藍調時刻的冷光（她的「首爾的日常」支柱，背景只有天空）。 |

| 風險 | 處理 |
|---|---|
| 安靜的表情變得呆板 | 用有名字的表情（平靜的淺笑）＋視線 |
| 窗戶過曝吃掉臉的輪廓 | 測光給臉、補光寫白牆 |
| 緞面裙在坐姿下皺褶怪異 | 生成後檢查；不行改站姿靠窗 |
| 房間太空變得像假棚 | 保留一張長凳與木地板的細節 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 21-year-old adult Korean woman with fair, luminous skin and large bright double-eyelid eyes, dark-brown natural wavy hair at collarbone length with airy volume and curtain bangs, a small red cherry hair clip above one ear. Slim figure, 168 cm tall, bust 84 cm, waist 58 cm, hips 89 cm, C cup. She wears a soft grey fine-knit cropped cardigan buttoned at the middle and sliding off one shoulder, an ivory satin bias-cut midi slip skirt that catches the light, bare feet and a thin silver chain necklace. Setting: a minimalist white Seoul apartment with a large window and sheer white curtains, a pale oak floor and one low white bench, nothing else in the room. She sits sideways on the bench by the window with her knees together and angled toward the camera, one hand resting on the satin skirt and the other lightly touching the curtain edge, turning her face to the camera with a calm, barely-there smile and steady eyes as the curtain drifts in a light breeze. Horizontal 3:2 frame shot on a full-frame camera with an 85mm lens from about three metres, camera at her seated chest height, framed from the knees up and placed on the right third, the bright window and drifting curtain to the left. Lighting: soft morning daylight through the sheer curtains from camera-right acts as a large diffused key; the white wall and pale floor bounce clean neutral fill into the shadow side of her face; cool white window light against the faint warm tone of the oak floor; exposure is set for her face, so the window itself glows near white. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 21-year-old adult Korean woman with fair, luminous skin and large bright double-eyelid eyes, dark-brown natural wavy hair at collarbone length with airy volume and curtain bangs, a small red cherry hair clip above one ear. Slim figure, 168 cm tall, bust 84 cm, waist 58 cm, hips 89 cm, C cup. She wears a soft grey fine-knit cropped cardigan buttoned at the middle and sliding off one shoulder, an ivory satin bias-cut midi slip skirt that catches the light, bare feet and a thin silver chain necklace. Setting: a minimalist white Seoul apartment with a large window and sheer white curtains, a pale oak floor and one low white bench, nothing else in the room. She sits sideways on the bench by the window with her knees together and angled toward the camera, one hand resting on the satin skirt and the other lightly touching the curtain edge, turning her face to the camera with a calm, barely-there smile and steady eyes as the curtain drifts in a light breeze. Vertical 3:4 frame shot on a full-frame camera with an 85mm lens from about three metres, camera at her seated chest height, framed from the knees up and centred, the top of the window frame near the top edge and space above her head. Lighting: soft morning daylight through the sheer curtains from camera-right acts as a large diffused key; the white wall and pale floor bounce clean neutral fill into the shadow side of her face; cool white window light against the faint warm tone of the oak floor; exposure is set for her face, so the window itself glows near white. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.7 Tammy Chou（周語彤，24）｜都會白色建築的熱粉色洋裝（型錄外拍）

- **與人設核對：** 主管方向「都會時裝、貼身洋裝、建築感背景」與人設一致（網拍老闆娘、自己當模特兒、配色螢光粉與高亮白）。調整：Rainie 也是貼身洋裝＋夜景，所以 Tammy 改成白天、熱粉色、白色建築，像一張型錄外拍；也與 Somi 的暖橘棚景分開（R2 目視紀錄兩人遮髮後骨架接近）。
- **為什麼適合她：** 她的工作就是「把衣服穿到讓人想買」。白色建築＋晴天硬光＋一件飽和的熱粉色洋裝，就是一張乾淨、明亮、有商品感的時裝照。
- **參考照片（既有）：** tammy-08、tammy-01

| 項目 | 內容 |
|---|---|
| 場景 | 現代白色建築外觀，晴天：寬大的清水混凝土階梯、身後一面平滑的白色弧形牆，階梯上沒有其他人。 |
| 服裝 | 熱粉色方領羅紋針織貼身迷你洋裝、白色尖頭露跟鞋（slingback）、小型白色硬挺肩背包。 |
| 髮型／髮色 | 奶茶金棕大波浪長捲髮、蓬鬆有空氣感，臉側一片淺色 money piece 挑染。 |
| 配件 | 金色圈耳環。 |
| 光線（主光／補光） | 主光：晴天硬光從右前上方，階梯邊緣投下清楚的斜線陰影。補光：白色弧形牆與淺色水泥把明亮中性光反回臉上，臉維持最亮。 |
| 背景與色彩 | 飽和熱粉對冷白牆與藍灰陰影；測光給臉，陽光照到的白牆允許輕微過曝。 |
| 表情與視線 | 明亮的大笑，看鏡頭。 |
| 姿勢與雙手 | 走下階梯、朝鏡頭走來：重心在後腳，前腳正要踏到下一階；一手插腰，另一手把頭髮往後撥；大波浪隨步伐彈動。 |
| 橫構圖 | 3:2，85mm、約 5 公尺、肚臍高度；全身，人物在左三分線，右側是階梯與弧形牆的幾何線條。 |
| 直構圖 | 3:4，同機位；全身置中，腳在下 1/3，頭頂留白。 |
| 甜美元素 | 大笑、彈動的長捲髮、熱粉色。 |
| 性感元素 | 貼身針織洋裝的曲線、方領、長腿與高跟鞋。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：全身構圖頭在畫面上 1/4，頭頂留白要寫足。身形：全身，橫直都完整。日期區：橫式右側階梯、直式下方階梯。 |
| 替代方向 | 白色無縫棚的型錄風：淺色牛仔外套披肩＋白色貼身針織洋裝，手拿衣架上的下一套，高亮均勻棚光（她的「換裝／試穿」支柱，乾淨版）。 |

| 風險 | 處理 |
|---|---|
| 硬光在臉上留下深陰影 | 寫明白牆與水泥的補光、臉是最亮區域 |
| 高跟鞋＋階梯的腳部結構錯誤 | 生成後放大檢查腳與鞋跟；不行改成站在平台上 |
| 包包出現 logo 或文字 | 寫素面、無標誌的白色包 |
| 與 Rainie 太像（都是貼身洋裝） | 白天、熱粉、白色建築 vs Rainie 的夜景血紅緞面 |
| 與 Somi 的 R2 目視相似紀錄 | 冷白建築與熱粉，不用暖橘；不改臉，不宣稱能消除相似 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 24-year-old adult Taiwanese woman with fair, luminous porcelain-toned skin, round almond eyes with visible aegyo-sal, shimmer eyeshadow and jelly-glossy lips, long voluminous big-wave hair in milk-tea golden brown with light money-piece highlights at the front. Curvy figure, 160 cm tall, bust 90 cm, waist 57 cm, hips 89 cm, E cup, full chest and slim waist. She wears a fitted hot-pink square-neck rib-knit mini dress, white pointed slingback heels, a small structured plain white shoulder bag and gold hoop earrings. Setting: a modern white architecture exterior on a clear day, a wide concrete staircase with clean geometric shadows and a smooth white curved wall behind, the steps empty. She walks down the steps toward the camera, weight on the back foot as the front foot reaches the next step, one hand on her hip and the other lifting her hair back from her face, smiling brightly at the camera, her big waves bouncing with the step. Horizontal 3:2 frame shot on a full-frame camera with an 85mm lens from about five metres, camera at her navel height, framed full body and placed on the left third, the staircase and curved white wall forming clean geometric lines to the right, generous space above her head. Lighting: strong clear sun from high front-right casting crisp diagonal shadows of the stair edges; the white curved wall and pale concrete bounce bright neutral fill up onto her face so it stays the brightest area; the saturated hot-pink dress against cool white and blue-grey shadow; exposure is set for her face, so the sunlit wall highlights clip slightly. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 24-year-old adult Taiwanese woman with fair, luminous porcelain-toned skin, round almond eyes with visible aegyo-sal, shimmer eyeshadow and jelly-glossy lips, long voluminous big-wave hair in milk-tea golden brown with light money-piece highlights at the front. Curvy figure, 160 cm tall, bust 90 cm, waist 57 cm, hips 89 cm, E cup, full chest and slim waist. She wears a fitted hot-pink square-neck rib-knit mini dress, white pointed slingback heels, a small structured plain white shoulder bag and gold hoop earrings. Setting: a modern white architecture exterior on a clear day, a wide concrete staircase with clean geometric shadows and a smooth white curved wall behind, the steps empty. She walks down the steps toward the camera, weight on the back foot as the front foot reaches the next step, one hand on her hip and the other lifting her hair back from her face, smiling brightly at the camera, her big waves bouncing with the step. Vertical 3:4 frame shot on a full-frame camera with an 85mm lens from about five metres, camera at her navel height, framed full body and centred with her feet in the lower third, clear space above her head. Lighting: strong clear sun from high front-right casting crisp diagonal shadows of the stair edges; the white curved wall and pale concrete bounce bright neutral fill up onto her face so it stays the brightest area; the saturated hot-pink dress against cool white and blue-grey shadow; exposure is set for her face, so the sunlit wall highlights clip slightly. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.8 Rin Ayase（綾瀨凜，25）｜黎明公寓的祖母綠緞袍（首批建議）

- **與人設核對：** 主管方向「緞面晨光、深色晨袍、露肩回眸」與 Penny 喜歡的 rin-04 一致，也符合她的「下班後清晨」支柱與深綠／金的配色。不調整。和 Yerin 有碰撞紀錄：用暗色室內、黎明冷光＋暖燈的成熟調性，與 Yerin 的明亮戶外分開。
- **為什麼適合她：** 銀座下班後的清晨，是她「私下很安靜」的那一面。緞面、裸肩、回眸，把 rin-04 的感覺拍成正式的大片：冷色的天光加一盞還沒關的暖燈。
- **參考照片（既有）：** rin-04、rin-01

| 項目 | 內容 |
|---|---|
| 場景 | 東京高樓層公寓的黎明：高窗外是淡色天空與遠方柔和的城市，一張鋪象牙白床單的低床，床邊一盞還亮著的黃銅檯燈，房間整齊。 |
| 服裝 | 深祖母綠真絲緞面晨袍，腰間鬆鬆繫起，從一側肩膀滑落露出背部。 |
| 髮型／髮色 | 深酒紅棕長髮，鬆鬆盤成低髻，頸邊落下幾縷。 |
| 配件 | 小金色垂墜耳環、細金手鍊。 |
| 光線（主光／補光） | 主光：高窗進來的冷藍灰黎明光打在臉與肩上。輪廓：她身後的黃銅檯燈在晨袍與頭髮上加一點琥珀色光。補光：象牙白床單把柔光補進陰影面。 |
| 背景與色彩 | 冷藍窗光對暖琥珀燈光；測光給臉，窗外天空偏白、遠處角落沉入深色陰影。 |
| 表情與視線 | 平靜、心照不宣的半笑。 |
| 姿勢與雙手 | 站在窗邊、背部 3/4 朝鏡頭：重心在左腳，一手在胸前拉住晨袍，另一手扶著窗框；越過裸肩回頭看鏡頭（轉頭不超過 90 度）；緞面下襬輕輕擺動。 |
| 橫構圖 | 3:2，85mm、約 3 公尺、肚臍高度；大腿中段以上，人物在左三分線，右側是窗與黎明的城市。 |
| 直構圖 | 3:4，同機位；大腿中段以上置中，頭頂留白。 |
| 甜美元素 | 回眸的淺笑、柔和的晨光。 |
| 性感元素 | 滑落的緞面露出肩與背、低髻露出頸線、緞面貼著身形的光澤。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：盤髮頭頂低，留白容易。身形：大腿中段以上。日期區：橫式右側窗景、直式下方較暗的床與地面（需確認日期字的對比）。 |
| 替代方向 | 出勤前的銀座：黑色絲絨細肩帶長禮服，坐在金色燈光的吧台邊（不拿酒杯），夜間金色燈光與玻璃反射（她的「出勤前準備」支柱）。 |

| 風險 | 處理 |
|---|---|
| 回頭造成脖子扭曲 | 寫明背部 3/4 朝鏡頭、轉頭不超過 90 度 |
| 晨袍遮蔽不足 | 寫明一手在胸前拉住晨袍，只露肩與背 |
| 暗場景噪點、臉發灰 | 寫明窗光主光在臉上、臉最亮；首批觀察 |
| rin-04 的臉偏小、側後方 | 這次用大腿以上構圖、臉朝鏡頭的回眸，讓臉更清楚 |
| 與 Yerin 的碰撞紀錄 | 暗色室內與黎明冷暖對比 vs Yerin 的明亮戶外運動；不改臉，不宣稱能消除碰撞 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 25-year-old adult Japanese woman with fair, cool-toned luminous skin, an oval face and long narrow eyes, precise eyeliner and a muted rose-red lip, long deep wine-red brown hair pinned in a loose low bun with a few strands fallen at her neck. Curvy figure, 166 cm tall, bust 92 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a deep emerald-green silk satin robe tied loosely at the waist and slipping off one shoulder to show her back, small gold drop earrings and a thin gold bracelet. Setting: a quiet high-floor Tokyo apartment at dawn, a tall window with pale sky and a soft distant city, a low bed with ivory linen and a brass bedside lamp still switched on, the room tidy. She stands by the window with her back three-quarters to the camera, weight on her left leg, one hand holding the robe closed at her chest and the other resting on the window frame, turning her head back over her bare shoulder toward the camera with a calm, knowing half-smile, the satin hem swaying. Horizontal 3:2 frame shot on a full-frame camera with an 85mm lens from about three metres, camera at her navel height, framed from mid-thigh up and placed on the left third, the tall window and pale dawn city to the right, clear space above her head. Lighting: cool blue-grey dawn light from the tall window as the key on her face and shoulder; the warm brass bedside lamp behind her adds a small amber glow on the robe and hair; the ivory linen bounces soft fill into the shadow side; cool blue window light against warm amber lamplight; exposure is set for her face, so the sky in the window goes pale and the far corners fall into deep shadow. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 25-year-old adult Japanese woman with fair, cool-toned luminous skin, an oval face and long narrow eyes, precise eyeliner and a muted rose-red lip, long deep wine-red brown hair pinned in a loose low bun with a few strands fallen at her neck. Curvy figure, 166 cm tall, bust 92 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a deep emerald-green silk satin robe tied loosely at the waist and slipping off one shoulder to show her back, small gold drop earrings and a thin gold bracelet. Setting: a quiet high-floor Tokyo apartment at dawn, a tall window with pale sky and a soft distant city, a low bed with ivory linen and a brass bedside lamp still switched on, the room tidy. She stands by the window with her back three-quarters to the camera, weight on her left leg, one hand holding the robe closed at her chest and the other resting on the window frame, turning her head back over her bare shoulder toward the camera with a calm, knowing half-smile, the satin hem swaying. Vertical 3:4 frame shot on a full-frame camera with an 85mm lens from about three metres, camera at her navel height, framed from mid-thigh up and centred, clear space above her head. Lighting: cool blue-grey dawn light from the tall window as the key on her face and shoulder; the warm brass bedside lamp behind her adds a small amber glow on the robe and hair; the ivory linen bounces soft fill into the shadow side; cool blue window light against warm amber lamplight; exposure is set for her face, so the sky in the window goes pale and the far corners fall into deep shadow. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.9 Rainie Hsu（許雷妮，24）｜頂樓夜景的血紅緞面馬甲洋裝

- **與人設核對：** 主管方向「夜色華麗、派對禮服、明亮主光＋城市散景」與人設一致（夜生活女王、血紅／黑／銀、高衩、馬甲）。限制：她的 brand_dont 有「實際飲酒或醉態」——畫面不放酒杯、酒瓶。和 Iris（同為長直黑髮）的 R2 目視相似：用夜景華麗 vs Iris 的白天甜美拉開。
- **為什麼適合她：** 她「走進來整個房間就變了」。一件血紅緞面馬甲洋裝、城市燈海、直視鏡頭的自信笑——是她的派對夜，而且臉要打得夠亮，不是暗暗的夜拍。
- **參考照片（既有）：** rainie-06、rainie-10

| 項目 | 內容 |
|---|---|
| 場景 | 高樓頂層露台的夜晚：玻璃欄杆、腳下城市燈光化成柔和散景、平滑的深色石材地面，露台上沒有其他東西，玻璃只反射城市燈光。 |
| 服裝 | 血紅緞面馬甲迷你洋裝（大腿高衩）、黑色細帶高跟涼鞋。 |
| 髮型／髮色 | 長直黑髮，梳得光滑有光澤，深側分。 |
| 配件 | 大型銀色垂墜耳環、細銀手環。 |
| 光線（主光／補光） | 主光：從左前方、頭部高度的大面積明亮柔光（像露台門口的光），臉最亮，緞面出現銳利的紅色高光。補光：深色石材地面反射一點洋裝的紅光。 |
| 背景與色彩 | 冷藍夜色與暖金城市散景；測光給臉，城市燈光化成發光的圓點，天空維持深藍。 |
| 表情與視線 | 直視鏡頭、自信又帶點壞的笑。 |
| 姿勢與雙手 | 背靠玻璃欄杆：重心在一側臀部，一腳從高衩往前伸；一手放在欄杆上，另一手把頭髮撥到一側肩上；頭髮隨動作擺動。 |
| 橫構圖 | 3:2，85mm、約 4 公尺、肚臍高度；膝上，人物在右三分線，左側是城市散景。 |
| 直構圖 | 3:4，同機位；膝上置中，頭頂留白。 |
| 甜美元素 | 頭髮撥向一側的動作、笑容。 |
| 性感元素 | 血紅緞面馬甲、高衩露出的腿、直視的眼神。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：膝上構圖頭頂留白足。身形：膝上。日期區：橫式左側城市散景（暗底，日期字要用淺色）、直式下方地面。 |
| 替代方向 | 銀色背景布的派對棚拍：黑色亮片細肩帶短洋裝，銀色金屬流蘇背景，硬一點的閃燈主光（她的「穿搭／出門前」支柱，棚內版）。 |

| 風險 | 處理 |
|---|---|
| 夜景噪點、臉發暗 | 寫明大面積明亮主光，臉是最亮區域 |
| 出現酒杯或酒瓶 | 場景只寫欄杆與地面，手上不拿東西（brand_dont） |
| 高衩遮蔽 | 寫明高衩只露出腿，生成後逐張檢查 |
| 玻璃反射出另一個人 | 寫明玻璃只反射城市燈光 |
| 與 Iris 的 R2 目視相似 | 夜景華麗、側分光滑髮、血紅 vs Iris 的白天河濱甜笑；不改臉 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 24-year-old adult Taiwanese woman with fair, luminous porcelain-toned skin, high cheekbones and a sculpted jaw, soft-glam makeup with a soft brown liner close to the lash line, long straight jet-black hair worn sleek and glossy with a deep side part. Curvy figure, 165 cm tall, bust 94 cm, waist 59 cm, hips 92 cm, F cup, full chest and slim waist. She wears a blood-red satin corset mini dress with a thigh-high slit, strappy black stiletto sandals, large silver statement drop earrings and a slim silver cuff. Setting: a high-rise penthouse terrace at night, a glass balustrade, the city lights far below spread into soft bokeh, a smooth dark stone floor, nothing else on the terrace, the glass reflecting only the city lights. She leans back against the glass balustrade with her weight on one hip and one leg forward through the slit, one hand resting on the rail and the other sweeping her hair over one shoulder, looking straight into the camera with a confident, slightly mischievous smirk, her hair swinging as she moves. Horizontal 3:2 frame shot on a full-frame camera with an 85mm lens from about four metres, camera at her navel height, framed from the knees up and placed on the right third, the glowing city bokeh filling the left side, clear space above her head. Lighting: a large bright soft key from front-left at head height, as if from the terrace doorway, makes her face the brightest area and the satin catches sharp red highlights; cool blue night ambience and warm gold city bokeh behind; the dark stone floor reflects a faint red glow from the dress; exposure is set for her face, so the city lights blur into glowing discs and the sky stays deep navy. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 24-year-old adult Taiwanese woman with fair, luminous porcelain-toned skin, high cheekbones and a sculpted jaw, soft-glam makeup with a soft brown liner close to the lash line, long straight jet-black hair worn sleek and glossy with a deep side part. Curvy figure, 165 cm tall, bust 94 cm, waist 59 cm, hips 92 cm, F cup, full chest and slim waist. She wears a blood-red satin corset mini dress with a thigh-high slit, strappy black stiletto sandals, large silver statement drop earrings and a slim silver cuff. Setting: a high-rise penthouse terrace at night, a glass balustrade, the city lights far below spread into soft bokeh, a smooth dark stone floor, nothing else on the terrace, the glass reflecting only the city lights. She leans back against the glass balustrade with her weight on one hip and one leg forward through the slit, one hand resting on the rail and the other sweeping her hair over one shoulder, looking straight into the camera with a confident, slightly mischievous smirk, her hair swinging as she moves. Vertical 3:4 frame shot on a full-frame camera with an 85mm lens from about four metres, camera at her navel height, framed from the knees up and centred, clear space above her head. Lighting: a large bright soft key from front-left at head height, as if from the terrace doorway, makes her face the brightest area and the satin catches sharp red highlights; cool blue night ambience and warm gold city bokeh behind; the dark stone floor reflects a faint red glow from the dress; exposure is set for her face, so the city lights blur into glowing discs and the sky stays deep navy. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.10 Miu Shiraishi（白石美羽，22）｜開店前的奶油色咖啡館（首批建議）

- **與人設核對：** 主管方向「奶油色咖啡館、露肩針織、甜美正面」與人設一致（中目黑咖啡店員、奶白／木色／窗光黃）。風險：她是童顏、156 cm——寫明 adult、成熟的針織與麂皮短裙，不用娃娃裝元素。碰撞最多（Miu–Jia 0.01219、Miu–Somi 0.01894）：用暖木與奶油色、安靜、淺亞麻短髮拉開調性。
- **為什麼適合她：** 她是「一天講不到幾句話、存在感很強」的店員。開店前、陽光剛進來、雙手捧著一杯拿鐵——安靜、甜，畫面有蒸氣與木頭的質地。
- **參考照片（既有）：** miu-01、miu-02

| 項目 | 內容 |
|---|---|
| 場景 | 開店前的中目黑小咖啡館：溫暖的長橡木吧台、一側是義式咖啡機與一疊素面陶杯、大片前窗，店內乾淨無人。 |
| 服裝 | 奶油色粗針織露肩毛衣、淺棕麂皮迷你裙、腰間繫一條短版天然亞麻咖啡師圍裙。 |
| 髮型／髮色 | 淺亞麻米金，齊肩內彎鮑伯、空氣瀏海。 |
| 配件 | 細金耳針。 |
| 光線（主光／補光） | 主光：低角度的暖色晨光從相機左側的前窗進來，打在臉與肩上。補光：橡木吧台把暖蜂蜜色光反進陰影。 |
| 背景與色彩 | 暖金窗光對店內深處的冷灰陰影；測光給臉，窗戶發亮、後牆變暗，蒸氣被陽光照亮。 |
| 表情與視線 | 輕輕歪頭、柔和的甜笑，直視鏡頭。 |
| 姿勢與雙手 | 站在吧台後面、面向鏡頭：雙手在胸口高度捧著一杯冒著熱氣的陶瓷拿鐵杯；毛衣滑落一側肩。 |
| 橫構圖 | 3:2，70mm、約 3 公尺、胸口高度；腰上，人物在左三分線，右側延伸吧台與發光的窗。 |
| 直構圖 | 3:4，同機位；腰上置中，頭頂留白。 |
| 甜美元素 | 捧杯、歪頭的甜笑、蒸氣與暖光。 |
| 性感元素 | 露肩毛衣、亞麻圍裙收出的腰線、她的曲線身材（童顏與身材的反差）。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：短髮、腰上構圖頭頂留白足。身形：腰上——比其他人近，是刻意的（咖啡館場景），但不是胸上特寫。日期區：橫式右側吧台、直式下方吧台面。 |
| 替代方向 | 目黑川邊的清晨步道：米色風衣敞開＋淺色短洋裝，沿河散步回頭，柔和陰天光（她的「外出／中目黑」支柱；只寫河道與樹，不點名地標）。 |

| 風險 | 處理 |
|---|---|
| 捧杯的手指融合 | 寫明雙手捧杯，生成後放大檢查 |
| 杯子或咖啡機出現文字或 logo | 寫素面陶杯、不寫品牌 |
| 髮色被拍得太白、像白髮 | 寫淺亞麻米金（flaxen beige-blonde） |
| 童顏顯小 | 寫明 adult、成熟服裝、不用娃娃裝與制服元素 |
| 與 Jia、Somi 的碰撞紀錄 | 暖木與奶油色、安靜、短髮 vs Jia 的冷色動態與 Somi 的暖橘吃播；不改臉，不宣稱能消除碰撞 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 22-year-old adult Japanese woman with very fair, translucent skin, a round face with big soft downturned eyes, orange-toned blush under the eyes and glossy lips, light flaxen beige-blonde hair in a shoulder-length bob curled inward with airy see-through bangs. Petite curvy figure, 156 cm tall, bust 87 cm, waist 55 cm, hips 86 cm, E cup, full chest and slim waist. She wears a cream chunky off-shoulder knit sweater, a light-brown suede mini skirt, a short natural linen barista apron tied at the waist and thin gold stud earrings. Setting: a small Nakameguro-style café before opening, a long warm oak counter, an espresso machine and stacked plain ceramic cups to one side, a big front window, the room clean and empty. She stands behind the counter facing the camera, both hands cupping a ceramic latte cup at chest height with steam rising, tilting her head slightly with a soft sweet smile and looking straight into the camera. Horizontal 3:2 frame shot on a full-frame camera with a 70mm lens from about three metres, camera at her chest height, framed from the waist up and placed on the left third, the oak counter and glowing window stretching to the right, clear space above her head. Lighting: warm low morning sun through the front window from camera-left as the key on her face and shoulder; the oak counter bounces warm honey light up into the shadows; warm golden window light against cool grey shade at the back of the café; exposure is set for her face, so the window glows bright and the back wall falls darker, the steam lit by the sun. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 22-year-old adult Japanese woman with very fair, translucent skin, a round face with big soft downturned eyes, orange-toned blush under the eyes and glossy lips, light flaxen beige-blonde hair in a shoulder-length bob curled inward with airy see-through bangs. Petite curvy figure, 156 cm tall, bust 87 cm, waist 55 cm, hips 86 cm, E cup, full chest and slim waist. She wears a cream chunky off-shoulder knit sweater, a light-brown suede mini skirt, a short natural linen barista apron tied at the waist and thin gold stud earrings. Setting: a small Nakameguro-style café before opening, a long warm oak counter, an espresso machine and stacked plain ceramic cups to one side, a big front window, the room clean and empty. She stands behind the counter facing the camera, both hands cupping a ceramic latte cup at chest height with steam rising, tilting her head slightly with a soft sweet smile and looking straight into the camera. Vertical 3:4 frame shot on a full-frame camera with a 70mm lens from about three metres, camera at her chest height, framed from the waist up and centred, clear space above her head. Lighting: warm low morning sun through the front window from camera-left as the key on her face and shoulder; the oak counter bounces warm honey light up into the shadows; warm golden window light against cool grey shade at the back of the café; exposure is set for her face, so the window glows bright and the back wall falls darker, the steam lit by the sun. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.11 Jia Seo（서지아，22）｜灰色無縫棚的舞者時尚

- **與人設核對：** 主管方向「舞者時尚棚拍、剪裁服裝、身體線條」與人設一致（舞蹈老師、冷白／灰／木地板／薄荷綠）。調整：避免肌肉線條過強（她是 C 罩杯纖細舞者，但要維持柔和女性線條）。碰撞（Miu、Somi）：用冷色、動態、薄荷綠內層髮色拉開。
- **為什麼適合她：** 她「對身體的控制力是最自豪的事」。一個乾淨的灰色棚、木地板、一個停格的舞蹈動作，讓身體線條本身成為時裝。
- **參考照片（既有）：** jia-02、jia-08

| 項目 | 內容 |
|---|---|
| 場景 | 乾淨的攝影棚：淺灰無縫牆、溫暖的木地板，棚內沒有其他東西。 |
| 服裝 | 黑色單肩貼身連身衣、透膚炭灰色寬版襯衫從一側手臂滑落、高腰灰色寬褲、白色厚底球鞋。 |
| 髮型／髮色 | 冷灰藍黑長髮，內層薄荷綠，甩頭時會閃出來。 |
| 配件 | 小銀色圈耳環。 |
| 光線（主光／補光） | 主光：大型冷白柔光箱從左前方，臉最亮。輪廓：她身後一支窄條燈在肩膀與頭髮畫出乾淨的白色輪廓。補光：木地板把一點暖光補到腿上。 |
| 背景與色彩 | 冷白棚光對溫暖木地板；測光給臉，條燈過曝、遠處牆面略灰。 |
| 表情與視線 | 冷靜自信的半笑，看鏡頭。 |
| 姿勢與雙手 | 舞蹈動作停格：重心在右腳、左腳向側邊延伸，上身扭向鏡頭；一手往外伸展、另一手在鎖骨；頭髮甩過去露出薄荷綠內層。 |
| 橫構圖 | 3:2，85mm、約 5 公尺、肚臍高度；全身，人物在左三分線，右側是灰牆留白。 |
| 直構圖 | 3:4，同機位；全身置中，腳在下 1/3，頭頂留白。 |
| 甜美元素 | 半笑、甩動的髮絲。 |
| 性感元素 | 單肩貼身連身衣與滑落的透膚襯衫、伸展的身體線條、直角肩與長腿。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：甩頭動作要確認頭髮不出框、頭頂留白足。身形：全身，伸展的手腳都要在框內（橫式比較容易）。日期區：橫式右側灰牆、直式下方木地板。 |
| 替代方向 | 收工後的練舞室窗邊：黑色運動內衣外搭寬版白 T、灰色運動褲，坐在大鏡子前的木地板上，傍晚窗光（她的「收工後的鏡子前」支柱；不拍鏡中倒影）。 |

| 風險 | 處理 |
|---|---|
| 動態肢體錯誤（多手、斷腿） | 寫明重心腳與兩手位置，生成後逐肢檢查 |
| 肌肉感過強 | 寫 soft feminine curves、slim dancer figure |
| 頭髮蓋住臉 | 寫明頭髮甩向一側、臉朝鏡頭 |
| 薄荷綠內層沒出現 | 寫明甩頭露出內層；不出現就接受，不為此重生 |
| 與 Miu、Somi 的碰撞紀錄 | 冷色、動態、薄荷綠內層 vs Miu 的暖木靜態與 Somi 的暖橘吃播；不改臉，不宣稱能消除碰撞 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 22-year-old adult Korean woman with fair, cool-toned luminous skin, a small face, straight broad shoulders and long narrow upturned eyes, dewy no-makeup Korean makeup with a soft brown liner and gradient lips, long cool blue-black hair with a mint-green inner layer that flashes when her hair moves. Slim dancer figure with soft feminine curves, 168 cm tall, bust 85 cm, waist 58 cm, hips 90 cm, C cup, long legs and a slim waist. She wears a black one-shoulder fitted bodysuit, a sheer charcoal oversized shirt slipping off one arm, high-waisted wide-leg grey trousers, white chunky sneakers and small silver hoop earrings. Setting: a clean photo studio with a seamless pale grey wall and a warm wooden dance floor, nothing else in the room. She is caught mid-movement in a dance pose, weight on her right leg and the left leg extended to the side, torso twisting toward the camera, one arm stretched outward and the other hand at her collarbone, her hair whipping across so the mint inner layer shows, looking into the camera with a cool, confident half-smile. Horizontal 3:2 frame shot on a full-frame camera with an 85mm lens from about five metres, camera at her navel height, framed full body with her outstretched arm inside the frame and placed on the left third, the pale grey wall open to the right, generous space above her head. Lighting: a large cool-white softbox key from front-left makes her face the brightest area, a narrow strip light behind her draws a clean white rim along her shoulder and hair, and the wooden floor bounces a faint warm fill onto her legs; cool white studio light against the warm wood floor; exposure is set for her face, so the strip light clips and the far wall falls a little grey. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 22-year-old adult Korean woman with fair, cool-toned luminous skin, a small face, straight broad shoulders and long narrow upturned eyes, dewy no-makeup Korean makeup with a soft brown liner and gradient lips, long cool blue-black hair with a mint-green inner layer that flashes when her hair moves. Slim dancer figure with soft feminine curves, 168 cm tall, bust 85 cm, waist 58 cm, hips 90 cm, C cup, long legs and a slim waist. She wears a black one-shoulder fitted bodysuit, a sheer charcoal oversized shirt slipping off one arm, high-waisted wide-leg grey trousers, white chunky sneakers and small silver hoop earrings. Setting: a clean photo studio with a seamless pale grey wall and a warm wooden dance floor, nothing else in the room. She is caught mid-movement in a dance pose, weight on her right leg and the left leg extended to the side, torso twisting toward the camera, one arm stretched outward and the other hand at her collarbone, her hair whipping across so the mint inner layer shows, looking into the camera with a cool, confident half-smile. Vertical 3:4 frame shot on a full-frame camera with an 85mm lens from about five metres, camera at her navel height, framed full body and centred with her feet in the lower third, her outstretched arm inside the frame, clear space above her head. Lighting: a large cool-white softbox key from front-left makes her face the brightest area, a narrow strip light behind her draws a clean white rim along her shoulder and hair, and the wooden floor bounces a faint warm fill onto her legs; cool white studio light against the warm wood floor; exposure is set for her face, so the strip light clips and the far wall falls a little grey. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.12 Yerin Han（한예린，26）｜清晨霧中的球道

- **與人設核對：** 主管方向「高爾夫度假、精緻運動套裝、清晨球場」與人設一致（高球教練、旅遊／球場遠征支柱、草地綠／天空藍／白），也接近她現有的 yerin-04（清晨球場）。人設寫「膚色維持白皙、對防曬近乎偏執」——寫明白皙、戴帽。和 Rin 的碰撞：明亮戶外運動 vs Rin 的暗色室內。也和 Iris 的戶外分開：清晨霧氣＋球桿 vs Iris 的傍晚河濱。
- **為什麼適合她：** 「球衣就是時尚，球技也真的好」。清晨的球道、薄霧、一套精緻的淺藍與白，把她的健康感與大方的笑拍成度假時尚照。
- **參考照片（既有）：** yerin-04、yerin-01

| 項目 | 內容 |
|---|---|
| 場景 | 清晨的高爾夫球道：遠處樹林上方有薄霧，短草上有露水，遠方一支白色旗桿，球道上沒有其他人。 |
| 服裝 | 淺天空藍無袖針織高爾夫 polo、白色百褶高爾夫迷你裙、左手白色皮手套、白色高爾夫鞋、素面白色球帽。 |
| 髮型／髮色 | 亞麻棕長髮、臉側金色挑染，低馬尾從球帽後方穿出。 |
| 配件 | 小金色耳針。 |
| 光線（主光／補光） | 主光：她身後右側的低角度晨光，在馬尾與肩膀畫出暖金輪廓。補光：明亮帶露水的草地與霧氣把柔和冷光補到臉上，臉最亮、膚色維持白皙。 |
| 背景與色彩 | 暖金陽光對冷藍綠的霧；測光給臉，被陽光照亮的霧發光、遠處樹林柔和。 |
| 表情與視線 | 大方明亮的笑，轉頭看鏡頭。 |
| 姿勢與雙手 | 一支一號木橫放在肩後、兩手腕掛在球桿上；重心在後腳，前腳輕輕交叉在前；轉頭看鏡頭；馬尾擺動。 |
| 橫構圖 | 3:2，85mm、約 5 公尺、肚臍高度；全身，人物在右三分線，左側是延伸的球道與霧。 |
| 直構圖 | 3:4，同機位；全身置中，腳在下 1/3，頭頂（含球帽與肩上球桿）留白。 |
| 甜美元素 | 大笑、馬尾、淺藍與白的清爽配色。 |
| 性感元素 | 無袖針織貼身 polo、百褶迷你裙與長腿、170 cm 的身形比例。 |
| 臉／髮頂／身形／日期區 | 臉與髮頂：球帽＋肩上球桿讓頭部附近更寬，頭頂留白要多一點。身形：全身。日期區：橫式左側球道、直式下方草地。 |
| 替代方向 | 高級室內練習場：白色合身 polo＋海軍藍百褶短裙，站在打擊位、收桿姿勢，冷白均勻光（她的「練習場／教課」支柱，背景只有草皮墊與網）。 |

| 風險 | 處理 |
|---|---|
| 握球桿的手與桿身變形 | 寫明手腕掛在球桿上，生成後放大檢查 |
| 肌肉感過強 | 寫 soft feminine lines |
| 膚色被拍成小麥色 | 寫明白皙、戴帽、臉在柔和補光裡 |
| 球帽或衣服出現文字或品牌 | 寫素面白帽、無標誌 |
| 與 Rin 的碰撞紀錄 | 明亮戶外運動 vs Rin 的暗色室內黎明；不改臉，不宣稱能消除碰撞 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 26-year-old adult Korean woman with fair, luminous porcelain-toned skin, bright defined features and a wide open smile, light sun-protective makeup and a bright lip, long flax-brown hair with golden face-framing highlights in a low ponytail pulled through the back of a plain white cap. Curvy athletic figure with soft feminine lines, 170 cm tall, bust 90 cm, waist 60 cm, hips 93 cm, E cup, long legs and a slim waist. She wears a pale sky-blue sleeveless knit golf polo, a white pleated golf mini skirt, a white leather glove on her left hand, white golf shoes and small gold stud earrings. Setting: a golf course fairway in the early morning, soft mist over the far trees, dew on the short grass, a white flagstick far in the distance, the fairway empty. She stands with a driver resting across her shoulders behind her neck, wrists draped over the club, weight on her back leg with the front leg crossed lightly in front, turning her face to the camera with a big bright smile, her ponytail swinging. Horizontal 3:2 frame shot on a full-frame camera with an 85mm lens from about five metres, camera at her navel height, framed full body and placed on the right third, the misty fairway stretching away to the left, generous space above her cap. Lighting: the low early sun behind her and to the right draws a warm gold rim along her ponytail and shoulders; the bright dewy grass and mist bounce soft cool fill onto her face so her face stays the brightest area and her skin stays fair; warm golden sunlight against cool blue-green mist; exposure is set for her face, so the sunlit mist glows and the distant tree line falls soft. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 26-year-old adult Korean woman with fair, luminous porcelain-toned skin, bright defined features and a wide open smile, light sun-protective makeup and a bright lip, long flax-brown hair with golden face-framing highlights in a low ponytail pulled through the back of a plain white cap. Curvy athletic figure with soft feminine lines, 170 cm tall, bust 90 cm, waist 60 cm, hips 93 cm, E cup, long legs and a slim waist. She wears a pale sky-blue sleeveless knit golf polo, a white pleated golf mini skirt, a white leather glove on her left hand, white golf shoes and small gold stud earrings. Setting: a golf course fairway in the early morning, soft mist over the far trees, dew on the short grass, a white flagstick far in the distance, the fairway empty. She stands with a driver resting across her shoulders behind her neck, wrists draped over the club, weight on her back leg with the front leg crossed lightly in front, turning her face to the camera with a big bright smile, her ponytail swinging. Vertical 3:4 frame shot on a full-frame camera with an 85mm lens from about five metres, camera at her navel height, framed full body and centred with her feet in the lower third, clear space above her cap and the club. Lighting: the low early sun behind her and to the right draws a warm gold rim along her ponytail and shoulders; the bright dewy grass and mist bounce soft cool fill onto her face so her face stays the brightest area and her skin stays fair; warm golden sunlight against cool blue-green mist; exposure is set for her face, so the sunlit mist glows and the distant tree line falls soft. Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

## 5. 橫直構圖策略

**建議：同一主題、同一造型，各拍一張橫構圖（3:2）與一張直構圖（3:4）。**

- 版面還沒定。R3 假設的照片框有三種形狀：橫式半版直幅 104×155 mm（比例約 0.67）、橫式寬幅 192×104 mm（約 1.85）、直式統一框 120×128 mm（約 0.94）。一張照片無法同時好用。
- 用一張 3:4 直幅硬裁成寬幅，只剩胸上特寫——主管已明說這不能算橫式寫真。用一張 3:2 橫幅裁成直式近方框，左右要裁掉很多，人物也會被截。
- 分開構圖，可以讓橫幅把人物放在三分線、另一側留給風景或日期；直幅則讓人物置中、頭頂留白避開線圈區。
- soul_2 沒有 seed，兩次生成的服裝與場景細節會有小差異；這是分開拍的代價，在首批測試裡確認差異能不能接受。

**另一種做法：** 同一張照片兩款裁切：只有在橫式最後選「左半直幅照片」（104×155）時才成立——這時 3:4 直幅可以同時供兩款使用。版面確定前不建議只拍一種。

| 層次 | 說明 |
|---|---|
| 拍攝構圖需求 | 橫：人物在左或右三分線、膝上或全身，另一側留給場景；直：人物置中、頭頂留白（線圈區假設畫布上緣 12 mm）、下方留安靜區給可能的小月曆。 |
| 模型原生輸出 | soul_2 quality 2k：3:4 實際輸出 1536×2048、9:16 實際輸出 1152×2048（repo 既有圖可查）。3:2 的實際像素沒有紀錄——依長邊 2048 推算約 2048×1365，未驗證。 |
| 裁切後解析度 | 只能依 R3 的假設框估算，供比較、不當承諾：3:4 原生放直式統一框約 325 ppi、放橫式半版約 336 ppi；3:2 原生放橫式寬幅約 271 ppi。框尺寸改了，數字就跟著變。 |
| 出血／線圈假設 | 沿用 R3：出血 2 mm、線圈區畫布上緣 0–12 mm（直式 12 mm 是本案假設）。照片頂端 12 mm 不放臉、最好不放髮頂。 |
| 廠商待確認 | 實際線圈尺寸、印刷品質門檻、拼版與照片朝向、尺度審稿——都還沒問，本輪也不聯絡廠商。 |
| 不預設的手段 | 外擴（outpaint）與 AI 放大不列為必要步驟。若排版後某張真的不夠，再個案提出，並由 Penny 決定。 |

每位在橫／直兩種構圖下臉、髮頂、身形、日期區能否保住，見第 4 節各位的「臉／髮頂／身形／日期區」列。

## 6. 執行與成本建議（只是提案，不授權任何花費）

**模型：** soul_2＋各人設既有 Soul ID，quality 2k，橫 3:2、直 3:4；不掛 Reference Element；首批不用參考圖。

- Soul ID 鎖臉——這是每位定案身分的來源；nano_banana_pro 曾被使用者以「臉有落差」否決（luna 紀錄），seedream_v4_5 沒有 Soul 鎖定，只靠文字描述臉，容易跑掉。
- 模型官方描述就是「Realistic UGC, fashion editorial and character generation」。

| 人設 | Soul 狀態（紀錄） |
|---|---|
| Somi、Tammy、Rin、Miu、Jia、Yerin | production_ready（2026-09-07／08 訓練；6 張驗證臉部門檻通過） |
| Iris、Luna、Coco、Mia、Yuna | ready（較早訓練；R1 紀錄寫這幾位不在 Soul 總表內，是否跑過同樣的 6 張驗證未知） |
| Rainie | 只能用 v2 的 Soul（ready）；舊的 deprecated Soul 不可用 |

Soul ID 不列在本文件與公開頁面。

**已知限制：**

- Soul V2 不繼承髮型與髮色：每張 prompt 都要寫她自己的髮色髮型（原則七 C-1）。
- Soul V2 不繼承身材：身材要用 prompt 句子補（數字直接寫）。
- 沒有 negative prompt：不要的東西只能用正面描述避開（例如「小徑空無一人」）。
- 碰撞配對（Miu–Jia、Miu–Somi、Jia–Somi、Yerin–Rin）不得同框（C-2）；本企劃每張只有一人。

**多階段：** 不規劃多階段（先生成再換臉、外擴、放大）。若首批發現橫直兩張服裝差太多，才考慮把第一張當唯一的參考圖餵第二張——這可能把構圖或身分一起帶過去，要另外測、另外批准。

**未知：** 3:2 的實際輸出像素、單張實際扣款（見成本）、ready 狀態的 Soul 在棚拍／夜景光線下的身分穩定度、同一造型跨兩次生成的一致性

### 6.1 單價依據

| 項目 | 數值 | 依據 | 等級 |
|---|---|---|---|
| 單張 soul_2 出圖 | 0.12 credits | 歷史紀錄：review/soul_training/FINAL_REPORT.md（2026-09-08）交易明細「Higgsfield Soul V2 -0.12」，114 張驗證圖約 13.7 credits。 | 歷史參考（交易紀錄） |
| get_cost 預檢顯示 | 「1 credit」（credits_exact 0.12） | 多位人設 generation_notes 的預檢紀錄 | 歷史參考 |
| 本輪查證 | 未知 | 本輪 models_explore 不回傳價格；沒有呼叫 get_cost（那屬於建立生成的流程） | 未查證 |
| 注意 | 帳號共用 | 既有生成紀錄裡有一批 4 張實扣 50 credits 的對帳異常（同時段帳號上有其他工作）；執行時要用交易明細逐筆對帳。 | 歷史參考 |

### 6.2 數量與預算

| 項目 | 內容 |
|---|---|
| 首批 | 4 位 × 2 構圖 × 3 個 spec ＝ 24 張；每個 spec 遇 AI 瑕疵最多重生 1 次 → 最多 48 張 |
| 首批預算 | 依 0.12／張：基本 2.88、上限 5.76 credits；若實扣其實是 1／張：基本 24、上限 48 credits。建議首批硬上限 10 credits（依 0.12 計價），超過立即停。 |
| 全案（含首批） | 12 位 × 6 張 ＝ 72 張；重生上限同上 → 最多 144 張。依 0.12／張：8.64–17.28 credits；若 1／張：72–144 credits。建議全案上限 40 credits（依 0.12 計價）。 |
| 不含 | 重新訓練（每次約 25 credits，本案不做）、外擴、放大、影片 |

### 6.3 首批建議人選

| 人設 | 理由 |
|---|---|
| Iris | Penny 最喜歡的參考（iris-04）；戶外逆光是最容易臉暗、膚色被曬黑的情境；Soul 是較早的 ready 版本 |
| Rin | Penny 的參考（rin-04）；室內混光、緞面與回眸是最容易出手部與脖子扭曲的姿勢 |
| Miu | 新入選、高解析素材最少；碰撞最多（Miu–Jia 0.01219），用來看造型與調性能不能拉開差異 |
| Mia | 受控 LED 棚拍（3-A 完整佈光）在這組裡最像商業棚拍；Soul 也是 ready 版本 |

### 6.4 重生上限與停止條件

- 手指、肢體、拼貼、身分跑掉這類 AI 瑕疵：同 spec 最多重生 1 次。
- 只有氛圍、光線、背景質感不如預期：不自動重生，先給 Penny 看（工作室既有規則）。
- 同一位連續 2 個 spec 都出現身分跑掉：停止該位，回報主管。
- 平台拒絕（內容審核）：改寫 1 次；再被拒就停止該 spec。
- 實際扣款與預檢不符、或達到預算上限：立刻全部停止並回報。

**授權：** 本輪不設定任何自動花費授權。Penny 拍板後，由主管另發執行指令；首批結果經 Penny 看過，才擴大到其餘 8 位。

## 7. 要請 Penny 決定的事

1. 12 位的主方向：每位在頁面上選「接受主方向／改用替代方向／想修改」，想修改的請直接寫在備註。
2. 是否同意「同一造型，橫構圖、直構圖各拍一張」？（版面確定前的建議；代價是兩張的細節會有小差異）
3. Somi：主管原方向是純棚拍（針織＋高腰裙），我改成「復古小吃店棚景＋手拿炸雞」以保留她的吃播人設——要哪一個？
4. Coco：主方向是泳池比基尼（尺度同第二階段的泳裝參考，交印前需確認廠商接受範圍）；替代是乾淨房間的居家穿搭——要哪一個？
5. 首批試拍：建議 Iris、Rin、Miu、Mia 四位、首批硬上限 10 credits（依歷史 0.12／張計價；實際單價未查證）。是否同意這個方向，再由主管另發執行指令？

## 8. 共同的皮膚與質感句（每段 prompt 結尾都加）

```text
Visible skin pores and subtle natural skin texture, unretouched skin detail, crisp sharp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```
