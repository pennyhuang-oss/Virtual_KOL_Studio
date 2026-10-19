TASK-CAL-001／M-3／R3｜24 套寫真景別、角度與構圖細化｜送審報告

# M-3／R3 送審紀錄

- **範圍**：只規劃。**生成 0、credits 0、訓練 0、上傳 0**；本輪沒有呼叫任何 Higgsfield 工具（連報價也沒有）。沒有改 canon、Soul ID、人設；roster-v1、12 位、24 套、同人兩款服裝與場景不同、兩本月份排序都不變；免登入、素材頁與四張備選不變；費用方案與 5 個決策題目不變；沒有聯絡廠商、執行 M-4 或製作交印包。
- **成果 SHA**：`8f061fcec58e3dd0451bab8947fe6ed411eb377f`（上一輪成果 `d56aee44b6cd8aabdedb8e1eda36fdc7f20980f8`、送審 `4bce92896c8c261e4e3b0c552cbd7cb43606632d`）
- **部署**：Railway `cal2027-decision`，來源固定在 `8f061fcec58e3dd0451bab8947fe6ed411eb377f`，deployment `d4ed4fac-3d69-414d-91a6-a8f09b180f20`（SUCCESS）；其他 service 未動
- **企劃頁**：https://cal2027-decision-production.up.railway.app/shoot.html（免登入）
- **資料與文件**：`docs/calendar/data/cal_m3_shoot_plan.json`（shoot-plan-v4）、`docs/calendar/data/cal_m3_owner_feedback_r3.json`（Penny 最新要求逐字）、`docs/calendar/CAL_18_M3_SHOOT_PLAN.md`（R3 標題，含攝影總覽與 24 套七欄位）、`docs/calendar/CAL_19_M3_R2_OWNER_DECISION.md`（R2 紀錄，位元組不變）
- 每套的景別與角度都是**執行者的推薦**，不是 owner 已核准（Iris 的「身體正面、有笑容」是 Penny 已提出的要求）。以下驗證都是 **Claude 自測**，不是主管的獨立驗證；部署不等於核准。

## 1. 做了什麼

- 24 套都補上七個攝影欄位（景別、畫面上下界、身體朝向、臉部朝向與視線、相機高度與俯仰、畫面配置、攝影目的），中文欄位與英文 prompt 由同一份設定產生並逐套檢查。服裝與場景沿用 v3；這些景別與角度都是執行者的推薦，待 Penny 定案（Iris 的「身體正面、有笑容」是 Penny 已提出的要求）。
- 七個欄位（景別、畫面上下界、身體朝向、臉部朝向與視線、相機高度與俯仰、畫面配置、攝影目的）每套都有中文與英文；英文 prompt 改成固定結構：身分與身材 → 服裝（只寫入鏡的）→ 場景 → 動作與表情（不寫朝向）→ `Shot:` → `Body:` → `Face and gaze:` → `Camera:` → `Composition:` → `Emphasis:` → `Lighting:` → 皮膚句。
- 頁面：每張卡片標題下直接是「景別｜身體方向｜臉與視線｜拍攝角度」四格（不在展開區），場景／服裝欄位第一列也寫同一行；「尚未生成」框裡畫簡單構圖示意（人物範圍與頭的位置，依企劃數字，不含人物細節、不是圖片）；七欄位、理由與本輪調整可展開；新增兩本攝影總覽表，手機上每列變成一張小卡。
- 回饋：v4 回饋另存一欄；v1／v2／v3 的回饋原樣保留、顯示為「舊版」、不算 v4；載入不改寫，只有 Penny 動手才存；「清除 v4 回饋」只刪 v4。
- 建置：網站建置器要求 shoot-plan-v4（上一版 v3），且 24 套都要有七欄位、英文句逐字在 prompt 裡，否則建置失敗。

## 2. 攝影總覽：橫式款（16:9）

