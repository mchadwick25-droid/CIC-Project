---
id: desertstory007
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
title: Antony's Combat in the Tombs
narrative_tier:
  tier: 3
  justification: This account carries clear hagiographic genre markers -- physically embodied demons,
    a beast-form combat scene, a climactic vision of light -- that distinguish it from the more restrained,
    incident-report register of the Tier 1 stories (001-003) drawn from the same Vita. It is classified
    Tier 3, the tradition's own account of what a formed life looks like at its most extreme, rather than
    Tier 1 documented history, precisely because the narrative register itself signals portrait rather
    than incident report.
text: This is how the tradition remembers Antony's own struggle -- what it believed total combat against
  the interior enemy could involve. Athanasius portrays Antony shutting himself in an abandoned tomb for
  solitary combat, where he is assailed by demons taking the form of beasts, beating him nearly to death,
  and later by a vision of demons in the shape of wild animals filling the tomb entirely. Antony is portrayed
  emerging from these confrontations progressively strengthened rather than destroyed, until at last a
  vision of light comes to him, understood as divine aid arriving only once his own struggle had been
  sufficiently proven.
attested_occasion: Solitary enclosure in the tombs (Vita Antonii chs. 8-10) - the tradition's own portrait
  register, not incident report.
tellable_as: scene
voice_surface: 'This is how the tradition remembers Antony''s own struggle, what it believed total combat
  could involve - offered as portrait, explicitly marked, never as literal event-claim. Usage guidance
  (chunk, verbatim): The Representative may offer this as the tradition''s own account of what total spiritual
  combat was understood to look like, explicitly marked as such -- "This is how the tradition remembers
  Antony''s own struggle, what it believed total combat against the interior enemy could involve..." The
  Representative should not present the demons-as-beasts imagery as a claim about literal historical events,
  only as this world''s own chosen register for representing interior struggle at its most extreme.'
retrieval:
  tier: 3
  retrieve_when:
  - participant asks what total spiritual combat was understood to look like at its most extreme
  - participant asks about the logismoi in their most dramatic, embodied register
  - conversation reaches gravity 2 (spiritual combat) and wants the tradition's own fullest account of
    it, explicitly as portrait rather than history.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking for documented history rather than the tradition's own hagiographic self-portrait
      -- use Stories 001-003 instead for that register
  - condition_type: sense-disambiguation
    text: conversation concerns Evagrius's later systematized taxonomy of thoughts specifically (available
      but not default, per Doc_10 §2) rather than this story's own un-systematized, narrative-form precursor
      to that vocabulary.
  force_llm_vote: false
sources:
- source_id: srcDES001
  author_gravity_note: Contested (as portrait of this world's own understanding of combat); Inferential / Thin
    (any claim about what specifically happened in the tomb)
- source_id: srcDES020
  author_gravity_note: 'Source line (chunk): Athanasius, Life of Antony, chs. 8-10 -- hagiographic portrait,
    not incident report'
owner_figure_id: desertfig001
gravity_links:
- gravity_id: desertgrav002
  note: This is this world's own paradigmatic portrait of gravity 2 (spiritual combat), told not as a
    neutral chronicle but as the tradition's own account of what total ascetic struggle looks like when
    carried to its furthest extremity. It stands as the un-systematized, narrative-form precursor to Evagrius's
    later systematized taxonomy of the eight thoughts (gravity 9, Doc_06 §§2.2-2.3) -- available to Papnoute
    deliberately, not by default, per Doc_10 §2's own caution against defaulting to the Evagrian register.
- gravity_id: desertgrav009
  note: Named in this story's Formation Ecology Connection - full text on the first gravity_links note
    (CO-P2-04).
---
Migrated at S2.4 (2026-07-27) from `data/desert_world/story_chunks/desertstory007_antony-combat-in-tombs.md` (Story Text / Tier Justification / Usage Guidance verbatim from the chunk's own sections; occasion and telling-formula per chunk + Doc_09a). Tier-4 owner gap: see FLAG-003.

CO-P2-04 (2026-07-27): parked FLAG-004 sections restructured into gravity_links[] (FEC verbatim on the first link) and, for this record's tier-4 table, per-element sources[] entries.
