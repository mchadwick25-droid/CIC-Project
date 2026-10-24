import { useEffect, useRef, useState } from 'react';
import { GiftNotice } from './components/GiftNotice';
import { AccountHome } from './components/AccountHome';
import { useConversation } from './hooks/useConversation';
import { useVisibleHeight } from './hooks/useVisibleHeight';
import { useTable } from './hooks/useTable';
import { useWorlds } from './hooks/useWorlds';
import { findWorld, findWorldByCensusId } from './data/worlds';
import { deleteSession } from './lib/api';
import { readStored } from './lib/sessionStore';
import { Launch } from './screens/Launch';
import { Conversation } from './screens/Conversation';
import { TableRoom } from './screens/TableRoom';

type Screen = 'arriving' | 'launch' | 'conversation' | 'table';

// Safe cross-origin (a reference comparison, never a property read) - the
// standard "am I inside an iframe" check. cic-website/talk.html embeds
// this app in a themed <iframe>; without this check, "Leave for now"
// would fall back to this app's own pre-redesign Launch screen, which
// reads as "the site broke and reverted to the old design" when rendered
// inside a themed iframe dressed up to look like part of the new site.
const isEmbedded = typeof window !== 'undefined' && window.self !== window.top;
// The site page around the frame already carries the wordmark and its own
// "Tell us what you think"; the app's first-screen bar drops its copies.
if (isEmbedded) document.documentElement.classList.add('is-framed');

// A question carried in from the site - a tradition page's question link, or
// the home page's held question - arrives as #q=. It waits in the message box;
// the participant sends it.
function readCarriedQuestion(): string {
  const hash = window.location.hash;
  if (!hash.startsWith('#q=')) return '';
  try {
    return decodeURIComponent(hash.slice(3)).trim().slice(0, 280);
  } catch {
    return '';
  }
}

/**
 * The deep-link grammar - the ONE contract between the discovery surfaces
 * (cic-website's world cards, the Atlas) and this app:
 *
 *   ?worlds=<id>&mode=interview      -> straight into the conversation, no
 *                                       waiting place (arrival happens
 *                                       inside the room)
 *   ?worlds=a,b[,c]&mode=table       -> straight into the table
 *                                       conversation, same as interview -
 *                                       2 or 3 named seats is enough to
 *                                       convene on arrival: a Table with
 *                                       that many seats goes straight into
 *                                       the conversation rather than
 *                                       waiting to be convened
 *   ?worlds=<one id>&mode=table,       -> too few seats to convene - the
 *   ?mode=table                          launch screen's Table field, with
 *                                        that one seat (or none) chosen
 *   /                                 -> the launch screen (the world cards)
 *
 * Interview mode with several ids honors the first (one voice per
 * interview, spec O9). Ids are census_ids - the same ids worlds.yaml and
 * world-census.json share, which is what lets a link land somewhere real.
 */
function parseDeepLink(): { censusIds: string[]; mode: string } {
  const params = new URLSearchParams(window.location.search);
  const worlds = params.get('worlds');
  return {
    censusIds: worlds ? worlds.split(',').map((s) => s.trim()).filter(Boolean) : [],
    mode: params.get('mode') ?? 'interview',
  };
}

/** A used deep link is consumed - a reload after it fires should rehydrate
 * the session it started (or land on launch), not fire it again. */
function consumeDeepLink() {
  if (window.location.search) window.history.replaceState({}, '', window.location.pathname);
}

/** Whether this load is headed for a room rather than the launch screen:
 * a deep link, or a session already open in this tab. The first screen
 * can't be decided until the world list loads, so such a load holds on
 * 'arriving' until it can - starting on 'launch' put the world cards up
 * for that whole wait, then swapped them out. */
function expectsRoom(): boolean {
  const params = new URLSearchParams(window.location.search);
  return params.has('worlds') || params.has('mode') || readStored() !== null;
}

/** Order-insensitive set equality for comparing a Table deep link's seats
 * against what's stored - reseating the same participants isn't a new
 * request, but a different lineup is. */
function sameSeats(a: string[], b: string[]): boolean {
  if (a.length !== b.length) return false;
  const sortedA = [...a].sort();
  const sortedB = [...b].sort();
  return sortedA.every((key, i) => key === sortedB[i]);
}

