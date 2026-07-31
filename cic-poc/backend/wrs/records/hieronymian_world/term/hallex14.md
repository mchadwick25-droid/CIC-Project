---
id: hallex14
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
term: Nosocomium
aliases:
- Fabiola's hospital
quick_meaning: The hospital Fabiola founded in Rome for the sick — a distinct institution from the hospice
  for travelers (*xenodochium*).
world_meaning: 'Before this world''s central scholar and his patrons ever built anything at Bethlehem,
  one of the women of this same network had already, in Rome, gathered the sick in from the streets and
  cared for them under one roof — the first such foundation. The word for the place she built came into
  Latin from Greek and was left there, untranslated, even by the very scholar who elsewhere insisted on
  precision in translation.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: Distinct expression of renunciation and patronage in this world''s
  ministry ecology; distinguished explicitly from *xenodochium* to prevent conflation of two real, separate
  institutions.'
distortion_risk: '**Modern Hearing:**

  Risk of conflating this with the travelers'' hospice, or assuming a modern hospital''s institutional
  scale and staffing.


  **World Hearing:**

  A genuinely novel act of charitable founding, on a scale not independently verified, but real and Rome-based,
  distinct from any Bethlehem institution.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about Fabiola
  - participant asks about early Christian hospitals/charitable institutions.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn
  - condition_type: sense-disambiguation
    text: participant is asking about the travelers' hospice specifically (direct instead to Xenodochium).
  force_llm_vote: false
sources:
- source_id: srcHAL001
  author_gravity_note: 'Jerome, Ep. 77.6, verified directly against critical text (Perseus): "Et primo
    omnium νοσοκομεῖον instituit, in quo aegrotantes colligeret de plateis" — Jerome leaves the term in
    Greek script.'
period_sense: The hospital Fabiola founded in Rome for the sick - the first such foundation, distinct
  from the travelers' hospice (xenodochium); the sick gathered in from the streets and cared for under
  one roof, before anything was built at Bethlehem; the Greek word left untranslated in Latin even by
  the scholar who elsewhere insisted on translation precision (chunk Quick/World Meaning).
prior_sense: 'A Greek loan (the chunk''s own note: the word ''came into Latin from Greek and was left
  there, untranslated'') - the prior is the Greek term for a place of care for the sick, new enough in
  Latin that this founding is what domesticated it; no Greek-script form appears in this build''s docs
  and none is fabricated here.'
modern_sense: Conflated with the travelers' hospice, or assumed to have a modern hospital's institutional
  scale and staffing (chunk Modern Hearing).
conceptual_distance_note: 'A genuinely novel act of charitable founding - real, Rome-based, distinct from
  any Bethlehem institution - ''on a scale not independently verified'' (chunk World Hearing, the caveat
  preserved verbatim). Standard grounding: an anti-conflation and scale guard. Front-matter Related-Term
  ''Xenodochium'' names a never-built term - declared, no edge possible; the Perseus critical-text verification
  of Ep. 77.6 is the pre-freeze re-sweep''s editions-class item.'
semantic_domain: charitable-foundation
grounding_criterion: standard
voice_surface: 'Before any of us built at Bethlehem, Fabiola had already done the newer thing in Rome:
  gathered the sick in from the streets and cared for them under one roof - the first house of its kind.
  Even the word for it stayed Greek on our tongues, as if Latin had not yet caught up with what she had
  done.'
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: corroborating
  formation_confidence: Documented
field_relations:
- type: presupposes
  target_id: hallex03
  note: 'The founding presupposes renounced wealth (hal_lex03''s EF names nosocomium among what renuntiatio
    is presupposed by). Chunk Ecological Function (verbatim, absorbed per FLAG-002): Distinct expression
    of renunciation and patronage in this world''s ministry ecology; distinguished explicitly from *xenodochium*
    to prevent conflation of two real, separate institutions.'
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex14_nosocomium.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.
