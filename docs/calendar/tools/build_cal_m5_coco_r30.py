"""TASK-CAL-001 M-5 R30：把 R28 回填範圍裡誤改的其他人與背景還原成 R27 原圖（免費、不生成、不上傳）。從 R29 結果另存，不覆蓋 R27／R28／R29。

- 起點：build_cal_m5_coco_r29 重建的 R29 無損結果（R27 原圖＋R28 編輯結果＋R29 膚色修正，sha256 與遮罩皆核對）。
- 人物歸屬：R28 的 3 塊回填多邊形裡，除了 Coco 還有 Somi 的左袖、Rainie 的手臂、Mia 的腳背與鞋、牆、椅子、地板。
  用 mediapipe 分割（頭髮／臉／皮膚／衣服）加上人工範圍（review/calendar/m5_r30/zones.json：鄰人位置、分割漏掉的鞋與裙擺）
  分別算出 R27 舊 Coco 與目前新 Coco 的範圍；兩者聯集＝Coco 實際編輯範圍。遮罩存成 PNG（review/calendar/m5_r30/masks/），之後建置只讀檔。
- 還原：Coco 實際編輯範圍外（離聯集超過 R_OUT px）一律直接用 R27 原圖像素；聯集外 R_IN～R_OUT px 是過渡帶。
  舊 Coco 有、新 Coco 沒有的地方（R27 捲髮原本蓋住、換髮後露出的牆、Somi 袖子、Rainie 手臂）R27 裡沒有可還原的內容，
  只能用編輯結果；把它的低頻色偏對齊到旁邊已還原的 R27 同類內容（牆對牆、皮膚對皮膚、衣服對衣服），避免舊捲髮輪廓留下接縫。
- 一併補齊 R29 的漏調：R29 小腿下段的修正矩形右緣切在腳踝中間（x＝4078），右側一條沒調到、有直線接縫；
  用相鄰已修正皮膚的同一套調整量（a/b 目標相同、明暗取相鄰修正量的平滑延伸）補上，不另外提亮。
- 驗證以無損像素為準（逐像素、門檻 0）；JPEG 輸出誤差另外記錄。輸出 docs/calendar/decision_site/public/cover30/，資料 docs/calendar/data/cal_m5_r30_restore.json。
用法：python3 -I docs/calendar/tools/build_cal_m5_coco_r30.py --raw-dir DIR --edit FILE [--make-masks] [--master OUT.png] [--check]
"""
import argparse
import hashlib
import io
import json
import os
import shutil
import subprocess
import sys
import tempfile

import numpy as np
from PIL import Image, ImageDraw, ImageFont

ROOT = subprocess.check_output(['git', 'rev-parse', '--show-toplevel'], text=True).strip()
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_cal_m5_coco_r28 as R28  # noqa: E402
import build_cal_m5_coco_r29 as R29  # noqa: E402

ROUND = 'M-5 R30'
PUB_REL = 'docs/calendar/decision_site/public/cover30'
DATA_REL = 'docs/calendar/data/cal_m5_r30_restore.json'
ZONES = 'review/calendar/m5_r30/zones.json'
MASK_DIR = 'review/calendar/m5_r30/masks'
CJK_FONT = '/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc'
CROP = (3430, 1475, 4375, 3155)   # R28 裁切範圍；R27→R29 的所有改動都在這裡面
HEAD_BOX = (3500, 1480, 4060, 2120)
LEGS_BOX = (3740, 2520, 4340, 3155)
LOW_BOX = (3820, 2820, 4160, 3150)   # 小腿下段在大子圖裡分不出來，用小子圖補
HEM_Y = 2640                          # 腿部範圍裡，這條線以上的衣服是 Coco 的裙擺；以下被判成衣服的是椅子
R_IN, R_OUT = 4, 10                   # 過渡帶（px）
SIGMA_D = 18                          # 露出區色偏對齊的低頻 σ（px）
HALO_DL = -2.0                        # 舊捲髮淡髮暈：R27 比目前暗多少（L*）才算舊頭髮
# R29 小腿下段漏調的那一條
ANKLE = {'rect': (4060, 2860, 4125, 3100), 'ab': (17.0, 23.0), 'sigma': 20, 'dl_sigma': 14}
VIEWS = {'face': (3600, 1560, 3920, 1900), 'neck_chest': (3600, 1820, 3960, 2110), 'hand': (3650, 2180, 3940, 2380), 'legs': (3780, 2560, 4320, 3150)}
VIEW_ZH = {'face': '臉', 'neck_chest': '脖子與胸口', 'hand': '右手', 'legs': '腿'}
NVIEWS = {'somi': (3520, 1560, 3680, 1920), 'rainie': (3860, 1500, 4020, 1960), 'mia': (3760, 2990, 3990, 3160), 'ankle': (3990, 2880, 4140, 3110)}
NVIEW_ZH = {'somi': 'Somi 左袖', 'rainie': 'Rainie 手臂', 'mia': 'Mia 腳背與鞋', 'ankle': 'Coco 腳踝（R29 漏調處）'}


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def poly_mask(shape, pts, ox, oy):
    import cv2
    m = np.zeros(shape, np.uint8)
    cv2.fillPoly(m, [np.array([(x - ox, y - oy) for x, y in pts], np.int32)], 1)
    return m.astype(bool)


