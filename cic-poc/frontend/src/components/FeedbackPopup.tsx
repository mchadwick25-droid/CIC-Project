import { useEffect, useRef } from 'react';
import { feedbackUrl, type FeedbackVariant } from '../lib/feedbackPrompt';

interface FeedbackPopupProps {
  variant: FeedbackVariant;
  turns: number;
  onClose: () => void;
}

function turnsPhrase(turns: number): string {
  return turns === 1 ? 'after one question' : `after ${turns} questions`;
}

const COPY: Record<FeedbackVariant, { title: string; yes: string; no: string }> = {
  invite: { title: 'Help us shape this', yes: 'Share feedback', no: 'Not now' },
  ending: { title: 'Before you go', yes: 'Tell us', no: 'No thanks' },
  return: { title: 'Welcome back', yes: 'Tell us', no: 'Not now' },
};

export function FeedbackPopup({ variant, turns, onClose }: FeedbackPopupProps) {
  const yesRef = useRef<HTMLAnchorElement>(null);
  const copy = COPY[variant];

  useEffect(() => {
    yesRef.current?.focus();
    function onKeyDown(e: KeyboardEvent) {
      if (e.key === 'Escape') onClose();
    }
    document.addEventListener('keydown', onKeyDown);
    return () => document.removeEventListener('keydown', onKeyDown);
  }, [onClose]);

  return (
    <div className="feedback-popup" role="dialog" aria-labelledby="feedback-popup-title">
      <h2 id="feedback-popup-title" className="feedback-popup__title">{copy.title}</h2>
      <p className="feedback-popup__body sans">
        {variant === 'invite' && 'We are in an early pilot. Tell us what you find, whenever you like. It takes about three minutes, and you do not need to finish a conversation first.'}
        {variant === 'ending' && 'What made you stop? Your answer helps us more than you might think.'}
        {variant === 'return' && `Last time you stopped ${turnsPhrase(turns)}. What happened?`}
      </p>
      <div className="feedback-popup__actions">
        <a
          ref={yesRef}
          className="feedback-popup__yes"
          href={feedbackUrl(variant)}
          target="_blank"
          rel="noopener noreferrer"
          onClick={onClose}
        >
          {copy.yes}
        </a>
        <button type="button" className="feedback-popup__no" onClick={onClose}>{copy.no}</button>
      </div>
    </div>
  );
}
