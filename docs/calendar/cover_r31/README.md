# 2027 桌曆 非人物封面候選（M-5 R31）— 可編輯來源

候選，未接受。橫式、直式各 A／B：

| 檔案 | 方向 | 畫布（含 2 mm 出血） |
|---|---|---|
| `H-A.svg` | A｜四季光影 | 204×155 mm（成品 200×151） |
| `H-B.svg` | B｜極簡典藏 | 204×155 mm |
| `V-A.svg` | A｜四季光影 | 144×204 mm（成品 140×200） |
| `V-B.svg` | B｜極簡典藏 | 144×204 mm |

- SVG 以 mm 為單位（viewBox＝含出血畫布）。畫面在 `<g id="art">`，細線在 `class="vec"`，文字在 `class="txt"`，文字保留為可編輯文字。
- 字型用相對路徑 `fonts/` 載入；在瀏覽器（Chrome）開啟即可正確顯示。其他軟體需先安裝 `fonts/` 裡的字型。
- 文字只放在文字安全區內：橫式 x 4–200、y 12–151 mm；直式 x 5–139、y 12–199 mm（上緣 12 mm 為線圈假設區）；另再留 3 mm。
- 這些檔案由 `docs/calendar/tools/build_cal_m5_cover_r31.py` 產生；改設計請改工具裡的參數後重跑，不要只改 SVG（否則預覽圖與 PDF 不會跟著更新）。

## 字型（皆為 SIL Open Font License 1.1，授權書在 `fonts/`）

| 檔案 | 用途 | 來源與修改 |
|---|---|---|
| `CormorantGaramond-Light-LF.ttf` | A 的「2027」 | Cormorant Garamond（Christian Thalmann），Google Fonts 開源庫可變字型；固定 wght 300、數字預設改為齊線數字、只保留拉丁字元 |
| `BodoniModa-96-Regular.ttf` | B 的「2027」 | Bodoni Moda（Owen Earl），同上；固定 opsz 96、wght 400、只保留拉丁字元 |
| `Inter-Medium.ttf` | 小字 DESK CALENDAR | Inter（Rasmus Andersson），同上；固定 opsz 14、wght 500、只保留拉丁字元 |

上游檔案與本資料夾檔案的 sha256 記在 `fonts/fonts.json`。OFL 允許修改與嵌入；不得單獨販售字型檔。
