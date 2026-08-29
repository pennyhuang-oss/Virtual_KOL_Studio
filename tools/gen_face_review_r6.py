#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生 review/REVIEW_BATCH3_FACES_R6.md —— 舊照片全面退場後剩下的 39 個指派。"""
import json, io, subprocess
from collections import Counter, defaultdict

D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
P, AX = D['personas'], D['axes']
RO = json.load(open('pilot/face_refs_readout.json', encoding='utf-8'))['refs']
M = json.load(open('pilot/face_crops_manifest.json', encoding='utf-8'))['artifacts']
COMMIT = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                        capture_output=True, text=True).stdout.strip()
SL = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
CAP = {'FACE_SHAPE_AND_JAW': 2, 'EYES_AND_BROWS': 3, 'NOSE': 3, 'MOUTH': 3}
AXOF = {'FACE_SHAPE_AND_JAW': ['輪廓原型', '臉長寬比', '三庭配置', '骨肉量', '顎頦', '頰部'],
        'EYES_AND_BROWS': ['眼眶結構', '眼距'], 'NOSE': ['鼻部量體'], 'MOUTH': ['口部幾何']}
RKEY = {'FACE_SHAPE_AND_JAW': 'face_shape_and_jaw', 'EYES_AND_BROWS': 'eyes_and_brows',
        'NOSE': 'nose', 'MOUTH': 'mouth'}
SYN = [f'ref_{i}' for i in range(16, 30)]

NEW = {
 'EYES_AND_BROWS': {'tammy-chou': 'ref_26', 'zoey-yeh': 'ref_21', 'kanon-komori': 'ref_21',
   'jia-seo': 'ref_17', 'zhiyi-shen': 'ref_16', 'wanyin-jiang': 'ref_24',
   'wendy-yeo': 'ref_29', 'peggy-lee': 'ref_27', 'angeline-kwee': 'ref_25'},
 'NOSE': {'tammy-chou': 'ref_18', 'zoey-yeh': 'ref_18', 'rin-ayase': 'ref_19',
   'yerin-han': 'ref_19', 'ruoruo-tang': 'ref_16', 'cheryl-soh': 'ref_24',
   'sydney-leong': 'ref_18', 'zhiyi-shen': 'ref_17', 'wanyin-jiang': 'ref_17',
   'wendy-yeo': 'ref_17', 'angeline-kwee': 'ref_24'},
 'MOUTH': {'angel-chiu': 'ref_18', 'nanami-fujiwara': 'ref_18', 'kanon-komori': 'ref_22',
   'jia-seo': 'ref_28', 'zhiyi-shen': 'ref_25', 'wanyin-jiang': 'ref_25',
   'peggy-lee': 'ref_26', 'somi-oh': 'ref_26', 'wendy-yeo': 'ref_19',
   'angeline-kwee': 'ref_16'}}
cur = {}
for p, d in P.items():
    r = dict(d.get('refs_v2') or d['refs'])
    for s, mp in NEW.items():
        if p in mp: r[s] = mp[p]
    cur[p] = r
todo = {s: [p for p in P if cur[p][s] < 'ref_16'] for s in SL}
ntodo = sum(len(v) for v in todo.values())

o = io.StringIO(); w = o.write
w(f"""# Batch 3 臉部規劃 — R6：舊照片全面退場後，還有 {ntodo} 個指派要配

## §0 給審閱者

**你只需要讀這一個檔案。**

你 R5 追加的三項（J-07 追認、J-08 六張新來源、J-09 風險界定）我全部核對過，**全部成立**（§1）。
`ref_24`–`ref_29` 的裁切我用 builder 自己重跑了一次，24/24 pass，輸出雜湊與你提交的完全一致。

但套用你 J-08 的分配表之後，gate 擋下 38 項。**原因不是你的表格有錯，是它的範圍不夠**：
J-08 只改了 J-03（規格矛盾）與 J-04（low 來源）點名過的指派，
而裁切 QA 拒絕的是**所有仍指向舊 15 張的指派**——不論那張圖的 usability 標成 high、mid 還是 low。
你在 J-09 已經同意「舊 15 張退出正式 crop 候選池」，這一輪就是把那句話走完（§2）。

**回覆方式**：寫在本檔案最下方 §6 回覆區（自成一行的 `REPLIES BELOW` 之後），然後 commit。

- 目前 commit：`{COMMIT}`
- 議題編號從 **K-01** 起跳
- 這一輪只有一件事要你做：把 §3 的 {ntodo} 個指派配完。容量充足（§4），純粹是幾何配對。

---

## §1 你 R5 追加的三項，核對結果

| 項目 | 核對 |
|---|---|
| J-07(a) 補灰邊而非擴張取景 | ✅ 已是 crop_spec v1 的正式行為 |
| J-07(b) 鼻框 bleed 改為「不得含完整眼睛」 | ✅ 已實作 |
| J-08 六張新來源 | ✅ 我用 `build_face_crops.py --all --only ref_nn` 自己重跑，24 件 **24/24 pass**，輸出雜湊與你提交的逐件相同 |
| J-08 眼槽 yaw | ✅ 0.0025–0.0351，全部低於我的 0.08 門檻 |
| J-09 相似度風險 | ✅ **你的修正我接受**——provenance 與雜湊只證明產生路徑，不能證明生成臉不會偶然近似某個真實人物。我先前把這個風險講成「整個消失」，講太滿了。已改為：來源風險與可追溯性解決了，偶然近似仍需在成品候選階段獨立檢查 |

另外有一件小事：J-08 的連動讓 `MOUTH` 的 `ref_10` 供給 4 位（cap 3）。
不過 `ref_10` 是舊照片，本來就要退場，這一輪配完就自然消失，不需要另外處理。

---

## §2 為什麼還有 {ntodo} 個

裁切 QA 拒絕舊照片的理由不是修圖，是**拍攝條件**——而 usability 評級管不到這個：

| 舊來源 | usability | 裁切 QA 為什麼不過 |
|---|---|---|
""")
for r in ['ref_01', 'ref_02', 'ref_11', 'ref_15', 'ref_08', 'ref_09', 'ref_10', 'ref_12']:
    rs = []
    for s in SL:
        k = f'{r}__{s}__v1'
        if k in M and M[k]['qa_status'] == 'fail':
            rs.append(M[k]['qa_reasons'][0])
    if rs:
        w(f"| `{r}` | **{RO[r]['usability']}** | {rs[0]} |\n")

