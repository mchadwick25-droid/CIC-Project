import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import crypto from 'node:crypto';
import vm from 'node:vm';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const census = JSON.parse(fs.readFileSync(path.join(root, 'cic-website/data/world-census.json'), 'utf8'));

function generate(c, audio = null, live = true) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'tree-pages-'));
  const file = path.join(dir, 'census.json');
  fs.writeFileSync(file, JSON.stringify(c));
  execFileSync('node', [path.join(root, 'Build/tools/generate_tree_pages.mjs'), '--census', file, '--out', dir, ...(audio ? ['--audio', audio] : []), ...(live ? ['--conversations-live'] : [])], { stdio: 'ignore' });
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

test('while conversations are not live, an open world names its Representative with no link to Church in Conversation', () => {
  const page = generate(census, null, false)(`tree/${open.id}.html`);
  assert.doesNotMatch(page, /churchinconversation.com\/traditions\//);
  assert.match(page, new RegExp(`<p class="door-quiet">Conversations with ${open.entry.representativeName} are coming soon to Church in Conversation.</p>`));
});

test('the map and the tree pages agree on whether conversations are live', () => {
  const site = JSON.parse(fs.readFileSync(path.join(root, 'Build/tools/tree_site_pages.json'), 'utf8'));
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.match(map, new RegExp(`const CONVERSATIONS_LIVE=${site.conversationsLive === true};`));
  const page = fs.readFileSync(path.join(root, `cft-website/tree/${open.id}.html`), 'utf8');
  assert.equal(/churchinconversation.com\/traditions\//.test(page), site.conversationsLive === true);
});

test('with every world closed, built worlds show only the quiet line', () => {
  const closed = structuredClone(census);
  closed.movements.forEach(m => { m.publicOpen = false; });
  const page = generate(closed)(`tree/${open.id}.html`);
  assert.doesNotMatch(page, /churchinconversation.com\/traditions\//);
  assert.match(page, /<p class="door-quiet"><a href="https:\/\/churchinconversation.com\/">Church in Conversation<\/a>, from the same team.<\/p>/);
});

test('the support page says who publishes it and that payments are not tax-deductible', () => {
  const page = fs.readFileSync(path.join(root, 'cft-website/support.html'), 'utf8');
  assert.match(page, /Published by Faithways Studio, Inc\., a Colorado public benefit corporation\./);
  assert.match(page, /not charitable donations\. They are not tax-deductible\./);
  assert.match(page, />Support once<\/a><a href="[^"]+">Support monthly<\/a>/);
})

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
  assert.doesNotMatch(match, /not a recording/);
  for (const stale of [withManifest({ ...base, text_sha256: sha('older text') }), withManifest(base), withManifest(null)]) {
    assert.doesNotMatch(stale, /class="narration"/);
    assert.doesNotMatch(stale, /narration-player\.js/);
  }
});

test('the Listen block is labeled as the audio brief, with its length from the recording', () => {
  const m = census.movements.find(x => x.longDescription && !fs.existsSync(path.join(root, `cic-website/data/worlds/${x.id}.json`)));
  const sha = crypto.createHash('sha256').update(m.longDescription, 'utf8').digest('hex');
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'tree-audio-'));
  fs.writeFileSync(path.join(dir, 'manifest.json'), JSON.stringify({ [m.id]: { file: `${m.id}.mp3`, bytes: 1200000, outputFormat: 'mp3_44100_64', text_sha256: sha } }));
  assert.match(generate(census, dir)(`tree/${m.id}.html`), /<p class="narration-label">Audio Brief · Narrated Edition <span>2:30<\/span><\/p>/);
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

test('the method page says the narrated briefs are a synthesized voice reading the card text', () => {
  const page = generate(census)('method.html');
  assert.match(page, /<h2>The narrated briefs<\/h2>/);
  assert.match(page, /read by a synthesized voice, made with the ElevenLabs text-to-speech service\. No person recorded it\./);
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
  assert.ok(sitemap.includes('<loc>https://www.churchfamilytree.com/method</loc>'));
  assert.ok(sitemap.includes('<loc>https://www.churchfamilytree.com/data</loc>'));
});

test('the about page counts traditions, rivers, eras and links from the census', () => {
  const c = structuredClone(census);
  withLinks(c, 12);
  const traditions = c.movements.filter(m => !m.kind);
  const rivers = new Set(traditions.map(m => m.laneOrder)).size;
  const inFull = traditions.filter(m => m.status === 'Built & Live').length;
  const page = generate(c)('about.html');
  assert.match(page, /The tree shows 12 links of seven kinds\./);
  assert.match(page, new RegExp(`The tree maps ${traditions.length} church traditions, and the councils, people and stories that shaped them\\.`));
  assert.match(page, new RegExp(`The traditions flow in ${rivers} rivers, across ${c.eras.length} eras\\.`));
  assert.match(page, new RegExp(`The tree tells ${inFull} traditions in full`));
  assert.match(page, new RegExp(`<meta name="description" content="[^"]*with ${traditions.length} church traditions`));
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
  assert.match(map, /const RIVER_WHO_MAX=5, TRAD_WHO_MAX=4,/);
  assert.doesNotMatch(map, /data-view-btn=/);
});

test('Who and the connection lines are never shown together', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.match(map, /svg\.who-on \.edge-line,svg\.who-on \.edge-hit,svg\.who-on \.continues\{display:none!important\}/);
  assert.match(map, /function setWho\(scope,opts\)\{\n  clearConnections\(\);/);
  assert.match(map, /function showConnections\(m,line\)\{\n  clearConnections\(\); if\(whoScope\)clearWho\(\);/);
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
    assert.deepEqual(h.council, m.council, `${m.id}: council`);
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
  const line = "The map runs to about 2010. Traditions that began after that will be added once enough time has passed.";
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
  assert.match(page, /<main class="page" id="content" data-retired="true">/);
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

test('there is no Movements switch: a movement across churches shows while a river it touches is on, and always when it touches none', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.doesNotMatch(map, /data-toggle="movements"/);
  assert.match(map, /g\.classList\.toggle\('across-out',!!ls\.size&&!\[\.\.\.ls\]\.some\(k=>!laneOff\(k\)\)\)/);
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
  const treeMain = tree.slice(tree.indexOf('<main class="page" id="content">'), tree.indexOf('<footer'));
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
  assert.ok(read('sitemap.xml').includes('<loc>https://www.churchfamilytree.com/terms</loc>'));
});

test('the tree serves its own copy of the license page, with every section of the Church in Conversation page', () => {
  const read = generate(census);
  const tree = read('license.html');
  const cic = fs.readFileSync(path.join(root, 'cic-website/license.html'), 'utf8');
  const headings = page => [...page.matchAll(/<h2>([\s\S]*?)<\/h2>/g)].map(m => m[1]);
  assert.ok(headings(cic).length > 10);
  assert.deepEqual(headings(tree), headings(cic));
  assert.ok(tree.includes('Ministry and Scholarship Permission'));
  assert.match(read(`tree/${open.id}.html`), /<a href="\.\.\/license.html">License<\/a>/);
  assert.ok(read('sitemap.xml').includes('<loc>https://www.churchfamilytree.com/license</loc>'));
});

test('a major council page shows its kind, its record, its traditions and its Who', () => {
  const council = census.movements.find(m => m.id === 'council-of-nicaea-325');
  const page = generate(census)(`tree/${council.id}.html`);
  assert.match(page, /<p class="kind-label">Major council<\/p>/);
  assert.match(page, /<h2>About This Council<\/h2>/);
  for (const h of ['Why They Met', 'Who Came', 'What They Decided', 'What Came of It', 'Traditions It Touched', 'Who', 'Whose Account We Have', 'What Is Uncertain', 'Sources']) {
    assert.match(page, new RegExp(`<h2>${h}</h2>`), h);
  }
  assert.match(page, /class="part-group">Gathered</);
  assert.match(page, /class="part-group">Condemned</);
  assert.match(page, /<a href="arius\.html">Arius<\/a> · /);
  assert.match(page, /class="verdict">Not yet assessed<\/span>/);
  assert.match(page, /<p class="source-group">From the council<\/p>/);
  assert.doesNotMatch(page, /No sources recorded/);
  assert.doesNotMatch(page, /<h2>In Its Own Record<\/h2>/);
  assert.doesNotMatch(page, /class="told-within"/);
});

test('a person page shows the card: facts, key works, legacy, councils, what is uncertain and sources in two groups', () => {
  const read = generate(census);
  const page = read('tree/arius.html');
  assert.match(page, /<dt>Known for<\/dt>/);
  assert.match(page, /<h2>Key Works<\/h2>/);
  assert.match(page, /<h2>Legacy<\/h2>/);
  assert.match(page, /<h2>At Major Councils<\/h2>[\s\S]*council-of-nicaea-325\.html/);
  assert.match(page, /<h2>What Is Uncertain<\/h2>/);
  assert.match(page, /<p class="source-group">Their own words<\/p>/);
  assert.match(page, /<p class="source-group">Written about them<\/p>/);
  assert.doesNotMatch(page, /No sources recorded/);
  assert.match(read('tree/josephus.html'), /<p class="kind-label">Outside witness<\/p>/);
  assert.doesNotMatch(page, /<p class="kind-label">Outside witness<\/p>/);
});

test('a page with nothing in its own record leaves the record heading out', () => {
  assert.doesNotMatch(generate(census)('tree/bede-of-jarrow.html'), /<h2>In Its Own Record<\/h2>/);
});

test('the map draws major councils in their own column, off the rivers, and a council opens its own card', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.match(map, /const councilEntries=DATA\.movements\.filter\(m=>m\.kind===COUNCIL_KIND\);/);
  assert.match(map, /DATA\.movements=DATA\.movements\.filter\(m=>m\.kind!==COUNCIL_KIND\);/);
  assert.match(map, /\[COUNCIL_KIND\]:'Major council'/);
  assert.match(map, /if\(councilById\[m\.id\]\)\{openCouncilCard\(m\);return;\}/);
  assert.match(map, /const x0=Math\.min\(\.\.\.cols\.map\(c=>c\.left\)\)-COUNCIL_GAP;/);
  assert.match(map, /c\._y=Math\.max\(yearToY\(c\.start\),lastY\+COUNCIL_ROW\)/);
  assert.match(map, /cap\.textContent='Major councils';/);
});

test('Who is a mark: a group figure with a count for each river in each era, and a single figure with a count beside each tradition, even for one person', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.match(map, /class:'who-pill river-pill'/);
  assert.match(map, /class:'who-pill prof-pill'/);
  const river = map.slice(map.indexOf('function renderWhoPills'), map.indexOf('function whoFigure'));
  assert.match(river, /groupGlyph\(\)/);
  assert.match(river, /t\.textContent=String\(n\)/);
  assert.doesNotMatch(river, /n===1\?''/);
  const figure = map.slice(map.indexOf('function whoFigure'), map.indexOf('function setWhoMark'));
  assert.match(figure, /personGlyph/);
  assert.match(figure, /cn\.textContent=String\(n\)/);
  assert.doesNotMatch(figure, /groupGlyph/);
  assert.doesNotMatch(map.slice(map.indexOf('function renderWhoPills'), map.indexOf('function setWhoMark')), /textContent='Who'/);
});

test('the map\'s own script parses', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  const open = map.indexOf('<script>\n"use strict";');
  assert.ok(open > 0);
  const code = map.slice(open + '<script>'.length, map.indexOf('</script>', open));
  assert.doesNotThrow(() => new vm.Script(code));
});

