---
id: don.quote.conscience-of-the-giver
world_id: donatism
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- C-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Verified word for word against the vendored NPNF volume, where the clause is printed as the quoted
    proposition of Petilian standing at the head of a chapter with Augustine's reply beneath it. Two things
    must travel with it. It survives ONLY inside the book written to demolish it - there is no independent
    manuscript of Petilian - so what is verified is that Augustine quoted him in these words, repeatedly
    and consistently, not that no wording was lost before it reached him. And Augustine's own text records
    a variant reading in which Petilian wrote "the conscience of him who gives IN HOLINESS," a phrase Augustine
    insists on and argues from; that variant is preserved in the modern_lens_note rather than silently
    dropped, because Augustine's own argument turns on it.
sources:
- source_id: don.source.augustine-answer-to-petilian
  locus: Book II, ch. 3, SS6 - "Petilianus said" (npnf104_augustine-anti-manichaean-anti-donatist.xml,
    div4 v.v.iv.iii)
  license: public-domain
- source_id: don.source.petilian-of-constantina-letters
  locus: the letter to his own clergy, surviving only as clauses inside the refutation
  license: public-domain
text: >-
  For what we look to is the conscience of the giver, to cleanse that of
  the recipient.
speaker_or_author: don.figure.petilian
license: verbatim
modern_lens_note: >-
  Read flat, this sounds like a rule about a priest needing to be a good
  person - a demand for personal holiness at the altar. It is not that.
  "Conscience" here (conscientia) means a man's standing and history:
  specifically, whether he or the bishop who ordained him handed the
  scriptures over during the persecution. The claim is about a broken
  chain of ordination, not about private sin. A modern reader should also
  notice what the clause does NOT say: nothing about the worthiness of
  the person being baptized. The scrutiny falls entirely on the minister.
  Two further cautions. This clause survives only because the man
  refuting it quoted it, clause by clause, and no independent copy of
  Petilian exists. And the same refutation preserves a longer reading -
  "the conscience of him who gives IN HOLINESS" - which Augustine
  insists on and builds his counter-argument around; the shorter form
  above is the one he quotes most often and heads the chapter with, but
  the variant is real and is part of the record.
retrieval:
  tier: 1
  retrieve_when:
  - participant asks what actually made a sacrament valid or invalid among us
  - participant asks whether their own past would have counted against them
  - participant asks for our own words rather than what our opponents said about us
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: don.dw.walking-to-one-font
- type: associated-with
  target: don.dw.becoming-one-of-us
modern_rendering: >-
  What we look at is the conscience of the one who gives, so that it can
  wash the one who takes.
---
Verified verbatim against the vendored
`npnf104_augustine-anti-manichaean-anti-donatist.xml`, at the chapter
head where the text reads: "Chapter 3.-6. Petilianus said: 'For what we
look to is the conscience of the giver, to cleanse that of the
recipient.'" No wording added, dropped, or reordered. The same clause
recurs at several further points in the volume in slightly varied
translation ("What we look for is the conscience of the giver, to cleanse
that of the recipient"), and the form above is the one printed as
Petilian's own quoted proposition rather than as Augustine's later
paraphrase of it.

The Latin is printed in the same volume's Prolegomena as "Conscientia
namque (sancte) dantis attenditur, quae (qui) abluat accipientis" - the
parenthesised words being the variant reading the `modern_lens_note`
carries.

Register `emic`: Petilian is this communion's own bishop of Constantina,
not an outside voice, which is why this is not handled the way
`cappadocian.quote.julian-galilaeans` handles a hostile outsider. What
travels with the emic register here is the transmission warning, not a
change of voice: `don.figure.petilian`'s own bridge line already names
him as the man "whose letters survive only inside the book written to
demolish them."

MODERN RENDERING AUTHORED, matching the standing fleet discipline: the
spoken form is modern English, never the archaic original, which stays in
`text` for Level 3.
