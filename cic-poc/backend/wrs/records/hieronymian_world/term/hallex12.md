---
id: hallex12
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
term: Grammaticus
aliases:
- Jerome's classical education
quick_meaning: 'The stage of Latin schooling in grammar and literature. This world''s scholar took it under
  a teacher named Aelius Donatus. It is what made his later work on words possible.'
world_meaning: 'Before there was a translator of Hebrew, there was a student of Latin grammar and literature,
  trained under a teacher whose name he kept, decades later, in his own writing, calling him simply "my
  teacher." This classical education is what made the later philological labor possible at all — not Hebrew
  study alone, but the whole prior discipline of close attention to a text''s precise wording that grammar-school
  training instilled.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: The documented, non-Contested foundation underneath the Contested
  claims about Hebrew fluency; distinguishes the well-attested early education from the more contested
  later self-presentation.'
distortion_risk: '**Modern Hearing:**

  Risk of conflating this early, well-documented grammatical training with the later, more contested claims
  about Hebrew mastery, as though both were equally certain.


  **World Hearing:**

  Two genuinely different confidence levels — the grammar training is solidly attested; the Hebrew fluency
  it supposedly enabled is separately, and seriously, contested.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about Jerome's early education
  - participant asks whether Jerome was actually fluent in Hebrew.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL001
  author_gravity_note: Jerome's own references to Donatus as "praeceptor" — Documented (grammar training,
    not rhetoric specifically).
period_sense: The stage of classical Latin grammatical and literary training - under the specific teacher
  Aelius Donatus, whose name the student kept decades later, 'my teacher' - that instilled the discipline
  of close attention to a text's precise wording underneath all the later philological labor (chunk Quick/World
  Meaning).
prior_sense: 'The prior IS the sense: the grammaticus was the empire''s standard second-stage schoolmaster
  - an inherited institution this world attended, not a concept it transformed; what the world adds is
  what the training later made possible.'
modern_sense: The early grammar training and the later Hebrew-mastery claims conflated into one equally-certain
  achievement (chunk Modern Hearing).
conceptual_distance_note: 'Two genuinely different confidence levels held apart: the grammar training
  is solidly attested; the Hebrew fluency it supposedly enabled is separately, and seriously, contested
  (chunk World Hearing, near-verbatim) - this entry is the documented, non-Contested foundation UNDER
  the contested claims (chunk EF). Standard grounding: a confidence-disambiguation guard. Front-matter
  Related-Term ''Praeceptor'' names a never-built term - declared, no edge possible.'
semantic_domain: classical-education
grounding_criterion: standard
voice_surface: 'Before there was a translator of Hebrew there was a boy at grammar school, parsing Latin
  under Donatus - a teacher whose name he kept all his life. Whatever is argued about the Hebrew, this
  much is not argued: the habit of weighing a text word by word was learned there first.'
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: corroborating
  formation_confidence: Documented
field_relations:
- type: presupposed-by
  target_id: hallex01
  note: 'Mirror of hallex01''s presupposes edge: the training under the philological commitment. Chunk
    Ecological Function (verbatim, absorbed per FLAG-002): The documented, non-Contested foundation underneath
    the Contested claims about Hebrew fluency; distinguishes the well-attested early education from the
    more contested later self-presentation.'
contested_claim_ids:
- halclaim001
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex12_grammaticus.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
