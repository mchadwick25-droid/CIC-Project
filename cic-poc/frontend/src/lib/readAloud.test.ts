/**
 * jsdom doesn't implement window.speechSynthesis (same category of gap
 * test/setup.ts already documents for matchMedia) - each test stubs the
 * minimal shape this module actually calls, scoped to this file rather
 * than added to the shared setup, since no other test in this repo needs
 * it yet.
 */
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { cancelReadAloud, isReadAloudSupported, recordReadAloudPlay, speakText, splitIntoSentences } from './readAloud';

class FakeUtterance {
  onend: (() => void) | null = null;
  onerror: (() => void) | null = null;
  constructor(public text: string) {}
}

function stubSpeechSynthesis() {
  const spoken: FakeUtterance[] = [];
  const speechSynthesis = {
    speak: vi.fn((u: FakeUtterance) => spoken.push(u)),
    cancel: vi.fn(),
  };
  vi.stubGlobal('speechSynthesis', speechSynthesis);
  vi.stubGlobal('SpeechSynthesisUtterance', FakeUtterance);
  return { speechSynthesis, spoken };
}

afterEach(() => {
  vi.unstubAllGlobals();
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
