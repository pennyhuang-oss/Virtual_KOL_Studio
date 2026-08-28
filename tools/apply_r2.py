#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""套用 ChatGPT R2（review/REVIEW_BATCH3_FACES_R2.md §7）裁決中可以機械執行的部分。

**刻意不做的事**：不把新的參考來源直接覆蓋進 refs。
ChatGPT 明說「改來源後不能只換陣列：ARCHETYPE、AXES、FACE_EN、MARKERS、WHY_DISTINCT
都必須依新來源同步重建」，而重建需要它對那些照片的骨相判讀。
所以新來源存成 refs_v2 並標記 needs_rebuild，等 R3 的重建文字到位才合併——
否則會出現「文字描述的是舊照片、附圖卻是新照片」的靜默不一致。
"""
import json, re

F = 'pilot/batch3_faces_v2.json'
D = json.load(open(F, encoding='utf-8'))
P = D['personas']

NEWSHAPE = dict(zip(
 ['angel-chiu','tammy-chou','emma-kao','zoey-yeh','miu-shiraishi','rin-ayase','nanami-fujiwara',
  'kanon-komori','jia-seo','yerin-han','somi-oh','zhiyi-shen','wanyin-jiang','ruoruo-tang',
  'cheryl-soh','wendy-yeo','peggy-lee','sydney-leong','angeline-kwee'],
 ['ref_15','ref_08','ref_11','ref_04','ref_05','ref_07','ref_03','ref_04','ref_02','ref_12',
  'ref_05','ref_09','ref_01','ref_10','ref_15','ref_11','ref_14','ref_06','ref_02']))
NEWNOSE = {'rin-ayase':'ref_14','yerin-han':'ref_03','ruoruo-tang':'ref_14',
           'cheryl-soh':'ref_06','peggy-lee':'ref_11'}

# F-01：ChatGPT 指定的確切措辭。它不同意我提的 first/second/third/fourth，
# 理由是 Image 1..4 更短、更接近多圖模型的索引語法。照它的字。
ASSIGN = ("Using the four attached reference images in input order: Image 1 defines the face shape "
          "and jawline; Image 2 defines the eyes and brows; Image 3 defines the nose; Image 4 "
          "defines the mouth. Combine these four assigned components into one coherent new identity.")
OLD_RE = re.compile(r'Reference assignment: FACE_SHAPE_AND_JAW from ref_\d+; EYES_AND_BROWS from '
                    r'ref_\d+; NOSE from ref_\d+; MOUTH from ref_\d+\.')

n_txt = 0
for pid, d in P.items():
    new, k = OLD_RE.subn(ASSIGN, d['face_en'])
    if k != 1:
        raise SystemExit(f'{pid}：找不到（或找到多個）參考圖指派句，不能盲改')
    d['face_en_v1_filename_form'] = d['face_en']
    d['face_en'] = new
    n_txt += 1

    v2 = dict(d['refs'])
    v2['FACE_SHAPE_AND_JAW'] = NEWSHAPE[pid]
    if pid in NEWNOSE:
        v2['NOSE'] = NEWNOSE[pid]
    d['refs_v2'] = v2
    changed = {k2: (d['refs'][k2], v) for k2, v in v2.items() if d['refs'][k2] != v}
    d['needs_rebuild'] = changed or None

D['_r2'] = {
  '_source': 'ChatGPT 於 review/REVIEW_BATCH3_FACES_R2.md §7 的裁決（commit 55d6b3e）。四項全部同意。',
  'F-01': {'狀態': '已套用',
    '措辭': 'ChatGPT 指定 Image 1..4，不採用我提的 first/second/third/fourth。',
    '附圖順序': ['FACE_SHAPE_AND_JAW', 'EYES_AND_BROWS', 'NOSE', 'MOUTH'],
    'manifest': '送出前必須寫入 persona-id、四個槽位、實際路徑、陣列索引；順序不符 HARD FAIL。',
    '備案': '若第一批逐張核對顯示分工穩定成立的部件低於 3/4，停止全臉多圖法，'
            '改用部件裁切輸入（Image 1 標準化輪廓／顎線裁切、Image 2 只留眼眉、Image 3 只留鼻、Image 4 只留口）；'
            '再失敗才改兩階段生成／局部編修，不得直接展開 19 位。'},
  'F-02': {'狀態': '來源已存為 refs_v2，尚未合併',
    '規則': '臉型來源上限 2 位、鼻子來源上限 3 位、每位四槽必須四張不同圖。',
    '待補': '8 位的來源改變，其 ARCHETYPE／AXES／FACE_EN／MARKERS／WHY_DISTINCT 需依新來源重建（R3）。',
    '補圖': 'ChatGPT 不同意把補圖列為生成前條件。若第一批仍聚類，再補 6–8 張中性正面、'
            '眼平、均勻光、低妝、無廣角變形的照片，優先補寬方顎／U 梨形／長臉鈍下巴／窄眼單眼皮各 2 張。'},
  'F-03': {'狀態': 'gate 已實作，尚有配對未過',
    'gate': ['任兩人 11 軸至少相異 6 條',
             '六條主導軸（輪廓原型／臉長寬比／三庭配置／骨肉量／顎頦／眼眶結構）至少相異 2 條',
             '若兩人共用同一張 FACE_SHAPE_AND_JAW：總相異至少 7 條、主導軸至少 3 條'],
    '原規則': '原本的粗分群 gate 是設計錯誤（key 定得太細，19 人落 19 群，永遠沒有比較對象），作廢。'},
  'F-04': {'狀態': '已套用',
    '第一批': ['kanon-komori','wendy-yeo','angeline-kwee','miu-shiraishi',
               'tammy-chou','sydney-leong','yerin-han','peggy-lee'],
    '_why': '8 位涵蓋短／長臉、方／窄顎等極端，並包含原本只差 4 條的三組完整配對'
            '（Miu–Sydney、Tammy–Sydney、Yerin–Peggy）。每位 4 個候選共 32 張。',
    '_gate': '8 位全部通過部件執行檢查、MARKERS、全配對 gate 與去髮妝盲測，才展開其餘 11 位。'
             '若容易組通過、任一困難組失敗，結論是方法尚未成立，不得只核可容易組後繼續生成。'},
  '_age_truth': 'fixed 是年齡與族裔的唯一真理來源。FACE_EN 暫時保留完整句，'
                'validator 必須逐字核對兩者一致；未來 fixed 改動應由編譯器重建 prompt 或 HARD FAIL。',
}
D['batch1'] = D['_r2']['F-04']['第一批']

json.dump(D, open(F, 'w', encoding='utf-8'), ensure_ascii=False, indent=2)
need = [p for p, d in P.items() if d.get('needs_rebuild')]
print(f'✓ FACE_EN 參考指派句改寫 {n_txt}/19')
print(f'✓ refs_v2 已寫入；其中 {len(need)} 位來源改變、文字待 R3 重建：{need}')
print(f'✓ 第一批設為 {len(D["batch1"])} 位')
