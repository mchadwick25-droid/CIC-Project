/** The pilot's free pack: one request, no cookie, a marker so it is asked for once, and silence when closed. */
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

const CODE = 'ABCD2345EFGH6789JKLM';
const SHOWN = 'ABCD 2345 EFGH 6789 JKLM';

async function load(enabled: boolean, hash = '') {
  vi.resetModules();
  vi.stubEnv('VITE_DEEPER_ENABLED', enabled ? 'on' : '');
  window.history.replaceState(null, '', `/${hash}`);
  const pilot = await import('./pilot');
  const deeper = await import('./deeper');
  return { pilot, deeper };
}

function answer(status: number, body: unknown) {
  const fetchMock = vi.fn().mockResolvedValue({ status, ok: status >= 200 && status < 300, json: async () => body });
  vi.stubGlobal('fetch', fetchMock);
  return fetchMock;
}

beforeEach(() => localStorage.clear());
afterEach(() => {
  vi.unstubAllEnvs();
  vi.unstubAllGlobals();
});

describe('the pilot join', () => {
  it('asks once for a link, saves the code and clears the address', async () => {
    const fetchMock = answer(200, { joined: true, code: SHOWN, tokens: 1100, conversations: 10 });
    const { pilot, deeper } = await load(true, '#cic-pilot=pastors-link-key-0123456789');
    await vi.waitFor(() => expect(pilot.pilotSnapshot().status).toBe('ready'));
    const joins = fetchMock.mock.calls.filter(([target]) => target === '/api/deeper/pilot-join');
    expect(joins).toHaveLength(1);
    const [url, init] = joins[0];
    expect(url).toBe('/api/deeper/pilot-join');
    expect(init).toMatchObject({ method: 'POST', credentials: 'omit', referrerPolicy: 'no-referrer' });
    expect(JSON.parse(init.body)).toEqual({ link: 'pastors-link-key-0123456789' });
    expect(pilot.pilotSnapshot()).toEqual({ status: 'ready', tokens: 1100, conversations: 10 });
    expect(deeper.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
    expect(window.location.hash).toBe('');
  });

  it('never offers the pack again to a browser that joined', async () => {
    answer(200, { joined: true, code: SHOWN, tokens: 1100, conversations: 10 });
    await load(true, '#cic-pilot=general');
    await vi.waitFor(() => expect(localStorage.getItem('cic_pilot')).toBe('1'));
    const again = answer(200, {});
    const { pilot } = await load(true, '#cic-pilot=general');
    await vi.waitFor(() => expect(pilot.pilotSnapshot().status).toBe('already'));
    expect(again).not.toHaveBeenCalled();
  });

  it.each(['full', 'ended', 'address_limit'])('says so when the server answers %s, and keeps no code', async (reason) => {
    answer(409, { joined: false, reason });
    const { pilot, deeper } = await load(true, '#cic-pilot=general');
    await vi.waitFor(() => expect(pilot.pilotSnapshot().status).toBe(reason));
    expect(deeper.codeHeaders()).toEqual({});
    expect(localStorage.getItem('cic_pilot')).toBeNull();
  });

  it('shows nothing when the link is closed or not named', async () => {
    answer(404, { detail: 'Not Found' });
    const { pilot } = await load(true, '#cic-pilot=general');
    await vi.waitFor(() => expect(pilot.pilotSnapshot().status).toBeNull());
    expect(localStorage.getItem('cic_pilot')).toBeNull();
  });

  it('says it failed when the server cannot be reached or sends nothing usable', async () => {
    vi.stubGlobal('fetch', vi.fn().mockRejectedValue(new Error('offline')));
    const { pilot } = await load(true, '#cic-pilot=general');
    await vi.waitFor(() => expect(pilot.pilotSnapshot().status).toBe('failed'));
    expect(localStorage.getItem('cic_pilot')).toBeNull();
  });

  it('does not ask for a code the server sent that is not a code', async () => {
    answer(200, { joined: true, code: 'nope', tokens: 1100, conversations: 10 });
    const { pilot } = await load(true, '#cic-pilot=general');
    await vi.waitFor(() => expect(pilot.pilotSnapshot().status).toBe('failed'));
    expect(localStorage.getItem('cic_pilot')).toBeNull();
  });

  it.each(['#cic-pilot=a b', '#cic-pilot=', '#cic-pilot=x&y=1', '#cic-pilot=../x', `#cic-pilot=${'x'.repeat(65)}`])(
    'asks nothing for the malformed fragment %s',
    async (hash) => {
      const fetchMock = answer(200, {});
      const { pilot } = await load(true, hash);
      expect(fetchMock).not.toHaveBeenCalled();
      expect(pilot.pilotSnapshot().status).toBeNull();
    }
  );

  it('does nothing at all with the module off', async () => {
    const fetchMock = answer(200, {});
    const { pilot } = await load(false, '#cic-pilot=general');
    expect(fetchMock).not.toHaveBeenCalled();
    expect(pilot.pilotSnapshot().status).toBeNull();
    expect(window.location.hash).toBe('#cic-pilot=general');
  });
});
