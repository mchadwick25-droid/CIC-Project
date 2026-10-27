/**
 * The person's account, as the server last said. A sign-in is a code sent to an email address,
 * proved here, with one question for a new account: are you 18 or over. The session cookie is set by
 * the server and cannot be read here. With VITE_ACCOUNTS_ENABLED not "on" nothing in this file runs:
 * no control, no request, no listener. A request to the account routes never logs an address or a code.
 */
import { useSyncExternalStore } from 'react';
import { prepare, type Provider } from './providerScripts';
import { clearStored, readStored, writeStored } from './sessionStore';

export type { Provider };

export const accountsEnabled = import.meta.env.VITE_ACCOUNTS_ENABLED === 'on';

const BASE = '/api/accounts';
const RESOURCES_FIRST_KEY = 'cic_resources_first';
const SHELF_OPEN_KEY = 'cic_shelf_open';

export interface Balance {
  free_left: number;
  free_total: number;
  refill_on: string;
  codes_held: number;
  code_tokens: number;
  // The tokens still unspent on each gift coupon the account holds.
  gifts?: number[];
}

export interface ShelfItem {
  session_id: string;
  mode: 'interview' | 'table';
  worlds: string[];
  world_keys: string[];
  title: string;
  started: string | null;
  last_active: string | null;
  turns: number;
  closed: boolean;
  holds_crisis_turn: boolean;
  saved: boolean;
}

export interface AccountState {
  // 'unknown' until the first answer; 'off' when the server has no accounts; 'out' and 'in' otherwise.
  status: 'unknown' | 'off' | 'out' | 'in';
  balance: Balance | null;
  shelf: ShelfItem[] | null;
  // The sign-in steps inside the Get more conversations panel, and the home page.
  signInOpen: boolean;
  homeOpen: boolean;
  refillDay: number | null;
  // Whether the conversation last opened went on the shelf (null when signed out or not yet known).
  lastShelved: boolean | null;
  recoveryPending: string | null;
  // How the person signs in now: 'address', 'google', 'apple'.
  methods: string[];
  hasRecoveryCode: boolean;
  // The providers this server has turned on, each with our app's public id there.
  providers: Record<string, string>;
  // The sizes of gift coupons that attached at the sign-in just made, until the person dismisses the notice.
  giftNotice: number[];
  // A sign-in just finished, so a code this browser already holds is offered to the account once.
  savedCodeOffer: boolean;
  // The last day to re-open an account just deleted in this tab, until the person leaves that notice.
  closedNotice: string | null;
}

export class AccountsError extends Error {
  status: number;
  constructor(status: number, message: string) {
    super(message);
    this.status = status;
  }
}

let state: AccountState = { status: 'unknown', balance: null, shelf: null, signInOpen: false, homeOpen: false, refillDay: null, lastShelved: null, recoveryPending: null, methods: [], hasRecoveryCode: false, providers: {}, giftNotice: [], savedCodeOffer: false, closedNotice: null };
const listeners = new Set<() => void>();

function set(next: Partial<AccountState>) {
  state = { ...state, ...next };
  listeners.forEach((l) => l());
}

export function useAccount(): AccountState {
  return useSyncExternalStore(
    (listener) => {
      listeners.add(listener);
      return () => listeners.delete(listener);
    },
    () => state,
  );
}

export function openSignIn() {
  set({ signInOpen: true });
  if (state.status === 'unknown') void refresh();
  void loadProviders();
}
export function closeSignIn() {
  set({ signInOpen: false });
}
export function openHome() {
  set({ homeOpen: true, signInOpen: false });
  if (state.status === 'unknown') void refresh();
  void loadProviders();
}
export function dismissGiftNotice() {
  set({ giftNotice: [] });
}

export function dismissSavedCodeOffer() {
  set({ savedCodeOffer: false });
}
export function closeHome() {
  set({ homeOpen: false, closedNotice: null });
}

async function call(path: string, init?: { method?: 'GET' | 'POST'; body?: unknown }): Promise<Record<string, unknown>> {
  const post = init?.method === 'POST';
  let response: Response;
  try {
    response = await fetch(`${BASE}${path}`, {
      method: init?.method ?? 'GET',
      headers: post ? { 'Content-Type': 'application/json', 'x-cic-accounts': '1' } : undefined,
      body: post ? JSON.stringify(init?.body ?? {}) : undefined,
    });
  } catch {
    throw new AccountsError(0, '');
  }
  let body: Record<string, unknown> = {};
  try {
    body = await response.json();
  } catch {
    // An empty or unreadable body is treated as no detail.
  }
  if (!response.ok) {
    const detail = typeof body.detail === 'string' ? body.detail : '';
    if (response.status === 401) set({ status: 'out', balance: null, shelf: null });
    throw new AccountsError(response.status, detail);
  }
  return body;
}