def r29_weights(shape):
    """R29 各塊修正遮罩合成的權重圖（全圖尺寸，0–1）。"""
    W = np.zeros(shape, np.float32)
    for k, p in R29.PARTS.items():
        x0, y0, x1, y1 = p['box']
        W[y0:y1, x0:x1] = np.maximum(W[y0:y1, x0:x1], np.asarray(Image.open(os.path.join(ROOT, R29.MASK_DIR, f'{k}.png')), np.float32) / 255)
    return W


def ankle_fix(r28, r29):
    """補齊 R29 小腿下段漏調的一條：同樣的 a/b 目標；明暗用相鄰已修正皮膚的修正量平滑延伸；權重與 R29 遮罩互補，接縫處總權重連續。"""
    import cv2
    x0, y0, x1, y1 = ANKLE['rect']
    w = np.asarray(Image.open(os.path.join(ROOT, MASK_DIR, 'ankle.png')), np.float32) / 255
    W29 = r29_weights(r29.shape[:2])
    # 明暗修正量：R29 已修正皮膚（權重 > 0.5）的實際 ΔL，在周圍 60 px 內做遮罩高斯平均後延伸到這一條
    m = 60
    X0, Y0, X1, Y1 = x0 - m, y0 - m, x1 + m, y1 + m
    L28 = R29.to_lab(r28[Y0:Y1, X0:X1])[..., 0]
    L29 = R29.to_lab(r29[Y0:Y1, X0:X1])[..., 0]
    src = (W29[Y0:Y1, X0:X1] > 0.5).astype(np.float32)
    dL = R29.masked_blur((L29 - L28) / np.maximum(W29[Y0:Y1, X0:X1], 1e-3) * src, src, ANKLE['dl_sigma'])[m:-m, m:-m]
    sub = r29[y0:y1, x0:x1].copy()
    L = R29.to_lab(sub)
    lowa = R29.masked_blur(L[..., 1], w, ANKLE['sigma'])
    lowb = R29.masked_blur(L[..., 2], w, ANKLE['sigma'])
    N = L.copy()
    N[..., 0] = L[..., 0] + w * dL
    N[..., 1] = L[..., 1] + w * (ANKLE['ab'][0] - lowa)
    N[..., 2] = L[..., 2] + w * (ANKLE['ab'][1] - lowb)
    rgb = np.where((w <= 0)[..., None], sub, R29.to_rgb(N))
    out = r29.copy()
    out[y0:y1, x0:x1] = rgb
    sel = w > 0.5
    rec = {'rect': list(ANKLE['rect']), 'px': int((w > 0).sum()), 'target_ab': list(ANKLE['ab']),
           'dL_range': [round(float(dL[sel].min()), 2), round(float(dL[sel].max()), 2)] if sel.any() else None,
           'before_Lab': R29.stats(L, w), 'after_Lab': R29.stats(R29.to_lab(rgb), w)}
    return out, rec


