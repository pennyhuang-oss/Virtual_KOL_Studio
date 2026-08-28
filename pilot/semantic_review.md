# 語意覆核清單 — Nico Pilot Phase C

> 資料 hash：`eeefb24eef7968c6`　|　20 列　|　**逐列 hash**：改一列只失效那一列，其餘核可保留
> **機器 lint 已通過不代表語意正確。** 逐列確認「scene 這句話」與右邊每個結構欄位是否真的相容。
> 覆核完成後把 `pilot/semantic_review.json` 的 `reviewed_shot_ids` 填滿並記錄 `data_hash`。
> 資料一改 hash 就變，舊的覆核紀錄自動失效。

### nico_a01　`9009c79ff7dc`

**scene**：咖啡廳靠窗的位子坐著，正對鏡頭，沒有在做任何事

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `seated` | ☐ |
| framing | `face_closeup` | ☐ |
| head_yaw / pitch | `front` / `neutral` | ☐ |
| eye_gaze | `camera` | ☐ |
| view | `third_person` | ☐ |
| expression | `neutral_relaxed` | ☐ |
| outfit | `nico_outfit_01` — ★極簡職人（high mock neck）| ☐ |
| hair | `nico_hair_01` — 短鮑伯自然放下，一側塞耳後，髮尾內彎 | ☐ |
| location | `local_cafe` | ☐ |
| light | `L2_single_window_daylight` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `window_mist` | 窗玻璃上凝結的水氣（background・zone=background・可見=True）| ☐ |
| prop `bar_dripper` | 身後吧台上的手沖濾杯架（background・zone=background・可見=True）| ☐ |
| hands.left | `free`（放在桌面上，在裁切外）| ☐ |
| hands.right | `free`（放在桌面上，在裁切外）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_a02　`925986eead60`

**scene**：同一個位子，身體轉向左邊，臉轉回鏡頭，手上端著咖啡杯

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `seated` | ☐ |
| framing | `chest_up` | ☐ |
| head_yaw / pitch | `left_30` / `neutral` | ☐ |
| eye_gaze | `camera` | ☐ |
| view | `third_person` | ☐ |
| expression | `soft_smile` | ☐ |
| outfit | `nico_outfit_01` — ★極簡職人（high mock neck）| ☐ |
| hair | `nico_hair_01` — 短鮑伯自然放下，一側塞耳後，髮尾內彎 | ☐ |
| location | `local_cafe` | ☐ |
| light | `L2_single_window_daylight` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `cup_a02` | 白瓷咖啡杯（held_right・zone=chest・可見=True）| ☐ |
| prop `menu_board` | 身後牆上的木質菜單板（background・zone=background・可見=True）| ☐ |
| hands.left | `free`（放在桌面上）| ☐ |
| hands.right | `holding`→`cup_a02`（端在胸前）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_a03　`a5af170879c8`

**scene**：白天的人行道上站著，身體轉向右邊，臉轉回鏡頭，手上端著外帶杯

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `standing` | ☐ |
| framing | `chest_up` | ☐ |
| head_yaw / pitch | `right_30` / `neutral` | ☐ |
| eye_gaze | `camera` | ☐ |
| view | `third_person` | ☐ |
| expression | `neutral_relaxed` | ☐ |
| outfit | `nico_outfit_01` — ★極簡職人（high mock neck）| ☐ |
| hair | `nico_hair_02` — 短鮑伯全部塞到雙耳後，露出雙耳與後頸 | ☐ |
| location | `city_street` | ☐ |
| light | `L6_soft_overcast` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `togo_a03` | 外帶咖啡杯（held_right・zone=chest・可見=True）| ☐ |
| prop `scooter_mirror` | 身後路邊停放的機車後照鏡（background・zone=background・可見=True）| ☐ |
| hands.left | `free`（自然垂在身側）| ☐ |
| hands.right | `holding`→`togo_a03`（端在胸前）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_a04　`7528502ca941`

