import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

const NOTE = { key: 'spent', text: 'A line.' };

type Reply = { facilitator: unknown; limit_note: unknown };

async function load(interview: Reply = { facilitator: { kind: 'limit', text: 'Paused.' }, limit_note: NOTE }, table: Reply = { facilitator: [{ kind: 'limit', text: 'Paused.' }], limit_note: NOTE }) {
  vi.resetModules();
  vi.stubEnv('VITE_DEEPER_ENABLED', 'on');
  vi.doMock('../lib/api', async () => {
    const actual = await vi.importActual<typeof import('../lib/api')>('../lib/api');
    return {
      ...actual,
      createSession: vi.fn().mockResolvedValue({ session_id: 's', session_code: 'c' }),
      createTableSession: vi.fn().mockResolvedValue({ session_id: 's', session_code: 'c', world_keys: ['a', 'b'] }),
      getTranscript: vi.fn().mockResolvedValue({ transcript: [], closed: false, mode: 'interview', world_keys: null, round_open: false }),
      sendMessage: vi.fn().mockResolvedValue({ ...interview, voice: null }),
      sendTableMessage: vi.fn().mockResolvedValue({ ...table, voice: null, round_open: false }),
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

  it('stays closed when an interview turn that is a safety check-in carries no limit note', async () => {
    const { deeper, useConversation } = await load({ facilitator: { kind: 'check_in', text: 'Are you all right?' }, limit_note: null });
    const { result } = renderHook(() => useConversation());
    await act(async () => {
      await result.current.begin('fix');
    });
    await act(async () => {
      await result.current.send('hello');
    });
    expect(deeper.deeperSnapshot().panelOpen).toBe(false);
  });

  it('stays closed when a Table round that is a safety turn carries no limit note', async () => {
    const { deeper, useTable } = await load(undefined, { facilitator: [{ kind: 'check_in', text: 'Are you all right?' }], limit_note: null });
    const { result } = renderHook(() => useTable());
    await act(async () => {
      await result.current.convene(['a', 'b']);
    });
    await act(async () => {
      await result.current.send('hello');
    });
    expect(deeper.deeperSnapshot().panelOpen).toBe(false);
  });
});