| 月 | 人物 | 景別 | 身體方向 | 臉部方向 | 視線 | 相機角度 | 人物位置 | 主要展示重點 |
|---|---|---|---|---|---|---|---|---|
| 1 | Yuna（H-yuna-kim） | 腰上 | 約45度斜側（朝畫面左） | 三分之二側臉 | 看鏡頭 | 坐姿時的肩膀高度・平視 | 右側約六成（左側窗光） | 水光肌與眼妝、通透窗光 |
| 2 | Rin（H-rin-ayase） | 斜躺全身 | 側面斜躺（朝畫面右） | 三分之二側臉 | 看鏡頭 | 略高於她斜躺時頭部的高度・輕俯 | 橫跨中央（頭在左、腳在右） | 斜躺 S 形曲線與長腿 |
| 3 | Miu（H-miu-shiraishi） | 坐姿全身 | 約30度斜側（朝畫面右） | 臉正面 | 看鏡頭 | 坐姿時的腰部高度・平視 | 置中（窗與床邊架左右平衡） | 胸型與很細的腰線、甜笑 |
| 4 | Tammy（H-tammy-chou） | 全身 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 膝蓋高度・輕仰 | 置中（展示櫃對稱） | 合身洋裝全身線條、高跟鞋與腿長 |
| 5 | Yerin（H-yerin-han） | 坐姿全身 | 約45度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 坐姿時的腰部高度・平視 | 中央偏右（球車與長腿成對角線） | 長腿、可愛笑容、高爾夫裝扮 |
| 6 | Coco（H-coco-wu） | 膝上 | 約30度斜側（朝畫面右） | 臉正面 | 看鏡頭 | 胸口高度・平視 | 置中（花壟對稱收攏） | 大笑、V 領胸型與收腰 |
| 7 | Mia（H-mia-huang） | 大腿中段以上 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 胸口高度・平視 | 置中（摩天輪光點在右肩後） | 馬甲胸腰比例、俏皮眨眼 |
| 8 | Iris（H-iris-chen） | 全身 | 正面 | 臉正面 | 看鏡頭 | 臀部高度・平視 | 左側三分之一（騎樓往右延伸） | 針織套裝全身比例、城市騎樓 |
| 9 | Jia（H-jia-seo） | 全身 | 側面（朝畫面左） | 三分之二側臉 | 看鏡頭 | 臀部高度・平視 | 置中（兩幅畫對稱） | 直角肩、細腰、修長線條 |
| 10 | Luna（H-luna-tanaka） | 席地坐姿全身 | 約30度斜側（朝畫面左） | 三分之二側臉 | 看向畫面左側紙拉門透進的晨光（不看鏡頭） | 坐姿時的胸口高度・平視 | 右側約六成（左側留給窗光與視線） | 斜側胸腰曲線、安靜的側臉 |
| 11 | Somi（H-somi-oh） | 膝上 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 腰部高度・平視 | 偏左（吧台往右延伸） | 腰臀曲線、交叉的腿、月牙眼大笑 |
| 12 | Rainie（H-rainie-hsu） | 膝上 | 正面 | 臉正面 | 直視鏡頭 | 腰部高度・平視 | 偏右（左側城市燈海） | 氣場、馬甲胸腰線、高衩腿線 |

景別：腰上 1、大腿中段以上 1、膝上 3、全身 3、坐姿全身 2、席地坐姿全身 1、斜躺全身 1；身體方向：正面 2、約30度斜側 6、約45度斜側 2、側面斜躺 1、側面 1。

橫式款以「人＋環境」為主，但不再一律膝上：全身 3（Iris 騎樓、Tammy 精品店、Jia 美術館）、坐／躺全身 4（Luna、Miu、Yerin、Rin）、膝上 3（Somi、Coco、Rainie）、大腿中段以上 1（Mia）、腰上 1（Yuna）。人物位置：置中 5、偏一側 5（其中 2 張是已接受的構圖）、斜躺橫跨與對角線各 1；偏一側的每張都有理由（透視線、視線方向、人物佔大半畫面），不是一側大面積空景。

依推薦月份：1月 腰上（Yuna）→2月 斜躺全身（Rin）→3月 坐姿全身（Miu）→4月 全身（Tammy）→5月 坐姿全身（Yerin）→6月 膝上（Coco）→7月 大腿中段以上（Mia）→8月 全身（Iris）→9月 全身（Jia）→10月 席地坐姿全身（Luna）→11月 膝上（Somi）→12月 膝上（Rainie）

## 3. 攝影總覽：直式款（3:4）

