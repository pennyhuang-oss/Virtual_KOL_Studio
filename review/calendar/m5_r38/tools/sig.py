import sys, pymupdf
doc=pymupdf.open(sys.argv[1]); out=[]
for i,p in enumerate(doc,1):
    if i>int(sys.argv[2]): break
    pix=p.get_pixmap(dpi=20); s=pix.samples; n=pix.n; N=pix.width*pix.height
    r=sum(s[k] for k in range(0,len(s),n))/N; g=sum(s[k+1] for k in range(0,len(s),n))/N; b=sum(s[k+2] for k in range(0,len(s),n))/N
    out.append(f"{i}:{r:.0f},{g:.0f},{b:.0f}")
print(" ".join(out))
