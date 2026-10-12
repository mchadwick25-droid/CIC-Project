import { act, renderHook } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { useConversation } from './useConversation';

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

// The server finishes a turn whose reader has gone: the reply is recorded
// under the message's id, and the same id is refused as a duplicate.
function server(recorded: { reply: boolean }) {
  const seen = new Set<string>();
  const transcript = (answered: boolean) => ({
    transcript: [
      { speaker: 'participant', text: QUESTION },
      ...(answered ? [{ speaker: 'fix', text: REPLY, citations: [] }] : []),
    ],
    closed: false,
    mode: 'interview',
    world_keys: null,
    round_open: false,
  });
  const sent: string[] = [];
  vi.stubGlobal(
    'fetch',
    vi.fn(async (url: string, init?: RequestInit) => {
      if (url.endsWith('/api/session')) return json(200, { session_id: 's', session_code: 'c' });
      if (url.endsWith('/transcript')) return json(200, transcript(recorded.reply));
      const id = JSON.parse(String(init?.body)).client_msg_id as string;
      sent.push(id);
      if (seen.has(id)) return json(409, { detail: 'duplicate message - already received' });
      seen.add(id);
      return droppedStream();
    })
  );
  return { sent };
}

async function started() {
  const hook = renderHook(() => useConversation());
  await act(async () => {
    await hook.result.current.begin('fix');
  });
  return hook;
}

beforeEach(() => sessionStorage.clear());
afterEach(() => vi.unstubAllGlobals());

describe('a stream that dropped after the server had the message', () => {
  it('shows the recorded reply when the same message is sent again and refused as a duplicate', async () => {
    const recorded = { reply: true };
    const { sent } = server(recorded);
    const { result } = await started();
    await act(async () => {
      await result.current.send(QUESTION);
    });
    expect(result.current.error).not.toBeNull();
    expect(result.current.streamed).toEqual([]);

    await act(async () => {
      await result.current.send(QUESTION);
    });

    expect(sent).toHaveLength(2);
    expect(sent[1]).toBe(sent[0]);
    expect(result.current.error).toBeNull();
    const last = result.current.turns[result.current.turns.length - 1];
    expect(last.speaker).toBe('fix');
    expect(last.text).toBe(REPLY);
    expect(result.current.turns.filter((turn) => turn.speaker === 'participant')).toHaveLength(1);
  });

  it('keeps the duplicate notice when the server has no reply for the message yet', async () => {
    const recorded = { reply: false };
    server(recorded);
    const { result } = await started();
    await act(async () => {
      await result.current.send(QUESTION);
    });
    await act(async () => {
      await result.current.send(QUESTION);
    });
    expect(result.current.error).toBe('That message already reached the room — give it a moment.');
    expect(result.current.turns[result.current.turns.length - 1].speaker).toBe('participant');
  });
});
