# Build handoff note

Read `Build-Blueprint.md` first; this note is only the "where things stand"
supplement it asks for at every stage boundary / stop-and-ask / economy
checkpoint.

## Current stage: 1 complete, ready to start stage 2

**Stage 0.6 (fixture world) — done, commit `75278a2`:**
- `records/worlds.yaml` — registry with the `fix` fixture-world entry
  (`state: building`, never advances, `census_id: null`).
- `records/fix/**` — clean fixture world, all 15 per-world record types
  (Artifact-1 §4), covering 8 seeded canon cells (5 substantive, 3
  honest_limit).
- `records/_fleet/canon_question/*.md` (8 files) + `records/_fleet/
  modern_term/_fleet.modern.trinity.md` — a fixture-scope subset of the real
  Appendix A canon, real question text/ids, **not** full Canon v1 (that's
  stage 3's job, the remaining 20 of 28 cells).
- `fixtures/seeded_defects.yaml` — 16 entries mapping defects to gates.
- `fixtures/README.md` — explains all of the above.

**Stage 1 (M1: schema, registry, gates) — done, commit `440cc15`:**
- `engine/m1/schemas.py` — per-type JSON-Schema (envelope + 17 types),
  flat-merged + `additionalProperties: false` (the `unevaluatedProperties`
  behavior Artifact-1 §6 asks for, without allOf/$ref machinery — DECIDABLE,
  reason in the commit). Required-ness stays split at the envelope floor;
  type-specific requiredness lives in the completion-per-type gate, not the
  schema, per Artifact-1 §3.
- `engine/m1/loader.py` + `registry.py` — front-matter/body parsing;
  `records/worlds.yaml` as the sole registry reader (law 4).
- `engine/m1/canon.py` — valid canon cells derived from the fleet's own
  `canon_question` records, never hardcoded.
- `engine/m1/gates.py` — all 12 named gates (referential, reciprocity,
  completion-per-type, narratability, quote-recording, alias-safety,
  distribution-health, confidence-crosscheck, rights, readability,
  canon-coverage, schema-validation) plus the canon_cells-resolves and
  sentinel-string hand rules folded into referential/schema-validation.
- `engine/m1/fk.py` — DECIDABLE: self-contained vowel-group FK grade
  computation, not textstat/nltk (its cmudict backend needs a network fetch
  this environment's proxy refuses on SSRF grounds, and hermetic CI is a
  value this repo's own CI already states). Reason recorded in the commit.
- `engine/m1/mutate.py` + `selftest.py` — applies each
  `fixtures/seeded_defects.yaml` mutation to an in-memory fixture copy,
  asserts the named gate fires there and stays silent on the clean copy
  (the inertness proof); M3-scope entries deferred to stage 4.
- `engine/m1/reports/selftest-report.json` — the committed evidence:
  `overall_pass: true`. Reproduce with `pip install -r
  engine/m1/requirements.txt && python -m pytest engine/m1/tests -q` from
  repo root, or `python -m engine.m1.selftest` for the full JSON report.
- `.github/workflows/ci.yml` — additive `m1-gates-selftest` job (old
  cic-poc/cic-website jobs untouched).
- Three fixture-data bugs were found and fixed by actually running the
  selftest (not by inspection alone): confidence-crosscheck reads a
  record's own `verification_state`, not a chase through linked source
  records; `fix.term.the-three`'s `plain_meaning` was itself over FK 10 in
  the "clean" fixture; the canon-cells-exist defect was mislabeled
  `gate:schema-validation` in the catalog when it's implemented under
  `referential`. All fixed; selftest is green.

Stage 1 gate reached: *"selftest passes the clean fixture and fails every
seeded-defect fixture; inertness reporting fires."* — confirmed by
`engine/m1/reports/selftest-report.json`.

## Next action: stage 2 — M2 compiler (Artifact-2)

Build the deterministic builder: `records/fix/**` (validated, stage-1-green)
→ a World Package under `<world_key>/<package_id>/` per Artifact-2 §1
(`manifest.json`, `records/` frozen copy, `compiled/{prompt.txt, capsule.md,
chunks/, indexes/, quotes.json, figures.json, repository.json, coverage.json,
frame.json, media/}`, `validation/{gates-report.json, admission/, signoffs.json}`).

Stage 2 gate: *"determinism twice (byte-identical); staleness CI green;
manifest hash verified by a stub loader."* Concretely:
1. `manifest_hash` = sha256 over canonical-JSON manifest (Artifact-2 §2);
   every compiled file hash-listed.
2. Compile the fixture world twice from the same `records_commit`; diff the
   two outputs — must be empty.
3. A staleness CI check: recompile from `records_commit`, diff against the
   stored package.
4. A stub loader that recomputes the manifest hash at "load" time and
   refuses to serve on mismatch (Artifact-2 §2's named availability
   decision — a wrong world is worse than an absent one).
5. `retrieval/indexes/{lexicon.faiss,story.faiss}` — the fixture world is
   tiny (2 terms, 1 story); a real FAISS index is legal but may be
   overkill for stage 2's own gate. `DECIDABLE`: pick the simplest thing
   that satisfies "byte-identical on determinism-twice" and record the
   reason (a real index built deterministically vs. a stub/flat format
   deferred until a real world's retrieval needs are known at stage 7).

## Open decisions still outstanding

- `gravity`/`force` record field shape (Artifact-1 §4 doesn't specify it
  beyond `contested_claim`'s fields): the stage-1 schema ratified the
  stage-0.6 fixture's placeholder shape (`name`/`description`/
  `manifestations`) as-is — no counter-evidence appeared to justify
  changing it, so it stands as the working shape unless a real world's
  build (stage 7) shows it's insufficient.
- FAISS vs. a simpler index format for the tiny fixture world — flagged
  above for stage 2 to decide.

## Nothing currently blocked

No stop-and-ask is open. Proceed directly into stage 2.
