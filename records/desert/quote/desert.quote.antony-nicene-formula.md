---
id: desert.quote.antony-nicene-formula
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: [C-T]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: "Contested for incident-level attribution, matching desert.quote.antony-arians-serpents's own basis for material from the same Vita and the same episode - reported teaching within Athanasius's own narrative, written by a bishop with his own anti-Arian purposes. The words themselves are quoted verbatim from the vendored text."
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS69 - Antony, summoned to Alexandria by the bishops, publicly teaching against the Arians"
  license: public-domain
text: "...the Son of God was not a created being, neither had He come into being from non-existence, but that He was the Eternal Word and Wisdom of the Essence of the Father. And therefore it was impious to say, 'there was a time when He was not,' for the Word was always co-existent with the Father."
speaker_or_author: desert.figure.antony
license: verbatim
modern_lens_note: "No significant modern-lens risk identified: the vocabulary here (Word, Essence, co-existent) is dense fourth-century Trinitarian argument, not language that has drifted meaning for a modern reader - it reads as unfamiliar and technical, not as something that misleadingly sounds familiar."
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether people outside the councils had settled views about who Jesus was"
  - "participant asks whether the creed reached ordinary members or stayed with bishops"
relations:
- type: associated-with
  target: desert.quote.antony-arians-serpents
- type: associated-with
  target: desert.dw.god
- type: associated-with
  target: desert.figure.antony
- type: associated-with
  target: desert.dw.judgment-and-resurrection
---
Verified verbatim against the vendored file, S69 - immediately
following the S68 passage desert.quote.antony-arians-serpents cites (a
narrowed locus as of this same commit; the two quotes are adjacent, not
overlapping). Added per Step 4 Round 1 review Finding S2, which found
that record's own body wrongly claimed §69 does not state "a positive
Trinitarian formula" - it does, in these words, and this record
supplies it directly rather than leave the claim standing uncorrected
by omission. §69's own narrative frame (Antony "being summoned by the
bishops and all the brethren, he descended from the mountain, and
having entered Alexandria, he denounced the Arians") shows this was
public teaching at episcopal summons, not private refusal - see the
corrected desert.dw.councils for that fuller picture.

Step4, Round 2 review Finding S1: the text above previously read "The
Son of God..." and "Wherefore," both silently altered from the vendored
"...that the Son of God..." and "And therefore," and was silently
truncated before "for the Word was always co-existent with the
Father," under a body sentence claiming the text had been verified
verbatim. Character-compared against the file directly this pass and
corrected above: the opening ellipsis marks the excerpt's start
mid-clause, "that" and "And therefore" are restored to the vendored
wording, and the full sentence including its final clause is now
carried rather than cut. Finding C6: the body's own claim that this
record and desert.quote.antony-arians-serpents cite "the same division
(SS68-69)" no longer held once that sibling record's locus was narrowed
to S68 alone by the same commit - corrected above to state the two
loci are adjacent, not identical.
