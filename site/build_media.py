#!/usr/bin/env python3
"""Curate + optimise persona media for the 897 audition site.

Reads the roster from site/public/data/roster.json, copies the selected
source images out of kols/<id>/ and writes web-sized WebP into
site/public/media/<id>/. Videos are copied verbatim (already web-sized).
"""
import json, os, shutil, sys
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_IMG = os.path.join(ROOT, "site/public/media")
OUT_VID = os.path.join(ROOT, "site/public/video")

# Shots we never put in front of a client: the 私下 tier of the library.
BLOCK = ("lingerie", "onsen", "bed_selfie", "bathroom", "hungover")

MAX_W, MAX_H = 1000, 1400          # portrait-first budget
COVER_W, COVER_H = 640, 900        # grid thumbnail


def blocked(p):
    return any(b in p.lower() for b in BLOCK)


def pick(kol_id):
    """Return ordered source image paths for one persona.

    Lifestyle shots come first because shots[0] becomes the grid cover, and
    identity_master.jpg is a neutral ID-style face reference — useful in the
    gallery as the face benchmark, wrong as the card a client sees first.
    """
    base = os.path.join(ROOT, "kols", kol_id)
    out = []
    for sub in ("images/training_v1", "images/training_v2", "images/casting_v1",
                "images/soul_test_v1", "images/video_startframes_v1"):
        d = os.path.join(base, sub)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            p = os.path.join(d, f)
            if not os.path.isfile(p) or blocked(p):
                continue
            if not f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                continue
            if any(x in f for x in ("_rejected", "_fail", "_superseded", "_alt_")):
                continue
            out.append(p)
        if len(out) >= 8:
            break
    out = out[:8]
    master = os.path.join(base, "identity/identity_master.jpg")
    if os.path.exists(master):
        out.append(master)          # face benchmark, last in the gallery
    return out


def save(src, dst, box):
    im = Image.open(src)
    if im.mode in ("RGBA", "P", "LA"):
        im = im.convert("RGB")
    im.thumbnail(box, Image.LANCZOS)
    im.save(dst, "WEBP", quality=82, method=5)
    return os.path.getsize(dst)


def main():
    roster = json.load(open(os.path.join(ROOT, "site/public/data/roster.json")))
    total = 0
    manifest = {}
    for c in roster["contestants"]:
        kid = c["id"]
        srcs = pick(kid)
        if not srcs:
            print(f"!! no images for {kid}", file=sys.stderr)
            continue
        d = os.path.join(OUT_IMG, kid)
        os.makedirs(d, exist_ok=True)
        shots = []
        for i, s in enumerate(srcs):
            name = f"{i:02d}.webp"
            total += save(s, os.path.join(d, name), (MAX_W, MAX_H))
            shots.append(f"media/{kid}/{name}")
        total += save(srcs[0], os.path.join(d, "cover.webp"), (COVER_W, COVER_H))
        manifest[kid] = {"cover": f"media/{kid}/cover.webp", "shots": shots}
        print(f"{kid:20s} {len(shots)} shots")

    os.makedirs(OUT_VID, exist_ok=True)
    for kid, rel in roster.get("videos", {}).items():
        for r in rel:
            src = os.path.join(ROOT, r)
            if not os.path.exists(src):
                print(f"!! missing video {r}", file=sys.stderr)
                continue
            name = f"{kid}__{os.path.basename(src)}"
            shutil.copy2(src, os.path.join(OUT_VID, name))
            total += os.path.getsize(src)
            manifest.setdefault(kid, {}).setdefault("videos", []).append(f"video/{name}")
            print(f"{kid:20s} video {os.path.basename(src)}")

    json.dump(manifest, open(os.path.join(ROOT, "site/public/data/media.json"), "w"),
              ensure_ascii=False, indent=1)
    print(f"\ntotal payload: {total/1048576:.1f} MB")


if __name__ == "__main__":
    main()
