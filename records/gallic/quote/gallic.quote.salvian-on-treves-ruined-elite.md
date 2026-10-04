---
id: gallic.quote.salvian-on-treves-ruined-elite
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Widely Accepted
  divergence_note: >-
    Widely Accepted: a named contemporary author, resident in the region, writing in the first person
    ("I myself have seen"). Not Documented outright, for the same reason the host record's own
    divergence_note states - Salvian is a preacher making an indictment, not a chronicler making a
    report, and his own moral judgment about the city's elite is carried here as his framing, not an
    independent finding this record verifies. "Taken by storm no less than four times" is Salvian's
    own count at this locus (VI.13); his own text gives a different count, "three times," elsewhere in
    the same book (VI.15) - a genuine internal inconsistency this record keeps rather than resolves.
sources:
- source_id: gallic.source.salvian-on-the-government-of-god
  locus: "On the Government of God, Book VI.13 (Sanford 1930, pp. 179-180; file lines 8089-8127): the moral ruin of Trier's surviving elite, and the city's repeated sack"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Salvian himself said about a specific ruined Gallic city's people, not just its buildings"
  - "participant asks whether disaster made people better or worse"
  - "Representative needs Salvian's own words on wealth and character surviving unevenly"
  prefer_instead:
  - "participant wants the corpses and the aftermath - retrieve gallic.quote.salvian-on-the-unburied-dead"
  - "participant wants the circus petition and Salvian's rebuke - retrieve gallic.quote.salvian-on-the-demand-for-circuses"
  - "participant wants the whole episode told as a story - retrieve gallic.story.circuses-amid-the-ruins, which this record is drawn from"
text: >-
  I myself have seen men of lofty birth and honor, though already despoiled and plundered, still less
  ruined in fortunes than in morality; for, ravaged and stripped though they were, something still
  remained to them of their property, but nothing of their character. ... The wealthiest city of Gaul
  was taken by storm no less than four times.
speaker_or_author: "Salvian of Marseilles"
license: verbatim
modern_lens_note: >-
  A modern reader expects a disaster narrative to measure loss in property or lives. Salvian measures
  it in character: men who kept "something still" of their wealth kept "nothing of their character."
  The line about four sacks, read against Salvian's own later count of three, is a reminder that even a
  direct eyewitness writing polemic does not always agree with himself - the record keeps that
  inconsistency rather than smoothing it away.
modern_rendering: >-
  I have seen with my own eyes men of high birth and high rank who had already been robbed and
  plundered. Yet their fortunes were less ruined than their morals. Ravaged and stripped as they were,
  they still had something left of their property, but nothing left of their character. ... The
  richest city in Gaul was taken by storm no fewer than four times.
relations:
- type: associated-with
  target: gallic.story.circuses-amid-the-ruins
- type: associated-with
  target: gallic.source.salvian-on-the-government-of-god
- type: associated-with
  target: gallic.quote.salvian-on-the-unburied-dead
- type: associated-with
  target: gallic.quote.salvian-on-the-demand-for-circuses
use_note:
  means: "Salvian, in On the Government of God, says Trier's despoiled nobles lost more in character than in fortune and that the city was stormed four times."
  not_for:
    - "a settled number of sacks, when Salvian says three in gallic.quote.salvian-on-the-unburied-dead"
    - "a neutral report rather than a preacher's moral indictment"
    - "the demand for circuses, which sits in gallic.quote.salvian-on-the-demand-for-circuses"
  years: {from: 439, to: 450}
  status: reviewed
---
Verified against cic/texts/salvian_on-the-government-of-god_sanford1930.txt. `grep -n "lofty birth and
honor"` returns one hit, line 8093; `grep -n "taken by storm no less than four"` returns one hit, line
8126-8127 (split across a line break in the OCR text: "...was taken / by storm no less than four
times"). Read lines 8089-8127 directly.

The remaining ellipsis marks the gap between "nothing of their character." and "The wealthiest city of
Gaul" - the two spans sit roughly 30 lines apart in the source, separated by an extended passage about
the elite's feasting and dissolution not itself flagged for this record. Both spans fall within the
same numbered section, VI.13, and the same continuous indictment of the same city's surviving notables,
so they are kept as one record rather than two.

At the point between "despoiled and plundered," and "still less ruined in fortunes," the vendored file
(line 8093-8094) has "though already despoiled and plundered,*® still less ruined in fortunes than in
morality" - the "*®" is Sanford's own superscript footnote marker (note 45, "That is, in the first sack
of the city of Tréves"), mangled by OCR into two glued glyphs with no space. It is apparatus, not a gap
in the sentence: read with the marker removed, the clause runs on unbroken, "though already despoiled
and plundered, still less ruined in fortunes than in morality." No content is omitted at that point.

Normalization: the vendored OCR text hyphenates words across page breaks and hard-wraps lines; line
breaks and hyphenation were joined with single spaces / no hyphen. Footnote markers (the source's own
superscript reference numbers) were dropped as apparatus, not text. No word was added, dropped,
substituted, or reordered within either quoted phrase.
