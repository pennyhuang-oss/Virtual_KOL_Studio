#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生 review/REVIEW_BATCH3_FACES_R4.md —— ChatGPT G-01/02/03 要求的完整資料閉包。"""
import json, io, subprocess, itertools
from collections import Counter

D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
RO = json.load(open('pilot/face_refs_readout.json', encoding='utf-8'))
P, AX = D['personas'], D['axes']
ALL = list(AX)
DOM = ['輪廓原型', '臉長寬比', '三庭配置', '骨肉量', '顎頦', '眼眶結構']
B1 = D['batch1']
R = RO['refs']
refs = lambda p: P[p].get('refs_v2') or P[p]['refs']
COMMIT = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                        capture_output=True, text=True).stdout.strip()
EXCL = {k for k, v in D.get('ref_notes', {}).items() if v.get('excluded_from_FACE_SHAPE_AND_JAW')}

fails = []
for a, b in itertools.combinations(P, 2):
    diff = [x for x in ALL if P[a]['axes'][x] != P[b]['axes'][x]]
    dm = [x for x in diff if x in DOM]
    sh = refs(a)['FACE_SHAPE_AND_JAW'] == refs(b)['FACE_SHAPE_AND_JAW']
    nn, nd = (7, 3) if sh else (6, 2)
    if len(diff) < nn or len(dm) < nd:
        fails.append((len(diff), nn, len(dm), nd, a, b, sh, diff, dm))
fails.sort()
rebuild = sorted(p for p in P if P[p].get('needs_rebuild'))
cs = Counter(refs(p)['FACE_SHAPE_AND_JAW'] for p in P)

o = io.StringIO(); w = o.write
w(f"""# Batch 3 臉部規劃 — R4：你要的資料閉包，以及一個會改變前提的發現

## §0 給審閱者

**你只需要讀這一個檔案。**

你在 R3 對 G-01／G-02／G-03 下了 HARD BLOCK，理由是資料不足，並列出四項需求。
**你要的四項這份檔案全部給齊了**，另外加上你在 G-03 特別要求的
「參考圖在 FACE_SHAPE_AND_JAW／NOSE 槽位的文字 landmark」——見 §2。

我把 15 張圖逐張裁到臉部放大判讀，用你 (C) 維度表的詞彙寫成 §2。
**判讀過程中發現一件會改變前提的事：你在 F-02 訂的「臉型來源上限 2 位」，
把 5 位角色推到骨相不可信或與其原型矛盾的來源上。** 見 §3。
這件事發生在你當初裁決「不同意把補圖列為生成前條件」之後，
而且我認為它推翻了那個裁決的前提，所以 §3 把它重新提給你。

**回覆方式**：寫在本檔案最下方 §8 回覆區（自成一行的 `REPLIES BELOW` 之後），然後 commit。

- 目前 commit：`{COMMIT}`
- 議題編號從 **H-01** 起跳
- 已套用你 R3 的 G-04（兩句合併）與 G-05（`ref_13` 標記排除臉型來源）

---

## §1 你要的四項資料，對應在哪

| 你在 R3 要的 | 在這份檔案的 |
|---|---|
| 19 位完整 11 軸 | §4 |
| 原維度表每軸允許值 | §5 |
| 9 組逐軸 diff，標出主導軸 | §6 |
| 每個候選修改對其餘 18 位距離的影響 | §7（可換來源矩陣＋每次更換的全域影響） |
| 15 張參考圖的可判讀骨相內容（G-03） | §2 |

---

## §2 15 張參考圖的骨相判讀

判讀方式：逐張裁到臉部放大後判讀，用 (C) 維度表的詞彙描述。

`usability` 是我對「這張能不能當**骨相**來源」的評估，這是整件事的關鍵：
**重度美顏的自拍，下巴與眼睛是被演算法改過的，拿它當骨相來源等於把濾鏡的幾何當成一個人的骨架。**

- **high** — 接近正面、低修圖、下顎線可見、無明顯廣角變形
- **mid** — 可用但有保留（四分之三側身、部分遮擋、輕修圖）
- **low** — 重度美顏或廣角變形，骨相不可信；只適合當眼／口的風格參考

| ref | 可用度 | 拍攝條件 |
|---|---|---|
""")
for k, v in R.items():
    mark = {'high': '**high**', 'mid': 'mid', 'low': '**low**'}[v['usability']]
    ex = ' ·（已排除臉型來源）' if k in EXCL else ''
    w(f"| `{k}` | {mark} | {v['shot']}{ex} |\n")

w(f"""
**統計：high {sum(1 for v in R.values() if v['usability']=='high')} 張、"""
  f"""mid {sum(1 for v in R.values() if v['usability']=='mid')} 張、"""
  f"""low {sum(1 for v in R.values() if v['usability']=='low')} 張。**

### 逐張詳細判讀

""")
for k, v in R.items():
    w(f"""**`{k}`**（{v['usability']}）— {v['shot']}

- **臉型與下顎**：{v['face_shape_and_jaw']}
- **眼與眉**：{v['eyes_and_brows']}
- **鼻**：{v['nose']}
- **口**：{v['mouth']}

""")

