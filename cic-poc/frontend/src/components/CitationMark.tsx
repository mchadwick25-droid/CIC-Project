/**
 * The ✲ citation marker, upgraded to the same InlineBridge grammar as the
 * name/figure bridge and the term gloss (Full UX Design §5.7: "inline
 * citations (the ✲ marker)" is named as one of the five applications of
 * the SAME transparency grammar, not its own thing) - hover/click on
 * desktop, tap/tap-through on phone, Level 3 a real side panel or bottom
 * sheet, not the inline toggle-reveal this used to be.
 *
 * A sentence can cite more than one record, so Level 2 stays a one-line
 * count/label and Level 3 lists every cited record's own resolved
 * sources (engine.m4.citation_cards.resolve_citation_sources) in full.
 */
import type { SourceCard } from '../types/conversation';
import { InlineBridge } from './InlineBridge';
import { SourceList } from './SourceList';

interface CitationMarkProps {
  sources: SourceCard[];
}

export function CitationMark({ sources }: CitationMarkProps) {
  const level2Text = sources.length === 0
    ? 'No source recorded for this.'
    : sources.length === 1
      ? sources[0].label
      : `${sources.length} sources for this`;

  return (
    <InlineBridge
      label=" ✲"
      markClassName="citation-mark"
      ariaLabel={`${sources.length} source${sources.length === 1 ? '' : 's'} for this sentence`}
      level2={<p>{level2Text}</p>}
      level3Title="Sources for this"
      level3={
        sources.length === 0 ? (
          <p>No source recorded for this.</p>
        ) : (
          <>
            {sources.map((card) => (
              <div key={card.record_id} className="turn__sources-card">
                <p className="turn__sources-label">{card.label}</p>
                <SourceList sources={card.sources} empty="No source recorded for this." />
              </div>
            ))}
          </>
        )
      }
    />
  );
}
