---
id: hallex08
world_id: hieronymian-ascetic-literary
record_type: term
schema_version: 1
jobs:
- 1
- 2
- 4
- 6
register: emic
review_state: draft
cache_stability: static
term: Origenism (the Origenist controversy)
aliases:
- The Origenist controversy
- the Rufinus dispute
quick_meaning: The theological dispute over Origen of Alexandria's teachings that split this community
  from a former close friend and from a bishop, in the 390s.
world_meaning: 'This world had, without quite meaning to, inherited a good deal of its own way of reading
  scripture from a teacher whose specific conclusions — about souls existing before birth, about what
  the resurrected body actually is — it later needed to renounce, urgently and publicly, once the wider
  church turned against them. This was not comfortable. It meant a former friend, once close enough to
  translate the same texts together, became the fiercest of opponents; it meant a bishop under whom this
  world''s own community technically lived became someone to be maneuvered against rather than simply
  obeyed. The controversy was not only, or even mainly, about doctrine in the abstract — it was about
  which teacher''s account of Jerome''s own faithfulness would be believed.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: Anchors G6 (Supporting gravity); reshapes the *Hebraica veritas*
  project (the Augustine dispute is a downstream test of related textual-authority commitments) and *patrocinium*
  (conducted through, and threatening, the patronage network — Pammachius and Marcella are named addressees
  of Jerome''s own polemic).'
distortion_risk: '**Modern Hearing:**

  Risk of reading this as a purely abstract theological disagreement, missing its personal and political
  stakes.


  **World Hearing:**

  A rupture that was simultaneously doctrinal, personal, and political — the three were not separable
  within it.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about Jerome and Rufinus
  - participant asks about Origen's influence on this world
  - participant asks about the community's break with a former friend or with Bishop John of Jerusalem.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL005
  author_gravity_note: 'Rufinus''s *Apologia contra Hieronymum* (401) and Jerome''s *Apologia adversus
    Rufinum* (401–403). Author Gravity note: both sides are adversarial; neither account of the dispute''s
    substance is privileged over the other.'
period_sense: 'The 390s dispute over Origen''s teachings as this world actually underwent it: a community
  that had inherited much of its way of reading scripture from a teacher whose specific conclusions it
  then renounced urgently and publicly - a former translating-partner become fiercest opponent, a bishop
  to be maneuvered against, and at stake ''which teacher''s account of Jerome''s own faithfulness would
  be believed'' (chunk Quick/World Meaning).'
prior_sense: 'The inherited debt itself is the prior: this world''s own exegetical method carried Origen''s
  stamp before the renunciation - ''inherited, without quite meaning to, a good deal of its own way of
  reading scripture'' (chunk World Meaning) - so the controversy''s prior sense is the unproblematic teacher
  the name later made dangerous.'
modern_sense: A purely abstract theological disagreement - souls, resurrection bodies - with the personal
  and political stakes trimmed away (chunk Modern Hearing).
conceptual_distance_note: 'The rupture was ''simultaneously doctrinal, personal, and political - the three
  were not separable within it'' (chunk World Hearing, verbatim). The corrective is a reintegration of
  dimensions, not a lived-concept reversal: standard grounding. The chunk''s CT Contest Type section stays
  parked in this record''s body for the S2.6 claims.'
semantic_domain: origenist-controversy
grounding_criterion: standard
voice_surface: We had learned to read scripture, more than we liked to admit, from a teacher whose conclusions
  we then had to renounce - publicly, urgently, while a friend who had once translated beside us became
  the fiercest voice against us. The quarrel was never only doctrine. It was about which account of our
  own faithfulness would be believed.
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
field_relations:
- type: associated-with
  target_id: hallex09
  note: 'The two controversies anchor G6 together (hal_lex09 EF: ''Anchors G6 alongside Origenism'') -
    association, no hierarchy. Chunk Ecological Function (verbatim, absorbed per FLAG-002): Anchors G6
    (Supporting gravity); reshapes the *Hebraica veritas* project (the Augustine dispute is a downstream
    test of related textual-authority commitments) and *patrocinium* (conducted through, and threatening,
    the patronage network — Pammachius and Marcella are named addressees of Jerome''s own polemic).'
- type: associated-with
  target_id: hallex01
  note: 'This chunk''s EF: the controversy ''reshapes the Hebraica veritas project (the Augustine dispute
    is a downstream test of related textual-authority commitments)''.'
- type: associated-with
  target_id: hallex06
  note: 'This chunk''s EF: ''conducted through, and threatening, the patronage network - Pammachius and
    Marcella are named addressees of Jerome''s own polemic.'''
contested_claim_ids:
- halclaim004
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex08_origenism.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.

[CT Contest Type - parked at the S2.2-equivalent; home arrives with the contested_claim records (S2.6-equivalent) / S2.3 authoring] **Meaning:** Live scholarly disagreement over how doctrinally serious versus personally/politically driven the controversy actually was — some scholarship treats the doctrinal disputes as substantively real and consequential; other scholarship treats them as largely a vehicle for a personal and reputational conflict already underway for other reasons. This is not resolved here; both readings are held in tension.
