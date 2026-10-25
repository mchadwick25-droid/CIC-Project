/**
 * The offer to go deeper, beside the conversation. A strip says how many
 * tokens are left; the panel opens when a turn is refused for want of them or
 * when the person asks, never on its own. Shown only when the app is built
 * with the module on.
 */
import { useEffect, useRef, useState } from 'react';
import { acceptClaim, addCode, closePanel, declineClaim, deeperEnabled, formatCode, getCodeUrl, openGetCode, openPanel, refreshBalances, refreshFreeLeft, removeCode, useDeeper } from '../lib/deeper';
import { deeperCopy, pilotCopy } from '../lib/deeperCopy';
import { giftLinks } from '../lib/giftLinks';
import { dismissPilot, usePilot } from '../lib/pilot';
import { peakBalance } from '../lib/balancePeak';
import { accountsEnabled, closeSignIn, openHome, openSignIn, useAccount } from '../lib/accounts';
import { accountsCopy } from '../lib/accountsCopy';
import { SignInSteps } from './SignInSteps';

const LOW_AT = 100;

export function GoDeeperPanel({ panelOnly = false }: { panelOnly?: boolean } = {}) {
  const { codes, remaining, low, freeLeft, claim, panelOpen } = useDeeper();
  const pilot = usePilot();
  const account = useAccount();
  const held = codes.length > 0;
  const accountBalance = accountsEnabled && account.status === 'in' ? account.balance : null;
  const count = accountBalance ? accountBalance.free_left + accountBalance.code_tokens : held ? (remaining === null ? null : remaining + (freeLeft ?? 0)) : freeLeft;
  const [entering, setEntering] = useState(false);
  const [text, setText] = useState('');
  const [bad, setBad] = useState(false);
  const [revealed, setRevealed] = useState(false);
  const toggleRef = useRef<HTMLButtonElement>(null);
  const wasOpen = useRef(false);
  const headRef = useRef<HTMLHeadingElement>(null);

  // A code on screen never outlives the panel: closing hides it, so a panel that
  // opens itself later at a limit starts with the code out of sight.
  useEffect(() => {
    if (!panelOpen) {
      setRevealed(false);
      closeSignIn();
    }
    // Closing returns the person to the control that opened it.
    if (wasOpen.current && !panelOpen) toggleRef.current?.focus();
    wasOpen.current = panelOpen;
  }, [panelOpen]);

  // Shown alone inside the site's slide-out frame: the panel opens at once, and
  // closing it tells the site page to put its drawer away.
  const opened = useRef(false);
  useEffect(() => {
    if (!panelOnly) return;
    if (panelOpen) opened.current = true;
    else if (opened.current) window.parent.postMessage({ type: 'cic:panel-close' }, '*');
  }, [panelOnly, panelOpen]);
  useEffect(() => {
    if (!panelOnly) return undefined;
    openPanel();
    const onMessage = (event: MessageEvent) => {
      if (event.source === window.parent && (event.data as { type?: string } | null)?.type === 'cic:panel-open') openPanel();
    };
    window.addEventListener('message', onMessage);
    return () => window.removeEventListener('message', onMessage);
  }, [panelOnly]);

  useEffect(() => {
    if (!panelOpen) return undefined;
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') closePanel();
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [panelOpen]);

  useEffect(() => {
    void refreshFreeLeft();
    void refreshBalances();
  }, [codes.length]);

  const signingIn = deeperEnabled && accountsEnabled && account.signInOpen && account.status !== 'in';
  useEffect(() => {
    if (signingIn) headRef.current?.focus();
  }, [signingIn]);

  if (!deeperEnabled) return null;

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (await addCode(text)) {
      setText('');
      setBad(false);
      setEntering(false);
    } else {
      setBad(true);
    }
  };

  const getMore = () => {
    if (!openGetCode()) window.location.assign(getCodeUrl());
  };

  return (
    <div className="go-deeper sans">
      {!panelOnly && (
      <div className="go-deeper__ribbon">
        {count !== null && (
          <span className={count < LOW_AT ? 'go-deeper__count go-deeper__count--low' : 'go-deeper__count'} role="status">
            {deeperCopy.left(count)}
          </span>
        )}
        <button ref={toggleRef} type="button" aria-expanded={panelOpen} aria-controls="go-deeper-panel" onClick={panelOpen ? closePanel : openPanel}>
          {deeperCopy.open}
        </button>
        {count !== null && <i className="go-deeper__line" style={{ width: `${Math.min(100, (count / peakBalance(count)) * 100)}%` }} />}
      </div>
      )}
      {panelOpen && (
        <aside id="go-deeper-panel" className="go-deeper__panel" aria-label={deeperCopy.heading}>
          <div className="go-deeper__head">
            <h2 ref={headRef} tabIndex={-1}>{signingIn ? accountsCopy.signInOrUp : deeperCopy.heading}</h2>
            {signingIn ? (
              <button type="button" onClick={closeSignIn}>
                {accountsCopy.back}
              </button>
            ) : (
              <button type="button" onClick={closePanel}>
                {deeperCopy.close}
              </button>
            )}
          </div>
          {signingIn && (
            <SignInSteps
              onSignedIn={() => {
                closeSignIn();
                closePanel();
              }}
            />
          )}
          {pilot.status && (
            <div className="go-deeper__section" role="group" aria-label={pilotCopy.group}>
              {pilot.status === 'joining' && <p role="status">{pilotCopy.joining}</p>}
              {pilot.status === 'ready' && (
                <>
                  <h3>{pilotCopy.readyHeading}</h3>
                  {pilot.tokens !== null && pilot.conversations !== null && <p>{pilotCopy.ready(pilot.tokens, pilot.conversations)}</p>}
                  <button type="button" onClick={() => { dismissPilot(); closePanel(); }}>
                    {pilotCopy.start}
                  </button>
                </>
              )}
              {pilot.status === 'already' && <p>{pilotCopy.already}</p>}
              {pilot.status === 'full' && <p>{pilotCopy.full}</p>}
              {pilot.status === 'ended' && <p>{pilotCopy.ended}</p>}
              {pilot.status === 'address_limit' && <p>{pilotCopy.addressLimit}</p>}
              {pilot.status === 'failed' && <p role="alert">{pilotCopy.failed}</p>}
            </div>
          )}
          {!signingIn && (claim ? (
            <div className="go-deeper__section" role="group" aria-label={deeperCopy.claimAsk}>
              <p>
                {deeperCopy.claimAsk}
                {held ? ` ${deeperCopy.claimReplace}` : ''}
              </p>
              <div className="go-deeper__actions">
                <button type="button" onClick={acceptClaim} disabled={claim.status === 'working'}>
                  {deeperCopy.claimUse}
                </button>
                <button type="button" onClick={declineClaim}>
                  {deeperCopy.claimLater}
                </button>
              </div>
              {claim.status === 'failed' && (
                <p className="go-deeper__error" role="alert">
                  {claim.code !== undefined ? deeperCopy.badCode : deeperCopy.claimFailed}
                </p>
              )}
            </div>
          ) : (
            <>
              <p>{held ? deeperCopy.introHeld : deeperCopy.intro}</p>
              {held && remaining !== null && (
                <p className="go-deeper__count">
                  {deeperCopy.balance(remaining)}
                  {low ? ` ${deeperCopy.low}` : ''}
                </p>
              )}
              {freeLeft !== null && (!held || freeLeft > 0) && <p className="go-deeper__count">{deeperCopy.freeLeft(freeLeft)}</p>}
              <div className="go-deeper__actions">
                <button type="button" onClick={getMore}>
                  {deeperCopy.getMore}
                </button>
                {!entering && (
                  <button type="button" onClick={() => setEntering(true)}>
                    {deeperCopy.haveCode}
                  </button>
                )}
              </div>
              {entering && (
                <form className="go-deeper__form" onSubmit={submit}>
                  <label htmlFor="go-deeper-field">{deeperCopy.fieldLabel}</label>
                  <input
                    id="go-deeper-field"
                    type="text"
                    value={text}
                    onChange={(e) => setText(e.target.value)}
                    autoComplete="off"
                    autoCapitalize="characters"
                    spellCheck={false}
                    aria-invalid={bad}
                    aria-describedby={bad ? 'go-deeper-error' : undefined}
                  />
                  <button type="submit">{deeperCopy.useCode}</button>
                  {bad && (
                    <p id="go-deeper-error" className="go-deeper__error" role="alert">
                      {deeperCopy.badCode}
                    </p>
                  )}
                </form>
              )}
              {held && (
                <div className="go-deeper__section">
                  <button type="button" aria-expanded={revealed} onClick={() => setRevealed(!revealed)}>
                    {revealed ? deeperCopy.hideCode : deeperCopy.showCode}
                  </button>
                  {revealed && codes.map((code) => <p key={code} className="go-deeper__code">{deeperCopy.yourCode(formatCode(code))}</p>)}
                  <button type="button" onClick={removeCode}>
                    {deeperCopy.removeCode}
                  </button>
                </div>
              )}
            </>
          ))}
          {!signingIn && !claim && (
            <div className="go-deeper__section go-deeper__give">
              <p className="go-deeper__eyebrow">{deeperCopy.giveEyebrow}</p>
              <h3>{deeperCopy.giveHeading}</h3>
              <p>{deeperCopy.giveBody}</p>
              <div className="go-deeper__actions">
                <a href={giftLinks.once} target="_blank" rel="noopener noreferrer">
                  {deeperCopy.giveOnce}
                </a>
                <a href={giftLinks.monthly} target="_blank" rel="noopener noreferrer">
                  {deeperCopy.giveMonthly}
                </a>
              </div>
              <p className="go-deeper__fine">{deeperCopy.giveFine}</p>
            </div>
          )}
          {!signingIn && !claim && accountsEnabled && account.status !== 'off' && account.status !== 'unknown' && (
            <div className="go-deeper__section go-deeper__account">
              {account.status === 'out' ? (
                <>
                  <h3>{accountsCopy.keepHeading}</h3>
                  <p>{accountsCopy.keepBody}</p>
                  <button type="button" onClick={openSignIn}>
                    {accountsCopy.signInOrUp}
                  </button>
                </>
              ) : (
                <button type="button" onClick={() => { closePanel(); openHome(); }}>
                  {accountsCopy.menuHome}
                </button>
              )}
            </div>
          )}
        </aside>
      )}
    </div>
  );
}
