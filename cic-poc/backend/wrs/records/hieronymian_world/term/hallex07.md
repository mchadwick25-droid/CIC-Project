---
id: hallex07
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
term: Epistula
aliases: []
quick_meaning: The letter — not merely a record of this world's life, but the actual medium through which
  its formation, direction, and community-maintenance happened across distance.
world_meaning: 'When a scholar and the household he directed no longer occupied the same city, a letter
  became more than news — it was how spiritual direction was actually delivered, how an argument about
  scripture was actually conducted, how a community that had physically split in two remained, in its
  own understanding, one project. A hard letter of exhortation, a commentary sent with a covering dedication,
  a furious exchange with a former friend turned theological opponent — all of these were the community''s
  actual formation apparatus, not paperwork about formation happening elsewhere.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: Anchors G4 (Supporting gravity); the vehicle for nearly every
  other term in this lexicon; bridges the Rome/Bethlehem bipolar geography by definition.'
distortion_risk: '**Modern Hearing:**

  Risk of reading letters as secondary evidence *about* the community''s life, rather than as the actual
  site where that life happened.


  **World Hearing:**

  The letter was itself a formation event, not a report of one.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks how the Rome and Bethlehem communities stayed connected
  - participant asks about Jerome's letters generally.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL001
  author_gravity_note: 'The entire surviving primary-voices corpus for this world is epistolary. Author
    Gravity/evidentiary-circularity note: this term''s overwhelming attestation is partly an artifact
    of the source base itself being almost entirely epistolary — its formation-centrality rests on independent
    dependency/explanatory evidence (e.g., the Rome/Bethlehem coherence it made possible), not on source-type
    circularity alone.'
period_sense: 'The letter as this world''s actual formation apparatus, not its paperwork: when the scholar
  and the household he directed no longer shared a city, spiritual direction, scriptural argument, and
  the community''s own oneness were delivered and maintained as epistulae - a hard letter of exhortation,
  a commentary under a covering dedication, a furious exchange with a former friend (chunk Quick/World
  Meaning).'
prior_sense: The ordinary Latin epistula, the empire's everyday letter - news, business, maintained relationships
  across distance; the formation-medium sense is this world's own intensification of a completely ordinary
  form - a builder note, UNVERIFIED against this build's own docs.
modern_sense: Letters as secondary evidence ABOUT the community's life - a documentary window onto formation
  happening elsewhere (chunk Modern Hearing).
conceptual_distance_note: 'The modern ear files the letters under sources; this world lived them as events
  - ''the letter was itself a formation event, not a report of one'' (chunk World Hearing, verbatim).
  Sharp gap: high grounding criterion by rule. The record''s alias set is empty by the S2.2 FLAG-028 resolution
  (''letter'' is a bare blocklist generic); reachability = term key ''epistula''.'
semantic_domain: epistolary-formation
grounding_criterion: high
voice_surface: When Rome and Bethlehem could no longer hear each other's voices, the letter became the
  room we met in. Direction was given there, scripture argued there, a community physically split in two
  remained one project there. A hard letter of exhortation was not news about our formation; it was the
  formation itself, arriving sealed.
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
field_relations:
- type: associated-with
  target_id: hallex02
  note: 'Symmetric mirror of hallex02''s edge: the translation project''s dedications, book by book, are
    epistulae. Chunk Ecological Function (verbatim, absorbed per FLAG-002): Anchors G4 (Supporting gravity);
    the vehicle for nearly every other term in this lexicon; bridges the Rome/Bethlehem bipolar geography
    by definition.'
- type: associated-with
  target_id: hallex06
  note: 'Symmetric mirror of hallex06''s edge: patronage conducted by letter across the bipolar geography
    this chunk''s EF says the genre ''bridges by definition''.'
- type: associated-with
  target_id: hallex01
  note: 'Symmetric mirror of hallex01''s edge: the Augustine exchange over textual authority was conducted
    as letters (srcHAL009).'
- type: associated-with
  target_id: hallex11
  note: 'Symmetric mirror of hallex11''s edge: exegetical direction at distance rode this medium - ''how
    an argument about scripture was actually conducted'' (this chunk''s World Meaning).'
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex07_epistula.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