w(f"""
`ref_01`、`ref_02`、`ref_11`、`ref_15` 這四張的 usability 是 **high**，但裁切 QA 全部不過：
側身太多（yaw_proxy 0.17–0.31，標準正面是 0.00–0.02），或部位在原圖上只有七、八十個像素。

**整張臉當參考時看不出來這件事**，因為那時模型根本沒在執行部件；
改用裁切之後，來源的拍攝條件直接決定成敗。這是 R5 那條「裁切法對來源的要求嚴格得多」的具體形狀。

---

## §3 要你配的 {ntodo} 個指派

每一項都要從 `ref_16`–`ref_29` 這 14 張合成標準正面照裡選。
下表列出每位在該槽的**規格軸值**——請照幾何配對，不要為了平均使用而配。

""")
for s in SL:
    if not todo[s]: continue
    w(f"### {s}（{len(todo[s])} 位）\n\n| persona | 規格 |\n|---|---|\n")
    for p in todo[s]:
        spec = ' / '.join(f'{a}={P[p]["axes"][a]}' for a in AXOF[s])
        w(f"| `{p}` | {spec} |\n")
    w("\n")

w(f"""---

## §4 可選的 14 張，以及目前用量

cap：臉型 ≤2 位、其餘 ≤3 位。下表的「已用」是 J-08 之後的狀態。

| 槽位 | 已用 | 剩餘容量 | 還要配 | |
|---|---|---|---|---|
""")
for s in SL:
    used = Counter(cur[p][s] for p in P if cur[p][s] >= 'ref_16')
    free = sum(CAP[s] - used.get(f'ref_{i}', 0) for i in range(16, 30))
    w(f"| {s} | {sum(used.values())} | {free} | {len(todo[s])} | {'✓ 足夠' if free >= len(todo[s]) else '✗ 不足'} |\n")

w("\n### 14 張的四槽判讀（你自己寫的，列在這裡方便配對）\n\n")
w("| ref | 臉型與下顎 | 眼與眉 | 鼻 | 口 | 目前已供給 |\n|---|---|---|---|---|---|\n")
for r in SYN:
    v = RO[r]
    used = []
    for s in SL:
        who = [p for p in P if cur[p][s] == r]
        if who: used.append(f'{s[:4]}×{len(who)}')
    w(f"| `{r}` | {v['face_shape_and_jaw'][:30]} | {v['eyes_and_brows'][:26]} | "
      f"{v['nose'][:22]} | {v['mouth'][:22]} | {'、'.join(used) or '—'} |\n")

w(f"""
---

## §5 輸出格式

**(K-01)** 上面 {ntodo} 個指派的完整分配。格式：

```
### FACE_SHAPE_AND_JAW
angel-chiu: ref_nn
tammy-chou: ref_nn
...

### EYES_AND_BROWS
...

### NOSE
...

### MOUTH
...
```

配的時候要同時滿足（我會用程式驗，不過就退回）：

1. 同一 persona 的四槽必須是四張不同的 ref；
2. slot cap：臉型 ≤2 位、眼／鼻／口各 ≤3 位；
3. 選中的來源，其該槽判讀要與該 persona 的規格相容——
   **不相容就直說「現有 14 張沒有相符的幾何」**，不要用「比較接近」的硬湊。
   （你在 J-03 已經立過這條原則：換素材，不改 identity 規格去遷就素材。）

**(K-02)** 配完之後，如果有任何 persona 因為找不到相符幾何而卡住，列出來並說明缺什麼。

**(K-03)** 確認一句：這一輪配完之後，下一步是不是就是
「重建 12 位的 ARCHETYPE／AXES／FACE_EN／MARKERS／WHY_DISTINCT → 重跑 171 組 gate →
只修仍失敗的配對 → 排第一批」？如果順序有變請說。

---

## §6 回覆區

REPLIES BELOW
""")

OUT = 'review/REVIEW_BATCH3_FACES_R6.md'
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
print(f'已產生 {OUT}（{len(body):,} 字元）；待配 {ntodo} 個指派')
