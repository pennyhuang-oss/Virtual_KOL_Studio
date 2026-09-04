# Virtual KOL Studio — Sexy Scene Library

> 親密生活風格場景庫。所有場景以 SFW 為前提，強調身體存在感、自然親密感與寄生社交效果。
> 生成前請依各角色的 `character.md` 調整 outfit 細節、光線偏好與鏡頭公式。

---

## 使用原則

- **視角是輸出照片的視角，不是拍攝動作**：不要描述「她拿著手機自拍」，而是描述「close-up front-facing selfie shot, slightly overhead angle looking down at camera」
- **真實感優先**：加入 `candid moment`、`slightly off-center composition`、`film grain`，避免完美置中構圖
- **光線是主角**：每個場景的光線描述比服裝描述更重要，光線決定氛圍
- **Prompt 結尾標配**：所有場景在 prompt 末尾加入 `film grain, candid lifestyle photo, shot on 35mm, warm tones, slightly off-center composition`

---

> 📄 **2026-08-27 新增：[`PHOTO_DIRECTION_STANDARD.md`](PHOTO_DIRECTION_STANDARD.md)**
> ——網美／街拍攝影的實際做法（相機參數、構圖、姿勢、道具、風格、AI-tell），
> 以及送生成前的十項稽核表。**每批生成前先過那份，再看本檔的反 AI 感檢查表。**

## 降低「AI 感」的技術要點（2026-07-24 新增）

> 真正決定生成結果精準度與真實感的是這些技術參數寫得夠不夠具體——不是靠對標哪個真人帳號。以下五項是常見反饋「還是看得出 AI 感」的主因，每個場景 prompt 都應該檢查是否涵蓋。

### 1. 皮膚質感
多數生成模型預設會往「打磨過、無瑕疵」的方向走。**每個 prompt 都要主動加入**：
```
visible skin pores, subtle natural skin texture, slight oil sheen on T-zone,
unretouched skin detail, natural skin imperfections
```
**避免使用**會把畫面推向塑膠感的字：`smooth`、`flawless`、`glossy skin`、`airbrushed`、`porcelain skin`。

### 2. 拍攝裝置感
只寫 `shot on iPhone` 不夠，需要具體到裝置的實際破綻：
```
shot on iPhone 15 Pro front camera, slight autofocus softness on background elements,
natural highlight clipping near window light, subtle motion blur on hair/hands,
faint JPEG compression at high-contrast edges
```
拍攝裝置與鏡頭必須逐場景明確指定（前鏡頭自拍 vs. 後鏡頭 vs. 單眼淺景深），不要讓模型自己猜。

**⚠️ 2026-07-30 新增：前鏡頭自拍不能無腦套用「crisp sharp focus / high dynamic range」**——真實手機前鏡頭的畫質天生就比後鏡頭低（感光元件小、畫素低），如果自拍照片跟後鏡頭拍的一樣銳利乾淨，反而會讀起來很假。**自拍視角**的 prompt 應該用：
```
front camera quality, slightly softer focus than a rear camera shot, mild natural grain,
slightly lower dynamic range, gentle noise in low light, NOT ultra-crisp or overly HD
```
**他拍/後鏡頭視角**才維持原本的 `crisp sharp focus, high dynamic range` 語氣。這條跟第 7 點「自拍與他拍比例」是同一個真實感邏輯的延伸：自拍不只是「視角」要對，「畫質等級」也要對。

### 2b. 相機/濾鏡風格變化（2026-07-30 新增）
不要整批素材都是同一種「iPhone 直出」質感，可視角色風格混入以下任一種作為部分照片的濾鏡效果，增加真實生活帳號該有的風格差異：
- **CCD 數位相機質感**（早期輕便數位相機的懷舊味）：
  ```
  shot on CCD digital camera, soft slightly muted colors, gentle film-like grain,
  subtle vignette, warm nostalgic tone, lower dynamic range than modern phone HDR,
  Y2K digicam aesthetic
  ```
- **美顏/美圖類 App 濾鏡質感**（華語圈社群常見的美顏相機風格）：
  ```
  soft beautifying camera app filter, subtle skin-smoothing glow, brightened even skin tone,
  soft dreamy focus, warm glowy filter, popular Asian beauty-camera-app aesthetic
  ```
這兩種風格**不是**要取代預設的「毛孔/自然瑕疵」真實感要求（第 1 點），而是作為訓練集裡「這個人真實生活會用的濾鏡」的其中幾張變化，不要整組都套用同一種濾鏡。

### 3. 光源（2026-08-05 全面改寫：從「形容詞」改為「物理規格」）

> **⚠️ 2026-08-05 第三次修正——這是本節最重要的一次改動，取代先前的兩套配方。**
>
> **背景**：使用者指出競品帳號 @sherry_digitalp510（同為全 AI 生成的虛擬 KOL，57 萬粉）的照片「不管是夜晚、室內還是室外，或是自拍、他拍、第三者視角，打光都會因應不同場景、服裝和時間，有很好的氛圍模擬效果」，要求拆解她是怎麼做到的。實際下載她 31 張跨光線條件的素材逐張拆解後，結論如下。
>
> **她做對的事，不是把光線寫得更漂亮，而是把光線寫成「物理規格」而不是「品質形容詞」。**
>
> 我們現行 prompt 的光線描述全部是**品質形容詞**——`golden hour`、`crisp`、`well-exposed`、`soft flattering falloff`、`high dynamic range`。這些字告訴模型「要好看」，但沒有告訴模型「光從哪來、被什麼反射回來、哪裡該暗」。結果就是每張圖都是同一種均勻、討喜、沒有空間感的光——**這正是「AI 感」的主要來源**，而且是我們自己用第 2 次修正的「NOT degraded, NOT dim」規則親手鎖死的。
>
> Sherry 的每一張圖，你都可以指著畫面說出「光是從那個東西來的、又被這個表面反射到她臉上」。這才是真實感的來源。

#### 3-0. ⚠️ 2026-09-03 實測裁決：五段式公式**退出生活照與訓練圖的預設模板**

> **這一段優先於 3-A、3-B、3-C。先讀這裡再決定要不要往下用。**

2026-08-05 從競品 @sherry_digitalp510 拆解出五段式公式時，它只是**待驗證假說**——
`kols/iris-chen/generation_notes.md` 當時的批次結論自己就寫了
「🔴 打光尚未套用新公式…下一批次應以驗證該公式為首要目標」。

**2026-09-03 首次實際驗證，結果是負面的。**

`wanyin-jiang` 訓練圖批次（`review/soul_pilot/wanyin-jiang/`）：使用者對套用完整五段式的
5 張成圖評語是「可以用，但 AI 感還是有一點重」。隨後做四張盲測
（同 seed 683324、同 element、同場景服裝動作，逐字對照，見 `ailook_ab/`）：

| 盲測代號 | 版本 | 與對照組的唯一差異 | 使用者盲評 |
|---|---|---|---|
| **D** | T1 | **只把五段式光線段換成一句** `Soft ordinary morning window light, even phone exposure.` | **最好，「很有自拍感」** |
| B | C0 對照組 | 441 字，完整五段式 | 「中規中矩，堪用」 |
| C | T2 | 縮到 163 字 | 不採用 |
| A | T3 | T2 + Iris 風格尾巴 | 不採用 |

**D 勝過 B，兩者唯一的差別就是這段佈光。** 裁決如下：

| 內容類型 | 佈光寫法 |
|---|---|
| **日常自拍、家中起居、工作隨拍、散步、咖啡桌、老宅生活、普通街拍、所有 Soul 訓練圖** | **不用五段式。** 一句話：一個主光來源＋一個自然結果。例：`Soft ordinary morning window light, even phone exposure, the room behind her a little darker.` |
| 場景本來就有一個明確光源且光是敘事的一部分（窗邊晨光、檯燈夜讀、店門自然光） | **縮短版，最多一句。** 不寫具名反射面、測光策略、色溫分裂、clip／crush、遮擋圖案 |
| 電影劇照、品牌 campaign、舞台、夜店、霓虹、戲劇性逆光、產品廣告 | **才用 3-A 完整版。** 它是風格 preset，不是所有人物的基礎規則 |

3-B 的十組配方（R-1～R-10）**保留**，但改列為上表第三類的選用素材，不再是預設。

---

#### 3-D. 2026-09-03 同批實測的另外兩項結論

**① 不要為了短而短——短 prompt 會丟掉構圖控制。**

同一批盲測裡的 A 與 C 是僅有的兩張短版（163 字），**兩張都生出同一個缺陷**：
畫面變成對著鏡子拍，而鏡中又有另一隻手拿手機自拍，拍攝者身分自相矛盾。
長版沒有這個問題。差別在於縮短時被壓掉的兩句：

- `Shot on a rear phone camera from about a metre away`（明確交代拍攝者位置與距離）
- `no figure in any mirror or window reflection, no portrait or photograph of a person on any wall or screen`
  （完整版的第二人物排除句；縮成「no one in any reflection」不夠）

**規則：凡是場景裡有鏡子、玻璃、螢幕等反射面，這兩句一句都不能省。**
目前驗證有效的模板長度約 **330 字**（盲測 D 的長度），不是 160 字。

**② `film grain / warm tones / shot on 35mm / Instagram style` 這串固定尾巴：從模板刪除。**

盲測 A（有尾巴）沒有優於 C（無尾巴）。另有一次獨立的負面結果：
`train5` 的 #4 v2 加上這串之後，成圖比未加的版本**更**像精修大片。
這串字本來就可以描述高級時尚攝影，不是去 AI 感的開關。

`iris-chen` 模板值得保留的是**原則**（「不要過度打光、不要過度構圖」），不是那串字。
是否使用 `35mm`／暖色調應由該角色與該場景決定，不跨 19 位固定套用。

---

#### 3-A. 五段式光線公式（每個 prompt 的光線段落都要寫滿這五段）

| 段 | 要寫什麼 | 反例（我們現在在寫的） |
|---|---|---|
| **① KEY 主光** | 具名、畫面內可指認的光源 + 方向 + 高度 | `golden hour lighting`（沒說太陽在哪） |
| **② BOUNCE 反射填光** | **具名的物理反射面** + 它把什麼顏色的光丟回主體 | 完全沒寫（這是最大的缺口） |
| **③ 色溫分裂** | 畫面裡同時存在的兩個色溫，各自落在哪 | `warm tones`（單一色溫＝假） |
| **④ 曝光取捨** | 相機對「什麼」測光，因此「什麼」被允許過曝或壓黑 | `well-exposed, high dynamic range`（＝什麼都不犧牲＝假） |
| **⑤ 遮擋/框架** | 鏡頭與主體之間形塑光線的實體（門框、百葉簾、樹蔭邊界、遮陽棚、鏡子） | 完全沒寫 |

**②「反射填光」是這次拆解最關鍵的發現。** Sherry 的圖裡，補進陰影的那道光永遠來自一個看得見的表面：白沙、遊艇的白色玻璃纖維船身、綠松色泳池水、夕陽照亮的海面、紫色 LED 燈帶、濕掉的柏油路。這個表面決定了填光的**顏色和方向**，也就決定了畫面讀起來是不是一個真的空間。少了它，臉就是「被打亮」，不是「被環境照亮」。

**④「曝光取捨」是第二關鍵。** 她的照片經常**不是**「曝光正確」的：逆光夕陽那張，她整個人比天空暗；車內那張，車外停車場整片過曝到死白；遊艇那張，背景海面過曝而她在陰影裡。真實相機一次只能對一個亮度測光，另一邊就得犧牲。**我們現行規則裡的 `NOT degraded, NOT dim, high dynamic range` 等於強迫模型兩邊都不犧牲——這在物理上不存在，所以看起來假。**

> **這條不是要推翻 2026-07-25 的修正。** 那次修正說的「真實感 ≠ 畫質差」仍然完全成立：不要寫 `grainy`、`muddy`、`degraded`、`low quality`。畫質要好、要清晰、要有細節。**但「畫質好」不等於「每一處都曝光均勻」**——這是兩件事，先前把它們混為一談了。允許畫面有壓黑的暗部和過曝的窗外，同時保持主體清晰銳利，這才是現代手機攝影的真實樣子。

#### 3-B. 十組可直接套用的光線配方

以下每一組都可以整段貼進 prompt 的 `[LIGHTING]` 位置，依場景挑選：

**R-1 夕陽逆光（海邊 / 戶外開闊處）**
```
backlit by the low setting sun directly behind her on the horizon, warm orange rim light
tracing her hair edge and shoulder line, her face filled only by soft bounce off the
bright water surface below, sky exposed correctly so she sits noticeably darker than
the background, deep warm orange near the horizon fading to cool violet overhead
```

**R-2 藍調時刻（日落後 10–20 分鐘）**
```
post-sunset blue hour, cool blue ambient sky light as the overall base, a residual warm
peach glow low on one side of the sky throwing warm light onto that side of her face
while the shadow side picks up cool blue skylight, streetlights just switching on,
foreground road falling into darkness with her as the brightest element in frame
```

**R-3 正午強光 + 白沙／淺水反射（高反差海灘）**
```
hard high overhead midday sun casting a short sharp shadow at her feet, strong white
bounce coming back up off the pale sand and shallow water filling the underside of her
chin, jaw and arms from below, highlights on the water surface allowed to clip to pure
white, saturated deep blue sky
```

**R-4 遮蔽物下（遊艇艙頂 / 騎樓 / 樹蔭）— 主體在陰影，背景過曝**
```
she sits in the shade under the hard-top canopy while the sea and sky behind are in
full sun and blow out slightly, the large white fiberglass surfaces around her acting
as a giant bounce card wrapping soft shadowless fill onto her skin, exposure metered
for her face so the background reads one to two stops hot
```

**R-5 暗框亮主體（車內 / 門洞 / 室內看向窗外）**
```
shot from outside into the dark cabin interior, the only light on her spilling in
through the open door and windows, the interior surfaces around her crushing to near
black, the parking lot visible through the far windows blown out to white, extreme
dynamic range between the dark frame and the bright opening
```

**R-6 陰天平光 / 俯拍**
```
flat overcast open-shade daylight with no directional sun and no visible shadow edge,
overall low contrast, her skin only marginally brighter than the mid-grey ground,
even soft light from the whole sky acting as one huge diffuser
```

**R-7 室內窗光 + 百葉簾**
```
soft window light entering from one side through venetian blinds, faint hard-edged
stripes of light falling across the wall and partly across her, warm interior tungsten
lamp deeper in the room adding a second warmer source behind her, gentle falloff into
the unlit side of the room
```

**R-8 夜間室內實用光源（餐廳 / lounge / 飯店走廊）**
```
lit only by the practical fixtures visible in frame — a warm pendant lamp and a
receding row of ceiling downlights — warm tungsten key from front-right, the depth of
the room falling away into deep shadow, high contrast with her face readable but the
background largely dark, no artificial fill
```

**R-9 RGB / LED 情境光 + 中性面光（直播 / ASMR / 電競房）**
```
magenta and violet LED cove lighting washing the walls and ceiling behind her as the
scene's colour, a separate neutral-warm frontal key from the camera side lighting her
face cleanly, two clearly different colour temperatures coexisting in one frame —
coloured background, neutral face
```

