---
id: ijclex004
world_id: imperial-juridical-christianity
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
term: communio
aliases:
- communion
- in communion
- out of communion
- ecclesiastical fellowship
quick_meaning: 'To be in communion with a see is to stand where that see stands. To be cut off is not a private grief. It is a public fact with consequences, and it is how our claims to authority become real rather than merely spoken.'
world_meaning: 'A letter can assert a great deal. What makes an assertion bind is whether the one who
  receives it still stands in communion with the one who sent it, or has been placed outside it. This
  is not, for us, a separate question from the sacramental one — to be outside communion is to be outside
  the altar as well — but it is also, and just as truly, the actual mechanism by which our own authority
  operates in the world, the thing a decretal or a Tome or a conciliar canon is actually reaching for
  when it speaks.


  When Leo would not receive what was settled at Chalcedon concerning the rank of the New Rome, this was
  not only a disagreement recorded in a letter. It was a refusal that had real weight precisely because
  communion with Rome is not a formality — a see that Rome will not receive stands in a genuinely different
  position than one it does. We do not think a claim is empty merely because its force depends on this
  kind of standing rather than on some power that could compel obedience by force of arms alone. The force
  here is real; it is simply not the same force a soldier commands. It is the force of being received,
  or not received, by the sees whose own reception makes a claim to Christian standing actually mean something.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: *Communio* is the mechanism, not merely the topic, behind *primatus*
  and *presbeia* alike — a participant who understands this term understands that this world''s own authority
  claims are not merely spoken assertions but enforceable through the specific, concrete instrument of
  who stands in fellowship with whom, and why a see''s own decretal or canon carries the weight it does
  only because communion is the real thing being granted or withheld.'
distortion_risk: In this world's own record, communion status is public, institutional, and consequential
  at the level of whole sees and whole regions — a genuinely juridical fact with real institutional force,
  inseparable from, not merely adjacent to, its sacramental meaning.
retrieval:
  tier: 1
  retrieve_when:
  - participant asks what it meant to be "excommunicated" or "in communion" in this world
  - participant asks how a bishop's authority was actually enforced day to day
  - conversation touches a specific dispute (Ursinus/Damasus, the Canon 28 rejection).
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the participant is asking specifically about the Eucharist as a sacramental rite rather than
      about communion as a status of standing with a see.
  force_llm_vote: false
sources:
- source_id: srcIJC13
  author_gravity_note: Leo I's own letters, both his Tome and his rejection of Canon 28, use communion-standing
    as the operative category throughout.
- source_id: srcIJC15
  author_gravity_note: Damasus's own decretal material touches this repeatedly, though **Author Gravity
    note:** much of that specific decretal corpus is of contested authenticity (Doc_02 §2; Source Registry
    row 15) — this chunk relies on Leo's own more securely-attested material as its primary evidentiary
    anchor, using the Damasine material only as corroborating rather than sole support.
modern_hearing: A modern participant is likely to hear "communion" as a private, devotional matter — a
  question of one's own standing with God, mediated by a local congregation, with no larger institutional-political
  weight.
alias_generic_override_note: '''communion'' is deliberately generic: the term IS communio - its English
  name is the bare word, no confirmed gloss carries the surface, and this world has no rival eucharistic
  term to collide with (the alexlex022 precedent; gate-caught on first emit, documented not suppressed).'
semantic_domain: juridical instrument - fellowship as enforceable status
modern_sense: '''Communion'' as private spiritual fellowship or the eucharistic act alone - the institutional
  force invisible (chunk Modern Hearing).'
period_sense: To be in communion with a see is to stand where it stands; being cut off is a public, consequential
  fact - the actual instrument by which authority claims become real rather than merely spoken; juridical
  and sacramental inseparably.
prior_sense: Latin communio - 'sharing, mutual participation'; the ordinary word made a juridical status;
  a builder note, UNVERIFIED.
grounding_criterion: high
conceptual_distance_note: 'GROUNDING (the enum''s free-text companion, carried here): Leo''s letters (Tome
  + Canon-28 rejections) using communion-standing as the operative category throughout - the chunk''s
  own more-securely-attested anchor, the contested Damasine decretals held aside (row 15). | DISTANCE:
  The alias ''communion'' is a documented generic exception (alias_generic_override_note; the alexlex022
  precedent).'
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
voice_surface: '''To be in communion with a see is to stand where that see stands; to be cut off from
  it is not a private grief but a public, consequential fact.'''
field_relations:
- type: mechanism-behind
  target_id: ijclex001
  note: 'Chunk Ecological Function (verbatim, absorbed per FLAG-002): *Communio* is the mechanism, not
    merely the topic, behind *primatus* and *presbeia* alike — a participant who understands this term
    understands that this world''s own authority claims are not merely spoken assertions but enforceable
    through the specific, concrete instrument of who stands in fellowship with whom, and why a see''s
    own decretal or canon carries the weight it does only because communion is the real thing being granted
    or withheld. The mechanism behind the primacy claim (the EF''s own word).'
- type: associated-with
  target_id: ijclex001
  note: Mirror of ijclex001's associated-with (the reciprocity gate's symmetric-type rule); the mechanism-behind
    edge above carries the substance.
- type: associated-with
  target_id: ijclex002
  note: 'Symmetric mirror: rank exercised through fellowship-standing.'
- type: associated-with
  target_id: ijclex008
  note: 'The boundary''s two sides: communio the inclusion instrument, haeresis the exclusion instrument
    - one juridical machinery; symmetric.'
- type: associated-with
  target_id: ijclex005
  note: Communion discipline is the sacramental lever the Ambrosian formula wields against a crowned communicant;
    symmetric.
- type: associated-with
  target_id: ijclex009
  note: A Tome's reception IS a communion event - received into fellowship or refused; symmetric.
- type: associated-with
  target_id: ijclex011
  note: 'The 386 standoff: the church''s own space held as communion-space against imperial demand; symmetric.'
contested_claim_ids: []
---
Migrated at the S6.2/IJC S2.2-equivalent (2026-07-31) from `data/imperial_juridical_world/lexicon_chunks/ijclex004_communio.md` (mechanical split; mapping and alias authoring tables in `wrs/migrate/s62_ijc_s22.py` - the FLAG-035 corrections and the one Rule-A birth drop declared there; the third world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[Final Assembly Instruction - parked at the S2.2-equivalent; typed home per the splitter docstring] Completed per `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0. No brackets or builder notes remain. CT tag not applied — this term's own function in this world is well-attested and not, on this document's own review, subject to the specific kind of live scholarly contest Article 26 §B requires for the tag.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 2 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