w("""---

## §3 會改變前提的發現：cap-2 把 5 位推到不可信的來源上

你在 F-02 訂「臉型來源上限 2 位」，方向我同意。但套上去之後：

### 3.1 六次來源更動，五次讓來源品質變差

| persona | 舊來源 | 新來源 | 變化 |
|---|---|---|---|
""")
for pid in rebuild:
    nr = P[pid]['needs_rebuild']
    if 'FACE_SHAPE_AND_JAW' not in nr: continue
    old, new = nr['FACE_SHAPE_AND_JAW']
    uo, un = R[old]['usability'], R[new]['usability']
    tag = '**變差**' if (uo == 'high' and un != 'high') or (uo == 'mid' and un == 'low') else '持平'
    w(f"| `{pid}` | {old}（{uo}）| {new}（{un}）| {tag} |\n")

w("""
### 3.2 現在有 5 位的臉型來源骨相不可信

| persona | 新來源 | 該圖的臉型判讀 | 這位的 ARCHETYPE | 對不對得上 |
|---|---|---|---|---|
""")
CONTRA = {
 'miu-shiraishi': '大致相符（短圓柔臉），但該圖有廣角變形，量測不可靠',
 'nanami-fujiwara': '**矛盾**：原型要「寬卵形、下巴短鈍」，該圖是中長鵝蛋、下巴小而收，且修圖重',
 'somi-oh': '**部分矛盾**：原型要「寬 U 形顎、下半臉飽滿」，該圖顎線柔和但廣角變形',
 'peggy-lee': '**直接矛盾**：原型要「窄額寬顎、方頦、梯形」，該圖是中短柔軟、下巴小而收、顎線無角',
 'sydney-leong': '**直接矛盾**：原型要「短寬圓角方、柔方顎＋短鈍頦」，該圖是窄臉、下巴極小而尖的 V 形，且是全批濾鏡最重的一張',
}
for pid, note in CONTRA.items():
    r = refs(pid)['FACE_SHAPE_AND_JAW']
    w(f"| `{pid}` | `{r}`（low）| {R[r]['face_shape_and_jaw'][:46]}… | {P[pid]['archetype']} | {note} |\n")

w(f"""
### 3.3 根因：`ref_11` 是全批唯一可信的「長方／寬骨量」來源

你原本把 `ref_11` 指派給 5 位（emma／yerin／ruoruo／wendy／peggy），
那不是隨意分配——**它是 15 張裡唯一低修圖的正面全臉，也是唯一輪廓接近直線、
顎線相對寬而平直的那一張**。而這 5 位的原型全都需要那個骨架方向。

cap-2 之後只有 emma 與 wendy 留著它，其餘 3 位被推到對不上的來源。
換句話說：**cap-2 這條規則是對的，但這個圖庫的容量不足以執行它。**

15 張裡真正能當骨相來源的只有 6 張（high），要供 19 位 × 臉型 1 槽，
在 cap-2 之下最多只能覆蓋 12 位。**數學上就不夠。**

**H-01｜請重新裁決**：你在 F-02 說「目前不同意把再補參考圖列為生成前條件，
15 張足以做第一批實驗」。我認為 §2 的判讀推翻了那個前提——
不是張數不夠，是**可當骨相來源的張數不夠**，而且分配後有 5 位的來源與自己的原型矛盾。

1. 要不要把補圖改成生成前的必要條件？
2. 如果要，請直接給使用者一份採購清單：需要幾張、每張的拍攝條件、以及要補哪些骨架方向。
   （你在 F-02 已經給過方向：寬方顎、下半臉較重的 U／梨形、長臉鈍下巴、窄眼／單眼皮各 2 張，
   加上「中性、正面、眼平、均勻光、低妝、無自拍廣角變形」。要不要照這份、還是要調整？）
3. 如果不要補圖，那 §3.2 那 5 位怎麼辦？是接受用 mid／low 來源，
   還是改他們的 ARCHETYPE 去遷就現有來源？

---

## §4 19 位完整 11 軸

| persona | {' | '.join(ALL)} |
|---|{'---|' * len(ALL)}
""")
for pid in P:
    b = ' 🔵' if pid in B1 else ''
    w(f"| `{pid}`{b} | " + " | ".join(P[pid]['axes'][a] for a in ALL) + " |\n")

w(f"""
🔵 = 第一批 8 位

---

## §5 各軸允許值（你 (C) 的原表）

⭐ = 主導軸（H-03 的 6 條）

| 軸 | 允許值 |
|---|---|
""")
for a, v in AX.items():
    w(f"| `{a}`{' ⭐' if a in DOM else ''} | {' / '.join(v['values'])} |\n")

