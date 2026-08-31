#!/usr/bin/env node
/**
 * 掃三個 repo 的 kols/，把「型錄裡有什麼可用」算成一份 JSON。
 *
 * 為什麼要有這支：本 repo 的覆核協定要求統計數字一律由程式計算後內嵌，
 * 不讓覆核者自己 parse、也不讓 Claude 手寫（review/README.md，C-07）。
 * 型錄的每一個數字（幾位人設、幾張圖、多少 MB）都必須能用這支重跑出來。
 *
 * 用法：
 *   node catalog/tools/scan_inventory.mjs                  # 寫入 catalog/data/inventory.json
 *   node catalog/tools/scan_inventory.mjs --print          # 只印摘要，不寫檔
 *   REPO_ROOT=/somewhere node catalog/tools/scan_inventory.mjs
 *
 * 三個 repo 必須是 REPO_ROOT 底下的姊妹目錄（預設 /home/user）。
 * 掃不到某個 repo 時不會失敗，會在 output 的 missing_repos 記下來——
 * 因為 Railway 的 build 環境只有 Virtual_KOL_Studio 一個。
 */
import fs from 'node:fs';
import path from 'node:path';

const REPO_ROOT = process.env.REPO_ROOT || '/home/user';
const OUT = path.join(import.meta.dirname, '..', 'data', 'inventory.json');

// 三個來源 repo。tag 是型錄內部用的短代號，source_of_truth_rank 見 KOLCAT_REVIEW_PACKET.md §2.4
const REPOS = [
  { dir: 'Virtual_KOL_Studio', tag: 'VKS', role: '人設 canon（identity / 外觀 / 視覺規格的真理來源）' },
  { dir: 'showgame-kol',       tag: 'SGK', role: '實戰線（已發布素材、平台連結、Metricool 成效）' },
  { dir: 'Buildup_KOL',        tag: 'BUP', role: '評估工具線（話題適配度、評分）' },
];

const IMG = new Set(['png', 'jpg', 'jpeg', 'webp', 'jfif']);
const VID = new Set(['mp4', 'mov', 'webm', 'mkv', 'avi']);

function walk(dir, hit) {
  let entries;
  try { entries = fs.readdirSync(dir, { withFileTypes: true }); } catch { return; }
  for (const e of entries) {
    const p = path.join(dir, e.name);
    if (e.isDirectory()) walk(p, hit);
    else if (e.isFile()) hit(p, fs.statSync(p).size);
  }
}

function classify(file, size, bucket) {
  const ext = path.extname(file).slice(1).toLowerCase();
  if (IMG.has(ext)) { bucket.images++; bucket.image_bytes += size; }
  else if (VID.has(ext)) { bucket.videos++; bucket.video_bytes += size; }
}

function readJson(p) {
  try { return JSON.parse(fs.readFileSync(p, 'utf8')); } catch { return null; }
}

const personas = {};   // id -> { sources: {tag: {...}}, ... }
const missing_repos = [];
const repo_totals = {};

for (const repo of REPOS) {
  const kolsDir = path.join(REPO_ROOT, repo.dir, 'kols');
  if (!fs.existsSync(kolsDir)) { missing_repos.push(repo.dir); continue; }

  const rt = { images: 0, videos: 0, image_bytes: 0, video_bytes: 0, persona_count: 0 };

  for (const e of fs.readdirSync(kolsDir, { withFileTypes: true })) {
    if (!e.isDirectory()) continue;
    const id = e.name;
    const pdir = path.join(kolsDir, id);

    const media = { images: 0, videos: 0, image_bytes: 0, video_bytes: 0 };
    walk(pdir, (f, s) => classify(f, s, media));

    const profile = readJson(path.join(pdir, 'profile.json'));
    const files = fs.readdirSync(pdir).filter(f => f.endsWith('.md')).sort();

    // 只取型錄真的會用到的欄位。刻意不抓 ai_assets（Soul ID / prompt / credits 不對外）。
    const ident = profile?.identity || {};
    const entry = {
      repo: repo.dir,
      has_profile_json: !!profile,
      docs: files,
      status: profile?.meta?.status ?? null,
      category: profile?.meta?.category ?? null,
      name: ident.name ?? null,
      name_zh: ident.name_zh ?? ident.native_name ?? null,
      nickname: ident.nickname ?? null,
      handle: ident.handle ?? null,
      age: ident.age ?? null,
      ethnicity: ident.ethnicity ?? null,
      location: ident.current_location ?? ident.origin ?? null,
      languages: Array.isArray(ident.languages) ? ident.languages.length : null,
      ...media,
    };

    personas[id] = personas[id] || { id, sources: {} };
    personas[id].sources[repo.tag] = entry;

    rt.images += media.images; rt.videos += media.videos;
    rt.image_bytes += media.image_bytes; rt.video_bytes += media.video_bytes;
    rt.persona_count++;
  }
  repo_totals[repo.tag] = rt;
}

