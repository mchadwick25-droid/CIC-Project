/**
 * The reply so far while the voice is still writing it, built from the
 * engine's "sentence" stream events (engine/m4/sentence_stream.py). Each
 * sentence carries the text before it (`lead`), its offsets in the finished
 * reply, and the quote and story marks the finished plan gives it, so the
 * partial reply renders through the same element renderer as the finished
 * one. The finished turn's plan replaces this when it arrives.
 */
import type { SourceCard, TransparencyElement, TransparencyPlan } from '../types/conversation';

export interface StreamedSentence {
  index: number;
  lead: string;
  text: string;
  text_start: number | null;
  text_end: number | null;
  elements: TransparencyElement[];
  cards: SourceCard[];
}

export function streamedReply(sentences: StreamedSentence[], worldKey: string): { text: string; transparency: TransparencyPlan } | null {
  if (sentences.length === 0) return null;
  let text = '';
  const cards = new Map<string, SourceCard>();
  for (const sentence of sentences) {
    if (sentence.text_start !== null) text += sentence.lead + sentence.text;
    for (const card of sentence.cards) cards.set(card.record_id, card);
  }
  return {
    text,
    transparency: {
      world_key: worldKey,
      sentences: sentences.map(({ index, text_start, text_end }) => ({ index, text_start, text_end })),
      elements: sentences.flatMap((sentence) => sentence.elements),
      references: [...cards.values()],
      end_references: [],
      unverified_claims: { count: 0, sentence_indexes: [] },
    },
  };
}
