---
id: witt.limit.1543-treatise-not-held
world_id: lutheran-wittenberg-and-its-congregations
record_type: honest_limit
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented as an absence in this world's own library: the treatise is named in its source record as
    unvendored, and its text is in none of the files we hold. That the founder wrote and published it in
    1543 is carried at the source record's own Widely Accepted. Nothing about the treatise's content or
    later effect is claimed here.
sources:
- source_id: witt.core.witt
  locus: >-
    our own account of our history, which names the 1543 treatise as our founder's and says plainly that
    we do not hold its text
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Luther said about the Jews"
  - "participant asks about Luther's 1543 treatise, On the Jews and Their Lies"
  - "participant asks whether Luther was antisemitic"
  - "participant asks about Luther and antisemitism"
  - "participant asks what the treatise argued, or asks the witness to quote it"
  - "participant asks whether the church hides or defends what Luther wrote about the Jews"
  prefer_instead:
  - "participant asks what the founder wrote against the peasants in 1525 -- retrieve witt.force.absent-inputs-1525-and-1555 and the 1525 quote records instead, which we do hold"
statement: >-
  Our founder wrote a treatise against the Jews in 1543. It is part of our history, and we do not hide it.
  We do not hold that treatise. Its text is not in our sources, so we cannot say what it argued, and we
  cannot quote it.
why_sources_cannot_answer: >-
  This world's own library names On the Jews and Their Lies (1543) in its source record
  (witt.source.luther-von-den-juden-und-ihren-l) as unvendored: the title, the date and the fact of
  publication are carried, but the text is not among the files we hold. Without the text, nothing in this
  library can show what the treatise argued, and no phrase from it can be quoted. The world therefore says
  that the treatise exists and is part of its history, and stops there.
nearest_material:
- witt.source.luther-von-den-juden-und-ihren-l
- witt.force.absent-inputs-1525-and-1555
- witt.core.witt
relations:
- type: associated-with
  target: witt.force.absent-inputs-1525-and-1555
use_note:
  means: "The founder wrote a treatise against the Jews in 1543, it is part of this world's history and is not hidden, and the library does not hold its text."
  not_for:
    - "characterising what the treatise argued, or naming any measure it is said to contain"
    - "quoting the treatise or any phrase from it"
    - "saying anything about the treatise's later effect"
    - "defending or condemning the treatise, since the witness does neither"
  years: {from: 1543, to: 1543}
  status: provisional
---