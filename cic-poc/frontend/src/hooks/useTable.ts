/**
 * Table-session state against engine/api (Artifact-7 SS6's turn-at-a-time
 * transport). One participant message opens a round; this hook then keeps
 * calling /continue while the round is open, appending each voice turn as
 * it lands - the participant watches the table speak voice by voice rather
 * than waiting for the whole round.
 *
 * Same storage discipline as useConversation, through lib/sessionStore.
 */
import { useCallback, useRef, useState } from 'react';
import { ApiRequestError, continueRound, createTableSession, getTranscript, sendTableMessage } from '../lib/api';
import { clearStored, readStored, writeStored } from '../lib/sessionStore';
import type { FacilitatorTurn, TableMessageResponse, VoiceTurn } from '../types/conversation';
import { toTurn, type ConversationTurn } from './useConversation';

function turnsFromAdvance(advance: TableMessageResponse): ConversationTurn[] {
  const appended: ConversationTurn[] = [];
  for (const f of advance.facilitator as FacilitatorTurn[]) {
    appended.push({ speaker: 'facilitator', text: f.text, kind: f.kind, modernTerms: f.modern_terms, note: f.kind === 'limit' ? advance.limit_note?.text : undefined });
  }
  const v = advance.voice as VoiceTurn | null;
  if (v) {
    appended.push({ speaker: v.speaker, text: v.text, citations: v.citations, figuresUsed: v.figures_used, glosses: v.glosses, transparency: v.transparency });
  }
  return appended;
}

interface TableState {
  sessionId: string | null;
  sessionCode: string | null;
  worldKeys: string[];
  turns: ConversationTurn[];
  roundOpen: boolean;
  closed: boolean;
  isLoading: boolean;
  error: string | null;
  errorRecoverable: boolean;
  // Stage 0c (Build-Plan.md): the real table session round cap, from the
  // API - null only before a session/transcript response has arrived.
  roundCap: number | null;
}

const initialState: TableState = {
  sessionId: null,
  sessionCode: null,
  worldKeys: [],
  turns: [],
  roundOpen: false,
  closed: false,
  isLoading: false,
  error: null,
  errorRecoverable: false,
  roundCap: null,
};

