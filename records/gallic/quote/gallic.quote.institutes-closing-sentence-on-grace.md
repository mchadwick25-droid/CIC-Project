---
id: gallic.quote.institutes-closing-sentence-on-grace
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
    Documented as Cassian's own text (Institutes XII.33, read at its locus for this record) - the
    work's own final sentence, closing the whole Institutes on humility toward God and dependence
    on grace.
sources:
- source_id: gallic.source.cassian-institutes
  locus: "Institutes XII.33 (npnf211 div iv.iii.xii.xxxiii, file lines 25856-25860): the closing
    sentence of the whole work"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how the Institutes actually ends"
  - "participant wants the work's own last word on grace, not a mid-book statement of the teaching"
  prefer_instead:
  - "participant wants the mid-book statement of the same teaching - retrieve gallic.quote.perfection-not-gained-without-grace"
text: >-
  Then, next after this we must keep a firm grasp of this same humility
  towards God: which we must so secure as not only to acknowledge that
  we cannot possibly perform anything connected with the attainment of
  perfect virtue without His assistance and grace, but also truly to
  believe that this very fact that we can understand this, is His own
  gift.
speaker_or_author: gallic.figure.cassian
license: verbatim
modern_lens_note: >-
  This is the very last sentence of the twelve-book Institutes, not an incidental remark. Cassian
  closes the whole work by pushing the humility one step further than usual: not only is virtue
  impossible without grace, but even the understanding that this is so is itself a gift, not
  something reasoned out independently.
modern_rendering: >-
  Next, after this, we must keep a firm grasp on this same humility toward God. We must hold it so
  firmly that we not only admit we cannot perform anything toward perfect virtue without His help
  and grace. We must also truly believe that even this understanding is itself His own gift.
relations:
- type: associated-with
  target: gallic.force.received-programs-logic
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"is His own gift"` returns line 25860; read with `sed -n '25852,25860p'`, inside `<div4 title="Chapter
XXXIII..." ... id="iv.iii.xii.xxxiii">` (Institutes XII.33). The quoted span is one complete
sentence, "Then, next after this..." through "...is His own gift.", immediately followed in the
source by `</div4></div3></div2>` - the close of the chapter, the book, and the whole work: this is
the Institutes' own final sentence.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
