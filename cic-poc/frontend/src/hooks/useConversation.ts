/**
 * React hook for managing conversation state and API communication.
 * Supports both single-world and multi-world table sessions.
 */

import { useState, useCallback } from 'react';
import type {
  ConversationState,
  StartSessionResponse,
  SendMessageResponse,
} from '../types/conversation';

const API_BASE = '/api';

const initialState: ConversationState = {
  sessionId: null,
  worldId: null,
  worldIds: [],
  messages: [],
  phase: 'reception',
  turnCount: 0,
  isLoading: false,
  error: null,
};

export function useConversation() {
  const [state, setState] = useState<ConversationState>(initialState);

  /**
   * Start a new conversation session for a specific world.
   */
  const startSession = useCallback(async (worldId: string) => {
    setState((prev) => ({ ...prev, isLoading: true, error: null }));

    try {
      const response = await fetch(`${API_BASE}/session/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ world_id: worldId }),
      });

      if (!response.ok) {
        throw new Error(`Failed to start session: ${response.statusText}`);
      }

      const data: StartSessionResponse = await response.json();

      setState({
        sessionId: data.session_id,
        worldId: data.world_id,
        worldIds: data.world_ids || [data.world_id],
        messages: data.messages,
        phase: 'active_encounter',
        turnCount: 0,
        isLoading: false,
        error: null,
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
   * @param worldIds Array of world IDs to invite to the table (1-5 worlds)
   */
  const startMultiWorldSession = useCallback(async (worldIds: string[]) => {
    if (worldIds.length === 0) {
      setState((prev) => ({ ...prev, error: 'At least one world is required' }));
      return null;
    }

    setState((prev) => ({ ...prev, isLoading: true, error: null }));

    try {
      const response = await fetch(`${API_BASE}/session/start`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ world_ids: worldIds }),
      });

      if (!response.ok) {
        throw new Error(`Failed to start session: ${response.statusText}`);
      }

      const data: StartSessionResponse = await response.json();

      setState({
        sessionId: data.session_id,
        worldId: data.world_id,
        worldIds: data.world_ids || [data.world_id],
        messages: data.messages,
        phase: 'active_encounter',
        turnCount: 0,
        isLoading: false,
        error: null,
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
   * Send a message in the current conversation.
   */
  const sendMessage = useCallback(async (message: string) => {
    if (!state.sessionId) {
      setState((prev) => ({ ...prev, error: 'No active session' }));
      return false;
    }

    setState((prev) => ({ ...prev, isLoading: true, error: null }));

    try {
      const response = await fetch(
        `${API_BASE}/session/${state.sessionId}/message`,
        {
          method: 'POST',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message, close_requested: false }),
        }
      );

      if (!response.ok) {
        throw new Error(`Failed to send message: ${response.statusText}`);
      }

      const data: SendMessageResponse = await response.json();

      setState((prev) => ({
        ...prev,
        messages: data.messages,
        phase: data.phase,
        turnCount: data.turn_count,
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
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify({ message: '', close_requested: true }),
        }
      );

      if (!response.ok) {
        throw new Error(`Failed to end conversation: ${response.statusText}`);
      }

      const data: SendMessageResponse = await response.json();

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
    setState(initialState);
  }, []);

  /**
   * Clear any error state.
   */
  const clearError = useCallback(() => {
    setState((prev) => ({ ...prev, error: null }));
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
  };
}
