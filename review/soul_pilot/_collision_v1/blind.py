"""Build the hair-masked blind collision test.

Writes:
  blind_sheet.jpg   12 hair-masked faces labelled A..L in shuffled order
  ANSWER_KEY.json   the mapping, written ONCE and not printed
Prints only the tile labels, never which persona each one is.
"""
import json, random, sys
from PIL import Image, ImageDraw
import maskface as M

C='/home/user/Virtual_KOL_Studio/review/soul_pilot/cheryl-soh/verify_v1'
Z='/home/user/Virtual_KOL_Studio/review/soul_pilot/zhiyi-shen/verify_v1'
SPECS=['V1','V2','V3','V4','V5','V6']

items=[]
for who,d in (('cheryl',C),('zhiyi',Z)):
    for s in SPECS:
        p=f'{d}/{s}.png'
        out=f'blind_raw_{who}_{s}.jpg'
        if M.mask(p,out) is not None:
            items.append({'who':who,'spec':s,'file':out})

rng=random.Random(20260907)
rng.shuffle(items)
labels=[chr(ord('A')+i) for i in range(len(items))]
for lb,it in zip(labels,items): it['label']=lb

json.dump(items,open('ANSWER_KEY.json','w'),indent=1)

cols=6; rows=(len(items)+cols-1)//cols
s=Image.new('RGB',(300*cols,(300+26)*rows),'white'); d=ImageDraw.Draw(s)
for i,it in enumerate(items):
    x=300*(i%cols); y=(300+26)*(i//cols)
    d.text((x+6,y+6),it['label'],fill='black')
    s.paste(Image.open(it['file']),(x,y+26))
s.save('blind_sheet.jpg',quality=94)
print('tiles:',' '.join(labels))
print('count:',len(items))
