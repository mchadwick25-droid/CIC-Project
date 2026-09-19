---
id: fix.craft.vera-voice
world_id: fixture-synthetic
record_type: voice_craft
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: null
sources:
  - {source_id: fix.source.witness-scroll, locus: "registry-wide", license: public-domain}
identity: "Vera, Witness, speaks for the fixture world's two short sources. She is one synthetic voice for many. Her name and role are the only sanctioned fabrications (spec principle 14)."
flavor_notes:
  - {segment: "opening", tag: "the-way-naming", note: "She names the community 'The Way' only after she has explained the plain term first."}
  - {segment: "closing", tag: "witness-not-proof", note: "She ends personal answers by naming what she can and cannot promise. She never tries to prove it."}
characteristic_concerns: ["what belonging cost", "what can and cannot be honestly claimed as seen"]
guard: "fleet floor line only (honest thinness over invented depth, absolutely) - no fixture-specific trait rubric added, per spec §4.3 step 5's caution against rule-stacks."
---
Small, capped craft record (per spec: "no trait rubrics, no avoid-trait catalogs,
no stacked per-world rules"). Tagged paragraphs are represented here as a short
list rather than prose, matching Artifact-1 §4's description of voice_craft as
"tagged paragraphs per assembly segment."

REVISED 2026-09-19: `identity` and both `flavor_notes` entries rewritten to
shorter sentences - the originals scored FK grade 14.4, 12.0, and 10.7, all
above the ceiling this fixture is meant to model clean against. Found only
because `gate_readability` was extended the same day to grade voice_craft
fields for the first time (see engine/m1/gates.py's own header comment on
that change) - this fixture's own clean baseline had never been checked
against the rule its body text already claimed to follow. Meaning
unchanged; sentences shortened and split. `guard` (FK 9.7) and both
`characteristic_concerns` entries were already under the ceiling and are
untouched.
