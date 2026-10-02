// Blueprint §L self-verify harness for cic-website/atlas-v3.html.
// Screenshots at 390/1280 (light+dark), geometric no-overlap check on .node
// boxes, interaction smoke (search, chip filters, hover-trace, document open,
// era rail jump). Zero JS errors required. Run: node Design/tools/shoot.mjs
import { chromium } from 'playwright';
import { createServer } from 'http';
import { readFileSync, mkdirSync, writeFileSync } from 'fs';
import { extname, join } from 'path';

const ROOT = '/home/user/CIC-Project/cic-website';
const OUT = '/home/user/CIC-Project/Ministry/Features/Atlas-World-Map/Design/tools/shots';
mkdirSync(OUT, { recursive: true });

const srv = createServer((req, res) => {
  try {
    const p = ROOT + (req.url === '/' ? '/atlas-v3.html' : req.url.split('?')[0]);
    const t = { '.html': 'text/html', '.css': 'text/css', '.js': 'text/javascript', '.json': 'application/json' }[extname(p)] || 'text/plain';
    res.writeHead(200, { 'content-type': t });
    res.end(readFileSync(p));
  } catch (e) { res.writeHead(404); res.end(); }
});
await new Promise(r => srv.listen(8124, r));

const browser = await chromium.launch({ executablePath: '/opt/pw-browsers/chromium' });
const results = { screenshots: [], overlaps: [], smoke: {}, jsErrors: [] };

async function shoot(width, scheme) {
  const page = await browser.newPage({ viewport: { width, height: 900 }, colorScheme: scheme });
  const errs = [];
  page.on('pageerror', e => errs.push(String(e)));
  await page.goto('http://localhost:8124/atlas-v3.html');
  await page.waitForTimeout(1200);
  const file = join(OUT, `atlas-v3_${width}_${scheme}.png`);
  await page.screenshot({ path: file, fullPage: true });
  results.screenshots.push(file);
  if (errs.length) results.jsErrors.push(...errs.map(e => `[${width}/${scheme}] ${e}`));

  // Geometric no-overlap check on .node boxes (own-era boxes should not overlap each other)
  const overlaps = await page.evaluate(() => {
    const nodes = [...document.querySelectorAll('.node')];
    const rects = nodes.map(n => ({ id: n.dataset.id, r: n.getBoundingClientRect() }))
      .filter(x => x.r.width > 0 && x.r.height > 0);
    const hits = [];
    const EPS = 1; // px tolerance
    for (let i = 0; i < rects.length; i++) {
      for (let j = i + 1; j < rects.length; j++) {
        const a = rects[i].r, b = rects[j].r;
        const overlapX = Math.min(a.right, b.right) - Math.max(a.left, b.left);
        const overlapY = Math.min(a.bottom, b.bottom) - Math.max(a.top, b.top);
        if (overlapX > EPS && overlapY > EPS) {
          hits.push({ a: rects[i].id, b: rects[j].id, overlapX: Math.round(overlapX), overlapY: Math.round(overlapY) });
        }
      }
    }
    return hits;
  });
  if (overlaps.length) results.overlaps.push({ width, scheme, count: overlaps.length, sample: overlaps.slice(0, 5) });

  // Box-vs-foreign-tail check (Wave 3, Engineering P1-8): the Blueprint's
  // own stated invariant is that a movement's box may sit on ITS OWN tail
  // (the continuation of the same movement) but never on another
  // movement's - previously unguarded by this harness. `.shoulder`/`.seal`
  // share the same data-mid convention and the same "own tail is fine,
  // someone else's is not" rule, so they're checked the same way.
  const foreignTailOverlaps = await page.evaluate(() => {
    const nodes = [...document.querySelectorAll('.node')]
      .map(n => ({ id: n.dataset.id, r: n.getBoundingClientRect() }))
      .filter(x => x.r.width > 0 && x.r.height > 0);
    const threads = [...document.querySelectorAll('#art .tail,#art .shoulder,#art .seal')]
      .map(t => ({ mid: t.dataset.mid, r: t.getBoundingClientRect() }))
      .filter(x => x.r.width > 0 && x.r.height > 0);
    const hits = [];
    const EPS = 1;
    for (const n of nodes) {
      for (const t of threads) {
        if (n.id === t.mid) continue; // a movement's own tail under its own box is expected
        const overlapX = Math.min(n.r.right, t.r.right) - Math.max(n.r.left, t.r.left);
        const overlapY = Math.min(n.r.bottom, t.r.bottom) - Math.max(n.r.top, t.r.top);
        if (overlapX > EPS && overlapY > EPS) {
          hits.push({ node: n.id, foreignTailOf: t.mid, overlapX: Math.round(overlapX), overlapY: Math.round(overlapY) });
        }
      }
    }
    return hits;
  });
  if (foreignTailOverlaps.length) {
    results.foreignTailOverlaps = results.foreignTailOverlaps || [];
    results.foreignTailOverlaps.push({ width, scheme, count: foreignTailOverlaps.length, sample: foreignTailOverlaps.slice(0, 5) });
  }

  await page.close();
}

