#!/usr/bin/env node
/**
 * 從 catalog.json ＋ assets/ 產生靜態頁面 → catalog/public/
 *
 * 內容依據只有使用者說的那四件事（見覆核包 §2.2）：
 *   1 設定是什麼  2 有哪些素材  3 細節到什麼程度  4 大概的營運數據
 * 🛑 不輸出任何狀態、handle、三圍、prompt／模型／credits、營運統計期間。
 */
import fs from 'node:fs';
import crypto from 'node:crypto';
import path from 'node:path';

const DIR = path.join(import.meta.dirname, '..');
const PUB = path.join(DIR, 'public');
const cat = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'catalog.json'), 'utf8'));
// 🛑 首頁與報價頁的文字全部來自 pitch.json（對外報價 PPT 逐字匯入），不要在這支程式裡編字。
// 那份 PPT 的數字、價格、方案內容是業務承諾（覆核包 §12.6）。
// ⚠ 案例段落渲染的是 `why_public` 不是 `why`：使用者 2026-09-03 裁決 PP-06
//   「改寫得模糊一點再放」，`why` 留逐字原文存查。
const pitch = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'pitch.json'), 'utf8'));
const copy  = JSON.parse(fs.readFileSync(path.join(DIR, 'data', 'copy.json'), 'utf8'));

const esc = s => String(s ?? '').replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');

const CAT_LABEL = {
  travel_culture: '旅遊・城市文化', digital_culture: '數位娛樂・科技', outdoor_adventure: '戶外・登山',
  knowledge_culture: '知識・規則研究', beauty: '美妝・保養', nightlife: '夜生活', lifestyle: '生活風格',
  fitness: '健身', gaming: '遊戲・實況', wellness: '身心健康', 'luxury lifestyle': '精品生活',
  mythology_immersion: '神話沉浸', history_immersion: '歷史沉浸', null: '其他',
};
const catLabel = c => CAT_LABEL[c] || c || '其他';

// 語言標準化：只留語言名，不留熟練度括號
const langShort = s => String(s).replace(/\s*[（(].*?[)）]\s*/g, '').replace(/\s*—.*$/, '').trim();

// 地區歸成市場（篩選器用，依 Q2 把語言與地區合併成「市場」）
function market(loc = '') {
  const l = String(loc);
  if (/Taiwan|台北|台中|高雄|新竹|台灣/i.test(l)) return '台灣';
  if (/Singapore|新加坡|丹戎巴葛/i.test(l)) return '新加坡';
  if (/Malaysia|Kuala Lumpur/i.test(l)) return '馬來西亞';
  if (/Japan|Kyoto|Tokyo|京都/i.test(l)) return '日本';
  if (/Korea|Seoul|首爾/i.test(l)) return '韓國';
  if (/India|Mumbai/i.test(l)) return '印度';
  if (/France|Paris/i.test(l)) return '法國';
  if (/California|Los Angeles|LA\b/i.test(l)) return '美國';
  return '跨區';
}

// 🛑 素材網址一定要帶內容雜湊。
// 2026-09-03 踩到：伺服器對 /assets/ 送 `max-age=604800`（七天），
// 而 `hero.jpg` 這種網址是固定的、內容卻會換。換完圖之後使用者的瀏覽器
// 七天內都拿自己的舊快取，看到的還是舊封面——而且**客戶也會遇到同一件事**，
// 那不是「叫他重新整理」能解決的。
// → 網址後面接 `?v=<內容雜湊>`：內容一變網址就變，快取自然失效，
//   而沒變的檔案仍然享有七天快取。
const vtag = (abs) => {
  try {
    const h = crypto.createHash('md5').update(fs.readFileSync(abs)).digest('hex').slice(0, 10);
    return '?v=' + h;
  } catch { return ''; }
};

// 🛑 讀 manifest,不要掃資料夾。
// 掃資料夾有兩個問題,兩個都實測過：
//   ① 上一次建置留下的檔案會被當成「還在的素材」→ 頁面多出不存在的影片格。
//   ② 排序只能靠檔名,而檔名現在是雜湊,跟使用者挑選的順序無關。
// manifest 由 build_assets 產生,它同時記了「有哪些」與「什麼順序」。
const assetsOf = id => {
  const d = path.join(DIR, 'assets', id);
  const u = f => `/assets/${id}/${f}` + vtag(path.join(d, f));
  let man;
  try { man = JSON.parse(fs.readFileSync(path.join(d, 'manifest.json'), 'utf8')); }
  catch {
    console.error(`🛑 ${id} 沒有 manifest.json —— 先跑 build_assets.mjs 再跑這一支。`);
    process.exit(2);
  }
  const has = f => f && fs.existsSync(path.join(d, f));
  return {
    hero: has(man.hero) ? u(man.hero) : (has(man.gallery[0]?.web) ? u(man.gallery[0].web) : null),
    gallery: man.gallery.filter(g => has(g.web)).map(g => ({ web: u(g.web), thumb: u(g.thumb) })),
    // 影片本體還沒轉,所以這一輪仍然只有 poster;轉好之後 mp4/webm 就會自己出現。
    videos: man.videos.filter(v => has(v.poster)).map(v => ({
      poster: u(v.poster),
      mp4: has(v.mp4) ? u(v.mp4) : null,
      webm: has(v.webm) ? u(v.webm) : null,
    })),
  };
};

