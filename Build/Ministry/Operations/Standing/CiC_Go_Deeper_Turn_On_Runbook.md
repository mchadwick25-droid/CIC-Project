# Go Deeper — Turn-On and Rollback Runbook

Slice S11 of the Go Deeper build. Written 2026-10-04 by the build thread. Reviewed by the Opus thread at the pull request. Mark walks the staging rehearsal and signs the checklist before step 1 touches production.

Go Deeper ships switched off. Nothing here changes a participant's experience until step 4. Every step below can be undone by the rollback section, and the free path never depends on the module.

## The two sentences that must stay true

- The conversation engine never learns that money exists. It is handed a cap and a Facilitator-only flag.
- The Go Deeper module never learns worlds, records, voices or quotes. Stripe, the meter and the conversation store share no key.

If a change made while turning this on would break either sentence, stop and escalate.

## Who does what

Mark owns every item marked **Mark**. The build thread does the rest and reports. Nothing marked **Mark** is done by the build thread, and nothing goes to production without Mark's promotion (`CiC_Promotion_Runbook.md`).

## Where the module is run from

Three places, one kind of control each. **Stripe** holds money: the pack links, the sponsor link and one-per-person discount codes. The **admin dashboard** (behind the admin login) holds the live day: the pause switch, the mint page, the door's current stage and the day's tiles, all with effect at once. The **operations file** (`engine/deeper/ops/go-deeper.yaml`, changed by pull request) holds the shape of the offer: token prices, pack sizes, the free grant, the door's base number and thresholds, and the admin mint limits. The free grant has no live dial: the door moves the free table by its stages, and the baseline stays a line in the file.

The mint page makes codes with no payment. The codes show once on the page; copy them before leaving it. If a response is lost, cancel the mint id it showed in the dashboard's cancel box (it takes a mint id or a payment id) and make them again. Each grant counts toward the door as a gift of the packs' price.

## Offers and goodwill

The module makes free codes; Stripe makes every percentage discount. Name each Stripe code for what it was for, so the list reads at a glance: `PILOT-`, `XMAS-`, `HOME-` for a cohort, `FIX-` for a complaint. Steps below use Stripe's feature names; check them against your account the first time, since Stripe's menus change.

| Situation | Where | What the door counts |
|---|---|---|
| Free package for the pilot | the pilot join (on when `pilot_open` is true) | a gift of the pack's price |
| One-off free grant | the dashboard mint page | a gift of the pack's price |
| A percentage off for a season or a cohort | a Stripe promotion code on the chosen package | what was paid |
| A discount on one package only | a Stripe coupon limited to that product, with promotion codes switched on only for that package's payment link | what was paid |
| A complaint, already bought | a partial refund in Stripe | no change; the codes keep working |
| A complaint, not yet bought | a one-redemption Stripe promotion code limited to that customer's email | what was paid |

The pilot join counts people by the address the request arrives from, taking the last entry of `X-Forwarded-For`; that holds only while Render is the one proxy in front of the service, so check it again if a CDN or second proxy is ever put in front. An IPv6 address is counted by its /64 block. Two codes an address means a shared network (a school, a church's wifi, a mobile carrier's shared address) can run out for later joiners; if a cohort reports that, raise `per_address` by pull request or give them a grant from the mint page.

