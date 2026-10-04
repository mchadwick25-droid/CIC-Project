---
id: gallic.quote.profane-notion-attribute-everything-to-free-will
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
    Documented as Chaeremon's own text (Conference XIII.16, read at its locus for this record) - the
    world's own refusal, in the same chapter-sequence as its refusal of a limited saving will (Conf.
    XIII.7, nine chapters earlier), of the opposite extreme: that everything rests on human free
    will.
sources:
- source_id: gallic.source.cassian-conferences-part-ii
  locus: "XIII.16 (npnf211 div iv.v.iv.xvi, file lines 38459-38465): the refusal of the opposite
    extreme, that grace is earned by desert"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why the south refused the idea that free will earns salvation by its own
    desert"
  - "participant wants the Conference's own words refusing that grace is deserved"
  prefer_instead:
  - "participant wants the companion refusal of a limited saving will - retrieve gallic.quote.grievous-blasphemy-not-all-men-to-be-saved"
text: >-
  But let no one imagine that we have brought forward these instances
  to try to make out that the chief share in our salvation rests with
  our faith, according to the profane notion of some who attribute
  everything to free will and lay down that the grace of God is
  dispensed in accordance with the desert of each man:
speaker_or_author: "Abbot Chaeremon, as Cassian records him (Conference XIII.16)"
license: verbatim
modern_lens_note: >-
  Chaeremon has just given examples of faith bringing a large reward - he stops here to head off a
  wrong conclusion. The examples are not proof that free will earns salvation by its own desert. He
  names that reading directly as a "profane notion," refusing it in the same chapter-sequence he
  refuses the opposite extreme (a limited saving will, Conf. XIII.7, nine chapters earlier) - grace
  and effort are held together, neither substituted for the other.
modern_rendering: >-
  But let no one imagine that we have given these examples to try to show that our faith has the
  chief share in our salvation. That would fit the profane notion of some people. They attribute
  everything to free will. They also lay down the rule that God gives out His grace according to
  what each person deserves.
relations:
- type: associated-with
  target: gallic.force.africa-and-rome-pressure
use_note:
  means: "Chaeremon, in Cassian's Conference XIII, rejects as profane the notion that everything rests on free will and that grace follows each man's desert."
  not_for:
    - "Cassian as a teacher of salvation by free will, which this passage expressly refuses"
    - "the opposite refusal of a limited saving will, which sits in gallic.quote.without-grievous-blasphemy-all-men-to-be-saved"
    - "a resolution of the contested grace teaching of Conference XIII"
  years: {from: 426, to: 426}
  status: provisional
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"let no one imagine" cic/texts/npnf211..."` matches two chapters; the one needed is line 38459,
inside `<div4 title="Chapter XVI. Of the grace of God; to the effect that it transcends the narrow
limits of human faith." ... id="iv.v.iv.xvi">` (Conference XIII, Chaeremon's own conference) -
confirmed by reading with `sed -n '38455,38468p'`, not the unrelated "let no one imagine" at line
44926 in a different chapter. The quoted span is Chaeremon's own subordinate clause, "But let no one
imagine..." through "...desert of each man:", ending at the source's own colon - the sentence itself
continues past this point ("but we plainly assert our unconditional opinion..."), not carried here;
no terminal punctuation is invented where the source has none.

Normalization: line breaks joined with single spaces. No word was added, dropped, substituted, or
reordered.
