/**
 * The participant's code, held by this browser, and the balance the server
 * last reported for it. The app never learns what a code costs: it sends the
 * code with each request and shows the number the server returns. With
 * VITE_DEEPER_ENABLED not "on" nothing here is used: no control, no header,
 * no listener.
 */
import { useSyncExternalStore } from 'react';

export const deeperEnabled = import.meta.env.VITE_DEEPER_ENABLED === 'on';

const STORAGE_KEY = 'cic_codes';
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

/** A code in the groups it is read and written in. */
export function formatCode(code: string): string {
  return code.match(/.{1,4}/g)?.join(' ') ?? code;
}

/** A purchase a link says is waiting, held until the person says yes. */
export interface PendingClaim {
  reference: string;
  status: 'asking' | 'working' | 'failed';
}

interface DeeperState {
  codes: string[];
  balances: Record<string, number | null>;
  // What the codes held add up to, or null before anything has reported.
  remaining: number | null;
  // The code in use is nearly spent and nothing else is held to carry on with.
  low: boolean;
  // What a visitor holding no code may still draw free, as the server last said, or null.
  freeLeft: number | null;
  claim: PendingClaim | null;
  // The panel beside the conversation: opened by a limit or by the person, never on its own.
  panelOpen: boolean;
}

function readStoredCodes(): string[] {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? parseCodes(raw) : [];
  } catch {
    return [];
  }
}

function parseCodes(raw: string): string[] {
  try {
    const parsed: unknown = JSON.parse(raw);
    if (!Array.isArray(parsed)) return [];
    const seen: string[] = [];
    for (const item of parsed) {
      const code = typeof item === 'string' ? normalizeCode(item) : null;
      if (code && !seen.includes(code)) seen.push(code);
    }
    return seen;
  } catch {
    return [];
  }
}

/**
 * Changes the stored list from what is stored right now, not from this tab's
 * memory, so two tabs changing it at once cannot overwrite each other. Returns
 * the list as written.
 */
function changeStoredCodes(change: (stored: string[]) => string[]): string[] {
  let current = state.codes;
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    current = raw ? parseCodes(raw) : [];
  } catch {
    // Storage blocked: work from this tab's own list.
  }
  const next = change(current);
  try {
    if (next.length === 0) localStorage.removeItem(STORAGE_KEY);
    else localStorage.setItem(STORAGE_KEY, JSON.stringify(next));
  } catch {
    // Storage blocked: the codes still work until the tab closes.
  }
  return next;
}

const emptyState = (codes: string[]): DeeperState => ({ codes, balances: {}, remaining: null, low: false, freeLeft: null, claim: null, panelOpen: false });

let state: DeeperState = emptyState(deeperEnabled ? readStoredCodes() : []);
const listeners = new Set<() => void>();

function update(next: DeeperState) {
  state = next;
  listeners.forEach((listener) => listener());
}

function total(codes: string[], balances: Record<string, number | null>): number | null {
  const known = codes.map((code) => balances[code]).filter((n): n is number => typeof n === 'number');
  return known.length === 0 ? null : known.reduce((sum, n) => sum + n, 0);
}

/** The code the next request carries: the first one not known to be spent, else the last held. */
function activeCode(): string | null {
  const usable = state.codes.find((code) => state.balances[code] !== 0);
  return usable ?? state.codes[state.codes.length - 1] ?? null;
}

/** The code a request sent now would carry, to be given back with its reply. */
export function currentCode(): string | null {
  return deeperEnabled ? activeCode() : null;
}

/** What the server says one code has left, by asking on the code's own account. */
async function refreshBalance(code: string) {
  try {
    const response = await fetch('/api/deeper/balance', { credentials: 'omit', headers: { 'X-Cic-Code': code } });
    if (response.status === 404) {
      forget(code);
      return;
    }
    if (!response.ok) return;
    const body = (await response.json()) as { remaining?: unknown };
    if (typeof body.remaining === 'number') setBalanceOf(code, body.remaining);
  } catch {
    // The balance shows when the next reply reports it.
  }
}

function setBalanceOf(code: string, remaining: number) {
  if (!state.codes.includes(code)) return;
  let codes = state.codes;
  const balances = { ...state.balances, [code]: remaining };
  // A spent code is dropped once another is held to carry on with.
  if (remaining === 0 && codes.length > 1) {
    codes = changeStoredCodes((stored) => stored.filter((c) => c !== code));
    delete balances[code];
  }
  update({ ...state, codes, balances, remaining: total(codes, balances) });
}

