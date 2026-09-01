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

<!-- PROMPT_ID: shot3_startframe_v1_RETIRED | FP: - | REVIEW: R21（已被 R22 取代，2/2 失敗，不得再送） -->
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

<!-- PROMPT_ID: shot3_anim_v1_RETIRED | FP: - | REVIEW: R21（設計已變更：放棄低眼，改為只做點頭。不得再送） -->
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

> **⚠️ 2026-09-01 Penny 改為「先 2 張」，覆蓋 R21 的 6 張。**
> R21 訂 6 張是因為**它不知道這個專案有成本限制**——我從沒在覆核請求裡寫過這件事。
> **prompt 完全不動，只改批量。**

**先生 2 張。用的是本專案既有的「生成 2 選 1」分流規則：**

| 2 張的結果 | 下一步 |
|---|---|
| 兩張都通過領口等硬 gate | 挑較好的一張，**收工**（成本 0.24） |
| **兩張都敗在同一個服裝 register** | **已達既有的「兩張同方向失敗＝系統性」門檻**，直接走服裝參考圖／靜態修圖，**不再抽卡** |
| 結果混雜（各敗在不同 gate） | 才需要更多樣本來看分布，再補到 4–6 張 |

**R21 原本的 6＋6 設計保留在下方作為上限參考，但預設不執行。**

---

<details><summary>R21 原始設計（12 張分兩批，預設不執行）</summary>

| 步 | 做法 |
|---|---|
| 1 | 先用**完全相同的 prompt** 生 **6 張**，依第六節硬 gate 記錄通過率與**失敗類型** |
| 2 | 若已有**至少 2 張完整通過** → 不改 prompt，再生同版 6 張，從 12 張中選**一張主片＋一張備援** |
| 3 | 若前 6 張**全部只敗在同一個服裝 register** → **不要把後 6 張浪費在同一抽樣**。保留這 6 張作證據，改走「已核准服裝參考圖」的靜態單變因測試或直接靜態修圖 |
| 4 | 若前 6 張是**分散的隨機小瑕疵**、但有接近合格者 → 維持原 prompt 補到 12 張 |

**總 start-frame 預算上限 12 張／1.44 credits。**

</details>

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

---

# 八、第一批實測（2026-09-01，2 張，0.24 credits）

job `4ea22154`（A）／`7738f9b3`（B），1152×2048。
`transactions` 逐筆 −0.12 ×2，與預期相符。

## 逐張對 20 條硬 gate

| gate | A | B |
|---|---|---|
| 臉是 Yuna | ✅ | ✅ |
| 只有一個人物主體 | ✅ | ✅ |
| 頭／肩／領口／上半身可見 | ✅ | ✅ |
| **象牙色 mock-neck，領圈在頸根一整圈** | **✅ 完全正確** | **❌ 變成「獨立頸環＋下方大圓領」，胸口外露** |
| 淘汰低領／V 領／細肩帶 | ✅ | **❌** |
| 衣服場合成立 | ✅ | ✅ |
| **視線落在畫內碗緣** | **❌ 直視鏡頭** | **❌ 直視鏡頭** |
| **碗緣夠大、在下方中央** | **❌ 整碗湯被舉在胸前** | **❌ 同** |
| 嘴唇自然閉合 | ✅ | ✅ |
| **畫面內可見手＝0** | **❌ 雙手捧碗** | **❌ 雙手捧碗＋湯匙** |
| 五官無結構瑕疵 | ✅ | ✅ |
| 頭髮符合設定 | ✅ | ✅ |
| 妝感自然 | ✅ | ✅ |
| 正面關係成立 | ✅ | ✅ |
| 曝光符合規劃 | ✅ | ✅ |
| 色彩可調 | ✅ | ✅ |
| 場景像餐廳 | ✅ | ✅ |
| **背景無偽文字** | **❌ 背景招牌有亂碼韓文字** | ✅ |
| 9:16 安全區 | ✅ | ✅ |
| **無時間矛盾** | **❌ 正在端碗** | **❌ 同** |

## 🔑 診斷：四個失敗其實是同一個根因

**2/2 同方向失敗的有四項**：視線看鏡頭、雙手捧碗、碗被畫成一整碗湯、時間矛盾（正在端碗）。

**但它們不是四個獨立問題，是一個：**

