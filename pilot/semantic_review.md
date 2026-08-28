# 語意覆核清單 — Nico Pilot Phase C

> 資料 hash：`edcacbc59355a286`　|　20 列
> **機器 lint 已通過不代表語意正確。** 逐列確認「scene 這句話」與右邊每個結構欄位是否真的相容。
> 覆核完成後把 `pilot/semantic_review.json` 的 `reviewed_shot_ids` 填滿並記錄 `data_hash`。
> 資料一改 hash 就變，舊的覆核紀錄自動失效。

### nico_a01

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_a02

**scene**：同一個位子，身體轉向左邊，臉轉回鏡頭

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_a03

**scene**：白天的人行道上站著，身體轉向右邊，臉轉回鏡頭

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_a04

**scene**：同一段人行道，身體較大幅度轉向左側

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_a05

**scene**：公園長椅上坐著，身體較大幅度轉向右側

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_a06

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_a07

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c01

**scene**：鐵門拉下後，坐在工作椅上轉過來看窗外，手還搭在椅背

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c02

**scene**：蹲在地上拆剛到的材料紙箱，抬頭看向門口

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `crouching` | ☐ |
| framing | `chest_up` | ☐ |
| head_yaw / pitch | `left_30` / `up_10` | ☐ |
| eye_gaze | `away` | ☐ |
| view | `third_person` | ☐ |
| expression | `mildly_surprised` | ☐ |
| outfit | `nico_outfit_06` — 上班正式（square neckline camisole under blazer）| ☐ |
| hair | `nico_hair_04` — 中分吹整、髮尾微內扣，比平時整齊 | ☐ |
| location | `workplace_own_studio` | ☐ |
| light | `L2_single_window_daylight` / bounce=diffuse | ☐ |
| face_visibility | `unobstructed` | ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c03

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c04

**scene**：床邊坐著，剛醒還沒站起來，低頭看手機

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `seated` | ☐ |
| framing | `waist_up` | ☐ |
| head_yaw / pitch | `front` / `down_15` | ☐ |
| eye_gaze | `camera` | ☐ |
| view | `selfie_front` | ☐ |
| expression | `just_woken_blank` | ☐ |
| outfit | `nico_outfit_08` — 居家貼身（modest scoop neck）| ☐ |
| hair | `nico_hair_06` — 剛洗完澡的濕髮，自然往後貼，髮尾滴水 | ☐ |
| location | `own_bedroom` | ☐ |
| light | `L2_single_window_daylight` / bounce=diffuse | ☐ |
| face_visibility | `partial_hair` | ☐ |

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c05

**scene**：玄關穿鞋，一手扶著牆

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c06

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c07

**scene**：低頭替客人上膠，側臉朝向鏡頭

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c08

**scene**：浴室鏡前修眉，另一手撐著洗手台

| 欄位 | 值 | 與 scene 相容？ |
|------|----|----------------|
| body_pose | `leaning` | ☐ |
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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c09

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c10

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c11

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_c12

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節

### nico_a08

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

**常見矛盾**：scene 說坐／站／蹲但 body_pose 不同｜scene 說看鏡頭但 eye_gaze=away｜室內場景配戶外光線家族｜自拍卻用 phone_rear｜full_body 卻寫臉部細節
