TASK-CAL-001／M-3／R3｜24 套寫真景別、角度與構圖細化｜送審報告

# CAL_18 — M-3 24 套雙款寫真企劃與攝影設計（shoot-plan-v4）

> 資料檔：`data/cal_m3_shoot_plan.json`（shoot-plan-v4，R3，2026-10-19）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。
> **僅規劃：沒有生成任何圖片（含測試圖、示意圖），沒有花 credits，沒有上傳，沒有訓練，沒有改 canon 或 Soul ID。** 本輪生成數 0、credits 0、訓練數 0。
> 這是企劃，不是核准：24 套內容、景別與角度、月份、版面與 H／V 分配都待 Penny 拍板；生成與費用都未授權。R2 的 Owner 決策逐字紀錄見 `CAL_19_M3_R2_OWNER_DECISION.md`。

## 0. 版本

| 項目 | 內容 |
|---|---|
| 名單 | roster-v1（docs/calendar/data/cal_m1_owner_roster.json）；不換人 |
| 上一版企劃 | shoot-plan-v3（commit `d56aee44b6cd8aabdedb8e1eda36fdc7f20980f8`） |
| 這一版 | 依 Penny 要求逐套補上攝影設計（景別、畫面上下界、身體朝向、臉部朝向與視線、相機高度與俯仰、畫面配置、攝影目的），中文與 prompt 同步；服裝與場景沿用 v3，景別與角度是推薦、待 Penny 定案。 |
| 素材頁版本 | `b8108eb648a46a57e3bb4dc2158cf878c23d7963` |
| 桌曆基準 | `4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45` |

**參考照片：** 參考照片都是既有照片，只按標示的用途參考（表情／場景／服裝材質／身分），不是新企劃的成品，也不會照抄；身材一律以設定數字為準。既有照片也不是新構圖的成品。

## 1. R3：Penny 最新要求（逐字，主管轉述）

> 資料檔：`data/cal_m3_owner_feedback_r3.json`（2026-10-19）。M-3／R3 Penny 最新要求逐字紀錄（主管轉述）。只保存需求原文；本輪執行的攝影設計是推薦，不是 owner 核准。

```text
【Penny 最新要求】
每張寫真必須明確規劃景別、拍攝角度與構圖。
可以安排半身、全身、較近的臉部特寫、大腿以上等不同景別，
並細緻規劃正面、側面等角度。
不能只說服裝、場景、姿態，讓模型自行決定怎麼拍。

現有技術區雖有部分景別，但不夠直觀，整組也過度集中正面膝上。
本輪補齊攝影設計，不全面推翻已規劃的服裝與場景。

維持：
- 12 位、24 套獨立拍攝。
- 同人 H／V 的服裝與場景不同。
- 兩本月份排序不同，仍待 Penny 定案。
- 專業美女寫真，以人物魅力與設定身材為核心。
- Iris 兩款身體正面、有笑容，不改回背部回眸。
- 生成與費用尚未授權。
```

```text
三、尊重既有要求
Iris：
兩款身體正面、有笑容。
可以透過景別、相機高度、手部與畫面配置做差異，
不能再變成背部回眸。

Luna、Miu：
取景與手部不能把胸型、腰線全部遮住。
身材依設定，不照抄舊圖錯誤比例。

Yerin：
性感可愛的高爾夫形象寫真，不打球、不展示球技。

Mia、Jia：
維持去電競、去運動工作照；Jia 不改回棚拍。

其他已接受方向保持，只有構圖確有衝突才調整，
並明確列出調整原因。
```

```text
Penny 尚未批准其餘人物的具體角度。
你可以提出推薦，不能寫成 owner 已核准。
```

**落實方式：** 24 套都補上七個攝影欄位（景別、畫面上下界、身體朝向、臉部朝向與視線、相機高度與俯仰、畫面配置、攝影目的），中文欄位與英文 prompt 由同一份設定產生並逐套檢查。服裝與場景沿用 v3；這些景別與角度都是執行者的推薦，待 Penny 定案（Iris 的「身體正面、有笑容」是 Penny 已提出的要求）。

**共同規則：**

- 景別依 Penny 指定的名稱：胸上／腰上／大腿中段以上／膝上／全身，坐姿與斜躺另寫「坐姿全身」「席地坐姿全身」「斜躺全身」，池邊坐姿寫「坐姿到水面」。不用含糊的「半身」。Rin 的及地長禮服蓋住雙腳，她的坐姿全身下緣寫在禮服下襬下方。
- 裁切不落在關節：膝上切在膝蓋下方的小腿上段；大腿中段以上切在膝蓋上方很遠；腰上切在腰線下方、臀部上方；胸上切在胸線下方、手肘上方。所有景別都保留完整髮頂。
- 鞋只在腳會入鏡的景別（全身、坐姿全身、席地坐姿全身、斜躺全身）寫進 prompt；其他景別的鞋在中文服裝欄標「不入鏡」，不當成這張照片的賣點。
- 身體朝向、臉部朝向、相機高度分開寫：身體用「正面／約30度斜側／約45度斜側／側面」，臉用「臉正面／三分之二側臉」，相機寫「她的哪個高度＋平視／輕俯／輕仰」。
- 俯仰由「畫面中心高度」與「相機高度」換算：差距小於約 2.5 度寫平視，2.5–8.5 度寫輕俯或輕仰，超過就讓建置失敗；也檢查相機到臉的仰角不超過 15 度，避免由下往上拍到鼻孔。
- 身體與頭部的扭轉不超過約 60 度（側身站姿、臉轉成三分之二側臉約 55 度）；完整側臉不能同時寫看鏡頭。24 套都沒有背面或回眸。
- 焦段與距離只是給模型的合理參考，比例換算不是生成保證。本輪不新增固定的日期區，也不做未確認的印刷承諾。

## 2. 兩本攝影總覽（推薦，待 Penny 定案）

### 2.1 橫式款（16:9）

| 月份（推薦） | 人物 | 景別 | 身體方向 | 臉部方向 | 視線 | 相機角度 | 人物位置 | 主要展示重點 |
|---|---|---|---|---|---|---|---|---|
| 1 月 | Yuna（H-yuna-kim） | 腰上 | 約45度斜側（朝畫面左） | 三分之二側臉 | 看鏡頭 | 坐姿時的肩膀高度・平視 | 右側約六成（左側窗光） | 水光肌與眼妝、通透窗光 |
| 2 月 | Rin（H-rin-ayase） | 斜躺全身 | 側面斜躺（朝畫面右） | 三分之二側臉 | 看鏡頭 | 略高於她斜躺時頭部的高度・輕俯 | 橫跨中央（頭在左、腳在右） | 斜躺 S 形曲線與長腿 |
| 3 月 | Miu（H-miu-shiraishi） | 坐姿全身 | 約30度斜側（朝畫面右） | 臉正面 | 看鏡頭 | 坐姿時的腰部高度・平視 | 置中（窗與床邊架左右平衡） | 胸型與很細的腰線、甜笑 |
| 4 月 | Tammy（H-tammy-chou） | 全身 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 膝蓋高度・輕仰 | 置中（展示櫃對稱） | 合身洋裝全身線條、高跟鞋與腿長 |
| 5 月 | Yerin（H-yerin-han） | 坐姿全身 | 約45度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 坐姿時的腰部高度・平視 | 中央偏右（球車與長腿成對角線） | 長腿、可愛笑容、高爾夫裝扮 |
| 6 月 | Coco（H-coco-wu） | 膝上 | 約30度斜側（朝畫面右） | 臉正面 | 看鏡頭 | 胸口高度・平視 | 置中（花壟對稱收攏） | 大笑、V 領胸型與收腰 |
| 7 月 | Mia（H-mia-huang） | 大腿中段以上 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 胸口高度・平視 | 置中（摩天輪光點在右肩後） | 馬甲胸腰比例、俏皮眨眼 |
| 8 月 | Iris（H-iris-chen） | 全身 | 正面 | 臉正面 | 看鏡頭 | 臀部高度・平視 | 左側三分之一（騎樓往右延伸） | 針織套裝全身比例、城市騎樓 |
| 9 月 | Jia（H-jia-seo） | 全身 | 側面（朝畫面左） | 三分之二側臉 | 看鏡頭 | 臀部高度・平視 | 置中（兩幅畫對稱） | 直角肩、細腰、修長線條 |
| 10 月 | Luna（H-luna-tanaka） | 席地坐姿全身 | 約30度斜側（朝畫面左） | 三分之二側臉 | 看向畫面左側紙拉門透進的晨光（不看鏡頭） | 坐姿時的胸口高度・平視 | 右側約六成（左側留給窗光與視線） | 斜側胸腰曲線、安靜的側臉 |
| 11 月 | Somi（H-somi-oh） | 膝上 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 腰部高度・平視 | 偏左（吧台往右延伸） | 腰臀曲線、交叉的腿、月牙眼大笑 |
| 12 月 | Rainie（H-rainie-hsu） | 膝上 | 正面 | 臉正面 | 直視鏡頭 | 腰部高度・平視 | 偏右（左側城市燈海） | 氣場、馬甲胸腰線、高衩腿線 |

**景別：** 腰上 1、大腿中段以上 1、膝上 3、全身 3、坐姿全身 2、席地坐姿全身 1、斜躺全身 1；**身體方向：** 正面 2、約30度斜側 6、約45度斜側 2、側面斜躺 1、側面 1。

**節奏：** 橫式款以「人＋環境」為主，但不再一律膝上：全身 3（Iris 騎樓、Tammy 精品店、Jia 美術館）、坐／躺全身 4（Luna、Miu、Yerin、Rin）、膝上 3（Somi、Coco、Rainie）、大腿中段以上 1（Mia）、腰上 1（Yuna）。人物位置：置中 5、偏一側 5（其中 2 張是已接受的構圖）、斜躺橫跨與對角線各 1；偏一側的每張都有理由（透視線、視線方向、人物佔大半畫面），不是一側大面積空景。

**依推薦月份的景別順序：** 1月 腰上（Yuna）→2月 斜躺全身（Rin）→3月 坐姿全身（Miu）→4月 全身（Tammy）→5月 坐姿全身（Yerin）→6月 膝上（Coco）→7月 大腿中段以上（Mia）→8月 全身（Iris）→9月 全身（Jia）→10月 席地坐姿全身（Luna）→11月 膝上（Somi）→12月 膝上（Rainie）

### 2.2 直式款（3:4）

| 月份（推薦） | 人物 | 景別 | 身體方向 | 臉部方向 | 視線 | 相機角度 | 人物位置 | 主要展示重點 |
|---|---|---|---|---|---|---|---|---|
| 1 月 | Tammy（V-tammy-chou） | 大腿中段以上 | 正面 | 臉正面 | 看鏡頭 | 腰部高度・輕仰 | 置中（吊燈在頭頂上方） | 自信姿態、深 V 翻領與腰帶的胸腰比例 |
| 2 月 | Jia（V-jia-seo） | 膝上 | 約30度斜側（朝畫面右） | 臉正面 | 看鏡頭 | 腰部高度・平視 | 置中（葉子框住兩側） | 細腰、臀線、開衩腿線 |
| 3 月 | Mia（V-mia-huang） | 胸上 | 約30度斜側（朝畫面右） | 三分之二側臉 | 看鏡頭 | 眼睛高度・輕俯 | 略偏左（花枝框住右上） | 臉與甜笑、露肩領口與胸型 |
| 4 月 | Miu（V-miu-shiraishi） | 大腿中段以上 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 胸口高度・平視 | 略偏左（欄杆對角線） | V 領胸型、細腰帶腰線 |
| 5 月 | Rainie（V-rainie-hsu） | 膝上 | 側面（朝畫面右） | 三分之二側臉 | 直視鏡頭 | 腰部高度・平視 | 左側約四成（右側街道倒影） | 側身曲線、長風衣直線、氣場 |
| 6 月 | Luna（V-luna-tanaka） | 全身 | 正面 | 臉正面 | 看鏡頭 | 膝蓋高度・輕仰 | 略偏左（約四成） | 整件洋裝、胸腰比例、腿長 |
| 7 月 | Coco（V-coco-wu） | 坐姿到水面 | 正面 | 臉正面 | 看鏡頭 | 坐姿時的胸口高度・平視 | 置中（水面在下） | 比基尼胸腰線條、歪頭大笑 |
| 8 月 | Yerin（V-yerin-han） | 膝上 | 約30度斜側（朝畫面左） | 臉正面 | 看鏡頭 | 臀部高度・輕仰 | 略偏右（天空在上方與左側） | 修長身形、健康的胸腰臀曲線 |
| 9 月 | Iris（V-iris-chen） | 大腿中段以上 | 正面 | 臉正面 | 看鏡頭 | 胸口高度・平視 | 置中 | Penny 指定穿搭：短上衣胸型、露腰、牛仔迷你裙；笑容 |
| 10 月 | Rin（V-rin-ayase） | 坐姿全身 | 約45度斜側（朝畫面左） | 三分之二側臉 | 看鏡頭 | 坐姿時的腰部高度・平視 | 右側約六成（吧台對角線在左） | 絲絨上身胸腰、交疊長腿、側臉輪廓 |
| 11 月 | Yuna（V-yuna-kim） | 全身 | 約30度斜側（朝畫面右） | 三分之二側臉 | 看鏡頭 | 臀部高度・平視 | 略偏左（右側大道延伸） | 腿長、毛呢套裝與長靴 |
| 12 月 | Somi（V-somi-oh） | 全身 | 正面 | 臉正面 | 看鏡頭 | 臀部高度・平視 | 略偏右（約六成） | 冬季整體造型、洋裝胸腰臀線 |

**景別：** 胸上 1、大腿中段以上 3、膝上 3、全身 3、坐姿全身 1、坐姿到水面 1；**身體方向：** 正面 5、約30度斜側 5、約45度斜側 1、側面 1。

**節奏：** 直式款以「身形修長」為主：全身 3（Luna、Somi、Yuna）、坐姿 2（Rin 高腳椅、Coco 池邊）、膝上 3（Rainie、Jia、Yerin）、大腿中段以上 3（Iris、Tammy、Miu）、胸上 1（Mia）。站姿置中只有 Iris、Tammy、Jia 三張，景別各不相同；其他偏左、偏右或用對角線。

**依推薦月份的景別順序：** 1月 大腿中段以上（Tammy）→2月 膝上（Jia）→3月 胸上（Mia）→4月 大腿中段以上（Miu）→5月 膝上（Rainie）→6月 全身（Luna）→7月 坐姿到水面（Coco）→8月 膝上（Yerin）→9月 大腿中段以上（Iris）→10月 坐姿全身（Rin）→11月 全身（Yuna）→12月 全身（Somi）

**近景：** 近景只有兩張：V-mia-huang 胸上、H-yuna-kim 腰上；兩人的另一款都保留身材展示（Mia 大腿中段以上、Yuna 全身），不因近景減少身材展示。沒有安排純臉部特寫，因為這本桌曆以人物魅力與設定身材為核心。

**角度：** 正面膝上站姿只剩 1 張（H-rainie-hsu，已接受方向，背靠欄杆本來就正對鏡頭）。側面 3 張（H-jia-seo 側身全身、V-rainie-hsu 側身膝上、H-rin-ayase 側面斜躺），都是為了身體線條；只有 H-luna-tanaka 不看鏡頭（看向窗光）。

**同一位的兩款：** 12 位中有 11 位的 H／V 景別不同；Rainie 兩款都是膝上，但橫式款正面背靠欄杆、直式款側身，角度完全不同。每位的兩款在身體方向或相機高度上也都有差異（Iris 兩款都正面，用全身＋臀部高度 vs 大腿中段以上＋胸口高度區分）。

### 2.3 prompt 一致性檢查（產生資料時逐套執行，不通過就無法建置）

- 24 套都有七個攝影欄位，中文與英文成對；每個英文句都逐字出現在該套 prompt 裡（各一次）。
- 景別、焦段、距離、相機高度互相換算：裁切景別頭頂留白 4–10%，全身與坐姿人物佔畫面高度 82–90%，斜躺佔畫面寬度 80–90%；俯仰標示與換算結果一致。
- 沒有同時寫正面臉與完整側臉；完整側臉不看鏡頭的規則成立（本輪沒有用到完整側臉）。
- 非全身景別的 prompt 不含任何鞋、赤腳或腳鍊字樣；全身景別寫明腳與鞋完整。
- 胸上與腰上不寫放在膝上、腿旁或插腰的手；大腿中段以上不寫垂在身側或放在膝上的手（會落在邊緣）。
- 姿勢句不寫朝向（facing、toward the camera、at the camera 等），朝向只寫在 Body 與 Face 句，避免相機角度、身體方向、臉部方向混寫。
- 身體與頭部扭轉在 0–55 度；Iris 兩款身體正面、臉正面、看鏡頭、笑，沒有回眸字樣。
- 沿用 v3 的禁字檢查（Mia 去電競、Jia 不棚拍不運動、Yerin 不打球、Yuna 不靠地標文字等）、膚色只寫一次、adult。
- 同一位兩款服裝、場景仍不同；已接受方向（H-somi-oh、V-coco-wu、H-rainie-hsu、V-rin-ayase）的場景與光線原文不動；月份不變，且同一本相鄰月份不出現相同景別＋相同身體方向。

## 3. 調整較大的套數與理由

「調整較大」的判定：景別跨兩級以上（胸上→腰上→大腿中段以上→膝上→全身／坐姿），或身體改為側面，或視線改為不看鏡頭，或場景細節與光線方向配合改寫。其餘 18 套是補齊角度與構圖、拿掉不入鏡的鞋等小調整。

| ID | 原景別 | 新設計 | 調整較大的原因 | 調整內容 | 理由 |
|---|---|---|---|---|---|
| H-luna-tanaka | 席地坐姿全身 | 席地坐姿全身｜約30度斜側（朝畫面左）｜三分之二側臉・看向窗光（畫面左）｜坐姿時的胸口高度・平視 | 視線改為不看鏡頭 | 視線由看鏡頭改為看向畫面左側的窗光（三分之二側臉）；身體改為約30度斜側。服裝與場景不變。 | Luna 的人設是「住在美麗白日夢裡的人」：24 套裡唯一不看鏡頭的一張，三分之二側臉仍能認人；直式款看鏡頭。相機放在她坐姿胸口高度平視，不俯拍，避免嬌小的她顯得更小。 |
| H-yuna-kim | 坐姿全身 | 腰上｜約45度斜側（朝畫面左）｜三分之二側臉・看鏡頭｜坐姿時的肩膀高度・平視 | 景別由坐姿全身改為腰上、場景細節與光線方向配合改寫 | 景別由坐姿全身改為腰上；姿勢改為「前臂搭窗台、手放鎖骨旁」，原本放在膝上的手會被裁掉；光線改寫為窗戶在畫面左側；白色平底鞋不入鏡。 | Yuna 的韓系感來自妝髮、色調與光：橫式用 24 套中唯一的腰上近景，讓臉與通透窗光成為主角；168 公分的腿長由直式款全身負責。 |
| H-jia-seo | 膝上 | 全身｜側面（朝畫面左）｜三分之二側臉・看鏡頭｜臀部高度・平視 | 身體改為側面 | 景別由膝上改為全身；身體由正面改為側面、臉改為三分之二側臉；人物由偏左改為置中＋兩幅畫對稱；手改為「靠鏡頭的手插臀側、露出腰側鏤空」。 | Jia 偏冷、俐落，側身最能表現直角肩與長腿；臉轉回鏡頭約55度成三分之二側臉，仍能認人，不是回眸。置中＋對稱畫作讓橫式不是「人在一側、另一側空景」。 |
| V-mia-huang | 膝上 | 胸上｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜眼睛高度・輕俯 | 景別由膝上改為胸上 | 景別由膝上改為胸上；白色及膝長靴不入鏡，從 prompt 拿掉；另一手改寫成「自然垂下、不入鏡」。 | 24 套中唯一的胸上近景，放在表情最豐富的 Mia；她的身形由橫式款的大腿中段以上負責，所以這張不會大幅減少身材展示。眼睛高度輕俯是常見的美顏角度，不會變形。 |
| V-tammy-chou | 全身 | 大腿中段以上｜正面｜臉正面・看鏡頭｜腰部高度・輕仰 | 景別由全身改為大腿中段以上 | 景別由全身改為大腿中段以上；黑色細高跟鞋不入鏡，從 prompt 拿掉；相機改為腰部高度輕仰。 | 高跟鞋已由橫式款全身呈現；直式款改大腿中段以上，正面插腰配腰部高度輕仰，拍出大飯店夜晚的氣場。 |
| V-rainie-hsu | 膝上 | 膝上｜側面（朝畫面右）｜三分之二側臉・看鏡頭｜腰部高度・平視 | 身體改為側面 | 身體由正面改為側面、臉改為三分之二側臉；人物由置中改為左側約四成；黑色短靴不入鏡，從 prompt 拿掉。 | 她的高顴骨與立體下顎適合側面；24 套中唯一的「側身站姿＋膝上」，與橫式款的正面靠欄杆完全不同。頭轉回鏡頭約55度，在自然範圍內，不是回眸。 |

**其他 18 套（含已接受方向）：**

| ID | 來源 | 原景別 | 新設計 | 調整內容 |
|---|---|---|---|---|
| H-iris-chen | 新企劃 | 膝上 | 全身｜正面｜臉正面・看鏡頭｜臀部高度・平視 | 景別由膝上改為全身，讓針織套裝與厚底涼鞋完整入鏡；姿勢、服裝、場景不變。 |
| H-somi-oh | Penny 已接受的 v2 主方向 | 膝上 | 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜腰部高度・平視 | 已接受方向，只做必要調整：膝上取景看不到鞋，棕色樂福鞋從 prompt 拿掉（中文標不入鏡）；姿勢句的「看鏡頭」移到視線欄。 |
| H-coco-wu | 新企劃 | 膝上 | 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視 | 人物由偏左改為置中、身體改為約30度斜側；相機由腰部改為胸口高度；膝上看不到的白色平底涼鞋與腳鍊從 prompt 拿掉。 |
| H-mia-huang | 新企劃 | 膝上 | 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視 | 景別由膝上改為大腿中段以上，人物由偏左改為置中；白色厚底涼鞋不入鏡，從 prompt 拿掉。 |
| H-tammy-chou | 新企劃 | 膝上 | 全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜膝蓋高度・輕仰 | 景別由膝上改為全身（高跟鞋入鏡），人物由偏左改為置中，相機改為膝蓋高度輕仰。 |
| H-rin-ayase | 新企劃 | 斜躺全身 | 斜躺全身｜側面斜躺（朝畫面右）｜三分之二側臉・看鏡頭｜略高於她斜躺時頭部的高度・輕俯 | 把原本的「面向鏡頭斜躺」改寫成「雙腿側面、上身轉向鏡頭約45度」，並把相機由椅面高度改為略高於頭部輕俯。 |
| H-rainie-hsu | Penny 已接受的 v2 主方向 | 膝上 | 膝上｜正面｜臉正面・看鏡頭｜腰部高度・平視 | 已接受方向，只做必要調整：膝上取景看不到鞋，黑色細帶高跟涼鞋從 prompt 拿掉（中文標不入鏡）；姿勢句的「直視鏡頭」移到視線欄。 |
| H-miu-shiraishi | 新企劃 | 坐姿全身 | 坐姿全身｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 | 人物由偏左改為置中；身體寫明為上身約30度斜側、膝蓋斜向另一側。 |
| H-yerin-han | 新企劃 | 坐姿全身 | 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 | 身體寫明為約45度斜側，球車改成斜放的對角線構圖；人物由偏左改為中央偏右。 |
| V-iris-chen | 新企劃 | 膝上 | 大腿中段以上｜正面｜臉正面・看鏡頭｜胸口高度・平視 | 景別由膝上改為大腿中段以上；白色帆布鞋不入鏡，從 prompt 拿掉。 |
| V-luna-tanaka | 新企劃 | 全身 | 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰 | 景別維持全身；相機由肚臍高度改為膝蓋高度輕仰，人物由置中改為略偏左。 |
| V-somi-oh | 新企劃 | 膝上 | 全身｜正面｜臉正面・看鏡頭｜臀部高度・平視 | 景別由膝上改為全身，人物由置中改為略偏右。 |
| V-coco-wu | Penny 已接受的 v2 主方向 | 坐姿到水面 | 坐姿到水面｜正面｜臉正面・看鏡頭｜坐姿時的胸口高度・平視 | 已接受方向，構圖沒有衝突，姿勢、取景、焦段距離都不改；只把原本隱含的角度寫成明確欄位，並把在水面下、畫面外的腳鍊從 prompt 拿掉（中文標不入鏡）。 |
| V-yuna-kim | 新企劃 | 全身 | 全身｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜臀部高度・平視 | 身體由正面改為約30度斜側並加上往右的腳步；人物由置中改為略偏左；臉改為三分之二側臉。 |
| V-rin-ayase | Penny 採用的 v2 替代方向 | 坐姿全身 | 坐姿全身｜約45度斜側（朝畫面左）｜三分之二側臉・看鏡頭｜坐姿時的腰部高度・平視 | 人物由置中改為右側、吧台改成對角線；臉改為三分之二側臉；黑色細帶高跟鞋多被及地長禮服蓋住，從 prompt 拿掉（中文標不入鏡）。 |
| V-miu-shiraishi | 新企劃 | 膝上 | 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視 | 景別由膝上改為大腿中段以上，人物由置中改為略偏左＋欄杆對角線；奶油色低跟鞋不入鏡，從 prompt 拿掉。 |
| V-jia-seo | 新企劃 | 膝上 | 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜腰部高度・平視 | 身體由正面改為約30度斜側，兩側加上葉子框邊；白色細帶涼鞋不入鏡，從 prompt 拿掉。 |
| V-yerin-han | 新企劃 | 膝上 | 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・輕仰 | 身體由正面改為約30度斜側、人物由置中改為略偏右；相機改為臀部高度輕仰；赤腳與腳鍊在膝上取景外，從 prompt 拿掉。 |

## 4. R2 Penny 回饋落實表（不變）

