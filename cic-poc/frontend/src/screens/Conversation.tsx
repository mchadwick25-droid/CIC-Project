import { Arrival } from '../components/Arrival';
import { BrandMark } from '../components/BrandMark';
import { ChatInput } from '../components/ChatInput';
import { ModernTermMark } from '../components/ModernTermMark';
import { ReadAloudControl } from '../components/ReadAloudControl';
import { ReadAloudDisclosure } from '../components/ReadAloudDisclosure';
import { VoiceTurnBody } from '../components/VoiceTurnBody';
import { useReadAloudAvailability } from '../hooks/useReadAloudAvailability';
import type { ConversationTurn } from '../hooks/useConversation';
import type { WorldEntry, WorldStarter } from '../data/worlds';
import { readAloudEnabled } from '../lib/flags';

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
  errorRecoverable: boolean;
  onSend: (text: string) => void;
  onEnd: () => void;
  onRestart: () => void;
}

function facilitatorParagraphs(text: string): string[] {
  return text.split('\n\n').filter(Boolean);
}

// Read-aloud step 1 always targets the latest completed voice/Facilitator
// turn - never the participant's own typed text (see ReadAloudControl's
// own docstring for why this is one global control, not a per-turn one).
function latestSpokenTurn(turns: ConversationTurn[]): { index: number; turn: ConversationTurn } | null {
  for (let i = turns.length - 1; i >= 0; i--) {
    if (turns[i].speaker !== 'participant') return { index: i, turn: turns[i] };
  }
  return null;
}

export function Conversation({ world, turns, sessionCode, closed, isLoading, error, errorRecoverable, onSend, onEnd, onRestart }: ConversationProps) {
  const latestSpoken = readAloudEnabled ? latestSpokenTurn(turns) : null;
  const readAloudAvailable = useReadAloudAvailability();

  return (
    <div className="conversation">
      <div className="conversation__bar">
        <BrandMark size={16} />
        <div className="conversation__bar-right">
          {sessionCode && (
            <div className="conversation__bar-note sans">
              Not saved to an account — this conversation lives in this tab
            </div>
          )}
          {readAloudAvailable && latestSpoken && (
            <ReadAloudControl text={latestSpoken.turn.text} turnKey={latestSpoken.index} />
          )}
        </div>
      </div>
      {readAloudAvailable && latestSpoken && (
        <ReadAloudDisclosure representativeName={world.representativeName} turnKey={latestSpoken.index} />
      )}

      <div className="conversation__transcript" role="log" aria-label="Conversation">
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
                  <p key={j}>
                    {paragraph}
                    {j === 0 && turn.kind === 'bridge' && turn.modernTerms?.map((card) => <ModernTermMark key={card.record_id} card={card} />)}
                  </p>
                ))}
              </div>
            );
          }
          return (
            <div key={i} className="turn turn--voice">
              <div className="turn__speaker sans" style={{ color: world.accentColor }}>
                <img className="turn__avatar" src={world.portraitImage} alt="" />
                {world.representativeName} · {world.cardName}
              </div>
              <VoiceTurnBody text={turn.text} citations={turn.citations ?? []} figuresUsed={turn.figuresUsed ?? []} glosses={turn.glosses ?? []} transparency={turn.transparency} />
            </div>
          );
        })}
      </div>

      {isLoading && !closed && (
        <p className="waiting-note sans" role="status">
          {world.representativeName} is considering
          <span className="typing-dots" aria-hidden="true">
            <span></span>
            <span></span>
            <span></span>
          </span>
        </p>
      )}
      {error && (
        <div className="conversation__error" role="alert">
          {error}
          {errorRecoverable && (
            <button type="button" className="error-restart sans" onClick={onRestart}>
              Begin again
            </button>
          )}
        </div>
      )}

      {closed ? (
        <div className="conversation__composer">
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
