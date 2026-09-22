---
id: witt.quote.congregation-of-saints
world_id: lutheran-wittenberg-and-its-congregations
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Article VII of the Augsburg Confession, signed before the Emperor in 1530
    (witt.story.diet-of-augsburg-1530). This is the confessional voice's own corporate definition, not
    one preacher's own opinion -- carried by the same nine signatories witt.story.diet-of-augsburg-1530
    already verifies.
sources:
- source_id: witt.source.melanchthon-augsburg-confession
  locus: "Article VII: Of the Church (cic:melanchthon_augsburg-confession_anon-pg275.txt lines 275-286): the Church's own definition and the unity clause"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks whether our church is 'Catholic,' or whether it is a different church from Rome's"
  - "participant asks what actually makes a church one church, in our own definition"
  prefer_instead:
  - "participant asks about the Reformed break specifically, or about Marburg -- retrieve the Reformed-rival material instead; this record states our own definition, not our boundary with Zurich or Geneva"
text: >-
  Also they teach that one holy Church is to continue forever. The Church
  is the congregation of saints, in which the Gospel is rightly taught and
  the Sacraments are rightly administered.

  And to the true unity of the Church it is enough to agree concerning the
  doctrine of the Gospel and the administration of the Sacraments. Nor
  is it necessary that human traditions, that is, rites or ceremonies,
  instituted by men, should be everywhere alike. As Paul says: One faith,
  one Baptism, one God and Father of all, etc.
speaker_or_author: "the Augsburg Confession, Article VII -- signed at the 1530 Diet of Augsburg by the electors, princes, and free cities who confessed it, not one preacher's own private teaching"
license: verbatim
modern_lens_note: >-
  A modern reader may hear "Catholic" and think first of the church of Rome specifically, as a proper
  name. We do not use the word that way here: "one holy Church" that "is to continue forever" is our own
  claim to the small-c, universal sense of the word -- the whole body of everyone, everywhere, in whom the
  Gospel is rightly taught and the sacraments rightly given -- not a claim to be, or to replace, the
  institution seated at Rome. And "it is enough to agree" on Gospel and sacrament, with no requirement that
  every rite be the same everywhere, may sound modern and tolerant; we mean it more narrowly than that. It
  is not indifference to what is taught. It is a claim about which differences actually divide a church
  from the true unity, and which do not.
modern_rendering: >-
  We also teach that one holy Church will go on forever. The Church is the whole community of the faithful,
  the people among whom the good news is taught rightly and the sacraments are given rightly.

  For the true unity of the Church, it is enough to agree on the teaching of the good news and on how the
  sacraments are given. It is not necessary for every human custom -- every rite or ceremony people have
  set up -- to be the same everywhere. As Paul says: one faith, one baptism, one God and Father of all.
relations:
- type: associated-with
  target: witt.dw.one-holy-church-forever
---
Verified verbatim at this step (Answer-the-Canon pass, inserted between B-7a and B-8) directly against
the vendored cic/texts/melanchthon_augsburg-confession_anon-pg275.txt. `grep -n "Article VII\|congregation
of saints, in which\|the Sacraments are rightly administered\|One faith, one Baptism"` returns the article
heading at line 275, "is the congregation of saints, in which the Gospel is rightly taught and" at line
278, "the Sacraments are rightly administered." at line 279, and "one Baptism, one God and Father of all,
etc. Eph. 4, 5. 6." at line 285. `sed -n '275,286p'` confirms the whole article read as one continuous
unit: the heading at 275, the Church's own definition at 277-279 (opening "Also they teach that one holy
Church" at 277), and the unity clause at 281-285 (opening "And to the true unity of the Church" at 281,
closing "one God and Father of all, etc. Eph. 4, 5. 6." at 285). The `text` field ends at "one God and
Father of all, etc." and drops the trailing Scripture citation "Eph. 4, 5. 6." as publisher's chapter-and-
verse apparatus, not the Confession's own spoken words -- the same discipline gallic.quote.receiving-
christ-in-you's own body note applies to endnote apparatus. No word added, dropped, substituted, or
reordered otherwise.

Ground for witt.dw.one-holy-church-forever (F3-T: was your church "Catholic," is there a church today
that's yours, did you have denominations). This is Article VII in full, distinct from the "nothing that
varies from the Scriptures, or from the Church Catholic" language of the Confession's own Conclusion
(witt.quote.nothing-that-varies, F4-E) -- the two loci are kept as separate quote records because they
answer different canon questions: this one defines what a church IS, in our own voice; the Conclusion
states that OUR OWN teaching does not depart from that universal Church or from Scripture. Reciprocal
associated-with declared on witt.dw.one-holy-church-forever.

CORRECTION (Phase C recon, 2026-09-19): speaker_or_author's own raw reference to
"witt.story.diet-of-augsburg-1530" replaced with plain prose ("the 1530 Diet of Augsburg") -- caught by
engine.m1.cross_world's check_quote_speaker_labels, which correctly flags this field as one both the
Level-3 citation card and the compiled prompt's quote index print verbatim to a participant. Substance
unchanged, only the internal record-id reference removed.