const CSS = `
:root{
  --bg:#0b0b0d; --bg2:#1e1e26; --line:rgba(242,242,244,.12); --line2:rgba(242,242,244,.2);
  --ink:#f4f0e8; --ink2:#c2c2cc; --ink3:#92929e; --ink4:#6f6f7c;
  --accent:#d8b955; --accent2:#e7cd74;
  --serif:"Noto Serif TC",Georgia,"Songti TC",serif;
  --sans:"Noto Sans TC",-apple-system,"Segoe UI","PingFang TC","Microsoft JhengHei",sans-serif;
}
*{box-sizing:border-box}
html{scroll-behavior:smooth}
body{margin:0;background:var(--bg);color:var(--ink);font-family:var(--sans);
  -webkit-font-smoothing:antialiased;line-height:1.7}
img{max-width:100%;display:block}
a{color:inherit;text-decoration:none}
.wrap{max-width:1240px;margin:0 auto;padding:0 24px}

/* ── 頁首 ── */
.top{border-bottom:1px solid var(--line);position:sticky;top:0;z-index:50;
  background:rgba(11,11,13,.88);backdrop-filter:blur(14px)}
.top .wrap{display:flex;align-items:center;gap:20px;height:64px}
.brand{font-family:var(--serif);font-size:19px;letter-spacing:.06em}
.brand b{color:var(--accent2);font-weight:600}
.top nav{margin-left:auto;display:flex;gap:22px;font-size:13px;color:var(--ink2)}
.top nav a:hover{color:var(--ink)}

/* ── 開場 ── */
.hero{padding:96px 0 56px;border-bottom:1px solid var(--line)}
.hero h1{font-family:var(--serif);font-size:clamp(34px,5.4vw,60px);line-height:1.18;margin:0 0 22px;
  font-weight:500;letter-spacing:.01em}
.hero h1 em{font-style:normal;color:var(--accent2)}
.hero .lede{max-width:660px;color:var(--ink2);font-size:16.5px;margin:0 0 30px}
.stats{display:flex;flex-wrap:wrap;gap:0;border:1px solid var(--line);border-radius:3px;overflow:hidden;max-width:760px}
.stat{flex:1 1 150px;padding:18px 22px;border-right:1px solid var(--line)}
.stat:last-child{border-right:0}
.stat b{display:block;font-family:var(--serif);font-size:30px;color:var(--accent2);line-height:1.1}
.stat span{font-size:12px;color:var(--ink3);letter-spacing:.08em}

/* ── AI 揭露（首屏，CC-04）── */
.disclose{margin-top:34px;border-left:2px solid var(--accent);background:var(--bg2);
  padding:16px 20px;max-width:760px;border-radius:0 3px 3px 0}
.disclose b{color:var(--accent2);font-weight:600}
.disclose p{margin:6px 0 0;color:var(--ink2);font-size:13.5px}

/* ── 篩選 ── */
.filters{padding:30px 0 8px;position:sticky;top:64px;background:var(--bg);z-index:40;
  border-bottom:1px solid var(--line)}
.frow{display:flex;gap:10px;align-items:baseline;flex-wrap:wrap;margin-bottom:12px}
.frow>span{font-size:11px;color:var(--ink3);letter-spacing:.12em;min-width:52px}
.chip{border:1px solid var(--line2);background:transparent;color:var(--ink2);
  padding:5px 13px;border-radius:100px;font-size:12.5px;cursor:pointer;font-family:inherit;
  transition:.16s}
.chip:hover{border-color:var(--ink3);color:var(--ink)}
.chip[aria-pressed=true]{background:var(--accent2);border-color:var(--accent2);color:#17130a;font-weight:600}
.count{font-size:12px;color:var(--ink3);padding:10px 0 14px}

/* ── 型錄牆 ── */
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(248px,1fr));gap:22px;padding:22px 0 80px}
.card{background:var(--bg2);border:1px solid var(--line);border-radius:3px;overflow:hidden;
  transition:.2s;display:flex;flex-direction:column}
.card:hover{border-color:var(--line2);transform:translateY(-3px)}
.card .ph{aspect-ratio:3/4;background:#1a1a20;overflow:hidden;position:relative}
.card .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 12%;transition:.4s}
.card:hover .ph img{transform:scale(1.03)}
.card .body{padding:15px 16px 17px}
.card .nm{font-family:var(--serif);font-size:18px;margin:0 0 2px;font-weight:500}
.card .zh{font-size:12px;color:var(--ink3);margin:0 0 9px}
.card .tl{font-size:13px;color:var(--ink2);margin:0 0 12px;line-height:1.6;
  display:-webkit-box;-webkit-line-clamp:3;-webkit-box-orient:vertical;overflow:hidden}
.tags{display:flex;flex-wrap:wrap;gap:5px}
.tag{font-size:10.5px;letter-spacing:.05em;color:var(--ink3);border:1px solid var(--line2);
  padding:2px 8px;border-radius:2px}
.tag.k{color:var(--accent2);border-color:#4a3d16}

/* ── 人設頁 ── */
.pback{font-size:12.5px;color:var(--ink3);padding:26px 0 0}
.pback:hover{color:var(--ink)}
.phead{display:grid;grid-template-columns:minmax(0,420px) minmax(0,1fr);gap:44px;padding:30px 0 46px;
  border-bottom:1px solid var(--line);align-items:start}
.phead .pimg{aspect-ratio:3/4;background:#1a1a20;border-radius:3px;overflow:hidden}
.phead .pimg img{width:100%;height:100%;object-fit:cover;object-position:50% 10%}
.phead h1{font-family:var(--serif);font-size:clamp(30px,4vw,44px);margin:0 0 4px;font-weight:500}
.phead .zh{color:var(--ink3);font-size:14px;margin:0 0 18px}
.phead .tl{font-size:18px;color:var(--accent2);font-family:var(--serif);line-height:1.6;margin:0 0 26px}
.facts{display:grid;grid-template-columns:repeat(auto-fit,minmax(120px,1fr));gap:1px;
  background:var(--line);border:1px solid var(--line);border-radius:3px;overflow:hidden;margin-bottom:24px}
.fact{background:var(--bg2);padding:13px 15px}
.fact span{display:block;font-size:10.5px;color:var(--ink3);letter-spacing:.1em;margin-bottom:3px}
.fact b{font-weight:500;font-size:13.5px}

section.sec{padding:44px 0;border-bottom:1px solid var(--line)}
section.sec>h2{font-family:var(--serif);font-size:13px;letter-spacing:.2em;color:var(--ink3);
  text-transform:uppercase;margin:0 0 22px;font-weight:400}
.two{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:36px}
.lbl{font-size:11px;letter-spacing:.1em;color:var(--ink3);margin:0 0 8px}
.prose{color:var(--ink2);font-size:14.5px;margin:0}
ul.plain{list-style:none;padding:0;margin:0}
ul.plain li{padding:7px 0;border-bottom:1px solid var(--line);font-size:14px;color:var(--ink2);
  display:flex;justify-content:space-between;gap:14px}
ul.plain li:last-child{border-bottom:0}
ul.plain li b{color:var(--ink);font-weight:500}
ul.plain li i{font-style:normal;color:var(--accent2);font-size:12.5px;white-space:nowrap}


/* 圖庫 */
.gal{display:grid;grid-template-columns:repeat(auto-fill,minmax(190px,1fr));gap:12px}
.gal a{aspect-ratio:3/4;overflow:hidden;background:#1a1a20;border-radius:2px;display:block}
.gal img{width:100%;height:100%;object-fit:cover;object-position:50% 12%;transition:.3s}
.gal a:hover img{transform:scale(1.04)}
.vids{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:14px}
.vid{position:relative;aspect-ratio:9/16;background:#1a1a20;border-radius:2px;overflow:hidden}
.vid img{width:100%;height:100%;object-fit:cover;object-position:50% 20%;opacity:.82}
.vid .play{position:absolute;inset:0;display:grid;place-items:center;font-size:34px;color:#fff;
  text-shadow:0 2px 14px rgba(0,0,0,.7)}

/* 燈箱 */
.lb{position:fixed;inset:0;background:rgba(6,6,8,.96);z-index:100;display:none;
  place-items:center;padding:36px}
.lb[open],.lb.on{display:grid}
.lb img{max-width:100%;max-height:88vh;object-fit:contain;border-radius:2px}
.lb button{position:absolute;top:22px;right:26px;background:none;border:1px solid var(--line2);
  color:var(--ink);width:38px;height:38px;border-radius:100px;cursor:pointer;font-size:17px}

/* ── 首頁（對外報價 PPT 的網頁版）──────────────────────────────
   R6 的設計裁決都落在這一段,四條原則：
   ① 金色只給互動與選中狀態（主 CTA／active nav／hover／focus）,
      數字與重點靠字級與 --ink 的暖白突出,不靠顏色。
   ② 閱讀寬度收起來：引言與內文 42rem、段落標題 16ch,
      只有比較表與圖片可以用滿 1240px。
   ③ 13 段不再用同一種版型。框線格子只留兩段（第 4 段比較、第 11 段四大保證）,
      其餘換成編號節點、遞進節點、橫向時間軸、無框比較列。
   ④ 隔段底色從 #131317 改成 #1e1e26——舊值對主底只有 1.061 的對比度,
      交替等於沒交替（實算過）。而且不再每段交替,只給需要強調的段。
   ────────────────────────────────────────────────────────── */
.top nav a.on{color:var(--accent2)}

/* 段落骨架 */
.hsec{padding:96px 0;border-top:1px solid var(--line)}
.hsec.tint{background:var(--bg2)}
.hsec:first-of-type{border-top:0}
.eyebrow{font-size:11px;margin:0 0 16px;color:var(--accent);font-weight:500;
  display:flex;align-items:baseline;gap:.5em;flex-wrap:wrap}
.eyebrow .en{letter-spacing:.22em}
.eyebrow .zh{letter-spacing:.02em;color:var(--ink3)}
.hsec h2{font-family:var(--serif);font-size:clamp(27px,3.7vw,42px);line-height:1.22;
  margin:0 0 20px;font-weight:500;letter-spacing:.01em;max-width:17em;text-wrap:balance}
/* ⚠ 標題的行長用 em 不要用 ch。實測這個字級下「1 個中文字 = 2ch」，
   所以覆核者建議的 16ch 照字面套進中文只放得下 8 個字，9 字的標題就被斷成兩行。
   em 在中文等於一個字寬，才是這裡要的量。內文用 rem 沒問題（那是整段的字數，不是字寬）。*/
.lead{color:var(--ink2);font-size:16.5px;max-width:42rem;margin:0 0 40px;text-wrap:pretty}
.kicker{margin:40px 0 0;padding-top:22px;border-top:1px solid var(--line2);color:var(--ink);
  font-family:var(--serif);font-size:17px;max-width:46rem;line-height:1.72;text-wrap:pretty}
.fine{color:var(--ink3);font-size:12.5px;margin:20px 0 0;max-width:42rem;line-height:1.7}
.nw{white-space:nowrap}

/* ① 開場：左 55% 文案 ＋ 右 45% 直式主視覺（4:5）*/
.hhero{padding:0;position:relative;overflow:hidden;min-height:640px;display:flex;align-items:center}
.hhero .wrap{width:100%;position:relative;z-index:2}
.hhero .txt{padding:96px 0;max-width:min(55%,640px)}
.hhero h1{font-family:var(--serif);font-size:clamp(36px,5.6vw,62px);line-height:1.14;
  margin:0 0 28px;font-weight:500;letter-spacing:.005em;text-wrap:balance}
.hhero h1 em{font-style:normal;color:var(--accent2)}
.hhero .sub{max-width:32rem;color:var(--ink2);font-size:17px;margin:0 0 38px;text-wrap:pretty}
.hhero .art{position:absolute;top:0;right:0;bottom:0;width:min(46%,660px);z-index:1;
  background:#15151a;overflow:hidden}
.hhero .art img{width:100%;height:100%;object-fit:cover;object-position:50% 14%}
/* 左緣漸層,讓圖跟左欄連成一體,不是硬邊 */
.hhero .art::after{content:"";position:absolute;inset:0;pointer-events:none;
  background:linear-gradient(90deg,var(--bg) 0%,rgba(11,11,13,.72) 18%,transparent 52%)}
.btns{display:flex;flex-wrap:wrap;gap:12px}
.btn{display:inline-block;padding:14px 28px;border:1px solid var(--line2);border-radius:2px;
  font-size:14.5px;color:var(--ink2);transition:.18s}
.btn:hover,.btn:focus-visible{border-color:var(--accent);color:var(--accent2)}
.btn.p{background:var(--accent);border-color:var(--accent);color:#17130a;font-weight:600}
.btn.p:hover,.btn.p:focus-visible{background:var(--accent2);border-color:var(--accent2);color:#17130a}

/* ② 編號節點（第 2 段）：三個水平節點共用一條細線 */
.nodes{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:0;
  border-top:1px solid var(--line2)}
.node{padding:26px 30px 0 0}
.node .n{font-family:var(--serif);font-size:13px;color:var(--accent);letter-spacing:.1em;
  margin:0 0 12px;padding-top:2px}
.node .t{font-family:var(--serif);font-size:19px;margin:0 0 9px;font-weight:500;color:var(--ink)}
.node p{margin:0;color:var(--ink2);font-size:14.5px;line-height:1.74;max-width:26rem}

/* ③ 編號敘事列（第 3 段）：左側 72px 大編號 */
.numrows{border-top:1px solid var(--line)}
.numrow{display:grid;grid-template-columns:104px minmax(0,1fr);gap:28px;
  padding:30px 0;border-bottom:1px solid var(--line);align-items:start}
.numrow .n{font-family:var(--serif);font-size:64px;line-height:.9;color:var(--ink4)}
.numrow .t{font-family:var(--serif);font-size:21px;margin:6px 0 10px;font-weight:500}
.numrow p{margin:0;color:var(--ink2);font-size:15px;max-width:44rem;line-height:1.74}

/* ④ 兩欄對照（第 4 段,框線保留 ── 全頁最需要直接對照的一段）*/
.vs{display:grid;grid-template-columns:1fr 1fr;border:1px solid var(--line);border-radius:3px;
  overflow:hidden}
.vs>div{padding:34px 32px 36px;display:grid;grid-template-rows:auto auto auto 1fr;row-gap:0}
.vs>.b{border-left:1px solid var(--line);border-top:2px solid var(--accent)}
/* ⚠ 標籤的 class 是 vlb 不是 lb：.lb 是燈箱，帶 display:none，撞上去整段會消失。*/
.vs .vlb{font-size:12px;letter-spacing:.14em;color:var(--ink3);margin:0 0 16px}
.vs .amt{font-family:var(--serif);font-size:clamp(38px,4.6vw,66px);line-height:1.02;
  margin:0 0 10px;color:var(--ink);letter-spacing:-.01em}
.vs .amtn{font-size:12.5px;color:var(--ink3);margin:0 0 28px;line-height:1.65;max-width:30rem}
.vs dl{margin:0;display:grid;grid-template-columns:auto 1fr;gap:12px 18px;font-size:14.5px;
  align-content:start}
.vs dt{color:var(--ink3);white-space:nowrap}
.vs dd{margin:0;color:var(--ink2)}

/* ⑤ 分叉圖（第 5 段）：中央大數字 → 左右兩種用法 → 跨欄結論 */
.fork{max-width:960px}
.fork .trunk{position:relative;height:44px}
.fork .trunk::after{content:"";position:absolute;left:50%;top:0;width:1px;height:44px;
  background:var(--line2)}
/* 整段置中（只有這一段）:h2 本身就是那個放大的數字,不要再重複印一次 */
.hsec.mid{text-align:center}
.hsec.mid .eyebrow{justify-content:center}
.hsec.mid h2{margin-left:auto;margin-right:auto}
.hsec.mid .lead,.hsec.mid .kicker,.hsec.mid .fine{margin-left:auto;margin-right:auto}
.hsec.mid .fork{margin:0 auto}
.hsec.mid .fork .arm,.hsec.mid .fork .both{text-align:left}
.hsec.mid .kicker{border-top:0;padding-top:0}
.fork .arms{display:grid;grid-template-columns:1fr 1fr;gap:1px;background:var(--line);
  border-top:1px solid var(--line2)}
.fork .arm{background:var(--bg);padding:26px 28px 28px}
.hsec.tint .fork .arm{background:var(--bg2)}
.fork .arm .k{font-family:var(--serif);font-size:19px;margin:0 0 10px;font-weight:500}
.fork .arm p{margin:0;color:var(--ink2);font-size:14.5px;line-height:1.74}
.fork .both{border-top:1px solid var(--line2);padding:24px 28px 0;margin-top:1px}
.fork .both .k{font-family:var(--serif);font-size:17px;color:var(--accent2);margin:0 0 8px}
.fork .both p{margin:0;color:var(--ink2);font-size:14.5px;max-width:44rem;line-height:1.74}

/* ⑥ 遞進節點（第 6 段）：大字由左向右,無框 */
.steps3{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:34px}
.st3{position:relative;padding-top:24px;border-top:1px solid var(--line2)}
.st3 .t{font-family:var(--serif);font-size:clamp(20px,2.2vw,26px);margin:0 0 12px;font-weight:500;
  line-height:1.3}
.st3 p{margin:0;color:var(--ink2);font-size:14.5px;line-height:1.74}
.st3::before{content:"→";position:absolute;top:-14px;left:-24px;color:var(--ink4);font-size:15px}
.st3:first-child::before{content:none}

/* ⑦ 無框比較列（第 7 段）：左灰 → 細箭頭 → 右白 */
.cmp{border-top:1px solid var(--line2)}
.cmphead{display:grid;grid-template-columns:150px 1fr 24px 1fr;gap:20px;padding:12px 0;
  font-size:11px;letter-spacing:.14em;color:var(--ink3);border-bottom:1px solid var(--line)}
.cmphead .hl{color:var(--accent2)}
.cmprow{display:grid;grid-template-columns:150px 1fr 24px 1fr;gap:20px;padding:24px 0;
  border-bottom:1px solid var(--line);align-items:baseline}
.cmprow:last-child{border-bottom:0}
.cmprow .k{font-family:var(--serif);font-size:16.5px;color:var(--ink)}
.cmprow .was{color:var(--ink3);font-size:14.5px;line-height:1.7}
.cmprow .ar{color:var(--ink4);text-align:center;font-size:14px}
.cmprow .now{color:var(--ink);font-size:14.5px;line-height:1.7}

/* ⑧ 精選預覽（第 8 段）：圖片本身就是版型,不加裝飾框 */
.feat{display:grid;grid-template-columns:repeat(4,1fr);gap:20px;margin-bottom:38px}
.fcard{display:block;transition:.2s}
.fcard .ph{aspect-ratio:4/5;background:#15151a;overflow:hidden}
.fcard .ph img{width:100%;height:100%;object-fit:cover;object-position:50% 12%;transition:.45s}
.fcard:hover .ph img,.fcard:focus-visible .ph img{transform:scale(1.04)}
.fcard .bd{padding:15px 0 0}
.fcard .nm{font-family:var(--serif);font-size:18px;margin:0 0 4px;font-weight:500}
.fcard .zh{font-size:12px;color:var(--ink3);margin:0 0 7px}
.fcard .mt{font-size:11.5px;color:var(--ink4);letter-spacing:.06em;margin:0}
.fcard:hover .mt,.fcard:focus-visible .mt{color:var(--accent2)}

/* ⑨⑫ 橫向時間軸（第 9、12 段）：數字在線上 */
.tl{display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:32px;
  position:relative}
.tl::before{content:"";position:absolute;top:9px;left:0;right:0;height:1px;background:var(--line2)}
.tlstep{position:relative;padding-top:38px}
.tlstep::before{content:"";position:absolute;top:5px;left:0;width:9px;height:9px;border-radius:50%;
  background:var(--accent)}
.tlstep .n{position:absolute;top:0;left:22px;font-size:11px;letter-spacing:.16em;color:var(--accent);
  line-height:19px}
.tlstep .t{font-family:var(--serif);font-size:19px;margin:0 0 10px;font-weight:500}
.tlstep p{margin:0;color:var(--ink2);font-size:14.5px;line-height:1.74}
.tlstep .you{margin:16px 0 0;padding-top:12px;border-top:1px solid var(--line);
  font-size:13px;color:var(--ink3)}
.tlstep .you b{color:var(--ink);font-weight:500}

/* ⑩ 大型受眾標題（第 10 段）*/
.aud{border-top:1px solid var(--line)}
.aud>div{padding:30px 0;border-bottom:1px solid var(--line)}
.aud .k{font-family:var(--serif);font-size:clamp(21px,2.5vw,28px);margin:0 0 12px;font-weight:500;
  line-height:1.3}
.aud p{margin:0 0 0 clamp(0px,3vw,40px);color:var(--ink2);font-size:15px;max-width:44rem;
  line-height:1.74}

/* ⑪ 四大保證（第 11 段,框線保留 ── 四項要能各自掃讀）*/
.cards4{display:grid;grid-template-columns:repeat(auto-fit,minmax(272px,1fr));gap:18px}
.c4{border:1px solid var(--line);border-radius:3px;padding:26px 26px 28px;transition:.18s}
.c4:hover,.c4:focus-within{border-color:var(--accent)}
.c4 .t{font-family:var(--serif);font-size:18px;margin:0 0 10px;font-weight:500}
.c4 p{margin:0;color:var(--ink2);font-size:14.5px;line-height:1.74}

/* AI 揭露 */
.hsec .disclose{margin-top:44px;max-width:46rem;border-left:2px solid var(--accent);
  background:rgba(216,185,85,.05);padding:18px 22px;border-radius:0 3px 3px 0}
.hsec .disclose b{color:var(--accent2);font-weight:600}
.hsec .disclose p{margin:7px 0 0;color:var(--ink2);font-size:13.5px;line-height:1.7}

/* 報價頁 */
.plans{display:grid;grid-template-columns:repeat(auto-fit,minmax(272px,1fr));gap:20px}
.plan{border:1px solid var(--line);border-radius:3px;padding:32px 28px 34px;
  display:flex;flex-direction:column;transition:.18s}
.plan:hover{border-color:var(--line2)}
.plan.f{border-color:var(--accent);background:rgba(216,185,85,.05)}
.plan .tier{font-size:11px;letter-spacing:.16em;color:var(--accent);margin:0 0 14px}
.plan h3{font-family:var(--serif);font-size:23px;margin:0 0 18px;font-weight:500}
.plan .pr{font-family:var(--serif);font-size:34px;color:var(--ink);line-height:1.1;margin:0 0 24px}
.plan .pr i{font-style:normal;font-size:14px;color:var(--ink3);font-family:var(--sans)}
.plan.f .pr{color:var(--accent2)}
.plan ul{list-style:none;padding:0;margin:0}
.plan li{padding:10px 0;border-bottom:1px solid var(--line);font-size:14px;color:var(--ink2);
  line-height:1.66}
.plan li:last-child{border-bottom:0}
.qa{border-top:1px solid var(--line)}
.qa>div{border-bottom:1px solid var(--line);padding:26px 0}
.qa .q{font-family:var(--serif);font-size:18px;margin:0 0 10px;color:var(--ink)}
.qa .a{margin:0;color:var(--ink2);font-size:15px;max-width:46rem;line-height:1.74}

/* 收尾 */
.close{padding:104px 0 112px;text-align:center;border-top:1px solid var(--line)}
.close h2{font-family:var(--serif);font-size:clamp(25px,3.4vw,38px);line-height:1.4;
  margin:0 auto 36px;max-width:22em;font-weight:500;text-wrap:balance}
.close .btns{justify-content:center}

@media(max-width:900px){
  .feat{grid-template-columns:repeat(2,1fr)}
  .vs{grid-template-columns:1fr}
  .vs>.b{border-left:0;border-top:2px solid var(--accent)}
  .fork .arms{grid-template-columns:1fr}
  .cmphead{display:none}
  .cmprow{grid-template-columns:1fr;gap:8px;padding:22px 0}
  .cmprow .ar{display:none}
  .cmprow .was::before{content:"傳統：";color:var(--ink4)}
  .cmprow .now::before{content:"數位人：";color:var(--accent2)}
  .numrow{grid-template-columns:60px minmax(0,1fr);gap:18px}
  .numrow .n{font-size:38px}
  .st3::before{content:none}
  /* 時間軸轉成沿左側的垂直線 */
  .tl{grid-template-columns:1fr;gap:0}
  .tl::before{top:0;bottom:0;left:4px;right:auto;width:1px;height:auto}
  .tlstep{padding:0 0 30px 26px}
  .tlstep::before{top:6px}
  .tlstep .n{position:static;display:block;margin:0 0 8px}
  /* 首屏改成 小標＋標題 → 16:10 橫裁圖 → 引言＋按鈕 */
  .hhero{min-height:0;display:block;padding:56px 0 0}
  .hhero .wrap{display:flex;flex-direction:column}
  .hhero .txt{display:contents}
  .hhero .eyebrow{order:1}
  .hhero h1{order:2;margin-bottom:26px}
  .hhero .art{position:static;order:3;width:auto;aspect-ratio:16/10;margin:0 0 30px}
  .hhero .art::after{background:linear-gradient(180deg,transparent 60%,rgba(11,11,13,.5) 100%)}
  .hhero .art img{object-position:50% 22%}
  .hhero .sub{order:4}
  .hhero .btns{order:5;margin-bottom:60px}
  .hsec{padding:60px 0}
  .close{padding:70px 0 78px}
}
footer{padding:52px 0 70px;color:var(--ink3);font-size:12.5px}
footer p{margin:0 0 7px;max-width:720px}
@media(max-width:820px){.phead{grid-template-columns:1fr;gap:26px}.hero{padding:60px 0 40px}}
`;

