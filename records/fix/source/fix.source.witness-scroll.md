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
edition: "cic/texts/fixture-synthetic_witness-scroll.txt (fixture text, public domain / CC0)"
rights_status: public-domain
attribution_status: attributed
discovery_channel: "authored for the stage-0.6 fixture, not a real archival source"
external_ids: {}
kind: vendored
shelf_row: fixture-synthetic--witness-scroll
---
Primary fixture source: clean, public-domain, verified-direct. The rights-gate
DEFECT (fixtures/seeded_defects.yaml) mutates a copy of records/fix/source/
fix.source.secondary-summary.md's rights_status.

Library Access Gate increment 2: `edition` now names the real vendored
fixture text (`cic/texts/fixture-synthetic_witness-scroll.txt`), and
`shelf_row` points at that file's own `tradition` row in
`cic/corpus-map/fixture-synthetic.yaml` - the M9 selftest's clean baseline
for `source-kind`, `shelf-row` and `verbatim-in-shelf` all passing on this
record's own citing quotes.
