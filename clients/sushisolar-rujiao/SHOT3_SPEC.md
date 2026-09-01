# 鏡 3｜Yuna 的 verdict（整支片唯一要生成人物的一鏡）

> 2026-09-01。規格由 R21 覆核裁決，逐字採用。未經 Penny 確認前不送生成。

## 一、🔴 R21 駁回了我的假設（先記這一條）

我在 R21 提出：**Yuna 帳號既有服裝全是貼身細肩帶，這可能是領口 4/4 失敗的第二層原因。**

**R21 判定：可列為待驗假設，不能列為已成立根因。** 三個理由：

> 1. soul_id 官方說法是鎖臉；**在沒有消融實驗前**，不能因 Yuna 已核准的四張恰好都是貼身／細肩帶，
>    就推論 embedding 一定把服裝 register 一起鎖入。**那四張也可能只是 prompt、選圖偏好
>    或既有企劃分布造成的選擇偏差。**
> 2. **先前 4/4 失敗發生在 Luna**，不足以證明 Yuna 的既有服裝會造成同一失敗。
>    兩件事可形成合理懷疑，但**不是同一角色上的對照實驗**。
> 3. 「表情綁實體動作」的證據**不能直接外推**成「衣服也必須綁實體」。

**但它仍然採用了具名衣物的寫法，理由跟我的不一樣、而且更準：**

> 「`mock-neck knit top` 是**模型可直接召回的完整物件**，
> 而 `upper chest fully covered` **只是要求結果**。」

**並且給了證偽條件**：若具名 mock-neck 在 12 張中**仍系統性**變成細肩帶／低領，
才把「soul 或模型先驗偏向既有 register」升格為有資料支持的假設。

## 二、🔴 我的色調量測被指出解讀錯了

我量了鏡 1（R/B 1.39）與鏡 2（R/B 2.07），主張「以實拍定色溫沒有唯一解」。

> 「**R/B 均值同時受畫面內容影響**：鏡 1 有大量黑背景與白碗，鏡 2 有整隻金黃雞與大面積暖蒸氣。
> 它能證明兩鏡**觀感不同**，卻**不是可直接拿來指定色溫的尺度**。」

**這是我第三次犯同一形狀的錯：拿一個全域統計量去推論一個特定屬性。**
（第一次：用音軌 RMS 平坦推論「聲音不同步」。第二次：這個。）
**分區量測＋對照組是對的（鏡 2 的蒸氣亮度與運動量測就成立）；全畫面平均不是。**

### 色調的正解

**鏡 3 不對鏡 1、也不對鏡 2，更不做數值平均。**
生成一個**暖而中性、膚色自然、亮暗有餘量的 bridge master**，四鏡粗剪後再統一調色。

> 「**人臉是四鏡中對偏色最敏感的物件。**若生成時就追到鏡 2 的 2.07 暖度，後製很難救回皮膚。」
> 「Prompt 只指定**物理光路**：暖琥珀燈籠光作主光，淺色桌面回一層**較中性**的柔和補光，
> 下方鍋區落入深暗。這會得到**可調的**雙色溫與曝光犧牲，而不是一層橘色濾鏡。」

**後製順序**：各鏡先校正白平衡／曝光 → 再套同一個暖金 look → 最後按相鄰剪接微調。
**不要先把鏡 3 烤死成任一現有鏡的數值。**

## 三、Step 1 — start frame（`soul_2`）

```
model         soul_2
soul_id       235794a5-2eff-45fb-91b4-3232910afefa   （Yuna Kim）
quality       2k
aspect_ratio  9:16
```
**0.12 credits／張。**

### Prompt（R21 逐字指定，210 字）

```
Yuna sits at a hotpot table immediately after tasting the first bowl of broth. The viewer is seated directly across the table from her. Her complete head, both shoulders, neckline, and upper torso are visible, with the broad rim of a white porcelain bowl spanning the bottom centre of the frame and both hands below the frame. Her chin is slightly lowered and her eyes are fixed on the clearly visible bowl rim, lips softly closed in a quiet moment of judgment. Deep brown to near-black naturally wavy hair falls with airy, irregular bends around her shoulders, paired with polished natural Korean-style makeup and clean luminous skin. She wears an opaque ivory mock-neck knit top with relaxed shoulders, its collar forming one continuous band around the base of her neck. A warm Chinese hotpot restaurant surrounds her, with a carved wooden screen, amber lanterns, and two indistinct diners in the mid-ground facing their own table. An amber lantern above and to her left lights her face, while the pale stone tabletop returns a softer neutral-gold fill under her jaw. Her face and neckline are clearly exposed; the lower foreground pot edge falls into deep shadow, and the lanterns form the brightest highlights. Clear natural skin texture and fine hair detail.
```

### 每一句在做什麼

