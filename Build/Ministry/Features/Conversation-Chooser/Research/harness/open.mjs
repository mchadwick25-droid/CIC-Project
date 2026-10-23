// Open one URL the way the research grid needs: desktop + phone full-page shots,
// reduced-motion render, keyboard tab order, and a count of horizontal scrollers.
// Usage: node open.mjs <name> <url> [--dismiss "selector"] [--scrollto "selector"]
import { chromium } from 'playwright-core';
import fs from 'node:fs';

const [name, url, ...rest] = process.argv.slice(2);
if (!name || !url) { console.error('usage: node open.mjs <name> <url>'); process.exit(1); }
const opt = {};
for (let i = 0; i < rest.length; i += 2) opt[rest[i].replace(/^--/, '')] = rest[i + 1];
const outDir = new URL('../shots/', import.meta.url).pathname;
fs.mkdirSync(outDir, { recursive: true });

const browser = await chromium.launch({
  executablePath: '/opt/pw-browsers/chromium-1194/chrome-linux/chrome',
  args: ['--no-sandbox', '--disable-gpu'],
});

async function visit(label, viewport, extra = {}) {
  const ctx = await browser.newContext({ viewport, deviceScaleFactor: 1, ...extra });
  const page = await ctx.newPage();
  const result = { label, viewport, url };
  try {
    await page.goto(url, { waitUntil: 'domcontentloaded', timeout: 45000 });
    await page.waitForLoadState('networkidle', { timeout: 20000 }).catch(() => {});
    if (opt.dismiss) await page.locator(opt.dismiss).first().click({ timeout: 3000 }).catch(() => {});
    // scroll through to trigger lazy content, then back to top (or to a target)
    const h = await page.evaluate(() => document.documentElement.scrollHeight);
    for (let y = 0; y < Math.min(h, 12000); y += viewport.height * 0.8) {
      await page.evaluate(v => window.scrollTo(0, v), y);
      await page.waitForTimeout(150);
    }
    await page.evaluate(() => window.scrollTo(0, 0));
    if (opt.scrollto) await page.locator(opt.scrollto).first().scrollIntoViewIfNeeded({ timeout: 3000 }).catch(() => {});
    await page.waitForTimeout(600);
    result.title = await page.title();
    result.pageWidthOverflow = await page.evaluate(() => document.documentElement.scrollWidth - document.documentElement.clientWidth);
    result.scrollHeight = await page.evaluate(() => document.documentElement.scrollHeight);
    result.horizontalScrollers = await page.evaluate(() => {
      const out = [];
      for (const el of document.querySelectorAll('*')) {
        const cs = getComputedStyle(el);
        if ((cs.overflowX === 'auto' || cs.overflowX === 'scroll') && el.scrollWidth > el.clientWidth + 8 && el.clientWidth > 100) {
          out.push({ tag: el.tagName.toLowerCase(), cls: (el.className || '').toString().slice(0, 60), w: el.clientWidth, sw: el.scrollWidth, snap: cs.scrollSnapType, role: el.getAttribute('role'), tabindex: el.getAttribute('tabindex') });
        }
      }
      return out.slice(0, 12);
    });
    result.transforms3d = await page.evaluate(() => {
      let n = 0;
      for (const el of document.querySelectorAll('*')) { const t = getComputedStyle(el).transform; if (t && t.startsWith('matrix3d')) n++; }
      return n;
    });
    // keyboard: first 40 tab stops
    const stops = [];
    for (let i = 0; i < 40; i++) {
      await page.keyboard.press('Tab');
      const info = await page.evaluate(() => {
        const a = document.activeElement; if (!a || a === document.body) return null;
        const r = a.getBoundingClientRect();
        return { tag: a.tagName.toLowerCase(), text: (a.getAttribute('aria-label') || a.innerText || a.getAttribute('alt') || '').trim().replace(/\s+/g, ' ').slice(0, 50), role: a.getAttribute('role'), visible: r.width > 0 && r.height > 0 };
      });
      if (!info) break; stops.push(info);
    }
    result.tabStops = stops;
    const file = `${outDir}${name}-${label}.png`;
    await page.screenshot({ path: file, fullPage: true });
    result.shot = file;
  } catch (e) { result.error = String(e).slice(0, 300); }
  await ctx.close();
  return result;
}

const results = [];
results.push(await visit('desktop', { width: 1280, height: 800 }));
results.push(await visit('phone', { width: 390, height: 844 }, { isMobile: true, hasTouch: true, userAgent: 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1' }));
results.push(await visit('reduced', { width: 1280, height: 800 }, { reducedMotion: 'reduce' }));
await browser.close();
fs.writeFileSync(`${outDir}${name}.json`, JSON.stringify(results, null, 1));
for (const r of results) {
  console.log(`== ${r.label} ${r.viewport.width}px ${r.error ? 'ERROR ' + r.error : ''}`);
  if (r.error) continue;
  console.log(`title: ${r.title} | height ${r.scrollHeight} | page x-overflow ${r.pageWidthOverflow}px | matrix3d elements ${r.transforms3d}`);
  console.log('horizontal scrollers:', JSON.stringify(r.horizontalScrollers));
  console.log('tab stops:', r.tabStops.map(s => `${s.tag}${s.role ? '[' + s.role + ']' : ''}:${s.text}${s.visible ? '' : '(hidden)'}`).join(' | '));
}
