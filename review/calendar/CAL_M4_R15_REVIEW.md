TASK-CAL-001／M-4／R15｜R14 主管覆核與有限收尾｜送審報告

# M-4 R15 送審紀錄

- 固定成果 commit：`374a7b8`（起點 `7f9f396`）
- 本輪：生成 0、付費編輯 0、上傳 0、部署 0。

## 主管報告

```
TASK-CAL-001／M-4／R15｜R14 主管覆核與有限收尾｜Claude 執行回報

起點 HEAD：7f9f39668b3541fe8cdb2c04dcb893051877104e（未回退、未覆蓋）
成果 commit：374a7b8（已 push claude/epic-carson-n5w0qu）
本輪：生成 0、付費編輯 0、上傳 0、部署 0；未重試、未改 V-Iris、未啟動其他角色、未合併 main

一、主管結論已保存（與 Claude 自查分開）
- 檔案：docs/calendar/data/cal_m4_supervisor_r14.json（含 R15 指令全文）
- Tammy：主管保留候選，待 Penny 決定，未接受
- Rin：主管建議修改（REVISE），Penny 未決定
- R14 Claude 自查原文保留在 cal_m4_r14_trial.json，未改寫

二、畫面下緣分開記錄（docs/calendar/data/cal_m4_r15_followup.json framing）
Tammy：原圖截斷＝是（著地那隻腳的腳掌與鞋底被原圖下緣切掉；抬起那隻完整，腳尖離下緣約 10–20 px）
       腳下緊迫＝是；3% 工作線＝越線；實際套框＝3:4 直接放入、不另裁切
Rin：  原圖截斷＝是（一隻靴子鞋頭被原圖下緣切掉；另一隻離下緣約 29 px）
       腳下緊迫＝是；3% 工作線＝越線；實際套框＝不另裁切
       prompt 偏離（全身而非膝上）與照片品質分開記錄
3% 線只作工作參考，不是廠商裁切線，不據此單獨判失敗

三、Rin prompt 修訂一次（未生成）
- 路徑：docs/calendar/data/cal_m4_r15_followup.json（rin_prompt_v2.text），commit 374a7b8
- sha256：f178e919d7015b082bf1e1d7de272e374974f093fd98808dba2104b0050cf898（342 詞）
- 來源：cal_m4_r13_cards.json @ bd84cf9，sha256 fa6975f3…（349 詞）
- 改動：迎光神情與姿態移到最前段；寫明暖光帶落在臉、臉是全畫面最亮處；
  雙臂不再垂下，只加一個簡單手勢（一手輕抓胸前大衣邊）；
  明確膝上景別、腳不入鏡，刪掉踝靴描述；柱子改為右緣一窄條陰影中的側邊框景；
  合併光、拱、柱的重複描述
- 保留：迴廊與庭院、黑色細針織方領中長洋裝、駝色大衣披肩、小金圈耳環、低髮髻、秋日左側硬光、色彩
- 下一次單張測試費用參考：Soul 2＋Rin Soul、2k、3:4、count 1，約 0.12 credits（送出前重新唯讀報價）

四、紀錄同步與檢查
- cal_m3_shoot_plan.json：Tammy、Rin set_notes 只追加 R15 主管結論；新增 m4r15；接受數與計數不變
  （月面照片 11／1.32；底稿 2／4；已接受仍只有 V-Iris）
- 檢查：CAL_18 --check PASS（其餘 CAL 文件未變）；建置 --check PASS（671 檔、問題 0、公開檔無私有 ID）

五、待 Penny
- Tammy R14 是否接受
- Rin 是否授權用修訂版 prompt 再試 1 張（約 0.12）

六、交付說明
- R14 兩張完整新圖與前後對照已直接在回覆中顯示
- Railway 審圖頁（cal2027-decision）未更新：本輪指示不部署；目前網站資料也還沒有收錄 R14 照片，
  若要在網站上選，需另行授權「把 R14 兩張加到審圖頁並部署」
```
