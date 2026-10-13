TASK-CAL-001／M-3／R1｜專業寫真企劃修訂與費用查證｜送審報告

# CAL_18 — M-3 12 位人設專業寫真拍攝企劃（R1 修訂版）

> 資料檔：`data/cal_m3_shoot_plan.json`（shoot-plan-v2，R1，2026-10-13）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。
> **僅規劃：沒有生成任何圖片（含測試圖、示意圖），沒有花 credits，沒有上傳，沒有訓練，沒有改 canon 或 Soul ID。** 本輪生成數 0、credits 0、訓練數 0。
> 這是企劃，不是核准：每一項都要 Penny 拍板；生成放行目前是 BLOCK，之後由主管另發執行指令。

## 0. 版本、範圍與主管覆核

| 項目 | 內容 |
|---|---|
| 名單 | roster-v1（docs/calendar/data/cal_m1_owner_roster.json）；不換人，順序不是月份 |
| 素材頁版本 | `b8108eb648a46a57e3bb4dc2158cf878c23d7963` |
| 桌曆基準 | `4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45` |
| 上一版企劃 | shoot-plan-v1（commit `256859b3d6bb77b7647837ccdcc14428dcdb7744`） |
| Aaliya 圖片來源 | repo `4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45`；型錄分支 `claude/kol-dashboard-catalog-gqw9jz` @ `d3fb91ab87547bfa04ee46cf4cfddd6750fcfe52` |
| 型錄頁 | https://kol-catalog-production.up.railway.app/p/aaliya-okonkwo.html |
| 模型查詢 | 2026-10-12 唯讀查詢 Higgsfield models_explore(get, soul_2)：參數只有 quality（1.5k／2k，預設 2k）、Soul ID、1 張參考圖；比例 1:1、16:9、9:16、4:3、3:4、3:2、2:3；沒有 seed、沒有 negative prompt；回傳沒有價格。與 AI_PROMPT_METHOD_REVIEW.md（2026-09-03）記錄一致。 |

| 主管覆核項目 | 結論 |
|---|---|
| Aaliya 研究 | PASS |
| 整組差異 | PASS |
| 拍攝內容、姿態 prompt、橫直構圖 | REVISE |
| 生成放行 | BLOCK（費用依據尚未可信） |

**R1 移除的全組硬性規則**（不是專業寫真的必要條件）：每位都要寫滿五層服裝、每張都要一件飄動的東西、每張都要兩種色溫、補光一定要來自畫面中看得到的物件。

## 1. Penny 喜歡的 4 張（審美參考，不變）

Penny 在第二階段素材頁把下列 4 張列為備選，沒有指定橫式／直式。記錄為 owner 喜歡的既有候選與審美參考；不轉成主照片、不清空瀏覽器裡的選擇。其餘 8 位沒有選中照片，不代表可以套用舊推薦。

| 素材 ID | 照片 | 可借用的特徵 |
|---|---|---|
| iris-04 | Iris｜公園夕陽、白色連帽短上衣＋黑短褲、回頭 | 黃金時段逆光、戶外草地、身形完整的 3/4 身 |
| luna-10 | Luna｜公園夕陽、白色小碎花洋裝、全身 | 柔和暖光、淺色洋裝、乾淨的戶外背景 |
| somi-02 | Somi｜深夜炸雞、握罐甜笑 | 人設本業（吃）＋暖色、笑容、生活感 |
| rin-04 | Rin｜緞面晨袍、回頭背影 | 緞面質感、裸肩回眸、成熟性感 |

四張共同點：光線有方向（夕陽、暖燈）、人物是主角、服裝或材質好看（連帽短上衣、碎花洋裝、緞面）、表情自然；不是手機自拍。這和 Penny 這輪要的「專業寫真質感」一致，企劃直接沿用這些特徵。

## 2. Aaliya 研究（主管 PASS；方法清單 R1 修訂）

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

「尺寸」是讀檔實測；「模型／prompt／Soul ID／後製」只照錄紀錄，紀錄沒有的寫「未知」或「推定」。

### 2.3 目視觀察（不是紀錄）

1. **黃金時段逆光・斜倚 3/4 身**：太陽在她身後斜上方，頭髮與肩線有一圈暖色輪廓光；臉部靠前方的環境反光補亮，沒有死黑；背景是失焦的綠樹與天空，只有一個主體；身體斜倚形成對角線；服裝單純（素色短 T＋牛仔褲），讓身形與光線成為重點。
2. **側光・插腰站姿 3/4 身**：低角度暖陽從側面打來，臉的受光面清楚、陰影面柔和；一手插腰、身體 3/4 側、重心在後腳——典型顯身形的站姿；背景樹叢失焦，地面與天空都乾淨。
3. **夜間室內暖燈・坐姿 3/4 身**：光源是畫面裡看得到的暖色串燈，背景整片暖色散景、遠處較暗；貼身針織洋裝的材質與曲線清楚；坐在木椅上、身體微側，一手放在腿上；直視鏡頭、表情收斂——是「拍照」的姿態，不是隨拍。
4. **戶外硬光・全身正面站姿**：晴天高角度陽光，泳池水面把青綠色反光打回腿與身體下側；全身置中、腳在畫面下緣、上方留天空——全身照沒有變形；長版針織罩衫垂到小腿，拉長身形線條；背景只有棕櫚樹與泳池，沒有人。
5. **坐姿・遠景城市留白**：人物只占畫面約三分之一，大片城市遠景與天空當留白——這種構圖最容易改成橫式；坐在池邊、雙腿入水，身體形成 S 形；白天柔和的自然光；缺點：人物偏小，臉的細節不足，桌曆用要更靠近。

未採用：自拍 2 張（selfie_01／02）是手機自拍角度，正是 Penny 這輪要避免的形式，不列為參考；restaurant_01、poolside_01_v1／v2 與入選的同場景，不重複列。

### 2.4 可移植的方法（R1 修訂版）

| 項目 | 做法 |
|---|---|
| 主光／補光 | 主光要有方向（夕陽在身後、窗在右側、柔光箱在左前）。補光可以來自畫面外的柔光箱、反光板或補光燈，不必是畫面裡看得到的東西。逆光一定要有足夠的臉部補光，讓臉曝光正確、看得清楚。 |
| 背景層次 | 前景乾淨、主體清楚、背景失焦。場景寫「有什麼」而不是「沒有什麼」：例如「草地與小徑空無一人」。 |
| 人物比例 | 先定景別（全身、膝上、大腿以上），再依焦段算距離，讓人物佔畫面高度約 80–88%；不要讓橫幅三分之二是空背景。每張的換算見各位的「取景設計」。 |
| 服裝 | 造型要完整、像寫真穿搭：材質、剪裁、顏色寫清楚，配件依畫面需要；不硬性規定件數。 |
| 表情 | 一個有名字的表情加視線，是一個靜止的瞬間；不寫「先……再……」這種需要時間的變化。 |
| 姿態 | 每張只有一個主要姿態：重心在哪隻腳、兩手各放哪裡；手部安排簡單，不疊加多個動作。 |
| 鏡頭感 | 他拍、全片幅相機、指定焦段與距離；不寫手機前鏡頭、不寫自拍。 |
| 色彩與皮膚 | 保留人物原本的膚色與自然肌膚質感（毛孔、細紋理）；膚色只寫一次，不重複堆疊「瓷白」之類的字；色溫跟著場景走，不強制每張兩種色溫。 |

## 3. 12 位差異總表

| 人設 | 企劃名稱 | 修訂 | 時段 | 光線 | 配色 | 場景 | 服裝 | 姿勢 | 表情 | 取景 | 第一階段 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Iris Chen（陳芯語，22） | 河濱草地的黃金時段 | 姿態與細節 | 傍晚 | 逆光＋畫面外反光板 | 米白・淺藍・暖金 | 河濱草地 | 平口短上衣＋牛仔短褲＋開襟 | 站定、越肩回眸 | 甜笑 | 橫 膝上／直 全身 | 建議 |
| Luna Tanaka（田中ひな，20） | 京都老宅後院的紫陽花 | 姿態與細節 | 白天（陰天） | 大面積柔光＋反光板 | 鼠尾草綠・白 | 町家後院紫陽花 | 方領蕾絲迷你洋裝 | 站姿、一手扶籬笆 | 安靜淺笑 | 橫 膝上／直 全身 |  |
| Somi Oh（오소미，24） | 暖橘色的復古棚景 | 主方向 | 棚內 | 暖色柔光箱 | 暖橘・奶油・紅 | 復古小吃店棚景 | 針織短開襟＋高腰針織短裙 | 輕靠吧台、塞頭髮 | 月牙眼大笑 | 橫 膝上／直 全身 |  |
| Coco Wu（吳可可，20） | 週末飯店泳池的薄荷綠 | 姿態與細節 | 上午 | 晴天高光＋反光板 | 薄荷綠・淺紫・湖水綠 | 飯店泳池 | 比基尼＋透膚罩衫 | 池邊坐姿往後撐 | 歪頭瞇眼大笑 | 橫 坐姿到水面／直 坐姿到水面 |  |
| Mia Huang（黃米亞，22） | 粉紫霓虹的電競時尚棚 | 主方向 | 棚內 | 中性柔光箱＋粉紫輪廓 | 洋紅・紫・黑 | 電競棚景 | 短版帽 T＋背心＋短褲＋過膝襪 | 站在椅旁、插腰 | 眨眼半笑 | 橫 膝上／直 全身 |  |
| Yuna Kim（김하은，21） | 首爾公寓的極簡窗光 | 姿態與細節 | 早晨 | 紗簾漫射窗光 | 冷白・柔灰・象牙 | 極簡白色公寓 | 針織開襟＋緞面中長裙 | 長凳併膝側坐 | 平靜淺笑 | 橫 坐姿全身／直 坐姿膝上 |  |
| Tammy Chou（周語彤，24） | 都會白色建築的熱粉色洋裝（型錄外拍） | 姿態與細節 | 晴天白天 | 硬光＋反光板 | 熱粉・白・藍灰 | 白色建築階梯 | 貼身針織洋裝＋高跟鞋 | 站在階梯上、插腰 | 明亮笑容 | 橫 全身／直 膝上 |  |
| Rin Ayase（綾瀨凜，25） | 黎明公寓的祖母綠緞袍 | 姿態與細節 | 黎明 | 冷色窗光＋暖色檯燈 | 祖母綠・金・象牙 | 高樓公寓臥室 | 緞面晨袍 | 背影 3/4、越肩回眸 | 心照不宣的半笑 | 橫 大腿中段以上／直 膝上 |  |
| Rainie Hsu（許雷妮，24） | 頂樓夜景的血紅緞面馬甲洋裝 | 姿態與細節 | 夜晚 | 明亮柔光箱＋城市散景 | 血紅・黑・銀・深藍 | 頂樓露台 | 緞面馬甲高衩迷你洋裝 | 背靠欄杆、一腳向前 | 直視、自信壞笑 | 橫 膝上／直 全身 |  |
| Miu Shiraishi（白石美羽，22） | 奶油色咖啡館的窗邊座位 | 主方向 | 早晨 | 暖色窗光＋補光 | 奶油・橡木・淺棕 | 咖啡館窗邊座位 | 露肩粗針織＋收腰麂皮短裙 | 窗邊長凳、交疊腿坐姿 | 歪頭甜笑 | 橫 坐姿全身／直 坐姿膝上 |  |
| Jia Seo（서지아，22） | 灰色無縫棚的舞者時尚 | 姿態與細節 | 棚內 | 冷白柔光箱＋條燈輪廓 | 黑・灰・木色・薄荷綠 | 灰色無縫棚 | 單肩連身衣＋窄管褲 | 停住的舞蹈線條 | 冷靜自信半笑 | 橫 全身／直 全身 |  |
| Yerin Han（한예린，26） | 清晨霧中的球道 | 姿態與細節 | 清晨 | 逆光＋反光板 | 天空藍・白・草綠 | 高爾夫球道 | 無袖針織 polo＋百褶短裙＋球帽 | 球桿橫掛肩後 | 大方明亮的笑 | 橫 膝上／直 全身 |  |

**仍然接近、需要 Penny 判斷的地方（不宣稱已消除）：**

