/**
 * Build-Plan.md Stage 3c: fixtures prove `A, A, B, A` and `1, 4, 7, 10`
 * render every verified citation, and an element-count test enforces the
 * one-mark-per-run house rule (see VoiceTurnBody.tsx's own docstring:
 * "ONE ✲ per story/quote source per turn... never one per cited
 * sentence"). These exercise the anchor-driven renderer directly (the
 * flag mocked on) - see VoiceTurnBody.legacy-default.test.tsx for the
 * proof that the flag is off by default and the legacy renderer's own
 * completeness gap is what these fixtures are written against.
 */
import { fireEvent, render } from '@testing-library/react';
import { describe, expect, it, vi } from 'vitest';
import type { Citation, SourceCard, TransparencyAnchor, TransparencyPlan } from '../types/conversation';

vi.mock('../lib/flags', () => ({ useAnchorRenderer: true }));
const { VoiceTurnBody } = await import('./VoiceTurnBody');

function card(recordId: string, recordType: string, label: string, confidence?: Record<string, unknown> | null): SourceCard {
  return { record_id: recordId, record_type: recordType, label, sources: [], confidence };
}

function citation(sentence: string, recordId: string, recordType: string, label: string, confidence?: Record<string, unknown> | null): { citation: Citation; card: SourceCard } {
  const c = card(recordId, recordType, label, confidence);
  return { citation: { sentence, record_ids: [recordId], sources: [c] }, card: c };
}

function anchor(recordId: string, recordType: string, runStart: number, runEnd: number, repeat: boolean): TransparencyAnchor {
  return { record_id: recordId, record_type: recordType, world_key: 'fix', run_start_sentence: runStart, run_end_sentence: runEnd, repeat, confidence: null };
}

