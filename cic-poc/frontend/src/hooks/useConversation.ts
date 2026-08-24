/**
 * Conversation state against engine/api. One world per session (spec O9:
 * multi-world "Table" sessions are a separate, later product) - a
 * participant who wants a different Representative starts a new session.
 *
 * sessionStorage (not localStorage), matching the old hook's own reasoning:
 * survive a reload of the same tab, not follow the participant to a new tab
 * or persist past the tab's lifetime.
 */
import { useCallback, useState } from 'react';
import { ApiRequestError, createSession, getTranscript, sendMessage } from '../lib/api';
import type { FacilitatorTurn, TranscriptEntry, VoiceTurn } from '../types/conversation';

const STORAGE_KEY = 'cic_session';

interface StoredSession {
  sessionId: string;
  sessionCode: string;
  worldKey: string;
}

function readStored(): StoredSession | null {
  try {
    const raw = sessionStorage.getItem(STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    if (typeof parsed?.sessionId === 'string' && typeof parsed?.sessionCode === 'string' && typeof parsed?.worldKey === 'string') {
      return parsed;
    }
    return null;
  } catch {
    return null;
  }
}

function writeStored(session: StoredSession) {
  try {
    sessionStorage.setItem(STORAGE_KEY, JSON.stringify(session));
  } catch {
    // Private browsing / quota - reconnect-on-refresh just won't work.
  }
}

function clearStored() {
  try {
    sessionStorage.removeItem(STORAGE_KEY);
  } catch {
    // Nothing to clean up if storage isn't available.
  }
}

export interface ConversationTurn {
  speaker: 'participant' | 'facilitator' | string; // world_key for a voice turn
  text: string;
  kind?: FacilitatorTurn['kind'];
  citations?: VoiceTurn['citations'];
}

// `entry.speaker === 'participant'` alone can't discriminate this union -
// VoiceTurn.speaker is a plain `string` (it's the world_key), which
// overlaps the 'participant' literal structurally and defeats TS's usual
// discriminated-union narrowing. `kind`/`citations` are each unique to one
// branch, so checking for those instead narrows cleanly.
function toTurn(entry: TranscriptEntry): ConversationTurn {
  if ('kind' in entry) return { speaker: 'facilitator', text: entry.text, kind: entry.kind };
  if ('citations' in entry) return { speaker: entry.speaker, text: entry.text, citations: entry.citations };
  return { speaker: 'participant', text: entry.text };
}

interface ConversationState {
  sessionId: string | null;
  sessionCode: string | null;
  worldKey: string | null;
  turns: ConversationTurn[];
  closed: boolean;
  isLoading: boolean;
  error: string | null;
}

const initialState: ConversationState = {
  sessionId: null,
  sessionCode: null,
  worldKey: null,
  turns: [],
  closed: false,
  isLoading: false,
  error: null,
};

export function useConversation() {
  const [state, setState] = useState<ConversationState>(initialState);

  const begin = useCallback(async (worldKey: string) => {
    setState((prev) => ({ ...prev, isLoading: true, error: null }));
    try {
      const { session_id, session_code } = await createSession(worldKey);
      writeStored({ sessionId: session_id, sessionCode: session_code, worldKey });
      setState({ sessionId: session_id, sessionCode: session_code, worldKey, turns: [], closed: false, isLoading: false, error: null });
      return session_id;
    } catch (error) {
      const message = error instanceof ApiRequestError ? error.message : 'Could not start a conversation.';
      setState((prev) => ({ ...prev, isLoading: false, error: message }));
      return null;
    }
  }, []);

  const send = useCallback(
    async (text: string) => {
      const { sessionId, sessionCode } = state;
      if (!sessionId || !sessionCode) {
        setState((prev) => ({ ...prev, error: 'No active session' }));
        return false;
      }
      setState((prev) => ({ ...prev, isLoading: true, error: null, turns: [...prev.turns, { speaker: 'participant', text }] }));
      try {
        const result = await sendMessage(sessionId, sessionCode, text, crypto.randomUUID());
        setState((prev) => {
          const appended: ConversationTurn[] = [];
          if (result.facilitator) appended.push({ speaker: 'facilitator', text: result.facilitator.text, kind: result.facilitator.kind });
          if (result.voice) appended.push({ speaker: result.voice.speaker, text: result.voice.text, citations: result.voice.citations });
          const closed = result.facilitator?.kind === 'close' || prev.closed;
          if (closed) clearStored();
          return { ...prev, isLoading: false, turns: [...prev.turns, ...appended], closed };
        });
        return true;
      } catch (error) {
        const message = error instanceof ApiRequestError ? error.message : 'That message did not go through.';
        setState((prev) => ({ ...prev, isLoading: false, error: message }));
        return false;
      }
    },
    [state]
  );

  const rehydrate = useCallback(async (): Promise<string | null> => {
    const stored = readStored();
    if (!stored) return null;
    try {
      const transcript = await getTranscript(stored.sessionId, stored.sessionCode);
      if (transcript.closed) {
        clearStored();
        return null;
      }
      setState({
        sessionId: stored.sessionId,
        sessionCode: stored.sessionCode,
        worldKey: stored.worldKey,
        turns: transcript.transcript.map(toTurn),
        closed: transcript.closed,
        isLoading: false,
        error: null,
      });
      return stored.worldKey;
    } catch {
      clearStored();
      return null;
    }
  }, []);

  const reset = useCallback(() => {
    clearStored();
    setState(initialState);
  }, []);

  return {
    sessionId: state.sessionId,
    sessionCode: state.sessionCode,
    worldKey: state.worldKey,
    turns: state.turns,
    closed: state.closed,
    isLoading: state.isLoading,
    error: state.error,
    begin,
    send,
    rehydrate,
    reset,
  };
}

export function hasStoredSession(): boolean {
  return readStored() !== null;
}
