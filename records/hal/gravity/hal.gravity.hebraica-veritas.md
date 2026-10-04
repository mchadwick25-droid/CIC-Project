---
id: hal.gravity.hebraica-veritas
world_id: hieronymian-ascetic-literary
record_type: gravity
schema_version: 2
status: ready
register: emic
canon_cells:
- F2-I
- F2-E
- F2-T
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: hal.source.vulgate-prefaces
  locus: passim (the principle argued book by book)
  license: public-domain
- source_id: hal.source.jerome-augustine-letters
  locus: Ep. 112 (the defense under contest)
  license: public-domain
- source_id: hal.source.augustine-letters
  locus: Epp. 71, 82 (the contest in the other hand)
  license: public-domain
relations:
- type: associated-with
  target: hal.gravity.patronage-authority
- type: associated-with
  target: hal.gravity.epistolary-formation
- type: associated-with
  target: hal.gravity.marcella-authority
- type: associated-with
  target: hal.gravity.controversy-pressure
- type: enabled-by
  target: hal.force.jerome-arrival
- type: associated-with
  target: hal.force.augustine-dispute
- type: associated-with
  target: hal.force.transmission-ongoing
- type: associated-with
  target: hal.force.transmission-ending
- type: associated-with
  target: hal.term.hebraica-veritas
- type: illustrated-by
  target: hal.story.translating-a-book
- type: illustrated-by
  target: hal.story.ciceronian-dream
- type: tension-with
  target: hal.quote.no-one-preferred-to-the-seventy
name: Hebraica veritas - Hebrew-based textual authority [PRIMARY]
description: 'The conviction that the Hebrew text of scripture carries the truth closest to its inspired
  origin, held and practiced as a formation commitment: the whole translation project, the years
  of Hebrew study, and the running public defense of both. CLASSIFICATION BASIS: Primary on the attestation-level
  evidence (the translation artifact exists; the dispute is independently attested in Augustine''s
  own hand); the separate Contested question of Jerome''s actual Hebrew fluency does not lower the
  gravity''s organizing strength and is carried as its own contest, not dissolved.'
manifestations:
- the translation project itself, from the Damasus-commissioned Gospels revision to the Hebrew Old
  Testament rendered book by book at Bethlehem
- the praefatio practice - each book defended on arrival against live objection
- the Augustine correspondence and the Oea congregation's revolt over one changed word
- Hebrew study under Jewish teachers, paid for by Paula's patronage
classification: primary
use_note:
  means: "Hebrew-based textual authority organized the translation project and its running defense, and the separate contest over Jerome's fluency leaves its organizing strength intact."
  not_for:
    - "asserting Jerome's maximal Hebrew fluency as settled"
    - "presenting the principle as uncontested in its own time"
    - "treating a primary gravity as a settled consensus"
  years: {from: 382, to: 420}
  status: provisional
---
Re-derived from the cleared Doc_04 (G1: passes all six tests; bipolar
geography holds - Rome origin and dispute-network, Bethlehem the sustained
work). The Confidence/Gravity Cross-Check divergence is carried explicitly:
attestation-level confidence (Widely-Accepted-to-Documented) is what
Primary status rests on; content-level confidence on Jerome's Hebrew
mastery is separately Contested (hal.contested.hebrew-fluency) - flagged,
not resolved by upgrading. Forces-connection (Doc_08 synthesis):
intensified under the Augustine dispute (2A-2); transformed at 3B-2 (loses
its real-time defense mechanism when its sole practitioner dies).
Canon_cells assigned at authoring: the record's content directly grounds
F2-I (how they read), F2-E (how the record holds up - the contest itself),
F2-T (which Bible / whose authority).
