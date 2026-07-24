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
| 臉型 | 五官銳利立體，高顴骨、下顎線分明、眉型有雕塑感。招牌是精緻貓眼眼線妝，唇色永遠正紅或深色調 | — |
| 身材 | 明顯沙漏型——胸型飽滿、腰線收緊、臀型有曲線，165cm，很適合貼身洋裝和馬甲上衣 | — |
| 穿衣風格 | Glam nightlife：貼身洋裝、馬甲上衣、大腿高衩裙、going-out set、高跟鞋、誇張配飾 | — |
| 眼鏡 | 無 | — |
| 髮型 | 黑色長直髮，油亮順滑，偶爾深中分或全部往後梳，出門前定裝時最俐落 | — |
| Soul 訓練 | **PENDING — 尚未開始** | 待執行 |
| 訓練圖張數 | **PENDING — 尚未生成任何圖片** | 待執行 |
| 生成日期 | **PENDING — 無** | 待執行 |

---

## 核心 Prompt 結構

> 以下為規劃中的基礎 prompt 字串，供實際生成時套用。所有描述皆為純外觀特徵，不引用任何真實名人或藝人作為臉型參考。

```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, sculpted brow, precise winged cat-eye eyeliner, bold red or dark statement lip color, glossy jet-black long straight hair, striking hourglass figure with full bust, cinched waist and curved hips, deliberate confident posture, [SCENE], wearing [OUTFIT], [POSE/ANGLE], [LIGHTING], high contrast saturated tones with cool undertone and warm skin highlight, sharp not hazy, film grain, candid nightlife photo, shot on 35mm, Instagram style
```

**風格關鍵詞備註**：
- 光線要「有目的」——化妝台暖黃燈泡光、浴室鏡燈、夜店霓虹光、手機閃光燈感，避免柔和夢幻的自然光濾鏡
- 禁止關鍵詞：`soft dreamy filter`、`bare-faced natural look`、`messy unkempt`（除了宿醉恢復場景外皆不適用）
- 直視鏡頭時要帶「我知道你在看」的自覺眼神，不是意外被拍到的隨性感

---

## 計畫批次 Prompt 規劃（尚未執行）

> 以下 6 個批次為建議的訓練圖／素材拍攝規劃，供之後實際送入生成平台時使用。**目前皆未生成，無 job ID、無 media ID、無已選圖片**。每個 prompt 已依 `SEXY_SCENE_LIBRARY.md`「降低「AI 感」的技術要點」五項checklist（皮膚質感／拍攝裝置感／混合不均勻光源／背景生活雜物具體度／完整明確服裝）逐項套用，送出生成前仍建議對照該清單再檢查一次。

### 批次規劃 1 — 浴室化妝台特寫（貓眼眼線特寫）

**場景描述**：化妝台前近景，正在畫貓眼眼線，眼神專注在鏡子細節，展現她招牌的妝容技術。檯面上散落著正在使用中的化妝品，不是乾淨擺拍的桌面。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, sculpted brow, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, precise winged cat-eye eyeliner mid-application, eyeliner brush held close to eye, bold red statement lip, glossy jet-black long straight hair loosely tucked behind one ear, close-up at vanity mirror, focused expression on her own reflection not at camera, wearing thin black ribbed camisole with visible bra strap, silk robe slipping off one shoulder, vanity counter cluttered with an uncapped lipstick, scattered cotton pads, a half-empty perfume bottle, a tangled phone charger cable, a tissue box, mixed color temperature — warm tungsten vanity bulbs blending with cooler bathroom ceiling light, uneven light falloff across her face, slight hot-spot glare on the mirror glass, shot on iPhone 15 Pro front camera propped at the counter edge, faint autofocus softness on the background bottles, natural highlight clipping on the vanity bulb reflections, subtle motion blur on the eyeliner-brush hand, faint JPEG compression artifacts at high-contrast edges, high contrast tones, film grain, candid nightlife photo, Instagram style
```

---

### 批次規劃 2 — 全身鏡前換裝定裝照

**場景描述**：全身鏡前，試穿貼身洋裝，轉身看背面剪裁，出門前最後一套的定裝時刻，直視鏡頭。鏡子周圍散落著已經試過又淘汰的衣服和鞋子。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, precise winged cat-eye eyeliner, bold red statement lip, glossy jet-black long straight hair, striking hourglass figure with full bust and cinched waist, standing in front of full-length mirror turning to check the back of the dress, wearing fitted black satin bodycon dress with visible seam lines and thigh-high slit, strappy black heels, confident direct gaze at camera through mirror reflection, phone visible in the mirror at chest height, bedroom floor cluttered with two or three rejected outfits tossed on the bed, kicked-off heels near the closet, half-open closet door with empty hangers, mixed color temperature — warm apartment ceiling light blending with the cool blue glow of the phone screen, uneven light falloff toward the room corners, soft visible shadow under her jawline, shot on iPhone 15 Pro back camera held at chest height for a mirror selfie, slight autofocus softness on the dress fabric texture, natural highlight clipping from the ceiling light reflected in the mirror glass, subtle motion blur on hair mid-turn, faint JPEG compression artifacts along the mirror edge, full body shot, high contrast saturated tones, film grain, candid nightlife photo, Instagram style
```

