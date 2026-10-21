/**
 * The Table's conversation room. Same bones as the interview Conversation
 * screen - the differences are exactly the Table's own: per-voice speaker
 * attribution (accent color and name), the round-in-progress state while
 * voices answer in turn, and the sitting's own close (the table session round
 * cap, engine.m4.round.TABLE_SESSION_ROUND_CAP, surfaced from the API rather
 * than a guessed number) rather than an open-ended end.
 */
import { ChatInput } from '../components/ChatInput';
import { ConversationCard } from '../components/ConversationCard';
import { ConversationChrome } from '../components/ConversationChrome';
import { DeletedNotice } from '../components/DeleteConversation';
import { Enter } from '../components/Enter';
import { ModernTermMark } from '../components/ModernTermMark';
import { TranscriptScroll } from '../components/TranscriptScroll';
import { TurnFeedback } from '../components/TurnFeedback';
import { VoiceTurnBody } from '../components/VoiceTurnBody';
import { WaitingNote } from '../components/WaitingNote';
import { useReveal, type RevealItem } from '../hooks/useReveal';
import type { ConversationTurn } from '../hooks/useConversation';
import type { WorldEntry } from '../data/worlds';
import { pageFeedbackId } from '../lib/api';
import { streamedReply, type StreamedSentence } from '../lib/streamedReply';
import { useRef, useState } from 'react';

interface TableRoomProps {
  seatedWorlds: WorldEntry[];
  turns: ConversationTurn[];
  streamed?: StreamedSentence[];
  sessionId?: string | null;
  sessionCode: string | null;
  closed: boolean;
  roundOpen: boolean;
  roundCap: number | null;
  isLoading: boolean;
  error: string | null;
  errorRecoverable: boolean;
  onSend: (text: string) => void;
  onResumeRound: () => void;
  onEnd: () => void;
  onRestart: () => void;
  onDelete?: () => Promise<void>;
}

function facilitatorParagraphs(text: string): string[] {
  return text.split('\n\n').filter(Boolean);
}

