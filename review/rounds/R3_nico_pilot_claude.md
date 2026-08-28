# Nico Pilot — 第三輪覆核包（回應 ChatGPT R2）

> 給外部審閱者：自帶背景與**全部依賴檔案**，不需存取 repo。
> 產出：2026-08-27　|　commit `eac5aa2`　|　狀態：**尚未生成任何圖片**
>
> **本檔所有 count / ratio / distribution 均由 `tools/gen_pilot_review.py` 從 `nico_pilot.json` 自動計算，
> 沒有任何人工抄寫的統計數字。** 這是為了修掉 R2 被指出的問題：上一版統計與 JSON 漂移。

---

## 0. ChatGPT R2 主張的實測驗證

我逐項跑數字驗證，**它的數值主張全部正確**：

| ChatGPT R2 的主張 | 我實測 | 判定 |
|---|---|---|
| lighting family 是 6 種不是 5 種，L1 是 5 張不是 3 張（38.5%）| 完全正確 | ✅ |
| 場景集中度是 3 studio + 3 bedroom，不是我寫的 4+4 | 完全正確 | ✅ |
| 家＋工作室合計 9/13 = 69% | 完全正確 | ✅ |
| 2 張 full_body 只有 1 張 body_readable（c10 是防潑水外套）| 完全正確 | ✅ |
| 2 張 face_closeup 只有 1 張是乾淨 identity evidence（c13 是手機下打光）| 完全正確 | ✅ |
| `nico_outfit_08` 佔 4/13 = 30.8% | 完全正確 | ✅ |
| QA 門檻 14/18 允許 4 個維度都有可見漂移仍 PASS | 完全正確（4×1 + 5×2 = 14）| ✅ |
| 覆核包沒附 `location_registry.json`，validator 無法重現 | 完全正確，我只送了 3 個檔 | ✅ |
| validator 沒驗 Phase A / B / D | 完全正確 | ✅ |

**我又犯了一次同一類錯誤**：R2 我才剛修掉 scene/ID 的雙重真理來源，
結果統計數字在**文件層**又漂了一次——因為我是人工抄的。這一版的統計改成程式產生。

---

## 1. 我反駁的一點：訓練張數不是 20，是 5–20

ChatGPT 的 P0-1 認為官方 Help Center 已改成 minimum 20 photos，
要求先做 endpoint preflight。**我做了 preflight，結論與它相反。**

我直接讀本專案實際呼叫的 MCP 工具 schema（`show_characters(action='train')`），逐字內容是：

```
train (needs `name` + 5-20 ref images, ~10 min, non-blocking) / Required with medias to total 5-20 images for action=train
```

- **實際 endpoint 允許 5–20 張**，13 張完全合法。
- 公開 Help Center 的 20-photo flow 是 **Web UI 規格**，與本專案使用的 API endpoint 不同。
- ChatGPT 自己預留了這個可能性：「你們的 API schema 同時列出 prompt 與 medias，
  所以 API runtime 是否與 Web UI 完全相同，值得實測。」——實測結果就是不同。
- repo 歷史一致：`rainie-hsu` v2 就是用這支工具送 13 張成功訓練。

**但我仍然把張數提高了，理由不是規格逼的，是 ChatGPT §9–§11 指出的缺口是真的：**
只有 1 張乾淨全身身材證據、1 張乾淨臉部特寫、0 張乾淨右側角度——
而 Nico 的 identity marker 偏偏是右側的（右鼻翼小痣、左右眉尾不對稱）。
既然 endpoint 上限是 20，這個 headroom 應該用掉。

---

## 2. 這一版的結構（全部數字由程式計算）

**訓練集：19 張 = 7 張 clean identity anchor + 12 張 lifestyle coverage**

這正是 ChatGPT R2 §2 建議的結構——把它上一輪的 7 張 identity core 從「替代方案」
改成「20 張方案裡的 clean anchor 區」。我採用了。

### 2-1 修掉的缺口

