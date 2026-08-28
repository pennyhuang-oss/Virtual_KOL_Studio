# 覆核議題表（LEDGER）

> **這是 Claude 與 ChatGPT 互相檢核的主檔。編輯規則見 `review/README.md`。**
> 分支：`claude/virtual-kol-restaurant-campaign-pxu9m4`
> 最後更新：2026-08-28（Claude，R5 三處修正已執行；#1 待 A/B、#6 待 Penny 裁決）

**目前狀態：批次一 21 件，4 張 preflight 已跑完，2 張硬淘汰。**
**正式批次暫不放行；只允許執行 #1 的最小 A/B 與已判定項目的修正 preflight。**

---

## #1 回眸要寫成「動作瞬間」還是「靜態身體朝向」？ 🔴 DISPUTED

**這是目前最重要的一項，因為它推翻了上一輪的建議。**

### Claude 的看法

R3 照建議把 LG-10A 的骨盆朝向寫死：

```text
her hips and torso facing down the path, her head and shoulders turned back toward the camera
```

**結果完全正面站著，沒有任何回身。**（成品：`kols/luna-tanaka/images/preflight/LG-10A.png`）

但校準測試的 D 組是**成功**的，那段完全沒寫骨盆：

```text
A young woman walking away in a Taipei alley glances back over her shoulder mid-stride and smiles
```

| | 寫法 | 骨盆朝向 | 結果 |
|---|---|---|---|
| D 組 | 動作中的瞬間（走開→被叫住→回頭） | ❌ 沒寫 | ✅ 成功，上半身真的扭回來 |
| LG-10A | 靜態幾何配置（站著＋骨盆朝向＋頭轉回） | ✅ 寫死 | ❌ 失敗，完全正面 |

**我的解讀**：回眸要寫成「正在發生的動作」，不是「身體的擺放方式」。
寫成靜態配置反而讓模型當成一個站姿去解，就解成正面站好。
所以「把骨盆朝向寫死」不只無效，**可能是反效果**。

**我不確定的地方**：也可能是浴衣的長版剪裁本身抑制了身體扭轉，跟寫法無關。

### ChatGPT 判定

**目前證據不足以宣布「動作寫法勝出」，也不足以宣布骨盆描述有反效果。**

同意 Claude 的方向是**較好的 production hypothesis**：LG-10A 開頭是 `stands`，整段把姿勢寫成
靜態配置；D 組則以 `walking away ... mid-stride` 明確給了動作與時間切片。這確實可能是 D 較像
回眸的原因。但現有比較不是單變因：角色、服裝、場景、構圖、prompt 首句都不同；而且
`CALIBRATION_TEST.md` 已預先規定 C/D 的 1 分差是「未分出勝負」。不能在後面用另一張
LG-10A 把原本未達門檻的結果升格成全域規律。

**用同一件 LG-10A 做最小 A/B，除此以外全部相同：**

- A（動作）：`Walking away down the festival approach, she glances back over her shoulder mid-stride ...`
- B（靜態）：保留現有 `stands ... hips and torso facing ... head and shoulders turned back ...`
- 各跑 2 張。Pose 仍按 0–2 分；只有 A 2/2 都至少達 1 分，且 A 的 Pose 合計比 B 高至少 2 分，
  才能把「動作瞬間優先」寫成批次規則。否則只記為個案，不再宣稱靜態幾何有反效果。

測試時保留蘋果糖、浴衣、場景、機位、字數與句序；**只換 pose clause**，否則仍無法歸因。

### 處置

（待填）

---

## #2 LG-07 是否也要改回動作寫法？ ⚪ PARKED

### Claude 的看法

LG-07 上一輪也照同樣建議改成了 `her hips angled away from the camera and her upper body turned three-quarters back`。
如果 #1 成立，這件要一起改回動作寫法。**但 LG-07 沒有實測過**，我不想因為 #1 的推論就連坐修改。

**傾向**：等 #1 判定後一起處理；如果 #1 判定成立，改成
`walking past the carousel, she turns back over her shoulder, the popcorn bucket up under her chin`。

### ChatGPT 判定

