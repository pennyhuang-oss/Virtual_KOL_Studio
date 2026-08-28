# -*- coding: utf-8 -*-
"""送生成前的 Prompt 機械檢查（見 SEXY_SCENE_LIBRARY.md 第 25 點）。

⚠️ 這支腳本只做**字串型**檢查。語意型的問題（自拍需要幾隻手、髮型基礎幾何與
造型是否打架、spec 與 prompt 是不是同一張圖）**它抓不到**，必須人工或 LLM 覆核。
不要把「機械檢查全過」當成可以送生成。

用法：python3 tools/prompt_lint.py <plan.md>
      python3 tools/prompt_lint.py --selftest
"""
import io, re, sys

# 真正的「長度」token。造型（低馬尾／鯊魚夾／盤髮／髮箍）不算長度——
# 低馬尾可以是及肩也可以是及腰，沒有鎖住任何東西。
# 這一條是 2026-08-27 外部覆核抓出來的：舊版把 low ponytail 當成有長度，
# 跟第 24 點自己寫的規則矛盾。
HAIR_LEN = r'(collarbone-length|chin-length|shoulder-length|waist-length|cropped short)'
# 鮑伯的底層剪裁幾何。兩種 wording 都已與成功結果共現（2026-08-27 preflight 3/3 穩定），
# 決定**不統一**——改寫沒有 production 收益，只會製造新的未驗證變因。
# 註：只能說兩者與成功共現，不能說各自已證明為因果控制桿。
BOB_GEOM = r'(cut evenly at the jawline|even blunt ends along the jawline)'
WARN_ONLY = ('⚠',)          # 以 ⚠ 開頭者只提醒、不列為不合格
NEGATION = r'\b(no|not|without|avoid|never)\b'
TIMELINE = r'(then |breaking into|just starting to|and then|before turning)'
FLUTTER  = r'(fluttering|lifting in the breeze|trailing in the|blowing in the wind)'
# 2026-08-28 二次修正：第一版把競品的「風格觀察」當成普遍物理定律，
# 硬性要求 21 件都要有三機制，結果 21/21 全紅——**那個紅燈本身會誘導過度修正**。
# 覆核指出正確做法是三個「可判定欄位」，各自允許「不適用」。
# 所以 lint 改成：檢查 spec 有沒有**明確宣告**，而不是檢查 prompt 有沒有那三句話。
OPTICS = r'\| \*\*光學設定\*\* \|(.+?)\|'
VALID_REFLECT = ('反射面：具名', '反射面：不適用')
VALID_EXPO    = ('曝光：取捨', '曝光：低反差')
VALID_TEMP    = ('色溫：分裂', '色溫：不適用')


# ── 背景路人（2026-08-29 加入）────────────────────────────────────
# 起因：13 段 prompt 寫完後才發現 7 件公共場景**一個路人都沒有**，
# 而 SEXY_SCENE_LIBRARY §9 早就寫了「公共場景必須有」，且是 soul_2 上 14/14 實測過的。
# 那幾輪的注意力都在手部與光線（R7／R8 的議題），沒有人提醒，我也沒回去對 §9。
# 這條檢查就是為了讓它以後漏不掉。
#
# 兩個刻意的例外，都記在這裡而不是藏在程式裡：
#  1. 這段已驗證措辭含 `never`，會撞到本檔的否定句檢查。
#     D-03 說的是否定句「無效」，不是「有害」；整段是 14/14 驗證過的，
#     改寫它等於引入新變因換取零已知收益。**選擇保留原文，並在檢查前把它切掉。**
#  2. 它有 40 字。120 字上限是沒有實證來源的啟發式（已核准成品落在 94–118），
#     所以**上限只管我自己寫的內容**，這段固定附加區塊另計。
BG_BLOCK = ('A few anonymous strangers in the mid-ground going about their own business, '
            'backs turned or heads angled away, never looking at the camera, softly out of '
            'focus with slight motion blur, clearly different from her in build, age and clothing.')
BG_LEN   = len(BG_BLOCK.split())
BG_MARK  = 'anonymous strangers'
PEOPLE_DECL = r'\| \*\*人物入鏡\*\* \|(.+?)\|'

