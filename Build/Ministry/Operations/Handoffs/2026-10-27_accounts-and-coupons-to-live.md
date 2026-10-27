# Handoff — accounts and coupons to live, one thread — 2026-10-27

From: the accounts build thread (session https://claude.ai/code/session_01MRvT5j5mnHd2UgC4WXEp8E). To: the one thread Mark is starting to take accounts and coupons to production together. Mark's instruction: one thread, full access, remembers what is done and not done, sees the implementation through. Mark no longer trusts this thread's reporting, so check each line below against the repo before relying on it.

## Rules that bite here

- Read `CLAUDE.md` first. Participant-facing words are Mark's only; drafts go to him as an Artifact. One question at a time, with options and a recommendation.
- Promoting `main` to `live`, and any pull request into `live`, is Mark's call. Never do it.
- Merge your own pull request to `main` once every check is green. Read every check, including skipped ones; a draft pull request skips the frontend and Docker jobs, so mark it ready first.
- No model call, live test or paid run without Mark naming it with a cap.
- Mark has set the Render keys several times. Do not ask him about them again. If start-up refuses, read its message.
- Do not take on the "split by case" rule for under-18 handling (decision 63 ruling "split by case"). It was relayed to this thread by mistake. It belongs to a later item (A8), needs its own decision with Mark and the Facilitator governance review, and does not block adult-only accounts.

## Done and merged to main

Checked against `main` at `46f81dbdf` plus pull request 1176 (below).

- Accounts module `engine/accounts/` behind `CIC_ACCOUNTS_ENABLED`: typed emailed code sign-in (8 digits, newest 3 live per address), sessions, step-up, recovery code, address change, shelf, Google and Apple.
- SES mailer (`engine/api/ses_mailer.py`, words in `engine/api/ops/accounts-mail.yaml`). SES is out of the sandbox; sending domain, DKIM, MAIL FROM and DMARC verified; the send-only credential works; a test email passed SPF, DKIM and DMARC.
- Sealed backups (AES-256-GCM, `CIC_ACCOUNTS_BACKUP_KEY`); deletion ledger, erasure ledger and now closure marks written to the backup bucket and replayed on restore. Runbooks updated.
- Question text cleared at 90 days with the answers.
- Refill day fix for months with fewer days.
- Privacy sections for accounts written and hidden (`cic-website/privacy.html`, switch `accounts: false` in `cic-website/assets/go-deeper-config.js`).
- "Home" is now "account" everywhere a participant sees it. The button reads "Delete my account" (Mark's words).
- Deleting an account closes it for 90 days. Everything stays. Signing in during that time (code, Google or Apple) offers "Re-open my account" and does not spend the code until the person chooses. After the last day the account is erased. The two-year unused rule closes first. Decision-Log rulings 107 and 108.
- Coupons (pull request 1119, rulings 85 to 90): one kind, a gift with no deadline; one dashboard button; only the keyed hash of the address kept; attaches at the next sign-in by code, Google or Apple; unclaimed ones lapse after 90 days; pending list and cancel on the dashboard. Notice words are Mark's.

## In flight

- Pull request 1176 (branch `claude/stoic-goldberg-fpitc3`, draft): started as a tests-only fix for the live-surface commentary check (dates written out in two new test files). It now also carries the fixes from the independent review of the closing build:
  - the last day still belongs to the person; erasure waits until the day after; a sign-in after that gets the plain "did not work" reply;
  - re-opening and erasing test the same row, so exactly one wins; an erasure that meets a re-opened account leaves it whole, with its contact intact;
  - a closure mark written while the account is re-opened is taken back out;
  - the two-year sweep decides in the same step as the write, so a person who signs in meanwhile stays open;
  - deleting ends a waiting recovery; a second delete at once answers ok;
  - the wrong-code test now compares the reply with a stranger's.
  Local checks: accounts suite 240 passed; shelf, ledger, routes, proofs and allowance suites 135 passed (run `python -m engine.m2.cli restore` first if a test says "world temporarily unavailable"); live-commentary check clean. CI on the new push has not run.
- A second independent review, a security review of the whole accounts system, was started and may have finished by the time this is read. Its report was sent to the accounts thread and is not in the repo. Ask Mark whether it arrived; if not, run it again before the flag goes on. Read-only, Opus, no model call beyond the subagent.

## Not done

1. Merge pull request 1176 once every check is green (mark it ready first).
2. Security review findings, if any: fix and merge.
3. Known low item left as a documented choice: a backup restored from before a re-open brings the closure back, and the account is erased on its last day unless the person signs in again. Add a line to the restore runbook (`Build/Ministry/Operations/Standing/CiC_Backup_Restore_Runbook.md`, "Closed accounts stay closed").
4. Mark's words still needed (draft each to him as an Artifact, one at a time):
   - the privacy retention line. Proposed: "A conversation you save in your account stays until you delete it or your account is erased." Not yet answered. The page's "We delete a conversation after 90 days" is false for saved conversations once accounts are on;
   - the coupon privacy sentence about waiting coupons (`Build/Ministry/Features/Coupons/Later_List.md` item 1);
   - approval of the delete screen, the confirmation after deleting, and the re-open screen. Current drafts are in `cic-poc/frontend/src/lib/accountsCopy.ts` (`deleteWhen`, `deletedDone`, `closedText`, `reopenYes`, `reopenNo`); only "you have 90 days to re-open it" is Mark's exact sentence.
5. Coupon limits in `engine/deeper/ops/go-deeper.yaml`, section `coupon`: `max_tokens` 20000 and `max_per_day` 20 are stated defaults, not Mark's rulings. Not a blocker; tell him they exist.
6. Turn-on: the checklist is at https://claude.ai/artifact/5e6ZW3VDehHT9Kaw1enDmx (private to Mark). Three switches set together: `CIC_ACCOUNTS_ENABLED` on Render, `VITE_ACCOUNTS_ENABLED=on` in the Docker build, and `accounts: true` in `cic-website/assets/go-deeper-config.js` (reaches the site through promotion). Then one rehearsal on Mark's own address: coupon made for it, sign in, see the gift notice, delete, re-open, check the gift is still there.
7. Promotion of `main` to `live` through `Build/Ministry/Operations/Standing/CiC_Promotion_Runbook.md`: Mark's call.
8. Mark's irreversible decision: clearing question text at 90 days reaches live with the next promotion.
9. Open check of Mark's in AWS: the default configuration set `my-first-configuration-set` in SES. Any event destinations or open/click tracking on it should be removed. Mark has not confirmed.
10. Legal question 14 (whether "promotional" is enough for coupons) is open with the professional. Mark's call whether it blocks the pilot; it does not block the build.

## From the coupons thread (its closing report, 2026-10-27)

Its work is all merged (pull requests 1119, 1135, 1138; rulings 85 to 90 and 101 to 104). Where it attaches: `AccountsService._sign_in_as` (code) and `_sign_in_by_provider` (Google, Apple, via `ProviderVerifier.verified_address`; an Apple relay address never matches); redemption is `_redeem_coupons` and never fails a sign-in. `engine/api/coupon_routes.py` is mounted only when Deeper and accounts are both on and sets `service.coupon_code_hash`; without it coupons wait. The meter's id for an attached coupon is `coupon_` plus a keyed value of the pending id, so to cancel an attached coupon use the id in the dashboard grants list.

Not tested live (the sandbox has no SES, Render or AWS):
1. A real coupon end to end: approve to Mark's address, sign in by code, see the notice and the "Gift" line, tokens spent from the coupon, a second sign-in shows no notice.
2. Google and Apple coupon match (needs the client ids).
3. That `pending_coupons` is carried and restored by the sealed accounts backup.
4. Dashboard admin requests are limited to 10 a minute per address and a page load uses most of that, which gave Mark a 429 ("The room is full") on button presses. Easing it is Mark's call, because the limit also slows admin-token guessing.

`main` is far ahead of `live` (159 commits, 334 files at the time), mostly other threads' work, so promotion carries more than accounts and coupons. Mark decides.

## Dependencies

- Coupons attach only at sign-in, so coupons cannot go live before accounts do. Go live together.
- A closed account's waiting coupon attaches when the person re-opens it, because redemption runs at sign-in.

## Spend

Sonnet for building, Opus for reviews (as the rules say). No metered model call, live test or paid run by this thread. One SES test email sent by Mark.