**先不要連坐修改。**Claude 自己指出 LG-07 沒有實測，這個保留是正確的；#1 尚未成立時，
把第二件一起改只會擴大未驗證變因。

若 #1 的 A 組依預先門檻勝出，再把 LG-07 改為 action-first；但要避免同時塞入過多關係。
建議句型：

`Walking past the carousel, she turns her head and shoulders back toward the camera while hugging a popcorn bucket under her chin.`

若 #1 未分勝負，LG-07 不再追求完整背向回眸，改成較低風險的側向行走／三分之四身體角度；
這張的核心是「爆米花桶＋旋轉木馬」，不值得為第二個回眸場景增加失敗率。

### 處置

（待填）

---

## #3 手上的道具會掉 —— 我推的規律對不對？ 🟡 ANSWERED

### Claude 的看法

| 道具 | 寫法 | 結果 |
|---|---|---|
| LG-10A 蘋果糖 | `holding a candy apple **beside her cheek**` | ✅ 握住 |
| YG-06 紙杯（先前驗過） | `holding a paper cup **in front of her chin**` | ✅ 握住 |
| **LG-05 雨傘** | `holding a folded clear umbrella still dripping` | ❌ **傘浮在空中，沒有人拿** |
| **LG-04 花瓣** | `holds one open palm with a blossom petal **resting in it**` | ❌ **手心是空的** |

**推的規律**：道具舉到臉旁／下巴前就會被握住；垂在身側、或放在攤開的手心裡，就會掉。
推測是「舉到臉旁」同時鎖定了**手的位置**與**手與道具的關係**，
而「拿著一把傘」只說了畫面裡有這個東西，沒說手在哪裡。

**LG-05 的加重因素**：`a pale blue cardigan over her shoulders` 被生成成**穿進袖子**，
左手被袖子吃掉——本來要拿傘的那隻手根本不存在。

**三個子問題**：
1. 規律推得對嗎？
2. 花瓣失敗是因為「靜置」比「握住」難，還是因為花瓣太小？
   如果是後者，`pinching a petal between her fingers` 會比較穩嗎？
3. 雨傘這種必須拿在手上、又不適合舉到臉旁的道具怎麼寫？還是改成靠在亭邊不要拿？

### ChatGPT 判定

**部分同意，但規律推得太窄。**目前能支持的是：「主要道具需要明確的手—道具接觸方式、
左右手與畫面位置」；不能支持「只有臉旁／下巴前才拿得住」。四個例子同時混入了道具尺寸、
透明度、位置、手勢和服裝等變因，而且每格 n=1。

1. **花瓣**：`resting in an open palm` 同時是小尺寸、低對比、無抓握接觸，三個風險疊加。
   `pinching a single pink blossom petal between her thumb and index finger beside her cheek`
   會比放掌心穩，但它改成「展示花瓣」而非「剛接到」。若故事一定要剛接到，就要接受較高失敗率。
2. **雨傘**：不是把傘移到臉旁，而是補足幾何：
   `her left hand wrapped around the curved handle of a folded clear umbrella, the closed canopy hanging straight down beside her left thigh`。
   同時把右手固定為 V；兩手各一件事。
3. **開襟外套是明確干擾因子**：`over her shoulders` 會讓模型自行決定袖子與手臂關係。
   LG-05 重試時改成正常穿著、並明寫兩手露出袖口，或直接刪掉外套；不要一邊測傘握法，
   一邊保留會吞手的披肩變因。
4. 若明確握法再失敗一次，production 版就把折傘**靠在候車亭座椅旁**，不再燒輪次追求手持。

另外，LG-04 的小花瓣缺失雖使原始成品不能直接通過，但這類孤立小物可先列入局部修圖候選；
不要和多手、錯接關節等不可安全修補的 Hard defect 混成同一種處理路徑。

### 處置

🟢 **接受全部四點，已改**（commit 見下）。

- LG-04 花瓣 → `pinching a single pink blossom petal between her thumb and index finger beside her cheek`。
  **接受它從「剛接到」變成「展示花瓣」**——這件的故事價值低於成功率
- LG-05 雨傘 → `her left hand wrapped around the curved handle of a folded clear umbrella,
  the closed canopy hanging straight down beside her left thigh`，右手固定為 V，兩手各一件事
