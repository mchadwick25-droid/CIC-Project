# Build handoff note

Read `Build-Blueprint.md` first; this note is only the "where things stand"
supplement it asks for at every stage boundary / stop-and-ask / economy
checkpoint.

## Current stage: 5 partial — non-model half done; Bedrock preflight PASSED; the live-model work itself (safety script, real generation call, crisis-append, lazy load/unload) not yet started

**Bedrock preflight — done, commit `7cfeda7`.** `engine/provider/` (seam +
preflight, commit `bde1ea7`) run for real against Mark's live account
(468683594478, us-east-1, `cic-bedrock-dev` IAM user scoped to 5 `bedrock:`
actions only). All three required legs green:
`engine/provider/reports/preflight-report.json` - model resolved (not
guessed) to `us.anthropic.claude-sonnet-4-5-20250929-v1:0`, cache write
confirmed (4202 tokens), cache read confirmed on the very next call (same
4202 tokens, not rewritten), streaming usage shape confirmed carrying cache
fields too (the specific silent-absence risk spec SS10 names). Invoice
reconciliation (the preflight's third leg) still pending - AWS billing data
lags; no $/token figure exists or is quoted anywhere yet, per spec
principle 13.

Credential handling note for whoever picks this up: the AWS access key was
pasted directly in chat (after two other delivery paths - session env vars,
a `.env` file created outside this container - failed to actually reach
this session's filesystem/process). It lives in a local, gitignored `.env`
here, never committed, never printed by any script. Mark was advised to
rotate/delete this key once live-model dev work is further along, since a
chat-pasted credential is a weaker channel than the ones tried first.

**Not started yet:** the actual stage-5 gate items needing live calls - the
safety script (~20 adversarial conversations, ≥19/20 floor), wiring a real
generation call into M4's turn loop, crisis-append-on-empty-stream, lazy
world load/unload timing. Each of these means real, repeated spend (not
one preflight's worth) - worth explicitly checking pace/scope with Mark
before running a batch of them, especially since the AWS Budget Action
(deny-policy backstop) still isn't in place - Mark chose to proceed without
it for now, accepting the $20 alert-only budget + free-plan credit ceiling
as the backstop (his call, recorded here, not silently assumed).

**Stage 0.6 — done, commit `75278a2`.** Fixture world, fixture-scope 8-cell
canon subset, `fixtures/seeded_defects.yaml`.

**Stage 1 (M1: schema, registry, gates) — done, commit `440cc15`.**
`engine/m1/`. Evidence: `engine/m1/reports/selftest-report.json`.

**Stage 2 (M2 compiler) — done, commits `dcac649` + `159044c`.**
`engine/m2/`. `records/worlds.yaml` fix entry: `building → built`.

**Stage 3 (Canon v1 + sealed admission paraphrases) — done, commits
`db1925b` + `2846d53`.** `records/_fleet/canon_question/` (86 records, 28
cells), `canon/sealed_probes/` (28 sealed paraphrases + isolation guard).

**Stage 4 (M3 admission harness) — done, this commit:**
- `engine/m3/protocol.py` — the battery: the 28 sealed probes, center-first
  draw order (canon maintenance rule 5).
- `engine/m3/masking.py` — the blind-protocol boundary: a `MaskedTranscript`
  TypedDict is the only shape any grading check accepts; `assert_blind()`
  raises on anything carrying `world_key` or `paraphrase_of`.
- `engine/m3/generation.py` — `FixtureRecordAnswerer`, a deterministic,
  no-model stand-in that answers a cell from the fixture's own records
  (demonstration first, then the coverage-gate's own substantive/
  honest_limit classification); citations are the *union* of every
  demonstration/substantive/honest_limit record's sources for that cell,
  not just whichever one supplies the answer text — otherwise the
  fabrication-defect scenario (a bad citation on a *quote* record) would
  never surface for a cell where a *demonstration* happens to answer.
  `LiveModelAnswerer` is a named, deliberately-`NotImplementedError` seam.
- `engine/m3/grading.py` — `source_boundedness_check` (mechanical, reliable:
  every citation must resolve to a real source record) and
  `register_check` (an explicitly narrow heuristic — one metaphor-as-
  definition regex, grounded-in-a-real-quote check — built and tested
  against exactly the one seeded register defect this stage's gate names,
  *not* offered as a general register grader; spec module M3 itself says
  Mark's reading is the real register instrument).
- `engine/m3/harness.py` + `results.py` — orchestration and
  `validation/admission/results.json`'s shape (`sealed-key refs`: results
  reference `probe_id`, never the sealed plaintext wording).
- `engine/m3/selftest.py` — stage-4 gate, confirmed:
  `engine/m3/reports/selftest-report.json` shows the clean fixture battery
  all-pass (28/28) and both M3-layer `fixtures/seeded_defects.yaml` entries
  caught (`admission-register-invented-aphorism`,
  `admission-fabricated-source`).
- **Deliberately reverted mid-stage:** `engine/m2/validation.py` briefly
  imported `engine.m3` to embed real admission results into a compiled
  package, then was walked back — `canon/sealed_probes/README.md` and
  `engine/canon/check_seal_isolation.py` both name M2 as a code path barred
  from the sealed plaintext, and M3 reads that plaintext, so M2 must never
  import M3 even transitively "just to build a package." Real admission
  evidence stays at `engine/m3/reports/selftest-report.json`, deliberately
  never routed through a package. Recorded here so nobody "fixes" this
  apparent gap the same way again without re-deriving why it isn't one.
- CI: `m3-admission-harness` (module name, not the stage-3 job — see
  `.github/workflows/ci.yml`'s own comment on the near-collision between
  "M3 the module" and "stage 3").

Stage 4 gate reached: *"catches a seeded register defect and a seeded
fabrication on the fixture world."*

**Stage 5 (M4+M5), non-model half — done, this commit:**
- `engine/m4/store.py` — the session event log (Artifact-3 SS1): SQLite-
  backed for dev/test (DECIDABLE, same pattern as M2's FAISS placeholder;
  real deployment is managed Postgres per Artifact-6 SS3 topology). Append
  is idempotent on `event_uuid` (a retried append is a silent success, never
  a duplicate row), ordered per-session via `seq`, with bounded (3×) retry
  on a concurrent-writer collision. `Store` holds no session state itself -
  that's what makes "any instance can serve any session" literally true.
- `engine/m4/events.py` — the event catalog (Artifact-3 SS2): required-key
  and closed-vocabulary validation per type; `guidance_*` is accepted as a
  reserved family but `validate()` refuses to ever pass one (spec principle
  2: no live guidance exists).
- `engine/m4/projection.py` — `project_fresh()`: folds the log into a fresh
  `SessionState` every call, never a cached/shared instance. The safety
  accumulator folds as "take the latest `safety_state` event per track,"
  never a manual re-summation - each event already carries its own full
  current value, so resume-safety is a property of the log, not the fold.
- `engine/m4/session_code.py` — 128-bit CSPRNG, Crockford base32 (26 chars,
  grouped), SHA-256 hashed at rest, constant-time compared.
- `engine/m4/entrance.py` — the entrance seal, enforced twice:
  `open_session()` refuses a second `session_started` for the same
  `session_id` at runtime (the real guarantee), and
  `find_second_writer_violations()` greps the rest of `engine/` for a
  session_started *write site* as defense-in-depth. **Found and fixed a
  false-positive on the first real run**, worth remembering: a plain
  substring grep for `"session_started"` flagged `events.py` (a schema
  declaration) and `projection.py` (a read/fold) as "violations" - neither
  is a write. Narrowed to a regex matching only the keyword-argument write
  shape (`event_type="session_started"`, excluding `==` reads) before
  trusting the guard - the same "don't ship a guard that flags legitimate
  code" lesson as stage 3's isolation guard, hit fresh here because it's a
  different guard.
- `engine/m4/tests/test_resume_across_processes.py` — the literal gate item:
  two independent `Store` instances sharing nothing but a file path
  reconstruct identical, full-fidelity state (including a safety
  accumulator that was updated *after* the simulated resume) from the log
  alone.
- `engine/m5/anachronism.py` — anachronism computed per world from its own
  `time_window` against fleet `modern_term.origin_year` data - no world
  identifier in the code (law 4).
- `engine/m5/routing.py` + `failure.py` — the deterministic routing merge
  (Artifact-4 SS3, priority order proven by test: safety > system_nature >
  anachronistic bridge > later_age/other_tradition press-state > ordinary)
  and the fail-open/degraded semantics (SS4: reader failure forces
  pass-through regardless of safety's own outcome; safety failure alone
  fails open but reader-based routing still applies; two consecutive
  degraded turns is the page-the-operator condition). Both take
  already-resolved call outcomes (`CallOutcome`) as input - they never make
  or await a model call themselves, which is exactly what makes this half
  buildable and testable today.
- CI: `m4-event-log`, `m5-gate-routing`. Evidence:
  `engine/m4/reports/pytest-output.txt` (22/22),
  `engine/m5/reports/pytest-output.txt` (25/25). Full suite across every
  stage: 60/60 (`python -m pytest engine -q`).

**Stage 5, model half — still blocked, ETA given but not yet live:** Mark
confirmed (this session) the Bedrock account is provisioning, "available in
a couple of hours" as of this note. Nothing about that changes the decision
below - it's still open until the account is actually live and a
model/provider choice is confirmed, not merely imminent. Do not start
spending against Bedrock or picking a model unprompted once it comes up;
confirm first per the reasoning already recorded here.

## Before the model half of stage 5: a decision, not a guess

Stage 5's remaining gate items — *"live safety script ≥19/20 vs fixture
world; crisis append asserted incl. empty-stream; lazy load/unload
measured"* — every one needs a **real conversational turn** (resume and the
entrance seal, the other two gate items, are already done above without
one). The live safety script alone is 20-ish adversarial conversations
against the fixture world. That means:

1. **A model provider must be chosen and configured** (spec principle 11:
   provider switches land last and alone — meaning this is exactly the kind
   of decision that shouldn't be made implicitly by whichever thread happens
   to need a model call first). Spec §7 names Bedrock as the pilot's target,
   but "Bedrock preflight — blocked on the live AWS account" is explicitly
   listed as an unresolved risk (spec §10), and no AWS account has been
   wired into this build environment.
2. **Real spend.** Even a cheap Haiku-class gate call, run ~20+ times for
   the safety script alone, is real API cost. Build-Blueprint.md §4 reserves
   "spending beyond the budget envelope" as Mark's decision, not this
   thread's.

Stage 4 deliberately avoided both by building `FixtureRecordAnswerer` (no
model call) instead of wiring a live one. The live safety script and a real
generation call can't avoid it — that IS the remaining stage-5 work. **This
is the decision to raise with Mark before writing that code**, not a guess
to make and correct later: which provider/model to call (Bedrock, once
actually live, or a cheaper interim path for dev-time iteration before the
real Bedrock preflight), and confirmation that the near-term spend (dev
iteration + the safety script's ~20+ calls) is within an approved envelope.
Mark has since said the Bedrock account is provisioning and should be
available in a couple of hours - noted above; still not a green light to
spend against it until it's actually live and the choice is confirmed.

**Already done without that decision** (this session, this commit): the
event log/store, session projection, session codes, the entrance seal,
resume-across-two-processes, and the Facilitator gate's routing/failure
logic — see the "non-model half" list above. What's left needs the live
call specifically: the actual generation/classification calls themselves,
the live safety script's 20-ish adversarial conversations, crisis-append-
on-empty-stream (needs a real stream to interrupt), and lazy load/unload
timing (needs real request latency to measure against).

## Open decisions still outstanding

- `gravity`/`force` record field shape — ratified as-is at stage 1, unchanged.
- FAISS placeholder vectors (`engine/m2/builders.py`) — still a
  deterministic hash-derived stand-in; folds into the stage-5 model/provider
  decision above (an embeddings choice is part of the same "which provider"
  question).
- Sealing mechanism (`canon/sealed_probes/README.md`) — commit-reveal +
  access-discipline guard; real secrets infra is a later, non-urgent call.
- `engine/m3`'s register heuristic — explicitly narrow; real register
  grading needs either Mark's read or a configured model, both blocked on
  the same stage-5 decision above.

## Currently blocked

**Stop-and-ask open:** the model-provider/spend decision above, before any
work that needs a live model call - unchanged by Mark's Bedrock ETA update;
"a couple of hours out" is a status, not a confirmation to proceed. Nothing
else is blocked: the non-model half of stage 5 is done (this commit).
