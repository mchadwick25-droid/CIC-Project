/**
 * The term/concept gloss's inline mark - the OTHER track VR_1A named,
 * addressing complicated vocabulary a participant may not know (e.g.
 * catechumen, Didache). Same InlineBridge grammar as the name/figure
 * bridge, same "sourced from" lead.
 *
 * `translational_sense` is the actual point of this whole system, not a
 * side effect: engine.m4.term_glosses reads it straight from the term
 * record's own `senses.translational` field, written specifically to
 * answer a modern-phrased question in the world's own terms - e.g.
 * alx.term.allegoria's: "'Was Jesus God?' - this world answers through
 * the Logos..." The point is surfacing how a world understands a question
 * in its own terms, not supplying a dictionary definition.
 */
import type { GlossUsed } from '../types/conversation';
import { InlineBridge } from './InlineBridge';
import { SourceList } from './SourceList';

interface GlossMarkProps {
  label: string;
  gloss: GlossUsed;
}

export function GlossMark({ label, gloss }: GlossMarkProps) {
  return (
    <InlineBridge
      label={label}
      markClassName="name-bridge-mark"
      level2={<p>{gloss.quick_meaning ?? gloss.plain_meaning}</p>}
      level3Title={gloss.matched_name}
      level3={
        <>
          <p className="level3__section-label">What's said here, sourced from</p>
          <SourceList sources={gloss.sourced_by} empty="Nothing in this sentence was drawn from a source." />

          {gloss.plain_meaning && (
            <>
              <p className="level3__section-label">What it means</p>
              <p>{gloss.plain_meaning}</p>
            </>
          )}

          {gloss.translational_sense && (
            <>
              <p className="level3__section-label">Where a modern ear might hear it differently</p>
              <p>{gloss.translational_sense}</p>
            </>
          )}

          {gloss.false_friend.length > 0 && (
            <>
              <p className="level3__section-label">Not to be confused with</p>
              <ul className="level3__false-friend">
                {gloss.false_friend.map((f) => (
                  <li key={f}>{f}</li>
                ))}
              </ul>
            </>
          )}
        </>
      }
    />
  );
}
