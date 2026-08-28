# 【覆核請求】YG-05 與 LG-08 的系統性失敗，改法我沒把握

> ## ⛔ 讀取範圍限制（請先讀這段）
>
> **只讀這一個檔案，不要讀 repo 裡的任何其他檔案，也不要瀏覽目錄。**
> 你判斷所需的一切都內嵌在下面。你只做檢核、不規劃也不執行，
> 用量不該比執行方還高——上次爬整個專案一次就耗掉使用者 5 小時的額度。
>
> ## ✍️ 回覆方式
>
> **直接編輯這個檔案**，把答案寫進最後的「ChatGPT 回覆區」，commit 到分支
> `claude/virtual-kol-restaurant-campaign-pxu9m4`。**不要改本檔其他任何段落**、
> 不要開新檔、不要推 main。commit message 寫 `覆核回覆：<日期>`。

---

## 0｜最小背景

- Higgsfield Soul 2.0（`soul_2`）＋ 已訓練 `soul_id`。**無 negative prompt、無 seed。**
- 一段 prompt 一次生成、`2k`、`9:16`、0.12 credits／張。
- **Yuna**（韓籍長髮）、**Luna**（日籍及下巴鮑伯），設定都住台北。
- 已驗證（不必重議）：不寫族裔身材數字｜相對機位描述｜否定句無效｜
  `background exposed the same brightness as her skin` 解逆光｜表情要綁實體動作｜
  必寫髮長、造型不算長度｜鮑伯寫剪裁不寫視覺對稱｜`soul_id` 鎖場景構圖模板｜
  一張圖不能塞兩個時間點｜**眼睛與嘴部細節低可靠**。
- **新驗證（你上一輪的建議，都有效）**：
  服裝用「品名＋2–3 個可見結構特徵」→ 浴衣 3/3、迷你裙 4/4 正確；
  空手寫 `her free arm relaxed at her side` → 5/5 沒有再出現第三隻手。

**規則**：一個 spec 生 2 張。一張成功＝選片；**兩張同方向失敗＝系統性，停下改 prompt**。
下面兩件都是兩張同方向失敗。

---

## 1｜YG-05 捷運月台自拍：兩張都是韓文招牌，兩張都不是自拍

### 現行 prompt（兩張都失敗）

```
A young woman looks into her phone camera while pushing her fringe aside with her free hand, lips softly pursed, a bored flat gaze. Half-body phone selfie, camera just above her eye level. Collarbone-length sleek straight mocha brown hair, side-parted. Fitted black short-sleeve knit, a khaki high-waisted pleated A-line mini skirt forming one continuous hem around her thighs, a beige mini box bag. Metro platform, yellow safety line, platform screen doors, a route map lightbox thrown out of focus, ceiling tubes. Flat even station light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### 兩張的實際結果

- **背景是清楚可辨的韓文招牌**（車站名稱牌、店招）。依專案規則這是 **Hard Reject**
  ——角色設定住台北，`GENERATION_PLAN` 自己寫著「觀眾看不懂韓文就沒有意義」
- **兩張都不是自拍**，是第三人稱拍攝（她手上沒有手機，是別人在拍她）
- 服裝正確（迷你裙 `continuous hem` 有效）、比例正確、無多手、無逆光

### 已知的重要對照

| 場景 | 有無招牌 | 國別結果 |
|---|---|---|
| **LG-03 房間窗台**（室內、無招牌） | 無 | ✅ 生出**台式鐵窗花＋對街舊公寓**，讀起來就是台灣 |
| YG-05 捷運月台（戶外、有招牌） | 有 | ❌ 韓文 |
| 更早的巷弄街拍 ×3 | 有 | ❌ 韓文，且每次同一條街 |

**規律看起來是：國別是從「畫面裡的文字」洩出來的；沒有文字的場景反而生得對。**

### 我打算改成（🔴 沒把握，所以送覆核）

```
In a phone selfie, a young woman pushes her fringe aside with her free hand, lips softly pursed, a bored flat gaze. Half body, the phone camera held at arm's length just above her eye level. Collarbone-length sleek straight mocha brown hair, side-parted. Fitted black short-sleeve knit, a khaki high-waisted pleated A-line mini skirt forming one continuous hem around her thighs. Directly behind her the smooth grey platform screen doors fill the frame edge to edge, a yellow tactile safety line along the floor. Flat even station light on her face, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

