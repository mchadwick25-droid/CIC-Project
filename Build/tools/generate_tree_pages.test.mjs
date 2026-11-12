import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import crypto from 'node:crypto';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const census = JSON.parse(fs.readFileSync(path.join(root, 'cic-website/data/world-census.json'), 'utf8'));

function generate(c, audio = null) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'tree-pages-'));
  const file = path.join(dir, 'census.json');
  fs.writeFileSync(file, JSON.stringify(c));
  execFileSync('node', [path.join(root, 'Build/tools/generate_tree_pages.mjs'), '--census', file, '--out', dir, ...(audio ? ['--audio', audio] : [])], { stdio: 'ignore' });
  return name => fs.readFileSync(path.join(dir, 'cft-website', name), 'utf8');
}

const open = census.movements.find(m => m.publicOpen);
const exampleLinkId = JSON.parse(fs.readFileSync(path.join(root, 'Build/tools/tree_site_pages.json'), 'utf8')).citationExamples.link;
const withLinks = (c, n) => {
  const example = c.edges.find(e => e.id === exampleLinkId);
  c.edges = [example, ...c.edges.filter(e => e !== example).slice(0, n - 1)];
};

test('an open world gets a door to Church in Conversation', () => {
  const read = generate(census);
  const page = read(`tree/${open.id}.html`);
  assert.match(page, new RegExp(`href="https://churchinconversation.com/traditions/${open.id}.html">Meet `));
  assert.doesNotMatch(page, /class="door-quiet"/);
});

test('with every world closed, built worlds show only the quiet line', () => {
  const closed = structuredClone(census);
  closed.movements.forEach(m => { m.publicOpen = false; });
  const page = generate(closed)(`tree/${open.id}.html`);
  assert.doesNotMatch(page, /churchinconversation.com\/traditions\//);
  assert.match(page, /<p class="door-quiet"><a href="https:\/\/churchinconversation.com\/">Church in Conversation<\/a>, from the same team.<\/p>/);
});

test('the support page carries the not-a-nonprofit words of the Church in Conversation page', () => {
  const source = fs.readFileSync(path.join(root, 'cic-website/support.html'), 'utf8');
  const line = source.match(/<p class="fine-print">Church in Conversation is part of (Faithways Studio[^<]*)<\/p>/)[1];
  const page = fs.readFileSync(path.join(root, 'cft-website/support.html'), 'utf8');
  assert.ok(page.includes(`<p>Church Family Tree is part of ${line}</p>`));
});

test('major links are marked, and a link with an outcome shows its lasting result', () => {
  const c = structuredClone(census);
  const judged = c.edges.find(e => e.type === 'argued against');
  judged.outcome = 'The council condemned the group by name.';
  const lineage = c.edges.find(e => e.type === 'continued as');
  const minor = c.edges.find(e => e.type === 'influenced' && !e.outcome && e.from !== judged.from && e.from !== lineage.from);
  const read = generate(c);
  const item = (page, id) => page.match(new RegExp(`<li id="${id}">[\\s\\S]*?</li>`))[0];
  const judgedItem = item(read(`tree/${judged.from}.html`), judged.id);
  assert.match(judgedItem, /class="lineage-major">Major</);
  assert.match(judgedItem, /<i>Lasting result:<\/i> The council condemned the group by name\./);
  assert.match(item(read(`tree/${lineage.from}.html`), lineage.id), /class="lineage-major">Major</);
  assert.doesNotMatch(item(read(`tree/${minor.from}.html`), minor.id), /lineage-major|Lasting result/);
});

test('the Listen block shows only when the recording matches the page text', () => {
  const m = census.movements.find(x => x.longDescription && !fs.existsSync(path.join(root, `cic-website/data/worlds/${x.id}.json`)));
  const sha = t => crypto.createHash('sha256').update(t, 'utf8').digest('hex');
  const withManifest = entry => {
    const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'tree-audio-'));
    fs.writeFileSync(path.join(dir, 'manifest.json'), JSON.stringify(entry ? { [m.id]: entry } : {}));
    return generate(census, dir)(`tree/${m.id}.html`);
  };
  const base = { file: `${m.id}.mp3`, bytes: 1, md5: 'x' };
  const match = withManifest({ ...base, text_sha256: sha(m.longDescription) });
  assert.match(match, /class="narration"/);
  assert.match(match, /narration-player\.js/);
  for (const stale of [withManifest({ ...base, text_sha256: sha('older text') }), withManifest(base), withManifest(null)]) {
    assert.doesNotMatch(stale, /class="narration"/);
    assert.doesNotMatch(stale, /narration-player\.js/);
  }
});

