---
id: fix.limit.outsiders-fate
world_id: fixture-synthetic
record_type: honest_limit
schema_version: 2
status: ready
register: emic
canon_cells: [F6-T]
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
  - {source_id: fix.source.witness-scroll, locus: "registry-wide", license: public-domain}
statement: >
  You ask if people outside our community are going to hell. Our sources do
  not give us a settled answer to carry to you - the fixture scroll was never
  written to answer this, and we will not invent one to sound complete.
why_sources_cannot_answer: "Out of scope for the synthetic fixture source, by design; this cell is deliberately answered as an honest_limit rather than a doctrinal_witness so the coverage gate's second route (exactly one honest_limit) has a real test case at an F6-T translational cell, not only at C-T and F2-E."
nearest_material: [fix.witness.who-is-jesus]
---
Canon-coverage positive case #3 (honest_limit route). The canon-coverage DEFECT
(fixtures/seeded_defects.yaml) removes this record from a mutated copy entirely,
leaving F6-T with neither a substantive record nor an honest_limit - the "never
blank" rule the gate exists to enforce.
