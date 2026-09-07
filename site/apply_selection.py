#!/usr/bin/env python3
"""Apply a selection exported from /pick.html to the live site's media.

Usage:
    python3 site/apply_selection.py selection.json

The picker exports asset ids; this resolves them back to their source files
via site/public/data/pool.json, then rewrites site/public/media,
site/public/video and site/public/data/media.json. The user's chosen cover
lands at index 0 so it becomes the grid card image.

Selections are stored as ids rather than paths so a rebuild of the pool
cannot silently repoint a choice at a different picture.
"""
import json, os, shutil, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_IMG = os.path.join(ROOT, "site/public/media")
OUT_VID = os.path.join(ROOT, "site/public/video")
MAX = (1000, 1400)
COVER = (640, 900)
VIDEO_BUDGET_MB = 90     # keep the deployed service inside a sane build size


def save(src, dst, box):
    im = Image.open(src)
    if im.mode in ("RGBA", "P", "LA"):
        im = im.convert("RGB")
    im.thumbnail(box, Image.LANCZOS)
    im.save(dst, "WEBP", quality=82, method=5)
    return os.path.getsize(dst)


def main():
    if len(sys.argv) < 2:
        sys.exit("usage: apply_selection.py <selection.json>")
    sel = json.load(open(sys.argv[1]))
    pool = json.load(open(os.path.join(ROOT, "site/public/data/pool.json")))

    shutil.rmtree(OUT_IMG, ignore_errors=True)
    shutil.rmtree(OUT_VID, ignore_errors=True)
    os.makedirs(OUT_VID, exist_ok=True)

    manifest, total, vid_mb, warn = {}, 0, 0.0, []

    for kid, entry in sel.get("personas", {}).items():
        if kid not in pool:
            warn.append(f"{kid}: not in pool, skipped")
            continue
        by_id = {it["id"]: it for it in pool[kid]["items"]}
        ids = [i for i in entry.get("items", []) if i in by_id]
        missing = [i for i in entry.get("items", []) if i not in by_id]
        if missing:
            warn.append(f"{kid}: {len(missing)} unknown asset id(s) ignored")
        if not ids:
            warn.append(f"{kid}: nothing selected, skipped")
            continue

        cover = entry.get("cover")
        if cover in ids:                      # cover first -> becomes the card
            ids = [cover] + [i for i in ids if i != cover]

        d = os.path.join(OUT_IMG, kid)
        os.makedirs(d, exist_ok=True)
        shots, vids, n = [], [], 0
        for i in ids:
            it = by_id[i]
            src = os.path.join(ROOT, it["src"]) if not it["src"].startswith("/") else it["src"]
            if not os.path.exists(src):
                warn.append(f"{kid}: missing source {it['src']}")
                continue
            if it["type"] == "image":
                name = f"{n:02d}.webp"
                total += save(src, os.path.join(d, name), MAX)
                shots.append(f"media/{kid}/{name}")
                n += 1
            else:
                mb = os.path.getsize(src) / 1048576
                if vid_mb + mb > VIDEO_BUDGET_MB:
                    warn.append(f"{kid}: {it['name']} ({mb:.0f}MB) skipped — "
                                f"video budget {VIDEO_BUDGET_MB}MB reached")
                    continue
                vname = f"{kid}__{it['name']}"
                shutil.copy2(src, os.path.join(OUT_VID, vname))
                vids.append(f"video/{vname}")
                vid_mb += mb

        if not shots:
            warn.append(f"{kid}: no usable image, contestant will show no cover")
            continue
        first = by_id[ids[0]]
        cover_src = os.path.join(ROOT, first["src"])
        if first["type"] != "image" or not os.path.exists(cover_src):
            cover_src = os.path.join(ROOT, by_id[[i for i in ids
                                     if by_id[i]["type"] == "image"][0]]["src"])
        total += save(cover_src, os.path.join(d, "cover.webp"), COVER)
        manifest[kid] = {"cover": f"media/{kid}/cover.webp", "shots": shots}
        if vids:
            manifest[kid]["videos"] = vids
        print(f"  {kid:16s} {len(shots)} imgs  {len(vids)} vids")

    for kid in pool:
        if kid not in manifest:
            warn.append(f"{kid}: NOT IN SELECTION — will render with no images")

    json.dump(manifest, open(os.path.join(ROOT, "site/public/data/media.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"\n{len(manifest)}/{len(pool)} contestants | "
          f"images {total/1048576:.1f}MB | video {vid_mb:.1f}MB")
    if warn:
        print("\nwarnings:")
        for w in warn:
            print("  !", w)


if __name__ == "__main__":
    main()
