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
import { CitationModal } from './CitationModal';
import { getTermMatches } from './LexiconHighlight';
import type { Citation, LexiconTerm, World } from '../types/conversation';

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
  const { termMap, termMapsByWorld } = useLexicon(worldIds.length > 0 ? worldIds : worldId);

  // Speaker key (message.name form, e.g. "mar_yausep") -> that world's own
  // term map. Two different worlds can share an everyday word as an alias
  // (confirmed live: "elder" and "renunciation" both collide between two of
  // the four worlds) - resolving per-speaker, not off one map merged across
  // every world at the table, is what keeps a representative's own word
  // linked to their own world's definition instead of whichever world's
  // terms happened to load last.
  const termMapBySpeakerKey = useMemo(() => {
    const map = new Map<string, Map<string, LexiconTerm>>();
    for (const world of selectedWorlds) {
      const speakerKey = world.representative.name.toLowerCase().replace(' ', '_');
      const worldTermMap = termMapsByWorld.get(world.id);
      if (worldTermMap) {
        map.set(speakerKey, worldTermMap);
      }
    }
    return map;
  }, [selectedWorlds, termMapsByWorld]);

  // A term gets the interactive highlight/tooltip treatment only the first
  // time it appears across the whole conversation - once a participant has
  // seen and can click a term, repeating the same visual treatment on every
  // later mention (sometimes many times a round) is noise, not help.
  const firstOccurrenceKeysByIndex = useMemo(() => {
    // Tracked per (world, key), not per raw key alone - two worlds can share
    // an alias (see termMapBySpeakerKey's comment), and deduping on the raw
    // key only would let an already-seen key from one world's vocabulary
    // wrongly suppress a genuinely first-time highlight of a different
    // world's own term that happens to share the same spelling.
    const seen = new Set<string>();
    return messages.map((message) => {
      const speakerKey = message.name?.toLowerCase().replace(' ', '_') || '';
      const messageTermMap = termMapBySpeakerKey.get(speakerKey);
      if (message.role !== 'assistant' || message.name === 'facilitator' || !messageTermMap || messageTermMap.size === 0) {
        return new Set<string>();
      }
      const newKeys = new Set<string>();
      for (const key of getTermMatches(message.content, messageTermMap)) {
        const seenKey = `${speakerKey}:${key}`;
        if (!seen.has(seenKey)) {
          seen.add(seenKey);
          newKeys.add(key);
        }
      }
      return newKeys;
    });
  }, [messages, termMapBySpeakerKey]);
  const [selectedTerm, setSelectedTerm] = useState<LexiconTerm | null>(null);
  const [selectedCitations, setSelectedCitations] = useState<Citation[] | null>(null);

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

  // The correct term map for a given message's own speaker - falls back to
  // the merged map (facilitator messages, or a speaker key not found in
  // termMapBySpeakerKey) rather than an empty map, so highlighting degrades
  // gracefully instead of silently vanishing for an edge case.
  const resolveTermMap = (message: { name?: string | null }) => {
    const speakerKey = message.name?.toLowerCase().replace(' ', '_') || '';
    return termMapBySpeakerKey.get(speakerKey) ?? termMap;
  };

  const closeModal = () => {
    setSelectedTerm(null);
  };

  const handleCitationClick = (citations: Citation[]) => {
    setSelectedCitations(citations);
  };

  const closeCitationModal = () => {
    setSelectedCitations(null);
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
              termMap={resolveTermMap(message)}
              onTermClick={handleTermClick}
              onCitationClick={handleCitationClick}
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
        {selectedCitations && (
          <CitationModal citations={selectedCitations} onClose={closeCitationModal} />
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
            termMap={resolveTermMap(message)}
            onTermClick={handleTermClick}
            onCitationClick={handleCitationClick}
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
      {selectedCitations && (
        <CitationModal citations={selectedCitations} onClose={closeCitationModal} />
      )}
    </div>
  );
}
