#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生 review/REVIEW_BATCH3_FACES_R8.md —— 實測結果與 19 張新來源的數值規格。"""
import json, io, subprocess

D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))['personas']
P = json.load(open('pilot/r8_source_plan.json', encoding='utf-8'))
T = json.load(open('pilot/geometry_targets.json', encoding='utf-8'))
G = json.load(open('pilot/ref_geometry.json', encoding='utf-8'))
COMMIT = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                        capture_output=True, text=True).stdout.strip()
SL = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
SLZH = {'FACE_SHAPE_AND_JAW': '臉型顎線', 'EYES_AND_BROWS': '眼與眉',
        'NOSE': '鼻', 'MOUTH': '口'}
AXZH = {'face_hw': '臉長寬比', 'jaw_ratio': '顎寬比', 'third_mid': '中庭佔比',
        'third_low': '下庭佔比', 'eye_space': '眼距比', 'eye_open': '眼開合比',
        'alar_r': '鼻翼比', 'mouth_r': '口寬比', 'lip_r': '唇厚比'}
DEF = {
 'face_hw':   '臉高（髮際點 10 → 頦下 152 的垂直距）÷ 臉寬（左右顴弓 234–454）',
 'jaw_ratio': '下顎角寬（172–397）÷ 臉寬',
 'third_mid': '（眉間 9 → 鼻下 2）÷（髮際 10 → 頦下 152）',
 'third_low': '（鼻下 2 → 頦下 152）÷（髮際 10 → 頦下 152）',
 'eye_space': '內眥間距（133–362）÷ 左右眼裂寬的平均',
 'eye_open':  '上下眼瞼開度平均（159–145、386–374）÷ 眼裂寬平均',
 'alar_r':    '鼻翼基部寬（98–327）÷ 臉寬',
 'mouth_r':   '口角間距（61–291）÷ 臉寬',
 'lip_r':     '唇高（0–17）÷ 口角間距',
}
AX = list(AXZH)
real = [v for k, v in G.items() if int(k.split('_')[1]) <= 15]
syn = [v for k, v in G.items() if int(k.split('_')[1]) >= 16]

