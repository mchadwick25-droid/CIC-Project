// Browser tests for the Church Family Tree map's view: the era information
// mark's place beside its title, the pan limit and the zoom-out floor.
// Run after `node tools/build_tree_site.mjs`:
//   node --test Build/tools/tree_map_view.test.mjs
// Needs Playwright's Chromium (require('playwright')).
import { test, before, after } from 'node:test';
import assert from 'node:assert/strict';
import { createRequire } from 'node:module';
import fs from 'node:fs';
import http from 'node:http';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const require = createRequire(import.meta.url);
const { chromium, devices } = require('playwright');
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

const SCREENS = [['desktop', { viewport: { width: 1440, height: 900 } }], ['iPhone 13', devices['iPhone 13']]];

async function openMap(opts, { holdFonts = false, dropFontEvents = false } = {}) {
  const ctx = await browser.newContext(opts);
  const page = await ctx.newPage();
  const errors = [];
  page.on('pageerror', e => errors.push(e.message));
  let release = () => {};
  if (holdFonts) {
    const held = new Promise(r => { release = r; });
    await page.route(/fonts\.gstatic\.com/, async route => { await held; await route.continue(); });
  }
  if (dropFontEvents) {
    await page.addInitScript(() => {
      const add = FontFaceSet.prototype.addEventListener;
      FontFaceSet.prototype.addEventListener = function (type, ...rest) { if (type !== 'loadingdone') add.call(this, type, ...rest); };
    });
  }
  await page.goto(base, { waitUntil: 'domcontentloaded' });
  await page.waitForFunction(() => typeof applyTransform === 'function' && document.querySelector('.era-label'));
  await page.waitForTimeout(400);
  return { ctx, page, errors, release };
}

const frames = page => page.evaluate(() => new Promise(r => requestAnimationFrame(() => requestAnimationFrame(r))));

// Gap in screen pixels between each era title's drawn end and its "i" mark.
async function markGaps(page) {
  await frames(page);
  return page.evaluate(() => [...document.querySelectorAll('.era-label')].map((t, i) => {
    const ring = document.querySelectorAll('.era-info')[i].querySelector('.era-info-ring');
    const tr = t.getBoundingClientRect(), rr = ring.getBoundingClientRect();
    return { era: i, gap: rr.left - tr.right, shown: tr.width > 0 && rr.width > 0 };
  }).filter(g => g.shown));
}

async function zoomTo(page, s) {
  await page.evaluate(s => { const cx = innerWidth / 2, cy = innerHeight / 2; zoomAt(cx, cy, s / scale); }, s);
}

function assertGaps(gaps, label) {
  assert.ok(gaps.length, `${label}: no era title is drawn`);
  for (const g of gaps) assert.ok(g.gap > 2 && g.gap < 22, `${label}: era ${g.era + 1} mark is ${g.gap.toFixed(1)} px from its title's end`);
}

for (const [name, opts] of SCREENS) {
  test(`${name}: the era mark sits just after its title at every zoom`, async () => {
    const { ctx, page, errors } = await openMap(opts);
    await page.evaluate(() => document.fonts.ready);
    for (const s of [0.2, 0.3, 0.39, 0.5, 0.6, 0.7, 0.79]) {
      await zoomTo(page, s);
      assertGaps(await markGaps(page), `zoom ${s}`);
    }
    assert.deepEqual(errors, []);
    await ctx.close();
  });

  test(`${name}: the era mark follows its title when the web font arrives late, with or without a font event`, async () => {
    for (const dropFontEvents of [false, true]) {
      const { ctx, page, errors, release } = await openMap(opts, { holdFonts: true, dropFontEvents });
      assert.equal(await page.evaluate(() => document.fonts.check('600 20px Cinzel')), false, 'the title font should still be loading');
      assertGaps(await markGaps(page), 'before the font');
      release();
      await page.waitForFunction(() => document.fonts.check('600 20px Cinzel'));
      await page.evaluate(() => document.fonts.ready);
      assertGaps(await markGaps(page), `font arrived${dropFontEvents ? ', no event' : ''}`);
      for (const s of [0.39, 0.5, 0.7]) {
        await zoomTo(page, s);
        assertGaps(await markGaps(page), `font arrived${dropFontEvents ? ', no event' : ''}, zoom ${s}`);
      }
      assert.deepEqual(errors, []);
      await ctx.close();
    }
  });
}

// The tree's box on screen against the map's own area (below the bars, beside
// an open Who list): no side may be more than a third empty.
async function assertOnScreen(page, label) {
  await frames(page);
  const v = await page.evaluate(() => {
    const top = Math.max(document.querySelector('.topbar').getBoundingClientRect().bottom,
      narrowScreen() ? 0 : document.querySelector('.feature-bar').getBoundingClientRect().bottom);
    const bottom = narrowScreen() ? document.querySelector('.feature-bar').getBoundingClientRect().top : innerHeight;
    const trayEl = document.getElementById('whoTray');
    const left = !narrowScreen() && !trayEl.hidden ? trayEl.getBoundingClientRect().right : 0;
    const r = document.getElementById('rivers').getBoundingClientRect();
    return { top, bottom, left, right: innerWidth, r: { l: r.left, r: r.right, t: r.top, b: r.bottom }, scale };
  });
  const w = v.right - v.left, h = v.bottom - v.top, slack = 40;
  assert.ok(v.r.l - v.left <= w / 3 + slack, `${label}: left of the tree is ${Math.round(v.r.l - v.left)} px empty of ${Math.round(w)}`);
  assert.ok(v.right - v.r.r <= w / 3 + slack, `${label}: right of the tree is ${Math.round(v.right - v.r.r)} px empty of ${Math.round(w)}`);
  assert.ok(v.r.t - v.top <= h / 3 + slack, `${label}: above the tree is ${Math.round(v.r.t - v.top)} px empty of ${Math.round(h)}`);
  assert.ok(v.bottom - v.r.b <= h / 3 + slack, `${label}: below the tree is ${Math.round(v.bottom - v.r.b)} px empty of ${Math.round(h)}`);
  return v;
}

