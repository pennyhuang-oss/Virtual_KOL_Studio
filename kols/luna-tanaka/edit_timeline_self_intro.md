# Luna Tanaka 自我介紹 — 剪輯時間軸

**主音軌：** `videos/self_intro/voiceover_luna.mp3`（目標 58 秒，日文+英文字幕）  
**背景音樂：** 日本傳統三味線 ambient（如 Haruka Nakamura 風格）— 壓低至 -20dB  
**格式：** 9:16，目標 58 秒  
**工具：** CapCut / Premiere Pro

> ⚠️ 進出點為**估算值**，請聽 voiceover 後按實際台詞時間微調。

---

## 影片 Track 順序

| 順位 | 檔案 | 估算進點 | 估算出點 | 用幾秒 | 對應 VO 台詞 |
|------|------|---------|---------|--------|------------|
| 1 | `shot01_window_light.mp4` | 0:00 | 0:05 | 5s | （無旁白，環境音：鳥聲、寺廟鐘聲） |
| 2 | `shot02_hands_camera.mp4` | 0:05 | 0:11 | 6s | *「私は田中ひな。京都に住んでいます。」* |
| 3 | `shot03_street_walk.mp4` | 0:11 | 0:17 | 6s | *「毎日、きれいなものを探しています。」* |
| 4 | `shot04_camera_flower.mp4` | 0:17 | 0:23 | 6s | *「急がないこと。それが私の哲学です。」* |
| 5 | `shot05_photos_table.mp4` | 0:23 | 0:28 | 5s | *「写真を撮るのは、記憶するためじゃなくて——」* |
| 6 | `shot06_face_reveal.mp4` | 0:28 | 0:32 | 4s | *「感謝するためです。」* |
| 7 | `shot07_mochi_cameo.mp4` | 0:32 | 0:37 | 5s | *「これは Mochi。批評家です。」*（輕笑） |
| 8 | `shot08_window_sitting.mp4` | 0:37 | 0:42 | 5s | *「もし、ゆっくりした世界を見たいなら——」* |
| 9 | `shot09_final_look.mp4` | 0:42 | 0:46 | 4s | *「ここにいます。」*（安靜點頭） |
| 10 | `shot10_fadeout_rooftop.mp4` | 0:46 | 0:50 | 4s | （無旁白，音樂淡出，畫面淡出至京都屋頂） |

**總時長：** 約 50s 畫面 + 淡出 ≈ **58 秒**

---

## 文字疊加（Text Overlay）

| 時間 | 文字 | 字體風格 |
|------|------|---------|
| 0:05–0:11 | `田中ひな / Kyoto` | 細線 serif，左下角，白字，很小 |
| 0:17–0:23 | `"Not rushing."` | 細英文斜體，中央 |
| 0:28–0:32 | `"to say thank you."` | 同字體，中央，漸入漸出 |
| 0:32–0:37 | `Mochi 🐱` | 手寫感字型，右下角，小 |
| 0:42–0:46 | `I'm here.` | 細英文，中央，最後停留 |
| 0:46–0:50 | `@luna.tnk` | 結尾字卡，極細白字 |

---

## 剪輯備注

- **全片節奏**：比一般 TikTok 慢 40%，每個 cut 之間用 0.5s 柔和淡入淡出，不用硬切
- **shot01（0:00–0:05）**：環境音（鳥聲、鐘聲）保留，音樂還沒進來，製造靜謐感
- **shot06（0:28–0:32）**：她第一次正面看向鏡頭是全片情感高點，不要急著切走
- **shot07 Mochi**：貓咪必須是自然走入畫面的，不能是擺拍，要保留那個意外感
- **shot09（0:42–0:46）**：說完「ここにいます」後有一個點頭的停頓——保留，不要剪
- **Color grade**：Kodak Portra 色調，暖白，輕微顆粒感，不要過度銳化

---

## CapCut 操作流程

1. 新建 9:16 專案，導入所有 `shot*.mp4` + `voiceover_luna.mp3`
2. 先放 VO 到音頻 track，標記每個台詞的開始點
3. 按照上表順序把 clips 拖進視頻 track，clip 之間設 0.5s 柔和轉場
4. 加三味線背景音樂，調到 -20dB
5. 加日文字幕 + 英文對照字幕，字體選細 serif（Google Fonts: Noto Serif JP）
6. Color grade：套 Kodak Portra 濾鏡，亮度 +5，色溫 +10（偏暖），顆粒感 +10

---

## 素材清單

```
kols/luna-tanaka/videos/self_intro/
├── voiceover_luna.mp3          ← 主 VO（待生成，日文）
├── shot01_window_light.mp4     ← 窗邊光影，無人，環境音
├── shot02_hands_camera.mp4     ← 手持底片相機，背景京都屋頂
├── shot03_street_walk.mp4      ← 從後面走在石板路上，Mochi 跟著
├── shot04_camera_flower.mp4    ← 蹲下對著路邊小花拍攝，非常認真
├── shot05_photos_table.mp4     ← 底片照片排在木桌上，手輕整理
├── shot06_face_reveal.mp4      ← 第一次正面看鏡頭，安靜微笑
├── shot07_mochi_cameo.mp4      ← Mochi 走過來坐在相機旁
├── shot08_window_sitting.mp4   ← 坐在窗邊翻照片，光打在側臉
├── shot09_final_look.mp4       ← 抬頭看鏡頭，不說話，輕輕點頭
└── shot10_fadeout_rooftop.mp4  ← 京都屋頂，慢慢淡出
```