export function TableRoom({
  seatedWorlds, turns, streamed = [], sessionId = null, sessionCode, closed, roundOpen, roundCap, isLoading, error, errorRecoverable, onSend, onResumeRound, onEnd, onRestart, onDelete,
}: TableRoomProps) {
  const [deleted, setDeleted] = useState(false);
  const handleDelete = async () => {
    await onDelete?.();
    setDeleted(true);
  };
  const byKey = new Map(seatedWorlds.map((w) => [w.worldKey, w]));
  const streamingSeat = streamed.length ? byKey.get(streamed[0].speaker) : undefined;
  const reply = streamingSeat ? streamedReply(streamed, streamingSeat.worldKey) : null;
  const tablePage = `table:${seatedWorlds.map((w) => w.worldKey).sort().join('+')}`;
  const participantTurns = turns.filter((t) => t.speaker === 'participant').length;
  const started = participantTurns > 0;
  const firstAsked = turns.findIndex((t) => t.speaker === 'participant');
  const initialTurns = useRef(turns.length).current;
  // Replies already on screen as they streamed, so the finished turn takes their place without opening again.
  const shown = useRef(new Set<string>());
  const anyLivingTradition = seatedWorlds.some((w) => w.livingTraditionFlag);

  const items: RevealItem[] = turns.flatMap((turn, i) =>
    turn.speaker === 'participant' || turn.speaker === 'facilitator' || !turn.text ? [] : [{ key: `v${i}`, speaker: turn.speaker, text: turn.text, complete: true }]
  );
  if (reply && streamingSeat) items.push({ key: `v${turns.length}`, speaker: streamingSeat.worldKey, text: reply.text, complete: false });
  const reveal = useReveal(items);
  const waiting = (isLoading || reveal.busy) && !closed && !reveal.showing;
  const streamingNow = reply !== null && streamingSeat !== undefined && reveal.reveal(`v${turns.length}`) !== null;
  if (streamingNow) shown.current.add(`v${turns.length}`);

  return (
    <div className="conversation">
      <ConversationChrome
        title="The Table"
        aboutLabel="About the table"
        about={
          <>
            <div className="arrival arrival--table">
              <div className="arrival__seats">
                {seatedWorlds.map((w) => (
                  <div key={w.worldKey} className="arrival__seat">
                    <div className="arrival__seat-portrait" style={{ background: w.accentColor }}>
                      <img src={w.portraitImage} alt={w.representativeName} />
                    </div>
                    <div className="arrival__seat-name">{w.representativeName}</div>
                    <div className="arrival__seat-detail sans" style={{ color: w.accentColor }}>
                      {w.cardName} · c. {w.eraStart}–{w.eraEnd}
                    </div>
                  </div>
                ))}
              </div>
              {anyLivingTradition && (
                <p className="arrival__living-tradition">These are bounded historical reconstructions, not today's churches of the same names.</p>
              )}
            </div>
            {sessionCode && <div className="conversation__bar-note sans">Not saved to an account — this conversation lives in this tab</div>}
          </>
        }
        feedbackPage={tablePage}
        reportPage={started ? pageFeedbackId('table', seatedWorlds.map((w) => w.worldKey).sort()) : null}
        onLeave={onEnd}
        onDelete={sessionCode && onDelete && !deleted ? handleDelete : undefined}
      />

      <div className="conv-cards">
        {seatedWorlds.map((w) => (
          <ConversationCard key={w.worldKey} world={w} speaking={reveal.showing && reveal.speaking === w.worldKey} />
        ))}
      </div>

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
          // The seat-identity guard's own exhausted case: engine.api.table_wiring
          // writes this voice_turn with deliberately empty text - "the voice's text
          // is not shown" - and a facilitator_turn (kind: seat_correction) carries
          // the honest line instead, so no blank bubble stands in for it.
          if (!turn.text) return null;
          const revealed = reveal.reveal(`v${i}`);
          if (!revealed) return null;
          const world = byKey.get(turn.speaker);
          return (
            <Enter key={i} still={still || shown.current.has(`v${i}`)}>
              <div className="turn turn--voice">
                <div className="turn__speaker sans" style={world ? { color: world.accentColor } : undefined}>
                  {world ? `${world.representativeName} · ${world.cardName}` : turn.speaker}
                </div>
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
                      representativeName={world?.representativeName ?? turn.speaker}
                    />
                  </Enter>
                )}
              </div>
            </Enter>
          );
        })}
        {streamingNow && streamingSeat && (
          <Enter>
            <div className="turn turn--voice">
              <div className="turn__speaker sans" style={{ color: streamingSeat.accentColor }}>
                {`${streamingSeat.representativeName} · ${streamingSeat.cardName}`}
              </div>
              <div className="turn__body">
                <div>{reveal.reveal(`v${turns.length}`)?.text}</div>
              </div>
            </div>
          </Enter>
        )}
        <WaitingNote show={waiting} label="The table is considering" />
      </TranscriptScroll>

      {error && (
        <div className="conversation__error" role="alert">
          {error}
          {errorRecoverable && (
            <button type="button" className="error-restart sans" onClick={onRestart}>
              Begin again
            </button>
          )}
          {!errorRecoverable && roundOpen && !isLoading && (
            <button type="button" className="error-restart sans" onClick={onResumeRound}>
              Let the table finish its round
            </button>
          )}
        </div>
      )}

      {deleted ? (
        <DeletedNotice onRestart={onRestart} restartLabel="Return to the traditions" />
      ) : closed ? (
        <div className="conversation__composer">
          <p className="conversation__bar-note sans" style={{ marginBottom: 'var(--spacing-sm)' }}>
            {roundCap != null
              ? `The sitting has ended — a Table holds ${roundCap} rounds, and this one is complete.`
              : 'The sitting has ended — this one is complete.'}
          </p>
          <button type="button" className="doorway__begin" onClick={onRestart}>
            Return to the worlds
          </button>
        </div>
      ) : (
        <ChatInput
          onSend={onSend}
          turns={turns}
          disabled={isLoading || roundOpen || reveal.busy}
          placeholder={roundOpen || reveal.busy ? 'The table is still speaking…' : 'Ask the table…'}
        />
      )}
    </div>
  );
}
