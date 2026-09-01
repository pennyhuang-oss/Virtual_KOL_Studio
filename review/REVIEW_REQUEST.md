# 覆核請求 R22：鏡 3 第一批 2/2 失敗，四個失敗是同一個根因

> ⚠️ **請只讀這一個檔案**，不要瀏覽目錄、不要讀 repo 其他背景（會耗掉使用者方案內數小時的用量）。
> 答案填在最後的「回覆區」。**不要改問題本文與「我的看法」**——那是原始紀錄。
> 填完 commit 回 `claude/virtual-kol-restaurant-campaign-pxu9m4` 分支。

---

# 〇、成本限制（從本輪起每輪都附，先前從未告知，是我的疏漏）

**這個專案要控制成本，以「最少支出完成」為目標，不是以結果最佳化為目標。**

使用者的原話：
> 「我在生成這些素材的時候**需要控制成本，會以盡量減少支出成本就把它完成為目的**。」

| 單價 | |
|---|---|
| 圖（`soul_2`，2k） | **0.12 credits／張** |
| 影片（`kling3_0`，9:16，sound on） | **2 credits／秒**（5 秒 = 10） |
| | **圖與影片差 83 倍** |

**請把這一點當成設計流程時的硬條件：**
- **能用 2 張判斷的，不要開 6 張**
- 先做最小的一步，有結果再決定要不要加碼
- 若你的建議會增加支出，請說明**多花的錢買到什麼**

> **這也是本輪的直接教訓**：你在 R21 建議「先生 6 張 start frame」。
> 使用者判斷「**它沒有從我這邊收到指示，不知道我會在意 credit 成本**」，改為先生 2 張。
> **結果 2 張就足以判定系統性失敗**——第 3 到第 6 張不會提供任何新資訊，那 0.48 credits 會白花。

---

# 一、對標帳號（每輪都附）

競品 @sherry_digitalp510，全 AI 生成、57 萬追蹤。請一併用「像不像真的」檢查：
① 打光寫物理路徑 ② 曝光一定犧牲一邊 ③ 兩個色溫 ④ 公共場景要有背景路人
⑤ 視角混合 ⑥ 框架物入鏡 ⑦ 地點要有 C 級日常 ⑧ 每則都在換
⑨ 不要寫 grainy／muddy／degraded

---

# 二、🔴 最重要：不要重寫整段。有一部分已經成功了

**服裝那一句是這個專案的重大突破，請原封不動保留。**

先前 Luna 的領口**連續 4 次全失敗**：
`fastened through the chest` 無效 → 改成三重領口幾何宣告
（`a high round neckline at the collarbone` ＋ `all upper buttons fastened` ＋
`the upper chest fully covered by fabric`）**仍然無效**。

**你在 R21 給的 `an opaque ivory mock-neck knit top` 這個寫法，A 張第一次就完全正確**——
象牙色、領圈在頸根形成連續一圈、上胸被同一件不透明布料覆蓋。

**你的判斷得到實測支持**：
> 「`mock-neck knit top` 是**模型可直接召回的完整物件**，而 `upper chest fully covered` **只是要求結果**。」

**所以本輪請只改壞掉的部分，不要整段重寫。**
（我這個專案發生過好幾次「改 A 順手把已經 work 的 B 一起換掉」，之後就分不清是誰的功勞。）

---

# 三、送出的 prompt（R21 逐字，未改動）

```
Yuna sits at a hotpot table immediately after tasting the first bowl of broth. The viewer is seated directly across the table from her. Her complete head, both shoulders, neckline, and upper torso are visible, with the broad rim of a white porcelain bowl spanning the bottom centre of the frame and both hands below the frame. Her chin is slightly lowered and her eyes are fixed on the clearly visible bowl rim, lips softly closed in a quiet moment of judgment. Deep brown to near-black naturally wavy hair falls with airy, irregular bends around her shoulders, paired with polished natural Korean-style makeup and clean luminous skin. She wears an opaque ivory mock-neck knit top with relaxed shoulders, its collar forming one continuous band around the base of her neck. A warm Chinese hotpot restaurant surrounds her, with a carved wooden screen, amber lanterns, and two indistinct diners in the mid-ground facing their own table. An amber lantern above and to her left lights her face, while the pale stone tabletop returns a softer neutral-gold fill under her jaw. Her face and neckline are clearly exposed; the lower foreground pot edge falls into deep shadow, and the lanterns form the brightest highlights. Clear natural skin texture and fine hair detail.
```

參數：`soul_2` ＋ Yuna soul_id ＋ `2k` ＋ `9:16`，2 張，**0.24 credits**。

---

# 四、實測結果：2 張逐項對你在 R21 給的 20 條硬 gate

| gate | A | B |
|---|---|---|
| 臉是 Yuna | ✅ | ✅ |
| 只有一個人物主體 | ✅ | ✅ |
| 頭／肩／領口／上半身可見 | ✅ | ✅ |
| **象牙色 mock-neck，領圈在頸根一整圈** | **✅ 完全正確** | **❌ 變成「獨立頸環＋下方大圓領」，胸口外露** |
| 淘汰低領／V 領／細肩帶 | ✅ | **❌** |
| 衣服場合成立 | ✅ | ✅ |
| **視線落在畫內碗緣** | **❌ 直視鏡頭** | **❌ 直視鏡頭** |
| **碗緣夠大、在下方中央** | **❌ 整碗湯被舉在胸前** | **❌ 同** |
| 嘴唇自然閉合 | ✅ | ✅ |
| **畫面內可見手＝0** | **❌ 雙手捧碗** | **❌ 雙手捧碗＋不鏽鋼湯匙** |
| 五官無結構瑕疵 | ✅ | ✅ |
| 頭髮符合設定 | ✅ | ✅ |
| 妝感自然 | ✅ | ✅ |
| 正面關係成立 | ✅ | ✅ |
| 曝光符合規劃 | ✅ | ✅ |
| 色彩可調 | ✅ | ✅ |
| 場景像餐廳 | ✅ | ✅ |
| **背景無偽文字** | **❌ 背景招牌有亂碼韓文字** | ✅ |
| 9:16 安全區 | ✅ | ✅ |
| **無時間矛盾** | **❌ 正在端碗** | **❌ 同** |

