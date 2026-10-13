import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useTable } from './useTable';

const QUESTION = 'What did you believe?';
const REPLY = 'We did not see him ourselves. We held what his witnesses told.';
const SENTENCE = { index: 0, speaker: 'fix', lead: '', text: 'We did not see him ourselves.', text_start: 0, text_end: 29, elements: [], cards: [] };

function json(status: number, body: unknown) {
  return new Response(JSON.stringify(body), { status, headers: { 'Content-Type': 'application/json' } });
}

function droppedStream() {
  const body = new ReadableStream<Uint8Array>({
    start(controller) {
      controller.enqueue(new TextEncoder().encode(`event: sentence\ndata: ${JSON.stringify(SENTENCE)}\n\n`));
      controller.error(new TypeError('network error'));
    },
  });
  return new Response(body, { status: 200, headers: { 'Content-Type': 'text/event-stream' } });
}

// The server keeps running the round after the reader has gone: the room's
// reply is recorded, and the same message id is refused as a duplicate.
function server(recorded: { reply: boolean; roundOpen: boolean }) {
  const seen = new Set<string>();
  const sent: string[] = [];
  const transcript = () => ({
    transcript: [
      { speaker: 'participant', text: QUESTION },
      ...(recorded.reply ? [{ speaker: 'fix', text: REPLY, citations: [] }] : []),
    ],
    closed: false,
    mode: 'table',
    world_keys: ['fix', 'alx'],
    round_open: recorded.roundOpen,
    round_cap: null,
  });
  const done = { round_no: 1, round_open: false, routing_action: null, routing_reason: '', degraded: false, facilitator: [], turn_selected: null, voice: null, position: null, turn_no: null, session_closed: false };
  vi.stubGlobal(
    'fetch',
    vi.fn(async (url: string, init?: RequestInit) => {
      if (url.endsWith('/api/session') && init?.method === 'POST') return json(200, { session_id: 's', session_code: 'c', round_cap: null });
      if (url.endsWith('/transcript')) return json(200, transcript());
      if (url.endsWith('/continue')) {
        recorded.roundOpen = false;
        return json(200, done);
      }
      const id = JSON.parse(String(init?.body)).client_msg_id as string;
      sent.push(id);
      if (seen.has(id)) return json(409, { detail: 'duplicate message - already received' });
      seen.add(id);
      return droppedStream();
    })
  );
  return { sent };
}

async function convened() {
  const hook = renderHook(() => useTable());
  await act(async () => {
    await hook.result.current.convene(['fix', 'alx']);
  });
  return hook;
}

beforeEach(() => sessionStorage.clear());
afterEach(() => vi.unstubAllGlobals());

describe('a Table stream that dropped after the server had the message', () => {
  it('shows the recorded round when the same message is sent again and refused as a duplicate', async () => {
    const recorded = { reply: true, roundOpen: false };
    const { sent } = server(recorded);
    const { result } = await convened();
    await act(async () => {
      await result.current.send(QUESTION);
    });
    expect(result.current.error).not.toBeNull();

    await act(async () => {
      await result.current.send(QUESTION);
    });

    expect(sent).toHaveLength(2);
    expect(sent[1]).toBe(sent[0]);
    expect(result.current.error).toBeNull();
    expect(result.current.roundOpen).toBe(false);
    const last = result.current.turns[result.current.turns.length - 1];
    expect(last.speaker).toBe('fix');
    expect(last.text).toBe(REPLY);
    expect(result.current.turns.filter((turn) => turn.speaker === 'participant')).toHaveLength(1);
  });

  it('picks the round back up when the server left it open', async () => {
    const recorded = { reply: true, roundOpen: true };
    server(recorded);
    const { result } = await convened();
    await act(async () => {
      await result.current.send(QUESTION);
    });
    await act(async () => {
      await result.current.send(QUESTION);
    });
    expect(result.current.error).toBeNull();
    expect(result.current.roundOpen).toBe(false);
    expect(result.current.isLoading).toBe(false);
  });

  it('keeps the duplicate notice when the server has nothing for the message yet', async () => {
    const recorded = { reply: false, roundOpen: false };
    server(recorded);
    const { result } = await convened();
    await act(async () => {
      await result.current.send(QUESTION);
    });
    await act(async () => {
      await result.current.send(QUESTION);
    });
    expect(result.current.error).toBe('That message already reached the room — give it a moment.');
  });
});
