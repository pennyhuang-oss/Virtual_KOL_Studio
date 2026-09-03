# 覆核請求 R4：AI 感消不掉，而且我的修正反效果

R3 的五題全部照做了，5 張訓練圖生出來。**使用者的評語是「可以用，但 AI 感還是有一點重」。**
她要我去參考 repo 裡最早驗證成功的 `iris-chen` 模板，我照做了，**修正無效，而且可能讓畫面更假**。
這一輪不是問流程，是問**寫法**。

---

## A. R3 的裁決執行結果（先報帳）

| R3 的裁決 | 執行結果 |
|---|---|
| Q-11 路線 1：純臉緊裁切 + `category: auto` + description 明寫不得推導身材 | **部分成功**。胸型改善、明顯優於原本，但不及完全不掛 element。使用者判定臉可接受 |
| Q-11 `category` | **關不掉**。填 `auto`，伺服器回傳 `auto:character`。你建議的純歸因實驗做不到 |
| Q-12 可發布下限清單 | 全數採用 |
| Q-13 5 張配額表 | 全數採用，5 張全部照你的角度／景別配置 |
| Q-14 身材分布 2 全身 + 1 腰上 + 2 胸上 | 照做 |
| Q-15 低人流／私密場景 | 直接解決了。她的人設場景（蘇州老宅、自家旗袍店、清晨園林、天井）**本來就合理獨處**，不需要假造空景公共場所 |

使用者另外裁決：**#2 那張不重做**（她認為可用），只補生缺的兩張。

**產出：5 張裡 3 張可用（#1 #2 #3），2 張全身圖因背對鏡頭作廢，補生後 1 張救回、1 張仍失敗。**

---

## B. 問題一：AI 感（這是主問題）

### B-1 我寫的 vs repo 裡驗證成功的，方向相反

`kols/iris-chen/generation_notes.md` 是本專案最早驗證成功的生活照模板：

- 全長**約 90 字**，逗號分隔的關鍵字串，不是散文
- 固定尾巴：`film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style`
- 明列原則：「**不要過度打光或過於精緻的構圖**」「是網紅在 Instagram 發的生活照，不是雜誌大片」

我寫的：**每張 2,300–2,500 字元的散文**，每一張都配完整的五段式物理光線
（具名反射面＋色溫分裂＋曝光取捨＋遮擋物），道具清單每張 5–6 項，**完全沒有 film grain / candid 那一層**。

等於我把訓練集的每一格都佈成了雜誌內頁的燈光。

### B-2 我做的修正，以及它為什麼算失敗

補生兩張時，我把 Iris 的風格層加回去：
`Candid lifestyle photo, an ordinary phone snapshot of the kind posted to Instagram without editing,
fine film grain, shot on 35mm, warm natural colour grading, slight highlight clipping,
faint JPEG compression at high-contrast edges.`

**結果：#4 v2 看起來比 #4 v1 更像精修大片，不是更像隨手拍。**
而且我寫的 `flat grey overcast morning light, no sun and no hard shadow edge`
被模型換成強烈暖色逆光＋輪廓光；指定的 `plain matte weave` 旗袍變成亮面緞。

### B-3 我自己的假說（請評估，我沒有把握）

**風格關鍵字被長度稀釋。** Iris 的模板全長 90 字，風格尾巴佔約三成；
我的 prompt 2,400 字元，同一段尾巴只佔十分之一，
而且前面有大量佈光敘述在把畫面往電影感拉。

### B-4 一個可能更重要的 repo 內部矛盾

`SEXY_SCENE_LIBRARY.md` §3（2026-08-05，從競品 @sherry_digitalp510 拆解而來）要求
把光線寫成五段式物理規格。但 `iris-chen/generation_notes.md` 的原則是「不要過度打光」。

**而且：`iris-chen/generation_notes.md` 2026-08-05 批次的結論明寫——**

> 🔴 **打光尚未套用新公式。** 本批次仍使用舊的寫法…**下一批次應以驗證該公式為首要目標**。

也就是說**那套五段式公式從來沒有被實際生成驗證過**。我這 5 張是第一批真的套用它的，
而使用者的第一反應就是 AI 感偏重。

競品 Sherry 的帳號本身走的是**光鮮亮麗的網紅風**；
`wanyin-jiang` 要的是**蘇州老宅的日常真實感**。
把從前者拆出來的佈光公式全套搬到後者，可能本身就是錯配。