| 人設 | Penny 回饋（逐字） | 怎麼落實 | 橫式款 | 直式款 |
|---|---|---|---|---|
| Iris | Iris： - 更顯身材的上衣，搭牛仔迷你裙。 - 身體面向鏡頭，專業寫真姿態、有笑容。 - 不要背部回眸或轉頭看鏡頭。 | 更顯身材的上衣：V 白色貼身方領短上衣（露腰）；H 貼身羅紋針織平口；牛仔迷你裙：V 淺藍高腰牛仔迷你裙；身體面向鏡頭、專業姿態、有笑容：兩款都正面站定（扶柱／插腰／碰髮）並微笑；不要背部回眸或轉頭：兩款 prompt 經程式檢查，不含回頭、轉身字樣 | 午後紅磚騎樓裡，穿米杏色針織套裝的 Iris 正面站定、對鏡頭笑。 | 黃金時段的河濱草地，白色方領短上衣配牛仔迷你裙，正面站著甜笑（Penny 指定的穿搭）。 |
| Luna | Luna： - 衣服要顯身材。 - 既有參考照片的身材不符合設定。 - 只能借表情／環境，不能當身材標準。 | 衣服顯身材：H 貼身緞面細肩洋裝；V 心形領有骨架的貼身洋裝；既有照片身材不符：所有 Luna 參考照片都標「不作身材參考」，身材依設定數字；只借表情／環境：參考用途只標「表情」與「場景」 | 清晨的京都町家和室，象牙白蕾絲緞面細肩洋裝，席地而坐的安靜微笑。 | 紫陽花盛開的町家庭院，鼠尾草綠馬甲感洋裝，正面站在石板路上。 |
| Somi | Somi：接受新版暖橘復古棚景主方向。（以上各保留為其中一款，再另設完全不同的一款。） | 接受暖橘復古棚景：H-somi-oh 沿用 v2 原文（含炸雞只在橫幅邊緣）；另一款完全不同：V 雪夜溫泉小鎮、白色針織洋裝＋紅色長大衣 | Penny 已接受的方向：暖橘復古小吃店棚景，針織短開襟＋高腰針織短裙，輕靠吧台大笑。 | 下雪的溫泉小鎮夜晚，象牙白貼身針織洋裝外披紅色長大衣，在燈籠光裡大笑。 |
| Coco | Coco：接受泳池主方向。（以上各保留為其中一款，再另設完全不同的一款。） | 接受泳池：V-coco-wu 沿用 v2 原文；另一款完全不同：H 初夏薰衣草花田、白色亞麻洋裝 | 初夏傍晚的薰衣草花田，白色細肩亞麻洋裝，拿著草帽大笑。 | Penny 已接受的方向：週末飯店泳池，薄荷綠比基尼＋淺紫透膚罩衫，坐在池邊大笑。 |
| Mia | Mia： - 場景、服裝全面去電競化。 - 原咖啡座替代方案太普通，兩款重新設計。 - 不放電競椅、耳機、RGB房間等職業符號。 | 全面去電競化：兩款都沒有電競椅、耳機、RGB 房間或霓虹（程式檢查）；咖啡座太普通、兩款重設：H 夏日黃昏遊樂碼頭；V 春夜櫻花步道 | 夏日黃昏的海邊遊樂碼頭，粉色緞面馬甲上衣配白色迷你裙，拿著棉花糖俏皮眨眼。 | 春夜的櫻花河岸步道，淺紫貼身露肩針織洋裝，站在花枝下甜笑。 |
| Yuna | Yuna： - 普通白色公寓不足。 - 需要更具韓系氛圍的專業寫真。 - 用服裝、妝髮、色調、場景與攝影建立韓系美感，   不靠文字標籤、國旗或隨意塞韓國地標。 | 普通白色公寓不足：兩款都不在公寓；韓系氛圍：H 通透的咖啡館（水光肌、奶油黃＋淺藍）；V 銀杏大道（毛呢短外套套裝＋長靴、柔和底片感）；不靠文字、國旗、地標：prompt 不含國旗、韓文、地名或招牌（程式檢查） | 明亮通透的感性咖啡館，奶油黃短版開襟配淺藍緞面中長裙，坐在窗邊的清透美感。 | 深秋的銀杏大道，奶油色毛呢短外套套裝配黑色長靴，站在落葉上的韓劇感街拍寫真。 |
| Tammy | Tammy： - 已提的合身洋裝與高跟鞋方向可保留。 - 重新安排與穿搭匹配的高級場景。 - 不是任意白牆或普通階梯。 | 保留合身洋裝＋高跟鞋：H 熱粉方領針織洋裝＋白色露跟高跟鞋；高級場景：H 精品店；V 大飯店大廳（白色西裝洋裝＋黑色細高跟）；不是白牆或普通階梯：prompt 不含階梯與白牆（程式檢查） | 高級精品店裡，熱粉色貼身針織洋裝配白色露跟高跟鞋，站在展示櫃旁的明亮笑容。 | 夜晚的大飯店大廳，白色西裝外套洋裝配黑色細跟鞋，雙手插腰的自信全身照。 |
| Rin | Rin：採用 shoot-plan-v2 的替代方向。 先精確讀出原替代內容，不猜測或自行替換。 作為其中一款，另一款另設不同服裝與場景。 | v2 替代方向逐字讀出：「出勤前的銀座：黑色絲絨細肩帶長禮服，坐在金色燈光的吧台邊（不拿酒杯）。」→ V-rin-ayase 依原文（黑色絲絨細肩帶長禮服、金色燈光吧台、不拿酒杯）；另一款不同服裝與場景：H 夕陽飯店套房、酒紅緞面垂墜領洋裝、斜躺 | 夕陽中的高樓飯店套房，酒紅緞面垂墜領細肩長洋裝，斜躺在深綠絲絨貴妃椅上。 | Penny 採用的 v2 替代方向：出勤前的銀座，黑色絲絨細肩帶長禮服，坐在金色燈光的吧台邊（不拿酒杯）。 |
| Rainie | Rainie：接受頂樓夜景血紅洋裝主方向。（以上各保留為其中一款，再另設完全不同的一款。） | 接受頂樓夜景血紅洋裝：H-rainie-hsu 沿用 v2 原文；另一款完全不同：V 雨後夜街、黑色緞面繞頸洋裝＋長皮風衣 | Penny 已接受的方向：頂樓夜景，血紅緞面馬甲高衩迷你洋裝，背靠玻璃欄杆直視鏡頭。 | 雨後的夜晚街道，黑色緞面繞頸迷你洋裝外搭黑色長皮風衣，站在濕亮的路面上直視鏡頭。 |
| Miu | Miu： - 服裝要呈現設定身材，尤其胸型與腰線。 - 不再以厚重寬鬆毛衣、圍裙遮住身材。 - 性感與甜美並存，不把她只拍成咖啡店工作照。 | 呈現胸型與腰線：H 貼身緞面細肩小可愛；V V 領合身針織洋裝＋細腰帶；不用厚重寬鬆毛衣、圍裙：程式檢查不含 apron、chunky、oversized；性感與甜美並存、不是咖啡店工作照：H 一人公寓晨光；V 運河步道 | 一人公寓的早晨，象牙白蕾絲緞面細肩小可愛與短褲，坐在床邊歪頭甜笑。 | 暮春的運河步道，奶油色 V 領合身針織洋裝繫細腰帶，靠著欄杆甜笑。 |
| Jia | Jia： - 服裝與場景重新設計。 - 不運動風、不舞蹈工作照。 - 不在攝影棚拍。 - 專業攝影質感可在實景完成，不需要棚景才成立。 | 服裝與場景重設：H 美術館黑色單肩洋裝；V 玻璃溫室白色短上衣＋薄荷綠緞面開衩裙；不運動、不舞蹈、不棚拍：程式檢查不含 studio、dance、sport、sneakers；兩款都是實景 | 現代美術館的白色展廳，黑色單肩貼身中長洋裝帶腰側鏤空，冷靜站在畫作之間。 | 明亮的玻璃溫室，白色無袖立領短上衣配薄荷綠緞面開衩中長裙，站在大葉植物之間。 |
| Yerin | Yerin： - 可穿高爾夫迷你裙裝。 - 性感、可愛、漂亮是拍攝重點。 - 不打球、不收桿、不拿球桿展示球技。 - 如高爾夫形象寫真，不把她改成啦啦隊職業。 | 高爾夫迷你裙裝：H 淺藍百褶高爾夫迷你裙＋白色針織 polo＋球帽；性感、可愛、漂亮：H 坐在球車上的可愛笑容；V 日落海灘的貼身白洋裝；不打球、不收桿、不拿球桿：程式檢查不含 club、driver、swing；不改成啦啦隊：不含 cheer、pom | 春天早晨的球場，白色無袖針織 polo 配淺藍百褶高爾夫迷你裙，坐在白色球車上的可愛笑容。 | 日落的白沙海灘，白色圓領貼身針織背心洋裝，赤腳站在淺浪邊的燦笑。 |

## 5. 橫式款 12 套總覽

| 月份（推薦） | ID | 主題 | 環境 | 服裝 | 色彩 | 姿態 | 表情 | 性感程度 | 攝影方法 | 景別｜身體方向｜臉與視線｜拍攝角度 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 月 | H-yuna-kim | 明亮通透的感性咖啡館，奶油黃短版開襟配淺藍緞面中長裙，坐在窗邊的清透美感。 | 明亮咖啡館（室內） | 上身：奶油黃貼身短版針織開襟（當上衣扣起，柔和 V 領）；下身：淺藍緞面斜裁中長裙（只入鏡腰頭）；鞋：白色尖頭平底鞋（不入鏡）；配件：耳上紅色櫻桃髮夾 | 奶油黃・淺藍・奶油白 | 坐在窗邊的咖啡椅上。一手前臂搭在窗台上，一手輕放在鎖骨旁。 | 平靜柔和的微笑 | 低 | 明亮漫射窗光、略偏亮的通透曝光 | 腰上｜約45度斜側（朝畫面左）｜三分之二側臉・看鏡頭｜坐姿時的肩膀高度・平視 |
| 2 月 | H-rin-ayase | 夕陽中的高樓飯店套房，酒紅緞面垂墜領細肩長洋裝，斜躺在深綠絲絨貴妃椅上。 | 飯店套房（室內夕陽） | 洋裝：深酒紅真絲緞面垂墜領細肩中長洋裝；鞋：赤腳；配件：細金鍊項鍊、金色小耳針 | 酒紅・深綠・柔金 | 斜躺在貴妃椅上，用一邊手肘撐著，雙腿併攏伸直。一手撐在手肘下，一手放在臀側。 | 平靜、心照不宣的半笑 | 高 | 夕陽窗光＋柔光補光 | 斜躺全身｜側面斜躺（朝畫面右）｜三分之二側臉・看鏡頭｜略高於她斜躺時頭部的高度・輕俯 |
| 3 月 | H-miu-shiraishi | 一人公寓的早晨，象牙白蕾絲緞面細肩小可愛與短褲，坐在床邊歪頭甜笑。 | 一人公寓（室內早晨） | 上身：象牙白緞面細肩小可愛（細蕾絲滾邊）；下身：同色緞面短褲；鞋：赤腳；配件：細金耳針、細金手鍊 | 象牙白・奶油・暖木 | 坐在床邊，雙膝併攏。雙手撐在身旁的床上。 | 歪頭、柔和的甜笑 | 高 | 紗簾晨光＋反光 | 坐姿全身｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 |
| 4 月 | H-tammy-chou | 高級精品店裡，熱粉色貼身針織洋裝配白色露跟高跟鞋，站在展示櫃旁的明亮笑容。 | 精品店（室內） | 洋裝：熱粉色方領羅紋針織貼身迷你洋裝（保留 Penny 同意的方向）；鞋：白色尖頭露跟高跟鞋；配件：手臂掛小型白色硬挺素面手提包、金色圈耳環 | 熱粉・奶油・大理石白・柔金 | 站在玻璃展示櫃旁。一手放在展示櫃上，一手插腰，小白包掛在手臂上。 | 明亮的笑容 | 中 | 柔光主光＋展示櫃投射燈 | 全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜膝蓋高度・輕仰 |
| 5 月 | H-yerin-han | 春天早晨的球場，白色無袖針織 polo 配淺藍百褶高爾夫迷你裙，坐在白色球車上的可愛笑容。 | 高爾夫球場（戶外） | 上身：白色無袖貼身針織高爾夫 polo；下身：淺天空藍百褶高爾夫迷你裙；鞋：白色高爾夫鞋；配件：素面白色球帽、小金色耳針 | 亮綠・天空藍・白 | 側坐在球車前座，雙腿伸出車外、在腳踝交叉。一手搭在椅背上，一手放在膝上。 | 明亮可愛的笑 | 中 | 晴朗晨光＋反光板 | 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 |
| 6 月 | H-coco-wu | 初夏傍晚的薰衣草花田，白色細肩亞麻洋裝，拿著草帽大笑。 | 花田（戶外） | 洋裝：白色亞麻細肩洋裝，抓皺貼身上身、柔和 V 領、收腰、微蓬迷你裙；鞋：白色平底涼鞋（不入鏡）；配件：白色雛菊髮夾、腳踝細金鍊（不入鏡）、草帽（拿在手上） | 薰衣草紫・白・暖金 | 站在花壟之間。一手把草帽拿在身側，一手把頭髮塞到耳後。 | 瞇眼大笑、深酒窩 | 中 | 傍晚逆光＋反光板 | 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視 |
| 7 月 | H-mia-huang | 夏日黃昏的海邊遊樂碼頭，粉色緞面馬甲上衣配白色迷你裙，拿著棉花糖俏皮眨眼。 | 海邊遊樂碼頭（戶外黃昏） | 上身：粉色緞面馬甲上衣（心形領）；下身：白色高腰 A 字迷你裙；鞋：白色厚底涼鞋（不入鏡）；配件：小珍珠耳環、細銀手鍊、一支粉色棉花糖 | 棉花糖粉・薰衣草紫・柔金 | 站在木棧道上。一手插腰，一手把棉花糖拿在肩高、離開臉。 | 俏皮眨眼、挑逗的半笑 | 中 | 黃昏天光＋柔光主光 | 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視 |
| 8 月 | H-iris-chen | 午後紅磚騎樓裡，穿米杏色針織套裝的 Iris 正面站定、對鏡頭笑。 | 城市老街（戶外） | 上身：米杏色貼身羅紋針織平口上衣；下身：同色高腰針織迷你裙（套裝）；鞋：米色厚底繫帶涼鞋；配件：細金鍊項鍊 | 紅磚・米杏・暖灰 | 站在一根磚柱旁。一手輕扶肩高的磚柱，一手插腰。 | 溫暖的笑容 | 中 | 側面午後光＋反光板 | 全身｜正面｜臉正面・看鏡頭｜臀部高度・平視 |
| 9 月 | H-jia-seo | 現代美術館的白色展廳，黑色單肩貼身中長洋裝帶腰側鏤空，冷靜站在畫作之間。 | 美術館（室內） | 洋裝：黑色單肩貼身中長洋裝，腰側一小塊鏤空；鞋：黑色細帶高跟鞋；配件：小銀色圈耳環 | 黑・白・灰・薄荷 | 站在展廳中央。靠鏡頭的手插在臀側、露出腰側鏤空，另一手自然垂放。 | 冷靜自信的半笑 | 中 | 天窗冷光＋柔光主光 | 全身｜側面（朝畫面左）｜三分之二側臉・看鏡頭｜臀部高度・平視 |
| 10 月 | H-luna-tanaka | 清晨的京都町家和室，象牙白蕾絲緞面細肩洋裝，席地而坐的安靜微笑。 | 和室（室內） | 洋裝：象牙白真絲細肩洋裝，細蕾絲滾邊、貼身上身、裙長大腿中段；鞋：赤腳（室內）；配件：細金鍊項鍊、耳上珍珠髮夾 | 柔白・暖木・淡粉 | 在榻榻米上側坐。兩手輕放在大腿上。 | 安靜的淺笑 | 中高 | 紙門柔光＋反光卡 | 席地坐姿全身｜約30度斜側（朝畫面左）｜三分之二側臉・看向窗光（畫面左）｜坐姿時的胸口高度・平視 |
| 11 月 | H-somi-oh | Penny 已接受的方向：暖橘復古小吃店棚景，針織短開襟＋高腰針織短裙，輕靠吧台大笑。 | 復古小吃店棚景（棚內） | 上身：奶油色合身羅紋針織短開襟（扣起）；下身：高腰鏽橘色針織迷你裙；鞋：棕色有跟皮革樂福鞋（不入鏡）；配件：紅色琺瑯小愛心耳環 | 暖橘・奶油・紅 | 站著，一側臀部輕靠磁磚吧台，重心在後腳、前腳輕交叉。一手放在吧台邊緣，一手把頭髮塞到耳後。 | 月牙眼大笑、露出酒窩 | 中 | 暖色柔光箱棚拍 | 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜腰部高度・平視 |
| 12 月 | H-rainie-hsu | Penny 已接受的方向：頂樓夜景，血紅緞面馬甲高衩迷你洋裝，背靠玻璃欄杆直視鏡頭。 | 頂樓露台（戶外夜晚） | 洋裝：血紅緞面馬甲迷你洋裝（大腿高衩）；鞋：黑色細帶高跟涼鞋（不入鏡）；配件：大型銀色垂墜耳環、細銀手環 | 血紅・黑・銀・深藍 | 背靠玻璃欄杆，一腳從高衩往前。雙手放在身後的欄杆上；不拿任何杯子。 | 自信又帶點壞的笑 | 高 | 夜景柔光箱主光＋城市散景 | 膝上｜正面｜臉正面・看鏡頭｜腰部高度・平視 |

## 6. 直式款 12 套總覽

| 月份（推薦） | ID | 主題 | 環境 | 服裝 | 色彩 | 姿態 | 表情 | 性感程度 | 攝影方法 | 景別｜身體方向｜臉與視線｜拍攝角度 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 月 | V-tammy-chou | 夜晚的大飯店大廳，白色西裝外套洋裝配黑色細跟鞋，雙手插腰的自信全身照。 | 飯店大廳（室內夜晚） | 洋裝：白色合身西裝外套式迷你洋裝（深 V 翻領、金色扣子、繫腰帶）；鞋：黑色尖頭細高跟鞋（不入鏡）；配件：金色垂墜耳環 | 白・金・暖大理石 | 站在大理石柱旁。雙手插腰。 | 自信的笑容 | 中 | 吊燈環境光＋柔光主光 | 大腿中段以上｜正面｜臉正面・看鏡頭｜腰部高度・輕仰 |
| 2 月 | V-jia-seo | 明亮的玻璃溫室，白色無袖立領短上衣配薄荷綠緞面開衩中長裙，站在大葉植物之間。 | 玻璃溫室（室內實景） | 上身：白色無袖立領貼身短上衣（露腰）；下身：高腰薄荷鼠尾草綠緞面中長裙（側開衩）；鞋：白色細帶涼鞋（不入鏡）；配件：細銀耳針 | 白・薄荷・深綠 | 站在植物之間的石板路上。一手輕觸身旁的大片龜背芋葉，一手插腰。 | 冷靜柔和的微笑 | 中 | 溫室漫射天光＋柔光 | 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜腰部高度・平視 |
| 3 月 | V-mia-huang | 春夜的櫻花河岸步道，淺紫貼身露肩針織洋裝，站在花枝下甜笑。 | 櫻花河岸（戶外夜晚） | 洋裝：淺紫細針織貼身露肩迷你洋裝；鞋：白色及膝長靴（不入鏡）；配件：一側小珍珠髮夾、細銀耳環 | 粉櫻・淺紫・夜藍 | 站在低垂的花枝下。一手輕觸肩旁的花枝，另一手自然垂下、不入鏡。 | 甜甜的微笑 | 中 | 夜景柔光主光＋燈籠 | 胸上｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜眼睛高度・輕俯 |
| 4 月 | V-miu-shiraishi | 暮春的運河步道，奶油色 V 領合身針織洋裝繫細腰帶，靠著欄杆甜笑。 | 運河步道（戶外） | 洋裝：奶油色 V 領細羅紋合身針織迷你洋裝（前排小扣、細棕色腰帶）；鞋：奶油色繫踝低跟鞋（不入鏡）；配件：細金耳針 | 奶油・新綠・淺棕 | 站在欄杆旁。一手扶著欄杆，一手輕輕拿著臉旁的一縷頭髮（不遮臉）。 | 甜甜的微笑 | 中 | 陰天柔光＋反光板 | 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視 |
| 5 月 | V-rainie-hsu | 雨後的夜晚街道，黑色緞面繞頸迷你洋裝外搭黑色長皮風衣，站在濕亮的路面上直視鏡頭。 | 雨後夜街（戶外夜晚） | 洋裝：黑色緞面繞頸迷你洋裝；外套：黑色長版皮革風衣（敞開）；鞋：黑色細跟尖頭短靴（不入鏡）；配件：大型銀色垂墜耳環 | 黑・銀・深藍・琥珀 | 站在濕亮的人行道上。一手拉著敞開的風衣衣襟在腰間，一手自然垂在大腿旁。 | 自信、帶點壞的笑 | 中高 | 夜景柔光主光＋濕路面倒影 | 膝上｜側面（朝畫面右）｜三分之二側臉・看鏡頭｜腰部高度・平視 |
| 6 月 | V-luna-tanaka | 紫陽花盛開的町家庭院，鼠尾草綠馬甲感洋裝，正面站在石板路上。 | 町家庭院（戶外） | 洋裝：淺鼠尾草綠棉質洋裝，心形領、有骨架的貼身上身、微蓬迷你裙；鞋：米色低跟繫帶涼鞋；配件：細金手鍊 | 鼠尾草綠・白・青苔綠 | 站在石板小徑上。雙手輕輕交握在身後。 | 溫柔的微笑 | 中 | 陰天柔光＋反光板 | 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰 |
| 7 月 | V-coco-wu | Penny 已接受的方向：週末飯店泳池，薄荷綠比基尼＋淺紫透膚罩衫，坐在池邊大笑。 | 飯店泳池（戶外） | 泳裝：薄荷綠羅紋三角比基尼上衣與同色側綁下著（完整遮蔽）；外搭：敞開的淺紫透膚短袖罩衫（落在肩後）；配件：白色雛菊髮夾、腳踝細金鍊（不入鏡） | 薄荷綠・淺紫・湖水綠 | 坐在池邊、兩條小腿泡在水裡，身體往後。雙手撐在身後地上。 | 歪頭、瞇眼大笑、酒窩 | 高 | 晴天高光＋反光板 | 坐姿到水面｜正面｜臉正面・看鏡頭｜坐姿時的胸口高度・平視 |
| 8 月 | V-yerin-han | 日落的白沙海灘，白色圓領貼身針織背心洋裝，赤腳站在淺浪邊的燦笑。 | 海灘夕陽（戶外） | 洋裝：白色圓領羅紋貼身背心迷你洋裝；鞋：赤腳（不入鏡）；配件：小金色圈耳環、腳踝細金鍊（不入鏡） | 暖金・蜜桃・白・淡藍 | 站在淺浪邊。一手輕放在鎖骨，一手自然垂放。 | 大方燦爛的笑 | 中 | 夕陽逆光＋反光板 | 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・輕仰 |
| 9 月 | V-iris-chen | 黃金時段的河濱草地，白色方領短上衣配牛仔迷你裙，正面站著甜笑（Penny 指定的穿搭）。 | 河濱草地（戶外） | 上身：白色貼身羅紋方領短袖短上衣（露腰）；下身：淺藍高腰牛仔迷你裙；鞋：白色低筒帆布鞋（不入鏡）；配件：小金色圈耳環 | 米白・淺牛仔藍・暖金 | 站在草地上。一手插腰，一手輕碰太陽穴旁的頭髮。 | 明亮溫暖的笑 | 中 | 黃金時段逆光＋反光板 | 大腿中段以上｜正面｜臉正面・看鏡頭｜胸口高度・平視 |
| 10 月 | V-rin-ayase | Penny 採用的 v2 替代方向：出勤前的銀座，黑色絲絨細肩帶長禮服，坐在金色燈光的吧台邊（不拿酒杯）。 | 會員制酒吧（室內夜晚） | 洋裝：黑色絲絨細肩帶及地長禮服（貼身上身）；鞋：黑色細帶高跟鞋（被及地長禮服蓋住，不入鏡）；配件：小金色垂墜耳環、細金手鍊 | 黑・金・深木 | 坐在高腳椅上，雙腿交疊。一手手肘靠在吧台上，一手放在膝上；手上不拿杯子。 | 平靜、端莊的微笑 | 中 | 金色吊燈＋柔光主光 | 坐姿全身｜約45度斜側（朝畫面左）｜三分之二側臉・看鏡頭｜坐姿時的腰部高度・平視 |
| 11 月 | V-yuna-kim | 深秋的銀杏大道，奶油色毛呢短外套套裝配黑色長靴，站在落葉上的韓劇感街拍寫真。 | 銀杏大道（戶外） | 上身：奶油色毛呢短外套（無領、扣起、合身）；下身：同色高腰毛呢迷你裙；鞋：黑色及膝皮長靴；配件：小珍珠耳環、小黑色肩背包 | 銀杏金黃・奶油・黑 | 站在落葉人行道上。一手拉著肩上的包包背帶，一手自然垂放。 | 頭微傾、柔和的微笑 | 低中 | 午後逆光＋反光板 | 全身｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜臀部高度・平視 |
| 12 月 | V-somi-oh | 下雪的溫泉小鎮夜晚，象牙白貼身針織洋裝外披紅色長大衣，在燈籠光裡大笑。 | 溫泉小鎮雪夜（戶外） | 洋裝：象牙白貼身羅紋針織迷你洋裝（高圓領）；外套：紅色羊毛長大衣（敞開）；鞋：白色及膝長靴；配件：小珍珠耳環 | 紅・象牙白・燈籠琥珀・雪夜藍 | 站在雪地上。雙手插在敞開的大衣口袋裡，把大衣往後撐開。 | 月牙眼大笑、露出酒窩 | 低中 | 夜景暖色主光＋燈籠 | 全身｜正面｜臉正面・看鏡頭｜臀部高度・平視 |

## 7. 兩本月份推薦（待 Penny 拍板，本輪不變）