for (const width of [390, 1280]) {
  for (const scheme of ['light', 'dark']) {
    await shoot(width, scheme);
  }
}

// Interaction smoke on one desktop/light page
{
  const page = await browser.newPage({ viewport: { width: 1280, height: 900 } });
  const errs = [];
  page.on('pageerror', e => errs.push(String(e)));
  await page.goto('http://localhost:8124/atlas-v3.html');
  await page.waitForTimeout(1200);

  results.smoke.totalNodes = await page.evaluate(() => document.querySelectorAll('.node').length);
  results.smoke.counterText = await page.evaluate(() => document.querySelector('#cnt')?.textContent);

  // The page's real filter model: non-hiding, .match class + dimmed via .filtering CSS;
  // #cnt reports "N of total" while filtering is active — that's the ground truth to read.
  await page.fill('#q', 'coptic');
  await page.waitForTimeout(400);
  results.smoke.searchCopticMatches = await page.evaluate(() => document.querySelectorAll('.node.match').length);
  results.smoke.searchCopticCounterText = await page.evaluate(() => document.querySelector('#cnt')?.textContent);
  await page.fill('#q', '');
  await page.waitForTimeout(300);

  await page.click('#builtToggle');
  await page.waitForTimeout(400);
  results.smoke.liveChipMatches = await page.evaluate(() => document.querySelectorAll('.node.match').length);
  results.smoke.liveChipCounterText = await page.evaluate(() => document.querySelector('#cnt')?.textContent);
  await page.click('#builtToggle');
  await page.waitForTimeout(300);

  // hover-trace on first node
  const first = await page.$('.node');
  if (first) {
    await first.hover();
    await page.waitForTimeout(300);
    results.smoke.hoverTipVisible = await page.evaluate(() => {
      const tip = document.querySelector('#tip');
      return !!(tip && tip.innerHTML.trim().length > 0);
    });
    // Confirm the sheet is actually closed before the click, so a true
    // result below reflects a real state transition, not a check that
    // would have passed regardless (see the fix note on sheetOpensOnClick).
    results.smoke.sheetClosedBeforeClick = await page.evaluate(() => {
      const sheet = document.querySelector('#sheet');
      return !!(sheet && !sheet.classList.contains('on'));
    });
    await first.click();
    await page.waitForTimeout(400);
    results.smoke.sheetOpensOnClick = await page.evaluate(() => {
      // Was checking classList.contains('open') - the real toggle class is
      // 'on' (see #sheet.on{bottom:0} and the click handler's
      // sheet.classList.add('on')) - so that branch never matched, and this
      // always fell through to a vacuous fallback: #sheet is
      // position:fixed;left:0;right:0 even when closed (only its bottom
      // offset moves off-screen), so getBoundingClientRect().width is > 0
      // whether the sheet is open or not, and sheetBody keeps whatever
      // content it last held rather than clearing on close - meaning this
      // check reported true even with the sheet never touched. Wave 3,
      // Engineering P1-8.
      const sheet = document.querySelector('#sheet');
      return !!(sheet && sheet.classList.contains('on'));
    });
  }

  results.smoke.railLinks = await page.evaluate(() => document.querySelectorAll('#rail a, #rail button, #rail [data-era]').length);

  if (errs.length) results.jsErrors.push(...errs.map(e => `[smoke] ${e}`));
  await page.close();
}

