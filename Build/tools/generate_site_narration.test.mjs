import { test } from 'node:test';
import assert from 'node:assert/strict';
import { storyText, sectionText, sitePieces, planPieces, parseArgs, fingerprint } from './generate_site_narration.mjs';

const story = `<h1 id="story-title" class="x">Two &amp; more   years.</h1>
<div class="story-body"><p>One <em>idea</em>.</p>\n<p>Second thought.</p></div>`;
const about = `<section class="page-section" id="mission"><p class="eyebrow">Mission</p><h2>The aim</h2><p>First.</p>
<div class="callout"><p class="label">Where we are</p><p>Now.</p></div></section>
<section class="page-section" id="convictions"><p class="eyebrow">Five</p><ol><li><h3>One title</h3><p>One body.</p></li></ol></section>`;

test('storyText: heading then each body paragraph, tags stripped, entities decoded', () => {
  assert.equal(storyText(story), 'Two & more years.\n\nOne idea.\n\nSecond thought.');
});

test('storyText: a page without the story structure is an error', () => {
  assert.throws(() => storyText('<p>nothing</p>'), /not found/);
});

test('sectionText: headings and paragraphs in page order, eyebrow label left out', () => {
  assert.equal(sectionText(about, 'mission'), 'The aim\n\nFirst.\n\nWhere we are\n\nNow.');
  assert.equal(sectionText(about, 'convictions'), 'One title\n\nOne body.');
  assert.throws(() => sectionText(about, 'nope'), /not found/);
});

test('sitePieces: the story first, then one piece per About section', () => {
  const full = ['mission', 'convictions', 'how-it-works', 'safety', 'about-us']
    .map((id) => `<section class="page-section" id="${id}"><h2>${id} heading</h2></section>`).join('');
  const pieces = sitePieces({ read: (f) => (f === 'story.html' ? story : full) });
  assert.deepEqual(pieces.map((p) => p.key), ['unfolding-story', 'about-mission', 'about-convictions', 'about-how-it-works', 'about-safety', 'about-about-us']);
  assert.equal(pieces[3].text, 'how-it-works heading');
  assert.throws(() => sitePieces({ read: (f) => (f === 'story.html' ? story : about) }), /not found/);
});

test('planPieces: skips a matching fingerprint, regenerates a changed one, --force and --only narrow', () => {
  const pieces = [{ key: 'a', text: 'one' }, { key: 'b', text: 'two' }];
  const manifest = { a: { hash: fingerprint('one') }, b: { hash: 'old' } };
  const exists = () => true;
  const plan = planPieces(pieces, { manifest, existsFn: exists });
  assert.deepEqual(plan.upToDate.map((p) => p.key), ['a']);
  assert.deepEqual(plan.toGenerate.map((p) => p.key), ['b']);
  assert.deepEqual(planPieces(pieces, { manifest, existsFn: exists, force: true }).toGenerate.map((p) => p.key), ['a', 'b']);
  assert.deepEqual(planPieces(pieces, { manifest, existsFn: exists, only: ['a'] }).upToDate.map((p) => p.key), ['a']);
  assert.deepEqual(planPieces(pieces, { manifest, existsFn: () => false }).toGenerate.map((p) => p.key), ['a', 'b']);
});

test('parseArgs: reads every paid setting and rejects unknown flags', () => {
  const o = parseArgs(['--voice-id', 'v', '--model', 'm', '--output-format', 'f', '--settings-json', '{}', '--only', 'a,b']);
  assert.deepEqual([o.voiceId, o.model, o.outputFormat, o.settingsJson, o.only], ['v', 'm', 'f', '{}', ['a', 'b']]);
  assert.throws(() => parseArgs(['--nope']), /unrecognized/);
});