**R-10 夜間街頭混合光（霓虹 + 鈉燈 + 濕地面）**
```
cool blue city ambient as the base, warm sodium streetlight raking across her from one
side, coloured neon spill from a shopfront hitting the other side, wet asphalt
reflecting the signage back up as a secondary coloured bounce from below, headlights
streaking past out of focus
```

#### 3-C. 光線規則（2026-08-28 由「三條硬性規則」改為條件式）

> ### ⚠️ 這一段原本寫成「三條硬性規則」，那是錯的
>
> 第 1、2 條原文是「必須寫出反射面」「必須寫出哪裡被犧牲」。
> 2026-08-28 依此寫成 lint 硬性檢查，**21 件 spec 全部不合格**。覆核裁決：
>
> > 「把競品的風格觀察誤當成普遍物理規則，**這個紅燈本身會誘導過度修正。**」
>
> 白牆室內單一柔光源的場景**本來就沒有第二色溫**，也沒有需要犧牲的一邊；
> 硬塞只會製造假陰影。這三件事是**條件式**的，適用範圍不同：
> 「具名反射面」幾乎到處適用（21 件裡 20 件寫得出來），色溫分裂只有一半場景成立。
>
> **現行做法**：規格表寫一列「光學設定」三態宣告，由 `tools/prompt_lint.py` 檢查宣告存在且合法，
> **不檢查 prompt 裡有沒有那三句話**：
>
> | 欄位 | 可選值 |
> |---|---|
> | 反射面 | 具名 / 不適用 |
> | 曝光 | 取捨 / 低反差 |
> | 色溫 | 分裂 / 不適用 |

1. **寫得出反射面就要寫。** 「光被什麼表面反射回她臉上」——白沙、白色船身、濕柏油、大理石檯面。
   **寫不出來的場景**（單一柔光源、無明顯反射體）宣告「不適用」，不要硬編一個。
2. **有高低差的場景要指定哪一邊被犧牲**（`allowed to clip`、`falling into deep shadow`）。
   **低反差場景**（陰天、室內柔光）宣告「低反差」——強寫犧牲會製造不存在的陰影。
3. **禁止在光線段落使用的字**：`high dynamic range`（它的意思正好是「不犧牲任何一邊」）、`evenly lit`、`well-exposed`、`perfect lighting`、`studio lighting`（除非該張真的就是棚拍設定）。
   - **仍然要保留**畫質相關的字：`crisp sharp focus on subject`、`fine detail`、`natural colour grading`。這些管的是解析度和銳利度，不是曝光均勻度。
   - **仍然禁止**：`grainy`、`muddy`、`degraded`、`low quality`、`dim and blurry`。
   - **⚠️ 2026-08-28 新增禁用（同義改寫也算）**：`background exposed the same brightness as her skin`。
     這句是為了解室內逆光而生的（餐廳批次一 D-04，室內 3/3 有效），
     字面上避開了 `evenly lit`／`well-exposed`，**但意思一模一樣**——強迫兩邊都不犧牲。
     實測數字（YG-04 A/B，各 2 張，`tools/light_meter.py`）：

     | | 背景比臉暗 | 臉部受光／陰影反差 |
     |---|---|---|
     | 用這句 | 0.03–0.11 級（＝等亮） | **0.0 級——臉是一塊平板** |
     | 改成場景化測光句 | 0.37–0.43 級 | 0.30–0.42 級 |

     **替代寫法**：`her face is evenly exposed, while the rear wall remains readable and slightly darker.
     Small marble highlights clip softly before her skin does.`（把「臉不能欠曝」與「背景要更暗」拆成兩件事）
     ⚠️ n=2、單一室內場景，**高反差場景（有窗／有天空）尚未驗證**，不要當成全域結論。
     完整紀錄見 `CALIBRATION_TEST.md` §24 與 `review/restaurant-b1/LEDGER.md` #15。

### 3-E. 全身照的朝向要寫鏡頭位置，不要寫身體姿勢（2026-09-03，連續三位都踩到）

**事件**：`wanyin`、`kanon`、`cheryl` 三位的訓練集，**每一位的全身照都站得像證件照**，
而同一位的胸上／腰上照都自然。使用者指出這兩張「完全不能拿來當日常素材發」。

**原因是 prompt，不是模型。** 比對後確認：這句只出現在全身那幾張，其餘一句都沒有——

> She is facing the camera: her face, the front of her body and both shoulders are toward the lens
> and **her feet point toward it**. Her back is not to the camera and her head is not turned away.

這句原本是為了修「模型把人轉成背面」而加的，它有效；**但它同時是一張證件照的指令**。
再加上全身那幾張配的動作也都是靜態的（`stands still and looks at the lens`），等於鎖死兩次。

**規則：朝向只寫鏡頭在哪裡，不寫身體要擺成什麼樣。**

| 不要寫 | 改寫成 |
|---|---|
| `her face, the front of her body and both shoulders are toward the lens` | `The camera is in front of her, not behind her.` |
| `her feet point toward it` | （刪除，不要寫腳的方向） |
| `standing square to the camera` | （刪除） |
| `She stands still and looks at the lens` | 一個**具體的、有重量的動作**（見下） |

**全身照必須配一個有以下至少兩項的動作**：重心偏在一隻腳、手上拿著或正在操作某個東西、
身體有一段正在進行的動作（蹲下、跨步、轉身中、把頭髮從領口撥出來）、視線不一定在鏡頭上。

可用的寫法範例：

```
The camera is in front of her, not behind her.
She is crouched down zipping the suitcase shut, one knee on the floor, and has just looked up.
```
```
The camera is in front of her, not behind her.
She is stepping into her shoes with one hand braced on the wardrobe door, weight on one leg,
still looking down at what she is doing.
```

**保留**「背對鏡頭」的否定句（`Her back is not to the camera`）——那一句是有效的且不造成僵硬。
被刪掉的是描述身體正面與雙腳方向的那部分。

---

### 3-F. 不要點名「不可以出現的物件」——點了它就會出現（2026-09-04）

**事件**：`miu-shiraishi` 訓練圖 #3 重跑時，我在 prompt 裡寫了
`no phone, tablet, television or lit screen of any kind anywhere in the picture`，
結果畫面右緣就多出一支手機（native crop 可見三顆鏡頭模組）。同一段落其他句子都正常執行。

**這是既有兩條發現的同族現象**，機制相同：**名詞被寫進 prompt 就會被畫出來，否定詞不生效。**

| 已知案例 | 寫了什麼 | 生出了什麼 |
|---|---|---|
| Iris Chen | 場景裡寫 `mirror` | 鏡子自拍、手機入鏡 |
| angel-chiu #4 | 結尾留 `Shot on a rear phone camera` | 整張圖被手機邊框框住 |
| miu-shiraishi #3r | `no phone, tablet, television or lit screen` | 畫面裡多一支手機 |

**規則**：要讓某個物件不出現，**不要點它的名**。改用肯定句把那個位置填滿：

| 不要寫 | 改寫成 |
|---|---|
| `no phone or screen in the hallway` | `a plain painted door filling the wall behind her` |
| `no television on the wall` | `a bare plastered wall behind her` |
| `no mirror in the bathroom` | （直接不提牆面，或寫 `a tiled wall behind her`） |

**唯一的例外是單人排除條款**（`The only person anywhere in this photograph is her — no one else…` 那一整段）。
它處理的是「人」，實測長期有效（本批 10 張裡擋掉了攤商、店員、客人、路人），**不要動它**。
換句話說：否定「人」有效，否定「物件」反而招來物件。

**這條同時解釋了為什麼「浴室不要有鏡子」一直難寫。** 舊寫法
`There is no mirror anywhere in this photograph` 至今沒有生出鏡子，
但它是撞運氣，不是可靠機制——同一句型換成手機就失效了。往後浴室場景改成
不提鏡子、直接把她放在「關上的門前」或「貼磚牆前」。

#### 3-F 補正（2026-09-04 同日，用第二輪資料修正上面的說法）

上面第一版把規則寫得太寬了。**全身照結尾那段裝置排除句，實測 18/18 一直有效**，
而它明明也點了 phone / screen / device 的名：

```
This is a plain photograph of the scene, edge to edge. There is no phone, no screen
and no device anywhere in the picture, and the image is not framed or bordered by
the edge of any device.
```

差別在於**它由一句肯定的畫面定義開頭**（`This is a plain photograph of the scene, edge to edge.`），
否定句是掛在那句後面的補充；而失敗的 miu #3r 是**把裸的否定句直接接在場景描述後面**，
前面沒有任何肯定的畫面定義。

**修正後的規則**：

1. **不要把裸的否定句接在場景句後面**（`Behind her: … . There is no phone, tablet, television or lit screen.`）——會招來那個物件。
2. **要排除某物件，先用肯定句把那個位置填滿**：`a plain painted door filling the wall behind her`、`a bare plastered wall behind her`。
3. **既有的兩段固定句不要動**：全身照的裝置排除句（由肯定句起頭，18/18 有效）、
   單人排除條款（否定「人」，實測長期有效）。它們是驗證過的例外，不受第 1 點約束。

#### 一個尚未證明的附帶觀察（2026-09-04）

`sydney-leong` 的 #3 #4 #5 是專案至今**第一次連續三張服裝完全照規格、零覆蓋度偏差**，
而這三張的共同點是段落裡沒有任何自創的否定句。對照組 `angeline-kwee` #3r：
同樣用肯定句寫足浴袍規格，但同一段塞了兩句否定，浴袍就被拉下單肩。

**假設：同一段落裡的否定句會排擠掉服裝指令。**
只有一輪對照，**樣本不足以推翻「覆蓋度無法用 prompt 控制」這個既有結論**。
下一輪繼續全面套用 §3-F，再看是否重現；重現兩輪以上才改寫覆蓋度那一條。

---

### QA-1. 小面積缺陷不得用插值放大來判讀（2026-09-03，踩過一次）

**事件**：`kanon-komori` 訓練圖 #5 是全身夜景，臉約 140px、虹膜約 13px。
我把虹膜區域用 LANCZOS 放大 4 倍後目視，判定「兩眼虹膜顏色不同（一眼黃綠）」，
據此退件並重生一張（1 credit），還把兩條錯誤結論寫進了紀錄。

**實際上沒有色差。** 事後在原生解析度量測 HSV：四組虹膜全部落在深紅褐
（色相 348–360°、飽和度 0.20–0.31），兩眼一致。那個綠是 **LANCZOS 在十幾個像素上的插值假色**。

**規則**：判讀虹膜、瞳孔、指節、牙齒、耳廓這類**只有十幾到幾十像素**的區域時：

1. **不得**單憑雙三次／LANCZOS 放大的目視結果退件——這類插值會在小區域造出原圖沒有的顏色與邊緣。
2. 必須至少做以下一項再下判斷：
   - 用 **NEAREST**（零插值）放大，看到的才是真實像素；
   - 或直接在原生解析度**量測數值**（例如以 mediapipe iris landmark 定位後比較兩眼 HSV）。
3. 判讀結果若要寫成「規則的例外」或「新的失敗機制」，**必須先完成第 2 點**。
   基於誤判寫進規範的結論，比原本的缺陷傷害更大。

---

### QA-2. `status=completed` 不等於出圖成功（2026-09-04，踩過一次）

**事件**：`peggy-lee` 訓練集 #2（job `e8eddf2c`，seedream_v4_5）在 `jobs_wait` 回報
`status: completed`、有正常的 result_url、檔案 11MB、尺寸 1728×2304——但**打開來是純雜訊**，
擴散過程完全沒有收斂，畫面上沒有任何可辨識的物件。

**排除過的可能**：
- 不是縮圖誤判——native-resolution crop 一樣是雜訊（§QA-1 的程序有跑）。
- 不是下載損毀——重新下載，SHA-256 與第一次完全相同（`254cd229…`），伺服器上的圖就是雜訊。
- 不是 prompt 問題——同一批同一模型的另外 9 張全部正常，重跑時 prompt 一字未改就成功。

**規則**：

1. **每一張圖在歸檔前都必須實際看過。** 不可因為 `jobs_wait` 回報 `completed`
   就直接把 result_url 存成訓練圖或素材。
2. 遇到雜訊圖時**不要改 prompt**——它不是 prompt 造成的，改了反而會失去對照。
   原樣重送即可（seed 會不同）。
3. 這種失敗**會計費**（1 credit）。回報成本時要把它算進去，不要假設「失敗不收費」。

---

### 4. 背景場景具體度
避免「乾淨、對稱、沒有雜物」的背景，主動寫入生活感細節（皺褶床單、地上的充電線、喝到一半的水瓶、隨手放的手機），而不是只寫地點名稱。

### 5. 聲音與環境音（影片專用）
乾淨的 BGM-only 音軌會讀起來像「後製過」。需要在環境音層加入：
```
room tone / air conditioning hum, fabric rustle, soft footsteps, faint distant background noise
```
疊在 BGM 底下（`generate_audio` 設定與音樂上傳流程見 `DAILY_VIDEO_SOP.md` / `DANCE_VIDEO_SOP.md`）。

### 6. 膚色基調（臺灣籍角色專用，2026-07-25 新增）
> **背景**：Coco Wu、Rainie Hsu、Sophia Tseng、Mia Huang、Zoe Lai 的第一輪探索批次生成後，使用者明確反饋膚色整體偏「健康小麥/古銅曬黑」，並指出臺灣觀眾對「漂亮性感」的審美偏好是**白幼瘦**——白皙皮膚、精緻年輕的五官、纖細身形，「健康古銅膚色」通常不是主流受眾偏好的類型。

臺灣籍角色（不論人設是居家、辦公室、健身、還是海邊/衝浪這類戶外活躍角色）的膚色基調都要維持**白皙透亮**，最多只能有極淡的自然日曬痕跡，**不可**整體呈現古銅色、小麥色、深咖啡色調。每個臺灣籍角色的核心 prompt 都必須明確寫入：
```
fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored)
```
同時保留第 1 點的毛孔/自然質感關鍵字——**白皙不等於無瑕疵磨皮**，兩者要同時成立。此規則對已核准的既有生成圖片（例如 Vicky Lin 已核准的 v4_anchored 訓練集）不追溯套用，只適用於尚未核准／尚未生成的新批次。

### 7. 自拍與他拍比例（2026-07-30 新增）
> **背景**：使用者反饋 Rainie Hsu 第二輪候選圖「風格都很像棚拍，很不自然、蠻刻意的」，並指出所有角色的素材不能只侷限在「像第三者幫她拍」的一種視角——女生本來就常常自拍，早期驗證成功的 Iris Chen 範本（`kols/iris-chen/generation_notes.md`）本來就包含 `close-up front-facing selfie shot, slightly overhead angle looking down at camera` 這類自拍視角批次，不是每張都是「編輯/攝影棚」語氣的第三人稱攝影。

每個角色的**完整素材組合（不只是單一場景/單一批次）**都必須混合以下至少兩種視角，不能全數採用同一種：
- **自拍視角**：`close-up front-facing selfie shot`、鏡子前自拍（`mirror selfie, phone visible in reflection`）、手臂伸展自拍角度——描述的是「照片本身呈現的視角」，不是「她正在自拍的動作」（見 Iris Chen 案例「自拍視角重要規則」：❌ `taking a selfie holding phone up` 會讓模型生成第三人視角+手機入鏡；✅ 直接寫出照片視角本身）
- **他拍/生活抓拍視角**：朋友幫忙拍、隨手抓拍、路人視角等，重點是自然不做作
- 避免整批次全部使用「editorial photography」「high-production-value」「dramatic and moody」這類會把畫面推向棚拍/雜誌大片感的語氣——這類語氣本身沒有錯（有些場景就是需要，例如換裝定裝照），但**不能是唯一的視角**，否則會讀起來刻意、失去「真實生活分享」的親近感