// 🛑 貼到 LINE／Slack／Messenger 的預覽卡靠 og: 標籤,沒有就是一片空白。
// 這個網址的用途就是被轉傳（使用者 2026-08-31：「完全公開，可以讓人任意轉傳」），
// 所以預覽卡不是加分項。⚠ og:image 一定要絕對網址,相對路徑抓不到。
const SITE = 'https://kol-catalog-production.up.railway.app';

const layout = (title, body, { desc = '', nav = '', ogImage = '' } = {}) => `<!doctype html>
<html lang="zh-Hant">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex,nofollow">
<title>${esc(title)}</title>
${desc ? `<meta name="description" content="${esc(desc)}">` : ''}
<meta property="og:type" content="website">
<meta property="og:site_name" content="兌心科技　數位人 KOL 品牌顧問服務">
<meta property="og:locale" content="zh_TW">
<meta property="og:title" content="${esc(title)}">
${desc ? `<meta property="og:description" content="${esc(desc)}">` : ''}
${ogImage ? `<meta property="og:image" content="${esc(SITE + ogImage)}">
<meta property="og:image:width" content="1080">
<meta property="og:image:height" content="1440">
<meta name="twitter:card" content="summary_large_image">` : `<meta name="twitter:card" content="summary">`}
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Noto+Serif+TC:wght@400;500;600&family=Noto+Sans+TC:wght@300;400;500&display=swap" rel="stylesheet">
<style>${CSS}</style>
</head>
<body>
<header class="top"><div class="wrap">
  <div class="brand"><a href="/"><b>兌心</b>科技</a></div>
  <nav>
    <a href="/kols.html"${nav === 'kols' ? ' class="on"' : ''}>全部人設</a>
    <a href="/pricing.html"${nav === 'pricing' ? ' class="on"' : ''}>報價</a>
  </nav>
</div></header>
${body}
<div class="lb" id="lb" role="dialog" aria-modal="true" aria-label="放大檢視">
  <button type="button" aria-label="關閉">✕</button><img alt="">
</div>
<script>
(function(){
  var lb=document.getElementById('lb'), im=lb.querySelector('img'), last=null;
  document.addEventListener('click',function(e){
    var a=e.target.closest('[data-lb]'); if(a){e.preventDefault();last=a;
      im.src=a.getAttribute('data-lb'); im.alt=a.getAttribute('data-alt')||'';
      lb.classList.add('on'); lb.querySelector('button').focus(); return;}
    if(e.target===lb||e.target.closest('#lb button')){close();}
  });
  document.addEventListener('keydown',function(e){if(e.key==='Escape'&&lb.classList.contains('on'))close();});
  function close(){lb.classList.remove('on'); im.src=''; if(last)last.focus();}
})();
</script>
</body></html>`;

