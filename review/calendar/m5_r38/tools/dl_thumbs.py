import sys, os, urllib.request, concurrent.futures as cf
CDN="https://d528ure73rx4b.cloudfront.net"
base=sys.argv[1]
jobs=[]
for kind in ("H","V"):
    for i,line in enumerate(open(f"{base}/{kind}_product_templates.tsv",encoding="utf-8")):
        name,path=line.rstrip("\n").split("\t")
        jobs.append((CDN+path, f"{base}/thumbs/templates_{kind}/{i:02d}_{os.path.basename(path)}"))
cats=dict(x.split(":",1) for x in open(f"{base}/design_categories.txt",encoding="utf-8").read().split())
items=[s for s in open(f"{base}/design_items.flat",encoding="utf-8").read().replace("\n",";").split(";") if s]
for j,s in enumerate(items):
    c,f=s.split("|",1)
    jobs.append((CDN+"/designnbuy/designidea/"+f, f"{base}/thumbs/designs/{int(c):02d}/{j:03d}_{f}"))
def get(job):
    url,out=job; os.makedirs(os.path.dirname(out),exist_ok=True)
    if os.path.exists(out) and os.path.getsize(out)>0: return "skip"
    try:
        req=urllib.request.Request(url, headers={"User-Agent":"Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=30) as r: data=r.read()
        open(out,"wb").write(data); return "ok"
    except Exception as e: return f"ERR {url} {e}"
with cf.ThreadPoolExecutor(12) as ex:
    res=list(ex.map(get,jobs))
print(len(jobs), sum(r=="ok" for r in res), [r for r in res if r.startswith("ERR")][:10])
