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
    mod.setRemaining(7);
    mod.clearCode();
    expect(mod.codeHeaders()).toEqual({});
    expect(localStorage.getItem('cic_code')).toBeNull();
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
    localStorage.setItem('cic_code', CODE);
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
    expect(localStorage.getItem('cic_code')).toBeNull();
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
    const fetchMock = vi.fn().mockResolvedValue(new Response(JSON.stringify({ codes: ['ABCD 2345 EFGH 6789 JKLM'], exchanges: 40 }), { status: 200 }));
    vi.stubGlobal('fetch', fetchMock);
    const mod = await load(true);
    expect(await mod.acceptClaim()).toBe(true);
    expect(fetchMock).toHaveBeenCalledWith('/api/deeper/claim', expect.objectContaining({ method: 'POST', body: JSON.stringify({ reference: REF }) }));
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
  });

  it('keeps nothing when the purchase holds several codes, or the server has none, or it cannot be reached', async () => {
    for (const reply of [
      () => Promise.resolve(new Response(JSON.stringify({ codes: [CODE, CODE.replace('A', 'B')], exchanges: 40 }), { status: 200 })),
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
    localStorage.setItem('cic_code', CODE);
    window.dispatchEvent(new StorageEvent('storage', { key: 'cic_code', newValue: CODE }));
    expect(mod.codeHeaders()).toEqual({ 'X-Cic-Code': CODE });
    window.dispatchEvent(new StorageEvent('storage', { key: 'cic_code', newValue: null }));
    expect(mod.codeHeaders()).toEqual({});
  });

  it('ignores other keys and values that are not codes, and does nothing with the module off', async () => {
    const on = await load(true);
    window.dispatchEvent(new StorageEvent('storage', { key: 'something_else', newValue: CODE }));
    window.dispatchEvent(new StorageEvent('storage', { key: 'cic_code', newValue: 'nonsense' }));
    expect(on.codeHeaders()).toEqual({});
    const off = await load(false);
    window.dispatchEvent(new StorageEvent('storage', { key: 'cic_code', newValue: CODE }));
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
