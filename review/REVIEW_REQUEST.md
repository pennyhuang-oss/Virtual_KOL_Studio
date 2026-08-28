# 覆核請求 R9：8 件公共場景補上背景路人（長度已超出已驗證範圍）

> ⚠️ **請只讀這一個檔案**，不要瀏覽目錄或讀 repo 背景。判斷所需內容已全部貼在下面。
> 回覆填在最後的「回覆區」，不要改問題本文。

## 發生了什麼

使用者問「之前小雪莉（@sherry_digitalp510）帳號的素材分析有沒有納入」，我去核對後發現：
**13 段 prompt 全部沒有背景路人。**

我們自己的 `SEXY_SCENE_LIBRARY.md` §9 早就寫了規則，**而且是同一個模型（soul_2、quality 2k）上
14/14 實測過的**（7 位角色各 2 張，全部成功產生自然背景人物、無配角撞臉主角、成本為零）。
規則原文：公共場景「空無一人本身就是最強的『這是合成的』訊號」。

漏掉的原因很具體：R7／R8 那幾輪的議題是手部任務與光線，**這條不在任何一輪的問題清單裡**。

現已把 §9 的四條件措辭**逐字**加進 8 件公共場景（下面全文）。

## 需要你判斷的兩個刻意例外

### ① 這段措辭含 `never`，撞到我們自己的否定句規則

已驗證結論 D-03：`soul_2` 沒有 negative prompt 欄位，否定句無效（`no open sky` 被完全無視）。
但 §9 這段 14/14 成功的措辭裡有 `never looking at the camera`。

**我的判斷**：D-03 說的是「無效」不是「有害」；整段是驗證過的，
改寫它等於**引入新變因換取零已知收益**。所以保留原文，只在 lint 檢查前把它切掉。
**這樣對嗎？還是應該改成正面寫法（例如 `their faces turned away from the camera`）並重新驗證？**

### ② 長度從 ~120 字變成 155–160 字，超出任何已驗證範圍

原本的 120 字上限，我查了一遍**沒有實證來源**，是啟發式；
已核准的 8 件成品落在 94–118 字。加上這 40 字的區塊後，公共場景變成 155–160 字。

我把上限改成「只管自己寫的內容，固定區塊另計」，但這只是記帳方式的改變——
**155–160 字這個長度本身沒有任何一張成功成品背書。**

**風險**：長 prompt 可能稀釋前段的動作與手部指令（那正是這批最脆弱的部分）。
**是否應該先用 1 件做長度 preflight，而不是 8 件一起放行？**

---
## YG-06｜汗蒸幕・甜米露

**全身（坐姿）。**　|　人物入鏡：公共場景——必寫背景路人（汗蒸幕休息大廳）

- **硬驗收**：① 雙手捧紙杯在**下巴前**（不是胸前）② 越過杯緣看向鏡頭 ③ 盤腿坐姿、全身入鏡 ④ 頭上毛巾羊角可見

```text
A young woman sits cross-legged on a heated wooden floor, cupping a paper cup of sweet rice punch in both hands in front of her chin, her eyes peeking over the rim toward the camera, crinkled into crescents. Full body, camera at her seated eye level, shot from well back. Collarbone-length mocha brown hair in a low bun, two damp strands at her temples. A grey sauna tee and shorts, a towel folded into sheep horns on her head, bare feet. A bright sauna rest hall with low tables. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm ceiling light on her face, the wooden floor bouncing warm fill up onto her chin, the hall behind her staying readable and slightly darker. Natural skin texture, subtle film grain.
```

## YG-08｜台式早餐店・第一則吃

**半身，人＋食物同框。**　|　人物入鏡：公共場景——必寫背景路人（早餐店）

- **硬驗收**：① **單手**拿蛋餅咬 ② 另一手比大拇指 ③ 人與食物同框 ④ 襯衫下擺在腰際打結、露一截腰

