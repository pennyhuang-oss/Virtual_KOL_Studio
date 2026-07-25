# Rainie Hsu — AI 生成規劃

> **狀態：PENDING（Soul 訓練與正式訓練集尚未執行）**
> 本文件是生成前的規劃文件，不是生產記錄。2026-07-25 第一輪用 `soul_2` 生成 4 張候選圖（`round1_candidate_01`–`round1_candidate_04`，見下方「臉部/風格選角候選批次」），已被使用者否決（臉不一致＋妝容過濃）。同日改用 `seedream_v4_5` 並修正 prompt 本體妝容描述後重新生成第二輪候選圖（`candidate_01`–`candidate_03`，第 4 張因帳戶額度不足尚未生成，見下方「三次修正」章節），供使用者挑選，但**尚未**建立 Reference Element、**尚未**進行任何正式訓練圖生成、Soul 訓練或影片生成。
> soul_id、Reference Element ID、正式訓練圖 job ID／張數、Soul 訓練完成日期等欄位待實際執行後才會填入 —— 本文件中不包含任何一項，也不應在完成前臆造。

---

## 人物設定

| 欄位 | 設定 | 狀態 |
|------|------|------|
| 名字 | Rainie Hsu（許雷妮） | — |
| 年齡 | 24 歲 | — |
| 國籍 | 台灣 | — |
| 臉型 | 五官立體深邃，高顴骨、下顎線分明、眉型有雕塑感，整體讀起來是美豔動人、讓全場回頭的驚艷等級，**不是**銳利冷硬或稜角過重的「訓練感」臉。膚色是白皙透亮的瓷肌（**不是**曬黑、古銅、橄欖或深金小麥色）。妝容是 soft-glam：自然俐落的細眼線（**不是**厚重誇張的貓眼上揚甩尾），唇色是柔粉或莓果色調（**不是**正紅或深色的濃烈唇妝）——2026-07-25 已修正（見下方校準記錄），舊版「精緻貓眼眼線妝，唇色永遠正紅或深色調」的描述已淘汰 | — |
| 身材 | 94-59-92cm，F 罩杯，明顯沙漏型——胸型飽滿突出、腰線收緊、臀型有曲線，165cm，很適合貼身洋裝和馬甲上衣 | — |
| 穿衣風格 | Glam nightlife：貼身洋裝、馬甲上衣、大腿高衩裙、going-out set、高跟鞋、誇張配飾 | — |
| 眼鏡 | 無 | — |
| 髮型 | 黑色長直髮，油亮順滑，偶爾深中分或全部往後梳，出門前定裝時最俐落 | — |
| Soul 訓練 | **PENDING — 尚未開始** | 待執行 |
| 訓練圖張數 | **PENDING — 尚無正式訓練圖**（已生成 4 張選角候選圖，等待使用者挑選，見下方 2026-07-25 記錄） | 待執行 |
| 生成日期 | 選角候選圖：2026-07-25；正式訓練圖／Soul 訓練日期 **PENDING — 無** | 待執行 |

**⚠️ 生成一致性注意**：她的核心視覺特徵是「美豔動人的戲劇性 glam」，銳利立體是五官輪廓，不是表情或畫質的冷硬/劣化。任何批次的 prompt 都必須維持：(1) 大而有神、非瞇眼/非冷硬的眼睛描述，(2) 三圍數字（94-59-92cm，F 罩杯）直接寫入，不要只用形容詞帶過，(3) 化妝台暖光／夜店霓虹／鏡前定裝這類戲劇性、有目的的燈光可以繼續保留（這是她的身分核心），但必須同時明確加上 crisp / high dynamic range / high production value 等字眼，不能讀起來像「刻意做舊、調暗、調糊」。詳見下方 2026-07-25 校準記錄。

---

## 核心 Prompt 結構

> 以下為規劃中的基礎 prompt 字串，供實際生成時套用。所有描述皆為純外觀特徵，不引用任何真實名人或藝人作為臉型參考。

