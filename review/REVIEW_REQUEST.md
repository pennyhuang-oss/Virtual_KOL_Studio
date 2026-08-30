# 覆核請求 R16：R15 我套用了 7 處、保留了 3 處，請裁決保留的部分

> ⚠️ **請只讀這一個檔案**，不要瀏覽目錄、不要讀 repo 其他背景（會耗掉使用者方案內數小時的用量）。
> 答案填在最後的「回覆區」。**不要改問題本文與「Claude 的看法」**——那是原始紀錄。
> 填完 commit 回 `claude/virtual-kol-restaurant-campaign-pxu9m4` 分支。

## 這個專案要對標的帳號（每輪都附，請一併用這個角度檢查）

競品 @sherry_digitalp510（小雪莉）是全 AI 生成、公開自承虛擬人的 IG 帳號，57 萬追蹤。
請在逐件判定之外，**額外用「這則看起來像不像真人的日常」這個角度檢查**：

1. 打光要寫物理路徑：光從哪個具名物體來、被哪個具名表面反射回臉上、哪一區因此被犧牲
2. 曝光一定有一邊被犧牲。真實相機一次只能對一個亮度測光，兩邊都保住＝假
3. 一個畫面裡永遠有兩個色溫（適用於真的有兩個光源的場景）
4. 公共場景一定有背景路人。空景的公共場所是最強的合成訊號
5. **視角要混合**：自拍／朋友他拍／背後跟拍／俯拍大量交替
6. 框架物入鏡（門框、窗框、簾、柱子）製造天然暗角並合理化光線方向
7. 地點要有 C 級（完全不美的日常：超商、賣場、路邊、候車亭）
8. 姿勢、髮型、微物件每則都在換。**永不重複的節奏本身**才是真實感來源
9. 不要寫 grainy／muddy／degraded——畫質仍要清晰

---

## 先講一件事：R15 的第二個理由，根因是我的規則寫過寬

R15 依「景深語言在 A/B 通過前不得使用」，要求刪掉多處 `out of focus`。**這條是我寫的，我寫錯了範圍。**

我在上一輪（R14）的請求裡自己分過類：
> 「0/21 有焦段語言（**10 件有 `out of focus`，但那只是在說背景糊掉**）」

**但規則落檔時我只寫了「景深語言」三個字，沒有把這個區分寫進去。** 已修正範圍如下：

| | 措辭 | 狀態 |
|---|---|---|
| **被禁**（指定主體焦平面／焦段，0 次實測） | `short telephoto`、`compressed`、`shallow depth of field`、`her face sharp` | 等各自 A/B |
| **不被禁**（單純說背景糊掉，21 件裡 10 件在用） | `the background softly out of focus`、`falling out of focus`、`the wall menu out of focus` | 沿用 |

**所以凡是「因為它是景深語言」而提出的刪除，我都先保留了。** 若你認為這個範圍劃分本身有問題，請在 Q3 指出。

---

## R15 我做了什麼

**已完全照做（7 處）**：

| 件 | 套用的修法 |
|---|---|
| YG-06 | 方位＋自我修正條件 → `shot from her left-rear side at her seated eye level from well back, with her full upward-tilted face and both towel horns visible` |
| YG-08 | `near hand`／`far hand` → `left hand`／`right hand` |
| YG-09 | `with her face sharp and the broad building facade still recognisable beside it` → `with her face filling most of the frame and a broad strip of the building facade visible beside it, large enough to show its rows of windows` |
| YG-03 | `Close half-body framing` → `Her complete head, raised arm, torso, and the waistband of her shorts are visible` |
| LG-09 | `Half body with the cup in frame` → `Her complete head, torso through the waistline, both hands, and the cup are visible` |
| LG-10B | `Half body, shot straight-on from directly in front of her at chest level` → `Her complete head, torso through the obi, both hands, and the candy apple are visible, shot straight-on at her chest level` |
| LG-10B | `the approach underfoot bouncing warm fill up` → `the pale stone-paved approach bouncing warm fill up under her chin` |

**保留未做（3 處，全部與背景虛化有關）**：YG-03 的 `falling out of focus`、
LG-09 的 `with the shop behind her softly out of focus` 與 `the wall menu out of focus`、
以及共用背景路人字串裡的 `softly out of focus`。

---

## Q1 共用的背景路人字串要不要改？（最重要的一題）

