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
