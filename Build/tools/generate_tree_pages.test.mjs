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