/** Reads who is signed in. A 404 means this server has no accounts, and every control stays hidden. */
export async function refresh(): Promise<void> {
  if (!accountsEnabled) return;
  try {
    const me = await call('/me');
    if (me.signed_in !== true) {
      set({ status: 'out', balance: null, shelf: null, recoveryPending: null, methods: [], hasRecoveryCode: false, refillDay: null });
      return;
    }
    const pending = me.recovery_pending as { effective_on?: string } | null;
    set({
      status: 'in',
      recoveryPending: pending?.effective_on ?? null,
      methods: Array.isArray(me.sign_in_methods) ? me.sign_in_methods.filter((m): m is string => typeof m === 'string') : [],
      hasRecoveryCode: me.has_recovery_code === true,
      refillDay: typeof me.refill_day === 'number' ? me.refill_day : null,
    });
    await loadBalance();
  } catch (error) {
    if (error instanceof AccountsError && error.status === 404) set({ status: 'off' });
    else if (state.status === 'unknown') set({ status: 'out' });
  }
}

async function loadBalance(): Promise<void> {
  try {
    const body = await call('/balance');
    if (body.signed_in === true && body.available === true) set({ balance: body as unknown as Balance });
  } catch {
    // The strip simply shows less.
  }
}

export async function loadShelf(): Promise<void> {
  const body = await call('/shelf');
  set({ shelf: (body.conversations as ShelfItem[]) ?? [] });
}

export type SignInResult =
  | { kind: 'ok'; newAccount: boolean; coupons: number[] }
  | { kind: 'ask_age'; message: string }
  | { kind: 'not_adult'; message: string }
  | { kind: 'waiting'; message: string; effectiveOn: string }
  | { kind: 'closed'; message: string; eraseOn: string };

export async function startSignIn(address: string): Promise<string> {
  const body = await call('/sign-in/start', { method: 'POST', body: { address } });
  return String(body.challenge);
}

export async function finishSignIn(challenge: string, address: string, code: string, over18?: boolean, reopen?: boolean): Promise<SignInResult> {
  const body = await call('/sign-in/finish', {
    method: 'POST',
    body: {
      challenge, address, code,
      ...(over18 === undefined ? {} : { over_18: over18 }),
      ...(reopen === undefined ? {} : { reopen }),
    },
  });
  return settleSignIn(body);
}

async function settleSignIn(body: Record<string, unknown>): Promise<SignInResult> {
  if (body.status === 'ok') {
    await refresh();
    await carryConversation();
    const coupons = Array.isArray(body.coupons) ? body.coupons.filter((n): n is number => Number.isInteger(n) && n > 0) : [];
    if (coupons.length > 0) set({ giftNotice: coupons });
    set({ savedCodeOffer: true });
    return { kind: 'ok', newAccount: body.new_account === true, coupons };
  }
  const message = typeof body.message === 'string' ? body.message : '';
  if (body.status === 'needs_age_answer') return { kind: 'ask_age', message };
  if (body.status === 'account_closed') return { kind: 'closed', message, eraseOn: String(body.erase_on ?? '') };
  if (body.status === 'recovery_waiting') return { kind: 'waiting', message, effectiveOn: String(body.effective_on ?? '') };
  return { kind: 'not_adult', message };
}

export function readStoredConversation(): boolean {
  return readStored() !== null;
}

/** The conversation open in this tab goes on the shelf when someone signs in, so it comes with them. */
async function carryConversation(): Promise<void> {
  const stored = readStored();
  if (!stored) return;
  try {
    await shelveCurrent(stored.sessionId, stored.sessionCode);
    set({ lastShelved: true });
  } catch {
    set({ lastShelved: false });
  }
}

export async function signOut(): Promise<void> {
  let leaveShelved = false;
  try {
    await call('/sign-out', { method: 'POST' });
  } finally {
    set({ status: 'out', balance: null, shelf: null, recoveryPending: null, methods: [], hasRecoveryCode: false, refillDay: null, homeOpen: false, lastShelved: null });
    leaveShelved = forgetShelvedConversation();
  }
  if (leaveShelved) window.location.reload();
}

