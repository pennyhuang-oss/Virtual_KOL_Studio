# Vicky Lin — AI 生成規劃

> **狀態：✅ Soul 訓練已完成（`status: ready`），soul_id `bdb1d879-da36-4c1a-bc63-9f5b49a3e94e` 已可用於 `model: soul_2` 正式生成內容**
> 2026-07-25：使用者審核第四輪 Element 錨定的 12 張參考圖後回覆「可以」，明確核准進入 Soul 訓練。已完成圖片重新上傳與確認（12 個 media_id 均已 `media_confirm` 成功），但 `show_characters(action='train')` 第一次 session 連續 10 次呼叫都回傳工具層級錯誤；使用者回覆「應該是要重新試試看吧」後，第二次 session 又嘗試 2 次（`images` 用 media_id、`medias` 用 `{role,value}` 格式各一次），**仍然全部失敗**，Higgsfield 後端也**沒有建立任何角色記錄**（已用 `action='list'` 逐一核對確認）。⚠️ 兩次 session 期間累計仍被扣款約 **2.64–2.88 credits**（`transactions` 記錄為多筆 `Higgsfield Soul V2` -0.12 credits，發生在重試時段內），屬於「呼叫失敗但仍計費」的異常情形，且此模式在第二次 session 又再次重現。詳見下方「2026-07-25 使用者核准，Soul 訓練嘗試」與「2026-07-25 Soul 訓練第二次重試」兩章節。**2026-07-31 使用者要求再次測試**：沿用先前已確認的 12 個 media_id 重新呼叫 `show_characters(action='train')`，**這次第一次呼叫即成功受理**，取得 `soul_id: bdb1d879-da36-4c1a-bc63-9f5b49a3e94e`，`raw_status: queued`。判斷先前的後端 `train` 端點異常已恢復正常。詳見下方「2026-07-31 第三次重試：訓練成功送出」章節。

---

## 人物設定

| 欄位 | 設定 | 狀態 |
|------|------|------|
| 名字 | Vicky Lin（林薇淇） | — |
| 年齡 | 25 歲 | — |
| 國籍 / 出身地 | 台灣，高雄 | — |
| 臉型 | 精緻迷人的甜美臉蛋——杏眼明亮、顴骨柔和、鼻梁挺秀、笑容親和有感染力，是漂亮正妹等級的長相，**絕對不要**銳利強勢、面無表情或稜角過重的「訓練感」臉 | 純外型描述，非參考真人 |
| 身材 | 緊實有曲線的性感沙漏型——腰腹平坦、腹肌只是淡淡若隱若現，胸型飽滿、腰細、臀腿因訓練而更翹更緊實。目標是「漂亮性感的健身網紅」，**絕對不是**塊狀肌肉、血管紋理的健美選手體態 | — |
| 膚色 | 因戶外訓練而略帶古銅色，非白皙 | — |
| 髮型 | 長黑髮，訓練時綁高馬尾或編髮，休息時自然放下 | — |
| 穿衣風格 | 運動內衣、緊身高腰褲、crop tank、練後帽 T（拉鏈半開或滑落一邊肩膀） | — |
| 眼鏡 | 無 | — |
| Soul 模型 | 尚未建立——使用者已核准，但 `show_characters(action='train')` 累計兩次 session、共 12 次呼叫全部失敗（工具層級錯誤），尚無 soul_id；累計仍被扣款約 2.64–2.88 credits（見下方訓練嘗試記錄） | **PENDING（訓練已兩度嘗試但未成功，費用損耗持續累積）** |
| 訓練圖 | 第四輪 Element 錨定參考圖已生成並經使用者核准（`v4_anchored_` 開頭 12 張，見下方 2026-07-25 第四輪記錄），以使用者核准的 `v3_06_3q_fullbody.png` 為身分錨點，透過 Reference Element（element_id `9f076fab-77ef-4c68-a146-f8060253c49a`）確保 12 張圖為同一身分；已重新上傳並確認為 12 個新 media_id（見下方訓練嘗試記錄），可直接用於下次重試；第二輪、第三輪圖片因各自獨立生成、身分不一致，僅保留供對照，**不建議**用於 Soul 訓練 | **已核准，待訓練成功** |
| 已生成圖片數量 | 28（第二輪 8 張 + 第三輪 8 張〔身分不一致，僅供對照〕+ 第四輪 12 張〔Element 錨定，身分一致，已核准〕），Soul 訓練已嘗試但尚未成功啟動 | **PENDING** |
| 已生成影片數量 | 1（舞蹈克隆 R3，`dance_clone_r3`，見下方 2026-08-07 章節） | **R3 已完成** |

**⚠️ 生成一致性注意**：她的核心視覺特徵是「漂亮性感」，健身只是風味設定。任何批次的 prompt 都必須維持甜美有魅力的臉部表情、精緻不誇張的體態線條、健康小麥膚色；場景、穿搭、光線可以依批次變化，但**絕對不能**往銳利強勢的臉部表情或塊狀/血管紋理的健美選手體態靠攏——第一輪試跑（見下方）就出現過這個問題，已修正描述，之後每批生成前都要對照這條檢查。

---

## 核心 Prompt 結構（規劃草稿，未驗證）

以下為預計用於後續訓練圖 / 生活照生成的**可重複使用基礎 prompt**。全部使用純外觀描述詞，不引用任何真實藝人或公眾人物姓名。

> **⚠️ 降低「AI 感」規則**：本節與下方所有批次 prompt 都必須涵蓋 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉五項——(1) 具體皮膚質感關鍵字、(2) 逐場景明確的拍攝裝置/鏡頭與其破綻、(3) 混合不均勻光源配方、(4) 具體生活雜物細節、(5) 完整明確服裝。送出生成前用該文件的「生成前檢查清單」逐項檢查。

```
25-year-old Taiwanese woman, strikingly beautiful face, large round bright double-eyelid eyes, soft high cheekbones, straight elegant nose, full lips with a natural warm smile, standard mainstream beauty — gorgeous fitness-model good looks (NOT a stern, intense, or narrow-eyed look), toned athletic hourglass figure with soft feminine curves, 88cm bust (D cup, full and lifted), 60cm waist (flat stomach with only a subtle soft hint of ab definition, NOT blocky or vascular bodybuilder muscle), 92cm hips (rounded, lifted glutes and thighs), sun-kissed glowing skin with a natural dewy sheen, visible skin pores, subtle natural skin texture, unretouched but flattering detail, long black hair, [HAIRSTYLE], [SCENE — real aspirational location: outdoor/natural setting preferred over indoor gym mirror], wearing [FULLY EXPLICIT OUTFIT — color-coordinated matching athletic set, e.g. terracotta/sage-green/beige tones, not plain black by default], [DYNAMIC CANDID POSE — mid-motion or caught in a natural moment: mid-stretch, mid-stride, looking away, NOT a stiff posed mirror stand, NOT a bodybuilding competition stance], modern smartwatch or sunglasses as a natural accessory detail, [NATURAL FLATTERING LIGHT — golden hour sun, bright clear daylight, or dappled outdoor light; soft shallow depth of field with blurred bokeh background], shot on iPhone 15 Pro with portrait-mode background blur, crisp high dynamic range, sharp focus on subject, high production quality like a modern fitness-influencer Instagram photo — NOT degraded, grainy, or dim, natural color grading, true-to-life skin tones
```

**⚠️ 2026-07-25 二次修正**：使用者提供了實際參考截圖（風格層面，非特定真人臉部/身分模仿）分析出的規律：自然光（黃金時段/戶外強光/樹蔭斑駁光）取代之前的「刻意不完美混合室內光源」；淺景深背景虛化；同色系成套穿搭（大地色系）取代單一黑色；動態抓拍姿勢取代站定擺拍；智慧錶/墨鏡等日常配件；皮膚自然濕潤光澤而非霧面。這證實「降低AI感」不等於「畫質做舊/做差」——兩者可以並存：真實感來自皮膚質感、生活細節、自然光的「不完美但好看」，不是刻意調低整體畫質。同時把三圍數字（88-60-92，D罩杯）直接寫進 prompt，解決身材跟設定不符的問題。

**⚠️ 2026-07-24 修正記錄**：第一輪試跑（6 張參考圖）因為舊版 prompt 寫了「sharp striking features, angular jawline」+「visible muscle definition, defined core and abs」，實際生成結果變成健美選手/男性化體態，使用者明確否決，已停止並移除該批圖片，Soul 訓練未啟動。上面的 prompt 已經是修正後版本，下一輪試跑前務必再次確認符合「漂亮性感健身網紅」而非「健美選手」的方向。

