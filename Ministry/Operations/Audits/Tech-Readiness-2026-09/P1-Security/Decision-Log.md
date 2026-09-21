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
Conversation-Transparency-Engine's guarded files.** The brief named
`engine/m1/gates.py`, `engine/m1/schemas.py`, `engine/m2/`, `engine/m4/`,
`records/`, and `cic-poc/frontend/src/components/VoiceTurnBody.tsx` as
requiring a Decision-Log entry in `Ministry/Features/
Conversation-Transparency-Engine/Decision-Log.md` before any edit. That
directory does not exist in this repo as of this audit — searched
`Ministry/Features/` in full, no match. Nothing in this package touched
any of the named files anyway (confirmed by reading `engine/api/wiring.py`:
session creation calls `_load_world`/`open_session`, never `run_turn()` —
it is not the turn path the brief was protecting), so this is a
non-blocking observation, not a finding this package can resolve. Flagged
here for whoever owns that workstream's naming.

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
