/**
 * Renders the confirmed inline-gloss pattern (modern gloss (original term) /
 * original phrase (modern reference)) as interactive spans - the same
 * hover/click affordance LexiconHighlight already gives bare lexicon terms,
 * applied to a different detection signal.
 *
 * Deliberately a separate detection pass from LexiconHighlight's alias-regex
 * matching, not an extension of it: that component matches single words
 * against a term map with `\b` word boundaries, which is the wrong tool for
 * a multi-word phrase like "a sign tied to a hidden truth (raza)" - regex
 * alternation across ~20 long phrases is fragile and slow next to a plain
 * substring scan, and the source signal here is fundamentally different
 * anyway: glosses_used is a short, exact, backend-verified list of strings
 * actually present in this one message (see confirmed_glosses.py's
 * find_glosses_used), not a term list to search broadly against.
 *
 * Reuses LexiconHighlight itself for the actual rendering (hover tooltip,
 * touch-vs-mouse click grammar, viewport-aware positioning) rather than
 * duplicating that logic - a GlossUsed item is adapted into a
 * LexiconTerm-shaped object so the same battle-tested component renders it.
 */

import { HighlightedText, LexiconHighlight } from './LexiconHighlight';
import type { FigureUsed, GlossUsed, LexiconTerm } from '../types/conversation';

/**
 * The name bridge (2026-08-09). Mark's live-site read found the transparency
 * gap is mostly NAMES, not vocabulary - a reader meets Aphrahat or Blaesilla
 * and has nothing. Figures ride the same rendering path as glosses because
 * the affordance is identical from the reader's side: a marked span, a hover,
 * a plain sentence. Only the copy differs, and it is deliberately spare - the
 * bridge_line is authored from that world's own figure record, so there is no
 * "confirmed reading" framing to add and nothing to editorialize.
 */
function figureToLexiconTerm(f: FigureUsed): LexiconTerm {
  return {
    term: f.display_name,
    aliases: [],
    quick_meaning: f.bridge_line,
    full_content: `## Who This Was\n${f.bridge_line}`,
    related_terms: [],
  };
}

function glossToLexiconTerm(g: GlossUsed): LexiconTerm {
  // Plain-side (tier 3): what is on screen is the ordinary English. The
  // reader is not stuck on a hard word, so explaining one would be beside
  // the point - what they are missing is that this world had its own word,
  // and a way through to the record behind it.
  const quickMeaning = g.plain_side
    ? `This world's own word for this was "${g.original}."`
    : g.category === 'A'
      ? `Confirmed reading: "${g.gloss}" - the period term is "${g.original}."`
      : `Confirmed reading: this phrase refers to ${g.gloss}.`;
  const explanation = g.plain_side
    ? `The Representative said this plainly, which is how this world's own people would have wanted it understood. Behind the plain phrase sits a term they used among themselves - "${g.original}" - and the reading given here has been reviewed and confirmed, not improvised.`
    : g.category === 'A'
      ? `This world has its own word for this - "${g.original}." The plain-language reading given here, "${g.gloss}," has been reviewed and confirmed as the accurate modern sense, not an improvised paraphrase.`
      : `This is how someone in this world would actually have named it - the phrase itself is genuine to the period, not modernized. "${g.gloss}" is what it refers to, confirmed against the historical record.`;
  return {
    term: g.original,
    aliases: [],
    quick_meaning: quickMeaning,
    full_content: `## What This Means\n${explanation}`,
    related_terms: [],
  };
}

interface Match {
  index: number;
  length: number;
  term: LexiconTerm;
  /** stable per-match React key fragment */
  key: string;
}

/**
 * Every occurrence of a named figure, CASE-SENSITIVELY - a name is a proper
 * noun, and the backend learned the same lesson (an ignore-case match put an
 * evangelist's panel on "mark the day"). Only the FIRST mention is marked:
 * a Representative naming Ambrose four times should not produce four
 * identical pills in one paragraph.
 */
function findFigureMatches(text: string, figures: FigureUsed[]): Match[] {
  const matches: Match[] = [];
  for (const figure of figures) {
    const needle = figure.matched;
    if (!needle) continue;
    const foundAt = text.indexOf(needle);
    if (foundAt === -1) continue;
    matches.push({
      index: foundAt,
      length: needle.length,
      term: figureToLexiconTerm(figure),
      key: `figure-${figure.figure_id}`,
    });
  }
  return matches;
}