**待決定事項（需在實際測試後補上結論）**：
- 使用哪個模型（Seedream / Recraft / 其他）對亞洲運動型女性身材與汗水質感還原度最好，需要實測比較
- `[HAIRSTYLE]` 依場景切換：`high ponytail pulled back tight`（訓練中）／`natural loose down`（居家、浴室、飯店）
- **不要**用「visible muscle striation」之類的詞去強化肌肉線條——這正是第一輪試跑跑偏成健美選手的原因之一，已明確排除，不列入待測試方向
- 皮膚質感關鍵字（pores / natural texture / unretouched）目前跟「淡淡若隱若現的腹肌」共存沒有問題，若之後實測發現互相打架需要再微調權重
- 避免使用會把畫面推向塑膠感的字：`smooth`、`flawless`、`glossy skin`、`airbrushed`、`porcelain skin`

---

## 計畫批次 Prompt 規劃（尚未執行）

以下 6 個批次為**規劃中的訓練圖 / 首波生活照場景**，用於之後建立 Soul 模型或直接生成生活照。批次順序、每批次張數、實際模型選擇都待執行時決定，這裡只先把場景與 prompt 草稿定下來。每個 prompt 都已依 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉的五項checklist補齊皮膚質感、拍攝裝置破綻、混合光源、生活雜物細節與完整服裝，但**仍是草稿，未經實際生成驗證**。

### 批次 1（規劃）— 健身房鏡前，訓練中全身

**場景描述**：深蹲架前或自由重量區的落地鏡前，正在準備或剛完成一組訓練，全身入鏡展示動作與身材線條，健身房日光燈或大窗自然光。

**草稿 Prompt**：
```
25-year-old Taiwanese woman, strikingly beautiful and warm face, bright almond-shaped eyes, soft high cheekbones, straight elegant nose, full lips with a natural friendly smile, gorgeous fitness-model good looks (NOT a stern or intense expression), direct confident gaze, toned athletic hourglass figure with soft feminine curves, flat stomach with only a subtle soft hint of ab definition (NOT blocky or vascular bodybuilder muscle), full chest, cinched waist, rounded lifted glutes and thighs, sun-tanned skin with visible skin pores, subtle natural skin texture, slight oil sheen on collarbones and chest, unretouched skin detail, long black hair in high tight ponytail with a few loose flyaway strands, standing in front of gym mirror near squat rack, mirror glass has faint fingerprints and dust smudges near the edges, scattered chalk dust on the rubber gym floor, a half-empty water bottle with condensation beading on it left by the rack, resistance bands hanging loosely off the rack frame, a phone charging cable coiled on the bench nearby, a gym towel draped over the corner of the rack, wearing black sports bra and high-waist fitted leggings, full body shot, confident direct gaze at mirror reflection, hard gym fluorescent overhead tubes mixed with cooler daylight spilling in from a side window, uneven light falloff across the mirror surface, slight lens flare and glare where the fluorescent tubes reflect off the glass, visible sweat sheen on skin, shot on iPhone 15 Pro rear camera held at chest height for a mirror selfie, slight autofocus hunting on the reflective mirror surface, natural highlight clipping where the overhead lights bounce in the mirror, subtle motion blur on the ponytail mid-movement, faint JPEG compression artifacts along the high-contrast mirror edge, slightly high-contrast true-to-skin color grading, film grain, candid lifestyle photo, Instagram style
```

---

### 批次 2（規劃）— 戶外訓練，黃金時段

**場景描述**：戶外空地或河濱訓練場景（高雄常見的戶外功能性訓練環境），黃昏黃金時段逆光或側光，動作中或組間喘氣的瞬間。

**草稿 Prompt**：
```
25-year-old Taiwanese woman, strikingly beautiful and warm face, bright almond-shaped eyes, soft high cheekbones, straight elegant nose, full lips with a natural friendly smile, gorgeous fitness-model good looks (NOT a stern or intense expression), toned athletic hourglass figure with soft feminine curves, flat stomach with only a subtle soft hint of ab definition (NOT blocky or vascular bodybuilder muscle), full chest, cinched waist, rounded lifted glutes and thighs, sun-tanned skin with visible skin pores, subtle natural skin texture, slight sweat sheen on the T-zone and shoulders, unretouched skin detail, long black hair in tight braid with a few flyaway strands catching the light, training outdoors on a cracked open-air concrete court, a gym bag and rolled resistance bands dropped on the ground nearby, a half-full water bottle rolling on the pavement, faint chalk marks and worn paint lines on the concrete, a couple of scooters parked at the edge of frame in the background, a sweat towel discarded on a nearby bench, wearing black crop tank and high-waist leggings, mid-action pose or catching breath between sets, warm golden-hour backlight mixed with cooler ambient bounce light off the concrete, uneven flare where direct sun edge grazes the frame, visible sweat sheen on skin, shot on iPhone 15 Pro rear camera handheld by a training partner a few steps away, slight autofocus softness on foreground dust kicked up mid-motion, natural highlight clipping around the sun's edge, subtle motion blur on hands and hair from the movement, faint compression artifacts along the high-contrast silhouette against the sky, slightly high-contrast true-to-skin color grading, film grain, candid lifestyle photo, Instagram style
```

---

### 批次 3（規劃）— 練後居家恢復

**場景描述**：高雄公寓客廳地板，練後伸展或滾筒放鬆,運動服未換,身體仍帶著訓練後的疲憊與泵感,自然居家光線。

**草稿 Prompt**：
```
25-year-old Taiwanese woman, strikingly beautiful and warm face, bright almond-shaped eyes, soft high cheekbones, straight elegant nose, full lips with a natural friendly smile, gorgeous fitness-model good looks (NOT a stern or intense expression), toned athletic hourglass figure with soft feminine curves, flat stomach with only a subtle soft hint of ab definition (NOT blocky or vascular bodybuilder muscle), full chest, cinched waist, rounded lifted glutes and thighs, sun-tanned skin with visible skin pores, subtle natural skin texture, slight oil sheen on nose and forehead, unretouched skin detail, long black hair naturally down and slightly damp at the roots from training, sitting on living room floor doing post-workout stretch, a protein shaker bottle left on the floor nearby, a phone charging cable snaking across the rug, a foam roller within reach, an oversized hoodie tossed on the couch behind her, a gym bag propped by the front door, a half-empty water bottle and the TV remote sitting on the coffee table, wrinkled throw blanket draped over the couch arm, wearing black sports bra and short shorts, oversized hoodie unzipped slipping off one shoulder nearby, relaxed tired expression, natural warm afternoon light through the apartment window mixed with the cooler glow of a floor lamp in the corner, uneven light falloff across the room, shot on iPhone front camera propped against a water bottle on the floor for a hands-free angle, slight autofocus softness as she shifts position, natural highlight clipping near the window, subtle motion blur on the arm mid-stretch, faint compression artifacts in the shadowed corner of the room, slightly high-contrast true-to-skin color grading, film grain, candid lifestyle photo, Instagram style
```

---

### 批次 4（規劃）— 賽前備賽飯店

**場景描述**：出差或賽前訓練營住宿的飯店房間，行李與比賽裝備並存,對著鏡子確認狀態或坐在床邊查看飯店健身房資訊,帶一點出差的緊繃感而非度假感。

**草稿 Prompt**：
```
25-year-old Taiwanese woman, strikingly beautiful and warm face, bright almond-shaped eyes, soft high cheekbones, straight elegant nose, full lips with a natural friendly smile, gorgeous fitness-model good looks (NOT a stern or intense expression), direct confident gaze, toned athletic hourglass figure with soft feminine curves, flat stomach with only a subtle soft hint of ab definition (NOT blocky or vascular bodybuilder muscle), full chest, cinched waist, rounded lifted glutes and thighs, sun-tanned skin with visible skin pores, subtle natural skin texture, slight oil sheen on collarbones, unretouched skin detail, long black hair in high ponytail with loose baby hairs at the temple, sitting on hotel bed with an open suitcase spilling clothes onto the floor, a competition gear bag propped against the nightstand, a phone charger cable coiled on the nightstand next to a half-empty water bottle, a room key card and hotel notepad on the desk in the background, gym shoes kicked off by the door, slightly wrinkled hotel bedsheet where she's sitting, checking phone for hotel gym hours, wearing black sports bra and leggings, focused slightly tense expression, warm bedside lamp light mixed with cooler daylight leaking through a gap in the curtains, uneven light falloff between the lamp-lit side of the bed and the dimmer far corner, shot on iPhone front camera selfie held at arm's length in dim hotel lighting, slight autofocus softness in the low light, natural highlight clipping around the bedside lamp, subtle motion blur on the hand holding the phone, faint compression artifacts in the darker shadow areas of the room, slightly high-contrast true-to-skin color grading, film grain, candid lifestyle photo, Instagram style
```

---

