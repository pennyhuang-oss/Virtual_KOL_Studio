#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生 review/REVIEW_BATCH3_FACES_R9.md —— 6 張取景重拍（幾何不變）。"""
import json, io, subprocess, sys
sys.path.insert(0, 'tools')

BAD = ['ref_41', 'ref_46', 'ref_48', 'ref_50', 'ref_51', 'ref_55']
SL = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
SLZH = {'FACE_SHAPE_AND_JAW': '臉型顎線', 'EYES_AND_BROWS': '眼與眉',
        'NOSE': '鼻', 'MOUTH': '口'}
AXZH = {'face_hw': '臉長寬比', 'jaw_ratio': '顎寬比', 'third_mid': '中庭佔比',
        'third_low': '下庭佔比', 'eye_space': '眼距比', 'eye_open': '眼開合比',
        'alar_r': '鼻翼比', 'mouth_r': '口寬比', 'lip_r': '唇厚比'}
SLOT_AX = {'FACE_SHAPE_AND_JAW': ['face_hw', 'jaw_ratio', 'third_mid', 'third_low'],
           'EYES_AND_BROWS': ['eye_space', 'eye_open'],
           'NOSE': ['alar_r'], 'MOUTH': ['mouth_r', 'lip_r']}

P = json.load(open('pilot/r8_source_plan.json', encoding='utf-8'))
G = json.load(open('pilot/ref_geometry.json', encoding='utf-8'))
man = json.load(open('pilot/face_crops_manifest.json', encoding='utf-8'))['artifacts']
COMMIT = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                        capture_output=True, text=True).stdout.strip()
# 取景實測（build_face_crops 的 landmark，重算一次以免抄錯）
from build_face_crops import landmarks
FR = {}
for n in range(40, 59):
    r = f'ref_{n}'
    pts, (W, H) = landmarks(f'review/batch3_face_refs/{r}.jpg')
    FR[r] = {'fh': (pts[152][1] - pts[10][1]) / H, 'fw': (pts[454][0] - pts[234][0]) / W,
             'ar': W / H, 'wh': (W, H),
             'pad': man[f'{r}__FACE_SHAPE_AND_JAW__v1']['qa_metrics']['padding_ratio']}
OVER = {'ref_41': '頭頂上方缺 20% 臉高、左右各缺 3–5% 臉寬',
        'ref_46': '頭頂上方缺 24% 臉高、下巴下方缺 1% 臉高',
        'ref_48': '頭頂上方缺 13% 臉高、左右各缺 14–15% 臉寬',
        'ref_50': '頭頂上方缺 26% 臉高',
        'ref_51': '頭頂上方缺 34% 臉高',
        'ref_55': '頭頂上方缺 15% 臉高、左右各缺 9% 臉寬'}

o = io.StringIO(); w = o.write
w(f"""# Batch 3 臉部規劃 — R9：6 張取景重拍，幾何完全不變

## §0 給審閱者

**你只需要讀這一個檔案。** 回覆請寫在檔案最末 `REPLIES BELOW` 那一行底下
（那一行要獨立成行）。倉庫 commit `{COMMIT}`。

**先講結論：R8 那批成功了。** 19 張的幾何做到了該做的事：

| | 舊池 ref_16–33 | 新池 ref_40–58 |
|---|---|---|
| 最小配對距離 | 0.50 | **1.48** |
| 中位 | 1.37 | 3.36 |
| 低於 1.02 的組數 | 29 | **0** |

我另外花 4 credits 實測驗證：最接近的可測配對 cheryl-soh ↔ wanyin-jiang
（輸入 1.51）輸出距離 **1.22**，是雜訊底線 0.38 的三倍以上，肉眼確實是兩個人。
對照上一輪 emma-kao ↔ wendy-yeo 的 0.36（比雜訊還小）。圖在
`review/separation_test/r8/compare_r8.jpg`。

**這一輪要你做的事很小：6 張圖的取景重拍，幾何一格都不要動。**

---

## §1 你在 M-03 提的統計限制，我採納並修正了

你說 `輸出 ≈ 0.45 × 輸入 + 0.11` 只有兩端校準、不能當普遍定律。你是對的，
而且新的實測直接推翻了那條線：

| 輸入距離 | 該線的預測 | 實測輸出 |
|---|---|---|
| 0.55 | 0.36 | 0.36 |
| **1.51** | **0.79** | **1.22** |
| 2.41 | 1.19 | 1.19 |

1.51 的實測遠好於外推，而更遠的 2.41 反而只有 1.19——關係不是線性的。
我已把那條線從文件裡拿掉，改成不需要擬合的說法：
**實測到輸入 ≥1.5 時輸出都在 1.19 以上，是雜訊底線的三倍以上。**
1.02 繼續當保守 gate，但現在標明它的來源是外推、不是實測。

## §2 M-01／M-02／M-04 的結果

- **M-01**：19 張 SHA-256 全部相符，我逐張量了九軸。171 格目標裡 33 格落在 ±0.5sd 內。
  命中率不高，但**目標是手段、分離度才是目的**，目的達成了，所以我不打算為命中率再跑一輪。
  唯一值得記下的系統性偏差是**眼距**：目標 1.12–1.34，19 張實測全部落在 1.44–1.63。
  這看起來是生成端做不到窄眼距，不是 19 次各自失手——**下次規劃不要再依賴窄眼距當分離軸。**
- **M-02**：沒有形容詞反轉，同意保留全部目標值。
- **M-04**：同意。ref_16–33 保留不刪，全部退出 active pool，標
  `legacy_narrow_band` / `excluded_from_separation_pool`，只作 provenance、
  回歸測試與失敗對照。我不會混用。

---

## §3 要重拍的 6 張：只有取景要改

這 6 張的**幾何都是可用的**，它們就是撐起 1.48 那個最小距離的一部分。
問題純粹是頭在畫面裡拍太滿，臉型裁切框擴到 4:5 時撞出畫面外，
padding 超過 12% 上限。

| ref | 原圖尺寸 | 長寬比 | 臉高佔畫面 | 臉寬佔畫面 | padding | 撞出畫面的方向 |
|---|---|---|---|---|---|---|""")
for r in BAD:
    f = FR[r]
    w(f"\n| {r} | {f['wh'][0]}×{f['wh'][1]} | {f['ar']:.2f} | {f['fh']:.0%} | {f['fw']:.0%} | {f['pad']:.0%} | {OVER[r]} |")

