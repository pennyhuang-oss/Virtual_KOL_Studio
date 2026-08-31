#!/usr/bin/env node
/**
 * 分層抽樣，用「最終轉檔參數」實際跑一遍，量出衍生檔的真實大小分布。
 *
 * 為什麼要有這支：覆核者對 KOLCAT R1 的 Q4／CC-05 的裁決是
 * 「230 張、0.26 MB、2 MB 都還是規劃假設，不要再給另一個估值，要實測」。
 * 這支就是那個實測——它不估，它轉檔然後量檔案大小。
 *
 * 抽樣方式：每個 repo 內按原始檔案大小分成四個區間（quartile），每區間隨機取樣，
 * 這樣才不會整批抽到同一種解析度。影片另外記時長，因為影片大小主要由時長決定。
 *
 * 用法：
 *   node catalog/tools/sample_derive_measure.mjs                # 預設抽 40 圖 / 24 影片
 *   node catalog/tools/sample_derive_measure.mjs --images 60 --videos 30
 *   node catalog/tools/sample_derive_measure.mjs --keep <dir>    # 保留轉出來的檔案供目視檢查
 *
 * 輸出：catalog/data/derive_measurements.json
 *
 * 相依：真正的 ffmpeg。容器內沒有預裝，一行就有（本專案已記錄過這個做法）：
 *   pip install imageio-ffmpeg
 *   FF=$(python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())")
 * 🛑 不要用 /opt/pw-browsers 底下 Playwright 那個精簡版 ffmpeg，它連 mp4 都 demux 不了。
 * 🛑 不要自己解 MP4 atom 讀規格——本專案踩過，offset 算錯會讀出一整套錯的結論。
 */
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';
import { execFileSync } from 'node:child_process';

const REPO_ROOT = process.env.REPO_ROOT || '/home/user';
const OUT = path.join(import.meta.dirname, '..', 'data', 'derive_measurements.json');

const argv = process.argv.slice(2);
const argOf = (k, d) => { const i = argv.indexOf(k); return i >= 0 ? argv[i + 1] : d; };
const N_IMG = Number(argOf('--images', 40));
const N_VID = Number(argOf('--videos', 24));
const KEEP = argOf('--keep', null);

// ── 最終轉檔參數。改這裡就等於改型錄的交付規格，量出來的數字才有意義。 ──
const SPEC = {
  thumb:  { desc: '首頁卡片', width: 400, quality: 78 },
  web:    { desc: '人設頁圖庫', longEdge: 1440, quality: 82 },
  poster: { desc: '影片播放前的首幀', width: 720, quality: 80 },
  // 🛑 longEdge 而不是 height。R1 只鎖 height，橫式影片（母體有 2 支 1280×720）會完全不被縮小。
  video:  { desc: '人設頁影片', longEdge: 1280, crf: 26, audioKbps: 96, preset: 'medium' },
};

const FFMPEG = (() => {
  try {
    return execFileSync('python3',
      ['-c', 'import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())'],
      { encoding: 'utf8' }).trim();
  } catch {
    console.error('找不到 ffmpeg。先跑：pip install imageio-ffmpeg');
    process.exit(1);
  }
})();

const REPOS = [
  { dir: 'Virtual_KOL_Studio', tag: 'VKS' },
  { dir: 'showgame-kol',       tag: 'SGK' },
  { dir: 'Buildup_KOL',        tag: 'BUP' },
];
const IMG_EXT = new Set(['.png', '.jpg', '.jpeg', '.webp', '.jfif']);
const VID_EXT = new Set(['.mp4', '.mov', '.webm']);

function collect(dir, extSet, out) {
  let es; try { es = fs.readdirSync(dir, { withFileTypes: true }); } catch { return; }
  for (const e of es) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) collect(p, extSet, out);
    else if (e.isFile() && extSet.has(path.extname(e.name).toLowerCase())) {
      out.push({ path: p, size: fs.statSync(p).size });
    }
  }
}

// 按原始大小分四個區間，每區間平均取樣。固定 seed 讓結果可重現。
let seed = 20260831;
const rand = () => (seed = (seed * 1103515245 + 12345) & 0x7fffffff) / 0x7fffffff;

