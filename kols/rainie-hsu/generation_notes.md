# Rainie Hsu — AI 生成規劃

> **狀態：PENDING（尚未執行）**
> 本文件是生成前的規劃文件，不是生產記錄。目前尚未進行任何訓練圖生成、Soul 訓練或影片生成。
> 所有 soul_id、job ID、圖片張數、完成日期等欄位待實際生成後才會填入 —— 本文件中不包含任何一項，也不應在生成完成前臆造。

---

## 人物設定

| 欄位 | 設定 | 狀態 |
|------|------|------|
| 名字 | Rainie Hsu（許雷妮） | — |
| 年齡 | 24 歲 | — |
| 國籍 | 台灣 | — |
| 臉型 | 五官立體深邃，高顴骨、下顎線分明、眉型有雕塑感，整體讀起來是美豔動人、讓全場回頭的驚艷等級，**不是**銳利冷硬或稜角過重的「訓練感」臉。招牌是精緻貓眼眼線妝，唇色永遠正紅或深色調 | — |
| 身材 | 94-59-92cm，F 罩杯，明顯沙漏型——胸型飽滿突出、腰線收緊、臀型有曲線，165cm，很適合貼身洋裝和馬甲上衣 | — |
| 穿衣風格 | Glam nightlife：貼身洋裝、馬甲上衣、大腿高衩裙、going-out set、高跟鞋、誇張配飾 | — |
| 眼鏡 | 無 | — |
| 髮型 | 黑色長直髮，油亮順滑，偶爾深中分或全部往後梳，出門前定裝時最俐落 | — |
| Soul 訓練 | **PENDING — 尚未開始** | 待執行 |
| 訓練圖張數 | **PENDING — 尚未生成任何圖片** | 待執行 |
| 生成日期 | **PENDING — 無** | 待執行 |

**⚠️ 生成一致性注意**：她的核心視覺特徵是「美豔動人的戲劇性 glam」，銳利立體是五官輪廓，不是表情或畫質的冷硬/劣化。任何批次的 prompt 都必須維持：(1) 大而有神、非瞇眼/非冷硬的眼睛描述，(2) 三圍數字（94-59-92cm，F 罩杯）直接寫入，不要只用形容詞帶過，(3) 化妝台暖光／夜店霓虹／鏡前定裝這類戲劇性、有目的的燈光可以繼續保留（這是她的身分核心），但必須同時明確加上 crisp / high dynamic range / high production value 等字眼，不能讀起來像「刻意做舊、調暗、調糊」。詳見下方 2026-07-25 校準記錄。

---

## 核心 Prompt 結構

> 以下為規劃中的基礎 prompt 字串，供實際生成時套用。所有描述皆為純外觀特徵，不引用任何真實名人或藝人作為臉型參考。

```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, the kind of face that stops a room when she walks in, high cheekbones, sculpted defined jawline, large striking dark eyes (NOT narrow, sleepy, or harsh/masculine) made dramatic by precise winged cat-eye eyeliner, sculpted brow, bold red or dark statement lip color, glossy jet-black long straight hair, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, deliberate confident posture always aware of how the outfit sits, [SCENE], wearing [FULLY STYLED, COLOR-COORDINATED OUTFIT — a specific going-out piece, nothing generic or accidental], [STATEMENT ACCESSORY — specific jewelry / bag / heels named], [POSE — direct "I know you're watching" gaze at camera for glam beats, or a dynamic natural candid moment for off-duty beats], [LIGHTING — see lighting notes below], high contrast saturated tones with cool undertone and warm skin highlight, crisp sharp focus, high dynamic range, high-production-value editorial nightlife photography, dramatic and moody where the scene calls for it but NEVER degraded, muddy, dim, or grainy, shot on 35mm, Instagram style
```

