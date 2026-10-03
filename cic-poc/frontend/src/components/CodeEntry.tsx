/**
 * The way in for a participant who holds a code, and the line that says how
 * much it has left. Shown only when the app is built with the module on.
 */
import { useState } from 'react';
import { acceptClaim, addCode, declineClaim, deeperEnabled, getCodeUrl, openGetCode, removeCode, useDeeper } from '../lib/deeper';
import { deeperCopy } from '../lib/deeperCopy';

export function CodeEntry() {
  const { codes, remaining, low, claim } = useDeeper();
  const held = codes.length > 0;
  const [open, setOpen] = useState(false);
  const [text, setText] = useState('');
  const [bad, setBad] = useState(false);

  if (!deeperEnabled) return null;

  const submit = async (e: React.FormEvent) => {
    e.preventDefault();
    if (await addCode(text)) {
      setText('');
      setBad(false);
      setOpen(false);
    } else {
      setBad(true);
    }
  };

  const getCode = () => {
    if (!openGetCode()) window.location.assign(getCodeUrl());
  };

  if (claim) {
    return (
      <div className="code-entry sans">
        <div className="code-entry__form" role="group" aria-label={deeperCopy.claimAsk}>
          <p className="code-entry__note">
            {deeperCopy.claimAsk}
            {held ? ` ${deeperCopy.claimReplace}` : ''}
          </p>
          <button type="button" onClick={acceptClaim} disabled={claim.status === 'working'}>
            {deeperCopy.claimUse}
          </button>
          <button type="button" onClick={declineClaim}>
            {deeperCopy.claimLater}
          </button>
          {claim.status === 'failed' && (
            <p className="code-entry__error" role="alert">
              {deeperCopy.claimFailed}
            </p>
          )}
        </div>
      </div>
    );
  }

  return (
    <div className="code-entry sans">
      {held && !open ? (
        <>
          <span className="code-entry__note" role="status">
            {remaining !== null ? deeperCopy.balance(remaining) : deeperCopy.saved}
            {low ? ` ${deeperCopy.low}` : ''}
          </span>
          <button type="button" onClick={getCode}>
            {deeperCopy.getMore}
          </button>
          <button type="button" onClick={() => setOpen(true)}>
            {deeperCopy.haveCode}
          </button>
          <button type="button" onClick={removeCode}>
            {deeperCopy.removeCode}
          </button>
        </>
      ) : open ? (
        <form className="code-entry__form" onSubmit={submit}>
          <label htmlFor="code-entry-field">{deeperCopy.fieldLabel}</label>
          <input
            id="code-entry-field"
            type="text"
            value={text}
            onChange={(e) => setText(e.target.value)}
            autoComplete="off"
            autoCapitalize="characters"
            spellCheck={false}
            aria-invalid={bad}
            aria-describedby={bad ? 'code-entry-error' : undefined}
          />
          <button type="submit">{deeperCopy.useCode}</button>
          {bad && (
            <p id="code-entry-error" className="code-entry__error" role="alert">
              {deeperCopy.badCode}
            </p>
          )}
        </form>
      ) : (
        <>
          <button type="button" onClick={() => setOpen(true)}>
            {deeperCopy.haveCode}
          </button>
          <button type="button" onClick={getCode}>
            {deeperCopy.getCode}
          </button>
        </>
      )}
    </div>
  );
}
