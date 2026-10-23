import { useState } from 'react';
import { AccountsError, providerToken, useAccount, type Provider, type ProviderToken } from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';

const ORDER: Provider[] = ['google', 'apple'];

/** One button for each provider this server has turned on. The provider's script loads only on the press. */
export function ProviderButtons({ label, only, onToken, onError }: {
  label: (name: string) => string;
  only?: Provider[];
  onToken: (token: ProviderToken) => Promise<void>;
  onError: (message: string) => void;
}) {
  const account = useAccount();
  const [busy, setBusy] = useState(false);
  const shown = ORDER.filter((p) => account.providers[p] && (!only || only.includes(p)));
  if (shown.length === 0) return null;

  const press = async (provider: Provider) => {
    setBusy(true);
    try {
      await onToken(await providerToken(provider));
    } catch (error) {
      onError(error instanceof AccountsError && error.status !== 0 && error.message ? error.message : copy.providerFailed);
    } finally {
      setBusy(false);
    }
  };

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
