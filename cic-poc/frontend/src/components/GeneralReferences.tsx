/**
 * The fourth transparency track: every citation not covered by the
 * lexicon gloss, the name/figure bridge, or story/quote sourcing - a
 * doctrinal_witness, gravity, force, or contested_claim record cited
 * without a word or story of its own to carry a mark, plus a term or
 * figure record cited without the sentence actually saying that term or
 * name (so nothing in the text itself is what earned the citation).
 *
 * These belong at the end of the answer, never as an asterisk inside the
 * running text - a reference is not the same claim on the reader's
 * attention as a word worth stopping on mid-sentence. The list sits
 * collapsed behind one disclosure line and opens on click, rather than
 * sitting open by default, so a long bibliography doesn't crowd the
 * conversation thread. No InlineBridge here on purpose: once opened this
 * is already the fullest disclosure (same SourceList used everywhere
 * else).
 */
import type { SourceCard } from '../types/conversation';
import { END_REFERENCES_HEADING } from '../lib/markCopy';
import { SourceList } from './SourceList';

interface GeneralReferencesProps {
  references: SourceCard[];
}

export function GeneralReferences({ references }: GeneralReferencesProps) {
  if (!references.length) return null;
  return (
    <details className="turn__general-references">
      <summary className="turn__general-references-label">
        {END_REFERENCES_HEADING} ({references.length})
      </summary>
      {references.map((card) => (
        <div key={card.record_id} className="turn__sources-card">
          <p className="turn__sources-label">{card.label}</p>
          <SourceList sources={card.sources} empty="No source recorded for this." />
        </div>
      ))}
    </details>
  );
}