---

### 批次規劃 3 — 夜店 / 酒吧入口全身照

**場景描述**：抵達夜店或酒吧門口，全身入鏡，霓虹燈光氛圍，走進場地前的那一刻定格。入口周圍是真實街景，不是乾淨背景。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, visible skin pores, subtle natural skin texture, slight oil sheen visible under the neon light, unretouched skin detail, natural skin imperfections, precise winged cat-eye eyeliner, bold dark statement lip, glossy jet-black long straight hair, striking hourglass figure, standing at a club entrance in Taipei's nightlife district about to step inside, wearing black corset top with visible boning and high-slit satin mini skirt, ankle-strap statement heels, layered gold necklace, confident poised stance, full body shot, background shows a blurred queue of people near the door, a parked scooter at the curb, a sticker-covered lamppost, wet pavement reflecting the venue's neon sign, mixed color temperature — magenta and cyan neon spill blending with warmer sodium street lamps, uneven light falloff leaving part of her body in soft shadow, slight lens flare off the neon tubing, faint glare on the wet pavement, shot on iPhone 15 Pro back camera taken by a friend a few steps away, slight handheld motion blur, natural highlight clipping around the neon signage, visible low-light sensor noise in shadow areas, faint JPEG compression artifacts along high-contrast neon edges, high contrast cool-toned with warm skin highlight, film grain, candid nightlife photo, Instagram style
```

---

### 批次規劃 4 — 出門造型 Reveal（近景+全身雙版本）

**場景描述**：出門前最後一眼，鏡頭從高跟鞋帶到全身再到臉部特寫，完整的「今晚就是這套」造型揭曉時刻。玄關處堆著日常生活痕跡。此批次維持「雙版本」設計，分別提供全身版與臉部特寫版兩組 prompt。

**草稿 Prompt（版本 A — 玄關全身版）**：
```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, sculpted brow, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, precise winged cat-eye eyeliner, bold red statement lip, glossy jet-black long straight hair worn sleek with deep side part, striking hourglass figure with full bust and curved hips, standing by apartment doorway ready to leave, wearing sleek satin bodycon dress with statement drop earrings and sky-high ankle-strap heels, direct confident gaze at camera, full body reveal shot, entryway cluttered with a shoe rack holding several other pairs of heels, an umbrella leaning in the corner, keys and a phone left on the entry table, a jacket on the coat hook, mixed color temperature — warm entryway bulb blending with cooler hallway light bleeding in from outside, uneven light falloff toward the door, faint glare on the small entry mirror, shot on iPhone 15 Pro back camera on self-timer propped against the shoe rack, slight autofocus hunting in the dim entryway light, natural highlight clipping near the doorway lamp, faint motion blur on the dress fabric as she turns to leave, faint JPEG compression artifacts at the shadow edges, high contrast saturated tones, film grain, candid nightlife photo, Instagram style
```

**草稿 Prompt（版本 B — 臉部特寫版）**：
```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, sculpted brow, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, natural skin imperfections, precise winged cat-eye eyeliner, bold red statement lip, glossy jet-black long straight hair worn sleek with deep side part, close-up face-to-collarbone shot at the apartment doorway, direct confident "I know you're watching" gaze at camera, statement drop earring visible in soft background bokeh, entry table faintly visible behind her with keys and a phone on it, mixed color temperature — warm entryway bulb blending with a sliver of cooler hallway light through the door gap, uneven light falloff across her face, faint glare on the golden pendant light overhead, shot on iPhone 15 Pro front camera held at a slight downward angle, close-range autofocus softness on the earring in the background bokeh, natural highlight clipping on the pendant light, faint compression noise around the sharp eyeliner edge, high contrast saturated tones, film grain, candid nightlife photo, Instagram style
```

---

### 批次規劃 5 — 飯店旅遊出發前鏡前定裝（新增）

**場景描述**：飯店房間全身鏡前，準備出發去新城市的夜店，行李箱半開，落地窗外是城市夜景，出發前的興奮感。對應人物設定中「飯店 / 旅遊 — 夜生活小旅行（15%）」這個尚未有規劃批次涵蓋的內容支柱。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, visible skin pores, subtle natural skin texture, slight oil sheen on T-zone, unretouched skin detail, precise winged cat-eye eyeliner, bold red statement lip, glossy jet-black long straight hair, striking hourglass figure with full bust and cinched waist, standing in a hotel room in front of a full-length mirror, turning slightly to check the fit of the dress before heading out to a new city's nightlife, wearing a fitted metallic slip dress with thin straps and side ruching, statement drop earrings, still barefoot and holding a pair of strappy heels in one hand, city skyline visible through the floor-to-ceiling window behind her, half-open suitcase on the bed with clothes spilling out, a room-service tray with an empty water glass on the desk, a phone charger cable snaking across the carpet, a hotel key card on the nightstand, mixed color temperature — warm tungsten spotlight from the hotel ceiling blending with the cool blue glow of the city skyline through the window, uneven light falloff across the room, faint glare on the window glass reflecting the room, shot on iPhone 15 Pro back camera held at chest height for a hotel mirror selfie, phone edge visible in the mirror reflection, slight autofocus softness on the distant window city lights, natural highlight clipping from the hotel ceiling spotlight, subtle motion blur on the dress hem mid-turn, faint JPEG compression artifacts near the bright window, full body shot, high contrast saturated tones, film grain, candid travel-nightlife photo, Instagram style
```

