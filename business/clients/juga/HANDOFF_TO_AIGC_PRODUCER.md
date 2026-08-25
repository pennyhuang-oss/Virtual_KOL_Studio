# JUGA App 指引影片 × Rainie Hsu — 交接包

> **給接手的 AIGC 製作師（與你的 Claude）**
> 把這份檔案整份丟給 Claude，它就能接手。前面是現況與素材，後面是**兩個腳本方向**讓你選，
> 不是規定。所有結論都附了判斷依據，你要推翻哪一條都可以，但請先看「不能動的三條紅線」。

**專案**：JUGA（`juga.com.tw`｜18+ 夜生活揪團 App）的操作指引影片，加入 KOL Rainie Hsu 導覽
**交接日**：2026-08-24
**Repo**：`pennyhuang-oss/Virtual_KOL_Studio`，分支 `claude/app-video-script-planning-ngoovg`
**目錄**：`business/clients/juga/`
**你有 repo 讀取權限**，所以不用等別人傳檔案——下面提到的每個路徑都可以直接叫 Claude 去讀。

---

## 0. 一分鐘搞懂現況

客戶自己做了一支 **65.7 秒、無旁白、只有三處黃色字卡**的 App 操作影片（用截圖後製接起來的，不是螢幕錄影）。
客戶覺得無趣，選了 Rainie 來當導覽的美女角色。我們要做的是**把 Rainie 加進去，讓這支片有人在講解**，
原本 18 個操作步驟一步都不能少。

**已經做完的**：原片逐格拆解（18 步）、完整分鏡腳本、57 句旁白稿、生成 prompt、後製清單。
**卡住的**：配音（見第 5 節，這是最大的未解問題）。
**主管最新指示**：造型用 Rainie 的**黑框眼鏡造型**；舞蹈段直接用**現成的 R10 成品**，不重新生成。

---

## 1. 不能動的三條紅線

這三條是實測踩過的坑，不是偏好問題。

| # | 紅線 | 為什麼 |
|---|---|---|
| 1 | **腰腹必須完整包覆，綁帶要疊在實心不透空的布料上** | R10 第一版起始畫面腰間鏤空開到接近肚臍，`motion_control` **連續兩次被判 `nsfw`**（兩次都零成本但白等）。改成實心打底後一次過審。 |
| 2 | **prompt 不能出現 `film grain`、`shot on 35mm`、`candid lifestyle photo`** | 這三個詞對 Rainie 的 soul_id **連三次觸發「三連拼貼」bug**（一張圖塞好幾格縮圖，完全不能用），當時一度誤判成 soul_id 壞掉差點花錢重訓。改用 `crisp sharp focus` / `high dynamic range` / `high-production-value` / `Instagram style` 就正常。 |
| 3 | **眼鏡要在每個 prompt 裡明寫** | Rainie 的 `profile.json` 是 `glasses: "None."`，soul_id 不會自己給眼鏡。這副眼鏡是 R10 從驅動片帶過來的例外造型。**不要去改 `profile.json`** —— 主管說只有這支片用，那是角色設定不是本片造型。 |

其他禁用詞：`sensor noise`、`autofocus hunting`、`JPEG compression artifacts`、`soft dreamy filter`、
`evenly lit`、`well-exposed`、`studio lighting`、`grainy`、`muddy`、`degraded`。

---

## 2. 素材盤點

### 2-1 客戶原片

`/root/.claude/uploads/.../c0d9cc53-__APP.mp4`（跟 Penny 要，沒進 repo）
1080×1920、25fps、65.72 秒、H.264 + AAC、有 BGM 無人聲。

**18 個操作步驟**（新版一步都不能少）：

