#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
批次多樣性配額檢查（2026-08-29 建立）。

起因：餐廳批次一 21 件寫完後，使用者指出「姿勢都非常單一，
真正的活人怎麼可能每次拍照姿勢都這麼普通」。實際清點後屬實——
11/21 手或物件停在臉／下巴附近，16/21 正面看鏡頭。

成因不是隨機：D-06「表情必須綁實體動作」被無限套用，
而要讓物件在畫面裡看得見，最省事的解法就是舉到臉旁邊。

⚠️ **這支腳本只做批次層級的分布檢查，不做逐件要求。**
2026-08-28 才發生過「把風格觀察寫成逐件硬性規則、21/21 全紅、
而那個紅燈本身誘導過度修正」。單件永遠不因為「不夠多元」被擋。

配額定義見 WARDROBE_SYSTEM.md 三點五。
"""
import re, sys

# (名稱, 在多樣性宣告裡的標記, 比較運算, 門檻)
QUOTAS = [
    ('動作中',   'A 動作中',        '>=', 5),
    ('不看鏡頭', '視線：不看鏡頭',   '>=', 5),
    ('手在臉旁', '手在臉旁：**是**', '<=', 3),
    ('自拍',     '1 自拍',          'range', (2, 3)),
    ('背後過肩', ('4 過肩', '4 背後'), '>=', 2),
    ('框架物',   '6 框架物',        '>=', 3),
    ('非站坐',   'D 非站坐',        '>=', 3),
]
DECL = r'\| \*\*多樣性\*\* \| (.+?) \|\n'

def hit(decl, mark):
    return any(m in decl for m in mark) if isinstance(mark, tuple) else mark in decl

def collect(path):
    s = open(path).read()
    b = re.split(r'\n### ((?:YG|LG)-\d+[AB]?)｜', s)
    items = []
    for i in range(1, len(b), 2):
        m = re.search(DECL, b[i+1])
        if m:
            items.append((b[i], m.group(1)))
    return items

def check(items):
    hard, notes = [], []
    n = len(items)
    for name, mark, op, thr in QUOTAS:
        got = sum(1 for _, d in items if hit(d, mark))
        if op == '>=':
            ok, q = got >= thr, f'≥{thr}'
        elif op == '<=':
            ok, q = got <= thr, f'≤{thr}'
        else:
            ok, q = thr[0] <= got <= thr[1], f'{thr[0]}–{thr[1]}'
        notes.append(f"  {'✓' if ok else '✗'} {name:<8}{got} 件（配額 {q}）")
        if not ok:
            hard.append(f'{name} {got} 件，配額 {q}')
    # 相鄰兩件不可同時同姿勢類別＋同相機關係
    def key(d):
        p = re.search(r'姿勢：([^｜]+)', d)
        c = re.search(r'相機：([^｜]+)', d)
        return (p.group(1) if p else '', c.group(1) if c else '')
    for i in range(len(items) - 1):
        if key(items[i][1]) == key(items[i+1][1]):
            hard.append(f'{items[i][0]} 與 {items[i+1][0]} 姿勢與相機關係完全相同')
    return hard, notes, n

def main(path):
    items = collect(path)
    if not items:
        print('找不到任何多樣性宣告——尚未整併，不檢查。')
        return 0
    hard, notes, n = check(items)
    print(f'批次多樣性（{n} 件有宣告）')
    for x in notes: print(x)
    if hard:
        print()
        for x in hard: print('  ✗ ' + x)
        print(f'\n{len(hard)} 項不符配額。')
        return 1
    print('\n配額全部符合。')
    print('⚠️ 配額符合**不等於**畫面就有生命力——那要看成品，不是看宣告。')
    return 0

SELFTEST = [
    ('全部同一種（應該擋）',
     [(f'X-{i}', '姿勢：**C 靜止站定**｜相機：**2 他拍正面**｜視線：看鏡頭｜手在臉旁：**是**')
      for i in range(13)], True),
    ('達標的分布（應該過）',
     [('A1', '姿勢：**A 動作中**｜相機：**1 自拍**｜視線：看鏡頭｜手在臉旁：否'),
      ('A2', '姿勢：**D 非站坐**｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否'),
      ('A3', '姿勢：**A 動作中**｜相機：**6 框架物**｜視線：不看鏡頭｜手在臉旁：否'),
      ('A4', '姿勢：**D 非站坐**｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否'),
      ('A5', '姿勢：**B 支撐**｜相機：**4 過肩**｜視線：不看鏡頭｜手在臉旁：否'),
      ('A6', '姿勢：**A 動作中**｜相機：**4 背後**｜視線：不看鏡頭｜手在臉旁：否'),
      ('A7', '姿勢：**B 支撐**｜相機：**6 框架物**｜視線：不看鏡頭｜手在臉旁：**是**'),
      ('A8', '姿勢：**A 動作中**｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否'),
      ('A9', '姿勢：**C 靜止站定**｜相機：**1 自拍**｜視線：看鏡頭｜手在臉旁：否'),
      ('A10','姿勢：**A 動作中**｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否'),
      ('A11','姿勢：**D 非站坐**｜相機：**6 框架物**｜視線：不看鏡頭｜手在臉旁：否'),
      ('A12','姿勢：**C 靜止站定**｜相機：**6 框架物**｜視線：看鏡頭｜手在臉旁：**是**'),
      ('A13','姿勢：**B 支撐**｜相機：**3 他拍抓拍**｜視線：不看鏡頭｜手在臉旁：否')], False),
]

def selftest():
    ok = True
    for name, items, want_fail in SELFTEST:
        hard, _, _ = check(items)
        got = bool(hard)
        if got != want_fail: ok = False
        print(f"  {'✓' if got == want_fail else '✗'} {name:<18}{'擋下' if got else '通過'}")
    print('自檢：' + ('通過——會過也會擋' if ok else '**失敗**'))
    return 0 if ok else 1

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--selftest':
        sys.exit(selftest())
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1
                  else 'clients/sushisolar-rujiao/GENERATION_PLAN_B1.md'))
