---
id: gallic.quote.antiquity-and-the-fathers-unanimous-decision
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
    Documented as Cassian's own statement in the Institutes (I.2), stating the reception criterion he
    applies to monastic custom directly.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes I.2 (npnf211 div iv.iii.i.ii, file lines 16667-16671): the rule for what allegiance is owed, on the question of the monk's dress"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks why this world valued old custom over new practice"
  - "participant asks what made a monastic rule legitimate to Cassian"
  - "participant asks about the difference between a few men's preference and the fathers' own tradition"
  prefer_instead:
  - "participant asks about a specific item of dress or custom this rule is applied to - this record carries the general principle, stated on the occasion of the monk's robe"
text: >-
  For we ought to give unhesitating allegiance and unquestioning
  obedience, not to those customs and rules which the will of a few
  have introduced, but to those which a long standing antiquity and
  numbers of the holy fathers have passed on by an unanimous decision
  to those that come after.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  Cassian states this as a general principle, but the occasion is a small, concrete question - what a
  monk should wear. That is itself part of the point: for Cassian, even a detail this minor cannot be
  decided by present taste, only by what long tradition and the consensus of the fathers has already
  settled.
modern_rendering: >-
  For we ought to give unhesitating loyalty and unquestioning obedience.
  We owe it not to the customs and rules that a few people have brought
  in by their own will. We owe it to those that long antiquity and many
  holy fathers have passed on, by one shared decision, to those who come
  after.
relations:
- type: associated-with
  target: gallic.gravity.received-not-invented
use_note:
  means: "Cassian lays down in Institutes I.2, on the monk's dress, that allegiance belongs to customs passed on by antiquity and the fathers' unanimous decision, not by a few."
  not_for:
    - "a separate witness from gallic.quote.allegiance-to-antiquity-not-a-few, which carries the identical sentence"
    - "a rule Cassian applies only to clothing"
    - "a conciliar or episcopal rule, when it is a monastic writer's criterion for custom"
  years: {from: 415, to: 426}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"unhesitating allegiance"` returns one hit, line 16668, inside `<div4 title="Chapter II. Of the
Monk's Robe." ... id="iv.iii.i.ii">`. The sentence runs lines 16667-16671: "For we ought to give
unhesitating allegiance and unquestioning obedience, not to those customs and rules which the will of
a few have introduced, but to those which a long standing antiquity and numbers of the holy fathers
have passed on by an unanimous decision to those that come after."

Normalization: line breaks joined with single spaces. No word added, dropped, substituted, or
reordered.
