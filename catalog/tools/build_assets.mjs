#!/usr/bin/env node
/**
 * 把 catalog.json 的候選素材轉成網頁尺寸的衍生檔 → catalog/assets/
 *
 * 規格與實測大小見覆核包 §2.1（p50/p95/max 都量過，不是估的）。
 * 🛑 影片不進 git（實測位元率 0.065–0.358 MB/秒，5.5 倍差距、上限不可控）。
 *    本程式只產影片的 poster；影片本體外放，另一支程式處理。
 *
 * 用法：
 *   node catalog/tools/build_assets.mjs              # 每位人設最多 9 張
 *   node catalog/tools/build_assets.mjs --per 12
 *   node catalog/tools/build_assets.mjs --force      # 重做已存在的
 */
import fs from 'node:fs';
import path from 'node:path';
import { execFileSync } from 'node:child_process';

const REPO_ROOT = process.env.REPO_ROOT || '/home/user';
const DIR = path.join(import.meta.dirname, '..');
const ASSETS = path.join(DIR, 'assets');
const argv = process.argv.slice(2);
const argOf = (k, d) => { const i = argv.indexOf(k); return i >= 0 ? argv[i + 1] : d; };
const PER = Number(argOf('--per', 9));
const FORCE = argv.includes('--force');

const SPEC = {
  web:    { longEdge: 1440, q: 82 },
  thumb:  { width: 400, q: 78 },
  poster: { width: 720, q: 80 },
  // 影片:720p 長邊上限、CRF 26、AAC 96k、yuv420p、faststart（moov 搬到檔頭才能邊下載邊播）。
  // 實測（三支分層抽樣）:2.7→0.89、22.1→1.56、65.6→4.96 MB,平均每秒 0.102 MB。
  video:  { longEdge: 1280, crf: 26, preset: 'medium', audioKbps: 96 },
};
// 上限的依據（依覆核者 Q9 的判準：能量出來的就量，不要猜餘裕倍數）
//   第一版：抽樣 48 張的 max 0.206 MB × 約 2 → 0.4 MB。
//   實跑之後被打到一次：rachel-ong 的橫式風景寬照輸出 0.431 MB 被擋下。
//   全量 179 張的分布：p50 0.089／p95 0.191／p99 0.245／max 0.267，
//   加上被擋那張的 0.431 才是真正的母體上界。
//   → 改成 0.6 MB（母體上界 0.431 × 1.4）。
//   這個放寬不影響總量：全部 377 檔目前 23.8 MB，觀察線是 80 MB。
const LIMIT = { single_image_mb: 0.6, assets_total_mb_warn: 80 };

const FF = execFileSync('python3', ['-c', 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())'], { encoding: 'utf8' }).trim();
const ff = a => execFileSync(FF, ['-hide_banner', '-nostdin', '-loglevel', 'error', '-y', ...a], { stdio: ['ignore', 'pipe', 'pipe'] });
const qOf = q => String(Math.round((100 - q) / 100 * 30) + 2);   // JPEG 品質 → ffmpeg -q:v

// 🛑 為什麼只有少數幾支會多出一份 WebM——這是為了「驗得到」,不是為了相容性。
// 上線的格式是 H.264/MP4,現代瀏覽器全部都播得動。但我用來驗的 Playwright Chromium
// **完全沒有 H.264**（實測 canPlayType 回空字串,VP8/VP9 回 probably）,
// 所以只出 MP4 的話「點下去會不會播」在這台機器上永遠驗不了,只能寫「應該可以」。
// 每支都出 VP9 要多 178 MB ＋ 20 分鐘（實測 720p:1.77 MB vs H.264 1.56 MB、1.2 倍即時）,
// 為了測而付這個代價不合理。所以只做 VP9_PROBE 支當探針,
// <source> 順序是 MP4 在前、WebM 在後——真瀏覽器拿 MP4,我這台自動退到 WebM。
const VP9_PROBE = 3;

// 🛑 衍生檔的檔名一律由「來源檔路徑」算出來,不要用「它在清單裡的第幾個」。
// 2026-09-04 實測過的坑：舊做法是 g01/g02…、v1_poster/v2_poster…,配上「檔案已存在就跳過」,
// 於是把 Luna 清單裡的前兩支對調再重建,v1_poster.jpg **完全沒變**——
// 它指的還是舊那支影片。圖庫與封面是同一個寫法,同一個坑。
// 換成雜湊之後:
//   ・加新素材 → 只有新的那幾個要轉,其餘一個都不動
//   ・調順序   → 什麼都不用重轉,而且不會錯
//   ・拿掉素材 → 清理只刪沒被引用到的那幾個
// （用跟 build_picker.mjs 同一個 djb2,兩邊算出來的 id 才會一致。）
const id7 = t => { let h = 5381; for (const c of String(t)) h = ((h * 33) ^ c.charCodeAt(0)) >>> 0;
  return h.toString(36).padStart(7, '0'); };

const cat = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'catalog.json'), 'utf8'));
// selection.json 若存在就以它為準（人挑過的），否則用候選池前 N 張
let selection = {};
try { selection = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'selection.json'), 'utf8')).personas || {}; } catch {}