```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, the kind of face that stops a room when she walks in, high cheekbones, sculpted defined jawline, fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored), large striking dark eyes (NOT narrow, sleepy, or harsh/masculine) softly defined by a naturally thin eyeliner (NOT a heavy, thick, or exaggerated winged/cat-eye liner), sculpted brow, a soft rosy or berry lip tint (NOT a bold statement red/dark lip), glossy jet-black long straight hair, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, deliberate confident posture always aware of how the outfit sits, [SCENE], wearing [FULLY STYLED, COLOR-COORDINATED OUTFIT — a specific going-out piece, nothing generic or accidental], [STATEMENT ACCESSORY — specific jewelry / bag / heels named], [POSE — direct "I know you're watching" gaze at camera for glam beats, or a dynamic natural candid moment for off-duty beats], [LIGHTING — see lighting notes below], high contrast saturated tones with cool undertone and warm skin highlight, crisp sharp focus, high dynamic range, high-production-value editorial nightlife photography, dramatic and moody where the scene calls for it but NEVER degraded, muddy, dim, or grainy, shot on 35mm, Instagram style
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

### 批次規劃 1 — 浴室化妝台特寫（自然眼線特寫）

**場景描述**：化妝台前近景，正在畫自然俐落的細眼線（**不是**厚重上揚的貓眼甩尾），眼神專注在鏡子細節，展現她招牌的妝容技術。檯面上散落著正在使用中的化妝品，不是乾淨擺拍的桌面。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored), large striking dark eyes (NOT narrow or harsh) softly defined by a naturally thin eyeliner (NOT a heavy dramatic wing) mid-application, eyeliner pencil held close to eye, sculpted brow, a soft rosy or berry lip tint (NOT a bold statement red/dark lip), visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, glossy jet-black long straight hair loosely tucked behind one ear, close-up at vanity mirror, focused expression on her own reflection not at camera, wearing a thin black ribbed camisole with visible bra strap and a matching black silk robe slipping off one shoulder — deliberately coordinated loungewear, not random pieces, vanity counter cluttered with an uncapped berry-toned lipstick, scattered cotton pads, a half-empty perfume bottle, a tangled phone charger cable, a tissue box, mixed color temperature — warm tungsten vanity bulbs blending with cooler bathroom ceiling light, soft but visible shadow edges across her face, slight glare on the mirror glass, shot on iPhone 15 Pro front camera propped at the counter edge, natural highlight clipping on the vanity bulb reflections, crisp sharp focus on her face and the eyeliner brush, high dynamic range, high-production-value glam-prep editorial photo — dramatic and moody but NOT degraded, dim, or grainy, high contrast tones, candid nightlife photo, Instagram style
```

---

### 批次規劃 2 — 全身鏡前換裝定裝照

