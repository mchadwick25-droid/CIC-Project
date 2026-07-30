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
  // Tracks the pointer type (mouse/touch/pen) behind the MOST RECENT
  // pointerdown on this term - a ref, not state, since updating it must
  // never itself trigger a render; it only needs to be current by the time
  // handleClick reads it, and pointerdown always fires before click. This
  // is a per-interaction check, not a one-time device/viewport check - see
  // the Decision Log for why that was chosen (it's what lets a hybrid
  // touch+mouse device get the correct grammar per-tap, and it's the only
  // approach of the ones considered that's actually exercisable against a
  // desktop-Chromium dev server, which never reports (hover:none) even at
  // a phone viewport width). Defaults to 'mouse' so a keyboard ('Enter'
  // -triggered click with no preceding pointerdown) gets today's desktop
  // behavior rather than landing on a popover with no easy second gesture
  // to act on.
  const lastPointerTypeRef = useRef<string>('mouse');

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

  const handlePointerDown = (event: React.PointerEvent<HTMLSpanElement>) => {
    lastPointerTypeRef.current = event.pointerType;
  };

  // Read FRESH from the ref every time, never captured into a render-scoped
  // const - handleClick's closure is fixed at the render that last ran
  // BEFORE the tap (pointerdown mutating the ref doesn't itself trigger a
  // re-render), so a render-time snapshot of "is this touch" would still be
  // whatever it was at mount, not what the ref holds by the time the click
  // this pointerdown precedes actually fires. This was a real bug caught in
  // testing (dispatching a synthetic touch pointerdown+click still opened
  // Level-3 directly) - see the Decision Log.
  const isTouch = () => lastPointerTypeRef.current === 'touch';

  const handleClick = () => {
    if (isTouch()) {
      // Phone tap grammar (Build Handoff Increment 1 V1.0 §3): a tap shows
      // the Level-2 popover only - it does NOT open Level-3 directly. The
      // popover's own "Full entry ->" footer (below) is the only thing
      // that opens Level-3 on touch.
      setShowTooltip(true);
      return;
    }
    // Desktop/mouse - unchanged from before this fix: hover already showed
    // the Level-2 popover, so a click advances straight to Level-3.
    if (onDetailClick) {
      onDetailClick(term);
    }
  };

  // The popover's "Full entry ->" action - the only way Level-3 opens on
  // touch. stopPropagation keeps this from also bubbling into handleClick
  // above (which would be a no-op today since isTouch() is already true at
  // that point, but relying on that would be fragile).
  const handleFullEntryClick = (event: React.MouseEvent) => {
    event.stopPropagation();
    setShowTooltip(false);
    if (onDetailClick) {
      onDetailClick(term);
    }
  };

  // Touch-only: tapping outside the term AND its open popover dismisses it,
  // the same job mouseleave does on desktop (desktop doesn't need this
  // listener - mouseleave already covers it, and adding a pointerdown
  // listener there too would be redundant, not incorrect, but unnecessary
  // work on every desktop hover). Bound in the capture phase so it sees
  // the tap before any stopPropagation() elsewhere in the tree. Gated on
  // isTouch() at effect-run time (after showTooltip commits), not a
  // dependency-array snapshot - same staleness reasoning as handleClick.
  useEffect(() => {
    if (!showTooltip || !isTouch()) {
      return;
    }
    const handleOutsidePointerDown = (event: PointerEvent) => {
      if (spanRef.current && !spanRef.current.contains(event.target as Node)) {
        setShowTooltip(false);
      }
    };
    document.addEventListener('pointerdown', handleOutsidePointerDown, true);
    return () => {
      document.removeEventListener('pointerdown', handleOutsidePointerDown, true);
    };
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [showTooltip]);

  return (
    <span
      ref={spanRef}
      className="lexicon-term"
      onMouseEnter={() => setShowTooltip(true)}
      onMouseLeave={() => setShowTooltip(false)}
      onPointerDown={handlePointerDown}
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
          <button
            type="button"
            className="lexicon-tooltip__footer"
            onClick={handleFullEntryClick}
          >
            {isTouch() ? 'Full entry →' : 'Click for full entry'}
          </button>
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
