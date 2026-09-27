/**
 * jsdom doesn't implement window.speechSynthesis (same category of gap
 * test/setup.ts already documents for matchMedia) - each test stubs the
 * minimal shape this module actually calls, scoped to this file rather
 * than added to the shared setup, since no other test in this repo needs
 * it yet.
 */
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import {
  cancelReadAloud,
  hasSeenReadAloudDisclosure,
  isReadAloudSupported,
  markReadAloudDisclosureSeen,
  pickVoiceForSeat,
  readAloudDisclosureText,
  recordReadAloudPlay,
  speakText,
  splitIntoSentences,
} from './readAloud';

class FakeUtterance {
  onend: (() => void) | null = null;
  onerror: (() => void) | null = null;
  voice: unknown = null;
  constructor(public text: string) {}
}

function stubSpeechSynthesis(voices: Array<{ name: string; lang: string }> = []) {
  const spoken: FakeUtterance[] = [];
  const speechSynthesis = {
    speak: vi.fn((u: FakeUtterance) => spoken.push(u)),
    cancel: vi.fn(),
    getVoices: vi.fn(() => voices),
  };
  vi.stubGlobal('speechSynthesis', speechSynthesis);
  vi.stubGlobal('SpeechSynthesisUtterance', FakeUtterance);
  return { speechSynthesis, spoken };
}

afterEach(() => {
  vi.unstubAllGlobals();
  document.documentElement.lang = '';
});

describe('isReadAloudSupported', () => {
  it('is false when the browser has no speechSynthesis at all', () => {
    expect(isReadAloudSupported()).toBe(false);
  });

  it('is true once both speechSynthesis and SpeechSynthesisUtterance exist', () => {
    stubSpeechSynthesis();
    expect(isReadAloudSupported()).toBe(true);
  });
});

describe('splitIntoSentences', () => {
  it('splits on sentence-ending punctuation, trimming whitespace', () => {
    expect(splitIntoSentences('First one. Second one! Third one?')).toEqual(['First one.', 'Second one!', 'Third one?']);
  });

  it('drops empty segments and keeps text with no terminal punctuation as one sentence', () => {
    expect(splitIntoSentences('  Just one clause  ')).toEqual(['Just one clause']);
    expect(splitIntoSentences('')).toEqual([]);
  });
});

describe('speakText', () => {
  beforeEach(() => {
    stubSpeechSynthesis();
  });

  it('cancels any prior speech, then queues one utterance per sentence', () => {
    const { speechSynthesis, spoken } = stubSpeechSynthesis();
    speakText('First one. Second one.', vi.fn());

    expect(speechSynthesis.cancel).toHaveBeenCalledTimes(1);
    expect(speechSynthesis.speak).toHaveBeenCalledTimes(2);
    expect(spoken.map((u) => u.text)).toEqual(['First one.', 'Second one.']);
  });

  it('attaches onDone only to the LAST utterance - it fires once, when the whole turn finishes', () => {
    const { spoken } = stubSpeechSynthesis();
    const onDone = vi.fn();
    speakText('First one. Second one. Third one.', onDone);

    expect(spoken[0].onend).toBeNull();
    expect(spoken[1].onend).toBeNull();
    expect(spoken[2].onend).toBeTypeOf('function');

    spoken[2].onend!();
    expect(onDone).toHaveBeenCalledTimes(1);
  });

  it('calls onDone immediately for text with nothing to say, and never touches speechSynthesis', () => {
    const { speechSynthesis } = stubSpeechSynthesis();
    const onDone = vi.fn();
    speakText('   ', onDone);

    expect(onDone).toHaveBeenCalledTimes(1);
    expect(speechSynthesis.speak).not.toHaveBeenCalled();
  });

  it('calls onDone immediately when the browser has no speech synthesis at all', () => {
    vi.unstubAllGlobals();
    const onDone = vi.fn();
    speakText('Some text.', onDone);
    expect(onDone).toHaveBeenCalledTimes(1);
  });

  it("never truncates a long, multi-paragraph safety turn's worth of sentences", () => {
    // Standing in for engine/m4/crisis_resources.py's ACUTE_DISTRESS_RESOURCES -
    // several sentences across blank-line paragraphs; every sentence must
    // still queue as its own utterance, none dropped.
    const { spoken } = stubSpeechSynthesis();
    const safetyText =
      "I want to step in for a moment. What you just told me matters. " +
      "Please reach out to someone real. You're not being sent away.";
    speakText(safetyText, vi.fn());
    expect(spoken).toHaveLength(4);
  });

  it('assigns the given voice to every sentence utterance when one is passed', () => {
    const { spoken } = stubSpeechSynthesis();
    const voice = { name: 'Fake Voice', lang: 'en-US' };
    speakText('First one. Second one.', vi.fn(), voice as SpeechSynthesisVoice);
    expect(spoken.every((u) => u.voice === voice)).toBe(true);
  });

  it('leaves voice unset (browser default) when none is passed', () => {
    const { spoken } = stubSpeechSynthesis();
    speakText('One sentence.', vi.fn());
    expect(spoken[0].voice).toBeNull();
  });
});

