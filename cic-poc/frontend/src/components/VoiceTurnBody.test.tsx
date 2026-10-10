/**
 * The element renderer: every mark placed by the engine's own offsets,
 * one mark per grounded element, general references at the end. Plans here are built by hand
 * in engine.m4.transparency_plan's own shape, so the positions under test
 * are pinned exactly. VoiceTurnBody.legacy-default.test.tsx covers the
 * legacy renderer, still used for a turn whose plan predates elements.
 */
import { fireEvent, render } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import type { Citation, FigureUsed, GlossUsed, SourceCard, TransparencyElement, TransparencyPlan } from '../types/conversation';
import { END_REFERENCES_HEADING, QUOTE_CARD_PHRASE, pendingMarkWording } from '../lib/markCopy';

vi.mock('../lib/flags', () => ({ useAnchorRenderer: true }));
const { VoiceTurnBody } = await import('./VoiceTurnBody');

function card(recordId: string, recordType: string, label: string, confidence?: Record<string, unknown> | null): SourceCard {
  return { record_id: recordId, record_type: recordType, label, sources: [], confidence };
}

function figure(id: string, matchedName: string): FigureUsed {
  return { id, matched_name: matchedName, names: [], bridge_line: null, dates: {}, sourced_by: [] };
}

function gloss(id: string, matchedName: string): GlossUsed {
  return { id, matched_name: matchedName, plain_meaning: null, quick_meaning: null, translational_sense: null, false_friend: [], sourced_by: [] };
}

// Joins sentences with one space, the way the engine's own reply text
// reads, and returns each sentence's span in it.
function turn(sentences: string[]) {
  const text = sentences.join(' ');
  let cursor = 0;
  const spans = sentences.map((s, index) => {
    const start = text.indexOf(s, cursor);
    cursor = start + s.length;
    return { index, text_start: start, text_end: start + s.length };
  });
  return { text, spans, sentences };
}

// An element covering `surface` inside sentence `index` (first occurrence),
// or the whole sentence when surface is omitted.
function el(
  sentences: string[],
  index: number,
  recordId: string,
  kind: TransparencyElement['kind'],
  surface?: string,
  extra: Partial<TransparencyElement> = {}
): TransparencyElement {
  const sentence = sentences[index];
  const start = surface === undefined ? 0 : sentence.indexOf(surface);
  const end = surface === undefined ? sentence.length : start + surface.length;
  return {
    record_id: recordId,
    record_type: kind === 'term' ? 'term' : kind,
    world_key: 'fix',
    confidence: null,
    repeat: false,
    kind,
    sentence_index: index,
    char_start: start,
    char_end: end,
    surface: sentence.slice(start, end),
    ...extra,
  };
}

function plan(spans: TransparencyPlan['sentences'], elements: TransparencyElement[], references: SourceCard[], endReferences: SourceCard[] = []): TransparencyPlan {
  return { world_key: 'fix', sentences: spans, elements, references, end_references: endReferences, unverified_claims: { count: 0, sentence_indexes: [] } };
}

// Reads the rendered body as text with every ✲ mark shown as [*] and every
// word mark as {word}, so a test can see exactly where each mark sits.
function markedText(container: HTMLElement): string {
  const body = container.querySelector('.turn__body > div')!;
  const walk = (node: Node): string => {
    if (node.nodeType === Node.TEXT_NODE) return node.textContent ?? '';
    const element = node as HTMLElement;
    if (element.classList?.contains('citation-mark')) return '[*]';
    if (element.classList?.contains('name-bridge-mark')) return `{${element.textContent}}`;
    return Array.from(node.childNodes).map(walk).join('');
  };
  return walk(body).replace(/\s*\[\*\]/g, '[*]');
}

