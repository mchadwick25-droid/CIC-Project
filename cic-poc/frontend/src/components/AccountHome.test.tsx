import { act, cleanup, fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { BALANCE, serve, signedIn, signedOut } from './accountsHarness';

const prepare = vi.fn(async (..._args: unknown[]) => undefined);
const renderGoogleButton = vi.fn((_el: HTMLElement, done: (credential: string | null) => void) => done('token-1'));
const appleSignIn = vi.fn(async () => 'token-1');

async function load(env: { accounts?: boolean; deeper?: boolean } = { accounts: true, deeper: true }) {
  vi.resetModules();
  vi.stubEnv('VITE_ACCOUNTS_ENABLED', env.accounts ? 'on' : '');
  vi.stubEnv('VITE_DEEPER_ENABLED', env.deeper ? 'on' : '');
  vi.doMock('../lib/providerScripts', () => ({ prepare, renderGoogleButton, appleSignIn }));
  const { AccountHome } = await import('./AccountHome');
  const { GoDeeperPanel } = await import('./GoDeeperPanel');
  const { ResourcesFirst } = await import('./ResourcesFirst');
  const { SavedToHome } = await import('./SavedToHome');
  const accounts = await import('../lib/accounts');
  const deeper = await import('../lib/deeper');
  const { accountsCopy } = await import('../lib/accountsCopy');
  return { AccountHome, GoDeeperPanel, ResourcesFirst, SavedToHome, accounts, deeper, copy: accountsCopy };
}

const home = () => within(screen.getByRole('main'));

beforeEach(() => {
  localStorage.clear();
  sessionStorage.clear();
  window.location.hash = '';
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

describe('with accounts off', () => {
  it('shows nothing and asks the server nothing', async () => {
    const calls = serve({});
    const { AccountHome, GoDeeperPanel, SavedToHome, accounts } = await load({ accounts: false, deeper: true });
    const { container } = render(<><AccountHome /><SavedToHome /></>);
    act(() => accounts.openHome());
    await act(async () => accounts.refresh());
    expect(container).toBeEmptyDOMElement();
    render(<GoDeeperPanel />);
    fireEvent.click(screen.getByRole('button', { name: 'Get more conversations' }));
    expect(screen.queryByText('Keep your conversations')).not.toBeInTheDocument();
    expect(calls.filter((call) => call.path !== '/api/deeper/free')).toHaveLength(0);
  });

  it('shows nothing when the server has no accounts', async () => {
    serve({});
    const { AccountHome, accounts } = await load();
    const { container } = render(<AccountHome />);
    act(() => accounts.openHome());
    await act(async () => accounts.refresh());
    expect(container).toBeEmptyDOMElement();
  });
});

describe('the invitation in the panel', () => {
  it('offers sign in under Get more conversations, in the approved words', async () => {
    serve(signedOut());
    const { GoDeeperPanel, accounts, copy } = await load();
    render(<GoDeeperPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: 'Get more conversations' }));
    const panel = within(screen.getByRole('complementary'));
    expect(panel.getByRole('heading', { name: copy.keepHeading })).toBeInTheDocument();
    expect(panel.getByText(copy.keepBody)).toBeInTheDocument();
    expect(panel.getByRole('button', { name: 'Get more conversations' })).toBeInTheDocument();
    expect(panel.getByRole('button', { name: 'I have a code' })).toBeInTheDocument();
    fireEvent.click(panel.getByRole('button', { name: copy.signInOrUp }));
    expect(screen.getByRole('complementary')).toHaveTextContent(copy.addressIntro);
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: copy.back }));
    expect(within(screen.getByRole('complementary')).getByRole('button', { name: copy.signInOrUp })).toBeInTheDocument();
  });

  it('signs a new person in with a code and the one click, and carries the open conversation', async () => {
    sessionStorage.setItem('cic_session', JSON.stringify({ sessionId: 's9', sessionCode: 'c9', mode: 'interview', worldKey: 'w1' }));
    let signedInNow = false;
    const calls = serve({
      ...signedOut(),
      '/me': () => (signedInNow ? { body: { signed_in: true, recovery_pending: null, sign_in_methods: ['address'], has_recovery_code: false, refill_day: 14 } } : { body: { signed_in: false } }),
      '/sign-in/start': { body: { status: 'sent', message: 'm', challenge: 'c1' } },
      '/sign-in/finish': (body) => (body?.over_18 === true ? ((signedInNow = true), { body: { status: 'ok', new_account: true } }) : { body: { status: 'needs_age_answer', message: 'm' } }),
      '/shelf/add': { body: { status: 'ok' } },
      '/balance': { body: BALANCE },
      '/shelf': { body: { conversations: [] } },
    });
    const { GoDeeperPanel, SavedToHome, accounts, copy } = await load();
    render(<><GoDeeperPanel /><SavedToHome /></>);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: 'Get more conversations' }));
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: copy.signInOrUp }));
    expect(screen.getByText(copy.comesWithYou)).toBeInTheDocument();
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'a@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '123456' } });
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: copy.codeSignIn }));
    fireEvent.click(await screen.findByRole('button', { name: copy.ageYes }));
    await waitFor(() => expect(calls.some((c) => c.path === '/shelf/add')).toBe(true));
    expect(calls.find((c) => c.path === '/shelf/add')!.body).toEqual({ session_id: 's9', session_code: 'c9' });
    expect(calls.filter((c) => c.path === '/sign-in/finish').pop()!.body).toMatchObject({ challenge: 'c1', address: 'a@b.org', code: '123456', over_18: true });
    expect(await screen.findByText(copy.savedToHome)).toBeInTheDocument();
    const start = calls.find((c) => c.path === '/sign-in/start')!;
    expect(start.method).toBe('POST');
    expect(start.headers['x-cic-accounts']).toBe('1');
  });

  it('offers to re-open a deleted account and sends the same code again with the answer', async () => {
    let signedInNow = false;
    const calls = serve({
      ...signedOut(),
      '/me': () => (signedInNow ? { body: { signed_in: true, recovery_pending: null, sign_in_methods: ['address'], has_recovery_code: false, refill_day: 14 } } : { body: { signed_in: false } }),
      '/sign-in/start': { body: { status: 'sent', message: 'm', challenge: 'c1' } },
      '/sign-in/finish': (body) => (body?.reopen === true ? ((signedInNow = true), { body: { status: 'ok', new_account: false } }) : { body: { status: 'account_closed', erase_on: '2027-01-25', message: 'm' } }),
      '/balance': { body: BALANCE },
      '/shelf': { body: { conversations: [] } },
    });
    const { GoDeeperPanel, accounts, copy } = await load();
    render(<GoDeeperPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: 'Get more conversations' }));
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: copy.signInOrUp }));
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'a@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '12345678' } });
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: copy.codeSignIn }));
    expect(await screen.findByText(copy.closedText('January 25, 2027'))).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: copy.reopenYes }));
    await waitFor(() => expect(calls.filter((c) => c.path === '/sign-in/finish').pop()!.body).toMatchObject({ code: '12345678', reopen: true }));
    await waitFor(() => expect(signedInNow).toBe(true));
    await waitFor(() => expect(calls.filter((c) => c.path === '/me').length).toBeGreaterThan(1));
  });

  it('lets a person leave a deleted account deleted', async () => {
    serve({
      ...signedOut(),
      '/sign-in/start': { body: { status: 'sent', message: 'm', challenge: 'c1' } },
      '/sign-in/finish': { body: { status: 'account_closed', erase_on: '2027-01-25', message: 'm' } },
    });
    const { GoDeeperPanel, accounts, copy } = await load();
    render(<GoDeeperPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: 'Get more conversations' }));
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: copy.signInOrUp }));
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'a@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '12345678' } });
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: copy.codeSignIn }));
    fireEvent.click(await screen.findByRole('button', { name: copy.reopenNo }));
    expect(await screen.findByLabelText(copy.addressLabel)).toBeInTheDocument();
  });

  it('shows a signed-in person the way to their home instead', async () => {
    serve(signedIn(['address']));
    const { GoDeeperPanel, accounts, copy } = await load();
    render(<GoDeeperPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: 'Get more conversations' }));
    expect(screen.queryByText(copy.keepHeading)).not.toBeInTheDocument();
    expect(within(screen.getByRole('complementary')).getByRole('button', { name: copy.menuHome })).toBeInTheDocument();
  });
});

