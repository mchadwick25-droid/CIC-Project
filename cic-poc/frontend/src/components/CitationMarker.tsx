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
  // See LexiconHighlight's identical ref for the full rationale - tracks
  // the pointer type of the most recent pointerdown on this marker so
  // handleClick can tell a touch tap from a desktop click, per-interaction
  // rather than via a one-time device/viewport check.
  const lastPointerTypeRef = useRef<string>('mouse');

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

  // Read FRESH from the ref every time - see LexiconHighlight's identical
  // isTouch() for why this must be a function, not a render-scoped const
  // (a real stale-closure bug caught in testing: a captured boolean would
  // reflect whatever the ref held at the LAST render, not what pointerdown
  // just set it to, since mutating a ref doesn't itself trigger a render).
  const isTouch = () => lastPointerTypeRef.current === 'touch';

  // Touch-only outside-tap dismiss - mirrors LexiconHighlight's identical
  // effect. Declared before the citations-empty early return below so hook
  // order stays unconditional across renders (Rules of Hooks).
  useEffect(() => {
    if (!showTooltip || !isTouch()) {
      return;
    }
    const handleOutsidePointerDown = (event: PointerEvent) => {
      if (markerRef.current && !markerRef.current.contains(event.target as Node)) {
        setShowTooltip(false);
      }
    };
    document.addEventListener('pointerdown', handleOutsidePointerDown, true);
    return () => {
      document.removeEventListener('pointerdown', handleOutsidePointerDown, true);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [showTooltip]);

  if (!citations || citations.length === 0) {
    return null;
  }

  // Two-tier (2026-08-10). The marker's count is DRAWN-ON sources only -
  // that number is a promise about this turn's text, and padding it with
  // consulted sources would make the promise false. Consulted entries still
  // appear, below the drawn-on ones and labelled as what they are.
  const isDrawnOn = (c: Citation) => c.grounded !== false;
  const drawnOn = citations.filter(isDrawnOn);
  const consulted = citations.filter((c) => !isDrawnOn(c));
  const ordered = [...drawnOn, ...consulted];

  const handlePointerDown = (event: React.PointerEvent<HTMLSpanElement>) => {
    lastPointerTypeRef.current = event.pointerType;
  };

  const handleClick = () => {
    if (isTouch()) {
      // Phone tap grammar (Build Handoff Increment 1 V1.0 §3): a tap shows
      // the Level-2 popover only, same as LexiconHighlight.
      setShowTooltip(true);
      return;
    }
    if (onDetailClick) {
      onDetailClick(citations);
    }
  };

  const handleFullSourcesClick = (event: React.MouseEvent) => {
    event.stopPropagation();
    setShowTooltip(false);
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
      onPointerDown={handlePointerDown}
      onClick={handleClick}
      aria-label={
        `${drawnOn.length} source${drawnOn.length === 1 ? '' : 's'} drawn on for this turn` +
        (consulted.length ? `, ${consulted.length} more consulted` : '')
      }
    >
      <span className="citation-marker__icon">&#x2732;</span>
      {drawnOn.length > 1 && (
        <span className="citation-marker__count">{drawnOn.length}</span>
      )}
      {showTooltip && (
        <div className={`citation-tooltip citation-tooltip--${tooltipPosition}`}
          style={{ '--tooltip-shift': `${tooltipShift}px` } as React.CSSProperties}
        >
          <div className="citation-tooltip__list">
            {ordered.slice(0, 4).map((citation, index) => (
              <div
                key={index}
                className={`citation-tooltip__item${isDrawnOn(citation) ? '' : ' citation-tooltip__item--consulted'}`}
              >
                <span className={`citation-tooltip__kind citation-tooltip__kind--${citation.type || 'lexicon'}`}>
                  {citation.type === 'story' ? 'Story' : 'Term'}
                </span>
                <span className="citation-tooltip__term">{citation.term}</span>
                {!isDrawnOn(citation) && (
                  <span className="citation-tooltip__tier">consulted</span>
                )}
              </div>
            ))}
            {ordered.length > 4 && (
              <div className="citation-tooltip__more">+{ordered.length - 4} more</div>
            )}
          </div>
          <button
            type="button"
            className="citation-tooltip__footer"
            onClick={handleFullSourcesClick}
          >
            {isTouch() ? 'Full entry →' : 'Click for full sources'}
          </button>
        </div>
      )}
    </span>
  );
}
