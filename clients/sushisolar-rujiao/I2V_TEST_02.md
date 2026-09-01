# i2v 路線探針 #02｜如嬌鏡 2（整隻玉米雞＋蒸氣）

> 2026-08-31。規格由 R20 覆核裁決，逐字採用。未經 Penny 確認前不送生成。

## 一、這一鏡的內容任務（R20 補充指出的）

> **鏡 1 已經證明「湯很濃」，鏡 2 不應再用蒸氣重講一次「很熱」。**
> **鏡 2 的內容任務是證明「真的有整隻玉米雞與花膠」。**

因此驗收優先序是：**產品身分 ＞ 雞／鍋幾何 ＞ 低幅熱紋 ＞ 蒸氣**。

## 二、首幀

| | |
|---|---|
| 來源 | <https://www.instagram.com/p/DF5Ze9JT9r9/>（客戶自有，**無燒字、無第三方浮水印**） |
| 檔案 | `reference/start_frames/rujiao_shot2_chickenpot_9x16.png`，1012×1800 |
| 排除 | `CmOaIiOv73S`（招牌鍋俯拍）——構圖更好但**又燒了「#喝一碗花膠抵數十片面膜」** |

## 三、R20 的關鍵判斷：不要讓蒸氣承擔主運動

我原本問的是「怎麼限制蒸氣不要變成白霧」。**R20 換了一個框架**：

> 「最有效的風險分配**不是跟明顯蒸氣拔河**，而是**先給模型一個更安全、可持續五秒的主運動**，
> 降低它把蒸氣升格為全片主角的需要。」

> 「探針 #01 證明 Kling 會從首幀中挑選既有元素加碼，
> **但沒有證明它會把每個元素都放大。**」

**我的提問方式本身是錯的**——我在想怎麼壓制風險元素，正解是給模型別的事做。

### 主運動：湯面極輕微的熱對流波紋

不選推鏡（會讓模型重建高風險畫面），不選只給蒸氣（把最危險的元素變成唯一運動來源），
不讓雞動（會像呼吸或變形）。

限定在「**雞與鍋內緣之間可見的狹窄湯面**」，幅度低、**始終位於厚鍋沿下方**——
用 `narrow visible bands`／`low-amplitude`／`contained below the thick rim`
把波紋和溢鍋、沸騰分開。

## 四、參數

```
model         kling3_0
duration      5
aspect_ratio  9:16
sound         on
medias        [{ role: "start_image", value: <media_id> }]
```
成本 **10 credits**。

## 五、Prompt（R20 逐字指定，114 字）

```
A locked-off close-up of the whole corn-fed chicken resting in thick golden-white broth inside the dark earthenware pot. Gentle, low-amplitude heat ripples travel across the narrow visible bands of broth between the chicken and the inner pot rim, remaining contained below the thick rim. The broad warm-brown steam layer in the upper half remains translucent and low-contrast, drifting upward as one slow soft veil while the dark background stays visible through it. The chicken, pale fish maw pieces, pot rim, and background maintain their original shapes and positions. Warm light remains concentrated on the chicken from the upper left while the right side of the pot stays in deep shadow. Quiet restaurant room tone.
```

### 每一句在做什麼

| 句 | 作用 |
|---|---|
| 1 | 固定身分與構圖；**把雞定義為 `resting`，不給任何生物式運動** |
| 2 | 分配**唯一主運動**：只有狹窄可見湯面產生低幅熱紋；`contained below the thick rim` 正向指定液體邊界 |
| 3 | 處理蒸氣：**承認原圖是一整片，不假裝只有一絲**；以暖褐、半透明、低對比、單一慢速薄層、暗背景可見鎖定視覺結果。**沒有用否定句** |
| 4 | 把所有高風險靜物寫成穩定狀態——防整雞呼吸、花膠漂移、鍋沿膨縮、背景重建 |
| 5 | 保留原照左上高光／右側暗部的曝光取捨，避免模型為了看清蒸氣而抬亮暗背景 |
| 6 | 只要安靜 room tone，**不要求沸騰聲**——否則聲音提示會反向把畫面推成大滾鍋 |

**刻意不寫**：`bubbling`、`simmering`、`boiling`、`oil glistening`、`camera push-in`。
這些都會新增第二主運動，或把既有油光／蒸氣再放大。

## 六、🆕 通用規則：運動預算

> **每個 i2v prompt 先列一個主運動、一個次運動；其餘既有元素全部寫成穩定狀態。**

鏡 2 是「**主：狹窄湯面熱紋；次：半透明蒸氣慢移**」。
不要再加雞皮閃光、推鏡、氣泡或花膠漂動。

## 七、驗收

**PASS 門檻改為連續 4.0 秒**（不是鏡 1 的 3.0）——本鏡在成片佔 3–7 秒，需要四秒。

### 共用（兩鏡通用）
① 首幀／來源忠實度 ② **不得新增內容**（文字、logo、食材、器皿、人物、門窗、燈具、桌椅）
③ 光色穩定，不閃爍、不自動提亮 ④ 輸出清晰度，不得出現時間性抖動、壓縮塊、邊緣 shimmer、油畫化

### 鏡 2 專屬
| # | 項目 | 硬 FAIL |
|---|---|---|
| 1 | **整雞身分** | 呼吸、抽動、膨縮、融化、變成另一種肉 |
| 2 | **湯面熱紋** | 大滾、冒泡、上升越過鍋沿、溢出、生成新液流 |
| 3 | **花膠／筍片** | 像活物游動、複製、消失 |
| 4 | **鍋體幾何** | 厚鍋沿／深褐粗陶／橢圓透視呼吸、熔接、改形 |
| 5 | **蒸氣** | 變成不透明白霧、下壓遮到雞／鍋、分裂成多股實體煙柱、邊界規律循環、背景曝光被抬亮 |
| 6 | **機位** | 推近、拉遠、平移、傾斜、改變透視 |
| 7 | **聲音** | **必須由人耳判斷**。RMS 只作紀錄，不能代替聽感（R19→R20 沿用我上一輪的錯誤修正） |

### 已刪除（鏡 1 專屬，本鏡不適用）
湯柱來源與連續性、懸空湯滴、碗內落點與液面、手部指尖、碗與湯勺幾何。

## 八、停損順序（R20 指定，不准同義改寫抽卡）

1. 首跑原圖 ＋ 本 prompt
2. **若只失敗在蒸氣** → 做一次**來源端**確認跑：在首幀上**局部降低上半部蒸氣的對比／不透明度**，
   雞、湯、鍋保持原像素，**固定同一 prompt** 重跑
3. **同類失敗再現** → 停止 Kling，改局部遮罩的 2.5D／合成熱氣

> **不要用第三、第四次 prompt 同義改寫消耗 credits。**
