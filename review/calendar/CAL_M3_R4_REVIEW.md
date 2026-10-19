TASK-CAL-001／M-3／R4｜16 套寫真修訂與印刷構圖核對｜送審報告

# M-3／R4 送審紀錄

- **範圍**：只規劃。**生成 0、credits 0、訓練 0、上傳 0**；本輪沒有呼叫任何 Higgsfield 工具（連報價也沒有）。沒有改 canon、Soul ID、人設設定與身材數字；roster-v1、24 套兩本策略、兩本月份排序都不變；免登入、素材頁不變；沒有登入廠商、上傳、接受條款、聯絡廠商、執行 M-4 或製作交印包；沒有假設 AI 放大或外擴已獲授權。
- **成果 SHA**：`4f1591790d0e04cd58b93d95be470c2ff602e63b`（本輪成果 commit 依序：`13fa4a0751b577a00f87a4a1ac6356878ab0ce3f` 主要內容；`9fa134330787c48cf10fc63b70fd490f1bdbca07` 修正攝影總覽寫錯的戶外與針織套數；`4f1591790d0e04cd58b93d95be470c2ff602e63b` 複查後修正中文「妝感」與英文 prompt 不一致。中間送審 commit `4cb57ba2ad66d7283886e22a93c27594909b44ee` 的內容已由本檔取代。上一輪成果 `8f061fcec58e3dd0451bab8947fe6ed411eb377f`、送審 `2d0784742aad9d4c900223331efe1b8ce0f03ce5`）
- **部署**：Railway `cal2027-decision`，來源固定在 `4f1591790d0e04cd58b93d95be470c2ff602e63b`，deployment `a57e31f0-2478-4b22-a028-6adcbed2e56b`（SUCCESS；先前 13fa4a0 的 `681f0e98-96a6-49ad-8116-08e36506e13f`、9fa1343 的 `dbb82db5-01b1-4bae-b618-8ea775ae0161` 都已被取代）；其他 service 未動
- **企劃頁**：https://cal2027-decision-production.up.railway.app/shoot.html（免登入）；印刷示意：`/print/layout_H.svg`、`/print/layout_V.svg`
- **資料與文件**：`docs/calendar/data/cal_m3_shoot_plan.json`（shoot-plan-v5）、`docs/calendar/data/cal_m3_owner_feedback_r4.json`（R4 owner 回饋逐字＋執行摘要）、`docs/calendar/CAL_18_M3_SHOOT_PLAN.md`（R4 標題）、`docs/calendar/CAL_19_M3_R2_OWNER_DECISION.md`（R2 紀錄，位元組不變）
- **owner 原文來源**：Penny 頁面複製的原始回饋文字沒有直接提供給執行者；本輪保存的是主管轉述的逐字段落，不是頁面 radio 統計，也沒有把舊版回饋當成新回饋。
- 16 套新主推薦是主管推薦的修訂起點加上執行者的細化，**尚未經 Penny 批准**；暫定照片框也未定案。以下驗證都是 **Claude 自測**，不是主管的獨立驗證；部署不等於核准。

## 1. Owner 決策落實表

| owner 決定 | 怎麼落實 | 檢查 |
|---|---|---|
| 1. 8 套接受、16 套修改；H-Jia 雖未勾選，文字要求換場景，列修改 | 資料 status：已接受 8（H-coco-wu、H-mia-huang、H-rainie-hsu、V-iris-chen、V-luna-tanaka、V-coco-wu、V-mia-huang、V-yerin-han）、修訂 16；H-jia-seo 從美術館改為初秋湖畔木平台與長椅 | 頁面測試：8 張綠色「已接受」卡沒有回饋選項、16 張「R4 修訂」卡有接受／想修改；資料測試：H-jia-seo 場景與 v4 不同 |
| 2. 兩本月份排序已確認，不再請 Penny 核准 | 月份與 v4 逐月相同；頁面每張卡標「N 月（已確認）」，月份區標題「兩本月份（已確認）」，題目裡不再有月份題 | 資料測試：兩本 1–12 月與確認排序完全相同；頁面測試：24 張卡月份標籤、月份對照 12 列順序 |
| 3. 更多戶外、更性感、更有寫真感的表情與姿態 | 戶外 14 → 18 套；看鏡頭 23 → 16 套（不看鏡頭 8 套，每套都有視線目標）；修訂的姿勢都有支撐點（岩台站姿插腰、榻榻米單手撐地、吧台倚靠、長椅扶背、貴妃椅前臂撐、床頭靠枕、長椅側坐、球車座椅後撐、繫船柱倚靠、吊床邊抓布邊） | 產生程式逐套檢查禁字（含 sexy、girl、teen、schoolgirl、childlike、kawaii 等）、手不遮胸腰、扭轉 ≤60 度、景別與鞋 |
| 4. 已接受 8 套不因整體偏好擅自重設 | 8 套的主題、場景、服裝、姿態、表情、光線、攝影七欄位與 prompt 都照 v4；印刷核對結果是不需改企劃 | 資料測試：8 套 18 個欄位與 v4 逐字相同 |
| 5. V-Iris 首試方向同意；費用與生成仍未授權 | 頁面與文件寫明未授權；本輪不執行 M-4、沒有任何 Higgsfield 呼叫；印刷核對回答「V-Iris 是否需要構圖微調」（見 §5.5） | 操作紀錄：Higgsfield 呼叫 0 |

**主管的整組檢查要求：**

