// TASK-CAL-001／M-4／R5 定向驗證：第一批 5 位生成紀錄（授權、送出 prompt、原圖、扣款）、企劃 v11、CAL_22；
// 目前檢視頁一次看一位（切換、大圖、原尺寸、下載、套框）、回饋保存與整批複製（未回覆不算接受）、Iris 已接受紀錄、舊資料不變、公開內容沒有私有識別碼。
// 用法：node review/calendar/m4_r5/live_check/check_m4r5.cjs <baseURL> <outdir> review/calendar/m4_r5/live_check/seed_state.json
// （seed_state.json 是測試瀏覽器的舊資料樣本，不是 Penny 的真實回饋；只寫進測試瀏覽器，不會影響 Penny 的瀏覽器）
const { chromium } = require('playwright');
const fs = require('fs');
const crypto = require('crypto');
const { execSync } = require('child_process');
const [base, out, seedFile] = process.argv.slice(2);
fs.mkdirSync(out, { recursive: true });
const REPO = '/home/user/Virtual_KOL_Studio';
const PUB = `${REPO}/docs/calendar/decision_site/public`;
const SEED = JSON.parse(fs.readFileSync(seedFile, 'utf8'));
const FIXED = '4fd3995cd75f726b19cb55c9c7f1e62a11a3cc45';
const KEY = 'cal2027-shoot-v1:' + FIXED, MKEY = 'cal2027-materials-v1:' + FIXED, RKEY = 'cal2027-review-v1:V-iris-chen-m4r2';
const R3FB = JSON.stringify({ v: 1, photo: 'V-iris-chen:M-4 R3', choice: 'accept', note: '測試：R3 留在瀏覽器的回饋', saved: '2026-10-20 18:00' });
const BASE_RESULT = 'b5cbe1c563df4a6252cc842ceeaccc2d358e2e6b', BASE_REVIEW = 'd09975652a751dd17a45d2aaf5c83b4dc4b18f5c';
const J = x => JSON.stringify(x);
const rd = f => fs.readFileSync(`${REPO}/${f}`, 'utf8');
const P = JSON.parse(rd('docs/calendar/data/cal_m3_shoot_plan.json'));
const PB = JSON.parse(execSync(`git show ${BASE_RESULT}:docs/calendar/data/cal_m3_shoot_plan.json`, { cwd: REPO, maxBuffer: 64 << 20 }).toString());
const B = JSON.parse(rd('docs/calendar/data/cal_m4_batch1_prep.json'));
const A = JSON.parse(rd('docs/calendar/data/cal_m4_auth_r5.json'));
const U = JSON.parse(rd('docs/calendar/data/cal_m4_batch1_run.json'));
const RV = JSON.parse(rd('docs/calendar/data/cal_review_current.json'));
const D22 = rd('docs/calendar/CAL_22_M4_BATCH1_RESULTS.md');
const D21 = rd('docs/calendar/CAL_21_M4_BATCH1_PREP.md');
const LOG = JSON.parse(rd('review/calendar/m4_r5/execution_log.json')).events;
const UUID = /[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/g;
const PIDS = ['iris-chen', 'tammy-chou', 'rin-ayase', 'somi-oh', 'yerin-han', 'jia-seo'];
const prof = pid => JSON.parse(rd(`kols/${pid}/profile.json`)).ai_assets.training_images_v1.soul_training;
const SOULS = PIDS.map(p => prof(p).soul_id);
const JOBS = [...new Set([...rd('review/calendar/m4_r2/execution_log.json').match(UUID), ...rd('review/calendar/m4_r5/execution_log.json').match(UUID)])];
const SECRETS = [...new Set([...SOULS, ...JOBS])].flatMap(x => [x, x.replace(/-/g, '')]);
const hasSecret = b => SECRETS.some(s => b.includes(Buffer.from(s)));
const TX = /\d{2}:\d{2}:\d{2}|\d{1,2}-\d{2} \d{2}:\d{2}|列 Nano Banana|個 nano_banana|筆交易|秒 \+0/;
const SETS = ['V-tammy-chou', 'V-rin-ayase', 'V-somi-oh', 'H-yerin-han', 'H-jia-seo'];
const BK = s => 'cal2027-batch1-v1:' + s;
const results = [];
const ok = (name, cond, info = '') => { results.push([cond ? 'PASS' : 'FAIL', name, info]); console.log((cond ? 'PASS' : 'FAIL') + '\t' + name + '\t' + info); };
const overflow = p => p.evaluate(() => document.scrollingElement.scrollWidth - window.innerWidth);
const sha = b => crypto.createHash('sha256').update(b).digest('hex');
const pngText = b => { const out = []; let i = 8; while (i < b.length) { const n = b.readUInt32BE(i), t = b.slice(i + 4, i + 8).toString(); if (['tEXt', 'iTXt', 'zTXt'].includes(t)) out.push(t); i += 12 + n; } return out; };

(async () => {
  // ---------- 授權與生成紀錄 ----------
  ok('主管 R5 指令逐字保存；範圍 5 套、每套 1 次、共最多 5 次、額度 0.60', A.verbatim.split('\n')[0] === 'TASK-CAL-001／M-4／R5｜第一批5位角色生成與上線審圖' && J(A.scope.sets) === J(SETS) &&
    A.scope.requests_max === 5 && A.scope.per_set === 1 && A.scope.budget_credits === 0.6 && A.scope.quote_max_each === 0.12);
  const subs = LOG.filter(e => / submitted$/.test(e.step)), terms = LOG.filter(e => / terminal$/.test(e.step)), intents = LOG.filter(e => / intent$/.test(e.step));
  ok('私有執行紀錄：5 次提交意圖、5 次送出（各一個工作 ID、不重複）、5 次終態 completed，依名單順序；送出都在提交意圖之後', subs.length === 5 && terms.length === 5 && intents.length === 5 &&
    new Set(subs.map(e => e.job_id)).size === 5 && J(subs.map(e => e.set)) === J(SETS) && terms.every(e => e.status === 'completed') && subs.every((e, i) => e.t >= intents[i].t));
  ok('重啟處理有紀錄：第 5 張送出前查過沒有重複提交', LOG.some(e => e.step === '5 H-jia-seo restart-check' && /沒有重複提交/.test(e.note)));
  const X = Object.fromEntries(B.sets.map(x => [x.id, x]));
  ok('送出 prompt：V-Rin＝CAL_21 原文只換授權的景別句；其餘 4 份逐字等於 CAL_21；sha256 與提交意圖相同', U.sets.every(z => {
    const want = z.id === 'V-rin-ayase' ? X[z.id].prompt.replace(A.prompt_fix.before, A.prompt_fix.after) : X[z.id].prompt;
    const it = intents.find(e => e.set === z.id);
    return z.prompt_final === want && sha(Buffer.from(want)) === z.prompt_sha256 && it.prompt_sha256 === z.prompt_sha256; }) && U.sets.find(z => z.id === 'V-rin-ayase').prompt_final.includes('Shot: framed from a little above her head') &&
    !U.sets.find(z => z.id === 'V-rin-ayase').prompt_final.includes('knee-up'));
  ok('設定：soul_2、2k、count 1、use_unlim false、無參考圖、不傳 style_id；比例 3:4×3、16:9×2', intents.every(e => e.settings.model === 'soul_2' && e.settings.quality === '2k' && e.settings.count === 1 && e.settings.use_unlim === false && e.settings.medias === 'none' && e.settings.style_id === 'none') &&
    J(intents.map(e => e.settings.aspect_ratio)) === J(['3:4', '3:4', '3:4', '16:9', '16:9']));
  ok('原圖 5 張：sha256 與紀錄相同、像素 1536×2048×3／2048×1152×2、私有原檔保留工作 ID 文字區塊', U.sets.every(z => { const b = fs.readFileSync(`${REPO}/${z.result.path}`); return sha(b) === z.result.sha256 && b.length === z.result.bytes && pngText(b).includes('tEXt'); }) &&
    J(U.sets.map(z => z.result.px)) === J([[1536, 2048], [1536, 2048], [1536, 2048], [2048, 1152], [2048, 1152]]));
  ok('扣款：每張精確報價 0.12、時窗內 Soul V2 −0.12 一筆、無退款；合計 0.60 ≤ 額度 0.60；歸屬「依時窗及唯一任務推定」', U.sets.every(z => z.quote.credits_exact === 0.12 && z.charge.rows.length === 1 && z.charge.rows[0].credits === -0.12 && z.charge.refunds.length === 0 && z.charge.attribution === '依時窗及唯一任務推定') &&
    U.charges.charged_total === 0.6 && U.charges.budget === 0.6);
  ok('15 分鐘複查有紀錄：本批無遲到扣款或退款；之後另一筆 Soul V2 判定不屬本批（依時間與任務 ID）', LOG.some(e => e.step === 'late recheck' && e.late_charges_for_batch === 0 && e.batch_net === 0.6 && e.after_batch.ours === false) && /不屬本批/.test(U.charges.late_recheck.after_batch));
  ok('結果資料檔不含工作 ID 或 Soul ID', !new RegExp(UUID.source).test(rd('docs/calendar/data/cal_m4_batch1_run.json')));
  ok('驗收：5 張都記錄身分髮型、身材、服裝、手腳、表情視線、場景、光線、構圖、質感與主管指定重點；不寫量測三圍或罩杯', U.sets.every(z => ['identity', 'body', 'outfit', 'hands_feet', 'expression_gaze', 'scene', 'light', 'composition', 'texture'].every(k => z.acceptance[k].length > 8) && z.acceptance.focus.length >= 3 && /不從照片推量尺寸/.test(z.acceptance.body)) &&
    !U.sets.some(z => /\d+\s*cm|[A-H] ?罩杯|罩杯 ?[A-H]/.test(J(z.acceptance))));
  ok('ppi：直式 325、橫式 271 標「低於 300 工作目標」，不重生、不放大', U.sets.every(z => z.ppi.effective === (z.id[0] === 'V' ? 325 : 271) && z.ppi.below_target === (z.id[0] === 'H')) && U.counts.upscaled === 0 && U.counts.retouched === 0 && /不重生、不放大/.test(U.sets[3].ppi.how));
  // ---------- 企劃與文件 ----------
  const PR = P.status.production;
  ok('企劃 shoot-plan-v11（M-4 R5）：已生成 6、已接受 1、待 Penny 看圖 5、其餘 18；累計 credits 0.72', P.version === 'shoot-plan-v11' && P.round === 'M-4 R5' && PR.generated === 6 && PR.accepted === 1 && PR.pending_owner_review === 5 && PR.remaining === 18 &&
    J(P.counts) === J({ generated: 6, credits: 0.72, trainings: 0 }) && P.batch1.status === 'generated-pending-owner-review');
  ok('24 套企劃、月份、M-4 R2/R4 紀錄與 b5cbe1c 相同', J(P.sets) === J(PB.sets) && J(P.months) === J(PB.months) && J(P.m4_prep) === J(PB.m4_prep) && J(P.m4r4) === J(PB.m4r4));
  const kept = execSync(`git diff --name-only --diff-filter=DMRT ${BASE_REVIEW} -- review/calendar kols docs/calendar/data/cal_m4_batch1_prep.json docs/calendar/data/cal_m4_owner_r4.json docs/calendar/data/cal_m4_auth_r5.json docs/calendar/CAL_19_M3_R2_OWNER_DECISION.md`, { cwd: REPO }).toString().trim();
  ok('既有證據、R4 準備資料、owner 紀錄、CAL_19 不刪不改', kept === '', kept);
  ok('CAL_22：第一行 R5 報告；5 份最終送出文字逐字在文件；V-Rin 修改前後；逐筆扣款與 15 分鐘複查；ppi 271 低於目標', D22.split('\n')[0] === 'TASK-CAL-001／M-4／R5｜第一批5位角色生成與上線審圖｜送審報告' &&
    U.sets.every(z => D22.includes(z.prompt_final) && D22.includes(z.charge.rows[0].at)) && D22.includes(A.prompt_fix.before) && D22.includes(A.prompt_fix.after) && /15 分鐘複查/.test(D22) && /271（低於 300 工作目標）/.test(D22) && !new RegExp(UUID.source).test(D22));
  ok('CAL_21 保留 R4 準備內容，標「M-4 R5 已依本文件生成」', /M-4 R5 已依本文件生成/.test(D21) && B.sets.every(x => D21.includes(x.prompt)));
  // ---------- 公開內容 ----------
  const pubFiles = execSync('find . -type f', { cwd: PUB }).toString().trim().split('\n');
  const leak = pubFiles.filter(f => hasSecret(fs.readFileSync(`${PUB}/${f}`)));
  ok('公開資料夾沒有任何 Soul ID 或工作 ID（含去連字號寫法；6 個 Soul＋首試與第一批工作 ID）', leak.length === 0 && SECRETS.length >= 24, leak.join(','));
  const rvd = fs.readFileSync(`${PUB}/review-data.js`, 'utf8');
  ok('目前檢視頁資料沒有 prompt、交易、repo 路徑或 ID', !/Lighting:|She wears|Natural skin|credit|扣款|交易|kols\/|review\/calendar|job|soul/i.test(rvd) && !TX.test(rvd) && !/[0-9a-f]{12,}/.test(rvd));
  ok('公開原圖 5 張：沒有文字中繼資料區塊，像素與私有原檔相同（builder --check 已逐位元組重現）', U.sets.every(z => { const b = fs.readFileSync(`${PUB}/img/review/${z.id}_m4r5.png`); return pngText(b).length === 0 && !hasSecret(b); }));
  const pubText = ['data.js', 'review-data.js', 'shoot.html', 'review.js', 'history.js'].map(f => fs.readFileSync(`${PUB}/${f}`, 'utf8')).join('');
  ok('公開頁面沒有交易原始資料（時間、他人交易列）', !TX.test(pubText));

  // ---------- 瀏覽器 ----------
  const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome' });
  for (const vp of [{ name: 'desktop', width: 1366, height: 900 }, { name: 'mobile390', width: 390, height: 844, isMobile: true, hasTouch: true, deviceScaleFactor: 3 }]) {
    const V = `[${vp.name}]`;
    const ctx = await browser.newContext({ viewport: { width: vp.width, height: vp.height }, isMobile: !!vp.isMobile, hasTouch: !!vp.hasTouch, deviceScaleFactor: vp.deviceScaleFactor || 1, acceptDownloads: true });
    await ctx.grantPermissions(['clipboard-read', 'clipboard-write'], { origin: base });
    const p = await ctx.newPage();
    const errs = [];
    p.on('pageerror', e => errs.push(String(e)));
    p.on('console', m => { if (m.type() === 'error') errs.push(m.text()); });
    await p.goto(base + '/index.html');
    await p.evaluate(([a, b, c, d, e, f]) => { localStorage.setItem(a, b); localStorage.setItem(c, d); localStorage.setItem(e, f); }, [KEY, SEED.shoot, MKEY, SEED.mat, RKEY, R3FB]);
    const same = async () => J(await p.evaluate(k => k.map(x => localStorage.getItem(x)), [KEY, MKEY, RKEY])) === J([SEED.shoot, SEED.mat, R3FB]);
    const allKeys = () => p.evaluate(() => Object.keys(localStorage).sort());
    await p.goto(base + '/shoot.html', { waitUntil: 'networkidle' });
    await p.waitForSelector('#photo .ph img');
    const m = await p.evaluate(() => ({ secs: Array.from(document.querySelectorAll('main > section, main > nav')).map(s => s.id || s.className), imgs: document.querySelectorAll('main img').length, tables: document.querySelectorAll('main table').length,
      text: document.querySelector('main').innerText, h: document.scrollingElement.scrollHeight, vh: window.innerHeight }));
    ok(`${V} 主頁：5 位導覽＋一位的照片、回饋、看圖提醒、套框、本批回饋、已接受紀錄、歷史連結；只有 2 張圖（照片與套框），沒有網格或表格`, J(m.secs) === J(['pn', 'photo', 'fb', 'check', 'frame', 'copy', 'acc', 'hist']) && m.imgs === 2 && m.tables === 0, `高 ${m.h}px（${(m.h / m.vh).toFixed(1)} 屏）`);
    ok(`${V} 進度一行：已生成 6、已接受 1、待你看 5、其餘 18`, (await p.locator('#prog').innerText()).trim() === RV.progress);
    const nav = await p.locator('.pn-b').allInnerTexts();
    ok(`${V} 導覽 5 位依序（Tammy、Rin、Somi、Yerin、Jia），預設第 1 位、全部「未回覆」`, nav.length === 5 && ['Tammy', 'Rin', 'Somi', 'Yerin', 'Jia'].every((n, i) => nav[i].includes(n) && nav[i].includes('未回覆')) && (await p.locator('.pn-b.on').innerText()).includes('Tammy'));
    ok(`${V} 主頁沒有 prompt、費用或交易資料`, !/Lighting:|She wears|credit|0\.12|報價|扣款|交易/.test(m.text));
    ok(`${V} 新頁面沒有寫入任何回饋鍵（未回覆不建立資料）`, !(await allKeys()).some(k => k.startsWith('cal2027-batch1-v1:')));
    const ph = await p.evaluate(() => { const i = document.querySelector('#photo .ph img'), r = i.getBoundingClientRect(); return { top: r.top, h: r.height, vh: window.innerHeight }; });
    ok(`${V} 照片在第一屏`, ph.top < ph.vh * 0.6, `top ${Math.round(ph.top)}`);
    await p.screenshot({ path: `${out}/${vp.name}_tammy_top.jpg`, type: 'jpeg', quality: 80 });
    // 逐位切換：一次只有一張照片，圖、標題、套框、提醒、下載檔名都跟著換
    for (const i of [1, 2, 3, 4, 0]) {  // 預設已在第 1 位（網址沒有 #）；最後從 Jia 切回 Tammy
      const s = RV.batch.photos[i];
      await p.locator(`.pn-b[data-go="${i}"]`).click();
      await p.waitForFunction(src => document.querySelector('#photo .ph img').getAttribute('src') === src, `img/review/${s.set}_m4r5_view.jpg`);
      await p.waitForFunction(() => document.querySelector('#photo .ph img').complete && document.querySelector('#photo .ph img').naturalWidth > 0);
      const st = await p.evaluate(() => ({ imgs: document.querySelectorAll('main img').length, cap: document.querySelector('#photo figcaption').innerText, fr: document.querySelector('#frame img').getAttribute('src'),
        dl: document.getElementById('dl').getAttribute('download'), ck: Array.from(document.querySelectorAll('#check li')).map(x => x.innerText), hash: location.hash, nat: document.querySelector('#photo .ph img').naturalWidth }));
      ok(`${V} 切到 ${s.name}：只顯示這一位（2 張圖）、標題、套框、看圖提醒、下載檔名都對；網址記住 #${s.set}`, st.imgs === 2 && st.cap.includes(s.title) && st.fr === `img/review/${s.frame_src.path.split('/').pop()}` && st.dl === s.download_name &&
        J(st.ck) === J(s.checks) && st.hash === '#' + s.set && st.nat === (s.set[0] === 'V' ? 1200 : 1600));
    }
    // 大圖與原尺寸：直式（Tammy）與橫式（Jia）
    for (const [i, w] of [[0, 1536], [4, 2048]]) {
      await p.locator(`.pn-b[data-go="${i}"]`).click();
      await p.click('#photo .ph .zoom');
      await p.waitForSelector('#viewer:not([hidden])');
      await p.click('#viewer-mode');
      await p.waitForFunction(([src, w]) => document.getElementById('viewer-img').currentSrc.endsWith(src) && document.getElementById('viewer-img').naturalWidth === w, [`${RV.batch.photos[i].set}_m4r5.png`, w], { timeout: 30000 });
      const cap = await p.locator('#viewer-cap').innerText();
      await p.keyboard.press('Escape');
      await p.waitForSelector('#viewer', { state: 'hidden' });
      ok(`${V} ${RV.batch.photos[i].name} 大圖→原尺寸（原圖 ${w} px 寬），Esc 關閉`, /原圖/.test(cap) && await p.locator('#viewer').isHidden());
    }
    // 套框大圖
    await p.locator('#frame .zoom').click();
    await p.waitForSelector('#viewer:not([hidden])');
    await p.waitForFunction(() => document.getElementById('viewer-img').naturalWidth === 1304);
    await p.locator('#viewer-close').click();
    await p.waitForSelector('#viewer', { state: 'hidden' });
    ok(`${V} 套框預覽（Jia 橫式 1304 px）可放大、關閉；標「不是印刷核准」；註明 271 ppi 低於工作目標`, /不是印刷核准/.test(await p.locator('#frame figcaption').innerText()) && /271 ppi，低於本案 300 ppi 工作目標/.test(await p.locator('#frame figcaption').innerText()));
    // 下載：Yerin
    await p.locator('.pn-b[data-go="3"]').click();
    const [d] = await Promise.all([p.waitForEvent('download'), p.locator('#dl').click()]);
    const db = fs.readFileSync(await d.path());
    ok(`${V} 下載 Yerin 原圖：${d.suggestedFilename()}、與發佈檔相同、沒有文字區塊與工作 ID`, d.suggestedFilename() === 'H-yerin-han_M4R5_2048x1152.png' && sha(db) === sha(fs.readFileSync(`${PUB}/img/review/H-yerin-han_m4r5.png`)) && pngText(db).length === 0 && !hasSecret(db));
    // 回饋：Tammy 接受；Rin 想修改＋備註；Somi 只寫備註（不算接受）；Yerin、Jia 不回覆
    await p.locator('.pn-b[data-go="0"]').click();
    await p.locator('input[name="fb-v"][value="accept"]').check();
    await p.locator('.pn-b[data-go="1"]').click();
    await p.locator('input[name="fb-v"][value="edit"]').check();
    await p.locator('#fb-note').fill('希望改成側臉看海、裁在膝下');
    await p.locator('.pn-b[data-go="2"]').click();  // 換人時離開備註欄會存檔
    await p.locator('#fb-note').fill('靴子再完整一點');
    await p.locator('#fb-note').blur();
    await p.waitForTimeout(500);
    const kv = await p.evaluate(ks => ks.map(k => JSON.parse(localStorage.getItem(k) || 'null')), SETS.map(BK));
    ok(`${V} 回饋存成一張一個鍵：Tammy 接受、Rin 想修改＋備註、Somi 只有備註、Yerin 與 Jia 沒有資料`, kv[0].v === 'accept' && kv[1].v === 'edit' && kv[1].note === '希望改成側臉看海、裁在膝下' && kv[2].v === '' && kv[2].note === '靴子再完整一點' && kv[3] === null && kv[4] === null && kv[0].batch === 'batch1-m4r5');
    const navNow = await p.locator('.pn-b .st').allInnerTexts();
    ok(`${V} 導覽狀態即時更新：接受／想修改／未回覆×3（只寫備註仍是未回覆）`, J(navNow) === J(['接受', '想修改', '未回覆', '未回覆', '未回覆']));
    ok(`${V} 只寫備註的那張註明「目前不算接受」`, /不算接受/.test(await p.locator('#fb-saved').innerText()));
    // 重新載入：保留
    await p.reload({ waitUntil: 'networkidle' });
    await p.waitForSelector('#photo .ph img');
    ok(`${V} 重新載入後停在同一位（Somi）、回饋保留`, (await p.locator('.pn-b.on').innerText()).includes('Somi') && (await p.locator('#fb-note').inputValue()) === '靴子再完整一點' && J(await p.locator('.pn-b .st').allInnerTexts()) === J(navNow));
    // 整批複製
    await p.locator('#cp-btn').scrollIntoViewIfNeeded();
    await p.locator('#cp-btn').click();
    await p.waitForFunction(() => /已複製|無法自動複製/.test(document.getElementById('cp-msg').innerText));
    const msg = await p.locator('#cp-msg').innerText();
    const clip = await p.evaluate(() => navigator.clipboard.readText().catch(() => ''));
    const txt = await p.locator('#cp-text').inputValue();
    const want = ['1. Tammy｜V-tammy-chou｜1 月直式：接受', '2. Rin｜V-rin-ayase｜10 月直式：想修改', '   備註：希望改成側臉看海、裁在膝下', '3. Somi｜V-somi-oh｜12 月直式：未回覆（不算接受）', '   備註：靴子再完整一點',
      '4. Yerin｜H-yerin-han｜5 月橫式：未回覆（不算接受）', '5. Jia｜H-jia-seo｜9 月橫式：未回覆（不算接受）', '合計：已回覆 2／5、未回覆 3（接受 1、想修改 1；未回覆不算接受）。'];
    ok(`${V} 「複製本批回饋」：剪貼簿內容＝畫面文字；5 張逐張列出，未回覆標「不算接受」、合計 1／1／3`, msg === '已複製。' && clip === txt && want.every(w => txt.split('\n').includes(w)) && txt.split('\n')[0].startsWith(RV.task) && txt.split('\n')[0].includes('頁面版本 ') && txt.split('\n')[0].includes('照片版本 ' + RV.batch.photo_version), msg);
    ok(`${V} 摘要：已回覆 2／5`, /已回覆 2／5：接受 1、想修改 1、未回覆 3/.test(await p.locator('#cp-sum').innerText()));
    await p.screenshot({ path: `${out}/${vp.name}_copy.jpg`, type: 'jpeg', quality: 80, fullPage: vp.name === 'mobile390' });
    // 已接受紀錄：Iris
    const acc = await p.locator('#acc').innerText();
    ok(`${V} 已接受紀錄：V-Iris 已接受（Penny，M-4 R4）、不需回覆；沒有回饋選項`, /V-Iris/.test(acc) && /已接受（Penny，M-4 R4）/.test(acc) && /不需回覆/.test(acc) && (await p.locator('#acc input, #acc textarea').count()) === 0);
    await p.locator('#acc [data-open="acc0"]').click();
    await p.waitForSelector('#viewer:not([hidden])');
    await p.waitForFunction(() => /V-iris-chen_m4r2_view\.jpg$/.test(document.getElementById('viewer-img').currentSrc));
    await p.keyboard.press('Escape');
    await p.waitForSelector('#viewer', { state: 'hidden' });
    const [d2] = await Promise.all([p.waitForEvent('download'), p.locator('#acc a[download]').click()]);
    ok(`${V} Iris 看大圖與下載原圖（${d2.suggestedFilename()}）`, d2.suggestedFilename() === RV.accepted[0].download_name && sha(fs.readFileSync(await d2.path())) === sha(fs.readFileSync(`${PUB}/img/review/V-iris-chen_m4r2_first_test.png`)));
    ok(`${V} 主頁沒有水平溢出`, await overflow(p) <= 0, String(await overflow(p)));
    ok(`${V} 互動後舊的三筆 localStorage（企劃回饋、素材選擇、R3 回饋）位元組不變；新增的只有本批鍵`, await same() && (await allKeys()).filter(k => ![KEY, MKEY, RKEY].includes(k)).every(k => k.startsWith('cal2027-batch1-v1:')));
    // 歷史頁與素材頁照舊
    await p.goto(base + '/history.html');
    await p.waitForSelector('.scard');
    await p.$$eval('details', a => a.forEach(x => { x.open = true; }));
    const prep = await p.locator('#prep').innerText();
    ok(`${V} 歷史頁：R3 回饋仍只讀顯示；狀態列寫第一批 5 位已生成、待 Penny 看圖；24 套企劃卡仍在`, /人物與身材呈現：接受；備註：測試：R3 留在瀏覽器的回饋/.test(prep) && /第一批 5 位已生成，待 Penny 看圖/.test(await p.locator('#bar-count').innerText()) && (await p.locator('.scard').count()) === 24);
    ok(`${V} 歷史頁沒有水平溢出（全部展開）`, await overflow(p) <= 0, String(await overflow(p)));
    await p.goto(base + '/index.html');
    await p.waitForSelector('#p-iris-chen');
    ok(`${V} 素材頁：Iris 的選擇照舊`, await p.locator('#m-iris-04.on-h').count() === 1);
    ok(`${V} 走完三頁後舊資料仍不變`, await same());
    ok(`${V} 沒有 JS 錯誤`, errs.length === 0, errs.join(' | '));
    await ctx.close();
  }
  await browser.close();
  const fail = results.filter(r => r[0] === 'FAIL').length;
  fs.writeFileSync(`${out}/results.tsv`, results.map(r => r.join('\t')).join('\n') + '\n');
  console.log(`${results.length - fail}/${results.length} PASS`);
  process.exit(fail ? 1 : 0);
})();
