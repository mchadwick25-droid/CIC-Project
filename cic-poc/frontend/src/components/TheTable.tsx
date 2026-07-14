/**
 * TheTable component - main conversation container.
 *
 * Flow:
 * 1. Show WorldSelector to choose tradition(s)
 * 2. Start conversation with selected world's representative(s)
 * 3. Display messages with lexicon highlighting
 *
 * Supports both single-world and multi-world (up to 3 representatives) tables.
 */

import { useEffect, useMemo, useRef, useState } from 'react';
import { useConversation } from '../hooks/useConversation';
import { useLexicon } from '../hooks/useLexicon';
import { WorldSelector } from './WorldSelector';
import { MessageBubble } from './MessageBubble';
import { ChatInput } from './ChatInput';
import { LexiconModal } from './LexiconModal';
import { getTermMatches } from './LexiconHighlight';
import type { LexiconTerm, World } from '../types/conversation';

export function TheTable() {
  const [selectedWorlds, setSelectedWorlds] = useState<World[]>([]);
  const [showWorldSelector, setShowWorldSelector] = useState(true);
  const [multiSelectMode, setMultiSelectMode] = useState(false);

  const {
    sessionId,
    worldId,
    worldIds,
    messages,
    phase,
    isLoading,
    isStreaming,
    error,
    isActive,
    startSession,
    startMultiWorldSession,
    sendMessage,
    endConversation,
    resetConversation,
    clearError,
  } = useConversation();

  // Every world at the table, not just the primary one - each representative
  // needs their own vocabulary highlightable, not only the first world's.
  const { termMap } = useLexicon(worldIds.length > 0 ? worldIds : worldId);

  // A term gets the interactive highlight/tooltip treatment only the first
  // time it appears across the whole conversation - once a participant has
  // seen and can click a term, repeating the same visual treatment on every
  // later mention (sometimes many times a round) is noise, not help.
  const firstOccurrenceKeysByIndex = useMemo(() => {
    const seen = new Set<string>();
    return messages.map((message) => {
      if (message.role !== 'assistant' || message.name === 'facilitator' || termMap.size === 0) {
        return new Set<string>();
      }
      const newKeys = new Set<string>();
      for (const key of getTermMatches(message.content, termMap)) {
        if (!seen.has(key)) {
          seen.add(key);
          newKeys.add(key);
        }
      }
      return newKeys;
    });
  }, [messages, termMap]);
  const [selectedTerm, setSelectedTerm] = useState<LexiconTerm | null>(null);

  const messagesEndRef = useRef<HTMLDivElement>(null);
  // Whether the participant is scrolled near the live edge right now. Starts
  // true (a fresh conversation opens pinned to the bottom). Read as a ref,
  // not state, so tracking scroll position doesn't itself trigger renders.
  const isPinnedToBottomRef = useRef(true);

  // Plain React onScroll prop (bound directly in JSX below), not a manually
  // managed addEventListener - this sidesteps any ref/effect mount-timing
  // question entirely (an earlier addEventListener-in-a-callback-ref version
  // and an IntersectionObserver version were both tried here; this is the
  // simplest implementation with the fewest places to get the timing wrong).
  const handleMessagesScroll = (event: React.UIEvent<HTMLDivElement>) => {
    const el = event.currentTarget;
    const distanceFromBottom = el.scrollHeight - el.scrollTop - el.clientHeight;
    isPinnedToBottomRef.current = distanceFromBottom < 120;
  };

  // Auto-scroll to bottom as new messages/tokens arrive - but only when the
  // participant was already pinned to the live edge. Scrolling up to reread
  // an earlier turn must not get yanked back down by a streaming response;
  // auto-scroll simply resumes once they return to the bottom themselves.
  useEffect(() => {
    if (isPinnedToBottomRef.current) {
      messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' });
    }
  }, [messages]);

  const handleWorldSelect = async (world: World) => {
    setSelectedWorlds([world]);
    setShowWorldSelector(false);
    await startSession(world.id);
  };

  const handleMultiWorldSelect = async (worlds: World[]) => {
    setSelectedWorlds(worlds);
    setShowWorldSelector(false);
    await startMultiWorldSession(worlds.map(w => w.id));
  };

  const handleTermClick = (term: LexiconTerm) => {
    setSelectedTerm(term);
  };

  const closeModal = () => {
    setSelectedTerm(null);
  };

  const handleResetConversation = () => {
    resetConversation();
    setSelectedWorlds([]);
    setShowWorldSelector(true);
  };

  // World selection screen
  if (showWorldSelector) {
    return (
      <div className="table-container table-container--selector">
        <header className="table-header">
          <h1>The Table</h1>
          <p>A space for engaging conversation with voices from Christian history</p>
        </header>

        <div className="table-mode-toggle">
          <button
            className={`mode-toggle-button ${!multiSelectMode ? 'mode-toggle-button--active' : ''}`}
            onClick={() => setMultiSelectMode(false)}
          >
            Single Representative
          </button>
          <button
            className={`mode-toggle-button ${multiSelectMode ? 'mode-toggle-button--active' : ''}`}
            onClick={() => setMultiSelectMode(true)}
          >
            Multiple Representatives
          </button>
        </div>

        <WorldSelector
          onSelectWorld={handleWorldSelect}
          onSelectWorlds={handleMultiWorldSelect}
          multiSelect={multiSelectMode}
        />
      </div>
    );
  }

  // Loading after world selection
  if (!sessionId && isLoading) {
    const repNames = selectedWorlds.map(w => w.representative.name).join(', ');
    return (
      <div className="table-container">
        <header className="table-header">
          <h1>The Table</h1>
          <p>A space for engaging conversation</p>
        </header>

        <div className="start-screen">
          <div className="loading-indicator loading-indicator--large">
            <div className="loading-dots">
              <span className="loading-dot"></span>
              <span className="loading-dot"></span>
              <span className="loading-dot"></span>
            </div>
            <span>
              {selectedWorlds.length > 1
                ? `Gathering ${repNames} at The Table...`
                : `Preparing your conversation with ${repNames}...`}
            </span>
          </div>
        </div>
      </div>
    );
  }

  // Error state
  if (!sessionId && error) {
    return (
      <div className="table-container">
        <header className="table-header">
          <h1>The Table</h1>
          <p>A space for engaging conversation</p>
        </header>

        <div className="start-screen">
          <div className="error-message">
            {error}
          </div>
          <button
            className="chat-button chat-button--primary"
            onClick={() => {
              clearError();
              setShowWorldSelector(true);
            }}
          >
            Try Again
          </button>
        </div>
      </div>
    );
  }

  // Build header content for active conversation
  const renderWorldIndicators = () => {
    if (selectedWorlds.length === 1) {
      const world = selectedWorlds[0];
      return (
        <div className="table-header__world">
          <span
            className="table-header__world-indicator"
            style={{ backgroundColor: world.color }}
          />
          <span className="table-header__world-name">
            {world.name} · {world.period}
          </span>
        </div>
      );
    }

    // Multi-world header
    return (
      <div className="table-header__worlds">
        {selectedWorlds.map(world => (
          <div key={world.id} className="table-header__world-badge">
            <span
              className="table-header__world-indicator"
              style={{ backgroundColor: world.color }}
            />
            <span className="table-header__world-badge-name">
              {world.representative.name}
            </span>
          </div>
        ))}
      </div>
    );
  };

  // Conversation ended
  if (phase === 'closing' && !isLoading) {
    return (
      <div className="table-container table-container--conversation">
        <header className="table-header table-header--conversation">
          {renderWorldIndicators()}
        </header>

        <div className="messages-container">
          {messages.map((message, index) => (
            <MessageBubble
              key={index}
              message={message}
              termMap={termMap}
              onTermClick={handleTermClick}
              allowedTermKeys={firstOccurrenceKeysByIndex[index]}
              worldColors={Object.fromEntries(selectedWorlds.map(w => [
                w.representative.name.toLowerCase().replace(' ', '_'),
                w.color
              ]))}
            />
          ))}
        </div>

        <div className="conversation-ended">
          <p>The conversation has ended.</p>
          <button className="chat-button chat-button--primary" onClick={handleResetConversation}>
            Return to World Selection
          </button>
        </div>

        {selectedTerm && (
          <LexiconModal term={selectedTerm} onClose={closeModal} />
        )}
      </div>
    );
  }

  // Active conversation
  return (
    <div className="table-container table-container--conversation">
      <header className="table-header table-header--conversation">
        {renderWorldIndicators()}
      </header>

      {error && (
        <div className="error-message">
          {error}
          <button onClick={clearError} style={{ marginLeft: '1rem' }}>
            Dismiss
          </button>
        </div>
      )}

      <div className="messages-container" onScroll={handleMessagesScroll}>
        {messages.map((message, index) => (
          <MessageBubble
            key={index}
            message={message}
            termMap={termMap}
            onTermClick={handleTermClick}
            allowedTermKeys={firstOccurrenceKeysByIndex[index]}
            worldColors={Object.fromEntries(selectedWorlds.map(w => [
              w.representative.name.toLowerCase().replace(' ', '_'),
              w.color
            ]))}
          />
        ))}

        {isLoading && !isStreaming && (
          <div className="loading-indicator">
            <div className="loading-dots">
              <span className="loading-dot"></span>
              <span className="loading-dot"></span>
              <span className="loading-dot"></span>
            </div>
            <span>Thinking...</span>
          </div>
        )}

        <div ref={messagesEndRef} />
      </div>

      <ChatInput
        onSend={sendMessage}
        onEnd={endConversation}
        disabled={!isActive}
        isLoading={isLoading}
      />

      {selectedTerm && (
        <LexiconModal term={selectedTerm} onClose={closeModal} />
      )}
    </div>
  );
}
