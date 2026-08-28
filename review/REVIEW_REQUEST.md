# 覆核請求 R8b：重寫後的 prompt（第二批，6 件）

> ⚠️ **請只讀這一個檔案**，不要瀏覽目錄或讀 repo 背景（連接器爬整個 repo 會一次耗掉使用者 5 小時用量）。
> 判斷所需內容已全部貼在下面。回覆填在最後的「回覆區」，不要改問題本文。

接續 R8a。你在 R8a 的判定已全部照做：
- 光線句改成「臉保留自然膚色與高光細節；具名光源是畫面最亮處，只有局部最高光到白」
- LG-02 赤腳退出驗收（比例優先）／LG-05 景別放寬到小腿中段（保住傘尖防浮空錨點）
- YG-03 明寫只有一隻可見手／YG-07 移除赤腳並改拇指停在螢幕／YG-10 手背朝鏡頭且鏡面柱改非鏡面／LG-10B 刪 ankle-length

**本批是剩下 6 件**：雙手共同一個任務，或完全沒有手部任務。
依 R7 Q5 **逐件回 PASS／REVISE／BLOCK**。

## 我這批自己看到的三個疑慮

1. **YG-09 的濕髮**：另一件（LG-08）的濕髮**連續 4/4 生成失敗已被移除**，但那是另一個角色。
   本件維持濕髮設定但**不列入硬驗收**，只記 soft observation。這樣處理夠嗎？
2. **LG-07 是本批最複雜**：全身 ＋ 骨盆朝離開鏡頭上半身轉回 ＋ 桶子抵下巴，三件事疊在一起。
3. **LG-01 的景別**：臉＋肩近景要同時放下蛋糕與拿鐵。
   同型的 YG-01 曾因「近景放不下桌上物件」出過事，當時的處置是把物件移出 prompt。
   本件寫「at the lower edge」是否足夠，還是應該比照 YG-01 直接移除？

---
## YG-06｜汗蒸幕・甜米露

**全身（坐姿）。**　|　反射面：具名（木地板把暖光反回下巴）｜曝光：低反差（室內均勻頂燈）｜色溫：不適用（全場暖色）

- **凍結瞬間**：盤腿坐在木地板上，雙手把紙杯捧在下巴前，眼睛越過杯緣往上看鏡頭。
- **手部任務**：可見手 A＋B：**共同**捧住紙杯在下巴前（兩手一個任務） ／ 無第三個手部任務
- **硬驗收**：① 雙手捧紙杯在**下巴前**（不是胸前）② 越過杯緣看向鏡頭 ③ 盤腿坐姿、全身入鏡 ④ 頭上毛巾羊角可見

```text
A young woman sits cross-legged on a heated wooden floor, cupping a paper cup of sweet rice punch in both hands in front of her chin, her eyes peeking over the rim toward the camera, crinkled into crescents. Full body, camera at her seated eye level, shot from well back. Collarbone-length mocha brown hair in a low bun, two damp strands at her temples. A grey sauna tee and shorts, a towel folded into sheep horns on her head, bare feet. A bright sauna rest hall with low tables. Warm ceiling light on her face, the wooden floor bouncing warm fill up onto her chin, the hall behind her staying readable and slightly darker. Natural skin texture, subtle film grain.
```

## YG-09｜飯店窗邊・皮膚特寫

**臉部大特寫。**　|　反射面：具名（白色床單回彈補下巴）｜曝光：取捨（窗外城市失細節）｜色溫：不適用（單一窗光）

- **凍結瞬間**：臉部大特寫，側身靠著窗框，眼睛看著窗外遠處，睫毛半垂、嘴唇放鬆——這件刻意不做表情。
- **手部任務**：可見手 A：**N/A**（臉部大特寫，裁切外） ／ 可見手 B：**N/A**（裁切外） ／ **本件沒有任何手部任務**——不要為了填表把「另一手自然垂放」寫進 prompt
- **硬驗收**：① 臉部大特寫比例，臉佔滿畫面 ② 視線在畫面外、**不看鏡頭** ③ **畫面內沒有任何手** ④ 光線正面均勻、無逆光

