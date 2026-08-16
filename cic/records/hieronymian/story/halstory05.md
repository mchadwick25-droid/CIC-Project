---
id: halstory05
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
title: A Death in the Sack of Rome
narrative_tier:
  tier: 1
  justification: Named author, near-contemporary (written two years after the event), but single-source
    with no independent corroboration.
text: 'When Alaric''s soldiers entered Rome, they came to the house of a widow who had given away most
  of her wealth years before. They demanded treasure she no longer had. She died soon after, from the
  injuries or deprivation that followed. The household''s own account dwells on the irony directly: soldiers
  searching a house that had already emptied itself for the poor.'
attested_occasion: 'Rome, 410: Alaric''s soldiers in the house of Marcella, demanding treasure given away
  years before; her death soon after from the injuries or deprivation - Jerome''s Ep. 127 to Principia,
  written two years after the event; single-source, no independent corroboration, and the reported irony
  follows the epitaph genre''s conventions (the chunk''s own genre caution).'
tellable_as: scene
owner_figure_id: halfig003
voice_surface: 'We tell how the Rome half of us ended: soldiers searching a house already emptied for
  the poor, and the widow who had emptied it dying of what followed. The irony is the epitaph''s own -
  real, but shaped by a mourner''s genre, and we carry it as such. Usage guidance (chunk, verbatim): May
  be offered as historical narrative for the bare event. The specific reported detail (soldiers demanding
  treasure from an already-emptied house) follows the epitaph genre''s conventions of dramatic irony and
  should be handled with the same genre-awareness as other epitaph material in this repository — real,
  but shaped by a commemorative genre, not a transcript.'
confidence_line: Widely Accepted (via Jerome's account; no independent corroboration)
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about the 410 sack of Rome
  - participant asks about the household's Rome-based leader
  - participant asks what ended the Rome half of this household.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant wants the full account of this widow's exegetical standing generally (retrieve story
      07 for that).
  force_llm_vote: false
sources:
- source_id: srcHAL001
  locus: Jerome, Epistula 127, to Principia
gravity_links:
- gravity_id: halgrav005
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at
    S2.5): The clearest ending-force in this world''s own bounded span — this event fractures the Rome-based
    pole of the household''s exegetical-authority gravity outright and ends Rome''s independent center
    of gravity within the wider network.'
chunk_slug: marcella-death
chunk_filename: hal_story05_marcella-death.md
---
Migrated at the S6.2/HAL S2.4-equivalent (2026-07-31) from `data/hieronymian_world/story_chunks/hal_story05_marcella-death.md` (mapping in `wrs/migrate/s62_hal_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX-SYR S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] The clearest ending-force in this world's own bounded span — this event fractures the Rome-based pole of the household's exegetical-authority gravity outright and ends Rome's independent center of gravity within the wider network.

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text field at
FRE 60.0 exactly, right at the boundary (FK 9.9 already clear). Per Mark's decision to extend the
readability pass to story records, the one long opening sentence is split at its own "demanding" clause
into two sentences, a single small nudge rather than a rewrite. No fact or hedge is dropped - the
soldiers, the widow's earlier gift of her wealth, her death from injuries or deprivation, and the
household's own genre-aware framing of the irony are unchanged. Re-scored: FK 8.0 / FRE 65.6, clearing
both thresholds.
