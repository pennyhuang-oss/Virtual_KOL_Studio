# M-4 R24：V-Rainie 回歸人設，改用早期成功的身分流程：Seedream 4.5＋既有 Reference Element（錨點 v2，只提供身分）。
# 依 canon（profile.json identity.appearance、character.md）重新設計場景、服裝、動作；R20–R23 圖片不作任何輸入或範本。
# 不寫人物占滿畫高、腳靠下緣、身高三圍數字；兩張都是朋友在合理距離平視拍的全身照（非自拍透視）。
ANCHOR = '<<<ANCHOR>>>'   # 送出時換成既有 Element ID（只留在私有紀錄）
IDENT = (ANCHOR + ' as a 24-year-old adult Taiwanese woman with fair, luminous skin and an hourglass figure, a full bust, a cinched waist, '
         'curved hips and long legs, her long straight jet-black hair sleek and glossy with a deep side part; '
         'barely-there soft brown eyeliner close to the lash line with no wing, and a sheer natural tinted lip balm.')
WEAR = 'She wears a fitted champagne satin midi dress with a thigh-high slit, gold statement drop earrings and strappy gold high heels.'
SETTING = ('Setting: a rooftop terrace in Taipei on a warm May evening just before sunset, a glass railing, potted olive trees and low lounge chairs, '
           'the city skyline soft in the haze behind her, nobody else around.')
LIGHT = 'Warm low sunlight from the side, soft and even on her face, a gentle golden glow across the terrace.'
END = 'A natural, realistic photograph with natural adult body proportions.'
S = {
 'A': dict(change='自然站姿：在露台欄杆邊放鬆站著、重心在一腳、一手輕放欄杆，看鏡頭微笑（全身）',
           moment='She stands relaxed by the railing with her weight on one leg and one hand resting lightly on the rail, smiling at the camera.',
           camera='A full-length photograph taken by a friend standing about five metres away with a 50mm lens at chest height, level, showing her whole figure from head to heels with space around her, natural perspective, vertical 3:4.'),
 'B': dict(change='自然行走：走過露台朝鏡頭走來、雙手自然放鬆，看鏡頭微笑（全身）',
           moment='She walks across the terrace toward the camera mid-stride, her arms relaxed at her sides, smiling at the camera.',
           camera='A full-length photograph taken by a friend standing about six metres away with a 50mm lens at chest height, level, showing her whole figure from head to heels with space around her, natural perspective, vertical 3:4.'),
}
NOTE = ('回歸 canon：成年、貼身緞面洋裝＋大腿高衩、誇張金飾、高跟鞋（style_vibe）；黑長直髮側分、近乎無痕的淺棕眼線不上揚、透亮唇彩（face_type／eyes）；沙漏身材與長腿（figure、腿長占比）。'
        '5 月傍晚的台北頂樓露台，符合她夜生活出門前的角色風格；場景簡單可信。身分只由既有錨點 Element v2 提供；不使用 R20–R23 任何圖片。')