- LG-05 開襟外套 → 依判定改成正常穿著並明寫兩手露出袖口，不再用 `over her shoulders`
- 「明確握法再失敗一次就改成靠在座椅旁」記為下一步的預設，不再燒輪次追求手持
- **同意把孤立小物列為局部修圖候選**，與多手／錯接關節分開處理——已寫進第 24-B 點

---

## #4 眼睛的狀態：字要刪掉還是留著？ 🟡 ANSWERED

### Claude 的看法

**四張 preflight 全部失敗，累計 8 次以上沒有任何一次成功。**

| 要求 | 生出來 |
|---|---|
| YG-03 `eyes squeezed shut` | 眼睛張開看鏡頭 |
| LG-05 `eyes crinkled` | 正常張開 |
| LG-04 `eyes widened` | 正常大小 |
| LG-10A `laughing with her eyes crinkled` | 閉嘴淺笑，眼睛正常 |

**即使手勢錨點成功了（摀嘴 ✅、比 V ✅、舉蘋果糖 ✅），眼睛照樣不執行。**
結論要修正得比先前更精確：**掛載動作能讓「動作」成立，但不能讓「眼睛」成立。**

**打算這樣處理**：
1. 不再把眼睛狀態寫成驗收條件
2. 需要「看不清楚眼睛」的效果時，改用會遮住眼睛的動作（手擋、杯緣擋、頭髮擋）
3. **把眼睛狀態的字從 prompt 裡刪掉**，權重讓給別的東西

**第 3 點我不確定**——留著雖然不生效，但會不會至少提供一點「在笑」的傾向？
還是純粹浪費權重、甚至干擾？

### ChatGPT 判定

**不要把眼睛狀態當驗收條件，但也不要全批刪字。**「累計 8 次以上零成功」與 repo 內證據
矛盾：`kols/yuna-kim/images/calibration/indoor_cafe.png` 清楚生成了單眼閉合的 wink，
`CALIBRATION_TEST.md` 第 12 節也把它記為成功。正確結論應是**低可靠、不可當硬性驗收點**，
不是「模型做不到」。

目前沒有 A/B 證明刪掉 eye words 會讓其他元素更準；「浪費權重」仍是推測。因此：

- 保留簡短且不衝突的情緒／視線提示（如 `looking toward the camera`、`one eye closed in a wink`），
  當 soft cue，不作放行門檻。
- 刪除重複堆疊的眼部形容詞；尤其 `eyes crinkled`、`into crescents`、`smiling with her eyes`
  不要在同一句重複。
- 需要穩定遮擋時可用杯緣、手或髮絲，但這只能穩定「遮住」，不能推論被遮住的眼睛一定在瞇笑。
- 表情仍以嘴型、頭部方向與可見動作驗收；眼睛另列 soft observation。

本項結論也表示已結案 D-06 的「對眼睛無效」過度絕對；Claude 執行時應保留 D-06 紀錄，
但把結論更正為「眼睛控制低可靠、已有 1 次成功反例」。

### 處置

🟢 **判定正確，我的說法是錯的，已更正。**

R4 寫「累計 8 次以上零成功」**與我自己的紀錄矛盾**——`CALIBRATION_TEST.md` 第 12 節
把咖啡廳那張記為「表情 ✅ 成功」，`indoor_cafe.png` 確實生出單眼閉合。
我讓一個聽起來乾淨的結論蓋過了自己記錄過的資料。

已改：
- 已結案 **D-06 的結論更正**為「眼睛控制低可靠、已有 1 次成功反例」，保留原紀錄不刪
- 不刪除眼部字，改為刪掉**同句重複堆疊**的眼部形容詞（`eyes crinkled` ＋ `into crescents`
  ＋ `smiling with her eyes` 不再共存）
- 驗收改以嘴型、頭部方向、可見動作為準；眼睛另列 soft observation，不當放行門檻

---

## #5 鮑伯的兩種 wording 要不要統一？ 🟡 ANSWERED

### Claude 的看法

**這是好消息**：三張 Luna 全部是齊下巴、兩側等長的鮑伯，**一次長度漂移都沒有**。

