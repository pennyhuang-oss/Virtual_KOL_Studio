"""M-5 R32：企劃狀態同步（Owner 選 R31 A 四季光影；本輪橫式淺色、直式深色各 2 個品牌版候選，待 Penny 選擇）。只改下列欄位，並把差異記在 m5r32.changes。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
p = os.path.join(ROOT, 'docs/calendar/data/cal_m3_shoot_plan.json')
P = json.load(open(p, encoding='utf-8'))
assert 'm5r32' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['cover'] == 'r31_non_person_candidates' and pr['cover_person_track'] == 'stopped'
chg('status.production.cover', pr['cover'], 'r32_seasons_brand_candidates')
pr['cover'] = 'r32_seasons_brand_candidates'
D = pr['definitions']
v = ('封面狀態；M-5 R28–R30 人物封面 Owner 未接受；M-5 R31 非人物候選中 Owner 選 A 四季光影；M-5 R32 起 r32_seasons_brand_candidates＝'
     '橫式淺色、直式深色各 2 個加入兌心科技品牌的版本已放上網站，等 Penny 選擇；候選不等於接受或交印核准')
chg('status.production.definitions.cover', D['cover'], v)
D['cover'] = v
P['m5r32'] = {
    'from_commit': '895ba18bb4a3078d53755b39e40d5c43c067f60e',
    'owner': 'docs/calendar/data/cal_m5_owner_r32.json',
    'design': 'docs/calendar/data/cal_m5_r32_design.json',
    'covers': 'docs/calendar/data/cal_m5_cover_r32.json',
    'page': 'docs/calendar/data/cal_cover_r32_page.json',
    'source': 'docs/calendar/cover_r32/',
    'status_line': 'M-5 R32：Owner 決定橫式、直式都用 R31 A 四季光影，橫式淺色、直式深色（近黑深藍底、局部光影），並加入兌心科技 Logo 與「兌心科技 Insight Software」，品牌主色為藍。'
                   '本輪做出橫式淺色、直式深色各 2 個版本（同一背景，只差年份與品牌區編排）；Logo 取自官網向量，深色版白色 Logo 為待確認的衍生版。'
                   '每張候選一份完整預覽 PDF（橫式 28 面、直式 32 面）。生成 0、付費 0；待 Penny 選擇；24 張照片與內頁排版不改。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