---

### 批次規劃 6 — 舞蹈有氧鏡前特訓（新增）

**場景描述**：家中或工作室鏡前跳舞有氧，出汗，緊身運動服，帶著「為了今晚穿得下那件洋裝」的目的性，不是自律人設。對應人物設定中「健身 / 舞蹈有氧（10%）」這個尚未有規劃批次涵蓋的內容支柱。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, visible skin pores, subtle natural skin texture, visible sweat sheen on hairline and collarbone, slightly flushed cheeks, unretouched skin detail, natural skin imperfections, black hair slicked back into a ponytail with a few flyaway strands from movement, striking hourglass figure with full bust and cinched waist, mid-dance move in front of a studio mirror, wearing a fitted matching workout set — cropped sports bra and high-waisted leggings, dancing with clear purposeful energy rather than a disciplined-athlete pose, studio mirror slightly smudged with fingerprints, a half-full water bottle and a rolled-up yoga mat on the floor nearby, a phone propped against the wall filming, a towel draped over a chair in the corner, scuff marks visible on the studio floor, mixed color temperature — cool fluorescent overhead studio lighting blending with warm daylight spilling in from a side window, uneven light falloff leaving one side of her body slightly dimmer, shot on iPhone 15 Pro back camera propped on the floor against the wall for a wide mirror shot, slight autofocus hunting as she moves quickly, natural highlight clipping from the studio ceiling lights, noticeable motion blur on her arms and hair mid-movement, faint JPEG compression artifacts around the mirror's bright reflection, full body shot, high contrast saturated tones, film grain, candid photo, Instagram style
```

---

## 建議生成流程（規劃，尚未執行）

> 以下為建議流程，供實際開始生成時參考，並非已完成的步驟記錄。

1. 建議先用同一組核心 prompt 結構，於候選圖片模型（可參考 Iris Chen 案例中 Seedream 4.5 對亞洲臉孔的表現）產出上述 6 個批次的候選圖，每批次 2–4 張
2. 挑選臉部與身材一致性最佳的圖片，確認符合「銳利立體、非可愛系」的臉型設定後，再進入 Soul 訓練階段
3. Soul 訓練完成後才建立 soul_id，並回填至本文件；訓練前不填入任何 ID
4. 影片素材生成需等待 Soul 訓練完成，且需遵守 `content_style.md` 中訂立的燈光、角度與剪輯節奏規範

---

## 尚未執行事項清單

- [ ] 批次規劃 1–6 尚未送出生成
- [ ] 尚無 Soul 訓練、尚無 soul_id
- [ ] 尚無任何已生成圖片或影片檔案
- [ ] 尚無模型選擇的實測結論（例如 Seedream vs. 其他模型對此臉型設定的適配度）