| 要求 | 結果 |
|---|---|
| 每人 H／V 服裝、場景不同 | 12 位都不同；24 套的場景（env）彼此都不同（資料測試） |
| 月份排序不變 | 與 v4 相同（資料測試） |
| 增加戶外，但不全變成花園、海邊、針織 | 整組戶外 18 套（R3 是 14 套）：室內改戶外 4 套（H-yuna-kim、H-tammy-chou、H-jia-seo、V-rin-ayase）；原本就在戶外、換了場景 2 套（H-iris-chen、V-miu-shiraishi）；庭園類 4 套（Coco 花田、V-Luna 町家庭院、H-Tammy 花園露台、V-Miu 度假木平台）、海景類 4 套（H-Iris 夏日上午岩岸、H-Mia 黃昏遊樂碼頭、V-Yerin 夕陽沙灘、V-Rin 秋日陰天港灣）時間與環境都不同；針織服裝 6 套（H-somi-oh、H-yuna-kim、H-tammy-chou、H-yerin-han、V-somi-oh、V-mia-huang），除了 H-yuna-kim 的內搭是本輪新選，其餘是已接受或 Penny 指定保留的服裝。 |
| 表情不再幾乎全部直視鏡頭 | 不看鏡頭 8 套（H-luna-tanaka、H-rin-ayase、H-jia-seo、V-somi-oh、V-yuna-kim、V-rin-ayase、V-rainie-hsu、V-miu-shiraishi），每套都有明確的視線目標；其餘看鏡頭。正面膝上站姿只剩 H-rainie-hsu（已接受）。側面 2 套（H-jia-seo 側坐、H-rin-ayase 側躺）。 |
| 性感姿態自然、手腳支撐合理、衣物遮蔽明確 | 每套姿勢都寫支撐點與手的位置；服裝寫結構（例：H-Somi 開襟全部不扣＋貼身細肩小可愛；V-Jia 高腰窄裙左前側開衩到大腿中段；V-Miu 有骨架的心形領上身）；H-Yerin 雙膝併攏、相機在坐姿腰部高度平視，不低角度、不走光 |
| 不用未成年化的服裝、表情或措辭 | 禁字檢查通過；所有身分句都是 adult 與設定年齡 |
| 臉、身材維持設定，不靠換臉製造差異 | 24 套身材數字與 v4 相同；16 套修訂的人設身分句（臉、膚色、身材）與 v4 相同（程式比對），只有 V-Rin 的髮型因新場景從俐落低髮髻改為鬆軟低髮髻（造型，不是換臉）；H-Iris、H-Somi、V-Somi 在身分句後另加一句妝感，內容就是中文本來寫的妝感 |
| 中文與 prompt 一致（必要驗證） | 七個攝影欄位、服裝顏色與材質、妝感逐套比對；複查時修正 H-Yuna 中文唇色（玫瑰→珊瑚，依人設）並替 H-Iris、H-Somi、V-Somi 補英文妝感句；已接受的 V-iris、H-coco、V-coco 同樣缺英文妝感句，不改、列待確認（§3） |
| 主角優先，不為家具建築道具縮小人物 | 橫式全身套人物佔畫面高度約 84%（下緣留 7%）；坐躺套依景別留白；道具只作支撐（長椅、吊床、繫船柱、球車） |

## 2. 16 套新主推薦

完整七個攝影欄位、服裝、場景、姿態、光影與英文 prompt 在 CAL_18 §3 與企劃頁每張卡片；中文欄位與 prompt 由同一份設定產生並逐套檢查。