w(f"""
---

## §6 9 組不過 gate 的配對：逐軸 diff

規則：一般配對總相異 ≥6、主導軸 ≥2；共用臉型來源者總相異 ≥7、主導軸 ≥3。

""")
for n, nn, dm, nd, a, b, sh, diff, dmx in fails:
    same = [x for x in ALL if x not in diff]
    w(f"""**`{a}` vs `{b}`** — 總相異 **{n}**／需 {nn}；主導軸 **{dm}**／需 {nd}"""
      f"""{'　**（共用臉型來源 `' + refs(a)['FACE_SHAPE_AND_JAW'] + '`）**' if sh else ''}"""
      f"""{'　第一批' if a in B1 and b in B1 else ''}

| 軸 | {a} | {b} | |
|---|---|---|---|
""")
    for x in ALL:
        d = x in diff
        star = ' ⭐' if x in DOM else ''
        mark = '✔ 相異' if d else '✗ 相同'
        w(f"| `{x}`{star} | {P[a]['axes'][x]} | {P[b]['axes'][x]} | {mark} |\n")
    w(f"\n需要再拉開 **{max(0, nn - n)}** 條總軸"
      f"{'、其中主導軸再 ' + str(nd - dm) + ' 條' if dm < nd else ''}。\n\n")

w(f"""---

## §7 可換來源矩陣與更換影響

### 7.1 目前 FACE_SHAPE_AND_JAW 的用量（cap 2）

| ref | 可用度 | 用量 | 給誰 | 還能再給幾位 |
|---|---|---|---|---|
""")
for k in R:
    if k in EXCL:
        w(f"| `{k}` | {R[k]['usability']} | — | （已排除臉型來源）| — |\n"); continue
    u = cs.get(k, 0)
    who = [p for p in P if refs(p)['FACE_SHAPE_AND_JAW'] == k]
    w(f"| `{k}` | {R[k]['usability']} | {u} | {'、'.join(who) or '—'} | {max(0, 2 - u)} |\n")

w("""
### 7.2 三組共用來源配對：換誰、換去哪、換完的全域影響

對每一組，我列出「把其中一位換到某張還有餘額的圖」之後會發生什麼。
**距離不受來源更換影響**（軸值沒動），所以這裡只列來源層的後果；
真正要拉開距離仍然要動軸值，那是你的判斷。

""")
free = [k for k in R if k not in EXCL and cs.get(k, 0) < 2]
for k in ['ref_11', 'ref_04', 'ref_05']:
    who = [p for p in P if refs(p)['FACE_SHAPE_AND_JAW'] == k]
    if len(who) != 2: continue
    a, b = who
    w(f"""**共用 `{k}`（{R[k]['usability']}）：{a} ／ {b}**

| 若把誰換走 | 可換到的圖（仍有餘額）| 換走後這組還共用嗎 |
|---|---|---|
""")
    for x in (a, b):
        opts = [f"`{f}`({R[f]['usability']})" for f in free if f != refs(x)['FACE_SHAPE_AND_JAW']]
        w(f"| `{x}` | {'、'.join(opts) if opts else '**沒有餘額**'} | 否，門檻回到 6/2 |\n")
    w("\n")

w(f"""**注意**：目前還有餘額的圖只有 {len(free)} 張——{'、'.join(f'`{f}`({R[f]["usability"]})' for f in free)}。
其中 high 只有 {sum(1 for f in free if R[f]['usability']=='high')} 張。這就是 §3 講的容量問題。

---

## §8 輸出格式

**(H-01) 補圖裁決** — §3 的三個問題。如果要補，給採購清單。

**(H-02) 三組共用來源衝突** — 每組明確講：換誰／換去哪，或改誰的哪幾條軸。

**(H-03) 9 組配對的軸值調整** — 每位一段，只列你實際要改的角色，格式：

```
### <persona-id>
ARCHETYPE: <中文一句話原型>
AXES: <11 條全給，分號分隔，值必須在 §5 允許值內>
FACE_EN: <完整英文段落。參考指派句用 R2 的 Image 1..4 版本 + R3 G-04 合併後的收尾句>
NEGATIVE_EN: <否定清單或 NONE>
MARKERS: <3–5 個，英文，分號分隔，左右翻轉後仍成立>
WHY_DISTINCT: <中文一句話>
```

**(H-04) 8 位重建** — 同上格式。若 H-01 裁決要補圖，這一項可以等補圖到位再做，
請明說「等補圖」，我不會催。

**(H-05) 第一批** — 上述完成後，第一批要跑誰、幾張。
你 R3 說先跑 1 位 4 張當技術探針，驗證四張參考圖各自只控制指定部件——
我同意。請指定是哪一位（你的條件是「第一批中 needs_rebuild=false 且最近鄰距離最大」，
符合的是 kanon-komori、wendy-yeo、angeline-kwee、miu-shiraishi、tammy-chou 這幾位，
但 miu 與 tammy 各自都還在不過關的配對裡）。

---

## §9 回覆區

REPLIES BELOW
""")

OUT = 'review/REVIEW_BATCH3_FACES_R4.md'
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
