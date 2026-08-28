import { Arrival } from '../components/Arrival';
import { BrandMark } from '../components/BrandMark';
import { ChatInput } from '../components/ChatInput';
import { VoiceTurnBody } from '../components/VoiceTurnBody';
import type { ConversationTurn } from '../hooks/useConversation';
import type { WorldEntry, WorldStarter } from '../data/worlds';

// Up to 3 starters spanning distinct cell tags (basic/identity, personal,
// critical/etic) rather than the first 3 alphabetically - carried from the
// retired Doorway screen along with the rest of the arrival content: a
// nervous participant benefits more from seeing the range of what's
// askable than from an arbitrary sample.
function sampleStarters(starters: WorldStarter[]): WorldStarter[] {
  const bySuffix = (suffix: string) => starters.find((s) => s.cell.endsWith(suffix));
  const picked = [bySuffix('-I'), bySuffix('-P'), bySuffix('-E')].filter((s): s is WorldStarter => s !== undefined);
  const deduped = picked.filter((s, i) => picked.findIndex((p) => p.cell === s.cell) === i);
  return deduped.length >= 2 ? deduped : starters.slice(0, 3);
}

interface ConversationProps {
  world: WorldEntry;
  turns: ConversationTurn[];
  sessionCode: string | null;
  closed: boolean;
  isLoading: boolean;
  error: string | null;
  onSend: (text: string) => void;
  onEnd: () => void;
  onRestart: () => void;
}

function facilitatorParagraphs(text: string): string[] {
  return text.split('\n\n').filter(Boolean);
}

export function Conversation({ world, turns, sessionCode, closed, isLoading, error, onSend, onEnd, onRestart }: ConversationProps) {
  return (
    <div className="conversation">
      <div className="conversation__bar">
        <BrandMark size={16} />
        {sessionCode && (
          <div className="conversation__bar-note sans">
            Not saved to an account — your session code is <strong>{sessionCode}</strong>
          </div>
        )}
      </div>

      <div className="conversation__transcript">
        <Arrival world={world} />
        {turns.map((turn, i) => {
          if (turn.speaker === 'participant') {
            return (
              <div key={i} className="turn turn--participant">
                <div className="turn__speaker sans">You</div>
                <div className="turn__body">{turn.text}</div>
              </div>
            );
          }
          if (turn.speaker === 'facilitator') {
            return (
              <div key={i} className="turn turn--facilitator">
                {facilitatorParagraphs(turn.text).map((paragraph, j) => (
                  <p key={j}>{paragraph}</p>
                ))}
              </div>
            );
          }
          return (
            <div key={i} className="turn turn--voice">
              <div className="turn__speaker sans" style={{ color: world.accentColor }}>
                {world.representativeName} · {world.cardName}
              </div>
              <VoiceTurnBody text={turn.text} citations={turn.citations ?? []} figuresUsed={turn.figuresUsed ?? []} glosses={turn.glosses ?? []} />
            </div>
          );
        })}
      </div>

      {error && <div className="conversation__error">{error}</div>}

      {closed ? (
        <div className="conversation__composer">
          {sessionCode && (
            <p className="conversation__bar-note sans" style={{ marginBottom: 'var(--spacing-sm)' }}>
              Keep this code to pick the conversation back up on any device: <strong>{sessionCode}</strong>
            </p>
          )}
          <button type="button" className="doorway__begin" onClick={onRestart}>
            Meet another world
          </button>
        </div>
      ) : (
        <>
          {!turns.some((t) => t.speaker === 'participant') && world.starters.length > 0 && (
            <div className="starter-chips">
              <div className="starter-chips__label sans">Questions you might ask</div>
              {sampleStarters(world.starters).map((s) => (
                <button key={s.cell} type="button" className="starter-chip" disabled={isLoading} onClick={() => onSend(s.text)}>
                  {s.text}
                </button>
              ))}
            </div>
          )}
          <ChatInput
            onSend={onSend}
            onEnd={onEnd}
            disabled={isLoading}
            placeholder={`Ask ${world.representativeName} anything…`}
          />
        </>
      )}
    </div>
  );
}
