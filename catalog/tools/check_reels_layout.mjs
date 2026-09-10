// 「有沒有擋到臉」不能用看的,要量。
// 臉的區域定義成影片畫面的「中間 56% 寬 × 上半 8%〜52% 高」——直式人像的臉幾乎都落在那裡。
// 客戶 2026-09-10 的截圖裡,「上一支」的箭頭正好壓在額頭上。
import { spawn } from 'node:child_process';
import { createRequire } from 'node:module';
import fs from 'node:fs';
const req = createRequire(import.meta.url);
let chromium = null;
for (const m of ['playwright', '/tmp/node_modules/playwright', '/usr/lib/node_modules/playwright']) {
  try { chromium = req(m).chromium; break; } catch {}
}
if (!chromium) { console.log('這台機器沒有 playwright,跳過影音版面檢查。'); process.exit(0); }
const exe = (() => {
  if (process.env.CHROME_PATH) return process.env.CHROME_PATH;
  try { const d = fs.readdirSync('/opt/pw-browsers').filter(x => /^chromium-/.test(x)).sort().pop();
    const p = `/opt/pw-browsers/${d}/chrome-linux/chrome`; if (fs.existsSync(p)) return p; } catch {}
  return undefined;
})();
const PORT = process.env.PORT || '8440';
const BASE = process.env.BASE || `http://127.0.0.1:${PORT}`;
let srv = null;
if (!process.env.BASE) {
  srv = spawn('node', ['server.js'], { cwd: '/home/user/Virtual_KOL_Studio/catalog',
    env: { ...process.env, PORT }, stdio: 'ignore' });
  await new Promise(r => setTimeout(r, 900));
}
const b = await chromium.launch({ executablePath: exe, args: ['--autoplay-policy=no-user-gesture-required'] });
let bad = 0;
for (const [w, h, tag] of [[1340, 950, '桌機'], [390, 844, '手機']]) {
  const pg = await b.newPage({ viewport: { width: w, height: h }, isMobile: w < 500, hasTouch: w < 500 });
  await pg.goto(BASE + '/reels.html', { waitUntil: 'load' });
  await pg.waitForTimeout(1000);
  await pg.click('.vc');
  await pg.waitForTimeout(1500);
  // 先換到第 3 支,這樣「上一支」也會出現
  await pg.evaluate(() => { const f = document.getElementById('rfeed');
    f.scrollTo({ top: f.clientHeight * 2, behavior: 'instant' }); });
  await pg.waitForTimeout(1600);
  const r = await pg.evaluate(() => {
    const st = document.querySelector(`[data-stage="2"]`) || document.querySelector('.stage');
    const s = st.getBoundingClientRect();
    const face = { l: s.left + s.width * 0.22, r: s.left + s.width * 0.78,
                   t: s.top + s.height * 0.08, b: s.top + s.height * 0.52 };
    const hit = [];
    for (const [id, name] of [['rprev', '上一支'], ['rnext', '下一支'], ['rmute', '聲音鈕'],
                              ['rtip', '提示字'], ['rclose', '關閉'], ['rcount', '計數']]) {
      const el = document.getElementById(id);
      if (!el || el.hidden || getComputedStyle(el).display === 'none') continue;
      const c = el.getBoundingClientRect();
      if (c.left < face.r && c.right > face.l && c.top < face.b && c.bottom > face.t)
        hit.push(`${name}(${Math.round(c.left)},${Math.round(c.top)})`);
    }
    return { 舞台: [s.left, s.top, s.width, s.height].map(Math.round).join(','),
      臉區: [face.l, face.t, face.r - face.l, face.b - face.t].map(Math.round).join(','), hit };
  });
  const ok = r.hit.length === 0;
  if (!ok) bad++;
  console.log(`${tag} ${w}×${h} ${ok ? '✅ 臉的區域沒有東西壓著' : '🛑 壓到臉：' + r.hit.join('、')}`);
  console.log(`   舞台 ${r.舞台}｜臉區 ${r.臉區}`);
  await pg.close();
}
console.log(bad ? `🛑 ${bad} 個尺寸有東西壓到臉` : '兩個尺寸都沒有壓到臉 ✅');
await b.close();
if (srv) srv.kill();
process.exit(bad ? 1 : 0);