// ── 型錄牆（原本的首頁,使用者 2026-09-03 裁決搬到 /kols.html,內容不重做）──
const people = cat.personas.map(p => ({ ...p, a: assetsOf(p.id), mk: market(p.location) }));
const totalImages = people.reduce((a, p) => a + p.media.image_count, 0);
const totalVideos = people.reduce((a, p) => a + p.media.video_count, 0);

const cats = [...new Set(people.map(p => catLabel(p.category)))].sort();
const mks = [...new Set(people.map(p => p.mk))].sort();

const card = p => `
<a class="card" href="/p/${esc(p.id)}.html">
  <div class="ph">${p.a.hero ? `<img src="${p.a.hero}" alt="${esc(p.name)}" loading="lazy" width="1080" height="1440">` : ''}</div>
  <div class="body">
    <h3 class="nm">${esc(p.name)}</h3>
    <p class="zh">${esc([p.name_zh, p.age ? p.age + ' 歲' : null, p.mk].filter(Boolean).join(' · '))}</p>
    <p class="tl">${esc(p.tagline || '')}</p>
    <div class="tags">
      <span class="tag k">${esc(catLabel(p.category))}</span>
      <span class="tag">${p.media.image_count} 張圖</span>
      ${p.media.video_count ? `<span class="tag">${p.media.video_count} 支影片</span>` : ''}
    </div>
  </div>
</a>`;

