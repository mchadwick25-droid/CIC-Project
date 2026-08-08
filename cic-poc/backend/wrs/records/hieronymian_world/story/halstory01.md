---
id: halstory01
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
title: The Departure from Rome and the Journey to Bethlehem
narrative_tier:
  tier: 1
  justification: Named author (the scholar, writing to Eustochium), datable (composed near the time of
    Paula's 404 death, describing events of 385-386), historically credible in broad outline though authored
    by an interested party and single-sourced. Meets Tier 1's core test of direct textual attestation
    with a named author and identifiable social location.
text: 'In his letter to Eustochium, written to mark her mother''s death, the scholar among us records
  the journey plainly: how he himself left Rome first, in the month named for the harvest, and how Paula
  and her daughter followed within a month, sailing from the port below the city. He tells of the stop
  at Cyprus, where the bishop there received them; of the slower road through Antioch and down into Palestine
  and Egypt; of Nitria, where a bishop and countless monks came out to meet them, and where Paula wished,
  and was refused, to stay among them rather than press on toward the Holy Land. He tells us she turned
  back toward Jerusalem instead, and that from there the household settled at last near Bethlehem, by
  the cave where the Lord was born.'
attested_occasion: The 385 departure from Rome and the journey through Cyprus, Antioch, Egypt (Nitria
  - where Paula wished, and was refused, to stay), and Palestine to Bethlehem - as Jerome records it in
  Ep. 108, the epitaph letter written to Eustochium near the time of Paula's 404 death; named author,
  datable, credible in broad outline, but authored by an interested party and single-sourced (the chunk's
  own Tier Justification).
tellable_as: scene
owner_figure_id: halfig002
voice_surface: 'We tell the journey as the scholar set it down for Paula''s own daughter, after her death.
  He left first, in the month named for the harvest; she followed within the month. Then
  Cyprus, Antioch, the monks of Nitria who nearly kept her, and the road that ended by the
  cave at Bethlehem. One pen holds this memory, and we say whose. Usage guidance (chunk,
  verbatim): May be offered as historical narrative, with the author and his relationship to
  Paula (writing to her own daughter, after her death) explicitly named where relevant. The
  specific roster of monks named at Nitria in the source text is a rhetorical flourish, not a
  literal list of individuals personally received — this detail should not be offered as
  itemized fact if a participant probes it.'
confidence_line: Documented-to-Widely Accepted (narrative level)
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks how the household came to Bethlehem
  - participant asks about the 385 departure from Rome
  - participant asks about the journey through Egypt and Palestine.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant is asking specifically about the 384-385 Rome crisis's causes (retrieve story 02
      instead)
  - condition_type: sense-disambiguation
    text: participant asks about daily life at Bethlehem itself (retrieve story 10).
  force_llm_vote: false
sources:
- source_id: srcHAL001
  locus: Jerome, Epistula 108 (Epitaphium Sanctae Paulae), to Eustochium
gravity_links:
- gravity_id: halgrav003
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at
    S2.5): Illuminates the patronage gravity (the journey and its funding depended entirely on Paula''s
    own wealth) and the bipolar Rome/Bethlehem geography that organizes this world''s whole structure.
    Shows the physical, costly reality behind the abstract fact of "relocation" — a household uprooting
    itself deliberately, twice over (once from Rome, once from the temptation to remain in Egypt), in
    pursuit of a single settled place to do its work.'
---
Migrated at the S6.2/HAL S2.4-equivalent (2026-07-31) from `data/hieronymian_world/story_chunks/hal_story01_departure-from-rome.md` (mapping in `wrs/migrate/s62_hal_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX-SYR S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] Illuminates the patronage gravity (the journey and its funding depended entirely on Paula's own wealth) and the bipolar Rome/Bethlehem geography that organizes this world's whole structure. Shows the physical, costly reality behind the abstract fact of "relocation" — a household uprooting itself deliberately, twice over (once from Rome, once from the temptation to remain in Egypt), in pursuit of a single settled place to do its work.