- 窗邊光有三位：Yuna（冷白漫射、極簡、併膝坐姿）、Miu（暖色窗光、咖啡館木頭、交疊腿坐姿）、Rin（黎明冷光＋暖燈、暗色、背影回眸）。Miu 這版從吧台改到窗邊座位，和 Yuna 更接近了；若 Penny 覺得太近，其中一位可以用替代方向。
- 坐姿有三位：Coco、Yuna、Miu；其餘九位站姿。
- 開懷大笑剩 Somi、Coco；Tammy、Yerin 是明亮笑容；Iris 改成甜笑。
- 棚拍三位：Somi（暖橘搭景）、Mia（霓虹電競）、Jia（灰色無縫），色彩與道具完全不同。
- 碰撞配對（Miu–Jia、Miu–Somi、Jia–Somi、Yerin–Rin）與 R2 目視相似（Somi–Tammy、Iris–Rainie）：只用拍攝調性拉開，不改臉、不換人；不宣稱能消除碰撞。每張只有一位，不違反同框規則。

## 4. 每位企劃

每位一個主推薦、一個替代方向。「參考照片」是第二階段素材頁既有的照片 ID，只用來認人與看氣質，**不是新成品、不會照抄**；新企劃的照片**尚未生成**。
prompt 是可直接使用的草稿，**尚未執行**；橫、直兩段的取景句依各自的取景設計寫成。

### 4.1 Iris Chen（陳芯語，22）｜河濱草地的黃金時段（第一階段建議）

**R1 修訂（姿態與細節）：**

- 姿勢改成單一姿態：背部斜向鏡頭、站定越肩回眸（取消「走向鏡頭＋回頭＋扭轉」）
- 表情改成甜笑（取消張口大笑），一手扶開襟、一手自然垂放
- 逆光加上畫面外反光板與柔光補臉；膚色只寫一次
- 取景重算：橫幅膝上、直幅全身（v1 的橫幅數字不成立）

- **與人設核對：** 主方向不變：金色戶外、短上衣＋短褲、甜笑，也是 Penny 喜歡的 iris-04。這版只修姿勢、補光與取景。
- **為什麼適合她：** 她的魅力是「不費力的好看」。把 iris-04 的回眸與夕陽拍成正式寫真：人站定、光從背後勾邊、臉用反光板補亮。
- **參考照片（既有）：** iris-04、iris-03
- **逐項檢查：** 隨拍感：v1「走向鏡頭＋回頭＋扭轉」像抓拍 → 改成站定回眸；道具遮身形：無；動作數量：改成一個姿態、一手扶開襟；穿搭完整度：平口上衣＋短褲＋開襟＋帆布鞋＋耳環，完整
- **舊版姿勢：** 前腳往前一步、重心在後腳，回頭時上身扭轉；右手把頭髮塞到耳後，左手自然垂放；針織外套下襬隨轉身擺動。

| 項目 | 內容 |
|---|---|
| 場景 | 台北河濱公園的開闊草地，傍晚太陽低，遠處一排柔綠樹與低矮公寓，草地與小徑空無一人。 |
| 服裝 | 米白羅紋平口短上衣、淺藍高腰牛仔短褲、燕麥色薄針織開襟滑落一側肩、白色低筒帆布鞋。 |
| 髮型／髮色 | 黑色柔順直髮自然垂放過肩。 |
| 配件 | 小金色圈耳環。 |
| 光線 | 主光：低角度夕陽在她身後左上，頭髮與肩線一圈暖色輪廓光。補光：畫面外前方的大反光板加柔光，讓臉曝光正確、清楚。整體暖金色調，太陽旁的天空可以過曝。 |
| 表情 | 甜甜的微笑，嘴唇微開，看鏡頭。 |
| 姿勢與雙手 | 站定，背部斜向鏡頭約 45 度，重心在後腳；越過肩膀回頭看鏡頭；一手輕扶肩上的開襟，另一手自然垂放。 |
| 甜美元素 | 回眸的甜笑、暖色夕陽、米白與淺藍的乾淨配色。 |
| 性感元素 | 平口上衣露出的肩背與腰線、牛仔短褲下的長腿、滑落一側的開襟。 |
| 替代方向 | 午後窗光的白色公寓：米白針織小可愛＋牛仔迷你裙，坐在窗邊木地板上，側光，甜而慵懶。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 膝上 | 全身 |
| 人物佔畫面高度 | 約 84% | 約 86% |
| 頭頂／手腳範圍 | 頭頂完整、雙手在框內，切在膝蓋下方 | 頭頂到腳完整，雙手在框內 |
| 留白位置 | 人物偏左，右側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 85mm／約 5.1 公尺 | 85mm／約 5.1 公尺 |
| 視野（寬×高，公尺） | 2.16×1.44 | 1.44×1.92 |
| 人物範圍高度（公尺） | 1.22 | 1.65 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框（約 1.85:1）要上下共裁約 19%：約剩大腿以上，頭頂留白變少但人物完整。 | 放進橫式半版直幅框（約 0.67:1）左右共裁約 11%：人物置中，不受影響。 |

| 風險 | 處理 |
|---|---|
| 逆光臉暗 | 寫明畫面外反光板與柔光補臉、測光給臉 |
| 膚色被夕陽拍偏 | 只寫一次她原本的白皙膚色，不堆疊形容詞 |
| 回頭角度過大造成脖子扭曲 | 背部斜向約 45 度，回頭幅度自然 |
| 太陽眩光蓋住臉 | 太陽放在左上、臉在右側 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone and black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, full chest and slim waist. She wears an off-white fitted ribbed tube top, high-waisted light-blue denim shorts, a thin oatmeal knit cardigan slipped off one shoulder, white low canvas sneakers and small gold hoop earrings. Setting: an open riverside lawn in a Taipei park in the late afternoon, a line of soft green trees and low distant apartment blocks far behind her, the lawn and the path empty. She stands still with her back angled about forty-five degrees to the camera and her weight on her back leg, looking back over her shoulder at the camera with a soft, sweet smile, lips slightly parted; one hand lightly holds the cardigan at her shoulder and the other arm hangs relaxed. Horizontal 3:2 frame, full-frame camera with an 85mm lens from about 5.1 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 84% of the frame height, standing left of centre with the sunlit lawn and soft trees filling the right side. Lighting: the low sun behind her and to the upper left draws a warm rim along her hair and shoulders; a large white reflector and a soft fill light just out of frame in front of her light her face evenly and correctly; warm golden tones overall, the sky near the sun allowed to clip. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone and black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, full chest and slim waist. She wears an off-white fitted ribbed tube top, high-waisted light-blue denim shorts, a thin oatmeal knit cardigan slipped off one shoulder, white low canvas sneakers and small gold hoop earrings. Setting: an open riverside lawn in a Taipei park in the late afternoon, a line of soft green trees and low distant apartment blocks far behind her, the lawn and the path empty. She stands still with her back angled about forty-five degrees to the camera and her weight on her back leg, looking back over her shoulder at the camera with a soft, sweet smile, lips slightly parted; one hand lightly holds the cardigan at her shoulder and the other arm hangs relaxed. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 5.1 metres, camera at her navel height; full length from her sneakers to a little above her head, she fills about 86% of the frame height, centred with soft lawn under her feet. Lighting: the low sun behind her and to the upper left draws a warm rim along her hair and shoulders; a large white reflector and a soft fill light just out of frame in front of her light her face evenly and correctly; warm golden tones overall, the sky near the sun allowed to clip. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.2 Luna Tanaka（田中ひな，20）｜京都老宅後院的紫陽花

**R1 修訂（姿態與細節）：**

- 取消「風吹掀裙、手按裙襬」，性感改由方領、合身腰線、迷你裙長與腿部線條呈現
- 表情改成單一瞬間的安靜微笑（取消「先垂眼再抬眼」）
- 補光改為畫面外反光板；光斑只落在背景
- 取景重算：橫幅膝上、直幅全身

- **與人設核對：** 主方向不變：花園、淺色小洋裝、柔和日光。她 20 歲、童顏：用合身腰線、低跟涼鞋、細金項鍊等成人線索；不用白襪、娃娃裝。
- **為什麼適合她：** 她是「住在美麗白日夢裡的人」。老宅庭院、白紫陽花、淺綠蕾絲洋裝，用剪裁與站姿呈現她的曲線，不靠風吹的小意外。
- **參考照片（既有）：** luna-10、luna-01
- **逐項檢查：** 隨拍感：v1 的「風吹掀裙＋按住」像抓拍瞬間 → 改成站定的姿態；道具遮身形：無；動作數量：v1 有按裙、摸鎖骨、垂眼再抬眼三件事 → 改成一手扶籬笆、一手自然垂放；穿搭完整度：洋裝＋涼鞋＋項鍊＋髮夾，完整
- **舊版姿勢：** 站在石板路上，重心在右腳、左膝微彎；一手輕按大腿處的裙襬（風在吹），另一手放在鎖骨。

| 項目 | 內容 |
|---|---|
| 場景 | 京都風老木造町家的後院：青苔地、石板小徑、低矮木籬笆旁一整排白色紫陽花，頭上有楓樹枝。 |
| 服裝 | 淺鼠尾草綠棉質蕾絲迷你洋裝（方領、短袖、合身腰線）、米色低跟繫帶涼鞋。 |
| 髮型／髮色 | 黑色細直髮，中分下巴長度的鮑伯，髮尾貼著下顎。 |
| 配件 | 細金鍊項鍊、耳上一支珍珠髮夾。 |
| 光線 | 主光：明亮陰天的大面積柔光。補光：畫面外的白色反光板，讓臉乾淨均勻。楓葉縫隙的光斑只落在背景的小徑與花上，不落在臉上。清新的綠與白。 |
| 表情 | 安靜的淺笑，看鏡頭。 |
| 姿勢與雙手 | 站在石板路上，重心在右腳、左膝微彎向前，露出腿部線條；一手輕放在木籬笆上，另一手自然垂放。 |
| 甜美元素 | 安靜的淺笑、白紫陽花、淺綠與白。 |
| 性感元素 | 方領與合身腰線、迷你裙長與微彎膝蓋的腿部線條、她的身材比例。 |
| 替代方向 | 雨後的木造緣側：白色蕾絲細肩洋裝＋薄針織外套，坐在木廊邊、腳垂向庭院，晨間柔光。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 膝上 | 全身 |
| 人物佔畫面高度 | 約 86% | 約 86% |
| 頭頂／手腳範圍 | 頭頂完整、雙手在框內，切在膝蓋下方 | 頭頂到腳完整，雙手在框內 |
| 留白位置 | 人物偏右，左側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 85mm／約 4.8 公尺 | 85mm／約 4.9 公尺 |
| 視野（寬×高，公尺） | 2.03×1.36 | 1.38×1.84 |
| 人物範圍高度（公尺） | 1.16 | 1.59 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框（約 1.85:1）要上下共裁約 19%：約剩大腿以上，頭頂留白變少但人物完整。 | 放進橫式半版直幅框（約 0.67:1）左右共裁約 11%：人物置中，不受影響。 |

| 風險 | 處理 |
|---|---|
| 童顏＋花園＋小洋裝顯小 | 寫明 adult、合身腰線、低跟涼鞋與首飾；不用白襪與娃娃裝 |
| 光斑落在臉上 | 寫明光斑只在背景 |
| 地名寫「京都」生出錯的地標 | 只寫環境元素，不點名地標 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 20-year-old adult Japanese woman with her natural fair skin tone and black fine straight hair in a centre-parted, chin-length bob, the ends brushing her jaw. Petite curvy figure, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup, full chest and slim waist. She wears a pale sage-green cotton lace mini dress with a square neckline, short sleeves and a fitted waist, cream low block-heel strappy sandals, a thin gold chain necklace and a pearl hair pin above one ear. Setting: a quiet garden behind an old wooden Kyoto-style townhouse, moss ground, a stone path, white hydrangeas in bloom along a low wooden fence, maple branches overhead. She stands on the stone path with her weight on her right leg and her left knee softly bent forward, one hand resting lightly on the top of the wooden fence and the other relaxed at her side, looking at the camera with a small, quiet smile. Horizontal 3:2 frame, full-frame camera with an 85mm lens from about 4.8 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 86% of the frame height, right of centre with the hydrangea-lined path and fence on the left. Lighting: bright overcast daylight as one large soft source from above and in front, with a white reflector just out of frame so her face is clean and evenly lit; soft dappled light through the maple leaves falls only on the path and hydrangeas behind her; fresh green and white tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 20-year-old adult Japanese woman with her natural fair skin tone and black fine straight hair in a centre-parted, chin-length bob, the ends brushing her jaw. Petite curvy figure, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup, full chest and slim waist. She wears a pale sage-green cotton lace mini dress with a square neckline, short sleeves and a fitted waist, cream low block-heel strappy sandals, a thin gold chain necklace and a pearl hair pin above one ear. Setting: a quiet garden behind an old wooden Kyoto-style townhouse, moss ground, a stone path, white hydrangeas in bloom along a low wooden fence, maple branches overhead. She stands on the stone path with her weight on her right leg and her left knee softly bent forward, one hand resting lightly on the top of the wooden fence and the other relaxed at her side, looking at the camera with a small, quiet smile. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 4.9 metres, camera at her navel height; full length from her sandals to a little above her head, she fills about 86% of the frame height, centred with maple branches across the top edge. Lighting: bright overcast daylight as one large soft source from above and in front, with a white reflector just out of frame so her face is clean and evenly lit; soft dappled light through the maple leaves falls only on the path and hydrangeas behind her; fresh green and white tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.3 Somi Oh（오소미，24）｜暖橘色的復古棚景

