---
id: halstory07
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
title: The Widow Roman Clergy Consulted
narrative_tier:
  tier: 3
  justification: 'Attributed to a specific figure in a specific commemorative-genre account, authored
    after her death for the scholar''s own partly self-vindicating purposes. The single most Author-Gravity-constrained
    story in this repository: single-source, Contested, authored by the one man whose pen survives, after
    the subject''s own death.'
text: 'This is how the household remembers one widow among us: after the traveling scholar left Rome for
  good, clergy who could no longer bring their hardest scriptural questions to him began, instead, bringing
  them to her, in her own house, on her own authority. Even before he left, the household remembers her
  disputing his own answers — not to win an argument, the household says, but to learn. She never needed
  anyone''s patronage to hold this standing; her own settled wealth was enough.'
attested_occasion: 'Marcella''s standing as the household remembers it (Ep. 127, written after her death,
  for the scholar''s own partly self-vindicating purposes): clergy bringing their hardest scriptural questions
  to her own house on her own authority once the scholar had left Rome - THE single most Author-Gravity-constrained
  story in this repository (single-source, Contested, post-mortem; the chunk''s own words), and the clearest evidence for the one real counter-current in this household''s life.'
tellable_as: scene
owner_figure_id: halfig003
voice_surface: 'We tell of the widow the clergy consulted carefully, for the memory comes to us in one
  voice, written after her death, by the very man whose answers she had once disputed - to learn, he says,
  not to win. Her standing was real and her wealth her own; how often the clergy came, no record but his
  remains to say. We never tell it as rivalry: the trust was of one kind, differently held. Usage guidance
  (chunk, verbatim): May be offered as the household''s own account of what independent female scriptural
  authority looked like within this world, with the attributed, single-source, post-mortem framing explicitly
  carried whenever this story is told. This is not usable as documented fact about the extent or frequency
  of her consultations — only as this world''s own remembered account of them. The Representative should
  never claim this widow''s standing rivaled or replaced the traveling scholar''s own authority — the
  two were the same kind of trust, differently held.'
confidence_line: Contested (per the Confidence/Gravity Cross-Check — single-source, does not meet Primary-gravity
  threshold)
retrieval:
  tier: 3
  retrieve_when:
  - Participant asks whether any woman in this world held recognized scriptural authority
  - participant asks about independent female authority
  - participant asks about this widow's standing directly.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant is asking about the general status category of ascetic widowhood (retrieve the vidua
      lexicon chunk instead — this story is specifically about one widow's exceptional standing, not the
      general category).
  force_llm_vote: false
sources:
- source_id: srcHAL001
  locus: Jerome, Epistula 127, to Principia
gravity_links:
- gravity_id: halgrav005
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at
    S2.5): The clearest evidence for the one real counter-current in this household''s life - an independent authority held by a woman, running against the main pattern without displacing it, which this household''s own record does not let it forget. Her authority is the same underlying currency as the traveling scholar''s, held in a different and materially independent position - not a rival structure.'
---
Migrated at the S6.2/HAL S2.4-equivalent (2026-07-31) from `data/hieronymian_world/story_chunks/hal_story07_the-widow-consulted.md` (mapping in `wrs/migrate/s62_hal_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX-SYR S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] The clearest evidence for the one real counter-current in this household's life - an independent authority held by a woman, running against the main pattern without displacing it, which this household's own record does not let it forget. Her authority is the same underlying currency as the traveling scholar's, held in a different and materially independent position - not a rival structure.
