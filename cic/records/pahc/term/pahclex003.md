---
id: pahclex003
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
term: ekklesia (ἐκκλησία)
aliases:
- the church of God
quick_meaning: >-
  The assembly. The called-out gathering. Not a building and not an
  institution, but the people who meet under whatever roof will hold them.
  Letters and a shared table join them to every other such gathering.
world_meaning: 'When someone asks who we are, we have only one name to answer with: the ekklesia, the
  assembly, the church of God sojourning in whatever city our members happen to live. It is not a title
  that distinguishes us from our neighbors down the street — it is the plain fact of being called out
  and gathered. We have no building the city can point to. What we have is a household that opens its
  door on the first day of the week, and a name that travels between such households by letter faster
  than any person could carry it on foot.


  The ekklesia in Antioch and the ekklesia in Rome and the ekklesia in Corinth are the same ekklesia,
  not because they share a common structure or answer to a common office, but because the letters that
  travel between them carry the proof that we belong to something larger than the room we gather in. When
  a letter arrives from another ekklesia, it is never only news — it is the assurance that somewhere else,
  under a different roof, others hold the same name and face the same questions we face.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: This term names what this world''s participants call themselves
  — and more, it names the translocal network (G02) that holds them together without a central structure.
  A participant who understands ekklesia understands why the letter and the table do the heavy lifting
  of unity, not a hierarchy.'
distortion_risk: 'In this world, ekklesia names the gathered people themselves — portable, without property,
  identified by a shared meal and a circulation of letters rather than by any fixed location or legal
  standing.


  **Living Tradition Note:**

  This entry describes this world''s own formation ecology (c.70–200 CE). It makes no claim about how
  any present-day tradition currently defines or understands the church.


  **Confidence:**

  Documented. Every extant voice in this world''s own record — 1 Clement, Ignatius, Polycarp, and the
  Didache — independently uses this term as the community''s own self-designation; this is among the most
  securely attested points in this world''s entire vocabulary.'
retrieval:
  tier: 1
  retrieve_when:
  - participant asks what the church is, how early Christians understood themselves as a community, or
    what holds them together across different cities.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about a church building or denominational structure with no connection
      to this period's understanding.
  force_llm_vote: false
sources:
- source_id: srcPAHCP03
  author_gravity_note: Ignatius of Antioch, all seven letters (ekklesia as address and identity).
- source_id: srcPAHCP02
  author_gravity_note: 1 Clement (Rome to Corinth — ekklesia addressing ekklesia).
- source_id: srcPAHCP04
  author_gravity_note: Polycarp, Letter to the Philippians (ekklesia self-reference).
- source_id: srcPAHCP01
  author_gravity_note: Didache 4:14, 9–10, 14 (the gathering).
- source_id: srcPAHCP06
  author_gravity_note: Justin Martyr, First Apology 67 (the Sunday gathering described — cited here as
    a topical parallel; not part of this term's original evidentiary citation set).
modern_hearing: A modern reader hears "church" and may picture a building, a denomination, or an institution
  with established structures.
period_sense: 'The community''s one self-name: the assembly, the church of God sojourning in whatever
  city its members live - no building, no property, a household door opening on the first day of the week;
  the ekklesia in Antioch and Rome and Corinth one ekklesia not by shared structure but by the letters
  traveling between them (chunk Quick/World Meaning).'
prior_sense: 'The Greek polis''s own ekklesia - the summoned assembly of citizens - and the LXX''s use
  for Israel gathered before God: a civic word already carrying ''called out and gathered'' before these
  communities took it as their name; a builder note, UNVERIFIED against this build''s own docs.'
modern_sense: '''Church'' as a building, a denomination, or an institution with established structures
  (chunk Modern Hearing).'
conceptual_distance_note: 'The gathered people themselves - portable, propertyless, identified by meal
  and letters rather than location or legal standing (chunk World Hearing). Sharp gap: high grounding
  criterion - the building/institution reading erases exactly the household-and-letter fabric this world
  is.'
semantic_domain: gathered-assembly
grounding_criterion: high
voice_surface: 'When someone asks who we are, we have one name: the ekklesia - the assembly, called out
  and gathered. The city can point to no building of ours. What we have is a door that opens on the first
  day of the week, and letters that carry our name between cities faster than any of us could walk it.'
original_script: ἐκκλησία
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
field_relations:
- type: associated-with
  target_id: pahclex004
  note: 'The chunk''s own EF: ''the letter and the table do the heavy lifting of unity, not a hierarchy'' - the
    table half is eucharistia; symmetric both ways. Chunk Ecological Function (verbatim, absorbed per
    FLAG-002): This term names what we call ourselves - and more than that, it names the network that holds
    us together without any central structure. A participant who understands ekklesia understands why the
    letter and the table do the heavy work of unity here, and not a hierarchy.'
- type: associated-with
  target_id: pahclex001
  note: Symmetric mirror of pahclex001's edge (the assembly and its oversight - the deployed reciprocity
    map).
contested_claim_ids:
- pahcclaim001
chunk_slug: ekklesia
chunk_related_line: eucharistia, episkopos
---
Migrated at the S6.2/PAHC S2.2-equivalent (2026-07-31) from `data/pahc_world/lexicon_chunks/pahclex003_ekklesia.md` (mechanical split; mapping in `wrs/migrate/s62_pahc_s22.py`; aliases parsed under the VG-1a semantics with the preflighted Rule-A drops at birth - the second world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 5 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
