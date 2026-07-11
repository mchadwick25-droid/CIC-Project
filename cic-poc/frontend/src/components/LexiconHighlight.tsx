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

interface HighlightedTextProps {
  text: string;
  termMap: Map<string, LexiconTerm>;
  onDetailClick?: (term: LexiconTerm) => void;
}

/**
 * Renders text with lexicon terms highlighted and interactive.
 */
export function HighlightedText({
  text,
  termMap,
  onDetailClick,
}: HighlightedTextProps) {
  if (termMap.size === 0) {
    return <>{text}</>;
  }

  // Build a regex pattern from all term keys
  const termKeys = Array.from(termMap.keys())
    .filter((key) => key.length > 2)
    .sort((a, b) => b.length - a.length); // Longer terms first

  if (termKeys.length === 0) {
    return <>{text}</>;
  }

  // Escape regex special characters
  const escapedKeys = termKeys.map((key) =>
    key.replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
  );

  const pattern = new RegExp(`\\b(${escapedKeys.join('|')})\\b`, 'gi');

  const parts: (string | JSX.Element)[] = [];
  let lastIndex = 0;
  let match;

  while ((match = pattern.exec(text)) !== null) {
    // Add text before match
    if (match.index > lastIndex) {
      parts.push(text.slice(lastIndex, match.index));
    }

    // Add highlighted term
    const matchedText = match[0];
    const term = termMap.get(matchedText.toLowerCase());

    if (term) {
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
