/**
 * React hook for managing conversation state and API communication.
 * Supports both single-world and multi-world table sessions.
 */

import { useState, useCallback } from 'react';
import type {
  ConversationState,
  StartSessionResponse,
  SendMessageResponse,
  SessionResponse,
} from '../types/conversation';
import { getAccessToken } from '../lib/supabase';

const API_BASE = '/api';

// Wave 3 (Engineering P1-11): a refresh used to lose the conversation
// outright - session state lived only in React memory, and the reconnect
// endpoint (GET /api/session/{id}) existed but nothing ever called it.
// sessionStorage (not localStorage) on purpose: this should survive a
// reload of the same tab, not follow the participant to a new tab or
// persist indefinitely - the same lifetime the session itself has.
const SESSION_STORAGE_KEY = 'cic_session';

interface StoredSession {
  sessionId: string;
  sessionToken: string;
}

function saveSessionToStorage(sessionId: string, sessionToken: string) {
  try {
    sessionStorage.setItem(SESSION_STORAGE_KEY, JSON.stringify({ sessionId, sessionToken }));
  } catch {
    // Storage unavailable (private browsing, quota) - reconnect-on-refresh
    // simply won't work; nothing else depends on this write succeeding.
  }
}

function readSessionFromStorage(): StoredSession | null {
  try {
    const raw = sessionStorage.getItem(SESSION_STORAGE_KEY);
    if (!raw) return null;
    const parsed = JSON.parse(raw);
    if (typeof parsed?.sessionId === 'string' && typeof parsed?.sessionToken === 'string') {
      return parsed;
    }
    return null;
  } catch {
    return null;
  }
}

function clearSessionStorage() {
  try {
    sessionStorage.removeItem(SESSION_STORAGE_KEY);
  } catch {
    // Nothing to clean up if storage isn't available in the first place.
  }
}

// Synchronous peek so the caller can decide its *initial* render (avoids a
// loading flash of the World Selector for the common case - a brand-new
// visitor with nothing stored - while still gating on a real reconnect
// attempt for a returning one).
export function hasStoredSession(): boolean {
  return readSessionFromStorage() !== null;
}

// Attaches the signed-in participant's Supabase access token (see
// src/lib/supabase.ts), replacing the old ?code=... tester-code scheme.
// Resolves to plain JSON headers, no Authorization header at all, when
// Supabase isn't configured (local dev / mock mode) - the backend's
// get_current_user dependency treats that the same way it always has.
async function authHeaders(): Promise<Record<string, string>> {
  const token = await getAccessToken();
  return token ? { Authorization: `Bearer ${token}` } : {};
}

async function extractErrorMessage(response: Response, fallback: string): Promise<string> {
  try {
    const body = await response.json();
    if (typeof body?.detail === 'string') {
      return body.detail;
    }
  } catch {
    // Response wasn't JSON - fall through to the generic message
  }
  return fallback;
}

// The possession secret session/start hands back once, required on every
// later request to that session (see the backend's app/session_auth.py) -
// proves this browser is the one that started the session, since sign-in is
// optional and every anonymous participant otherwise looks the same.
function sessionTokenHeader(token: string | null): Record<string, string> {
  return token ? { 'X-Session-Token': token } : {};
}

const initialState: ConversationState & { isStreaming: boolean } = {
  sessionId: null,
  sessionToken: null,
  worldId: null,
  worldIds: [],
  messages: [],
  phase: 'reception',
  turnCount: 0,
  isLoading: false,
  error: null,
  isStreaming: false,
};

interface StreamEvent {
  type: 'speaker_start' | 'token' | 'speaker_end' | 'done' | 'error';
  speaker?: string;
  text?: string;
  citations?: import('../types/conversation').Citation[] | null;
  glosses_used?: import('../types/conversation').GlossUsed[] | null;
  phase?: string;
  turn_count?: number;
  message?: string;
}