```text
A young woman leans against the window frame gazing far out through the glass, lashes lowered, lips relaxed. Tight close-up of her face, camera at her eye level, lens horizontal. Wet collarbone-length mocha brown hair pushed straight back, water still beading at the ends. A white bathrobe with the collar loosened. A hotel room, white bedding, a floor-to-ceiling window, city towers outside. Soft window light full on her face, the white bedding bouncing fill up under her jaw. Her face is clearly exposed with natural skin texture; the city outside is the brightest area, only its smallest highlights reaching white. Visible skin pores, subtle film grain.
```

## LG-01｜甜點店靠窗・臉部近景

**臉部＋肩膀近景。**　|　反射面：具名（淺木桌面回彈補下巴）｜曝光：取捨（窗外失細節）｜色溫：不適用（單一窗光）

- **凍結瞬間**：手肘撐在桌上、雙手托著兩頰把臉擠得更圓，頭往一側傾，對鏡頭用眼睛笑。
- **手部任務**：可見手 A＋B：**共同**托腮（左右各托一頰，兩手一個任務） ／ 無第三個手部任務
- **硬驗收**：① 雙手托兩頰、臉被擠圓 ② 頭往一側傾 ③ 臉佔畫面約 45%，蛋糕與拿鐵在下緣入鏡 ④ 鮑伯及下巴、剪裁齊平

```text
A young woman rests both elbows on the table, cupping both cheeks in her palms, her cheeks squished round, head tilted to one side, smiling with her eyes. Close-up of her face and shoulders, camera at her eye level. A blunt chin-length black bob cut evenly at the jawline, centre-parted. A cream square-neck puff-sleeve top, small pearl earrings. A dessert shop window seat, a white tiled wall, a strawberry cake and a latte at the lower edge. Soft window light from her side, the pale wood table bouncing fill onto her chin. Her face is clearly exposed with natural skin texture; the window is the brightest area, only its smallest highlights reaching white. Visible skin pores, subtle film grain.
```

## LG-06｜可愛系街區・扭蛋機前

**半身。**　|　反射面：具名（扭蛋機彩色面板回一點顏色）｜曝光：低反差（街上柔和天光）｜色溫：不適用

- **凍結瞬間**：雙手把打開的扭蛋殼捧在胸前，頭朝著它低下去，笑到眼睛瞇起來。
- **手部任務**：可見手 A＋B：**共同**捧著打開的扭蛋殼在胸前（兩手一個任務） ／ 無第三個手部任務
- **硬驗收**：① 雙手捧扭蛋在胸前 ② 頭朝扭蛋低下 ③ 眼睛瞇起／閉起笑（**與「看鏡頭」互斥，不可並存**）④ 半身比例

```text
A young woman holds an opened gachapon capsule in both hands at chest level, her head angled down toward it as she laughs with her eyes squeezed shut. Half body, camera level with her chest. A blunt chin-length black bob cut evenly at the jawline, two small clips holding her fringe back. A pale pink cropped knit top showing a sliver of waist, white high-waisted shorts, a denim jacket tied at her waist. A row of colourful gachapon machines behind her, bright shop signage, clean pavement. Soft daylight on her face, her face evenly exposed, the coloured machine panels throwing a little colour onto her arms, the machines behind her staying slightly darker. Natural skin texture, subtle film grain.
```

## LG-07｜遊樂園・旋轉木馬

**全身。**　|　反射面：具名（淺色地面回彈補下巴）｜曝光：低反差（遊樂園柔和天光）｜色溫：分裂（天光冷白 vs 旋轉木馬燈泡暖黃）

- **凍結瞬間**：雙臂把爆米花桶抱到下巴下方，骨盆朝離開鏡頭的方向、上半身轉回四分之三，越過桶緣看鏡頭。
- **手部任務**：可見手 A＋B：**共同**抱住爆米花桶抵在下巴下方（兩手一個任務） ／ 無第三個手部任務
- **硬驗收**：① 雙臂抱桶抵在下巴下方 ② 越過桶緣看鏡頭 ③ 骨盆朝離開鏡頭、上半身轉回 ④ 全身比例，腳貼近畫面下方 1/3

