# Go Deeper — Decision Log

The build record of the Go Deeper module: pay as you go, a code that buys more conversation through Stripe, the door, the free allowance, the token words, the pilot, the admin controls, and the accounts change order. Entries run from 3 October 2026. They were carried here on 7 October 2026 from the Funding Strategy decision log, whose earlier entries (organization, banking, business research) left the public repository that day and remain in the repository's history. The turn-on and rollback steps are in `Build/Ministry/Operations/Standing/CiC_Go_Deeper_Turn_On_Runbook.md`.

## 2026-10-03 — Go Deeper: the design, the rulings, the carried review findings, and what was filed where

The Go Deeper module (pay as you go, a code that buys more conversation, through Stripe, with no accounts) has a converged design. The build thread's first act is this record. The System Hub log carries the rulings as decisions 26 to 31, and the other logs carry the parked items below.

**The record pages** (the pages are the design; the repo holds this index):

- Handoff (slices S0 to S11, parking list): https://claude.ai/artifact/87s72iQMDXv1YnNukEqCVu
- Opus review, round one (B1 to B7, N1 to N13): https://claude.ai/artifact/WFXgLYTzv9JNtD1FnYwmPQ
- Design: https://claude.ai/artifact/79H5o1x9GdTSfHbuvZZL5B
- Ledger, Ship Dark, Wording: https://claude.ai/artifact/H6JdTHykotWJj3B4kefnnx
- Stages, Pilot Test, Pre-mortem: https://claude.ai/artifact/QucZMBM9C71emVDWkpsY5Y
- Four Ways to Pay: https://claude.ai/artifact/Mu6sxQKdmBWHeNXdx3af2r
- Cost Model: https://claude.ai/artifact/XKAx8g4YrhnNRQkbDCkA1g
- Map: https://claude.ai/artifact/NosTTmUbjF4PGhd27RCCSD

**Ruled by Mark, 2026-10-03.** The design is codes, with the browser remembering. Decision 19 is amended: the meter keys on a hash of the code, never on a cookie or an IP. Stripe, the meter and the conversation store share no key, except that the meter keeps the Stripe payment id. The door holds the free path's ceiling. A code holds exchanges. The wording is carried as drafted, for Mark's approval at each pull request. The module ships switched off behind one flag, with a runtime pause behind the admin login and a written rollback. All seven blocking findings and all thirteen notes from Opus round one carry into the build. On B3: at every limit the module adds, a message the safety check reads as unclear, or one where the safety check failed, gets the Facilitator's check-in instead of the limit message. Today's two limits are not changed by this ruling.

**Build order.** S0 (this record), then S1 and S3 together, S2, S10, then S6, S7 and S8 together, S5, S9, S4 by Mark, S11. One slice per pull request. The full existing suite runs with the flag off and on in every pull request.

**Carried findings and the slice that closes each.**

- B1 (joins): S1, S2, S3, S7. Money words stay out of the event log; the claim reference leaves the query string; access logging is stripped for the session and deeper routes; the claim table stays out of backups; "day last used" coarsens to the week; the privacy page says "no shared key" and waits on CO-6.
- B2 (capped visitor): S2 touches `engine/api/anon_cap.py`; S10 tests it. Wording question to Mark at S8.
- B3 (check-in at module limits): S2 builds the exemption; S10 tests it at every module limit.
- B4 (ceiling): S5 and S2. The meter fails open to free; the door fails closed to its last computed stage; `admit_turn` consults the door; the bound is the ceiling plus the turns in flight; the door's sum carries the measured invoice factor; the webhook tells go-deeper payments from gifts by Payment Link.
- B5 (request-diff): S2 and S10 run the diff at turns past the free cap from a hand-built transcript. One paid voice-quality run at the longest sitting a pack allows, before S11 step 4, needs Mark's approval, sample first, every setting printed, a stated cap.
- B6 (untrue sentences): questions to Mark at S7 and S8.
- B7 (a class behind one IP): S2 touches `engine/api/anon_cap.py` and `engine/api/ratelimit.py`; a valid code lifts the daily session cap; the burst bucket keys per code; S10 tests 25 students behind one IP.
- N1 to N13: S1 (N1, N2, N5, N8, N13), S3 (N2, N3, N4, N13), S2 (N7, N9), S10 (N10), S7 and S8 (N6, N11), S4 (N12). N7 needs Mark's value before S2.

**Mark's, not the build's.** The price, pack sizes and the sponsor pack. How many exchanges a Table round costs against a code (N7). The door's base number, stage thresholds, gift share and invoice factor. The free allowance numbers. Expiry and refund policy. Every participant-facing word. Stripe's written answer and the Stripe setup. Whether an AWS budget alarm exists. Widening the network policy. The minors question before the first group code is sold. The one paid voice-quality run. The production promotion. Each of these goes into config with a safe default, and Mark gets one question at the slice gate that needs it.

**Questions for a professional (registered, none answered).**

1. Stored value: whether seller-held conversation credits fall under Stripe's stored-value restrictions (a written question to Stripe, answered before any Payment Link exists; slice S4).
2. Gift-card law: whether a code counts, and what validity period follows.
3. Unclaimed property: whether unspent balances carry reporting duties.
4. Sales tax on a code.
5. Minors: group codes for classes start in the pilot, so the answer is needed before the first group code is sold (N12), not only before public release.

**Stripe and legal facts unverified.** The network policy blocked stripe.com and the regulation sites, so Mark verifies each before the slice that depends on it: the client reference in the completion event (S3, S7); the signature header (S3); the redirect to the return page (S4, S7); which id refund and dispute events carry (S1, S3); event order, retries and replay (S3); quantity on a Payment Link (S3, S4); telling a go-deeper payment from a gift on one endpoint (S3, S5); whether the monthly gift link, a subscription, needs other event types (S5); what Stripe itself records about the buyer, including IP and email (S7); Stripe's fees (pricing).

**Parked items filed here.** (a) The 2026-10-01 pay-as-you-go study cited in the entry "Notes moved out of `support.html`" above is not in the repo. (b) Whether the AWS account carries a budget alarm or spending limit is unverified from the repo; Mark confirms. (c) The network policy blocks stripe.com, docs.stripe.com, ecfr.gov, consumerfinance.gov, ftc.gov, mullvad.net, meta.wikimedia.org and render.com; widening it is Mark's. (d) The close text marked "draft, not yet approved" in `engine/m4/facilitator_turns.py` is replaced by S8, and P1-Security entry 10's open question (a capped visitor reaching the Facilitator) is answered by the Facilitator-only sitting built in S2.

## 2026-10-03 — Go Deeper: Opus round two on S1 and S3 (PR #723), and what each finding became

Opus's targeted recheck (comment on PR #723) found two blocking bugs in S3, one blocking item that belongs to S2, and nine notes. #725 was merged into the S1 branch at 13:31, so #723 carries both slices.

**Fixed in #723.**

- R2-1. A second purchase on a claim reference that already held another buyer's codes deleted that claim. A claim is now deleted only by the call that created it; a reused reference mints nothing and shows as a gap.
- R2-2. A Stripe retry after the claim hour minted codes nobody could reach. `put` now clears an expired row first; the caller refuses to mint, and counts a gap, when the claim cannot be stored.
- a. The claim page answers "no codes yet" until the codes exist in the meter.
- b. The claim file uses `journal_mode=DELETE`, so `secure_delete` scrubs it; a test reads the file after the purge.
- c. The wrong-code delay is `await asyncio.sleep`, so it no longer holds a worker thread.
- d. The webhook refuses a body over 256 KB before it reads the signature.
- e. A partial refund adds to `partial_refunds_ignored` on the reconciliation. Refund policy stays the project lead's.
- h. The module docstring now says what the flag does.

**Carried to later slices.**

- R2-3, blocking, S2's definition of done: the message log records each turn with its session id and a time. Once paid sittings run past ten exchanges, a turn 11 or later marks a paid session, and Stripe's payment time then links a named payment to a conversation. S2 drops the session id from the per-message success lines (kept on error lines) or logs a per-day salted hash of it. S2 does not merge without this.
- g. S2 releases every reservation in a `finally`. A reservation time-out is left out because a long Table round would need its own limit; S2 decides.
- f. S4's sponsor Payment Link uses a fixed quantity, and the expected `amount_total` per product is checked.
- i. S7's return page has the browser make references of at least 22 base64url characters (128 bits), and a new reference for every purchase click, so a repeat purchase never reuses one.

## 2026-10-03 — Go Deeper S2: the admission seam

S2 is the one slice that touches the conversation engine. What it does, and the choices inside it:

