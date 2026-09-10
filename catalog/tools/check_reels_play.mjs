// 「有沒有真的在播」要用畫素證明，不是問 video 元素。
// 上一版我只驗了 videoWidth > 0（那只代表 metadata 載到了），結果影片被首幀蓋住、
// 客戶看到的是「只有聲音，畫面停在封面」。這支改成：
//   ① 影片的矩形要跟舞台重疊（沒有被推到看不見的地方）
//   ② 相隔 1.2 秒截兩張同一塊區域的圖，畫素必須不一樣
//   ③ currentTime 要前進
import { chromium } from 'playwright';
import { spawn } from 'node:child_process';
import crypto from 'node:crypto';

const PORT = process.env.PORT || '8432';
const BASE = process.env.BASE || `http://127.0.0.1:${PORT}`;
let srv = null;
if (!process.env.BASE) {
  srv = spawn('node', ['server.js'], { cwd: '/home/user/Virtual_KOL_Studio/catalog',
    env: { ...process.env, PORT }, stdio: 'ignore' });
  await new Promise(r => setTimeout(r, 900));
}
const b = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args: ['--autoplay-policy=no-user-gesture-required'] });
const md5 = buf => crypto.createHash('md5').update(buf).digest('hex').slice(0, 10);
let fail = 0;

for (const [w, h, tag] of [[1340, 950, '桌機'], [390, 844, '手機']]) {
  const pg = await b.newPage({ viewport: { width: w, height: h }, deviceScaleFactor: 1,
    isMobile: w < 500, hasTouch: w < 500 });
  const errs = []; pg.on('pageerror', e => errs.push(String(e)));
  await pg.goto(BASE + '/reels.html', { waitUntil: 'load' });
  await pg.waitForTimeout(1200);
  await pg.click('.vc');
  await pg.waitForTimeout(2600);

  const geo = await pg.evaluate(() => {
    const st = document.querySelector('.stage'), v = st && st.querySelector('video');
    if (!v) return { err: '沒有 video' };
    const a = st.getBoundingClientRect(), c = v.getBoundingClientRect();
    return {
      舞台: [a.left, a.top, a.width, a.height].map(Math.round).join(','),
      影片: [c.left, c.top, c.width, c.height].map(Math.round).join(','),
      對齊: Math.abs(a.left - c.left) < 2 && Math.abs(a.top - c.top) < 2
        && Math.abs(a.width - c.width) < 2 && Math.abs(a.height - c.height) < 2,
      在畫面內: c.top < window.innerHeight && c.bottom > 0 && c.width > 0,
      可見: getComputedStyle(v).visibility !== 'hidden' && getComputedStyle(v).opacity !== '0',
      t0: v.currentTime, paused: v.paused, videoWidth: v.videoWidth,
    };
  });
  const clip = { x: Math.round(w / 2 - 90), y: Math.round(h / 2 - 90), width: 180, height: 180 };
  const a = md5(await pg.screenshot({ clip }));
  await pg.waitForTimeout(1200);
  const c2 = md5(await pg.screenshot({ clip }));
  const t1 = await pg.evaluate(() => document.querySelector('.stage video').currentTime);

  const ok = geo.對齊 && geo.在畫面內 && geo.可見 && a !== c2 && t1 > geo.t0;
  if (!ok) fail++;
  console.log(`${tag} ${w}×${h} ${ok ? '✅ 真的在播' : '🛑 沒在播'}`);
  console.log(`   舞台 ${geo.舞台}｜影片 ${geo.影片}｜對齊 ${geo.對齊}｜在畫面內 ${geo.在畫面內}`);
  console.log(`   畫面中央 1.2 秒前後：${a} → ${c2}　${a !== c2 ? '有變化' : '一模一樣（＝靜止）'}`);
  console.log(`   currentTime ${geo.t0.toFixed(2)} → ${t1.toFixed(2)}｜paused ${geo.paused}｜JS 錯誤 ${errs.length}`);
  if (tag === '桌機') await pg.screenshot({ path: '/tmp/claude-0/-home-user/8adf1a71-b0cf-561a-9e5c-a38024791086/scratchpad/plays.png' });
  await pg.close();
}
console.log(fail ? `🛑 ${fail} 個尺寸沒在播` : '兩個尺寸都真的在播 ✅');
await b.close();
if (srv) srv.kill();