**R1 修訂（主方向）：**舊版標題「暖橘色的復古小吃店棚景」。

- 主推薦取消「舉炸雞」：臉、腰線與姿態優先
- 保留暖橘復古棚景；炸雞只放在橫幅右緣、失焦的一小盤，直幅不放
- 服裝改成針織短開襟＋高腰針織短裙（取消格紋百褶，避免制服感）
- 原本的「手拿炸雞」改列為備選拍法
- 取景重算：橫幅膝上、直幅全身

- **與人設核對：** 保留主管要的暖橘復古棚、漂亮針織裙裝、爽朗笑容。她是美食人設，但不必每張都在吃：食物只當場景邊緣的小線索。
- **為什麼適合她：** 她最好看的是爽朗的笑和健康的曲線。暖橘磁磚、紅色高腳椅、一盞吊燈，讓她站著大笑，畫面主角是她，不是食物。
- **參考照片（既有）：** somi-02、somi-01
- **舊版姿勢：** 側坐高腳椅、雙腿在膝上交疊，一手肘靠在吧台；另一手把一隻炸雞腿舉在臉頰旁；百褶裙在椅面上散開。

| 項目 | 內容 |
|---|---|
| 場景 | 搭景的韓式復古小吃店：暖橘色磁磚吧台、一排紅色皮面高腳椅、一盞暖色吊燈，整齊乾淨。橫幅右緣的吧台末端有一小盤失焦的金黃炸雞；直幅不放食物。 |
| 服裝 | 奶油色合身羅紋針織短開襟（扣起）、高腰鏽橘色針織迷你裙、棕色有跟皮革樂福鞋。 |
| 髮型／髮色 | 明亮蜜橘棕的韓式狼尾層次剪。 |
| 配件 | 紅色琺瑯小愛心耳環。 |
| 光線 | 主光：前右方頭部高度的大型暖色柔光箱。補光：畫面外左側柔光，臉均勻。吊燈在頭髮上加一點暖光。暖橘與奶油色調。 |
| 表情 | 月牙眼大笑、露出酒窩，看鏡頭。 |
| 姿勢與雙手 | 站著，一側臀部輕靠磁磚吧台，重心在後腳、前腳輕交叉；一手放在吧台邊緣，另一手把頭髮塞到耳後（她的招牌動作）。 |
| 甜美元素 | 月牙眼與酒窩的大笑、暖色調。 |
| 性感元素 | 短版針織收出的腰線、高腰短裙與交叉的腿、她的曲線身材。 |
| 替代方向 | 炸雞拍法（備選）：同一棚景，側坐高腳椅、手拿一隻炸雞腿舉在臉旁，咬下去前的停頓——保留她的美食人設，但不當主推薦。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 膝上 | 全身 |
| 人物佔畫面高度 | 約 86% | 約 85% |
| 頭頂／手腳範圍 | 頭頂完整、雙手在框內，切在膝蓋下方 | 頭頂到腳完整，雙手在框內 |
| 留白位置 | 人物偏左，右側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 70mm／約 4.1 公尺 | 70mm／約 4.2 公尺 |
| 視野（寬×高，公尺） | 2.11×1.41 | 1.44×1.92 |
| 人物範圍高度（公尺） | 1.21 | 1.64 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框（約 1.85:1）要上下共裁約 19%：約剩大腿以上，頭頂留白變少但人物完整。 | 放進橫式半版直幅框（約 0.67:1）左右共裁約 11%：人物置中，不受影響。 |

| 風險 | 處理 |
|---|---|
| 棚景太像真實餐廳、雜物多 | 寫明整齊、只有吧台、高腳椅與吊燈 |
| 炸雞搶戲或出現包裝假字 | 只在橫幅右緣、失焦、放在盤子上，不寫包裝 |
| 與 Miu、Jia 的碰撞紀錄 | 暖橘高飽和、站姿大笑、蜜橘狼尾；不改臉，不宣稱能消除碰撞 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a fitted cream rib-knit cropped cardigan buttoned up, a high-waisted rust-orange knit mini skirt, brown leather heeled loafers and small red enamel heart earrings. Setting: a studio-built retro Korean snack-bar set with a warm orange tiled counter, a row of red vinyl bar stools and a warm pendant lamp, everything tidy. She stands leaning one hip lightly against the tiled counter, weight on her back leg with the front leg crossed in front, one hand resting on the counter edge and the other tucking her hair behind her ear, laughing openly at the camera with her eyes curved into crescents and dimples showing. Horizontal 3:2 frame, full-frame camera with a 70mm lens from about 4.1 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 86% of the frame height, left of centre with the orange counter running to the right and a small plate of golden fried chicken resting soft and out of focus at the right edge. Lighting: a large warm softbox key from the front right at head height and a soft fill from the left just out of frame light her face evenly; the pendant lamp adds a warm glow on her hair; warm orange and cream tones throughout. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a fitted cream rib-knit cropped cardigan buttoned up, a high-waisted rust-orange knit mini skirt, brown leather heeled loafers and small red enamel heart earrings. Setting: a studio-built retro Korean snack-bar set with a warm orange tiled counter, a row of red vinyl bar stools and a warm pendant lamp, everything tidy. She stands leaning one hip lightly against the tiled counter, weight on her back leg with the front leg crossed in front, one hand resting on the counter edge and the other tucking her hair behind her ear, laughing openly at the camera with her eyes curved into crescents and dimples showing. Vertical 3:4 frame, full-frame camera with a 70mm lens from about 4.2 metres, camera at her navel height; full length from her loafers to a little above her head, she fills about 85% of the frame height, centred with the pendant lamp just inside the top edge and no food in the frame. Lighting: a large warm softbox key from the front right at head height and a soft fill from the left just out of frame light her face evenly; the pendant lamp adds a warm glow on her hair; warm orange and cream tones throughout. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.4 Coco Wu（吳可可，20）｜週末飯店泳池的薄荷綠

**R1 修訂（姿態與細節）：**

- 動作簡化：取消踢水濺花與罩衫被風掀起，只保留「坐池邊、往後撐、歪頭大笑」
- 補光改為畫面外反光板；膚色只寫一次
- 取景重算：橫幅較遠、直幅較近，兩張都到水面

- **與人設核對：** 主方向不變：週末泳池、薄荷綠與淺紫。她 20 歲、大學生人設：不用校園或制服元素，寫明成人。泳裝尺度與第二階段的泳裝參考相同，交印前需確認廠商接受範圍。
- **為什麼適合她：** 她的魅力是對自己柔軟曲線的自在與大笑。泳池、薄荷綠比基尼、透膚淺紫罩衫，清透又甜。
- **參考照片（既有）：** coco-21、coco-08
- **逐項檢查：** 隨拍感：v1 踢水濺花、罩衫被風掀起像抓拍 → 拿掉；道具遮身形：罩衫落在肩後，不遮身形；動作數量：只剩坐池邊往後撐＋歪頭大笑；穿搭完整度：比基尼＋罩衫＋髮夾＋腳鍊，完整
- **舊版姿勢：** 坐在池邊、兩條小腿泡在水裡，身體往後用雙手撐地；一腳踢水濺起水花；透膚罩衫被風掀起。

| 項目 | 內容 |
|---|---|
| 場景 | 週末早上的度假飯店泳池：淺米色石材地磚、清澈的湖水綠池水、遠處收起的白色陽傘，池畔乾淨無人。 |
| 服裝 | 薄荷綠羅紋三角比基尼上衣與同色側綁下著（完整遮蔽）、敞開的淺紫透膚短袖罩衫（落在肩後）、腳踝細金鍊。 |
| 髮型／髮色 | 深棕長波浪捲髮、蓬鬆空氣瀏海，髮尾微濕。 |
| 配件 | 白色雛菊髮夾。 |
| 光線 | 主光：晚上午的陽光從左前上方。補光：畫面外的大反光板補亮臉與身體的陰影，臉均勻。池水在腿上留下淡淡的水光。清爽的夏日色彩。 |
| 表情 | 歪頭、瞇成一條線的大笑、露出酒窩。 |
| 姿勢與雙手 | 坐在池邊、兩條小腿泡在水裡，身體往後用雙手撐地。 |
| 甜美元素 | 瞇眼大笑、酒窩、雛菊髮夾、粉嫩配色。 |
| 性感元素 | 比基尼與透膚罩衫、往後撐的姿勢展現曲線、濕髮與水光。 |
| 替代方向 | 清晨的乾淨房間：奶油白針織開襟＋淺紫細肩小可愛＋百褶迷你裙，坐在床邊，窗光；背景整理乾淨。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 坐姿到水面 | 坐姿到水面 |
| 人物佔畫面高度 | 約 81% | 約 81% |
| 頭頂／手腳範圍 | 頭頂完整、撐地的雙手在框內，小腿在水中 | 頭頂完整、撐地的雙手在框內，小腿在水中 |
| 留白位置 | 人物偏左，右側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 70mm／約 3.6 公尺 | 70mm／約 2.7 公尺 |
| 視野（寬×高，公尺） | 1.85×1.23 | 0.93×1.23 |
| 人物範圍高度（公尺） | 1.0 | 1.0 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框要上下共裁約 19%：約剩胸口到腰的位置以上，水面會被裁掉大半。 | 放進橫式半版直幅框左右共裁約 11%：撐地的手會貼近邊緣。 |

| 風險 | 處理 |
|---|---|
| 泳裝遮蔽與走光 | 寫明完整遮蔽、坐姿；生成後逐張檢查，比照第二階段的遮蔽規則 |
| 水下腳掌與撐地手指變形 | 小腿入水、腳掌不必看清；檢查手 |
| 校園甜心＋泳裝顯小 | 寫明 adult、不用校園元素 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 20-year-old adult Taiwanese woman with her natural fair skin tone, deep dimples when she smiles and dark-brown long wavy hair with soft wispy bangs, the ends slightly wet. Petite curvy figure, 158 cm tall, bust 89 cm, waist 56 cm, hips 86 cm, E cup, full chest and slim waist. She wears a mint-green ribbed triangle bikini top with matching side-tie bottoms that fully cover, an open sheer lilac short-sleeve cover-up shirt resting off her shoulders, a white daisy hair clip and a thin gold anklet. Setting: a resort hotel pool on a weekend morning, pale cream stone tiles, clear turquoise water, white umbrellas folded in the distance, the pool deck empty. She sits on the pool edge with both lower legs in the water, leaning back on her hands, head tilted, laughing with her eyes squeezed into crescents and dimples showing. Horizontal 3:2 frame, full-frame camera with a 70mm lens from about 3.6 metres, camera at her seated chest height; framed from the waterline to a little above her head, she fills about 81% of the frame height, left of centre with the open turquoise pool on the right. Lighting: bright late-morning sun from high front-left; a large white reflector just out of frame fills the shadows on her face and body so her face is evenly lit; the turquoise water adds soft aqua reflections on her legs; clear, fresh summer colours. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 20-year-old adult Taiwanese woman with her natural fair skin tone, deep dimples when she smiles and dark-brown long wavy hair with soft wispy bangs, the ends slightly wet. Petite curvy figure, 158 cm tall, bust 89 cm, waist 56 cm, hips 86 cm, E cup, full chest and slim waist. She wears a mint-green ribbed triangle bikini top with matching side-tie bottoms that fully cover, an open sheer lilac short-sleeve cover-up shirt resting off her shoulders, a white daisy hair clip and a thin gold anklet. Setting: a resort hotel pool on a weekend morning, pale cream stone tiles, clear turquoise water, white umbrellas folded in the distance, the pool deck empty. She sits on the pool edge with both lower legs in the water, leaning back on her hands, head tilted, laughing with her eyes squeezed into crescents and dimples showing. Vertical 3:4 frame, full-frame camera with a 70mm lens from about 2.7 metres, camera at her seated chest height; framed from the waterline to a little above her head, she fills about 81% of the frame height, centred with the water across the bottom of the frame. Lighting: bright late-morning sun from high front-left; a large white reflector just out of frame fills the shadows on her face and body so her face is evenly lit; the turquoise water adds soft aqua reflections on her legs; clear, fresh summer colours. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.5 Mia Huang（黃米亞，22）｜粉紫霓虹的電競時尚棚