### 8. Discovery／參考錨定圖的穿搭要「日常」，不是角色的極端招牌造型（2026-07-30 新增）
> **背景**：使用者看過 Rainie Hsu 的候選圖後指出，貼身洋裝＋大量金飾這種「出門夜店」等級的造型，拿來當某一篇「她去參加 party」的限定貼文素材沒問題，但**不適合當作她的身分錨定／參考圖**——參考圖代表的是「這個人平常長怎樣」，不是「她最誇張的一次穿搭」。角色本身的個性/魅力設定（例如豔麗、性感）不需要靠每張參考圖都穿最浮誇的服裝來體現。

Discovery 批次與任何用於 Reference Element 錨定身分的參考圖，服裝預設應該是**該角色的日常/居家/普通外出款**（見該角色 `character.md` 的「居家」「家人時光」「耍廢日」等非招牌 pillar 段落找對應穿搭），而不是她的招牌極端造型（夜店洋裝、比賽級健身戰袍、大量誇張配飾等）。招牌造型留給之後**明確對應到那個場景的正式批次**（例如「今晚出門」「夜店」這種有明確情境的貼文素材），不要預設套用在純粹用來確認臉部/身材一致性的參考圖上。

### 9. 人物入鏡規則：區分「同框互動者」與「背景路人」（2026-08-05 修訂，原 2026-07-30 版本已被實測推翻一半）

> **原規則（2026-07-30）**：「預設只有本人入鏡，不要無故加入其他人。」
>
> **2026-08-05 實測結果：這條規則對「同框互動者」仍然成立，但對「背景路人」是錯的，而且是我們畫面看起來假的主因之一。**
>
> 競品 @sherry_digitalp510 的素材中，只要場景是公共空間（街道、夜市、海灘、商場、路口），畫面裡幾乎**一定**有背景路人。原因很簡單：**一個真實的公共場所不可能空無一人。** 空景的台北巷弄、空景的夜市、空無一人的海灘，本身就是最強的「這是合成的」訊號。
>
> 2026-08-05 用 7 位台灣籍角色各 2 張（共 14 張）實測加入背景路人，結果：14/14 全部成功產生自然的背景人物，**且沒有任何一個配角撞臉主角**（Coco Wu 案例的問題沒有復發）。成本為零——同樣的生成次數。

**修訂後的規則分兩類：**

**(a) 同框互動者（朋友、家人、室友等有戲份的人）—— 維持原規則，預設不要有。**
除非該張 prompt 明確需要，否則不要出現。真的需要時必須明確指定該人物的外型特徵，與主角做出區隔，不能讓模型自行決定（見 Coco Wu 案例：室友因未指定區隔特徵，長得跟 Coco 本人很像）。

**(b) 背景路人（公共空間裡的無關陌生人）—— 規則反轉：公共場景應該要有。**
只要場景是街道、夜市、商場、海灘、車站、路口等公共空間，就**應該**寫入背景路人，並且必須用下列這組已驗證有效的措辭，同時滿足四個條件（背向／不看鏡頭／失焦／外型區隔）：

```
BACKGROUND PEOPLE: a few anonymous strangers in the mid-ground going about their own
business, backs turned or heads angled away, never looking at the camera, softly out of
focus with slight motion blur, clearly different from her in build, age and clothing
```

四個條件缺一不可：
- `backs turned or heads angled away` + `never looking at the camera` → 避免配角搶焦點、也避免生成正臉時撞臉
- `softly out of focus with slight motion blur` → 把他們留在背景層，同時製造真實的景深與動態
- `clearly different from her in build, age and clothing` → 這一句是防撞臉的關鍵，不可省略
- `anonymous` / `going about their own business` → 避免模型把他們處理成「跟她一起的人」

**私密場景（臥室、浴室、自家客廳、飯店房內）維持只有本人**——那些場所本來就不該有陌生人。

**(b-例外) 建模訓練集：不寫背景路人（2026-08-28 新增，這是唯一的例外）**

(b) 只適用於**日常素材**。**Soul 訓練集是唯一的例外**——訓練圖的用途是讓模型學一個身分，
畫面裡任何第二個人都可能被學進去，或讓模型分不清哪張臉才是要學的那個。
所以訓練集的公共場景**維持只有她一個人**，並且要用正面封閉集合寫死：

```
Everything in this picture is accounted for: the only person in it is her, and every visible
hand connects to one of her own arms.
```

**代價要講清楚**：訓練集因此會看起來比日常素材假——空景的超商、空景的月台、空景的藥妝店。
**這是刻意的取捨，不是忘了寫。** 但 Soul 訓練完成之後，**日常素材必須立刻切回 (b)**，
否則那個「空無一人的台北」會變成這個角色所有素材的共同特徵。

> **2026-08-28 事故**：Nico 的 Phase C 訓練集 20 張中，14 張是公共場所，全部寫成「只有她一個人」，
> 0 張有背景路人。當時的判斷本身是對的（訓練集就該如此），但我**沒有意識到這條規則存在**，
> 也沒有把它記成一個「訓練集專屬的例外、之後要切回來」的決定——
> 是使用者看完出圖說「還是少了一點真人感」並問「怎麼都沒參考小雪莉」才發現的。
> 這一節就是為了讓下一次不必再靠人眼發現。

---

**(c) 敘事裝置型背景人物（2026-08-05 第三輪分析新增，與 (b) 規則相反）**

> **背景**：競品觀看數第 2 高的 Reels（156 萬觀看）整支影片的賣點，就是**手扶梯上前方的中年男子一再回頭看她**——那個男人的反應才是內容主體。這直接牴觸 (b) 的「絕不看鏡頭／背向」。

當背景人物的**反應本身就是這則內容的梗**時，規則反轉：**刻意讓他看她、回頭、有反應**。但必須在 prompt 中明確指定該人物的外型、年齡、動作方向與反應強度，不可讓模型自由發揮（否則會回到 Coco Wu 撞臉那類問題）。

三者的判準很簡單：
- 只是要讓公共場所不空曠 → 用 (b)，背向失焦
- 這個人的反應就是笑點／看點 → 用 (c)，明確指定他的反應
- 這個人跟她有互動關係（朋友、家人）→ 用 (a)，明確指定且做外型區隔

### 10. 生成後必須實際檢查 AI 生成瑕疵，不能只看「大致像不像」（2026-07-30 新增）
> **背景**：使用者反饋，有幾張已經生成的訓練圖仔細看會發現手部瑕疵（例如多長出一隻手／手指數量不對）或鏡頭/拍攝角度不自然，但先前的「誠實視覺評估」只檢查了身分一致性、膚色、自拍/他拍風格等大方向，沒有逐張檢查這類常見的 AI 生成缺陷。

之後每一批次生成完成後，用 Read 工具實際檢視每一張圖片時，除了身分一致性/膚色/風格之外，**必須額外檢查**：
- 手部是否正常（手指數量、手部姿勢是否符合人體結構，AI 生成最容易出錯的部位）
- 肢體/關節是否有不自然的扭曲或多餘肢體
- **畫面裡有沒有多出一個「不屬於任何人」的身體部位**——2026-08-28 Nico 訓練集 `c08`（浴室鏡前自拍）在洗手台下方生出了一雙赤腳與黑褲腿，不連接畫面中任何人。**這類錯誤特別容易出現在「畫面深處、家具下方、鏡子邊緣」這些注意力不會停留的區域**，看整體構圖時很容易漏掉。逐張檢查時要**刻意掃過畫面的四個角落與家具底下**，不要只看主體
- 鏡頭角度/透視是否合理（不能出現物理上不可能的拍攝角度或比例扭曲）
- 背景物件是否有明顯的生成錯亂（例如文字亂碼、物體邊緣融合錯誤）

有瑕疵的圖片要在文件中明確標記出來（哪一張、什麼問題），不要因為整體「看起來還可以」就略過細節檢查；如果瑕疵明顯，該張應該重新生成或替換，不要直接送入訓練集。

### 11. 地點要寫「在地質感」，不要點名地標（2026-08-05 新增，實測結論）

> **背景**：2026-08-05 的 14 張實測中，prompt 明確點名了「台北永康街」「高雄愛河」「台中逢甲夜市」「台北 101」「新竹巨城」「墾丁南灣」「恆春老街」等真實地標。

實測結果**兩極**：

- ✅ **「無地標的在地質感」全部成功**：巷弄的鏽蝕鐵窗花、糾纏的電線、手寫中文招牌、緊貼牆邊停的機車、冷氣滴水痕、夜市的層疊 LED 價目燈箱、老街的鐵捲門與盆栽、手寫菜單黑板——這些描述模型都能精準生成，台灣感非常強。
- ❌ **點名地標全部失敗**：「高雄愛河」生出墨爾本天際線，「台北 101」生出通用摩天樓群。模型認得「台灣街景的紋理」，**不認得特定地標的外觀**。

**所以：把地點寫成「環境元素的清單」，不要寫成「地名」。** 寫 `a narrow lane of weathered mid-century Taipei apartments with rusted iron window grilles, tangled overhead power lines and hand-painted Traditional Chinese shop banners`，不要寫 `Yongkang Street, Taipei`。效果一樣好，而且不會生出錯的地標穿幫。

**唯一例外**：畫面裡真的需要出現可辨識地標時（例如刻意要拍 101），必須生成後逐張確認地標外觀正確，錯了就重生或改場景——不要放行一個長得不像 101 的「101」。

### 12. 用「同穿搭一日敘事」串聯多張素材（2026-08-05 新增，實測有效）

> **背景**：拆解競品 Sherry 的貼文結構發現，她 90% 的貼文是 4–5 張的 Carousel，而同一則 Carousel 內的多張圖是**同一套穿搭、同一天、不同時刻／不同角度**，而不是各自獨立的漂亮單圖。

2026-08-05 實測 7 組配對，7/7 成功：服裝與配件在兩張之間完整延續，而且**配件的狀態會自然演變**（風衣從腰間移到肩上、墨鏡從桌上移到手上、飲料換成另一杯、鞋子脫下放在旁邊）——讀起來確實像同一天拍的。

寫法：第二張以後的 prompt 在 `[OUTFIT]` 段落開頭直接寫 `the exact same outfit as earlier that day —`，再完整重複一次服裝清單，然後**刻意描述一個「時間過去了」的小變化**（頭髮被風吹亂、多了一杯飲料、外套穿法改變、腳上多了沙）。

這是把單張素材變成「一則貼文」的關鍵，成本為零。

### 13. 造型與地點是「獨立變數」，不是內容主題的附屬品（2026-08-05 新增，最高優先級之一）

> **⚠️ 這條對應使用者最強烈的一次反饋**：「我一直很排斥你將特定人格設定得過於單一，例如做瑜伽的就只穿韻律衣韻律褲、喜歡衝浪的就只穿比基尼、遊戲直播主就只戴耳機坐在電腦前，環境完全不變。這很不 OK。如果要打造得像真人，怎麼可能所有素材都在相同的環境、穿著與髮型下進行？」

**問題根因**：我們的 `content_style.md` 用「活動」定義內容支柱（晨間衝浪／直播開台／健身重訓），導致服裝與場景變成活動的附屬品被自動推導出來——支柱寫「直播開台」，服裝就只能是帽T、場景就只能是電腦桌前。**每個角色被自己的人設關進了一個房間。**

**修正**：**造型（穿搭／髮型／配件）與地點，是獨立於內容支柱的變數，各自獨立輪替。** 規劃任何一批素材時，決定完「這則屬於哪個支柱」之後，必須再獨立轉四個轉盤：

1. **穿搭風格**（每個角色至少 8 種風格區間，連續兩則不可同區間，招牌風格 ≤30%）
2. **髮型**（每個角色至少 5 種，每則明確指定，不可讓模型自己決定）
3. **地點層級**（每 10 則配額：A 級嚮往感 2–3、B 級有質感日常 4–5、**C 級完全不美的日常至少 2，硬性下限不可為 0**）
4. **微物件**（手機殼／包／鞋／髮飾／指甲／手上拿的東西，每則至少換 2 樣且具體點名）

**完整系統、各角色的 8 種風格光譜、C 級地點清單、prompt 寫法範例，見獨立文件 `WARDROBE_SYSTEM.md`。**

**最關鍵的單一發現——C 級地點**：競品 Sherry 敢在 57 萬粉帳號上發 Costco 推推車、麥當勞得來速、蝦皮店到店取貨機、路口凸面反光鏡自拍。**正是這些一點都不美的地方，讓觀眾相信「她是個剛好很有錢的真人」而不是型錄。** 我們現行素材幾乎全部落在 B 級、偶爾 A 級，**C 級掛零**——這是我們看起來假的重要原因之一。

**服裝段落的 prompt 必須寫滿五層**（上身／下身／鞋／包或外套／首飾髮飾），每層具體到單品＋材質＋顏色；`[HAIR]` 要獨立成欄位。只寫 `wearing a casual top and shorts` 這種等級一律退回重寫。

### 14. Carousel 是「1 個 setup × 5–6 種表情」，不是 5 個不同場景（2026-08-05 新增，最高操作優先級）

> **這一條會直接改變產製流程與成本結構。** 拆解競品按讚最高的幾則 carousel 逐張看，發現 6 張全部是**同一個機位、同一套衣服、同一個場景、同一組光線**，只有**表情與手勢**在變（吐舌／眨眼／嘟嘴／手托腮／張嘴笑／手比在臉旁）。

**規則：**
> **一則貼文之內 → 高度一致**（同一套衣服、同一個地點、同一組光線）
> **貼文與貼文之間 → 全部換掉**（衣服、髮型、地點層級、配件——見第 13 點與 `WARDROBE_SYSTEM.md`）

**為什麼重要**：她每 1.2 天發一則、每則 5.1 張，等於每天要產出約 4.3 張新圖。若每張都是不同場景，成本高且身分一致性風險大；**「同 setup 只變表情」邊際成本極低、身分一致性最穩**——這正好是 AI 生成最可靠的事。我們現在每張獨立生成不同場景的做法，既貴、身分又容易飄、而且不像她。

**實作**：先定下**唯一一組** `[OUTFIT] + [SCENE] + [LIGHTING]`，然後只變動 `[EXPRESSION / GESTURE / MICRO-POSE]` 生 5–6 張；中間可穿插 1–2 張拉遠的中景換口氣，但衣服／地點／光線不變。

完整分析見 `REELS_AND_STRUCTURE_SYSTEM.md`。

### 15. 短影音：剪接越少越好，情境 > 美貌（2026-08-05 新增，數據驗證）

30 支 Reels 場景切點偵測 × 觀看數交叉比對結果：

| | 平均切點 | 平均秒數 | 單鏡頭長度 | 平均觀看 |
|---|---|---|---|---|
| 前 8 名 | **3.0 刀** | 13.6 秒 | **5.79 秒** | 781,917 |
| 後 8 名 | **5.9 刀** | 13.4 秒 | **3.84 秒** | 47,538 |

