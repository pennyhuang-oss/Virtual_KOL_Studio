#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生 review/REVIEW_BATCH3_FACES_R5.md —— 探針結果與眼／鼻／口三槽的來源盤點。"""
import json, io, subprocess, itertools, sys
from collections import Counter
sys.path.insert(0, 'tools')
from check_part_sources import rows as PARTROWS

D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
R = json.load(open('pilot/face_refs_readout.json', encoding='utf-8'))['refs']
P, AX = D['personas'], D['axes']
ALL = list(AX)
DOM = ['輪廓原型', '臉長寬比', '三庭配置', '骨肉量', '顎頦', '眼眶結構']
B1 = D['batch1']
refs = lambda p: P[p].get('refs_v2') or P[p]['refs']
COMMIT = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                        capture_output=True, text=True).stdout.strip()
RAW = "https://raw.githubusercontent.com/pennyhuang-oss/Virtual_KOL_Studio/main"
NEW = [f'ref_{i}' for i in range(16, 24)]

fails = []
for a, b in itertools.combinations(P, 2):
    diff = [x for x in ALL if P[a]['axes'][x] != P[b]['axes'][x]]
    dm = [x for x in diff if x in DOM]
    sh = refs(a)['FACE_SHAPE_AND_JAW'] == refs(b)['FACE_SHAPE_AND_JAW']
    nn, nd = (7, 3) if sh else (6, 2)
    if len(diff) < nn or len(dm) < nd:
        fails.append((len(diff), nn, len(dm), nd, a, b, diff))
fails.sort()
rebuild = sorted(set([p for p in P if P[p].get('needs_rebuild')] +
                     ['emma-kao', 'kanon-komori', 'miu-shiraishi', 'somi-oh']))
contra = [r for r in PARTROWS if r['contradictions']]
lows = [r for r in PARTROWS if r['usability'] == 'low']

