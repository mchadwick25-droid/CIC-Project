---
id: gallic.quote.vincent-tempests-of-secular-warfare
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
    Documented as Vincent's own text (Commonitory ch. 1 [2], read at its locus for this record) -
    his own description of his life before monastic life, using the soldier idiom in its negative
    form. Vincent does not name Lérins in this passage (he writes only of "a Monastery, situated in
    a remote grange"), and the vendored edition's own endnote 427 reports a scholarly view (Noris)
    that he may not yet have been at Lérins when he wrote it; this record does not assert Lérins.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "ch. 1 [2] (npnf211 div iii.ii, file lines 12112-12120): Vincent's own account of leaving
    secular warfare for the harbour of religion"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Vincent's own life was like before he became a monk"
  - "participant asks for the soldier idiom used as an antonym, not as praise"
  prefer_instead:
  - "participant wants Vincent's own stated reason for writing the Commonitory instead - retrieve gallic.quote.vincent-awful-expectation-of-judgment"
text: >-
  Moreover, it suits well with my purpose in adopting this life; for,
  whereas I was at one time involved in the manifold and deplorable
  tempests of secular warfare, I have now at length, under Christ's
  auspices, cast anchor in the harbour of religion, a harbour to all
  always most safe, in order that, having there been freed from the
  blasts of vanity and pride, and propitiating God by the sacrifice of
  Christian humility, I may be able to escape not only the shipwrecks
  of the present life, but also the flames of the world to come.
speaker_or_author: gallic.figure.vincent
license: verbatim
modern_lens_note: >-
  Vincent uses "warfare" here for the life he left, not the life he entered - the opposite of how
  the Institutes and Sulpitius use the same military idiom for the ascetic life itself. His own
  image is nautical, not military, for what came after: a harbour reached after tempests, not a
  battle joined.
modern_rendering: >-
  Moreover, it fits well with my purpose in taking up this life. At one time I was caught up in
  the many and wretched storms of worldly warfare. Now, at last, under Christ's guidance, I have
  cast anchor in the harbour of the religious life. It is a harbour that is always very safe for
  everyone. I did this for a purpose. There I have been freed from the blasts of vanity and pride.
  There I seek God's favour through the sacrifice of Christian humility. In this way I may be able
  to escape not only the shipwrecks of this life, but also the flames of the world to come.
relations:
- type: associated-with
  target: gallic.gravity.soldier-of-christ
- type: associated-with
  target: gallic.force.army-and-rank-before
use_note:
  means: "Vincent describes leaving the tempests of secular warfare for the harbour of religion in a remote monastery, to escape present shipwreck and future flames."
  not_for:
    - "a confirmed residence at Lerins, which this passage does not name"
    - "the soldier-of-Christ idiom for ascetic life, which Vincent here reverses and which sits in gallic.quote.institutes-opening-soldier-of-christ"
    - "Vincent's reasons for writing, which sit in gallic.quote.vincent-awful-expectation-of-judgment"
  years: {from: 434, to: 434}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"in the harbour of religion"` returns line 12115; read with `sed -n '12112,12120p'`, inside `<p
id="iii.ii-p13">` of `<div2 title="Chapter I..." ... id="iii.ii">` (Commonitory ch. 1). The quoted
span is one complete sentence, "Moreover, it suits well with my purpose..." through "...the flames
of the world to come.", ending at its own period; a translator's endnote citing "Ps. xlvi. 10" sits
in the preceding sentence, outside this quoted span.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
