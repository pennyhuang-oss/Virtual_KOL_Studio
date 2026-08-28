#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
送測前的覆核狀態閘門（2026-08-29 建立）。

**這個機制在 R7 Q5 就被建議過，我一直沒做：**
> 「最好為每件保存 prompt 版本或內容雜湊，**避免後續悄悄改字後仍沿用舊核准**。」

沒做的後果，2026-08-29 由使用者問出來：
LG-01 是 R10 判 REVISE、R11 只裁決了「片語層級」的還原，
**組裝後的完整 prompt 從來沒有人看過整段**，我就直接送生成了。
我把「片語被核可」當成「整段被核可」——那是我自己的判斷，不是覆核給的授權。

規則很簡單：**指紋對得上才可以送生成。**
  已覆核  = 規格表登記的 sha1 與現行 prompt 相符
  改過字  = 有登記但對不上（覆核後又被動過，即使只改一個字）
  未覆核  = 沒有登記

這支工具不知道你想生成哪一件，所以它只報狀態；
**「未覆核／改過字的不准送生成」是流程規則，不是程式能擋的**——
但至少現在「有沒有被覆核過」是一個可查的事實，不是我的印象。
"""
import re, sys, hashlib

FP = r'\| \*\*覆核指紋\*\* \| sha1:([0-9a-f]{12})(?:（(.*?)）)? \|'

def fingerprint(prompt):
    return hashlib.sha1(prompt.encode('utf-8')).hexdigest()[:12]

def scan(path):
    s = open(path).read()
    b = re.split(r'\n### ((?:YG|LG)-\d+[AB]?)｜', s)
    rows = []
    for i in range(1, len(b), 2):
        body = b[i+1]
        pm = re.search(r'\| \*\*生成 prompt\*\* \| `([^`]+)`', body)
        if not pm:
            continue
        fm = re.search(FP, body)
        cur = fingerprint(pm.group(1))
        if not fm:
            rows.append((b[i], '未覆核', cur, ''))
        elif fm.group(1) == cur:
            rows.append((b[i], '已覆核', cur, fm.group(2) or ''))
        else:
            rows.append((b[i], '改過字', cur, fm.group(2) or ''))
    return rows

def main(path):
    rows = scan(path)
    ok = [r for r in rows if r[1] == '已覆核']
    bad = [r for r in rows if r[1] != '已覆核']
    print('覆核狀態閘門\n')
    for name, st, cur, note in rows:
        mark = {'已覆核': '✓', '改過字': '✗', '未覆核': '·'}[st]
        extra = f'  ← {note}' if note else ''
        print(f'  {mark} {name:<8}{st}  sha1:{cur}{extra}')
    print(f'\n可送生成 {len(ok)} 件，不可送 {len(bad)} 件。')
    if bad:
        print('\n⚠️ 以下**不得送生成**，要先送覆核並登記指紋：')
        print('   ' + '、'.join(r[0] for r in bad))
    return 0

def stamp(path, names, note):
    """把指定件的現行 prompt 指紋寫進規格表。只在覆核通過後使用。"""
    s = open(path).read()
    b = re.split(r'(\n### (?:YG|LG)-\d+[AB]?｜)', s)
    out, i, n = [b[0]], 1, 0
    while i < len(b):
        h, body = b[i], b[i+1]
        k = re.match(r'\n### ((?:YG|LG)-\d+[AB]?)｜', h).group(1)
        if k in names:
            pm = re.search(r'\| \*\*生成 prompt\*\* \| `([^`]+)`', body)
            row = f'| **覆核指紋** | sha1:{fingerprint(pm.group(1))}（{note}） |\n'
            body = re.sub(FP + r'\n', '', body)
            body = re.sub(r'(\| \*\*生成 prompt\*\* \| `[^`]+` \|\n)',
                          lambda m: m.group(1) + row, body, count=1)
            n += 1
        out.append(h); out.append(body); i += 2
    open(path, 'w').write(''.join(out))
    return n

if __name__ == '__main__':
    PLAN = 'clients/sushisolar-rujiao/GENERATION_PLAN_B1.md'
    if len(sys.argv) > 2 and sys.argv[1] == '--stamp':
        names = set(sys.argv[2].split(','))
        note = sys.argv[3] if len(sys.argv) > 3 else '已核准成品'
        print('已登記', stamp(PLAN, names, note), '件')
    else:
        sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else PLAN))