/** A conversation opened from the shelf does not stay in this tab once its owner signs out. */
function forgetShelvedConversation(): boolean {
  try {
    const opened = sessionStorage.getItem(SHELF_OPEN_KEY);
    sessionStorage.removeItem(SHELF_OPEN_KEY);
    sessionStorage.removeItem(RESOURCES_FIRST_KEY);
    if (opened && readStored()?.sessionId === opened) {
      clearStored();
      return true;
    }
  } catch {
    // Without storage there is nothing held here.
  }
  return false;
}

export async function attachCode(code: string): Promise<void> {
  await call('/codes/attach', { method: 'POST', body: { code } });
  await loadBalance();
}

/** A code just saved on this device is added to the account when someone is signed in. Never fails the caller. */
export async function attachIfSignedIn(code: string): Promise<void> {
  if (!accountsEnabled || state.status !== 'in') return;
  try {
    await attachCode(code);
  } catch {
    // The code still works from this device.
  }
}

/** Puts the conversation open in this browser on the shelf, with the code it was opened with. */
async function shelveCurrent(sessionId: string, sessionCode: string): Promise<void> {
  await call('/shelf/add', { method: 'POST', body: { session_id: sessionId, session_code: sessionCode } });
}

export function noteShelved(shelved: boolean | null | undefined) {
  if (accountsEnabled) set({ lastShelved: shelved ?? null });
}

/** Opens a shelved conversation: stores it as this tab's conversation and reloads, so the app picks it up. */
export async function openShelved(item: ShelfItem): Promise<void> {
  const body = await call('/shelf/reopen', { method: 'POST', body: { session_id: item.session_id } });
  const stored =
    item.mode === 'table'
      ? { sessionId: item.session_id, sessionCode: String(body.session_code), mode: 'table' as const, worldKeys: item.world_keys }
      : { sessionId: item.session_id, sessionCode: String(body.session_code), mode: 'interview' as const, worldKey: item.world_keys[0] };
  writeStored(stored);
  try {
    sessionStorage.setItem(SHELF_OPEN_KEY, item.session_id);
    if (typeof body.resources_text === 'string' && body.resources_text) {
      sessionStorage.setItem(RESOURCES_FIRST_KEY, JSON.stringify({ sessionId: item.session_id, text: body.resources_text }));
    } else sessionStorage.removeItem(RESOURCES_FIRST_KEY);
  } catch {
    // Without storage the line is simply not pinned; the transcript still holds it.
  }
  window.location.reload();
}

/** The stored Facilitator text to pin first, when this tab's conversation was reopened from the shelf and holds one. */
export function resourcesFirst(sessionId: string | null): string | null {
  if (!sessionId) return null;
  try {
    const raw = sessionStorage.getItem(RESOURCES_FIRST_KEY);
    const held = raw ? (JSON.parse(raw) as { sessionId?: unknown; text?: unknown }) : null;
    return held && held.sessionId === sessionId && typeof held.text === 'string' ? held.text : null;
  } catch {
    return null;
  }
}

export async function deleteShelved(sessionId: string): Promise<void> {
  await call('/shelf/delete', { method: 'POST', body: { session_id: sessionId } });
  set({ shelf: (state.shelf ?? []).filter((c) => c.session_id !== sessionId) });
}

export async function startStepUp(address: string): Promise<string> {
  const body = await call('/step-up/start', { method: 'POST', body: { address } });
  return String(body.challenge);
}

export async function finishStepUp(challenge: string, code: string): Promise<void> {
  await call('/step-up/finish', { method: 'POST', body: { challenge, code } });
}

/** The account's data as a file download. Needs a fresh step-up. */
export async function exportData(): Promise<void> {
  const body = await call('/export', { method: 'POST' });
  const blob = new Blob([JSON.stringify(body, null, 2)], { type: 'application/json' });
  const url = URL.createObjectURL(blob);
  const link = document.createElement('a');
  link.href = url;
  link.download = 'my-conversations-data.json';
  document.body.appendChild(link);
  link.click();
  link.remove();
  URL.revokeObjectURL(url);
}

export async function deleteAccount(): Promise<void> {
  const body = await call('/delete', { method: 'POST' });
  clearStored();
  forgetShelvedConversation();
  set({ status: 'out', balance: null, shelf: null, recoveryPending: null, methods: [], hasRecoveryCode: false, refillDay: null, homeOpen: true, lastShelved: null, closedNotice: typeof body.erase_on === 'string' ? body.erase_on : '' });
}

