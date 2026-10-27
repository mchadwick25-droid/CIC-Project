import { useEffect, useState } from 'react';
import { accountsEnabled, attachCode, dismissSavedCodeOffer, refresh, useAccount } from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';
import { refreshBalances, useDeeper } from '../lib/deeper';

type Answer = 'asking' | 'busy' | 'added' | 'kept' | 'failed';

const OFFERED_KEY = 'cic_codes_offered';

function offeredCodes(): string[] {
  try {
    const raw = localStorage.getItem(OFFERED_KEY);
    const parsed: unknown = raw ? JSON.parse(raw) : [];
    return Array.isArray(parsed) ? parsed.filter((c): c is string => typeof c === 'string') : [];
  } catch {
    return [];
  }
}

function markOffered(codes: string[]) {
  try {
    localStorage.setItem(OFFERED_KEY, JSON.stringify([...new Set([...offeredCodes(), ...codes])]));
  } catch {
    // Storage blocked: the offer may come again at the next sign-in.
  }
}

/** Shown once, right after a sign-in, when this browser already holds a purchased code. It names the tokens and asks. */
export function SavedCodeOffer() {
  const account = useAccount();
  const deeper = useDeeper();
  const [answer, setAnswer] = useState<Answer>('asking');
  const pending = accountsEnabled && account.status === 'in' && account.savedCodeOffer;
  useEffect(() => {
    if (pending) void refreshBalances();
    else setAnswer('asking');
  }, [pending]);
  if (!pending) return null;
  const asked = offeredCodes();
  const held = deeper.codes.filter((code) => (deeper.balances[code] ?? 0) > 0 && !asked.includes(code));
  const tokens = held.reduce((sum, code) => sum + (deeper.balances[code] ?? 0), 0);
  if (answer === 'asking' && held.length === 0) return null;

  const add = async () => {
    setAnswer('busy');
    try {
      for (const code of held) await attachCode(code);
      markOffered(held);
      await refresh();
      setAnswer('added');
    } catch {
      setAnswer('failed');
    }
  };

  if (answer === 'added' || answer === 'kept' || answer === 'failed') {
    return (
      <div className="account__section gift-notice" role="status">
        <p>{answer === 'added' ? copy.codeAdded : answer === 'kept' ? copy.savedCodeKept : copy.failed}</p>
        <button type="button" onClick={dismissSavedCodeOffer}>{copy.gotIt}</button>
      </div>
    );
  }
  return (
    <div className="account__section gift-notice" role="status">
      <p>{copy.savedCodeOffer(tokens)}</p>
      <button type="button" disabled={answer === 'busy'} onClick={() => void add()}>{copy.savedCodeAdd}</button>
      <button type="button" disabled={answer === 'busy'} onClick={() => { markOffered(held); setAnswer('kept'); }}>{copy.savedCodeKeep}</button>
    </div>
  );
}
