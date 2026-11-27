// Browser test for the Church Family Tree's owner opt-out of the anonymous counts:
// ?count=off sets a flag on the device and the map then sends no events; ?count=on clears it.
// Run after `node tools/build_tree_site.mjs`:
//   node --test Build/tools/cft_count_optout.test.mjs
// Needs Playwright's Chromium (require('playwright')).
import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import fs from 'node:fs';
import http from 'node:http';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium } = require('playwright');
const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const site = path.join(root, '.build', 'tree');
const TYPES = { '.html': 'text/html', '.js': 'text/javascript', '.mjs': 'text/javascript', '.css': 'text/css', '.json': 'application/json', '.svg': 'image/svg+xml', '.png': 'image/png', '.webp': 'image/webp', '.woff2': 'font/woff2' };

let server, base, browser;
before(async () => {
  assert.ok(fs.existsSync(path.join(site, 'index.html')), 'build the tree site first: node tools/build_tree_site.mjs');
  server = http.createServer((req, res) => {
    const rel = decodeURIComponent(new URL(req.url, 'http://x').pathname).replace(/\/$/, '/index.html');
    const file = path.join(site, path.normalize(rel));
    if (!file.startsWith(site) || !fs.existsSync(file) || fs.statSync(file).isDirectory()) { res.writeHead(404); res.end(); return; }
    res.writeHead(200, { 'content-type': TYPES[path.extname(file)] || 'application/octet-stream' });
    fs.createReadStream(file).pipe(res);
  });
  await new Promise(r => server.listen(0, '127.0.0.1', r));
  base = `http://127.0.0.1:${server.address().port}/`;
  browser = await chromium.launch();
});
after(async () => { await browser?.close(); server?.close(); });

// Visits the map with one shared browser context, acts once, and returns what was sent to /e.
async function visit(ctx, query) {
  const page = await ctx.newPage();
  await page.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => false });
    window.__sent = [];
    navigator.sendBeacon = (url, body) => { window.__sent.push(url); return true; };
  });
  await page.goto(base + query, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => typeof applyTransform === 'function');
  await page.mouse.click(300, 300);
  await page.waitForTimeout(200);
  await page.evaluate(() => window.dispatchEvent(new Event('pagehide')));
  const state = await page.evaluate(() => ({
    sent: window.__sent.filter(u => u === '/e').length,
    flag: localStorage.getItem('cft-count-off'),
    toast: document.getElementById('barToast').textContent,
    url: location.search,
  }));
  await page.close();
  return state;
}

test('without the flag, a visit is counted', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const s = await visit(ctx, '');
  assert.ok(s.sent > 0);
  assert.equal(s.flag, null);
  await ctx.close();
});

test('?count=off sets the flag, says so, and sends nothing, now or later', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const first = await visit(ctx, '?count=off');
  assert.equal(first.flag, '1');
  assert.equal(first.sent, 0);
  assert.match(first.toast, /no longer counted/);
  assert.doesNotMatch(first.url, /count=/);
  const later = await visit(ctx, '');
  assert.equal(later.sent, 0);
  assert.equal(later.toast, '');
  await ctx.close();
});

test('?count=on clears the flag and counting resumes', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  await visit(ctx, '?count=off');
  const back = await visit(ctx, '?count=on');
  assert.equal(back.flag, null);
  assert.match(back.toast, /counted again/);
  assert.ok(back.sent > 0);
  await ctx.close();
});

test('other query parameters survive the opt-out visit', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const s = await visit(ctx, '?utm_source=x&count=off');
  assert.match(s.url, /utm_source=x/);
  assert.doesNotMatch(s.url, /count=/);
  await ctx.close();
});
