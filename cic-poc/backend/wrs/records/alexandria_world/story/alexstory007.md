---
id: alexstory007
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
title: The Catechetical-School Succession
narrative_tier:
  tier: 3
  justification: 'An attributed institutional tradition, transmitted through a single mediating source
    (Eusebius, early fourth century) reconstructing the school''s history from earlier and largely lost
    materials — HIGH Author-Gravity risk, since no independent contemporary source corroborates the specific
    succession as narrated. The succession''s *institutional form itself* is genuinely and actively Contested
    in the scholarship: some scholars (van den Broek, van den Hoek) argue no formal institution with continuous
    headship existed before Origen''s own mature period, and that Eusebius''s orderly succession retrospectively
    schematizes what was actually a looser, informal teaching milieu; others (Scholten) hold that an institution
    did exist but was a different kind of school than "catechetical" implies. This story cannot be assigned
    a higher tier than Contested precisely because its central institutional claim — an orderly, continuous
    school with named heads — is what the scholarship disputes most directly.'
text: 'The tradition kept of this world''s teaching life names a line: Pantaenus, said to have come first,
  a former Stoic philosopher turned catechist; then Clement, who studied under him and took up the teaching
  after; then Origen, still a young man when he began, whose reputation as a teacher would come to eclipse
  every name before or after his; then Heraclas, once Origen''s own student, who succeeded him; then Dionysius,
  who followed Heraclas and would go on to become bishop of the city. Told this way, it reads as an orderly
  handing-on, one teacher to the next, an institution with a memory of its own headship reaching back
  to the earliest Christian teaching in this city. This is how the tradition remembers itself, and it
  is worth telling for what it says about how much this world valued its own teaching lineage — that it
  kept the names at all, in order, across generations, says something true about what this community thought
  mattered.'
attested_occasion: The teacher-succession (Pantaenus - Clement - Origen - Heraclas - Dionysius - Didymus)
  as Eusebius scaffolds it - carrying the Didaskaleion historical-scope contest and Eusebius's HIGH institutional-claims
  screen (Doc_01 §1.2; srcALX009).
tellable_as: background-fact
owner_figure_id: alexfig011
voice_surface: 'We name our teachers in the order handed down - and we say plainly that the order''s tidiness
  is its transmitter''s, and that whether the school was an institution or a tradition is genuinely disputed.
  Usage guidance (chunk, verbatim): The succession of names may be told as the tradition''s own account
  of its teaching lineage — it is worth telling for what it reveals about this community''s own sense
  of its teaching continuity. It must not be told as a settled orderly institution with confirmed offices:
  the neat succession itself is very likely, in part, a later schematizing of a looser reality, the same
  kind of rhetorical ordering a Representative should recognize and carry lightly (compare the caution
  around named rosters in other worlds'' foundation narratives). Where a participant presses on whether
  this was "a real school," the honest answer is that this is genuinely disputed, and this world''s own
  construction record holds the dispute open rather than resolving it in either direction.'
retrieval:
  tier: 3
  retrieve_when:
  - participant asks about the teaching lineage of this world — who taught whom, across the generations
  - participant asks whether there was a formal school with an ordered succession of heads.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant wants this offered as a settled, orderly institution with confirmed offices and
      continuous headship — the institutional form itself is genuinely Contested (Doc_01 §1.2) and this
      story must not be told as though that question were closed.
  force_llm_vote: false
sources:
- source_id: srcALX009
  locus: Eusebius, Historia Ecclesiastica 5.10–6.30 (Pantaenus → Clement → Origen → Heraclas → Dionysius)
- source_id: srcALX001
  locus: Eusebius, Historia Ecclesiastica 5.10–6.30 (Pantaenus → Clement → Origen → Heraclas → Dionysius)
- source_id: srcALX002
  locus: Eusebius, Historia Ecclesiastica 5.10–6.30 (Pantaenus → Clement → Origen → Heraclas → Dionysius)
gravity_links:
- gravity_id: alexgrav005
  note: 'Illustrates C5 (Learning-Formation Integration) at the level of institutional memory — a community
    that kept a lineage of teachers'' names is a community that believed the handing-on of formation from
    one teacher to the next mattered enough to remember. It also bears directly on T1 (Teacher–Bishop):
    the succession culminates in Dionysius moving from teacher to bishop, which the tradition remembers
    without comment on the tension that move could carry — a detail worth noting rather than smoothing
    over when this story is told alongside alexstory008.'
- gravity_id: alexgrav006
  note: Named in this story's Formation Ecology Connection - full text on the first gravity_links note
    (CO-P2-04).
confidence_line: Contested
---
Migrated at the S6.2 S2.4-equivalent (2026-07-27) from `data/alexandria_world/story_chunks/alexstory007_school-succession.md` (mapping in `wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage Guidance verbatim; occasion/owner/frame authored per Desert S2.4 conventions).

S2.5-equivalent (2026-07-27): the parked Formation Ecology Connection converted to typed gravity_links[] (CO-P2-04 - FEC verbatim on the first link's note); see wrs/migrate/s62_alx_s25.py.

CO-P2-16 (2026-07-28): confidence_line backfilled verbatim from the deployed chunk's Confidence front-matter line (live retrieval-context metadata); see wrs/migrate/s62_alx_s29_co16.py.