| 月 | 人物 | 景別 | 身體方向 | 臉部方向 | 視線 | 相機角度 | 人物位置 | 主要展示重點 |
|---|---|---|---|---|---|---|---|---|
| 1 | Tammy（V-tammy-chou） | 大腿中段以上 | 正面 | 臉正面 | 看鏡頭 | 腰部高度・輕仰 | 置中（吊燈在頭頂上方） | 自信姿態、深 V 翻領與腰帶的胸腰比例 |
| 2 | Jia（V-jia-seo） | 膝上 | 約30度斜側（朝畫面右） | 臉正面 | 看鏡頭 | 腰部高度・平視 | 置中（葉子框住兩側） | 細腰、臀線、開衩腿線 |
| 3 | Mia（V-mia-huang） | 胸上 | 約30度斜側（朝畫面右） | 三分之二側臉 | 看鏡頭 | 眼睛高度・輕俯 | 略偏左（花枝框住右上） | 臉與甜笑、露肩領口與胸型 |
| 4 | Miu（V-miu-shiraishi） | 大腿中段以上 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 胸口高度・平視 | 略偏左（欄杆對角線） | V 領胸型、細腰帶腰線 |
| 5 | Rainie（V-rainie-hsu） | 膝上 | 側面（朝畫面右） | 三分之二側臉 | 直視鏡頭 | 腰部高度・平視 | 左側約四成（右側街道倒影） | 側身曲線、長風衣直線、氣場 |
| 6 | Luna（V-luna-tanaka） | 全身 | 正面 | 臉正面 | 看鏡頭 | 膝蓋高度・輕仰 | 略偏左（約四成） | 整件洋裝、胸腰比例、腿長 |
| 7 | Coco（V-coco-wu） | 坐姿到水面 | 正面 | 臉正面 | 看鏡頭 | 坐姿時的胸口高度・平視 | 置中（水面在下） | 比基尼胸腰線條、歪頭大笑 |
| 8 | Yerin（V-yerin-han） | 膝上 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 臀部高度・輕仰 | 略偏右（天空在上方與左側） | 修長身形、健康的胸腰臀曲線 |
| 9 | Iris（V-iris-chen） | 大腿中段以上 | 正面 | 臉正面 | 看鏡頭 | 胸口高度・平視 | 置中 | Penny 指定穿搭：短上衣胸型、露腰、牛仔迷你裙；笑容 |
| 10 | Rin（V-rin-ayase） | 坐姿全身 | 約45度斜側（朝畫面左） | 三分之二側臉 | 看鏡頭 | 坐姿時的腰部高度・平視 | 右側約六成（吧台對角線在左） | 絲絨上身胸腰、交疊長腿、側臉輪廓 |
| 11 | Yuna（V-yuna-kim） | 全身 | 約30度斜側（朝畫面右） | 三分之二側臉 | 看鏡頭 | 臀部高度・平視 | 略偏左（右側大道延伸） | 腿長、毛呢套裝與長靴 |
| 12 | Somi（V-somi-oh） | 全身 | 正面 | 臉正面 | 看鏡頭 | 臀部高度・平視 | 略偏右（約六成） | 冬季整體造型、洋裝胸腰臀線 |

景別：胸上 1、大腿中段以上 3、膝上 3、全身 3、坐姿全身 1、坐姿到水面 1；身體方向：正面 5、約30度斜側 5、約45度斜側 1、側面 1。

直式款以「身形修長」為主：全身 3（Luna、Somi、Yuna）、坐姿 2（Rin 高腳椅、Coco 池邊）、膝上 3（Rainie、Jia、Yerin）、大腿中段以上 3（Iris、Tammy、Miu）、胸上 1（Mia）。站姿置中只有 Iris、Tammy、Jia 三張，景別各不相同；其他偏左、偏右或用對角線。

依推薦月份：1月 大腿中段以上（Tammy）→2月 膝上（Jia）→3月 胸上（Mia）→4月 大腿中段以上（Miu）→5月 膝上（Rainie）→6月 全身（Luna）→7月 坐姿到水面（Coco）→8月 膝上（Yerin）→9月 大腿中段以上（Iris）→10月 坐姿全身（Rin）→11月 全身（Yuna）→12月 全身（Somi）

## 4. 整組節奏

- 近景：近景只有兩張：V-mia-huang 胸上、H-yuna-kim 腰上；兩人的另一款都保留身材展示（Mia 大腿中段以上、Yuna 全身），不因近景減少身材展示。沒有安排純臉部特寫，因為這本桌曆以人物魅力與設定身材為核心。
- 角度：正面膝上站姿只剩 1 張（H-rainie-hsu，已接受方向，背靠欄杆本來就正對鏡頭）。側面 3 張（H-jia-seo 側身全身、V-rainie-hsu 側身膝上、H-rin-ayase 側面斜躺），都是為了身體線條；只有 H-luna-tanaka 不看鏡頭（看向窗光）。
- 同一位的兩款：12 位中有 11 位的 H／V 景別不同；Rainie 兩款都是膝上，但橫式款正面背靠欄杆、直式款側身，角度完全不同。每位的兩款在身體方向或相機高度上也都有差異（Iris 兩款都正面，用全身＋臀部高度 vs 大腿中段以上＋胸口高度區分）。

## 5. 調整較大的套數與理由

「調整較大」的判定：景別跨兩級以上（胸上→腰上→大腿中段以上→膝上→全身／坐姿），或身體改為側面，或視線改為不看鏡頭，或場景細節與光線方向配合改寫。其餘 18 套是補齊角度與構圖、拿掉不入鏡的鞋等小調整。

