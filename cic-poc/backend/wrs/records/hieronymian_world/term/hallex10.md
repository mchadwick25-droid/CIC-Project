---
id: hallex10
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
term: Matrona
aliases:
- Roman aristocratic woman
quick_meaning: The Roman aristocratic social-status category — inherited wealth, senatorial family connection,
  household authority — occupied by Paula, Marcella, and Fabiola before and alongside their ascetic renunciation.
world_meaning: 'To be a *matrona* of this rank was to command real household authority even before any
  turn to asceticism — the capacity to direct a large household''s resources, to receive and be received
  by the highest ranks of Roman society, to be, in one''s own right, a person whose decisions mattered
  materially to many others. This standing did not disappear when a woman renounced; it was precisely
  what made large-scale renunciation — funding a monastery, a hostel, a hospital — possible at all. The
  three women who shared this status did not, however, share identical family circumstances, and this
  world''s own record does not let their differences be flattened into one interchangeable type.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: The social-historical precondition for renunciation and patronage;
  distinguishes this world''s participant base from a mass-lay population.'
distortion_risk: '**Modern Hearing:**

  Risk of treating "aristocratic Roman woman" as a single, undifferentiated social type.


  **World Hearing:**

  Real, individually distinct family situations, wealth levels, and social positions within the same broad
  status category.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about the women's social background
  - participant asks how Paula/Marcella/Fabiola had the means to fund large projects.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL001
  author_gravity_note: Genealogical claims within Ep. 108 (Paula's claimed Scipio/Gracchi descent); general
    social-historical scholarship on senatorial households.
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex10_matrona.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.