> prompt 寫的是
> `the broad rim of a white porcelain bowl spanning the bottom centre of the frame`
> （碗緣橫跨畫面下方中央）。
> **模型把它讀成「她正在端一碗湯給你看」**，而不是「桌上有個碗、只露出碗緣」。

一旦模型決定她在端碗，後面三項是**必然的連鎖**：
端碗需要手 → 手就進畫面 → 端碗給人看的人自然看鏡頭 → 於是變成「正要端上桌」而不是「已喝完」。

**所以要改的是碗那一句，不是四個地方。**

### 附帶發現：`both hands below the frame` 這種寫法可能無效

這是在指定「某個東西不在畫面裡」——**形式上接近否定句**，而 D-05 已驗證否定句無效。
2/2 都出現雙手，與這個推測一致。

## 🎯 服裝：具名衣物寫法 1/2 成功，這是重要的正面結果

**A 張的 mock-neck 完全正確**——象牙色、領圈在頸根形成連續一圈、上胸被同一件不透明布料覆蓋。

對照先前 Luna 的領口**連續 4 次全失敗**（`fastened through the chest` → 三重領口幾何宣告），
**這是第一次用一句話就拿到正確領口。**

R21 的說法得到支持：
> 「`mock-neck knit top` 是**模型可直接召回的完整物件**，而 `upper chest fully covered` **只是要求結果**。」

**B 張的失敗方式也很有資訊**：它把 `collar forming one continuous band around the base of her neck`
**畫成一個獨立的頸環**，下面配大圓領。
→ 「一整圈」這個幾何描述**可以被拆離衣服本體**。具名衣物有效，但補充的幾何描述可能反而製造第二個物件。

## 處置

依本專案既有分流規則：**兩張同方向失敗＝系統性，停下來改 prompt，不要再抽卡。**

- **不生第 3、第 4 張**（R21 的 6 張批量在此無意義——失敗不是隨機的）
- **服裝層停損未觸發**（A 已證明寫法可行），**不需要走服裝參考圖路線**
- **要改的是碗那一句**，以及可能無效的 `both hands below the frame`
- **prompt 要改 → 必須送覆核**（R22）

---

# 九、第二版 start frame（R22 逐字裁決）

## 它照做了「不要重寫整段」

**只改 4 句，其餘逐句列出「原封不動」。** 我逐字驗證過：

| 檢查 | 結果 |
|---|---|
| `an opaque ivory mock-neck knit top`（受保護的突破字串） | ✅ 原封不動 |
| 開頭兩句、髮妝句、打光句、曝光句、質感句 | ✅ 原封不動 |
| `both hands below the frame` | ✅ 已刪 |
| `the broad rim of a white porcelain bowl spanning the bottom centre of the frame` | ✅ 已刪 |
| `its collar forming one continuous band around the base of her neck` | ✅ 已刪 |

v1 210 字 → v2 **221 字**。

## 🔑 最有價值的一條：手不入鏡的正解

**這解決了 D-05 一直沒回答的問題——否定句無效，那要排除東西時該怎麼寫？**

| | |
|---|---|
| ❌ v1 | `both hands below the frame`——**只描述不可見結果**，被更強的「端碗」場景語意覆蓋。2/2 失敗 |
| ❌ 我想到的替代 | 「雙手放腿上」——**仍然把注意力叫到兩隻手**，位置不可驗收，可能反向生成膝上手或拉遠景別 |
| ✅ R22 | `the lower frame edge crosses both upper arms above the elbows`——**描述畫面內確實可見的裁切邊界** |

> 「**手不需要被生成後再藏起來；構圖本身在手腕／手掌出現以前就結束。**」

**已寫成通則 `SEXY_SCENE_LIBRARY.md` §24-F。⚠️ n=0，這批就是它的第一次驗證。**

## 四處改動

| 原句 | 新句 | 為什麼 |
|---|---|---|
| `the broad rim of a white porcelain bowl spanning the bottom centre of the frame and both hands below the frame` | `the lower frame edge crosses both upper arms above the elbows, while the near rim of a small empty white porcelain tasting bowl rests flat on the pale stone tabletop in the extreme foreground` | 「被端起展示的大碗」→ **有桌面承重的小型空碗**；不可見的 hands 指令 → **可見的裁切幾何** |
| `her eyes are fixed on the clearly visible bowl rim` | `her eyes are fixed on the near rim of the tasting bowl resting on the tabletop` | **再次綁定桌面**，防止視線句把碗重新升格成胸前展示物 |
| `...knit top with relaxed shoulders, its collar forming one continuous band around the base of her neck.` | `...knit top with relaxed shoulders.` | 保留已成功的具名衣物，**刪除可能被拆成獨立 choker 的幾何補充** |
| `...a carved wooden screen, amber lanterns, and two indistinct diners...` | `...a carved wooden screen, plain continuous dark-wood wall panels, amber lanterns, and two indistinct diners...` | **用連續深木牆面正向占據招牌生成位置**，降低隨機偽文字風險（不寫 no text） |

