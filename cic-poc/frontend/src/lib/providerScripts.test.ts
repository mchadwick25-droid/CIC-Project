import { afterEach, beforeEach, describe, expect, it, vi } from 'vitest';

beforeEach(() => vi.resetModules());
afterEach(() => {
  document.head.querySelectorAll('script').forEach((s) => s.remove());
  delete (window as unknown as Record<string, unknown>).AppleID;
});

describe('providerScripts', () => {
  it('adds no script to the page until a provider is readied', async () => {
    await import('./providerScripts');
    expect(document.head.querySelector('script')).toBeNull();
  });

  it('loads Apple\'s script from its own host only when readied, and inits it with the nonce', async () => {
    const { prepare } = await import('./providerScripts');
    const init = vi.fn();
    const readying = prepare('apple', 'a-client', 'nonce-1');
    const script = document.head.querySelector('script') as HTMLScriptElement;
    expect(script.src).toBe('https://appleid.cdn-apple.com/appleauth/static/jsapi/appleid/1/en_US/appleid.auth.js');
    (window as unknown as Record<string, unknown>).AppleID = { auth: { init, signIn: vi.fn() } };
    script.onload?.(new Event('load'));
    await readying;
    expect(init).toHaveBeenCalledWith(expect.objectContaining({ clientId: 'a-client', nonce: 'nonce-1', usePopup: true }));
  });

  it('removes the script and fails plainly when it cannot load', async () => {
    const { prepare } = await import('./providerScripts');
    const readying = prepare('google', 'g', 'n');
    const script = document.head.querySelector('script') as HTMLScriptElement;
    script.onerror?.(new Event('error'));
    await expect(readying).rejects.toThrow('script');
    expect(document.head.querySelector('script')).toBeNull();
  });
});
