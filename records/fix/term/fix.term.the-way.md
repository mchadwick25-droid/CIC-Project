---
id: fix.term.the-way
world_id: fixture-synthetic
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: [C-I]
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
  - {source_id: fix.source.secondary-summary, locus: "2.3", license: public-domain}
retrieval:
  tier: 2
  retrieve_when: []
  do_not_retrieve_when: []
relations:
  - {type: associated-with, target: fix.term.the-three}
plain_meaning: "the name this community used for its own shared practice of life"
world_word: "The Way"
false_friend: ["a hiking or walking trail - unrelated to this world's sense, flagged so the voice never lets the modern reading slip in unglossed"]
senses:
  informational: "What we called our shared practice among ourselves."
  evidential: "How the name shows up in the record, and how sure we are of that."
  personal: "What it felt like to be named as one who walked The Way."
  translational: "Not a physical road or trail. A name for a whole way of living."
quick_meaning: "Our own name for our shared way of life together."
distortion_risk: low
---
Positive-case: retrieve_when/do_not_retrieve_when are proper empty arrays (the
sentinel rule - Artifact-1 §3 - forbids "n/a" or an em-dash here; the DEFECT
mutation replaces retrieve_when with the string "n/a"). Also the reciprocity-gate
and referential-gate positive case via its relation to fix.term.the-three; the
alias-safety and referential DEFECTs both mutate a copy of this record.