**場景描述**：全身鏡前，試穿貼身洋裝，轉身看背面剪裁，出門前最後一套的定裝時刻，直視鏡頭。鏡子周圍散落著已經試過又淘汰的衣服和鞋子。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored), large striking dark eyes (NOT narrow or harsh) softly defined by a naturally thin eyeliner (NOT a heavy dramatic wing), a soft rosy or berry lip tint (NOT a bold statement red/dark lip), visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, glossy jet-black long straight hair, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, standing in front of full-length mirror turning to check the back of the dress, wearing fitted black satin bodycon dress with visible seam lines and thigh-high slit, layered gold statement necklace, strappy black ankle-tie heels, confident direct "I know you're watching" gaze at camera through mirror reflection, phone visible in the mirror at chest height, bedroom floor cluttered with two or three rejected coordinated outfits tossed on the bed, kicked-off heels near the closet, half-open closet door with empty hangers, mixed color temperature — warm apartment ceiling light blending with the cool blue glow of the phone screen, soft visible shadow under her jawline, shot on iPhone 15 Pro back camera held at chest height for a mirror selfie, natural highlight clipping from the ceiling light reflected in the mirror glass, crisp sharp focus on the dress fabric and her face, high dynamic range, high-production-value glam editorial photo — dramatic but NOT degraded, dim, or grainy, full body shot, high contrast saturated tones, candid nightlife photo, Instagram style
```

---

### 批次規劃 3 — 夜店 / 酒吧入口全身照

**場景描述**：抵達夜店或酒吧門口，全身入鏡，霓虹燈光氛圍，走進場地前的那一刻定格。入口周圍是真實街景，不是乾淨背景。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored), large striking dark eyes (NOT narrow or harsh) softly defined by a naturally thin eyeliner (NOT a heavy dramatic wing) under the neon light, a soft rosy or berry lip tint (NOT a bold statement red/dark lip), visible skin pores, subtle natural skin texture, slight oil sheen visible under the neon light, unretouched skin detail, glossy jet-black long straight hair, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, standing at a club entrance in Taipei's nightlife district about to step inside, wearing a black corset top with visible boning and high-slit satin mini skirt — a deliberately coordinated going-out set, ankle-strap statement heels, layered gold statement necklace, confident poised stance, full body shot, background shows a blurred queue of people near the door, a parked scooter at the curb, a sticker-covered lamppost, wet pavement reflecting the venue's neon sign, mixed color temperature — magenta and cyan neon spill blending with warmer sodium street lamps, slight lens flare off the neon tubing, glare on the wet pavement, shot on iPhone 15 Pro back camera taken by a friend a few steps away, natural highlight clipping around the neon signage, crisp sharp focus on her face and outfit, high dynamic range, high-production-value nightlife editorial photo — dramatic, saturated, and glossy but NOT degraded, dim, or grainy, high contrast cool-toned with warm skin highlight, candid nightlife photo, Instagram style
```

---

### 批次規劃 4 — 出門造型 Reveal（近景+全身雙版本）

**場景描述**：出門前最後一眼，鏡頭從高跟鞋帶到全身再到臉部特寫，完整的「今晚就是這套」造型揭曉時刻。玄關處堆著日常生活痕跡。此批次維持「雙版本」設計，分別提供全身版與臉部特寫版兩組 prompt。

**草稿 Prompt（版本 A — 玄關全身版）**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored), large striking dark eyes (NOT narrow or harsh) softly defined by a naturally thin eyeliner (NOT a heavy dramatic wing), sculpted brow, a soft rosy or berry lip tint (NOT a bold statement red/dark lip), visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, glossy jet-black long straight hair worn sleek with deep side part, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, standing by apartment doorway ready to leave, wearing a sleek satin bodycon dress with statement drop earrings and a matching going-out bag on her shoulder, sky-high ankle-strap heels, direct confident "I know you're watching" gaze at camera, full body reveal shot, entryway cluttered with a shoe rack holding several other pairs of heels, an umbrella leaning in the corner, keys and a phone left on the entry table, a jacket on the coat hook, mixed color temperature — warm entryway bulb blending with cooler hallway light bleeding in from outside, soft glare on the small entry mirror, shot on iPhone 15 Pro back camera on self-timer propped against the shoe rack, natural highlight clipping near the doorway lamp, crisp sharp focus on her face and dress, high dynamic range, high-production-value editorial photo — dramatic but NOT degraded, dim, or grainy, high contrast saturated tones, candid nightlife photo, Instagram style
```

**草稿 Prompt（版本 B — 臉部特寫版）**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored), large striking dark eyes (NOT narrow or harsh) softly defined by a naturally thin eyeliner (NOT a heavy dramatic wing), sculpted brow, a soft rosy or berry lip tint (NOT a bold statement red/dark lip), visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, glossy jet-black long straight hair worn sleek with deep side part, close-up face-to-collarbone shot at the apartment doorway, direct confident "I know you're watching" gaze at camera, statement drop earring visible in soft background bokeh, entry table faintly visible behind her with keys and a phone on it, mixed color temperature — warm entryway bulb blending with a sliver of cooler hallway light through the door gap, soft shadow across her face, glare on the golden pendant light overhead, shot on iPhone 15 Pro front camera held at a slight downward angle, natural highlight clipping on the pendant light, crisp sharp focus on her eyes and lips, high dynamic range, high-production-value glam close-up — dramatic but NOT degraded, dim, or grainy, high contrast saturated tones, candid nightlife photo, Instagram style
```

