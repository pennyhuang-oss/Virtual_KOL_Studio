# Vicky Lin — AI 生成規劃

> **狀態：PENDING（尚未執行）**
> 本文件只是生成前的規劃筆記——尚未進行任何 Soul 訓練、尚未生成任何訓練圖或影片，也尚未選定最終使用的模型版本。所有 prompt 為草稿，需要實際跑過並確認效果後才能標記為已驗證。文件中不含任何 soul_id、job_id、圖片張數或生成日期，因為目前都還不存在。

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
| Soul 模型 | 尚未建立 | **PENDING** |
| 訓練圖 | 第二輪參考圖已生成（8 張，見下方 2026-07-25 記錄），**等待使用者確認** | **PENDING** |
| 已生成圖片數量 | 8（臉部參考圖，待使用者審核，尚未進入 Soul 訓練） | **PENDING** |
| 已生成影片數量 | 0 | **PENDING** |

**⚠️ 生成一致性注意**：她的核心視覺特徵是「漂亮性感」，健身只是風味設定。任何批次的 prompt 都必須維持甜美有魅力的臉部表情、精緻不誇張的體態線條、健康小麥膚色；場景、穿搭、光線可以依批次變化，但**絕對不能**往銳利強勢的臉部表情或塊狀/血管紋理的健美選手體態靠攏——第一輪試跑（見下方）就出現過這個問題，已修正描述，之後每批生成前都要對照這條檢查。

---

## 核心 Prompt 結構（規劃草稿，未驗證）

以下為預計用於後續訓練圖 / 生活照生成的**可重複使用基礎 prompt**。全部使用純外觀描述詞，不引用任何真實藝人或公眾人物姓名。

> **⚠️ 降低「AI 感」規則**：本節與下方所有批次 prompt 都必須涵蓋 `SEXY_SCENE_LIBRARY.md`〈降低「AI 感」的技術要點〉五項——(1) 具體皮膚質感關鍵字、(2) 逐場景明確的拍攝裝置/鏡頭與其破綻、(3) 混合不均勻光源配方、(4) 具體生活雜物細節、(5) 完整明確服裝。送出生成前用該文件的「生成前檢查清單」逐項檢查。

```
25-year-old Taiwanese woman, strikingly beautiful and warm face, bright almond-shaped eyes, soft high cheekbones, straight elegant nose, full lips with a natural friendly smile, gorgeous fitness-model good looks (NOT a stern or intense expression), toned athletic hourglass figure with soft feminine curves, flat stomach with only a subtle soft hint of ab definition (NOT blocky or vascular bodybuilder muscle), full chest, cinched waist, rounded lifted glutes and thighs, sun-kissed glowing skin with visible skin pores, subtle natural skin texture, unretouched skin detail, natural skin imperfections, long black hair, [HAIRSTYLE], [SCENE — with specific lived-in clutter details relevant to the location], wearing [FULLY EXPLICIT OUTFIT], [POSE/ANGLE — natural and flattering, NOT a bodybuilding competition stance], [MIXED, UNEVEN LIGHTING RECIPE — not clean studio light], [DEVICE/CAMERA SPEC — specific model, front or back camera, and its actual artifacts: autofocus softness, highlight clipping, motion blur, compression artifacts, as fits the scene], slightly high-contrast true-to-skin color grading, visible sweat sheen where relevant, film grain, candid lifestyle photo, Instagram style
```

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

## 下一步（待執行，非已完成）

1. ~~選定圖片生成模型並小規模測試~~ 已完成：本輪使用 `soul_2`（無 soul_id，一次性角色參考圖）
2. **等待使用者確認上方 8 張參考圖是否滿意**——這是強制的人工確認關卡，不可跳過
3. 使用者確認滿意後，才呼叫 `show_characters(action='train')` 執行 Soul 訓練
4. Soul 訓練完成後才回頭補上 soul_id、訓練圖路徑與實際批次記錄至 `profile.json` 與 `character.md`
5. 影片生成流程（模型選擇、prompt 模板、剪輯節奏對應）待圖片流程確認後另行規劃，目前尚未展開
