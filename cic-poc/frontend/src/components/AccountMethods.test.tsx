import { act, cleanup, fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

type Reply = { status?: number; body?: unknown };
type Call = { path: string; method: string; body: Record<string, unknown> | null };

function serve(routes: Record<string, Reply | ((body: Record<string, unknown> | null) => Reply)>) {
  const calls: Call[] = [];
  vi.stubGlobal(
    'fetch',
    vi.fn(async (url: string, init: RequestInit = {}) => {
      const path = String(url).replace('/api/accounts', '');
      const body = init.body ? (JSON.parse(String(init.body)) as Record<string, unknown>) : null;
      calls.push({ path, method: init.method ?? 'GET', body });
      const hit = routes[path];
      const reply = typeof hit === 'function' ? hit(body) : hit;
      if (!reply) return new Response(JSON.stringify({ detail: 'x' }), { status: 404 });
      return new Response(JSON.stringify(reply.body ?? {}), { status: reply.status ?? 200 });
    })
  );
  return calls;
}

const prepare = vi.fn(async (..._args: unknown[]) => undefined);
const renderGoogleButton = vi.fn((_el: HTMLElement, done: (credential: string | null) => void) => done('token-1'));
const appleSignIn = vi.fn(async () => 'token-1');

async function load() {
  vi.resetModules();
  vi.stubEnv('VITE_ACCOUNTS_ENABLED', 'on');
  vi.doMock('../lib/providerScripts', () => ({ prepare, renderGoogleButton, appleSignIn }));
  const { AccountPanel } = await import('./AccountPanel');
  const accounts = await import('../lib/accounts');
  const { accountsCopy } = await import('../lib/accountsCopy');
  return { AccountPanel, accounts, copy: accountsCopy };
}

const BALANCE = { signed_in: true, available: true, free_left: 5, free_total: 10, refill_on: '', codes_held: 0, code_tokens: 0 };
const panel = () => within(screen.getByRole('complementary'));

beforeEach(() => {
  localStorage.clear();
  sessionStorage.clear();
  prepare.mockClear();
  renderGoogleButton.mockClear();
  appleSignIn.mockClear();
});
afterEach(() => {
  cleanup();
  vi.unstubAllEnvs();
  vi.unstubAllGlobals();
  vi.doUnmock('../lib/providerScripts');
});

describe('provider sign-in', () => {
  it('shows a button only for a provider the server has on, and loads no script until it is pressed', async () => {
    const calls = serve({
      '/me': { body: { signed_in: false } },
      '/providers': { body: { providers: { google: 'g-client' } } },
      '/provider/start': { body: { status: 'ok', nonce: 'n1' } },
      '/provider/finish': { body: { status: 'ok', new_account: false } },
      '/balance': { body: BALANCE },
    });
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.signIn }));
    const google = await screen.findByRole('button', { name: copy.continueWith('Google') });
    expect(screen.queryByRole('button', { name: copy.continueWith('Apple') })).not.toBeInTheDocument();
    expect(prepare).not.toHaveBeenCalled();
    fireEvent.click(google);
    await waitFor(() => expect(calls.some((c) => c.path === '/provider/finish')).toBe(true));
    expect(prepare).toHaveBeenCalledWith('google', 'g-client', 'n1');
    expect(calls.find((c) => c.path === '/provider/finish')!.body).toMatchObject({ provider: 'google', id_token: 'token-1', nonce: 'n1' });
  });

  it('asks the age question for a new account and sends the same token with the answer', async () => {
    const calls = serve({
      '/me': { body: { signed_in: false } },
      '/providers': { body: { providers: { apple: 'a-client' } } },
      '/provider/start': { body: { status: 'ok', nonce: 'n2' } },
      '/provider/finish': (body) => (body?.over_18 === true ? { body: { status: 'ok', new_account: true } } : { body: { status: 'needs_age_answer', message: 'm' } }),
      '/balance': { body: BALANCE },
    });
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.signIn }));
    fireEvent.click(await screen.findByRole('button', { name: copy.continueWith('Apple') }));
    fireEvent.click(await screen.findByRole('button', { name: copy.openProvider('Apple') }));
    fireEvent.click(await screen.findByRole('button', { name: copy.ageYes }));
    await waitFor(() => expect(calls.filter((c) => c.path === '/provider/finish')).toHaveLength(2));
    const finishes = calls.filter((c) => c.path === '/provider/finish');
    expect(finishes[1].body).toMatchObject({ id_token: 'token-1', nonce: 'n2', over_18: true });
    expect(appleSignIn).toHaveBeenCalledTimes(1);
  });

  it('shows the plain failure line when the provider window closes', async () => {
    serve({
      '/me': { body: { signed_in: false } },
      '/providers': { body: { providers: { google: 'g-client' } } },
      '/provider/start': { body: { status: 'ok', nonce: 'n3' } },
    });
    renderGoogleButton.mockImplementationOnce((_el, done) => done(null));
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.signIn }));
    fireEvent.click(await screen.findByRole('button', { name: copy.continueWith('Google') }));
    expect(await screen.findByRole('alert')).toHaveTextContent(copy.providerFailed);
  });
});

