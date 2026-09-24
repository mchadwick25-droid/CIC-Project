/**
 * The flag now defaults ON - this file's own title
 * predates that flip and is kept only because the legacy renderer stays
 * genuinely reachable, not because the flag defaults to it anymore. No
 * mock here: exercises VoiceTurnBody exactly as a caller with no
 * `transparency` plan on the turn does (an older logged session, or a
 * turn from before Stage 3b) - VoiceTurnBody's own top-level export falls
 * back to the legacy renderer whenever `transparency` is absent,
 * regardless of the flag. Its known completeness gap is reproduced here
 * on purpose, so the fix in VoiceTurnBody.test.tsx has something concrete
 * to be a fix FOR.
 */
import { render } from '@testing-library/react';
import { describe, expect, it } from 'vitest';
import type { Citation, SourceCard } from '../types/conversation';
import { VoiceTurnBody } from './VoiceTurnBody';

function card(recordId: string, recordType: string, label: string): SourceCard {
  return { record_id: recordId, record_type: recordType, label, sources: [] };
}

function citation(sentence: string, recordId: string, recordType: string, label: string): { citation: Citation; card: SourceCard } {
  const c = card(recordId, recordType, label);
  return { citation: { sentence, record_ids: [recordId], sources: [c] }, card: c };
}

describe('VoiceTurnBody - legacy renderer, reachable with no transparency plan on the turn', () => {
  it('renders an ordinary single citation the same way it always has', () => {
    const s0 = citation('An ordinary sentence with one citation.', 'fix.story.a', 'story', 'Story A');
    const { container } = render(<VoiceTurnBody text={s0.citation.sentence} citations={[s0.citation]} />);
    expect(container.querySelectorAll('.story-mark')).toHaveLength(1);
  });

  it("A, A, B, A: the known gap this stage fixes - a non-consecutive repeat's sources are dropped, not just its mark", () => {
    // Passing `transparency` too, exactly as every real caller now does
    // post-3b - the point of this test is that the LEGACY renderer never
    // looks at it while the flag is off, so the gap it has is unchanged.
    const s0 = citation('Sentence zero about A.', 'fix.story.a', 'story', 'Story A');
    const s1 = citation('Sentence one about A too.', 'fix.story.a', 'story', 'Story A');
    const s2 = citation('Sentence two about B.', 'fix.witness.b', 'doctrinal_witness', 'Witness B');
    const s3 = citation('Sentence three about A again.', 'fix.story.a', 'story', 'Story A');
    const text = [s0, s1, s2, s3].map((s) => s.citation.sentence).join(' ');
    const citations = [s0.citation, s1.citation, s2.citation, s3.citation];

    const { container } = render(<VoiceTurnBody text={text} citations={citations} />);

    // Only ONE story-mark (A's first run) - the repeat at sentence 3 is
    // suppressed by renderedStoryIds, same as it is in production today.
    expect(container.querySelectorAll('.story-mark')).toHaveLength(1);
    expect(container.querySelectorAll('.witness-mark')).toHaveLength(1);
    // And the repeat's sources are not even in General References -
    // story/witness sources are never passed to addReference in the
    // legacy renderer. This is the actual data loss, not just a missing
    // mark - the fixed renderer's own "no General References" assertion
    // in VoiceTurnBody.test.tsx is the direct contrast.
    expect(container.querySelector('.turn__general-references')).toBeNull();
  });
});
