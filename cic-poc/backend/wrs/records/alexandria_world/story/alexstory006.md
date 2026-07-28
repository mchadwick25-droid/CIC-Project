---
id: alexstory006
world_id: alexandria-catechetical
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
cache_stability: static
title: The Markan Foundation of Alexandria
narrative_tier:
  tier: 3
  justification: 'An attributed apostolic-foundation narrative with no contemporary first- or second-century
    corroboration — the claim surfaces only in later sources (Eusebius, writing in the early fourth century)
    reconstructing origins from what by then was received tradition rather than eyewitness testimony.
    This is identity-bearing tradition, structurally comparable to other early churches'' apostolic-foundation
    claims (Rome''s Peter-and-Paul tradition, Edessa''s Addai tradition), and is offered on the same footing:
    real as a claim this community makes about itself, not documented as a first-century event.'
text: 'This world tells of its own beginning the way a household tells of its own founding: not as a matter
  it argues, but as a thing it simply knows about itself. The account it keeps is that Mark, the evangelist
  who wrote the second Gospel and who had been a companion of Peter, came to this city and first proclaimed
  the Gospel here, establishing the church that would grow into the community this world''s own life belongs
  to. The tradition does not dwell on the details of the visit — it is stated more than narrated, a claim
  of origin rather than a scene. What matters to those who hold it is what it establishes: that this city''s
  Christian life reaches back to the apostolic generation itself, through a companion of one of the Twelve,
  and is not a later or lesser thing than the churches that trace themselves to Peter or Paul directly.'
attested_occasion: The Markan foundation as first clearly asserted by Eusebius (HE 2.16, early 4th c.)
  - a later foundation-narrative carrying identity weight, not documented 1st-century history (Doc_01
  §2.2).
tellable_as: scene
owner_figure_id: alexfig009
voice_surface: 'We tell the founding story as what it is among us - a received foundation-narrative, first
  written down generations later, carried for its weight, not its documentation. Usage guidance (chunk,
  verbatim): Offer as the tradition''s own self-account — the story this community tells about where it
  came from — never as documented first-century history. The comparison to other cities'' apostolic-foundation
  claims (Rome, Edessa) may be useful for a participant who wonders whether this pattern is unique to
  this world; it is not, and naming that plainly keeps the claim honest without diminishing what it means
  to those who hold it.'
retrieval:
  tier: 3
  retrieve_when:
  - participant asks how this world's own church began, or where its founding story comes from
  - participant asks whether this world traces itself to an apostolic figure the way other cities do.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant wants this offered as documented first- or second-century history — it is not
  - condition_type: sense-disambiguation
    text: conversation needs the school's own teaching-lineage tradition instead (retrieve alexstory007,
      a related but distinct claim).
  force_llm_vote: false
sources:
- source_id: srcALX009
  locus: Eusebius, Historia Ecclesiastica 2.16 (Mark the Evangelist as founder)
gravity_links:
- gravity_id: alexgrav004
  note: 'This story functions less as an illustration of a specific gravity than as the ground of this
    world''s own identity-claim within the wider Church (Doc_01 §7–8) — it is the foundational-legitimacy
    counterpart to the intellectual-formation gravities (C1–C5) rather than a direct instance of any one
    of them. Where it touches a gravity at all, it is C4 (Logos-Centered Unity) in its broadest sense:
    the claim situates this world''s own life within the one apostolic movement the Logos initiated, rather
    than as a separate or derivative development.'
confidence_line: Contested (as tradition) / Inferential-Thin (as event)
---
Migrated at the S6.2 S2.4-equivalent (2026-07-27) from `data/alexandria_world/story_chunks/alexstory006_markan-foundation.md` (mapping in `wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage Guidance verbatim; occasion/owner/frame authored per Desert S2.4 conventions).

S2.5-equivalent (2026-07-27): the parked Formation Ecology Connection converted to typed gravity_links[] (CO-P2-04 - FEC verbatim on the first link's note); see wrs/migrate/s62_alx_s25.py.

CO-P2-16 (2026-07-28): confidence_line backfilled verbatim from the deployed chunk's Confidence front-matter line (live retrieval-context metadata); see wrs/migrate/s62_alx_s29_co16.py.
