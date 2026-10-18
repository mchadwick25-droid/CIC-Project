import { useEffect, useRef, useState, type FormEvent, type KeyboardEvent } from 'react';
import { sendExperienceFeedback, type QuoteConsent } from '../lib/api';
import { FEEDBACK_FAILED, FEEDBACK_SAFETY_LINE } from './feedbackText';

const TOGGLE_ID = 'experience-feedback-toggle';
const CARD_ID = 'experience-feedback-card';

interface ExperienceFeedbackButtonProps {
  open: boolean;
  onToggle: () => void;
}

// The quiet button in the page bar that opens the experience card.
export function ExperienceFeedbackButton({ open, onToggle }: ExperienceFeedbackButtonProps) {
  return (
    <button
      type="button"
      id={TOGGLE_ID}
      className="experience-feedback__toggle sans"
      aria-expanded={open}
      aria-controls={CARD_ID}
      onClick={onToggle}
    >
      Tell us what you think
    </button>
  );
}

interface ExperienceFeedbackCardProps {
  page: string;
  onClose: () => void;
}

const CONSENTS: { value: QuoteConsent; label: string }[] = [
  { value: 'no', label: 'No' },
  { value: 'anonymous', label: 'Yes, without my name' },
  { value: 'first_name', label: 'Yes, with my first name:' },
];

// The card below the bar: words about the experience, consent to quote, an
// optional email. It posts with the page it was opened on and needs no session.
export function ExperienceFeedbackCard({ page, onClose }: ExperienceFeedbackCardProps) {
  const [text, setText] = useState('');
  const [consent, setConsent] = useState<QuoteConsent>('no');
  const [firstName, setFirstName] = useState('');
  const [email, setEmail] = useState('');
  const [sending, setSending] = useState(false);
  const [failed, setFailed] = useState(false);
  const [sent, setSent] = useState(false);
  const textRef = useRef<HTMLTextAreaElement>(null);

  useEffect(() => {
    textRef.current?.focus();
  }, []);

  const close = () => {
    onClose();
    document.getElementById(TOGGLE_ID)?.focus();
  };

  const onKeyDown = (event: KeyboardEvent) => {
    if (event.key === 'Escape') {
      event.stopPropagation();
      close();
    }
  };

  const submit = async (event: FormEvent) => {
    event.preventDefault();
    if (!text.trim() || sending) return;
    setSending(true);
    setFailed(false);
    try {
      await sendExperienceFeedback({
        kind: 'comment',
        page,
        text: text.trim(),
        quote_consent: consent,
        first_name: consent === 'first_name' ? firstName.trim() || null : null,
        email: email.trim() || null,
      });
      setSent(true);
    } catch {
      setFailed(true);
      setSending(false);
    }
  };

  if (sent) {
    return (
      <div className="experience-feedback sans">
        <p className="feedback-card__thanks" role="status">Thank you. A person reads these each week.</p>
      </div>
    );
  }

  return (
    <div className="experience-feedback sans">
      <form id={CARD_ID} className="feedback-card" role="dialog" aria-labelledby="experience-feedback-title" onKeyDown={onKeyDown} onSubmit={submit}>
        <p id="experience-feedback-title" className="feedback-card__title">Tell us what you think</p>

        <label className="feedback-card__label" htmlFor="experience-feedback-text">What was this like for you? What should we do better?</label>
        <textarea
          id="experience-feedback-text"
          ref={textRef}
          className="feedback-card__field"
          rows={4}
          required
          maxLength={2000}
          value={text}
          onChange={(e) => setText(e.target.value)}
        />

        <fieldset className="feedback-card__group">
          <legend>May we quote you?</legend>
          {CONSENTS.map((c) => (
            <label key={c.value} className="feedback-card__option" htmlFor={`experience-feedback-consent-${c.value}`}>
              <input
                type="radio"
                id={`experience-feedback-consent-${c.value}`}
                name="experience-feedback-consent"
                checked={consent === c.value}
                onChange={() => setConsent(c.value)}
              />
              <span>{c.label}</span>
            </label>
          ))}
          <input
            type="text"
            id="experience-feedback-first-name"
            className="feedback-card__field"
            aria-label="First name"
            maxLength={60}
            disabled={consent !== 'first_name'}
            value={firstName}
            onChange={(e) => setFirstName(e.target.value)}
          />
        </fieldset>

        <p className="feedback-card__fine">{FEEDBACK_SAFETY_LINE}</p>

        <label className="feedback-card__label" htmlFor="experience-feedback-email">Email, if you would like a reply (optional)</label>
        <input
          type="email"
          id="experience-feedback-email"
          className="feedback-card__field"
          maxLength={200}
          autoComplete="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
        />

        {failed && <p className="feedback-card__failed" role="alert">{FEEDBACK_FAILED}</p>}
        <div className="feedback-card__actions">
          <button type="submit" id="experience-feedback-send" disabled={sending || !text.trim()}>Send</button>
          <button type="button" id="experience-feedback-cancel" disabled={sending} onClick={close}>Cancel</button>
        </div>
      </form>
    </div>
  );
}
