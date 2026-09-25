---
id: gallic.quote.benjamin-relied-on-his-own-judgment
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
    Documented as Cassian's own narration in the Second Conference, closing the story of Brother
    Benjamin as a cautionary example.
sources:
- source_id: gallic.source.cassian-conferences-part-i
  locus: "Conference II, ch. XXIV (npnf211 div iv.iv.iii.xxiv, file lines 28106-28110): Cassian's narration of Brother Benjamin's fall"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks for a cautionary example of a monk who trusted his own judgment over the Elders"
  - "participant asks what happened to a monk who broke with the tradition of the Elders"
  prefer_instead:
  - "participant asks for the whole story of Brother Benjamin's fasting dispute - this record carries only its closing moral, not the earlier narrative of the dispute itself"
text: >-
  And you doubtless remember what sort of an end there was to the life
  of this man who obstinately and pertinaciously relied on his own
  judgment rather than on the traditions of the Elders, for he forsook
  the desert and returned back to the vain philosophy of this world and
  earthly vanities.
speaker_or_author: John Cassian, narrating the fall of Brother Benjamin (Second Conference)
license: verbatim
modern_lens_note: >-
  Benjamin's fault, as Cassian frames it, was not gluttony itself but obstinacy - insisting on his own
  fasting schedule against what the Elders had handed down. The moral Cassian draws is not about food
  at all: it is that trusting private judgment over inherited tradition is what led, in the end, to
  leaving the desert altogether.
modern_rendering: >-
  And you surely remember what kind of end this man's life came to. He
  stubbornly and persistently relied on his own judgment rather than on
  the traditions of the Elders. For he left the desert and went back to
  the empty philosophy of this world and the hollow things of earth.
relations:
- type: associated-with
  target: gallic.gravity.received-not-invented
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"relied on his own judgment"` returns one hit, line 28108, inside `<div4 title="Chapter XXIV. Of the
difficulty of uniformity in eating; and of the gluttony of brother Benjamin." ... id="iv.iv.iii.xxiv">`,
itself within `<div3 title="Conference II. Second Conference of Abbot Moses." ... id="iv.iv.iii">`.
The sentence runs lines 28106-28110: "And you doubtless remember what sort of an end there was to the
life of this man who obstinately and pertinaciously relied on his own judgment rather than on the
traditions of the Elders, for he forsook the desert and returned back to the vain philosophy of this
world and earthly vanities." "This man" is Brother Benjamin, named several lines earlier in the same
chapter.

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
