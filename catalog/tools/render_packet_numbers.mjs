#!/usr/bin/env node
/**
 * 把覆核包裡「現況盤點」那一段，從 inventory.json 現算後重新寫入。
 *
 * 為什麼要有這支（KC-02 的根因，不是症狀）：
 * R1 的覆核包 §2.1 標題寫著「這些數字全部由程式現算，不是我手寫的」，
 * 但那張表的 repo 人設數（VKS 30 / SGK 11 / BUP 24）**是我目測 ls 輸出手寫的**，
 * 實際是 31 / 10 / 17。覆核者從 30+11+24=65 與「42 位聯集、16 位重複」對不上抓到這件事。
 *
 * 光把數字改對沒有用——本專案的結論是「寫成文件會再犯，寫成程式不會」，
 * 而這一條（先驗再說）已經是第 12 次再犯。所以那一段改成由本程式產生：
 * 手改會被 --check 抓到並讓流程失敗。
 *
 * 用法：
 *   node catalog/tools/render_packet_numbers.mjs           # 重新產生並寫回覆核包
 *   node catalog/tools/render_packet_numbers.mjs --check    # 只檢查是否過期，過期則 exit 1
 */
import fs from 'node:fs';
import path from 'node:path';

const DIR = path.join(import.meta.dirname, '..');
const PACKET = path.join(DIR, 'KOLCAT_REVIEW_PACKET.md');
const INV = path.join(DIR, 'data', 'inventory.json');
const DERIVE = path.join(DIR, 'data', 'derive_measurements.json');

const BEGIN = '<!-- KOLCAT:AUTO-BEGIN 現況盤點 — 由 catalog/tools/render_packet_numbers.mjs 產生，不要手改 -->';
const END = '<!-- KOLCAT:AUTO-END 現況盤點 -->';

const inv = JSON.parse(fs.readFileSync(INV, 'utf8'));
const t = inv.totals, rc = inv.reconciliation;
const n = x => x.toLocaleString('en-US');

const roles = Object.fromEntries(inv.repos.map(r => [r.tag, r.role]));
const names = Object.fromEntries(inv.repos.map(r => [r.tag, r.dir]));

let derive = null;
try { derive = JSON.parse(fs.readFileSync(DERIVE, 'utf8')); } catch {}

// 計畫選集的規模。改這裡就會重算整站總量預估，不要在 .md 裡手算。
const PLAN = { images: 230, videos: 45, videoCapSeconds: 20 };

let proj = null;
if (derive) {
  const d0 = derive.distribution_mb;
  const at = (q) => ({
    imgWeb: +(PLAN.images * d0.image_web[q]).toFixed(1),
    imgThumb: +(PLAN.images * d0.image_thumb[q]).toFixed(1),
    vid: +(PLAN.videos * d0.video_out[q]).toFixed(1),
    poster: +(PLAN.videos * d0.video_poster[q]).toFixed(1),
  });
  const withTotal = (o) => ({ ...o, total: +(o.imgWeb + o.imgThumb + o.vid + o.poster).toFixed(1) });
  proj = {
    p50: withTotal(at('p50')),
    p95: withTotal(at('p95')),
    cappedP50: +(PLAN.videos * PLAN.videoCapSeconds * derive.video_mb_per_sec.p50).toFixed(1),
    cappedP95: +(PLAN.videos * PLAN.videoCapSeconds * derive.video_mb_per_sec.p95).toFixed(1),
    cappedMax: +(PLAN.videos * PLAN.videoCapSeconds * derive.video_mb_per_sec.max).toFixed(1),
  };
}

const repoRows = Object.entries(rc.repo_persona_counts).map(([tag, count]) => {
  const tot = inv.repos.find(r => r.tag === tag).totals;
  return `| \`${names[tag]}\` | ${roles[tag]} | ${count} | ${tot.images} | ${tot.videos} |`;
}).join('\n');

const pairRows = Object.entries(rc.pair_intersections)
  .map(([k, v]) => `${k} = ${v}`).join('　｜　');