```text
A young woman hugs a popcorn bucket up under her chin with both arms, her hips angled away from the camera and her upper body turned three-quarters back, looking over the rim toward the camera with a playful smile. Full body, camera at her navel level, shot from well back, her feet near the lower third. A blunt chin-length black bob cut evenly at the jawline, a cat-ear headband. A white square-neck puff-sleeve top, a pale blue pinafore skirt, white mary janes with lace socks. A carousel behind her, coloured balloons. Cool soft daylight on her face, warm carousel bulbs glowing behind, the pale ground bouncing fill onto her chin. Natural skin texture, subtle film grain.
```

## LG-09｜台式早餐店・豆漿

**半身，人＋食物同框。**　|　反射面：具名（不鏽鋼餐檯回彈補下巴）｜曝光：取捨（門口天光失細節）｜色溫：分裂（門口冷白 vs 店內日光燈）

- **凍結瞬間**：雙手把玻璃杯捧在下巴前，頭略低、眼睛往上越過杯緣看鏡頭，用眼睛笑。
- **手部任務**：可見手 A＋B：**共同**捧住玻璃杯在下巴前（兩手一個任務） ／ 無第三個手部任務
- **硬驗收**：① 雙手捧杯在**下巴前**（不是胸前）② 頭略低、眼睛往上看鏡頭 ③ 人與豆漿杯同框 ④ 半身比例

```text
A young woman holds a glass of soy milk in both hands in front of her chin, head slightly lowered, eyes looking up over the rim toward the camera. Half body with the glass in frame, camera at her eye level. A blunt chin-length black bob cut evenly at the jawline, centre-parted. A cream fitted thin-knit top, a light pleated A-line mini skirt with one continuous hem. A breakfast shop, a steel counter, the wall menu out of focus. Cool daylight from the doorway, warm fluorescent light inside, the counter bouncing fill onto her chin. Her face clearly exposed with natural skin texture; the doorway is the brightest area, only its smallest highlights reaching white. Subtle film grain.
```

---

## 回覆區（請只填這一段）

### 疑慮：YG-09 濕髮的處理
- **判定**：REVISE
- **理由**：不列入硬驗收只能避免「濕髮沒出現」造成誤殺，不能消除該字串對髮型、髮長與畫面穩定性的干擾。LG-08 的 4/4 雖不能證明換角色後也必敗，但已是同一生成流程下足以採取避險措施的負面證據；在沒有本角色反證前，不宜把濕髮留在正式 prompt 再當 soft observation。
- **建議改法**：正式生成先刪除 `Wet`、`pushed straight back`、`water still beading at the ends`，改回角色可辨識的乾髮固定描述。若濕髮對敘事不可替代，另開單變因 preflight：同一 prompt 只比較乾髮／濕髮，各至少 2 張；在濕髮能保住長度、髮色與臉部一致性前，不併入正式批次。

### 疑慮：LG-07 複雜度
- **判定**：REVISE
- **理由**：全身本身不是問題；風險來自「骨盆明顯背離＋上身轉回四分之三＋雙臂把大桶抵到下巴」同時要求大幅軀幹扭轉與雙臂交疊，容易以腰部變形、肩臂錯位或多手來完成。現句的 `upper body turned three-quarters back` 也可能被理解成上身仍背對鏡頭，而不是轉向鏡頭。
- **建議改法**：把極端扭轉降成溫和三分之四背側站姿：`standing in a gentle three-quarter back pose, hips angled diagonally away, shoulders turned toward the camera`。桶改由兩手從左右托住、上緣停在下巴下，避免 `hugs ... with both arms` 形成手臂交疊。這件修後仍應先做 2 張 preflight，驗收順序先看肢體，再看骨盆／肩線方向。

