---
id: halstory02
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
title: The Crisis in Rome
narrative_tier:
  tier: 1
  justification: Named author, datable, attested across multiple of the scholar's own letters rather than
    one isolated account, though the full causal interpretation (that Blaesilla's death and the pope's
    death together drove the departure) is the scholar's own framing. The claim that a formal proceeding
    reviewed his conduct is not well attested and is not part of this story at more than Inferential/Thin
    confidence.
text: A young woman among the household's earliest circle in Rome, Blaesilla, took up fasting with a severity
  that broke her health, and she died of it. The city laid the blame at the scholar's own door — his teaching,
  they said, had driven her to it. Within months, the pope whose favor had protected him in Rome also
  died, and without that protection, the hostility already gathering against him had nowhere left to be
  checked. He left the city that same year.
attested_occasion: 'Rome, 384-385: Blaesilla''s death after fasting that broke her health, the city''s
  blame laid at the scholar''s door, Damasus''s death removing his protection, and the departure that
  same year - the documented sequence attested across multiple of Jerome''s own letters; the full causal
  framing is his own, and any formal proceeding is Inferential/Thin at best (the chunk''s own confidence
  split).'
tellable_as: scene
owner_figure_id: halfig001
voice_surface: 'We tell what the record holds: a young woman of our first circle dead of the severity
  she took up, a city that blamed her teacher, a protector''s death, and a leaving. That the one drove
  the other is the scholar''s own telling; no trial or synod is in the record, and we add none. Usage
  guidance (chunk, verbatim): May be offered as historical narrative for the documented sequence (a death,
  a loss of protection, a departure). Must not be embellished with a formal "trial" or "synod" narrative
  — the source does not support that level of institutional process, only informal hostility and departure.'
confidence_line: Documented (sequence); Inferential/Thin (formal proceeding claim)
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks why the scholar left Rome
  - participant asks about opposition or scandal the household faced
  - participant asks about the death of a young woman named Blaesilla.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant asks specifically about the journey itself (retrieve story 01).
  force_llm_vote: false
sources:
- source_id: srcHAL001
  locus: Multiple letters of Jerome referencing the episode (see Doc_02 Author Gravity Assessment)
gravity_links:
- gravity_id: halgrav003
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at
    S2.5): Illuminates the patronage-as-authority gravity directly: this is the clearest demonstration
    in this world''s own record that authority resting on personal favor rather than office carries no
    institutional insulation. Also shapes the boundary structures lens — renunciation invited real public
    suspicion, not only admiration, in this specific season.'
---
Migrated at the S6.2/HAL S2.4-equivalent (2026-07-31) from `data/hieronymian_world/story_chunks/hal_story02_the-rome-crisis.md` (mapping in `wrs/migrate/s62_hal_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX-SYR S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] Illuminates the patronage-as-authority gravity directly: this is the clearest demonstration in this world's own record that authority resting on personal favor rather than office carries no institutional insulation. Also shapes the boundary structures lens — renunciation invited real public suspicion, not only admiration, in this specific season.
