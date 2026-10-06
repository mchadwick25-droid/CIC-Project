# Fixture world — stage 0.6

Build-Blueprint.md §5, stage 0.6: *"Fixture world (synthetic, exercises every
gate + admission + safety script) — seeded defects enumerated and mapped to
the gates that must catch them; the firing and harness proofs land in stages
1 and 4."* This directory plus `records/fix/**`, `records/_fleet/canon_question/
_fleet.canon.{c-i,c-p,c-t,f1-i,f2-e,f5-p,f6-p,f6-t}-01.md`, and
`records/_fleet/modern_term/_fleet.modern.trinity.md` are that deliverable.

## What's here

- **`records/worlds/fix.yaml`** — registry entry for world_key `fix`. State
  advances mechanically as far as `built` (gates green, per Artifact-1 SS2 -
  no human touchpoint required for that transition) but never past it: it is
  never admitted or opened for real, and `census_id` stays `null` (not an
  Atlas entry) forever. It exists only so the pipeline (M1 gates, M2
  compiler, M3 admission, M4/M5 runtime + the live safety script) has
  something real to run against before Alexandria (stage 7) is built.
- **`records/fix/**`** — a clean, gate-passing fixture world covering all 15
  per-world record types (Artifact-1 §4): world_core, source (×2), term (×2),
  story, quote (×3, including the paraphrase-only case), figure, gravity, force,
  contested_claim, doctrinal_witness, honest_limit (×3), ambient,
  demonstration (×2, including the identity-collision case), voice_craft,
  search_record (×2, including a search that returned nothing). Plus
  world_front (×1, `fix.front.fixture-synthetic`) - deliberately minimal
  (one skim.tile unit, one orientation unit), a schema-valid example
  quoting `fix.quote.identity-collision-saying`'s own `modern_rendering`
  field correctly. Not yet exercised by a seeded defect or the M1
  selftest: `gate_quote_mark_fidelity` (engine/m1/gates.py) is implemented
  and unit-tested directly, but deliberately not yet added to GATES/
  run_all - see that gate's own registration comment for why (registering
  it changes validation/gates-report.json for every already-built world's
  committed package). No world (fixture or real) has a fully-populated
  world_front yet; content migration is a separate, later stage.
- **A fixture-scope canon subset**, 8 of the real 28 Appendix A cells (C-I,
  C-P, C-T, F1-I, F2-E, F5-P, F6-P/identity-collision, F6-T), seeded here (at
  stage 0.6) under `records/_fleet/canon_question/` using the *real* Appendix
  A question text and ids for those cells — enough to unblock fixture testing
  before the full canon existed. **Stage 3 has since seeded the other 20**
  (`engine/canon/seed_appendix_a.py`, all 86 questions across all 28 cells,
  verbatim from Appendix A); the fleet canon is complete as of stage 3. These
  8 ids were preserved exactly when stage 3 ran, since two of them
  (`_fleet.canon.c-p-01`, `_fleet.canon.f6-p-01`) are referenced by
  `records/fix/demonstration/*.md`.
- The fixture world itself stays deliberately synthetic and thin: it answers
  5 of the (now 28) canon cells substantively (doctrinal_witness, term,
  story, quote) and honest-limits the other 23 — 3 individually
  (`records/fix/honest_limit/fix.limit.{c-t-trinity-language,
  f2-e-scholarly-scrutiny, f6-t-outsiders-fate}.md`) plus one record
  covering the 20 cells stage 3 added
  (`fix.limit.unbuilt-appendix-a-cells.md`, one honest_limit naming all 20 —
  the reason is genuinely the same for all of them, so one record states it
  once rather than 20 near-duplicates). Both coverage-gate routes still get a
  real, checkable positive case (Artifact-1 §6 coverage rule: *"never
  neither, never blank"*) — now against the real, complete canon rather than
  a fixture-scope subset.
- **`fixtures/seeded_defects.yaml`** — the enumerated-and-mapped defect
  catalog: one entry per gate in the Artifact-1 §6 battery (schema
  validation/unevaluatedProperties, referential, reciprocity,
  completion-per-type, narratability, quote-recording, alias-safety,
  distribution-health, confidence-crosscheck, rights, readability,
  canon-coverage, the sentinel-string hand rule, the canon_cells-must-exist
  hand rule, and inertness itself), plus two defects scoped to stage 4's M3
  admission harness (a register defect — a coined quotable aphorism — and a
  fabrication defect — a quote citing a source that doesn't exist), exactly
  as the blueprint's stage-0.6 line calls for.

## How it gets consumed later

- **Stage 1 (M1 selftest):** for each `layer: M1` entry, apply
  `mutation` to an in-memory copy of `records/fix/**`, run the gate battery,
  and assert the named gate fails with the given reason — *and* that the same
  gate passes on the unmutated clean copy. That dual assertion, run across
  every entry, is the `inertness-proof` entry's own check: a gate that never
  fires anywhere is itself a reported failure (spec principle 12).
- **Stage 4 (M3 admission harness) — done.** The `layer: M3` entries feed the
  blueprint's stage-4 gate directly — *"catches a seeded register defect and
  a seeded fabrication on the fixture world"* — and both are caught
  (`engine/m3/reports/selftest-report.json`). The harness runs against
  `engine.m3.generation.FixtureRecordAnswerer`, a deterministic no-model
  stand-in, not a live model call — see that module's docstring for why.
- **Stage 5 (M4/M5 runtime + live safety script):** the fixture world (not
  this catalog) is the target world the live safety script runs conversations
  against. No fixture-specific safety content was added here on purpose — the
  safety call (Artifact-4 §1) takes only the participant message, a recent
  window, and the accumulator; it is world-agnostic by design, so any open
  world (including this one) is a valid target for adversarial probes.

## Why a mutation catalog instead of 12+ checked-in broken copies

`seeded_defects.yaml` is a single source of truth: one mutation, one expected
failure, applied on demand by the stage-1/4 harnesses. Checking in a dozen
full broken-world directory trees would drift from the clean fixture the
moment either changed (exactly the hand-synced-list failure mode
Build-Blueprint.md §6 names as a landmine) and would violate law 4 (one
registry; everything derived) in spirit even though it's fixture data, not
production config.
