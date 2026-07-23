/**
 * The static "Arriving" mark alone (ring + seat, no wordmark, no build
 * animation) - for slim chrome contexts like the table bar, where the full
 * ArrivingLockup hero (world-selection screen only) would be wrong: no
 * wordmark/sentence room, and no sessionStorage-gated play-once motion to
 * re-trigger mid-conversation. Renders in the same resting appearance the
 * hero settles into once its own animation finishes, using the same
 * .arriving-ring/.arriving-seat CSS so both places stay visually identical.
 */
export function BrandMark({ size = 22 }: { size?: number }) {
  return (
    <svg
      width={size}
      height={size}
      viewBox="0 0 100 100"
      role="img"
      aria-label="Church in Conversation"
    >
      <circle className="arriving-ring" cx="50" cy="50" r="31" pathLength="360" />
      <circle className="arriving-seat" cx="88.5" cy="50" r="6.5" />
    </svg>
  );
}