### 批次 5（規劃）— 早晨出門前，浴室鏡前綁頭髮

**場景描述**：高雄公寓浴室鏡前，清晨準備出門訓練，運動服已上身，正在綁高馬尾或整理髮尾，還帶點剛起床的沒睡醒感，不是刻意擺拍。對應人物設定中的「早晨」內容支柱（15%）。

**草稿 Prompt**：
```
25-year-old Taiwanese woman, strikingly beautiful and warm face, bright almond-shaped eyes, soft high cheekbones, straight elegant nose, full lips, gorgeous fitness-model good looks (NOT a stern or intense expression), straight thick eyebrows, slightly sleepy unposed gaze, toned athletic hourglass figure with soft feminine curves, flat stomach with only a subtle soft hint of ab definition (NOT blocky or vascular bodybuilder muscle), full chest, cinched waist, rounded lifted glutes and thighs, sun-tanned skin with visible skin pores, subtle natural skin texture, no makeup, faint under-eye shadow from early wake-up, unretouched skin detail, long black hair half-tied, hands mid-motion pulling hair into a high ponytail, standing in front of bathroom mirror, mirror has faint water spots and a small toothpaste smear near the edge, a cup with toothbrushes and a half-used dry shampoo bottle cluttering the counter, spare hair ties looped around the faucet handle, a gym bag leaning against the doorframe just visible in frame, a damp towel hanging on the hook behind her, wearing black sports bra and high-waist leggings already on for training, standing three-quarter angle toward the mirror, cool bathroom LED vanity light mixed with faint pale morning daylight coming through a small frosted window, uneven light falloff with a slightly greenish cast from the LED strip, shot on iPhone front camera propped against the counter edge for a hands-free angle, slight autofocus softness from the close distance, natural highlight clipping off the vanity light bulbs, subtle motion blur on the hands mid-hair-tie, faint compression artifacts near the bright mirror highlights, slightly high-contrast true-to-skin color grading, film grain, candid lifestyle photo, Instagram style
```

---

### 批次 6（規劃）— 練後浴室沖澡恢復

**場景描述**：健身房或住處浴室，練後沖澡沖掉汗水，肌肉線條在水珠下更明顯，皮膚帶點練後的紅潤，同時做冰敷或簡單恢復性動作。對應人物設定中的「浴室」內容支柱（15%），誠實呈現訓練後的真實身體狀態而非浪漫化。

**草稿 Prompt**：
```
25-year-old Taiwanese woman, strikingly beautiful and warm face, bright almond-shaped eyes, soft high cheekbones, straight elegant nose, full lips with a natural friendly smile, gorgeous fitness-model good looks (NOT a stern or intense expression), toned athletic hourglass figure with soft feminine curves, flat stomach with only a subtle soft hint of ab definition under wet skin (NOT blocky or vascular bodybuilder muscle, NOT visible striation), full chest, cinched waist, rounded lifted glutes and thighs, sun-tanned skin with visible skin pores, subtle natural skin texture, unretouched skin detail, skin slightly flushed pink from training and hot water, water droplets beaded on shoulders and collarbones, long black hair damp and slicked back from the shower, standing in bathroom or gym locker shower area holding an ice pack against one shoulder, steam fogging the edges of the mirror and tile, a shampoo bottle and bar of soap sitting on the shower ledge, a foam roller propped in the corner just outside the shower stall, a towel hanging on a hook nearby, small puddle of water on the tile floor, wearing sports bra soaked through from the shower or a plain oversized t-shirt clinging damply, honest tired post-training expression, cool bathroom LED light mixed with warm diffuse light from the shower steam, uneven light falloff with soft glare where condensation catches the light, shot on iPhone rear camera propped on the bathroom counter for a hands-free angle since her hands are occupied with the ice pack, slight autofocus softness from the fogged air, natural highlight clipping on the wet tile reflections, subtle motion blur on the water droplets and steam, faint compression artifacts along the foggy mirror edge, slightly high-contrast true-to-skin color grading, film grain, candid lifestyle photo, Instagram style
```

---

## 2026-07-25 第二輪參考圖生成記錄（已生成，等待使用者確認，尚未送入 Soul 訓練）

**狀態：⚠️ 等待使用者審核 —— 尚未執行 Soul 訓練，`profile.json` 沒有 soul_id，也不會在這輪自動送訓。**

依照本文件「2026-07-24 修正記錄」修正後的核心外型描述，重新生成了 8 張臉部參考圖，取代第一輪被否決並已刪除的 6 張圖。這次沒有再使用舊版「sharp striking features / visible muscle definition, defined core and abs」的字眼，全程使用修正後的「gorgeous fitness-model good looks, NOT a stern or intense expression」+「soft feminine curves, subtle soft hint of ab definition, NOT blocky or vascular bodybuilder muscle」語言。

**模型選擇**：呼叫 `models_explore(action='recommend')` 確認後，因她尚未有 soul_id，使用 `soul_2`（無 soul_id，作為一次性角色參考圖生成，符合 `generate_image` 工具說明中「soul_2 for one-off character refs」的預設建議），`aspect_ratio: 9:16`，`quality: 2k`。

**服裝與場景**：統一使用素色黑色貼身細肩帶運動內衣 + 高腰緊身褲，站在素色淺灰牆面前，僅以自然窗光 + 暖色環境反射光做混合光源，不同圖之間僅變化角度（正面／四分之三側／側面）與景別（特寫臉部／半身／全身），身份特徵（臉型、體態、髮型）全部保持一致。已依 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉五項逐一檢查（皮膚質感關鍵字、iPhone 15 Pro 前/後鏡頭與具體破綻、混合不均勻光源、牆面雜物質感細節、完整服裝描述），並額外檢查運動類角色專用項目（是否偏向健美選手/男性化方向）——已確認全數 8 張 prompt 都維持「漂亮性感健身網紅」方向，未使用塊狀肌肉/血管紋理/銳利強勢臉部語言。

**費用**：`get_cost` 預估每張 1 credit（0.12 credits_exact）；實際餘額由生成前 32.27 credits 降至生成後 31.31 credits，共花費 0.96 credits（8 張）。

**產出檔案**（`kols/vicky-lin/images/face_reference/`）：

| 檔名 | 角度 | 景別 | Job ID |
|------|------|------|--------|
| 01_front_headshot.png | 正面 | 臉部特寫 | `647216d3-e794-41c5-a2b4-0470ecdb5241` |
| 02_front_halfbody.png | 正面 | 半身 | `7f414bd8-671e-4de5-ad93-76ef5e72803a` |
| 03_front_fullbody.png | 正面 | 全身 | `6241eb42-4404-4863-a723-c912c19e7554` |
| 04_3q_headshot.png | 四分之三側 | 臉部特寫 | `11501236-1f64-42b0-896a-64a7165e44a2` |
| 05_3q_halfbody.png | 四分之三側 | 半身 | `84e29671-1aee-4c41-9264-c8f431c128ae` |
| 06_3q_fullbody.png | 四分之三側 | 全身 | `a702a222-6ac5-409b-a8af-8445d783050c` |
| 07_side_headshot.png | 側面 | 臉部特寫 | `59245b55-2125-4f45-af1b-9cb792d4d289` |
| 08_side_halfbody.png | 側面 | 半身 | `809f17de-9d88-4b13-bb82-c085e224a1d4` |

生成後已目視檢查數張圖（headshot、front full-body、3/4 full-body、side headshot），確認呈現的是漂亮性感健身網紅方向、表情溫暖自然、體態柔和有曲線，沒有再出現健美選手/男性化的問題。

**⚠️ 下一步（不可跳過）**：依照 README.md「新增 KOL 流程」第 6 點與 `KOL_TRAINING_SOP.md` 的強制規則，**必須停下來，等使用者實際看過這 8 張參考圖並明確確認滿意後，才可以進入 Soul 訓練**。本輪不會、也沒有呼叫 `show_characters(action='train')`，`profile.json` 的 `ai_generation`／soul_id 維持原狀未變更。

---

## 2026-07-25 第三輪參考圖生成記錄（已生成，等待使用者確認，尚未送入 Soul 訓練）

**狀態：⚠️ 等待使用者審核 —— 尚未執行 Soul 訓練，`profile.json` 沒有 soul_id，也不會在這輪自動送訓。**

**觸發原因**：使用者審核第二輪 8 張圖後回報三個新問題——(1) 臉仍不是「標準大眾審美的漂亮」，眼睛讀起來偏細長/上揚（almond-shaped 這個詞被生成模型解讀成瞇眼）；(2) 胸型跟人物設定的三圍（88-60-92，D罩杯）對不上；(3) 整體濾鏡/光線/畫質偏差、偏暗，不像現代 Instagram 健身網紅該有的質感。使用者另外提供了幾張實際健身網紅帳號的截圖，明確說明僅供**風格層面**分析（光線角度、構圖、穿搭配色），不涉及對截圖中真人臉部/身分的模仿。分析後對本文件「核心 Prompt 結構」做了 2026-07-25 二次修正（見上方該節），本輪即依照修正後版本重新生成。

