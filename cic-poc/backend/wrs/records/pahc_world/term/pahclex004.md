---
id: pahclex004
world_id: post-apostolic-house-church
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
term: eucharistia (εὐχαριστία)
aliases:
- eucharist
- thanksgiving
- the Lord's Supper
quick_meaning: The *eucharistia* is the thanksgiving — the meal of bread and cup over which we give thanks,
  returning to that table again and again to be re-formed into the body we belong to.
world_meaning: 'Whatever else has been decided or left open among us, we gather to give thanks over bread
  and cup. The meal itself does more of our community''s ongoing forming than anything else we do. We
  return to it again and again, and each return is not merely a repetition but a re-making of who we are
  together.


  Who may preside at this table is never a merely liturgical question for us. It reaches straight into
  the argument about who leads. Ignatius writes that no eucharist is to be considered valid except under
  the bishop or one he has appointed — and in households that have received his letters, this instruction
  shapes everything about order. But we know too of gatherings where no single bishop presides, where
  the presbyters together give thanks, and nothing in their practice suggests they feel something is missing.


  What it means to refuse a rival teacher''s separate table — set up instead of our own, over against
  our unity — is equally serious. To hold to our own table is, in the same breath, an act of worship and
  an act of belonging. The table and the question of authority cannot be separated.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: This term anchors the Liturgical Practice gravity (G07), which
  the ecological reconstruction treats as doing the heaviest lifting of any single practice in this world.
  It also ties directly into G01 (Authority Consolidation) through the question of who presides.'
distortion_risk: 'In this world, eucharistia names what happens at the table — thanksgiving over bread
  and cup — but the exact form varies from household to household. What is constant is that the table
  itself is central to forming and maintaining the community.


  **Living Tradition Note:**

  This entry describes this world''s own formation ecology (c.70–200 CE). It makes no claim about how
  any present-day tradition currently defines, practices, or understands the eucharist.


  **Confidence:**

  Documented for the baseline practice — thanksgiving over bread and cup is independently attested across
  every strand of this world''s evidence. Contested for Justin''s fuller account specifically: whether
  it represents a genuinely wider, network-level development or one community''s own particular elaboration
  that happened to survive in unusual detail is not resolved by this world''s own evidentiary base (see
  CT Contest Type below).'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks about the Lord's Supper, communion, the eucharist, what happens at the table, or
    the meal that forms the community.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about modern eucharistic theology or transubstantiation debates with no
      connection to this period.
  force_llm_vote: false
sources:
- source_id: srcPAHCP01
  author_gravity_note: Didache 9–10, 14 (thanksgiving prayers over cup and bread, no institution narrative).
- source_id: srcPAHCP03
  author_gravity_note: Ignatius, Letter to the Philadelphians 4 (the "one eucharist" instruction) and
    Letter to the Smyrnaeans 8 (bishop-validated eucharist — a related but separate instruction; Smyrnaeans
    8 does not itself contain the "one eucharist" phrase).
- source_id: srcPAHCP06
  author_gravity_note: 'Justin Martyr, First Apology 65–67 (fullest surviving account — distribution to
    the absent, explanatory theology of the elements).


    Note: Justin''s account, despite being the fullest, should not be read as more representative simply
    because it is more explained — a live methodological caution this world''s own reconstruction carries
    throughout rather than resolves. See CT Contest Type below.'
modern_hearing: A modern reader may hear "eucharist" and assume a uniform ritual with established prayers,
  or may think of later theological debates about presence and sacrifice.
period_sense: 'The thanksgiving over bread and cup - the meal that does ''more of our community''s ongoing
  forming than anything else we do''; its presidency inseparable from the authority question (Ignatius:
  no valid eucharist apart from the bishop - in the households his letters shaped; elsewhere presbyters
  give thanks together with nothing felt missing); refusing a rival''s separate table an act of worship
  and belonging in one breath (chunk Quick/World Meaning).'
prior_sense: The ordinary Greek eucharistia, 'thanksgiving' - gratitude itself, the word every letter-writer
  used for thanking God or a benefactor, specialized here to THE thanksgiving; a builder note, UNVERIFIED
  against this build's own docs.
modern_sense: A uniform ritual with established prayers, or the later debates about presence and sacrifice
  (chunk Modern Hearing).
conceptual_distance_note: 'Form varies household to household (the Didache''s prayers carry no institution
  narrative; Justin''s account is fullest but not thereby most representative - the chunk''s own methodological
  caution, parked with its CT section for S2.6); what is constant is the table''s centrality to forming
  the community. Sharp gap: high grounding criterion.'
semantic_domain: thanksgiving-table
grounding_criterion: high
voice_surface: Whatever else is decided or left open among us, we gather to give thanks over bread and
  cup, and each return to that table re-makes who we are together. Who may preside is never a small question
  - it reaches straight into who leads. And to hold to our own table against a rival's separate one is
  worship and belonging in the same act.
original_script: εὐχαριστία
confidence:
  citation_specificity: A
  verification_state: verified-via-authority
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
field_relations:
- type: associated-with
  target_id: pahclex001
  note: 'The chunk''s own EF: G07 anchored, tying directly into G01 through who presides. Chunk Ecological
    Function (verbatim, absorbed per FLAG-002): This term anchors the Liturgical Practice gravity (G07),
    which the ecological reconstruction treats as doing the heaviest lifting of any single practice in
    this world. It also ties directly into G01 (Authority Consolidation) through the question of who presides.'
- type: associated-with
  target_id: pahclex003
  note: Symmetric mirror of pahclex003's edge (letter and table).
- type: associated-with
  target_id: pahclex005
  note: Justin's deacons carry the elements to the absent (pahclex005 World Meaning); symmetric mirror.
- type: associated-with
  target_id: pahclex010
  note: 'The chunk-attested bridge: agape <-> eucharistia, ''aware they may name the same thing or two
    things, without forcing an answer'' (pahclex010); symmetric mirror.'
- type: presupposes
  target_id: pahclex011
  note: '''Baptism opens the door to the table'' (pahclex011 World Meaning) - the threshold ordering,
    typed as the Desert pairing.'
contested_claim_ids:
- pahcclaim002
---
Migrated at the S6.2/PAHC S2.2-equivalent (2026-07-31) from `data/pahc_world/lexicon_chunks/pahclex004_eucharistia.md` (mechanical split; mapping in `wrs/migrate/s62_pahc_s22.py`; aliases parsed under the VG-1a semantics with the preflighted Rule-A drops at birth - the second world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[CT Contest Type - parked at the S2.2-equivalent; home arrives with the contested_claim records (S2.6-equivalent) / S2.3 authoring] **Historical scope** — whether Justin's fuller, more explained account (First Apology 65–67) represents a network-wide template or one community's own development.
