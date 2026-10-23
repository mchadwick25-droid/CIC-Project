import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { TranscriptScroll } from './TranscriptScroll';

const sizes = { scrollHeight: 1000, clientHeight: 200 };

beforeEach(() => {
  vi.stubGlobal('matchMedia', (query: string) => ({ matches: query.includes('reduce'), media: query, addEventListener() {}, removeEventListener() {}, addListener() {}, removeListener() {}, dispatchEvent: () => false }));
  Object.defineProperty(HTMLElement.prototype, 'scrollHeight', { configurable: true, get: () => sizes.scrollHeight });
  Object.defineProperty(HTMLElement.prototype, 'clientHeight', { configurable: true, get: () => sizes.clientHeight });
});

afterEach(() => {
  cleanup();
  vi.unstubAllGlobals();
  delete (HTMLElement.prototype as unknown as Record<string, unknown>).scrollHeight;
  delete (HTMLElement.prototype as unknown as Record<string, unknown>).clientHeight;
});

const frame = () => act(() => new Promise<void>((done) => requestAnimationFrame(() => done())));
const settle = async () => {
  for (let i = 0; i < 3; i += 1) await frame();
};

describe('TranscriptScroll', () => {
  it('is a labelled, keyboard-reachable log with a gold bar for a mouse', () => {
    const { container } = render(<TranscriptScroll label="Conversation" followSignal={0}>text</TranscriptScroll>);
    const log = screen.getByRole('log', { name: 'Conversation' });
    expect(log).toHaveAttribute('tabindex', '0');
    expect(container.querySelector('.conv-scroll__track')?.getAttribute('aria-hidden')).toBe('true');
    expect(container.querySelector('.conv-scroll__thumb')).not.toBeNull();
  });

  it('stays with the newest line, and offers no way back while it is there', async () => {
    render(<TranscriptScroll label="Conversation" followSignal={0}>text</TranscriptScroll>);
    await settle();
    expect(screen.getByRole('log').scrollTop).toBe(800);
    expect(screen.queryByRole('button', { name: /Latest/ })).toBeNull();
  });

  it('lets the reader go back up, then returns to the latest on request', async () => {
    render(<TranscriptScroll label="Conversation" followSignal={0}>text</TranscriptScroll>);
    await settle();
    const log = screen.getByRole('log');
    fireEvent.wheel(log);
    log.scrollTop = 100;
    await settle();
    expect(log.scrollTop).toBe(100);
    const latest = screen.getByRole('button', { name: 'Latest ↓' });
    fireEvent.click(latest);
    await settle();
    expect(log.scrollTop).toBe(800);
    expect(screen.queryByRole('button', { name: /Latest/ })).toBeNull();
  });

  it('follows again when the reader scrolls back to the end, or sends a new question', async () => {
    const { rerender } = render(<TranscriptScroll label="Conversation" followSignal={0}>text</TranscriptScroll>);
    await settle();
    const log = screen.getByRole('log');
    fireEvent.wheel(log);
    log.scrollTop = 300;
    await settle();
    log.scrollTop = 799;
    fireEvent.scroll(log);
    sizes.scrollHeight = 1400;
    await settle();
    expect(log.scrollTop).toBe(1200);
    fireEvent.wheel(log);
    log.scrollTop = 100;
    await settle();
    expect(log.scrollTop).toBe(100);
    rerender(<TranscriptScroll label="Conversation" followSignal={1}>text</TranscriptScroll>);
    await settle();
    expect(log.scrollTop).toBe(1200);
    sizes.scrollHeight = 1000;
  });

  it('goes back up with the keyboard too', async () => {
    render(<TranscriptScroll label="Conversation" followSignal={0}>text</TranscriptScroll>);
    await settle();
    const log = screen.getByRole('log');
    fireEvent.keyDown(log, { key: 'PageUp' });
    log.scrollTop = 200;
    await settle();
    expect(log.scrollTop).toBe(200);
  });
});

describe('TranscriptScroll - with motion', () => {
  it('reaches the very end even when the browser rounds each scroll position to a whole pixel', () => {
    vi.stubGlobal('matchMedia', (query: string) => ({ matches: false, media: query, addEventListener() {}, removeEventListener() {}, addListener() {}, removeListener() {}, dispatchEvent: () => false }));
    vi.useFakeTimers({ toFake: ['requestAnimationFrame', 'cancelAnimationFrame', 'performance'] });
    const stored = new WeakMap<object, number>();
    Object.defineProperty(HTMLElement.prototype, 'scrollTop', {
      configurable: true,
      get() {
        return stored.get(this) ?? 0;
      },
      set(value: number) {
        stored.set(this, Math.round(value));
      },
    });
    try {
      render(<TranscriptScroll label="Conversation" followSignal={0}>text</TranscriptScroll>);
      act(() => {
        vi.advanceTimersByTime(6000);
      });
      expect(screen.getByRole('log').scrollTop).toBe(800);
    } finally {
      vi.useRealTimers();
      delete (HTMLElement.prototype as unknown as Record<string, unknown>).scrollTop;
    }
  });
});
