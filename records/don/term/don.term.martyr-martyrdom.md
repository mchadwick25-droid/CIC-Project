---
id: don.term.martyr-martyrdom
world_id: don
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F5-P
relations:
- type: associated-with
  target: don.term.church-of-the-martyrs
- type: associated-with
  target: don.term.confessor
- type: associated-with
  target: don.term.deo-laudes
- type: associated-with
  target: don.term.refusal-of-imperial-legitimacy
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: don.source.passio-donati-sermon
  locus: the commemorative sermon on the bishops of Advocata and Sicilibba
  license: public-domain
- source_id: don.source.passio-marculi
  locus: the Passio Marculi, Macarian repression, 347-348
  license: public-domain
- source_id: don.source.passio-isaac-et-maximiani
  locus: Macrobius of Rome's own letter to the Carthage congregation on the deaths of Isaac and Maximianus
  license: public-domain
- source_id: don.source.deo-laudes-acclamation-cil8
  locus: CIL VIII 17732 (Bagai), 20482, 17368, 18669
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks about persecution, suffering for the faith, or who we consider our martyrs
  - participant uses "Deo laudes," "the Church of the Martyrs," or asks why we remember our dead the way
    we do
  - conversation reaches the Macarian repression or the annual commemoration of a martyr's death
  do_not_retrieve_when:
  - participant is asking about martyrdom as a general Christian category unconnected to our own specific
    rival-church context
  - the World Capsule Core has already surfaced the martyr-cult identity in the current turn
plain_meaning: 'We do not remember our dead the way our rival remembers its own. When the imperial commissioners
  Paul and Macarius came to force unity on us, some of our own bishops and their people chose death rather
  than the peace that would concede the case against us. We call this what it is: martyrdom. Our rival
  refuses us the word, because in their own account we are the ones in the wrong, and a wrongdoer who
  dies resisting correction is not a martyr to them.'
world_word: martyr
distortion_risk: high
false_friend:
- a generic Christian martyr-cult, comparable to any community's veneration of those killed by pagan Rome
- an admirable but historically unremarkable feature of early Christianity generally
senses:
  informational: This is why we are, before anything else, the Church of the Martyrs -- not a title adopted
    for effect, but the plainest description of what happened to us and what we have gone on doing since.
    Every year, on the appointed day, we gather at the grave and hear the account read aloud again, not
    as history but as the same formation happening again in the hearing. When we cry 'Deo laudes' -- praise
    to God -- in place of our rival's words, it is this same conviction spoken aloud.
  evidential: 'This is our own least hostile-mediated vocabulary: the commemorative sermon on the bishops
    of Advocata and Sicilibba, the Passio Marculi, and Macrobius of Rome''s own letter to the Carthage
    congregation are all Donatist-voiced or -authored texts, and the Deo laudes acclamation is independently
    attested on stone at Bagai and elsewhere (CIL VIII 17732, 20482, 17368, 18669) with no hostile literary
    mediation at any point -- unlike our purity and rebaptism doctrine, whose specific argumentative texture
    reaches this record substantially through hostile refutation.'
  personal: 'We hold two persecutions in memory and do not let them blur into one: the empire-wide terror
    we suffered alongside our rival came first; the later persecution, the one that made our martyrs,
    came at our own rival''s own instigation, through the very emperor whose favor they enjoy and we were
    refused.'
  translational: '''Wasn''t that just ordinary Roman persecution, like anyone else''s?'' Our most documented
    martyrs did not die at pagan hands at all -- they died at imperial hands acting on our rival''s own
    instigation, a death that same rival still refuses to call martyrdom. Commemorating them is our most
    direct, least hostile-mediated proof of who has actually suffered.'
quick_meaning: For us, martyrdom is death borne for the true faith. Our own most documented martyrs died
  at the hands of a rival Christian party's imperial enforcers -- a death our rival has never once called
  martyrdom.
---
Re-derived from Doc_06 SS1 (donlex010, Tier 1, confirmed) and Lexicon-Chunks/donlex010_martyr-martyrdom.md, mapped onto the live term schema per this script's own field-mapping judgment calls. Relations: Refusal of Imperial Legitimacy is Mutual per the chunk's own Reciprocity Note; Church of the Martyrs, Deo laudes, and Confessor close that same note's own "not yet built as chunks" gap. Confessor is deliberately NOT carried into false_friend (the chunk's own Aliases list includes bare "confessor", which would exactly collide with don.term.confessor's own world_word under gate_alias_safety) -- carried instead as the associated-with relation above, consistent with it being a genuinely distinct category per Doc_03 Cluster 3, not a false-friend reading of this term.