| 句 | 作用 |
|---|---|
| 1 | 只建立已完成的前情「喝完第一碗」，**不生成入口、吞嚥或咀嚼** |
| 2 | **用可想像的場景關係建立正面機位**（「觀眾坐在她正對面」），不依賴已知可能無效的攝影術語，也不命令她先看鏡頭 |
| 3 | 列出必須看得見的東西（頭、雙肩、領口、上半身、碗緣在下方中央、**雙手在畫面外**） |
| 4 | 低眼、視線鎖在**畫面內夠大的碗緣**、唇自然閉合 |
| 5 | 髮（深棕近黑、自然不規則波浪、空氣感）＋韓系自然妝＋乾淨透亮膚質 |
| 6 | **服裝：具名實體 `an opaque ivory mock-neck knit top`＋一個辨識幾何「領圈在頸根形成連續一圈」。不再堆疊三句同義覆蓋宣告** |
| 7 | 場景：雕花木屏、琥珀燈籠、**兩個模糊食客面向自己那桌**（公共場景紋理） |
| 8 | 光的物理路徑：左上琥珀燈籠為主光，**淺色石桌回一層較中性的補光** |
| 9 | 曝光取捨：臉與領口可判讀，**下方鍋緣落入深暗**，燈籠是最亮處 |
| 10 | 皮膚紋理與髮絲細節 |

## 四、Step 2 — 動畫（`kling3_0`）

**運動預算**：
- **主運動＝視線轉移**：先在碗緣停一拍，再抬眼看向正對面的觀眾（允許極小幅抬下巴）
- **次運動＝眼神到位後，一次極小、受控的點頭**，隨即回穩
- 呼吸、頭髮、背景食客、燈籠、碗、衣服**全部列為穩定狀態**

```
From the locked frontal close-up, she holds her lowered gaze on the white bowl rim for one quiet beat, then raises her gaze with a slight lift of her chin to meet the viewer directly across the table. After her eye contact settles, she gives one very small, controlled nod and returns to a composed still posture, her lips softly closed. Her face, mock-neck collar, shoulders, hair, bowl rim, table, background diners, and lighting maintain their original shapes and positions. The warm lantern key light and softer neutral-gold tabletop fill remain steady while the lower foreground stays in deep shadow. Quiet restaurant room tone.
```

| 段 | 作用 |
|---|---|
| 1 | 完成「低眼停拍 → 抬眼」的主運動。**不是一開始就直視**，不加微笑或說話 |
| 2 | 點頭放在 eye contact **已成立之後**，避免模型同時抬眼＋點頭做成大幅仰頭。明寫**一次、很小、完成後穩定** |
| 3–4 | 鎖住領口、頭髮、碗、背景與曝光。**特別防衣服在點頭時變領型、背景食客被放大、燈籠閃爍** |
| 5 | 聲音只給安靜 room tone |

> **Yuna 的「이거 진짜 좋아——這個真的好」一律後製畫外音，
> 不讓 Kling 生成嘴型或語音。畫面中的嘴全程閉合。**

## 五、Step 3 — 生成節奏與停損（R21 指定）

**12 張 start frame，分兩批 6 張，中間有一個決策點——不直接連續送 Kling。**

| 步 | 做法 |
|---|---|
| 1 | 先用**完全相同的 prompt** 生 **6 張**，依第六節硬 gate 記錄通過率與**失敗類型** |
| 2 | 若已有**至少 2 張完整通過** → 不改 prompt，再生同版 6 張，從 12 張中選**一張主片＋一張備援** |
| 3 | 若前 6 張**全部只敗在同一個服裝 register** → **不要把後 6 張浪費在同一抽樣**。保留這 6 張作證據，改走「已核准服裝參考圖」的靜態單變因測試或直接靜態修圖 |
| 4 | 若前 6 張是**分散的隨機小瑕疵**、但有接近合格者 → 維持原 prompt 補到 12 張 |

**總 start-frame 預算上限 12 張／1.44 credits。**

### 三層停損

| 層 | 條件 | 處置 |
|---|---|---|
| **服裝層** | 6 張全生成細肩帶／低領／蕾絲，且臉與構圖大致正確 | 判定「**prompt-only 服裝控制不通**」，立即改服裝參考圖 A/B 或靜態修圖。**不再寫第五組領口同義句** |
| **start-frame 層** | 做到 12 張仍沒有任何一張同時通過五個核心 gate（Yuna 臉／mock-neck／低眼看碗／可見領口／零可見手） | 判定這一鏡**不能靠純 soul_2 抽卡完成**，停止新增圖片 |
| **動畫層** | 兩支 Kling 都重複改臉／改衣服／產生肢體，或始終沒有連續 4 秒可用窗 | 判定**人物 i2v 路線不通**，不再花第三支 10 credits |

**最終替代方案**：用通過或已修好的 Yuna 靜態圖做 2.5D 微推＋後製 verdict 畫外音；
若連合格靜態圖都沒有，**取消人物鏡**，改用鏡 2 的產品尾段＋Yuna verdict 字卡／聲音銜接鏡 4。

