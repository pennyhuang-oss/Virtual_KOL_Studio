# M-4 R24：組裝 2 份 prompt（公開版以 <<<ANCHOR>>> 代替 Element ID）；用法：python3 assemble.py <工作資料夾> <element_id>
import json, hashlib, os, re, runpy, sys
D, EL = sys.argv[1], sys.argv[2]
sp = runpy.run_path(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'specs.py'))
items = []
for v in 'AB':
    s = sp['S'][v]
    pub = re.sub(r'\s+', ' ', ' '.join([sp['IDENT'], sp['WEAR'], sp['SETTING'], s['moment'], s['camera'], sp['LIGHT'], sp['END']])).strip()
    real = pub.replace(sp['ANCHOR'], f'<<<{EL}>>>')
    assert pub.count(sp['ANCHOR']) == 1 and real.count('<<<') == 1
    low = pub.lower()
    bad = ['selfie', 'mirror', 'phone', 'fills', 'filling', 'bottom edge', 'cm', 'f cup', 'bust 9', 'low angle', 'wide-angle', 'wide angle', 'eyes', 'gaze', 'photobook', 'unretouched']
    assert not [w for w in bad if w in low], (v, [w for w in bad if w in low])
    items.append({'set': 'V-rainie-hsu', 'v': v, 'month': 5, 'ratio': '3:4', 'model': 'seedream_v4_5', 'change': s['change'], 'note': sp['NOTE'],
                  'prompt_public': pub, 'prompt_sha256': hashlib.sha256(real.encode()).hexdigest(), 'words': len(real.split()), 'prompt': real})
json.dump(items, open(f'{D}/prompts.json', 'w'), ensure_ascii=False, indent=1)
for it in items:
    print(it['v'], it['words'], it['prompt_sha256'][:10]); print(it['prompt'])