**R1 修訂（主方向）：**

- 姿勢改成簡潔站姿：站在電競椅旁，一手扶椅背、一手插腰（取消腳勾扶手＋扭身＋拉耳機）
- 耳機只是掛在脖子上的小配件，不遮臉、不拿在手上
- 保留粉紫霓虹輪廓光；臉用中性柔光箱打出自然明亮的膚色
- 桌子與鍵盤拿掉，畫面只剩椅子與霓虹牆
- 取景重算：橫幅膝上、直幅全身

- **與人設核對：** 保留電競風時尚棚與粉紫輪廓光；姿勢改成簡潔、乾淨，像棚拍而不是直播截圖。
- **為什麼適合她：** 她的工作就是被看。把直播間的 RGB 光變成棚拍的輪廓光，臉用乾淨的白光打；站姿簡單，讓俏皮的表情和身形成為重點。
- **參考照片（既有）：** mia-11、mia-02
- **舊版姿勢：** 橫坐在電競椅上，一腳勾在扶手、另一腳踩地，上身扭向鏡頭；一手把耳機從脖子上拉開，另一手放在膝上；帽 T 下襬擺動。

| 項目 | 內容 |
|---|---|
| 場景 | 乾淨的攝影棚，布置成電競場景：一張白色電競椅、深炭灰牆上幾支直立的洋紅與紫色霓虹燈管，畫面裡沒有其他東西。 |
| 服裝 | 黑色短版拉鍊帽 T（敞開）、淺紫羅紋短版背心、黑色高腰短褲、白色過膝襪、白色厚底球鞋。 |
| 髮型／髮色 | 灰棕色長髮鬆散大波浪，左側臉旁一片粉紅 money piece 挑染。 |
| 配件 | 細白耳機掛在脖子上（小配件）、細銀手鍊。 |
| 光線 | 主光：相機左側的大型中性柔光箱，臉乾淨、膚色自然明亮。輪廓：身後的洋紅與紫色霓虹在頭髮與肩膀邊緣留下粉紫輪廓光。背景沉到深炭灰。 |
| 表情 | 俏皮眨眼、挑逗的半笑。 |
| 姿勢與雙手 | 站在電競椅旁，重心在一隻腳；一手放在椅背頂端，另一手插腰。 |
| 甜美元素 | 眨眼、二次元感的眼妝、粉紅挑染。 |
| 性感元素 | 短版背心露腰、短褲與過膝襪之間的腿部線條、插腰的身形。 |
| 替代方向 | 白天的新竹咖啡座：白色短版 T＋牛仔短褲＋灰色帽 T 綁在腰間，戶外座位、午後側光，去電競化。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 膝上 | 全身 |
| 人物佔畫面高度 | 約 85% | 約 85% |
| 頭頂／手腳範圍 | 頭頂完整、雙手在框內，切在膝蓋下方 | 頭頂到腳完整，雙手在框內 |
| 留白位置 | 人物偏左，右側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 70mm／約 4.1 公尺 | 70mm／約 4.2 公尺 |
| 視野（寬×高，公尺） | 2.11×1.41 | 1.44×1.92 |
| 人物範圍高度（公尺） | 1.2 | 1.64 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框（約 1.85:1）要上下共裁約 19%：約剩大腿以上，頭頂留白變少但人物完整。 | 放進橫式半版直幅框（約 0.67:1）左右共裁約 11%：人物置中，不受影響。 |

| 風險 | 處理 |
|---|---|
| 霓虹讓臉變紫、變髒 | 中性柔光箱是臉的主光，霓虹只當輪廓 |
| 耳機或椅子出現品牌字 | 寫素白耳機、白色電競椅，不寫品牌 |
| 過膝襪＋電競感顯小 | 寫明 adult，不加貓耳等幼化道具 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone and big expressive eyes with soft anime-inspired makeup, softly winged liner and glossy tinted lips, long ash-brown hair in loose waves with a pastel-pink money-piece highlight framing the left side of her face. Curvy figure, 160 cm tall, bust 91 cm, waist 57 cm, hips 88 cm, F cup, full chest and slim waist. She wears a black cropped zip-up hoodie worn open over a lilac ribbed crop tank, black high-waisted shorts, white over-the-knee socks, chunky white platform sneakers, a slim plain white headset resting around her neck and a thin silver chain bracelet. Setting: a clean photo studio styled as a gaming set, a white gaming chair and vertical magenta and violet neon tubes on a dark charcoal wall behind, nothing else in the frame. She stands beside the gaming chair with her weight on one leg, one hand resting on top of the chair back and the other on her hip, giving a playful wink with a teasing half-smile. Horizontal 3:2 frame, full-frame camera with a 70mm lens from about 4.1 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 85% of the frame height, left of centre with the white chair and neon-lit wall on the right. Lighting: a large neutral softbox key from camera-left lights her face cleanly with natural, bright skin tones; the magenta and violet neon tubes behind her draw a soft pink-purple rim along her hair and shoulders; the background falls to deep charcoal. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone and big expressive eyes with soft anime-inspired makeup, softly winged liner and glossy tinted lips, long ash-brown hair in loose waves with a pastel-pink money-piece highlight framing the left side of her face. Curvy figure, 160 cm tall, bust 91 cm, waist 57 cm, hips 88 cm, F cup, full chest and slim waist. She wears a black cropped zip-up hoodie worn open over a lilac ribbed crop tank, black high-waisted shorts, white over-the-knee socks, chunky white platform sneakers, a slim plain white headset resting around her neck and a thin silver chain bracelet. Setting: a clean photo studio styled as a gaming set, a white gaming chair and vertical magenta and violet neon tubes on a dark charcoal wall behind, nothing else in the frame. She stands beside the gaming chair with her weight on one leg, one hand resting on top of the chair back and the other on her hip, giving a playful wink with a teasing half-smile. Vertical 3:4 frame, full-frame camera with a 70mm lens from about 4.2 metres, camera at her navel height; full length from her sneakers to a little above her head, she fills about 85% of the frame height, centred with the neon tubes rising behind her. Lighting: a large neutral softbox key from camera-left lights her face cleanly with natural, bright skin tones; the magenta and violet neon tubes behind her draw a soft pink-purple rim along her hair and shoulders; the background falls to deep charcoal. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.6 Yuna Kim（김하은，21）｜首爾公寓的極簡窗光

**R1 修訂（姿態與細節）：**

- 手部簡化：一手放在緞面裙上、一手放在長凳上（取消「手碰窗簾＋窗簾飄動」）
- 補光改為畫面外白色反光卡
- 取景重算：橫幅坐姿全身（50mm）、直幅坐姿膝上（85mm）

- **與人設核對：** 主方向不變：極簡窗光、針織＋緞面裙、安靜氣質。和 Rin 的緞面晨袍分得開（Yuna 是白天、極簡、正面坐姿）。
- **為什麼適合她：** 她的氣質是「清冷、乾淨」。大窗、白紗簾、一張長凳，讓臉成為畫面的重點。
- **參考照片（既有）：** yuna-06、yuna-01
- **逐項檢查：** 隨拍感：低，本來就是擺好的坐姿；道具遮身形：無；動作數量：v1 手碰窗簾＋窗簾飄動 → 改成兩手各放裙上與長凳；穿搭完整度：開襟＋緞面裙＋髮夾＋項鍊；赤腳符合室內場景
- **舊版姿勢：** 側坐在窗邊長凳，雙膝併攏朝向鏡頭；一手放在緞面裙上，另一手輕碰窗簾邊緣；窗簾在微風中飄動。

| 項目 | 內容 |
|---|---|
| 場景 | 極簡白色首爾公寓：大窗配白色薄紗簾、淺橡木地板、一張低矮白色長凳，房間裡沒有其他東西。 |
| 服裝 | 柔灰細針織短版開襟（扣中間一顆、滑落一側肩）、象牙白緞面斜裁中長裙、赤腳。 |
| 髮型／髮色 | 深棕到黑的自然波浪、鎖骨長度、空氣感、八字瀏海。 |
| 配件 | 耳上一支紅色櫻桃髮夾、細銀鍊。 |
| 光線 | 主光：早晨日光透過白紗簾，從相機右側大面積柔光。補光：畫面外左側白色反光卡，臉的陰影面保持清楚。乾淨的白與柔灰。 |
| 表情 | 平靜、幾乎看不出來的微笑，眼神穩定看鏡頭。 |
| 姿勢與雙手 | 側坐在窗邊長凳，雙膝併攏朝向鏡頭；一手放在緞面裙上，另一手放在長凳上。 |
| 甜美元素 | 櫻桃髮夾、溫柔的微笑、柔軟的針織。 |
| 性感元素 | 開襟滑落露肩、緞面裙的光澤與身體線條。 |
| 替代方向 | 清晨的空屋頂：白色細肩背心＋灰色迷你格紋裙＋短版外套，站在欄杆邊，藍調時刻的冷光。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 坐姿全身 | 坐姿膝上 |
| 人物佔畫面高度 | 約 86% | 約 84% |
| 頭頂／手腳範圍 | 坐姿頭頂到腳完整，雙手在框內 | 坐姿頭頂完整、雙手在框內，從膝蓋以上 |
| 留白位置 | 人物偏右，左側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 50mm／約 3.2 公尺 | 85mm／約 2.6 公尺 |
| 視野（寬×高，公尺） | 2.3×1.54 | 0.73×0.98 |
| 人物範圍高度（公尺） | 1.32 | 0.82 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框要上下共裁約 19%：坐姿全身會切到腳；若最後選大照片框，改用坐姿膝上。 | 放進橫式半版直幅框左右共裁約 11%：人物置中，不受影響。 |

| 風險 | 處理 |
|---|---|
| 窗戶過曝吃掉臉的輪廓 | 測光給臉、寫明反光卡補光 |
| 緞面裙坐姿皺褶怪異 | 生成後檢查；不行改站姿靠窗 |
| 房間太空像假棚 | 保留長凳與木地板的細節 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 21-year-old adult Korean woman with her natural fair skin tone and large bright double-eyelid eyes, dark-brown natural wavy hair at collarbone length with airy volume and curtain bangs, a small red cherry hair clip above one ear. Slim figure, 168 cm tall, bust 84 cm, waist 58 cm, hips 89 cm, C cup. She wears a soft grey fine-knit cropped cardigan buttoned at the middle and sliding off one shoulder, an ivory satin bias-cut midi slip skirt, bare feet and a thin silver chain necklace. Setting: a minimalist white Seoul apartment with a large window and sheer white curtains, a pale oak floor and one low white bench, nothing else in the room. She sits sideways on the bench by the window with her knees together and angled toward the camera, one hand resting on the satin skirt and the other on the bench beside her, facing the camera with a calm, barely-there smile. Horizontal 3:2 frame, full-frame camera with a 50mm lens from about 3.2 metres, camera at her seated chest height; full length seated, from her bare feet to a little above her head, she fills about 86% of the frame height, right of centre with the bright window and curtains on the left. Lighting: soft morning daylight through the sheer curtains from camera-right as a large diffused key, with a white bounce card just out of frame on the left so the shadow side of her face stays open; clean whites and soft greys. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 21-year-old adult Korean woman with her natural fair skin tone and large bright double-eyelid eyes, dark-brown natural wavy hair at collarbone length with airy volume and curtain bangs, a small red cherry hair clip above one ear. Slim figure, 168 cm tall, bust 84 cm, waist 58 cm, hips 89 cm, C cup. She wears a soft grey fine-knit cropped cardigan buttoned at the middle and sliding off one shoulder, an ivory satin bias-cut midi slip skirt, bare feet and a thin silver chain necklace. Setting: a minimalist white Seoul apartment with a large window and sheer white curtains, a pale oak floor and one low white bench, nothing else in the room. She sits sideways on the bench by the window with her knees together and angled toward the camera, one hand resting on the satin skirt and the other on the bench beside her, facing the camera with a calm, barely-there smile. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 2.6 metres, camera at her seated chest height; framed from her knees to a little above her head, she fills about 84% of the frame height, centred with the top of the window frame near the top edge. Lighting: soft morning daylight through the sheer curtains from camera-right as a large diffused key, with a white bounce card just out of frame on the left so the shadow side of her face stays open; clean whites and soft greys. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.7 Tammy Chou（周語彤，24）｜都會白色建築的熱粉色洋裝（型錄外拍）

