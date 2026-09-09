/**
 * Thin client for engine/api's three endpoints (engine/api/app.py). No
 * streaming - handle_message() is one blocking call per participant
 * message, so `sendMessage` resolves with the full MessageResponse rather
 * than emitting incremental events.
 */
import type { CreateSessionResponse, MessageResponse, TableMessageResponse, TranscriptResponse, WorldListResponse } from '../types/conversation';

const API_BASE = '/api';

/**
 * The error-language layer (2026-08-28 foundation audit): eleven raw
 * backend strings could reach a participant verbatim - "invalid session",
 * "provider call failed", "Bad Gateway". The Facilitator's own prose is
 * careful and warm; the error layer was a different register from a
 * different author, and it was the register a participant met on a bad
 * day. Every message below is participant-facing prose, inventoried in
 * the decision log for Mark's read. The raw detail is preserved on
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
    // recoverable: true (2026-09-04) - was false, which left a live bug
    // with no clickable remedy but "Leave for now" (see App.tsx's
    // isEmbedded handling of onRestart/onEnd for why that used to be its
    // own dead end too). The message already promises "try again in a
    // moment" is the honest remedy; the affordance should match it.
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
    headers: { 'Content-Type': 'application/json' },
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
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ world_keys: worldKeys }),
  });
  if (!response.ok) {
    throw new ApiRequestError(response.status, await readErrorDetail(response));
  }
  return response.json();
}

// Advance the open table round by one voice turn (Artifact-7 SS6's
// turn-at-a-time transport) - called repeatedly while round_open is true,
// so each voice's words reach the participant as they land rather than
// after the whole round.
export async function continueRound(sessionId: string, sessionCode: string): Promise<TableMessageResponse> {
  const response = await fetch(`${API_BASE}/session/${sessionId}/continue`, {
    method: 'POST',
    headers: { ...authHeader(sessionCode) },
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
  const response = await fetch(`${API_BASE}/session/${sessionId}/message`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...authHeader(sessionCode) },
    body: JSON.stringify({ text, client_msg_id: clientMsgId }),
  });
  if (!response.ok) {
    throw new ApiRequestError(response.status, await readErrorDetail(response));
  }
  return response.json();
}

export async function sendMessage(
  sessionId: string,
  sessionCode: string,
  text: string,
  clientMsgId?: string
): Promise<MessageResponse> {
  const response = await fetch(`${API_BASE}/session/${sessionId}/message`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json', ...authHeader(sessionCode) },
    body: JSON.stringify({ text, client_msg_id: clientMsgId }),
  });
  if (!response.ok) {
    throw new ApiRequestError(response.status, await readErrorDetail(response));
  }
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
