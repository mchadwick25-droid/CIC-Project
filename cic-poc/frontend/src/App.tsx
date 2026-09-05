import { useEffect, useRef, useState } from 'react';
import { useConversation } from './hooks/useConversation';
import { useTable } from './hooks/useTable';
import { useWorlds } from './hooks/useWorlds';
import { findWorld, findWorldByCensusId } from './data/worlds';
import { readStored } from './lib/sessionStore';
import { Launch } from './screens/Launch';
import { Conversation } from './screens/Conversation';
import { TableRoom } from './screens/TableRoom';

type Screen = 'launch' | 'conversation' | 'table';

// Safe cross-origin (a reference comparison, never a property read) - the
// standard "am I inside an iframe" check. Real today: cic-website/talk.html
// embeds this app in a themed <iframe>, and this app had zero awareness of
// that (2026-09-04 live bug, Mark hit it directly) - "Leave for now" fell
// back to this app's own pre-redesign Launch screen, which used to just
// read as the app's own homepage when reached in its own tab, but reads as
// "the site broke and reverted to the old design" rendered inside a themed
// iframe dressed up to look like part of the new site.
const isEmbedded = typeof window !== 'undefined' && window.self !== window.top;

/**
 * The deep-link grammar - the ONE contract between the discovery surfaces
 * (cic-website's world cards, the Atlas) and this app (Mark's launch
 * ruling, 2026-08-28):
 *
 *   ?worlds=<id>&mode=interview   -> straight into the conversation, no
 *                                    waiting place (arrival happens inside
 *                                    the room)
 *   ?worlds=a,b[,c]&mode=table    -> the launch screen's Table field with
 *                                    those seats chosen - a Table is
 *                                    CONVENED, never auto-started
 *   ?mode=table                   -> the Table field, empty
 *   /                             -> the launch screen (the world cards)
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

function App() {
  const conversation = useConversation();
  const table = useTable();
  const { worlds, isLoading: worldsLoading, error: worldsError } = useWorlds();
  const [screen, setScreen] = useState<Screen>('launch');
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
    // A fresh deep link explicitly asking for a DIFFERENT mode than
    // whatever's left over in this tab's storage is the participant
    // choosing to start something new (2026-09-05 live bug, Mark hit it
    // directly: an earlier interview left mode:'interview' in storage,
    // and a subsequent Table deep link - a genuinely different request -
    // never got its one chance to fire, because resuming the stale
    // interview always ran first and always succeeded, since that old
    // session was still open server-side; parseDeepLink was only ever
    // reached once resume came back empty). Only resume when the
    // incoming request agrees with (or says nothing explicit about) what
    // is stored - a bare reload of an already-open room still carries no
    // conflicting params and resumes exactly as before.
    const hasExplicitDeepLink = deepLink.censusIds.length > 0 || new URLSearchParams(window.location.search).has('mode');
    const storedModeConflicts = hasExplicitDeepLink && stored !== null && deepLink.mode !== stored.mode;
    const resume = storedModeConflicts
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
      const linked = censusIds
        .map((id) => findWorldByCensusId(worlds, id))
        .filter((w): w is NonNullable<typeof w> => w !== undefined)
        .map((w) => w.worldKey);
      if (mode === 'table') {
        // Intentional by design: the link chooses seats, the participant
        // convenes. Never auto-creates a session.
        setSeated([...new Set(linked)].slice(0, 3));
        setTableFocus(true);
        consumeDeepLink();
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
        setLaunchNotice("We couldn't find that world here — choose from the cards below.");
      }
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

  const world = selectedWorldKey ? findWorld(worlds, selectedWorldKey) : undefined;
  const seatedWorlds = (screen === 'table' && table.worldKeys.length > 0 ? table.worldKeys : seated)
    .map((k) => findWorld(worlds, k))
    .filter((w): w is NonNullable<typeof w> => w !== undefined);

  return (
    <div className="app-shell">
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
          sessionCode={conversation.sessionCode}
          closed={conversation.closed}
          isLoading={conversation.isLoading}
          error={conversation.error}
          errorRecoverable={conversation.errorRecoverable}
          onSend={conversation.send}
          onEnd={handleLeave}
          onRestart={handleLeave}
        />
      )}

      {screen === 'table' && seatedWorlds.length > 0 && (
        <TableRoom
          seatedWorlds={seatedWorlds}
          turns={table.turns}
          sessionCode={table.sessionCode}
          closed={table.closed}
          roundOpen={table.roundOpen}
          isLoading={table.isLoading}
          error={table.error}
          errorRecoverable={table.errorRecoverable}
          onSend={table.send}
          onResumeRound={table.resumeRound}
          onEnd={handleLeave}
          onRestart={handleLeave}
        />
      )}
    </div>
  );
}

export default App;
