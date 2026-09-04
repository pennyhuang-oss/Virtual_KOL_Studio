#!/usr/bin/env node
/**
 * 零依賴靜態伺服器。沿用 showgame-kol/railway 已驗證可部署的模式。
 *
 * 🛑 Railway 的兩個坑（那個 repo 實際踩過並寫下來的）：
 *   1. Railway 會自己注入 PORT=8080。**不要自己加 PORT 環境變數**，
 *      而且 Settings → Networking 網址底下的 → Port 要設 8080，兩邊對不上會一路 502。
 *      診斷第一步是看 Deploy Logs 裡下面那行 listening on ____，不要猜埠號。
 *   2. Root Directory 設 /catalog、Watch Paths 設 catalog/**。換過就要一起改。
 *
 * 存取控制分兩層：
 *   ・**型錄本身完全公開、不設密碼**（使用者 2026-08-31 裁決）。
 *   ・🛑 **素材挑選後台（`/pick.html` 與 `/assets/_pick/`）不是公開的。**
 *     那一頁列出全部 657 張圖與 170 支影片,**包含刻意沒放上型錄的**,
 *     使用者 2026-09-04：「我不想要讓外人也可以看。」
 *     做法：要帶 `?k=<PICK_KEY>` 才進得去,進去後發一個 session cookie,
 *     後續 `_pick` 素材靠那個 cookie 放行。
 *     **`PICK_KEY` 設在 Railway 的環境變數,不進 repo**——這個 repo 是公開的
 *     （2026-09-04 實測：不帶授權抓得到檔案）,所以密鑰放進 repo 等於沒有密鑰。
 *     **沒設 PICK_KEY 就整個關掉**（回 404），預設是安全的那一邊。
 * 兩者都帶 X-Robots-Tag: noindex 讓它不進搜尋引擎。
 */
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';

const ROOT = path.join(import.meta.dirname, 'public');
const ASSETS = path.join(import.meta.dirname, 'assets');
const PORT = process.env.PORT || 3000;
const PICK_KEY = process.env.PICK_KEY || '';
const COOKIE = 'kolcat_pick';

const TYPES = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp',
  '.mp4': 'video/mp4', '.webm': 'video/webm', '.txt': 'text/plain; charset=utf-8',
  '.svg': 'image/svg+xml',
};

// 挑選後台的門。回傳 'ok'｜'setcookie'｜'deny'
function pickGate(req, pathname, query) {
  const isPick = pathname === '/pick.html' || pathname.startsWith('/assets/_pick/');
  if (!isPick) return 'ok';
  if (!PICK_KEY) return 'deny';                       // 沒設密鑰 → 整個關掉
  if (query && query.k === PICK_KEY) return 'setcookie';
  const c = String(req.headers.cookie || '');
  // 逐個 cookie 比對,不要用 includes()——那樣別的 cookie 的值裡剛好含這串就會過
  const hit = c.split(';').some(kv => {
    const i = kv.indexOf('=');
    return i > 0 && kv.slice(0, i).trim() === COOKIE && kv.slice(i + 1).trim() === PICK_KEY;
  });
  return hit ? 'ok' : 'deny';
}

// 解析後的路徑一定要還在允許的根目錄底下，否則 403（路徑穿越）
function resolveSafe(base, rel) {
  const p = path.normalize(path.join(base, rel));
  return p.startsWith(base) ? p : null;
}

const server = http.createServer((req, res) => {
  let pathname, query;
  try {
    const u = url.parse(req.url, true);
    pathname = decodeURIComponent(u.pathname);
    query = u.query;
  } catch { res.writeHead(400); return res.end('bad request'); }

  const gate = pickGate(req, pathname, query);
  if (gate === 'deny') {
    // 刻意回 404 不回 401：不要讓外人知道這個網址存在
    res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8', 'X-Robots-Tag': 'noindex, nofollow' });
    return res.end('<meta charset="utf-8"><p style="font:16px system-ui;padding:40px">找不到這一頁。<a href="/">回到型錄</a></p>');
  }
  const setCookie = gate === 'setcookie'
    ? [`${COOKIE}=${PICK_KEY}; Path=/; HttpOnly; SameSite=Lax; Secure; Max-Age=604800`]
    : null;

  let base = ROOT, rel = pathname;
  if (pathname.startsWith('/assets/')) { base = ASSETS; rel = pathname.slice('/assets'.length); }

  let file = resolveSafe(base, rel);
  if (!file) { res.writeHead(403); return res.end('forbidden'); }

  // 目錄 → index.html；無副檔名 → 試 .html
  try {
    if (fs.existsSync(file) && fs.statSync(file).isDirectory()) file = path.join(file, 'index.html');
    else if (!fs.existsSync(file) && !path.extname(file) && fs.existsSync(file + '.html')) file += '.html';
  } catch {}

  if (!fs.existsSync(file) || !fs.statSync(file).isFile()) {
    res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8' });
    return res.end('<meta charset="utf-8"><p style="font:16px system-ui;padding:40px">找不到這一頁。<a href="/">回到型錄</a></p>');
  }

  const ext = path.extname(file).toLowerCase();
  const isAsset = base === ASSETS;
  const isPick = pathname === '/pick.html' || pathname.startsWith('/assets/_pick/');
  const head = {
    'Content-Type': TYPES[ext] || 'application/octet-stream',
    'X-Robots-Tag': 'noindex, nofollow',
    'X-Content-Type-Options': 'nosniff',
    // 素材是內容雜湊等級的靜態檔，可以長快取；HTML 每次重新驗證
    // ⚠ 挑選後台的東西一律 private，不要讓中間的快取層留一份給沒帶 cookie 的人
    'Cache-Control': isPick ? 'private, max-age=0, must-revalidate'
      : (isAsset ? 'public, max-age=604800' : 'public, max-age=0, must-revalidate'),
  };
  if (setCookie) head['Set-Cookie'] = setCookie;
  res.writeHead(200, head);
  fs.createReadStream(file).pipe(res);
});

server.listen(PORT, () => console.log(`listening on ${PORT}`));
