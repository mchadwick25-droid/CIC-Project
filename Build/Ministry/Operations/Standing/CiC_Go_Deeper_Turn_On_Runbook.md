# Go Deeper — Turn-On and Rollback Runbook

Slice S11 of the Go Deeper build. Written 2026-10-04 by the build thread. Reviewed by the Opus thread at the pull request. Mark walks the staging rehearsal and signs the checklist before step 1 touches production.

Go Deeper ships switched off. Nothing here changes a participant's experience until step 4. Every step below can be undone by the rollback section, and the free path never depends on the module.

## The two sentences that must stay true

- The conversation engine never learns that money exists. It is handed a cap and a Facilitator-only flag.
- The Go Deeper module never learns worlds, records, voices or quotes. Stripe, the meter and the conversation store share no key.

If a change made while turning this on would break either sentence, stop and escalate.

## Who does what

Mark owns every item marked **Mark**. The build thread does the rest and reports. Nothing marked **Mark** is done by the build thread, and nothing goes to production without Mark's promotion (`CiC_Promotion_Runbook.md`).

## Part 1 — Before the staging rehearsal

All of these must be true. The build thread checks the first group; Mark confirms the second.

**Built and merged on `main`** (check in the Funding-Strategy Decision-Log):

- The meter, routes, admission seam, proofs in CI, app panel, site pages, Facilitator words, the door (computation, admission, public line), and the standing measure.
- The token words (T3) are merged. No dollar figure appears in the conversation.
- The "already closed" 409 on a crisis message is fixed (System Hub decision 35), so a crisis message to a closed sitting is answered.

**Mark's, before any real sale:**

