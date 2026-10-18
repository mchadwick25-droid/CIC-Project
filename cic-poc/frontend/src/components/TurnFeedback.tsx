import { useState, type FormEvent } from 'react';
import { sendTurnFeedback, type FlagReason } from '../lib/api';
import type { TransparencyPlan } from '../types/conversation';
import { FEEDBACK_FAILED, FEEDBACK_SAFETY_LINE } from './feedbackText';

interface TurnFeedbackProps {
  sessionId: string;
  sessionCode: string;
  turnIndex: number;
  text: string;
  transparency?: TransparencyPlan;
  representativeName: string;
}

const REASONS: { value: FlagReason; label: string }[] = [
  { value: 'fact_wrong', label: 'I think this fact is wrong' },
  { value: 'source_mismatch', label: 'The source shown does not say this' },
  { value: 'overcertain', label: 'It sounds more certain than it should' },
  { value: 'unclear', label: 'This is not clear' },
];

interface SentenceChoice {
  index: number | null;
  label: string;
}

// One choice per sentence the turn's plan marks out, or the whole reply when
// the stored turn carries no sentence spans.
function sentenceChoices(text: string, transparency?: TransparencyPlan): SentenceChoice[] {
  const choices: SentenceChoice[] = [];
  for (const s of transparency?.sentences ?? []) {
    if (s.text_start === null || s.text_end === null) continue;
    const label = text.slice(s.text_start, s.text_end).trim();
    if (label) choices.push({ index: s.index, label });
  }
  return choices.length > 0 ? choices : [{ index: null, label: 'The whole reply' }];
}

function HeartIcon({ filled }: { filled: boolean }) {
  return (
    <svg className="turn-feedback__heart" width="13" height="13" viewBox="0 0 24 24" aria-hidden="true" focusable="false">
      <path
        d="M12 20.5 4.2 12.9a4.7 4.7 0 0 1 0-6.7 4.8 4.8 0 0 1 6.8 0l1 1 1-1a4.8 4.8 0 0 1 6.8 0 4.7 4.7 0 0 1 0 6.7L12 20.5Z"
        fill={filled ? 'currentColor' : 'none'}
        stroke="currentColor"
        strokeWidth="2"
        strokeLinejoin="round"
      />
    </svg>
  );
}

// The quiet line under a finished Representative turn: a private like, and a
// link that opens the flag card in place.
export function TurnFeedback({ sessionId, sessionCode, turnIndex, text, transparency, representativeName }: TurnFeedbackProps) {
  const [liked, setLiked] = useState(false);
  const [liking, setLiking] = useState(false);
  const [open, setOpen] = useState(false);
  const [sent, setSent] = useState(false);

  const like = async () => {
    if (liked || liking) return;
    setLiking(true);
    try {
      await sendTurnFeedback(sessionId, sessionCode, {
        kind: 'like', turn_index: turnIndex, sentence_index: null, reason: null, text: null, email: null,
      });
      setLiked(true);
    } catch {
      // A like is private and low stakes; a failed one leaves the control as it was.
    } finally {
      setLiking(false);
    }
  };

  const cardId = `turn-${turnIndex}-flag-card`;

  return (
    <div className="turn-feedback-wrap">
      <div className="turn-feedback sans">
        <button
          type="button"
          id={`turn-${turnIndex}-like`}
          className="turn-feedback__like"
          aria-pressed={liked}
          disabled={liked || liking}
          onClick={like}
        >
          <HeartIcon filled={liked} />
          This helped
        </button>
        <button
          type="button"
          id={`turn-${turnIndex}-flag`}
          className="turn-feedback__flag"
          aria-expanded={open}
          aria-controls={cardId}
          disabled={sent}
          onClick={() => setOpen((o) => !o)}
        >
          Answer was not clear or accurate
        </button>
      </div>
      {sent && (
        <p className="feedback-card__thanks sans" role="status">
          Thank you. We check every one of these against the sources. What we find goes on our Corrections page.
        </p>
      )}
      {open && !sent && (
        <FlagCard
          id={cardId}
          sessionId={sessionId}
          sessionCode={sessionCode}
          turnIndex={turnIndex}
          text={text}
          transparency={transparency}
          representativeName={representativeName}
          onCancel={() => setOpen(false)}
          onSent={() => {
            setSent(true);
            setOpen(false);
          }}
        />
      )}
    </div>
  );
}

