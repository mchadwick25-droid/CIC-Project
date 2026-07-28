---
id: syrlex008
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
term: Mar (ܡܪܝ)
aliases:
- '"my lord'
- '" "Saint" (loose parallel honorific)'
quick_meaning: '"Mar" is an honorific title-prefix meaning "my lord," used across Syriac Christianity
  for bishops, saints, and revered teachers, roughly parallel to "Saint" — broadly attested for this world
  (Aphrahat himself was called "Mar Jacob, the Persian sage" in a 510 CE colophon), but not confirmed
  as attached to Ephrem''s own name during his lifetime.'
world_meaning: ''
distortion_risk: '**Modern Hearing / World Hearing:** A participant may assume "Mar Ephrem" was a form
  of address already in use during Ephrem''s own lifetime (d. 373) or immediately after. No source confirms
  this specific compound within that window; it may reflect a later, veneration-driven convention, and
  should not be asserted as a contemporary usage without further check.'
retrieval:
  tier: 3
  retrieve_when:
  - participant uses "Mar" as a title prefix (e.g., "Mar Ephrem," "Mar Aphrahat")
  - participant asks what "Mar" means.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about a specific bishop's formal office or title of authority rather than
      the honorific prefix itself (see Catholicos entry for office-title anachronism risk).
  force_llm_vote: false
sources: []
original_script: ܡܪܝ
period_sense: An honorific title-prefix, 'my lord,' used across Syriac Christianity for bishops, saints,
  and revered teachers (roughly parallel to 'Saint') - broadly attested for this world, but NOT confirmed
  as attached to Ephrem's own name during his lifetime (chunk Quick Meaning).
prior_sense: The ordinary Aramaic address 'my lord' (mar + first-person suffix) - a secular honorific
  whose ecclesial use is a specialization of everyday deference, per the chunk's own gloss.
modern_sense: '''Mar Ephrem'' assumed to be a form of address already in use during Ephrem''s own lifetime
  or immediately after (chunk combined Modern/World Hearing).'
conceptual_distance_note: 'A dating caution on a compound, not a conceptual gap: the honorific is real
  and low-controversy as a linguistic fact (Aphrahat called ''Mar Jacob, the Persian sage'' in a 510 CE
  colophon - itself post-window), but the specific compound ''Mar Ephrem'' within the window is unconfirmed
  and may be a later veneration-driven convention. Low grounding: included for runtime recognizability,
  the chunk says, not because it organizes the ecology.'
semantic_domain: honorific
grounding_criterion: low
voice_surface: Mar is how we say 'my lord' - for a bishop, a holy one, a teacher whose word is weighed.
  Whether anyone said 'Mar Ephrem' while Ephrem lived, our record does not show.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-28'
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
field_relations: []
---
Migrated at the S6.2/SYR S2.2-equivalent (2026-07-28) from `data/syriac_world/lexicon_chunks/syrlex008_mar.md` (mechanical split; mapping in `wrs/migrate/s62_syr_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note - parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] No reciprocal cross-reference asserted. This is a general honorific, real and low-controversy as a linguistic fact, but not itself structurally tied to another lexicon entry — included for completeness and runtime recognizability rather than because it organizes the ecology.
