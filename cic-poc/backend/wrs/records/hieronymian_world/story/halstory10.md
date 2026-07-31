---
id: halstory10
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
title: A Day at the Double Monastery
narrative_tier:
  tier: 4
  justification: 'No single source narrates a specific day. This is explicitly a composite reconstruction
    of typical practice, not a story about a specific named individual on a specific day — meeting the
    Tier 4 discipline exactly: every element traceable to attested evidence, nothing invented or extrapolated
    beyond it.'
text: This is how it would have been, in the typical shape of a day at Bethlehem — not a specific day
  the household remembers, but the pattern its own life took. A day given over to prayer in common, alongside
  a day given over to the correction of a Hebrew word against its Greek rendering, were not different
  kinds of days for this household; both were the same discipline, worked at from different ends. Study
  of Hebrew continued under teachers who did not share the household's own faith, but whose learning was
  needed and paid for. Manual labor and the ordinary work of a large household ran alongside the scholarly
  correspondence that connected Bethlehem to Rome.
attested_occasion: 'Tier-4 composite: the typical shape of a day at the Bethlehem double monastery, assembled
  ONLY from attested elements (communal discipline per Ep. 108; Hebrew study under paid non-Christian
  teachers per the prefaces; the Bethlehem-Rome correspondence; manual labor by monastic-template analogy,
  declared as analogy) - no single source narrates a specific day, no individual is its subject (the chunk''s
  own Source Identification table, parked verbatim in this record''s body).'
tellable_as: scene
owner_figure_id: halfig009
voice_surface: 'This is no remembered day but the shape our days took - prayer and the correction of a
  Hebrew word held as one discipline worked from different ends. We say plainly that it is a pattern assembled
  from what is attested; and if you ask for the hours and the psalms, we will tell you honestly that no
  record of ours kept them. Usage guidance (chunk, verbatim): Appropriate as reconstruction of typical
  practice, explicitly marked as such when told. Must not include a specific liturgical horarium (which
  hours, which psalms) — that level of detail is not attested and is not supplied here.'
confidence_line: Inferential/Thin (always, for Tier 4, regardless of individual-element sourcing)
retrieval:
  tier: 4
  retrieve_when:
  - Participant asks what daily life at Bethlehem was like
  - participant asks for a concrete picture of the household's ordinary practice.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: Participant asks for a specific liturgical schedule (this world's own evidence does not support
      that level of specificity — the Representative should decline that specific request honestly rather
      than retrieve this chunk to fill it).
  force_llm_vote: false
sources:
- source_id: srcHAL001
  locus: 'Composite - elements per the chunk''s own Source Identification table (parked verbatim in this
    record''s body; the monastic-template element of halstory10 is declared analogy, Doc_01 SS6/Doc_08,
    no row owed): Composite — see Source Identification below'
- source_id: srcHAL023
  locus: 'Composite - elements per the chunk''s own Source Identification table (parked verbatim in this
    record''s body; the monastic-template element of halstory10 is declared analogy, Doc_01 SS6/Doc_08,
    no row owed): Composite — see Source Identification below'
---
Migrated at the S6.2/HAL S2.4-equivalent (2026-07-31) from `data/hieronymian_world/story_chunks/hal_story10_a-day-at-the-monastery.md` (mapping in `wrs/migrate/s62_hal_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX-SYR S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] Illuminates the formation-logic gravity directly — the fusion of ascetic discipline and scholarly labor as one practice, not two.

[Source Identification - the composite's own element-to-source table, parked verbatim (CO-P2-06 composite convention)] **Element: general structured common life.** Source: Jerome, Ep. 108 (general outline of communal discipline).
**Element: Hebrew study under named but non-Christian teachers.** Source: Jerome's own prefaces; Doc_01 §3.1 (Contested extent of his fluency, not asserted here beyond the bare fact of study).
**Element: correspondence connecting Bethlehem and Rome.** Source: the entire epistolary primary-source base (Doc_02 §1).
**Element: manual labor as part of communal life.** Source: general Egyptian/Palestinian monastic template this household adapted (Doc_01 §6, Doc_08 force 2A-3), by analogy — not directly attested for this specific community's own schedule.

[Absent Story Note - the chunk's own honest-brevity rule, parked verbatim] This chunk deliberately does not supply a specific horarium (hours of prayer, specific psalms used) because no source attests one for this specific community — only the general fact of structured common life. A participant asking for the schedule should receive honest brevity, not an invented timetable.
