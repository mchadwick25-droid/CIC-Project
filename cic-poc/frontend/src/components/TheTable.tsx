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
import { useConversation, hasStoredSession } from '../hooks/useConversation';
import { useLexicon } from '../hooks/useLexicon';
import { WorldSelector } from './WorldSelector';
import { ArrivingLockup } from './ArrivingLockup';
import { BrandMark } from './BrandMark';
import { MessageBubble } from './MessageBubble';
import { ChatInput } from './ChatInput';
import { LexiconModal } from './LexiconModal';
import { CitationModal } from './CitationModal';
import { OnboardingScreen, hasSeenOnboarding } from './OnboardingScreen';
import { SignInScreen } from './SignInScreen';
import { supabase, supabaseEnabled } from '../lib/supabase';
import { getTermMatches } from './LexiconHighlight';
import type { Citation, LexiconTerm, ResourcePack, World, WorldsResponse } from '../types/conversation';

export function TheTable() {
  // Shown once per tester (a persistent localStorage flag, not once per
  // session) - re-shown only if their browser's local storage itself
  // resets, which is the same edge case that would confuse them anyway.
  const [showOnboarding, setShowOnboarding] = useState(() => !hasSeenOnboarding());
  // Wave 3 (Readiness P0-3b): the onboarding screen's optional "what brings
  // you here?" answer, held here until a session actually starts (world
  // selection happens after onboarding) - for feedback correlation only,
  // sent as StartSessionRequest.persona, never touches participant_role.
  const [persona, setPersona] = useState<string | undefined>(undefined);
  // Signed in by default when Supabase isn't configured (local dev / before
  // Mark's project exists) - the sign-in screen only appears once a real
  // pilot deployment is wired up, same "off until configured" pattern as
  // the backend's session_cap.py.
  const [isSignedIn, setIsSignedIn] = useState(!supabaseEnabled);
  const [selectedWorlds, setSelectedWorlds] = useState<World[]>([]);
  // Wave 3 (Engineering P1-11): if a session is saved in sessionStorage, start
  // in a brief "reconnecting" state instead of flashing the World Selector -
  // a returning participant refreshing the tab should not have to re-pick
  // worlds and lose their transcript. A fresh visitor with nothing stored
  // skips this state entirely (isRehydrating starts false for them).
  const [isRehydrating, setIsRehydrating] = useState(() => hasStoredSession());
  const [showWorldSelector, setShowWorldSelector] = useState(() => !hasStoredSession());

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
    rehydrateSession,
  } = useConversation();

  useEffect(() => {
    if (!isRehydrating) return;
    let cancelled = false;
    rehydrateSession().then(async (restored) => {
      if (cancelled) return;
      if (!restored) {
        setIsRehydrating(false);
        setShowWorldSelector(true);
        return;
      }
      // Reconstruct selectedWorlds (representative names, term maps, colors)
      // from the same /api/worlds WorldSelector itself fetches from - the
      // hook only knows world ids, not the full World objects the rest of
      // this component renders from. Using restored.worldIds here (not the
      // worldId/worldIds destructured above) deliberately - this callback's
      // closure over those is stale until the hook's own setState above
      // lands and this component re-renders.
      try {
        const response = await fetch('/api/worlds');
        const data: WorldsResponse = await response.json();
        if (cancelled) return;
        const ids = new Set(restored.worldIds.length > 0 ? restored.worldIds : restored.worldId ? [restored.worldId] : []);
        setSelectedWorlds(data.worlds.filter((w) => ids.has(w.id)));
      } catch {
        // Conversation itself is restored even if this lookup fails - the
        // transcript and messaging still work, just without display names
        // resolving through selectedWorlds until the next reload.
      }
      setShowWorldSelector(false);
      setIsRehydrating(false);
    });
    return () => {
      cancelled = true;
    };
    // Deliberately runs once on mount only.
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

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
  // Phone-only: the table bar's status line truncates to its lead phrase;
  // tap expands it (§2, §6). No effect on desktop - CSS always shows the
  // full text there regardless of this state.
  const [statusExpanded, setStatusExpanded] = useState(false);

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
      await startSession(worlds[0].id, persona);
    } else {
      await startMultiWorldSession(worlds.map(w => w.id), persona);
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

  // Wave 3 ending-screen rebuild (Readiness §5, the lever all four
  // full-system reviews independently pointed at): fetched once the
  // conversation reaches the closing screen, not before - no need to pay
  // for it on every active turn. Reuses the same per-world JSON files the
  // Facilitator's own sensed-closing resources offer already reads
  // (backend/app/graph/closing_sequence.py) via the new GET /api/resources.
  const [resourcePacks, setResourcePacks] = useState<ResourcePack[]>([]);
  const [copyStatus, setCopyStatus] = useState<'idle' | 'copied' | 'error'>('idle');

  useEffect(() => {
    if (phase !== 'closing') return;
    const ids = worldIds.length > 0 ? worldIds : worldId ? [worldId] : [];
    if (ids.length === 0) return;
    let cancelled = false;
    fetch(`/api/resources?world_ids=${encodeURIComponent(ids.join(','))}`)
      .then((res) => (res.ok ? res.json() : Promise.reject(new Error('non-200'))))
      .then((data: { packs: ResourcePack[] }) => {
        if (!cancelled) setResourcePacks(data.packs || []);
      })
      .catch(() => {
        // The offer/list feature already degrades gracefully when a pack is
        // missing (closing_sequence.py's _load_resources returns None) -
        // an empty list here does the same on the frontend: the further-
        // reading section simply doesn't render, nothing else breaks.
        if (!cancelled) setResourcePacks([]);
      });
    return () => {
      cancelled = true;
    };
  }, [phase, worldIds, worldId]);

  // A plain-text takeaway: speaker names resolved the same way the
  // transcript bubbles resolve them, each assistant turn's cited sources
  // inlined under it - readable pasted into an email or a notes app, not
  // just a JSON dump.
  const buildTranscriptText = () => {
    const displayName = (message: { role: string; name?: string | null }) => {
      if (message.role === 'user') return 'You';
      if (message.name === 'facilitator') return 'Facilitator';
      const world = selectedWorlds.find(
        (w) => w.representative.name.toLowerCase().replace(' ', '_') === message.name
      );
      return world ? world.representative.name : message.name || 'Representative';
    };
    const lines: string[] = [];
    lines.push('Church in Conversation — a conversation transcript');
    lines.push(new Date().toLocaleDateString());
    lines.push('');
    for (const message of messages) {
      lines.push(`${displayName(message)}:`);
      lines.push(message.content);
      if (message.citations && message.citations.length > 0) {
        for (const c of message.citations) {
          lines.push(`  [source: ${c.key_sources}]`);
        }
      }
      lines.push('');
    }
    if (resourcePacks.length > 0) {
      lines.push('Further reading:');
      for (const pack of resourcePacks) {
        for (const r of pack.resources) {
          const bits = [r.title];
          if (r.author) bits.push(`by ${r.author}`);
          lines.push(`- ${bits.join(' ')}`);
        }
      }
      lines.push('');
    }
    return lines.join('\n');
  };

  const handleCopyTranscript = async () => {
    try {
      await navigator.clipboard.writeText(buildTranscriptText());
      setCopyStatus('copied');
    } catch {
      setCopyStatus('error');
    }
    setTimeout(() => setCopyStatus('idle'), 2500);
  };

  if (!isSignedIn) {
    return <SignInScreen />;
  }

  // Reconnecting a session found in sessionStorage (Wave 3, Engineering
  // P1-11) - ahead of onboarding/world-selection so a returning participant
  // never sees either flash before landing back in their live conversation.
  if (isRehydrating) {
    return (
      <div className="table-container">
        <div className="start-screen">
          <div className="loading-indicator loading-indicator--large">
            <div className="loading-dots">
              <span className="loading-dot"></span>
              <span className="loading-dot"></span>
              <span className="loading-dot"></span>
            </div>
            <span>Reconnecting your conversation...</span>
          </div>
        </div>
      </div>
    );
  }

  // Pre-encounter onboarding - gates everything else, shown once per tester
  if (showOnboarding) {
    return (
      <OnboardingScreen
        onContinue={(chosenPersona) => {
          setPersona(chosenPersona);
          setShowOnboarding(false);
        }}
      />
    );
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
        <div className="table-bar__mark">
          <BrandMark size={22} />
        </div>
        <div
          className={`table-bar__status${statusExpanded ? ' table-bar__status--expanded' : ''}`}
          onClick={() => statusMessage && setStatusExpanded((v) => !v)}
        >
          <span className="table-bar__status-full">{statusMessage}</span>
          <span className="table-bar__status-lead">{statusMessage.split(' — ')[0]}</span>
        </div>
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

          <div className="conversation-ended__takeaway">
            <button className="chat-button chat-button--secondary" onClick={handleCopyTranscript}>
              {copyStatus === 'copied' ? 'Copied' : copyStatus === 'error' ? "Couldn't copy — select and copy manually" : 'Copy this conversation'}
            </button>
            <p className="conversation-ended__takeaway-note">
              Copies the transcript with speaker names and cited sources, ready to paste
              into an email or notes.
            </p>
          </div>

          {resourcePacks.some((pack) => pack.resources.length > 0) && (
            <div className="conversation-ended__reading">
              <p className="conversation-ended__reading-heading">Further reading</p>
              {resourcePacks
                .filter((pack) => pack.resources.length > 0)
                .map((pack) => (
                  <div key={pack.world_id} className="conversation-ended__reading-pack">
                    {pack.world_id !== 'general' && (
                      <p className="conversation-ended__reading-label">{pack.world_offer_label}</p>
                    )}
                    <ul>
                      {pack.resources.map((r) => (
                        <li key={r.resource_id}>
                          {r.title}
                          {r.author ? ` — ${r.author}` : ''}
                          {r.note ? <span className="conversation-ended__reading-note"> {r.note}</span> : null}
                        </li>
                      ))}
                    </ul>
                  </div>
                ))}
            </div>
          )}

          <button className="chat-button chat-button--primary" onClick={handleResetConversation}>
            Return to World Selection
          </button>
          <p className="conversation-ended__feedback">
            If you're willing to tell us how this went, we'd genuinely like to know —{' '}
            <a href="https://churchinconversation.com/pilot-feedback.html" target="_blank" rel="noopener noreferrer">
              a few quick questions
            </a>
            {', or reach us directly: '}
            <a href="mailto:info@churchinconversation.com">info@churchinconversation.com</a>
          </p>
          <p className="conversation-ended__feedback">
            One honest ask: please don't post this publicly or forward it widely — we're
            covering the cost of every conversation ourselves, and can't support that yet.
            But if one specific person came to mind — a pastor or teacher, an academic, or
            someone re-examining their faith — we'd welcome that one introduction.
          </p>
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
        worldIds={worldIds.length > 0 ? worldIds : worldId ? [worldId] : []}
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
