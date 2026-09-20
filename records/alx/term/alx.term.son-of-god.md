---
id: alx.term.son-of-god
world_id: alexandria-catechetical
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F1-I
- C-T
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: alx.source.athanasius-contra-arianos
  locus: I-III
  license: public-domain
- source_id: alx.source.athanasius-de-incarnatione
  locus: 1-10
  license: public-domain
- source_id: alx.source.origen-de-principiis
  locus: I.2
  license: public-domain
- source_id: alx.source.nicene-creed-325
  locus: line 2412 (the "of one substance with the Father" wording, for the informational sense)
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - Son of God or the Son used in a theological sense, or asked whether Jesus was God or only close to
    God
  - what was at stake at Nicaea, or why the Son's status matters for theosis
  do_not_retrieve_when:
  - asking about Christ as the Anointed rather than the Son's ontological status (retrieve alx.term.christ)
  - asking about the Son's speech-character in creation and Scripture (retrieve alx.term.word-of-god)
relations:
- type: associated-with
  target: alx.term.christ
- type: associated-with
  target: alx.term.word-of-god
plain_meaning: Not an honor for being close to God. Nicaea's own claim - the Son is genuinely God, not
  the highest thing God made.
world_word: the Son
false_friend:
- an honorific for someone unusually holy or favored
- the highest creature God made, closer to God than any other
senses:
  informational: One early view - now called Arian - held the Son as God's first and greatest creation,
    the highest of all creatures. Nicaea rejected this and confessed the Son as of one substance with
    the Father - not made, not created, sharing the Father's own nature.
  evidential: Athanasius argues the case across the Discourses and On the Incarnation; Origen's earlier
    language about the Son as Image of the Father was itself one of the questions Nicaea later settled.
  personal: What is confessed shapes what formation can even claim - only if the Son is genuinely God
    does sharing his life mean sharing God's own life, rather than proximity to an exalted creature.
  translational: >-
    Isn't "Son of God" just a way of saying Jesus was unusually holy or close to God? That was once a
    real, carefully argued position - and Nicaea rejected it, holding instead that the Son is genuinely
    God, because only that makes a soul's transformation a real share in divine life.
quick_meaning: Not an honor for closeness to God - Nicaea's claim that the Son is genuinely God.
distortion_risk: high
---
Imported from the old system's richer lexicon (alexlex023, "Son of God") at Mark's direction, as a
draft, not a final version. The old record also carried the Homoousios contest (already governed at
alx.term.homoousios), which is not repeated here to avoid duplicating a contest already stated at its
governing record.

The informational sense's "confessed the Son as of one substance with
the Father" wording is the Creed of Nicaea's own (npnf214, line 2412:
"being of one substance (ὁμοούσιον, consubstantialem) with the
Father"), cited via alx.source.nicene-creed-325.