| 項目 | R2 版 | 本版 | ChatGPT 的要求 |
|---|---|---|---|
| 乾淨臉部特寫 | 1 | **2** | ≥2 |
| 乾淨且 body_readable 的全身 | 1 | **3** | ≥2 |
| 乾淨右側高資訊角度 | 0 | **2** | ≥1 |
| `L1_single_ugly_overhead` | 5（38.5%）| **3**（16%）| 降到 2–3 |
| 家＋工作室集中度 | 9/13（69%）| **8/19（42%）** | 降低 |
| anchor 落在住處或職業空間 | — | **0/7** | 不要放 |

最後一列是我認為最關鍵的處理：**7 張 clean anchor 全部不在她的住處或工作室**
（分布在咖啡廳、人行道、公園）。這樣最強的身分訊號不會跟那兩個空間綁在一起，
即使 lifestyle 那 12 張仍有一定集中度。

### 2-2 完整分布

- **光線家族**：`L2_single_window_daylight` 6（32%）、`L6_soft_overcast` 6（32%）、`L3_mixed_warm_cool_practical` 3（16%）、`L1_single_ugly_overhead` 3（16%）、`L8_bathroom_fluorescent` 1（5%）
- **景別**：`chest_up` 6、`full_body` 4、`waist_up` 4、`knee_up` 3、`face_closeup` 2
- **頭部角度**：`front` 5、`right_30` 5、`left_30` 4、`left_60` 2、`right_60` 2、`profile_left` 1
- **身體姿態**：`standing` 10、`seated` 4、`crouching` 2、`leaning` 2、`walking_frozen` 1
- **視角**：`third_person` 17、`selfie_front` 1、`selfie_mirror` 1
- **濾鏡**：`none` 17、`ccd` 2（meitu = 0）
- **地點層級**：`B` 16、`C` 3
- **地點**：`city_street` 3、`park` 3、`workplace_own_studio` 3、`local_cafe` 2、`own_bedroom` 2、`own_kitchen` 1、`own_entryway` 1、`own_bathroom` 1、`laundromat` 1、`pharmacy` 1、`train_platform` 1
- **穿搭**：`nico_outfit_01` 7（37%）、`nico_outfit_03` 5（26%）、`nico_outfit_08` 4（21%）、`nico_outfit_09` 1（5%）、`nico_outfit_05` 1（5%）、`nico_outfit_06` 1（5%）
- **髮型**：`nico_hair_01` 7、`nico_hair_02` 4、`nico_hair_04` 3、`nico_hair_03` 3、`nico_hair_06` 1、`nico_hair_05` 1
- **表情種類**：14 種
- **career_related**：3/19（16%，上限 40%）
- **signature_family**：3/19（16%，上限 25%）

---

## 3. 其他接受並執行的 R2 建議

| ChatGPT R2 建議 | 執行 |
|---|---|
| 極端手機下打光（原 c13）不該在訓練集 | ✅ 移出訓練，改列 Phase D `st08b` |
| `imperfection_profile` 需要 `identity_safe` 限制 | ✅ 新增 `identity_safe` / `face_motion_blur` / `face_detail_preserved`；validator 強制訓練圖三者達標（可以歪、背景可以亂、燈管可以爆，但臉不能糊）|
| `signature_family` / `career_related` 應由 registry 推導 | ✅ registry 加 `defaults`，validator 比對推導值，要改必須填 `label_override_reason`。**它在我自己的資料裡抓到 `c01` 標錯**（收工後仍在工作室＝仍屬職業世界）|
| Phase A 不應宣稱「已完整確認臉＋身材」 | ✅ 改為「臉＋上半身／腰臀輪廓**初選**」，完整身材比例的 final gate 移到 Phase B 全身圖 |
| Phase B 第二張應做中度變量 | ✅ B2 改為不同 B 級場景 + 不同日常穿搭 + 不同髮型 + 正常自然光的 full_body |
| Phase D 缺乾淨基準線 | ✅ 新增 `st00` |
| st09 髮型變化應拆兩級 | ✅ `st09a` 中度、`st09b` 極端，且極端只在中度通過後才測 |
| QA 門檻 14/18 憑空訂且偏鬆 | ✅ **移除固定門檻**，改為 Retroactive Benchmark（見 §4）＋ 4 條 hard gate |
| identity marker 不要用 `2mm` 這種幾何單位 | ⚠️ 見 §5 未處理項 |
| 覆核包要附 registry / validator output / commit | ✅ 見 §6、§7 |
| 其餘 19 位不要現在遷移，但要真凍結 | ⚠️ 見 §5 未處理項 |

