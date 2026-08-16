---
id: ijcstory001
world_id: imperial-juridical-christianity
record_type: story
schema_version: 1
jobs:
- 1
- 2
- 4
register: emic
review_state: draft
cache_stability: static
title: The Vision and the Alliance (Eusebius's Account)
text: 'In his own account, written after the emperor''s death, Eusebius tells what Constantine himself
  told him. Before the battle at the Milvian Bridge, in the sky above the sun, Constantine saw a
  cross of light, and with it the words *by this, conquer*. That night, Christ himself appeared to him
  in sleep and showed him the same sign. [He] commanded that he make of it a standard to carry before his
  armies. Constantine did as he was shown. The army that carried that standard won the bridge, and
  Rome, and, before long, the whole of the West.


  Eusebius does not offer this lightly. He is careful to say that he had this from the emperor''s own
  mouth, confirmed by oath, long after the event itself. [Eusebius was] a witness once removed, reporting
  what a ruler wished remembered about his own rise. What follows from it, in Eusebius''s own telling, is
  not in doubt. An emperor who had seen this sign no longer persecuted the church that bore it, and within
  a year, toleration was law.'
confidence_line: Documented (the text's existence and content); Contested (what the vision meant to Constantine
  himself)
attested_occasion: Eusebius of Caesarea, Life of Constantine (Vita Constantini), reporting an account
  Eusebius states he heard from Constantine himself, under oath, some years after the event
tellable_as: scene
owner_figure_id: ijcfig002
narrative_tier:
  tier: 1
  justification: 'Tier 1 (Documented Historical Narrative): the text exists, is named to a specific author
    and work, and Eusebius states plainly the chain of testimony (Constantine, under oath, to Eusebius).
    This is not attributed tradition or reconstruction — it is a documented claim, with its own named
    limitations already carried at full strength: Eusebius''s own court proximity (Doc_02 §2) means this
    is a court panegyrist''s report of his patron''s own account, not an independent witness''s. Confidence
    is Documented at the level of "this is what Eusebius wrote Constantine told him"; it drops to Contested
    at the level of what the vision actually was or meant, since Lactantius''s own, earlier and differently-detailed
    account (a dream, not a daylight vision; the night before the battle, not some prior day) is not simply
    reconcilable with this one.'
voice_surface: 'Usage guidance (chunk, verbatim): The Representative may draw on this story as remembered
  history, with Eusebius''s own authorship and his own stated chain of testimony named directly — "Eusebius
  tells us that Constantine himself told him..." The Representative does not claim more certainty than
  the source supports: this is not offered as settled fact about what Constantine saw, only as documented
  fact about what this world''s own founding historian recorded the emperor as having said. Where a participant
  presses on the vision''s own historicity, the honest move is naming the divergence from Lactantius''s
  account directly, not resolving it.


  Additional guidance specific to this story: pairs naturally with `ijcstory002_a-dream-before-the-battle`
  — the two accounts'' own divergence is itself formationally significant (Doc_02 §4) and should not be
  flattened into a single harmonized version.'
gravity_links:
- gravity_id: ijcgrav002
  note: 'CO-P2-04: the chunk''s Formation Ecology Connection, verbatim (the S2.4 parking, converted at
    S2.5): This is this world''s founding story, and its own actors keep returning to it because the
      commitment that starts everything here - the alliance with the empire, and the limits of
      that alliance - is what it organizes around. The alliance did not simply happen; on this
      telling it was given, which is what makes the church''s later confidence in imperial
      partnership intelligible rather than merely opportunistic. It is also the first instance
      of a pattern this world repeats constantly: a claim resting on one man''s report of what
      he alone witnessed, passed on by a single author with his own reasons for telling it that
      way.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks how this world's own alliance with imperial power began
  - participant asks about Constantine's own conversion
  - conversation reaches the Edict of Milan or the Milvian Bridge.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the participant specifically asks about Lactantius's own, differently-detailed account (retrieve
      that story instead, or both together if the divergence itself is the question).
  force_llm_vote: false
sources:
- source_id: srcIJC02
chunk_slug: the-vision-and-the-alliance
---
Migrated at the S6.2/IJC S2.4-equivalent (2026-07-31) from `data/imperial_juridical_world/story_chunks/ijcstory001_the-vision-and-the-alliance.md` (mechanical split; ownership map in `wrs/migrate/s62_ijc_s24.py`).

[Formation Ecology Connection - parked at the S2.4-equivalent; converted to gravity_links at the S2.5-equivalent per CO-P2-04] This is this world's own founding story, and its own actors return to it because it is the account this world's initiating gravity (Church-State Alliance and Its Limits, Doc_04 Candidate 2) organizes around — the alliance did not simply happen; it was *given*, on this telling, in a way that makes the church's own later confidence in imperial partnership intelligible rather than merely opportunistic. It is also the world's own first instance of a pattern this world repeats constantly: a claim resting on one figure's own report of what he alone witnessed, examined and passed on by a single, interested author (Doc_02 §2's own Eusebius Author Gravity entry).

[Final Assembly Instruction - parked verbatim as assembly provenance] Completed per `L4-Templates/Story_Repository_Chunk_Template.md` V1.0. No brackets or builder notes remain. Tier/Confidence alignment confirmed (Tier 1 → Documented at the narrative-existence level).

UPDATE 2026-08-16 (T3 readability follow-on): gate_voice_readability flagged the original text field at
FK grade 11.9 / FRE 61.7 - a colon-joined opening sentence covering the vision, the dream, and the
Milvian Bridge victory in one run, plus two more long sentences each joining several clauses with "and"
or a colon. Per Mark's decision to extend the readability pass to story records, each sentence is split
at its own existing colon, "and", or dash boundary, with two bracketed supplied subjects ("[He]",
"[Eusebius was]") added where a resulting clause had no subject of its own. No fact, hedge, quotation, or
attribution is dropped - Eusebius's own authorship and stated chain of testimony, the vision and dream as
narrated, the oath-confirmation, and the toleration outcome are all unchanged. Re-scored: FK 6.9 / FRE
74.2, clearing both thresholds.
