# Build handoff note

Read `Build-Blueprint.md` first; this note is only the "where things stand"
supplement it asks for at every stage boundary / stop-and-ask / economy
checkpoint.

## Current stage: 0.6 complete, ready to start stage 1

**Stage 0.6 (fixture world) — done, committed on `build/phase-1`:**
- `records/worlds.yaml` — registry with the `fix` fixture-world entry
  (`state: building`, never advances, `census_id: null`).
- `records/fix/**` — clean fixture world, all 15 per-world record types
  (Artifact-1 §4), covering 8 seeded canon cells (4 substantive, 4
  honest_limit).
- `records/_fleet/canon_question/*.md` (8 files) + `records/_fleet/
  modern_term/_fleet.modern.trinity.md` — a fixture-scope subset of the real
  Appendix A canon, real question text/ids, **not** full Canon v1 (that's
  stage 3's job, the remaining 20 of 28 cells).
- `fixtures/seeded_defects.yaml` — 16 entries: one per Artifact-1 §6 gate
  (13 M1 gates/hand-rules + the inertness meta-check) plus 2 M3-admission
  defects (register / fabrication), each naming the exact record, mutation,
  and expected failure.
- `fixtures/README.md` — explains all of the above and how stages 1/4/5
  consume it.

No code exists yet — stage 0.6 is data + a mutation catalog only, per the
blueprint's own gate for this stage ("seeded defects enumerated and mapped
... firing proof lands in stages 1 and 4").

## Next action: stage 1 — M1 (schema, registry, gates), Artifact-1

Build, in order:
1. Per-type JSON-Schema for all 15 per-world + 2 fleet record types
   (Artifact-1 §3-4), `unevaluatedProperties: false`.
2. A loader that walks `records/<world_key>/<record_type>/*.md`, parses the
   YAML front matter + body, validates against the per-type schema.
3. The registry reader (`records/worlds.yaml`) — the test from Artifact-1 §2
   that the runtime/tooling reads world facts from the registry alone (no
   world identifier hardcoded anywhere).
4. The gate battery itself: referential, reciprocity, completion-per-type,
   narratability, quote-recording, alias-safety, distribution-health,
   confidence-crosscheck, rights, readability, canon-coverage, inertness —
   plus the sentinel-string and canon_cells-exists hand rules.
5. The selftest harness described in `fixtures/README.md`: for each
   `layer: M1` entry in `fixtures/seeded_defects.yaml`, mutate an in-memory
   copy of `records/fix/**`, run the gates, assert the named gate fails with
   the given reason on the mutated copy AND passes on the clean copy. Commit
   the run's report as evidence (gate — spec: a stage's gate is evidence in
   the repo, never an assertion).

Stage 1 gate to reach before stage 2: *"selftest passes the clean fixture and
fails every seeded-defect fixture; inertness reporting fires."*

## Open decisions taken so far (recorded per law 14 — see commit)

- Language/stack for the M1 tooling: **not yet chosen** — first decision of
  stage 1, `DECIDABLE` per Build-Blueprint.md §4 (library/implementation
  choices), record the reason in that commit.
- `gravity`/`force` record field shape: Artifact-1 §4 only specifies
  `contested_claim`'s fields explicitly. The fixture used a minimal
  placeholder shape (`name`/`description`/`manifestations`) for
  `fix.gravity.*` and `fix.force.*`, flagged in-body as fixture-only, not
  normative. Stage 1 should either ratify this shape or replace it — either
  way, record the reason in the commit (gate-integrity rule, law 12, applies
  to schema shape decisions too).

## Nothing currently blocked

No stop-and-ask is open. Proceed directly into stage 1.
