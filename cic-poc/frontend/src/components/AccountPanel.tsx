/**
 * The account, beside the conversation. A strip says what is left and the panel opens only when the
 * person asks. Signed out it is one short form: an email address, the code sent to it, and, for a new
 * account, one question about age. Signed in it holds the saved conversations, a place to add a code,
 * the person's data and sign-out. Shown only when the app is built with accounts on.
 */
import { useEffect, useRef, useState } from 'react';
import {
  accountsEnabled, attachCode, closeAccountPanel, deleteAccount, deleteShelved, exportData, finishSignIn, loadProviders,
  loadShelf, openAccountPanel, openShelved, providerSignIn, refresh, signOut, startSignIn, useAccount, type ProviderToken, type ShelfItem, type SignInResult,
} from '../lib/accounts';
import { normalizeCode } from '../lib/deeper';
import { accountsCopy as copy } from '../lib/accountsCopy';
import { ProviderButtons } from './ProviderButtons';
import { RecoveryHelp } from './RecoveryHelp';
import { SignInMethods } from './SignInMethods';
import { StepUp } from './StepUp';
import { messageOf, useGuard } from './useGuard';

function dayOf(iso: string | null): string {
  if (!iso) return '';
  const date = new Date(`${iso.slice(0, 10)}T12:00:00Z`);
  return Number.isNaN(date.getTime()) ? iso.slice(0, 10) : date.toLocaleDateString('en-US', { month: 'long', day: 'numeric', year: 'numeric', timeZone: 'UTC' });
}

export function AccountPanel() {
  const account = useAccount();
  const toggleRef = useRef<HTMLButtonElement>(null);
  const wasOpen = useRef(false);
  const headRef = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    if (accountsEnabled) void refresh();
  }, []);

  useEffect(() => {
    if (account.panelOpen) void loadProviders();
  }, [account.panelOpen]);

  useEffect(() => {
    if (wasOpen.current && !account.panelOpen) toggleRef.current?.focus();
    if (account.panelOpen && !wasOpen.current) headRef.current?.focus();
    wasOpen.current = account.panelOpen;
  }, [account.panelOpen]);

  useEffect(() => {
    if (!account.panelOpen) return undefined;
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') closeAccountPanel();
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [account.panelOpen]);

  if (!accountsEnabled || account.status === 'off') return null;
  const signedIn = account.status === 'in';
  const balance = account.balance;

  return (
    <div className="account sans">
      <div className="account__ribbon">
        {signedIn && balance && (
          <span className="account__count" role="status">
            {copy.freeLeft(balance.free_left)}.{balance.refill_on ? ` ${copy.refills(dayOf(balance.refill_on))}.` : ''}
          </span>
        )}
        <button ref={toggleRef} type="button" aria-expanded={account.panelOpen} aria-controls="account-panel" onClick={account.panelOpen ? closeAccountPanel : openAccountPanel}>
          {signedIn ? copy.yourAccount : copy.signIn}
        </button>
      </div>
      {account.panelOpen && (
        <aside id="account-panel" className="account__panel" aria-label={copy.heading}>
          <div className="account__head">
            <h2 ref={headRef} tabIndex={-1}>{copy.heading}</h2>
            <button type="button" onClick={closeAccountPanel}>
              {copy.close}
            </button>
          </div>
          {signedIn ? <SignedIn /> : <SignIn />}
        </aside>
      )}
    </div>
  );
}

type Step = 'address' | 'code' | 'age' | 'done' | 'recovery';

