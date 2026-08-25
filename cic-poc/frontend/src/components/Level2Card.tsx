/**
 * Level-2: the short card (CiC_Full_UX_Design_V1_0.md §2.4) - desktop
 * hover, phone tap. `position: fixed` against a measured anchor rect,
 * not `position: absolute` inside the trigger's own DOM position: the
 * transcript column scrolls (`.conversation__transcript`'s overflow-y:
 * auto also computes overflow-x: auto per the CSS spec), which clips an
 * absolutely-positioned descendant that extends past its box - a real
 * bug caught by actually opening this in a browser, not a hypothetical.
 * `fixed` positioning escapes that clip (its containing block is the
 * viewport, not the scrolling ancestor). `anchor` is the trigger's own
 * getBoundingClientRect(), measured by InlineBridge, so this only has to
 * place itself relative to that rect and clamp inside the viewport.
 *
 * Phone carries the one extra affordance the design names: a "Full
 * entry →" action to reach Level 3, since there is no hover state to
 * fall back on for "give me more."
 */
interface Level2CardProps {
  children: React.ReactNode;
  showFullEntry: boolean;
  onFullEntry: () => void;
  anchor: DOMRect;
}

const CARD_WIDTH = 320;
const VIEWPORT_MARGIN = 12;

export function Level2Card({ children, showFullEntry, onFullEntry, anchor }: Level2CardProps) {
  const idealLeft = anchor.left + anchor.width / 2 - CARD_WIDTH / 2;
  const maxLeft = window.innerWidth - CARD_WIDTH - VIEWPORT_MARGIN;
  const left = Math.min(Math.max(idealLeft, VIEWPORT_MARGIN), Math.max(maxLeft, VIEWPORT_MARGIN));
  const top = anchor.bottom + 6;

  return (
    <div
      className="level2-card"
      role="tooltip"
      style={{ position: 'fixed', top, left, width: `min(${CARD_WIDTH}px, calc(100vw - ${VIEWPORT_MARGIN * 2}px))` }}
    >
      <div className="level2-card__body">{children}</div>
      {showFullEntry && (
        <button type="button" className="level2-card__full-entry" onClick={onFullEntry}>
          Full entry →
        </button>
      )}
    </div>
  );
}