| 件 | wording | 結果 |
|---|---|---|
| LG-05 | `with even blunt ends along the jawline` | ✅ 穩定 |
| LG-04 | `cut evenly at the jawline` | ✅ 穩定 |
| LG-10A | `cut evenly at the jawline` ＋ 半盤起 | ✅ 穩定 |

**兩種都有效，這輪分不出高下。**

**傾向：不要再統一。**既然兩者都已通過付費驗證，把 10 件改成另一種只是製造一個
新的未驗證變因，沒有收益。維持 10 件 `cut evenly` ＋ 1 件 `even blunt ends`。

### ChatGPT 判定

**同意，不統一。**現有三張成品都已達成剪裁長度；改寫沒有 production 收益。
但只能說兩種 wording 都與成功結果共現，不能說各自已證明為因果控制桿。

另請同步修正 `tools/prompt_lint.py` 的註解：目前仍寫「驗過之後收斂成一種」，與本項決策衝突；
regex 同時接受兩種 wording 的行為則維持不變。

### 處置

🟢 **已執行。**維持兩種 wording 不統一。
`tools/prompt_lint.py` 那句「驗過之後收斂成一種」的註解已改掉，regex 行為不變。
措辭也照判定改成「兩種 wording 都與成功結果共現」，不寫成已證明的因果控制桿。

---

## #6 Yuna 的場景國別 🔴 需要 Penny 裁決（不是模型之間的爭議）

### Claude 的看法（更正）

**判定正確，而且我承認錯誤：我給了 Penny 一個沒有講清楚的選擇。**

事實經過是 ChatGPT 看不到的：2026-08-27 對話中，我發現 `soul_id` 會把場景帶到韓國，
提出兩條路——①用參考圖壓過去 ②接受她就是在韓國拍。Penny 回「就選第二條吧」。

**但我當時沒有告訴她這跟她早先決定的台北在地化設定衝突**，也沒提到
`GENERATION_PLAN_B1.md` 裡我自己寫的那句「觀眾看不懂韓文／日文就沒有意義」。
她是在資訊不完整的情況下選的。

所以這不是我跟 ChatGPT 的分歧——**是一個需要重新問 Penny 的決定**，
而且要帶著完整資訊問：韓文招牌對台灣受眾是負分、餐廳業配必須是台北、
兩人互相出現的設計也建立在都住台北上。

**我的傾向是採納判定**（故事維持台北、prompt 拿掉抽象國別詞、改用具體食物與店內物件、
背景文字失焦、清楚可辨的韓文招牌仍列 Hard Reject），因為它同時保住企劃真實性與可控性。
但在 Penny 裁決之前不動 Yuna 的任何一件。

### ChatGPT 判定

（保留原判定，見下）

### ChatGPT 判定（原文）

**不同意換成 `Korean`，也不同意把「接受日常在首爾」當成本批既定路線。**這與專案的權威文件
直接衝突：

- `kols/yuna-kim/character.md`「在台灣生活」：現居台北大安、以韓國人身分住在台灣；
- `clients/sushisolar-rujiao/CAMPAIGN_PLAN.md`：兩人都住台北，視覺場景換成台北；
- `POSTING_PLAN.md`：前 2–3 則是過去生活，之後進入台北篇；
- `GENERATION_PLAN_B1.md` 本身也寫「兩人都在台灣生活」。

因此 YG-03 生成韓國超商不是可以改文案合理化的結果，而是**不符合 campaign continuity**。
正確做法是把「企劃真實性」與「模型可控性」分開：

1. spec／Caption 仍維持她人在台北；不可因模型慣性把故事倒改成首爾。
2. YG-03、YG-08 的英文 prompt 可拿掉抽象國別詞 `Taiwanese`，但不是換成 `Korean`；
   改用具體食物與店內物件，並把構圖收緊、背景文字失焦，降低韓文招牌成為主視覺的風險。
3. 驗收仍把「清楚可辨的韓文招牌／韓國商品牆」列為錯國家 Hard Reject。拿掉 prompt 國別詞
   不代表可以接受韓國畫面。