- Prices, packs and the sponsor pack (ruled: $7 = 1,100 tokens, $15 = 2,750, $30 = 6,600; nothing under $7; the sponsor pack shape is open).
- The door's numbers: base $150 a week is ruled. The gift and purchase shares (0.8, 0.5), the invoice factor (1.35) and the five stages ship as stated defaults in `engine/deeper/ops/go-deeper.yaml`. Change them by pull request if wanted.
- The converted numbers: group daily ceiling 6000 tokens, low-balance warning at 100 tokens.
- Words: the free-day count line, "beside" or "under" the message box, the last-stage public line, and "give at Get Involved" showing on Get Involved itself.
- Expiry, refund and lost-code policy, after a professional answers the stored-value, gift-card, unclaimed-property, sales-tax and minors questions.
- **The minors question, answered before the first group code is sold.**
- Stripe: the written answer on stored value, the account set up, and each unverified Stripe fact checked before the slice that depends on it (below).
- An AWS budget alarm exists (Mark's check), and the network policy lets the engine reach what it needs.

**Stripe facts Mark verifies** (each blocks the slice named):

- A Payment Link's `client_reference_id` arrives in the completion event (claim flow).
- The after-payment redirect can return the participant to the exact sitting, and the opener window is reachable after Stripe checkout (the same-sitting return).
- The signature header, the ids that refund and dispute events carry, `async_payment_succeeded`, `quantity`, buyer-data retention, `amount_total` in cents, and whether gifts run on their own Payment Links.
- Whether an in-page checkout is available on a Payment Link, and Adaptive Pricing or currency behaviour.

## Part 2 — Settings, and where each one lives

| Setting | Where | Value | Notes |
|---|---|---|---|
| `CIC_DEEPER_ENABLED` | engine (Render) | `1` | Off by default. Off means no route under `/api/deeper` or `/api/admin/deeper` exists and no file is opened. |
| `CIC_API_ANON_CAP_ENABLED` | engine | on | **Required.** The engine refuses to start with the module on and this off. |
| `CIC_DEEPER_WEBHOOK_SECRET` | engine, secret | from Stripe | Never in the repo. |
| `CIC_DEEPER_PRODUCTS` | engine | JSON keyed by Payment Link id | One entry per pack: kind, tokens, optional count and daily ceiling. A link not listed here mints nothing. |
| `CIC_DEEPER_GIFT_LINKS` | engine | JSON list of Payment Link ids | Gifts count toward the door; a link cannot be both a product and a gift. |
| `CIC_DEEPER_SITE_ORIGIN` | engine | the site's exact origin, no `www`, no wildcard | The claim route answers only this origin. |
| `CIC_DEEPER_OPS_FILE` | engine | optional | Defaults to `engine/deeper/ops/go-deeper.yaml`. A bad file stops the start. |
| `CIC_DEEPER_METER_DB`, `CIC_DEEPER_CLAIMS_DB` | engine | optional | Default to the directory that holds the event store, so they sit on the backed-up disk. |
| `VITE_DEEPER_ENABLED` | app build | `on` | Build-time. Off means no panel, no header, no change. Changing it needs a rebuild and deploy. |
| `VITE_DEEPER_SITE_ORIGIN` | app build | the same exact origin | Must match `CIC_DEEPER_SITE_ORIGIN`. |
| `enabled` | `cic-website/assets/go-deeper-config.js` | `true` at step 4 | Until it is true the home and Get Involved pages make no door-line request. |
| `PAYMENT_LINK` | `cic-website/go-deeper.html` | the Payment Link | The buy button stays off until one is set. The page carries one link today and the packs are three, so a link per pack is a change to make at step 4 once the S4 links exist. |

The meter file is backed up daily when the backup job is given `--meter-db`. Confirm that is configured before step 2. The claim table lives in its own file and stays out of backups on purpose.

The website's production deploy follows `main` directly, not `live`. Merging a site change to `main` ships it. The `enabled: false` setting and the unlinked pages are what keep it dark.

## Part 3 — The staging rehearsal (Mark walks it)

Staging is `cic-engine-staging`, which follows `main`. Use Stripe test mode.

1. Set the Part 2 engine settings on staging, with test-mode Payment Links and the test webhook secret. Build the app with `VITE_DEEPER_ENABLED=on`.
2. Confirm the engine starts, and that starting with `CIC_API_ANON_CAP_ENABLED` off is refused.
3. Run a test-mode purchase of each pack. Each must mint one code, shown on the return page, and the daily reconciliation count (`GET /api/admin/deeper/reconciliation`) must show the payment seen, the code made, and a gap of zero.
4. Replay the same webhook. Nothing more is minted.
5. Send a refund event for a purchase. Its code is void, and the reconciliation counts it.
6. In the app, with no code, have a free conversation to its third round. The panel opens at the limit. Enter the code. The same sitting carries on, and the token count falls.
7. Pause codes (`POST /api/admin/deeper/pause` with `{"on": true}`). The next message with a code gets the paused line. Free conversations carry on. Unpause.
8. Run each state on the Ledger page's list and read the words as a participant would: spent, too few, in use, group daily limit, code not accepted, paused.
9. Send a message that reads as distress, one that is unclear, and one the safety check cannot read, at: the third free round, a spent code, a paused module, and each door stage. Each must get the Facilitator's answer and never the limit message.
10. Drive the door: with a low base number in the operations file on staging, run traffic until each stage is reached. Read `GET /api/admin/deeper/door` at each. Confirm the free path narrows in the order the operations file lists, free voice closes, and at the last stage a code is refused with nothing spent.
11. Open the admin dashboard. The Go Deeper section shows the day's codes, tokens and refusals, and the "highest door stage" column moves with step 10.
12. Take a backup and restore it to a scratch copy. The restored meter file has the same balances.
13. Flip the module off (rollback step 4). Confirm the free path is unchanged and every deeper route returns 404.
14. Mark signs the checklist, listing anything that did not behave and what was done about it.

## Part 4 — The paid voice-quality run (needs Mark's approval first)

One paid run before step 4, to see that the voice holds across the longest sitting a pack allows. This is a paid bulk run on a metered outside service, so it follows the standing rule: a small sample first, Mark approves the sample by ear or eye, and only then the rest.

- **Sizing:** the longest sitting a pack allows is about sixty conversations on the $30 pack. Size the run to that, and state the count in the request.
- **Settings are passed on the command, never inherited:** the voice model id, generation settings and the cap are named explicitly, and the run prints them with item counts. Confirm from that printout that what was paid for is what was meant.
- **A stated cap** on spend is written into the request, and the run stops at it.
- **Approval:** Mark approves the sample first, then the cost and the settings, before anything runs. The build thread does not start the run on its own.
- A check that files match each other proves nothing about what produced them. Verify the thing that was paid for.

## Part 5 — The four production steps

Each step is a separate promotion or setting change, with a wait and a look between. Mark does the promotion; the build thread watches and reports.

**Step 1 — Ship dark.** Promote the code with every flag off. Check: the engine behaves as before, no route under `/api/deeper` exists, the site pages are unchanged and make no request, the dashboard shows no Go Deeper section. Wait a day.

**Step 2 — Engine on.** Set the Part 2 engine settings with live-mode Stripe values and turn `CIC_DEEPER_ENABLED` on. The app and site are still off, so no participant sees anything. Check: the webhook endpoint is reachable by Stripe, the door computes from the usage log (`GET /api/admin/deeper/door`), the dashboard section appears. The first real use is a hand-minted test code through the sponsor path, spent in a sitting from the app build in step 3.

**Step 3 — App on.** Build the app with `VITE_DEEPER_ENABLED=on` and promote. The panel opens at a limit and on request, and accepts a code a person enters. There is still no buy button anywhere. Check the safety matrix again on production with the hand-minted code.

**Step 4 — Site on.** Only after the Part 4 run is approved and clean, and Mark has signed Part 3. Set the Payment Link or links on `go-deeper.html`, set `enabled: true` in `go-deeper-config.js`, remove `noindex` from the two pages, and link the Go Deeper page. Merging to `main` ships the site. Watch the reconciliation gap and the dashboard daily for the first week.

## Part 6 — Rollback

Do the first step that stops the harm, then stop. Each is reversible. The order is from the lightest to the heaviest.

1. **Pause codes** (`POST /api/admin/deeper/pause`, admin login). Takes effect on the next request. Codes stop being spent; the free path is untouched; a participant with a code sees the paused line. Use this first for any doubt about money or codes.
2. **Close the site.** Set `enabled: false` in `go-deeper-config.js`, remove the Go Deeper link and clear `PAYMENT_LINK`, and merge to `main`. Deactivate the Payment Links in Stripe so nothing new is sold even from an old link or bookmark.
3. **Turn the app off.** Rebuild with `VITE_DEEPER_ENABLED` unset and deploy. The panel and the code header go away.
4. **Turn the engine module off.** Unset `CIC_DEEPER_ENABLED` and deploy. Every deeper route is gone, no file is opened, and every conversation gets the free grant. The meter and claim files stay on disk; do not delete them.

After any rollback past step 1, work out who is owed (below) before closing the incident. Rolling back the code with `git revert` of the promotion PR is the permanent fix (`CiC_Incident_Rollback_Runbook.md`).

## Part 7 — Balances owed at a switch-off

`GET /api/admin/deeper/owed` (admin login) lists, for each payment with unspent tokens: the Stripe payment id, kind, number of codes, tokens bought, tokens left, and the day bought. It holds no code and no hash. Match the payment id to Stripe to find who paid.

What is refunded, and whether a refund is whole or partial, is the refund policy, which is Mark's. This report gives the numbers; it does not decide them.

Refunds made in Stripe reach the meter by the refund event and void the code; the reconciliation count shows them.

## Part 8 — Removal checklist (if Go Deeper is retired)

1. Roll back through step 4 above and keep the module off.
2. Export the owed report and settle every balance per the refund policy.
3. Deactivate the Payment Links and delete the webhook endpoint in Stripe.
4. Take a last backup of the meter file, and hold it for the retention period the privacy page states.
5. Remove the secrets (`CIC_DEEPER_WEBHOOK_SECRET`) and the Go Deeper settings from Render.
6. Remove the Go Deeper pages and the door line from the site, and the privacy page's Go Deeper paragraph.
7. Only then delete the module's code in a reviewed pull request. The proofs in CI named for the module go with it.

## Part 9 — What to watch in the first weeks

- **Daily:** the reconciliation gap on the dashboard should be zero. A gap above zero is money not matched to codes; look at it the same day.
- **Daily:** the door stage and the refusal reasons. A growing "door closed to free" count means free conversations are being turned away; the gifts line is what reopens them.
- **Weekly:** the cost per refused message. Every message, even a refused one, still gets its safety check, about $0.003. The door bounds the voice, not those checks.
- **After any change** to prices, packs or door numbers: change the operations file by pull request, and read the log entry it adds.

## Known gaps, stated

- The door's week of observe mode (stage shown, nothing narrowed) is not built. The door narrows from the first week it is on. Mark decides whether to add it before step 2.
- Crisis turns are not counted by the module, which never sees message content.
- A refused message that the safety check then lets through to the Facilitator is counted as a refusal.
- The go-deeper page carries one Payment Link; three packs need three.
