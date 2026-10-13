TASK-CAL-001／M-3／R2｜24套雙款獨立寫真企劃｜送審報告

# CAL_18 — M-3 24 套雙款獨立寫真企劃（shoot-plan-v3）

> 資料檔：`data/cal_m3_shoot_plan.json`（shoot-plan-v3，R2，2026-10-13）。本文件由 `tools/build_cal_m3_plan_doc.py` 產生，內容以資料檔為準。
> **僅規劃：沒有生成任何圖片（含測試圖、示意圖），沒有花 credits，沒有上傳，沒有訓練，沒有改 canon 或 Soul ID。** 本輪生成數 0、credits 0、訓練數 0。
> 這是企劃，不是核准：24 套內容、月份、版面與 H／V 分配都待 Penny 拍板；生成與費用都未授權。Owner 決策逐字紀錄見 `CAL_19_M3_R2_OWNER_DECISION.md`。

## 0. 版本

| 項目 | 內容 |
|---|---|
| 名單 | roster-v1（docs/calendar/data/cal_m1_owner_roster.json）；不換人 |
| 上一版企劃 | shoot-plan-v2（commit `792d4f4e23ebb85dc10f6b1ebc392c1e35b86e07`） |
| 這一版 | 依 Penny 決定改成 24 套雙款獨立企劃；撤回「同造型橫直各一張」與「同圖兩款裁切」主策略。 |
| 素材頁版本 | `b8108eb648a46a57e3bb4dc2158cf878c23d7963` |
| 桌曆基準 | `4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45` |

**參考照片：** 參考照片都是既有照片，只按標示的用途參考（表情／場景／服裝材質／身分），不是新企劃的成品，也不會照抄；身材一律以設定數字為準。

## 1. Penny 回饋落實表

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

## 2. 橫式款 12 套總覽

| 月份（推薦） | ID | 主題 | 環境 | 服裝 | 色彩 | 姿態 | 表情 | 性感程度 | 攝影方法 | 景別 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 月 | H-yuna-kim | 明亮通透的感性咖啡館，奶油黃短版開襟配淺藍緞面中長裙，坐在窗邊的清透美感。 | 明亮咖啡館（室內） | 上身：奶油黃貼身短版針織開襟（當上衣扣起，柔和 V 領）；下身：淺藍緞面斜裁中長裙；鞋：白色尖頭平底鞋；配件：耳上紅色櫻桃髮夾 | 奶油黃・淺藍・奶油白 | 坐在轉向鏡頭的咖啡椅上，雙腿在膝上交疊。一手放在桌緣，一手放在膝上。 | 平靜柔和的微笑 | 低 | 明亮漫射窗光、略偏亮的通透曝光 | 坐姿全身（16:9） |
| 2 月 | H-rin-ayase | 夕陽中的高樓飯店套房，酒紅緞面垂墜領細肩長洋裝，斜躺在深綠絲絨貴妃椅上。 | 飯店套房（室內夕陽） | 洋裝：深酒紅真絲緞面垂墜領細肩中長洋裝；鞋：赤腳；配件：細金鍊項鍊、金色小耳針 | 酒紅・深綠・柔金 | 面向鏡頭斜躺在貴妃椅上，用一邊手肘撐著。一手撐在手肘下，一手放在臀側。 | 平靜、心照不宣的半笑 | 高 | 夕陽窗光＋柔光補光 | 斜躺全身（16:9） |
| 3 月 | H-miu-shiraishi | 一人公寓的早晨，象牙白蕾絲緞面細肩小可愛與短褲，坐在床邊歪頭甜笑。 | 一人公寓（室內早晨） | 上身：象牙白緞面細肩小可愛（細蕾絲滾邊）；下身：同色緞面短褲；鞋：赤腳；配件：細金耳針、細金手鍊 | 象牙白・奶油・暖木 | 面向鏡頭坐在床邊，雙膝併攏、略偏向一側。雙手撐在身旁的床上。 | 歪頭、柔和的甜笑 | 高 | 紗簾晨光＋反光 | 坐姿全身（16:9） |
| 4 月 | H-tammy-chou | 高級精品店裡，熱粉色貼身針織洋裝配白色露跟高跟鞋，站在展示櫃旁的明亮笑容。 | 精品店（室內） | 洋裝：熱粉色方領羅紋針織貼身迷你洋裝（保留 Penny 同意的方向）；鞋：白色尖頭露跟高跟鞋；配件：手臂掛小型白色硬挺素面手提包、金色圈耳環 | 熱粉・奶油・大理石白・柔金 | 正面站在玻璃展示櫃旁，重心在一隻腳。一手放在展示櫃上，一手插腰。 | 明亮的笑容 | 中 | 柔光主光＋展示櫃投射燈 | 膝上（16:9） |
| 5 月 | H-yerin-han | 春天早晨的球場，白色無袖針織 polo 配淺藍百褶高爾夫迷你裙，坐在白色球車上的可愛笑容。 | 高爾夫球場（戶外） | 上身：白色無袖貼身針織高爾夫 polo；下身：淺天空藍百褶高爾夫迷你裙；鞋：白色高爾夫鞋；配件：素面白色球帽、小金色耳針 | 亮綠・天空藍・白 | 側坐在球車前座、身體面向鏡頭，雙腿伸出車外、在腳踝交叉。一手搭在椅背上，一手放在膝上。 | 明亮可愛的笑 | 中 | 晴朗晨光＋反光板 | 坐姿全身（16:9） |
| 6 月 | H-coco-wu | 初夏傍晚的薰衣草花田，白色細肩亞麻洋裝，拿著草帽大笑。 | 花田（戶外） | 洋裝：白色亞麻細肩洋裝，抓皺貼身上身、柔和 V 領、收腰、微蓬迷你裙；鞋：白色平底涼鞋；配件：白色雛菊髮夾、腳踝細金鍊、草帽（拿在手上） | 薰衣草紫・白・暖金 | 正面站在花壟之間。一手把草帽拿在身側，一手把頭髮塞到耳後。 | 瞇眼大笑、深酒窩 | 中 | 傍晚逆光＋反光板 | 膝上（16:9） |
| 7 月 | H-mia-huang | 夏日黃昏的海邊遊樂碼頭，粉色緞面馬甲上衣配白色迷你裙，拿著棉花糖俏皮眨眼。 | 海邊遊樂碼頭（戶外黃昏） | 上身：粉色緞面馬甲上衣（心形領）；下身：白色高腰 A 字迷你裙；鞋：白色厚底涼鞋；配件：小珍珠耳環、細銀手鍊、一支粉色棉花糖 | 棉花糖粉・薰衣草紫・柔金 | 正面站在木棧道上。一手插腰，一手把棉花糖拿在肩高、離開臉。 | 俏皮眨眼、挑逗的半笑 | 中 | 黃昏天光＋柔光主光 | 膝上（16:9） |
| 8 月 | H-iris-chen | 午後紅磚騎樓裡，穿米杏色針織套裝的 Iris 正面站定、對鏡頭笑。 | 城市老街（戶外） | 上身：米杏色貼身羅紋針織平口上衣；下身：同色高腰針織迷你裙（套裝）；鞋：米色厚底繫帶涼鞋；配件：細金鍊項鍊 | 紅磚・米杏・暖灰 | 正面站在磚柱旁，重心在左腳。一手輕扶肩高的磚柱，一手插腰。 | 溫暖的笑容 | 中 | 側面午後光＋反光板 | 膝上（16:9） |
| 9 月 | H-jia-seo | 現代美術館的白色展廳，黑色單肩貼身中長洋裝帶腰側鏤空，冷靜站在畫作之間。 | 美術館（室內） | 洋裝：黑色單肩貼身中長洋裝，腰側一小塊鏤空；鞋：黑色細帶高跟鞋；配件：小銀色圈耳環 | 黑・白・灰・薄荷 | 正面站在展廳中央，重心在一隻腳。一手放在腰側，一手自然垂放。 | 冷靜自信的半笑 | 中 | 天窗冷光＋柔光主光 | 膝上（16:9） |
| 10 月 | H-luna-tanaka | 清晨的京都町家和室，象牙白蕾絲緞面細肩洋裝，席地而坐的安靜微笑。 | 和室（室內） | 洋裝：象牙白真絲細肩洋裝，細蕾絲滾邊、貼身上身、裙長大腿中段；鞋：赤腳（室內）；配件：細金鍊項鍊、耳上珍珠髮夾 | 柔白・暖木・淡粉 | 在榻榻米上側坐、雙腿收在一側，身體面向鏡頭。兩手輕放在大腿上。 | 安靜的淺笑 | 中高 | 紙門柔光＋反光卡 | 席地坐姿全身（16:9） |
| 11 月 | H-somi-oh | Penny 已接受的方向：暖橘復古小吃店棚景，針織短開襟＋高腰針織短裙，輕靠吧台大笑。 | 復古小吃店棚景（棚內） | 上身：奶油色合身羅紋針織短開襟（扣起）；下身：高腰鏽橘色針織迷你裙；鞋：棕色有跟皮革樂福鞋；配件：紅色琺瑯小愛心耳環 | 暖橘・奶油・紅 | 站著，一側臀部輕靠磁磚吧台，重心在後腳、前腳輕交叉。一手放在吧台邊緣，一手把頭髮塞到耳後。 | 月牙眼大笑、露出酒窩 | 中 | 暖色柔光箱棚拍 | 膝上（16:9） |
| 12 月 | H-rainie-hsu | Penny 已接受的方向：頂樓夜景，血紅緞面馬甲高衩迷你洋裝，背靠玻璃欄杆直視鏡頭。 | 頂樓露台（戶外夜晚） | 洋裝：血紅緞面馬甲迷你洋裝（大腿高衩）；鞋：黑色細帶高跟涼鞋；配件：大型銀色垂墜耳環、細銀手環 | 血紅・黑・銀・深藍 | 背靠玻璃欄杆，一腳從高衩往前。雙手放在身後的欄杆上；不拿任何杯子。 | 自信又帶點壞的笑 | 高 | 夜景柔光箱主光＋城市散景 | 膝上（16:9） |

## 3. 直式款 12 套總覽

