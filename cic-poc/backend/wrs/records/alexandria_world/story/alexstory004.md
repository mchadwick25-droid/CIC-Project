---
id: alexstory004
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
title: The Sayings of the Desert Fathers (referenced near the horizon)
narrative_tier:
  tier: 2
  justification: 'A collected tradition with an identifiable, datable collection history (late 4th–5th
    century compilation), academically treated as authentic evidence of what a community remembered and
    valued even where individual attribution to a specific named elder cannot be independently verified.
    This meets Tier 2''s criteria precisely: real evidentiary weight as collected tradition, without the
    direct textual attestation a Tier 1 claim would require. The Contested status of individual attributions
    (which saying truly belongs to which named abba, versus later convergence onto a well-known name)
    is carried explicitly rather than smoothed over.'
text: 'Near this world''s own edge stand voices this world knows of but does not itself produce: the sayings
  kept and handed down from the elders who went out into the desert — Antony, Macarius, Poemen, and many
  more, named and unnamed, whose brief, tested words on humility, discernment, and the taming of the mind
  were treasured and repeated by those who sought them out. This world''s own teachers knew of that movement,
  respected the seriousness of its pursuit of God, and in Antony''s case in particular held him up as
  a formation-ideal worth telling of (see alexstory005). But the sayings themselves — their content, their
  form, the discipline of cell and manual labor and unceasing watchfulness they distill — belong to a
  different life than the one lived in the reading-room and the school. This world can gesture toward
  that near neighbor. It cannot speak from inside it.'
attested_occasion: Sayings collected late 4th-5th c.; individual attributions moderate; world-attribution
  held open (cross-build provisional, Doc_01 §3.3).
tellable_as: background-fact
owner_figure_id: alexfig011
voice_surface: 'These sayings are kept collections whose desert-or-city belonging our own record holds
  open - we say so when we reach for them. Usage guidance (chunk, verbatim): This is the one story in
  this inventory governed first by a cross-build constraint, not primarily by its own tier. It may be
  referenced as material this world''s own teachers knew of and respected, standing near this world''s
  temporal and geographic edge — never offered as this world''s own formation logic, and never voiced
  as though this world''s own teachers produced or systematically practiced it. A participant whose question
  genuinely wants the desert''s own interior should be redirected honestly, not answered from a borrowed
  voice.'
retrieval:
  tier: 2
  retrieve_when:
  - participant asks about the desert tradition near this world's own edge, or how the school-tradition's
    teachers regarded the ascetic movement growing alongside them.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking this world to speak the desert's sayings AS its own formation logic —
      the world-attribution of this material is HELD OPEN (Doc_01 §3.3) and this world does not claim
      it
  - condition_type: sense-disambiguation
    text: retrieve the Desert Christianity world's own construction for that. Do not offer any individual
      saying as securely attributed to the named abba without the attribution's own Contested status carried
      alongside it.
  force_llm_vote: false
sources:
- source_id: srcALX011
  locus: Apophthegmata Patrum — Sayings of the Desert Fathers (collected late 4th–5th c.; named abbas
    including Antony, Macarius, Poemen, plus anonymous material)
gravity_links:
- gravity_id: alexgrav014
  note: This material sits at the boundary this world's own construction record deliberately holds open
    (Doc_01 §3.3; Doc_04's cross-build constraint) rather than inside any of the confirmed gravities.
    It is retrieved not to illustrate C1–C5 as this world's own organizing forces, but to mark honestly
    where this world's own life brushes against — without absorbing — the distinct Desert Christianity
    ecology. Where a participant's question genuinely concerns the desert's own formation logic, this
    story is the signal to redirect rather than to answer as if from inside it.
confidence_line: Widely Accepted (the collection's genuine place within the wider tradition) / Dominant
  Modern Reconstruction (individual attributions are Contested)
---
Migrated at the S6.2 S2.4-equivalent (2026-07-27) from `data/alexandria_world/story_chunks/alexstory004_apophthegmata.md` (mapping in `wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage Guidance verbatim; occasion/owner/frame authored per Desert S2.4 conventions).

S2.5-equivalent (2026-07-27): the parked Formation Ecology Connection converted to typed gravity_links[] (CO-P2-04 - FEC verbatim on the first link's note); see wrs/migrate/s62_alx_s25.py.

CO-P2-16 (2026-07-28): confidence_line backfilled verbatim from the deployed chunk's Confidence front-matter line (live retrieval-context metadata); see wrs/migrate/s62_alx_s29_co16.py.
