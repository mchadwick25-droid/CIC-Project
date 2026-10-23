import { useState } from 'react';
import { finishStepUp, providerStepUp, startStepUp, useAccount, type Provider } from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';
import { ProviderButtons } from './ProviderButtons';

/** Asks the person to prove it is them again: a fresh emailed code, or the provider they use. */
export function StepUp({ onDone, onCancel, fail, busy, run }: {
  onDone: () => void;
  onCancel: () => void;
  fail: (message: string) => void;
  busy: boolean;
  run: (work: () => Promise<void>) => Promise<boolean>;
}) {
  const account = useAccount();
  const [stage, setStage] = useState<'address' | 'code'>('address');
  const [address, setAddress] = useState('');
  const [code, setCode] = useState('');
  const [challenge, setChallenge] = useState('');
  const hasAddress = account.methods.includes('address');
  const linked = (['google', 'apple'] as Provider[]).filter((p) => account.methods.includes(p));

  const send = async (e: React.FormEvent) => {
    e.preventDefault();
    if (await run(async () => setChallenge(await startStepUp(address.trim())))) setStage('code');
  };
  const verify = async (e: React.FormEvent) => {
    e.preventDefault();
    if (await run(() => finishStepUp(challenge, code.trim()))) {
      setCode('');
      onDone();
    }
  };

  return (
    <div className="account__section" role="group" aria-label={copy.confirmIntro}>
      <p>{copy.confirmIntro}</p>
      {hasAddress && stage === 'address' && (
        <form onSubmit={send}>
          <label htmlFor="account-confirm-address">{copy.addressLabel}</label>
          <input id="account-confirm-address" type="email" value={address} onChange={(e) => setAddress(e.target.value)} autoComplete="email" required />
          <button type="submit" disabled={busy || address.trim() === ''}>{copy.sendCode}</button>
        </form>
      )}
      {hasAddress && stage === 'code' && (
        <form onSubmit={verify}>
          <label htmlFor="account-confirm-code">{copy.codeLabel}</label>
          <input id="account-confirm-code" type="text" inputMode="numeric" autoComplete="one-time-code" value={code} onChange={(e) => setCode(e.target.value)} />
          <button type="submit" disabled={busy || code.trim() === ''}>{copy.codeSignIn}</button>
        </form>
      )}
      <ProviderButtons
        label={copy.confirmWith}
        only={linked}
        onError={fail}
        onToken={async (token) => {
          if (await run(() => providerStepUp(token))) onDone();
        }}
      />
      <button type="button" onClick={onCancel}>{copy.back}</button>
    </div>
  );
}