長度幾乎相同，**差別在切點密度**。切 23 刀的快剪蒙太奇只拿到 5.7 萬觀看；完全不切的單鏡頭 14.7 秒拿到 74.6 萬。**畫面運動量不是差異因子**（14.0% vs 12.7%）。

**規則**：預設 **0–3 刀、單一鏡頭 ≥4 秒**，禁止快剪蒙太奇。

**另外三條**（詳見 `REELS_AND_STRUCTURE_SYSTEM.md`）：
- 每支要有**三秒內看得懂的情境**，且必須由**畫面**演出來——用字卡講故事的那支只拿到 5.3 萬
- **標題負責點破笑點，畫面負責承載**（例：「Uber司機表示不知道怎麼辦」＋她在後座睡著的畫面 = 167 萬觀看）
- 不必蹭熱門音檔（她 30 支有 26 支用自己的 original audio，唯一用熱門曲的排倒數第二）；不必追畫質（26 支是 720×1280）

### 16. 避免奇怪的鏡頭角度，尤其是「由下往上」的低角度仰拍（2026-08-12 新增，使用者實測反饋）

> **背景**：Iris Chen 的日常性感短片 v2（`kling3_0` 多鏡頭切換版）其中一個鏡頭用了「低角度仰拍咬草莓/眨眼」的構圖。使用者看過整支影片後回饋：「這個還行，但以後要避開一些奇怪的鏡頭角度，由下往上拍這種怪角度」——即使身分/畫質/多鏡頭切換感都合格，這類角度本身仍會被判定「怪」，不能用「其他方面沒問題」來抵銷。

**規則**：無論是靜態圖片還是 `generate_video` 的多鏡頭 prompt，預設**避免「由下往上」的低角度仰拍**（camera looking up at the subject from below，常見措辭如 `low angle`、`shot from below`、`looking up at her`）。這類角度即使技術上執行成功（無拼貼、無變形），構圖本身也會顯得不自然、不討喜。

**預設可用的角度**（見上方第 9 條之前各場景「鏡頭角度」寫法，以及本節前述规格）：
- 平視（eye-level，最安全、最常用）
- 微俯角／從上方略往下拍（slightly overhead angle，尤其自拍類鏡頭常見且效果好）
- 側面、3/4 側身角度
- 從鏡子反射拍攝形成雙重視角

**設計多鏡頭切換 prompt 時**（例如 `kling3_0` 這類支援鏡頭切換的模型），每個鏡頭的角度描述都要逐一檢查是否落在上述安全範圍內，不要為了「製造角度變化的豐富感」而加入低角度仰拍這種本身就不自然的選項——切鏡的多樣性應該來自景別（近景/中景/廣角）與姿勢/表情的變化，不是靠奇怪的相機角度。

### 生成前檢查清單
每個 prompt 送出生成前，逐項確認：
- [ ] **（2026-07-25 新增，第一優先）是否已經先讀過既有已驗證成功的角色範本，而不是直接採用生成工具本身的預設建議？** 預設參考 `kols/iris-chen/generation_notes.md`（模型 `seedream_v4_5`，已證實同 prompt 重複生成身分一致性高）。訓練圖／Discovery 批次的預設模型是 `seedream_v4_5`，不是 `soul_2`——`soul_2` 只在角色已經有 `soul_id` 時才用於後續生成。2026-07-25 事故：多個角色的 Discovery 批次因為跳過這一步、直接沿用工具建議的 `soul_2` 無錨點生成，導致同批次 4 張圖臉孔不一致。
- [ ] 裝置/鏡頭是否具體指定
- [ ] 皮膚質感關鍵字是否存在
- [ ] **（2026-08-05 改寫，最高優先）光線是否寫成「物理規格」而不是「品質形容詞」**——見上方第 3 點。逐項確認：① 具名主光+方向 ② 反射面（**寫不出來的場景宣告「不適用」，不要硬編**）③ 色溫（**單一光源宣告「不適用」**）④ 曝光取捨（**低反差場景宣告「低反差」**）⑤ 遮擋/框架。②③④ 是條件式的，見上方 3-C 的警語。可直接套用 3-B 的十組配方
- [ ] **光線段落是否誤用了 `high dynamic range` / `well-exposed` / `evenly lit` / `background exposed the same brightness as her skin`**——這些寫法現已禁用（它們的意思正好是「不犧牲任何一邊」）；`crisp sharp focus` / `fine detail` / `natural colour grading` 則仍要保留
- [ ] 身材數據（三圍/罩杯，見 `profile.json` 的 measurements）是否直接寫進 prompt，不要只用模糊形容詞
- [ ] 背景是否有具體生活雜物細節
- [ ] 服裝是否完整明確寫出（不留給模型自己猜）
- [ ] （影片）環境音層是否有指定，`generate_audio` 設定是否正確
- [ ] **（運動/健身類角色專用）是否偏向健美選手/男性化方向**：任何帶有「運動員」「健身」「肌肉線條」設定的角色，prompt 都必須明確寫「漂亮性感」「柔和曲線」「淡淡若隱若現」這類字眼，並且**明確排除**「塊狀肌肉」「血管紋理」「銳利強勢的臉」「健美比賽站姿」。2026-07-24：Vicky Lin 第一輪試跑因未做這個排除，實際生成結果變成健美選手體態，使用者明確否決、已重新生成描述——這是每個運動類角色都要檢查的固定項目，不是個案。
- [ ] **（臺灣籍角色專用）膚色是否為白皙基調**：即使是戶外/海邊/健身類人設，也不可整體呈現古銅/小麥/曬黑色調——見上方第 6 點
- [ ] **（2026-07-30 新增）整組素材是否混合自拍與他拍視角**，不是全部都用同一種「棚拍/編輯攝影」語氣——見上方第 7 點
- [ ] **（2026-08-05 修訂）人物入鏡是否分清兩類**：同框互動者維持預設沒有；但**公共場景（街道／夜市／商場／海灘／車站）應該要寫入背景路人**，並套用第 9 點那組四條件措辭（背向／不看鏡頭／失焦／外型區隔）。私密場景（臥室／浴室／自家／飯店房內）維持只有本人
- [ ] **（2026-08-05 新增）地點是否寫成「環境元素清單」而非「地名」**——見上方第 11 點，點名地標會生出錯的地標
- [ ] **（2026-08-05 新增，多張成組時）第二張以後是否用「同穿搭一日敘事」串聯**——`the exact same outfit as earlier that day —` + 完整重複服裝清單 + 一個「時間過去了」的小變化，見上方第 12 點
- [ ] **（2026-08-05 新增，造型差異化四項，見第 13 點與 `WARDROBE_SYSTEM.md`）**
  - [ ] **穿搭風格是否與上一則落在不同區間？** 招牌風格是否已超過配額（一般 ≤30%；Mia 的電競服與 cosplay-lite 各 ≤25%；Vicky 的運動機能 ≤30%）？
  - [ ] **髮型是否明確指定，且與上一則不同？**（不可只寫「長黑髮」讓模型自己決定）
  - [ ] **這批 10 則裡，C 級「完全不美的日常」地點是否至少 2 則？** 為 0 就退回重排——這是硬性下限
  - [ ] **微物件是否至少換了 2 樣，且在 prompt 裡具體點名？**（手機殼／包／鞋／髮飾／指甲／手上拿的東西）
  - [ ] **服裝段落是否寫滿五層**（上身／下身／鞋／包或外套／首飾髮飾），每層具體到單品＋材質＋顏色？只寫 `casual top and shorts` 一律退回
- [ ] **（2026-08-05 新增，Carousel 專用，見第 14 點）同一則貼文的 5–6 張，是否共用唯一一組 outfit／scene／lighting，只變表情與手勢？** 若每張都是不同場景，退回重排——那是舊做法
- [ ] **（2026-08-05 新增，影片專用，見第 15 點）切點是否 ≤3 刀、單一鏡頭 ≥4 秒？是否有一個三秒內看得懂、且由畫面（非字卡）演出來的情境？**
- [ ] **（2026-08-26 修正，第 20 點）表情是否先給了一個「有名字的表情」（回眸一笑／吐舌／眨眼／鼓臉頰／上目遣い…），再用細節修飾？** 只寫「嘴角微揚、眉毛微抬」這種微小偏差一律退回——那是影片用的寫法，靜態圖會生成面無表情
- [ ] **（2026-08-26 新增，第 20 點）這批 10 則裡表情是否換了至少 8 種？** 重複太多就退回重排
- [ ] **（2026-08-26 新增，第 21 點）是否一個 spec 只生一張？** 同 prompt 生 2 張以上的結果幾乎相同，沒有資訊價值；要變體就寫成不同 spec
- [ ] **（2026-08-26 新增，第 17 點）肢體是否寫了重心在哪隻腳、兩手分別在哪、骨盆與上半身有無扭轉？** 只寫姿勢名稱（「回頭」「站著」）一律退回
- [ ] **（2026-08-26 新增，第 17 點）這套服裝有沒有至少一個「會飄的元素」，並在 prompt 裡說明它正在動？** 沒有就換裝——這是 blocking issue
- [ ] **（2026-08-26 新增，第 18 點，最高優先）主光是否打在她臉上？** 問一句「她的臉是不是畫面最亮的區域之一」——背後的光只能當輪廓光
- [ ] **（2026-08-27 修正，第 22 點）機位是否＝被攝者的「肚臍高度」（身高×0.60）？** 第 19 點的「全身用臀部高度」是錯的——太低會腳大頭小
- [ ] **（2026-08-27 新增，第 22 點，最容易犯）全身／3-4 身是否寫了 50–85mm 與拍攝距離？** 寫 `35mm` 是廣角、會讓全身變形，一律退回
- [ ] **（2026-08-27 新增，第 22 點）站姿是否用了顯腿長定番**（一腳前伸＋重心後腳＋一手插腰／撥髮＋身體 3/4 側）**、構圖是否腳在下 1/3、上方留白？**
- [ ] **（2026-08-27 新增，第 22 點）表情與姿勢是否寫成同一個連續動作，而不是兩個獨立段落？** 分兩段寫模型會各吃一半，拼出動作與表情不一致的畫面
- [ ] **（2026-07-30 新增）生成後是否逐張實際檢查手部/肢體/鏡頭透視等 AI 瑕疵**，不是只看大方向像不像——見上方第 10 點
- [ ] **（2026-08-12 新增，使用者實測反饋，見第 16 點）鏡頭角度是否避開「由下往上」的低角度仰拍**：多鏡頭切換 prompt（如 `kling3_0`）裡每個鏡頭都要逐一檢查，不要為了角度多樣性硬塞這種本身就顯得怪的視角
- [ ] **（建立實際 Soul 訓練集專用，非探索性預覽）是否用 Reference Element 錨定身分，而不是每張獨立文字生成**：2026-07-25 Vicky Lin 案例發現，用同一組文字 prompt 各自獨立呼叫 8 次生成（無身分錨點），每次生成模型都會重新「想像」一個符合描述但**不是同一個人**的臉/身形——8 張圖風格看起來一致，但實際上是 8 個不同的人，不是同一人的 8 個角度。若把這種身分不一致的圖直接送進 Soul 訓練，訓練結果會是多人特徵的平均/混合，而非使用者想要的單一穩定身分。**正確流程**：(1) 先生成或從既有圖中選出**一張**使用者核准的參考圖；(2) 用 `media_upload` → PUT 位元組 → `media_confirm` → `show_reference_elements(action='create')` 把這張圖轉成可重複使用的 Reference Element，取得 `element_id`；(3) 之後每張訓練圖的 prompt 都內嵌 `<<<element_id>>>` 取代文字描述五官/身形，只變化角度、景別、姿勢、場景、穿搭——這樣後端會把同一張參考圖直接注入生成，確保臉部/身形真正共享同一身分。此流程適用於**任何角色**建立正式 Soul 訓練集之前，不只是 Vicky Lin 的個案；純探索性的一次性風格預覽（不打算送訓練）則不受此限制。

---

## 場景庫

---

### 一、Morning / Waking Up（晨起系列）20%

#### Scene M-1：床上晨起，直視鏡頭

**場景描述**：剛醒來的樣子，躺在白色棉麻床單上，枕頭有壓過的痕跡，頭髮略亂但好看。
**服裝**：oversized 白色棉T or 絲質細肩帶睡衣（米白 / 淡粉）
**燈光**：早晨窗邊側光（7–9am），漫射、柔和，不強烈直射
**鏡頭角度**：臉部至上半身，從略高俯角向下拍（床上視角），直視鏡頭
**情緒**：慵懶、剛醒、眼神半睜、不用力

```
lying on white linen bed, morning sunlight streaming softly through window,
wearing oversized white cotton t-shirt, sleepy half-lidded eyes looking directly at camera,
hair slightly messy on pillow, one arm stretched above head, close-up chest-to-face,
slightly overhead angle, warm diffused morning light, intimate bedroom atmosphere
```

---

#### Scene M-2：鏡前晨間，梳整頭髮

**場景描述**：早晨站在衛浴或臥室鏡前，梳頭髮或撥頭髮，半側面，沒有意識到被拍。
**服裝**：薄棉細肩帶背心 + 短褲，或只穿細肩帶睡衣上身
**燈光**：冷白浴室自然光 or 暖黃臥室晨光，取決於角色
**鏡頭角度**：從側後方拍，鏡子裡能看到她的正面，形成雙重視角
**情緒**：自然、不表演、沉浸在自己的事情裡

```
standing in front of large bedroom mirror in the morning, wearing thin cotton cami top and shorts,
hands lifting hair to tie it up or letting it fall, looking at her own reflection not at camera,
soft warm morning light from window casting gentle shadow, 3/4 angle from behind showing mirror reflection,
candid unposed moment, natural relaxed posture
```

---

#### Scene M-3：窗邊發呆，手拿咖啡杯

**場景描述**：早晨靠著窗邊，捧著咖啡杯，望向窗外，什麼都不想。
**服裝**：oversized 男友款針織毛衣（下身若隱若現）or 薄紗睡袍
**燈光**：早晨窗邊強逆光（backlit silhouette 感）or 側光打在臉部輪廓
**鏡頭角度**：從室內平視拍向窗邊，半身或全身，逆光讓輪廓發光
**情緒**：靜止、思緒飄遠、沉浸在自己的早晨

```
standing by window in morning, holding ceramic coffee mug with both hands,
wearing oversized knit sweater that barely covers, gazing out at the view not at camera,
strong backlit window light creating soft glowing outline, 3/4 body shot from inside the room,
dreamy quiet morning energy, slightly soft focus on background
```

---

#### Scene M-4：床上坐起，剛睡醒的懶散

**場景描述**：坐起來但還沒真正醒，腿收在胸前，頭靠在膝蓋上，或者撐著床頭板。
**服裝**：短版睡衣套裝（棉質細肩帶 + 短褲）或單穿細肩帶
**燈光**：窗簾沒完全拉開，漫射的柔和室內光，有點昏暗但溫暖
**鏡頭角度**：從床腳方向平視拍，全身，她在畫面一角
**情緒**：剛醒、軟、有一點可愛的困惑感

```
sitting up on bed with knees pulled to chest, wearing cotton cami and shorts set,
head tilted to one side, eyes slightly unfocused just woken up, morning light filtering through curtains,
full body shot from end of bed, off-center composition with negative space,
rumpled white bedding around her, intimate domestic atmosphere
```