// Mobile pinch-zoom smoke (Wave 3, Engineering P1-8): a real hasTouch
// context dispatching actual touch events at #mapViewport, checking that
// mapScale genuinely changes - this is the pinch-zoom path six straight
// rounds of manual fixes went into (Decision Log, 2026-08-05), and until
// now nothing in this harness exercised it at all.
{
  const page = await browser.newPage({ viewport: { width: 390, height: 844 }, hasTouch: true, isMobile: true });
  const errs = [];
  page.on('pageerror', e => errs.push(String(e)));
  await page.goto('http://localhost:8124/atlas-v3.html');
  await page.waitForTimeout(1200);

  // mapScale is a script-scoped `let` in a classic <script> tag, not a
  // window property - read the value it drives instead: #wrap's own
  // inline transform (applyMapScale sets style.transform = `scale(${s})`).
  const readScale = () => page.evaluate(() => {
    const m = (document.getElementById('wrap')?.style.transform || '').match(/scale\(([\d.]+)\)/);
    return m ? parseFloat(m[1]) : null;
  });
  const before = await readScale();
  const mv = await page.$('#mapViewport');
  const box = await mv.boundingBox();
  if (box) {
    const cx = box.x + box.width / 2, cy = box.y + box.height / 2;
    // Playwright has no native multi-touch pinch gesture - dispatch a
    // synthetic touchstart/touchmove/touchend pair directly, the same shape
    // the page's own pinch handler expects (ev.touches with 2 points).
    await page.evaluate(({ cx, cy }) => {
      const mv = document.getElementById('mapViewport');
      const mk = (x, y) => ({ clientX: x, clientY: y, identifier: Math.random() });
      const dispatch = (type, touches) => {
        const ev = new Event(type, { bubbles: true, cancelable: true });
        ev.touches = touches;
        mv.dispatchEvent(ev);
      };
      dispatch('touchstart', [mk(cx - 30, cy), mk(cx + 30, cy)]);
      dispatch('touchmove', [mk(cx - 80, cy), mk(cx + 80, cy)]);
      dispatch('touchend', []);
    }, { cx, cy });
    await page.waitForTimeout(300);
  }
  results.smoke.mobilePinchScaleBefore = before;
  results.smoke.mobilePinchScaleAfter = await readScale();
  results.smoke.mobilePinchChangedScale = results.smoke.mobilePinchScaleAfter !== results.smoke.mobilePinchScaleBefore;

  if (errs.length) results.jsErrors.push(...errs.map(e => `[mobile-pinch] ${e}`));
  await page.close();
}

await browser.close();
srv.close();

writeFileSync(join(OUT, 'report.json'), JSON.stringify(results, null, 1));
const foreignTailCount = (results.foreignTailOverlaps || []).reduce((n, g) => n + g.count, 0);
console.log(JSON.stringify({
  nodes: results.smoke.totalNodes,
  counter: results.smoke.counterText,
  searchCopticMatches: results.smoke.searchCopticMatches,
  searchCopticCounterText: results.smoke.searchCopticCounterText,
  liveChipMatches: results.smoke.liveChipMatches,
  liveChipCounterText: results.smoke.liveChipCounterText,
  hoverTipVisible: results.smoke.hoverTipVisible,
  sheetClosedBeforeClick: results.smoke.sheetClosedBeforeClick,
  sheetOpensOnClick: results.smoke.sheetOpensOnClick,
  railLinks: results.smoke.railLinks,
  overlapGroups: results.overlaps.length,
  foreignTailOverlaps: foreignTailCount,
  mobilePinchChangedScale: results.smoke.mobilePinchChangedScale,
  jsErrors: results.jsErrors.length ? results.jsErrors : 'none',
  screenshots: results.screenshots.length
}, null, 1));

// Non-zero exit so this can gate CI (Wave 3, Engineering P1-8) - previously
// always exited 0 regardless of what it found, so a real regression here
// was silent unless someone read report.json by hand.
//
// KNOWN, DISCLOSED, NOT YET FIXED: the box-vs-foreign-tail check above is
// new this wave and immediately found 17 real overlaps at 390px / 5 at
// 1280px (see report.json's foreignTailOverlaps) - a genuine violation of
// the Blueprint's own stated invariant, in the box-placement algorithm
// itself (layout()'s tryPack), not something this pass touches. This
// harness deliberately still fails on it rather than special-casing it
// quiet, so the defect stays visible until a future session fixes the
// packing logic - see Decision Log, Wave 3, for the disclosure.
const hasRegression =
  results.jsErrors.length > 0 ||
  results.overlaps.length > 0 ||
  foreignTailCount > 0 ||
  results.smoke.sheetOpensOnClick !== true ||
  results.smoke.mobilePinchChangedScale !== true;
if (hasRegression) process.exitCode = 1;