```text
A young woman bites into an egg crepe held in one hand and throws a thumbs up with her other hand, nose scrunched, eyes crinkled. Half body with the food in frame, camera level with her chest. Collarbone-length soft wavy mocha brown hair, side-parted, a small pearl clip on one side. A light blue short-sleeve shirt knotted at the waist, white high-waisted shorts. A breakfast shop, a stainless steel counter, red plastic stools, iced tea in a tall glass. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the steel counter bouncing fill onto her chin. Her face is clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## YG-10｜百貨美妝櫃・精緻的一面

**半身。**　|　人物入鏡：公共場景——必寫背景路人（百貨美妝樓層）

- **硬驗收**：① 試色的手背舉在臉旁 ② **臉部區域只有一隻手** ③ 風衣掛在另一側前臂 ④ 半身比例

```text
A young woman holds the back of one swatched hand facing the camera beside her face, her other arm relaxed at her side with a trench coat draped over that forearm, one eyebrow raised, the same corner of her mouth lifted. Half body, camera level with her chest. Sleek glossy collarbone-length mocha brown hair, side-parted, ends curving slightly inward. A cream cropped fitted knit top, matching off-white high-waisted straight trousers, gold hoop earrings. A department store beauty floor, glass counters, rows of lipsticks, glossy pale columns. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool recessed ceiling light on her face, warm accent light inside the glass cases, the white counter bouncing fill onto her chin, the floor behind her slightly darker. Natural skin texture, subtle film grain.
```

## LG-05｜公車站・雨停前

**景別到小腿中段**（2026-08-29 由膝上放寬，理由見硬驗收）。　|　人物入鏡：公共場景——必寫背景路人（公車站）

- **硬驗收**：① 一手握收起的透明傘、**整把傘含傘尖可見、朝下貼在腿側**（不可浮空）② 另一手在臉頰旁比 V ③ 襯衫扣到胸口、不露 ④ 景別到**小腿中段**

```text
A young woman stands at a bus shelter, one hand gripping the handle of a folded clear umbrella, its entire closed canopy and downward-pointing tip visible beside her leg, her other hand making a V beside her cheek, head tilted. Framed down to mid-calf, camera at her navel level, shot from well back. A blunt chin-length black bob with even blunt ends along the jawline. An off-white cotton button-front blouse fastened through the chest, a pale blue checked skirt with one continuous hem. A route map lightbox, wet asphalt throwing warm sign colour back up. Her face is clearly exposed with natural skin texture; the signs are the brightest area, only their smallest highlights reaching white. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Subtle film grain.
```

## LG-06｜可愛系街區・扭蛋機前

**半身。**　|　人物入鏡：公共場景——必寫背景路人（扭蛋店門口人行道）

- **硬驗收**：① 雙手捧扭蛋在胸前 ② 頭朝扭蛋低下 ③ 眼睛瞇起／閉起笑（**與「看鏡頭」互斥，不可並存**）④ 半身比例

```text
A young woman holds an opened gachapon capsule in both hands at chest level, her head angled down toward it as she laughs with her eyes squeezed shut. Half body, camera level with her chest. A blunt chin-length black bob cut evenly at the jawline, two small clips holding her fringe back. A pale pink cropped knit top showing a sliver of waist, white high-waisted shorts, a denim jacket tied at her waist. A row of colourful gachapon machines behind her, storefront signage well out of focus. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Soft daylight on her face, her face evenly exposed, the coloured machine panels throwing a little colour onto her arms, the machines behind her staying slightly darker. Natural skin texture, subtle film grain.
```

## LG-07｜遊樂園・旋轉木馬

**全身。**　|　人物入鏡：公共場景——必寫背景路人（遊樂園）

- **硬驗收**：① 兩手從左右托住桶、上緣在下巴下方 ② 越過桶緣看鏡頭 ③ 骨盆斜向離開鏡頭、肩線轉向鏡頭 ④ **完整的腳落在畫面下方 1/3 之內**

```text
A young woman stands in a gentle three-quarter back pose, hips angled away and shoulders turned toward the camera. She supports a popcorn bucket from both sides with exactly two visible hands, its upper rim just below her chin, looking over the rim with a playful smile. Full body, camera at her navel level, shot from well back, her complete feet within the bottom third of the frame. A blunt chin-length black bob cut evenly at the jawline, a cat-ear headband. A white square-neck puff-sleeve top, a pale blue pinafore skirt. A carousel behind her, coloured balloons. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight on her face, warm carousel bulbs behind, the pale ground bouncing fill onto her chin. Natural skin texture, subtle film grain.
```

## LG-09｜台式早餐店・豆漿

**半身，人＋食物同框。**　|　人物入鏡：公共場景——必寫背景路人（早餐店）

- **硬驗收**：① 雙手捧杯在**下巴前**（不是胸前）② 頭略低、眼睛往上看鏡頭 ③ 人與豆漿杯同框 ④ 半身比例

```text
A young woman holds a glass of soy milk in both hands in front of her chin, head slightly lowered, eyes looking up over the rim toward the camera. Half body with the glass in frame, camera at her eye level. A blunt chin-length black bob cut evenly at the jawline, centre-parted. A cream fitted thin-knit top with a clear waistline. A breakfast shop, a steel counter, red plastic stools, the wall menu out of focus. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