| 月份 | 橫式款 | 理由 | 直式款 | 理由 |
|---|---|---|---|---|
| 1 月 | H-yuna-kim（Yuna） | 冬日的明亮咖啡館，用清透的奶油黃開場 | V-tammy-chou（Tammy） | 新年的大飯店大廳，白金色開場 |
| 2 月 | H-rin-ayase（Rin） | 夕陽套房的酒紅緞面，冬季的溫暖華麗 | V-jia-seo（Jia） | 冬末溫室的新綠 |
| 3 月 | H-miu-shiraishi（Miu） | 早春晨光的一人公寓 | V-mia-huang（Mia） | 春夜櫻花 |
| 4 月 | H-tammy-chou（Tammy） | 春天逛精品店的熱粉洋裝 | V-miu-shiraishi（Miu） | 暮春運河新綠 |
| 5 月 | H-yerin-han（Yerin） | 春日球場的清新綠 | V-rainie-hsu（Rainie） | 梅雨季的雨後夜街 |
| 6 月 | H-coco-wu（Coco） | 初夏薰衣草花田 | V-luna-tanaka（Luna） | 紫陽花季的庭院 |
| 7 月 | H-mia-huang（Mia） | 盛夏黃昏的遊樂碼頭 | V-coco-wu（Coco） | 盛夏泳池 |
| 8 月 | H-iris-chen（Iris） | 夏末午後的紅磚騎樓 | V-yerin-han（Yerin） | 夏日夕陽海灘 |
| 9 月 | H-jia-seo（Jia） | 初秋美術館的冷調 | V-iris-chen（Iris） | 夏末黃金時段草地 |
| 10 月 | H-luna-tanaka（Luna） | 秋日清晨的和室柔光 | V-rin-ayase（Rin） | 秋夜的金色酒吧 |
| 11 月 | H-somi-oh（Somi） | 晚秋的暖橘棚景 | V-yuna-kim（Yuna） | 深秋銀杏大道 |
| 12 月 | H-rainie-hsu（Rainie） | 年末頂樓夜景的派對感收尾 | V-somi-oh（Somi） | 冬天下雪的溫泉小鎮 |

- 每本 12 位各出現一次；同一月份兩本是不同的人。
- 既有碰撞配對（Miu–Jia、Miu–Somi、Jia–Somi、Yerin–Rin）與 R2 目視相似（Somi–Tammy、Iris–Rainie）：不放同一月份，也不放在同一本的相鄰月份。這不是同框規則（每頁只有一人），只是避免翻頁時直接並排比較。
- 先看季節（花田、紫陽花、櫻花、銀杏、雪景、海灘、泳池這些有季節的場景放在對的月份），再讓前後月份的色調交替；不為了季節改動已接受的企劃。
- 不把 12 人編成劇情。月份只是推薦，待 Penny 拍板。

## 8. 24 套企劃

### 8.1 H-iris-chen｜Iris｜橫式款（新企劃）

**一句話：** 午後紅磚騎樓裡，穿米杏色針織套裝的 Iris 正面站定、對鏡頭笑。

**攝影：** 全身｜正面｜臉正面・看鏡頭｜臀部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：平口針織上衣、高腰針織迷你裙、雙腿與米色厚底涼鞋；扶柱的手與插腰的手 | from a little above her head to just below her feet, both feet whole, showing the knit tube top, the high-waisted knit mini skirt, her legs and the platform sandals, one hand on the pillar and the other on her hip |
| 3. 身體朝向 | 正面：站姿，重心在左腳、右膝微彎放鬆；身體正對鏡頭，肩線放平放鬆，臀部隨重心微微偏移 | standing with her weight on her left leg and her right knee softly bent, her body square to the camera, shoulders level and relaxed, her hips shifted slightly with her weight |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她臀部高度，平視（參考：50mm 鏡頭、約 4.7 公尺；畫面中心與相機高度差換算俯仰約 -0.2 度） | camera at her hip height, level |
| 6. 畫面配置 | 人物在左側約三分之一處、緊靠一根磚柱；整排拱柱與木門店面從她身後往右側深處延伸成一點透視，右側是有層次的騎樓、不是空景；人物佔畫面高度約八成六 | she stands at the left third beside a brick pillar, the row of arches and closed wooden shopfronts receding behind her to the right in one-point perspective |
| 7. 攝影目的 | 完整展示米杏針織套裝的比例與腿長，以及她和老街騎樓的城市關係；正面笑容清楚 | the full proportion of the knit set and her legs, and her place in the old arcade street, with her smile clear |

**選擇理由：** Iris 依 Penny 要求身體正面、笑；橫式用全身＋臀部高度平視，直式用大腿中段以上＋胸口高度，靠景別與相機高度拉開差異。騎樓的透視線讓右側有內容，不是空景。

**本輪調整：** 景別由膝上改為全身，讓針織套裝與厚底涼鞋完整入鏡；姿勢、服裝、場景不變。

| 項目 | 內容 |
|---|---|
| 場景 | 台北老街的紅磚拱廊騎樓，午後；一排拱形磚柱、關著的木門店面，走廊空無一人。 |
| 服裝 | 上身：米杏色貼身羅紋針織平口上衣；下身：同色高腰針織迷你裙（套裝）；鞋：米色厚底繫帶涼鞋；配件：細金鍊項鍊 |
| 髮型 | 黑色柔順直髮自然垂放過肩。 |
| 妝感 | 乾淨的日常妝、自然唇色。 |
| 身材設定（數字） | 162 cm／87-58-90／D |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 平口針織貼合胸型、露出肩線；高腰迷你裙收出腰線，短裙長讓腿顯長。 |
| 主光 | 從騎樓開口側面斜射進來的午後陽光，在地面與身上留下柔和光帶 |
| 補光 | 畫面外的大白色反光板，臉均勻 |
| 姿態 | 站在一根磚柱旁。 |
| 手的位置 | 一手輕扶肩高的磚柱，一手插腰。 |
| 表情 | 溫暖的笑容 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，50mm，約 4.7 公尺，視野 3.38×1.9 公尺；人物約佔畫面高度 87%；相機約 0.87 公尺高、畫面中心約 0.86 公尺高，俯仰約 -0.2 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | 她是「台北的日常生活者」：老街的紅磚與午後光，加上隨手就好看的針織套裝，是她的城市感。 |
| 與同一人另一款的差異 | 直式款在河濱草地、白色短上衣＋牛仔迷你裙、黃金時段逆光；這款是城市老街、米杏針織套裝、側面午後光。 |
| 參考照片（用途） | iris-01：身分（認臉與甜笑；服裝不同）；iris-12：表情（開心的笑） |
| 推薦月份 | 8 月（夏末） |

| 風險 | 處理 |
|---|---|
| 騎樓招牌出現假字 | 寫明店面關著、只有木門，不寫招牌 |
| 側光讓臉一半暗 | 寫明反光板補臉 |
| 扶柱的手指變形 | 生成後放大檢查 |

prompt 草稿（16:9，尚未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a round sweet face with large bright double-eyelid eyes and full lips, black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, a full chest, a slim waist and rounded hips. She wears a fitted dusty-beige ribbed knit tube top and a matching high-waisted knit mini skirt, beige strappy platform sandals and a thin gold chain necklace. Setting: an old red-brick arcade walkway on a historic Taipei shopping street in the afternoon, a row of arched brick pillars, closed wooden shopfront doors, the walkway empty and clean. She stands beside one of the brick pillars, one hand resting lightly on the pillar at shoulder height and the other on her hip, smiling warmly. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing the knit tube top, the high-waisted knit mini skirt, her legs and the platform sandals, one hand on the pillar and the other on her hip. Body: standing with her weight on her left leg and her right knee softly bent, her body square to the camera, shoulders level and relaxed, her hips shifted slightly with her weight. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 4.7 metres, camera at her hip height, level, natural perspective without distortion; she fills about 87% of the frame height. Composition: she stands at the left third beside a brick pillar, the row of arches and closed wooden shopfronts receding behind her to the right in one-point perspective. Emphasis: the full proportion of the knit set and her legs, and her place in the old arcade street, with her smile clear. Lighting: warm afternoon sunlight enters from the open side of the arcade and lays soft shafts of light across the floor and her body; a large white reflector just out of frame fills her face evenly; warm brick, beige and soft grey tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.2 H-luna-tanaka｜Luna｜橫式款（新企劃）

**一句話：** 清晨的京都町家和室，象牙白蕾絲緞面細肩洋裝，席地而坐的安靜微笑。

**攝影：** 席地坐姿全身｜約30度斜側（朝畫面左）｜三分之二側臉・看向窗光（畫面左）｜坐姿時的胸口高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 席地坐姿全身 | a full-length shot of her seated on the floor |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在榻榻米上，收起的雙腿與雙腳完整。入鏡：完整席地坐姿；象牙白緞面洋裝與細肩帶、收在一側的雙腿與赤腳；兩手輕放在大腿上，不遮胸腰 | her whole seated figure from a little above her head down to the tatami, folded legs and feet whole, showing her whole seated figure, the ivory slip dress and thin straps, her folded legs and bare feet, both hands resting on her lap, nothing covering her chest or waist |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：席地側坐，雙腿收向畫面右側；上身身體朝畫面左轉約30度、自然挺直，臀部穩坐在榻榻米上 | sitting on the tatami with her legs folded toward camera-right, her upper body upright with her body turned about 30 degrees toward camera-left, her hips settled on the floor |
| 4. 臉部朝向與視線 | 三分之二側臉，看向畫面左側紙拉門透進的晨光（不看鏡頭） | her face in a three-quarter view, looking toward the morning light of the shoji screens on camera-left, away from the camera |
| 5. 相機高度與俯仰 | 相機在她坐姿時的胸口高度，平視（參考：50mm 鏡頭、約 2.3 公尺；畫面中心與相機高度差換算俯仰約 +1.2 度） | camera at her seated chest height, level |
| 6. 畫面配置 | 人物在右側約六成處；她轉向左側的紙拉門，左側留給視線、窗光與低矮木桌上的白花，背景不搶主體 | she sits right of centre, turned toward the shoji screens, leaving space on the left for her gaze, the light and the low table with white flowers |
| 7. 攝影目的 | 斜側坐姿讓胸型與細腰的側面曲線更清楚，看向窗光的三分之二側臉呈現她「白日夢」般的安靜 | the oblique seated pose shows the curve of her full chest and slim waist, and the three-quarter face toward the window light carries her quiet, dreamy mood |

**選擇理由：** Luna 的人設是「住在美麗白日夢裡的人」：24 套裡唯一不看鏡頭的一張，三分之二側臉仍能認人；直式款看鏡頭。相機放在她坐姿胸口高度平視，不俯拍，避免嬌小的她顯得更小。

**本輪調整：** 視線由看鏡頭改為看向畫面左側的窗光（三分之二側臉）；身體改為約30度斜側。服裝與場景不變。

| 項目 | 內容 |
|---|---|
| 場景 | 京都風老町家的和室，早晨；一面紙拉門、低矮木桌上一小瓶白花，房間整齊。 |
| 服裝 | 洋裝：象牙白真絲細肩洋裝，細蕾絲滾邊、貼身上身、裙長大腿中段；鞋：赤腳（室內）；配件：細金鍊項鍊、耳上珍珠髮夾 |
| 髮型 | 黑色細直髮，中分下巴長度的鮑伯。 |
| 妝感 | 柔和自然妝、玫瑰色唇。 |
| 身材設定（數字） | 155 cm／88-56-87／E（童顏與曲線的反差） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身緞面上身與細肩帶呈現 E 罩杯的飽滿胸型與細腰；大腿中段的裙長露出腿部線條。 |
| 主光 | 紙拉門透進的柔和晨光（相機左側） |
| 補光 | 畫面外右側白色反光卡 |
| 姿態 | 在榻榻米上側坐。 |
| 手的位置 | 兩手輕放在大腿上。 |
| 表情 | 安靜的淺笑 |
| 視線 | 看向畫面左側紙拉門透進的晨光（不看鏡頭） |
| 焦段／距離／視野（參考） | 16:9，50mm，約 2.3 公尺，視野 1.66×0.93 公尺；人物約佔畫面高度 87%；相機約 0.37 公尺高、畫面中心約 0.42 公尺高，俯仰約 +1.2 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | 她是「住在美麗白日夢裡的人」：和室、紙門、柔光與復古細肩洋裝，安靜又帶一點性感。 |
| 與同一人另一款的差異 | 直式款在戶外紫陽花庭院、鼠尾草綠馬甲洋裝、站姿；這款在室內和室、象牙白緞面洋裝、席地坐姿。 |
| 參考照片（用途） | luna-22：場景（和室的環境；不作身材參考：既有照片的身材不符合設定（Penny））；luna-04：表情（窗邊安靜的表情；不作身材參考：既有照片的身材不符合設定（Penny）） |
| 推薦月份 | 10 月（秋） |

| 風險 | 處理 |
|---|---|
| 童顏＋細肩洋裝顯小 | 寫明 adult、金項鍊與成熟妝感；不用娃娃裝元素 |
| 緞面坐姿皺褶怪異 | 生成後檢查 |
| 紙門出現文字 | 只寫紙門與木桌 |

prompt 草稿（16:9，尚未執行）：

```text
A 20-year-old adult Japanese woman with her natural fair skin tone, large round dark-brown eyes and soft natural makeup with a rosy lip, black fine straight hair in a centre-parted, chin-length bob. Petite figure with a noticeably full chest and a slim waist, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup. She wears an ivory silk slip dress with fine lace trim, thin straps and a fitted bodice that follows her full chest and slim waist, the hem at mid-thigh, a thin gold chain necklace and a pearl hair pin above one ear; her feet are bare. Setting: a quiet tatami room in an old Kyoto-style townhouse in the morning, paper shoji screens along one wall, a low wooden table with a small vase of white flowers, the room tidy. She sits with both hands resting lightly on her lap and a small, quiet smile. Shot: a full-length shot of her seated on the floor, her whole seated figure from a little above her head down to the tatami, folded legs and feet whole, showing her whole seated figure, the ivory slip dress and thin straps, her folded legs and bare feet, both hands resting on her lap, nothing covering her chest or waist. Body: sitting on the tatami with her legs folded toward camera-right, her upper body upright with her body turned about 30 degrees toward camera-left, her hips settled on the floor. Face and gaze: her face in a three-quarter view, looking toward the morning light of the shoji screens on camera-left, away from the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 2.3 metres, camera at her seated chest height, level, natural perspective without distortion; she fills about 87% of the frame height. Composition: she sits right of centre, turned toward the shoji screens, leaving space on the left for her gaze, the light and the low table with white flowers. Emphasis: the oblique seated pose shows the curve of her full chest and slim waist, and the three-quarter face toward the window light carries her quiet, dreamy mood. Lighting: soft morning daylight diffused through the shoji screens from camera-left as a large gentle key, a white bounce card just out of frame on the right keeping her face clear; soft white, warm wood and pale blush tones with a gentle film-like softness. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.3 H-somi-oh｜Somi｜橫式款（Penny 已接受的 v2 主方向）

**一句話：** Penny 已接受的方向：暖橘復古小吃店棚景，針織短開襟＋高腰針織短裙，輕靠吧台大笑。

**攝影：** 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：短開襟包住的胸型、腰線、高腰針織迷你裙與交叉的雙腿到膝蓋下方；扶吧台的手與塞頭髮的手 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the cropped cardigan over her chest, her waistline, the high-waisted knit mini skirt and her crossed legs down to just below the knees, one hand on the counter and the other at her ear |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：站姿，左側臀部輕靠在畫面右側的吧台上，身體朝畫面左轉約30度；重心在後腳、前腳輕輕交叉，肩線放鬆 | standing with her hip leaning on the counter on camera-right, her body turned about 30 degrees toward camera-left, weight on her back leg with the front leg crossed, shoulders relaxed |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她腰部高度，平視（參考：70mm 鏡頭、約 4.5 公尺；畫面中心與相機高度差換算俯仰約 +0.5 度） | camera at her waist height, level |
| 6. 畫面配置 | 人物偏左；暖橘吧台與紅色高腳椅往右延伸，一小盤失焦的炸雞在右緣（已接受的構圖） | left of centre with the orange counter running to the right and a small plate of golden fried chicken resting soft and out of focus at the right edge |
| 7. 攝影目的 | 斜側倚靠讓腰臀曲線與交叉的腿更明顯，臉正對鏡頭保留月牙眼大笑 | the oblique lean shows her waist-to-hip curve and crossed legs while her face stays toward the camera for the crescent-eyed laugh |

**選擇理由：** 已接受方向：服裝、場景、姿勢與「人物偏左、吧台往右、炸雞在右緣」都照舊；只把倚靠吧台的身體角度寫明為約30度斜側。

**本輪調整：** 已接受方向，只做必要調整：膝上取景看不到鞋，棕色樂福鞋從 prompt 拿掉（中文標不入鏡）；姿勢句的「看鏡頭」移到視線欄。

| 項目 | 內容 |
|---|---|
| 場景 | 搭景的韓式復古小吃店：暖橘色磁磚吧台、一排紅色皮面高腳椅、一盞暖色吊燈；橫幅右緣有一小盤失焦的炸雞。 |
| 服裝 | 上身：奶油色合身羅紋針織短開襟（扣起）；下身：高腰鏽橘色針織迷你裙；鞋：棕色有跟皮革樂福鞋（不入鏡）；配件：紅色琺瑯小愛心耳環 |
| 髮型 | 明亮蜜橘棕的韓式狼尾層次剪。 |
| 妝感 | 淡妝、亮澤唇釉。 |
| 身材設定（數字） | 161 cm／91-58-90／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 合身短開襟包覆 F 罩杯胸型並露出腰線；高腰短裙與交叉的腿呈現腰臀比。 |
| 主光 | 前右方頭部高度的大型暖色柔光箱 |
| 補光 | 畫面外左側柔光；吊燈在頭髮上加暖光 |
| 姿態 | 站著，一側臀部輕靠磁磚吧台，重心在後腳、前腳輕交叉。 |
| 手的位置 | 一手放在吧台邊緣，一手把頭髮塞到耳後。 |
| 表情 | 月牙眼大笑、露出酒窩 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，70mm，約 4.5 公尺，視野 2.31×1.3 公尺；頭頂上方留白約 6%；相機約 1.03 公尺高、畫面中心約 1.07 公尺高，俯仰約 +0.5 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | Penny 接受的 v2 主方向；吧台與高腳椅橫向延伸，最適合橫式款。 |
| 與同一人另一款的差異 | 直式款在雪夜溫泉小鎮、象牙白針織洋裝＋紅色長大衣、戶外冬夜；這款是棚內暖橘、針織短開襟＋短裙。 |
| 參考照片（用途） | somi-02：表情（Penny 喜歡的笑容與暖色調）；somi-01：身分（認臉） |
| 推薦月份 | 11 月（秋） |

| 風險 | 處理 |
|---|---|
| 炸雞搶戲或出現包裝假字 | 只在橫幅右緣、失焦、放在盤子上 |
| 棚景雜物多 | 寫明整齊 |

prompt 草稿（16:9，尚未執行）：

```text
A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a fitted cream rib-knit cropped cardigan buttoned up, a high-waisted rust-orange knit mini skirt and small red enamel heart earrings. Setting: a studio-built retro Korean snack-bar set with a warm orange tiled counter, a row of red vinyl bar stools and a warm pendant lamp, everything tidy. She stands leaning one hip lightly against the tiled counter, weight on her back leg with the front leg crossed in front, one hand resting on the counter edge and the other tucking her hair behind her ear, laughing openly with her eyes curved into crescents and dimples showing. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the cropped cardigan over her chest, her waistline, the high-waisted knit mini skirt and her crossed legs down to just below the knees, one hand on the counter and the other at her ear. Body: standing with her hip leaning on the counter on camera-right, her body turned about 30 degrees toward camera-left, weight on her back leg with the front leg crossed, shoulders relaxed. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 70mm lens from about 4.5 metres, camera at her waist height, level, natural perspective without distortion. Composition: left of centre with the orange counter running to the right and a small plate of golden fried chicken resting soft and out of focus at the right edge. Emphasis: the oblique lean shows her waist-to-hip curve and crossed legs while her face stays toward the camera for the crescent-eyed laugh. Lighting: a large warm softbox key from the front right at head height and a soft fill from the left just out of frame light her face evenly; the pendant lamp adds a warm glow on her hair; warm orange and cream tones throughout. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.4 H-coco-wu｜Coco｜橫式款（新企劃）

**一句話：** 初夏傍晚的薰衣草花田，白色細肩亞麻洋裝，拿著草帽大笑。

**攝影：** 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：抓皺貼身上身與 V 領、收腰、微蓬迷你裙到膝蓋下方；拿在身側的草帽與塞頭髮的手 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the ruched bodice and soft V neckline, the cinched waist and the flared mini skirt down to just below her knees, the straw hat held at her side and the other hand at her ear |
| 3. 身體朝向 | 約30度斜側（朝畫面右）：站在花壟之間，重心在後腳、前膝放鬆；身體朝畫面右轉約30度，肩與臀同向 | standing between the lavender rows with her weight on her back leg and her front knee relaxed, her body turned about 30 degrees toward camera-right, shoulders and hips turned together |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她胸口高度，平視（參考：85mm 鏡頭、約 5.4 公尺；畫面中心與相機高度差換算俯仰約 -1.2 度） | camera at her chest height, level |
| 6. 畫面配置 | 人物置中；薰衣草花壟從畫面下緣往地平線收攏到她身後，形成對稱的引導線 | she is centred, the lavender rows converging from the bottom edge to the horizon behind her as symmetrical leading lines |
| 7. 攝影目的 | 置中構圖與花壟引導線把視線集中在她的大笑；膝上保留 V 領胸型、收腰與裙長 | the centred frame and converging rows lead the eye to her laugh, while the knee-up framing keeps the V neckline, cinched waist and skirt length |

**選擇理由：** 橫式改用置中＋對稱引導線，避免又是「人在一側、另一側空景」；身體約30度斜側讓收腰的線條更明顯，臉正對鏡頭大笑。直式款是池邊坐姿，景別完全不同。

**本輪調整：** 人物由偏左改為置中、身體改為約30度斜側；相機由腰部改為胸口高度；膝上看不到的白色平底涼鞋與腳鍊從 prompt 拿掉。

| 項目 | 內容 |
|---|---|
| 場景 | 初夏傍晚一大片薰衣草花田，紫色花壟延伸到遠方，地平線上幾棵柔綠樹，花田裡沒有其他人。 |
| 服裝 | 洋裝：白色亞麻細肩洋裝，抓皺貼身上身、柔和 V 領、收腰、微蓬迷你裙；鞋：白色平底涼鞋（不入鏡）；配件：白色雛菊髮夾、腳踝細金鍊（不入鏡）、草帽（拿在手上） |
| 髮型 | 深棕長波浪捲髮、蓬鬆空氣瀏海。 |
| 妝感 | 甜美淡妝、粉色唇。 |
| 身材設定（數字） | 158 cm／89-56-86／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 抓皺貼身上身與 V 領呈現 E 罩杯胸型，收腰線清楚；迷你裙長露出腿。 |
| 主光 | 她身後的低角度傍晚陽光，頭髮與肩膀暖色輪廓光 |
| 補光 | 畫面外前方大反光板與柔光 |
| 姿態 | 站在花壟之間。 |
| 手的位置 | 一手把草帽拿在身側，一手把頭髮塞到耳後。 |
| 表情 | 瞇眼大笑、深酒窩 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，85mm，約 5.4 公尺，視野 2.29×1.29 公尺；頭頂上方留白約 7%；相機約 1.15 公尺高、畫面中心約 1.03 公尺高，俯仰約 -1.2 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | 她的配色有淺紫丁香與奶油白；週末出遊的花田讓她的大笑與甜美成立，不需要校園元素。 |
| 與同一人另一款的差異 | 直式款是飯店泳池、薄荷綠比基尼、坐姿；這款是花田、白色亞麻洋裝、站姿。 |
| 參考照片（用途） | coco-08：身分（認臉與身形比例）；coco-15：表情（大笑） |
| 推薦月份 | 6 月（初夏） |

| 風險 | 處理 |
|---|---|
| 花田出現遊客或標示牌 | 寫明花田空無一人 |
| 逆光臉暗 | 寫明反光板補臉 |
| 甜美＋洋裝顯小 | 寫明 adult、成熟剪裁 |

prompt 草稿（16:9，尚未執行）：