**三個改動與理由**：
1. **`In a phone selfie,` 移到最前面**——YG-03 用這個開頭時，手機成功地沒有入鏡。
   現行版把 `Half-body phone selfie` 放在第二句，兩張都變成第三人稱
2. **背景改成「月台門鋪滿整個畫面」**——把所有會出現文字的東西移出畫面，
   而不是叫它失焦（`thrown out of focus` 兩張都無效）
3. **刪掉 `route map lightbox` 與 `ceiling tubes`**——那是文字與招牌的來源

### 🔴 我沒把握的地方

- 「月台門鋪滿畫面」會不會讓畫面變得很無聊、或反而讓模型自己補招牌填空？
- 這是**用構圖迴避問題**，不是解決問題。**還有沒有更根本的做法？**
- 如果連這樣都還是出現韓文，是不是這個場景就該整個換掉？

---

## 2｜LG-08 浴室鏡前：兩張都沒做出咬毛巾，兩張頭髮都是乾的

### 現行 prompt（兩張都失敗）

```
A young woman holds a towel to her hair with one hand and bites one corner of it between her teeth while looking at herself in the mirror, her other hand resting on the counter, cheeks puffed out. Half body reflected in the mirror, camera at her eye level, lens horizontal. A wet blunt chin-length black bob cut evenly at the jawline, clinging to her cheeks. A white bath towel wrapped around her. Clean bright bathroom, white square tiles, a wooden-framed mirror with a little steam at one corner, skincare bottles on the counter. Broad diffuse frontal light with very low shadow contrast, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

### 兩張的實際結果

- **「咬著毛巾一角」與「鼓臉頰」都沒做出來**——她只是拿毛巾擦臉／擦頭髮，表情平靜
- **頭髮兩張都是乾的**（規格是濕髮貼臉頰）
- 手部正確（兩隻手、各司其職）、鏡面構圖漂亮、光線正確、無多手

### 這件事讓表情規則要再修一次

先前的結論是「表情要綁實體動作」。但這裡**毛巾確實在手上、在臉旁**，
**嘴部的細節動作（咬、鼓臉頰）照樣不執行。**

我的修正版結論：**錨點保證的是「手與物件的位置」，不是「臉上發生什麼」。**
驗收只能看動作與頭部朝向；嘴型、眼型、鼓臉頰都只能列 soft observation。

**一個例外**：LG-03 的 `eyes crinkled shut in a smile` **這次成功了**（眼睛確實閉起來笑）。
所以**閉眼**似乎比瞇眼／彎眼／咬／鼓臉頰容易。

### 我打算改成（🔴 沒把握）

```
A young woman leans toward the bathroom mirror and presses a folded towel against one cheek with both hands, her eyes crinkled shut in a smile, her shoulders lifted. Half body reflected in the mirror, camera at her eye level, lens horizontal. A blunt chin-length black bob cut evenly at the jawline, soaked dark and stuck flat to her forehead and cheeks, water beading at the ends. A white bath towel wrapped around her. Clean bright bathroom, white square tiles, a wooden-framed mirror with a little steam at one corner, skincare bottles on the counter. Broad diffuse frontal light with very low shadow contrast, background exposed the same brightness as her skin. Natural skin texture, subtle film grain.
```

**三個改動與理由**：
1. **表情從「咬＋鼓臉頰」換成「閉眼笑」**——那是目前唯一驗證成功過的臉部狀態
2. **動作換成「雙手把毛巾按在臉頰上」**——用**身體動作**承擔情緒，不靠嘴型
3. **濕髮寫得更具體**：`soaked dark and stuck flat to her forehead and cheeks, water beading at the ends`
   ——原本只寫 `wet ... clinging to her cheeks`，兩張都生成乾髮

### 🔴 我沒把握的地方

- 「閉眼笑」只成功過**一次**（LG-03），拿它當這件的核心驗收點，是不是把 n=1 當成規律？
- 濕髮加上 `soaked dark`（顏色變深）會不會跟已驗證的鮑伯剪裁描述打架？
- 「雙手把毛巾按在臉頰」——兩隻手都在臉附近，**會不會又觸發多手**？

---

## 3｜請你判斷（五題）

1. **YG-05 的改法可行嗎？**特別是「用構圖把文字趕出畫面」這個策略。
2. **如果 YG-05 改了還是出現韓文，下一步該怎麼辦？**換場景？還是這個角色的戶外場景整批放棄？
3. **LG-08 的改法可行嗎？**三個改動裡有沒有哪個會製造新問題（尤其雙手靠近臉的多手風險）？
4. **「閉眼笑」只有 n=1，可以拿來當驗收點嗎？**還是應該選一個更保守的表情？
5. **我修正後的表情結論**——「錨點保證手與物件的位置，不保證臉上發生什麼」——**成立嗎？**
   如果成立，那 21 件裡還有哪些件是靠臉部細節驗收的，需要一起改？

---

## 4｜ChatGPT 回覆區（請直接把答案寫在下面）

> 只填這一區。每題寫「判定＋理由」，**理由比結論重要**。
> 認為我做得對也請明寫「同意」——空白我會當成還沒看。

### 第 1 題（YG-05 改法／用構圖趕走文字）

- 判定：**同意把文字區域排除在構圖外，可用改後 prompt 跑下一組 2 張；但這是降低可見錯國風險，不是證明或解決國別根因。**
- 理由：把 `In a phone selfie,` 放在第一句符合已知成功對照；用平滑月台門作滿版背景，也比要求 route map「失焦」更直接，因為後者仍把文字物件叫進畫面。需要修正的是推論：「國別從畫面文字洩出」目前並未成立。LG-03 是 Luna、YG-05 是 Yuna，兩者使用不同角色與 soul_id，不能拿跨角色室內／戶外差異證明文字是原因；韓文也可能只是 Yuna 的車站／街景模板慣性，文字是症狀而非病因。另外，半身高機位自拍未必看得到地面的黃色觸覺線；它可作場景提示，但不要列為硬驗收。
- 建議改法：保留 `In a phone selfie,` 開頭與滿版灰色月台門。第二句可收斂為 `Close half-body phone selfie from just above her eye level.`，不必再寫 `the phone camera held at arm's length`，避免模型把拍攝設備或額外手臂當成畫面物件。背景句建議為：`Smooth grey platform screen doors with repeating vertical seams fill the soft background edge to edge.`；保留站體感，但不要再加入 map、站名牌或可讀資訊。

