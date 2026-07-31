---
id: hallex02
world_id: hieronymian-ascetic-literary
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
term: Vulgata (translation project)
aliases:
- The Vulgate
quick_meaning: Jerome's decades-long labor of translating and correcting the Latin Bible, later — long
  after this world's own span — known as "the Vulgate."
world_meaning: 'This is not one act but a project stretched across a working life: the Gospels revised
  against the Greek while still in Rome, under a pope''s own commission; then, at Bethlehem, book after
  book of the Hebrew scriptures rendered afresh, each with its own preface explaining and defending the
  choices made. This world did not call the finished, standard thing "the Vulgate" — that name and that
  status belong to a much later church than this one, once the older Latin versions had finally, slowly,
  been set aside in its favor. Within this world''s own span, the project was still contested, still incomplete
  in parts, still one translator''s ongoing labor rather than a settled, universal text.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: The material product of *Hebraica veritas*; anchors the community''s
  scholarly ministry; dedicated, book by book, to the women who requested and funded it.'
distortion_risk: '**Modern Hearing:**

  A participant is likely to assume "the Vulgate" as an already-standard, church-wide text existed as
  such within this world''s own time.


  **World Hearing:**

  This world experienced the project as ongoing, partial, and contested — not yet the unchallenged standard
  it later became.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks about "the Vulgate"
  - participant asks what Jerome actually translated and when.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL023
  author_gravity_note: Jerome's own prefaces and commentaries. The gradual, uneven reception of the finished
    project into later Western Christianity is not asserted as achieved within this world's own 382–420
    span.
period_sense: 'A decades-long working project, not a finished thing: the Gospels revised in Rome under
  papal commission, then at Bethlehem the Hebrew scriptures rendered afresh book by book, each with its
  own defending preface - still contested, still incomplete in parts, within this world''s own span. The
  name ''the Vulgate'' and the standard-text status belong to a much later church (chunk Quick/World Meaning).'
prior_sense: The ordinary Latin vulgatus, 'common, widespread, publicly known' - the surface the much
  later name applies; within this world's span the project had no such settled name at all - a builder
  note, UNVERIFIED against this build's own docs, which carry only the anachronism flag itself.
modern_sense: '''The Vulgate'' assumed to exist within this world''s own time as an already-standard,
  church-wide text (chunk Modern Hearing).'
conceptual_distance_note: 'A retrojection gap in the memra/Catholicos class: the finished name and status
  are read back onto an ongoing, partial, contested labor - one translator''s project, defended preface
  by preface, not yet anyone''s standard (chunk World Hearing). Standard grounding: the correction is
  a dating/status guard, and the record''s own alias set is empty for exactly this reason (the S2.2 FLAG-028
  resolution; reachability = term key ''vulgata'').'
semantic_domain: translation-project
grounding_criterion: standard
voice_surface: What later ages call the Vulgate was, with us, a labor still under way - the Gospels corrected
  in Rome under Damasus, then book after book of the Hebrew scriptures at Bethlehem, each sent out with
  its own preface answering the objections we knew would come. We did not have a finished Bible; we had
  a working life.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
field_relations:
- type: presupposes
  target_id: hallex01
  note: 'The organizing commitment behind the whole project (hal_lex01 EF names Vulgata as what Hebraica
    veritas organizes). Chunk Ecological Function (verbatim, absorbed per FLAG-002): The material product
    of *Hebraica veritas*; anchors the community''s scholarly ministry; dedicated, book by book, to the
    women who requested and funded it.'
- type: associated-with
  target_id: hallex13
  note: Nearly every translated book 'came with its own short, combative essay attached' (hal_lex13 World
    Meaning) - the prefaces travel inside the project's volumes (srcHAL023's containment relation) - association,
    no hierarchy.
- type: associated-with
  target_id: hallex07
  note: The project was 'dedicated, book by book, to the women who requested and funded it' (this chunk's
    EF) - the dedications and covering letters are epistulae; symmetric mirror on hallex07.
contested_claim_ids:
- halclaim001
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex02_vulgata.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.

[FLAG-028 correction applied at the S2.8-equivalent (2026-07-31): alias re-authored as the unqualified 'The Vulgate' after retrieval parity MEASURED the reachability regression the flag predicted (HAL-RT-01 recall 1.0 -> 0.5 staged vs deployed - the qualified alias line's English surface was doing live cross-encoder work). The S2.2 empty-set reading held that the author's parenthetical was an anachronism flag; the flag's guard survives in full in this record's own prose (quick_meaning / world_meaning / distortion_risk) - the alias map is retrieval reachability, not voice usage. Gate-safe: no blocklist hit, no Rule-B collision; alias_safety re-run 0.]
