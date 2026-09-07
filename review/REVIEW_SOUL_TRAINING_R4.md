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

### Q-16

**結論：主因排序是 ② 五段式佈光公式 ＞ ④ 場景／道具過度美術設計 ＞ ⑥ Seedream 的精修先驗 ＞ ① prompt 過長 ＞ ③ 缺少 Iris 風格尾巴 ＞ ⑤ 散文句式；第一個要動的是全面拿掉生活照裡的五段式佈光。**

這個排序不是把所有可能性並列，而是依現有對照的解釋力排序：

1. **② 五段式佈光公式。** 它要求具名主光、反射面、雙色溫、曝光取捨、遮擋與光影形狀；這些正是攝影棚／電影劇照的 art direction 語言。五張又每張都套完整公式，模型自然把「精心設計的光」當成全套視覺目標。這套公式在 repo 中原本只是待驗證假說，wanyin 是第一批負面資料，不能再視為已驗證規則。
2. **④ 場景與道具太完整。** 每張都有 5–6 個精確擺放、材質與磨損狀態都被指定的物件，連背景的反光與遮擋都有功能；成圖因此像美術部搭出的「生活感」，不是碰巧拍到的生活。
3. **⑥ Seedream 的精修先驗。** 對照圖裡人物皮膚、旗袍、構圖對稱性與輪廓光都有明顯 fashion/editorial 偏好；#4v2 把平光改成暖逆光，支持模型先驗存在。但 prompt 同時給了園林、絲質旗袍、35mm、warm grading、highlight clipping 等訊號，現階段不能把全部責任推給模型。
4. **① prompt 過長。** 「風格詞按字數比例被稀釋」不是可靠機制；模型不是按尾巴佔全文百分比線性加權。真正問題是長 prompt 累積了太多互相競爭、又都指向高製作價值的要求，使簡單的 candid 指令失去決策優先級。因此要縮短，但縮短是移除過度設計的手段，不是單純追求字少。
5. **③ 缺少 film grain／35mm／candid 層。** 已有一次負面資料：加回後沒有變自然，反而更像類比精修 editorial。`35mm`、`warm tones`、`film grain` 本來就可描述高級時尚攝影，不能當成去 AI 感開關。
6. **⑤ 散文句式。** 沒有證據顯示逗號關鍵字串本身比完整句更自然；差異主要在資訊量與內容，而不是標點。短句或逗號都可以，只要每個片語只有一個可見任務。

另需更正一個判讀：#4v2 的實際 prompt 是 `silk qipao, plain weave`，沒有寫 `matte`。因此亮面緞感是模型偏好與 `silk` 的結果，但不能記成模型違反了明確的 `matte` 指令。

### Q-17

**結論：五段式佈光不要全面刪除，但要從生活照／Soul 訓練圖的預設模板中停用，只保留給明確要做 editorial、廣告或戲劇性場面的內容。**

分場景規則如下：

- **不用五段式：** 日常自拍、家中起居、工作隨拍、清晨散步、咖啡桌、老宅生活、普通街拍，以及所有以「朋友拿手機順手拍到」為目標的訓練圖。
- **可用縮短版：** 場景本來就有一個明確光源，而且光是敘事的一部分，例如窗邊晨光、檯燈夜讀、店門自然光。只寫「一個主光來源＋一個自然結果」，最多一句，不寫具名反射面、測光策略、色溫分裂、clip／crush 與遮擋圖案。
- **才用完整版：** 明確要求電影劇照、品牌 campaign、舞台、夜店、霓虹、戲劇性逆光、產品廣告，或需要精確重現競品 Sherry 的光鮮網紅風時。它應是風格 preset，不是所有人物的基礎規則。

wanyin 的老宅日常應改成例如：`Soft ordinary window light in the old house, with the room behind her naturally a little darker.` 到此為止。若是陰天園林：`Flat overcast daylight, even and slightly cool, like an ordinary phone photo after rain.` 不再指定池水補光、牆面反射、曝光測點、剪影或幾何投影。

也不要機械地退回 Iris 的固定暖色尾巴。Iris 模板可保留的是「不過度打光、不過度構圖」原則；`warm tones / 35mm / film grain` 是否適合要由人物與場景決定，不能跨 19 位固定套用。

### Q-18

**結論：19 位共用模板以 140–180 個英文單字為目標，硬上限 200 字；分成 6 個短段或逗號片語，不再寫 2,300–2,500 字元的攝影散文。**

建議固定結構：

| 區塊 | 目標長度 | 內容 |
|---|---:|---|
| 身分引用＋景別 | 15–25 字 | element、年齡／地點、close／waist／full、正面或 front three-quarter |
| 只保留可見的身材／臉部不變項 | 25–35 字 | 骨架、胸腰反差、膚色；不重複同義形容詞 |
| 髮型＋服裝 | 20–30 字 | 一套衣服、材質只留一個關鍵詞、臉部需露出的部位 |
| 動作＋場景 | 30–40 字 | 一個自然動作、2–3 個場景證據；不列完整道具清單 |
| 光線＋拍攝媒介 | 20–30 字 | 一個主光結果、phone／rear camera／front camera 擇一 |
| 單人與構圖硬條件 | 20–30 字 | only person、手臂連接、全身圖的頭腳完整等必要 gate |

R3 Q-12 的可發布下限不應全部塞進 prompt。兩者用三層分工並存：

