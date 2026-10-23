import { useState } from 'react';
import { cancelRecovery, finishRecovery, startRecovery } from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';
import { useGuard } from './useGuard';

type Screen = 'start' | 'code' | 'done' | 'cancel' | 'cancelled';

/** For someone who cannot reach their email: recover with the saved code, or stop a recovery they did not start. */
export function RecoveryHelp({ dayOf, onBack }: { dayOf: (iso: string | null) => string; onBack: () => void }) {
  const { busy, error, setError, run } = useGuard();
  const [screen, setScreen] = useState<Screen>('start');
  const [recoveryCode, setRecoveryCode] = useState('');
  const [newAddress, setNewAddress] = useState('');
  const [challenge, setChallenge] = useState('');
  const [code, setCode] = useState('');
  const [address, setAddress] = useState('');
  const [cancelCode, setCancelCode] = useState('');
  const [result, setResult] = useState<{ recoveryCode: string; effectiveOn: string } | null>(null);

  const start = async (e: React.FormEvent) => {
    e.preventDefault();
    if (await run(async () => setChallenge(await startRecovery(recoveryCode.trim(), newAddress.trim())))) setScreen('code');
  };
  const finish = async (e: React.FormEvent) => {
    e.preventDefault();
    if (await run(async () => setResult(await finishRecovery(challenge, code.trim(), newAddress.trim())))) setScreen('done');
  };
  const cancel = async (e: React.FormEvent) => {
    e.preventDefault();
    if (await run(() => cancelRecovery(address.trim(), cancelCode.trim()))) setScreen('cancelled');
  };

  return (
    <div className="account__section">
      {screen === 'start' && (
        <form onSubmit={start}>
          <h3>{copy.recoveryHeading}</h3>
          <p>{copy.recoveryIntro}</p>
          <label htmlFor="account-recovery-code">{copy.recoveryCodeLabel}</label>
          <input id="account-recovery-code" type="text" value={recoveryCode} onChange={(e) => setRecoveryCode(e.target.value)} autoComplete="off" spellCheck={false} />
          <label htmlFor="account-recovery-address">{copy.newAddressLabel}</label>
          <input id="account-recovery-address" type="email" value={newAddress} onChange={(e) => setNewAddress(e.target.value)} autoComplete="email" required />
          <button type="submit" disabled={busy || recoveryCode.trim() === '' || newAddress.trim() === ''}>{copy.sendCode}</button>
          <button type="button" onClick={() => { setError(null); setScreen('cancel'); }}>{copy.cancelHeading}</button>
        </form>
      )}
      {screen === 'code' && (
        <form onSubmit={finish}>
          <p role="status">{copy.codeSent}</p>
          <label htmlFor="account-recovery-finish">{copy.codeLabel}</label>
          <input id="account-recovery-finish" type="text" inputMode="numeric" autoComplete="one-time-code" value={code} onChange={(e) => setCode(e.target.value)} />
          <button type="submit" disabled={busy || code.trim() === ''}>{copy.codeSignIn}</button>
        </form>
      )}
      {screen === 'done' && result && (
        <div role="status">
          <p>{copy.recoveryDone(dayOf(result.effectiveOn))}</p>
          <p>{copy.newRecoveryCode}</p>
          <p className="account__code">{result.recoveryCode}</p>
        </div>
      )}
      {screen === 'cancel' && (
        <form onSubmit={cancel}>
          <h3>{copy.cancelHeading}</h3>
          <p>{copy.cancelIntro}</p>
          <label htmlFor="account-cancel-address">{copy.addressLabel}</label>
          <input id="account-cancel-address" type="email" value={address} onChange={(e) => setAddress(e.target.value)} autoComplete="email" required />
          <label htmlFor="account-cancel-code">{copy.cancelCodeLabel}</label>
          <input id="account-cancel-code" type="text" value={cancelCode} onChange={(e) => setCancelCode(e.target.value)} autoComplete="off" spellCheck={false} />
          <button type="submit" disabled={busy || address.trim() === '' || cancelCode.trim() === ''}>{copy.cancelSend}</button>
        </form>
      )}
      {screen === 'cancelled' && <p role="status">{copy.cancelDone}</p>}
      {error && <p className="account__error" role="alert">{error}</p>}
      {screen !== 'done' && <button type="button" onClick={onBack}>{copy.back}</button>}
    </div>
  );
}
