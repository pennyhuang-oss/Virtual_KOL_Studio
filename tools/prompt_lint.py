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

# 未驗證的光學／焦點控制措辭（SEXY_SCENE_LIBRARY §24-E，R16 定案）。
# 允許的只有三個「已有使用證據的精確字串」，見 OPTICS_ALLOW；其餘一律先禁。
# R16：不要用「主體／背景」語意判斷——`creamy bokeh`、`only the subject in focus`
# 都是在寫背景，卻會強烈改變光學效果。
OPTICS_ALLOW = ('softly out of focus', 'falling out of focus', 'the wall menu out of focus')
OPTICS_DENY = (
    r'short telephoto', r'\btelephoto\b', r'\bcompressed\b',
    r'shallow depth of field', r'deep depth of field', r'everything sharp',
    r'\b(?:razor|tack)-sharp\b', r'\bface sharp\b',
    r'only [a-z ]{0,20}in focus', r'focus plane', r'\bbokeh\b',
    r'(?:completely|heavily) blurred', r'\b\d{2,3}\s?mm\b', r'\bf/\d',
)
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


# ── 不可刪除措辭（2026-08-29 Penny 核可後建立）─────────────────────
# 起因：覆核指定的安全措辭，在**兩輪內連續三次**從 prompt 裡消失。
#   R8b  為壓字數剪掉 LG-07 的 `toward the camera`        → 硬驗收②失去約束
#   R10  為壓字數剪掉 confined to／clearly visible in the central area／
#        of the camera／hands                              → 遮擋安全區被拆掉
#   R10  多樣性改寫時，LG-07 的 `her complete feet...` 與
#        YG-07 的 `Exactly two hands are visible.` 隨首段重寫一起消失
#
# 前兩次是**主動剪掉**，第三次是**重寫時被動遺失**——後者更危險，
# 因為沒有人會注意到一句話「不見了」。
#
# 機制：規格表登記該件的不可刪除措辭與出處，這支檢查器驗它們**逐字**還在。
# 這不是風格規則，是「覆核講過的話有沒有被執行」的稽核，所以是硬性的。
IMMUTABLE = r'\| \*\*不可刪除措辭\*\* \|(.+?)\|\n'
FRAG      = r'`([^`]+)`'

def lint(sid, prompt, is_close, is_luna, decl=None, immutable=()):
    out = []
    has_bg = BG_MARK in prompt
    w = len(prompt.split())
    cap = 120 + (BG_LEN if has_bg else 0)
    # 2026-08-29 R11 判定 A：**放棄硬性字數上限。**
    # 120／160 沒有成品失敗分界支持，是啟發式；但為了守它，我已經**連續兩輪**
    # 把覆核指定的界定詞剪掉（R8b 剪掉 toward the camera、R10 剪掉 confined to／
    # clearly visible in the central area／of the camera），造成可驗收關係退化。
    # 覆核原文：「這證明目前硬上限的實際危害，而『多幾個必要單字必然稀釋任務』
    # 仍沒有同等證據。」
    # 改為只提醒、不阻擋，也**不得因此自動剪字**。
    # 接觸點、相機視線、遮擋安全區、身份／服裝固定詞，一律不得為壓字數而刪。
    if w > cap:
        out.append('⚠字數 %d（超過參考值 %d，建議分批 preflight，不阻擋送測）' % (w, cap))
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

    # 挖掉 allowlist 的精確字串後才掃，這樣被檢查的文字與實際送出的文字仍然對得起來
    optics = prompt
    for allowed in OPTICS_ALLOW:
        optics = optics.replace(allowed, ' ' * len(allowed))
    for pat in OPTICS_DENY:
        m = re.search(pat, optics, re.I)
        if m:
            out.append('未驗證的光學／焦點控制措辭：%s' % m.group(0))
            break

    # 宣告與 prompt 必須一致。沒有宣告的件只提醒，不擋——
    # 8 件已核准的走的是另一套處理（規格對齊成品、prompt 不動）。
    for frag in immutable:
        if frag not in prompt:
            out.append('刪掉了覆核指定的措辭：%s' % frag[:46])

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
    # R16：allowlist 的三個精確字串要放行，denylist 的同義／增強詞要擋
    ('景深 allowlist 放行', 'A woman smiles, the wall menu out of focus. Half body. Collarbone-length brown hair. '
      'A tee. A cafe. Soft light. Natural skin texture.', False, False, []),
    ('景深 denylist 擋 bokeh', 'A woman smiles, creamy bokeh behind her. Half body. Collarbone-length brown hair. '
      'A tee. A cafe. Soft light. Natural skin texture.',
      False, False, ['未驗證的光學／焦點控制措辭：bokeh']),
    ('景深 denylist 擋焦距', 'A woman smiles, shot on 85mm. Half body. Collarbone-length brown hair. '
      'A tee. A cafe. Soft light. Natural skin texture.',
      False, False, ['未驗證的光學／焦點控制措辭：85mm']),
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
    ('覆核措辭被刪掉', 'A woman smiles. Half body. Collarbone-length brown hair. A tee. Her bedroom. '
      'Soft light. Natural skin texture.', False, False,
      ['刪掉了覆核指定的措辭：Exactly two hands are visible.'],
      '私密場景（測試）——只有本人', ('Exactly two hands are visible.',)),
    ('覆核措辭還在', 'A woman smiles. Exactly two hands are visible. Half body. Collarbone-length brown hair. '
      'A tee. Her bedroom. Soft light. Natural skin texture.', False, False, [],
      '私密場景（測試）——只有本人', ('Exactly two hands are visible.',)),
    ('抽象飄動', 'A woman walks, her shirt fluttering. Half body. Collarbone-length brown hair. '
      'Natural skin texture.', False, False, ['抽象飄動描述']),
]

def selftest():
    ok = True
    for row in SELFTEST:
        name, p, c, l, expect = row[:5]
        decl = row[5] if len(row) > 5 else '私密場景（測試）——只有本人'
        imm  = row[6] if len(row) > 6 else ()
        _, got = lint('T', p, c, l, decl, imm)
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
        im = re.search(IMMUTABLE, b)
        frags = tuple(re.findall(FRAG, im.group(1))) if im else ()
        w, issues = lint(sid, pm.group(1), is_close, sid.startswith('LG'),
                         dm.group(1) if dm else None, frags)
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