| 月份（推薦） | ID | 主題 | 環境 | 服裝 | 色彩 | 姿態 | 表情 | 性感程度 | 攝影方法 | 景別 |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 月 | V-tammy-chou | 夜晚的大飯店大廳，白色西裝外套洋裝配黑色細跟鞋，雙手插腰的自信全身照。 | 飯店大廳（室內夜晚） | 洋裝：白色合身西裝外套式迷你洋裝（深 V 翻領、金色扣子、繫腰帶）；鞋：黑色尖頭細高跟鞋；配件：金色垂墜耳環 | 白・金・暖大理石 | 正面站在大理石柱旁，一腳略往前。雙手插腰。 | 自信的笑容 | 中 | 吊燈環境光＋柔光主光 | 全身（3:4） |
| 2 月 | V-jia-seo | 明亮的玻璃溫室，白色無袖立領短上衣配薄荷綠緞面開衩中長裙，站在大葉植物之間。 | 玻璃溫室（室內實景） | 上身：白色無袖立領貼身短上衣（露腰）；下身：高腰薄荷鼠尾草綠緞面中長裙（側開衩）；鞋：白色細帶涼鞋；配件：細銀耳針 | 白・薄荷・深綠 | 正面站在植物之間的石板路上。一手輕觸身旁的大片龜背芋葉，一手插腰。 | 冷靜柔和的微笑 | 中 | 溫室漫射天光＋柔光 | 膝上（3:4） |
| 3 月 | V-mia-huang | 春夜的櫻花河岸步道，淺紫貼身露肩針織洋裝，站在花枝下甜笑。 | 櫻花河岸（戶外夜晚） | 洋裝：淺紫細針織貼身露肩迷你洋裝；鞋：白色及膝長靴；配件：一側小珍珠髮夾、細銀耳環 | 粉櫻・淺紫・夜藍 | 正面站在低垂的花枝下。一手輕觸肩旁的花枝，一手自然垂放。 | 甜甜的微笑 | 中 | 夜景柔光主光＋燈籠 | 膝上（3:4） |
| 4 月 | V-miu-shiraishi | 暮春的運河步道，奶油色 V 領合身針織洋裝繫細腰帶，靠著欄杆甜笑。 | 運河步道（戶外） | 洋裝：奶油色 V 領細羅紋合身針織迷你洋裝（前排小扣、細棕色腰帶）；鞋：奶油色繫踝低跟鞋；配件：細金耳針 | 奶油・新綠・淺棕 | 正面站在欄杆旁，重心在一隻腳。一手扶著欄杆，一手輕輕拿著臉旁的一縷頭髮。 | 甜甜的微笑 | 中 | 陰天柔光＋反光板 | 膝上（3:4） |
| 5 月 | V-rainie-hsu | 雨後的夜晚街道，黑色緞面繞頸迷你洋裝外搭黑色長皮風衣，站在濕亮的路面上直視鏡頭。 | 雨後夜街（戶外夜晚） | 洋裝：黑色緞面繞頸迷你洋裝；外套：黑色長版皮革風衣（敞開）；鞋：黑色細跟尖頭短靴；配件：大型銀色垂墜耳環 | 黑・銀・深藍・琥珀 | 正面站在濕亮的人行道上，重心在一隻腳。一手拉著敞開的風衣衣襟在腰間，一手自然垂放。 | 自信、帶點壞的笑 | 中高 | 夜景柔光主光＋濕路面倒影 | 膝上（3:4） |
| 6 月 | V-luna-tanaka | 紫陽花盛開的町家庭院，鼠尾草綠馬甲感洋裝，正面站在石板路上。 | 町家庭院（戶外） | 洋裝：淺鼠尾草綠棉質洋裝，心形領、有骨架的貼身上身、微蓬迷你裙；鞋：米色低跟繫帶涼鞋；配件：細金手鍊 | 鼠尾草綠・白・青苔綠 | 正面站在石板路上，重心在一隻腳。雙手輕輕交握在身後。 | 溫柔的微笑 | 中 | 陰天柔光＋反光板 | 全身（3:4） |
| 7 月 | V-coco-wu | Penny 已接受的方向：週末飯店泳池，薄荷綠比基尼＋淺紫透膚罩衫，坐在池邊大笑。 | 飯店泳池（戶外） | 泳裝：薄荷綠羅紋三角比基尼上衣與同色側綁下著（完整遮蔽）；外搭：敞開的淺紫透膚短袖罩衫（落在肩後）；配件：白色雛菊髮夾、腳踝細金鍊 | 薄荷綠・淺紫・湖水綠 | 坐在池邊、兩條小腿泡在水裡，身體往後。雙手撐在身後地上。 | 歪頭、瞇眼大笑、酒窩 | 高 | 晴天高光＋反光板 | 坐姿到水面（3:4） |
| 8 月 | V-yerin-han | 日落的白沙海灘，白色圓領貼身針織背心洋裝，赤腳站在淺浪邊的燦笑。 | 海灘夕陽（戶外） | 洋裝：白色圓領羅紋貼身背心迷你洋裝；鞋：赤腳；配件：小金色圈耳環、腳踝細金鍊 | 暖金・蜜桃・白・淡藍 | 正面站在浪花邊的淺水裡，重心在一隻腳。一手輕放在鎖骨，一手自然垂放。 | 大方燦爛的笑 | 中 | 夕陽逆光＋反光板 | 膝上（3:4） |
| 9 月 | V-iris-chen | 黃金時段的河濱草地，白色方領短上衣配牛仔迷你裙，正面站著甜笑（Penny 指定的穿搭）。 | 河濱草地（戶外） | 上身：白色貼身羅紋方領短袖短上衣（露腰）；下身：淺藍高腰牛仔迷你裙；鞋：白色低筒帆布鞋；配件：小金色圈耳環 | 米白・淺牛仔藍・暖金 | 身體正面朝鏡頭站著，重心在一隻腳、另一膝放鬆。一手插腰，一手輕碰太陽穴旁的頭髮。 | 明亮溫暖的笑 | 中 | 黃金時段逆光＋反光板 | 膝上（3:4） |
| 10 月 | V-rin-ayase | Penny 採用的 v2 替代方向：出勤前的銀座，黑色絲絨細肩帶長禮服，坐在金色燈光的吧台邊（不拿酒杯）。 | 會員制酒吧（室內夜晚） | 洋裝：黑色絲絨細肩帶及地長禮服（貼身上身）；鞋：黑色細帶高跟鞋；配件：小金色垂墜耳環、細金手鍊 | 黑・金・深木 | 坐在高腳椅上、身體轉向鏡頭，雙腿交疊。一手手肘靠在吧台上，一手放在膝上；手上不拿杯子。 | 平靜、端莊的微笑 | 中 | 金色吊燈＋柔光主光 | 坐姿全身（3:4） |
| 11 月 | V-yuna-kim | 深秋的銀杏大道，奶油色毛呢短外套套裝配黑色長靴，站在落葉上的韓劇感街拍寫真。 | 銀杏大道（戶外） | 上身：奶油色毛呢短外套（無領、扣起、合身）；下身：同色高腰毛呢迷你裙；鞋：黑色及膝皮長靴；配件：小珍珠耳環、小黑色肩背包 | 銀杏金黃・奶油・黑 | 正面站在落葉人行道上，重心在一隻腳。一手拉著肩上的包包背帶，一手自然垂放。 | 頭微傾、柔和的微笑 | 低中 | 午後逆光＋反光板 | 全身（3:4） |
| 12 月 | V-somi-oh | 下雪的溫泉小鎮夜晚，象牙白貼身針織洋裝外披紅色長大衣，在燈籠光裡大笑。 | 溫泉小鎮雪夜（戶外） | 洋裝：象牙白貼身羅紋針織迷你洋裝（高圓領）；外套：紅色羊毛長大衣（敞開）；鞋：白色及膝長靴；配件：小珍珠耳環 | 紅・象牙白・燈籠琥珀・雪夜藍 | 正面站在雪地上，重心在一隻腳。雙手插在敞開的大衣口袋裡，把大衣往後撐開。 | 月牙眼大笑、露出酒窩 | 低中 | 夜景暖色主光＋燈籠 | 膝上（3:4） |

## 4. 兩本月份推薦（待 Penny 拍板）

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

## 5. 24 套企劃

### 5.1 H-iris-chen｜Iris｜橫式款（新企劃）

**一句話：** 午後紅磚騎樓裡，穿米杏色針織套裝的 Iris 正面站定、對鏡頭笑。

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
| 姿態 | 正面站在磚柱旁，重心在左腳。 |
| 手的位置 | 一手輕扶肩高的磚柱，一手插腰。 |
| 表情 | 溫暖的笑容 |
| 視線 | 直視鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 86%；頭頂完整、雙手在框內，切在膝蓋下方；人物偏左，右側約四到五成給場景 |
| 焦段／距離／視野 | 16:9，70mm，約 4.9 公尺，視野 2.52×1.42 公尺 |
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
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a round sweet face with large bright double-eyelid eyes and full lips, black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, a full chest, a slim waist and rounded hips. She wears a fitted dusty-beige ribbed knit tube top and a matching high-waisted knit mini skirt, beige strappy platform sandals and a thin gold chain necklace. Setting: an old red-brick arcade walkway on a historic Taipei shopping street in the afternoon, a row of arched brick pillars, closed wooden shopfront doors, the walkway empty and clean. She stands facing the camera beside one of the brick pillars, weight on her left leg, one hand resting lightly on the pillar at shoulder height and the other on her hip, smiling warmly at the camera. Horizontal 16:9 frame, full-frame camera with a 70mm lens from about 4.9 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 86% of the frame height, standing left of centre with the arched brick arcade receding to the right. Lighting: warm afternoon sunlight enters from the open side of the arcade and lays soft shafts of light across the floor and her body; a large white reflector just out of frame fills her face evenly; warm brick, beige and soft grey tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.2 H-luna-tanaka｜Luna｜橫式款（新企劃）

