/**
 * Renders a Representative turn's text with its citations. engine/m4/turn.py
 * tags citations per SENTENCE ({sentence, record_ids}), not per turn - a
 * strictly finer grain than the old cic-poc backend ever had, so this is a
 * new component rather than an adapted CitationMarker/CitationModal (whose
 * whole model - term/type/grounded, one marker for the whole turn - doesn't
 * match this shape). There is no drawn-on/consulted tier here either: the
 * new engine's citations are flat, so that distinction isn't rendered.
 *
 * A marker's own record_ids are shown on click - genuinely resolvable to
 * the exact sentence, not just "this turn used N sources somewhere."
 */
import { useState } from 'react';
import type { Citation } from '../types/conversation';

interface VoiceTurnBodyProps {
  text: string;
  citations: Citation[];
}

interface Segment {
  text: string;
  recordIds: string[] | null;
}

function splitIntoSegments(text: string, citations: Citation[]): Segment[] {
  const segments: Segment[] = [];
  let remaining = text;
  for (const citation of citations) {
    const idx = remaining.indexOf(citation.sentence);
    if (idx === -1) continue; // the sentence didn't survive verbatim in this text - skip rather than guess a position
    const before = remaining.slice(0, idx + citation.sentence.length);
    segments.push({ text: before, recordIds: citation.record_ids });
    remaining = remaining.slice(idx + citation.sentence.length);
  }
  if (remaining) segments.push({ text: remaining, recordIds: null });
  return segments;
}

export function VoiceTurnBody({ text, citations }: VoiceTurnBodyProps) {
  const [openIndex, setOpenIndex] = useState<number | null>(null);
  const segments = splitIntoSegments(text, citations);

  return (
    <div className="turn__body">
      <div>
        {segments.map((segment, i) => (
          <span key={i}>
            {segment.text}
            {segment.recordIds && (
              <button
                type="button"
                className="citation-mark"
                aria-label={`${segment.recordIds.length} source${segment.recordIds.length === 1 ? '' : 's'} for this sentence`}
                onClick={() => setOpenIndex(openIndex === i ? null : i)}
              >
                {' '}✲
              </button>
            )}
          </span>
        ))}
      </div>
      {openIndex !== null && segments[openIndex]?.recordIds && (
        <div className="turn__sources">
          <ul className="turn__sources-list">
            {segments[openIndex].recordIds!.map((id) => (
              <li key={id}>{id}</li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}