def lint(sid, prompt, is_close, is_luna, decl=None):
    out = []
    has_bg = BG_MARK in prompt
    w = len(prompt.split())
    cap = 120 + (BG_LEN if has_bg else 0)
    if w > cap: out.append('過長 %d words（上限 %d）' % (w, cap))
    # 否定句：檢查**實際要送出的整段文字**，只對已驗證區塊所在的字元範圍放行。
    # 2026-08-29 覆核修正：原本先把區塊 replace 掉再檢查，
    # 那會讓「檢查的文字」與「實際送出的文字」不同——檢查器就不再代表真實輸入。
    # 改成具名 allowlist：算出區塊在 prompt 裡的字元範圍，
    # 落在範圍內的否定詞放行，範圍外的照常擋。
    spans = []
    st = prompt.find(BG_BLOCK)
    while st != -1:
        spans.append((st, st + len(BG_BLOCK)))
        st = prompt.find(BG_BLOCK, st + 1)
    for m in re.finditer(NEGATION, prompt, re.I):
        if not any(a <= m.start() and m.end() <= b for a, b in spans):
            out.append('含否定句')
            break
    if not re.search(HAIR_LEN, prompt, re.I): out.append('缺明確髮長（造型不算長度）')
    if is_luna and not re.search(BOB_GEOM, prompt, re.I): out.append('鮑伯缺剪裁幾何')
    pores = 'visible skin pores' in prompt.lower()
    if pores and not is_close: out.append('非近景卻寫 pores')
    if not pores and is_close: out.append('近景缺 pores')
    if re.search(TIMELINE, prompt, re.I): out.append('兩個時間點')
    if re.search(FLUTTER, prompt, re.I): out.append('抽象飄動描述')
    if 'selfie' in prompt.lower() and re.search(r'phone (up )?beside her (face|cheek)', prompt, re.I):
        out.append('自拍卻要求手機入鏡')

    # 宣告與 prompt 必須一致。沒有宣告的件只提醒，不擋——
    # 8 件已核准的走的是另一套處理（規格對齊成品、prompt 不動）。
    if decl is None:
        out.append('⚠尚未整併（無人物入鏡宣告）')   # 警告類，見 WARN_ONLY
    elif '公共場景——必寫' in decl:
        if not has_bg: out.append('公共場景卻沒有背景路人')
    elif '私密場景' in decl or '景別排除' in decl:
        if has_bg: out.append('宣告不寫背景路人，prompt 卻有')
    else:
        out.append('人物入鏡宣告無法辨識')

    return w, out

SELFTEST = [
    # (說明, prompt, is_close, is_luna, 應該要中的項目)
    ('known-good 近景', 'A woman smiles. Close-up, camera at her eye level. Collarbone-length brown hair. '
      'A tee. A cafe. Soft light on her face. Visible skin pores, natural skin texture, subtle film grain.',
      True, False, []),
    ('造型冒充長度', 'A woman smiles. Half body. Brown hair in a low ponytail. A tee. A cafe. '
      'Soft light. Natural skin texture.', False, False, ['缺明確髮長（造型不算長度）']),
    ('否定句', 'A woman smiles, no open sky in frame. Half body. Collarbone-length brown hair. '
      'A tee. Natural skin texture.', False, False, ['含否定句']),
    ('兩個時間點', 'A woman pouts and then breaking into a laugh. Half body. Collarbone-length brown hair. '
      'Natural skin texture.', False, False, ['兩個時間點']),
    ('全身卻寫 pores', 'A woman stands. Full body. Collarbone-length brown hair. '
      'Visible skin pores, natural skin texture.', False, False, ['非近景卻寫 pores']),
    ('Luna 缺剪裁幾何', 'A woman smiles. Half body. A chin-length black bob, tucked behind her ear. '
      'Natural skin texture.', False, True, ['鮑伯缺剪裁幾何']),
    ('鮑伯新 wording', 'A woman smiles. Half body. A blunt chin-length black bob with even blunt ends '
      'along the jawline. Natural skin texture.', False, True, []),
    ('公共場景漏路人', 'A woman smiles. Half body. Collarbone-length brown hair. A tee. A night market. '
      'Soft light. Natural skin texture.', False, False, ['公共場景卻沒有背景路人'], '公共場景——必寫背景路人（夜市）'),
    ('私密場景誤加路人', 'A woman smiles. Half body. Collarbone-length brown hair. A tee. Her bedroom. '
      'A few anonymous strangers in the mid-ground going about their own business, backs turned or heads '
      'angled away, never looking at the camera, softly out of focus with slight motion blur, clearly '
      'different from her in build, age and clothing. Soft light. Natural skin texture.',
      False, False, ['宣告不寫背景路人，prompt 卻有'], '私密場景（臥室）——只有本人'),
    ('合法區塊＋區塊外否定詞', 'A woman smiles, no open sky in frame. Half body. Collarbone-length brown hair. '
      'A tee. A night market. A few anonymous strangers in the mid-ground going about their own business, '
      'backs turned or heads angled away, never looking at the camera, softly out of focus with slight '
      'motion blur, clearly different from her in build, age and clothing. Soft light. Natural skin texture.',
      False, False, ['含否定句'], '公共場景——必寫背景路人（夜市）'),
    ('抽象飄動', 'A woman walks, her shirt fluttering. Half body. Collarbone-length brown hair. '
      'Natural skin texture.', False, False, ['抽象飄動描述']),
]

