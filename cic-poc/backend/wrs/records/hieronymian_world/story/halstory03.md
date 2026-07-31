---
id: halstory03
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
title: The Word That Changed a Congregation's Prayer (the Oea Incident)
narrative_tier:
  tier: 1
  justification: Two named authors (Jerome and Augustine), both sides independently attested in their
    own surviving letters — the rare case in this world's evidence where "the other side" of a dispute
    is not lost to a single author's framing.
text: 'In one town, a bishop read from the corrected text in the assembly, at the passage where the prophet
  Jonah sits beneath a plant for shade. Where the congregation had always heard "gourd," the corrected
  word, closer to the Hebrew, gave "ivy" — a climbing vine, not a gourd-plant. The change was small. The
  reaction was not: the people took it as tampering with scripture they trusted, and the disturbance reached
  as far as a respected bishop in Africa, Augustine, who wrote to raise the concern directly and press
  it more than once.'
attested_occasion: 'Oea: a bishop reads the corrected text of Jonah - ''ivy'' where the congregation had
  always heard ''gourd'' - and the disturbance reaches Augustine in Africa, who presses the concern by
  letter more than once (Ep. 112 = Augustine''s Ep. 75); the rare two-sided case - both parties independently
  attested in their own surviving letters.'
tellable_as: scene
owner_figure_id: halfig001
voice_surface: 'We tell the gourd and the ivy as both sides kept it - the congregation''s anger at a changed
  word, and the African bishop''s letters pressing the question. Neither voice is ours to silence: this
  quarrel survives in two hands, and we tell it two-handed. Usage guidance (chunk, verbatim): May be offered
  as historical narrative, with both Jerome''s and Augustine''s perspectives nameable and neither privileged
  over the other — this is a genuine, two-sided historical exchange, not a story told only from this household''s
  own side.'
confidence_line: Documented
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about the cost of the Hebrew-translation project
  - participant asks about disagreement with Augustine
  - participant asks for a concrete example of the Hebraica veritas dispute.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant wants an abstract explanation of Hebraica veritas alone (use the lexicon chunk for
      that, retrieve this story only when a concrete cost/example is wanted).
  force_llm_vote: false
sources:
- source_id: srcHAL009
  locus: Jerome, Epistula 112 (= Augustine's Epistula 75); the wider Jerome-Augustine correspondence
---
Migrated at the S6.2/HAL S2.4-equivalent (2026-07-31) from `data/hieronymian_world/story_chunks/hal_story03_the-oea-incident.md` (mapping in `wrs/migrate/s62_hal_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX-SYR S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] Illuminates the *Hebraica veritas* gravity at its most concrete and costly — not an abstract scholarly preference but a change that could unsettle an actual congregation's prayer, and a dispute conducted, by letter, with one of the era's most respected bishops. Also illuminates the epistula gravity: this dispute was conducted entirely through correspondence.
