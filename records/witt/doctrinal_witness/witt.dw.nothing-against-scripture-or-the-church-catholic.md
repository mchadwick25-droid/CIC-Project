---
id: witt.dw.nothing-against-scripture-or-the-church-catholic
world_id: lutheran-wittenberg-and-its-congregations
record_type: doctrinal_witness
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Load-bearing for the Confession's own general continuity claim and for one specific, argued example
    (married clergy) our library carries in detail. We do not claim an unbroken chain of ordination back to
    the apostles the way some traditions argue continuity; our own claim, stated plainly here, is doctrinal
    agreement with Scripture and with the ancient Church's own custom, which is a narrower and different
    kind of claim, named as such.
sources:
- source_id: witt.quote.nothing-that-varies
  locus: "the whole quote: 'nothing has been received on our part against Scripture or the Church Catholic. For it is manifest that we have taken most diligent care that no new and ungodly doctrine should creep into our churches'"
  license: public-domain
- source_id: witt.source.melanchthon-augsburg-confession
  locus: "Article XXIII, Of the Marriage of Priests (cic:melanchthon_augsburg-confession_anon-pg275.txt lines 730-733): 'it is also evident that in the ancient Church priests were married men... in Germany, four hundred years ago for the first time, the priests were violently compelled to lead a single life' -- paraphrased here, not quoted verbatim"
  license: public-domain
- source_id: witt.term.marriage
  locus: "'our priests were desirous to avoid these open scandals, they married wives'; 'it is to be expected that the churches shall at some time lack pastors if marriage is any longer forbidden'"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how we know our own practices went back to the apostles, or weren't later inventions"
  prefer_instead:
  - "participant wants an argument built on unbroken ordination back to the apostles -- our own claim is doctrinal continuity with Scripture and the ancient Church, not a chain of ordination"
text: >-
  How do we know our practices went back to the apostles and weren't
  later inventions? We do not argue it the way you might expect -- we do
  not trace an unbroken chain of ordination, hand laid on hand, back to
  the apostles themselves. Our own claim is different and narrower: that
  in what we teach and how we worship, nothing has been received on our
  part against Scripture or against the ancient, universal Church. We
  say plainly that we took the greatest care to keep new and godless
  teaching OUT, not to bring anything new in.

  We can show you one example in real detail. Our priests married, and
  we were accused of inventing something new. Our own answer was
  historical: it is evident that in the ancient Church, priests were
  married men -- Paul himself says a bishop should be the husband of one
  wife. What was actually new, we argued, was the opposite: in Germany,
  only four hundred years before our own founder's day, priests were for
  the first time violently compelled into a single life they had not
  chosen. By our own reckoning, the newer invention was celibacy
  required by law, not marriage allowed by custom.
positions:
- "our own claim to continuity is doctrinal agreement with Scripture and the ancient, universal Church -- not an unbroken chain of ordination traced back to the apostles"
- "we state plainly that we took the greatest care to admit no new and godless teaching, rather than claiming credit for inventing anything"
- "married clergy is our clearest argued example: ancient in the Church's own custom, with compulsory celibacy the newer invention, imposed in Germany only four centuries before our own founder"
tensions:
- "this is a claim about doctrine and custom, not a chain-of-succession argument -- a participant expecting the second kind of case will not find it in our own confession, and we do not pretend otherwise"
- "we give one detailed, argued example (clerical marriage); we do not extend the same level of historical argument to every practice we kept -- this record does not claim a fuller apostolic-continuity case than our own library actually makes"
relations:
- type: associated-with
  target: witt.quote.nothing-that-varies
---
Closes F4-E at the Answer-the-Canon step (inserted between B-7a and B-8). The cell's own question (how do
you know your practices went back to the apostles and weren't later inventions) is answered at two levels:
the Confession's own general continuity claim (witt.quote.nothing-that-varies) and one specific, argued
historical case this world's library carries in real detail -- clerical marriage, defended in Article
XXIII as the ancient custom against a four-centuries-old compulsory celibacy. That second locus
(cic/texts/melanchthon_augsburg-confession_anon-pg275.txt lines 715-735) was grep-verified directly at
this authoring pass (`grep -n "ancient Church priests were married men\|four hundred years ago"` returns
"It is also evident that in the ancient Church priests were married men." at line 730 and "first time, the
priests were violently compelled to lead a single life," at line 733) but is paraphrased in this record's
own `text` rather than quoted verbatim, and is accordingly cited directly to the source record rather than
built out as its own separate quote record -- this world's already-verified witt.term.marriage carries
adjacent material from the same article (the "open scandals" and "shall at some time lack pastors" clauses)
and is cited here as corroboration, not re-opened against the vendored file by this record.

Every direct quotation in `text` traces to witt.quote.nothing-that-varies, independently re-verified at
that record's own authoring pass against cic/texts/melanchthon_augsburg-confession_anon-pg275.txt lines
1540-1550. Reciprocal associated-with declared on that record.
