import sys, pymupdf
pix=pymupdf.Pixmap(sys.argv[1]); W,H,n=pix.width,pix.height,pix.n
print("size",W,H,"n",n,"alpha",pix.alpha)
mm_w=float(sys.argv[2]); mm_h=float(sys.argv[3])
s=pix.samples
rows=[]
for y in range(H):
    cnt=0
    for x in range(0,W,2):
        a=s[(y*W+x)*n+n-1] if pix.alpha else 255
        if a>10: cnt+=1
    rows.append(cnt)
nz=[y for y,c in enumerate(rows) if c>0]
print("opaque rows y-range px",nz[0] if nz else None, nz[-1] if nz else None, "-> mm", (nz[0]*mm_h/H if nz else None), (nz[-1]*mm_h/H if nz else None))
cols=[]
for x in range(W):
    cnt=sum(1 for y in range(0,H,2) if s[(y*W+x)*n+n-1]>10)
    cols.append(cnt)
nzc=[x for x,c in enumerate(cols) if c>0]
print("opaque cols x-range px",nzc[0],nzc[-1],"-> mm",nzc[0]*mm_w/W, nzc[-1]*mm_w/W)
# count hole groups along x at the row with max opaque