| # | 原片時間 | 畫面 |
|---|---|---|
| S1 | 0:00 | Safari 私密瀏覽新分頁 |
| S2 | 0:02 | 網址列逐字打 `www.juga.com.tw` → 前往（**佔全片 14%，全是打字**） |
| S3 | 0:11 | JUGA 登入頁：登入｜客戶註冊／帳號密碼／忘記密碼／訪客瀏覽／限 18 歲以上 |
| S4 | 0:13 | Safari「⋯」→ 選單 → 點**分享** |
| S5 | 0:19 | iOS 分享面板 → **檢視較多** → 出現**加入主畫面** |
| S6 | 0:21 | 加入主畫面設定頁：名稱 JUGA、**「打開為網頁 App」開關維持開啟** → 加入 |
| S7 | 0:24 | 主畫面出現 JUGA 圖示 |
| S8 | 0:26 | 客戶註冊：手機號碼／簡訊驗證碼＋發送驗證碼／暱稱／密碼至少 6 碼／勾 18 歲同意條款（**要拉到最下面才勾得下去**）→ 註冊並開始 |
| S9 | 0:27 | 回登入畫面（原片字卡「註冊完成，切換到登入畫面」）→ 登入 |
| S10 | 0:29 | 完成設定（標題寫「再三步就能開始」）：頭貼／暱稱／所在區域／自我介紹／推播說明 → 繼續 |
| S11 | 0:31 | **首頁**：搜尋用戶・通知鈴／開啟通知橫幅／我的邀請（空狀態）／今晚在線名單／底部五分頁 **首頁｜廣場｜＋｜通知｜我的** |
| S12 | 0:35 | 點中央 **＋** |
| S13 | 0:36 | 發布邀請：區域／類型（**After Party・喝一杯・補位・臨時約會・其他**）／人數（最多 20）／備註 0/200／**邀請有效時間 2 小時** → 發送 |
| S14 | 0:39 | 我的邀請出現卡片：類型・區域・人數・♡♡ 已加入約會 0/2・0 人想加入 |
| S15 | 0:42 | 卡片變 **3 人想加入**（紅圈標註＋字卡），通知鈴紅點 3 |
| S16 | 0:46 | 邀請詳情：0/3 人／約 2 小時後關閉／發布者／**想加入 (3)** 各有接受｜婉拒／底部關閉邀請。字卡「**先點選大頭貼，可觀看相簿**／喜歡按接受，不喜歡按婉拒」 |
| S17 | 0:52 | 通知（收件匣）：配對卡「喝一杯・{發布者}／關於 {對方}／**聊天視窗開啟中・還有 1 天**」＋聊天鈕 |
| S18 | 0:57 | 聊天室：**聊天視窗將在 1 天 23:58:26 後關閉**倒數／傳訊「信義區 a11 10 點 包廂 999」→ 回「好的 安排」→ 頂部亮起 **♥ 約會中・忙碌**。**直接結束，無片尾** |

**App 核心邏輯一句話**：網頁加到主畫面當 App 用 → 註冊 → 發一則**限時 2 小時**的「今晚想做什麼」邀請 →
看誰舉手 → 你挑人 → 開一個**只存在 1 天**的聊天視窗喬地點時間 → 狀態變「約會中」。
賣點是**限時**＋**今晚在線**的即時感，不是長期交友。旁白全程都該強化這兩點。

### 2-2 原片的三個瑕疵（後製要處理）

1. **狀態列一路跳**：開頭是紅色錄影中膠囊，之後 `2:55 → 3:34 → 3:46 → 3:37 → 3:38`，電量從 94% 掉到低電量。
   → **全片蓋一條統一的假狀態列**（固定時間、滿格訊號、固定電量），一次解決三個問題。
2. **「我的邀請」卡片顯示松山區，但發布表單填的是信義區**，人數也從 2 變 3（兩次錄製混剪）。
   → 客戶補圖，或用局部放大裁掉區域欄位、旁白只講人數變化。
3. **「完成設定」寫「再三步就能開始」但只演一步**；**「廣場」「我的」兩個分頁從沒出現過**。
   → 客戶重出約 6 張截圖（**不是重錄**，成本很低），或用備援作法帶過。

### 2-3 Rainie 現成素材

