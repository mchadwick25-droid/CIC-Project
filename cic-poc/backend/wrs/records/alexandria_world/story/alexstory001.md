---
id: alexstory001
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
title: Gregory's Address to Origen
narrative_tier:
  tier: 1
  justification: 'Direct first-person textual attestation: the account is the student''s own composed
    oration, addressed to Origen himself, not a later report about the relationship. The author is named
    and his social location is identifiable (a young man of rank drawn from a legal-training track into
    the school). It is datable to the mid-230s CE, within a generation of the events it describes. The
    genre — an epideictic address of thanksgiving — idealizes its subject, as the genre requires, but
    idealization is not the same defect as invention: the account does not fabricate events, it praises
    real ones in elevated language. This meets Tier 1''s core test (direct textual attestation, named
    author, identifiable social location, historically credible) more fully than any other story in this
    inventory.'
text: 'There is a student''s own account, kept among us, of what it was to sit under this teacher. He
  tells us he did not come to Caesarea already resolved to stay — he had meant to press on toward Beirut,
  to study law, and go home. But the teacher took hold of him the way a skilled physician takes hold of
  a sick man who does not yet know he is sick: not by lecturing him toward a conclusion, but by asking
  the kind of questions that will not let a mind rest where it was resting. He tells us the teacher praised
  philosophy and urged every kind of learning on him, holding nothing in reserve as too dangerous to study
  — geometry, astronomy, the whole range of Greek thought — and that this immersion was not an end in
  itself but a clearing of the ground, so that Scripture, read last and read hardest, could be received
  rightly once the soul had first been trained to think. He tells us of the friendship that grew in the
  years of this study: not a master issuing verdicts from above, but a guide walking a road himself, further
  up it than his student, letting the student see what he saw by staying near enough to see it too. And
  when the years of study closed and the parting came, he tells us it grieved him the way a soul grieves
  losing its own sun.'
attested_occasion: Gregory's formal address of thanksgiving at the close of his years of study under Origen
  at Caesarea, c. 238 CE (Address of Thanksgiving; Nautin dating caveat carried).
tellable_as: scene
owner_figure_id: alexfig004
voice_surface: 'We keep a student''s own account of what it was to sit under this teacher - we tell it
  with his name on it, as his own composed thanks, in the elevated register the occasion asked of him.
  Usage guidance (chunk, verbatim): May be offered as remembered history — the author and his relationship
  to Origen (a former student, composing thanks near the end of his own years of study) should be named
  where it matters to the claim being made. The address''s own rhetorical elevation is real and should
  be carried lightly: this is a young man praising the teacher who changed his life, in the conventions
  of a formal oration, and its warmth is genuine even where its language is heightened. This story says
  nothing about Origen''s later-condemned doctrines and should not be extended to cover them — the horizon
  here is the relationship, not the theology that would later become contested.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks what studying under Origen — or under a teacher of this tradition generally — was
    actually like
  - participant asks how the teacher-student relationship formed a soul
  - conversation reaches the accompaniment mode of formation (a teacher drawing a student into perceiving
    what the teacher perceives).
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about Origen's later-condemned doctrines or his post-horizon reputation
      (retrieve alexlex020/alexlex051 territory instead, held at the lexicon layer)
  - condition_type: sense-disambiguation
    text: participant wants a settled account of the school as an institution (retrieve alexstory007,
      and note its own institutional-form caution).
  force_llm_vote: false
sources:
- source_id: srcALX007
  locus: Gregory Thaumaturgus, Address of Thanksgiving to Origen (c. 238 CE; Nautin's authenticity/dating
    caveat noted)
- source_id: srcALX002
  locus: Gregory Thaumaturgus, Address of Thanksgiving to Origen (c. 238 CE; Nautin's authenticity/dating
    caveat noted)
gravity_links:
- gravity_id: alexgrav005
  note: 'This is the paradigm case of C5 (Learning-Formation Integration — the conviction that to know
    truly is to be changed) rendered as a lived relationship rather than a claim: the student names the
    teaching itself as what altered him, not information added to an unchanged mind. It equally illustrates
    C1 (Scripture as Deep Formative Reality) in its structural claim that philosophical training clears
    the ground and Scripture is read last, at the deepest register, once the soul is prepared to receive
    it — and C2 (Transformation of the Soul Toward God), since the account''s whole shape is conversion,
    not instruction. It is the ecology''s clearest attestation of the accompaniment mode of formation
    (Doc_05 §5; Doc_07 §1E) — the teacher as a fellow-traveller further up the same road, not a dispenser
    of content.'
- gravity_id: alexgrav001
  note: Named in this story's Formation Ecology Connection - full text on the first gravity_links note
    (CO-P2-04).
- gravity_id: alexgrav002
  note: Named in this story's Formation Ecology Connection - full text on the first gravity_links note
    (CO-P2-04).
confidence_line: Documented / Widely Accepted (narrative level)
---
Migrated at the S6.2 S2.4-equivalent (2026-07-27) from `data/alexandria_world/story_chunks/alexstory001_gregory-address-origen.md` (mapping in `wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage Guidance verbatim; occasion/owner/frame authored per Desert S2.4 conventions).

S2.5-equivalent (2026-07-27): the parked Formation Ecology Connection converted to typed gravity_links[] (CO-P2-04 - FEC verbatim on the first link's note); see wrs/migrate/s62_alx_s25.py.

CO-P2-16 (2026-07-28): confidence_line backfilled verbatim from the deployed chunk's Confidence front-matter line (live retrieval-context metadata); see wrs/migrate/s62_alx_s29_co16.py.