| ID | 原景別 | 新設計（景別｜身體方向｜臉與視線｜拍攝角度） | 原因 | 調整 | 理由 |
|---|---|---|---|---|---|
| H-luna-tanaka | 席地坐姿全身 | 席地坐姿全身｜約30度斜側（朝畫面左）｜三分之二側臉・看向窗光（畫面左）｜坐姿時的胸口高度・平視 | 視線改為不看鏡頭 | 視線由看鏡頭改為看向畫面左側的窗光（三分之二側臉）；身體改為約30度斜側。服裝與場景不變。 | Luna 的人設是「住在美麗白日夢裡的人」：24 套裡唯一不看鏡頭的一張，三分之二側臉仍能認人；直式款看鏡頭。相機放在她坐姿胸口高度平視，不俯拍，避免嬌小的她顯得更小。 |
| H-yuna-kim | 坐姿全身 | 腰上｜約45度斜側（朝畫面左）｜三分之二側臉・看鏡頭｜坐姿時的肩膀高度・平視 | 景別由坐姿全身改為腰上、場景細節與光線方向配合改寫 | 景別由坐姿全身改為腰上；姿勢改為「前臂搭窗台、手放鎖骨旁」，原本放在膝上的手會被裁掉；光線改寫為窗戶在畫面左側；白色平底鞋不入鏡。 | Yuna 的韓系感來自妝髮、色調與光：橫式用 24 套中唯一的腰上近景，讓臉與通透窗光成為主角；168 公分的腿長由直式款全身負責。 |
| H-jia-seo | 膝上 | 全身｜側面（朝畫面左）｜三分之二側臉・看鏡頭｜臀部高度・平視 | 身體改為側面 | 景別由膝上改為全身；身體由正面改為側面、臉改為三分之二側臉；人物由偏左改為置中＋兩幅畫對稱；手改為「靠鏡頭的手插臀側、露出腰側鏤空」。 | Jia 偏冷、俐落，側身最能表現直角肩與長腿；臉轉回鏡頭約55度成三分之二側臉，仍能認人，不是回眸。置中＋對稱畫作讓橫式不是「人在一側、另一側空景」。 |
| V-mia-huang | 膝上 | 胸上｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜眼睛高度・輕俯 | 景別由膝上改為胸上 | 景別由膝上改為胸上；白色及膝長靴不入鏡，從 prompt 拿掉；另一手改寫成「自然垂下、不入鏡」。 | 24 套中唯一的胸上近景，放在表情最豐富的 Mia；她的身形由橫式款的大腿中段以上負責，所以這張不會大幅減少身材展示。眼睛高度輕俯是常見的美顏角度，不會變形。 |
| V-tammy-chou | 全身 | 大腿中段以上｜正面｜臉正面・看鏡頭｜腰部高度・輕仰 | 景別由全身改為大腿中段以上 | 景別由全身改為大腿中段以上；黑色細高跟鞋不入鏡，從 prompt 拿掉；相機改為腰部高度輕仰。 | 高跟鞋已由橫式款全身呈現；直式款改大腿中段以上，正面插腰配腰部高度輕仰，拍出大飯店夜晚的氣場。 |
| V-rainie-hsu | 膝上 | 膝上｜側面（朝畫面右）｜三分之二側臉・看鏡頭｜腰部高度・平視 | 身體改為側面 | 身體由正面改為側面、臉改為三分之二側臉；人物由置中改為左側約四成；黑色短靴不入鏡，從 prompt 拿掉。 | 她的高顴骨與立體下顎適合側面；24 套中唯一的「側身站姿＋膝上」，與橫式款的正面靠欄杆完全不同。頭轉回鏡頭約55度，在自然範圍內，不是回眸。 |

**已接受方向（只在構圖確有衝突時調整）：**

| ID | 來源 | 調整 | 理由 |
|---|---|---|---|
| H-somi-oh | Penny 已接受的 v2 主方向 | 已接受方向，只做必要調整：膝上取景看不到鞋，棕色樂福鞋從 prompt 拿掉（中文標不入鏡）；姿勢句的「看鏡頭」移到視線欄。 | 已接受方向：服裝、場景、姿勢與「人物偏左、吧台往右、炸雞在右緣」都照舊；只把倚靠吧台的身體角度寫明為約30度斜側。 |
| H-rainie-hsu | Penny 已接受的 v2 主方向 | 已接受方向，只做必要調整：膝上取景看不到鞋，黑色細帶高跟涼鞋從 prompt 拿掉（中文標不入鏡）；姿勢句的「直視鏡頭」移到視線欄。 | 已接受方向：姿勢、取景、焦段與「人物偏右、左側燈海」都照舊；24 套中只剩這一張是正面膝上站姿，因為背靠欄杆的姿勢本來就正對鏡頭。 |
| V-coco-wu | Penny 已接受的 v2 主方向 | 已接受方向，構圖沒有衝突，姿勢、取景、焦段距離都不改；只把原本隱含的角度寫成明確欄位，並把在水面下、畫面外的腳鍊從 prompt 拿掉（中文標不入鏡）。 | 已接受方向：姿勢、取景與焦段距離都照 v3；只把身體正面、臉正面、相機在坐姿胸口高度平視寫明。 |
| V-rin-ayase | Penny 採用的 v2 替代方向 | 人物由置中改為右側、吧台改成對角線；臉改為三分之二側臉；黑色細帶高跟鞋多被及地長禮服蓋住，從 prompt 拿掉（中文標不入鏡）。 | 依 Penny 採用的替代方向（坐在金色燈光的吧台邊、不拿酒杯）；吧台改成對角線，比置中更有空間感；三分之二側臉適合她的五官。 |

