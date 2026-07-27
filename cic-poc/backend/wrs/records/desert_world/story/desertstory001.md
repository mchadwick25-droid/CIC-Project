---
id: desertstory001
world_id: desert-monasticism
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
cache_stability: static
title: Antony's Call — Hearing Matthew 19:21
narrative_tier:
  tier: 1
  justification: 'Named author (Athanasius), specific text and chapter reference, composed within a generation
    of Antony''s death — well inside this world''s own attested horizon. Confidence is calibrated at two
    levels, matching Doc_09a''s own treatment: Widely Accepted as to the narrative''s existence and general
    content within the Vita; Contested as to incident-level historical reliability specifically, per Doc_01
    §10''s carried-forward Rubenson/Athanasius tension over Antony''s own philosophical literacy and Doc_08
    Force 1B-ii''s own confidence label. This is a Tier 1 story, not a Tier 3 one, because its narrative
    register is a restrained incident report, not a hagiographic portrait — contrast Story 007 (Antony''s
    Combat in the Tombs), drawn from the same Vita but carrying clear hagiographic genre markers this
    story does not.'
text: 'In his Life of Antony, Athanasius records that Antony, not yet twenty years old and recently orphaned,
  entered church one day not long after reflecting on how the apostles left everything to follow Christ.
  He heard the Gospel being read: "If you would be perfect, go, sell what you possess and give to the
  poor, and you will have treasure in heaven; and come, follow me." Athanasius tells us that Antony took
  the words as spoken directly to him — not as instruction offered generally to any hearer, but as an
  address meant for him in that hour. He left the church, and gave away the land and possessions he had
  inherited, keeping back only enough to provide for his sister.'
attested_occasion: Hearing Matthew 19:21 read in church, not yet twenty and recently orphaned (Vita Antonii
  ch. 2).
tellable_as: scene
voice_surface: 'Athanasius records that Antony heard the word as spoken to him in that hour - we tell
  it with his name on it, as remembered history, not as our own eyewitness. Usage guidance (chunk, verbatim):
  The Representative may tell this as remembered history, with Athanasius named as the source — "Athanasius
  records that..." The Representative should not claim more certainty about Antony''s specific interior
  experience than the source supports, and should be prepared to note, if a participant presses further,
  that Antony''s own literacy and philosophical formation are independently and genuinely contested among
  scholars (Doc_06 §2.2''s [CT] tag) — this story''s own confidence does not extend to settling that separate
  question.


  **Additional guidance:** This is the single clearest concrete instance of this world''s own scriptural-address
  pattern, and the natural first story to reach for when a participant asks, in any form, "what actually
  started this."'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks what first drew someone to this way of life, or how withdrawal actually began for
    anyone
  - participant asks how scripture is heard or applied in this world
  - conversation reaches the founding moment or origin story of desert monasticism specifically
  - Representative needs a formation example for gravity 1 (withdrawal) or gravity 7 (practical scriptural
    engagement).
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about Antony's later career, his combat in the tombs (see Story 007 instead),
      or his staged withdrawal itself (see Story 002)
  - condition_type: sense-disambiguation
    text: conversation concerns the cenobitic/Strand B founding instead (see Story 003)
  - condition_type: sense-disambiguation
    text: participant is asking about Antony's own literacy or philosophical formation as a scholarly
      question — that is a separate, unresolved dispute this story does not settle.
  force_llm_vote: false
sources:
- source_id: srcDES001
  author_gravity_note: Widely Accepted (that the narrative exists and reports Antony's founding call);
    Contested (incident-level historical reliability, per the Rubenson/Athanasius literacy tension)
- source_id: srcDES020
  author_gravity_note: 'Source line (chunk): Athanasius, Life of Antony, ch. 2 (composed c. 356-362)'
owner_figure_id: desertfig001
gravity_links:
- gravity_id: desertgrav001
  note: This story directly generates gravity 1 (withdrawal) and gravity 7 (practical, personally-addressed
    scriptural engagement, Doc_08 Force 1B-ii). It is this world's own founding narrative for the specific
    interpretive posture Doc_05 §8.1-8.2 identifies as characteristic of the whole tradition — scripture
    heard as immediate personal command, not general instruction offered to any reader. It is also the
    direct source for Papnoute's own Christ-Ward Telos derivation (Doc_10 §5), which grounds the stripping-away
    of withdrawal in exactly this pattern of staying reachable by an address once heard.
- gravity_id: desertgrav007
  note: Named in this story's Formation Ecology Connection - full text on the first gravity_links note
    (CO-P2-04).
---
Migrated at S2.4 (2026-07-27) from `data/desert_world/story_chunks/desertstory001_antonys-call-matthew-19-21.md` (Story Text / Tier Justification / Usage Guidance verbatim from the chunk's own sections; occasion and telling-formula per chunk + Doc_09a). Tier-4 owner gap: see FLAG-003.

CO-P2-04 (2026-07-27): parked FLAG-004 sections restructured into gravity_links[] (FEC verbatim on the first link) and, for this record's tier-4 table, per-element sources[] entries.
