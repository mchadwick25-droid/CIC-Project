---
id: hallex04
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
term: Virginitas
aliases:
- Consecrated virginity
quick_meaning: Consecrated, lifelong sexual continence, held in this world as the highest form of Christian
  formation available to a woman.
world_meaning: 'Virginity here was not merely the absence of marriage; it was understood as a state nearer
  to what the redeemed life will finally be — a foretaste, kept now, of a condition not yet arrived for
  everyone else. To choose it was to choose against the ordinary shape a senatorial daughter''s life was
  expected to take, and the choice was defended with real rhetorical force: sharp words against marriage
  itself, an argument that a woman keeping her virginity kept something no other state of life could offer.
  This was not gentle counsel — it provoked real controversy, even from within the household that most
  prized it.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: Distinguishes Eustochium''s formation category from Paula''s,
  Marcella''s, and Fabiola''s (*vidua*); central theological content in this world''s own self-understanding.'
distortion_risk: '**Modern Hearing:**

  Risk of reading this as straightforward, uncontroversial praise of celibacy.


  **World Hearing:**

  A genuinely severe, contested rhetorical position that drew criticism even in its own time for its harshness
  toward marriage.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about Eustochium
  - participant asks why virginity was valued so highly
  - conversation touches Ep. 22 or its "Ciceronian, not a Christian" dream.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL001
  author_gravity_note: 'Ep. 22 (to Eustochium, *De virginitate servanda*). Author Gravity note: the theological
    argument is Jerome''s own construction; carried at Widely Accepted confidence for "virginity held
    superior standing in this world''s self-understanding," Contested for the specific rhetorical severity
    of any one articulation representing the whole community''s uniform voice.'
period_sense: Consecrated, lifelong sexual continence held as the highest form of Christian formation
  available to a woman - understood as a foretaste of the redeemed life, defended with sharp rhetorical
  force against marriage itself, and provoking real controversy even within the household that most prized
  it (chunk Quick/World Meaning).
prior_sense: The ordinary Latin status word for maidenhood - a condition, not a vocation; the consecrated,
  eschatological sense is this world's own specialization - a builder note, UNVERIFIED against this build's
  own docs.
modern_sense: Straightforward, uncontroversial praise of celibacy (chunk Modern Hearing).
conceptual_distance_note: 'The modern ear hears gentle counsel; this world''s advocacy was a genuinely
  severe, contested rhetorical position that drew criticism in its own time for its harshness toward marriage
  (chunk World Hearing). Sharp gap: high grounding criterion by rule.'
semantic_domain: consecrated-virginity
grounding_criterion: high
voice_surface: Virginity with us was not the absence of marriage but a state nearer to what the redeemed
  life will finally be - a foretaste kept now. To choose it was to choose against the shape a senatorial
  daughter's life was expected to take, and we defended the choice with words sharp enough that even our
  own household flinched.
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
field_relations:
- type: associated-with
  target_id: hallex03
  note: 'Symmetric mirror of hallex03''s edge: renunciation is this state''s practical expression (hal_lex03
    EF). Chunk Ecological Function (verbatim, absorbed per FLAG-002): Distinguishes Eustochium''s formation
    category from Paula''s, Marcella''s, and Fabiola''s (*vidua*); central theological content in this
    world''s own self-understanding.'
- type: associated-with
  target_id: hallex05
  note: 'This chunk''s EF: ''Distinguishes Eustochium''s formation category from Paula''s, Marcella''s,
    and Fabiola''s (vidua)'' - sister formation categories, deliberately kept distinct; symmetric both
    ways.'
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex04_virginitas.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.
