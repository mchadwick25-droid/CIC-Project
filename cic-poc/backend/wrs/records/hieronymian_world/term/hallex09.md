---
id: hallex09
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
term: Pelagianism (the Pelagian controversy)
aliases:
- The 416 attack
- the Pelagian mob attack
quick_meaning: 'The quarrel over grace, free will, and whether a person can stop sinning. It led to a
  violent attack on this household''s monastery in 416.'
world_meaning: 'This controversy did not stay confined to argument. In 416, whatever combination of theological
  conviction and local grievance had built up around this dispute turned physical: a mob attacked the
  Bethlehem monastery itself, buildings burned, and — by report — at least one member of the community
  died. This is a controversy this world experienced not as a debate to be won on paper but as a real
  threat to its own physical safety, arriving at the doors of the very place its scholarly project called
  home.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: Anchors G6 alongside Origenism; an ending-adjacent external force
  pressing on this world''s final years.'
distortion_risk: '**Modern Hearing:**

  Risk of treating this purely as an abstract soteriological dispute (grace vs. free will) disconnected
  from real-world consequence.


  **World Hearing:**

  A dispute this world experienced, at least once, as physical violence at its own door.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about the attack on the Bethlehem monastery
  - participant asks about grace and free will disputes in this period.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL001
  author_gravity_note: 'Jerome''s own account (letter to Riparius). Author Gravity note: notably vague
    on casualty/detail specifics; this world''s own record does not supply the precision a modern account
    might expect, and none is manufactured here.'
period_sense: 'The dispute over grace, free will, and human capacity for sinlessness as this world underwent
  it in 416: not an argument won or lost on paper but a mob at the Bethlehem monastery''s own doors -
  buildings burned and, by report, at least one member of the community dead (chunk Quick/World Meaning;
  the ''by report'' qualifier is the chunk''s own and is preserved, not firmed up).'
prior_sense: none-attested - a dispute-name, not an inherited concept; the record register is the event
  and its pressure on this world's final years, not a transformed prior sense.
modern_sense: An abstract soteriological dispute - grace versus free will - disconnected from real-world
  consequence (chunk Modern Hearing).
conceptual_distance_note: 'This world experienced the controversy, at least once, as physical violence
  at its own door (chunk World Hearing) - an ending-adjacent external force on the community''s last years,
  not a seminar topic. Standard grounding: the corrective restores consequence, not a different concept.'
semantic_domain: pelagian-controversy
grounding_criterion: standard
voice_surface: 'In the year 416 the argument stopped being an argument. Whatever mixture of conviction
  and grievance had gathered around the dispute came to our own doors: the monastery attacked, buildings
  burned, and - as it was reported - one of our own dead. We knew this controversy not as a debate to
  be won but as a danger that had found where we lived.'
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
field_relations:
- type: associated-with
  target_id: hallex08
  note: 'Symmetric mirror of hallex08''s edge: joint G6 anchors, the two controversies pressing on this
    world from outside. Chunk Ecological Function (verbatim, absorbed per FLAG-002): Anchors G6 alongside
    Origenism; an ending-adjacent external force pressing on this world''s final years.'
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex09_pelagianism.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