- **The engine receives only numbers.** `engine/m4/grants.py` defines a grant (a cap and a Facilitator-only flag). `run_turn` and `open_table_round` read the cap and the flag in place of the constants, and treat Facilitator-only exactly like a spent daily allowance. No money word, price or balance exists in the engine. The free defaults read the live constants, so tests that patch them still work.
- **The API edge turns a code into a grant.** `engine/api/deeper_admission.py` reserves exchanges before the turn and settles them after it, in a `finally` around the interview, stream and Table calls (review note g). A turn the Facilitator answers alone, a failed voice call and a failed stream all give the exchanges back.
- **A code is spent only on turns the free allowance refuses** (decision 45 in the System Hub log). The first ten exchanges of a sitting stay free.
- **Check-in and crisis at every limit (B3).** The module's limits use the same branch as today's, and System Hub decision 35 already exempts every safety route from it, so the check-in and the fail-closed route are answered at the session limit, the daily limit, the free cap, zero balance, paused, a wrong code, a module error and a Facilitator-only sitting. 24 tests cover the three cases at each of eight limits.
- **A visitor at the daily session limit opens a Facilitator-only sitting instead of getting a 429 (B2)**, only when the module is on. The marks are kept in memory, like the daily counters, so a restart forgets them.
- **A valid code lifts the daily session limit and has its own burst bucket (B7).** A group code's bucket is six times larger. Twenty-five students behind one address, on one group code, all get through; without a code the address limit still applies.
- **R2-3 closed.** The per-message success log lines no longer carry the session id or the turn number.
- **The Table:** the price is charged once, when the round opens. The voices that follow in the round (`/continue`) are already paid for, so a round is never stopped part-way by a balance or a pause.
- **Not built here:** the door (S5). The seam leaves one place for it, the free grant. When the module fails, the free path stays open; the door's fail-closed rule arrives with S5.
- **The balance** travels in an `X-Cic-Remaining` response header (and in the stream's final event), so the app can show it after each exchange without extra calls. The code goes in an `X-Cic-Code` request header.
- **Entry 98 items 1 to 4** were already fixed by System Hub decision 35, so the precondition for S11 step 4 that the Handoff names (the "already closed" 409) is met.
## 2026-10-03 — Go Deeper: S1 and S3 merged; Opus round three

S1 and S3 merged to `main` together as PR #723 (merge commit 8584e600), switched off. Opus round three found no blocking finding and three non-blocking notes: the claim route served a refunded code with its full count (fixed in the S3 follow-up); the three route handlers made blocking store calls on the event loop (fixed in the same follow-up, through the thread pool); and a new column does not reach a meter file created before the change. No meter file exists yet, so nothing breaks today. Any later change to a meter column needs a migration step before the flag is first turned on. S2 stays blocked on R2-3 (the per-message log lines).

## 2026-10-03 — Go Deeper S2: Opus review, and what each finding became

Opus reviewed S2 in full (comment on PR #736): three blocking findings and six notes.

**Fixed in S2.**

- S2-1. A visitor past the daily session limit could open unlimited Facilitator-only sittings, each costing the safety check, with no limit but six creations a minute. A visitor now gets one Facilitator-only sitting a day (`daily_facilitator_session_limit`); further creations answer 429, as the limit did before the module. A Facilitator-only sitting that closes still answers a later crisis message with the safety turn, through System Hub decision 35, and a test covers the fifth message.
- S2-2. Any code, even a spent one, lifted the session limit free. Only a live code with exchanges left, with codes not paused, lifts it. A sitting opened that way is marked, and every turn in it is metered from its first. A spent or paused code gets the Facilitator-only sitting. A round already admitted keeps its `/continue` for any code that is not void, so a round paid down to zero is not stopped part-way.
- Notes: a, the module docstring now says the process remembers session ids in memory and never stores them; b, the request-diff test now also covers the stream path and a Table round past the free rounds; f, a request's code is looked up once.

**Change order on the Handoff (S2-3).** The Handoff gave S2 a `close_reason` that selects the close text. S2 does not build it. The engine cannot yet say "your code has run out" or "codes are paused" in words different from the free-cap close, so a participant refused on a paid sitting reads the free-cap text, and a refusal for a passing state (paused, exchanges held by another device) closes the sitting for good. Words are the project lead's, and an engine selector with no new words would be an empty mechanism. So S8 owns both: it adds the reason to the grant, selects the text by reason, and supplies the words; it is therefore no longer text-only. The reasons are free cap, balance out, paused, daily allowance and each door stage. S8 is a precondition of S11 step 4, the step that links the go-deeper page. Until then the module stays dark, so no participant is paid and told the wrong thing.

**Accepted, recorded.**

- d. The session-created log line keeps its session id. It carries no client address and no payment state, and another thread's privacy test depends on it.
- c. Exchanges are reserved before the safety check runs, so on a pooled code with one exchange left a second device's turn is refused while the first is in flight, even if the first turns out to be a safety route. The refusal is the daily close.
- e. A Table round is charged at its opening (decision 45). If every voice in it then fails on `/continue`, the charge stands.

## 2026-10-03 — Go Deeper S10: the standing proofs

S10 adds `engine/api/tests/test_deeper_proofs.py`, which runs in the engine job with the module off and again with it mounted.

- **The two sentences, as imports.** The conversation engine (m1 to m10, provider, canon, prose, wiring, table_wiring) imports nothing from the module. The edge middleware (anon_cap, ratelimit) imports nothing from it. Only `app.py`, `deeper_routes.py` and `deeper_admission.py` do. The module imports only the standard library and itself. The engine core names no payment service, meter or balance header, and the grant types hold only numbers.
- **No join between stores.** After a paid sitting with a real code, the raw bytes of the event and usage databases, including the write-ahead log, hold no plain code, no hash, no payment id, no claim reference and no balance word. The meter and claim files hold no session id, session code, visitor id or conversation text. No event payload in a paid sitting carries a money field.
- **The guard.** A test fails if any of the named proofs is deleted, skipped or marked expected-to-fail. I broke the engine's import rule and skipped a proof on purpose; both were caught.
- **Already in place from S1 to S3 and S2:** the request-diff (interview, stream and Table, past the free cap), the safety tests at eight limits, route absence with the flag off, never-mid-answer, the log scrub, the 25-student class, the schema tests, the race test.
- **Still to come:** overlapping sittings against the ceiling, which needs the door (S5).
- **Recorded next to the Facilitator-only marks:** the marks for sittings a code opens past the session limit are also kept only in memory. After a restart such a sitting is an ordinary one, with its first ten exchanges free. That is bounded, and the daily counters reset on a restart as well.

## 2026-10-03 — Go Deeper S8 (mechanism): a limit is a pause, and the wording lives in one operations file

**Opus round three on S8 (#738, first version).** Three blocking findings, notes a to h. The first version put close texts that mention a code inside the engine and stored them, which marked paid sittings in the conversation store, and it promised "carry on from this point" while closing the sitting for good. It was reverted in full and redone, not patched.

**Rulings (Mark, 2026-10-03).**
1. Prices and anything that may change do not live in the engine. One operations file in the repo holds them, is read at startup, and is changed by pull request. The file is `engine/deeper/ops/go-deeper.yaml`, inside the existing engine tree so it ships with it and needs no new top-level entry. It holds the module's three numbers (group daily ceiling, Table round cost, group burst multiplier) and the participant wording. Prices, pack sizes, the door numbers and the free allowance numbers join it as their slices arrive.
2. At a limit a code can lift, the sitting stays open. The Facilitator answers, nothing writes `session_closed`, and the next message with a valid code continues the same conversation.

**What S8 now is.**
- The grant carries `limit_text`, the words the Facilitator speaks at a refusal. It is a plain string handed in from the edge. With none, the default close and the closing of the sitting are unchanged, so the module off changes nothing.
- The stored words are one neutral line, the same for a free sitting and a paid one. They name no code, no balance and no pause. A new Facilitator kind, `limit`, marks it. The Facilitator's text in the engine never contains the word code, and a proof enforces that.
- The reason a code could not carry the turn (no code, code not accepted, balance out, too few for a Table round, daily ceiling, paused, in use) is a separate line from the operations file. It travels only in the response, as `limit_note`, in the plain reply, the stream's final event and the Table reply. It is never stored. A test checks the store for every note text.
- A fault in admission still leaves the free path exactly as it was, including the default close.
- The edge reads and checks the file at startup and refuses to start on a missing, incomplete or malformed one.

**Findings, one by one.**
- 1 fixed as above. 2 fixed (option i). 3 fixed: a proof runs a free sitting and a code-driven sitting to its last exchange and compares the stored Facilitator words, and another forbids the word code in the engine's Facilitator text.
- Note a fixed: a code with too few exchanges for a Table round has its own line. Note b fixed: a code that did not work has its own line. Note c: moot, a double-sent message no longer closes anything. Note d: readability is scored in a test for every line in the file.
- Notes e to h, from the S10 proofs: e fixed (a named proof must assert something), f fixed (no collection hook or CI flag may drop a proof from outside its file), g fixed (a CI step runs the guard by name, so deleting it fails the build), h fixed (the S2-2 proof is now required). The new S8 proofs are required too.

**Change orders and parked.**
- Moving `SESSION_TURN_CAP`, `TABLE_SESSION_ROUND_CAP` and the `anon_cap.py` defaults into the operations file goes beyond S8 and touches the conversation engine redesign's ground. Not done; it needs that thread's agreement. The limit numbers the module reads today still come from those constants.
- The admin page that shows the file's current values is part of S9.
- The wording in the file is a draft held for Mark. It is shown as an Artifact and is changed by editing the file.
- Each further message at a limit without a code costs one safety check, bounded by the daily message count. Accepted by the review.
- The app and website must show `limit_note` and treat the `limit` kind as a pause, not an ending. That is S6 and S7.

**Opus recheck of #739 (head 63000eb1): no blocking finding.** Notes i to k.
- i. The runtime's Table round cost and burst multiplier now default to the operations file's values, so tests and production read one source. The meter keeps its own safe default for the group ceiling, because the module imports only the standard library and cannot read the file; the edge passes the file's value in.
- j. Keeping a sitting open costs one safety check for each further message without a code. The bound is the daily message count: 150 messages a visitor, about $0.75 at most. Mark accepted this when ruling.
- k. #738 merged with three blocking findings open. #739 removes what it carried. From here a slice is merged only after the review thread has cleared its blocking findings, and the checkpoint says so.
- Flag-on suite: three older tests assert the module-off contract (a session closes for good at the cap). They now say so with an explicit `deeper=None`. With the module on, a limit pauses, and the new tests cover that.

## 2026-10-03 — Go Deeper S7: the website pages

S7 adds two static pages to `cic-website`: the go-deeper page and the return page. The wording is a draft for Mark.

- **Switched off.** Nothing links to either page, both are marked noindex, and the buy button stays hidden until a Stripe Payment Link is set in the page when sales open. A test checks that no other page links to them.
- **The purchase click.** The browser makes a reference of 22 base64url characters from 16 random bytes (128 bits), a new one for every click, keeps it in local storage for up to three hours, and sends the buyer to the Payment Link with it as `client_reference_id`. Nothing else is sent.
- **The return page.** It reads the reference from local storage, never from the address, and asks the server for the code with one request that carries only the reference, with no cookies and no referrer. If the code is not there yet it asks again every three seconds for up to a minute, then says so in words. A reload within the hour shows the code again, because the server's claim lasts an hour. It writes nothing to the console.
- **The words.** No price or money figure appears; Stripe shows the amount. The Table round cost on the page is read by a test against the operations file, so the two cannot drift.
- **Held.** The privacy section about codes waits for CO-6 and S11, as the review ruled: until then the privacy page keeps stating today's facts. The draft is with Mark. The door's one-line state on the home and Get Involved pages belongs to S5. Refund, expiry and lost-code policy are Mark's; the pages promise none.
- **Facts for Mark to verify before S11:** that a Payment Link carries `client_reference_id` through to the completion event, and that its after-payment redirect can point at the return page. The server must also allow the site's origin (`CIC_DEEPER_SITE_ORIGIN`) for the claim request.
- **Tests.** Readability of both pages, no money figure, the operations-file number, the two contribution links unchanged, the reference's length and uniqueness, the hour's expiry, the claim's retry and give-up, and no reference in the address or console. They run in the site job with Node.

**Popup flow (Mark, 2026-10-03).** To pay without leaving the conversation, "Get a code" in the app opens the site's go-deeper page in a popup. When payment finishes, the popup's return page hands the code to the conversation that opened it, which saves it. Payment Links stay the plan: no Stripe secret key on the server and no payment session route. The return page sends the code to the app's origin only, never a wildcard, and shows the code in the popup regardless, so if the browser has cut the link to the conversation the participant copies it as before. Gift and sponsor codes, minted by us, are how someone gets more time without paying; Stripe promo codes are a later option, once the amount check allows for discounts. Facts for Mark to verify: that Stripe's pages leave the opening window reachable after checkout.

**No paste (Mark, 2026-10-03), as changed by the Opus review.** The return page puts a single code into the conversation by itself. If the window that opened the popup is still there, the page sends it the code, to the app's origin only, and waits up to three seconds for the app to say it saved it, then closes. If that window is gone, silent, or answers from the wrong origin, the page sends this window to the app with the purchase reference, not the code, in the address fragment (`#cic-claim=`). The first version put the code there; the review found that browsers keep visited addresses, fragment included, in history that can sync to other devices, and a code is a bearer credential. A reference stops working when the server's claim hour ends, so a copy in history is dead soon after. The app reads the reference at once and clears it from the address, then asks "A code came with this link. Use it?" before doing anything, and says so if it would replace a code the person holds, so a crafted link cannot swap or plant a code silently. On a yes the app claims the code itself from its own server. A pack of several codes is never delivered this way and stays on the page. The site's reference lasts three hours locally and the server's hour decides; once a single code is delivered the reference is removed from the site's storage. The two addresses the site talks to are in one file, `assets/go-deeper-config.js`; for S11, `CIC_DEEPER_SITE_ORIGIN` on the server and `VITE_DEEPER_SITE_ORIGIN` in the app must both equal the site's exact origin (no `www.`).
## 2026-10-03 — Go Deeper S6: the app

S6 gives the app a way to hold a code and read what the server says. It ships switched off: the app is built with `VITE_DEEPER_ENABLED` unset, and S11 sets it.

- **The code.** "I have a code" under the message box opens one field. A code is checked for shape on the device (20 characters from the 32-letter alphabet, case and spacing forgiven) and kept in the browser's local storage, so it survives closing the tab. "Remove code" forgets it. With the build flag off no control shows, no header is sent, and a code left in storage by an earlier build is ignored.
- **What is sent.** The code goes as `X-Cic-Code` on session creation, messages, Table messages and `/continue`, and on nothing else.
- **What is shown.** The balance the server reports, in a line under the box: "12 exchanges left on your code." The number comes from the `X-Cic-Remaining` header, or from the stream's final event. The app knows no price and shows no money figure; a test checks the control's text for one.
- **A pause is not an ending.** The new `limit` Facilitator kind keeps the room open and the box enabled. The server's reason line (`limit_note`) shows once under the pause and is not kept, so a reload shows only the pause. The room closes only on `close`, as before.
- **Words.** The participant words are the set Mark approved on 2026-10-03, in one file, `cic-poc/frontend/src/lib/deeperCopy.ts`. The pause and its reason lines come from the operations file, not the app.
- **Parked.** After a pause the participant sends their message again once the code is saved; the app does not resend it for them. The flag-on frontend build is checked in S11 with the rest of the turn-on.

## 2026-10-03 — Go Deeper S6, balances: several codes, a getting-low line, Get more always

Mark's description of the product, 2026-10-03: the buying sits beside the conversation; at any time a person can open the popup, buy, and the access updates without leaving; they are told how much they have, and told again when they are getting close to needing more. Mark also said the price will be worked out later, using a token system that balances opening new conversations and rounds. This slice builds only what does not depend on that.

- **Several codes.** The app holds a short list of codes, each once, in the order they came. It sends the first one not known to be spent. When the one in use runs out the app moves to the next and drops the spent one; the last code is kept even when spent, so the server can say why it cannot carry on. A code added while one is held is added to it, not swapped, which also settles the review's note d on the popup. The balance line shows what the codes hold together, from each reply and from the server's own balance route, asked with no cookies.
- **Getting low.** The server says when the code in use is at or below `low_balance_at` in the operations file (5 today, Mark's number to set). It sends `X-Cic-Low` on the reply and `low` in the stream's final event. The app shows its getting-low line only when no other code is held to carry on with.
- **Get more is always there**, with a code held or not, beside the balance line.
- **A typed code is checked on the spot** against the server's balance route, so a wrong one is refused in plain words instead of being saved; if the server cannot be reached the code is kept and the next reply says.
- **Tokens.** The meter counts a plain whole number. A token system with different costs for opening a conversation and for a round changes what is charged at which step, not how a balance is held, so this slice does not stand in its way. The charge at opening a conversation is a separate change at the engine seam and waits for Mark's numbers.
- **New participant words, for Mark:** "Get more", "Your code is running low.", and the changed line "You already have a code. This one will be added to it."
- **Stale local build.** A frontend build left in `cic-poc/frontend/dist` makes the engine answer 405 where a test expects 404; the build output is derived and ignored, so nothing is committed.

**Opus review of the balances (#747), round one.** One blocking finding and notes a to e.
- Blocking: a reply's balance was credited to whichever code was in use when the reply arrived, not the code the request carried; a change made by another tab while the request was out could drop a live paid code. A reply is now credited to the code its request was sent with, and ignored if that code is no longer held.
- a. Two tabs changing the list at once could lose a code. Every change now starts from what is stored, not from the tab's memory.
- b. One tap removed every held code. "Remove code" now removes only the code in use.
- c. An unknown balance counted as empty in the getting-low check. It now counts as possibly carrying on, so the line shows only when no other code might.
- d. The balance fetch had no test for cookies; it has one.
- e. Wording for Mark: the balance line says "on your code" while it adds several codes together, and "Remove code" now removes one at a time. Proposed: "N exchanges left" (no "on your code"), and keep "Remove code".

## 2026-10-03 — Go Deeper: the unit is tokens (Mark's ruling, a named change order)

**Ruling.** A code holds tokens, one currency for everything. This is a named change order on the 2026-10-03 ruling "a code holds exchanges". Basis: the Token Proportions Study (https://claude.ai/artifact/NHompAUFtzwLVXEBYgbjJ8), including the approved three-seat Table run of 2026-10-03 ($0.62 at the rate card). Full text: the ruling block on the Handoff page.

| | Tokens |
|---|---|
| Solo: open a conversation | 50 |
| Solo: a round, rounds 1 to 3 | 20 |
| Solo: a round from round 4 | 25 |
| Table: open | 50 a seat (100 at two seats, 150 at three) |
| Table: a round at two seats / three seats | 60 / 100 |
| Table: a round from round 4, two / three seats | 75 / 125 |
| Free: a day | 330 |
| Free: a conversation stops after | 3 rounds; a code lifts the cap |
| Packs | $7 = 1,100, $15 = 2,750, $30 = 6,600; nothing under $7 |

**What this slice does (T0, no behaviour change).** The numbers go into `engine/deeper/ops/go-deeper.yaml` under `tokens`, read and checked at startup (whole numbers; a later round never cheaper than an earlier one; three seats never cheaper than two; packs rise in price and tokens; none under $7). The arithmetic is a pure module, `engine/deeper/tokens.py`. Nothing yet draws tokens: the meter still counts exchanges until T1.

**The opening amount (decided by Mark, 2026-10-03).** A conversation draws its opening amount with its first admitted round, on top of that round's own amount: a solo conversation of three rounds draws 50 + 3 x 20 = 110, so the $7 pack is 10 conversations and the free day is three. A Table at three seats is 150 to open plus 100 a round. Nothing is drawn by opening a conversation and leaving without a message. A test holds these facts.

**What the ruling changes next, one slice each, nothing built yet.**
- T1, the meter: reserve and settle in tokens, by round number and seat count; `table_round_cost` and the exchange count in `X-Cic-Remaining` retire. N7 and decision 45 (a Table round costs 3 exchanges; first numbered 36, corrected) are superseded by this ruling, recorded as System Hub decision 46.
- T2, the free path: a free conversation stops at three rounds and a free visitor has 330 tokens a day instead of 150 messages and five sittings. That touches the free allowance constants in the engine and `anon_cap.py`, which are the engine redesign's ground; coordinate before editing.
- T3, the words: every "exchange" in the app, the site pages and the Facilitator's texts becomes tokens, and the pack page offers three packs. Words are Mark's.
- T4, the door (S5): its priced sum and stages are in dollars already; the paid-voice-quality run (B5) is sized by the longest sitting a pack allows. At the $30 pack that is 60 three-round conversations, or one solo sitting of about 262 rounds; the run is sized to the long sitting, and Mark names which.
- `low_balance_at` becomes a token number; it is 5 today and must be reset by Mark.
**Opus review of the popup, round one (#744 and #745).** Three blocking findings, notes a to d on the site and a to c on the app, all fixed.
- #744 finding 1 and #745 finding 1: the address carried the code, and a link could plant or replace one. Now the address carries the reference, the app clears it at once and asks "A code came with this link. Use it?" and says when it would replace a code, and only a yes fetches the code.
- #745 finding 2: a code saved in another tab never reached an open conversation. The app now follows the stored code across tabs.
- #744 notes: a, the local reference lasts three hours and the server's hour decides; b, a delivered single code is removed from the site's storage; c, the site's two addresses are in one file; d, the S11 checklist names `CIC_DEEPER_SITE_ORIGIN` and `VITE_DEEPER_SITE_ORIGIN`, which must both equal the site's exact origin.
- #745 notes: a, the same origin point; b, a blocked popup now opens the page in the same tab; c, the app answers the popup on every screen, not only where the code field shows.
- New participant words from these fixes, for Mark's approval: "A code came with this link. Use it?", "You already have a code. Using this one will replace it.", "Use it", "Not now", "We couldn't get that code. Try the page where you paid."

## 2026-10-03 — Go Deeper: the offer is a panel beside the conversation (Mark's second ruling, a named change order on S6 and S7 as built in #743, #744 and #745)

**Ruling.** The offer is a panel beside the conversation. It opens at a limit or when the participant asks, never on its own. The participant pays on Stripe and returns to the same sitting. The app claims the code from the purchase reference behind the scenes and keeps it in the browser, and the sitting carries on from the pause. The participant sees a token count and nothing to copy. One opt-in line, "show my code", reveals the code for use on another device. Sponsors still hand out codes. Full text: the second ruling block on the Handoff page.

**The cost the ruling accepts.** Without "show my code", a cleared browser or a second device loses the balance. A member enters a sponsor's code once. Nothing in the three stores, the meter or the tests changes.

**Two Stripe facts to verify before S6 and S7 ship.** The ruling named the build thread; Mark took them himself on 2026-10-04, since the sandbox blocks stripe.com. Whether Stripe's return redirect can carry the participant back to the exact sitting. Whether in-page checkout exists on a Payment Link. Neither is assumed.

**What stays.** The claim route and its one-hour table, the meter, the operations file, sponsor codes, the stored list of codes, balances and the getting-low flag.

**What this reshapes, one slice each, nothing built yet.**
- The popup "Get a code" and the return page with its Copy button give way to a panel and a return to the same sitting. The return reference travels back to the app, which claims the code without showing it.
- The "I have a code" entry stays for sponsors and for a code used on another device. The code field and the "show my code" line sit inside the panel.
- No sitting or session id goes into any Stripe-bound URL or field (success_url parameter, client_reference_id, metadata). The return reaches the app by the purchase reference alone, and the app's own browser state finds the sitting.
- The balance line becomes a token count. The words for the panel, the count and "show my code" are Mark's: one question when the slice is ready.

## 2026-10-04 — Go Deeper T1: the meter draws tokens by round and seats

Carries out System Hub decision 46 on the meter. Still switched off behind the flag.

- **The meter counts tokens.** Its columns, status fields, the mint call and a purchase's product table say tokens, not exchanges. No meter file exists anywhere yet (the module has never been switched on), so the columns were renamed in place with no migration. The claim route answers with `tokens`.
- **What a turn draws comes from the round and the seats.** Admission reserves `charge(round, seats)` from `engine/deeper/tokens.py` before the turn and settles it after: a solo round is 20 (25 from round 4), a Table round 60 or 100 by seats (75 or 125 from round 4), and the opening amount is added once, to the first admitted round of a sitting. A sitting that crosses from free into paid at round 4 draws no opening amount: the conversation was opened when it started. The engine still receives only a cap and a flag.
- **`table_round_cost` is retired** from the operations file and the loader. A file that still carries it is refused.
- **Two numbers converted, for Mark to set.** `group_daily_ceiling` 300 exchanges becomes 6,000 tokens and `low_balance_at` 5 becomes 100, both at one exchange = one 20-token round. These are conversions so the shipped file keeps its old meaning, not rulings.
- **Words not yet changed.** The balance line, the refusal notes ("no exchanges left") and the site page still say exchanges. T3 rewrites them in tokens for Mark's approval. The sentence on the site page giving a Table round's cost is removed, since it no longer holds.
- The free path (330 a day, three free rounds) is T2 and touches the engine redesign's constants; not in this slice.
- A positive test through `api.ts` that a reply's balance reaches the code the request carried, plain and stream (the open note from the #747 review).
- **Review fixes (Opus, #755).** A seam test opens a 2-seat and a 3-seat Table with a code and asserts the literal draws (160 then 60; 250 then 100); capping seats at 2 in the app or in the charge fails it. A reply with no words is no longer counted as voiced, so the round number and the opening amount stay in step with the memory the next turn counts from. The most one code can hold is 1,000,000 tokens, so a large group pack is not refused by the sanity bound.
- **For the S11 checklist:** T3 (words in tokens, three-pack page) must merge before the module is ever switched on, because the app, the site page and the refusal lines still say exchanges until then.

## 2026-10-04 — Go Deeper P1: the panel beside the conversation (words approved by Mark)

Carries out the panel ruling on the app. Still switched off with the build flag.

- **The panel replaces the code line.** A strip under the message box shows the token count, and the panel opens when a turn comes back refused (a limit note arrives, on an interview or a Table round) or when the person asks. It never opens on its own otherwise. Escape and a Close button shut it. On a wide screen it sits beside the conversation; on a narrow one it rises from the bottom. The conversation underneath is untouched, so the sitting carries on from the pause.
- **Inside it:** the intro, the count and the low line, Get more tokens, I have a code, a "show my code" line that reveals the code held (or each code, if several) for use on another device and hides it again, and Remove code. A code that arrives with a link opens the panel and asks first, as before.
- **Words.** Mark approved the panel words as proposed on 2026-10-04: "Go deeper", the intro line, "N tokens left.", "Your tokens are running low.", "Get more tokens", "I have a code", "Show my code" and its reveal line, "Hide my code". "Close" is added as a plain control label. The old "Get a code" and "exchanges left on your code" are gone from the app.
- **Not changed, because the two Stripe facts are unverified:** "Get more tokens" still opens the site's page in a popup, and a code still comes back by the popup message or a purchase reference in the address. The return to the exact sitting and any in-page checkout wait on Mark verifying them (he took them himself on 2026-10-04, since the sandbox blocks stripe.com); no sitting or session id goes into a Stripe-bound field either way.
- The site pages and the server's refusal lines still say exchanges; T3 changes them with the three-pack page.
- Tests: the panel's behaviour (closed until asked, opens at a limit, code reveal and hide, claim prompt, popup origin check), and that an interview turn and a Table round each open it when a limit note arrives.

## 2026-10-04 — Go Deeper T2: the free day in tokens, and the free conversation stops after three rounds

Carries out the free half of System Hub decision 46. Still switched off behind the flag; with the module off the free path is exactly as it was.

- **Where it lives.** Entirely in the module's admission seam: a new in-memory `DailyFreeAllowance` (`engine/deeper/free.py`, standard library only) and `engine/api/deeper_admission.py`. `anon_cap.py`, `SESSION_TURN_CAP`, `TABLE_SESSION_ROUND_CAP`, `wiring.py` and `table_wiring.py` are untouched, so none of the engine redesign thread's ground moved. That thread was told so.
- **How it works.** With the module on, a turn within a conversation's first three rounds draws its amount (the same `charge(round, seats)` a code draws) from the visitor's free day of 330 tokens (held before the turn, spent when the turn is voiced, given back otherwise). The visitor is the daily-cap cookie's id when there is one, else the address. When the third round is done, or the day cannot cover the turn, a code carries it instead, as before; with no code the Facilitator gives the neutral pause and the participant is shown the no-code line. A code lifts the stop: round 4 on draws the later price.
- **What it means in numbers.** Three solo conversations of three rounds use the day exactly (110 each). A Table at two seats fits its three free rounds (160, 60, 60); a Table at three seats opens (250) and its second round (100) does not fit, so a code carries it from there.
- **Counters left alone.** The daily 150-turn and 5-sitting counters stay as the abuse backstop; the free day binds first.
- **Not shown to the participant yet:** the free day's remaining tokens. The panel shows a count only for a held code; whether to show the free day too is Mark's, with T3's words.
- **Refuses to start without the visitor cap.** The free day is kept per visitor; without the cookie everyone behind one address would share one day, so the module on with `CIC_API_ANON_CAP_ENABLED` off is refused at startup.
- **Safety at the new limits.** The proof matrix now includes a fresh conversation refused because the free day is spent, and one refused after its free rounds: acute distress, an unclear turn and a failed safety check each get their Facilitator answer, and an ordinary message gets the pause with no voice call. The allowance's own file is checked never to log, persist or import anything beyond threading, datetime and typing. It resets on the UTC day, with the daily counters.
- **Still soft:** the free day is memory only, so a restart gives everyone a fresh day, as the daily counters already do.
- Tests: the allowance itself (hold, spend, give back, double settle, a new day, separate visitors); a free solo conversation stops after three rounds with the no-code line and the voice is not called for the fourth; three conversations exhaust the day and a code carries the fourth; a code carries round 4 at the later price; a failed voice call gives the free tokens back; Tables at two and three seats draw by seats and stop after three rounds; with the module off a fourth round still runs.

## 2026-10-04 — Go Deeper S5a: the door's funds (how the week's gifts and purchases reach the app)

**Ruled by Mark, 2026-10-04: Stripe plus my adjustments.** Gift payments and go-deeper purchases arrive by the signed webhook the codes already use and are counted over the last seven days; refunds and disputes subtract. Mark can also post a manual adjustment behind the admin login for friends-and-family gifts. No total to keep by hand.

**What this slice builds (the door itself is S5b and S5c).**
- A `funds` table in the meter's file (so the daily backup already covers it): the day, a kind (gift, purchase, adjustment), whole cents, the Stripe payment id for the two Stripe kinds, a note on an adjustment, and a reversed flag. The entry id is random, the table has no row order, and no time finer than a day is kept, in the same way as the rest of the meter. No code, buyer, session or visitor is anywhere in it. Rows are deleted 90 days on.
- The webhook records a paid checkout's `amount_total` as a purchase (a go-deeper Payment Link) or a gift (a link named in `CIC_DEEPER_GIFT_LINKS`). A link cannot be both, so a purchase is never also a gift. A replayed event adds nothing; a payment refunded before its completion arrives adds nothing; an unpaid checkout, or one with no usable amount, adds nothing and logs the fact.
- A refund or dispute reverses the payment's entry along with voiding its code.
- Admin: `POST /api/admin/deeper/funds` (cents and a short note), `POST /api/admin/deeper/funds/{entry}/reverse`, `GET /api/admin/deeper/funds` (the seven-day sum by kind and the last fourteen days' entries, without payment ids). A reversed entry stays listed.

**Added to the unverified Stripe facts for Mark:** that a completion event carries the amount paid as `amount_total` in cents, that gifts go through their own Payment Links (S4), whether Adaptive Pricing is on for these links, and which currency `amount_total` is in when it is.

**Money is counted only in US dollars.** A checkout whose currency is not `usd` is logged and adds nothing, so a payment in another currency cannot be read as dollars and lift the door. **A partial refund is not subtracted** (as for codes, it is ignored); only a full refund or a dispute takes a payment back out, so a partially refunded gift stays counted at its full amount. **Adjustment notes are plain words about the money ("church gift, cash"); never a person's name or email.** The notes are kept 90 days and listed to the admin.

**Still to come:** S5b computes the week's priced spend from the usage log (the approved price tables in `engine/m8/price_tables.py`, times the measured invoice factor) against a ceiling of the base number plus a share of these funds; S5c lets admission narrow the free path in stages, failing closed to the last computed stage. The base number, the stage thresholds, the gift and purchase shares and the invoice factor are Mark's; each will ship in the operations file with a stated default.

## 2026-10-04 — Go Deeper T3: the words in tokens (approved by Mark), and a ruling on the free count

**Words.** Mark approved on 2026-10-04, as written: four refusal lines (no code "To carry on in this conversation, add tokens or enter a code."; spent "Your tokens have run out. Add more to carry on."; too few "You do not have enough tokens left for a Table round. Add more to carry on."; in use "Your tokens are in use by another conversation. Try again in a moment."), with the other three unchanged, and the Go Deeper page: the free part is three rounds a conversation and a free daily allowance; tokens pay for each new conversation and each round; three packs ($7, $15, $30) with what each holds; "open Go deeper beside the message box".

**The approved text, verbatim.** Refusal lines: no code "To carry on in this conversation, add tokens or enter a code."; spent "Your tokens have run out. Add more to carry on."; too few "You do not have enough tokens left for a Table round. Add more to carry on."; in use "Your tokens are in use by another conversation. Try again in a moment." The page: "Every conversation here starts free. A free conversation lasts three rounds, and each day has a free allowance. When the free part ends, tokens let you carry on in the same conversation." / "In a conversation, open Go deeper beside the message box and enter your code. The conversation carries on from where it stopped." / "A new conversation uses 50 tokens. Each round, one question from you and one answer, uses 20 tokens, or 25 after the third round. A Table uses more, by the number of voices. We show how many tokens you have left beside the message box." / "$7: 1,100 tokens, about ten conversations of three rounds", "$15: 2,750 tokens, about twenty-five", "$30: 6,600 tokens, about sixty", "Stripe shows the amount before you pay."

**Two words to put to Mark.** The approved page says the count is shown "beside the message box"; the strip with the count sits under the message box, and the panel sits beside the conversation. And "the next page shows your code" (how it works) stops being true after the panel rework (the code is claimed behind the scenes and shown only on request); that page is listed for that slice.

**What changed.** The four lines in the operations file; the page's intro, how-it-works step, "what tokens pay for" and "three packs" sections; the old Table-round sentence stays gone. Every figure on the page sits in a marked span and a test compares each to the operations file (solo opening and round prices, the later-round price, each pack's price and tokens), so a change to the file cannot leave the page wrong. A second test checks each pack line's "about N conversations of three rounds" against the pack's tokens divided by a three-round conversation (110). The page may now show the pack prices and nothing else with a money sign; that check is narrowed to the pack lines.

**Not changed.** Choosing a pack at purchase needs one Stripe Payment Link per pack mapped in `CIC_DEEPER_PRODUCTS`; that is Stripe setup (S4, Mark's hands), and the page's single buy button stays hidden until then. The page is still unlinked and not indexed until S11. With T3 merged, the S11 checklist item "T3 before any flag-on" is met.

**Ruled by Mark, 2026-10-04: a free visitor sees their free tokens left today**, in the strip under the message box, as a code holder sees a count. One more slice (T3b, after T2 merges): the server reports the free day's remainder with each reply (a response header and the stream's final event, neither stored), and the app shows it in the same strip. The words for it are one line for Mark.

## 2026-10-04 — Go Deeper S5b: the door's computation (base number ruled by Mark; the rest are stated defaults)

**Ruled by Mark, 2026-10-04: the weekly base is $150.** The other door numbers ship in the operations file as stated defaults for Mark to change by pull request: the gift share 0.8 (also applied to adjustments), the purchase share 0.5, the invoice factor 1.35 (the AWS bill ran 28.6% and 35.1% above list on the two days measured; the dearer is used), and five stages. Nothing is switched on: this slice computes the door's state and nothing consults it yet (S5c).

**The arithmetic** (`engine/deeper/door.py`, standard library, no model, price or world in it). Ceiling = the base + 0.8 of the week's gifts and adjustments + 0.5 of its purchases (money never lowers it below the base). Ratio = the week's list-price spend times the invoice factor, over the ceiling. Each stage whose threshold the ratio has passed narrows; a stage can only narrow, so a higher ratio never opens what a lower one closed. Default stages: 66% free Table rounds limited to 1; 75% the free day halved and free solo rounds limited to 2; 90% free Tables closed; 95% free voice closed; 100% paid voice closed (zero headroom). The Facilitator is not part of this and nothing here can close it. The numbers come from the design's illustration (a Table limited at 66% closed and stopped at 90%; a solo conversation full until 75% and stopped at 95%).

**The spend** (`engine/api/deeper_door.py`). The last seven days of the usage log, each participant call priced at the approved table for its model and call kind (`engine/m8/price_tables.py`). A call on a model with no approved row, or of a kind the tables do not know, is counted at the dearest approved price in each category rather than left out, so it can only make the door narrower. Preflight and other system calls are left out. The state is refreshed at most once a minute; if it cannot be worked out the last good state stands, so a fault never opens what had closed. The last good state, with every field it narrows, is kept in the meter's state table whenever it changes (the table the pause uses) and read back at startup, so a restart during a fault does not open the door either. Only an install that has never worked a state out starts open.

**Two things named plainly.** The $150 base covers the participant calls the usage log prices; system calls (preflight, evidence scripts) are outside it. The spend is a rolling 7 x 24 hours while the funds are the last 7 calendar days, so the two windows differ by up to a day at the edge.

**One additive read in M8's file:** `UsageLogStore.read_since(iso)`, a windowed read (the usage dashboard's cost half is all-time because the log had no windowed read; this adds one and changes nothing else in that file).

**The operations file** gains a `door` section, checked at startup: positive base, shares 0 to 1, invoice factor at least 1, stages rising strictly, every field only narrowing, free voice never reopened, and paid voice never closing before free voice does.

**Still to come:** S5c, where admission narrows the free path by these stages and fails closed, with the safety matrix and the overlap test (priced spend stays under the ceiling plus the turns in flight). The participant-facing words for a door-closed refusal are Mark's: until then a closed free path shows the existing no-code line, and a closed paid path shows the paused line.

## 2026-10-04 — Go Deeper S5c: admission narrows the free path by the door's stage

Still switched off behind the flag; with the module off nothing changes.

- **What the stages do at admission.** The door's state is read at each admission. From stage 1 on: free Table rounds are limited, then closed; free solo rounds are limited; the free day is scaled down (halved at the default's stage 2); at the stage where free voice closes, a visitor with no code gets the neutral pause with the no-code line and no voice call; at the last stage a code is refused too, with the paused line, and nothing is spent. The rounds a stage allows are the smaller of that number and the free path's own, so a stage can only shorten a conversation. A code carries a conversation the door has stopped for free, until the last stage. A round already admitted is not stopped part-way.
- **The Facilitator stays at every stage.** Every refusal is a grant the engine answers with the Facilitator, which runs the safety check first. The safety matrix now includes the door's two refusals, and a Table the door has closed: acute distress, an unclear message and a failed safety check each get their Facilitator answer, and an ordinary message gets the pause with no voice call.
- **The bound, shown.** A simulation puts forty free sittings and forty coded sittings in turn against a $1 base, each voiced turn priced into the usage log; the door moves through every stage in order, the voice's cost stays at or under the base plus one turn, free voice closes, and at the last stage a code is refused and keeps its balance.
- **A cost the door cannot stop, stated:** every message, even a refused one, still gets its safety check (two small model calls, about $0.003). The door bounds the voice, not those checks. The door's ratio counts them, so they bring the door's stages on sooner. Before the module goes on, S11 should size this against a visitor who keeps messaging at a closed door (the per-visitor and per-address limits already bound it).
- **A fault never reopens a closed door.** If admission itself fails, the engine is handed a grant that keeps to the door: a refusal when free voice is closed, otherwise a free grant no longer than the door's rounds allow. The operations file refuses a free-day share of 0 (a closed free path is a stage, not a share). A restart with the usage log down still finds the door where it was left.
- **Wiring.** The runtime builds the door when it is given the usage log (the real app is); tests without it have no door. `GET /api/admin/deeper/door` shows Mark the stage, ratio, ceiling and whether free and paid voice are open.
- **Words:** a closed door shows existing lines only (no-code for a closed free path, the paused line for a closed paid path). A line of its own for a closed door is Mark's to approve; candidates when he wants them. The public one-line door state on the home and Get Involved pages is a later slice with Mark's words.

## 2026-10-04 — Go Deeper S5d: the public line about the free conversations (words approved by Mark)

Still switched off behind the flag. With the module off no route exists, so the pages show nothing and their one request gets a 404.

- **Ruled by Mark, 2026-10-04: the line shows only when the door has narrowed.** Nothing shows while the door is wide open.
- **His words, kept in the operations file** (`words.door`): "Free conversations are limited this week. Gifts keep them open — give at Get Involved." while the free path is narrowed; "Free conversations are paused until the week turns. A code still works." when free voice is closed. His second sentence is stored as its own line so it can be left off at the last stage, when codes are refused too and "a code still works" would be untrue. At that stage only the first sentence shows. If Mark wants a line of his own for that stage, it is a words change in the operations file.
- **What the route sends:** `GET /api/deeper/door` returns the state name and the line, nothing else: no stage number, no ratio, no ceiling, no money. It may be kept for a minute.
- **Where it shows:** a hidden line under the headline on the home page and on Get Involved, filled by `assets/door-line.js` only when the server sends one. Any failure leaves the page as it was.
- **A test rule refined:** the page test that kept the site from linking to the Go Deeper pages now forbids links to those pages, not the shared address file the home and Get Involved pages also load.
- **The site stays quiet until turn-on.** `go-deeper-config.js` carries `enabled: false`; the door line makes no request while it is false. S11 flips it with the module. The no-link test now catches an extensionless link such as `/go-deeper`, which the host serves.
- **Raised for Mark with the next words question:** "give at Get Involved" also shows on the Get Involved page itself.

## 2026-10-04 — Go Deeper S9: the standing measure (daily totals, no keys)

Still switched off behind the flag. With the module off no route exists and the dashboard section stays hidden.

- **What is kept:** one number per measure per day, in a new `daily` table in the meter file (no rowid; the key is the day and the measure name, nothing else). Codes minted by kind, tokens sold, tokens spent, the highest door stage reached, and refused turns by reason: no code, code not accepted, spent, too few, group daily limit, paused, in use, free rounds done, free day spent, door closed to free, door closed to codes. Ninety days, then dropped, like the reconciliation counts.
- **Each refused turn counts once,** when the turn ends, by the reason admission gave, and a failed measure never changes a grant. This is the count the S5c note asked for: turns refused at a closed door, and what a visitor who keeps messaging at one adds up to.
- **Where it shows:** `GET /api/admin/deeper/measures` (admin only) returns the last fourteen days and the reconciliation counts; a Go Deeper section on the existing admin dashboard shows today's tiles and a day-by-day table. The money not yet matched to codes is the reconciliation gap.
- **One measure left out, stated:** crisis turns. The module never sees what a message says, so it cannot count them. A crisis count belongs on the engine's side, from the routing it already records; it is an open gap for the engine thread and for Mark to ask for.
- **Still to come in S5:** the plan's week of observe mode (the door computing and showing its stage while narrowing nothing) is not built; the door narrows from the first week it is on. Mark decides whether to add it before turn-on (S11).
- **A count never changes work.** Every measure is written best-effort: a failure is logged and the purchase, the spend, the grant and the door stand. The group daily ceiling's running total is updated before the spend's count is written, so a failed count cannot loosen it (a test makes the count fail and the ceiling still refuses at three).
- **Stated over-count:** a refused turn is counted when the grant refuses, even if the safety check then lets the message through to the Facilitator for a check-in or distress answer. The count is of refusals, not of turns that went unanswered.
- **A residual for the privacy page's list:** at pilot volume a day's refusal counts and tokens spent are small numbers, and someone holding the meter file and knowing when one person used the app could read that person's day from them. They hold no code, visitor, address or time of day.

## 2026-10-04 — Go Deeper S11: the turn-on and rollback runbook, and the balances-owed report

Still switched off behind the flag.

- **The runbook** is `Build/Ministry/Operations/Standing/CiC_Go_Deeper_Turn_On_Runbook.md`: what must be true before the staging rehearsal, every setting and where it lives, the fourteen-step rehearsal Mark walks, the paid voice-quality run (sample first, settings passed on the command and printed, a stated cap, Mark's approval before anything runs), the four production steps (ship dark; engine on; app on; site on), a rollback from lightest to heaviest, the removal checklist, and what to watch in the first weeks. The build thread has run nothing paid.
- **The balances-owed report:** `GET /api/admin/deeper/owed` (admin only) lists, by Stripe payment id, the unspent tokens on every payment that has any. It holds no code and no hash. What is refunded is the refund policy, which is Mark's.
- **The website ships from `main`,** not `live`, so the site stays dark by its own settings (`enabled: false`, no link, no payment link), which step 4 changes.
- **Open for Mark before step 2:** whether to add the week of observe mode; the per-pack Payment Links; the policy and words items listed in Part 1.
- **Opus review round one on the runbook, all five blocking findings taken.** The anonymous-cap setting takes `1`, `true` or `yes`, not `on`. There is no hand-mint path, so the first live codes are real smallest-pack purchases through an unlinked Payment Link, refunded. The production steps are cumulative, and any doubt about money starts with deactivating Payment Links, because pausing codes does not stop Stripe selling and a removed webhook leaves buyers with no code. A partial refund is not seen by the module, so `POST /api/admin/deeper/void` voids a payment's codes the way a full-refund event does, and the runbook states the double-refund risk and the rule that the module stays off until balances are voided. The paid run is sized to the longest solo sitting (about 262 rounds), with its size put to Mark.
- **Round two on the runbook (B6 and notes):** the owed snapshot and the voids now happen before the engine is turned off, because both routes are gone afterwards; an engine-only switch-on just to void is allowed under stated conditions. The void is only for a wholly refunded balance. A mistyped payment id answers 404 and records nothing, and a late completion for a voided payment is shown to mint nothing.

## 2026-10-04 — Go Deeper S5e: the door starts in observe mode; no paid voice-quality run; a provisional round cap for paid conversations

Two rulings by Mark, 2026-10-04. Still switched off behind the flag.

- **No paid voice-quality run now.** The new engine is about to land and would make the result stale. The question the run was meant to answer, how many rounds a paid conversation may run before quality falls, is answered from the new engine's own baseline runs when they exist. S11 step 4 is not gated on a paid run. This change order retires the paid run named as a precondition in the handoff (B5) and in the runbook.
- **A per-conversation round cap for paid conversations,** in the operations file under `paid`: `round_cap: 40`, `provisional: true`. The 40 is the build thread's safe default, with no measurement behind it, and is Mark's to replace when the new engine's baselines exist. Past the cap a code is not spent, the turn is refused, and the Facilitator answers with the neutral limit text. No new participant words are added; a line of its own for this stop is Mark's to approve. The refusal is counted as `paid_round_cap` on the dashboard.
- **Door: a week of observe mode before it narrows anything.** `door.observe: true` ships in the operations file. The door is worked out every minute and its stage is kept, but admission uses an open door: no free round, free day or code is narrowed, the public door line says nothing, and a closed door refuses nobody.
- **What it would have done, each day:** the dashboard's Go Deeper table gains, for each day, the door's peak stage, the peak share of its ceiling, the peak weekly spend it saw, and the number of voiced turns it would have refused, free and coded separately. Mark sets the base number and thresholds from that, in the operations file by pull request, then sets `door.observe: false` and the door goes live.
- **A limit of the counts, stated:** the free-day share scaling (halving the free day at a stage) is not counted as a would-have-refused turn, because a scaled day refuses only when the day runs out. The peaks show how close the week came.
- **Opus review of S5e, taken:** the safety matrix now has a row for the paid round cap and one for a door that is closed but only observing, so distress, an unclear message and a failed safety check each get the Facilitator at both; counting an observed turn happens once; a no-code turn past the cap is not counted as the cap; and noting what the door would have done can never change a grant. **For Mark's words question:** the cap stop shows only the Facilitator's neutral line, but the participant's code still holds tokens, so a line saying so is needed.

## 2026-10-04 — Go Deeper S2b: the free grant becomes a 30-day window, kept in the meter's file (ruled by Mark)

Ruling by Mark, 2026-10-04, amending the free grant: **550 tokens a month, five solo conversations of three rounds, refilling 30 days after a visitor's first use (rolling, not calendar). The daily 330 is withdrawn.** The counter is kept in the meter's store, not in memory, so a deploy does not refill it. A free conversation still stops at three rounds, and a code lifts the cap. Basis: the ruling block on the Handoff page (the refill-window check of 2026-10-04). Still switched off behind the flag.

- **Operations file:** `tokens.free` now holds `window_tokens: 550`, `window_days: 30` and `rounds_per_conversation: 3`; the daily number is gone. Five conversations of three solo rounds cost 110 tokens each, which is the whole 550.
- **How the window runs:** a visitor's first settled draw starts their window. A draw after the window has ended (30 days after its first day) starts a new one. A reservation alone never starts a window, and a turn that was not voiced draws nothing. Days, not times, are kept.
- **Where it is kept:** a new table in the meter file, `free_window`, with a hashed key, the first day and the amount drawn, and nothing else. A row is deleted when its window ends. A restart, a deploy and a crash no longer refill anyone.
- **A tension with decision 19, stated for Mark.** Decision 19 as amended says the meter keys on a hash of the code, never on a cookie or an IP. A free window kept per visitor needs a key from the visitor: the cookie id the free path already uses, or the address when there is none. To keep the meter file from naming a visitor, the row key is a keyed hash (HMAC-SHA256) under a secret from the server's environment, `CIC_DEEPER_FREE_KEY`, at least 32 characters, required at start like the webhook secret and **never written to disk**. A first version kept a random salt in the meter file; Opus's review showed that anyone with the file, or a daily backup of it, could then match windows to the conversation store's visitor ids, and could recover an address from an `ip:` key by trying every IPv4 address. With the secret outside the file, neither works from the file alone. Tests read the file's bytes for the secret and for a raw address, and check that no salt row is kept.
- **What still remains, stated:** whoever holds the secret and the meter file, together with an event store that carries the same visitor ids, can match a window to a visitor's sessions. Rotating or losing the secret refills every window, since every row key changes. Backups of the meter file keep a window's row after the purge has deleted it from the live file, for as long as the backup is kept.
- **Soft by design, as before:** a visitor who clears their cookie, or whose address changes, starts a new window, and a client that keeps no cookie at all gets a fresh window with each visit when it is not keyed by address. This is an allowance, not a ledger.
- **Renames that follow from it:** the door's stage setting `free_day_share` is now `free_share`, the refusal reason `free_day_spent` is `free_allowance_spent`, and the dashboard says "free allowance". The numbers and behaviour of the door are unchanged.
- **Words that are now untrue, for Mark:** the Go Deeper page says "each day has a free allowance". The page is unlinked and switched off, and the sentence needs Mark's replacement before the site goes on.
- **Opus review of S2b, taken:** the key is now the server secret above (the blocking finding), the meter's own description says what the free window table holds, and the residuals are named.

## 2026-10-04 — Go Deeper: the free allowance line on the Go Deeper page (words approved by Mark)

Mark chose the recommended line to replace the sentence the 30-day window made untrue. The page now reads: "A free conversation lasts three rounds, and you get a free allowance each month." The number of rounds is still filled from the operations file. The page is unlinked and switched off until turn-on.

## 2026-10-04 — Go Deeper: the privacy page's Go Deeper words (drafted by the build thread at Mark's instruction, for him to edit)

Mark asked for the recommended wording on the privacy page "for now", to be edited later. No wording had been put to him, so the build thread drafted it and says so here. The page is public and live today, so the new words are hidden until Go Deeper is turned on and shown by the same switch as the rest of the site (`enabled` in `go-deeper-config.js`).

- **A Go Deeper section** says: tokens are paid for on Stripe's pages and Stripe holds the name, email and payment details; a code holds the tokens and only its hash, the token count, the Stripe payment id, the day made and the week last used are kept; the three records are kept apart with no shared ID, with the residual stated (someone who could see all of them and the Stripe account might guess which conversation used a code); the free allowance is kept per visitor as a scrambled value, a day and an amount, deleted 30 days after the first day, up to 14 more days in a backup, and deleting the cookie ends the match.
- **The cookie paragraph** swaps "one job" for "two jobs" when Go Deeper is on, since the cookie's id now also keys the free allowance.
- **Checks:** the section reads at the target level, names no money figure, and its numbers are tested against the free window in the operations file and the backup keep in the backup job. With Go Deeper off, the page is unchanged.
- **For Mark:** this is a draft. The CO-6 gate in the Handoff (the conversation redesign) is not met by it. The deletion section and retention section do not yet mention Go Deeper records.
- **Opus review of the privacy words, taken (three blocking findings, all sentences that were untrue):** the words no longer say no ID is shared, because the token records and Stripe both hold the payment ID (kept so a refund can cancel a code); they now say the plain code is held for up to one hour with the browser's reference and never backed up; and they no longer say the conversation system never receives Stripe's details, because Stripe's payment notice can carry a name and email, of which only the payment ID, the amount and the pack are used and nothing else is kept. The webhook handler logs only the event type and its outcome. The free-window residual (someone with the server's secret key and the conversation records) is stated. At step 4 the hidden attributes are removed from the HTML itself.

## 2026-10-04 — Go Deeper S13: the admin mint page, and the live-day controls on the dashboard (ruled by Mark)

Ruling by Mark, 2026-10-04, on where the module is run from: **Stripe holds money; the admin dashboard holds the live day (pause switch, mint page, the door's current stage, the tiles), with effect at once; the operations file, changed by pull request, holds the shape of the offer.** The free grant has no live dial and no formula tying it to inflow: the door moves the free table by its stages, and the baseline is a line in the file.

- **The mint page:** `POST /api/admin/deeper/mint` behind the existing admin login. The operator picks one of the offer's packs, a count, and either "that many separate codes" (a batch) or "one code holding the whole amount" (a single code). The codes come back in that response only. The meter keeps their hashes and nothing else, so a lost response is cancelled by its mint id, never recovered.
- **Never a payment, never a sale:** a grant's id starts `admin_` and the meter refuses the prefix on a Stripe payment. It counts in its own reconciliation column (`admin_codes_minted`; `pilot_codes_minted` is ready for S12), not as a payment seen or minted, so the "money not matched to codes" figure cannot be moved by a grant. It counts as tokens granted, not tokens sold. It is left out of the owed list, since nothing was paid. Voiding the mint id cancels its codes and takes its gift out of the door, and does not count as a refund.
- **The door counts it as a gift, by the pack's price (a number for Mark to confirm).** Mark ruled that admin and pilot mints count as gifts and never a sale, and gave no dollar value. The build thread used the packs' price: a $7 pack raises the weekly ceiling by 0.8 × $7 = $5.60 at today's gift share. If that is too generous, the choice is a smaller value or none, and it is one line.
- **Limits, in the operations file** (new `admin` section, defaults chosen by the build thread, for Mark to set): 6,600 tokens a request and 13,200 a day, in tokens so a "whole amount" code cannot hold more than a batch would. The day's limit is checked in the same transaction that makes the codes, so two requests at once cannot both pass. A voided grant still counts toward the day, so a stolen login cannot get past the limit by cancelling and trying again.
- **Dashboard:** the Go Deeper section gains the pause switch, the mint form (with a confirm step and a one-time code display that can be copied or hidden), tiles for admin mints and pilot mints today, the door's stage and the current free grant beside them, read-only. `GET /api/admin/deeper/status` feeds these. The pilot tile reads 0 until S12.
- **Why a JSON-only check is not added:** FastAPI already refuses a body that is not sent as JSON, and the admin cookie is `SameSite=Lax`, so a form post from another site neither carries the cookie nor parses.
- **Opus review of S13, taken:** the rule that a cancelled grant still counts toward the day's limit is now tested. The dashboard lists the last two days' grant ids (ids, counts and token totals, never codes) so a grant whose response was lost can be cancelled, and the code display clears when the tab is hidden as well as on Hide. A failure to count a grant's gift no longer fails the grant. **Left as is, for Mark:** a grant's gift sits in the same funds kind as real gifts; a separate kind would need a change to the funds table, and the grant's id and note already tell them apart.

## 2026-10-04 — Go Deeper S12: the pilot join, one shared link with a cap (ruled by Mark)

Mark ruled: a pilot link that awards one $7 package automatically, as a one-time offer; **one shared link with a cap**, not a link for each person. Percentage discounts stay in Stripe (Mark's ruling: "keep it in Stripe for now"); only a free grant is made inside the module.

- **How it works:** a page's button calls `POST /api/deeper/pilot-join`, which makes one ordinary code of the chosen pack's tokens with no payment and shows it once. The code is made on the press, not on the page load, so a link preview or email scanner cannot use one up.
- **Operations file** (new `pilot` section): `pilot_open` (ships `false`), `pilot_cap`, `pilot_end_date`, `per_address` and `pack_usd`. Defaults chosen by the build thread, for Mark to set: cap 50, end date 31 December 2026, 2 per address, the $7 pack. Two per address, not one, because a household, a school or a homeschool cohort can share an address, and because a lost response cannot be replayed.
- **One at a time, atomically:** the open switch, end date, cap and address count are checked in the same transaction that makes the code, so two joins at once cannot both take the last place. A refusal takes nothing. The cap counts every code ever given, kept as one number that survives the address rows, so a second pilot needs a higher cap.
- **What is kept:** the address as a keyed hash (the same secret and construction as the free allowance), how many codes it has had and the day of its first; rows are deleted after 90 days. No plain address, no code, no time of day. The route is left out of the access log with the rest of `/api/deeper`.
- **Never a payment:** the code's id starts `pilot_`, it counts in the `pilot_codes_minted` reconciliation column and as tokens granted, is left out of the owed list, and counts toward the door as a gift of the pack's price (the same open number for Mark as the admin mint). The dashboard shows given against the cap, whether it is open, the end date and today's count.
- **Refusals:** a closed pilot is a 404, so a link found early shows nothing. An ended, full or address-limited join answers 409 with its reason, and the page that shows the participant words is built after Mark approves them.
- **Not built yet, stated:** the page itself, its words and consent line, the pilot marker on conversations, the group id and the survey line. They need Mark's words, and the group id needs an attack review as a possible join between records.
- **Carried from the S13 review:** a failure to count a grant's gift never fails the grant, whatever the error.
- **Opus review of S12, taken:** an IPv6 address is now counted by its /64 block, for the pilot's per-address count and for the Go Deeper routes' rate limit, because one connection holds a whole /64 and could otherwise take every code in seconds. IPv4 stays exact. Address rows are kept 90 days, as this entry says, and a boundary test pins it (it was 30 in the code). A preflight to the pilot route is a 404 while the pilot is closed. **Cost for Mark, stated:** two codes an address means a shared address (a school, a church's wifi, a mobile carrier's shared address) can run out for later joiners; the answer is a higher `per_address` by pull request or a grant from the mint page. The address is read from the last `X-Forwarded-For` entry, which holds while Render is the only proxy.

## 2026-10-04 — Go Deeper S12: the pilot runs for named audiences (ruled by Mark)

Mark asked to close the pilot to general visitors while keeping it open for pastors and church historians, whose feedback is critical, and approved the Pilot Words Draft with an Audiences section. Change order to the pilot as first built (one open switch, one cap).

- **Operations file:** `pilot` holds `pack_usd`, one shared `pilot_end_date` and `audiences`. Each audience (shipped: `general`, `pastors`, `historians`) has its own `pilot_open` (all ship `false`), `pilot_cap`, `per_address` and `public`. Defaults chosen by the build thread, for Mark to set: general 50, pastors 25, historians 25, 2 per address, ending 31 December 2026. Closing the pilot to the public is `pilot_open: false` on `general`, by pull request.
- **A private audience is joined only by a secret key.** `general` is public and is joined by its name. `pastors` and `historians` are not: their names are in the public operations file and easy to guess, so a request must carry a link key kept in the server's environment (`CIC_DEEPER_PILOT_LINKS`, a JSON object of key to audience; 16 to 64 letters, digits, hyphens or underscores; never in the repository). The request is `{"link": "<key or public name>"}`. A key is compared in constant time. A private audience's bare name, an unknown key, a closed audience and a request with no link all answer 404 alike, so a link found early shows nothing and nothing says which audiences exist. With no keys set, no private audience can be joined.
- **Found by Opus review:** the first version named the audience in the request and called such links unlisted; they were not secret.
- **Counts are kept apart.** Each audience has its own total given (one number that outlives the address rows) and its own count per address; the address is hashed with the audience name, never the key, so changing a key does not refill anyone. The old single pilot total is dropped when the file opens.
- **Worst case for one address, stated:** three audiences times two packs is six packs, 6,600 tokens, counted as $42 of gifts toward the door. Each audience's cap bounds the total.
- **Not verified, stated:** the app cannot check who a visitor is, and there are no accounts. A private link key can be forwarded; its audience's cap bounds that. Question 1 of the questionnaire still asks people to describe themselves, so results by audience come from the link used and what people say. To end a leaked link, remove or replace its key in the environment.
- **Dashboard:** the pilot tile shows given against cap for each audience, open or closed, whether a private audience has a link key set, and the pilot's end date.

## 2026-10-04 — Go Deeper S12: the join button, on the site and in the app (words approved by Mark)

Mark approved the Pilot Words Draft and asked for the join button. The words below are the approved ones; two lines are new and are flagged.

- **The site:** `pilot.html`, unlisted, `noindex`, linked from nowhere. It shows the offer ("Join the pilot… one free pack: 1,100 tokens, about ten conversations… a short questionnaire after the end date… Places are limited.") and a "Get my free pack" link. The link carries the audience's public name or a private audience's secret key (`pilot.html?for=<key>`; no query means general), and the page takes the key out of the address as soon as it loads, sets no-referrer, and loads no analytics. The one end date shown is the pilot's, and the figures are tested against the operations file. Until `pilot: true` is set in `assets/go-deeper-config.js`, the page shows nothing at all, so a link found early is an empty page.
- **The press:** the link opens the app with the link key in the address fragment (`#cic-pilot=<key>`). The press on the site is the press: the app clears the fragment at once and asks its own server once. The fragment is never sent to a server, and the site's page makes no request at all. A link preview or email scanner that opens the site page mints nothing; one that runs the app's script from the link could, and the cap and the per-address count bound that.
- **In the app:** the code is saved like any other, a marker is kept so a browser that has joined is never offered the pack again ("You have joined the pilot. Your pack is in this browser."), and the request carries no cookie and no referrer. The panel says "Your free pack is ready", the token and conversation counts from the server, and "Start a conversation". Full, ended and "this connection has taken its share" use the approved lines, the last with a link to the feedback form. A closed or unnamed audience shows nothing.
- **The server** now also returns how many conversations the pack holds, worked out from the operations file, so the app never learns a cost.
- **Two new lines, for Mark to approve or reword:** "Getting your free pack." while the request runs, and "We couldn't get your pack. Try again from the pilot page." when it cannot be reached.
- **To open the pilot:** three switches, in order: set the audience's `pilot_open` to true in the operations file (and, for a private audience, its key in `CIC_DEEPER_PILOT_LINKS`), set `pilot: true` in the site's config, and have the app built with the module on. The pastors and historians links are `pilot.html?for=<their secret key>`; Cloudflare's own logs see that address, so treat a key as a password for one audience and replace it if it leaks.
- **Not built yet:** the pilot panel with its questionnaire button and "I'm finished", the pilot group id, the questions page, and the Tally questionnaire (another thread). The group id still needs the Opus attack before it ships.
- **Opus review of the join button, taken:** the site page and the app both take the key out of the address before anything else can return, including when the pilot or the module is off; the panel's group is labelled neutrally; the runbook says to send only the site link, never the app address. **Stated, not changed:** a code the server made but the app could not save (a dropped connection on the reply, or storage that refuses it) is not shown and uses one of the address's places; the second place and the "Try again" line are the recovery, and showing the code would need a new line of words from Mark.

## 2026-10-05 — Go Deeper: the pilot's address-limit line no longer links a form (pre-turn-on item 9, words approved by Mark)

The line shown when a connection has taken the free packs the pilot allows ended "If that seems wrong, tell us through the feedback form", linking the old feedback page, which asks for a name and an email. The pilot's survey holds no identifying field, and it does not exist yet. Mark approved dropping the link and the sentence: the line now reads "This connection has already taken the free packs the pilot allows." The app's link helper and the unused origin constant are removed; the survey link can be added back when the survey exists. The site's footer "Feedback" link to the old page is a separate item and is not changed here.

## 2026-10-05 — Go Deeper: the app's build switches reach the Docker build

Found while walking the staging turn-on with Mark: the runbook says to build the app with `VITE_DEEPER_ENABLED=on`, but the Dockerfile's frontend stage declared no such argument, so a Render service had no way to turn the panel on. The Dockerfile now declares `VITE_DEEPER_ENABLED` and `VITE_DEEPER_SITE_ORIGIN` as build arguments (both empty by default, so an unset service builds the module dark) and exports them before the frontend build. A test pins both. Render is expected to pass a service's environment variables to a Docker build as the arguments the Dockerfile declares; that is not yet proved. The build now prints the value it received into its log (`Go Deeper app build: VITE_DEEPER_ENABLED='...'`), so the first staging build with the variable set shows it, and the panel appears or it does not. The two switches are public: they end up in the built JavaScript, so no ARG named after a secret is ever declared. The runbook's settings table now says where each is set.

## 2026-10-05 — Go Deeper: a working purchase leaves no log line (pre-turn-on item 8)

The accounts review found that the webhook's "webhook handled" line carried a timestamp beside the "session created" lines in the same log stream. No line held a code, a payment id or a session id together, but a purchase and a sitting a few seconds apart could be read as related. The webhook now logs an outcome only when it is not routine: a minted code, a replay, a counted gift and a full refund leave no line, and a stray or failed event still does. The day's counts live in the meter's tallies and the dashboard, not in the log. The meter's own "minted" and "voided" lines, which carried the same moments on the same logger, are now debug-level, so nothing at INFO or above records a purchase or a full refund. A purchase that fails still leaves one timestamped error line, by design: it is the line an operator needs. A test pins both halves: two deliveries of one purchase and a full refund leave no line at INFO or above; an event for a link that is not ours leaves exactly one.

## 2026-10-05 — Go Deeper: a funds note is one of a fixed list (pre-turn-on item 7)

The admin's funds route took a free-text note of up to 200 characters, so a donor's name typed there would have been stored in the meter's file. A note is now one of a fixed list, in the meter and at the route: "cash gift", "check gift", "other gift" and "correction" for an adjustment made by hand, and "pilot grant" and "admin grant" written by the app for the grants it counts. Anything else is refused (422 at the route). Rows already written keep what they hold; nothing is rewritten. The words are internal to the admin page and are not shown to participants. Tests pin that every listed kind is accepted and that a typed name, a different case, an empty string and an over-long string are refused.

## 2026-10-05 — Go Deeper: the three draft close texts are replaced by one plain line (pre-turn-on item 6, words approved by Mark)

The Facilitator's close texts for the sitting cap, the Table cap and the daily cap were long drafts, marked "not yet approved", that explained the cost of a conversation and pointed at the support page. With the module off they are what a visitor sees at a cap. Mark approved replacing all three with the line the module already uses: "This is the Facilitator. This sitting has reached its limit for now. Nothing in it is lost." The three constants share that one line (`CAP_CLOSE_TEXT`), the draft docstrings are removed, and so is the stale "$2-5 an hour" discussion, which cited a rate the support page no longer shows. The functions keep their arguments so no caller changes, and with the module on the module's own line still replaces this one and the sitting stays open. The new line does not name the Representative, so the test that checked the cap named the Representative now checks the line. The other Table texts keep the draft marking they have.

## 2026-10-05 — Go Deeper: two stale runbook lines corrected (pre-turn-on item 5)

Two runbook lines said there is no way to hand-mint a code, which stopped being true with the admin mint page (S13). Both now say that free codes are made there and count as gifts, and that the first live proof of the purchase path is still a real smallest-pack purchase. A third line said the door "halves the free day"; the free allowance is a 30-day window, so it says "halving the free allowance". Nothing else in the runbook changes.

## 2026-10-05 — Change order: accounts for conversations and tokens (ruled by Mark)

System Hub decision 53.

A named change order on the 2026-09-03 lock "no accounts for this launch" and on
decision 19 as amended by decisions 26 and 29. It takes effect for the version
after the codes launch; nothing in the codes build, its rulings or its runbook
changes.

An account is optional, open to anyone at any time, and exists so a person can
keep a record of their conversations and their tokens from their first
conversation on. Free use without an account is unchanged.

Ruled:
- Sign-in is an emailed one-time code or link. No password exists.
- The account store keeps a scrambled value of the address under a server
  secret, never the address. We store no name or address of our own; what a
  person types is kept as they typed it. We cannot write
  to an account holder; a closure refund goes through Stripe.
- An account holds the codes that hold its tokens, the list of its
  conversations, and its allowance. Its free allowance is the visitor's
  allowance carried by the account while signed in: 550 tokens a month,
  refilling on the person's own day of the month (a day past a month's end
  uses that month's last day), never accumulating, spent before purchased
  tokens. Signed out, the cookie allowance applies.
- Saved conversations are kept until the person deletes them or the account
  has sat unused for two years. A delete control exists for each conversation
  and for the whole account. Anonymous conversations keep the ninety-day rule.
- A crisis turn is saved as it happened. Reopening a conversation that holds
  one shows the Facilitator's resources line first, every time.
- Thirteen and over. A parent confirms for anyone under eighteen. A
  professional confirms the policy before accounts open.
- Provisional, pending the treasurer and a professional: purchased tokens
  lapse after two years of inactivity and are not refundable except in a rare
  case the project lead approves. Nothing is stated at purchase until checked.
- Decision 19's three unjoinable stores stand for everyone without an account.
  For an account holder the account store is, by design, the join between
  tokens and conversations. The account store never holds a value the meter
  or Stripe also holds: a code is linked to an account only as a keyed
  scramble of its hash under CIC_ACCOUNTS_KEY, so joining an account to a
  person needs that secret as well as the payment id and Stripe. We store no
  name or address of our own; what a person types in a conversation is kept as
  they typed it. The privacy page states this in the same words.
  (Modification by Mark, 2026-10-05, after Opus's read of this change order.)
- Stripe's information stays with Stripe. The program keeps nothing Stripe
  holds about a buyer: no name, email, card, address or receipt detail. The
  webhook reads only the link, the paid status, the purchase reference, the
  amount and the currency. The account store never receives anything from
  Stripe; the sign-in address is the one the person types, used for one send
  and not kept. The payment id alone stays, under decision 29, for refunds.
  (Modification by Mark, 2026-10-05, after convergence.)
- Accounts ship dark behind CIC_ACCOUNTS_ENABLED. Off, the product is the
  codes product exactly.
- Order: codes launch first. Account slices start after the door's observe
  week. This record and the professional questions start now.

Professional questions added to the register: the Article 9 condition and
whether GDPR or UK GDPR applies; the age policy and the parent confirmation;
the two-year lapse against gift-card and unclaimed-property rules; the EU
withdrawal right at checkout.

Plan: Accounts Build Plan (artifact). Analysis: Go Deeper Accounts Review
(artifact). The Opus thread attacks the account store as a join before the
shelf slice merges.

A6 proofs added by these modifications: the account file's bytes hold no value that appears in a webhook payload; and the account file's bytes contain no meter code hash and no payment id. Both join the other named A6 proofs and are guarded the same way.

Pages: Go Deeper Accounts Review, `https://claude.ai/artifact/NTTKUrGeKJ73nYkcPNfhjJ`; Accounts Build Plan, `https://claude.ai/artifact/GHerMTQjcKNkLKM1GrvK83`.

**Questions for a professional, added to the register (none answered).** These sit beside the five registered on 2026-10-03.

6. Article 9: which condition covers a conversation that reveals religious or philosophical belief when saving is the account's purpose, and whether GDPR or UK GDPR reaches CiC at all.
7. Age: the policy of thirteen and over with a parent's confirmation under eighteen, and whether a one-time emailed confirmation to a parent address that is then not kept is enough.
8. The two-year lapse of purchased tokens, checked against the gift-card five-year floor, California's rules and unclaimed-property reporting (it extends questions 2 and 3). Nothing about expiry is stated at purchase until this is answered.
9. The EU withdrawal right at checkout for a digital purchase, and whether a waiver must be taken at the Stripe page.

## 2026-10-05 — Go Deeper: Render passes the app's build switches to the Docker build (proved on staging)

The entry above of the same date left this unproved. On staging the first build with `VITE_DEEPER_ENABLED` set to `on` printed `Go Deeper app build: VITE_DEEPER_ENABLED='on'` in its log, and the Go deeper button appeared inside a conversation in the staging app. Render does pass a service's environment variable to the Docker build as the argument the Dockerfile declares.

## 2026-10-05 — Accounts: the panel line, for A4's words list (Mark's words)

Mark's words for the line in the Go deeper panel that explains signing up, recorded here as the first entry on A4's words list. They are his words as given; A4's pull request still brings every participant-facing line to him, with the readability check, before it merges.

"Signing up allows you to keep your conversation and to purchase more conversations. The tokens are held by the account, not by a code in one browser. Codes stay for anyone without an account and for sponsors."

What the line settles: an account holder's tokens belong to the account and are not carried in one browser; a code remains the way anyone without an account holds tokens, and the way a sponsor hands tokens out. Nothing in the codes build changes.

## 2026-10-05 — Go Deeper T3b: a free visitor sees their free tokens left (pre-turn-on item 3, words approved by Mark)

Mark's 2026-10-04 ruling gave a free visitor a count of what they have left, as a code holder has. It was ruled and not built; the accounts review found the strip showed a count only for a code holder. This builds it, in Mark's wording A: "{n} free tokens left." (Chosen over a version with a refill sentence and one that said "this month", which would have been wrong: the window runs 30 days from a person's first use.)

**Engine.** The free allowance can now say what a visitor may still draw under the share in force: the window narrowed by the door's stage, less what is spent and held, never below zero. Admission keeps the share it used and, when a turn is over and no code was in use, reports that number: a response header (`X-Cic-Free-Left`) and a `free_left` field in the stream's final event. Neither is stored, and a visitor holding a code gets the code's balance as before and no free count. With the module off nothing is reported. The count is measured against what the door lets a visitor draw, not the whole window, so a halved window at a stage shows half.

**App.** The count is read from the header or the final event, held in memory only, and shown in the strip under the message box and in the Go deeper panel, in place of the code count when no code is held. It disappears once a code is held, and nothing shows with the module off.

**Not changed.** The count appears after a visitor's first reply, not before. When accounts arrive, a signed-in person's allowance is the account's (the accounts change order), and this line is where it will show.