function App() {
  const conversation = useConversation();
  useVisibleHeight();
  const table = useTable();
  const { worlds, isLoading: worldsLoading, error: worldsError } = useWorlds();
  const [screen, setScreen] = useState<Screen>(() => (expectsRoom() ? 'arriving' : 'launch'));
  const [carriedQuestion] = useState(readCarriedQuestion);
  // Read once; a reload should not put the question back in the box.
  useEffect(() => {
    if (window.location.hash.startsWith('#q=')) {
      window.history.replaceState(window.history.state, '', window.location.pathname + window.location.search);
    }
  }, []);
  const [selectedWorldKey, setSelectedWorldKey] = useState<string | null>(null);
  const [seated, setSeated] = useState<string[]>([]);
  const [tableFocus, setTableFocus] = useState(false);
  // A deep link naming no known world used to fail in silence (and left
  // the stale query to re-fail on reload) - now it says so, once.
  const [launchNotice, setLaunchNotice] = useState<string | null>(null);
  const deepLinkFired = useRef(false);

  // Waits for the world list before deciding the first screen - a ?worlds=
  // deep link can't be matched against an empty list. Resuming a session
  // already open in this tab takes priority (interview or table, decided
  // by the stored mode) UNLESS the incoming URL explicitly asks for the
  // OTHER mode - a fresh, different request always wins over a stale
  // leftover session (see the conflict check just inside the effect).
  // Only when there's nothing to resume, or nothing to conflict with,
  // does the deep link get its one chance to fire.
  useEffect(() => {
    if (worldsLoading || deepLinkFired.current) return;
    deepLinkFired.current = true;
    const stored = readStored();
    const deepLink = parseDeepLink();
    const linked = deepLink.censusIds
      .map((id) => findWorldByCensusId(worlds, id))
      .filter((w): w is NonNullable<typeof w> => w !== undefined)
      .map((w) => w.worldKey);
    // A fresh deep link explicitly asking for a DIFFERENT mode than
    // whatever's left over in this tab's storage is the participant
    // choosing to start something new. Without this check: an earlier
    // interview left mode:'interview' in storage, and a subsequent Table
    // deep link - a genuinely different request - never got its one
    // chance to fire, because resuming the stale interview always ran
    // first and always succeeded, since that old session was still open
    // server-side; parseDeepLink was only ever reached once resume came
    // back empty. Only resume when the incoming request agrees with (or
    // says nothing explicit about) what is stored - a bare reload of an
    // already-open room still carries no conflicting params and resumes
    // exactly as before.
    const hasExplicitDeepLink = deepLink.censusIds.length > 0 || new URLSearchParams(window.location.search).has('mode');
    const storedModeConflicts = hasExplicitDeepLink && stored !== null && deepLink.mode !== stored.mode;
    // A SAME-mode deep link naming a different world (interview) or a
    // different lineup (table) than what's stored is just as much a fresh
    // request as a mode switch - the check above only ever looked at mode.
    // Without this check: back out of an interview with one voice, click a
    // different voice - both land on mode: 'interview', so nothing noticed
    // the world itself had changed, and the OLD interview resumed instead
    // of the newly-picked one starting.
    const storedWorldConflicts =
      !storedModeConflicts &&
      hasExplicitDeepLink &&
      stored !== null &&
      deepLink.mode === stored.mode &&
      linked.length > 0 &&
      (stored.mode === 'table' ? !sameSeats(linked.slice(0, 3), stored.worldKeys ?? []) : linked[0] !== stored.worldKey);
    const resume = storedModeConflicts || storedWorldConflicts
      ? Promise.resolve(null)
      : stored?.mode === 'table'
        ? table.rehydrate().then((keys) => (keys ? 'table' : null))
        : conversation.rehydrate().then((key) => (key ? 'interview' : null));
    resume.then((resumed) => {
      if (resumed === 'table') {
        setScreen('table');
        return;
      }
      if (resumed === 'interview') {
        const stored2 = readStored();
        if (stored2?.worldKey) setSelectedWorldKey(stored2.worldKey);
        setScreen('conversation');
        return;
      }
      const { censusIds, mode } = deepLink;
      if (mode === 'table') {
        const uniqueLinked = [...new Set(linked)].slice(0, 3);
        if (uniqueLinked.length >= 2) {
          // Auto-convene, same as interview's frictionless arrival.
          // Optimistic, mirroring beginInterview two lines below exactly:
          // setScreen('table') fires before convene()'s round trip even
          // starts, not inside its .then() - setting it only on success
          // leaves the full Launch screen (hero, every world card)
          // rendered and sitting there for the round trip, then swapped
          // out, a visible flash. TableRoom already renders sensibly on
          // table.isLoading with seatedWorlds falling back to `seated`
          // before table.worldKeys exists, same as Conversation does
          // mid-beginInterview. Reverting to 'launch' below is still the
          // failure path if convene() itself comes back empty.
          consumeDeepLink();
          setSeated(uniqueLinked);
          setScreen('table');
          table.convene(uniqueLinked).then((sessionId) => {
            if (!sessionId) {
              setScreen('launch');
              setTableFocus(true);
            }
          });
          return;
        }
        // Too few named seats to convene - land on the Table field with
        // what we have (0 or 1 seat), awaiting the rest.
        setSeated(uniqueLinked);
        setTableFocus(true);
        consumeDeepLink();
        setScreen('launch');
        return;
      }
      if (linked.length > 0) {
        // Straight into the room - the interview is the frictionless door.
        consumeDeepLink();
        beginInterview(linked[0]);
        return;
      }
      if (censusIds.length > 0) {
        consumeDeepLink();
        setLaunchNotice("We couldn't find that Christian tradition here — choose from the cards below.");
      }
      setScreen('launch');
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [worldsLoading]);

  const beginInterview = (worldKey: string) => {
    setSelectedWorldKey(worldKey);
    setScreen('conversation');
    conversation.begin(worldKey).then((sessionId) => {
      if (!sessionId) setScreen('launch');
    });
  };

  const toggleSeat = (worldKey: string) => {
    setSeated((prev) => (prev.includes(worldKey) ? prev.filter((k) => k !== worldKey) : prev.length >= 3 ? prev : [...prev, worldKey]));
  };

  const convene = () => {
    table.convene(seated).then((sessionId) => {
      if (sessionId) setScreen('table');
    });
  };

  const handleLeave = () => {
    conversation.reset();
    table.reset();
    setSelectedWorldKey(null);
    setSeated([]);
    setTableFocus(false);
    setLaunchNotice(null);
    if (isEmbedded) {
      // Tell the parent page to navigate itself, rather than falling back
      // to this app's own Launch screen inside the iframe (see isEmbedded's
      // own comment). talk.html owns where "leave" actually goes - its own
      // #back-link, already real and already styled - this app has no
      // business re-deciding that destination.
      window.parent.postMessage({ type: 'cic:leave' }, '*');
      return;
    }
    setScreen('launch');
  };

  // Once a conversation has started, the site page around the frame hides
  // its own bars, so only the portrait and names sit above the transcript.
  const conversationStarted = screen === 'conversation' && conversation.turns.some((t) => t.speaker === 'participant');
  useEffect(() => {
    if (isEmbedded) window.parent.postMessage({ type: 'cic:started', started: conversationStarted }, '*');
  }, [conversationStarted]);

  const world = selectedWorldKey ? findWorld(worlds, selectedWorldKey) : undefined;
  const seatedWorlds = (screen === 'table' && table.worldKeys.length > 0 ? table.worldKeys : seated)
    .map((k) => findWorld(worlds, k))
    .filter((w): w is NonNullable<typeof w> => w !== undefined);

  return (
    <div className="app-shell">
      <AccountHome />
      <GiftNotice />
      {screen === 'arriving' && (
        <p className="arriving-hold" role="status">
          <span className="visually-hidden">Opening the conversation</span>
          <span className="typing-dots" aria-hidden="true">
            <span></span>
            <span></span>
            <span></span>
          </span>
        </p>
      )}

      {screen === 'launch' && (
        <Launch
          worlds={worlds}
          isLoading={worldsLoading}
          error={worldsError ?? conversation.error ?? launchNotice}
          seated={seated}
          tableFocus={tableFocus}
          convening={table.isLoading}
          tableError={table.error}
          onBeginInterview={beginInterview}
          onToggleSeat={toggleSeat}
          onSeatPairing={(keys) => {
            setSeated(keys.slice(0, 3));
            setTableFocus(true);
          }}
          onConvene={convene}
        />
      )}

      {screen === 'conversation' && world && (
        <Conversation
          world={world}
          turns={conversation.turns}
          streamed={conversation.streamed}
          sessionId={conversation.sessionId}
          sessionCode={conversation.sessionCode}
          closed={conversation.closed}
          isLoading={conversation.isLoading}
          error={conversation.error}
          errorRecoverable={conversation.errorRecoverable}
          onSend={conversation.send}
          carriedQuestion={carriedQuestion}
          onEnd={handleLeave}
          onRestart={handleLeave}
          onDelete={async () => {
            if (!conversation.sessionId || !conversation.sessionCode) return;
            await deleteSession(conversation.sessionId, conversation.sessionCode);
            conversation.reset();
          }}
        />
      )}

      {screen === 'table' && seatedWorlds.length > 0 && (
        <TableRoom
          seatedWorlds={seatedWorlds}
          turns={table.turns}
          streamed={table.streamed}
          sessionId={table.sessionId}
          sessionCode={table.sessionCode}
          closed={table.closed}
          roundOpen={table.roundOpen}
          roundCap={table.roundCap}
          isLoading={table.isLoading}
          error={table.error}
          errorRecoverable={table.errorRecoverable}
          onSend={table.send}
          onResumeRound={table.resumeRound}
          onEnd={handleLeave}
          onRestart={handleLeave}
          onDelete={async () => {
            if (!table.sessionId || !table.sessionCode) return;
            await deleteSession(table.sessionId, table.sessionCode);
            table.reset();
          }}
        />
      )}
    </div>
  );
}

export default App;
