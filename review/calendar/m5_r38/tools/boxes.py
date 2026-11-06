import sys, pypdf
MM=25.4/72
for path in sys.argv[1:]:
    r=pypdf.PdfReader(path)
    print("==",path.split('/')[-1],"pages",len(r.pages), "meta", {k:str(v)[:60] for k,v in (r.metadata or {}).items()})
    seen={}
    for i,p in enumerate(r.pages,1):
        def bx(name):
            b=p.get(name)
            if b is None: return None
            b=[float(x) for x in b]
            return tuple(round(v*MM,2) for v in b)
        key=(bx('/MediaBox'),bx('/CropBox'),bx('/BleedBox'),bx('/TrimBox'),bx('/ArtBox'),p.get('/Rotate'))
        seen.setdefault(key,[]).append(i)
    for k,v in seen.items():
        print(" pages",v[:3],"...",len(v)," Media",k[0]," Crop",k[1]," Bleed",k[2]," Trim",k[3]," Art",k[4]," Rot",k[5])
