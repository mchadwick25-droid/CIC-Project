---
id: desertstory004
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
title: Abba Moses and the Leaking Jug
narrative_tier:
  tier: 2
  justification: Attributed to a named figure but transmitted through the compiled Apophthegmata tradition
    (5th-6th century compilation, per Doc_02 §2.3's compiler-mediation caveat, carried forward at Doc_08
    Force 3B-ii) rather than through a datable, single-authored text contemporary with the events. Confidence
    is Widely Accepted as to the saying's genuine place within the tradition; Contested/Inferential as
    to whether this specific incident occurred as narrated versus condensing a more general teaching pattern
    into a single memorable scene.
text: 'The tradition tells that a brother at Scetis had committed a fault, and a council of elders was
  called to judge him. Abba Moses at first refused to attend. When pressed, he came anyway, carrying a
  jar with a crack in it, filled with water, the water running out behind him the whole walk to the gathering.
  When the others asked what this meant, he said: "My sins run out behind me, and I do not see them, and
  today I am coming to judge the errors of another." Hearing this, the assembly forgave the brother and
  said no more to him.'
attested_occasion: A council at Scetis called to judge a brother's fault; Moses, pressed to attend, arriving
  with the leaking jar (Apophthegmata, Moses, Alphabetical Collection).
tellable_as: scene
voice_surface: 'The tradition tells of Abba Moses that... - told as community tradition, never as verified
  single-event history; his story, kept on his name. Usage guidance (chunk, verbatim): Told as community
  tradition -- "The tradition tells of Abba Moses that..." -- not as verified single-event history. The
  Representative should not claim the specific council scene as historically documented fact, only as
  the tradition''s own preserved teaching.


  **Additional guidance:** This story was directly implicated in live adversarial testing, which found
  it fabricated-then-corrected under a first attempt that misattributed it to a different figure ("Macarius")
  and altered its content. The Permanent Prompt now carries an explicit named-attribution guard built
  around exactly this story. Any deployment monitoring for drift should watch this story specifically
  as the canonical test case.'
retrieval:
  tier: 2
  retrieve_when:
  - participant asks about self-judgment, humility, or how this tradition handles the temptation to judge
    another's failing
  - conversation reaches gravity 5 (diakrisis) in its self-directed register
  - Representative needs the single most load-bearing, exactly-attested named story it carries.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking for a specific, unattested episode about Moses beyond this one saying
      -- the Permanent Prompt's own guard exists precisely because this is the only story this Representative
      carries whole for this figure, and it should not be extended or embellished
  - condition_type: sense-disambiguation
    text: conversation concerns a different elder's own saying (see Stories 005-006).
  force_llm_vote: false
sources:
- source_id: srcDES005
  author_gravity_note: Widely Accepted (the saying's genuine place within the Apophthegmata tradition);
    Contested/Inferential (whether this specific incident occurred as narrated, versus condensing a general
    teaching pattern into one memorable scene)
- source_id: srcDES021
  author_gravity_note: 'Source line (chunk): Apophthegmata Patrum, Moses (Alphabetical Collection)'
owner_figure_id: desertfig004
---
Migrated at S2.4 (2026-07-27) from `data/desert_world/story_chunks/desertstory004_moses-leaking-jug.md` (Story Text / Tier Justification / Usage Guidance verbatim from the chunk's own sections; occasion and telling-formula per chunk + Doc_09a). Tier-4 owner gap: see FLAG-003.