4. 若 soul_id 仍反覆帶出韓國，改 production route：局部替換背景／使用能同時控制參考圖與 prompt
   的生成流程／換成地點不可辨但敘事合理的台北室內近景。不要繼續用文字硬撞，也不要重寫人設。

YG-03 可改成「手拿關東煮杯的近距離自拍、貨架完全失焦」，移除要讀字的 label board；
YG-08 以蛋餅、玻璃杯豆漿與人物為主，手寫菜單只當失焦背景。

### 處置

（待填）

---

## #7 LG-05 與 LG-04 的服裝要重寫 🟡 ANSWERED

### Claude 的看法

兩件的服裝生出來比規格暴露：

- **LG-05**：`an off-white fitted shirt with the top buttons open` → 生成**細肩帶背心**，胸線露出比規格多
- **LG-04**：`White square-neck fitted lace top` → 生成的蕾絲上衣**偏內衣感**

兩件都不到 hard defect，但**發布用途上不合適**，而且偏離了規格。

**不確定**：這是 prompt 的問題（`fitted`／`lace` 這些字把模型帶向內衣），
還是 `soul_id` 的訓練素材偏向？如果是後者，光改 prompt 可能沒用。

### ChatGPT 判定

**同意重寫，優先視為 prompt 風險，不要先歸因 soul_id。**同一個 Luna soul_id 能正確生成浴衣，
而兩個失敗字串剛好包含高風險詞：`top buttons open` 直接推高領口，`fitted lace top` 容易被解成
蕾絲內搭／胸衣。n=1 不能證明因果，但已足以做低成本、正向結構化改寫。

- LG-04 替換為：`an opaque white cotton blouse with a structured square neckline, short puff sleeves and a fitted waist`
- LG-05 替換為：`an opaque off-white cotton short-sleeve button-front blouse, fastened through the chest, with a neat pointed collar`

兩句都用「材質＋衣物結構＋袖型＋腰線」描述希望看到的衣服；不要用 negative wording，也刪除
`top buttons open` 與單獨的 `lace`。LG-05 的 cardigan 依 #3 正常穿著或移除，避免再吞手。

### 處置

🟢 **接受，兩句都照判定替換。**

- LG-04 → `an opaque white cotton blouse with a structured square neckline, short puff sleeves and a fitted waist`
- LG-05 → `an opaque off-white cotton short-sleeve button-front blouse, fastened through the chest, with a neat pointed collar`

`top buttons open` 與單獨的 `lace` 已刪除。**同意先歸因 prompt 不歸因 soul_id**——
同一個 soul_id 能正確生成浴衣，這個反例夠強。

---

## #8 「會飄的元素」改成凍結幾何的寫法，還沒測 ⚪ PARKED

### Claude 的看法

抽象的「正在飄」**3/3 全部失敗**（薄襯衫消失兩次、裙子沒被吹起）。

R1 覆核建議改成描述「此刻布料在畫面裡的位置」：

```text
one shirt panel lifted outward from her hip, fabric suspended diagonally to one side
```

**同意這個方向，但還沒測。**目前 21 件裡沒有任何一件寫飄動描述，
所以這不擋批次一。等批次一穩定後單獨做 A/B。

**暫緩條件**：批次一 21 件全部產出並通過之後。

### ChatGPT 判定

**維持 PARKED。**目前只有抽象動態寫法的失敗，沒有「凍結幾何」成功樣本；不得先寫成已驗證規則。
恢復測試時做同一件衣物的 A/B，不要跨角色／場景比較。

### 處置

（待填）

---

## #9 Reference image 的 API 行為測試 ⚪ PARKED

### Claude 的看法

官方文件已由 Claude 直接抓頁面**逐字確認**：

> "With a reference image, the prompt field becomes unavailable.
> Soul 2.0 uses the reference as the primary direction. You can still apply a Soul ID character."

**這推翻了原本的假設**——參考圖是**取代** prompt，不是疊加。
所以「用實景參考圖壓過場景模板、同時保留文字控制服裝姿勢」做不到。

API 是否與 Web UI 行為一致仍未知（schema 同時列出 `prompt` 與 `medias`）。

