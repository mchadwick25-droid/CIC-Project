import { test } from 'node:test';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import worker, { parseRange, BASELINE_HEADERS, resetRenamesForTests } from './worker.mjs';

const FILE = Buffer.from(Array.from({ length: 100 }, (_, i) => i));

function envWith(files) {
  return {
    ASSETS: {
      calls: [],
      async fetch(req) {
        this.calls.push({ url: req.url, range: req.headers.get('Range'), method: req.method });
        const p = new URL(req.url).pathname;
        if (!(p in files)) return new Response('not found', { status: 404 });
        return new Response(req.method === 'HEAD' ? null : files[p], {
          status: 200,
          headers: { 'Content-Type': 'audio/mpeg', 'Content-Length': String(files[p].length), ETag: '"abc"', 'Cache-Control': 'public, max-age=0, must-revalidate' },
        });
      },
    },
  };
}
const get = (path, headers = {}, method = 'GET') => new Request('https://example.test' + path, { method, headers });

test('parseRange: open end, closed, suffix, clamped end', () => {
  assert.deepEqual(parseRange('bytes=0-1', 100), { start: 0, end: 1 });
  assert.deepEqual(parseRange('bytes=10-', 100), { start: 10, end: 99 });
  assert.deepEqual(parseRange('bytes=-5', 100), { start: 95, end: 99 });
  assert.deepEqual(parseRange('bytes=90-500', 100), { start: 90, end: 99 });
});

test('parseRange: unsatisfiable is null; not a single bytes range is ignored', () => {
  assert.equal(parseRange('bytes=100-', 100), null);
  assert.equal(parseRange('bytes=50-10', 100), null);
  assert.equal(parseRange('bytes=-0', 100), null);
  assert.equal(parseRange('bytes=0-1,5-6', 100), 'ignore');
  assert.equal(parseRange('items=0-1', 100), 'ignore');
  assert.equal(parseRange('bytes=-', 100), 'ignore');
});

test('Safari probe: bytes=0-1 on audio answers 206 with the right bytes and headers', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=0-1' }), env);
  assert.equal(res.status, 206);
  assert.equal(res.headers.get('Content-Range'), 'bytes 0-1/100');
  assert.equal(res.headers.get('Content-Length'), '2');
  assert.equal(res.headers.get('Accept-Ranges'), 'bytes');
  assert.equal(res.headers.get('Content-Type'), 'audio/mpeg');
  assert.deepEqual([...Buffer.from(await res.arrayBuffer())], [0, 1]);
  assert.equal(env.ASSETS.calls[0].range, null, 'the asset fetch carries no Range header');
});

test('a later range returns exactly that slice', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=40-' }), env);
  assert.equal(res.status, 206);
  assert.equal(res.headers.get('Content-Range'), 'bytes 40-99/100');
  assert.deepEqual([...Buffer.from(await res.arrayBuffer())], [...FILE.subarray(40)]);
});

test('no Range: 200 with the whole file and Accept-Ranges advertised', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3'), env);
  assert.equal(res.status, 200);
  assert.equal(res.headers.get('Accept-Ranges'), 'bytes');
  assert.equal(res.headers.get('ETag'), '"abc"');
  assert.equal((await res.arrayBuffer()).byteLength, 100);
});

test('unsatisfiable range: 416 with Content-Range */size', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=500-' }), env);
  assert.equal(res.status, 416);
  assert.equal(res.headers.get('Content-Range'), 'bytes */100');
});

test('multi-range is ignored: 200 with the whole file', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=0-1,5-6' }), env);
  assert.equal(res.status, 200);
  assert.equal((await res.arrayBuffer()).byteLength, 100);
});

test('HEAD advertises Accept-Ranges and sends no body', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', {}, 'HEAD'), env);
  assert.equal(res.status, 200);
  assert.equal(res.headers.get('Accept-Ranges'), 'bytes');
});

test('a missing audio file is passed through as 404', async () => {
  const env = envWith({});
  const res = await worker.fetch(get('/audio/none.mp3', { Range: 'bytes=0-1' }), env);
  assert.equal(res.status, 404);
});

test('anything outside /audio/ goes straight to the assets, Range untouched', async () => {
  const env = envWith({ '/data/x.json': FILE });
  const res = await worker.fetch(get('/data/x.json', { Range: 'bytes=0-1' }), env);
  assert.equal(res.status, 200);
  assert.equal(env.ASSETS.calls[0].range, 'bytes=0-1');
});

