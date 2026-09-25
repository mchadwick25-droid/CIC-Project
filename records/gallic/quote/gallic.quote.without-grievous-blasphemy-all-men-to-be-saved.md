---
id: gallic.quote.without-grievous-blasphemy-all-men-to-be-saved
world_id: gallic-monastic-ascetic-christianity
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Widely Accepted
  divergence_note: >-
    Documented as Cassian's own text (Conference XIII.7, read at its locus for this record);
    Widely Accepted as Cassian's report of Chaeremon's teaching, the same caveat carried by this
    world's other Chaeremon quote records (gallic.quote.chaeremon-grace-requires-our-effort,
    gallic.quote.chaeremon-three-stages-of-grace).
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "Conference XIII.7 (npnf211 div iv.v.iv.vii, file lines 37742-37759): Chaeremon's
    argument that God cannot be imagined to will only some, rather than all, to be saved"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether this world believed God chose only some people for salvation"
  - "participant asks how Chaeremon argued against a limited view of God's saving will"
  prefer_instead:
  - "participant wants the practical, effort-focused side of the same teaching - retrieve gallic.quote.chaeremon-grace-requires-our-effort"
text: >-
  For if He willeth not that one of His little ones should perish, how
  can we imagine without grievous blasphemy that He does not generally
  will all men, but only some instead of all to be saved?
speaker_or_author: "Abbot Chaeremon, as Cassian records him (Conference XIII.7)"
license: verbatim
modern_lens_note: >-
  Chaeremon calls the opposite view - that God wills only some to be saved - not merely wrong but
  blasphemous. The argument runs from a smaller claim (God does not will one child to perish) to
  the larger one (God wills all, not some, to be saved), as a single continuous inference.
modern_rendering: >-
  For if He wills none of His little ones to perish, how can we, without grievous blasphemy,
  imagine He does not will all people's salvation? That He wills only some to be saved, instead
  of all people in general?
relations:
- type: associated-with
  target: gallic.gravity.grace-and-effort
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"generally will"` returns line 37758, inside `<div4 title="Chapter VII. Of the main purpose of God
and His daily Providence." ... id="iv.v.iv.vii">` (line 37735) - Conference XIII, chapter 7,
matching this world's own established locus format for Conference XIII citations. The source's own
italic emphasis on "all" and "some" is typographic, not part of the words themselves. Read with
`sed -n '37742,37759p'`. The quoted span is one complete sentence, "For if He willeth not..."
through "...to be saved?", ending at its own question mark. The host record's own prior citation
located this at "XIII.7," which this record confirms directly against the text rather than taking
on the host's word alone - a first grep for the host's own quoted wording, searched without regard
to chapter, initially matched an unrelated "grievous blasphemy" passage roughly 3,300 lines earlier
(Conference IX, on natural law); the correct locus was found by searching for the distinctive
"generally will...all men...some instead of all" construction instead.

Normalization: line breaks joined with single spaces; the source's own italic markup around "all"
and "some" was dropped (plain-text rendering, no emphasis added or removed in meaning). No word was
added, dropped, substituted, or reordered.