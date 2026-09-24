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
 *
 * TWO RENDERERS LIVE HERE. `renderFromElements` (the default) reads
 * engine.m4.transparency_plan's own `sentences`/`elements` and places every
 * mark by offset (R31, R31-A, R31-B; Decision-Log.md Entry 69) - see its
 * own comment. `renderLegacy` is everything above, unchanged: it rebuilds
 * marks by searching the finished text for each citation's own sentence,
 * and draws any turn whose plan predates per-element placement (a stored
 * transcript), or every turn when VITE_TRANSPARENCY_ANCHOR_RENDERER is
 * "off" (lib/flags.ts).
 */
import type { Citation, FigureUsed, GlossUsed, SourceCard, TransparencyElement, TransparencyPlan } from '../types/conversation';
import { useAnchorRenderer } from '../lib/flags';
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
  transparency?: TransparencyPlan;
}

interface Segment {
  text: string;
  citation: Citation | null;
}

type Mark = { start: number; end: number; matchedName: string; kind: 'figure'; figure: FigureUsed } | { start: number; end: number; matchedName: string; kind: 'gloss'; gloss: GlossUsed };

const STORY_RECORD_TYPES = new Set(['story', 'quote']);
const WITNESS_RECORD_TYPES = new Set(['doctrinal_witness']);

// R9 (RULED a, 2026-09-21): "Contested" and "Inferential-Thin" are two of
// the five formation_confidence values (CLAUDE.md's own vocabulary,
// engine/m1/schemas.py) that name real scholarly uncertainty rather than
// a well-attested claim - the two this ruling's "contested or thin-
// evidence claims" covers. transparency.anchors carries each cited
// record's confidence envelope verbatim (transparency_plan.py), computed
// but never rendered until this ruling; nothing else in this module reads
// or renders any other confidence field.
const THIN_EVIDENCE_CONFIDENCE_LEVELS = new Set(['Contested', 'Inferential-Thin']);

function isContested(confidence: Record<string, unknown> | null): boolean {
  const level = confidence?.formation_confidence;
  return typeof level === 'string' && THIN_EVIDENCE_CONFIDENCE_LEVELS.has(level);
}

// R17 (RULED, house rule; Rulings-Pending.md, Decision-Log.md Entry 29) -
// Adjusted-Design.md's own N2 note splits it into an M7 instrument
// (engine/m7/instruments.py's level1_element_density, already built and
// merged) and this: the renderer fixture test + enforcement it names as
// the other engineering half. The cap number/formula and drop order
// below are Mark's own confirmed answer this session, not invented here:
// a small, capped number of inline Level-1 elements per turn, scaling
// gently with sentence count - floor of 3 so even a short turn isn't
// capped away entirely, ceiling of 8 regardless of length, roughly one
// mark per two sentences in between. Over cap, drop order is glosses
// first, then figures, then stories - quote marks (someone else's actual
// quoted words) NEVER drop, the highest-stakes case for silently losing a
// citation. A dropped mark still reaches the participant via
// the collapsed General References line below - only its inline
// prominence is lost, never its disclosure.
function capForSentences(sentences: number): number {
  return Math.max(3, Math.min(8, Math.ceil(sentences / 2)));
}

type CandidateKind = 'gloss' | 'figure' | 'story' | 'witness' | 'quote';

interface Candidate {
  key: string;
  kind: CandidateKind;
}

// Drops whole candidates (never a partial mark) from the lowest-priority
// kind first. Within a kind, drops the MOST RECENTLY occurring ones
// first, keeping earlier disclosures visible - R17 doesn't specify this
// tie-break, so it's a documented default, not an implicit accident.
function selectDropped(candidates: Candidate[], cap: number): Set<string> {
  const dropped = new Set<string>();
  let over = candidates.length - cap;
  if (over <= 0) return dropped;
  for (const kind of ['gloss', 'figure', 'story'] as const) {
    if (over <= 0) break;
    const ofKind = candidates.filter((c) => c.kind === kind);
    for (let i = ofKind.length - 1; i >= 0 && over > 0; i--) {
      dropped.add(ofKind[i].key);
      over--;
    }
  }
  return dropped;
}

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

