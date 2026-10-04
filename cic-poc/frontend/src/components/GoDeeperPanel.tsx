/**
 * The offer to go deeper, beside the conversation. A strip says how many
 * tokens are left; the panel opens when a turn is refused for want of them or
 * when the person asks, never on its own. Shown only when the app is built
 * with the module on.
 */
import { useEffect, useState } from 'react';
import { acceptClaim, addCode, closePanel, declineClaim, deeperEnabled, formatCode, getCodeUrl, openGetCode, openPanel, removeCode, useDeeper } from '../lib/deeper';
import { deeperCopy } from '../lib/deeperCopy';

export function GoDeeperPanel() {
  const { codes, remaining, low, claim, panelOpen } = useDeeper();
  const held = codes.length > 0;
  const [entering, setEntering] = useState(false);
  const [text, setText] = useState('');
  const [bad, setBad] = useState(false);
  const [revealed, setRevealed] = useState(false);

  useEffect(() => {
    if (!panelOpen) return undefined;
    const onKey = (event: KeyboardEvent) => {
      if (event.key === 'Escape') closePanel();
    };
    window.addEventListener('keydown', onKey);
    return () => window.removeEventListener('keydown', onKey);
  }, [panelOpen]);

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
      <div className="go-deeper__bar">
        {held && remaining !== null && (
          <span className="go-deeper__count" role="status">
            {deeperCopy.balance(remaining)}
            {low ? ` ${deeperCopy.low}` : ''}
          </span>
        )}
        <button type="button" aria-expanded={panelOpen} aria-controls="go-deeper-panel" onClick={panelOpen ? closePanel : openPanel}>
          {deeperCopy.open}
        </button>
      </div>
      {panelOpen && (
        <aside id="go-deeper-panel" className="go-deeper__panel" aria-label={deeperCopy.heading}>
          <div className="go-deeper__head">
            <h2>{deeperCopy.heading}</h2>
            <button type="button" onClick={closePanel}>
              {deeperCopy.close}
            </button>
          </div>
          {claim ? (
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
                  {deeperCopy.claimFailed}
                </p>
              )}
            </div>
          ) : (
            <>
              <p>{deeperCopy.intro}</p>
              {held && remaining !== null && (
                <p className="go-deeper__count">
                  {deeperCopy.balance(remaining)}
                  {low ? ` ${deeperCopy.low}` : ''}
                </p>
              )}
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
          )}
        </aside>
      )}
    </div>
  );
}
