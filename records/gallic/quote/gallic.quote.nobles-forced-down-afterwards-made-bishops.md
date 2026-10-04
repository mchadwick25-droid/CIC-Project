---
id: gallic.quote.nobles-forced-down-afterwards-made-bishops
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as Sulpitius's own text (Vita Martini ch. X, read at its locus for this record) -
    his own narration of Marmoutier's noble-born disciples and, in the same sentence, his own
    aside that many of them went on to become bishops.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "ch. X (npnf211 div ii.ii.xi, file line 1153): the nobles who took up this humility, and
    Sulpitius's own note that many of them were afterwards made bishops"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks whether Marmoutier's monks became bishops, and in Sulpitius's own words"
  - "participant asks about noble-born disciples at Marmoutier"
  prefer_instead:
  - "participant wants the same claim from the wider passage about cities wanting priests from Martin's monastery - that sentence is carried in this host record's own manifestations"
text: >-
  These, though far differently brought up, had forced themselves down
  to this degree of humility and patient endurance, and we have seen
  numbers of these afterwards made bishops.
speaker_or_author: gallic.figure.sulpitius
license: verbatim
modern_lens_note: >-
  "These" refers back to the noble-born disciples Sulpitius has just described - men used to a
  softer life who took up the same plain dress and discipline as everyone else at Marmoutier. In the
  same sentence, without a pause, Sulpitius adds that he has personally seen many of them go on to
  become bishops - the two facts sit together as one observation, not two separate claims.
modern_rendering: >-
  These men had been raised in a very different way. Even so, they had forced themselves down to
  this level of humility and patient endurance. And we have seen many of them made bishops
  afterwards.
relations:
- type: associated-with
  target: gallic.force.army-and-rank-before
- type: associated-with
  target: gallic.gravity.monk-bishop
use_note:
  means: "Sulpitius records that noble-born disciples at Martin's monastery took up humble discipline and that he had seen many of them later made bishops."
  not_for:
    - "a count or list of bishops drawn from Martin's monastery, which the record does not give"
    - "evidence that most Gallic bishops were monks"
    - "Martin's own conduct as bishop, which sits in gallic.quote.martin-kept-the-virtues-of-a-monk"
  years: {from: 397, to: 397}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"deemed of noble"` returns line 1153; read with `sed -n '1148,1157p'`, inside `<div3 title="Chapter
X..." ... id="ii.ii.xi">`. The quoted span is one complete sentence, "These, though far differently
brought up..." through "...afterwards made bishops.", ending at its own period; "These" refers to
"many among them...such as are deemed of noble rank" in the immediately preceding sentence, not
supplied from outside this span.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