---

### 批次規劃 5 — 飯店旅遊出發前鏡前定裝（新增）

**場景描述**：飯店房間全身鏡前，準備出發去新城市的夜店，行李箱半開，落地窗外是城市夜景，出發前的興奮感。對應人物設定中「飯店 / 旅遊 — 夜生活小旅行（15%）」這個尚未有規劃批次涵蓋的內容支柱。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored), large striking dark eyes (NOT narrow or harsh) softly defined by a naturally thin eyeliner (NOT a heavy dramatic wing), a soft rosy or berry lip tint (NOT a bold statement red/dark lip), visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, glossy jet-black long straight hair, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, standing in a hotel room in front of a full-length mirror, turning slightly to check the fit of the dress before heading out to a new city's nightlife, wearing a fitted metallic slip dress with thin straps and side ruching, statement drop earrings, still barefoot and holding a pair of strappy heels in one hand, city skyline visible through the floor-to-ceiling window behind her, half-open suitcase on the bed with a few coordinated outfits spilling out, a room-service tray with an empty water glass on the desk, a phone charger cable snaking across the carpet, a hotel key card on the nightstand, mixed color temperature — warm tungsten spotlight from the hotel ceiling blending with the cool blue glow of the city skyline through the window, soft glare on the window glass reflecting the room, shot on iPhone 15 Pro back camera held at chest height for a hotel mirror selfie, phone edge visible in the mirror reflection, natural highlight clipping from the hotel ceiling spotlight, crisp sharp focus on the dress and the skyline, high dynamic range, high-production-value travel-glam editorial photo — dramatic but NOT degraded, dim, or grainy, full body shot, high contrast saturated tones, candid travel-nightlife photo, Instagram style
```

---

### 批次規劃 6 — 舞蹈有氧鏡前特訓（新增）

**場景描述**：家中或工作室鏡前跳舞有氧，出汗，緊身運動服，帶著「為了今晚穿得下那件洋裝」的目的性，不是自律人設。對應人物設定中「健身 / 舞蹈有氧（10%）」這個尚未有規劃批次涵蓋的內容支柱。

> **⚠️ 2026-07-25 校準**：舞蹈有氧是她的**非 glam 支柱**之一，`content_style.md` 該支柱的視覺規格本來就寫「自然光、乾淨明亮」，舊版 prompt 卻誤套用了跟其他 glam 批次一樣的「混合不均勻＋度感雜訊」戲劇光源配方，讀起來反而不像現代健身網紅內容該有的清爽質感。本次改用 `SEXY_SCENE_LIBRARY.md` 的「討喜自然光＋淺景深」配方，跟她的 glam 支柱形成正確的反差。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, stunning bold glamour-model beauty, high cheekbones, sculpted defined jawline, fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored), large striking dark eyes (NOT narrow or harsh), visible skin pores, subtle natural skin texture, visible sweat sheen on hairline and collarbone, slightly flushed cheeks, unretouched skin detail, natural skin imperfections, minimal or no makeup, black hair slicked back into a ponytail with a few flyaway strands from movement, striking hourglass figure — 94cm full lifted bust (F cup), 59cm cinched waist, 92cm curved hips, mid-dance move in front of a studio mirror, wearing a fitted matching workout set — cropped sports bra and high-waisted leggings, dancing with clear purposeful energy rather than a disciplined-athlete pose, studio mirror slightly smudged with fingerprints, a half-full water bottle and a rolled-up yoga mat on the floor nearby, a phone propped against the wall filming, a towel draped over a chair in the corner, scuff marks visible on the studio floor, bright natural daylight spilling in from a side window mixed with soft mirror-bounced ambient light, shallow depth of field with the studio background softly blurred, crisp sharp focus on her face and movement, high dynamic range, natural color grading, high-production-value lifestyle-fitness photo — clean, bright, energetic, NOT degraded, dim, or grainy, shot on iPhone 15 Pro back camera propped on the floor against the wall for a wide mirror shot, natural motion blur on her arms and hair mid-movement, full body shot, candid photo, Instagram style
```