| ID | 新主推薦 | 景別｜身體方向｜臉與視線｜拍攝角度 | 改了什麼 |
|---|---|---|---|
| H-yuna-kim（1月） | 雪後清晨的白樺林小徑，霧玫瑰粉貼身方領針織上衣＋淺灰高腰羊毛迷你裙，外披敞開的白色短版羊羔毛外套。 | 大腿中段以上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視 | 撤回咖啡館與奶油黃開襟＋淺藍裙：改成雪後白樺林小徑的戶外冬日寫真，霧玫瑰貼身方領針織＋淺灰高腰迷你裙＋敞開的白色羊羔毛短外套；景別由腰上改為大腿中段以上。主管推薦是雪後庭園／冬日花園露台，因整組庭園類場景已有 4 個，改提白樺林（理由見選擇理由）。 |
| H-rin-ayase（2月） | 夕陽中的高樓飯店套房，酒紅緞面垂墜領細肩長洋裝，側躺在深綠絲絨貴妃椅上望向窗外的夕陽。 | 斜躺全身｜側面斜躺（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側窗外的夕陽｜略高於她斜躺時頭部的高度・輕俯 | 保留酒紅緞面與斜躺；改為不看鏡頭、望向窗外夕陽；姿勢寫清楚：下方前臂撐椅墊、肩頸放鬆往後、腰側下凹臀線抬高、上方腿微彎搭在伸直的下方腿上、上方手放在大腿上。 |
| H-miu-shiraishi（3月） | 晨光灑進的一人公寓，象牙白蕾絲緞面細肩小可愛與短褲，背靠床頭的枕頭堆自然半倚、歪頭甜笑。 | 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 | 從端坐床邊、雙膝併攏雙手撐床，改為背靠枕頭的自然半倚（一膝立起、一腿伸直、手肘搭膝、另一手放床上），床改成斜放的對角線；服裝與晨光不變。 |
| H-tammy-chou（4月） | 春日花園露台的平整石板步道，熱粉色方領貼身針織洋裝配白色露跟高跟鞋，站在庭園長椅旁明亮地笑。 | 全身｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜膝蓋高度・輕仰 | 取消精品店：改成春日花園露台的平整石板步道（不踩泥地、碎石或沙灘），熱粉合身洋裝＋白色高跟鞋保留；手改為一手扶白色庭園長椅、一手插腰；拿掉手提包（素面小包放到直式款）。 |
| H-yerin-han（5月） | 春日球場的白色球車，白色無袖針織 polo＋淺藍百褶高爾夫迷你裙，坐在座椅邊緣微微後靠、伸長雙腿的俏皮笑容。 | 坐姿全身｜約45度斜側（朝畫面左）｜臉正面・看鏡頭｜坐姿時的腰部高度・平視 | 保留高爾夫迷你裙裝與球車；坐姿改為坐在座椅邊緣、身體微微後靠、後手撐座椅、前手放膝上，雙膝併攏、腳踝交叉、腳尖點地；相機維持坐姿腰部高度平視，不俯拍、不低角度。 |
| H-iris-chen（8月） | 夏日上午的淺色平坦岩岸海灣，向日葵黃有骨架的平口馬甲短上衣配同色低腰迷你裙，身體正面燦笑。 | 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰 | 全面換掉紅磚騎樓與米杏針織套裝：改成夏日上午的淺色平坦岩岸海灣、向日葵黃有骨架的平口馬甲短上衣＋同色低腰迷你裙；身體正面、笑容不變；手改成雙手放在低腰裙腰頭兩側；相機改為膝蓋高度輕仰。 |
| H-jia-seo（9月） | 初秋傍晚的湖畔木平台，黑色單肩貼身中長洋裝帶腰側鏤空與側開衩，側坐在臨水長椅上望向湖面。 | 坐姿全身｜側面（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側的湖面與遠岸｜坐姿時的腰部高度・平視 | 撤回美術館與畫作背景：改為初秋傍晚的湖畔木平台與臨水長椅；黑色單肩鏤空洋裝保留，加側開衩、鞋改低跟細帶涼鞋（木平台上較合理）；姿勢由側身站改為側坐、雙腿交疊；景別由全身改為坐姿全身；視線看向湖面。 |
| H-luna-tanaka（10月） | 新穎整潔的當代日式旅宿房間，香檳色斜裁緞面細肩洋裝，在榻榻米上單手撐地慵懶斜坐、望向窗外的紅葉。 | 席地坐姿全身｜約45度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側窗外的紅葉庭院｜坐姿時的胸口高度・平視 | 房間改成新穎整潔的當代日式旅宿（新榻榻米、乾淨木作、白色寢具），不再是古舊和室；服裝改為香檳色斜裁緞面細肩洋裝（仍是貼身緞面方向）；姿勢由端正側坐、雙手放腿上改為單手撐地的慵懶斜坐；視線看窗外紅葉。 |
| H-somi-oh（11月） | Penny 已接受的方向（R4 只改上衣穿法）：暖橘復古小吃店棚景，敞開的奶油色短開襟＋鏽橘貼身細肩小可愛＋高腰針織短裙，輕靠吧台大笑。 | 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜腰部高度・平視 | 短開襟不再全扣：改成「敞開的奶油色短開襟（全部不扣、從肩上垂下）＋鏽橘貼身方領細肩小可愛」兩層，衣物結構寫明；場景、光線、姿勢、大笑與構圖照 v4，不新增吃東西的動作。 |
| V-tammy-chou（1月） | 夜晚的大飯店大廳，白色西裝外套洋裝配素面黑色小手提包，一手拎包、一手插腰的自信笑容。 | 大腿中段以上｜正面｜臉正面・看鏡頭｜腰部高度・輕仰 | 加入素面黑色小手提包（不仿特定品牌）：一手拎包在臀側、一手插腰，包不遮胸腰；文案改正：這張是大腿中段以上，不再稱「全身照」；場景、服裝、景別、相機不變。 |
| V-jia-seo（2月） | 明亮的玻璃溫室，白色無袖立領短上衣配薄荷綠緞面高腰貼臀窄裙，斜側站在大葉植物之間，臀腰曲線清楚。 | 全身｜約45度斜側（朝畫面右）｜臉正面・看鏡頭｜臀部高度・平視 | 保留玻璃溫室；薄荷緞面中長裙改為高腰貼臀窄裙（腰頭在肚臍上方、貼臀往膝下收窄、左前側開衩到大腿中段）；景別由膝上改為全身、身體改為約45度斜側並把臀部往後側，讓輪廓真的看得出曲線；白色細帶涼鞋因全身入鏡寫回 prompt。 |
| V-miu-shiraishi（4月） | 春日度假別墅的木平台，杏桃色有骨架的細肩短洋裝，坐在白色帆布吊床邊，笑著看向開花的果樹。 | 坐姿全身｜約30度斜側（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側開滿白花的果樹｜坐姿時的腰部高度・平視 | 撤回運河與奶油 V 領針織裙：改為春日度假別墅木平台與白色帆布吊床，杏桃色有骨架的細肩短洋裝（配色與其他 23 套比較後選定）；姿勢由欄杆站姿改為坐在吊床邊、雙手抓布邊、微微前傾；不看鏡頭、看向開花的果樹；景別由大腿中段以上改為坐姿全身。 |
| V-rainie-hsu（5月） | 雨後的夜晚街道，黑色緞面繞頸迷你洋裝外搭黑色長皮風衣，看向前方的街燈，放鬆、微啟唇的沉思神情。 | 膝上｜約30度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側前方的街燈｜腰部高度・平視 | 保留雨後夜街與黑色服裝；改為不看鏡頭：看向前方街燈，表情改成放鬆、微啟唇、帶點沉思（不是橫式款的自信壞笑），臉不改；身體由側面改為約30度斜側；人物改到右側約六成，左側留給街燈。 |
| V-rin-ayase（10月） | 秋日午後的安靜港灣石砌碼頭，墨綠仿麂皮裹身洋裝，倚著木頭繫船柱望向港口。 | 膝上｜約45度斜側（朝畫面左）｜三分之二側臉・不看鏡頭：看畫面左側港口的出口與海面｜腰部高度・平視 | 撤回黑金高級吧台（最新意見取代先前選擇）：改成秋日午後的安靜港灣石砌碼頭，服裝改為墨綠仿麂皮裹身洋裝（深 V、繫帶收腰、前開衩）＋深棕踝靴；髮型改為鬆低髮髻；景別由坐姿全身改為膝上；不看鏡頭、望向港口。 |
| V-yuna-kim（11月） | 深秋的銀杏大道，奶油色毛呢短外套套裝配黑色長靴，停下腳步望向大道深處、手裡拿著一片銀杏葉。 | 全身｜約30度斜側（朝畫面右）｜三分之二側臉・不看鏡頭：看畫面右側銀杏大道的深處｜臀部高度・平視 | 保留銀杏大道與毛呢套裝；改為不看鏡頭：停下腳步望向右側大道深處，柔和若有所思的微笑；另一手改成指尖輕拿一片銀杏葉在腰側；不擺打卡姿勢。 |
| V-somi-oh（12月） | 下雪的溫泉小鎮夜晚，象牙白貼身針織洋裝外披紅色長大衣，抬眼看著燈籠旁飄落的雪，自然地笑開。 | 全身｜正面｜三分之二側臉・不看鏡頭：看畫面右上方燈籠旁飄落的雪｜臀部高度・平視 | 保留雪夜溫泉小鎮與冬季穿搭；改為不看鏡頭：抬眼看向右上方燈籠旁飄落的雪，一手攤開接雪，笑容由情境帶出；臉是三分之二側臉、眼睛睜開，不仰頭到看不清五官；人物改到略偏左。 |

