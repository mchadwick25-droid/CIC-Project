# Accounts A1a — Opus review of the redesigned slice (ordered by the cap ruling), 2026-10-22

## Scope

- Branch `claude/amazing-johnson-ayi2y3`, commit `0df50a2aeb25fe281483e10977190af50e8afe64`, working tree clean.
- Read as the code stands: `engine/accounts/{keys,store,service,config}.py`, `engine/api/accounts_routes.py`, the accounts lines in `engine/api/app.py` and `engine/api/required_secrets.py`, `engine/accounts/tests/*`, `engine/api/tests/test_accounts_*.py`.
- Design sources: Go Deeper Decision Log, the 2026-10-05 change order (decision 53), the 2026-10-22 change order (rulings 1–22 and the safety minimum), rulings 23–24, and the A1a entries through "redesigned at the root".
- Method: reading, plus two throwaway probe scripts run against the service in a scratch directory (no repo edits, no model calls, no spend).

## Verdict on the root cause

The redesign removes the root cause it names. Proof state is no longer keyed by the address. A challenge is found only by its 128-bit random id. Its code MAC is bound to that id. `_check` enforces kind, and enforces account for step-up and change and address for sign-in. A stranger's recovery or change to the same address can no longer replace, block or stand in for another account's challenge. I found no remaining path where one account's proof state touches another's.

One Blocking defect remains. It has a **different root cause**: a global send budget that anyone can fill also gates the owner's only defence against a pending recovery. It belongs to the same family (shared state that one party can use up against another), but it is not keyed by address and is not proof state. The redesign did not create it. The round-three entry recorded the global "other" pause as an accepted denial. It did not see that the pause also turns the seven-day wait into a takeover.

## Findings

### Blocking

**B1. A thief holding a recovery code can stop the owner from cancelling the recovery, and so take over the account.**
`engine/accounts/service.py:171-176` (`_admit` counts step-up against `send_global_other`), `:347-354` (`step_up_start`), `:414-419` (`cancel_recovery` needs `session.stepped_up`).

- Scenario (reproduced with a probe script against this commit): a thief has the victim's recovery code. Ruling 11 offers it "to download or print", and ruling 18 builds the seven-day wait for exactly this case. The thief runs `recover_start` and `recover_finish` to their own address, and a pending change is written. The thief then opens six free accounts on six IPv4 addresses (one /24 is enough). At the start of every hour each account sends 20 step-up starts to its own address. That fills the 100-per-hour `send_global_other` budget within seconds. For the rest of each hour the victim's `step_up_start` returns `paused`. The probe saw this for 48 of 48 hours tested. The victim sees the banner but cannot step up, so cannot cancel, make a new recovery code or change address. After seven days the thief signs in at their address, `_apply_pending` moves the account, every victim session ends, and the thief receives a fresh recovery code. The project holds no address, so it cannot warn the victim.
- Cost to the thief: six sign-ins, then about 100 step-up mails an hour to their own inboxes for a week. A cron job does it. The same action also pauses step-up, change and recovery for every other user all week.
- Proposed fix (root, not a patch): the owner's proof of their own address must never share a budget that other parties can fill. Two parts:
  - Take step-up out of the global "other" budget. Its mail goes only to the account's own address, and the per-account and per-network counters already bound it. If a global ceiling on step-up mail is wanted for cost, give step-up its own budget, and never apply it to an account with a pending recovery.
  - Let cancelling a pending recovery accept a fresh sign-in as proof. A sign-in in the last ten minutes proves the address just as a step-up does. Then the owner's defence depends only on the sign-in path, which the thief cannot reach for that address without the owner's inbox.
  - Add a named proof: with the global "other" budget full, an owner with a pending recovery can still cancel it.
  - If this belongs to Mark as a design change (the waiting-period guarantee of ruling 18), it is a change order, not a quiet edit.

### Substantial

**S1. Change and recovery starts still differ in timing and in failure between a taken and a free address, once a mailer is wired.**
`engine/accounts/service.py:191-197` (mail sent inline only for a free address; `send_failed` only reachable for a free one), `engine/api/accounts_routes.py:173-176` and `:39-40` (0.3-second floor).

