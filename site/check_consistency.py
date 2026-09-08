#!/usr/bin/env python3
"""Cross-check the whole site, not just the part that was last edited.

Written after a real failure: the voting mechanic was rewritten but the
schedule section kept quoting the options that no longer existed, and the
user found it. Editing one section without sweeping the rest is the mistake
this guards against. Run it before every push.

    python3 site/check_consistency.py
"""
import json, os, re, sys
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
if str(trained) not in chk.get("建模與產能", ""):
    bad.append(f"checks/建模與產能 disagrees with roster ({trained} trained)")
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
