/**
 * Thin client for engine/api's endpoints (engine/api/app.py). `sendMessage`
 * resolves with the full MessageResponse. Given an `onSentence` callback it
 * also asks for the reply as an event stream: each "sentence" event is the
 * next sentence of the reply, with its marks, as the voice finishes it, and
 * the resolved MessageResponse is still the finished turn, whose plan is
 * authoritative. A server that answers with plain JSON is handled the same
 * way, with no sentences.
 */
import { codeHeaders, currentCode, remainingFromHeader, reportBalance } from './deeper';
import type { CreateSessionResponse, MessageResponse, TableMessageResponse, TranscriptResponse, WorldListResponse } from '../types/conversation';
import type { StreamedSentence } from './streamedReply';

const API_BASE = '/api';

/**
 * The error-language layer: eleven raw backend strings could reach a
 * participant verbatim - "invalid session", "provider call failed", "Bad
 * Gateway". The Facilitator's own prose is careful and warm; the error
 * layer was a different register from a different author, and it was the
 * register a participant met on a bad day. Every message below is
 * rewritten as participant-facing prose. The raw detail is preserved on
 * `.detail` and logged to the console for diagnosis - it just never
 * becomes the sentence a person reads.
 *
 * `recoverable` marks the errors whose honest remedy is starting fresh
 * (a restarted server, a closed session) - the screens render a
 * begin-again affordance for exactly these, so no error is ever a dead
 * end.
 */
function participantMessage(status: number, detail: string): { message: string; recoverable: boolean } {
  if (status === 401) {
    return {
      message: 'This conversation has slipped away from us — the server was restarted, and nothing you said caused it. You can begin a new one.',
      recoverable: true,
    };
  }
  if (status === 409 && detail.includes('already closed')) {
    return { message: "This conversation has closed. You're welcome to begin a new one.", recoverable: true };
  }
  if (status === 409 && detail.includes('round still open')) {
    return { message: 'The table is still finishing its round — let it speak, then ask again.', recoverable: false };
  }
  if (status === 409 && detail.includes('duplicate message')) {
    return { message: 'That message already reached the room — give it a moment.', recoverable: false };
  }
  if (status === 409 && detail.includes('advance already in flight')) {
    return { message: 'The table is already speaking — one moment.', recoverable: false };
  }
  if (status === 429) {
    // The server already speaks to the participant here (engine/api/ratelimit.py).
    return { message: detail, recoverable: false };
  }
  if (status === 502) {
    return { message: "The voice couldn't be reached just now. Give it a moment, then send again.", recoverable: false };
  }
  if (status === 503) {
    // recoverable: true, so the retry affordance matches the message's
    // own promise ("try again in a moment") instead of leaving only
    // "Leave for now" (see App.tsx's isEmbedded handling of
    // onRestart/onEnd).
    return { message: "This world's records are briefly unavailable — try again in a moment.", recoverable: true };
  }
  return { message: "That didn't go through. Try again in a moment, or begin a new conversation.", recoverable: false };
}

export class ApiRequestError extends Error {
  status: number;
  detail: string;
  recoverable: boolean;
  constructor(status: number, detail: string) {
    const { message, recoverable } = participantMessage(status, detail);
    super(message);
    this.status = status;
    this.detail = detail;
    this.recoverable = recoverable;
    console.warn(`api error ${status}: ${detail}`);
  }
}

async function readErrorDetail(response: Response): Promise<string> {
  try {
    const body = await response.json();
    if (typeof body?.detail === 'string') return body.detail;
  } catch {
    // not JSON - Render's proxy answers with HTML on cold starts and
    // gateway timeouts, which is exactly when a participant most needs a
    // human sentence instead of "Bad Gateway".
  }
  return response.statusText || `HTTP ${response.status}`;
}

function authHeader(sessionCode: string): Record<string, string> {
  return { Authorization: `Session ${sessionCode}` };
}

export async function createSession(worldKey: string): Promise<CreateSessionResponse> {
  const response = await fetch(`${API_BASE}/session`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...codeHeaders() },
    body: JSON.stringify({ world_key: worldKey }),
  });
  if (!response.ok) {
    throw new ApiRequestError(response.status, await readErrorDetail(response));
  }
  return response.json();
}

// 2-3 distinct world keys convene a table session (Artifact-7 SS1/SS6) -
// the ONLY way a table starts; nothing auto-creates one from a deep link.
export async function createTableSession(worldKeys: string[]): Promise<CreateSessionResponse> {
  const response = await fetch(`${API_BASE}/session`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...codeHeaders() },
    body: JSON.stringify({ world_keys: worldKeys }),
  });
  if (!response.ok) {
    throw new ApiRequestError(response.status, await readErrorDetail(response));
  }
  return response.json();
}

