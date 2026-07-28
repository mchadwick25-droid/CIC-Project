---
id: alexlex014
world_id: alexandria-catechetical
record_type: term
schema_version: 1
jobs:
- 1
- 2
- 4
- 6
register: emic
review_state: draft
cache_stability: static
term: Scripture
aliases:
- the Scriptures
- the text
- the written Word
- holy Scripture
- the sacred writings
quick_meaning: For this world Scripture is not a historical document that records what God once said —
  it is the living address of the Logos speaking now, through the text, to the soul that has been formed
  to hear; a text with genuine depths that formation opens and every honest encounter deepens.
world_meaning: 'The reading Scripture asks for here is not study but encounter. Study approaches the text
  as words from the past, to be understood by recovering their circumstances and applying interpretive
  skill; it produces information, and it stops there. That is not what this world means by reading. To
  read Scripture is to come before one who is genuinely present and genuinely speaking: the Logos who
  first inspired the text is the same Logos who speaks through it when the reader has been formed to hear.
  The text is not the record of the Logos having spoken; it is the Logos speaking.


  This is why Scripture is held to contain real depths. The surface sense is genuine and not to be despised
  — it is the ground the deeper reading stands on — but the surface is not the whole, and the reader who
  stops there has not yet met what was placed in the words for them. The depths were not invented by a
  clever interpreter; they were put there by the Logos, and the formed perception (the illumined nous)
  begins to see them. The interpreter''s task is not to impose a meaning but to help the reader perceive
  what is already there.


  And Scripture reaches the community through more than one channel, all of them the same Word speaking:
  the school-tradition''s patient depth-reading; the homily heard in the assembly; the Psalms prayed until
  they become the soul''s own words; the annual walk through the Paschal cycle. These are not equivalent,
  and the ecology needs all of them — the depth-reading is not available to everyone, but the Logos speaking
  through the heard Scripture and the prayed Psalm reaches those the school cannot. What unites them is
  that in each, something is being said, now, by someone who is present.'
distortion_risk: '**World Hearing:**

  The Logos speaking *now*, held in a *formative* relationship: the text forms the reader through the
  encounter itself. The task is not correct interpretation but genuine encounter — and the depths are
  really there to be perceived, not projected.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how this world reads the Bible, or about allegory / multiple senses / "reading for
    depth"
  - participant treats Scripture as a historical document or a rulebook
  - conversation reaches interpretation, the Old Testament read christologically, or why the same text
    yields more to some readers than others.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the participant is asking a narrow textual-criticism question with no bearing on the world's
      formative reading
  - condition_type: sense-disambiguation
    text: the World Capsule Core has already surfaced Scripture-as-address in the current turn.
  force_llm_vote: false
sources:
- source_id: srcALX001
  author_gravity_note: John 1:1–18. Clement of Alexandria, *Stromateis* I and V (multilevel meaning —
    attested independently of Origen).
- source_id: srcALX002
  author_gravity_note: 'Origen, *On First Principles* IV (the levels of Scripture and the "stumbling blocks"
    placed to drive the reader deeper) and the Homilies. Athanasius, *Letter to Marcellinus* and the *Festal
    Letters* (Scripture forming the whole Egyptian church, beyond the school).


    Note: Origen dominates the surviving *systematic* account (the three-level taxonomy and the stumbling-blocks
    argument) — Dominant Modern Reconstruction for any ecology-wide method claim; the underlying conviction
    that Scripture has formative depth is broadly Alexandrian (Clement attests allegory independently),
    so the core is Widely Accepted (Doc_04 C1, two-level result).'
modern_hearing: '**Modern Hearing:**

  Either a set of fixed divine propositions to be believed, or a collection of ancient human documents
  to be analyzed — both of which make Scripture a text *from the past* held in a *cognitive* relationship.'
period_sense: Not a historical document recording what God once said - the living address of the Logos
  speaking now, through the text, to the soul formed to hear; read as encounter, held in a formative relationship
  (chunk Quick/World Meaning).
prior_sense: 'none-attested as a lexical prior: the entry''s frame is the world''s reading practice, not
  a pre-world career of the word - the practice''s own inheritance (allegorical reading of Scripture as
  philosophy) is the Philonic grammar (Doc_02 SS3.5).'
modern_sense: Either fixed divine propositions to believe, or ancient human documents to analyze - both
  making Scripture a text FROM the past (chunk Modern Hearing).
conceptual_distance_note: 'Both modern readings freeze the text in the past; the world read a present
  address - the task is not correct interpretation but formed hearing (chunk World Hearing). Sharp gap
  in tense: high grounding criterion by rule.'
semantic_domain: scripture-reading
grounding_criterion: high
voice_surface: The reading Scripture asks for here is not study but encounter. Study produces information
  and stops. To read Scripture is to come before one who is genuinely speaking - now, to you.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-27'
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
field_relations:
- type: presupposes
  target_id: alexlex001
  note: 'Scripture forms because the Logos speaks in it (chunk EF: the primary vehicle of the first Primary
    gravity). Chunk Ecological Function (verbatim, absorbed per FLAG-002): Scripture is the primary vehicle
    of the first Primary gravity (Scripture as Deep Formative Reality, Doc_04 C1): nearly every other
    practice takes Scripture as its content or is organized around hearing it. A participant who understands
    Scripture-as-address understands the whole interpretive tradition (the reader is helped to perceive,
    not taught to decode), the formation sequence (the text forms the one who encounters it), the liturgical
    ecology (worship is where Scripture is heard by all), and the Rule of Faith (the boundary within which
    the reading stays faithful).'
- type: presupposed-by
  target_id: alexlex015
  note: Christological Reading is the orientation that makes Scripture-as-address operable (alexlex015
    EF).
- type: presupposed-by
  target_id: alexlex016
  note: The method reaches Scripture's own depths (alexlex016 EF).
- type: presupposed-by
  target_id: alexlex035
  note: Interpretation is the discipline exercised on the address (alexlex035 QM).
- type: associated-with
  target_id: alexlex031
  note: 'CO-P2-13 (Mark, 2026-07-28): the chunks'' own mutual Related-Terms cross-reference, typed as
    symmetric association - no hierarchy claimed (both sides'' Reciprocity Notes, verbatim in the record
    bodies, attest the pair).'
contested_claim_ids:
- alexclaim001
---
Migrated at the S6.2 S2.2-equivalent (2026-07-27) from `data/alexandria_world/lexicon_chunks/alexlex014_scripture.md` (mechanical split; mapping in `wrs/migrate/s62_alx_chunk_split.py`). Related-Terms and new-authoring fields arrive at the S2.3-equivalent.

[Related-Terms Reciprocity Note — parked at the S2.2-equivalent; absorbed into field_relations notes at the S2.3-equivalent] Cross-referenced with Logos, Divine Pedagogy, Illumination, Nous, Christological Reading, Allegory, Rule of Faith. **Mutual** (each lists this term back): Logos, Christological Reading, Allegory, Rule of Faith. **One-directional** (this term lists them; they do not list it back yet — deployment-layer reciprocity-completion items, per Doc_06 §4 flag-don't-hide): Divine Pedagogy, Illumination, Nous. **Not yet built as chunks** (Tier-2 / governed-CT entries): none.

S2.6-equivalent (2026-07-27): contested_claim_ids populated at claim-authoring time (the FLAG-014 sequencing gap closed for this world); see wrs/migrate/s62_alx_s26.py for the linking rationale.

CO-P2-13 (2026-07-28): the Reciprocity Note's mutual cross-references now carry typed associated-with edges; see wrs/migrate/s62_alx_s29_co13.py.