**一句話：** 清晨的京都町家和室，象牙白蕾絲緞面細肩洋裝，席地而坐的安靜微笑。

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
| 姿態 | 在榻榻米上側坐、雙腿收在一側，身體面向鏡頭。 |
| 手的位置 | 兩手輕放在大腿上。 |
| 表情 | 安靜的淺笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 席地坐姿全身；人物約佔畫面高度 85%；席地坐姿完整，雙手在框內；人物偏右，左側約四到五成給場景 |
| 焦段／距離／視野 | 16:9，50mm，約 2.5 公尺，視野 1.8×1.01 公尺 |
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
A 20-year-old adult Japanese woman with her natural fair skin tone, large round dark-brown eyes and soft natural makeup with a rosy lip, black fine straight hair in a centre-parted, chin-length bob. Petite figure with a noticeably full chest and a slim waist, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup. She wears an ivory silk slip dress with fine lace trim, thin straps and a fitted bodice that follows her full chest and slim waist, the hem at mid-thigh, a thin gold chain necklace and a pearl hair pin above one ear; her feet are bare. Setting: a quiet tatami room in an old Kyoto-style townhouse in the morning, paper shoji screens along one wall, a low wooden table with a small vase of white flowers, the room tidy. She sits on the tatami with her legs folded to one side and her body facing the camera, both hands resting lightly on her lap, looking at the camera with a small, quiet smile. Horizontal 16:9 frame, full-frame camera with a 50mm lens from about 2.5 metres, camera at her seated chest height; her whole seated figure from the floor to a little above her head, she fills about 85% of the frame height, right of centre with the shoji screens and low table on the left. Lighting: soft morning daylight diffused through the shoji screens from camera-left as a large gentle key, a white bounce card just out of frame on the right keeping her face clear; soft white, warm wood and pale blush tones with a gentle film-like softness. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.3 H-somi-oh｜Somi｜橫式款（Penny 已接受的 v2 主方向）

**一句話：** Penny 已接受的方向：暖橘復古小吃店棚景，針織短開襟＋高腰針織短裙，輕靠吧台大笑。

| 項目 | 內容 |
|---|---|
| 場景 | 搭景的韓式復古小吃店：暖橘色磁磚吧台、一排紅色皮面高腳椅、一盞暖色吊燈；橫幅右緣有一小盤失焦的炸雞。 |
| 服裝 | 上身：奶油色合身羅紋針織短開襟（扣起）；下身：高腰鏽橘色針織迷你裙；鞋：棕色有跟皮革樂福鞋；配件：紅色琺瑯小愛心耳環 |
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
| 景別與人物佔比 | 膝上；人物約佔畫面高度 85%；頭頂完整、雙手在框內，切在膝蓋下方；人物偏左，右側約四到五成給場景 |
| 焦段／距離／視野 | 16:9，70mm，約 4.9 公尺，視野 2.52×1.42 公尺 |
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
A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a fitted cream rib-knit cropped cardigan buttoned up, a high-waisted rust-orange knit mini skirt, brown leather heeled loafers and small red enamel heart earrings. Setting: a studio-built retro Korean snack-bar set with a warm orange tiled counter, a row of red vinyl bar stools and a warm pendant lamp, everything tidy. She stands leaning one hip lightly against the tiled counter, weight on her back leg with the front leg crossed in front, one hand resting on the counter edge and the other tucking her hair behind her ear, laughing openly at the camera with her eyes curved into crescents and dimples showing. Horizontal 16:9 frame, full-frame camera with a 70mm lens from about 4.9 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 85% of the frame height, left of centre with the orange counter running to the right and a small plate of golden fried chicken resting soft and out of focus at the right edge. Lighting: a large warm softbox key from the front right at head height and a soft fill from the left just out of frame light her face evenly; the pendant lamp adds a warm glow on her hair; warm orange and cream tones throughout. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.4 H-coco-wu｜Coco｜橫式款（新企劃）

**一句話：** 初夏傍晚的薰衣草花田，白色細肩亞麻洋裝，拿著草帽大笑。

| 項目 | 內容 |
|---|---|
| 場景 | 初夏傍晚一大片薰衣草花田，紫色花壟延伸到遠方，地平線上幾棵柔綠樹，花田裡沒有其他人。 |
| 服裝 | 洋裝：白色亞麻細肩洋裝，抓皺貼身上身、柔和 V 領、收腰、微蓬迷你裙；鞋：白色平底涼鞋；配件：白色雛菊髮夾、腳踝細金鍊、草帽（拿在手上） |
| 髮型 | 深棕長波浪捲髮、蓬鬆空氣瀏海。 |
| 妝感 | 甜美淡妝、粉色唇。 |
| 身材設定（數字） | 158 cm／89-56-86／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 抓皺貼身上身與 V 領呈現 E 罩杯胸型，收腰線清楚；迷你裙長露出腿。 |
| 主光 | 她身後的低角度傍晚陽光，頭髮與肩膀暖色輪廓光 |
| 補光 | 畫面外前方大反光板與柔光 |
| 姿態 | 正面站在花壟之間。 |
| 手的位置 | 一手把草帽拿在身側，一手把頭髮塞到耳後。 |
| 表情 | 瞇眼大笑、深酒窩 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 84%；頭頂完整、雙手在框內，切在膝蓋下方；人物偏左，右側約四到五成給場景 |
| 焦段／距離／視野 | 16:9，85mm，約 5.9 公尺，視野 2.5×1.41 公尺 |
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
A 20-year-old adult Taiwanese woman with her natural fair skin tone, a doll-like round face with big sweet eyes and deep dimples when she smiles, dark-brown long wavy hair with soft wispy bangs. Petite curvy figure, 158 cm tall, bust 89 cm, waist 56 cm, hips 86 cm, E cup, full chest and slim waist. She wears a white linen sundress with thin straps, a fitted ruched bodice with a soft V neckline that shapes her full chest, a cinched waist and a flared mini skirt, white flat sandals, a white daisy hair clip and a thin gold anklet. Setting: a wide lavender field in early summer in the late afternoon, long purple rows running into the distance, a few soft green trees on the horizon, the field empty. She stands between the lavender rows facing the camera, holding a straw sun hat loosely at her side with one hand and tucking her hair behind her ear with the other, laughing with her eyes squeezed into crescents and deep dimples showing. Horizontal 16:9 frame, full-frame camera with an 85mm lens from about 5.9 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 84% of the frame height, left of centre with the lavender rows running away to the right. Lighting: the low late-afternoon sun behind her draws a warm rim along her hair and shoulders; a large white reflector and a soft fill just out of frame light her face evenly; soft lilac, white and warm gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.5 H-mia-huang｜Mia｜橫式款（新企劃）

**一句話：** 夏日黃昏的海邊遊樂碼頭，粉色緞面馬甲上衣配白色迷你裙，拿著棉花糖俏皮眨眼。

| 項目 | 內容 |
|---|---|
| 場景 | 夏天黃昏的海邊遊樂碼頭：遠處亮燈的摩天輪與串燈化成柔和光點、粉紫色晚霞映在海上，木棧道上沒有其他人。 |
| 服裝 | 上身：粉色緞面馬甲上衣（心形領）；下身：白色高腰 A 字迷你裙；鞋：白色厚底涼鞋；配件：小珍珠耳環、細銀手鍊、一支粉色棉花糖 |
| 髮型 | 灰棕色長髮鬆散大波浪，左側臉旁粉紅 money piece 挑染。 |
| 妝感 | 柔和動漫感眼妝、上揚眼線、圓形腮紅、水光唇。 |
| 身材設定（數字） | 160 cm／91-57-88／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 心形領馬甲上衣塑出 F 罩杯胸型與細腰；高腰 A 字短裙讓腰臀比與腿長清楚。 |
| 主光 | 畫面外右前方的大型柔光，臉乾淨、膚色自然明亮 |
| 補光 | 黃昏天光與遠處遊樂設施的粉紫光點只當背景色 |
| 姿態 | 正面站在木棧道上。 |
| 手的位置 | 一手插腰，一手把棉花糖拿在肩高、離開臉。 |
| 表情 | 俏皮眨眼、挑逗的半笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 85%；頭頂完整、雙手在框內，切在膝蓋下方；人物偏左，右側約四到五成給場景 |
| 焦段／距離／視野 | 16:9，70mm，約 4.9 公尺，視野 2.52×1.42 公尺 |
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
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a soft round face with big expressive eyes, softly winged liner, rounded blush and glossy tinted lips, long ash-brown hair in loose waves with a pastel-pink money-piece highlight framing the left side of her face. Curvy figure, 160 cm tall, bust 91 cm, waist 57 cm, hips 88 cm, F cup, a full chest and a slim waist. She wears a pastel-pink satin corset top with a sweetheart neckline that shapes her full chest and slim waist, a white high-waisted A-line mini skirt, white platform sandals, small pearl earrings and a thin silver bracelet. Setting: a seaside amusement pier at dusk in summer, a lit Ferris wheel and string lights far behind her softening into bokeh, a pink and lavender sunset sky over the sea, the wooden boardwalk empty. She stands on the boardwalk facing the camera, one hand on her hip and the other holding a small pink cotton candy at shoulder height away from her face, giving a playful wink with a teasing half-smile. Horizontal 16:9 frame, full-frame camera with a 70mm lens from about 4.9 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 85% of the frame height, left of centre with the Ferris wheel bokeh and sunset sea on the right. Lighting: a large soft key light from front-right just out of frame lights her face cleanly with natural, bright skin tones; the dusk sky and the distant ride lights add pink and lavender colour behind her; cotton-candy pink, lavender and soft gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.6 H-yuna-kim｜Yuna｜橫式款（新企劃）

**一句話：** 明亮通透的感性咖啡館，奶油黃短版開襟配淺藍緞面中長裙，坐在窗邊的清透美感。