const kolsPage = layout('虛擬 KOL 型錄 — 兌心科技', `
<div class="hero"><div class="wrap">
  <h1>虛擬 <em>KOL</em> 型錄</h1>
  <p class="lede">${people.length} 位可合作的虛擬 KOL。每一位都有完整的人物設定、內容主題與視覺調性，
  並且已經產出可用的圖像與影片素材。</p>
  <div class="disclose">
    <b>這些是 AI 生成的虛擬人物。</b>
    <p>不是真人。所有肖像與影片皆由本團隊自行生成，角色設定、語氣與內容規範亦為原創。
    虛擬 KOL 沒有檔期衝突、不會有個人爭議，且能同時經營多個平台與多語市場。</p>
  </div>
</div></div>

<div class="filters"><div class="wrap">
  <div class="frow"><span>領域</span>
    <button class="chip" aria-pressed="true" data-f="cat" data-v="">全部</button>
    ${cats.map(c => `<button class="chip" aria-pressed="false" data-f="cat" data-v="${esc(c)}">${esc(c)}</button>`).join('')}
  </div>
  <div class="frow"><span>市場</span>
    <button class="chip" aria-pressed="true" data-f="mk" data-v="">全部</button>
    ${mks.map(m => `<button class="chip" aria-pressed="false" data-f="mk" data-v="${esc(m)}">${esc(m)}</button>`).join('')}
  </div>
  <div class="frow"><span>素材</span>
    <button class="chip" aria-pressed="true" data-f="med" data-v="">全部</button>
    <button class="chip" aria-pressed="false" data-f="med" data-v="video">有影片素材</button>
  </div>
  <div class="frow"><span>排序</span>
    <button class="chip" aria-pressed="true" data-s="feat">推薦</button>
    <button class="chip" aria-pressed="false" data-s="material">素材最多</button>
    <button class="chip" aria-pressed="false" data-s="age">年齡由小到大</button>
    <button class="chip" aria-pressed="false" data-s="name">名字</button>
  </div>
  <p class="count" id="count">顯示 ${people.length} 位</p>
</div></div>

<div class="wrap"><div class="grid" id="grid">
${people.map((p, i) => `<div class="cell" data-cat="${esc(catLabel(p.category))}" data-mk="${esc(p.mk)}" data-video="${p.media.video_count ? 'video' : ''}" data-feat="${i}" data-material="${p.media.image_count * 10 + p.media.video_count}" data-age="${p.age || 99}" data-name="${esc(p.name)}">${card(p)}</div>`).join('')}
</div></div>

<div class="wrap" id="about"><section class="sec">
  <h2>關於這份型錄</h2>
  <div class="two">
    <div><p class="lede prose">這份型錄只收錄<b>素材已經到位</b>的人設。還在建置中的角色不列入，
    所以你在這裡看到的每一位，都是現在就能討論合作的。</p></div>
    <div><p class="prose">每一位人設的頁面包含：角色設定與語氣、內容主題與比重、合作邊界、
    設定文件的深度，以及實際產出的圖像與影片素材。</p></div>
  </div>
</section></div>

<footer><div class="wrap">
  <p>本型錄所有人物均為 AI 生成的虛擬角色，非真實人物。</p>
  <p>素材與設定為本團隊原創。頁面不進入搜尋引擎索引。</p>
</div></footer>

<script>
(function(){
  var st={cat:'',mk:'',med:''}, sort='feat';
  var grid=document.getElementById('grid');
  var cells=[].slice.call(grid.querySelectorAll('.cell'));

  function apply(){
    var n=0;
    cells.forEach(function(c){
      var ok=(!st.cat||c.dataset.cat===st.cat)&&(!st.mk||c.dataset.mk===st.mk)&&(!st.med||c.dataset.video===st.med);
      c.hidden=!ok; if(ok)n++;
    });
    document.getElementById('count').textContent='顯示 '+n+' 位';

    var sorted=cells.slice().sort(function(a,b){
      if(sort==='feat')     return (+a.dataset.feat)-(+b.dataset.feat);
      if(sort==='material') return (+b.dataset.material)-(+a.dataset.material);
      if(sort==='age')      return (+a.dataset.age)-(+b.dataset.age);
      return a.dataset.name.localeCompare(b.dataset.name,'zh-Hant');
    });
    sorted.forEach(function(c){ grid.appendChild(c); });
  }

  document.querySelectorAll('.chip[data-f]').forEach(function(b){
    b.addEventListener('click',function(){
      var f=b.dataset.f; st[f]=b.dataset.v;
      document.querySelectorAll('.chip[data-f="'+f+'"]').forEach(function(o){
        o.setAttribute('aria-pressed', String(o===b)); });
      apply();
    });
  });
  document.querySelectorAll('.chip[data-s]').forEach(function(b){
    b.addEventListener('click',function(){
      sort=b.dataset.s;
      document.querySelectorAll('.chip[data-s]').forEach(function(o){
        o.setAttribute('aria-pressed', String(o===b)); });
      apply();
    });
  });
  apply();
})();
</script>
`, { desc: '可合作的虛擬 KOL 型錄，含完整角色設定與可用素材。', nav: 'kols',
     ogImage: (people[0] && people[0].a.hero) || '' });

