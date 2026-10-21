import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useReveal, type RevealItem } from './useReveal';

const item = (key: string, text: string, complete = true, speaker = 'x'): RevealItem => ({ key, speaker, text, complete });
const tick = (ms: number) => {
  for (let t = 0; t < ms; t += 60) {
    act(() => {
      vi.advanceTimersByTime(60);
    });
  }
};

beforeEach(() => vi.useFakeTimers());
afterEach(() => {
  vi.useRealTimers();
  vi.unstubAllGlobals();
});

describe('useReveal', () => {
  it('shows what was already complete when it opened, whole and at rest', () => {
    const { result } = renderHook(() => useReveal([item('a', 'one two three')]));
    expect(result.current.reveal('a')).toEqual({ text: 'one two three', revealing: false });
    expect(result.current.busy).toBe(false);
    expect(result.current.speaking).toBeNull();
  });

  it('rolls a later reply out word by word, then leaves it whole', () => {
    const { result, rerender } = renderHook(({ items }) => useReveal(items), { initialProps: { items: [] as RevealItem[] } });
    rerender({ items: [item('a', 'one two three four five six')] });
    expect(result.current.reveal('a')).toBeNull();
    tick(360);
    const part = result.current.reveal('a');
    expect(part?.revealing).toBe(true);
    expect(part?.text.length).toBeGreaterThan(0);
    expect(part?.text.length).toBeLessThan('one two three four five six'.length);
    tick(1500);
    expect(result.current.reveal('a')).toEqual({ text: 'one two three four five six', revealing: false });
    expect(result.current.busy).toBe(false);
  });

  it('holds the next voice back until the one before has finished, and names who is speaking', () => {
    const { result, rerender } = renderHook(({ items }) => useReveal(items), { initialProps: { items: [] as RevealItem[] } });
    rerender({ items: [item('a', 'one two three four five six seven eight', true, 'first'), item('b', 'nine ten', true, 'second')] });
    tick(300);
    expect(result.current.speaking).toBe('first');
    expect(result.current.reveal('b')).toBeNull();
    tick(1500);
    expect(result.current.reveal('a')?.revealing).toBe(false);
    expect(result.current.speaking === 'second' || result.current.reveal('b')?.revealing === false).toBe(true);
    tick(1500);
    expect(result.current.reveal('b')).toEqual({ text: 'nine ten', revealing: false });
    expect(result.current.speaking).toBeNull();
  });

  it('waits for a reply that is still arriving, without ending it early', () => {
    const { result, rerender } = renderHook(({ items }) => useReveal(items), { initialProps: { items: [] as RevealItem[] } });
    rerender({ items: [item('a', 'one two', false)] });
    tick(1500);
    expect(result.current.reveal('a')).toEqual({ text: 'one two', revealing: true });
    expect(result.current.busy).toBe(true);
    rerender({ items: [item('a', 'one two three', false)] });
    tick(600);
    expect(result.current.reveal('a')?.text).toBe('one two three');
    rerender({ items: [item('a', 'one two three', true)] });
    tick(300);
    expect(result.current.reveal('a')?.revealing).toBe(false);
  });

  it('shows a complete reply whole at once when the reader asks for less motion', () => {
    vi.stubGlobal('matchMedia', (query: string) => ({ matches: query.includes('reduce'), media: query, addEventListener() {}, removeEventListener() {}, addListener() {}, removeListener() {}, dispatchEvent: () => false }));
    const { result, rerender } = renderHook(({ items }) => useReveal(items), { initialProps: { items: [] as RevealItem[] } });
    rerender({ items: [item('a', 'one two three four five six')] });
    expect(result.current.reveal('a')).toEqual({ text: 'one two three four five six', revealing: false });
  });

  it('speeds up when the reader has fallen well behind', () => {
    const long = Array.from({ length: 200 }, (_, i) => `w${i}`).join(' ');
    const { result, rerender } = renderHook(({ items }) => useReveal(items), { initialProps: { items: [] as RevealItem[] } });
    rerender({ items: [item('a', long)] });
    tick(1020);
    const shown = result.current.reveal('a')?.text.split(' ').length ?? 0;
    expect(shown).toBeGreaterThan(9 * 1.02 * 1.5);
  });
});