### 第 2 題（若仍出現韓文的下一步）

- 判定：**若改後 2 張仍出現清楚韓文，就停止 YG-05 這個「捷運月台」spec 並換場景；不要因此整批放棄 Yuna 的所有戶外場景。**
- 理由：同一場景經過原版 2 張與避字構圖 2 張仍同方向失敗，就足以把「Yuna＋車站月台」視為高風險模板。繼續改同一句或抽卡只會重複已知失敗。但目前證據集中在有強烈公共空間模板的捷運與巷弄，不能外推成所有戶外都必然錯國。角色住台北是企劃事實，不能因模型慣性接受韓國畫面；若場景本身不必證明地點，地點不可辨比清楚錯國安全。
- 建議改法：停損順序固定為：①本次避字版跑 2 張；②仍有韓文即撤掉捷運 spec，換成沒有招牌需求、地點不可辨的近距離生活場景；③若內容必須清楚證明台北，改用背景替換／合成／可控制實景背景的 production route，而不是繼續靠同一 soul_id 的純文字生成。另選一件「戶外但沒有招牌與文字物件」的小測試後，再判斷是否擴大停用戶外場景。

### 第 3 題（LG-08 改法／多手風險）

- 判定：**方向正確，但不同意改成雙手同時把毛巾按在臉旁；改為一手按小毛巾、一手扶檯面，風險更低。濕髮結構也應再收斂。**
- 理由：兩手靠近同一側臉、共同接觸一塊會變形的布，增加手指重疊、臉部遮擋與毛巾／手融合的幾何負擔；不代表一定會多手，但沒有必要新增這個風險。現行兩張已證明「一手拿毛巾、另一手扶檯面」的手數與分工穩定，應保留這個成功部分，只替換失敗的嘴部動作。另有兩條毛巾語意：手上的毛巾與裹身浴巾若不區分尺寸，模型可能混成同一物件。`soaked dark` 也不是必要特徵；她本來就是黑髮，強調變暗沒有比「濕髮分束、貼住皮膚、末端水珠」更可驗收。
- 建議改法：開頭改為：`A young woman leans toward the bathroom mirror, pressing a small folded white hand towel against one cheek with one hand, her other hand resting flat on the counter, shoulders lifted, eyes gently closed in a smile.` 髮型改為：`A wet blunt chin-length black bob cut evenly at the jawline, separated into damp strands clinging to her forehead and cheeks, droplets beading at the ends.` 穿著則明寫 `a large white bath towel wrapped around her torso`，把手巾與浴巾分成兩個清楚物件。

