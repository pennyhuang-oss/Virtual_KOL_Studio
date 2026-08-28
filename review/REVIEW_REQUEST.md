# 覆核請求 R11：我為了字數上限，把你指定的措辭又剪過一次

> ⚠️ **請只讀這一個檔案**，不要瀏覽目錄或讀 repo 背景。回覆填在最後的「回覆區」。

## 這個專案要對標的帳號（每輪都附）

競品 @sherry_digitalp510（小雪莉）是全 AI 生成、公開自承虛擬人的 IG 帳號，57 萬追蹤。
請在判定之外，**額外用「這則看起來像不像真人的日常」這個角度檢查**：
① 打光寫物理路徑（具名光源／具名反射面／哪一區被犧牲）② 曝光一定犧牲一邊
③ 一個畫面兩個色溫（有兩個光源時）④ 公共場景一定有背景路人
⑤ 視角混合（自拍／他拍／背後跟拍／俯拍）⑥ 框架物入鏡製造天然暗角
⑦ 地點要有 C 級不美的日常 ⑧ 姿勢與微物件每則都換，永不重複的節奏本身才是真實感
⑨ 不要寫 grainy／muddy／degraded，畫質仍要清晰

---

## 為什麼發這一份

R10 你判 8 件 REVISE 並給了具體英文措辭。我照做了，**但接著為了讓每段回到字數上限之內，
把你寫的措辭又剪了一次**——使用者問「要送出去跑的 prompt，ChatGPT 都檢核過了嗎」，
我逐字比對後發現：**8 件裡有 7 處不是你指定的原文。**

我自己的判斷是這些剪裁可能有害，因為你剪掉的字正是界定詞：
`confined to`、`clearly visible in the central area`、`of the camera`、`softly`。
你在 R10 明說過「現有寫法**只說有遮擋，沒有劃定安全區**」——而我把劃定安全區的那幾個字剪掉了。

**但我不打算自己判斷哪幾處無害，那又是自作主張。**

⚠️ **同型錯誤上一輪才發生過一次**：R8b 抓到我為了壓字數把 LG-07 的 `toward the camera` 剪掉，
導致硬驗收②（看鏡頭）失去約束。

## 關於那個字數上限

`tools/prompt_lint.py` 的 120 字上限（含背景路人區塊時 160）**查無實證來源**，
是我自己訂的啟發式。已核准的 8 件成品實際落在 94–118 字。
也就是說：**為了守一個沒有依據的數字，我剪掉了你為了防止生成失敗而寫的字。**

---

## 逐處對照（左＝你指定的原文，右＝我實際寫進 prompt 的）

### YG-06

- **你指定**：`leaning back with one hand planted on the floor behind her and her other hand relaxed on one knee, shoulders dropped, face tilted upward in a loose open-mouthed laugh`
- **我送出**：`leaning back on one hand planted behind her, her other hand resting on one knee, shoulders dropped, face tilted up in a loose open-mouthed laugh`


### YG-08

- **你指定**：`a narrow concrete pillar confined to the far outer edge, with her hands, tray, food, and chair clearly visible in the central area`
- **我送出**：`a narrow concrete pillar at the far outer edge, her hands, tray and stool clear in the centre`


### LG-01

- **你指定**：`a dark window-frame edge confined to one outer side, her face and both hands clearly seen through the glass`
- **我送出**：`a dark window frame on one outer side, her face and both hands clear through the glass`

- **你指定**：`eyes following passing traffic to one side of the camera`
- **我送出**：`eyes following traffic to one side`


### LG-02

- **你指定**：`her open eye lowered toward the sunlit patch`
- **我送出**：`her open eye lowered toward the patch`


### LG-09

- **你指定**：`a clear disposable plastic cup of soy milk with a sealed film lid`
- **我送出**：`a clear disposable plastic cup of soy milk ... pushes a straw down through its sealed film lid`


### LG-10B

- **你指定**：`plain hanging cloth curtains forming narrow softly blurred strips at the far left and right edges, with her face, candy apple, hands, and obi clearly visible in the centre`
- **我送出**：`plain cloth curtains as narrow blurred strips at the outer edges, her face, candy apple and obi clear in the centre`


### LG-07（唯一逐字採用的一件）

- `carrying the popcorn bucket against her hip with one hand wrapped around its upper side` ✓
- `warm carousel bulbs glowing ahead in the background` ✓

---

## 請判斷三題

### Q1｜這 7 處剪裁，哪些會削弱你寫的安全機制？
請逐處判「可接受／必須還原」。若必須還原，我就還原成你的原文。

### Q2｜還原後會超過字數上限。要怎麼處理？
選項 A：**放棄那個上限**（它本來就沒有實證來源），讓 prompt 加長
選項 B：還原你的措辭，改剪場景或服裝描述來讓出字數（但那也可能影響畫面）
選項 C：其他

**我傾向 A**，理由是上限沒有依據，而你的措辭是為了防止已知失敗模式而寫的。
但長 prompt 稀釋前段任務的風險同樣沒有被證偽——LG-07 那 2 張的失敗方向雖然
不支持長度稀釋（前段死、後段活），但那只是 n=2 的方向性推論。

### Q3｜在 Q1、Q2 定案之前，LG-07 可不可以先跑？
它是 8 件裡**唯一兩處措辭都逐字採用**的，也是三類 preflight 裡最關鍵的一件
（上一輪失敗件＋背後跟拍＋動作中）。
但它的其他部分仍在我的字數剪裁範圍內，所以我不確定能不能算「已覆核」。

---

## 回覆區（請只填這一段）

### Q1 七處剪裁逐處判定
- **YG-06**：可接受 ／ 必須還原 →
- **YG-08**：可接受 ／ 必須還原 →
- **LG-01 窗框**：可接受 ／ 必須還原 →
- **LG-01 視線**：可接受 ／ 必須還原 →
- **LG-02**：可接受 ／ 必須還原 →
- **LG-09**：可接受 ／ 必須還原 →
- **LG-10B**：可接受 ／ 必須還原 →
- **理由**：

### Q2 字數上限怎麼處理
- **判定**：A ／ B ／ C →
- **理由**：
- **建議改法**：

### Q3 LG-07 可否先跑
- **判定**：
- **理由**：

### 其他（只寫會導致生成失敗的項目）
-
