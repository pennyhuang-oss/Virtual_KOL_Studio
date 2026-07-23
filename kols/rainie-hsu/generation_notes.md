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

> 以下 4 個批次為建議的訓練圖／素材拍攝規劃，供之後實際送入生成平台時使用。**目前皆未生成，無 job ID、無 media ID、無已選圖片**。

### 批次規劃 1 — 浴室化妝台特寫（貓眼眼線特寫）

**場景描述**：化妝台前近景，正在畫貓眼眼線，眼神專注在鏡子細節，展現她招牌的妝容技術。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, sculpted brow, precise winged cat-eye eyeliner mid-application, eyeliner brush in hand, bold red statement lip, glossy jet-black long straight hair, close-up at vanity mirror, wearing thin black camisole, focused expression on her own reflection not at camera, warm vanity bulb lighting, high contrast tones, film grain, candid nightlife photo, shot on 35mm, Instagram style
```

---

### 批次規劃 2 — 全身鏡前換裝定裝照

**場景描述**：全身鏡前，試穿貼身洋裝，轉身看背面剪裁，出門前最後一套的定裝時刻，直視鏡頭。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, precise winged cat-eye eyeliner, bold red statement lip, glossy jet-black long straight hair, striking hourglass figure with full bust and cinched waist, standing in front of full-length mirror, wearing fitted black bodycon dress with thigh-high slit, confident direct gaze at camera through mirror reflection, high heels visible, warm apartment lighting mixed with phone flash energy, full body shot, high contrast saturated tones, film grain, candid nightlife photo, shot on 35mm, Instagram style
```

---

### 批次規劃 3 — 夜店 / 酒吧入口全身照

**場景描述**：抵達夜店或酒吧門口，全身入鏡，霓虹燈光氛圍，走進場地前的那一刻定格。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, precise winged cat-eye eyeliner, bold dark statement lip, glossy jet-black long straight hair, striking hourglass figure, standing at club or bar entrance in Taipei nightlife district, wearing corset top and high-slit mini skirt with statement heels, confident poised stance, full body shot, neon club lighting spill mixed with street lighting, high contrast cool-toned with warm skin highlight, film grain, candid nightlife photo, shot on 35mm, Instagram style
```

---

### 批次規劃 4 — 出門造型 Reveal（近景+全身雙版本）

**場景描述**：出門前最後一眼，鏡頭從高跟鞋帶到全身再到臉部特寫，完整的「今晚就是這套」造型揭曉時刻。

**草稿 Prompt**：
```
24-year-old Taiwanese woman, sharp striking facial features, high cheekbones, defined sharp jawline, sculpted brow, precise winged cat-eye eyeliner, bold red statement lip, glossy jet-black long straight hair worn sleek with deep side part, striking hourglass figure with full bust and curved hips, standing by apartment doorway ready to leave, wearing sleek bodycon dress with statement jewelry and sky-high heels, direct confident gaze at camera, full body reveal shot, warm entryway lighting with hint of golden hour spill through door, high contrast saturated tones, film grain, candid nightlife photo, shot on 35mm, Instagram style
```

---

## 建議生成流程（規劃，尚未執行）

> 以下為建議流程，供實際開始生成時參考，並非已完成的步驟記錄。

1. 建議先用同一組核心 prompt 結構，於候選圖片模型（可參考 Iris Chen 案例中 Seedream 4.5 對亞洲臉孔的表現）產出上述 4 個批次的候選圖，每批次 2–4 張
2. 挑選臉部與身材一致性最佳的圖片，確認符合「銳利立體、非可愛系」的臉型設定後，再進入 Soul 訓練階段
3. Soul 訓練完成後才建立 soul_id，並回填至本文件；訓練前不填入任何 ID
4. 影片素材生成需等待 Soul 訓練完成，且需遵守 `content_style.md` 中訂立的燈光、角度與剪輯節奏規範

---

## 尚未執行事項清單

- [ ] 批次規劃 1–4 尚未送出生成
- [ ] 尚無 Soul 訓練、尚無 soul_id
- [ ] 尚無任何已生成圖片或影片檔案
- [ ] 尚無模型選擇的實測結論（例如 Seedream vs. 其他模型對此臉型設定的適配度）