- Scenario: a free account, stepped up, calls `/address/start` with a target address. A taken address answers at the 0.3-second floor, because no mail is sent. A free address answers at the floor or at the provider's latency, whichever is longer. A typical HTTP mail API takes 150–800 ms. Repeated probes, within the per-address budget of 6 per 15 minutes, separate the two distributions and give an existence oracle on an address. The safety minimum names this directly: "the same reply and similar timing whether or not an account exists". The same holds for `/recovery/start`. A provider that rejects a suppressed recipient synchronously (several do, for example on a previously bounced address) gives a 503 `send_failed` for a free address and a 200 for a taken one.
- This is latent today: `build_runtime` refuses to start without a mailer (`accounts_routes.py:84-87`), and none is wired. It becomes live the moment the mail slice lands, and no test would catch it: the route tests set `start_floor_seconds=0.0` and the fake mailer returns instantly (`engine/api/tests/test_accounts_routes.py:34`).
- Proposed fix: take the send off the request path for every kind. Queue the send and reply at once, so the reply never waits on or learns from the provider. A send that fails then burns the challenge silently, and the person asks for a new code. Add a test with a slow and a failing fake mailer that asserts identical status and body, and timing within a tolerance, for taken and free targets.

### Minor

**M1. A cross-account `INSERT OR REPLACE` silently deletes another account's pending change.** `engine/accounts/store.py:224-233`. SQLite's REPLACE resolves the `UNIQUE new_address_hash` conflict by deleting the other row, so the `IntegrityError` branch never runs and the method never returns False. This was confirmed with a probe: putting B's pending on A's address returned True and A's pending was gone. Today only `recover_finish`'s separate `other` check (`service.py:404-406`) prevents it, and that check and the write are not one transaction. The harm is negligible: both recoveries need codes from the same inbox, so one person controls both. But the store's stated contract is false. Fix: `INSERT ... ON CONFLICT(account_id) DO UPDATE`, so a cross-account clash raises. Claim the recovery code and write the pending in one durable transaction (today the code is deleted at `:407` before the write at `:410`).

**M2. The recovery-code claim is not bound to the code the challenge was opened with.** `service.py:407` deletes whatever code the account holds. If the owner regenerates a code in the gap between a thief's `recover_start` lookup and its `put_challenge`, the challenge survives the regeneration's `delete_challenges_of`, and finishing it deletes the owner's new code. The window is one request's duration and cannot be timed by the thief, so this is minor. Fix: store the recovery code's hash on the recover challenge and claim with `DELETE ... WHERE account_id = ? AND code_hash = ?`.

**M3. A new recovery code does not end a recovery already proved.** `make_recovery_code` (`service.py:372-378`) says it "ends any recovery already started with it", but it removes only open challenges, not a written pending change. The banner and `cancel_recovery` remain, so the owner is not left without a path (subject to B1). A person who regenerates expecting the thief to be shut out will be wrong. Either cancel the pending there too, or correct the claim and the matching test name (`test_recovery.py:29` covers only an unproved challenge).

