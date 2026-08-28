#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""跨檔案資訊一致性檢查。

為什麼需要：這個 repo 的規格散在 JSON、Markdown 人設檔、計畫文件、SOP、索引裡。
改了一處沒同步另一處，下次讀取就會拿到舊值——這已經發生過很多次
（C-07 的衍生統計漂移、C-01 的雙重真理來源、Round 1 的錯誤修法被沿用）。

這支腳本把「同一個事實在不同檔案裡必須一致」寫成可執行的斷言。
改規格之後跑一次，就知道還有哪裡沒同步。
"""
import json, os, re, sys

ERR, WARN = [], []
def err(m): ERR.append(m)
def warn(m): WARN.append(m)
def read(p): return open(p, encoding='utf-8').read()

pilot = json.load(open('pilot/nico_pilot.json', encoding='utf-8'))
prof  = json.load(open('kols/nico-tsai/profile.json', encoding='utf-8'))
ids   = pilot['identity_spec']
ap    = prof['identity']['appearance']

# ── 1. Nico 的身材數字：pilot / profile / character.md 必須一致 ──
bn, m = ids['body_numeric'], ap['measurements']
for k_p, k_m in (('height_cm','height_cm'), ('weight_kg','weight_kg'),
                 ('bust_cm','bust_cm'), ('waist_cm','waist_cm'),
                 ('hip_cm','hip_cm'), ('cup','cup_size')):
    if bn[k_p] != m[k_m]:
        err(f"身材 {k_p}：pilot={bn[k_p]} ≠ profile={m[k_m]}")
trio = f"{bn['bust_cm']}-{bn['waist_cm']}-{bn['hip_cm']}"
ch = read('kols/nico-tsai/character.md')
if trio not in ch:
    err(f"character.md 沒有現行三圍 {trio}")
if f"| {bn['cup']} |" not in ch:
    err(f"character.md 的罩杯與 pilot 的 {bn['cup']} 不符")

# ── 2. 舊值不得出現在任何「現行」檔案裡 ──
HIST = ('review/rounds/', 'BATCH3_REVIEW_PACKET.md', 'pilot/NICO_PILOT_REVIEW',
        'kols/nico-tsai/generation_notes.md', 'review/LEDGER.md', 'review/REVIEW.md',
        'pilot/semantic_review.md', 'review/REVIEW_PHASE_C.md', 'tools/check_consistency.py')
STALE = {
    '86-59-88': 'Nico 的舊三圍',
    '細長丹鳳眼': 'Nico 的舊臉部描述（已改少女短臉型）',
    '冷灰奶茶（漂色）': 'Nico 的舊髮色（已改冷調中棕＋銀灰挑染）',
}
for root, dirs, files in os.walk('.'):
    dirs[:] = [d for d in dirs if d not in ('.git', '__pycache__', 'images')]
    for f in files:
        if not f.endswith(('.md', '.json')): continue
        p = os.path.join(root, f).lstrip('./')
        if any(h in p for h in HIST): continue
        try: t = read(p)
        except Exception: continue
        # 只在提到 nico 的檔案裡判定（其他角色可以有自己的數字）
        if 'nico' not in t.lower() and 'Nico' not in t: continue
        for pat, why in STALE.items():
            for ln_no, ln in enumerate(t.split('\n'), 1):
                if pat in ln and ('ico' in ln or 'ICO' in ln or '02' in ln[:6]):
                    err(f"{p}:{ln_no} 仍有 {why}：{pat}")

# ── 3. 錨點 id 必須一致：pilot 的 prompt、profile、builder ──
anchor = prof['ai_assets']['reference_element']['id']
prompts = json.load(open('pilot/phase_c_prompts.json', encoding='utf-8'))
for sid, txt in prompts.items():
    if f"<<<{anchor}>>>" not in txt:
        err(f"prompt {sid} 沒有引用現行錨點 {anchor}")
if anchor not in read('tools/build_phase_c_prompts.py'):
    err("build_phase_c_prompts.py 的 ANCHOR 與 profile 的錨點 id 不符")

# ── 4. prompt 必須是現行 spec 產生的（不得手動編輯後漂移）──
import subprocess
r = subprocess.run([sys.executable, 'tools/build_phase_c_prompts.py'],
                   capture_output=True, text=True)
if r.returncode != 0:
    err("build_phase_c_prompts.py 執行失敗：" + r.stderr.strip()[:200])
else:
    fresh = json.load(open('pilot/phase_c_prompts.json', encoding='utf-8'))
    if fresh != prompts:
        err("phase_c_prompts.json 與 spec 重新產生的結果不同——有人手動改過 prompt")

# ── 5. 訓練集張數：pilot / profile / SOP 必須一致 ──
n = len(pilot['phase_c_shots'])
if prof['ai_assets']['training_images_v1']['target_count'] != n:
    err(f"profile 的 target_count ≠ pilot 的 {n} 張")
if pilot['phase_c_quota']['shots'] != n:
    err(f"phase_c_quota.shots ≠ 實際 {n} 張")

# ── 6. 已被實測推翻的修法不得以「現行建議」的形式留在 SOP ──
sop = read('KOL_TRAINING_SOP.md')
if '這個模型的實測行為' not in sop:
    err("KOL_TRAINING_SOP.md 缺〈這個模型的實測行為〉章節")
sl = sop.split('\n')
for i, line in enumerate(sl):
    if '排他性措辭' not in line: continue
    window = ' '.join(sl[max(0, i-2):i+3])   # 推翻的說明可能在前後幾行
    if '推翻' not in window and '無效' not in window:
        err(f"SOP 仍把已推翻的「排他性措辭」當現行修法：{line[:60]}")

# ── 7. 索引與 README 的狀態要跟得上 ──
idx = json.load(open('kols/index.json', encoding='utf-8'))
ks = idx['kols'] if isinstance(idx, dict) and 'kols' in idx else idx
nico = next(k for k in ks if k['id'] == 'nico-tsai')
if nico.get('status') == 'draft':
    err("kols/index.json 的 nico-tsai 仍是 draft，但選角與錨定已完成")
nico_row = [l for l in read('README.md').split('\n') if '[nico-tsai]' in l]
if not nico_row:
    err("README.md 找不到 nico-tsai 那一列")
elif 'draft' in nico_row[0]:
    err("README.md 的 Nico 狀態仍是 draft，但選角與錨定已完成")
# 其餘 19 位維持 draft/待訓練是正確的（凍結中），不檢查

# ── 8. 憲章原則六與職責分界必須存在 ──
if '原則六' not in read('PERSONA_CANON.md'):
    err("PERSONA_CANON.md 缺原則六（臉部骨架必須寫死並與既有角色區隔）")
if '必須由使用者拍板' not in read('review/README.md'):
    err("review/README.md 缺「哪些事不能交給外部覆核者決定」")

# ── 9. 髮色的三處敘述要一致（都必須提到挑染）──
for p in ('kols/nico-tsai/profile.json', 'kols/nico-tsai/character.md',
          'kols/nico-tsai/content_style.md'):
    if '挑染' not in read(p):
        err(f"{p} 沒有記錄那段銀灰挑染（使用者已裁決保留為造型）")
if '挑染' not in pilot.get('hair_color_en', '') and 'silver-grey' not in pilot.get('hair_color_en', ''):
    err("pilot 的 hair_color_en 沒有描述那段銀灰挑染")

# ══════════════════════════════════════════════════════════════════
# 餐廳批次一（Yuna＋Luna）—— 2026-08-28 加入
# 這條線與 Nico 線共用同一個 repo，但事實散在不同檔案裡，
# 之前就發生過 profile.json 已改台北、character.md 身分表還寫首爾。
# ══════════════════════════════════════════════════════════════════

PLAN = 'clients/sushisolar-rujiao/GENERATION_PLAN_B1.md'

for slug, city, sid in (
        ('yuna-kim',    '台北', '235794a5-2eff-45fb-91b4-3232910afefa'),
        ('luna-tanaka', '台北', 'a3dc13ec-16e7-4990-89c6-9e0461db46ef')):
    pj = json.load(open(f'kols/{slug}/profile.json', encoding='utf-8'))
    idn = pj['identity']

    # 現居地：profile.json 與 character.md 的身分表必須都是台北
    if 'Taipei' not in idn['current_location']:
        err(f"{slug} profile.json 的 current_location 不是台北：{idn['current_location']}")
    cm = read(f'kols/{slug}/character.md')
    row = [l for l in cm.split('\n') if l.startswith('| 現居地 |')]
    if not row:
        err(f"{slug} character.md 找不到「現居地」那一列")
    elif city not in row[0]:
        err(f"{slug} character.md 的現居地仍是舊值：{row[0].strip()}")

    # 搬遷設定必須成套存在，否則「她是外國人住在台灣」這個前提會失傳
    if 'relocation' not in idn:
        err(f"{slug} profile.json 缺 relocation 區塊")
    if '在台灣生活' not in cm:
        err(f"{slug} character.md 缺「在台灣生活」段")

    # soul_id：profile.json 必須與實際送生成的那一支相符
    got = pj['identity']['appearance'].get('ai_generation', {}).get('soul_id')
    if got != sid:
        err(f"{slug} profile.json 的 soul_id={got}，與實際生成用的 {sid} 不符")
    if os.path.exists(PLAN) and sid not in read(PLAN) and sid not in read('CALIBRATION_TEST.md'):
        warn(f"{slug} 的 soul_id 沒有出現在生成計畫或校準紀錄裡")

# 已降級的曝光寫法不得再被當成建議寫法
BANNED = 'background exposed the same brightness as her skin'
for p in ('SEXY_SCENE_LIBRARY.md', 'review/restaurant-b1/LEDGER.md'):
    t = read(p)
    if BANNED in t and ('禁用' not in t and '降級' not in t):
        err(f"{p} 還在把「{BANNED}」當現行建議寫法（已於 2026-08-28 降級）")

# 21 段既有 prompt 仍帶著那句，是**已知待處理**，不是新問題——
# 只報數字，不當錯誤。全部改寫要等 #15 的高反差場景驗證過。
if os.path.exists(PLAN):
    n = read(PLAN).count(BANNED)
    if n:
        warn(f"{PLAN} 仍有 {n} 段 prompt 使用已降級的曝光寫法"
             f"（等 LEDGER #15 高反差驗證後改寫；已核准成品不重跑）")

# 三態光學宣告：每件 spec 都要有，否則 prompt_lint 會漏檢
if os.path.exists(PLAN):
    plan = read(PLAN)
    n_items = len(re.findall(r'\n### (?:YG|LG)-\d+[AB]?｜', plan))
    n_optics = plan.count('| **光學設定** |')
    if n_items and n_optics != n_items:
        err(f"{PLAN}：{n_items} 件 spec 只有 {n_optics} 件有光學設定宣告")

# 兩條覆核線的檔名分家必須有索引，否則下一個人會覆蓋掉別人的 LEDGER
if not os.path.exists('review/INDEX.md'):
    err("review/INDEX.md 不存在——兩條覆核工作線共用 review/，沒有索引會互相覆蓋")
else:
    idx = read('review/INDEX.md')
    for p in ('review/LEDGER.md', 'review/restaurant-b1/LEDGER.md'):
        if p not in idx:
            err(f"review/INDEX.md 沒有列出 {p}")

print("跨檔案一致性檢查")
for w in WARN: print("  ⚠ ", w)
if ERR:
    for e in ERR: print("  ✗ ", e)
    print(f"\n{len(ERR)} 處資訊落差")
    sys.exit(1)
print("  ✓ 全數一致")