good = [r for r in FR if r not in BAD]
w(f"""

對照通過的 13 張，規律很清楚：

- **三張是橫幅**（ref_46、ref_50、ref_51，長寬比 1.50）。橫幅一定過不了，
  因為臉型裁切是 4:5 的直幅，橫幅畫面高度根本不夠。
- **另外三張是頭拍太大**（ref_48 臉寬佔畫面 68%、ref_55 佔 63%、ref_41 佔 59%），
  裁切框往兩側擴的時候出界。

通過的 13 張臉高佔畫面 {min(FR[r]['fh'] for r in good):.0%}–{max(FR[r]['fh'] for r in good):.0%}，
臉寬佔畫面 {min(FR[r]['fw'] for r in good):.0%}–{max(FR[r]['fw'] for r in good):.0%}。

### 重拍規則（這兩條照做就會過）

1. **直幅**，長寬比 3:4 到 2:3 之間。**不要橫幅、不要正方形。**
2. **頭要拍小**：髮際線到下巴 **≤ 畫面高的 45%**，左右耳外緣 **≤ 畫面寬的 50%**。
   頭頂上方要留出明顯的空白——寧可留太多，裁切是我這邊做，多的我會裁掉，
   少的我補不回來。

其餘條件與 ref_40–58 完全相同（標準正面、頭髮往後梳綁起、無妝、灰 T、
平光、無輸入影像、不參考真人或公眾人物）。

---

## §4 每張要保住的幾何

**重要：不要照 R8 §4 的原始目標重畫。** 那批目標有不少沒命中，
但**實際做出來的數值才是我算出 1.48 那個結果所用的值**。
所以請以「現在這張的實際長相」為準去重拍，只把鏡頭拉遠。

下表是我實測到的值，也就是要保住的值。括號是 R8 的原始目標，僅供參考。
""")
for r in BAD:
    img = P['images'][r]
    w(f"\n### {r}\n\n| 部位 | 供給 | 軸 | 要保住（實測） | R8 原始目標 |\n|---|---|---|---|---|")
    for slot in SL:
        e = img[slot]
        for a in SLOT_AX[slot]:
            w(f"\n| {SLZH[slot]} | {e['for_persona']} | {AXZH[a]} | **{G[r][a]:.3f}** | {e['targets'][a]:.3f} |")
    w("\n")

w(f"""
---

## §5 這 6 張擋住誰

| ref | 臉型供給 | 其他三槽供給 |
|---|---|---|""")
for r in BAD:
    img = P['images'][r]
    others = '、'.join(f"{img[s]['for_persona']}（{SLZH[s]}）" for s in SL[1:])
    w(f"\n| {r} | **{img['FACE_SHAPE_AND_JAW']['for_persona']}** | {others} |")
w(f"""

只有臉型槽卡住，其他三槽的裁切都已通過 QA，所以**這 6 張重拍後我只會重裁臉型槽**，
其餘不動。被擋住的 6 位是 angeline-kwee、miu-shiraishi、peggy-lee、
ruoruo-tang、somi-oh、wendy-yeo。

**另外 13 位我已經開始跑選角了**，不等這 6 張——它們不影響那 13 位的任何一格。

---

## §6 要你確認的三件事

- **(N-01)** P0：重拍 §3 的 6 張，規則就那兩條（直幅、頭拍小）。
  幾何以 §4 的實測值為準，不要回頭照原始目標重畫。
- **(N-02)** P1：§2 記的那條「眼距做不到窄」，你那邊有沒有辦法突破？
  如果沒有，我下一輪規劃就不把窄眼距當分離軸用。
  做不到就直說做不到，不要為了回答而回答。
- **(N-03)** P2：ref_49 我看起來比 persona 年齡（24–28）老不少，
  也偏清瘦憔悴。它目前供給 zoey-yeh 的臉型。幾何與 QA 都過了，
  所以我不打算擋它——但裁切會帶進皮膚質地，先跟你確認這是有意的還是要換。

REPLIES BELOW
""")

OUT = 'review/REVIEW_BATCH3_FACES_R9.md'
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
