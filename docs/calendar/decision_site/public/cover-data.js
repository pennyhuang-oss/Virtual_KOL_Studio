// 程式產生（docs/calendar/tools/build_cal_decision_site.py），不要手改。排版頁（layout.html）封面比較區的資料，來源 docs/calendar/data/cal_m5_cover_r27.json、cal_m5_r27_trial.json、cal_cover_r27_page.json 與 M-5 R28 的 cal_m5_r28_*.json、cal_cover_r28_page.json
window.CAL_COVER = {
 "accepted": {
  "items": [
   "橫式照片框：完整 16:9（192×108 mm）",
   "橫式排版：接受推薦排法",
   "直式排版：接受推薦排法"
  ],
  "scope": "排版接受不等於交印核准；廠商規格、打樣與印刷色彩仍待確認。24 張月面照片與內頁不動。",
  "title": "內頁排版：你已接受（R27 紀錄）"
 },
 "cards": {
  "H": [
   {
    "checks": [
     {
      "item": "恰好 12 人，無重複、漏人或額外人物",
      "note": "12 人；髮色各不相同，無重複或額外人物",
      "result": "通過"
     },
     {
      "item": "每位臉部可辨識，與對照表對應",
      "note": "部分相符 9、不符 2（Yerin、Coco）、無法判定 1（Somi）；相符 0",
      "result": "未通過"
     },
     {
      "item": "沒有串臉、換人、多人長同一張臉",
      "note": "Coco 換成另一位不同族裔的人；Yerin 髮型與臉型改變；多位臉型與笑容趨同",
      "result": "未通過"
     },
     {
      "item": "人體比例、手腳、遮擋與接觸合理",
      "note": "未見多手多腳或錯位；坐、站、席地的接觸合理",
      "result": "通過"
     },
     {
      "item": "服裝同系列，人物仍有個性",
      "note": "象牙白／燕麥色同系列，緞面洋裝、西裝、裙裝、長褲剪裁各異",
      "result": "通過"
     },
     {
      "item": "真正是同場團體寫真，光線與空間一致",
      "note": "同一棚景，窗光方向與地面陰影一致",
      "result": "通過"
     },
     {
      "item": "整張有封面吸引力，縮到成品尺寸仍可讀",
      "note": "左右展開、高低自然；上方約三分之一乾淨牆面放標題",
      "result": "通過"
     }
    ],
    "counts": {
     "不符": 2,
     "無法判定": 1,
     "相符": 0,
     "部分相符": 9
    },
    "dir": "A",
    "dir_zh": "象牙白日光棚景",
    "flagged": [
     {
      "grade": "不符",
      "name": "Yerin"
     },
     {
      "grade": "不符",
      "name": "Coco"
     },
     {
      "grade": "無法判定",
      "name": "Somi"
     }
    ],
    "id": "H-A",
    "ids": {
     "h": 790,
     "src": "cover/ids_H-A.jpg",
     "w": 1810
    },
    "page": {
     "full": {
      "h": 1831,
      "src": "cover/cover_H-A_f.jpg",
      "w": 2409
     },
     "view": {
      "h": 916,
      "src": "cover/cover_H-A_v.jpg",
      "w": 1204
     }
    },
    "people": [
     {
      "grade": "部分相符",
      "name": "Yuna",
      "note": "髮型髮色相符；臉較圓、笑容不同，無法確認同一人"
     },
     {
      "grade": "部分相符",
      "name": "Rin",
      "note": "酒紅長髮相符；五官接近但不足以確認"
     },
     {
      "grade": "部分相符",
      "name": "Miu",
      "note": "淺金短髮與瀏海相符；臉型略圓"
     },
     {
      "grade": "部分相符",
      "name": "Tammy",
      "note": "金色長捲髮相符；五官接近但不足以確認"
     },
     {
      "grade": "不符",
      "name": "Yerin",
      "note": "多了厚瀏海、少了淺色挑染，臉型與五官不同"
     },
     {
      "grade": "不符",
      "name": "Coco",
      "note": "換成另一位不同族裔的人，與基準臉完全不同"
     },
     {
      "grade": "部分相符",
      "name": "Mia",
      "note": "灰棕捲髮與粉色挑染（少量）相符；五官接近但不足以確認"
     },
     {
      "grade": "部分相符",
      "name": "Iris",
      "note": "黑長髮相符；五官接近但不足以確認"
     },
     {
      "grade": "部分相符",
      "name": "Jia",
      "note": "深藍黑髮相符，但少了藍綠內層挑染；五官接近但不足以確認"
     },
     {
      "grade": "部分相符",
      "name": "Luna",
      "note": "黑色齊瀏海鮑伯相符，臉型接近"
     },
     {
      "grade": "無法判定",
      "name": "Somi",
      "note": "閉眼大笑，看不到眼睛"
     },
     {
      "grade": "部分相符",
      "name": "Rainie",
      "note": "黑長髮相符；眉眼特徵不明顯，無法確認"
     }
    ],
    "photo": {
     "h": 3584,
     "src": "cover/photo_H-A.jpg",
     "w": 4800
    },
    "verdict": "不可定案：12 人身分未能全部確認"
   },
   {
    "checks": [
     {
      "item": "恰好 12 人，無重複、漏人或額外人物",
      "note": "12 人；無重複或額外人物",
      "result": "通過"
     },
     {
      "item": "每位臉部可辨識，與對照表對應",
      "note": "部分相符 9、不符 0、無法判定 3（Iris、Jia、Somi）；相符 0",
      "result": "未通過"
     },
     {
      "item": "沒有串臉、換人、多人長同一張臉",
      "note": "沒有明顯換成他人；Yerin 多了瀏海、Coco 改成捲髮；多位臉型趨同",
      "result": "部分"
     },
     {
      "item": "人體比例、手腳、遮擋與接觸合理",
      "note": "左下多人腿部交疊，放大看歸屬大致合理但擁擠",
      "result": "部分"
     },
     {
      "item": "服裝同系列，人物仍有個性",
      "note": "香檳／象牙緞面同系列，剪裁各異",
      "result": "通過"
     },
     {
      "item": "真正是同場團體寫真，光線與空間一致",
      "note": "同一室內，暖色燈光一致",
      "result": "通過"
     },
     {
      "item": "整張有封面吸引力，縮到成品尺寸仍可讀",
      "note": "有坐有站、有互動；少量香檳杯與果盤，兩位舉杯稍像展示動作",
      "result": "部分"
     }
    ],
    "counts": {
     "不符": 0,
     "無法判定": 3,
     "相符": 0,
     "部分相符": 9
    },
    "dir": "B",
    "dir_zh": "香檳色聚會",
    "flagged": [
     {
      "grade": "無法判定",
      "name": "Iris"
     },
     {
      "grade": "無法判定",
      "name": "Jia"
     },
     {
      "grade": "無法判定",
      "name": "Somi"
     }
    ],
    "id": "H-B",
    "ids": {
     "h": 790,
     "src": "cover/ids_H-B.jpg",
     "w": 1810
    },
    "page": {
     "full": {
      "h": 1831,
      "src": "cover/cover_H-B_f.jpg",
      "w": 2409
     },
     "view": {
      "h": 916,
      "src": "cover/cover_H-B_v.jpg",
      "w": 1204
     }
    },
    "people": [
     {
      "grade": "部分相符",
      "name": "Yuna",
      "note": "髮型髮色相符；五官接近但不足以確認"
     },
     {
      "grade": "部分相符",
      "name": "Rin",
      "note": "酒紅長髮相符；臉較成熟，無法確認"
     },
     {
      "grade": "部分相符",
      "name": "Miu",
      "note": "淺金短髮與瀏海相符；唇形較厚"
     },
     {
      "grade": "部分相符",
      "name": "Tammy",
      "note": "金色長捲髮相符；五官接近但不足以確認"
     },
     {
      "grade": "部分相符",
      "name": "Yerin",
      "note": "多了瀏海；臉型接近但不足以確認"
     },
     {
      "grade": "部分相符",
      "name": "Coco",
      "note": "東亞臉、瀏海相符，但改成捲髮、頭部傾斜，無法確認"
     },
     {
      "grade": "部分相符",
      "name": "Mia",
      "note": "灰棕髮與粉色挑染相符；五官接近但不足以確認"
     },
     {
      "grade": "無法判定",
      "name": "Iris",
      "note": "大笑且側轉，眼睛半閉"
     },
     {
      "grade": "無法判定",
      "name": "Jia",
      "note": "側臉，只看到半邊"
     },
     {
      "grade": "部分相符",
      "name": "Luna",
      "note": "黑色齊瀏海鮑伯相符，臉型與眼型很接近"
     },
     {
      "grade": "無法判定",
      "name": "Somi",
      "note": "瞇眼大笑，看不清五官"
     },
     {
      "grade": "部分相符",
      "name": "Rainie",
      "note": "黑長髮與眉型接近；少了基準照的眼妝，無法確認"
     }
    ],
    "photo": {
     "h": 3584,
     "src": "cover/photo_H-B.jpg",
     "w": 4800
    },
    "verdict": "不可定案：12 人身分未能全部確認"
   }
  ],
  "V": [
   {
    "checks": [
     {
      "item": "恰好 12 人，無重複、漏人或額外人物",
      "note": "12 人；無重複或額外人物",
      "result": "通過"
     },
     {
      "item": "每位臉部可辨識，與對照表對應",
      "note": "部分相符 9、不符 2（Tammy、Rainie）、無法判定 1（Somi）；相符 0",
      "result": "未通過"
     },
     {
      "item": "沒有串臉、換人、多人長同一張臉",
      "note": "Tammy、Rainie 換成不同長相（膚色偏深、五官不同）",
      "result": "未通過"
     },
     {
      "item": "人體比例、手腳、遮擋與接觸合理",
      "note": "左緣一條腿與高跟鞋從 Miu 身後伸出、位置不自然；左右緣肢體太靠邊，會落在裁切／出血區",
      "result": "部分"
     },
     {
      "item": "服裝同系列，人物仍有個性",
      "note": "象牙白／燕麥色同系列",
      "result": "通過"
     },
     {
      "item": "真正是同場團體寫真，光線與空間一致",
      "note": "同一棚景，光線一致",
      "result": "通過"
     },
     {
      "item": "整張有封面吸引力，縮到成品尺寸仍可讀",
      "note": "前後三層高低清楚，不是橫圖裁直；上方留白足",
      "result": "通過"
     }
    ],
    "counts": {
     "不符": 2,
     "無法判定": 1,
     "相符": 0,
     "部分相符": 9
    },
    "dir": "A",
    "dir_zh": "象牙白日光棚景",
    "flagged": [
     {
      "grade": "不符",
      "name": "Tammy"
     },
     {
      "grade": "無法判定",
      "name": "Somi"
     },
     {
      "grade": "不符",
      "name": "Rainie"
     }
    ],
    "id": "V-A",
    "ids": {
     "h": 790,
     "src": "cover/ids_V-A.jpg",
     "w": 1810
    },
    "page": {
     "full": {
      "h": 2409,
      "src": "cover/cover_V-A_f.jpg",
      "w": 1701
     },
     "view": {
      "h": 1204,
      "src": "cover/cover_V-A_v.jpg",
      "w": 850
     }
    },
    "people": [
     {
      "grade": "部分相符",
      "name": "Yuna",
      "note": "髮型髮色相符；臉較寬，無法確認"
     },
     {
      "grade": "部分相符",
      "name": "Rin",
      "note": "酒紅長髮相符；五官接近但不足以確認"
     },
     {
      "grade": "部分相符",
      "name": "Miu",
      "note": "淺金短髮與瀏海相符；臉型略寬"
     },
     {
      "grade": "不符",
      "name": "Tammy",
      "note": "膚色偏深、五官與基準不同"
     },
     {
      "grade": "部分相符",
      "name": "Yerin",
      "note": "有淺色挑染但多了瀏海；臉型接近但不足以確認"
     },
     {
      "grade": "部分相符",
      "name": "Coco",
      "note": "東亞臉、瀏海相符，但髮型改成大捲，無法確認"
     },
     {
      "grade": "部分相符",
      "name": "Mia",
      "note": "灰棕髮與粉色挑染相符；頭部傾斜"
     },
     {
      "grade": "部分相符",
      "name": "Iris",
      "note": "黑長髮相符；五官接近但不足以確認"
     },
     {
      "grade": "部分相符",
      "name": "Jia",
      "note": "深藍黑髮與藍綠挑染相符；五官較銳利"
     },
     {
      "grade": "部分相符",
      "name": "Luna",
      "note": "黑色齊瀏海鮑伯相符，臉型接近"
     },
     {
      "grade": "無法判定",
      "name": "Somi",
      "note": "側轉大笑，看不到正臉"
     },
     {
      "grade": "不符",
      "name": "Rainie",
      "note": "膚色偏深、五官與基準不同"
     }
    ],
    "photo": {
     "h": 4800,
     "src": "cover/photo_V-A.jpg",
     "w": 3584
    },
    "verdict": "不可定案：12 人身分未能全部確認"
   },
   {
    "checks": [
     {
      "item": "恰好 12 人，無重複、漏人或額外人物",
      "note": "12 人；無重複或額外人物",
      "result": "通過"
     },
     {
      "item": "每位臉部可辨識，與對照表對應",
      "note": "部分相符 3、不符 1（Coco）、無法判定 8（Miu、Tammy、Yerin、Mia、Jia、Luna、Somi、Rainie）；相符 0",
      "result": "未通過"
     },
     {
      "item": "沒有串臉、換人、多人長同一張臉",
      "note": "Coco 換成另一位不同族裔的人",
      "result": "未通過"
     },
     {
      "item": "人體比例、手腳、遮擋與接觸合理",
      "note": "Jia 的腳伸到左緣裁切區；其餘坐姿合理",
      "result": "部分"
     },
     {
      "item": "服裝同系列，人物仍有個性",
      "note": "香檳／象牙緞面同系列",
      "result": "通過"
     },
     {
      "item": "真正是同場團體寫真，光線與空間一致",
      "note": "同一室內，燈光一致",
      "result": "通過"
     },
     {
      "item": "整張有封面吸引力，縮到成品尺寸仍可讀",
      "note": "互動自然、最像聚會瞬間；但多數臉側轉，封面上認不出是誰",
      "result": "部分"
     }
    ],
    "counts": {
     "不符": 1,
     "無法判定": 8,
     "相符": 0,
     "部分相符": 3
    },
    "dir": "B",
    "dir_zh": "香檳色聚會",
    "flagged": [
     {
      "grade": "無法判定",
      "name": "Miu"
     },
     {
      "grade": "無法判定",
      "name": "Tammy"
     },
     {
      "grade": "無法判定",
      "name": "Yerin"
     },
     {
      "grade": "不符",
      "name": "Coco"
     },
     {
      "grade": "無法判定",
      "name": "Mia"
     },
     {
      "grade": "無法判定",
      "name": "Jia"
     },
     {
      "grade": "無法判定",
      "name": "Luna"
     },
     {
      "grade": "無法判定",
      "name": "Somi"
     },
     {
      "grade": "無法判定",
      "name": "Rainie"
     }
    ],
    "id": "V-B",
    "ids": {
     "h": 790,
     "src": "cover/ids_V-B.jpg",
     "w": 1810
    },
    "page": {
     "full": {
      "h": 2409,
      "src": "cover/cover_V-B_f.jpg",
      "w": 1701
     },
     "view": {
      "h": 1204,
      "src": "cover/cover_V-B_v.jpg",
      "w": 850
     }
    },
    "people": [
     {
      "grade": "部分相符",
      "name": "Yuna",
      "note": "四分之三側臉；髮型髮色相符"
     },
     {
      "grade": "部分相符",
      "name": "Rin",
      "note": "四分之三側臉；酒紅長髮相符"
     },
     {
      "grade": "無法判定",
      "name": "Miu",
      "note": "接近側臉"
     },
     {
      "grade": "無法判定",
      "name": "Tammy",
      "note": "側轉、瞇眼笑"
     },
     {
      "grade": "無法判定",
      "name": "Yerin",
      "note": "側轉，多了瀏海"
     },
     {
      "grade": "不符",
      "name": "Coco",
      "note": "換成另一位不同族裔的人"
     },
     {
      "grade": "無法判定",
      "name": "Mia",
      "note": "側臉"
     },
     {
      "grade": "部分相符",
      "name": "Iris",
      "note": "四分之三側臉；黑長髮相符"
     },
     {
      "grade": "無法判定",
      "name": "Jia",
      "note": "側轉，藍綠挑染幾乎看不到"
     },
     {
      "grade": "無法判定",
      "name": "Luna",
      "note": "側臉且頭髮遮住"
     },
     {
      "grade": "無法判定",
      "name": "Somi",
      "note": "瞇眼大笑，看不清五官"
     },
     {
      "grade": "無法判定",
      "name": "Rainie",
      "note": "側臉"
     }
    ],
    "photo": {
     "h": 4800,
     "src": "cover/photo_V-B.jpg",
     "w": 3584
    },
    "verdict": "不可定案：12 人身分未能全部確認"
   }
  ]
 },
 "cover_note": "照片本身沒有文字；「2027」與 DESK CALENDAR 是本機排上去的，沒有放品牌或 Logo（品牌名稱未提供）。頁面含 2 mm 出血；開「參考線」可看裁切線、線圈假設區與安全區。",
 "feedback_key": "cal2027-cover-r27-v1",
 "formats": {
  "H": {
   "H": 155,
   "W": 204,
   "coil_assumed": 12,
   "safe": [
    4,
    12,
    200,
    151
   ],
   "safe_label": "廠商安全框",
   "trim": 2,
   "zh": "橫式"
  },
  "V": {
   "H": 204,
   "W": 144,
   "coil_assumed": 12,
   "safe": [
    5,
    12,
    139,
    199
   ],
   "safe_label": "文字安全區（本案自訂）",
   "trim": 2,
   "zh": "直式"
  }
 },
 "grades": [
  "相符",
  "部分相符",
  "不符",
  "無法判定"
 ],
 "history_label": "R26 排版回饋（你在這台裝置填過的內容，保留不動）",
 "intro": "R27 四張封面你已全部退回。這一輪只做一個技術測試：把 H-A 裡的 Coco 換回本人；不是完成的封面，H-A 也不代表你接受它的構圖。下面是你已接受的內頁排版。",
 "made": "4 張候選（橫式、直式各 A／B），每張 1 次生成；12 位用各自的身分參考圖一起送入。",
 "r26_cover_label": "R26 暫用封面（12 張縮圖；正式封面尚未決定）",
 "r27": {
  "feedback": [
   "橫式封面：都想修改（寫在備註）",
   "橫式備註：全部人臉都不符合，這算什麼團體封面照？怎麼會這樣？",
   "直式封面：都想修改（寫在備註）",
   "直式備註：全部人臉都不符合，這算什麼團體封面照？怎麼會這樣？"
  ],
  "label": "Owner 已退回",
  "note": "你的回饋原文已存檔；這 4 張不再提供選擇。",
  "title": "R27 封面候選（4 張，Owner 已全部退回）"
 },
 "round": "M-5 R28",
 "task": "TASK-CAL-001",
 "test": {
  "checks": [
   {
    "item": "Coco 是否可辨識為正式角色，不只髮色相近",
    "note": "臉型、眼睛、眉毛、鼻子、嘴形與笑容都和身分基準一致，連瀏海與髮夾都對；R27 原本是另一位不同族裔的人",
    "result": "通過"
   },
   {
    "item": "頭臉與髮際、頸部、光色及銳利度是否自然",
    "note": "髮際、頭髮邊緣、脖子銜接、左側光線方向與銳利度都自然、範圍邊界沒有重影；但臉是白皙膚色，胸口、右手、小腿只淡化成小麥色，放大看得出臉比身體白（封面尺寸不明顯）",
    "result": "部分"
   },
   {
    "item": "其餘 11 人、姿態、服裝、背景及構圖是否被改動",
    "note": "量測：裁切範圍外與遮罩外的像素完全沒變；Coco 的姿勢、頭部角度、衣服、項鍊、鞋子維持原樣",
    "result": "通過"
   },
   {
    "item": "全圖縮到封面尺寸是否仍自然好看",
    "note": "縮到成品 200 mm 寬時，Coco 和旁邊的人光線、清晰度一致，看不出是後製",
    "result": "通過"
   }
  ],
  "diff": "最後合成圖逐像素和原圖比：裁切範圍外改動 0 像素（共 15,615,600）、裁切內但回填範圍外改動 0 像素（共 1,099,622）；回填範圍約占全圖 2.8%。這是對最後合成圖的量測；生成工具本身在範圍外也有些微改動，那些像素沒有用到。",
  "feedback_key": "cal2027-cover-r28-v1",
  "imgs": {
   "after": {
    "full": {
     "h": 3584,
     "src": "cover28/r28_after_f.jpg",
     "w": 4800
    },
    "view": {
     "h": 1195,
     "src": "cover28/r28_after_v.jpg",
     "w": 1600
    }
   },
   "before": {
    "full": {
     "h": 3584,
     "src": "cover28/r28_before_f.jpg",
     "w": 4800
    },
    "view": {
     "h": 1195,
     "src": "cover28/r28_before_v.jpg",
     "w": 1600
    }
   },
   "crop_after": {
    "h": 1680,
    "src": "cover28/r28_crop_after.jpg",
    "w": 945
   },
   "crop_before": {
    "h": 1680,
    "src": "cover28/r28_crop_before.jpg",
    "w": 945
   },
   "diffmap": {
    "h": 1195,
    "src": "cover28/r28_diff_v.jpg",
    "w": 1600
   },
   "face": {
    "h": 396,
    "src": "cover28/r28_face_cmp.jpg",
    "w": 1100
   },
   "region": {
    "h": 1195,
    "src": "cover28/r28_region_v.jpg",
    "w": 1600
   }
  },
  "label": "單人身分測試，非完成封面",
  "not_finished": "完整 12 人流程沒有授權、也沒有開始；要不要做、怎麼做，等主管與你決定。",
  "note_label": "對這次 Coco 單人測試的備註（只記錄意見，不是接受封面）",
  "scope": "只重畫 Coco 一個人（頭髮臉部到胸口、右手、雙腿）；其他 11 人與背景沒有經過重新生成。H-A 只是測試底圖，不代表接受它的構圖、服裝或方向。",
  "title": "H-A 裡的 Coco：單人身分校正測試",
  "verdict": "未通過",
  "verdict_text": "依「任何一項不過就記失敗」：第 2 項膚色一致性只算部分通過，整體記失敗。可以確定的是：臉部身分這一項成功（第 1 項），範圍也確實只限 Coco 本人（第 3 項）。未繼續修其他人。"
 },
 "title": "2027 桌曆｜封面（單人身分測試）與排版"
};
