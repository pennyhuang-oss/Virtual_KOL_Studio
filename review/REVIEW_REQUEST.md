# 覆核請求 R15：R14 之後改動的 6 件，逐件判定

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

## 背景速查（已驗證結論，不用回頭查）

| 代號 | 結論 |
|---|---|
| D-01 | 不要寫族裔詞與身體數字，soul 已鎖臉 |
| D-02 | 相機用相對描述（`at her chest level`），不要寫公制距離 |
| D-05 | **否定句無效**（`no text`、`without X` 都會反向生成），要改寫成正面的可見物清單 |
| D-06 | 表情要綁一個實體動作，不能只寫情緒詞 |
| D-09 | 一張靜態圖只能承載**一個瞬間** |
| R13 | 景別不要寫 `half body`／`full body` 這種名稱，要**列出必須看得見的東西** |
| R13 | 視線目標必須**在畫面內、夠大、必然會被畫出來** |
| R13 | 領口要寫**這一件衣服的幾何**（`high crew neckline`），不要寫扣子扣到第幾顆 |
| R14 | 每件都要明寫**相機方位**（在她的哪一側）；順序是 ① 方位 → ② 高度距離 → ③ 只在硬驗收需要時補身體朝向 |
| R14 | **焦段與景深語言 0/21 實測，一律先移除**，等兩個獨立 A/B（焦段用 LG-09、景深用 YG-09）通過才可用 |

**模型可用參數只有**：`quality=2k`、`soul_id`、`aspect_ratio=9:16`、`prompt`、1 張參考圖。
**沒有 negative_prompt、沒有 seed。**所以所有限制都必須寫在正面敘述裡。

---

## 這 6 件在 R14 之後改了什麼（改前／改後）

| 件 | 改前 | 改後 |
|---|---|---|
| **YG-03** | （沒有任何方位詞） | 加 `the phone camera held slightly to her front-right and just above eye level` |
| **YG-06** | `three-quarter back` | `shot from her rear-left quarter, far enough around her side that her upward-tilted face remains fully visible in three-quarter profile` |
| **YG-08** | `shot from her side in profile`；柱子在 `far outer edge`；兩手寫 hand A/B | `shot from her three-quarter front-left at chest level`；柱子改到 `far outer right edge`；兩手改成 `near hand`／`far hand` |
| **YG-09** | `shallow depth of field, only her face sharp` | `Shot from slightly on the window side in a three-quarter close-up at her eye level, with her face sharp and the broad building facade still recognisable beside it` |
| **LG-09** | `on a short telephoto with the shop behind her compressed`；`both forearms supported` | `shot from her three-quarter front-right at her eye level, with the shop behind her softly out of focus`；`one forearm resting lightly on its edge` |
| **LG-10B** | （沒有方位詞）＋ 一句 telephoto | 刪 telephoto，加 `shot straight-on from directly in front of her at chest level`（**刻意保留的正面**） |

改完後：**未生成的 9 件全部有明寫方位（9/9）**，左右側分布 3:2。

---

## 六段完整 prompt（要判定的就是這六段全文）

### YG-03（自拍／陽台收毛巾）
```
In a phone selfie, a young woman pulls a plain white towel down off the drying pole, arm still raised, smiling at the camera. The frame contains exactly one visible hand; her phone and her camera-holding hand stay outside the frame. Close half-body framing, the phone camera held slightly to her front-right and just above eye level, the balcony behind her falling out of focus. Collarbone-length mocha brown hair in a low ponytail, see-through bangs. An opaque grey fitted cropped cotton tee with a high crew neckline, high-waisted black shorts, black-rimmed glasses. A narrow covered balcony, a white painted wall, an iron window grille, plain towels on the pole. Flat overcast daylight on her face, her face evenly exposed, the white wall bouncing cool fill onto her jaw, staying slightly darker than her skin. Natural skin texture, subtle film grain.
```

