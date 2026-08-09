---
id: pahcstory002
world_id: post-apostolic-house-church
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
cache_stability: static
title: 1 Clement's Intervention in the Corinthian Dispute
narrative_tier:
  tier: 1
  justification: A specific, named occasion — the deposition of legitimately appointed Corinthian presbyters
    — addressed in a real, surviving letter. The letter itself is anonymous; attribution to "Clement"
    is traditional (first attested by later writers, not self-declared in the text), which is why Confidence
    is Widely Accepted for the intervention itself but Contested for the precise date, since dating arguments
    partly rest on assumptions about Clement's own identity and career.
text: 'In this letter, the church at Rome — writing anonymously in its own text, though later tradition
  names Clement as its author — tells us that the church at Corinth had removed certain presbyters from
  office who had served blamelessly. The letter addresses this directly: it argues at length that the
  Corinthians'' action was a departure from proper order, drawing on scriptural example after scriptural
  example of jealousy and strife destroying what unity had built, and it urges the restoration of the
  deposed presbyters.


  The letter does not claim any formal jurisdiction over Corinth — it does not command, in the register
  of a later ecclesial authority; it appeals, at length and with real theological seriousness, as one
  church writing to another out of concern. Rome''s own letter tells us Rome believed disputes in a sister
  church were its business to address, even without institutional authority to compel a result.'
attested_occasion: 'Rome''s letter to Corinth (trad. c. 96; contested range 80-140): presbyters removed
  without cause, and a sister church''s long, scripture-laden appeal for their restoration - appealing,
  never commanding; anonymous in its own text, ''Clement'' a traditional attribution the letter itself
  does not make (the chunk''s own confidence split).'
tellable_as: scene
owner_figure_id: pahcfig002
voice_surface: 'We tell how Rome wrote to Corinth - one church to another, with no power to compel and
  no bishop invoked, only the long argument that removing blameless presbyters tears what unity built.
  The letter names no author; later memory calls him Clement, and we pass that name on as memory, not
  as the letter''s own word. Usage guidance (chunk, verbatim): The Representative may offer this as remembered
  history — Rome''s own church writing to correct a specific dispute — while naming that the letter''s
  own text does not self-identify its author, and that "Clement" is a traditional attribution the letter
  itself does not make. The Representative does not claim more certainty about authorship or exact date
  than the source supports.


  Additional guidance specific to this story: this is Strand B material. It should not be presented as
  evidence for a Strand A monarchical-bishop reading — the letter''s own argument works from presbyteral,
  not episcopal, office.'
confidence_line: Widely Accepted (that Rome intervened) / Contested (exact date)
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks how disputes between church leaders were handled
  - participant asks about G01 (Authority Consolidation) or G02 (Translocal Correspondence Network)
  - participant asks about Strand B (Rome/plural-presbyter) governance
  - conversation reaches questions of how one church's letter to another functioned, or what happens when
    a community removes its own leaders.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant has just received Story 001 and a second correspondence-network example would be
      redundant in the same exchange
  - condition_type: sense-disambiguation
    text: conversation needs specifically Strand A material.
  force_llm_vote: false
sources:
- source_id: srcPAHCP02
  locus: 1 Clement (Registry P02), traditionally dated c. 96 CE, Contested range 80–140 CE.
gravity_links:
- gravity_id: pahcgrav002
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at S2.5):
    This is the other kind of letter-network: activated not by one man''s crisis but by one community''s
    concern for another''s internal order. It also shows the council pattern from the inside. The letter''s
    argument assumes that elders hold a real, structured office which removing them without cause violates -
    and it makes that case without ever appealing to a single bishop. So translocal concern was not peculiar
    to the bishop-centred communities. A community governed by a council of elders exercised its own
    translocal voice, through sustained argument rather than personal urgency.'
- gravity_id: pahcgrav001
  note: Named in the same FEC (full text on this record's first gravity link).
---
Migrated at the S6.2/PAHC S2.4-equivalent (2026-07-31) from `data/pahc_world/story_chunks/pahcstory002_1clement-corinthian-dispute.md` (mapping in `wrs/migrate/s62_pahc_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; sources extracted mechanically from the Source line's own Registry tags; occasion/owner/frame authored per the fleet S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] This story is Strand B's own version of G02 (Translocal Correspondence Network, Primary) — a network activated not around personal crisis (as in Story 001) but around institutional concern for a sister community's internal order. It also connects to G01 (Authority Consolidation, Supporting) from the Strand B (plural-presbyter) side: the letter's own argument assumes presbyters hold a legitimate, structured office that removal without cause violates, without invoking a monarchical bishop to make that case.

This story shows something Story 001 cannot: that translocal concern and correspondence were not unique to Strand A's bishop-centered, crisis-driven mode. Rome's own plural-presbyter community exercised its own form of translocal voice through sustained theological argument rather than personal urgency.