o = io.StringIO(); w = o.write
w(f"""# Batch 3 臉部規劃 — R5：技術探針的結果，以及部件被執行之後浮出的問題

## §0 給審閱者

**你只需要讀這一個檔案。**

你在 R4 的 H-05 指定先跑 `wendy-yeo` 4 張技術探針，驗證「Image 1–4 各自只控制指定部件」這個假說。
**我跑了，而且跑了兩版**——你的原方法，以及你在 F-01 就寫好的備案。結果決定性地分開了（§1）。

備案通過之後，浮出一個在此之前看不見的問題：**部件一旦真的被執行，來源選錯就會直接畫在臉上。**
我把眼／鼻／口三槽做了你替 `FACE_SHAPE_AND_JAW` 做過的那種盤點，
找到 **{len(contra)} 組規格與來源明確矛盾**、**{len(lows)} 個指派用 low 可用度的來源**（§3）。

**回覆方式**：寫在本檔案最下方 §7 回覆區（自成一行的 `REPLIES BELOW` 之後），然後 commit。

- 目前 commit：`{COMMIT}`
- 議題編號從 **J-01** 起跳
- 你 R4 補的 8 張新圖我逐張核對過骨架方向，與你宣稱的缺口相符；
  `tools/check_face_ref_sources.py` 8/8 通過；臉型來源 high 從 10/19 提升到 15/19，
  `low` 全部退出臉型池，cap-2 成立。**這一輪沒有任何對那 8 張的意見。**

---

## §1 探針結果：全臉多圖失敗，部件裁切通過

成本 8 credits（兩版各 4 張）。判定門檻沿用你 F-01 的「4 張中至少 3 張穩定呈現各槽指定部件」。

出圖對照：`{RAW}/review/batch3_probe_A_vs_B.jpg`
（上排＝輸入部件，中排 A1–A4＝全臉多圖，下排 B1–B4＝部件裁切）

### A 版：四張**完整人臉**當參考（你的原方法）— **不通過**

附圖 `[ref_11 臉型, ref_13 眼眉, ref_02 鼻, ref_06 口]`，未裁切。

| 槽位 | 來源判讀 | 出圖 | 判定 |
|---|---|---|---|
| Image 1 臉型與下顎 | ref_11：中長、輪廓近直線、顎相對寬而平直、下巴鈍方 | 短窄柔臉、下巴小而收、**完全看不到顎角** | ✗ |
| Image 2 眼與眉 | ref_13：大而圓、寬雙眼皮 | 大而圓、寬雙眼皮 | ～ 與模型預設臉無法區分 |
| Image 3 鼻 | ref_02：長、直、窄 | 小而短 | ✗ |
| Image 4 口 | ref_06：小而飽滿 | 小而飽滿 | ～ 同上 |

四張候選是同一張臉，而那張臉是模型的預設美人臉：小 V 下巴、大雙眼皮眼、小鼻、小豐唇。
整體 gestalt 最接近 `ref_06`——**全批濾鏡最重的那張完整人臉吃掉了整個身分**。
這正是你在 F-01 預想的失敗模式（「模型可能平均四張完整人臉，甚至偏向其中一張」）。

### B 版：部件裁切（你 F-01 的既定備案）— **通過**

同樣四個來源、同樣的角色與髮色，Image 2–4 改成只保留該部位的裁切。

| 槽位 | 出圖 | 判定 |
|---|---|---|
| Image 1 臉型與下顎 | **臉明顯變長變寬、顎角看得出來、下巴轉方**，四張一致 | ✓ |
| Image 2 眼與眉 | 與裁切圖的大而圓寬雙眼皮一致 | ✓ |
| Image 3 鼻 | 中長、直、窄，與裁切圖一致 | ✓ |
| Image 4 口 | 中等飽滿、唇線清楚 | ～ 難以歸因 |

**3/4 以上成立，通過門檻。**

### ⚠ 一個我必須先講清楚的實驗瑕疵

**A 與 B 之間我同時改了兩件事**，所以嚴格說不能把改善單獨歸因給裁切：

1. Image 2–4 從完整人臉改成部件裁切；
2. prompt 的指派句也改寫了。A 版是
   `Using the four attached reference images in input order: Image 1 defines the face shape and jawline; …`（你 R2 指定的字），
   B 版改成
   `The four attached images are cropped body parts, not four people: Image 1 is a whole face showing only the outline and jawline to copy; Image 2 is a crop of an eye and brow region; … Take the face outline and jawline from Image 1, … and assemble those four parts into one coherent new face.`

另外 **Image 1 在 B 版仍然是一張完整的臉**（只裁到頭肩），不是輪廓裁切。

**J-01｜要不要花 4 credits 跑一次消融實驗**（維持 B 版的裁切，但把指派句改回你 R2 的原字），
把「裁切」與「措辭」拆開？我的看法：值得，因為之後 19 位都要吃這個決定，
而且如果其實是措辭在起作用，那 76 張裁切圖的工就省下來了。

---

## §2 如果採用部件裁切，裁切規格要你訂

我這次的做法（供你評斷，不是既定規格）：

| Image | 內容 | 這次的做法 |
|---|---|---|
| 1 臉型與下顎 | 整張臉 | 裁到頭肩，含髮際到下巴以下，兩側到耳外緣 |
| 2 眼與眉 | 橫帶 | 從眉上緣到下眼瞼下方，**含雙眼**，兩側到眼尾外 |
| 3 鼻 | 方框 | 鼻根到鼻下緣，兩側到鼻翼外 |
| 4 口 | 方框 | 人中到下唇下緣，兩側到嘴角外 |

**J-02｜請訂下正式規格**，至少要涵蓋：

1. Image 1 到底該是整張臉、還是去背只留臉部輪廓？（去背可能更純，也可能讓模型失去比例參照）
2. 眼睛要**雙眼**還是**單眼**？雙眼會同時帶入眼距，單眼不會——而眼距是你維度表裡獨立的一條軸。
3. 每張裁切要不要統一長寬比與解析度？（我這次沒統一）
4. 裁切圖要不要一併寫進 manifest 並存進 repo？（我這次存了，在 `kols/wendy-yeo/images/a0_probe_crop/inputs/`）
5. 76 張裁切（19 位 × 4 槽）由誰產生、用什麼準則框定？

---

## §3 眼／鼻／口三槽的來源盤點

這是探針 B 通過之後才成立的問題：**在 A 版，來源選錯看不出來，因為根本沒執行。**

### 3.1 集中度

""")
for slot in ['EYES_AND_BROWS', 'NOSE', 'MOUTH']:
    c = Counter(refs(p)[slot] for p in P)
    nlow = sum(1 for p in P if R[refs(p)[slot]]['usability'] == 'low')
    w(f"**{slot}**（最高集中 {c.most_common(1)[0][1]} 位；用 low 來源 {nlow} 位）\n\n")
    w("| 來源 | 可用度 | 供給 | 是哪幾位 |\n|---|---|---|---|\n")
    for k, v in c.most_common():
        who = [p for p in P if refs(p)[slot] == k]
        w(f"| `{k}` | {R[k]['usability']} | {v} | {'、'.join(who)} |\n")
    w("\n")

