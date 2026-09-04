---
id: fix.term.the-three
world_id: fixture-synthetic
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: [F1-I]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
  - {source_id: fix.source.witness-scroll, locus: "1.1", license: public-domain}
retrieval:
  tier: 1
  retrieve_when: ["participant asks what this world believed about God"]
  do_not_retrieve_when: []
relations:
  - {type: associated-with, target: fix.term.the-way}
plain_meaning: "How we named Father, Son, and Spirit together. We said this before any later word for it existed."
world_word: "The Three"
false_friend: ["a hiking trail (unrelated meaning of an unrelated word - see fix.term.the-way for the real false-friend case)"]
senses:
  informational: "What we called the Three among ourselves, and how we came to speak of them together."
  evidential: "How we know the earliest way of naming this, and where the record is thin."
  personal: "What it meant to pray to Father, Son, and Spirit as one people, one hope."
  translational: "Not the word 'Trinity' - that word is later. The subject underneath it is ours; the label is not."
quick_meaning: "Father, Son, and Spirit, named together, before the later word for it."
distortion_risk: medium
---
Fleet bridge target for _fleet.modern.trinity (native_subject_map.fix). Also the
positive-case reciprocal-relation partner for fix.term.the-way (associated-with is
symmetric - both directions must be declared, which they are here in the clean copy).