**Soul ID（生成用）**：`a4a000fe-fd96-4c36-97ff-0df9358a9b47`
> ⚠️ `generation_notes.md` 開頭那組 `994e33d2-…` 是**已棄用**的舊 ID（身材不符規格），不要用。
> 以 `profile.json` / `README.md` 為準。

**指定造型參考圖**：`kols/rainie-hsu/images/dance_clone_r10/start_frame_v2.png`
黑色深V halter 綁帶洋裝（交叉綁帶＋金屬圓孔，**綁帶底下是實心布料**）＋ 敞開的黑色長袖絲質罩袍 ＋
**黑色粗框眼鏡** ＋ 金色圓形耳釘 ＋ 長直黑髮放下。場景是飯店房間（金色巴洛克壁紙、暖色壁燈、全身鏡）。

> 同目錄的 `start_frame.png` 是 v1，腰間鏤空過深、被判 `nsfw`，**只供對照不要用**。

**現成舞蹈短片（三支，全部 1072×1936 / 30fps）**：

| 檔案 | 長度 | 造型 | 能不能用在這支片 |
|---|---|---|---|
| `videos/dance_clone_r10/rainie_dance_clone_r10_ig_reel.mp4` | 9.33s | **黑框眼鏡＋深V綁帶洋裝＋絲質罩袍，飯店房間** | ✅ **就是主管要的那支** |
| `videos/dance_clone_r5/rainie_dance_clone_r5_ig_reel.mp4` | 14.0s | 桃紅短T＋牛仔短褲，戶外工業區道路 | ❌ 造型與場景都不合 |
| `videos/dance_clone_r14/rainie_dance_clone_r14_ig_reel.mp4` | 7.2s | 黑色高衩連身泳裝，宮廷風房間 | ❌ 沒眼鏡，且尺度不適合客戶官方教學片 |

> ⚠️ **三支的配樂都是驅動片原始音樂，未取得商用授權**，`generation_notes.md` Step 7 標記為僅供內部驗證。
> **要用進客戶交付物，音軌一定要換成可商用曲庫版本。**

**其他可參考**：`images/training_v2/`（13 張訓練圖）、`images/face_reference/`（選角候選圖）。

---

## 3. 兩個腳本方向，自己挑

兩份都在 repo 裡，也都有可以直接點開的網頁版。**可以混搭**，不必二選一。

### 方向 A —— 完整教學長片（已寫完，2 分 36 秒）

**網頁版**：<https://claude.ai/code/artifact/4dd88bd3-338e-474b-bf15-aaf6c0db9973>
**生成工單**：<https://claude.ai/code/artifact/a19d292d-1990-4197-a5af-8dc261b4fdec>
**repo**：`JUGA_APP_GUIDE_SCRIPT_V2.md`、`juga-rainie-script.html`、`juga-rainie-aigc-worksheet.html`

12 段分鏡、57 句旁白稿全部寫好，5 張起始畫面 ＋ 5 支影片 ＋ 1 支 Motion Control 的可複製 prompt 都有。

| # | 時間 | 秒 | 段落 |
|---|---|---|---|
| 1 | 00:00 | 8 | ★ 開場（Rainie 全畫面） |
| 2 | 00:08 | 8 | ▣ ① 用 Safari 開網站 |
| 3 | 00:16 | 20 | ▣ ② 加到主畫面 |
| 4 | 00:36 | 6 | ★ 換氣點 |
| 5 | 00:42 | 16 | ▣ ③ 註冊 |
| 6 | 00:58 | 16 | ▣ ④ 登入＋完成設定 |
| 7 | 01:14 | 14 | ▣ ⑤ 首頁導覽 |
| 8 | 01:28 | 18 | ▣ ⑥ 發出邀請 |
| 9 | 01:46 | 8 | ★ **舞蹈段** |
| 10 | 01:54 | 16 | ▣ ⑦ 誰想加入 |
| 11 | 02:10 | 16 | ▣ ⑧ 聊天喬細節 |
| 12 | 02:26 | 10 | ★ 片尾 CTA |