主管推薦之外的選擇（附理由）：

- **H-Yuna**：主管推薦韓系冬季戶外；我選「雪後白樺林小徑」而不是庭園或街景，因為修訂後庭園類已有 4 套（Coco 花田、V-Luna 町家庭院、H-Tammy 花園露台、V-Miu 度假木平台），白樺林與其他 23 套都不重複，也和 V-Yuna 的銀杏大道（秋）分開季節。
- **V-Miu**：顏色選杏桃色，是 24 套裡沒有用過的顏色（程式檢查其他 23 套的 prompt 與中文都沒有 apricot／杏桃）。
- **V-Rin**：港灣碼頭配墨綠仿麂皮裹身洋裝；髮型改成鬆軟低髮髻配合戶外與風，臉與身材不變。

## 3. 8 套已接受：是否受影響

- 企劃內容：**不受影響**。8 套的主題、場景、服裝、姿態、表情、光線、攝影七欄位與 prompt 都與 v4 逐字相同（程式比對）。
- 印刷：8 套已接受的企劃內容都不需要為印刷改動；H-coco-wu、H-rainie-hsu 是橫式膝上，放入框後下緣會再往上移約 2–3 cm，生成後若接近膝蓋，4 mm 的裁切改由頭頂留白多取——這是後製裁切位置，不改服裝、場景、表情或 prompt，不列待確認。
- 印刷方面沒有任何已接受套數列為「待確認」。
- **技術備註（待主管確認，本輪未改動）**：已接受 8 套的服裝、場景、表情、攝影與 prompt 本輪都沒有改。複查中文與 prompt 時發現 3 套（V-iris-chen、H-coco-wu、V-coco-wu）的中文「妝感」有寫、英文 prompt 沒寫——Iris 與 Coco 的人設身分句沒有妝感，上一版（v4）就是如此。建議生成前在英文 prompt 補一句與中文相同的妝感（只補妝感，不改服裝、場景、表情或攝影），請主管確認；V-iris-chen 是 M-4 首試，若首試獲准，建議先補上。

| ID | 中文妝感（已接受） | 建議補進英文 prompt 的一句 |
|---|---|---|
| V-iris-chen | 乾淨的日常妝、自然唇色。 | Fresh, light everyday makeup with a natural lip colour. |
| H-coco-wu | 甜美淡妝、粉色唇。 | Sweet, light makeup with a pink lip. |
| V-coco-wu | 甜美淡妝。 | Sweet, light makeup. |

| ID | 月 | 景別｜身體方向｜臉與視線｜拍攝角度 | 印刷判斷 |
|---|---|---|---|
| H-coco-wu | 6 | 膝上｜約30度斜側（朝畫面右）｜臉正面・看鏡頭｜胸口高度・平視 | 不需改企劃（膝上的下緣會因上下裁切再往上移，生成後若接近膝蓋，4 mm 改由頭頂留白多裁） |
| H-mia-huang | 7 | 大腿中段以上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜胸口高度・平視 | 不需改企劃 |
| H-rainie-hsu | 12 | 膝上｜正面｜臉正面・看鏡頭｜腰部高度・平視 | 不需改企劃（膝上的下緣會因上下裁切再往上移，生成後若接近膝蓋，4 mm 改由頭頂留白多裁） |
| V-iris-chen | 9 | 大腿中段以上｜正面｜臉正面・看鏡頭｜胸口高度・平視 | 不需改企劃 |
| V-luna-tanaka | 6 | 全身｜正面｜臉正面・看鏡頭｜膝蓋高度・輕仰 | 不需改企劃 |
| V-coco-wu | 7 | 坐姿到水面｜正面｜臉正面・看鏡頭｜坐姿時的胸口高度・平視 | 不需改企劃 |
| V-mia-huang | 3 | 胸上｜約30度斜側（朝畫面右）｜三分之二側臉・看鏡頭｜眼睛高度・輕俯 | 不需改企劃 |
| V-yerin-han | 8 | 膝上｜約30度斜側（朝畫面左）｜臉正面・看鏡頭｜臀部高度・輕仰 | 不需改企劃 |

## 4. 整組節奏

- 橫式款：橫式款：大腿中段以上 2、膝上 3、全身 2、坐姿全身 3、席地坐姿全身 1、斜躺全身 1。戶外 8 套、室內 4 套；坐或躺的 5 套（Miu、Yerin、Jia、Luna、Rin）姿勢各不相同：床上靠枕半倚、球車座椅邊緣後靠、湖畔長椅側坐、榻榻米單手撐地斜坐、貴妃椅全身側躺。
- 直式款：直式款：胸上 1、大腿中段以上 2、膝上 3、全身 4、坐姿全身 1、坐姿到水面 1。戶外 10 套、室內 2 套；站姿置中只有 Tammy、Iris、Jia 三張，景別或角度各不相同。
- 近景：V-mia-huang 胸上；大腿中段以上 4 張（H-mia-huang、H-yuna-kim、V-iris-chen、V-tammy-chou）。沒有純臉部特寫，身材展示優先。
- 同一位的兩款：12 位中有 10 位的 H／V 景別不同；Rainie 兩款都是膝上（正面直視 vs 斜側看街燈），Miu 兩款都是坐姿全身（室內床上半倚看鏡頭 vs 戶外吊床邊看果樹）。每位的兩款在身體方向、相機高度或視線上至少一項不同。
- 橫式依月份：1月 大腿中段以上（Yuna）→2月 斜躺全身（Rin）→3月 坐姿全身（Miu）→4月 全身（Tammy）→5月 坐姿全身（Yerin）→6月 膝上（Coco）→7月 大腿中段以上（Mia）→8月 全身（Iris）→9月 坐姿全身（Jia）→10月 席地坐姿全身（Luna）→11月 膝上（Somi）→12月 膝上（Rainie）
- 直式依月份：1月 大腿中段以上（Tammy）→2月 全身（Jia）→3月 胸上（Mia）→4月 坐姿全身（Miu）→5月 膝上（Rainie）→6月 全身（Luna）→7月 坐姿到水面（Coco）→8月 膝上（Yerin）→9月 大腿中段以上（Iris）→10月 膝上（Rin）→11月 全身（Yuna）→12月 全身（Somi）

