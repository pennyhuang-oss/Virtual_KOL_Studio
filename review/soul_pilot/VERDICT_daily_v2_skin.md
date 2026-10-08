# 膚質句修正 — 有效，而且順帶推翻了我先前一個判斷

**日期**：2026-09-09
**改的東西**：GLOW 段裡的膚質那一句。
**驗證**：zoey-yeh D1（與前兩輪同格對比）＋ D3（不同框架、不同光線，看是否通用），2 張 = **0.24 credits**。
**判定**：**有效。膚質問題解決，而且妝也跟著出來了。**

---

## 一、改了什麼，以及為什麼是這樣改

原本寫的是：

```
Her skin is even and healthy with fine natural texture and a soft sheen where the light lands.
```

回頭查 `identity_master.json`——**產生那 20 張已經認可的臉孔的 prompt**——它寫的是：

```
Even, healthy-looking skin with fine natural texture and subtle professional retouching.
…
Soft wrapping light from slightly above and in front …, creates a small natural catchlight in both eyes
```

**「紋理」與「修飾」在原文裡是成對的，我只抄了「紋理」那一半。**
紋理沒有修飾配著，在素顏調性的 Soul 上就變成瑕疵。

改成：

```
Her skin is even and healthy-looking with subtle professional retouching, clear and consistent
in tone, with a soft sheen where the light lands and a small natural catchlight in both eyes.
```

不再寫「紋理」（素顏調性的 Soul 會讀成不均勻），改寫**均勻膚色 ＋ 修飾 ＋ 光落處的光澤 ＋ 眼神光**。
真實感交給光線與構圖負責，不交給皮膚負責。

---

## 二、三輪對比（同一格 zoey-yeh D1）

| | 1 原始 | 2 修正 C | 3 膚質句改掉 |
|---|---|---|---|
| 皮膚 | 尚可 | 🔴 鼻梁雙頰額頭斑點、胸口鎖骨大片不均勻 | ✅ **乾淨均勻，臉與胸口都沒有斑塊** |
| 眉毛 | 柔散 | 柔散 | ✅ **有形、有畫過** |
| 睫毛 | 幾乎沒有 | 幾乎沒有 | ✅ **分明、有捲度** |
| 眼神光 | 無 | 無 | ✅ **雙眼都有** |
| 姿勢 | 手懸空、手肘外翻 | 手指碰到耳朵、手肘壓低 | ✅ 維持 |
| 表情 | 面無表情 | 有一點 | ✅ 維持，眼睛有神 |

**第 3 張是三張裡最好的一張。**

D3（老屋改的店、洋裝、近距他拍）同樣成立：皮膚乾淨、眉睫清楚、閉唇笑而眼神暖、
手確實放在腰上、只有兩隻手。**修法通用，不是只在 D1 那一格有效。**

---

## 三、要更正我先前的一個判斷

我在 `VERDICT_daily_v2_fixC.md` 與對話中說過：

> 「妝仍然很淡……美貌段在她身上依舊被 Soul 抵抗。」

**這句話是錯的。** 妝之所以不出來，不是 zoey 的 Soul 在抵抗，是我自己那句
`fine natural texture` 把畫面往素顏方向拉——它跟妝互相打架，而不是 Soul 跟妝打架。
把那句換掉之後，同一個 Soul、同一段美貌詞，眉毛、睫毛、眼神光全部出來了。

**`FINDING_soul_register.md` 的結論要縮小範圍：**
Soul 確實承載訓練圖的調性，但這件事影響的是**服裝／場景／整體氛圍的傾向**，
**不是「妝上不去」**。妝上不去是 prompt 的錯，已修。

---

## 四、還沒解決的

- **`three_quarter`（膝上三分身）的框架控制很弱。** D3 指定膝上，出來是全身連腳與貓都在畫面裡。
  不算缺陷（構圖仍好看），但這一格的框架指令等於沒有生效，要記著。
- **zoey 的整體調性仍偏文青**，那部分是 Soul，需要另外決策（重訓 25 credits／接受原生調性）。
  但她現在「好看」了，所以這個決策的急迫性下降很多。

---

## 附：累計成本

| 批次 | 張數 | 扣款 |
|---|---|---|
| v1 首批 | 10（1 張退款） | 1.08 |
| 美貌段 A/B | 4 | 0.48 |
| 修正 C before/after | 2 | 0.24 |
| 膚質句驗證 | 2 | 0.24 |
| **合計** | **18** | **2.04 credits** |