**scene**：同一段人行道，身體較大幅度轉向左側，手上端著外帶杯

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `standing` | ☐ |
| framing | `chest_up` | ☐ |
| head_yaw / pitch | `left_60` / `neutral` | ☐ |
| eye_gaze | `away` | ☐ |
| view | `third_person` | ☐ |
| expression | `listening_attentive` | ☐ |
| outfit | `nico_outfit_03` — 日常有型（crew neck）| ☐ |
| hair | `nico_hair_01` — 短鮑伯自然放下，一側塞耳後，髮尾內彎 | ☐ |
| location | `city_street` | ☐ |
| light | `L6_soft_overcast` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `togo_a04` | 外帶咖啡杯（held_right・zone=chest・可見=True）| ☐ |
| prop `rent_flyer` | 騎樓柱子上的租屋紅單（background・zone=background・可見=True）| ☐ |
| hands.left | `free`（自然垂在身側）| ☐ |
| hands.right | `holding`→`togo_a04`（端在胸前）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_a05　`cc5d5e8e02a9`

**scene**：公園長椅上坐著，身體較大幅度轉向右側，手上拿著保溫瓶

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `seated` | ☐ |
| framing | `chest_up` | ☐ |
| head_yaw / pitch | `right_60` / `neutral` | ☐ |
| eye_gaze | `away` | ☐ |
| view | `third_person` | ☐ |
| expression | `mid_conversation` | ☐ |
| outfit | `nico_outfit_03` — 日常有型（crew neck）| ☐ |
| hair | `nico_hair_02` — 短鮑伯全部塞到雙耳後，露出雙耳與後頸 | ☐ |
| location | `park` | ☐ |
| light | `L6_soft_overcast` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `bottle_a05` | 保溫瓶（held_right・zone=chest・可見=True）| ☐ |
| prop `park_lamp` | 身後的公園路燈桿（background・zone=background・可見=True）| ☐ |
| hands.left | `supporting`（撐在長椅椅面上）| ☐ |
| hands.right | `holding`→`bottle_a05`（拿在胸前）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_a06　`72cfb7cda02e`

**scene**：公園步道上站著，正對鏡頭，雙手自然垂下

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `standing` | ☐ |
| framing | `full_body` | ☐ |
| head_yaw / pitch | `front` / `neutral` | ☐ |
| eye_gaze | `camera` | ☐ |
| view | `third_person` | ☐ |
| expression | `neutral_relaxed` | ☐ |
| outfit | `nico_outfit_03` — 日常有型（crew neck）| ☐ |
| hair | `nico_hair_01` — 短鮑伯自然放下，一側塞耳後，髮尾內彎 | ☐ |
| location | `park` | ☐ |
| light | `L6_soft_overcast` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `bottle_a06` | 腳邊步道上放著的保溫瓶（surface・zone=floor・可見=True）| ☐ |
| prop `yellow_post` | 步道旁的黃色分隔柱（background・zone=background・可見=True）| ☐ |
| hands.left | `free`（自然垂在身側）| ☐ |
| hands.right | `free`（自然垂在身側）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_a07　`5ce37fee9aa8`

**scene**：同一條步道，身體轉向右側四分之三，臉轉回鏡頭

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `standing` | ☐ |
| framing | `full_body` | ☐ |
| head_yaw / pitch | `right_30` / `neutral` | ☐ |
| eye_gaze | `camera` | ☐ |
| view | `third_person` | ☐ |
| expression | `soft_smile` | ☐ |
| outfit | `nico_outfit_01` — ★極簡職人（high mock neck）| ☐ |
| hair | `nico_hair_04` — 中分吹整、髮尾微內扣，比平時整齊 | ☐ |
| location | `park` | ☐ |
| light | `L6_soft_overcast` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `bottle_a07` | 保溫瓶（held_right・zone=hip・可見=True）| ☐ |
| prop `trash_bin` | 步道邊的鐵製垃圾桶（background・zone=background・可見=True）| ☐ |
| hands.left | `free`（自然垂在身側）| ☐ |
| hands.right | `holding`→`bottle_a07`（垂在身側提著）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c01　`f76ead301b5e`

**scene**：收工後鐵門拉下，坐在工作椅上轉過來看側窗外

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `seated` | ☐ |
| framing | `face_closeup` | ☐ |
| head_yaw / pitch | `front` / `neutral` | ☐ |
| eye_gaze | `away` | ☐ |
| view | `third_person` | ☐ |
| expression | `neutral_composed` | ☐ |
| outfit | `nico_outfit_08` — 居家貼身（modest scoop neck）| ☐ |
| hair | `nico_hair_01` — 短鮑伯自然放下，一側塞耳後，髮尾內彎 | ☐ |
| location | `workplace_own_studio` | ☐ |
| light | `L2_single_window_daylight` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `window_plant` | 窗台上的一盆小綠植（background・zone=background・可見=True）| ☐ |
| prop `hours_sign` | 牆上掛的營業時間牌（background・zone=background・可見=True）| ☐ |
| hands.left | `free`（搭在椅背上，在裁切外）| ☐ |
| hands.right | `free`（放在大腿上，在裁切外）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c02　`f302be244680`