---

### 二、Outfit / Changing（換裝系列）20%

#### Scene O-1：鏡前試穿，檢視全身

**場景描述**：站在全身鏡前，正在看自己的穿搭，頭微側，表情是在評估。
**服裝**：今天的穿搭（依角色的服裝公式選擇），上衣或洋裝
**燈光**：室內自然光 or 窗邊側光，讓穿搭的細節和身材比例清晰
**鏡頭角度**：鏡面正面拍（從鏡子裡看她），或從側面拍她看鏡子，雙版本各有效果
**情緒**：自我評估、安靜的自信、沒有為鏡頭表演

```
standing in front of full-length mirror looking at her reflection, head slightly tilted assessing the outfit,
wearing [outfit], natural indoor light from nearby window,
mirror selfie shot — camera visible in mirror reflection held casually at chest height,
slightly off-center, neutral expression with hint of satisfaction, body visible from head to toe
```

---

#### Scene O-2：換裝中途，只穿內搭

**場景描述**：換衣服換到一半，只穿內搭（細肩帶或運動背心），下一件衣服還拿在手上。
**服裝**：棉質細肩帶或 bralette（SFW），手上拿著還沒穿的外衣
**燈光**：臥室窗邊自然光，柔和直接
**鏡頭角度**：3/4 身，平視，她側對著鏡頭
**情緒**：隨意、自然，不是在表演性感，就是在換衣服

```
mid-outfit-change, wearing just a cotton cami or bralette, holding a shirt in one hand not yet put on,
turning slightly to grab something off the bed, 3/4 body angle, casual and unaware,
bedroom natural light, clothes visible on bed in background suggesting she's been trying things on,
natural relaxed posture, candid moment
```

---

#### Scene O-3：坐在床邊穿鞋，低頭綁鞋帶

**場景描述**：快要出門，坐在床邊穿鞋或綁鞋帶，低頭，整套穿搭清晰可見。
**服裝**：完整的當日穿搭，腿部可見（短裙 / 短褲 / 緊身褲）
**燈光**：室內暖光 or 窗邊午前光
**鏡頭角度**：從斜前方平視，全身坐姿，腿部比例清楚
**情緒**：準備出門的最後一刻，專心、不看鏡頭

```
sitting on edge of bed putting on sneakers, wearing [full outfit] showing legs clearly,
leaning forward to tie laces, focused on shoes not camera,
bedroom ambient light, full body sitting shot from slightly in front and to the side,
outfit fully visible, candid getting-ready moment before going out
```

---

#### Scene O-4：衣服掛滿，站在衣櫃前考慮

**場景描述**：站在打開的衣櫃前，手放在衣架上，思考今天要穿什麼。只穿著睡衣或內搭。
**服裝**：晨間睡衣或細肩帶，背對或側對鏡頭
**燈光**：臥室窗光或衣櫃燈的暖黃光
**鏡頭角度**：從床側拍她的背影或側面，衣櫃填滿背景
**情緒**：日常選擇的糾結，安靜、不為人看的狀態

```
standing in front of open wardrobe in morning, wearing cami and shorts or silk slip,
hand resting on hanging clothes looking at options, back or side profile facing the wardrobe,
warm soft light from bedside lamp or window, full body or 3/4 shot,
intimate domestic scene, clothes clearly hanging in background, no awareness of camera
```

---

### 三、Bathroom / After Shower（浴後系列）15%

#### Scene B-1：浴後白巾，浴室鏡前

**場景描述**：洗完澡，白色浴巾包裹身體，站在浴室鏡前，頭髮濕潤，皮膚微紅。
**服裝**：白色浴巾（從胸部包到大腿），或浴袍
**燈光**：浴室柔和燈光（不是刺眼白光），或窗邊透進的自然光，有蒸氣感
**鏡頭角度**：平視，半身或全身，可以是鏡中反射
**情緒**：剛洗完澡的放鬆、皮膚有水份的光澤、不刻意

```
standing in bathroom after shower, wrapped in white towel tucked at chest,
damp hair, skin slightly flushed, facing bathroom mirror with relaxed expression,
soft warm bathroom light with faint steam in air, medium shot mirror reflection visible,
natural post-shower state, one hand touching damp hair, calm and unhurried
```

---

#### Scene B-2：護膚例行，棉T站在浴室

**場景描述**：洗完澡換上棉T短褲，站在浴室或梳妝台前做護膚，拍眼霜或塗乳液。
**服裝**：短版棉T + 短褲，或細肩帶背心，皮膚剛洗完澡的狀態
**燈光**：浴室冷白自然光（Yuna 類型）或暖黃窗邊光（Camille 類型）
**鏡頭角度**：臉部至上半身近景，她看向鏡子而不是鏡頭
**情緒**：專注、護膚中、沉浸在自己的事情

```
standing at bathroom vanity doing skincare, wearing cotton cami and shorts,
applying moisturizer with fingertips, eyes focused on mirror reflection not camera,
clean bathroom light, close-up chest to face, skin visibly clean and freshly washed,
peaceful skincare routine moment, minimal products visible on counter
```

---

#### Scene B-3：浴缸邊，腿伸出來

**場景描述**：泡澡中，側躺在浴缸邊緣，腿伸出來，手臂放在浴缸邊，眼睛閉著或望向上方。
**服裝**：無（泡泡浴遮蓋），或薄棉睡袍放在浴缸邊
**燈光**：蠟燭暖光 or 浴室晨光，整體昏暗而溫暖
**鏡頭角度**：從浴缸側面拍，半身，腿部清晰可見
**情緒**：完全放鬆、奢侈的獨處時刻、慵懶而滿足

```
lying in bathtub with foam bubbles, one leg resting on the edge of the tub,
arm draped over the side, eyes closed or looking upward with relaxed expression,
warm candlelight or soft bathroom window light, medium shot from the side showing profile and leg,
steamy intimate bathroom atmosphere, small candles or greenery visible in background
```

---

### 四、私下 / 她自己的空間（25%）

> **2026-08-27 憲章同步**：本系列原名「Home Lounging 居家閒躺」，框架是「最放鬆、什麼都不做」。
> 依 [`PERSONA_CANON.md`](PERSONA_CANON.md) 原則一，這個框架已作廢——
> 私下的她**依然精心打理自己**，只是打理的方向從「給任何人看」換成「只給自己和特定的人看」。
> 以下 L 系列場景仍可用，但使用時要把服裝與情緒往「她自己選擇要留下這個畫面」的方向寫，
> 而不是「懶散、無聊、不在意」。每則 prompt 的服裝都必須具體寫出材質與款式。

#### Scene L-1：沙發上的懶散，滑手機

**場景描述**：窩在沙發上，腿搭在扶手上或橫躺著，滑手機，完全不在意被拍。
**服裝**：oversized 棉T + 短褲，或細肩帶 + 短褲，光腳
**燈光**：午後客廳自然光（窗簾沒完全拉），或傍晚落地燈的暖光
**鏡頭角度**：從沙發正前方或斜前方平視，全身可見，偏側臥姿
**情緒**：放鬆但有意識——她知道自己現在的樣子好看，這個畫面是她自己要留下的

```
lying on sofa with legs up over the armrest, scrolling phone held above face,
wearing oversized cotton tee and shorts, barefoot, hair loose and casual,
afternoon living room light through curtains, full body side-lying shot from in front of couch,
relaxed but self-aware at home, unhurried, phone screen slightly glowing
```

---

#### Scene L-2：地板坐著，吃零食看電視

**場景描述**：坐在客廳地板上，背靠沙發，吃零食，面前可能有筆電或電視。
**服裝**：短版棉T + 緊身短褲，或運動短褲，光腳
**燈光**：電視 / 螢幕的藍光 + 室內暖燈，兩種光同時存在
**鏡頭角度**：從斜側面平視，半身至全身，她面對螢幕而非鏡頭
**情緒**：完全在自己的世界裡、有點懶、有點放空

```
sitting on living room floor with back against sofa, eating snacks from a bowl,
wearing crop tee and tight shorts, legs stretched out or crossed,
TV or laptop screen light mixing with warm lamp in background,
3/4 shot from the side, completely absorbed in screen, natural domestic scene
```

---

#### Scene L-3：臥室地板，看書或發呆

**場景描述**：坐在臥室地板上，背靠床，腿伸直，手拿一本書或什麼都不做，望向遠處。
**服裝**：細肩帶背心 + 短褲，光腳，頭髮鬆散
**燈光**：午後臥室窗邊散射光，整體柔和暖黃
**鏡頭角度**：從正前方或斜前方平視，全身，腿部比例清楚
**情緒**：沉靜、一個人的時光、完全不需要表演

```
sitting on bedroom floor leaning against the bed, legs stretched out, reading a book or looking into distance,
wearing cami top and shorts, barefoot, hair loosely tied or down,
soft afternoon light from window, full body front-facing shot showing long legs,
quiet introspective mood, entirely alone in her own world
```

---

#### Scene L-4：床上捲縮，抱枕頭，電話中

**場景描述**：側躺在床上，抱著枕頭，講電話或聽音樂，身體捲縮但放鬆。
**服裝**：絲質細肩帶睡衣 or 棉質短版睡衣套裝
**燈光**：傍晚臥室暖燈光，溫柔而昏黃
**鏡頭角度**：從床側拍，全身側躺，她面對另一個方向
**情緒**：放鬆、溫暖、像好朋友偷偷拍到的她

```
lying on side on bed hugging pillow, on phone or listening to music with earphones,
wearing silk slip or cotton pajama set, knees slightly bent, body curled comfortably,
warm evening bedroom lamp light, full body shot from side of bed,
she's facing away from camera or turned slightly, intimate cozy evening at home
```

---

### 五、Hotel / Travel（飯店旅行系列）15%

#### Scene H-1：飯店大床，剛到房間

**場景描述**：剛到飯店，直接倒在大床上，仰躺或趴著，行李還放在旁邊。
**服裝**：出門的當日穿搭（不用特別換），或剛換上飯店睡袍
**燈光**：飯店房間的暖黃燈光，或窗外的城市光線透進來
**鏡頭角度**：從床腳方向拍，全身，她倒在床上，城市窗景在背景
**情緒**：旅行抵達的放鬆感、終於可以倒下、有點興奮

```
just arrived at hotel room, flopped on the large bed face-up or face-down,
wearing travel outfit still, arms out to the sides, shoes possibly still on one foot,
warm hotel room lighting with city view visible through window,
full body shot from foot of bed looking toward the window, bags visible to the side,
arrival relief energy, genuine exhausted-but-happy
```

---

#### Scene H-2：飯店浴袍，窗邊看夜景

**場景描述**：穿著飯店白色浴袍，站在落地窗前，一手拿著酒杯或咖啡，看著城市夜景。
**服裝**：白色飯店浴袍，寬鬆，腰帶輕繫
**燈光**：室內暖燈 + 窗外城市燈光，對比鮮明
**鏡頭角度**：從房間內側拍，半身或全身，她面對窗戶背對鏡頭，或側面
**情緒**：有點孤獨也有點自在、城市在腳下、這個夜晚是她自己的

```
wearing white hotel robe loosely belted, standing at floor-to-ceiling window holding a wine glass,
looking out at city lights below, back or profile to camera,
warm amber room lighting contrasting with blue-lit city outside,
full body or 3/4 shot from inside the room, cinematic quiet night energy
```

---

#### Scene H-3：飯店泳池，躺椅邊

**場景描述**：飯店屋頂泳池，坐或躺在白色躺椅上，腿垂入水或晒太陽，有飲料在旁邊。
**服裝**：一件式泳衣 or 比基尼（依角色選擇），太陽眼鏡
**燈光**：下午陽光（3–5pm），直射或城市天際線背景
**鏡頭角度**：從旁邊平視拍，全身或半身，腿部比例清楚
**情緒**：vacation mode、陽光、完全不想事情

```
sitting on poolside lounger at hotel rooftop pool, legs dangling in turquoise water,
wearing one-piece swimsuit [or bikini], sunglasses on, hand resting on armrest with drink nearby,
afternoon sun casting warm shadows, city skyline visible in background,
3/4 body shot from poolside, relaxed confident vacation energy, slightly squinting in the sun
```

---

#### Scene H-4：飯店床上，深夜獨處

**場景描述**：飯店房間深夜或清晨，在床上吃簡單的東西或喝東西，手機在旁邊，燈光很暗。
**服裝**：飯店睡袍 or 自帶的細肩帶睡衣
**燈光**：床頭燈的暖黃光，只有一個光源，整體很暗但溫暖
**鏡頭角度**：從床側拍，半身，她看著手機或看向食物，不看鏡頭
**情緒**：旅行時的那種「不想睡」、獨自在陌生城市的夜晚感

```
late night in hotel room sitting on bed eating room service snacks or drinking tea,
wearing silk slip or hotel robe, phone lit beside her on the bed,
only bedside lamp on creating warm intimate pool of light in otherwise dark room,
medium shot from beside the bed, she's focused on her phone not camera,
quiet solo traveler night energy, city outside the window dark and distant
```

---

### 六、Daily Selfie Video（手機自拍日常影片）— 主力內容

> **定位**：男性受眾的核心日常內容。手機自拍感，真實不刻意，展示身材但不像廣告。
> **模型**：`kling3_0`（單鏡頭，透過 `start_image` 鎖定臉部身份）
> **Benchmark 帳號**：@yua_mikami、@asuka.kirara、@eimi0318
> **完整 SOP 見**：`DAILY_VIDEO_SOP.md`

#### 核心方向

- **不是廣告**：不要 multi-shot 剪輯，不要旁白，不要 CTA，就是她在自拍
- **手機自拍角度**：slightly overhead angle（從上方俯拍臉和胸），或 arm-level selfie（正面平視）
- **鏡頭真實感**：適時加入輕微 camera rotation / movement，讓影片看起來像真人拿著手機拍
- **BGM 後製**：聲音在 CapCut 後製加入，生成時 `sound = "on"` 但 prompt 不提音樂

#### 已驗證場景（2026-07-07 全部批准）

| KOL | 場景 | 服裝 | 重點 | Start Frame Media ID | Video Job ID |
|-----|------|------|------|----------------------|-------------|
| Iris Chen | 浴室鏡前，手持手機自拍，微微低頭露乳溝 | 黑色細肩帶背心 | 乳溝，浴室燈光 | `b8078a7d` | `b68ac46c` |
| Yuna Kim | 飯店房間門邊慢慢轉身，側面到正面展示胸腰比 | 白色 crop top + 低腰牛仔短褲 | 胸腰比，身材線條 | `9e7d8009` | `2aca7a9e` |
| Luna Tanaka | 床上仰拍，俯角，臉到胸口，微笑看鏡頭 | 白色薄棉睡衣，領口微開 | 童顏巨乳反差 | `81d7442e` | `c2cfc025` |
| Aaliya Rivera | 泳池邊，半身出水，撥頭髮，看鏡頭 | 黑色比基尼上衣 | 濕身，運動感性感 | `e6892cd0` | `d51676c3` |
| Camille Dupont | 臥室窗邊逆光，轉頭看鏡頭，側面輪廓 | 白色絲質（實際生成：crop top + bikini bottom） | 逆光側面輪廓 | `5c868b09` | `c70f6307` |
| Ananya Kapoor | 浴室出來，濕髮，毛巾裹身，露鎖骨露肩 | 白色浴巾，微開露肩 | 濕髮，鎖骨，肩膀 | `d94c27c9` | `59dcbb98` |

