"""M-5 R27：12 人團體封面 4 份 prompt（H-A、H-B、V-A、V-B）、服裝分配、站位與身分對照。
輸出 docs/calendar/data/cal_m5_r27_prompts.json（全文與 sha256）與 cal_m5_r27_identity.json（角色—來源—畫面位置）；不含任何平台 ID。"""
import hashlib
import json
import os
import subprocess

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
REFS = json.load(open(os.path.join(ROOT, 'review', 'calendar', 'm5_r27', 'refs.json'), encoding='utf-8'))['refs']
MODEL = {'model': 'nano_banana_pro', 'resolution': '4k', 'aspect': {'H': '4:3', 'V': '3:4'}}

# 角色外觀（只寫髮型髮色與氣質，臉交給參考圖）
LOOK = {
    'yuna-kim': 'collarbone-length dark brown-black hair with soft airy waves; calm, cool, elegant expression; tall and slender',
    'rin-ayase': 'long deep wine-red hair in soft waves; mature, poised, gentle smile',
    'miu-shiraishi': 'platinum ash-blonde shoulder-length bob with airy see-through bangs; sweet, small and petite',
    'tammy-chou': 'long honey-caramel blonde hair in big airy waves with lighter face-framing pieces; chic and confident',
    'yerin-han': 'long straight flaxen-brown hair with blonde face-framing streaks; sporty, bright smile; the tallest of the group',
    'coco-wu': 'long dark brown curly waves with wispy bangs; bubbly, the widest smile; petite',
    'mia-huang': 'shoulder-length ash-brown loose waves with one pastel-pink face-framing streak; playful; petite',
    'iris-chen': 'long silky straight black hair worn down; round sweet face with a bright girl-next-door smile',
    'jia-seo': 'shoulder-length straight blue-black hair with a mint-green inner layer showing at the ends; cool and composed',
    'luna-tanaka': 'chin-length straight black bob with blunt bangs; gentle and quiet; the smallest of the group',
    'somi-oh': 'bright copper-orange layered wolf-cut hair; cheerful, open laugh',
    'rainie-hsu': 'very long glossy jet-black straight hair with a deep side part; glamorous, defined makeup; hourglass figure',
}
# 服裝：同色系（象牙白、奶油白、香檳、燕麥）、同系列不同剪裁；依角色個性分配
WEAR = {
    'A': {
        'yuna-kim': 'an ivory tailored blazer and matching wide-leg trousers over a cream silk camisole',
        'rin-ayase': 'a champagne satin bias-cut slip midi dress with a soft cowl neckline',
        'miu-shiraishi': 'a cream puff-sleeve mini dress with a square neckline',
        'tammy-chou': 'an oat-beige one-shoulder satin midi dress',
        'yerin-han': 'an ivory sleeveless fine-knit top tucked into cream high-waisted wide trousers',
        'coco-wu': 'a champagne satin slip mini dress with a cropped cream cardigan',
        'mia-huang': 'an ivory fitted knit top with an oat pleated mini skirt',
        'iris-chen': 'a cream off-shoulder fine-knit top with a champagne satin midi skirt',
        'jia-seo': 'an oat cropped blazer with matching straight trousers over an ivory bandeau top',
        'luna-tanaka': 'an ivory lace short-sleeve blouse with a cream pleated midi skirt',
        'somi-oh': 'an oat cropped jacket with a matching mini skirt over a cream top',
        'rainie-hsu': 'a champagne satin strapless fitted maxi dress with a side slit',
    },
    'B': {
        'yuna-kim': 'an ivory silk shirt dress with a slim belt',
        'rin-ayase': 'a champagne satin one-shoulder midi dress',
        'miu-shiraishi': 'a cream satin babydoll mini dress',
        'tammy-chou': 'an oat satin wrap midi dress',
        'yerin-han': 'an ivory satin halter top with cream wide-leg trousers',
        'coco-wu': 'a champagne satin slip mini dress with fine straps',
        'mia-huang': 'a cream fitted knit mini dress with short puff sleeves',
        'iris-chen': 'a champagne satin square-neck midi dress',
        'jia-seo': 'an ivory satin blazer dress',
        'luna-tanaka': 'a cream chiffon blouse with a champagne satin midi skirt',
        'somi-oh': 'an oat satin camisole with a matching midi skirt',
        'rainie-hsu': 'a champagne satin cowl-neck slip maxi dress with a side slit',
    },
}
SET = {
    'H-A': ('A bright ivory photo studio: a seamless warm-white backdrop curving into the floor, one long low cream plinth platform about '
            '40 cm high, one low cream ottoman and one rounded cream lounge chair, all in one continuous space. Soft diffused daylight from a '
            'large window-like source on the left, gentle fill, soft natural shadows on the floor. Clean and airy; no props other than this furniture.'),
    'V-A': ('A bright ivory photo studio: a seamless warm-white backdrop curving into the floor, a wide low cream riser step at the back, '
            'a long cream boucle bench in the middle and one low cream ottoman in front, all in one continuous space. Soft diffused daylight '
            'from a large window-like source on the left, gentle fill, soft natural shadows on the floor. Clean and airy; no props other than this furniture.'),
    'B': ('A calm, warm, minimalist living room in early evening: warm white walls, a long curved cream sofa, a cream rug, a low travertine '
          'coffee table with a few champagne glasses and one small bowl of fruit, a warm table lamp and a floor lamp, soft dusk light from a '
          'window. Uncluttered: no balloons, banners, confetti, flower walls or party decorations, nothing written anywhere.'),
}
MOOD = {
    'A': 'The feeling is a relaxed annual editorial group portrait: friends at ease, a few soft laughs, most of them looking toward the camera.',
    'B': ('The feeling is a natural reunion moment captured for an annual magazine issue, not an event snapshot: a light toast, laughter, '
          'leaning on a shoulder, most faces toward the camera, two or three glancing at each other.'),
}
# 站位（橫式由左到右展開；直式前後高低）
POS = {
    'H-A': [
        ('yerin-han', 'far left, standing, one hand loosely in her trouser pocket'),
        ('tammy-chou', 'seated sideways on the left end of the low plinth, legs crossed'),
        ('rin-ayase', 'standing just behind Tammy, one hand resting lightly on Tammy\'s shoulder'),
        ('miu-shiraishi', 'sitting on the floor in front of the plinth, legs folded to one side, leaning toward Tammy'),
        ('yuna-kim', 'standing left of center, slightly behind the plinth'),
        ('iris-chen', 'seated in the middle of the plinth, hands on her knees, smiling'),
        ('luna-tanaka', 'sitting on a low cream ottoman in front, just right of center'),
        ('jia-seo', 'standing right of center behind the plinth, one hand on her hip'),
        ('somi-oh', 'perched on the right end of the plinth, laughing toward Coco'),
        ('coco-wu', 'sitting in a rounded cream lounge chair on the right'),
        ('mia-huang', 'sitting on the floor in front of Coco\'s chair, legs to the side'),
        ('rainie-hsu', 'far right, standing and leaning one hand on the arm of Coco\'s chair'),
    ],
    'V-A': [
        ('rin-ayase', 'back row on a low riser, left, standing'),
        ('yerin-han', 'back row on the riser, center-left, standing, tallest'),
        ('jia-seo', 'back row on the riser, center-right, standing'),
        ('rainie-hsu', 'back row, right, sitting on the edge of the riser with one leg extended'),
        ('tammy-chou', 'middle, seated on the left end of a long cream bench'),
        ('yuna-kim', 'middle, seated on the bench left of center, legs crossed'),
        ('iris-chen', 'middle, seated on the bench right of center, smiling'),
        ('somi-oh', 'middle, seated on the right end of the bench, turning toward Iris and laughing'),
        ('miu-shiraishi', 'front, left, sitting on the floor with her legs folded to the side'),
        ('luna-tanaka', 'front, center-left, sitting on a low cream ottoman'),
        ('coco-wu', 'front, center-right, sitting on the floor with her knees drawn up'),
        ('mia-huang', 'front, right, sitting on the floor and leaning against Coco\'s shoulder'),
    ],
    'H-B': [
        ('rainie-hsu', 'far left, standing beside the floor lamp, holding a champagne glass'),
        ('jia-seo', 'sitting on the left arm of the sofa, turned toward Rainie'),
        ('tammy-chou', 'sitting on the left end of the sofa, legs crossed'),
        ('mia-huang', 'sitting on the rug in front of Tammy, leaning back against the sofa'),
        ('yuna-kim', 'standing behind the sofa left of center, one hand on the sofa back'),
        ('iris-chen', 'sitting in the middle of the sofa, laughing'),
        ('rin-ayase', 'standing behind the sofa right of center, raising her glass slightly'),
        ('coco-wu', 'sitting on the sofa next to Iris, leaning her head toward Iris'),
        ('luna-tanaka', 'sitting on the rug in front, right of center, holding a glass with both hands'),
        ('somi-oh', 'sitting on the right part of the sofa, mid-laugh'),
        ('miu-shiraishi', 'perched on the right arm of the sofa'),
        ('yerin-han', 'far right, standing, one shoulder leaning on the wall'),
    ],
    'V-B': [
        ('yerin-han', 'back, standing behind the sofa on the left'),
        ('rin-ayase', 'back, standing behind the sofa left of center, holding a glass'),
        ('yuna-kim', 'back, standing behind the sofa right of center'),
        ('rainie-hsu', 'back, standing behind the sofa on the right, one hand on the sofa back'),
        ('jia-seo', 'middle, perched on the left arm of the sofa'),
        ('tammy-chou', 'middle, sitting on the left part of the sofa'),
        ('iris-chen', 'middle, sitting in the center of the sofa, smiling'),
        ('somi-oh', 'middle, sitting on the right part of the sofa, laughing'),
        ('miu-shiraishi', 'middle, perched on the right arm of the sofa'),
        ('luna-tanaka', 'front, left, sitting on the rug with her legs folded to the side'),
        ('coco-wu', 'front, center, sitting on the rug, laughing'),
        ('mia-huang', 'front, right, sitting on the rug, leaning toward Coco'),
    ],
}
FRAME = {
    'H': ('Horizontal 4:3 frame. The group spreads from left to right across the whole width in a relaxed, staggered arrangement at '
          'different heights (standing, perched, seated, on the floor), not in rigid rows and not a graduation photo. Keep the top 22% of '
          'the frame as clean empty background with no heads or hands in it (reserved for a title added later). Keep every person at least '
          '4% away from the left and right edges. Full-length figures on one shared floor.'),
    'V': ('Vertical 3:4 frame composed for a portrait cover (not a crop of a horizontal photo). Build depth: a back group, a middle group '
          'and a front group at clearly different heights, staggered and slightly overlapping, never three straight rows. Keep the top 22% of '
          'the frame as clean empty background with no heads or hands in it (reserved for a title added later). Keep all people inside the '
          'central 86% of the width (at least 7% empty margin on the left and on the right). Full-length figures on one shared floor.'),
}


