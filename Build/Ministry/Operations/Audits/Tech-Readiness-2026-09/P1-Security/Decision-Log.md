# P1-Security — Decision Log

Append-only. One entry per PR and per escalation, per `CLAUDE.md`'s "Track
gaps and exceptions explicitly" rule. Entries are numbered and never
renumbered; a merged entry's number is permanent.

---

**1. 2026-09-21 — Package launched.** Dispatched as one of three wave-1
packages in the tech-readiness program (see the launch brief). Scope:
OWASP ASVS 4.0 L1, OWASP LLM Top 10 (unbounded consumption / prompt
injection / sensitive-information disclosure), AWS least-privilege
identity. Read `CLAUDE.md`, `render.yaml`, `engine/api/README.md`,
`engine/api/app.py`, `engine/api/ratelimit.py`, `engine/api/config.py`,
`engine/provider/bedrock.py`, `Ministry/Operations/Standing/
CiC_Promotion_Runbook.md` first, per the brief's own instruction.

**2. 2026-09-21 — Coordination check: no touch needed on the
Conversation-Transparency-Engine's guarded files.** ~~That directory does
not exist in this repo~~ — **wrong when originally written, corrected
2026-09-21 after Mark flagged it.** `Ministry/Features/
Conversation-Transparency-Engine/` exists on `main` (`README.md`,
`Build-Plan.md`, `Adjusted-Design.md`, `Rulings-Pending.md`,
`Decision-Log.md`) and was already there at the commit this package's
own work is based on (`c9b09ea1`, confirmed via `git ls-tree -d
c9b09ea1 Ministry/Features/` — the directory is listed) — the original
`find Ministry/Features -maxdepth 1 -type d` search that produced the
"no match" claim was simply wrong; the directory was there to find. Not
a timing issue (it wasn't created by concurrent work after this check;
`git log` shows files at this path as far back as 2026-09-19, two days
before this session started) — this package's own search failed, and the
claim went into this log unverified a second time.

**What actually matters — re-checked properly this time — still holds:**
the coordination rule requires a Decision-Log entry there before *editing*
`engine/m1/gates.py`, `engine/m1/schemas.py`, `engine/m2/`, `engine/m4/`,
`records/`, or `cic-poc/frontend/src/components/VoiceTurnBody.tsx`, not
before reading them. `git diff c9b09ea1..origin/<branch> --stat -- <those
six paths>` returns empty for all four of this package's branches
(`p1-security/dependency-audit`, `p1-security/anon-visitor-cap`,
`p1-security/prompt-injection-probes`,
`p1-security/docs-asvs-iam-logging`) — checked directly, not inferred.
`engine/api/wiring.py` was read (not edited) to confirm session creation
never reaches `run_turn()`, and `engine/m4/crisis_resources.py` /
`engine/m4/turn.py` / `engine/m5/routing.py` were read (not edited) for
entry 9's safety-interaction analysis. No entry was owed in that
workstream's own Decision-Log because nothing in it was ever edited —
that conclusion is unchanged, but it now rests on an actual diff check
against a directory confirmed to exist, not on a search that missed it.