function stratify(files, n) {
  if (files.length <= n) return files;
  const sorted = [...files].sort((a, b) => a.size - b.size);
  const perBand = Math.ceil(n / 4);
  const bandSize = Math.floor(sorted.length / 4);
  const picked = [];
  for (let b = 0; b < 4; b++) {
    const band = sorted.slice(b * bandSize, b === 3 ? sorted.length : (b + 1) * bandSize);
    const idx = new Set();
    while (idx.size < Math.min(perBand, band.length)) idx.add(Math.floor(rand() * band.length));
    for (const i of idx) picked.push(band[i]);
  }
  // 最大的那一支一定要進樣本——p95 與 max 是這次要回答的重點。
  if (!picked.includes(sorted.at(-1))) picked.push(sorted.at(-1));
  return picked.slice(0, n + 1);
}

const tmp = KEEP || fs.mkdtempSync(path.join(os.tmpdir(), 'kolcat-derive-'));
fs.mkdirSync(tmp, { recursive: true });

function ff(args) {
  execFileSync(FFMPEG, ['-hide_banner', '-loglevel', 'error', '-y', ...args], { stdio: 'pipe' });
}
function probeDims(file) {
  // 用 ffmpeg 自己印的那一行，不要自己解檔頭。
  try {
    execFileSync(FFMPEG, ['-hide_banner', '-i', file], { stdio: 'pipe' });
  } catch (e) {
    const s = String(e.stderr || '');
    const dim = s.match(/,\s(\d{2,5})x(\d{2,5})[\s,]/);
    const dur = s.match(/Duration:\s(\d+):(\d+):(\d+\.\d+)/);
    return {
      width: dim ? +dim[1] : null,
      height: dim ? +dim[2] : null,
      seconds: dur ? (+dur[1] * 3600 + +dur[2] * 60 + +dur[3]) : null,
    };
  }
  return { width: null, height: null, seconds: null };
}

const stats = a => {
  if (!a.length) return null;
  const s = [...a].sort((x, y) => x - y);
  const q = p => s[Math.min(s.length - 1, Math.floor(p * (s.length - 1) + 0.5))];
  return {
    n: s.length,
    min: +s[0].toFixed(3),
    p50: +q(0.50).toFixed(3),
    p95: +q(0.95).toFixed(3),
    max: +s.at(-1).toFixed(3),
    mean: +(s.reduce((a, b) => a + b, 0) / s.length).toFixed(3),
  };
};
const MB = b => b / 1048576;

const results = { images: [], videos: [] };

// ── 圖 ──────────────────────────────────────────────────────────────
let allImg = [];
for (const r of REPOS) { const o = []; collect(path.join(REPO_ROOT, r.dir, 'kols'), IMG_EXT, o); o.forEach(x => x.repo = r.tag); allImg.push(...o); }
const imgSample = REPOS.flatMap(r => stratify(allImg.filter(x => x.repo === r.tag), Math.ceil(N_IMG / 3)));

console.log(`圖：母體 ${allImg.length} 張，抽 ${imgSample.length} 張實際轉檔…`);
for (const f of imgSample) {
  const base = path.basename(f.path).replace(/\.[^.]+$/, '');
  const uniq = `${f.repo}_${base}_${Math.abs(hash(f.path))}`;
  const web = path.join(tmp, `${uniq}_web.jpg`);
  const thumb = path.join(tmp, `${uniq}_thumb.jpg`);
  try {
    const d = probeDims(f.path);
    ff(['-i', f.path, '-vf', `scale='if(gt(iw,ih),min(${SPEC.web.longEdge},iw),-2)':'if(gt(iw,ih),-2,min(${SPEC.web.longEdge},ih))'`,
        '-q:v', String(Math.round((100 - SPEC.web.quality) / 100 * 30) + 2), web]);
    ff(['-i', f.path, '-vf', `scale=${SPEC.thumb.width}:-2`,
        '-q:v', String(Math.round((100 - SPEC.thumb.quality) / 100 * 30) + 2), thumb]);
    results.images.push({
      repo: f.repo, file: path.relative(REPO_ROOT, f.path),
      src_w: d.width, src_h: d.height,
      src_mb: +MB(f.size).toFixed(3),
      web_mb: +MB(fs.statSync(web).size).toFixed(3),
      thumb_mb: +MB(fs.statSync(thumb).size).toFixed(3),
    });
  } catch (e) { results.images.push({ repo: f.repo, file: path.relative(REPO_ROOT, f.path), error: String(e.message).slice(0, 120) }); }
}

// ── 影片 ────────────────────────────────────────────────────────────
let allVid = [];
for (const r of REPOS) { const o = []; collect(path.join(REPO_ROOT, r.dir, 'kols'), VID_EXT, o); o.forEach(x => x.repo = r.tag); allVid.push(...o); }
const vidSample = REPOS.flatMap(r => stratify(allVid.filter(x => x.repo === r.tag), Math.ceil(N_VID / 3)));

