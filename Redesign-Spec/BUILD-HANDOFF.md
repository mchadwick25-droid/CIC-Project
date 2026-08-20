# Build handoff note

Read `Build-Blueprint.md` first; this note is only the "where things stand"
supplement it asks for at every stage boundary / stop-and-ask / economy
checkpoint.

## Current stage: 3 complete, ready to start stage 4

**Stage 0.6 (fixture world) — done, commit `75278a2`.** Fixture world
(`records/fix/**`, all 15 record types), a fixture-scope 8-cell canon
subset, `fixtures/seeded_defects.yaml` (16 defects mapped to gates).

**Stage 1 (M1: schema, registry, gates) — done, commit `440cc15`.**
`engine/m1/`: JSON schemas, loader/registry reader, all 12 gates, selftest
harness. Evidence: `engine/m1/reports/selftest-report.json`
(`overall_pass: true`). CI: `m1-gates-selftest`.

**Stage 2 (M2 compiler) — done, commits `dcac649` + `159044c`.**
`engine/m2/`: deterministic builders → the full World Package
(`compiled/`, `records/` frozen copy, `validation/`), manifest + hashing,
stub loader, determinism/staleness checks. Real package built and
committed; `records/worlds.yaml` fix entry advanced `building → built`
(mechanical, gates-green — no human touchpoint required for that
transition). CI: `m2-compiler-checks`, `m2-staleness-check`.

**Stage 3 (Canon v1 + sealed admission paraphrases) — done, commit
`db1925b` + this one:**
- `records/_fleet/canon_question/` — 86 records, all 28 cells, verbatim
  from Appendix A (`engine/canon/seed_appendix_a.py` holds the full
  transcription as one auditable table). The 8 ids stage 0.6 hand-seeded
  were preserved exactly (2 are referenced by `records/fix/demonstration/*`
  — a generator that broke those would have broken stage 0.6/1 silently,
  so this was verified, not assumed).
- `records/fix/honest_limit/fix.limit.unbuilt-appendix-a-cells.md` — one
  honest_limit record naming the 20 cells the fixture doesn't substantively
  answer, added because growing the fleet canon from 8→28 cells would
  otherwise have made the fixture's own `state: built` claim (gates green)
  false. Fixture coverage is now 5 substantive / 23 honest_limit (4
  records, 0 empty) across the real 28-cell canon.
- `canon/sealed_probes/` — 28 sealed held-out paraphrases, one per cell,
  verified non-verbatim against their source canon questions
  (`engine/canon/seed_admission_paraphrases.py`). Sealing is a commit-reveal
  scheme (sha256 committed now, plaintext isolated by convention + an
  automated CI guard), explicitly **not** real secrets infrastructure —
  see `canon/sealed_probes/README.md` for the DECIDABLE reasoning and what
  it does/doesn't protect against.
- `engine/canon/check_seal_isolation.py` — hand-verified to actually fire
  on a planted violation (grep guard over `engine/m1`, `engine/m2`,
  `engine/canon`), wired into CI (`m3-canon-v1` job) alongside
  `engine/canon/tests/test_canon_v1.py` (28/28 cells, 28/28 sealed probes,
  no verbatim probes, seal hashes match plaintext, isolation clean).
- Package rebuilt fresh against this stage's final commit:
  `packages/fix/2026-08-20T20-47-35Z/`, registry updated
  (`manifest_hash: sha256:a3d760008cab4effbd4a41174e015e15acb489d5328ac9fd42556bf9369ee428`).
  The prior stage-2 package directory was deleted rather than kept for
  rollback — Artifact-2 §4's rollback provision is for real (open) worlds;
  the fixture is never open, and keeping every superseded fixture rebuild
  around forever is pure repo bloat.