## 碗那一句為什麼這樣改就不會被讀成「端著」

> ① `rests flat on the pale stone tabletop` 給碗**唯一、明確的承重表面**；它不再需要人物的手來解釋位置
> ② `small empty tasting bowl` 定義成**已喝完後留下的小碗**，不是盛滿配料、準備展示的大碗
> ③ `near rim…in the extreme foreground` 只要求**一段夠大、有邊界與對比的碗緣**作視線錨點，不再要求整個碗橫跨中央搶成主體
> ④ `the lower frame edge crosses both upper arms above the elbows` **用人體與裁切的正面幾何關係排除端碗姿勢**

## v2 Prompt（R22 逐字指定，221 字）

<!-- PROMPT_ID: shot3_startframe_v2 | FP: sha1:b54275c37ef4 | REVIEW: R22 逐字指定 -->
```
Yuna sits at a hotpot table immediately after tasting the first bowl of broth. The viewer is seated directly across the table from her. Her complete head, both shoulders, neckline, and upper torso are visible; the lower frame edge crosses both upper arms above the elbows, while the near rim of a small empty white porcelain tasting bowl rests flat on the pale stone tabletop in the extreme foreground. Her chin is slightly lowered and her eyes are fixed on the near rim of the tasting bowl resting on the tabletop, lips softly closed in a quiet moment of judgment. Deep brown to near-black naturally wavy hair falls with airy, irregular bends around her shoulders, paired with polished natural Korean-style makeup and clean luminous skin. She wears an opaque ivory mock-neck knit top with relaxed shoulders. A warm Chinese hotpot restaurant surrounds her, with a carved wooden screen, plain continuous dark-wood wall panels, amber lanterns, and two indistinct diners in the mid-ground facing their own table. An amber lantern above and to her left lights her face, while the pale stone tabletop returns a softer neutral-gold fill under her jaw. Her face and neckline are clearly exposed; the lower foreground pot edge falls into deep shadow, and the lanterns form the brightest highlights. Clear natural skin texture and fine hair detail.
```

## 生成與停損（R22 依成本限制指定）

**再生 2 張，0.24 credits。**

> 「這輪只改四個已定位的句子，**不需要用 6–12 張換取更漂亮的抽樣**；
> 2 張已足以判斷『桌面小空碗＋上臂裁切』是否消除端碗連鎖。」

| 結果 | 處置 |
|---|---|
| **至少 1 張同時通過**「碗平放、零可見手、低眼看碗、已喝完、mock-neck 正確」 | **立即停止生圖，採用通過者。不為選美追加成本** |
| 2/2 又把碗舉到胸前／生雙手／直視鏡頭 | 判定新碗句仍有系統性端碗語意。**下一步不是再抽圖，而是完全移除碗與餐具**，改用桌面暖色光斑或另一個**非可握持**的實體視線目標，再做 2 張 |
| 端碗連鎖已解，但服裝 1 過 1 不過 | **沿用通過的那張，不改服裝 prompt**——這是隨機服從差異 |
| 只剩背景 1 張亂碼、1 張乾淨 | **取乾淨者，不為背景多花 credits** |

## R22 補充的三點

| # | 內容 |
|---|---|
| 1 | **`empty` 是時間狀態，不是要證明沒有食物。**若平放小碗裡留下少量湯痕、但其餘核心 gate 全過，**可接受；不要因為碗不是像素級全空而誤殺** |
| 2 | **不要同時改 animation prompt。**本輪只重做 start frame，靜態圖通過後沿用 R21 已定的動畫設計，**否則會把靜態修正與動畫修正混成同一輪** |
| 3 | **本批的成功定義是「有一張可直接進 Kling」，不是 2/2 都要過。**一張通過即停，另一張只作隨機性參考 |

---

