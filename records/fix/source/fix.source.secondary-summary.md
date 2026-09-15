---
id: fix.source.secondary-summary
world_id: fixture-synthetic
record_type: source
schema_version: 2
status: ready
register: etic
canon_cells: []
confidence:
  citation_specificity: C
  verification_state: named-not-rechecked
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: null
sources: []
author: "Synthetic Summarizer B"
work: "A Later Summary of Testland Practice (fixture text)"
edition: "cic/texts/fixture-synthetic_later-summary.txt (fixture text, public domain / CC0)"
rights_status: public-domain
attribution_status: attributed-secondhand
discovery_channel: "authored for the stage-0.6 fixture"
external_ids: {}
kind: vendored
shelf_row: fixture-synthetic--later-summary
---
Secondary fixture source: lower confidence tier, used to give the fixture world's
confidence axes real spread (distribution-health gate needs variety to check, not
just a single confidence profile repeated everywhere).

Library Access Gate increment 2: `edition` now names the real vendored
fixture text (`cic/texts/fixture-synthetic_later-summary.txt`), and
`shelf_row` points at that file's own `context` row (`voice_of:
fixture-synthetic-neighbour`, `documented_exchange: confirmed`) in
`cic/corpus-map/fixture-synthetic.yaml` - the M9 selftest's clean baseline
for a voiceable non-tradition row (Mark's R-1/R-2/R-3 ruling, CM-8).