test('a person card with printed originals shows them, and its references, below the brief', () => {
  const m = census.movements.find(x => x.card && x.card.quotationOriginals && x.card.quotationOriginals.length);
  const page = generate(census)(`tree/${m.id}.html`);
  assert.match(page, /<p class="quotes-note">Quotations are given in our modern English\. The printed wording of each is below\.<\/p><details class="quotes-panel"><summary>Quotations and references<\/summary>/);
  assert.ok(page.indexOf('class="reading"') < page.indexOf('class="quotes-panel"'));
  const e = m.card.quotationOriginals[0];
  assert.ok(page.includes(e.printed.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;').replace(/'/g, '&#039;')));
  assert.match(page, /<p class="source-group">References<\/p>/);
  const c = structuredClone(census);
  const n = c.movements.find(x => x.id === m.id);
  delete n.card.quotationOriginals; delete n.card.briefReferences;
  assert.doesNotMatch(generate(c)(`tree/${m.id}.html`), /quotes-panel"|quotes-note"/);
});

test('the map card shows the printed originals and references below the brief, collapsed', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  assert.match(map, /function quotesPanel\(card\)\{/);
  assert.match(map, /<details class="sources-panel quotes-panel"><summary>Quotations and references<\/summary>/);
  assert.match(map, /read=briefTextHTML\(p\.longDescription\);\n    if\(card\.quotationOriginals&&card\.quotationOriginals\.length\)read\+='<p class="quotes-note">Quotations are given in our modern English\. The printed wording of each is below\.<\/p>';\n    read\+=quotesPanel\(card\);/);
  assert.match(map, /folds\.push\(foldHTML\('Read the brief',readLen,\[\['',read\]\]\)\);/);
});

