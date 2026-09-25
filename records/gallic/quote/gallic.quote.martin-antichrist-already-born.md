---
id: gallic.quote.martin-antichrist-already-born
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: >-
    Documented as Gallus's own account, in Sulpitius's Dialogues (II.14, read at its locus for
    this record), of what Martin reportedly told him and his companions. Reported speech at one
    remove - Gallus's own third-person account of Martin's teaching, not a first-person quotation
    of Martin.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues II.14 (npnf211 div ii.iv.ii.xiv, file lines 4589-4608): Gallus's account of
    Martin's own teaching that Antichrist was already born and growing toward manhood"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Martin himself reportedly taught about the end times"
  - "participant asks how specific this world's expectation of Antichrist actually was"
  prefer_instead:
  - "participant wants Sulpitius's own separate inference on the same theme - retrieve gallic.quote.martin-antichrist-already-at-hand"
text: >-
  He told us, too, that there was no doubt but that Antichrist, having
  been conceived by an evil spirit, was already born, and had, by this
  time, reached the years of boyhood, while he would assume power as
  soon as he reached the proper age.
speaker_or_author: "Gallus, reporting Martin's own account, in Sulpitius's Dialogues"
license: verbatim
modern_lens_note: >-
  This is Gallus's own retelling of what Martin taught, not Martin's words in direct quotation -
  the passage's own surrounding text makes clear "he" throughout refers to Martin, questioned by
  Gallus and his companions about the end of the world.
modern_rendering: >-
  He also told us there was no doubt that Antichrist, conceived by an evil spirit, was already
  born. By this time he had reached boyhood. He would take power as soon as he reached the proper
  age.
relations:
- type: associated-with
  target: gallic.gravity.judgment-imminent-present
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"reached the years of boyhood"` returns line 4606; read with `sed -n '4589,4608p'`, inside `<div4
... id="ii.iv.ii.xiv">` (Chapter XIV). The surrounding paragraph opens "But when we questioned him
concerning the end of the world, he said to us..." - "him"/"he" is Martin, per the preceding
chapter's own subject. The quoted span is one complete sentence, "He told us, too..." through
"...reached the proper age.", ending at its own period.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.

speaker_or_author is a plain string, not gallic.figure.martin: the words are Gallus's own
third-person account of what Martin told him, not a direct quotation attributed to Martin.