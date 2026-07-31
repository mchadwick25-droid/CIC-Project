---
id: halstory09
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
title: The Household's Own Desert Tales
narrative_tier:
  tier: 3
  justification: Explicit hagiographic romance genre with acknowledged legendary and rhetorical elements,
    not straightforward historical reporting — the clearest, most self-evident Tier 3 case in this repository.
    These are structurally about specific named individuals (Malchus, Hilarion), which is precisely why
    they cannot border Tier 4 regardless of how thin their historical confidence is — Tier 4 requires
    a story not about a specific named individual.
text: The household's scholar wrote his own tales of desert heroism — a captive monk, Malchus, who kept
  his vows even in slavery and returned at last to freedom; a hermit, Hilarion, who withdrew from the
  world to find what remained when everything else was stripped away. These are not remembered as plain
  history. They are remembered as the household's own answer to the Egyptian desert stories it encountered
  on its own journey — a way of giving Latin Christians their own account of what a formed ascetic life
  could become.
attested_occasion: 'The Vita Malchi and Vita Hilarionis as the household''s own literary production: desert
  romances answering the Egyptian stories encountered on the founding journey - explicit hagiographic-romance
  genre, the clearest Tier 3 case in the repository, and structurally about named individuals, which is
  exactly why they cannot border Tier 4 (the chunk''s own Tier Justification).'
tellable_as: background-fact
owner_figure_id: halfig001
voice_surface: 'Our scholar wrote desert tales of his own - the captive monk who kept his vows, the hermit
  who went to find what remained when all else was stripped away. We tell them as what they are: our own
  answer to Egypt''s stories, models of what we believed formation could become - not chronicles of two
  men''s lives. Usage guidance (chunk, verbatim): May be offered as models of ascetic heroism this household''s
  own literary output produced and valued — evidence of what this world believed formation could look
  like, not evidence of specific historical events involving Malchus or Hilarion as named individuals.'
confidence_line: Inferential/Thin
retrieval:
  tier: 3
  retrieve_when:
  - Participant asks about ascetic heroism this household admired
  - participant asks for a story in the household's own literary voice
  - participant asks about the influence of Egyptian/desert monasticism on this household.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant wants factual history of specific individuals (these are literary, not documentary,
      sources).
  force_llm_vote: false
sources:
- source_id: srcHAL004
  locus: Jerome, Vita Malchi and Vita Hilarionis
---
Migrated at the S6.2/HAL S2.4-equivalent (2026-07-31) from `data/hieronymian_world/story_chunks/hal_story09_the-desert-romances.md` (mapping in `wrs/migrate/s62_hal_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX-SYR S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] Illuminates the formation-narrative dimension directly: what this household believed formation could look like, expressed through a genre it deliberately adapted from the Egyptian desert tradition it encountered on its own founding journey.