| 項目 | 內容 |
|---|---|
| 場景 | 明亮的極簡咖啡館：大片窗戶與白紗、淺木桌、奶油色牆面、玻璃瓶裡一朵白色鬱金香，店內沒有其他人。 |
| 服裝 | 上身：奶油黃貼身短版針織開襟（當上衣扣起，柔和 V 領）；下身：淺藍緞面斜裁中長裙；鞋：白色尖頭平底鞋；配件：耳上紅色櫻桃髮夾 |
| 髮型 | 深棕自然波浪、鎖骨長度、空氣感八字瀏海。 |
| 妝感 | 水光肌、眼妝為重點、珊瑚漸層唇。 |
| 身材設定（數字） | 168 cm／84-58-89／C（纖細長腿） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 短版開襟收在腰上、緞面裙貼著腰臀，呈現她纖細的腰與長腿比例（C 罩杯、偏纖細，不寫成豐滿）。 |
| 主光 | 大窗透進的明亮漫射日光（背後與側面） |
| 補光 | 畫面外前方柔光；曝光略偏亮、通透 |
| 姿態 | 坐在轉向鏡頭的咖啡椅上，雙腿在膝上交疊。 |
| 手的位置 | 一手放在桌緣，一手放在膝上。 |
| 表情 | 平靜柔和的微笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 坐姿全身；人物約佔畫面高度 86%；坐姿頭頂到腳完整，雙手在框內；人物偏右，左側約四到五成給場景 |
| 焦段／距離／視野 | 16:9，50mm，約 3.8 公尺，視野 2.74×1.54 公尺 |
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
A 21-year-old adult Korean woman with her natural fair skin tone, large bright double-eyelid eyes as the focus of her makeup, a dewy glass-skin finish and soft coral gradient lips, dark-brown natural wavy hair at collarbone length with airy curtain bangs. Slim, long-legged figure, 168 cm tall, bust 84 cm, waist 58 cm, hips 89 cm, C cup, a narrow waist and long legs. She wears a soft butter-yellow fitted cropped cardigan buttoned as a top with a gentle V neckline, a pale-blue satin bias-cut midi skirt that follows her waist and hips, white pointed flats and a small red cherry hair clip above one ear. Setting: a bright minimalist café with large windows and sheer white curtains, pale wood tables, cream walls and a glass vase with a single white tulip, the room empty and calm. She sits on a café chair turned toward the camera with her legs crossed at the knee, one hand resting on the table edge and the other on her knee, looking at the camera with a calm, soft smile. Horizontal 16:9 frame, full-frame camera with a 50mm lens from about 3.8 metres, camera at her seated chest height; full length seated, from her flats to a little above her head, she fills about 86% of the frame height, right of centre with the bright windows and curtains on the left. Lighting: bright diffused daylight from the large windows behind and to the side, a soft fill just out of frame in front; an airy, slightly bright exposure with clean cream, butter-yellow and pale-blue tones, a soft fashion-lookbook mood. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.7 H-tammy-chou｜Tammy｜橫式款（新企劃）

**一句話：** 高級精品店裡，熱粉色貼身針織洋裝配白色露跟高跟鞋，站在展示櫃旁的明亮笑容。

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
| 姿態 | 正面站在玻璃展示櫃旁，重心在一隻腳。 |
| 手的位置 | 一手放在展示櫃上，一手插腰。 |
| 表情 | 明亮的笑容 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 85%；頭頂完整、雙手在框內，切在膝蓋下方；人物偏左，右側約四到五成給場景 |
| 焦段／距離／視野 | 16:9，50mm，約 3.5 公尺，視野 2.52×1.42 公尺 |
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
A 24-year-old adult Taiwanese woman with her natural fair skin tone, round almond eyes with visible aegyo-sal, shimmer eyeshadow and jelly-glossy lips, long voluminous big-wave hair in milk-tea golden brown with light money-piece highlights at the front. Curvy figure, 160 cm tall, bust 90 cm, waist 57 cm, hips 89 cm, E cup, a full chest and a slim waist. She wears a fitted hot-pink square-neck rib-knit mini dress that follows her full chest, slim waist and hips, white pointed slingback heels, a small structured plain white handbag on her arm and gold hoop earrings. Setting: an upscale fashion boutique with pale marble floors, cream walls and softly lit glass display shelves holding plain leather handbags without any logos, a low velvet bench, the boutique empty. She stands beside a glass display counter facing the camera, weight on one leg, one hand resting on the counter and the other on her hip, smiling brightly at the camera. Horizontal 16:9 frame, full-frame camera with a 50mm lens from about 3.5 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 85% of the frame height, left of centre with the glowing display shelves on the right. Lighting: a large soft key light from front-left just out of frame lights her face evenly while warm display spotlights glow on the shelves behind her; hot pink against cream, marble white and soft gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.8 H-rin-ayase｜Rin｜橫式款（新企劃）

**一句話：** 夕陽中的高樓飯店套房，酒紅緞面垂墜領細肩長洋裝，斜躺在深綠絲絨貴妃椅上。

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
| 姿態 | 面向鏡頭斜躺在貴妃椅上，用一邊手肘撐著。 |
| 手的位置 | 一手撐在手肘下，一手放在臀側。 |
| 表情 | 平靜、心照不宣的半笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 斜躺全身；人物約佔畫面寬度 87%；斜躺全身完整，雙手在框內；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 16:9，50mm，約 2.6 公尺，視野 1.87×1.05 公尺 |
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
A 25-year-old adult Japanese woman with her natural fair, cool-toned skin, an oval face with long narrow eyes and a straight nose, a clean base with precise eyeliner and a muted rose-red lip, long deep wine-red brown hair styled in soft big waves over one shoulder. Curvy figure, 166 cm tall, bust 92 cm, waist 58 cm, hips 90 cm, F cup, a full chest, a slim waist and long legs. She wears a deep wine-red silk satin cowl-neck slip midi dress with thin straps that drapes over her full chest and slim waist, a thin gold chain necklace and small gold stud earrings; her feet are bare. Setting: a luxury hotel suite at sunset, a deep green velvet chaise longue beside a floor-to-ceiling window, the city skyline far below in warm evening haze, the room tidy. She reclines on the chaise longue facing the camera, propped on one elbow, her other hand resting on her hip and her legs extended together along the chaise, looking at the camera with a calm, knowing half-smile. Horizontal 16:9 frame, full-frame camera with a 50mm lens from about 2.6 metres, camera at the height of the chaise; her whole reclining figure from her bare feet to her head, she fills about 87% of the frame width, centred along the chaise with the window and skyline behind her. Lighting: warm low sunset light through the window from camera-right as the key, a soft fill just out of frame on the left keeping her face clear; wine red, deep green and soft gold tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.9 H-rainie-hsu｜Rainie｜橫式款（Penny 已接受的 v2 主方向）

**一句話：** Penny 已接受的方向：頂樓夜景，血紅緞面馬甲高衩迷你洋裝，背靠玻璃欄杆直視鏡頭。

| 項目 | 內容 |
|---|---|
| 場景 | 高樓頂層露台的夜晚：玻璃欄杆、腳下城市燈光化成柔和散景、平滑深色石材地面，露台上沒有其他東西。 |
| 服裝 | 洋裝：血紅緞面馬甲迷你洋裝（大腿高衩）；鞋：黑色細帶高跟涼鞋；配件：大型銀色垂墜耳環、細銀手環 |
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
| 景別與人物佔比 | 膝上；人物約佔畫面高度 84%；頭頂完整、雙手在框內，切在膝蓋下方；人物偏右，左側約四到五成給場景 |
| 焦段／距離／視野 | 16:9，85mm，約 6.0 公尺，視野 2.54×1.43 公尺 |
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
A 24-year-old adult Taiwanese woman with her natural fair skin tone, high cheekbones and a sculpted jaw, soft-glam makeup with a soft brown liner close to the lash line, long straight jet-black hair worn sleek and glossy with a deep side part. Curvy figure, 165 cm tall, bust 94 cm, waist 59 cm, hips 92 cm, F cup, full chest and slim waist. She wears a blood-red satin corset mini dress with a thigh-high slit, strappy black stiletto sandals, large silver statement drop earrings and a slim silver cuff. Setting: a high-rise penthouse terrace at night, a glass balustrade with the city lights far below spread into soft bokeh, a smooth dark stone floor, nothing else on the terrace, the glass reflecting only city lights. She leans back against the glass balustrade with both hands resting on the rail behind her and one leg forward through the slit, looking straight into the camera with a confident, slightly mischievous smirk. Horizontal 16:9 frame, full-frame camera with an 85mm lens from about 6 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 84% of the frame height, right of centre with the glowing city bokeh on the left. Lighting: a large bright softbox key from front-left at head height lights her face and catches crisp red highlights on the satin; a soft fill from the right just out of frame; deep navy night sky and warm gold city bokeh behind her. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.10 H-miu-shiraishi｜Miu｜橫式款（新企劃）

**一句話：** 一人公寓的早晨，象牙白蕾絲緞面細肩小可愛與短褲，坐在床邊歪頭甜笑。

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
| 姿態 | 面向鏡頭坐在床邊，雙膝併攏、略偏向一側。 |
| 手的位置 | 雙手撐在身旁的床上。 |
| 表情 | 歪頭、柔和的甜笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 坐姿全身；人物約佔畫面高度 84%；坐姿頭頂到腳完整，雙手在框內；人物偏左，右側約四到五成給場景 |
| 焦段／距離／視野 | 16:9，35mm，約 2.7 公尺，視野 2.78×1.56 公尺 |
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
A 22-year-old adult Japanese woman with her natural very fair skin tone, a round face with big soft downturned eyes, orange-toned blush under the eyes and glossy lips, light flaxen beige-blonde hair in a shoulder-length bob curled inward with airy see-through bangs. Petite curvy figure, 156 cm tall, bust 87 cm, waist 55 cm, hips 86 cm, E cup, a full chest and a very slim waist. She wears an ivory satin camisole with thin straps and fine lace trim that follows her full chest, matching ivory satin shorts, small gold stud earrings and a thin gold bracelet; her feet are bare. Setting: a small sunlit Tokyo apartment in the morning, a neatly made bed with cream linen, a wooden bedside shelf with a small potted plant, sheer white curtains at the window, the room tidy. She sits on the edge of the bed facing the camera, knees together and angled slightly to one side, both hands resting on the bed beside her hips, tilting her head with a soft, sweet smile at the camera. Horizontal 16:9 frame, full-frame camera with a 35mm lens from about 2.7 metres, camera at her seated chest height; full length seated, from her feet to a little above her head, she fills about 84% of the frame height, left of centre with the bright curtained window on the right. Lighting: warm morning sunlight through the sheer curtains from camera-left as a soft key, a white bounce just out of frame on the right so her face is evenly lit; cream, ivory and warm wood tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.11 H-jia-seo｜Jia｜橫式款（新企劃）

