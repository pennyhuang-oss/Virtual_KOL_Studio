# Iris Chen 自我介紹 — 剪輯時間軸

**主音軌：** `videos/self_intro/voiceover_iris.mp3`（目標 50–58 秒）
**背景音樂：** 慵懶流行輕音樂（偏暖，有點隨性感，BPM 約 90）— 壓低至 -18dB
**格式：** 9:16，目標 55 秒
**工具：** CapCut / Premiere Pro

> ⚠️ 進出點為**估算值**，請聽 voiceover 後按實際台詞時間微調。

---

## 影片 Track 順序

| 順位 | 檔案 | 估算進點 | 估算出點 | 用幾秒 | 對應 VO |
|------|------|---------|---------|--------|---------|
| 1 | `shot01_mirror_outfit.mp4` | 0:00 | 0:05 | 5s | （無旁白）|
| 2 | `shot02_look_at_camera.mp4` | 0:05 | 0:09 | 4s | 「我叫 Iris，我住台北。」|
| 3 | `shot03_taipei_street_walk.mp4` | 0:09 | 0:14 | 5s | 「這是我每天的樣子。」|
| 4 | `shot04_cafe_window.mp4` | 0:14 | 0:18 | 4s | 「我很喜歡台北。」|
| 5 | `shot05_friends_street.mp4` | 0:18 | 0:23 | 5s | 「跟朋友出去是我最常做的事。」|
| 6 | `shot06_outfit_closeup.mp4` | 0:23 | 0:27 | 4s | 「然後就是穿的、去的、吃的。」|
| 7 | `shot07_cafe_coffee.mp4` | 0:27 | 0:31 | 4s | 「我不講什麼大道理。」|
| 8 | `shot08_walk_lookback.mp4` | 0:31 | 0:36 | 5s | 「就是台北，就是這樣過。」|
| 9 | `shot09_direct_camera.mp4` | 0:36 | 0:40 | 4s | （無旁白）|
| fadeout | — | 0:40 | 0:55 | 15s | 靜止畫面 + handle 淡出 |

**總時長：** 約 40s 畫面 + 15s 淡出 ≈ **55 秒**

---

## 文字疊加（Text Overlay）

| 時間 | 文字 | 字體風格 |
|------|------|---------|
| 0:05 | `@iris.chen` | 細字，右下角，白色 |
| 0:30 | `台北 📍` | 小字，左下角 |
| 0:52 | `追蹤一下` | 中央，簡潔白字 |

---

## 剪輯備注

- **shot01（0:00–0:05）**：無旁白開場，音樂直接進，讓換裝動作帶節奏——不說話，不解釋
- **shot02 → shot03**：直接切，不要轉場效果，節奏要乾淨
- **全片轉場**：硬切為主，最多 1 次淡入（留給最後 fadeout 就夠了）
- **shot09**：她直接看鏡頭不說話——讓這個靜默比旁白更有力量，不要加任何效果

---

## Color Grade

- 色溫偏暖（+10~+15）
- 高光輕微壓低，不要死白
- 輕微 film grain 疊加（VSCO A4 效果感）
- 飽和度略降（-5~-10），膚色保持暖調，不要過度冷

---

## CapCut 操作流程

1. 新建 9:16 專案，導入所有 `shot*.mp4` + `voiceover_iris.mp3`
2. 先放 VO 到音頻 track，聽完整遍，在各台詞位置打標記點
3. 按照上表順序把 clips 拖進視頻 track，對齊標記點裁剪
4. 加輕流行背景音樂，調到 -18dB（CapCut → 音頻 → 音量）
5. 加文字疊加，選無襯線細字（思源黑體 / Noto Sans TC，白色）
6. Color grade：套暖調 LUT 或手動調色溫 +12，輕 film grain

---

## 素材清單

```
kols/iris-chen/videos/self_intro/
├── voiceover_iris.mp3
├── shot01_mirror_outfit.mp4       ← 鏡前換裝，試第三件，歪頭比較，就這件
├── shot02_look_at_camera.mp4      ← 她轉頭直視鏡頭，嘴角微揚
├── shot03_taipei_street_walk.mp4  ← 大安區巷子，走過來，光線打在她身上
├── shot04_cafe_window.mp4         ← 窗邊坐著，咖啡，往外看
├── shot05_friends_street.mp4      ← 和朋友在街上，朋友說話，她在笑
├── shot06_outfit_closeup.mp4      ← 細肩帶 + mini skirt，台北街頭背景
├── shot07_cafe_coffee.mp4         ← 拿起咖啡喝，看向鏡頭
├── shot08_walk_lookback.mp4       ← 走著，回頭看鏡頭，自然表情
└── shot09_direct_camera.mp4       ← 直視鏡頭，不說話，嘴角小弧度
```
