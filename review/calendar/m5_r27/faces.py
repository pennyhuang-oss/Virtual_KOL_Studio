"""M-5 R27：在封面原圖上找臉（mediapipe FaceLandmarker 分塊掃描），輸出臉框供人工身分比對。只讀像素。"""
import json
import os
import sys

import numpy as np
from PIL import Image

MODEL = os.path.expanduser('~/.cache/mediapipe/face_landmarker.task')


def detect(path, tile=900, stride=600):
    import mediapipe as mp
    from mediapipe.tasks import python as mpp
    from mediapipe.tasks.python import vision
    lm = vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(base_options=mpp.BaseOptions(model_asset_path=MODEL), num_faces=6,
                                                                              min_face_detection_confidence=0.4))
    rgb = np.asarray(Image.open(path).convert('RGB'))
    H, W = rgb.shape[:2]
    found = []
    for y in list(range(0, H - tile, stride)) + [H - tile]:
        for x in list(range(0, W - tile, stride)) + [W - tile]:
            sub = np.ascontiguousarray(rgb[y:y + tile, x:x + tile])
            r = lm.detect(mp.Image(image_format=mp.ImageFormat.SRGB, data=sub))
            for f in r.face_landmarks:
                P = np.array([[p.x * tile + x, p.y * tile + y] for p in f])
                x0, y0 = P.min(0)
                x1, y1 = P.max(0)
                found.append([float(x0), float(y0), float(x1), float(y1)])
    faces = []
    for b in sorted(found, key=lambda b: -(b[2] - b[0])):
        cx, cy = (b[0] + b[2]) / 2, (b[1] + b[3]) / 2
        if all(abs(cx - (f[0] + f[2]) / 2) > (f[2] - f[0]) * 0.5 or abs(cy - (f[1] + f[3]) / 2) > (f[3] - f[1]) * 0.5 for f in faces):
            faces.append(b)
    faces.sort(key=lambda b: (b[0] + b[2]) / 2)
    return [[round(v) for v in b] for b in faces], [W, H]


if __name__ == '__main__':
    # 用法：python3 -I faces.py <原圖資料夾（私有，不進 git）> H-A H-B V-A V-B
    out = {}
    for c in sys.argv[2:]:
        p = os.path.join(sys.argv[1], f'cover_{c}.png')
        faces, size = detect(p)
        out[c] = {'size': size, 'faces': faces}
        print(c, len(faces), [(round((b[0] + b[2]) / 2), round((b[1] + b[3]) / 2), b[2] - b[0]) for b in faces])
    json.dump(out, open('review/calendar/m5_r27/faces_auto.json', 'w'), indent=1)