```text
A 20-year-old adult Taiwanese woman with her natural fair skin tone, a doll-like round face with big sweet eyes and deep dimples when she smiles, dark-brown long wavy hair with soft wispy bangs. Petite curvy figure, 158 cm tall, bust 89 cm, waist 56 cm, hips 86 cm, E cup, full chest and slim waist. She wears a white linen sundress with thin straps, a fitted ruched bodice with a soft V neckline that shapes her full chest, a cinched waist and a flared mini skirt, and a white daisy hair clip. Setting: a wide lavender field in early summer in the late afternoon, long purple rows running into the distance, a few soft green trees on the horizon, the field empty. She holds a straw sun hat loosely at her side with one hand and tucks her hair behind her ear with the other, laughing with her eyes squeezed into crescents and deep dimples showing. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the ruched bodice and soft V neckline, the cinched waist and the flared mini skirt down to just below her knees, the straw hat held at her side and the other hand at her ear. Body: standing between the lavender rows with her weight on her back leg and her front knee relaxed, her body turned about 30 degrees toward camera-right, shoulders and hips turned together. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with an 85mm lens from about 5.4 metres, camera at her chest height, level, natural perspective without distortion. Composition: she is centred, the lavender rows converging from the bottom edge to the horizon behind her as symmetrical leading lines. Emphasis: the centred frame and converging rows lead the eye to her laugh, while the knee-up framing keeps the V neckline, cinched waist and skirt length. Lighting: the low late-afternoon sun behind her draws a warm rim along her hair and shoulders; a large white reflector and a soft fill just out of frame light her face evenly; soft lilac, white and warm gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.5 H-mia-huang｜Mia｜橫式款（新企劃）

**一句話：** 夏日黃昏的海邊遊樂碼頭，粉色緞面馬甲上衣配白色迷你裙，拿著棉花糖俏皮眨眼。

**攝影：** 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 大腿中段以上 | a mid-thigh-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在大腿中段，不切在膝蓋。入鏡：心形領馬甲上衣、細腰、整條白色 A 字迷你裙與大腿上段；插腰的手與拿在肩高的棉花糖 | from a little above her head down to mid-thigh, well above the knees, showing the sweetheart corset top, her slim waist and the whole white A-line mini skirt with her upper thighs, one hand on her hip and the cotton candy held at shoulder height |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：站在木棧道上，重心在後腳；身體朝畫面左轉約30度，肩與臀同向，插腰那側的臀部自然往外 | standing on the boardwalk with her weight on her back leg, her body turned about 30 degrees toward camera-left, shoulders and hips turned together, the hip on her hand-on-hip side pushed out slightly |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她胸口高度，平視（參考：85mm 鏡頭、約 4.5 公尺；畫面中心與相機高度差換算俯仰約 -0.1 度） | camera at her chest height, level |
| 6. 畫面配置 | 人物置中；亮燈的摩天輪光點在她右肩後方（畫面右），粉紫晚霞與海面橫在背景 | she is centred, the lit Ferris wheel glowing as bokeh behind her shoulder on camera-right and the pink and lavender sunset sea across the background |
| 7. 攝影目的 | 大腿中段以上把馬甲塑出的胸腰比例放大，正對鏡頭的俏皮眨眼是主角 | a closer frame that enlarges the chest-to-waist shape of the corset top, with her playful wink as the focal point |

**選擇理由：** Mia 的魅力在表情與 F 罩杯曲線：大腿中段以上讓臉與身形都夠大；斜側＋插腰做出腰臀曲線。橫式改置中，背景光點只作氛圍。

**本輪調整：** 景別由膝上改為大腿中段以上，人物由偏左改為置中；白色厚底涼鞋不入鏡，從 prompt 拿掉。

| 項目 | 內容 |
|---|---|
| 場景 | 夏天黃昏的海邊遊樂碼頭：遠處亮燈的摩天輪與串燈化成柔和光點、粉紫色晚霞映在海上，木棧道上沒有其他人。 |
| 服裝 | 上身：粉色緞面馬甲上衣（心形領）；下身：白色高腰 A 字迷你裙；鞋：白色厚底涼鞋（不入鏡）；配件：小珍珠耳環、細銀手鍊、一支粉色棉花糖 |
| 髮型 | 灰棕色長髮鬆散大波浪，左側臉旁粉紅 money piece 挑染。 |
| 妝感 | 柔和動漫感眼妝、上揚眼線、圓形腮紅、水光唇。 |
| 身材設定（數字） | 160 cm／91-57-88／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 心形領馬甲上衣塑出 F 罩杯胸型與細腰；高腰 A 字短裙讓腰臀比與腿長清楚。 |
| 主光 | 畫面外右前方的大型柔光，臉乾淨、膚色自然明亮 |
| 補光 | 黃昏天光與遠處遊樂設施的粉紫光點只當背景色 |
| 姿態 | 站在木棧道上。 |
| 手的位置 | 一手插腰，一手把棉花糖拿在肩高、離開臉。 |
| 表情 | 俏皮眨眼、挑逗的半笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，85mm，約 4.5 公尺，視野 1.91×1.07 公尺；頭頂上方留白約 7%；相機約 1.2 公尺高、畫面中心約 1.19 公尺高，俯仰約 -0.1 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | 她的配色是棉花糖粉與紫；把「被看、被反應」的俏皮放進夏夜遊樂碼頭，不需要任何直播或電競符號。 |
| 與同一人另一款的差異 | 直式款是春夜櫻花步道、淺紫露肩針織洋裝；這款是夏日黃昏碼頭、粉色緞面馬甲＋白裙。 |
| 參考照片（用途） | mia-08：表情（戶外大笑；畫面裡的白 T 不採用）；mia-12：身分（認臉與髮色挑染；不採用畫面裡的帽 T） |
| 推薦月份 | 7 月（盛夏） |

| 風險 | 處理 |
|---|---|
| 棉花糖遮臉 | 寫明拿在肩高、離開臉 |
| 遊樂設施招牌字 | 只寫摩天輪與串燈光點 |
| 出現電競元素 | 程式檢查 prompt 不含 gaming、headset、RGB、neon |

prompt 草稿（16:9，尚未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a soft round face with big expressive eyes, softly winged liner, rounded blush and glossy tinted lips, long ash-brown hair in loose waves with a pastel-pink money-piece highlight framing the left side of her face. Curvy figure, 160 cm tall, bust 91 cm, waist 57 cm, hips 88 cm, F cup, a full chest and a slim waist. She wears a pastel-pink satin corset top with a sweetheart neckline that shapes her full chest and slim waist, a white high-waisted A-line mini skirt, small pearl earrings and a thin silver bracelet. Setting: a seaside amusement pier at dusk in summer, a lit Ferris wheel and string lights far behind her softening into bokeh, a pink and lavender sunset sky over the sea, the wooden boardwalk empty. One hand rests on her hip and the other holds a small pink cotton candy at shoulder height, away from her face; she gives a playful wink with a teasing half-smile. Shot: a mid-thigh-up shot, from a little above her head down to mid-thigh, well above the knees, showing the sweetheart corset top, her slim waist and the whole white A-line mini skirt with her upper thighs, one hand on her hip and the cotton candy held at shoulder height. Body: standing on the boardwalk with her weight on her back leg, her body turned about 30 degrees toward camera-left, shoulders and hips turned together, the hip on her hand-on-hip side pushed out slightly. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with an 85mm lens from about 4.5 metres, camera at her chest height, level, natural perspective without distortion. Composition: she is centred, the lit Ferris wheel glowing as bokeh behind her shoulder on camera-right and the pink and lavender sunset sea across the background. Emphasis: a closer frame that enlarges the chest-to-waist shape of the corset top, with her playful wink as the focal point. Lighting: a large soft key light from front-right just out of frame lights her face cleanly with natural, bright skin tones; the dusk sky and the distant ride lights add pink and lavender colour behind her; cotton-candy pink, lavender and soft gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.6 H-yuna-kim｜Yuna｜橫式款（新企劃）

**一句話：** 明亮通透的感性咖啡館，奶油黃短版開襟配淺藍緞面中長裙，坐在窗邊的清透美感。

**攝影：** 腰上｜約45度斜側（朝畫面左）｜三分之二側臉・看鏡頭｜坐姿時的肩膀高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 腰上 | a waist-up portrait |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腰線下方、臀部上方。入鏡：奶油黃短版開襟與 V 領、細腰、緞面裙的腰頭；搭在窗台上的前臂與輕放在鎖骨旁的手 | from a little above her head down to just below her waist, above the hips, showing the butter-yellow cropped cardigan and V neckline, her narrow waist and the waistband of the satin skirt, one forearm on the windowsill and the other hand lightly at her collarbone |
| 3. 身體朝向 | 約45度斜側（朝畫面左）：坐在窗邊的咖啡椅上（窗在畫面左），身體朝畫面左轉約45度；背挺直、肩線放鬆，臀部坐穩在椅面上 | seated on a café chair by the window on camera-left, her body turned about 45 degrees toward camera-left, back straight and shoulders relaxed |
| 4. 臉部朝向與視線 | 三分之二側臉，看鏡頭 | her face in a three-quarter view, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她坐姿時的肩膀高度，平視（參考：85mm 鏡頭、約 3.2 公尺；畫面中心與相機高度差換算俯仰約 -0.4 度） | camera at her seated shoulder height, level |
| 6. 畫面配置 | 人物在右側約六成處、佔畫面大半；左側是發亮的大窗與白紗，窗光從左側照在臉上 | she sits right of centre and fills most of the frame, the bright window and sheer curtains glowing on the left |
| 7. 攝影目的 | 較近的腰上：放大韓系寫真的水光肌、眼妝與通透窗光；她的長腿交給直式款的全身照 | a closer waist-up portrait that brings forward her dewy glass skin, eye makeup and the airy window light, leaving her long legs to the full-length vertical shot |

**選擇理由：** Yuna 的韓系感來自妝髮、色調與光：橫式用 24 套中唯一的腰上近景，讓臉與通透窗光成為主角；168 公分的腿長由直式款全身負責。

**本輪調整：** 景別由坐姿全身改為腰上；姿勢改為「前臂搭窗台、手放鎖骨旁」，原本放在膝上的手會被裁掉；光線改寫為窗戶在畫面左側；白色平底鞋不入鏡。

| 項目 | 內容 |
|---|---|
| 場景 | 明亮的極簡咖啡館：大片窗戶與白紗、低矮的木窗台、淺木桌、奶油色牆面，窗台上的玻璃瓶插一朵白色鬱金香，店內沒有其他人。 |
| 服裝 | 上身：奶油黃貼身短版針織開襟（當上衣扣起，柔和 V 領）；下身：淺藍緞面斜裁中長裙（只入鏡腰頭）；鞋：白色尖頭平底鞋（不入鏡）；配件：耳上紅色櫻桃髮夾 |
| 髮型 | 深棕自然波浪、鎖骨長度、空氣感八字瀏海。 |
| 妝感 | 水光肌、眼妝為重點、珊瑚漸層唇。 |
| 身材設定（數字） | 168 cm／84-58-89／C（纖細長腿） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 短版開襟收在腰上、緞面裙貼著腰臀，呈現她纖細的腰與長腿比例（C 罩杯、偏纖細，不寫成豐滿）。 |
| 主光 | 畫面左側大窗的明亮漫射日光（柔和主光） |
| 補光 | 畫面外右側柔光；曝光略偏亮、通透 |
| 姿態 | 坐在窗邊的咖啡椅上。 |
| 手的位置 | 一手前臂搭在窗台上，一手輕放在鎖骨旁。 |
| 表情 | 平靜柔和的微笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，85mm，約 3.2 公尺，視野 1.36×0.76 公尺；頭頂上方留白約 7%；相機約 1.02 公尺高、畫面中心約 1.0 公尺高，俯仰約 -0.4 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | 韓系寫真的美感來自通透的光、水光肌、奶油與淺藍的柔和配色、乾淨的空間——不需要文字、國旗或地標。 |
| 與同一人另一款的差異 | 直式款是秋日銀杏大道、奶油色毛呢短外套套裝＋長靴、站姿；這款是室內咖啡館、奶油黃開襟＋淺藍緞面裙、坐姿。 |
| 參考照片（用途） | yuna-15：場景（咖啡店氛圍；捧杯遮嘴的姿勢不採用）；yuna-05：表情（窗邊柔和的表情） |
| 推薦月份 | 1 月（冬末初春） |

| 風險 | 處理 |
|---|---|
| 咖啡館出現招牌字或菜單 | 只寫窗、紗簾、木桌與花瓶 |
| 過曝吃掉臉 | 測光給臉、補光 |
| 變成普通咖啡店照 | 用色調、妝感與構圖撐起雜誌感 |

prompt 草稿（16:9，尚未執行）：

```text
A 21-year-old adult Korean woman with her natural fair skin tone, large bright double-eyelid eyes as the focus of her makeup, a dewy glass-skin finish and soft coral gradient lips, dark-brown natural wavy hair at collarbone length with airy curtain bangs. Slim, long-legged figure, 168 cm tall, bust 84 cm, waist 58 cm, hips 89 cm, C cup, a narrow waist and long legs. She wears a soft butter-yellow fitted cropped cardigan buttoned as a top with a gentle V neckline, the high waist of a pale-blue satin bias-cut skirt and a small red cherry hair clip above one ear. Setting: a bright minimalist café, a seat beside a large window with a low wooden sill and sheer white curtains, pale wood tables, cream walls and a glass vase with a single white tulip on the sill, the room empty and calm. She rests one forearm on the windowsill beside her and lightly touches her collarbone with the other hand, with a calm, soft smile. Shot: a waist-up portrait, from a little above her head down to just below her waist, above the hips, showing the butter-yellow cropped cardigan and V neckline, her narrow waist and the waistband of the satin skirt, one forearm on the windowsill and the other hand lightly at her collarbone. Body: seated on a café chair by the window on camera-left, her body turned about 45 degrees toward camera-left, back straight and shoulders relaxed. Face and gaze: her face in a three-quarter view, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with an 85mm lens from about 3.2 metres, camera at her seated shoulder height, level, natural perspective without distortion. Composition: she sits right of centre and fills most of the frame, the bright window and sheer curtains glowing on the left. Emphasis: a closer waist-up portrait that brings forward her dewy glass skin, eye makeup and the airy window light, leaving her long legs to the full-length vertical shot. Lighting: bright diffused daylight from the large window on camera-left as a soft key, a soft fill just out of frame on the right; an airy, slightly bright exposure with clean cream, butter-yellow and pale-blue tones, a soft fashion-lookbook mood. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.7 H-tammy-chou｜Tammy｜橫式款（新企劃）

**一句話：** 高級精品店裡，熱粉色貼身針織洋裝配白色露跟高跟鞋，站在展示櫃旁的明亮笑容。

**攝影：** 全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜膝蓋高度・輕仰

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到鞋底完整；熱粉色貼身針織洋裝的胸腰臀線、雙腿與白色尖頭露跟高跟鞋；扶展示櫃的手與插腰的手，小白包掛在手臂上 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to heels, the fitted hot-pink knit dress over her chest, waist and hips, her legs and the white slingback heels, one hand on the counter and the other on her hip with the small white bag on her arm |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：站在展示櫃旁，重心在後腳、前腳尖朝鏡頭輕點，雙腿一前一後；身體朝畫面左轉約30度，肩與臀同向 | standing beside a glass display counter with her weight on her back leg and her front foot pointed toward the camera, legs one in front of the other, her body turned about 30 degrees toward camera-left, shoulders and hips turned together |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她膝蓋高度，輕仰（參考：50mm 鏡頭、約 4.8 公尺；畫面中心與相機高度差換算俯仰約 +4.1 度） | camera at her knee height, tilted slightly upward |
| 6. 畫面配置 | 人物置中；身後兩側是對稱、柔光照亮的展示櫃，低矮絲絨長凳失焦在左緣；人物佔畫面高度約八成五，不被店景縮小 | she is centred between softly lit display shelves on both sides behind her, the low velvet bench out of focus at the left edge |
| 7. 攝影目的 | 保留 Penny 同意的合身洋裝＋高跟鞋：全身、斜側與輕仰讓腿與高跟鞋完整修長，精品店的高級感在身後 | the fitted dress and heels Penny kept, shown head to toe with an oblique stance and a slightly low camera that lengthens her legs, the boutique behind her |

**選擇理由：** Penny 說合身洋裝＋高跟鞋可保留，所以橫式款用全身讓高跟鞋入鏡；膝蓋高度輕仰拉長腿部比例。直式款改大腿中段以上，兩款景別不同。

**本輪調整：** 景別由膝上改為全身（高跟鞋入鏡），人物由偏左改為置中，相機改為膝蓋高度輕仰。

| 項目 | 內容 |
|---|---|
| 場景 | 高級時裝精品店內：淺色大理石地板、奶油色牆、柔光照亮的玻璃展示櫃（只有素面皮包、無任何標誌）、一張低矮絲絨長凳，店內沒有其他人。 |
| 服裝 | 洋裝：熱粉色方領羅紋針織貼身迷你洋裝（保留 Penny 同意的方向）；鞋：白色尖頭露跟高跟鞋；配件：手臂掛小型白色硬挺素面手提包、金色圈耳環 |
| 髮型 | 奶茶金棕大波浪長捲髮，臉側淺色 money piece 挑染。 |
| 妝感 | 閃粉眼影、果凍唇。 |
| 身材設定（數字） | 160 cm／90-57-89／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身針織洋裝完整勾出 E 罩杯胸型、細腰與臀線；高跟鞋拉長腿。 |
| 主光 | 畫面外左前方大型柔光 |
| 補光 | 背景展示櫃的暖色投射燈 |
| 姿態 | 站在玻璃展示櫃旁。 |
| 手的位置 | 一手放在展示櫃上，一手插腰，小白包掛在手臂上。 |
| 表情 | 明亮的笑容 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，50mm，約 4.8 公尺，視野 3.46×1.94 公尺；人物約佔畫面高度 86%；相機約 0.53 公尺高、畫面中心約 0.87 公尺高，俯仰約 +4.1 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | 她做服飾電商、自己當模特兒；精品店是和合身洋裝與高跟鞋相配的高級場景，不是白牆或階梯。 |
| 與同一人另一款的差異 | 直式款是飯店大廳夜晚、白色西裝外套洋裝＋黑色高跟鞋；這款是白天精品店、熱粉針織洋裝＋白色高跟鞋。 |
| 參考照片（用途） | tammy-02：服裝材質（貼身針織洋裝的質感）；tammy-08：身分（認臉與購物穿搭氣質） |
| 推薦月份 | 4 月（春） |

| 風險 | 處理 |
|---|---|
| 包包或櫃子出現品牌 logo | 寫明素面、無標誌 |
| 像在工作賣貨 | 寫成她在店裡被拍的時裝照，不寫店員動作 |

prompt 草稿（16:9，尚未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, round almond eyes with visible aegyo-sal, shimmer eyeshadow and jelly-glossy lips, long voluminous big-wave hair in milk-tea golden brown with light money-piece highlights at the front. Curvy figure, 160 cm tall, bust 90 cm, waist 57 cm, hips 89 cm, E cup, a full chest and a slim waist. She wears a fitted hot-pink square-neck rib-knit mini dress that follows her full chest, slim waist and hips, white pointed slingback heels, a small structured plain white handbag on her arm and gold hoop earrings. Setting: an upscale fashion boutique with pale marble floors, cream walls and softly lit glass display shelves holding plain leather handbags without any logos, a low velvet bench, the boutique empty. One hand rests on the counter and the other on her hip, the small white bag on her arm; she smiles brightly. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to heels, the fitted hot-pink knit dress over her chest, waist and hips, her legs and the white slingback heels, one hand on the counter and the other on her hip with the small white bag on her arm. Body: standing beside a glass display counter with her weight on her back leg and her front foot pointed toward the camera, legs one in front of the other, her body turned about 30 degrees toward camera-left, shoulders and hips turned together. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 4.8 metres, camera at her knee height, tilted slightly upward, natural perspective without distortion; she fills about 86% of the frame height. Composition: she is centred between softly lit display shelves on both sides behind her, the low velvet bench out of focus at the left edge. Emphasis: the fitted dress and heels Penny kept, shown head to toe with an oblique stance and a slightly low camera that lengthens her legs, the boutique behind her. Lighting: a large soft key light from front-left just out of frame lights her face evenly while warm display spotlights glow on the shelves behind her; hot pink against cream, marble white and soft gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.8 H-rin-ayase｜Rin｜橫式款（新企劃）

**一句話：** 夕陽中的高樓飯店套房，酒紅緞面垂墜領細肩長洋裝，斜躺在深綠絲絨貴妃椅上。

**攝影：** 斜躺全身｜側面斜躺（朝畫面右）｜三分之二側臉・看鏡頭｜略高於她斜躺時頭部的高度・輕俯

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 斜躺全身 | a full-length reclining shot |
| 2. 畫面上下界 | 左右包含頭到腳的完整身長；頭部上方留白，下緣在椅面下方。入鏡：垂墜領緞面洋裝貼著胸腰、併攏的長腿與赤腳；撐著的手肘與放在臀側的手 | her whole reclining length from her head to her feet, with space above her head and the frame bottom below the seat, showing the cowl-neck satin dress over her chest and waist, her long legs together and her bare feet, one elbow propping her up and the other hand on her hip |
| 3. 身體朝向 | 側面斜躺（朝畫面右）：斜躺在貴妃椅上，雙腿併攏沿椅面伸直；雙腿側面朝畫面右、上身轉向鏡頭約45度，用一邊手肘撐起上身，肩線放鬆 | reclining along the chaise with her legs together and extended, her legs in side view toward camera-right and her upper body turned about 45 degrees toward the camera, propped on one elbow with her shoulders relaxed |
| 4. 臉部朝向與視線 | 三分之二側臉，看鏡頭 | her face in a three-quarter view, looking into the camera |
| 5. 相機高度與俯仰 | 相機在略高於她斜躺時頭部的高度，輕俯（參考：50mm 鏡頭、約 2.6 公尺；畫面中心與相機高度差換算俯仰約 -7.1 度） | camera at a height slightly above her head as she reclines, tilted slightly downward |
| 6. 畫面配置 | 人物沿貴妃椅橫跨畫面中央，身體從左側的頭部延伸到右側的赤腳，成一條水平的 S 形曲線；落地窗與天際線在後方 | she lies across the centre of the frame along the chaise, her body running from her head on the left to her bare feet on the right in a long horizontal S-curve, the window and skyline behind her |
| 7. 攝影目的 | 斜躺的身體曲線與長腿成為畫面主線，略高的相機輕俯讓 S 形線條完整 | her reclining curves and long legs become the main line of the picture, the slightly raised camera keeping the S-curve whole |

**選擇理由：** 橫式最適合躺姿的水平線：上身轉向鏡頭約45度、雙腿側面，兼顧胸腰與腿長；相機略高於她的頭部、輕俯，不從椅面高度仰拍。

**本輪調整：** 把原本的「面向鏡頭斜躺」改寫成「雙腿側面、上身轉向鏡頭約45度」，並把相機由椅面高度改為略高於頭部輕俯。

| 項目 | 內容 |
|---|---|
| 場景 | 日落時的高級飯店套房：落地窗邊一張深綠絲絨貴妃椅，窗外遠方城市天際線籠罩在暖色暮靄，房間整齊。 |
| 服裝 | 洋裝：深酒紅真絲緞面垂墜領細肩中長洋裝；鞋：赤腳；配件：細金鍊項鍊、金色小耳針 |
| 髮型 | 深酒紅棕長髮，柔和大波浪撥到一側肩上。 |
| 妝感 | 乾淨底妝、精準眼線、豆沙紅唇。 |
| 身材設定（數字） | 166 cm／92-58-90／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 垂墜領緞面貼著 F 罩杯胸型與細腰流動；斜躺姿勢讓身體曲線與長腿成為畫面主線。 |
| 主光 | 相機右側落地窗進來的低角度夕陽 |
| 補光 | 畫面外左側柔光 |
| 姿態 | 斜躺在貴妃椅上，用一邊手肘撐著，雙腿併攏伸直。 |
| 手的位置 | 一手撐在手肘下，一手放在臀側。 |
| 表情 | 平靜、心照不宣的半笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，50mm，約 2.6 公尺，視野 1.87×1.05 公尺；人物約佔畫面寬度 87%；相機約 1.02 公尺高、畫面中心約 0.69 公尺高，俯仰約 -7.1 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | 她的配色是深綠、酒紅與金，旅遊／飯店是她的支柱之一；斜躺的緞面是成熟艷麗但收斂的性感。 |
| 與同一人另一款的差異 | 直式款是銀座酒吧、黑色絲絨長禮服、坐吧台（Penny 指定的替代方向）；這款是飯店套房、酒紅緞面、斜躺。 |
| 參考照片（用途） | rin-05：服裝材質（緞面開衩洋裝的質感）；rin-01：身分（盤髮與妝感） |
| 推薦月份 | 2 月（冬） |

| 風險 | 處理 |
|---|---|
| 斜躺肢體結構錯誤 | 寫明手肘撐地與雙腿併攏 |
| 緞面遮蔽 | 寫中長洋裝、細肩帶 |

prompt 草稿（16:9，尚未執行）：

