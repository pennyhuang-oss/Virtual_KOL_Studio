import sys, pymupdf
pdf, png, Wmm, Hmm = sys.argv[1], sys.argv[2], float(sys.argv[3]), float(sys.argv[4])
regions = [r.split(':') for r in sys.argv[5:]]
v = pymupdf.Pixmap(png); W, H = v.width, v.height
page = pymupdf.open(pdf)[0]
m = pymupdf.Matrix(W / page.rect.width, H / page.rect.height)
o = page.get_pixmap(matrix=m, alpha=False)
assert (o.width, o.height) == (W, H), (o.width, o.height, W, H)
vs, os_, vn, on = v.samples, o.samples, v.n, o.n
def stats(x0, y0, x1, y1):
    X0, X1 = int(x0 / Wmm * W), int(x1 / Wmm * W); Y0, Y1 = int(y0 / Hmm * H), int(y1 / Hmm * H)
    diffs = []; sv = [0, 0, 0]; so = [0, 0, 0]; n = 0
    for y in range(Y0, Y1, 2):
        for x in range(X0, X1, 2):
            i = (y * W + x); a = vs[i * vn:i * vn + 3]; b = os_[i * on:i * on + 3]
            d = max(abs(a[k] - b[k]) for k in range(3)); diffs.append(d)
            for k in range(3): sv[k] += a[k]; so[k] += b[k]
            n += 1
    diffs.sort()
    return dict(n=n, mean=round(sum(diffs) / n, 2), p99=diffs[int(n * .99)], max=diffs[-1],
                vendor_avg=[round(s / n) for s in sv], ours_avg=[round(s / n) for s in so])
print(png.split('/')[-1], f"{W}x{H}")
for name, rect in regions:
    print(" ", name, stats(*[float(t) for t in rect.split(',')]))
