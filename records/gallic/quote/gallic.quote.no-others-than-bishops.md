---
id: gallic.quote.no-others-than-bishops
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
    The wording is Documented as Sulpitius's own aside (Vita ch. XXVII). Who exactly these
    "calumniators" were is not named - Sulpitius pointedly withholds names - so the identity of the
    bishops in question is Inferential-Thin; what this record carries as load-bearing is Sulpitius's
    own plain statement that some of Martin's detractors held episcopal office, not an identification
    of which bishops.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. XXVII (npnf211 div ii.ii.xxviii, file lines 1938-1941): Sulpitius's aside on the source of some of Martin's slander"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether Martin's opposition came from outside the Church or from within it"
  - "participant asks who resented or worked against Martin during his lifetime"
  prefer_instead:
  - "participant asks for the names of these bishops - Sulpitius does not give them, and this record does not supply what the source withholds"
text: >-
  And—O wickedness worthy of deepest grief and groans!—some of his
  calumniators, although very few, some of his maligners, I say, were
  reported to be no others than bishops!
speaker_or_author: Sulpitius Severus, narrating
license: verbatim
modern_lens_note: >-
  Sulpitius writes this as a genuine shock, not a routine complaint - the exclamation point and the
  "wickedness worthy of deepest grief" are his own outrage. The detail matters for this world's
  formation: it shows that opposition to Martin's kind of holiness did not come only from outside the
  Church but sometimes from inside the episcopate itself, the very office Martin himself had been made
  to hold.
modern_rendering: >-
  And oh, what wickedness, worthy of the deepest grief and groans! Some
  of his slanderers, though very few - some of those who spoke evil of
  him, I say - were reported to be none other than bishops!
relations:
- type: associated-with
  target: gallic.gravity.authority-ambivalence
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"calumniators"` returns a hit at line 1939 inside the chapter div `<div3 title="Chapter XXVII.
Wonderful Piety of Martin." ... id="ii.ii.xxviii">` (printed heading "Chapter XXVII.", div id one
Roman numeral higher, the offset this corpus's records consistently note). The sentence runs lines
1938-1941: "And—O wickedness worthy of deepest grief and groans!—some of his calumniators, although
very few, some of his maligners, I say, were reported to be no others than bishops!"

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single
spaces. No word was added, dropped, substituted, or reordered. The host record's own prior wording
("some of his calumniators ... were reported to be no others than bishops!") elided the interior
clause "although very few, some of his maligners, I say,"; this record restores the full sentence as
Sulpitius wrote it.
