/**
 * Renders a Representative turn's text with its citations and its
 * name/figure bridges. engine/m4/turn.py tags citations per SENTENCE
 * ({sentence, record_ids}), not per turn - a strictly finer grain than
 * the old cic-poc backend ever had, so this is a new component rather
 * than an adapted CitationMarker/CitationModal (whose whole model -
 * term/type/grounded, one marker for the whole turn - doesn't match this
 * shape). There is no drawn-on/consulted tier here either: the new
 * engine's citations are flat, so that distinction isn't rendered.
 *
 * A citation marker's own record_ids are shown on click - genuinely
 * resolvable to the exact sentence, not just "this turn used N sources
 * somewhere."
 *
 * Figures (engine.m4.name_bridge.find_figures_used) are word-level marks
 * INSIDE a sentence, not sentence-end markers, so they're found within
 * each citation segment's own text rather than by re-splitting the whole
 * turn a second, independent way. Segments already partition the full
 * text left to right in order - the first segment a figure's matched_name
 * is found in is exactly where find_figures_used found it too (its own
 * search is over the same, unsegmented text), so matching segment-by-
 * segment and marking each figure used at most once reproduces the
 * backend's first-occurrence result rather than a second guess at it.
 */
import { useState } from 'react';
import type { Citation, FigureUsed } from '../types/conversation';
import { FigureBridgeMark } from './FigureBridgeMark';

interface VoiceTurnBodyProps {
  text: string;
  citations: Citation[];
  figuresUsed?: FigureUsed[];
}

interface Segment {
  text: string;
  recordIds: string[] | null;
}

interface FigureSpan {
  start: number;
  end: number;
  figure: FigureUsed;
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

function findFigureSpans(segmentText: string, figures: FigureUsed[]): FigureSpan[] {
  const spans: FigureSpan[] = [];
  for (const figure of figures) {
    const idx = segmentText.indexOf(figure.matched_name);
    if (idx === -1) continue;
    spans.push({ start: idx, end: idx + figure.matched_name.length, figure });
  }
  spans.sort((a, b) => a.start - b.start);
  // Two figures' spans overlapping is a real, named possibility
  // (engine.m4.name_bridge's own docstring: "Simeon" inside "Simeon
  // Stylites") - drop the later one rather than render broken markup.
  const nonOverlapping: FigureSpan[] = [];
  let cursor = 0;
  for (const span of spans) {
    if (span.start >= cursor) {
      nonOverlapping.push(span);
      cursor = span.end;
    }
  }
  return nonOverlapping;
}

function renderSegmentText(segmentText: string, figures: FigureUsed[], usedFigureIds: Set<string>, keyPrefix: string) {
  const candidates = figures.filter((f) => !usedFigureIds.has(f.id));
  const spans = findFigureSpans(segmentText, candidates);
  if (!spans.length) return segmentText;

  const nodes: React.ReactNode[] = [];
  let cursor = 0;
  spans.forEach((span, i) => {
    if (span.start > cursor) nodes.push(segmentText.slice(cursor, span.start));
    nodes.push(<FigureBridgeMark key={`${keyPrefix}-fig-${i}`} label={span.figure.matched_name} figure={span.figure} />);
    usedFigureIds.add(span.figure.id);
    cursor = span.end;
  });
  if (cursor < segmentText.length) nodes.push(segmentText.slice(cursor));
  return nodes;
}

export function VoiceTurnBody({ text, citations, figuresUsed = [] }: VoiceTurnBodyProps) {
  const [openIndex, setOpenIndex] = useState<number | null>(null);
  const segments = splitIntoSegments(text, citations);
  const usedFigureIds = new Set<string>();

  return (
    <div className="turn__body">
      <div>
        {segments.map((segment, i) => (
          <span key={i}>
            {renderSegmentText(segment.text, figuresUsed, usedFigureIds, `seg${i}`)}
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
