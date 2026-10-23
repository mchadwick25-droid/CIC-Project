import { useEffect, useRef, useState, type FormEvent, type KeyboardEvent } from 'react';
import { sendPageFeedback, type PageReportReason } from '../lib/api';
import { FEEDBACK_FAILED, FEEDBACK_SAFETY_LINE } from './feedbackText';

const MAX_NOTE = 600;
const LIKE_KEY_PREFIX = 'cic-page-like:';

const REASONS: { value: PageReportReason; label: string }[] = [
  { value: 'accuracy', label: 'Accuracy' },
  { value: 'craft', label: 'Craft' },
];

function wasLiked(page: string): boolean {
  try {
    return window.localStorage.getItem(LIKE_KEY_PREFIX + page) === '1';
  } catch {
    return false;
  }
}

function rememberLike(page: string): void {
  try {
    window.localStorage.setItem(LIKE_KEY_PREFIX + page, '1');
  } catch {
    // The like was sent; remembering it is only a convenience.
  }
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

interface PageFeedbackProps {
  page: string;
}

// The quiet row at the foot of a page: a like, and a link that opens a small
// card to report a problem with accuracy or craft. Neither needs a session.
export function PageFeedback({ page }: PageFeedbackProps) {
  const [liked, setLiked] = useState(() => wasLiked(page));
  const [liking, setLiking] = useState(false);
  const [open, setOpen] = useState(false);
  const [sent, setSent] = useState(false);
  const toggleRef = useRef<HTMLButtonElement>(null);

  const like = async () => {
    if (liked || liking) return;
    setLiking(true);
    try {
      await sendPageFeedback({ kind: 'like', page });
      rememberLike(page);
      setLiked(true);
    } catch {
      // A like is low stakes; a failed one leaves the control as it was.
    } finally {
      setLiking(false);
    }
  };

  const closeCard = () => {
    setOpen(false);
    toggleRef.current?.focus();
  };

  return (
    <div className="page-feedback sans">
      <div className="page-feedback__row">
        <button type="button" className="turn-feedback__like" aria-pressed={liked} disabled={liked || liking} onClick={like}>
          <HeartIcon filled={liked} />
          This helped
        </button>
        <button
          type="button"
          ref={toggleRef}
          className="turn-feedback__flag"
          aria-expanded={open}
          aria-controls="page-feedback-card"
          onClick={() => {
            setSent(false);
            setOpen((o) => !o);
          }}
        >
          Report a problem
        </button>
      </div>
      <p className="feedback-card__thanks" role="status">{sent ? 'Thank you. A person will read it.' : ''}</p>
      {open && (
        <ReportCard
          page={page}
          onCancel={closeCard}
          onSent={() => {
            setSent(true);
            closeCard();
          }}
        />
      )}
    </div>
  );
}

interface ReportCardProps {
  page: string;
  onCancel: () => void;
  onSent: () => void;
}

export function ReportCard({ page, onCancel, onSent }: ReportCardProps) {
  const [reason, setReason] = useState<PageReportReason | null>(null);
  const [note, setNote] = useState('');
  const [email, setEmail] = useState('');
  const [sending, setSending] = useState(false);
  const [failed, setFailed] = useState(false);
  const firstRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    firstRef.current?.focus();
  }, []);

  const ready = reason !== null && note.trim().length > 0 && !sending;

  const submit = async (event: FormEvent) => {
    event.preventDefault();
    if (reason === null || !note.trim() || sending) return;
    setSending(true);
    setFailed(false);
    try {
      await sendPageFeedback({ kind: 'report', page, reason, text: note.trim(), email: email.trim() || null });
      onSent();
    } catch {
      setFailed(true);
      setSending(false);
    }
  };

  const onKeyDown = (event: KeyboardEvent) => {
    if (event.key === 'Escape') {
      event.stopPropagation();
      onCancel();
    }
  };

  return (
    <form
      id="page-feedback-card"
      className="feedback-card"
      role="dialog"
      aria-labelledby="page-feedback-title"
      onKeyDown={onKeyDown}
      onSubmit={submit}
    >
      <p id="page-feedback-title" className="feedback-card__title">Tell us what is wrong</p>

      <fieldset className="feedback-card__group">
        <legend>What kind of problem?</legend>
        <div className="feedback-card__chips">
          {REASONS.map((r) => (
            <span key={r.value} className="feedback-card__chip">
              <input
                type="radio"
                id={`page-feedback-reason-${r.value}`}
                name="page-feedback-reason"
                ref={r.value === 'accuracy' ? firstRef : undefined}
                checked={reason === r.value}
                onChange={() => setReason(r.value)}
              />
              <label htmlFor={`page-feedback-reason-${r.value}`}>{r.label}</label>
            </span>
          ))}
        </div>
      </fieldset>

      <label className="feedback-card__label" htmlFor="page-feedback-note">What did you see?</label>
      <textarea
        id="page-feedback-note"
        className="feedback-card__field"
        rows={4}
        required
        maxLength={MAX_NOTE}
        aria-describedby="page-feedback-count"
        value={note}
        onChange={(e) => setNote(e.target.value)}
      />
      <p id="page-feedback-count" className="feedback-card__fine">{MAX_NOTE - note.length} characters left</p>

      <p className="feedback-card__fine">{FEEDBACK_SAFETY_LINE}</p>

      <label className="feedback-card__label" htmlFor="page-feedback-email">Email (only if you want a reply)</label>
      <input
        type="email"
        id="page-feedback-email"
        className="feedback-card__field"
        maxLength={200}
        autoComplete="email"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
      />

      {failed && <p className="feedback-card__failed" role="alert">{FEEDBACK_FAILED}</p>}
      <div className="feedback-card__actions">
        <button type="submit" disabled={!ready}>Send</button>
        <button type="button" disabled={sending} onClick={onCancel}>Cancel</button>
      </div>
    </form>
  );
}