**一句話：** 現代美術館的白色展廳，黑色單肩貼身中長洋裝帶腰側鏤空，冷靜站在畫作之間。

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
| 姿態 | 正面站在展廳中央，重心在一隻腳。 |
| 手的位置 | 一手放在腰側，一手自然垂放。 |
| 表情 | 冷靜自信的半笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 84%；頭頂完整、雙手在框內，切在膝蓋下方；人物偏左，右側約四到五成給場景 |
| 焦段／距離／視野 | 16:9，50mm，約 3.7 公尺，視野 2.66×1.5 公尺 |
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
A 22-year-old adult Korean woman with her natural fair, cool-toned skin, a small face, straight shoulders and long narrow upturned eyes, dewy no-makeup makeup with a soft brown liner and gradient lips, long cool blue-black hair tucked behind one ear so its mint-green inner layer shows. Slim, long-legged figure with soft feminine curves, 168 cm tall, bust 85 cm, waist 58 cm, hips 90 cm, C cup, a slim waist and long legs. She wears a black one-shoulder fitted midi dress with a small cut-out at the waist that shows her slim waist and long lines, black strappy heels and small silver hoop earrings. Setting: a modern art gallery with high white walls, a polished concrete floor and large abstract paintings in soft grey and mint tones, track lights on the ceiling, the gallery empty. She stands in the middle of the gallery facing the camera, weight on one leg, one hand resting at her waist and the other relaxed at her side, looking at the camera with a cool, confident half-smile. Horizontal 16:9 frame, full-frame camera with a 50mm lens from about 3.7 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 84% of the frame height, left of centre with the abstract paintings on the white wall to the right. Lighting: cool daylight from a skylight with warm track lights on the paintings; a soft key light from front-left just out of frame lights her face evenly; black, white, grey and mint tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.12 H-yerin-han｜Yerin｜橫式款（新企劃）

**一句話：** 春天早晨的球場，白色無袖針織 polo 配淺藍百褶高爾夫迷你裙，坐在白色球車上的可愛笑容。

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
| 姿態 | 側坐在球車前座、身體面向鏡頭，雙腿伸出車外、在腳踝交叉。 |
| 手的位置 | 一手搭在椅背上，一手放在膝上。 |
| 表情 | 明亮可愛的笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 坐姿全身；人物約佔畫面高度 86%；坐姿頭頂到腳完整，雙手在框內；人物偏左，右側約四到五成給場景 |
| 焦段／距離／視野 | 16:9，50mm，約 4.4 公尺，視野 3.17×1.78 公尺 |
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
A 26-year-old adult Korean woman with her natural fair skin tone, bright defined features and a wide open smile, light sun-protective makeup and a bright lip, long flax-brown hair with golden face-framing highlights in a low ponytail pulled through the back of a plain white cap. Curvy athletic figure with soft feminine lines, 170 cm tall, bust 90 cm, waist 60 cm, hips 93 cm, E cup, long legs and a slim waist. She wears a white fitted sleeveless knit golf polo that follows her full chest and slim waist, a pale sky-blue pleated golf mini skirt, white golf shoes, a plain white cap and small gold stud earrings. Setting: a golf course on a clear spring morning, a plain white golf cart parked on the cart path beside a bright green fairway, soft trees in the distance, the course empty. She sits sideways on the front seat of the golf cart facing the camera, her legs out of the cart and crossed at the ankles, one hand resting on the seat back and the other on her knee, smiling brightly at the camera. Horizontal 16:9 frame, full-frame camera with a 50mm lens from about 4.4 metres, camera at her seated chest height; full length seated, from her golf shoes to a little above her head, she fills about 86% of the frame height, left of centre with the white golf cart and green fairway on the right. Lighting: clear morning sun from high front-left, a large white reflector just out of frame softening the shadow of the cap on her face; bright green, sky blue and white tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.13 V-iris-chen｜Iris｜直式款（新企劃）

**一句話：** 黃金時段的河濱草地，白色方領短上衣配牛仔迷你裙，正面站著甜笑（Penny 指定的穿搭）。

| 項目 | 內容 |
|---|---|
| 場景 | 台北河濱公園的開闊草地，傍晚太陽低，遠處柔綠樹林與低矮公寓，草地與小徑空無一人。 |
| 服裝 | 上身：白色貼身羅紋方領短袖短上衣（露腰）；下身：淺藍高腰牛仔迷你裙；鞋：白色低筒帆布鞋；配件：小金色圈耳環 |
| 髮型 | 黑色柔順直髮自然垂放過肩。 |
| 妝感 | 乾淨的日常妝、自然唇色。 |
| 身材設定（數字） | 162 cm／87-58-90／D |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身方領短上衣清楚呈現 D 罩杯胸型、露出細腰；高腰牛仔迷你裙強調腰臀比與腿長。 |
| 主光 | 她身後側方的低角度夕陽，頭髮與肩線一圈暖色輪廓光 |
| 補光 | 畫面外前方的大反光板加柔光，臉與身體均勻 |
| 姿態 | 身體正面朝鏡頭站著，重心在一隻腳、另一膝放鬆。 |
| 手的位置 | 一手插腰，一手輕碰太陽穴旁的頭髮。 |
| 表情 | 明亮溫暖的笑 |
| 視線 | 直視鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 85%；頭頂完整、雙手在框內，切在膝蓋下方；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，85mm，約 3.8 公尺，視野 1.07×1.43 公尺 |
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
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a round sweet face with large bright double-eyelid eyes and full lips, black silky straight hair worn down past her shoulders. Petite curvy figure, 162 cm tall, bust 87 cm, waist 58 cm, hips 90 cm, D cup, a full chest, a slim waist and rounded hips. She wears a fitted white ribbed square-neck short-sleeve crop top that shows the shape of her chest and her bare waist, a high-waisted light-blue denim mini skirt, white low canvas sneakers and small gold hoop earrings. Setting: an open riverside lawn in a Taipei park in the late afternoon, soft green trees and low distant apartment blocks far behind her, the lawn and the path empty. She stands with her body facing the camera, weight on one leg and the other knee relaxed, one hand on her hip and the other lightly touching her hair at her temple, smiling at the camera with a bright, warm smile. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.8 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 85% of the frame height, centred with soft lawn and trees behind her. Lighting: the low sun behind her and to one side draws a warm rim along her hair and shoulders; a large white reflector and a soft fill light just out of frame in front of her light her face and body evenly; warm golden tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.14 V-luna-tanaka｜Luna｜直式款（新企劃）

**一句話：** 紫陽花盛開的町家庭院，鼠尾草綠馬甲感洋裝，正面站在石板路上。

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
| 姿態 | 正面站在石板路上，重心在一隻腳。 |
| 手的位置 | 雙手輕輕交握在身後。 |
| 表情 | 溫柔的微笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 全身；人物約佔畫面高度 86%；頭頂到腳完整，雙手在框內；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，85mm，約 4.9 公尺，視野 1.38×1.84 公尺 |
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
A 20-year-old adult Japanese woman with her natural fair skin tone, large round dark-brown eyes and soft natural makeup with a rosy lip, black fine straight hair in a centre-parted, chin-length bob. Petite figure with a noticeably full chest and a slim waist, 155 cm tall, bust 88 cm, waist 56 cm, hips 87 cm, E cup. She wears a pale sage-green cotton sundress with a sweetheart neckline, a fitted boned bodice that shapes her full chest and narrow waist and a softly flared mini skirt, cream low block-heel strappy sandals and a thin gold bracelet. Setting: a quiet garden behind an old wooden Kyoto-style townhouse, moss ground, a stone path, white hydrangeas in bloom along a low wooden fence, maple branches overhead. She stands on the stone path facing the camera, weight on one leg, both hands clasped lightly behind her back, looking at the camera with a gentle smile. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 4.9 metres, camera at her navel height; full length from her sandals to a little above her head, she fills about 86% of the frame height, centred with maple branches across the top edge. Lighting: bright overcast daylight as one large soft source, with a white reflector just out of frame so her face is clean and evenly lit; soft dappled light falls only on the hydrangeas and path behind her; fresh green, white and sage tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.15 V-somi-oh｜Somi｜直式款（新企劃）

**一句話：** 下雪的溫泉小鎮夜晚，象牙白貼身針織洋裝外披紅色長大衣，在燈籠光裡大笑。

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
| 姿態 | 正面站在雪地上，重心在一隻腳。 |
| 手的位置 | 雙手插在敞開的大衣口袋裡，把大衣往後撐開。 |
| 表情 | 月牙眼大笑、露出酒窩 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 84%；頭頂完整、雙手在框內，切在膝蓋下方；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，85mm，約 3.8 公尺，視野 1.07×1.43 公尺 |
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
A 24-year-old adult Korean woman with her natural fair skin tone and round cheeks that dimple when she smiles, bright honey-orange brown hair in a layered Korean wolf cut. Curvy figure, 161 cm tall, bust 91 cm, waist 58 cm, hips 90 cm, F cup, full chest and slim waist. She wears a fitted ivory ribbed knit mini dress with a high round neck that follows her full chest, slim waist and hips, a long red wool coat worn open, white knee-high boots and small pearl earrings. Setting: a quiet street in a small hot-spring town on a snowy winter evening, low wooden inns with warm paper lanterns, thin steam rising from a stone channel at the roadside, a light layer of snow on the ground, the street empty. She stands facing the camera with her weight on one leg, both hands in the pockets of the open coat holding it back so the fitted dress shows, laughing at the camera with her eyes curved into crescents and dimples showing, a few snowflakes in the air. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.8 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 84% of the frame height, centred with the lantern-lit street behind her. Lighting: a soft warm key light from front-left just out of frame lights her face evenly; the paper lanterns behind her glow warm amber against the cool blue evening light on the snow; red, ivory and warm amber tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.16 V-coco-wu｜Coco｜直式款（Penny 已接受的 v2 主方向）

**一句話：** Penny 已接受的方向：週末飯店泳池，薄荷綠比基尼＋淺紫透膚罩衫，坐在池邊大笑。

