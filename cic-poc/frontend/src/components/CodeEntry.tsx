/**
 * The way in for a participant who holds a code, and the line that says how
 * much it has left. Shown only when the app is built with the module on.
 */
import { useEffect, useState } from 'react';
import { acceptCodeMessage, clearCode, deeperEnabled, openGetCode, saveCode, useDeeper } from '../lib/deeper';
import { deeperCopy } from '../lib/deeperCopy';

export function CodeEntry() {
  const { code, remaining } = useDeeper();
  const [open, setOpen] = useState(false);
  const [text, setText] = useState('');
  const [bad, setBad] = useState(false);

  useEffect(() => {
    if (!deeperEnabled) return;
    const onMessage = (event: MessageEvent) => {
      acceptCodeMessage(event);
    };
    window.addEventListener('message', onMessage);
    return () => window.removeEventListener('message', onMessage);
  }, []);

  if (!deeperEnabled) return null;

  const submit = (e: React.FormEvent) => {
    e.preventDefault();
    if (saveCode(text)) {
      setText('');
      setBad(false);
      setOpen(false);
    } else {
      setBad(true);
    }
  };

  return (
    <div className="code-entry sans">
      {code ? (
        <>
          <span className="code-entry__note" role="status">
            {remaining !== null ? deeperCopy.balance(remaining) : deeperCopy.saved}
          </span>
          <button type="button" onClick={clearCode}>
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
          <button type="button" onClick={openGetCode}>
            {deeperCopy.getCode}
          </button>
        </>
      )}
    </div>
  );
}
