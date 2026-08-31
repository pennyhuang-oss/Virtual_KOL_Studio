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

const cat = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'catalog.json'), 'utf8'));
// selection.json 若存在就以它為準（人挑過的），否則用候選池前 N 張
let selection = {};
try { selection = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'selection.json'), 'utf8')).personas || {}; } catch {}

fs.mkdirSync(ASSETS, { recursive: true });
let made = 0, skipped = 0, failed = [];

for (const p of cat.personas) {
  const dir = path.join(ASSETS, p.id);
  fs.mkdirSync(dir, { recursive: true });

  const picked = selection[p.id]?.gallery || p.media.candidates.slice(0, PER).map(c => c.rel);
  const heroRel = selection[p.id]?.hero || picked[0];

  const jobs = [];
  if (heroRel) jobs.push({ rel: heroRel, out: 'hero', kind: 'web' });
  picked.forEach((rel, i) => {
    jobs.push({ rel, out: `g${String(i + 1).padStart(2, '0')}`, kind: 'web' });
    jobs.push({ rel, out: `g${String(i + 1).padStart(2, '0')}_t`, kind: 'thumb' });
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
  vids.forEach((rel, i) => {
    const src = path.join(REPO_ROOT, rel);
    const out = path.join(dir, `v${i + 1}_poster.jpg`);
    if (!FORCE && fs.existsSync(out)) { skipped++; return; }
    if (!fs.existsSync(src)) { failed.push({ file: rel, why: '影片不存在' }); return; }
    try { ff(['-ss', '1', '-i', src, '-frames:v', '1', '-vf', `scale=${SPEC.poster.width}:-2`, '-q:v', qOf(SPEC.poster.q), out]); made++; }
    catch (e) { failed.push({ file: rel, why: 'poster 失敗：' + String(e.message).slice(0, 60) }); }
  });
}

// 總量
let total = 0, count = 0;
(function w(d) { for (const e of fs.readdirSync(d, { withFileTypes: true })) {
  const f = path.join(d, e.name);
  if (e.isDirectory()) w(f); else { total += fs.statSync(f).size; count++; } } })(ASSETS);
const totalMb = total / 1048576;

console.log(`產出 ${made} 個衍生檔（跳過已存在 ${skipped} 個）`);
console.log(`assets/ 共 ${count} 檔、${totalMb.toFixed(1)} MB`);
if (totalMb > LIMIT.assets_total_mb_warn)
  console.log(`⚠ 超過觀察線 ${LIMIT.assets_total_mb_warn} MB —— 依 CC-05 這一項只警告不擋，但要回報`);
if (failed.length) {
  console.log(`\n🛑 ${failed.length} 個失敗：`);
  for (const f of failed.slice(0, 10)) console.log(`   ${f.why}  ←  ${f.file}`);
  process.exit(1);
}
