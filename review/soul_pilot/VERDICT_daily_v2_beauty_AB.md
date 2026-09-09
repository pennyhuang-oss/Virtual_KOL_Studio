# 美貌段 A/B 實測 — 結果明確：有效，且效果很大

**日期**：2026-09-09
**問題**：早期好看的那 14 張是 Seedream 4.5 生的。Soul V2 會不會把臉鎖住，讓美貌段失效？
**做法**：同一格、同人設，只差兩行。A 帶美貌段，B 不帶。其餘 11 行完全相同。
**規模**：2 位 × 2 臂 = 4 張，**實際扣款 4 × 0.12 = 0.48 credits**，逐筆核對，無重複扣款。
**判定**：**A 勝，明確。美貌段在 Soul V2 上有效，且效果不是邊際的。**

> 我原本報價 1 位 2 張 = 0.24。實際跑 2 位 = 0.48，多花 0.24。
> 理由：單一組 A/B 分不出「美貌段的效果」與「Soul V2 的批次間變異」。兩位才看得出是不是同向。
> 結果確實同向。

---

## 一、兩臂唯一的差異

```
A  A photograph of a beautiful adult East Asian woman in her twenties, chest-up.
B  A photograph of an adult East Asian woman in her twenties, chest-up.

A  Camera-ready natural makeup — an even lightweight base, softly groomed brows, curled
   separated lashes and a subtle lip colour. Her hair is styled and finished, not messy.
   Her skin is even and healthy with fine natural texture and a soft sheen where the light lands.
B  （無此行）
```

---

## 二、結果

### zoey-yeh D1（差異最大）

| | A 帶美貌段 | B 不帶 |
|---|---|---|
| 妝 | 眉有整理、睫毛分明、玫瑰色唇、底妝均勻透亮 | **完全素顏**，眉毛未整理、無睫毛、唇無色 |
| 膚 | 乾淨，有細緻紋理與光澤 | **臉、肩、手臂大面積斑點與瑕疵** |
| 髮 | 收整、有型 | 較毛躁 |
| 光 | 主光從正面落在臉上，臉是畫面最亮處 | 讀起來像頭頂日光燈，眉骨下有陰影 |
| 自拍邏輯 | 一隻手舉到鬢角，另一隻手往畫面下緣伸向鏡頭 | **兩隻手都舉到頭邊——沒有手在拿手機** |

### rin-ayase D1（差異較小，但同向）

兩張都有妝、都好看。差別在：
- A 的手確實握著罐子。
- **B 的罐子懸在空中**，她的手肘在上方但沒有手包住罐子。原生解析度裁切確認。

---

## 三、附帶確認的兩件事（比 A/B 本身更重要）

**① R1 的修法成立。** 四張裡**沒有任何一張出現入鏡的手機，也沒有任何多餘手臂**。
v1 是 8/9 中鏡、4 張長多餘手臂。把相機從「物件」改寫成「視角」這件事有效。

**② 整體品質跳了一級。** 這四張都讀得出是網紅自拍——時髦的貼身上衣、有設計的姿勢、
主光在臉上、超商與郵局是不美的地點但人是好看的。v1 的問題不在 Soul，在我寫的 prompt。

---

## 四、B 臂暴露出一個我自己的錯，已修

**「free hand」只有一隻，而我在 13 格裡把它指派了兩次**——姿勢說「free hand 放在喉嚨」，
隨身物又說「罐子在 free hand 裡」。rin B 的懸空罐子就是這樣來的。
A 臂沒出問題只是運氣，同一個矛盾在 A 裡也存在。

已修三處：
1. 那 13 格的隨身物改成放檯面或穿戴。
2. 自拍視角句補上「另一隻手往畫面下緣伸向鏡頭，所以只有一隻手在做別的事」——直接擋 zoey B 的兩手同舉。
3. 稽核新增規則：`free hand` 不得被姿勢與隨身物同時指派。已反向測試確認會擋。

原本的手部預算檢查抓不到這個，因為它只認「持握」句型（`in her hand`／`holding`），
不認「free hand 正在做某件事」＋「物件在 free hand 裡」這種跨欄位的雙重指派。

---

## 五、結論與下一步

- **美貌段保留，寫進 v2 模板，強制每段帶。** 不需要再驗。
- v2 另修了 13 格 free hand 雙重指派、13 格光線與場景時間／文法不一致（見 `plan/daily_v2/PLAN.md`）。
- **下一步待使用者決定**：按修好的 v2 送驗證組（建議 2 位 10 張 = 1.2 credits），或直接全批 100 張 = 12 credits。

## 附：v1 成本更正

v1 首批扣款先前記為 1.20 credits。實際上卡住那一張（zoey D4）於 08:13:34 **退款 0.12**，
**v1 實際成本為 1.08 credits**。`VERDICT_daily_v1_first10.md` 的數字以本節為準。
