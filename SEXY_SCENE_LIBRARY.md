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

#### 3-C. 三條硬性規則

1. **每個 `[LIGHTING]` 段落必須寫出「反射面」。** 只要寫不出「光被什麼表面反射回她臉上」，這段光線描述就不合格，退回重寫。
2. **每個 `[LIGHTING]` 段落必須寫出「哪裡被犧牲」。** 明確指定過曝的區域（`allowed to clip`、`blown out`）或壓黑的區域（`crushing to near black`、`falling into deep shadow`）。兩邊都保住＝假。
3. **禁止在光線段落使用的字**：`high dynamic range`（它的意思正好是「不犧牲任何一邊」）、`evenly lit`、`well-exposed`、`perfect lighting`、`studio lighting`（除非該張真的就是棚拍設定）。
   - **仍然要保留**畫質相關的字：`crisp sharp focus on subject`、`fine detail`、`natural colour grading`。這些管的是解析度和銳利度，不是曝光均勻度。
   - **仍然禁止**：`grainy`、`muddy`、`degraded`、`low quality`、`dim and blurry`。

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
- [ ] **（2026-08-05 改寫，最高優先）光線是否寫成「物理規格」而不是「品質形容詞」**——見上方第 3 點。逐項確認五段都寫了：① 具名主光+方向 ② **具名的反射面**（寫不出來就退回重寫）③ 兩個色溫 ④ **哪裡被犧牲**（過曝或壓黑，兩邊都保住＝假）⑤ 遮擋/框架。可直接套用 3-B 的十組配方
- [ ] **光線段落是否誤用了 `high dynamic range` / `well-exposed` / `evenly lit`**——這三個字現已禁用（它們的意思正好是「不犧牲任何一邊」）；`crisp sharp focus` / `fine detail` / `natural colour grading` 則仍要保留
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
- [ ] **（2026-08-26 新增，第 17 點）表情是否寫了不對稱（哪邊嘴角高、哪邊眉毛抬）＋ 眼神的具名焦點？** 只寫 `looking at camera` 一律退回
- [ ] **（2026-08-26 新增，第 17 點）肢體是否寫了重心在哪隻腳、兩手分別在哪、骨盆與上半身有無扭轉？** 只寫姿勢名稱（「回頭」「站著」）一律退回
- [ ] **（2026-08-26 新增，第 17 點）這套服裝有沒有至少一個「會飄的元素」，並在 prompt 裡說明它正在動？** 沒有就換裝——這是 blocking issue
- [ ] **（2026-08-26 新增，第 18 點，最高優先）主光是否打在她臉上？** 問一句「她的臉是不是畫面最亮的區域之一」——背後的光只能當輪廓光
- [ ] **（2026-08-26 新增，第 19 點）機位是否寫成離地的絕對公分數、並註明鏡頭嚴格水平？** 寫「胸口高度」而沒說是誰的胸口一律退回；嬌小角色拍全身時最容易失敗
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

### 四、Home Lounging（居家閒躺系列）20%

#### Scene L-1：沙發上的懶散，滑手機

**場景描述**：窩在沙發上，腿搭在扶手上或橫躺著，滑手機，完全不在意被拍。
**服裝**：oversized 棉T + 短褲，或細肩帶 + 短褲，光腳
**燈光**：午後客廳自然光（窗簾沒完全拉），或傍晚落地燈的暖光
**鏡頭角度**：從沙發正前方或斜前方平視，全身可見，偏側臥姿
**情緒**：完全放鬆、無聊但自在、這是她家她最隨意的樣子

```
lying on sofa with legs up over the armrest, scrolling phone held above face,
wearing oversized cotton tee and shorts, barefoot, hair loose and casual,
afternoon living room light through curtains, full body side-lying shot from in front of couch,
comfortable domestic laziness, zero performance for camera, phone screen slightly glowing
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

#### 17-A. 表情：不對稱 ＋ 眼神要有具名焦點

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

### 19. 機位高度要寫「離地公分數」，不能寫「胸口高度」（2026-08-26 新增，pilot 實測反饋）

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
