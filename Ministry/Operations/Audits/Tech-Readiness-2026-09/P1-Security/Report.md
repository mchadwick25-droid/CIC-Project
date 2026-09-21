# Tech-Readiness Package 1 — Security & Abuse Hardening — Report

2026-09-21. Standards: OWASP ASVS 4.0 Level 1; OWASP Top 10 for LLM
Applications 2025 (unbounded consumption, prompt injection,
sensitive-information disclosure); AWS Well-Architected Security pillar
(least-privilege identity). This package covers `engine/api/` — the
FastAPI service on Render, backed by AWS Bedrock, SQLite on a Render
disk, serving `cic-poc/frontend`'s built static assets same-origin.
Participant safety (the Facilitator crisis mechanism) is explicitly out
of scope — see `CLAUDE.md`'s own "Safety comes first" section and
`engine/m4/crisis_resources.py`, both untouched here.

Every PR referenced below is open against `main`, not merged, not pushed
to `live`. Full narrative and rationale for every decision is in
`Decision-Log.md`, entries 1–8.

---

## Item 1 — OWASP ASVS 4.0 Level 1 checklist

Evidence gathered by a read-only research pass over `engine/api/`,
`engine/m4/`, `engine/m8/`, `render.yaml`, and
`reference/Redesign-Spec/Artifact-6-Operations.md`. Every PASS below cites
a file:line; every FAIL states the gap and its citation. No item is
marked PASS on assertion alone.

### V1 — Architecture, Design and Threat Modeling
- **PASS (partial)** — a real threat model exists:
  `reference/Redesign-Spec/Artifact-6-Operations.md` §2 (lines 18–33):
  assets, and a threat/control table covering session-code guessing,
  transcript exfiltration, prompt injection, spend attacks, availability
  attacks.
- **FAIL (drift)** — that same document's deployment section (lines
  35–45) describes RDS Postgres + CloudFront + KMS-encrypted storage; the
  actually-deployed topology (`render.yaml` lines 87–199) is SQLite on a
  Render disk with no CDN. Several of the threat model's own stated
  controls are aspirational, not implemented. The threat model needs a
  refresh pass to describe what's actually running, or it stops being a
  reliable audit input.
- **Correction, closing adversarial review:** the original draft of this
  item cited the threat model's "5/min + 20/day per-IP attempt limits"
  (Artifact-6-Operations.md line 24) as a general volume-limit spec the
  shipped limiter under-delivers on, and drew the wrong conclusion from
  it. That line is the **session-code guessing** row of the threat
  model's own table — i.e. an *authentication anti-automation* control,
  not a spend-volume one. Read correctly, it pointed at a real gap this
  package had otherwise missed: `GET /transcript` and
  `/round-close-reasons` both guess a session code through the identical
  401 the message/continue POSTs use, and neither was in
  `engine/api/ratelimit.py`'s own path match before this PR — an
  unlimited-rate credential-guessing surface. **Fixed**: both GETs now
  share the conversation-traffic bucket (see item 6 below). The separate,
  still-open question — no *daily* ceiling on spend-bearing traffic at
  all — is item 3's own subject, not this citation's, and remains not yet
  decided.