# 十、第二批實測（2026-09-01，2 張，0.24 credits）

job `fe935239`（C）／`e8bcc146`（D）。`transactions` 逐筆 −0.12 ×2。

## 逐張對硬 gate

| gate | C | D |
|---|---|---|
| 臉是 Yuna | ✅ | ✅ |
| 只有一個人物主體 | ✅ | ✅ |
| 頭／肩／領口／上半身可見 | ✅ | ✅ |
| **象牙色 mock-neck、上胸覆蓋** | ✅ | ✅ |
| 淘汰低領 | ✅ | ✅ |
| 衣服場合成立 | ✅ | ✅ |
| **碗平放在桌上** | **✅ 解決了** | **✅ 解決了** |
| **可見手＝0** | **✅ 手掌在畫面外** | **✅ 同** |
| **無時間矛盾（已喝完，不是端碗）** | **✅ 解決了** | **✅ 解決了** |
| 嘴唇自然閉合 | ✅ | ✅ |
| 五官無結構瑕疵 | ✅ | ✅ |
| 頭髮符合設定 | ✅ | ✅ |
| 妝感自然 | ✅ | ✅ |
| 正面關係成立 | ✅ | ✅ |
| 曝光符合規劃 | ✅ | ✅ |
| 色彩可調 | ✅ | ✅ |
| 場景像餐廳 | ✅ | ✅ |
| 背景無偽文字 | 🟡 左側框內有輕微模糊字樣 | 🟡 同 |
| 9:16 安全區 | ✅ | ✅ |
| **視線落在碗緣** | **❌ 直視鏡頭** | **❌ 直視鏡頭** |

## ✅ R22 的碗修法有效：四個連鎖失敗解決了三個

| v1 的失敗 | v2 |
|---|---|
| 碗被舉在胸前 | **✅ 平放在桌面上** |
| 雙手捧碗入鏡 | **✅ 手掌在畫面外，看不到手指** |
| 時間矛盾（正在端碗） | **✅ 已喝完的狀態** |
| 視線看鏡頭 | ❌ **仍然失敗** |

**「碗緣橫跨下方中央」被讀成「她在端碗」這個診斷是對的，改成「平放在石桌上的小空碗」把整條連鎖打斷了。**

## 🔴 但 R22 的停損規則對不上這次的結果

R22 寫：
> 「若 2/2 又把碗舉到胸前／**生成雙手**／直視鏡頭，判定新碗句仍有系統性端碗語意；
> 下一步是**完全移除碗與餐具**。」

**它把三個症狀綁在一起，假設它們會一起動。實際上碗與手都修好了，只剩視線。**
**所以「完全移除碗」這個處方對應的是錯的診斷——碗那一句是成功的，不該拆掉。**

## 我對視線失敗的推測

**碗現在離她更遠、更低了。** v1 的碗（被端著）在她胸前；v2 的碗平放在桌面中央，
**比她的臉低很多、也遠很多**。要看那個碗需要大幅低頭。

**修好端碗的同時，把視線目標變得更難看。** 這是一個真實的權衡，不是單純的模型不服從。

另一層：prompt 同時要求「觀眾坐在她正對面」＋「完整頭部可見」，
模型可能判斷大幅低頭會讓臉看不清楚，於是選擇抬頭。
**而 `soul_2` 的先驗本來就強烈偏向「正面看鏡頭的人像」。**

## 處置

依既有分流規則：**2/2 同方向失敗＝系統性，停下來改 prompt，不再抽卡。**
**不生第 3、4 張。要送覆核（R23）。**

**但要明確告訴覆核：碗那一句是成功的，不要拆掉——這正是上一輪「保護已成功部分」的同一件事。**

---

# 十一、🔴 設計變更：放棄「低眼看碗」，改用已生成的首幀（2026-09-01 Penny 判斷）

## 起因

> 「我覺得你根本就生成不出來確定的起始幀。這個前面已經走了兩輪了，根本就沒有用。
> **難道一定要生成出原本的樣子，才能做出這個影片嗎？**」

## 她是對的，而且我犯的錯是規則用錯層級

**「視線離開鏡頭」這條軸線全專案已經失敗 8 次：**