def prompt(cover):
    book, look = cover.split('-')
    names = {r['set']: (r['image_no'], r['name'].split()[0]) for r in REFS}
    L = ['One single photograph: a premium magazine-cover group portrait of exactly twelve young women together in one room, taken in one '
         'moment by one camera. It is not a collage, not a grid and not separate photos combined.', '',
         'Identity references: the twelve attached images are, in order, ' +
         '; '.join(f'Image {r["image_no"]} = {r["name"].split()[0]}' for r in REFS) + '. '
         'Use each image only for that one woman\'s face, facial features, skin tone, hair color and hairstyle. Do not copy clothing, '
         'background, pose, props, lighting or camera angle from any reference image. Every woman appears exactly once. Exactly twelve '
         'people in the photograph: no extra people, no duplicates, no missing person, no reflections, posters or photos of people. Each '
         'face stays distinct and matches only its own reference; do not blend faces and do not give two women the same face.', '',
         'The women (hair and personality):']
    for r in REFS:
        L.append(f'- {r["name"].split()[0]} (Image {r["image_no"]}): {LOOK[r["set"]]}.')
    L += ['', f'Wardrobe: one coordinated collection in ivory, cream, champagne and oat tones, same series with different cuts; nude or '
              f'cream shoes; minimal fine gold jewelry. ' + ' '.join(f'{names[s][1]} wears {w}.' for s, w in WEAR[look].items()), '',
          f'Setting: {SET.get(cover, SET.get(look))}', '', f'Arrangement ({"left to right" if book == "H" else "back, middle and front"}):']
    for s, where in POS[cover]:
        n, nm = names[s]
        L.append(f'- {nm} (Image {n}): {where}.')
    L += ['', FRAME[book], '',
          MOOD[look] + ' Every face is clearly visible and in focus; no face hidden, turned away or covered by hands, hair or glasses.', '',
          'Photography: medium-format camera at chest height from about six meters, 50mm-equivalent lens, f/8 so all twelve faces are '
          'sharp, no wide-angle distortion. One shared light and perspective for everyone; consistent shadows on the floor. Natural adult '
          'proportions, realistic hands with five fingers, believable overlaps and touch (a hand on a shoulder, leaning together), no merged '
          'or extra limbs. Natural skin texture, true-to-life color, refined editorial finish.', '',
          'No text, letters, numbers, logos, watermarks or magazine masthead anywhere in the image.']
    return '\n'.join(L)


