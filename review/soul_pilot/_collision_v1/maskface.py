import sys, numpy as np
from PIL import Image, ImageDraw
import mediapipe as mp
from mediapipe.tasks import python as mpp
from mediapipe.tasks.python import vision

FACE_OVAL=[10,338,297,332,284,251,389,356,454,323,361,288,397,365,379,378,400,377,
152,148,176,149,150,136,172,58,132,93,234,127,162,21,54,103,67,109]

_fl=None
def fl():
    global _fl
    if _fl is None:
        _fl=vision.FaceLandmarker.create_from_options(vision.FaceLandmarkerOptions(
            base_options=mpp.BaseOptions(model_asset_path='/root/.cache/mediapipe/face_landmarker.task'),
            num_faces=1))
    return _fl

def mask(path,out,size=300):
    """Crop to the face oval and blank everything outside it, so hair colour
    and hairstyle carry no information."""
    im=Image.open(path).convert('RGB'); W,H=im.size
    r=fl().detect(mp.Image(image_format=mp.ImageFormat.SRGB,data=np.asarray(im)))
    if not r.face_landmarks: return None
    A=np.array([[l.x*W,l.y*H] for l in r.face_landmarks[0]])
    poly=[tuple(A[i]) for i in FACE_OVAL]
    m=Image.new('L',(W,H),0); ImageDraw.Draw(m).polygon(poly,fill=255)
    flat=Image.new('RGB',(W,H),(128,128,128)); flat.paste(im,mask=m)
    xs=[p[0] for p in poly]; ys=[p[1] for p in poly]
    pad=6
    box=(int(min(xs)-pad),int(min(ys)-pad),int(max(xs)+pad),int(max(ys)+pad))
    c=flat.crop(box)
    # letterbox to square so aspect ratio itself leaks nothing
    s=max(c.size); sq=Image.new('RGB',(s,s),(128,128,128))
    sq.paste(c,((s-c.width)//2,(s-c.height)//2))
    sq.resize((size,size)).save(out,quality=95)
    return A

def landmarks(path):
    im=Image.open(path).convert('RGB'); W,H=im.size
    r=fl().detect(mp.Image(image_format=mp.ImageFormat.SRGB,data=np.asarray(im)))
    if not r.face_landmarks: return None
    return np.array([[l.x*W,l.y*H] for l in r.face_landmarks[0]])

def norm(A):
    A=A-A.mean(0)
    return A/np.sqrt((A**2).sum(1).mean())

def dist(A,B):
    """Procrustes-aligned mean RMS landmark distance."""
    A,B=norm(A),norm(B)
    U,_,Vt=np.linalg.svd(A.T@B)
    R=U@Vt
    return np.sqrt(((A@R-B)**2).sum(1)).mean()