1. **Prompt 只寫模型必須畫出的東西：** 人物、服裝、動作、場景、簡單光線、景別、單人。
2. **Spec／validator 管生成參數：** 解析度、長邊 960 px、自拍數量、場景與服裝分散、是否為近重複圖。
3. **成圖 QA 管不可接受結果：** 美顏臉、廣角變形、壓縮、噪點、動態模糊、遮臉、錯手、第二人物、身材漂移。

只有當某個缺陷已在該模型反覆出現時，才把一條短限制升回 prompt；不要把整份 QA checklist 當成生成描述。Capture 尾巴也只能選一套：例如 `ordinary unedited rear-phone snapshot, natural colour, slight sensor noise, imperfect framing`。不要同時寫 phone、35mm、film grain、JPEG compression、crisp detail，這些媒介訊號會互相競爭。

### Q-19

**結論：不要再用「turned away／looked back／over her shoulder」或精確 45–60° 數字控制身體；改寫成 front three-quarter 的可見幾何，並把 5 張配額從角度數字改成結果式驗收。**

`turned away`、`look back` 和 `over shoulder` 都直接喚起背影構圖先驗；後面再要求雙眼可見，模型也可能只把頭轉回來。較可行的寫法是：

`Front three-quarter view. The camera is positioned diagonally in front of her, not behind her. Her near shoulder is slightly closer to the lens, while the far shoulder, both eyes, the front of her chest and the front of her waist remain visible in the same frame.`

這仍不保證精確 50°。不確定 Seedream 能否只靠文字穩定落在指定角度，建議只用 **1 張圖**測上面這句；若仍生成背面，立即停止文字角度微調，不再換同義詞抽卡。需要精確姿勢時改用 pose／composition reference 或 image edit，但 pose reference 必須先確認不會重新帶入錯誤身材。

5 張的務實配額改為：

1. 正面胸上：雙眼、雙眉、完整下顎可見。
2. 左側 front three-quarter 胸上：雙眼可見，左側臉型資訊增加。
3. 右側 front three-quarter 腰上：雙眼與胸腰正面仍可見，右側臉型資訊增加。
4. 正面全身：臉、身體正面、雙肩、雙腳都朝鏡頭，頭腳完整。
5. front-oblique 全身／及膝：近肩略靠前、遠肩仍可見、胸腹正面仍可讀；實際落在約 20–40° 即通過，不再追求 45–60°。

只要五張提供正面、左右兩側臉型與兩種身材視角，而且臉可辨識、身材正確，就比為了命中 55° 而收下一張背影更有訓練價值。真正的 60°／側臉可移到 Soul 訓練後的壓力測試，不佔五張稀缺名額。

### Q-20

**結論：最小封閉實驗是 4 張新圖，加上既有 #1 作零成本 control；同一 element、seed、場景、人物、服裝、動作、構圖、尺寸與模型設定，四張生成後一次盲評，禁止 reroll。**

先從 API 取回 #1 的原 seed。既有 #1 是 C0，不重生。新增四張：

| 圖 | 唯一目的 | 相對前一可比版本的變動 |
|---|---|---|
| **T1** | 測 ② 五段式佈光 | 沿用 #1 全文，只把完整五段式光線段替換成一句 `Soft ordinary morning window light, even phone exposure.`；其他逐字不動 |
| **T2** | 測 ①＋④＋⑤ 的「短模板／低美術設計」組合 | 以 T1 為內容基準縮成 140–180 字；道具只留 2 個，改成短段／逗號片語；不加 Iris 尾巴；capture 只留 `ordinary unedited rear-phone snapshot, natural colour, imperfect framing` |
| **T3** | 單獨測 ③ Iris 尾巴 | 與 T2 逐字相同，只把 capture 片語換成 `film grain, candid lifestyle photo, warm tones, shot on 35mm, Instagram style`；不得同時保留 phone 尾巴 |
| **T4** | 測 ⑥ Seedream 先驗 | T2 prompt 原文不變，只把模型換成 `gpt_image_2`；若不同模型不接受相同 seed，仍只生 1 張並記為模型級對照，不追加抽樣 |

先把 C0、T1、T2、T3、T4 隨機改名 A–E 做同尺寸接觸表，請使用者只回答兩件事：「最不像 AI 的一張」與「可直接發布的所有張」。在揭盲前不要告訴她哪張是哪種 prompt。預先寫死採納規則：

- T1 明顯優於 C0：五段式從生活照模板退役。
- T2 明顯優於 T1：採用 140–180 字短模板；場景道具上限 2–3 個，散文不再回補。
- T3 優於 T2：Iris 尾巴可保留；T3 持平或更差：19 位模板刪除固定 35mm／warm／film-grain 尾巴。
- T4 優於 T2且臉、身材都過：Seedream 先驗是主要剩餘因素，後續改用 `gpt_image_2`；若身份或身材退步，即使質感較自然也不換。
- C0、T1、T2、T3 都相近，而 T4 明顯較自然：⑥ 升為第一主因；停止在 Seedream 上繼續改 prompt。
- 五張都不達可發布：停止，不再加同義詞或換 seed；結論是現有 element／模型組合有不可由這些文字槓桿解除的質感上限，回到模型或 reference 管線決策。

這組成本固定為 **4 張圖，最多 4 credits（若 `gpt_image_2` 單價不同則先查價，但仍只生成 1 張）**。它不能在統計學上把六個因素完全獨立估計；那至少需要更多單因子重複，與本輪 stop-loss 衝突。但它能一次回答所有會改變 19 人模板的決策：是否停用五段式、是否縮短、是否保留 Iris 尾巴、是否換模型。