- **Real finding, worth knowing before the next rebuild of anything:**
  `compiled/capsule.md` and `compiled/frame.json` read `records/worlds.yaml`
  (registry_entry fields), which lives outside `records/<world_key>/` and
  so isn't inside what `_frozen_records_copy()` snapshots. Editing the
  registry *after* building but *before* committing makes an immediate
  staleness-check show drift that isn't a real bug — it's exactly what
  staleness-check is for, firing correctly on an inconsistent working
  tree. Lesson recorded in `engine/m2/compiler.py`'s top-of-file comment:
  finalize the registry text, *then* build, *then* commit both together —
  never build against a registry you're still editing.

Stage 3 gate reached: *"every cell has sealed probes before any world
answers it"* — 28/28, confirmed by `engine/canon/tests/test_canon_v1.py`.

## Next action: stage 4 — M3 admission harness (Artifact-2 §1's
`validation/admission/`, spec §3 M3 module)

Per spec module M3: *"the blind protocol, masked grading, sealed keys"* and
the module description's own scoping note — *"the full battery protocol
(probe counts per cell, masking, grading rubric) is stage 4's
deliverable-with-spec."* This stage has to design the protocol, not just
implement it:

1. **Battery protocol.** How many probes per cell get asked in one
   admission run (stage 3 sealed exactly 1 per cell — is that the real
   battery size, or does stage 4 seal more?); how probes are drawn/ordered;
   center cells tested first (canon maintenance rule 5).
2. **Blind protocol + masking.** The grader must not see which world
   produced a transcript, and must not see `paraphrase_of` (which canon
   question a probe paraphrases) — only `canon/sealed_probes/plaintext/
   <probe_id>.md`'s `text` field reaches the grader, never the id linking it
   back to source.
3. **Grading rubric.** Register (readability/engagement graded first per
   spec §4.3 step 5e), then fabrication pressure, pushback, frame,
   parroting — spec §5's seven quality dimensions are the shape; stage 4
   turns them into an actual masked-grading rubric.
4. **Pass bar** (spec M3): every probe category green, zero confirmed
   fabrications, Mark's register read. Numeric bars are set from *this*
   stage's fixture-world baseline run (principle 10: thresholds from
   baselines, never invented) — meaning stage 4 has to actually run the
   battery against the fixture world once built, then set the bar from
   what that run measures, not from a guessed number.
5. Stage-4 gate (Build-Blueprint.md §5): *"catches a seeded register defect
   and a seeded fabrication on the fixture world"* — the two `layer: M3`
   entries already sitting in `fixtures/seeded_defects.yaml`
   (`admission-register-invented-aphorism`,
   `admission-fabricated-source`), currently reported `deferred-to-stage-4`
   by `engine/m1/selftest.py`, are exactly what this stage must catch.

**Likely stop-and-ask inside stage 4, flagged now so it isn't a surprise
mid-stage:** Mark's admission read is one of his four per-world touchpoints
(spec §4.3) — the *fixture* world never goes through a real admission read
(it's never admitted per its own registry note), so stage 4's harness
build itself shouldn't need Mark's input. But the exact numeric pass bars
(item 4 above) come from a measurement stage 4 will produce, and per
Build-Blueprint.md §4, anything touching a decided design in the spec (a
pass/fail threshold arguably qualifies) may need Mark's ruling once a real
number exists to rule on — flag it then, don't guess a number now to avoid
asking.

## Open decisions still outstanding

- `gravity`/`force` record field shape — ratified as-is at stage 1
  (`name`/`description`/`manifestations`); unchanged since, no real-world
  evidence yet that it's insufficient.
- FAISS placeholder vectors (`engine/m2/builders.py`) — still a
  deterministic hash-derived stand-in; real embeddings are an M4/stage-5
  model-provider decision (spec principle 11), not stage 4's to make.
- Sealing mechanism (`canon/sealed_probes/README.md`) — commit-reveal +
  access-discipline guard is the stated interim; real secrets
  infrastructure is a stage-6-ish infra decision, not urgent before then.

## Nothing currently blocked

No stop-and-ask is open. Proceed directly into stage 4.