interface FlagCardProps extends TurnFeedbackProps {
  id: string;
  onCancel: () => void;
  onSent: () => void;
}

function FlagCard({ id, sessionId, sessionCode, turnIndex, text, transparency, representativeName, onCancel, onSent }: FlagCardProps) {
  const choices = sentenceChoices(text, transparency);
  const prefix = `turn-${turnIndex}`;
  const [sentence, setSentence] = useState<number | null | undefined>(undefined);
  const [reason, setReason] = useState<FlagReason | null>(null);
  const [line, setLine] = useState('');
  const [email, setEmail] = useState('');
  const [sending, setSending] = useState(false);
  const [failed, setFailed] = useState(false);

  const ready = sentence !== undefined && reason !== null && !sending;

  const submit = async (event: FormEvent) => {
    event.preventDefault();
    if (sentence === undefined || reason === null || sending) return;
    setSending(true);
    setFailed(false);
    try {
      await sendTurnFeedback(sessionId, sessionCode, {
        kind: 'flag',
        turn_index: turnIndex,
        sentence_index: sentence,
        reason,
        text: line.trim() || null,
        email: email.trim() || null,
      });
      onSent();
    } catch {
      setFailed(true);
      setSending(false);
    }
  };

  return (
    <form id={id} className="feedback-card sans" aria-labelledby={`${prefix}-flag-title`} onSubmit={submit}>
      <p id={`${prefix}-flag-title`} className="feedback-card__title">Tell us what was not clear or accurate</p>

      <fieldset className="feedback-card__group">
        <legend>Which sentence?</legend>
        {choices.map((c) => (
          <label key={c.index ?? 'whole'} className="feedback-card__option" htmlFor={`${prefix}-sentence-${c.index ?? 'whole'}`}>
            <input
              type="radio"
              id={`${prefix}-sentence-${c.index ?? 'whole'}`}
              name={`${prefix}-sentence`}
              checked={sentence === c.index}
              onChange={() => setSentence(c.index)}
            />
            <span>{c.label}</span>
          </label>
        ))}
      </fieldset>

      <fieldset className="feedback-card__group">
        <legend>What is the problem?</legend>
        <div className="feedback-card__chips">
          {REASONS.map((r) => (
            <span key={r.value} className="feedback-card__chip">
              <input
                type="radio"
                id={`${prefix}-reason-${r.value}`}
                name={`${prefix}-reason`}
                checked={reason === r.value}
                onChange={() => setReason(r.value)}
              />
              <label htmlFor={`${prefix}-reason-${r.value}`}>{r.label}</label>
            </span>
          ))}
        </div>
      </fieldset>

      <p className="feedback-card__fine">
        If you disagree with what {representativeName} believes, say so in the conversation. That is what it is for. Anything else about the experience: use "Tell us what you think" at the top of the page.
      </p>

      {reason !== null && (
        <>
          <label className="feedback-card__label" htmlFor={`${prefix}-line`}>Add a line if you like (optional)</label>
          <textarea
            id={`${prefix}-line`}
            className="feedback-card__field"
            rows={3}
            maxLength={600}
            placeholder="What you know, or where we should look."
            value={line}
            onChange={(e) => setLine(e.target.value)}
          />
          <p className="feedback-card__fine">{FEEDBACK_SAFETY_LINE}</p>
        </>
      )}

      <label className="feedback-card__label" htmlFor={`${prefix}-email`}>Email, if you want to hear what we find (optional)</label>
      <input
        type="email"
        id={`${prefix}-email`}
        className="feedback-card__field"
        maxLength={200}
        autoComplete="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      {failed && <p className="feedback-card__failed" role="alert">{FEEDBACK_FAILED}</p>}
      <div className="feedback-card__actions">
        <button type="submit" id={`${prefix}-send`} disabled={!ready}>Send</button>
        <button type="button" id={`${prefix}-cancel`} disabled={sending} onClick={onCancel}>Cancel</button>
      </div>
    </form>
  );
}