test('a council page shows how it worked, the printed wording behind its quotations, and its story with recording', () => {
  // Its own recordings folder: an empty tree manifest, and a docstory manifest made from the story's current text.
  const nicaea = census.movements.find(m => m.id === 'council-of-nicaea-325');
  const audio = path.join(fs.mkdtempSync(path.join(os.tmpdir(), 'tree-audio-')), 'tree');
  fs.mkdirSync(audio); fs.mkdirSync(path.join(path.dirname(audio), 'docstories'));
  fs.writeFileSync(path.join(audio, 'manifest.json'), '{}');
  const hash = crypto.createHash('sha256').update(nicaea.documentedStories[0].text).digest('hex').slice(0, 16);
  fs.writeFileSync(path.join(path.dirname(audio), 'docstories', 'manifest.json'), JSON.stringify({ 'council-of-nicaea-325-0': { hash } }));
  const page = generate(census, audio)('tree/council-of-nicaea-325.html');
  assert.match(page, /<h2>How the Council Worked<\/h2>/);
  assert.match(page, /<details class="quotes-panel"><summary>Quotations and references<\/summary>/);
  assert.ok(page.indexOf('class="reading"') < page.indexOf('class="quotes-panel"'));
  assert.match(page, /<h2>How Nicaea decided<\/h2><div class="narration"><audio controls preload="none" src="\.\.\/audio\/docstories\/council-of-nicaea-325-0\.mp3">/);
  const c = structuredClone(census);
  c.movements.find(m => m.id === 'council-of-nicaea-325').documentedStories[0].text += ' Changed.';
  assert.doesNotMatch(generate(c, audio)('tree/council-of-nicaea-325.html'), /audio\/docstories\/council-of-nicaea-325-0\.mp3/);
});

