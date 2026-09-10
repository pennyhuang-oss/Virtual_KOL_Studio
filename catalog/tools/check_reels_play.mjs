// 影音頁「有沒有真的在播」的檢查。
//
// 🛑 兩件一定要知道的事，不然這支的結果會被讀錯：
//
// ① 「在播」要用畫素證明，不能問 video 元素。
//    2026-09-10 客戶回報「只有聲音、畫面停在封面」——首幀當時是獨立的 <div>，
//    跟 <video> 並排在版面裡各佔一整屏，影片被排到看不見的地方。
//    而我當時的檢查看的是 videoWidth > 0（只代表 metadata 到了），所以它「通過」了。
//
// ② 這個容器的 Chromium 沒有 H.264。
//    48 支素材是 avc1 + mp4a（用 box 結構驗過），真瀏覽器都播得動，
//    但這裡只播得動有 WebM 備援的那 6 支。所以這支腳本會印出它實際用了哪一個檔案，
//    看到 .mp4 播不動不要當成素材壞了——那是這台機器的解碼器缺H.264。
//
// 用法：node tools/check_reels_play.mjs            （本機 public/）
//       BASE=http://127.0.0.1:8300 node ...        （對著別的來源，例如線上鏡像）
import { spawn } from 'node:child_process';
import { createRequire } from 'node:module';
import fs from 'node:fs';

// playwright 與 Chromium 都不是這個 repo 的東西,位置每台機器不一樣。
// 找不到就直接跳過（回 0）——這支是輔助檢查,不該讓沒有瀏覽器的環境整個失敗。
const req = createRequire(import.meta.url);
let chromium = null;
for (const m of ['playwright', '/tmp/node_modules/playwright', '/usr/lib/node_modules/playwright']) {
  try { chromium = req(m).chromium; break; } catch {}
}
if (!chromium) { console.log('這台機器沒有 playwright,跳過影音播放檢查。'); process.exit(0); }
const exe = (() => {
  if (process.env.CHROME_PATH) return process.env.CHROME_PATH;
  const root = '/opt/pw-browsers';
  try {
    const d = fs.readdirSync(root).filter(x => /^chromium-/.test(x)).sort().pop();
    const p = `${root}/${d}/chrome-linux/chrome`;
    if (fs.existsSync(p)) return p;
  } catch {}
  return undefined;                       // 交給 playwright 自己找
})();

const PORT = process.env.PORT || '8439';
const BASE = process.env.BASE || `http://127.0.0.1:${PORT}`;
const WALK = Number(process.env.WALK || 8);
let srv = null;
if (!process.env.BASE) {
  srv = spawn('node', ['server.js'], { cwd: new URL('..', import.meta.url).pathname,
    env: { ...process.env, PORT }, stdio: 'ignore' });
  await new Promise(r => setTimeout(r, 900));
}
const b = await chromium.launch({ executablePath: exe,
  args: ['--autoplay-policy=no-user-gesture-required'] });
let fail = 0, viaMp4 = 0, viaWebm = 0;

