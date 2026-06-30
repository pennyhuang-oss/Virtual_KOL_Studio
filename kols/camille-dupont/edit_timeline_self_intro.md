# Camille Dupont 自我介紹 — 剪輯時間軸

**主音軌：** `videos/self_intro/voiceover_camille.mp3`（目標 60 秒，法文）
**背景音樂：** 法式 chanson（Françoise Hardy 或 Serge Gainsbourg 風格）— 壓低至 -18dB，比環境音稍大聲
**格式：** 9:16，目標 60 秒
**工具：** CapCut / Premiere Pro

> ⚠️ 進出點為**估算值**，請聽 voiceover 後按實際台詞時間微調。全片光源只用自然光，不補燈。

---

## 影片 Track 順序

| 順位 | 檔案 | 估算進點 | 估算出點 | 用幾秒 | 對應 VO 台詞 |
|------|------|---------|---------|--------|------------|
| 1 | `shot01_cutting_onion.mp4` | 0:00 | 0:05 | 5s | （無旁白，切菜聲，遠處巴黎街道聲，發夾快要掉）|
| 2 | `shot02_looks_up.mp4` | 0:05 | 0:10 | 5s | *「Je m'appelle Camille. Je suis à Paris.」* |
| 3 | `shot03_oil_and_onion.mp4` | 0:10 | 0:16 | 6s | *「Je fais des vidéos de cuisine. Pas de la haute cuisine —」* |
| 4 | `shot04_turn_deadpan.mp4` | 0:16 | 0:22 | 6s | *「de la vraie cuisine. Celle que les Français font chez eux.」* |
| 5 | `shot05_wine_pour.mp4` | 0:22 | 0:28 | 6s | *「Mon père m'envoie le vin de Lyon. C'est mieux.」* |
| 6 | `shot06_wine_sip.mp4` | 0:28 | 0:33 | 5s | *「Je suis aussi à la Sorbonne. En littérature.」* |
| 7 | `shot07_plate_food.mp4` | 0:33 | 0:38 | 5s | *「Mais c'est surtout pour ça que je suis là.」* |
| 8 | `shot08_window_gaze.mp4` | 0:38 | 0:44 | 6s | *「Manger bien. Vivre bien. Pas plus compliqué.」* |
| 9 | `shot09_hairclip_joke.mp4` | 0:44 | 0:49 | 5s | *「La pince dans mes cheveux va tomber. C'est normal.」* |
| 10 | `shot10_fadeout.mp4` | 0:49 | 0:53 | 4s | （無旁白，她轉頭看窗外，音樂淡出） |

**總時長：** 約 53s 畫面 + 淡出 ≈ **60 秒**

---

## 文字疊加（Text Overlay）

| 時間 | 文字 | 字體風格 |
|------|------|---------|
| 0:00–0:05 | `Paris. Dimanche matin.` | 細斜體，右下角，白字 |
| 0:05–0:10 | `Camille Dupont @camille.dpnt` | 細 sans-serif，左下角 |
| 0:16–0:22 | `"not haute cuisine. real cooking."` | 細英文斜體，中央 |
| 0:22–0:28 | `Lyon wine from her father 🍷` | 手寫感，右下角，小 |
| 0:38–0:44 | `"manger bien. vivre bien."` | 細斜體，中央，漸入漸出 |
| 0:44–0:49 | `"La pince va tomber. C'est normal."` | 細斜體，中央 |
| 0:49–0:53 | `@camille.dpnt` + `Les Invités 🥖` | 結尾字卡，米白底色 |

---

## 剪輯備注

- **全片只用自然光**：廚房窗光是唯一光源，這是 Camille 的視覺法則——不補燈
- **shot01（0:00–0:05）**：鏡頭從手（切洋蔥）慢慢 pan 到她的臉，發夾快掉的狀態要清楚可見，音樂從這裡進，環境音（切菜聲、街道聲）保留底層
- **shot04**：她轉頭看鏡頭的表情是完全 deadpan——「就是這樣」，不解釋，不邀請，節奏放慢讓這句話落地
- **shot05**：她給自己倒酒完全自然，不解釋——讓觀眾自己理解這是她的日常
- **shot08（0:38–0:44）**：她看著窗外，不看鏡頭——這是全片情感上最重的時刻，鏡頭不要晃，讓她的側臉靜靜說話
- **shot09（0:44–0:49）**：最後那句關於發夾的話是全片唯一的幽默——要說得完全不當一回事，這是法式 deadpan 的精髓
- **全片轉場**：柔和淡入淡出，不用硬切，節奏比一般 TikTok 慢 20%
- **英文字幕**：全程顯示，字型選細 serif（Google Fonts: Playfair Display），不要粗體

---

## Color Grade

- 暖米色調，微微去飽和（-10）
- 高光保留窗邊光的柔亮，不死白
- 食物顏色真實，不過度飽和
- 皮膚保留自然暖調，不磨皮

---

## CapCut 操作流程

1. 新建 9:16 專案，導入所有 `shot*.mp4` + `voiceover_camille.mp3`
2. 先放 VO 到音頻 track，標記發夾台詞位置、品嘗停頓、CTA 位置
3. 按照上表順序拖 clips，clip 之間設 0.3s 柔和淡入淡出
4. 加法式 chanson 背景音樂，調到 -18dB
5. 加法文字幕 + 英文對照字幕，字體選細 serif（Playfair Display）
6. Color grade：套暖米色 LUT，飽和 -10，色溫 +8，高光 -5

---

## 素材清單

```
kols/camille-dupont/videos/self_intro/
├── voiceover_camille.mp3         ← 主 VO（待生成，法文）
├── shot01_cutting_onion.mp4      ← 手切洋蔥，鏡頭 pan 到臉，發夾快掉
├── shot02_looks_up.mp4           ← 她抬頭看向鏡頭，平靜，嘴角微揚
├── shot03_oil_and_onion.mp4      ← 繼續做菜，把洋蔥倒進鍋裡
├── shot04_turn_deadpan.mp4       ← 轉頭看鏡頭，完全 deadpan
├── shot05_wine_pour.mp4          ← 倒一杯葡萄酒，完全自然，不解釋
├── shot06_wine_sip.mp4           ← 喝了一口，閉眼一秒，繼續做菜
├── shot07_plate_food.mp4         ← 把菜盛進有點缺角的舊陶盤，窗邊擺盤
├── shot08_window_gaze.mp4        ← 坐在窗邊，手拿酒杯，看向窗外的巴黎
├── shot09_hairclip_joke.mp4      ← 轉回鏡頭，輕描淡寫說發夾快掉了
└── shot10_fadeout.mp4            ← 又轉頭看窗外，音樂淡出
```
