---
id: ijclex008
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
term: haeresis
aliases:
- heresy
quick_meaning: 'A teaching placed outside what the church will recognise, and now outside what the law will recognise. With us it is a legal exclusion as much as a theological one.'
world_meaning: 'A teaching does not become *haeresis* for us merely because a bishop disagrees with it.
  It becomes *haeresis* when the church, gathered and confirmed, declares it so — and, in our own world''s
  own record, increasingly, when the emperor''s own law then gives that declaration legal force and consequence.
  This double character is not something we experience as two separate facts sitting side by side. The
  theological judgment and the legal exclusion are, for us, one act, arrived at together, and we do not
  think this makes the theological judgment any less real or any more merely political for having legal
  teeth.


  [Ecological Function - parked at the S2.2-equivalent; restructured into typed field_relations at the
  S2.3-equivalent per SS3.2 / FLAG-002]: *Haeresis* is what *homoios* was named as, once our own settlement
  changed — a participant who understands this term understands that the same juridical machinery that
  names and excludes was, at another point in this world''s own record, the machinery enforcing the very
  teaching later so named.'
distortion_risk: in this world's own record, the theological and the legal-juridical senses of this term
  are not sequential (belief first, law second) but simultaneous and mutually constituting.
retrieval:
  tier: 2
  retrieve_when:
  - participant asks how a teaching came to be legally excluded, or asks about the relationship between
    imperial law and doctrinal boundary-drawing.
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the question is really about a specific confession's own content (retrieve homoios instead).
  force_llm_vote: false
sources:
- source_id: srcIJC16
  author_gravity_note: The Theodosian Code, Book 16 (its legal use of this category); the conciliar canons
    (its doctrinal use).
modern_hearing: a modern participant may assume "heresy" names a purely doctrinal category, separate from
  and prior to any legal consequence.
semantic_domain: juridical category - doctrinal exclusion
modern_sense: '''Heresy'' as purely theological error, church-internal - the legal force invisible (chunk
  Modern Hearing).'
period_sense: A teaching placed outside what the church AND NOW THE LAW ITSELF will recognize - theological
  and legal-juridical senses simultaneous and mutually constituting, not sequential.
prior_sense: Greek hairesis - 'choice, school, sect' (the neutral doxographic sense); Latin haeresis inherits
  it already narrowed; a builder note, UNVERIFIED.
grounding_criterion: high
conceptual_distance_note: 'GROUNDING (the enum''s free-text companion, carried here): Theodosian Code
  Book 16 (the legal use, row 16) + the conciliar canons (the doctrinal use, row 9). | DISTANCE: The CT
  contest: whether law-backed doctrinal exclusion was corruption or consolidation is a live inter-tradition
  contest; the homoios case keeps the term honest (the machinery once enforced what it later named).'
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-31'
  evidentiary_weight: load-bearing
  formation_confidence: Contested
voice_surface: '''Haeresis names a teaching placed outside what the church, and now the law itself, will
  recognize - a juridical exclusion as much as a theological one, in our own record.'''
field_relations:
- type: associated-with
  target_id: ijclex003
  note: 'Chunk Ecological Function (verbatim, absorbed per FLAG-002): *Haeresis* is what *homoios* was
    named as, once our own settlement changed — a participant who understands this term understands that
    the same juridical machinery that names and excludes was, at another point in this world''s own record,
    the machinery enforcing the very teaching later so named. Symmetric mirror of the enforced-then-condemned
    honesty.'
- type: associated-with
  target_id: ijclex004
  note: 'Symmetric mirror: the one machinery''s two instruments.'
- type: associated-with
  target_id: ijclex007
  note: 'Symmetric mirror: named in the arena.'
contested_claim_ids:
- ijcclaim005
chunk_slug: haeresis
chunk_related_line: homoios, communio, concilium
---
Migrated at the S6.2/IJC S2.2-equivalent (2026-07-31) from `data/imperial_juridical_world/lexicon_chunks/ijclex008_haeresis.md` (mechanical split; mapping and alias authoring tables in `wrs/migrate/s62_ijc_s22.py` - the FLAG-035 corrections and the one Rule-A birth drop declared there; the third world born matching the runtime key space AND the gate). Related-Terms and authored fields arrive at S2.3.

[CT Contest Type - parked at the S2.2-equivalent; typed home per the splitter docstring] **Historical scope:** whether this term functioned as a settled juridical category from Nicaea onward, or became so only gradually, alongside and partly through the Theodosian Code's own legal innovations, is itself contested in the modern scholarship this document draws on.

[Final Assembly Instruction - parked at the S2.2-equivalent; typed home per the splitter docstring] Completed per `L4-Templates/Deployment_Lexicon_Chunk_Template.md` V1.0. No brackets or builder notes remain; CT Contest Type completed per Doc_06 §3.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 1 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