### YG-06（汗蒸幕休息大廳／盤腿坐地後仰大笑）
```
A young woman sits cross-legged on a heated floor, leaning back with one hand planted on the floor behind her and her other hand relaxed on one knee, shoulders dropped, face tilted upward in a loose open-mouthed laugh with her eyes squeezed shut, a paper cup resting on the floor beside her. Her complete head, crossed legs, and both bare feet are visible, with floor visible around her seated body, shot from her rear-left quarter, far enough around her side that her upward-tilted face remains fully visible in three-quarter profile, at her seated eye level, from well back. Collarbone-length mocha brown hair in a low bun, damp strands at her temples. A grey crew-neck sauna tee and shorts, a towel folded into sheep horns on her head, bare feet. A bright sauna rest hall. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm ceiling light on her face, the wooden floor bouncing warm fill up onto her chin, the hall behind her staying readable and slightly darker. Natural skin texture, subtle film grain.
```

### YG-08（早餐店／端盤拉凳，騎樓柱框景）
```
A young woman carries a metal tray with an egg crepe in her near hand while her far hand grips the side edge of a red plastic stool and pulls it out, eyes down on the seat. Her upper body and both thighs through mid-thigh are visible, with both hand-object contact points, the tray, food, and stool seat clearly visible in the central area, shot from her three-quarter front-left at chest level, a narrow concrete pillar confined to the far outer right edge. Collarbone-length soft wavy mocha brown hair, side-parted. A light-blue collared button-front shirt knotted at the waist, its upper buttons fastened and upper chest covered, white high-waisted shorts. A breakfast shop, a steel counter. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

### YG-09（飯店房內／臉部大特寫靠窗框）
```
A young woman leans against the window frame, a nearby building facade filling the visible strip of window beside her face, her lowered eyes focused on that broad facade, lips relaxed. Shot from slightly on the window side in a three-quarter close-up at her eye level, with her face sharp and the broad building facade still recognisable beside it. The crop contains only her face, hair, neck, and bathrobe collar, with both arms and hands below the frame. Collarbone-length mocha brown hair pushed back off her face. An opaque white bathrobe with overlapping lapels closed securely at the collarbone. A hotel room, white bedding, a floor-to-ceiling window, city towers outside. Soft window light full on her face, the white bedding bouncing fill up under her jaw. Her face is clearly exposed with natural skin texture; the city outside is the brightest area, only its smallest highlights reaching white. Visible skin pores, subtle film grain.
```

### LG-09（早餐店／插吸管，上目遣い）
```
A young woman leans forward over the counter with one forearm resting lightly on its edge, holding a clear disposable plastic cup of soy milk steady with one hand while her other hand pushes a straw down through its sealed film lid, her eyes down on the cup. Half body with the cup in frame, shot from her three-quarter front-right at her eye level, with the shop behind her softly out of focus. A blunt chin-length black bob cut evenly at the jawline, centre-parted. An opaque cream fitted crew-neck knit top with a clear waistline. A breakfast shop, a steel counter, the wall menu out of focus. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

### LG-10B（祭典參道／蘋果糖，布簾框景）
```
A young woman holds a candy apple beside her cheek, her other hand resting lightly on the front of her obi, laughing, eyes toward the camera. Half body, shot straight-on from directly in front of her at chest level, plain hanging cloth curtains forming narrow blurred strips at the far left and right edges, with her face, candy apple, hands, and obi clearly visible in the centre. A blunt chin-length black bob cut evenly at the jawline, half-pinned with a hairpin. A pale-blue floral yukata, the wearer's left panel over the right, a flat navy obi. Paper lanterns overhead. A few anonymous strangers in the mid-ground going about their own business, backs turned or heads angled away, never looking at the camera, softly out of focus with slight motion blur, clearly different from her in build, age and clothing. Warm lantern light on her face, the approach underfoot bouncing warm fill up. Her face is clearly exposed with natural skin texture; the lanterns are the brightest area, only their smallest highlights reaching white. Subtle film grain.
```

---

## 問題

