import { test } from 'node:test';
import assert from 'node:assert/strict';
import { cardPieces } from './generate_card_narration.mjs';

const census = {
  movements: [
    { id: 'a', status: 'Built & Live', entry: { representativeName: 'A', summary: 'One   idea.\n Two.' } },
    { id: 'b', status: 'Built & Live', entry: { representativeName: 'B' } },
    { id: 'c', status: 'Planned', entry: { representativeName: 'C', summary: 'Not built.' } },
  ],
};

test('cardPieces: one piece per built, live world with a summary, spacing collapsed', () => {
  assert.deepEqual(cardPieces(census), [{ key: 'a', text: 'One idea. Two.' }]);
});