**其他新企劃的小調整：**

| ID | 原景別 | 新設計 | 調整 |
|---|---|---|---|
| H-iris-chen | 膝上 | 全身｜正面｜臉正面・看鏡頭｜臀部高度・平視 | 景別由膝上改為全身，讓針織套裝與厚底涼鞋完整入鏡；姿勢、服裝、場景不變。 |
| H-coco-wu | 膝上 | 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視 | 人物由偏左改為置中、身體改為約30度斜側；相機由腰部改為胸口高度；膝上看不到的白色平底涼鞋與腳鍊從 prompt 拿掉。 |
| H-mia-huang | 膝上 | 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視 | 景別由膝上改為大腿中段以上，人物由偏左改為置中；白色厚底涼鞋不入鏡，從 prompt 拿掉。 |
| H-tammy-chou | 膝上 | 全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜膝蓋高度・輕仰 | 景別由膝上改為全身（高跟鞋入鏡），人物由偏左改為置中，相機改為膝蓋高度輕仰。 |
| H-rin-ayase | 斜躺全身 | 斜躺全身｜側面斜躺（朝畫面右）｜三分之二側臉・看鏡頭｜略高於她斜躺時頭部的高度・輕俯 | 把原本的「面向鏡頭斜躺」改寫成「雙腿側面、上身轉向鏡頭約45度」，並把相機由椅面高度改為略高於頭部輕俯。 |
| H-miu-shiraishi | 坐姿全身 | 坐姿全身｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 | 人物由偏左改為置中；身體寫明為上身約30度斜側、膝蓋斜向另一側。 |
| H-yerin-han | 坐姿全身 | 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 | 身體寫明為約45度斜側，球車改成斜放的對角線構圖；人物由偏左改為中央偏右。 |
| V-iris-chen | 膝上 | 大腿中段以上｜正面｜臉正面・看鏡頭｜胸口高度・平視 | 景別由膝上改為大腿中段以上；白色帆布鞋不入鏡，從 prompt 拿掉。 |
| V-luna-tanaka | 全身 | 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰 | 景別維持全身；相機由肚臍高度改為膝蓋高度輕仰，人物由置中改為略偏左。 |
| V-somi-oh | 膝上 | 全身｜正面｜臉正面・看鏡頭｜臀部高度・平視 | 景別由膝上改為全身，人物由置中改為略偏右。 |
| V-yuna-kim | 全身 | 全身｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜臀部高度・平視 | 身體由正面改為約30度斜側並加上往右的腳步；人物由置中改為略偏左；臉改為三分之二側臉。 |
| V-miu-shiraishi | 膝上 | 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視 | 景別由膝上改為大腿中段以上，人物由置中改為略偏左＋欄杆對角線；奶油色低跟鞋不入鏡，從 prompt 拿掉。 |
| V-jia-seo | 膝上 | 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜腰部高度・平視 | 身體由正面改為約30度斜側，兩側加上葉子框邊；白色細帶涼鞋不入鏡，從 prompt 拿掉。 |
| V-yerin-han | 膝上 | 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・輕仰 | 身體由正面改為約30度斜側、人物由置中改為略偏右；相機改為臀部高度輕仰；赤腳與腳鍊在膝上取景外，從 prompt 拿掉。 |

## 6. 尊重既有要求

| 要求 | 怎麼做 | 檢查 |
|---|---|---|
| Iris 兩款身體正面、有笑容，不回眸 | H 全身＋臀部高度平視、扶柱＋插腰、人物在左側三分之一；V 大腿中段以上＋胸口高度平視、插腰＋碰頭髮、置中 | 程式檢查：body=正面、臉正面、看鏡頭、prompt 有 smile、沒有回頭字樣 |
| Luna、Miu 取景與手不遮胸腰 | Luna H 兩手放大腿、V 雙手在身後；Miu H 雙手撐在身側床上、V 一手扶欄杆一手拿臉旁髮絲；景別都包含胸與腰 | 程式檢查姿勢句不含交叉手臂、擋在胸前等；「入鏡」欄寫明胸腰 |
| Yerin 性感可愛的高爾夫形象，不打球 | H 坐在球車上、球車與長腿成對角線；V 海灘 | 沿用 v3 禁字（club、driver、swing、iron、putter、cheer、pom） |
| Mia、Jia 去電競、去運動工作照；Jia 不棚拍 | Mia 碼頭與櫻花；Jia 美術館與溫室，都是實景 | 沿用 v3 禁字（gaming、headset、rgb、neon；studio、dance、sport、gym、sneakers、leggings） |
| 已接受方向保持 | H-somi-oh、V-coco-wu、H-rainie-hsu、V-rin-ayase 的場景與光線原文不動、取景不變；只拿掉不入鏡的鞋或腳鍊，並把姿勢句裡的「看鏡頭」移到視線欄 | 程式檢查 v3 場景與光線原文仍在 prompt 裡；V-coco 姿勢句與 v2 原文相同 |

