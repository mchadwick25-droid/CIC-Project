---
id: alexstory003
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
title: Persecution Shapes the School — Leonidas and Origen Under Decius
narrative_tier:
  tier: 1
  justification: 'The persecutions themselves — the Severan-era pressure on Alexandrian Christians and
    the Decian persecution of 249–251 — are documented events, independently attested beyond this single
    source (including the empire-wide *libelli* record). This story rests on Eusebius in two distinct
    modes that must be told apart: Origen''s own Decian imprisonment is corroborated by Dionysius of Alexandria''s
    own contemporary correspondence on the Decian persecution, quoted (not narrated) by Eusebius — doubly-mediated,
    but resting on a near-contemporary primary voice rather than Eusebius''s own construction, which is
    why it earns Widely Accepted. The Leonidas martyrdom and the specific detail of the hidden clothes
    rest on Eusebius''s own institutional narration alone, with no such quoted corroboration, and carry
    HIGH Author-Gravity risk — the event of a father''s martyrdom under this persecution is plausible
    and broadly credible, but the narrated particulars (the boy''s intention, the mother''s specific act)
    lean Contested rather than Documented. This event-versus-particulars split is stated explicitly, as
    required, and this is a split-confidence composite story by design (Doc_09 §1).'
text: 'The teacher''s own father was taken and killed for the faith. This happened when the teacher was
  still a young man, early in this world''s life, in a persecution under an emperor determined to make
  an example of the city''s Christians. We are told the son, still a boy, wished to follow his father to
  the same death. He was kept from it only because his mother, having no other way to hold him back, hid
  his clothes so he could not leave the house. The household''s property was seized with the father''s
  death, and the family was left in want. Decades later, a fiercer persecution reached the city again
  under another emperor. It fell on the teacher himself, now old and renowned. He was bound, put to torture
  designed to break rather than kill him outright, and held for a long imprisonment. We are told he endured
  it without yielding what his tormentors wanted from him. He did not die in that imprisonment. But what
  it did to his body, he carried for the rest of his life, which by then was not long.'
attested_occasion: The recurring persecution episodes (Severan c. 202, Decian 249-251, Diocletianic 303-311)
  as they bore on the school's life - a pattern across the horizon, not one event.
tellable_as: background-fact
owner_figure_id: alexfig011
voice_surface: 'We tell this as the pattern our own record attests across generations - named episodes,
  not one man''s remembered day. Usage guidance (chunk, verbatim): The persecutions and Origen''s own
  suffering under Decius may be offered with confidence as documented history. The Leonidas episode''s
  specific narrated details (the boy''s wish to join his father, the hidden clothes) should be carried
  as the tradition''s own remembered account, mediated through Eusebius, rather than asserted as secured
  historical particulars — the pattern is credible; the scene''s precise details are less secure than
  the fact of the martyrdom itself. This story does not narrate what the experience felt like from inside;
  it establishes only that persecution reached this world''s own teachers and households as a real, costly
  event, not a distant fact.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how persecution actually pressed on the teaching life of this world, not as an abstract
    threat but as something that happened to specific people
  - participant asks about T4 (martyrdom held alongside the contemplative ascent) with a concrete anchor.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant wants the Coptic martyrological tradition's own memory of the later Great Persecution
      (retrieve alexstory009 instead — a different persecution, a different evidentiary register)
  - condition_type: sense-disambiguation
    text: participant is pressing for narrated interior experience of the martyrdom (that remains Inferential-Thin
      and is not supplied).
  force_llm_vote: false
sources:
- source_id: srcALX009
  locus: Eusebius, Historia Ecclesiastica 6, and the broader documented record of the Severan and Decian
    persecutions
gravity_links:
- gravity_id: alexgrav009
  note: 'The clearest concrete anchor for the tension between martyrdom and contemplative ascent, showing that
    tension is not abstract: the same teacher whose contemplative, scholarly formation this world treasures
    also endured what martyrdom actually cost, in his own body and his own household. It also shows the
    divine pedagogy at its hardest edge - the conviction that even suffering teaches is not asserted here as
    doctrine but shown pressing on an actual life - and connects to the ongoing pressure of persecution,
    which this world experienced as formation''s sharpest and most concrete pressure.'
- gravity_id: alexgrav003
  note: Named in this story's Formation Ecology Connection - full text on the first gravity_links note
    (CO-P2-04).
confidence_line: Documented (the persecutions as events) / Widely Accepted (Origen's Decian imprisonment
  specifically) / Contested-leaning (the Leonidas particulars, Eusebius-mediated)
chunk_slug: persecution-shapes-school
---
Migrated at the S6.2 S2.4-equivalent (2026-07-27) from `data/alexandria_world/story_chunks/alexstory003_persecution-shapes-school.md` (mapping in `wrs/migrate/s62_alx_s24.py`; Story Text / Tier Justification / Usage Guidance verbatim; occasion/owner/frame authored per Desert S2.4 conventions).

S2.5-equivalent (2026-07-27): the parked Formation Ecology Connection converted to typed gravity_links[] (CO-P2-04 - FEC verbatim on the first link's note); see wrs/migrate/s62_alx_s25.py.

CO-P2-16 (2026-07-28): confidence_line backfilled verbatim from the deployed chunk's Confidence front-matter line (live retrieval-context metadata); see wrs/migrate/s62_alx_s29_co16.py.

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text field at
FK grade 14.6 / FRE 55.1 - five sentences, several stacking a "when ... in a" or "and ... having ... hid"
chain onto an already long main clause, and one sentence running a colon into a three-part "bound, put to
torture ... and held" list ending in an em-dash aside. Per Mark's decision to extend the readability pass
to story records, each sentence is split at its own existing comma, colon, em-dash, or conjunction
boundary. No fact, hedge, or attribution is dropped - Leonidas's martyrdom, the "we are told" framing on
both the boy's wish to follow him and the hidden clothes, the household's seized property, Origen's later
Decian imprisonment and torture "designed to break rather than kill," and the closing note that he did not
die but carried the damage the rest of his shortened life are all unchanged. Re-scored: FK 6.9 / FRE 75.4,
clearing both thresholds.
