#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""驗證裁切 manifest，並執行「prompt 只能引用通過 QA 的 crop」這道 gate。

ChatGPT R5 J-02.4：prompt manifest 只能引用通過 QA 的 crop hash。
這支程式就是那道閘門——生成前跑，不過就不准送。
"""
import json, os, sys, hashlib

SPEC = json.load(open('pilot/crop_spec.json', encoding='utf-8'))
V = SPEC['crop_spec_version']
MAN = 'pilot/face_crops_manifest.json'
D = json.load(open('pilot/batch3_faces_v2.json', encoding='utf-8'))


def sha256(p):
    h = hashlib.sha256()
    with open(p, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def main():
    err, warn = [], []
    if not os.path.exists(MAN):
        sys.exit('✗ 還沒有 manifest，先跑 tools/build_face_crops.py')
    m = json.load(open(MAN, encoding='utf-8'))
    if m.get('crop_spec_version') != V:
        err.append(f"manifest 是 {m.get('crop_spec_version')}，spec 已經是 {V}——要重跑 builder")
    A = m['artifacts']

    # 1. 每一件的檔案與雜湊
    for k, a in A.items():
        for f, h in (('out_path', 'out_sha256'), ('source_path', 'source_sha256')):
            if not os.path.exists(a[f]):
                err.append(f'{k}: {a[f]} 不存在'); continue
            if sha256(a[f]) != a[h]:
                err.append(f'{k}: {a[f]} 的雜湊與 manifest 不符（檔案被改過或重生成過）')
        if a['crop_spec_version'] != V:
            err.append(f'{k}: crop_spec_version 是 {a["crop_spec_version"]}')
        if a['qa_status'] == 'pass' and a['qa_reasons']:
            err.append(f'{k}: 標 pass 卻有 QA 理由')
        if a['qa_status'] not in ('pass', 'fail', 'manual_pass'):
            err.append(f'{k}: 未知的 qa_status {a["qa_status"]}')

    # 2. gate：目前分配用到的每個 (ref, slot) 都必須有通過 QA 的 crop
    need = {}
    for pid, d in D['personas'].items():
        r = d.get('refs_v2') or d['refs']
        for slot, ref in r.items():
            need.setdefault((ref, slot), []).append(pid)
    missing, failing = [], []
    for (ref, slot), who in sorted(need.items()):
        k = f'{ref}__{slot}__{V}'
        if k not in A:
            missing.append((k, who))
        elif A[k]['qa_status'] == 'fail':
            failing.append((k, who, A[k]['qa_reasons']))

    print(f'裁切 manifest 檢查（spec {V}）')
    print(f'  manifest {len(A)} 件，qa pass {sum(1 for a in A.values() if a["qa_status"] in ("pass","manual_pass"))}')
    print(f'  目前分配用到 {len(need)} 個 (來源, 槽位) 組合')
    if missing:
        print(f'\n  尚未產生 {len(missing)} 個：')
        for k, who in missing:
            print(f'    · {k}  ← {"、".join(who)}')
    if failing:
        print(f'\n  QA 未通過 {len(failing)} 個（這些角色不得送生成）：')
        for k, who, rs in failing:
            print(f'    ✗ {k}  ← {"、".join(who)}')
            for r in rs:
                print(f'        {r}')
    for e in err:
        print('  ✗ ', e)
    if err or missing or failing:
        print(f'\nHARD FAIL：manifest 問題 {len(err)}、缺件 {len(missing)}、QA 未過 {len(failing)}。')
        print('gate 規則（ChatGPT J-02.4）：prompt 只能引用通過 QA 的 crop hash。')
        sys.exit(1)
    print('  ✓ 全部通過，可以送生成')


if __name__ == '__main__':
    main()
