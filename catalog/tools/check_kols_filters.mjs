// 「捲下去看得到幾排人設」要用量的。
// 使用者 2026-09-10：篩選列黏在上面，每次滑下去只剩一排。
import { spawn } from 'node:child_process';
import { createRequire } from 'node:module';
import fs from 'node:fs';
const req = createRequire(import.meta.url);
let chromium = null;
for (const m of ['playwright', '/tmp/node_modules/playwright', '/usr/lib/node_modules/playwright']) {
  try { chromium = req(m).chromium; break; } catch {}
}
if (!chromium) { console.log('這台機器沒有 playwright,跳過篩選列檢查。'); process.exit(0); }
const exe = (() => {
  if (process.env.CHROME_PATH) return process.env.CHROME_PATH;
  try { const d = fs.readdirSync('/opt/pw-browsers').filter(x => /^chromium-/.test(x)).sort().pop();
    const p = `/opt/pw-browsers/${d}/chrome-linux/chrome`; if (fs.existsSync(p)) return p; } catch {}
  return undefined;
})();
const PORT = process.env.PORT || '8442';
const BASE = process.env.BASE || `http://127.0.0.1:${PORT}`;
let srv = null;
if (!process.env.BASE) {
  srv = spawn('node', ['server.js'], { cwd: '/home/user/Virtual_KOL_Studio/catalog',
    env: { ...process.env, PORT }, stdio: 'ignore' });
  await new Promise(r => setTimeout(r, 900));
}
const b = await chromium.launch({ executablePath: exe });
for (const [w, h, tag] of [[1440, 900, '桌機'], [390, 844, '手機']]) {
  const pg = await b.newPage({ viewport: { width: w, height: h }, isMobile: w < 500, hasTouch: w < 500 });
  await pg.goto(BASE + '/kols.html', { waitUntil: 'load' });
  await pg.waitForTimeout(900);
  // 捲到中段
  await pg.evaluate(() => window.scrollTo({ top: 1800, behavior: 'instant' }));
  await pg.waitForTimeout(700);
  const r = await pg.evaluate(() => {
    const top = document.querySelector('.top').getBoundingClientRect().height;
    const mini = document.getElementById('minif');
    const mh = mini && !mini.hidden ? mini.getBoundingClientRect().height : 0;
    const panel = document.querySelector('.filters').getBoundingClientRect();
    // 完全看得到的卡片有幾張（不能被頁首或細列蓋住）
    const guard = top + mh;
    const cards = [...document.querySelectorAll('.cell:not([hidden])')].filter(c => {
      const b = c.getBoundingClientRect();
      return b.top >= guard - 1 && b.bottom <= window.innerHeight + 1;
    });
    return { 頁首: Math.round(top), 細列高: Math.round(mh), 細列出現: mini ? !mini.hidden : null,
      篩選列還黏著: panel.top >= 0 && panel.bottom > guard,
      完整看得到的卡片: cards.length,
      細列內容: mini && !mini.hidden ? mini.innerText.replace(/\s+/g, ' ').trim() : '' };
  });
  console.log(`${tag} ${w}×${h}｜頁首 ${r.頁首} ＋ 細列 ${r.細列高} = 被佔 ${r.頁首 + r.細列高}px`);
  console.log(`   細列出現 ${r.細列出現}｜舊的篩選列還黏著 ${r.篩選列還黏著}｜完整看得到 ${r.完整看得到的卡片} 張卡`);
  console.log(`   細列寫著：${r.細列內容}`);
  // 篩選之後細列要跟著更新
  await pg.evaluate(() => window.scrollTo({ top: 0, behavior: 'instant' }));
  await pg.waitForTimeout(400);
  await pg.click('.chip[data-f="med"][data-v="video"]');
  await pg.evaluate(() => window.scrollTo({ top: 1500, behavior: 'instant' }));
  await pg.waitForTimeout(700);
  console.log('   選「有影片素材」後細列：', await pg.evaluate(() => {
    const m = document.getElementById('minif');
    return m.hidden ? '（沒出現）' : m.innerText.replace(/\s+/g, ' ').trim(); }));
  // 「篩選 ↑」要能回到上面
  await pg.click('#mfgo');
  await pg.waitForTimeout(1200);
  console.log('   按「篩選 ↑」後 scrollY =', await pg.evaluate(() => Math.round(window.scrollY)),
    '｜細列', await pg.evaluate(() => document.getElementById('minif').hidden ? '已收起 ✅' : '還在 🛑'));
  await pg.close();
}
await b.close();
if (srv) srv.kill();