---

## 建議生成流程（規劃，尚未執行）

> 以下為建議流程，供實際開始生成時參考，並非已完成的步驟記錄。

1. 建議先用同一組核心 prompt 結構，於候選圖片模型（可參考 Iris Chen 案例中 Seedream 4.5 對亞洲臉孔的表現）產出上述 6 個批次的候選圖，每批次 2–4 張
2. 挑選臉部與身材一致性最佳的圖片，確認符合「美豔動人、驚艷大氣，非可愛系也非銳利冷硬」的臉型設定，以及 94-59-92cm／F 罩杯身材數字視覺上吻合後，再進入 Soul 訓練階段
3. Soul 訓練完成後才建立 soul_id，並回填至本文件；訓練前不填入任何 ID
4. 影片素材生成需等待 Soul 訓練完成，且需遵守 `content_style.md` 中訂立的燈光、角度與剪輯節奏規範

---

## 2026-07-25 臉部/風格選角候選批次 — 第一輪（Discovery Batch Round 1，⚠️ 已被使用者否決，檔案已改名為 round1_candidate_01–04.png，見下方「三次修正」章節的第二輪結果）

**狀態：⚠️ 本輪 4 張候選圖已被使用者否決 —— 四張臉不夠一致，且妝容（精緻貓眼眼線＋正紅唇色）讀起來過於濃烈/戲劇化，不符合主流審美期待。原始檔名 `candidate_01–04.png` 已改名為 `round1_candidate_01–04.png` 保留存查。尚未建立 Reference Element、尚未執行 Soul 訓練、`profile.json` 沒有 soul_id，也不會在這輪自動送訓。**

**目的**：延續 Vicky Lin 案例確立的兩階段流程——獨立生成的圖片彼此不共享身分，因此第一階段先產出一小批「候選圖」讓使用者挑出喜歡的臉／風格，確認後才對該張核准圖建立 Reference Element 錨定身分，再擴充成完整訓練集。本批次**只是**第一階段的候選圖，不是最終訓練圖，也刻意只生成 4 張（不是 8 張），純粹用於臉部/風格選角。

**模型選擇**：呼叫 `models_explore(action='recommend')`，查詢「generating consistent character reference images without soul_id」，並另外用 `models_explore(action='get', model_id='soul_2')` 確認參數。因 Rainie 尚未有 soul_id，依循 `generate_image` 工具說明「soul_2 for one-off character refs」的預設建議，並延續 Vicky Lin 案例的既有作法，採用 `soul_2`（無 soul_id，一次性角色參考圖），`aspect_ratio: 9:16`，`quality: 2k`。

**Prompt 設計**：以本文件校準後的核心 prompt 結構為基礎，四張圖的外觀描述（臉部特徵、三圍數字 94-59-92cm／F 罩杯、髮型、服裝——黑色緞面細肩帶貼身洋裝＋層次金項鍊＋金圈耳環、燈光——素色鴿灰攝影棚牆前的自然窗光混合暖色環境反射光、直視鏡頭的自覺眼神）在四張圖之間**完全相同**，僅變化鏡頭角度／景別：

| 檔名（已改名） | 角度／景別 | Job ID |
|------|-----------|--------|
| round1_candidate_01.png | 正面臉部特寫（headshot） | `29e39fae-8856-4b6d-8846-650dcc3a6bbb` |
| round1_candidate_02.png | 正面半身（half-body） | `68b88057-97f3-4cad-895e-e68b89bfad8c` |
| round1_candidate_03.png | 四分之三側半身（3/4 half-body） | `9624ce6e-f4c6-4419-888e-3a066671e006` |
| round1_candidate_04.png | 正面全身（full-body，實際出圖為正面半身偏下的裁切，未完全到腳，鏡頭指令未 100% 依照角度描述執行） | `9a6aeee7-6239-45fd-a875-fd461b6bf638` |

