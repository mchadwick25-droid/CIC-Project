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

## Security review of the accounts system (Opus, read-only, 2026-10-27)

Finding 1 (a closed account re-opened on its last day and then erased anyway; a waiting recovery surviving a delete; the two-year close not re-checking use) is fixed in pull request 1176. The rest is open:

2. **Needs Mark's decision.** Export needs a fresh step-up, but `/shelf/reopen` (returns each saved conversation's code, which opens the full transcript) and `/shelf/delete` (erases a conversation everywhere) need only a session (`engine/api/accounts_routes.py`, about lines 600 to 645). Anyone holding the cookie on a shared device can read or erase every saved conversation; sessions slide for 14 days idle, up to 60. Suggested fix: require step-up for shelf delete at least, and decide whether opening needs it. This is a methodology call, so put it to Mark with options.
3. Low: the per-address send budget across networks (9 per 15 minutes, 30 a day) counts IPv6 at /64, so one cheap IPv6 /56 can lock an address out of code sign-in for a day (ruling 100 recorded it as costing "three networks"). Fix: count the cross-network budget per /48 or per /24, or tell Mark the real cost.
4. Low: the coupon admin POSTs (`engine/api/coupon_routes.py`, about lines 62 to 96) have no custom-header or Origin check; a page on another subdomain of the same registrable domain could approve or cancel coupons with the admin cookie. Fix: the same guard as the accounts routes, or require the Bearer token for changes.
5. Low: a non-ASCII `session_code` on `/shelf/add` gives a 500 (`engine/m4/session_code.py` line 36 encodes as ASCII). Fix: reject non-ASCII in `codes_match` and `code_opens`.
6. Low: `required_secrets.py` omits `CIC_ACCOUNTS_CONTACT_KEY` and `CIC_ACCOUNTS_SHELF_KEY`, which `build_runtime` requires. Start-up still refuses safely, but the all-at-once message and the render.yaml test miss them. Fix: add both.

Checked and sound: cookie flags and rotation, step-up on the sensitive actions, code hashing and single use, enumeration replies and timing, CSRF and origin checks on the accounts routes, SQL, the SES recipient and template handling, AES-GCM sealing, per-account scoping of shelf, export and coupon routes, sealed backups, logs, and provider token checks.

## Dependencies

- Coupons attach only at sign-in, so coupons cannot go live before accounts do. Go live together.
- A closed account's waiting coupon attaches when the person re-opens it, because redemption runs at sign-in.

## Spend

Sonnet for building, Opus for reviews (as the rules say). No metered model call, live test or paid run by this thread. One SES test email sent by Mark.

## Running record — combined thread (2026-10-27)

- Pull request 1176 marked ready (it was a draft). Security items 5 and 6 and the restore-runbook line (Not done 3) are on the same branch, commit `f60a143a`; 332 accounts, shelf, secrets and session-code tests pass locally; commentary check clean. Merge waits on CI.
- The security review report arrived in this file (above); not re-run.
- Open with Mark, one at a time: (a) security item 2, step-up for shelf delete and reopen; (b) items 3 and 4; (c) the 429 rate limit; (d) the words in Not done 4; (e) coupon limits (Not done 5); (f) the SES configuration set (Not done 9).
- Mark ruled on security item 2: shelf delete needs a fresh step-up; open stays session only. Built on the same branch (service `shelf_delete_allowed`, route check, `RemoveShelvedScreen` reusing the export confirmation words; no new participant words). Tests: shelf 36 passed, frontend suite passed.
- Mark ruled on the dashboard 429: admin limit 30 a minute (ruling 110). Changed in `engine/api/ratelimit.py`.
- Mark ruled on security finding 4: guard the coupon admin POSTs (ruling 111; `engine/api/coupon_routes.py` and the dashboard page). Open: the same hole exists on the dashboard's other change buttons (pause, void, mint, unmatched-dismiss, feedback-close); ask Mark.
- Security finding 3 (IPv6 /64 send budget) still to put to Mark.
- Mark ruled on security finding 3: sign-in send budgets use IPv6 /48 (ruling 112; `sign_in_network_of` in `engine/api/ratelimit.py`). All six security findings are now resolved or ruled.
- Mark chose privacy retention draft B (ruling 113). Built locally in `cic-website/privacy.html`, `privacy-go-deeper.js` and the pages tests; committed, not pushed, so it does not cancel CI run 3652. It rides the next push (merge 1176 first, or a follow-up PR with the other words).
- Mark gave his own coupon privacy sentence (ruling 114), added to `cic-website/privacy.html` inside the hidden "What an account holds" section. Later_List item 1 is done.
- Mark approved the plainer wording for the delete, after-delete and re-open screens (ruling 115; `accountsCopy.ts` `deleteGoes`, `deleteStays`, `closedText`). Not-done item 4 words are now all answered.

## Running record, after pull request 1176 merged (cb59b339)

- Pull request 1176 merged to main at 05:00 UTC by the shared account, not by this thread, while the engine test suite and library validators jobs were still running. This thread then ran those suites on the merged tree: accounts, deeper, m1, m2, m3, m4, m5, m6, m7, m8, m10, provider, shape, canon, engine/tests and api (both modes) all passed; library validator scripts up to the registry checks passed; the last four library test scripts were still running when this was written.
- Mark's rulings this session: 109 shelf delete step-up; 110 admin limit 30 a minute; 111 coupon admin same-page check; 112 IPv6 /48 send budget; 113 privacy retention paragraph (draft B); 114 his own free-tokens privacy sentence; 115 plainer delete and re-open screens; 116 coupon limits 100,000 tokens and 300 a day.
- Not done: the same-page check on the dashboard's other change buttons (pause, void, mint, unmatched-dismiss, feedback-close), Mark has not decided. SES `my-first-configuration-set` check in AWS. Turn-on and rehearsal. Promotion (Mark). Question 14 (Mark). Clearing of question text at 90 days reaches live with promotion (Mark).
- Found, not caused by this thread: the library test script `cic/engine/tests_corpus_map.py` fails four checks on main (map filename is a census movement id; buckets reproducible from staging; every author ruling used; every transmitted work has its voice assigned elsewhere, with a list of orphan works). CI's Library validators job failed the same way on the head of pull request 1176 after it merged. Same result run locally. Belongs to the library thread; flagged to Mark, not touched.
- Mark chose A for the side panel (ruling 117): signed in, the panel shows the account's free tokens and tokens on codes. Built in GoDeeperPanel.tsx with two tests in AccountHome.test.tsx. Open: Mark said free tokens are always spent before paid; the engine only draws free for the first rounds of a conversation, so this needs his decision (put to him separately).
- Mark chose A to show the person their own email on the account screen, label 'Signed in as' (ruling 119). Two wording questions for Mark: the account-screen note 'It holds no name.' and the privacy page line that says the email is used only to send codes and notices.


- Mark chose 'use up free tokens, then paid, in any round' (ruling 118). Built in engine/api/deeper_admission.py with the seam tests updated and six new tests; the explicit refund of the free part is proved by a test that fails when the refund is removed. Awaiting independent Opus review before the pull request.
- Opus review of the free-first change found a blocking bug (any code header took a person past the free rounds for free) and a weakened-tests problem; both fixed on claude/free-first-split-2026-10-27 with the guarding tests restored and five more added. A targeted recheck is the next step before the pull request.
- Mark ruled on the code gate for the free-first change: a live code with any tokens left opens the rounds past the free ones, free pays first (part of ruling 118). The second Opus recheck found no blocking issue; its one new finding was this rule.