describe('My home', () => {
  const shelf = {
    conversations: [
      { session_id: 's1', mode: 'interview', worlds: ['The Scattered Households'], world_keys: ['w1'], title: 'A private first question', started: 'x', last_active: 'x', turns: 2, closed: false, holds_crisis_turn: false, saved: true },
      { session_id: 's2', mode: 'interview', worlds: ['Another voice'], world_keys: ['w2'], title: 'Hidden', started: 'x', last_active: 'x', turns: 1, closed: true, holds_crisis_turn: false, saved: true },
    ],
  };

  it('shows the count, the refill day and the saved conversations by voice and day only', async () => {
    serve({ ...signedIn(['address'], {}, { has_recovery_code: false }), '/shelf': { body: shelf } });
    const { AccountHome, accounts, copy } = await load();
    render(<AccountHome />);
    await act(async () => accounts.refresh());
    act(() => accounts.openHome());
    expect(await home().findByRole('heading', { name: copy.homeHeading })).toBeInTheDocument();
    expect(home().getByText('440 tokens left')).toBeInTheDocument();
    expect(home().getByText('440 free. They refill to 550 on the 14th of each month.')).toBeInTheDocument();
    expect(home().getByText(copy.freeFirst)).toBeInTheDocument();
    expect(await home().findByText('The Scattered Households')).toBeInTheDocument();
    expect(home().queryByText('A private first question')).not.toBeInTheDocument();
    expect(home().queryByText('Hidden')).not.toBeInTheDocument();
    expect(home().getByText(copy.recoveryPrompt)).toBeInTheDocument();
    expect(home().getByText(copy.conversationsNote)).toBeInTheDocument();
    expect(home().getByText(new RegExp(copy.ended))).toBeInTheDocument();
  });

  it('opens a saved conversation with its own code and stores it for the reload', async () => {
    serve({
      ...signedIn(['address']),
      '/shelf': { body: shelf },
      '/shelf/reopen': { body: { session_id: 's1', session_code: 'code-1', holds_crisis_turn: true, resources_text: 'One.\n\nTwo.' } },
    });
    const reload = vi.fn();
    vi.stubGlobal('location', { ...window.location, reload });
    const { AccountHome, accounts, copy } = await load();
    render(<AccountHome />);
    await act(async () => accounts.refresh());
    act(() => accounts.openHome());
    fireEvent.click(await home().findByRole('button', { name: new RegExp('The Scattered Households') }));
    await waitFor(() => expect(reload).toHaveBeenCalled());
    expect(JSON.parse(sessionStorage.getItem('cic_session') ?? '{}')).toMatchObject({ sessionId: 's1', sessionCode: 'code-1', mode: 'interview', worldKey: 'w1' });
    expect(accounts.resourcesFirst('s1')).toBe('One.\n\nTwo.');
    expect(accounts.resourcesFirst('other')).toBeNull();
    expect(copy.opening).toBeTruthy();
  });

  it('opens from the address #home and asks a signed-out visitor to sign in, with a way to carry on without', async () => {
    window.location.hash = '#home';
    serve(signedOut());
    const { AccountHome, copy } = await load();
    render(<AccountHome />);
    expect(await screen.findByRole('heading', { name: copy.homeSignedOutHeading })).toBeInTheDocument();
    expect(screen.getByText(copy.newHere)).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: copy.startWithout }));
    expect(screen.queryByRole('main')).not.toBeInTheDocument();
  });

  it('adds a code to the home', async () => {
    const calls = serve({ ...signedIn(['address']), '/codes/attach': { body: { status: 'ok' } } });
    const { AccountHome, accounts, copy } = await load();
    render(<AccountHome />);
    await act(async () => accounts.refresh());
    act(() => accounts.openHome());
    fireEvent.click(await home().findByRole('button', { name: copy.addCodeLink }));
    fireEvent.change(home().getByLabelText(copy.addCodeLabel), { target: { value: 'ABCD2345EFGH6789JKLM' } });
    fireEvent.click(home().getByRole('button', { name: copy.addCode }));
    expect(await home().findByText(copy.codeAdded)).toBeInTheDocument();
    expect(calls.find((c) => c.path === '/codes/attach')!.body).toEqual({ code: 'ABCD2345EFGH6789JKLM' });
  });

  it('signs out and closes', async () => {
    const calls = serve({ ...signedIn(['address']), '/sign-out': { body: { status: 'ok' } } });
    const { AccountHome, accounts, copy } = await load();
    render(<AccountHome />);
    await act(async () => accounts.refresh());
    act(() => accounts.openHome());
    fireEvent.click(await home().findByRole('button', { name: copy.signOut }));
    await waitFor(() => expect(screen.queryByRole('main')).not.toBeInTheDocument());
    expect(calls.some((c) => c.path === '/sign-out')).toBe(true);
  });
});

