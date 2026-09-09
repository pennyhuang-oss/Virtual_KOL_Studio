# -*- coding: utf-8 -*-
"""背景撞臉自動偵測。

我兩次漏掉這個缺陷（rin D2 已通過的圖、rin D4 重驗的圖），都是因為
「有沒有剛好去看那一區」。這支程式把它變成量測：
偵測畫面裡所有的臉 → 最大的當主體 → 其餘每一張臉算與該人設 identity master 的身分距離。

距離基準沿用先前碰撞測試的結果：
  同一個人不同張        ≈ 0.0129
  不同人的 master 互比  ≈ 0.0157
  當時採用的碰撞門檻      0.0220
所以背景臉若距離 < 0.0157，就是高度可疑的撞臉。
"""
import numpy as np, mediapipe as mp, cv2, sys, json
from mediapipe.tasks import python as mpp
from mediapipe.tasks.python import vision

OVAL=[10,338,297,332,284,251,389,356,454,323,361,288,397,365,379,378,400,377,
      152,148,176,149,150,136,172,58,132,93,234,127,162,21,54,103,67,109]

_lm=None
def landmarker(n=5):
    global _lm
    o=vision.FaceLandmarkerOptions(
        base_options=mpp.BaseOptions(model_asset_path='/root/.cache/mediapipe/face_landmarker.task'),
        num_faces=n)
    return vision.FaceLandmarker.create_from_options(o)

def faces(path,n=5):
    img=cv2.cvtColor(cv2.imread(path),cv2.COLOR_BGR2RGB)
    h,w=img.shape[:2]
    res=landmarker(n).detect(mp.Image(image_format=mp.ImageFormat.SRGB,data=img))
    out=[]
    for f in res.face_landmarks:
        P=np.array([[f[i].x*w,f[i].y*h,f[i].z*w] for i in OVAL])
        xs=[p.x*w for p in f]; ys=[p.y*h for p in f]
        area=(max(xs)-min(xs))*(max(ys)-min(ys))
        out.append({"pts":P,"area":area,"cx":float(np.mean(xs)),"cy":float(np.mean(ys)),
                    "bw":float(max(xs)-min(xs))})
    out.sort(key=lambda d:-d["area"])
    return out,(w,h)

def dist(A,B):
    """FACE_OVAL 36 點的 Procrustes 對齊後平均殘差，對尺度正規化。"""
    A=A-A.mean(0); B=B-B.mean(0)
    A=A/np.sqrt((A**2).sum()); B=B/np.sqrt((B**2).sum())
    U,S,Vt=np.linalg.svd(A.T@B); R=U@Vt
    if np.linalg.det(R)<0: Vt[-1]*=-1; R=U@Vt
    return float(np.sqrt(((A@R-B)**2).sum(1)).mean())

if __name__=="__main__":
    ref_path, *imgs = sys.argv[1:]
    ref,_=faces(ref_path,1)
    if not ref: sys.exit("identity master 偵測不到臉")
    R=ref[0]["pts"]
    print(f"參考臉：{ref_path}")
    print(f"{'圖':28} {'臉數':>4} {'主體距離':>9}  背景臉距離（<0.0157 = 高度可疑）")
    for p in imgs:
        fs,(w,h)=faces(p)
        if not fs: print(f"{p.split('/')[-1]:28} {0:>4}"); continue
        d0=dist(R,fs[0]["pts"])
        rest=[]
        for f in fs[1:]:
            d=dist(R,f["pts"])
            flag="  ← 撞臉" if d<0.0157 else ("  ← 可疑" if d<0.0220 else "")
            rest.append(f"{d:.4f}(寬{f['bw']:.0f}px){flag}")
        print(f"{p.split('/')[-1]:28} {len(fs):>4} {d0:>9.4f}  " + ("; ".join(rest) if rest else "—"))
