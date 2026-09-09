# 日常素材 v1 為什麼不好看 — 根因診斷（2026-09-09）

**使用者評語**：「不管構圖還是場景都很難看，一點網美的時尚感都沒有，包含穿著衣服、風格、
妝容、髮型還有姿勢、氛圍、打光、構圖、場景都完全沒有，根本沒有把小雪莉帳號的素材分析考慮進去。」

**她的指示**：去看 Iris Chen 最早期那一批是怎麼生成的。

**做完之後的結論：她指的那批的做法，答案早就寫在 repo 裡，而 v1 每一條都違反了。**

---

## 一、最關鍵的一條：手機入鏡的規則早就寫下來了，我做的正好是被標成 ❌ 的那件事

`kols/iris-chen/generation_notes.md` 批次 4 底下：

> **⚠️ 自拍視角重要規則**：prompt 描述的是照片本身的**輸出視角**，不是描述「她在拍自拍」的動作。
> - ❌ 錯誤：`taking a selfie holding phone up` → 會生成第三人視角、手機出現在畫面中
> - ✅ 正確：`close-up front-facing selfie shot, slightly overhead angle looking down at camera,
>   looks like a photo taken by her own phone front camera`

v1 每一段 prompt 有**三句**在做 ❌ 那件事：

```
CAMERA_POS   The person holding the phone is standing roughly two metres away…
DEVICE_TELL  …taken quickly by someone who was already walking with her.
DEVICE       Shot on a phone rear camera by someone standing about two metres away…
```

把手機與拍攝者寫成世界裡的實體 → 模型把他們畫進畫面。實測 8/9 中鏡，4 張長出多餘手臂。
**這不是新發現，是一條已經寫在案上的規則被無視。**

---

## 二、我把「臉由 Soul 提供」誤讀成「不必寫好看」

早期 Iris 的核心 prompt 開頭是**九個美貌描述詞**：

```
strikingly beautiful sweet face, large bright double-eyelid eyes, delicate high nose bridge,
soft full lips, small defined chin, glowing skin, photogenic idol-level beauty,
petite curvy hourglass figure with full chest and slim waist, black silky straight hair naturally down
```

而 20 位人設的臉之所以好看，是因為 `identity_master.json` 的 prompt 本身就寫著
`a beautiful N-year-old woman`、`Camera-ready natural makeup`、`subtle professional retouching`、
`Soft wrapping light from slightly above and in front`、`a small natural catchlight in both eyes`。

v1 的模板寫的是反方向：沒有妝、沒有美貌詞，而且明確寫
`printed as it is with no retouching and no smoothing`。

> **Soul 提供的是「身分」，不是「好看」。** 它保證是同一個人，不保證這張照片裡她有妝、
> 頭髮有整理、光有打在臉上、表情有設計。這三件事全部要 prompt 自己負責。

---

## 三、我的光線詞庫本身就是醜的——而這是對 9/3 盲測結果的過度推論

9/3 盲測贏的那一句是 `Soft ordinary morning window light, even phone exposure.`
——那是一句**好看的**平常光。

我把「一句平常光」推論成 14 句詞庫，其中至少三句是主動在寫醜：

| 代碼 | 句子 | §18 檢查「她的臉是畫面最亮的區域之一嗎？」 |
|---|---|---|
| L1 | Plain overhead fluorescent light, flat and a little **green** | ✗ |
| L6 | A single strip light overhead, **hard on the top of her head and dim below it** | ✗ 光在頭頂，臉是暗的 |
| L14 | Flat white light from directly above, even and **unflattering** | ✗ 我把「不好看」直接寫進 prompt |

§18 是 2026-08-26 寫下的規則，原文就是「五段式公式保證的是這個空間的光說得通，
**不保證這個人好看**」，檢查方式是問「她的臉是不是畫面最亮的區域之一」。
v1 有 40 格用到上面三句，全部答案是「不是」。

---

## 四、我把小雪莉的 C 級機制讀錯了：C 級是「地點不美」，不是「人不美」

競品分析寫的 C 級是：**Costco 賣場、麥當勞得來速、蝦皮店到店、超商、機場候機室、
路口凸面反光鏡、停在路邊的車裡**——**地點**完全不美。
但她在那些地點裡**仍然是個時髦白富美**，衣服照樣好看。

v1 做的是把**衣服**也弄不美：醫院刷手服、工作圍裙、素灰運動衫、開襟毛衣配 T、
針織背心配百褶裙。這不是 C 級，這是把人一起做醜了。

---

## 五、姿勢與表情：我寫的是低頭、不看鏡頭、疲憊臉

早期 Iris：3/4 側身、腰臀 S 曲線、回眸、下巴角度、看鏡頭、微笑。

v1 寫的：
- `too tired to arrange her face`（累到沒力氣整理表情）
- `a flat, unbothered expression`（面無表情）
- `head down`、`looking down at the step`、`not looking up`

100 格裡真正看鏡頭的是少數。§17（靜態圖也要有表情設計）與 §20（表情要先有名字再有細節）
都沒有被套用。

---

## 六、構圖：早期是淺景深、人填滿畫面；v1 是廣角、人很小、場景很雜

v1 有 20 格是 `mid_environment`（廣角、她在畫面裡很小、周圍是房間）。
早期 Iris 全部是人填滿畫面、背景散景。rin D4 那張連廣角指示都被相機特寫吃掉。

---

## 七、唯一不需要改的部分

- **背景路人**：2026-08-05 的 14/14 與這次的 zoey D5 都成立，四條件措辭有效，維持。
- **地點寫環境元素不點名地標**：成立，維持（v1 掃描 0 命中）。
- **同穿搭一日敘事**：2026-08-05 的 7/7 成立，維持並擴大。
- **鏡面自拍時手機該入鏡**：v1 實測 2/2 正確，這是唯一該看到手機的格式，維持。

---

## 八、關於那串尾巴（`film grain / warm tones / shot on 35mm / Instagram style`）

§3-D② 把它從模板刪掉，但原文寫的是：

> `iris-chen` 模板值得保留的是**原則**，不是那串字。
> **是否使用 `35mm`／暖色調應由該角色與該場景決定，不跨 19 位固定套用。**

所以這不是禁用，是禁止「跨 19 位固定套用」。
早期 Iris 好看的那 14 張都帶這串尾巴。
v2 的做法：**按場景決定**，戶外自然光與咖啡廳場景使用，室內人工光場景不用。
這不是推翻 §3-D②，是照它原文執行。
