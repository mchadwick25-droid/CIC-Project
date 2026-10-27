import { useState } from 'react';
import { finishSignIn, providerSignIn, readStoredConversation, startSignIn, type ProviderToken, type SignInResult } from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';
import { dayOf } from './dayOf';
import { messageOf } from './useGuard';
import { ProviderButtons } from './ProviderButtons';
import { RecoveryHelp } from './RecoveryHelp';

type Step = 'address' | 'code' | 'age' | 'closed' | 'done' | 'recovery';

/** An address, the emailed code, and for a new account the one click about age. Or Google or Apple. */
export function SignInSteps({ onSignedIn }: { onSignedIn: () => void }) {
  const [step, setStep] = useState<Step>('address');
  const [address, setAddress] = useState('');
  const [code, setCode] = useState('');
  const [challenge, setChallenge] = useState('');
  const [busy, setBusy] = useState(false);
  const [note, setNote] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [token, setToken] = useState<ProviderToken | null>(null);
  const [eraseOn, setEraseOn] = useState('');

  const send = async (e?: React.FormEvent) => {
    e?.preventDefault();
    setToken(null);
    setBusy(true);
    setError(null);
    try {
      setChallenge(await startSignIn(address.trim()));
      setCode('');
      setStep('code');
    } catch (err) {
      setError(messageOf(err));
    } finally {
      setBusy(false);
    }
  };

  const settle = (result: SignInResult) => {
    if (result.kind !== 'ask_age' && result.kind !== 'closed') setToken(null);
    if (result.kind === 'ok') onSignedIn();
    else if (result.kind === 'ask_age') setStep('age');
    else if (result.kind === 'closed') {
      setEraseOn(result.eraseOn);
      setStep('closed');
    }
    else if (result.kind === 'not_adult') {
      setNote(result.message);
      setStep('done');
    } else {
      setNote(result.message || copy.recoveryWaiting(dayOf(result.effectiveOn)));
      setStep('done');
    }
  };

  const verify = async (over18?: boolean, reopen?: boolean) => {
    setBusy(true);
    setError(null);
    try {
      settle(token ? await providerSignIn(token, over18, reopen) : await finishSignIn(challenge, address.trim(), code.trim(), over18, reopen));
    } catch (err) {
      if (token) setToken(null);
      setError(messageOf(err));
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="account__section">
      {step === 'address' && (
        <>
          <p>{copy.addressIntro}</p>
          <ProviderButtons
            label={copy.continueWith}
            onError={setError}
            onToken={async (made) => {
              setError(null);
              setToken(made);
              try {
                settle(await providerSignIn(made));
              } catch (err) {
                setToken(null);
                setError(messageOf(err));
              }
            }}
          />
          <form onSubmit={send}>
            <label htmlFor="account-address">{copy.addressLabel}</label>
            <input id="account-address" type="email" value={address} onChange={(e) => setAddress(e.target.value)} autoComplete="email" inputMode="email" placeholder="name@example.com" required aria-invalid={error !== null} aria-describedby="account-keeps" />
            <button type="submit" disabled={busy || address.trim() === ''}>{busy ? copy.sending : copy.sendCode}</button>
            <p id="account-keeps" className="account__small">{copy.keepsAddress}</p>
            {readStoredConversation() && <p className="account__small">{copy.comesWithYou}</p>}
            <button type="button" onClick={() => { setError(null); setStep('recovery'); }}>{copy.lostEmail}</button>
          </form>
        </>
      )}
      {step === 'recovery' && <RecoveryHelp dayOf={dayOf} onBack={() => setStep('address')} />}
      {step === 'code' && (
        <form onSubmit={(e) => { e.preventDefault(); void verify(); }}>
          <h3>{copy.codeHeading}</h3>
          <p role="status">{copy.codeSent}</p>
          <label htmlFor="account-code">{copy.codeLabel}</label>
          <input id="account-code" type="text" inputMode="numeric" autoComplete="one-time-code" maxLength={8} value={code} onChange={(e) => setCode(e.target.value)} aria-invalid={error !== null} />
          <button type="submit" disabled={busy || code.trim() === ''}>{busy ? copy.checking : copy.codeSignIn}</button>
          <button type="button" disabled={busy} onClick={() => void send()}>{copy.newCode}</button>
          <p className="account__small">{copy.junkNote}</p>
        </form>
      )}
      {step === 'age' && (
        <div role="group" aria-label={copy.ageHeading}>
          <h3>{copy.ageHeading}</h3>
          <p>{copy.ageQuestion}</p>
          <div className="account__actions">
            <button type="button" disabled={busy} onClick={() => void verify(true)}>{copy.ageYes}</button>
            <button type="button" disabled={busy} onClick={() => void verify(false)}>{copy.ageNo}</button>
          </div>
          <p className="account__small">{copy.ageNote}</p>
        </div>
      )}
      {step === 'closed' && (
        <div role="group" aria-label={copy.closedHeading}>
          <h3>{copy.closedHeading}</h3>
          <p>{copy.closedText(dayOf(eraseOn))}</p>
          <div className="account__actions">
            <button type="button" disabled={busy} onClick={() => void verify(undefined, true)}>{copy.reopenYes}</button>
            <button type="button" disabled={busy} onClick={() => { setToken(null); setError(null); setStep('address'); }}>{copy.reopenNo}</button>
          </div>
        </div>
      )}
      {step === 'done' && note && <p role="status">{note}</p>}
      {error && <p className="account__error" role="alert">{error}</p>}
    </div>
  );
}
