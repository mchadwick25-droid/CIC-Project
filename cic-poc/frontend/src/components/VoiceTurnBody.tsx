/**
 * Renders a Representative turn's text with its citations, its name/
 * figure bridges, and its term glosses - the three tracks of the
 * transparency system, all sharing InlineBridge's one grammar (Full UX
 * Design §5.7: "one grammar, five applications, no feature may introduce
 * a sixth verb"). engine/m4/turn.py tags citations per SENTENCE
 * ({sentence, record_ids}), not per turn - a strictly finer grain than
 * the old cic-poc backend ever had, so this is a new component rather
 * than an adapted CitationMarker/CitationModal. There is no drawn-on/
 * consulted tier here either: the new engine's citations are flat, so
 * that distinction isn't rendered.
 *
 * Figures (engine.m4.name_bridge) and glosses (engine.m4.term_glosses)
 * are word-level marks INSIDE a sentence, not sentence-end markers, so
 * they're found within each citation segment's own text rather than by
 * re-splitting the whole turn a second, independent way. Segments already
 * partition the full text left to right in order - the first segment a
 * mark's matched_name is found in is exactly where the backend found it
 * too (its own search is over the same, unsegmented text), so matching
 * segment-by-segment and marking each id used at most once reproduces
 * the backend's first-occurrence result rather than a second guess at
 * it. Figures and glosses are looked up independently (a name and a term
 * are never the same record), so their spans are found and dropped for
 * overlap together, in one pass.
 */
import type { Citation, FigureUsed, GlossUsed } from '../types/conversation';
import { CitationMark } from './CitationMark';
import { FigureBridgeMark } from './FigureBridgeMark';
import { GlossMark } from './GlossMark';

interface VoiceTurnBodyProps {
  text: string;
  citations: Citation[];
  figuresUsed?: FigureUsed[];
  glosses?: GlossUsed[];
}

interface Segment {
  text: string;
  citation: Citation | null;
}

type Mark = { start: number; end: number; matchedName: string; kind: 'figure'; figure: FigureUsed } | { start: number; end: number; matchedName: string; kind: 'gloss'; gloss: GlossUsed };

function splitIntoSegments(text: string, citations: Citation[]): Segment[] {
  const segments: Segment[] = [];
  let remaining = text;
  for (const citation of citations) {
    const idx = remaining.indexOf(citation.sentence);
    if (idx === -1) continue; // the sentence didn't survive verbatim in this text - skip rather than guess a position
    const before = remaining.slice(0, idx + citation.sentence.length);
    segments.push({ text: before, citation });
    remaining = remaining.slice(idx + citation.sentence.length);
  }
  if (remaining) segments.push({ text: remaining, citation: null });
  return segments;
}

function findMarks(segmentText: string, figures: FigureUsed[], glosses: GlossUsed[]): Mark[] {
  const candidates: Mark[] = [];
  for (const figure of figures) {
    const idx = segmentText.indexOf(figure.matched_name);
    if (idx === -1) continue;
    candidates.push({ start: idx, end: idx + figure.matched_name.length, matchedName: figure.matched_name, kind: 'figure', figure });
  }
  for (const gloss of glosses) {
    const idx = segmentText.indexOf(gloss.matched_name);
    if (idx === -1) continue;
    candidates.push({ start: idx, end: idx + gloss.matched_name.length, matchedName: gloss.matched_name, kind: 'gloss', gloss });
  }
  candidates.sort((a, b) => a.start - b.start);
  // Two marks' spans overlapping is a real, named possibility (a figure's
  // name inside a longer one; a term that happens to share a substring
  // with a name) - drop the later one rather than render broken markup.
  const nonOverlapping: Mark[] = [];
  let cursor = 0;
  for (const mark of candidates) {
    if (mark.start >= cursor) {
      nonOverlapping.push(mark);
      cursor = mark.end;
    }
  }
  return nonOverlapping;
}

function renderSegmentText(
  segmentText: string,
  figures: FigureUsed[],
  glosses: GlossUsed[],
  usedIds: Set<string>,
  keyPrefix: string
) {
  const figureCandidates = figures.filter((f) => !usedIds.has(f.id));
  const glossCandidates = glosses.filter((g) => !usedIds.has(g.id));
  const marks = findMarks(segmentText, figureCandidates, glossCandidates);
  if (!marks.length) return segmentText;

  const nodes: React.ReactNode[] = [];
  let cursor = 0;
  marks.forEach((mark, i) => {
    if (mark.start > cursor) nodes.push(segmentText.slice(cursor, mark.start));
    if (mark.kind === 'figure') {
      nodes.push(<FigureBridgeMark key={`${keyPrefix}-mark-${i}`} label={mark.matchedName} figure={mark.figure} />);
      usedIds.add(mark.figure.id);
    } else {
      nodes.push(<GlossMark key={`${keyPrefix}-mark-${i}`} label={mark.matchedName} gloss={mark.gloss} />);
      usedIds.add(mark.gloss.id);
    }
    cursor = mark.end;
  });
  if (cursor < segmentText.length) nodes.push(segmentText.slice(cursor));
  return nodes;
}

export function VoiceTurnBody({ text, citations, figuresUsed = [], glosses = [] }: VoiceTurnBodyProps) {
  const segments = splitIntoSegments(text, citations);
  const usedIds = new Set<string>();

  return (
    <div className="turn__body">
      <div>
        {segments.map((segment, i) => (
          <span key={i}>
            {renderSegmentText(segment.text, figuresUsed, glosses, usedIds, `seg${i}`)}
            {segment.citation && <CitationMark sources={segment.citation.sources} />}
          </span>
        ))}
      </div>
    </div>
  );
}