def classes(img):
    """裁切範圍的類別圖（0 背景、1 頭髮、2 身體皮膚、3 臉、4 衣服、5 配件）：頭部、腿部、小腿下段各自分割。"""
    from cal_seg import categories
    cx0, cy0, cx1, cy1 = CROP
    C = np.zeros((cy1 - cy0, cx1 - cx0), np.uint8)
    for x0, y0, x1, y1 in (HEAD_BOX, LEGS_BOX, LOW_BOX):
        C[y0 - cy0:y1 - cy0, x0 - cx0:x1 - cx0] = categories(np.ascontiguousarray(img[y0:y1, x0:x1]))
    return C


def footprint(img, C, Z, cur=None):
    """單一版本裡 Coco 的範圍（裁切座標，bool）。cur：算 R27 舊範圍時傳入目前版本，用來抓舊捲髮外圍的淡髮暈。"""
    import cv2
    cx0, cy0, cx1, cy1 = CROP
    sh = C.shape
    F = np.zeros(sh, bool)
    yy = np.arange(sh[0])[:, None] + cy0
    xx = np.arange(sh[1])[None, :] + cx0
    inbox = lambda b: (xx >= b[0]) & (xx < b[2]) & (yy >= b[1]) & (yy < b[3])  # noqa: E731
    nb = {k: poly_mask(sh, v['poly'], cx0, cy0) for k, v in Z['neighbors'].items()}
    zone = nb['somi_sleeve'] | nb['rainie_arm']
    # 頭部
    hb = inbox(HEAD_BOX)
    hair = C == 1
    L = R29.to_lab(img[cy0:cy1, cx0:cx1])[..., 0]
    near = cv2.dilate(hair.astype(np.uint8), np.ones((31, 31), np.uint8)).astype(bool)
    dark = (L < 38) & near
    F |= hb & (hair | dark | (C == 3) | (C == 5))
    F |= hb & ((C == 2) | (C == 4)) & ~zone
    if cur is not None:
        # 舊捲髮外圍的淡髮暈與細髮絲：分割抓不到、只比牆暗 2–6；在舊頭髮 30 px 內、R27 比目前版本明顯暗（模糊後差 < −2）的地方也算舊 Coco，
        # 否則還原 R27 會把舊髮暈帶回來。鄰人與牆本身的色偏只有約 1，不會被算進來。
        Lc = R29.to_lab(cur[cy0:cy1, cx0:cx1])[..., 0]
        near30 = cv2.dilate((hair | dark).astype(np.uint8), cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (61, 61))).astype(bool)
        halo = hb & near30 & (cv2.GaussianBlur(L - Lc, (0, 0), 2) < HALO_DL)
        halo = cv2.morphologyEx(halo.astype(np.uint8), cv2.MORPH_OPEN, np.ones((3, 3), np.uint8))
        F |= cv2.dilate(halo, np.ones((5, 5), np.uint8)).astype(bool)
    # 右手範圍整塊（連同 R28 羽化帶：四周都是 Coco 自己的開襟衫與洋裝）
    R = json.load(open(os.path.join(ROOT, R28.REGION), encoding='utf-8'))
    F |= cv2.dilate(poly_mask(sh, R['parts']['right_hand'], cx0, cy0).astype(np.uint8), np.ones((33, 33), np.uint8)).astype(bool)
    # 腿部
    lb = inbox(LEGS_BOX)
    F |= lb & (C == 2) & ~nb['mia_foot']
    F |= lb & (C == 4) & (yy < HEM_Y)
    for k in ('back_shoe', 'front_shoe', 'dress_drape'):
        F |= poly_mask(sh, Z['coco_add'][k], cx0, cy0)
    return F