**這輪相對第二輪的具體改動**：
- 眼睛描述從 `bright almond-shaped eyes` 改成 `large round bright double-eyelid eyes`，並明講 `NOT a stern, intense, or narrow-eyed look`——直接排除瞇眼/細長眼的生成傾向
- 三圍數字（88cm bust D cup、60cm waist、92cm hips）直接寫進每張圖的 prompt 本體，而不是只靠「toned athletic hourglass figure」這種形容詞帶過
- 服裝從單一素色黑色運動內衣＋緊身褲，改成同色系成套穿搭並逐張變化顏色：赤陶橘（terracotta）、鼠尾草綠（sage-green）、燕麥色（beige）、黑色都各有出現，對應使用者截圖分析出的「大地色系成套穿搭」趨勢
- 光線配方從第二輪沿用的「室內混合不均勻」邏輯，改用 `SEXY_SCENE_LIBRARY.md` 2026-07-25 修正後的「戶外/生活風格場景」配方——黃金時段斜陽或戶外強光＋淺景深背景虛化＋crisp high dynamic range，並在每張 prompt 明講 `NOT degraded, grainy, or dim`
- 場景從素色淺灰牆面前，全部改成戶外真實場景：公園慢跑道、戶外跑道、樹蔭步道、河濱步道、草坡、戶外球場，呼應人物設定「健身網紅」應有的戶外訓練內容調性
- 姿勢從站定擺拍改成動態抓拍（爬樓梯中途、伸展中、扶頭髮、看向遠方），並保留 iPhone 15 Pro 前/後鏡頭＋具體裝置破綻（對焦稍軟、高光溢出、動態模糊）與生活雜物細節（水瓶、瑜伽墊、健身包、耳機線等），確保沒有為了追求「畫面好看」而把 `SEXY_SCENE_LIBRARY.md` 五項降低 AI 感的技術要點犧牲掉

**模型選擇**：延續第二輪的方式，因她尚未有 soul_id，使用 `soul_2`（一次性角色參考圖），`aspect_ratio: 9:16`，`quality: 2k`。

**生成前逐張自我檢查**：對照 `SEXY_SCENE_LIBRARY.md` 五項降低 AI 感檢查清單（皮膚質感關鍵字、裝置/鏡頭具體破綻、對應場景類型的正確光源配方、生活雜物背景細節、完整服裝描述）＋本角色專屬檢查（大圓眼非細長眼、88-60-92/D罩杯體態、絕非健美選手、絕非畫質做舊/偏暗）——8 張 prompt 逐一確認皆符合後才送出生成。

**費用**：`get_cost` 預估每張 1 credit（0.12 credits_exact），與第二輪相同。其中第 1 張（正面臉部特寫，公園黃金時段）第一次生成的 job（`f45ed632-c2a2-45b8-afc1-5c15258bb47e`）在伺服器端卡在 `in_progress` 狀態遲遲未完成（已扣款但未出圖），判斷為單筆卡住，改用相同 prompt 重新送出一次（`5ce7e4e5-d394-485a-8660-dd991d2bd1d9`），這次正常完成並下載存檔。實際餘額由生成前 31.31 credits 降至生成後 30.23 credits，共花費 1.08 credits（8 張成功張＋1 張卡住未取得結果的重複扣款，共 9 次生成請求）。

**產出檔案**（`kols/vicky-lin/images/face_reference/`，檔名加 `v3_` 前綴以跟第二輪 8 張圖區隔，兩輪皆保留在目錄中供使用者比較）：

| 檔名 | 角度 | 景別 | 場景／穿搭色系 | Job ID |
|------|------|------|----------------|--------|
| v3_01_front_headshot.png | 正面 | 臉部特寫 | 公園慢跑道，黃金時段，赤陶橘 | `5ce7e4e5-d394-485a-8660-dd991d2bd1d9`（原始 job `f45ed632-c2a2-45b8-afc1-5c15258bb47e` 卡住未完成，已改用此重生成結果） |
| v3_02_front_halfbody.png | 正面 | 半身 | 戶外跑道，正午強光，鼠尾草綠 | `37f34802-401f-4dfe-b46d-ab883262268f` |
| v3_03_front_fullbody.png | 正面 | 全身 | 公園石階，黃金時段動態抓拍，赤陶橘 | `007c1d19-c2a8-4061-9a21-9decd4c21722` |
| v3_04_3q_headshot.png | 四分之三側 | 臉部特寫 | 樹蔭步道，斑駁光，黑色 | `4ca2ef1b-b278-4d77-9d8c-db9a69ec0223` |
| v3_05_3q_halfbody.png | 四分之三側 | 半身 | 戶外球場，正午強光，燕麥色 | `e1b56dc7-adfe-4517-a3fb-3a8182e3f831` |
| v3_06_3q_fullbody.png | 四分之三側 | 全身 | 草坡，黃金時段伸展中，鼠尾草綠 | `e7059e94-312a-4747-b338-e31b470f97cf` |
| v3_07_side_headshot.png | 側面 | 臉部特寫 | 河濱步道，日光側光，黑色 | `432e10d1-5d7a-4266-99ac-686ce976a0e1` |
| v3_08_side_halfbody.png | 側面 | 半身 | 戶外跑道草地，黃金時段伸展，鼠尾草綠 | `c0e1c4ed-b4f7-4ca2-ac38-a3922b715284` |

**生成後目視檢查**（已逐張用 Read 工具開啟檢視 v3_01、v3_02、v3_03、v3_04、v3_05、v3_06、v3_07、v3_08 全部 8 張）：眼睛均呈現大圓明亮雙眼皮，沒有再出現細長/瞇眼的問題；胸型與三圍設定（88-60-92/D罩杯）視覺上吻合，不再偏瘦或跟設定不符；整體畫面明亮清晰、有淺景深散景，看起來像現代 Instagram 健身網紅的生活照，沒有再出現偏暗/顆粒感過重/濾鏡做舊的問題；成套配色穿搭（赤陶橘、鼠尾草綠、燕麥色、黑色）每張都有完整明確描述且視覺上一致；場景全部改為戶外真實場景，動態抓拍姿勢自然不生硬；沒有再出現健美選手/男性化的問題。整體判斷：這一輪已針對使用者回報的三個問題（眼睛、胸型、畫質光線）逐項修正，且沒有為了修正而讓 5 項降低 AI 感技術要點退化。

**⚠️ 下一步（不可跳過，比第二輪多一步）**：依照 README.md「新增 KOL 流程」第 6 點與 `KOL_TRAINING_SOP.md` 的強制規則，**必須停下來，等使用者實際比較第二輪與第三輪參考圖、明確確認滿意（包含確認要採用哪一輪的圖／是否需要混用）後，才可以進入 Soul 訓練**。本輪不會、也沒有呼叫 `show_characters(action='train')`，`profile.json` 的 `ai_generation`／soul_id 維持原狀未變更，訓練狀態明確標記為 **PENDING**。

---

## 2026-07-25 第四輪：Element 錨定的一致性訓練圖（已生成，等待使用者確認，尚未送入 Soul 訓練）

**狀態：⚠️ 等待使用者審核 —— 尚未執行 Soul 訓練，`profile.json` 沒有 soul_id，也不會在這輪自動送訓。**

**觸發原因（重大技術問題）**：發現第二輪、第三輪的做法有根本性缺陷——每張圖都是獨立呼叫文字生成（無身分錨點），模型每次都會重新「想像」一個符合文字描述但**不是同一個人**的臉。8 張圖看起來都是「漂亮性感健身網紅」這個類型，但彼此的臉其實不是同一張臉，只是風格相似。如果直接把這種身分不一致的圖送進 Soul 訓練，訓練結果會是多人臉部特徵的平均/混合，而不是使用者想要的單一穩定身分。這個問題在使用者審核截圖比對後才被發現——之前兩輪的「使用者確認」都還沒到這一步。

**修正方式**：改用 Higgsfield Reference Element 機制，把使用者已經明確核准的**單一一張圖**上傳並轉成可重複使用的 Element，之後每一張新圖的 prompt 都在文字中內嵌 `<<<element_id>>>`（而不是重新用文字描述五官），讓後端把同一張參考圖直接注入生成流程，確保臉部/身形真正共享同一個身分，而不是靠文字描述「長得像」。

### 1. 核准的錨點圖片確認

