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
 * track rather than a single generic asterisk placed without regard to
 * what's actually being cited:
 *   - story/quote sources get their own inline mark (StoryMark), right
 *     where the generic citation mark used to sit.
 *   - doctrinal_witness sources get their own inline mark too
 *     (WitnessMark) - same reasoning, different copy: a witness sentence
 *     is the build's own reviewed synthesis of real sources, not a story
 *     or a verbatim quote, and reads as freely generated when its
 *     sourcing only shows up in the collapsed end-of-turn list instead of
 *     inline, even when the underlying synthesis is fully grounded.
 *   - a term/figure source already carrying a word-level mark ANYWHERE
 *     EARLIER IN THIS TURN is not marked again - the word itself is the
 *     mark, so a General-Reference entry for the same id later in the
 *     same turn would be pure duplication, one sentence further apart
 *     (checked against `usedIds`, the turn-scoped set every word mark
 *     already accumulates into - not a second, segment-scoped set, which
 *     is exactly what let this duplication back in the first pass).
 *   - everything else (a term/figure cited without its own word actually
 *     said, or a gravity/force/contested_claim record) has no word or
 *     story to attach to, and moves to the General References list at
 *     the end of the turn instead of marking the running text at all.
 *     This includes any citation whose own sentence didn't survive
 *     verbatim in the finished text (splitIntoSegments' own `orphaned`
 *     list) - its sources still deserve disclosure, just not an inline
 *     position to anchor a mark to.
 */
import type { Citation, FigureUsed, GlossUsed, SourceCard } from '../types/conversation';
import { FigureBridgeMark } from './FigureBridgeMark';
import { GeneralReferences } from './GeneralReferences';
import { GlossMark } from './GlossMark';
import { StoryMark } from './StoryMark';
import { WitnessMark } from './WitnessMark';

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
const WITNESS_RECORD_TYPES = new Set(['doctrinal_witness']);

function splitIntoSegments(text: string, citations: Citation[]): { segments: Segment[]; orphaned: Citation[] } {
  const segments: Segment[] = [];
  const orphaned: Citation[] = [];
  let remaining = text;
  for (const citation of citations) {
    const idx = remaining.indexOf(citation.sentence);
    if (idx === -1) {
      // the sentence didn't survive verbatim in this text (paraphrased,
      // or emptied by the citation-verification net) - there's no inline
      // position left to anchor a mark to, but the sources are still
      // real and still owed disclosure; the caller routes these to
      // General References rather than dropping them.
      orphaned.push(citation);
      continue;
    }
    const before = remaining.slice(0, idx + citation.sentence.length);
    segments.push({ text: before, citation });
    remaining = remaining.slice(idx + citation.sentence.length);
  }
  if (remaining) segments.push({ text: remaining, citation: null });
  return { segments, orphaned };
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

// Renders the segment's own text with its word-level marks, mutating
// `usedIds` (turn-scoped, owned by the caller) as each mark fires - the
// one piece of state the citation-routing step below needs to tell
// "already bridged by its own word, somewhere in this turn" apart from
// "cited, but nothing in the text itself earned it."
function renderSegmentText(segmentText: string, figures: FigureUsed[], glosses: GlossUsed[], usedIds: Set<string>, keyPrefix: string): React.ReactNode {
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

function splitCitationSources(sources: SourceCard[]): { storySources: SourceCard[]; witnessSources: SourceCard[]; otherSources: SourceCard[] } {
  const storySources: SourceCard[] = [];
  const witnessSources: SourceCard[] = [];
  const otherSources: SourceCard[] = [];
  for (const card of sources) {
    if (STORY_RECORD_TYPES.has(card.record_type)) storySources.push(card);
    else if (WITNESS_RECORD_TYPES.has(card.record_type)) witnessSources.push(card);
    else otherSources.push(card);
  }
  return { storySources, witnessSources, otherSources };
}

export function VoiceTurnBody({ text, citations, figuresUsed = [], glosses = [] }: VoiceTurnBodyProps) {
  const { segments, orphaned } = splitIntoSegments(text, citations);
  const usedIds = new Set<string>();
  const generalReferences: SourceCard[] = [];
  const seenReferenceIds = new Set<string>();

  // Shared by both the per-segment routing below and the orphaned-
  // citation sweep after it, so "already word-marked" and "already
  // listed" mean the same thing in both places rather than two
  // independently-maintained dedupe rules drifting apart.
  const addReference = (card: SourceCard) => {
    if (usedIds.has(card.record_id) || seenReferenceIds.has(card.record_id)) return;
    seenReferenceIds.add(card.record_id);
    generalReferences.push(card);
  };

  // ONE ✲ per story/quote source per turn, after the telling ends -
  // never one per cited sentence. Rendering the engine's per-sentence
  // citation grain 1:1 would draw one identical mark per sentence for a
  // story told across several sentences - the design's own grammar is
  // sparse: dotted-underline words plus the ✲, placed after THE sentence
  // that told the story - singular. A card renders at the last segment of
  // the contiguous run of sentences citing its record; a non-consecutive
  // re-cite later in the turn renders nothing more. The citation DATA
  // is untouched - verification stays per-sentence; only the marks
  // thin out.
  const segmentStoryCards = segments.map((segment) =>
    segment.citation ? splitCitationSources(segment.citation.sources).storySources : []
  );
  const segmentWitnessCards = segments.map((segment) =>
    segment.citation ? splitCitationSources(segment.citation.sources).witnessSources : []
  );
  const renderedStoryIds = new Set<string>();
  const renderedWitnessIds = new Set<string>();

  const rendered = segments.map((segment, i) => {
    const nodes = renderSegmentText(segment.text, figuresUsed, glosses, usedIds, `seg${i}`);

    const marks: React.ReactNode[] = [];
    if (segment.citation) {
      const { otherSources } = splitCitationSources(segment.citation.sources);

      const nextStoryIds = new Set((segmentStoryCards[i + 1] ?? []).map((c) => c.record_id));
      const finishingStoryCards = segmentStoryCards[i].filter((card) => {
        if (renderedStoryIds.has(card.record_id)) return false;
        if (nextStoryIds.has(card.record_id)) return false; // still being told - mark where the telling ends
        return true;
      });
      if (finishingStoryCards.length) {
        finishingStoryCards.forEach((card) => renderedStoryIds.add(card.record_id));
        marks.push(<StoryMark key="story" sources={finishingStoryCards} />);
      }

      const nextWitnessIds = new Set((segmentWitnessCards[i + 1] ?? []).map((c) => c.record_id));
      const finishingWitnessCards = segmentWitnessCards[i].filter((card) => {
        if (renderedWitnessIds.has(card.record_id)) return false;
        if (nextWitnessIds.has(card.record_id)) return false; // same run still citing it - mark where the run ends
        return true;
      });
      if (finishingWitnessCards.length) {
        finishingWitnessCards.forEach((card) => renderedWitnessIds.add(card.record_id));
        marks.push(<WitnessMark key="witness" sources={finishingWitnessCards} />);
      }

      otherSources.forEach(addReference);
    }

    return (
      <span key={i}>
        {nodes}
        {marks}
      </span>
    );
  });

  // Orphaned citations have no surviving sentence to anchor an inline
  // mark to - even a story/quote source among them goes to General
  // References rather than a StoryMark, since there's nowhere left to
  // place one.
  orphaned.forEach((citation) => citation.sources.forEach(addReference));

  return (
    <div className="turn__body">
      <div>{rendered}</div>
      <GeneralReferences references={generalReferences} />
    </div>
  );
}
