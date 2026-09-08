#!/usr/bin/env python3
"""Record each clip's pixel dimensions: site/public/data/video_meta.json

Without this the detail page has to wait for the browser to fetch enough of
every mp4 to learn its shape. Until that lands a <video> reports the spec's
default 300x150, so a column of 9:16 reels lays out as flat letterbox boxes
and then jumps to full height — and any CSS that sizes from the intrinsic
ratio cannot work at all until the metadata arrives.

Dimensions are read straight from the mp4 `tkhd` box rather than by shelling
out to ffprobe, which is not installed here. `tkhd` carries width and height
as 16.16 fixed point; the box layout differs between version 0 and 1, hence
the two offsets.

Run after any change to the video set (build_media.py / apply_selection.py).
"""

import json
import os
import struct

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PUB = os.path.join(ROOT, "site/public")


def mp4_dims(path):
    """(width, height) from the first track header, or None."""
    with open(path, "rb") as fh:
        blob = fh.read(3_000_000)          # tkhd lives in the header atoms

    at = blob.find(b"tkhd")
    if at < 0:
        return None

    version = blob[at + 4]
    # after the 4-byte type: version+flags(4), then the timing fields, whose
    # width depends on the version, then the fixed tail before width/height
    pos = at + 4 + 4
    pos += (8 + 8 + 4 + 4 + 8) if version == 1 else (4 + 4 + 4 + 4 + 4)
    pos += 8 + 2 + 2 + 2 + 2 + 36          # reserved, layer, group, volume, matrix

    if pos + 8 > len(blob):
        return None
    raw_w, raw_h = struct.unpack(">II", blob[pos:pos + 8])
    w, h = raw_w >> 16, raw_h >> 16
    return (w, h) if w and h else None


def main():
    media = json.load(open(os.path.join(PUB, "data/media.json")))

    out, missing = {}, []
    for kid, entry in sorted(media.items()):
        for rel in entry.get("videos") or []:
            path = os.path.join(PUB, rel)
            if not os.path.exists(path):
                missing.append(rel)
                continue
            dims = mp4_dims(path)
            if dims:
                out[rel] = list(dims)
            else:
                missing.append(rel)

    dst = os.path.join(PUB, "data/video_meta.json")
    json.dump(out, open(dst, "w"), indent=1, sort_keys=True)
    open(dst, "a").write("\n")

    shapes = {}
    for w, h in out.values():
        shapes["portrait" if h > w else "landscape" if w > h else "square"] = \
            shapes.get("portrait" if h > w else "landscape" if w > h else "square", 0) + 1
    print(f"{len(out)} clips measured  {shapes}")
    for rel in missing:
        print(f"!! could not read dimensions: {rel}")


if __name__ == "__main__":
    main()
