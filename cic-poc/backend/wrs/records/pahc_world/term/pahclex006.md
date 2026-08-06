---
id: pahclex006
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
term: presbyterion (πρεσβυτέριον)
aliases:
- council of elders
- presbytery
quick_meaning: The *presbyterion* is the council of elders gathered around the bishop — tuned to him,
  Ignatius says, the way strings are tuned to a harp.
world_meaning: 'Ignatius speaks of the presbyterion — the gathered body of presbyters — as something that
  should be harmonized with the bishop the way a harp''s strings are tuned together. This council supports
  and surrounds the bishop''s leadership, neither replacing him nor merely following instructions. Where
  there is a bishop, there is a presbyterion around him.


  But this way of speaking belongs to Ignatius and to communities shaped by his letters. In Rome, no such
  presbyterion-around-a-bishop appears in the correspondence we have — the presbyters govern together
  without a single figure at their center. The presbyterion as Ignatius describes it is a Strand A pattern,
  real and deeply formative where it is practiced, but not the only shape governance has taken among us.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: This term specifies a particular form the Authority Consolidation
  question (G01) takes in communities with a single bishop. It marks the difference between a bishop who
  acts alone and one who acts with a council.'
distortion_risk: 'In this world, presbyterion names the gathered body of elders around a bishop — a council,
  not an institution. And it is not found everywhere.


  **Confidence:**

  Documented, with maximal single-witness dependency. The presbyterion and its lyre-image are directly
  attested in Ignatius''s own letters, but no other voice in this world''s evidentiary base independently
  corroborates the term.'
retrieval:
  tier: 2
  retrieve_when:
  - participant asks about the council of elders, the presbytery, or how presbyters function together
    around a bishop.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about a modern presbytery or denominational structure.
  force_llm_vote: false
sources:
- source_id: srcPAHCP03
  author_gravity_note: 'Ignatius, Letter to the Ephesians 4, Letter to the Magnesians 6–7, Letter to the
    Philadelphians 5 (the presbyterion as harp strings around the bishop).


    Note: this term rests on a single voice within this world''s own Native evidentiary base — Ignatius
    alone supplies it, with no independent corroboration elsewhere in this world''s sources. See episkopos''s
    own Key Sources for the fuller Author-Gravity caution this single-witness dependency shares.'
modern_hearing: A modern reader may hear "presbytery" and think of a denominational governing body or
  a physical building.
period_sense: 'The gathered body of presbyters around a bishop - tuned to him, Ignatius says, as strings
  to a harp; supporting without replacing and without merely obeying. A Strand A pattern: real and deeply
  formative where practiced, absent from the Roman correspondence entirely (chunk Quick/World Meaning).'
prior_sense: The word's nearer inheritance is the Jewish elder-council (the LXX/NT presbyterion of Jerusalem)
  - a council-word, not a place-word; a builder note, UNVERIFIED against this build's own docs.
modern_sense: A denominational governing body or a physical building (chunk Modern Hearing).
conceptual_distance_note: 'A council, not an institution - and not found everywhere (chunk World Hearing).
  The chunk''s own confidence carries the fleet-familiar single-witness honesty: ''maximal single-witness
  dependency… no other voice independently corroborates the term.'' Standard grounding.'
semantic_domain: council-around-bishop
grounding_criterion: standard
voice_surface: Where one of our households has a bishop, his elders gather around him as a presbyterion
  - tuned together, Ignatius says, the way strings are tuned to a harp. But this way of speaking is his,
  and the households his letters formed. In Rome the elders govern together, and no such council-around-a-bishop
  appears in anything they wrote.
original_script: πρεσβυτέριον
confidence:
  citation_specificity: A
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: corroborating
  formation_confidence: Documented
field_relations:
- type: presupposes
  target_id: pahclex001
  note: 'The chunk''s own EF: the form G01 takes ''in communities with a single bishop'' - the council-around
    exists only where the bishop does. Chunk Ecological Function (verbatim, absorbed per FLAG-002): This
    term specifies a particular form the Authority Consolidation question (G01) takes in communities with
    a single bishop. It marks the difference between a bishop who acts alone and one who acts with a council.'
- type: associated-with
  target_id: pahclex002
  note: Symmetric mirror of pahclex002's edge (the same elders, differently configured).
contested_claim_ids:
- pahcclaim003
---
Migrated at the S6.2/PAHC S2.2-equivalent (2026-07-31) from `data/pahc_world/lexicon_chunks/pahclex006_presbyterion.md` (mechanical split; mapping in `wrs/migrate/s62_pahc_s22.py`; aliases parsed under the VG-1a semantics with the preflighted Rule-A drops at birth - the second world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