**M4. Per-address change and recovery counters are still shared across accounts.** `service.py:163-168`. A stranger who knows the address a victim intends to recover to can fill `recover|X` (20 a day, from their own free account's recovery code) and block that recovery for the UTC day. The stranger cannot touch the victim's challenge, and a plus-tagged or other address works around it, so the harm is small. This is the one deliberately kept address-keyed scope. The design entry argues it carries no existence signal, which holds. It is a denial, not a takeover.

**M5. One inbox can receive up to 50 codes a day from strangers.** Sign-in, change and recovery each have their own per-address day budget (10 + 20 + 20, `service.py:50-53`, `:157-168`). The round-three fix capped change and recovery per inbox, but the kinds are not summed. Fix if wanted: one per-address daily mail counter across kinds, counted before the taken-or-free check, as now.

**M6. A key rotation during the seven-day wait strands a pending change.** The pending change is stored under the then-current hash (`service.py:410`), but looked up only by the current hash (`:245`, `:395`, `:450`). It never applies, and the banner stays until the owner cancels. The case is rare. Fix: look up pending by `candidate_hashes`.

**M7. Known and recorded, restated only for completeness.** Anyone can fill an address's sign-in budget or the global sign-in budget (a denial the safety minimum accepts). A deleted account on an older key leaves its current-key sign-in challenge for up to ten minutes and its counters for up to a day. Expired challenges sit up to an hour until the hourly purge, though `take_try` deletes them on touch.

## Checked and found sound

- Challenge ids come from `secrets.token_urlsafe(16)` (128 bits). The MAC binds id and code under the session key with domain separation. A challenge id cannot be reused across kinds (kind check), accounts (step-up and change), or addresses (sign-in). Recovery is found by id alone, which is correct because the id holder is the requester.
- A start to a taken address opens a real challenge whose code is never sent. No mail goes out, and status, body, headers and every counter are the same as for a free address. Only S1's timing and failure path differ. The redesign holds for status, shape and counters.
- `take_try` is one immediate transaction: it counts, then returns the row, and an expired row or one at the limit is deleted. Concurrent guesses cannot beat five tries. `burn_challenge_if` (delete where id and mac match) gives exactly one winner among concurrent right codes. The process is single-worker uvicorn (`engine/Dockerfile:136`), and the cross-process case rests on SQLite immediate transactions, as recorded.
- The round-three cross-account recovery collision is gone. Two recoveries to the same address hold separate challenges, and the other's mail proves nothing (`test_recovery.py:131`).
- Sign-in with a verified pending: an unexpired pending returns `recovery_waiting` without spending the challenge. An expired one spends first, then applies. If the address was taken during the wait, nothing moves and no one's code is replaced. A successful move ends all sessions and issues a new recovery code once.
- Sessions: a 256-bit token, an HMAC-signed `__Host-` cookie, HTTP-only, SameSite Lax, idle and absolute limits, deleted when the account is gone. "Sign out everywhere", an address change (other sessions) and an applied recovery (all sessions) end sessions as ruled.
- Deletion: the account, its recovery code and its pending change go in one transaction, plus a ledger entry of a hash of the random id. Sessions, the account's challenges, and challenges and counters under its address hash are removed. `reapply_ledger` runs at start-up.
- The route guard requires the custom header and a JSON content type, and checks Origin against scheme and host. With `--proxy-headers --forwarded-allow-ips='*'` the scheme is https behind Render, so legitimate posts pass. Body field lengths are capped. Wrong codes get a fixed delay.
- Flag off: no route and no file. Flag on: start-up refuses without keys of 32+ characters, with equal keys, or without a mailer. `required_secrets.py` names both keys.
- On disk: no address, no code, and no time finer than a day in the durable file. Ephemeral rows hold only keyed hashes. `secure_delete` is on.

## Tests that pass without proving their claim

- `test_recovery_and_address_change_replies_and_limits_are_the_same_for_a_taken_and_a_free_address` and `test_start_reply_is_the_same_whether_or_not_an_account_exists` cannot see timing or a failing send. The floor is 0 and the mailer is instant (S1).
- `test_a_new_recovery_code_replaces_the_old_one_and_ends_a_recovery_begun_with_it` covers only an unproved challenge (M3).
- `test_many_accounts_cannot_send_more_than_a_few_codes_to_one_inbox` checks one kind within 15 minutes, not the daily total across kinds (M5).
- No test covers a full global budget against an owner who needs to cancel (B1).

## Could not verify

- Real mail-provider latency and synchronous failure modes (no provider is chosen), so S1's size is estimated.
- Behaviour under several processes or Render instances, beyond SQLite's locking.
- Render request-log retention and whether disk snapshots copy the ephemeral file (already open in the Decision Log).
- I did not run the repository's test suite: pytest is not installed in this environment. The two probe scripts ran with a stub.
