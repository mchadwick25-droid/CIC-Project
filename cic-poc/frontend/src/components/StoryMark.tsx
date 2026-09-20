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
 * different. Placed exactly where CitationMark used to sit for these
 * citations: right after the sentence that told the story.
 */
import type { SourceCard } from '../types/conversation';
import { InlineBridge } from './InlineBridge';
import { SourceList } from './SourceList';

interface StoryMarkProps {
  sources: SourceCard[]; // pre-filtered by the caller to record_type "story" | "quote"
}

export function StoryMark({ sources }: StoryMarkProps) {
  return (
    <InlineBridge
      label=" ✲"
      markClassName="citation-mark story-mark"
      ariaLabel={`Where this ${sources.length === 1 ? 'story' : 'story and quote'} comes from`}
      level2={
        <>
          {sources.map((card) => (
            <div key={card.record_id} className="story-mark__entry">
              <p className="story-mark__title">{card.label}</p>
              {card.sources.map((s) => (
                <p key={s.source_id} className="story-mark__source">
                  {s.work ?? s.source_id}
                  {s.author && ` — ${s.author}`}
                </p>
              ))}
            </div>
          ))}
        </>
      }
      level3Title="Where this story comes from"
      level3={
        <>
          {sources.map((card) => (
            <div key={card.record_id} className="turn__sources-card">
              <p className="turn__sources-label">{card.label}</p>
              {card.original_wording && (
                <div className="story-mark__original">
                  <p className="story-mark__original-label">Original wording</p>
                  <blockquote>{card.original_wording}</blockquote>
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