/** Which providers the server has turned on. Our own server only; no provider script is touched. */
async function loadProviders(): Promise<void> {
  if (!accountsEnabled) return;
  try {
    const body = await call('/providers');
    const listed = (body.providers ?? {}) as Record<string, unknown>;
    const ids: Record<string, string> = {};
    for (const name of ['google', 'apple']) if (typeof listed[name] === 'string' && listed[name]) ids[name] = listed[name] as string;
    set({ providers: ids });
  } catch {
    set({ providers: {} });
  }
}

export interface ProviderToken {
  provider: Provider;
  id_token: string;
  nonce: string;
}

/** Asks our server for a one-use nonce and readies the provider's script for it. Returns the nonce. */
export async function prepareProvider(provider: Provider): Promise<string> {
  const clientId = state.providers[provider];
  if (!clientId) throw new AccountsError(404, '');
  const started = await call('/provider/start', { method: 'POST' });
  const nonce = String(started.nonce);
  try {
    await prepare(provider, clientId, nonce);
  } catch {
    throw new AccountsError(0, '');
  }
  return nonce;
}

export async function providerSignIn(token: ProviderToken, over18?: boolean, reopen?: boolean): Promise<SignInResult> {
  const body = await call('/provider/finish', {
    method: 'POST',
    body: {
      ...token,
      ...(over18 === undefined ? {} : { over_18: over18 }),
      ...(reopen === undefined ? {} : { reopen }),
    },
  });
  return settleSignIn(body);
}

export async function providerStepUp(token: ProviderToken): Promise<void> {
  await call('/step-up/provider', { method: 'POST', body: token });
}

export async function providerLink(token: ProviderToken): Promise<void> {
  await call('/provider/link', { method: 'POST', body: token });
  await refresh();
}

export async function providerUnlink(provider: Provider): Promise<void> {
  await call('/provider/unlink', { method: 'POST', body: { provider } });
  await refresh();
}

export async function startAddressChange(newAddress: string): Promise<string> {
  const body = await call('/address/start', { method: 'POST', body: { new_address: newAddress } });
  return String(body.challenge);
}

export async function finishAddressChange(challenge: string, code: string, newAddress: string): Promise<void> {
  await call('/address/finish', { method: 'POST', body: { challenge, code, new_address: newAddress } });
  await refresh();
}

/** Makes a new recovery code. It is shown once and not kept here. */
export async function makeRecoveryCode(): Promise<string> {
  const body = await call('/recovery/code', { method: 'POST' });
  await refresh();
  return String(body.recovery_code);
}

export async function startRecovery(recoveryCode: string, newAddress: string): Promise<string> {
  const body = await call('/recovery/start', { method: 'POST', body: { recovery_code: recoveryCode, new_address: newAddress } });
  return String(body.challenge);
}

export async function finishRecovery(challenge: string, code: string, newAddress: string): Promise<{ recoveryCode: string; effectiveOn: string }> {
  const body = await call('/recovery/finish', { method: 'POST', body: { challenge, code, new_address: newAddress } });
  return { recoveryCode: String(body.recovery_code), effectiveOn: String(body.effective_on) };
}

export async function cancelRecovery(address: string, cancelCode: string): Promise<void> {
  await call('/recovery/cancel', { method: 'POST', body: { address, cancel_code: cancelCode } });
}

export async function cancelRecoverySignedIn(): Promise<void> {
  await call('/recovery/cancel-signed-in', { method: 'POST' });
  await refresh();
}

export async function signOutEverywhere(): Promise<void> {
  try {
    await call('/sign-out-everywhere', { method: 'POST' });
  } finally {
    set({ status: 'out', balance: null, shelf: null, recoveryPending: null, methods: [], hasRecoveryCode: false, refillDay: null, homeOpen: false, lastShelved: null, giftNotice: [], savedCodeOffer: false });
    if (forgetShelvedConversation()) window.location.reload();
  }
}

/** For tests: back to the first state. */
export function resetAccountsForTest() {
  state = { status: 'unknown', balance: null, shelf: null, signInOpen: false, homeOpen: false, refillDay: null, lastShelved: null, recoveryPending: null, methods: [], hasRecoveryCode: false, providers: {}, giftNotice: [], savedCodeOffer: false, closedNotice: null };
  listeners.forEach((l) => l());
}
