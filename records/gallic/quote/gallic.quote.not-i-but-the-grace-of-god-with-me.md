---
id: gallic.quote.not-i-but-the-grace-of-god-with-me
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
    Documented as Cassian's own text (Institutes XII.9, read at its locus for this record) - the
    closing book of the Institutes' own remedy for pride, load-bearing as this world's plainest,
    least controversial statement of the grace-and-effort teaching, offered before any outside
    report of the controversy existed.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes XII.9 (npnf211 div iv.iii.xii.ix, file lines 25037-25044): the remedy for
    pride - crediting every sense of progress to God's grace, in the Apostle's own words"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how an individual monk was supposed to think about their own progress"
  - "participant asks for the plainest, least argumentative statement of this world's own grace teaching"
  prefer_instead:
  - "participant wants the fuller, more contested doctrinal argument - retrieve gallic.quote.chaeremon-grace-requires-our-effort or gallic.quote.chaeremon-three-stages-of-grace"
text: >-
  And so we can escape the snare of this most evil spirit, if in the
  case of every virtue in which we feel that we make progress, we say
  these words of the Apostle: "Not I, but the grace of God with me,"
  and "by the grace of God I am what I am;" and "it is God that
  worketh in us both to will and to do of His good pleasure."
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  This is Book XII's own remedy against pride, not an entry in the later Augustine controversy -
  Cassian offers it as a practical habit of speech for a monk who senses progress, quoting Paul
  three times over rather than arguing a position.
modern_rendering: >-
  And so we can escape the snare of this most evil spirit. We can do so if, in every virtue where
  we feel we are making progress, we say these words of the Apostle: "Not I, but the grace of God
  with me." And: "By the grace of God I am what I am." And: "It is God who works in us both to
  will and to do, according to His good pleasure."
relations:
- type: associated-with
  target: gallic.gravity.grace-and-effort
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"Not I, but the grace of God"` returns line 25041; `grep -n "worketh in us both to will"` returns
line 25043. Read with `sed -n '25036,25044p'`, inside `<div4 title="Chapter IX. How we too may
overcome pride." ... id="iv.iii.xii.ix">` (Institutes Book XII, chapter 9). The quoted span is one
complete sentence with three nested Pauline quotations, "And so we can escape..." through "...of
His good pleasure.", ending at its own period.

Normalization: line breaks joined with single spaces; the source's curly quotation marks around
the three nested Pauline quotations are rendered here as straight double quotes, the same marks in
a different Unicode form - these are Scripture quoted inside Cassian's own sentence, not this
record's own added structure. No word was added, dropped, substituted, or reordered.

This span was previously carried, unresolved, inside gallic.gravity.grace-and-effort's own
`description` field. The host record now paraphrases it in its own voice and
points here for the verbatim wording.