| 項目 | 內容 |
|---|---|
| 場景 | 週末早上的度假飯店泳池：淺米色石材地磚、清澈的湖水綠池水、遠處收起的白色陽傘，池畔無人。 |
| 服裝 | 泳裝：薄荷綠羅紋三角比基尼上衣與同色側綁下著（完整遮蔽）；外搭：敞開的淺紫透膚短袖罩衫（落在肩後）；配件：白色雛菊髮夾、腳踝細金鍊 |
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
| 景別與人物佔比 | 坐姿到水面；人物約佔畫面高度 81%；頭頂完整、撐地的雙手在框內，小腿在水中；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，70mm，約 2.7 公尺，視野 0.93×1.23 公尺 |
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
A 20-year-old adult Taiwanese woman with her natural fair skin tone, deep dimples when she smiles and dark-brown long wavy hair with soft wispy bangs, the ends slightly wet. Petite curvy figure, 158 cm tall, bust 89 cm, waist 56 cm, hips 86 cm, E cup, full chest and slim waist. She wears a mint-green ribbed triangle bikini top with matching side-tie bottoms that fully cover, an open sheer lilac short-sleeve cover-up shirt resting off her shoulders, a white daisy hair clip and a thin gold anklet. Setting: a resort hotel pool on a weekend morning, pale cream stone tiles, clear turquoise water, white umbrellas folded in the distance, the pool deck empty. She sits on the pool edge with both lower legs in the water, leaning back on her hands, head tilted, laughing with her eyes squeezed into crescents and dimples showing. Vertical 3:4 frame, full-frame camera with a 70mm lens from about 2.7 metres, camera at her seated chest height; framed from the waterline to a little above her head, she fills about 81% of the frame height, centred with the water across the bottom of the frame. Lighting: bright late-morning sun from high front-left; a large white reflector just out of frame fills the shadows on her face and body so her face is evenly lit; the turquoise water adds soft aqua reflections on her legs; clear, fresh summer colours. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.17 V-mia-huang｜Mia｜直式款（新企劃）

**一句話：** 春夜的櫻花河岸步道，淺紫貼身露肩針織洋裝，站在花枝下甜笑。

| 項目 | 內容 |
|---|---|
| 場景 | 春天夜晚的河岸步道，盛開的櫻花樹在頭上交錯，步道旁掛著柔和紙燈籠，步道空無一人。 |
| 服裝 | 洋裝：淺紫細針織貼身露肩迷你洋裝；鞋：白色及膝長靴；配件：一側小珍珠髮夾、細銀耳環 |
| 髮型 | 灰棕色長髮鬆散大波浪，左側臉旁粉紅 money piece 挑染。 |
| 妝感 | 柔和動漫感眼妝、圓形腮紅、水光唇。 |
| 身材設定（數字） | 160 cm／91-57-88／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 露肩貼身針織洋裝勾出 F 罩杯胸型、細腰與臀線；及膝靴拉長腿部。 |
| 主光 | 畫面外左前方柔和暖色主光 |
| 補光 | 燈籠讓櫻花透出暖粉色，背後深藍夜空 |
| 姿態 | 正面站在低垂的花枝下。 |
| 手的位置 | 一手輕觸肩旁的花枝，一手自然垂放。 |
| 表情 | 甜甜的微笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 84%；頭頂完整、雙手在框內，切在膝蓋下方；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，85mm，約 3.8 公尺，視野 1.07×1.43 公尺 |
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
A 22-year-old adult Taiwanese woman with her natural fair skin tone, a soft round face with big expressive eyes, softly winged liner, rounded blush and glossy tinted lips, long ash-brown hair in loose waves with a pastel-pink money-piece highlight framing the left side of her face. Curvy figure, 160 cm tall, bust 91 cm, waist 57 cm, hips 88 cm, F cup, a full chest and a slim waist. She wears a lilac fitted fine-knit off-shoulder mini dress that follows her full chest, slim waist and hips, white knee-high boots, small pearl hair clips on one side and thin silver earrings. Setting: a riverside promenade at night in spring, cherry trees in full bloom arching overhead, soft plain paper lanterns hanging along the path, the path empty. She stands under a low blossom branch facing the camera, one hand lightly touching the branch above her shoulder and the other relaxed at her side, smiling sweetly at the camera. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.8 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 84% of the frame height, centred under the arching blossoms. Lighting: a soft warm key light from front-left just out of frame lights her face evenly; the lanterns give the blossoms a warm pink glow against a deep blue night sky; pink, lilac and deep blue tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.18 V-yuna-kim｜Yuna｜直式款（新企劃）

**一句話：** 深秋的銀杏大道，奶油色毛呢短外套套裝配黑色長靴，站在落葉上的韓劇感街拍寫真。

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
| 姿態 | 正面站在落葉人行道上，重心在一隻腳。 |
| 手的位置 | 一手拉著肩上的包包背帶，一手自然垂放。 |
| 表情 | 頭微傾、柔和的微笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 全身；人物約佔畫面高度 87%；頭頂到腳完整，雙手在框內；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，85mm，約 5.3 公尺，視野 1.5×2.0 公尺 |
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
A 21-year-old adult Korean woman with her natural fair skin tone, large bright double-eyelid eyes as the focus of her makeup, a dewy glass-skin finish and soft coral gradient lips, dark-brown natural wavy hair at collarbone length with airy curtain bangs. Slim, long-legged figure, 168 cm tall, bust 84 cm, waist 58 cm, hips 89 cm, C cup, a narrow waist and long legs. She wears a cream tweed cropped jacket, collarless and buttoned, fitted close to her chest and waist, a matching high-waisted tweed mini skirt, black knee-high leather boots, small pearl earrings and a small plain black shoulder bag. Setting: a quiet residential avenue in late autumn lined with golden ginkgo trees, fallen yellow leaves covering the sidewalk, low modern buildings softly out of focus, the street empty. She stands on the leaf-covered sidewalk facing the camera, weight on one leg, one hand holding the strap of the bag at her shoulder and the other relaxed at her side, head tilted slightly with a soft smile. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 5.3 metres, camera at her navel height; full length from her boots to a little above her head, she fills about 87% of the frame height, centred with golden ginkgo trees on both sides. Lighting: low afternoon sun behind the ginkgo trees lights the leaves and draws a warm rim on her hair; a large white reflector just out of frame lights her face evenly; golden yellow, cream and black tones with a soft film-like finish. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.19 V-tammy-chou｜Tammy｜直式款（新企劃）

**一句話：** 夜晚的大飯店大廳，白色西裝外套洋裝配黑色細跟鞋，雙手插腰的自信全身照。

| 項目 | 內容 |
|---|---|
| 場景 | 夜晚大飯店的大廳：拋光大理石地板與柱子、頭頂溫暖的水晶吊燈、背景圓桌上一大盆白花，大廳沒有其他人。 |
| 服裝 | 洋裝：白色合身西裝外套式迷你洋裝（深 V 翻領、金色扣子、繫腰帶）；鞋：黑色尖頭細高跟鞋；配件：金色垂墜耳環 |
| 髮型 | 奶茶金棕大波浪長捲髮，臉側淺色 money piece 挑染。 |
| 妝感 | 閃粉眼影、果凍唇。 |
| 身材設定（數字） | 160 cm／90-57-89／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 深 V 翻領與腰帶勾出 E 罩杯胸型與細腰；迷你裙長與高跟鞋讓腿部比例完整。 |
| 主光 | 畫面外右前方柔光 |
| 補光 | 水晶吊燈的暖色環境光 |
| 姿態 | 正面站在大理石柱旁，一腳略往前。 |
| 手的位置 | 雙手插腰。 |
| 表情 | 自信的笑容 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 全身；人物約佔畫面高度 85%；頭頂到腳完整，雙手在框內；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，70mm，約 4.3 公尺，視野 1.47×1.97 公尺 |
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
A 24-year-old adult Taiwanese woman with her natural fair skin tone, round almond eyes with visible aegyo-sal, shimmer eyeshadow and jelly-glossy lips, long voluminous big-wave hair in milk-tea golden brown with light money-piece highlights at the front. Curvy figure, 160 cm tall, bust 90 cm, waist 57 cm, hips 89 cm, E cup, a full chest and a slim waist. She wears a white tailored blazer mini dress with a deep V lapel, gold buttons and a belted waist that defines her full chest and slim waist, black pointed stiletto heels and gold drop earrings. Setting: the lobby of a grand hotel at night, polished marble floor and columns, a warm crystal chandelier overhead, a large arrangement of white flowers on a round table in the background, the lobby empty. She stands beside a marble column facing the camera with both hands on her hips and one foot slightly forward, smiling confidently at the camera. Vertical 3:4 frame, full-frame camera with a 70mm lens from about 4.3 metres, camera at her navel height; full length from her heels to a little above her head, she fills about 85% of the frame height, centred with the chandelier glow above her. Lighting: warm chandelier light fills the space; a soft key light from front-right just out of frame lights her face evenly; white, gold and warm marble tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.20 V-rin-ayase｜Rin｜直式款（Penny 採用的 v2 替代方向）

**一句話：** Penny 採用的 v2 替代方向：出勤前的銀座，黑色絲絨細肩帶長禮服，坐在金色燈光的吧台邊（不拿酒杯）。

