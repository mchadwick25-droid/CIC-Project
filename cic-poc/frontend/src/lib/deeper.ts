/**
 * The participant's code, held by this browser, and the balance the server
 * last reported for it. The app never learns what a code costs: it sends the
 * code with each request and shows the number the server returns. With
 * VITE_DEEPER_ENABLED not "on" nothing here is used: no control, no header,
 * no listener.
 */
import { useSyncExternalStore } from 'react';

export const deeperEnabled = import.meta.env.VITE_DEEPER_ENABLED === 'on';

const STORAGE_KEY = 'cic_code';
const SITE_ORIGIN = import.meta.env.VITE_DEEPER_SITE_ORIGIN || 'https://churchinconversation.com';
const MESSAGE_TYPE = 'cic-deeper-code';
const ALPHABET = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ';
const CODE_LENGTH = 20;
const REFERENCE = /^[A-Za-z0-9_-]{16,64}$/;

/** The canonical form of what a person typed or pasted, or null if it cannot be a code. */
export function normalizeCode(raw: string): string | null {
  const code = raw.replace(/[\s-]+/g, '').toUpperCase();
  if (code.length !== CODE_LENGTH) return null;
  for (const ch of code) if (!ALPHABET.includes(ch)) return null;
  return code;
}

/** A purchase a link says is waiting, held until the person says yes. */
export interface PendingClaim {
  reference: string;
  status: 'asking' | 'working' | 'failed';
}

interface DeeperState {
  code: string | null;
  remaining: number | null;
  claim: PendingClaim | null;
}

function readStoredCode(): string | null {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? normalizeCode(raw) : null;
  } catch {
    return null;
  }
}

let state: DeeperState = { code: deeperEnabled ? readStoredCode() : null, remaining: null, claim: null };
const listeners = new Set<() => void>();

function update(next: DeeperState) {
  state = next;
  listeners.forEach((listener) => listener());
}

/** Saves a code this browser will send from now on. Returns false when the text is not a code. */
export function saveCode(raw: string): boolean {
  const code = normalizeCode(raw);
  if (!code) return false;
  try {
    localStorage.setItem(STORAGE_KEY, code);
  } catch {
    // Storage blocked: the code still works until the tab closes.
  }
  update({ code, remaining: null, claim: null });
  return true;
}

export function clearCode() {
  try {
    localStorage.removeItem(STORAGE_KEY);
  } catch {
    // Nothing to clean up if storage isn't available.
  }
  update({ ...state, code: null, remaining: null });
}

/** The balance a response reported, or null when it reported none. */
export function setRemaining(remaining: number | null) {
  if (!deeperEnabled || state.remaining === remaining) return;
  update({ ...state, remaining });
}

/** The header every request carries while a code is held. */
export function codeHeaders(): Record<string, string> {
  return deeperEnabled && state.code ? { 'X-Cic-Code': state.code } : {};
}

export function remainingFromHeader(value: string | null): number | null {
  if (value === null || !/^\d+$/.test(value)) return null;
  return Number(value);
}

export function getCodeUrl(): string {
  return `${SITE_ORIGIN}/go-deeper.html`;
}

/** Opens the site's page for getting a code in a popup, so the conversation stays where it is. */
export function openGetCode(): boolean {
  if (!deeperEnabled) return false;
  return window.open(getCodeUrl(), 'cic-get-code', 'popup=yes,width=520,height=760') !== null;
}

/**
 * What the popup sends back when payment is done. Only the site's own origin
 * is believed, and only a single well-formed code is kept; a pack of several
 * codes stays in the popup for the buyer to share out.
 */
export function acceptCodeMessage(event: { origin: string; data: unknown; source?: unknown }): boolean {
  if (!deeperEnabled || event.origin !== SITE_ORIGIN) return false;
  const data = event.data as { type?: unknown; codes?: unknown } | null;
  if (!data || data.type !== MESSAGE_TYPE || !Array.isArray(data.codes) || data.codes.length !== 1) return false;
  if (typeof data.codes[0] !== 'string' || !saveCode(data.codes[0])) return false;
  // Tell the popup the code is saved, so it can close; to the site's origin only.
  try {
    (event.source as { postMessage: (message: unknown, origin: string) => void } | null)?.postMessage({ type: 'cic-deeper-saved' }, SITE_ORIGIN);
  } catch {
    // The popup is gone; it will fall back to sending its own window here.
  }
  return true;
}

/**
 * A purchase reference the return page put in the address fragment. The
 * address is cleared at once, so it does not stay in the history or a copied
 * link, and nothing is saved until the person agrees: a link made by someone
 * else must not be able to swap or plant a code. A fragment is never sent to
 * a server.
 */
export function takeClaimFromAddress(): boolean {
  if (!deeperEnabled || typeof window === 'undefined') return false;
  const match = /^#cic-claim=([^&]*)$/.exec(window.location.hash);
  if (!match) return false;
  window.history.replaceState(null, '', window.location.pathname + window.location.search);
  let reference = '';
  try {
    reference = decodeURIComponent(match[1]);
  } catch {
    reference = '';
  }
  if (!REFERENCE.test(reference)) return false;
  update({ ...state, claim: { reference, status: 'asking' } });
  return true;
}

export function declineClaim() {
  if (state.claim) update({ ...state, claim: null });
}

/** The person said yes: the app asks its own server for the code and keeps it if there is exactly one. */
export async function acceptClaim(): Promise<boolean> {
  const claim = state.claim;
  if (!deeperEnabled || !claim) return false;
  update({ ...state, claim: { ...claim, status: 'working' } });
  try {
    const response = await fetch('/api/deeper/claim', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ reference: claim.reference }),
    });
    const body = response.ok ? ((await response.json()) as { codes?: unknown }) : null;
    if (body && Array.isArray(body.codes) && body.codes.length === 1 && typeof body.codes[0] === 'string' && saveCode(body.codes[0])) {
      return true;
    }
  } catch {
    // Fall through to the failed state.
  }
  update({ ...state, claim: { ...claim, status: 'failed' } });
  return false;
}

function subscribe(listener: () => void) {
  listeners.add(listener);
  return () => listeners.delete(listener);
}

export function useDeeper(): DeeperState {
  return useSyncExternalStore(subscribe, () => state);
}

/**
 * Another tab saved or removed the code: this one follows, so a code that
 * reached the app in a different tab is used by the conversation already open
 * here. A message from the popup is answered whichever screen is showing.
 */
if (deeperEnabled && typeof window !== 'undefined') {
  window.addEventListener('storage', (event) => {
    if (event.key !== STORAGE_KEY) return;
    const code = event.newValue ? normalizeCode(event.newValue) : null;
    if (code !== state.code) update({ ...state, code, remaining: null });
  });
  window.addEventListener('message', (event) => {
    acceptCodeMessage(event);
  });
  takeClaimFromAddress();
}