// ── 人設頁 ──────────────────────────────────────────────────────────
const personPage = p => {
  const facts = [
    ['年齡', p.age ? p.age + ' 歲' : null],
    ['市場', p.mk],
    ['族裔', p.ethnicity],
    ['語言', p.languages.length ? p.languages.map(langShort).slice(0, 3).join('・') : null],
    ['領域', catLabel(p.category)],
  ].filter(x => x[1]);

  return layout(`${p.name} — 虛擬 KOL 型錄`, `
<div class="wrap">
  <p class="pback"><a href="/kols.html">← 回到全部人設</a></p>
  <div class="phead">
    <div class="pimg">${p.a.hero ? `<img src="${p.a.hero}" alt="${esc(p.name)}" width="1080" height="1440">` : ''}</div>
    <div>
      <h1>${esc(p.name)}</h1>
      <p class="zh">${esc(p.name_zh || '')}</p>
      <p class="tl">${esc(p.tagline || '')}</p>
      <div class="facts">${facts.map(([k, v]) => `<div class="fact"><span>${esc(k)}</span><b>${esc(v)}</b></div>`).join('')}</div>
      ${p.archetype ? `<p class="prose">${esc(p.archetype)}</p>` : ''}
    </div>
  </div>

  ${p.pillars.length ? `<section class="sec"><h2>內容主題</h2>
    <ul class="plain">${p.pillars.map(x => `<li><b>${esc(x.name)}</b>${x.weight ? `<i>${esc(x.weight)}</i>` : ''}</li>`).join('')}</ul>
  </section>` : ''}

  ${(p.personality.length || p.voice_tone || p.aesthetic_mood) ? `<section class="sec"><h2>性格・語氣・視覺調性</h2>
    ${p.personality.length ? `<p class="lbl">性格</p><ul class="plain">${p.personality.slice(0, 8).map(t => `<li>${esc(t)}</li>`).join('')}</ul>` : ''}
    <div class="two" style="margin-top:26px">
      ${p.voice_tone ? `<div><p class="lbl">語氣</p><p class="prose">${esc(p.voice_tone)}</p></div>` : ''}
      ${p.aesthetic_mood ? `<div><p class="lbl">視覺調性</p><p class="prose">${esc(p.aesthetic_mood)}</p></div>` : ''}
    </div>
  </section>` : ''}

  ${p.a.gallery.length ? `<section class="sec"><h2>圖像素材</h2>
    <div class="gal">${p.a.gallery.map((g, i) => `<a href="${g.web}" data-lb="${g.web}" data-alt="${esc(p.name)} 素材 ${i + 1}">
      <img src="${g.thumb}" alt="${esc(p.name)} 素材 ${i + 1}" loading="lazy" width="400" height="533"></a>`).join('')}</div>
  </section>` : ''}

  ${p.a.videos.length ? `<section class="sec"><h2>影片素材</h2>
    <div class="vids">${p.a.videos.map((v, i) => `<div class="vid">
      <img src="${v.poster}" alt="${esc(p.name)} 影片 ${i + 1} 首幀" loading="lazy" width="720" height="1280">
      <span class="play" aria-hidden="true">▶</span></div>`).join('')}</div>
    <p class="prose" style="margin-top:14px;font-size:13px">影片可於洽談時提供完整檔案。</p>
  </section>` : ''}

  ${p.fit.length ? `<section class="sec"><h2>適合的合作方向</h2>
    <ul class="plain">${p.fit.slice(0, 8).map(x => `<li>${esc(x)}</li>`).join('')}</ul>
    <p class="prose" style="margin-top:16px;font-size:13.5px">
      以上是依她現有人設最自然的方向。<b>虛擬 KOL 的設定可以依品牌需求調整</b>——
      選定了外形之後，內容主題與語氣都能配合合作內容重新設定。</p>
  </section>` : ''}
</div>
<footer><div class="wrap">
  <p>${esc(p.name)} 為 AI 生成的虛擬角色，非真實人物。</p>
  <p><a href="/kols.html">← 回到全部人設</a></p>
</div></footer>
`, { desc: p.tagline || '', nav: 'kols', ogImage: p.a.hero || '' });
};


// ── 首頁：對外報價 PPT 的網頁版 ──────────────────────────────────
// 使用者 2026-09-03：「我現在就是想把對外報價的 PPT 轉成網頁版的 dashboard。」
// 段落與 PPT 頁次的對應表在覆核包 §12.2（13 段）。
// 🛑 PPT 的 p15 方案報價與 p16 常見問題不在首頁，搬去 /pricing.html。
// 🛑 文字全部來自 pitch.json，這裡只排版，不改一個字（業務承諾）。
// ⚠ R6（2026-09-03）之後每一段的版型都不一樣了，改法逐段記在 §14／§12.8。
const P = pitch;

// 第 8 段的精選預覽、第 1 段的主視覺。
// 🛑 都是使用者指定的，程式不自己挑（§0.4「哪一張圖」是她的；§12.2 的 R5 規定）。
const featured = (copy.featured || [])
  .map(id => people.find(p => p.id === id))
  .filter(Boolean);

