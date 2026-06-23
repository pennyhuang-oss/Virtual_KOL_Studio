# Virtual KOL Studio — Character Database

虛擬 KOL 角色設定資料庫。每個 KOL 為一個獨立目錄，包含結構化 JSON 資料、完整角色 Bible 與內容風格指南。

---

## 目錄結構

```
Virtual_KOL_Studio/
├── kols/
│   ├── index.json           # 所有 KOL 的主索引
│   ├── schema.json          # 標準欄位定義（JSON Schema）
│   └── {kol-id}/
│       ├── profile.json     # 結構化角色資料（符合 schema）
│       ├── character.md     # 完整角色 Bible
│       ├── content_style.md # 內容方向與風格指南
│       ├── images/          # 訓練圖片與參考圖
│       └── videos/          # 製作影片
```

---

## KOL 陣容

| ID | 名字 | 本名 | 國籍 / 城市 | 類型 | 年齡 | 狀態 |
|----|------|------|------------|------|------|------|
| [iris-chen](kols/iris-chen/) | **Iris Chen** | 陳芯語 | 台灣，台北 | 科技 / AI | 22 | active |
| [luna-tanaka](kols/luna-tanaka/) | **Luna Tanaka** | 田中ひな | 日本，京都 | 生活美學 / 攝影 | 20 | active |
| [ananya-kapoor](kols/ananya-kapoor/) | **Ananya Kapoor** | अनन्या कपूर | 印度，孟買 | 瑜伽 / 身心靈 | 23 | active |
| [yuna-kim](kols/yuna-kim/) | **Yuna Kim** | 김하은 | 韓國，首爾 | K-beauty / 彩妝 | 21 | active |
| [aaliya-okonkwo](kols/aaliya-okonkwo/) | **Aaliya Okonkwo** | — | 奈及利亞，拉哥斯 | 非洲時尚 / 文化 | 24 | active |
| [camille-dupont](kols/camille-dupont/) | **Camille Dupont** | — | 法國，巴黎 | 美食 / 葡萄酒 / 生活 | 22 | active |

---

## 新增 KOL 流程

1. 在 `kols/` 下建立新目錄，命名規則：`{firstname}-{lastname}`（kebab-case）
2. 按照 `kols/schema.json` 建立 `profile.json`
3. 撰寫 `character.md`（角色 Bible）與 `content_style.md`（內容指南）
4. 在 `kols/index.json` 新增對應紀錄

---

## 後續補充計劃

- [ ] `reference_profiles` — 每個 KOL 的真實參考帳號與分析
- [ ] `script_self_intro.md` — 第一支自我介紹影片腳本
- [ ] `edit_timeline_self_intro.md` — 剪輯時間軸
- [ ] `ai_assets` — Higgsfield Soul ID、訓練圖片紀錄
- [ ] `productions` — 影片製作記錄（shot list、voiceover、job ID）

---

## 架構參考

本資料庫架構參考自 [firekou/Buildup_KOL](https://github.com/firekou/Buildup_KOL)。