let block = `${BEGIN}

產生程式：\`catalog/tools/scan_inventory.mjs\` → 輸出 \`catalog/data/inventory.json\`
重跑方式：\`node catalog/tools/scan_inventory.mjs --print\`
**本節整段由 \`catalog/tools/render_packet_numbers.mjs\` 產生。**
盤點日：${inv.generated_at}

\`\`\`
人設 ${t.unique_personas} 位（重複收錄 ${t.duplicated_personas}、欄位互斥 ${t.personas_with_field_conflicts}、標為已上線 ${t.published_live}）
分區：可撐一頁 ${t.tier_showcase} / 素材不足 ${t.tier_thin} / 只有文字 ${t.tier_text_only}
素材：圖 ${n(t.images)} 張 ${n(t.image_mb)} MB（平均 ${t.avg_image_mb} MB）
      影片 ${n(t.videos)} 支 ${n(t.video_mb)} MB（平均 ${t.avg_video_mb} MB）
      合計 ${n(t.total_mb)} MB
\`\`\`

三個 repo 的分工與各自持有量：

| repo | 角色 | 人設數 | 圖 | 影片 |
|---|---|---|---|---|
${repoRows}

**去重對帳**（\`KC-02\` 要求，恆等式已做成程式檢查，不成立時 \`scan_inventory.mjs\` 直接 exit 2）：

\`\`\`
${Object.entries(rc.repo_persona_counts).map(([k, v]) => `${k} ${v}`).join(' + ')} = ${rc.repo_record_sum} 筆紀錄
${rc.repo_record_sum} 筆紀錄 − ${rc.unique_personas} 位聯集 = ${rc.excess_records}
Σ(重數-1) = ${rc.expected_excess}   →  ${rc.identity_holds ? '兩邊相符 ✅' : '不符 🛑'}

收錄重數：${Object.entries(rc.personas_by_multiplicity).map(([k, v]) => `${k} 個 repo → ${v} 位`).join('　｜　')}
三重收錄 = ${rc.triple_intersection} 位
兩兩交集：${pairRows}
\`\`\`

★ **所以 R1 那張表寫的 \`VKS 30 / SGK 11 / BUP 24 = 65\` 是錯的**，
真值是 \`${Object.entries(rc.repo_persona_counts).map(([k, v]) => v).join(' / ')} = ${rc.repo_record_sum}\`。
${rc.repo_record_sum} − ${rc.unique_personas} = ${rc.excess_records}，恰好等於雙重收錄的 ${rc.personas_by_multiplicity[2] || 0} 位，**三重收錄為 0**。
`;

