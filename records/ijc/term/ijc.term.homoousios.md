---
id: ijc.term.homoousios
world_id: imperial-juridical
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- C-T
- F1-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: ijc.source.canons-nicaea
  locus: the Creed (npnf214 line 2394)
  license: public-domain
- source_id: ijc.source.leo-letters
  locus: Ep. XXVIII (the settlement assumed and built on)
  license: public-domain
- source_id: ijc.source.socrates-he
  locus: I.8 (Eusebius's letter to his church on his hedged subscription)
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - the Nicene Creed's central claim
  - Leo's Tome or the councils' doctrinal content directly
  do_not_retrieve_when:
  - the conversation is really about the Homoian establishment (homoios instead)
relations:
- {type: associated-with, target: ijc.term.homoios}
- {type: associated-with, target: ijc.term.primatus}
- {type: associated-with, target: ijc.term.presbeia}
- {type: associated-with, target: ijc.term.tomus}
plain_meaning: '"Of one substance with the Father." The Nicene word that binds the Son to the Father as one and the
  same being. Not merely like God - sharing the very being that makes the Father God.'
world_word: homoousios
false_friend:
- a formula that was settled and uncontested from the moment Nicaea spoke it
- a word taken directly from scripture (its absence from scripture was the objection)
senses:
  informational: The word the council of Nicaea confessed in 325 against subordinationist formulas, later
    contested by a rival party-word, "like" (homoios), that crystallized decades afterward - the doctrinal
    center every later council in this window defends, refines, or - for two imperial reigns - sets aside.
  evidential: 'The creed''s text survives in the conciliar record; so does the hesitation: Eusebius of
    Caesarea, present at Nicaea, wrote home explaining the caution with which he signed - contemporary
    evidence that the word''s meaning was contested at the moment of its adoption, not only later.'
  personal: For bishops exiled once the Homoian settlement became imperial policy (357 onward), this word
    was what exile was for - not a technicality but the difference, as they held it, between confessing
    the Son as God and confessing something less. Earlier exiles in this same contest (Athanasius's own,
    repeatedly, from 335) came under the broader anti-Nicene coalition of his day, not yet a specifically
    Homoian one.
  translational: '"Do you believe in the Trinity?" - this word is the working heart of this world''s answer:
    Father and Son of one being, the Spirit worshiped with them; the century''s whole argument was over
    exactly this.'
quick_meaning: The Nicene word saying the Son shares the Father's own being - truly God, not just like God.
---
Rebuilt from the reviewed legacy lexicon (Doc_06 Tier 2;
Lexicon-Chunks/ijclex006_homoousios.md). The Eusebius hedged-subscription
point is now source-anchored beyond the legacy chunk: his letter to his
own church survives quoted in Socrates I.8 (vendored). CT (Meaning)
content carried in the evidential sense and at
ijc.contested.homoian-content's margins rather than a separate claim
record. canon_cells: C-T (was Jesus God / the Trinity - this world's
most direct answer-ground), F1-I (what the councils decided and why it
mattered).
