# VERDICT — 兩條失效規則的修法驗證（rulefix_v1，2026-09-10）

送 4 張 = 0.48 credits。3 張回來，1 張（201 angel-chiu D4，背景修法）還在跑。
每張只換**一個句子**，其餘與原本失效的那一格逐字相同，所以變數是隔離的。

## 修法 A — 背景路人（原本約 45/138 過近過清）

**改動**：把「一到兩位陌生人遠遠在她後方…嚴重失焦」換成一句同時鎖住**畫面比例**與**位置**的：

> Far behind her and much smaller in the frame than she is, one or two people are already
> walking out of the frame, so far back that they read only as soft blurred silhouettes with
> no facial features and no clear clothing detail. Nobody stands level with her or beside
> either shoulder; the ground and air immediately around her are empty, and she is the only
> sharply focused thing in the picture.

思路：原句只講「遠」和「失焦」，是形容詞；新句改成講**在畫面中佔多小**、
**不得與她同高或在肩側**、**她周圍是空的**——是可判定的構圖事實。

| 測試 | 對照原圖 | 結果 |
|---|---|---|
| `F202` zoey-yeh D5 | `140`（兩名男性一左一右緊貼） | ✅ 路人變小、退到遠處、背對走離、明顯失焦，沒有與她同高或在肩側 |
| `201` angel-chiu D4 | `101`（兩名男性緊貼） | ⏳ 仍在生成 |

**假設判定：暫時通過（1/1，樣本太小）。** 不宣告全面有效。

## 修法 B — 牆上人像會畫出人設自己的臉（原本 12/138）

**改動**：把否定句換成**正面描述牆上有什麼**：

> The only reflection is her own; there is no second person and no second phone in the
> reflection. Every wall, panel and screen behind her carries only plain surfaces and printed
> text — notices, price cards and signage lettering — and no framed pictures, posters or
> displays of any kind hang on them.

思路：沿用先前「相機入鏡」那次成功的修法邏輯——**否定句擋不住，改成正面描述該有什麼**。

| 測試 | 對照原圖 | 結果 |
|---|---|---|
| `F203` tammy-chou D2 | `072`（牆上大幅海報＝她的臉，臉寬 168px） | ✅ 牆上只剩公告與價目表等純文字，無任何人像 |
| `F204` wendy-yeo D2 | `082`（牆上三張證件照＝她的臉） | ✅ 同上 |

**假設判定：2/2 通過。**

## 意外收穫：手機螢幕不再顯示她自己的臉

使用者指出「每個人設的對鏡自拍基本上都失敗了，手機螢幕上會顯示人設自己的臉」——**她是對的，我判錯了。**
我在 `VERDICT_daily140.md` 第五節把 D2 的第二張臉寫成「手機前鏡頭預覽，屬預期非缺陷」。
物理上是反的：對鏡自拍時螢幕朝著她自己、背對鏡子，鏡子裡看到的應該是**手機背面與鏡頭模組**。
螢幕上出現她的臉是錯的。**該段判定作廢。**

`F203`、`F204` 兩張都畫出了**手機背面與鏡頭模組**，是物理正確的。

**可能的機制（假設，n=2，未驗證）**：我原本那句否定裡自己寫了
「no portrait or photograph of a person on any wall **or screen**」——
把「螢幕上有一張人臉」這個概念直接餵進畫面。移掉那句之後螢幕就正常了。
這條要用更多樣本驗，現在不能當結論。

## 這 4 張沒有解決的事

- **動作／構圖模組化**（見 `FINDING_pose_module.md`）：`F203`、`F204` 仍是同一組
  「重心後腳、上身三分之三轉、拇指勾腰頭」的庫存動作。修法 A/B 只動背景與牆面，碰不到這件事。
- `wendy-yeo` 仍明顯超過二十幾歲。
- 取景仍塌向膝上。