**風格關鍵詞備註**：
- 光線要「有目的」，但「有目的」不等於「畫質差」——化妝台暖黃燈泡光、浴室鏡燈、夜店霓虹光、手機閃光燈感這些**戲劇性、高對比的光源**要繼續保留，這是她的視覺身分核心，不需要改成柔和夢幻的自然光濾鏡；但每個 prompt 都要同時明確加上 `crisp sharp focus` / `high dynamic range` / `high-production-value` 等字眼，並避免疊加 `sensor noise`、`autofocus hunting`、`faint JPEG compression artifacts`、`film grain` 這類讀起來像「刻意做舊/畫質故障」的裝置破綻詞——真實感用 `slight motion blur`、`natural highlight clipping` 這類輕微、自然的痕跡就夠了
- 身材數字（94-59-92cm，F 罩杯）要直接寫進 prompt 本體，不要只用「striking hourglass figure」這種形容詞帶過
- 禁止關鍵詞：`soft dreamy filter`、`bare-faced natural look`、`messy unkempt`（除了宿醉恢復場景外皆不適用）、以及任何讓眼睛讀起來 narrow / sleepy / harsh / cold 的形容詞——她的眼睛要是 large and striking，不是瞇眼或冷硬
- 直視鏡頭時要帶「我知道你在看」的自覺眼神，不是意外被拍到的隨性感——這是換裝、化妝、夜店等 **glam 支柱**的招牌鏡頭語言，維持不變
- **非 glam 支柱**（完全耍廢的休息日、家人時光、深夜烘焙等，跟她的張揚人設形成刻意反差的內容）改用討喜自然光邏輯：自然窗光／黃金時段光、淺景深背景虛化、crisp high dynamic range，**不要**套用化妝台/夜店那套戲劇性光源配方——這幾個支柱的重點就是「跟出門版本判若兩人」的反差感，戲劇燈光會削弱這個反差；姿勢也可以換成自然動態抓拍，不需要每張都直視鏡頭

**⚠️ 2026-07-25 燈光/身材數字校準**：

Vicky Lin 三輪修正後確認的根本原則——「降低 AI 感」不等於「刻意做舊、調暗、調糊」——同樣適用於 Rainie，但修法方向不同：Vicky 是「自然系」人設，全面改用自然光；Rainie 的核心身分就是「刻意、戲劇性的燈光」（化妝台暖光、夜店霓虹、鏡前定裝），這個身分設定本身沒有錯，不能拿掉，也不該被「自然光才是真實」這個結論誤套用。這次修正的重點：

1. 把原本每個批次 prompt 裡疊加的 `uneven light falloff toward corners`、`visible low-light sensor noise`、`autofocus hunting`、`faint JPEG compression artifacts`、`film grain` 這類讀起來像「畫質故障／劣化」的詞全部移除或收斂，換成 `crisp sharp focus`、`high dynamic range`、`high-production-value` 等字眼——戲劇性的光源配方（暖黃燈泡、霓虹、混合色溫、手機閃光燈感）繼續保留，只是要讀起來像「高質感的夜生活雜誌／網紅拍攝」，不是「手機拍壞了」。戲劇 ≠ 劣質。
2. 三圍數字（94-59-92cm，F 罩杯）直接寫進核心 prompt 與所有批次 prompt，取代原本「striking hourglass figure with full bust, cinched waist and curved hips」這種模糊形容詞，解決身材跟人物設定數字對不上的問題。
3. 臉部描述從舊版「sharp striking facial features...defined sharp jawline」的銳利框架，改成「stunning bold glamour-model beauty...large striking dark eyes (NOT narrow, sleepy, or harsh/masculine)」——這是舊版 prompt 字串裡還沒同步更新的地方（`character.md` 早先已修正為「美豔動人，不是銳利冷硬」，但本文件的實際 prompt 字串當時沒有一起改），本次一併對齊。
4. 服裝／配件描述補上「同色系／成套／刻意搭配」與具體配飾名稱（項鍊款式、耳環、包款、鞋款），呼應她「造型永遠是刻意的、沒有將就」的人設，不再只寫「wearing [OUTFIT]」帶過。
5. 批次規劃 6（舞蹈有氧）改用「討喜自然光＋淺景深」配方——健身有氧本身是她的非 glam 支柱之一（`content_style.md` 該支柱視覺規格本來就寫「自然光、乾淨明亮」），舊版 prompt 卻套用了跟其他 glam 批次一樣的「混合不均勻＋度感雜訊」配方，這次一併修正對齊。
6. 姿勢維持她的招牌「直視鏡頭、我知道你在看」，但為非 glam 支柱（耍廢日、家人時光、深夜烘焙——目前尚未有對應批次 prompt，待之後規劃時套用本節的自然光配方）預留動態自然抓拍的空間。

