/**
 * The fourth transparency track: every citation not covered by the
 * lexicon gloss, the name/figure bridge, or story/quote sourcing - a
 * doctrinal_witness, gravity, force, or contested_claim record cited
 * without a word or story of its own to carry a mark, plus a term or
 * figure record cited without the sentence actually saying that term or
 * name (so nothing in the text itself is what earned the citation).
 *
 * Mark's own correction (2026-08-25): these belong in a plain list at
 * the end of the answer, never as an asterisk inside the running text -
 * a reference is not the same claim on the reader's attention as a word
 * worth stopping on mid-sentence. No InlineBridge here on purpose: this
 * is already the fullest disclosure (same SourceList used everywhere
 * else), sitting in the open rather than behind a hover/click.
 */
import type { SourceCard } from '../types/conversation';
import { SourceList } from './SourceList';

interface GeneralReferencesProps {
  references: SourceCard[];
}

export function GeneralReferences({ references }: GeneralReferencesProps) {
  if (!references.length) return null;
  return (
    <div className="turn__general-references">
      <p className="turn__general-references-label">General references</p>
      {references.map((card) => (
        <div key={card.record_id} className="turn__sources-card">
          <p className="turn__sources-label">{card.label}</p>
          <SourceList sources={card.sources} empty="No source recorded for this." />
        </div>
      ))}
    </div>
  );
}