def main():
    covers = {}
    for c in ('H-A', 'H-B', 'V-A', 'V-B'):
        assert sorted(s for s, _ in POS[c]) == sorted(r['set'] for r in REFS), c   # 12 人各一次
        p = prompt(c)
        covers[c] = {'book': c[0], 'direction': c[2], 'aspect_ratio': MODEL['aspect'][c[0]], 'resolution': MODEL['resolution'],
                     'prompt': p, 'prompt_sha256': hashlib.sha256(p.encode()).hexdigest(), 'chars': len(p)}
    out = {'note': 'M-5 R27 封面 prompt 全文（每張最多 1 次請求）。身分參考依 Image 1–12 順序送入；不含平台 ID。', 'round': 'M-5 R27',
           'model': MODEL['model'], 'references_in_order': [{k: r[k] for k in ('image_no', 'set', 'name', 'file', 'sha256')} for r in REFS],
           'covers': covers}
    json.dump(out, open(os.path.join(ROOT, 'docs', 'calendar', 'data', 'cal_m5_r27_prompts.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    ident = {'note': '12 人封面身分對照：角色—身分來源—每張封面的畫面位置。來源只裁切頭肩、不修圖；月面照片未當成臉部參考。', 'round': 'M-5 R27',
             'rows': [{**{k: r[k] for k in ('image_no', 'set', 'name', 'source', 'source_sha256', 'why', 'crop_box_px', 'file', 'sha256')},
                       'look': LOOK[r['set']], 'wear': {k: WEAR[k][r['set']] for k in 'AB'},
                       'position': {c: next(w for s, w in POS[c] if s == r['set']) for c in POS}} for r in REFS]}
    json.dump(ident, open(os.path.join(ROOT, 'docs', 'calendar', 'data', 'cal_m5_r27_identity.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    for c, v in covers.items():
        print(c, v['chars'], v['prompt_sha256'][:12])


if __name__ == '__main__':
    main()
