/**
 * Doctrinal-witness sourcing - its own named application of the shared
 * transparency grammar, same family as StoryMark (CiC_Full_UX_Design_V1_0.md
 * §5.7: "one grammar, five applications, no feature may introduce a sixth
 * verb"). A doctrinal_witness record is the build's own reviewed synthesis
 * of a world's stance, sourced from real texts - not a story, not a
 * verbatim quote - so it earns its own copy rather than borrowing
 * StoryMark's ("where this story comes from" reads wrong for a sentence
 * that's actually the build's own crafted answer).
 *
 * A synthesis sentence that sounds freely generated can actually trace to
 * real, reviewed ground (the record's own text) - without this, the
 * interface gave no inline sign of that, only the end-of-turn General
 * References list, which nobody is obliged to open. Before this,
 * doctrinal_witness (like gravity/force/contested_claim) had no word or
 * story to attach a mark to and fell straight through to General
 * References - this gives it the same inline disclosure story/quote
 * already have.
 *
 * Same purple, same ✲, same InlineBridge grammar, same one-mark-per-run
 * dedup as StoryMark - a multi-sentence answer built on one witness record
 * gets one mark, not one per sentence, matching the same rule already
 * applied to story/quote. Placed at the run's FIRST sentence, not its
 * last (R10, RULED c, 2026-09-21) - a participant should see "this is
 * someone else's words" before reading them, the opposite of a story's
 * own placement at the run's end.
 *
 * `repeat` and `contested` are CSS-only modifiers (app.css
 * .citation-mark--repeat/--contested) - same glyph, same color, same
 * verb, per R9's and R10's own design constraints; see VoiceTurnBody.tsx's
 * renderFromTransparencyPlan for where these are computed.
 */
import type { SourceCard } from '../types/conversation';
import { confidencePhrase } from '../lib/confidence';
import { InlineBridge } from './InlineBridge';
import { SourceList } from './SourceList';

interface WitnessMarkProps {
  sources: SourceCard[]; // pre-filtered by the caller to record_type "doctrinal_witness"
  repeat?: boolean;
  contested?: boolean;
}

export function WitnessMark({ sources, repeat, contested }: WitnessMarkProps) {
  const markClassName = ['citation-mark', 'witness-mark', repeat && 'citation-mark--repeat', contested && 'citation-mark--contested']
    .filter(Boolean)
    .join(' ');
  return (
    <InlineBridge
      label=" ✲"
      markClassName={markClassName}
      ariaLabel="Where this comes from"
      level2={
        <>
          {sources.map((card) => {
            const phrase = confidencePhrase(card.confidence);
            return (
              <div key={card.record_id} className="witness-mark__entry">
                <p className="witness-mark__title">{card.label}</p>
                {card.sources.map((s) => (
                  <p key={s.source_id} className="witness-mark__source">
                    {s.work ?? s.source_id}
                    {s.author && ` — ${s.author}`}
                  </p>
                ))}
                {phrase && <p className="witness-mark__confidence">{phrase}</p>}
              </div>
            );
          })}
        </>
      }
      level3Title="Where this comes from"
      level3={
        <>
          {sources.map((card) => (
            <div key={card.record_id} className="turn__sources-card">
              <p className="turn__sources-label">{card.label}</p>
              <SourceList sources={card.sources} empty="No source recorded for this." />
            </div>
          ))}
        </>
      }
    />
  );
}
