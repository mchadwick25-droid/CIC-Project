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
import type { GlossUsed, LexiconTerm } from '../types/conversation';

function glossToLexiconTerm(g: GlossUsed): LexiconTerm {
  const quickMeaning =
    g.category === 'A'
      ? `Confirmed reading: "${g.gloss}" - the period term is "${g.original}."`
      : `Confirmed reading: this phrase refers to ${g.gloss}.`;
  const explanation =
    g.category === 'A'
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
  gloss: GlossUsed;
}

/** Every non-overlapping occurrence of any gloss's `rendered` string in `text`, left to right. */
function findGlossMatches(text: string, glosses: GlossUsed[]): Match[] {
  const matches: Match[] = [];
  for (const gloss of glosses) {
    if (!gloss.rendered) continue;
    let fromIndex = 0;
    while (fromIndex <= text.length) {
      const foundAt = text.indexOf(gloss.rendered, fromIndex);
      if (foundAt === -1) break;
      matches.push({ index: foundAt, length: gloss.rendered.length, gloss });
      fromIndex = foundAt + gloss.rendered.length;
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
  onDetailClick?: (term: LexiconTerm) => void;
}

export function GlossHighlightedText({ text, glossesUsed, onDetailClick }: GlossHighlightedTextProps) {
  if (!glossesUsed || glossesUsed.length === 0) {
    return <>{text}</>;
  }

  const matches = findGlossMatches(text, glossesUsed);
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
        key={`${match.index}-${match.gloss.original}`}
        term={glossToLexiconTerm(match.gloss)}
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
export function ComposedLine({ line, glossesUsed, termMap, allowedTermKeys, onGlossClick, onTermClick }: ComposedLineProps) {
  const glosses = glossesUsed && glossesUsed.length > 0 ? glossesUsed : null;
  const matches = glosses ? findGlossMatches(line, glosses) : [];

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
        key={`gloss-${match.index}-${match.gloss.original}`}
        term={glossToLexiconTerm(match.gloss)}
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
