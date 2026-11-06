import sys, pypdf
src, out, pages = sys.argv[1], sys.argv[2], [int(x) for x in sys.argv[3].split(',')]
r=pypdf.PdfReader(src); w=pypdf.PdfWriter()
for p in pages: w.add_page(r.pages[p-1])
w.add_metadata({"/Title":"R38 platform import test (derived from R37 final preview; NOT print file)"})
with open(out,"wb") as f: w.write(f)