describe('settings', () => {
  const open = async (routes: ReturnType<typeof signedIn>, extra: Record<string, unknown> = {}) => {
    const calls = serve({ ...routes, ...extra } as never);
    const ctx = await load();
    render(<ctx.AccountHome />);
    await act(async () => ctx.accounts.refresh());
    act(() => ctx.accounts.openHome());
    await home().findByRole('heading', { name: ctx.copy.homeHeading });
    return { calls, ...ctx };
  };
  const confirmByEmail = async (copy: { addressLabel: string; sendCode: string; codeLabel: string; codeSignIn: string }) => {
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'me@b.org' } });
    fireEvent.click(home().getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '111111' } });
    fireEvent.click(home().getByRole('button', { name: copy.codeSignIn }));
  };
  const step = { '/step-up/start': { body: { status: 'sent', challenge: 's1' } }, '/step-up/finish': { body: { status: 'ok' } } };

  it('changes the address only after a fresh confirmation', async () => {
    const { calls, copy } = await open(signedIn(['address']), {
      ...step,
      '/address/start': { body: { status: 'sent', challenge: 'a1' } },
      '/address/finish': { body: { status: 'ok' } },
    });
    fireEvent.click(home().getByRole('button', { name: copy.changeAddress }));
    expect(calls.some((c) => c.path === '/address/start')).toBe(false);
    await confirmByEmail(copy);
    fireEvent.change(await screen.findByLabelText(copy.newAddressLabel), { target: { value: 'next@b.org' } });
    fireEvent.click(home().getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '222222' } });
    fireEvent.click(home().getByRole('button', { name: copy.codeSignIn }));
    expect(await home().findByText(copy.changeAddressDone)).toBeInTheDocument();
    expect(calls.find((c) => c.path === '/address/finish')!.body).toEqual({ challenge: 'a1', code: '222222', new_address: 'next@b.org' });
  });

  it('shows the recovery code once, after a confirmation, with Download and Print', async () => {
    const { copy } = await open(signedIn(['address']), { ...step, '/recovery/code': { body: { status: 'ok', recovery_code: 'FRESH-CODE' } } });
    fireEvent.click(home().getByRole('button', { name: copy.recoveryCode }));
    expect(screen.queryByText('FRESH-CODE')).not.toBeInTheDocument();
    await confirmByEmail(copy);
    expect(await home().findByText('FRESH-CODE')).toBeInTheDocument();
    expect(home().getByRole('button', { name: copy.recoveryDownload })).toBeInTheDocument();
    expect(home().getByRole('button', { name: copy.recoveryPrint })).toBeInTheDocument();
    fireEvent.click(home().getByRole('button', { name: copy.gotIt }));
    expect(screen.queryByText('FRESH-CODE')).not.toBeInTheDocument();
    expect(localStorage.length + sessionStorage.length).toBe(0);
  });

  it('lets an account with only Google confirm with Google, and offers no email form', async () => {
    const { calls, copy } = await open(signedIn(['google'], { google: 'g-client' }), {
      '/provider/start': { body: { status: 'ok', nonce: 'n5' } },
      '/step-up/provider': { body: { status: 'ok' } },
      '/recovery/code': { body: { status: 'ok', recovery_code: 'G-CODE' } },
    });
    fireEvent.click(home().getByRole('button', { name: copy.recoveryCode }));
    expect(screen.queryByLabelText(copy.addressLabel)).not.toBeInTheDocument();
    fireEvent.click(await home().findByRole('button', { name: copy.confirmWith('Google') }));
    expect(await home().findByText('G-CODE')).toBeInTheDocument();
    expect(calls.find((c) => c.path === '/step-up/provider')!.body).toMatchObject({ provider: 'google', nonce: 'n5' });
  });

  it('does not offer the provider for confirmation when the account has an address', async () => {
    const { copy } = await open(signedIn(['address', 'google'], { google: 'g-client' }));
    fireEvent.click(home().getByRole('button', { name: copy.recoveryCode }));
    expect(screen.getByLabelText(copy.addressLabel)).toBeInTheDocument();
    expect(screen.queryByRole('button', { name: copy.confirmWith('Google') })).not.toBeInTheDocument();
  });

  it('removes a second sign-in method after a confirmation, and offers no removal for the only one', async () => {
    const { calls, copy } = await open(signedIn(['address', 'google'], { google: 'g-client' }), { ...step, '/provider/unlink': { body: { status: 'ok' } } });
    fireEvent.click(home().getByRole('button', { name: copy.methodsHeading }));
    fireEvent.click(await home().findByRole('button', { name: copy.unlinkMethod('Google') }));
    await confirmByEmail(copy);
    expect(calls.some((c) => c.path === '/provider/unlink')).toBe(false);
    fireEvent.click(await home().findByRole('button', { name: copy.unlinkMethod('Google') }));
    await waitFor(() => expect(calls.find((c) => c.path === '/provider/unlink')?.body).toEqual({ provider: 'google' }));
  });

  it('shows what goes and what stays, then deletes only after a confirmation and a second press', async () => {
    const { calls, copy } = await open(signedIn(['address']), { ...step, '/delete': { body: { status: 'ok', erase_on: '2027-01-25' } } });
    fireEvent.click(home().getByRole('button', { name: copy.deleteHome }));
    expect(home().getByText(copy.deleteWhen)).toBeInTheDocument();
    expect(home().getByText(copy.deleteGoes)).toBeInTheDocument();
    expect(home().getByText(copy.deleteStays)).toBeInTheDocument();
    expect(home().queryByRole('button', { name: copy.deleteYes })).not.toBeInTheDocument();
    await confirmByEmail(copy);
    fireEvent.click(await home().findByRole('button', { name: copy.deleteYes }));
    await waitFor(() => expect(calls.some((c) => c.path === '/delete')).toBe(true));
    expect(await home().findByRole('heading', { name: copy.deletedHeading })).toBeInTheDocument();
    expect(home().getByText(copy.deletedDone)).toBeInTheDocument();
    expect(home().getByText(copy.deletedLastDay('January 25, 2027'))).toBeInTheDocument();
    expect(home().queryByRole('button', { name: copy.signInOrUp })).not.toBeInTheDocument();
    fireEvent.click(home().getByRole('button', { name: copy.backToSite }));
    await waitFor(() => expect(screen.queryByRole('main')).not.toBeInTheDocument());
  });

  it('keeps the home when the person says so', async () => {
    const { calls, copy } = await open(signedIn(['address']), step);
    fireEvent.click(home().getByRole('button', { name: copy.deleteHome }));
    await confirmByEmail(copy);
    fireEvent.click(await home().findByRole('button', { name: copy.deleteNo }));
    expect(await home().findByRole('heading', { name: copy.homeHeading })).toBeInTheDocument();
    expect(calls.some((c) => c.path === '/delete')).toBe(false);
  });
});

