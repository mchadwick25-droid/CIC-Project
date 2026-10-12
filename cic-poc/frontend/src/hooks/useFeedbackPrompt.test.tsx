import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { INVITE_DELAY_MS, useFeedbackPrompt } from './useFeedbackPrompt';

describe('useFeedbackPrompt', () => {
  beforeEach(() => {
    localStorage.clear();
    vi.useFakeTimers();
  });
  afterEach(() => vi.useRealTimers());

  it('invites once, ten seconds after the launch screen opens', () => {
    const first = renderHook(() => useFeedbackPrompt(true, 0));
    act(() => { vi.advanceTimersByTime(INVITE_DELAY_MS - 1); });
    expect(first.result.current.popup).toBeNull();
    act(() => { vi.advanceTimersByTime(1); });
    expect(first.result.current.popup?.variant).toBe('invite');
    first.unmount();

    const second = renderHook(() => useFeedbackPrompt(true, 0));
    act(() => { vi.advanceTimersByTime(INVITE_DELAY_MS); });
    expect(second.result.current.popup).toBeNull();
  });

  it('stays quiet while a conversation is open', () => {
    const { result } = renderHook(() => useFeedbackPrompt(false, 1));
    act(() => { vi.advanceTimersByTime(INVITE_DELAY_MS); });
    expect(result.current.popup).toBeNull();
  });

  it('asks on the next visit when the last one was left without ending', () => {
    const first = renderHook(() => useFeedbackPrompt(false, 3));
    first.unmount();
    const next = renderHook(() => useFeedbackPrompt(true, 0));
    act(() => { vi.advanceTimersByTime(INVITE_DELAY_MS); });
    expect(next.result.current.popup).toEqual({ variant: 'return', turns: 3 });
  });

  it('does not ask on the next visit after an ending', () => {
    const first = renderHook(() => useFeedbackPrompt(false, 3));
    act(() => { first.result.current.showEnding(); });
    expect(first.result.current.popup?.variant).toBe('ending');
    first.unmount();
    const next = renderHook(() => useFeedbackPrompt(true, 0));
    act(() => { vi.advanceTimersByTime(INVITE_DELAY_MS); });
    expect(next.result.current.popup?.variant).not.toBe('return');
  });
});
