#!/usr/bin/env python3
"""Build the asset picker: every candidate image/clip for the 15 contestants.

Two sources feed the pool:
  A. kols/<id>/**            — the persona library originals
  B. catalog/assets/_pick/   — the catalog project's already-web-sized set,
                               extracted from its branch (only exists for the
                               five Soul-trained personas)

Writes 190px thumbs for the grid, 800px versions for judging quality in the
lightbox, and copies the catalog's small mp4 clips so video can be previewed
inline. Repo reels are 1.4-59MB each, so those are represented by their
start_frame.png and only pulled in at apply time.

Output: site/public/pick/** plus site/public/data/pool.json
"""
import json, os, shutil, hashlib, subprocess
from PIL import Image

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PICK = os.path.join(ROOT, "site/public/pick")
CAT = "/tmp/catpick/catalog/assets/_pick"
CAT_BRANCH = "origin/claude/kol-dashboard-catalog-gqw9jz"

# The 私下 tier stays out of a client deck; it is still listed here so the
# picker can show it greyed with a reason rather than silently hiding assets.
SENSITIVE = ("lingerie", "onsen", "bed_selfie", "bathroom", "hungover")
SKIP = ("_rejected", "_fail", "_superseded", "_alt_")

THUMB = (190, 275)
FULL = (800, 1160)


def ensure_catalog():
    if os.path.isdir(CAT):
        return
    os.makedirs("/tmp/catpick", exist_ok=True)
    p1 = subprocess.Popen(["git", "archive", CAT_BRANCH, "catalog/assets/_pick"],
                          cwd=ROOT, stdout=subprocess.PIPE)
    subprocess.run(["tar", "-x", "-C", "/tmp/catpick"], stdin=p1.stdout, check=True)
    p1.wait()


def aid(path):
    """Stable short id for an asset, so selections survive a rebuild."""
    return hashlib.sha1(path.encode()).hexdigest()[:10]


def repo_assets(kid):
    """Images and reels from the persona library."""
    base = os.path.join(ROOT, "kols", kid)
    imgs, vids = [], []
    for dirpath, _, files in os.walk(base):
        rel_dir = os.path.relpath(dirpath, base)
        if rel_dir.startswith("videos"):
            for f in sorted(files):
                if not f.lower().endswith(".mp4"):
                    continue
                src = os.path.join(dirpath, f)
                job = os.path.basename(dirpath)
                # its own first frame, if the job dir kept one
                poster = None
                for cand in (f"images/{job}/start_frame.png",
                             f"images/{job}/start_frame_v2.png"):
                    pp = os.path.join(base, cand)
                    if os.path.exists(pp):
                        poster = pp
                        break
                vids.append({"src": src, "poster": poster, "job": job,
                             "mb": round(os.path.getsize(src) / 1048576, 1)})
            continue
        for f in sorted(files):
            if not f.lower().endswith((".png", ".jpg", ".jpeg", ".webp")):
                continue
            if any(x in f for x in SKIP):
                continue
            imgs.append(os.path.join(dirpath, f))
    return imgs, vids


def catalog_assets(kid):
    d = os.path.join(CAT, kid)
    if not os.path.isdir(d):
        return [], []
    files = sorted(os.listdir(d))
    imgs = [os.path.join(d, f) for f in files
            if f.endswith(".jpg") and not f.endswith("_vp.jpg")]
    vids = []
    for f in files:
        if not f.endswith("_vc.mp4"):
            continue
        stem = f[:-7]
        poster = os.path.join(d, stem + "_vp.jpg")
        vids.append({"src": os.path.join(d, f),
                     "poster": poster if os.path.exists(poster) else None,
                     "job": stem,
                     "mb": round(os.path.getsize(os.path.join(d, f)) / 1048576, 2)})
    return imgs, vids


def write_img(src, kid, key, box, sub):
    out_dir = os.path.join(PICK, sub, kid)
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, key + ".webp")
    im = Image.open(src)
    if im.mode in ("RGBA", "P", "LA"):
        im = im.convert("RGB")
    im.thumbnail(box, Image.LANCZOS)
    im.save(dst, "WEBP", quality=78 if sub == "full" else 72, method=4)
    return f"pick/{sub}/{kid}/{key}.webp", os.path.getsize(dst)


def main():
    ensure_catalog()
    roster = json.load(open(os.path.join(ROOT, "site/public/data/roster.json")))
    shutil.rmtree(PICK, ignore_errors=True)
    pool, total = {}, 0

    for c in roster["contestants"]:
        kid = c["id"]
        items = []

        for origin, (imgs, vids) in (("庫", repo_assets(kid)),
                                     ("型錄", catalog_assets(kid))):
            for src in imgs:
                rel = os.path.relpath(src, ROOT) if src.startswith(ROOT) else src
                key = aid(rel)
                t, n1 = write_img(src, kid, key, THUMB, "thumb")
                f, n2 = write_img(src, kid, key, FULL, "full")
                total += n1 + n2
                items.append({
                    "id": key, "type": "image", "origin": origin,
                    "thumb": t, "full": f, "src": rel,
                    "name": os.path.basename(src),
                    "sensitive": any(s in rel.lower() for s in SENSITIVE),
                })
            for v in vids:
                rel = os.path.relpath(v["src"], ROOT) if v["src"].startswith(ROOT) else v["src"]
                key = aid(rel)
                thumb = full = None
                if v["poster"]:
                    thumb, n1 = write_img(v["poster"], kid, key, THUMB, "thumb")
                    full, n2 = write_img(v["poster"], kid, key, FULL, "full")
                    total += n1 + n2
                clip = None
                if v["mb"] <= 1.0:          # catalog clips are tiny; inline them
                    cd = os.path.join(PICK, "clip", kid)
                    os.makedirs(cd, exist_ok=True)
                    shutil.copy2(v["src"], os.path.join(cd, key + ".mp4"))
                    clip = f"pick/clip/{kid}/{key}.mp4"
                    total += os.path.getsize(v["src"])
                items.append({
                    "id": key, "type": "video", "origin": origin,
                    "thumb": thumb, "full": full, "clip": clip, "src": rel,
                    "name": os.path.basename(v["src"]), "mb": v["mb"],
                    "job": v["job"],
                    "sensitive": any(s in rel.lower() for s in SENSITIVE),
                })

        pool[kid] = {"name": c["name"], "native": c["native_name"],
                     "group": c["group"], "talent": c["talent"], "items": items}
        ni = sum(1 for x in items if x["type"] == "image")
        nv = len(items) - ni
        print(f"  {kid:16s} {ni:3d} imgs  {nv:2d} vids")

    dest = os.path.join(ROOT, "site/public/data/pool.json")
    json.dump(pool, open(dest, "w"), ensure_ascii=False, indent=1)
    n = sum(len(v["items"]) for v in pool.values())
    print(f"\n{n} candidates across {len(pool)} contestants")
    print(f"picker payload: {total/1048576:.1f} MB")


if __name__ == "__main__":
    main()