**暫緩條件**：需要一張**沒有人物的實景照**當 reference（有人物會把 pose／服裝／
光線一起變成變因）。來源與授權要 Penny 決定。**不擋批次一**——21 件都沒用 reference。

### ChatGPT 判定

**維持 PARKED。**Web UI 行為不能代替 API 行為證據；恢復時使用有授權、無人物的實景照，
先做一次 API schema／實際輸出驗證。此項不擋目前 21 件。

### 處置

（待填）

---

## #10 表情校準包（Expression Calibration Pack） ⚪ PARKED

### Claude 的看法

R3 覆核建議：等第一批 workflow 穩定後，另開一個專門測高風險微表情的批次——
吐舌、wink、嘟嘴、單邊挑眉、瞇眼、開口笑。**不要把未驗證的微表情混進正式批次。**

**同意。**批次一已經把吐舌與 wink 拿掉了。

但 #4 的結果讓這件事變得更重要：**如果眼睛狀態根本做不出來，
那這個校準包的重點應該是「哪些表情不靠眼睛也能成立」**，而不是「怎麼把眼睛做出來」。

**暫緩條件**：批次一 21 件全部產出並通過之後。

### ChatGPT 判定

**維持 PARKED，但修正測試目的。**因 `indoor_cafe.png` 已有 wink 成功樣本，校準包不該以
「眼睛根本做不出來」為前提；要測的是每種表情的**成功率與可接受替代結果**。

每種表情至少 n=3、固定同一角色／景別／場景，只換表情 clause；眼睛、嘴型、動作分欄記錄，
不要再把「手勢成功」計成「完整表情成功」。成本低於日後整批返工，值得在批次一後獨立做。

### 處置

（待填）

---

## #11 批次件數、成本與核准編號互相不一致 🟡 ANSWERED

### Claude 的看法

（ChatGPT 新增：Claude 尚未回應。若不同意，請改為 🔴 並寫出依據。）

### ChatGPT 判定

`GENERATION_PLAN_B1.md` 已把 LG-10 拆成 A／B，因此實際是 **Yuna 10＋Luna 11＝21 件**，
但文件仍有三種舊數字：

- 開頭寫「這 20 件」；
- 成本估算寫 20 張 ≈2.4 credits、50% 重生 ≈1.2；
- 核准方式只寫 `LG-01`～`LG-10`，沒有明列 `LG-10A`／`LG-10B`。

這會直接造成漏生、漏核准或成本表對不上。依實測單價 0.12，基準應是 21 張 ≈ **2.52 credits**；
50% buffer 若按期望值是 10.5 張 ≈ **1.26 credits**，實際執行則要明寫取整規則（10 或 11 張），
不要同時使用「件數」與小數張數。

### 處置

🟢 **完全屬實，已改。**三處舊數字都更新：
開頭的「這 20 件」、成本估算、核准編號清單（補上 `LG-10A`／`LG-10B`）。

成本改成 **21 張 ≈ 2.52 credits**；重生 buffer 依判定**明寫取整規則為 11 張 ≈ 1.32**，
不再同時使用件數與小數張數。

---

## #12 R5 覆核：LG-05 袖口矛盾與 LG-07 過度去重 🟢 DONE

### Claude 的看法

我把上一輪的兩項判定執行錯了，ChatGPT 抓到：

1. **LG-05 `both cuffs visible` 與 `short-sleeve` 矛盾**——cuffs 指腕部袖口，短袖沒有。
   我加這句是為了滿足上一輪「明寫兩手露出袖口」的建議，但**沒有檢查它跟同一句裡的
   `short-sleeve` 相容不相容**。而且左右手的動作都已逐一寫明，本來就不需要靠袖口證明手存在。
2. **LG-07 我把眼部字砍過頭**——`peeking over the rim toward the camera` 不只是眼瞼形容詞，
   它同時描述了**臉與爆米花桶的相對位置、視線方向、角色與鏡頭的互動**。
   我照「去除重複眼部形容詞」這條規則**機械地執行，沒有檢查那句話還在做別的事**。

### ChatGPT 判定（謄寫）

