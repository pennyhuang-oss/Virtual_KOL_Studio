#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""產生 review/REVIEW_BATCH3_FACES_R3.md —— R2 裁決套用後剩下的缺口，回頭問 ChatGPT。"""
import json, io, subprocess, itertools
from collections import Counter

D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))
P, ALL = D['personas'], list(D['axes'])
DOM = ['輪廓原型', '臉長寬比', '三庭配置', '骨肉量', '顎頦', '眼眶結構']
B1 = D['batch1']
SLOTS = ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH']
COMMIT = subprocess.run(['git', 'rev-parse', '--short', 'HEAD'],
                        capture_output=True, text=True).stdout.strip()
refs = lambda p: P[p].get('refs_v2') or P[p]['refs']

fails = []
for a, b in itertools.combinations(P, 2):
    n = sum(1 for x in ALL if P[a]['axes'][x] != P[b]['axes'][x])
    dm = sum(1 for x in DOM if P[a]['axes'][x] != P[b]['axes'][x])
    sh = refs(a)['FACE_SHAPE_AND_JAW'] == refs(b)['FACE_SHAPE_AND_JAW']
    nn, nd = (7, 3) if sh else (6, 2)
    if n < nn or dm < nd:
        fails.append((n, nn, dm, nd, a, b, sh))
fails.sort()
rebuild = sorted(p for p in P if P[p].get('needs_rebuild'))
touched = sorted(set(rebuild) | {x for f in fails for x in (f[4], f[5])})

o = io.StringIO(); w = o.write
w(f"""# Batch 3 臉部規劃 — R3：你的 F-02 與 F-03 互相衝突，還有 9 組配對過不了

## §0 給審閱者

**你只需要讀這一個檔案。**

你在 R2（`REVIEW_BATCH3_FACES_R2.md` §7）對四項意見全部給了「同意」，並指定了新的參考來源分配、
新的分離 gate、新的第一批名單。我已經把**能機械執行的部分全部套用**（§1）。

套用之後跑 gate，**171 組配對裡有 9 組過不了**，其中 3 組是**你的 F-02 修正自己製造出來的**。
另外有 8 位的參考來源改變，你說過「改來源後不能只換陣列，五個欄位都要依新來源重建」，
但 R2 只給了其中 3 位的方向，沒有給任何一位的重建文字。

這一輪要你補完這兩件事，**補完就可以開始生成第一批 8 位**。

**回覆方式**：寫在本檔案最下方 §6 回覆區（自成一行的 `REPLIES BELOW` 之後），然後 commit。

- 目前 commit：`{COMMIT}`
- 議題編號從 **G-01** 起跳
- §5 有嚴格輸出格式，我會直接拿去生成

---

## §1 我已經照你的裁決做完的事

| 項目 | 狀態 |
|---|---|
| **F-01 措辭** | 已套用你指定的 `Image 1 / Image 2 / Image 3 / Image 4` 版本，19/19 位改寫完成。我提的 `first/second/third/fourth` 已捨棄。原句留存為 `face_en_v1_filename_form` 供比對。 |
| **F-01 附圖順序與 manifest** | 陣列順序固定 `[FACE_SHAPE_AND_JAW, EYES_AND_BROWS, NOSE, MOUTH]`；送出前寫入 persona-id、四槽位、實際路徑、陣列索引，順序不符 HARD FAIL。 |
| **F-01 備案** | 已記錄：第一批若穩定成立的部件低於 3/4，改用部件裁切輸入；再失敗才走兩階段生成，不得直接展開 19 位。 |
| **F-02 來源分配** | 你的 19 位臉型分配與 5 項鼻子改動已存為 `refs_v2`。驗證通過：臉型上限 2 位、鼻子上限 3 位、每位四槽都是四張不同圖。 |
| **F-03 gate** | 三條規則已實作為 `tools/check_face_gate.py`，原粗分群 gate 作廢。 |
| **F-04 第一批** | 已設為你指定的 8 位。 |
| **年齡族裔真理來源** | 已標記 `fixed` 為唯一真理來源，validator 逐字核對 FACE_EN 與 fixed 一致。 |

**我刻意沒做的一件事**：沒有把 `refs_v2` 直接覆蓋 `refs`。
因為你說過來源一改、五個欄位都要重建，而重建需要你對那些照片的骨相判讀。
現在直接換掉會變成「文字描述的是舊照片、附圖卻是新照片」的靜默不一致。
所以新來源存在 `refs_v2` 並標記 `needs_rebuild`，等你的重建文字到位才合併。

---

## §2 你的兩項修正互相衝突

F-02 讓 5 組人共用同一張 `FACE_SHAPE_AND_JAW`：

| 共用的圖 | 哪兩位 | 套上 F-03 的較嚴規則（總 ≥7、主導 ≥3）後 |
|---|---|---|
""")
cs = Counter(refs(p)['FACE_SHAPE_AND_JAW'] for p in P)
for k, v in sorted(cs.items(), key=lambda x: -x[1]):
    if v < 2: continue
    who = [p for p in P if refs(p)['FACE_SHAPE_AND_JAW'] == k]
    a, b = who
    n = sum(1 for x in ALL if P[a]['axes'][x] != P[b]['axes'][x])
    dm = sum(1 for x in DOM if P[a]['axes'][x] != P[b]['axes'][x])
    ok = '✅ 通過' if (n >= 7 and dm >= 3) else f'❌ **不過**（總 {n}／需 7，主導 {dm}／需 3）'
    w(f"| `{k}` | {a}、{b} | {ok} |\n")

