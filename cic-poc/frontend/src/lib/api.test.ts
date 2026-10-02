import { afterEach, describe, expect, it, vi } from 'vitest';
import { ApiRequestError, sendMessage } from './api';

const DONE = {
  turn_no: 1,
  routing_action: 'voice_with_directive',
  routing_reason: 'ordinary',
  degraded: false,
  facilitator: null,
  voice: { speaker: 'fix', text: 'One. Two.', citations: [], glosses: [], figures_used: [], quote_offers: [], attempts_meta: {} },
};

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
  it('asks for an event stream only when a draft callback is given', async () => {
    const fetchMock = vi.fn().mockImplementation(async () => new Response(JSON.stringify(DONE), { status: 200, headers: { 'Content-Type': 'application/json' } }));
    vi.stubGlobal('fetch', fetchMock);
    await sendMessage('s', 'code', 'hi');
    expect(fetchMock.mock.calls[0][1].headers.Accept).toBeUndefined();
    await sendMessage('s', 'code', 'hi', undefined, () => {});
    expect(fetchMock.mock.calls[1][1].headers.Accept).toContain('text/event-stream');
  });

  it('passes each draft to the callback and resolves with the finished turn', async () => {
    mockFetch(streamOf([sse('draft', { text: 'One. ' }), sse('draft', { text: 'Two. ' }), sse('done', DONE)]));
    const drafts: string[] = [];
    const result = await sendMessage('s', 'code', 'hi', 'id', (text) => drafts.push(text));
    expect(drafts).toEqual(['One. ', 'Two. ']);
    expect(result.voice?.text).toBe('One. Two.');
  });

  it('reads an event that arrives split across network chunks', async () => {
    const whole = sse('draft', { text: 'One. ' }) + sse('done', DONE);
    mockFetch(streamOf([whole.slice(0, 20), whole.slice(20, 60), whole.slice(60)]));
    const drafts: string[] = [];
    const result = await sendMessage('s', 'code', 'hi', 'id', (text) => drafts.push(text));
    expect(drafts).toEqual(['One. ']);
    expect(result.turn_no).toBe(1);
  });

  it('answers a plain JSON reply the same way, with no drafts', async () => {
    mockFetch(new Response(JSON.stringify(DONE), { status: 200, headers: { 'Content-Type': 'application/json' } }));
    const drafts: string[] = [];
    const result = await sendMessage('s', 'code', 'hi', 'id', (text) => drafts.push(text));
    expect(drafts).toEqual([]);
    expect(result.voice?.text).toBe('One. Two.');
  });

  it('turns an error event into the same participant-facing error as the HTTP status', async () => {
    mockFetch(streamOf([sse('draft', { text: 'One. ' }), sse('error', { status: 502 })]));
    await expect(sendMessage('s', 'code', 'hi', 'id', () => {})).rejects.toMatchObject({ status: 502, recoverable: false });
  });

  it('reports a stream that ends before the finished turn', async () => {
    mockFetch(streamOf([sse('draft', { text: 'One. ' })]));
    await expect(sendMessage('s', 'code', 'hi', 'id', () => {})).rejects.toBeInstanceOf(ApiRequestError);
  });

  it('keeps an HTTP refusal as an HTTP refusal', async () => {
    mockFetch(new Response(JSON.stringify({ detail: 'session already closed' }), { status: 409, headers: { 'Content-Type': 'application/json' } }));
    await expect(sendMessage('s', 'code', 'hi', 'id', () => {})).rejects.toMatchObject({ status: 409, recoverable: true });
  });
});
