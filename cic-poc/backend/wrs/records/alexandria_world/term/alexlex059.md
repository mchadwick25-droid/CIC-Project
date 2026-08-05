---
world_id: alexandria-catechetical
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
id: alexlex059
term: Catechetical School / Didaskaleion
aliases:
- the didaskaleion
- the catechetical school
- the school of Alexandria
- the teaching succession
quick_meaning: For this world the didaskaleion names its own teaching life - teachers the community knew
  to be truly formed, seekers who came to read beside them, and a reading handed from one to the next.
  Whether that was a formal institution with a succession of heads is a genuinely open question the record
  cannot settle.
world_meaning: 'What lived among us was accompanied reading: one who had been given sight read beside
  another until that other began to see for himself, and those who were formed became teachers to others
  in turn. The community remembers a line - Pantaenus, Clement, Origen, on to Didymus - and remembers
  it with gratitude: the handing-on mattered enough to keep the names.


  Whether there stood behind that memory a formal institution - a house with an office and a roll of masters,
  one succeeding the next - was never a question our own life stopped to ask, and it is genuinely contested
  now: the succession''s main narrator wrote generations later, and the record has no second witness to
  the institutional continuity he presents. What is well-attested is the KIND of authority the teacher
  held - grounded in demonstrated wisdom, enacted as accompaniment - and that authority does not depend
  on the institutional question being resolved (alexlex029''s carried contest; alexclaim004; Doc_01 SS1.2).'
modern_hearing: '**Modern Hearing:**

  "The Catechetical School of Alexandria" as a settled historical institution - an ancient university
  with founding date, faculty, and succession neatly documented.'
distortion_risk: '**World Hearing:**

  Accompanied reading remembered as a living line of teachers - the reality is the formation relationship
  and the community''s memory of its handing-on, with the institutional form held open, not asserted.'
period_sense: 'The teaching tradition of Alexandria as its own community remembered it: formed teachers,
  seekers who came to read, a remembered succession of names (Doc_01 SS1.2; alexclaim004.claim).'
prior_sense: Didaskaleion as ordinary Greek for a place of teaching - a schoolroom; the word itself carries
  no institutional grandeur - noted from standard lexica, UNVERIFIED against a registry source.
modern_sense: 'A proto-university: formal institution, official heads, continuous succession - the reading
  van den Broek and van den Hoek deny for the period before Origen, and Scholten affirms only as a theological
  (not catechumen-training) school (Doc_06 SS2).'
conceptual_distance_note: 'The modern frame asks an institutional question (was the school real?); the
  world''s own register is the formation relationship the question papers over. The contest is Historical
  scope (Doc_06 SS2), Eusebius HIGH Author-Gravity on the succession particulars; the voice answers from
  the attested authority-kind, never the institutional claim. Sharp frame gap: high grounding criterion.'
semantic_domain: formation-institutions
grounding_criterion: high
voice_surface: There were teachers among us the community knew to be truly formed - you could see that
  they saw - and seekers came to read beside them, and the reading passed from one to the next. Whether
  a later tongue names that an institution or something looser was never a question our own life stopped
  to ask.
confidence:
  citation_specificity: B
  verification_state: named-not-rechecked
  verification_date: '2026-07-28'
  evidentiary_weight: corroborating
  formation_confidence: Contested
retrieval:
  tier: 2
  force_llm_vote: false
  retrieve_when:
  - participant asks whether the catechetical school was a real institution, or about its succession of
    heads
  - participant asks how the Alexandrian school was organized, founded, or run
  - a scholarly framing of the school's historicity arrives (van den Broek / Scholten class)
  do_not_retrieve_when:
  - condition_type: sense-disambiguation
    text: the participant asks what studying under a teacher was LIKE - retrieve alexstory001/alexlex029
      territory (the formation relationship), not the institutional contest
  - condition_type: sense-disambiguation
    text: the Teacher chunk has already surfaced the carried contest this turn (alexlex029 reproduces
      it)
sources:
- source_id: srcALX009
  locus: Eusebius, Ecclesiastical History (the succession narrative)
  author_gravity_note: The main - often sole - source for the succession; HIGH Author-Gravity risk, carried
    on every succession particular (Doc_06 SS2).
- source_id: srcALX021
  locus: 'The Alexandrian Church: People and Institutions'
  author_gravity_note: Institutional scholarship on what the Alexandrian church's structures actually
    were - the modern side of the scope contest.
- source_id: srcALX001
  locus: Clement (the teaching life's own witness)
  author_gravity_note: The teaching tradition attested from inside - independent of the institutional
    frame.
- source_id: srcALX007
  locus: Gregory Thaumaturgus, Address of Thanksgiving
  author_gravity_note: The student-side account of the accompaniment mode - what the 'school' was as lived.
field_relations:
- type: associated-with
  target_id: alexlex029
  note: 'CO-P2-15: the governed contest this term carries is surfaced at the partner term (Doc_06 SS3''s
    CT-surfacing convention). Teacher is where a participant most directly meets this contest.'
- type: associated-with
  target_id: alexlex003
  note: 'CO-P2-15: the governed contest this term carries is surfaced at the partner term (Doc_06 SS3''s
    CT-surfacing convention). Catechesis is Doc_06 SS3''s named reference point.'
contested_claim_ids:
- alexclaim004
---
CO-P2-15 (Mark, 2026-07-28) - governed-CT term record authored (the CO-P2-03 Alexandria application): Doc_06 SS2's authority table is the contest source (verbatim-adjacent); the S2.6 claim records carry the contest analysis; world_meaning/voice_surface authored from-inside per the built terms' register; prior sense UNVERIFIED-flagged per the S2.3 convention. Tier 2 (this world assigns no Tier 3). No chunk file exists yet - the chunk view generates one at swap time. See wrs/migrate/s62_alx_s29_co15.py.

[Verification State Re-grade (2026-08-05, Rigor P1-1 fix)]: `verification_state` corrected from the fleet-wide default `verified-via-authority` to `named-not-rechecked`: all 4 linked source(s) show discovery_channel=builder-prior-knowledge (named from the builder's own prior knowledge, not independently investigated this session).
