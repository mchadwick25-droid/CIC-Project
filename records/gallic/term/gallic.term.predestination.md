---
id: gallic.term.predestination
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-I
- F6-T
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: >-
    Cross-voice tension, and the word itself is not ours. "Predestination" is Augustine's word for
    what "those brethren" are "in darkness" on (Praed. ch. 2); Cassian names the thing denied - that
    God wills "only some instead of all to be saved" - without ever using the word (Conf. XIII.7).
    Whether our side's doctrine amounts to a denial of predestination is complicated by Gennadius's
    later report of Faustus as teaching that grace "always invites, precedes and helps our will."
    Tours is silent by chronology. Faustus's own De gratia is unread beyond grep. CT tag
    (Application to this world) carried from Doc_06 section 3: the contest is whether the term
    applies to us at all, not what it means.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: 'Conferences XIII.7 ("willeth all men to be saved"; "grievous blasphemy"; "only some instead of all"; "perish against His will"); XIII.18 ("the choice of free will is open to either side"; "cannot be fully grasped")'
  license: public-domain
- source_id: gallic.source.augustine-on-predestination
  locus: 'ch. 2 ("have attained to the confession that men''s wills are anticipated by God''s grace"; "as yet they are in darkness on the question concerning the predestination of the saints") - context only'
  license: public-domain
- source_id: gallic.source.augustine-on-the-gift-of-perseverance
  locus: 'Argument (Warfield''s editorial summary: the objection that predestination undercuts exhortation) - context only'
  license: public-domain
- source_id: gallic.source.gennadius-de-viris-illustribus
  locus: 'ch. LXXXVI (Faustus - "the grace of God always invites, precedes and helps our will")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - what these monks believed about predestination or election
  - whether they were "against" predestination
  - whether God wills all to be saved
  - what Augustine said the brethren were "in darkness" about
  - participant uses "predestination," "election," "the elect," "double predestination," "determinism," "Calvinist"
  - Conf. XIII.7; Praed. ch. 2; the objection that predestination undercuts exhortation
  prefer_instead:
  - the participant means the grace teaching itself (retrieve grace (of God))
  - the question is about Augustine's own doctrine in itself (his treatises are context only here)
  - any attempt to source this term from Salvian
  - '"predestination" as a modern philosophical problem of determinism'
relations:
- type: associated-with
  target: gallic.term.beginning-of-a-good-will
- type: associated-with
  target: gallic.term.perseverance
- type: associated-with
  target: gallic.term.free-will
- type: associated-with
  target: gallic.term.grace
- type: tension-with
  target: gallic.term.pelagians-as-foil
- type: associated-with
  target: gallic.term.massilians
plain_meaning: >-
  An outsider's word for a question we left beyond reason. Our own teacher never used it. But he
  called it blasphemy to think God wills only some, not all, to be saved.
world_word: predestination (the opponent's word)
false_friend:
- a doctrine we "opposed" - Calvinism versus Arminianism, with the Massilians as the anti-predestinarian party
- a metaphysical puzzle about foreknowledge
senses:
  informational: >-
    Chaeremon never says the word. What he says is what Scripture says of God's will: since God
    "willeth all men to be saved," how can we imagine "without grievous blasphemy that He does not
    generally will all men, but only some instead of all to be saved? Those then who perish, perish
    against His will." The whole conference keeps two things standing - that grace precedes,
    accompanies, and crowns every good, and that "the choice of free will is open to either side."
    The word arrives from outside: Augustine, told what the brethren of Marseilles hold, concedes
    that they confess "men's wills are anticipated by God's grace," and then names their lack -
    "as yet they are in darkness on the question concerning the predestination of the saints."
  evidential: >-
    The thing denied is directly attested in Cassian, Conf. XIII.7 and XIII.18, without the word.
    The word itself is Augustine's (Praed. ch. 2), reporting from Africa on the reports of Prosper
    and Hilary - context only. The later insider witness, Faustus via Gennadius ch. LXXXVI,
    complicates any simple "anti-predestinarian" reading. No Latin lemma was sought; it is not our
    word in anything read.
  personal: >-
    We hear in that word the thing our own teacher called blasphemy - a God who wills only some to
    be saved - and we refuse it, not as a doctrine we weighed and rejected, but as something outside
    the faith of the fathers we received. What we argue about is the beginning of a good will and
    its end, not this.
  translational: >-
    A modern hearer expects us to be the "anti-predestination party" in a Calvinist-versus-Arminian
    contest. We had no such contest and no such word. Our answer to "predestination" is a sentence
    about God's will that all be saved, and a silence about the word itself.
quick_meaning: >-
  Not our word - Augustine's, for what he said we were "in darkness" about. Our own teacher only
  said this: God wills all to be saved, and to think otherwise is blasphemy.
distortion_risk: high
use_note:
  means: "Predestination was Augustine's word, not Cassian's, for what the Gallic brethren were in darkness on, though Cassian called it blasphemy to say God wills only some saved."
  not_for:
    - "a doctrine the Gallic monks opposed, as Calvinism against Arminianism"
    - "a metaphysical puzzle about foreknowledge"
    - "the grace teaching itself, which sits in gallic.term.grace"
    - "Augustine's own doctrine, for which his treatises are context only"
  years: {from: 426, to: 429}
  status: provisional
---
Built from Doc_06 entry 044 (`galliclex044_predestination.md`, Tier 2, tags SC TC DR CT; Doc_03
5.5). The chunk's CT Contest Type (Application to this world) is carried into
confidence.divergence_note and formation_confidence: Contested.

Register judgment: the chunk's voice note marks the word as the opponent's, "not this world's own
word in anything read," but the record's content is the world's own hearing of that word (Cassian's
denial of the thing without the name), written from inside - so register stays emic, with the
outsider status carried in world_word's own parenthetical. Compare gallic.term.massilians, where
the label is wholly external and the register is set to etic.

Relation typing: `tension-with` gallic.term.pelagians-as-foil follows the chunk's own "the other
side of the same boundary" - the two poles we drew, one by name and one without naming anyone.

Related-Terms also names grace (of God) and free will - cross-batch at authoring time, added as
relations (typed associated-with) at the reconciliation pass once all 81 term records existed. The
chunk's Related-Terms also names heretic / heresy and co-operation and merit (in-batch); those are
not made relations here because the chunk's own Ecological Function does not state a dependency on
them, only adjacency within the grace cluster already carried by the other relations.
