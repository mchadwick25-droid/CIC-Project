import { useEffect, useRef, useState } from 'react';

export interface RevealItem {
  key: string;
  speaker: string;
  text: string;
  complete: boolean;
}

export interface Revealed {
  text: string;
  revealing: boolean;
}

const WORDS_PER_SECOND = 9;
const CATCH_UP_AFTER = 40;
const TICK_MS = 60;

function words(text: string): string[] {
  return text.match(/\S+\s*/g) ?? [];
}

/**
 * Lets replies arrive one after another at a reading pace. Replies already
 * complete when the screen opens show whole; every later one rolls out word by
 * word, in order, so the next voice waits for the one before it to finish.
 */
export function useReveal(items: RevealItem[]) {
  const [, redraw] = useState(0);
  const done = useRef<Set<string> | null>(null);
  if (done.current === null) done.current = new Set(items.filter((i) => i.complete).map((i) => i.key));
  const shown = useRef(0);
  const latest = useRef(items);
  latest.current = items;

  const still = typeof window !== 'undefined' && window.matchMedia?.('(prefers-reduced-motion: reduce)').matches;
  if (still) for (const item of items) if (item.complete) done.current.add(item.key);

  const active = items.find((i) => !done.current!.has(i.key)) ?? null;
  const activeKey = active?.key ?? null;

  useEffect(() => {
    if (activeKey === null) return undefined;
    shown.current = 0;
    let last = performance.now();
    const timer = window.setInterval(() => {
      const now = performance.now();
      const seconds = (now - last) / 1000;
      last = now;
      const item = latest.current.find((i) => i.key === activeKey);
      if (!item) return;
      const total = words(item.text).length;
      const behind = total - shown.current;
      const rate = behind > CATCH_UP_AFTER ? WORDS_PER_SECOND * 2 : WORDS_PER_SECOND;
      shown.current = Math.min(total, shown.current + rate * seconds);
      if (item.complete && shown.current >= total) {
        done.current!.add(activeKey);
        shown.current = 0;
        window.clearInterval(timer);
      }
      redraw((n) => n + 1);
    }, TICK_MS);
    return () => window.clearInterval(timer);
  }, [activeKey]);

  const reveal = (key: string): Revealed | null => {
    const item = items.find((i) => i.key === key);
    if (!item) return null;
    if (done.current!.has(key)) return { text: item.text, revealing: false };
    if (key !== activeKey) return null;
    const count = Math.floor(shown.current);
    if (count <= 0) return null;
    return { text: words(item.text).slice(0, count).join('').trimEnd(), revealing: true };
  };

  return { reveal, speaking: active ? active.speaker : null, busy: active !== null, showing: active !== null && Math.floor(shown.current) > 0 };
}