def selftest():
    ok = True
    for row in SELFTEST:
        name, p, c, l, expect = row[:5]
        decl = row[5] if len(row) > 5 else '私密場景（測試）——只有本人'
        _, got = lint('T', p, c, l, decl)
        if sorted(got) != sorted(expect):
            print('  ✗ %-16s 預期 %s，實得 %s' % (name, expect, got)); ok = False
        else:
            print('  ✓ %-16s %s' % (name, '無問題' if not expect else got))
    print('自檢：%s' % ('通過——檢查器會過也會擋' if ok else '**失敗，不要拿去檢查正式內容**'))
    return ok

def main(path):
    md = io.open(path, encoding='utf-8').read()
    blocks = [b for b in re.split(r'\n(?=### [YL]G-\d\d)', md) if re.match(r'### [YL]G-\d\d', b)]
    bad = 0
    for b in blocks:
        sid = re.match(r'### ([YL]G-\d\d[AB]?)', b).group(1)
        pm = re.search(r'\| \*\*生成 prompt\*\* \| `([^`]+)`', b)
        fm = re.search(r'\| \*\*機位與構圖\*\* \| \*\*([^*]+)\*\*', b)
        if not pm: print('%-7s ✗ 沒有生成 prompt' % sid); bad += 1; continue
        is_close = '近景' in fm.group(1) or '特寫' in fm.group(1)
        dm = re.search(PEOPLE_DECL, b)
        w, issues = lint(sid, pm.group(1), is_close, sid.startswith('LG'),
                         dm.group(1) if dm else None)
        om = re.search(OPTICS, b)
        if not om:
            issues.append('缺光學設定宣告')
        else:
            decl = om.group(1)
            if not any(v in decl for v in VALID_REFLECT): issues.append('反射面未宣告')
            if not any(v in decl for v in VALID_EXPO):    issues.append('曝光未宣告')
            if not any(v in decl for v in VALID_TEMP):    issues.append('色溫未宣告')
        hard = [x for x in issues if not x.startswith(WARN_ONLY)]
        warn = [x for x in issues if x.startswith(WARN_ONLY)]
        if hard:
            print('%-7s ✗ %3dw  %s' % (sid, w, '｜'.join(issues))); bad += 1
        elif warn:
            print('%-7s ⚠ %3dw  %s' % (sid, w, '｜'.join(warn)))
        else:
            print('%-7s ✓ %3dw' % (sid, w))
    print('\n%d 件，%d 件有問題。' % (len(blocks), bad))
    print('⚠️ 機械檢查全過**不等於**可以送生成——語意與物理一致性仍須人工／LLM 覆核。')
    return 1 if bad else 0

if __name__ == '__main__':
    if '--selftest' in sys.argv: sys.exit(0 if selftest() else 1)
    sys.exit(main(sys.argv[1]))
