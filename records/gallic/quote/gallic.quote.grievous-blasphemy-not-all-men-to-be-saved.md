---
id: gallic.quote.grievous-blasphemy-not-all-men-to-be-saved
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Chaeremon's own text (Conference XIII.7, read at its locus for this record) - the
    world's own refusal, stated as a rhetorical question, of any reading that limits God's saving
    will to some rather than all.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "XIII.7 (npnf211 div iv.v.iv.vii, file lines 37756-37759): the rhetorical question refusing
    a limited saving will"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why the south called a limited reading of God's saving will blasphemy"
  - "participant wants the Conference's own words on God's will for all, not a summary"
  prefer_instead:
  - "participant wants the companion refusal of the opposite extreme (free will alone) - retrieve gallic.quote.profane-notion-attribute-everything-to-free-will"
text: >-
  For if He willeth not that one of His little ones should perish, how
  can we imagine without grievous blasphemy that He does not generally
  will all men, but only some instead of all to be saved?
speaker_or_author: "Abbot Chaeremon, as Cassian records him (Conference XIII.7)"
license: verbatim
modern_lens_note: >-
  This is a rhetorical question, not a flat statement - Chaeremon reasons from a premise (God does
  not want even one of his "little ones" to perish) to a conclusion he treats as obvious: reading
  God's saving will as limited to only some people, not all, would be blasphemy. The force of the
  passage is in the logic, not just the word "blasphemy" alone.
modern_rendering: >-
  He does not want even one of His little ones to perish. So how can we imagine, without grievous
  blasphemy, that He does not want all people to be saved, but only some instead of all?
relations:
- type: associated-with
  target: gallic.force.africa-and-rome-pressure
use_note:
  means: "Cassian reports Chaeremon arguing that it would be grievous blasphemy to think God wills only some, not all, to be saved."
  not_for:
    - "a named reply to Augustine, when the text names no opponent"
    - "a teaching that all are in fact saved, when it concerns God's will"
    - "the three stages of grace, which sit in gallic.quote.chaeremon-three-stages-of-grace"
    - "a separate witness from gallic.quote.without-grievous-blasphemy-all-men-to-be-saved, which carries the same sentence"
  years: {from: 426, to: 426}
  status: reviewed
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"how can we imagine without grievous"` returns line 37758; read with `sed -n '37756,37760p'`, inside
`<div4 title="Chapter VII. Of the main purpose of God and His daily Providence." ... id="iv.v.iv.vii">`
(Conference XIII, Chaeremon's own conference). The quoted span is one complete sentence, "For if He
willeth not..." through "...to be saved?", ending at its own question mark.

Normalization: line breaks joined with single spaces; the source's own italic markup around "all"
and "some" (emphasis, not quotation) is dropped, the words themselves unchanged. No word was added,
dropped, substituted, or reordered.
