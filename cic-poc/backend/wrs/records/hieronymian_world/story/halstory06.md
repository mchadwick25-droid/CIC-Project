---
id: halstory06
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
title: What a Formed Life Looked Like (Paula's Epitaph)
narrative_tier:
  tier: 3
  justification: Attributed narrative in a recognized hagiographic-adjacent genre. The bare facts of Paula's
    death (26 January 404) are Tier 1-adjacent; the narrative texture — how her life is dramatized, what
    words are put in her mouth — follows genre conventions of idealization and cannot be treated as historical
    reporting of specific scenes.
text: 'This is how the household remembers the widow Paula — not merely what happened to her, but what
  her life was held up to show: a woman of senatorial birth who gave away what she had until her own household
  could no longer easily say where the wealth had gone, and who still, from that same emptied purse, raised
  a monastery, a convent, and a house of welcome for travelers. The household does not ask which of these
  two things — total poverty, or the capacity still to build — was truer. Both are told together, without
  resolving the tension between them.'
attested_occasion: 'The Epitaphium Sanctae Paulae (Ep. 108) as formation portrait: senatorial birth, wealth
  given until the household could not say where it had gone, and still - from the same emptied purse -
  a monastery, a convent, a house of welcome raised; the bare death date (26 January 404) Tier-1-adjacent,
  the narrative texture genre-idealized and not historical reporting of scenes (the chunk''s own Tier
  Justification).'
tellable_as: scene
owner_figure_id: halfig002
voice_surface: 'This is how we remember Paula - not merely what happened to her but what her life was
  held up to show. That she gave until nothing could be found, and that she still built - we tell both
  together, as our record does, without deciding which was truer. It is an epitaph''s portrait, and we
  say so. Usage guidance (chunk, verbatim): May be offered as the household''s own account of what a formed
  ascetic woman''s life looked like, with the epitaph framing explicitly acknowledged. Not usable as historical
  fact about specific reported scenes or quoted words — the formation ideal is the evidence, not the biographical
  detail.'
confidence_line: Contested (general portrait); Inferential/Thin (specific details, quoted words)
retrieval:
  tier: 3
  retrieve_when:
  - Participant asks what a well-formed ascetic woman's life looked like in this world
  - participant asks about Paula specifically
  - participant asks how this household remembers its dead.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant wants only the bare historical facts of the journey (retrieve story 01) or death
      date (use lexicon/Doc reference).
  force_llm_vote: false
sources:
- source_id: srcHAL001
  locus: Jerome, Epistula 108 (Epitaphium Sanctae Paulae)
gravity_links:
- gravity_id: halgrav002
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at
    S2.5): Illuminates the ascetic self-impoverishment gravity at its richest, and the memory-structures/formation-narrative
    dimension of this world''s ecology — the epitaph-letter genre does formation work by showing what
    a well-formed life looks like, not merely recording what happened.'
---
Migrated at the S6.2/HAL S2.4-equivalent (2026-07-31) from `data/hieronymian_world/story_chunks/hal_story06_paulas-epitaph.md` (mapping in `wrs/migrate/s62_hal_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX-SYR S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] Illuminates the ascetic self-impoverishment gravity at its richest, and the memory-structures/formation-narrative dimension of this world's ecology — the epitaph-letter genre does formation work by showing what a well-formed life looks like, not merely recording what happened.
