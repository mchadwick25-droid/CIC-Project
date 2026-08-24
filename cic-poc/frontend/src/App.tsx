import { useEffect, useState } from 'react';
import { useConversation } from './hooks/useConversation';
import { findWorld } from './data/worlds';
import { WorldList } from './screens/WorldList';
import { Doorway } from './screens/Doorway';
import { Conversation } from './screens/Conversation';

type Screen = 'list' | 'doorway' | 'conversation';

function App() {
  const conversation = useConversation();
  const [screen, setScreen] = useState<Screen>('list');
  const [selectedWorldKey, setSelectedWorldKey] = useState<string | null>(null);

  // On first mount, try to resume a session already open in this tab
  // (sessionStorage) before showing the world list.
  useEffect(() => {
    conversation.rehydrate().then((worldKey) => {
      if (worldKey) {
        setSelectedWorldKey(worldKey);
        setScreen('conversation');
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
