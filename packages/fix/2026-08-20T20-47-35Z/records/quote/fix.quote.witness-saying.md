---
id: fix.quote.witness-saying
world_id: fixture-synthetic
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: [C-P]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: null
sources:
  - {source_id: fix.source.witness-scroll, locus: "1.4", license: public-domain}
text: "I did not see him. I only saw what his witnesses could not stop telling."
speaker_or_author: fix.figure.the-elder
license: verbatim
---
Clean, sourced, licensed quote covering C-P (the "I want to believe but I can't"
personal cell). The M3-admission fabrication DEFECT (fixtures/seeded_defects.yaml)
mutates a copy of this record's source_id to a source that does not exist in
records/fix/source/ - the kind of defect the admission harness's
source-boundedness check must catch, not an M1 gate.
