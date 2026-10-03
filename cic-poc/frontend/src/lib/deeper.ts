/**
 * The participant's code, held by this browser, and the balance the server
 * last reported for it. The app never learns what a code costs: it sends the
 * code with each request and shows the number the server returns. With
 * VITE_DEEPER_ENABLED not "on" nothing here is used: no control, no header.
 */
import { useSyncExternalStore } from 'react';

export const deeperEnabled = import.meta.env.VITE_DEEPER_ENABLED === 'on';

const STORAGE_KEY = 'cic_code';
const ALPHABET = '23456789ABCDEFGHJKLMNPQRSTUVWXYZ';
const CODE_LENGTH = 20;

/** The canonical form of what a person typed or pasted, or null if it cannot be a code. */
export function normalizeCode(raw: string): string | null {
  const code = raw.replace(/[\s-]+/g, '').toUpperCase();
  if (code.length !== CODE_LENGTH) return null;
  for (const ch of code) if (!ALPHABET.includes(ch)) return null;
  return code;
}

interface DeeperState {
  code: string | null;
  remaining: number | null;
}

function readStoredCode(): string | null {
  try {
    const raw = localStorage.getItem(STORAGE_KEY);
    return raw ? normalizeCode(raw) : null;
  } catch {
    return null;
  }
}

let state: DeeperState = { code: deeperEnabled ? readStoredCode() : null, remaining: null };
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
  update({ code, remaining: null });
  return true;
}

export function clearCode() {
  try {
    localStorage.removeItem(STORAGE_KEY);
  } catch {
    // Nothing to clean up if storage isn't available.
  }
  update({ code: null, remaining: null });
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

function subscribe(listener: () => void) {
  listeners.add(listener);
  return () => listeners.delete(listener);
}

export function useDeeper(): DeeperState {
  return useSyncExternalStore(subscribe, () => state);
}

/** For tests: put the module back as a fresh load would find it. */
export function resetDeeperForTests(code: string | null = null) {
  state = { code, remaining: null };
  listeners.forEach((listener) => listener());
}