Rainie 全畫面 32 秒（21%），其餘 124 秒她以**去背半身站右下角**、手勢指向當下按鈕（螢幕縮到 82% 置上，UI 不被遮）。

**這個方向的成本重點**：要生 5 張起始畫面 ＋ 5 支影片 ＋ 1 支 Motion Control，人工後製也不少
（統一狀態列、切段配速、局部放大、六個去背 clip 的淡入淡出）。你如果覺得人工介入太多，看方向 B。

### 方向 B —— 主管的新方向（骨架，細節留給你）

主管的原話大意：Rainie 開場 → 跳到 App 指引介面 → **介面中間穿插說明，像是「App 上面可以放女生自己的
短影音」** → 才接上 Rainie 跳舞的影片，而且**跳舞直接用現成的 R10，不重新生成**。

**這個方向比 A 好在哪（我認為值得採納）**：

方向 A 的舞蹈段是「邀請發出去了，慶祝一下」——情緒上說得通，但舞蹈本身跟 App 沒有關係。
主管這個安排讓舞蹈**有了內容上的理由**：那就是女生會放在 JUGA 上的短影音，是 App 功能的示範。
觀眾看到的不是「插播一段美女跳舞」，是「原來 App 裡面長這樣」。**這比我原本的設計成立得多。**

**建議的切入點**：原片 **S16** 有一句字卡「**先點選大頭貼，可觀看相簿**」。這是全片唯一提到
「使用者個人內容」的地方，也就是舞蹈影片最自然的插入位置——旁白講到「點大頭貼可以看她的檔案」，
畫面就切進 R10 那支，看完再切回接受／婉拒。時間點約在方向 A 的 01:54–02:10 那一段。

**製作上的一個小技巧**：把 R10 那 9.33 秒**放進一個手機畫面框裡播放**（像是在 App 內看影片），
一次解決三件事——解析度差異（1072×1936 vs 1080×1920）看不出來、視覺上直接說明「這是 App 裡的內容」、
而且不會跟教學畫面搶主導權。

> ### ✅ 短影音功能已確認存在（2026-08-24 客戶確認）
>
> 一開始我在原片裡找不到這個功能的證據——逐格看完 65.7 秒，只有 S16 的字卡提到「可觀看**相簿**」，
> 底部的「廣場」和「我的」兩個分頁從頭到尾沒出現過。**已向客戶確認：JUGA 確實有短影音功能**，
> 所以主管的原意可以直接照寫，R10 那支就是最好的示範素材。
>
> 旁白建議寫成「點大頭貼可以看她的檔案——相簿、還有她自己放的短影音」，畫面接著切進 R10。
> 這樣同時涵蓋原片字卡提到的相簿，也帶出短影音，兩個都是真的功能。
>
> 但那 6 張補圖還是要跟客戶要（見第 2-2 節），「廣場」和「我的」沒畫面這件事沒解決。

**方向 B 的其他段落**沒有寫死，你可以直接沿用方向 A 的分鏡與旁白稿（S1–S18 的教學內容兩個方向完全一樣），
只是把舞蹈段從「01:46 慶祝」改成「S16 功能示範」，並且**省掉一整支 Motion Control 生成**。

---

## 4. 生成規格（兩個方向共用）

完整內容在**生成工單**：<https://claude.ai/code/artifact/a19d292d-1990-4197-a5af-8dc261b4fdec>
（原始碼 `juga-rainie-aigc-worksheet.html`，有每一張圖、每一支影片的可複製 prompt）

### 共用參數

```
起始畫面：generate_image(model="soul_2", soul_id="a4a000fe-fd96-4c36-97ff-0df9358a9b47",
                        aspect_ratio="9:16", count=1)
影片：    generate_video(model="kling3_0", aspect_ratio="9:16", duration=10, sound="on",
                        medias=[{"role":"start_image","value":"<image_media_id>"}])
                        # multi_shots 不設定；cinematic_studio_video_v2 禁用（會變廣告感）
前置：    每張起始畫面先 media_import_url(url=<rawUrl>) 換成 image_media_id
```

