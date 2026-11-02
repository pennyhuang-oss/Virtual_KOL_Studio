"""M-5 R31：企劃狀態同步（人物封面停止；改做非人物封面 4 張候選，待 Penny 選擇）。只改下列欄位，並把差異記在 m5r31.changes。"""
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
p = os.path.join(ROOT, 'docs/calendar/data/cal_m3_shoot_plan.json')
P = json.load(open(p, encoding='utf-8'))
assert 'm5r31' not in P, '已同步過'
pr = P['status']['production']
changes = []


def chg(where, old, new):
    changes.append({'kind': '事實同步', 'where': where, 'old': json.dumps(old, ensure_ascii=False) if not isinstance(old, str) else old,
                    'new': json.dumps(new, ensure_ascii=False) if not isinstance(new, str) else new})


assert pr['cover'] == 'r30_single_fix_owner_check' and pr['cover_edit_log'] == {'M-5 R28': 1} and pr['generated_cumulative'] == 85
chg('status.production.cover', pr['cover'], 'r31_non_person_candidates')
pr['cover'] = 'r31_non_person_candidates'
assert 'cover_person_track' not in pr
pr['cover_person_track'] = 'stopped'
chg('status.production.cover_person_track', '（無）', 'stopped')
D = pr['definitions']
for k, v in (
        ('cover', '封面狀態；M-5 R28–R30 的人物團體封面與 Coco 單人校正 Owner 均未接受；M-5 R31 起 r31_non_person_candidates＝非人物封面 4 張候選'
                  '（橫式、直式各 A 四季光影／B 極簡典藏）已放上網站，等 Penny 選擇；候選不等於接受或交印核准'),
        ('cover_person_track', '人物封面路線；M-5 R31 Owner 表示「全部都不像本人」後停止（不再修臉、不換模型試拍、不追加人物生成），歷史紀錄保留')):
    old = D.get(k, '（無）')
    D[k] = v
    chg(f'status.production.definitions.{k}', old, v)
P['m5r31'] = {
    'from_commit': 'f82eee4d467ffd9eba2ed5a1a6d819eaea0b839a',
    'owner': 'docs/calendar/data/cal_m5_owner_r31.json',
    'covers': 'docs/calendar/data/cal_m5_cover_r31.json',
    'trial': 'docs/calendar/data/cal_m5_r31_trial.json',
    'page': 'docs/calendar/data/cal_cover_r31_page.json',
    'source': 'docs/calendar/cover_r31/',
    'status_line': 'M-5 R31：Owner 表示人物封面「全部都不像本人」，人物團體封面與 Coco 單人校正均未接受，人物封面停止（紀錄保留）。'
                   '改做非人物封面：橫式、直式各 A｜四季光影、B｜極簡典藏共 4 張（原創向量、漸層、光影與字體排版；生成 0、付費 0、未購買素材；字型為 SIL OFL 並嵌入）。'
                   '另出兩份完整預覽 PDF（封面 A、B＋已接受內頁），R26 正式預覽不覆蓋。待 Penny 選 A／B 或寫修改；24 張月面照片與兩款內頁排版維持定案。',
    'changes': changes,
}
with open(p, 'w', encoding='utf-8') as f:
    json.dump(P, f, ensure_ascii=False, indent=1)
    f.write('\n')
print(len(changes), 'changes')