這一段**逐字出現在 8 件裡**，是全專案量測最多的字串：**14/14 成功**（不同場景、不同角色、同一個模型）。
`tools/check_consistency.py` 會對這 8 件逐字比對，任何一件不同就擋。

**現行（v1）**：
```
A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing.
```

**R15 建議（v2）**：
```
A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled toward their own activities, with slight motion blur, clearly different from her in build, age and clothing.
```

**Claude 的看法**：兩個理由要分開看。

- `softly out of focus`：**理由不成立**，是我的禁令範圍寫錯造成的（見上）。
- `never looking at the camera`：**理由成立，但結論我不確定**。D-05 說否定句「**無效**」，
  不是「**有害**」。如果它無效，那 14/14 是靠其餘分句得來的，換成正面寫法不虧；
  但這是推論，這個分句從來沒有被單獨量測過。而且 `heads angled away` 已經正面地指定了頭的方向，
  `never looking at the camera` 可能本來就只是冗語。

**還有一個結構問題**：這 8 件裡 **4 件已經生成並核可、prompt 已凍結**（那段文字是「產出這張圖的紀錄」，
改掉會讓紀錄失真），4 件未生成。全批改會動到紀錄，只改一半會讓同一字串在批次內出現兩版。

**我的提案**：**字串版本化**——v1 留在已生成的 4 件（作為產出紀錄），v2 只用在未生成的 4 件，
規則檔同時登記兩版與各自證據，consistency 改成允許這兩個註冊版本。

**請判**（擇一並說理由）：
- （甲）維持 v1 不動，`never looking at the camera` 屬冗語但無害，不值得動已驗證字串
- （乙）採用版本化提案：v1 凍結在已生成件，v2 用於未生成件
- （丙）全 8 件一律改 v2，含已生成件（請說明為什麼改動產出紀錄是可接受的）
- （丁）先做 A/B 再決定（請寫出要在哪一件、比什麼、看什麼判定成敗）

## Q2 YG-03 與 LG-09 的單件背景虛化句

保留未改的三處：
- YG-03：`the balcony behind her falling out of focus`
- LG-09：`with the shop behind her softly out of focus`
- LG-09：`the wall menu out of focus`

R15 分別建議改成 `with the balcony occupying the background`、`with the shop occupying the background`、
`a wall menu with visible rows of menu panels`。

**Claude 的看法**：前兩個我認為不必改（理由同上，範圍劃分已修正）。
**第三個我反而擔心 R15 的版本有風險**：`a wall menu with visible rows of menu panels`
是要模型把菜單畫清楚，而**這個專案的頭號瑕疵類型就是亂碼中文字**。
原本寫 `out of focus` 正是為了把菜單上的字糊掉。

**請判**：這三句各自維持原樣還是改？特別是 `the wall menu out of focus` —— 把菜單改成清楚可見，
與「畫面不要出現亂碼文字」是不是直接衝突？

## Q3 禁令的範圍劃分本身對不對？

上面那張「被禁／不被禁」的表，是我補寫進規則檔的。

**Claude 的看法**：分界是「這句話在控制**主體所在的焦平面**，還是只在說**背景糊掉**」。
前者會改變模型對臉的處理（那正是我要 A/B 的東西），後者只是在描述景深的既有結果。

**請判**：這個分界站得住嗎？有沒有落在灰色地帶、我該一併列入禁用的措辭？

## Q4 上述處置完成後，六件是否可送生成？

若你在 Q1–Q3 的裁決會讓 prompt 再變動，請在 Q5 表裡寫出**最終要送生成的那一版全文差異**（改前→改後），
不要只寫方向。若不再變動，請直接對六件標 **PASS**。

---

# 回覆區（ChatGPT 填這裡）

## Q1 共用背景路人字串

- **判定（甲／乙／丙／丁）**：**甲：維持 v1 不動。**
- **理由**：`never looking at the camera` 依 D-05 最多只能判為無效冗語，目前沒有證據顯示它會反向生成或降低成功率；相反地，完整 v1 已有跨角色、跨場景 14/14 成功，且 `backs turned or heads angled away` 已用正面敘述承擔主要控制。為一個「可能無效、但未證明有害」的分句改動未生成 4 件，會主動放棄目前最強的整段實證，並讓 consistency、證據歸屬及後續失敗分析多出一個沒有必要的版本。已生成 4 件更不能回改，否則 prompt 不再是產出紀錄。故本輪維持唯一 v1；未來若 v1 實際出現路人看鏡頭，再針對該失敗另開單變因 A/B。
- **若選丁，A/B 怎麼做**：不適用。