| 件 | 視線目標 | 結果 |
|---|---|---|
| LG-01 | 鏡頭一側的車流（**畫面外**） | ❌ 2/2 |
| LG-05 | 掌心裡的雨滴（**畫面內但太小、沒被畫出來**） | ❌ 2/2 |
| 鏡 3 v1 | 被端著的碗緣 | ❌ 2/2 |
| 鏡 3 v2 | 平放桌上的小碗緣 | ❌ 2/2 |

**我們的規則是「兩張同方向失敗＝系統性，停下來」。
我在每一輪內部套用了，卻沒有跨輪套用**——第三輪還想再試同一件事。

## 決定：低眼是手段，不是目的

R18 給這一鏡的目的原文：
> 「她的人設價值在**試完才下一句結論**；反應鏡頭讓 verdict 有人承擔，又避開最危險的進食動作。」

**「低眼看碗」只是表達「先判斷再下結論」的一種手段。**
而選定的首幀**已經是一張 verdict 臉**——沒有笑、沒有比讚、神情克制、直視觀眾。
**下結論本來就是對著人說的。**

**「先判斷」那一拍留在剪接裡**：鏡 2（湯鍋）接到她一張不動的臉，那個停頓本身就是判斷。

## 選定：D（`reference/start_frames/yuna_shot3_selected.png`）

D 比 C 乾淨：**長袖、mock-neck 更明確、背景單純、右側一位食客提供公共場景紋理**。
C 是短袖、背景較雜。

**D 通過 R21 那 20 條硬 gate 中除視線外的全部。**

## 連帶的設計簡化

| 原設計 | 改成 |
|---|---|
| 低眼停一拍 → 抬眼 → 點頭 | **神情穩住 → 一次極小的點頭** |
| 運動預算：一主（視線轉移）一次（點頭） | **只有一個主運動＝點頭** |

**新設計比原設計更安全**：原本要 kling 從「已抬眼」的首幀先低下去再抬起來，
是**先反向再正向**的難動作，而中間那個低眼狀態我們正好知道模型做不出來。

**動畫 prompt 因此要重寫 → 送 R23 覆核。**

---

# 十二、R23 裁決：動畫段重寫（2026-09-01）

R23 只問一件事——首幀已定、拿在手上，唯一要寫的是那 5 秒。

## Q1 一次點頭夠不夠撐 5 秒？

**判定：正確，五秒只做一次極小點頭，不需要第二個敘事運動。**

它給的理由裡，有兩條是我沒想到的：

- **一次小點頭本身就有三個可讀階段**——穩定 eye contact → 下壓 → 回穩。
  它不是一個瞬間抽動，已足以形成完整動作弧。
- **「像靜態圖套濾鏡」不是靠動作數量判定的**，而是靠動作是否有意圖、
  起止是否自然、聲畫是否對位。**一次準確的 verdict nod 比兩三個無意義微動更像真人。**

其餘（眨眼、微笑、視線轉移、呼吸起伏、頭髮飄動）都不新增必要訊息，
卻會增加改臉、改表情、改衣領與背景放大的風險。

> **若 kling 自然生成一次結構正常的眨眼或幾乎不可見的呼吸微動，可接受**，
> 但不作硬要求、不算第二個敘事運動；**不能因為沒有眨眼而判 FAIL**。

## v2 動畫 Prompt（R23 逐字指定，118 字）

<!-- PROMPT_ID: shot3_anim_v2 | FP: sha1:7271744bbeea | REVIEW: R23 逐字指定 -->
```
A locked-off frontal close-up. She holds calm, direct eye contact with the viewer for one quiet beat, then gives one single, very small and controlled nod: her chin lowers slightly and returns once to its original neutral position. She settles into the same composed posture for the rest of the shot, her restrained expression unchanged and her lips softly closed. Her face identity, mock-neck collar, shoulders, forearms, hair, white porcelain bowl, dark pot rim, stone tabletop, background diner, carved wooden screen, dark wood panels, and amber lanterns maintain their original shapes and positions. The warm amber lantern key light and softer neutral-gold tabletop fill remain steady while the lower foreground stays in deep shadow. Quiet restaurant room tone.
```

