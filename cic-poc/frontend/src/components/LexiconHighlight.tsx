/**
 * LexiconHighlight component - highlights lexicon terms with hover tooltips.
 */

import { useState, useRef, useEffect } from 'react';
import type { LexiconTerm } from '../types/conversation';

interface LexiconHighlightProps {
  term: LexiconTerm;
  matchedText: string;
  onDetailClick?: (term: LexiconTerm) => void;
}

export function LexiconHighlight({
  term,
  matchedText,
  onDetailClick,
}: LexiconHighlightProps) {
  const [showTooltip, setShowTooltip] = useState(false);
  const [tooltipPosition, setTooltipPosition] = useState<'above' | 'below'>('above');
  const [tooltipShift, setTooltipShift] = useState(0);
  const spanRef = useRef<HTMLSpanElement>(null);
  const tooltipRef = useRef<HTMLDivElement>(null);

  const TOOLTIP_WIDTH = 280;
  const VIEWPORT_MARGIN = 12;

  useEffect(() => {
    if (showTooltip && spanRef.current) {
      const rect = spanRef.current.getBoundingClientRect();
      const spaceAbove = rect.top;
      const spaceBelow = window.innerHeight - rect.bottom;

      // Position tooltip where there's more space
      setTooltipPosition(spaceAbove > spaceBelow ? 'above' : 'below');

      // Tooltip is centered on the term by default (shift 0). Clamp it
      // horizontally so it doesn't run off the left/right of the viewport.
      const termCenter = rect.left + rect.width / 2;
      const idealLeft = termCenter - TOOLTIP_WIDTH / 2;
      const idealRight = termCenter + TOOLTIP_WIDTH / 2;

      let shift = 0;
      if (idealLeft < VIEWPORT_MARGIN) {
        shift = VIEWPORT_MARGIN - idealLeft;
      } else if (idealRight > window.innerWidth - VIEWPORT_MARGIN) {
        shift = window.innerWidth - VIEWPORT_MARGIN - idealRight;
      }
      setTooltipShift(shift);
    }
  }, [showTooltip]);

  const handleClick = () => {
    if (onDetailClick) {
      onDetailClick(term);
    }
  };

  return (
    <span
      ref={spanRef}
      className="lexicon-term"
      onMouseEnter={() => setShowTooltip(true)}
      onMouseLeave={() => setShowTooltip(false)}
      onClick={handleClick}
    >
      {matchedText}
      {showTooltip && (
        <div
          ref={tooltipRef}
          className={`lexicon-tooltip lexicon-tooltip--${tooltipPosition}`}
          style={{ '--tooltip-shift': `${tooltipShift}px` } as React.CSSProperties}
        >
          <div className="lexicon-tooltip__header">
            {term.term.split('/')[0].replace(/\s*\([^)]*\)\s*/g, '').trim()}
          </div>
          <div className="lexicon-tooltip__content">
            {term.quick_meaning || 'No definition available.'}
          </div>
          <div className="lexicon-tooltip__footer">
            Click for full entry
          </div>
        </div>
      )}
    </span>
  );
}

function buildTermPattern(termMap: Map<string, LexiconTerm>): RegExp | null {
  const termKeys = Array.from(termMap.keys())
    .filter((key) => key.length > 2)
    .sort((a, b) => b.length - a.length); // Longer terms first

  if (termKeys.length === 0) {
    return null;
  }

  const escapedKeys = termKeys.map((key) =>
    key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  );

  return new RegExp(`\\b(${escapedKeys.join('|')})\\b`, 'gi');
}

/**
 * Returns the lowercased term-map keys matched in `text`, in order of
 * appearance (duplicates included). Shared between HighlightedText's actual
 * rendering pass and callers that need to know what a message would match
 * without rendering it (e.g. computing which terms are "new" this message).
 */
export function getTermMatches(text: string, termMap: Map<string, LexiconTerm>): string[] {
  const pattern = buildTermPattern(termMap);
  if (!pattern) {
    return [];
  }
  const matches: string[] = [];
  let match;
  while ((match = pattern.exec(text)) !== null) {
    matches.push(match[0].toLowerCase());
  }
  return matches;
}

interface HighlightedTextProps {
  text: string;
  termMap: Map<string, LexiconTerm>;
  onDetailClick?: (term: LexiconTerm) => void;
  /**
   * When provided, only matches whose lowercased key is in this set are
   * rendered as interactive highlights - everything else renders as plain
   * text. Used to show a term's hover/click treatment only the first time
   * it appears across the conversation, not on every repeated occurrence.
   * When omitted, every match is highlighted (back-compat default).
   *
   * Read-only - never mutated. If the same key appears more than once in
   * `text`, only the first occurrence within this call highlights (tracked
   * locally, not via mutating this set). Cross-line/cross-message dedup is
   * the caller's responsibility: only include a key here for the one
   * line/message it should actually appear in - see MessageBubble, which
   * precomputes this per line before rendering rather than sharing one
   * mutable set across calls (mutating a shared prop during render breaks
   * under React StrictMode's double-invocation of render).
   */
  allowedKeys?: Set<string>;
}

/**
 * Renders text with lexicon terms highlighted and interactive.
 */
export function HighlightedText({
  text,
  termMap,
  onDetailClick,
  allowedKeys,
}: HighlightedTextProps) {
  if (termMap.size === 0) {
    return <>{text}</>;
  }

  const pattern = buildTermPattern(termMap);
  if (!pattern) {
    return <>{text}</>;
  }

  const parts: (string | JSX.Element)[] = [];
  let lastIndex = 0;
  let match;
  // Local only, discarded when this call returns - never exposed as a prop,
  // so it's safe under React StrictMode's double-invocation of render (each
  // invocation gets its own fresh, independent copy). This is what prevents
  // a term appearing twice within this SAME text from highlighting twice;
  // duplicates across different lines/messages are already excluded by the
  // caller only including a key in `allowedKeys` for the one line it should
  // appear in - see MessageBubble.
  const usedInThisCall = new Set<string>();

  while ((match = pattern.exec(text)) !== null) {
    // Add text before match
    if (match.index > lastIndex) {
      parts.push(text.slice(lastIndex, match.index));
    }

    // Add highlighted term
    const matchedText = match[0];
    const key = matchedText.toLowerCase();
    const term = termMap.get(key);
    const isAllowed = (!allowedKeys || allowedKeys.has(key)) && !usedInThisCall.has(key);
    if (isAllowed) {
      usedInThisCall.add(key);
    }

    if (term && isAllowed) {
      parts.push(
        <LexiconHighlight
          key={`${match.index}-${matchedText}`}
          term={term}
          matchedText={matchedText}
          onDetailClick={onDetailClick}
        />
      );
    } else {
      parts.push(matchedText);
    }

    lastIndex = pattern.lastIndex;
  }

  // Add remaining text
  if (lastIndex < text.length) {
    parts.push(text.slice(lastIndex));
  }

  return <>{parts}</>;
}