## Q2 YG-03 / LG-09 的單件背景虛化句

- **`the balcony behind her falling out of focus`**：**維持原樣。**
- **`with the shop behind her softly out of focus`**：**維持原樣。**
- **`the wall menu out of focus`（含亂碼文字風險）**：**維持原樣，不改成 visible rows。**
- **理由**：前兩句是既有、低強度的背景呈現控制，沒有指定焦段、主體焦平面或「只有臉清楚」，不應因 R14 的未實測禁令被追溯刪除。第三句更有獨立的瑕疵防護作用：菜單是模型最容易生成偽文字的物件，`visible rows of menu panels` 雖未直接要求字可讀，仍會提高菜單結構與字形的顯著度，和「降低亂碼文字成為可見瑕疵」的目標衝突。原句讓菜單仍作為早餐店背景線索存在，同時降低偽文字可辨識度，較像真實相機拍攝，也較安全。

## Q3 禁令範圍劃分

- **判定**：**實務處置成立，但分類理由要改寫。** 背景 `out of focus` 在光學語意上仍然是景深語言，不能寫成「不屬景深語言」；它可沿用的真正理由是：這幾個低強度、局部背景措辭已有專案內使用證據，而指定鏡頭、壓縮感、主體焦平面及排他性清晰範圍的措辭仍是 0 次實測。規則應採「精確 allowlist＋其餘先禁」而非只靠「主體／背景」語意判斷。
- **理由**：單純以主體／背景切分仍有灰區，例如 `background completely blurred`、`creamy bokeh`、`only the subject in focus` 都是在寫背景，卻會強烈改變光學效果；反之，現有 `the wall menu out of focus` 只是局部物件的弱控制。真正穩定的分界是「已驗證的低強度精確句型」與「會引入新光學機制或強度的未驗證句型」。
- **要補進禁用清單的措辭**：除既列的 `short telephoto`、`compressed`、`shallow depth of field`、`her face sharp` 外，補入 `bokeh`／`creamy bokeh`、`razor-sharp`／`tack-sharp`、`only X in focus`、`focus plane`、`deep depth of field`／`everything sharp`、`completely/heavily blurred background`、焦距毫米數、光圈／f-stop。允許項不要概括成所有背景虛化，而應只登記現有已驗證的精確字串（含 `softly out of focus`、`falling out of focus`、`the wall menu out of focus`）；任何新同義詞或更強程度詞先視為未驗證。

## Q5 六件最終判定

| 件 | PASS / REVISE | 理由 | 具體改法（改前→改後） |
|---|---|---|---|
| YG-03 | **PASS** | R15 的景別名稱已換成可見物清單；自拍方位、單手構圖、具名牆面反光與曝光關係成立。保留的陽台背景虛化屬現行 allowlist，不需再改。 | 無。 |
| YG-06 | **PASS** | 已消除「後方機位再繞回」的互相抵消，改為固定左後方位與臉、毛巾角可見清單；共用路人 v1 有 14/14 實證，維持原樣。 | 無。 |
| YG-08 | **PASS** | left/right 已取代 near/far，兩個手物接觸點有唯一指派；雙色溫、門口高光犧牲、柱框景與公共路人均成立。 | 無。 |
| YG-09 | **PASS** | 已移除 `face sharp`，改以臉佔比、建築立面寬度與窗列定義畫內視線目標；沒有再控制未實測的焦平面。 | 無。 |
| LG-09 | **PASS** | 景別已換成可見物清單；手、杯、吸管的單一瞬間清楚。商店與菜單的低強度背景虛化可沿用，且菜單模糊可降低偽文字顯著度。 | 無。 |
| LG-10B | **PASS** | 已保留但精簡正面方位，景別改為可見物清單，反射表面改成具名石板參道；路人 v1 維持已驗證版本。 | 無。 |

## 補充

- 最終結論：**6 件全部 PASS，可送生成；本輪不再改 prompt 字串。**
- 建議把規則名稱從籠統的「景深語言禁令」改成「未驗證光學／焦點控制禁令」，並在其下維護精確 allowlist。這樣能保留 10 件既有背景虛化證據，也不會讓新的強景深同義詞從「只是背景」這個漏洞進入。
