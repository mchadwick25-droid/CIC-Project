/**
 * The participant's code in this browser: what counts as a code, what is
 * sent, and what stays silent when the app is built with the module off.
 */
import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

const CODE = 'ABCD2345EFGH6789JKLM';

async function load(enabled: boolean) {
  vi.resetModules();
  vi.stubEnv('VITE_DEEPER_ENABLED', enabled ? 'on' : '');
  return import('./deeper');
}

beforeEach(() => localStorage.clear());
afterEach(() => vi.unstubAllEnvs());

describe('normalizeCode', () => {
  it('forgives case and spacing and nothing else', async () => {
    const { normalizeCode } = await load(true);
    expect(normalizeCode(CODE)).toBe(CODE);
    expect(normalizeCode('abcd 2345-efgh 6789 jklm')).toBe(CODE);
    expect(normalizeCode(CODE.slice(0, 19))).toBeNull();
    expect(normalizeCode(`${CODE}2`)).toBeNull();
    expect(normalizeCode('ABCD2345EFGH6789JKL0')).toBeNull(); // 0 is not in the alphabet
    expect(normalizeCode('')).toBeNull();
  });
});

describe('with the module on', () => {
  it('sends the code once it is saved, and remembers it across a reload', async () => {
    const first = await load(true);
    expect(first.codeHeaders()).toEqual({});
    expect(first.saveCode('abcd 2345 efgh 6789 jklm')).toBe(true);
    expect(first.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
    const reloaded = await load(true);
    expect(reloaded.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
  });

  it('refuses text that is not a code and keeps no header', async () => {
    const mod = await load(true);
    expect(mod.saveCode('not a code')).toBe(false);
    expect(mod.codeHeaders()).toEqual({});
  });

  it('forgets the code and the balance when it is removed', async () => {
    const mod = await load(true);
    mod.saveCode(CODE);
    mod.reportBalance(CODE, 7, false);
    mod.clearCode();
    expect(mod.codeHeaders()).toEqual({});
    expect(localStorage.getItem('cic_codes')).toBeNull();
  });

  it('reads the balance header as a whole number and nothing else', async () => {
    const { remainingFromHeader } = await load(true);
    expect(remainingFromHeader('12')).toBe(12);
    expect(remainingFromHeader('0')).toBe(0);
    expect(remainingFromHeader(null)).toBeNull();
    expect(remainingFromHeader('-1')).toBeNull();
    expect(remainingFromHeader('lots')).toBeNull();
  });

  it('still works when the browser will not store anything', async () => {
    const mod = await load(true);
    vi.spyOn(Storage.prototype, 'setItem').mockImplementation(() => {
      throw new Error('blocked');
    });
    expect(mod.saveCode(CODE)).toBe(true);
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
    vi.restoreAllMocks();
  });
});

describe('with the module off', () => {
  it('sends nothing, even if a code was stored by an earlier build', async () => {
    localStorage.setItem('cic_codes', JSON.stringify([CODE]));
    const mod = await load(false);
    expect(mod.deeperEnabled).toBe(false);
    expect(mod.codeHeaders()).toEqual({});
    mod.saveCode(CODE);
    expect(mod.codeHeaders()).toEqual({});
  });
});

describe('the code handed back from the popup', () => {
  const SITE = 'https://churchinconversation.com';
  const good = { type: 'cic-deeper-code', codes: ['ABCD 2345 EFGH 6789 JKLM'] };

  it('is saved when it comes from the site as one well-formed code', async () => {
    const mod = await load(true);
    expect(mod.acceptCodeMessage({ origin: SITE, data: good })).toBe(true);
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
  });

  it('is ignored from any other origin, and for any other shape', async () => {
    const mod = await load(true);
    expect(mod.acceptCodeMessage({ origin: 'https://evil.example', data: good })).toBe(false);
    expect(mod.acceptCodeMessage({ origin: `${SITE}.evil.example`, data: good })).toBe(false);
    expect(mod.acceptCodeMessage({ origin: SITE, data: { ...good, type: 'other' } })).toBe(false);
    expect(mod.acceptCodeMessage({ origin: SITE, data: { type: good.type, codes: [] } })).toBe(false);
    expect(mod.acceptCodeMessage({ origin: SITE, data: { type: good.type, codes: [good.codes[0], good.codes[0]] } })).toBe(false);
    expect(mod.acceptCodeMessage({ origin: SITE, data: { type: good.type, codes: ['nonsense'] } })).toBe(false);
    expect(mod.acceptCodeMessage({ origin: SITE, data: { type: good.type, codes: [42] } })).toBe(false);
    expect(mod.acceptCodeMessage({ origin: SITE, data: null })).toBe(false);
    expect(mod.codeHeaders()).toEqual({});
  });

  it('opens the site page in a popup, and does nothing with the module off', async () => {
    const open = vi.fn().mockReturnValue({});
    vi.stubGlobal('open', open);
    const on = await load(true);
    expect(on.openGetCode()).toBe(true);
    expect(open).toHaveBeenCalledWith('https://churchinconversation.com/go-deeper.html', 'cic-get-code', expect.stringContaining('popup'));
    open.mockClear();
    const off = await load(false);
    expect(off.openGetCode()).toBe(false);
    expect(off.acceptCodeMessage({ origin: SITE, data: good })).toBe(false);
    expect(open).not.toHaveBeenCalled();
    vi.unstubAllGlobals();
  });

  it('reports a blocked popup', async () => {
    vi.stubGlobal('open', vi.fn().mockReturnValue(null));
    const mod = await load(true);
    expect(mod.openGetCode()).toBe(false);
    vi.unstubAllGlobals();
  });
});

describe('a purchase reference carried in the address', () => {
  const REF = 'r'.repeat(22);
  afterEach(() => {
    window.history.replaceState(null, '', '/');
    vi.unstubAllGlobals();
  });

  it('is removed from the address at once and held, saving nothing until the person agrees', async () => {
    window.history.replaceState(null, '', `/?mode=table#cic-claim=${REF}`);
    const mod = await load(true);
    expect(window.location.hash).toBe('');
    expect(window.location.search).toBe('?mode=table');
    expect(mod.codeHeaders()).toEqual({});
    expect(localStorage.getItem('cic_codes')).toBeNull();
  });

  it('is cleared from the address even when it is not a reference, and nothing is held', async () => {
    window.history.replaceState(null, '', '/#cic-claim=short');
    const mod = await load(true);
    expect(window.location.hash).toBe('');
    expect(mod.codeHeaders()).toEqual({});
  });

  it('a code planted in the address is not taken at all', async () => {
    window.history.replaceState(null, '', '/#cic-code=ABCD2345EFGH6789JKLM');
    const mod = await load(true);
    expect(mod.codeHeaders()).toEqual({});
    expect(window.location.hash).toBe('#cic-code=ABCD2345EFGH6789JKLM');
  });

  it('is left alone when the module is off', async () => {
    window.history.replaceState(null, '', `/#cic-claim=${REF}`);
    await load(false);
    expect(window.location.hash).toBe(`#cic-claim=${REF}`);
  });

  it('on a yes, the app asks its own server and keeps exactly one code', async () => {
    window.history.replaceState(null, '', `/#cic-claim=${REF}`);
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({ codes: ['ABCD 2345 EFGH 6789 JKLM'], tokens: 40 }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    const mod = await load(true);
    expect(await mod.acceptClaim()).toBe(true);
    expect(fetchMock).toHaveBeenCalledWith(
      '/api/deeper/claim',
      expect.objectContaining({ method: 'POST', credentials: 'omit', referrerPolicy: 'no-referrer', body: JSON.stringify({ reference: REF }) })
    );
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
  });

  it('keeps nothing when the purchase holds several codes, or the server has none, or it cannot be reached', async () => {
    for (const reply of [
      () => Promise.resolve(new Response(JSON.stringify({ codes: [CODE, CODE.replace('A', 'B')], tokens: 40 }), { status: 200 })),
      () => Promise.resolve(new Response('{}', { status: 404 })),
      () => Promise.reject(new Error('offline')),
    ]) {
      window.history.replaceState(null, '', `/#cic-claim=${REF}`);
      vi.stubGlobal('fetch', vi.fn().mockImplementation(reply));
      localStorage.clear();
      const mod = await load(true);
      expect(await mod.acceptClaim()).toBe(false);
      expect(mod.codeHeaders()).toEqual({});
    }
  });

  it('is dropped when the person says not now', async () => {
    window.history.replaceState(null, '', `/#cic-claim=${REF}`);
    const fetchMock = vi.fn();
    vi.stubGlobal('fetch', fetchMock);
    const mod = await load(true);
    mod.declineClaim();
    expect(await mod.acceptClaim()).toBe(false);
    expect(fetchMock).not.toHaveBeenCalled();
  });

  it('tells the popup its code is saved, to the site origin only', async () => {
    const mod = await load(true);
    const reply = vi.fn();
    mod.acceptCodeMessage({
      origin: 'https://churchinconversation.com',
      data: { type: 'cic-deeper-code', codes: ['ABCD 2345 EFGH 6789 JKLM'] },
      source: { postMessage: reply },
    });
    expect(reply).toHaveBeenCalledWith({ type: 'cic-deeper-saved' }, 'https://churchinconversation.com');
  });
});

describe('a code saved or removed in another tab', () => {
  it('is followed by this tab, so a conversation already open uses it', async () => {
    const mod = await load(true);
    expect(mod.codeHeaders()).toEqual({});
    const stored = JSON.stringify([CODE]);
    localStorage.setItem('cic_codes', stored);
    window.dispatchEvent(new StorageEvent('storage', { key: 'cic_codes', newValue: stored }));
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
    window.dispatchEvent(new StorageEvent('storage', { key: 'cic_codes', newValue: null }));
    expect(mod.codeHeaders()).toEqual({});
  });

  it('ignores other keys and values that are not codes, and does nothing with the module off', async () => {
    const on = await load(true);
    window.dispatchEvent(new StorageEvent('storage', { key: 'something_else', newValue: CODE }));
    window.dispatchEvent(new StorageEvent('storage', { key: 'cic_codes', newValue: 'nonsense' }));
    expect(on.codeHeaders()).toEqual({});
    const off = await load(false);
    window.dispatchEvent(new StorageEvent('storage', { key: 'cic_codes', newValue: JSON.stringify([CODE]) }));
    expect(off.codeHeaders()).toEqual({});
  });
});

describe('a message from the popup', () => {
  it('is answered on any screen, not only where the code field shows', async () => {
    const mod = await load(true);
    window.dispatchEvent(new MessageEvent('message', { origin: 'https://churchinconversation.com', data: { type: 'cic-deeper-code', codes: [CODE] } }));
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
  });
});

describe('several codes held together', () => {
  const OTHER = 'BCDE2345EFGH6789JKLM';

  afterEach(() => vi.unstubAllGlobals());

  it('keeps each code once, in the order they came, and sends the first not known to be spent', async () => {
    const mod = await load(true);
    mod.saveCode(CODE);
    mod.saveCode(OTHER);
    mod.saveCode(CODE);
    expect(JSON.parse(localStorage.getItem('cic_codes') ?? '[]')).toEqual([CODE, OTHER]);
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
  });

  it('moves to the next code when the one in use runs out, and drops the spent one', async () => {
    const mod = await load(true);
    mod.saveCode(CODE);
    mod.saveCode(OTHER);
    mod.reportBalance(CODE, 0, false);
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': OTHER });
    expect(JSON.parse(localStorage.getItem('cic_codes') ?? '[]')).toEqual([OTHER]);
  });

  it('keeps the last code even when spent, so the server can say why it cannot carry on', async () => {
    const mod = await load(true);
    mod.saveCode(CODE);
    mod.reportBalance(CODE, 0, false);
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
  });

  it('adds what each code holds, and says low only when nothing else is held to carry on with', async () => {
    vi.stubGlobal('fetch', vi.fn().mockImplementation(async (_url: string, init: RequestInit) => {
      const code = (init.headers as Record<string, string>)['X-Cic-Code'];
      return new Response(JSON.stringify({ kind: 'single', remaining: code === OTHER ? 30 : 4, paused: false }), { status: 200 });
    }));
    const mod = await load(true);
    mod.saveCode(CODE);
    mod.saveCode(OTHER);
    await vi.waitFor(() => expect(mod.deeperSnapshot().remaining).toBe(34));
    mod.reportBalance(CODE, 4, true);
    expect(mod.deeperSnapshot().low).toBe(false);
    mod.clearCode();
    mod.saveCode(CODE);
    mod.reportBalance(CODE, 4, true);
    expect(mod.deeperSnapshot().low).toBe(true);
    mod.reportBalance(CODE, 40, false);
    expect(mod.deeperSnapshot().low).toBe(false);
  });

  it('refuses a typed code the server does not know, and keeps one when the server cannot be reached', async () => {
    const mod = await load(true);
    vi.stubGlobal('fetch', vi.fn().mockResolvedValue(new Response('{}', { status: 404 })));
    expect(await mod.addCode(CODE)).toBe(false);
    expect(mod.codeHeaders()).toEqual({});
    vi.stubGlobal('fetch', vi.fn().mockRejectedValue(new Error('offline')));
    expect(await mod.addCode(CODE)).toBe(true);
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
  });

  it('asks the balance endpoint with no cookies', async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({ remaining: 3 }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    const mod = await load(true);
    await mod.addCode(CODE);
    expect(fetchMock).toHaveBeenCalledWith('/api/deeper/balance', expect.objectContaining({ credentials: 'omit' }));
  });
});

describe('a reply is credited to the code the request carried', () => {
  const OTHER = 'BCDE2345EFGH6789JKLM';
  const THIRD = 'CDEF2345GHJK6789LMNP';

  afterEach(() => vi.unstubAllGlobals());

  it('not to whichever code happens to be in use when the reply arrives', async () => {
    const mod = await load(true);
    mod.saveCode(CODE);
    mod.saveCode(OTHER);
    mod.saveCode(THIRD);
    const sentWith = mod.currentCode();
    expect(sentWith).toBe(CODE);
    // while the request is in flight, another tab spends the first code to zero and drops it
    const stored = JSON.stringify([OTHER, THIRD]);
    localStorage.setItem('cic_codes', stored);
    window.dispatchEvent(new StorageEvent('storage', { key: 'cic_codes', newValue: stored }));
    // the reply says the first code is at zero: the codes still held must not be touched
    mod.reportBalance(sentWith, 0, false);
    expect(JSON.parse(localStorage.getItem('cic_codes') ?? '[]')).toEqual([OTHER, THIRD]);
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': OTHER });
  });

  it('and a reply for a code no longer held is ignored', async () => {
    const mod = await load(true);
    mod.saveCode(CODE);
    mod.reportBalance(OTHER, 0, true);
    expect(mod.deeperSnapshot().remaining).toBeNull();
    expect(mod.deeperSnapshot().low).toBe(false);
  });
});

describe('two tabs changing the list at once', () => {
  const OTHER = 'BCDE2345EFGH6789JKLM';

  it('keep both codes: a change starts from what is stored, not from this tab\'s memory', async () => {
    const mod = await load(true);
    mod.saveCode(CODE);
    // another tab adds a code that this tab has not heard about yet
    localStorage.setItem('cic_codes', JSON.stringify([CODE, OTHER]));
    mod.saveCode('CDEF2345GHJK6789LMNP');
    expect(JSON.parse(localStorage.getItem('cic_codes') ?? '[]')).toEqual([CODE, OTHER, 'CDEF2345GHJK6789LMNP']);
  });
});

describe('removing a code', () => {
  const OTHER = 'BCDE2345EFGH6789JKLM';

  it('removes only the one in use, one tap at a time', async () => {
    const mod = await load(true);
    mod.saveCode(CODE);
    mod.saveCode(OTHER);
    mod.removeCode();
    expect(JSON.parse(localStorage.getItem('cic_codes') ?? '[]')).toEqual([OTHER]);
    mod.removeCode();
    expect(localStorage.getItem('cic_codes')).toBeNull();
  });
});

describe('the getting-low line and balances not yet known', () => {
  const OTHER = 'BCDE2345EFGH6789JKLM';

  it('is not shown while another held code has not reported, since it may carry on', async () => {
    vi.stubGlobal('fetch', vi.fn().mockReturnValue(new Promise(() => {})));
    const mod = await load(true);
    mod.saveCode(CODE);
    mod.saveCode(OTHER);
    mod.reportBalance(CODE, 4, true);
    expect(mod.deeperSnapshot().low).toBe(false);
    vi.unstubAllGlobals();
  });

  it('asks each code its balance with no cookies', async () => {
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({ remaining: 3 }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    const mod = await load(true);
    mod.saveCode(CODE);
    await vi.waitFor(() => expect(fetchMock).toHaveBeenCalled());
    expect(fetchMock).toHaveBeenCalledWith('/api/deeper/balance', expect.objectContaining({ credentials: 'omit', headers: { 'X-Cic-Code': CODE } }));
    vi.unstubAllGlobals();
  });
});