---

## 4. QA 門檻改用 Retroactive Benchmark

> 上一版寫 14/18 是我憑空訂的。而且 9 項每項至少 1 分時，4 項給 1 分 + 5 項給 2 分 = 14 剛好 PASS——四個維度都有可見漂移仍會通過，門檻太鬆。

**方法：Retroactive Benchmark**

1. 從 repo 已 ready 的 6 個 Soul 中，挑 1–2 個目前生產環境公認最好用的
1. 若有歷史上已知不好的 soul（例如 rainie-hsu 已 deprecated 的 994e33d2 舊 soul），一併測
1. 對它們跑同一套 Phase D 12 張與同一套 rubric
1. 得到 GOOD soul 的實際分數與 KNOWN-BAD soul 的實際分數
1. 用這個區間訂 Nico 的 gate——門檻變成『至少達到我們現在已經願意上線的角色品質』

**成本**：每個既有 soul 12 張，1–2 個 soul 共 12–24 張。比訓練完才發現門檻訂錯便宜太多。

**Hard gates（總分無法掩蓋的關鍵失敗）**：

- face_identity 在任一 identity_core 測項（st00–st05）為 0 → 整批 fail
- body_identity 在 st04（全身）或 st05（坐姿）為 0 → 整批 fail
- 出現明顯固定背景烙印（換場景仍冒出工作室或她的房間）→ 直接 fail
- 換裝後仍固定帶出 training garment → 直接 fail

**總分門檻**：**待定，不憑空訂。**

---

## 5. 我這一輪**沒有**處理的（誠實列出）

1. **identity marker 的 `2mm` 寫法還沒改。** ChatGPT 建議改成
   `left eyebrow tail sits subtly higher than the right, especially visible when she smiles`，
   並增加 1–2 個不依賴左右方向的骨相 marker（inter-eye distance / nose tip / jaw taper / philtrum）。
   我同意，但還沒動——因為改 marker 會影響 Phase A 的 prompt，想跟 prompt 定稿一起做。
2. **其餘 19 位還沒設 `status: blocked_pending_v2_pilot`**，也還沒產生 `v1_known_issues_report.json`。
   目前只是「文件上說凍結」，沒有機制上的硬阻擋。ChatGPT 說得對，這不是真凍結。
3. **跨 persona row fingerprint 檢查還沒寫**——目前只有一位 v2，無從比對。
   ChatGPT 也同意這個可以等 pilot 之後。
4. **validator 的 scene 衝突仍是 keyword guard 不是語意理解。** regex 漏字（T恤／上衣／鞋／靴／
   長髮／短髮／dress／skirt 等）我還沒補齊，`MULTI` 把「以及」當多時空觸發也可能誤殺。
   這一項本質上補不完，應定位為 heuristic lint，真正的語意審查靠人／LLM。

---

## 6. Validator 實際輸出

```
驗證 nico-tsai（schema v2.0.0）
  ✓ 全數通過
```

驗證器在本輪改動過程中，於**我自己剛寫的資料**裡抓到 3 次違規：
`c10` scene 出現「襯衫」觸發服裝詞攔截、`c01` 的 `career_related` 與 registry 推導不符、
Phase D 的 `count` 與實際 shots 數不符。全部已修。

---

## 7. 依賴檔案：`location_registry.json`（完整內容）