**R1 修訂（姿態與細節）：**

- 取消「走下階梯＋插腰＋撥髮＋頭髮彈動」，改成站定在階梯上：一手插腰、一手拉包包肩帶
- 硬光加上畫面外反光板柔化臉上陰影
- 取景重算：橫幅全身 70mm（約 5.9 公尺）、直幅膝上

- **與人設核對：** 主方向不變：都會白色建築、熱粉色貼身洋裝，像一張型錄外拍；用白天熱粉與 Rainie 的夜景血紅分開。
- **為什麼適合她：** 她的工作就是「把衣服穿到讓人想買」。白色建築、晴天、一件飽和的熱粉洋裝，站定就是一張乾淨明亮的型錄照。
- **參考照片（既有）：** tammy-08、tammy-01
- **逐項檢查：** 隨拍感：v1 走下階梯像街拍抓拍 → 改成站定；道具遮身形：包包小、背在肩上，不遮；動作數量：v1 走路＋插腰＋撥髮＋頭髮彈動 → 改成插腰＋拉肩帶；穿搭完整度：洋裝＋高跟鞋＋包＋耳環，完整
- **舊版姿勢：** 走下階梯、朝鏡頭走來：重心在後腳，前腳正要踏到下一階；一手插腰，另一手把頭髮往後撥；大波浪隨步伐彈動。

| 項目 | 內容 |
|---|---|
| 場景 | 現代白色建築外觀，晴天：寬大的清水混凝土階梯、身後一面平滑的白色弧形牆，階梯上沒有其他人。 |
| 服裝 | 熱粉色方領羅紋針織貼身迷你洋裝、白色尖頭露跟鞋、小型白色硬挺素面肩背包。 |
| 髮型／髮色 | 奶茶金棕大波浪長捲髮、蓬鬆有空氣感，臉側一片淺色 money piece 挑染。 |
| 配件 | 金色圈耳環。 |
| 光線 | 主光：晴天硬光從右前上方，階梯邊緣有清楚的斜線陰影。補光：畫面外的大反光板柔化臉上陰影，臉均勻。熱粉對白牆與淡藍灰陰影。 |
| 表情 | 明亮的笑容，看鏡頭。 |
| 姿勢與雙手 | 站在階梯上、身體微側面向鏡頭，重心在後腳、前腳踩在低一階；一手插腰，另一手拉著肩上的包包肩帶。 |
| 甜美元素 | 明亮的笑、蓬鬆的長捲髮、熱粉色。 |
| 性感元素 | 貼身針織洋裝的曲線、方領、長腿與高跟鞋。 |
| 替代方向 | 白色無縫棚的型錄風：淺色牛仔外套披肩＋白色貼身針織洋裝，高亮均勻棚光。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 全身 | 膝上 |
| 人物佔畫面高度 | 約 86% | 約 85% |
| 頭頂／手腳範圍 | 頭頂到腳完整，雙手在框內 | 頭頂完整、雙手在框內，切在膝蓋下方 |
| 留白位置 | 人物偏左，右側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 70mm／約 5.7 公尺 | 70mm／約 3.1 公尺 |
| 視野（寬×高，公尺） | 2.93×1.95 | 1.06×1.42 |
| 人物範圍高度（公尺） | 1.68 | 1.2 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框要上下共裁約 19%：全身會切到腳或頭頂；若最後選大照片框，這張要改拍膝上。 | 放進橫式半版直幅框左右共裁約 11%：人物置中，不受影響。 |

| 風險 | 處理 |
|---|---|
| 硬光在臉上留下深陰影 | 寫明反光板補光 |
| 高跟鞋＋階梯的腳部結構錯誤 | 站定、前腳踩低一階；生成後放大檢查 |
| 包包出現 logo 或文字 | 寫素面、無標誌 |
| 與 Rainie 太像 | 白天、熱粉、白色建築 vs 夜景血紅緞面 |
| 與 Somi 的 R2 目視相似紀錄 | 冷白建築與熱粉；不改臉，不宣稱能消除相似 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, round almond eyes with visible aegyo-sal, shimmer eyeshadow and jelly-glossy lips, long voluminous big-wave hair in milk-tea golden brown with light money-piece highlights at the front. Curvy figure, 160 cm tall, bust 90 cm, waist 57 cm, hips 89 cm, E cup, full chest and slim waist. She wears a fitted hot-pink square-neck rib-knit mini dress, white pointed slingback heels, a small structured plain white shoulder bag and gold hoop earrings. Setting: a modern white building exterior on a clear day, a wide concrete staircase with clean geometric shadows and a smooth white curved wall behind, the steps empty. She stands on the staircase facing the camera at a slight angle, weight on her back leg with the front foot resting one step lower, one hand on her hip and the other holding the strap of the bag at her shoulder, smiling brightly at the camera. Horizontal 3:2 frame, full-frame camera with a 70mm lens from about 5.7 metres, camera at her navel height; full length from her heels to a little above her head, she fills about 86% of the frame height, left of centre with the staircase and curved white wall forming clean lines on the right. Lighting: clear sun from high front-right casting crisp diagonal stair shadows; a large white reflector just out of frame softens the shadows on her face so it is evenly lit; saturated hot pink against clean white and soft blue-grey shade. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, round almond eyes with visible aegyo-sal, shimmer eyeshadow and jelly-glossy lips, long voluminous big-wave hair in milk-tea golden brown with light money-piece highlights at the front. Curvy figure, 160 cm tall, bust 90 cm, waist 57 cm, hips 89 cm, E cup, full chest and slim waist. She wears a fitted hot-pink square-neck rib-knit mini dress, white pointed slingback heels, a small structured plain white shoulder bag and gold hoop earrings. Setting: a modern white building exterior on a clear day, a wide concrete staircase with clean geometric shadows and a smooth white curved wall behind, the steps empty. She stands on the staircase facing the camera at a slight angle, weight on her back leg with the front foot resting one step lower, one hand on her hip and the other holding the strap of the bag at her shoulder, smiling brightly at the camera. Vertical 3:4 frame, full-frame camera with a 70mm lens from about 3.1 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 85% of the frame height, centred with the diagonal stair shadows behind her. Lighting: clear sun from high front-right casting crisp diagonal stair shadows; a large white reflector just out of frame softens the shadows on her face so it is evenly lit; saturated hot pink against clean white and soft blue-grey shade. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.8 Rin Ayase（綾瀨凜，25）｜黎明公寓的祖母綠緞袍

**R1 修訂（姿態與細節）：**

- 保留越肩回眸這一個主要姿態；取消「緞面下襬擺動」
- 加上畫面外柔光補臉；冷色天光＋暖色檯燈是這個場景本身的光，不是全組規則
- 取景重算：橫幅大腿中段以上、直幅膝上（70mm）

- **與人設核對：** 主方向不變：與 Penny 喜歡的 rin-04 一致，也符合她的「下班後清晨」支柱。和 Yerin 的碰撞：暗色室內黎明 vs Yerin 的明亮戶外。
- **為什麼適合她：** 銀座下班後的清晨，是她私下安靜的那一面。緞面、裸肩、回眸，把 rin-04 的感覺拍成正式的大片。
- **參考照片（既有）：** rin-04、rin-01
- **逐項檢查：** 隨拍感：低，擺好的回眸；道具遮身形：無；動作數量：保留回眸＋兩手位置；拿掉下襬擺動；穿搭完整度：晨袍是這個場景的完整造型（Penny 喜歡的 rin-04 同類）
- **舊版姿勢：** 站在窗邊、背部 3/4 朝鏡頭：重心在左腳，一手在胸前拉住晨袍，另一手扶著窗框；越過裸肩回頭看鏡頭（轉頭不超過 90 度）；緞面下襬輕輕擺動。

| 項目 | 內容 |
|---|---|
| 場景 | 東京高樓層公寓的黎明：高窗外是淡色天空與遠方柔和的城市，一張鋪象牙白床單的低床，床邊一盞還亮著的黃銅檯燈，房間整齊。 |
| 服裝 | 深祖母綠真絲緞面晨袍，腰間鬆鬆繫起，從一側肩膀滑落露出上背。 |
| 髮型／髮色 | 深酒紅棕長髮，鬆鬆盤成低髻，頸邊落下幾縷。 |
| 配件 | 小金色垂墜耳環、細金手鍊。 |
| 光線 | 主光：高窗進來的柔和冷色黎明光打在臉與肩上。補光：畫面外的柔光板讓臉清楚。她身後的黃銅檯燈在緞面上加一點暖光。深綠、象牙白與金色。 |
| 表情 | 平靜、心照不宣的半笑。 |
| 姿勢與雙手 | 站在窗邊、背部 3/4 朝鏡頭，重心在左腳；一手在胸前拉住晨袍，另一手扶著窗框；越過裸肩回頭看鏡頭（轉頭不超過 90 度）。 |
| 甜美元素 | 回眸的淺笑、柔和的晨光。 |
| 性感元素 | 滑落的緞面露出肩與背、低髻露出頸線、緞面貼著身形的光澤。 |
| 替代方向 | 出勤前的銀座：黑色絲絨細肩帶長禮服，坐在金色燈光的吧台邊（不拿酒杯）。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 大腿中段以上 | 膝上 |
| 人物佔畫面高度 | 約 86% | 約 85% |
| 頭頂／手腳範圍 | 頭頂完整、雙手在框內，切在大腿中段 | 頭頂完整、雙手在框內，切在膝蓋下方 |
| 留白位置 | 人物偏左，右側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 70mm／約 3.1 公尺 | 70mm／約 3.2 公尺 |
| 視野（寬×高，公尺） | 1.59×1.06 | 1.1×1.46 |
| 人物範圍高度（公尺） | 0.91 | 1.24 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框要上下共裁約 19%：約剩腰上，回眸的臉與肩仍完整。 | 放進橫式半版直幅框左右共裁約 11%：人物置中，不受影響。 |

| 風險 | 處理 |
|---|---|
| 回頭造成脖子扭曲 | 背部 3/4 朝鏡頭、轉頭不超過 90 度 |
| 晨袍遮蔽不足 | 一手在胸前拉住晨袍，只露肩與上背 |
| 暗場景噪點、臉發灰 | 窗光主光加畫面外補光 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 25-year-old adult Japanese woman with her natural fair, cool-toned skin, an oval face and long narrow eyes, precise eyeliner and a muted rose-red lip, long deep wine-red brown hair pinned in a loose low bun with a few strands at her neck. Curvy figure, 166 cm tall, bust 92 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a deep emerald-green silk satin robe tied loosely at the waist and slipping off one shoulder to show her upper back, small gold drop earrings and a thin gold bracelet. Setting: a quiet high-floor Tokyo apartment at dawn, a tall window with pale sky and a soft distant city, a low bed with ivory linen and a brass bedside lamp still switched on, the room tidy. She stands by the window with her back three-quarters to the camera, weight on her left leg, one hand holding the robe closed at her chest and the other resting on the window frame, looking back over her bare shoulder at the camera with a calm, knowing half-smile. Horizontal 3:2 frame, full-frame camera with a 70mm lens from about 3.1 metres, camera at her chest height; framed from mid-thigh to a little above her head, she fills about 86% of the frame height, left of centre with the tall window and dawn city on the right. Lighting: soft cool dawn light from the tall window as the key on her face and shoulder, a soft fill panel just out of frame keeping her face clear, and the brass lamp behind her adding a small warm glow on the satin; deep green, ivory and gold tones, the far corners of the room in shadow. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 25-year-old adult Japanese woman with her natural fair, cool-toned skin, an oval face and long narrow eyes, precise eyeliner and a muted rose-red lip, long deep wine-red brown hair pinned in a loose low bun with a few strands at her neck. Curvy figure, 166 cm tall, bust 92 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a deep emerald-green silk satin robe tied loosely at the waist and slipping off one shoulder to show her upper back, small gold drop earrings and a thin gold bracelet. Setting: a quiet high-floor Tokyo apartment at dawn, a tall window with pale sky and a soft distant city, a low bed with ivory linen and a brass bedside lamp still switched on, the room tidy. She stands by the window with her back three-quarters to the camera, weight on her left leg, one hand holding the robe closed at her chest and the other resting on the window frame, looking back over her bare shoulder at the camera with a calm, knowing half-smile. Vertical 3:4 frame, full-frame camera with a 70mm lens from about 3.2 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 85% of the frame height, centred with the window edge beside her. Lighting: soft cool dawn light from the tall window as the key on her face and shoulder, a soft fill panel just out of frame keeping her face clear, and the brass lamp behind her adding a small warm glow on the satin; deep green, ivory and gold tones, the far corners of the room in shadow. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.9 Rainie Hsu（許雷妮，24）｜頂樓夜景的血紅緞面馬甲洋裝

