import sys, math
from PIL import Image, ImageStat

def patch(im, box, label):
    st = ImageStat.Stat(im.convert('L').crop(box))
    return label, st.mean[0], st.stddev[0]

def report(path, regions):
    im = Image.open(path)
    print(f"\n=== {path}  {im.size} ===")
    vals = {}
    for label, box in regions.items():
        _, m, sd = patch(im, box, label)
        vals[label] = m
        print(f"  {label:<14} L={m:6.1f}  sd={sd:5.1f}")
    face = vals['face_lit']
    for k in vals:
        if k.startswith('bg'):
            stops = math.log2(max(vals[k],1)/max(face,1))
            print(f"  -> {k} vs face: {stops:+.2f} stops")
    if 'face_shadow' in vals:
        r = math.log2(max(vals['face_lit'],1)/max(vals['face_shadow'],1))
        print(f"  -> face lit/shadow ratio: {r:+.2f} stops (臉部反差)")
