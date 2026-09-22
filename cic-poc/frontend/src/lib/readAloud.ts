/**
 * Thin Web Speech API wrapper - step 1 of Mark's read-aloud ruling
 * (2026-09-22: "start with read-aloud free, composite voice on the paid
 * tier... test one step at a time" - see Ministry/Technology/
 * CiC_ReadAloud_Step1_Design_Note.md). Zero API cost, no new backend, no
 * audio files: the participant's own browser reads text already on
 * screen through window.speechSynthesis. Composite Representative
 * voices, server-side TTS, and any paid tier are a later, separate step
 * and nothing here reaches toward them.
 *
 * No voice is ever chosen here - SpeechSynthesisUtterance.voice is never
 * assigned, so the browser always speaks in its own default voice for
 * the page's language (design note Q6: no picker, no gendered/character
 * voice choice in this step).
 *
 * Text is split into sentences and queued as separate utterances rather
 * than spoken as one long one. Two independent reasons, not one:
 *   - Chrome's speechSynthesis has a long-standing bug where a single
 *     utterance longer than ~15s of audio silently stops
 *     (https://bugs.chromium.org/p/chromium/issues/detail?id=679437) -
 *     unacceptable for the text this project can least afford to cut off,
 *     engine/m4/crisis_resources.py's safety turns (design note Q1: never
 *     skipped or truncated).
 *   - Design note Q2 ("only completed sentences, never a partial one")
 *     needs a sentence-granular queue regardless, ahead of Stage 7's own
 *     streaming work - this gives that boundary for free rather than
 *     inventing a second mechanism later.
 */
const SENTENCE_SPLIT = /(?<=[.!?])\s+/;

export function isReadAloudSupported(): boolean {
  return (
    typeof window !== 'undefined' &&
    'speechSynthesis' in window &&
    typeof window.SpeechSynthesisUtterance === 'function'
  );
}

// Exported for the design note's own claim to be checkable, not just
// asserted - a reviewer or test can see exactly what "sentence" means
// here without reading speakText's internals.
export function splitIntoSentences(text: string): string[] {
  return text
    .split(SENTENCE_SPLIT)
    .map((s) => s.trim())
    .filter(Boolean);
}

/**
 * Speaks `text` sentence-by-sentence, calling `onDone` exactly once when
 * playback finishes on its own or errors out. Never called for a manual
 * stop - `cancelReadAloud` handles that path directly (see
 * ReadAloudControl), so a caller doesn't have to guess which of two
 * completion signals actually means "the button should go back to idle."
 */
export function speakText(text: string, onDone: () => void): void {
  if (!isReadAloudSupported()) {
    onDone();
    return;
  }
  window.speechSynthesis.cancel(); // only one turn ever speaks at a time
  const sentences = splitIntoSentences(text);
  if (sentences.length === 0) {
    onDone();
    return;
  }
  sentences.forEach((sentence, i) => {
    const utterance = new SpeechSynthesisUtterance(sentence);
    if (i === sentences.length - 1) {
      utterance.onend = onDone;
      utterance.onerror = onDone;
    }
    window.speechSynthesis.speak(utterance);
  });
}

export function cancelReadAloud(): void {
  if (isReadAloudSupported()) window.speechSynthesis.cancel();
}

/**
 * Mark's ruling, 2026-09-22 (design note Q7) - Option A, verbatim. This
 * is the only disclosure text this project ships for read-aloud; it is
 * not a prop some future caller can override with different wording -
 * changing it is a change order, the same discipline every other
 * approved participant-facing string in this project is held to.
 * `representativeName` is interpolated the same way engine/m4/
 * crisis_resources.py's own `{representative_name}` slot is - a real
 * name already carried by the world, never invented here.
 */
export function readAloudDisclosureText(representativeName: string): string {
  return `This reads the words on screen aloud in your device's own voice — it isn't ${representativeName} speaking.`;
}

const DISCLOSURE_SEEN_KEY = 'cic_read_aloud_disclosure_seen';

// sessionStorage (not localStorage) - same "survive a reload of the same
// tab, not a new tab" scope lib/sessionStore.ts already establishes.
// Without this, reloading mid-conversation while the disclosure is still
// showing would look like a second "first time" once React state resets.
export function hasSeenReadAloudDisclosure(): boolean {
  try {
    return sessionStorage.getItem(DISCLOSURE_SEEN_KEY) === '1';
  } catch {
    return false;
  }
}

export function markReadAloudDisclosureSeen(): void {
  try {
    sessionStorage.setItem(DISCLOSURE_SEEN_KEY, '1');
  } catch {
    // Private browsing / quota - the note simply shows again next time.
  }
}

/**
 * Design note Q8: the one number this instruments is "share of
 * conversations with at least one read-aloud play." No UX-telemetry
 * pipeline exists yet in cic-poc/frontend (checked: engine/api's own
 * *_events.db stores conversation transcripts, not client UX events) -
 * wiring a real sink is out of this step's scope. This dispatches one
 * browser CustomEvent per play so a later analytics thread has a single,
 * already-named integration point to listen for, rather than inventing
 * one from scratch; nothing currently listens for it.
 */
export function recordReadAloudPlay(): void {
  if (typeof window === 'undefined') return;
  window.dispatchEvent(new CustomEvent('cic:read-aloud-play'));
}