## 7. prompt 一致性（逐套）

- 24 套都有七個攝影欄位，中文與英文成對；每個英文句都逐字出現在該套 prompt 裡（各一次）。
- 景別、焦段、距離、相機高度互相換算：裁切景別頭頂留白 4–10%，全身與坐姿人物佔畫面高度 82–90%，斜躺佔畫面寬度 80–90%；俯仰標示與換算結果一致。
- 沒有同時寫正面臉與完整側臉；完整側臉不看鏡頭的規則成立（本輪沒有用到完整側臉）。
- 非全身景別的 prompt 不含任何鞋、赤腳或腳鍊字樣；全身景別寫明腳與鞋完整。
- 胸上與腰上不寫放在膝上、腿旁或插腰的手；大腿中段以上不寫垂在身側或放在膝上的手（會落在邊緣）。
- 姿勢句不寫朝向（facing、toward the camera、at the camera 等），朝向只寫在 Body 與 Face 句，避免相機角度、身體方向、臉部方向混寫。
- 身體與頭部扭轉在 0–55 度；Iris 兩款身體正面、臉正面、看鏡頭、笑，沒有回眸字樣。
- 沿用 v3 的禁字檢查（Mia 去電競、Jia 不棚拍不運動、Yerin 不打球、Yuna 不靠地標文字等）、膚色只寫一次、adult。
- 同一位兩款服裝、場景仍不同；已接受方向（H-somi-oh、V-coco-wu、H-rainie-hsu、V-rin-ayase）的場景與光線原文不動；月份不變，且同一本相鄰月份不出現相同景別＋相同身體方向。

逐套數字（焦段與距離只是參考，不是生成保證）：

