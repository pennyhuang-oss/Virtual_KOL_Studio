#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
手部任務衝突檢查。

為什麼只做這兩條、不做更多：
2026-08-28 才因為「把競品的風格觀察當成普遍物理定律」寫出一組 21/21 全紅的檢查，
覆核指出紅燈本身會誘導過度修正。所以這支只檢查**在任何場景下都成立的算術事實**：
人有兩隻手。不檢查「應該怎麼寫比較好」。

檢 2 條：
  1. 硬衝突：同一件裡同時出現「雙手做 X」與「空著的手／另一手做 Y」——
     雙手都被佔用時不存在空手，這與場景無關。
  2. 任務數警告：跨列抽出的手部任務數 > 2 就列出來給人看。
     這條**只警告不擋**——同一隻手先後做兩件事在敘述上是合法的，
     機械檢查分不出「同時」與「先後」，那是語意問題。
"""
import re, sys, json

# 「雙手捧 X」＝兩隻手做同一件事，此時不存在空手。
# 「兩手都有事做」＝各做各的，後面接「另一手」是合法的指涉，不是衝突。
BOTH        = r'雙手|兩手|both hands'
BOTH_SPLIT  = r'(?:雙手|兩手)(?:都|各|分別)'
FREE  = r'空著的手|空手|另一手|另一隻手|free hand|free arm|other hand'
# 手部任務：動詞 + 受詞，抽得寬鬆，寧可多抓給人看
TASK  = r'(?:一手|另一手|左手|右手|雙手|空著的手|手指|指尖|手背|手肘)[^；。，、]{2,20}'

ROWS = ['表情', '肢體與重心']

# 註解與規格寫在同一個儲存格裡，是這份文件的結構問題。
# 註解常在複述**被否決的**寫法（「原本寫雙手捧杯…已改」），
# 直接掃全文會把被否決的寫法當成現行規格 —— 首版就因此誤報 LG-08、LG-10B。
ANNOT_MARK = r'原本|已刪|已改|已拿掉|修正|風險|那樣|不是已證實|沿用'

def strip_annotations(text):
    """去掉全形括號內容與整段註解，只留現行規格敘述。"""
    prev = None
    while prev != text:                      # 括號可能巢狀
        prev = text
        text = re.sub(r'（[^（）]*）', '', text)
    keep = [seg for seg in re.split(r'<br>', text)
            if not re.search(ANNOT_MARK, seg)]
    return ' '.join(keep)

def rows_of(body):
    return dict(re.findall(r'\| \*\*(.+?)\*\* \| (.+?) \|\n', body))

def check(name, r):
    text = strip_annotations(' '.join(r.get(f, '') for f in ROWS))
    hard, warn = [], []
    shared = re.search(BOTH, text) and not re.search(BOTH_SPLIT, text)
    if shared and re.search(FREE, text):
        hard.append('雙手佔用卻又出現「空著的手／另一手」')
    tasks = re.findall(TASK, text)
    # 去掉重複敘述（同一件事被增補寫了兩次）
    uniq = []
    for t in tasks:
        if not any(t[:6] == u[:6] for u in uniq):
            uniq.append(t)
    if len(uniq) > 2:
        warn.append(f'手部任務 {len(uniq)} 件：' + '／'.join(uniq))
    return hard, warn

def main(path):
    s = open(path).read()
    blocks = re.split(r'\n### ((?:YG|LG)-\d+[AB]?)｜', s)
    nh = nw = 0
    for i in range(1, len(blocks), 2):
        name, r = blocks[i], rows_of(blocks[i+1])
        hard, warn = check(name, r)
        if hard:
            nh += 1
            print(f'{name:<7} ✗ ' + '；'.join(hard))
        if warn:
            nw += 1
            print(f'{name:<7} ⚠ ' + '；'.join(warn))
        if not hard and not warn:
            print(f'{name:<7} ✓')
    print(f'\n硬衝突 {nh} 件，任務數警告 {nw} 件。')
    print('⚠️ 警告不等於錯——同一隻手先後做兩件事是合法敘述，需人工判讀。')
    return 1 if nh else 0

SELFTEST = [
    ('雙手＋空手（硬衝突）', {'肢體與重心': '雙手捧著蛋餅；手肘靠在桌上',
                       '表情': '空著的手對鏡頭比大拇指'}, True),
    ('一手一事（正常）',   {'肢體與重心': '一手搔貓頭；另一手撐在窗台', '表情': '瞇眼笑'}, False),
    ('雙手同事（正常）',   {'肢體與重心': '雙手捧著紙杯；一邊肩膀比另一邊低', '表情': '越過杯緣看鏡頭'}, False),
    # 以下兩例是本檢查器首版的誤報，固定下來防止回歸
    ('註解提到被否決的雙手寫法', {'肢體與重心': '一手拿毛巾擦頭髮；另一手扶著洗手台',
                       '表情': '單手拿小方巾按臉頰<br>（雙手同時靠近臉會增加手指重疊風險，所以維持一手一事分工）'}, False),
    ('兩手都有事做＋另一手',    {'肢體與重心': '站定，重心在一腳；兩手都有事做（舉糖、扶簪）',
                       '表情': '一手把蘋果糖舉在臉頰旁、另一手扶著髮簪'}, False),
]

def selftest():
    ok = True
    for label, r, want_hard in SELFTEST:
        hard, warn = check(label, r)
        got = bool(hard)
        mark = '✓' if got == want_hard else '✗'
        if got != want_hard: ok = False
        print(f'  {mark} {label:<16} hard={hard} warn={warn}')
    print('自檢：' + ('通過——會過也會擋' if ok else '**失敗**'))
    return 0 if ok else 1

if __name__ == '__main__':
    if len(sys.argv) > 1 and sys.argv[1] == '--selftest':
        sys.exit(selftest())
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1
                  else 'clients/sushisolar-rujiao/GENERATION_PLAN_B1.md'))
