/**
 * The pilot's free pack. A link from the site carries the audience in the
 * address fragment (#cic-pilot=pastors); the app clears the fragment at once,
 * asks its own server for a code once, saves it like any other code, and keeps
 * a marker so a browser that has joined is never offered the pack again. The
 * marker and the code sit apart from conversations, and the request carries no
 * cookie. With VITE_DEEPER_ENABLED not "on" nothing here runs.
 */
import { useSyncExternalStore } from 'react';
import { deeperEnabled, openPanel, saveCode } from './deeper';

const MARKER_KEY = 'cic_pilot';
const AUDIENCE = /^[a-z][a-z0-9-]{0,23}$/;
const SITE_ORIGIN = import.meta.env.VITE_DEEPER_SITE_ORIGIN || 'https://churchinconversation.com';

export type PilotStatus = 'joining' | 'ready' | 'already' | 'full' | 'ended' | 'address_limit' | 'failed';

export interface PilotState {
  status: PilotStatus | null;
  tokens: number | null;
  conversations: number | null;
}

const idle: PilotState = { status: null, tokens: null, conversations: null };
let state: PilotState = idle;
const listeners = new Set<() => void>();

function update(next: PilotState) {
  state = next;
  listeners.forEach((listener) => listener());
}

function holdsMarker(): boolean {
  try {
    return localStorage.getItem(MARKER_KEY) === '1';
  } catch {
    return false;
  }
}

function setMarker() {
  try {
    localStorage.setItem(MARKER_KEY, '1');
  } catch {
    // Storage blocked: the pack still works until the tab closes.
  }
}

export function feedbackFormUrl(): string {
  return `${SITE_ORIGIN}/pilot-feedback.html`;
}

/** The audience a link named in the address fragment, or null. The fragment is cleared whatever it holds. */
export function takePilotFromAddress(): string | null {
  if (!deeperEnabled || typeof window === 'undefined') return null;
  const match = /^#cic-pilot=([^&]*)$/.exec(window.location.hash);
  if (!match) return null;
  window.history.replaceState(null, '', window.location.pathname + window.location.search);
  return AUDIENCE.test(match[1]) ? match[1] : null;
}

/** Asks for the pack once. A browser that already joined is told so and asks nothing. */
export async function joinPilot(audience: string): Promise<void> {
  if (!deeperEnabled || !AUDIENCE.test(audience) || state.status === 'joining') return;
  if (holdsMarker()) {
    update({ ...idle, status: 'already' });
    openPanel();
    return;
  }
  update({ ...idle, status: 'joining' });
  openPanel();
  try {
    // No cookies: the visitor cookie sits beside conversations and must not travel with this.
    const response = await fetch('/api/deeper/pilot-join', {
      method: 'POST',
      credentials: 'omit',
      referrerPolicy: 'no-referrer',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ audience }),
    });
    if (response.status === 404) {
      // Closed or not named: nothing is shown, as if there were no pilot.
      update(idle);
      return;
    }
    const body = (await response.json()) as { joined?: unknown; code?: unknown; tokens?: unknown; conversations?: unknown; reason?: unknown };
    if (response.ok && body.joined === true && typeof body.code === 'string' && saveCode(body.code)) {
      setMarker();
      update({
        status: 'ready',
        tokens: typeof body.tokens === 'number' ? body.tokens : null,
        conversations: typeof body.conversations === 'number' ? body.conversations : null,
      });
      return;
    }
    if (response.status === 409 && (body.reason === 'full' || body.reason === 'ended' || body.reason === 'address_limit')) {
      update({ ...idle, status: body.reason });
      return;
    }
  } catch {
    // Fall through to the failed state.
  }
  update({ ...idle, status: 'failed' });
}

export function dismissPilot() {
  update(idle);
}

function subscribe(listener: () => void) {
  listeners.add(listener);
  return () => listeners.delete(listener);
}

export function pilotSnapshot(): PilotState {
  return state;
}

export function usePilot(): PilotState {
  return useSyncExternalStore(subscribe, () => state);
}

if (deeperEnabled && typeof window !== 'undefined') {
  const audience = takePilotFromAddress();
  if (audience) void joinPilot(audience);
}
