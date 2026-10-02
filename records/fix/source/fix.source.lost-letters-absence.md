---
id: fix.source.lost-letters-absence
world_id: fixture-synthetic
record_type: source
schema_version: 2
status: ready
register: etic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: null
sources: []
author: "Not applicable -- this row documents an edition-level absence, not an authored work."
work: "The absence, from the Witness Scroll, of any letters from Testland's outlying households"
edition: "cic/texts/fixture-synthetic_witness-scroll.txt (fixture text, public domain / CC0)"
rights_status: "not applicable -- no text exists to hold rights over. This row's own subject is a documented absence from a vendored fixture text (what the text does NOT contain), not a held work."
attribution_status: "not applicable -- this row documents an edition-level absence, not an authored work"
discovery_channel: "authored for the stage-0.6 fixture, alongside fix.search.lost-letters-search's own searched-and-found-nothing record"
external_ids: {}
kind: absence
absence_probes:
  - "letters from the outlying households"
  - "correspondence from the borderlands"
---
Library Access Gate increment 2: the fixture world's third positive case
for `absence-probe`. `fix.search.lost-letters-search`
already documents that a search for "letters from Testland's outlying
households" came back `not_found`; this record makes that absence
mechanically checkable - the compiler reads `cic/texts/fixture-synthetic_
witness-scroll.txt` to confirm neither probe string window-matches inside
it, logs the read, and the Representative never sees the off-shelf-style
read itself. No `shelf_row`: an absence record documents what a text does
NOT contain, so there is no row for it to name (D2 SS3/C's own finding -
no derived field can exist for a row that does not).