#### Start Frame 生成原則

- **角度**：描述「phone selfie angle from above」或「arm-level selfie」，而非「她拿著手機」
- **服裝**：日常服裝（睡衣、泳衣、浴巾等），不能用舞蹈 start frame 代替
- **服裝避雷**：crop top 露腹、belly dance bra 等 revealing 服裝 → `status: "failed"`（pixel-level filter）
- **Soul ID 流程**：`soul_2` 生成圖 → `media_import_url` 匯入 → `image_media_id` → 帶入 `kling3_0` 的 `start_image`

#### 影片 Prompt 核心元素

```
[年齡+民族+身材特徵],
[場景描述 — 浴室/床/泳池/飯店],
[服裝] + [關鍵身體焦點 — cleavage/collarbone/waist ratio],
[動作 — 轉身/撥頭髮/看鏡頭],
[鏡頭角度 — phone selfie / overhead / arm-level],
[光線描述],
single continuous shot, phone selfie casual feel, warm tones
```

#### 鏡頭真實感規則

- 日常自拍影片應加入輕微 camera rotation / subtle hand movement
- 讓影片看起來像真人手拿手機拍，而非三腳架固定的靜態畫面
- 在 prompt 加入：`slight natural camera movement as if hand-held, subtle rotation`

#### 各 KOL 日常自拍推薦方向

| KOL | 場景方向 | 服裝方向 | 身體焦點 |
|-----|---------|---------|---------|
| **Iris Chen** 台北熱辣 | 浴室、健身後、臥室 | 黑色細肩帶、運動背心 | 乳溝、腰線 |
| **Luna Tanaka** 京都安靜 | 床上、榻榻米、浴室後 | 白色薄棉睡衣、浴巾 | 童顏巨乳反差、鎖骨 |
| **Ananya Kapoor** 孟買舞者 | 浴室後、瑜伽後、泳池 | 浴巾、瑜伽服 | 鎖骨、肩線、纖腰 |
| **Yuna Kim** 首爾美妝 | 飯店、臥室、護膚時 | crop top、睡衣 | 胸腰比、高挑身材 |
| **Aaliya Rivera** LA 拉丁 | 泳池、海邊、健身後 | 比基尼上衣、運動服 | 曲線、濕身效果 |
| **Camille Dupont** 巴黎慢活 | 臥室窗邊、飯店、浴後 | 絲質睡衣、浴袍 | 側面輪廓、逆光 |

---

### 七、TikTok Dance（舞蹈影片系列）

> 完整生成流程見 `DANCE_VIDEO_SOP.md`。本節僅記錄場景庫和服裝參考。

**核心氛圍**：跟著 TikTok 熱門歌曲跳舞，性感有活力，節拍感強。三段式：進場→主舞→收尾。

#### 服裝選擇原則

| 類型 | 服裝範例 | 效果 |
|------|---------|------|
| 緊身運動風 | black crop top + high-waist biker shorts | 腰線和臀線清晰，動作自然 |
| 性感休閒 | light blue V-neck mini dress | 飄逸感，裙擺隨動作飛起 |
| 派對風 | silver metallic mini skirt + crop top | 反光，在燈光下效果好 |
| 街頭風 | oversized hoodie（crop）+ tight shorts | 年輕感，臀部線條突出 |

**構圖規則**：所有舞蹈影片使用 **THREE QUARTER SHOT（mid-thigh up, no shoes shown）**，避免腿部截斷。

#### 背景選擇

| 背景 | 氛圍 | 適合 |
|------|------|------|
| Plain white/gray studio | 簡潔，突出舞者 | 首選（不分散注意力） |
| Urban rooftop, city at dusk | 城市感，台北/首爾 | 有場景感的版本 |
| Club/neon lighting background | 夜店感，強燈光 | 派對主題 |
| Bedroom/living room | 居家隨性感 | 模仿真實 TikTok 風格 |

#### 音樂類型與舞蹈效果

| 音樂類型 | 適合舞蹈 prompt 描述 |
|---------|-------------------|
| 越南鼓（Vietnamese drum） | `powerful rhythmic stomping, traditional meets street style, hip drops` |
| K-pop（流行/電音） | `K-pop choreography, sharp arm movements, body roll, bouncing to beat` |
| 拉丁（reggaeton/cumbia） | `hip-hop reggaeton moves, waist rolls, confident swagger` |
| 西方流行（pop/R&B） | `body wave, chest bounce, fluid arm movements, sensual groove` |

#### 各 KOL 舞蹈推薦

| KOL | 推薦服裝 | 推薦音樂 | 背景 |
|-----|---------|---------|------|
| **Iris Chen** 台北熱辣 | 黑色 crop top + 騎車短褲，或 mini dress | 越南鼓、Sugar on my tongue | 白色背景或城市夜景 |
| **Luna Tanaka** 京都安靜 | 白色短版和服領上衣 + 黑色緊身褲 | 輕柔 J-pop 或 city pop | 日式簡潔室內 |
| **Ananya Kapoor** 孟買舞者 | 印度傳統 crop top + 露腰半裙 | Bollywood remixes | 金色燈光背景 |
| **Yuna Kim** 首爾美妝 | 韓系短版外套 + 短褲 | K-pop | 首爾都市感背景 |
| **Aaliya Rivera** LA 拉丁 | 性感拉丁裙或緊身褲 | Reggaeton/Latin pop | 城市夜景 |
| **Camille Dupont** 巴黎慢活 | 法式休閒 + 緊身褲 | 法語流行 or 歐洲電音 | 簡潔白背景 |

---

### 七、Fitness / Active（運動系列）10%

#### Scene F-1：瑜伽後躺在地墊上

**場景描述**：瑜伽做完，仰躺在瑜伽墊上，手臂張開，閉眼放鬆，做最後的攤屍式。
**服裝**：瑜伽套裝（高腰緊身褲 + 運動背心 or sports bra）
**燈光**：室內瑜伽空間的自然漫射光，或晨間木地板上的斜射光
**鏡頭角度**：從正上方俯拍（鳥瞰），全身，她在地墊上
**情緒**：運動後的完全放鬆、什麼都不想、身體在地板上融化

```
lying flat on yoga mat after practice in savasana pose, arms slightly out to sides, eyes closed,
wearing high-waist yoga leggings and sports bra, visible muscle definition,
soft natural light on wooden floor, overhead bird's eye shot looking down at her on the mat,
complete post-workout surrender, slight sheen of sweat, peaceful exhaustion
```

---

#### Scene F-2：鏡前伸展，側面線條

**場景描述**：對著大鏡子做伸展，側面拍到她的身體線條，表情專注，沒有對鏡頭。
**服裝**：高腰緊身瑜伽褲 + 細肩帶運動上衣，光腳
**燈光**：健身空間的自然光 or 大窗側光，強調身體線條的立體感
**鏡頭角度**：側面拍，全身，身體的伸展線條是主角
**情緒**：專注、身體的力量感、完全沉浸在動作裡

```
stretching in front of large mirror, side profile showing full body extension,
wearing high-waist leggings and fitted sports top, barefoot on wood floor,
strong natural side light from window accentuating muscle lines and curves,
full body side shot, expression focused and absorbed in the stretch, not looking at camera
```

---

#### Scene F-3：運動後，坐在地板喝水

**場景描述**：健身或跑步完，坐在地板上，腿伸直，大口喝水，頭髮有些凌亂，臉上有汗。
**服裝**：運動套裝（緊身褲 + 運動背心），可能有外套半脫在腰上
**燈光**：戶外黃金時段光 or 室內健身空間自然光
**鏡頭角度**：從斜前方平視，半身至全身，她正在喝水，不看鏡頭
**情緒**：運動完的真實疲憊感、有汗有氣、這個狀態比刻意擺拍更吸引人

```
sitting on floor after workout, legs stretched out, drinking from water bottle,
wearing athletic set, hair slightly disheveled, light sweat visible on skin,
golden hour outdoor light or gym window light, 3/4 body shot from slightly in front,
looking at something off-frame not camera, genuine post-exercise fatigue and satisfaction,
sports jacket or hoodie loosely around waist
```

---

## 各角色推薦組合

| KOL | 最適配場景（按角色美學） |
|-----|----------------------|
| **Iris Chen** 台北熱辣 | O-1 鏡前穿搭、M-1 床上晨起直視鏡頭、H-3 飯店泳池、Dance 六 舞蹈影片 |
| **Luna Tanaka** 京都安靜 | M-3 窗邊發呆、B-3 浴缸邊、L-3 臥室地板看書 |
| **Ananya Kapoor** 孟買舞者 | F-1 瑜伽後躺墊、F-2 鏡前伸展、M-3 窗邊（晨間海邊版） |
| **Yuna Kim** 首爾美妝 | B-2 護膚例行、M-2 鏡前梳整、O-1 鏡前穿搭 |
| **Aaliya Rivera** LA 拉丁 | H-3 飯店泳池、O-2 換裝中途、L-1 沙發懶散 |
| **Camille Dupont** 巴黎慢活 | M-3 窗邊（薄紗睡袍版）、H-2 浴袍看夜景、B-3 浴缸泡澡 |

---

## Prompt 通用結尾模板

所有場景加上以下結尾效果更佳：

```
film grain, candid lifestyle photo, shot on 35mm, warm tones,
slightly off-center composition, natural imperfect framing like a friend took the photo
```

---

*最後更新：2026-07-07*

---

### 17. 靜態圖也要有表情設計、肢體設計與「會飄的元素」（2026-08-26 新增，pilot 實測反饋）

**背景**：批次 1 pilot 生出 4 張，使用者反饋「姿勢僵硬、表情都沒什麼變化、人不亮眼」。
逐條追回 prompt 後發現，問題不在模型，在**規格本身缺了三個維度**。

`.claude/agents/emotion-director.md` 與 `performance-director.md` 早就寫了這些原則，
但它們的描述只提到「video / clip」，所以規劃靜態圖時整個被跳過了。
**這三條對靜態圖同樣適用**，只是形式不同：

#### 17-A. 表情（⚠️ **本小節已被下方第 20 點取代**——那套寫法只適用影片，靜態圖要先給表情名稱）

「看鏡頭微笑」是死的。每個 prompt 都要寫明：

- **哪邊嘴角高、哪邊眉毛抬**（對稱的臉是最強的 AI tell）
- **眼睛在看什麼**——寫出具體的東西或方向（「看向鏡頭稍微偏右，像剛被叫住在找聲音來源」、
  「看著亭外的雨」），而不是 `looking at camera`
- 捕捉**表情的中間態**：正要說話、剛想到什麼、憋笑破功的那一秒

#### 17-B. 肢體：寫身體在做什麼，不是寫姿勢名稱

「走在巷子裡回頭」是姿勢名稱。要寫的是：

- **重心在哪隻腳**，另一隻腳在做什麼（腳跟離地／腳尖點地／膝蓋微彎）
- **骨盆與上半身的關係**（有沒有扭轉；雙腳平均站立＝最死板的站姿）
- **兩隻手分別在哪**、手指的狀態
- **捕捉動作的中間態**：走路被叫住的那一秒，不是站定擺姿勢

#### 17-C. 每套服裝至少要有一個「會飄的元素」

`performance-director.md` 的原話：「若服裝沒有可擺動元素，**這是 blocking issue，
要求換裝**，不是 nitpick。」這條對靜態圖一樣成立——一張沒有任何東西在動的照片就是僵的。

可用的元素：敞開的長版薄襯衫、只掛在肩上沒穿進袖子的開襟外套、被風帶起的髮尾、
裙襬、長帶子、耳環。**寫進 prompt 時要說明它正在動**（「下襬還在轉身的慣性裡飄著」）。

---

### 18. 主光必須打在臉上——五段式公式不保證「人好看」（2026-08-26 新增，pilot 實測反饋）

**這是第 3 點五段式物理光線公式的必要補充。**

pilot 的 YG-06 光線段寫的是：
`low sun raking in from the far end of the alley **behind her**`
——主光被指定在人物**背後**。五段式的其他四段都寫對了（有具名反射面、有色溫分裂、
有曝光取捨、有遮擋框架），生出來也確實物理成立，**但人是暗的、不亮眼**。

> **五段式公式保證的是「這個空間的光說得通」，不保證「這個人好看」。**
> 反射補光在物理上永遠比主光弱，主光在背後 ＝ 臉一定暗。

**補充規則**：

- **① KEY 的方向必須讓光落在她臉上**——正面或前側 45 度。
- 背後、側後方的光**只能當輪廓光／邊緣光**，不能當 KEY。
- 逆光構圖不是不能拍，但**要明確寫出補光從哪個具名表面來、而且要夠強**
  （例如正對面的白牆、大片沙灘、雪地），否則不要用。
- 檢查方式：問一句「**這張圖裡她的臉是不是畫面最亮的區域之一？**」不是就重寫。

---

### 19. ⚠️ 機位高度要寫「離地公分數」（2026-08-26）——**換算表已被下方第 22 點修正，以第 22 點為準**

pilot 的 LG-05 寫的是 `camera at chest height` ——**但沒說是誰的胸口**。
Luna 只有 155cm，模型採用了拍攝者的高度，變成由上往下俯拍她，
結果**頭大、腿短**，比例完全跑掉。

**規則**：機位一律寫成**離地的絕對公分數**，按該角色的身高換算。

| 景別 | 建議機位 | 155cm（Luna） | 168cm（Yuna） |
|---|---|---|---|
| 臉部近景 | её眼睛高度 | ≈144cm | ≈156cm |
| 半身 | 胸口高度 | ≈115cm | ≈125cm |
| 3/4 身 | 腰部高度 | ≈92cm | ≈100cm |
| **全身** | **臀部高度** | **≈80cm** | **≈88cm** |
| 坐姿 | 坐姿眼睛高度 | ≈70cm | ≈75cm |

**並且一律加註「鏡頭嚴格保持水平（horizontal），不上仰」**——
低機位負責拉長腿部比例，水平鏡頭負責避開第 16 點說的仰拍變形。
兩者要一起寫，只寫低機位會被理解成仰拍。

**嬌小角色（<160cm）拍全身時這條特別關鍵**，是最容易失敗的一種組合。

---

### 20. 靜態圖的表情要「先有名字，再有細節」（2026-08-26 修正第 17-A 點）
> ⚠️ **2026-08-27 實測補充：「有名字」還不夠，還必須「綁在一個實體動作上」。**
> 下面表情庫裡的純臉部項目（回眸一笑、上目遣い、挑眉微笑…）**實測不會被執行**。
> 見第 23 點，用那裡的改寫版取代。

**第 17-A 點（不對稱＋眼神焦點）寫錯了適用範圍，這一條取代它。**

那套「左嘴角比右邊高一點、右眉微抬、眼神看向鏡頭偏右」的寫法來自
`.claude/agents/emotion-director.md`——但那是為**影片**設計的：影片裡臉會動，
不對稱是為了避免「一秒以上不動的面具臉」。

**靜態圖不是這樣看的。一張照片就是一個表情。**
只寫微小偏差而沒有主體，讀的人想像不出來，生成出來就是**面無表情**。

