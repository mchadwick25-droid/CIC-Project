---
id: ijc.term.concilium
world_id: imperial-juridical
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-I
- F1-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: ijc.source.canons-nicaea
  locus: creed and canons
  license: public-domain
- source_id: ijc.source.canons-constantinople-381
  locus: canons
  license: public-domain
- source_id: ijc.source.chalcedon-acts
  locus: Definition, canons, session extracts
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - how doctrinal disputes were actually resolved
  - a specific council (Nicaea, Constantinople, Ephesus, Chalcedon)
  prefer_instead:
  - the question concerns one council's specific doctrinal content rather than the conciliar mechanism itself
relations:
- {type: associated-with, target: ijc.term.primatus}
- {type: associated-with, target: ijc.term.presbeia}
- {type: associated-with, target: ijc.term.haeresis}
- {type: associated-with, target: ijc.term.tomus}
plain_meaning: 'A council: bishops gathered, most often at the emperor''s summons, to argue, vote, and issue rules
  meant to bind the whole church. Our chief tool for settling disputes. It did not always keep
  them settled.'
world_word: concilium (synodos)
distortion_risk: high
false_friend:
- a modern legislature whose majority vote all parties then accept
- a merely advisory conference with no binding force claimed
senses:
  informational: 'The mechanism replayed across the whole window: Nicaea (325), Constantinople (381),
    Ephesus (431), Chalcedon (451) - hundreds of bishops summoned at imperial expense to one place, arguing
    to a decision meant to bind everyone.'
  evidential: 'The canons and creeds survive as the councils'' own instruments; Chalcedon''s session extracts
    even preserve the arguing. The record also preserves the mechanism failing: the same council that
    settled Christ''s natures produced a canon on rank that Rome refused to receive - a vote taken is
    not, in this world, a question closed.'
  personal: To be summoned was to be caught up in something at the scale of the empire itself - and to
    discover that after the arguing and the vote, whether the decision held still depended on who would
    receive it.
  translational: '"Church councils decided everything by committee?" - the vote was real, but reception
    was a separate act: a council''s authority was itself one of the things the councils kept having to
    contest.'
quick_meaning: A gathering of bishops, called to settle what the whole church must hold.
use_note:
  means: "A council is bishops gathered, usually at the emperor's summons, to argue, vote and issue binding rules; decisions did not always hold."
  not_for:
    - "a claim that a council worked like a modern legislature whose majority vote all parties then accept"
    - "a claim that a council was a merely advisory conference with no binding force claimed"
  years: {from: 325, to: 451}
  status: reviewed
---
Rebuilt from the reviewed legacy lexicon (Doc_06 Tier 2;
Lexicon-Chunks/ijclex007_concilium.md). canon_cells: F1-I (what did the
councils in your time decide, and why did it matter so much - the
direct home question), F1-E (when belief was disputed, who had the
right to decide - the mechanism half of that answer; the reception
caveat is the honest other half).