```json
{
  "_note": "地點層級不再由每列自由判斷。A/B/C 由本表決定；特殊情況可用 location_tier_override，但必須附 reason。",
  "_definition": {
    "A": "一般人做不到、帶明顯嚮往感（遊艇、五星飯店套房、精品開箱、豪華 villa、私人招待所）",
    "B": "一般人偶爾會去（咖啡廳、餐酒館、酒吧、錄音室、健身房、自宅、工作場所）",
    "C": "一般人天天在做、且畫面完全不美（賣場、超商、加油站、洗衣店、藥妝店、車站月台、早餐店、菜市場、候診間、停車場）"
  },
  "tiers": {
    "own_bedroom": "B",
    "own_living_room": "B",
    "own_bathroom": "B",
    "own_kitchen": "B",
    "own_entryway": "B",
    "own_balcony": "B",
    "workplace_own_studio": "B",
    "workplace_office": "B",
    "workplace_shop": "B",
    "local_cafe": "B",
    "restaurant": "B",
    "bar": "B",
    "gym": "B",
    "dance_studio": "B",
    "rental_photo_studio": "B",
    "city_street": "B",
    "park": "B",
    "convenience_store": "C",
    "supermarket": "C",
    "hypermarket": "C",
    "laundromat": "C",
    "train_platform": "C",
    "bus_stop": "C",
    "gas_station": "C",
    "pharmacy": "C",
    "breakfast_shop": "C",
    "wet_market": "C",
    "clinic_waiting_room": "C",
    "parking_garage": "C",
    "post_office": "C",
    "pickup_locker": "C",
    "car_interior_parked": "C",
    "stairwell": "C",
    "five_star_suite": "A",
    "luxury_hotel_lobby": "A",
    "private_yacht": "A",
    "luxury_villa": "A",
    "resort_pool": "A",
    "first_class_lounge": "A",
    "designer_boutique": "A",
    "private_club": "A"
  },
  "_v2_note": "signature_family 與 career_related 不再由每列自由填 label——改由本表給預設值，shot 可 override 但必須寫 reason。這樣『忘了標』或『改 label 逃過 25% 上限』都會被擋。",
  "defaults": {
    "workplace_own_studio": {
      "signature_family": "{persona_workplace}",
      "career_related_default": true
    },
    "workplace_office": {
      "signature_family": "{persona_workplace}",
      "career_related_default": true
    },
    "workplace_shop": {
      "signature_family": "{persona_workplace}",
      "career_related_default": true
    },
    "dance_studio": {
      "signature_family": "{persona_workplace}",
      "career_related_default": true
    },
    "gym": {
      "signature_family": "{persona_workplace}",
      "career_related_default": true
    }
  },
  "_defaults_note": "{persona_workplace} 由各 persona 的 signature_family_key 代入（Nico = nail_studio）。其餘 location 預設 signature_family=null、career_related=false。"
}
```

---

## 8. 完整 19 張規格

