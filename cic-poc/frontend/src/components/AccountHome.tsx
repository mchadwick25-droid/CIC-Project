/**
 * My home: the account's page. It holds the count, the saved conversations and the settings. Signed
 * out, the same page is the sign-in. Shown only when the app is built with accounts on.
 */
import { useEffect, useRef, useState } from 'react';
import { accountsEnabled, attachCode, closeHome, loadShelf, openHome, openShelved, refresh, signOut, signOutEverywhere, cancelRecoverySignedIn, useAccount, readStoredConversation, type ShelfItem } from '../lib/accounts';
import { normalizeCode } from '../lib/deeper';
import { accountsCopy as copy } from '../lib/accountsCopy';
import { AddressScreen, DeleteScreen, ExportScreen, MethodsScreen, RecoveryScreen } from './HomeScreens';
import { SignInSteps } from './SignInSteps';
import { dayOf } from './dayOf';
import { useGuard } from './useGuard';
import { getCodeUrl, openGetCode } from '../lib/deeper';

type Screen = 'main' | 'recovery' | 'address' | 'methods' | 'export' | 'delete';

function shortDay(iso: string | null): string {
  if (!iso) return '';
  const today = new Date().toISOString().slice(0, 10);
  if (iso.slice(0, 10) === today) return 'Today';
  const date = new Date(`${iso.slice(0, 10)}T12:00:00Z`);
  return Number.isNaN(date.getTime()) ? iso.slice(0, 10) : date.toLocaleDateString('en-GB', { day: 'numeric', month: 'long', timeZone: 'UTC' });
}

