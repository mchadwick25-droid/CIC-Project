/**
 * The one breakpoint the transparency apparatus's interaction grammar
 * actually branches on (CiC_Full_UX_Design_V1_0.md §2.4): "hover = short ·
 * click = full" above 640px, "tap = short · tap-through = full" below it.
 * The design also names a ≥900px desktop layout breakpoint (for the wide
 * column, not built yet - see Conversation.tsx's own narrow 640px shell),
 * but the INTERACTION grammar itself only has two states, split at the
 * one boundary phone is explicitly named against: "<640px phone... between
 * them the single-column layout narrows gracefully" - so 640-899px still
 * gets hover/click, the same as true desktop.
 */
import { useEffect, useState } from 'react';

const PHONE_QUERY = '(max-width: 639px)';

export function useIsPhone(): boolean {
  const [isPhone, setIsPhone] = useState(() =>
    typeof window === 'undefined' ? false : window.matchMedia(PHONE_QUERY).matches
  );

  useEffect(() => {
    const mql = window.matchMedia(PHONE_QUERY);
    const onChange = () => setIsPhone(mql.matches);
    mql.addEventListener('change', onChange);
    return () => mql.removeEventListener('change', onChange);
  }, []);

  return isPhone;
}