```text
A 25-year-old adult Japanese woman with her natural fair, cool-toned skin, an oval face with long narrow eyes and a straight nose, a clean base with precise eyeliner and a muted rose-red lip, long deep wine-red brown hair styled in soft big waves over one shoulder. Curvy figure, 166 cm tall, bust 92 cm, waist 58 cm, hips 90 cm, F cup, a full chest, a slim waist and long legs. She wears a deep wine-red silk satin cowl-neck slip midi dress with thin straps that drapes over her full chest and slim waist, a thin gold chain necklace and small gold stud earrings; her feet are bare. Setting: a luxury hotel suite at sunset, a deep green velvet chaise longue beside a floor-to-ceiling window, the city skyline far below in warm evening haze, the room tidy. She is propped on one elbow with her other hand resting on her hip and her legs extended together, with a calm, knowing half-smile. Shot: a full-length reclining shot, her whole reclining length from her head to her feet, with space above her head and the frame bottom below the seat, showing the cowl-neck satin dress over her chest and waist, her long legs together and her bare feet, one elbow propping her up and the other hand on her hip. Body: reclining along the chaise with her legs together and extended, her legs in side view toward camera-right and her upper body turned about 45 degrees toward the camera, propped on one elbow with her shoulders relaxed. Face and gaze: her face in a three-quarter view, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 2.6 metres, camera at a height slightly above her head as she reclines, tilted slightly downward, natural perspective without distortion; she fills about 87% of the frame width. Composition: she lies across the centre of the frame along the chaise, her body running from her head on the left to her bare feet on the right in a long horizontal S-curve, the window and skyline behind her. Emphasis: her reclining curves and long legs become the main line of the picture, the slightly raised camera keeping the S-curve whole. Lighting: warm low sunset light through the window from camera-right as the key, a soft fill just out of frame on the left keeping her face clear; wine red, deep green and soft gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.9 H-rainie-hsu｜Rainie｜橫式款（Penny 已接受的 v2 主方向）

**一句話：** Penny 已接受的方向：頂樓夜景，血紅緞面馬甲高衩迷你洋裝，背靠玻璃欄杆直視鏡頭。

**攝影：** 膝上｜正面｜臉正面・看鏡頭｜腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：馬甲塑出的胸型與細腰、高衩露出的大腿到膝蓋下方；放在身後欄杆上的雙手 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the corset bodice over her chest and slim waist and her leg through the thigh-high slit down to just below the knee, both hands on the rail behind her |
| 3. 身體朝向 | 正面：背靠玻璃欄杆站著，重心在後腳、一腿從高衩往前；身體正對鏡頭，肩膀輕靠玻璃 | leaning back against the glass balustrade with her weight on her back leg and one leg forward through the slit, her body square to the camera, her shoulders resting lightly on the glass |
| 4. 臉部朝向與視線 | 臉正面，直視鏡頭 | her face toward the camera, looking straight into the camera |
| 5. 相機高度與俯仰 | 相機在她腰部高度，平視（參考：85mm 鏡頭、約 5.7 公尺；畫面中心與相機高度差換算俯仰約 +0.5 度） | camera at her waist height, level |
| 6. 畫面配置 | 人物偏右；左側是城市燈海散景（已接受的構圖） | right of centre with the glowing city bokeh on the left |
| 7. 攝影目的 | 正面直視呈現她的氣場，膝上保留馬甲胸腰線與高衩腿線 | her direct gaze carries her presence while the knee-up frame keeps the corset lines and the slit leg |

**選擇理由：** 已接受方向：姿勢、取景、焦段與「人物偏右、左側燈海」都照舊；24 套中只剩這一張是正面膝上站姿，因為背靠欄杆的姿勢本來就正對鏡頭。

**本輪調整：** 已接受方向，只做必要調整：膝上取景看不到鞋，黑色細帶高跟涼鞋從 prompt 拿掉（中文標不入鏡）；姿勢句的「直視鏡頭」移到視線欄。

| 項目 | 內容 |
|---|---|
| 場景 | 高樓頂層露台的夜晚：玻璃欄杆、腳下城市燈光化成柔和散景、平滑深色石材地面，露台上沒有其他東西。 |
| 服裝 | 洋裝：血紅緞面馬甲迷你洋裝（大腿高衩）；鞋：黑色細帶高跟涼鞋（不入鏡）；配件：大型銀色垂墜耳環、細銀手環 |
| 髮型 | 長直黑髮，光滑有光澤，深側分。 |
| 妝感 | 柔和魅惑妝、貼近睫毛的淡棕眼線。 |
| 身材設定（數字） | 165 cm／94-59-92／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 馬甲塑出 F 罩杯胸型與細腰；高衩露出的腿呈現臀腿比例。 |
| 主光 | 左前方頭部高度的大型明亮柔光箱 |
| 補光 | 畫面外右側柔光；背後深藍夜空與暖金城市散景 |
| 姿態 | 背靠玻璃欄杆，一腳從高衩往前。 |
| 手的位置 | 雙手放在身後的欄杆上；不拿任何杯子。 |
| 表情 | 自信又帶點壞的笑 |
| 視線 | 直視鏡頭 |
| 焦段／距離／視野（參考） | 16:9，85mm，約 5.7 公尺，視野 2.41×1.36 公尺；頭頂上方留白約 8%；相機約 1.12 公尺高、畫面中心約 1.17 公尺高，俯仰約 +0.5 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | Penny 接受的 v2 主方向；城市燈海是橫向展開的景，最適合橫式款。 |
| 與同一人另一款的差異 | 直式款是雨後夜街、黑色緞面繞頸洋裝＋黑色長皮風衣；這款是頂樓城市燈海、血紅馬甲洋裝。 |
| 參考照片（用途） | rainie-06：場景（飯店窗邊的城市景）；rainie-10：服裝材質（緞面長洋裝的光澤） |
| 推薦月份 | 12 月（年末） |

| 風險 | 處理 |
|---|---|
| 出現酒杯或酒瓶 | 手放在欄杆上，場景只寫欄杆與地面 |
| 高衩遮蔽 | 生成後逐張檢查 |
| 玻璃反射出另一個人 | 寫明玻璃只反射城市燈光 |

prompt 草稿（16:9，尚未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, high cheekbones and a sculpted jaw, soft-glam makeup with a soft brown liner close to the lash line, long straight jet-black hair worn sleek and glossy with a deep side part. Curvy figure, 165 cm tall, bust 94 cm, waist 59 cm, hips 92 cm, F cup, full chest and slim waist. She wears a blood-red satin corset mini dress with a thigh-high slit, large silver statement drop earrings and a slim silver cuff. Setting: a high-rise penthouse terrace at night, a glass balustrade with the city lights far below spread into soft bokeh, a smooth dark stone floor, nothing else on the terrace, the glass reflecting only city lights. She leans back against the glass balustrade with both hands resting on the rail behind her and one leg forward through the slit, with a confident, slightly mischievous smirk. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the corset bodice over her chest and slim waist and her leg through the thigh-high slit down to just below the knee, both hands on the rail behind her. Body: leaning back against the glass balustrade with her weight on her back leg and one leg forward through the slit, her body square to the camera, her shoulders resting lightly on the glass. Face and gaze: her face toward the camera, looking straight into the camera. Camera: horizontal 16:9 frame, full-frame camera with an 85mm lens from about 5.7 metres, camera at her waist height, level, natural perspective without distortion. Composition: right of centre with the glowing city bokeh on the left. Emphasis: her direct gaze carries her presence while the knee-up frame keeps the corset lines and the slit leg. Lighting: a large bright softbox key from front-left at head height lights her face and catches crisp red highlights on the satin; a soft fill from the right just out of frame; deep navy night sky and warm gold city bokeh behind her. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.10 H-miu-shiraishi｜Miu｜橫式款（新企劃）

**一句話：** 一人公寓的早晨，象牙白蕾絲緞面細肩小可愛與短褲，坐在床邊歪頭甜笑。

**攝影：** 坐姿全身｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 坐姿全身 | a full-length seated shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，坐姿的雙腿與雙腳完整。入鏡：完整坐姿；緞面小可愛的胸型與很細的腰、短褲、併攏的雙腿與赤腳；兩手撐在身旁床上，不遮胸腰 | her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the satin camisole over her full chest and very slim waist, the shorts, her legs together and bare feet, both hands on the bed beside her hips, nothing covering her chest or waist |
| 3. 身體朝向 | 約30度斜側（朝畫面右）：坐在床邊，雙膝併攏、往畫面左側斜放；上身身體朝畫面右轉約30度，背挺直、肩線放鬆，臀部坐在床沿 | seated on the edge of the bed with her knees together and angled toward camera-left, her upper body upright with her body turned about 30 degrees toward camera-right, shoulders relaxed |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她坐姿時的腰部高度，平視（參考：35mm 鏡頭、約 2.6 公尺；畫面中心與相機高度差換算俯仰約 -0.9 度） | camera at her seated waist height, level |
| 6. 畫面配置 | 人物置中坐在床沿；左側是透著晨光的白紗窗、右側是木製床邊架與小盆栽，左右平衡 | she sits centred on the edge of the bed, the sheer-curtained window glowing on the left and the wooden bedside shelf with a small plant on the right |
| 7. 攝影目的 | 斜側坐姿＋雙手撐在身側，把胸型與很細的腰線完整打開；平視高度不俯拍，避免把她拍得顯小 | the oblique seated pose with her hands on the bed opens up her chest and very slim waist, and a level camera keeps her looking like an adult |

**選擇理由：** Miu 的胸腰不能被遮：雙手撐在身側、膝蓋斜放成 Z 字，曲線最清楚；小公寓空間有限，用 35mm 約 2.6 公尺，人物在中央、不貼邊，避免廣角變形；平視不俯拍，降低童顏顯小的風險。

**本輪調整：** 人物由偏左改為置中；身體寫明為上身約30度斜側、膝蓋斜向另一側。

| 項目 | 內容 |
|---|---|
| 場景 | 早晨陽光灑進的東京小公寓：鋪奶油色亞麻床單的整齊床鋪、木製床邊架上一小盆植物、窗上白紗簾，房間整齊。 |
| 服裝 | 上身：象牙白緞面細肩小可愛（細蕾絲滾邊）；下身：同色緞面短褲；鞋：赤腳；配件：細金耳針、細金手鍊 |
| 髮型 | 淺亞麻米金，齊肩內彎鮑伯、空氣瀏海。 |
| 妝感 | 眼下橘調腮紅、水潤唇。 |
| 身材設定（數字） | 156 cm／87-55-86／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身緞面小可愛直接呈現 E 罩杯胸型與很細的腰；雙手撐在身側讓胸腰線打開，不被毛衣或圍裙遮住。 |
| 主光 | 相機左側白紗簾透進的溫暖晨光 |
| 補光 | 畫面外右側白色反光 |
| 姿態 | 坐在床邊，雙膝併攏。 |
| 手的位置 | 雙手撐在身旁的床上。 |
| 表情 | 歪頭、柔和的甜笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，35mm，約 2.6 公尺，視野 2.67×1.5 公尺；人物約佔畫面高度 87%；相機約 0.72 公尺高、畫面中心約 0.68 公尺高，俯仰約 -0.9 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | 她的支柱是「私下／一人公寓」；晨光、奶油色與緞面讓她的甜美和性感同時成立，不是咖啡店工作照。 |
| 與同一人另一款的差異 | 直式款是春天運河步道、奶油色 V 領針織洋裝＋細腰帶；這款是室內晨光、緞面小可愛＋短褲、坐床邊。 |
| 參考照片（用途） | miu-06：身分（米白背心＋短裙的身形比例）；miu-01：表情（坐姿的甜美表情；厚毛衣不採用） |
| 推薦月份 | 3 月（冬末初春） |

| 風險 | 處理 |
|---|---|
| 童顏顯小 | 寫明 adult、成熟的緞面與金飾；不用娃娃裝與制服元素 |
| 居家服尺度 | 細肩小可愛＋短褲，完整遮蔽 |
| 碰撞紀錄（Jia、Somi） | 暖白奶油色、安靜甜美、淺亞麻短髮；不改臉、不宣稱能消除 |

prompt 草稿（16:9，尚未執行）：

```text
A 22-year-old adult Japanese woman with her natural very fair skin tone, a round face with big soft downturned eyes, orange-toned blush under the eyes and glossy lips, light flaxen beige-blonde hair in a shoulder-length bob curled inward with airy see-through bangs. Petite curvy figure, 156 cm tall, bust 87 cm, waist 55 cm, hips 86 cm, E cup, a full chest and a very slim waist. She wears an ivory satin camisole with thin straps and fine lace trim that follows her full chest, matching ivory satin shorts, small gold stud earrings and a thin gold bracelet; her feet are bare. Setting: a small sunlit Tokyo apartment in the morning, a neatly made bed with cream linen, a wooden bedside shelf with a small potted plant, sheer white curtains at the window, the room tidy. Both hands rest on the bed beside her hips; she tilts her head with a soft, sweet smile. Shot: a full-length seated shot, her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the satin camisole over her full chest and very slim waist, the shorts, her legs together and bare feet, both hands on the bed beside her hips, nothing covering her chest or waist. Body: seated on the edge of the bed with her knees together and angled toward camera-left, her upper body upright with her body turned about 30 degrees toward camera-right, shoulders relaxed. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 35mm lens from about 2.6 metres, camera at her seated waist height, level, natural perspective without distortion; she fills about 87% of the frame height. Composition: she sits centred on the edge of the bed, the sheer-curtained window glowing on the left and the wooden bedside shelf with a small plant on the right. Emphasis: the oblique seated pose with her hands on the bed opens up her chest and very slim waist, and a level camera keeps her looking like an adult. Lighting: warm morning sunlight through the sheer curtains from camera-left as a soft key, a white bounce just out of frame on the right so her face is evenly lit; cream, ivory and warm wood tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.11 H-jia-seo｜Jia｜橫式款（新企劃）

**一句話：** 現代美術館的白色展廳，黑色單肩貼身中長洋裝帶腰側鏤空，冷靜站在畫作之間。

**攝影：** 全身｜側面（朝畫面左）｜三分之二側臉・看鏡頭｜臀部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到鞋底完整；單肩剪裁露出的直角肩、腰側鏤空、貼身中長洋裝的修長線條與黑色細帶高跟鞋；靠鏡頭的手插在臀側、手臂彎出空間露出腰側鏤空，另一手自然垂在另一側 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to heels, the bare straight shoulder of the one-shoulder cut, the waist cut-out, the long line of the fitted midi dress and the black strappy heels, the arm nearer the camera bent with her hand on her hip so the cut-out shows, the other arm relaxed at her far side |
| 3. 身體朝向 | 側面（朝畫面左）：站在展廳中央，身體側面朝畫面左；重心在後腳、前腳尖輕點地，直角肩與背脊拉成一直線 | standing in the middle of the gallery, her body side-on to the camera, facing camera-left, weight on her back leg and the toes of her front foot lightly touching the floor, her straight shoulders and back in one long line |
| 4. 臉部朝向與視線 | 三分之二側臉，看鏡頭 | her face in a three-quarter view, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她臀部高度，平視（參考：50mm 鏡頭、約 5.1 公尺；畫面中心與相機高度差換算俯仰約 -0.3 度） | camera at her hip height, level |
| 6. 畫面配置 | 人物置中；兩側白牆各一幅灰與薄荷色調的大型抽象畫對稱排列，她側身的直線剪影在兩幅畫之間；人物佔畫面高度約八成五 | she stands centred between two large grey-and-mint abstract paintings hung symmetrically on the white walls, her side-on silhouette a clean vertical line between them |
| 7. 攝影目的 | 側身全身把她的直角肩、細腰與 168 公分的修長線條變成畫面主角，像美術館裡的時裝作品 | the side-on full figure makes her straight shoulders, slim waist and long lines the subject, like a fashion piece in the gallery |

**選擇理由：** Jia 偏冷、俐落，側身最能表現直角肩與長腿；臉轉回鏡頭約55度成三分之二側臉，仍能認人，不是回眸。置中＋對稱畫作讓橫式不是「人在一側、另一側空景」。

**本輪調整：** 景別由膝上改為全身；身體由正面改為側面、臉改為三分之二側臉；人物由偏左改為置中＋兩幅畫對稱；手改為「靠鏡頭的手插臀側、露出腰側鏤空」。

| 項目 | 內容 |
|---|---|
| 場景 | 現代美術館展廳：挑高白牆、拋光水泥地、牆上大幅灰色與薄荷色調的抽象畫、天花板軌道燈，展廳空無一人。 |
| 服裝 | 洋裝：黑色單肩貼身中長洋裝，腰側一小塊鏤空；鞋：黑色細帶高跟鞋；配件：小銀色圈耳環 |
| 髮型 | 冷灰藍黑長髮，一側塞在耳後露出薄荷綠內層。 |
| 妝感 | 水光無妝感、淡棕眼線、漸層唇。 |
| 身材設定（數字） | 168 cm／85-58-90／C（直角肩、長腿） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 單肩剪裁露出直角肩；貼身中長洋裝與腰側鏤空呈現細腰與 168 cm 的修長線條（C 罩杯，寫成纖細，不寫成豐滿）。 |
| 主光 | 畫面外左前方柔光 |
| 補光 | 天窗的冷調日光＋畫作上的暖色軌道燈 |
| 姿態 | 站在展廳中央。 |
| 手的位置 | 靠鏡頭的手插在臀側、露出腰側鏤空，另一手自然垂放。 |
| 表情 | 冷靜自信的半笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，50mm，約 5.1 公尺，視野 3.67×2.07 公尺；人物約佔畫面高度 85%；相機約 0.95 公尺高、畫面中心約 0.93 公尺高，俯仰約 -0.3 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | 她冷調、俐落；美術館的白牆與抽象畫讓她的身體線條像時裝作品，實景完成、不需要攝影棚，也不跳舞。 |
| 與同一人另一款的差異 | 直式款是玻璃溫室、白色立領短上衣＋薄荷綠緞面開衩長裙；這款是美術館、黑色單肩洋裝。 |
| 參考照片（用途） | jia-08：身分（夜晚穿搭與認臉；回頭姿勢不採用）；jia-02：表情（冷靜的表情；棚拍背景不採用） |
| 推薦月份 | 9 月（秋） |

| 風險 | 處理 |
|---|---|
| 畫作出現文字或真實作品 | 寫抽象色塊，不寫藝術家 |
| 展廳出現其他人 | 寫明空無一人 |
| 碰撞紀錄（Miu、Somi） | 冷色、黑白、薄荷內層；不改臉、不宣稱能消除 |

prompt 草稿（16:9，尚未執行）：

```text
A 22-year-old adult Korean woman with her natural fair, cool-toned skin, a small face, straight shoulders and long narrow upturned eyes, dewy no-makeup makeup with a soft brown liner and gradient lips, long cool blue-black hair tucked behind one ear so its mint-green inner layer shows. Slim, long-legged figure with soft feminine curves, 168 cm tall, bust 85 cm, waist 58 cm, hips 90 cm, C cup, a slim waist and long legs. She wears a black one-shoulder fitted midi dress with a small cut-out at the waist, the bare shoulder and the cut-out on the side toward the camera, black strappy heels and small silver hoop earrings. Setting: a modern art gallery with high white walls, a polished concrete floor and large abstract paintings in soft grey and mint tones, track lights on the ceiling, the gallery empty. The arm nearer the camera is bent with her hand resting on her hip and the other arm is relaxed at her side; she has a cool, confident half-smile. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to heels, the bare straight shoulder of the one-shoulder cut, the waist cut-out, the long line of the fitted midi dress and the black strappy heels, the arm nearer the camera bent with her hand on her hip so the cut-out shows, the other arm relaxed at her far side. Body: standing in the middle of the gallery, her body side-on to the camera, facing camera-left, weight on her back leg and the toes of her front foot lightly touching the floor, her straight shoulders and back in one long line. Face and gaze: her face in a three-quarter view, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 5.1 metres, camera at her hip height, level, natural perspective without distortion; she fills about 85% of the frame height. Composition: she stands centred between two large grey-and-mint abstract paintings hung symmetrically on the white walls, her side-on silhouette a clean vertical line between them. Emphasis: the side-on full figure makes her straight shoulders, slim waist and long lines the subject, like a fashion piece in the gallery. Lighting: cool daylight from a skylight with warm track lights on the paintings; a soft key light from front-left just out of frame lights her face evenly; black, white, grey and mint tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.12 H-yerin-han｜Yerin｜橫式款（新企劃）

**一句話：** 春天早晨的球場，白色無袖針織 polo 配淺藍百褶高爾夫迷你裙，坐在白色球車上的可愛笑容。

**攝影：** 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 坐姿全身 | a full-length seated shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，坐姿的雙腿與雙腳完整。入鏡：完整坐姿；白色無袖 polo 的胸型與手臂線條、百褶迷你裙、交叉的長腿與白色高爾夫鞋；搭椅背的手與放在膝上的手 | her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the sleeveless polo over her full chest and her toned arms, the pleated mini skirt, her long crossed legs and white golf shoes, one hand on the seat back and the other on her knee |
| 3. 身體朝向 | 約45度斜側（朝畫面左）：側坐在球車前座、雙腿伸出車外並在腳踝交叉；身體朝畫面左轉約45度，上身挺直、肩線放鬆 | sitting sideways on the front seat of the golf cart with her legs out of the cart and crossed at the ankles, her body turned about 45 degrees toward camera-left, upper body upright and shoulders relaxed |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她坐姿時的腰部高度，平視（參考：50mm 鏡頭、約 4.3 公尺；畫面中心與相機高度差換算俯仰約 -0.7 度） | camera at her seated waist height, level |
| 6. 畫面配置 | 白色球車斜放在畫面中、車頭朝左；她坐在畫面中央偏右的車門開口，伸出的長腿沿對角線指向左下，後方是亮綠球道 | the white golf cart sits at an angle across the frame with its front toward the left; she sits just right of centre in the open side of the cart, her long legs reaching diagonally toward the lower left, the bright green fairway behind |
| 7. 攝影目的 | 球車的對角線把 170 公分的長腿帶進畫面；高爾夫裝扮一看就是她，重點是可愛笑容與腿長，不打球 | the diagonal of the cart carries her long legs into the frame; the golf outfit makes her recognisable while the focus is her bright smile and leg length |

**選擇理由：** 性感可愛的高爾夫形象：坐在球車上不需要任何揮桿或球具；斜放的球車與伸出的長腿形成對角線，比正面站更有畫面節奏。

**本輪調整：** 身體寫明為約45度斜側，球車改成斜放的對角線構圖；人物由偏左改為中央偏右。

| 項目 | 內容 |
|---|---|
| 場景 | 晴朗春日早晨的高爾夫球場：一台素面白色球車停在車道旁，旁邊是亮綠的球道，遠方柔和的樹林，球場上沒有其他人。 |
| 服裝 | 上身：白色無袖貼身針織高爾夫 polo；下身：淺天空藍百褶高爾夫迷你裙；鞋：白色高爾夫鞋；配件：素面白色球帽、小金色耳針 |
| 髮型 | 亞麻棕長髮、臉側金色挑染，低馬尾從球帽後方穿出。 |
| 妝感 | 防曬淡妝、亮色唇。 |
| 身材設定（數字） | 170 cm／90-60-93／E（健康曲線） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 無袖貼身 polo 呈現 E 罩杯胸型與手臂線條；百褶迷你裙與伸出車外的雙腿呈現 170 cm 的長腿比例。 |
| 主光 | 左前上方的晴朗晨光 |
| 補光 | 畫面外大反光板，柔化帽簷下臉上的陰影 |
| 姿態 | 側坐在球車前座，雙腿伸出車外、在腳踝交叉。 |
| 手的位置 | 一手搭在椅背上，一手放在膝上。 |
| 表情 | 明亮可愛的笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 16:9，50mm，約 4.3 公尺，視野 3.1×1.74 公尺；人物約佔畫面高度 87%；相機約 0.84 公尺高、畫面中心約 0.78 公尺高，俯仰約 -0.7 度 |
| 原生尺寸 | 16:9 原生尺寸未知：沒有 soul_2 16:9 的實際輸出紀錄（9:16 為 1152×2048，16:9 推測約 2048×1152，未驗證） |
| 版面適配 | 橫式款建議用「大照片」框（約 1.85:1）：16:9 只需上下共裁約 4%，人物完整。若橫式款最後改用半版直幅框，這張不適用，要另拍直幅，不能硬裁。 |
| 為何符合人設 | 高爾夫形象寫真：球場、球車與高爾夫裙裝讓人一看就知道是她，但不打球、不拿球桿，重點是可愛與漂亮。 |
| 與同一人另一款的差異 | 直式款是日落海灘、白色圓領針織背心洋裝、赤腳；這款是球場球車、polo＋百褶裙＋球帽。 |
| 參考照片（用途） | yerin-01：服裝材質（白帽＋白 polo 的高爾夫穿搭）；yerin-05：服裝材質（polo＋百褶球裙的比例；俯身動作不採用） |
| 推薦月份 | 5 月（春） |

| 風險 | 處理 |
|---|---|
| 球車或衣帽出現品牌 logo | 寫素面白色球車與素面帽 |
| 帽簷陰影遮臉 | 寫明反光板補光 |
| 碰撞紀錄（Rin） | 明亮戶外清新色 vs Rin 的夜晚深色；不改臉 |

prompt 草稿（16:9，尚未執行）：

```text
A 26-year-old adult Korean woman with her natural fair skin tone, bright defined features and a wide open smile, light sun-protective makeup and a bright lip, long flax-brown hair with golden face-framing highlights in a low ponytail pulled through the back of a plain white cap. Curvy athletic figure with soft feminine lines, 170 cm tall, bust 90 cm, waist 60 cm, hips 93 cm, E cup, long legs and a slim waist. She wears a white fitted sleeveless knit golf polo that follows her full chest and slim waist, a pale sky-blue pleated golf mini skirt, white golf shoes, a plain white cap and small gold stud earrings. Setting: a golf course on a clear spring morning, a plain white golf cart parked on the cart path beside a bright green fairway, soft trees in the distance, the course empty. One hand rests on the seat back and the other on her knee; she smiles brightly. Shot: a full-length seated shot, her whole seated figure from a little above her head to just below her feet, legs and feet whole, showing her whole seated figure, the sleeveless polo over her full chest and her toned arms, the pleated mini skirt, her long crossed legs and white golf shoes, one hand on the seat back and the other on her knee. Body: sitting sideways on the front seat of the golf cart with her legs out of the cart and crossed at the ankles, her body turned about 45 degrees toward camera-left, upper body upright and shoulders relaxed. Face and gaze: her face toward the camera, looking into the camera. Camera: horizontal 16:9 frame, full-frame camera with a 50mm lens from about 4.3 metres, camera at her seated waist height, level, natural perspective without distortion; she fills about 87% of the frame height. Composition: the white golf cart sits at an angle across the frame with its front toward the left; she sits just right of centre in the open side of the cart, her long legs reaching diagonally toward the lower left, the bright green fairway behind. Emphasis: the diagonal of the cart carries her long legs into the frame; the golf outfit makes her recognisable while the focus is her bright smile and leg length. Lighting: clear morning sun from high front-left, a large white reflector just out of frame softening the shadow of the cap on her face; bright green, sky blue and white tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.13 V-iris-chen｜Iris｜直式款（新企劃）

**一句話：** 黃金時段的河濱草地，白色方領短上衣配牛仔迷你裙，正面站著甜笑（Penny 指定的穿搭）。

**攝影：** 大腿中段以上｜正面｜臉正面・看鏡頭｜胸口高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 大腿中段以上 | a mid-thigh-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在大腿中段，不切在膝蓋。入鏡：白色方領短上衣、露出的腰、整條牛仔迷你裙與大腿上段；插腰的手與碰頭髮的手 | from a little above her head down to mid-thigh, well above the knees, showing the square-neck crop top, her bare waist, the whole denim mini skirt and her upper thighs, one hand on her hip and the other at her hair |
| 3. 身體朝向 | 正面：站姿，重心在一隻腳；身體正對鏡頭，肩線放平放鬆，臀部隨重心微微偏向一側 | standing with her weight on one leg, her body square to the camera, shoulders level and relaxed, her hips shifted slightly to one side |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她胸口高度，平視（參考：85mm 鏡頭、約 2.9 公尺；畫面中心與相機高度差換算俯仰約 -0.1 度） | camera at her chest height, level |
| 6. 畫面配置 | 人物置中；頭頂上方少量留白，兩側是柔焦的草地與樹林，夕陽輪廓光落在頭髮與肩線 | she is centred with a little space above her head and the soft lawn and trees on both sides |
| 7. 攝影目的 | 放大 Penny 指定的穿搭：短上衣的胸型、露腰與牛仔迷你裙，加上明亮的笑容 | Penny's chosen outfit up close, the crop top on her chest, her bare waist and the denim mini skirt, with her bright smile |

**選擇理由：** 直式是首張試拍候選：大腿中段以上讓穿搭與笑容最清楚，又保留腰臀比例；胸口高度平視不變形。

**本輪調整：** 景別由膝上改為大腿中段以上；白色帆布鞋不入鏡，從 prompt 拿掉。