| 句 | 作用 |
|---|---|
| 1 `A locked-off frontal close-up.` | 固定機位與既有正面關係，不給推鏡、搖鏡或重新構圖的空間 |
| 2 `She holds calm…one quiet beat` | **保留首幀原有的直視狀態**，讓鏡 2 切進來後有一拍可讀停頓 |
| 3 `then gives one single…` | 唯一主運動。把點頭拆成「下壓＋回到原中立位」；`single`／`once` **防止連續 bobbing** |
| 4 `She settles…` | 動作完成後回穩；表情、嘴唇全程維持首幀，不新增微笑、說話或誇張反應 |
| 5 `Her face identity…` | 逐項鎖住高風險既有元素，尤其**已經成功的 mock-neck、畫面下緣前臂、白碗、鍋緣、背景食客** |
| 6 `The warm amber…` | 維持首幀已成立的雙色溫與曝光犧牲，避免點頭時臉忽亮、暗部抬起或燈籠閃爍 |
| 7 `Quiet restaurant room tone.` | 只給可被後製覆蓋的安靜環境底聲；**verdict 仍是後製畫外音，不要語音或嘴型** |

## Q3 驗收標準：R21 的 12 條改寫成 16 條

### 刪除（都是為「低眼→抬眼」寫的）

- 起始低眼看碗、低眼停一拍、視線由碗移向觀眾、抬眼與抬下巴同步、碗緣作動畫視線目標
- 不再要求「先低眼再下結論」的時間順序——**這個順序已由鏡 2→鏡 3 的剪接停頓承擔**
- **不把「必須眨眼」「必須有呼吸起伏」「頭髮必須微動」列為驗收項**

### 新的硬 gate

| # | 項目 | 判準 |
|---|---|---|
| 1 | 首幀忠實度 | 第 0 幀的臉、mock-neck、前臂裁切、白碗、鍋緣、背景食客與光色與 start image 連續，不能開場跳變 |
| 2 | 直視狀態 | 點頭前後都看向正對面觀眾。點頭過程可有極小眼位變化，**不能改看碗、閉眼過久、斜視或轉向畫外** |
| 3 | 點頭次數 | 全片**恰好一個完成循環**；不連點、不顫抖、不重複 bobbing、不先仰頭再猛壓 |
| 4 | 點頭幅度 | 下巴最低點相對中立位下移 **2–4% 臉高（約 3–6°）**。超過約 6%／10°、或帶動上半身鞠躬 → FAIL |
| 5 | 點頭時間 | 先穩 **0.7–1.5s** → **0.6–1.2s** 內完成「下壓＋回位」→ 其後至少穩 **1.5s**。不能五秒都在緩慢下沉，或最後一幀還沒回位 |
| 6 | 回穩精度 | 鼻尖／下巴垂直位置與首幀差異 **≤ 1–2% 臉高**；不能停在低頭、仰頭或側傾 |
| 7 | 表情與嘴型 | 克制 verdict 臉全程不變；嘴唇自然閉合，不微笑、不張嘴、不咀嚼、不產生說話嘴型 |
| 8 | 身份與五官 | 臉型、五官比例、年齡感穩定；不換臉、不大小眼、瞳孔不漂移、嘴角不熔化、皮膚不塑膠化 |
| 9 | 服裝 | 象牙色 mock-neck 仍是**一件連續上衣**；領口不下降、不變 choker、不變大圓領、不露上胸，針織紋理不游動 |
| 10 | 肢體 | 雙前臂穩定，**畫面內始終不長出手掌／手指**；肩膀不做大幅鞠躬 |
| 11 | 物件 | 白碗平放、少量湯汁、鍋緣、桌面、木屏、牆板、燈籠不移位、不膨縮、不複製、不新增餐具或文字 |
| 12 | 背景食客 | 維持背對／側對與中景位置；**不轉頭看鏡頭**、不靠近 Yuna、不長出清楚陌生人臉或肢體 |
| 13 | 相機與光 | locked-off，無推拉搖移與透視改變；暖主光、中性回填、深暗鍋區與燈籠高光不閃爍 |
| 14 | 可用窗 | 至少連續 **4.0 秒**同時通過全部硬 gate。**唯一瑕疵若落在可裁掉的最後一秒，仍可用** |
| 15 | 聲音 | **以人耳判斷** room tone 是否自然。聲音單獨失敗可靜音／替換，不判視覺路線失敗 |
| 16 | 允許的非指令微動 | 至多一次結構正常的自然眨眼、極小呼吸或亞像素髮絲微動。不得改變身份、衣服、姿勢或搶過點頭 |

> **第 15 條是把「不要用 RMS 代替人耳」寫成驗收條文。**

### 「一次極小的點頭」的可驗收定義