#### 正確寫法：表情名稱在前，細節修飾在後

```
❌ 右嘴角微揚、左眉略高、眼神看向鏡頭稍微偏右
✅ 回眸一笑——轉頭的瞬間眼睛彎成月牙，嘴唇微開像在笑出聲，
   髮尾還在甩動的軌跡上
```

**先給一個有名字、想像得出來的表情**，再用一兩個細節讓它具體。

#### 表情庫（每批素材至少換 8 種，不要重複）

**可愛系**
| 表情 | 具體 |
|---|---|
| **回眸一笑** | 轉頭瞬間眼睛彎成月牙，嘴唇微開，髮尾在甩動軌跡上 |
| **吐舌** | 舌尖輕輕吐出、眼睛彎起來，通常配單眼眨眼 |
| **眨眼（wink）** | 單眼閉起、另一眼看鏡頭，同側嘴角上揚 |
| **鼓臉頰** | 嘟嘴鼓氣，眼睛圓睜看鏡頭 |
| **歪頭笑** | 頭往一側傾 15–20 度，眼睛彎，肩膀同側微聳 |
| **雙手托腮** | 手肘撐桌、雙手托著兩頰，臉被擠得圓一點 |
| **比 V** | 手勢舉到臉旁或眼下，笑到瞇眼 |
| **摀嘴笑** | 手背或指尖擋在嘴前，眼睛彎起來 |
| **上目遣い** | 頭略低、眼睛往上看鏡頭（日系經典） |
| **嘟嘴** | 韓系的無聊嘟嘴，眼神平淡 |
| **手比小愛心** | 拇指食指交叉，舉在臉側 |

**逗趣系**
| 表情 | 具體 |
|---|---|
| **憋笑破功** | 抿著嘴想忍住，最後笑出來，眼睛瞇成一條線 |
| **驚訝張嘴** | 眼睛睜大、嘴呈小 O 形，眉毛抬高 |
| **被拍到嚇一跳** | 正在做別的事，突然轉頭，表情還沒準備好 |
| **邊吃邊瞪大眼** | 嘴裡還有東西、臉頰鼓著，眼睛圓睜看鏡頭 |
| **假裝生氣** | 皺眉＋嘟嘴，但眼睛在笑 |

**擺拍系**
| 表情 | 具體 |
|---|---|
| **撥髮回眸** | 一手正把頭髮撥到耳後，同時轉頭看鏡頭 |
| **挑眉微笑** | 一邊眉毛抬起、嘴角單邊上揚（自信、chic） |
| **閉眼享受** | 眼睛閉起、嘴角放鬆微揚（吃到好吃的、護膚、曬太陽） |
| **側身回眸** | 身體背對、只有頭轉回來 |
| **抓裙襬轉圈** | 雙手提著裙襬，笑著看鏡頭 |
| **手遮陽光瞇眼笑** | 手擋在額前，瞇著眼笑 |

#### 兩位的取向

- **Yuna（韓系）**：偏 chic 一點——回眸、撥髮、挑眉、嘟嘴、笑到瞇眼。
  可愛的也能做，但不要太幼齒。
- **Luna（日系可愛）**：吐舌、鼓臉頰、比 V、歪頭、上目遣い、雙手托腮——
  這些是她的主場。

> 這是**選項清單，不是配額**。一批裡換得夠多就好，
> 也可以出現清單以外的表情。

---

### 21. 每個 spec 只生一張，變化靠改 prompt 不靠 count（2026-08-26 修正，取代「每批生 2 張」）
> ## ⚠️ 2026-08-28 修正：正式批次改成**一個 spec 生 2 張、選 1 張**
>
> 這一點原本寫「一個 spec 只生一張」——那是在**以為輸出可控**的前提下訂的。
> 14 張實測後（依 unique image 計）：**hard defect 3/14 ≈ 21%、服裝漂移 7/14 ≈ 50%**。
> 一張 0.12 credits，21 件多生一份只多約 2.5 credits，**遠低於逐張返工與中斷流程的成本**。
>
> **但兩張不是 prompt 修正的替代品**，必須配分流規則使用：
>
> | 兩張的結果 | 判讀 | 處置 |
> |---|---|---|
> | 一張成功 | 隨機瑕疵 | **選片**，不改 prompt，不因此改全批規則 |
> | 兩張**同方向**失敗 | **系統性偏差** | **立刻停這件**，改 prompt 再跑。**不要用原句繼續抽** |
> | 兩張都失敗但方向不同 | 隨機 | 可再跑一次；連續三次記為系統性 |
>
> 牛仔裙連續 3/3 變短褲就是系統性偏差——那種**抽卡抽不出來**。
>
> **記錄時要分開標示「隨機 defect（兩張結果不同）」與「系統性 drift（兩張同方向失敗）」。**
> 另：要比較兩種 wording 請另立 A/B，**不要把不同 prompt 的兩張混稱為「選 1」**。
>
> 原本反對 `count=2` 的理由仍然成立——那是「同一次呼叫產出兩張幾乎一樣的圖」，
> 第二張沒有新資訊。**現在是兩次獨立生成，第二張的用途是對沖隨機瑕疵，不是變體。**


`kols/iris-chen/generation_notes.md` 的舊做法是「每批次生成 2 張（不用 4 張：
同場景同 prompt 下 4 張差異太小）」。**實測後修正為：同一個 spec 只生 1 張。**

**原因**：2026-08-26 的 pilot 用 `count=2` 生了兩組，
**每組兩張的構圖、姿勢、服裝幾乎一模一樣**——差異只有隨機 seed 帶來的細微變化。
既然如此，第二張沒有提供任何新資訊，只是把同一個結果再看一次。

**新做法**：

1. **一個 spec → `count=1`**
2. 不滿意就**改 prompt 再生一張**——改動本身才是資訊（知道哪個描述沒吃到）
3. 真的需要同場景多張變體時，**寫成不同的 spec**
   （不同表情、不同景別、不同機位），而不是靠 `count` 複製

> 圖片成本極低（實測約 0.12 credits/張，見 `clients/*/cost-log.md`），
> 所以「多生幾張」不是成本問題，是**資訊問題**：
> 同 prompt 的第二張學不到東西，改過的第二張才學得到。


---

### 22. 全身街拍的參數方向（2026-08-27 修正第 19 點）
> ⚠️ **本節的數值經外部覆核後降級為「方向與起點」，不是規格。**
> 特別是：機位不要寫絕對公分數（改相對描述）、不要全部用 85mm、不要每張都固定距離。
> 詳見 `PHOTO_DIRECTION_STANDARD.md` 開頭的修正說明。

**第 19 點的換算表寫錯了，這一條取代它。**

pilot v2 的兩張全身照仍然不好看：Yuna 動作與表情不一致，Luna 仍讀起來像俯拍、
而且「不像正常拍全身照會站那麼近」。查證網美街拍的實際做法後，錯在三個參數。

#### 22-A. 機位高度＝被攝者的「肚臍高度」，不是腰／臀

> 業界說法：**「很多人誤以為鏡位越低越能拍出長腿，但其實這樣只會顯得腳大頭小，
> 呈現古怪的比例。」中鏡位（鏡位高度約在肚臍處）能讓身體比例最真實還原。**

第 19 點寫「全身用臀部高度」是錯的——**太低了**。

| | 公式 | Luna 155cm | Yuna 168cm |
|---|---|---|---|
| **全身（正確）** | **身高 × 0.60（肚臍）** | **≈93cm** | **≈101cm** |
| ~~全身（第 19 點的錯誤值）~~ | ~~臀部~~ | ~~80cm~~ | ~~88cm~~ |
| 3/4 身 | 身高 × 0.62 | ≈96cm | ≈104cm |
| 半身 | 胸口 | ≈115cm | ≈125cm |
| 臉部近景 | 眼睛高度 | ≈144cm | ≈156cm |

> Yuna 那張我寫 100cm，**高度其實是對的**——她不好看是敗在下面兩點。
> Luna 我寫 80cm，**低於她的肚臍**，所以還是歪的。

#### 22-B. 焦段：全身街拍用 50–85mm，**絕對不要寫 35mm**

我在兩張的 prompt 都寫了 `shot on a 35mm lens`。**35mm 是廣角**——
用在全身近距離會讓靠近鏡頭的部位放大、臉與四肢比例失真，
正是業界說的「記得把廣角關掉以免變形」。

| 景別 | 焦段 | 拍攝距離 |
|---|---|---|
| **全身** | **50–85mm** | **3–5 公尺**（站遠一點） |
| 3/4 身 | 50–85mm | 2–3 公尺 |
| 半身／近景 | 85mm | 1.5–2 公尺 |
| 自拍 | 手機前鏡頭（本來就廣角，這時才寫） | 手臂長度 |

**prompt 要同時寫焦段與距離**，例如
`shot on an 85mm lens from about 4 metres away, compressed perspective, no wide-angle distortion`。

#### 22-C. 構圖與站姿：用網美定番，不要自己發明

**構圖**：腳貼齊畫面**下 1/3**，上方留**約 1/4–1/3 的背景**；人物置中或落在三分線。

**顯腿長的站姿定番**（這一組是有效的，不要自己想別的）：
- **一腳自然往前伸出**
- **重心往後腳偏移**
- **一手插腰**（或撥髮）平衡身體
- 身體 3/4 側向鏡頭，不要正面站得直挺挺

#### 22-D. 表情與姿勢要寫成「同一個連續動作」，不要分兩段

pilot v2 的 Yuna 之所以「動作和表情很不一致」，是因為我把
`EXPRESSION: 回眸一笑` 和 `POSE: 走路被叫住回頭` 寫成**兩個獨立段落**，
模型各吃一半，拼出一個正面站著抬腳、卻面無表情的奇怪組合。

**寫法要改成一句話裡的因果關係**：

```
❌ EXPRESSION: 回眸一笑。POSE: 走路被叫住，重心在後腳……
✅ 她站定、一腳往前伸、重心壓在後腳、一手插腰，
   側身 3/4 朝鏡頭，另一手把頭髮撥到耳後的同時轉頭看向鏡頭並笑了出來
```

**並且：表情要跟姿勢相容。**「回眸」需要身體背對，
「顯腿長站姿」需要身體 3/4 朝前——硬湊兩者會互相打架。
**選一個跟姿勢自然相容的表情。**


---

### 23. 表情必須綁在一個實體動作上，純臉部的描述模型不執行（2026-08-27 實測）

**這是第 20 點的關鍵補充，也是目前為止對表情最有用的一條。**

第 20 點說「表情要先有名字」——那個方向是對的，但不夠。
實測 5 次之後，成功與失敗的分界線非常乾淨，而且**跟寫得細不細無關**：

| 表情 | 有沒有實體動作可掛 | 結果 |
|---|---|---|
| 比 V 手勢 | ✅ 手 | **成功** |
| 雙手捧杯遮住嘴 ＋ 眨眼 | ✅ 杯子 | **成功** |
| 回眸一笑（眼睛彎成月牙、嘴唇微開） | ❌ 純臉部 | 失敗——生出平靜表情 |
| 單眼瞇起 ＋ 嘴巴微張 ooh | ❌ 純臉部 | 失敗——生出平靜表情 |

> **規律：表情做不做得出來，取決於它有沒有一個實體動作可以掛。**
> 不是寫得夠不夠細，也不是身體連動寫得夠不夠多。

**還有一個必須分清楚的區別**：**身體姿勢做得出來，臉部表情做不出來。**
測試 D 組要求「側身回眸」——**身體的扭轉完整做出來了**，
但同一句要求的「笑到眼睛彎」**沒有做出來**。
所以問題不在姿勢層，只在臉部層。

#### 改寫規則：純臉部 → 加一個物件或手勢

| 原本（純臉部，無效） | 改成（綁物件／手勢） |
|---|---|
| 回眸一笑 | 回頭時**用手把被風吹亂的頭髮撥開**，笑到眼睛彎 |
| 上目遣い | **雙手捧著杯子擋在下巴前**，只露出眼睛往上看 |
| 鼓臉頰 | **咬著吸管**鼓起臉頰 |
| 嘟嘴 | **對著鏡子塗唇釉**時嘟起嘴 |
| 憋笑破功 | **用手背抵著嘴**忍住笑 |
| 驚訝張嘴 | **手摀住嘴**、眼睛睜大 |
| 挑眉微笑 | **手撐著下巴**挑起一邊眉毛 |
| 假裝生氣 | **雙手叉腰**＋嘟嘴，眼睛在笑 |

#### 表情庫重新分級

**可以直接用（本來就綁著動作）**
比 V／摀嘴笑／雙手托腮／手比小愛心／撥髮回眸／抓裙襬轉圈／手遮陽光瞇眼笑／
邊吃邊瞪大眼／歪頭笑（頭部動作，屬姿勢層）／側身回眸（身體，已實測成功）

**要照上表改寫才能用**
回眸一笑／上目遣い／鼓臉頰／嘟嘴／憋笑破功／驚訝張嘴／挑眉微笑／假裝生氣

**還沒驗過**
吐舌／單獨的眨眼／閉眼享受（寫的時候一定要把「在享受什麼」的那個物件寫出來）

#### 順帶：否定句實測確認無效

同一輪測試裡寫了 `no open sky`、`no distant vanishing point`——**兩句都被完全無視**。
`soul_2` 沒有 negative prompt 欄位，這件事現在是**實測結果**，不再是推論。

**要排除什麼，一律改成正面描述那個位置應該有什麼：**

| ❌ 否定（無效） | ✅ 正向（實測有效） |
|---|---|
| `no blown-out highlights` | `background exposed the same brightness as her skin` |
| `no open sky in frame` | （文字無效，改用換場景或參考圖） |

---

### 24. 每段 prompt 都要寫明髮長，而且成品要先驗瑕疵再評內容（2026-08-27 實測）

#### 24-A：沒寫髮長，就會生出一邊長一邊短

Luna 的測試圖被使用者一眼看出頭髮不對——**設定是及下巴的鮑伯，
生出來卻是一邊到肩、另一邊有一撮長到腰。**

根因很單純：**那段 prompt 裡完全沒有提到頭髮。**
模型沒有髮型指令，就自己拼了一個長短不一的出來。

> **規則：每一段 prompt 都必須寫出髮長。**
> 不能只寫「側分」「別到耳後」「戴髮箍」——那些是**造型**，不是**長度**。
> 沒有長度，模型會自己決定，而且會決定得不一致。

**⚠️ 2026-08-27 二次修正：`symmetrical`（視覺對稱）改成 `cut evenly at the jawline`（剪裁長度）。**

外部覆核指出：`symmetrical` 描述的是**畫面上的視覺結果**，會跟刻意不對稱的造型互相打架——
一側壓扁、一側塞耳後、濕髮貼臉，這些都不是剪得不對稱，是**造型**不對稱。
硬加 `symmetrical` 等於逼模型在「左右要對稱」與「一側要塞耳後」之間二選一。

| | 寫法 |
|---|---|
| **底層剪裁**（每件都要） | `a blunt chin-length black bob cut evenly at the jawline` |
| **頭髮自然垂放時再加** | `balanced evenly on both sides` |
| **造型本身不對稱時** | 只用底層，然後照常寫造型（塞耳後／壓扁／濕髮／半盤起） |