| 項目 | 內容 |
|---|---|
| 場景 | 開店前的高級會員制酒吧：一長條拋光深色木吧台、溫暖的金色吊燈、背後柔焦的層架，吧台面乾淨，店內沒有其他人。 |
| 服裝 | 洋裝：黑色絲絨細肩帶及地長禮服（貼身上身）；鞋：黑色細帶高跟鞋；配件：小金色垂墜耳環、細金手鍊 |
| 髮型 | 深酒紅棕長髮，光滑的低髻。 |
| 妝感 | 乾淨底妝、精準眼線、豆沙紅唇。 |
| 身材設定（數字） | 166 cm／92-58-90／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身絲絨上身呈現 F 罩杯胸型與細腰；坐在高腳椅上、雙腿交疊，長禮服順著腿部線條垂下。 |
| 主光 | 頭頂溫暖的金色吊燈＋畫面外左前方柔光 |
| 補光 | 吧台與層架的金色反光 |
| 姿態 | 坐在高腳椅上、身體轉向鏡頭，雙腿交疊。 |
| 手的位置 | 一手手肘靠在吧台上，一手放在膝上；手上不拿杯子。 |
| 表情 | 平靜、端莊的微笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 坐姿全身；人物約佔畫面高度 84%；坐姿頭頂到腳完整，雙手在框內；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，70mm，約 4.2 公尺，視野 1.44×1.92 公尺 |
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
A 25-year-old adult Japanese woman with her natural fair, cool-toned skin, an oval face with long narrow eyes and a straight nose, a clean base with precise eyeliner and a muted rose-red lip, long deep wine-red brown hair pinned in a sleek low bun. Curvy figure, 166 cm tall, bust 92 cm, waist 58 cm, hips 90 cm, F cup, a full chest, a slim waist and long legs. She wears a black velvet floor-length gown with thin spaghetti straps and a fitted bodice that follows her full chest and slim waist, black strappy heels, small gold drop earrings and a thin gold bracelet. Setting: an elegant high-end Tokyo members' bar before opening, a long polished dark-wood counter, warm golden pendant lights and softly blurred shelves behind the counter, the counter clean and clear, the bar empty. She sits on a tall bar stool turned toward the camera with her legs crossed under the long gown, one elbow resting on the counter and the other hand on her knee, looking at the camera with a calm, poised smile. Vertical 3:4 frame, full-frame camera with a 70mm lens from about 4.2 metres, camera at her seated chest height; full length seated, from her heels to a little above her head, she fills about 84% of the frame height, centred with the golden bar counter beside her. Lighting: warm golden pendant light from above and a soft key light from front-left just out of frame light her face evenly; the velvet holds deep black while the counter glows gold; black, gold and deep wood tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.21 V-rainie-hsu｜Rainie｜直式款（新企劃）

**一句話：** 雨後的夜晚街道，黑色緞面繞頸迷你洋裝外搭黑色長皮風衣，站在濕亮的路面上直視鏡頭。

| 項目 | 內容 |
|---|---|
| 場景 | 夜晚剛下過雨的城市街道：濕亮的路面倒映暖色櫥窗光與冷色路燈，店面已打烊、只有素面霧玻璃，街上沒有人。 |
| 服裝 | 洋裝：黑色緞面繞頸迷你洋裝；外套：黑色長版皮革風衣（敞開）；鞋：黑色細跟尖頭短靴；配件：大型銀色垂墜耳環 |
| 髮型 | 長直黑髮，光滑有光澤，深側分。 |
| 妝感 | 柔和魅惑妝、貼近睫毛的淡棕眼線。 |
| 身材設定（數字） | 165 cm／94-59-92／F |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 繞頸緞面洋裝貼合 F 罩杯胸型、細腰與臀線；敞開的長風衣形成直向線條，讓 165 cm 的身形更修長。 |
| 主光 | 畫面外左前方大型柔光，臉清楚 |
| 補光 | 濕路面上暖琥珀與冷藍的倒影 |
| 姿態 | 正面站在濕亮的人行道上，重心在一隻腳。 |
| 手的位置 | 一手拉著敞開的風衣衣襟在腰間，一手自然垂放。 |
| 表情 | 自信、帶點壞的笑 |
| 視線 | 直視鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 84%；頭頂完整、雙手在框內，切在膝蓋下方；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，85mm，約 3.9 公尺，視野 1.1×1.47 公尺 |
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
A 24-year-old adult Taiwanese woman with her natural fair skin tone, high cheekbones and a sculpted jaw, soft-glam makeup with a soft brown liner close to the lash line, long straight jet-black hair worn sleek and glossy with a deep side part. Curvy figure, 165 cm tall, bust 94 cm, waist 59 cm, hips 92 cm, F cup, full chest and slim waist. She wears a black satin halter mini dress that follows her full chest, slim waist and hips, a long black leather trench coat worn open, black pointed ankle boots with a slim heel and large silver statement drop earrings. Setting: a city street at night just after rain, the wet pavement reflecting warm amber light from closed shopfronts with plain frosted glass and cool blue street lights, the street empty. She stands on the wet pavement facing the camera, weight on one leg, one hand holding the edge of the open coat at her waist and the other relaxed at her side, looking straight into the camera with a confident, slightly mischievous smirk. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.9 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 84% of the frame height, centred with the reflective wet street behind her. Lighting: a large soft key light from front-left just out of frame lights her face clearly; warm amber and cool blue reflections shimmer on the wet street behind her; black, silver and deep blue tones with a hint of amber. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.22 V-miu-shiraishi｜Miu｜直式款（新企劃）

**一句話：** 暮春的運河步道，奶油色 V 領合身針織洋裝繫細腰帶，靠著欄杆甜笑。

| 項目 | 內容 |
|---|---|
| 場景 | 暮春安靜的運河步道：窄窄的運河兩岸新綠的樹、低矮金屬欄杆、對岸的小咖啡館在背景失焦，步道上沒有人。 |
| 服裝 | 洋裝：奶油色 V 領細羅紋合身針織迷你洋裝（前排小扣、細棕色腰帶）；鞋：奶油色繫踝低跟鞋；配件：細金耳針 |
| 髮型 | 淺亞麻米金，齊肩內彎鮑伯、空氣瀏海。 |
| 妝感 | 眼下橘調腮紅、水潤唇。 |
| 身材設定（數字） | 156 cm／87-55-86／E |
| 畫面上怎麼呈現胸型、腰線、臀腿 | V 領與合身細針織清楚呈現 E 罩杯胸型，細腰帶收出 55 cm 的腰線；迷你裙長露出腿。 |
| 主光 | 明亮柔和的陰天光 |
| 補光 | 畫面外白色反光板 |
| 姿態 | 正面站在欄杆旁，重心在一隻腳。 |
| 手的位置 | 一手扶著欄杆，一手輕輕拿著臉旁的一縷頭髮。 |
| 表情 | 甜甜的微笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 84%；頭頂完整、雙手在框內，切在膝蓋下方；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，85mm，約 3.7 公尺，視野 1.04×1.39 公尺 |
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
A 22-year-old adult Japanese woman with her natural very fair skin tone, a round face with big soft downturned eyes, orange-toned blush under the eyes and glossy lips, light flaxen beige-blonde hair in a shoulder-length bob curled inward with airy see-through bangs. Petite curvy figure, 156 cm tall, bust 87 cm, waist 55 cm, hips 86 cm, E cup, a full chest and a very slim waist. She wears a cream fitted V-neck fine-rib knit mini dress with small front buttons and a thin brown belt at the waist that shows her full chest and very slim waist, cream ankle-strap low heels and thin gold stud earrings. Setting: a quiet canal-side promenade in late spring, fresh green trees along a narrow canal, a low metal railing, small cafés softly out of focus on the far bank, the promenade empty. She stands by the railing facing the camera, weight on one leg, one hand resting on the railing and the other lightly holding a strand of her hair at her cheek, smiling sweetly at the camera. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.7 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 84% of the frame height, centred with the green canal behind her. Lighting: soft bright overcast daylight with a white reflector just out of frame lighting her face evenly; fresh green, cream and soft brown tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.23 V-jia-seo｜Jia｜直式款（新企劃）

**一句話：** 明亮的玻璃溫室，白色無袖立領短上衣配薄荷綠緞面開衩中長裙，站在大葉植物之間。

| 項目 | 內容 |
|---|---|
| 場景 | 玻璃溫室：白色鋼骨結構、茂密的熱帶植物與大片龜背芋葉、石板小徑，溫室裡沒有其他人。 |
| 服裝 | 上身：白色無袖立領貼身短上衣（露腰）；下身：高腰薄荷鼠尾草綠緞面中長裙（側開衩）；鞋：白色細帶涼鞋；配件：細銀耳針 |
| 髮型 | 冷灰藍黑長髮，一側塞在耳後露出薄荷綠內層。 |
| 妝感 | 水光無妝感、淡棕眼線、漸層唇。 |
| 身材設定（數字） | 168 cm／85-58-90／C（直角肩、長腿） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 短上衣露出細腰，緞面長裙貼著臀線、側開衩露出一條長腿。 |
| 主光 | 玻璃屋頂的大面積明亮漫射光 |
| 補光 | 畫面外前方柔光 |
| 姿態 | 正面站在植物之間的石板路上。 |
| 手的位置 | 一手輕觸身旁的大片龜背芋葉，一手插腰。 |
| 表情 | 冷靜柔和的微笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 86%；頭頂完整、雙手在框內，切在膝蓋下方；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，85mm，約 3.9 公尺，視野 1.1×1.47 公尺 |
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
A 22-year-old adult Korean woman with her natural fair, cool-toned skin, a small face, straight shoulders and long narrow upturned eyes, dewy no-makeup makeup with a soft brown liner and gradient lips, long cool blue-black hair tucked behind one ear so its mint-green inner layer shows. Slim, long-legged figure with soft feminine curves, 168 cm tall, bust 85 cm, waist 58 cm, hips 90 cm, C cup, a slim waist and long legs. She wears a white sleeveless mock-neck fitted crop top that shows her slim waist, a high-waisted mint-sage satin midi skirt with a side slit, white strappy sandals and small silver stud earrings. Setting: a glass greenhouse conservatory with white steel frames, lush tropical plants and large monstera leaves, a stone path, the greenhouse empty. She stands on the stone path among the plants facing the camera, one hand lightly touching a large monstera leaf beside her and the other on her hip, the slit of the skirt showing one leg, looking at the camera with a cool, soft smile. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 3.9 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 86% of the frame height, centred among the plants. Lighting: bright diffused daylight through the glass roof as a large soft key, a soft fill just out of frame in front; white, mint and deep green tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

### 5.24 V-yerin-han｜Yerin｜直式款（新企劃）

**一句話：** 日落的白沙海灘，白色圓領貼身針織背心洋裝，赤腳站在淺浪邊的燦笑。

