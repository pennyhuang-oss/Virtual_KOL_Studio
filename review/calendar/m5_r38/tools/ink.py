import sys, pymupdf
doc=pymupdf.open(sys.argv[1]); page=doc[0]
# render text only: remove images by drawing page with only text? Instead compare full render vs. blue dominance
dpi=300; pix=page.get_pixmap(dpi=dpi); W,H,n=pix.width,pix.height,pix.n; s=pix.samples
mm=lambda px: px*25.4/dpi
x0=int(110/25.4*dpi); x1=int(200/25.4*dpi)
lowest=None; highest=None; left=None; right=None
for y in range(int(90/25.4*dpi), H):
    for x in range(x0,x1,2):
        i=(y*W+x)*n; r,g,b=s[i],s[i+1],s[i+2]
        if b-r>60 and b-g>40 and r<140:
            lowest=y if lowest is None or y>lowest else lowest
            highest=y if highest is None or y<highest else highest
            left=x if left is None or x<left else left
            right=x if right is None or x>right else right
print(f"2027 ink: x {mm(left):.2f}-{mm(right):.2f} y {mm(highest):.2f}-{mm(lowest):.2f} mm (bleed coords); bottom margin to trim(153)={153-mm(lowest):.2f} mm; to H safe bottom(151)={151-mm(lowest):.2f} mm")