## 5. 印刷構圖核對

以下分成「已知」「假設」「未知」。已知值來自廠商編輯器設定與商品頁（R1 查證，本輪只重讀既有證據、沒有重查網站）；假設值是本案為了規劃先定的數字，不是廠商規格；未知要等廠商回覆或實際打樣。只有構圖方框不代表印刷安全。

### 5.1 已知

| 項目 | 橫式 | 直式 | 來源 |
|---|---|---|---|
| 成品尺寸（裁切線） | 200×151 mm | 140×200 mm | docs/calendar/CAL_01_SPEC_EVIDENCE.md §5；商品頁規格、編輯器狀態列 |
| 出血 | 四邊各 2 mm | 四邊各 2 mm | docs/calendar/data/vendor_editor_config_2026-10-08.json（bleedMargin） |
| 含出血畫布 | 204×155 mm | 144×204 mm | docs/calendar/CAL_01_SPEC_EVIDENCE.md §5（範本 SVG 尺寸換算） |
| 編輯器安全框 | 裁切線內 上 10、右 2、下 2、左 2 mm | 0 mm（四邊） | docs/calendar/data/vendor_editor_config_2026-10-08.json（safeMargin） |
| 編輯器影像解析度設定 | imageDPI 300 | imageDPI 300 | docs/calendar/data/vendor_editor_config_2026-10-08.json |
| 裝訂 | 黑色雙環線圈（在上緣） | 黑色雙環線圈（在上緣） | docs/calendar/CAL_01_SPEC_EVIDENCE.md §5；商品頁規格 |

### 5.2 假設（本案規劃用，不是廠商規格）

| 項目 | 橫式 | 直式 | 為什麼 |
|---|---|---|---|
| 線圈／裝訂區（規劃用） | 畫布上緣 0–12 mm | 畫布上緣 0–12 mm | 橫式＝出血 2＋廠商安全框 10；直式安全框是 0，不代表沒有裝訂區，所以沿用同一個 12 mm 假設（CAL_14 §1）。編輯器的線圈示意圖量得約 8.9 mm（橫）、9.7 mm（直），是量測值、不是廠商書面規格。 |
| 暫定照片框 | 畫布 (6,14)–(198,118)，192×104 mm | 畫布 (12,16)–(132,176)，120×160 mm | 版面還沒有 Penny 定案；照片框整個在安全區內、避開假設線圈區，所以照片本身不碰出血與裁切線。 |
| 日期區（暫定） | 畫布 (6,122)–(198,149) | 畫布 (12,180)–(132,200) | 只是示意位置；日期素材是廠商提供的點陣圖（CAL_01 §4）。 |
| 有效 ppi 工作目標 | 300 | 300 | 本專案自訂的工作目標，不是廠商門檻（廠商只公開「好／標準／差」三級，數字未知）。 |

### 5.3 未知

- 實際線圈尺寸、打孔位置與裝訂區（廠商書面規格）
- 廠商「好／標準／差」三級對應的 ppi 門檻
- soul_2 16:9 的實際輸出像素（推測 2048×1152，未驗證）
- 上傳 RGB 是否自動轉 CMYK、色差與暗部表現（要打樣）
- 拼版與背面是否自動旋轉（影響立架兩側看到哪兩面，CAL_01 §3.3）
- 最後選哪個版面（橫式大照片框或半版、直式 3:4 或統一框）——待 Penny 定案

### 5.4 照片框、比例裁切與示意圖

- 橫式：橫式大照片框（暫定），畫布座標 (6,14)–(198,118)，192×104 mm（約 1.85:1）；16:9 照片等比放入為 192×108 mm：上下各約 2 mm（照片高度的 1.9%），左右不裁。來源：R3 版型的「橫 B」192×104（CAL_14 §1）；M-3 企劃一直建議的橫式大照片框
- 直式：直式 3:4 照片框（暫定），畫布座標 (12,16)–(132,176)，120×160 mm（3:4）；3:4 照片等比放入為 120×160 mm：不裁切。來源：本輪提出：與 R3「直式統一框」同寬、同左右與上緣留白（12／16 mm），只把高度改成 3:4；月曆大格面另有一面
- 示意圖（只有方框與尺寸，不含照片；實線＝已知、虛線＝假設或暫定、點線＝照片比例示範）：
  - `/home/user/Virtual_KOL_Studio/docs/calendar/decision_site/public/print/layout_H.svg`（1304×886）→ 線上 https://cal2027-decision-production.up.railway.app/print/layout_H.svg
  - `/home/user/Virtual_KOL_Studio/docs/calendar/decision_site/public/print/layout_V.svg`（1064×1082）→ 線上 https://cal2027-decision-production.up.railway.app/print/layout_V.svg
  - 點陣預覽：`/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/print_layout_H.jpg`、`/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/print_layout_V.jpg`
- 產生示意圖的程式檢查：含出血畫布＝成品＋2×出血；照片框在安全區內、在假設線圈區下方；16:9 放入橫式框高 108 mm、上下各裁約 2 mm；3:4 放入直式框剛好不裁；R3 直式統一框 120×128 會讓 3:4 照片上下共裁 20%。

| 如果改用其他框 | 影響 |
|---|---|
| 若橫式改用 R3「橫 A 半版」104×155（直幅） | 16:9 橫幅照片不適用（要裁掉約七成寬度），必須另拍直幅——不從 16:9 硬裁。 |
| 若直式改用 R3「直式統一框」120×128（約 0.94:1） | 3:4 照片上下共要裁掉 32 mm（20%）：大腿中段以上會切到髮頂或腿、全身會切到腳——12 套直式款都要重排構圖。 |
| 若改成滿版出血照片 | 照片會進入假設線圈區（上緣 12 mm）與 2 mm 出血；背景延伸到出血區是正常的，但臉、髮頂、手腳與關鍵服裝要離開裁切線與線圈區，需要另外規劃餘量。 |

