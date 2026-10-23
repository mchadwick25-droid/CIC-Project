import { act, cleanup, fireEvent, render, screen, waitFor, within } from '@testing-library/react';
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';
import type { ConversationTurn } from '../hooks/useConversation';

type Reply = { status?: number; body?: unknown };

function serve(routes: Record<string, Reply | (() => Reply)>) {
  const calls: { path: string; method: string; headers: Record<string, string>; body: unknown }[] = [];
  vi.stubGlobal(
    'fetch',
    vi.fn(async (url: string, init: RequestInit = {}) => {
      const path = String(url).replace('/api/accounts', '');
      calls.push({
        path,
        method: init.method ?? 'GET',
        headers: (init.headers ?? {}) as Record<string, string>,
        body: init.body ? JSON.parse(String(init.body)) : null,
      });
      const hit = routes[path];
      const reply = typeof hit === 'function' ? hit() : hit;
      if (!reply) return new Response(JSON.stringify({ detail: 'x' }), { status: 404 });
      return new Response(JSON.stringify(reply.body ?? {}), { status: reply.status ?? 200 });
    })
  );
  return calls;
}

async function load(enabled: boolean) {
  vi.resetModules();
  vi.stubEnv('VITE_ACCOUNTS_ENABLED', enabled ? 'on' : '');
  const { AccountPanel } = await import('./AccountPanel');
  const { ResourcesFirst } = await import('./ResourcesFirst');
  const accounts = await import('../lib/accounts');
  const { accountsCopy } = await import('../lib/accountsCopy');
  return { AccountPanel, ResourcesFirst, accounts, copy: accountsCopy };
}

beforeEach(() => {
  localStorage.clear();
  sessionStorage.clear();
});
afterEach(() => {
  cleanup();
  vi.unstubAllEnvs();
  vi.unstubAllGlobals();
});

