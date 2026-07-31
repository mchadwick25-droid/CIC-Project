---
id: hallex05
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
term: Vidua (includes continentia)
aliases:
- Ascetic widowhood
- continentia
quick_meaning: The status of a Christian widow who declines remarriage and adopts ascetic discipline —
  the formation category of Paula, Marcella, and Fabiola.
world_meaning: 'A widow in this world faced real pressure to remarry — family expectation, social convention,
  sometimes a specific, insistent suitor. To refuse, and to take up instead a life of fasting, plain dress,
  and (for at least one of these three women) recognized scriptural authority within her own household,
  was its own distinct form of renunciation — not virginity''s total, lifelong abstention from the start,
  but a deliberate turning-away from a life already lived once, chosen again in its second half. The abstract
  virtue this required — *continentia*, self-mastery over what one''s body and social position would otherwise
  incline toward — is inseparable from the status itself in this world''s own understanding: one does
  not practice *continentia* in the abstract; one lives it out as a *vidua*, specifically.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: Anchors G2 alongside *virginitas*; Marcella''s specific standing
  (see *exegesis-as-practiced-authority*) is exercised from within this category, not virginity.'
distortion_risk: '**Modern Hearing:**

  Risk of treating widowed continence as a lesser, merely-negative absence of remarriage.


  **World Hearing:**

  A genuine, actively-chosen ascetic vocation with its own discipline and, for at least one of these women,
  real recognized standing.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about Paula, Marcella, or Fabiola's status
  - participant asks about widowhood as a Christian vocation.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL001
  author_gravity_note: 'Ep. 108 (Paula), Ep. 127 (Marcella), Ep. 77 (Fabiola). Note: all three sources
    are Jerome''s own idealizing epitaph genre; the general credibility of the pattern rests on independent
    social-historical scholarship on senatorial renunciation, not the letter count itself.'
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex05_vidua.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.
