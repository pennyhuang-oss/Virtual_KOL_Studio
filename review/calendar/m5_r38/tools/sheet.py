import sys, os, glob, json, pymupdf
# usage: sheet.py out.jpg title cols cellW cellH  label1=path1 ...  (args via json file)
spec=json.load(open(sys.argv[1],encoding="utf-8"))
cols=spec["cols"]; cw=spec["cw"]; ch=spec["ch"]; lh=34; pad=10
items=spec["items"]; title=spec["title"]
rows=(len(items)+cols-1)//cols
W=cols*(cw+pad)+pad; H=70+rows*(ch+lh+pad)+pad
doc=pymupdf.open(); page=doc.new_page(width=W,height=H)
page.draw_rect(page.rect, color=None, fill=(1,1,1))
page.insert_text((pad,40), title, fontname="china-t", fontsize=24, color=(0,0,0))
for k,(label,path) in enumerate(items):
    r,c=divmod(k,cols); x=pad+c*(cw+pad); y=70+r*(ch+lh+pad)
    rect=pymupdf.Rect(x,y,x+cw,y+ch)
    page.draw_rect(rect, color=(.85,.85,.85), fill=(.96,.96,.96), width=0.5)
    try: page.insert_image(rect, filename=path, keep_proportion=True)
    except Exception as e: page.insert_text((x+5,y+20),"ERR",fontsize=10)
    page.insert_textbox(pymupdf.Rect(x,y+ch+2,x+cw,y+ch+lh), label, fontname="china-t", fontsize=11, color=(.1,.1,.1))
pix=page.get_pixmap(dpi=spec.get("dpi",72))
pix.save(spec["out"], jpg_quality=82) if spec["out"].endswith(".jpg") else pix.save(spec["out"])
print(spec["out"], pix.width, pix.height, os.path.getsize(spec["out"])//1024, "KB")