describe('provider sign-in', () => {
  const start = async (providers: Record<string, string>, extra: Record<string, unknown>) => {
    const calls = serve({ ...signedOut(providers), ...extra } as never);
    const ctx = await load();
    render(<ctx.GoDeeperPanel />);
    await act(async () => ctx.accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: 'Get more conversations' }));
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: ctx.copy.signInOrUp }));
    return { calls, ...ctx };
  };

  it('shows only the providers that are on, and loads no script until one is pressed', async () => {
    const { calls, copy } = await start({ google: 'g-client' }, {
      '/provider/start': { body: { status: 'ok', nonce: 'n1' } },
      '/provider/finish': { body: { status: 'ok', new_account: false } },
      '/balance': { body: BALANCE },
      '/shelf': { body: { conversations: [] } },
    });
    const google = await screen.findByRole('button', { name: copy.continueWith('Google') });
    expect(screen.queryByRole('button', { name: copy.continueWith('Apple') })).not.toBeInTheDocument();
    expect(prepare).not.toHaveBeenCalled();
    fireEvent.click(google);
    await waitFor(() => expect(calls.some((c) => c.path === '/provider/finish')).toBe(true));
    expect(prepare).toHaveBeenCalledWith('google', 'g-client', 'n1');
  });

  it('asks the age question for a new Apple account and sends the same token with the answer', async () => {
    const { calls, copy } = await start({ apple: 'a-client' }, {
      '/provider/start': { body: { status: 'ok', nonce: 'n2' } },
      '/provider/finish': (body: Record<string, unknown> | null) => (body?.over_18 === true ? { body: { status: 'ok', new_account: true } } : { body: { status: 'needs_age_answer', message: 'm' } }),
      '/balance': { body: BALANCE },
      '/shelf': { body: { conversations: [] } },
    });
    fireEvent.click(await screen.findByRole('button', { name: copy.continueWith('Apple') }));
    fireEvent.click(await screen.findByRole('button', { name: copy.openProvider('Apple') }));
    fireEvent.click(await screen.findByRole('button', { name: copy.ageYes }));
    await waitFor(() => expect(calls.filter((c) => c.path === '/provider/finish')).toHaveLength(2));
    expect(calls.filter((c) => c.path === '/provider/finish')[1].body).toMatchObject({ id_token: 'token-1', nonce: 'n2', over_18: true });
    expect(appleSignIn).toHaveBeenCalledTimes(1);
  });

  it('does not let a failed provider attempt take over the emailed code', async () => {
    const { calls, copy } = await start({ google: 'g-client' }, {
      '/provider/start': { body: { status: 'ok', nonce: 'n7' } },
      '/provider/finish': { status: 400, body: { detail: 'That sign-in did not work. Please try again.' } },
      '/sign-in/start': { body: { status: 'sent', challenge: 'c7' } },
      '/sign-in/finish': { body: { status: 'ok', new_account: false } },
      '/balance': { body: BALANCE },
      '/shelf': { body: { conversations: [] } },
    });
    fireEvent.click(await screen.findByRole('button', { name: copy.continueWith('Google') }));
    expect(await screen.findByRole('alert')).toHaveTextContent('That sign-in did not work');
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'a@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '123456' } });
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: copy.codeSignIn }));
    await waitFor(() => expect(calls.some((c) => c.path === '/sign-in/finish')).toBe(true));
    expect(calls.filter((c) => c.path === '/provider/finish')).toHaveLength(1);
  });

  it('recovers with the saved code and shows the new code once', async () => {
    const { calls, copy } = await start({}, {
      '/recovery/start': { body: { status: 'sent', challenge: 'c9' } },
      '/recovery/finish': { body: { status: 'ok', recovery_code: 'NEW-CODE', effective_on: 'Nov 1' } },
    });
    fireEvent.click(await screen.findByRole('button', { name: copy.lostEmail }));
    fireEvent.change(screen.getByLabelText(copy.recoveryCodeLabel), { target: { value: 'OLD-CODE' } });
    fireEvent.change(screen.getByLabelText(copy.newAddressLabel), { target: { value: 'new@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(copy.codeLabel), { target: { value: '654321' } });
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: copy.codeSignIn }));
    expect(await screen.findByText('NEW-CODE')).toBeInTheDocument();
    expect(calls.find((c) => c.path === '/recovery/start')!.body).toEqual({ recovery_code: 'OLD-CODE', new_address: 'new@b.org' });
    expect(calls.find((c) => c.path === '/recovery/finish')!.body).toEqual({ challenge: 'c9', code: '654321', new_address: 'new@b.org' });
    expect(localStorage.length + sessionStorage.length).toBe(0);
  });

  it('stops a recovery with the address and the cancel code from the notice', async () => {
    const { calls, copy } = await start({}, { '/recovery/cancel': { body: { status: 'ok' } } });
    fireEvent.click(await screen.findByRole('button', { name: copy.lostEmail }));
    fireEvent.click(screen.getByRole('button', { name: copy.cancelHeading }));
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'old@b.org' } });
    fireEvent.change(screen.getByLabelText(copy.cancelCodeLabel), { target: { value: 'CANCEL' } });
    fireEvent.click(screen.getByRole('button', { name: copy.cancelSend }));
    expect(await screen.findByText(copy.cancelDone)).toBeInTheDocument();
    expect(calls.find((c) => c.path === '/recovery/cancel')!.body).toEqual({ address: 'old@b.org', cancel_code: 'CANCEL' });
  });
});