---

## 計畫批次 Prompt 規劃（尚未執行）

> 以下 6 個批次為建議的訓練圖／素材拍攝規劃，供之後實際送入生成平台時使用。**目前皆未生成，無 job ID、無 media ID、無已選圖片**。每個 prompt 已依 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五項checklist（皮膚質感／拍攝裝置感／光源配方／背景生活雜物具體度／完整明確服裝）逐項套用，送出生成前仍建議對照該清單再檢查一次。**2026-07-25 已依下方校準記錄全數重寫**：批次 1–5（glam 支柱）維持戲劇性光源但補上 crisp/high-production 字眼、三圍數字直接寫入、臉部描述對齊「美豔動人非銳利冷硬」；批次 6（舞蹈有氧，非 glam 支柱）改用自然光＋淺景深配方。

### 批次規劃 1 — 浴室化妝台特寫（貓眼眼線特寫）

**場景描述**：化妝台前近景，正在畫貓眼眼線，眼神專注在鏡子細節，展現她招牌的妝容技術。檯面上散落著正在使用中的化妝品，不是乾淨擺拍的桌面。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, large striking dark eyes (NOT narrow or harsh) made dramatic by precise winged cat-eye eyeliner mid-application, eyeliner brush held close to eye, sculpted brow, bold red statement lip, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, glossy jet-black long straight hair loosely tucked behind one ear, close-up at vanity mirror, focused expression on her own reflection not at camera, wearing a thin black ribbed camisole with visible bra strap and a matching black silk robe slipping off one shoulder — deliberately coordinated loungewear, not random pieces, vanity counter cluttered with an uncapped red lipstick, scattered cotton pads, a half-empty perfume bottle, a tangled phone charger cable, a tissue box, mixed color temperature — warm tungsten vanity bulbs blending with cooler bathroom ceiling light, soft but visible shadow edges across her face, slight glare on the mirror glass, shot on iPhone 15 Pro front camera propped at the counter edge, natural highlight clipping on the vanity bulb reflections, crisp sharp focus on her face and the eyeliner brush, high dynamic range, high-production-value glam-prep editorial photo — dramatic and moody but NOT degraded, dim, or grainy, high contrast tones, candid nightlife photo, Instagram style
```

---

### 批次規劃 2 — 全身鏡前換裝定裝照

**場景描述**：全身鏡前，試穿貼身洋裝，轉身看背面剪裁，出門前最後一套的定裝時刻，直視鏡頭。鏡子周圍散落著已經試過又淘汰的衣服和鞋子。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, large striking dark eyes (NOT narrow or harsh) made dramatic by precise winged cat-eye eyeliner, bold red statement lip, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, glossy jet-black long straight hair, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, standing in front of full-length mirror turning to check the back of the dress, wearing fitted black satin bodycon dress with visible seam lines and thigh-high slit, layered gold statement necklace, strappy black ankle-tie heels, confident direct "I know you're watching" gaze at camera through mirror reflection, phone visible in the mirror at chest height, bedroom floor cluttered with two or three rejected coordinated outfits tossed on the bed, kicked-off heels near the closet, half-open closet door with empty hangers, mixed color temperature — warm apartment ceiling light blending with the cool blue glow of the phone screen, soft visible shadow under her jawline, shot on iPhone 15 Pro back camera held at chest height for a mirror selfie, natural highlight clipping from the ceiling light reflected in the mirror glass, crisp sharp focus on the dress fabric and her face, high dynamic range, high-production-value glam editorial photo — dramatic but NOT degraded, dim, or grainy, full body shot, high contrast saturated tones, candid nightlife photo, Instagram style
```

---

### 批次規劃 3 — 夜店 / 酒吧入口全身照

