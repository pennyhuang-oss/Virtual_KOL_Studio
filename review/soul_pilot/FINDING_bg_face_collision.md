# 使用者抓到兩個我漏掉的缺陷，其中一個是系統性的、而且污染了已通過的圖

**日期**：2026-09-09
**來源**：使用者看 rin D4 與 zoey D4 的重驗結果。
原話：「這個路人的長相跟我這個人設的長相不就是同一張臉嗎？」「它多出來一隻手」「它就是廢片啊」
**成本**：0 credits（純判讀既有圖）

---

## 一、先更正我自己說錯的一句話

我在 `VERDICT_daily_v2_reshoot4.md` 與對話中寫過：

> zoey D4「籃子是**背在肩上**（不是握著），原生解析度確認一手撐牆、**動作乾淨**」

**這句話是錯的。** 我當時裁的區域是 (550,750)–(1350,1400)，剛好切掉左側，
而第三隻手就在左側。重新裁 (0,700)–(850,1350) 之後很清楚：

- 左側白色針織袖口下有一隻手**平貼在石牆上**
- 同一個袖口區域另外伸出一隻手**捧著籃子底部**，這隻手沒有連到任何看得見的肩膀
- 右側還有她的另一隻手撐在牆上

**＝三隻手。** 我看錯了區域就宣稱整張乾淨，這是判讀流程的錯誤，不是模型的錯誤。

---

## 二、缺陷一：背景路人撞臉（系統性，且已污染通過的圖）

**rin D4**：背景**三個**女人的臉都是 rin 的臉——同樣的眼型、鼻子、唇色、髮際線。
中間那位還穿著白色平口上衣，與 rin 的奶油色背心相似。

**更嚴重的是**：我回頭查前一批那 10 張，**`rin D2`（使用者已經通過的那一張）也有同樣問題**
——背景至少兩位女性也是 rin 的臉。**我們兩個當時都沒看到。**

### 為什麼 §9 的第四條件擋不住

§9 的措辭 `clearly different from her in build, age and clothing` 被稱為「防撞臉的關鍵，不可省略」，
它**確實寫在 prompt 裡**，然後失效了。

合理推測（尚未實測）：**Soul V2 是對整張圖做身分條件化，不是只對主體。**
畫面裡任何一張真的被渲染出來的臉，都會被拉向該 soul。文字條件擋不住模型層級的身分條件化。

**為什麼 2026-08-05 的 14/14 沒抓到**：那一批的背景人物遠、背向、沒有渲染出可辨識的臉，
所以那次驗證證明的是「背景不空曠、配角不搶焦點」，**沒有驗到撞臉這個失效模式**。
§9 的驗證範圍要縮小陳述，不能當成「撞臉已解決」。

### 修法（已改，但**尚未實測**）

不再允許任何臉出現在畫面裡——把措辭從「頭轉開」改成「只有後腦勺」，並加重失焦、減少人數：

```
One or two anonymous strangers are well back behind her, walking away with the backs of their
heads to the camera so that no face is visible at any angle, heavily out of focus and reduced
to soft shapes with motion blur, clearly different from her in build, age and clothing.
```

改動點：`A few` → `One or two`；`heads angled away`（仍會渲染側臉）→ `backs of their heads`
＋ `no face is visible at any angle`；`softly out of focus` → `heavily out of focus and reduced
to soft shapes`。並新增稽核規則，防止這段被改回舊版。

**這是推測性的修法，必須實測。** 影響 59 格。

---

## 三、缺陷二：多一隻手 —— 舊規則的判準漏了

**根因是四肢重複指派，跟先前那隻懸空的罐子同一類，但我的規則沒涵蓋這個寫法：**

```
pose : She is leaning back … with both elbows resting solidly on it …   ← 兩隻手臂都被佔用
micro: a woven basket on one arm                                        ← 再要一隻
```

舊規則只認 `free hand` / `one hand` / `both hands`，**不認 `both elbows` / `one arm`**，所以放過了。

已改成真正的四肢預算：`both hands|both elbows|both arms` 記 2，
`free hand|one hand|one arm|fingertips|one palm|thumb hooked|on one arm` 等記 1，
姿勢＋隨身物加總不得超過 2（自拍與鏡面格為 1，因為一隻手已被手機佔用）。

**改完立刻抓出全批 5 格超額**，包含出事的 zoey D4：

| 格 | 佔用/上限 | 問題 |
|---|---|---|
| zoey-yeh D4 | 3 / 2 | both elbows ＋ basket on one arm |
| emma-kao D4 | 3 / 2 | both elbows ＋ mug held in her free hand |
| angeline-kwee D2 | 2 / 1 | 鏡面格 ＋ thumb hooked ＋ handbag over one forearm |
| cheryl-soh D1 | 2 / 1 | 自拍格 ＋ fingertips ＋ parcel under one arm |
| wendy-yeo D1 | 2 / 1 | 自拍格 ＋ fingertips ＋ parcel under one arm |

五格的隨身物都改成穿戴或放在檯面／牆上。三條規則都做過反向測試確認會擋。

---

## 四、對放行 90 張的影響

**不能放行。** 撞臉影響 59 格，而修法尚未實測。
在確認新的背景措辭真的能消除撞臉之前，跑 90 張就是在製造 59 格的廢片風險。

建議：**先驗背景措辭。** 挑 4 張全部帶背景路人、且是先前確認撞臉的構圖
（rin D2 鏡面站內、rin D4 柱廊、rin D5 夜間、zoey D4 農舍巷），4 張 = 0.48 credits。
只驗這一件事，其他變因不動。
