# -*- coding: utf-8 -*-
"""v4 稽核：每一份 spec 都必須符合場域配額與憲章原則二。"""
import json, glob, sys, re
SHORT={"wendy-yeo":5,"zhiyi-shen":5,"angel-chiu":3,"angeline-kwee":3,"somi-oh":3,"yerin-han":3,
       "zoey-yeh":3,"emma-kao":2,"peggy-lee":2,"sydney-leong":2,"tammy-chou":2,"wanyin-jiang":2,
       "cheryl-soh":1,"jia-seo":1,"miu-shiraishi":1,"ruoruo-tang":1}
errs=[]; rows=[]
files=sorted(glob.glob('specs/*.json'))
for f in files:
    d=json.load(open(f)); pid=d["pid"]; S=d["slots"]
    work=[s for s in S if s.get("flag") and "唯一的工作場域" in s["flag"]]
    out =[s for s in S if s.get("flag") and "房間以外" in s["flag"]]
    quota=[s for s in S if s.get("flag") and "標誌性配額" in s["flag"]]
    priv=len(S)-len(work)-len(out)
    if len(S)!=5: errs.append(f"{pid}: 格數 {len(S)} ≠ 5")
    if len(work)>1: errs.append(f"{pid}: 工作場域 {len(work)} 格 > 1（憲章原則二 25% 上限）")
    if priv<3: errs.append(f"{pid}: 她自己的空間只有 {priv} 格 < 3")
    if len(quota)>1: errs.append(f"{pid}: 標誌性配額用了 {len(quota)} 格 > 1")
    for s in S:
        for k in ("place","action","action_src","outfit","outfit_src","light","light_src","face","face_src","people"):
            if not s.get(k): errs.append(f"{pid} {s['id']}: 缺 {k}")
    # 每一格的光都必須有出處
    if len({s["place"] for s in S})!=5: errs.append(f"{pid}: 場域有重複")
    rows.append((pid,len(S),priv,len(work),len(out),len(quota),SHORT.get(pid,"?")))
# 跨人設不得撞場域
allp={}
for f in files:
    d=json.load(open(f))
    for s in d["slots"]:
        key=s["place"]
        if key in allp: errs.append(f"跨人設撞場域：{d['pid']} 與 {allp[key]} 都用了「{key[:30]}」")
        allp[key]=d["pid"]
# 格號必須全域唯一，而且要跟 en/ 的英文稿對得上。
# 這條是補的：wanyin-jiang 原本用 W1–W5，跟 wendy-yeo 整組撞號，
# 而 en/ 那邊已經改成 Q1–Q5，等於同一個格號在兩份檔案指向不同人設。
seen={}
for f in files:
    d=json.load(open(f))
    for s in d["slots"]:
        if s["id"] in seen: errs.append(f"格號重複：{d['pid']} 與 {seen[s['id']]} 都有 {s['id']}")
        seen[s["id"]]=d["pid"]
for f in files:
    d=json.load(open(f)); e=f.replace("specs/","en/")
    try: en=json.load(open(e))
    except FileNotFoundError: errs.append(f"{d['pid']}: 找不到 {e}"); continue
    a=[s["id"] for s in d["slots"]]; b=[s["id"] for s in en["slots"]]
    if a!=b: errs.append(f"{d['pid']}: specs 格號 {a} 與 en 格號 {b} 不一致")

print(f"{'人設':18s} {'格':>2s} {'私下':>4s} {'工作':>4s} {'外出':>4s} {'配額':>4s} {'本輪缺':>6s}")
for r in rows: print(f"{r[0]:18s} {r[1]:2d} {r[2]:4d} {r[3]:4d} {r[4]:4d} {r[5]:4d} {r[6]:>6}")
print(f"\n人設 {len(rows)} 位 · 總格數 {sum(r[1] for r in rows)} · 場域 {len(allp)} 個（零重複）")
if errs:
    print(f"\n❌ {len(errs)} 項不通過："); [print("  ",e) for e in errs]; sys.exit(1)
print("\n✅ 稽核全數通過")