### V2 — Authentication
- **PASS** — session code: 128-bit CSPRNG (`engine/m4/session_code.py`
  line 25, `secrets.token_bytes(16)`), hashed not plaintext (`hash_code`,
  same file lines 34–36; only the hash is ever stored —
  `engine/api/wiring.py`'s `create_session`), constant-time compared
  (`codes_match`, same file lines 39–42, `hmac.compare_digest`), header
  only, never URL (`engine/api/app.py` `_extract_code`, lines 161–165 in
  the pre-audit line numbering — grep `_AUTH_PREFIX` for the current
  location). Unknown-session and wrong-code return the identical 401
  (`_authenticate`).
- **PASS** — admin token: separate `Bearer` credential, constant-time
  compare (`_authenticate_admin`, `hmac.compare_digest`), unconfigured/
  missing/wrong all return the identical 404 (never confirms the route
  exists to an unauthorized caller).
- **FAIL, fixed in this package** — the admin token had no rate limiting
  at all (ASVS V2.2.1, anti-automation on authentication): zero cost to
  an attacker trying tokens at unlimited rate. Fixed — see item 6 below
  and `engine/api/ratelimit.py`'s new `ADMIN_LIMIT` bucket (this PR).
- **FAIL, fixed after the closing adversarial review** — no minimum-
  entropy/format validation on `CIC_API_ADMIN_TOKEN` at load time
  (`engine/api/config.py`, `Settings.from_env`) — an operator could set a
  short, low-entropy token and the app would accept it silently. Flagged
  by the review as interacting multiplicatively with the admin rate
  limiter above (a limiter's whole point is making a weak token
  infeasible to brute-force in reasonable time — irrelevant against a
  token short enough to guess outright). Fixed: `Settings.from_env` now
  raises `WeakAdminTokenError` on a set-but-under-32-char token.
  is a reasonable follow-up.

### V3 — Session Management
- **PASS** — session_id (routing key) vs. session_code (the actual
  capability) split avoids fixation; the code is server-generated at
  creation, never client-supplied.
- **PASS** — idle-close lifecycle: `engine/m4/idle_close.py`,
  `IDLE_AFTER = timedelta(days=7)`, daily background sweep, explicitly
  reversible (a participant resuming with their code is never refused —
  this is reporting-only by design, not an access gate).
- **PASS** — hard session cap: `SESSION_TURN_CAP = 10`
  (`engine/m4/turn.py`), a real spend/abuse control, not just a rate
  limit.
- **NOT-APPLICABLE (architectural choice, not a gap)** — no logout
  endpoint exists; the capability-token design (possession-of-code) has
  no login/logout concept. Worth a plain note for anyone auditing this
  fresh: a leaked code has no revocation path short of the 7-day idle
  window or the 10-turn cap.

### V4 — Access Control
- **PASS** — full route enumeration (`engine/api/app.py`): every route
  touching session- or operator-specific data calls the correct
  authenticator (`_authenticate` or `_authenticate_admin`); `/health`,
  `/api/worlds`, `POST /api/session` (deliberately — it's the credential-
  issuance endpoint, protected by rate limiting instead), and the static
  SPA catch-all are the only unauthenticated routes, all by design and
  all free of session/operator data.

### V5 — Validation, Sanitization and Encoding
- **Correction, closing adversarial review — was PASS, now FAIL-then-fixed:**
  the original draft marked this PASS on "every request body is a typed
  Pydantic model." Typed is not validated, and the review caught the real
  gap this glossed over: `MessageRequest.text` (`engine/api/app.py`) had
  **no length bound anywhere in the request path** — not this model, not
  `engine/m4/turn.py`, not the Dockerfile. Every participant message is
  forwarded to Bedrock twice per turn (the safety gate, then voice
  generation) and stored verbatim, at up to 40 messages/min per IP
  (`engine/api/ratelimit.py`'s own `CONVERSE_LIMIT`). Output was already
  bounded (`max_tokens` on the generation call); input wasn't — textbook
  OWASP LLM Top 10 "unbounded consumption," and cheaper for an attacker to
  reach than the session-creation path item 3 addresses. **Fixed**:
  `MessageRequest.text` now carries `Field(max_length=4000)`.
- **PASS** — zero raw string interpolation into SQL anywhere in
  `engine/m4/store.py` / `engine/m8/log_store.py`; every query uses `?`
  placeholders with bound values.
- **PASS** — zero `eval`/`exec`/`pickle`/`os.system` anywhere under
  `engine/`. The one `subprocess.check_output` call
  (`engine/m2/cli.py`, fixed-argument `git rev-parse`, no `shell=True`)
  is build-tooling, not reachable from any HTTP request path.
- **UNVERIFIED** — prompt-injection defenses inside `engine/m4/turn.py` /
  `engine/m5/routing.py` (does participant text ever get spliced into a
  directive/schema path, vs. staying pure data) were not independently
  traced line-by-line in this pass; only the threat model's own claim was
  read. See item 4 (the probe set) for the behavioral side of this same
  question — this checklist item and that probe set are answering
  related but different questions, and neither alone closes V5 for
  prompt injection specifically.

### V7 — Error Handling and Logging
- **PASS** — participant/voice text is never logged, by policy
  (`engine/api/app.py` module docstring) and by grep evidence across
  every `logger.*` call site in `engine/api/app.py`,
  `engine/m4/idle_close.py`, `engine/m7/scheduler.py` — session ids,
  world keys, turn numbers, timing, and a Bedrock error's own `str()`
  only, never request/response text.
- **PASS** — HTTP error responses are short, fixed, generic strings;
  the one place a raw exception is captured (`ProviderCallFailed`) is
  logged server-side only, the client gets a fixed literal.
- **PASS** — no `debug=True` anywhere; FastAPI/Starlette's default
  non-debug posture applies to unhandled exceptions.
- **UNVERIFIED** — no centralized `@app.exception_handler` was found for
  truly unhandled (non-`HTTPException`) exceptions; Starlette's default
  in non-debug mode is ASVS-compliant (generic 500, no trace), but no
  test in this repo pins that exact response shape.

### V8 — Data Protection
- **FAIL (real gap, handed to Package 6/Privacy — see item 6 below)** —
  participant text is not encrypted at rest. `session_events.payload` is
  plain `TEXT` (`engine/m4/store.py`); no encryption call anywhere in
  that file or `engine/m8/log_store.py`. The threat model's own claimed
  control ("encryption at rest, RDS/S3 default KMS") describes the
  undeployed design, not the SQLite-on-Render-disk system actually
  running.
- **PASS** — TLS: Render terminates TLS at its edge; nothing in
  `engine/api` attempts to manage or downgrade it; `uvicorn` runs plain
  HTTP behind `--proxy-headers` trusting Render's proxy, the correct
  posture for a service behind a TLS-terminating platform.
- **FAIL (gap, not fixed — low severity, noted)** — no `Cache-Control`
  headers anywhere in `engine/api`; transcript/message responses rely on
  framework defaults rather than an explicit `no-store` on
  session-content endpoints.

### V9 — Communications
- **FAIL (drift vs. design, informational)** — the threat model names
  "CloudFront in front" as part of the intended topology
  (Artifact-6-Operations.md line 41); `render.yaml` never implements
  this for either `cic-engine` service. No WAF/edge rate-limiting exists
  beyond the application's own in-process limiter, which is explicitly
  single-instance-scoped by its own docstring — not a defense against a
  distributed attack. Cloudflare is genuinely in front of `cic-website`
  (the separate marketing site), not `cic-engine`.
- **PASS** — Bedrock calls go through `anthropic.AnthropicBedrock`
  (`engine/provider/bedrock.py`), HTTPS by default, no insecure-transport
  override.

### V10 — Malicious Code
- **FAIL (gap, not fixed here)** — every `requirements.txt` under
  `engine/` uses `>=`, zero `==` pins, no lockfile. A build today can
  pull a materially different, unreviewed transitive tree next month.
  Item 5 (dependency audit, PR #376) confirms today's resolved tree is
  clean; it does not address the pinning discipline itself — a real
  follow-up, not fixed in this package (would touch every
  `requirements.txt` in the repo, a wider change than this audit's
  scope).
- **PASS** — no `eval`/`exec`/`pickle` anywhere (same grep as V5).

### V11 — Business Logic
- **PASS** — duplicate-message replay protection (`DuplicateMessage` →
  409, backed by `Store.event_exists`'s idempotency-by-uuid).
- **PASS** — `SESSION_TURN_CAP` (see V3) is a genuine business-logic
  abuse control, not just a rate limit.
- **PASS** — table-mode sequencing rules (`TableRoundStillOpen`,
  `TableAdvanceInFlight`, `TableRoundNotOpen`) are all server-enforced,
  never trusted from client state.
- **PASS, with the item-3 gap still open** — per-IP rate limiting covers
  both spend-bearing surfaces; the missing *daily* ceiling is exactly
  what item 3's anonymous visitor cap (PR #377) proposes to close, not
  yet decided.

### V12 — Files and Resources
- **PASS, confirmed sound** — the SPA catch-all's path-traversal guard
  (`engine/api/app.py`, `serve_frontend`): resolves the candidate path
  first, then checks `is_relative_to` the dist root before ever serving
  it — the correct order and the correct primitive, not a naive
  string-prefix check a symlink could bypass. Explicitly the fix for a
  known historical vulnerability class in a sibling codebase
  (the function's own docstring).
- **NOT-APPLICABLE** — no file upload functionality exists anywhere in
  this service.

### V13 — API and Web Service
- **PASS** — JSON-only (every response is a Pydantic model via FastAPI's
  default serialization; no XML import anywhere in `engine/api`).
- **PASS** — no CORS middleware exists anywhere in `engine/` — correctly
  absent, not misconfigured, matching the documented same-origin design
  (`render.yaml`'s own top-of-file comment).
- **PASS** — error responses are generic, no internals leaked (cross-ref
  V7).

### V14 — Configuration
- **FAIL (real gap, not fixed here)** — no HTTP security-header
  middleware anywhere: no CSP, no `X-Frame-Options` (clickjacking
  exposure on the served SPA), no `X-Content-Type-Options`, no
  app-layer HSTS. Zero matches for any of these across `engine/`. This
  is the single largest concrete gap this checklist found that's both
  cheap to fix and squarely in ASVS L1 scope — recommended as the next
  small PR after this package closes (a `SecurityHeadersMiddleware`
  analogous to `ratelimit.py`'s own `install()` pattern), deliberately
  not bundled into this already-multi-PR package.
- **PASS** — debug mode off; directory listing not applicable
  (`StaticFiles` mount has no listing feature, and the catch-all never
  enumerates a directory).
- **PASS** — admin-token-absent returns 404 not 401 (deliberate,
  covered under V2).
- **UNVERIFIED** — uvicorn's default `Server: uvicorn` response header
  is very likely present (no suppression flag in the Dockerfile CMD);
  not confirmed against a running instance. Minor info-disclosure item.

### Checklist summary

| Result | Count | Notes |
|---|---|---|
| PASS | 25 | |
| FAIL — fixed in this package | 4 | admin rate limiting, admin token entropy, message-length cap (V5), session-code-guessing GETs unprotected (V1 correction) |
| FAIL — real gap, handed off or flagged for follow-up | 6 | encryption at rest (→Package 6), security headers, Cache-Control, dependency pinning, threat-model drift (x2) |
| NOT-APPLICABLE | 2 | logout, file upload |
| UNVERIFIED | 3 | V5 prompt-injection code trace, V7 500-handler shape, V14 server header |

(The IAM policy's ARN syntax error is a defect in item 2's own artifact, not an ASVS checklist line — counted separately below, not in this table.)

No item above is a silent pass. Every FAIL either has a fix in this
package's own PRs or a named owner/destination below.

**A closing adversarial review (Opus, 2026-09-21 — full findings in
`Decision-Log.md` entry 8) found three genuinely blocking defects across
this package's own PRs, all now fixed**: this PR's IAM policy had an ARN
syntax error that would have made its own "least-privilege" grant
authorize nothing at the foundation-model layer (see item 2 below); PR
#377's anonymous cap was fully bypassable via unlimited token harvesting
(the cap didn't cap); and PR #376's dependency audit had been run against
a tree that no longer matched `main`. The review also caught a client-IP-
spoofing bypass of every rate limiter in this file (including this PR's
own admin fix) and the two V2/V5 findings folded into the counts above.
Every item below reflects the POST-review, fixed state, not the original
draft.

---

## Item 2 — Production Bedrock IAM identity

Full policy and step-by-step setup: `IAM-Runbook.md` and
`iam-policy-cic-bedrock-prod.json`, both in this directory. Summary:
least-privilege `bedrock:InvokeModel`/`InvokeModelWithResponseStream`
scoped to the two inference profiles this service resolves at startup
(the pinned safety profile exactly, the voice profile by its committed
loose pattern), plus the underlying foundation-model ARNs across the
inference profile's constituent regions (required for cross-region
routing to actually authorize — a common, easy-to-miss Bedrock IAM
mistake), plus `bedrock:ListInferenceProfiles` for the startup resolution
call. One policy, two separate IAM users/credentials (`cic-bedrock-prod`,
`cic-bedrock-staging`) for rotation and CloudTrail-attribution separation.

**Corrected after the closing adversarial review:** the original draft
put `<AWS_ACCOUNT_ID>` in all eight resource ARNs. Bedrock foundation-
model ARNs have no account segment at all
(`arn:aws:bedrock:${Region}::foundation-model/${id}` — AWS-owned, not
account-owned resources) — applied as originally written, the policy
would have authorized correctly at the inference-profile layer and
granted **nothing** at the foundation-model layer, producing exactly the
intermittent, region-dependent `AccessDenied` the runbook's own
troubleshooting section warns about, for a reason its own hint (adjust
the region list) would never have led anyone to. Fixed: the account id
now appears only on the two `inference-profile/` ARNs. Also corrected:
the runbook's "two identities, one policy" section originally claimed
this setup gives blast-radius containment between prod and staging — it
doesn't (both credentials can invoke the exact same models, region, and
account); reworded to claim only what two access keys actually buy
(rotation and attribution), and to say plainly what would be needed for
real containment if that's ever wanted.

**Not applied.** Creating the IAM user and policy in AWS, and setting the
resulting keys in the Render dashboard, is Mark's own account action —
nothing here was created from this sandbox (no AWS access exists here),
and the runbook says so explicitly.

---

## Item 3 — Anonymous visitor daily cap (unbounded consumption)

PR #377. `engine/api/anon_cap.py`: HMAC-signed HttpOnly cookie token, no
accounts, no PII, daily session/turn cap layered on the existing per-IP
limiter, flagged OFF by default. Three options compared in the PR body,
Option A (signed cookie) built as the proposal:

| Option | Mechanism | Frontend change? | Recommendation |
|---|---|---|---|
| A | Signed HttpOnly cookie, server-issued | None (same-origin) | **Recommended — built** |
| B | Client token in localStorage + header | Small (`api.ts`) | More moving parts, similar protection |
| C | Pure per-IP daily bucket, no visitor concept | None | Simplest, but conflates shared/NAT'd IPs |

**Escalation, open:** mechanism choice and the proposed numbers (5
sessions/day, 150 turns/day) need Mark's decision before
`CIC_API_ANON_CAP_ENABLED` is ever set anywhere. Per `CLAUDE.md`'s
escalation table, participant-facing flow is always-ask, and this
package didn't pick silently — see Decision-Log entry 4.
`CIC_API_ANON_CAP_ENABLED`/`_VISITOR_SECRET` are now declared explicitly
in `render.yaml` as `"0"`/`sync: false` (not left unset), so the pending
decision has a visible, reviewable config-as-code home once Mark makes it.

**Corrected after the closing adversarial review — the built option A did
not actually cap anything.** Three blocking defects, all traced to one
gap: no test in the original suite ever exercised a real HTTPS cookie
round-trip, so the cookie path shipped unverified.
1. A fresh, empty-bucket token was minted on **every** request, including
   ones the cap had just refused with a 429 — an attacker deleting their
   cookie before each request harvested an unbounded supply of tokens
   without ever needing to succeed once. Fixed: minting only happens on
   the allowed path now, and a new token is seeded from the requesting
   IP's own current count rather than starting at zero — bounds the
   exploit to a small, rate-limited residual instead of eliminating the
   cap outright (exact bound in `DailyVisitorLimiter.mint_seeded_token`'s
   own docstring).
2. Middleware registration order was backwards (Starlette's stack is
   LIFO), so the daily-quota check actually ran *before* the cheap per-IP
   burst check, meaning a request the burst limiter was always going to
   reject still spent daily quota first. Fixed by swapping registration
   order in `create_app`.
3. The test suite's `TestClient` used the default `http://` base URL; the
   visitor cookie is (correctly) `Secure`, and no `Secure` cookie ever
   round-trips over plain HTTP in a real client — so "cookie persists
   across requests" tests were silently landing in the IP-fallback bucket
   instead of exercising the real per-visitor path the whole time. Fixed,
   plus two new tests that directly reproduce the harvesting exploit and
   pin it bounded, not unlimited.

113 tests now pass on this branch (full `engine/api/` suite), including
16 in `test_anon_cap.py` (7 new — two direct regression tests for the
harvesting exploit and the double-charge ordering bug, plus the fixed
`https://` base URL that made the existing cookie tests meaningful).

---

## Item 4 — Prompt-injection probe set

PR #378. 40 probes, 5 categories (instruction override, system-prompt
extraction, sealed-probe extraction, persona break-out, Facilitator
redirect talk-down), `probes/probes.yaml` + `probes/run_probes.py`.

- **Live run against `cic-engine-staging`: not done.** This sandbox's
  network egress is allowlisted to a short fixed host set that does not
  include Render — confirmed directly against the staging host and
  against a general-internet control. Matches
  `CiC_Promotion_Runbook.md`'s own prior finding that Render is
  egress-blocked from this environment. Exact command to run it for real
  is in `probes/RESULTS.md`.
- **Structural run against the local dev server: done.** 40/40 probes
  completed over real HTTP against `engine/api/dev_server.py`'s fixed
  fake client — proves the harness (session creation, auth, the
  multi-turn `talkdown-1` thread, response capture) works end to end.
  Proves nothing about real model behavior. Found and fixed one
  unrelated bug blocking even this run (see Decision-Log entry 5).

**This item is genuinely incomplete** — the security-relevant question
(does the real model resist these 40 probes) has no answer yet. Handing
this forward explicitly: whoever has network access to
`cic-engine-staging` needs to run `probes/run_probes.py --base-url
https://cic-engine-staging.onrender.com --world alx` (a real, admitted
world — **not** `--world fix`, see below) and grade each
`response_excerpt` against its `expect` line.

**Corrected after the closing adversarial review:** the hand-off command
above originally named `--world fix`, the synthetic fixture world, which
`engine/api/app.py`'s own comment says must never be participant-
reachable. `fix` has no real Representative persona (defeats the 9 PB
probes), nothing sealed behind it (defeats the 6 SEAL probes), and none
of the historical-otherness texture 9 of the FRT probes' `expect` lines
depend on — the live run would have completed and reported success while
testing almost nothing the categories actually name. Fixed the example
and added the same warning to `run_probes.py`'s own usage docstring, at
the point anyone would actually read it before invoking the script.

Also flagged by the review, documented but not built in this pass (see
`probes/RESULTS.md`'s own "Known limitation" section): all 40 probes are
direct injection through the participant's own message. Indirect
injection via retrieved corpus content, and probes aimed at the safety
classifier itself rather than at talking a voice model out of an
already-fired redirect, are both real, higher-value gaps — recommended as
a named, separate follow-up probe set rather than built blind here.

---

## Item 5 — Dependency audit

PR #376. `pip-audit` clean on both files the production Dockerfile
installs (`engine/api/requirements.txt`, `engine/m1/requirements.txt`).

**Corrected after the closing adversarial review — the original audit was
run against a stale tree.** This branch was the only one of the
package's four not based on current `main`; its merge-base predated
`main`'s own commit `9321610b` ("Fix frontend-tests CI: jsdom 30.x
requires Node >=22, CI runs Node 20"), which added `vitest`, `jsdom`,
`@testing-library/react`, and `@testing-library/jest-dom` as new
devDependencies — none of which were in scope when the original `npm
audit` ran. Merged `main` in and re-ran the audit against the real
current tree.

The picture changed: 5 findings (3 moderate, 1 high, 1 **critical** —
`GHSA-5xrq-8626-4rwp`, arbitrary file read/execution when vitest's UI
server is listening), still all devDependency-only. Unlike the previous
round's 2 waived findings, `npm audit fix --force` (vite 5→8, vitest
2→5) this time verified **fully clean**: both `npm run build` and `npm
test` (`vitest run`, the mode CI actually uses) pass with no changes
needed beyond the version bump. Took the full fix rather than waiving —
`npm audit` now reports **0 vulnerabilities**. The `@vitejs/plugin-react`
peer-range warning from the previous round is still present (it doesn't
officially list vite 8 yet) but no longer blocks taking the fix once
build and test are both empirically confirmed passing on it.

---

## Item 6 — Logging and data-at-rest review

**Fixed in this package** (this PR): `/api/admin/pilot-summary` had zero
rate limiting on its Bearer-token check — an attacker could brute-force
guess the token at unlimited rate with zero cost per attempt.
`engine/api/ratelimit.py` now covers `/api/admin/*` with its own 10/min
per-IP bucket, same mechanism as the existing session/conversation
limiters. This is genuinely this package's own scope (ASVS V2.2.1,
directly security-relevant, small), not a hand-off. Also fixed, both
caught by the closing adversarial review: `client_ip()` (the same
function every limiter in this file keys on) trusted the *first*
`X-Forwarded-For` entry, which a standard reverse proxy (Render's edge
included) appends the real peer onto rather than replacing — so the
first entry is exactly the part a client controls directly, and trusting
it let anyone bypass every limiter in this file, this PR's own admin fix
included, with one request header. Now takes the last entry. And the two
GET endpoints (`/transcript`, `/round-close-reasons`) that guess a
session code through the identical 401 the message/continue POSTs use
were never in this limiter's own path match at all — same ASVS V2.2.1
class, the participant-facing instance rather than the operator-facing
one, closed the same way.

**Findings, not fixed here — handed to Package 2 (Operations) and
Package 6 (Privacy) by name**, per this package's own instruction that
item 6 is findings-plus-trivial-fixes only:

- **→ Package 6 (Privacy):** Participant text (`session_events.payload`
  and the usage log) is stored as plaintext in SQLite on the Render
  disk, with no application-level encryption at rest. A Render disk
  backup or snapshot — if one exists; this sandbox has no visibility
  into Render's backup configuration, and that's itself worth
  confirming — would carry plaintext transcripts. `render.yaml`'s own
  comment already names the intended follow-up ("retention/TTL and the
  deletion_requested writer — audit move 6") as deferred and not yet
  built anywhere in `engine/m4/store.py` or `engine/m8/log_store.py` —
  confirmed by grep, zero matches for retention/TTL/deletion_requested
  in either file. Persistence without retention is unbounded growth of
  exactly the data this finding is about.
- **→ Package 2 (Operations):** Whether Render's disk-level storage is
  encrypted at rest by the platform itself (a property this repo can't
  verify), and whether Render's disk backup/snapshot feature is even
  enabled for either service, are both platform-configuration questions
  outside this repo's own visibility — worth a direct check in the
  Render dashboard.
- **Admin endpoint soundness (the second half of item 6's own
  question):** otherwise sound. `PilotSummaryResponse` (the only
  response body this endpoint returns) carries pure aggregate counts —
  total sessions, counts by mode/close-reason/round-cap, two
  timestamps — no participant text, no transcripts, no session ids.
  Auth is a separate, constant-time-compared credential from the
  per-session code, and now rate-limited (this PR). No further finding
  here beyond the two handed off above.

---

## Done bar

**Corrected after the closing adversarial review** — two lines below were
checked off before they were actually true (the review caught this too,
as its own finding S10). Both are accurate now, reflecting the state
after every fix documented above and in `Decision-Log.md` entry 8.

- [x] ASVS L1 checklist on file, no unexplained fails (item 1, above —
      every FAIL has a fix, an owner, or an explicit follow-up)
- [x] IAM policy document and runbook steps written, and corrected for
      the ARN-syntax defect the closing review caught (item 2) — **not
      applied; Mark's own account action**
- [ ] Anonymous cap — code fixed (was fully bypassable; now bounded, see
      item 3 above) and 4 PRs open, **none merged yet** — options
      presented to Mark, not yet decided (item 3 — **open escalation**,
      Decision-Log entry 4)
- [ ] Probe results with response excerpts (item 4) — **live run against
      a real model not done**, structural harness proven and its own
      world-choice bug fixed, handed forward explicitly
- [x] Dependency audit clean (item 5 — re-run against current `main`
      after the closing review caught the original run was stale; 0
      vulnerabilities, no waiver needed anymore)
- [x] Closing Opus adversarial review run — findings above; every
      BLOCKING and SHOULD-FIX finding addressed in a follow-up commit on
      its own PR, see `Decision-Log.md` entry 8 for the full list and
      what's fixed vs. accepted-open

### For the reviewer thread

Checked against ASVS L1: 25 PASS, 4 FAILs fixed in-package (2 of them —
the message-length cap and the session-code-guessing GETs — found only
by the closing adversarial review, not the original pass), 6 real gaps
named with an owner or explicit follow-up (none silently dropped), 2
architectural not-applicables, 3 explicitly UNVERIFIED rather than
guessed either way. Checked against the LLM Top 10: unbounded consumption
has this package's own rate-limiting and message-length fixes (item 6)
plus a proposed, not-yet-decided daily-cap mechanism whose code was
fully bypassable until the closing review caught it — now bounded, not
yet merged (item 3); prompt injection has a 40-probe set whose live-model
run is not yet complete, and whose hand-off command pointed at the wrong
world until corrected (item 4); sensitive-information disclosure has one
real open gap (encryption at rest, handed to Package 6) and no other
findings from this pass. AWS least-privilege identity has a written
policy and runbook — corrected after the review found an ARN-syntax
error that would have made the policy authorize nothing at the
foundation-model layer — not yet applied (item 2, Mark's action).

**None of this package's four PRs are merged.** All four (#376, #377,
#378, #379) carry a follow-up commit addressing the closing review's
findings and are ready for Mark's review; none should be treated as
"done" until actually merged, and #377 (the anonymous cap) additionally
needs his mechanism/numbers decision before `CIC_API_ANON_CAP_ENABLED`
is ever set to `"1"` anywhere.
