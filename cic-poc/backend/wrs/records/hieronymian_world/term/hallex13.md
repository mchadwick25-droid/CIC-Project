---
id: hallex13
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
term: Praefatio
aliases:
- Jerome's prefaces
quick_meaning: 'Jerome''s prefaces to his translations and commentaries. They are not throat-clearing at the
  front of a book. They are where he explains and defends his method.'
world_meaning: 'Nearly every book this world''s central scholar translated came with its own short, combative
  essay attached — explaining why this rendering differs from the familiar one, anticipating the objection
  before it could be raised, sometimes naming the objector directly. These prefaces are where the *Hebraica
  veritas* commitment is actually argued, book by book, not merely asserted once and assumed thereafter.
  A participant who has read one of these prefaces has heard this world defending itself in its own voice,
  under real pressure, in real time.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: The primary evidentiary basis for *Hebraica veritas*; directly
  load-bearing for this world''s central textual-authority gravity.'
distortion_risk: '**Modern Hearing:**

  Risk of treating a preface as neutral scholarly apparatus, missing its combative, self-justifying rhetorical
  function.


  **World Hearing:**

  A preface was an argument, addressed to real critics, not a neutral introduction.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks how Jerome defended his translation choices
  - participant asks about the prefaces to his biblical books.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL023
  author_gravity_note: 'Jerome''s own extensive corpus of prefaces (dozens survive). Author Gravity note:
    by its very genre, a single-voice, self-justifying source type; it cannot independently corroborate
    its own claims.'
period_sense: 'Jerome''s prefaces to his translations and commentaries - ''not incidental front matter'':
  short, combative essays, one per book, explaining why this rendering differs, anticipating the objection,
  sometimes naming the objector - the genre where the Hebraica veritas commitment is actually argued,
  book by book, under real pressure (chunk Quick/World Meaning).'
prior_sense: The ordinary Latin praefatio - a spoken or written opening, a foreword - the neutral surface
  this world's combative, self-justifying use sharpens - a builder note, UNVERIFIED against this build's
  own docs.
modern_sense: A preface as neutral scholarly apparatus - skippable front matter before the real text (chunk
  Modern Hearing).
conceptual_distance_note: '''A preface was an argument, addressed to real critics, not a neutral introduction''
  (chunk World Hearing, verbatim) - and the genre is directly load-bearing for the world''s central textual-authority
  gravity (chunk EF). High grounding: the gap decides whether a participant hears this world defending
  itself in its own voice or files the defense under apparatus. The corpus row (srcHAL023) carries the
  genre''s own caveat: a single-voice, self-justifying source type.'
semantic_domain: preface-genre
grounding_criterion: high
voice_surface: Nearly every book we sent out went with a short, combative essay at its head - why this
  rendering differs from the one you know, what the objection will be, and sometimes the objector's name.
  Read one and you have heard us defending ourselves in our own voice, under real pressure, in real time.
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
field_relations:
- type: material-source-of
  target_id: hallex01
  note: 'The primary evidentiary basis for the Hebraica veritas principle (this chunk''s EF, near-verbatim;
    srcHAL023 is the corpus row) - the Desert material-source-of/presupposes pairing. Chunk Ecological
    Function (verbatim, absorbed per FLAG-002): The primary evidentiary basis for *Hebraica veritas*;
    directly load-bearing for this world''s central textual-authority gravity.'
- type: presupposed-by
  target_id: hallex01
  note: Mirror of hallex01's presupposes edge (the principle argued in, and evidenced by, this genre).
- type: associated-with
  target_id: hallex02
  note: 'Symmetric mirror of hallex02''s edge: the prefaces travel attached to the translation project''s
    own books.'
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex13_praefatio.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` was already `verified-via-authority` under the old fleet-wide default; re-examined and CONFIRMED (not simply carried over unchecked): all 1 linked source(s) show an active-discovery channel (not builder-prior-knowledge).