**R1 修訂（姿態與細節）：**

- 取消「撥髮＋頭髮擺動」：雙手放在身後欄杆上、一腳從高衩往前
- 補光改為畫面外柔光
- 取景重算：橫幅膝上、直幅全身

- **與人設核對：** 主方向不變：夜色華麗、派對禮服、明亮主光＋城市散景。她的禁忌清單排除飲酒畫面：畫面不放酒杯酒瓶。
- **為什麼適合她：** 她「走進來整個房間就變了」。血紅緞面、城市燈海、直視鏡頭的自信笑，臉打得夠亮，不是暗暗的夜拍。
- **參考照片（既有）：** rainie-06、rainie-10
- **逐項檢查：** 隨拍感：低；道具遮身形：無；不拿酒杯；動作數量：v1 撥髮＋頭髮擺動 → 改成雙手放欄杆；穿搭完整度：馬甲洋裝＋細帶高跟＋耳環＋手環，完整
- **舊版姿勢：** 背靠玻璃欄杆：重心在一側臀部，一腳從高衩往前伸；一手放在欄杆上，另一手把頭髮撥到一側肩上；頭髮隨動作擺動。

| 項目 | 內容 |
|---|---|
| 場景 | 高樓頂層露台的夜晚：玻璃欄杆、腳下城市燈光化成柔和散景、平滑的深色石材地面，露台上沒有其他東西，玻璃只反射城市燈光。 |
| 服裝 | 血紅緞面馬甲迷你洋裝（大腿高衩）、黑色細帶高跟涼鞋。 |
| 髮型／髮色 | 長直黑髮，梳得光滑有光澤，深側分。 |
| 配件 | 大型銀色垂墜耳環、細銀手環。 |
| 光線 | 主光：左前方頭部高度的大型明亮柔光箱，臉與緞面都清楚。補光：畫面外右側柔光。背後是深藍夜空與暖金城市散景。 |
| 表情 | 直視鏡頭、自信又帶點壞的笑。 |
| 姿勢與雙手 | 背靠玻璃欄杆，雙手放在身後的欄杆上，一腳從高衩往前。 |
| 甜美元素 | 笑容裡的俏皮。 |
| 性感元素 | 血紅緞面馬甲、高衩露出的腿、直視的眼神。 |
| 替代方向 | 銀色背景布的派對棚拍：黑色亮片細肩帶短洋裝，硬一點的閃燈主光。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 膝上 | 全身 |
| 人物佔畫面高度 | 約 86% | 約 86% |
| 頭頂／手腳範圍 | 頭頂完整、雙手在框內，切在膝蓋下方 | 頭頂到腳完整，雙手在框內 |
| 留白位置 | 人物偏右，左側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 85mm／約 5.0 公尺 | 85mm／約 5.3 公尺 |
| 視野（寬×高，公尺） | 2.12×1.41 | 1.5×2.0 |
| 人物範圍高度（公尺） | 1.21 | 1.72 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框（約 1.85:1）要上下共裁約 19%：約剩大腿以上，頭頂留白變少但人物完整。 | 放進橫式半版直幅框（約 0.67:1）左右共裁約 11%：人物置中，不受影響。 |

| 風險 | 處理 |
|---|---|
| 夜景噪點、臉發暗 | 大面積明亮主光＋補光 |
| 出現酒杯或酒瓶 | 手放在欄杆上，場景只寫欄杆與地面 |
| 高衩遮蔽 | 生成後逐張檢查 |
| 玻璃反射出另一個人 | 寫明玻璃只反射城市燈光 |
| 與 Iris 的 R2 目視相似 | 夜景華麗、側分光滑髮、血紅 vs Iris 的白天河濱；不改臉 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, high cheekbones and a sculpted jaw, soft-glam makeup with a soft brown liner close to the lash line, long straight jet-black hair worn sleek and glossy with a deep side part. Curvy figure, 165 cm tall, bust 94 cm, waist 59 cm, hips 92 cm, F cup, full chest and slim waist. She wears a blood-red satin corset mini dress with a thigh-high slit, strappy black stiletto sandals, large silver statement drop earrings and a slim silver cuff. Setting: a high-rise penthouse terrace at night, a glass balustrade with the city lights far below spread into soft bokeh, a smooth dark stone floor, nothing else on the terrace, the glass reflecting only city lights. She leans back against the glass balustrade with both hands resting on the rail behind her and one leg forward through the slit, looking straight into the camera with a confident, slightly mischievous smirk. Horizontal 3:2 frame, full-frame camera with an 85mm lens from about 5 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 86% of the frame height, right of centre with the glowing city bokeh on the left. Lighting: a large bright softbox key from front-left at head height lights her face and catches crisp red highlights on the satin; a soft fill from the right just out of frame; deep navy night sky and warm gold city bokeh behind her. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, high cheekbones and a sculpted jaw, soft-glam makeup with a soft brown liner close to the lash line, long straight jet-black hair worn sleek and glossy with a deep side part. Curvy figure, 165 cm tall, bust 94 cm, waist 59 cm, hips 92 cm, F cup, full chest and slim waist. She wears a blood-red satin corset mini dress with a thigh-high slit, strappy black stiletto sandals, large silver statement drop earrings and a slim silver cuff. Setting: a high-rise penthouse terrace at night, a glass balustrade with the city lights far below spread into soft bokeh, a smooth dark stone floor, nothing else on the terrace, the glass reflecting only city lights. She leans back against the glass balustrade with both hands resting on the rail behind her and one leg forward through the slit, looking straight into the camera with a confident, slightly mischievous smirk. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 5.3 metres, camera at her navel height; full length from her stilettos to a little above her head, she fills about 86% of the frame height, centred. Lighting: a large bright softbox key from front-left at head height lights her face and catches crisp red highlights on the satin; a soft fill from the right just out of frame; deep navy night sky and warm gold city bokeh behind her. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.10 Miu Shiraishi（白石美羽，22）｜奶油色咖啡館的窗邊座位

**R1 修訂（主方向）：**舊版標題「開店前的奶油色咖啡館」。

- 主推薦改到咖啡館座位區：窗邊木長凳、奶油色牆面，坐姿讓腰線與裙裝可見
- 取消圍裙與胸前捧杯；杯子只放在旁邊小桌上
- 毛衣紮進高腰麂皮短裙並加細腰帶，收出腰線
- 原本的「吧台後、圍裙、捧拿鐵」改列為職業風備選
- 取景重算：橫幅坐姿全身（50mm）、直幅坐姿膝上（85mm）

- **與人設核對：** 保留奶油色咖啡館、露肩針織與甜美氣質；不拍成咖啡店員的工作照。童顏：寫明 adult、成熟的服裝。碰撞（Jia、Somi）：暖木奶油色、安靜、淺亞麻短髮；不宣稱能消除碰撞。
- **為什麼適合她：** 她安靜、存在感很強。不讓她工作，讓她坐在窗邊——露肩毛衣、收腰短裙、交疊的腿，甜而有曲線。
- **參考照片（既有）：** miu-01、miu-02
- **舊版姿勢：** 站在吧台後面、面向鏡頭：雙手在胸口高度捧著一杯冒著熱氣的陶瓷拿鐵杯；毛衣滑落一側肩。

| 項目 | 內容 |
|---|---|
| 場景 | 中目黑小咖啡館的座位區：暖色橡木窗邊長凳、平滑的奶油色灰泥牆、身旁一扇大窗，一張小圓桌上放著一只陶瓷杯，店內乾淨無人。 |
| 服裝 | 奶油色粗針織露肩毛衣紮進高腰淺棕麂皮迷你裙、細棕色腰帶、奶油色繫踝低跟鞋。 |
| 髮型／髮色 | 淺亞麻米金，齊肩內彎鮑伯、空氣瀏海。 |
| 配件 | 細金耳針。 |
| 光線 | 主光：相機左側大窗進來的柔和晨光。補光：畫面外右側柔光，臉均勻。奶油、橡木與淺棕色調。 |
| 表情 | 輕輕歪頭、柔和的甜笑，看鏡頭。 |
| 姿勢與雙手 | 坐在窗邊長凳，身體 3/4 朝鏡頭、雙腿在膝上交疊；雙手放在膝上。 |
| 甜美元素 | 歪頭的甜笑、柔和的晨光、奶油色。 |
| 性感元素 | 露肩毛衣、細腰帶收出的腰線、交疊的腿與短裙（童顏與身材的反差）。 |
| 替代方向 | 職業風（備選）：吧台後、短版亞麻圍裙、雙手捧一杯拿鐵，開店前的晨光——保留咖啡店員人設，但不當主推薦。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 坐姿全身 | 坐姿膝上 |
| 人物佔畫面高度 | 約 85% | 約 84% |
| 頭頂／手腳範圍 | 坐姿頭頂到腳完整，雙手在框內 | 坐姿頭頂完整、雙手在框內，從膝蓋以上 |
| 留白位置 | 人物偏左，右側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 50mm／約 3.1 公尺 | 85mm／約 2.4 公尺 |
| 視野（寬×高，公尺） | 2.23×1.49 | 0.68×0.9 |
| 人物範圍高度（公尺） | 1.26 | 0.76 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框要上下共裁約 19%：坐姿全身會切到腳；若最後選大照片框，改用坐姿膝上。 | 放進橫式半版直幅框左右共裁約 11%：人物置中，不受影響。 |

| 風險 | 處理 |
|---|---|
| 童顏顯小 | 寫明 adult、成熟服裝與低跟鞋，不用娃娃裝與制服元素 |
| 杯子或窗外出現文字 | 素面陶杯、窗外只寫柔光 |
| 髮色被拍得太白 | 寫淺亞麻米金（flaxen beige-blonde） |
| 與 Jia、Somi 的碰撞紀錄 | 暖木奶油、坐姿安靜、短髮；不改臉，不宣稱能消除碰撞 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 22-year-old adult Japanese woman with her natural very fair skin tone, a round face with big soft downturned eyes, orange-toned blush under the eyes and glossy lips, light flaxen beige-blonde hair in a shoulder-length bob curled inward with airy see-through bangs. Petite curvy figure, 156 cm tall, bust 87 cm, waist 55 cm, hips 86 cm, E cup, full chest and slim waist. She wears a cream chunky off-shoulder knit sweater tucked into a high-waisted light-brown suede mini skirt with a thin brown belt, cream ankle-strap low heels and thin gold stud earrings. Setting: the seating corner of a small Nakameguro-style café, a warm oak window bench, a smooth cream plaster wall and a big window beside her, a small round table with one plain ceramic cup resting on it, the room clean and empty. She sits on the window bench with her body angled three-quarters to the camera and her legs crossed at the knee, both hands resting on her knee, tilting her head slightly with a soft, sweet smile at the camera. Horizontal 3:2 frame, full-frame camera with a 50mm lens from about 3.1 metres, camera at her seated chest height; full length seated, from her heels to a little above her head, she fills about 85% of the frame height, left of centre with the window and cream wall on the right and the small table at the edge. Lighting: warm soft morning light through the big window from camera-left as the key, a soft fill just out of frame on the right so her face is evenly lit; cream, oak and soft brown tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 22-year-old adult Japanese woman with her natural very fair skin tone, a round face with big soft downturned eyes, orange-toned blush under the eyes and glossy lips, light flaxen beige-blonde hair in a shoulder-length bob curled inward with airy see-through bangs. Petite curvy figure, 156 cm tall, bust 87 cm, waist 55 cm, hips 86 cm, E cup, full chest and slim waist. She wears a cream chunky off-shoulder knit sweater tucked into a high-waisted light-brown suede mini skirt with a thin brown belt, cream ankle-strap low heels and thin gold stud earrings. Setting: the seating corner of a small Nakameguro-style café, a warm oak window bench, a smooth cream plaster wall and a big window beside her, a small round table with one plain ceramic cup resting on it, the room clean and empty. She sits on the window bench with her body angled three-quarters to the camera and her legs crossed at the knee, both hands resting on her knee, tilting her head slightly with a soft, sweet smile at the camera. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 2.4 metres, camera at her seated chest height; framed from her knees to a little above her head, she fills about 84% of the frame height, centred with the window frame beside her. Lighting: warm soft morning light through the big window from camera-left as the key, a soft fill just out of frame on the right so her face is evenly lit; cream, oak and soft brown tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.11 Jia Seo（서지아，22）｜灰色無縫棚的舞者時尚

