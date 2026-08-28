#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Phase C prompt 靜態檢查。

把 ChatGPT R10 抓到的每一類缺陷寫成可執行的規則，避免改 builder 之後又破掉。
規則來源：`KOL_TRAINING_SOP.md`〈這個模型的實測行為〉與 review/LEDGER.md 的 C-34…C-43。
"""
import json, re, sys

ERR = []
def err(m): ERR.append(m)

pilot = json.load(open('pilot/nico_pilot.json', encoding='utf-8'))
pr    = json.load(open('pilot/phase_c_prompts.json', encoding='utf-8'))
en    = json.load(open('pilot/phase_c_actions_en.json', encoding='utf-8'))
S     = {s['shot_id']: s for s in pilot['phase_c_shots']}

VISIBLE = {'face_closeup':['top','jewelry'], 'chest_up':['top','jewelry'],
           'waist_up':['top','top_hem','bottom','jewelry'],
           'knee_up':['top','top_hem','bottom','jewelry'],
           'full_body':['top','top_hem','bottom','shoes','jewelry']}
# C-47：戒指／手鍊由「有沒有手入鏡」決定，不由景別決定
BODY_TAIL = {'face_closeup':'collarbone visible', 'chest_up':'upper arms',
             'waist_up':'waist is narrow', 'knee_up':'hips are about as wide',
             'full_body':'legs are long and straight'}
POSE_VERB = re.compile(r'\bShe (sits|stands|crouches|kneels|lies|leans|walks)\b')
NEG = re.compile(r'\b(not|no|none|nothing|never|neither)\b', re.I)

for sid, txt in pr.items():
    s = S[sid]; f = s['framing']

    # C-35：構圖／服裝／相機的否定式一律不得出現
    for m in NEG.finditer(txt):
        a = max(0, m.start() - 40)
        err(f"{sid} 仍有否定式：…{txt[a:m.end()+40].strip()}…")

    # C-36：composition 與其他樣板不得用姿態動詞覆蓋 body_pose
    for m in POSE_VERB.finditer(txt):
        verb = m.group(1)
        want = {'seated':'sits','standing':'stands','crouching':'crouches',
                'lying':'lies','leaning':'leans','walking_frozen':'walks'}.get(s['body_pose'])
        if verb != want:
            err(f"{sid} prompt 出現「She {verb}」，但 body_pose={s['body_pose']}（C-36）")

    # C-34：每段都要有身材描述
    if 'Her build' not in txt and 'Her frame is slight' not in txt:
        err(f"{sid} 沒有任何身材描述——Reference Element 固定臉不等於固定全身（C-34）")

    # C-44：身材描述必須是該 framing 的版本，不得跨用到看不見的部位
    if pilot['body_en'][f] not in txt:
        err(f"{sid} 用的不是 framing={f} 對應的身材版本（C-44）")
    for other, tail in BODY_TAIL.items():
        order = ['face_closeup','chest_up','waist_up','knee_up','full_body']
        if order.index(other) > order.index(f) and tail in txt:
            err(f"{sid} framing={f} 卻描述了 {other} 才看得到的身體部位：「{tail}」（C-44）")

    # C-49：整段掃描——任何段落都不得提到該 framing 裁切外的身體部位，
    # 不只是身材模板。（R12 抓到朝向句寫 hip、動作句寫 hands、相機句寫 room。）
    ANAT = {
     'face_closeup': ['chest','bust','waist','hip','abdomen','leg','knee','feet','foot','thigh'],
     'chest_up':     ['waist','hip','abdomen','leg','knee','feet','foot','thigh'],
     'waist_up':     ['hip','leg','knee','feet','foot','thigh'],
     'knee_up':      ['feet','foot'],
     'full_body':    [],
    }
    # 服裝／道具名稱裡的同形字不算（例如 high-waisted jeans 是衣服規格，不是要求畫出腰）
    EXEMPT = ('high-waisted', 'waistband', 'knee-high', 'knee-length', 'legs of', 'wide-leg',
              'straight-leg', 'cargo', 'bent knee', 'footwear')
    # 景別句本身就是在陳述哪些部位落在邊界外——R11 已裁決這是有效寫法，不算違規
    body_lines = [l for l in txt.split('\n')
                  if not (l.startswith('The bottom edge of the picture')
                          or l.startswith('The whole of her is inside'))]
    scan = '\n'.join(body_lines)
    for tok in ANAT[f]:
        for m in re.finditer(r'\b' + tok + r's?\b', scan, re.I):
            a = max(0, m.start() - 30); ctx = scan[a:m.end() + 30]
            if any(x in ctx for x in EXEMPT): continue
            err(f"{sid} framing={f} 的裁切外部位「{tok}」出現在 prompt：…{ctx.strip()}…（C-49）")

    # C-50：相機幾何句不得鎖住 camera roll——與 composition=slightly_tilted 互斥。
    # 「直線不彎曲」（rectilinear）與「直線平行畫面邊緣」（roll=0）是兩件事。
    if s['imperfection_profile']['composition'] == 'slightly_tilted':
        for bad in ('parallel to the frame edges', 'vertical lines in the scene stay vertical',
                    'vertical lines stay vertical'):
            if bad in txt:
                err(f"{sid} composition=slightly_tilted，相機句卻寫「{bad}」"
                    f"——地平線歪了，場景垂直線就不會平行畫面邊緣（C-50）")

    # C-48：相機句不得假設室內
    if 'lines in the room' in txt:
        err(f"{sid} 相機句假設室內（`lines in the room`），戶外列不成立（C-48）")

    # C-44：face_closeup 的相機句與朝向句不得指名畫面外的軀幹
    if f == 'face_closeup':
        for bad in ('her body and the background', 'the front of her chest', 'her chest and both shoulders'):
            if bad in txt:
                err(f"{sid} 是 face_closeup，卻寫了「{bad}」——胸／軀幹在裁切外（C-44）")

    # C-45：戶外場景不得說光源來自 room / fixtures and windows
    OUTDOOR = {'park','city_street','train_platform'}
    if s['location'] in OUTDOOR and 'light in the room' in txt:
        err(f"{sid} 是戶外場景，封閉集合卻說光來自 room（C-45）")

    # C-46：封閉集合宣告只有她一人，前文不得再引入第二個 person token
    for tok in ('Someone standing', 'another person', 'a second person'):
        if tok in txt:
            err(f"{sid} 引入了第二個 person token「{tok}」，與封閉集合互相抵消（C-46）")

    # C-37：不得描述該景別看不見的服裝層
    lay = pilot['outfits'][s['outfit_id']]['en_layers']
    for k in ('top','top_hem','bottom','shoes','jewelry','rings','bag'):
        v = lay.get(k)
        if not v: continue
        shown = (k in VISIBLE[f]) \
            or (k == 'bag' and en[sid].get('bag_state','none').startswith('worn')) \
            or (k == 'rings' and any(en[sid].get('hands_visible', {}).values()))
        if not shown and v in txt:
            err(f"{sid} framing={f} 看不到 {k}，prompt 卻寫了「{v[:40]}…」（C-37）")

    # C-49：兩隻手都在裁切外時，prompt 任何地方都不得提到手或手臂
    # （封閉集合的樣板句「every visible hand connects to one of her own arms」除外）
    if not any(en[sid].get('hands_visible', {}).values()):
        for l in txt.split('\n'):
            if 'Everything in this picture is accounted for' in l: continue
            # 上臂在 chest_up 是看得到的，不算——這裡只擋「手」
            if re.search(r'\bhands?\b', l, re.I):
                err(f"{sid} 兩手都在裁切外，prompt 卻提到手／手臂：…{l.strip()[:70]}…（C-49）")

    # C-37：裁切外的手不得描述
    for side in ('left','right'):
        if not en[sid].get('hands_visible',{}).get(side, True):
            if f"Her {side} hand" in txt:
                err(f"{sid} {side} 手在裁切外，prompt 卻描述了它（C-37）")

    # C-37/C-39：宣告 expected_visible=False 的道具不得出現
    for q in s['props']:
        if not q.get('expected_visible') and en[sid]['props'][q['id']] in txt:
            err(f"{sid} 道具 {q['id']} 宣告不可見，卻寫進 prompt（C-37）")

    # 錨點必須被引用
    if '<<<' not in txt:
        err(f"{sid} 沒有引用 Reference Element")

# C-42：排除清單必須是正面封閉集合，不能靠 no/none
for sid, txt in pr.items():
    if 'Everything in this picture is accounted for' not in txt:
        err(f"{sid} 缺正面封閉集合的收尾（C-42）")

print("Phase C prompt 檢查")
if ERR:
    for e in ERR[:40]: print("  ✗ ", e)
    if len(ERR) > 40: print(f"  …還有 {len(ERR)-40} 條")
    print(f"\n{len(ERR)} 處問題")
    sys.exit(1)
print(f"  ✓ {len(pr)} 段全數通過")