def make_masks(raw_dir, edit_path):
    """產生 R30 用的遮罩（只需做一次；建置只讀檔）：腳踝漏調那一條、R27／R30 兩版的 Coco 範圍、兩版的類別圖。"""
    import cv2
    from cal_seg import categories
    K = R28.compose(raw_dir, edit_path, R28.EDIT_SHA)
    orig, r28 = np.asarray(K['orig']), np.asarray(K['result'])
    r29, _ = R29.correct(r28)
    os.makedirs(os.path.join(ROOT, MASK_DIR), exist_ok=True)
    # 腳踝：小子圖分割的身體皮膚 ∩ 矩形，扣掉 R29 已修正的權重（互補），引導濾波柔邊
    x0, y0, x1, y1 = ANKLE['rect']
    lx0, ly0, lx1, ly1 = LOW_BOX
    cat = categories(np.ascontiguousarray(r28[ly0:ly1, lx0:lx1]))[y0 - ly0:y1 - ly0, x0 - lx0:x1 - lx0]
    Z = json.load(open(os.path.join(ROOT, ZONES), encoding='utf-8'))
    sk = (cat == 2) & ~poly_mask(cat.shape, Z['neighbors']['mia_foot']['poly'], x0, y0)
    gray = cv2.cvtColor(np.ascontiguousarray(r28[y0:y1, x0:x1]), cv2.COLOR_RGB2GRAY).astype(np.float32) / 255
    soft = np.clip(R29.guided(gray, sk.astype(np.float32), 4, 1e-3), 0, 1)
    W29 = r29_weights(r28.shape[:2])[y0:y1, x0:x1]
    soft = np.clip(soft * (1 - W29), 0, 1)
    Image.fromarray((soft * 255).round().astype(np.uint8)).save(os.path.join(ROOT, MASK_DIR, 'ankle.png'), optimize=False)
    r30a, _ = ankle_fix(r28, r29)
    rec = {}
    for tag, img in (('r27', orig), ('r30', r30a)):
        C = classes(img)
        F = footprint(img, C, Z, r30a if tag == 'r27' else None)
        if tag == 'r30':   # 本系列實際修正過的皮膚（R29 各塊與腳踝）一定在新 Coco 範圍內
            cx0, cy0, cx1, cy1 = CROP
            Wc = r29_weights(r28.shape[:2])[cy0:cy1, cx0:cx1]
            Wc[y0 - cy0:y1 - cy0, x0 - cx0:x1 - cx0] = np.maximum(Wc[y0 - cy0:y1 - cy0, x0 - cx0:x1 - cx0], soft)
            F |= Wc > 0
        Image.fromarray(C).save(os.path.join(ROOT, MASK_DIR, f'cls_{tag}.png'), optimize=False)
        Image.fromarray((F * 255).astype(np.uint8)).save(os.path.join(ROOT, MASK_DIR, f'coco_{tag}.png'), optimize=False)
        rec[tag] = int(F.sum())
    return rec


def load_mask(name):
    return np.asarray(Image.open(os.path.join(ROOT, MASK_DIR, name)))


