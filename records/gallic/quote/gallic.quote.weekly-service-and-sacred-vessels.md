---
id: gallic.quote.weekly-service-and-sacred-vessels
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F5-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as Cassian's own description of a custom he locates "throughout the whole of
    Mesopotamia, Palestine, and Cappadocia and all the East," set down for a new Gallic house. The
    wording is Documented as Cassian's text (Institutes IV.19, read at its locus for this record); the
    custom's reach ("all the East") is Cassian's own generalization, not independently checked here.
    This record carries the general custom as background for the lentil-bean incident it introduces,
    not as a claim about any Gallic house's own practice.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes IV.19 (npnf211 div iv.iii.iv.xix, file lines 19172-19200): the weekly rotation of service across the East, and the handover of vessels and utensils on the Monday after the Mattin hymns"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks why monks took turns at chores, or how a monastery organized its work by the week"
  - "participant asks what happened to the tools and vessels a monk used during his week of service"
  prefer_instead:
  - "participant wants the specific incident this custom sets up - retrieve gallic.quote.three-lentils-and-the-lords-things instead, or alongside"
  - "participant is asking about Egypt specifically - Cassian places this custom in Mesopotamia, Palestine, and Cappadocia, and gives Egypt a different arrangement (Institutes IV.22, one brother as cook)"
text: >-
  throughout the whole of Mesopotamia, Palestine, and Cappadocia and all the East the brethren succeed
  one another in turn every week for the performance of certain duties ... they hand over to others who
  take their place the vessels and utensils with which they have ministered, which these receive and
  keep with the utmost care and anxiety, that none of them may be injured or destroyed, as they believe
  that even for the smallest vessels they must give an account, as sacred things, not only to a present
  steward, but to the Lord.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  A modern reader may hear a chore rota and a supply closet. Cassian means something stronger: the
  brothers keep the vessels "with the utmost care and anxiety" because they believe an account for them
  is owed "not only to a present steward, but to the Lord." An ordinary bowl or tool is treated as
  sacred property - not because it is valuable, but because the house itself is consecrated.
modern_rendering: PENDING_OPUS_RENDERING
relations:
- type: associated-with
  target: gallic.story.the-three-lentil-beans
---
Verified directly against the vendored cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml.
`grep -n "Mesopotamia, Palestine"` returns one hit, line 19173. The chapter div is `<div4 title="Chapter
XIX. How throughout Palestine and Mesopotamia a daily service is undertaken by the brethren." ...
id="iv.iii.iv.xix">` (line 19162). The first quoted clause runs lines 19172-19175 ("For throughout the
whole of / Mesopotamia, Palestine, and Cappadocia and all the East the brethren / succeed one another
in turn every week for the performance of certain / duties"); the second runs lines 19195-19200 ("they
hand over to / others who take their place the vessels and utensils with which they have ministered, /
which these receive and keep with the utmost care and anxiety, that / none of them may be injured or
destroyed, as they believe that even for / the smallest vessels they must give an account, as sacred
things, not / only to a present steward, but to the Lord"). Between them the source describes the night
vigils, the Sunday hand-off, and the foot-washing (lines 19175-19195); this is omitted here, marked
with "...", as narrative connective tissue rather than part of either quoted clause. The source
continues past "to the Lord" with ", if by chance any of them is injured through their carelessness" -
left out, ending the excerpt at a complete clause.

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single spaces.
No word was added, dropped, substituted, or reordered within either clause.

speaker_or_author is gallic.figure.cassian: this is Cassian's own narration (Institutes, third-person
description of the custom), not a quoted elder's speech.
