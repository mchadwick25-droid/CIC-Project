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

**8. 2026-09-21 — Closing Opus adversarial review.** [To be appended once
run — see Report.md's own closing section for the outcome.]