def restore(orig, cur, m28):
    """Coco 實際編輯範圍外還原成 R27；露出區對齊色偏。回傳（結果、範圍與權重、紀錄）。全部在裁切座標內算，範圍外原樣。"""
    import cv2
    cx0, cy0, cx1, cy1 = CROP
    O = orig[cy0:cy1, cx0:cx1].astype(np.float32)
    P = cur[cy0:cy1, cx0:cx1].astype(np.float32)
    M = m28[cy0:cy1, cx0:cx1]
    Fo, Fn = load_mask('coco_r27.png') > 0, load_mask('coco_r30.png') > 0
    C27, C30 = load_mask('cls_r27.png'), load_mask('cls_r30.png')
    U = Fo | Fn
    dist = cv2.distanceTransform((~U).astype(np.uint8), cv2.DIST_L2, 5)
    w = np.clip((dist - R_IN) / (R_OUT - R_IN), 0, 1).astype(np.float32)   # 1＝直接用 R27
    # 新 Coco 的柔邊（只在範圍外 R_IN px 內有值）
    gray = cv2.cvtColor(cur[cy0:cy1, cx0:cx1], cv2.COLOR_RGB2GRAY).astype(np.float32) / 255
    a = np.clip(R29.guided(gray, Fn.astype(np.float32), 3, 1e-3), 0, 1)
    a[Fn] = 1
    a[cv2.distanceTransform((~Fn).astype(np.uint8), cv2.DIST_L2, 5) > R_IN] = 0
    # 色偏場：已還原、且兩版同類別的地方，R27 − 目前；按類別（背景、皮膚、衣服）各自低頻延伸
    omega = (w >= 1) & (M > 0.98)
    Dr = O - P
    probs, fields = [], []
    for c in (0, 2, 4):
        sup = (omega & (C27 == c) & (C30 == c)).astype(np.float32)
        den = cv2.GaussianBlur(sup, (0, 0), SIGMA_D)
        f = np.dstack([cv2.GaussianBlur(Dr[..., i] * sup, (0, 0), SIGMA_D) for i in range(3)]) / np.maximum(den, 1e-4)[..., None]
        den2 = cv2.GaussianBlur(sup, (0, 0), SIGMA_D * 4)
        f2 = np.dstack([cv2.GaussianBlur(Dr[..., i] * sup, (0, 0), SIGMA_D * 4) for i in range(3)]) / np.maximum(den2, 1e-4)[..., None]
        t = np.clip(den / 0.05, 0, 1)[..., None]
        fields.append(t * f + (1 - t) * f2)
        pc = np.clip(R29.guided(gray, (C30 == c).astype(np.float32), 3, 1e-3), 0, 1)
        probs.append(pc)
    pr = np.dstack(probs) + 1e-6
    pr /= pr.sum(2, keepdims=True)
    D = sum(fields[i] * pr[..., i:i + 1] for i in range(3))
    out = P + (1 - a)[..., None] * (w[..., None] * (O - P) + (1 - w)[..., None] * M[..., None] * D)
    out = out.round().clip(0, 255).astype(np.uint8)
    out[(w >= 1) & (a <= 0)] = orig[cy0:cy1, cx0:cx1][(w >= 1) & (a <= 0)]
    E = ~((w >= 1) & (a <= 0)) & ((M > 0) | (P != O).any(2))   # Coco 實際編輯範圍（含過渡帶；只算可能被改到的像素）
    res = cur.copy()
    res[cy0:cy1, cx0:cx1] = out
    revealed = Fo & ~Fn & (M > 0)
    rec = {'coco_r27_px': int(Fo.sum()), 'coco_r30_px': int(Fn.sum()), 'edit_range_px': int(E.sum()),
           'revealed_px': int(revealed.sum()), 'band_px': [R_IN, R_OUT], 'sigma_D_px': SIGMA_D}
    return res, E, revealed, rec


def jpeg(im, q=90):
    b = io.BytesIO()
    im.save(b, 'JPEG', quality=q, subsampling=2, optimize=False)
    return b.getvalue()


def lbl(im, text, h=34):
    W = Image.new('RGB', (im.width, im.height + h), (255, 255, 255))
    W.paste(im, (0, h))
    ImageDraw.Draw(W).text((6, h - 8), text, font=ImageFont.truetype(CJK_FONT, 21), fill=(30, 30, 34), anchor='ls')
    return W


def compute(raw_dir, edit_path):
    K = R28.compose(raw_dir, edit_path, R28.EDIT_SHA)
    orig, r28 = np.asarray(K['orig']), np.asarray(K['result'])
    r29, _ = R29.correct(r28)
    cur, ank = ankle_fix(r28, r29)
    x0, y0, x1, y1 = K['R']['crop']
    m28 = np.zeros(orig.shape[:2], np.float32)
    m28[y0:y1, x0:x1] = K['mask']
    r30, E, revealed, rrec = restore(orig, cur, m28)
    return {'K': K, 'orig': orig, 'r28': r28, 'r29': r29, 'r30': r30, 'E': E, 'revealed': revealed, 'm28': m28, 'ankle': ank, 'restore': rrec}


