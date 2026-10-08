#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
手部任務檢查（2026-08-29 依 R7 覆核重寫）。

舊版讀「表情」「肢體與重心」兩列，用字串啟發式猜手部任務。
它 12 件衝突只抓到 1 件，還誤報 2 件（註解在複述被否決的寫法）。
根因是**規格與註解混在同一個儲存格**，機械檢查分不出來。

R7 的解法不是把檢查器寫得更聰明，是**把手部任務獨立成一列**，
其他列不准再宣告手部任務。檢查器因此只做三件與場景無關的算術：

  1. 同一個凍結瞬間最多兩隻解剖學的手
     —— 拿手機自拍的那隻手雖然 off-frame，仍佔一隻
  2. 表情列與肢體列不得再出現手部任務（跨欄重複占用是最常漏的一種）
  3. 每隻手最多一個主要抓握／手勢任務

不檢查「應該怎麼寫比較好」——那是語意覆核的事。
"""
import re, sys

HAND_ROW = '手部任務'
CLEAN_ROWS = ['表情', '肢體與重心']

# 手部任務的字眼。手肘不是手；手機／手寫是物件與名詞，不是手。
HAND_WORD = r'(?<!手)(?:一手|另一手|雙手|兩手|左手|右手|手指|指尖|手背|手掌|空著的手)'
NOT_HAND  = ('手肘', '手機', '手寫', '手部')

def rows_of(body):
    return dict(re.findall(r'\| \*\*(.+?)\*\* \| (.+?) \|\n', body))

def count_hands(txt):
    """數這一列宣告了幾隻解剖學的手。N/A 不算。"""
    n = 0
    for seg in re.split(r'<br>', txt):
        if not re.search(r'(拍攝手|鏡外手|可見手)', seg):
            continue
        if re.search(r'\*\*N/A\*\*|：\s*N/A', seg):
            continue
        # 「可見手 A＋B：共同…」＝兩隻手做同一件事
        n += 2 if re.search(r'A ?＋ ?B|A\+B', seg) else 1
    return n

def count_tasks(txt):
    """數主要任務數（一段宣告＝一個任務，共同捧仍是一個任務）。"""
    return sum(1 for seg in re.split(r'<br>', txt)
               if re.search(r'(拍攝手|鏡外手|可見手)', seg)
               and not re.search(r'\*\*N/A\*\*|：\s*N/A', seg))

def check(name, r):
    hard, warn = [], []
    if HAND_ROW not in r:
        warn.append('尚未整併成有效規格（沒有手部任務列）')
        return hard, warn
    h = r[HAND_ROW]
    hands, tasks = count_hands(h), count_tasks(h)
    if hands > 2:
        hard.append(f'宣告了 {hands} 隻手——人只有兩隻')
    if tasks > hands:
        hard.append(f'{tasks} 個任務分給 {hands} 隻手')
    for rn in CLEAN_ROWS:
        txt = r.get(rn, '')
        for m in re.finditer(HAND_WORD, txt):
            around = txt[max(0, m.start()-2):m.end()+2]
            if any(w in around for w in NOT_HAND):
                continue
            hard.append(f'「{rn}」列又宣告了手部任務：{m.group(0)}')
            break
    return hard, warn

def main(path):
    s = open(path).read()
    blocks = re.split(r'\n### ((?:YG|LG)-\d+[AB]?)｜', s)
    nh = nw = 0
    for i in range(1, len(blocks), 2):
        name, r = blocks[i], rows_of(blocks[i+1])
        hard, warn = check(name, r)
        if hard:
            nh += 1; print(f'{name:<7} ✗ ' + '；'.join(hard))
        elif warn:
            nw += 1; print(f'{name:<7} ⚠ ' + '；'.join(warn))
        else:
            h = count_hands(r[HAND_ROW])
            print(f'{name:<7} ✓ {h} 隻手 / {count_tasks(r[HAND_ROW])} 個任務')
    print(f'\n硬衝突 {nh} 件，未整併 {nw} 件。')
    return 1 if nh else 0

SELFTEST = [
 ('自拍＋兩個可見任務＝三隻手', {
   HAND_ROW: '拍攝手／鏡外手：持手機自拍，**off-frame**<br>可見手 A：撥瀏海<br>可見手 B：勾著包帶'}, True),
 ('自拍＋一個可見任務', {
   HAND_ROW: '拍攝手／鏡外手：持手機自拍，**off-frame**<br>可見手 A：按住毛巾<br>可見手 B：**N/A**——兩隻手已用完'}, False),
 ('雙手共同一個任務', {
   HAND_ROW: '可見手 A＋B：**共同**捧住紙杯在下巴前（兩手一個任務）<br>無第三個手部任務'}, False),
 ('大特寫、完全沒有手', {
   HAND_ROW: '可見手 A：**N/A**（裁切外）<br>可見手 B：**N/A**（裁切外）'}, False),
 ('肢體列偷偷又指派了手', {
   HAND_ROW: '可見手 A：拿蛋餅<br>可見手 B：比大拇指',
   '肢體與重心': '雙手捧著蛋餅；手肘靠在桌上'}, True),
 ('手肘與手機不算手', {
   HAND_ROW: '可見手 A：滑手機<br>可見手 B：伸進零食袋',
   '肢體與重心': '手肘靠在桌上；上半身前傾', '表情': '看著手機笑'}, False),
]

def selftest():
    ok=True
    for label, r, want in SELFTEST:
        hard,_=check(label,r); got=bool(hard)
        if got!=want: ok=False
        print(f'  {"✓" if got==want else "✗"} {label:<22} hard={hard}')
    print('自檢：' + ('通過——會過也會擋' if ok else '**失敗**'))
    return 0 if ok else 1

if __name__ == '__main__':
    if len(sys.argv)>1 and sys.argv[1]=='--selftest':
        sys.exit(selftest())
    sys.exit(main(sys.argv[1] if len(sys.argv)>1
                  else 'clients/sushisolar-rujiao/GENERATION_PLAN_B1.md'))
