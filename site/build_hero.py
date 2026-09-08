#!/usr/bin/env python3
"""Build the landing-band line-up tiles: site/public/media/<id>/hero.webp

The hero band is a slow-drifting row of all 15 portraits above the headline —
the audition line-up. It has to read as portraits, so this does not reuse the
grid cover: the covers are lifestyle shots chosen to sell each persona's world,
and at band size they crop to a torso in a room rather than to a face.

Instead every shot for a persona is scanned for a face, the largest clear one
wins, and the tile is cropped as head-and-shoulders around it. That fixes both
problems at once — the band reads as a line-up, and the room context (several
covers are bedroom shots, wrong as the first thing a client sees) crops away.

Face detection is optional. Without OpenCV installed this falls back to the
persona's cover with a fixed upward bias, which is the previous behaviour and
still usable — just less tightly framed.

Reads media.json, so it follows whichever builder last wrote the manifest
(build_media.py for a full rebuild, apply_selection.py after the client
re-picks material). Re-run it after either one.
"""

import json
import os

from PIL import Image

try:
    import cv2
    import numpy as np
except ImportError:                                   # optional dependency
    cv2 = None

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, "site/public")
HERO_W, HERO_H = 300, 400          # 2x the rendered tile, for retina
HEAD_ROOM = 1.75                   # crop width as a multiple of face width
EYE_LINE = 0.45                    # where the face centre sits vertically
MIN_FACE_PX = 120                  # below this a "face" is usually a false positive
MIN_FACE_FRAC = 0.10               # and a real face this small crops to a long shot

# Editorial overrides, same idea as EDITORIAL in build_roster.py. Face size is
# a decent proxy for "good portrait" but not a complete one, so these three are
# chosen by eye:
#   kanon-komori   only 4 shots; the largest detection in her others is a
#                  sewing machine, so this pins the one unambiguous face
#   angeline-kwee  the largest face is turned away; 02 is the one front portrait
#   iris-chen      her set is mostly lingerie and bed shots (the client picked
#                  them, and they stay on her own page) — but the band is the
#                  first thing anyone sees, so it takes a street portrait
PICK = {
    "kanon-komori": "01.webp",
    "angeline-kwee": "02.webp",
    "iris-chen": "01.webp",
}


def detector():
    if cv2 is None:
        return None
    path = os.path.join(cv2.data.haarcascades, "haarcascade_frontalface_default.xml")
    return cv2.CascadeClassifier(path) if os.path.exists(path) else None


def find_face(cascade, path):
    """Largest frontal face as (cx, cy, w), in pixels. None if nothing found."""
    img = cv2.imread(path)
    if img is None:
        return None
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    grey = cv2.equalizeHist(grey)
    faces = cascade.detectMultiScale(grey, scaleFactor=1.08, minNeighbors=6,
                                     minSize=(60, 60))
    if len(faces) == 0:
        return None
    ih, iw = img.shape[:2]
    # Drop detections in the bottom third of the frame: a real face is never
    # there in a portrait, but a pair of shoes in one shot read as one.
    faces = [f for f in faces if (f[1] + f[3] / 2) < ih * 0.66]
    if not len(faces):
        return None
    x, y, w, h = max(faces, key=lambda f: f[2] * f[3])
    strong = w >= MIN_FACE_PX and w >= iw * MIN_FACE_FRAC
    return x + w / 2, y + h / 2, w, strong


def crop_to(im, cx, cy, face_w):
    """Head-and-shoulders window around a face, clamped inside the frame."""
    want = HERO_W / HERO_H
    w, h = im.size

    box_w = min(w, face_w * HEAD_ROOM)
    box_h = box_w / want
    if box_h > h:                                     # not tall enough: fit height
        box_h = h
        box_w = box_h * want

    left = min(max(cx - box_w / 2, 0), w - box_w)
    top = min(max(cy - box_h * EYE_LINE, 0), h - box_h)
    return im.crop((round(left), round(top),
                    round(left + box_w), round(top + box_h)))


def crop_centre(im):
    """Fallback: keep the upper part of the frame."""
    want = HERO_W / HERO_H
    w, h = im.size
    if w / h > want:
        new_w = round(h * want)
        left = (w - new_w) // 2
        return im.crop((left, 0, left + new_w, h))
    new_h = round(w / want)
    top = round((h - new_h) * 0.18)
    return im.crop((0, top, w, top + new_h))


def main():
    media = json.load(open(os.path.join(PUB, "data/media.json")))
    roster = json.load(open(os.path.join(PUB, "data/roster.json")))
    cascade = detector()
    if cascade is None:
        print("!! OpenCV not available — falling back to cover crops")

    total = 0
    for c in roster["contestants"]:
        kid = c["id"]
        entry = media.get(kid) or {}
        shots = list(entry.get("shots") or [])
        cover = entry.get("cover")
        if cover and cover not in shots:
            shots.insert(0, cover)
        if not shots:
            print(f"!! {kid}: no images, skipped")
            continue

        forced = PICK.get(kid)
        if forced:
            shots = [r for r in shots if r.endswith("/" + forced)] or shots

        best = None
        if cascade is not None:
            for rel in shots:
                src = os.path.join(PUB, rel)
                face = find_face(cascade, src)
                if not face:
                    continue
                # A strong face always beats a weak one; among equals, biggest
                # wins. Without this a long shot can outrank a clean portrait
                # just by being first in the list.
                if best is None or (face[3], face[2]) > (best[1][3], best[1][2]):
                    best = (src, face)

        dst = os.path.join(PUB, "media", kid, "hero.webp")
        if best:
            src, (cx, cy, fw, strong) = best
            im = Image.open(src)
            if im.mode in ("RGBA", "P", "LA"):
                im = im.convert("RGB")
            tile = crop_to(im, cx, cy, fw)
            note = f"face {fw:.0f}px {'' if strong else '(weak) '} {os.path.basename(src)}"
        else:
            src = os.path.join(PUB, shots[0])
            im = Image.open(src)
            if im.mode in ("RGBA", "P", "LA"):
                im = im.convert("RGB")
            tile = crop_centre(im)
            note = f"no face  {os.path.basename(src)}"

        tile = tile.resize((HERO_W, HERO_H), Image.LANCZOS)
        tile.save(dst, "WEBP", quality=80, method=5)
        total += os.path.getsize(dst)
        print(f"{kid:20s} {note}")

    print(f"\n{len(roster['contestants'])} tiles, {total / 1024:.0f} KB total")


if __name__ == "__main__":
    main()