function SignIn() {
  const [step, setStep] = useState<Step>('address');
  const [address, setAddress] = useState('');
  const [code, setCode] = useState('');
  const [challenge, setChallenge] = useState('');
  const [busy, setBusy] = useState(false);
  const [note, setNote] = useState<string | null>(null);
  const [error, setError] = useState<string | null>(null);
  const [token, setToken] = useState<ProviderToken | null>(null);

  const send = async (e: React.FormEvent) => {
    e.preventDefault();
    setBusy(true);
    setError(null);
    try {
      setChallenge(await startSignIn(address.trim()));
      setStep('code');
    } catch (err) {
      setError(messageOf(err));
    } finally {
      setBusy(false);
    }
  };

  const settle = (result: SignInResult) => {
    if (result.kind === 'ask_age') setStep('age');
    else if (result.kind === 'not_adult') {
      setNote(result.message);
      setStep('done');
    } else if (result.kind === 'waiting') {
      setNote(result.message || copy.recoveryWaiting(dayOf(result.effectiveOn)));
      setStep('done');
    }
  };

  const verify = async (over18?: boolean) => {
    setBusy(true);
    setError(null);
    try {
      settle(token ? await providerSignIn(token, over18) : await finishSignIn(challenge, address.trim(), code.trim(), over18));
    } catch (err) {
      setError(messageOf(err));
    } finally {
      setBusy(false);
    }
  };

  return (
    <div className="account__section">
      {step === 'address' && (
        <ProviderButtons
          label={copy.continueWith}
          onError={setError}
          onToken={async (made) => {
            setError(null);
            setToken(made);
            try {
              settle(await providerSignIn(made));
            } catch (err) {
              setError(messageOf(err));
            }
          }}
        />
      )}
      {step === 'address' && (
        <form onSubmit={send}>
          <p>{copy.intro}</p>
          <label htmlFor="account-address">{copy.addressLabel}</label>
          <input id="account-address" type="email" value={address} onChange={(e) => setAddress(e.target.value)} autoComplete="email" required aria-invalid={error !== null} aria-describedby="account-keeps" />
          <p id="account-keeps" className="account__small">{copy.keepsAddress}</p>
          <button type="submit" disabled={busy || address.trim() === ''}>{busy ? copy.sending : copy.sendCode}</button>
          <button type="button" onClick={() => { setError(null); setStep('recovery'); }}>{copy.lostEmail}</button>
        </form>
      )}
      {step === 'recovery' && <RecoveryHelp dayOf={dayOf} onBack={() => setStep('address')} />}
      {step === 'code' && (
        <form onSubmit={(e) => { e.preventDefault(); void verify(); }}>
          <p role="status">{copy.codeSent}</p>
          <label htmlFor="account-code">{copy.codeLabel}</label>
          <input id="account-code" type="text" inputMode="numeric" autoComplete="one-time-code" value={code} onChange={(e) => setCode(e.target.value)} aria-invalid={error !== null} />
          <button type="submit" disabled={busy || code.trim() === ''}>{busy ? copy.checking : copy.codeSignIn}</button>
          <button type="button" onClick={() => { setStep('address'); setCode(''); setError(null); }}>{copy.differentAddress}</button>
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
        </div>
      )}
      {step === 'done' && note && <p role="status">{note}</p>}
      {error && <p className="account__error" role="alert">{error}</p>}
    </div>
  );
}

type Confirm = null | { action: 'export' | 'delete'; stage: 'confirm' | 'sure' };

