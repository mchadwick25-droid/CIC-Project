---
id: hallex15
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
term: Monachus
aliases:
- Monk
quick_meaning: 'The usual word for a male ascetic - a monk. It is well attested across this world''s own
  writing.'
world_meaning: 'This is the ordinary word this world used for the men who filled the communities its central
  scholar visited on his journey to the Holy Land, and for the men of his own Bethlehem household. It
  is a simple, well-worn term, in contrast to how much more specifically this world''s own vocabulary
  is worked out for its women (*virgo*, *vidua*) rather than a single parallel feminine term.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: Names the unnamed monastic multitudes this world''s own sources
  reference but never individuate.'
distortion_risk: '**Modern Hearing:**

  Likely unproblematic — this term maps reasonably well onto modern "monk."


  **World Hearing:**

  Broadly consistent with modern usage; low distortion risk relative to nearly every other entry in this
  lexicon.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about the male monastic community at Bethlehem or in Nitria/Egypt.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL001
  author_gravity_note: Extensively attested throughout Jerome's corpus generally.
period_sense: The standard term for a male ascetic - the ordinary word for the men of the communities
  visited on the journey to the Holy Land and of the Bethlehem household itself; a simple, well-worn term,
  in deliberate contrast to the much more differentiated vocabulary this world worked out for its women
  (virgo, vidua) (chunk Quick/World Meaning).
prior_sense: A Greek loan into Latin (monachus, from the Greek for a solitary or single one) already ordinary
  by this world's time - the inherited surface used as-is, not transformed; a builder note on the etymology,
  UNVERIFIED against this build's own docs, which treat the term only as standard vocabulary.
modern_sense: 'Modern ''monk'' - which the chunk itself judges a reasonable mapping (chunk Modern Hearing:
  ''likely unproblematic'').'
conceptual_distance_note: Broadly consistent with modern usage; low distortion risk relative to nearly
  every other entry in this lexicon (chunk World Hearing, near-verbatim). Low grounding by the chunk's
  own assessment - the entry's work is naming 'the unnamed monastic multitudes' the sources reference
  but never individuate (chunk EF). Both front-matter Related-Terms (Monasterium duplex, Praeceptor) name
  never-built terms - declared; this record carries no field_relations and its parked EF remains in world_meaning
  (no first edge to ride).
semantic_domain: male-asceticism
grounding_criterion: low
voice_surface: For the men we had one plain word - monachus, a monk - worn smooth by use. It is our women
  for whom the language grew careful and exact; the men it names in multitudes, and mostly leaves unnamed.
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
field_relations: []
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex15_monachus.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