async function cdpTouch(page, cdp, type, points) {
  await cdp.send('Input.dispatchTouchEvent', { type, touchPoints: points.map(([x, y], id) => ({ x, y, id })) });
}

test('desktop: a long drag, wheel and keys never take the tree off the screen', async () => {
  const { ctx, page, errors } = await openMap(SCREENS[0][1]);
  const start = await page.evaluate(() => scale);
  for (const [dx, dy] of [[-1, 0], [1, 0], [0, -1], [0, 1], [-1, -1], [1, 1]]) {
    await page.mouse.move(720, 500);
    await page.mouse.down();
    for (let k = 1; k <= 40; k++) await page.mouse.move(720 + dx * k * 150, 500 + dy * k * 150);
    await page.mouse.up();
    await assertOnScreen(page, `drag ${dx},${dy}`);
  }
  await page.mouse.move(720, 500);
  for (const [dx, dy] of [[4000, 0], [-8000, 0], [0, 30000], [0, -60000]]) {
    for (let k = 0; k < 10; k++) await page.mouse.wheel(dx / 10, dy / 10);
    await assertOnScreen(page, `wheel ${dx},${dy}`);
  }
  await page.evaluate(() => { document.activeElement?.blur?.(); });
  for (const key of ['ArrowLeft', 'ArrowRight', 'ArrowUp', 'ArrowDown', 'PageDown', 'PageUp']) {
    for (let k = 0; k < 60; k++) await page.keyboard.press(key);
    await assertOnScreen(page, `key ${key}`);
  }
  for (const key of ['End', 'Home']) { await page.keyboard.press(key); await assertOnScreen(page, `key ${key}`); }
  for (let k = 0; k < 30; k++) await page.keyboard.press('-');
  await assertOnScreen(page, 'keyboard zoom out');
  await page.keyboard.down('Control');
  for (let k = 0; k < 20; k++) await page.mouse.wheel(0, 300);
  await page.keyboard.up('Control');
  await assertOnScreen(page, 'ctrl-wheel zoom out');
  assert.ok(start > 0.45, `desktop opens at ${start}`);
  assert.deepEqual(errors, []);
  await ctx.close();
});

test('iPhone 13: a fling and a pinch never take the tree off the screen', async () => {
  const { ctx, page, errors } = await openMap(SCREENS[1][1]);
  const cdp = await ctx.newCDPSession(page);
  for (const [dx, dy] of [[-1, 0], [1, 0], [0, -1], [0, 1]]) {
    await cdpTouch(page, cdp, 'touchStart', [[195, 330]]);
    for (let k = 1; k <= 6; k++) { await cdpTouch(page, cdp, 'touchMove', [[195 + dx * k * 30, 330 + dy * k * 30]]); await page.waitForTimeout(8); }
    await cdpTouch(page, cdp, 'touchEnd', []);
    await page.waitForTimeout(2500);
    await assertOnScreen(page, `fling ${dx},${dy}`);
  }
  for (const [label, from, to] of [['pinch out far', [150, 40], [40, 4]], ['pinch in', [40, 4], [150, 40]]]) {
    await cdpTouch(page, cdp, 'touchStart', [[195 - from[0], 330 - from[1]], [195 + from[0], 330 + from[1]]]);
    for (let k = 1; k <= 20; k++) {
      const t = k / 20, ox = from[0] + (to[0] - from[0]) * t, oy = from[1] + (to[1] - from[1]) * t;
      await cdpTouch(page, cdp, 'touchMove', [[195 - ox + 60, 330 - oy + 200], [195 + ox + 60, 330 + oy + 200]]);
    }
    await cdpTouch(page, cdp, 'touchEnd', []);
    await assertOnScreen(page, label);
  }
  assert.deepEqual(errors, []);
  await ctx.close();
});

for (const [name, opts] of SCREENS) {
  test(`${name}: zooming out stops a little below the opening zoom, with the tree's width on screen`, async () => {
    const { ctx, page, errors } = await openMap(opts);
    const open = await page.evaluate(() => scale);
    for (let k = 0; k < 40; k++) await page.evaluate(() => document.getElementById('zoomOutBtn').click());
    const v = await assertOnScreen(page, 'zoomed all the way out');
    assert.ok(v.scale < open, `the floor ${v.scale} should sit below the opening zoom ${open}`);
    assert.ok(v.scale >= open * 0.4, `the floor ${v.scale} is too far below the opening zoom ${open}`);
    assert.ok(v.r.r - v.r.l <= v.right - v.left + 1, 'the whole width of the tree fits at the floor');
    assert.ok(v.r.l >= v.left - 1 && v.r.r <= v.right + 1, 'the tree is fully across the screen at the floor');
    await page.evaluate(() => document.getElementById('zoomResetBtn').click());
    assert.equal(await page.evaluate(() => scale), open, 'reset returns to the opening zoom');
    assert.deepEqual(errors, []);
    await ctx.close();
  });
}