/**
 * Gloss matches and figure matches merged into one left-to-right list with
 * overlaps dropped. Merging BEFORE rendering rather than running two passes
 * is what keeps a figure name that sits inside a gloss phrase from being
 * highlighted twice, nested - the same reason ComposedLine carves plain
 * segments out for the bare-alias matcher instead of letting it re-scan.
 */
function mergeMatches(...groups: Match[][]): Match[] {
  const all = groups.flat().sort((a, b) => a.index - b.index);
  const kept: Match[] = [];
  let lastEnd = -1;
  for (const m of all) {
    if (m.index >= lastEnd) {
      kept.push(m);
      lastEnd = m.index + m.length;
    }
  }
  return kept;
}

/**
 * Every non-overlapping occurrence of any gloss's `rendered` string in
 * `text`, left to right. Case-insensitive - a Representative opening a
 * sentence with a gloss capitalizes its first letter ("A transformative
 * knowing of God (gnosis)..."), which a case-sensitive match would miss
 * (caught in production verification: the backend's own detection had the
 * same bug - see confirmed_glosses.py's find_glosses_used). Matching is
 * done against lowercased copies; `index`/`length` still index into the
 * ORIGINAL `text`, so the rendered highlight preserves whatever casing the
 * Representative actually used rather than forcing lowercase.
 */
function findGlossMatches(text: string, glosses: GlossUsed[]): Match[] {
  const matches: Match[] = [];
  const lowerText = text.toLowerCase();
  for (const gloss of glosses) {
    // Tier-2 fallback (gloss-firing fix, 2026-08-09): when the voice used
    // the ORIGINAL phrase naturally without the rendered inline form
    // (backend marks these inline: false), highlight the original so the
    // participant still gets the confirmed modern reading from the UI -
    // Three-Level Transparency supplying the bridge the natural register
    // deliberately left unsaid.
    // Tier 3 (plain_side): neither the rendered form nor the period term is
    // on screen - the plain phrase is what the reader actually sees, so it
    // is what gets marked.
    const needle = gloss.plain_side
      ? gloss.gloss
      : gloss.rendered && lowerText.includes(gloss.rendered.toLowerCase())
        ? gloss.rendered
        : gloss.original;
    if (!needle) continue;
    const lowerNeedle = needle.toLowerCase();
    let fromIndex = 0;
    while (fromIndex <= lowerText.length) {
      const foundAt = lowerText.indexOf(lowerNeedle, fromIndex);
      if (foundAt === -1) break;
      matches.push({
        index: foundAt,
        length: needle.length,
        term: glossToLexiconTerm(gloss),
        key: `gloss-${gloss.original}${gloss.plain_side ? '-plain' : ''}`,
      });
      fromIndex = foundAt + needle.length;
    }
  }
  matches.sort((a, b) => a.index - b.index);
  // Drop any match that overlaps one already kept (can only happen if two
  // confirmed phrases happen to share a substring - keep the earlier one).
  const nonOverlapping: Match[] = [];
  let lastEnd = -1;
  for (const m of matches) {
    if (m.index >= lastEnd) {
      nonOverlapping.push(m);
      lastEnd = m.index + m.length;
    }
  }
  return nonOverlapping;
}

interface GlossHighlightedTextProps {
  text: string;
  glossesUsed: GlossUsed[] | null | undefined;
  figuresUsed?: FigureUsed[] | null;
  onDetailClick?: (term: LexiconTerm) => void;
}

