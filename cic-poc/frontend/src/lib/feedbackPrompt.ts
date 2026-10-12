export const FEEDBACK_FORM_URL = 'https://tally.so/r/PdMgbd';

export type FeedbackVariant = 'invite' | 'ending' | 'return';

const STORAGE_KEY = 'cic_feedback';

interface FeedbackState {
  invited: boolean;
  pendingTurns: number;
}

function read(): FeedbackState {
  try {
    const parsed = JSON.parse(localStorage.getItem(STORAGE_KEY) ?? '{}');
    return {
      invited: parsed?.invited === true,
      pendingTurns: Number.isInteger(parsed?.pendingTurns) && parsed.pendingTurns > 0 ? parsed.pendingTurns : 0,
    };
  } catch {
    return { invited: false, pendingTurns: 0 };
  }
}

function write(state: FeedbackState) {
  try {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(state));
  } catch {
    // Storage refused: the prompts simply do not remember anything.
  }
}

export function feedbackUrl(variant: FeedbackVariant): string {
  return `${FEEDBACK_FORM_URL}?from=${variant}`;
}

export function readFeedbackState(): FeedbackState {
  return read();
}

export function markInvited() {
  write({ ...read(), invited: true });
}

/** A visit that has begun and not been ended on purpose. */
export function recordOpenVisit(participantTurns: number) {
  write({ ...read(), pendingTurns: participantTurns });
}

export function clearOpenVisit() {
  write({ ...read(), pendingTurns: 0 });
}