test('non-read methods on /audio/ go straight to the assets', async () => {
  const env = envWith({ '/audio/a.mp3': FILE });
  await worker.fetch(get('/audio/a.mp3', {}, 'POST'), env);
  assert.equal(env.ASSETS.calls[0].method, 'POST');
});

// ---- the R2 bucket bound as AUDIO ----

function bucketWith(objects, { throws = false } = {}) {
  const calls = [];
  return {
    calls,
    async head(key) {
      calls.push(['head', key]);
      if (throws) throw new Error('bucket unreachable');
      if (!(key in objects)) return null;
      return { size: objects[key].length, httpEtag: '"r2etag"', httpMetadata: { contentType: 'audio/mpeg' } };
    },
    async get(key, opts) {
      calls.push(['get', key, opts && opts.range]);
      if (!(key in objects)) return null;
      const r = opts && opts.range;
      const body = r ? objects[key].subarray(r.offset, r.offset + r.length) : objects[key];
      return { body: new Blob([body]).stream() };
    },
  };
}
const withBucket = (files, objects, opts) => ({ ...envWith(files), AUDIO: bucketWith(objects, opts) });

test('bucket: a range is read from the bucket, with a 206 and the right bytes', async () => {
  const env = withBucket({}, { 'audio/a.mp3': FILE });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=10-19' }), env);
  assert.equal(res.status, 206);
  assert.equal(res.headers.get('Content-Range'), 'bytes 10-19/100');
  assert.equal(res.headers.get('Content-Length'), '10');
  assert.equal(res.headers.get('ETag'), '"r2etag"');
  assert.deepEqual([...Buffer.from(await res.arrayBuffer())], [...FILE.subarray(10, 20)]);
  assert.deepEqual(env.AUDIO.calls[1], ['get', 'audio/a.mp3', { offset: 10, length: 10 }]);
  assert.equal(env.ASSETS.calls.length, 0, 'the assets are not touched');
});

test('bucket: whole file, HEAD, 416 and the conditional 304', async () => {
  const env = withBucket({}, { 'audio/a.mp3': FILE });
  const whole = await worker.fetch(get('/audio/a.mp3'), env);
  assert.equal(whole.status, 200);
  assert.equal(whole.headers.get('Accept-Ranges'), 'bytes');
  assert.equal((await whole.arrayBuffer()).byteLength, 100);
  const head = await worker.fetch(get('/audio/a.mp3', {}, 'HEAD'), env);
  assert.equal(head.status, 200);
  assert.equal(head.headers.get('Content-Length'), '100');
  const bad = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=500-' }), env);
  assert.equal(bad.status, 416);
  assert.equal(bad.headers.get('Content-Range'), 'bytes */100');
  const same = await worker.fetch(get('/audio/a.mp3', { 'If-None-Match': '"r2etag"' }), env);
  assert.equal(same.status, 304);
});

test('bucket: a file the bucket lacks falls back to the assets', async () => {
  const env = withBucket({ '/audio/old.mp3': FILE }, {});
  const res = await worker.fetch(get('/audio/old.mp3', { Range: 'bytes=0-1' }), env);
  assert.equal(res.status, 206);
  assert.equal(env.ASSETS.calls.length, 1);
});

test('bucket: an unreachable bucket falls back to the assets instead of failing', async () => {
  const env = withBucket({ '/audio/a.mp3': FILE }, { 'audio/a.mp3': FILE }, { throws: true });
  const res = await worker.fetch(get('/audio/a.mp3', { Range: 'bytes=0-1' }), env);
  assert.equal(res.status, 206);
  assert.deepEqual([...Buffer.from(await res.arrayBuffer())], [0, 1]);
});

test('bucket: manifest and other non-recording files under /audio/ always come from the assets', async () => {
  const env = withBucket({ '/audio/worlds/manifest.json': FILE }, { 'audio/worlds/manifest.json': FILE });
  const res = await worker.fetch(get('/audio/worlds/manifest.json'), env);
  assert.equal(res.status, 200);
  assert.equal(env.AUDIO.calls.length, 0);
  assert.equal(env.ASSETS.calls.length, 1);
});