function forget(code: string) {
  const codes = changeStoredCodes((stored) => stored.filter((c) => c !== code));
  const balances = { ...state.balances };
  delete balances[code];
  update({ ...state, codes, balances, remaining: total(codes, balances), low: false, freeLeft: null });
}

/** Adds a code to the ones this browser holds. Returns false when the text is not a code. */
export function saveCode(raw: string): boolean {
  const code = normalizeCode(raw);
  if (!code) return false;
  if (state.codes.includes(code)) {
    update({ ...state, claim: null });
    return true;
  }
  const codes = changeStoredCodes((stored) => (stored.includes(code) ? stored : [...stored, code]));
  update({ ...state, codes, claim: null, freeLeft: null });
  void refreshBalance(code);
  return true;
}

/**
 * A code the person typed: checked with the server first, so a wrong one is
 * refused on the spot. If the server cannot be reached the code is kept and
 * checked by the next reply.
 */
export async function addCode(raw: string): Promise<boolean> {
  const code = normalizeCode(raw);
  if (!code) return false;
  try {
    const response = await fetch('/api/deeper/balance', { credentials: 'omit', headers: { 'X-Cic-Code': code } });
    if (response.status === 404) return false;
  } catch {
    // Unreachable: keep it and let the next reply say.
  }
  return saveCode(code);
}

/** Removes every held code. */
export function clearCode() {
  changeStoredCodes(() => []);
  update({ ...emptyState([]), panelOpen: state.panelOpen });
}

/** Removes the code in use, and only that one. */
export function removeCode() {
  const code = activeCode();
  if (code !== null) forget(code);
}

/**
 * What a reply reported, credited to the code the request carried. The list may
 * have changed while the request was in flight, so the code is never worked out
 * again here; a reply for a code no longer held is ignored.
 */
export function reportBalance(sentWith: string | null, remaining: number | null, low: boolean) {
  if (!deeperEnabled || sentWith === null || remaining === null || !state.codes.includes(sentWith)) return;
  // Another code might carry on unless it is known to be spent: an unknown balance counts as might.
  const otherMayCarry = state.codes.some((c) => c !== sentWith && state.balances[c] !== 0);
  setBalanceOf(sentWith, remaining);
  const nextLow = low && !otherMayCarry;
  if (state.low !== nextLow) update({ ...state, low: nextLow });
}

/** The free tokens a visitor with no code has left, as the reply reported them. Not stored. */
export function reportFreeLeft(freeLeft: number | null) {
  if (!deeperEnabled || freeLeft === null || state.freeLeft === freeLeft) return;
  update({ ...state, freeLeft });
}

export function freeLeftFromHeader(value: string | null): number | null {
  return remainingFromHeader(value);
}

/** The header every request carries while a code is held. */
export function codeHeaders(): Record<string, string> {
  const code = deeperEnabled ? activeCode() : null;
  return code ? { 'X-Cic-Code': code } : {};
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
  update({ ...state, claim: { reference, status: 'asking' }, panelOpen: true });
  return true;
}

export function openPanel() {
  if (deeperEnabled && !state.panelOpen) update({ ...state, panelOpen: true });
}

export function closePanel() {
  if (state.panelOpen) update({ ...state, panelOpen: false });
}

/** A turn came back refused for want of tokens or a code: the panel opens beside it. */
export function noteLimit() {
  openPanel();
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
    // No cookies: the reference is held beside the buyer's name at Stripe, and the
    // visitor cookie sits beside conversations. They must never travel together.
    const response = await fetch('/api/deeper/claim', {
      method: 'POST',
      credentials: 'omit',
      referrerPolicy: 'no-referrer',
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

/** The current state without a component, for tests. */
export function deeperSnapshot(): DeeperState {
  return state;
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
    const codes = event.newValue ? parseCodes(event.newValue) : [];
    if (codes.join() === state.codes.join()) return;
    const balances = Object.fromEntries(Object.entries(state.balances).filter(([code]) => codes.includes(code)));
    update({ ...state, codes, balances, remaining: total(codes, balances) });
  });
  window.addEventListener('message', (event) => {
    acceptCodeMessage(event);
  });
  takeClaimFromAddress();
}
