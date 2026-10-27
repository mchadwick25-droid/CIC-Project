import { useState } from 'react';
import {
  deleteAccount, deleteShelved, exportData, finishAddressChange, makeRecoveryCode, providerLink, providerUnlink, startAddressChange, useAccount,
  type Provider,
} from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';
import { ProviderButtons } from './ProviderButtons';
import { StepUp } from './StepUp';
import { useGuard } from './useGuard';

type Guard = ReturnType<typeof useGuard>;

function Gate({ guard, onDone, onCancel, intro }: { guard: Guard; onDone: () => void; onCancel: () => void; intro?: string }) {
  return <StepUp busy={guard.busy} run={guard.run} fail={guard.setError} onCancel={onCancel} onDone={onDone} intro={intro} />;
}

function Problem({ message }: { message: string | null }) {
  return message ? <p className="account__error" role="alert">{message}</p> : null;
}

/** The recovery code: confirmed first, then shown once with Download and Print. */
export function RecoveryScreen({ onBack }: { onBack: () => void }) {
  const guard = useGuard();
  const [shown, setShown] = useState<string | null>(null);

  const download = () => {
    if (!shown) return;
    const url = URL.createObjectURL(new Blob([`${shown}\n`], { type: 'text/plain' }));
    const link = document.createElement('a');
    link.href = url;
    link.download = 'recovery-code.txt';
    link.click();
    URL.revokeObjectURL(url);
  };

  return (
    <div className="account__section">
      <h2>{copy.recoveryCodeHeading}</h2>
      <p>{copy.recoveryCodeIntro}</p>
      {shown === null ? (
        <Gate guard={guard} onCancel={onBack} onDone={() => void guard.run(async () => setShown(await makeRecoveryCode()))} />
      ) : (
        <>
          <p className="account__small">{copy.recoveryCodeFresh}</p>
          <p className="account__code">{shown}</p>
          <div className="account__actions">
            <button type="button" onClick={download}>{copy.recoveryDownload}</button>
            <button type="button" onClick={() => window.print()}>{copy.recoveryPrint}</button>
          </div>
          <p className="account__small">{copy.recoveryCodeNote}</p>
          <button type="button" onClick={() => { setShown(null); onBack(); }}>{copy.gotIt}</button>
        </>
      )}
      {shown === null && <button type="button" onClick={onBack}>{copy.recoveryLater}</button>}
      <Problem message={guard.error} />
    </div>
  );
}

export function AddressScreen({ onBack }: { onBack: () => void }) {
  const guard = useGuard();
  const [stage, setStage] = useState<'confirm' | 'new' | 'code' | 'done'>('confirm');
  const [address, setAddress] = useState('');
  const [challenge, setChallenge] = useState('');
  const [code, setCode] = useState('');

  const send = async (e: React.FormEvent) => {
    e.preventDefault();
    if (await guard.run(async () => setChallenge(await startAddressChange(address.trim())))) setStage('code');
  };
  const finish = async (e: React.FormEvent) => {
    e.preventDefault();
    if (await guard.run(() => finishAddressChange(challenge, code.trim(), address.trim()))) setStage('done');
  };

  return (
    <div className="account__section">
      <h2>{copy.changeAddress}</h2>
      {stage === 'confirm' && <Gate guard={guard} onCancel={onBack} onDone={() => setStage('new')} />}
      {stage === 'new' && (
        <form onSubmit={send}>
          <label htmlFor="account-new-address">{copy.newAddressLabel}</label>
          <input id="account-new-address" type="email" value={address} onChange={(e) => setAddress(e.target.value)} autoComplete="email" required />
          <button type="submit" disabled={guard.busy || address.trim() === ''}>{copy.sendCode}</button>
        </form>
      )}
      {stage === 'code' && (
        <form onSubmit={finish}>
          <p role="status">{copy.codeSent}</p>
          <label htmlFor="account-new-code">{copy.codeLabel}</label>
          <input id="account-new-code" type="text" inputMode="numeric" autoComplete="one-time-code" maxLength={8} value={code} onChange={(e) => setCode(e.target.value)} />
          <button type="submit" disabled={guard.busy || code.trim() === ''}>{copy.codeSignIn}</button>
        </form>
      )}
      {stage === 'done' && <p role="status">{copy.changeAddressDone}</p>}
      {stage !== 'confirm' && <button type="button" onClick={onBack}>{stage === 'done' ? copy.gotIt : copy.back}</button>}
      <Problem message={guard.error} />
    </div>
  );
}

type Change = { kind: 'link' | 'unlink'; provider: Provider } | null;

