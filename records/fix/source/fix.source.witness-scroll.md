---
id: fix.source.witness-scroll
world_id: fixture-synthetic
record_type: source
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
sources: []
author: "Synthetic Author A"
work: "The Witness Scroll (fixture text)"
edition: "Fixture Edition 1"
rights_status: public-domain
attribution_status: attributed
discovery_channel: "authored for the stage-0.6 fixture, not a real archival source"
external_ids: {}
---
Primary fixture source: clean, public-domain, verified-direct. The rights-gate
DEFECT (fixtures/seeded_defects.yaml) mutates a copy of this record's
rights_status; the confidence-crosscheck DEFECT mutates a copy of this record's
verification_state while the citing record's formation_confidence stays Documented.
