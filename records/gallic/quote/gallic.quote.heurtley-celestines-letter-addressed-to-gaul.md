---
id: gallic.quote.heurtley-celestines-letter-addressed-to-gaul
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
    Widely Accepted as editorial transmission history, not this world's own primary-source voice -
    this is the NPNF volume's own editorial Appendix III (read at its locus for this record),
    reporting who complained to Pope Celestine and about what, not a passage from Vincent, Cassian,
    or Sulpitius themselves.
sources:
- source_id: gallic.source.npnf-editorial-apparatus
  locus: "Appendix III, Note on Section 85, Page 156 (npnf211 div iii.xxxvii, file lines 14867-14870):
    the editor's account of who complained to Celestine, and of what"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks who actually complained to Rome about the Gallic clergy, and what the complaint was"
  - "participant wants the letter's own real-world direction, distinct from Vincent's own reading of it"
  prefer_instead:
  - "participant wants Vincent's own quotation of the letter and his own reading of it - retrieve gallic.quote.vincent-celestines-letter-and-its-reading"
text: >-
  It appears that Prosper and Hilary had made a journey to Rome, where
  they then were, for the purpose of complaining to Celestine of the
  connivance of certain bishops of Southern Gaul with the unsound
  teaching of their clergy.
speaker_or_author: "Charles A. Heurtley, editorial Appendix III"
license: verbatim
modern_lens_note: >-
  This sentence is not Vincent's, Cassian's, or Sulpitius's voice - it is the modern editor's own
  account of the real complaint behind Celestine's letter, added to explain who wrote to Rome and
  why. It is carried here because it names the letter's actual direction (against certain Gallic
  bishops' own clergy), which Vincent's own quotation of the letter does not state outright.
modern_rendering: >-
  It appears that Prosper and Hilary had traveled to Rome, where they were staying at the time.
  They went there to complain to Celestine. Their complaint was that certain bishops of southern
  Gaul were tolerating the unsound teaching of their own clergy.
relations:
- type: associated-with
  target: gallic.force.contest-over-antiquity
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"It appears that Prosper and Hilary"` returns line 14867; read with `sed -n '14856,14872p'`, inside
`<div2 title="Appendix III. Note on Section 85, Page 156." ... id="iii.xxxvii">`. The quoted span is
one complete paragraph (`<p id="iii.xxxvii-p3">`), "It appears that Prosper and Hilary..." through
"...unsound teaching of their clergy.", ending at its own period.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.

speaker_or_author is a plain string: this is the NPNF volume's own editorial apparatus (Charles A.
Heurtley's Appendix III), not a figure from within this world.
