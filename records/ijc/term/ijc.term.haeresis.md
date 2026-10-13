---
id: ijc.term.haeresis
world_id: imperial-juridical
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-P
- F1-I
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: ijc.source.sozomen-he
  locus: "VII.4 (the 380 law's heretic clause, npnf202 line 40625)"
  license: public-domain
- source_id: ijc.source.canons-nicaea
  locus: the Creed's anathemas
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - how a teaching came to be legally excluded
  - the relationship between imperial law and doctrinal boundary-drawing
  prefer_instead:
  - the question is really about a specific confession's own content (homoios instead)
relations:
- {type: associated-with, target: ijc.term.homoios}
- {type: associated-with, target: ijc.term.communio}
- {type: associated-with, target: ijc.term.concilium}
plain_meaning: "Heresy as we wielded it: a teaching placed outside what the church would recognize and, more and more, outside the law itself. Faith and law were joined in the one judgment."
world_word: haeresis
distortion_risk: high
false_friend:
- a purely doctrinal category with no legal consequence
- a boundary that always pointed the same direction (under Homoian emperors it pointed at the Nicenes)
senses:
  informational: 'A teaching becomes haeresis when the church gathered declares it so - and, from Theodosius
    onward, when imperial law gives the declaration force: the Thessalonica law reserved the very name
    "Catholic Church" to one confession and handed the rest the name of heretics, with consequences.'
  evidential: 'The creed''s anathemas show the church''s own half of the act from 325; the historians preserve
    the law''s half, including its wording. The record also shows the category''s direction reversing:
    the machinery that condemned the Homoian confession had, under other emperors, enforced it.'
  personal: "The weight fell first on office-holders. They were deposed, exiled, or found their see declared empty. The record shows this machinery from the side of those who used it and those it removed."
  translational: "\"Heresy-hunting\" here was a state process, and private zeal was only part of it. Whether it became settled legal machinery all at once or slowly across this window is a live scholarly question. We hold it open."
quick_meaning: A teaching ruled outside the church - and, under our laws, outside legal standing too.
use_note:
  means: "Heresy is a teaching placed outside what the church would recognize and, increasingly, outside the law: one act, a judgment of faith with legal force."
  not_for:
    - "a claim that heresy was a purely doctrinal category with no legal consequence"
    - "a claim that the boundary of heresy always pointed the same direction"
  years: {from: 312, to: 451}
  status: reviewed
---
Rebuilt from the reviewed legacy lexicon (Doc_06 Tier 2;
Lexicon-Chunks/ijclex008_haeresis.md). The legacy chunk's Key Source
was the Theodosian Code directly; no PD English of the Code is
vendorable (ijc.search.theodosian-code-english), so this record anchors
the legal half on Sozomen's report of the law's content - the honest
citation path. The CT (Historical scope) contest - settled category
from Nicaea vs. gradual legal construction - is carried in the
translational sense; Hanson (1988) is the referenced scholarship.
canon_cells: F3-P (your church used power against Christians who
disagreed - defend that: this term is that question's factual ground),
F1-I (what you argued about).
