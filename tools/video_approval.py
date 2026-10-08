#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
影片線的覆核指紋閘門（2026-09-01 建立）。

**為什麼是現在才建：**
`approval_check.py` 只掃 `GENERATION_PLAN_B1.md` 的 21 段圖片 prompt。
影片這條線（i2v、start frame、動畫）從第一支開始就沒有任何機械檢查——
每次都靠使用者開口問「這是 ChatGPT 審過的嗎」、我再手動跑一次逐字比對。

**我兩次說過「要開始量產影片時閘門一定要先建起來」，結果第二支影片
還是在沒有閘門的情況下跑的。**這支工具補上那個缺口。

格式與圖片線不同：影片 prompt 在 ``` 區塊裡，不是表格列。
所以用一行不可見的 HTML 註解當標記，放在 prompt 區塊的正上方：

    <!-- PROMPT_ID: shot1_pour_i2v | FP: sha1:0123456789ab | REVIEW: R19 -->
    ```
    A locked-off close-up of ...
    ```

三種狀態，與圖片線一致：
  已覆核  = 登記的 sha1 與現行 prompt 相符
  改過字  = 有登記但對不上（覆核後又被動過，即使只改一個字）
  未覆核  = 沒有登記（FP 欄為 -）

**「未覆核／改過字的不准送生成」是流程規則，程式只負責讓狀態變成可查的事實。**
"""
import re, sys, hashlib, glob

SPECS = ['clients/sushisolar-rujiao/I2V_TEST_01.md',
         'clients/sushisolar-rujiao/I2V_TEST_02.md',
         'clients/sushisolar-rujiao/SHOT3_SPEC.md',
         'clients/sushisolar-rujiao/SPEAK_SHOT_SPEC.md']

MARK = re.compile(
    r'<!--\s*PROMPT_ID:\s*([A-Za-z0-9_]+)\s*\|\s*FP:\s*(sha1:[0-9a-f]{12}|-)\s*'
    r'(?:\|\s*REVIEW:\s*([^\s|>-][^|>]*?)\s*)?-->\s*\n```\n(.+?)\n```', re.S)

def fingerprint(p):
    return 'sha1:' + hashlib.sha1(p.strip().encode('utf-8')).hexdigest()[:12]

def scan(paths):
    rows = []
    for path in paths:
        try:
            s = open(path, encoding='utf-8').read()
        except FileNotFoundError:
            continue
        for m in MARK.finditer(s):
            pid, fp, review, prompt = m.group(1), m.group(2), (m.group(3) or '').strip(), m.group(4)
            cur = fingerprint(prompt)
            if fp == '-':
                st = '未覆核'
            elif fp == cur:
                st = '已覆核'
            else:
                st = '改過字'
            rows.append((pid, st, cur, review, path, len(prompt.split())))
    return rows

def main(paths):
    rows = scan(paths)
    if not rows:
        print('沒有找到任何帶 PROMPT_ID 標記的影片 prompt。')
        return 1
    ok  = [r for r in rows if r[1] == '已覆核']
    bad = [r for r in rows if r[1] != '已覆核']
    print('影片線覆核指紋閘門\n')
    for pid, st, cur, review, path, words in rows:
        mark = {'已覆核': '✓', '改過字': '✗', '未覆核': '·'}[st]
        extra = f'  ← {review}' if review else ''
        print(f'  {mark} {pid:<30}{st}  {cur}  {words:>3}字{extra}')
    print(f'\n可送生成 {len(ok)} 段，不可送 {len(bad)} 段。')
    if bad:
        print('\n⚠️ 以下**不得送生成**，要先送覆核並登記指紋：')
        print('   ' + '、'.join(r[0] for r in bad))
    print('\n⚠️ 指紋相符只證明「這段字被覆核看過」，不證明它會成功。')
    return 1 if any(r[1] == '改過字' for r in rows) else 0

def stamp(paths, ids, note):
    n = 0
    for path in paths:
        try:
            s = open(path, encoding='utf-8').read()
        except FileNotFoundError:
            continue
        def rep(m):
            nonlocal n
            pid, fp, review, prompt = m.group(1), m.group(2), (m.group(3) or '').strip(), m.group(4)
            if pid not in ids:
                return m.group(0)
            n += 1
            r = note or review
            return ('<!-- PROMPT_ID: %s | FP: %s | REVIEW: %s -->\n```\n%s\n```'
                    % (pid, fingerprint(prompt), r, prompt))
        s2 = MARK.sub(rep, s)
        if s2 != s:
            open(path, 'w', encoding='utf-8').write(s2)
    return n

SELFTEST = [
    # id 只能是 ASCII（PROMPT_ID 規則），2026-09-01 自檢第一次跑就是敗在這裡
    ('ok',      'A locked-off close-up.', True,  '已覆核'),
    ('changed', 'A locked-off close-up.', False, '改過字'),
]

def selftest():
    import tempfile, os
    ok = True
    for name, prompt, correct, expect in SELFTEST:
        fp = fingerprint(prompt) if correct else 'sha1:000000000000'
        body = ('<!-- PROMPT_ID: t_%s | FP: %s | REVIEW: RX -->\n```\n%s\n```\n'
                % (name, fp, prompt))
        d = tempfile.mkdtemp(); p = os.path.join(d, 'spec.md')
        open(p, 'w', encoding='utf-8').write(body)
        got = scan([p])
        st = got[0][1] if got else '(沒抓到)'
        if st != expect:
            print('  ✗ %-8s 預期 %s，實得 %s' % (name, expect, st)); ok = False
        else:
            print('  ✓ %-8s %s' % (name, st))
    # 未登記
    d = __import__('tempfile').mkdtemp(); p = d + '/s.md'
    open(p, 'w', encoding='utf-8').write('<!-- PROMPT_ID: t_new | FP: - -->\n```\nX Y Z.\n```\n')
    st = scan([p])[0][1]
    print('  %s %-8s %s' % ('✓' if st == '未覆核' else '✗', '未登記', st))
    ok = ok and st == '未覆核'
    print('自檢：%s' % ('通過——會過也會擋' if ok else '**失敗，不要拿去檢查正式內容**'))
    return ok

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--selftest':
        sys.exit(0 if selftest() else 1)
    if len(sys.argv) > 2 and sys.argv[1] == '--stamp':
        note = sys.argv[3] if len(sys.argv) > 3 else ''
        print('已登記', stamp(SPECS, set(sys.argv[2].split(',')), note), '段')
    else:
        sys.exit(main(SPECS))