export function useConversation() {
  const [state, setState] = useState<ConversationState & { isStreaming: boolean }>(initialState);

  /**
   * Start a new conversation session for a specific world.
   */
  const startSession = useCallback(async (worldId: string, persona?: string) => {
    setState((prev) => ({ ...prev, isLoading: true, error: null }));

    try {
      const response = await fetch(`${API_BASE}/session/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', ...(await authHeaders()) },
        body: JSON.stringify({ world_id: worldId, persona }),
      });

      if (!response.ok) {
        throw new Error(await extractErrorMessage(response, `Failed to start session: ${response.statusText}`));
      }

      const data: StartSessionResponse = await response.json();
      saveSessionToStorage(data.session_id, data.session_token);

      setState({
        sessionId: data.session_id,
        sessionToken: data.session_token,
        worldId: data.world_id,
        worldIds: data.world_ids || [data.world_id],
        messages: data.messages,
        phase: 'active_encounter',
        turnCount: 0,
        isLoading: false,
        error: null,
        isStreaming: false,
      });

      return data.session_id;
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      setState((prev) => ({
        ...prev,
        isLoading: false,
        error: errorMessage,
      }));
      return null;
    }
  }, []);

  /**
   * Start a new multi-world conversation session.
   * @param worldIds Array of world IDs to invite to the table (1-3 worlds)
   */
  const startMultiWorldSession = useCallback(async (worldIds: string[], persona?: string) => {
    if (worldIds.length === 0) {
      setState((prev) => ({ ...prev, error: 'At least one world is required' }));
      return null;
    }

    setState((prev) => ({ ...prev, isLoading: true, error: null }));

    try {
      const response = await fetch(`${API_BASE}/session/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json', ...(await authHeaders()) },
        body: JSON.stringify({ world_ids: worldIds, persona }),
      });

      if (!response.ok) {
        throw new Error(await extractErrorMessage(response, `Failed to start session: ${response.statusText}`));
      }

      const data: StartSessionResponse = await response.json();
      saveSessionToStorage(data.session_id, data.session_token);

      setState({
        sessionId: data.session_id,
        sessionToken: data.session_token,
        worldId: data.world_id,
        worldIds: data.world_ids || [data.world_id],
        messages: data.messages,
        phase: 'active_encounter',
        turnCount: 0,
        isLoading: false,
        error: null,
        isStreaming: false,
      });

      return data.session_id;
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      setState((prev) => ({
        ...prev,
        isLoading: false,
        error: errorMessage,
      }));
      return null;
    }
  }, []);

  /**
   * Send a message in the current conversation, streaming each representative's
   * reply token-by-token as it's generated rather than waiting for the full
   * turn (or full multi-representative round) to complete.
   */
  const sendMessage = useCallback(async (message: string) => {
    if (!state.sessionId) {
      setState((prev) => ({ ...prev, error: 'No active session' }));
      return false;
    }

    setState((prev) => ({
      ...prev,
      isLoading: true,
      isStreaming: false,
      error: null,
      // The streaming endpoint only emits representative events, not an echo
      // of the participant's own message, so add it optimistically here.
      messages: [...prev.messages, { role: 'user', content: message, name: null, citations: null }],
    }));

    try {
      const response = await fetch(
        `${API_BASE}/session/${state.sessionId}/message/stream`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            ...sessionTokenHeader(state.sessionToken),
          },
          body: JSON.stringify({ message, close_requested: false }),
        }
      );

      if (!response.ok || !response.body) {
        throw new Error(`Failed to send message: ${response.statusText}`);
      }

      const applyEvent = (evt: StreamEvent) => {
        switch (evt.type) {
          case 'speaker_start':
            setState((prev) => ({
              ...prev,
              isStreaming: true,
              messages: [
                ...prev.messages,
                { role: 'assistant', content: '', name: evt.speaker ?? null, citations: null, glosses_used: null },
              ],
            }));
            break;
          case 'token':
            setState((prev) => {
              const messages = prev.messages.slice();
              const lastIndex = messages.length - 1;
              if (lastIndex >= 0) {
                messages[lastIndex] = {
                  ...messages[lastIndex],
                  content: messages[lastIndex].content + (evt.text ?? ''),
                };
              }
              return { ...prev, messages };
            });
            break;
          case 'speaker_end':
            setState((prev) => {
              const messages = prev.messages.slice();
              const lastIndex = messages.length - 1;
              if (lastIndex >= 0) {
                messages[lastIndex] = {
                  ...messages[lastIndex],
                  citations: evt.citations ?? null,
                  glosses_used: evt.glosses_used ?? null,
                };
              }
              return { ...prev, messages };
            });
            break;
          case 'done':
            if (evt.phase === 'closing') {
              // A sensed close (the wind-down sequence reaching its end)
              // reaches 'closing' the same way an explicit end-conversation
              // does - same reasoning, same cleanup.
              clearSessionStorage();
            }
            setState((prev) => ({
              ...prev,
              phase: (evt.phase as ConversationState['phase']) ?? prev.phase,
              turnCount: evt.turn_count ?? prev.turnCount,
              isLoading: false,
              isStreaming: false,
            }));
            break;
          case 'error':
            setState((prev) => ({
              ...prev,
              isLoading: false,
              isStreaming: false,
              error: evt.message ?? 'Something went wrong while streaming the response',
            }));
            break;
        }
      };

      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = '';

      while (true) {
        const { value, done } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });

        let boundary = buffer.indexOf('\n\n');
        while (boundary !== -1) {
          const rawEvent = buffer.slice(0, boundary);
          buffer = buffer.slice(boundary + 2);

          const dataLine = rawEvent.split('\n').find((line) => line.startsWith('data:'));
          if (dataLine) {
            const jsonStr = dataLine.slice(5).trim();
            if (jsonStr) {
              try {
                applyEvent(JSON.parse(jsonStr) as StreamEvent);
              } catch {
                // Skip malformed/partial event rather than breaking the stream
              }
            }
          }

          boundary = buffer.indexOf('\n\n');
        }
      }

      return true;
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      setState((prev) => ({
        ...prev,
        isLoading: false,
        isStreaming: false,
        error: errorMessage,
      }));
      return false;
    }
  }, [state.sessionId]);

  /**
   * End the current conversation gracefully.
   */
  const endConversation = useCallback(async () => {
    if (!state.sessionId) {
      return false;
    }

    setState((prev) => ({ ...prev, isLoading: true, error: null }));

    try {
      const response = await fetch(
        `${API_BASE}/session/${state.sessionId}/message`,
        {
          method: 'POST',
          headers: {
            'Content-Type': 'application/json',
            ...sessionTokenHeader(state.sessionToken),
          },
          body: JSON.stringify({ message: '', close_requested: true }),
        }
      );

      if (!response.ok) {
        throw new Error(`Failed to end conversation: ${response.statusText}`);
      }

      const data: SendMessageResponse = await response.json();

      // Nothing left to reconnect into once a conversation reaches its
      // natural end - same reasoning rehydrateSession applies on the read
      // side for a session it discovers is already 'closing'.
      clearSessionStorage();

      setState((prev) => ({
        ...prev,
        messages: data.messages,
        phase: 'closing',
        isLoading: false,
      }));

      return true;
    } catch (error) {
      const errorMessage = error instanceof Error ? error.message : 'Unknown error';
      setState((prev) => ({
        ...prev,
        isLoading: false,
        error: errorMessage,
      }));
      return false;
    }
  }, [state.sessionId]);

  /**
   * Reset the conversation state.
   */
  const resetConversation = useCallback(() => {
    clearSessionStorage();
    setState(initialState);
  }, []);

  /**
   * Clear any error state.
   */
  const clearError = useCallback(() => {
    setState((prev) => ({ ...prev, error: null }));
  }, []);

  /**
   * Reconnect to a session saved in sessionStorage (Wave 3, Engineering
   * P1-11) - called once on mount, before the world-selection screen would
   * otherwise show. Returns the restored world id(s) if a live session was
   * restored (the caller needs these to reconstruct World objects for
   * display, and can't rely on this hook's own state - it wouldn't have
   * re-rendered into the caller's async callback yet), or null if there was
   * nothing to restore or the saved session is no longer valid (expired,
   * 404'd, or the token no longer matches) - in which case the stale entry
   * is cleared so this doesn't loop on every future mount.
   */
  const rehydrateSession = useCallback(async (): Promise<{ worldId: string | null; worldIds: string[] } | null> => {
    const stored = readSessionFromStorage();
    if (!stored) return null;

    try {
      const response = await fetch(`${API_BASE}/session/${stored.sessionId}`, {
        headers: sessionTokenHeader(stored.sessionToken),
      });
      if (!response.ok) {
        clearSessionStorage();
        return null;
      }
      const data: SessionResponse = await response.json();
      if (data.phase === 'closing') {
        // Session already reached its natural end - nothing to resume into,
        // and the "closing" screen with no live send/end path would just
        // strand the participant. Treat it the same as an expired session.
        clearSessionStorage();
        return null;
      }

      const restoredWorldIds =
        data.world_ids && data.world_ids.length > 0 ? data.world_ids : data.world_id ? [data.world_id] : [];

      setState({
        sessionId: data.session_id,
        sessionToken: stored.sessionToken,
        worldId: data.world_id ?? null,
        worldIds: restoredWorldIds,
        messages: data.messages,
        phase: data.phase,
        turnCount: data.turn_count,
        isLoading: false,
        error: null,
        isStreaming: false,
      });
      return { worldId: data.world_id ?? null, worldIds: restoredWorldIds };
    } catch {
      clearSessionStorage();
      return null;
    }
  }, []);

  return {
    // State
    sessionId: state.sessionId,
    worldId: state.worldId,
    worldIds: state.worldIds,
    messages: state.messages,
    phase: state.phase,
    turnCount: state.turnCount,
    isLoading: state.isLoading,
    isStreaming: state.isStreaming,
    error: state.error,
    isActive: state.sessionId !== null && state.phase !== 'closing',
    isMultiWorld: state.worldIds.length > 1,

    // Actions
    startSession,
    startMultiWorldSession,
    sendMessage,
    endConversation,
    resetConversation,
    clearError,
    rehydrateSession,
  };
}
