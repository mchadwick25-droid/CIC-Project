import { useState } from 'react';
import { AccountsError } from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';

export function messageOf(error: unknown): string {
  if (error instanceof AccountsError) return error.status === 0 ? copy.offline : error.message || copy.failed;
  return copy.failed;
}

/** Runs one request at a time and keeps the plain message of a refusal. Resolves true when it worked. */
export function useGuard() {
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState<string | null>(null);
  const run = async (work: () => Promise<void>): Promise<boolean> => {
    setBusy(true);
    setError(null);
    try {
      await work();
      return true;
    } catch (err) {
      setError(messageOf(err));
      return false;
    } finally {
      setBusy(false);
    }
  };
  return { busy, error, setError, run };
}
