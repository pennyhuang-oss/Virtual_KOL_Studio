import sys, os, glob, json, subprocess
base=sys.argv[1]; out=sys.argv[2]; py=sys.argv[3]; sheet=sys.argv[4]
os.makedirs(out,exist_ok=True)
def run(spec):
    p=os.path.join(out,"_spec.json"); json.dump(spec,open(p,"w",encoding="utf-8"),ensure_ascii=False)
    print(subprocess.run([py,"-I",sheet,p],capture_output=True,text=True).stdout.strip())
for kind,cw,ch in (("H",220,170),("V",150,220)):
    names=[l.split("\t")[0] for l in open(f"{base}/{kind}_product_templates.tsv",encoding="utf-8").read().splitlines()]
    files=sorted(glob.glob(f"{base}/thumbs/templates_{kind}/*"))
    items=[(f"{i:02d} {n}",f) for i,(n,f) in enumerate(zip(names,files))]
    run(dict(title=f"永豐雲端印刷網｜{'經典橫式桌曆 YFP-CA01' if kind=='H' else '經典直式桌曆 YFP-CA08'}｜內建設計版型（選擇設計版型）{len(items)} 款｜2026-11-06 擷取",
             cols=8, cw=cw, ch=ch, items=items, out=f"{out}/templates_{kind}_{len(items)}.jpg"))
cats=dict(x.split(":",1) for x in open(f"{base}/design_categories.txt",encoding="utf-8").read().split())
groups=[("calendar_A_horizontal",[0,1,2,3,8,10]),("calendar_B_vertical",[4,5,6,9]),("calendar_C_other",[7,11,12,13,14,15,16])]
for gname,cl in groups:
    items=[]
    for c in cl:
        for f in sorted(glob.glob(f"{base}/thumbs/designs/{c:02d}/*")):
            items.append((f"[{c}] {cats[str(c)]}",f))
    run(dict(title=f"永豐雲端印刷網｜編輯器「設計」面板｜日期／年曆類 {gname}｜{len(items)} 款｜2026-11-06 擷取",
             cols=8, cw=200, ch=200, items=items, out=f"{out}/designs_{gname}_{len(items)}.jpg"))
deco=list(range(17,44))
items=[]
for c in deco:
    for f in sorted(glob.glob(f"{base}/thumbs/designs/{c:02d}/*")):
        items.append((f"[{c}] {cats[str(c)]}",f))
half=(len(items)+1)//2
for n,chunk in enumerate((items[:half],items[half:]),1):
    run(dict(title=f"永豐雲端印刷網｜編輯器「設計」面板｜裝飾素材類（非日期）第{n}頁｜{len(chunk)} 款｜2026-11-06 擷取",
             cols=12, cw=120, ch=120, items=chunk, out=f"{out}/designs_decor_part{n}_{len(chunk)}.jpg"))
os.remove(os.path.join(out,"_spec.json"))
