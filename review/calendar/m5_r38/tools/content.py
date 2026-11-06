import sys, pymupdf
for path in sys.argv[1:]:
    doc=pymupdf.open(path)
    print("==",path.split('/')[-1])
    for pno,page in enumerate(doc,1):
        imgs=page.get_images(full=True)
        fonts=page.get_fonts()
        txt=page.get_text().strip().replace('\n',' ')[:50]
        info=[]
        for im in imgs:
            xref=im[0]
            rects=page.get_image_rects(xref)
            for r in rects:
                wmm=r.width*25.4/72; hmm=r.height*25.4/72
                ppi_w=im[2]/(r.width/72) if r.width else 0
                info.append(f"{im[2]}x{im[3]} {im[5]} bpc{im[4]} smask{im[1]!=0} @({r.x0*25.4/72:.1f},{r.y0*25.4/72:.1f}) {wmm:.1f}x{hmm:.1f}mm ~{ppi_w:.0f}ppi")
        dr=len(page.get_drawings())
        print(f"p{pno:02d} fonts={len(fonts)} drawings={dr} text='{txt}' imgs={info}")
