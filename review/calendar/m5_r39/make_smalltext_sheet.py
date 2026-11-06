"""R39：把最小字與試印重點區以 1:1 成品尺寸（向量）排在 A4 上；以 100% 列印即為成品大小。"""
import sys, pymupdf
H = 'docs/calendar/proof_r39/cal2027_H_R39_試印候選_尚未核准下單.pdf'
V = 'docs/calendar/proof_r39/cal2027_V_R39_試印候選_尚未核准下單.pdf'
MM = 72 / 25.4
ITEMS = [  # (檔, 頁, (x0,y0,x1,y1) 出血座標 mm, 標籤)
    (V, 3, (6, 192.5, 66, 199), '1 直式 第3頁 假日說明 4.1pt 灰字（全書最小字；第3–31頁單數頁同）'),
    (H, 3, (6, 146, 66, 152), '2 橫式 第3頁 假日說明 4.8pt 灰字（第3–25頁單數頁同）'),
    (V, 2, (10, 179, 136, 197), '3 直式 第2頁 照片面日期條：星期 5.4pt＋日期 6.9pt；人名 6.8pt 灰字'),
    (H, 2, (4, 122, 200, 141), '4 橫式 第2頁 照片面日期條：星期／日期 6.5pt；人名 7.4pt 灰字'),
    (V, 31, (6, 27, 70, 66), '5 直式 第31頁 全年年曆：星期 5.7pt＋日期 6.5pt（1–2 月局部）'),
    (V, 1, (28, 130, 116, 194), '6 直式 封面 金色年份＋小藍圖示（深色暗部）'),
    (H, 1, (100, 100, 202, 150), '7 橫式 封面 藍色年份光感＋淺色漸層（局部）'),
]
out = pymupdf.open()
page = out.new_page(width=210 * MM, height=297 * MM)
y = 14 * MM
page.insert_text((12 * MM, 9 * MM), 'TASK-CAL-001 R39 小字與試印重點｜1:1 成品尺寸（以 100% 列印、不要縮放）｜試印候選、尚未核准下單',
                 fontname='china-t', fontsize=7.5)
for path, pno, (x0, y0, x1, y1), label in ITEMS:
    src = pymupdf.open(path)
    w, h = (x1 - x0) * MM, (y1 - y0) * MM
    if y + h + 12 * MM > 290 * MM:
        page = out.new_page(width=210 * MM, height=297 * MM); y = 14 * MM
    page.insert_text((12 * MM, y + 3 * MM), label, fontname='china-t', fontsize=7)
    r = pymupdf.Rect(12 * MM, y + 5 * MM, 12 * MM + w, y + 5 * MM + h)
    page.show_pdf_page(r, src, pno - 1, clip=pymupdf.Rect(x0 * MM, y0 * MM, x1 * MM, y1 * MM))
    page.draw_rect(r, color=(.6, .6, .6), width=0.3)
    y = r.y1 + 6 * MM
out.set_metadata(dict(title='R39 小字與試印重點 1:1 檢查頁（試印候選、尚未核准下單）', producer='cal2027 R39'))
out.save(sys.argv[1], garbage=3, deflate=True)
for i, p in enumerate(out):
    p.get_pixmap(dpi=110).save(sys.argv[1].replace('.pdf', f'_p{i+1}.png'))
print(len(out), 'pages')
