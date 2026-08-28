---
id: ijc.quote.jerome-damasus-verses
world_id: imperial-juridical
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- F3-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: ijc.source.jerome-de-viris
  locus: ch. 103 (npnf203 lines 41382-41386)
  license: public-domain
text: Damasus, bishop of Rome, had a fine talent for making verses and published many brief works in
  heroic metre. He died in the reign of the Emperor Theodosius at the age of almost eighty.
speaker_or_author: "Jerome, De Viris Illustribus 103"
license: verbatim
modern_lens_note: >-
  'Heroic metre' names a specific ancient verse form (dactylic hexameter), not a genre label in any
  modern sense of 'heroic.'
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how Rome advanced its own standing"
  - "participant asks what a bishop did with the tombs of the martyrs"
  do_not_retrieve_when: []
relations:
- {type: illustrates, target: ijc.figure.damasus}
---
Text verified verbatim against the vendored file 2026-08-21. A
contemporary's entire notice - two sentences, from a man who had worked
in Damasus's own chancery. The build's best quotable witness to the
verse-inscription program, since no public-domain English of the
epigrams themselves exists (ijc.search.damasus-epigrams-english).
Corrected at review (Opus canon-structure pass, 2026-08-21): canon_cells
emptied - this quote names no inscription, archaeology, or evidential
method, so an F5-E tag was a loose association; its real and sole job
is corroborating ijc.figure.damasus (F5-E stays covered by
ijc.term.basilica and ijc.term.martyrium).

FIXED 2026-08-26 (cross-world transparency audit): speaker_or_author
used to carry "(licensed for this world's figure notices only)" - a
build-team scope note rendered verbatim to the participant as this
quote's speaker line. The speaker line now just names Jerome and the
locus. NARROW LICENSE: this quote is licensed for use as figure-notice
material specifically, not for reuse as general testimony elsewhere.

CELL ASSIGNED 2026-08-27; the record had none and sat outside coverage.
F3-I asks who held authority and how anyone came to have it. Damasus setting
his own verses over the martyrs' tombs is Rome making that claim in stone,
and it is one of this world's clearest instances of it.