o = io.StringIO(); w = o.write
w(f"""# Batch 3 臉部規劃 — R8：分離度實測不過，需要按數值重生參考圖

## §0 給審閱者

**你只需要讀這一個檔案。** 回覆請寫在檔案最末 `REPLIES BELOW` 那一行底下
（那一行要獨立成行），我只讀最後一次出現的那一行以後的內容，其餘會被下一版覆蓋。
倉庫 commit `{COMMIT}`。

R7 我全部照做了：ref_30–33 驗過（SHA-256 相符、16 張裁切我自己重跑 builder 產出、
QA 全過），76 格分配已套用，來源使用量重算 16/15/9/12 與你的數字一致。

**但在排第一批之前我多做了一件事，結果推翻了「可以開始生成」這個結論。**

我量了「實際會被餵進生成的那些裁切，彼此的形狀比例差多少」。
這跟 K-05 那張註冊表量的不是同一件事——那張量的是規格形容詞之間的距離，
結果 4 張臉零碰撞卻長成同一個人。這次量 landmark 實測比例，中間不隔形容詞。
數字不好看，所以我花 6 credits 直接生圖驗證，沒有用推論代替實測。

---

## §1 實測：gate 不過的那一對，真的是同一張臉

把上一批「看起來不一樣」的東西全部拿掉——同髮型（全部往後梳綁起、露出髮際線與
整條下顎線）、完全不上妝、同一件灰色圓領 T、同一種正面平光、同樣的證件照構圖。
剩下唯一能不同的就是骨架。

| 組 | 人物 | 為什麼選這一對 |
|---|---|---|
| 實驗組 | emma-kao ↔ wendy-yeo | 舊 gate 判定不過，實測輸入距離第 2 近（0.55）；兩人共用 ref_16 當臉型來源 |
| 對照組 | rin-ayase ↔ sydney-leong | 171 組裡輸入距離最遠（2.41），四個來源完全不重疊 |

實驗組各抽 2 張（順便量同一人不同抽的雜訊底線），對照組各抽 1 張。
圖在 `review/separation_test/`，`compare_gate_fail.jpg` 與 `compare_control.jpg` 是對照圖。

| 比較 | 輸出實測距離 | 判讀 |
|---|---|---|
| 同一人不同抽 emma_1 ↔ emma_2 | 0.57 | 雜訊底線 |
| 同一人不同抽 wendy_1 ↔ wendy_2 | 0.32 | 雜訊底線 |
| **emma-kao ↔ wendy-yeo** | **0.36** | **比雜訊還小＝同一張臉** |
| **rin-ayase ↔ sydney-leong** | **1.19** | **雜訊的 2–4 倍＝清楚是兩個人** |

肉眼與數字一致。

**三件事因此確定：**

1. **pipeline 是好的。** 對照組證明裁切重混確實生得出不同的人。上一批「五官全都太像」
   不是方法錯，是配對太近。這一點我要講清楚，因為它決定我們不必推翻整套做法。
2. **相符度不蘊含分離度。** emma-kao 與 wendy-yeo 各自都符合自己的規格，
   你排的來源在幾何上也都對，但兩人就是同一張臉。這是兩個獨立條件。
3. **門檻是輸入距離 1.02。** 兩點校準 `輸出 ≈ 0.45 × 輸入 + 0.11`，雜訊底線取 0.57，
   反推得 1.02。用它掃 171 組，**30 組不合格**（舊的形容詞 gate 只抓到 9 組）。

---

## §2 根因：形容詞沒錯，是每個形容詞都被畫成中位數

你的 18 張合成圖，每一張的形容詞都對。問題是同一個形容詞——例如「寬顎」——
你一律畫在池子中位數附近，於是 19 位人物擠在很窄的一條帶裡。

| 軸 | 真人照 ref_01–15 | 你的合成池 ref_16–33 | 幅寬比 |
|---|---|---|---|""")
for a in ['alar_r', 'mouth_r', 'third_mid', 'third_low', 'lip_r', 'face_hw', 'eye_space']:
    r = [v[a] for v in real]; s = [v[a] for v in syn]
    rs, ss = max(r) - min(r), max(s) - min(s)
    w(f"\n| {AXZH[a]} | {min(r):.3f}–{max(r):.3f} | {min(s):.3f}–{max(s):.3f} | {ss/rs:.2f}x |")
w(f"""

三庭是垂直比例，最不受 yaw 影響，也就是這張表裡最乾淨的兩列。

**眼距這一列請特別看：** 你 18 張全部落在 1.357–1.528，
真人照是 1.119–1.346——**兩段完全不重疊**。也就是說在你的池子裡，
「窄眼距」的意思是「比我其他張沒那麼寬」，不是真的窄。

我用兩次搜尋確認了問題在哪：

- **只看幾何、不管相符度**：18 張來源重排，最差的一對可以從 0.535 拉到 **1.190**，過門檻。
- **在你已認可的相容集合內重排**：**一格都動不了**。相容集合把每格幾乎鎖死成單一選項。

所以卡點不是來源數量，是「每個來源都要符合該 persona 的指定軸值」與
「人跟人要夠遠」在這個池寬下無法同時成立。

**但你的形容詞規劃本身沒問題。** 我把 11 條形容詞軸翻成 9 條可量測的數值窗
（窗的上下界取自真人照的實測範圍，不是我定的），在窗內求最佳解，
**最小配對距離可以到 2.29**，是門檻的兩倍多。
也就是說：不必改任何一位的軸值，只要把同一個形容詞畫到它該有的幅度就夠了。

---

## §3 量測方法（你可以拿去核，但你自己跑不了，所以由我量）

全部用 mediapipe face_landmarker 478 點，以下標號是它的 canonical index。
比值都用臉寬或眼裂寬正規化，所以跟拍攝距離無關。

| 軸 | 定義 |
|---|---|""")
for a in AX:
    w(f"\n| {AXZH[a]} | {DEF[a]} |")