**「造型」不等於「長度」——這是最容易漏的一條。**
`low ponytail`、`claw clip`、`low bun`、`髮箍`、`側分` **全部都不算長度**：
低馬尾可以是及肩也可以是及腰。每段一定要有真正的長度詞
（`collarbone-length`／`chin-length`／`shoulder-length`…）。

> ⚠️ **`cut evenly at the jawline` 這個修法還沒被驗證過。**
> 下一次生 Luna 的第一張要專門看這一項，而且要挑**看得到整顆頭輪廓**的景別
> （近景看不出兩側輪廓，測不出來）。

**檢查方式**（本檔的自動檢查器出過假陰性，所以連檢查器也要驗）：
比對時**大小寫要不分**——`Chin-length` 開頭在句首會被大小寫敏感的規則漏掉。
這次寫檢查器就又踩了一次同樣的坑。

#### 24-B：成品要先驗瑕疵，再評「有沒有照規格做」

這次的教訓不只是漏寫髮長，**更嚴重的是我看了那張圖、逐項評了分，卻沒看出頭髮的瑕疵。**
我評的是「規格有沒有被執行」，完全沒有評「這張圖本身有沒有壞掉」。

**往後每張成品分兩段看，順序不能反：**

**第一段——瑕疵掃描，分三級（2026-08-27 外部覆核後修正，原本的「中一項就淘汰」太粗）**

> 舊版把「遠景招牌字亂碼」跟「多一隻手」放同一級，
> 會淘汰掉一堆人物、姿勢、服裝其實都很成功的圖。

**A 級｜Hard Reject——中一項就淘汰，不進評分**

| 檢查 | 看什麼 |
|---|---|
| 手的數量與手指 | 多手／少手；多指、少指、融合、長度異常 |
| 四肢 | 手臂腿的數量與關節方向 |
| 手與道具錯接 | 穿模、半透明、憑空接續、握法不可能 |
| **臉部結構完整** | 五官有沒有異常扭曲、崩壞。**不是「臉部對稱」**——真人臉本來就不對稱，歪頭、四分之三臉、單邊嘴角上揚都會讓畫面不對稱 |
| identity 漂移 | 明顯變成另一個人 |
| **髮長／剪裁漂移** | **不是「兩側對稱」**——歪頭、塞耳後、濕髮貼臉、半盤起，本來就不該左右等長。要擋的是**剪裁長度跑掉**：鮑伯一側到下巴、另一側突然到肩或腰；該及鎖骨的一側長到腰 |
| 衣物不可能結構 | 領口、袖口、腰帶接不起來 |
| 主要道具缺失或變形到不可辨識 | 那件 spec 的掛載動作所依賴的東西 |

**B 級｜Conditional Reject——看這張圖的驗收點是什麼**

背景人物輕微異常｜遠景招牌／菜單／路線圖是亂碼｜次要單品掉失｜頭髮少量不對稱

> **文字只有在這三種情況才是 Hard Reject**：
> ①文字本身是這張圖的主題　②客戶需要讀出特定文字　③錯字會造成錯國家／錯品牌／法律風險。
> 其餘遠景 pseudo-text 一律 B 或 C 級——
> 要求所有背景文字都像排版一樣正確，會淘汰掉大量其實成功的圖。

**C 級｜Soft Defect——記錄但照常進評分**

背景 pseudo-text｜少一件小飾品｜顆粒強弱差異｜次要擺件不完全一致

**第二段——才是規格達成度**（身分／姿勢／表情／場景／服裝各 0–2 分）

> **一張規格全中但頭髮壞掉的圖，是不能發的圖。**
> 先前的評分表少了這一段，等於預設「模型不會出瑕疵」——這個假設是錯的。

---

### 25. 送生成前的 Prompt Preflight Lint（2026-08-27，外部覆核後建立）

外部覆核指出：目前缺一個**送出前的機械檢查**，很多錯誤是可以在花錢之前就抓到的。
每一段 prompt 寫完都跑這 10 項，全過才送。

| # | 檢查 | 為什麼 |
|---|---|---|
| 1 | **這張圖需要幾隻手？含拿自拍手機的那隻，是否 ≤ 2？** | 曾寫出「一手指標牌＋一手摀嘴＋還要拿自拍手機」= 三隻手 |
| 2 | **自拍手機是否又被要求出現在畫面裡？** | 手機是相機就不可能同時在她臉旁；除非是 mirror selfie |
| 3 | **spec 的表情／姿勢是否真的出現在英文 prompt 裡？** | 曾發生規格寫「雙手托腮」、prompt 卻寫成「雙手捧拿鐵」的 drift |
| 4 | **是否只描述一個 frozen 表情？** | 搜尋 `then`／`breaking into`／`just starting to`／「下一秒」／「忍不住開始」。兩個時間點是影片寫法 |
| 5 | **動態衣物／髮絲是否寫成畫面中的位置，而不是抽象的「正在飄」？** | `fluttering in the breeze` 3/3 失敗；要寫成「衣襬被吹離身體、朝一側懸空」 |
| 6 | **髮長是否有明確的幾何描述？** | 只寫「側分」「戴髮箍」不算。短髮還要寫輪廓（`ending evenly at the jawline`） |
| 7 | **主要服裝是否 ≤ 3–4 件，最不能錯的排在前面？** | 長 prompt 尾端容易掉；**排序依「不能錯的重要度」，不是上衣→下身→鞋→飾品的固定順序** |
| 8 | **`visible pores` 是否只留在真的看得到臉部細節的景別？** | 全身圖的臉部像素撐不起毛孔，寫了只是稀釋尾段權重 |
| 9 | **機位高度／視線／頭部朝向三者是否一致？** | 曾寫出「機位在她坐姿的眼睛高度」＋「往上看鏡頭」互相打架 |
| 10 | **一段 prompt 的產出張數，是否等於 spec 宣告的景別數？** | 曾出現 spec 寫「全身＋半身各一」但只有一段 prompt |

#### 額外兩條體質性的提醒

- **鏡中反射的構圖，要預設拍攝設備可能入鏡。**`soul_2` 沒有 negative 欄位，
  不可能穩定地把相機／手機從鏡子裡消掉。**要嘛接受，要嘛不要用鏡面構圖**——
  不要期待 prompt 能解決。
- **回眸類姿勢要寫死骨盆與軀幹的朝向**（`her hips and torso facing away from the camera
  while her head and shoulders turn back`），否則模型會把整個人轉正。

#### ⚠️ 檢查器本身也要驗

本檔的自動檢查器已經出過**四次假陰性**。往後寫檢查腳本一律：
正規表達式加 `re.I`、**先用一組已知正確與一組已知錯誤的樣本各跑一次**，確認檢查器會過也會擋，才拿來檢查正式內容。

---

### 26. 覆核流程：機械檢查 → 語意覆核 → 付費 preflight → 放行批次（2026-08-27）

外部覆核連續兩輪都在同一個地方抓到問題：**我把「機械檢查全過」當成「可以送生成」。**
兩輪各出現一次 false pass：

| 輪次 | 我宣稱 | 實際 | 根因 |
|---|---|---|---|
| R1 | 髮長 21/21 | 18/21 | 腳本把 `low ponytail`／`claw clip`／`low bun` 當成有髮長，**但第 24 點自己寫著造型不算長度**——腳本執行的規則跟文件寫的規則不一樣 |
| R1 | 鮑伯幾何 11/11 | 9/11 | 腳本裡有一個 `half-pinned` 豁免，但**報告時沒有揭露**，等於灌水 |

**所以流程要分成四段，前一段過不代表可以跳到後一段：**

| 段 | 誰做 | 抓什麼 |
|---|---|---|
| **① 機械檢查** | `tools/prompt_lint.py` | 字數、否定句、髮長 token、pores 分級、時間序列詞、抽象飄動詞 |
| **② 語意覆核** | 人 ／ 另一個模型 | 這張圖需要幾隻手、機位與視線是否衝突、髮型基礎幾何與造型是否打架、**spec 與 prompt 是不是同一張圖** |
| **③ 付費 preflight** | 3–4 張 | 風險最高、一旦錯會浪費整批的項目 |
| **④ 放行批次** | — | preflight 過了才送其餘 |

**② 是 regex 永遠做不到的**，不要期待腳本代替它。

#### 檢查器自己的規矩

- 一律加 `re.I`
- **內建 `--selftest`：known-good 與 known-bad 樣本各一組**，證明它會過也會擋，才拿去檢查正式內容
- **報告時要揭露豁免**。有豁免就寫「9/11 ＋ 2 件豁免」，不要寫 11/11
- 件數分類要對總數（21 = 17 + 4），加進檢查清單

#### 另一條 production 原則（外部覆核建議直接寫進 SOP）

> **Validated baseline by default，只有當場景需求明確衝突時才做局部 override。**

已經用 credits 驗證過的字串，不要因為新寫法「聽起來比較好」就整批替換。
但也**不要把它升格成 magic string**——目前只證明「它與成功結果一起出現」，
沒有證明「正是它、而且只有它造成成功」。文件裡一律標為
**validated baseline wording**，不是 universally proven formula。

---

### 27. 手部可見性計畫與服裝辨識結構（2026-08-28 外部覆核後建立）

實測 14 張的兩個集中失敗處：**手／道具 hard defect 21%、服裝漂移 50%。**
覆核判定：現有檢查清單只管「手數 ≤2」與「服裝件數與排序」，
**沒有管「每隻手在畫面裡該不該出現、會不會被遮住」與「品名是否足以區分常見替代品」。**

#### 27-A 手部可見性計畫（每段 prompt 都要做）

**不要**升格成「兩隻手都必須有任務」——那是錯的。
A1／A2 只指派一隻手也正常；而硬逼每隻手都拿東西會增加關節、接觸物與語意關係，
**反而提高穿模、多指與第三隻手的風險。**

**正確做法是先把左右手各分類成三種之一：**

| 類 | 寫法 |
|---|---|
| ① **可見且有任務** | 逐一寫明：哪隻手、接觸部位、握法、相對位置 |
| ② **可見但只需休息位置** | `her free arm relaxed at her side`、`her other hand resting on the counter`——**單純位置就好，不要另外找事做** |
| ③ **依景別自然不入鏡** | 不必描述。臉部特寫用正向構圖 `tight close-up cropped at the shoulders` 交代即可 |

**為什麼要有 ②**：LG-10A 的靜態版兩手都沒指派，模型**自行補了雙手叉腰**（prompt 完全沒要求），
於是舉蘋果糖的手變成第三隻。**空手不是多手的充分條件，但它是風險因子。**

#### 27-B 遮擋衝突（硬檢查）

> **任何被衣袖、披肩或畫面裁切遮住的手，不得同時被指派握主要道具。**

LG-05 就是這樣爆的：`cardigan over her shoulders` 被生成成穿進袖子、左手被吃掉，
於是那把該被握住的傘**浮在空中**。

#### 27-C 服裝：標準品名 ＋ 2–3 個可見結構特徵

**不要**用純結構描述取代品名。品名負責叫出模型既有的整體概念，
少量結構詞負責鎖住最不能錯的視覺差異。只寫 `wrap robe` 而拿掉 `yukata`，
可能被解成浴袍或一般長袍；**結構詞越多也不等於控制越強，反而稀釋主體。**

| 高風險服裝 | 實測的退化方向 | 寫法 |
|---|---|---|
| 浴衣 | → 上下兩件式長褲 | `a pale-blue floral Japanese yukata, an ankle-length wrap robe with the left panel crossed over the right, a wide flat navy obi sash, wooden geta` |
| 迷你裙 | → 短褲（**3/3**） | `a pleated A-line mini skirt forming one continuous hem around her thighs`（**continuous hem 是與短褲的關鍵區隔**） |
| 透明外層 | → 整件消失 | `a long sheer overshirt worn open over the tee, both front panels visible down to mid-thigh` |

**方法**：先寫下「這件最容易退化成什麼」，再加**一個正向可見特徵**去區隔它。

#### 27-D 送生成前新增的檢查項

1. **手部可見性計畫**——左／右手各屬 ①②③ 哪一類
2. **手—道具接觸幾何**——主要道具是否寫明哪隻手、接觸部位、握法、相對位置；手部任務總數 ≤2
3. **遮擋衝突**——披肩／長袖／袖口／裁切是否會遮住被指派握道具的手
4. **靜態姿勢的空手位置**——兩手都入鏡時，沒拿道具的手是否有一個簡單休息位置
5. **高風險服裝標記**——是否用「品名＋2–3 個可見結構特徵」，且結構彼此不衝突
6. **替代剪影檢查**——是否寫明最容易退化成什麼，並加了一個正向特徵區隔
7. **景別可驗收性**——構圖是否真的看得到要驗收的腰帶、裙襬、鞋或雙手；**看不到就不能拿那張驗證服裝完整度**
8. **雙張分流規則**——見第 21 點

> 第 1–7 項是**語意檢查，regex 做不到**，必須人工或另一個模型看。
> `tools/prompt_lint.py` 只負責字串型檢查。

---

### 28. 硬驗收 vs soft observation（2026-08-28 外部覆核後建立）

#### 28-A 錨點做什麼、不做什麼

先前寫的是「表情要綁實體動作」，後來一度寫成「錨點**保證**手與物件的位置」。
**「保證」這個詞過度了**——反例是現成的：
LG-05 寫了傘卻**浮在空中**、LG-04 寫了花瓣卻**手心是空的**。

> **正確說法：實體錨點會提高「巨觀手勢與手—物件關係」的成功率，
> 但不保證那個關係一定成立，更不會連帶保證眼型、嘴型或臉頰形變。**

LG-08 是最清楚的證據：毛巾確實在手上、在臉旁（巨觀動作成立），
但同一句要求的**咬與鼓臉頰兩張全失敗**。

#### 28-B 每件 spec 都要分出硬驗收與 soft observation

| | 只能放什麼 |
|---|---|
| **硬驗收**（沒做到就淘汰） | 可見的**身體動作**、**頭部朝向**、**手—物件接觸**、**構圖**、**服裝結構**、**髮長與剪裁** |
| **soft observation**（記錄但不淘汰） | 眼型、嘴型、眉毛、臉頰形變 |

**降為 soft 的詞類**（稽核時機械搜尋這些，再人工判斷）：

```
wink / 單眼閉合｜eyes crinkled / widened / squeezed shut / narrowed
pursed lips｜small O mouth｜mouth softly open｜咬｜cheeks puffed 鼓臉頰
one eyebrow / eyebrows raised｜one corner of her mouth 單邊嘴角
nose scrunched｜mid-yawn｜mid-chew｜bored flat gaze
```

**這些字不必從 prompt 刪掉**——留著當 soft cue 無害，
**但不能拿它們當淘汰依據。**

#### 28-C 自相矛盾的陷阱

覆核指出一個我差點犯的錯：**剛把眼／嘴細節降級，
馬上又想用另一個眼部細節（`eyes crinkled shut`，只成功過 1 次）當硬門檻。**

> **n=1 只證明「曾經做得到」，不證明在另一個角色／場景／動作下有可靠成功率。**
> 別在同一份文件裡一邊降級一邊升格。

#### 28-D 2026-08-28 稽核結果

21 件裡有 **12 件**的 prompt 含上列詞類，**全部已在「表情」欄標註硬驗收是哪個巨觀動作**，
臉部細節一律註明列 soft observation。
