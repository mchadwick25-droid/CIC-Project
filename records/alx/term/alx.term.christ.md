---
id: alx.term.christ
world_id: alexandria-catechetical
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- C-I
- C-T
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: alx.source.clement-stromateis
  locus: I.5
  license: public-domain
- source_id: alx.source.origen-comm-john
  locus: I
  license: public-domain
- source_id: alx.source.athanasius-de-incarnatione
  locus: 1-3, 54
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - Christ used as though it were Jesus's surname, or asked what the title itself means
  - how Christ's death and resurrection connect to the soul's formation
  prefer_instead:
  - asking about the Son's status as fully God specifically (retrieve alx.term.son-of-god)
  - asking about Scripture as the Word's living address (retrieve alx.term.word-of-god)
relations:
- type: associated-with
  target: alx.term.son-of-god
- type: associated-with
  target: alx.term.word-of-god
plain_meaning: Not a surname added to Jesus, but a confession - the Anointed One, sent to be priest,
  king, and prophet all in one person.
world_word: the Christ
false_friend:
- Christ used as Jesus's last name
- a vague title of general holiness
senses:
  informational: In Israel's practice, anointing was a commission - priests were anointed to mediate,
    kings to govern, prophets to speak God's word. To confess Jesus as the Christ is to confess that he
    is commissioned as all three at once, in their fullness, and not as an honor added afterward.
  evidential: Clement reads Christ as the one the whole scriptural and philosophical inquiry was moving
    toward; Origen reads the Christ as the Logos incarnate, meeting each soul according to its need;
    Athanasius reads Christ's death and resurrection as what actually reverses sin and death.
  personal: The catechumen is not being formed toward an idea but toward a person confessed as Anointed -
    the one their reading, their prayer, and their community life are already organized around.
  translational: >-
    Isn't "Christ" just how Jesus's name is usually said in full? This world heard a confession staked on
    a claim: that this is the one commissioned to mediate, govern, and speak for God, and that a life is
    now organized around him, not merely informed about him.
quick_meaning: Not Jesus's last name - the confession that he is priest, king, and prophet in one person.
distortion_risk: high
use_note:
  means: "Christ was a confession that Jesus is the Anointed One, commissioned as priest, king, and prophet in one person, not a surname."
  not_for:
    - "treating Christ as Jesus's surname"
    - "reducing it to a vague title of general holiness"
    - "presenting Clement, Origen, and Athanasius as holding one identical reading of Christ"
  years: {from: 180, to: 373}
  status: reviewed
---
Imported from the old system's richer lexicon (alexlex022, "Christ") at Mark's direction, as a draft,
not a final version. The old record also carried the Homoousios contest (already governed at
alx.term.homoousios) since the Christ confession itself asserts the Son's consubstantiality; that
material is not repeated here to avoid duplicating a contest already stated at its governing record.