需要 8 秒或 6 秒的段落**一律生 10 秒再後製裁切**，比跟模型爭長度穩定。

### prompt 組裝方式

完整 prompt ＝ **身分段 ＋ 造型段 ＋ 各張的變動段 ＋ 光線段 ＋ 收尾段**，五段依序串起來。
前後四段共用，只有變動段每張不同。全文在生成工單第 03 節，這裡只列造型段與光線段：

**造型段**
```
wearing a black deep-V halter dress with a decorative criss-cross lace-up panel set with
gold metal eyelets — the lacing sits on top of solid opaque fabric, NOT open to skin, and
the waist and stomach are fully covered by the dress — layered under a long-sleeved black
silk robe worn open and slipping off both shoulders, thick black rounded acetate-framed
glasses, small round gold stud earrings — a deliberately coordinated set, nothing generic
or accidental,
```

**光線段**（飯店房間，五段式物理光線公式）
```
lit by a warm tungsten wall sconce on the left as the key, its light bouncing off the gold
damask wallpaper and wrapping a warm fill around her jaw and shoulder, a second cooler
magenta-violet source coming from the phone screen in her hand and a neon sign bleeding
through the window on the right, two clearly different colour temperatures coexisting in
one frame — warm room, cool magenta accent, exposure metered for her face so the depth of
the hotel room behind her crushes to near black, shot into the full-length mirror whose
dark wooden frame crops the top and right edge of the image,
```
> 洋紅紫是刻意從**手機螢幕光＋窗外霓虹**注入的，讓 Rainie 的畫面跟 JUGA 的紫紅漸層 UI 在同一個色系裡。
> 鏡子也是刻意留的：`scene_control: "image"` 下背景整體鎖死，但**鏡面反射區會跟著人動**，
> 等於免費換到一點局部背景動態。

### 交片檢核

- **身分一致**：把成品幀跟起始畫面的**圖檔本身**並排比對，不能只憑印象
- **造型一致**：洋裝、罩袍、**眼鏡**、耳釘、髮型，四段並排看
- **眼鏡**：鏡框對稱、兩隻鏡腿都在且沒穿過頭髮、鏡片反光沒蓋掉眼睛、**影片全程鏡框不能飄移或忽大忽小**
- **腰腹包覆**：綁帶底下確認是實心布料
- **拼貼 bug**：每張起始畫面都是單張照片，不是多格縮圖
- **手部**：去背素材的手勢特寫，手指數量與關節逐格看
- **去背邊緣**：髮絲殘留灰底、罩袍長袖邊緣、**鏡腿有沒有被摳斷**
- **狀態列**：全片時間／電量／訊號一致，沒有殘留錄影中膠囊

參考 SOP：`DAILY_VIDEO_SOP.md`、`DANCE_CLONE_SOP.md`、`SEXY_SCENE_LIBRARY.md`（降低 AI 感的技術要點）、
`kol-content-qa-pipeline` skill。

---

## 5. 未解決：配音（最大的卡點）

**旁白稿 57 句已經寫好**（生成工單第 06 節，12 段對應 12 個時間碼），但**用什麼聲音念還沒定案**。

已經查證過的：

| 選項 | 狀況 |
|---|---|
| Higgsfield **preset 聲音** | 114 個全部翻過，**一個中文聲線都沒有**，全是 Grady / Tallulah / Elena / Alexey 這種西方東歐名字。`CLAUDE_HANDOFF.md` 記錄的「聽起來像外國人說中文」就是這個原因。 |
| 帳號現有的 **element（自建）聲音** | 三個：`Faye Tan`、`Tan XiaoXiao`、`Yulenda Clean`。**Penny 聽過，三個都不像 Rainie 的人設。** |
| **影片模型直接生語音** | `kling3_0` / `veo3_1` / `seedance_2_0` / `wan2_7` / `flux_3_video` 都能生同步語音，**但沒有任何一個有 `voice_id` 參數**——每次生成的聲音都不一樣。切成十幾支 clip 就是十幾個聲音，**這條路直接排除**。 |
| **`seed_audio` ＋ `image_references`** | ⭐ 目前最可行。`seed_audio` 支援「用一張圖當聲音線索」，可以**餵 Rainie 的起始畫面，讓模型從那張臉推導出聲音**，不需要任何真人樣本。**一次只要 0.2 credits**，可以一直試到滿意。 |