function SignedIn() {
  const account = useAccount();
  const [pending, setPending] = useState<string | null>(null);
  const [sure, setSure] = useState<string | null>(null);
  const [text, setText] = useState('');
  const [added, setAdded] = useState(false);
  const [confirm, setConfirm] = useState<Confirm>(null);
  const { busy, error, setError, run } = useGuard();

  useEffect(() => {
    void loadShelf().catch(() => undefined);
  }, []);

  const guard = (work: () => Promise<void>) => run(work);

  const open = (item: ShelfItem) => { setPending(item.session_id); void guard(() => openShelved(item)); };
  const remove = (id: string) => { setSure(null); void guard(() => deleteShelved(id)); };
  const add = (e: React.FormEvent) => {
    e.preventDefault();
    const normal = normalizeCode(text);
    if (!normal) { setError(copy.failed); return; }
    void guard(async () => { await attachCode(normal); setText(''); setAdded(true); });
  };

  const beginConfirm = (action: 'export' | 'delete') => { setError(null); setConfirm({ action, stage: 'confirm' }); };
  const confirmed = () => {
    if (!confirm) return;
    if (confirm.action === 'export') void guard(async () => { await exportData(); setConfirm(null); });
    else setConfirm({ ...confirm, stage: 'sure' });
  };

  return (
    <>
      {account.recoveryPending && <p className="account__error" role="alert">{copy.recoveryWaiting(dayOf(account.recoveryPending))}</p>}
      {account.balance && account.balance.codes_held > 0 && <p className="account__count">{copy.codeTokens(account.balance.code_tokens)}</p>}
      <div className="account__section">
        <h3>{copy.shelfHeading}</h3>
        {account.shelf === null && <p role="status">{copy.shelfLoading}</p>}
        {account.shelf !== null && account.shelf.length === 0 && <p>{copy.shelfEmpty}</p>}
        {account.shelf !== null && account.shelf.length > 0 && (
          <ul className="account__list">
            {account.shelf.map((item) => (
              <li key={item.session_id}>
                <p className="account__title">{item.title || item.worlds.join(', ')}</p>
                <p className="account__small">{[item.worlds.join(', '), item.started ? copy.started(dayOf(item.started)) : '', copy.turns(item.turns)].filter(Boolean).join(' · ')}</p>
                {sure === item.session_id ? (
                  <div role="group" aria-label={copy.removeSure}>
                    <p>{copy.removeSure}</p>
                    <button type="button" onClick={() => remove(item.session_id)}>{copy.removeYes}</button>
                    <button type="button" onClick={() => setSure(null)}>{copy.removeNo}</button>
                  </div>
                ) : (
                  <div className="account__actions">
                    {item.closed ? (
                      <span className="account__small">{copy.ended}</span>
                    ) : (
                      <button type="button" disabled={busy} onClick={() => open(item)}>{pending === item.session_id ? copy.opening : copy.open}</button>
                    )}
                    <button type="button" disabled={busy} onClick={() => setSure(item.session_id)}>{copy.remove}</button>
                  </div>
                )}
              </li>
            ))}
          </ul>
        )}
      </div>
      <form className="account__section" onSubmit={add}>
        <h3>{copy.addCodeHeading}</h3>
        <p>{copy.addCodeIntro}</p>
        <label htmlFor="account-add-code">{copy.addCodeLabel}</label>
        <input id="account-add-code" type="text" value={text} onChange={(e) => { setText(e.target.value); setAdded(false); }} autoComplete="off" autoCapitalize="characters" spellCheck={false} />
        <button type="submit" disabled={busy || text.trim() === ''}>{copy.addCode}</button>
        {added && <p role="status">{copy.codeAdded}</p>}
      </form>
      <SignInMethods />
      <div className="account__section">
        <h3>{copy.dataHeading}</h3>
        {confirm === null && (
          <div className="account__actions">
            <button type="button" onClick={() => beginConfirm('export')}>{copy.exportData}</button>
            <button type="button" onClick={() => beginConfirm('delete')}>{copy.deleteAccount}</button>
          </div>
        )}
        {confirm?.stage === 'confirm' && <StepUp busy={busy} run={run} fail={setError} onCancel={() => setConfirm(null)} onDone={confirmed} />}
        {confirm?.stage === 'sure' && (
          <div role="group" aria-label={copy.deleteWarning}>
            <p>{copy.deleteWarning}</p>
            <button type="button" disabled={busy} onClick={() => void guard(async () => { await deleteAccount(); closeAccountPanel(); })}>{copy.deleteYes}</button>
            <button type="button" onClick={() => setConfirm(null)}>{copy.deleteNo}</button>
          </div>
        )}
      </div>
      <div className="account__section">
        <button type="button" onClick={() => void signOut().then(closeAccountPanel)}>{copy.signOut}</button>
      </div>
      {error && <p className="account__error" role="alert">{error}</p>}
    </>
  );
}
