# M-4 R21：由 specs.py＋base.json（R20 身分段落）組裝 20 份 prompt，寫 prompts.json
import json, hashlib, re, runpy, sys
D = sys.argv[1]
sp = runpy.run_path(f'{D}/specs.py')
S, END, ORDER = sp['S'], sp['END'], sp['ORDER']
base = json.load(open(f'{D}/base.json'))
order = ['H-rin-ayase', 'H-miu-shiraishi', 'H-tammy-chou', 'H-yerin-han', 'H-mia-huang', 'H-luna-tanaka', 'H-somi-oh', 'V-jia-seo', 'V-rainie-hsu', 'V-yuna-kim']
items = []
for sid in order:
    s, b = S[sid], base[sid]
    for v in 'AB':
        f = {k: s[k] for k in ORDER if k in s}
        f.update({k: x for k, x in s[v].items() if k in ORDER or k == 'moment'})
        assert all(k in f for k in ORDER + ['moment']), (sid, v)
        p = re.sub(r'\s+', ' ', ' '.join([b['identity'] + s.get('identity_add', ''), f['wear'], f['setting'], f['moment'], f['shot'], f['camera'], f['comp'], f['light'], END])).strip()
        assert ('horizontal 16:9' if b['ratio'] == '16:9' else 'vertical 3:4') in f['camera']
        items.append({'set': sid, 'v': v, 'pid': b['pid'], 'month': b['month'], 'ratio': b['ratio'], 'soul_id': b['soul_id'], 'change': s[v]['change'], 'note': s['note'],
                      'prompt': p, 'sha256': hashlib.sha256(p.encode()).hexdigest(), 'words': len(p.split())})
bad = ['photobook', 'unretouched', 'softbox', 'reflector', '%', 'fills about', 'editorial', 'emphasis', 'unposed', 'string of warm bulbs', 'golf club', 'clubs', 'fried chicken', 'greenhouse']
for it in items:
    hits = [w for w in bad if w in it['prompt'].lower()]
    assert not hits, (it['set'], it['v'], hits)
json.dump(items, open(f'{D}/prompts.json', 'w'), ensure_ascii=False, indent=1)
for i, it in enumerate(items):
    print(i, it['set'], it['v'], it['words'], it['sha256'][:10])