> 中立位 → 下巴下降約 **2–4% 臉高（約 3–6°）** → 回到距原中立位 **1–2% 臉高**內，
> **完整循環恰好一次**；不帶側傾、不帶肩膀鞠躬，完成後至少穩定 **1.5 秒**。
> **必須肉眼看得出她在「確認」，但不能像連續點頭、鞠躬或抽動。**

## Q4 停損：🔴 本鏡只跑 1 支，不預設第二支

R23 直接依成本限制把停損收緊了：

| 首支結果 | 處置 |
|---|---|
| 有連續 4 秒通過全部硬 gate | **採用。**點頭時間不完美置中、或聲音要替換，**不值得重跑** |
| 畫面穩定但點頭沒發生／太小／超過一次 | **不再花第二個 10 credits**，直接走靜態微推備案 |
| 換臉、領口改形、長手、碗／鍋變形、背景食客轉頭、沒有連續 4 秒窗 | **立即停止人物 i2v** |
| 只有一種情況跑第二支 | 使用者明確判定「真實點頭本身值得再付 10 credits」，**且**首支失敗屬單一隨機瑕疵 |

> 它同時提醒：立即停止**是本次製作的成本停損，不等於以 n=1 宣稱 kling 一般性做不到**。

### 備案：2D 微推（新增生成成本 0）——但**不要照鏡 4 的做法**

這是我原本會做錯的地方。R23 指出：**這張是人物近景，不要像鏡 4 那樣切頭髮／人物／背景做三層大視差**——
**人物細髮與肩線分層容易出白邊，沒有必要。**

- **單層 2D 微推**，5 秒內只做約 **1.5–2% 等速微推近**
- **不旋轉、不橫移、不生成補邊**，用原圖安全邊界完成
- 最後 1 秒可停止或減慢
- 旁白在微推開始約一秒後進入，**讓聲音成為 verdict 的動作**
- 驗收：臉、mock-neck、碗、背景人物與光線逐像素保持；沒有 AI 新動作、沒有人物增生、沒有髮絲遮罩白邊
- **速度不要與鏡 4 的 CTA 微推完全相同**，以免連續兩鏡像同一模板

## R23 補充的三點

1. **不要為了「動起來」要求 kling 改表情。**
   首幀的克制直視正是兩輪成本換來的有效資產；
   **表情若變甜笑，會把「試完才推薦」降成一般業配反應。**
2. **旁白的落點比第二個動作重要。**
   穩定直視約 0.8–1.2s 後開始韓文 verdict，在點頭下壓／回位時接中文「這個真的好」，完成後留一拍安靜。
   **實際點頭時間不同就剪旁白配動作，不要求模型為音訊重生。**
3. **通過不一定要用滿 5 秒。**
   若前 4–4.5 秒最自然，可提早切到鏡 4，或把最後 0.5–1 秒交給鏡 4 的櫻花 CTA；
   **不要為了時碼保留末段瑕疵。**

---

# 十三、動畫實測（2026-09-01，1 支，10 credits）

**job**：`b8c5c2e4-24f1-4471-963f-e40d58591566`　**檔**：`reference/shot3/rujiao_shot3_nod_v1.mp4`
**規格**：`kling3_0` ／ 5s ／ 9:16 ／ sound on ／ start_image = `yuna_shot3_selected.png`
**帳**：`transactions` 顯示 `Kling v3.0 −10`（不是用餘額差推算）

> 同一時段帳上另有 24 筆 `Seedream 4.5 −1`（10:35–10:44），**不是這條線跑的**，我沒有用 Seedream。

## 量測方法

720×1280、24fps、121 幀。以首幀眼帶（y 415–485, x 260–440）為模板，
逐幀做 ±40px 垂直 ／ ±25px 水平的 SAD 比對，得到頭部位移曲線。
臉高以首幀量得 **225px**（髮際 y≈365 → 下巴 y≈590），位移換算成臉高百分比。

## 🔴 點頭曲線：形狀與幅度都超規

| 時間 | 位移 | 佔臉高 | 狀態 |
|---|---|---|---|
| 0.00–1.05s | 0～−2px | ~0% | 穩定直視 ✅ |
| 1.17–1.42s | **−17px** | **−7.6%** | **先仰頭**（頭往上） |
| 1.67–2.08s | **+38px** | **+16.9%** | **下壓最低點** |
| 2.6–3.3s | −10px | −4.4% | **回位時越過中立位再往上** |
| 3.9–5.0s | +2～+3px | +0.9% | 回穩 ✅ |