**費用**：`get_cost` 預估每張 1 credit（0.12 credits_exact），4 張預估共 0.48 credits。實際帳戶餘額由生成前 18.23 credits 降至生成後 16.07 credits，共減少 2.16 credits——高於本批次 4 張圖的預估花費，帳戶為共用環境，同一時段可能有其他 KOL 批次的並行生成活動，此差額不確定是否全數來自本批次，僅如實記錄觀察到的餘額變化，不臆測原因。四個 job 皆一次成功完成（`completed`），沒有卡住或重試的情形。

**產出檔案**（`kols/rainie-hsu/images/face_reference/`，共 4 張，已用 Read 工具逐張目視檢查，現已改名為 `round1_candidate_01–04.png`）：candidate_01–04 皆呈現「美豔動人、驚艷大氣」的臉型方向（非銳利冷硬），大而有神的雙眼搭配精緻貓眼眼線、正紅唇色，四張圖之間臉部特徵、髮型、服裝、配件與燈光風格判讀一致；candidate_04 的實際出圖鏡頭裁切比預期更接近半身而非到腳的全身，鏡頭指令未完全被模型遵守。

**❌ 使用者回饋（否決）**：四張臉不夠像同一個人（`soul_2` 在沒有 soul_id 錨定的情況下，每次獨立呼叫都會重新想像臉型），且妝容讀起來太濃烈/戲劇化（精緻貓眼眼線＋正紅唇色），不符合主流審美期待——兩項問題皆已於下方「三次修正」章節處理：改用 `seedream_v4_5`（同 prompt 重複生成臉型高度一致）、並修正 prompt 本體的妝容描述（本文件 `core_prompt_base` 與批次規劃 1–6 的英文 prompt 字串於本次修正時已同步更新，不再是舊版貓眼/正紅唇描述）。

**⚠️ 下一步（不可跳過）**：依照 README.md「新增 KOL 流程」與 `KOL_TRAINING_SOP.md` 的強制規則，**必須停下來，等使用者實際看過候選圖並明確指出最喜歡的一張（或說明皆不滿意需要重新調整）後，才可以進入下一階段**——下一階段流程為：(1) 將使用者核准的單一一張圖上傳並建立 Reference Element，(2) 以該 Element 錨定身分，重新生成一組完整的一致性訓練圖／素材（比照 Vicky Lin 第四輪的做法），(3) 訓練圖經確認後才呼叫 `show_characters(action='train')` 建立 soul_id。本輪（含第二輪修正批次）**沒有**建立 Reference Element，**沒有**呼叫 `show_characters(action='train')`，`profile.json` 的 `ai_generation`／soul_id 維持原狀未變更，訓練狀態明確標記為 **PENDING**。

---

## 2026-07-25 三次修正：改用 Seedream 4.5 並修正妝感 prompt 本體

**背景與根本問題**：第一輪候選批次（上方章節，`round1_candidate_01–04.png`）被使用者否決，原因有二：(1) 四張臉不夠像同一個人，(2) 妝容讀起來太濃烈/戲劇化。已排查出兩個根本原因：