export function AccountHome() {
  const account = useAccount();
  const headRef = useRef<HTMLHeadingElement>(null);

  useEffect(() => {
    if (!accountsEnabled) return;
    void refresh();
    if (window.location.hash === '#home') openHome();
  }, []);

  useEffect(() => {
    if (account.homeOpen) headRef.current?.focus();
  }, [account.homeOpen]);

  useEffect(() => {
    if (!account.homeOpen) return undefined;
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') closeHome();
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [account.homeOpen]);

  if (!accountsEnabled || !account.homeOpen || account.status === 'off') return null;

  return (
    <main className="account-home account sans" aria-label={account.status === 'in' ? copy.homeHeading : copy.homeSignedOutHeading}>
      <div className="account-home__bar">
        <button type="button" onClick={closeHome}>{readStoredConversation() ? copy.backToConversation : copy.backToSite}</button>
      </div>
      {account.status === 'in' ? (
        <Home headRef={headRef} />
      ) : (
        <div className="account-home__body">
          <h1 ref={headRef} tabIndex={-1}>{copy.homeSignedOutHeading}</h1>
          {account.status !== 'unknown' && <SignInSteps onSignedIn={() => undefined} />}
          <p className="account__small">{copy.newHere}</p>
          <button type="button" onClick={closeHome}>{copy.startWithout}</button>
        </div>
      )}
    </main>
  );
}

function Home({ headRef }: { headRef: React.RefObject<HTMLHeadingElement> }) {
  const account = useAccount();
  const [screen, setScreen] = useState<Screen>('main');
  const [pending, setPending] = useState<string | null>(null);
  const [entering, setEntering] = useState(false);
  const [text, setText] = useState('');
  const [added, setAdded] = useState(false);
  const { busy, error, setError, run } = useGuard();
  const back = () => setScreen('main');

  useEffect(() => {
    void loadShelf().catch(() => undefined);
  }, []);

  if (screen === 'recovery') return <div className="account-home__body"><RecoveryScreen onBack={back} /></div>;
  if (screen === 'address') return <div className="account-home__body"><AddressScreen onBack={back} /></div>;
  if (screen === 'methods') return <div className="account-home__body"><MethodsScreen onBack={back} /></div>;
  if (screen === 'export') return <div className="account-home__body"><ExportScreen onBack={back} /></div>;
  if (screen === 'delete') return <div className="account-home__body"><DeleteScreen onBack={back} /></div>;

  const balance = account.balance;
  const open = (item: ShelfItem) => { setPending(item.session_id); void run(() => openShelved(item)); };
  const getMore = () => {
    closeHome();
    if (!openGetCode()) window.location.assign(getCodeUrl());
  };
  const add = (e: React.FormEvent) => {
    e.preventDefault();
    const normal = normalizeCode(text);
    if (!normal) { setError(copy.failed); return; }
    void run(async () => { await attachCode(normal); setText(''); setAdded(true); setEntering(false); });
  };
  const canChooseMethods = account.methods.some((m) => m !== 'address') || Object.keys(account.providers).length > 0;

  return (
    <div className="account-home__body">
      <h1 ref={headRef} tabIndex={-1}>{copy.homeHeading}</h1>
      <p className="account__small">{copy.homeNote}</p>
      {account.recoveryPending && (
        <div className="account__section" role="alert">
          <p>{copy.recoveryWaiting(dayOf(account.recoveryPending))}</p>
          <button type="button" disabled={busy} onClick={() => void run(cancelRecoverySignedIn)}>{copy.stopRecovery}</button>
        </div>
      )}
      {balance && (
        <div className="account-home__card">
          <p className="account-home__count" role="status">{copy.tokensLeft(balance.free_left + balance.code_tokens)}</p>
          <p>{copy.freeRefill(balance.free_left, balance.free_total, account.refillDay)}</p>
          {balance.codes_held > 0 && <p>{copy.codeTokens(balance.code_tokens)}</p>}
          <p className="account__small">{copy.freeFirst}</p>
          <button type="button" onClick={getMore}>{copy.getMore}</button>
          {!entering && <button type="button" onClick={() => { setEntering(true); setAdded(false); }}>{copy.addCodeLink}</button>}
          {entering && (
            <form onSubmit={add}>
              <label htmlFor="account-add-code">{copy.addCodeLabel}</label>
              <input id="account-add-code" type="text" value={text} onChange={(e) => setText(e.target.value)} autoComplete="off" autoCapitalize="characters" spellCheck={false} />
              <button type="submit" disabled={busy || text.trim() === ''}>{copy.addCode}</button>
            </form>
          )}
          {added && <p role="status">{copy.codeAdded}</p>}
        </div>
      )}
      {!account.hasRecoveryCode && account.shelf !== null && account.shelf.length > 0 && (
        <div className="account__section">
          <p>{copy.recoveryPrompt}</p>
          <button type="button" onClick={() => setScreen('recovery')}>{copy.getRecoveryCode}</button>
        </div>
      )}
      <h2>{copy.conversationsHeading}</h2>
      {account.shelf === null && <p role="status">{copy.conversationsLoading}</p>}
      {account.shelf !== null && account.shelf.length === 0 && <p>{copy.conversationsEmpty}</p>}
      {account.shelf !== null && account.shelf.length > 0 && (
        <ul className="account__list">
          {account.shelf.map((item) => (
            <li key={item.session_id}>
              {item.closed ? (
                <>
                  <span className="account__title">{item.worlds.join(', ')}</span>
                  <span className="account__small">{shortDay(item.last_active)} · {copy.ended}</span>
                </>
              ) : (
                <button type="button" disabled={busy} onClick={() => open(item)}>
                  <span className="account__title">{item.worlds.join(', ')}</span>
                  <span className="account__small">{pending === item.session_id ? copy.opening : shortDay(item.last_active)}</span>
                </button>
              )}
            </li>
          ))}
        </ul>
      )}
      <p className="account__small">{copy.conversationsNote}</p>
      <h2>{copy.settingsHeading}</h2>
      <ul className="account__list">
        {account.methods.includes('address') && <li><button type="button" onClick={() => setScreen('address')}>{copy.changeAddress}</button></li>}
        {canChooseMethods && <li><button type="button" onClick={() => setScreen('methods')}>{copy.methodsHeading}</button></li>}
        <li><button type="button" onClick={() => setScreen('recovery')}>{copy.recoveryCode}</button></li>
        <li><button type="button" onClick={() => setScreen('export')}>{copy.exportData}</button></li>
        <li><button type="button" onClick={() => void signOut().then(closeHome)}>{copy.signOut}</button></li>
        <li><button type="button" onClick={() => void signOutEverywhere().then(closeHome)}>{copy.signOutEverywhere}</button></li>
        <li><button type="button" className="account__danger" onClick={() => setScreen('delete')}>{copy.deleteHome}</button></li>
      </ul>
      {error && <p className="account__error" role="alert">{error}</p>}
    </div>
  );
}