### 疑慮：LG-01 近景放物件
- **判定**：REVISE
- **理由**：`at the lower edge` 只指定位置，沒有解決容量衝突。臉佔約 45%、雙肘落桌、雙手完整托腮後，畫面下緣剩餘空間不足以穩定辨識蛋糕與拿鐵兩件物品；模型很可能裁切物件、縮小臉，或擴成胸上景。已有 YG-01 同型失敗時，不應只換位置詞重試。
- **建議改法**：比照 YG-01，以近景與臉部表演為優先，從 prompt 與硬驗收③移除蛋糕、拿鐵；甜點店仍可由桌面、磁磚牆與窗邊座位成立。若兩件物品不可刪，必須把景別正式改成胸上／中近景並降低臉部占比，不能仍標「臉部＋肩膀近景」。

### YG-06
- **判定**：PASS ／ REVISE ／ BLOCK → PASS
- **理由**：盤腿全身、雙手共同捧杯、杯在下巴前與越過杯緣看鏡頭形成同一個可凍結瞬間；兩手沒有互相競爭的第二任務。坐姿全身也能同時容納赤腳與頭頂毛巾，不存在景別衝突。
- **建議改法**：可原樣送 preflight。驗收時「雙手」應指左右手各自接觸杯身，不接受多出的第三隻手或只剩單手持杯。

### YG-09
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：大特寫、畫外視線與均勻正面窗光彼此成立；但濕髮應依上方負面證據先退出正式 prompt。此外，`leans against the window frame` 可能誘發扶窗或摸臉的手勢，而硬驗收要求零隻手，現 prompt 只有靠裁切暗示，沒有直接鎖定。
- **建議改法**：移除濕髮三段，改用角色固定乾髮描述；在景別句補 `The crop contains only her face, hair, neck, and bathrobe collar, with both arms and hands below the frame.` 保留視線朝畫外與現行局部高光句。

### LG-01
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：雙手托雙頰的任務清楚，髮型與表情也可驗收；失敗點只在硬塞蛋糕與拿鐵造成近景容量矛盾。這會直接動搖臉占比與指定景別，不能以成品碰運氣。
- **建議改法**：採「近景優先」方案：刪除 prompt 的 `a strawberry cake and a latte at the lower edge`，硬驗收③改為只驗「臉佔畫面約 45%、臉部＋肩膀近景」。若企劃選擇食物優先，則須同步把景別與臉占比改成胸上中近景版本後再送。

### LG-06
- **判定**：PASS ／ REVISE ／ BLOCK → PASS
- **理由**：雙手共同捧開啟的扭蛋、低頭看扭蛋、閉眼笑是互相支持的同一瞬間；沒有「看鏡頭」殘留，也沒有第三個手部任務。半身足以容納胸前扭蛋與腰間外套。
- **建議改法**：可送 preflight。若成品管理規則不接受生成文字，再把 `bright shop signage` 換成 `bright pastel storefront lights`；此項不影響本次動作與構圖放行。

### LG-07
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：桶在下巴下、越過桶緣看鏡頭與全身構圖可以共存；需要修的是軀幹與雙臂的實現方式。現有大幅轉體加 `hugs ... with both arms` 容易產生肩腰變形、交疊手臂或額外手，尚不宜原樣送。
- **建議改法**：首句改為：`A young woman stands in a gentle three-quarter back pose, hips angled diagonally away and shoulders turned toward the camera. She supports a popcorn bucket from both sides with exactly two visible hands, its upper rim just below her chin, looking over the rim toward the camera with a playful smile.` 景別句把 `her feet near the lower third` 明確化為 `her complete feet visible within the bottom third of the frame`。修後先做 2 張肢體 preflight。

### LG-09
- **判定**：PASS ／ REVISE ／ BLOCK → REVISE
- **理由**：雙手共同捧杯、杯位、低頭抬眼與半身人食同框均成立；但半身 prompt 加入 `mini skirt with one continuous hem`，會要求模型展示通常落在裁切外的裙襬，容易把半身拉成膝上景。裙裝也不在本件硬驗收內，屬不必要的構圖競爭訊號。
- **建議改法**：刪除 `a light pleated A-line mini skirt with one continuous hem`，只保留半身可見的上衣描述。其餘動作與已修正的門口局部高光句可原樣送 preflight。

### 其他（只寫會導致生成失敗的項目）
- 無。