w(f"""### 3.2 {len(contra)} 組規格與來源明確矛盾

判定方式：只在「規格與來源判讀互斥」時才列（例如規格要單眼皮、來源是雙眼皮）。
判斷不了的一律不列，交給你。

| persona | 槽位 | 來源 | 可用度 | 該角色的規格 | 來源的判讀 | 矛盾 |
|---|---|---|---|---|---|---|
""")
for r in contra:
    b1 = ' 🔵' if r['persona'] in B1 else ''
    w(f"| `{r['persona']}`{b1} | {r['slot'].replace('_AND_','／').replace('EYES／BROWS','眼眉').replace('NOSE','鼻').replace('MOUTH','口')} "
      f"| `{r['ref']}` | {r['usability']} | {r['spec']} | {r['readout'][:44]} | {'；'.join(r['contradictions'])} |\n")

w(f"""
🔵 = 第一批 8 位

**最尖銳的一組是 `wendy-yeo` 的眼睛**：她的規格是**單眼皮窄平視**——
那是全庫 13 位已訓練角色都沒有的稀有值，也是她整個角色最強的辨識點。
但她被指派的 `ref_13` 是大而圓的寬雙眼皮。探針 B 的四張出圖，眼睛全部照著 `ref_13` 畫。

**J-03｜這 {len(contra)} 組要怎麼處理？** 每一組是換來源、還是改規格去遷就來源？
（我的看法：規格是你依角色人設設計的，來源只是素材，應該換來源。但 wendy 的單眼皮
在現有 {len(R)} 張裡幾乎找不到——`ref_17` 的判讀是「細長眼、低眉」，最接近，
但它目前被你保留為臉型備援。）

### 3.3 {len(lows)} 個指派仍用 low 可用度的來源

你在 H-01 裁決「`low` 全部標記 `excluded_from_FACE_SHAPE_AND_JAW`，`mid` 可暫作非骨相槽位或備援」。
臉型槽已經清乾淨，但眼／鼻／口三槽仍有 {len(lows)} 個指派落在 low 上：

| persona | 槽位 | 來源 | 該來源為什麼是 low |
|---|---|---|---|
""")
for r in lows:
    w(f"| `{r['persona']}` | {r['slot']} | `{r['ref']}` | {R[r['ref']]['shot']} |\n")

w(f"""
**J-04｜low 來源用在眼／鼻／口可不可以接受？**
探針 B 證明這些槽位現在會被執行，所以「重度美顏的眼睛」也會被照著畫。
你要不要把 `excluded` 規則從臉型擴大到全部四槽？如果擴大，素材就不夠了（見 §4）。

---

## §4 你補的 8 張新圖，眼／鼻／口三槽完全沒用到

`ref_16`–`ref_23` 每一張都有完整四槽判讀（你自己寫的），但目前 **19 位裡沒有任何一位**
把它們用在 EYES_AND_BROWS／NOSE／MOUTH。它們是標準正面、中性、低妝、無濾鏡——
以「部件裁切」的用途來說，條件比原本 15 張裡的多數都好。

| 新圖 | 眼與眉 | 鼻 | 口 |
|---|---|---|---|
""")
for k in NEW:
    v = R[k]
    w(f"| `{k}` | {v.get('eyes_and_brows','—')[:34]} | {v.get('nose','—')[:30]} | {v.get('mouth','—')[:30]} |\n")

