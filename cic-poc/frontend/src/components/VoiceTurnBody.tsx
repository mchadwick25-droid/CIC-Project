/**
 * Renders a Representative turn's text with its citations, its name/
 * figure bridges, its term glosses, and its story/quote sourcing - the
 * four tracks of the transparency system, all sharing InlineBridge's one
 * grammar (Full UX Design §5.7: "one grammar, five applications, no
 * feature may introduce a sixth verb"). engine/m4/turn.py tags citations
 * per SENTENCE ({sentence, record_ids}), not per turn - a strictly finer
 * grain than the old cic-poc backend ever had, so this is a new component
 * rather than an adapted CitationMarker/CitationModal. There is no drawn-
 * on/consulted tier here either: the new engine's citations are flat, so
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
 *
 * A citation's own sources (engine.m4.citation_cards.resolve_source_card)
 * carry record_type, which is what routes each cited record to its own
 * track (Mark's own correction, 2026-08-25 - the asterisks "don't make
 * sense where they're placed"):
 *   - story/quote sources get their own inline mark (StoryMark), right
 *     where the generic citation mark used to sit.
 *   - a term/figure source already carrying a word-level mark IN THIS
 *     SEGMENT is not marked again - the word itself is the mark, so a
 *     trailing ✲ on the same sentence was pure duplication.
 *   - everything else (a term/figure cited without its own word actually
 *     said, or a gravity/force/contested_claim/doctrinal_witness record)
 *     has no word or story to attach to, and moves to the General
 *     References list at the end of the turn instead of marking the
 *     running text at all.
 */
import type { Citation, FigureUsed, GlossUsed, SourceCard } from '../types/conversation';
import { FigureBridgeMark } from './FigureBridgeMark';
import { GeneralReferences } from './GeneralReferences';
import { GlossMark } from './GlossMark';
import { StoryMark } from './StoryMark';

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

const STORY_RECORD_TYPES = new Set(['story', 'quote']);

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

// Renders the segment's own text with its word-level marks, and reports
// back which record ids actually got marked here - the one piece of
// information the citation-routing step below needs to tell "already
// bridged by its own word, right in this sentence" apart from "cited,
// but nothing in the text itself earned it."
function renderSegmentText(
  segmentText: string,
  figures: FigureUsed[],
  glosses: GlossUsed[],
  usedIds: Set<string>,
  keyPrefix: string
): { nodes: React.ReactNode; markedIds: Set<string> } {
  const figureCandidates = figures.filter((f) => !usedIds.has(f.id));
  const glossCandidates = glosses.filter((g) => !usedIds.has(g.id));
  const marks = findMarks(segmentText, figureCandidates, glossCandidates);
  const markedIds = new Set<string>();
  if (!marks.length) return { nodes: segmentText, markedIds };

  const nodes: React.ReactNode[] = [];
  let cursor = 0;
  marks.forEach((mark, i) => {
    if (mark.start > cursor) nodes.push(segmentText.slice(cursor, mark.start));
    if (mark.kind === 'figure') {
      nodes.push(<FigureBridgeMark key={`${keyPrefix}-mark-${i}`} label={mark.matchedName} figure={mark.figure} />);
      usedIds.add(mark.figure.id);
      markedIds.add(mark.figure.id);
    } else {
      nodes.push(<GlossMark key={`${keyPrefix}-mark-${i}`} label={mark.matchedName} gloss={mark.gloss} />);
      usedIds.add(mark.gloss.id);
      markedIds.add(mark.gloss.id);
    }
    cursor = mark.end;
  });
  if (cursor < segmentText.length) nodes.push(segmentText.slice(cursor));
  return { nodes, markedIds };
}

function splitCitationSources(sources: SourceCard[]): { storySources: SourceCard[]; otherSources: SourceCard[] } {
  const storySources: SourceCard[] = [];
  const otherSources: SourceCard[] = [];
  for (const card of sources) {
    (STORY_RECORD_TYPES.has(card.record_type) ? storySources : otherSources).push(card);
  }
  return { storySources, otherSources };
}

export function VoiceTurnBody({ text, citations, figuresUsed = [], glosses = [] }: VoiceTurnBodyProps) {
  const segments = splitIntoSegments(text, citations);
  const usedIds = new Set<string>();
  const generalReferences: SourceCard[] = [];
  const seenReferenceIds = new Set<string>();

  const rendered = segments.map((segment, i) => {
    const { nodes, markedIds } = renderSegmentText(segment.text, figuresUsed, glosses, usedIds, `seg${i}`);

    let trailingMark: React.ReactNode = null;
    if (segment.citation) {
      const { storySources, otherSources } = splitCitationSources(segment.citation.sources);
      if (storySources.length) {
        trailingMark = <StoryMark sources={storySources} />;
      }
      for (const card of otherSources) {
        if (markedIds.has(card.record_id)) continue; // already the word itself, right here - no second mark
        if (seenReferenceIds.has(card.record_id)) continue;
        seenReferenceIds.add(card.record_id);
        generalReferences.push(card);
      }
    }

    return (
      <span key={i}>
        {nodes}
        {trailingMark}
      </span>
    );
  });

  return (
    <div className="turn__body">
      <div>{rendered}</div>
      <GeneralReferences references={generalReferences} />
    </div>
  );
}