**建議流程**（尚未執行，交給你決定要不要走）：

1. `generate_audio(model="seed_audio", prompt="<台詞>", medias=[{"role":"image_references", "value":"<R10 v2 起始畫面 media_id>"}])` — 生幾個版本來聽
2. 選到滿意的音色後，用同一個設定生一段 **10 秒～3 分鐘**的長樣本當 clone 素材
3. `media_upload` → `media_confirm(type='audio')` → `create_voice_from_confirmed_audio(name="Rainie Hsu")` → 拿到固定 `voice_id`
4. 之後所有旁白都用 `voice_type='element'` ＋ 那個 voice_id → **57 句聲音完全一致**
5. voice_id 存進 `kols/rainie-hsu/profile.json`（`CLAUDE_HANDOFF.md` 第 458 行本來就規劃了這個欄位，一直沒執行）

**尚未驗證的風險**：`seed_audio` 是字節跳動的，預設可能是**大陸腔**。查不到任何公開評測測過台灣腔，
只能生出來聽。台詞裡塞台灣語尾（「啦」「喔」「欸」）、調 `speech_rate` / `pitch_rate` 或許能拉，
拉不回來就是這條路的天花板。

**另一個備案**：`seedance_2_0` / `seedance_2_0_mini` / `wan2_7` / `grok_video_v15` 都吃 `audio_references`，
可以把定案的音軌餵進去，讓模型生成**對嘴**的講話影片。這樣 Rainie 就能在畫面上真的開口說話。
如果不走這條，就照方向 A 的設計——**全片旁白，她在畫面上不開口**，每支影片 prompt 都要寫
`lips closed throughout, not speaking, no mouth movement`。

---

## 6. 給接手的 Claude：先讀這些

```
business/clients/juga/
├── HANDOFF_TO_AIGC_PRODUCER.md      ← 你正在讀的這份
├── JUGA_APP_GUIDE_SCRIPT_V2.md       ← 方向 A 的腳本摘要
├── juga-rainie-script.html           ← 方向 A 完整分鏡＋旁白（網頁版原始碼）
└── juga-rainie-aigc-worksheet.html   ← 生成工單，所有可複製的 prompt

kols/rainie-hsu/
├── profile.json                      ← soul_id、外型規格（glasses 維持 "None."，不要改）
├── character.md                      ← 人設與語氣（旁白改稿時看這份）
├── generation_notes.md               ← R5/R10/R14 三支舞蹈的完整執行記錄與踩坑
├── images/dance_clone_r10/start_frame_v2.png   ← 指定造型參考圖
└── videos/dance_clone_r10/rainie_dance_clone_r10_ig_reel.mp4  ← 現成舞蹈素材

根目錄 SOP：
DAILY_VIDEO_SOP.md / DANCE_CLONE_SOP.md / SEXY_SCENE_LIBRARY.md / REELS_AND_STRUCTURE_SYSTEM.md
```

**旁白改稿的原則**（Rainie 的語氣，見 `character.md`）：短、利、不解釋，5–12 字一句最理想。
規則是**教學句講清楚，態度句才耍帥**——「條款要拉到最下面才勾得下去」是教學，
「你挑人，不是人挑你」是態度，兩種不要混在同一句裡。

---

## 7. 動工前要問清楚的四件事

1. **客戶要不要補那 6 張截圖？**（廣場 ×1、我的 ×1、完成設定剩兩步 ×2、統一 demo 資料的我的邀請卡 ×2）
2. **配音走哪條路？**（第 5 節）
3. **走方向 A、方向 B，還是混搭？** 長度、成本、人工介入程度都不一樣。

有任何一條你想推翻，都可以——這份文件記的是判斷依據，不是規定。
