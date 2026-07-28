---
id: alexstory002
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
title: Palladius Meets Didymus
narrative_tier:
  tier: 1
  justification: 'Direct first-person testimony: the author records his own repeated visits over a decade,
    not a report of someone else''s encounter. Palladius elsewhere in the same work relays received desert
    traditions at one or more removes (those passages are Tier 3); this passage is explicitly his own
    meeting, which the tier criteria distinguish as Tier 1 even within a single author''s larger work.
    The account is internally consistent with the independently attested fact of Didymus''s blindness
    and his standing as a teacher in Alexandria in this period.'
text: A visitor to Alexandria, later in this world's life, tells us of going to see the blind teacher
  four times over ten years, seeking him out the way one seeks out someone whose sight has gone but whose
  seeing has not. He tells us Didymus had lost his eyes as a small child, before he had learned even his
  letters, and so had never read a word with his own eyes in his whole life — and that this had not closed
  a single door his formation needed open. The visitor tells us Didymus explained it himself, likening
  his blindness to the blindness of the mice and ants and other small creatures who have no eyes at all
  and yet find what they need; if such creatures may still possess what they need without sight, he reasoned,
  why should he grieve for the loss of eyes that are shared even by gnats and flies, when he possessed
  instead the eyes that the saints see God with — eyes by which the deep things of God are perceived?
  He heard the man discourse from memory on Scripture with the same command another might bring to a scroll
  open on the table before him.
attested_occasion: Palladius's personal visits to the blind teacher Didymus in Alexandria, recounted in
  the Lausiac History (c. 419-420) as direct testimony.
tellable_as: scene
owner_figure_id: alexfig005
voice_surface: 'Palladius tells us himself of visiting the blind teacher - we tell it as his own witnessed
  account, not ours. Usage guidance (chunk, verbatim): May be offered as remembered history, with Palladius
  named as the visitor and firsthand witness. This story belongs to the late horizon (Didymus''s active
  teaching years run into the 380s–390s CE) — it should not be used to characterize the school tradition''s
  earlier, mid-horizon peak, where the evidentiary base is different (Origen-concentrated rather than
  Didymus-concentrated). The story is silent on Didymus''s specific theological positions in their later,
  contested reception; it attests only the encounter and the capacity it demonstrates.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks about Didymus, the blind master of the late-horizon teaching tradition
  - participant asks whether formation can proceed without the eyes to read
  - conversation reaches the school tradition's own late (post-Nicene) horizon.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant asks about Palladius's other, received (non-firsthand) desert accounts — those are
      Tier 3 material and carry a different evidentiary weight
  - condition_type: sense-disambiguation
    text: participant wants a systematic account of Didymus's own teaching (this story attests the encounter,
      not a summary of his doctrine).
  force_llm_vote: false
sources:
- source_id: srcALX010
  locus: Palladius, Lausiac History (c. 419–420 CE), his own firsthand account of meeting Didymus the
    Blind
---
Migrated at the S6.2 S2.4-equivalent (2026-07-27) from `data/alexandria_world/story_chunks/alexstory002_palladius-meets-didymus.md` (mapping in `wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage Guidance verbatim; occasion/owner/frame authored per Desert S2.4 conventions).

[Formation Ecology Connection — parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] Illustrates C1 (Scripture as Deep Formative Reality) at its sharpest edge: the deep reading this world prizes is shown here to be a capacity of the soul, not merely a skill of the eyes — the text's depths are perceived, not decoded. It equally illustrates the accompaniment mode of formation (Doc_05 §5) continuing across the whole span into the late horizon, and C5's own documented late-horizon attenuation (Doc_04 §3.5; the C5↔T2 interaction, §6): the story attests that even at the school tradition's late edge, when C5's living force was documented to be attenuating, the teacher-student encounter it names remained sought out and real.
