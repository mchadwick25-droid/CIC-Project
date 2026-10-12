import { useCallback, useEffect, useRef, useState } from 'react';
import { clearOpenVisit, markInvited, readFeedbackState, recordOpenVisit, type FeedbackVariant } from '../lib/feedbackPrompt';

export const INVITE_DELAY_MS = 10_000;

export interface FeedbackPopupState {
  variant: FeedbackVariant;
  turns: number;
}

/**
 * Three moments, all in a pop-up: ten seconds after the launch screen
 * opens, when a conversation is ended on purpose, and on the next visit
 * after one that was left without ending. Never while a conversation is open.
 */
export function useFeedbackPrompt(onLaunch: boolean, participantTurns: number) {
  const [popup, setPopup] = useState<FeedbackPopupState | null>(null);
  const onLaunchRef = useRef(onLaunch);
  onLaunchRef.current = onLaunch;

  useEffect(() => {
    const timer = window.setTimeout(() => {
      if (!onLaunchRef.current) return;
      const state = readFeedbackState();
      if (state.pendingTurns > 0) {
        clearOpenVisit();
        setPopup({ variant: 'return', turns: state.pendingTurns });
      } else if (!state.invited) {
        markInvited();
        setPopup({ variant: 'invite', turns: 0 });
      }
    }, INVITE_DELAY_MS);
    return () => window.clearTimeout(timer);
  }, []);

  useEffect(() => {
    if (participantTurns > 0) recordOpenVisit(participantTurns);
  }, [participantTurns]);

  const showEnding = useCallback(() => {
    clearOpenVisit();
    setPopup({ variant: 'ending', turns: 0 });
  }, []);

  const dismiss = useCallback(() => setPopup(null), []);

  return { popup, showEnding, dismiss };
}
