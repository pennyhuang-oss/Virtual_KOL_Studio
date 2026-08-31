#!/usr/bin/env node
/**
 * 從三個 repo 的人設檔產生型錄要顯示的全部內容 → catalog/data/catalog.json
 *
 * 內容依據只有一個：使用者 2026-08-31 說客戶要知道的四件事。
 *   1 這個人設的設定是什麼      → persona / content 欄位
 *   2 他有哪些素材              → media
 *   3 人設的細節到什麼程度      → depth（本檔最重要也最容易做錯的一塊）
 *   4 曾經營運過的大概數據      → ops（大概值，不講期間）
 *
 * 🛑 刻意不輸出的（§2.4 與使用者裁決）：
 *   - 任何狀態（籌備中／正在營運中／已停用／多久沒更新）
 *   - handle（有沒有上線本身就是狀態）
 *   - 三圍與罩杯（`identity.appearance.measurements`）
 *   - prompt、Soul ID、模型名稱、credits、重做輪數
 *   - 營運的統計期間
 *
 * 用法：
 *   node catalog/tools/build_catalog.mjs
 *   node catalog/tools/build_catalog.mjs --min-images 14   # 收錄門檻（預設 14）
 */
import fs from 'node:fs';
import path from 'node:path';

const REPO_ROOT = process.env.REPO_ROOT || '/home/user';
const DIR = path.join(import.meta.dirname, '..');
const OUT = path.join(DIR, 'data', 'catalog.json');

const argv = process.argv.slice(2);
const argOf = (k, d) => { const i = argv.indexOf(k); return i >= 0 ? argv[i + 1] : d; };
const MIN_IMAGES = Number(argOf('--min-images', 14));

const inv = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'inventory.json'), 'utf8'));

// 手寫的內容（程式產不出來的）：一句話定位，以及刻意排除的人設。
const COPY = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'copy.json'), 'utf8'));

const REPO_OF = { VKS: 'Virtual_KOL_Studio', SGK: 'showgame-kol', BUP: 'Buildup_KOL' };

const IMG = new Set(['.png', '.jpg', '.jpeg', '.webp']);
const VID = new Set(['.mp4', '.mov', '.webm']);