w(f"""
**5 組裡有 3 組不過。** 這 3 組在你 R2 之前是通過的——是 F-02 把它們配成共用來源，
才觸發 F-03 的較嚴門檻。你的兩項修正在這裡打架。

**G-01｜請裁決**：
1. 這 3 組要怎麼處理？把其中一位的臉型來源換掉（但 15 張已經排滿，換誰去哪）？
   還是調整它們的軸值把距離拉到 7/3？
2. 或者「共用臉型來源就要 7/3」這條規則本身要放寬？
   如果放寬，放寬到多少、理由是什麼？

---

## §3 9 組配對過不了 gate

""")
w("| 總相異／需 | 主導軸／需 | 組合 | 共用臉型來源 | 在第一批 | R2 有給方向嗎 |\n|---|---|---|---|---|---|\n")
GIVEN = {('sydney-leong', 'miu-shiraishi'), ('sydney-leong', 'tammy-chou'),
         ('yerin-han', 'peggy-lee')}
for n, nn, dm, nd, a, b, sh in fails:
    inb = ('兩位都在' if a in B1 and b in B1 else '一位在' if (a in B1) ^ (b in B1) else '都不在')
    g = '✅ 有' if frozenset((a, b)) in {frozenset(x) for x in GIVEN} else '❌ **沒有**'
    w(f"| {n}／{nn} | {dm}／{nd} | {a} vs {b} | {'是' if sh else ''} | {inb} | {g} |\n")

w(f"""
**R2 只給了 3 組的調整方向**（Sydney 重建、Yerin 改 ref_12、Peggy 改 ref_14），
而且那 3 組的方向是文字描述，沒有具體的軸值。**另外 6 組完全沒有處理。**

其中 **3 組完整落在第一批 8 位裡**（miu↔sydney、yerin↔peggy、tammy↔sydney）——
那正是你刻意把它們放進第一批的原因。這 3 組不解決，第一批就不能跑。

**G-02｜請給出具體的軸值調整**。這 9 組每一組都要處理，格式見 §5。

---

## §4 8 位的參考來源改了，文字還沒重建

你在 F-02 寫：「改來源後不能只換陣列：ARCHETYPE、AXES、FACE_EN、MARKERS、WHY_DISTINCT
與 hash 都必須依新來源同步重建。」

以下 8 位的來源確實改了：

| persona | 槽位 | 舊來源 → 新來源 | 在第一批 |
|---|---|---|---|
""")
for pid in rebuild:
    for slot, (old, new) in P[pid]['needs_rebuild'].items():
        w(f"| `{pid}` | {slot} | `{old}` → `{new}` | {'**是**' if pid in B1 else ''} |\n")

