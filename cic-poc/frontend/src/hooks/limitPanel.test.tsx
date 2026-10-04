import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

const NOTE = { key: 'spent', text: 'A line.' };

async function load() {
  vi.resetModules();
  vi.stubEnv('VITE_DEEPER_ENABLED', 'on');
  vi.doMock('../lib/api', async () => {
    const actual = await vi.importActual<typeof import('../lib/api')>('../lib/api');
    return {
      ...actual,
      createSession: vi.fn().mockResolvedValue({ session_id: 's', session_code: 'c' }),
      createTableSession: vi.fn().mockResolvedValue({ session_id: 's', session_code: 'c', world_keys: ['a', 'b'] }),
      getTranscript: vi.fn().mockResolvedValue({ transcript: [], closed: false, mode: 'interview', world_keys: null, round_open: false }),
      sendMessage: vi.fn().mockResolvedValue({ facilitator: { kind: 'limit', text: 'Paused.' }, voice: null, limit_note: NOTE }),
      sendTableMessage: vi.fn().mockResolvedValue({ facilitator: [{ kind: 'limit', text: 'Paused.' }], voice: null, limit_note: NOTE, round_open: false }),
    };
  });
  const deeper = await import('../lib/deeper');
  const { useConversation } = await import('./useConversation');
  const { useTable } = await import('./useTable');
  return { deeper, useConversation, useTable };
}

beforeEach(() => localStorage.clear());
afterEach(() => {
  vi.doUnmock('../lib/api');
  vi.unstubAllEnvs();
});

describe('the panel opens at a limit', () => {
  it('opens when an interview turn comes back with a limit note', async () => {
    const { deeper, useConversation } = await load();
    const { result } = renderHook(() => useConversation());
    await act(async () => {
      await result.current.begin('fix');
    });
    expect(deeper.deeperSnapshot().panelOpen).toBe(false);
    await act(async () => {
      await result.current.send('hello');
    });
    expect(deeper.deeperSnapshot().panelOpen).toBe(true);
  });

  it('opens when a Table round comes back with a limit note', async () => {
    const { deeper, useTable } = await load();
    const { result } = renderHook(() => useTable());
    await act(async () => {
      await result.current.convene(['a', 'b']);
    });
    expect(deeper.deeperSnapshot().panelOpen).toBe(false);
    await act(async () => {
      await result.current.send('hello');
    });
    expect(deeper.deeperSnapshot().panelOpen).toBe(true);
  });
});
