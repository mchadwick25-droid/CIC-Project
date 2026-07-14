/**
 * CitationMarker component - inline sourcing marker for a representative's
 * message, replacing the old always-visible "Sources" list at the bottom of
 * every message.
 *
 * Mirrors LexiconHighlight's Level 2/3 interaction pattern (hover for a
 * short summary, click for full detail) so sourcing/story citations use the
 * same consistent mechanic as lexicon terms, per Article 30's Three-Level
 * Transparency - rather than a second, differently-shaped UI for the same
 * kind of information. Anchored at message end, not per-sentence: the
 * backend currently attributes citations to a whole turn, not to the
 * specific sentence they ground, so this is the honest granularity
 * available today, not a simulated precision the data doesn't support.
 */

import { useState, useRef, useEffect } from 'react';
import type { Citation } from '../types/conversation';

interface CitationMarkerProps {
  citations: Citation[];
  onDetailClick?: (citations: Citation[]) => void;
}

export function CitationMarker({ citations, onDetailClick }: CitationMarkerProps) {
  const [showTooltip, setShowTooltip] = useState(false);
  const [tooltipPosition, setTooltipPosition] = useState<'above' | 'below'>('above');
  const [tooltipShift, setTooltipShift] = useState(0);
  const markerRef = useRef<HTMLSpanElement>(null);

  const TOOLTIP_WIDTH = 280;
  const VIEWPORT_MARGIN = 12;

  useEffect(() => {
    if (showTooltip && markerRef.current) {
      const rect = markerRef.current.getBoundingClientRect();
      const spaceAbove = rect.top;
      const spaceBelow = window.innerHeight - rect.bottom;
      setTooltipPosition(spaceAbove > spaceBelow ? 'above' : 'below');

      const markerCenter = rect.left + rect.width / 2;
      const idealLeft = markerCenter - TOOLTIP_WIDTH / 2;
      const idealRight = markerCenter + TOOLTIP_WIDTH / 2;

      let shift = 0;
      if (idealLeft < VIEWPORT_MARGIN) {
        shift = VIEWPORT_MARGIN - idealLeft;
      } else if (idealRight > window.innerWidth - VIEWPORT_MARGIN) {
        shift = window.innerWidth - VIEWPORT_MARGIN - idealRight;
      }
      setTooltipShift(shift);
    }
  }, [showTooltip]);

  if (!citations || citations.length === 0) {
    return null;
  }

  const handleClick = () => {
    if (onDetailClick) {
      onDetailClick(citations);
    }
  };

  return (
    <span
      ref={markerRef}
      className="citation-marker"
      onMouseEnter={() => setShowTooltip(true)}
      onMouseLeave={() => setShowTooltip(false)}
      onClick={handleClick}
      aria-label={`${citations.length} source${citations.length > 1 ? 's' : ''} for this turn`}
    >
      <span className="citation-marker__icon">&#x2732;</span>
      {citations.length > 1 && (
        <span className="citation-marker__count">{citations.length}</span>
      )}
      {showTooltip && (
        <div className={`citation-tooltip citation-tooltip--${tooltipPosition}`}
          style={{ '--tooltip-shift': `${tooltipShift}px` } as React.CSSProperties}
        >
          <div className="citation-tooltip__list">
            {citations.slice(0, 4).map((citation, index) => (
              <div key={index} className="citation-tooltip__item">
                <span className={`citation-tooltip__kind citation-tooltip__kind--${citation.type || 'lexicon'}`}>
                  {citation.type === 'story' ? 'Story' : 'Term'}
                </span>
                <span className="citation-tooltip__term">{citation.term}</span>
              </div>
            ))}
            {citations.length > 4 && (
              <div className="citation-tooltip__more">+{citations.length - 4} more</div>
            )}
          </div>
          <div className="citation-tooltip__footer">Click for full sources</div>
        </div>
      )}
    </span>
  );
}