describe('recovery', () => {
  it('recovers with the saved code and shows the new code once', async () => {
    const calls = serve({
      '/me': { body: { signed_in: false } },
      '/providers': { body: { providers: {} } },
      '/recovery/start': { body: { status: 'sent', challenge: 'c9' } },
      '/recovery/finish': { body: { status: 'ok', recovery_code: 'NEW-CODE', effective_on: 'Nov 1' } },
    });
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.signIn }));
    fireEvent.click(await screen.findByRole('button', { name: copy.lostEmail }));
    fireEvent.change(screen.getByLabelText(copy.recoveryCodeLabel), { target: { value: 'OLD-CODE' } });
    fireEvent.change(screen.getByLabelText(copy.newAddressLabel), { target: { value: 'new@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '654321' } });
    fireEvent.click(panel().getByRole('button', { name: copy.codeSignIn }));
    expect(await screen.findByText('NEW-CODE')).toBeInTheDocument();
    expect(calls.find((c) => c.path === '/recovery/start')!.body).toEqual({ recovery_code: 'OLD-CODE', new_address: 'new@b.org' });
    expect(calls.find((c) => c.path === '/recovery/finish')!.body).toEqual({ challenge: 'c9', code: '654321', new_address: 'new@b.org' });
    expect(localStorage.length + sessionStorage.length).toBe(0);
  });

  it('stops a recovery with the address and the cancel code from the notice', async () => {
    const calls = serve({
      '/me': { body: { signed_in: false } },
      '/providers': { body: { providers: {} } },
      '/recovery/cancel': { body: { status: 'ok' } },
    });
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.signIn }));
    fireEvent.click(await screen.findByRole('button', { name: copy.lostEmail }));
    fireEvent.click(screen.getByRole('button', { name: copy.cancelHeading }));
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'old@b.org' } });
    fireEvent.change(screen.getByLabelText(copy.cancelCodeLabel), { target: { value: 'CANCEL' } });
    fireEvent.click(screen.getByRole('button', { name: copy.cancelSend }));
    expect(await screen.findByText(copy.cancelDone)).toBeInTheDocument();
    expect(calls.find((c) => c.path === '/recovery/cancel')!.body).toEqual({ address: 'old@b.org', cancel_code: 'CANCEL' });
  });
});