/** Add or remove Google or Apple, each after a fresh confirmation. */
export function MethodsScreen({ onBack }: { onBack: () => void }) {
  const account = useAccount();
  const guard = useGuard();
  const [change, setChange] = useState<Change>(null);
  const [confirmed, setConfirmed] = useState(false);
  const [done, setDone] = useState(false);
  const providers: Provider[] = ['google', 'apple'];
  const canAdd = providers.filter((p) => account.providers[p] && !account.methods.includes(p));
  const begin = (next: Change) => { guard.setError(null); setDone(false); setConfirmed(false); setChange(next); };

  return (
    <div className="account__section">
      <h2>{copy.methodsHeading}</h2>
      <ul className="account__list">
        {account.methods.map((method) => (
          <li key={method}>
            <span>{copy.methodName(method)}</span>
            {method !== 'address' && account.methods.length > 1 && change === null && (
              <button type="button" onClick={() => begin({ kind: 'unlink', provider: method as Provider })}>{copy.unlinkMethod(copy.methodName(method))}</button>
            )}
          </li>
        ))}
      </ul>
      {change === null && (
        <div className="account__actions">
          {canAdd.map((provider) => (
            <button key={provider} type="button" onClick={() => begin({ kind: 'link', provider })}>{copy.linkMethod(copy.methodName(provider))}</button>
          ))}
        </div>
      )}
      {change !== null && !confirmed && !done && <Gate guard={guard} onCancel={() => setChange(null)} onDone={() => setConfirmed(true)} />}
      {change?.kind === 'link' && confirmed && !done && (
        <ProviderButtons
          label={copy.linkMethod}
          only={[change.provider]}
          onError={guard.setError}
          onToken={async (token) => {
            if (await guard.run(() => providerLink(token))) setDone(true);
          }}
        />
      )}
      {change?.kind === 'unlink' && confirmed && !done && (
        <button type="button" disabled={guard.busy} onClick={() => void guard.run(() => providerUnlink(change.provider)).then((ok) => ok && setDone(true))}>
          {copy.unlinkMethod(copy.methodName(change.provider))}
        </button>
      )}
      {done && <p role="status">{copy.methodDone}</p>}
      {change !== null && !done && confirmed && <button type="button" onClick={() => setChange(null)}>{copy.back}</button>}
      <button type="button" onClick={onBack}>{copy.back}</button>
      <Problem message={guard.error} />
    </div>
  );
}

export function ExportScreen({ onBack }: { onBack: () => void }) {
  const guard = useGuard();
  const [done, setDone] = useState(false);
  return (
    <div className="account__section">
      <h2>{copy.exportData}</h2>
      {!done && <Gate guard={guard} onCancel={onBack} onDone={() => void guard.run(exportData).then((ok) => ok && setDone(true))} />}
      {done && <p role="status">{copy.methodDone}</p>}
      {done && <button type="button" onClick={onBack}>{copy.gotIt}</button>}
      <Problem message={guard.error} />
    </div>
  );
}

/** Erasing a saved conversation cannot be undone, so it asks for the same fresh confirmation as export. */
export function RemoveShelvedScreen({ sessionId, onBack }: { sessionId: string; onBack: () => void }) {
  const guard = useGuard();
  return (
    <div className="account__section">
      <h2>{copy.remove}</h2>
      <Gate guard={guard} onCancel={onBack} onDone={() => void guard.run(() => deleteShelved(sessionId)).then((ok) => ok && onBack())} />
      <Problem message={guard.error} />
    </div>
  );
}

export function DeleteScreen({ onBack }: { onBack: () => void }) {
  const guard = useGuard();
  const [confirmed, setConfirmed] = useState(false);
  return (
    <div className="account__section">
      <h2>{copy.deleteHome}</h2>
      <p>{copy.deleteIntro}</p>
      {!confirmed && <Gate guard={guard} onCancel={onBack} onDone={() => setConfirmed(true)} intro={copy.confirmIntro} />}
      <h3>{copy.deleteWhenHeading}</h3>
      <p>{copy.deleteWhen}</p>
      <h3>{copy.deleteGoesHeading}</h3>
      <p>{copy.deleteGoes}</p>
      <h3>{copy.deleteStaysHeading}</h3>
      <p>{copy.deleteStays}</p>
      {confirmed && (
        <div className="account__actions">
          <button type="button" disabled={guard.busy} onClick={() => void guard.run(async () => { await deleteAccount(); })}>{copy.deleteYes}</button>
          <button type="button" onClick={onBack}>{copy.deleteNo}</button>
        </div>
      )}
      <Problem message={guard.error} />
    </div>
  );
}