test('the data page reads its release number, date and counts from the census', () => {
  const c = structuredClone(census);
  c.meta.release = { number: 987, date: '2031-02-03' };
  withLinks(c, 40);
  const page = generate(c)('data.html');
  assert.match(page, /The current file is release 987, dated February 3, 2031\./);
  assert.match(page, /release 987 \(February 3, 2031\), CC BY-NC 4\.0/);
  assert.match(page, new RegExp(`It holds ${c.movements.length} movements and 40 links\\.`));
  assert.doesNotMatch(page, new RegExp(`release ${census.meta.release.number}\\b`));
});

test('the citation examples name a real movement and a real link', () => {
  const content = JSON.parse(fs.readFileSync(path.join(root, 'Build/tools/tree_site_pages.json'), 'utf8'));
  const { movement, link } = content.citationExamples;
  assert.ok(census.movements.some(m => m.id === movement));
  const edge = census.edges.find(e => e.id === link);
  assert.ok(edge);
  const page = generate(census)('data.html');
  assert.ok(page.includes(`https://www.churchfamilytree.com/tree/${movement}`));
  assert.ok(page.includes(`https://www.churchfamilytree.com/tree/${edge.to}#${link}`));
  assert.match(generate(census)(`tree/${edge.to}.html`), new RegExp(`<li id="${link}">`));
});

test('the method page names the latest era and the census counts', () => {
  const c = structuredClone(census);
  withLinks(c, 25);
  const latest = c.eras.reduce((a, b) => (b.num > a.num ? b : a));
  const page = generate(c)('method.html');
  assert.ok(page.includes(`The tenth era, ${latest.title} (${latest.dates}), is not yet linked`));
  assert.match(page, new RegExp(`Today the tree holds 25 links among ${c.movements.length} movements\\.`));
  assert.match(page, /None of it has yet been reviewed by an independent scholar\./);
});