// THE LEGACY RENDERER (kept byte-for-byte; default until the flag below is
// explicitly on). Reconstructs marks and General References client-side by
// searching for each citation's own sentence in the finished text - the
// approach Build-Plan.md Stage 3c replaces, because it has a real,
// measured completeness gap: engine.m4.transparency_plan's own docstring
// names it directly - a non-consecutive repeat citation of the same story
// or witness record is silently dropped (renderedStoryIds/
// renderedWitnessIds correctly suppress a second inline mark, but
// story/witness sources are never passed to addReference, so the repeat's
// sourcing disappears rather than moving to General References). See
// renderFromElements below for the fix.
function renderLegacy({ text, citations, figuresUsed = [], glosses = [] }: VoiceTurnBodyProps) {
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

// THE ELEMENT RENDERER (R31, R31-A, R31-B; Decision-Log.md Entry 69).
// Reads engine.m4.transparency_plan's own `sentences`/`elements` and
// places every mark by offset - nothing is searched for in the text:
// - a quote element's ✲ follows its quoted words;
// - a story element's ✲ ends its telling (the run's last sentence);
// - a term/figure element is the word itself (GlossMark/FigureBridgeMark);
// - every other cited record is a general reference, listed at the end.
// One mark per element, never merged: two elements on one sentence are
// two marks in two places, and share a spot only when they genuinely end
// at the same character.
//
// R10: a repeat element (a record's later run) keeps its mark at reduced
// opacity (.citation-mark--repeat). R9: an element whose record reads
// Contested or Inferential-Thin renders hollow (.citation-mark--contested).
// R17: the cap scales with the engine's own sentence count; over cap,
// glosses drop first, then figures, then stories, newest first. Quote
// marks never drop (the reviewer's ruling on Entry 69's Q4 - the one mark
// saying "these exact words are a source's"). A dropped mark still
// reaches the end list: inline prominence is lost, never disclosure.
type ElementNode = { start: number; end: number; node: React.ReactNode };

function renderFromElements({ text, figuresUsed = [], glosses = [], transparency }: VoiceTurnBodyProps & { transparency: TransparencyPlan }) {
  const sentences = transparency.sentences ?? [];
  const cardById = new Map(transparency.references.map((card) => [card.record_id, card]));
  const figureById = new Map(figuresUsed.map((f) => [f.id, f]));
  const glossById = new Map(glosses.map((g) => [g.id, g]));

  const placeable = (transparency.elements ?? []).filter((el) => {
    const span = sentences[el.sentence_index];
    if (!span || span.text_start === null || span.text_end === null) return false;
    if (el.kind === 'term') return glossById.has(el.record_id);
    if (el.kind === 'figure') return figureById.has(el.record_id);
    return cardById.has(el.record_id);
  });

  // Word marks may not overlap; the later one renders as plain text.
  const overlapped = new Set<TransparencyElement>();
  const lastWordEnd = new Map<number, number>();
  for (const el of placeable) {
    if (el.kind !== 'term' && el.kind !== 'figure') continue;
    if (el.char_start < (lastWordEnd.get(el.sentence_index) ?? 0)) overlapped.add(el);
    else lastWordEnd.set(el.sentence_index, el.char_end);
  }
  const drawn = placeable.filter((el) => !overlapped.has(el));

  const candidates: Candidate[] = drawn.map((el, i) => ({ key: `el:${i}`, kind: el.kind === 'term' ? 'gloss' : el.kind }));
  const droppedKeys = selectDropped(candidates, capForSentences(sentences.length));

  const inlineMarkedIds = new Set<string>();
  const bySentence = new Map<number, ElementNode[]>();
  drawn.forEach((el, i) => {
    if (droppedKeys.has(`el:${i}`)) return;
    let node: React.ReactNode;
    const key = `el${i}`;
    if (el.kind === 'term') node = <GlossMark key={key} label={el.surface} gloss={glossById.get(el.record_id)!} />;
    else if (el.kind === 'figure') node = <FigureBridgeMark key={key} label={el.surface} figure={figureById.get(el.record_id)!} />;
    else
      node = (
        <StoryMark key={key} sources={[cardById.get(el.record_id)!]} repeat={el.repeat} contested={isContested(el.confidence)} quote={el.kind === 'quote'} />
      );
    inlineMarkedIds.add(el.record_id);
    const isWord = el.kind === 'term' || el.kind === 'figure';
    const list = bySentence.get(el.sentence_index) ?? [];
    list.push({ start: isWord ? el.char_start : el.char_end, end: el.char_end, node });
    bySentence.set(el.sentence_index, list);
  });

  const renderSentence = (body: string, nodes: ElementNode[]): React.ReactNode[] => {
    const out: React.ReactNode[] = [];
    let cursor = 0;
    // Words before points at the same offset; a point never splits a word.
    const ordered = [...nodes].sort((a, b) => a.start - b.start || b.end - b.start - (a.end - a.start));
    for (const item of ordered) {
      const at = Math.max(item.start, cursor);
      if (at > cursor) out.push(body.slice(cursor, at));
      out.push(item.node);
      cursor = Math.max(cursor, item.start === item.end ? at : item.end);
    }
    if (cursor < body.length) out.push(body.slice(cursor));
    return out;
  };

  const rendered: React.ReactNode[] = [];
  let cursor = 0;
  sentences.forEach((span) => {
    if (span.text_start === null || span.text_end === null || span.text_start < cursor) return;
    if (span.text_start > cursor) rendered.push(text.slice(cursor, span.text_start));
    rendered.push(<span key={`s${span.index}`}>{renderSentence(text.slice(span.text_start, span.text_end), bySentence.get(span.index) ?? [])}</span>);
    cursor = span.text_end;
  });
  if (cursor < text.length) rendered.push(text.slice(cursor));

  const generalReferences = transparency.references.filter((card) => !inlineMarkedIds.has(card.record_id));

  return (
    <div className="turn__body">
      <div>{rendered}</div>
      <GeneralReferences references={generalReferences} />
    </div>
  );
}

export function VoiceTurnBody(props: VoiceTurnBodyProps) {
  const plan = props.transparency;
  if (useAnchorRenderer && plan?.elements && plan.sentences) {
    return renderFromElements({ ...props, transparency: plan });
  }
  return renderLegacy(props);
}
