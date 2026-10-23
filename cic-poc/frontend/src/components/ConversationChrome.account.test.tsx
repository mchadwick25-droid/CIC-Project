import { act, cleanup, fireEvent, render, screen, within } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import { serve, signedIn, signedOut } from './accountsHarness';

async function load(accounts: boolean) {
  vi.resetModules();
  vi.stubEnv('VITE_ACCOUNTS_ENABLED', accounts ? 'on' : '');
  vi.stubEnv('VITE_DEEPER_ENABLED', 'on');
  const { ConversationChrome } = await import('./ConversationChrome');
  const { AccountHome } = await import('./AccountHome');
  const accountsLib = await import('../lib/accounts');
  const { accountsCopy } = await import('../lib/accountsCopy');
  const element = (
    <>
      <ConversationChrome title="Church in Conversation" aboutLabel="About Vera" about={<p>About</p>} feedbackPage="w" reportPage={null} onLeave={() => undefined} />
      <AccountHome />
    </>
  );
  return { element, accounts: accountsLib, copy: accountsCopy };
}

const menu = () => fireEvent.click(screen.getByRole('button', { name: 'More' }));

beforeEach(() => {
  localStorage.clear();
  sessionStorage.clear();
});
afterEach(() => {
  cleanup();
  vi.unstubAllEnvs();
  vi.unstubAllGlobals();
});

describe('the more menu and the account', () => {
  it('has no account line when accounts are off', async () => {
    serve({});
    const { element } = await load(false);
    render(element);
    menu();
    expect(screen.getAllByRole('menuitem').map((i) => i.textContent)).toEqual(['About Vera', 'Tell us what you think', 'Leave for now']);
  });

  it('puts the invitation first when signed out, and it opens the sign-in steps in the panel', async () => {
    serve(signedOut());
    const { element, accounts, copy } = await load(true);
    render(element);
    await act(async () => accounts.refresh());
    menu();
    const items = screen.getAllByRole('menuitem');
    expect(items[0]).toHaveTextContent(copy.menuSignIn);
    fireEvent.click(items[0]);
    const panel = within(screen.getByRole('complementary'));
    expect(panel.getByRole('heading', { name: copy.signInOrUp })).toBeInTheDocument();
    expect(panel.getByLabelText(copy.addressLabel)).toBeInTheDocument();
  });

  it('puts My home first when signed in, and it opens the home', async () => {
    serve(signedIn(['address']));
    const { element, accounts, copy } = await load(true);
    render(element);
    await act(async () => accounts.refresh());
    menu();
    const items = screen.getAllByRole('menuitem');
    expect(items[0]).toHaveTextContent(copy.menuHome);
    fireEvent.click(items[0]);
    expect(await screen.findByRole('heading', { name: copy.homeHeading })).toBeInTheDocument();
  });
});