describe('AccountPanel', () => {
  it('shows nothing and makes no request when the app is built with accounts off', async () => {
    const calls = serve({});
    const { AccountPanel, accounts } = await load(false);
    const { container } = render(<AccountPanel />);
    await act(async () => accounts.refresh());
    expect(container).toBeEmptyDOMElement();
    expect(calls).toHaveLength(0);
  });

  it('shows nothing when the server has no accounts', async () => {
    serve({});
    const { AccountPanel, accounts } = await load(true);
    const { container } = render(<AccountPanel />);
    await act(async () => accounts.refresh());
    expect(container).toBeEmptyDOMElement();
  });

  it('signs a new person in: address, code, then the age question', async () => {
    const calls = serve({
      '/me': { body: { signed_in: false } },
      '/sign-in/start': { body: { status: 'sent', message: 'm', challenge: 'c1' } },
      '/sign-in/finish': () =>
        calls.some((c) => c.path === '/sign-in/finish' && (c.body as { over_18?: boolean }).over_18 === true)
          ? { body: { status: 'ok', new_account: true } }
          : { body: { status: 'needs_age_answer', message: 'm' } },
      '/balance': { body: { signed_in: true, available: true, free_left: 10, free_total: 10, refill_on: '', codes_held: 0, code_tokens: 0 } },
      '/shelf': { body: { conversations: [] } },
    });
    const { AccountPanel, accounts, copy } = await load(true);
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.signIn }));
    fireEvent.change(screen.getByLabelText(copy.addressLabel), { target: { value: 'a@b.org' } });
    fireEvent.click(screen.getByRole('button', { name: copy.sendCode }));
    const code = await screen.findByLabelText(copy.codeLabel);
    fireEvent.change(code, { target: { value: '123456' } });
    fireEvent.click(within(screen.getByRole('complementary')).getByRole('button', { name: copy.codeSignIn }));
    fireEvent.click(await screen.findByRole('button', { name: copy.ageYes }));
    await waitFor(() => expect(calls.filter((c) => c.path === '/sign-in/finish')).toHaveLength(2));
    const finish = calls.filter((c) => c.path === '/sign-in/finish').pop()!;
    expect(finish.body).toMatchObject({ challenge: 'c1', address: 'a@b.org', code: '123456', over_18: true });
    const start = calls.find((c) => c.path === '/sign-in/start')!;
    expect(start.method).toBe('POST');
    expect(start.headers['x-cic-accounts']).toBe('1');
  });

  it('lists the shelf and opens a conversation with its own code', async () => {
    serve({
      '/me': { body: { signed_in: true, recovery_pending: null } },
      '/balance': { body: { signed_in: true, available: true, free_left: 5, free_total: 10, refill_on: '', codes_held: 0, code_tokens: 0 } },
      '/shelf': {
        body: {
          conversations: [
            { session_id: 's1', mode: 'interview', worlds: ['W'], world_keys: ['w1'], title: 'Hello', started: 'Oct 1', last_active: 'Oct 2', turns: 2, closed: false, holds_crisis_turn: true, saved: true },
          ],
        },
      },
      '/shelf/reopen': { body: { session_id: 's1', session_code: 'code-1', holds_crisis_turn: true, resources_text: 'One.\n\nTwo.' } },
    });
    const reload = vi.fn();
    vi.stubGlobal('location', { ...window.location, reload });
    const { AccountPanel, accounts, copy } = await load(true);
    render(<AccountPanel />);
    await act(async () => accounts.refresh());
    fireEvent.click(screen.getByRole('button', { name: copy.yourAccount }));
    expect(await screen.findByText('Hello')).toBeInTheDocument();
    fireEvent.click(screen.getByRole('button', { name: new RegExp(copy.open) }));
    await waitFor(() => expect(reload).toHaveBeenCalled());
    expect(JSON.parse(sessionStorage.getItem('cic_session') ?? '{}')).toMatchObject({ sessionId: 's1', sessionCode: 'code-1', mode: 'interview', worldKey: 'w1' });
    expect(accounts.resourcesFirst('s1')).toBe('One.\n\nTwo.');
    expect(accounts.resourcesFirst('other')).toBeNull();
  });
});

describe('ResourcesFirst', () => {
  const crisis = 'One.\n\nTwo.';
  const turns: ConversationTurn[] = [
    { speaker: 'participant', text: 'hi' },
    { speaker: 'facilitator', kind: 'safety', text: crisis } as ConversationTurn,
    { speaker: 'facilitator', kind: 'safety', text: 'Can I check something?' } as ConversationTurn,
  ];
  const hold = (id: string) => sessionStorage.setItem('cic_resources_first', JSON.stringify({ sessionId: id, text: crisis }));

  it('pins the stored crisis text, not a later check-in', async () => {
    const { ResourcesFirst, copy } = await load(true);
    hold('s1');
    render(<ResourcesFirst turns={turns} sessionId="s1" />);
    expect(screen.getByText(copy.resourcesFirst)).toBeInTheDocument();
    expect(screen.getByText('One.')).toBeInTheDocument();
    expect(screen.getByText('Two.')).toBeInTheDocument();
    expect(screen.queryByText('Can I check something?')).not.toBeInTheDocument();
  });

  it('shows nothing for another conversation, without the flag, or with the build flag off', async () => {
    let loaded = await load(true);
    const first = render(<loaded.ResourcesFirst turns={turns} sessionId="s2" />);
    hold('s1');
    expect(first.container).toBeEmptyDOMElement();
    first.unmount();
    sessionStorage.clear();
    const second = render(<loaded.ResourcesFirst turns={turns} sessionId="s1" />);
    expect(second.container).toBeEmptyDOMElement();
    second.unmount();
    loaded = await load(false);
    hold('s1');
    const third = render(<loaded.ResourcesFirst turns={turns} sessionId="s1" />);
    expect(third.container).toBeEmptyDOMElement();
  });
});
