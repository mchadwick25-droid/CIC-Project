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
    his own description of his life before Lérins, using the soldier idiom in its negative form.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "ch. 1 [2] (npnf211 div iii.ii, file lines 12112-12119): Vincent's own account of leaving
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
  Besides, this fits well with why I chose this life. I was once caught up in the many terrible
  storms of the world's own warfare. Now, at last, under Christ's guidance, I have dropped anchor
  in the harbour of religion, a harbour that is always safest for everyone. There I hope to be
  freed from the winds of vanity and pride. By offering God the sacrifice of Christian humility, I
  hope to escape not only the shipwrecks of this present life, but also the fires of the world to
  come.
relations:
- type: associated-with
  target: gallic.gravity.soldier-of-christ
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"in the harbour of religion"` returns line 12115; read with `sed -n '12112,12120p'`, inside `<p
id="iii.ii-p13">` of `<div2 title="Chapter I..." ... id="iii.ii">` (Commonitory ch. 1). The quoted
span is one complete sentence, "Moreover, it suits well with my purpose..." through "...the flames
of the world to come.", ending at its own period; a translator's endnote citing "Ps. xlvi. 10" sits
in the preceding sentence, outside this quoted span.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
