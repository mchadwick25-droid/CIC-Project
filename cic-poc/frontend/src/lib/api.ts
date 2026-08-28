/**
 * Thin client for engine/api's three endpoints (engine/api/app.py). No
 * streaming - handle_message() is one blocking call per participant
 * message, so `sendMessage` resolves with the full MessageResponse rather
 * than emitting incremental events.
 */
import type { CreateSessionResponse, MessageResponse, TableMessageResponse, TranscriptResponse, WorldListResponse } from '../types/conversation';

const API_BASE = '/api';

export class ApiRequestError extends Error {
  status: number;
  constructor(status: number, detail: string) {
    super(detail);
    this.status = status;
  }
}

async function readErrorDetail(response: Response): Promise<string> {
  try {
    const body = await response.json();
    if (typeof body?.detail === 'string') return body.detail;
  } catch {
    // not JSON - fall through
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
