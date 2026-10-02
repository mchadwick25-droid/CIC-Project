import { test } from 'node:test';
import assert from 'node:assert/strict';
import { storyText, parseArgs, fingerprint } from './generate_site_narration.mjs';

const html = `<h1 id="story-title" class="x">Two &amp; more   years.</h1>
<div class="story-body"><p>One <em>idea</em>.</p>\n<p>Second&nbsp;thought.</p></div>`;

test('storyText: heading then each body paragraph, tags stripped, entities decoded', () => {
  assert.ok(storyText(html).startsWith('Two & more years.\n\nOne idea.'));
});

test('storyText: a page without the story structure is an error', () => {
  assert.throws(() => storyText('<p>nothing</p>'), /not found/);
});

test('parseArgs: reads every paid setting and rejects unknown flags', () => {
  const o = parseArgs(['--voice-id', 'v', '--model', 'm', '--output-format', 'f', '--settings-json', '{}']);
  assert.deepEqual([o.voiceId, o.model, o.outputFormat, o.settingsJson], ['v', 'm', 'f', '{}']);
  assert.throws(() => parseArgs(['--nope']), /unrecognized/);
});

test('fingerprint: stable and text-sensitive', () => {
  assert.equal(fingerprint('a'), fingerprint('a'));
  assert.notEqual(fingerprint('a'), fingerprint('b'));
});
