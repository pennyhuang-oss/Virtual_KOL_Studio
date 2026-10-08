# -*- coding: utf-8 -*-
"""v5 稽核。v4 的 validate 只檢查配額與欄位非空，所以 16/16 位都有浴室、
13 位還落在同一格位，全部通過。v5 加上語意矩陣：把 80 格按格位橫排，
檢查有沒有哪個屬性值或屬性組合在跨人設的層級變成主導。"""
import collections, sys
from specs_data import SPECS

PRIV = {"臥室","浴室","廚房","客廳","玄關","衣櫃 / 更衣","陽台 / 頂樓","車內","車庫"}
PUB  = {"街道","店內","市場","車站機場","老街","園林 / 戶外自然","工作場域"}
MUST_HAVE_PEOPLE = {"市場","車站機場","老街"}   # 這三族空無一人本身就不合理
REQ = ("id","ev","pil","wt","fam","pose","hand","gaze","view","topo","time",
       "pl","pl_en","ac","ac_en","ac_s","of","of_en","of_s",
       "li","li_en","li_s","fa","fa_en","fa_s","hair_en")
PPL_REQ = ("level","dist","act","wear","facing")

errs=[]; rows=[]; allslots=[]
for pid,d in SPECS.items():
    S=d["slots"]; allslots += [(pid,i+1,s) for i,s in enumerate(S)]
    if len(S)!=5: errs.append(f"{pid}: 格數 {len(S)} ≠ 5")
    work=[s for s in S if s.get("flag")=="唯一的工作場域"]
    out =[s for s in S if s.get("flag")=="房間以外"]
    quota=[s for s in S if s.get("flag")=="標誌性配額"]
    priv=len(S)-len(work)-len(out)
    if len(work)>1: errs.append(f"{pid}: 工作場域 {len(work)} 格 > 1")
    if len(quota)>1: errs.append(f"{pid}: 標誌性配額 {len(quota)} 格 > 1")
    if not 2<=priv<=4: errs.append(f"{pid}: 她自己的空間 {priv} 格，不在 2–4")
    if not 1<=len(out)<=3: errs.append(f"{pid}: 房間以外 {len(out)} 格，不在 1–3")
    day=sum(1 for s in S if s["time"]=="day")
    if day not in (2,3): errs.append(f"{pid}: 日 {day} 格，必須是 2 或 3")
    for s in S:
        t=f"{pid} {s['id']}"
        for k in REQ:
            if not s.get(k): errs.append(f"{t}: 缺 {k}")
        # 光的出處必須帶 character.md 的原句，不能只寫欄位名稱
        if "原句" not in s.get("li_s","") and "：" not in s.get("li_s",""):
            errs.append(f"{t}: light_src 沒有附 character.md 原句摘錄")
        p=s.get("ppl")
        if p:
            if s["fam"] in PRIV: errs.append(f"{t}: {s['fam']} 是私人空間，不該有路人")
            for k in PPL_REQ:
                if not p.get(k): errs.append(f"{t}: 路人缺 {k}")
        elif s["fam"] in MUST_HAVE_PEOPLE:
            errs.append(f"{t}: {s['fam']} 沒有半個人，這個場域空著本身就不合理")
    rows.append((pid,priv,len(work),len(out),len(quota),day,5-day,d["comp"]))

# 場域零重複
seen={}
for pid,_,s in allslots:
    if s["pl"] in seen: errs.append(f"跨人設撞場域：{pid} 與 {seen[s['pl']]}")
    seen[s["pl"]]=pid
# 格號唯一
ids=[s["id"] for _,_,s in allslots]
for k,v in collections.Counter(ids).items():
    if v>1: errs.append(f"格號重複：{k} × {v}")

day_total=sum(1 for _,_,s in allslots if s["time"]=="day")
if day_total!=40: errs.append(f"全批日 {day_total} 格 ≠ 40")

bath=[(pid,i) for pid,i,s in allslots if s["fam"]=="浴室"]
if len(bath)>6: errs.append(f"全批浴室 {len(bath)} 格 > 6")
bp=collections.Counter(i for _,i in bath)
for i,n in bp.items():
    if n>3: errs.append(f"浴室集中在第 {i} 格 {n} 次 > 3")

ppl=[s for _,_,s in allslots if s.get("ppl")]
if not 8<=len(ppl)<=12: errs.append(f"有路人 {len(ppl)} 格，不在 8–12")

# ---- 語意矩陣：按格位橫排，看有沒有主導值 ----
ATTR=("fam","pose","hand","gaze","view","topo","time")
dom=[]
for i in range(1,6):
    col=[s for _,j,s in allslots if j==i]
    for a in ATTR:
        c=collections.Counter(s[a] for s in col)
        v,n=c.most_common(1)[0]
        if n>10: errs.append(f"第 {i} 格的 {a} 有 {n}/16 都是「{v}」——格位被鎖死")
        elif n>=8: dom.append(f"第 {i} 格 {a}：{v} {n}/16")
# 屬性組合
for keys,cap in ((("fam","pose"),6),(("pose","hand"),8),(("view","topo"),8),(("pose","gaze"),8)):
    c=collections.Counter(tuple(s[k] for k in keys) for _,_,s in allslots)
    for combo,n in c.items():
        if n>cap: errs.append(f"組合 {'+'.join(keys)}={combo} 出現 {n}/80 > {cap}")

print(f"{'人設':16s} {'私':>2s} {'工':>2s} {'外':>2s} {'配':>2s} {'日':>2s} {'夜':>2s}  組成")
for r in rows: print(f"{r[0]:16s} {r[1]:2d} {r[2]:2d} {r[3]:2d} {r[4]:2d} {r[5]:2d} {r[6]:2d}  {r[7]}")
print(f"\n人設 {len(rows)} · 格 {len(allslots)} · 場域 {len(seen)} 個零重複 · 日 {day_total}/夜 {80-day_total}")
print(f"浴室 {len(bath)} 格，落在第 {sorted(bp.items())} 格 · 有路人 {len(ppl)} 格")
print("組成分布：", dict(collections.Counter(r[7] for r in rows)))
for i in range(1,6):
    col=[s for _,j,s in allslots if j==i]
    print(f"  第{i}格 場景族：", dict(collections.Counter(s['fam'] for s in col)))
if dom:
    print("\n⚠️ 接近上限（僅提示，未違規）："); [print("  ",x) for x in dom]
if errs:
    print(f"\n❌ {len(errs)} 項不通過："); [print("  ",e) for e in errs]; sys.exit(1)
print("\n✅ 稽核全數通過")