## LG-10B｜浴衣・蘋果糖（半身）

**半身。**　|　人物入鏡：公共場景——必寫背景路人（祭典參道，規格表原本就寫了「遠處的人群」）

- **硬驗收**：① 一手舉蘋果糖在臉頰旁 ② 另一手扶髮簪 ③ 浴衣**左襟在上**、半幅帶綁緊收腰 ④ 半身比例

```text
A young woman holds a candy apple up beside her cheek with one hand and steadies the hairpin in her half-up bob with her other hand, laughing with her eyes crinkled. Half body, camera level with her chest. A blunt chin-length black bob cut evenly at the jawline, half-pinned up with a Japanese hairpin, two strands at her temples. A pale-blue floral yukata with the wearer's left front panel layered over the wearer's right, a wide flat navy obi. Paper lanterns overhead. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm lantern light on her face, the approach underfoot bouncing warm fill up. Her face is clearly exposed with natural skin texture; the lanterns are the brightest area, only their smallest highlights reaching white. Subtle film grain.
```

---

## 回覆區（請只填這一段）

### ① never 要保留原文還是改正面寫法
- **判定**：PASS（保留已驗證原文）
- **理由**：D-03 能支持的是這個否定片段未必具有約束力，不能推導它會傷害整段；而目前唯一直接實證是這個完整區塊在同模型上 14/14 成功。區塊前面已有正面可視關係 `backs turned or heads angled away`，所以即使 `never` 被忽略，主要控制訊號仍在。為了清除一個可能無效但已知無害的片段而改寫整段，現階段確實是引入未驗證變因。
- **建議改法**：本批保留原文。不要在 lint 執行前把它從待檢文字切掉，因為那會讓檢查結果與實際送出的 prompt 不同；應對這一段精確的已驗證字串建立具名 allowlist／例外，其他否定詞仍照常阻擋。日後若要改成全正面句，另做單變因驗證，不要與本次長度變更同輪發生。

### ② 155–160 字要不要先做長度 preflight
- **判定**：REVISE（先做 preflight，不放行 8 件整批）
- **理由**：120 字不是實證上限，因此不能直接判 160 字會失敗；但本次同時把 40 字固定區塊加入 8 個含脆弱手部／視線任務的 prompt，且沒有任何 155–160 字成品證據。把固定區塊「另計」只改變統計口徑，不會降低模型實際讀到的長度或注意力競爭。單張成功也只能當冒煙測試，不能證明整批成功率。
- **建議改法**：先以 LG-07 完整長版做 2 張 preflight，因為它同時具有全身、轉體、雙手托桶與視線四項高風險條件；兩張都先驗主體動作與手數，再驗路人。若任一張前段任務失敗，再以同 seed／同設定做「有路人區塊 vs 移除該區塊」最小 A/B，才能判斷是不是長度／後段稀釋，而不是姿勢本身。通過後分批送其餘 7 件，不把一張成功當成 8 件全放行證據。