// 🛑 寫成程式擋住，不要只寫成規則（這個 repo 的教訓：文件會再犯，程式不會）。
// R5 否決了「第 8 段只放一個文字連結」，理由是客戶點擊之前就要先看到真的有人設有素材。
// 所以這一段少於 3 位就不是那個規劃，直接不要產出。
if (featured.length < 3) {
  console.error(`🛑 首頁精選預覽只湊到 ${featured.length} 位（規劃要求 3〜4 位）。`);
  console.error(`   copy.json 的 \`featured\` = ${JSON.stringify(copy.featured || [])}`);
  console.error('   → 那幾個 id 要在 catalog.json 的人設裡找得到。改好再跑。');
  process.exit(2);
}
if (featured.some(p => !p.a.hero)) {
  console.error('🛑 精選預覽有人設沒有封面圖 → ' +
    featured.filter(p => !p.a.hero).map(p => p.id).join('、'));
  process.exit(2);
}

const heroPerson = people.find(p => p.id === copy.hero_persona);
if (!heroPerson || !heroPerson.a.hero) {
  console.error(`🛑 首屏主視覺指定的人設找不到或沒有封面圖：${copy.hero_persona}`);
  console.error('   → 改 copy.json 的 `hero_persona`（要是 catalog.json 裡有封面的人設 id）。');
  process.exit(2);
}

// 中英混排的小標：英文要字距、中文不要，不然「什 麼 是」會被拉散（R6 Q24 第 3 點）。
const eyebrow = s => {
  // ⚠ 不能靠「｜」來分中英——`hero.eyebrow` 是「方案與報價提案 · 2026」，沒有分隔符號，
  //   整串套上英文字距會被拉成「方 案 與 報 價」。所以直接按字元切 ASCII 段與中文段。
  const parts = String(s).match(/[^\u2e80-\u9fff\uff00-\uffef]+|[\u2e80-\u9fff\uff00-\uffef]+/g) || [];
  return `<p class="eyebrow">` + parts.map(t =>
    /[\u2e80-\u9fff\uff00-\uffef]/.test(t)
      ? `<span class="zh">${esc(t.trim())}</span>`
      : `<span class="en">${esc(t.trim())}</span>`
  ).filter(x => !/>\s*<\/span>$/.test(x)).join('') + `</p>`;
};

// 不可拆的詞包成 nowrap，手機才不會留下單字孤行（R6 Q21 第 3 點；390px 實測過 7 處）。
const NOWRAP = ['NT$2,000,000', 'NT$110,000', 'NT$65,000', 'NT$35,000', 'NT$3,000', 'NT$200',
  '3 次確認', '2 小時', '32.5 萬', '6.5 萬', '30 天', '6 平台', '6 大平台', 'B2C',
  '找出缺口', '免費品牌健檢', '3 週'];
const nw = s => {
  let o = esc(s);
  for (const t of NOWRAP) o = o.split(esc(t)).join(`<span class="nw">${esc(t)}</span>`);
  return o;
};

const pad2 = i => String(i + 1).padStart(2, '0');

const homePage = layout('虛擬 KOL 品牌顧問服務 — 兌心科技', `
<div class="hhero"><div class="wrap">
  <div class="txt">
    ${eyebrow(P.hero.eyebrow)}
    <h1>${P.hero.title_lines.map((l, i) => i === P.hero.title_lines.length - 1
        ? `<em>${esc(l)}</em>` : esc(l)).join('<br>')}</h1>
    <p class="sub">${nw(P.hero.sub)}</p>
    <div class="btns">${P.hero.cta.map(c =>
      `<a class="btn${c.primary ? ' p' : ''}" href="${esc(c.href)}">${esc(c.label)}</a>`).join('')}</div>
  </div>
  <div class="art">
    <img src="${heroPerson.a.hero}" alt="虛擬 KOL 形象範例" width="1080" height="1350">
  </div>
</div></div>

<section class="hsec"><div class="wrap">
  ${eyebrow(P.what.eyebrow)}
  <h2>${esc(P.what.title)}</h2>
  <p class="lead">${nw(P.what.lead)}</p>
  <div class="nodes">${P.what.pillars.map((x, i) => `<div class="node">
    <p class="n">${pad2(i)}</p><p class="t">${esc(x.k)}</p><p>${nw(x.v)}</p></div>`).join('')}</div>
  <p class="kicker">${nw(P.what.note)}</p>
  <div class="disclose">
    <b>這些 KOL 是 AI 生成的虛擬人物。</b>
    <p>不是真人。所有肖像、聲音與影片皆由本團隊自行生成，人設、語氣與內容規範亦為原創；
    發布時依各平台規範標示 AI 內容。虛擬 KOL 沒有檔期衝突、不會有個人爭議，
    且能同時經營多個平台與多語市場。</p>
  </div>
</div></section>

<section class="hsec tint"><div class="wrap">
  ${eyebrow(P.value.eyebrow)}
  <h2>${esc(P.value.title)}</h2>
  <div class="numrows">${P.value.cards.map((c, i) => `<div class="numrow">
    <div class="n">${pad2(i)}</div>
    <div><p class="t">${esc(c.h)}</p><p>${nw(c.p)}</p></div></div>`).join('')}</div>
</div></section>

<section class="hsec"><div class="wrap">
  ${eyebrow(P.why_public.eyebrow)}
  <h2>${esc(P.why_public.title)}</h2>
  <p class="lead">${nw(P.why_public.lead)}</p>
  <div class="vs">
    ${[['a', P.why_public.compare.a], ['b', P.why_public.compare.b]].map(([cls, d]) => `<div class="${cls}">
      <p class="vlb">${esc(d.label)}</p>
      <p class="amt">${nw(d.amount)}</p>
      <p class="amtn">${nw(d.amount_note)}</p>
      <dl>${d.rows.map(([k, v]) => `<dt>${esc(k)}</dt><dd>${nw(v)}</dd>`).join('')}</dl>
    </div>`).join('')}
  </div>
  <p class="kicker">${nw(P.why_public.kicker)}</p>
  <p class="fine">${nw(P.why_public.disclaimer)}</p>
</div></section>

<section class="hsec mid"><div class="wrap">
  ${eyebrow(P.budget.eyebrow)}
  <h2>${nw(P.budget.title)}</h2>
  <div class="fork">
    <div class="trunk" aria-hidden="true"></div>
    <div class="arms">${P.budget.rows.slice(0, 2).map(r => `<div class="arm">
      <p class="k">${esc(r.k)}</p><p>${nw(r.v)}</p></div>`).join('')}</div>
    ${P.budget.rows[2] ? `<div class="both">
      <p class="k">${esc(P.budget.rows[2].k)}</p><p>${nw(P.budget.rows[2].v)}</p></div>` : ''}
  </div>
  <p class="kicker">${nw(P.budget.note)}</p>
  <p class="fine">${nw(P.budget.footnote)}</p>
</div></section>

<section class="hsec tint"><div class="wrap">
  ${eyebrow(P.legacy.eyebrow)}
  <h2>${esc(P.legacy.title)}</h2>
  <p class="lead">${nw(P.legacy.lead)}</p>
  <div class="steps3">${P.legacy.rows.map(([k, v]) => `<div class="st3">
    <p class="t">${esc(k)}</p><p>${nw(v)}</p></div>`).join('')}</div>
</div></section>

<section class="hsec"><div class="wrap">
  ${eyebrow(P.breakthrough.eyebrow)}
  <h2>${esc(P.breakthrough.title)}</h2>
  <div class="cmp">
    <div class="cmphead"><div></div><div>傳統製作的限制</div><div></div><div class="hl">數位人 KOL</div></div>
    ${P.breakthrough.rows.map(([k, was, now]) => `<div class="cmprow">
      <div class="k">${esc(k)}</div>
      <div class="was">${nw(was)}</div>
      <div class="ar" aria-hidden="true">→</div>
      <div class="now">${nw(now)}</div></div>`).join('')}
  </div>
  <p class="fine">${nw(P.breakthrough.note)}</p>
</div></section>

<section class="hsec tint"><div class="wrap">
  ${eyebrow('CATALOGUE｜看實際的人設與素材')}
  <h2>不必想像，直接看</h2>
  <p class="lead">每一位都有完整的人物設定、內容主題與視覺調性，並且已經產出可用的圖像與影片素材。
  點進任何一位，都能直接在網頁上看完他全部的素材。</p>
  <div class="feat">${featured.map(p => `<a class="fcard" href="/p/${esc(p.id)}.html">
    <div class="ph"><img src="${p.a.hero}" alt="${esc(p.name)}" loading="lazy" width="1080" height="1350"></div>
    <div class="bd">
      <p class="nm">${esc(p.name)}</p>
      <p class="zh">${esc([p.name_zh, p.mk].filter(Boolean).join(' · '))}</p>
      <p class="mt">${esc(catLabel(p.category))}</p>
    </div></a>`).join('')}</div>
  <div class="btns"><a class="btn p" href="/kols.html">看全部人設 →</a></div>
</div></section>

<section class="hsec"><div class="wrap">
  ${eyebrow(P.engine.eyebrow)}
  <h2>${esc(P.engine.title)}</h2>
  <p class="lead">${nw(P.engine.lead)}</p>
  <div class="tl">${P.engine.steps.map(x => `<div class="tlstep">
    <p class="n">${esc(x.n)}</p><p class="t">${esc(x.t)}</p><p>${nw(x.p)}</p></div>`).join('')}</div>
</div></section>

<section class="hsec"><div class="wrap">
  ${eyebrow(P.fit.eyebrow)}
  <h2>${nw(P.fit.title)}</h2>
  <p class="lead">${nw(P.fit.lead)}</p>
  <div class="aud">${P.fit.rows.map(([k, v]) => `<div>
    <p class="k">${esc(k)}</p><p>${nw(v)}</p></div>`).join('')}</div>
</div></section>

<section class="hsec tint"><div class="wrap">
  ${eyebrow(P.quality.eyebrow)}
  <h2>${esc(P.quality.title)}</h2>
  <div class="cards4">${P.quality.cards.map(([h, p]) => `<div class="c4">
    <p class="t">${esc(h)}</p><p>${nw(p)}</p></div>`).join('')}</div>
  <p class="kicker">${nw(P.quality.kicker)}</p>
</div></section>

<section class="hsec"><div class="wrap">
  ${eyebrow(P.onboarding.eyebrow)}
  <h2>${nw(P.onboarding.title)}</h2>
  <div class="tl">${P.onboarding.steps.map(x => `<div class="tlstep">
    <p class="n">${esc(x.n)}</p><p class="t">${esc(x.t)}</p><p>${nw(x.p)}</p>
    ${x.you ? `<p class="you">您要做的：<b>${nw(x.you)}</b></p>` : ''}</div>`).join('')}</div>
  <p class="kicker">${nw(P.onboarding.kicker)}</p>
</div></section>

<div class="close"><div class="wrap">
  <h2>${nw(P.closing.title)}</h2>
  <div class="btns">
    <a class="btn p" href="${esc(P.closing.cta.href)}">${esc(P.closing.cta.label)}</a>
    <a class="btn" href="/pricing.html">方案與報價</a>
  </div>
</div></div>

<footer><div class="wrap">
  <p>${esc(P.brand.name)}　${esc(P.brand.en)}　${esc(P.brand.line)}</p>
  <p>本站所有 KOL 均為 AI 生成的虛擬角色，非真實人物；素材與設定為本團隊原創。</p>
  <p>頁面不進入搜尋引擎索引。</p>
</div></footer>
`, { desc: P.hero.sub, nav: '', ogImage: heroPerson.a.hero });