1. **模型選擇錯誤**：第一輪用了 `soul_2`（無 soul_id）。`soul_2` 在沒有訓練好的 soul_id 錨定身分的情況下，每一次獨立呼叫都會重新想像一張臉，這正是本工作室在 `kols/iris-chen/generation_notes.md` 已驗證記錄的模型特性——Iris Chen 的原始 6 位 KOL 參考圖全部改用 `seedream_v4_5`（Seedream 4.5），文件明確記載「同 prompt 下生成臉型高度一致，一致到 4 張會太像，所以每批次只生成 2 張」。這是本工作室目前唯一有實證的「無 soul_id 情況下維持臉型一致」做法，`README.md`「新增 KOL 流程」步驟 5 與 `SEXY_SCENE_LIBRARY.md` checklist 已新增此規則。第一輪選 `soul_2` 是誤信了 `generate_image` 工具說明裡「soul_2 for one-off character refs」的通用建議，沒有先查本репо自己的實證紀錄。這次已改正，全數使用 `seedream_v4_5`。
2. **Prompt 本體從未真正修正**：`profile.json` 與 `character.md` 的妝容描述早先已軟化為「a naturally defined, thin eyeliner (NOT thick, heavy, or exaggerated winged liner), a soft rosy or berry lip tint (not a bold statement red/dark lip)」，但本文件（`generation_notes.md`）的 `core_prompt_base` 與批次規劃 1–6 的**實際英文 prompt 字串**當時完全沒有跟著改——`precise winged cat-eye eyeliner`、`bold red or dark statement lip color` / `bold red statement lip` / `bold dark statement lip` 這些舊字眼原封不動地重複出現在送進生成模型的 prompt 本體裡。這才是第一輪妝容讀起來依然濃烈的真正原因：character-sheet 的文字改了，但實際送進模型的 prompt 沒有改。本次已將 `core_prompt_base`（見上方「核心 Prompt 結構」）以及批次規劃 1–6 的全部草稿 prompt 逐一改為：`large striking dark eyes ... softly defined by a naturally thin eyeliner (NOT a heavy, thick, or exaggerated winged/cat-eye liner) ... a soft rosy or berry lip tint (NOT a bold statement red/dark lip)`，並在 `core_prompt_base` 本體（不只是 `profile.json`）明確加入膚色描述：`fair, luminous porcelain-toned skin (NOT tanned, bronzed, olive, or deep golden/wheat-colored)`。批次規劃 1 的場景標題與描述也一併從「貓眼眼線特寫」改為「自然眼線特寫」，避免場景概念本身還在暗示戲劇性貓眼。批次規劃 1 提及的化妝台唇膏道具也從「an uncapped red lipstick」改為「an uncapped berry-toned lipstick」以維持一致。

**模型確認**：呼叫 `models_explore(action='get', model_id='seedream_v4_5')` 確認可用——`provider_name: Bytedance`，4K 輸出，支援 `aspect_ratios` 含 `9:16`，`quality` 參數 `basic`/`high`（預設 `basic`）。

**新批次 Prompt 設計**：沿用修正後的 `core_prompt_base` 外觀描述（含新版妝容與膚色文字），四張圖的臉部特徵、三圍數字、髮型、服裝（黑色緞面細肩帶貼身洋裝＋層次金項鍊＋金圈耳環）、燈光（素色鴿灰攝影棚背景，自然窗光混合暖色環境反射光）、直視鏡頭的自覺眼神在四張圖之間**完全相同**，僅變化鏡頭角度／景別，比照第一輪的設計方式：

| 檔名 | 角度／景別 | Job ID | 狀態 |
|------|-----------|--------|------|
| candidate_01.png | 正面臉部特寫（headshot） | `8b6939d5-12cc-4a25-91c1-6dcbf107fd12` | ✅ 完成 |
| candidate_02.png | 正面半身（half-body） | `30c12337-72c8-4f93-a521-6e53ccb4ce0d` | ✅ 完成 |
| candidate_03.png | 四分之三側半身（3/4 half-body） | `ea1ac03f-a123-457d-a521-e4e534b0f875` | ✅ 完成 |
| candidate_04.png（全身，正面全身） | 未生成 | — | ❌ **未執行** |

**⚠️ 費用與帳戶餘額限制（誠實記錄，不可省略）**：`get_cost:true` 預檢每張 1 credit（`credits_exact: 1`）。前三張依序生成成功（皆為 `completed`，無卡住或重試）。第四張（全身版）呼叫時收到工作室帳戶回傳的明確錯誤：**「Out of credits in the selected workspace」**。事後查詢 `balance`：帳戶餘額僅剩 **0.35 credits**（`plan_type: ultra`），不足以支付第四張圖所需的 1 credit。因此**本批次只完成 3 張（candidate_01–03），第 4 張（全身版）尚未生成**，等待帳戶儲值/額度恢復後再補生成，不臆造第 4 張的結果。

**產出檔案**（`kols/rainie-hsu/images/face_reference/`，共 3 張，已用 Read 工具逐張目視檢查）：`candidate_01.png`、`candidate_02.png`、`candidate_03.png`。

**誠實視覺評估**：