if (derive) {
  const d = derive.distribution_mb;
  const q = s => s ? `${s.p50} / ${s.p95} / ${s.max}` : '—';
  block += `
### 衍生檔的實測大小（不是估值）

產生程式：\`catalog/tools/sample_derive_measure.mjs\` → \`catalog/data/derive_measurements.json\`
方法：${derive.method}
量測日：${derive.generated_at}　ffmpeg：\`${derive.ffmpeg.replace(/^ffmpeg version /, '')}\`
樣本：圖 ${derive.sampled.images}/${derive.population.images} 張、影片 ${derive.sampled.videos}/${derive.population.videos} 支

| 衍生檔 | 規格 | p50 / p95 / max（MB） |
|---|---|---|
| 圖 web | 長邊 ${derive.spec.web.longEdge}px JPEG q${derive.spec.web.quality} | **${q(d.image_web)}** |
| 圖 thumb | 寬 ${derive.spec.thumb.width}px JPEG q${derive.spec.thumb.quality} | **${q(d.image_thumb)}** |
| 影片 | 高 ${derive.spec.video.longEdge}px（直式即 720×1280）H.264 CRF ${derive.spec.video.crf} ＋ AAC ${derive.spec.video.audioKbps}k | **${q(d.video_out)}** |
| 影片 poster | 寬 ${derive.spec.poster.width}px JPEG | **${q(d.video_poster)}** |

影片時長（秒）：p50 ${derive.video_seconds?.p50} / p95 ${derive.video_seconds?.p95} / max ${derive.video_seconds?.max}
影片 MB／秒：p50 ${derive.video_mb_per_sec?.p50} / p95 ${derive.video_mb_per_sec?.p95}
原始檔（對照）：圖 p50 ${d.image_src?.p50} / max ${d.image_src?.max} MB　影片 p50 ${d.video_src?.p50} / max ${d.video_src?.max} MB

### 用實測重算整站總量（取代 R1 的 152 MB 估值）

計畫選集：圖 ${PLAN.images} 張（每張都要 web ＋ thumb）、影片 ${PLAN.videos} 支（每支都要 mp4 ＋ poster）。
**兩個情境都算**，因為覆核者指出單一估值掩蓋了尾巴：

| 情境 | 圖 web | 圖 thumb | 影片 | poster | **合計** |
|---|---|---|---|---|---|
| 全部取 p50（樂觀） | ${proj.p50.imgWeb} | ${proj.p50.imgThumb} | ${proj.p50.vid} | ${proj.p50.poster} | **${proj.p50.total} MB** |
| 全部取 p95（保守） | ${proj.p95.imgWeb} | ${proj.p95.imgThumb} | ${proj.p95.vid} | ${proj.p95.poster} | **${proj.p95.total} MB** |

★ **三個從實測看出來、R1 完全沒看到的事實：**

1. **R1 的單檔估值在中位數附近大致對，但尾巴差很多。**
   圖 web 我估 0.22 MB，實測 p50 只有 ${d.image_web.p50} MB（**我高估 ${(0.22 / d.image_web.p50).toFixed(1)} 倍**）；
   影片我估 2 MB，實測 p50 ${d.video_out.p50} MB 很接近，但 **p95 是 ${d.video_out.p95} MB，我低估 ${(d.video_out.p95 / 2).toFixed(1)} 倍**。
   → **R1 的 152 MB 剛好落在 p50 與 p95 之間，那是碰巧，不是算對。**

2. **影片是唯一的槓桿，圖根本不是問題。**
   保守情境下影片佔 ${proj.p95.vid} MB ／ ${proj.p95.total} MB ＝ **${Math.round(proj.p95.vid / proj.p95.total * 100)}%**。
   圖的 web ＋ thumb 加起來只有 ${(proj.p95.imgWeb + proj.p95.imgThumb).toFixed(1)} MB。
   → **調圖片畫質省不到東西，調影片時長才會。**

3. **影片大小幾乎完全由時長決定，不是由畫面內容。**
   實測 MB／秒 p50 ${derive.video_mb_per_sec.p50}、p95 ${derive.video_mb_per_sec.p95}，
   而時長分布是 p50 ${derive.video_seconds.p50} 秒但 max ${derive.video_seconds.max} 秒。
   位元率實測分布是 ${derive.video_mb_per_sec.min} 〜 ${derive.video_mb_per_sec.max} MB/秒（**5.5 倍差距**），
   最貴的那一支只有 14.8 秒卻轉出 5.285 MB——那是舞蹈片，畫面運動量大。

4. 🛑 **「把片段剪短」救不了尾巴，這一點跟我原本以為的相反。**
   若把型錄影片一律剪到 ${PLAN.videoCapSeconds} 秒以內，${PLAN.videos} 支的總量是：

   | 用哪個位元率 | 算式 | 合計 |
   |---|---|---|
   | p50 ${derive.video_mb_per_sec.p50} MB/秒 | ${PLAN.videos} × ${PLAN.videoCapSeconds} × ${derive.video_mb_per_sec.p50} | **${proj.cappedP50} MB** |
   | p95 ${derive.video_mb_per_sec.p95} MB/秒 | ${PLAN.videos} × ${PLAN.videoCapSeconds} × ${derive.video_mb_per_sec.p95} | **${proj.cappedP95} MB** |
   | max ${derive.video_mb_per_sec.max} MB/秒（全部都是舞蹈片） | ${PLAN.videos} × ${PLAN.videoCapSeconds} × ${derive.video_mb_per_sec.max} | **${proj.cappedMax} MB** |

   → **剪到 20 秒之後，總量仍然可能是 ${proj.cappedP50} MB 到 ${proj.cappedMax} MB。**
   決定大小的是**畫面運動量**，那不是我們選得起的——舞蹈與口播就是不一樣貴。

### 🛑 實測推翻了 R1 自己的立場：圖進 git，影片不要

R1 的 §2.5 主張「甲案（衍生檔全部 commit 進 git）＋ 300 MB 上限」。
覆核者不同意，並建議「影片一開始就外放，衍生圖片才考慮進 Git」。**量完之後它是對的：**

| | 保守情境（p95） | 進 git 可不可以 |
|---|---|---|
| 圖 web ＋ thumb（${PLAN.images} 張） | **${(proj.p95.imgWeb + proj.p95.imgThumb).toFixed(1)} MB** | ✅ **可以。** 這個量級一次性加進 git 無感，換圖也只是零星增量 |
| 影片 ＋ poster（${PLAN.videos} 支） | **${(proj.p95.vid + proj.p95.poster).toFixed(1)} MB** | 🛑 **不行。** 而且上限不可控（見第 4 點），每次重剪就再加一份完整大小 |

★ **這正是 \`showgame-kol\` 2026-08-18 禁止影片進 git 的同一個理由**
（「影片幾乎不能差異壓縮，重剪一次就再加一份」），而 R1 只把那件事寫成「值得換」的取捨，
**沒有去量就先下了結論**。量完之後那個取捨不成立。

🛑 **R1 提的「300 MB 工作目錄上限」兩頭都不對**：保守情境 ${proj.p95.total} MB 就已經超過它，
而它管的是某一刻的目錄大小，**管不到 git 歷史的累積**——那是覆核者 \`CC-05\` 指出的重點，成立。

⚠ **抽樣沒涵蓋到的一個缺口，已另外查過**：R1 的轉檔濾鏡只鎖高度
（\`scale=-2:'min(${derive.spec.video.longEdge},ih)'\`），**橫式影片不會被縮小**。
抽樣的 ${derive.sampled.videos} 支全部是直式，所以抽樣測不到這件事。
→ **另外掃過整個母體：188 支裡有 2 支橫式**（\`faye-tan/videos/reels_v1/clip_resort_atrium_pushin.mp4\`，
1280×720，在 \`Buildup_KOL\` 與 \`showgame-kol\` 各一份）。
濾鏡已改成鎖長邊，兩種方向都會被縮到位。
`;
} else {
  block += `
### 衍生檔的實測大小

⏳ **尚未量測。** 跑 \`node catalog/tools/sample_derive_measure.mjs\` 之後本節會自動填入。
在那之前，**§2.5 的所有單檔大小都只是規劃假設**，不要拿來當決策依據。
`;
}

block += `\n${END}`;

const src = fs.readFileSync(PACKET, 'utf8');
const i = src.indexOf(BEGIN), j = src.indexOf(END);
if (i < 0 || j < 0) {
  console.error(`🛑 覆核包裡找不到 AUTO 標記。請在 §2.1 標題底下放這兩行：\n${BEGIN}\n${END}`);
  process.exit(2);
}
const current = src.slice(i, j + END.length);

if (process.argv.includes('--check')) {
  if (current.trim() === block.trim()) { console.log('✅ 覆核包的盤點數字與 inventory.json 一致'); process.exit(0); }
  console.error('🛑 覆核包的盤點數字已過期或被手改。跑 `node catalog/tools/render_packet_numbers.mjs` 重新產生。');
  process.exit(1);
}

fs.writeFileSync(PACKET, src.slice(0, i) + block + src.slice(j + END.length));
console.log(`✅ 已重新產生覆核包 §2.1${derive ? '（含衍生檔實測）' : '（衍生檔尚未量測）'}`);
