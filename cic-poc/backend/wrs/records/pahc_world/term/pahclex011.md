---
id: pahclex011
world_id: post-apostolic-house-church
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
term: baptisma (βάπτισμα)
aliases:
- baptism
quick_meaning: '*Baptisma* is the water — the washing that marks a person''s entry into the community,
  given after teaching and fasting, in running water if it can be had.'
world_meaning: 'We call it the water, or by its Greek name, baptisma. Before anyone comes to it, they
  are taught — the Two Ways, what must be put away, what must be taken up. Then, after fasting, they come
  to the water itself. The Didache instructs: baptize in running water if you can; if not, in still water;
  if neither is available, pour water over the head three times in the name of Father, Son, and Holy Spirit.
  This flexibility tells us something: the heart of the matter is not the precise method but the washing
  itself and what precedes it.


  Justin in Rome describes the same basic pattern: those who believe, who commit to the life, who fast
  and pray with the community, are brought to a place with water and are reborn in the name of the Father
  of all, and of Jesus Christ, and of the Holy Spirit. After the water comes the eucharist — baptism opens
  the door to the table.


  Ignatius tells us that no one should baptize without the bishop — which means, for communities shaped
  by his instruction, this is not something any household member does on their own authority. Where a
  bishop presides, the water comes under his oversight.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: This term anchors the formation process by which new members
  enter the community. Baptism is the threshold between outside and inside, after catechesis and before
  the table.'
distortion_risk: 'In this world, baptism shows genuine variation — running water, still water, pouring
  — while holding a common pattern of teaching first, then washing, then table.


  **Living Tradition Note:**

  This entry describes this world''s own formation ecology (c.70–200 CE). It makes no claim about how
  any present-day tradition currently defines or practices baptism.


  **Confidence:**

  Widely Accepted for the basic pattern (teaching, fasting, water, threefold divine naming, admission
  to the table) — independently attested in both this community''s own account (Didache) and Rome''s (Justin),
  each in its own register. Documented, but not generalizable beyond this community, for the specific
  water-type preference order and threefold-pouring fallback described here. Ignatius''s evidence (Antioch/Asia
  Minor) confirms only that baptism existed and required the bishop''s own sanction — it contributes no
  procedural detail and should not be read as corroborating this community''s specific sequence.'
retrieval:
  tier: 2
  retrieve_when:
  - participant asks about baptism, initiation, coming to the water, or preparation for joining the community.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about infant baptism debates or modern baptismal theology with no connection
      to this period.
  force_llm_vote: false
sources:
- source_id: srcPAHCP01
  author_gravity_note: Didache 7 (baptismal instructions — running water, still water, pouring).
- source_id: srcPAHCP06
  author_gravity_note: Justin Martyr, First Apology 61, 65–66 (baptismal practice at Rome).
- source_id: srcPAHCP03
  author_gravity_note: Ignatius, Letter to the Smyrnaeans 8:2 (baptism requiring the bishop).
modern_hearing: A modern reader may assume a uniform baptismal practice, or may project later debates
  about mode or timing onto this period.
period_sense: 'The water, the threshold: teaching first (the Two Ways), then fasting, then the washing
  - running water if you can, still water if not, pouring three times if neither, in the threefold name;
  the flexibility itself the teaching (the heart is the washing and what precedes it, not the method);
  after the water, the table; under Strand-A letters, under the bishop''s oversight (chunk Quick/World
  Meaning).'
prior_sense: The ordinary Greek baptisma - dipping, washing - an everyday water-word made the threshold
  of a life; a builder note, UNVERIFIED against this build's own docs.
modern_sense: A uniform practice, or later debates about mode and timing projected back (chunk Modern
  Hearing).
conceptual_distance_note: 'Genuine variation (running, still, poured) holding one common pattern: teaching,
  washing, table (chunk World Hearing). The Rule-A-dropped alias surface ''the water'' is carried at runtime
  by this world''s own exact A-gloss (''the water''->''baptism'') - the S2.2 drop and the SS4 gloss design
  meeting as intended, noted for the record. Standard grounding.'
semantic_domain: water-threshold
grounding_criterion: standard
voice_surface: 'We call it the water. Before it, the teaching and the fast; at it, running water if we
  have it, still if we do not, poured three times if we have neither - the washing matters, not the plumbing.
  And after the water, the table: baptism opens that door. Where a bishop presides, the water comes under
  his oversight; where none does, it is no less the water.'
original_script: βάπτισμα
confidence:
  citation_specificity: A
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
field_relations:
- type: presupposes
  target_id: pahclex007
  note: 'The chunk''s own EF: the threshold ''after catechesis and before the table'' - teaching first.
    Chunk Ecological Function (verbatim, absorbed per FLAG-002): This term anchors the formation process
    by which new members enter the community. Baptism is the threshold between outside and inside, after
    catechesis and before the table.'
- type: presupposed-by
  target_id: pahclex004
  note: Mirror of pahclex004's presupposes edge (the door to the table).
- type: associated-with
  target_id: pahclex001
  note: Symmetric mirror of pahclex001's edge (Strand-A oversight of the water).
---
Migrated at the S6.2/PAHC S2.2-equivalent (2026-07-31) from `data/pahc_world/lexicon_chunks/pahclex011_baptisma.md` (mechanical split; mapping in `wrs/migrate/s62_pahc_s22.py`; aliases parsed under the VG-1a semantics with the preflighted Rule-A drops at birth - the second world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 3 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
