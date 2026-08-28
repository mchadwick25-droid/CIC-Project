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
import { clearStored, readStored, writeStored } from '../lib/sessionStore';
import type { FacilitatorTurn, TranscriptEntry, VoiceTurn } from '../types/conversation';

export interface ConversationTurn {
  speaker: 'participant' | 'facilitator' | string; // world_key for a voice turn
  text: string;
  kind?: FacilitatorTurn['kind'];
  citations?: VoiceTurn['citations'];
  figuresUsed?: VoiceTurn['figures_used'];
  glosses?: VoiceTurn['glosses'];
}

// `entry.speaker === 'participant'` alone can't discriminate this union -
// VoiceTurn.speaker is a plain `string` (it's the world_key), which
// overlaps the 'participant' literal structurally and defeats TS's usual
// discriminated-union narrowing. `kind`/`citations` are each unique to one
// branch, so checking for those instead narrows cleanly.
function toTurn(entry: TranscriptEntry): ConversationTurn {
  if ('kind' in entry) return { speaker: 'facilitator', text: entry.text, kind: entry.kind };
  if ('citations' in entry) {
    return { speaker: entry.speaker, text: entry.text, citations: entry.citations, figuresUsed: entry.figures_used, glosses: entry.glosses };
  }
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
  // True when the honest remedy is starting fresh (restarted server,
  // closed session) - the screens render a begin-again button for these.
  errorRecoverable: boolean;
}

const initialState: ConversationState = {
  sessionId: null,
  sessionCode: null,
  worldKey: null,
  turns: [],
  closed: false,
  isLoading: false,
  error: null,
  errorRecoverable: false,
};

export function useConversation() {
  const [state, setState] = useState<ConversationState>(initialState);

  const begin = useCallback(async (worldKey: string) => {
    setState((prev) => ({ ...prev, isLoading: true, error: null, errorRecoverable: false }));
    try {
      const { session_id, session_code } = await createSession(worldKey);
      writeStored({ sessionId: session_id, sessionCode: session_code, mode: 'interview', worldKey });
      // create_session already appends the Facilitator's door turn (its
      // first-ever line - engine/api/wiring.py) before this ever returns,
      // so one transcript fetch picks it up rather than starting the
      // screen with an empty transcript and no introduction.
      const transcript = await getTranscript(session_id, session_code);
      setState({
        sessionId: session_id,
        sessionCode: session_code,
        worldKey,
        turns: transcript.transcript.map(toTurn),
        closed: transcript.closed,
        isLoading: false,
        error: null,
        errorRecoverable: false,
      });
      return session_id;
    } catch (error) {
      const message = error instanceof ApiRequestError ? error.message : 'We couldn\'t reach the room just now. Check your connection, then try again.';
      const recoverable = error instanceof ApiRequestError && error.recoverable;
      setState((prev) => ({ ...prev, isLoading: false, error: message, errorRecoverable: recoverable }));
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
      setState((prev) => ({ ...prev, isLoading: true, error: null, errorRecoverable: false, turns: [...prev.turns, { speaker: 'participant', text }] }));
      try {
        const result = await sendMessage(sessionId, sessionCode, text, crypto.randomUUID());
        setState((prev) => {
          const appended: ConversationTurn[] = [];
          if (result.facilitator) appended.push({ speaker: 'facilitator', text: result.facilitator.text, kind: result.facilitator.kind });
          if (result.voice) {
            appended.push({
              speaker: result.voice.speaker,
              text: result.voice.text,
              citations: result.voice.citations,
              figuresUsed: result.voice.figures_used,
              glosses: result.voice.glosses,
            });
          }
          const closed = result.facilitator?.kind === 'close' || prev.closed;
          if (closed) clearStored();
          return { ...prev, isLoading: false, turns: [...prev.turns, ...appended], closed };
        });
        return true;
      } catch (error) {
        const message = error instanceof ApiRequestError ? error.message : 'That message didn\'t go through - check your connection and try again.';
        const recoverable = error instanceof ApiRequestError && error.recoverable;
        setState((prev) => ({ ...prev, isLoading: false, error: message, errorRecoverable: recoverable }));
        return false;
      }
    },
    [state]
  );

  const rehydrate = useCallback(async (): Promise<string | null> => {
    const stored = readStored();
    if (!stored || stored.mode !== 'interview' || !stored.worldKey) return null;
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
        errorRecoverable: false,
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
    errorRecoverable: state.errorRecoverable,
    begin,
    send,
    rehydrate,
    reset,
  };
}

export function hasStoredSession(): boolean {
  return readStored() !== null;
}
