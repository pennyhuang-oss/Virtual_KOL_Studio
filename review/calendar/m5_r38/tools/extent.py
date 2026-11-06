import sys, pymupdf
path=sys.argv[1]; W=float(sys.argv[2]); H=float(sys.argv[3])  # bleed-box size mm
sx0,sy0,sx1,sy1=[float(v) for v in sys.argv[4].split(',')]     # safe rect in bleed coords mm
coil=float(sys.argv[5])
K=25.4/72
doc=pymupdf.open(path)
worst=[]
for pno,page in enumerate(doc,1):
    boxes=[]
    for b in page.get_text("dict")["blocks"]:
        for l in b.get("lines",[]):
            for s in l["spans"]:
                if s["text"].strip(): boxes.append(("text:"+s["text"][:18],[v*K for v in s["bbox"]]))
    for im in page.get_images(full=True):
        for r in page.get_image_rects(im[0]):
            bb=[r.x0*K,r.y0*K,r.x1*K,r.y1*K]
            if bb[2]-bb[0]>W-1 and bb[3]-bb[1]>H-1: continue  # full-bleed background
            boxes.append(("img",bb))
    for dr in page.get_drawings():
        r=dr["rect"]; bb=[r.x0*K,r.y0*K,r.x1*K,r.y1*K]
        if bb[2]-bb[0]>W-1 and bb[3]-bb[1]>H-1: continue
        boxes.append(("draw",bb))
    if not boxes: print(f"p{pno:02d} (no non-bg content)"); continue
    x0=min(b[1][0] for b in boxes); y0=min(b[1][1] for b in boxes); x1=max(b[1][2] for b in boxes); y1=max(b[1][3] for b in boxes)
    out=[]
    if x0<sx0-0.01: out.append(f"left {x0:.2f}<{sx0}")
    if y0<sy0-0.01: out.append(f"top {y0:.2f}<{sy0}")
    if x1>sx1+0.01: out.append(f"right {x1:.2f}>{sx1}")
    if y1>sy1+0.01: out.append(f"bottom {y1:.2f}>{sy1}")
    coilhit = y0<coil
    lowest=[b for b in boxes if b[1][3]==y1][0][0]
    print(f"p{pno:02d} extent x {x0:.2f}-{x1:.2f} y {y0:.2f}-{y1:.2f} | margins to trim: L{x0-2:.1f} T{y0-2:.1f} R{W-2-x1:.1f} B{H-2-y1:.1f} | outside_safe={out or 'none'} coil_overlap={coilhit} lowest={lowest}")
