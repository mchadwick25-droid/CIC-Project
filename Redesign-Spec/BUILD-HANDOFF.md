# Build handoff note

Read `Build-Blueprint.md` first; this note is only the "where things stand"
supplement it asks for at every stage boundary / stop-and-ask / economy
checkpoint.

## Current stage: 4 complete, ready to start stage 5 — with a real decision to raise first

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

## Before stage 5 (M4+M5 runtime, gate, safety): a decision, not a guess

Stage 5 is *"resume across two processes incl. accumulator; entrance-seal
test; live safety script ≥19/20 vs fixture world; crisis append asserted
incl. empty-stream; lazy load/unload measured."* Every one of those needs a
**real conversational turn** — the live safety script alone is 20-ish
adversarial conversations against the fixture world. That means:

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
model call) instead of wiring a live one. Stage 5 can't avoid it — M4's
whole job *is* the live turn. **This is the stage boundary to raise with
Mark before writing stage-5 code**, not a guess to make and correct later:
which provider/model to call (Bedrock now, or a cheaper interim path for
dev-time iteration before the real Bedrock preflight), and confirmation
that the near-term spend (dev iteration + the safety script's ~20+ calls) is
within an approved envelope.

**What stage 5 CAN do without that decision, if asked to keep moving in the
meantime:** the parts of M4/M5 that don't need a live model call - the event
log schema and store (Artifact-3), the append-only session projection, the
entrance-seal test (one writer of `session_started`), resume-across-two-
processes machinery, and the Facilitator gate's *routing logic* (Artifact-4
§3's deterministic merge) all the way up to *where* a model call would go -
stubbed the same way `LiveModelAnswerer` is stubbed now. That's real,
useful, DECIDABLE progress; the live safety script and the actual generation
call are not.

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
further stage-5 work that needs a live model call. Everything else keeps
moving in the meantime per the "what stage 5 CAN do" note.