// ── ① 畫素會動嗎（第一支，桌機與手機各一次）
for (const [w, h, tag] of [[1340, 950, '桌機'], [390, 844, '手機']]) {
  const pg = await b.newPage({ viewport: { width: w, height: h }, isMobile: w < 500, hasTouch: w < 500 });
  const errs = []; pg.on('pageerror', e => errs.push(String(e)));
  await pg.goto(BASE + '/reels.html', { waitUntil: 'load' });
  await pg.waitForTimeout(1100);
  await pg.click('.vc');
  await pg.waitForTimeout(2600);
  const geo = await pg.evaluate(() => {
    const st = document.querySelector('.stage'), v = st && st.querySelector('video');
    if (!v) return { err: '沒有 video' };
    const a = st.getBoundingClientRect(), c = v.getBoundingClientRect();
    return {
      對齊: Math.abs(a.left - c.left) < 2 && Math.abs(a.top - c.top) < 2
        && Math.abs(a.width - c.width) < 2 && Math.abs(a.height - c.height) < 2,
      在畫面內: c.top < window.innerHeight && c.bottom > 0 && c.width > 0,
      可見: getComputedStyle(v).visibility !== 'hidden' && getComputedStyle(v).opacity !== '0',
      t0: v.currentTime, src: (v.currentSrc || '').split('/').pop().split('?')[0],
    };
  });
  const clip = { x: Math.round(w / 2 - 90), y: Math.round(h / 2 - 90), width: 180, height: 180 };
  const a = (await pg.screenshot({ clip })).toString('base64').slice(0, 64);
  await pg.waitForTimeout(1200);
  const c2 = (await pg.screenshot({ clip })).toString('base64').slice(0, 64);
  const t1 = await pg.evaluate(() => document.querySelector('.stage video').currentTime);
  const ok = geo.對齊 && geo.在畫面內 && geo.可見 && a !== c2 && t1 > geo.t0;
  if (!ok) fail++;
  console.log(`${tag} ${w}×${h} ${ok ? '✅ 畫面真的在動' : '🛑 畫面沒動'}`
    + `（矩形對齊 ${geo.對齊}／在畫面內 ${geo.在畫面內}／畫素有變 ${a !== c2}／時間 ${geo.t0?.toFixed(2)}→${t1?.toFixed(2)}）`);
  console.log(`   實際播的是 ${geo.src}`);
  await pg.close();
}

// ── ② 逐支走一遍：換片之後有沒有真的接上
const pg = await b.newPage({ viewport: { width: 1340, height: 950 } });
await pg.goto(BASE + '/reels.html', { waitUntil: 'load' });
await pg.waitForTimeout(900);
await pg.click('.vc'); await pg.waitForTimeout(2500);
const dead = [];
for (let i = 0; i < WALK; i++) {
  if (i) await pg.evaluate(() => { const f = document.getElementById('rfeed');
    f.scrollTo({ top: f.scrollTop + f.clientHeight, behavior: 'instant' }); });
  await pg.waitForTimeout(2500);
  const s = await pg.evaluate(() => { const n = Number(document.getElementById('rcount').textContent.split(' / ')[0]) - 1;
    const v = document.querySelector(`[data-stage="${n}"] video`);
    return { n, rs: v?.readyState, ns: v?.networkState, t: v ? v.currentTime : null,
      src: (v?.currentSrc || '').split('/').pop().split('?')[0] }; });
  await pg.waitForTimeout(1000);
  const t2 = await pg.evaluate(() => { const n = Number(document.getElementById('rcount').textContent.split(' / ')[0]) - 1;
    const v = document.querySelector(`[data-stage="${n}"] video`); return v ? v.currentTime : null; });
  const played = s.rs >= 2 && t2 > s.t;
  if (/\.webm$/.test(s.src)) viaWebm++; else if (/\.mp4$/.test(s.src)) viaMp4++;
  if (!played) dead.push(`第 ${s.n + 1} 支 ${s.src}`);
  console.log(`   第 ${String(s.n + 1).padStart(2)} 支 ${played ? '✅' : '⚠ '} ${s.src}`
    + `（readyState ${s.rs}／networkState ${s.ns}）`);
}
console.log(`走過 ${WALK} 支：WebM 播成功 ${viaWebm} 支、MP4 ${viaMp4} 支`);
if (dead.length) console.log(`⚠ 這幾支在這台機器上播不動（幾乎一定是缺 H.264，不是素材壞了）：\n   ${dead.join('\n   ')}`);
console.log(fail ? `🛑 有 ${fail} 個尺寸畫面沒在動——這是真的壞了` : '✅ 版面正確：影片有蓋在首幀上、畫素會動');
await b.close();
if (srv) srv.kill();
process.exit(fail ? 1 : 0);