def by_person(X):
    """按人物歸屬分組：R28 回填範圍內、不屬於目前 Coco 的像素，R28 改了多少、R30 還剩多少（無損、門檻 0）。"""
    cx0, cy0, cx1, cy1 = CROP
    Z = json.load(open(os.path.join(ROOT, ZONES), encoding='utf-8'))
    sl = (slice(cy0, cy1), slice(cx0, cx1))
    o, r28, r30 = X['orig'][sl].astype(int), X['r28'][sl].astype(int), X['r30'][sl].astype(int)
    M, E = X['m28'][sl], X['E']
    Fo, Fn = load_mask('coco_r27.png') > 0, load_mask('coco_r30.png') > 0
    zones = {k: poly_mask(Fo.shape, v['poly'], cx0, cy0) for k, v in Z['neighbors'].items()}
    anyz = np.zeros(Fo.shape, bool)
    for v in zones.values():
        anyz |= v
    groups = [('somi_sleeve', 'Somi 左袖（含旁邊牆面）', zones['somi_sleeve']), ('rainie_arm', 'Rainie 手臂與洋裝（含旁邊牆面）', zones['rainie_arm']),
              ('mia_foot', 'Mia 腳背、鞋與褲管（含旁邊地板）', zones['mia_foot']), ('background', '其他背景（牆、椅子、地板）', ~anyz)]
    c28 = (r28 != o).any(2)
    c30 = (r30 != o).any(2)
    dd28, dd30 = np.abs(r28 - o).max(2), np.abs(r30 - o).max(2)
    out = []
    for k, zh, g in groups:
        base = g & (M > 0) & ~Fn
        over = base & ~Fo & c28   # R27 裡本來就是這個人／背景、被 R28 改到的像素（誤改）
        rest = over & ~E          # 直接還原成 R27
        band = over & E           # 緊貼 Coco 的過渡帶（混合）
        rev = base & Fo           # R27 裡是舊 Coco 頭髮、換髮後露出這個人／背景：R27 沒有可還原的內容，用編輯結果並對齊色調
        out.append({'key': k, 'zh': zh,
                    'r28_overreach_px': int(over.sum()), 'r28_overreach_gt3_px': int((over & (dd28 > 3)).sum()),
                    'r28_overreach_mean_abs_diff': round(float(dd28[over].mean()), 2) if over.any() else 0,
                    'restored_px': int(rest.sum()), 'restored_still_changed_px': int((rest & c30).sum()),
                    'band_px': int(band.sum()), 'band_mean_abs_diff_r30': round(float(dd30[band].mean()), 2) if band.any() else 0,
                    'revealed_px': int(rev.sum())})
    return out


