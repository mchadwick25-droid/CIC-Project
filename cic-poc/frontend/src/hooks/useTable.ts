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
import type { FacilitatorTurn, TableMessageResponse, TranscriptEntry, VoiceTurn } from '../types/conversation';
import type { ConversationTurn } from './useConversation';

function toTurn(entry: TranscriptEntry): ConversationTurn {
  if ('kind' in entry) return { speaker: 'facilitator', text: entry.text, kind: entry.kind };
  if ('citations' in entry) {
    return { speaker: entry.speaker, text: entry.text, citations: entry.citations, figuresUsed: entry.figures_used, glosses: entry.glosses };
  }
  return { speaker: 'participant', text: entry.text };
}

function turnsFromAdvance(advance: TableMessageResponse): ConversationTurn[] {
  const appended: ConversationTurn[] = [];
  for (const f of advance.facilitator as FacilitatorTurn[]) {
    appended.push({ speaker: 'facilitator', text: f.text, kind: f.kind });
  }
  const v = advance.voice as VoiceTurn | null;
  if (v) {
    appended.push({ speaker: v.speaker, text: v.text, citations: v.citations, figuresUsed: v.figures_used, glosses: v.glosses });
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
};

export function useTable() {
  const [state, setState] = useState<TableState>(initialState);
  // The continue-loop reads credentials from here rather than from the
  // (stale) closure state React handed the callback.
  const sessionRef = useRef<{ sessionId: string; sessionCode: string } | null>(null);

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
      applyAdvance(first);
      let open = first.round_open && !first.session_closed;
      while (open && sessionRef.current) {
        try {
          const next = await continueRound(sessionRef.current.sessionId, sessionRef.current.sessionCode);
          applyAdvance(next);
          open = next.round_open && !next.session_closed;
        } catch (error) {
          const message = error instanceof ApiRequestError ? error.message : 'The table lost its thread mid-round.';
          setState((prev) => ({ ...prev, isLoading: false, error: message }));
          return;
        }
      }
      setState((prev) => ({ ...prev, isLoading: false }));
    },
    [applyAdvance]
  );

  const convene = useCallback(async (worldKeys: string[]) => {
    setState((prev) => ({ ...prev, isLoading: true, error: null }));
    try {
      const { session_id, session_code } = await createTableSession(worldKeys);
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
      });
      return session_id;
    } catch (error) {
      const message = error instanceof ApiRequestError ? error.message : 'Could not convene the table.';
      setState((prev) => ({ ...prev, isLoading: false, error: message }));
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
      setState((prev) => ({ ...prev, isLoading: true, error: null, turns: [...prev.turns, { speaker: 'participant', text }] }));
      try {
        const first = await sendTableMessage(session.sessionId, session.sessionCode, text, crypto.randomUUID());
        await runRound(first);
        return true;
      } catch (error) {
        const message = error instanceof ApiRequestError ? error.message : 'That message did not go through.';
        setState((prev) => ({ ...prev, isLoading: false, error: message }));
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
    closed: state.closed,
    isLoading: state.isLoading,
    error: state.error,
    convene,
    send,
    rehydrate,
    reset,
  };
}