原則：

- 背景延伸到出血區是正常需求；臉、髮頂、手腳與關鍵服裝細節才要避開裁切與裝訂風險。
- 本輪的暫定照片框整個在安全區內，所以照片不碰出血線；真正會裁掉的只有「照片比例≠框比例」的部分（橫式 16:9→約 1.85:1，上下各約 2 mm）。
- 16:9 放進橫式框的 4 mm 裁切，原則上上下平均；若頭頂留白不足 4%，改從下緣多裁，反之亦然——以髮頂留白 ≥3%、下緣不落在膝或肘為準，生成後用實圖決定。
- 生成後仍須用實圖逐張確認裁切與有效 ppi；不預設 AI 放大或外擴已獲授權；不為安全餘量把人物縮小。

### 5.5 V-Iris 首試是否需要構圖微調

- 不需要構圖微調：直式 3:4 照片放進暫定的 3:4 框不裁切，髮頂留白約 7%、下緣在大腿中段，人物置中、雙手都在框內；prompt 不改。
- 前提是直式採 3:4 照片框。若 Penny 最後選 R3 的直式統一框（120×128，約 0.94:1），3:4 照片上下要共裁 20%，這張的髮頂與下緣都會被切到，需要重排構圖；所以建議在 M-4 首試前先確認直式照片框。
- 首試出圖後要用實圖確認：實際像素（預期 1536×2048）、髮頂與雙手是否在框內、有效 ppi（120 mm 寬約 325 ppi）。

### 5.6 24 套逐張判斷（依暫定照片框）

| ID | 狀態 | 比例裁切 | 邊緣的重要部位 | 不能切 | 需要的餘量 | 判斷 | 原生尺寸 | 有效 ppi |
|---|---|---|---|---|---|---|---|---|
| H-yuna-kim | R4 修訂 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 9%，放入框後約 7.3%；下緣：裁切線在大腿中段，放入框後往上移約 2 cm | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 已依印刷餘量規劃 | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| H-rin-ayase | R4 修訂 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 24%，放入框後約 22.9%；左右：頭與腳離左右邊緣各約 7% | 髮頂、臉、入鏡的雙手、頭與腳 | 放入框後：髮頂上方 ≥4%、左右各 ≥5% | 已依印刷餘量規劃 | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| H-miu-shiraishi | R4 修訂 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 9%，放入框後約 7.5%；下緣：雙腳下方留白約 7%，放入框後約 5.3% | 髮頂、臉、入鏡的雙手、雙腳 | 放入框後：髮頂上方 ≥4%、腳下 ≥3% | 已依印刷餘量規劃 | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| H-tammy-chou | R4 修訂 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 9%，放入框後約 7.2%；下緣：雙腳與鞋下方留白約 7%，放入框後約 5.3% | 髮頂、臉、入鏡的雙手、雙腳與鞋 | 放入框後：髮頂上方 ≥4%、腳下 ≥3% | 已依印刷餘量規劃 | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| H-yerin-han | R4 修訂 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 10%，放入框後約 8.4%；下緣：雙腳與鞋下方留白約 7%，放入框後約 5.3% | 髮頂、臉、入鏡的雙手、雙腳與鞋 | 放入框後：髮頂上方 ≥4%、腳下 ≥3% | 已依印刷餘量規劃 | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| H-coco-wu | 已接受 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 7%，放入框後約 5.0%；下緣：裁切線在膝蓋下方的小腿上段，放入框後往上移約 2 cm | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 不需改企劃（膝上的下緣會因上下裁切再往上移，生成後若接近膝蓋，4 mm 改由頭頂留白多裁） | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| H-mia-huang | 已接受 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 8%，放入框後約 5.9%；下緣：裁切線在大腿中段，放入框後往上移約 2 cm | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 不需改企劃 | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| H-iris-chen | R4 修訂 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 9%，放入框後約 7.6%；下緣：雙腳與鞋下方留白約 7%，放入框後約 5.3% | 髮頂、臉、入鏡的雙手、雙腳與鞋 | 放入框後：髮頂上方 ≥4%、腳下 ≥3% | 已依印刷餘量規劃 | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| H-jia-seo | R4 修訂 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 8%，放入框後約 6.7%；下緣：雙腳與鞋下方留白約 7%，放入框後約 5.3% | 髮頂、臉、入鏡的雙手、雙腳與鞋 | 放入框後：髮頂上方 ≥4%、腳下 ≥3% | 已依印刷餘量規劃 | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| H-luna-tanaka | R4 修訂 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 10%，放入框後約 8.6%；下緣：雙腳下方留白約 7%，放入框後約 5.3% | 髮頂、臉、入鏡的雙手、雙腳 | 放入框後：髮頂上方 ≥4%、腳下 ≥3% | 已依印刷餘量規劃 | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| H-somi-oh | R4 修訂 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 8%，放入框後約 6.4%；下緣：裁切線在膝蓋下方的小腿上段，放入框後往上移約 2 cm | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 注意：膝上的下緣會因上下裁切再往上移，生成後若接近膝蓋，4 mm 改由頭頂留白多裁 | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| H-rainie-hsu | 已接受 | 上下各約 2 mm（照片高度的 1.9%），左右不裁 | 上緣：髮頂留白約 8%，放入框後約 6.1%；下緣：裁切線在膝蓋下方的小腿上段，放入框後往上移約 3 cm | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 不需改企劃（膝上的下緣會因上下裁切再往上移，生成後若接近膝蓋，4 mm 改由頭頂留白多裁） | H 16:9：原生尺寸未知（推測 2048×1152，未驗證） | 若是 2048×1152：約 271 ppi（低於 300 工作目標，待驗證實際輸出） |
| V-tammy-chou | R4 修訂 | 不裁切 | 上緣：髮頂留白約 6%；下緣：裁切線在大腿中段 | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 已依印刷餘量規劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |
| V-jia-seo | R4 修訂 | 不裁切 | 上緣：髮頂留白約 9%；下緣：雙腳與鞋下方留白約 5% | 髮頂、臉、入鏡的雙手、雙腳與鞋 | 放入框後：髮頂上方 ≥4%、腳下 ≥3% | 已依印刷餘量規劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |
| V-mia-huang | 已接受 | 不裁切 | 上緣：髮頂留白約 9%；下緣：裁切線在胸線下方 | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 不需改企劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |
| V-miu-shiraishi | R4 修訂 | 不裁切 | 上緣：髮頂留白約 8%；下緣：雙腳與鞋下方留白約 5% | 髮頂、臉、入鏡的雙手、雙腳與鞋 | 放入框後：髮頂上方 ≥4%、腳下 ≥3% | 已依印刷餘量規劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |
| V-rainie-hsu | R4 修訂 | 不裁切 | 上緣：髮頂留白約 8%；下緣：裁切線在膝蓋下方的小腿上段 | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 已依印刷餘量規劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |
| V-luna-tanaka | 已接受 | 不裁切 | 上緣：髮頂留白約 9%；下緣：雙腳與鞋下方留白約 5% | 髮頂、臉、入鏡的雙手、雙腳與鞋 | 放入框後：髮頂上方 ≥4%、腳下 ≥3% | 不需改企劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |
| V-coco-wu | 已接受 | 不裁切 | 上緣：髮頂留白約 11%；下緣：水面下方留白約 8% | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 不需改企劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |
| V-yerin-han | 已接受 | 不裁切 | 上緣：髮頂留白約 7%；下緣：裁切線在膝蓋下方的小腿上段 | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 不需改企劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |
| V-iris-chen | 已接受 | 不裁切 | 上緣：髮頂留白約 8%；下緣：裁切線在大腿中段 | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 不需改企劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |
| V-rin-ayase | R4 修訂 | 不裁切 | 上緣：髮頂留白約 7%；下緣：裁切線在膝蓋下方的小腿上段 | 髮頂、臉、入鏡的雙手 | 放入框後：髮頂上方 ≥4% | 已依印刷餘量規劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |
| V-yuna-kim | R4 修訂 | 不裁切 | 上緣：髮頂留白約 8%；下緣：雙腳與鞋下方留白約 5% | 髮頂、臉、入鏡的雙手、雙腳與鞋 | 放入框後：髮頂上方 ≥4%、腳下 ≥3% | 已依印刷餘量規劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |
| V-somi-oh | R4 修訂 | 不裁切 | 上緣：髮頂留白約 10%；下緣：雙腳與鞋下方留白約 5% | 髮頂、臉、入鏡的雙手、雙腳與鞋 | 放入框後：髮頂上方 ≥4%、腳下 ≥3% | 已依印刷餘量規劃 | V 3:4：原生 1536×2048（已知） | 約 325 ppi（1536 px／120 mm） |