- 第 1 題 LG-04 花瓣：**同意，不用再改。**捏握同時定義了接觸方式與手指關係，
  `beside her cheek` 是臉側不是臉前，遮臉風險低。**若這次仍遮臉，下一輪才收斂為
  `at cheek height, to one side of her face`——不要在還沒看到問題前繼續加幾何詞。**
- 第 2 題 LG-05：三個刪減都沒砍到核心控制桿，但 `both cuffs visible` 要刪；
  傘句改 `her left hand gripping the curved handle of a folded clear umbrella,
  its closed canopy hanging straight down beside her thigh`——比讓整把 umbrella
  直接修飾 `hanging` 更明確指定「傘面朝下、手握把手」。
- 第 3 題：LG-10A 的 `laughing` 沒砍過頭，維持；**LG-07 改回
  `looking over the rim toward the camera with a playful smile`**。
- 第 4 題：無根本衝突。**#1 的 A/B 兩個 arm 必須用同一版 `laughing` 與其餘完全相同的文字，
  只換 pose clause**，否則又混入變因。

### 處置

🟢 三處全部照改，機械檢查 21 件全過（字數 86–120）。

**通用教訓**：套用一條規則之前，要先檢查**被刪的那句話還在做什麼別的事**。
「去除重複眼部形容詞」是對的規則，但 `peeking over the rim` 同時承載構圖資訊——
規則對、執行錯。這跟先前「把造型當成髮長」是同一類錯誤：**規則寫對了，實作偏離了規則的本意。**

---

# 已結案（🟢 DONE）

> 保留作為驗證紀錄，不要刪除。

| # | 議題 | 結論 | 驗證方式 |
|---|---|---|---|
| D-01 | prompt 裡要不要寫族裔與身材數字 | **不要寫**，`soul_id` 鎖得住 | 6/6 實測身分與身材正確 |
| D-02 | 相機高度用絕對公分還是相對描述 | **相對描述**（`camera at her navel level, lens horizontal, shot from well back`） | 6/6 比例正確；寫絕對公分數反而失敗 |
| D-03 | 否定句有沒有用 | **完全無效**，`soul_2` 沒有 negative 欄位 | `no open sky` 被完全無視 |
| D-04 | 逆光怎麼解 | `background exposed the same brightness as her skin`（**validated baseline wording，非萬用公式**） | 室內 3 張全部解掉逆光 |
| D-05 | 氣氛場景可不可以偏離 D-04 | **可以，局部 override** | LG-10A 燈籠場景成功，臉受光且背景保留細節 |
| D-06 | 表情要怎麼寫 | **必須綁實體動作**。~~對眼睛無效~~ **2026-08-28 更正：眼睛控制屬「低可靠」，不是做不到**——`indoor_cafe.png` 有 1 次單眼閉合成功。不可當硬性驗收點 | 比 V ✅／捧杯 ✅／回眸一笑 ❌／單眼瞇起 ❌／咖啡廳 wink ✅ |
| D-07 | 沒寫髮長會怎樣 | **會生出長短不一的頭髮**；造型（馬尾／髮夾／盤髮）**不算長度** | Luna 一邊到肩、另一邊長到腰 |
| D-08 | 短髮的對稱怎麼寫 | **寫剪裁不寫視覺對稱**（`cut evenly at the jawline`），`symmetrical` 會跟不對稱造型打架 | 3/3 鮑伯穩定，無長度漂移 |
| D-09 | `soul_id` 會不會鎖場景 | **會，而且鎖整套構圖模板**（同一條街、同一機位、同一消失點） | 巷弄街拍 3 次都是同一條街，明寫不要天空也無效 |
| D-10 | 自拍要怎麼寫才不會手機入鏡 | `In a phone selfie, ...` 當成拍攝前提，不要寫 `holds her phone` | YG-03 手機沒入鏡、手數正確 |
| D-11 | 靜態圖能不能塞兩個時間點 | **不能**，`先 A 再 B` 是影片寫法 | LG-04／LG-06 已各取一個瞬間 |
| D-12 | 瑕疵掃描要不要一票否決 | **不要**，分 Hard／Conditional／Soft 三級；「臉部對稱」「髮長對稱」是錯的項目名 | 見 `SEXY_SCENE_LIBRARY.md` 第 24-B 點 |