使用者核准的圖片描述為：3/4 角度、半身/膝上景、左手臂完全舉高過頭、鼠尾草綠成套細肩帶運動內衣＋緊身褲、黃金時段戶外逆光、墨鏡推到馬尾上、白色智慧錶、右手插腰、站在陽光灑落的草地上、背景有樹。

**逐張核對結果**：一開始依景別分類猜測是 `v3_05_3q_halfbody.png`，實際用 Read 工具開圖比對後**不吻合**（v3_05 是燕麥色運動內衣＋短褲、站在球場圍籬前、手扶著髮辮而非舉高過頭、無墨鏡）。改為逐張檢視 `v3_02`、`v3_06`、`v3_08` 後確認：**`v3_06_3q_fullbody.png`**（草坡，黃金時段伸展中，鼠尾草綠，Job ID `e7059e94-312a-4747-b338-e31b470f97cf`）與描述完全吻合——左臂舉高過頭、鼠尾草綠成套運動內衣＋緊身褲、黃金時段逆光穿過樹梢、墨鏡推入馬尾、白色智慧錶、右手插腰、陽光草地背景有樹。雖然檔名分類是「3q_fullbody」而非使用者描述的「3/4 half-body」，但視覺內容（角度、框景範圍到大腿、姿勢、穿搭、光線、配件）逐項核對後確認就是這一張，非 v3_05。

### 2. Reference Element 建立

- 上傳流程：`media_upload`（filename `vicky_lin_v3_06_anchor.png`）→ 取得 presigned S3 URL 與 `media_id: 9077b11f-57b0-4e98-9b30-d891542ff64c` → `curl -X PUT` 上傳 `v3_06_3q_fullbody.png` 原始檔案位元組（HTTP 200）→ `media_confirm(media_id, type='image')` 確認上傳完成
- `show_reference_elements(action='create', category='character', name='vicky-lin-anchor-v3-06', medias=[{id, url}])` 建立成功
- **Element ID：`9f076fab-77ef-4c68-a146-f8060253c49a`**（name: `vicky-lin-anchor-v3-06`）
- 生成第一張測試圖後目視比對，確認臉部特徵（眼型、鼻型、唇型、臉頰輪廓、髮色）與錨點圖高度一致，證實 Element 機制確實有效錨定身分，跟前兩輪「各自獨立生成、只是風格像」的結果性質不同

### 3. 模型選擇與費用

- Element 內嵌只支援特定模型：`nano_banana_2`、`nano_banana_flash`、`gpt_image_2`、`seedream_v4_5`、`seedream_v5_lite`、`cinematic_studio_2_5`（`soul_2` 不支援，因此本輪不能沿用前兩輪的 `soul_2`）
- `get_cost` 預檢：`nano_banana_2` 2k 解析度每張 2 credits，1k 解析度每張 1.5 credits；`seedream_v4_5`（basic quality，最高 4K 輸出）每張固定 **1 credit**，成本最低且仍支援 Element embedding，故本輪採用 `seedream_v4_5`，`aspect_ratio: 9:16`，`quality: basic`
- 生成前餘額：30.23 credits；生成後餘額：**18.23 credits**，共花費 **12 credits**（12 張全部成功張，含 1 張伺服器端一度卡在 `in_progress`、稍後自行完成，未額外重生成；另有 2 次因 `rate_limit_reached (429)` 被拒絕的請求未扣款、已用相同 prompt 成功重送一次）

### 4. 產出檔案（`kols/vicky-lin/images/face_reference/`，`v4_anchored_` 前綴）

全部使用 `<<<9f076fab-77ef-4c68-a146-f8060253c49a>>>` 錨定同一身分，僅變化角度、景別、姿勢、場景、穿搭顏色：

| 檔名 | 角度 | 景別 | 場景／穿搭色系 | Job ID |
|------|------|------|----------------|--------|
| v4_anchored_01_front_headshot.png | 正面 | 臉部特寫 | 公園慢跑道，黃金時段，赤陶橘，開懷笑 | `8760591d-4c76-4901-8748-584418137d0e` |
| v4_anchored_02_front_halfbody.png | 正面 | 半身 | 戶外跑道，正午強光，鼠尾草綠，綁馬尾動作 | `2e7a86ce-89e4-4150-9ead-0fc7f1e1c5d7` |
| v4_anchored_03_front_fullbody.png | 正面 | 全身 | 海邊木棧道，日光，燕麥色，行走中 | `bcc779cb-bf7e-431a-b723-5b6fa215a613` |
| v4_anchored_04_3q_headshot.png | 四分之三側 | 臉部特寫 | 林蔭步道，斑駁光，黑色，回眸 | `4f280cad-8dbf-47b6-a01b-cdf53567397f` |
| v4_anchored_05_3q_halfbody.png | 四分之三側 | 半身 | 戶外球場，正午強光，燕麥色，插腰持手機 | `bf9446b0-c9f2-420c-8cd8-4141e9d8fea5` |
| v4_anchored_06_3q_fullbody.png | 四分之三側 | 全身 | 草坡，黃金時段伸展觸腳尖，赤陶橘 | `384c901f-4fc5-4d6c-825c-e234d2d082ea` |
| v4_anchored_07_side_headshot.png | 側面 | 臉部特寫 | 河濱步道，日光側光，鼠尾草綠 | `b9e3c54b-8cd0-4663-a908-5197f17634a1` |
| v4_anchored_08_side_halfbody.png | 側面 | 半身 | 戶外球場，黃金時段逆光，黑色，肩部伸展 | `cc88aada-dd27-4bb3-8c00-c00b0e767e70` |
| v4_anchored_09_side_fullbody.png | 側面 | 全身 | 戶外階梯，日光，燕麥色，爬階動態 | `8d4b40c6-efaf-4f51-af1d-bfdf6c2e4fae` |
| v4_anchored_10_front_halfbody_rooftop.png | 正面 | 半身 | 頂樓露台，午後光，赤陶橘，喝水 | `e48d64b0-4126-4555-acab-13a1b8c685fc` |
| v4_anchored_11_3q_fullbody_seated.png | 四分之三側 | 全身 | 公園草坪，黃金時段，鼠尾草綠，坐姿休息 | `d50c22b0-d2da-4a96-8f0e-c4113d9594d2` |
| v4_anchored_12_front_fullbody_turnback.png | 正面 | 全身 | 戶外跑道，日光，黑色，走離回眸 | `26956ab1-820e-49cf-92a4-81095811393b` |

**生成後目視檢查**：已用 Read 工具開啟 `v4_anchored_01`、`v4_anchored_04`、`v4_anchored_09`、`v4_anchored_12` 等多張跨角度/跨場景圖比對，臉型、五官、髮色、體態在 12 張圖中呈現高度一致的同一人身分，這是本輪與第二、三輪最根本的差異——第二、三輪是「同類型但不同人」，第四輪是「同一人，不同角度/場景/穿搭」。仍依 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉五項檢查（皮膚質感、裝置/鏡頭破綻、對應場景光線配方、生活雜物細節、完整服裝描述）逐張確認未退化。

**⚠️ 下一步（不可跳過）**：依照 README.md「新增 KOL 流程」第 6 點與 `KOL_TRAINING_SOP.md` 的強制規則，**必須停下來，等使用者實際審核這 12 張 Element 錨定的一致性參考圖，確認身分一致、風格滿意後，才可以進入 Soul 訓練**。本輪**沒有**呼叫 `show_characters(action='train')`，`profile.json` 的 `ai_generation`／soul_id 維持原狀未變更，訓練狀態明確標記為 **PENDING**。第二輪（`01_`–`08_`）與第三輪（`v3_01_`–`v3_08_`）圖片全部保留在同目錄供對照，未刪除。

---

## 2026-07-25 使用者核准，Soul 訓練嘗試（⚠️ 未成功啟動，訓練狀態仍為 PENDING）

**觸發**：使用者審核完第四輪 12 張 Element 錨定參考圖後回覆「可以」，明確核准進入 Soul 訓練。