test('every page names its own address for search engines, and the sitemap lists those addresses', () => {
  const read = generate(structuredClone(census));
  const m = census.movements.find(x => !x.kind);
  const page = read(`tree/${m.id}.html`);
  assert.match(page, new RegExp(`<link rel="canonical" href="https://www.churchfamilytree.com/tree/${m.id}">`));
  assert.match(page, /<meta property="og:image" content="https:\/\/www.churchfamilytree.com\/share\/church-family-tree.jpg">/);
  assert.match(read('about.html'), /<link rel="canonical" href="https:\/\/www.churchfamilytree.com\/about">/);
  assert.match(read('license.html'), /<link rel="canonical" href="https:\/\/www.churchfamilytree.com\/license">/);
  const sitemap = read('sitemap.xml');
  assert.ok(sitemap.includes('<loc>https://www.churchfamilytree.com/about</loc>'));
  assert.ok(!sitemap.includes('.html</loc>'));
});

test('the page for a missing address links back with absolute paths and asks not to be indexed', () => {
  const page = generate(structuredClone(census))('404.html');
  assert.match(page, /<h1>Page not found<\/h1>/);
  assert.match(page, /<meta name="robots" content="noindex">/);
  assert.doesNotMatch(page, /(href|src)="(?!\/|https?:|#|mailto:)/);
});

const DESCENT = new Set(['gave rise to', 'continued as']);
const kindOf = (id) => (census.movements.find(m => m.id === id) || {}).kind || 'tradition';
const bothTraditions = (e) => kindOf(e.from) === 'tradition' && kindOf(e.to) === 'tradition';
const descentEdges = census.edges.filter(e => DESCENT.has(e.type) && bothTraditions(e));
const isTrad = (m) => kindOf(m.id) === 'tradition';
const withLine = census.movements.find(m => isTrad(m) && descentEdges.some(e => e.to === m.id) && descentEdges.some(e => e.from === m.id));
const noLine = census.movements.find(m => isTrad(m) && !descentEdges.some(e => e.from === m.id || e.to === m.id));
const between = (page, from, to) => { const a = page.indexOf(from); const b = page.indexOf(to, a); return page.slice(a, b < 0 ? undefined : b); };

test('a tradition page shows a lineage line, then its direct line, then everything else', () => {
  const page = generate(census)(`tree/${withLine.id}.html`);
  assert.match(page, /<nav class="lineage-strip" aria-label="Direct line of descent">/);
  assert.ok(page.indexOf('class="lineage-strip"') < page.indexOf('<h2>About This Movement</h2>'));
  assert.match(page, /<h2>Connections<\/h2>/);
  const at = (h) => page.indexOf(`<h3>${h}</h3>`);
  assert.ok(at('Descended from') > 0 && at('Descended from') < at('Direct descendants'));
  const parents = between(page, '<h3>Descended from</h3>', '<h3>Direct descendants</h3>');
  const kids = between(page, '<h3>Direct descendants</h3>', 'lineage-rest-heading');
  for (const e of descentEdges.filter(x => x.to === withLine.id)) assert.ok(parents.includes(`href="${e.from}.html"`), `parent ${e.from}`);
  for (const e of descentEdges.filter(x => x.from === withLine.id)) assert.ok(kids.includes(`href="${e.to}.html"`), `descendant ${e.to}`);
  assert.match(parents, /class="lineage-kind">(continues|grew out of)</);
});

test('a tradition with no direct line says so, and has no lineage line', () => {
  const page = generate(census)(`tree/${noLine.id}.html`);
  assert.match(page, /<p class="lineage-none">No direct parent is recorded\.<\/p>/);
  assert.match(page, /<p class="lineage-none">No direct descendant is recorded\./);
  assert.doesNotMatch(page, /<nav class="lineage-strip"/);
});

test('people, councils and movements across churches keep the plain list of links', () => {
  const read = generate(census);
  const across = census.movements.find(m => m.kind === 'cross-church movement' && census.edges.some(e => e.from === m.id || e.to === m.id));
  for (const id of ['arius', 'council-of-nicaea-325', across.id]) {
    const page = read(`tree/${id}.html`);
    assert.doesNotMatch(page, /Descended from|Direct descendants|class="lineage-strip"/, id);
  }
});

test('a descent link to a person or a movement is not listed as a direct descendant', () => {
  const odd = census.edges.find(e => DESCENT.has(e.type) && !bothTraditions(e) && kindOf(e.from) === 'tradition');
  const page = generate(census)(`tree/${odd.from}.html`);
  const direct = between(page, '<h3>Direct descendants</h3>', 'lineage-rest-heading');
  assert.ok(!direct.includes(`href="${odd.to}.html"`), 'it must sit with the other links');
  assert.ok(page.includes(`href="${odd.to}.html"`));
});

test('a break has no direction, as the Method page says', () => {
  const brk = census.edges.find(e => e.type === 'broke with' && bothTraditions(e));
  const page = generate(census)(`tree/${brk.from}.html`);
  assert.match(page, /<h3>Broke With<\/h3>/);
  assert.doesNotMatch(page, /this broke with|broke with this/);
});

test('the map card and the tradition pages sort links the same way', () => {
  const map = fs.readFileSync(path.join(root, 'cft-website/index.html'), 'utf8');
  const gen = fs.readFileSync(path.join(root, 'Build/tools/generate_tree_pages.mjs'), 'utf8');
  assert.match(map, /const DESCENT_TYPES=new Set\(\['gave rise to','continued as'\]\)/);
  assert.match(gen, /const DESCENT_TYPES = new Set\(\['gave rise to', 'continued as'\]\)/);
  for (const h of ['Descended from', 'Direct descendants', 'Influence, argument and contact']) {
    assert.ok(map.includes(h), `the map card lacks "${h}"`);
    assert.ok(gen.includes(h), `the page generator lacks "${h}"`);
  }
  assert.ok(map.includes('Broke with') && gen.includes('Broke With'));
  const method = JSON.parse(fs.readFileSync(path.join(root, 'Build/tools/tree_site_pages.json'), 'utf8')).method.sections;
  assert.ok(method.some(s => s.heading === 'Direct descendants and influence'));
});
