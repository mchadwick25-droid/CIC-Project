---
id: desertstory005
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
title: Abba Arsenius's Call to Flee, Be Silent, Be Still
narrative_tier:
  tier: 2
  justification: Same basis as Story 004 -- attributed to a named figure, preserved through the compiled
    tradition rather than a contemporary datable text. Arsenius's own historical existence and imperial-court
    background are independently well-attested in the broader tradition, but this world's own evidence
    base does not extend to full verification of his court career specifically, and this document does
    not overclaim it. Confidence is Widely Accepted for the saying's place in the tradition; Inferential / Thin
    for the specific court-tutor biographical frame.
text: 'The tradition tells that Arsenius, while still a tutor in the imperial court at Constantinople,
  prayed for guidance, and heard a voice say: "Arsenius, flee the company of men and you will be saved."
  Having withdrawn to Egypt, he prayed again, and heard: "Arsenius, flee, be silent, be still -- these
  are the roots of sinlessness."'
attested_occasion: Prayer for guidance while still tutor at the imperial court, and again after withdrawal
  to Egypt (Apophthegmata, Arsenius, Alphabetical Collection).
tellable_as: scene
voice_surface: 'They say of Abba Arsenius that... - the court frame told thinly, as the tradition gives
  it, without elaboration. Usage guidance (chunk, verbatim): Told as tradition, not verified biography
  -- "They say of Abba Arsenius that..." Particularly useful for illustrating gravity 1''s own logic in
  its most compressed, memorable form -- a call, a departure, and a further call once the departure was
  already made.'
retrieval:
  tier: 2
  retrieve_when:
  - participant asks why someone would leave a position of status or comfort for withdrawal
  - participant asks what hesychia (stillness) actually is, or how it is sought rather than merely described
  - conversation reaches gravity 1 (withdrawal) or gravity 3 (personal, directly-addressed guidance) in
    their most compressed, memorable form.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: conversation is asking for elaboration on Arsenius's court career beyond this brief biographical
      frame -- this document does not extend its own evidence base to full verification of that career,
      and neither should the Representative
  - condition_type: sense-disambiguation
    text: participant is asking about a different elder's own call story (see Stories 001, 004, 006).
  force_llm_vote: false
sources:
- source_id: srcDES005
  author_gravity_note: Widely Accepted (the saying's place in the tradition); Inferential / Thin (the specific
    court-tutor biographical frame)
- source_id: srcDES021
  author_gravity_note: 'Source line (chunk): Apophthegmata Patrum, Arsenius (Alphabetical Collection)'
owner_figure_id: desertfig005
gravity_links:
- gravity_id: desertgrav001
  note: This story directly illustrates gravity 1 (withdrawal), gravity 3 (the personal, directly-addressed
    mode of guidance this world's own authority structure assumes throughout), and hesychia (Doc_06 §1.3)
    as a named, actively sought discipline rather than a passive absence of noise.
- gravity_id: desertgrav003
  note: Named in this story's Formation Ecology Connection - full text on the first gravity_links note
    (CO-P2-04).
---
Migrated at S2.4 (2026-07-27) from `data/desert_world/story_chunks/desertstory005_arsenius-flee-be-still.md` (Story Text / Tier Justification / Usage Guidance verbatim from the chunk's own sections; occasion and telling-formula per chunk + Doc_09a). Tier-4 owner gap: see FLAG-003.

CO-P2-04 (2026-07-27): parked FLAG-004 sections restructured into gravity_links[] (FEC verbatim on the first link) and, for this record's tier-4 table, per-element sources[] entries.
