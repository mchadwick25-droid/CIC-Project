import { describe, expect, it } from 'vitest';
import { streamedReply, type StreamedSentence } from './streamedReply';

const CARD = { record_id: 'w.quote.song', record_type: 'quote', label: 'The new song', sources: [] };
const QUOTE = {
  record_id: 'w.quote.song', record_type: 'quote', world_key: 'w', confidence: null, repeat: false,
  kind: 'quote' as const, sentence_index: 1, char_start: 18, char_end: 38, surface: '"Look, the new song"',
};

const SENTENCES: StreamedSentence[] = [
  { index: 0, lead: '', text: 'We kept the bread.', text_start: 0, text_end: 18, elements: [], cards: [] },
  { index: 1, lead: '\n\n', text: 'Our teacher said: "Look, the new song".', text_start: 20, text_end: 59, elements: [QUOTE], cards: [CARD] },
];

describe('streamedReply', () => {
  it('is nothing until a sentence arrives', () => {
    expect(streamedReply([], 'w')).toBeNull();
  });

  it('rebuilds the reply so far with its paragraph breaks, at the offsets the plan uses', () => {
    const reply = streamedReply(SENTENCES, 'w')!;
    expect(reply.text).toBe('We kept the bread.\n\nOur teacher said: "Look, the new song".');
    for (const s of reply.transparency.sentences!) {
      expect(reply.text.slice(s.text_start!, s.text_end!)).toBe(SENTENCES[s.index].text);
    }
  });

  it('carries each sentence\'s marks and the cards they open', () => {
    const plan = streamedReply(SENTENCES, 'w')!.transparency;
    expect(plan.elements).toEqual([QUOTE]);
    expect(plan.references).toEqual([CARD]);
  });
});
