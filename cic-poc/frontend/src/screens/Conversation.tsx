import { Arrival } from '../components/Arrival';
import { ChatInput } from '../components/ChatInput';
import { ConversationCard } from '../components/ConversationCard';
import { ConversationChrome } from '../components/ConversationChrome';
import { DeletedNotice } from '../components/DeleteConversation';
import { Enter } from '../components/Enter';
import { ModernTermMark } from '../components/ModernTermMark';
import { ResourcesFirst } from '../components/ResourcesFirst';
import { TranscriptScroll } from '../components/TranscriptScroll';
import { TurnFeedback } from '../components/TurnFeedback';
import { VoiceTurnBody } from '../components/VoiceTurnBody';
import { WaitingNote } from '../components/WaitingNote';
import { useReveal, type RevealItem } from '../hooks/useReveal';
import type { ConversationTurn } from '../hooks/useConversation';
import { accountsEnabled, useAccount } from '../lib/accounts';
import { accountsCopy } from '../lib/accountsCopy';
import { pageFeedbackId } from '../lib/api';
import { streamedReply, type StreamedSentence } from '../lib/streamedReply';
import type { WorldEntry } from '../data/worlds';
import { useRef, useState } from 'react';

interface ConversationProps {
  world: WorldEntry;
  turns: ConversationTurn[];
  // The reply so far while the voice is still writing it; empty otherwise.
  streamed?: StreamedSentence[];
  sessionId?: string | null;
  sessionCode: string | null;
  closed: boolean;
  isLoading: boolean;
  error: string | null;
  errorRecoverable: boolean;
  onSend: (text: string) => void;
  onEnd: () => void;
  onRestart: () => void;
  onDelete?: () => Promise<void>;
  // A question brought in from the site, waiting in the box until sent.
  carriedQuestion?: string;
}

function facilitatorParagraphs(text: string): string[] {
  return text.split('\n\n').filter(Boolean);
}

