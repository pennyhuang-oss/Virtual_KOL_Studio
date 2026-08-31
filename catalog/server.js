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
 * 存取控制：使用者 2026-08-31 裁決「完全公開，不設密碼」，
 * 所以這裡沒有 Basic Auth（另外兩個 Railway 站有，那是因為它們放的是內部判斷）。
 * 仍然帶 X-Robots-Tag: noindex 讓它不進搜尋引擎。
 */
import http from 'node:http';
import fs from 'node:fs';
import path from 'node:path';
import url from 'node:url';

const ROOT = path.join(import.meta.dirname, 'public');
const ASSETS = path.join(import.meta.dirname, 'assets');
const PORT = process.env.PORT || 3000;

const TYPES = {
  '.html': 'text/html; charset=utf-8', '.css': 'text/css; charset=utf-8',
  '.js': 'text/javascript; charset=utf-8', '.json': 'application/json; charset=utf-8',
  '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg', '.png': 'image/png', '.webp': 'image/webp',
  '.mp4': 'video/mp4', '.txt': 'text/plain; charset=utf-8', '.svg': 'image/svg+xml',
};

// 解析後的路徑一定要還在允許的根目錄底下，否則 403（路徑穿越）
function resolveSafe(base, rel) {
  const p = path.normalize(path.join(base, rel));
  return p.startsWith(base) ? p : null;
}

const server = http.createServer((req, res) => {
  let pathname;
  try { pathname = decodeURIComponent(url.parse(req.url).pathname); }
  catch { res.writeHead(400); return res.end('bad request'); }

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
  res.writeHead(200, {
    'Content-Type': TYPES[ext] || 'application/octet-stream',
    'X-Robots-Tag': 'noindex, nofollow',
    'X-Content-Type-Options': 'nosniff',
    // 素材是內容雜湊等級的靜態檔，可以長快取；HTML 每次重新驗證
    'Cache-Control': isAsset ? 'public, max-age=604800' : 'public, max-age=0, must-revalidate',
  });
  fs.createReadStream(file).pipe(res);
});

server.listen(PORT, () => console.log(`listening on ${PORT}`));
