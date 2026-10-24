import { act, cleanup, fireEvent, render, screen } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { BALANCE, serve, signedIn } from './accountsHarness';

async function load() {
  vi.resetModules();
  vi.stubEnv('VITE_ACCOUNTS_ENABLED', 'on');
  vi.stubEnv('VITE_DEEPER_ENABLED', 'on');
  const { GiftNotice } = await import('./GiftNotice');
  const { AccountHome } = await import('./AccountHome');
  const accounts = await import('../lib/accounts');
  const { accountsCopy } = await import('../lib/accountsCopy');
  return { GiftNotice, AccountHome, accounts, copy: accountsCopy };
}

beforeEach(() => {
  localStorage.clear();
  sessionStorage.clear();
  window.location.hash = '';
});
afterEach(() => {
  cleanup();
  vi.unstubAllEnvs();
  vi.unstubAllGlobals();
});

describe('the gift notice', () => {
  it('says what Mark approved, once, and goes away when dismissed', async () => {
    serve({ ...signedIn(['address']), '/sign-in/finish': { body: { status: 'ok', new_account: false, coupons: [3000] } } });
    const { GiftNotice, accounts, copy } = await load();
    render(<GiftNotice />);
    await act(async () => { await accounts.finishSignIn('c1', 'a@b.org', '123456'); });
    expect(screen.getByRole('status')).toHaveTextContent('3,000 gift tokens have been added to your account.');
    expect(copy.giftAdded(3000)).toBe('3,000 gift tokens have been added to your account.');
    fireEvent.click(screen.getByRole('button', { name: copy.gotIt }));
    expect(screen.queryByRole('status')).not.toBeInTheDocument();
  });

  it('names each coupon that attached at the same sign-in', async () => {
    serve({ ...signedIn(['address']), '/sign-in/finish': { body: { status: 'ok', new_account: true, coupons: [1100, 500] } } });
    const { GiftNotice, accounts } = await load();
    render(<GiftNotice />);
    await act(async () => { await accounts.finishSignIn('c1', 'a@b.org', '123456', true); });
    expect(screen.getByRole('status')).toHaveTextContent('1,100 gift tokens have been added to your account.');
    expect(screen.getByRole('status')).toHaveTextContent('500 gift tokens have been added to your account.');
  });

  it('shows nothing when no coupon attached, or when the reply carries something else', async () => {
    serve({ ...signedIn(['address']), '/sign-in/finish': { body: { status: 'ok', new_account: false, coupons: [0, -5, 'x', 1.5] } } });
    const { GiftNotice, accounts } = await load();
    const { container } = render(<GiftNotice />);
    await act(async () => { await accounts.finishSignIn('c1', 'a@b.org', '123456'); });
    expect(container).toBeEmptyDOMElement();
  });

  it('puts one line on the account for each gift still held', async () => {
    serve({ ...signedIn(['address']), '/balance': { body: { ...BALANCE, codes_held: 2, code_tokens: 3500, gifts: [3000, 500] } } });
    const { AccountHome, accounts, copy } = await load();
    render(<AccountHome />);
    act(() => accounts.openHome());
    await act(async () => accounts.refresh());
    expect(await screen.findByText('Gift: 3,000 tokens.')).toBeInTheDocument();
    expect(screen.getByText('Gift: 500 tokens.')).toBeInTheDocument();
    expect(copy.giftLine(3000)).toBe('Gift: 3,000 tokens.');
  });
});