**scene**：蹲在地上拆剛到的材料紙箱，抬頭看向門口

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `crouching` | ☐ |
| framing | `knee_up` | ☐ |
| head_yaw / pitch | `left_30` / `up_10` | ☐ |
| eye_gaze | `away` | ☐ |
| view | `third_person` | ☐ |
| expression | `mildly_surprised` | ☐ |
| outfit | `nico_outfit_06` — 上班正式（square neckline camisole under blazer）| ☐ |
| hair | `nico_hair_04` — 中分吹整、髮尾微內扣，比平時整齊 | ☐ |
| location | `workplace_own_studio` | ☐ |
| light | `L2_single_window_daylight` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `box_cutter` | 美工刀（held_right・zone=knee・可見=True）| ☐ |
| prop `open_box` | 地上拆開一半的紙箱（surface・zone=knee・可見=True）| ☐ |
| hands.left | `supporting`（扶著紙箱邊緣）| ☐ |
| hands.right | `holding`→`box_cutter`（拿著美工刀）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c03　`3135370de382`

**scene**：早餐店的板凳上等餐，手肘擱在桌沿

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `seated` | ☐ |
| framing | `waist_up` | ☐ |
| head_yaw / pitch | `right_30` / `down_15` | ☐ |
| eye_gaze | `down` | ☐ |
| view | `third_person` | ☐ |
| expression | `tired_soft` | ☐ |
| outfit | `nico_outfit_03` — 日常有型（crew neck）| ☐ |
| hair | `nico_hair_04` — 中分吹整、髮尾微內扣，比平時整齊 | ☐ |
| location | `breakfast_shop` | ☐ |
| light | `L2_single_window_daylight` / bounce=specular | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `soy_milk` | 塑膠杯裝的豆漿（surface・zone=waist・可見=True）| ☐ |
| prop `number_tag` | 桌上的號碼牌（surface・zone=waist・可見=True）| ☐ |
| hands.left | `free`（手肘擱在桌沿，手掌鬆開）| ☐ |
| hands.right | `free`（放在膝上）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c04　`4a6326aeec6a`

**scene**：剛洗完澡坐在床邊，舉起手機直視鏡頭

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `seated` | ☐ |
| framing | `waist_up` | ☐ |
| head_yaw / pitch | `front` / `down_15` | ☐ |
| eye_gaze | `camera` | ☐ |
| view | `selfie_front` | ☐ |
| expression | `post_shower_calm` | ☐ |
| outfit | `nico_outfit_08` — 居家貼身（modest scoop neck）| ☐ |
| hair | `nico_hair_06` — 剛洗完澡的濕髮，自然往後貼，髮尾滴水 | ☐ |
| location | `own_bedroom` | ☐ |
| light | `L2_single_window_daylight` / bounce=diffuse | ☐ |
| face_visibility | `partial_hair` | ☐ |
| prop `quilt` | 身旁沒疊好的薄被（surface・zone=waist・可見=True）| ☐ |
| prop `water_glass` | 床頭櫃上的玻璃水杯（surface・zone=waist・可見=True）| ☐ |
| hands.left | `camera`（舉著手機（拍攝裝置））| ☐ |
| hands.right | `free`（撐在床沿）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c05　`4ceb1fc8c7ca`

**scene**：玄關靠著牆，低頭把鑰匙收進口袋

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `leaning` | ☐ |
| framing | `knee_up` | ☐ |
| head_yaw / pitch | `left_60` / `down_15` | ☐ |
| eye_gaze | `down` | ☐ |
| view | `third_person` | ☐ |
| expression | `focused` | ☐ |
| outfit | `nico_outfit_04` — 學院感（collared button-down, top two buttons open）| ☐ |
| hair | `nico_hair_05` — 髮尾用電棒外翹，右側夾一支銀色細髮夾 | ☐ |
| location | `own_entryway` | ☐ |
| light | `L3_mixed_warm_cool_practical` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `keys` | 鑰匙（held_right・zone=waist・可見=True）| ☐ |
| prop `succulent` | 鞋櫃上的一盆多肉（surface・zone=waist・可見=True）| ☐ |
| hands.left | `supporting`（撐在牆上）| ☐ |
| hands.right | `holding`→`keys`（拿著鑰匙）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c06　`98ec559397c5`