fs.mkdirSync(ASSETS, { recursive: true });
let made = 0, skipped = 0, stale = 0, failed = [];
let probeLeft = VP9_PROBE;

for (const p of cat.personas) {
  const dir = path.join(ASSETS, p.id);
  fs.mkdirSync(dir, { recursive: true });

  const picked = selection[p.id]?.gallery || p.media.candidates.slice(0, PER).map(c => c.rel);
  const heroRel = selection[p.id]?.hero || picked[0];

  const jobs = [];
  // manifest 記的是「順序」,檔名記的是「來源」,兩件事分開之後就不會互相汙染。
  const man = { hero: null, gallery: [], videos: [] };

  if (heroRel) {
    jobs.push({ rel: heroRel, out: `hero_${id7(heroRel)}`, kind: 'web' });
    man.hero = `hero_${id7(heroRel)}.jpg`;
  }
  picked.forEach(rel => {
    const k = id7(rel);
    jobs.push({ rel, out: `g_${k}`, kind: 'web' });
    jobs.push({ rel, out: `g_${k}_t`, kind: 'thumb' });
    man.gallery.push({ web: `g_${k}.jpg`, thumb: `g_${k}_t.jpg` });
  });

  for (const j of jobs) {
    const src = path.join(REPO_ROOT, j.rel);
    const out = path.join(dir, `${j.out}.jpg`);
    if (!FORCE && fs.existsSync(out)) { skipped++; continue; }
    if (!fs.existsSync(src)) { failed.push({ file: j.rel, why: '原始檔不存在' }); continue; }
    try {
      const s = SPEC[j.kind];
      const vf = s.longEdge
        ? `scale='if(gt(iw,ih),min(${s.longEdge},iw),-2)':'if(gt(iw,ih),-2,min(${s.longEdge},ih))'`
        : `scale=${s.width}:-2`;
      ff(['-i', src, '-vf', vf, '-q:v', qOf(s.q), out]);
      const mb = fs.statSync(out).size / 1048576;
      if (j.kind === 'web' && mb > LIMIT.single_image_mb) {
        failed.push({ file: j.rel, why: `輸出 ${mb.toFixed(3)} MB 超過單張上限 ${LIMIT.single_image_mb} MB` });
        fs.unlinkSync(out); continue;
      }
      made++;
    } catch (e) { failed.push({ file: j.rel, why: String(e.message).slice(0, 100) }); }
  }

  // 影片 poster（影片本體不進 git）
  const vids = (selection[p.id]?.videos || p.media.videos.slice(0, 3).map(v => v.rel));
  vids.forEach(rel => {
    const k = id7(rel);
    man.videos.push({ poster: `v_${k}_poster.jpg`, mp4: `v_${k}.mp4`, webm: `v_${k}.webm` });
    const src = path.join(REPO_ROOT, rel);
    if (!fs.existsSync(src)) { failed.push({ file: rel, why: '影片不存在' }); return; }

    // 首幀圖。⚠ 這裡不可以用 `return` 提前結束——下面還有影片本體要轉,
    //   用 return 會把影片一起跳過（踩過一次:回報「產出 0 個」而 51 支一支都沒轉）。
    const out = path.join(dir, `v_${k}_poster.jpg`);
    if (!FORCE && fs.existsSync(out)) { skipped++; }
    else {
      try { ff(['-ss', '1', '-i', src, '-frames:v', '1', '-vf', `scale=${SPEC.poster.width}:-2`, '-q:v', qOf(SPEC.poster.q), out]); made++; }
      catch (e) { failed.push({ file: rel, why: 'poster 失敗：' + String(e.message).slice(0, 60) }); }
    }

    // ── 影片本體:轉成網頁播得動的 MP4 ──
    const mp4 = path.join(dir, `v_${k}.mp4`);
    const sc = `scale='if(gt(iw,ih),min(${SPEC.video.longEdge},iw),-2)':'if(gt(iw,ih),-2,min(${SPEC.video.longEdge},ih))'`;
    if (FORCE || !fs.existsSync(mp4)) {
      try {
        ff(['-i', src, '-vf', sc,
            '-c:v', 'libx264', '-crf', String(SPEC.video.crf), '-preset', SPEC.video.preset,
            '-pix_fmt', 'yuv420p', '-profile:v', 'high', '-level', '4.0',
            // ✅ 無聲的來源帶著 -c:a 也不會失敗——實測過:ffmpeg 直接忽略,輸出就是 0 個音軌,
            //    所以不需要另外一條「不帶音訊」的備援路徑。
            '-c:a', 'aac', '-b:a', `${SPEC.video.audioKbps}k`, '-ac', '2',
            '-movflags', '+faststart', mp4]);
        made++;
      } catch (e) { failed.push({ file: rel, why: '影片轉檔失敗：' + String(e.message).slice(0, 80) }); }
    } else skipped++;

    // ── 探針:只有前 VP9_PROBE 支會多一份 WebM,理由見檔案上方註解 ──
    if (probeLeft > 0 && fs.existsSync(mp4)) {
      const webm = path.join(dir, `v_${k}.webm`);
      if (FORCE || !fs.existsSync(webm)) {
        try {
          ff(['-i', mp4, '-c:v', 'libvpx-vp9', '-crf', '34', '-b:v', '0',
              '-deadline', 'good', '-cpu-used', '4', '-row-mt', '1',
              '-c:a', 'libopus', '-b:a', `${SPEC.video.audioKbps}k`, webm]);
          made++;
        } catch { /* 探針轉失敗不擋,MP4 還在 */ }
      }
      probeLeft--;
    }
  });

  // manifest 就是這位人設的「該有哪些衍生檔、順序是什麼」的唯一依據。
  // build_site 讀它,不要再去掃資料夾——掃資料夾就是上一個 bug 的來源。
  fs.writeFileSync(path.join(dir, 'manifest.json'), JSON.stringify(man, null, 1));

  // 🛑 清掉沒被 manifest 引用到的衍生檔。
  // 踩過兩次：① 影片從 3 支改成 1 支,舊的 v2/v3_poster.jpg 留著,頁面就多出兩個不存在的影片格；
  //          ② 檔名照位置命名時,調順序會讓舊檔「名字對、內容錯」而且永遠不會被重轉。
  // 衍生檔不清,頁面就會說謊。
  const keep = new Set([
    'manifest.json', man.hero,
    ...man.gallery.flatMap(g => [g.web, g.thumb]),
    ...man.videos.flatMap(v => [v.poster, v.mp4, v.webm]),
  ].filter(Boolean));
  for (const f of fs.readdirSync(dir)) {
    if (!keep.has(f)) { fs.rmSync(path.join(dir, f), { force: true }); stale++; }
  }
}

// 總量
let total = 0, count = 0;
(function w(d) { for (const e of fs.readdirSync(d, { withFileTypes: true })) {
  const f = path.join(d, e.name);
  if (e.isDirectory()) w(f); else { total += fs.statSync(f).size; count++; } } })(ASSETS);
const totalMb = total / 1048576;

console.log(`產出 ${made} 個衍生檔（跳過已存在 ${skipped} 個）`);
if (stale) console.log(`清掉 ${stale} 個沒被 manifest 引用到的舊衍生檔`);
console.log(`assets/ 共 ${count} 檔、${totalMb.toFixed(1)} MB`);
if (totalMb > LIMIT.assets_total_mb_warn)
  console.log(`⚠ 超過觀察線 ${LIMIT.assets_total_mb_warn} MB —— 依 CC-05 這一項只警告不擋，但要回報`);
if (failed.length) {
  console.log(`\n🛑 ${failed.length} 個失敗：`);
  for (const f of failed.slice(0, 10)) console.log(`   ${f.why}  ←  ${f.file}`);
  process.exit(1);
}
