import { useState } from 'react';
import {
  cancelRecoverySignedIn, finishAddressChange, makeRecoveryCode, providerLink, providerUnlink, signOutEverywhere, startAddressChange, useAccount,
  type Provider,
} from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';
import { ProviderButtons } from './ProviderButtons';
import { StepUp } from './StepUp';
import { useGuard } from './useGuard';

type Action = { kind: 'address' } | { kind: 'recovery' } | { kind: 'link'; provider: Provider } | { kind: 'unlink'; provider: Provider };
type Stage = 'confirm' | 'act' | 'code' | 'done';

const PROVIDERS: Provider[] = ['google', 'apple'];

/** How the person signs in: the methods they hold, and the changes that need a fresh confirmation first. */
export function SignInMethods() {
  const account = useAccount();
  const { busy, error, setError, run } = useGuard();
  const [action, setAction] = useState<Action | null>(null);
  const [stage, setStage] = useState<Stage>('confirm');
  const [newAddress, setNewAddress] = useState('');
  const [challenge, setChallenge] = useState('');
  const [code, setCode] = useState('');
  const [shownCode, setShownCode] = useState<string | null>(null);

  const begin = (next: Action) => { setError(null); setShownCode(null); setAction(next); setStage('confirm'); };
  const end = () => { setAction(null); setStage('confirm'); setNewAddress(''); setCode(''); setChallenge(''); };

  const sendNew = async (e: React.FormEvent) => {
    e.preventDefault();
    if (await run(async () => setChallenge(await startAddressChange(newAddress.trim())))) setStage('code');
  };
  const finishNew = async (e: React.FormEvent) => {
    e.preventDefault();
    if (await run(() => finishAddressChange(challenge, code.trim(), newAddress.trim()))) setStage('done');
  };
  const recovery = async () => {
    if (await run(async () => setShownCode(await makeRecoveryCode()))) setStage('done');
  };

  const canAdd = PROVIDERS.filter((p) => account.providers[p] && !account.methods.includes(p));

  return (
    <div className="account__section">
      <h3>{copy.methodsHeading}</h3>
      <ul className="account__list">
        {account.methods.map((method) => (
          <li key={method}>
            <span>{copy.methodName(method)}</span>
            {method !== 'address' && action === null && (
              <button type="button" onClick={() => begin({ kind: 'unlink', provider: method as Provider })}>{copy.unlinkMethod(copy.methodName(method))}</button>
            )}
          </li>
        ))}
      </ul>
      {action === null && (
        <div className="account__actions">
          {canAdd.map((provider) => (
            <button key={provider} type="button" onClick={() => begin({ kind: 'link', provider })}>{copy.linkMethod(copy.methodName(provider))}</button>
          ))}
          {account.methods.includes('address') && <button type="button" onClick={() => begin({ kind: 'address' })}>{copy.changeAddress}</button>}
          <button type="button" onClick={() => begin({ kind: 'recovery' })}>{account.hasRecoveryCode ? copy.makeNewRecoveryCode : copy.makeRecoveryCode}</button>
          {account.recoveryPending && <button type="button" disabled={busy} onClick={() => void run(cancelRecoverySignedIn)}>{copy.stopRecovery}</button>}
          <button type="button" onClick={() => void run(signOutEverywhere)}>{copy.signOutEverywhere}</button>
        </div>
      )}
      {action !== null && stage === 'confirm' && (
        <StepUp busy={busy} run={run} fail={setError} onCancel={end} onDone={() => (action.kind === 'recovery' ? void recovery() : setStage('act'))} />
      )}
      {action?.kind === 'link' && stage === 'act' && (
        <ProviderButtons
          label={copy.linkMethod}
          only={[action.provider]}
          onError={setError}
          onToken={async (token) => {
            if (await run(() => providerLink(token))) setStage('done');
          }}
        />
      )}
      {action?.kind === 'unlink' && stage === 'act' && (
        <div className="account__actions">
          <button type="button" disabled={busy} onClick={() => void run(() => providerUnlink(action.provider)).then((ok) => ok && setStage('done'))}>
            {copy.unlinkMethod(copy.methodName(action.provider))}
          </button>
        </div>
      )}
      {action?.kind === 'address' && stage === 'act' && (
        <form onSubmit={sendNew}>
          <label htmlFor="account-new-address">{copy.newAddressLabel}</label>
          <input id="account-new-address" type="email" value={newAddress} onChange={(e) => setNewAddress(e.target.value)} autoComplete="email" required />
          <button type="submit" disabled={busy || newAddress.trim() === ''}>{copy.sendCode}</button>
        </form>
      )}
      {action?.kind === 'address' && stage === 'code' && (
        <form onSubmit={finishNew}>
          <p role="status">{copy.codeSent}</p>
          <label htmlFor="account-new-code">{copy.codeLabel}</label>
          <input id="account-new-code" type="text" inputMode="numeric" autoComplete="one-time-code" value={code} onChange={(e) => setCode(e.target.value)} />
          <button type="submit" disabled={busy || code.trim() === ''}>{copy.codeSignIn}</button>
        </form>
      )}
      {stage === 'done' && action !== null && (
        <div role="status">
          <p>{action.kind === 'address' ? copy.changeAddressDone : copy.methodDone}</p>
          {shownCode && (
            <>
              <p>{copy.newRecoveryCode}</p>
              <p className="account__code">{shownCode}</p>
              <p className="account__small">{copy.recoveryCodeNote}</p>
            </>
          )}
          <button type="button" onClick={() => { setShownCode(null); end(); }}>{copy.gotIt}</button>
        </div>
      )}
      {error && <p className="account__error" role="alert">{error}</p>}
    </div>
  );
}
