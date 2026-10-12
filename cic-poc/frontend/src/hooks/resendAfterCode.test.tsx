import { act, renderHook, waitFor } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

const CODE = '2345 6789 ABCD EFGH JKLM';
const NOTE = { key: 'spent', text: 'A line.' };

interface Sent {
  text: string;
  id: string;
  withCode: boolean;
}

function json(status: number, body: unknown) {
  return new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json' } });
}

function serverWith(options: { refuse: (sent: Sent) => 'limit' | 'safety' | null }) {
  const seen = new Set<string>();
  const sent: Sent[] = [];
  const fetchMock = vi.fn(async (url: string, init?: RequestInit) => {
    if (url.endsWith('/api/session')) return json(200, { session_id: 's', session_code: 'c' });
    if (url.endsWith('/transcript')) return json(200, { transcript: [], closed: false, mode: 'interview', world_keys: null, round_open: false });
    if (url.endsWith('/api/deeper/balance')) return json(200, { remaining: 100 });
    const body = JSON.parse(String(init?.body));
    const headers = init?.headers as Record<string, string>;
    const message: Sent = { text: body.text, id: body.client_msg_id, withCode: 'X-Cic-Code' in headers };
    sent.push(message);
    if (seen.has(message.id)) return json(409, { detail: 'duplicate message - already received' });
    seen.add(message.id);
    const refusal = options.refuse(message);
    if (refusal === 'limit') return json(200, { facilitator: { kind: 'limit', text: 'Paused.' }, voice: null, limit_note: NOTE });
    if (refusal === 'safety') return json(200, { facilitator: { kind: 'check_in', text: 'Are you all right?' }, voice: null, limit_note: null });
    return json(200, { facilitator: null, voice: { speaker: 'fix', text: 'An answer.', citations: [] }, limit_note: null });
  });
  vi.stubGlobal('fetch', fetchMock);
  return { sent };
}

async function load() {
  vi.resetModules();
  vi.stubEnv('VITE_DEEPER_ENABLED', 'on');
  const deeper = await import('../lib/deeper');
  const { useConversation } = await import('./useConversation');
  return { deeper, useConversation };
}

async function started(useConversation: typeof import('./useConversation').useConversation) {
  const hook = renderHook(() => useConversation());
  await act(async () => {
    await hook.result.current.begin('fix');
  });
  return hook;
}

const limitWithoutCode = (sent: Sent) => (sent.withCode ? null : 'limit');

beforeEach(() => localStorage.clear());
afterEach(() => {
  vi.unstubAllGlobals();
  vi.unstubAllEnvs();
});

describe('a question the limit turned away', () => {
  it('goes again under a new id once a code is accepted, without the visitor retyping it', async () => {
    const { sent } = serverWith({ refuse: limitWithoutCode });
    const { deeper, useConversation } = await load();
    const { result } = await started(useConversation);
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
    const { sent } = serverWith({ refuse: (message) => (message.text === 'First question' ? 'limit' : null) });
    const { deeper, useConversation } = await load();
    const { result } = await started(useConversation);
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

  it('is not sent again when the turn was a safety check-in', async () => {
    const { sent } = serverWith({ refuse: () => 'safety' });
    const { deeper, useConversation } = await load();
    const { result } = await started(useConversation);
    await act(async () => {
      await result.current.send('hello');
    });
    await act(async () => {
      deeper.saveCode(CODE);
    });
    expect(sent).toHaveLength(1);
  });

  it('is sent only once, however many later renders there are', async () => {
    const { sent } = serverWith({ refuse: limitWithoutCode });
    const { deeper, useConversation } = await load();
    const { result, rerender } = await started(useConversation);
    await act(async () => {
      await result.current.send('Once');
    });
    await act(async () => {
      deeper.saveCode(CODE);
    });
    await waitFor(() => expect(sent).toHaveLength(2));
    rerender();
    expect(sent).toHaveLength(2);
  });
});

describe('a genuine double send', () => {
  it('is still refused by the server and still shows its line', async () => {
    const { sent } = serverWith({ refuse: () => null });
    const { useConversation } = await load();
    const { result } = await started(useConversation);
    await act(async () => {
      await result.current.send('Same words');
    });
    await act(async () => {
      await result.current.send('Same words');
    });
    expect(sent).toHaveLength(2);
    expect(sent[1].id).toBe(sent[0].id);
    expect(result.current.error).toBe('That message already reached the room — give it a moment.');
  });
});