| 項目 | 內容 |
|---|---|
| 場景 | 台北河濱公園的開闊草地，傍晚太陽低，遠處柔綠樹林與低矮公寓，草地與小徑空無一人。 |
| 服裝 | 上身：白色貼身羅紋方領短袖短上衣（露腰）；下身：淺藍高腰牛仔迷你裙；鞋：白色低筒帆布鞋（不入鏡）；配件：小金色圈耳環 |
| 髮型 | 黑色柔順直髮自然垂放過肩。 |
| 妝感 | 乾淨的日常妝、自然唇色。 |
| 身材設定（數字） | 162 cm／87-58-90／D |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身方領短上衣清楚呈現 D 罩杯胸型、露出細腰；高腰牛仔迷你裙強調腰臀比與腿長。 |
| 主光 | 她身後側方的低角度夕陽，頭髮與肩線一圈暖色輪廓光 |
| 補光 | 畫面外前方的大反光板加柔光，臉與身體均勻 |
| 姿態 | 站在草地上。 |
| 手的位置 | 一手插腰，一手輕碰太陽穴旁的頭髮。 |
| 表情 | 明亮溫暖的笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 2.9 公尺，視野 0.82×1.09 公尺；頭頂上方留白約 8%；相機約 1.19 公尺高、畫面中心約 1.18 公尺高，俯仰約 -0.1 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | Penny 的回饋：更顯身材的上衣＋牛仔迷你裙、身體面向鏡頭、專業姿態、有笑容；保留她喜歡的 iris-04 夕陽草地氛圍。 |
| 與同一人另一款的差異 | 橫式款在紅磚騎樓、米杏針織套裝、側光；這款在河濱草地、白上衣＋牛仔迷你裙、逆光。 |
| 參考照片（用途） | iris-04：場景（草地、夕陽光線氛圍（Penny 喜歡的照片）；不採用回頭姿勢）；iris-06：服裝材質（白短上衣＋牛仔短裙的穿搭方向） |
| 推薦月份 | 9 月（夏末初秋） |

| 風險 | 處理 |
|---|---|
| 逆光臉暗 | 寫明反光板與柔光補臉 |
| 膚色被夕陽拍偏 | 只寫一次她原本的白皙膚色 |
| 碰頭髮的手指融合 | 生成後放大檢查；不行改成兩手插腰 |

prompt 草稿（3:4，尚未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a round sweet face with large bright double-eyelid eyes and full lips, black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, a full chest, a slim waist and rounded hips. She wears a fitted white ribbed square-neck short-sleeve crop top that shows the shape of her chest and her bare waist, a high-waisted light-blue denim mini skirt and small gold hoop earrings. Setting: an open riverside lawn in a Taipei park in the late afternoon, soft green trees and low distant apartment blocks far behind her, the lawn and the path empty. One hand rests on her hip and the other lightly touches her hair at her temple; she smiles brightly and warmly. Shot: a mid-thigh-up shot, from a little above her head down to mid-thigh, well above the knees, showing the square-neck crop top, her bare waist, the whole denim mini skirt and her upper thighs, one hand on her hip and the other at her hair. Body: standing with her weight on one leg, her body square to the camera, shoulders level and relaxed, her hips shifted slightly to one side. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 2.9 metres, camera at her chest height, level, natural perspective without distortion. Composition: she is centred with a little space above her head and the soft lawn and trees on both sides. Emphasis: Penny's chosen outfit up close, the crop top on her chest, her bare waist and the denim mini skirt, with her bright smile. Lighting: the low sun behind her and to one side draws a warm rim along her hair and shoulders; a large white reflector and a soft fill light just out of frame in front of her light her face and body evenly; warm golden tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.14 V-luna-tanaka｜Luna｜直式款（新企劃）

**一句話：** 紫陽花盛開的町家庭院，鼠尾草綠馬甲感洋裝，正面站在石板路上。

**攝影：** 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到涼鞋完整；有骨架的心形領上身、微蓬迷你裙、雙腿與米色低跟涼鞋；雙手交握在身後，胸腰線完整露出 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to sandals, the boned sweetheart bodice, the flared mini skirt and her legs, with both hands clasped behind her back so her chest and waist stay clear |
| 3. 身體朝向 | 正面：站在石板小徑上，重心在一隻腳、另一膝微彎；身體正對鏡頭，雙手在身後讓肩膀自然往後打開 | standing on the stone path with her weight on one leg and the other knee softly bent, her body square to the camera, her shoulders drawn gently back by her hands behind her |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她膝蓋高度，輕仰（參考：85mm 鏡頭、約 4.9 公尺；畫面中心與相機高度差換算俯仰約 +4.2 度） | camera at her knee height, tilted slightly upward |
| 6. 畫面配置 | 人物略偏左（約四成處）；石板路從她腳邊往右後方彎進庭院、經過紫陽花，楓枝橫過上緣；人物佔畫面高度約八成五 | she stands slightly left of centre, the stone path curving away behind her to the right past the hydrangeas, maple branches across the top edge |
| 7. 攝影目的 | 較低的相機輕仰讓 155 公分的她腿更修長；全身呈現有骨架上身塑出的胸腰比例與整件洋裝 | a slightly low camera lengthens her petite legs, and the full figure shows how the boned bodice shapes her chest and waist and the whole dress |

**選擇理由：** 嬌小的 Luna 用膝蓋高度輕仰拍全身，比例更修長；雙手在身後讓胸腰線完全不被遮住。與橫式款的席地斜側、看窗光完全不同。

**本輪調整：** 景別維持全身；相機由肚臍高度改為膝蓋高度輕仰，人物由置中改為略偏左。

| 項目 | 內容 |
|---|---|
| 場景 | 京都風老町家的後院：青苔地、石板小徑、木籬笆旁一整排白色紫陽花，頭上有楓樹枝。 |
| 服裝 | 洋裝：淺鼠尾草綠棉質洋裝，心形領、有骨架的貼身上身、微蓬迷你裙；鞋：米色低跟繫帶涼鞋；配件：細金手鍊 |
| 髮型 | 黑色細直髮，中分下巴長度的鮑伯。 |
| 妝感 | 柔和自然妝、玫瑰色唇。 |
| 身材設定（數字） | 155 cm／88-56-87／E（童顏與曲線的反差） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 心形領與有骨架的上身塑出飽滿胸型與細腰；雙手放身後讓胸腰線完整露出。 |
| 主光 | 明亮陰天的大面積柔光 |
| 補光 | 畫面外白色反光板；光斑只落在背景 |
| 姿態 | 站在石板小徑上。 |
| 手的位置 | 雙手輕輕交握在身後。 |
| 表情 | 溫柔的微笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 4.9 公尺，視野 1.38×1.84 公尺；人物約佔畫面高度 86%；相機約 0.47 公尺高、畫面中心約 0.83 公尺高，俯仰約 +4.2 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | 保留 Penny 沒有否定的紫陽花庭院，換成真正顯身材的剪裁。 |
| 與同一人另一款的差異 | 橫式款是室內和室、象牙白緞面、席地坐；這款是戶外庭院、綠色馬甲洋裝、站姿全身。 |
| 參考照片（用途） | luna-10：表情（Penny 喜歡的表情與柔光；不作身材參考：既有照片的身材不符合設定（Penny））；luna-01：場景（京都巷弄氛圍；不作身材參考：既有照片的身材不符合設定（Penny）） |
| 推薦月份 | 6 月（初夏（梅雨季紫陽花）） |

| 風險 | 處理 |
|---|---|
| 童顏＋花園顯小 | 寫明 adult、成熟剪裁與首飾 |
| 光斑落在臉上 | 寫明光斑只在背景 |
| 地名生出錯的地標 | 只寫環境元素 |

prompt 草稿（3:4，尚未執行）：

```text
A 20-year-old adult Japanese woman with her natural fair skin tone, large round dark-brown eyes and soft natural makeup with a rosy lip, black fine straight hair in a centre-parted, chin-length bob. Petite figure with a noticeably full chest and a slim waist, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup. She wears a pale sage-green cotton sundress with a sweetheart neckline, a fitted boned bodice that shapes her full chest and narrow waist and a softly flared mini skirt, cream low block-heel strappy sandals and a thin gold bracelet. Setting: a quiet garden behind an old wooden Kyoto-style townhouse, moss ground, a stone path, white hydrangeas in bloom along a low wooden fence, maple branches overhead. Both hands are clasped lightly behind her back; she smiles gently. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to sandals, the boned sweetheart bodice, the flared mini skirt and her legs, with both hands clasped behind her back so her chest and waist stay clear. Body: standing on the stone path with her weight on one leg and the other knee softly bent, her body square to the camera, her shoulders drawn gently back by her hands behind her. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 4.9 metres, camera at her knee height, tilted slightly upward, natural perspective without distortion; she fills about 86% of the frame height. Composition: she stands slightly left of centre, the stone path curving away behind her to the right past the hydrangeas, maple branches across the top edge. Emphasis: a slightly low camera lengthens her petite legs, and the full figure shows how the boned bodice shapes her chest and waist and the whole dress. Lighting: bright overcast daylight as one large soft source, with a white reflector just out of frame so her face is clean and evenly lit; soft dappled light falls only on the hydrangeas and path behind her; fresh green, white and sage tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.15 V-somi-oh｜Somi｜直式款（新企劃）

**一句話：** 下雪的溫泉小鎮夜晚，象牙白貼身針織洋裝外披紅色長大衣，在燈籠光裡大笑。

**攝影：** 全身｜正面｜臉正面・看鏡頭｜臀部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到靴底完整；敞開的紅色長大衣、貼身白色針織洋裝的胸腰臀線條、白色及膝長靴；插在口袋的雙手把大衣撐開 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to boots, the open red coat, the fitted ivory knit dress over her chest, waist and hips, and the white knee-high boots, both hands in the coat pockets holding it open |
| 3. 身體朝向 | 正面：站在薄雪上，重心在後腳、前腳微微向前；身體正對鏡頭，肩線放鬆，敞開的大衣左右對稱 | standing on the thin snow with her weight on her back leg and her front foot slightly forward, her body square to the camera, shoulders relaxed, the open coat falling evenly on both sides |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她臀部高度，平視（參考：70mm 鏡頭、約 4.2 公尺；畫面中心與相機高度差換算俯仰約 -0.0 度） | camera at her hip height, level |
| 6. 畫面配置 | 人物略偏右（約六成處）；掛著燈籠的溫泉街與蒸氣往左後方延伸；人物佔畫面高度約八成五 | she stands slightly right of centre, the lantern-lit street and rising steam receding behind her on the left |
| 7. 攝影目的 | 全身展示長大衣、針織洋裝與長靴的冬季整體造型；正面讓撐開的大衣像框一樣框住洋裝的胸腰臀線 | the whole winter look of long coat, knit dress and boots, the open coat framing the curves of the dress like a frame |

**選擇理由：** 膝上會切掉紅色長大衣的下襬與白色長靴；改全身讓整套冬裝完整。雙手插口袋把大衣往兩側撐開，正面最能讓洋裝線條露出。

**本輪調整：** 景別由膝上改為全身，人物由置中改為略偏右。

| 項目 | 內容 |
|---|---|
| 場景 | 小型溫泉小鎮的街道，冬夜飄雪；低矮木造旅館掛著暖色紙燈籠、路旁石溝冒出薄薄的蒸氣，地上一層薄雪，街上沒有人。 |
| 服裝 | 洋裝：象牙白貼身羅紋針織迷你洋裝（高圓領）；外套：紅色羊毛長大衣（敞開）；鞋：白色及膝長靴；配件：小珍珠耳環 |
| 髮型 | 明亮蜜橘棕的韓式狼尾層次剪。 |
| 妝感 | 淡妝、亮澤唇釉、凍紅的臉頰。 |
| 身材設定（數字） | 161 cm／91-58-90／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身羅紋針織洋裝清楚勾出 F 罩杯胸型、細腰與臀線；雙手插在大衣口袋把大衣撐開，讓洋裝線條露出來。 |
| 主光 | 畫面外前左方的柔和暖色主光 |
| 補光 | 背後燈籠的暖光；雪地上的冷藍夜色 |
| 姿態 | 站在雪地上。 |
| 手的位置 | 雙手插在敞開的大衣口袋裡，把大衣往後撐開。 |
| 表情 | 月牙眼大笑、露出酒窩 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，70mm，約 4.2 公尺，視野 1.44×1.92 公尺；人物約佔畫面高度 85%；相機約 0.87 公尺高、畫面中心約 0.86 公尺高，俯仰約 -0.0 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | 她的配色有「蒸氣白」與紅；溫泉街的蒸氣與燈籠暖光延續她的溫暖感，但完全不靠食物。 |
| 與同一人另一款的差異 | 橫式款是棚內暖橘小吃店、針織短開襟＋短裙；這款是戶外雪夜、白色針織洋裝＋紅大衣＋長靴。 |
| 參考照片（用途） | somi-08：服裝材質（外套穿搭與身分）；somi-02：表情（月牙眼的笑） |
| 推薦月份 | 12 月（冬） |

| 風險 | 處理 |
|---|---|
| 雪夜臉暗或發灰 | 寫明柔和暖色主光 |
| 燈籠或招牌出現文字 | 只寫紙燈籠、不寫招牌 |
| 雪花蓋住臉 | 只寫空中少量雪花 |

prompt 草稿（3:4，尚未執行）：

```text
A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a fitted ivory ribbed knit mini dress with a high round neck that follows her full chest, slim waist and hips, a long red wool coat worn open, white knee-high boots and small pearl earrings. Setting: a quiet street in a small hot-spring town on a snowy winter evening, low wooden inns with warm paper lanterns, thin steam rising from a stone channel at the roadside, a light layer of snow on the ground, the street empty. Both hands are in the pockets of the open coat, holding it back so the fitted dress shows; she laughs with her eyes curved into crescents and dimples showing, a few snowflakes in the air. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to boots, the open red coat, the fitted ivory knit dress over her chest, waist and hips, and the white knee-high boots, both hands in the coat pockets holding it open. Body: standing on the thin snow with her weight on her back leg and her front foot slightly forward, her body square to the camera, shoulders relaxed, the open coat falling evenly on both sides. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with a 70mm lens from about 4.2 metres, camera at her hip height, level, natural perspective without distortion; she fills about 85% of the frame height. Composition: she stands slightly right of centre, the lantern-lit street and rising steam receding behind her on the left. Emphasis: the whole winter look of long coat, knit dress and boots, the open coat framing the curves of the dress like a frame. Lighting: a soft warm key light from front-left just out of frame lights her face evenly; the paper lanterns behind her glow warm amber against the cool blue evening light on the snow; red, ivory and warm amber tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.16 V-coco-wu｜Coco｜直式款（Penny 已接受的 v2 主方向）

**一句話：** Penny 已接受的方向：週末飯店泳池，薄荷綠比基尼＋淺紫透膚罩衫，坐在池邊大笑。

**攝影：** 坐姿到水面｜正面｜臉正面・看鏡頭｜坐姿時的胸口高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 坐姿到水面 | a seated shot down to the waterline |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在水面下一點，膝蓋與小腿上段入鏡。入鏡：比基尼上衣與下著、細腰、膝蓋與入水的小腿上段；撐在身後的雙手 | from a little above her head down to just below the waterline, her knees and the upper part of her lower legs showing, showing the bikini top and bottoms, her slim waist, her knees and the upper part of her lower legs in the water, with both hands braced behind her |
| 3. 身體朝向 | 正面：坐在池邊，兩條小腿泡在水裡；上身往後靠在撐地的雙手上，身體正對鏡頭，肩膀自然打開 | sitting on the pool edge with both lower legs in the water, leaning back on her hands, her body square to the camera, her shoulders open |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她坐姿時的胸口高度，平視（參考：70mm 鏡頭、約 2.7 公尺；畫面中心與相機高度差換算俯仰約 -0.8 度） | camera at her seated chest height, level |
| 6. 畫面配置 | 人物置中；池水橫在畫面下方，池畔石磚與收起的白色陽傘在後方（已接受的構圖） | she is centred, with the water across the bottom of the frame and the pool deck and folded umbrellas behind her |
| 7. 攝影目的 | 坐姿＋下方水面讓身體在直幅裡又大又完整，正面呈現比基尼的胸腰線條與大笑 | the seated pose and the water below keep her body large and complete in the vertical frame, showing the bikini, her chest and waist, and her laugh |

**選擇理由：** 已接受方向：姿勢、取景與焦段距離都照 v3；只把身體正面、臉正面、相機在坐姿胸口高度平視寫明。

**本輪調整：** 已接受方向，構圖沒有衝突，姿勢、取景、焦段距離都不改；只把原本隱含的角度寫成明確欄位，並把在水面下、畫面外的腳鍊從 prompt 拿掉（中文標不入鏡）。

| 項目 | 內容 |
|---|---|
| 場景 | 週末早上的度假飯店泳池：淺米色石材地磚、清澈的湖水綠池水、遠處收起的白色陽傘，池畔無人。 |
| 服裝 | 泳裝：薄荷綠羅紋三角比基尼上衣與同色側綁下著（完整遮蔽）；外搭：敞開的淺紫透膚短袖罩衫（落在肩後）；配件：白色雛菊髮夾、腳踝細金鍊（不入鏡） |
| 髮型 | 深棕長波浪捲髮、蓬鬆空氣瀏海，髮尾微濕。 |
| 妝感 | 甜美淡妝。 |
| 身材設定（數字） | 158 cm／89-56-86／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 比基尼呈現 E 罩杯胸型與細腰；往後撐的坐姿拉長身體線條。 |
| 主光 | 晚上午的陽光從左前上方 |
| 補光 | 畫面外大反光板；池水在腿上留下淡淡水光 |
| 姿態 | 坐在池邊、兩條小腿泡在水裡，身體往後。 |
| 手的位置 | 雙手撐在身後地上。 |
| 表情 | 歪頭、瞇眼大笑、酒窩 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，70mm，約 2.7 公尺，視野 0.93×1.23 公尺；人物約佔畫面高度 81%；相機約 0.36 公尺高、畫面中心約 0.32 公尺高，俯仰約 -0.8 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | Penny 接受的 v2 主方向；坐姿與下方水面在直幅裡讓身體更大、更清楚，所以建議放直式款。 |
| 與同一人另一款的差異 | 橫式款是花田、白色亞麻洋裝、站姿；這款是泳池、比基尼、坐姿。 |
| 參考照片（用途） | coco-21：表情（泳裝照的大笑；尺度同第二階段泳裝參考）；coco-20：身分（認臉與身形） |
| 推薦月份 | 7 月（盛夏） |

| 風險 | 處理 |
|---|---|
| 泳裝遮蔽與走光 | 寫明完整遮蔽；交印前需確認廠商接受範圍 |
| 水下腳掌與撐地手指變形 | 生成後檢查 |

prompt 草稿（3:4，尚未執行）：

```text
A 20-year-old adult Taiwanese woman with her natural fair skin tone, deep dimples when she smiles and dark-brown long wavy hair with soft wispy bangs, the ends slightly wet. Petite curvy figure, 158 cm tall, bust 89 cm, waist 56 cm, hips 86 cm, E cup, full chest and slim waist. She wears a mint-green ribbed triangle bikini top with matching side-tie bottoms that fully cover, an open sheer lilac short-sleeve cover-up shirt resting off her shoulders and a white daisy hair clip. Setting: a resort hotel pool on a weekend morning, pale cream stone tiles, clear turquoise water, white umbrellas folded in the distance, the pool deck empty. She sits on the pool edge with both lower legs in the water, leaning back on her hands, head tilted, laughing with her eyes squeezed into crescents and dimples showing. Shot: a seated shot down to the waterline, from a little above her head down to just below the waterline, her knees and the upper part of her lower legs showing, showing the bikini top and bottoms, her slim waist, her knees and the upper part of her lower legs in the water, with both hands braced behind her. Body: sitting on the pool edge with both lower legs in the water, leaning back on her hands, her body square to the camera, her shoulders open. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with a 70mm lens from about 2.7 metres, camera at her seated chest height, level, natural perspective without distortion; she fills about 81% of the frame height. Composition: she is centred, with the water across the bottom of the frame and the pool deck and folded umbrellas behind her. Emphasis: the seated pose and the water below keep her body large and complete in the vertical frame, showing the bikini, her chest and waist, and her laugh. Lighting: bright late-morning sun from high front-left; a large white reflector just out of frame fills the shadows on her face and body so her face is evenly lit; the turquoise water adds soft aqua reflections on her legs; clear, fresh summer colours. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.17 V-mia-huang｜Mia｜直式款（新企劃）

**一句話：** 春夜的櫻花河岸步道，淺紫貼身露肩針織洋裝，站在花枝下甜笑。

**攝影：** 胸上｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜眼睛高度・輕俯

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 胸上 | a chest-up portrait |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在胸線下方、手肘上方。入鏡：露肩針織領口、肩頸線、鎖骨與胸型；碰花枝的手在肩旁，另一手自然垂下、不入鏡（裁在上臂，不在手肘） | from a little above her head down to just below her bust, above the elbows, showing the off-shoulder knit neckline, her shoulders, collarbones and chest, one hand touching a blossom branch beside her shoulder and the other arm relaxed below the frame |
| 3. 身體朝向 | 約30度斜側（朝畫面右）：站在低垂的花枝下，身體朝畫面右轉約30度，肩線放鬆、露肩領口平整 | standing under a low blossom branch, her body turned about 30 degrees toward camera-right, shoulders relaxed so the off-shoulder neckline sits evenly |
| 4. 臉部朝向與視線 | 三分之二側臉，看鏡頭 | her face in a three-quarter view, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她眼睛高度，輕俯（參考：85mm 鏡頭、約 1.5 公尺；畫面中心與相機高度差換算俯仰約 -4.5 度） | camera at her eye level, tilted slightly downward |
| 6. 畫面配置 | 人物略偏左；上緣與右上角有櫻花枝框住畫面，燈籠化成柔和光點；臉在畫面上三分之一 | she is slightly left of centre, blossom branches framing the top and upper right, the lanterns softened into warm bokeh, her face in the upper third |
| 7. 攝影目的 | 全組最近的一張：放大她的柔和眼妝、甜笑與露肩領口，櫻花與燈籠只作氛圍 | the closest shot of the set: her soft eye makeup, sweet smile and off-shoulder neckline, with blossoms and lanterns only as mood |

**選擇理由：** 24 套中唯一的胸上近景，放在表情最豐富的 Mia；她的身形由橫式款的大腿中段以上負責，所以這張不會大幅減少身材展示。眼睛高度輕俯是常見的美顏角度，不會變形。

**本輪調整：** 景別由膝上改為胸上；白色及膝長靴不入鏡，從 prompt 拿掉；另一手改寫成「自然垂下、不入鏡」。

| 項目 | 內容 |
|---|---|
| 場景 | 春天夜晚的河岸步道，盛開的櫻花樹在頭上交錯，步道旁掛著柔和紙燈籠，步道空無一人。 |
| 服裝 | 洋裝：淺紫細針織貼身露肩迷你洋裝；鞋：白色及膝長靴（不入鏡）；配件：一側小珍珠髮夾、細銀耳環 |
| 髮型 | 灰棕色長髮鬆散大波浪，左側臉旁粉紅 money piece 挑染。 |
| 妝感 | 柔和動漫感眼妝、圓形腮紅、水光唇。 |
| 身材設定（數字） | 160 cm／91-57-88／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 露肩貼身針織洋裝勾出 F 罩杯胸型、細腰與臀線；及膝靴拉長腿部。 |
| 主光 | 畫面外左前方柔和暖色主光 |
| 補光 | 燈籠讓櫻花透出暖粉色，背後深藍夜空 |
| 姿態 | 站在低垂的花枝下。 |
| 手的位置 | 一手輕觸肩旁的花枝，另一手自然垂下、不入鏡。 |
| 表情 | 甜甜的微笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 1.5 公尺，視野 0.42×0.56 公尺；頭頂上方留白約 9%；相機約 1.52 公尺高、畫面中心約 1.4 公尺高，俯仰約 -4.5 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | 她是夜貓子，夜晚的櫻花與燈籠延續她的粉紫配色與「深夜」氣質，但完全是寫真場景。 |
| 與同一人另一款的差異 | 橫式款是夏日黃昏海邊碼頭、粉色緞面馬甲＋白裙；這款是春夜櫻花、淺紫針織洋裝＋長靴。 |
| 參考照片（用途） | mia-08：表情（開朗的笑）；mia-06：身分（認臉；畫面裡的帽 T 與貓不採用） |
| 推薦月份 | 3 月（春） |

| 風險 | 處理 |
|---|---|
| 燈籠上出現文字 | 寫素面紙燈籠 |
| 夜景臉暗 | 寫明柔和主光 |
| 碰花枝的手指變形 | 生成後檢查 |

prompt 草稿（3:4，尚未執行）：

```text
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a soft round face with big expressive eyes, softly winged liner, rounded blush and glossy tinted lips, long ash-brown hair in loose waves with a pastel-pink money-piece highlight framing the left side of her face. Curvy figure, 160 cm tall, bust 91 cm, waist 57 cm, hips 88 cm, F cup, a full chest and a slim waist. She wears a lilac fitted fine-knit off-shoulder mini dress that follows her full chest, small pearl hair clips on one side and thin silver earrings. Setting: a riverside promenade at night in spring, cherry trees in full bloom arching overhead, soft plain paper lanterns hanging along the path, the path empty. One hand lightly touches a blossom branch beside her shoulder; she smiles sweetly. Shot: a chest-up portrait, from a little above her head down to just below her bust, above the elbows, showing the off-shoulder knit neckline, her shoulders, collarbones and chest, one hand touching a blossom branch beside her shoulder and the other arm relaxed below the frame. Body: standing under a low blossom branch, her body turned about 30 degrees toward camera-right, shoulders relaxed so the off-shoulder neckline sits evenly. Face and gaze: her face in a three-quarter view, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 1.5 metres, camera at her eye level, tilted slightly downward, natural perspective without distortion. Composition: she is slightly left of centre, blossom branches framing the top and upper right, the lanterns softened into warm bokeh, her face in the upper third. Emphasis: the closest shot of the set: her soft eye makeup, sweet smile and off-shoulder neckline, with blossoms and lanterns only as mood. Lighting: a soft warm key light from front-left just out of frame lights her face evenly; the lanterns give the blossoms a warm pink glow against a deep blue night sky; pink, lilac and deep blue tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.18 V-yuna-kim｜Yuna｜直式款（新企劃）

**一句話：** 深秋的銀杏大道，奶油色毛呢短外套套裝配黑色長靴，站在落葉上的韓劇感街拍寫真。