describe('VoiceTurnBody - element renderer', () => {
  it('a term and a quote in one sentence get two marks in two places, not a stack at the end', () => {
    const quoted = '"a clear and unmistakeable proof"';
    const { text, spans, sentences } = turn([`By allegoria he read it, and called it ${quoted} of the truth.`]);
    const quoteCard = card('fix.quote.proof', 'quote', 'Proof — Origen');
    const transparency = plan(spans, [el(sentences, 0, 'fix.term.allegoria', 'term', 'allegoria'), el(sentences, 0, 'fix.quote.proof', 'quote', quoted)], [quoteCard]);

    const { container } = render(
      <VoiceTurnBody text={text} citations={[]} glosses={[gloss('fix.term.allegoria', 'allegoria')]} transparency={transparency} />
    );

    expect(markedText(container)).toBe(`By {allegoria} he read it, and called it ${quoted}[*] of the truth.`);
    expect(container.querySelector('.turn__general-references')).toBeNull();
  });

  it('a story mark ends its telling, after the sentence\'s own punctuation', () => {
    const { text, spans, sentences } = turn(['Part one.', 'Part two.', 'Something else.']);
    const storyCard = card('fix.story.a', 'story', 'Story A');
    const transparency = plan(spans, [el(sentences, 1, 'fix.story.a', 'story')], [storyCard]);

    const { container } = render(<VoiceTurnBody text={text} citations={[]} transparency={transparency} />);

    expect(markedText(container)).toBe('Part one. Part two.[*] Something else.');
  });

  it('one mark per element, never merged: two stories ending on one sentence are two marks', () => {
    const { text, spans, sentences } = turn(['Both were told here.']);
    const a = card('fix.story.a', 'story', 'Story A');
    const b = card('fix.story.b', 'story', 'Story B');
    const transparency = plan(spans, [el(sentences, 0, 'fix.story.a', 'story'), el(sentences, 0, 'fix.story.b', 'story')], [a, b]);

    const { container } = render(<VoiceTurnBody text={text} citations={[]} transparency={transparency} />);

    expect(container.querySelectorAll('.story-mark')).toHaveLength(2);
  });

  it('witness and gravity records are general references at the end, never inline', () => {
    const { text, spans } = turn(['A claim grounded twice over.']);
    const witness = card('fix.dw.a', 'doctrinal_witness', 'Witness A');
    const gravity = card('fix.gravity.b', 'gravity', 'Gravity B');
    const transparency = plan(spans, [], [witness, gravity], [witness, gravity]);

    const { container } = render(<VoiceTurnBody text={text} citations={[]} transparency={transparency} />);

    expect(container.querySelector('.citation-mark')).toBeNull();
    expect(markedText(container)).toBe('A claim grounded twice over.');
    const labels = Array.from(container.querySelectorAll('.turn__general-references .turn__sources-label')).map((n) => n.textContent);
    expect(labels).toEqual(['Witness A', 'Gravity B']);
    // The list sits after the running text.
    const body = container.querySelector('.turn__body')!;
    expect(body.lastElementChild?.classList.contains('turn__general-references')).toBe(true);
  });

  it('text between and after sentences is kept exactly, marks or no marks', () => {
    const text = 'First sentence.\n\nSecond sentence, after a paragraph break.';
    const spans = [
      { index: 0, text_start: 0, text_end: 15 },
      { index: 1, text_start: 17, text_end: text.length },
    ];
    const storyCard = card('fix.story.a', 'story', 'Story A');
    const transparency = plan(spans, [el(['First sentence.'], 0, 'fix.story.a', 'story')], [storyCard]);

    const { container } = render(<VoiceTurnBody text={text} citations={[]} transparency={transparency} />);

    expect(markedText(container)).toBe('First sentence.[*]\n\nSecond sentence, after a paragraph break.');
  });

  it('a repeat element renders the lighter .citation-mark--repeat mark', () => {
    const { text, spans, sentences } = turn(['Told here.', 'Something else.', 'Told again.']);
    const storyCard = card('fix.story.a', 'story', 'Story A');
    const transparency = plan(spans, [el(sentences, 0, 'fix.story.a', 'story'), el(sentences, 2, 'fix.story.a', 'story', undefined, { repeat: true })], [storyCard]);

    const { container } = render(<VoiceTurnBody text={text} citations={[]} transparency={transparency} />);

    const marks = container.querySelectorAll('.story-mark');
    expect(marks).toHaveLength(2);
    expect(marks[0].classList.contains('citation-mark--repeat')).toBe(false);
    expect(marks[1].classList.contains('citation-mark--repeat')).toBe(true);
  });

  it('Contested or Inferential-Thin renders hollow; a solid claim does not', () => {
    const { text, spans, sentences } = turn(['A thin story.', 'A solid story.']);
    const thin = card('fix.story.thin', 'story', 'Thin');
    const solid = card('fix.story.solid', 'story', 'Solid');
    const transparency = plan(
      spans,
      [
        el(sentences, 0, 'fix.story.thin', 'story', undefined, { confidence: { formation_confidence: 'Inferential-Thin' } }),
        el(sentences, 1, 'fix.story.solid', 'story', undefined, { confidence: { formation_confidence: 'Documented' } }),
      ],
      [thin, solid]
    );

    const { container } = render(<VoiceTurnBody text={text} citations={[]} transparency={transparency} />);

    const marks = container.querySelectorAll('.story-mark');
    expect(marks[0].classList.contains('citation-mark--contested')).toBe(true);
    expect(marks[1].classList.contains('citation-mark--contested')).toBe(false);
  });

  it('the card shows the plain formation_confidence phrase for the cited record', () => {
    const { text, spans, sentences } = turn(['A contested claim.']);
    const contested = card('fix.story.thin', 'story', 'Thin Story', { formation_confidence: 'Contested' });
    const transparency = plan(spans, [el(sentences, 0, 'fix.story.thin', 'story')], [contested]);

    const { container } = render(<VoiceTurnBody text={text} citations={[]} transparency={transparency} />);

    fireEvent.mouseEnter(container.querySelector('.story-mark')!);
    expect(container.querySelector('.story-mark__confidence')?.textContent).toBe('Historians disagree about this.');
  });

  it('a card with no confidence envelope shows no phrase line (never invents one)', () => {
    const { text, spans, sentences } = turn(['A claim with no data.']);
    const nodata = card('fix.story.nodata', 'story', 'No-Data Story');
    const transparency = plan(spans, [el(sentences, 0, 'fix.story.nodata', 'story')], [nodata]);

    const { container } = render(<VoiceTurnBody text={text} citations={[]} transparency={transparency} />);

    fireEvent.mouseEnter(container.querySelector('.story-mark')!);
    expect(container.querySelector('.story-mark__title')?.textContent).toBe('No-Data Story');
    expect(container.querySelector('.story-mark__confidence')).toBeNull();
  });

  it('over the cap, glosses drop before figures before stories; a quote mark never drops', () => {
    // One sentence -> cap = 3. Six candidates: Antony, Origen (figures),
    // catechumens, baptism (glosses), a story, a quote. Three over cap:
    // baptism, catechumens, then Origen drop. Antony, the story and the
    // quote survive.
    const quoted = '"wash and be clean"';
    const sentence = `Antony taught Origen about catechumens and baptism, saying ${quoted} at the font.`;
    const { text, spans, sentences } = turn([sentence]);
    const storyCard = card('fix.story.a', 'story', 'Story A');
    const quoteCard = card('fix.quote.b', 'quote', 'Quote B');
    const transparency = plan(
      spans,
      [
        el(sentences, 0, 'fix.figure.antony', 'figure', 'Antony'),
        el(sentences, 0, 'fix.figure.origen', 'figure', 'Origen'),
        el(sentences, 0, 'fix.term.catechumens', 'term', 'catechumens'),
        el(sentences, 0, 'fix.term.baptism', 'term', 'baptism'),
        el(sentences, 0, 'fix.quote.b', 'quote', quoted),
        el(sentences, 0, 'fix.story.a', 'story'),
      ],
      [storyCard, quoteCard]
    );

    const { container } = render(
      <VoiceTurnBody
        text={text}
        citations={[]}
        figuresUsed={[figure('fix.figure.antony', 'Antony'), figure('fix.figure.origen', 'Origen')]}
        glosses={[gloss('fix.term.catechumens', 'catechumens'), gloss('fix.term.baptism', 'baptism')]}
        transparency={transparency}
      />
    );

    expect(markedText(container)).toBe(`{Antony} taught Origen about catechumens and baptism, saying ${quoted}[*] at the font.[*]`);
  });

  it('a dropped story mark reaches the end list and its sentence stays; quote marks are never the overflow', () => {
    // Four sentences -> cap = 3. Three stories and one quote: one over
    // cap, so the LAST story (C) drops. The quote is never a candidate.
    const quoted = '"the quoted words"';
    const { text, spans, sentences } = turn(['First story.', 'Second story.', 'Third story.', `He said ${quoted} once.`]);
    const a = card('fix.story.a', 'story', 'Story A');
    const b = card('fix.story.b', 'story', 'Story B');
    const c = card('fix.story.c', 'story', 'Story C');
    const q = card('fix.quote.d', 'quote', 'Quote D');
    const transparency = plan(
      spans,
      [el(sentences, 0, 'fix.story.a', 'story'), el(sentences, 1, 'fix.story.b', 'story'), el(sentences, 2, 'fix.story.c', 'story'), el(sentences, 3, 'fix.quote.d', 'quote', quoted)],
      [a, b, c, q]
    );

    const { container } = render(<VoiceTurnBody text={text} citations={[]} transparency={transparency} />);

    expect(markedText(container)).toBe(`First story.[*] Second story.[*] Third story. He said ${quoted}[*] once.`);
    expect(container.querySelector('.turn__general-references-label')?.textContent).toBe(`${END_REFERENCES_HEADING} (1)`);
    expect(container.querySelector('.turn__general-references .turn__sources-label')?.textContent).toBe('Story C');
  });

  it('an element whose record has no card, gloss or figure is not drawn, and nothing breaks', () => {
    const { text, spans, sentences } = turn(['Cites a record with no card.']);
    const transparency = plan(spans, [el(sentences, 0, 'fix.story.gone', 'story')], []);

    const { container } = render(<VoiceTurnBody text={text} citations={[]} transparency={transparency} />);

    expect(container.querySelector('.citation-mark')).toBeNull();
    expect(markedText(container)).toBe('Cites a record with no card.');
  });

  it('a quote mark\'s card carries QUOTE_CARD_PHRASE', () => {
    const quoted = '"the quoted words"';
    const { text, spans, sentences } = turn([`He said ${quoted} once.`]);
    const transparency = plan(spans, [el(sentences, 0, 'fix.quote.d', 'quote', quoted)], [card('fix.quote.d', 'quote', 'Quote D')]);

    const { container } = render(<VoiceTurnBody text={text} citations={[]} transparency={transparency} />);

    expect(container.querySelector('.story-mark')?.getAttribute('aria-label')).toBe(QUOTE_CARD_PHRASE);
  });

  it('falls back to the legacy renderer for a plan that predates elements, or no plan at all', () => {
    const sentence = 'An ordinary sentence with one citation.';
    const storyCard = card('fix.story.a', 'story', 'Story A');
    const citations: Citation[] = [{ sentence, record_ids: ['fix.story.a'], sources: [storyCard] }];
    const oldPlan: TransparencyPlan = {
      world_key: 'fix',
      anchors: [{ record_id: 'fix.story.a', record_type: 'story', world_key: 'fix', run_start_sentence: 0, run_end_sentence: 0, repeat: false, confidence: null }],
      references: [storyCard],
      unverified_claims: { count: 0, sentence_indexes: [] },
    };

    for (const transparency of [oldPlan, undefined]) {
      const { container } = render(<VoiceTurnBody text={sentence} citations={citations} transparency={transparency} />);
      expect(markedText(container)).toBe(`${sentence}[*]`);
    }
  });
});

describe('mark wording placeholders', () => {
  it('each pending entry still shows the wording the app used before per-element placement', () => {
    // Remove an entry from pendingMarkWording when its final wording
    // replaces the value; until then the value is the earlier wording, so
    // no placeholder copy ever reaches a participant.
    const before: Record<string, string> = {
      QUOTE_CARD_PHRASE: 'Where this story comes from',
      END_REFERENCES_HEADING: 'General references',
    };
    const current: Record<string, string> = { QUOTE_CARD_PHRASE, END_REFERENCES_HEADING };
    for (const name of pendingMarkWording) {
      if (name in before) expect(current[name]).toBe(before[name]);
    }
    expect(pendingMarkWording).toContain('Arrival disclosure line');
  });
});
