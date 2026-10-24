# Accounts: later list

Not blocking. Nothing here stops accounts from working online.

1. Google and Apple sign-in, live check. Needs a Google sign-in client and an Apple Services ID. Set `CIC_ACCOUNTS_GOOGLE_CLIENT_ID` and `CIC_ACCOUNTS_APPLE_CLIENT_ID`. The Apple Services ID must list the site's address as a return URL. Steps to be given when wanted.
2. Words to approve in `cic-poc/frontend/src/lib/accountsCopy.ts` that are not on the design boards: the My home / Sign in button in the panel on the Launch screen, "How you sign in" under Settings, "tokens on your codes" on the home card, "Delete" / "Delete this conversation for good?" for ended conversations, and the Google and Apple screens.
3. Website masthead "My home" link. The app opens its home from `#home`. The link belongs on the site.
4. Gift lines on the home ("1,100 gift, until 20 January"). The server does not report gifts yet.
5. Build Plan artifact: amend A4 from rulings 55 to 60. Optional.
6. Rulings 57 and 58 (spent line, day free tokens return). With the visitor-limit thread.
7. Small edges: accounts on with Go Deeper off leaves only `#home` to sign in; a full shelf at sign-in is silent.
8. Still open from before: SES production access and settings, Stripe facts, turning accounts on (A7), A5 (privacy page, deletion inventory, incident runbook).
9. Closed (rulings 93 and 95): each deletion-ledger entry and each erasure entry is also written to the backup bucket and replayed on restore.