test('bucket: a path with encoded characters is looked up by its decoded key', async () => {
  const env = withBucket({}, { 'audio/a b.mp3': FILE });
  const res = await worker.fetch(get('/audio/a%20b.mp3'), env);
  assert.equal(res.status, 200);
});

for (const site of ['cic-website', 'cft-website']) {
  test(`the headers added to bucket answers match the baseline of ${site}/_headers`, () => {
    const text = fs.readFileSync(new URL(`../${site}/_headers`, import.meta.url), 'utf8');
    const block = text.split('\n').reduce((acc, line) => {
      if (/^\/\*\s*$/.test(line)) acc.on = true;
      else if (/^\S/.test(line) && acc.on) acc.on = false;
      else if (acc.on && /^\s+[A-Za-z-]+:/.test(line)) {
        const [k, ...v] = line.trim().split(':');
        acc.map[k.trim()] = v.join(':').trim();
      }
      return acc;
    }, { on: false, map: {} }).map;
    assert.deepEqual(BASELINE_HEADERS, block);
  });
}

const TREE = 'https://www.churchfamilytree.com';
function oldSite(census = { retiredMovements: [] }) {
  resetRenamesForTests();
  const env = envWith({ '/data/world-census.json': Buffer.from(JSON.stringify(census)), '/index.html': Buffer.from('home') });
  env.TREE_ORIGIN = TREE;
  return env;
}

test('old site: a tree page redirects permanently, in one hop, to the same path on the tree domain', async () => {
  for (const path of ['/tree/donatism', '/tree/donatism.html']) {
    const res = await worker.fetch(get(path + '?from=x'), oldSite());
    assert.equal(res.status, 301);
    assert.equal(res.headers.get('Location'), TREE + '/tree/donatism?from=x');
    assert.equal(res.headers.get('X-Content-Type-Options'), 'nosniff');
  }
});

test('old site: the map addresses redirect to the tree home, keeping the query', async () => {
  for (const path of ['/atlas-v3.html', '/atlas-v3', '/atlas.html', '/atlas', '/world-atlas.html', '/world-atlas', '/tree', '/tree/']) {
    const res = await worker.fetch(get(path + '?worlds=donatism'), oldSite());
    assert.equal(res.status, 301, path);
    assert.equal(res.headers.get('Location'), TREE + '/?worlds=donatism', path);
  }
});

test('old site: moved narration redirects to the same path on the tree domain', async () => {
  for (const path of ['/audio/tree/donatism.mp3', '/audio/docstories/x-0.mp3', '/audio/stories/y.mp3', '/audio/tree/manifest.json']) {
    const res = await worker.fetch(get(path), oldSite());
    assert.equal(res.status, 301, path);
    assert.equal(res.headers.get('Location'), TREE + path);
  }
});

test('old site: a renamed movement goes straight to its new page in the same hop', async () => {
  const env = oldSite({ retiredMovements: [{ id: 'old-name', date: '2026-11-07', reason: 'renamed', redirectTo: 'new-name' }] });
  const res = await worker.fetch(get('/tree/old-name.html'), env);
  assert.equal(res.status, 301);
  assert.equal(res.headers.get('Location'), TREE + '/tree/new-name');
});

test('old site: the census and everything else are served, never redirected', async () => {
  const env = oldSite();
  for (const path of ['/data/world-census.json', '/index.html']) {
    const res = await worker.fetch(get(path), env);
    assert.equal(res.status, 200, path);
  }
  const audio = await worker.fetch(get('/audio/worlds/x.mp3'), env);
  assert.notEqual(audio.status, 301);
});

test('tree site: with no TREE_ORIGIN nothing redirects', async () => {
  resetRenamesForTests();
  const env = envWith({ '/tree/donatism': Buffer.from('page') });
  const res = await worker.fetch(get('/tree/donatism'), env);
  assert.equal(res.status, 200);
});

function eventsEnv() {
  const points = [];
  return { points, env: { ...envWith({}), EVENTS: { writeDataPoint: (p) => points.push(p) } } };
}
const post = (body, headers = {}) => new Request('https://example.test/e', { method: 'POST', body, headers: { 'User-Agent': 'Mozilla/5.0 (iPhone)', ...headers } });