本輪沒有任何一套需要為印刷改 prompt；橫式膝上的 3 套（H-somi-oh、H-coco-wu、H-rainie-hsu）只標注生成後裁切位置的注意事項。

## 6. 自測結果

| 項目 | 結果 | 檔案 |
|---|---|---|
| 企劃頁（桌機＋390px）與資料：24 套 ID、兩本月份與確認排序相同；8 套已接受與 v4 逐欄相同；16 套 owner 要求逐項（英文 prompt 與中文欄位都比對）；七欄位英文在 prompt；16 套妝感中英逐項一致、身分句與 v4 相同；已接受 3 套技術備註只列不改並顯示在卡片；同人兩款不同、24 個環境不重複；不看鏡頭與戶外都比 v4 多；無幼態字眼；印刷已知尺寸、照片框座標、16:9／3:4 裁切計算、24 套逐張判斷、兩張示意圖尺寸與內容；公開資料 v5、無 Soul ID／job_id／repo 路徑、免登入、SVG 以 image/svg+xml 提供；頁面狀態標示、R4 改了什麼、月份已確認、攝影四格直接可見、構圖示意、總覽與修訂表、印刷區與放大檢視；v1–v4 舊回饋保留並標「不算 v5」；回饋保存、重新整理、複製；清除 v5 只刪 v5；素材選擇不變；圖片載入、手機表格改小卡、無水平溢出、無 JS 錯誤 | 線上 146/146（本機 146/146） | /home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_shoot_v5_tests.tsv、local_shoot_v5_tests.tsv |
| 真實升版：同一個測試瀏覽器設定檔先在線上 v1–v4 各填回饋（最後在 8f061fc 填 v4），再打開線上 v5 | 14/14（localStorage 位元組相同；v1–v4 顯示為舊版；v5 為 0／16；只開頁不改寫） | /home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_upgrade_v4_to_v5.tsv |
| 線上檔案 sha256 與本機比對（圖片、資料、頁面程式、兩張印刷示意，加 4 個 HTML 頁） | 666 檔，不符 0；四個 HTML 頁與本機相同（頁面版本 4f15917） | /home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_bytes_check.txt |
| 網站建置器 --check | PASS：654 檔，問題 0；ASSET_MANIFEST.json 與上一版位元組相同 | — |
| 文件產生器 --check | PASS；CAL_19 與上一版位元組相同 | — |
| kol-catalog 首頁 | 與上一輪存檔位元組相同（44801 bytes） | /home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_bytes_check.txt |

產生資料與測試時的修正（照實記錄）：