---

## C. 問題二：角度／朝向不被執行

| 寫法 | 結果 |
|---|---|
| v1：`standing almost square to the camera and turned no more than fifteen degrees` | **全背面**，臉完全看不到 |
| v2：`She is facing the camera: her face, the front of her body and both shoulders are toward the lens and her feet point toward it. Her back is not to the camera.` | **成功**，正面 |
| v1：`her body turned about fifty-five degrees away from the camera with her head turned back` | 全背面 |
| v2：`Her shoulders are turned about fifty degrees away but her face is fully turned back to it and she is looking straight into the lens` | **仍是約 140 度全背面**，只有頭轉回來 |

正向敘述在**正面**構圖有效，在**要求特定側轉角度**時仍然失效。
這與本專案既有發現一致：結構性的角度上限／否定詞不被執行。

服裝也一起被改寫：指定 `fitted long-sleeved practice top`，出來是露背款。

---

## D. 需要你回答

### Q-16　AI 感的主因是哪一個？請排序，不要全列

候選（我列的，可能有漏）：
1. prompt 太長，風格關鍵字被稀釋
2. 五段式佈光公式本身就會把畫面推向電影感／雜誌感
3. 缺少 film grain / 35mm / candid 這一層（但我加了沒用）
4. 道具與場景敘述太完整，變成「被美術設計過的場景」而不是隨手拍
5. 散文句式本身（vs 逗號關鍵字串）
6. `seedream_v4_5` 對「漂亮亞洲女生」有很強的精修先驗，文字壓不掉

**請給排序，並指出哪一個是我應該第一個動的。**

### Q-17　五段式佈光公式要不要退回去？

它從來沒有被生成驗證過，而我第一次套用就得到 AI 感偏重的評語。

- 要不要**全面停用**，回到 Iris 的簡短寫法？
- 還是**分場景**用（哪些場景該用、哪些不該）？
- 還是保留但**大幅縮短**？

如果你認為要保留，請說它在哪一類場景上是必要的，而在 `wanyin-jiang` 這種
「老宅日常」的場景上該怎麼調。

### Q-18　prompt 該多長？

Iris 的模板 90 字有效。我的 2,400 字元。中間值在哪？
**請直接給一個目標長度或結構**（例如：身分固定段 X 字、場景 Y 字、風格尾巴 Z 字），
我要拿來當所有 19 位的模板。

注意：短 prompt 會丟掉 R3 Q-12 你自己給的那份可發布下限清單裡的一些要求
（膚質、遮臉、自拍畫質等級）。**這兩者要怎麼並存？**

### Q-19　側轉角度怎麼寫才會執行？

正向敘述解決了「正面」，沒解決「45–60 度」。
- 有沒有寫法能讓模型真的執行特定側轉角度？
- 還是應該**放棄用文字控制角度**，改成別的手段（例如接受它給的角度，只要臉可辨識就收）？
- 如果放棄，R3 Q-13 那份 5 張角度配額表要怎麼改才務實？

### Q-20　最省的驗證方式

我不想再一張一張試錯。**請直接給一組最小對照實驗**：幾張圖、每張變什麼，
能一次把 Q-16 的排序測出來。使用者對「反覆試錯燒 credit」已經明確表達不滿，
所以這一組必須小而且結論明確。

---

## E. 現況

- 已花：**15 credits**（4 失敗候選 + 3 診斷 + 1 element 測試 + 5 訓練圖 + 2 補生）
- 餘額：**1,333**
- 可用素材：#1 #2 #3 #4v2 共 4 張（#5 待解）
- element `a0e68491-43ac-40c8-99d5-fec60596ac50`（純臉版）使用者已核可
- **在你回覆之前不再送任何生成**

檔案：
- 5 張與補生圖：`review/soul_pilot/wanyin-jiang/train5/`
- 逐張判讀與 prompt 全文：`train5/prompts.json`、`train5/prompts_v2.json`
- 對照圖：`train5/contact_sheet.jpg`、`train5/face_check.jpg`、`train5/v1_vs_v2.jpg`

---

## REPLIES BELOW

<!-- ChatGPT 的回覆貼在這一行下面。上面的內容不要動。 -->