### Q1（YG-06）方位＋自我修正條件，會不會互相打架？

我寫的是「從她的後左四分之三拍，**但要繞得夠遠、遠到她仰起的臉仍以四分之三側臉完整可見**」。
這是一個方位詞加上一個條件子句，條件的作用是把方位往回拉。

**Claude 的看法**：R14 指出我原本的 `three-quarter back` 會讓臉被後腦與肩膀遮掉，
所以我加了條件。但我沒把握——這句同時要求「在後方」與「臉要完整」，
模型可能直接退回最安全的正側面甚至正面（那就等於方位這條又白寫了）。
替代寫法是把條件改成純可見物清單：`her full face and the towel horns on her head both visible`。

**請判**：現在這個寫法可用嗎？還是要改成可見物清單？兩者擇一，並說理由。

### Q2（YG-08）`near hand` / `far hand` 這種相對命名成立嗎？

我把兩隻手從「A/B」改寫成 `in her near hand` 與 `her far hand`。

**Claude 的看法**：既然同一句裡已經寫明 `shot from her three-quarter front-left`，
near/far 對觀者應該有唯一解。但這是我第一次用相對命名，沒有任何實測前例。
風險是模型把 near/far 理解成「離托盤近／遠」而不是「離相機近／遠」。

**請判**：near/far 在這句的上下文裡是否有唯一解？若沒有，該用什麼寫法區分兩隻手？

### Q3（LG-10B）刻意寫正面，是必要還是浪費字數？

我寫了 `shot straight-on from directly in front of her at chest level`。
這是未生成的 9 件裡唯一刻意保留的正面機位。

**Claude 的看法**：R14 說「每件都要明寫方位，包括有意保留的正面」，所以我照寫了。
但反面論點也成立：**不寫方位模型本來就給正面**，那這 10 個字就只是佔字數
（這段已 176 字，是全批最長）。

**請判**：刻意明寫正面有沒有實質作用？還是應該刪掉、把字數讓給別的限制？

### Q4（YG-09）這句還算不算「景深語言」？

原本是 `shallow depth of field, only her face sharp`（已依 R14 移除）。
現在是 `with her face sharp and the broad building facade still recognisable beside it`。

**Claude 的看法**：我認為新句已經不是景深語言，而是一份「哪個東西要清楚、哪個東西要看得出來」
的可見物清單，所以不受「景深語言在 A/B 通過前不得使用」這條限制。
但 `sharp` 這個字本身仍然是在描述對焦結果，我不確定這個區分站不站得住。

**請判**：這句該歸類為（甲）可見物清單，可以用；還是（乙）仍屬景深語言，要等 YG-09 的景深 A/B？

### Q5 六件逐件判定

每件給 **PASS** 或 **REVISE**。REVISE 請寫出**具體要改的字串**（改前→改後），不要只寫方向。
判定時請一併看：物理成不成立、硬驗收看不看得出來、有沒有 D-05 的否定句、
有沒有 R13 的景別名稱／畫外視線目標、以及**對標小雪莉那九點**。

---

# 回覆區（ChatGPT 填這裡）

## Q1 YG-06 方位＋條件子句

- **判定**：
- **理由**：
- **建議改法（改前→改後）**：

## Q2 YG-08 near/far 相對命名

- **判定**：
- **理由**：
- **建議改法（改前→改後）**：

## Q3 LG-10B 刻意寫正面

- **判定**：
- **理由**：
- **建議改法（改前→改後）**：

## Q4 YG-09 sharp 算不算景深語言

- **判定**：
- **理由**：
- **建議改法（改前→改後）**：

## Q5 逐件判定

| 件 | PASS / REVISE | 理由 | 具體改法（改前→改後） |
|---|---|---|---|
| YG-03 | | | |
| YG-06 | | | |
| YG-08 | | | |
| YG-09 | | | |
| LG-09 | | | |
| LG-10B | | | |

## 補充（若有跨件的橫向問題請寫在這裡）

- 
