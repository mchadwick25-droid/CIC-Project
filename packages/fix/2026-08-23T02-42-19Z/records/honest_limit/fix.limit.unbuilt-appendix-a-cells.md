---
id: fix.limit.unbuilt-appendix-a-cells
world_id: fixture-synthetic
record_type: honest_limit
schema_version: 2
status: ready
register: emic
canon_cells: [C-E, F1-E, F1-P, F1-T, F2-I, F2-P, F2-T, F3-I, F3-E, F3-P, F3-T, F4-I, F4-E, F4-P, F4-T, F5-I, F5-E, F5-T, F6-I, F6-E]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
  - {source_id: fix.source.witness-scroll, locus: "registry-wide", license: public-domain}
statement: >
  You have asked me something my fixture record was never built to answer.
  I was made from two short synthetic texts, on purpose, to test how a
  system like this one handles gates and coverage - not to speak for the
  whole shape of Christian history. On this question I have nothing
  honestly to give you.
why_sources_cannot_answer: >
  The fixture world (records/fix/**) was deliberately built to cover only
  eight of Canon v1's twenty-eight cells (see fixtures/README.md) so the
  coverage gate's two routes - substantive and honest_limit - could both be
  exercised without authoring a full synthetic canon. Once stage 3 grew the
  fleet canon to its real twenty-eight cells (records/_fleet/canon_question/,
  Appendix A), the remaining twenty cells needed real coverage of their own
  to keep the fixture's own state=built claim (Artifact-1 SS2: gates green)
  honest. One record naming all twenty is the accurate statement of the
  actual reason (uniform: out of the fixture's deliberately narrow scope),
  not twenty near-duplicate files repeating it.
nearest_material: [fix.core.fixture-world, fix.witness.who-is-jesus]
---
Added at stage 3 alongside the full Appendix A canon seed
(engine/canon/seed_appendix_a.py). Keeps records/fix/** truthfully
coverage-complete against the real 28-cell canon, the same bar any world
reaching state=built must clear (Artifact-1 SS6 coverage rule), without
pretending the fixture answers questions it was never built to answer.
