---
id: desertstory003
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
title: Pachomius's Founding of the Koinonia at Tabennesi
narrative_tier:
  tier: 1
  justification: Named textual tradition with a datable founding event, but the multiple, only partially
    overlapping recensions of the Lives carry a genuinely live, unresolved version-priority debate (Doc_01
    §10; Doc_02 §1.2) that this document does not adjudicate. This story is held at Tier 1 for the broad,
    cross-recension-consistent outline -- founding date range, house count, membership scale at Pachomius's
    death -- rather than for incident-level detail specific to any single recension.
text: The Lives record that Pachomius, an early convert following military service, founded the first
  cenobitic community at Tabennesi in the Thebaid around 320, joined initially by his own brother John
  and then by additional companions. He established a written Rule, common property held by the community
  rather than by any individual, and a working hierarchy of housemasters and stewards to keep the community's
  shared life ordered. By the time of his death in 346, the koinonia had grown to nine houses for men
  and two for women.
attested_occasion: The founding at Tabennesi c. 320, joined first by his brother John; by his death in
  346, nine houses for men and two for women (the Lives, cross-recension outline).
tellable_as: scene
voice_surface: 'The Lives record it; we tell the broad outline all recensions share and say plainly that
  their textual history is tangled. Usage guidance (chunk, verbatim): May be told as remembered history,
  with the caveat -- offered if the conversation reaches that depth -- that the Lives'' own textual history
  is complex, and that this account does not claim priority for any single recension''s specific wording.
  When a participant asks which authority mode this world actually trusted, this story should be paired
  honestly with the elder-authority sayings (Stories 004-006), not used alone to suggest the office-based
  pattern settled the question.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks about communal or cenobitic life specifically, or how a written rule and common household
    came to exist alongside solitary withdrawal
  - conversation reaches gravity 6 (koinonia) or the person-based/office-based authority tension (gravity
    10)
  - Representative needs to speak from genuine Strand B fluency rather than a Strand C vantage point describing
    it from outside.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about Strand A's solitary pattern (see Stories 001-002, 007) or Strand
      C's semi-anchoritic pattern (see Story 008)
  - condition_type: sense-disambiguation
    text: conversation asks for a resolved answer about which authority mode -- elder-word or written
      rule -- is more truly authoritative, since this world never settled that question and this story
      should not be used to imply it did.
  force_llm_vote: false
sources:
- source_id: srcDES002
  author_gravity_note: 'Widely Accepted (broad outline: founding date range, house count, membership scale
    at Pachomius''s death); Contested (recension-specific detail, given the live version-priority debate
    across the Bohairic, Sahidic, and Greek Lives)'
- source_id: srcDES018
  author_gravity_note: 'Source line (chunk): The Pachomian corpus -- the Lives of Pachomius (Bohairic,
    Sahidic Coptic, and Greek recensions) and the Pachomian Rule'
owner_figure_id: desertfig002
gravity_links:
- gravity_id: desertgrav006
  note: 'This is where the common life begins among us - the shared rule, the shared table, the brothers under one
    roof. It stands alongside the elder-and-disciple way rather than replacing it, and the two never quite
    became one thing. Whether authority rests in a person tested by God or in an office held under a rule is
    the one question this world never collapsed into a single answer. Both ways were ours, at the same time,
    and we carry both.'
- gravity_id: desertgrav010
  note: Named in this story's Formation Ecology Connection - full text on the first gravity_links note
    (CO-P2-04).
chunk_slug: pachomius-founding-koinonia-tabennesi
---
Migrated at S2.4 (2026-07-27) from `data/desert_world/story_chunks/desertstory003_pachomius-founding-koinonia-tabennesi.md` (Story Text / Tier Justification / Usage Guidance verbatim from the chunk's own sections; occasion and telling-formula per chunk + Doc_09a). Tier-4 owner gap: see FLAG-003.

CO-P2-04 (2026-07-27): parked FLAG-004 sections restructured into gravity_links[] (FEC verbatim on the first link) and, for this record's tier-4 table, per-element sources[] entries.