| # | id | 目的 | 場景 | 地點 | 層級 | outfit | hair | framing | yaw | 表情 | 姿態 | 視角 | 光線家族 | 濾鏡 |
|---|----|------|------|------|------|--------|------|---------|-----|------|------|------|---------|------|
| 01 | `a01` | identity_core | 咖啡廳靠窗的位子坐著，正對鏡頭，沒有在做任何事 | `local_cafe` | B | `01` | `01` | face_closeup | front | neutral_relaxed | standing | third_person | L2 | none |
| 02 | `a02` | identity_core | 同一個位子，身體轉向左邊，臉轉回鏡頭 | `local_cafe` | B | `01` | `01` | chest_up | left_30 | soft_smile | standing | third_person | L2 | none |
| 03 | `a03` | identity_core | 白天的人行道上站著，身體轉向右邊，臉轉回鏡頭 | `city_street` | B | `01` | `02` | chest_up | right_30 | neutral_relaxed | standing | third_person | L6 | none |
| 04 | `a04` | identity_core | 同一段人行道，身體較大幅度轉向左側 | `city_street` | B | `03` | `01` | chest_up | left_60 | listening_attentive | standing | third_person | L6 | none |
| 05 | `a05` | identity_core | 公園長椅上坐著，身體較大幅度轉向右側 | `park` | B | `03` | `02` | chest_up | right_60 | mid_conversation | seated | third_person | L6 | none |
| 06 | `a06` | body_pose_coverage | 公園步道上站著，正對鏡頭，雙手自然垂下 | `park` | B | `03` | `01` | full_body | front | neutral_relaxed | standing | third_person | L6 | none |
| 07 | `a07` | body_pose_coverage | 同一條步道，身體轉向右側四分之三，臉轉回鏡頭 | `park` | B | `01` | `04` | full_body | right_30 | soft_smile | standing | third_person | L6 | none |
| 08 | `c01` | identity_core | 鐵門拉下後，坐在工作椅上轉過來看窗外，手還搭在椅背 | `workplace_own_studio` | B | `01` | `03` | face_closeup | front | neutral_composed | seated | third_person | L2 | none |
| 09 | `c02` | identity_core | 蹲在地上拆剛到的材料紙箱，抬頭看向門口 | `workplace_own_studio` | B | `01` | `03` | chest_up | left_30 | mildly_surprised | crouching | third_person | L2 | none |
| 10 | `c03` | identity_core | 站在流理台前等水滾，一手撐著檯面 | `own_kitchen` | B | `08` | `01` | waist_up | right_30 | tired_soft | standing | third_person | L2 | none |
| 11 | `c04` | identity_core | 床邊坐著，剛醒還沒站起來，低頭看手機 | `own_bedroom` | B | `08` | `06` | waist_up | front | just_woken_blank | seated | selfie_front | L2 | none |
| 12 | `c05` | body_pose_coverage | 玄關穿鞋，一手扶著牆 | `own_entryway` | B | `03` | `01` | knee_up | left_60 | focused | leaning | third_person | L3 | none |
| 13 | `c06` | body_pose_coverage | 大安區巷子裡走路，剛越過一台停在牆邊的機車 | `city_street` | B | `03` | `01` | full_body | right_60 | neutral_walking | walking_frozen | third_person | L6 | none |
| 14 | `c07` | identity_core | 低頭替客人上膠，側臉朝向鏡頭 | `workplace_own_studio` | B | `01` | `03` | chest_up | profile_left | focused | seated | third_person | L3 | none |
| 15 | `c08` | body_pose_coverage | 浴室鏡前修眉，另一手撐著洗手台 | `own_bathroom` | B | `08` | `02` | waist_up | left_30 | concentrating_slight_frown | leaning | selfie_mirror | L8 | none |
| 16 | `c09` | body_pose_coverage | 蹲在床邊伸手到床底下找充電線，回頭 | `own_bedroom` | B | `08` | `02` | knee_up | left_30 | mildly_annoyed | crouching | third_person | L3 | none |
| 17 | `c10` | environment_stress | 自助洗衣店裡把烘好的衣物從滾筒抱出來，站在機台前 | `laundromat` | C | `09` | `04` | full_body | right_30 | neutral_composed | standing | third_person | L1 | none |
| 18 | `c11` | environment_stress | 藥妝店貨架前拿護手霜比較成分 | `pharmacy` | C | `05` | `05` | knee_up | front | reading_focused | standing | third_person | L1 | ccd |
| 19 | `c12` | environment_stress | 捷運月台等車，看著對面的到站顯示 | `train_platform` | C | `06` | `04` | waist_up | right_30 | blank_waiting | standing | third_person | L1 | ccd |

---

## 9. 給第三輪審閱者：請幫我檢查什麼

1. **§1 的 endpoint 反駁我做得對嗎？** 我用的是本專案實際呼叫的 MCP 工具 schema，
   而不是官網 Help Center。這個證據層級夠嗎？還是應該真的送一次 API request 實測？
2. **7 + 12 = 19 張的比例合理嗎？** 還是應該補到滿 20？
3. **家＋工作室仍佔 42%**，但 anchor 全部在外面。這個緩解方式夠嗎？
4. **`nico_outfit_01` 現在佔 7/19（37%）**
   ——比 R2 的 outfit_08 30.8% 更高，因為 anchor 用了同一套以維持可比較性。
   對 identity training 這是幫助（重複 body-readable outfit 幫模型學身體）還是 burn-in 風險？
5. **Retroactive Benchmark 要拿哪一個既有 Soul 當 GOOD baseline？** repo 有 6 個 ready，
   我沒有生產使用頻率的資料可以判斷哪個「公認最好用」。這需要使用者提供。
6. **§5 那 4 項我沒做的，哪幾項應該在生成前補完，哪幾項可以等 pilot 之後？**
