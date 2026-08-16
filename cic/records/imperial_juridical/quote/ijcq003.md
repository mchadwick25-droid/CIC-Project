---
id: ijcq003
world_id: imperial-juridical-christianity
record_type: quote
schema_version: 1
jobs:
- 1
- 2
- 3
register: emic
review_state: draft
speaker_or_author: ijcfig002
text_translation: But since the victorious emperor himself long afterwards declared it to the writer
  of this history, when he was honored with his acquaintance and society, and confirmed his statement
  by an oath, who could hesitate to accredit the relation, especially since the testimony of after-time
  has established its truth?
locus: Eusebius, Life of Constantine, Book I, ch. 28
translation_used: srcIJC45
license: verbatim
confidence:
  citation_specificity: A
  verification_state: verified-direct
  verification_date: '2026-08-15'
  evidentiary_weight: load-bearing
  formation_confidence: Documented
---
Added 2026-08-15, deepening imperial_juridical further (Julius, then Ambrose, now Eusebius) from the
vendored NPNF2-01 attachment Mark sent with no accompanying text - read, per the session's established
pattern, as continuing "deepen imperial_juridical." Wording transcribed directly from
cic/texts/npnf201_eusebius-church-history-life-of-constantine.xml (CCEL proofed transcription of NPNF
Second Series vol. 1), the chapter recounting Constantine's cross-of-light vision. This is Eusebius
speaking in his own voice, in the third person, about his own historiographical method - explaining WHY
he credits the story: the emperor himself told him personally, years afterward, and swore an oath to it.
This is the passage ijcstory001 (title: "The Vision and the Alliance (Eusebius's Account)") actually
attests: its attested_occasion field describes "an account Eusebius states he heard from Constantine
himself, under oath, some years after the event," which this chapter's own text confirms nearly
verbatim ("confirmed his statement by an oath"). Matches ijcfig002's bridge_line closely ("A bishop and
historian. He wrote the emperor's life years after the events.") - this quote IS Eusebius explaining
that lag and that sourcing, in his own words.

A GENUINE SCOPING MISMATCH WAS CAUGHT AND AVOIDED while sourcing this: the world's only existing
Eusebius source row, srcIJC02, cites "esp. 4.24" and is licensed_for a different theological claim (the
"bishop of those outside" line). Assuming that citation was simply loosely stated and reusing it here
would have repeated the same category of error the Ambrose quote (ijcq002) caught by a different route -
trusting a citation instead of verifying it. Instead the vendored XML was searched directly by chapter
title, independent of srcIJC02's claim, and the vision account was located at div4 id="iv.vi.i.xxviii"
(Book I, ch. 28) - a different locus than 4.24. Two new, narrowly-scoped source rows were written for
it (srcIJC44, the primary Greek work; srcIJC45, the NPNF2-01 translation) rather than stretching
srcIJC02 to cover ground it does not license. srcIJC02 itself is untouched and remains valid only for
its own 4.24 claim.

Single-source, but doubly self-referential rather than doubly mediated the way Julius's letter is:
Eusebius is both the historian recording the vision AND the one reporting that he personally received
Constantine's oath - so this quote voices Eusebius's own testimony about his own sourcing, not a
third-party's quotation of someone else's words.
