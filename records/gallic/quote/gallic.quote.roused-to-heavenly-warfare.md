---
id: gallic.quote.roused-to-heavenly-warfare
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
  formation_confidence: Documented
  divergence_note: >-
    Documented as Sulpitius's own text (Vita ch. I, read at its locus for this record) - his own
    stated purpose for writing Martin's life, in his own opening chapter.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. I (npnf211 div ii.ii.ii, file lines 592-598): Sulpitius's own
    stated reason for writing - to rouse his readers to true knowledge, heavenly warfare, and
    divine virtue"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks why Sulpitius says he wrote Martin's life at all"
  - "participant asks where 'heavenly warfare' language first appears in this world's own literature"
  prefer_instead:
  - "participant wants the military idiom applied to Martin's own life directly - retrieve gallic.quote.martin-refuses-the-donative"
text: >-
  For this reason, I think I will accomplish something well worth the
  necessary pains, if I write the life of a most holy man, which shall
  serve in future as an example to others; by which, indeed, the
  readers shall be roused to the pursuit of true knowledge, and
  heavenly warfare, and divine virtue.
speaker_or_author: Sulpitius Severus, narrating
license: verbatim
modern_lens_note: >-
  This is Sulpitius's own stated purpose, in his opening chapter, before any story of Martin
  begins: the book exists to rouse readers to three things named together - true knowledge, heavenly
  warfare, and divine virtue. The military term sits inside a list about right living, not about an
  external adversary.
modern_rendering: >-
  For this reason, I think I will achieve something well worth the effort it needs if I write the
  life of a most holy man. It will serve in future as an example to others. Through it, indeed, its
  readers will be roused to pursue true knowledge, heavenly warfare, and divine virtue.
relations:
- type: associated-with
  target: gallic.gravity.soldier-of-christ
use_note:
  means: "Sulpitius states in the first chapter of the Life of Martin that he writes so readers will be roused to true knowledge, heavenly warfare and divine virtue."
  not_for:
    - "a call to physical combat, when the warfare sits in a list about right living"
    - "Cassian's soldier-of-Christ opening, which sits in gallic.quote.institutes-opening-soldier-of-christ"
    - "a neutral history rather than an exemplary life written to form its readers"
  years: {from: 397, to: 397}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"shall be roused to the pursuit of true"` returns line 597; read with `sed -n '592,599p'`, inside
`<div3 title="Chapter I. Reasons for writing the Life of St. Martin." ... id="ii.ii.ii">`. The
quoted span is one complete sentence, "For this reason, I think I will accomplish..." through
"...heavenly warfare, and divine virtue.", ending at its own period.

Normalization: the source hard-wraps prose at fixed widths, including a page break mid-sentence
(`<pb .../>` before "seek after"); line breaks and the page break were joined with single spaces.
No word was added, dropped, substituted, or reordered.
