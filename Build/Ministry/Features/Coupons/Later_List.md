# Coupons: later list

Built on 2026-10-24 under the rulings of that date in `Build/Ministry/Features/Go-Deeper/Decision-Log.md` (85 to 90). Not blocking.

1. Privacy page. It should say that the project lead can keep a coupon under the keyed hash of an address until the person signs in or 90 days pass, and that the address is dropped after hashing, as a verified Google address is when it is used to find a coupon. The words are Mark's.
2. Starting numbers in `engine/deeper/ops/go-deeper.yaml`, section `coupon`: `max_tokens` 20000, `max_per_day` 20, `unclaimed_days` 90 (Mark ruled the 90; the other two are stated defaults for him to change by pull request).
3. Mail. A coupon cannot attach until a person can sign in, which needs the accounts `Mailer`. Mark named Amazon SES; no sender exists yet (accounts thread).
4. Apple's hide-my-email address never matches a typed address. That person receives a waiting coupon only by signing in once with the emailed code.
5. A person signed in on a live session is not signed in again, so a coupon waits for their next sign-in (sessions end at 14 days idle or 60 days).
6. Price cut at checkout (Mark's "discount"): not built. It needs a Stripe promotion code and a checkout that knows the account, and waits for buying to reopen.
7. `cic-poc/frontend/src/lib/accountsCopy.ts` still says "home" in older lines. Mark's change from "home" to "account" was made on the two coupon lines only.
8. Backups. The durable accounts file is not in the daily backup until accounts slice A5, so a waiting coupon would not survive a restore. An attached coupon lives in the meter, which is backed up.
9. The meter's id for an attached coupon is a keyed value of the waiting coupon's id, so the account file and the meter never hold the same string for it (accounts proof A6). To cancel an attached coupon, use its id in the grants list, not the id shown at approval.
