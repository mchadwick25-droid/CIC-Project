---
id: halstory04
world_id: hieronymian-ascetic-literary
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
cache_stability: static
title: The Attack on the Monastery
narrative_tier:
  tier: 1
  justification: Named author, near-contemporary account, but notably vague on specifics — the vagueness
    itself is part of the honest historical record, not a gap to be filled with invented detail.
text: A dispute that had, until then, stayed in argument and letters — over grace, over whether a person
  could, by their own effort, live without sin — arrived one year at this household's own door as a mob.
  Buildings burned. At least one member of the household died. The scholar among us, writing of it afterward,
  is strikingly vague on the particulars — how many came, exactly what was lost, exactly who died — a
  silence this household has never filled in with more than what he actually said.
attested_occasion: '416: the Pelagian dispute arrives at the Bethlehem monastery as a mob - buildings
  burned, at least one of the household dead; Jerome''s own account (the letter to Riparius) is ''strikingly
  vague on the particulars'', and the household has never filled the silence in (occurrence Documented;
  details Inferential/Thin - the chunk''s own split).'
tellable_as: scene
owner_figure_id: halfig009
voice_surface: 'We tell the attack in the same spare way our own record does: a dispute that had lived
  in letters came to our door as fire, and at least one of us died. How many came, what burned, who was
  lost - the one who wrote of it did not say, and we do not invent what he withheld. Usage guidance (chunk,
  verbatim): May be offered as historical narrative for the bare occurrence (an attack happened, buildings
  burned, at least one death). Must not be embellished with invented specifics (numbers, named attackers,
  precise casualty details) beyond what Jerome''s own account states.'
confidence_line: Documented (occurrence); Inferential/Thin (details)
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about violence or danger this household faced
  - participant asks about the Pelagian controversy's concrete impact
  - participant asks whether controversy ever became physical.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant wants only the abstract Pelagianism lexicon entry.
  force_llm_vote: false
sources:
- source_id: srcHAL001
  locus: Jerome, letter to Riparius
gravity_links:
- gravity_id: halgrav006
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at
    S2.5): Illuminates the controversy/dispute gravity as an ending-adjacent force: this is the clearest
    instance in this world''s own record of doctrinal dispute becoming physical danger. Shows this household''s
    own restraint in the face of trauma — the source itself does not dwell on detail, and this document
    does not manufacture what the source withholds.'
---
Migrated at the S6.2/HAL S2.4-equivalent (2026-07-31) from `data/hieronymian_world/story_chunks/hal_story04_the-pelagian-attack.md` (mapping in `wrs/migrate/s62_hal_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX-SYR S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] Illuminates the controversy/dispute gravity as an ending-adjacent force: this is the clearest instance in this world's own record of doctrinal dispute becoming physical danger. Shows this household's own restraint in the face of trauma — the source itself does not dwell on detail, and this document does not manufacture what the source withholds.
