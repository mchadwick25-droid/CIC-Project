import { useEffect, useRef, useState } from 'react';
import { AccountsError, prepareProvider, useAccount, type Provider, type ProviderToken } from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';
import { appleSignIn, renderGoogleButton } from '../lib/providerScripts';

const ORDER: Provider[] = ['google', 'apple'];

/**
 * One button for each provider this server has turned on. The provider's script loads only on the
 * press; the person then finishes in the provider's own button or window.
 */
export function ProviderButtons({ label, only, onToken, onError }: {
  label: (name: string) => string;
  only?: Provider[];
  onToken: (token: ProviderToken) => Promise<void>;
  onError: (message: string) => void;
}) {
  const account = useAccount();
  const [busy, setBusy] = useState(false);
  const [ready, setReady] = useState<{ provider: Provider; nonce: string } | null>(null);
  const mount = useRef<HTMLDivElement>(null);
  const shown = ORDER.filter((p) => account.providers[p] && (!only || only.includes(p)));

  const finish = async (provider: Provider, nonce: string, idToken: string | null) => {
    setReady(null);
    if (!idToken) {
      onError(copy.providerFailed);
      return;
    }
    await onToken({ provider, id_token: idToken, nonce });
  };

  useEffect(() => {
    if (ready?.provider !== 'google' || !mount.current) return;
    const { provider, nonce } = ready;
    renderGoogleButton(mount.current, (credential) => void finish(provider, nonce, credential));
  }, [ready]);

  if (shown.length === 0) return null;

  const press = async (provider: Provider) => {
    setBusy(true);
    try {
      setReady({ provider, nonce: await prepareProvider(provider) });
    } catch (error) {
      onError(error instanceof AccountsError && error.status !== 0 && error.message ? error.message : copy.providerFailed);
    } finally {
      setBusy(false);
    }
  };

  const open = async () => {
    if (!ready) return;
    try {
      await finish(ready.provider, ready.nonce, await appleSignIn());
    } catch {
      setReady(null);
      onError(copy.providerFailed);
    }
  };

  if (ready) {
    return (
      <div className="account__actions">
        {ready.provider === 'google' ? (
          <div ref={mount} />
        ) : (
          <button type="button" onClick={() => void open()}>{copy.openProvider(copy.methodName(ready.provider))}</button>
        )}
        <button type="button" onClick={() => setReady(null)}>{copy.back}</button>
      </div>
    );
  }

  return (
    <div className="account__actions">
      {shown.map((provider) => (
        <button key={provider} type="button" disabled={busy} onClick={() => void press(provider)}>
          {label(copy.methodName(provider))}
        </button>
      ))}
    </div>
  );
}