// ── 報價頁（PPT p15 方案報價 ＋ p16 常見問題）────────────────────
// 🛑 價格與方案內容一個字都不改（覆核包 §12.6）。
const pricingPage = layout('方案與報價 — 兌心科技', `
<section class="hsec"><div class="wrap">
  ${eyebrow(P.plans.eyebrow)}
  <h2>${esc(P.plans.title)}</h2>
  <div class="plans">${P.plans.items.map(x => `<div class="plan${x.featured ? ' f' : ''}">
    <p class="tier">${esc(x.tier)}</p>
    <h3>${esc(x.name)}</h3>
    <p class="pr">${nw(x.price)}<i>${esc(x.unit)}</i></p>
    <ul>${x.bullets.map(b => `<li>${nw(b)}</li>`).join('')}</ul>
  </div>`).join('')}</div>
  <p class="kicker">${nw(P.quality.kicker)}</p>
</div></section>

<section class="hsec tint"><div class="wrap">
  ${eyebrow(P.faq.eyebrow)}
  <h2>${esc(P.faq.title)}</h2>
  <div class="qa">${P.faq.items.map(([q, a]) => `<div>
    <p class="q">${nw(q)}</p><p class="a">${nw(a)}</p></div>`).join('')}</div>
</div></section>

<div class="close"><div class="wrap">
  <h2>${nw(P.closing.title)}</h2>
  <div class="btns">
    <a class="btn p" href="${esc(P.closing.cta.href)}">${esc(P.closing.cta.label)}</a>
    <a class="btn" href="/">回首頁</a>
  </div>
</div></div>

<footer><div class="wrap">
  <p>${esc(P.brand.name)}　${esc(P.brand.en)}　${esc(P.brand.line)}</p>
  <p>本站所有 KOL 均為 AI 生成的虛擬角色，非真實人物。</p>
</div></footer>
`, { desc: '虛擬 KOL 經營的方案與報價。', nav: 'pricing', ogImage: heroPerson.a.hero });

// ── 寫檔 ────────────────────────────────────────────────────────────
// 🛑 pick.html 是另一支程式（build_picker.mjs）產的,不要被這裡的清空掃掉。
// 踩過的形狀：跑完 npm run site 之後挑選後台就從部署裡消失,而它不進 git 的話就回不來了。
// 現在它進 git 了,但清空還是會讓「這次部署」少一頁,所以先備份再放回去。
let pickHtml = null;
try { pickHtml = fs.readFileSync(path.join(PUB, 'pick.html')); } catch {}

fs.rmSync(PUB, { recursive: true, force: true });
fs.mkdirSync(path.join(PUB, 'p'), { recursive: true });
if (pickHtml) fs.writeFileSync(path.join(PUB, 'pick.html'), pickHtml);
fs.writeFileSync(path.join(PUB, 'index.html'), homePage);
fs.writeFileSync(path.join(PUB, 'kols.html'), kolsPage);
fs.writeFileSync(path.join(PUB, 'pricing.html'), pricingPage);
for (const p of people) fs.writeFileSync(path.join(PUB, 'p', `${p.id}.html`), personPage(p));
fs.writeFileSync(path.join(PUB, 'robots.txt'), 'User-agent: *\nDisallow: /\n');

console.log(`產生 ${people.length + 3} 頁 → ${PUB}`);
for (const f of ['index.html', 'kols.html', 'pricing.html']) {
  console.log(`  ${f.padEnd(13)} ${(fs.statSync(path.join(PUB, f)).size / 1024).toFixed(0)} KB`);
}
console.log(`  p/*.html      ${people.length} 頁`);
console.log(`  首頁精選預覽   ${featured.map(p => p.name).join('、')}`);
