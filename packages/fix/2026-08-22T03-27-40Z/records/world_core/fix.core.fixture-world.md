---
id: fix.core.fixture-world
world_id: fixture-synthetic
record_type: world_core
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
  - {source_id: fix.source.witness-scroll, locus: "front matter", license: public-domain}
time_window: {start: 100, end: 100}
horizon: "A single synthetic year, Testland. No real time or place - built only to exercise every gate, builder, and admission check before a real world is built."
formation_logic: "The fixture is deliberately thin: eight canon cells carry real content (five substantive, three honest_limit) so both coverage routes are exercised; everything else is absent on purpose, not by oversight."
thinness: "Synthetic. Thin everywhere except the eight seeded canon cells (see fixtures/README.md)."
cautions: "Never treated as a real world: state in records/worlds.yaml advances only as far as 'built' (a mechanical, gates-green transition), census_id is null, and it never enters admission for real. It is the target of the stage-5 live safety script and the stage-1/4 gate and admission selftests."
---
The fixture world exists solely to prove the pipeline (M1-M5) against known-good and
known-bad data before any real world (Alexandria) is built. See fixtures/README.md
for how records/fix/** and fixtures/seeded_defects.yaml work together.
