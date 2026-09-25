---
id: gallic.quote.martin-power-present-catechumen-raising
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
    Documented as Sulpitius's own text (Vita ch. VII, read at its locus for this record). The
    event is Martin's best-known miracle, told by an author who was not present; what this record
    carries as load-bearing is the wording itself (Roberts's editorial endnote glosses "power was
    present" as adesse virtutem, the Latin behind this world's own virtus vocabulary), not an
    assessment of whether the raising happened.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "Life of St. Martin ch. VII (npnf211 div ii.ii.viii, file lines 987-999): Martin's prayer
    over the dead catechumen, and his own sense that power was present"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what a virtus (an act of power) actually looked like from the inside"
  - "participant asks how Martin himself experienced the moment before a miracle"
  prefer_instead:
  - "participant wants the miracle story told in full, with what came before and after - retrieve the fuller narrative context, not this one moment alone"
text: >-
  Having given himself for some time to earnest prayer, and perceiving by
  means of the Spirit of God that power was present, he then rose up for
  a little, and gazing on the countenance of the deceased, he waited
  without misgiving for the result of his prayer and of the mercy of the
  Lord.
speaker_or_author: Sulpitius Severus, narrating
license: verbatim
modern_lens_note: >-
  A modern reader may expect "power" here to mean force or control. Sulpitius means something
  narrower and more precise: a sense, given by the Spirit, that God was about to act. Martin does
  not command anything at this point - he waits. The power is God's; what Martin has is a
  perception that it is present.
modern_rendering: >-
  He gave himself to earnest prayer for some time. Through the Spirit of God, he sensed that
  power was present. Then he rose up for a little while. He gazed at the face of the one who had
  died. He waited without misgiving for the result of his prayer and of the Lord's mercy.
relations:
- type: associated-with
  target: gallic.force.power-displayed-disowned
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"perceiving by"` returns line 995; `grep -n "he then rose up for a little"` returns line 998.
Read with `sed -n '993,1000p'`, inside `<div3 ... id="ii.ii.viii">` (Chapter VII, the raising of
the catechumen). The quoted span runs from "Having given himself" through "of the mercy of the
Lord," ending at the sentence's own period.

Normalization: the source hard-wraps prose at fixed widths; line breaks were joined with single
spaces. A translator's endnote (`<note n="18" .../>`, glossing "power was present" as Latin
"adesse virtutem") sits inside the source's own sentence and is apparatus, not part of the quoted
prose - excluded exactly as the fleet's quote-verbatim tooling strips every `<note>` block before
matching. No word was added, dropped, substituted, or reordered.

speaker_or_author is a plain string, not a figure id: this is Sulpitius's own third-person
narration of Martin's action, not Martin's own words in quotation.