def build(raw_dir, edit_path, pub, data_path, master=None):
    if os.path.isdir(pub):
        shutil.rmtree(pub)
    os.makedirs(pub)
    X = compute(raw_dir, edit_path)
    orig, r29, r30 = X['orig'], X['r29'], X['r30']
    cx0, cy0, cx1, cy1 = CROP
    Ef = np.zeros(orig.shape[:2], bool)
    Ef[cy0:cy1, cx0:cx1] = X['E']
    d0 = (r30 != orig).any(2)
    d3 = np.abs(r30.astype(int) - orig.astype(int)).max(2) > 3
    diff = {'tolerance': '無損主檔逐像素比對，門檻 0（任一通道有差就算改動）；另列差 > 3 的數量',
            'edit_range_px': int(Ef.sum()),
            'vs_r27_changed_px': int(d0.sum()), 'vs_r27_changed_gt3_px': int(d3.sum()),
            'vs_r27_changed_outside_edit_range_px': int((d0 & ~Ef).sum()),
            'r29_vs_r27_changed_outside_edit_range_px': int(((r29 != orig).any(2) & ~Ef).sum()),
            'vs_r29_changed_px': int((r30 != r29).any(2).sum())}
    assert diff['vs_r27_changed_outside_edit_range_px'] == 0, 'Coco 實際編輯範圍外仍有改動'
    if master:
        Image.fromarray(r30).save(master, optimize=False)
    O, P9, P = Image.fromarray(orig), Image.fromarray(r29), Image.fromarray(r30)
    files = {}

    def save(name, data):
        open(os.path.join(pub, name), 'wb').write(data)
        files[name] = sha256(data)
    full = jpeg(P)
    save('r30_after_f.jpg', full)
    vw = 1600
    vh = round(P.height * vw / P.width)
    save('r30_after_v.jpg', jpeg(P.resize((vw, vh), Image.LANCZOS), 88))
    # JPEG 誤差另外記：發佈的 JPEG 解回來與無損主檔、與 R27 原圖的差（不拿來證明主檔零差異）
    J = np.asarray(Image.open(io.BytesIO(full)).convert('RGB')).astype(int)
    ej = np.abs(J - r30.astype(int)).max(2)
    eo = np.abs(J - orig.astype(int)).max(2)[~Ef]
    jpeg_err = {'note': '網站上的 JPEG（品質 90）解碼後與無損主檔的差，以及在 Coco 範圍外與 R27 原圖的差；這是壓縮誤差，主檔零差異只以無損像素為準',
                'vs_master_mean': round(float(ej.mean()), 3), 'vs_master_max': int(ej.max()), 'vs_master_gt3_share': round(float((ej > 3).mean()), 4),
                'outside_edit_range_vs_r27_mean': round(float(eo.mean()), 3), 'outside_edit_range_vs_r27_max': int(eo.max())}
    # Coco 前後（R27 原圖｜R30）：原尺寸局部與封面尺寸
    for k, b in VIEWS.items():
        save(f'r30_part_{k}.jpg', jpeg(R29.row([lbl(O.crop(b), f'R27 原圖｜{VIEW_ZH[k]}'), lbl(P.crop(b), f'R30 目前｜{VIEW_ZH[k]}')]), 92))
    cw = 2440
    s = cw / P.width
    cb = tuple(round(v * s) for v in (3380, 1450, 4420, 3200))
    ch = round(P.height * s)
    save('r30_coverscale.jpg', jpeg(R29.row([lbl(O.resize((cw, ch), Image.LANCZOS).crop(cb), 'R27 原圖｜封面尺寸'),
                                             lbl(P.resize((cw, ch), Image.LANCZOS).crop(cb), 'R30 目前｜封面尺寸')]), 92))
    ref = Image.open(os.path.join(ROOT, R28.REF)).convert('RGB')
    bx = json.load(open(os.path.join(ROOT, R28.BOXES), encoding='utf-8'))
    T = 360
    save('r30_face_cmp.jpg', jpeg(R29.row([lbl(ref.crop(tuple(bx['refs']['coco-wu'])).resize((T, T), Image.LANCZOS), '身分基準（Coco）'),
                                           lbl(R28.face_crop(P, bx['covers']['H-A']['people']['coco-wu']['face']).resize((T, T), Image.LANCZOS), 'R30 目前')]), 90))
    # 技術紀錄（收合）：鄰人還原與腳踝補齊（R27｜R29｜R30）、Coco 實際編輯範圍、相對 R27 的差異圖
    for k, b in NVIEWS.items():
        sc = 2 if (b[2] - b[0]) <= 160 else 1.5
        ims = [lbl(im.crop(b).resize((round((b[2] - b[0]) * sc), round((b[3] - b[1]) * sc)), Image.LANCZOS), t)
               for im, t in ((O, 'R27 原圖'), (P9, 'R29'), (P, 'R30'))]
        save(f'r30_fix_{k}.jpg', jpeg(R29.row(ims), 92))
    rb = (3380, 1450, 4420, 3200)
    base = np.asarray(P.crop(rb)).astype(np.float32)
    em = np.zeros((rb[3] - rb[1], rb[2] - rb[0]), bool)
    em[cy0 - rb[1]:cy1 - rb[1], cx0 - rb[0]:cx1 - rb[0]] = X['E']
    tint = base.copy()
    tint[em] = base[em] * 0.45 + np.array([40, 110, 255]) * 0.55
    save('r30_range_v.jpg', jpeg(Image.fromarray(tint.round().astype(np.uint8)).resize((520, 875), Image.LANCZOS), 88))
    dm = Image.fromarray((d0 * 255).astype(np.uint8)).resize((vw, vh), Image.BOX)
    save('r30_diff_v.jpg', jpeg(Image.merge('RGB', (dm, dm, dm)), 88))
    out = []
    for name, h in sorted(files.items()):
        im = Image.open(os.path.join(pub, name))
        out.append({'path': name, 'sha256': h, 'px': [im.width, im.height], 'bytes': os.path.getsize(os.path.join(pub, name))})
    mk = {n: sha256(open(os.path.join(ROOT, MASK_DIR, n), 'rb').read()) for n in sorted(os.listdir(os.path.join(ROOT, MASK_DIR)))}
    D = {'round': ROUND,
         'note': '從 R29 結果另存（R27／R28／R29 不覆蓋）：R28 回填範圍內不屬於 Coco 的像素還原成 R27 原圖；補齊 R29 腳踝漏調。生成 0、付費 0、上傳 0。',
         'source': {'r27_sha256': R28.SRC_SHA, 'r28_edit_sha256': R28.EDIT_SHA, 'zones_sha256': sha256(open(os.path.join(ROOT, ZONES), 'rb').read()), 'masks_sha256': mk},
         'master': {'what': '無損主檔（RGB 4800×3584，PNG，不進 git；可用本工具從私有原圖重建）', 'pixels_sha256': sha256(np.ascontiguousarray(r30).tobytes())},
         'method': {'attribution': '分割（頭髮、臉、皮膚、衣服）＋人工範圍（鄰人位置、分割漏掉的鞋與裙擺）＋舊捲髮淡髮暈偵測 → R27 舊 Coco、目前新 Coco 的範圍；聯集外擴過渡帶＝Coco 實際編輯範圍',
                    'restore': f'範圍外直接用 R27 像素；聯集外 {R_IN}–{R_OUT} px 過渡；舊 Coco 有、新 Coco 沒有的露出區只能用編輯結果，低頻色偏按類別（牆、皮膚、衣服）對齊旁邊已還原的 R27（σ {SIGMA_D} px）',
                    'ankle': 'R29 小腿下段修正矩形右緣（x＝4078）外的一條：同樣 a/b 目標；明暗取相鄰已修正皮膚修正量的平滑延伸；權重與 R29 遮罩互補'},
         'ankle': X['ankle'], 'restore': X['restore'], 'by_person': by_person(X), 'diff': diff, 'jpeg': jpeg_err, 'files': out}
    with open(data_path, 'w', encoding='utf-8') as fh:
        json.dump(D, fh, ensure_ascii=False, indent=1)
        fh.write('\n')
    return D


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--raw-dir', required=True)
    ap.add_argument('--edit', required=True)
    ap.add_argument('--make-masks', action='store_true')
    ap.add_argument('--master', help='另存無損主檔（PNG）的路徑；放在 repo 外')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    if a.make_masks:
        print(json.dumps(make_masks(a.raw_dir, a.edit), ensure_ascii=False))
        return
    if a.check:
        old = json.load(open(os.path.join(ROOT, DATA_REL), encoding='utf-8'))
        with tempfile.TemporaryDirectory() as tmp:
            D = build(a.raw_dir, a.edit, os.path.join(tmp, 'p'), os.path.join(tmp, 'd.json'))
            same = json.loads(json.dumps(D, ensure_ascii=False)) == old
            pub = os.path.join(ROOT, PUB_REL)
            diff = [x['path'] for x in D['files'] if not os.path.exists(os.path.join(pub, x['path'])) or sha256(open(os.path.join(pub, x['path']), 'rb').read()) != x['sha256']]
            extra = sorted(set(os.listdir(pub)) - {x['path'] for x in D['files']})
        ok = same and not diff and not extra
        print(json.dumps({'check': 'PASS' if ok else 'FAIL', 'data_same': same, 'files': len(D['files']), 'diff': diff, 'extra': extra,
                          'outside_edit_range_changed_px': D['diff']['vs_r27_changed_outside_edit_range_px']}, ensure_ascii=False))
        sys.exit(0 if ok else 1)
    D = build(a.raw_dir, a.edit, os.path.join(ROOT, PUB_REL), os.path.join(ROOT, DATA_REL), a.master)
    print(json.dumps({k: D[k] for k in ('ankle', 'restore', 'by_person', 'diff', 'jpeg')}, ensure_ascii=False, indent=1))


if __name__ == '__main__':
    main()