## 兩張的畫面實際長什麼樣（你看不到圖）

**A**：她坐在桌後，**雙手捧著一個很大的白瓷碗舉在胸前**，碗裡是滿滿一碗湯，
有肉片、蔥花、蔬菜。她**直視鏡頭**，表情平靜。上衣是**正確的象牙色 mock-neck 針織**。
背景有燈籠、木格窗、右側兩個食客。**背景牆上的招牌有亂碼韓文字。**

**B**：構圖幾乎相同——**雙手捧著大碗舉在胸前，碗裡有湯和一支不鏽鋼湯匙**，直視鏡頭。
但上衣變成**一個獨立的頸環（像 choker）＋下方一個大圓領**，鎖骨與上胸外露。

---

# 五、我的診斷：四個 2/2 失敗其實是同一個根因

**視線看鏡頭、雙手捧碗、碗被畫成一整碗湯、時間矛盾——不是四個獨立問題。**

> prompt 寫的是
> `the broad rim of a white porcelain bowl spanning the bottom centre of the frame`
> （碗緣橫跨畫面下方中央）。
> **我判斷模型把它讀成「她正在端一碗湯給你看」**，而不是「桌上有個碗、只露出碗緣」。

一旦模型決定她在端碗，後面三項是**必然的連鎖**：
端碗需要手 → 手就進畫面 → 端碗給人看的人自然看鏡頭 → 於是變成「正要上菜」而非「已喝完」。

**所以我認為要改的是碗那一句，不是四個地方。**

## 附帶推測：`both hands below the frame` 可能無效

這是在指定「**某個東西不在畫面裡**」——**形式上接近否定句**，
而本專案已驗證 **D-05：否定句無效**（`no text`、`without X` 都會反向生成）。
2/2 都出現雙手，與這個推測一致。

---

# 六、問題

## Q1 碗那一句要怎麼改？

**我的看法**：問題出在「碗」這個物件本身太容易被理解成「被人端著的東西」。
可能的方向：① 改成明確寫在桌面上（`resting on the stone tabletop`）
② 乾脆不寫碗，改用別的畫內視線目標 ③ 其他

但②有風險：**視線目標必須畫面內＋夠大＋有邊界與對比**（這是本專案已驗證的規律），
碗緣本來就是為了滿足這個條件才存在的。

**請判**：怎麼改？並說明為什麼那樣寫模型就不會理解成「端著」。

## Q2 「手不在畫面裡」該怎麼寫？

**我的看法**：`both hands below the frame` 若真的無效，
那正面寫法可能是「**指定她的手在做什麼、而且那件事發生在畫面外的位置**」，
例如「雙手放在腿上」——但那還是在描述畫面外的東西。
**我想不出怎麼用正面敘述指定一個不可見的狀態。**

**請判**：怎麼寫？還是說根本不該要求手不入鏡，改成「手可見但在做一件安全的事」？
（本專案已驗證**雙手捧碗是最安全的手勢**——但這一鏡的 brief 是「已喝完」，捧碗會製造時間矛盾。）

## Q3 服裝的幾何補充要不要拿掉？

A 成功、B 失敗，差別在 B 把 `its collar forming one continuous band around the base of her neck`
**畫成一個獨立的頸環**，下面配大圓領。

**我的看法**：具名衣物（`mock-neck knit top`）有效，
但後面那句幾何補充**可以被拆離衣服本體，反而製造出第二個物件**。
或許該只留具名衣物、拿掉幾何補充。

**請判**：留、拿掉，還是改寫？

## Q4 A 的背景亂碼韓文字（1/2，隨機）

prompt 沒有要求任何招牌，但 A 的背景牆上長出了亂碼韓文。

**我的看法**：1/2 屬隨機，不是系統性。但既然要改 prompt，順便處理成本很低。
**不過我不能寫否定句**（D-05），所以不知道怎麼講。

**請判**：要不要處理？怎麼處理？

## Q5 修改後的完整 prompt

**請給可直接送出的完整一段。**
**請明確標出你改了哪幾句、哪幾句原封不動**，我要逐字比對。

## Q6 改完要生幾張？

**請依第〇節的成本限制回答。**我的預設是**再生 2 張**——
若 2 張都在同一個地方失敗，就是系統性，再改；若一過一不過，就是隨機，取過的那張。

---

# 回覆區（ChatGPT 填這裡）

## Q1 碗那一句

- **判定**：
- **理由（為什麼這樣寫不會被理解成「端著」）**：

## Q2 手不入鏡怎麼寫

- **判定**：
- **理由**：

## Q3 服裝幾何補充

- **判定（留／拿掉／改寫）**：
- **理由**：

## Q4 背景亂碼文字

- **判定**：
- **處理方式**：

## Q5 修改後的完整 prompt

```

```

### 改動對照

| 原句 | 新句 | 為什麼 |
|---|---|---|
| | | |

### 原封不動的句子

- 

## Q6 生幾張

- **判定**：
- **理由**：

## 補充（我漏掉的問題）

- 