**scene**：大安區巷子裡走路，剛越過一台停在牆邊的機車

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `walking_frozen` | ☐ |
| framing | `full_body` | ☐ |
| head_yaw / pitch | `right_60` / `neutral` | ☐ |
| eye_gaze | `away` | ☐ |
| view | `third_person` | ☐ |
| expression | `neutral_walking` | ☐ |
| outfit | `nico_outfit_03` — 日常有型（crew neck）| ☐ |
| hair | `nico_hair_05` — 髮尾用電棒外翹，右側夾一支銀色細髮夾 | ☐ |
| location | `city_street` | ☐ |
| light | `L6_soft_overcast` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `drink_c06` | 手搖杯（held_right・zone=hip・可見=True）| ☐ |
| prop `meter_box` | 巷口的電表箱（background・zone=background・可見=True）| ☐ |
| hands.left | `free`（自然擺動）| ☐ |
| hands.right | `holding`→`drink_c06`（提在身側）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c07　`6111a006e0a0`

**scene**：低頭在展示棒上試新的色膠，側臉朝向鏡頭

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `seated` | ☐ |
| framing | `chest_up` | ☐ |
| head_yaw / pitch | `profile_left` / `down_15` | ☐ |
| eye_gaze | `down` | ☐ |
| view | `third_person` | ☐ |
| expression | `focused` | ☐ |
| outfit | `nico_outfit_01` — ★極簡職人（high mock neck）| ☐ |
| hair | `nico_hair_03` — 鯊魚夾把後半部夾起，前側留兩撮碎髮（工作時） | ☐ |
| location | `workplace_own_studio` | ☐ |
| light | `L3_mixed_warm_cool_practical` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `tip_stick` | 甲片展示棒（held_left・zone=chest・可見=True）| ☐ |
| prop `color_board` | 身後牆上的美甲色卡板（background・zone=background・可見=True）| ☐ |
| prop `gel_brush` | 上膠筆（held_right・zone=chest・可見=True）| ☐ |
| hands.left | `holding`→`tip_stick`（固定著甲片展示棒）| ☐ |
| hands.right | `holding`→`gel_brush`（拿著上膠筆）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c08　`8e72e5be7825`

**scene**：浴室鏡前修眉，另一手舉著手機對著鏡子拍

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `standing` | ☐ |
| framing | `waist_up` | ☐ |
| head_yaw / pitch | `left_30` / `up_10` | ☐ |
| eye_gaze | `mirror` | ☐ |
| view | `selfie_mirror` | ☐ |
| expression | `concentrating_slight_frown` | ☐ |
| outfit | `nico_outfit_08` — 居家貼身（modest scoop neck）| ☐ |
| hair | `nico_hair_02` — 短鮑伯全部塞到雙耳後，露出雙耳與後頸 | ☐ |
| location | `own_bathroom` | ☐ |
| light | `L8_bathroom_fluorescent` / bounce=diffuse | ☐ |
| face_visibility | `partial_hand` | ☐ |
| prop `brow_razor` | 修眉刀（held_right・zone=head・可見=True）| ☐ |
| prop `cleanser` | 台面上倒著的洗面乳（surface・zone=waist・可見=True）| ☐ |
| hands.left | `camera`（舉著手機對鏡子（拍攝裝置））| ☐ |
| hands.right | `holding`→`brow_razor`（拿著修眉刀靠近眉尾）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c09　`2d197e3c191a`

**scene**：便利商店的雜誌架前蹲下來看最下層，回頭

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `crouching` | ☐ |
| framing | `knee_up` | ☐ |
| head_yaw / pitch | `left_30` / `up_10` | ☐ |
| eye_gaze | `camera` | ☐ |
| view | `third_person` | ☐ |
| expression | `mildly_annoyed` | ☐ |
| outfit | `nico_outfit_05` — 街頭（crew neck, cropped hem）| ☐ |
| hair | `nico_hair_02` — 短鮑伯全部塞到雙耳後，露出雙耳與後頸 | ☐ |
| location | `convenience_store` | ☐ |
| light | `L1_single_ugly_overhead` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `basket_c09` | 放在腳邊的購物籃（surface・zone=knee・可見=True）| ☐ |
| prop `onigiri` | 飯糰（held_right・zone=chest・可見=True）| ☐ |
| hands.left | `supporting`（扶著雜誌架下層）| ☐ |
| hands.right | `holding`→`onigiri`（拿著飯糰）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c10　`00e8ad7f9e48`