export function useTable() {
  const [state, setState] = useState<TableState>(initialState);
  // The continue-loop reads credentials from here rather than from the
  // (stale) closure state React handed the callback.
  const sessionRef = useRef<{ sessionId: string; sessionCode: string } | null>(null);
  const lastAttemptRef = useRef<{ text: string; id: string } | null>(null);
  // Guards the continue loop against running twice at once (mid-round
  // reload auto-resume racing an existing loop) - the server refuses the
  // overlap too (TableAdvanceInFlight); this simply avoids provoking it.
  const loopingRef = useRef(false);

  const applyAdvance = useCallback((advance: TableMessageResponse) => {
    setState((prev) => ({
      ...prev,
      turns: [...prev.turns, ...turnsFromAdvance(advance)],
      roundOpen: advance.round_open,
      closed: advance.session_closed || prev.closed,
      isLoading: advance.round_open,
    }));
    if (advance.session_closed) clearStored();
  }, []);

  const runRound = useCallback(
    async (first: TableMessageResponse) => {
      if (loopingRef.current) return;
      loopingRef.current = true;
      applyAdvance(first);
      let open = first.round_open && !first.session_closed;
      while (open && sessionRef.current) {
        try {
          const next = await continueRound(sessionRef.current.sessionId, sessionRef.current.sessionCode);
          applyAdvance(next);
          open = next.round_open && !next.session_closed;
        } catch (error) {
          const message = error instanceof ApiRequestError ? error.message : 'The table lost its thread mid-round - you can pick the round back up below.';
          const recoverable = error instanceof ApiRequestError && error.recoverable;
          setState((prev) => ({ ...prev, isLoading: false, error: message, errorRecoverable: recoverable }));
          loopingRef.current = false;
          return;
        }
      }
      loopingRef.current = false;
      setState((prev) => ({ ...prev, isLoading: false }));
    },
    [applyAdvance]
  );

  const convene = useCallback(async (worldKeys: string[]) => {
    setState((prev) => ({ ...prev, isLoading: true, error: null, errorRecoverable: false }));
    try {
      const { session_id, session_code, round_cap } = await createTableSession(worldKeys);
      sessionRef.current = { sessionId: session_id, sessionCode: session_code };
      writeStored({ sessionId: session_id, sessionCode: session_code, mode: 'table', worldKeys });
      // create_table_session already appends the Facilitator's door turn,
      // so one transcript fetch opens the room introduced, not empty.
      const transcript = await getTranscript(session_id, session_code);
      setState({
        sessionId: session_id,
        sessionCode: session_code,
        worldKeys,
        turns: transcript.transcript.map(toTurn),
        roundOpen: transcript.round_open,
        closed: transcript.closed,
        isLoading: false,
        error: null,
        errorRecoverable: false,
        roundCap: round_cap,
      });
      return session_id;
    } catch (error) {
      const message = error instanceof ApiRequestError ? error.message : 'We couldn\'t convene the table just now - check your connection, then try again.';
      const recoverable = error instanceof ApiRequestError && error.recoverable;
      setState((prev) => ({ ...prev, isLoading: false, error: message, errorRecoverable: recoverable }));
      return null;
    }
  }, []);

  const send = useCallback(
    async (text: string) => {
      const session = sessionRef.current;
      if (!session) {
        setState((prev) => ({ ...prev, error: 'No table convened' }));
        return false;
      }
      setState((prev) => ({ ...prev, isLoading: true, error: null, errorRecoverable: false, turns: [...prev.turns, { speaker: 'participant', text }] }));
      try {
        const attempt = lastAttemptRef.current?.text === text ? lastAttemptRef.current : { text, id: crypto.randomUUID() };
        lastAttemptRef.current = attempt;
        const first = await sendTableMessage(session.sessionId, session.sessionCode, text, attempt.id);
        await runRound(first);
        return true;
      } catch (error) {
        const message = error instanceof ApiRequestError ? error.message : 'That message didn\'t go through - check your connection and try again.';
        const recoverable = error instanceof ApiRequestError && error.recoverable;
        setState((prev) => ({ ...prev, isLoading: false, error: message, errorRecoverable: recoverable }));
        return false;
      }
    },
    [runRound]
  );

  const rehydrate = useCallback(async (): Promise<string[] | null> => {
    const stored = readStored();
    if (!stored || stored.mode !== 'table' || !stored.worldKeys) return null;
    try {
      const transcript = await getTranscript(stored.sessionId, stored.sessionCode);
      if (transcript.closed) {
        clearStored();
        return null;
      }
      sessionRef.current = { sessionId: stored.sessionId, sessionCode: stored.sessionCode };
      setState({
        sessionId: stored.sessionId,
        sessionCode: stored.sessionCode,
        worldKeys: transcript.world_keys ?? stored.worldKeys,
        turns: transcript.transcript.map(toTurn),
        roundOpen: transcript.round_open,
        closed: transcript.closed,
        isLoading: false,
        error: null,
        errorRecoverable: false,
        roundCap: transcript.round_cap,
      });
      // A round left open by a mid-round reload is resumable - keep
      // continuing it so the table finishes what it was saying.
      if (transcript.round_open) {
        setState((prev) => ({ ...prev, isLoading: true }));
        await runRound({
          round_no: 0, round_open: true, routing_action: null, routing_reason: '', degraded: false,
          facilitator: [], turn_selected: null, voice: null, position: null, turn_no: null, session_closed: false,
        });
      }
      return transcript.world_keys ?? stored.worldKeys;
    } catch {
      clearStored();
      return null;
    }
  }, [runRound]);

  const resumeRound = useCallback(async () => {
    // A mid-round failure leaves roundOpen true with the loop stopped -
    // without this, the room was permanently stuck behind a 409 the UI
    // gave no way out of (foundation audit). Re-enter the continue loop;
    // the server replays the open round's real state.
    setState((prev) => ({ ...prev, isLoading: true, error: null, errorRecoverable: false }));
    await runRound({
      round_no: 0, round_open: true, routing_action: null, routing_reason: '', degraded: false,
      facilitator: [], turn_selected: null, voice: null, position: null, turn_no: null, session_closed: false,
    });
  }, [runRound]);

  const reset = useCallback(() => {
    clearStored();
    sessionRef.current = null;
    setState(initialState);
  }, []);

  return {
    sessionId: state.sessionId,
    sessionCode: state.sessionCode,
    worldKeys: state.worldKeys,
    turns: state.turns,
    roundOpen: state.roundOpen,
    roundCap: state.roundCap,
    closed: state.closed,
    isLoading: state.isLoading,
    error: state.error,
    errorRecoverable: state.errorRecoverable,
    convene,
    send,
    resumeRound,
    rehydrate,
    reset,
  };
}