### YG-06
- **判定**：PASS ／ REVISE ／ BLOCK → PASS
- **理由**：路人被限定在中景、失焦並各自活動，和前景盤腿全身、雙手捧杯沒有空間或任務衝突；公共汗蒸幕休息廳加入少量人物也符合場景邏輯。主體動作仍位於 prompt 最前段。
- **建議改法**：逐件內容可保留；待全批長度 preflight 通過後送。驗收路人時不可因背景人物的手入鏡而誤判主角多手，主角與背景人物的肢體需分開計數。

### YG-08
- **判定**：PASS ／ REVISE ／ BLOCK → PASS
- **理由**：半身前景主角與中景食客能自然分層，路人區塊沒有新增主角手部任務，也沒有改動單手拿蛋餅、另一手比讚的互斥關係。早餐店本來就需要一定人流才不顯得合成。
- **建議改法**：內容可保留；待長度 preflight 通過後送。硬驗收仍只計主角的兩隻手。

### YG-10
- **判定**：PASS ／ REVISE ／ BLOCK → PASS
- **理由**：百貨美妝樓層加入中景顧客合理，且 `softly out of focus` 能把配角降為場景訊號。主角兩側手臂的任務已在前段清楚分配，不會因路人描述本身產生第三個主角手部任務。
- **建議改法**：內容可保留；待長度 preflight 通過後送。驗收「臉部區域只有一隻手」時只看主角，但若背景人物的手在透視上貼到主角臉旁，仍應判構圖失敗而非忽略。

### LG-05
- **判定**：PASS ／ REVISE ／ BLOCK → PASS
- **理由**：放寬至小腿中段後，整把傘與傘尖已有足夠畫面空間；路人位於中景，不會在文字規格上與傘的前景錨點競爭。公車站出現候車者也符合公共場景規則。
- **建議改法**：內容可保留；待長度 preflight 通過後送。成品仍須確認背景路人沒有遮住傘尖，否則硬驗收①不成立。

### LG-06
- **判定**：PASS ／ REVISE ／ BLOCK → PASS
- **理由**：主角低頭閉眼看扭蛋的方向已明確，路人的 `never looking at the camera` 不會與主角視線形成矛盾。半身前景與人行道中景亦可共存，沒有新增手部競爭。
- **建議改法**：內容可保留；待長度 preflight 通過後送。若文字成品規則要求零可辨文字，`storefront signage well out of focus` 必須實際保持不可讀，但這不阻擋本輪人物配置。

### LG-07
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：加入路人本身可行，也最適合作為長度閘門；但本版把上一輪明確的視線目標刪成 `looking over the rim with a playful smile`，沒有 `toward the camera`。硬驗收②要求看鏡頭，現句只保證越過桶緣看，可能看向畫外。這與路人區塊的 `never looking at the camera` 同時存在時，主角視線更不應留給模型自行補。
- **建議改法**：把第一段末尾改回 `looking over the rim toward the camera with a playful smile`。其餘路人與姿勢句可保留；修後用本件完整長版做 2 張 preflight，再決定是否放行其餘 7 件。

### LG-09
- **判定**：PASS ／ REVISE ／ BLOCK → PASS
- **理由**：早餐店中景路人與半身主體層次合理；雙手捧杯、杯在下巴前、低頭抬眼的核心任務仍集中在第一句，沒有被背景人物改寫。路人也不會在規格上引入第三個主角手部任務。
- **建議改法**：內容可保留；待長度 preflight 通過後送。驗收時需排除背景肢體在透視上與主角杯緣／手部黏連的成品。

### LG-10B
- **判定**：PASS ／ REVISE ／ BLOCK → PASS
- **理由**：祭典參道原規格已有遠處人群，現在只是把人物行為、焦點與差異化條件具體化；半身主角的一手蘋果糖、一手髮簪仍在最前段且互不競爭。路人區塊與祭典光線也沒有語意衝突。
- **建議改法**：內容可保留；待長度 preflight 通過後送。背景人物不得在主角臉旁形成看似第三隻手的輪廓，否則仍應重跑。

### 其他（只寫會導致生成失敗的項目）
- 8 件共用的路人區塊雖有 14/14 證據，但「加入目前這批 155–160 字完整 prompt 後仍不稀釋前段任務」尚未被驗證；因此上述逐件 PASS 是內容層級通過，不等於略過 LG-07 長度閘門直接整批送出。
