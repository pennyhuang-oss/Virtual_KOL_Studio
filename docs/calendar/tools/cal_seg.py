"""R3：主角保護遮罩與髮頂判定（只讀像素、產生遮罩，不改任何像素）。

模型：mediapipe selfie_multiclass_256x256（類別 0 背景、1 頭髮、2 身體皮膚、3 臉部皮膚、4 衣服、5 其他配件）。
下載：https://storage.googleapis.com/mediapipe-models/image_segmenter/selfie_multiclass_256x256/float32/latest/selfie_multiclass_256x256.tflite
放在 ~/.cache/mediapipe/（R3 使用的檔案 sha256 c6748b12…7e0e0）。這是分類模型，只用來決定「哪些像素不准動」，不生成內容。
"""
import os

import numpy as np

MODEL = os.path.expanduser('~/.cache/mediapipe/selfie_multiclass_256x256.tflite')
_SEG = None
_CACHE = {}


def _segmenter():
    global _SEG
    if _SEG is None:
        from mediapipe.tasks import python as mpp
        from mediapipe.tasks.python import vision
        _SEG = vision.ImageSegmenter.create_from_options(vision.ImageSegmenterOptions(
            base_options=mpp.BaseOptions(model_asset_path=MODEL), output_category_mask=True))
    return _SEG


def categories(rgb):
    """rgb: (H,W,3) uint8 → (H,W) uint8 類別圖，與輸入同尺寸。"""
    import mediapipe as mp
    key = (rgb.shape, hash(rgb[::37, ::37].tobytes()))
    if key not in _CACHE:
        r = _segmenter().segment(mp.Image(image_format=mp.ImageFormat.SRGB, data=np.ascontiguousarray(rgb)))
        _CACHE[key] = r.category_mask.numpy_view()[..., 0].copy() if r.category_mask.numpy_view().ndim == 3 else r.category_mask.numpy_view().copy()
    return _CACHE[key]


def subject_mask(rgb, face_pts, keep_hull=None):
    """主角遮罩：人物類別（1–5）中，包含主臉特徵點的連通區塊。
    face_pts：(N,2) 主臉特徵點（像素）。keep_hull：可選的人工多邊形（像素），與連通區塊取交集，用來把貼在主角身上的路人分開。"""
    import cv2
    cat = categories(rgb)
    person = (cat > 0).astype(np.uint8)
    n, lab = cv2.connectedComponents(person, connectivity=8)
    pts = np.clip(np.round(face_pts).astype(int), 0, [rgb.shape[1] - 1, rgb.shape[0] - 1])
    ids = lab[pts[:, 1], pts[:, 0]]
    ids = ids[ids > 0]
    main = np.bincount(ids).argmax() if len(ids) else 0
    m = (lab == main) if main else np.zeros(person.shape, bool)
    if keep_hull is not None:
        hull = np.zeros(person.shape, np.uint8)
        cv2.fillPoly(hull, [np.round(np.array(keep_hull)).astype(np.int32)], 1)
        m = m & hull.astype(bool)
    return m


def hair_top(rgb, face_pts, keep_hull=None):
    """回傳 (主角頭髮最上緣 y 像素, 頭髮是否碰到原圖上緣, 碰到上緣的頭髮欄數)。沒有頭髮像素則回 (None, False, 0)。"""
    cat = categories(rgb)
    subj = subject_mask(rgb, face_pts, keep_hull)
    hair = (cat == 1) & subj
    rows = np.where(hair.any(1))[0]
    if not len(rows):
        return None, False, 0
    top_cols = int(hair[0].sum())
    return int(rows.min()), top_cols >= 20, top_cols
