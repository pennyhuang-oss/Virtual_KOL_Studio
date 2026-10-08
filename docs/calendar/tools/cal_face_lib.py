"""Face geometry helpers for the calendar face comparison (crop/scale/mask only; never edits pixels of features)."""
import os

import numpy as np
from PIL import Image, ImageDraw, ImageFilter

MODEL = os.path.expanduser('~/.cache/mediapipe/face_landmarker.task')  # same model file as tools/build_face_crops.py


def landmarks(path):
    """mediapipe FaceLandmarker on decoded RGB pixels (works for webp too). Returns ((478,2) px array | None, (W,H))."""
    import mediapipe as mp
    from mediapipe.tasks import python as mpp
    from mediapipe.tasks.python import vision
    if not hasattr(landmarks, '_lm'):
        landmarks._lm = vision.FaceLandmarker.create_from_options(
            vision.FaceLandmarkerOptions(base_options=mpp.BaseOptions(model_asset_path=MODEL), num_faces=1))
    rgb = np.asarray(Image.open(path).convert('RGB'))
    r = landmarks._lm.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=rgb))
    H, W = rgb.shape[:2]
    if not r.face_landmarks:
        return None, (W, H)
    return np.array([[l.x * W, l.y * H] for l in r.face_landmarks[0]], dtype=float), (W, H)

# mediapipe FaceMesh face-oval ring (canonical 36-point loop)
FACE_OVAL = [10, 338, 297, 332, 284, 251, 389, 356, 454, 323, 361, 288, 397, 365, 379, 378, 400, 377,
             152, 148, 176, 149, 150, 136, 172, 58, 132, 93, 234, 127, 162, 21, 54, 103, 67, 109]
L_EYE, R_EYE, NOSE, CHIN, TOP = (33, 133), (362, 263), 1, 152, 10


def geometry(path):
    P, (W, H) = landmarks(path)
    if P is None:
        return None
    le = P[list(L_EYE)].mean(axis=0)
    re = P[list(R_EYE)].mean(axis=0)
    mid = (le + re) / 2
    iod = float(np.linalg.norm(re - le))
    yaw = float((P[NOSE][0] - mid[0]) / iod)          # 0 ≈ frontal; sign = turn direction
    roll = float(np.degrees(np.arctan2(re[1] - le[1], re[0] - le[0])))
    faceh = float(P[CHIN][1] - P[TOP][1])
    return {'P': P, 'W': W, 'H': H, 'mid': mid, 'iod': iod, 'yaw': yaw, 'roll': roll, 'faceh': faceh}


def head_crop(path, g, out, size=420, scale=2.35):
    """Square crop centred a little above the eye line; side = scale x (forehead-chin height). Crop + resize only."""
    im = Image.open(path).convert('RGB')
    side = g['faceh'] * scale
    cx, cy = g['mid'][0], g['mid'][1] + 0.05 * g['faceh']
    box = (cx - side / 2, cy - side / 2, cx + side / 2, cy + side / 2)
    canvas = Image.new('RGB', (int(side), int(side)), (128, 128, 128))
    x0, y0 = int(box[0]), int(box[1])
    ix0, iy0 = max(x0, 0), max(y0, 0)
    ix1, iy1 = min(int(box[2]), im.width), min(int(box[3]), im.height)
    canvas.paste(im.crop((ix0, iy0, ix1, iy1)), (ix0 - x0, iy0 - y0))  # out-of-frame area stays flat grey
    canvas = canvas.resize((size, size), Image.LANCZOS)
    canvas.save(out, quality=90)
    return out


def masked_face(path, g, out, w=360, h=440, iod_px=120):
    """Keep only the face-oval polygon (hair, clothes, background → flat grey). Scale so the eye distance = iod_px.
    No rotation, no warping, no retouch."""
    im = Image.open(path).convert('RGB')
    m = Image.new('L', im.size, 0)
    ImageDraw.Draw(m).polygon([tuple(g['P'][i]) for i in FACE_OVAL], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(max(1, int(g['iod'] * 0.04))))
    grey = Image.new('RGB', im.size, (128, 128, 128))
    comp = Image.composite(im, grey, m)
    k = iod_px / g['iod']
    comp = comp.resize((int(im.width * k), int(im.height * k)), Image.LANCZOS)
    cx, cy = g['mid'][0] * k, g['mid'][1] * k
    x0, y0 = int(cx - w / 2), int(cy - h * 0.42)
    canvas = Image.new('RGB', (w, h), (128, 128, 128))
    ix0, iy0 = max(x0, 0), max(y0, 0)
    ix1, iy1 = min(x0 + w, comp.width), min(y0 + h, comp.height)
    canvas.paste(comp.crop((ix0, iy0, ix1, iy1)), (ix0 - x0, iy0 - y0))
    canvas.save(out, quality=90)
    return out
