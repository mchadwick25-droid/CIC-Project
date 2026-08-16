---
id: alexstory008
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
title: The Origen–Demetrius Conflict
narrative_tier:
  tier: 3
  justification: An attributed conflict-narrative, transmitted through a single mediating source (Eusebius)
    writing decades after the events, with HIGH Author-Gravity risk attached. The *structural fact* —
    that a real conflict occurred between this teacher and his bishop, and that it ended in the teacher's
    departure — is more securely attested than the *particulars* (the exact charges, whether the ordination
    objection was the true cause or a pretext, the fairness of the proceedings). This story earns Contested/Inferential-Thin
    rather than a higher tier precisely because the structural shape is credible while the specific content
    of the dispute is not independently corroborated.
text: 'The teacher whose reading opened more of the Scriptures than almost any other had taught and traveled
  for years with wide respect. [He] was sought out even by bishops in other cities for his learning. But
  in his own city, his relationship with the bishop who governed it came, in time, to a breaking point.
  The bishop convened a council and moved against him. The tradition remembers ordination irregularities
  and doctrinal concerns raised against him, though the precise grounds and their fairness are not preserved
  with confidence. The teacher was condemned by his own bishop and left the city he had taught in for
  decades. He continued his work from Caesarea instead, where he would remain honored and productive for
  the rest of his life. What the tradition preserves clearly is the fact of the rupture and its cost.
  [It shows] a teacher of undisputed learning, driven from the city his whole teaching life had been rooted
  in, by the one authority that could not be out-argued by learning alone.'
attested_occasion: 'Origen''s rupture with bishop Demetrius (c. 231-234): ordination abroad, condemnation
  at Alexandria, departure to Caesarea - via Eusebius (HE VI) with his institutional screen active.'
tellable_as: scene
owner_figure_id: alexfig001
voice_surface: 'We tell the parting of teacher and bishop as our record holds it - through Eusebius''s
  telling, with his order-loving hand named. Usage guidance (chunk, verbatim): Tell the structural fact
  — a real conflict, a real departure, a real cost to both the teacher and the community he left — as
  the paradigmatic instance of the Teacher–Bishop tension. Do not present the specific charges or the
  fairness of the proceedings as settled fact; the tradition itself does not preserve them with that confidence.
  This story should not be resolved into a verdict about who was right — this world''s own construction
  record holds the Teacher–Bishop tension open, not settled, and this story is the concrete case that
  tension is drawn from, not an argument for one side of it.'
retrieval:
  tier: 3
  retrieve_when:
  - participant asks about T1 (the Teacher–Bishop tension) with a concrete, named example
  - participant asks what happened when a teacher's authority and a bishop's authority pulled against
    each other in this world's own life.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant wants the specific charges and proceedings narrated as settled, secure fact — the
      particulars are Eusebius-mediated and thin
  - condition_type: sense-disambiguation
    text: participant wants this resolved into a verdict about who was right — the tension this story
      carries is meant to be held, not settled.
  force_llm_vote: false
sources:
- source_id: srcALX009
  locus: Eusebius, Historia Ecclesiastica 6 (Origen's departure to Caesarea c. 231–234 CE; Demetrius's
    condemnation)
- source_id: srcALX002
  locus: Eusebius, Historia Ecclesiastica 6 (Origen's departure to Caesarea c. 231–234 CE; Demetrius's
    condemnation)
gravity_links:
- gravity_id: alexgrav006
  note: 'This is the best-known illustration of the tension between authority grounded in demonstrated wisdom and
    authority grounded in apostolic office - the two are not the same, and this story shows what happens when
    they cannot be reconciled. It is illustration, not foundation: that tension is confirmed by the broader,
    better-attested pattern of school and episcopate coexisting structurally (Pantaenus and Clement alongside
    the bishops of their day; Didymus alongside Athanasius), not by this single Eusebius-mediated episode. It
    also touches the tension between speculative freedom and doctrinal boundary: whatever the specific
    charges, the underlying pattern - a teacher whose reach exceeded what the settled boundary could
    comfortably hold - sits at the same site as the broader Origen inheritance this world carries as
    treasure-and-unease.'
- gravity_id: alexgrav008
  note: Named in this story's Formation Ecology Connection - full text on the first gravity_links note
    (CO-P2-04).
confidence_line: Contested / Inferential-Thin (particulars)
chunk_slug: origen-demetrius
---
Migrated at the S6.2 S2.4-equivalent (2026-07-27) from `data/alexandria_world/story_chunks/alexstory008_origen-demetrius.md` (mapping in `wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage Guidance verbatim; occasion/owner/frame authored per Desert S2.4 conventions).

S2.5-equivalent (2026-07-27): the parked Formation Ecology Connection converted to typed gravity_links[] (CO-P2-04 - FEC verbatim on the first link's note); see wrs/migrate/s62_alx_s25.py.

CO-P2-16 (2026-07-28): confidence_line backfilled verbatim from the deployed chunk's Confidence front-matter line (live retrieval-context metadata); see wrs/migrate/s62_alx_s29_co16.py.

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text field at
FK grade 15.0 / FRE 46.2 - five sentences, several stacking a comma-joined participial clause or an
em-dash/colon aside onto an already long main clause (the opening sentence alone ran a relative clause
into a "for years, taught and traveled ... sought out" participial tail). Per Mark's decision to extend
the readability pass to story records, each sentence is split at its own existing comma, em-dash, or
colon boundary, with two bracketed supplied words ([He], [It shows]) standing in for clauses that had
no subject of their own. No fact, hedge, or attribution is dropped - the teacher's wide-respected
reputation, the bishop-convened council, the tradition's own hedge that the ordination charges and their
fairness "are not preserved with confidence," the condemnation and departure to Caesarea, and the closing
claim that no amount of learning could out-argue apostolic office are all unchanged. Re-scored: FK 9.3 /
FRE 62.3, clearing both thresholds.
