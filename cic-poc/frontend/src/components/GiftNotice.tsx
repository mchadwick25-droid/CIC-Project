import { accountsEnabled, dismissGiftNotice, useAccount } from '../lib/accounts';
import { accountsCopy as copy } from '../lib/accountsCopy';

/** Shown once, at the sign-in where a gift coupon attached. It names the amount and nothing else. */
export function GiftNotice() {
  const account = useAccount();
  if (!accountsEnabled || account.status !== 'in' || account.giftNotice.length === 0) return null;
  return (
    <div className="account__section gift-notice" role="status">
      {account.giftNotice.map((n, i) => <p key={i}>{copy.giftAdded(n)}</p>)}
      <button type="button" onClick={dismissGiftNotice}>{copy.gotIt}</button>
    </div>
  );
}