// ── 每位人設的彙總判斷 ───────────────────────────────────────────────
// catalog_tier 是型錄的分區依據，不是人設的品質評價：
//   showcase  = 有圖可以撐一個人設頁（≥8 張圖）
//   thin      = 有圖但不足以撐一頁（1–7 張）
//   text_only = 一張圖都沒有，型錄只能給名字與定位
const rows = Object.values(personas).map(p => {
  const tags = Object.keys(p.sources);
  const images = tags.reduce((a, t) => a + p.sources[t].images, 0);
  const videos = tags.reduce((a, t) => a + p.sources[t].videos, 0);
  const image_bytes = tags.reduce((a, t) => a + p.sources[t].image_bytes, 0);
  const video_bytes = tags.reduce((a, t) => a + p.sources[t].video_bytes, 0);

  // 真理來源：VKS > SGK > BUP（見 packet §2.4，這是待覆核的立場不是定案）
  const primary = ['VKS', 'SGK', 'BUP'].find(t => tags.includes(t));
  const s = p.sources[primary];

  const live = tags.some(t => p.sources[t].status === '正在經營中');
  const tier = images >= 8 ? 'showcase' : images > 0 ? 'thin' : 'text_only';

  return {
    id: p.id,
    in_repos: tags,
    primary_source: primary,
    name: tags.map(t => p.sources[t].name).find(Boolean) || null,
    name_zh: tags.map(t => p.sources[t].name_zh).find(Boolean) || null,
    nickname: tags.map(t => p.sources[t].nickname).find(Boolean) || null,
    handle: tags.map(t => p.sources[t].handle).find(Boolean) || null,
    category: tags.map(t => p.sources[t].category).find(Boolean) || null,
    age: tags.map(t => p.sources[t].age).find(Boolean) ?? null,
    ethnicity: tags.map(t => p.sources[t].ethnicity).find(Boolean) || null,
    location: tags.map(t => p.sources[t].location).find(Boolean) || null,
    status_by_repo: Object.fromEntries(tags.map(t => [t, p.sources[t].status])),
    published_live: live,
    duplicated: tags.length > 1,
    field_conflicts: fieldConflicts(p.sources, tags),
    missing_profile_json: tags.filter(t => !p.sources[t].has_profile_json),
    images, videos, image_bytes, video_bytes,
    catalog_tier: tier,
  };
}).sort((a, b) => b.images - a.images || a.id.localeCompare(b.id));

// 同一位人設在兩個 repo 的同名欄位值不一樣 → 型錄要顯示哪一個？這是 packet §2.4 的證據。
function fieldConflicts(sources, tags) {
  if (tags.length < 2) return [];
  const check = ['name', 'name_zh', 'handle', 'category', 'age', 'ethnicity'];
  const out = [];
  for (const f of check) {
    const vals = [...new Set(tags.map(t => sources[t][f]).filter(v => v !== null && v !== undefined))];
    if (vals.length > 1) out.push({ field: f, values: Object.fromEntries(tags.map(t => [t, sources[t][f]])) });
  }
  return out;
}

const mb = b => Math.round(b / 1048576 * 10) / 10;
const sum = (k) => rows.reduce((a, r) => a + r[k], 0);

const tierCount = t => rows.filter(r => r.catalog_tier === t).length;

// ── 收錄重數的分解（KC-02）─────────────────────────────────────────
// 覆核者抓到 §2.1 手寫的 repo 人設數（30/11/24=65）與「42 位聯集、16 位重複」
// 對不上：d2=16 時 2x = 65-42-16 = 7 → x=3.5，非整數，所以 65 本身不可能成立。
// 實際是 31/10/17=58，58-42=16，恰好等於雙重收錄數，三重收錄為 0。
// 把這個恆等式做成輸出＋測試，不要再靠手寫。
const multiplicity = {};
for (const r of rows) multiplicity[r.in_repos.length] = (multiplicity[r.in_repos.length] || 0) + 1;

const pair_intersections = {};
for (const r of rows) {
  if (r.in_repos.length === 2) {
    const k = [...r.in_repos].sort().join('∩');
    pair_intersections[k] = (pair_intersections[k] || 0) + 1;
  }
}
const exclusive = {};
for (const r of rows) {
  if (r.in_repos.length === 1) exclusive[r.in_repos[0]] = (exclusive[r.in_repos[0]] || 0) + 1;
}

