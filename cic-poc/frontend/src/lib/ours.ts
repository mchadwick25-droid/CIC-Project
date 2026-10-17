/**
 * Marks a browser as one the team tests with. A private link carries
 * ?ours=1 (or ?ours=0 to undo it); the app keeps the choice in its own
 * storage and drops the parameter from the address at once. Every session
 * this browser opens is then sent as internal, so the admin dashboard can
 * leave it out of the headline numbers. Nothing here reads a cookie or an
 * address.
 */
const STORAGE_KEY = 'cic_ours';
const PARAM = 'ours';

export function isOurs(): boolean {
  try {
    return localStorage.getItem(STORAGE_KEY) === '1';
  } catch {
    return false;
  }
}

function setOurs(on: boolean) {
  try {
    if (on) localStorage.setItem(STORAGE_KEY, '1');
    else localStorage.removeItem(STORAGE_KEY);
  } catch {
    // Storage blocked: the browser simply stays unmarked.
  }
}

/** Reads ?ours= from the address, sets or clears the mark, and removes only that parameter. */
export function takeOursFromAddress(): void {
  if (typeof window === 'undefined') return;
  const params = new URLSearchParams(window.location.search);
  if (!params.has(PARAM)) return;
  const value = params.get(PARAM);
  if (value === '1') setOurs(true);
  else if (value === '0') setOurs(false);
  params.delete(PARAM);
  const rest = params.toString();
  window.history.replaceState(window.history.state, '', window.location.pathname + (rest ? `?${rest}` : '') + window.location.hash);
}

/** The extra body field a session-create request carries from a marked browser. */
export function internalField(): { internal?: true } {
  return isOurs() ? { internal: true } : {};
}

takeOursFromAddress();
