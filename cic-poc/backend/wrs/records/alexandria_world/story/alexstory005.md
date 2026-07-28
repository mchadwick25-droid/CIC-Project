---
id: alexstory005
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
title: The Life of Antony
narrative_tier:
  tier: 3
  justification: A hagiographic account shaped by recognizable and identifiable genre conventions (the
    call narrative, the escalating temptation sequence, the exemplary triumph over adversity) — genuinely
    attested as a work of this world's own bishop, datable and historically situated, but not a work of
    historical reporting in its specific episodes. The *portrait* it communicates — that ascetic withdrawal,
    taken seriously, produces a formed and stable soul — is credible evidence of what this world's own
    leadership believed formation could produce, which grounds a Contested-but-real tier-3 claim about
    the portrait. The *specific events* (named visions, demonic combat, particular miracles) are not historical
    reporting and are held at Inferential-Thin. Antony's own literacy is itself a live scholarly question
    (some readings take the text's "unlettered" framing as rhetorical humility rather than fact) and is
    not resolved here in either direction.
text: The bishop of this city, some generations into its life, wrote of a man who had heard the Gospel's
  call to sell all he had and give it to the poor, and who took the words as addressed to him personally
  rather than as a saying to be admired from a comfortable distance. He gave away his possessions, placed
  his sister in the care of known and trusted virgins, and went out to live the ascetic life at the edge
  of habitation and then beyond it, deeper into the desert than any had gone in settled practice before
  him. The account tells of years spent in a tomb and then an abandoned fort, of temptations that came
  to him in the shape of visions and assaults, of demons met and withstood, and of a man who emerged from
  long solitude with his body and mind unbroken, in fact strengthened, so that those who saw him marveled
  at a soul so plainly whole. The bishop who wrote this account held Antony up not as a curiosity but
  as a model — proof that this world's own conviction, that the soul truly can be transformed all the
  way through, was not confined to the reading-room and the school but could be lived to its furthest
  edge.
attested_occasion: Athanasius's Life of Antony (c. 356-362), composed within living memory - the formation
  ideal credible, specific episodes hagiographic; cross-build constraint applies (Doc_01 §3.3).
tellable_as: scene
owner_figure_id: alexfig010
voice_surface: 'Athanasius wrote Antony''s life within living memory - we tell it as his portrait, with
  the desert''s own claim on this story held open beside ours. Usage guidance (chunk, verbatim): May be
  offered as this world''s own account of what a formed ascetic life looks like — never as historical
  fact about the specific visions or miracles narrated, which are the genre''s conventions doing their
  expected work, not eyewitness reporting. The desert-formation substance this life exemplifies is held
  open cross-build (Doc_01 §3.3): this world may honor Antony and tell of him, as its own bishop did,
  without claiming his developed ascetic discipline as its own formation logic — that belongs, in its
  fuller and more technical form, to the Desert Christianity world. Antony''s literacy should not be asserted
  as either securely literate or securely unlettered; the question is live and unresolved.'
retrieval:
  tier: 3
  retrieve_when:
  - participant asks what a formed ascetic life looks like, by this world's own account of it
  - participant asks about Antony specifically, as a figure this world's own bishop wrote of and held
    up.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant wants the specific visions, temptations, or miracles narrated as verified historical
      events — these are the genre's own conventions, not historical reporting
  - condition_type: sense-disambiguation
    text: participant is asking for the desert's own developed formation logic as this world's own (cross-build
      HELD OPEN, Doc_01 §3.3)
  - condition_type: sense-disambiguation
    text: participant presses on Antony's literacy as a settled fact — it is itself Contested (Rubenson's
      literate-Antony thesis) and should not be asserted either way as secure.
  force_llm_vote: false
sources:
- source_id: srcALX004
  locus: Athanasius, Life of Antony (c. 356–362 CE)
- source_id: srcALX003
  locus: Athanasius, Life of Antony (c. 356–362 CE)
---
Migrated at the S6.2 S2.4-equivalent (2026-07-27) from `data/alexandria_world/story_chunks/alexstory005_life-of-antony.md` (mapping in `wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage Guidance verbatim; occasion/owner/frame authored per Desert S2.4 conventions).

[Formation Ecology Connection — parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] Illustrates C2 (Transformation of the Soul Toward God) at its most extreme instantiation — a soul held up as evidence that the ascent this world teaches is not merely theoretical. It is also this world's clearest attestation of T4 (Martyrdom vs. Contemplative-Ascent) from the contemplative pole: Antony's whole life is offered as a different but equally formed answer to the question of what a completed Christian life looks like, alongside the martyr's answer (see alexstory009). The account is written by this world's own bishop, which grounds its inclusion here even though its formation-logic content belongs, in its developed form, to the distinct desert ecology.
