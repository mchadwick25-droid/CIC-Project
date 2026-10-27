import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { serve, signedIn } from './accountsHarness';

const CODE = 'ABCDEFGHJKLMNPQRSTUV';

async function load(extra: Record<string, unknown> = {}) {
  vi.resetModules();
  vi.stubEnv('VITE_ACCOUNTS_ENABLED', 'on');
  vi.stubEnv('VITE_DEEPER_ENABLED', 'on');
  localStorage.setItem('cic_codes', JSON.stringify([CODE]));
  const routes = {
    ...signedIn(['address']),
    '/sign-in/finish': { body: { status: 'ok', new_account: true, coupons: [] } },
    '/codes/attach': { body: { status: 'ok' } },
    ...extra,
  };
  const calls = serve(routes);
  const fetchBase = globalThis.fetch;
  vi.stubGlobal('fetch', vi.fn(async (url: string, init?: RequestInit) => {
    if (String(url).startsWith('/api/deeper/balance')) return new Response(JSON.stringify({ remaining: 1050, tokens: 1050 }), { status: 200 });
    return fetchBase(url, init);
  }));
  const { SavedCodeOffer } = await import('./SavedCodeOffer');
  const accounts = await import('../lib/accounts');
  const { accountsCopy: copy } = await import('../lib/accountsCopy');
  const deeper = await import('../lib/deeper');
  return { SavedCodeOffer, accounts, copy, deeper, calls };
}

beforeEach(() => { localStorage.clear(); sessionStorage.clear(); window.location.hash = ''; });
afterEach(() => { cleanup(); vi.unstubAllEnvs(); vi.unstubAllGlobals(); });

describe('the saved-code offer', () => {
  it('says what Mark chose, once, and adds the code when asked', async () => {
    const { SavedCodeOffer, accounts, copy, deeper, calls } = await load();
    render(<SavedCodeOffer />);
    await act(async () => { await deeper.refreshBalances(); await accounts.finishSignIn('c1', 'a@b.org', '123456'); });
    expect(copy.savedCodeOffer(1050)).toBe('You have 1,050 tokens on a code saved in this browser. Add them to your account so they come with you on any device? Once added, the code belongs to this account only.');
    expect(screen.getByRole('status')).toHaveTextContent(copy.savedCodeOffer(1050));
    await act(async () => { fireEvent.click(screen.getByRole('button', { name: copy.savedCodeAdd })); });
    expect(calls.some((c) => c.path === '/codes/attach')).toBe(true);
    expect(screen.getByRole('status')).toHaveTextContent(copy.codeAdded);
    fireEvent.click(screen.getByRole('button', { name: copy.gotIt }));
    expect(screen.queryByRole('status')).not.toBeInTheDocument();
  });

  it('keeps the code in the browser when declined, says where to add it later, and does not ask again', async () => {
    const { SavedCodeOffer, accounts, copy, deeper, calls } = await load();
    const view = render(<SavedCodeOffer />);
    await act(async () => { await deeper.refreshBalances(); await accounts.finishSignIn('c1', 'a@b.org', '123456'); });
    fireEvent.click(screen.getByRole('button', { name: copy.savedCodeKeep }));
    expect(screen.getByRole('status')).toHaveTextContent(copy.savedCodeKept);
    expect(calls.some((c) => c.path === '/codes/attach')).toBe(false);
    fireEvent.click(screen.getByRole('button', { name: copy.gotIt }));
    expect(localStorage.getItem('cic_codes')).toContain(CODE);
    await act(async () => { await accounts.finishSignIn('c2', 'a@b.org', '654321'); });
    view.rerender(<SavedCodeOffer />);
    expect(screen.queryByRole('status')).not.toBeInTheDocument();
  });

  it('asks nothing when the browser holds no code', async () => {
    const { SavedCodeOffer, accounts } = await load();
    localStorage.removeItem('cic_codes');
    vi.resetModules();
    const fresh = await import('../lib/accounts');
    const { SavedCodeOffer: Offer } = await import('./SavedCodeOffer');
    render(<Offer />);
    await act(async () => { await fresh.finishSignIn('c1', 'a@b.org', '123456'); });
    expect(screen.queryByRole('status')).not.toBeInTheDocument();
    void SavedCodeOffer; void accounts;
  });

  it('says it did not work, and keeps the code, when adding fails', async () => {
    const { SavedCodeOffer, accounts, copy, deeper } = await load({ '/codes/attach': { status: 409, body: { detail: 'taken' } } });
    render(<SavedCodeOffer />);
    await act(async () => { await deeper.refreshBalances(); await accounts.finishSignIn('c1', 'a@b.org', '123456'); });
    await act(async () => { fireEvent.click(screen.getByRole('button', { name: copy.savedCodeAdd })); });
    expect(screen.getByRole('status')).toHaveTextContent(copy.failed);
    expect(localStorage.getItem('cic_codes')).toContain(CODE);
  });
});
