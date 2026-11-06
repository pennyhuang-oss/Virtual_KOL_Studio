"""TASK-CAL-001 M-5 R38 — build print-candidate PDFs from the R37 final previews.

Only two technical changes, nothing else:
  1. remove the preview footer text "版面預覽 R26｜非交印核准｜面 n／N" (text only;
     images and vector graphics under it are kept);
  2. drop the last page (barcode placeholder) — the vendor's barcode page takes that face.

Then verify every kept page: render source and output at 200 dpi and confirm that all
pixel differences fall inside the removed label's rectangle, page boxes are unchanged,
and every image stream is byte-identical.

usage: python build_print_r38.py SRC_H.pdf SRC_V.pdf OUT_DIR
"""
import hashlib
import json
import sys

import numpy as np
import pymupdf

LABEL = "版面預覽 R26"
MM = 25.4 / 72
SPECS = {
    "H": dict(out="cal2027_H_print_R38.pdf", pages=28, cover="H-L1-R36L",
              sha256="23b32c22c106119b4439a0da55d523bb8b275dbfe4e44bdad002a6115ba146d1",
              title="2027 桌曆 橫式 交印版候選 R38（封面 H-L1-R36L）"),
    "V": dict(out="cal2027_V_print_R38.pdf", pages=32, cover="V-D2-R34B",
              sha256="21f1b4faf1ed049d2820c09fb47baa399749106730ea71e2ff180e0b685271d6",
              title="2027 桌曆 直式 交印版候選 R38（封面 V-D2-R34B）"),
}
SUBJECT = ("交印版候選｜由 R37 定案預覽移除「版面預覽」標記並拿掉條碼佔位頁｜"
           "最後一面由印廠條碼頁占用｜尚未打樣、尚未核准交印（TASK-CAL-001 M-5 R38）")


def sha256(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def label_rects(page):
    rects, others = [], []
    for b in page.get_text("dict")["blocks"]:
        for line in b.get("lines", []):
            for s in line["spans"]:
                (rects if s["text"].startswith(LABEL) else others).append(
                    (pymupdf.Rect(s["bbox"]), s["text"]))
    return rects, others


def boxes(page):
    return {k: tuple(round(v, 3) for v in getattr(page, k))
            for k in ("mediabox", "bleedbox", "trimbox", "cropbox")}


def image_hashes(doc, pno):
    out = []
    for img in doc[pno].get_images(full=True):
        out.append(hashlib.sha256(doc.xref_stream_raw(img[0])).hexdigest())
    return sorted(out)


def build(kind, src, out_dir):
    spec = SPECS[kind]
    assert sha256(src) == spec["sha256"], f"{kind}: source sha256 mismatch"
    doc = pymupdf.open(src)
    assert len(doc) == spec["pages"]
    removed = []
    for pno in range(len(doc) - 1):  # last page is dropped below
        page = doc[pno]
        rects, others = label_rects(page)
        for r, text in rects:
            rr = r + (-0.3, -0.3, 0.3, 0.3)
            clash = [t for o, t in others if o.intersects(rr)]
            assert not clash, f"{kind} p{pno+1}: other text inside label rect: {clash}"
            page.add_redact_annot(rr, fill=False)
            removed.append(dict(page=pno + 1, text=text,
                                rect_mm=[round(v * MM, 2) for v in rr]))
        if rects:
            page.apply_redactions(images=pymupdf.PDF_REDACT_IMAGE_NONE,
                                  graphics=pymupdf.PDF_REDACT_LINE_ART_NONE,
                                  text=pymupdf.PDF_REDACT_TEXT_REMOVE)
    doc.delete_page(len(doc) - 1)
    now = pymupdf.get_pdf_now()
    doc.set_metadata(dict(
        title=spec["title"], subject=SUBJECT, author="Virtual KOL Studio",
        keywords="print candidate; preview labels removed; barcode placeholder page removed; not yet proofed; not approved for print",
        creator="build_print_r38.py", producer="cal2027 R38", creationDate=now, modDate=now))
    out = f"{out_dir}/{spec['out']}"
    doc.save(out, garbage=3, deflate=True)
    return out, removed


def verify(kind, src, out):
    spec = SPECS[kind]
    s, o = pymupdf.open(src), pymupdf.open(out)
    assert len(o) == spec["pages"] - 1, "page count"
    report = []
    for pno in range(len(o)):
        ps, po = s[pno], o[pno]
        assert boxes(ps) == boxes(po), f"{kind} p{pno+1}: boxes changed"
        assert image_hashes(s, pno) == image_hashes(o, pno), f"{kind} p{pno+1}: image changed"
        assert not any(LABEL in sp for sp in [po.get_text()]), f"{kind} p{pno+1}: label still present"
        txt_s = ps.get_text().replace("\n", "")
        txt_o = po.get_text().replace("\n", "")
        rects, _ = label_rects(ps)
        for r, t in rects:
            txt_s = txt_s.replace(t, "")
        assert txt_s == txt_o, f"{kind} p{pno+1}: other text changed"
        a = ps.get_pixmap(dpi=200, alpha=False)
        b = po.get_pixmap(dpi=200, alpha=False)
        A = np.frombuffer(a.samples, np.uint8).reshape(a.height, a.width, a.n)
        B = np.frombuffer(b.samples, np.uint8).reshape(b.height, b.width, b.n)
        diff = (A != B).any(axis=2)
        changed = int(diff.sum())
        mask = np.zeros_like(diff)
        for r, _ in rects:
            q = (r + (-0.3, -0.3, 0.3, 0.3)) * (200 / 72)
            mask[max(int(q.y0) - 1, 0):int(q.y1) + 2, max(int(q.x0) - 1, 0):int(q.x1) + 2] = True
        outside = int((diff & ~mask).sum())
        assert outside == 0, f"{kind} p{pno+1}: {outside} changed pixels outside label rect"
        report.append(dict(page=pno + 1, labels=len(rects), changed_px=changed, outside_px=outside))
    return report


if __name__ == "__main__":
    src_h, src_v, out_dir = sys.argv[1:4]
    result = {}
    for kind, src in (("H", src_h), ("V", src_v)):
        out, removed = build(kind, src, out_dir)
        checks = verify(kind, src, out)
        result[kind] = dict(source=src.split("/")[-1], source_sha256=SPECS[kind]["sha256"],
                            output=out.split("/")[-1], output_sha256=sha256(out),
                            pages=len(pymupdf.open(out)), labels_removed=len(removed),
                            removed=removed, page_checks=checks)
        print(kind, "OK", result[kind]["pages"], "pages,", len(removed), "labels removed,",
              "changed px per page max", max(c["changed_px"] for c in checks))
    json.dump(result, open(f"{out_dir}/print_R38_build.json", "w", encoding="utf-8"),
              ensure_ascii=False, indent=1)
