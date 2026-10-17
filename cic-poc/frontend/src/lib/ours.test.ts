/** The team's own browsers: ?ours=1 marks one, ?ours=0 clears it, and a marked browser sends internal: true when it opens a session. */
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

async function load(address: string) {
  vi.resetModules();
  window.history.replaceState(null, '', address);
  const ours = await import('./ours');
  const api = await import('./api');
  return { ours, api };
}

function stubCreate() {
  const fetchMock = vi.fn().mockImplementation(
    async () => new Response(JSON.stringify({ session_id: 's', session_code: 'c' }), { status: 201, headers: { 'Content-Type': 'application/json' } })
  );
  vi.stubGlobal('fetch', fetchMock);
  return fetchMock;
}

const bodies = (fetchMock: ReturnType<typeof vi.fn>) => fetchMock.mock.calls.map((call) => JSON.parse((call[1] as RequestInit).body as string));

beforeEach(() => localStorage.clear());
afterEach(() => {
  vi.unstubAllGlobals();
  vi.restoreAllMocks();
});

describe('the ours mark', () => {
  it('marks the browser from ?ours=1 and removes only that parameter', async () => {
    const { ours } = await load('/?worlds=desert&ours=1&mode=interview#q=hello');
    expect(localStorage.getItem('cic_ours')).toBe('1');
    expect(ours.isOurs()).toBe(true);
    expect(window.location.search).toBe('?worlds=desert&mode=interview');
    expect(window.location.hash).toBe('#q=hello');
  });

  it('clears the mark from ?ours=0', async () => {
    localStorage.setItem('cic_ours', '1');
    const { ours } = await load('/?ours=0');
    expect(localStorage.getItem('cic_ours')).toBeNull();
    expect(ours.isOurs()).toBe(false);
    expect(window.location.search).toBe('');
  });

  it('keeps the mark across loads without the parameter, and ignores any other value', async () => {
    await load('/?ours=1');
    const again = await load('/');
    expect(again.ours.isOurs()).toBe(true);
    const odd = await load('/?ours=yes');
    expect(odd.ours.isOurs()).toBe(true);
    expect(window.location.search).toBe('');
  });

  it('sends internal: true on both kinds of session from a marked browser', async () => {
    const { api } = await load('/?ours=1');
    const fetchMock = stubCreate();
    await api.createSession('fix');
    await api.createTableSession(['a', 'b']);
    expect(bodies(fetchMock)).toEqual([
      { world_key: 'fix', internal: true },
      { world_keys: ['a', 'b'], internal: true },
    ]);
  });

  it('sends no internal field from an unmarked browser', async () => {
    const { api } = await load('/');
    const fetchMock = stubCreate();
    await api.createSession('fix');
    await api.createTableSession(['a', 'b']);
    expect(bodies(fetchMock)).toEqual([{ world_key: 'fix' }, { world_keys: ['a', 'b'] }]);
  });

  it('treats blocked storage as unmarked and never throws', async () => {
    vi.spyOn(Storage.prototype, 'getItem').mockImplementation(() => {
      throw new Error('blocked');
    });
    vi.spyOn(Storage.prototype, 'setItem').mockImplementation(() => {
      throw new Error('blocked');
    });
    const { ours, api } = await load('/?ours=1');
    expect(ours.isOurs()).toBe(false);
    expect(window.location.search).toBe('');
    const fetchMock = stubCreate();
    await api.createSession('fix');
    expect(bodies(fetchMock)).toEqual([{ world_key: 'fix' }]);
  });
});