w(f"""
**J-05｜要不要把這 8 張也開放給眼／鼻／口三槽？**
如果要，請直接給新的三槽分配（或至少給 §3.2 那 {len(contra)} 組的替代來源）。
注意：同一張圖同時供給某位的臉型與另一位的鼻子，是否可接受？你先前只對「每位四槽必須四張不同圖」定過規則，
沒有定過跨槽位的共用規則。

---

## §5 兩件從 R4 就懸著、還沒解的

### 5.1 H-03：{len(fails)} 組配對仍不過 gate

你在 H-03 說「等補圖後重算」。補圖已入庫，我重算了，**仍有 {len(fails)} 組不過**：

| 總相異／需 | 主導軸／需 | 組合 | 在第一批 |
|---|---|---|---|
""")
for n, nn, dm, nd, a, b, diff in fails:
    inb = '兩位都在' if a in B1 and b in B1 else ('一位在' if (a in B1) ^ (b in B1) else '都不在')
    w(f"| {n}／{nn} | {dm}／{nd} | {a} vs {b} | {inb} |\n")

w(f"""
其中 3 組完整落在第一批 8 位裡。

### 5.2 H-04：{len(rebuild)} 位的文字仍待重建

你在 H-04 列出的 12 位（8 位換源 ＋ H-02 新增的 emma／kanon／miu／somi）：

{'、'.join(f'`{p}`' for p in rebuild)}

這些人的 `refs_v2` 已經是新來源，但 ARCHETYPE／AXES／FACE_EN／MARKERS／WHY_DISTINCT
仍是舊來源寫的。你 R4 說「等補圖」——補圖到位了。

**J-06｜這 {len(rebuild)} 位的重建，要現在做，還是等 J-01 的消融實驗與 J-02 的裁切規格定案後一起做？**
我的看法是等，因為裁切規格會影響 FACE_EN 的指派句寫法，現在重建等於要寫兩次。

---

## §6 輸出格式

- **(J-01)** 消融實驗跑不跑。跑的話請給要測的確切 prompt 措辭。
- **(J-02)** 部件裁切的正式規格，五個問題逐項回答。
- **(J-03)** §3.2 的 {len(contra)} 組矛盾，逐組給「換來源到 X」或「改規格為 Y」。
- **(J-04)** low 來源能不能用在眼／鼻／口。
- **(J-05)** 新 8 張要不要開放給三槽；要的話給分配。跨槽位共用同一張圖的規則。
- **(J-06)** 12 位重建的時機。
- **最後給一句**：下一個可以動手的動作是什麼、成本多少張。

角色欄位如果要改，格式與前幾輪相同：

```
### <persona-id>
ARCHETYPE: <中文一句話原型>
AXES: <11 條全給，分號分隔，值必須在原維度表允許值內>
FACE_EN: <完整英文段落>
NEGATIVE_EN: <否定清單或 NONE>
MARKERS: <3–5 個，英文，分號分隔>
WHY_DISTINCT: <中文一句話>
```

---

## §7 回覆區

REPLIES BELOW
""")

OUT = 'review/REVIEW_BATCH3_FACES_R5.md'
body = o.getvalue()
try:
    old = open(OUT, encoding='utf-8').read().split('\n')
    hits = [i for i, ln in enumerate(old) if ln.strip() == 'REPLIES BELOW']
    if hits:
        kept = '\n' + '\n'.join(old[hits[-1] + 1:])
        if kept.strip():
            body = body.rstrip('\n') + kept
            print(f'保留既有回覆 {len(kept.strip()):,} 字元')
except FileNotFoundError:
    pass
open(OUT, 'w', encoding='utf-8').write(body)
print(f'已產生 {OUT}（{len(body):,} 字元）')