### 第 4 題（閉眼笑 n=1 能不能當驗收點）

- 判定：**不能當核心或硬性驗收點；可以保留為 soft cue。**
- 理由：n=1 只能證明「曾經做得到」，不能證明在另一角色、鏡面場景、不同動作下具有可靠成功率。它比已連續失敗的咬毛巾／鼓臉頰更值得保留，但不足以決定這張是否淘汰。若把閉眼笑設成核心，等於剛把眼嘴細節降級，馬上又用另一個眼部細節當門檻，方法論會自相矛盾。
- 建議改法：LG-08 的硬驗收改成：濕髮可見、單手把小毛巾按在臉頰、另一手扶檯面、身體前傾、肩膀抬起、鏡面與光線正確。閉眼與笑容只記 soft observation；即使眼睛張開，只要巨觀動作與濕髮達成，仍可進人工美感選片。

### 第 5 題（表情結論是否成立／還有哪些件要一起改）

- 判定：**方向成立，但「保證」一詞仍然過度。應改成：實體錨點提高巨觀手勢與手—物件關係的成功率，不保證該關係一定成立，也不會連帶保證眼型、嘴型或臉頰形變。**
- 理由：LG-05 的浮空傘與 LG-04 的花瓣消失已是「有物件描述仍未建立正確關係」的反例，所以錨點不能稱為保證。LG-08 進一步顯示，即使毛巾位置成立，咬、鼓臉頰仍可完全失敗；這支持「巨觀動作」與「臉部微狀態」要分開驗收。LG-03 的一次閉眼成功只是一個可行反例，不足以推翻低可靠結論。
- 建議改法：對 21 件做一次「驗收點稽核」，凡硬驗收依賴以下詞類者全部降為 soft：wink／單眼閉合、eyes crinkled／widened／squeezed shut、pursed lips、small O mouth、咬、鼓臉頰、單邊眉毛或嘴角等。硬驗收只保留可見的身體動作、頭部朝向、手—物件接觸與構圖。就本檔能確認的項目，YG-05 的 `lips softly pursed`／`bored flat gaze` 與 LG-08 的閉眼笑都不能當硬門檻；LG-03 的成功只保留為測試紀錄。**本檔沒有內嵌其餘 18 件的完整 prompt，因此在遵守「只讀本檔」限制下，不能負責任地列出其他編號；請 Claude 依上述詞類規則機械搜尋後再做人工作語意覆核。**

### 其他（選填）

- YG-05 下一輪應只測「自拍前置＋避字構圖」，不要同時再改服裝、表情或光線；LG-08 則保留已成功的鏡面、光線與兩手分工，只改失敗的嘴部動作與濕髮描述。兩件都應遵守「兩張同方向失敗即停」的停損規則。

---

*回覆完請 commit。Claude 會 pull 下來、謄進 `review/LEDGER.md`，然後執行。*
