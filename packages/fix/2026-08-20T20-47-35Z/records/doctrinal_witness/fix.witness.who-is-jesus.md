---
id: fix.witness.who-is-jesus
world_id: fixture-synthetic
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells: [C-I]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
  - {source_id: fix.source.witness-scroll, locus: "1.1-1.3", license: public-domain}
retrieval:
  tier: 1
  retrieve_when: ["participant asks who Jesus was to this world"]
  do_not_retrieve_when: []
positions: ["The Elder is remembered as the one who could not stop telling what he had received from others who saw."]
tensions: ["The scroll does not say whether the Elder himself ever saw; it records only that he would not stop repeating what witnesses told him."]
text: >
  We did not claim to have seen him ourselves. We claimed only that the ones who
  told us could not be talked out of what they had seen, and that this was worth
  our lives changing because of it.
---
Substantive coverage for the CENTER cell C-I; the highest-priority cell per
Appendix A canon maintenance rule 5 (tested first at every admission). Also the
confidence-crosscheck DEFECT target: the clean copy legitimately has
formation_confidence=Documented, divergence_note=null, and its own
verification_state=verified-direct; the DEFECT mutates a copy's
verification_state to named-not-rechecked while leaving formation_confidence
and divergence_note untouched, which the crosscheck must catch as a
now-unjustified null divergence_note (Artifact-1 §3).
