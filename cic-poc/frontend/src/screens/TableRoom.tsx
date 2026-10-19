/**
 * The Table's conversation room. Same bones as the interview Conversation
 * screen - the differences are exactly the Table's own: seated-voices
 * arrival, per-voice speaker attribution (accent color and name), the
 * round-in-progress state while voices answer in turn, and the sitting's
 * own close (the table session round cap, engine.m4.round.
 * TABLE_SESSION_ROUND_CAP, surfaced from the API rather than a guessed
 * number) rather than an open-ended end.
 *
 * The seated-arrival strip relocates the Doorway's approved disclosure
 * prose the same way the interview Arrival does; the one adaptation is
 * the names sentence pluralized ("These names are ours…"), flagged as an
 * adaptation of approved prose rather than treated as new prose.
 */
import { BrandMark } from '../components/BrandMark';
import { ChatInput } from '../components/ChatInput';
import { DeleteConversation, DeletedNotice } from '../components/DeleteConversation';
import { ExperienceFeedbackButton, ExperienceFeedbackCard } from '../components/ExperienceFeedback';
import { PageFeedback } from '../components/PageFeedback';
import { ModernTermMark } from '../components/ModernTermMark';
import { TurnFeedback } from '../components/TurnFeedback';
import { VoiceTurnBody } from '../components/VoiceTurnBody';
import { useAskedAtRest } from '../hooks/useAskedAtRest';
import type { ConversationTurn } from '../hooks/useConversation';
import type { WorldEntry } from '../data/worlds';
import { pageFeedbackId } from '../lib/api';
import { streamedReply, type StreamedSentence } from '../lib/streamedReply';
import { useState } from 'react';

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
  const [feedbackOpen, setFeedbackOpen] = useState(false);
  const handleDelete = async () => {
    await onDelete?.();
    setDeleted(true);
  };
  const byKey = new Map(seatedWorlds.map((w) => [w.worldKey, w]));
  const streamingSeat = streamed.length ? byKey.get(streamed[0].speaker) : undefined;
  const reply = streamingSeat ? streamedReply(streamed, streamingSeat.worldKey) : null;
  const tablePage = `table:${seatedWorlds.map((w) => w.worldKey).sort().join('+')}`;
  const participantTurns = turns.filter((t) => t.speaker === 'participant').length;
  const lastAsked = turns.map((t) => t.speaker).lastIndexOf('participant');
  const { transcriptRef, askedRef, roomRef } = useAskedAtRest(participantTurns, Boolean(reply));
  const anyLivingTradition = seatedWorlds.some((w) => w.livingTraditionFlag);
  return (
    <div className="conversation">
      <div className="conversation__bar">
        <BrandMark size={16} />
        <div className="conversation__bar-right">
          <ExperienceFeedbackButton open={feedbackOpen} onToggle={() => setFeedbackOpen((o) => !o)} />
          {sessionCode && (
            <div className="conversation__bar-note sans">
              Not saved to an account — this conversation lives in this tab
            </div>
          )}
        </div>
      </div>
      {feedbackOpen && <ExperienceFeedbackCard page={tablePage} onClose={() => setFeedbackOpen(false)} />}

      <div className="conversation__transcript" role="log" aria-label="Conversation" ref={transcriptRef}>
        <div className="arrival arrival--table">
          <div className="arrival__seats">
            {seatedWorlds.map((w) => (
              <div key={w.worldKey} className="arrival__seat">
                <div className="arrival__seat-portrait" style={{ background: w.accentColor }}>
                  <img src={w.portraitImage} alt={w.representativeName} />
                </div>
                <div className="arrival__seat-name">{w.representativeName}</div>
                <div className="arrival__seat-detail sans">{w.roleLabel}</div>
                <div className="arrival__seat-detail sans" style={{ color: w.accentColor }}>
                  {w.cardName} · c. {w.eraStart}–{w.eraEnd}
                </div>
              </div>
            ))}
          </div>
          <details className="arrival__thinness">
            <summary className="arrival__thinness-label sans">What each voice knows well — and doesn't</summary>
            {seatedWorlds.map((w) => (
              <p key={w.worldKey}>
                <strong>{w.representativeName}:</strong> {w.thinnessStatement}
              </p>
            ))}
          </details>
          {anyLivingTradition && (
            <p className="arrival__living-tradition">These are bounded historical reconstructions, not today's churches of the same names.</p>
          )}
          <div className="arrival__disclosure sans">
            <p>
              The system exists to reveal Jesus through the witness of his church across history. Every other outcome
              serves this one. Revealing is witness, never recruitment: each world testifies from its own sources, and
              interpretation remains the participant's own. We believe an honest, transparent telling of the church's
              story will reveal Christ's faithfulness — it is never a pushed objective.
            </p>
            <p>These names are ours; every quote and claim is theirs, and you can check each one.</p>
          </div>
        </div>

        {turns.map((turn, i) => {
          // The seat-identity guard's own exhausted case:
          // engine.api.table_wiring writes this voice_turn with
          // deliberately empty text - "the voice's text is not shown" -
          // and a facilitator_turn (kind: seat_correction) carries the
          // honest line instead. Rendering an empty turn--voice bubble
          // here (portrait, name, nothing underneath) would still be
          // showing that this seat had a turn, just with blank content -
          // not the same as not shown.
          if (turn.speaker !== 'participant' && turn.speaker !== 'facilitator' && !turn.text) {
            return null;
          }
          if (turn.speaker === 'participant') {
            return (
              <div key={i} className="turn turn--participant" ref={i === lastAsked ? askedRef : undefined}>
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
                {turn.note && <p className="turn__note sans">{turn.note}</p>}
              </div>
            );
          }
          const world = byKey.get(turn.speaker);
          return (
            <div key={i} className="turn turn--voice">
              <div className="turn__speaker sans" style={world ? { color: world.accentColor } : undefined}>
                {world ? `${world.representativeName} · ${world.cardName}` : turn.speaker}
              </div>
              <VoiceTurnBody text={turn.text} citations={turn.citations ?? []} figuresUsed={turn.figuresUsed ?? []} glosses={turn.glosses ?? []} transparency={turn.transparency} />
              {sessionId && sessionCode && (
                <TurnFeedback
                  sessionId={sessionId}
                  sessionCode={sessionCode}
                  turnIndex={i}
                  text={turn.text}
                  transparency={turn.transparency}
                  representativeName={world?.representativeName ?? turn.speaker}
                />
              )}
            </div>
          );
        })}

        {reply && streamingSeat && (
          <div className="turn turn--voice">
            <div className="turn__speaker sans" style={{ color: streamingSeat.accentColor }}>
              {`${streamingSeat.representativeName} · ${streamingSeat.cardName}`}
            </div>
            <VoiceTurnBody text={reply.text} citations={[]} transparency={reply.transparency} />
          </div>
        )}

        {isLoading && !closed && !reply && (
          <p className="waiting-note sans" role="status">
            The table is speaking — voices answer in turn
            <span className="typing-dots" aria-hidden="true">
              <span></span>
              <span></span>
              <span></span>
            </span>
          </p>
        )}
        {participantTurns > 0 && <div className="conversation__room" ref={roomRef} aria-hidden="true" />}
      </div>

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
        <DeletedNotice onRestart={onRestart} restartLabel="Return to the worlds" />
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
          onEnd={onEnd}
          disabled={isLoading || roundOpen}
          placeholder={roundOpen ? 'The table is still speaking…' : 'Bring your question to the table…'}
        />
      )}
      {!deleted && turns.some((t) => t.speaker === 'participant') && (
        <PageFeedback page={pageFeedbackId('table', seatedWorlds.map((w) => w.worldKey).sort())} />
      )}
      {!deleted && sessionCode && onDelete && <DeleteConversation onDelete={handleDelete} />}
    </div>
  );
}
