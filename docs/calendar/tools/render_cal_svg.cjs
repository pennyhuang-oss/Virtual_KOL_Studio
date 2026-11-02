// 用 Chromium 把封面 SVG 轉成指定像素的 PNG（SVG 會拉滿畫面）。字型由 SVG 內的 @font-face 以相對路徑載入，必須全部載入成功才輸出。
// 用法：node render_cal_svg.cjs <svg> <out.png> <寬 px> <高 px> [隱藏的 class，逗號分隔]
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
(async () => {
  const [svgPath, out, w, h, hide] = process.argv.slice(2);
  const dir = path.dirname(path.resolve(svgPath));
  const svg = fs.readFileSync(svgPath, 'utf8').replace(/^<\?xml[^>]*>\s*/, '');
  const hideCss = (hide || '').split(',').filter(Boolean).map(c => `.${c}{display:none}`).join('');
  const html = `<!doctype html><html><head><meta charset="utf-8"><style>html,body{margin:0;padding:0;background:#fff}body>svg{display:block;width:${w}px;height:${h}px}${hideCss}</style></head><body>${svg}</body></html>`;
  const tmp = path.join(dir, `.render_${process.pid}.html`);
  fs.writeFileSync(tmp, html);
  const browser = await chromium.launch();
  try {
    const page = await browser.newPage({ viewport: { width: +w, height: +h }, deviceScaleFactor: 1 });
    await page.goto('file://' + tmp, { waitUntil: 'load' });
    await page.evaluate(() => document.fonts.ready);
    const bad = await page.evaluate(() => [...document.fonts].filter(f => f.status !== 'loaded').map(f => `${f.family}:${f.status}`));
    if (bad.length) throw new Error('字型沒有載入：' + bad.join(', '));
    await page.screenshot({ path: out });
  } finally {
    await browser.close();
    fs.unlinkSync(tmp);
  }
})().catch(e => { console.error(e.message || e); process.exit(1); });
