# 身材補正實測：靠 prompt 補得動嗎？（2026-09-07）

## 為什麼要做這個實測

決策 (B)（`../../soul_training/DECISION_body_spec_B.md`）維持 `profile.json` 的
`bust_cm 89 / cup_size D` 不動，改用正式出圖的 prompt 來補落差。

但這個補法**當時完全沒有實測過**，而 `SEXY_SCENE_LIBRARY.md` 已載明
「覆蓋度無法用 prompt 可靠控制」——覆蓋度控不動是實測推翻過的結論，
所以「身材控得動」不能預設成立。使用者裁定用一位來實測。

## 實驗設計

用 **cheryl-soh**（`soul_id 6d4c90b5-…`），因為她的落差是已量測並存證的，
可以直接對照她既有的 V1／V4。

**prompt 與鎖定的 V1／V4 逐字相同，只在髮型句之後插入一句身材描述。**
其餘所有字（場景、服裝、光線、機位、動作、單人排除句、拍攝句）完全不動，
因此差異只能歸因於那一句。

| 組 | 插入的句子 |
|---|---|
| 基準 | **無**（即既有的 V1／V4，2026-09-07 早上產出） |
| A 描述性 | `She is slim but distinctly full-chested: a soft, heavy curve at the bust that clearly fills and shapes the top, sitting above a noticeably narrow waist.`（V4 版尾端加 `with long legs`） |
| B 數字 | `She is 169 cm tall with an 89 cm bust, a 60 cm waist and 90 cm hips, a D cup on a slim frame.`（V4 版加 `and her legs are 83 cm long`） |

各組 V1（胸上）與 V4（全身）各一張，共 4 張新圖 = **0.48 credits**。

## 結果：**補得動。**

見 `compare_V1_torso.jpg`（胸上三組並排）與 `compare_V4_fulllength.jpg`（全身三組並排）。

| | 基準 | A 描述性 | B 數字 |
|---|---|---|---|
| V1 胸型 | **幾乎平**，背心完全沒有形狀 | **明顯胸型**，背心被填起並有輪廓 | **明顯胸型**，與 A 相當 |
| V1 腰線 | 不明顯 | 較清楚 | 較清楚 |
| V4 胸型 | 平 | 明顯 | 明顯 |
| V4 腿長比例 | 長 | 長（維持） | 長（維持） |

**兩種寫法都有效，且效果相當；描述性至少不輸寫數字。**

## 結論與建議寫法

1. **決策 (B) 可行。** 先前標記的風險（「補法未實測」）**已解除**。
   `profile.json` 的三圍數字可以維持不動，出圖時靠 prompt 補。
2. **建議用描述性寫法，不要在 prompt 裡塞三圍數字。** 理由：
   - 實測效果相當，數字沒有優勢。
   - 數字不會泛化（換人就要換一組數字），描述性句子可以按人微調。
   - 數字讀起來像規格表，與本 repo 追求的「像真實照片」方向相反。
3. **這一句只用於正式內容圖，永遠不寫進驗證圖。**
   `../../soul_training/ACCEPTANCE_LOCKED.md` §二 禁止驗證圖重述三圍，
   理由是驗證圖若描述身材，測到的是 prompt 而不是 Soul。兩者不衝突但不可混用。

## 方法上的限制（誠實記錄）

- **n=1 人設、每組各 1 張。** 證明了「這一句在 cheryl 身上有效」，
  沒有證明「對 19 位都有效」或「每次都有效」。
- 沒有測到量化程度——只能說「明顯從平變成有胸型」，
  不能說「補到了 89cm／D」。要驗證到那個精度需要更多樣本。
- A 與 B 兩組的上衣領口都與基準略有差異（B 的 V4 變成 V 領），
  屬既有的服裝漂移現象，與本測試無關。
- **身高／嬌小感沒有一併測。** kanon-komori（153cm）與 miu-shiraishi（156cm）
  的抽驗顯示 Soul 不繼承嬌小感；本測試沒有測「寫身高能不能補出嬌小」，
  只在 B 組寫了 169cm 而 cheryl 本來就接近該身高。**嬌小感補正仍未驗證。**