describe('VoiceTurnBody - anchor-driven renderer (Stage 3c)', () => {
  it('A, A, B, A: a non-consecutive repeat citation gets its own mark, not silently dropped', () => {
    // The exact defect engine.m4.transparency_plan.py's own docstring
    // names: story A is cited twice, non-consecutively (a real B citation
    // sits between them). The legacy renderer's renderedStoryIds would
    // suppress A's second mark AND drop its sources entirely, since
    // story/witness sources never reached addReference. This fixture
    // proves the fix: three marks total (A's first run, B's run, A's
    // repeat run), not two.
    const s0 = citation('Sentence zero about A.', 'fix.story.a', 'story', 'Story A');
    const s1 = citation('Sentence one about A too.', 'fix.story.a', 'story', 'Story A');
    const s2 = citation('Sentence two about B.', 'fix.witness.b', 'doctrinal_witness', 'Witness B');
    const s3 = citation('Sentence three about A again.', 'fix.story.a', 'story', 'Story A');
    const text = [s0, s1, s2, s3].map((s) => s.citation.sentence).join(' ');
    const citations = [s0.citation, s1.citation, s2.citation, s3.citation];
    const transparency: TransparencyPlan = {
      world_key: 'fix',
      anchors: [
        anchor('fix.story.a', 'story', 0, 1, false),
        anchor('fix.witness.b', 'doctrinal_witness', 2, 2, false),
        anchor('fix.story.a', 'story', 3, 3, true),
      ],
      references: [s0.card, s2.card], // completeness invariant: one entry per distinct record_id
      unverified_claims: { count: 0, sentence_indexes: [] },
    };

    const { container } = render(<VoiceTurnBody text={text} citations={citations} transparency={transparency} />);

    expect(container.querySelectorAll('.story-mark')).toHaveLength(2); // A's first run + A's repeat run
    expect(container.querySelectorAll('.witness-mark')).toHaveLength(1);
    // Everything got an inline mark - nothing left over for General References.
    expect(container.querySelector('.turn__general-references')).toBeNull();
  });

  it('1, 4, 7, 10: four widely-separated citations, interspersed with uncited prose, all render', () => {
    const records = ['fix.story.one', 'fix.story.four', 'fix.story.seven', 'fix.story.ten'].map((id, i) =>
      citation(`Cited sentence number ${i}.`, id, 'story', `Story ${i}`)
    );
    const filler = (n: number) => Array.from({ length: n }, (_, i) => `Uncited filler sentence ${i}.`).join(' ');
    const text = [filler(1), records[0].citation.sentence, filler(2), records[1].citation.sentence, filler(2), records[2].citation.sentence, filler(2), records[3].citation.sentence].join(' ');
    const citations = records.map((r) => r.citation);
    const transparency: TransparencyPlan = {
      world_key: 'fix',
      anchors: records.map((_, i) => anchor(records[i].card.record_id, 'story', i, i, false)),
      references: records.map((r) => r.card),
      unverified_claims: { count: 0, sentence_indexes: [] },
    };

    const { container } = render(<VoiceTurnBody text={text} citations={citations} transparency={transparency} />);

    expect(container.querySelectorAll('.story-mark')).toHaveLength(4);
    expect(container.querySelector('.turn__general-references')).toBeNull();
  });

  it('one mark per run, never one per cited sentence (the house rule an element-count test enforces)', () => {
    // Three CONSECUTIVE sentences all citing the same story - one run,
    // one mark, exactly as VoiceTurnBody.tsx's own docstring requires:
    // "a story told across four sentences drew four identical marks...
    // that is not the design."
    const s0 = citation('Part one of the telling.', 'fix.story.long', 'story', 'A Long Story');
    const s1 = citation('Part two of the telling.', 'fix.story.long', 'story', 'A Long Story');
    const s2 = citation('Part three of the telling.', 'fix.story.long', 'story', 'A Long Story');
    const text = [s0, s1, s2].map((s) => s.citation.sentence).join(' ');
    const citations = [s0.citation, s1.citation, s2.citation];
    const transparency: TransparencyPlan = {
      world_key: 'fix',
      anchors: [anchor('fix.story.long', 'story', 0, 2, false)],
      references: [s0.card],
      unverified_claims: { count: 0, sentence_indexes: [] },
    };

    const { container } = render(<VoiceTurnBody text={text} citations={citations} transparency={transparency} />);

    expect(container.querySelectorAll('.story-mark')).toHaveLength(1);
  });

  it('a record with no word or story to attach to reaches General References, not an inline mark', () => {
    const s0 = citation('A claim resting on a gravity record.', 'fix.gravity.one', 'gravity', 'A Gravity');
    const transparency: TransparencyPlan = {
      world_key: 'fix',
      anchors: [anchor('fix.gravity.one', 'gravity', 0, 0, false)],
      references: [s0.card],
      unverified_claims: { count: 0, sentence_indexes: [] },
    };

    const { container, getByText } = render(<VoiceTurnBody text={s0.citation.sentence} citations={[s0.citation]} transparency={transparency} />);

    expect(container.querySelectorAll('.story-mark')).toHaveLength(0);
    expect(container.querySelectorAll('.witness-mark')).toHaveLength(0);
    expect(getByText('General references (1)')).toBeInTheDocument();
  });

  it('falls back to the legacy renderer when transparency is absent even with the flag on', () => {
    // A transcript entry replayed from before Stage 3a existed carries no
    // transparency field at all (types/conversation.ts marks it optional
    // for exactly this reason) - the flag alone must never crash the turn.
    const s0 = citation('An old turn with no transparency plan.', 'fix.story.old', 'story', 'Old Story');
    const { container } = render(<VoiceTurnBody text={s0.citation.sentence} citations={[s0.citation]} />);
    expect(container.querySelectorAll('.story-mark')).toHaveLength(1);
  });

  it('R10 (RULED c): a witness mark lands at the run\'s FIRST sentence, a story mark at its LAST', () => {
    // Two runs of equal length, one witness and one story, so any
    // placement difference in the rendered output can only come from the
    // placement rule itself, not from run length.
    const s0 = citation('Witness sentence one.', 'fix.witness.w', 'doctrinal_witness', 'Witness W');
    const s1 = citation('Witness sentence two.', 'fix.witness.w', 'doctrinal_witness', 'Witness W');
    const s2 = citation('Story sentence one.', 'fix.story.s', 'story', 'Story S');
    const s3 = citation('Story sentence two.', 'fix.story.s', 'story', 'Story S');
    const text = [s0, s1, s2, s3].map((s) => s.citation.sentence).join(' ');
    const citations = [s0.citation, s1.citation, s2.citation, s3.citation];
    const transparency: TransparencyPlan = {
      world_key: 'fix',
      anchors: [anchor('fix.witness.w', 'doctrinal_witness', 0, 1, false), anchor('fix.story.s', 'story', 2, 3, false)],
      references: [s0.card, s2.card],
      unverified_claims: { count: 0, sentence_indexes: [] },
    };

    const { container } = render(<VoiceTurnBody text={text} citations={citations} transparency={transparency} />);

    const spans = Array.from(container.querySelectorAll('.turn__body > div > span'));
    // The witness mark sits in the FIRST segment's span (run_start_sentence
    // = 0), not the second - even though the run doesn't end until index 1.
    expect(spans[0].querySelector('.witness-mark')).not.toBeNull();
    expect(spans[1].querySelector('.witness-mark')).toBeNull();
    // The story mark sits in the LAST segment's span (run_end_sentence = 3).
    expect(spans[2].querySelector('.story-mark')).toBeNull();
    expect(spans[3].querySelector('.story-mark')).not.toBeNull();
  });

  it('R10 (RULED c): a repeat citation renders the same mark with the lighter .citation-mark--repeat class', () => {
    const s0 = citation('First mention of the story.', 'fix.story.a', 'story', 'Story A');
    const s1 = citation('Something else entirely.', 'fix.witness.b', 'doctrinal_witness', 'Witness B');
    const s2 = citation('Second mention of the story.', 'fix.story.a', 'story', 'Story A');
    const text = [s0, s1, s2].map((s) => s.citation.sentence).join(' ');
    const citations = [s0.citation, s1.citation, s2.citation];
    const transparency: TransparencyPlan = {
      world_key: 'fix',
      anchors: [
        anchor('fix.story.a', 'story', 0, 0, false),
        anchor('fix.witness.b', 'doctrinal_witness', 1, 1, false),
        anchor('fix.story.a', 'story', 2, 2, true),
      ],
      references: [s0.card, s1.card],
      unverified_claims: { count: 0, sentence_indexes: [] },
    };

    const { container } = render(<VoiceTurnBody text={text} citations={citations} transparency={transparency} />);

    const storyMarks = container.querySelectorAll('.story-mark');
    expect(storyMarks).toHaveLength(2);
    expect(storyMarks[0].classList.contains('citation-mark--repeat')).toBe(false);
    expect(storyMarks[1].classList.contains('citation-mark--repeat')).toBe(true);
  });

  it('R9 (RULED a): Contested or Inferential-Thin formation_confidence renders the hollow .citation-mark--contested class, a solid claim does not', () => {
    const s0 = citation('A well-attested claim.', 'fix.story.solid', 'story', 'Solid Story');
    const s1 = citation('A contested claim.', 'fix.story.thin', 'story', 'Thin Story');
    const text = [s0, s1].map((s) => s.citation.sentence).join(' ');
    const citations = [s0.citation, s1.citation];
    const transparency: TransparencyPlan = {
      world_key: 'fix',
      anchors: [
        { ...anchor('fix.story.solid', 'story', 0, 0, false), confidence: { formation_confidence: 'Widely Accepted' } },
        { ...anchor('fix.story.thin', 'story', 1, 1, false), confidence: { formation_confidence: 'Contested' } },
      ],
      references: [s0.card, s1.card],
      unverified_claims: { count: 0, sentence_indexes: [] },
    };

    const { container } = render(<VoiceTurnBody text={text} citations={citations} transparency={transparency} />);

    const storyMarks = container.querySelectorAll('.story-mark');
    expect(storyMarks).toHaveLength(2);
    expect(storyMarks[0].classList.contains('citation-mark--contested')).toBe(false);
    expect(storyMarks[1].classList.contains('citation-mark--contested')).toBe(true);
  });

  it('Stage 6b: the Level 2 card shows the plain formation_confidence phrase for the cited record', () => {
    const s0 = citation('A contested claim.', 'fix.story.thin', 'story', 'Thin Story', { formation_confidence: 'Contested' });
    const transparency: TransparencyPlan = {
      world_key: 'fix',
      anchors: [{ ...anchor('fix.story.thin', 'story', 0, 0, false), confidence: { formation_confidence: 'Contested' } }],
      references: [s0.card],
      unverified_claims: { count: 0, sentence_indexes: [] },
    };

    const { container, getByText } = render(<VoiceTurnBody text={s0.citation.sentence} citations={[s0.citation]} transparency={transparency} />);

    fireEvent.mouseEnter(container.querySelector('.story-mark')!);
    expect(getByText('Historians disagree about this.')).toBeInTheDocument();
  });

  it("Stage 6b: a card with no confidence envelope shows no phrase line (never invents one)", () => {
    const s0 = citation('A claim with no confidence data.', 'fix.story.nodata', 'story', 'No-Data Story');
    const transparency: TransparencyPlan = {
      world_key: 'fix',
      anchors: [anchor('fix.story.nodata', 'story', 0, 0, false)],
      references: [s0.card],
      unverified_claims: { count: 0, sentence_indexes: [] },
    };

    const { container } = render(<VoiceTurnBody text={s0.citation.sentence} citations={[s0.citation]} transparency={transparency} />);

    fireEvent.mouseEnter(container.querySelector('.story-mark')!);
    expect(container.querySelector('.story-mark__confidence')).toBeNull();
  });
});