w(f"""

**你沒辦法自己驗這些數字**，所以流程是：你生圖 → 我量 → 我把實測值與目標的差回報給你 →
不夠的重生。請往極端方向畫，因為「回歸中位數」正是這次已經量到的失敗模式。

---

## §4 要生的 19 張圖（ref_40–ref_58）

結構沿用你做 ref_30–33 的方式：**一張圖同時供應四位不同人物的四個不同槽位**，
所以沒有任何一張圖等於任何一位人物的完整長相。
排法是循環錯位（第 k 張帶第 k 位的臉、k+1 的眼、k+2 的鼻、k+3 的口），
我已用程式驗證：四槽互異違規 0、(來源,槽) 重用違規 0、
**若每張都命中目標，171 組的最小配對距離 {P['min_pair_if_hit']:.2f}**（門檻 {P['threshold']}）。

拍攝條件與 ref_16–33 完全相同（標準正面、頭髮往後梳綁起、無妝、灰 T、平光、無輸入影像、
不參考真人或公眾人物）。**只有幾何要改。**

每張圖底下列的是「這張圖的哪個部位要做到什麼數值」。
括號裡是該軸在你現有 18 張裡的實際範圍，用來看要往哪邊推、推多遠。
""")

for rid in sorted(P['images'], key=lambda r: int(r.split('_')[1])):
    img = P['images'][rid]
    w(f"\n### {rid}\n\n| 部位 | 供給 | 軸 | 目標值 | 你現有 18 張的範圍 | 方向 |\n|---|---|---|---|---|---|")
    for slot in SL:
        e = img[slot]
        for a, tv in e['targets'].items():
            s = [v[a] for v in syn]
            if tv > max(s):   d = f'**高於你所有 18 張**'
            elif tv < min(s): d = f'**低於你所有 18 張**'
            else:
                med = sorted(s)[len(s)//2]
                d = '略高於中位' if tv > med else ('略低於中位' if tv < med else '中位')
            w(f"\n| {SLZH[slot]} | {e['for_persona']} | {AXZH[a]} | **{tv:.3f}** | {min(s):.3f}–{max(s):.3f} | {d} |")
    w("\n")

w(f"""
---

## §5 生成後的分配表

| persona | 臉型顎線 | 眼與眉 | 鼻 | 口 |
|---|---|---|---|---|""")
for p in sorted(P['assignment']):
    a = P['assignment'][p]
    w(f"\n| {p} | {a['FACE_SHAPE_AND_JAW']} | {a['EYES_AND_BROWS']} | {a['NOSE']} | {a['MOUTH']} |")

w(f"""

---

## §6 我要你確認的四件事

- **(M-01)** P0：生成 §4 的 19 張圖。數值命中比形容詞漂亮重要——
  如果某一格的數值做不到，直接講哪一格、做得到多少，不要用形容詞含混過去。
- **(M-02)** P0：§4 的目標值是我從你的形容詞規劃推出來的
  （形容詞 → 數值窗 → 窗內最佳化）。有沒有哪一格你認為數值與該 persona 的
  形容詞相牴觸？有就指出來並給替代值。
- **(M-03)** P1：§1 的結論你同不同意——「pipeline 是好的，失敗在配對太近，
  不在方法」？如果你認為還有第三種解釋，現在講。
- **(M-04)** P1：舊的 18 張（ref_16–33）在新圖到位後怎麼處理？
  我的想法是保留不刪，但分配表全部改用新圖，因為混用會把窄帶重新帶回來。
  你同意還是有部分值得留用？

生成後的順序不變：我量測 → 不合格的重生 → 重跑 171 組 gate → 排第一批。

REPLIES BELOW
""")

OUT = 'review/REVIEW_BATCH3_FACES_R8.md'
body = o.getvalue()
try:
    old = open(OUT, encoding='utf-8').read().split('\n')
    hits = [i for i, ln in enumerate(old) if ln.strip() == 'REPLIES BELOW']
    if hits:
        kept = '\n' + '\n'.join(old[hits[-1] + 1:])
        if kept.strip():
            body = body.rstrip('\n') + kept
except FileNotFoundError:
    pass
open(OUT, 'w', encoding='utf-8').write(body)
print(f'已產生 {OUT}（{len(body):,} 字元）')