test('events: listed types are written as short anonymous points; others are dropped', async () => {
  const { points, env } = eventsEnv();
  const body = JSON.stringify([
    { t: 'visit', a: 'returning', b: 'facebook', c: 'phone', n: [1, 1, 0] },
    { t: 'open', a: 'tradition', b: 'desert-monasticism' },
    { t: 'listen', a: 'tree', b: 'tertullian-s-voice', c: '50' },
    { t: 'ip', a: '1.2.3.4' },
    { t: 'open', a: '<script>', b: 'x'.repeat(500) },
  ]);
  const res = await worker.fetch(post(body), env);
  assert.equal(res.status, 204);
  assert.equal(points.length, 4);
  assert.deepEqual(points[0], { indexes: ['visit'], blobs: ['visit', 'returning', 'facebook', 'phone', '', '', '', 'other'], doubles: [1, 1, 0] });
  assert.equal(points[3].blobs[1], 'script');
  assert.equal(points[3].blobs[2].length, 120);
  assert.equal(env.ASSETS.calls.length, 0);
});

test('events: the visitor id, country, region and browser family are stored; a malformed id is not; no address is stored', async () => {
  const { points, env } = eventsEnv();
  const vid = 'a1b2c3d4e5f60718293a4b5c6d7e8f90';
  const body = JSON.stringify([{ t: 'open', a: 'tradition', b: 'x', v: vid }, { t: 'open', a: 'tradition', b: 'y', v: 'not-an-id' }, { t: 'owner', v: vid }]);
  const req = post(body, { 'CF-Connecting-IP': 'addr-nine' });
  Object.defineProperty(req, 'cf', { value: { country: 'GB', region: 'England' } });
  await worker.fetch(req, env);
  assert.deepEqual(points[0].blobs, ['open', 'tradition', 'x', '', vid, 'GB', 'England', 'other']);
  assert.equal(points[1].blobs[4], '');
  assert.equal(points[2].blobs[0], 'owner');
  assert.ok(!JSON.stringify(points).includes('addr-nine'));
});

test('events: a step onward from a brief is counted with its kind and the card it opens', async () => {
  const { points, env } = eventsEnv();
  const body = JSON.stringify([
    { t: 'next', a: 'after', b: 'coptic-orthodox-church' },
    { t: 'next', a: 'teaser', b: 'donatism' },
  ]);
  assert.equal((await worker.fetch(post(body), env)).status, 204);
  assert.deepEqual(points.map((p) => p.blobs.slice(0, 3)), [['next', 'after', 'coptic-orthodox-church'], ['next', 'teaser', 'donatism']]);
});

test('events: a request from an address in OWNER_IPS writes nothing; others still count; unset counts all', async () => {
  const one = JSON.stringify([{ t: 'open', a: 'tradition', b: 'x' }]);
  const { points, env } = eventsEnv();
  env.OWNER_IPS = 'addr-one, addr-two';
  assert.equal((await worker.fetch(post(one, { 'CF-Connecting-IP': 'addr-two' }), env)).status, 204);
  assert.equal(points.length, 0);
  await worker.fetch(post(one, { 'CF-Connecting-IP': 'addr-three' }), env);
  assert.equal(points.length, 1);
  delete env.OWNER_IPS;
  await worker.fetch(post(one, { 'CF-Connecting-IP': 'addr-two' }), env);
  assert.equal(points.length, 2);
});

test('events: bots, wrong methods, oversized bodies and a site without the binding write nothing', async () => {
  const { points, env } = eventsEnv();
  const one = JSON.stringify([{ t: 'open', a: 'tradition', b: 'x' }]);
  assert.equal((await worker.fetch(post(one, { 'User-Agent': 'facebookexternalhit/1.1' }), env)).status, 204);
  assert.equal((await worker.fetch(get('/e'), env)).status, 405);
  assert.equal((await worker.fetch(post('[' + '{"t":"open"},'.repeat(1000) + '{}]'), env)).status, 413);
  assert.equal((await worker.fetch(post('not json'), env)).status, 204);
  assert.equal((await worker.fetch(post(one), envWith({}))).status, 204);
  assert.equal(points.length, 0);
});

test('events: at most 25 events from one request', async () => {
  const { points, env } = eventsEnv();
  await worker.fetch(post(JSON.stringify(Array.from({ length: 40 }, () => ({ t: 'layer', a: 'people' })))), env);
  assert.equal(points.length, 25);
});