describe('pickVoiceForSeat', () => {
  it('gives two seats different voices when at least two voices exist', () => {
    stubSpeechSynthesis([
      { name: 'Alpha', lang: 'en-US' },
      { name: 'Beta', lang: 'en-US' },
    ]);
    const seats = ['alx', 'desert'];
    const alx = pickVoiceForSeat(seats, 'alx');
    const desert = pickVoiceForSeat(seats, 'desert');
    expect(alx).not.toBe(desert);
  });

  it('is deterministic - the same seating always maps to the same voice per world', () => {
    stubSpeechSynthesis([
      { name: 'Alpha', lang: 'en-US' },
      { name: 'Beta', lang: 'en-US' },
    ]);
    const seats = ['alx', 'desert', 'pahc'];
    expect(pickVoiceForSeat(seats, 'pahc')).toBe(pickVoiceForSeat(seats.slice().reverse(), 'pahc'));
  });

  it('filters to the page language when more than one is available, falling back to all voices otherwise', () => {
    stubSpeechSynthesis([
      { name: 'German One', lang: 'de-DE' },
      { name: 'English One', lang: 'en-US' },
    ]);
    document.documentElement.lang = 'en';
    expect(pickVoiceForSeat(['alx'], 'alx')?.name).toBe('English One');
  });

  it('degrades to one shared voice, not a crash, when the device has only one', () => {
    stubSpeechSynthesis([{ name: 'Only One', lang: 'en-US' }]);
    const seats = ['alx', 'desert', 'pahc'];
    expect(seats.map((k) => pickVoiceForSeat(seats, k)?.name)).toEqual(['Only One', 'Only One', 'Only One']);
  });

  it('returns undefined when the device has no voices at all, or no speech synthesis', () => {
    stubSpeechSynthesis([]);
    expect(pickVoiceForSeat(['alx'], 'alx')).toBeUndefined();
    vi.unstubAllGlobals();
    expect(pickVoiceForSeat(['alx'], 'alx')).toBeUndefined();
  });
});

describe('cancelReadAloud', () => {
  it('calls speechSynthesis.cancel when supported', () => {
    const { speechSynthesis } = stubSpeechSynthesis();
    cancelReadAloud();
    expect(speechSynthesis.cancel).toHaveBeenCalledTimes(1);
  });

  it('is a no-op when unsupported (never throws)', () => {
    expect(() => cancelReadAloud()).not.toThrow();
  });
});

describe('recordReadAloudPlay', () => {
  it('dispatches exactly one cic:read-aloud-play CustomEvent', () => {
    const listener = vi.fn();
    window.addEventListener('cic:read-aloud-play', listener);
    recordReadAloudPlay();
    window.removeEventListener('cic:read-aloud-play', listener);
    expect(listener).toHaveBeenCalledTimes(1);
  });
});

describe('readAloudDisclosureText', () => {
  it("is Mark's Option A, verbatim, with the representative's real name interpolated", () => {
    expect(readAloudDisclosureText('Julian of Norwich')).toBe(
      "This reads the words on screen aloud in your device's own voice — it isn't Julian of Norwich speaking."
    );
  });
});

describe('read-aloud disclosure seen-tracking', () => {
  beforeEach(() => {
    sessionStorage.clear();
  });

  it('is unseen until marked, then stays seen', () => {
    expect(hasSeenReadAloudDisclosure()).toBe(false);
    markReadAloudDisclosureSeen();
    expect(hasSeenReadAloudDisclosure()).toBe(true);
  });

  it('survives being read again without re-marking (idempotent)', () => {
    markReadAloudDisclosureSeen();
    markReadAloudDisclosureSeen();
    expect(hasSeenReadAloudDisclosure()).toBe(true);
  });
});