const total_records = rows.reduce((a, r) => a + r.in_repos.length, 0);
const repo_record_sum = Object.values(repo_totals).reduce((a, t) => a + t.persona_count, 0);
const excess = total_records - rows.length;             // Σ(重數-1)
const expected_excess = Object.entries(multiplicity)
  .reduce((a, [n, c]) => a + (Number(n) - 1) * c, 0);

// 🛑 恆等式：三個 repo 的人設數相加 == 紀錄總數，且 紀錄總數 - 聯集 == Σ(重數-1)。
// 任何一邊不符就是 bug，直接讓程式失敗——不要印警告然後繼續（文件寫過會再犯，程式不會）。
const identity_ok = repo_record_sum === total_records && excess === expected_excess;

const inventory = {
  generated_by: 'catalog/tools/scan_inventory.mjs',
  generated_at: new Date().toISOString().slice(0, 10),
  repo_root: REPO_ROOT,
  missing_repos,
  note: '每個數字都由本程式現算。手寫的數字若與這份不符，那是 bug，不是這份錯。',
  repos: REPOS.map(r => ({ ...r, totals: repo_totals[r.tag] || null })),
  reconciliation: {
    note: 'KC-02：repo 人設數相加必須等於紀錄總數，紀錄總數減聯集必須等於 Σ(重數-1)。手寫的數字對不上就是手寫錯了。',
    repo_persona_counts: Object.fromEntries(Object.entries(repo_totals).map(([t, v]) => [t, v.persona_count])),
    repo_record_sum,
    total_records,
    unique_personas: rows.length,
    excess_records: excess,
    expected_excess,
    identity_holds: identity_ok,
    personas_by_multiplicity: multiplicity,
    exclusive_to_one_repo: exclusive,
    pair_intersections,
    triple_intersection: multiplicity[3] || 0,
  },
  totals: {
    unique_personas: rows.length,
    duplicated_personas: rows.filter(r => r.duplicated).length,
    personas_with_field_conflicts: rows.filter(r => r.field_conflicts.length > 0).length,
    published_live: rows.filter(r => r.published_live).length,
    tier_showcase: tierCount('showcase'),
    tier_thin: tierCount('thin'),
    tier_text_only: tierCount('text_only'),
    images: sum('images'),
    videos: sum('videos'),
    image_mb: mb(sum('image_bytes')),
    video_mb: mb(sum('video_bytes')),
    total_mb: mb(sum('image_bytes') + sum('video_bytes')),
    avg_image_mb: Math.round(sum('image_bytes') / sum('images') / 1048576 * 100) / 100,
    avg_video_mb: Math.round(sum('video_bytes') / sum('videos') / 1048576 * 100) / 100,
  },
  personas: rows,
};

if (!identity_ok) {
  console.error('🛑 恆等式不成立，盤點有 bug，不要用這份數字：');
  console.error(`   repo 人設數相加 = ${repo_record_sum}，紀錄總數 = ${total_records}`);
  console.error(`   紀錄 - 聯集 = ${excess}，Σ(重數-1) = ${expected_excess}`);
  process.exit(2);
}

if (process.argv.includes('--print')) {
  const t = inventory.totals;
  const rc = inventory.reconciliation;
  console.log(`人設 ${t.unique_personas} 位（重複收錄 ${t.duplicated_personas}、欄位互斥 ${t.personas_with_field_conflicts}、已上線 ${t.published_live}）`);
  console.log(`對帳：${Object.entries(rc.repo_persona_counts).map(([k, v]) => k + ' ' + v).join(' + ')} = ${rc.repo_record_sum} 筆紀錄 − ${rc.unique_personas} 位聯集 = ${rc.excess_records}（雙重 ${rc.personas_by_multiplicity[2] || 0}、三重 ${rc.triple_intersection}）✅`);
  console.log(`分區：可撐一頁 ${t.tier_showcase} / 素材不足 ${t.tier_thin} / 只有文字 ${t.tier_text_only}`);
  console.log(`素材：圖 ${t.images} 張 ${t.image_mb} MB（平均 ${t.avg_image_mb} MB）｜影片 ${t.videos} 支 ${t.video_mb} MB（平均 ${t.avg_video_mb} MB）｜合計 ${t.total_mb} MB`);
  if (missing_repos.length) console.log(`⚠ 掃不到：${missing_repos.join(', ')}`);
} else {
  fs.mkdirSync(path.dirname(OUT), { recursive: true });
  fs.writeFileSync(OUT, JSON.stringify(inventory, null, 2) + '\n');
  console.log(`寫入 ${OUT}`);
  console.log(`人設 ${inventory.totals.unique_personas} 位、圖 ${inventory.totals.images} 張、影片 ${inventory.totals.videos} 支、合計 ${inventory.totals.total_mb} MB`);
}
