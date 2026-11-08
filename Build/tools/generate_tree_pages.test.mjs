import { test } from 'node:test';
import assert from 'node:assert/strict';
import { execFileSync } from 'node:child_process';
import fs from 'node:fs';
import os from 'node:os';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), '..', '..');
const census = JSON.parse(fs.readFileSync(path.join(root, 'cic-website/data/world-census.json'), 'utf8'));

function generate(c) {
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), 'tree-pages-'));
  const file = path.join(dir, 'census.json');
  fs.writeFileSync(file, JSON.stringify(c));
  execFileSync('node', [path.join(root, 'Build/tools/generate_tree_pages.mjs'), '--census', file, '--out', dir], { stdio: 'ignore' });
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

test('the support page carries the not-a-nonprofit line word for word', () => {
  const source = fs.readFileSync(path.join(root, 'cic-website/support.html'), 'utf8');
  const line = source.match(/<p class="fine-print">(Church in Conversation is part of Faithways Studio[^<]*)<\/p>/)[1];
  const page = fs.readFileSync(path.join(root, 'cft-website/support.html'), 'utf8');
  assert.ok(page.includes(`<p>${line}</p>`));
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
  assert.match(page, /The tree shows 12 links of six kinds\./);
  assert.match(page, new RegExp(`The tree covers ${c.movements.length} movements\\.`));
});
