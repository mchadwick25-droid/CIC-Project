---
id: syrstory008
world_id: syriac-edessa-nisibis
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
cache_stability: static
title: The Legend of Ephrem's Meeting with Basil of Caesarea
narrative_tier:
  tier: 3
  justification: 'Modern scholarship (per GEDSH''s own entry on Basil of Caesarea) states plainly that
    this episode "is legendary and is based on a misidentification of an anonymous ''Syrian'' in Basil''s
    writings" — a figure now identified as Eusebius of Emesa, a different person entirely, whom later
    Syriac tradition mistook for Ephrem. This is a stronger and more specific finding than ordinary Tier
    3 uncertainty: rather than merely resting on unverifiable attributed tradition, this legend has been
    traced to an identified historical error. It remains Tier 3 rather than being excluded outright, per
    the Framework''s own logic that a hagiographic tradition''s formation-ideal content (here, the desire
    of a later community to connect its own revered teacher to the wider, Greek-speaking church''s most
    eminent bishop) is itself genuine evidence of that later community''s own concerns, even where the
    specific claimed event is not merely undocumented but actively shown to rest on mistaken identity.'
text: The later Syriac Vita Ephraemi tells that Ephrem, prompted by a vision, journeyed to Caesarea in
  Cappadocia to meet the great bishop Basil, that Basil received him with honor, recognized his sanctity
  though Ephrem spoke no Greek and Basil no Syriac, and that it was Basil himself who ordained Ephrem
  to the diaconate during this visit.
attested_occasion: 'The Syriac Vita Ephraemi''s legend (6th c.): Ephrem''s vision-prompted journey to
  Basil at Caesarea and ordination to the diaconate - positively identified by modern scholarship as resting
  on a documented case of mistaken identity (chunk front matter; Rousseau 1957-58; Muraviev 2015); engaged
  ONLY when a participant raises it, always with the correction attached (the chunk''s own retrieve-when
  rule and srcSYR059''s licensing).'
tellable_as: scene
owner_figure_id: syrfig001
voice_surface: 'If you have heard that our Ephrem met the great Basil, we will tell you what the later
  life-story says - and tell you with it that those who have searched the record find the meeting rests
  on a mistaken name, not a kept memory. We do not offer this story unasked. Usage guidance (chunk, verbatim):
  If a participant raises this legend directly, the Representative may acknowledge it as a story later
  told about Ephrem, without asserting it happened: "Some among us have told of a visit to the great Basil,
  of a wordless recognition between us despite no common tongue — it is a story told with love for both
  men, though I could not tell you it happened as it is told." The Representative should not introduce
  this story unprompted, and should not use it to support any claim about Ephrem''s ordination, since
  this world''s own more securely attested record (Jerome, contemporary with Ephrem) already establishes
  his diaconate independently of this legend.


  **Additional guidance:** This is the one story in this repository where the Representative may, if directly
  asked, acknowledge that the specific claim does not hold up — this is not a breach of the Representative''s
  own in-world awareness (per the Representative Construction Framework''s Total Embeddedness principle),
  since a formed voice within this tradition could plausibly know that a beloved story about its own teacher
  is more legend than fact, the way any community holds some of its own traditions loosely.'
confidence_line: Inferential/Thin — and, unusually for this repository, positively identified by modern
  scholarship as resting on a documented case of mistaken identity, not merely unverified tradition
retrieval:
  tier: 3
  retrieve_when:
  - a participant specifically raises this legend, asks whether Ephrem met Basil of Caesarea, or asks
    about Ephrem's ordination as deacon.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: general questions about Ephrem's life, diaconate, or formation (use syrstory001 or Doc_05/07
      material instead) — this story should not be offered proactively as a likely-true account, only
      engaged directly if a participant raises it, and even then only with its correction attached.
  force_llm_vote: false
sources:
- source_id: srcSYR059
  locus: The Syriac Vita Ephraemi (6th c.); discussed in GEDSH, "Basil of Caesarea" entry; O. Rousseau,
    "La rencontre de S. Ephrem et de S. Basile," L'Orient Syrien 2-3 (1957-58); Alexei Muraviev, "Early
    Syriac Version of the Encounter of Basil of Caesarea and Ephrem the Syrian," Vestnik Drevney Istorii
    4 (2015)
- source_id: srcSYR051
  locus: The Syriac Vita Ephraemi (6th c.); discussed in GEDSH, "Basil of Caesarea" entry; O. Rousseau,
    "La rencontre de S. Ephrem et de S. Basile," L'Orient Syrien 2-3 (1957-58); Alexei Muraviev, "Early
    Syriac Version of the Encounter of Basil of Caesarea and Ephrem the Syrian," Vestnik Drevney Istorii
    4 (2015)
- source_id: srcSYR060
  locus: The Syriac Vita Ephraemi (6th c.); discussed in GEDSH, "Basil of Caesarea" entry; O. Rousseau,
    "La rencontre de S. Ephrem et de S. Basile," L'Orient Syrien 2-3 (1957-58); Alexei Muraviev, "Early
    Syriac Version of the Encounter of Basil of Caesarea and Ephrem the Syrian," Vestnik Drevney Istorii
    4 (2015)
- source_id: srcSYR061
  locus: The Syriac Vita Ephraemi (6th c.); discussed in GEDSH, "Basil of Caesarea" entry; O. Rousseau,
    "La rencontre de S. Ephrem et de S. Basile," L'Orient Syrien 2-3 (1957-58); Alexei Muraviev, "Early
    Syriac Version of the Encounter of Basil of Caesarea and Ephrem the Syrian," Vestnik Drevney Istorii
    4 (2015)
chunk_slug: ephrem-basil-legend
---
Migrated at the S6.2/SYR S2.4-equivalent (2026-07-28) from `data/syriac_world/story_chunks/syrstory008_ephrem-basil-legend.md` (mapping in `wrs/migrate/s62_syr_s24.py`; Story Text / Tier Justification / Usage Guidance / Confidence line verbatim; occasion/owner/frame authored per Desert-ALX S2.4 conventions).

[Formation Ecology Connection - parked at the S2.4-equivalent; becomes typed gravity_links (CO-P2-04 shape) when the S2.5-equivalent authors the gravity records] This story does not belong to this world's own attested formation ecology as a plausible historical event, and is included here specifically as a documented case of legendary conflation rather than as evidence of anything this world's own formation logic produced. It is retained in this repository — rather than simply omitted — because it is a well-known and often-repeated piece of later tradition about this world's central figure, and because this project's own discipline requires naming what should not be told as fact just as carefully as it documents what may be.
