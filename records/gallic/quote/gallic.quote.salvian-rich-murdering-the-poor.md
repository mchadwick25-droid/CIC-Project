---
id: gallic.quote.salvian-rich-murdering-the-poor
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
    Documented as Salvian's own text (Gov. IV.6, read at its locus for this record). Salvian's
    picture is a preacher's indictment, not a survey - Sanford's own Introduction (editorial)
    treats his hyperbole as a critical problem, Dominant Modern Reconstruction as to the province's
    actual fiscal condition; this record carries Salvian's own stated claim, not an assessment of
    how literally to take it.
sources:
- source_id: gallic.source.salvian-on-the-government-of-god
  locus: "IV.6 (Sanford p. 110): tax relief that enriches the rich and further burdens the poor"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks what Salvian actually blamed for Gaul's ruin"
  - "participant asks whether this world saw the barbarian collapse as purely external"
  prefer_instead:
  - "participant wants Salvian's fuller theological reading of the collapse as judgment - retrieve gallic.quote.salvian-ever-present-judgment-gallic-provinces"
text: >-
  Hence I say that nothing can be more wicked than the rich who are
  murdering the poor by their so-called remedies, and nothing more
  unlucky than the poor, to whom even the general panacea brings death.
speaker_or_author: Salvian of Marseilles, On the Government of God
license: verbatim
modern_lens_note: >-
  Salvian is not describing violence in the literal sense. The "remedies" are real tax measures -
  relief laws that, as he reads their actual effect, shifted the burden onto those least able to
  bear it. He calls this murder because the outcome is death, not because anyone drew a blade.
modern_rendering: >-
  That is why I say nothing can be more wicked than the rich who are murdering the poor with
  their so-called remedies. And nothing can be more unlucky than the poor, for whom even the cure
  meant for everyone brings death.
relations:
- type: associated-with
  target: gallic.force.barbarian-fiscal-ruin
use_note:
  means: "Salvian, in On the Government of God, calls the rich murderers of the poor because so-called tax remedies shifted the burden onto those least able to bear it."
  not_for:
    - "literal killing, when Salvian means the deadly effect of tax measures"
    - "a measured fiscal history rather than a preacher's indictment"
    - "flight to the barbarians, which sits in gallic.quote.salvian-free-men-in-seeming-captivity"
  years: {from: 439, to: 450}
  status: provisional
---
Verified directly against cic/texts/salvian_on-the-government-of-god_sanford1930.txt. `grep -n
"more wicked than the rich"` returns line 5064; read with `sed -n '5052,5067p'`, on the page
numbered "110 THE FOURTH BOOK" in this edition's own running head. The quoted span is one
continuous sentence, "Hence I say..." through "...brings death.", ending at its own period.

Normalization: this edition's own hard line-wraps and a hyphenated line-break word ("so-\ncalled")
were rejoined with no character lost. No word was added, dropped, substituted, or reordered.

speaker_or_author is a plain string: no gallic.figure record exists for Salvian.