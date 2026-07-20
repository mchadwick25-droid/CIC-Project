/**
 * ArrivingLockup - the "Arriving" mark + "Church in Conversation" wordmark,
 * placed at the top of the world-selection screen (§5 recommended default -
 * the S0 threshold that will formally host the brand lockup is Phase 1, not
 * this increment). The wordmark carries the header; the mark plays its
 * build-then-settle motion once per browser session (sessionStorage, not
 * localStorage - a fresh arrival each session, never replayed within one),
 * never again this session, never on the conversation screen.
 *
 * The animation itself (timing, easing, keyframes) is lifted verbatim from
 * Brand-Assets/CiC_Logo_Arriving_Motion_Reference.html, not re-derived -
 * only the color source (the app's own --color-text/--color-primary tokens
 * instead of the reference's standalone --ink/--madder) and the resting-vs-
 * animating CSS structure changed to fit inline UI placement instead of a
 * full-page standalone demo.
 */

import { useEffect, useState } from 'react';

const MOTION_PLAYED_KEY = 'cic_arriving_motion_played';

export function ArrivingLockup() {
  // The lazy initializer must stay a pure read - it runs twice under
  // StrictMode's deliberate double-invocation, so writing sessionStorage
  // here (as an earlier version of this component did) lets the second
  // invocation see the first invocation's own write and wrongly compute
  // shouldPlay=false on every mount, including the real first one. The
  // write itself belongs in the effect below.
  const [shouldPlay] = useState(() => sessionStorage.getItem(MOTION_PLAYED_KEY) !== 'true');

  useEffect(() => {
    if (shouldPlay) {
      sessionStorage.setItem(MOTION_PLAYED_KEY, 'true');
    }
  }, [shouldPlay]);

  return (
    <div className="arriving-lockup">
      <span className={`arriving${shouldPlay ? ' play' : ''}`}>
        <svg
          width="44"
          height="44"
          viewBox="0 0 100 100"
          role="img"
          aria-label="A single red dot waits alone; a table is drawn around toward it, the doorway completing last; the dot sits down and breathes"
        >
          <circle className="arriving-ring" cx="50" cy="50" r="31" pathLength="360" />
          <circle className="arriving-seat" cx="88.5" cy="50" r="6.5" />
        </svg>
      </span>
      <h1 className="arriving-lockup__wordmark">
        Church <em>in</em> Conversation
      </h1>
      <p className="arriving-lockup__sentence">
        The mark is a table; the opening is the way in — and it never closes.
      </p>
    </div>
  );
}
