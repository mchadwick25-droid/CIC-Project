import { afterEach, describe, expect, it, vi } from 'vitest';
import { ApiRequestError, sendMessage } from './api';
import type { StreamedSentence } from './streamedReply';

const DONE = {
  turn_no: 1,
  routing_action: 'voice_with_directive',
  routing_reason: 'ordinary',
  degraded: false,
  facilitator: null,
  voice: { speaker: 'fix', text: 'One. Two.', citations: [], glosses: [], figures_used: [], quote_offers: [], attempts_meta: {} },
};

function sentence(index: number, lead: string, text: string, start: number): StreamedSentence {
  return { index, lead, text, text_start: start, text_end: start + text.length, elements: [], cards: [] };
}

const ONE = sentence(0, '', 'One.', 0);
const TWO = sentence(1, ' ', 'Two.', 5);

function sse(event: string, data: unknown): string {
  return `event: ${event}\ndata: ${JSON.stringify(data)}\n\n`;
}

function streamOf(parts: string[]): Response {
  const encoder = new TextEncoder();
  const body = new ReadableStream<Uint8Array>({
    start(controller) {
      parts.forEach((part) => controller.enqueue(encoder.encode(part)));
      controller.close();
    },
  });
  return new Response(body, { status: 200, headers: { 'Content-Type': 'text/event-stream' } });
}

function mockFetch(response: Response) {
  const fetchMock = vi.fn().mockResolvedValue(response);
  vi.stubGlobal('fetch', fetchMock);
  return fetchMock;
}

afterEach(() => {
  vi.unstubAllGlobals();
});

describe('sendMessage', () => {
  it('asks for an event stream only when a sentence callback is given', async () => {
    const fetchMock = vi.fn().mockImplementation(async () => new Response(JSON.stringify(DONE), { status: 200, headers: { 'Content-Type': 'application/json' } }));
    vi.stubGlobal('fetch', fetchMock);
    await sendMessage('s', 'code', 'hi');
    expect(fetchMock.mock.calls[0][1].headers.Accept).toBeUndefined();
    await sendMessage('s', 'code', 'hi', undefined, () => {});
    expect(fetchMock.mock.calls[1][1].headers.Accept).toContain('text/event-stream');
  });

  it('passes each sentence to the callback and resolves with the finished turn', async () => {
    mockFetch(streamOf([sse('sentence', ONE), sse('sentence', TWO), sse('done', DONE)]));
    const sentences: StreamedSentence[] = [];
    const result = await sendMessage('s', 'code', 'hi', 'id', (s) => sentences.push(s));
    expect(sentences).toEqual([ONE, TWO]);
    expect(result.voice?.text).toBe('One. Two.');
  });

  it('reads an event that arrives split across network chunks', async () => {
    const whole = sse('sentence', ONE) + sse('done', DONE);
    mockFetch(streamOf([whole.slice(0, 20), whole.slice(20, 60), whole.slice(60)]));
    const sentences: StreamedSentence[] = [];
    const result = await sendMessage('s', 'code', 'hi', 'id', (s) => sentences.push(s));
    expect(sentences).toEqual([ONE]);
    expect(result.turn_no).toBe(1);
  });

  it('answers a plain JSON reply the same way, with no sentences', async () => {
    mockFetch(new Response(JSON.stringify(DONE), { status: 200, headers: { 'Content-Type': 'application/json' } }));
    const sentences: StreamedSentence[] = [];
    const result = await sendMessage('s', 'code', 'hi', 'id', (s) => sentences.push(s));
    expect(sentences).toEqual([]);
    expect(result.voice?.text).toBe('One. Two.');
  });

  it('turns an error event into the same participant-facing error as the HTTP status', async () => {
    mockFetch(streamOf([sse('sentence', ONE), sse('error', { code: 'provider_failed', status: 502, detail: 'provider call failed' })]));
    await expect(sendMessage('s', 'code', 'hi', 'id', () => {})).rejects.toMatchObject({ status: 502, detail: 'provider call failed', recoverable: false });
  });

  it('reports a stream that ends before the finished turn', async () => {
    mockFetch(streamOf([sse('sentence', ONE)]));
    await expect(sendMessage('s', 'code', 'hi', 'id', () => {})).rejects.toBeInstanceOf(ApiRequestError);
  });

  it('keeps an HTTP refusal as an HTTP refusal', async () => {
    mockFetch(new Response(JSON.stringify({ detail: 'session already closed' }), { status: 409, headers: { 'Content-Type': 'application/json' } }));
    await expect(sendMessage('s', 'code', 'hi', 'id', () => {})).rejects.toMatchObject({ status: 409, recoverable: true });
  });
});


describe('the code and the balance', () => {
  const CODE = 'ABCD2345EFGH6789JKLM';

  async function loadApi(enabled: boolean) {
    vi.resetModules();
    vi.stubEnv('VITE_DEEPER_ENABLED', enabled ? 'on' : '');
    localStorage.clear();
    const deeper = await import('./deeper');
    const api = await import('./api');
    return { deeper, api };
  }

  afterEach(() => vi.unstubAllEnvs());

  it('sends the code with every request that starts or carries a conversation, and reports the balance header', async () => {
    const { deeper, api } = await loadApi(true);
    deeper.saveCode(CODE);
    const fetchMock = vi.fn().mockImplementation(
      async () => new Response(JSON.stringify(DONE), { status: 200, headers: { 'Content-Type': 'application/json', 'X-Cic-Remaining': '4' } })
    );
    vi.stubGlobal('fetch', fetchMock);
    await api.createSession('fix');
    await api.createTableSession(['a', 'b']);
    await api.sendMessage('s', 'c', 'hello');
    await api.sendTableMessage('s', 'c', 'hello');
    await api.continueRound('s', 'c');
    for (const call of fetchMock.mock.calls) {
      expect((call[1] as RequestInit).headers).toMatchObject({ 'X-Cic-Code': CODE });
    }
    expect(deeper.remainingFromHeader('4')).toBe(4);
  });

  it('reads the balance from the stream\'s final event', async () => {
    const { deeper, api } = await loadApi(true);
    deeper.saveCode(CODE);
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(streamOf([sse('done', { ...DONE, remaining: 9 })])));
    const result = await api.sendMessage('s', 'c', 'hello', undefined, () => {});
    expect(result.voice?.text).toBe('One. Two.');
  });

  it('sends no code header when no code is held', async () => {
    const { api } = await loadApi(true);
    const fetchMock = mockFetch(new Response(JSON.stringify(DONE), { status: 200, headers: { 'Content-Type': 'application/json' } }));
    await api.sendMessage('s', 'c', 'hello');
    expect((fetchMock.mock.calls[0][1] as RequestInit).headers).not.toHaveProperty('X-Cic-Code');
  });

  it('sends no code header at all when the app is built with the module off', async () => {
    localStorage.setItem('cic_code', CODE);
    vi.resetModules();
    vi.stubEnv('VITE_DEEPER_ENABLED', '');
    const api = await import('./api');
    const fetchMock = vi.fn().mockImplementation(
      async () => new Response(JSON.stringify(DONE), { status: 200, headers: { 'Content-Type': 'application/json' } })
    );
    vi.stubGlobal('fetch', fetchMock);
    await api.sendMessage('s', 'c', 'hello');
    await api.createSession('fix');
    for (const call of fetchMock.mock.calls) {
      expect((call[1] as RequestInit).headers).not.toHaveProperty('X-Cic-Code');
    }
  });
});
