/**
 * Thin Web Speech API wrapper. Zero API cost, no new backend, no audio
 * files: the participant's own browser reads text already on screen
 * through window.speechSynthesis. Composite Representative voices,
 * server-side TTS, and any paid tier are a later, separate step and
 * nothing here reaches toward them.
 *
 * No voice is ever chosen here - SpeechSynthesisUtterance.voice is never
 * assigned, so the browser always speaks in its own default voice for
 * the page's language.
 *
 * Text is split into sentences and queued as separate utterances rather
 * than spoken as one long one. Two independent reasons, not one:
 *   - Chrome's speechSynthesis has a long-standing bug where a single
 *     utterance longer than ~15s of audio silently stops
 *     (https://bugs.chromium.org/p/chromium/issues/detail?id=679437) -
 *     unacceptable for the text this project can least afford to cut off,
 *     engine/m4/crisis_resources.py's safety turns, which must never be
 *     skipped or truncated.
 *   - Speaking only completed sentences, never a partial one, needs a
 *     sentence-granular queue regardless of when live streaming lands -
 *     this gives that boundary for free rather than inventing a second
 *     mechanism later.
 */
const SENTENCE_SPLIT = /(?<=[.!?])\s+/;

export function isReadAloudSupported(): boolean {
  return (
    typeof window !== 'undefined' &&
    'speechSynthesis' in window &&
    typeof window.SpeechSynthesisUtterance === 'function'
  );
}

// Exported so a test can check exactly what "sentence" means here
// without reading speakText's internals.
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
 * The one disclosure text this project ships for read-aloud - not a
 * prop some future caller can override with different wording.
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
 * No UX-telemetry pipeline exists yet in cic-poc/frontend (engine/api's
 * own *_events.db stores conversation transcripts, not client UX events),
 * so this dispatches one browser CustomEvent per play - a single,
 * already-named integration point a later analytics thread can listen
 * for, rather than inventing one from scratch. Nothing currently listens
 * for it.
 */
export function recordReadAloudPlay(): void {
  if (typeof window === 'undefined') return;
  window.dispatchEvent(new CustomEvent('cic:read-aloud-play'));
}
