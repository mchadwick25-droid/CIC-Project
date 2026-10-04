---
id: gallic.limit.no-one-who-saw-him
world_id: gallic-monastic-ascetic-christianity
record_type: honest_limit
schema_version: 2
status: ready
register: emic
canon_cells:
- C-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented that the gap exists: this world's whole read corpus is monastic formation
    literature, one saint's Life with its letters and dialogues, and a remembrancer on doctrine -
    none of it apologetic, none of it argues the resurrection to a doubter, and none of it claims
    any link to an eyewitness across the three centuries and more between the Lord's days and this
    world's floor. The positive things the statement says first (the two lessons at the office; the
    Gospel one body in four; the canon complete and sufficient, needing the Church's understanding)
    were each read at their own lines for this record. The one unread candidate that might bear on
    the cell - Cassian's seven books against Nestorius - is a coverage limit stated, not filled.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "II.6 (npnf211 div iv.iii.ii.iv, file lines 17119-17120): 'two lessons follow, one from the Old and the other from the New Testament'; III.3 (lines 17896-17913): the Gospel 'divided by the fourfold narrative of the Evangelists ... yet the body of the Gospel is but one'; 'His soul was not left in hell'; 'I lay it down of Myself ... and I have power to take it again'"
  license: public-domain
- source_id: gallic.source.vincent-commonitory
  locus: "ch. 2 [5] (div iii.iii, file lines 12169-12176): 'the canon of Scripture is complete, and sufficient of itself for everything, and more than sufficient'; yet 'owing to the depth of Holy Scripture, all do not accept it in one and the same sense'"
  license: public-domain
- source_id: gallic.story.the-cloak-at-amiens
  locus: "the Lord seen in a soldier's dream, wearing the half of a cloak - what this world had of him in place of anyone who saw him"
  license: public-domain
- source_id: gallic.story.raising-of-the-catechumen
  locus: "a dead man breathing at the saint's prayer - the power present, not a proof of the Lord's rising"
  license: public-domain
- source_id: gallic.source.cassian-de-incarnatione
  locus: "present in the vendored volume and unread by this build - a coverage limit, stated"
  license: public-domain
statement: >-
  What did we have of Jesus? The books, read at the hours. After the
  psalms come two lessons, one from the old books and one from the new.
  Four men tell the Gospel, Cassian says, but the Gospel is one body. And
  Vincent held that the canon of Scripture is complete and more than
  enough, and that it still needs the Church's own understanding, because
  each man reads it his own way. Had any of us known someone who saw him?
  No. More than three hundred years lay between his days and ours. No one
  in our record claims it. What we had instead was the saints. The Lord
  was seen once in a soldier's dream at a city gate, wearing the half of a
  cloak. How do we know the resurrection really happened? We did not ask
  it that way. We confessed it at the hours: his soul was not left in
  hell; no one took his life from him, he laid it down himself and took it
  again. We saw a dead man breathe at the saint's prayer. But a proof that
  the Lord rose, written by one of us for someone who doubts it - that is
  not in our record.
why_sources_cannot_answer: >-
  This world's own read corpus contains no apologetic writing at all. The
  Institutes and Conferences are formation literature carrying Egypt's
  teaching to Gallic cells; Sulpitius's Life, Letters, and Dialogues are
  hagiography and its defence; the Commonitory is a rule for telling
  received faith from novelty. None argues the resurrection to a doubter,
  and none names any chain of witnesses back to the apostolic age - the
  world's floor (c. 360) stands more than three centuries after the
  events, and its own texts never claim otherwise. The cell's evidentiary
  questions (who saw him; how do you know) are therefore unanswerable
  from this world's own voice, and the nearest material is of a different
  kind: Scripture read at the office (gallic.source.cassian-institutes
  II.6, III.3), the canon-plus-interpretation rule
  (gallic.source.vincent-commonitory ch. 2), and Christ seen in vision
  (gallic.story.the-cloak-at-amiens) - confession and practice, not
  evidence. The one unread work that might bear on it, Cassian's seven
  books against Nestorius (gallic.source.cassian-de-incarnatione), is a
  Christological polemic, not an apologetic for the resurrection, and its
  content is a stated coverage limit this record does not fill.
nearest_material:
- gallic.dw.the-christ-who-bears-the-wounds
- gallic.story.the-cloak-at-amiens
- gallic.story.raising-of-the-catechumen
- gallic.term.tradition
- gallic.term.the-deposit
- gallic.term.theotocos
- gallic.source.cassian-de-incarnatione
relations: []
use_note:
  means: "The record attests that this world's books never claim a witness to the Lord and never argue the resurrection to a doubter, and it cannot supply either."
  not_for:
    - "a proof of the resurrection written by this world for a doubter, which the record says is absent"
    - "the cloak vision or the raised catechumen as evidence that the Lord rose, when they show the saint's power, as in gallic.story.the-cloak-at-amiens and gallic.story.raising-of-the-catechumen"
    - "the content of Cassian's seven books against Nestorius, which is unread"
    - "a chain of witnesses, when the world's floor stands more than three centuries after the events"
  years: {from: 397, to: 434}
  status: reviewed
---
Closes C-E at the Answer-the-Canon step (inserted between B-7 and B-8)
as a genuine, declared absence rather than a strained dw. The cell's
three canon questions are evidentiary - what did you have, who had known
a witness, how do you know the resurrection happened - and the honest
shape here follows desert.limit.doubt-and-doctrine's corrected
discipline: say the positive thing first (what we did have of him: the
lessons, the one Gospel in four, the canon and its rule), then name the
silence exactly where it bears (no eyewitness chain; no argument for
the resurrection written for a doubter), without a sentence whose
subject is the voice's own declining. The resurrection confession this
world did hold is carried substantively in
gallic.dw.the-christ-who-bears-the-wounds (C-I), which this record
points to first in nearest_material; the two cells are kept distinct by
register - C-I asks what we believed, C-E asks how we knew.

Loci read at their own lines in
cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml for this
record: Inst. II.6 lines 17119-17120; Inst. III.3 lines 17896-17913 (the
Gospel "but one" at 17898-17899; "His soul was not left in hell" at
17906; "I lay it down of Myself" at 17912); Comm. 2 [5] lines
12169-12176. Statement register measured with engine/m1/fk.py before
commit (see gate battery).
