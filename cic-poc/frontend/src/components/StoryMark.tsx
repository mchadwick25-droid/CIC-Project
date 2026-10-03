/**
 * Story/quote sourcing - its own named application of the shared
 * transparency grammar (CiC_Full_UX_Design_V1_0.md §5.7: "story/quote
 * sourcing" is listed as its own track, distinct from "inline citations
 * (the ✲ marker)"). Before this, a cited story or quote fell through to
 * the generic CitationMark and read exactly like any other citation -
 * author/work/locus, nothing naming it as a story. A story's mark should
 * hover with what a participant actually wants to check for a story
 * specifically - its reference code, the English source it's drawn from,
 * and the story's own title.
 *
 * Same purple, same ✲, same InlineBridge grammar as every other track -
 * only the content and the record_types it fires for (story, quote) are
 * different. A story's mark sits at the end of its telling; a quote's
 * mark follows the quoted words (VoiceTurnBody.tsx places both).
 *
 * `repeat` and `contested` are CSS-only modifiers (app.css
 * .citation-mark--repeat/--contested) - same glyph, same color, same
 * verb, per the citation marks' own design constraints; see VoiceTurnBody.tsx's
 * renderFromElements for where these are computed.
 */
import type { SourceCard } from '../types/conversation';
import { confidencePhrase } from '../lib/confidence';
import { QUOTE_CARD_PHRASE } from '../lib/markCopy';
import { InlineBridge } from './InlineBridge';
import { SourceList } from './SourceList';

interface StoryMarkProps {
  sources: SourceCard[]; // pre-filtered by the caller to record_type "story" | "quote"
  repeat?: boolean;
  contested?: boolean;
  // A quote element's own mark: it follows the quoted words, not the
  // story's telling. Its card's title is QUOTE_CARD_PHRASE.
  quote?: boolean;
}

export function StoryMark({ sources, repeat, contested, quote }: StoryMarkProps) {
  const title = quote ? QUOTE_CARD_PHRASE : null;
  const markClassName = ['citation-mark', 'story-mark', repeat && 'citation-mark--repeat', contested && 'citation-mark--contested']
    .filter(Boolean)
    .join(' ');
  return (
    <InlineBridge
      label=" ✲"
      markClassName={markClassName}
      ariaLabel={title ?? `Where this ${sources.length === 1 ? 'story' : 'story and quote'} comes from`}
      level2={
        <>
          {sources.map((card) => {
            const phrase = confidencePhrase(card.confidence);
            return (
              <div key={card.record_id} className="story-mark__entry">
                <p className="story-mark__title">{card.label}</p>
                {card.sources.map((s) => (
                  <p key={s.source_id} className="story-mark__source">
                    {s.work ?? s.source_id}
                    {s.author && ` — ${s.author}`}
                  </p>
                ))}
                {phrase && <p className="story-mark__confidence">{phrase}</p>}
              </div>
            );
          })}
        </>
      }
      level3Title={title ?? 'Where this story comes from'}
      level3={
        <>
          {sources.map((card) => (
            <div key={card.record_id} className="turn__sources-card">
              <p className="turn__sources-label">{card.label}</p>
              {card.spoken_rendering && (
                <div className="story-mark__rendering">
                  <blockquote>{card.spoken_rendering}</blockquote>
                </div>
              )}
              <SourceList sources={card.sources} empty="No source recorded for this." />
            </div>
          ))}
        </>
      }
    />
  );
}
