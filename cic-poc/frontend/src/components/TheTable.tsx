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
import { ArrivingLockup } from './ArrivingLockup';
import { MessageBubble } from './MessageBubble';
import { ChatInput } from './ChatInput';
import { LexiconModal } from './LexiconModal';
import { CitationModal } from './CitationModal';
import { OnboardingScreen, hasSeenOnboarding } from './OnboardingScreen';
import { SignInScreen } from './SignInScreen';
import { supabase, supabaseEnabled } from '../lib/supabase';
import { getTermMatches } from './LexiconHighlight';
import type { Citation, LexiconTerm, World } from '../types/conversation';

export function TheTable() {
  // Shown once per tester (a persistent localStorage flag, not once per
  // session) - re-shown only if their browser's local storage itself
  // resets, which is the same edge case that would confuse them anyway.
  const [showOnboarding, setShowOnboarding] = useState(() => !hasSeenOnboarding());
  // Signed in by default when Supabase isn't configured (local dev / before
  // Mark's project exists) - the sign-in screen only appears once a real
  // pilot deployment is wired up, same "off until configured" pattern as
  // the backend's session_cap.py.
  const [isSignedIn, setIsSignedIn] = useState(!supabaseEnabled);
  const [selectedWorlds, setSelectedWorlds] = useState<World[]>([]);
  const [showWorldSelector, setShowWorldSelector] = useState(true);

  useEffect(() => {
    if (!supabase) return;
    supabase.auth.getSession().then(({ data }) => setIsSignedIn(Boolean(data.session)));
    const { data: subscription } = supabase.auth.onAuthStateChange((_event, session) => {
      setIsSignedIn(Boolean(session));
    });
    return () => subscription.subscription.unsubscribe();
  }, []);

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
  // Whether a Level-3 surface is open (§3) - on desktop this narrows the
  // transcript column so the side panel never covers it; see table.css.
  const isLevel3Open = selectedTerm !== null || selectedCitations !== null;

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

  // Mode is emergent from seat count (§4) - one seat is a Deep Interview,
  // two-three is Compare Worlds; the value already sent to the backend
  // (world_id vs. world_ids) is unchanged, just no longer chosen up front.
  const handleBegin = async (worlds: World[]) => {
    setSelectedWorlds(worlds);
    setShowWorldSelector(false);
    if (worlds.length === 1) {
      await startSession(worlds[0].id);
    } else {
      await startMultiWorldSession(worlds.map(w => w.id));
    }
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

  if (!isSignedIn) {
    return <SignInScreen />;
  }

  // Pre-encounter onboarding - gates everything else, shown once per tester
  if (showOnboarding) {
    return <OnboardingScreen onContinue={() => setShowOnboarding(false)} />;
  }

  // World selection screen
  if (showWorldSelector) {
    return (
      <div className="table-container table-container--selector">
        <ArrivingLockup />

        <WorldSelector onBegin={handleBegin} />
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

  // The table bar (§2): one quiet chrome line, replacing the old
  // table-header--conversation + the standalone RefreshWarningBanner it sat
  // above. Left: seats (unchanged single-vs-multi rendering, just restyled).
  // Right: the consolidated status line - priority-ordered, never stacked.
  // `showStatus` is false in the closing/ended view, matching the old
  // RefreshWarningBanner's own behavior (it never rendered there either).
  const renderTableBar = (showStatus: boolean) => {
    // No live "nearing the session length limit" signal exists yet (no
    // per-conversation turn/token cap is surfaced by the backend today) -
    // this priority slot is reserved but unreachable until that data
    // exists. See Decision-Log.
    const statusMessage = showStatus
      ? 'This conversation lives in this tab — refreshing loses it'
      : '';

    return (
      <div className="table-bar">
        <div className="table-bar__seats">
          {selectedWorlds.length === 1 ? (
            <span className="table-bar__seat">
              <span
                className="table-bar__seat-dot"
                style={{ backgroundColor: selectedWorlds[0].color }}
              />
              <span className="table-bar__seat-name">
                {selectedWorlds[0].name} · {selectedWorlds[0].period}
              </span>
            </span>
          ) : (
            selectedWorlds.map(world => (
              <span key={world.id} className="table-bar__seat">
                <span
                  className="table-bar__seat-dot"
                  style={{ backgroundColor: world.color }}
                />
                <span className="table-bar__seat-name">
                  {world.representative.name}
                </span>
              </span>
            ))
          )}
        </div>
        <div className="table-bar__status">{statusMessage}</div>
      </div>
    );
  };

  // Conversation ended
  if (phase === 'closing' && !isLoading) {
    return (
      <div className={`table-container table-container--conversation${isLevel3Open ? ' table-container--panel-open' : ''}`}>
        {renderTableBar(false)}

        <div className="messages-container">
          {messages.map((message, index) => (
            <MessageBubble
              key={index}
              message={message}
              termMap={resolveTermMap(message)}
              onTermClick={handleTermClick}
              onCitationClick={handleCitationClick}
              allowedTermKeys={firstOccurrenceKeysByIndex[index]}
              worldNames={Object.fromEntries(selectedWorlds.map(w => [
                w.representative.name.toLowerCase().replace(' ', '_'),
                w.name
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
    <div className={`table-container table-container--conversation${isLevel3Open ? ' table-container--panel-open' : ''}`}>
      {renderTableBar(true)}

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
            worldNames={Object.fromEntries(selectedWorlds.map(w => [
              w.representative.name.toLowerCase().replace(' ', '_'),
              w.name
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