**對 R23 的 16 條硬 gate：**

| # | 項目 | 判 | 依據 |
|---|---|---|---|
| 1 | 首幀忠實度 | ✅ | 第 0 幀與 start image 連續，無開場跳變 |
| 2 | 直視狀態 | ✅ | **全程看向觀眾**，沒有改看碗、沒有斜視、沒有轉向畫外 |
| 3 | 點頭次數／形狀 | ❌ | **先仰頭（−7.6%）再猛壓**，且回位時越過中立位再上抬 −4.4%。R23 明列「不能先仰頭再猛壓」 |
| 4 | 點頭幅度 | ❌ | **16.9% 臉高**。規格 2–4%，**FAIL 線是 6%——超過約 2.8 倍** |
| 5 | 點頭時間 | ❌ | 先穩 1.05s ✅，但「下壓＋回位」花了 **約 2.2s**（規格 0.6–1.2s） |
| 6 | 回穩精度 | ✅ | 收在 +2～3px＝**0.9% 臉高**（規格 ≤1–2%） |
| 7 | 表情與嘴型 | ❌ | **下壓最低點出現閉唇微笑**（見 `shot3_f0_vs_f48.png`），首幀是中性唇 |
| 8 | 身份與五官 | ✅ | 全程同一張臉，無換臉、無熔解、無塑膠化 |
| 9 | 服裝 | ✅ | 象牙 mock-neck 連續、領口不變形、長袖維持 |
| 10 | 肢體 | ✅ | 畫面內始終無手掌／手指；**肩膀只位移 3px**（頭 38px）→ 沒有鞠躬 |
| 11 | 物件 | ✅ | 白碗位移 0px、殘差 1.7–2.0；桌面、鍋緣、木屏穩定 |
| 12 | 背景食客 | ✅ | 位移 4–7px 的自然進食動作，維持側對、沒有轉頭看鏡頭 |
| 13 | 相機與光 | ✅ | locked-off。六個取樣區亮度全程只差 1–3 級（鍋 98.9→101.1、碗 175.3→176.5、燈籠 51.2→53.1） |
| 14 | 連續 4 秒窗 | ❌ | 乾淨窗是 **0–1.15s** 與 **3.5–5.0s**，中間 2.2s 是超規動作。**瑕疵在中段，不在可裁掉的末段** |
| 15 | 聲音 | — | **依規則要人耳判斷，我不判**（新 gate 第 15 條） |
| 16 | 非指令微動 | ✅ | 沒有搶戲的額外動作 |

**11 過、4 不過、1 待人耳。**

## 診斷

**不是「沒動」，是「動太多」。** 這和前兩鏡的失敗方向相反——
鏡 1、鏡 2 的風險是模型不動，這次是模型把 `one single, very small and controlled nod`
做成一個**帶預備動作的完整點頭**（先抬頭蓄力 → 下壓 → 回彈）。

`very small`／`controlled`／`single` 三個字都寫了，但：
- `single` **有效**——只有一個下壓，沒有連點
- `very small` **無效**——16.9% vs 規格 4%
- 「不要預備動作」**我們沒寫**，R23 的 prompt 裡也沒有這句；
  它只在**驗收條文**裡禁止「先仰頭再猛壓」，**沒有寫進 prompt**

> **這是規格與 prompt 之間的漏縫**：驗收條文抓得到的東西，prompt 沒有相對應的句子去防它。
> 和 D-05（否定無效）不同——這裡不是否定失效，是**根本沒有下指令**。

## 微笑那一項最關鍵

R23 的補充第 1 點寫得很準：
> 「表情若變甜笑，會把『試完才推薦』降成一般業配反應。」

下壓最低點確實出現了閉唇微笑。**幅度不大，但它落在整支片最被注視的那一格。**

## 處置：依 R23 的停損，不自動跑第二支

R23 的表列得很清楚——點頭幅度／次數不對 → **不再花第二個 10 credits**，走靜態微推備案。
**我沒有自行決定重跑。** 交給 Penny 判斷。

累計（如嬌）：鏡 1 影片 10 ＋ 鏡 2 影片 10 ＋ 鏡 3 首幀 4×0.12 ＋ 鏡 3 影片 10 = **30.48 credits**。
