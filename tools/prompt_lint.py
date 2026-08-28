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

def lint(sid, prompt, is_close, is_luna):
    out = []
    w = len(prompt.split())
    if w > 120: out.append('過長 %d words' % w)
    if re.search(NEGATION, prompt, re.I): out.append('含否定句')
    if not re.search(HAIR_LEN, prompt, re.I): out.append('缺明確髮長（造型不算長度）')
    if is_luna and not re.search(BOB_GEOM, prompt, re.I): out.append('鮑伯缺剪裁幾何')
    pores = 'visible skin pores' in prompt.lower()
    if pores and not is_close: out.append('非近景卻寫 pores')
    if not pores and is_close: out.append('近景缺 pores')
    if re.search(TIMELINE, prompt, re.I): out.append('兩個時間點')
    if re.search(FLUTTER, prompt, re.I): out.append('抽象飄動描述')
    if 'selfie' in prompt.lower() and re.search(r'phone (up )?beside her (face|cheek)', prompt, re.I):
        out.append('自拍卻要求手機入鏡')

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
    ('抽象飄動', 'A woman walks, her shirt fluttering. Half body. Collarbone-length brown hair. '
      'Natural skin texture.', False, False, ['抽象飄動描述']),
]

def selftest():
    ok = True
    for name, p, c, l, expect in SELFTEST:
        _, got = lint('T', p, c, l)
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
        w, issues = lint(sid, pm.group(1), is_close, sid.startswith('LG'))
        om = re.search(OPTICS, b)
        if not om:
            issues.append('缺光學設定宣告')
        else:
            decl = om.group(1)
            if not any(v in decl for v in VALID_REFLECT): issues.append('反射面未宣告')
            if not any(v in decl for v in VALID_EXPO):    issues.append('曝光未宣告')
            if not any(v in decl for v in VALID_TEMP):    issues.append('色溫未宣告')
        if issues: print('%-7s ✗ %3dw  %s' % (sid, w, '｜'.join(issues))); bad += 1
        else:      print('%-7s ✓ %3dw' % (sid, w))
    print('\n%d 件，%d 件有問題。' % (len(blocks), bad))
    print('⚠️ 機械檢查全過**不等於**可以送生成——語意與物理一致性仍須人工／LLM 覆核。')
    return 1 if bad else 0

if __name__ == '__main__':
    if '--selftest' in sys.argv: sys.exit(0 if selftest() else 1)
    sys.exit(main(sys.argv[1]))
