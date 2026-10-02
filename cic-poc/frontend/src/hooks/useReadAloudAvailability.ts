/**
 * Design note constraint: "if a browser has no voices, the control
 * hides." `speechSynthesis.getVoices()` is notoriously async on first
 * load in several browsers - it can return an empty array on the very
 * first call even though voices arrive moments later - so a single
 * synchronous check at mount would wrongly hide the control on a browser
 * that simply hasn't finished loading its voice list yet. This re-checks
 * once via the 'voiceschanged' event, the browser's own signal that the
 * list just changed, rather than polling.
 */
import { useEffect, useState } from 'react';
import { isReadAloudSupported } from '../lib/readAloud';

function hasVoices(): boolean {
  return isReadAloudSupported() && window.speechSynthesis.getVoices().length > 0;
}

export function useReadAloudAvailability(): boolean {
  const [available, setAvailable] = useState(hasVoices);

  useEffect(() => {
    if (!isReadAloudSupported()) return;
    if (hasVoices()) {
      setAvailable(true);
      return;
    }
    const onVoicesChanged = () => setAvailable(hasVoices());
    window.speechSynthesis.addEventListener('voiceschanged', onVoicesChanged);
    return () => window.speechSynthesis.removeEventListener('voiceschanged', onVoicesChanged);
  }, []);

  return available;
}