| ID | 景別 | 焦段／距離 | 視野（寬×高 m） | 人物或留白 | 相機高度／畫面中心（m） | 俯仰 | 臉的仰角 | 身體與頭扭轉 |
|---|---|---|---|---|---|---|---|---|
| H-iris-chen | 全身 | 50mm／4.7 m | 3.38×1.9 | 佔畫面高度 87% | 0.87／0.86 | -0.2°（平視） | 8.0° | 0° |
| H-luna-tanaka | 席地坐姿全身 | 50mm／2.3 m | 1.66×0.93 | 佔畫面高度 87% | 0.37／0.42 | +1.2°（平視） | 8.1° | -5° |
| H-somi-oh | 膝上 | 70mm／4.5 m | 2.31×1.3 | 頭頂留白 6% | 1.03／1.07 | +0.5°（平視） | 6.3° | 30° |
| H-coco-wu | 膝上 | 85mm／5.4 m | 2.29×1.29 | 頭頂留白 7% | 1.15／1.03 | -1.2°（平視） | 3.5° | 30° |
| H-mia-huang | 大腿中段以上 | 85mm／4.5 m | 1.91×1.07 | 頭頂留白 7% | 1.2／1.19 | -0.1°（平視） | 4.3° | 30° |
| H-yuna-kim | 腰上 | 85mm／3.2 m | 1.36×0.76 | 頭頂留白 7% | 1.02／1.0 | -0.4°（平視） | 3.3° | 10° |
| H-tammy-chou | 全身 | 50mm／4.8 m | 3.46×1.94 | 佔畫面高度 86% | 0.53／0.87 | +4.1°（輕仰） | 12.2° | 30° |
| H-rin-ayase | 斜躺全身 | 50mm／2.6 m | 1.87×1.05 | 佔畫面寬度 87% | 1.02／0.69 | -7.1°（輕俯） | -3.7° | 10° |
| H-rainie-hsu | 膝上 | 85mm／5.7 m | 2.41×1.36 | 頭頂留白 8% | 1.12／1.17 | +0.5°（平視） | 5.1° | 0° |
| H-miu-shiraishi | 坐姿全身 | 35mm／2.6 m | 2.67×1.5 | 佔畫面高度 87% | 0.72／0.68 | -0.9°（平視） | 10.5° | 30° |
| H-jia-seo | 全身 | 50mm／5.1 m | 3.67×2.07 | 佔畫面高度 85% | 0.95／0.93 | -0.3°（平視） | 7.7° | 55° |
| H-yerin-han | 坐姿全身 | 50mm／4.3 m | 3.1×1.74 | 佔畫面高度 87% | 0.84／0.78 | -0.7°（平視） | 7.0° | 45° |
| V-iris-chen | 大腿中段以上 | 85mm／2.9 m | 0.82×1.09 | 頭頂留白 8% | 1.19／1.18 | -0.1°（平視） | 6.7° | 0° |
| V-luna-tanaka | 全身 | 85mm／4.9 m | 1.38×1.84 | 佔畫面高度 86% | 0.47／0.83 | +4.2°（輕仰） | 11.6° | 0° |
| V-somi-oh | 全身 | 70mm／4.2 m | 1.44×1.92 | 佔畫面高度 85% | 0.87／0.86 | -0.0°（平視） | 8.9° | 0° |
| V-coco-wu | 坐姿到水面 | 70mm／2.7 m | 0.93×1.23 | 佔畫面高度 81% | 0.36／0.32 | -0.8°（平視） | 7.0° | 0° |
| V-mia-huang | 胸上 | 85mm／1.5 m | 0.42×0.56 | 頭頂留白 9% | 1.52／1.4 | -4.5°（輕俯） | 0.0° | -5° |
| V-yuna-kim | 全身 | 85mm／5.3 m | 1.5×2.0 | 佔畫面高度 87% | 0.92／0.9 | -0.3°（平視） | 7.4° | -5° |
| V-tammy-chou | 大腿中段以上 | 70mm／2.3 m | 0.79×1.05 | 頭頂留白 6% | 1.08／1.22 | +3.5°（輕仰） | 12.2° | 0° |
| V-rin-ayase | 坐姿全身 | 70mm／4.1 m | 1.41×1.87 | 佔畫面高度 86% | 0.98／0.84 | -1.9°（平視） | 7.2° | 10° |
| V-rainie-hsu | 膝上 | 85mm／3.6 m | 1.02×1.36 | 頭頂留白 7% | 1.09／1.14 | +0.8°（平視） | 8.1° | 55° |
| V-miu-shiraishi | 大腿中段以上 | 85mm／2.8 m | 0.79×1.05 | 頭頂留白 8% | 1.16／1.16 | -0.1°（平視） | 6.7° | 30° |
| V-jia-seo | 膝上 | 85mm／3.6 m | 1.02×1.36 | 頭頂留白 6% | 1.08／1.12 | +0.6°（平視） | 8.2° | 30° |
| V-yerin-han | 膝上 | 85mm／3.7 m | 1.04×1.39 | 頭頂留白 7% | 0.88／1.1 | +3.4°（輕仰） | 10.7° | 30° |

## 8. 自測結果

| 項目 | 結果 | 檔案 |
|---|---|---|
| 企劃頁（桌機＋390px）：資料層（24 套七欄位、英文句在 prompt、焦段距離一致、非全身不寫鞋、景別名稱、側臉與看鏡頭、扭轉、正面膝上只剩 1 套、6 套較大調整有原因、Iris／Rin 原文）；公開資料 v4、無 Soul ID／job_id／repo 路徑、免登入；24 張卡片直接顯示四格攝影列（不在展開區、看得到、與資料一致、在場景／服裝之上）、七欄位展開區、構圖示意在框內、兩本總覽表各 12 列 9 欄、手機改小卡、調整表 6 列；參考圖用途、Luna 不作身材參考；v1／v2／v3 舊回饋保留並標「不算 v4」、v3 題目與整體備註為舊版、題目仍 5 題；未回覆不算接受；回饋保存、重新整理、複製（含攝影列與舊版回饋）；清除 v4 只刪 v4；素材選擇不變；圖片載入、無水平溢出、放大、無 JS 錯誤 | 線上 111/111（本機 111/111） | review/calendar/m3_r3/live_shoot_v4_tests.tsv、local_shoot_v4_tests.tsv |
| 真實升版：同一個測試瀏覽器設定檔先在線上 v1（256859b）、v2（792d4f4）、v3（d56aee4）各填回饋，再打開線上 v4 | 11/11（localStorage 位元組相同；v1／v2／v3 顯示為舊版；v4 為 0／24；只開頁不改寫） | review/calendar/m3_r3/live_upgrade_v3_to_v4.tsv |
| 線上檔案 sha256 與本機比對（圖片、資料與頁面程式，加 4 個 HTML 頁） | 664 檔，不符 0；index、cast、plan、shoot 四個 HTML 頁與本機相同（頁面版本 8f061fc） | review/calendar/m3_r3/live_bytes_check.txt |
| 網站建置器 --check | PASS：654 檔，問題 0；ASSET_MANIFEST.json 與上一版位元組相同 | — |
| 文件產生器 --check | PASS；CAL_19 與上一版位元組相同 | — |
| kol-catalog 首頁 | 與上一輪存檔位元組相同（200，44801 bytes） | — |

