# R1 複核回覆的查證結果

**日期**：2026-09-11　**查證者**：Claude Code
GPT 的回覆在 `REVIEW_DAILY_V4_R1_GPT.md`。以下逐條實測，**不採信、只驗算**。

## 一、他說對的（全部實測通過）

| 他的主張 | 我的實測 | 結論 |
|---|---|---|
| 16/16 的浴室格都用 selfie | `Counter({'selfie': 16})` | ✅ |
| 格位被鎖死 | 第 2 格 16/16 私下、第 3 格 16/16 私下（13 格浴室）、第 4 格 10/16 工作、第 5 格 12/16 外出 | ✅ |
| `build_v4.py` 定義了 `low` 鏡位但 80 格沒用到 | 實際鏡位只有 near/selfie/knee/floor/full | ✅ |
| `P1` 牆上有汽車海報，WALL 守則卻禁止任何 poster | `P1` place：*a poster of a car on the wall*；WALL：*no framed pictures, posters or displays of any kind* | ✅ **直接矛盾** |
| `J2` 手機螢幕停在練習影片，WALL 卻規定 screen 只能是 plain surfaces and printed text | 兩句同時出現在 `J2` 的 prompt | ✅ **直接矛盾** |
| MIRROR_GUARD 只掃 `place`+`action`，漏掉 `light` | `build_v4.py:63` 確實只掃這兩欄 | ✅ |
| `T1` 的鏡子只留在 `light`，因此沒插 guard | `T1` light：*the mirror throws it back*；prompt 無 guard | ✅ |
| 中文 spec 與 en 只核對格號、不核對內容 | `validate_v4.py` 只比 id 序列 | ✅ |

我另外自己加驗的一條，**比他講的更嚴重**：

> **80 格裡有 15 格帶反射面卻沒有 MIRROR_GUARD**，
> 其中 6 格是浴室自拍（`C4` `M3` `R3` `D3` `T3` `W4`）——鏡子就在她正前方。
> 有 guard 的只有 15 格。**等於一半的鏡面場景是沒有防線的。**
> 這正是 v1 `jia-seo D5` 失敗的同一個成因（守則在 v1→v2 改寫時被靜默丟掉）。

`T1` 還有第二層問題：我上一輪「把 T1 改寫成前鏡頭自拍、移除鏡子」只改了英文的
`place`/`action`，**中文 spec 至今仍寫著「落地鏡前…一手舉著手機」**，英文 `light` 也仍寫著
鏡子把光反回來。這一格在三份檔案之間是不一致的。

他點名的 screen 衝突我複驗後是 **`J2` 與 `S2` 兩格**為真；`P2`（擋風玻璃）、`Y2`／`Y3`
（sunscreen 命中 screen 字串）、`Z3`（淋浴玻璃隔間）是我的偵測誤判，不是真衝突。

## 二、我不採納他的部分

**Q5 他建議的替代守則句用回否定式**：*No human faces or portraits appear on walls or screens.*

這跟 `VERDICT_rulefix_v1.md` 的實測結論相反。那次 4 張測試裡，Fix B 的有效做法正是
**把否定句改成正面描述**（描述牆上有什麼，而不是宣告牆上沒有什麼），2/2 通過。
樣本只有 n=2、未複驗，但那是我們手上唯一的實測資料，不應該被沒有實測的建議推翻。

**採納他要縮短、要條件化、要修掉 WALL 與海報／螢幕衝突的部分；
不採納把正面描述改回否定句。** 縮短後的句子應維持正面描述，只是不再強迫每面牆長出標示牌。

## 三、待使用者裁決

1. 是否退回重做規劃（拆五格骨架、加回路人、日夜各半）。
2. 膚質 D3 與 character.md 的衝突怎麼解。
3. 16 格探針 vs 80 格全拍。