> **不能用低領、錯臉或錯視線版本硬湊客戶成片。**

## 六、我挑圖時要逐項確認的清單（R21 Q4，這是我特別要求的）

### A. 硬 gate — 任何一項不過即淘汰

- [ ] **臉是 Yuna**：眼型、鼻、嘴、臉型、年齡感與 soul_id 既有臉一致，**不只是「漂亮的陌生韓系女生」**
- [ ] **只有一個人物主體**：無第二張臉、鏡面人臉、肩後多出肢體、與背景食客融合
- [ ] **完整頭部、雙肩、領口、上半身都可見**；不得用近裁／頭髮／碗／暗部遮掉**領口驗收區**
- [ ] **衣服確實是象牙色 mock-neck knit top**：領圈在頸根形成連續一圈，上胸由同一件不透明布料覆蓋
- [ ] **淘汰任何低領、V 領、細肩帶、蕾絲領、開襟露胸線、透明布、胸口挖空或假領片——即使臉最好看**
- [ ] **衣服場合成立**：不像睡衣、內衣、泳裝、禮服或厚重戶外高領
- [ ] **視線明確落在畫內白瓷碗緣**，不是看鏡頭／看畫外／閉眼／兩眼方向不一致
- [ ] **碗緣夠大且位置明確**：下方中央、單一白瓷碗；不得複製、融化、長出字、變成盤子
- [ ] **嘴唇自然閉合**：無喝湯、吞嚥、咀嚼、吸管、食物入口或說話嘴型
- [ ] **畫面內可見手的數量為 0**：無指尖、筷子、湯勺或不明肢體從邊緣伸入
- [ ] **五官與牙齒無結構瑕疵**：無大小眼失控、瞳孔錯位、嘴角熔化、不自然牙齒、皮膚塑膠化
- [ ] **頭髮符合設定**：深棕至近黑棕、自然不規則波浪、有空氣感；**不是金髮、筆直黑長髮、規整電棒捲或濕髮**
- [ ] **妝感自然精緻**：無過重煙燻、誇張假睫毛、亮片；膚色未被推成灰白或橘黃
- [ ] **正面關係成立**：觀眾在桌子正對面，雙肩沒變成正側面或背面；同時低眼視線仍清楚
- [ ] **曝光符合規劃**：臉、眼睛、領口可判讀；下方鍋區可暗，**但不能反過來讓臉陷入黑影**
- [ ] **色彩可調**：膚色仍有中性資訊，象牙衣物與白瓷碗未整片黃爆或高光剪死
- [ ] **場景像餐廳而非棚拍**：至少有雕花木屏／燈籠等具體線索，背景有少量合理食客
- [ ] **背景不搶主體**：食客沒看鏡頭，無清楚陌生人臉、亂碼菜單、假 logo、可讀偽文字
- [ ] **9:16 安全區成立**：頭頂、髮尾、雙肩與碗緣沒貼死裁切線，**後續小幅點頭仍有活動空間**
- [ ] **沒有時間矛盾**：看起來是「已喝完、正在判斷」，不是「還沒喝」「正準備喝」「正在端碗」

### B. 通過硬 gate 後才比優先級

1. **臉部一致性＋服裝合規**（**高於單純好看**）
2. 低眼視線與碗緣關係一眼看懂，可直接支撐後續抬眼
3. 膚色、暖光與暗部有後製餘量，能接鏡 2 而不必重度校色
4. 表情克制、有「正在下結論」的停頓——**不選甜笑、驚訝張嘴或業配式比讚**
5. 兩張同分 → 選**頭髮、領口、背景邊緣最穩定**的，**不選妝最重或光最夢幻的**
6. **保留原圖、prompt、生成批次與淘汰理由**；不能只存「最好看」的一張而失去抽樣證據

## 七、R21 補充的四點

| # | 內容 |
|---|---|
| 1 | **鏡 3 不是用來再次證明產品**。鏡 1、2 已完成湯與整雞的證據。**鏡 3 的碗只作視線錨點，不能讓 AI 再畫金黃湯、花膠、筷子或蒸氣**，否則把已由實拍建立的可信度重新交給生成模型 |
| 2 | **背景食客在動畫中也可能被放大**。start frame 可有兩個低細節食客作公共場景紋理，但已列入穩定狀態。**若動畫讓食客轉頭看鏡頭、靠近 Yuna 或長出清晰人臉，即硬 FAIL** |
| 3 | **旁白時序要配動作，不配嘴型**。verdict 應在她抬眼完成、點頭開始前後進入。**若旁白先說完她才抬眼，會失去「先判斷再下結論」的節奏** |
| 4 | **統一調色要在四鏡粗剪後做**，不要只看三張單獨截圖。把鏡 1→2→3→4 排在同一時間線，以**膚色、白瓷碗、象牙衣物、櫻花粉**四個檢查點定共同暖金 look |