測試與產生資料時的修正（照實記錄）：

- 產生程式的檢查擋下：V-coco-wu 的腳鍊在水面下、畫面外（從 prompt 拿掉，中文標不入鏡）；V-rin-ayase 的及地長禮服蓋住雙腳，和「坐姿全身要雙腳完整」衝突（改成下緣在禮服下襬下方，鞋從 prompt 拿掉）；H-coco-wu 原本是第二張正面膝上站姿（改為約30度斜側）。
- 檢查本身過寬兩次：「nothing covering her chest or waist」被「covering her」誤擋（改成只檢查姿勢句、只擋遮住胸腰身體的寫法）；頁面測試的「沒有半身」誤中 Rin 的「下半身側面」（改寫成「雙腿側面」，英文本來就是 legs）。
- 措辭修正：Yuna H 與 Rin V 的英文出現兩次 toward；Rin H 的相機高度句改成「a height slightly above her head」；Rin H 上下界與入鏡內容重複，刪掉重複句；正面姿勢的「shoulders and hips square」與方向句重複，改寫肩線。
- 頁面：構圖示意的說明文字原本蓋在框的上緣、壓到頭的位置，改放到框下方；景別與身體方向的統計順序被資料的鍵排序打亂，改成固定順序；手機總覽的欄名欄加寬。都在部署前修正。

## 9. 截圖與覆核檔案（完整路徑）

截圖都來自線上企劃頁（8f061fc）；`oldfb_` 開頭的是帶 v1／v2／v3 測試回饋的畫面，`upgraded_` 開頭的是真實升版後的畫面。

- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_books_both_tables.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_card_H-jia_camera_detail.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_card_V-iris_camera_detail.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_composition.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_iris_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_jia_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_luna_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_mia_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_miu_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_photo_overview.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_rainie_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_requirement_decisions.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_rin_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_desktop_yuna_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_mobile390_card_H-iris.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_mobile390_card_H-rin.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_mobile390_card_V-iris.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_mobile390_card_V-mia.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_mobile390_luna_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_mobile390_photo_overview_H.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_mobile390_photo_overview_V.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_mobile390_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/oldfb_live_desktop_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/oldfb_live_desktop_iris_with_old_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/oldfb_live_desktop_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/oldfb_live_mobile390_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/oldfb_live_mobile390_iris_with_old_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/oldfb_live_mobile390_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/upgraded_feedback_section_v4.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/upgraded_iris_old_feedback_v4.jpg`

覆核檔案：

- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_shoot_v4_tests.tsv`、`/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/local_shoot_v4_tests.tsv`、`/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_upgrade_v3_to_v4.tsv`、`/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/live_bytes_check.txt`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/copy_example_unanswered_with_old.txt`、`/home/user/Virtual_KOL_Studio/review/calendar/m3_r3/copy_example_answered.txt`（測試用假回饋的複製結果）
- `/home/user/Virtual_KOL_Studio/docs/calendar/data/cal_m3_shoot_plan.json`、`/home/user/Virtual_KOL_Studio/docs/calendar/data/cal_m3_owner_feedback_r3.json`、`/home/user/Virtual_KOL_Studio/docs/calendar/CAL_18_M3_SHOOT_PLAN.md`

## 10. 操作紀錄

| # | 動作 | 性質 |
|---|---|---|
| 1 | 定向讀：本輪指令（從本次對話紀錄取出原文，供逐字保存）、上一版企劃資料（git d56aee4）、R2 owner 紀錄、企劃頁程式、文件產生器、網站建置器的 M-3 段落；沒有掃描整個 repo | 唯讀 |
| 2 | 在線上 v3 頁（d56aee4）用測試瀏覽器設定檔（已有 v1、v2 回饋）再填 v3 測試回饋，供升版測試 | 只在本機測試瀏覽器；不影響 Penny 的瀏覽器 |
| 3 | 本機產生 shoot-plan-v4、R3 owner 紀錄、CAL_18；建置網站資料並 --check；本機伺服器測試與截圖（本機 pkill 誤關了自己的 shell 一次，改用背景執行伺服器） | 本機 |
| 4 | commit 8f061fc，push 到 claude/epic-carson-n5w0qu | 未合併 main、未開 PR |
| 5 | Railway 只把 cal2027-decision 固定到 8f061fc（d4ed4fac-3d69-414d-91a6-a8f09b180f20） | 其他 service 未動、沒有新增付費服務 |
| 6 | 線上升版驗證、頁面測試、檔案比對、截圖；讀 kol-catalog 首頁比對 | 唯讀 |
| 7 | 寫本送審紀錄並 commit、push | — |

**本輪數字：** 生成 0、credits 0、訓練 0、上傳 0、Higgsfield 呼叫 0、聯絡廠商 0。