**3. 2026-09-21 — PR #376 (item 5, dependency audit).** `pip-audit` clean
on both files the production Dockerfile installs. `npm audit` found 8
findings, all in frontend devDependencies (vite's own toolchain), none
reaching the built `dist/` bundle. 6/8 fixed non-breaking. The remaining
2 (esbuild/vite, coupled) need a vite 5→8 major bump that
`@vitejs/plugin-react@4.7.0` doesn't yet officially support — waived
rather than forced in. **Waiver: ACCEPTED_OPEN, esbuild/vite
devDependency chain, owner Mark, dated 2026-09-21, revisit when
`@vitejs/plugin-react` certifies vite 8.**

**4. 2026-09-21 — PR #377 (item 3, anonymous visitor cap) — escalation
raised, not yet resolved.** Built `engine/api/anon_cap.py`: a signed,
HttpOnly-cookie visitor token with a daily session/turn cap, layered on
the existing per-IP limiter, flagged OFF by default
(`CIC_API_ANON_CAP_ENABLED`). Three mechanism options compared in the PR
body (signed cookie / client-token+header / pure-IP daily bucket);
Option A (signed cookie) is what's built, as the proposal, not a decided
default. **Escalation: Mark needs to pick a mechanism and confirm or
revise the proposed numbers (5 sessions/day, 150 turns/day) before
`CIC_API_ANON_CAP_ENABLED` is ever set to `"1"` anywhere.** Participant-
facing flow, so per `CLAUDE.md`'s own escalation table this isn't a
silent pick — the code is inert until that decision lands.

**5. 2026-09-21 — PR #378 (item 4, prompt-injection probes).** 40 probes
across 5 categories, `run_probes.py` runner. Live run against
`cic-engine-staging`: **not done** — this sandbox's egress allowlist
(`pypi.org`, `registry.npmjs.org`, `api.anthropic.com`, a handful of
others) does not include Render, confirmed directly and against a
general-internet control. Structural run against the local dev server
(fake client): 40/40 completed, proving the harness works and nothing
about real model behavior. Found and fixed one unrelated pre-existing
bug blocking even the structural run (`dev_server.py`'s
`_ReactiveFakeMessages.stream()` missing a `timeout=None` kwarg its
sibling method already had — drift from unrelated concurrent work on
`engine/m4`'s streaming call site). **Open item, not this package's to
close: the live run against staging needs to happen from a
network-reachable environment before item 4's real question (does the
model resist these 40 probes) has an answer.**

**6. 2026-09-21 — Item 6 finding, fixed in this package: admin endpoint
had no brute-force throttle.** `engine/api/ratelimit.py`'s existing
per-IP limiter covered `/api/session*` only; `/api/admin/pilot-summary`'s
Bearer-token check (`_authenticate_admin`, constant-time compare) had
zero rate limiting, so an attacker could attempt tokens at unlimited
rate. Added a third bucket (`ADMIN_LIMIT`, 10/min per IP) — small,
directly in this package's own scope (ASVS V2.2.1), fixed rather than
handed off. See `Report.md` item 6 for the larger findings (no
application-level encryption at rest; no retention/deletion mechanism
yet) that are **NOT** fixed here and are handed to Package 2 (Operations)
and Package 6 (Privacy) by name, per the brief's own instruction that
this package's item 6 scope is findings-plus-trivial-fixes only.

**7. 2026-09-21 — IAM policy handed to Mark, not applied.** Least-
privilege `bedrock:InvokeModel`/`InvokeModelWithResponseStream` policy
written (`iam-policy-cic-bedrock-prod.json`) plus runbook steps
(`IAM-Runbook.md`). The cross-region constituent-region list
(us-east-1/us-east-2/us-west-2) is stated as AWS's documented "US"
geography for `us.`-prefixed inference profiles, not independently
verified against the live account (no AWS access from this sandbox) —
runbook explicitly asks Mark to confirm with `aws bedrock
get-inference-profile` before applying. **Creating the IAM user/policy
in AWS and setting it in the Render dashboard is Mark's own account
action, not done here.**

**8. 2026-09-21 — Closing Opus adversarial review: 3 blocking, 8
should-fix, 5 nice-to-have findings, all triaged and addressed.** Run
against all four branches (checked out in an isolated worktree, diffed
against `main`, several findings empirically reproduced with a live
FastAPI TestClient rather than reasoned about). Full findings text is in
the review agent's own report (not duplicated here in full — this entry
is the disposition of each one). Headline: the review found this
package's own artifacts didn't do what they claimed in three places, all
now fixed:

- **BLOCKING, fixed (PR #377):** `anon_cap.py` minted a fresh, empty-
  bucket visitor token on every request, including ones the cap itself
  had just refused with a 429 — an attacker who deletes their cookie
  before each request harvested an unbounded supply of tokens without
  ever needing to succeed once, so the daily cap enforced nothing against
  a deliberate attacker. Fixed: minting only on the allowed path, seeded
  from the requesting IP's current count rather than zero (bounds the
  residual instead of eliminating it — accepted, documented tradeoff, see
  `mint_seeded_token`'s own docstring). Also fixed in the same commit:
  middleware registration order was backwards (daily-quota check ran
  before the cheap burst check, double-charging quota on requests the
  burst limiter would reject anyway), and the test suite's `TestClient`
  never actually round-tripped the (correctly) `Secure` cookie over its
  default `http://` base URL, so the cookie path had shipped unverified.
  Added 7 regression tests, 2 of them direct reproductions of the
  harvesting exploit and the double-charge bug.
- **BLOCKING, fixed (PR #379):** `iam-policy-cic-bedrock-prod.json`'s
  foundation-model ARNs carried `<AWS_ACCOUNT_ID>`, which Bedrock
  foundation-model ARNs don't have (they're AWS-owned, account-less
  resources). Applied as written, the policy would have authorized at
  the inference-profile layer and failed with `AccessDenied` at the
  actual model call — exactly the intermittent, region-dependent failure
  `IAM-Runbook.md`'s own step 8 warns about, for a reason its own
  troubleshooting hint wouldn't have found. Fixed the JSON and the
  runbook's incorrect "six places" instruction.
- **BLOCKING, fixed (PR #376):** the dependency-audit branch was the only
  one of the four not based on current `main` — its audit predated
  `main`'s own addition of `vitest`/`jsdom`/testing-library
  (`9321610b`), so none of those new devDependencies were ever actually
  audited. Merged `main` in and re-ran: the real current tree has 5
  findings including one CRITICAL (`GHSA-5xrq-8626-4rwp`). Unlike the
  original 2 waived findings, this round's `npm audit fix --force`
  verified fully clean end to end (build + `vitest run`, the mode CI
  uses) — took the full fix. `npm audit` now reports 0 vulnerabilities;
  the earlier ACCEPTED_OPEN waiver (entry 3, above) is superseded and no
  longer needed.

**SHOULD-FIX, all addressed:**
- `client_ip()` trusted the *first* X-Forwarded-For entry; a standard
  reverse proxy appends the real peer rather than replacing the header,
  so the first entry is attacker-controlled — bypassed every limiter in
  `ratelimit.py`, this package's own admin fix included, with one request
  header. Fixed: takes the last entry now (PR #379).
- `GET /transcript` and `/round-close-reasons` guess a session code
  through the identical 401 the message/continue POSTs use but were never
  in the rate limiter's path match — unlimited-rate credential guessing,
  same ASVS class as the admin-token finding this package already fixed,
  just the participant-facing instance of it. Fixed: both GETs now share
  the conversation-traffic bucket (PR #379).
- No bound anywhere on participant message length — unbounded input
  forwarded to Bedrock twice per turn, textbook OWASP LLM Top 10
  "unbounded consumption," and the ASVS checklist had marked the relevant
  item PASS on "typed" without checking "validated." Fixed: `Field(
  max_length=4000)` on `MessageRequest.text` (PR #379).
- `CIC_API_ADMIN_TOKEN` had no minimum length, which interacts
  multiplicatively with the admin rate limiter this package added (a
  limiter's job is making a weak token infeasible to brute-force in
  reasonable time — irrelevant against a token short enough to guess
  outright). Fixed: `Settings.from_env` refuses a set-but-under-32-char
  token (PR #379).
- The IAM runbook's "two identities, one policy" section claimed
  blast-radius containment between prod and staging credentials; two
  access keys under an identical policy give rotation and CloudTrail
  attribution, not containment (both can invoke the same models, region,
  account). Reworded to claim only what's actually true (PR #379).
- The probe hand-off command named `--world fix` (the synthetic fixture
  world, which must never be participant-reachable) — a live run against
  it would have completed and reported success while testing almost
  nothing the PB/SEAL/FRT categories actually name. Fixed the example and
  `run_probes.py`'s own usage docstring (PR #378).
- `Report.md`'s Done bar had two items checked off before they were true
  ("merged" for an unmerged PR, the review itself checked off before it
  ran). Fixed (this PR).
- A thread-continuation bug in `run_probes.py`: if a threaded probe's
  first session failed to create, later members of the same thread
  silently opened their own unrelated sessions instead of surfacing that
  the thread never happened as designed. Fixed (PR #378).

**NICE-TO-HAVE, addressed where cheap, logged where not:**
- `RESULTS.md`'s "20/8/8/6/9/9" summed to 60, not 40 (the correct
  8/8/6/9/9 was already right elsewhere in the same file) — fixed.
- `run_probes.py`'s docstring advertised a `--admin-token` flag that was
  never actually registered — removed.
- **ACCEPTED_OPEN, not built in this pass:** the 40-probe set is entirely
  direct-injection-via-participant-text; indirect injection via retrieved
  corpus content, and probes targeting the safety classifier itself
  (rather than talking a voice model out of an already-fired redirect),
  are both real, higher-value gaps this package didn't have the corpus-
  injection surface mapped well enough to test blind. Documented in
  `probes/RESULTS.md` as a named follow-up (a second, smaller probe set),
  owner: whoever picks up item 4's live run. Dated 2026-09-21.
- **FALSE ALARMS the review checked and confirmed fine, not touched:**
  the visitor cookie's `secure=True` flag (correct — Render always
  terminates TLS, and this only ever broke the test harness, which is
  where it was fixed); `bedrock:ListInferenceProfiles` with `Resource:
  "*"` (correct — it's an unscopable list action); the cross-region
  constituent-region claim in the IAM runbook (substantively correct AWS
  behavior); the admin endpoint's response body (no participant data);
  eleven separate ASVS PASS spot-checks; no credential leaks in any of
  the four diffs; no fail-open logic introduced anywhere.

All four PRs (#376, #377, #378, #379) carry a follow-up commit addressing
this review and are pushed. None are merged. Mark's decision on item 3's
cap mechanism/numbers (entry 4) remains the one open item this session
cannot close on its own.

**9. 2026-09-21 — Mark's follow-up round: three items, all addressed.**
He caught three things after reviewing the package: PR #376 was red on
its own tip commit (Docker build + Frontend tests CI jobs both failing),
he asked for an analysis of how `anon_cap`'s turn-level 429 interacts
with the Facilitator crisis redirect, and he caught this log's own
entry 2 making a false claim about `Ministry/Features/
Conversation-Transparency-Engine/` not existing. All three below.

**9a — PR #376 CI red, fixed.** Root cause: entry 8's dependency
re-audit was verified with `npm install`/`npm audit fix --force`, which
silently overrides an unresolved peer-dependency conflict — `npm ci`
(what both `engine/Dockerfile` line 46 and `.github/workflows/ci.yml`'s
"Frontend tests" job actually run) does not, and failed immediately:
`@vitejs/plugin-react@4.7.0`'s peer range never included vite 8. Pulled
both jobs' actual failure logs from the PR's check runs to confirm
before touching anything. Fixed by bumping `@vitejs/plugin-react` to
`^6.1.1` (declares `vite: "^8.0.0"` as its own peer — the certified
pairing that didn't exist when the original audit ran), regenerated the
lockfile with a plain `npm install`, then verified with the exact
sequence CI/Docker run: `rm -rf node_modules && npm ci` (clean, 0
vulnerabilities, no ERESOLVE — run twice), `npm run build`, `npm test`
(9/9). Node engine check done explicitly this time:
`@vitejs/plugin-react@6.x` needs `^20.19.0 || >=22.12.0`; CI's Frontend
tests job runs Node 20.20.2 (satisfies it), Dockerfile's frontend-build
stage is `node:20-slim` (resolves to a current 20.x patch, also
satisfies it). PR description and comment corrected to state plainly
that the previous "verified clean" claim was true but incomplete — it
never ran the one command that actually gates CI.

**9b — anon-cap 429 vs. crisis redirect, analyzed.** Full trace and
proposed rule: `Anon-Cap-Safety-Interaction.md` (on
`p1-security/anon-visitor-cap`, PR #377 — that's where the code this
analyzes actually lives). Summary: `anon_cap`'s turn-level 429 fires as
HTTP middleware, before `call_next()` runs, which is before the safety
classification call, `engine.m5.routing.route()`, or
`crisis_resources.append_crisis_resources_turn()` ever execute — a
capped turn is never classified, never routed, never redirected, and
never stored. `engine/m4/turn.py`'s own `SESSION_TURN_CAP` already
solved the identical problem (its own comment: "THE CAP OVERRIDES
EVERYTHING EXCEPT A REAL CRISIS... checked after routing") by checking
its cap *after* the gate call, with a `not is_acute_crisis` guard that
structurally cannot fire on a real crisis turn. `anon_cap` does the
opposite — cap-checks before any classification exists to consult.
Proposed: three options (A, move the turn-cap check to the same
post-gate/pre-generation point `SESSION_TURN_CAP` already uses, mirroring
its exemption — recommended; B, drop the standalone turn cap and rely on
session-cap × `SESSION_TURN_CAP`'s existing bound instead — simpler
fallback; C, a copy-only fix that doesn't actually close the gap — listed,
not recommended alone). **No safety code touched** —
`engine/m4/crisis_resources.py` and `engine/m5/routing.py` were read
only, confirmed via diff (see entry 2's correction above). This is now
part of the same open escalation as item 3's mechanism/numbers decision
(entry 4) — it changes what "capped" means, not just the thresholds, so
it needs deciding in the same conversation, not after the fact.

**9c — Entry 2 corrected.** See the strikethrough and correction inline
in entry 2, above. Root issue: an unverified negative claim ("does not
exist... searched in full, no match") went into an append-only log
without the search actually being re-checked against the real
git-tracked contents at the commit this package's own work was based
on. Re-checked properly this time (`git ls-tree -d c9b09ea1
Ministry/Features/` — lists the directory; `git diff c9b09ea1..origin/
<branch> --stat -- <the six guarded paths>` — empty for all four
branches). The substantive conclusion (nothing in this package edited
any guarded file, so no entry was owed in that workstream's own log)
was and remains correct — it just wasn't actually verified the first
time it was written down.

**10. 2026-10-02 — Item 9b ruled: a crisis message at the daily cap continues to the Facilitator.** Mark's ruling (pilot readiness thread): "if there is a crisis comment we continue to the facilitator." This is Option A from 9b. The daily turn cap no longer rejects `/message` in the middleware. `anon_cap` marks an over-limit message (`request.state.daily_turn_cap_reached`) and lets it through uncounted. `engine.m4.turn.run_turn` and `engine.m4.round.open_table_round` then check it at the same post-gate, pre-voice point as `SESSION_TURN_CAP`, with the same `not is_acute_crisis` exemption. A real crisis gets the Track A redirect. Any other over-limit message gets a fixed Facilitator close and the session closes, so each session spends at most one extra gate pass after the cap. `/continue` carries no participant text and keeps its 429. Not changed: the daily session cap still refuses session creation before any message exists. Under the coming pay-as-you-go module, whether a capped visitor can open a session to reach the Facilitator is a question for that design. The close wording reuses the live 429 text and carries the same DRAFT status as the other Facilitator cap texts.

**11. 2026-10-02 — Safety gate fails closed to the Facilitator check-in.** Mark's ruling (pilot readiness thread), on the safety check: "it shouldn't time out". He approved this design ("sure"):
- The safety call (`engine.m5.live_calls.call_safety`) waits up to 15 s per attempt and retries once. The reader keeps its 4 s.
- If safety still fails, `engine.m5.failure.resolve_gate` routes to `check_in_turn`, whatever the reader said, so the voice never answers a message no one has read for risk.

This replaces Artifact-4 §4's earlier fail-open rule. That rule depended on an async re-classification that was never built: `needs_async_safety_reclassification` had no reader. The flag is removed, and Artifact-4 §4 is updated to the new rule. Before this change, the SDK's own default of 2 retries applied at 4 s each, so the old worst case was about 12 s before failing open. The classifier prompt, model and schema are unchanged, so the live safety script does not need a re-run under Artifact-4 §5.

**12. 2026-10-02 — Entry 11's timing change reverted; the fail-closed rule stays.** Mark's ruling: the 15 s timeout and the extra retry were over-protection for a rare case. When Bedrock is fully down, the voice call fails too, so the safety rule only changes the outcome in a partial outage. The safety call is back to the original 4 s timeout, with the SDK's default retries. The check-in on safety failure from entry 11 stays. Artifact-4 §4 and Artifact-6 are updated to match.

**13. 2026-10-03 — Record gap found by the Go Deeper build: the daily cap is on, and no entry says so.** Entry 4 says `CIC_API_ANON_CAP_ENABLED` is never to be set to `"1"` until Mark picks the numbers. The cap has been on since 2026-09-28 (commit `67a70338`, which edits `render.yaml` and `engine/api/anon_cap.py`), and this log never recorded the change. The Go Deeper module does not touch the flag. Owner action: confirm the numbers now live in `render.yaml` and record the ruling here.
