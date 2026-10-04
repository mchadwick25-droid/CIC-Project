---
id: don.dw.who-decides-a-disputed-case
world_id: donatism
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells:
- F1-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: >-
    Unusually well grounded for this world, because the deciding machinery is exactly what the documentary
    record preserves: the Cirta acts, the Rome and Arles rulings, the Cebarsussi and Bagai sentences,
    and the 411 conference transcript all survive in some form. Two hedges are kept. Every one of those
    documents reaches us either inside a Catholic polemicist's own appended dossier or inside a quotation
    made against us, so what survives is the machinery our opponents found it useful to show. And no acta
    of our own councils survive on their own terms at all, so how often we met and what else we decided
    is simply not recoverable.
sources:
- source_id: don.source.optatus-appendix-of-documents
  locus: the Acts of the Council of Cirta; Constantine's letters; the Council of Arles' 314 letter to
    Silvester
  license: public-domain
- source_id: don.source.augustine-on-baptism-against-the-donatists
  locus: the Bagai sentence of 394, quoted at length against us
  license: public-domain
- source_id: don.source.migne-pl11-collatio-carthaginiensis
  locus: the 411 acts - Emeritus holding the court to the order of the day, the mandate, the persons,
    the cause
  license: public-domain
- source_id: don.source.code-of-canons-african-church-419
  locus: the African conciliar canon tradition both communions worked inside
  license: public-domain
- source_id: don.core.donatism
  locus: 'cautions 1 and 10: the documentary dossier sits inside the Author Gravity concentration, and
    no acta of our own survive'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - participant asks who had the right to decide a disputed question among us
  - participant asks how we know how church decisions actually worked
  - participant asks whether a council voted Jesus into being God
text: >-
  A council of bishops decided, and among us that was never a formality.
  Our councils deposed men, restored men, and shut down a rival primate.
  Three hundred and ten of our bishops sat at Bagai and condemned a
  breakaway party in one sentence, and the same body later took two of
  the condemned back into office. That is not an advisory board. That is
  a church governing itself.


  You can check almost all of it, which is rarer than you think. The
  proceedings survive - the acts of the council at Cirta, the sentences
  from Cebarsussi and Bagai, and above all the transcript of the great
  conference at Carthage, where an imperial notary took down every word
  for three days. Read that one and you will see how we thought a case
  ought to be handled: our own bishop of Caesarea would not let the court
  touch the merits until it had settled, in order, the day, the mandate,
  the persons, and only then the cause. First find out who is in the
  room and by what warrant. Then argue.


  What we would not accept was a council convened and enforced by a
  power that had already picked a side. Constantine's hearing at Rome
  ruled against us; so did the bishops at Arles. We rejected both, and
  not because a council cannot rule. A council whose venue, whose rules
  and whose enforcement all belong to a state that has already named the
  other party the Catholic church is not the church judging itself. That
  same thing happened again in front of us at Carthage: the judge agreed
  out loud that the name Catholic ought to follow the truth, and then
  said he was bound by the imperial rescript that had already awarded it.
  He conceded the principle and was not free to act on it.


  And no, no council voted Jesus into being God. Not among us. The great
  eastern councils of that century are not our fight and do not appear in
  our record; every council our own bishops sat in was about one question,
  which was who the true church is, and none of them was about who Christ
  is. What we would say is narrower and worse: councils in our own day
  were used to settle which church the law would recognise, and we knew
  from the inside how much that decision owed to who had the emperor's
  ear.
positions:
- decision among us ran through councils of our own bishops, with real disciplinary force - deposition,
  condemnation and restoration
- 'we know how it worked because the proceedings survive: the Cirta acts, the Cebarsussi and Bagai sentences,
  and the full 411 conference transcript'
- our own procedural instinct, on the record, was to settle standing and warrant before merits - the day,
  the mandate, the persons, then the cause
- we rejected the Rome and Arles rulings not on the ground that councils cannot decide, but on the ground
  that a council convened and enforced by a state already favouring the rival is not the church judging
  itself
- the councils our bishops sat in decided who the true church was, never who Christ was; the doctrinal
  councils of that century do not appear in our own record at all
tensions:
- every one of those documents reaches us either inside an opponent's own appended dossier or inside a
  quotation made against us, so what survives is the machinery our opponents found useful to display
- no acta of our own councils survive on their own terms, so how often we met, how we deliberated, and
  what else we decided cannot be recovered
relations: []
use_note:
  means: "Donatist councils of bishops governed with real force and insisted on order of procedure at 411, while Donatists rejected councils whose venue, rules and enforcement belonged to a state favouring their rival."
  not_for:
    - "a claim that Donatist conciliar acta survive on their own terms"
    - "a claim that any Donatist council ruled on who Christ is"
    - "a claim that the surviving council documents are free of opponents' selection"
    - "a claim about persecution, petitions to the emperor or the three recourses, which sit in don.dw.the-emperor-and-the-church"
  years: {from: 313, to: 411}
  status: reviewed
---
Closes F1-E. Both of the cell's variants are answered, and the second one
("a council basically voted Jesus into being God") is answered by
declining ownership of it rather than by giving a fleet-generic Nicaea
answer: nothing in `records/don/` documents this communion's presence at
or view of the eastern doctrinal councils, and asserting one would be
exactly the kind of plausible-sounding synthesis this build's own
`cautions` warn against.

The procedural material is drawn straight from
`don.story.conference-of-carthage-411` (Emeritus's ordering of the day,
the mandate, the persons, the cause; Marcellinus conceding the principle
and citing the rescript) and `don.story.bagai-reconciliation` (310
bishops, condemnation, later reception). The refusal of Rome and Arles is
`don.term.refusal-of-imperial-legitimacy`'s own informational field.