| 項目 | 內容 |
|---|---|
| 場景 | 日落時寬闊的白沙海灘，平靜的淺水、海上金色與蜜桃色的天空，海灘上沒有其他人。 |
| 服裝 | 洋裝：白色圓領羅紋貼身背心迷你洋裝；鞋：赤腳；配件：小金色圈耳環、腳踝細金鍊 |
| 髮型 | 亞麻棕長髮、臉側金色挑染，放下的鬆散波浪。 |
| 妝感 | 防曬淡妝、亮色唇。 |
| 身材設定（數字） | 170 cm／90-60-93／E（健康曲線） |
| 畫面上怎麼呈現胸型、腰線、臀腿 | 貼身羅紋背心洋裝勾出 E 罩杯胸型、細腰與 93 cm 的臀線；赤腳站立讓長腿比例自然。 |
| 主光 | 她身後的低角度夕陽，頭髮與肩膀暖色輪廓光 |
| 補光 | 畫面外前方大反光板與柔光 |
| 姿態 | 正面站在浪花邊的淺水裡，重心在一隻腳。 |
| 手的位置 | 一手輕放在鎖骨，一手自然垂放。 |
| 表情 | 大方燦爛的笑 |
| 視線 | 看鏡頭 |
| 景別與人物佔比 | 膝上；人物約佔畫面高度 85%；頭頂完整、雙手在框內，切在膝蓋下方；人物置中，頭頂與兩側少量留白 |
| 焦段／距離／視野 | 3:4，85mm，約 4.0 公尺，視野 1.13×1.51 公尺 |
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
A 26-year-old adult Korean woman with her natural fair skin tone, bright defined features and a wide open smile, light sun-protective makeup and a bright lip, long flax-brown hair with golden face-framing highlights worn down in loose waves. Curvy athletic figure with soft feminine lines, 170 cm tall, bust 90 cm, waist 60 cm, hips 93 cm, E cup, long legs and a slim waist. She wears a white fitted ribbed scoop-neck tank mini dress that follows her full chest, slim waist and hips, small gold hoop earrings and a thin gold anklet; her feet are bare and the dress is dry. Setting: a wide white-sand beach at sunset, calm shallow water and a soft gold and peach sky over the sea, the beach empty. She stands in the shallow foam at the water's edge facing the camera, weight on one leg, one hand lightly at her collarbone and the other relaxed at her side, smiling brightly at the camera. Vertical 3:4 frame, full-frame camera with an 85mm lens from about 4 metres, camera at her waist height; framed from just below her knees to a little above her head, she fills about 85% of the frame height, centred with the sunset sea behind her. Lighting: the low sun behind her draws a warm rim along her hair and shoulders; a large white reflector and a soft fill just out of frame in front light her face evenly; warm gold, peach and soft blue tones. Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```

## 6. 構圖與生成提案

| 款式 | 建議 |
|---|---|
| 橫式款（H） | 建議版面用「大照片」框（約 1.85:1）。生成用 16:9（工具支援；原生尺寸未知）：只需上下共裁約 4%。取景以膝上或坐姿全身為主，人物佔畫面高度約 85%，場景放在另一側；不寫成胸上特寫。 |
| 直式款（V） | 建議照片區至少 3:4。生成用 3:4（原生 1536×2048，已知）。取景以膝上為主，Luna、Yuna、Tammy 與 Rin 的長禮服用全身或坐姿全身，讓整套服裝看得到。 |

**評估：**

- 橫式款的價值在於「人＋環境」的寬畫面：大照片框比半版適合。半版直幅框比較適合直式照片，而直式款已經另有 12 套直幅照片。
- 若 Penny 最後選擇橫式款用半版直幅框：這 12 套 16:9 不適用，要另外規劃與生成直幅版本——不從 16:9 硬裁成直幅。
- 直式款若最後用近方形框（約 0.94:1），3:4 要上下共裁約 20%：膝上變大腿以上、全身會切到腳。所以建議直式款的照片區至少 3:4。
- 避免人物縮小到背景裡：所有企劃的人物都佔畫面高度約 80–88%（斜躺的 Rin 佔畫面寬度約 85%），服裝與身形可以辨認。

**限制：**

- 16:9 原生尺寸未知（推測 2048×1152，未驗證）；3:2 也未知。3:4 已知 1536×2048。
- 換算只做比例，不承諾 ppi，也不判斷線圈安全；廠商尺寸與印刷門檻還沒問。
- 外擴與 AI 放大不列為必要步驟。

換算方法：全片幅 36×24 mm。橫式款 16:9 取 36×20.25 mm，視野高＝20.25 mm×距離÷焦段；直式款 3:4 直拿裁成 24×32 mm，視野高＝32 mm×距離÷焦段。每套的焦段、距離、視野與人物佔比都由程式換算，數字矛盾會讓建置失敗。

## 7. 費用（分開精確報價、歷史實扣、未知）

**狀態：** 仍未授權：沒有生成授權、沒有費用核准。下面的數字分成「精確報價」「歷史實扣」「未知」，情境試算不是預算。

**模型：** soul_2＋各人設既有 Soul，quality 2k，每次請求 1 張（count 1）；橫式款 16:9、直式款 3:4；不掛 Reference Element、不用參考圖。

### 7.1 精確報價（generate_image 的 get_cost 預檢，不送出工作）

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

### 7.2 歷史實扣與紀錄

| 項目 | 數值 | 依據 | 等級 | 來源檔 |
|---|---|---|---|---|
| Soul V2 實際扣款（交易明細） | 每筆 −0.12 | Soul 訓練總報告（2026-09-08）：驗證圖 114 張約 13.7 credits，交易明細為重複的「Higgsfield Soul V2 −0.12」；驗證紀錄寫明「每 spec 只生一張」，所以是一次請求 1 張。這批的比例與畫質沒有寫在讀到的文件裡。 | 歷史實扣（交易明細） | `review/soul_training/FINAL_REPORT.md`、`review/soul_pilot/VERIFY_REMAINING_12.md` |
| 2026-10-13 帳號交易明細 | 今天也有 Soul V2 −0.12 的扣款 | 唯讀查詢 transactions：這些是帳號上其他人的工作，不是本案；只說明 Soul V2 目前仍以 −0.12 一筆扣款。 | 歷史實扣（他人工作，只作參考） |  |
| Iris 先前的 Soul 生成 | 費用未逐筆記錄 | Iris 的生成筆記記錄 soul_2＋Soul、2k、3:4 共 7 次生成成功、輸出 1536×2048，但沒有逐筆扣款。 | 無費用紀錄 | `kols/iris-chen/generation_notes.md` |
| 失敗也可能扣款 | 有紀錄 | Soul 訓練總報告的對帳判準：曾出現「重複的 Soul V2 −0.12 扣款但工作失敗」的情況（Vicky Lin 案例），所以重試也要算進上限。 | 歷史紀錄 | `review/soul_training/FINAL_REPORT.md` |

### 7.3 計價方式、張數、上限、異常

| 項目 | 說明 | 來源檔 |
|---|---|---|
| 計價單位 | 工具報價以「每次請求」回傳；count 4 的報價與 count 1 完全相同，所以無法判斷報價是每張還是每次請求。本案只用 count 1，不推算多張的費用。 |  |
| 每次請求產生幾張 | generate_image：count 1–4（同一 prompt 的變體）；generate_image_batch：最多 12 個請求、每個固定 1 張，而且批次不支援費用預檢。本案每次只送 1 個請求、count 1。 |  |
| 能不能限制總費用 | generate_image 與 generate_image_batch 都沒有「費用上限」參數（只有 AI Influencer 工具有，不適用）。只能靠流程控制：一次一個請求、每次之後查交易明細、累計達上限就停。餘額不能用來對帳——帳號同時有其他人在用。 |  |
| 異常扣款 | 原因未知。另一位人設的生成筆記記錄過三次「實扣高於預檢」：seedream_v4_5 4 張扣 50、seedream_v4_5 4 張扣 8、soul_2（不帶 Soul）4 張扣 2.16。三次都是用帳戶餘額前後相減算的，而帳號同時有其他人在用；沒有用交易明細逐筆核對，所以不能歸因，也不能排除。其中兩次是不同模型（seedream_v4_5）。 | `kols/sophia-tseng/generation_notes.md`、`review/soul_training/FINAL_REPORT.md` |

### 7.4 24 套獨立拍攝的情境試算（不是預算）

| 情境 | 請求數 | 依 credits_exact 報價 | 若實扣是顯示值（每次 1） |
|---|---|---|---|
| 每套 1 次請求 | 24 | 約 2.88 | 24 |
| 每套 2 次請求 | 48 | 約 5.76 | 48 |
| 每套 3 次請求 | 72 | 約 8.64 | 72 |

只是用今天的報價換算的情境，不是預算、不保證能做完幾張。「依 credits_exact」是工具的精確報價欄位；「若實扣是顯示值」是假設每次請求扣 1 credit 的上界情境。實扣是哪一個，要等第一張試拍用交易明細確認。失敗與重試都可能扣款。

**未知：** 16:9 與 3:2 的實際輸出像素、16:9、3:4 在這些企劃下的實際扣款（只有報價）、count 大於 1 時的費用、ready 狀態的 Soul 在逆光、夜景、室內暖光下的身分穩定度、24 套獨立造型各自需要幾次才能成功

### 7.5 Iris 首張試拍提案（只是提案）

**推薦：V-iris-chen**

- 直式 3:4 的原生尺寸已知（1536×2048）、報價已查，第一張只需要驗證「寫真質感、身分、身材與實際扣款」，少一個未知數。
- 直幅膝上最能看清 Penny 這次指定的穿搭與姿態：更顯身材的上衣＋牛仔迷你裙、身體面向鏡頭、笑容。
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

## 8. 要請 Penny 決定的事

1. 24 套企劃：每套選「接受」或「想修改」，想修改的寫在備註。未回覆不算接受。
2. 兩本月份推薦（橫式款、直式款）：接受，或想怎麼調。
3. 版面與構圖建議（橫式款用大照片框＋16:9；直式款照片區至少 3:4）：接受，或想改。
4. Iris 首張試拍候選：建議先試 V-iris-chen（只是候選；生成與費用仍要另外核定）。
5. 已接受方向的 H／V 分配（Somi、Rainie 放橫式款；Coco、Rin 放直式款）：接受，或想對調。

## 9. 共同的皮膚與質感句（每段 prompt 結尾都加）

```text
Natural skin texture with visible pores, unretouched, crisp focus on her eyes, fine fabric detail, natural colour grading, a professional fashion editorial photograph.
```