- **臉型一致性 — ✅ 明顯改善**：三張圖之間是同一張臉——相同的臉型輪廓、眉眼距離、鼻樑、唇形、髮際線，膚色皆為白皙透亮的瓷肌（沒有曬黑/古銅感）。這證實了 Seedream 4.5 在無 soul_id 情況下、同 prompt 重複呼叫確實能維持高度臉型一致性，與 Iris Chen 案例的既有記錄相符，明顯優於第一輪 `soul_2` 產出的四張不同臉。
- **妝容 — ⚠️ 部分改善，未達完全「柔和」**：眼線比第一輪明顯收斂，不再是誇張上揚甩尾的濃厚貓眼，讀起來偏向乾淨俐落的細線；但三張圖的外眼角仍帶有一絲極輕微的上揚細尾，不是完全平貼、零上揚的自然眼線，介於「純自然」與舊版「精緻貓眼」之間，比舊版柔和很多但仍有一點點戲劇感的痕跡。唇色是飽和度偏高的莓紅/酒紅色調——技術上符合 prompt 裡「soft rosy or berry lip tint」的「berry」選項，膚色與眼線確實比第一輪柔和許多，但唇色本身仍相當濃郁飽和，一般觀眾仍可能讀成偏濃烈而非「淡雅柔和」的唇妝，還沒有完全達到「絕對不會被誤讀為 statement lip」的程度。**結論：方向正確且有實質改善（不再是明顯的厚重貓眼＋正紅唇），但如果使用者對「柔和」的要求是更接近全素顏或极淡唇彩，可能還需要再收斂一輪唇色飽和度。**

**⚠️ 下一步（不可跳過，維持既有規則）**：
1. **待使用者決定**：是否要（a）先用現有 3 張（candidate_01–03）供挑選，等帳戶額度恢復後再補第 4 張全身版；或（b）等額度恢復後一次生成完整 4 張再一起挑選。
2. 依照 README.md「新增 KOL 流程」與 `KOL_TRAINING_SOP.md` 的強制規則，**必須停下來，等使用者實際看過候選圖並明確指出最喜歡的一張（或說明妝容/臉型是否仍需調整）後，才可以進入下一階段**——下一階段流程仍為：(1) 使用者核准單一一張圖後上傳並建立 Reference Element，(2) 以該 Element 錨定身分重新生成完整訓練集，(3) 訓練圖確認後才呼叫 `show_characters(action='train')` 建立 soul_id。
3. 本輪（第二輪修正批次）**沒有**建立 Reference Element，**沒有**呼叫 `show_characters(action='train')`，`profile.json` 的 `ai_generation`／soul_id 維持原狀未變更，訓練狀態明確標記為 **PENDING**。

**⚠️ 本輪任務到此停止，等待使用者對 candidate_01–03（以及是否需要補第 4 張）給出明確回饋，不自行往下一階段推進。**

---

## 尚未執行事項清單

- [ ] 批次規劃 1–6 尚未送出生成（此為之後完整訓練集規劃，待 Reference Element 錨定後才依此重新調整生成）
- [x] 臉部/風格選角候選批次 — 第一輪（4 張，`round1_candidate_01`–`round1_candidate_04`）已生成，已被使用者否決
- [x] 臉部/風格選角候選批次 — 第二輪修正（`seedream_v4_5` + 修正妝感 prompt，`candidate_01`–`candidate_03` 已生成；`candidate_04` 因帳戶額度不足尚未生成）
- [ ] 使用者尚未挑選出核准的候選圖
- [ ] 第 4 張（全身版）候選圖因帳戶餘額僅 0.35 credits（需要 1 credit）尚未生成，待額度恢復
- [ ] 尚無 Reference Element
- [ ] 尚無 Soul 訓練、尚無 soul_id
- [ ] 尚無任何用於最終訓練集或影片生成的圖片/影片檔案
- [x] 模型選擇的實測結論：`seedream_v4_5` 在無 soul_id 情況下同 prompt 重複生成臉型高度一致，優於 `soul_2`（無 soul_id 時每次獨立想像新臉），與 Iris Chen 案例記錄相符
