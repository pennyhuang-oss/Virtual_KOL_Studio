"""M-5 R28：Coco 單人身分測試的底圖裁切。從 R27 H-A 原圖（私有，sha256 必須相符）裁出 region.json 的 crop 範圍，
只取像素（不帶中繼資料）存成 PNG，供上傳當編輯底圖。用法：python3 -I prep.py <R27 原圖資料夾> <輸出資料夾>"""
import hashlib
import json
import os
import sys

from PIL import Image

HERE = os.path.dirname(os.path.abspath(__file__))
SRC_SHA = '278ce0954d3a5527c418a25de527a0cb82fe9f5e958ea27eede2c9ce38aae6f5'   # R27 H-A 原圖
R = json.load(open(os.path.join(HERE, 'region.json')))
raw = open(os.path.join(sys.argv[1], 'cover_H-A.png'), 'rb').read()
assert hashlib.sha256(raw).hexdigest() == SRC_SHA
im = Image.open(os.path.join(sys.argv[1], 'cover_H-A.png')).convert('RGB')
x0, y0, x1, y1 = R['crop']
assert abs((x1 - x0) / (y1 - y0) - 9 / 16) < 1e-3, '裁切比例＝9:16（與輸出比例相同，回填不變形）'
c = im.crop((x0, y0, x1, y1))
out = os.path.join(sys.argv[2], 'base_crop_H-A_coco.png')
c.save(out, optimize=False)
print(out, c.size, hashlib.sha256(open(out, 'rb').read()).hexdigest())