export function Conversation({ world, turns, streamed = [], sessionId = null, sessionCode, closed, isLoading, error, errorRecoverable, onSend, onEnd, onRestart, onDelete, carriedQuestion = '' }: ConversationProps) {
  const [deleted, setDeleted] = useState(false);
  const handleDelete = async () => {
    await onDelete?.();
    setDeleted(true);
  };
  const participantTurns = turns.filter((t) => t.speaker === 'participant').length;
  const started = participantTurns > 0;
  const firstAsked = turns.findIndex((t) => t.speaker === 'participant');
  const reply = streamedReply(streamed, world.worldKey);
  const initialTurns = useRef(turns.length).current;
  // Replies already on screen as they streamed, so the finished turn takes their place without opening again.
  const shown = useRef(new Set<string>());
  // Loading also covers the room opening; only a sent question awaits a reply.
  const awaitingReply = isLoading && turns.length > 0 && turns[turns.length - 1].speaker === 'participant';

  const items: RevealItem[] = turns.flatMap((turn, i) =>
    turn.speaker === 'participant' || turn.speaker === 'facilitator' ? [] : [{ key: `v${i}`, speaker: world.worldKey, text: turn.text, complete: true }]
  );
  if (reply) items.push({ key: `v${turns.length}`, speaker: world.worldKey, text: reply.text, complete: false });
  const reveal = useReveal(items);
  const waiting = (awaitingReply || reveal.busy) && !closed && !reveal.showing;
  const streamingNow = reply !== null && reveal.reveal(`v${turns.length}`) !== null;
  if (streamingNow) shown.current.add(`v${turns.length}`);

  const voiceHeader = (
    <div className="turn__speaker sans" style={{ color: world.accentColor }}>
      <img className="turn__avatar" src={world.portraitImage} alt="" />
      {world.representativeName} · {world.cardName}
    </div>
  );

  return (
    <div className="conversation">
      <ConversationChrome
        title="Church in Conversation"
        aboutLabel={`About ${world.representativeName}`}
        about={
          <>
            <Arrival world={world} />
            {sessionCode && <NotSavedNote />}
          </>
        }
        feedbackPage={world.worldKey}
        reportPage={started ? pageFeedbackId('conversation', [world.worldKey]) : null}
        onLeave={onEnd}
        onDelete={started && sessionCode && onDelete && !deleted ? handleDelete : undefined}
      />

      <div className="conv-cards">
        <ConversationCard world={world} speaking={(awaitingReply && !closed) || reveal.busy} />
      </div>

      <ResourcesFirst turns={turns} />
      <TranscriptScroll label="Conversation" followSignal={participantTurns}>
        {turns.map((turn, i) => {
          const still = i < initialTurns;
          if (turn.speaker === 'participant') {
            return (
              <Enter key={i} still={still}>
                <div className="turn turn--participant">
                  <div className="turn__speaker sans">You</div>
                  <div className="turn__body">{turn.text}</div>
                </div>
              </Enter>
            );
          }
          if (turn.speaker === 'facilitator') {
            const welcome = firstAsked < 0 || i < firstAsked;
            return (
              <Enter key={i} still={still} shown={!welcome || !started}>
                <div className={welcome ? 'turn turn--facilitator turn--welcome' : 'turn turn--facilitator'}>
                  {facilitatorParagraphs(turn.text).map((paragraph, j) => (
                    <p key={j}>
                      {paragraph}
                      {!welcome && j === 0 && turn.kind === 'bridge' && turn.modernTerms?.map((card) => <ModernTermMark key={card.record_id} card={card} />)}
                    </p>
                  ))}
                  {!welcome && turn.note && <p className="turn__note sans">{turn.note}</p>}
                </div>
              </Enter>
            );
          }
          const revealed = reveal.reveal(`v${i}`);
          if (!revealed) return null;
          return (
            <Enter key={i} still={still || shown.current.has(`v${i}`)}>
              <div className="turn turn--voice">
                {voiceHeader}
                {revealed.revealing ? (
                  <div className="turn__body">
                    <div>{revealed.text}</div>
                  </div>
                ) : (
                  <VoiceTurnBody text={turn.text} citations={turn.citations ?? []} figuresUsed={turn.figuresUsed ?? []} glosses={turn.glosses ?? []} transparency={turn.transparency} />
                )}
                {!revealed.revealing && sessionId && sessionCode && (
                  <Enter still={still} flush>
                    <TurnFeedback
                      sessionId={sessionId}
                      sessionCode={sessionCode}
                      turnIndex={i}
                      text={turn.text}
                      transparency={turn.transparency}
                      representativeName={world.representativeName}
                    />
                  </Enter>
                )}
              </div>
            </Enter>
          );
        })}
        {streamingNow && (
          <Enter>
            <div className="turn turn--voice">
              {voiceHeader}
              <div className="turn__body">
                <div>{reveal.reveal(`v${turns.length}`)?.text}</div>
              </div>
            </div>
          </Enter>
        )}
        <WaitingNote show={waiting} label={`${world.representativeName} is considering`} />
      </TranscriptScroll>

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

      {deleted ? (
        <DeletedNotice onRestart={onRestart} restartLabel="Meet another tradition" />
      ) : closed ? (
        <div className="conversation__composer">
          <button type="button" className="doorway__begin" onClick={onRestart}>
            Meet another world
          </button>
        </div>
      ) : (
        <ChatInput
          onSend={onSend}
          turns={turns}
          disabled={isLoading || reveal.busy}
          sending={awaitingReply}
          placeholder={`Ask ${world.representativeName}…`}
          initialMessage={started ? '' : carriedQuestion}
        />
      )}
      {!deleted && <p className="conversation__ai-line sans">This is an AI-generated voice.</p>}
    </div>
  );
}

function NotSavedNote() {
  const account = useAccount();
  if (accountsEnabled && account.status === 'in' && account.lastShelved === true) return null;
  if (accountsEnabled && account.status === 'in') {
    return <div className="conversation__bar-note sans">{accountsCopy.notShelvedNote}</div>;
  }
  return <div className="conversation__bar-note sans">Not saved to an account — this conversation lives in this tab</div>;
}
