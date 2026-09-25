/**
 * A bridged modern term's own sourced card (OG-13,
 * worlds/pahc/Open_Gaps_Tracking.md): the Facilitator's bridge_turn speaks
 * the underlying_subject in plain English and drops the modern word itself
 * from the voice - this is where a participant can still see that modern
 * word's own sense and how it relates to what the voice actually said,
 * with the real sources behind it. Same InlineBridge grammar as
 * WitnessMark/StoryMark, its own copy rather than borrowed ("modern sense"
 * reads wrong as "where this comes from").
 */
import type { SourceCard } from '../types/conversation';
import { InlineBridge } from './InlineBridge';
import { SourceList } from './SourceList';

interface ModernTermMarkProps {
  card: SourceCard; // record_type "modern_term"
}

export function ModernTermMark({ card }: ModernTermMarkProps) {
  return (
    <InlineBridge
      label=" ≈"
      markClassName="citation-mark modern-term-mark"
      ariaLabel={`What "${card.label}" means here`}
      level2={
        <div className="modern-term-mark__entry">
          <p className="modern-term-mark__title">{card.label}</p>
          {card.modern_sense && <p className="modern-term-mark__sense">{card.modern_sense}</p>}
          {card.distinguishing_claim && <p className="modern-term-mark__distinguishing">{card.distinguishing_claim}</p>}
        </div>
      }
      level3Title={`What "${card.label}" means here`}
      level3={
        <div className="turn__sources-card">
          <p className="turn__sources-label">{card.label}</p>
          {card.modern_sense && <p className="modern-term-mark__sense">{card.modern_sense}</p>}
          {card.distinguishing_claim && <p className="modern-term-mark__distinguishing">{card.distinguishing_claim}</p>}
          <SourceList sources={card.sources} empty="No source recorded for this." />
        </div>
      }
    />
  );
}
