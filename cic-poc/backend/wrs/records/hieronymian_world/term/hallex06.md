---
id: hallex06
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
term: Patrocinium
aliases:
- Patronage
quick_meaning: The voluntary, wealth-based relationship by which an aristocratic patron sustains a scholar's
  work — this world's actual authority structure, standing in place of church office.
world_meaning: 'Authority here did not come from ordination to a bishop''s seat; it came from being trusted,
  and being funded, by someone with the wealth to make scholarship possible. A presbyter''s whole life''s
  labor — his travel, his years with a Hebrew teacher, the community he came to lead — depended on whether
  a widow''s fortune continued to back him. This made him, for all his learning, genuinely vulnerable:
  when the pope who had favored him died, and rumor turned against him, he had no office to fall back
  on, only reputation and a patron''s continued goodwill. This is not incidental background to this world;
  it is close to how this world actually worked.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: One of the commitments this household''s whole life organizes around, and the one that most holds its two homes - Rome and Bethlehem - together; the bedrock under how authority actually works here; and the clearest difference between this household and a world where authority runs through a bishop''s office.'
distortion_risk: '**Modern Hearing:**

  Risk of reading "patronage" as a minor financial detail, secondary to the "real" spiritual/scholarly
  authority.


  **World Hearing:**

  Patronage *was* the authority structure — not funding for authority, but the actual substance of it.'
retrieval:
  tier: 1
  retrieve_when:
  - Participant asks how Jerome was funded
  - participant asks about authority without episcopal office
  - participant asks about the 384-385 Rome crisis.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: The World Capsule Core has already addressed this in the current turn.
  force_llm_vote: false
sources:
- source_id: srcHAL001
  author_gravity_note: Ep.
- source_id: srcHAL015
  author_gravity_note: 108 (financing details); independent scholarly analysis (Rebenich, Cain) — genuinely
    independent corroboration of the interpretive frame, distinct from Jerome's own account of specific
    financial mechanics.
period_sense: 'The voluntary, wealth-based relationship by which an aristocratic patron sustains a scholar''s
  work - this world''s ACTUAL authority structure, standing in place of church office: a presbyter''s
  whole labor depending on whether a widow''s fortune continued to back him, leaving him genuinely vulnerable
  when papal favor died and rumor turned (chunk Quick/World Meaning).'
prior_sense: The standard Roman patron-client institution - patrocinium as the empire's ordinary machinery
  of protection and obligation - which this world inherits whole and turns to the sustaining of scholarship;
  the chunk's own framing presents the Christian use as a redirection of a thoroughly Roman form, not
  an invention.
modern_sense: '''Patronage'' as a minor financial detail, secondary to the ''real'' spiritual or scholarly
  authority (chunk Modern Hearing).'
conceptual_distance_note: 'The modern ear demotes funding to background; this world''s patronage WAS the
  authority structure - not funding FOR authority but the actual substance of it (chunk World Hearing,
  near-verbatim). Sharp gap: high grounding criterion by rule.'
semantic_domain: patronage-authority
grounding_criterion: high
voice_surface: Ask where authority lived among us and the honest answer is not a bishop's seat. It lived
  in trust and in wealth freely given - a scholar's travel, his Hebrew teacher, the roofs over his community,
  all resting on whether a widow's fortune continued to back him. When the pope who favored him died and
  rumor turned, he had no office to fall back on; only reputation, and a patron's continued goodwill.
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
field_relations:
- type: presupposes
  target_id: hallex03
  note: 'Renounced wealth is this relationship''s material source (hal_lex03 EF; the Desert material-source-of/presupposes
    pairing). Chunk Ecological Function (verbatim, absorbed per FLAG-002): One of the commitments this household''s whole life organizes around, and the one that most holds its two homes - Rome and Bethlehem - together; the bedrock under how authority actually works here; and the clearest difference between this household and a world where authority runs through a bishop''s office.'
- type: presupposes
  target_id: hallex10
  note: Matrona standing is the precondition - 'the social-historical precondition for renunciation and
    patronage' (hal_lex10 EF).
- type: associated-with
  target_id: hallex07
  note: 'The patronage relationship was conducted across the Rome/Bethlehem split by letter (hal_lex07
    World Meaning: direction, argument, and community-maintenance delivered as epistulae) - association,
    no hierarchy; symmetric mirror on hallex07.'
- type: associated-with
  target_id: hallex08
  note: 'Symmetric mirror of hallex08''s edge: the Origenist controversy was ''conducted through, and
    threatening, the patronage network'' (hal_lex08 EF).'
- type: tension-with
  target_id: hallex11
  note: 'Symmetric mirror of hallex11''s edge: the one Tensional gravity''s counter-current - authority
    held through demonstrated learning apart from both office AND wealth, ''a difference in position''
    within the ecology this term organizes (hal_lex11 EF).'
contested_claim_ids:
- halclaim003
---
Migrated at the S6.2/HAL S2.2-equivalent (2026-07-31) from `data/hieronymian_world/lexicon_chunks/hal_lex06_patrocinium.md` (mechanical split; mapping in `wrs/migrate/s62_hal_chunk_split.py`; aliases parsed under the VG-1a semantics at authoring - this world's records are born matching the runtime key space). Related-Terms and authored fields arrive at S2.3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 2 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
