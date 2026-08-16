---
id: pahcstory003
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
title: Polycarp Forwards Ignatius's Letters to Philippi
narrative_tier:
  tier: 1
  justification: A specific, directly attested transmission event, named by the person who performed it,
    in his own surviving letter. The uncertainty here is not about whether the act happened but about
    the letter's own composition history — some scholars (following Harrison) argue *To the Philippians*
    is a composite of two originally separate letters, which affects how confidently this passage can
    be dated relative to Ignatius's own journey (Story 001).
text: 'In his letter to the Philippians, Polycarp tells the Philippian church that he is sending them the
  collected letters of Ignatius. Polycarp''s community had gathered these letters, and now sent them at
  the Philippians'' own request. Polycarp names himself only as "one of the presbyters," not as bishop,
  though later tradition remembers him as Smyrna''s bishop. "The letters of Ignatius which he sent to us,
  and any others we had by us, we have sent to you, as you requested," he writes, "from which you will
  be able to derive great advantage."


  It is a small, practical act, described in a single line. But it tells us something no larger claim
  could: that letters moved between named individuals, at specific requests. At least one community made
  a point of collecting and keeping them for others.'
attested_occasion: Polycarp's forwarding of the collected Ignatius letters to Philippi at their request
  (Philippians 13) - the correspondence network's ordinary, almost administrative operation; the Harrison
  two-letter-splice question carried as the chunk carries it (affects dating confidence, not the act's
  attestation).
tellable_as: background-fact
owner_figure_id: pahcfig003
voice_surface: 'A small thing, told in a single line of his own letter: they asked for the letters, and
  he sent what his community had gathered. We tell it because it shows the network at its most ordinary
  - not a postal system, but one named man doing one requested kindness. And we note what he calls himself
  there: one of the presbyters, not bishop. Usage guidance (chunk, verbatim): The Representative may offer
  this as a small, concrete instance of how the correspondence network actually functioned — one named
  person doing one specific, requested thing — without overstating its scale. This is not evidence of
  a formal postal system; it is evidence of personal, relationship-based transmission.


  Additional guidance specific to this story: Polycarp names himself "one of the presbyters" here, not
  bishop — a detail worth naming if a participant asks whether Polycarp fits cleanly into Strand A''s
  monarchical-bishop pattern. He does not, cleanly; this is one of this world''s own disclosed tensions,
  not resolved by this document.'
confidence_line: Documented (the forwarding act, as textual content) / Contested (the letter's own unity
  and precise dating)
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks for a small, concrete example of how the correspondence network actually functioned
  - participant asks about Polycarp specifically, ahead of or alongside Story 008
  - conversation needs a brief, low-stakes illustration of G02 rather than the high-drama Story 001.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant needs the fuller, higher-stakes correspondence story — use Story 001 or 002 instead
  - condition_type: sense-disambiguation
    text: this story is best as a supporting detail, not a centerpiece.
  force_llm_vote: false
sources:
- source_id: srcPAHCP04
  locus: Polycarp of Smyrna, *Letter to the Philippians*, ch. 13 (Registry P04).
gravity_links:
- gravity_id: pahcgrav002
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at S2.5): A
    small, concrete point about the letter-network, and one of the few we have. Where one story shows the
    network moving in a crisis and another shows it moving over a community''s internal order, this one
    shows it in its ordinary, almost administrative working: collecting, requesting and forwarding letters
    as a routine act of care between communities.'
chunk_slug: polycarp-forwards-letters
---
Migrated at the S6.2/PAHC S2.4-equivalent (2026-07-31) from `data/pahc_world/story_chunks/pahcstory003_polycarp-forwards-letters.md` (mapping in `wrs/migrate/s62_pahc_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; sources extracted mechanically from the Source line's own Registry tags; occasion/owner/frame authored per the fleet S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] This is a small, concrete data point for G02 (Translocal Correspondence Network, Primary) — one of its three founding data points. Where Story 001 shows the network activated by crisis and Story 002 shows it activated by institutional concern, this story shows its ordinary, almost administrative operation: collecting, requesting, and forwarding letters as a routine act of care between communities.

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text field at
FK grade 18.9 / FRE 37.2 - the opening sentence carried a parenthetical em-dash aside naming Polycarp's
self-description mid-sentence, and the closing sentence stacked a colon-introduced double claim. Per Mark's
decision to extend the readability pass to story records, both long sentences are split into short ones
along their own existing clause boundaries (one clause per sentence, in the same order); no plain-synonym
substitution was needed beyond "preserving" -> "keeping." The two embedded direct quotations (Polycarp's
"one of the presbyters" self-description and his full closing sentence, "The letters of Ignatius which he
sent to us...") are untouched, word for word. No fact, hedge, or attribution is dropped - the request from
Philippi, Polycarp's own self-naming as presbyter rather than bishop, and the later tradition that remembers
him as bishop are all still stated in full. Re-scored: FK 9.5 / FRE 61.3, clearing both thresholds.