export function GlossHighlightedText({ text, glossesUsed, figuresUsed, onDetailClick }: GlossHighlightedTextProps) {
  const hasGlosses = !!glossesUsed && glossesUsed.length > 0;
  const hasFigures = !!figuresUsed && figuresUsed.length > 0;
  if (!hasGlosses && !hasFigures) {
    return <>{text}</>;
  }

  const matches = mergeMatches(
    hasGlosses ? findGlossMatches(text, glossesUsed!) : [],
    hasFigures ? findFigureMatches(text, figuresUsed!) : []
  );
  if (matches.length === 0) {
    return <>{text}</>;
  }

  const parts: (string | JSX.Element)[] = [];
  let lastIndex = 0;
  for (const match of matches) {
    if (match.index > lastIndex) {
      parts.push(text.slice(lastIndex, match.index));
    }
    parts.push(
      <LexiconHighlight
        key={`${match.index}-${match.key}`}
        term={match.term}
        matchedText={text.slice(match.index, match.index + match.length)}
        onDetailClick={onDetailClick}
      />
    );
    lastIndex = match.index + match.length;
  }
  if (lastIndex < text.length) {
    parts.push(text.slice(lastIndex));
  }

  return <>{parts}</>;
}

interface ComposedLineProps {
  line: string;
  glossesUsed: GlossUsed[] | null | undefined;
  figuresUsed?: FigureUsed[] | null;
  termMap: Map<string, LexiconTerm>;
  allowedTermKeys?: Set<string>;
  onGlossClick?: (term: LexiconTerm) => void;
  onTermClick?: (term: LexiconTerm) => void;
}

/**
 * Drop-in replacement for a bare `HighlightedText` call: renders one line
 * with BOTH the confirmed-gloss phrases (this file) AND the existing
 * bare-alias term highlighting (LexiconHighlight.tsx) applied together,
 * without one pass re-matching text the other already claimed - a gloss
 * phrase like "a sign tied to a hidden truth (raza)" contains "raza"
 * itself, which the bare-alias matcher would otherwise also highlight as
 * its own, separate, nested span.
 *
 * Approach: carve the line into gloss-matched spans and everything else,
 * render gloss spans directly, and run the existing bare-alias highlighter
 * only over the remaining plain-text segments. One known, accepted
 * limitation: `HighlightedText`'s own first-occurrence dedup is local to
 * each call, so if the same bare term appears in two different plain
 * segments of a line that a gloss match splits apart, it could highlight
 * in both rather than only the first - rare (a line needs a gloss match in
 * the middle of two separate bare-term occurrences) and cosmetic, not a
 * correctness break, so left as a known edge case rather than a larger
 * matching-engine rewrite.
 */
export function ComposedLine({ line, glossesUsed, figuresUsed, termMap, allowedTermKeys, onGlossClick, onTermClick }: ComposedLineProps) {
  const glosses = glossesUsed && glossesUsed.length > 0 ? glossesUsed : null;
  const figures = figuresUsed && figuresUsed.length > 0 ? figuresUsed : null;
  const matches = mergeMatches(
    glosses ? findGlossMatches(line, glosses) : [],
    figures ? findFigureMatches(line, figures) : []
  );

  if (matches.length === 0) {
    return termMap.size > 0 ? (
      <HighlightedText text={line} termMap={termMap} onDetailClick={onTermClick} allowedKeys={allowedTermKeys} />
    ) : (
      <>{line}</>
    );
  }

  const parts: (string | JSX.Element)[] = [];
  let lastIndex = 0;
  matches.forEach((match, i) => {
    if (match.index > lastIndex) {
      const plainSegment = line.slice(lastIndex, match.index);
      parts.push(
        termMap.size > 0 ? (
          <HighlightedText
            key={`plain-${i}`}
            text={plainSegment}
            termMap={termMap}
            onDetailClick={onTermClick}
            allowedKeys={allowedTermKeys}
          />
        ) : (
          <span key={`plain-${i}`}>{plainSegment}</span>
        )
      );
    }
    parts.push(
      <LexiconHighlight
        key={`${match.index}-${match.key}`}
        term={match.term}
        matchedText={line.slice(match.index, match.index + match.length)}
        onDetailClick={onGlossClick}
      />
    );
    lastIndex = match.index + match.length;
  });
  if (lastIndex < line.length) {
    const plainSegment = line.slice(lastIndex);
    parts.push(
      termMap.size > 0 ? (
        <HighlightedText
          key="plain-tail"
          text={plainSegment}
          termMap={termMap}
          onDetailClick={onTermClick}
          allowedKeys={allowedTermKeys}
        />
      ) : (
        <span key="plain-tail">{plainSegment}</span>
      )
    );
  }

  return <>{parts}</>;
}
