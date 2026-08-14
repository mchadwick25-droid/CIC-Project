---
id: pahclex008
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
term: prophetes (προφήτης)
aliases:
- prophet
- prophets
quick_meaning: 'One who speaks as the Spirit prompts. Welcomed where genuine, tested where doubtful. In some places
  already giving way to the steadier offices of overseer and elder.'
world_meaning: 'Prophets still move among us — those who speak under the Spirit''s prompting, who arrive
  at a household and may preside at the thanksgiving if they are genuine. The Didache gives careful instructions
  for testing them: let a prophet speak in the Spirit, but if he asks for money for himself, or if he
  does not practice what he teaches, he is a false prophet. A true prophet may stay two or three days;
  longer than that raises questions.


  But even as the Didache speaks of prophets, it also instructs communities to appoint bishops and deacons,
  "for they too conduct the ministry of the prophets and teachers." The prophetic office is not disappearing
  in our time, but it is being joined — and in some places replaced — by the more settled offices. Where
  a bishop now presides, the prophet''s place at the table is less certain.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: This term connects to the question of Authority Consolidation
  (G01) from a different angle: the shift from charismatic, itinerant authority to settled, local office.'
distortion_risk: 'In this world, prophets are still active — Spirit-led figures who move between communities
  — but their place is being negotiated alongside emerging local offices.


  **Confidence:**

  Documented within this community''s own record — the Didache directly attests these tests — but single-source,
  and not established as universal practice across this world''s other communities.'
retrieval:
  tier: 2
  retrieve_when:
  - participant asks about prophets, prophecy, itinerant teachers, or the Didache's instructions about
    testing prophets.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: participant is asking about Old Testament prophets or modern charismatic prophecy with no connection
      to this period.
  force_llm_vote: false
sources:
- source_id: srcPAHCP01
  author_gravity_note: 'Didache 11–13 (tests for genuine versus false prophets), 15:1 (transition to local
    office).


    Note: within this world''s own Native evidentiary base, these specific tests for prophets are single-source
    — the Didache alone attests them.'
- source_id: srcPAHCP05
  author_gravity_note: (Hermas, Shepherd, Mandate 11 addresses testing true and false prophets in the
    wider historical record and is a topical parallel, but its correspondence to this specific community's
    own practice is not established by this world's own sources.)
modern_hearing: A modern reader may hear "prophet" and think of someone who predicts the future, or may
  assume prophets had already disappeared by this period.
period_sense: 'Spirit-prompted speakers still moving between households - presiding at the thanksgiving
  if genuine, tested by the Didache''s own rules (asks money for himself: false; does not practice what
  he teaches: false; stays past three days: questions) - while the same handbook instructs appointing
  bishops and deacons ''for they too conduct the ministry of the prophets and teachers'': the charismatic
  office being joined, and in places replaced, by the settled ones (chunk Quick/World Meaning).'
prior_sense: The Greek prophetes and the Jewish prophetic inheritance - the one who speaks for God - carried
  into an itinerant office these communities still received and tested; a builder note, UNVERIFIED against
  this build's own docs.
modern_sense: A future-predictor, or an office assumed already vanished by this period (chunk Modern Hearing).
conceptual_distance_note: Still active, still fed and housed - but 'their place is being negotiated alongside
  emerging local offices' (chunk World Hearing); single-source per the chunk's own confidence (the Didache's
  tests, with Hermas Mandate 11 a topical parallel the chunk declines to promote). Standard grounding.
semantic_domain: itinerant-prophecy
grounding_criterion: standard
voice_surface: 'Prophets still come to our doors - and we test them, as we were taught: a true prophet
  does not ask money for himself, lives what he teaches, and moves on within a few days. If he is genuine,
  he may preside at the thanksgiving. But we have also begun appointing bishops and deacons who carry
  that same ministry - and where a bishop now presides, the prophet''s place at the table is less certain
  than it was.'
original_script: προφήτης
confidence:
  citation_specificity: A
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: corroborating
  formation_confidence: Documented
field_relations:
- type: tension-with
  target_id: pahclex001
  note: 'The chunk''s own EF: G01 ''from a different angle - the shift from charismatic, itinerant authority to
    settled, local office''; symmetric mirror on pahclex001. Chunk Ecological Function (verbatim, absorbed
    per FLAG-002): This term comes at the question of who leads from a different angle: the shift from
    wandering, charismatic authority to settled, local office.'
- type: associated-with
  target_id: pahclex005
  note: Didache 15:1 appoints bishops AND deacons for they too conduct the ministry of the prophets and
    teachers - the chunk's own Related-Terms membership (the deployed reciprocity map - the S2.8 render-parity
    catch, fixed as a declared S2.3 correction); symmetric mirror.
chunk_slug: prophetes
chunk_related_line: episkopos, diakonos
---
Migrated at the S6.2/PAHC S2.2-equivalent (2026-07-31) from `data/pahc_world/lexicon_chunks/pahclex008_prophetes.md` (mechanical split; mapping in `wrs/migrate/s62_pahc_s22.py`; aliases parsed under the VG-1a semantics with the preflighted Rule-A drops at birth - the second world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 2 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