describe('ResourcesFirst', () => {
  const crisis = 'One.\n\nTwo.';
  const turns = [
    { speaker: 'participant', text: 'hi' },
    { speaker: 'facilitator', kind: 'safety', text: crisis },
    { speaker: 'facilitator', kind: 'safety', text: 'Can I check something?' },
  ] as never;
  const hold = (id: string) => sessionStorage.setItem('cic_resources_first', JSON.stringify({ sessionId: id, text: crisis }));

  it('pins the stored crisis text, not a later check-in', async () => {
    const { ResourcesFirst, copy } = await load();
    hold('s1');
    render(<ResourcesFirst turns={turns} sessionId="s1" />);
    expect(screen.getByText(copy.resourcesFirst)).toBeInTheDocument();
    expect(screen.getByText('One.')).toBeInTheDocument();
    expect(screen.queryByText('Can I check something?')).not.toBeInTheDocument();
  });

  it('shows nothing for another conversation, without the flag, or with the build flag off', async () => {
    let ctx = await load();
    hold('s1');
    const first = render(<ctx.ResourcesFirst turns={turns} sessionId="s2" />);
    expect(first.container).toBeEmptyDOMElement();
    first.unmount();
    sessionStorage.clear();
    const second = render(<ctx.ResourcesFirst turns={turns} sessionId="s1" />);
    expect(second.container).toBeEmptyDOMElement();
    second.unmount();
    ctx = await load({ accounts: false, deeper: true });
    hold('s1');
    const third = render(<ctx.ResourcesFirst turns={turns} sessionId="s1" />);
    expect(third.container).toBeEmptyDOMElement();
  });
});