const HOME_HEAD = '<!doctype html><html><head><meta charset="utf-8"><title>Church Family Tree — An Interactive Map of Church History</title>\n'
  + '<meta name="description" content="A free map of church history.">\n<link rel="canonical" href="https://www.churchfamilytree.com/">\n'
  + '<meta property="og:title" content="Church Family Tree">\n<meta property="og:image" content="https://www.churchfamilytree.com/share/church-family-tree.jpg">\n'
  + '<meta name="twitter:card" content="summary_large_image">\n<script>var SECRET_DATA_MARKER=1;</script></head><body>';
function homeEnv(head = HOME_HEAD, filler = 5 * 1024 * 1024) {
  const state = { pulled: 0, calls: [] };
  return {
    state,
    ASSETS: {
      async fetch(req) {
        state.calls.push(new URL(req.url).pathname + ':' + req.method);
        const chunk = new Uint8Array(65536).fill(120);
        let sent = false;
        return new Response(new ReadableStream({
          pull(controller) {
            if (!sent) { sent = true; controller.enqueue(new TextEncoder().encode(head)); return; }
            if (state.pulled * 65536 >= filler) { controller.close(); return; }
            state.pulled += 1; controller.enqueue(chunk);
          },
        }), { status: 200, headers: { 'Content-Type': 'text/html' } });
      },
    },
  };
}
const LINKEDIN = 'LinkedInBot/1.0 (compatible; Mozilla/5.0; Apache-HttpClient +http://www.linkedin.com)';

test('link-preview crawler gets a small page made from the home page head tags', async () => {
  const env = homeEnv();
  const res = await worker.fetch(get('/?utm_source=linkedin', { 'User-Agent': LINKEDIN }), env);
  const body = await res.text();
  assert.equal(res.status, 200);
  assert.match(res.headers.get('Content-Type'), /text\/html/);
  assert.ok(body.length < 3000, 'small page, not the 9 MB map');
  for (const tag of ['<title>Church Family Tree', 'name="description"', 'rel="canonical"', 'property="og:image"', 'name="twitter:card"']) assert.ok(body.includes(tag), tag);
  assert.ok(!body.includes('SECRET_DATA_MARKER'), 'scripts and data are left out');
  assert.equal(res.headers.get('Vary'), 'User-Agent');
  for (const k of Object.keys(BASELINE_HEADERS)) assert.equal(res.headers.get(k), BASELINE_HEADERS[k]);
  assert.ok(env.state.pulled < 20, 'stopped reading after the head, not the whole page');
});

test('every preview crawler on the list gets the small page; a browser and a search crawler do not', async () => {
  for (const ua of ['Twitterbot/1.0', 'Slackbot-LinkExpanding 1.0', 'Mozilla/5.0 (compatible; Discordbot/2.0)', 'WhatsApp/2.23', 'facebookexternalhit/1.1']) {
    const res = await worker.fetch(get('/', { 'User-Agent': ua }), homeEnv());
    assert.ok((await res.text()).length < 3000, ua);
  }
  for (const ua of ['Mozilla/5.0 (Windows NT 10.0) Chrome/120 Safari/537.36', 'Mozilla/5.0 (compatible; Googlebot/2.1; +http://www.google.com/bot.html)', '']) {
    const env = homeEnv(HOME_HEAD, 65536);
    const res = await worker.fetch(get('/', ua ? { 'User-Agent': ua } : {}), env);
    assert.ok((await res.text()).includes('SECRET_DATA_MARKER'), 'the page itself: ' + (ua || 'no agent'));
  }
});

test('preview page: HEAD has no body, other paths and a head with no tags pass through', async () => {
  const head = await worker.fetch(get('/', { 'User-Agent': LINKEDIN }, 'HEAD'), homeEnv());
  assert.equal(head.status, 200);
  assert.equal(await head.text(), '');
  const env = homeEnv();
  await worker.fetch(get('/about', { 'User-Agent': LINKEDIN }), env);
  assert.deepEqual(env.state.calls, ['/about:GET']);
  const bare = homeEnv('<!doctype html><html><head></head><body>', 65536);
  const res = await worker.fetch(get('/', { 'User-Agent': LINKEDIN }), bare);
  assert.ok((await res.text()).includes('<body>'), 'no tags to use: the page itself');
});
