---
id: gallic.quote.perfection-not-gained-without-grace
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
    Documented as Cassian's own text (Institutes XII.14, read at its locus for this record) - his
    own stated position, attributed by him to the elders rather than given as his own private
    opinion.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes XII.14 (npnf211 div iv.iii.xii.xiv, file lines 25166-25171): Cassian's own
    statement that effort and grace are both required, neither sufficient alone"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether Cassian thought effort alone could gain perfection"
  - "participant asks for the plainest statement of the grace-and-effort balance, in Cassian's own words"
  prefer_instead:
  - "participant wants the practical remedy for pride instead - retrieve gallic.quote.not-i-but-the-grace-of-god-with-me"
text: >-
  But clearly and most earnestly do I lay down, not giving my own
  opinion, but that of the elders, that perfection cannot possibly be
  gained without these, but that by these only without the grace of God
  nobody can ever attain it.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  Cassian frames this as inherited teaching, not his own opinion - "not giving my own opinion, but
  that of the elders." The claim itself cuts both ways at once: effort ("these") is necessary, but
  never sufficient by itself; grace is necessary too, and without it effort alone gains nothing.
modern_rendering: >-
  But I state this clearly and most earnestly. It is not my own opinion, but that of the elders.
  Perfection cannot possibly be gained without these efforts. Yet by these efforts alone, without
  the grace of God, nobody can ever reach it.
relations:
- type: associated-with
  target: gallic.force.received-programs-logic
- type: associated-with
  target: gallic.force.africa-and-rome-pressure
use_note:
  means: "Cassian, in Institutes XII, states as the elders' teaching that perfection needs human effort yet no one attains it by effort without God's grace."
  not_for:
    - "a settled verdict on Cassian's orthodoxy in the grace controversy"
    - "the habit of crediting progress to grace, which sits in gallic.quote.not-i-but-the-grace-of-god-with-me"
    - "Chaeremon's teaching that God wills all to be saved, which sits in gallic.quote.without-grievous-blasphemy-all-men-to-be-saved"
  years: {from: 415, to: 426}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"nobody can ever attain it"` returns line 25170; read with `sed -n '25163,25171p'`, inside `<div4
title="Chapter XIV..." ... id="iv.iii.xii.xiv">` (Institutes XII.14). The quoted span is one
complete sentence, "But clearly and most earnestly do I lay down..." through "...nobody can ever
attain it.", ending at its own period.

Normalization: line breaks joined with single spaces; a translator's endnote on the chapter heading
("The language in this chapter is perilously near semi-Pelagianism...") sits at the chapter title,
outside this quoted sentence, and is excluded as apparatus rather than as part of the quoted prose.
No word was added, dropped, substituted, or reordered.
