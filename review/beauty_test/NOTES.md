# 美感回歸測試（2 credits）

## 為什麼要做

ref_40–58 那批生出來的臉是怪物。原因不是模型，是我：

1. **目標函數只有分離度，沒有美感。** `derive_geometry_targets.py` 的目標是
   「最大化最接近那一對的距離」，窗開到真人照全幅。這個函數本身就在獎勵極端，
   它不在乎好看，甚至不在乎正不正常。
2. **九條軸各自獨立推極端。** 真人五官是相關的；分開推會組出
   「極長窄臉＋寬鼻翼＋薄平唇」這種真人身上不會同時出現的組合。
3. **一張參考圖同時扛四個不同人物的目標。** `plan_r8_sources.py` 的循環錯位
   在約束滿足上很漂亮，但它保證每張參考圖本身就是四個不相干的人拼起來的臉。
4. **我還明確叫 ChatGPT 往極端畫**（R8 §3：「請刻意往極端畫」）。
5. **52 段選角 prompt 裡沒有一句要求她好看。** 全是骨相描述加素顏。
   這是替 KOL 選角，這句話不該漏。

ChatGPT 原本那批 ref_16–33 每張都是好看的正常人。壞掉的是我把形容詞換算成數字、
然後要求分佈的尾端。

## 這次改了什麼

| | 之前 | 現在 |
|---|---|---|
| 來源池 | ref_40–58（極端幾何） | ref_16–33（原本那批漂亮的） |
| 開場句 | `A vertical photograph of a 25-year-old adult woman.` | `A vertical photograph of a strikingly beautiful 24-year-old Taiwanese woman — the kind of face people follow an account for.` |
| 融合指示 | `Combine these four assigned components` | `Blend them into one harmonious, coherent and beautiful face — the proportions must sit together naturally, as a real attractive woman's features do.` |
| 妝 | `Her face is bare`（素顏） | `light and flattering: dewy base, peach blush, defined lashes, glossy coral-pink lip` |

其餘（骨相軸、身材措辭、服裝、場景、光線、收尾封閉句）一字未動。

## 結果

`sheet.jpg`。臉是正常好看的 24 歲，膚況乾淨，E 罩杯有出來，年齡對。
可以拿去當 KOL 的臉。

## 待修的小問題

- 髮色偏金，`milk-tea golden brown` 被畫成接近金髮，要再壓深。
- a01 鏡中出現手機——自拍句仍會把器材帶進畫面，之後改寫。

## 順序改成

**先美感，再分離度。** 生成端負責好看與五官協調；量測只當篩子，
篩到太接近的配對就請對方在兩三條軸上微調重生，不再用數字驅動生成。

---

# 追加：源頭找到了——是參考圖的規格，不是 prompt 的字

加了「strikingly beautiful」與淡妝之後，臉還是不夠好看。所以改測一件事：
**同一段 prompt，唯一差別是有沒有掛那四張裁切。**

`crop_vs_nocrop.jpg`：左邊掛裁切（`tammy_a02.jpg`），右邊兩張不掛（`nocrop_1/2.jpg`）。
不掛裁切的就是要的那種臉；掛了就是素人。

## 源頭

ref_16–33 當初的規格是「標準正面模板：素顏、頭髮往後梳綁起、灰 T、平光、中性背景」。
那是一份**量測用**規格——為了 landmark 量得準、裁切裁得穩——它做出來的是證件照裡的素人。

整條線繼承了它：從證件照素人身上裁五官 → 四片素人五官去混 → 混出素人。
prompt 裡一句「strikingly beautiful」對抗四張寫著「平凡」的圖，圖贏了。

ref_40–58 更糟：同一個素顏證件照模板，**再加上**我要求的極端幾何——
平凡的底加上怪異的骨相，就是怪物。

**所以錯的不是最近幾次改字，是最上游那份參考圖規格從頭到尾只有「好量」，沒有「好看」。**
我一路往下做，沒有回頭質疑它。

## 修法

參考圖規格改一處：

| | 保留 | 改掉 |
|---|---|---|
| 為了可量可裁 | 正面、頭髮往後露出髮際與整條下顎線、平光、乾淨背景、頭要留白 | — |
| 為了好看 | — | 素顏與證件照調性 → 改成「20–28 歲漂亮女生，五官精緻、上淡妝、氣色好」，即美妝廣告的乾淨正臉照 |

四片素材本身是美女的五官，混出來才會是美女，而且照樣可量、可裁、可做分離度。

## 待決

先請 ChatGPT 按新規格生 6 張驗證（夠裁四槽、混一個人出來看臉），
認可之後再補齊；或者放棄裁切改純文字生美女，代價是 19 位會較像，
分離度得換別的手段。**在使用者點頭之前不再生圖。**
