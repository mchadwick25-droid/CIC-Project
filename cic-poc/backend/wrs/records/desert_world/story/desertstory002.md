---
id: desertstory002
world_id: desert-monasticism
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
cache_stability: static
title: Antony's Withdrawal to the Outer and Inner Mountain
narrative_tier:
  tier: 1
  justification: Same source and confidence basis as Story 001. The staged chronology — outer mountain
    from roughly the mid-280s, inner mountain from the early 310s — is treated by Doc_01 §2.1 as the standard,
    well-established outline, while incident-level narrative detail remains Contested on the same grounds
    as Story 001's own Rubenson/Athanasius tension.
text: Athanasius records Antony's withdrawal as staged, not sudden. He first remained near his own village,
  under an older ascetic's guidance, before moving out to the tombs. From there he crossed the Nile to
  what came to be called the outer mountain, at Pispir, where he remained in near-total seclusion for
  some twenty years, before at last emerging to instruct the disciples who had by then gathered near him,
  drawn by report of his life. Later still, seeking greater solitude from the crowds his own reputation
  now drew, he withdrew further, to an inner mountain between the Nile and the Red Sea, where he spent
  most of what remained of his life.
attested_occasion: 'The staged withdrawal: near the village under an older ascetic, the tombs, the outer
  mountain at Pispir (c. 286) with emergence c. 305, the inner mountain from c. 311-313 (Vita chs. 3-14,
  49-50; Doc_01 SS2.1).'
tellable_as: scene
voice_surface: 'Athanasius records the stages; we tell it as a lifelong deepening, not one departure.
  Usage guidance (chunk, verbatim): May be narrated as remembered history with the same author-named,
  distance-acknowledged framing as Story 001. Particularly useful for correcting a common misreading —
  that withdrawal in this world''s own logic was a single departure — into the more accurate picture of
  a lifelong, deepening practice that kept moving further from what had already become familiar.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks whether withdrawal happened all at once or gradually
  - participant asks how a solitary elder came to have disciples, or why Antony kept moving further from
    settled life
  - conversation reaches gravity 1 (withdrawal) as a lifelong deepening practice rather than a single
    decision
  - conversation reaches gravity 3 (elder-mediated authority) and how a reputation for holiness draws
    visitors.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about the original call itself (see Story 001)
  - condition_type: sense-disambiguation
    text: participant is asking about the interior combat specifically (see Story 007)
  - condition_type: sense-disambiguation
    text: conversation concerns cenobitic or semi-anchoritic communal structure rather than Strand A's
      own solitary pattern.
  force_llm_vote: false
sources:
- source_id: srcDES001
  author_gravity_note: Widely Accepted (the staged chronology and general outline); Contested (incident-level
    narrative detail, same basis as Story 001)
- source_id: srcDES020
  author_gravity_note: 'Source line (chunk): Athanasius, Life of Antony, chs. 3-14 (outer mountain) and
    chs. 49-50 (inner mountain)'
owner_figure_id: desertfig001
gravity_links:
- gravity_id: desertgrav001
  note: 'Withdrawal here is not one decisive act but a going further, and then further again. This is that pattern
    in its clearest form. It also shows how authority begins among us: not conferred, but gathered, as
    disciples come to a reputation tested by years alone. The solitary struggle that runs through much of our
    life is built out of this story.'
- gravity_id: desertgrav003
  note: Named in this story's Formation Ecology Connection - full text on the first gravity_links note
    (CO-P2-04).
---
Migrated at S2.4 (2026-07-27) from `data/desert_world/story_chunks/desertstory002_antony-withdrawal-outer-inner-mountain.md` (Story Text / Tier Justification / Usage Guidance verbatim from the chunk's own sections; occasion and telling-formula per chunk + Doc_09a). Tier-4 owner gap: see FLAG-003.

CO-P2-04 (2026-07-27): parked FLAG-004 sections restructured into gravity_links[] (FEC verbatim on the first link) and, for this record's tier-4 table, per-element sources[] entries.
