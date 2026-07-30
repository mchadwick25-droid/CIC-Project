---
id: syrlex005
world_id: syriac-edessa-nisibis
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
term: memra (ܡܐܡܪܐ) / memre (plural)
aliases:
- verse homily
quick_meaning: Within this world's own 200–410 window, "memra" names a small, narrowly authenticated set
  of verse compositions by Ephrem in couplets and single syllabic meter — not yet the fully developed,
  named "verse homily" genre that later Syriac tradition associates with the term.
world_meaning: ''
distortion_risk: '**Modern Hearing / World Hearing:** A participant familiar with later Syriac literature
  may hear "memra" as an already-settled, named literary category standing alongside madrasha within this
  world''s own period. In fact, only a handful of texts are securely Ephrem''s own in this bare metrical
  form (per Brock, the six memre "On Faith" and the memra on the destruction of Nicomedia are definitely
  his; a few others are probably or less certainly genuine) — the fully developed verse-homily genre that
  dominates later discussion is a fifth/sixth-century crystallization associated with Narsai and Jacob
  of Serugh, well after this world''s own 410 boundary, and is not attested for Aphrahat at all.'
retrieval:
  tier: 3
  retrieve_when:
  - participant asks about "memra" as a Syriac literary genre, likely from familiarity with later Syriac
    tradition (Narsai, Jacob of Serugh)
  - participant asks whether memra and madrasha are the same thing.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant has not raised memra specifically and madrasha alone answers the question.
  force_llm_vote: false
sources: []
original_script: ܡܐܡܪܐ
period_sense: 'Within this world''s own 200-410 window, a small, narrowly authenticated set of verse compositions
  by Ephrem in couplets and single syllabic meter (per Brock: the six memre ''On Faith'' and the Nicomedia
  memra definitely his; a few others probably or less certainly genuine) - not yet the named ''verse homily''
  genre of later tradition (chunk Quick Meaning and Distortion Risk).'
prior_sense: The ordinary Syriac word for a discourse or utterance is the inherited surface - a builder
  note, UNVERIFIED against this build's own docs, which treat the term only at genre level (Doc_03 SS1.5).
modern_sense: '''Memra'' heard through later Syriac literature as an already-settled, named literary category
  standing alongside madrasha within this world''s own period (chunk combined Modern/World Hearing).'
conceptual_distance_note: 'A retrojection gap: the fully developed verse-homily genre is a fifth/sixth-century
  crystallization (Narsai, Jacob of Serugh), after this world''s own 410 boundary, and not attested for
  Aphrahat at all - this world''s own memra is a handful of authenticated Ephrem pieces in a bare metrical
  form. Standard grounding: genre-history correction, anachronism-guard shaped.'
semantic_domain: verse-genre
grounding_criterion: standard
voice_surface: A memra with us is a recited thing, couplets in one meter, and only a few are surely Ephrem's
  own. The great named genre of verse homilies that later teachers made famous is their harvest, not our
  field.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-28'
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
field_relations:
- type: associated-with
  target_id: syrlex004
  note: Sister verse genre, distinguished by meter and - for madrasha - sung/refrain structure against
    memra's recited couplets (chunk Reciprocity Note); symmetric mirror of syrlex004's edge.
---
Migrated at the S6.2/SYR S2.2-equivalent (2026-07-28) from `data/syriac_world/lexicon_chunks/syrlex005_memra.md` (mechanical split; mapping in `wrs/migrate/s62_syr_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note - parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with madrasha (sister verse genre, distinguished by meter and — for madrasha — sung/refrain structure against memra's recited couplets). Entry lists this term back.
