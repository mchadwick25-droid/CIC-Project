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
async function visit(ctx, query, eu = false) {
  const page = await ctx.newPage();
  await page.route('**/region', (route) => route.fulfill({ json: { eu } }));
  await page.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => false });
    window.__sent = [];
    navigator.sendBeacon = (url, body) => { if (url === '/e') body.text().then(t => window.__sent.push(JSON.parse(t))); return true; };
  });
  await page.goto(base + query, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => typeof applyTransform === 'function');
  await page.mouse.click(300, 300);
  await page.waitForTimeout(200);
  await page.evaluate(() => window.dispatchEvent(new Event('pagehide')));
  await page.waitForTimeout(300);
  const state = await page.evaluate(() => ({
    events: window.__sent.flat(),
    cookie: (document.cookie.match(/cft_vid=([a-f0-9]{32})/) || [])[1] || null,
    flag: localStorage.getItem('cft-count-off'),
    toast: document.getElementById('barToast').textContent,
    url: location.search,
  }));
  state.sent = state.events.filter(e => e.t !== 'owner').length;
  await page.close();
  return state;
}

test('without the flag, a visit is counted', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const s = await visit(ctx, '');
  assert.ok(s.sent > 0);
  assert.match(s.cookie, /^[a-f0-9]{32}$/);
  assert.ok(s.events.every(e => e.v === s.cookie));
  assert.equal(s.flag, null);
  await ctx.close();
});

test('?count=off sets the flag, says so, sends nothing, and marks an existing visitor number as the owner', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const counted = await visit(ctx, '');
  const first = await visit(ctx, '?count=off');
  assert.equal(first.flag, '1');
  assert.equal(first.sent, 0);
  assert.deepEqual(first.events.map(e => e.t), ['owner']);
  assert.equal(first.events[0].v, counted.cookie);
  assert.match(first.toast, /no longer counts/);
  assert.doesNotMatch(first.url, /count=/);
  const later = await visit(ctx, '');
  assert.equal(later.sent, 0);
  assert.equal(later.events.length, 0);
  assert.equal(later.toast, '');
  await ctx.close();
});

test('?count=off on a device with no visitor number makes none and sends nothing', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const s = await visit(ctx, '?count=off');
  assert.equal(s.flag, '1');
  assert.equal(s.events.length, 0);
  assert.equal(s.cookie, null);
  await ctx.close();
});

test('the visitor id stays the same across visits', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const a = await visit(ctx, '');
  const b = await visit(ctx, '');
  assert.equal(a.cookie, b.cookie);
  await ctx.close();
});

test('?count=on clears the flag and counting resumes', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  await visit(ctx, '?count=off');
  const back = await visit(ctx, '?count=on');
  assert.equal(back.flag, null);
  assert.match(back.toast, /counts your use in this browser again/);
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

async function euPage(ctx) {
  const page = await ctx.newPage();
  await page.route('**/region', (route) => route.fulfill({ json: { eu: true } }));
  await page.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => false });
    window.__sent = [];
    navigator.sendBeacon = (url, body) => { if (url === '/e') body.text().then(t => window.__sent.push(JSON.parse(t))); return true; };
  });
  await page.goto(base, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => typeof applyTransform === 'function');
  await page.waitForSelector('#cftConsent');
  return page;
}
const settle = async (page) => {
  await page.mouse.click(300, 300);
  await page.waitForTimeout(200);
  await page.evaluate(() => window.dispatchEvent(new Event('pagehide')));
  await page.waitForTimeout(300);
  return page.evaluate(() => ({ events: window.__sent.flat().length, cookie: document.cookie.includes('cft_vid') }));
};

test('Europe: the notice shows, and nothing is stored or sent until Yes', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await euPage(ctx);
  const before = await settle(page);
  assert.deepEqual(before, { events: 0, cookie: false });
  await page.click('#cftConsent button:first-of-type');
  const after = await settle(page);
  assert.ok(after.events > 0);
  assert.equal(after.cookie, true);
  await ctx.close();
});

test('Europe: No thanks sends nothing, keeps no cookie, and the notice does not return', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await euPage(ctx);
  await page.click('#cftConsent button:last-of-type');
  const s = await settle(page);
  assert.deepEqual(s, { events: 0, cookie: false });
  await page.close();
  const again = await ctx.newPage();
  await again.route('**/region', (route) => route.fulfill({ json: { eu: true } }));
  await again.goto(base, { waitUntil: 'domcontentloaded' });
  await again.waitForFunction(() => typeof applyTransform === 'function');
  await again.waitForTimeout(500);
  assert.equal(await again.locator('#cftConsent').count(), 0);
  await ctx.close();
});

test('outside Europe no notice shows, and a failed region lookup counts nothing', async () => {
  const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 } });
  const page = await ctx.newPage();
  await page.route('**/region', (route) => route.abort());
  await page.addInitScript(() => {
    Object.defineProperty(navigator, 'webdriver', { get: () => false });
    window.__sent = [];
    navigator.sendBeacon = (url, body) => { window.__sent.push(1); return true; };
  });
  await page.goto(base, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => typeof applyTransform === 'function');
  const s = await settle(page);
  assert.equal(s.events, 0);
  assert.equal(await page.locator('#cftConsent').count(), 0);
  await ctx.close();
});