**R1 修訂（姿態與細節）：**

- 動作改成一個停住的舞蹈線條：重心右腳、左腳側伸、一手平伸、一手放腰（取消扭身＋甩頭髮）
- 寬褲改成合身窄管褲、拿掉透膚襯衫，讓腿與身體線條看得見
- 薄荷綠內層改成塞在耳後露出，不靠甩頭
- 取景重算：橫直都是全身，50mm；伸展的手腳都在框內

- **與人設核對：** 主方向不變：舞者時尚棚拍、身體線條。檢查發現 v1 的寬褲與透膚襯衫會遮住身形、動作也太多，已修正。
- **為什麼適合她：** 她「對身體的控制力是最自豪的事」。乾淨的灰色棚、木地板、一個停住的舞蹈線條，讓身體本身成為時裝。
- **參考照片（既有）：** jia-02、jia-08
- **逐項檢查：** 隨拍感：v1 甩頭動態像影片截圖 → 改成停住的舞蹈線條；道具遮身形：v1 寬褲與透膚襯衫遮住腿與身形 → 改合身窄管褲、拿掉襯衫；動作數量：v1 扭身＋伸手＋甩頭 → 改成一個線條；穿搭完整度：連身衣＋窄管褲＋球鞋＋耳環，完整
- **舊版姿勢：** 舞蹈動作停格：重心在右腳、左腳向側邊延伸，上身扭向鏡頭；一手往外伸展、另一手在鎖骨；頭髮甩過去露出薄荷綠內層。

| 項目 | 內容 |
|---|---|
| 場景 | 乾淨的攝影棚：淺灰無縫牆、溫暖的木地板，棚內沒有其他東西。 |
| 服裝 | 黑色單肩貼身連身衣、高腰合身灰色窄管褲、白色厚底球鞋。 |
| 髮型／髮色 | 冷灰藍黑長髮，一側塞在耳後，露出內層的薄荷綠。 |
| 配件 | 小銀色圈耳環。 |
| 光線 | 主光：左前方的大型冷白柔光箱。補光：畫面外右側柔光，臉均勻。輪廓：身後一支窄條燈在肩膀與頭髮畫出乾淨的輪廓。冷灰與木色。 |
| 表情 | 冷靜自信的半笑，看鏡頭。 |
| 姿勢與雙手 | 停住的舞蹈線條：重心在右腳，左腳向側邊伸直、腳尖點地；一手向外平伸到肩高，另一手放在腰上；臉朝鏡頭。 |
| 甜美元素 | 半笑、露出的薄荷綠髮色。 |
| 性感元素 | 單肩貼身連身衣、伸展的腿與身體線條、直角肩與長腿。 |
| 替代方向 | 收工後的練舞室窗邊：黑色運動內衣外搭寬版白 T、灰色運動褲，坐在大鏡子前的木地板上，傍晚窗光（不拍鏡中倒影）。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 全身 | 全身 |
| 人物佔畫面高度 | 約 85% | 約 79% |
| 頭頂／手腳範圍 | 頭頂到腳完整，雙手在框內 | 頭頂到腳完整，雙手在框內 |
| 留白位置 | 人物偏左，右側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 50mm／約 4.2 公尺 | 50mm／約 3.4 公尺 |
| 視野（寬×高，公尺） | 3.02×2.02 | 1.63×2.18 |
| 人物範圍高度（公尺） | 1.72 | 1.72 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框要上下共裁約 19%：全身會切到腳或頭頂；若最後選大照片框，這張要改拍膝上。 | 放進橫式半版直幅框左右共裁約 11%：伸展的手與腳會貼近邊緣；若最後選半版，拍攝時要再拉遠一點。 |

| 風險 | 處理 |
|---|---|
| 伸展肢體錯誤（多手、斷腿） | 寫明重心腳與兩手位置；生成後逐肢檢查 |
| 肌肉感過強 | 寫 soft feminine curves |
| 薄荷綠沒出現 | 寫明塞在耳後露出；不出現就接受，不為此重生 |
| 與 Miu、Somi 的碰撞紀錄 | 冷色、舞蹈線條、薄荷綠；不改臉，不宣稱能消除碰撞 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 22-year-old adult Korean woman with her natural fair, cool-toned skin, a small face, straight broad shoulders and long narrow upturned eyes, dewy no-makeup Korean makeup with a soft brown liner and gradient lips, long cool blue-black hair tucked behind one ear so its mint-green inner layer shows. Slim dancer figure with soft feminine curves, 168 cm tall, bust 85 cm, waist 58 cm, hips 90 cm, C cup, long legs and a slim waist. She wears a black one-shoulder fitted bodysuit, high-waisted slim-fit grey trousers, white chunky sneakers and small silver hoop earrings. Setting: a clean photo studio with a seamless pale grey wall and a warm wooden dance floor, nothing else in the room. She holds a still dance line: weight on her right leg, left leg extended straight to the side with the toe touching the floor, one arm extended out at shoulder height and the other hand resting at her waist, face toward the camera with a cool, confident half-smile. Horizontal 3:2 frame, full-frame camera with a 50mm lens from about 4.2 metres, camera at her navel height; full length from her sneakers to a little above her head, she fills about 85% of the frame height, left of centre with her outstretched arm and leg inside the frame and the pale grey wall open on the right. Lighting: a large cool-white softbox key from front-left and a soft fill from the right just out of frame light her face evenly; a narrow strip light behind her draws a clean rim along her shoulder and hair; cool grey and warm wood tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 22-year-old adult Korean woman with her natural fair, cool-toned skin, a small face, straight broad shoulders and long narrow upturned eyes, dewy no-makeup Korean makeup with a soft brown liner and gradient lips, long cool blue-black hair tucked behind one ear so its mint-green inner layer shows. Slim dancer figure with soft feminine curves, 168 cm tall, bust 85 cm, waist 58 cm, hips 90 cm, C cup, long legs and a slim waist. She wears a black one-shoulder fitted bodysuit, high-waisted slim-fit grey trousers, white chunky sneakers and small silver hoop earrings. Setting: a clean photo studio with a seamless pale grey wall and a warm wooden dance floor, nothing else in the room. She holds a still dance line: weight on her right leg, left leg extended straight to the side with the toe touching the floor, one arm extended out at shoulder height and the other hand resting at her waist, face toward the camera with a cool, confident half-smile. Vertical 3:4 frame, full-frame camera with a 50mm lens from about 3.4 metres, camera at her navel height; full length from her sneakers to a little above her head, she fills about 79% of the frame height, centred with her outstretched arm and leg inside the frame and extra space above her head. Lighting: a large cool-white softbox key from front-left and a soft fill from the right just out of frame light her face evenly; a narrow strip light behind her draws a clean rim along her shoulder and hair; cool grey and warm wood tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 4.12 Yerin Han（한예린，26）｜清晨霧中的球道

**R1 修訂（姿態與細節）：**

- 保留球桿橫掛肩後這一個姿態；取消「馬尾擺動」
- 逆光加上畫面外反光板與柔光補臉；不再重複寫膚色
- 取景重算：橫幅膝上、直幅全身，球桿兩端都在框內

- **與人設核對：** 主方向不變：高爾夫度假、精緻運動套裝、清晨球場，也接近她現有的 yerin-04。和 Rin 的碰撞：明亮戶外運動 vs 暗色室內。
- **為什麼適合她：** 「球衣就是時尚」。清晨球道、薄霧、一套淺藍與白，把她的健康感和大方的笑拍成度假時尚照。
- **參考照片（既有）：** yerin-04、yerin-01
- **逐項檢查：** 隨拍感：低，擺好的姿態；道具遮身形：球桿橫在肩後，不遮身體；動作數量：拿掉馬尾擺動；穿搭完整度：polo＋百褶裙＋手套＋球鞋＋球帽，完整
- **舊版姿勢：** 一支一號木橫放在肩後、兩手腕掛在球桿上；重心在後腳，前腳輕輕交叉在前；轉頭看鏡頭；馬尾擺動。

| 項目 | 內容 |
|---|---|
| 場景 | 清晨的高爾夫球道：遠處樹林上方有薄霧，短草上有露水，遠方一支白色旗桿，球道上沒有其他人。 |
| 服裝 | 淺天空藍無袖針織高爾夫 polo、白色百褶高爾夫迷你裙、左手白色皮手套、白色高爾夫鞋、素面白色球帽。 |
| 髮型／髮色 | 亞麻棕長髮、臉側金色挑染，低馬尾從球帽後方穿出。 |
| 配件 | 小金色耳針。 |
| 光線 | 主光：她身後右側的低角度晨光，在馬尾與肩膀畫出暖金輪廓。補光：畫面外前方的大反光板與柔光，臉均勻清楚。柔和晨霧與清新綠色。 |
| 表情 | 大方明亮的笑，看鏡頭。 |
| 姿勢與雙手 | 一支一號木橫放在肩後、兩手腕掛在球桿上；重心在後腳，前腳輕輕交叉在前。 |
| 甜美元素 | 大方的笑、淺藍與白的清爽配色。 |
| 性感元素 | 無袖針織貼身 polo、百褶迷你裙與長腿、170 cm 的身形比例。 |
| 替代方向 | 高級室內練習場：白色合身 polo＋海軍藍百褶短裙，站在打擊位、收桿姿勢，冷白均勻光。 |

**取景設計：**

|  | 橫 3:2 | 直 3:4 |
|---|---|---|
| 景別 | 膝上 | 全身 |
| 人物佔畫面高度 | 約 85% | 約 87% |
| 頭頂／手腳範圍 | 頭頂完整、雙手在框內，切在膝蓋下方 | 頭頂到腳完整，雙手在框內 |
| 留白位置 | 人物偏右，左側約四成給背景 | 人物置中，頭頂與兩側少量留白 |
| 焦段／距離 | 85mm／約 5.5 公尺 | 85mm／約 5.4 公尺 |
| 視野（寬×高，公尺） | 2.33×1.55 | 1.52×2.03 |
| 人物範圍高度（公尺） | 1.31 | 1.76 |
| 模型原生輸出 | 3:2 原生尺寸未知：沒有 soul_2 3:2 的實際輸出紀錄；約 2048×1365 只是依長邊 2048 推算 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 放進橫式大照片框（約 1.85:1）要上下共裁約 19%：約剩大腿以上，頭頂留白變少但人物完整。 | 放進橫式半版直幅框左右共裁約 11%：球桿兩端會貼近邊緣。 |

| 風險 | 處理 |
|---|---|
| 握球桿的手與桿身變形 | 手腕掛在球桿上；生成後放大檢查 |
| 肌肉感過強 | 寫 soft feminine lines |
| 逆光臉暗 | 寫明反光板與柔光補臉 |
| 球帽或衣服出現文字或品牌 | 寫素面白帽、無標誌 |
| 與 Rin 的碰撞紀錄 | 明亮戶外 vs 暗色室內；不改臉，不宣稱能消除碰撞 |

橫構圖 prompt 草稿（3:2，未執行）：

