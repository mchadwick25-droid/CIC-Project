import { useEffect, useState } from 'react';
import { useConversation } from './hooks/useConversation';
import { findWorld, findWorldByCensusId } from './data/worlds';
import { WorldList } from './screens/WorldList';
import { Doorway } from './screens/Doorway';
import { Conversation } from './screens/Conversation';

type Screen = 'list' | 'doorway' | 'conversation';

// cic-website's own "Launch an Interview with X" links (index.html,
// atlas-v3.html) send ?worlds=<census_id>&mode=interview - a holdover from
// the old cic-poc backend's multi-world sessions. This engine seats one
// world per session (spec O9), so only the first id is honored; the rest
// of the query string (mode=interview) is accepted but unused.
function censusIdFromLocation(): string | null {
  const params = new URLSearchParams(window.location.search);
  const worlds = params.get('worlds');
  return worlds ? worlds.split(',')[0].trim() : null;
}

function App() {
  const conversation = useConversation();
  const [screen, setScreen] = useState<Screen>('list');
  const [selectedWorldKey, setSelectedWorldKey] = useState<string | null>(null);

  // On first mount, resuming a session already open in this tab
  // (sessionStorage) takes priority; only when there's nothing to resume
  // does a ?worlds= deep link from the website get a chance to fire.
  useEffect(() => {
    conversation.rehydrate().then((worldKey) => {
      if (worldKey) {
        setSelectedWorldKey(worldKey);
        setScreen('conversation');
        return;
      }
      const censusId = censusIdFromLocation();
      const deepLinked = censusId ? findWorldByCensusId(censusId) : undefined;
      if (deepLinked) {
        setSelectedWorldKey(deepLinked.worldKey);
        setScreen('doorway');
      }
    });
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleSelectWorld = (worldKey: string) => {
    setSelectedWorldKey(worldKey);
    setScreen('doorway');
  };

  const handleBegin = async () => {
    if (!selectedWorldKey) return;
    const sessionId = await conversation.begin(selectedWorldKey);
    if (sessionId) setScreen('conversation');
  };

  const handleLeave = () => {
    conversation.reset();
    setSelectedWorldKey(null);
    setScreen('list');
  };

  const world = selectedWorldKey ? findWorld(selectedWorldKey) : undefined;

  return (
    <div className="app-shell">
      {screen === 'list' && <WorldList onSelect={handleSelectWorld} />}

      {screen === 'doorway' && world && (
        <Doorway
          world={world}
          onBack={() => setScreen('list')}
          onBegin={handleBegin}
          isLoading={conversation.isLoading}
          error={conversation.error}
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
          onSend={conversation.send}
          onEnd={handleLeave}
          onRestart={handleLeave}
        />
      )}
    </div>
  );
}

export default App;
