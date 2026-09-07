#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""把臉型槽的裁切圖遮成「有輪廓、沒五官」。

為什麼要這支：
  眼／鼻／口三個槽是窄帶（1536×512、768×768、1024×512），帶不動身分。
  臉型槽是 1024×1280 的完整人像——髮際到下巴、耳到耳、背景都在。
  模型拿到的等於一張真人正面照，於是照著畫，輸出就是那個真人
  （ref_15 → 兩位被認出原圖本人；ref_03 → 被認出高允貞）。

  ChatGPT J-02.1 否決過純剪影，理由是會失去臉長寬、三庭與顎角的相對位置。
  那個顧慮成立，但它只考慮全有或全無。這支做中間解：
  **五官區域模糊，輪廓、頰緣、顎角、髮際、三庭全部原樣保留。**

用法：
  python3 tools/mask_face_crop.py <ref_id> [ref_id ...]
  讀 review/donor_cards/<ref>__FACE_SHAPE_AND_JAW.jpg
  寫 review/donor_cards/<ref>__FACE_SHAPE_AND_JAW__masked.jpg
"""
import os, sys
import numpy as np
from PIL import Image, ImageDraw, ImageFilter

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from build_face_crops import landmarks  # noqa

SLOT = "FACE_SHAPE_AND_JAW"
BROW = (105, 334, 70, 300)      # 眉線
BELOW_MOUTH = (17, 18, 200)     # 嘴下緣
LEFT = (234, 127, 93)
RIGHT = (454, 356, 323)
RX_SCALE, RY_SCALE = 0.92, 1.05  # 橢圓相對五官外框的縮放
BLUR_FRAC, FEATHER_FRAC = 0.055, 0.030


def mask_one(src, dst):
    im = Image.open(src).convert("RGB")
    P, _ = landmarks(src)
    if P is None:
        raise SystemExit(f"偵測不到臉：{src}")
    W, H = im.size
    top = min(P[i][1] for i in BROW)
    bot = max(P[i][1] for i in BELOW_MOUTH)
    left = min(P[i][0] for i in LEFT)
    right = max(P[i][0] for i in RIGHT)
    cx, cy = (left + right) / 2, (top + bot) / 2
    rx, ry = (right - left) / 2 * RX_SCALE, (bot - top) / 2 * RY_SCALE

    m = Image.new("L", (W, H), 0)
    ImageDraw.Draw(m).ellipse([cx - rx, cy - ry, cx + rx, cy + ry], fill=255)
    m = m.filter(ImageFilter.GaussianBlur(int(min(W, H) * FEATHER_FRAC)))

    blurred = im.filter(ImageFilter.GaussianBlur(int(min(W, H) * BLUR_FRAC)))
    Image.composite(blurred, im, m).save(dst, quality=94)
    return dst


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit(__doc__)
    for ref in sys.argv[1:]:
        s = f"review/donor_cards/{ref}__{SLOT}.jpg"
        d = f"review/donor_cards/{ref}__{SLOT}__masked.jpg"
        print(mask_one(s, d))
