import { accountsEnabled, useAccount } from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';

/** One quiet line, once a signed-in person's conversation is on their shelf. */
export function SavedToHome() {
  const account = useAccount();
  if (!accountsEnabled || account.status !== 'in' || account.lastShelved !== true) return null;
  return <p className="conversation__saved sans" role="status">{copy.savedToHome}</p>;
}
