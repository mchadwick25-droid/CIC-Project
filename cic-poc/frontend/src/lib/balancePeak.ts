const KEY = 'cic_balance_peak';

/** The most tokens this browser has seen at once, so the gold line has a full length to measure against. */
export function peakBalance(current: number): number {
  let peak = current;
  try {
    const stored = Number(localStorage.getItem(KEY));
    if (Number.isFinite(stored) && stored > peak) peak = stored;
    if (peak !== stored) localStorage.setItem(KEY, String(peak));
  } catch {
    // Storage blocked: the line measures against the balance in view.
  }
  return peak;
}