- **已部署後才發現、已修正並重新部署**：攝影總覽的「戶外」說明寫成「R3 是 15 套」並把 H-Iris、V-Miu 算成新增戶外；v4 資料其實是 14 套，室內改戶外的是 H-Yuna、H-Tammy、H-Jia、V-Rin 四套，H-Iris 與 V-Miu 原本就在戶外、只換場景；針織服裝是 6 套不是 7 套。改成由資料計算（commit `9fa1343`），重新部署後所有線上測試重跑。
- 產生程式的檢查：V-somi 的身體與頭部扭轉是負值，原本的上限檢查沒有取絕對值（改成 |扭轉| ≤ 60）；胸上與腰上景別被誤報左右邊距不足（這兩種景別不檢查左右）；近景套數的說明原本寫死（改成計算）。
- 印刷逐張判斷：赤腳的套數原本也寫「雙腳與鞋」，泳池套沒有水面標示——都改正。
- 示意圖：標題壓到尺寸文字、圖例換行不佳（加上邊距、圖例在 25 字處換行、加上裁切標示與直式安全線）。
- 頁面測試本身的錯誤（不是頁面問題）：owner 段落用錯資料型別、「小吃店」的「吃」誤中「不吃東西」檢查、V-Tammy 的「改了什麼」本來就寫「不再稱『全身照』」、複製文字的人名是 Jia／Rin 不是全名、sophia 檢查應只看企劃資料（素材候選名單本來就有 sophia-tseng）——都改正測試後全數通過。
- 手機版：狀態標籤在小卡表格裡被拉滿整列，部署前改成靠左。
- **送審後複查發現、已修正並重新部署**：R4 指令再次送來，我逐字對照後發現中文「妝感」和英文 prompt 不一致——H-Yuna 中文寫玫瑰漸層唇、人設身分句是珊瑚漸層唇；H-Iris、H-Somi、V-Somi 的妝感只寫在中文（人設身分句沒有妝感）。上一版的測試只比對攝影七欄位，沒有比對妝感。修正：H-Yuna 中文改為珊瑚；三套另加一句英文妝感（身分句本身不改）；已接受的 V-iris、H-coco、V-coco 有同樣缺口，prompt 不改、列技術備註待主管確認。測試新增妝感、身分句與技術備註檢查（commit `4f15917`）。

## 7. 截圖與覆核檔案（完整路徑）

截圖都來自線上企劃頁（4f15917）；`oldfb_` 開頭的是帶 v1–v4 測試回饋的畫面，`upgraded_` 開頭的是真實升版後的畫面，`print_layout_` 是示意圖的點陣預覽。

- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_books_months_confirmed.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_card_H-iris_camera_detail.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_card_V-rin_camera_detail.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_coco_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_iris_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_jia_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_luna_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_mia_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_miu_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_photo_overview_with_changes.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_print_diagrams.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_print_section.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_print_viewer_H.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_r4_decisions.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_rainie_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_rin_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_somi_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_tammy_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_yerin_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_desktop_yuna_HV.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_mobile390_card_H-iris_revised.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_mobile390_card_H-jia_revised.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_mobile390_card_V-iris_accepted.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_mobile390_card_V-miu_revised.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_mobile390_changes_table.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_mobile390_print_diagrams.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_mobile390_print_row_H-iris.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_mobile390_status.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_mobile390_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/oldfb_live_desktop_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/oldfb_live_desktop_iris_with_old_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/oldfb_live_desktop_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/oldfb_live_mobile390_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/oldfb_live_mobile390_iris_with_old_feedback.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/oldfb_live_mobile390_top.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/print_layout_H.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/print_layout_V.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/upgraded_feedback_section_v5.jpg`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/upgraded_jia_old_feedback_v5.jpg`

覆核檔案：

- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_shoot_v5_tests.tsv`、`/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/local_shoot_v5_tests.tsv`、`/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_upgrade_v4_to_v5.tsv`、`/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/live_bytes_check.txt`
- `/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/copy_example_unanswered_with_old.txt`、`/home/user/Virtual_KOL_Studio/review/calendar/m3_r4/copy_example_answered.txt`（測試用假回饋的複製結果）
- `/home/user/Virtual_KOL_Studio/docs/calendar/data/cal_m3_shoot_plan.json`、`/home/user/Virtual_KOL_Studio/docs/calendar/data/cal_m3_owner_feedback_r4.json`、`/home/user/Virtual_KOL_Studio/docs/calendar/CAL_18_M3_SHOOT_PLAN.md`
- `/home/user/Virtual_KOL_Studio/docs/calendar/decision_site/public/print/layout_H.svg`、`/home/user/Virtual_KOL_Studio/docs/calendar/decision_site/public/print/layout_V.svg`

## 8. 操作紀錄

| # | 動作 | 性質 |
|---|---|---|
| 1 | 定向讀：本輪指令、上一版企劃資料（git 8f061fc）、R3／R2 owner 紀錄、規格證據（CAL_01 §4–5、vendor_editor_config_2026-10-08.json、CAL_14 §1、CAL_10）、企劃頁程式、文件產生器、網站建置器的 M-3 段落；沒有掃描整個 repo、沒有重查廠商網站 | 唯讀 |
| 2 | 在線上 v4 頁（8f061fc）用測試瀏覽器設定檔（已有 v1–v3 回饋）再填 v4 測試回饋，供升版測試 | 只在本機測試瀏覽器；不影響 Penny 的瀏覽器 |
| 3 | 本機產生 R4 owner 紀錄、shoot-plan-v5、兩張印刷示意 SVG、CAL_18；建置網站資料並 --check；本機伺服器測試與截圖 | 本機 |
| 4 | commit 13fa4a0，push 到 claude/epic-carson-n5w0qu；Railway 只把 cal2027-decision 固定到 13fa4a0（681f0e98）並做線上驗證 | 未合併 main、未開 PR |
| 5 | 發現戶外／針織套數說明有誤，修正後 commit 9fa1343、push，cal2027-decision 改固定到 9fa1343（dbb82db5），線上全部測試重跑；送審 commit 4cb57ba | 其他 service 未動、沒有新增付費服務 |
| 6 | R4 指令再次送來；逐字複查後修正妝感中英不一致，commit 4f15917、push，cal2027-decision 改固定到 4f15917（a57e31f0-2478-4b22-a028-6adcbed2e56b） | 其他 service 未動 |
| 7 | 線上升版驗證、頁面測試、檔案比對、截圖；讀 kol-catalog 首頁比對 | 唯讀 |
| 8 | 更新本送審紀錄並 commit、push | — |

**本輪數字：** 生成 0、credits 0、訓練 0、上傳 0、Higgsfield 呼叫 0、聯絡廠商 0、登入 0。V-Iris 費用未核准，不執行 M-4。