// The participant's own deletion request: the server removes the
// conversation now (204), or refuses with the usual 401 for a wrong code.
export async function deleteSession(sessionId: string, sessionCode: string): Promise<void> {
  const response = await fetch(`${API_BASE}/session/${sessionId}`, {
    method: 'DELETE',
    headers: { ...authHeader(sessionCode) },
  });
  if (!response.ok) {
    throw new ApiRequestError(response.status, await readErrorDetail(response));
  }
}

// Advance the open table round by one voice turn (Artifact-7 SS6's
// turn-at-a-time transport) - called repeatedly while round_open is true,
// so each voice's words reach the participant as they land rather than
// after the whole round.
export async function continueRound(sessionId: string, sessionCode: string): Promise<TableMessageResponse> {
  const response = await fetch(`${API_BASE}/session/${sessionId}/continue`, {
    method: 'POST',
    headers: { ...authHeader(sessionCode), ...codeHeaders() },
  });
  if (!response.ok) {
    throw new ApiRequestError(response.status, await readErrorDetail(response));
  }
  return response.json();
}

export async function sendTableMessage(
  sessionId: string,
  sessionCode: string,
  text: string,
  clientMsgId?: string
): Promise<TableMessageResponse> {
  const sentWith = currentCode();
  const response = await fetch(`${API_BASE}/session/${sessionId}/message`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...authHeader(sessionCode), ...codeHeaders() },
    body: JSON.stringify({ text, client_msg_id: clientMsgId }),
  });
  if (!response.ok) {
    throw new ApiRequestError(response.status, await readErrorDetail(response));
  }
  reportBalance(sentWith, remainingFromHeader(response.headers.get('X-Cic-Remaining')), response.headers.get('X-Cic-Low') === '1');
  return response.json();
}

interface StreamEvent {
  event: string;
  data: unknown;
}

function parseStreamBlock(block: string): StreamEvent | null {
  let event = 'message';
  const data: string[] = [];
  for (const line of block.split('\n')) {
    if (line.startsWith('event:')) event = line.slice(6).trim();
    else if (line.startsWith('data:')) data.push(line.slice(5).trimStart());
  }
  if (data.length === 0) return null;
  return { event, data: JSON.parse(data.join('\n')) };
}

async function readMessageStream(response: Response, onSentence: (sentence: StreamedSentence) => void, sentWith: string | null): Promise<MessageResponse> {
  if (!response.body) throw new ApiRequestError(502, 'the reply stream had no body');
  const reader = response.body.getReader();
  const decoder = new TextDecoder();
  let buffer = '';
  for (;;) {
    const { done, value } = await reader.read();
    buffer += decoder.decode(value, { stream: !done });
    let boundary = buffer.indexOf('\n\n');
    while (boundary !== -1) {
      const parsed = parseStreamBlock(buffer.slice(0, boundary));
      buffer = buffer.slice(boundary + 2);
      if (parsed?.event === 'sentence') onSentence(parsed.data as StreamedSentence);
      else if (parsed?.event === 'done') {
        const done = parsed.data as MessageResponse & { remaining?: number; low?: boolean };
        reportBalance(sentWith, typeof done.remaining === 'number' ? done.remaining : null, done.low === true);
        return done;
      }
      else if (parsed?.event === 'error') {
        const failure = parsed.data as { code: string; status: number; detail: string };
        throw new ApiRequestError(failure.status, failure.detail);
      }
      boundary = buffer.indexOf('\n\n');
    }
    if (done) throw new ApiRequestError(502, 'the reply stream ended before the reply finished');
  }
}

export async function sendMessage(
  sessionId: string,
  sessionCode: string,
  text: string,
  clientMsgId?: string,
  onSentence?: (sentence: StreamedSentence) => void
): Promise<MessageResponse> {
  const sentWith = currentCode();
  const response = await fetch(`${API_BASE}/session/${sessionId}/message`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      ...(onSentence ? { Accept: 'text/event-stream, application/json;q=0.9' } : {}),
      ...authHeader(sessionCode),
      ...codeHeaders(),
    },
    body: JSON.stringify({ text, client_msg_id: clientMsgId }),
  });
  if (!response.ok) {
    throw new ApiRequestError(response.status, await readErrorDetail(response));
  }
  if (onSentence && (response.headers.get('content-type') ?? '').startsWith('text/event-stream')) {
    return readMessageStream(response, onSentence, sentWith);
  }
  reportBalance(sentWith, remainingFromHeader(response.headers.get('X-Cic-Remaining')), response.headers.get('X-Cic-Low') === '1');
  return response.json();
}

export async function getWorlds(): Promise<WorldListResponse> {
  const response = await fetch(`${API_BASE}/worlds`);
  if (!response.ok) {
    throw new ApiRequestError(response.status, await readErrorDetail(response));
  }
  return response.json();
}

export async function getTranscript(sessionId: string, sessionCode: string): Promise<TranscriptResponse> {
  const response = await fetch(`${API_BASE}/session/${sessionId}/transcript`, {
    headers: authHeader(sessionCode),
  });
  if (!response.ok) {
    throw new ApiRequestError(response.status, await readErrorDetail(response));
  }
  return response.json();
}
