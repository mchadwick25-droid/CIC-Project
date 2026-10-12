import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

const CODE = '2345 6789 ABCD EFGH JKLM';
const NOTE = { key: 'spent', text: 'A line.' };
const DUPLICATE = 'That message already reached the room — give it a moment.';

interface Sent {
  text: string;
  id: string;
  withCode: boolean;
}

function json(status: number, body: unknown) {
  return new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json' } });
}

const voice = { speaker: 'fix', text: 'An answer.', citations: [] };

function reply(table: boolean, limited: boolean) {
  if (table) {
    return { round_no: 1, round_open: false, facilitator: limited ? [{ kind: 'limit', text: 'Paused.' }] : [], voice: limited ? null : voice, limit_note: limited ? NOTE : null, session_closed: false };
  }
  return { facilitator: limited ? { kind: 'limit', text: 'Paused.' } : null, voice: limited ? null : voice, limit_note: limited ? NOTE : null };
}

function serverWith(options: { table: boolean; fail?: (sent: Sent, count: number) => boolean; limit?: (sent: Sent) => boolean; hold?: Promise<void> }) {
  const seen = new Set<string>();
  const sent: Sent[] = [];
  const fetchMock = vi.fn(async (url: string, init?: RequestInit) => {
    if (url.endsWith('/api/session')) return json(200, { session_id: 's', session_code: 'c', round_cap: 5 });
    if (url.endsWith('/transcript')) return json(200, { transcript: [], closed: false, mode: options.table ? 'table' : 'interview', world_keys: null, round_open: false });
    if (url.endsWith('/api/deeper/balance')) return json(200, { remaining: 100 });
    const body = JSON.parse(String(init?.body));
    const headers = init?.headers as Record<string, string>;
    const message: Sent = { text: body.text, id: body.client_msg_id, withCode: 'X-Cic-Code' in headers };
    sent.push(message);
    if (seen.has(message.id)) return json(409, { detail: 'duplicate message - already received' });
    if (options.fail?.(message, sent.length)) return json(503, { detail: 'unavailable' });
    seen.add(message.id);
    if (options.hold) await options.hold;
    return json(200, reply(options.table, options.limit?.(message) ?? false));
  });
  vi.stubGlobal('fetch', fetchMock);
  return { sent };
}

async function load() {
  vi.resetModules();
  vi.stubEnv('VITE_DEEPER_ENABLED', 'on');
  const deeper = await import('../lib/deeper');
  const { useConversation } = await import('./useConversation');
  const { useTable } = await import('./useTable');
  return { deeper, useConversation, useTable };
}

type Room = { send: (text: string) => Promise<boolean>; error: string | null; turns: { speaker: string }[] };

async function open(kind: 'interview' | 'table'): Promise<{ result: { current: Room } }> {
  const { useConversation, useTable } = await load();
  if (kind === 'table') {
    const hook = renderHook(() => useTable());
    await act(async () => {
      await hook.result.current.convene(['a', 'b']);
    });
    return hook;
  }
  const hook = renderHook(() => useConversation());
  await act(async () => {
    await hook.result.current.begin('fix');
  });
  return hook;
}

beforeEach(() => localStorage.clear());
afterEach(() => {
  vi.unstubAllGlobals();
  vi.unstubAllEnvs();
});

describe.each(['interview', 'table'] as const)('the same question asked again (%s)', (kind) => {
  const table = kind === 'table';

  it('goes through under a new id once the first one was answered', async () => {
    const { sent } = serverWith({ table });
    const { result } = await open(kind);
    await act(async () => {
      await result.current.send('Same words');
    });
    await act(async () => {
      await result.current.send('Same words');
    });
    expect(sent).toHaveLength(2);
    expect(sent[1].id).not.toBe(sent[0].id);
    expect(result.current.error).toBeNull();
    expect(result.current.turns.filter((t) => t.speaker === 'fix')).toHaveLength(2);
  });

  it('goes through under a new id once the first one was turned away by a limit', async () => {
    const { sent } = serverWith({ table, limit: (message) => message.id === sent[0]?.id });
    const { result } = await open(kind);
    await act(async () => {
      await result.current.send('Same words');
    });
    await act(async () => {
      await result.current.send('Same words');
    });
    expect(sent[1].id).not.toBe(sent[0].id);
    expect(result.current.error).toBeNull();
  });

  it('keeps its id when the first try failed, so the retry is safe', async () => {
    const { sent } = serverWith({ table, fail: (_message, count) => count === 1 });
    const { result } = await open(kind);
    await act(async () => {
      await result.current.send('Same words');
    });
    expect(result.current.error).not.toBeNull();
    await act(async () => {
      await result.current.send('Same words');
    });
    expect(sent).toHaveLength(2);
    expect(sent[1].id).toBe(sent[0].id);
    expect(result.current.error).toBeNull();
  });

  it('is still refused as a duplicate when sent again while the first is in flight', async () => {
    let release: () => void = () => {};
    const hold = new Promise<void>((resolve) => {
      release = resolve;
    });
    const { sent } = serverWith({ table, hold });
    const { result } = await open(kind);
    let both: Promise<boolean[]> = Promise.resolve([]);
    await act(async () => {
      both = Promise.all([result.current.send('Same words'), result.current.send('Same words')]);
    });
    expect(sent).toHaveLength(2);
    expect(sent[1].id).toBe(sent[0].id);
    await act(async () => {
      release();
      await both;
    });
    expect(result.current.error).toBe(DUPLICATE);
  });
});

describe('a Table question a limit turned away', () => {
  it('goes again under a new id once a code is accepted, without the visitor retyping it', async () => {
    const { sent } = serverWith({ table: true, limit: (message) => !message.withCode });
    const { deeper, useTable } = await load();
    const { result } = renderHook(() => useTable());
    await act(async () => {
      await result.current.convene(['a', 'b']);
    });
    await act(async () => {
      await result.current.send('What did you believe?');
    });
    expect(deeper.deeperSnapshot().panelOpen).toBe(true);
    await act(async () => {
      deeper.saveCode(CODE);
    });
    await waitFor(() => expect(result.current.turns[result.current.turns.length - 1]?.speaker).toBe('fix'));
    expect(sent).toHaveLength(2);
    expect(sent[1].text).toBe('What did you believe?');
    expect(sent[1].id).not.toBe(sent[0].id);
    expect(sent[1].withCode).toBe(true);
    expect(result.current.error).toBeNull();
    expect(result.current.turns.filter((t) => t.speaker === 'participant')).toHaveLength(1);
  });

  it('is not sent again when the visitor has already sent something new', async () => {
    const { sent } = serverWith({ table: true, limit: (message) => message.text === 'First question' });
    const { deeper, useTable } = await load();
    const { result } = renderHook(() => useTable());
    await act(async () => {
      await result.current.convene(['a', 'b']);
    });
    await act(async () => {
      await result.current.send('First question');
    });
    await act(async () => {
      await result.current.send('Second question');
    });
    await act(async () => {
      deeper.saveCode(CODE);
    });
    expect(sent.map((s) => s.text)).toEqual(['First question', 'Second question']);
  });

  it('is not sent again when the round was not turned away', async () => {
    const { sent } = serverWith({ table: true });
    const { deeper, useTable } = await load();
    const { result } = renderHook(() => useTable());
    await act(async () => {
      await result.current.convene(['a', 'b']);
    });
    await act(async () => {
      await result.current.send('hello');
    });
    await act(async () => {
      deeper.saveCode(CODE);
    });
    expect(sent).toHaveLength(1);
  });
});