w(f"""
**其中 3 位在第一批**（yerin-han、peggy-lee、sydney-leong），所以第一批同樣卡在這裡。

**G-03｜請給出這 8 位重建後的完整欄位**，格式見 §5。

---

### 這 8 位目前的規格（供你對照）

""")
for pid in rebuild:
    d = P[pid]; f = d['fixed']
    w(f"""**`{pid}`**（{f['age']} 歲・{f['ethnicity']}・{f['public_face'].split(' — ')[0]}）
來源變動：{'；'.join(f'{k} {v[0]}→{v[1]}' for k, v in d['needs_rebuild'].items())}
- ARCHETYPE: {d['archetype']}
- AXES: {'; '.join(f'{k}={v}' for k, v in d['axes'].items())}
- MARKERS: {'; '.join(d['markers'])}
- WHY_DISTINCT: {d['why_distinct']}

""")

w("""---

## §5 兩件小事 ＋ 輸出格式

**G-04｜P2｜你的新指派句與原有的收尾句重複了。** 套用後每段 FACE_EN 現在同時有：

> ... Combine these four assigned components into one coherent new identity. Build a ... **Synthesize these four components into one new coherent identity**; each reference contributes its assigned geometry rather than a complete likeness.

兩句在講同一件事。後半句的「each reference contributes its assigned geometry rather than a complete likeness」
是有意義的、不重複，但「Synthesize these four components into one new coherent identity」與你新句的
「Combine these four assigned components into one coherent new identity」是同義重複。
prompt 冗贅正是稀釋訊號的成因之一。要刪哪一句？還是兩句都留？

**G-05｜P2｜`ref_13` 現在沒有任何人拿它當臉型來源了。** 這是刻意的（它的輪廓不適合當骨架來源），
還是重新分配時的副作用？它仍被用在眼眉與口部。

### 輸出格式

**(G-01) 共用來源衝突的裁決** — 明確講三組各怎麼處理。

**(G-02+G-03) 需要改動的角色** — 每位一段，**只列出你實際要改的角色**。
§4 的 8 位是一定要重建的（來源已經換了）；§3 的 9 組配對牽涉到 """
  + str(len(touched)) + """ 位，但你不必全改——
每組只要動其中一位就能把距離拉開，請自己判斷動誰代價最小。格式與 R1 完全相同，欄位要給全：

```
### <persona-id>
ARCHETYPE: <中文一句話原型>
AXES: <11 條全給，分號分隔，值必須在原維度表的允許值內>
FACE_EN: <完整英文段落。參考指派句用你 R2 指定的 Image 1..4 版本，不要再寫檔名>
NEGATIVE_EN: <否定清單或 NONE>
MARKERS: <3–5 個，英文，分號分隔，左右翻轉後仍成立>
WHY_DISTINCT: <中文一句話>
```

**(G-04)(G-05)** — 各一句話回答。

**最後請確認一句**：改完之後，第一批 8 位是否就可以開始生成？
還是你認為要先跑更小的技術探針（例如只跑 1 位、4 張，先確認「四張圖各司其職」這個假說成不成立）？
我傾向後者——你在 F-01 自己也說那仍是待驗證假說，而 32 張全跑下去如果假說不成立就是全廢。

---

## §6 回覆區

REPLIES BELOW
""")

OUT = 'review/REVIEW_BATCH3_FACES_R3.md'
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
print(f'已產生 {OUT}（{len(body):,} 字元）；待改動角色 {len(touched)} 位')
