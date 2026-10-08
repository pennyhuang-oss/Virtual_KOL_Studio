// 看配對索引的數字（診斷用）。索引本身由 match_data.mjs 建,型錄站是直接 import 那支,
// 不讀這裡寫出來的檔案——所以這支只是「印出來看」＋留一份 JSON 方便手動查。
import fs from 'node:fs';
import { buildIndex, COLS, cell } from './match_data.mjs';

const out = buildIndex();
const rich = out.filter(o => o.rich), thin = out.filter(o => !o.rich);
const avg = a => (a.reduce((x, o) => x + o.kw.length, 0) / a.length).toFixed(1);
console.log(`人設 ${out.length} 位｜有 topic_affinity 的 ${rich.length} 位`);
console.log(`關鍵詞:平均每位 ${avg(out)} 個`);
console.log(`  有 affinity 的平均 ${avg(rich)} 個`);
console.log(`  只有型錄欄位的 ${thin.length} 位平均 ${avg(thin)} 個｜最少 ${Math.min(...thin.map(o => o.kw.length))}`);
console.log(`題目連結點 ${out.reduce((a, o) => a + o.hooks.length, 0)} 個｜block 紅線詞 ${out.reduce((a, o) => a + o.block.length, 0)} 個`);

// 雷達:整列都空的人設會在人設頁上出現一張全「—」的圖,要抓得出來。
const rows = out.map(o => ({ o, cells: COLS.map(c => cell(o, c)) }));
const empty = rows.filter(r => r.cells.every(c => !c.v)).map(r => r.o.zh || r.o.name);
console.log(`雷達 ${rows.length} × ${COLS.length}｜有值 ${rows.reduce((a, r) => a + r.cells.filter(c => c.v > 0).length, 0)} 格`
  + `｜整列都空 ${empty.length ? empty.join('、') : '無 ✅'}`);
console.log('人設'.padEnd(9) + COLS.map(c => c.k.slice(0, 4).padStart(6)).join(''));
const tot = r => r.cells.reduce((a, c) => a + c.v, 0);
rows.slice().sort((a, b) => tot(b) - tot(a)).slice(0, 8).forEach(r =>
  console.log((r.o.zh || r.o.name).padEnd(9) + r.cells.map(c => String(c.v || '·').padStart(6)).join('')));

const OUT = process.env.MATCH_OUT || '/home/user/Virtual_KOL_Studio/catalog/build';
fs.mkdirSync(OUT, { recursive: true });
fs.writeFileSync(OUT + '/match_index.json', JSON.stringify(out));
console.log('索引也寫了一份 → ' + OUT + '/match_index.json');