**執行嘗試**：
1. 先嘗試直接用第四輪 12 張圖各自的原始生成 `job_id`（見上表）作為 `show_characters(action='train', images=[...])` 的輸入——連續 3 次呼叫都回傳工具層級的通用錯誤（`Something went wrong`），非額度或參數錯誤（`balance` 檢查全程維持 18.23 credits 不變，未被扣款）。
2. 依照 fallback 流程，改用 `media_upload`（12 個檔名）取得 12 組 presigned S3 URL 與全新 `media_id`，用 `curl -X PUT` 逐一上傳 12 張 `v4_anchored_01`–`12` 原始檔案位元組（全部回傳 HTTP 200），再用 `media_confirm` 確認全部 12 個 `media_id` 狀態為 `uploaded`。
3. 用這 12 個全新 `media_id` 重新呼叫 `show_characters(action='train', name='Vicky Lin', images=[...])`——**仍然持續失敗**，總共又嘗試 7 次，含：`images` 參數用 media_id（4 次）、`medias` 參數用 `{value: media_id}` 格式（1 次）、`images` 參數改用 media 的 https URL（1 次）、只傳 5 張測試是否為張數問題（2 次，含 `type='soul_2'` 顯式指定）——**每一次都回傳同樣的通用 `Something went wrong` 錯誤**，共 10 次訓練呼叫全部失敗。
4. 排除法確認問題出在 `show_characters(action='train')` 本身，而非帳號/圖片本身：`show_characters(action='list')`、`action='status')`、`show_reference_elements(action='list')`、`media_upload`、`media_confirm` 在同一段時間內全部正常運作；`action='list'` 也確認 Higgsfield 後端**沒有**建立任何名為「Vicky Lin」的角色記錄（`ready`/`training`/`failed` 皆無），代表訓練從未成功產生一個可查詢的角色物件。
5. **⚠️ 但並非完全零成本**：`balance` 在攻擊性重試期間曾多次顯示持平 18.23 credits（讓人一度誤判為「未扣款」），但後來重新檢查 `balance` 發現已降到 **16.07 credits**，用 `transactions` 工具核對，時間戳 `2026-07-25T18:41:22Z`–`18:42:51Z`（正好對應本輪重試 `show_characters(action='train')` 的時段）出現約 20 筆 `Higgsfield Soul V2`、每筆 `-0.12 credits` 的扣款紀錄，累計約 **2.16–2.4 credits** 被扣款，即使**沒有任何一次呼叫成功回傳、也沒有建立任何角色記錄**。換句話說：工具回傳給呼叫端的是失敗訊息，但 Higgsfield 後端顯然仍對部分/全部重試呼叫實際處理並扣款，屬於「呼叫失敗但仍計費」的異常情形，並非單純的免費失敗重試。

**結論（誠實記錄，不可竄改）**：
- **沒有**取得任何 `soul_id`、也沒有建立任何角色記錄；`profile.json`／README.md **保持原狀未修改**，避免記錄不存在的訓練結果；`KOL_TRAINING_SOP.md` 進度表的 Vicky Lin 列已更新為反映「已核准但訓練呼叫失敗」的真實現況（不含虛構 soul_id）。
- Soul 訓練狀態維持 **PENDING（訓練未啟動）**，不是 `training`，也不是 `ready`。
- **實際已產生費用損耗：約 2.16–2.4 credits**（10 次訓練呼叫中的部分嘗試被計費，即使全部回傳失敗且無任何訓練結果），下次重試前應留意這是「有成本的失敗」，不是完全免費的重試。
- 12 張 `v4_anchored_` 圖片與其新的 `media_id`（供下次直接重試，不需要重新上傳）：

| 檔名 | media_id（已上傳並確認，可直接用於下次 `show_characters(action='train')` 嘗試） |
|------|------|
| v4_anchored_01_front_headshot.png | `b23c9a4f-693b-49fd-9134-a7d92639c7fb` |
| v4_anchored_02_front_halfbody.png | `713313a7-e4bf-44c3-a0b1-21c04558f1e9` |
| v4_anchored_03_front_fullbody.png | `d80fbaf1-f2b7-4ea5-9e3f-d37d4cfb004d` |
| v4_anchored_04_3q_headshot.png | `122c157d-f89c-4c97-821b-999271075ba3` |
| v4_anchored_05_3q_halfbody.png | `a2faf175-5afa-40fa-b835-26179fc42240` |
| v4_anchored_06_3q_fullbody.png | `acb42383-efff-4f90-8878-a00ecb0a74d7` |
| v4_anchored_07_side_headshot.png | `2299b514-103b-42c9-b168-1a10d2cda689` |
| v4_anchored_08_side_halfbody.png | `1a0f5e61-ac44-431d-bf80-e73b4b288031` |
| v4_anchored_09_side_fullbody.png | `33e0abeb-bb7d-43a9-b85a-e68bf6d06705` |
| v4_anchored_10_front_halfbody_rooftop.png | `da3eca16-a732-48c4-a984-96902492c3b3` |
| v4_anchored_11_3q_fullbody_seated.png | `089798dc-96cc-42de-b314-592bd6f8ea8a` |
| v4_anchored_12_front_fullbody_turnback.png | `3ab2c1e1-e974-4787-a844-3a6dba6350e1` |

**⚠️ 下一步（不可跳過）**：這 12 個 `media_id` 有效期未知（S3 presigned URL 本身已過期無妨，`media_id` 是伺服器端物件不受 900 秒 presign 過期影響），下次 session 應直接優先重試 `show_characters(action='train', name='Vicky Lin', images=[上表 12 個 media_id])`，不需要重新上傳；若持續失敗，需視為 Higgsfield MCP 服務本身的 `train` 端點暫時異常，建議稍後再試或聯繫確認服務狀態。**在成功取得真實 `soul_id` 且狀態確認前，不可以更新 `profile.json`／README.md／`KOL_TRAINING_SOP.md` 的訓練欄位。**

---

## 2026-07-25 Soul 訓練第二次重試（同日、第二次 session，⚠️ 仍未成功啟動）

**觸發**：使用者被詢問是否要重試 Soul 訓練時回覆「應該是要重新試試看吧」，明確同意重試。本次重試**刻意限制嘗試次數**（最多 2–3 次），避免重演上一次 session「連續 10 次盲目重試、每次都可能計費」的問題。

**執行前檢查**：呼叫 `balance` 確認重試前餘額為 **15.35 credits**（低於前次記錄的 16.07 credits——研判前次 session 記錄的 16.07 是重試當下尚未完全結算的中繼值，`transactions` 本身有延遲入帳的已知現象，實際扣款在那之後可能又持續入帳了一段時間，把餘額進一步壓低到 15.35；沒有找到其他花費紀錄可以解釋這筆差額，記錄於此供後續核對）。

**嘗試 1（最標準參數形狀）**：使用上表已上傳確認的 12 個 `media_id`，呼叫
```
show_characters(action='train', name='Vicky Lin', images=[12 個 media_id])
```
結果：**再次失敗**，回傳同樣的工具層級通用錯誤 `Something went wrong. Please try again.`（Request ID `53698440-dea4-48dc-8b62-59216b2e30ed`）。

**立即查核計費情形**：呼叫前 `balance` 為 15.35 credits，呼叫失敗後立刻再查一次 `balance` 仍顯示 15.35 credits（表面上看似未扣款）。但用 `transactions` 直接核對交易明細，發現在呼叫發生的同一時間窗（`2026-07-25T19:43:07Z`–`19:43:22Z`）多了 **4 筆全新的 `Higgsfield Soul V2` -0.12 credits 扣款紀錄**（與上一輪 session 18:41–18:42 的舊記錄時間戳明顯不同、確定是本次新產生的）——代表**這一次呼叫確實又被計費約 0.48 credits，只是 `balance` 端點沒有即時反映**，跟上一輪 session 記錄的「呼叫失敗但仍計費」+「balance 有延遲」現象完全一致，這個異常模式在本次重試中又重現了一次。

**嘗試 2（替代參數形狀）**：依指示只再試一種替代形狀後即停止，改用 `medias` 參數（`{role: 'image', value: media_id}` 陣列）呼叫
```
show_characters(action='train', name='Vicky Lin', medias=[{role:'image', value: media_id}, ... 12 組])
```
結果：**同樣失敗**，回傳同樣的通用錯誤 `Something went wrong. Please try again.`（Request ID `9b9dcdf1-c44d-41f1-9b4e-bca312e043ae`）。事後核對 `transactions`（取最新 20 筆）未出現新增的扣款時間戳，判斷這一次呼叫本身**沒有**被計費。

**依指示停止重試**：本次 session 只嘗試 2 次（1 個標準形狀 + 1 個替代形狀）即停止，不再繼續排列組合，避免重演上一輪「10 次盲試、每次都可能計費」的狀況。

**驗證確實無角色記錄產生**：呼叫 `show_characters(action='list')` 取得目前帳號下全部角色，共 6 筆（Camille Dupont、Aaliya Rivera、Yuna Kim、Ananya Kapoor、Luna Tanaka、Iris Chen，全數 `status: ready`），**沒有任何名為「Vicky Lin」的角色記錄**，確認本次兩次嘗試都沒有在伺服器端建立任何角色物件，即使其中一次被計費。

**本次 session 費用損耗**：約 **0.48 credits**（嘗試 1 計費 4×0.12；嘗試 2 未計費）。

**累計費用損耗（兩次 session 合計）**：約 **2.64–2.88 credits**（第一次 session 2.16–2.4 credits ＋ 本次 session 0.48 credits），仍然**沒有取得任何 soul_id、沒有任何可用的訓練結果**。