**scene**：自助洗衣店裡把烘好的衣物從滾筒抱出來，站在機台前

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `standing` | ☐ |
| framing | `full_body` | ☐ |
| head_yaw / pitch | `right_30` / `neutral` | ☐ |
| eye_gaze | `away` | ☐ |
| view | `third_person` | ☐ |
| expression | `neutral_composed` | ☐ |
| outfit | `nico_outfit_09` — 雨天機能（high round neck）| ☐ |
| hair | `nico_hair_04` — 中分吹整、髮尾微內扣，比平時整齊 | ☐ |
| location | `laundromat` | ☐ |
| light | `L1_single_ugly_overhead` / bounce=specular | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `laundry` | 抱在懷裡烘好的衣物（held_both・zone=chest・可見=True）| ☐ |
| prop `coin_tray` | 機台上的零錢盤（surface・zone=waist・可見=True）| ☐ |
| hands.left | `holding`→`laundry`（與另一手一起抱著）| ☐ |
| hands.right | `holding`→`laundry`（與另一手一起抱著）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c11　`75b4ca95359c`

**scene**：藥妝店貨架前拿護手霜比較成分

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `standing` | ☐ |
| framing | `knee_up` | ☐ |
| head_yaw / pitch | `front` / `down_15` | ☐ |
| eye_gaze | `down` | ☐ |
| view | `third_person` | ☐ |
| expression | `reading_focused` | ☐ |
| outfit | `nico_outfit_05` — 街頭（crew neck, cropped hem）| ☐ |
| hair | `nico_hair_05` — 髮尾用電棒外翹，右側夾一支銀色細髮夾 | ☐ |
| location | `pharmacy` | ☐ |
| light | `L1_single_ugly_overhead` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `hand_creams` | 兩罐護手霜（held_both・zone=chest・可見=True）| ☐ |
| prop `basket_c11` | 掛在手肘的購物籃（worn・zone=waist・可見=True）| ☐ |
| hands.left | `holding`→`hand_creams`（拿著一罐）| ☐ |
| hands.right | `holding`→`hand_creams`（拿著另一罐）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_c12　`d38996201490`

**scene**：捷運月台等車，看著對面的到站顯示

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `standing` | ☐ |
| framing | `waist_up` | ☐ |
| head_yaw / pitch | `right_30` / `up_10` | ☐ |
| eye_gaze | `away` | ☐ |
| view | `third_person` | ☐ |
| expression | `blank_waiting` | ☐ |
| outfit | `nico_outfit_06` — 上班正式（square neckline camisole under blazer）| ☐ |
| hair | `nico_hair_04` — 中分吹整、髮尾微內扣，比平時整齊 | ☐ |
| location | `train_platform` | ☐ |
| light | `L3_mixed_warm_cool_practical` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `easycard` | 悠遊卡（held_right・zone=waist・可見=True）| ☐ |
| prop `arrival_board` | 月台上的到站顯示器（background・zone=background・可見=True）| ☐ |
| hands.left | `free`（自然垂在身側）| ☐ |
| hands.right | `holding`→`easycard`（拿著悠遊卡）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）

### nico_a08　`4091f47cd339`

**scene**：公園步道旁站著，整個身體與臉都轉向右側，看著遠處

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `standing` | ☐ |
| framing | `chest_up` | ☐ |
| head_yaw / pitch | `profile_right` / `neutral` | ☐ |
| eye_gaze | `away` | ☐ |
| view | `third_person` | ☐ |
| expression | `calm_distant` | ☐ |
| outfit | `nico_outfit_02` — 極休閒（straight neckline spaghetti strap）| ☐ |
| hair | `nico_hair_02` — 短鮑伯全部塞到雙耳後，露出雙耳與後頸 | ☐ |
| location | `park` | ☐ |
| light | `L6_soft_overcast` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |
| prop `wood_bench` | 身後步道旁的木製長椅（background・zone=background・可見=True）| ☐ |
| prop `falling_leaf` | 肩線後方一片正在飄落的葉子（background・zone=background・可見=True）| ☐ |
| hands.left | `free`（自然垂在身側）| ☐ |
| hands.right | `free`（自然垂在身側）| ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節｜**改了時間狀態（剛醒／剛洗完澡）卻沒同步 expression 與 hair**｜**zone=background 的物件實際上不在構圖內**（機器驗不出來，只能靠這一關）