// ── 素材候選池 ─────────────────────────────────────────────────────
// 程式只做「可稽核的候選整理」，不做審美淘汰——最後挑哪幾張是人的事。
// 排除規則每一條都會記進 excluded，讓人看得到為什麼被排除。
const EXCLUDE_PATTERNS = [
  { re: /未採用|已作廢|廢棄|discard/i, why: '檔名標示未採用或已作廢' },
  { re: /_tiktok\//, why: 'TikTok 縮圖，是衍生檔不是母檔' },
  { re: /_fail|_v\d+_body_fail/i, why: '檔名標示為失敗版' },
  { re: /face_crops?\//i, why: '臉部部位裁切，不是成品' },
  { re: /probe/i, why: '探測測試，不是成品' },
  { re: /casting/i, why: '選角批次——同一個資料夾裡是好幾張不同的臉，不是這位人設的成品' },
  { re: /candidate_\d/i, why: '選角候選圖，不是成品' },
  { re: /sheet\.|_qa_|compare_|ablation/i, why: '比對表，不是成品' },
];

// 🛑 機械防線：真人參考素材一律排除。
// 為什麼需要這一道：檔名規則會漏。`kols/*/images/face_reference/` 底下其實是
// **生成出來的人像**（1728×2304／1152×2048 這種整齊尺寸），是可用的成品；
// 而真人參考素材全部是不規則的小尺寸（實測 `wendy-yeo/images/a0_probe_crop/inputs/`
// 是 614×640／640×274／527×639）。生成輸出的最小長邊實測是 1152。
// → 長邊小於 1024 的一律排除。這比檔名規則可靠，而且它擋的正是唯一真的不能公開的東西。
// ⚠ 本 repo 的 58 張真人參考照放在 `review/batch3_face_refs/`（498×616 等），
//   不在 `kols/` 底下，所以本程式根本掃不到——這一道是防未來有人把它們放進 kols/。
const MIN_LONG_EDGE = 1024;

// 讀圖檔頭拿寬高。只讀前 64KB，不解整張圖。
function imageSize(file) {
  let fd, buf;
  try {
    fd = fs.openSync(file, 'r');
    buf = Buffer.alloc(65536);
    const n = fs.readSync(fd, buf, 0, 65536, 0);
    buf = buf.subarray(0, n);
  } catch { return null; } finally { if (fd !== undefined) try { fs.closeSync(fd); } catch {} }

  // PNG
  if (buf.length > 24 && buf.readUInt32BE(0) === 0x89504e47)
    return { w: buf.readUInt32BE(16), h: buf.readUInt32BE(20) };

  // WebP (VP8X / VP8 / VP8L)
  if (buf.length > 30 && buf.toString('ascii', 0, 4) === 'RIFF' && buf.toString('ascii', 8, 12) === 'WEBP') {
    const fourcc = buf.toString('ascii', 12, 16);
    if (fourcc === 'VP8X') return { w: (buf.readUIntLE(24, 3) & 0xffffff) + 1, h: (buf.readUIntLE(27, 3) & 0xffffff) + 1 };
    if (fourcc === 'VP8 ') return { w: buf.readUInt16LE(26) & 0x3fff, h: buf.readUInt16LE(28) & 0x3fff };
    if (fourcc === 'VP8L') { const b = buf.readUInt32LE(21); return { w: (b & 0x3fff) + 1, h: ((b >> 14) & 0x3fff) + 1 }; }
  }

  // JPEG：走 marker 找 SOFn
  if (buf.length > 4 && buf[0] === 0xff && buf[1] === 0xd8) {
    let i = 2;
    while (i + 9 < buf.length) {
      if (buf[i] !== 0xff) { i++; continue; }
      const marker = buf[i + 1];
      if (marker >= 0xc0 && marker <= 0xcf && marker !== 0xc4 && marker !== 0xc8 && marker !== 0xcc)
        return { h: buf.readUInt16BE(i + 5), w: buf.readUInt16BE(i + 7) };
      const len = buf.readUInt16BE(i + 2);
      if (len < 2) return null;
      i += 2 + len;
    }
  }
  return null;
}

function walkMedia(dir) {
  const out = [];
  (function w(d) {
    let es; try { es = fs.readdirSync(d, { withFileTypes: true }); } catch { return; }
    for (const e of es) {
      const p = path.join(d, e.name);
      if (e.isDirectory()) w(p);
      else if (e.isFile()) {
        const ext = path.extname(e.name).toLowerCase();
        if (IMG.has(ext) || VID.has(ext)) out.push({ abs: p, size: fs.statSync(p).size, kind: IMG.has(ext) ? 'image' : 'video' });
      }
    }
  })(dir);
  return out;
}

// ── 候選排序（不是排除，是排序）─────────────────────────────────────
// 為什麼需要：第一版按檔案大小排，結果 18 位裡有一半的封面挑到影片首幀
// （「爆炸前完好」「街景」）、UI 字卡（「287days」）、校正測試圖（「arm_C」）
// 與橫式風景寬照——都是檔案很大但不是人像的東西。
// 型錄的封面必須是這個人的人像，所以改成評分：**直式人像高分，其他扣分。**
// 🛑 這裡只排序不淘汰（覆核者 Q11：程式不可以做不可逆的審美淘汰），
//    分數低的仍然留在候選池裡，人可以自己挑回來。
const PENALTY = [
  { re: /首幀|尾幀|keyframe/i, s: -60, why: '影片首尾幀' },
  { re: /ref[AB]-|[-_]ui[-_]|287|screen|_hud/i, s: -60, why: 'UI 或字卡' },
  { re: /calibration|preflight|_fix|fix_|arm_|hand_|leg_|測試/i, s: -50, why: '技術校正或測試圖' },
  { re: /pov|_tv[-_]|screenshot/i, s: -40, why: 'POV 或畫面截圖' },
  { re: /16x9|[-_]wide\b|panorama/i, s: -40, why: '橫式構圖' },
  { re: /備用|_v\d+$/i, s: -10, why: '備用版' },
  { re: /\/圖文\//i, s: -15, why: '圖文貼文素材——主角常常是題材物件不是人' },
];
const BONUS = [
  // `images/ref/` 與 `face_reference/` 是人設的正規人像組（`<name>_01_fullbody_front` 這種命名），
  // 型錄封面最該用的就是那一組。少了這一條，林曜的封面被 `圖文/…/zeus-1-halfbody.png`
  // （一尊宙斯雕像，檔名剛好有 halfbody）搶走。
  { re: /\/(images\/ref|face_reference)\//i, s: 40, why: '人設正規人像組' },
  { re: /\/(training_v\d+|soul_test\w*|pilot_\w+|batch\d+|seedream_\w+)\//i, s: 40, why: '人像生成批次' },
  { re: /selfie|portrait|headshot|halfbody|fullbody|全身|半身/i, s: 30, why: '檔名指明是人像' },
  { re: /生活照/i, s: 20, why: '生活照' },
];

function scoreCandidate(m) {
  let s = 0; const why = [];
  for (const r of PENALTY) if (r.re.test(m.rel)) { s += r.s; why.push('−' + r.why); }
  for (const r of BONUS)   if (r.re.test(m.rel)) { s += r.s; why.push('+' + r.why); }
  // 直式人像優先。3:4（0.75）到 9:16（0.5625）之間最好，橫式重扣。
  if (m.w && m.h) {
    const ar = m.w / m.h;
    if (ar > 1.05) s -= 45;                       // 橫式
    else if (ar >= 0.55 && ar <= 0.82) s += 35;   // 直式人像的常見比例
    else if (ar > 0.95) s -= 15;                  // 接近正方
  }
  return { score: s, reasons: why };
}

function collectMedia(id, repos) {
  const kept = [], excluded = [];
  for (const tag of repos) {
    const base = path.join(REPO_ROOT, REPO_OF[tag], 'kols', id);
    for (const m of walkMedia(base)) {
      const rel = m.abs.replace(REPO_ROOT + '/', '');
      const hit = EXCLUDE_PATTERNS.find(x => x.re.test(rel));
      if (hit) { excluded.push({ file: rel, why: hit.why }); continue; }
      if (m.kind === 'image') {
        const d = imageSize(m.abs);
        if (!d) { excluded.push({ file: rel, why: '讀不到尺寸，無法確認是成品還是參考素材' }); continue; }
        if (Math.max(d.w, d.h) < MIN_LONG_EDGE) {
          excluded.push({ file: rel, why: `長邊 ${Math.max(d.w, d.h)}px < ${MIN_LONG_EDGE}px，低於生成輸出的下限，可能是參考素材` });
          continue;
        }
        m.w = d.w; m.h = d.h;
      }
      kept.push({ ...m, repo: tag, rel, dir: path.dirname(rel), name: path.basename(rel) });
    }
  }
  return { kept, excluded };
}

// 同一個資料夾的連號檔案構圖往往很像，分群讓人一眼看出來，但**不自動刪**
// （覆核者 Q11：程式不可以做不可逆的審美淘汰）。
function groupBySeries(items) {
  const groups = new Map();
  for (const it of items) {
    const stem = it.name.replace(/\.[^.]+$/, '').replace(/\d+/g, '#');
    const key = `${it.dir}::${stem}`;
    if (!groups.has(key)) groups.set(key, []);
    groups.get(key).push(it);
  }
  return [...groups.values()];
}

// ── 設定深度（客戶要知道的第 3 點）─────────────────────────────────
// 給「涵蓋哪些面向、各多細」，不給內容本文。
const ASPECTS = [
  { key: '外觀規格', test: j => !!j?.identity?.appearance },
  { key: '性格與價值觀', test: j => !!(j?.persona?.personality_traits || j?.persona?.values) },
  { key: '語氣與幽默感', test: j => !!(j?.persona?.voice_tone || j?.persona?.humor_style) },
  { key: '背景故事', test: j => !!j?.persona?.backstory },
  { key: '內容支柱與比重', test: j => Array.isArray(j?.content?.pillars) && j.content.pillars.length > 0 },
  { key: '視覺美學規範', test: j => !!j?.content?.aesthetic },
  { key: '合作邊界', test: j => !!(j?.content?.brand_do || j?.content?.brand_dont) },
  { key: '各平台內容分工', test: j => !!j?.social?.platforms },
];

const DOC_LABEL = {
  'character.md': '角色設定書',
  'content_style.md': '內容與語氣規範',
  'visual_prompts.md': '視覺規格書',
  'character-card.md': '角色卡',
};

function depthOf(id, repos, profile) {
  const docs = [];
  for (const tag of repos) {
    const base = path.join(REPO_ROOT, REPO_OF[tag], 'kols', id);
    let files = []; try { files = fs.readdirSync(base).filter(f => f.endsWith('.md')); } catch {}
    for (const f of files) {
      if (!DOC_LABEL[f]) continue;                       // 只列對外講得通的幾份
      if (docs.some(d => d.file === f)) continue;
      const lines = fs.readFileSync(path.join(base, f), 'utf8').split('\n').filter(l => l.trim()).length;
      docs.push({ file: f, label: DOC_LABEL[f], lines });
    }
  }
  const aspects = ASPECTS.filter(a => a.test(profile)).map(a => a.key);
  const countFields = (o) => {
    let n = 0;
    for (const v of Object.values(o || {})) {
      if (v && typeof v === 'object' && !Array.isArray(v)) n += countFields(v);
      else if (v !== null && v !== undefined && v !== '') n++;
    }
    return n;
  };
  // ai_assets 與 measurements 不計入對外的欄位數（那些不對外）
  const forCount = JSON.parse(JSON.stringify(profile || {}));
  delete forCount.ai_assets;
  if (forCount?.identity?.appearance) delete forCount.identity.appearance.measurements;

  const trainingSet = Object.values(profile?.ai_assets || {})
    .map(v => v?.soul_training?.training_image_count || v?.training_image_count || v?.image_count || 0)
    .reduce((a, b) => Math.max(a, b), 0);

  return {
    docs,
    doc_lines_total: docs.reduce((a, d) => a + d.lines, 0),
    spec_fields: countFields(forCount),
    aspects,
    pillar_count: (profile?.content?.pillars || []).length,
    training_set_images: trainingSet || null,
  };
}

// 沒有 profile.json 的人設（例如 leon-lim），名字從 character.md 的標題抓。
function nameFromCharacterMd(id, repos) {
  for (const tag of repos) {
    const f = path.join(REPO_ROOT, REPO_OF[tag], 'kols', id, 'character.md');
    try {
      const first = fs.readFileSync(f, 'utf8').split('\n').find(l => l.startsWith('# '));
      if (first) return first.replace(/^#\s*/, '').split('—')[0].trim();
    } catch {}
  }
  return null;
}

// ── 主流程 ──────────────────────────────────────────────────────────
const rows = [];
const skipped = [];

for (const p of inv.personas) {
  if (COPY.exclude?.[p.id]) { skipped.push({ id: p.id, why: COPY.exclude[p.id] }); continue; }
  // 🛑 門檻要套在「排除之後」的可用張數，不是原始張數。
  // wendy-yeo 原始 25 張全部是選角／探測／比對圖，可用 0 張——用原始數會把她放進型錄。

  const primary = p.primary_source;
  const profPath = path.join(REPO_ROOT, REPO_OF[primary], 'kols', p.id, 'profile.json');
  let profile = null; try { profile = JSON.parse(fs.readFileSync(profPath, 'utf8')); } catch {}
  // 主 repo 沒有 profile.json 時退到另一個 repo
  if (!profile) for (const t of p.in_repos) {
    try { profile = JSON.parse(fs.readFileSync(path.join(REPO_ROOT, REPO_OF[t], 'kols', p.id, 'profile.json'), 'utf8')); break; } catch {}
  }

  const { kept, excluded } = collectMedia(p.id, p.in_repos);
  const images = kept.filter(m => m.kind === 'image')
    .map(m => ({ ...m, ...scoreCandidate(m) }))
    .sort((a, b) => b.score - a.score || b.size - a.size);
  const videos = kept.filter(m => m.kind === 'video');

  if (images.length < MIN_IMAGES) {
    skipped.push({ id: p.id, why: `可用素材不足（原始 ${p.images} 張，排除 ${excluded.length} 張後只剩 ${images.length} 張，門檻 ${MIN_IMAGES}）` });
    continue;
  }

  const copy = COPY.personas?.[p.id] || {};

  rows.push({
    id: p.id,
    name: copy.name || p.name || nameFromCharacterMd(p.id, p.in_repos) || p.id,
    name_zh: p.name_zh || null,
    category: copy.category || p.category,
    age: p.age,
    ethnicity: p.ethnicity,
    location: p.location,
    languages: (profile?.identity?.languages || []).map(s => String(s).replace(/\s*\(.*?\)\s*/g, '').trim()),

    // 第 1 點：設定是什麼
    tagline: copy.tagline || null,                       // 🛑 手寫，程式產不出來
    archetype: profile?.persona?.archetype || null,
    personality: profile?.persona?.personality_traits || [],
    voice_tone: profile?.persona?.voice_tone || null,
    pillars: (profile?.content?.pillars || []).map(x => ({ name: x.name, weight: x.weight || null })),
    formats: profile?.content?.formats || [],
    aesthetic: profile?.content?.aesthetic
      ? { mood: profile.content.aesthetic.mood, palette: profile.content.aesthetic.color_palette } : null,
    boundaries: {
      fit: profile?.content?.brand_do || [],
      not: profile?.content?.brand_dont || [],
      note: profile?.content?.brand_fit_note || null,
    },

    // 第 3 點：細節到什麼程度
    depth: depthOf(p.id, p.in_repos, profile),

    // 第 2 點：有哪些素材（候選池，最後由人挑）
    media: {
      image_count: images.length,
      video_count: videos.length,
      candidates: images.slice(0, 24).map(m => ({
        rel: m.rel, mb: +(m.size / 1048576).toFixed(2),
        w: m.w || null, h: m.h || null,
        score: m.score, reasons: m.reasons,
      })),
      series_groups: groupBySeries(images).filter(g => g.length > 1)
        .map(g => g.map(x => x.rel)),
      videos: videos.map(m => ({ rel: m.rel, mb: +(m.size / 1048576).toFixed(2) })),
      excluded,
    },
  });
}

const out = {
  generated_by: 'catalog/tools/build_catalog.mjs',
  generated_at: new Date().toISOString().slice(0, 10),
  min_images: MIN_IMAGES,
  note: '型錄要顯示的內容。刻意不含：任何狀態、handle、三圍、prompt／Soul ID／模型／credits、營運統計期間。',
  included: rows.length,
  skipped,
  personas: rows.sort((a, b) => b.media.image_count - a.media.image_count),
};
fs.mkdirSync(path.dirname(OUT), { recursive: true });
fs.writeFileSync(OUT, JSON.stringify(out, null, 2) + '\n');

console.log(`收錄 ${rows.length} 位（門檻 ${MIN_IMAGES} 張圖）／排除 ${skipped.length} 位`);
const noTag = rows.filter(r => !r.tagline).map(r => r.id);
if (noTag.length) console.log(`⚠ 還沒寫一句話定位的 ${noTag.length} 位：${noTag.join(', ')}`);
console.log(`寫入 ${OUT}`);