**攝影：** 全身｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜臀部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 全身 | a full-length shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在腳下方，雙腳完整。入鏡：從髮頂到靴底完整；毛呢短外套、高腰迷你裙、雙腿與黑色及膝長靴；拉包帶的手與自然垂放的手 | from a little above her head to just below her feet, both feet whole, showing her whole figure from head to boots, the cropped tweed jacket, the high-waisted mini skirt, her legs and the black knee-high boots, one hand on the bag strap and the other relaxed at her side |
| 3. 身體朝向 | 約30度斜側（朝畫面右）：站在落葉人行道上，重心在後腳、前腳朝畫面右側輕踏；身體朝畫面右轉約30度，肩與臀同向 | standing on the leaf-covered sidewalk with her weight on her back leg and her front foot stepping lightly toward camera-right, her body turned about 30 degrees toward camera-right, shoulders and hips turned together |
| 4. 臉部朝向與視線 | 三分之二側臉，看鏡頭 | her face in a three-quarter view, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她臀部高度，平視（參考：85mm 鏡頭、約 5.3 公尺；畫面中心與相機高度差換算俯仰約 -0.3 度） | camera at her hip height, level |
| 6. 畫面配置 | 人物略偏左（約四成處）；身體與步伐朝右，右側留出銀杏大道往遠方延伸的空間，兩側金黃銀杏框住畫面 | she stands slightly left of centre, her body and step toward the right where the ginkgo avenue recedes into the distance, golden trees framing both sides |
| 7. 攝影目的 | 全身＋斜側步伐拉長 168 公分的腿部比例，呈現毛呢套裝與長靴的韓系街拍造型 | the full-length oblique step lengthens her long legs and shows the tweed set and boots as a Korean street-style look |

**選擇理由：** 直式款負責 Yuna 的腿長：全身斜側、腳步朝右，比正面站更有街拍的動感；三分之二側臉看鏡頭，仍能認人。

**本輪調整：** 身體由正面改為約30度斜側並加上往右的腳步；人物由置中改為略偏左；臉改為三分之二側臉。

| 項目 | 內容 |
|---|---|
| 場景 | 深秋安靜的住宅大道，兩旁金黃銀杏，人行道鋪滿落葉，低矮的現代建築在背景失焦，街上沒有人。 |
| 服裝 | 上身：奶油色毛呢短外套（無領、扣起、合身）；下身：同色高腰毛呢迷你裙；鞋：黑色及膝皮長靴；配件：小珍珠耳環、小黑色肩背包 |
| 髮型 | 深棕自然波浪、鎖骨長度、空氣感八字瀏海。 |
| 妝感 | 水光肌、眼妝為重點、珊瑚漸層唇。 |
| 身材設定（數字） | 168 cm／84-58-89／C（纖細長腿） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 合身短外套收在腰上、高腰迷你裙與及膝長靴拉長 168 cm 的腿部比例。 |
| 主光 | 銀杏樹後方的低角度午後陽光，頭髮上一圈暖色輪廓 |
| 補光 | 畫面外前方大反光板 |
| 姿態 | 站在落葉人行道上。 |
| 手的位置 | 一手拉著肩上的包包背帶，一手自然垂放。 |
| 表情 | 頭微傾、柔和的微笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 5.3 公尺，視野 1.5×2.0 公尺；人物約佔畫面高度 87%；相機約 0.92 公尺高、畫面中心約 0.9 公尺高，俯仰約 -0.3 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | 毛呢套裝、長靴、水光妝與銀杏的金黃——用穿搭、色調與季節建立韓系美感，沒有任何文字或地標。 |
| 與同一人另一款的差異 | 橫式款是室內咖啡館、奶油黃開襟＋緞面裙、坐姿；這款是戶外銀杏大道、毛呢套裝＋長靴、站姿全身。 |
| 參考照片（用途） | yuna-11：場景（首爾街頭夕陽光線；回頭姿勢不採用）；yuna-03：表情（柔和近照與妝感） |
| 推薦月份 | 11 月（深秋） |

| 風險 | 處理 |
|---|---|
| 背景出現招牌或文字 | 寫明低矮建築失焦、不寫店面 |
| 逆光臉暗 | 寫明反光板 |
| 包包出現 logo | 寫素面小包 |

prompt 草稿（3:4，尚未執行）：

```text
A 21-year-old adult Korean woman with her natural fair skin tone, large bright double-eyelid eyes as the focus of her makeup, a dewy glass-skin finish and soft coral gradient lips, dark-brown natural wavy hair at collarbone length with airy curtain bangs. Slim, long-legged figure, 168 cm tall, bust 84 cm, waist 58 cm, hips 89 cm, C cup, a narrow waist and long legs. She wears a cream tweed cropped jacket, collarless and buttoned, fitted close to her chest and waist, a matching high-waisted tweed mini skirt, black knee-high leather boots, small pearl earrings and a small plain black shoulder bag. Setting: a quiet residential avenue in late autumn lined with golden ginkgo trees, fallen yellow leaves covering the sidewalk, low modern buildings softly out of focus, the street empty. One hand holds the strap of the bag at her shoulder and the other is relaxed at her side; her head tilts slightly with a soft smile. Shot: a full-length shot, from a little above her head to just below her feet, both feet whole, showing her whole figure from head to boots, the cropped tweed jacket, the high-waisted mini skirt, her legs and the black knee-high boots, one hand on the bag strap and the other relaxed at her side. Body: standing on the leaf-covered sidewalk with her weight on her back leg and her front foot stepping lightly toward camera-right, her body turned about 30 degrees toward camera-right, shoulders and hips turned together. Face and gaze: her face in a three-quarter view, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 5.3 metres, camera at her hip height, level, natural perspective without distortion; she fills about 87% of the frame height. Composition: she stands slightly left of centre, her body and step toward the right where the ginkgo avenue recedes into the distance, golden trees framing both sides. Emphasis: the full-length oblique step lengthens her long legs and shows the tweed set and boots as a Korean street-style look. Lighting: low afternoon sun behind the ginkgo trees lights the leaves and draws a warm rim on her hair; a large white reflector just out of frame lights her face evenly; golden yellow, cream and black tones with a soft film-like finish. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.19 V-tammy-chou｜Tammy｜直式款（新企劃）

**一句話：** 夜晚的大飯店大廳，白色西裝外套洋裝配黑色細跟鞋，雙手插腰的自信全身照。

**攝影：** 大腿中段以上｜正面｜臉正面・看鏡頭｜腰部高度・輕仰

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 大腿中段以上 | a mid-thigh-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在大腿中段，不切在膝蓋。入鏡：深 V 翻領、金扣與腰帶、迷你裙擺與大腿上段；雙手插腰，兩手都在框內 | from a little above her head down to mid-thigh, well above the knees, showing the deep V lapel, the gold buttons and belted waist, the mini skirt hem and her upper thighs, with both hands on her hips inside the frame |
| 3. 身體朝向 | 正面：站在大理石柱旁，重心在一隻腳；身體正對鏡頭，肩膀打開、雙手插腰，臀部隨重心微微偏向一側 | standing beside a marble column with her weight on one leg, her body square to the camera, shoulders open and both hands on her hips, her hips shifted slightly to one side |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她腰部高度，輕仰（參考：70mm 鏡頭、約 2.3 公尺；畫面中心與相機高度差換算俯仰約 +3.5 度） | camera at her waist height, tilted slightly upward |
| 6. 畫面配置 | 人物置中；水晶吊燈的暖光在她頭頂上方，大理石柱在一側、白花在背景失焦 | she is centred, the warm crystal chandelier glowing above her head, a marble column at one side and the white flowers soft in the background |
| 7. 攝影目的 | 大腿中段以上加上輕仰，呈現雙手插腰的自信與西裝洋裝勾出的胸腰比例 | a closer frame with a slightly low camera that shows her confident hands-on-hips stance and how the blazer dress defines her chest and waist |

**選擇理由：** 高跟鞋已由橫式款全身呈現；直式款改大腿中段以上，正面插腰配腰部高度輕仰，拍出大飯店夜晚的氣場。

**本輪調整：** 景別由全身改為大腿中段以上；黑色細高跟鞋不入鏡，從 prompt 拿掉；相機改為腰部高度輕仰。

| 項目 | 內容 |
|---|---|
| 場景 | 夜晚大飯店的大廳：拋光大理石地板與柱子、頭頂溫暖的水晶吊燈、背景圓桌上一大盆白花，大廳沒有其他人。 |
| 服裝 | 洋裝：白色合身西裝外套式迷你洋裝（深 V 翻領、金色扣子、繫腰帶）；鞋：黑色尖頭細高跟鞋（不入鏡）；配件：金色垂墜耳環 |
| 髮型 | 奶茶金棕大波浪長捲髮，臉側淺色 money piece 挑染。 |
| 妝感 | 閃粉眼影、果凍唇。 |
| 身材設定（數字） | 160 cm／90-57-89／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 深 V 翻領與腰帶勾出 E 罩杯胸型與細腰；迷你裙長與高跟鞋讓腿部比例完整。 |
| 主光 | 畫面外右前方柔光 |
| 補光 | 水晶吊燈的暖色環境光 |
| 姿態 | 站在大理石柱旁。 |
| 手的位置 | 雙手插腰。 |
| 表情 | 自信的笑容 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，70mm，約 2.3 公尺，視野 0.79×1.05 公尺；頭頂上方留白約 6%；相機約 1.08 公尺高、畫面中心約 1.22 公尺高，俯仰約 +3.5 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | 合身洋裝＋高跟鞋，換成白色俐落的西裝洋裝，配上大飯店的大理石與吊燈——高級感來自場景與剪裁。 |
| 與同一人另一款的差異 | 橫式款是白天精品店、熱粉針織洋裝；這款是夜晚飯店大廳、白色西裝洋裝、全身站姿。 |
| 參考照片（用途） | tammy-01：服裝材質（貼身洋裝的線條）；tammy-03：表情（較柔的表情） |
| 推薦月份 | 1 月（年末） |

| 風險 | 處理 |
|---|---|
| 大廳出現其他人或招牌 | 寫明大廳無人、不寫招牌 |
| 高跟鞋腳部結構 | 生成後放大檢查 |

prompt 草稿（3:4，尚未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, round almond eyes with visible aegyo-sal, shimmer eyeshadow and jelly-glossy lips, long voluminous big-wave hair in milk-tea golden brown with light money-piece highlights at the front. Curvy figure, 160 cm tall, bust 90 cm, waist 57 cm, hips 89 cm, E cup, a full chest and a slim waist. She wears a white tailored blazer mini dress with a deep V lapel, gold buttons and a belted waist that defines her full chest and slim waist, and gold drop earrings. Setting: the lobby of a grand hotel at night, polished marble floor and columns, a warm crystal chandelier overhead, a large arrangement of white flowers on a round table in the background, the lobby empty. Both hands rest on her hips; she smiles confidently. Shot: a mid-thigh-up shot, from a little above her head down to mid-thigh, well above the knees, showing the deep V lapel, the gold buttons and belted waist, the mini skirt hem and her upper thighs, with both hands on her hips inside the frame. Body: standing beside a marble column with her weight on one leg, her body square to the camera, shoulders open and both hands on her hips, her hips shifted slightly to one side. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with a 70mm lens from about 2.3 metres, camera at her waist height, tilted slightly upward, natural perspective without distortion. Composition: she is centred, the warm crystal chandelier glowing above her head, a marble column at one side and the white flowers soft in the background. Emphasis: a closer frame with a slightly low camera that shows her confident hands-on-hips stance and how the blazer dress defines her chest and waist. Lighting: warm chandelier light fills the space; a soft key light from front-right just out of frame lights her face evenly; white, gold and warm marble tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.20 V-rin-ayase｜Rin｜直式款（Penny 採用的 v2 替代方向）

**一句話：** Penny 採用的 v2 替代方向：出勤前的銀座，黑色絲絨細肩帶長禮服，坐在金色燈光的吧台邊（不拿酒杯）。

**攝影：** 坐姿全身｜約45度斜側（朝畫面左）｜三分之二側臉・看鏡頭｜坐姿時的腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 坐姿全身 | a full-length seated shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在及地長禮服下襬下方，雙腳被禮服蓋住。入鏡：從髮頂到禮服下襬完整；貼身絲絨上身的胸腰線、交疊雙腿在長禮服下的線條；靠在吧台上的手肘與放在膝上的手（不拿杯子） | her whole seated figure from a little above her head to just below the hem of her floor-length gown, showing her whole seated figure from head to the hem of the gown, the fitted velvet bodice over her chest and waist and the line of her crossed legs under the gown, one elbow on the counter and the other hand on her knee, holding nothing |
| 3. 身體朝向 | 約45度斜側（朝畫面左）：坐在高腳椅上（吧台在畫面左），雙腿在長禮服下交疊；身體朝畫面左轉約45度，一側手肘靠在吧台上，背挺直、肩線放鬆 | seated on a tall bar stool beside the counter on camera-left with her legs crossed under the gown, her body turned about 45 degrees toward camera-left, one elbow on the counter, back straight and shoulders relaxed |
| 4. 臉部朝向與視線 | 三分之二側臉，看鏡頭 | her face in a three-quarter view, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她坐姿時的腰部高度，平視（參考：70mm 鏡頭、約 4.1 公尺；畫面中心與相機高度差換算俯仰約 -1.9 度） | camera at her seated waist height, level |
| 6. 畫面配置 | 人物在右側約六成處；金色燈光的長吧台從左下沿對角線往後延伸，吊燈光點在上方；人物佔畫面高度約八成六 | she sits right of centre, the long golden-lit counter running diagonally from the lower left into the background, the pendant lights glowing above |
| 7. 攝影目的 | 斜側坐姿讓絲絨上身的胸腰曲線與交疊雙腿的長線條同時成立；三分之二側臉呈現她細長的眼與挺直的鼻 | the oblique seated pose shows both the curve of the velvet bodice and the long line of her crossed legs, and the three-quarter face shows her long narrow eyes and straight nose |

**選擇理由：** 依 Penny 採用的替代方向（坐在金色燈光的吧台邊、不拿酒杯）；吧台改成對角線，比置中更有空間感；三分之二側臉適合她的五官。

**本輪調整：** 人物由置中改為右側、吧台改成對角線；臉改為三分之二側臉；黑色細帶高跟鞋多被及地長禮服蓋住，從 prompt 拿掉（中文標不入鏡）。

| 項目 | 內容 |
|---|---|
| 場景 | 開店前的高級會員制酒吧：一長條拋光深色木吧台、溫暖的金色吊燈、背後柔焦的層架，吧台面乾淨，店內沒有其他人。 |
| 服裝 | 洋裝：黑色絲絨細肩帶及地長禮服（貼身上身）；鞋：黑色細帶高跟鞋（被及地長禮服蓋住，不入鏡）；配件：小金色垂墜耳環、細金手鍊 |
| 髮型 | 深酒紅棕長髮，光滑的低髻。 |
| 妝感 | 乾淨底妝、精準眼線、豆沙紅唇。 |
| 身材設定（數字） | 166 cm／92-58-90／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身絲絨上身呈現 F 罩杯胸型與細腰；坐在高腳椅上、雙腿交疊，長禮服順著腿部線條垂下。 |
| 主光 | 頭頂溫暖的金色吊燈＋畫面外左前方柔光 |
| 補光 | 吧台與層架的金色反光 |
| 姿態 | 坐在高腳椅上，雙腿交疊。 |
| 手的位置 | 一手手肘靠在吧台上，一手放在膝上；手上不拿杯子。 |
| 表情 | 平靜、端莊的微笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，70mm，約 4.1 公尺，視野 1.41×1.87 公尺；人物約佔畫面高度 86%；相機約 0.98 公尺高、畫面中心約 0.84 公尺高，俯仰約 -1.9 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | 逐字依 Penny 採用的替代方向（出勤前的銀座：黑色絲絨細肩帶長禮服，坐在金色燈光的吧台邊，不拿酒杯）；及地長禮服適合直幅。 |
| 與同一人另一款的差異 | 橫式款是飯店套房夕陽、酒紅緞面中長洋裝、斜躺；這款是酒吧金色燈光、黑色絲絨長禮服、坐高腳椅。 |
| 參考照片（用途） | rin-09：服裝材質（黑洋裝＋高跟鞋的線條）；rin-04：表情（Penny 喜歡的成熟氣質） |
| 推薦月份 | 10 月（秋） |

| 風險 | 處理 |
|---|---|
| 出現酒杯或酒瓶 | 只寫乾淨的吧台與柔焦層架，手上不拿東西 |
| 寫「銀座」生出招牌字 | prompt 只寫高級會員制酒吧的元素，不寫地名招牌 |

prompt 草稿（3:4，尚未執行）：

```text
A 25-year-old adult Japanese woman with her natural fair, cool-toned skin, an oval face with long narrow eyes and a straight nose, a clean base with precise eyeliner and a muted rose-red lip, long deep wine-red brown hair pinned in a sleek low bun. Curvy figure, 166 cm tall, bust 92 cm, waist 58 cm, hips 90 cm, F cup, a full chest, a slim waist and long legs. She wears a black velvet floor-length gown with thin spaghetti straps and a fitted bodice that follows her full chest and slim waist, small gold drop earrings and a thin gold bracelet. Setting: an elegant high-end Tokyo members' bar before opening, a long polished dark-wood counter, warm golden pendant lights and softly blurred shelves behind the counter, the counter clean and clear, the bar empty. One elbow rests on the counter and the other hand rests on her knee, holding nothing; she has a calm, poised smile. Shot: a full-length seated shot, her whole seated figure from a little above her head to just below the hem of her floor-length gown, showing her whole seated figure from head to the hem of the gown, the fitted velvet bodice over her chest and waist and the line of her crossed legs under the gown, one elbow on the counter and the other hand on her knee, holding nothing. Body: seated on a tall bar stool beside the counter on camera-left with her legs crossed under the gown, her body turned about 45 degrees toward camera-left, one elbow on the counter, back straight and shoulders relaxed. Face and gaze: her face in a three-quarter view, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with a 70mm lens from about 4.1 metres, camera at her seated waist height, level, natural perspective without distortion; she fills about 86% of the frame height. Composition: she sits right of centre, the long golden-lit counter running diagonally from the lower left into the background, the pendant lights glowing above. Emphasis: the oblique seated pose shows both the curve of the velvet bodice and the long line of her crossed legs, and the three-quarter face shows her long narrow eyes and straight nose. Lighting: warm golden pendant light from above and a soft key light from front-left just out of frame light her face evenly; the velvet holds deep black while the counter glows gold; black, gold and deep wood tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.21 V-rainie-hsu｜Rainie｜直式款（新企劃）

**一句話：** 雨後的夜晚街道，黑色緞面繞頸迷你洋裝外搭黑色長皮風衣，站在濕亮的路面上直視鏡頭。

**攝影：** 膝上｜側面（朝畫面右）｜三分之二側臉・看鏡頭｜腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：側面的胸型與腰臀曲線、緞面繞頸洋裝與長風衣到膝蓋下方；拉著衣襟的手在腰間、另一手垂在大腿旁 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the side curves of her chest, waist and hips, the satin halter dress and the long open coat down to just below the knees, one hand holding the coat edge at her waist and the other relaxed beside her thigh |
| 3. 身體朝向 | 側面（朝畫面右）：站在濕亮的人行道上，身體側面朝畫面右；重心在後腳、前腳輕踏，肩與臀同向，敞開的長風衣從肩線垂成直線 | standing on the wet pavement, her body side-on to the camera, facing camera-right, weight on her back leg and her front foot stepping lightly, shoulders and hips aligned, the open coat falling in a straight line from her shoulders |
| 4. 臉部朝向與視線 | 三分之二側臉，直視鏡頭 | her face in a three-quarter view, looking straight into the camera |
| 5. 相機高度與俯仰 | 相機在她腰部高度，平視（參考：85mm 鏡頭、約 3.6 公尺；畫面中心與相機高度差換算俯仰約 +0.8 度） | camera at her waist height, level |
| 6. 畫面配置 | 人物在左側約四成處、身體朝右；右側留給濕亮街道往遠處延伸的倒影 | she stands left of centre with her body toward the right, the wet street and its reflections receding into the space on the right |
| 7. 攝影目的 | 側身讓胸與臀的側面曲線、長風衣的直線同時成立；三分之二側臉配直視保留氣場與辨識度 | the side-on stance shows the side curves of her chest and hips against the straight line of the long coat, and the three-quarter face with a direct gaze keeps her presence and recognisability |

**選擇理由：** 她的高顴骨與立體下顎適合側面；24 套中唯一的「側身站姿＋膝上」，與橫式款的正面靠欄杆完全不同。頭轉回鏡頭約55度，在自然範圍內，不是回眸。

**本輪調整：** 身體由正面改為側面、臉改為三分之二側臉；人物由置中改為左側約四成；黑色短靴不入鏡，從 prompt 拿掉。

| 項目 | 內容 |
|---|---|
| 場景 | 夜晚剛下過雨的城市街道：濕亮的路面倒映暖色櫥窗光與冷色路燈，店面已打烊、只有素面霧玻璃，街上沒有人。 |
| 服裝 | 洋裝：黑色緞面繞頸迷你洋裝；外套：黑色長版皮革風衣（敞開）；鞋：黑色細跟尖頭短靴（不入鏡）；配件：大型銀色垂墜耳環 |
| 髮型 | 長直黑髮，光滑有光澤，深側分。 |
| 妝感 | 柔和魅惑妝、貼近睫毛的淡棕眼線。 |
| 身材設定（數字） | 165 cm／94-59-92／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 繞頸緞面洋裝貼合 F 罩杯胸型、細腰與臀線；敞開的長風衣形成直向線條，讓 165 cm 的身形更修長。 |
| 主光 | 畫面外左前方大型柔光，臉清楚 |
| 補光 | 濕路面上暖琥珀與冷藍的倒影 |
| 姿態 | 站在濕亮的人行道上。 |
| 手的位置 | 一手拉著敞開的風衣衣襟在腰間，一手自然垂在大腿旁。 |
| 表情 | 自信、帶點壞的笑 |
| 視線 | 直視鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 3.6 公尺，視野 1.02×1.36 公尺；頭頂上方留白約 7%；相機約 1.09 公尺高、畫面中心約 1.14 公尺高，俯仰約 +0.8 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | 她的配色是黑、煙灰、金屬銀；雨夜街道的倒影是派對夜的另一種華麗，與頂樓燈海完全不同。 |
| 與同一人另一款的差異 | 橫式款是頂樓燈海、血紅馬甲洋裝、靠欄杆；這款是雨夜街道、黑色緞面＋長皮風衣、站在路面。 |
| 參考照片（用途） | rainie-01：表情（濃豔妝感與氣場）；rainie-11：服裝材質（黑色細肩帶洋裝的線條） |
| 推薦月份 | 5 月（春末梅雨） |

| 風險 | 處理 |
|---|---|
| 店面出現招牌文字 | 寫明打烊的素面霧玻璃 |
| 夜景臉暗 | 寫明大型柔光主光 |
| 路面倒影出現其他人 | 寫明街上沒有人 |

prompt 草稿（3:4，尚未執行）：