**結論（誠實記錄，不可竄改）**：
- Soul 訓練狀態維持 **PENDING（訓練未啟動）**，`profile.json`／README.md 保持原狀未修改。
- `show_characters(action='train')` 端點對 Vicky Lin 這批資料持續回傳工具層級通用錯誤，累計兩次 session、12 次呼叫全部失敗，判斷更可能是 Higgsfield 後端 `train` 端點本身的持續性異常（而非單次暫時性問題、也不是參數格式問題——已測試過 job_id、media_id（`images`）、`medias` 包裝格式、https URL、不同張數等多種形狀，全部失敗），建議下次重試前先確認 Higgsfield 服務狀態，或考慮改用人工／客服管道回報此問題，而非持續消耗 credits 盲目重試。
- 12 張 `v4_anchored_` 圖片與其 media_id（見上方「使用者核准，Soul 訓練嘗試」章節表格）仍然有效可直接重試，不需要重新上傳。

---

## 2026-07-31 第三次重試：訓練成功送出

**觸發背景**：使用者要求重新測試 Vicky Lin 的訓練，看服務是否已恢復正常。

**做法**：沿用先前已上傳確認、仍然有效的 12 個 `v4_anchored_` media_id（見上方「使用者核准，Soul 訓練嘗試」章節表格），不需重新上傳圖片，直接呼叫 `show_characters(action='train', name='Vicky Lin', images=[...12個 media_id])`。

**結果**：**第一次呼叫即成功受理**，與先前兩次 session 累計 12 次全部失敗的情形完全不同。取得 `soul_id: bdb1d879-da36-4c1a-bc63-9f5b49a3e94e`，`status: training`，`raw_status: queued`。呼叫後查詢 `balance` 為 2202.2 credits（`ultra` 方案），本次餘額充足，未觀察到異常扣款。

**判斷**：先前記錄中懷疑的「Higgsfield 後端 `train` 端點持續性異常」看來已經恢復正常，並非參數或圖片本身的問題——這與最初的懷疑方向一致（因為先前已測試過多種參數形狀皆失敗，指向服務端問題而非請求格式問題）。

**同日追蹤確認完成**：透過 `show_characters(action='status', soul_id='bdb1d879-da36-4c1a-bc63-9f5b49a3e94e')` 確認 `status: ready`、`raw_status: completed`。Soul 訓練正式完成，可用 `model: soul_2` + 此 soul_id 生成正式發布內容。

`profile.json` 已補上 `ai_assets.training_images_v1.soul_training` 欄位（`status: ready`）。`README.md`／`KOL_TRAINING_SOP.md` 已同步更新。

---

## 下一步（待執行）

1. ~~選定圖片生成模型並小規模測試~~ 已完成：第二輪、第三輪使用 `soul_2`（一次性角色參考圖，但無身分錨定）；第四輪改用 `seedream_v4_5` + Reference Element 錨定同一身分
2. ~~等待使用者比較第二輪與第三輪參考圖~~ 已被更根本的問題取代：發現獨立文字生成無法保證身分一致，因此第四輪改採 Element 錨定方式重新生成訓練圖
3. ~~等待使用者審核第四輪（`v4_anchored_01`–`v4_anchored_12`）Element 錨定參考圖，確認身分一致且風格滿意~~ 已完成：使用者回覆「可以」，明確核准進入 Soul 訓練
4. ~~`show_characters(action='train')`~~ 已於 2026-07-31 第三次重試成功送出（`soul_id: bdb1d879-da36-4c1a-bc63-9f5b49a3e94e`）——前兩次 session 累計 12 次失敗的記錄保留於上方章節供未來參考
5. ~~確認訓練完成狀態~~ 已完成（2026-07-31 同日，`action='status'` 確認 `status: ready`、`raw_status: completed`）
6. 現在可用 `model: soul_2` + 此 soul_id 生成正式發布內容
7. 影片生成流程（模型選擇、prompt 模板、剪輯節奏對應）待圖片流程確認後另行規劃，目前尚未展開

---

## 2026-08-05 競品對標實測批次（Sherry 打法驗證，7 位台灣籍角色各 2 張）

> **批次目的**：驗證從競品 @sherry_digitalp510 拆解出的三項新做法能否用純生成複製——(1) 公共場景加入背景路人、(2) 同穿搭一日敘事串聯兩張、(3) 地點寫成環境元素清單。完整拆解見 `COMPETITOR_sherry_digitalp510.md`，規則已寫入 `SEXY_SCENE_LIBRARY.md` 第 9／11／12 點。
>
> **平台／模型**：Higgsfield `soul_2` + 本角色 `soul_id`，quality 2k，aspect_ratio 3:4
> **成本**：全批 14 張約 8 credits
> **使用者決定**：本批次**不重新生成**，spec 落差記錄在案，留待後續處理

### 本角色結果

| 項目 | 內容 |
|---|---|
| Soul ID | `bdb1d879-da36-4c1a-bc63-9f5b49a3e94e` |
| 場景 | 河濱步道（晨跑伸展／長椅補水） |
| 穿搭（A/B 共用） | 鼠尾草綠運動內衣 + 同色高腰緊身褲 + 米色風衣（A 綁腰／B 滑落肩）+ 白色跑鞋 + 智慧錶 |
| Job ID（A） | `aa691d78-83bd-4a5a-a3b8-09d9079262d2` |
| Job ID（B） | `c69bbb43-3e16-46a3-91b7-ee7024a56df3` |
| 評定 | ✅ 通過（本批最佳之一） |

背景慢跑者／散步者／單車騎士自然分布、全部背向失焦。同色系成套穿搭與配件狀態演變（風衣從腰間移到肩上、長椅上多了手機與毛巾）非常成功。手部經放大檢查正常（扶欄杆姿勢、智慧錶皆無異常）。**落差 1**：點名「高雄愛河」，生成天際線為墨爾本樣貌——已據此新訂規則 11。**落差 2**：膚色仍偏溫暖小麥，未完全達到規則 6 的白皙基調。

### 本批次共同結論（全 7 位角色適用）

- ✅ **背景路人：14/14 全部成功，且無任何配角撞臉主角。** 四條件措辭（背向／不看鏡頭／失焦／外型與主角區隔）有效，成本為零。原「預設只有本人入鏡」規則對公共場景已反轉。
- ✅ **同穿搭一日敘事：7/7 成功。** 服裝配件完整延續且狀態自然演變。
- ⚠️ **地點：環境元素清單成功，點名地標全部失敗。** 「愛河」生出墨爾本天際線、「台北 101」生出通用摩天樓群。
- ⚠️ **中文招牌全部亂碼**（與競品同等程度），本批次接受此取捨。

---

## 2026-08-07 R3 舞蹈克隆完整跑完 Step 1–8（動作驅動複製法 Method B）

**背景**：舞蹈批次分配（見 `DANCE_CLONE_SOP.md` 大量選片 SOP、GitHub Issue #3）R3 原本分配給 Zoe Lai，
該人格已停用，改分配給 Vicky Lin。驅動片：`https://www.instagram.com/reel/C2zOi2uPdxn/`（原創作者
@yua_mikami）。**敘事包裝**：內容是婚紗試穿間手勢舞，跟 Vicky 本人「健身正妹」的日常人設不同調，但她的
`character.md` 背景設定本來就是競技舞蹈出身、退出後才轉練重訓，且她有明確的「反差萌」特質（見
`character.md` 165 行、`content_style.md` 305 行）——用「陪閨蜜思穎試婚紗，順便自己也試穿一件」的敘事
框架來合理化這支特殊場景，符合人設鬆綁後「多數時候如此，但不是不可能」的原則，不需要視為出戏。

### Step 1–2：下載與裁剪

- `yt-dlp` 下載，720×1280、30fps、~10.85s，含原始配樂（aac）
- 內容目視核對：白色鑽飾/亮片胸衣婚紗 + 白色頭紗，試衣間場景（淺藍布幔背景、掛著禮服的衣架、落地鏡），
  單鏡頭手持自拍運鏡無切鏡，一連串手勢/表情動作＋結尾轉身側身秀禮服，符合分配描述「婚紗禮服快手勢舞，
  試衣間場景」
- 畫面左下角帶有 TikTok 浮水印（@yua_mikami）：`ffmpeg crop=in_w*0.5:in_h:in_w*0.25:0` 裁成單人置中，
  同時裁掉浮水印（剛好落在裁掉的左側 25% 範圍內），輸出 360×1280；音軌另存 `driver_audio.m4a`
- `ffprobe` 確認原始碼流已是 h264，不需要額外重新編碼

### Step 3：Performance Sheet + Emotion Timeline