Never use the dashboard's cancel box for a goodwill refund: it cancels the codes. A full refund or a dispute cancels them by itself. The pilot runs for named audiences (general, pastors, historians). Each has its own open switch, cap and per-address count in the operations file, and all share one end date. `general` is public. `pastors` and `historians` are joined only by a secret link key you make and keep in the server's environment; the dashboard shows how many each has been given and whether a private audience has its key set. To close the pilot to the public and keep it for pastors and historians, set `general` to `pilot_open: false`.  Make each private link `pilot.html?for=<its key>` on the site, send it yourself, and send only that site link, never the app address with `#cic-pilot=` (an email scanner that runs the app's script from the link could use up a place), and treat the key as a password: Cloudflare's logs see the address, so replace the key in `CIC_DEEPER_PILOT_LINKS` if it leaks. To open an audience, set its `pilot_open` to true in the operations file, set `pilot: true` in `assets/go-deeper-config.js`, and have the app built with the module on; the page stays empty until all three are set.

## Part 1 — Before the staging rehearsal

All of these must be true. The build thread checks the first group; Mark confirms the second.

**Built and merged on `main`** (check in the Funding-Strategy Decision-Log):

- The meter, routes, admission seam, proofs in CI, app panel, site pages, Facilitator words, the door (computation, admission, public line), and the standing measure.
- The token words (T3) are merged. No dollar figure appears in the conversation.
- The "already closed" 409 on a crisis message is fixed (System Hub decision 35), so a crisis message to a closed sitting is answered.

**Mark's, before any real sale:**

- Prices, packs and the sponsor pack (ruled: $7 = 1,100 tokens, $15 = 2,750, $30 = 6,600; nothing under $7; the sponsor pack shape is open).
- The door's numbers: the base number and thresholds are set from the observe week (Part 5, step 2). The gift and purchase shares (0.8, 0.5), the invoice factor (1.35) and the five stages ship as stated defaults in `engine/deeper/ops/go-deeper.yaml`. Change them by pull request.
- The converted numbers: group daily ceiling 6000 tokens, low-balance warning at 100 tokens.
- The free allowance, ruled 2026-10-04: 550 tokens in a window of 30 days that starts at a visitor's first use and refills 30 days after it (rolling, not calendar), five solo conversations of three rounds. It is kept in the meter file (a keyed hash of the visitor key, a day and a number; the key is `CIC_DEEPER_FREE_KEY`, which is not in the file), so a deploy does not refill it. The old daily 330 is withdrawn.
- Words: the free-allowance count line, "beside" or "under" the message box, the last-stage public line, "give at Get Involved" showing on Get Involved itself, and a line for the paid round-cap stop that says the participant's code still holds tokens.
- **The privacy page.** Mark asked for the recommended wording for now, to be edited later. The page carries a Go Deeper section and a two-job cookie paragraph, both hidden until `enabled: true` in `go-deeper-config.js`, so the page says today's facts until step 4 and the Go Deeper facts after it. Mark may edit the words at any time. Until step 4 the page's JavaScript is what shows them. At step 4, edit the HTML itself: remove the `hidden` attributes from the Go Deeper section and the two-job paragraph, and delete the one-job paragraph, so a visitor with scripts off reads the truth. The hidden words are in the page source while Go Deeper is off.
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
| `CIC_API_ANON_CAP_ENABLED` | engine | `1` (`true` or `yes` also work; `on` does not and stops the start) | **Required.** The engine refuses to start with the module on and this off. |
| `CIC_DEEPER_WEBHOOK_SECRET` | engine, secret | from Stripe | Never in the repo. |
| `CIC_DEEPER_PRODUCTS` | engine | JSON keyed by Payment Link id | One entry per pack: kind, tokens, optional count and daily ceiling. A link not listed here mints nothing. |
| `CIC_DEEPER_FREE_KEY` | engine, secret | at least 32 random characters | **Required.** Keys the free allowance's rows. Never written to disk or the repo. The engine refuses to start without it. Rotating or losing it refills every visitor's free window, so keep it. |
| `CIC_DEEPER_PILOT_LINKS` | engine | JSON object of secret link key to private audience, for example `{"<key>": "pastors"}`; make each key with `python3 -c "import secrets; print(secrets.token_urlsafe(18))"` | Optional. Without it no private pilot audience can be joined. A key is 16 to 64 letters, digits, hyphens or underscores. Replace a key to end a leaked link. |
| `CIC_DEEPER_GIFT_LINKS` | engine | JSON list of Payment Link ids | Gifts count toward the door; a link cannot be both a product and a gift. |
| `CIC_DEEPER_SITE_ORIGIN` | engine | the site's exact origin, no `www`, no wildcard | The claim route answers only this origin. |
| `CIC_DEEPER_OPS_FILE` | engine | optional | Defaults to `engine/deeper/ops/go-deeper.yaml`. A bad file stops the start. |
| `CIC_DEEPER_METER_DB`, `CIC_DEEPER_CLAIMS_DB` | engine | optional | Default to the directory that holds the event store, so they sit on the backed-up disk. |
| `VITE_DEEPER_ENABLED` | app build | `on` | Build-time. Off means no panel, no header, no change. Changing it needs a rebuild and deploy. |
| `VITE_DEEPER_SITE_ORIGIN` | app build | the same exact origin | Must match `CIC_DEEPER_SITE_ORIGIN`. |
| `enabled` | `cic-website/assets/go-deeper-config.js` | `true` at step 4 | Until it is true the home and Get Involved pages make no door-line request. |
| `PAYMENT_LINK` | `cic-website/go-deeper.html` | the Payment Link | The buy button stays off until one is set. The page carries one link today and the packs are three, so a link per pack is a change to make at step 4 once the S4 links exist. |

The meter file is backed up by the engine's own daily job whenever the module is on (the app passes it as an extra database). Production relies on that. The CLI option `--meter-db` is for taking a backup by hand, for example before a rollback. Confirm the daily job lists a meter backup before step 2. The claim table lives in its own file and stays out of backups on purpose.

The website's production deploy follows `main` directly, not `live`. Merging a site change to `main` ships it. The `enabled: false` setting and the unlinked pages are what keep it dark.

## Part 3 — The staging rehearsal (Mark walks it)

Staging is `cic-engine-staging`, which follows `main`. Use Stripe test mode.

1. Set the Part 2 engine settings on staging, with test-mode Payment Links and the test webhook secret. Build the app with `VITE_DEEPER_ENABLED=on`.
2. Confirm the engine starts, and that starting with `CIC_API_ANON_CAP_ENABLED` off is refused.
3. Run a test-mode purchase of each pack. Each must mint one code, shown on the return page, and the daily reconciliation count (`GET /api/admin/deeper/reconciliation`) must show the payment seen, the code made, and a gap of zero.
4. Replay the same webhook. Nothing more is minted.
5. Send a refund event for a purchase. Its code is void, and the reconciliation counts it.
6. In the app, with no code, have a free conversation to its third round, and note the free allowance falling by 110 tokens. Restart the staging engine and confirm the allowance did not refill. The panel opens at the limit. Enter the code. The same sitting carries on, and the token count falls.
7. Pause codes (`POST /api/admin/deeper/pause` with `{"on": true}`). The next message with a code gets the paused line. Free conversations carry on. Unpause.
8. Run each state on the Ledger page's list and read the words as a participant would: spent, too few, in use, group daily limit, code not accepted, paused.
9. Send a message that reads as distress, one that is unclear, and one the safety check cannot read, at: the third free round, a spent code and a paused module. Each must get the Facilitator's answer and never the limit message. Run the same three messages again at each door stage during step 10, because the door narrows nothing until `observe` is false in the copy.
10. Drive the door: copy the operations file, set a low base number in the copy, and point `CIC_DEEPER_OPS_FILE` at the copy on staging (never edit the shipped file for a test). In that copy set `door.observe` to false, because in observe mode the door narrows nothing. Run traffic until each stage is reached. Read `GET /api/admin/deeper/door` at each. Confirm the free path narrows in the order the operations file lists, free voice closes, and at the last stage a code is refused with nothing spent.
11. Open the admin dashboard. The Go Deeper section shows the day's codes, tokens and refusals, and the "Door stage (peak)" column moves with step 10.
12. Take a backup and restore it to a scratch copy. The restored meter file has the same balances.
13. Flip the module off (rollback step 4). Confirm the free path is unchanged and every deeper route returns 404.
14. Mark signs the checklist, listing anything that did not behave and what was done about it.

## Part 4 — No paid voice-quality run

Ruled by Mark, 2026-10-04: there is no paid voice-quality run now. The new engine is about to land and would make the result stale. The question the run was meant to answer, how many rounds a paid conversation may run before quality falls, is answered from the new engine's own baseline runs when they exist. Step 4 is not gated on a paid run.

Until then a provisional cap holds. The operations file carries `paid: {round_cap: 40, provisional: true}`. Past 40 rounds in one conversation a code is not spent, the turn is refused, and the Facilitator answers with the neutral limit text. The 40 is the build thread's safe default with no measurement behind it. Replace it, and set `provisional: false`, when the new engine's baselines exist. The refusals show on the dashboard as "paid conversation at its round cap". The participant sees no line of their own for this stop yet: that wording is Mark's, and it needs to tell a participant that their code still holds tokens.

If a paid run is ever wanted again, it follows the standing rule for paid bulk runs: a small sample first, Mark approves it by ear or eye, settings are passed on the command and printed with item and character counts, a stated cap, and the run script gets its own review.

## Part 5 — The four production steps

Each step is a separate promotion or setting change, with a wait and a look between. Mark does the promotion; the build thread watches and reports. **The steps are cumulative.** Step 3 and step 4 assume the engine is still on from step 2. The module cannot be turned off at the engine while a Payment Link is live and the app or site is on (Part 6 says why).

There is no way to hand-mint a code. Only a Stripe completion event makes one. So the first live code is a real purchase.

**Step 1 — Ship dark.** Promote the code with every flag off. Check: the engine behaves as before, no route under `/api/deeper` exists, the site pages are unchanged and make no request, the dashboard shows no Go Deeper section. Wait a day.

**Step 2 — Engine on.** Set the Part 2 engine settings with live-mode Stripe values and turn `CIC_DEEPER_ENABLED` on. The app and site are still off, so no participant sees anything. Check: the webhook endpoint is reachable by Stripe, the door computes from the usage log (`GET /api/admin/deeper/door`), the dashboard section appears. Then Mark makes one real purchase of the smallest pack through a live Payment Link that no page links to, and reads the code from the return page. The reconciliation count must show one payment seen, one code made, a gap of zero. Mark then refunds that purchase in full in Stripe and checks that the refund event voids the code (`refunds_applied` is one, `GET /api/admin/deeper/owed` no longer lists it). This is the first live proof of the whole loop.

The door starts in **observe mode** (`door.observe: true` in the operations file). It is worked out every minute and counted, but it narrows nothing, the public door line says nothing, and no turn is refused for it. Leave it for one week. Each day the dashboard's Go Deeper table shows the door's peak stage, its peak share of the ceiling, the peak weekly spend, and the voiced turns it would have refused, free and coded separately. Halving the free day at a stage is not counted as a refused turn, so read the peaks for how close the week came. Mark sets the base number and thresholds from that week, by pull request to the operations file, then sets `door.observe: false`, and the door goes live. Until it is live, a surge of free traffic is bounded only by the existing per-visitor, per-address and daily limits, so watch the dashboard through the week.

**Step 3 — App on.** Build the app with `VITE_DEEPER_ENABLED=on` and promote. The panel opens at a limit and on request, and accepts a code a person enters. There is still no buy button anywhere. Mark makes a second real smallest-pack purchase through the unlinked Payment Link, enters its code in a sitting, and runs the safety matrix on production (Part 3, step 9) with it, then refunds it in full.

**Step 4 — Site on.** Only after Mark has signed Part 3, the door has run its week of observe mode and gone live (Part 5, step 2), and the words items in Part 1 are settled. Set the Payment Link or links on `go-deeper.html`, set `enabled: true` in `go-deeper-config.js`, remove `noindex` from the two pages, and link the Go Deeper page. Merging to `main` ships the site. Watch the reconciliation gap and the dashboard daily for the first week.

## Part 6 — Rollback

Do the first step that stops the harm, then stop. The order is from the lightest to the heaviest.

**What pausing does and does not do.** Pausing codes stops codes being spent. It does not stop Stripe selling. A live Payment Link keeps taking money while codes are paused, and after the engine module is off (step 4) the webhook is a 404, so a buyer pays and never gets a code. Stripe retries a failed webhook for a while and then gives up. So the rule is: **stop selling before, or with, anything that removes the webhook.**

1. **Stop selling, and pause codes.** For any doubt about money or codes, do both together: deactivate every Payment Link in Stripe (so nothing new is sold, even from an old link or bookmark), then pause codes (`POST /api/admin/deeper/pause`, admin login; effective on the next request). The free path is untouched; a participant with a code sees the paused line.
2. **Close the site.** Set `enabled: false` in `go-deeper-config.js`, remove the Go Deeper link and clear `PAYMENT_LINK`, and merge to `main`. Payment Links must already be deactivated (step 1).
3. **Turn the app off.** Rebuild with `VITE_DEEPER_ENABLED` unset and deploy. The panel and the code header go away.
4. **Turn the engine module off.** Only with every Payment Link deactivated, any sale from the last hours reconciled (the daily reconciliation gap is zero), **and the owed snapshot exported and every refunded payment voided (Part 7)**, because both routes are gone afterwards. Unset `CIC_DEEPER_ENABLED` and deploy. Every deeper route is gone, no file is opened, and every conversation gets the free grant. The meter and claim files stay on disk; do not delete them.

Before step 4, work out who is owed (Part 7); do not leave it until after. Reverting the promotion PR with `git revert` is the permanent fix (`CiC_Incident_Rollback_Runbook.md`).

## Part 7 — Balances owed at a switch-off

`GET /api/admin/deeper/owed` (admin login) lists, for each payment with unspent tokens: the Stripe payment id, kind, number of codes, tokens bought, tokens left, and the day bought. It holds no code and no hash. Match the payment id to Stripe to find who paid.

What is refunded, and whether a refund is whole or partial, is the refund policy, which is Mark's. This report gives the numbers; it does not decide them.

**Two facts about refunds that the report does not hide:**

- **A partial refund is not seen.** The webhook ignores a partial refund (it counts it as `partial_refunds_ignored`) and the code stays live. A refund made while the module is off sends the module no event at all.
- **A balance stays live until it is voided.** A refunded payment whose code was never voided still shows in the owed report, can still be spent, and could be refunded a second time. If the module is switched back on, the code works again.

So at a switch-off, **before the engine goes off**:

1. Export the owed report as a snapshot.
2. Settle every balance in Stripe against that snapshot, not against the live list afterwards.
3. For a refund of the whole remaining balance, void the payment's codes with `POST /api/admin/deeper/void` and `{"payment_id": "pi_..."}`. The route does what a full-refund event does: voids the codes, takes the money out of the door's sum, and counts it in the reconciliation. It voids everything the payment made, so it is only for when the whole remaining balance is refunded. Any other partial refund is Mark's policy to decide; the module has no way to void part of a balance.
4. Check each void against the snapshot. The route answers 404 for a payment that made no codes (a mistyped id changes nothing and records nothing), and `voided: 0` for one already voided. Confirm the payment's row is gone from `GET /api/admin/deeper/owed` afterwards.

The routes do not exist once the engine module is off. If a void is found to be missing after that, switch the engine module on alone to do it: every Payment Link deactivated, the app and site flags off, codes paused, then void, then switch it off again.

Until every refunded payment is voided, the written rule is that **the module is not turned back on for sales**. A switch-on only to void is allowed under the conditions above.

## Part 8 — Removal checklist (if Go Deeper is retired)

1. Roll back through step 3 above: Payment Links deactivated, codes paused, site and app off.
2. Export the owed report as a snapshot, settle every balance per the refund policy, and void every wholly refunded payment's codes (Part 7).
3. Roll back step 4 and keep the module off.
4. Delete the webhook endpoint in Stripe.
5. Take a last backup of the meter file, and hold it for the retention period the privacy page states.
6. Remove the secrets (`CIC_DEEPER_WEBHOOK_SECRET` and `CIC_DEEPER_FREE_KEY`) and the Go Deeper settings from Render.
7. Remove the Go Deeper pages and the door line from the site, and the privacy page's Go Deeper paragraph.
8. Only then delete the module's code in a reviewed pull request. The proofs in CI named for the module go with it.

## Part 9 — What to watch in the first weeks

- **Daily:** the reconciliation gap on the dashboard should be zero. A gap above zero is money not matched to codes; look at it the same day.
- **Daily:** the door stage and the refusal reasons. A growing "door closed to free" count means free conversations are being turned away; the gifts line is what reopens them.
- **Weekly:** the cost per refused message. Every message, even a refused one, still gets its safety check, about $0.003. The door bounds the voice, not those checks.
- **After any change** to prices, packs or door numbers: change the operations file by pull request, and read the log entry it adds.

## Known gaps, stated

- The paid round cap of 40 is provisional and unmeasured. Its stop has no participant line of its own yet.
- Observe mode does not count the halving of the free allowance as a refusal.
- Crisis turns are not counted by the module, which never sees message content.
- A refused message that the safety check then lets through to the Facilitator is counted as a refusal.
- The go-deeper page carries one Payment Link; three packs need three.
- There is no hand-mint or sponsor-code path: only a Stripe completion event makes a code. The first live codes are real smallest-pack purchases, refunded. A sponsor path is its own slice if Mark wants one.
- A partial refund is not reflected in a balance automatically. Use the admin void route.
