---
id: gallic.quote.cassian-archebius-expelled-from-monastic-system
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Documented as Cassian's own narration (Conference XI.2, read at its locus for this record) -
    his own report of how Archebius himself spoke of his election, in Cassian's own indirect
    speech, not a direct quotation of Archebius's own words.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "XI.2 (npnf211 div iv.v.ii.ii, file lines 36807-36823): Cassian's own narration of
    Archebius's election as Bishop of Panephysis and how he himself spoke of it"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how an Egyptian anchorite spoke of being made bishop"
  - "participant wants Cassian's own words for Archebius's case, not a paraphrase"
  prefer_instead:
  - "participant wants Cassian's own dedications naming the shift from monk to bishop directly - retrieve a monk-bishop force/gravity record's own citations"
text: >-
  (for he vowed that he had not been summoned to that office as fit
  for it, but complained that he had been expelled from the monastic
  system as unworthy of it because though he had spent thirty-seven
  years in it he had never been able to arrive at the purity so high a
  profession demands)
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  This is a parenthetical inside a much longer sentence introducing Bishop Archebius - Cassian's own
  report of how Archebius spoke of his own election, in Cassian's indirect speech ("he vowed...but
  complained"), not a direct quotation from Archebius himself. The parentheses are the source's own;
  nothing outside them is carried here.
modern_rendering: >-
  He insisted that he had not been called to that office as someone fit for it. Instead, he
  complained that he had been expelled from the monastic way of life as someone unworthy of it. The
  reason, he said, was that even in thirty-seven years there he had never been able to reach the
  purity that so high a calling demands.
relations:
- type: associated-with
  target: gallic.gravity.monk-bishop
use_note:
  means: "Cassian reports that Archebius denied being fit for the episcopate and complained he had been expelled from the monastic life as unworthy after thirty-seven years."
  not_for:
    - "Archebius's own direct speech, when it is Cassian's indirect report"
    - "a separate passage from gallic.quote.archebius-carried-off-to-panephysis, whose sentence already contains this parenthesis"
    - "a claim that all monk-bishops felt their office as a loss"
  years: {from: 426, to: 426}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"expelled from the monastic system"` returns line 36822; read with `sed -n '36805,36825p'`, inside
`<div4 title="Chapter II. Of Bishop Archebius." ... id="iv.v.ii.ii">` (Conference XI). The sentence
introducing Archebius is one long sentence running from "And when we arrived there..." through
"...had brought him," and continuing past a semicolon into Archebius's own direct welcome to the
visitors - a parenthetical aside on how Archebius spoke of his own election sits inside it. This
record carries only that parenthetical, "(for he vowed..." through "...profession demands)",
bounded by the source's own opening and closing parentheses, not the surrounding sentence about the
journey to Thennesus or Archebius's own welcome that follows it.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
