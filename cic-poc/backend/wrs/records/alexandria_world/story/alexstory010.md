---
id: alexstory010
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
title: A Typical Catechumen's Formation (Composite, Marked as Reconstruction)
narrative_tier:
  tier: 4
  justification: 'A narration of typical practice, not a specific named individual, with every element
    traceable to attested evidence within this world''s own horizon: the staged catechumenate is Clement''s
    own description of how his community formed newcomers; the daily prayer-and-Scripture rhythm is Origen''s
    own treatise on the practice of prayer; the festal and Paschal cycle is directly attested in Athanasius''s
    own Festal Letters. No element in this composite is invented; the composite itself — stitching these
    attested elements into a single narrated passage — is the reconstructive move, and it is marked as
    such rather than offered as remembered history. This meets Tier 4''s criteria exactly: historically
    grounded, explicitly labeled, never claiming the status of a documented individual account.'
text: 'Offered explicitly as a picture of the shape of things, not a known person''s history: a seeker
  comes to this world''s own community wanting to know God, and is received first as a catechumen, given
  time and staged instruction before ever approaching the water — the tradition is explicit that formation
  here is not a single decision but a passage with stages, each one preparing the ground for the next.
  Across the months of that preparation, the rhythm of an ordinary day is shaped by prayer at set points
  and Scripture returned to again and again, not read once and set aside but taken up daily as something
  inexhaustible. The year itself carries its own larger rhythm, turning on the great fast and the feast
  that follows it, so that the catechumen''s own formation is carried inside a community-wide cycle that
  does not pause for any one person''s readiness but that any person''s readiness is drawn along by. This
  is the shape this world''s own attested sources describe when they describe formation in practice —
  not any one person''s particular story, but the pattern a great many particular stories, had we them,
  would likely have shared.'
attested_occasion: 'Tier-4 composite: a typical catechumen''s formation path assembled only from attested
  elements (catechumenal stages, scrutinies, baptism at Pascha); no single attested person - the composite
  is the community''s own pattern (CO-P2-06 convention).'
tellable_as: scene
owner_figure_id: alexfig011
voice_surface: 'This is no one person''s remembered story - it is the shape of the path itself, assembled
  from what our record attests, and we say so when we tell it. Usage guidance (chunk, verbatim): Must
  always be introduced as reconstruction — "this is the shape a typical formation likely took," never
  "this is what happened to a known person." This narration concerns the school-and-community''s own attested
  *practice*; it is not, and must never be offered as, an account of the non-literate majority''s interior
  formation. That remains a named absence in this world''s own record (Doc_09 §3): the majority''s channels
  of formation (the assembly, the Eucharist, the fast) are known and may be named, but their inner experience
  of that formation is not reconstructed here or anywhere in this inventory, and this composite does not
  fill that absence by extension or implication.'
retrieval:
  tier: 4
  retrieve_when:
  - participant asks what a typical formation in this world actually looked like, day to day and stage
    to stage — not a specific known person's story, but the shape of the practice as this world's own
    attested sources describe it.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant wants this offered as a specific, named, historically known individual's story —
      it is not
  - condition_type: sense-disambiguation
    text: participant wants this to stand in for the non-literate majority's own interior formation —
      it explicitly does NOT do this (that remains a named absence, Doc_09 §3)
  - condition_type: sense-disambiguation
    text: this story must always be introduced as reconstruction, never as remembered history.
  force_llm_vote: false
sources:
- source_id: srcALX003
  locus: 'COMPOSITE — built only from attested elements: the staged catechumenate (Clement, Paedagogus),
    the daily prayer-and-Scripture rhythm (Origen, On Prayer), the festal/Paschal cycle (Athanasius, Festal
    Letters)'
- source_id: srcALX001
  locus: 'COMPOSITE — built only from attested elements: the staged catechumenate (Clement, Paedagogus),
    the daily prayer-and-Scripture rhythm (Origen, On Prayer), the festal/Paschal cycle (Athanasius, Festal
    Letters)'
- source_id: srcALX002
  locus: 'COMPOSITE — built only from attested elements: the staged catechumenate (Clement, Paedagogus),
    the daily prayer-and-Scripture rhythm (Origen, On Prayer), the festal/Paschal cycle (Athanasius, Festal
    Letters)'
---
Migrated at the S6.2 S2.4-equivalent (2026-07-27) from `data/alexandria_world/story_chunks/alexstory010_typical-catechumen.md` (mapping in `wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage Guidance verbatim; occasion/owner/frame authored per Desert S2.4 conventions).

[Formation Ecology Connection — parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] Illustrates C3 (Divine Pedagogy) and C5 (Learning-Formation Integration) as lived, staged, and communally embedded practice rather than as abstract claims — the graduated ascent this world's construction record names (catechesis → illumination → the knowing that transforms) rendered as the shape of an actual passage through time. It also grounds C1 and C2's claim that Scripture and transformation are inseparable, showing the daily rhythm of return to Scripture as ordinary practice, not exceptional discipline reserved for the learned few.