describe('what the room says and shows', () => {
  it('does not claim a save that failed, and forgets it on sign-out', async () => {
    sessionStorage.setItem('cic_session', JSON.stringify({ sessionId: 's9', sessionCode: 'c9', mode: 'interview', worldKey: 'w1' }));
    let signedInNow = false;
    const calls = serve({
      ...signedOut(),
      '/me': () => (signedInNow ? { body: { signed_in: true, recovery_pending: null, sign_in_methods: ['address'], has_recovery_code: true, refill_day: 14 } } : { body: { signed_in: false } }),
      '/sign-in/start': { body: { status: 'sent', message: 'm', challenge: 'c1' } },
      '/sign-in/finish': () => ((signedInNow = true), { body: { status: 'ok', new_account: false } }),
      '/shelf/add': { status: 400, body: { detail: 'That conversation is already on another account\'s shelf.' } },
      '/sign-out': { body: { status: 'ok' } },
      '/balance': { body: BALANCE },
      '/shelf': { body: { conversations: [] } },
    });
    const ctx = await load();
    render(<><ctx.GoDeeperPanel /><ctx.SavedToHome /></>);
    await act(async () => ctx.accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: 'Get more conversations' }));
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: ctx.copy.signInOrUp }));
    fireEvent.change(screen.getByLabelText(ctx.copy.addressLabel), { target: { value: 'a@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: ctx.copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(ctx.copy.codeLabel), { target: { value: '123456' } });
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: ctx.copy.codeSignIn }));
    await waitFor(() => expect(calls.some((c) => c.path === '/shelf/add')).toBe(true));
    await act(async () => undefined);
    expect(screen.queryByText(ctx.copy.savedToHome)).not.toBeInTheDocument();
  });

  it('shows the ribbon the account\'s count, free and on codes together', async () => {
    serve({ ...signedIn(['address']), '/balance': { body: { ...BALANCE, free_left: 440, code_tokens: 1100, codes_held: 1 } } });
    const ctx = await load();
    render(<ctx.GoDeeperPanel />);
    await act(async () => ctx.accounts.refresh());
    expect(await screen.findByText('1,540 tokens left')).toBeInTheDocument();
  });

  it('keeps the held-code line for someone holding a code, and the free-allowance pitch for everyone else', async () => {
    serve(signedOut());
    const ctx = await load();
    render(<ctx.GoDeeperPanel />);
    fireEvent.click(screen.getByRole('button', { name: 'Get more conversations' }));
    expect(screen.getByRole('complementary')).toHaveTextContent('Every conversation starts free.');
    cleanup();
    ctx.deeper.saveCode('ABCD2345EFGH6789JKLM');
    render(<ctx.GoDeeperPanel />);
    expect(screen.getByRole('complementary')).toHaveTextContent('Tokens pay for each new conversation and each round.');
  });

  it('lets someone delete an ended conversation after asking, and Escape does not close the home', async () => {
    const calls = serve({
      ...signedIn(['address']),
      '/shelf': { body: { conversations: [{ session_id: 's2', mode: 'interview', worlds: ['Another voice'], world_keys: ['w2'], title: '', started: 'x', last_active: 'x', turns: 1, closed: true, holds_crisis_turn: false, saved: true }] } },
      '/shelf/delete': { body: { status: 'ok' } },
    });
    const ctx = await load();
    render(<ctx.AccountHome />);
    await act(async () => ctx.accounts.refresh());
    act(() => ctx.accounts.openHome());
    fireEvent.click(await home().findByRole('button', { name: ctx.copy.remove }));
    expect(calls.some((c) => c.path === '/shelf/delete')).toBe(false);
    fireEvent.keyDown(window, { key: 'Escape' });
    expect(screen.getByRole('main')).toBeInTheDocument();
    fireEvent.click(home().getByRole('button', { name: ctx.copy.removeYes }));
    await waitFor(() => expect(calls.find((c) => c.path === '/shelf/delete')?.body).toEqual({ session_id: 's2' }));
  });

  it('asks again for the confirmation after backing out of it', async () => {
    const calls = serve({ ...signedIn(['address']), '/step-up/start': { body: { status: 'sent', challenge: 's1' } }, '/step-up/finish': { body: { status: 'ok' } }, '/delete': { body: { status: 'ok' } } });
    const ctx = await load();
    render(<ctx.AccountHome />);
    await act(async () => ctx.accounts.refresh());
    act(() => ctx.accounts.openHome());
    fireEvent.click(await home().findByRole('button', { name: ctx.copy.deleteHome }));
    fireEvent.change(screen.getByLabelText(ctx.copy.addressLabel), { target: { value: 'me@b.org' } });
    fireEvent.click(home().getByRole('button', { name: ctx.copy.sendCode }));
    fireEvent.change(await screen.findByLabelText(ctx.copy.codeLabel), { target: { value: '111111' } });
    fireEvent.click(home().getByRole('button', { name: ctx.copy.codeSignIn }));
    await home().findByRole('button', { name: ctx.copy.deleteNo }).then((b) => fireEvent.click(b));
    fireEvent.click(await home().findByRole('button', { name: ctx.copy.deleteHome }));
    expect(home().queryByRole('button', { name: ctx.copy.deleteYes })).not.toBeInTheDocument();
    expect(calls.some((c) => c.path === '/delete')).toBe(false);
  });
});
