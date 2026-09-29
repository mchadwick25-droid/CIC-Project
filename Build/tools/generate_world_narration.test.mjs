import { test } from 'node:test';
import assert from 'node:assert/strict';
import { parseArgs, splitParagraphs, worldPieces, MAX_CHARS_PER_REQUEST } from './generate_world_narration.mjs';

test('splitParagraphs: one part when it fits; balanced parts, in order, none over the limit', () => {
  assert.equal(splitParagraphs(['a'.repeat(100)]).length, 1);
  const paras = [594, 674, 649, 642, 475, 643, 800, 814].map((n) => 'x'.repeat(n));
  const parts = splitParagraphs(paras);
  assert.equal(parts.length, 2);
  assert.ok(parts.every((p) => p.length <= MAX_CHARS_PER_REQUEST));
  assert.equal(parts.join('\n\n'), paras.join('\n\n'));
});

test('worldPieces: story, documented stories and legacy only; blank text skipped', () => {
  const compiled = { orientation: {
    story: [{ text: 'one' }, { text: 'two' }],
    documented_stories: [{ text: 'ds0', teaser: 'no' }, { text: ' ' }, { text: 'ds2' }],
    legacy: [{ text: 'leg' }], voices: [{ bio: 'skip' }],
  } };
  assert.deepEqual(worldPieces(compiled).map((p) => p.key), ['story', 'docstory-0', 'docstory-2', 'legacy']);
});

test('parseArgs: paid settings only from flags', () => {
  const o = parseArgs(['--world', 'w', '--voice-id', 'v', '--model', 'm', '--api-speed', '1.12', '--tempo', '1.15', '--settings-json', '{}']);
  assert.deepEqual([o.world, o.voiceId, o.model, o.apiSpeed, o.tempo], ['w', 'v', 'm', 1.12, 1.15]);
  assert.throws(() => parseArgs(['--bogus']), /unrecognized/);
});