```text
A 24-year-old adult Taiwanese woman with her natural fair skin tone, high cheekbones and a sculpted jaw, soft-glam makeup with a soft brown liner close to the lash line, long straight jet-black hair worn sleek and glossy with a deep side part. Curvy figure, 165 cm tall, bust 94 cm, waist 59 cm, hips 92 cm, F cup, full chest and slim waist. She wears a black satin halter mini dress that follows her full chest, slim waist and hips, a long black leather trench coat worn open and large silver statement drop earrings. Setting: a city street at night just after rain, the wet pavement reflecting warm amber light from closed shopfronts with plain frosted glass and cool blue street lights, the street empty. One hand holds the edge of the open coat at her waist and the other is relaxed beside her thigh, with a confident, slightly mischievous smirk. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the side curves of her chest, waist and hips, the satin halter dress and the long open coat down to just below the knees, one hand holding the coat edge at her waist and the other relaxed beside her thigh. Body: standing on the wet pavement, her body side-on to the camera, facing camera-right, weight on her back leg and her front foot stepping lightly, shoulders and hips aligned, the open coat falling in a straight line from her shoulders. Face and gaze: her face in a three-quarter view, looking straight into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.6 metres, camera at her waist height, level, natural perspective without distortion. Composition: she stands left of centre with her body toward the right, the wet street and its reflections receding into the space on the right. Emphasis: the side-on stance shows the side curves of her chest and hips against the straight line of the long coat, and the three-quarter face with a direct gaze keeps her presence and recognisability. Lighting: a large soft key light from front-left just out of frame lights her face clearly; warm amber and cool blue reflections shimmer on the wet street behind her; black, silver and deep blue tones with a hint of amber. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.22 V-miu-shiraishi｜Miu｜直式款（新企劃）

**一句話：** 暮春的運河步道，奶油色 V 領合身針織洋裝繫細腰帶，靠著欄杆甜笑。

**攝影：** 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 大腿中段以上 | a mid-thigh-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在大腿中段，不切在膝蓋。入鏡：V 領合身針織洋裝的胸型、細腰帶收出的腰線、迷你裙擺與大腿上段；扶欄杆的手與拿著臉旁髮絲的手（不遮臉） | from a little above her head down to mid-thigh, well above the knees, showing the fitted V-neck knit dress over her full chest, the thin belt at her very slim waist, the mini skirt hem and her upper thighs, one hand on the railing and the other holding a strand of hair beside her cheek without covering her face |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：站在欄杆旁，重心在靠欄杆的那隻腳；身體朝畫面左轉約30度，肩與臀同向，腰線自然拉長 | standing by the railing with her weight on the leg nearer the railing, her body turned about 30 degrees toward camera-left, shoulders and hips turned together |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她胸口高度，平視（參考：85mm 鏡頭、約 2.8 公尺；畫面中心與相機高度差換算俯仰約 -0.1 度） | camera at her chest height, level |
| 6. 畫面配置 | 人物略偏左；低矮欄杆從右下沿對角線延伸到她手邊，後方是新綠的運河與失焦的對岸 | she stands slightly left of centre, the low railing running diagonally from the lower right to her hand, the green canal and the soft far bank behind her |
| 7. 攝影目的 | 大腿中段以上把 V 領胸型與細腰帶的腰線放大，斜側讓胸腰曲線更立體 | a closer frame that enlarges the V-neck chest line and the belted waist, the oblique stance giving her curves more shape |

**選擇理由：** Miu 的設定重點是胸型與腰線：大腿中段以上把兩者放大；扶欄杆的手在身側、拿髮絲的手在臉旁，都不擋胸腰。

**本輪調整：** 景別由膝上改為大腿中段以上，人物由置中改為略偏左＋欄杆對角線；奶油色低跟鞋不入鏡，從 prompt 拿掉。

| 項目 | 內容 |
|---|---|
| 場景 | 暮春安靜的運河步道：窄窄的運河兩岸新綠的樹、低矮金屬欄杆、對岸的小咖啡館在背景失焦，步道上沒有人。 |
| 服裝 | 洋裝：奶油色 V 領細羅紋合身針織迷你洋裝（前排小扣、細棕色腰帶）；鞋：奶油色繫踝低跟鞋（不入鏡）；配件：細金耳針 |
| 髮型 | 淺亞麻米金，齊肩內彎鮑伯、空氣瀏海。 |
| 妝感 | 眼下橘調腮紅、水潤唇。 |
| 身材設定（數字） | 156 cm／87-55-86／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | V 領與合身細針織清楚呈現 E 罩杯胸型，細腰帶收出 55 cm 的腰線；迷你裙長露出腿。 |
| 主光 | 明亮柔和的陰天光 |
| 補光 | 畫面外白色反光板 |
| 姿態 | 站在欄杆旁。 |
| 手的位置 | 一手扶著欄杆，一手輕輕拿著臉旁的一縷頭髮（不遮臉）。 |
| 表情 | 甜甜的微笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 2.8 公尺，視野 0.79×1.05 公尺；頭頂上方留白約 8%；相機約 1.16 公尺高、畫面中心約 1.16 公尺高，俯仰約 -0.1 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | 她的支柱「外出／中目黑」：運河新綠與奶油色針織洋裝，甜美裡有曲線，不是厚重寬鬆的毛衣。 |
| 與同一人另一款的差異 | 橫式款是室內晨光床邊、緞面小可愛＋短褲；這款是戶外運河步道、V 領針織洋裝＋腰帶。 |
| 參考照片（用途） | miu-05：場景（運河邊的環境與光線；回頭姿勢不採用）；miu-07：身分（運河散步的全身比例） |
| 推薦月份 | 4 月（春） |

| 風險 | 處理 |
|---|---|
| 對岸店面出現招牌字 | 寫明失焦，不寫店名 |
| 拿頭髮的手指融合 | 生成後檢查 |
| 童顏顯小 | 寫明 adult、成熟剪裁 |

prompt 草稿（3:4，尚未執行）：

```text
A 22-year-old adult Japanese woman with her natural very fair skin tone, a round face with big soft downturned eyes, orange-toned blush under the eyes and glossy lips, light flaxen beige-blonde hair in a shoulder-length bob curled inward with airy see-through bangs. Petite curvy figure, 156 cm tall, bust 87 cm, waist 55 cm, hips 86 cm, E cup, a full chest and a very slim waist. She wears a cream fitted V-neck fine-rib knit mini dress with small front buttons and a thin brown belt at the waist that shows her full chest and very slim waist, and thin gold stud earrings. Setting: a quiet canal-side promenade in late spring, fresh green trees along a narrow canal, a low metal railing, small cafés softly out of focus on the far bank, the promenade empty. One hand rests on the railing and the other lightly holds a strand of her hair beside her cheek without covering her face; she smiles sweetly. Shot: a mid-thigh-up shot, from a little above her head down to mid-thigh, well above the knees, showing the fitted V-neck knit dress over her full chest, the thin belt at her very slim waist, the mini skirt hem and her upper thighs, one hand on the railing and the other holding a strand of hair beside her cheek without covering her face. Body: standing by the railing with her weight on the leg nearer the railing, her body turned about 30 degrees toward camera-left, shoulders and hips turned together. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 2.8 metres, camera at her chest height, level, natural perspective without distortion. Composition: she stands slightly left of centre, the low railing running diagonally from the lower right to her hand, the green canal and the soft far bank behind her. Emphasis: a closer frame that enlarges the V-neck chest line and the belted waist, the oblique stance giving her curves more shape. Lighting: soft bright overcast daylight with a white reflector just out of frame lighting her face evenly; fresh green, cream and soft brown tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.23 V-jia-seo｜Jia｜直式款（新企劃）

**一句話：** 明亮的玻璃溫室，白色無袖立領短上衣配薄荷綠緞面開衩中長裙，站在大葉植物之間。

**攝影：** 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜腰部高度・平視

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：白色立領短上衣與露出的細腰、緞面中長裙的臀線、側開衩露出的腿到膝蓋下方；碰葉子的手與插腰的手 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the white mock-neck crop top and her bare slim waist, the satin skirt over her hips and the leg through the side slit down to just below the knee, one hand touching a monstera leaf and the other on her hip |
| 3. 身體朝向 | 約30度斜側（朝畫面右）：站在石板小徑上，重心在後腳、開衩那側的腿往前；身體朝畫面右轉約30度，肩與臀同向 | standing on the stone path with her weight on her back leg and the leg on the slit side stepping forward, her body turned about 30 degrees toward camera-right, shoulders and hips turned together |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她腰部高度，平視（參考：85mm 鏡頭、約 3.6 公尺；畫面中心與相機高度差換算俯仰約 +0.6 度） | camera at her waist height, level |
| 6. 畫面配置 | 人物置中；兩側大片龜背芋葉框住畫面邊緣，白色鋼骨溫室結構在上方；葉子只在兩側、不遮身體 | she is centred on the path, large monstera leaves framing both side edges and the white steel frames of the greenhouse above, the leaves never covering her body |
| 7. 攝影目的 | 斜側讓緞面裙的臀線與開衩腿線更明顯，露腰短上衣呈現她的細腰 | the oblique stance makes the satin skirt's hip line and the slit leg clearer, and the crop top shows her slim waist |

**選擇理由：** 直式用斜側＋葉子框邊，和橫式款的側身全身不同；膝上剛好收進開衩露出的腿，不切在膝蓋。

**本輪調整：** 身體由正面改為約30度斜側，兩側加上葉子框邊；白色細帶涼鞋不入鏡，從 prompt 拿掉。

| 項目 | 內容 |
|---|---|
| 場景 | 玻璃溫室：白色鋼骨結構、茂密的熱帶植物與大片龜背芋葉、石板小徑，溫室裡沒有其他人。 |
| 服裝 | 上身：白色無袖立領貼身短上衣（露腰）；下身：高腰薄荷鼠尾草綠緞面中長裙（側開衩）；鞋：白色細帶涼鞋（不入鏡）；配件：細銀耳針 |
| 髮型 | 冷灰藍黑長髮，一側塞在耳後露出薄荷綠內層。 |
| 妝感 | 水光無妝感、淡棕眼線、漸層唇。 |
| 身材設定（數字） | 168 cm／85-58-90／C（直角肩、長腿） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 短上衣露出細腰，緞面長裙貼著臀線、側開衩露出一條長腿。 |
| 主光 | 玻璃屋頂的大面積明亮漫射光 |
| 補光 | 畫面外前方柔光 |
| 姿態 | 站在植物之間的石板路上。 |
| 手的位置 | 一手輕觸身旁的大片龜背芋葉，一手插腰。 |
| 表情 | 冷靜柔和的微笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 3.6 公尺，視野 1.02×1.36 公尺；頭頂上方留白約 6%；相機約 1.08 公尺高、畫面中心約 1.12 公尺高，俯仰約 +0.6 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | 薄荷綠是她的髮色內層與配色；溫室的綠與白延伸她的冷調，實景、無運動感。 |
| 與同一人另一款的差異 | 橫式款是美術館白牆、黑色單肩洋裝；這款是溫室綠意、白色短上衣＋薄荷緞面開衩裙。 |
| 參考照片（用途） | jia-03：身分（白色上衣與認臉）；jia-07：服裝材質（白色綁結上衣的露腰比例） |
| 推薦月份 | 2 月（冬末） |

| 風險 | 處理 |
|---|---|
| 植物遮住身體 | 寫明站在小徑上、葉子在身旁 |
| 開衩遮蔽 | 生成後檢查 |

prompt 草稿（3:4，尚未執行）：

```text
A 22-year-old adult Korean woman with her natural fair, cool-toned skin, a small face, straight shoulders and long narrow upturned eyes, dewy no-makeup makeup with a soft brown liner and gradient lips, long cool blue-black hair tucked behind one ear so its mint-green inner layer shows. Slim, long-legged figure with soft feminine curves, 168 cm tall, bust 85 cm, waist 58 cm, hips 90 cm, C cup, a slim waist and long legs. She wears a white sleeveless mock-neck fitted crop top that shows her slim waist, a high-waisted mint-sage satin midi skirt with a side slit and small silver stud earrings. Setting: a glass greenhouse conservatory with white steel frames, lush tropical plants and large monstera leaves, a stone path, the greenhouse empty. One hand lightly touches a large monstera leaf beside her and the other rests on her hip, the slit of the skirt showing one leg; she has a cool, soft smile. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the white mock-neck crop top and her bare slim waist, the satin skirt over her hips and the leg through the side slit down to just below the knee, one hand touching a monstera leaf and the other on her hip. Body: standing on the stone path with her weight on her back leg and the leg on the slit side stepping forward, her body turned about 30 degrees toward camera-right, shoulders and hips turned together. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.6 metres, camera at her waist height, level, natural perspective without distortion. Composition: she is centred on the path, large monstera leaves framing both side edges and the white steel frames of the greenhouse above, the leaves never covering her body. Emphasis: the oblique stance makes the satin skirt's hip line and the slit leg clearer, and the crop top shows her slim waist. Lighting: bright diffused daylight through the glass roof as a large soft key, a soft fill just out of frame in front; white, mint and deep green tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 8.24 V-yerin-han｜Yerin｜直式款（新企劃）

**一句話：** 日落的白沙海灘，白色圓領貼身針織背心洋裝，赤腳站在淺浪邊的燦笑。

**攝影：** 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・輕仰

| 攝影欄位 | 中文 | prompt 對應句 |
|---|---|---|
| 1. 景別 | 膝上 | a knee-up shot |
| 2. 畫面上下界 | 完整髮頂，上緣少量留白；下緣在膝蓋下方的小腿上段，不切在膝關節。入鏡：貼身羅紋背心洋裝的胸型、細腰與臀線、裙擺下的大腿到膝蓋下方；放在鎖骨的手與自然垂放的手 | from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the fitted ribbed tank dress over her full chest, slim waist and hips and her legs down to just below the knees, one hand at her collarbone and the other relaxed at her side |
| 3. 身體朝向 | 約30度斜側（朝畫面左）：站在淺浪邊，重心在後腳、前膝微彎；身體朝畫面左轉約30度，肩與臀同向 | standing at the water's edge with her weight on her back leg and her front knee softly bent, her body turned about 30 degrees toward camera-left, shoulders and hips turned together |
| 4. 臉部朝向與視線 | 臉正面，看鏡頭 | her face toward the camera, looking into the camera |
| 5. 相機高度與俯仰 | 相機在她臀部高度，輕仰（參考：85mm 鏡頭、約 3.7 公尺；畫面中心與相機高度差換算俯仰約 +3.4 度） | camera at her hip height, tilted slightly upward |
| 6. 畫面配置 | 人物略偏右；海平線壓低在她臀部高度，金色與蜜桃色的夕陽天空佔滿上方與左側，夕陽在她身後形成頭髮輪廓光 | she stands slightly right of centre, the horizon low behind her hips and the gold and peach sunset sky filling the space above and to the left |
| 7. 攝影目的 | 輕仰與低海平線讓 170 公分的身形更修長，斜側呈現臀線的健康曲線 | the slightly low camera and low horizon make her tall figure look longer, and the oblique stance shows the healthy curve of her hips |

**選擇理由：** 海灘夕陽用臀部高度輕仰，讓天空成為乾淨背景、身形更長；斜側呈現 93 公分臀線的健康曲線。與橫式款的坐姿全身不同。

**本輪調整：** 身體由正面改為約30度斜側、人物由置中改為略偏右；相機改為臀部高度輕仰；赤腳與腳鍊在膝上取景外，從 prompt 拿掉。

| 項目 | 內容 |
|---|---|
| 場景 | 日落時寬闊的白沙海灘，平靜的淺水、海上金色與蜜桃色的天空，海灘上沒有其他人。 |
| 服裝 | 洋裝：白色圓領羅紋貼身背心迷你洋裝；鞋：赤腳（不入鏡）；配件：小金色圈耳環、腳踝細金鍊（不入鏡） |
| 髮型 | 亞麻棕長髮、臉側金色挑染，放下的鬆散波浪。 |
| 妝感 | 防曬淡妝、亮色唇。 |
| 身材設定（數字） | 170 cm／90-60-93／E（健康曲線） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身羅紋背心洋裝勾出 E 罩杯胸型、細腰與 93 cm 的臀線；赤腳站立讓長腿比例自然。 |
| 主光 | 她身後的低角度夕陽，頭髮與肩膀暖色輪廓光 |
| 補光 | 畫面外前方大反光板與柔光 |
| 姿態 | 站在淺浪邊。 |
| 手的位置 | 一手輕放在鎖骨，一手自然垂放。 |
| 表情 | 大方燦爛的笑 |
| 視線 | 看鏡頭 |
| 焦段／距離／視野（參考） | 3:4，85mm，約 3.7 公尺，視野 1.04×1.39 公尺；頭頂上方留白約 7%；相機約 0.88 公尺高、畫面中心約 1.1 公尺高，俯仰約 +3.4 度 |
| 原生尺寸 | 3:4 原生 1536×2048（已知：Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 輸出皆 1536×2048） |
| 版面適配 | 直式款建議照片區至少 3:4：原生 3:4 可完整使用。若最後選近方形框（約 0.94:1），要上下共裁約 20%：膝上會變成大腿以上、全身會切到腳——不承諾任意裁切都成立。 |
| 為何符合人設 | 她的支柱「旅遊／球場遠征」的另一面：度假海灘的夕陽，健康又性感，和球場完全不同。 |
| 與同一人另一款的差異 | 橫式款是春日球場、polo＋百褶裙＋球帽、坐球車；這款是日落海灘、白色背心洋裝、赤腳站在水邊。 |
| 參考照片（用途） | yerin-07：服裝材質（白色平口＋白短裙的清爽穿搭）；yerin-08：表情（燦爛的大笑） |
| 推薦月份 | 8 月（盛夏） |

| 風險 | 處理 |
|---|---|
| 逆光臉暗 | 寫明反光板與柔光 |
| 白色洋裝濕透透光 | 寫明站在淺浪邊、洋裝是乾的 |
| 膚色被曬成小麥色 | 只寫一次她原本的白皙膚色 |

prompt 草稿（3:4，尚未執行）：

```text
A 26-year-old adult Korean woman with her natural fair skin tone, bright defined features and a wide open smile, light sun-protective makeup and a bright lip, long flax-brown hair with golden face-framing highlights worn down in loose waves. Curvy athletic figure with soft feminine lines, 170 cm tall, bust 90 cm, waist 60 cm, hips 93 cm, E cup, long legs and a slim waist. She wears a white fitted ribbed scoop-neck tank mini dress that follows her full chest, slim waist and hips, and small gold hoop earrings; the dress is dry. Setting: a wide white-sand beach at sunset, calm shallow water and a soft gold and peach sky over the sea, the beach empty. One hand rests lightly at her collarbone and the other is relaxed at her side; she smiles brightly. Shot: a knee-up shot, from a little above her head down to her upper shins just below the knees, not cutting at the knee joint, showing the fitted ribbed tank dress over her full chest, slim waist and hips and her legs down to just below the knees, one hand at her collarbone and the other relaxed at her side. Body: standing at the water's edge with her weight on her back leg and her front knee softly bent, her body turned about 30 degrees toward camera-left, shoulders and hips turned together. Face and gaze: her face toward the camera, looking into the camera. Camera: vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.7 metres, camera at her hip height, tilted slightly upward, natural perspective without distortion. Composition: she stands slightly right of centre, the horizon low behind her hips and the gold and peach sunset sky filling the space above and to the left. Emphasis: the slightly low camera and low horizon make her tall figure look longer, and the oblique stance shows the healthy curve of her hips. Lighting: the low sun behind her draws a warm rim along her hair and shoulders; a large white reflector and a soft fill just out of frame in front light her face evenly; warm gold, peach and soft blue tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

## 9. 構圖與生成提案

| 款式 | 建議 |
|---|---|
| 橫式款（H） | 建議版面用「大照片」框（約 1.85:1）。生成用 16:9（工具支援；原生尺寸未知）：只需上下共裁約 4%。12 套的景別從腰上到全身、斜躺都有，見「攝影總覽」。 |
| 直式款（V） | 建議照片區至少 3:4。生成用 3:4（原生 1536×2048，已知）。12 套的景別從胸上到全身都有；全身與坐姿讓整套服裝看得到，近一點的景別放大胸腰比例。 |

**評估：**

- 橫式款的價值在於「人＋環境」的寬畫面：大照片框比半版適合。半版直幅框比較適合直式照片，而直式款已經另有 12 套直幅照片。
- 若 Penny 最後選擇橫式款用半版直幅框：這 12 套 16:9 不適用，要另外規劃與生成直幅版本——不從 16:9 硬裁成直幅。
- 直式款若最後用近方形框（約 0.94:1），3:4 要上下共裁約 20%：膝上變大腿以上、全身會切到腳。所以建議直式款的照片區至少 3:4。
- 避免人物縮小到背景裡：全身與坐姿的人物佔畫面高度約 85%（斜躺的 Rin 佔畫面寬度約 87%）；裁切景別保留完整髮頂、上緣約 4–10% 留白。

**限制：**

- 16:9 原生尺寸未知（推測 2048×1152，未驗證）；3:2 也未知。3:4 已知 1536×2048。
- 換算只做比例，不承諾 ppi，也不判斷線圈安全；廠商尺寸與印刷門檻還沒問。
- 外擴與 AI 放大不列為必要步驟。

換算方法：全片幅 36×24 mm。橫式款 16:9 取 36×20.25 mm，視野高＝20.25 mm×距離÷焦段；直式款 3:4 直拿裁成 24×32 mm，視野高＝32 mm×距離÷焦段。每套依景別算出畫面上下界、距離與畫面中心高度，再和相機高度比較得出平視／輕俯／輕仰；數字矛盾會讓建置失敗。焦段與距離只是參考，不是生成保證。

## 10. 費用（本輪不變；分開精確報價、歷史實扣、未知）

**狀態：** 仍未授權：沒有生成授權、沒有費用核准。下面的數字分成「精確報價」「歷史實扣」「未知」，情境試算不是預算。

**模型：** soul_2＋各人設既有 Soul，quality 2k，每次請求 1 張（count 1）；橫式款 16:9、直式款 3:4；不掛 Reference Element、不用參考圖。

### 10.1 精確報價（generate_image 的 get_cost 預檢，不送出工作）

| 設定 | 回傳 |
|---|---|
| soul_2＋Soul（Iris）、2k、3:4、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、2k、3:2、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、2k、2:3、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、1.5k、3:4、count 1 | credits 1／credits_exact 0.12 |
| soul_2、不帶 Soul、2k、3:4、count 1 | credits 1／credits_exact 0.12 |
| soul_2＋Soul（Iris）、2k、3:4、count 4 | credits 1／credits_exact 0.12（與 count 1 相同） |
| soul_2＋Soul（Iris）、2k、16:9、count 1（2026-10-13，本輪查詢） | credits 1／credits_exact 0.12 |

2026-10-13 用 generate_image 的 get_cost 預檢查詢 6 次（工具說明：只回傳費用、不送出工作）；查詢前後交易明細沒有新增任何一筆。回傳有兩個欄位：credits（整數顯示值 1）與 credits_exact（0.12）。不把 1 解讀成 0.12，也不把 0.12 當成已證實的實扣：0.12 與歷史 Soul V2 交易明細一致，但 3:2、2:3、1.5k 這幾種設定從沒有實扣紀錄。 本輪另查 16:9 一次，回傳相同；查詢前後交易明細沒有新增。

### 10.2 歷史實扣與紀錄

| 項目 | 數值 | 依據 | 等級 | 來源檔 |
|---|---|---|---|---|
| Soul V2 實際扣款（交易明細） | 每筆 −0.12 | Soul 訓練總報告（2026-09-08）：驗證圖 114 張約 13.7 credits，交易明細為重複的「Higgsfield Soul V2 −0.12」；驗證紀錄寫明「每 spec 只生一張」，所以是一次請求 1 張。這批的比例與畫質沒有寫在讀到的文件裡。 | 歷史實扣（交易明細） | `review/soul_training/FINAL_REPORT.md`、`review/soul_pilot/VERIFY_REMAINING_12.md` |
| 2026-10-13 帳號交易明細 | 今天也有 Soul V2 −0.12 的扣款 | 唯讀查詢 transactions：這些是帳號上其他人的工作，不是本案；只說明 Soul V2 目前仍以 −0.12 一筆扣款。 | 歷史實扣（他人工作，只作參考） |  |
| Iris 先前的 Soul 生成 | 費用未逐筆記錄 | Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 共 7 次生成成功、輸出 1536×2048，但沒有逐筆扣款。 | 無費用紀錄 | `kols/iris-chen/generation_notes.md` |
| 失敗也可能扣款 | 有紀錄 | Soul 訓練總報告的對帳判準：曾出現「重複的 Soul V2 −0.12 扣款但工作失敗」的情況（Vicky Lin 案例），所以重試也要算進上限。 | 歷史紀錄 | `review/soul_training/FINAL_REPORT.md` |

### 10.3 計價方式、張數、上限、異常

| 項目 | 說明 | 來源檔 |
|---|---|---|
| 計價單位 | 工具報價以「每次請求」回傳；count 4 的報價與 count 1 完全相同，所以無法判斷報價是每張還是每次請求。本案只用 count 1，不推算多張的費用。 |  |
| 每次請求產生幾張 | generate_image：count 1–4（同一 prompt 的變體）；generate_image_batch：最多 12 個請求、每個固定 1 張，而且批次不支援費用預檢。本案每次只送 1 個請求、count 1。 |  |
| 能不能限制總費用 | generate_image 與 generate_image_batch 都沒有「費用上限」參數（只有 AI Influencer 工具有，不適用）。只能靠流程控制：一次一個請求、每次之後查交易明細、累計達上限就停。餘額不能用來對帳——帳號同時有其他人在用。 |  |
| 異常扣款 | 原因未知。另一位人設的生成筆記記錄過三次「實扣高於預檢」：seedream_v4_5 4 張扣 50、seedream_v4_5 4 張扣 8、soul_2（不帶 Soul）4 張扣 2.16。三次都是用帳戶餘額前後相減算的，而帳號同時有其他人在用；沒有用交易明細逐筆核對，所以不能歸因，也不能排除。其中兩次是不同模型（seedream_v4_5）。 | `kols/sophia-tseng/generation_notes.md`、`review/soul_training/FINAL_REPORT.md` |

### 10.4 24 套獨立拍攝的情境試算（不是預算）

| 情境 | 請求數 | 依 credits_exact 報價 | 若實扣是顯示值（每次 1） |
|---|---|---|---|
| 每套 1 次請求 | 24 | 約 2.88 | 24 |
| 每套 2 次請求 | 48 | 約 5.76 | 48 |
| 每套 3 次請求 | 72 | 約 8.64 | 72 |

只是用今天的報價換算的情境，不是預算、不保證能做完幾張。「依 credits_exact」是工具的精確報價欄位；「若實扣是顯示值」是假設每次請求扣 1 credit 的上界情境。實扣是哪一個，要等第一張試拍用交易明細確認。失敗與重試都可能扣款。

**未知：** 16:9 與 3:2 的實際輸出像素、16:9、3:4 在這些企劃下的實際扣款（只有報價）、count 大於 1 時的費用、ready 狀態的 Soul 在逆光、夜景、室內暖光下的身分穩定度、24 套獨立造型各自需要幾次才能成功

### 10.5 Iris 首張試拍提案（只是提案）

**推薦：V-iris-chen**

- 直式 3:4 的原生尺寸已知（1536×2048）、報價已查，第一張只需要驗證「寫真質感、身分、身材與實際扣款」，少一個未知數。
- 直幅大腿中段以上最能看清 Penny 這次指定的穿搭與姿態：更顯身材的上衣＋牛仔迷你裙、身體面向鏡頭、笑容。
- 保留她喜歡的 iris-04 草地夕陽氛圍，又是全組最難的逆光，先驗證補光是否足夠。
- 橫式款（H-iris-chen，16:9 原生尺寸未知）放在之後，等第一張結果與費用確認再測。

| 項目 | 內容 |
|---|---|
| 範圍 | 只做 1 張：V-iris-chen 的 prompt 草稿（本頁「prompt 草稿」原文，不沿用上一輪被 Penny 修改的 Iris prompt）。 |
| 設定 | soul_2＋Iris 既有 Soul、quality 2k、aspect 3:4、count 1、不掛參考圖；use_unlim 設為 false（用 credits 付費；查詢時帳號沒有可用的免費額度）。 |
| 報價 | 今天的預檢：credits 1／credits_exact 0.12；實扣未確認。 |
| 重試 | 不自動重試。無論結果好壞、成功或失敗，都先停下回報。 |
| 對帳 | 送出前後各查一次交易明細，記錄這一張的實際扣款；不用餘額對帳（帳號有他人同時使用）。 |
| 前提 | 需要 Penny 核定這套造型與費用，再由主管另發 M-4 指令；本輪什麼都不送出。 |

**授權：** 本輪沒有任何花費授權。任何試拍都要 Penny 批准，再由主管另發 M-4 指令。

## 11. 要請 Penny 決定的事（本輪不新增題目）

1. 24 套企劃：每套選「接受」或「想修改」，想修改的寫在備註。未回覆不算接受。
2. 兩本月份推薦（橫式款、直式款）：接受，或想怎麼調。
3. 版面與構圖建議（橫式款用大照片框＋16:9；直式款照片區至少 3:4）：接受，或想改。
4. Iris 首張試拍候選：建議先試 V-iris-chen（只是候選；生成與費用仍要另外核定）。
5. 已接受方向的 H／V 分配（Somi、Rainie 放橫式款；Coco、Rin 放直式款）：接受，或想對調。

## 12. 共同的皮膚與質感句（每段 prompt 結尾都加）

```text
Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```