```text
A 26-year-old adult Korean woman with her natural fair skin tone, bright defined features and a wide open smile, light sun-protective makeup and a bright lip, long flax-brown hair with golden face-framing highlights in a low ponytail pulled through the back of a plain white cap. Curvy athletic figure with soft feminine lines, 170 cm tall, bust 90 cm, waist 60 cm, hips 93 cm, E cup, long legs and a slim waist. She wears a pale sky-blue sleeveless knit golf polo, a white pleated golf mini skirt, a white leather glove on her left hand, white golf shoes and small gold stud earrings. Setting: a golf course fairway in the early morning, soft mist over the far trees, dew on the short grass, a white flagstick far in the distance, the fairway empty. She stands with a driver resting across her shoulders behind her neck, wrists draped over the club, weight on her back leg with the front leg crossed lightly in front, smiling brightly at the camera. Horizontal 3:2 frame, full-frame camera with an 85mm lens from about 5.5 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 85% of the frame height, right of centre with the whole club inside the frame and the misty fairway on the left. Lighting: the low early sun behind her and to the right draws a warm rim along her ponytail and shoulders; a large white reflector and a soft fill just out of frame in front of her light her face evenly; soft morning mist and fresh green tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

直構圖 prompt 草稿（3:4，未執行）：

```text
A 26-year-old adult Korean woman with her natural fair skin tone, bright defined features and a wide open smile, light sun-protective makeup and a bright lip, long flax-brown hair with golden face-framing highlights in a low ponytail pulled through the back of a plain white cap. Curvy athletic figure with soft feminine lines, 170 cm tall, bust 90 cm, waist 60 cm, hips 93 cm, E cup, long legs and a slim waist. She wears a pale sky-blue sleeveless knit golf polo, a white pleated golf mini skirt, a white leather glove on her left hand, white golf shoes and small gold stud earrings. Setting: a golf course fairway in the early morning, soft mist over the far trees, dew on the short grass, a white flagstick far in the distance, the fairway empty. She stands with a driver resting across her shoulders behind her neck, wrists draped over the club, weight on her back leg with the front leg crossed lightly in front, smiling brightly at the camera. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 5.4 metres, camera at her navel height; full length from her golf shoes to a little above her head, she fills about 87% of the frame height, centred with the whole club inside the frame. Lighting: the low early sun behind her and to the right draws a warm rim along her ponytail and shoulders; a large white reflector and a soft fill just out of frame in front of her light her face evenly; soft morning mist and fresh green tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

## 5. 橫直構圖策略（R1 修訂）

**建議：同一主題、同一造型，橫構圖（3:2）與直構圖（3:4）分開拍——這是建議，Penny 還沒有批准這個策略。**

- 版面還沒定。橫式大照片框（約 1.85:1）與半版直幅框（約 0.67:1）形狀差很多，一張照片很難兩邊都好用。
- 分開拍時，橫幅與直幅用不同景別：多數人橫幅拍膝上（人物大、留白在一側）、直幅拍全身；坐姿或需要伸展空間的人另外設計。
- 同一個距離把相機轉直，視野高度會多三分之一，所以「橫幅膝上、直幅全身」可以在同一個位置完成；每張的焦段、距離與視野都換算過。
- soul_2 沒有 seed，橫直兩次生成的服裝與場景細節會有小差異；這要在第一階段試拍確認能不能接受。

**另一種做法：** 只拍一張 3:4 直幅：若版面最後選「橫式半版直幅框」，一張 3:4 就夠用。版面確定前，兩種做法都保留給 Penny 決定。

**換算與檢查：**

- 換算方法：全片幅 36×24 mm。橫 3:2 的視野高度＝24 mm×距離÷焦段；直 3:4（直拿、裁成 3:4）的視野高度＝32 mm×距離÷焦段。
- v1 的錯誤：85mm、5 公尺、橫 3:2 的視野高度只有約 1.41 公尺，拍不下 1.6–1.7 公尺的全身還留白。v2 的全身橫幅改用 50–70mm 或拉遠到約 7 公尺。
- 人物佔畫面高度控制在約 80–88%；橫幅留白在一側約四成，不是三分之二。
- 版面未定：不再預設要大片日期區。下面的適配說明只做比例換算，不承諾 ppi，也不判斷線圈安全。

| 層次 | 說明 |
|---|---|
| 拍攝構圖需求 | 每位的橫、直各有景別、人物佔比、頭頂與手腳範圍、留白位置（見各位的取景設計）。 |
| 模型原生輸出 | 3:4（2k）＝1536×2048，已知；3:2 未知（約 2048×1365 只是推算，第一階段試拍時一併確認）。 |
| 版面適配 | 橫幅放進橫式大照片框（約 1.85:1）要上下共裁約 19%；直幅放進橫式半版直幅框（約 0.67:1）要左右共裁約 11%。其他組合不做。 |
| 出血／線圈 | 沿用 R3 假設（出血 2 mm、線圈在上緣）；頭頂都有留白，但線圈是否安全要等版面與廠商尺寸確定，不在這裡判斷。 |
| 廠商待確認 | 線圈尺寸、印刷品質門檻、尺度審稿——本輪不聯絡廠商。 |
| 不預設的手段 | 外擴與 AI 放大不列為必要步驟。 |

## 6. 執行與費用（R1 唯讀查證）

**狀態：** 未確認可執行預算：工具報價查到了，但與實際扣款的對應只在部分設定上觀察過。生成放行仍是 BLOCK。

**模型：** soul_2＋各人設既有 Soul，quality 2k，每次請求只出 1 張（count 1）；橫 3:2、直 3:4；不掛 Reference Element、不用參考圖。

| 人設 | Soul 狀態（紀錄） |
|---|---|
| Somi、Tammy、Rin、Miu、Jia、Yerin | production_ready（2026-09-07／08 訓練；6 張驗證臉部門檻通過） |
| Iris、Luna、Coco、Mia、Yuna | ready（較早訓練；R1 紀錄寫這幾位不在 Soul 總表內，是否跑過同樣的 6 張驗證未知） |
| Rainie | 只能用 v2 的 Soul（ready）；舊的 deprecated Soul 不可用 |

Soul ID 不列在本文件與公開頁面。

### 6.1 歷史實際扣款

| 項目 | 數值 | 依據 | 等級 | 來源檔 |
|---|---|---|---|---|
| Soul V2 實際扣款（交易明細） | 每筆 −0.12 | Soul 訓練總報告（2026-09-08）：驗證圖 114 張約 13.7 credits，交易明細為重複的「Higgsfield Soul V2 −0.12」；驗證紀錄寫明「每 spec 只生一張」，所以是一次請求 1 張。這批的比例與畫質沒有寫在讀到的文件裡。 | 歷史實扣（交易明細） | `review/soul_training/FINAL_REPORT.md`、`review/soul_pilot/VERIFY_REMAINING_12.md` |
| 2026-10-13 帳號交易明細 | 今天也有 Soul V2 −0.12 的扣款 | 唯讀查詢 transactions：這些是帳號上其他人的工作，不是本案；只說明 Soul V2 目前仍以 −0.12 一筆扣款。 | 歷史實扣（他人工作，只作參考） |  |
| Iris 先前的 Soul 生成 | 費用未逐筆記錄 | Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 共 7 次生成成功、輸出 1536×2048，但沒有逐筆扣款。 | 無費用紀錄 | `kols/iris-chen/generation_notes.md` |

### 6.2 今天的工具報價（get_cost 預檢，2026-10-13）

| 設定 | 回傳 |
|---|---|
| soul_2＋Soul（Iris）、2k、3:4、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、2k、3:2、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、2k、2:3、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、1.5k、3:4、count 1 | credits 1／credits_exact 0.12 |
| soul_2、不帶 Soul、2k、3:4、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、2k、3:4、count 4 | credits 1／credits_exact 0.12（與 count 1 相同） |

2026-10-13 用 generate_image 的 get_cost 預檢查詢 6 次（工具說明：只回傳費用、不送出工作）；查詢前後交易明細沒有新增任何一筆。回傳有兩個欄位：credits（整數顯示值 1）與 credits_exact（0.12）。不把 1 解讀成 0.12，也不把 0.12 當成已證實的實扣：0.12 與歷史 Soul V2 交易明細一致，但 3:2、2:3、1.5k 這幾種設定從沒有實扣紀錄。

### 6.3 計價方式、每次張數、費用上限、異常

| 項目 | 說明 | 來源檔 |
|---|---|---|
| 計價單位 | 工具報價以「每次請求」回傳；count 4 的報價與 count 1 完全相同，所以無法判斷報價是每張還是每次請求。本案只用 count 1，不推算多張的費用。 |  |
| 每次請求產生幾張 | generate_image：count 1–4（同一 prompt 的變體）；generate_image_batch：最多 12 個請求、每個固定 1 張，而且批次不支援費用預檢。本案每次只送 1 個請求、count 1。 |  |
| 能不能限制總費用 | generate_image 與 generate_image_batch 都沒有「費用上限」參數（只有 AI Influencer 工具有，不適用）。只能靠流程控制：一次一個請求、每次之後查交易明細、累計達上限就停。餘額不能用來對帳——帳號同時有其他人在用。 |  |
| 異常扣款 | 原因未知。另一位人設的生成筆記記錄過三次「實扣高於預檢」：seedream_v4_5 4 張扣 50、seedream_v4_5 4 張扣 8、soul_2（不帶 Soul）4 張扣 2.16。三次都是用帳戶餘額前後相減算的，而帳號同時有其他人在用；沒有用交易明細逐筆核對，所以不能歸因，也不能排除。其中兩次是不同模型（seedream_v4_5）。 | `kols/sophia-tseng/generation_notes.md`、`review/soul_training/FINAL_REPORT.md` |

### 6.4 撤回的數字

- 首批 2.88–5.76 credits、全案 8.64–17.28 credits：撤回，不再作為可執行預算。
- 10／40 credits：只保留為待核定的上限提案，不承諾能完成多少張。

### 6.5 分階段測試（提案）

| 項目 | 內容 |
|---|---|
| 第一階段（建議） | 只試 Iris 一位：橫 3:2 與直 3:4 各一個 spec，每個 spec 最多 2 次單張請求（共最多 4 次）。目的：看寫真質感、身分穩定度、3:2 原生尺寸與實際扣款。 |
| 第一階段上限（待核定） | 建議 1 credit。依今天的報價，4 次單張請求合計約 0.48；實扣未確認，所以不承諾一定做得完 4 次。 |
| 第一階段停止條件 | 任何一筆實扣與報價不同、累計達上限、身分跑掉、平台拒絕——立刻停止並回報，不自動重試。 |
| 之後 | 第一階段結果與實扣經 Penny 看過，才決定擴大到四位（Iris、Rin、Miu、Mia）或十二位；費用用第一階段的實扣重新估算。 |

**為什麼第一階段是 Iris：**

- Penny 最喜歡的 iris-04 正是這個方向（戶外黃金時段、回眸）。
- 逆光戶外是最容易臉暗、膚色被拍偏的光線，先驗證最難的情況。
- 她的 Soul 是較早的 ready 版本，是否跑過 6 張驗證未知；先確認身分穩定度。
- 她的 3:4 輸出尺寸已有紀錄，可以拿來對照 3:2 的實際尺寸。

**已知限制：**

- Soul V2 不繼承髮型與髮色：每張 prompt 都要寫她自己的髮色髮型（原則七 C-1）。
- Soul V2 不繼承身材：身材要用 prompt 句子補（數字直接寫）。
- 沒有 negative prompt：不要的東西只能用正面描述避開（例如「小徑空無一人」）。
- 碰撞配對（Miu–Jia、Miu–Somi、Jia–Somi、Yerin–Rin）不得同框（C-2）；本企劃每張只有一人。

**多階段：** 不規劃多階段（先生成再換臉、外擴、放大）。若首批發現橫直兩張服裝差太多，才考慮把第一張當唯一的參考圖餵第二張——這可能把構圖或身分一起帶過去，要另外測、另外批准。

**未知：** 3:2 的實際輸出像素、3:2 與其他設定的實際扣款（只有報價）、count 大於 1 時的費用、ready 狀態的 Soul 在逆光／棚拍／夜景下的身分穩定度、同一造型跨兩次生成的一致性

**授權：** 本輪不設定任何花費授權。任何測試都要 Penny 批准，再由主管另發執行指令。

## 7. 要請 Penny 決定的事

1. 12 位的方向：每位在頁面上選「接受主方向／改用替代方向／想修改」。這版每位都有修訂，舊版的回饋保留在頁面上，但不算新版的回覆。
2. 橫直構圖：「同一造型橫、直各拍一張」是建議，不是已批准的策略。要先採用它，還是先只拍 3:4 直幅、等版面決定？
3. 第一階段只試 Iris 一位：同意這個方向嗎？這一題不是費用核准——費用上限另外查證、另外核定。

## 8. 共同的皮膚與質感句（每段 prompt 結尾都加）

```text
Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```
