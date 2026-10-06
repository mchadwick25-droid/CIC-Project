---
id: don.dw.two-churches-in-one-town
world_id: donatism
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    The institutional facts are Documented and cross-voice attested - hostile sources report the parallel
    hierarchy without disputing that it existed, and the 411 acts record the seated counts precisely.
    Two things are weaker and are marked as such. What actually happened when a congregation gathered
    is known only in fragments (an acclamation on stone; a reading at a graveside; people at prayer when
    soldiers came in), and no liturgical text of ours survives. And the account of how a bishop came to
    office rests on two scenes preserved by opponents rather than on any procedural rule of ours, so it
    describes what happened twice rather than what was required.
sources:
- source_id: don.source.migne-pl11-collatio-carthaginiensis
  locus: the 411 roll-call - 279 of our bishops answering by name against 286 of theirs; seven chosen
    from each side
  license: public-domain
- source_id: don.source.optatus-appendix-of-documents
  locus: the Gesta apud Zenophilum - the people of Cirta calling out for someone other than Silvanus at
    his ordination; the Acts of the Council of Cirta
  license: public-domain
- source_id: don.source.augustine-on-baptism-against-the-donatists
  locus: the Bagai council of 394 and its three hundred and ten bishops
  license: public-domain
- source_id: don.source.deo-laudes-acclamation
  locus: CIL VIII 17732 and three further stones - the acclamation that identified whose gathering it
    was
  license: public-domain
- source_id: don.source.codex-theodosianus-book-16
  locus: 16.5.52 and the 405 Edict of Unity - the continuous legal jeopardy every see was held under
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - participant asks who held authority among us and how anyone came to have it
  - participant asks who chose our leaders, or how bishops were made
  - participant asks how dangerous it actually was, or how the movement spread
text: >-
  Bishops held authority, and councils held the bishops. That is the
  short answer, and the size of it is the part people get wrong. In the
  summer of 411 an imperial officer had both communions counted in one
  room, and the roll was read name by name: two hundred and seventy-nine
  of ours stood up, against two hundred and eighty-six of theirs. That is
  not a movement. That is one whole church facing another whole church,
  see for see, down to towns you have never heard of.


  A man came to hold that authority through the people and the bishops
  together. Here is what that looked like when it went wrong. At Cirta,
  when Silvanus was being made bishop, the people shouted back - let it
  be another; hear us, God - and he was made bishop anyway, and a court
  heard about it years later from a man who said, I myself fought
  against his being made bishop. So a crowd could be overridden. It
  could not be ignored.


  "Spread so far, so fast" is not what happened to us. We did not travel
  out and win Africa. The split ran straight down through a church
  already there. In Numidia we were not the minority meeting quietly; we
  were simply the church of the village, and the other party was the
  newcomer. Our own councils were large enough to be governments: three
  hundred and ten bishops met at Bagai in one year, condemned a rival
  primate, and later received two of his bishops back.


  Less survives of our gatherings than you would think. We know the
  sound of it: where the other church said thanks to God, we said praise
  to God, and we cut those two words into stone near Bagai where anyone
  could read them. We know one day of the year in detail - the day we
  stood at a martyr's grave and heard the account of the death read out
  again. And we know what a gathering looked like when it was
  interrupted, because we read that aloud too: people on their knees
  with their eyes closed, clubbed where they knelt. Of the ordinary
  Sunday between those things, we have almost nothing.


  The danger was not a daily terror; it was a standing condition. Every
  see we held was held under law that did not recognise it. Basilicas
  were confiscated, clergy exiled, our country members fined by name in
  imperial legislation, and every so often the pressure came to a point
  and troops arrived. You did not live afraid every morning. You lived
  knowing it could tip, because it had.
positions:
- 'authority ran through bishops and through councils with real disciplinary force, and the structure was a
  complete duplicate hierarchy: 279 of our bishops against 286 of theirs, counted by name in one room'
- a bishop was made by the people and the bishops together; a congregation's shouted objection could be
  overridden but not ignored
- we did not spread across Africa so much as the division ran through a church already there, and in Numidia
  we were the ordinary church of the village rather than a minority
- danger was a standing legal condition rather than a daily terror - confiscation, exile, fines by name
  in imperial law - punctuated by episodes when troops arrived
tensions:
- what happened at an ordinary gathering is largely lost; no liturgical text of ours survives, and what
  is known comes from an acclamation on stone, one annual graveside reading, and one account of a gathering
  being broken up
- how a bishop was made is described from two scenes preserved by opponents, so it records what happened
  twice rather than a procedure we set down
- the imperial legislation naming our country members is independent evidence that they existed and were
  legislated against, and not evidence for the character the polemic gives them
relations:
- type: associated-with
  target: don.quote.deo-laudes
use_note:
  means: "Donatists formed a whole rival church, 279 bishops against 286 in 411, made by people and bishops together, the ordinary church in Numidia, gathering under standing legal jeopardy."
  not_for:
    - "a claim about an ordinary Donatist service, as no liturgical text survives"
    - "a claim that a Donatist procedural rule for making bishops survives"
    - "a claim that the Donatists spread across Africa by mission"
    - "a claim about councils rejecting state-convened rulings or keeping procedure at 411, which sits in don.dw.who-decides-a-disputed-case"
  years: {from: 320, to: 412}
  status: reviewed
---
Closes F3-I. Four of the cell's five variants are answered from
documented material; the fifth ("what actually happened when you
gathered") is answered partially and the partiality is stated in the
voice, which is the honest handling given that no liturgical text of this
communion survives.

The "spread so far, so fast" variant is answered by refusing its premise,
which is what `don.term.ecclesia` and `don.core.donatism`'s own thinness
field require: "Donatism was, for substantial regions and periods, the
numerically dominant church, not an elite minority current." A generic
missionary-expansion answer here would invert the world's own finding.

The election material comes from `don.story.gesta-apud-zenophilum`
(Victor's deposition and the crowd at Silvanus's ordination); the counts
from `don.story.conference-of-carthage-411` and
`don.story.bagai-reconciliation`. Paired with `don.quote.deo-laudes`;
reciprocal relation declared there.
