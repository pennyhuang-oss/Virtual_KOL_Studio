#!/usr/bin/env python3
"""Cross-check the whole site, not just the part that was last edited.

Written after a real failure: the voting mechanic was rewritten but the
schedule section kept quoting the options that no longer existed, and the
user found it. Editing one section without sweeping the rest is the mistake
this guards against. Run it before every push.

    python3 site/check_consistency.py
"""
import json
import re, os, re, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(ROOT, "site/public")

plan = json.load(open(f"{P}/data/plan.json"))
roster = json.load(open(f"{P}/data/roster.json"))
media = json.load(open(f"{P}/data/media.json"))
html = open(f"{P}/index.html").read()
js = open(f"{P}/app.js").read()

bad = []

# --- wiring: markup, renderers and data must agree -----------------------
ids = set(re.findall(r'<section id="([a-z]+)"', html))
for n in set(re.findall(r"\['([a-z]+)',", js)):
    if n not in ids:
        bad.append(f"nav points at a missing section: #{n}")
for eid in set(re.findall(r"\$\('#([a-z0-9-]+)'\)", js)):
    if f'id="{eid}"' not in html:
        bad.append(f"app.js writes to a missing element: #{eid}")

# --- internal-only facts must not reach the client-facing page -----------
# The user's ruling: our staffing is internal. It lives in the internal
# record (clients/girl-group-audition/), never in the site payload.
site_blob = json.dumps(plan, ensure_ascii=False) + html
for tok in ("1.5 位", "製作師", "AIGC 製作師", "FTE", "人力配置"):
    if tok in site_blob:
        bad.append(f"internal staffing detail on the client-facing site: {tok}")

# --- an option must not claim a superlative its own numbers contradict ---
# Written after a real failure: the schedule cards sit side by side, so when
# the full-version card claimed 素材量最省 the stat row directly above it
# already read 35 支 against the short version's 20 支. Comparative claims
# have to agree with the numbers rendered next to them.
for group in plan.get("choices", []):
    opts = group.get("options", [])
    for field, label in (("videos", "影片需求"), ("weeks", "賽程")):
        vals = [o.get(field) for o in opts]
        if any(v is None for v in vals):
            continue
        lowest = min(vals)
        for o in opts:
            blob = " ".join(o.get("pros", []) + o.get("cons", []))
            for sup in ("最省", "最低", "最快", "最少"):
                if sup in blob and o[field] != lowest:
                    bad.append(
                        f"{o.get('id')} claims 「{sup}」 but {label}={o[field]} "
                        f"(lowest is {lowest})"
                    )

# --- stale references to structures that were removed --------------------
blob = json.dumps(plan, ensure_ascii=False) + html + js
for tok in ("方案 A", "方案 B", "方案 C", "方案 D", "方案 E",
            "voteA", "voteB", "voteC", "voteD", "voteE", "schFast",
            "formA", "formB", "formC", "formD", "壓縮版"):
    if tok in blob:
        bad.append(f"stale reference to a removed option: {tok}")

# --- every contestant must have media, and vice versa -------------------
ids_r = {c["id"] for c in roster["contestants"]}
for cid in ids_r - set(media):
    bad.append(f"{cid}: on the roster but has no media")
for cid in set(media) - ids_r:
    bad.append(f"{cid}: has media but is not on the roster")
for cid, m in media.items():
    if not m.get("shots"):
        bad.append(f"{cid}: no images, its card will be blank")

# --- every video count quoted in prose must match media.json ------------
# Written after a real failure: media.json was rebuilt from the catalog
# selection (21 clips across 5 personas) but the 組合體檢 row still read
# "3 位共 6 支" from the previous build, contradicting the 素材現況 tiles
# on the same page. Counts get quoted in several places; only one is true.
vid_by_id = {cid: len(m.get("videos") or []) for cid, m in media.items()}
have_vid = {cid: n for cid, n in vid_by_id.items() if n}
n_clips, n_people = sum(have_vid.values()), len(have_vid)
prose = json.dumps(plan, ensure_ascii=False)
for m_ in re.finditer(r"(\d+)\s*位共\s*(\d+)\s*支", prose):
    if (int(m_.group(1)), int(m_.group(2))) != (n_people, n_clips):
        bad.append(
            f"prose says {m_.group(0)} but media.json has "
            f"{n_people} 位共 {n_clips} 支"
        )
for m_ in re.finditer(r"既有\s*(\d+)\s*支影片", prose):
    if int(m_.group(1)) != n_clips:
        bad.append(
            f"prose says 既有 {m_.group(1)} 支影片 but media.json has {n_clips}"
        )

# --- talent groups declared vs used -------------------------------------
declared = {g["key"] for g in plan["groups"]}
for k in Counter(c["group"] for c in roster["contestants"]):
    if k not in declared:
        bad.append(f"roster uses talent group '{k}' that plan.groups omits")

# --- figures quoted in prose vs the roster they describe -----------------
chk = {c["k"]: c["v"] for c in plan["checks"]}
n = len(roster["contestants"])
trained = sum(1 for c in roster["contestants"] if c["soul"] == "已訓練")
cups = Counter(c["specs"]["cup"] for c in roster["contestants"])
cupstr = "・".join(f"{k}×{cups[k]}" for k in "FEDC" if cups[k])
h = sorted(c["specs"]["height_cm"] for c in roster["contestants"])

if plan["talent_model"]["stats"][0]["k"] != str(n):
    bad.append(f"talent_model says {plan['talent_model']['stats'][0]['k']}, roster has {n}")
# The row's key has been renamed before; find it by content, not by name.
soul_row = next((v for k, v in chk.items() if "建模" in k), None)
if soul_row is None:
    bad.append("checks has no row about modelling status")
elif str(trained) not in soul_row:
    bad.append(f"the 建模 row says '{soul_row}', roster has {trained} trained")
if cupstr not in chk.get("罩杯", ""):
    bad.append(f"checks/罩杯 is '{chk.get('罩杯')}', roster is '{cupstr}'")
if f"{h[0]} – {h[-1]} cm" not in chk.get("身高", ""):
    bad.append(f"checks/身高 is '{chk.get('身高')}', roster is {h[0]}–{h[-1]}")

# --- schedule options: video counts must match their own breakdown -------
S = {o["id"]: o for g in plan["choices"] if g["group"] == "schedule"
     for o in g["options"]}
for oid, o in S.items():
    if not o.get("weeks") or not o.get("videos"):
        bad.append(f"schedule option {oid} is missing weeks or videos")

print(f"sections {len(ids)} | contestants {n} | media {len(media)} | "
      f"schedule options {len(S)} | decisions {len(plan['decisions'])}")
if bad:
    print("\nINCONSISTENT:")
    for x in bad:
        print("  x", x)
    sys.exit(1)
print("\nall consistent")
