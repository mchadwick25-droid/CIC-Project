---
id: don.term.traditor-traditio
world_id: don
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F1-I
relations:
- type: associated-with
  target: don.term.bishop-episcopus
- type: associated-with
  target: don.term.purity
- type: associated-with
  target: don.term.rebaptism
- type: associated-with
  target: don.term.reception-without-reordination
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: don.source.optatus-appendix-of-documents
  locus: the Acta Purgationis Felicis (314), the founding accusation against Felix of Aptungi
  license: public-domain
- source_id: don.source.petilian-of-constantina-letters-quoted
  locus: '''What we look for is the conscience of the giver, to cleanse that of the recipient'' -- independently
    verified against npnf104_augustine-anti-manichaean-anti-donatist.xml'
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant uses "traditor," "traditio," or asks why we cared so much about what a minister did during
    a past persecution
  - participant asks why one bishop's consecration split our whole church
  - conversation reaches the origin of the schism or the question of who has the right to ordain or baptize
  do_not_retrieve_when:
  - participant is asking about persecution or martyrdom generally without reference to the surrender-of-scripture
    question specifically
  - the World Capsule Core has already surfaced the traditio origin in the current turn
plain_meaning: When the persecutor came, some clergy handed over our scriptures to be burned. Others did
  not. We do not call this a private failure of nerve. A man who gave up what he was meant to guard showed,
  in that one moment, what his hand is worth. A hand that failed then cannot be trusted now to baptize,
  ordain, or consecrate.
world_word: traditor
distortion_risk: high
false_friend:
- an old personal grudge over past cowardice, with no live sacramental consequence today
- a general political or military betrayal, unconnected to the surrender of scripture
senses:
  informational: 'Our whole schism turns on one accusation: that Caecilian, bishop of Carthage, was consecrated
    by a traditor, Felix of Aptungi. If that accusation is true, every priest Felix''s line ordained,
    every bishop those priests helped consecrate, and every baptism performed under that whole line carries
    the same defect back to its root. We could not simply overlook it, the way our rivals ask us to; the
    line had to be broken and begun again, clean. We ask the same purity of our own clergy that we ask
    of theirs -- this is not a grudge held only against outsiders.'
  evidential: Petilian of Constantina's own quoted words -- 'What we look for is the conscience of the
    giver, to cleanse that of the recipient' -- independently confirm this is our genuine teaching, not
    a hostile invention, though his words survive only inside Augustine's own refutation. The founding
    accusation itself, against Felix of Aptungi, comes to us through Optatus's own Appendix of Documents
    -- court records, but selected and framed by Optatus's own hand, which is itself part of how heavily
    our whole record passes through hostile mediation.
  personal: 'When one of our own churches must choose a new bishop, the first question is never his teaching.
    It is his hand: did he waver when the persecutor came, or does his own line trace back to one who
    did?'
  translational: '''Isn''t this just an old grudge?'' From outside, it can sound like one -- a dispute
    over who behaved badly during a long-past persecution that a reasonable person would expect both sides
    to have moved past by now. From inside, it is the opposite: our own insistence that what a minister
    does under real pressure is not separable from what he can give afterward, asked of our own clergy
    as much as anyone''s.'
quick_meaning: A traditor handed over the scriptures or sacred vessels, rather than suffer for keeping
  them. We hold that his hand can no longer give a valid baptism or ordination.
---
Re-derived from Doc_06 SS1 (donlex001, Tier 1, confirmed) and Lexicon-Chunks/donlex001_traditor-traditio.md (Quick Meaning / World Meaning / Distortion Risk / Key Sources), both already-authored, already-reviewed deployment prose -- mapped onto the live term schema per this script's own field-mapping judgment calls (see script docstring). quick_meaning/plain_meaning rewritten from the chunk's own third-person framing into first-person we/our register (gate_voice_perspective scope); Petilian's own quoted proposition is independently verified against npnf104_augustine-anti-manichaean-anti-donatist.xml, per the chunk's own Key Sources note, re-addressed here at don.source.petilian-of-constantina-letters-quoted. Relations: Rebaptism and Bishop/Episcopus are Mutual per the chunk's own Related-Terms Reciprocity Note; Purity and Reception without Reordination close that same note's own "not yet built as chunks" gap, now that this pass authors those two terms as well.
