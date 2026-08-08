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
quick_meaning: 'A Roman woman of high birth. She held inherited wealth, senatorial family ties, and charge
  of a household. Paula, Marcella, and Fabiola were all such women, before and while they gave
  it up.'
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
period_sense: The Roman aristocratic status category - inherited wealth, senatorial connection, real household
  authority - occupied by Paula, Marcella, and Fabiola before and alongside their renunciation; the standing
  did not disappear at renunciation but was precisely what made large-scale founding possible, and the
  three women's circumstances were individually distinct, not one interchangeable type (chunk Quick/World
  Meaning).
prior_sense: 'The prior IS the sense: this world uses the empire''s own status category as-is - the term
  names an inherited social position, not a transformed concept; what the world adds is only what the
  standing was then FOR.'
modern_sense: '''Aristocratic Roman woman'' as a single, undifferentiated social type (chunk Modern Hearing).'
conceptual_distance_note: 'The record''s own guard is against flattening: real, individually distinct
  family situations, wealth levels, and positions within one broad category - ''this world''s own record
  does not let their differences be flattened'' (chunk World Meaning). Standard grounding: a differentiation
  guard, not a concept gap.'
semantic_domain: aristocratic-status
grounding_criterion: standard
voice_surface: Before any of these women renounced, each already commanded a household whose decisions
  mattered materially to many others - and no two of them from the same circumstances. That standing is
  not what they gave up; it is what they gave WITH. A monastery, a hostel, a hospital - none of it rises
  from nothing.
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
field_relations:
- type: presupposed-by
  target_id: hallex03
  note: 'Mirror of hallex03''s presupposes edge: this standing is renunciation''s precondition. Chunk
    Ecological Function (verbatim, absorbed per FLAG-002): The social-historical precondition for renunciation
    and patronage; distinguishes this world''s participant base from a mass-lay population.'
- type: presupposed-by
  target_id: hallex06
  note: 'Mirror of hallex06''s presupposes edge: the same precondition under patronage (this chunk''s
    EF: ''the social-historical precondition for renunciation and patronage'').'
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex10_matrona.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