describe('signed-in changes', () => {
  const signedIn = (methods: string[], providers: Record<string, string> = {}) => ({
    '/me': { body: { signed_in: true, recovery_pending: null, sign_in_methods: methods, has_recovery_code: false } },
    '/providers': { body: { providers } },
    '/balance': { body: BALANCE },
    '/shelf': { body: { conversations: [] } },
  });

  it('changes the address only after a fresh confirmation', async () => {
    const calls = serve({
      ...signedIn(['address']),
      '/step-up/start': { body: { status: 'sent', challenge: 's1' } },
      '/step-up/finish': { body: { status: 'ok' } },
      '/address/start': { body: { status: 'sent', challenge: 'a1' } },
      '/address/finish': { body: { status: 'ok' } },
    });
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.yourAccount }));
    fireEvent.click(await screen.findByRole('button', { name: copy.changeAddress }));
    expect(calls.some((c) => c.path === '/address/start')).toBe(false);
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'me@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '111111' } });
    fireEvent.click(panel().getByRole('button', { name: copy.codeSignIn }));
    fireEvent.change(await screen.findByLabelText(copy.newAddressLabel), { target: { value: 'next@b.org' } });
    fireEvent.click(panel().getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '222222' } });
    fireEvent.click(panel().getByRole('button', { name: copy.codeSignIn }));
    expect(await screen.findByText(copy.changeAddressDone)).toBeInTheDocument();
    expect(calls.find((c) => c.path === '/address/finish')!.body).toEqual({ challenge: 'a1', code: '222222', new_address: 'next@b.org' });
  });

  it('lets an account with only Google confirm with Google, then make a recovery code shown once', async () => {
    const calls = serve({
      ...signedIn(['google'], { google: 'g-client' }),
      '/provider/start': { body: { status: 'ok', nonce: 'n5' } },
      '/step-up/provider': { body: { status: 'ok' } },
      '/recovery/code': { body: { status: 'ok', recovery_code: 'FRESH-CODE' } },
    });
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.yourAccount }));
    fireEvent.click(await screen.findByRole('button', { name: copy.makeRecoveryCode }));
    expect(screen.queryByLabelText(copy.addressLabel)).not.toBeInTheDocument();
    fireEvent.click(await screen.findByRole('button', { name: copy.confirmWith('Google') }));
    expect(await screen.findByText('FRESH-CODE')).toBeInTheDocument();
    expect(calls.find((c) => c.path === '/step-up/provider')!.body).toMatchObject({ provider: 'google', nonce: 'n5' });
    fireEvent.click(panel().getByRole('button', { name: copy.gotIt }));
    expect(screen.queryByText('FRESH-CODE')).not.toBeInTheDocument();
  });

  it('links Google after a confirmation', async () => {
    const calls = serve({
      ...signedIn(['address'], { google: 'g-client' }),
      '/step-up/start': { body: { status: 'sent', challenge: 's2' } },
      '/step-up/finish': { body: { status: 'ok' } },
      '/provider/start': { body: { status: 'ok', nonce: 'n6' } },
      '/provider/link': { body: { status: 'ok' } },
    });
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.yourAccount }));
    fireEvent.click(await screen.findByRole('button', { name: copy.linkMethod('Google') }));
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'me@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '333333' } });
    fireEvent.click(panel().getByRole('button', { name: copy.codeSignIn }));
    expect(prepare).not.toHaveBeenCalled();
    fireEvent.click(await screen.findByRole('button', { name: copy.linkMethod('Google') }));
    await waitFor(() => expect(calls.some((c) => c.path === '/provider/link')).toBe(true));
    expect(prepare).toHaveBeenCalledWith('google', 'g-client', 'n6');
  });

  it('does not offer the provider for confirmation when the account has an address', async () => {
    serve(signedIn(['address', 'google'], { google: 'g-client' }));
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.yourAccount }));
    fireEvent.click(await screen.findByRole('button', { name: copy.makeRecoveryCode }));
    expect(screen.getByLabelText(copy.addressLabel)).toBeInTheDocument();
    expect(screen.queryByRole('button', { name: copy.confirmWith('Google') })).not.toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: copy.back }));
    expect(screen.getByRole('button', { name: copy.makeRecoveryCode })).toBeInTheDocument();
  });

  it('offers no removal for the only way in, and removes a second one after a confirmation', async () => {
    const calls = serve({
      ...signedIn(['address', 'google'], { google: 'g-client' }),
      '/step-up/start': { body: { status: 'sent', challenge: 's3' } },
      '/step-up/finish': { body: { status: 'ok' } },
      '/provider/unlink': { body: { status: 'ok' } },
    });
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.yourAccount }));
    fireEvent.click(await screen.findByRole('button', { name: copy.unlinkMethod('Google') }));
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'me@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '444444' } });
    fireEvent.click(panel().getByRole('button', { name: copy.codeSignIn }));
    expect(calls.some((c) => c.path === '/provider/unlink')).toBe(false);
    fireEvent.click(await screen.findByRole('button', { name: copy.unlinkMethod('Google') }));
    await waitFor(() => expect(calls.find((c) => c.path === '/provider/unlink')?.body).toEqual({ provider: 'google' }));
  });

  it('shows no removal when Google is the only way in', async () => {
    serve(signedIn(['google'], { google: 'g-client' }));
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.yourAccount }));
    await screen.findByText(copy.methodsHeading);
    expect(screen.queryByRole('button', { name: copy.unlinkMethod('Google') })).not.toBeInTheDocument();
  });
});

describe('a failed provider sign-in does not take over the email sign-in', () => {
  it('uses the email route for the emailed code after a provider attempt failed', async () => {
    const calls = serve({
      '/me': { body: { signed_in: false } },
      '/providers': { body: { providers: { google: 'g-client' } } },
      '/provider/start': { body: { status: 'ok', nonce: 'n7' } },
      '/provider/finish': { status: 400, body: { detail: 'That sign-in did not work. Please try again.' } },
      '/sign-in/start': { body: { status: 'sent', challenge: 'c7' } },
      '/sign-in/finish': { body: { status: 'ok', new_account: false } },
      '/balance': { body: BALANCE },
    });
    const { AccountPanel, accounts, copy } = await load();
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.signIn }));
    fireEvent.click(await screen.findByRole('button', { name: copy.continueWith('Google') }));
    expect(await screen.findByRole('alert')).toHaveTextContent('That sign-in did not work');
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'a@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '123456' } });
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: copy.codeSignIn }));
    await waitFor(() => expect(calls.some((c) => c.path === '/sign-in/finish')).toBe(true));
    expect(calls.filter((c) => c.path === '/provider/finish')).toHaveLength(1);
  });
});