呼叫 `performance-director` 與 `emotion-director` agent（依 1 秒取樣的文字時間軸描述）。重點結論：

- **阻斷級問題（生成前已修正）**：驅動片本身是胸口以上的緊裁鏡位，禮服本身（鑽飾胸衣）沒有次級動態
  載體，且裙擺根本不入鏡——performance-director 判定這是 wardrobe 層級的缺口，建議加一件**教堂長頭紗**
  當次級動態載體（頭紗在結尾 9–10.8s 轉身時會有慣性甩動，本來就是婚紗場景敘事上合理的元素），
  並保留驅動片本身描述的「放下的長髮」作為第二載體。已在 Step 4 的 prompt 中加入頭紗。
- **情緒設計**：驅動片表情強度偏「偶像可愛」路線（4.0s 嘟嘴飛吻、多次誇張大笑），跟 Vicky「自信直接、
  有點欠揍」的人設不同調——建議把 4.0s 嘟嘴飛吻改成「不對稱抿嘴笑+眨眼」，3.0s/6.0s 的大笑保留動作但
  詮釋成「被自己的美震驚到真心笑出來」而非表演給鏡頭看的可愛。核心識別錨點：**右嘴角明顯高於左邊的
  不對稱冷笑**（她標誌性的自信表情），全片必須維持這個不對稱基準，不能變成對稱的甜笑。
- **風險標記**：6.0s 手指張開的比手勢動作（Kling 手部常見失敗區）、9.0–10.8s 轉身側面（soul_id 訓練圖
  是否有側面/3/4 角度）、亮片/鑽飾材質（不能上磨皮濾鏡，會糊掉細節）——皆列入 Step 8 QA 重點。

### Step 4：起始畫面（生成兩次，第一次因對稱笑容打回）

- 第一次生成（job `24e325ae-291c-4b26-b61c-a2716ba449eb`）：構圖、場景、服裝、頭紗都符合要求，但笑容是
  左右對稱的露齒大笑，違反 emotion-director 訂的「不對稱冷笑」識別錨點——判定不合格，**不進入 Step 5**，
  保留檔案為 `start_frame_v1_rejected_symmetric_smile.png` 供對照
- 第二次生成（job `a2c0426f-4de1-4610-a69b-78d12e6163d1`，soul_id `bdb1d879-da36-4c1a-bc63-9f5b49a3e94e`，
  `soul_2`，`count=1`，`aspect_ratio 9:16`）：prompt 明確要求「閉唇冷笑、只有右嘴角揚起、不露齒、左眉
  略高於右眉」，生成結果確認不對稱冷笑成立，頭紗、場景、身分一致性皆符合，使用者審閱後回覆「可以直接
  拿來做」——核准為 `start_frame.png`，進入 Step 5

### Step 5：Motion Control

- 驅動片 `driver_cropped.mp4` 上傳確認，`media_id: 8c5de43c-693c-4696-8c6c-d1d766346d79`
- `image_id`: `a2c0426f-4de1-4610-a69b-78d12e6163d1`（起始畫面 job，直接沿用不需重新上傳）
- `scene_control`: `image`（保留 Vicky 自己的試衣間場景，不借用驅動片的真實店家背景，避免帶出可辨識
  的第三方店家資訊），`resolution`: `1080p`
- 輸出：`1072×1936`、30fps、10.8s，Job ID `e574a1eb-8003-4cb9-a8b6-c36eebc48ec1`
- **輸出本身無聲**（`ffprobe` 確認只有一條 h264 視訊流），需要 Step 6 手動混音

### Step 6：手動混音

用 `ffmpeg -map 0:v:0 -map 1:a:0 -c:v copy -c:a aac -shortest` 把 Step 2 抽出的 `driver_audio.m4a`
（驅動片原始配樂，裁剪起點對齊 0s）蓋上 Kling 輸出的無聲畫面，輸出
`vicky_dance_clone_r3_ig_reel.mp4`（10.8s，含視訊+音訊雙軌，已用 `ffprobe` 確認）。

### Step 7：授權與發佈限制檢查

- **驅動動作**：來自第三方 Instagram/TikTok 創作者（@yua_mikami，浮水印已在裁切時去除），本次生成僅供
  內部方法驗證；若要對外發佈，需評估重現程度是否需要致敬標註或改編到不可辨識
- **配樂**：混音使用的是驅動片原始配樂，**未取得商用授權**，正式發佈前必須替換為已授權/可商用曲庫版本，
  並重新對拍
- **背景**：`scene_control` 選用 `image`（Vicky 自己的生成場景），未借用驅動片真實店家背景，不涉及第三方
  地點/招牌可辨識性問題
- **素材存放**：驅動片原始檔（`driver_raw.mp4`、`driver_cropped.mp4`、`driver_audio.m4a` 原始複本）僅存
  在本機工作資料夾，未存入本 repo，符合 `DANCE_CLONE_SOP.md` 的規定

### Step 8：QA 檢核（已用 Read 工具目視抽幀比對，非假設）

抽樣 0.2s / 1.5s / 2.5s / 3.0s / 4.0s / 4.2s / 6.0s / 6.2s / 7.0s / 8.0s / 8.2s / 9.3s / 9.5s / 10.0s /
10.5s 共 15 個時間點：

- [x] **身分一致**：全程可清楚辨認深色長髮、健身身材曲線，跟起始畫面的錨定身分一致
- [x] **不對稱冷笑識別錨點有效轉印**：多個抽樣幀（0.2s、6.2s、9.3s、10.5s）都看得到右嘴角明顯高於左邊
  的冷笑，不是對稱甜笑，符合 emotion-director 訂的識別錨點
- [x] **微表情有變化**：抽樣幀之間表情、嘴型、眼神角度皆不同（冷笑 → 張口說話 → 皺眉驚訝 → 交叉手臂
  → 側身回眸），不是同一張臉套多個手勢的面具臉
- [x] **次級動態確實轉印**：頭紗在多個抽樣幀呈現不同垂墜角度與飄動狀態（尤其 9.3s–10.5s 轉身段落，
  頭紗明顯甩動），長髮也有隨轉身擺動的痕跡，確認次級動態有效轉印，不是靜態貼圖
- [x] **6.0s 附近的手勢張開手指風險——實際檢視後判定沒有出問題**：Performance Sheet 擔心的比手勢手指
  變形沒有發生，手指數量與形狀正常
- [x] **4.0s/4.2s 手部交叉胸前風險——實際檢視後判定沒有出問題**：雙手交叉貼近胸口的動作手指清晰可辨，
  沒有觀察到多指/融指等變形
- [x] **9.3s–10.5s 側面轉身風險——實際檢視後判定沒有出問題**：轉身至側面/四分之三側臉時身分仍清晰可辨，
  沒有出現崩臉或身分漂移
- [x] **背景穩定**：試衣間場景（淺藍布幔、衣架掛禮服、落地鏡）全程一致，無鬼影閃爍
- [x] **鑽飾/亮片材質保留細節**：胸衣上的水鑽/亮片圖案在多個抽樣幀清晰可辨，沒有被磨皮糊成一片
- [x] **手部整體無明顯崩壞**（15 幀抽樣檢視未發現手指數量/形狀異常）
- [x] **卡拍**：驅動片原始配樂與生成畫面長度一致（皆 10.8s），混音對齊裁剪起點
- [x] **規格**：1072×1936（超過 1080×1920 門檻）、30fps、音樂已對齊長度

**結論**：Step 4 起始畫面第一次生成因對稱笑容不符合角色識別錨點被打回、重新生成後才進入 Motion Control，
是這次流程裡唯一需要重做的環節；Step 5–8 一次到位，Performance Sheet 標記的三個風險（手勢手指、手部
交叉、側面轉身）實際檢視後都沒有出問題。使用者已審閱起始畫面並核准「直接拿來做」。

### 產出檔案

- `kols/vicky-lin/images/dance_clone_r3/start_frame.png`（已核准起始畫面）
- `kols/vicky-lin/images/dance_clone_r3/start_frame_v1_rejected_symmetric_smile.png`（第一次生成，對稱
  笑容不符合識別錨點，僅供對照）
- `kols/vicky-lin/videos/dance_clone_r3/vicky_dance_clone_r3_ig_reel.mp4`（1072×1936、30fps、10.8s，
  含驅動片原始配樂音軌，未經授權，僅供內部驗證）
- 🔴 **打光尚未套用新公式。** 本批次仍使用舊的「品質形容詞」寫法（`crisp`／`high dynamic range`／`well-exposed`）。2026-08-05 拆解競品後已改寫 `SEXY_SCENE_LIBRARY.md` 第 3 點為五段式物理光線公式，**下一批次應以驗證該公式為首要目標**。
