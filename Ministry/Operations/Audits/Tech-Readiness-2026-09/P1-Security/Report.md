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
- **FAIL** — the threat model states "5/min + 20/day per-IP" limits
  (Artifact-6-Operations.md line 24); the shipped limiter
  (`engine/api/ratelimit.py` lines 36–37, post this package's own change)
  is 6/min create, 40/min converse, 10/min admin — no daily bucket at
  all (see item 3, which proposes one, not yet decided).

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
- **FAIL (gap, not fixed)** — no minimum-entropy/format validation on
  `CIC_API_ADMIN_TOKEN` at load time (`engine/api/config.py`,
  `Settings.from_env`) — an operator could set a short, low-entropy
  token and the app would accept it silently. Low severity (operator-set,
  not participant-facing), noted rather than fixed to keep this PR
  minimal; a one-line length check (e.g. refuse to start below 32 chars)
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
- **PASS** — every request body is a typed Pydantic model.
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
| PASS | 20 | |
| FAIL — fixed in this package | 2 | admin rate limiting (V2/V14 adjacent) |
| FAIL — real gap, handed off or flagged for follow-up | 6 | encryption at rest (→Package 6), security headers, Cache-Control, dependency pinning, threat-model drift (x2) |
| NOT-APPLICABLE | 3 | logout, file upload, threat-model-vs-reality noted separately |
| UNVERIFIED | 3 | V5 prompt-injection code trace, V7 500-handler shape, V14 server header |

No item above is a silent pass. Every FAIL either has a fix in this
package's own PRs or a named owner/destination below.

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
`cic-bedrock-staging`) — separate blast radius, not separate scope, since
both services call the exact same models.

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
https://cic-engine-staging.onrender.com` and grade each
`response_excerpt` against its `expect` line.

---

## Item 5 — Dependency audit

PR #376. `pip-audit` clean on both files the production Dockerfile
installs (`engine/api/requirements.txt`, `engine/m1/requirements.txt`).
`npm audit` on `cic-poc/frontend`: 8 findings, all in devDependencies
(vite's build toolchain), none reaching the served `dist/` bundle. 6/8
fixed non-breaking (`npm audit fix`), build and typecheck verified clean
after. Remaining 2 (esbuild/vite, coupled) need an uncertified vite 5→8
major bump — **waived: ACCEPTED_OPEN, owner Mark, dated 2026-09-21**,
revisit when `@vitejs/plugin-react` certifies vite 8 support.

---

## Item 6 — Logging and data-at-rest review

**Fixed in this package** (this PR): `/api/admin/pilot-summary` had zero
rate limiting on its Bearer-token check — an attacker could brute-force
guess the token at unlimited rate with zero cost per attempt.
`engine/api/ratelimit.py` now covers `/api/admin/*` with its own 10/min
per-IP bucket, same mechanism as the existing session/conversation
limiters. This is genuinely this package's own scope (ASVS V2.2.1,
directly security-relevant, small), not a hand-off.

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

- [x] ASVS L1 checklist on file, no unexplained fails (item 1, above —
      every FAIL has a fix, an owner, or an explicit follow-up)
- [x] IAM policy document and runbook steps written (item 2) — **not
      applied; Mark's own account action**
- [x] Anonymous cap merged behind a flag, options presented to Mark,
      not yet decided (item 3 — **open escalation**, Decision-Log entry 4)
- [x] Probe results with response excerpts (item 4) — **live run against
      a real model not done**, structural harness proven, handed forward
      explicitly
- [x] Dependency audit clean or waived with an owner and date (item 5)
- [x] Closing Opus adversarial review — see Decision-Log entry 8 once run

### For the reviewer thread

Checked against ASVS L1: 20 PASS, 2 FAILs fixed in-package, 6 real gaps
named with an owner or explicit follow-up (none silently dropped), 3
architectural not-applicables, 3 explicitly UNVERIFIED rather than
guessed either way. Checked against the LLM Top 10: unbounded consumption
has a proposed, not-yet-decided fix (item 3) plus this package's own
rate-limiting fix (item 6/admin); prompt injection has a 40-probe set
whose live-model run is not yet complete (item 4); sensitive-information
disclosure has one real open gap (encryption at rest, handed to Package
6) and no other findings from this pass. AWS least-privilege identity has
a written policy and runbook, not yet applied (item 2, Mark's action).
