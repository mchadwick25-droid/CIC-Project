---
id: gallic.quote.gennadius-martin-famous-for-signs
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
voice: analytic
register: etic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted as Gennadius's own later description (De Viris Illustribus ch. XIX, read at its
    locus for this record) of Martin's own fame - independent ancient testimony that Martin was
    known for wonders, not a claim this record independently verifies.
sources:
- source_id: gallic.source.gennadius-de-viris-illustribus
  locus: "ch. XIX (npnf203 div v.iv.xx, file lines 42539-42547): Gennadius's description of
    Sulpitius's Life of St. Martin, and of Martin's own fame"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks how Martin was remembered outside Sulpitius's own circle"
  - "participant wants independent ancient confirmation of Martin's reputation for wonders"
  prefer_instead:
  - "participant wants Gennadius's own description of the Dialogues specifically - retrieve gallic.quote.gennadius-on-the-dialogues-subject"
text: >-
  He composed also a Chronicle, and wrote also to the profit of many, a
  Life of the holy Martin, monk and bishop, a man famous for signs and
  wonders and virtues.
speaker_or_author: Gennadius of Marseilles, De Viris Illustribus
license: verbatim
modern_lens_note: >-
  Gennadius is describing Sulpitius's book, not Martin directly - but the phrase he reaches for to
  characterize Martin himself, independently of Sulpitius's own claims, is "famous for signs and
  wonders and virtues." That fame, not just the book that carried it, is what an outside witness
  attests.
modern_rendering: >-
  He also wrote a Chronicle. For the benefit of many, he also wrote a Life of the holy Martin, monk
  and bishop. Martin was a man famous for signs and wonders and miracles.
relations:
- type: associated-with
  target: gallic.gravity.virtus
---
Verified directly against cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml. `grep -n "famous
for signs and wonders"` returns line 42547; read with `sed -n '42538,42548p'`, inside `<div3
type="Chapter" title="Severus the presbyter." ... id="v.iv.xx">` (the body text's own visible
chapter number, "Chapter XIX.", is a separate heading span inside this div, not the div's own
title attribute). The quoted span is one complete sentence, "He composed also a Chronicle..."
through "...famous for signs and wonders and virtues.", ending at its own period, and sits in the
source immediately before the sentence gallic.quote.gennadius-on-the-dialogues-subject carries ("He
also wrote a Conference between Postumianus and Gallus...") - a distinct sentence about Martin's
own fame, not the Dialogues' subject, so carried as its own record rather than extending that one.

Normalization: line breaks joined with single spaces; a translator's endnote on "virtues" ("Virtues
or miracles") falls right after the sentence's own closing period and is apparatus, excluded per
the fleet's own `<note>`-stripping convention; the source's own italic markup around "Chronicle" and
"Life of the holy Martin" was dropped, the same normalization the fleet applies elsewhere to
italicized titles. No word was added, dropped, substituted, or reordered.

speaker_or_author is a plain string: no gallic.figure record exists for Gennadius.
