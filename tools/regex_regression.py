# -*- coding: utf-8 -*-
"""正則的正向 ＋ 反向 regression cases。

存在的理由（2026-09-09，GPT daily_v2 R2 複核建議）：
我先前只測「壞字串會不會被擋」，從來沒測「正常字串會不會被誤擋」，
結果自己撞到六次誤判：
  crop shirt / very short navy pleated skirt / low cowl neck /
  short pencil skirt / in her free hand / waist seam
每一次都是規則把本來合格的寫法判成不合格，而我要等到跑不過才發現。

用法：python3 tools/regex_regression.py
"""
import importlib.util, sys, re
spec=importlib.util.spec_from_file_location("bp","plan/daily_v2/build_prompts.py")
bp=importlib.util.module_from_spec(spec); spec.loader.exec_module(bp)

# (正則, 應該命中的, 不應該被誤擋的)
CASES=[
 ("SKIN", bp.SKIN,
  ["a fitted white ribbed crop tank and high-waisted denim micro shorts",
   "a fitted white crop shirt with a soft collar and a very short navy pleated skirt with socks",
   "a satin slip midi dress with a low cowl neck and a belted waist",
   "a fitted cream shirt knotted at the waist over a high-waisted short pencil skirt",
   "a black satin slip mini dress with a plunging cowl neck and a low back",
   "an off-shoulder fitted oat rib knit and a high-waisted long skirt with a side slit",
   "a white crochet open cover-up over a white triangle bikini"],
  ["a long-sleeve high-neck knit tucked into ankle-length wool trousers",
   "a loose smock dress with long sleeves and a hem below the calf"]),

 ("WAIST", bp.WAIST,
  ["a fitted knit tucked into high-waisted tailored shorts",
   "a cropped white shirt knotted at the waist over a pleated micro skirt",
   "a floral chiffon wrap mini dress with a deep V neck and a tie waist",
   "a black floor-length satin gown with a plunging neckline, cinched at the waist",
   "a white crochet cover-up with a sarong tied low on the hips",
   "a fitted cream crop top with a small round collar and a very short checked skirt"],
  ["a loose sleeveless smock over wide palazzo trousers",
   "a straight shift dress that skims the body"]),

 ("LIMB_ONE", bp.LIMB_ONE,
  ["a canned coffee in her free hand","one hand settled on the curve of her waist",
   "a woven basket on one arm","her fingertips rest flat against her collarbone",
   "one palm pressed flat on the surface","her thumb hooked into the waistband"],
  ["a black leather tote on one shoulder","a straw bag on her shoulder",
   "a posting slip on the counter","a canned coffee standing on the shelf edge beside her",
   "a slim crossbody bag worn across her body"]),

 ("LIMB_TWO", bp.LIMB_TWO,
  ["with both elbows resting solidly on it","both hands folding the edge","both arms raised"],
  ["one hand on her waist","her fingertips against her collarbone"]),

 ("DYNAMIC_POSE", bp.DYNAMIC_POSE,
  ["She is leaning back against the low edge behind her",
   "She is mid-stride with her weight rolling onto the front foot",
   "She has stopped and turned back over her shoulder toward the lens",
   "She is half-seated on the edge of something"],
  ["She stands facing the camera with her feet together"]),

 ("EYES_DOING", bp.EYES_DOING,
  ["her eyes bright and holding the lens","the warmth showing in her eyes",
   "her gaze going past the camera"],
  ["Her expression is a small smile."]),

 ("REFLECTIVE", bp.REFLECTIVE,
  ["a mirrored pillar","looking into a small stand mirror","her reflection over the counter",
   "about a metre from the reflective surface"],
  ["water bright on both sides","wet asphalt reflecting the signage",
   "small bright highlights on glass"]),
]

fail=0
for name,rx,pos,neg in CASES:
    for t in pos:
        if not rx.search(t):
            print(f"[FAIL] {name} 漏判（應命中）：{t}"); fail+=1
    for t in neg:
        if rx.search(t):
            print(f"[FAIL] {name} 誤擋（不應命中）：{t}  ← 命中片段 {rx.search(t).group(0)!r}"); fail+=1

print(f"\n{sum(len(p)+len(n) for _,_,p,n in CASES)} 個 case，{fail} 個失敗")
sys.exit(1 if fail else 0)