**場景描述**：抵達夜店或酒吧門口，全身入鏡，霓虹燈光氛圍，走進場地前的那一刻定格。入口周圍是真實街景，不是乾淨背景。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, large striking dark eyes (NOT narrow or harsh) made dramatic by precise winged cat-eye eyeliner under the neon light, bold dark statement lip, visible skin pores, subtle natural skin texture, slight oil sheen visible under the neon light, unretouched skin detail, glossy jet-black long straight hair, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, standing at a club entrance in Taipei's nightlife district about to step inside, wearing a black corset top with visible boning and high-slit satin mini skirt — a deliberately coordinated going-out set, ankle-strap statement heels, layered gold statement necklace, confident poised stance, full body shot, background shows a blurred queue of people near the door, a parked scooter at the curb, a sticker-covered lamppost, wet pavement reflecting the venue's neon sign, mixed color temperature — magenta and cyan neon spill blending with warmer sodium street lamps, slight lens flare off the neon tubing, glare on the wet pavement, shot on iPhone 15 Pro back camera taken by a friend a few steps away, natural highlight clipping around the neon signage, crisp sharp focus on her face and outfit, high dynamic range, high-production-value nightlife editorial photo — dramatic, saturated, and glossy but NOT degraded, dim, or grainy, high contrast cool-toned with warm skin highlight, candid nightlife photo, Instagram style
```

---

### 批次規劃 4 — 出門造型 Reveal（近景+全身雙版本）

**場景描述**：出門前最後一眼，鏡頭從高跟鞋帶到全身再到臉部特寫，完整的「今晚就是這套」造型揭曉時刻。玄關處堆著日常生活痕跡。此批次維持「雙版本」設計，分別提供全身版與臉部特寫版兩組 prompt。

**草稿 Prompt（版本 A — 玄關全身版）**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, large striking dark eyes (NOT narrow or harsh) made dramatic by precise winged cat-eye eyeliner, sculpted brow, bold red statement lip, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, glossy jet-black long straight hair worn sleek with deep side part, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, standing by apartment doorway ready to leave, wearing a sleek satin bodycon dress with statement drop earrings and a matching going-out bag on her shoulder, sky-high ankle-strap heels, direct confident "I know you're watching" gaze at camera, full body reveal shot, entryway cluttered with a shoe rack holding several other pairs of heels, an umbrella leaning in the corner, keys and a phone left on the entry table, a jacket on the coat hook, mixed color temperature — warm entryway bulb blending with cooler hallway light bleeding in from outside, soft glare on the small entry mirror, shot on iPhone 15 Pro back camera on self-timer propped against the shoe rack, natural highlight clipping near the doorway lamp, crisp sharp focus on her face and dress, high dynamic range, high-production-value editorial photo — dramatic but NOT degraded, dim, or grainy, high contrast saturated tones, candid nightlife photo, Instagram style
```

**草稿 Prompt（版本 B — 臉部特寫版）**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, large striking dark eyes (NOT narrow or harsh) made dramatic by precise winged cat-eye eyeliner, sculpted brow, bold red statement lip, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, glossy jet-black long straight hair worn sleek with deep side part, close-up face-to-collarbone shot at the apartment doorway, direct confident "I know you're watching" gaze at camera, statement drop earring visible in soft background bokeh, entry table faintly visible behind her with keys and a phone on it, mixed color temperature — warm entryway bulb blending with a sliver of cooler hallway light through the door gap, soft shadow across her face, glare on the golden pendant light overhead, shot on iPhone 15 Pro front camera held at a slight downward angle, natural highlight clipping on the pendant light, crisp sharp focus on her eyes and lips, high dynamic range, high-production-value glam close-up — dramatic but NOT degraded, dim, or grainy, high contrast saturated tones, candid nightlife photo, Instagram style
```

---

### 批次規劃 5 — 飯店旅遊出發前鏡前定裝（新增）

**場景描述**：飯店房間全身鏡前，準備出發去新城市的夜店，行李箱半開，落地窗外是城市夜景，出發前的興奮感。對應人物設定中「飯店 / 旅遊 — 夜生活小旅行（15%）」這個尚未有規劃批次涵蓋的內容支柱。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, large striking dark eyes (NOT narrow or harsh) made dramatic by precise winged cat-eye eyeliner, bold red statement lip, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, glossy jet-black long straight hair, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, standing in a hotel room in front of a full-length mirror, turning slightly to check the fit of the dress before heading out to a new city's nightlife, wearing a fitted metallic slip dress with thin straps and side ruching, statement drop earrings, still barefoot and holding a pair of strappy heels in one hand, city skyline visible through the floor-to-ceiling window behind her, half-open suitcase on the bed with a few coordinated outfits spilling out, a room-service tray with an empty water glass on the desk, a phone charger cable snaking across the carpet, a hotel key card on the nightstand, mixed color temperature — warm tungsten spotlight from the hotel ceiling blending with the cool blue glow of the city skyline through the window, soft glare on the window glass reflecting the room, shot on iPhone 15 Pro back camera held at chest height for a hotel mirror selfie, phone edge visible in the mirror reflection, natural highlight clipping from the hotel ceiling spotlight, crisp sharp focus on the dress and the skyline, high dynamic range, high-production-value travel-glam editorial photo — dramatic but NOT degraded, dim, or grainy, full body shot, high contrast saturated tones, candid travel-nightlife photo, Instagram style
```

