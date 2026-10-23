import { describe, expect, it } from 'vitest';
import { accountsCopy } from './accountsCopy';

function syllables(word: string): number {
  const w = word.toLowerCase().replace(/[^a-z]/g, '');
  if (!w) return 0;
  const groups = w.replace(/e$/, '').match(/[aeiouy]+/g);
  return Math.max(1, groups ? groups.length : 1);
}

function fleschReadingEase(text: string): number {
  const sentences = text.split(/[.?!]+/).filter((s) => s.trim());
  const words = text.split(/\s+/).filter((w) => /[a-z]/i.test(w));
  const total = words.reduce((n, w) => n + syllables(w), 0);
  return 206.835 - 1.015 * (words.length / sentences.length) - 84.6 * (total / words.length);
}

describe('accounts copy', () => {
  it('reads at Flesch Reading Ease 60 or above', () => {
    const lines = Object.values(accountsCopy).map((v) => (typeof v === 'function' ? v(3 as never) : v));
    const text = lines.map((l) => (/[.?!]$/.test(String(l)) ? String(l) : `${l}.`)).join(' ');
    expect(fleschReadingEase(text)).toBeGreaterThanOrEqual(60);
  });

  it('keeps every sentence to 25 words or fewer', () => {
    for (const v of Object.values(accountsCopy)) {
      const line = typeof v === 'function' ? v('Monday' as never) : v;
      for (const sentence of String(line).split(/[.?!]+/)) {
        expect(sentence.trim().split(/\s+/).filter(Boolean).length).toBeLessThanOrEqual(25);
      }
    }
  });
});