test('the method and data pages are linked from the about page, the map, every page footer and the sitemap', () => {
  const read = generate(census);
  const about = read('about.html');
  assert.match(about, /<a href="method.html">method page<\/a>/);
  assert.match(about, /<a href="data.html">data and citation page<\/a>/);
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  const keyFoot = map.match(/key\+=`<div class="foot">[^`]*`/)[0];
  assert.match(keyFoot, /<a href="method.html">Method<\/a>/);
  assert.match(keyFoot, /<a href="data.html">Data and citation<\/a>/);
  assert.match(read(`tree/${open.id}.html`), /<a href="\.\.\/method.html">Method<\/a>[\s\S]*<a href="\.\.\/data.html">Data and citation<\/a>/);
  const sitemap = read('sitemap.xml');
  assert.ok(sitemap.includes('<loc>https://www.churchfamilytree.com/method.html</loc>'));
  assert.ok(sitemap.includes('<loc>https://www.churchfamilytree.com/data.html</loc>'));
});

test('the about page counts movements and links from the census', () => {
  const c = structuredClone(census);
  withLinks(c, 12);
  const page = generate(c)('about.html');
  assert.match(page, /The tree shows 12 links of seven kinds\./);
  assert.match(page, new RegExp(`The tree covers ${c.movements.length} movements\\.`));
});

test('a person page says which tradition tells it, and carries that world door while it is open', () => {
  const c = structuredClone(census);
  const person = c.movements.find(m => m.kind === 'person');
  const read = generate(c);
  const page = read(`tree/${person.id}.html`);
  const home = c.movements.find(m => m.id === person.toldWithin);
  const world = c.movements.find(m => m.id === open.id);
  assert.match(page, new RegExp(`<p class="told-within">A person. The tradition that tells their story: <a href="${home.id}.html">`));
  assert.match(page, /<h2>About This Person<\/h2>/);
  assert.match(read(`tree/${home.id}.html`), new RegExp(`<ul class="people-list">\\s*<li><a href="${person.id}.html">`));
  person.toldWithin = world.id;
  home.people = [];
  world.people = [{ person: person.id }];
  const opened = generate(c);
  assert.match(opened(`tree/${person.id}.html`), new RegExp(`href="https://churchinconversation.com/traditions/${world.id}.html">Meet `));
  assert.match(opened(`tree/${world.id}.html`), new RegExp(`<a href="${person.id}.html">`));
  world.publicOpen = false;
  assert.doesNotMatch(generate(c)(`tree/${person.id}.html`), /churchinconversation.com\/traditions\//);
  person.toldWithin = null;
  world.people = [];
  assert.match(generate(c)(`tree/${person.id}.html`), /A person whose story no single tradition tells\./);
});

test('the map keeps person entries off the rivers and shows them through Who', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  const at = map.indexOf("const PERSON_IDS=new Set(DATA.movements.filter(m=>m.kind==='person')");
  assert.ok(at > 0);
  assert.ok(at < map.indexOf('const byId={}; DATA.movements.forEach'));
  assert.match(map, /const personEntries=DATA\.movements\.filter\(m=>PERSON_IDS\.has\(m\.id\)\);/);
  assert.match(map, /DATA\.edges=DATA\.edges\.filter\(e=>!PERSON_IDS\.has\(e\.from\)&&!PERSON_IDS\.has\(e\.to\)\);/);
  assert.match(map, /const WHO_TRAD_MAX=6, WHO_RIVER_MAX=4,/);
  assert.doesNotMatch(map, /data-view-btn=/);
});

test('Who and the connection lines are never shown together', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.match(map, /svg\.who-on \.edge-line,svg\.who-on \.edge-hit,svg\.who-on \.continues\{display:none!important\}/);
  assert.match(map, /if\(whoScope\)whoLinks\.suspend\(\);else whoLinks\.restore\(\);/);
  assert.match(map, /whoScope=null;whoLinks\.restore\(\);renderWho\(\);/);
  assert.match(map, /if\(whoLinks\.saved&&\(k==='links-all'\|\|k==='major'\|\|k\.startsWith\('family:'\)\)&&familyKeys\.some\(f=>!hidden\.has\(f\)\)\)\{whoLinks\.saved=null;clearWho\(\);\}/);
});

test('the map holds every tradition\'s people, every person\'s home tradition and card', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  const start = map.indexOf('const DATA = ') + 'const DATA = '.length;
  const data = JSON.parse(map.slice(start, map.indexOf('\n;\n', start)));
  const held = new Map(data.movements.map(m => [m.id, m]));
  for (const m of census.movements) {
    const h = held.get(m.id);
    assert.deepEqual(h.people, m.people, `${m.id}: people`);
    assert.equal(h.peopleNote, m.peopleNote, `${m.id}: peopleNote`);
    assert.equal(h.toldWithin, m.toldWithin, `${m.id}: toldWithin`);
    assert.deepEqual(h.card, m.card, `${m.id}: card`);
  }
});

test('a movement that names no one says why, in its own People section', () => {
  const c = structuredClone(census);
  const m = c.movements.find(x => x.kind !== 'person');
  m.people = [];
  m.peopleNote = 'The Library holds no words of its own leaders.';
  assert.match(generate(c)(`tree/${m.id}.html`), /<h2>People<\/h2>\s*<p class="people-note">The Library holds no words of its own leaders\.<\/p>/);
  delete m.peopleNote;
  assert.doesNotMatch(generate(c)(`tree/${m.id}.html`), /<h2>People<\/h2>/);
});

test('Who shows person entries only: named voices are not listed as people', () => {
  const c = structuredClone(census);
  const m = c.movements.find(x => x.kind !== 'person' && !x.people.some(p => p.person));
  m.people = [{ name: 'Named Voice', year: 100, voice: 0, source: { work: 'w', file: 'f', lines: '1', quote: 'q' } }];
  const page = generate(c)(`tree/${m.id}.html`);
  assert.doesNotMatch(page, /<h2>People<\/h2>/);
  assert.doesNotMatch(page, /Named Voice/);
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.match(map, /const WHO_ENTRIES_ONLY=true;/);
  assert.match(map, /if\(WHO_ENTRIES_ONLY&&!row\.person\)return;/);
});

test('every page states its review status in plain words', () => {
  const c = structuredClone(census);
  const [a, b] = c.movements;
  b.reviewStatus = 'scholar-reviewed';
  const read = generate(c);
  assert.match(read(`tree/${a.id}.html`), /<p class="review-status"><b>Review:<\/b> checked with AI tools\. No scholar or church partner has reviewed it yet\./);
  assert.match(read(`tree/${b.id}.html`), /<b>Review:<\/b> reviewed by a scholar\./);
});

test('a movement retired into another loses its page and redirects permanently', () => {
  const c = structuredClone(census);
  const [kept, gone] = c.movements;
  c.movements = c.movements.filter(m => m !== gone);
  c.edges = c.edges.filter(e => e.from !== gone.id && e.to !== gone.id);
  c.retiredMovements = [{ id: gone.id, date: '2031-01-01', reason: 'Merged.', redirectTo: kept.id }];
  const read = generate(c);
  assert.throws(() => read(`tree/${gone.id}.html`));
  assert.equal(read('_redirects'), `/tree/${gone.id} /tree/${kept.id} 301\n/tree/${gone.id}.html /tree/${kept.id} 301\n`);
});

test('the method page and the era 10 band say where the history ends, in the same words', () => {
  const line = "The tree's history runs to 2010. Movements since then will be added as they become history.";
  const page = generate(census)('method.html').replace(/&#039;/g, "'");
  assert.ok(page.includes(`<p>${line}</p>`));
  assert.ok(page.includes('<p>Nothing after 2010 is mapped yet.</p>'));
  assert.ok(page.includes('<h2>What the living mark means</h2>'));
  assert.ok(page.includes('<p>A living mark means one thing: the tradition is alive today, in 2026.'));
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.ok(map.includes(`10:${JSON.stringify(line)}`));
});

test('a retired movement with no redirect gets a retired page with only its census record', () => {
  const c = structuredClone(census);
  c.retiredMovements = [
    { id: 'gone-movement', name: 'Gone & Movement', date: '2026-11-08', reason: 'Its story falls after the tree ends.' },
    { id: 'merged-movement', name: 'Merged', date: '2026-11-08', reason: 'Merged.', redirectTo: census.movements[0].id },
  ];
  const read = generate(c);
  const page = read('tree/gone-movement.html');
  assert.match(page, /<div class="page" data-retired="true">/);
  assert.match(page, /<h1>Gone &amp; Movement<\/h1>/);
  assert.match(page, /<p>This entry was retired from the tree on November 8, 2026\.<\/p>/);
  assert.match(page, /<p>Its story falls after the tree ends\.<\/p>/);
  assert.match(page, /<header class="site-header">/);
  assert.match(page, /<meta name="robots" content="noindex">/);
  assert.doesNotMatch(page, /In Its Own Record|Sources<\/h2>/);
  assert.throws(() => read('tree/merged-movement.html'));
});

test('a cross-church movement shows its kind, and a church body shows none', () => {
  const movement = census.movements.find(m => m.kind === 'cross-church movement');
  const body = census.movements.find(m => m.kind === undefined);
  const read = generate(census);
  assert.match(read(`tree/${movement.id}.html`), /<p class="kind-label">A movement across churches<\/p>/);
  assert.doesNotMatch(read(`tree/${body.id}.html`), /class="kind-label"/);
});

test('the map draws cross-church movements in their own column, not over a river', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.doesNotMatch(map, /current-hatch|current-band|currentPath|striped band/);
  assert.match(map, /const churchBodies=DATA\.movements\.filter\(m=>!isAcross\(m\)\);/);
  assert.match(map, /const laneKeys=\[\.\.\.new Set\(churchBodies\.map\(m=>m\.laneOrder\)\)\]/);
  assert.match(map, /laneMembers\[k\]=churchBodies\.filter\(m=>m\.laneOrder===k\)/);
  assert.match(map, /if\(!a\|\|!b\|\|isAcross\(a\)\|\|isAcross\(b\)\)return;/);
});

test('the movements column sits left of the era rivers, its names reading leftward', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.match(map, /left=Math\.min\(left,g\.own\[k\]\[j\]-g\.half\[k\]\[j\]\)/);
  assert.match(map, /const x0=\(Number\.isFinite\(left\)\?left:70\)-ACROSS_GAP;/);
  assert.match(map, /m\._x=x0-tracks\[j\]\*ACROSS_TRACK;/);
  assert.match(map, /class:'across-lbl',x:m\._x-7,y:m\._labelY,'text-anchor':'end'/);
});

test('the Movements switch starts off and is remembered like the other switches', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.match(map, /<button type="button" class="chip" data-toggle="movements" aria-pressed="false">Movements<\/button>/);
  assert.match(map, /let movementsOn=false;\n\s*try\{movementsOn=localStorage\.getItem\('tree-movements'\)==='1';\}catch\(e\)\{\}/);
  assert.match(map, /localStorage\.setItem\('tree-movements',movementsOn\?'1':'0'\)/);
  assert.ok(map.includes('The Movements switch shows movements that ran across churches as thin lines beside their era, for the years they lasted.'));
});

test('ties come only from census links, and a movement line never runs under a later name', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.match(map, /acrossMovements\.forEach\(m=>\{\n\s*DATA\.edges\.forEach\(edg=>\{\n\s*if\(edg\.from!==m\.id&&edg\.to!==m\.id\)return;/);
  const src = map.match(/function acrossTracks\(items\)\{[\s\S]*?\n\}/)[0];
  const acrossTracks = new Function(`${src}; return acrossTracks;`)();
  const across = census.movements.filter(m => m.kind === 'cross-church movement');
  for (const era of new Set(across.map(m => m.era))) {
    const items = across.filter(m => m.era === era).sort((a, b) => a.start - b.start || a.end - b.end || a.id.localeCompare(b.id));
    const tracks = acrossTracks(items);
    items.forEach((m, i) => items.forEach((o, j) => {
      if (j >= i || o.end < m.start) return;
      assert.ok(tracks[j] < tracks[i], `${o.id} runs under the name of ${m.id}`);
    }));
  }
  assert.deepEqual(acrossTracks([{ start: 1900, end: 2000 }, { start: 1910, end: 1920 }, { start: 1930, end: 1940 }]), [0, 1, 1]);
  assert.deepEqual(acrossTracks([{ start: 1900, end: 1950 }, { start: 1910, end: 2000 }, { start: 1960, end: 1990 }]), [0, 1, 2]);
});

test('the Terms page is on both sites with the same text, and every tree footer links to it', () => {
  const read = generate(census);
  const strip = s => s.replace(/<[^>]+>/g, '').replace(/&rsquo;/g, '’').replace(/&#0?39;|'/g, '’').replace(/&amp;/g, '&').replace(/\s+/g, ' ').trim();
  const items = page => [...page.matchAll(/<(?:h2|p|li)>([\s\S]*?)<\/(?:h2|p|li)>/g)].map(m => strip(m[1]));
  const tree = read('terms.html');
  const cic = fs.readFileSync(path.join(root, 'cic-website/terms.html'), 'utf8');
  const treeMain = tree.slice(tree.indexOf('<div class="page">'), tree.indexOf('<footer'));
  const cicMain = cic.slice(cic.indexOf('<main'), cic.indexOf('</main>'));
  const terms = JSON.parse(fs.readFileSync(path.join(root, 'Build/tools/tree_site_pages.json'), 'utf8')).terms;
  for (const sec of terms.sections) {
    for (const line of [sec.heading, ...sec.paragraphs, ...(sec.list || []), ...(sec.after || [])]) {
      const text = strip(line.replace(/\[([^\]]+)\]\([^)]+\)/g, '$1'));
      assert.ok(items(treeMain).includes(text), `tree Terms is missing: ${text}`);
      assert.ok(items(cicMain).includes(text), `Church in Conversation Terms is missing: ${text}`);
    }
  }
  assert.match(read(`tree/${open.id}.html`), /<a href="\.\.\/terms.html">Terms<\/a>/);
  assert.ok(read('sitemap.xml').includes('<loc>https://www.churchfamilytree.com/terms.html</loc>'));
});