console.log(`影片：母體 ${allVid.length} 支，抽 ${vidSample.length} 支實際轉檔（會慢）…`);
let done = 0;
for (const f of vidSample) {
  const uniq = `${f.repo}_${Math.abs(hash(f.path))}`;
  const out = path.join(tmp, `${uniq}.mp4`);
  const poster = path.join(tmp, `${uniq}_poster.jpg`);
  try {
    const d = probeDims(f.path);
    ff(['-i', f.path,
        '-vf', `scale='if(gt(iw,ih),min(${SPEC.video.longEdge},iw),-2)':'if(gt(iw,ih),-2,min(${SPEC.video.longEdge},ih))'`,
        '-c:v', 'libx264', '-crf', String(SPEC.video.crf), '-preset', SPEC.video.preset,
        '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
        '-c:a', 'aac', '-b:a', `${SPEC.video.audioKbps}k`, out]);
    ff(['-ss', '1', '-i', f.path, '-frames:v', '1', '-vf', `scale=${SPEC.poster.width}:-2`, '-q:v', '4', poster]);
    const outSize = fs.statSync(out).size;
    results.videos.push({
      repo: f.repo, file: path.relative(REPO_ROOT, f.path),
      src_w: d.width, src_h: d.height, seconds: d.seconds ? +d.seconds.toFixed(1) : null,
      src_mb: +MB(f.size).toFixed(3),
      out_mb: +MB(outSize).toFixed(3),
      poster_mb: +MB(fs.statSync(poster).size).toFixed(3),
      mb_per_sec: d.seconds ? +(MB(outSize) / d.seconds).toFixed(4) : null,
    });
  } catch (e) { results.videos.push({ repo: f.repo, file: path.relative(REPO_ROOT, f.path), error: String(e.message).slice(0, 120) }); }
  if (++done % 5 === 0) console.log(`  …${done}/${vidSample.length}`);
}

function hash(s) { let h = 0; for (const c of s) h = (h * 31 + c.charCodeAt(0)) | 0; return h; }

const okImg = results.images.filter(x => !x.error);
const okVid = results.videos.filter(x => !x.error);

const measured = {
  generated_by: 'catalog/tools/sample_derive_measure.mjs',
  generated_at: new Date().toISOString().slice(0, 10),
  method: '分層抽樣（每 repo 按原始檔案大小分四區間取樣，並強制納入各 repo 最大的一支）＋用最終轉檔參數實際轉檔後量檔案大小。不是估值。',
  ffmpeg: execFileSync(FFMPEG, ['-version'], { encoding: 'utf8' }).split('\n')[0],
  spec: SPEC,
  population: { images: allImg.length, videos: allVid.length },
  sampled: { images: okImg.length, videos: okVid.length, image_errors: results.images.length - okImg.length, video_errors: results.videos.length - okVid.length },
  distribution_mb: {
    image_src: stats(okImg.map(x => x.src_mb)),
    image_web: stats(okImg.map(x => x.web_mb)),
    image_thumb: stats(okImg.map(x => x.thumb_mb)),
    video_src: stats(okVid.map(x => x.src_mb)),
    video_out: stats(okVid.map(x => x.out_mb)),
    video_poster: stats(okVid.map(x => x.poster_mb)),
  },
  video_seconds: stats(okVid.map(x => x.seconds).filter(Boolean)),
  video_mb_per_sec: stats(okVid.map(x => x.mb_per_sec).filter(Boolean)),
  samples: results,
};

fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(measured, null, 2) + '\n');

const d = measured.distribution_mb;
const f = (s) => s ? `p50 ${s.p50} / p95 ${s.p95} / max ${s.max} MB（n=${s.n}）` : '—';
console.log(`\n寫入 ${OUT}\n`);
console.log(`圖 web (長邊 1440 q82)  ${f(d.image_web)}`);
console.log(`圖 thumb (寬 400 q78)   ${f(d.image_thumb)}`);
console.log(`影片 out (720p CRF26)   ${f(d.video_out)}`);
console.log(`影片 poster             ${f(d.video_poster)}`);
console.log(`影片時長（秒）           p50 ${measured.video_seconds?.p50} / p95 ${measured.video_seconds?.p95} / max ${measured.video_seconds?.max}`);
console.log(`影片 MB/秒               p50 ${measured.video_mb_per_sec?.p50} / p95 ${measured.video_mb_per_sec?.p95}`);
if (!KEEP) fs.rmSync(tmp, { recursive: true, force: true });
else console.log(`\n轉出來的檔案留在 ${tmp}`);
