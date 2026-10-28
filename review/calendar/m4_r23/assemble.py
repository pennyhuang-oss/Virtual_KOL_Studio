# M-4 R23：由 specs.py＋base.json（R20–R22 V-Rainie 身分段落）組裝 2 份 prompt，寫 prompts.json
# 用法：python3 assemble.py <工作資料夾>（資料夾內需有 base.json；specs.py 取本檔同層）
import json, hashlib, os, re, runpy, sys
D = sys.argv[1]
sp = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'specs.py'))
S, END, ORDER = sp['S'], sp['END'], sp['ORDER']
base = json.load(open(f'{D}/base.json'))
items = []
for sid in ['V-rainie-hsu']:
    s, b = S[sid], base[sid]
    for v in 'AB':
        f = {k: s[k] for k in ORDER if k in s}
        f.update({k: x for k, x in s[v].items() if k in ORDER or k == 'moment'})
        assert all(k in f for k in ORDER + ['moment']), (sid, v)
        p = re.sub(r'\s+', ' ', ' '.join([b['identity'], f['wear'], f['setting'], f['moment'], f['shot'], f['camera'], f['comp'], f['light'], END])).strip()
        assert 'vertical 3:4' in f['camera'] and p.count('looking into the camera') == 1 and 'gaze' not in p and 'eyes' not in p
        items.append({'set': sid, 'v': v, 'pid': b['pid'], 'month': b['month'], 'ratio': b['ratio'], 'soul_id': b['soul_id'], 'change': s[v]['change'], 'note': s['note'],
                      'prompt': p, 'sha256': hashlib.sha256(p.encode()).hexdigest(), 'words': len(p.split())})
bad = ['photobook', 'unretouched', 'softbox', 'reflector', '%', 'fills about', 'editorial', 'emphasis', 'unposed',
       'night', 'rain', 'leather', 'street light', 'shop window', 'low angle', 'wide-angle', 'wide angle', 'tilted', 'turns her head', 'toward the distant', 'lens', 'mirror']
for it in items:
    hits = [w for w in bad if w in it['prompt'].lower().replace('85mm lens', '')]
    assert not hits, (it['set'], it['v'], hits)
json.dump(items, open(f'{D}/prompts.json', 'w'), ensure_ascii=False, indent=1)
for i, it in enumerate(items):
    print(i, it['set'], it['v'], it['words'], it['sha256'][:10])
    print(it['prompt'])
