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

type Line = string | ((...args: never[]) => string);
const lineOf = (value: Line, fill: unknown): string =>
  typeof value === 'function' ? (value as (...args: unknown[]) => string)(...Array.from({ length: value.length }, () => fill)) : value;

describe('accounts copy', () => {
  it('reads at Flesch Reading Ease 60 or above', () => {
    const lines = Object.values(accountsCopy).map((v) => lineOf(v as Line, 3));
    const text = lines.map((l) => (/[.?!]$/.test(String(l)) ? String(l) : `${l}.`)).join(' ');
    expect(fleschReadingEase(text)).toBeGreaterThanOrEqual(60);
  });

  it('reads at 50 or above on every line of 7 words or more', () => {
    for (const v of Object.values(accountsCopy)) {
      const line = lineOf(v as Line, 'Monday');
      if (line.split(/\s+/).length >= 7) expect(fleschReadingEase(/[.?!]$/.test(line) ? line : `${line}.`), line).toBeGreaterThanOrEqual(50);
    }
  });

  it('keeps every sentence to 25 words or fewer', () => {
    for (const v of Object.values(accountsCopy)) {
      const line = lineOf(v as Line, 'Monday');
      for (const sentence of String(line).split(/[.?!]+/)) {
        expect(sentence.trim().split(/\s+/).filter(Boolean).length).toBeLessThanOrEqual(25);
      }
    }
  });
});
