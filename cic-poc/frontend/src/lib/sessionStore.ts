/**
 * One stored session per tab, interview or table - the single source both
 * hooks (useConversation, useTable) read, so App can route a reload to the
 * right room by peeking `mode` before either hook rehydrates.
 *
 * sessionStorage (not localStorage), same reasoning the old hook carried:
 * survive a reload of the same tab, not follow the participant to a new
 * tab or persist past the tab's lifetime.
 */

const STORAGE_KEY = 'cic_session';

export interface StoredSession {
  sessionId: string;
  sessionCode: string;
  mode: 'interview' | 'table';
  worldKey?: string; // interview
  worldKeys?: string[]; // table
}

export function readStored(): StoredSession | null {
  try {
    const raw = sessionStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    if (typeof parsed?.sessionId !== 'string' || typeof parsed?.sessionCode !== 'string') return null;
    // Sessions stored before table mode existed carry worldKey and no mode.
    if (parsed.mode === 'table' && Array.isArray(parsed.worldKeys)) return { ...parsed, mode: 'table' };
    if (typeof parsed.worldKey === 'string') return { ...parsed, mode: 'interview' };
    return null;
  } catch {
    return null;
  }
}

export function writeStored(session: StoredSession) {
  try {
    sessionStorage.setItem(STORAGE_KEY, JSON.stringify(session));
  } catch {
    // Private browsing / quota - reconnect-on-refresh just won't work.
  }
}

export function clearStored() {
  try {
    sessionStorage.removeItem(STORAGE_KEY);
  } catch {
    // Nothing to clean up if storage isn't available.
  }
}