---

### 批次規劃 6 — 舞蹈有氧鏡前特訓（新增）

**場景描述**：家中或工作室鏡前跳舞有氧，出汗，緊身運動服，帶著「為了今晚穿得下那件洋裝」的目的性，不是自律人設。對應人物設定中「健身 / 舞蹈有氧（10%）」這個尚未有規劃批次涵蓋的內容支柱。

> **⚠️ 2026-07-25 校準**：舞蹈有氧是她的**非 glam 支柱**之一，`content_style.md` 該支柱的視覺規格本來就寫「自然光、乾淨明亮」，舊版 prompt 卻誤套用了跟其他 glam 批次一樣的「混合不均勻＋度感雜訊」戲劇光源配方，讀起來反而不像現代健身網紅內容該有的清爽質感。本次改用 `SEXY_SCENE_LIBRARY.md` 的「討喜自然光＋淺景深」配方，跟她的 glam 支柱形成正確的反差。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, large striking dark eyes (NOT narrow or harsh), visible skin pores, subtle natural skin texture, visible sweat sheen on hairline and collarbone, slightly flushed cheeks, unretouched skin detail, natural skin imperfections, minimal or no makeup, black hair slicked back into a ponytail with a few flyaway strands from movement, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, mid-dance move in front of a studio mirror, wearing a fitted matching workout set — cropped sports bra and high-waisted leggings, dancing with clear purposeful energy rather than a disciplined-athlete pose, studio mirror slightly smudged with fingerprints, a half-full water bottle and a rolled-up yoga mat on the floor nearby, a phone propped against the wall filming, a towel draped over a chair in the corner, scuff marks visible on the studio floor, bright natural daylight spilling in from a side window mixed with soft mirror-bounced ambient light, shallow depth of field with the studio background softly blurred, crisp sharp focus on her face and movement, high dynamic range, natural color grading, high-production-value lifestyle-fitness photo — clean, bright, energetic, NOT degraded, dim, or grainy, shot on iPhone 15 Pro back camera propped on the floor against the wall for a wide mirror shot, natural motion blur on her arms and hair mid-movement, full body shot, candid photo, Instagram style
```

---

## 建議生成流程（規劃，尚未執行）

> 以下為建議流程，供實際開始生成時參考，並非已完成的步驟記錄。

1. 建議先用同一組核心 prompt 結構，於候選圖片模型（可參考 Iris Chen 案例中 Seedream 4.5 對亞洲臉孔的表現）產出上述 6 個批次的候選圖，每批次 2–4 張
2. 挑選臉部與身材一致性最佳的圖片，確認符合「美豔動人、驚艷大氣，非可愛系也非銳利冷硬」的臉型設定，以及 94-59-92cm／F 罩杯身材數字視覺上吻合後，再進入 Soul 訓練階段
3. Soul 訓練完成後才建立 soul_id，並回填至本文件；訓練前不填入任何 ID
4. 影片素材生成需等待 Soul 訓練完成，且需遵守 `content_style.md` 中訂立的燈光、角度與剪輯節奏規範

---

## 尚未執行事項清單

- [ ] 批次規劃 1–6 尚未送出生成
- [ ] 尚無 Soul 訓練、尚無 soul_id
- [ ] 尚無任何已生成圖片或影片檔案
- [ ] 尚無模型選擇的實測結論（例如 Seedream vs. 其他模型對此臉型設定的適配度）
