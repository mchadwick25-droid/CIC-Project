---
id: gallic.quote.martin-exorcism-without-touch-or-reproach
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
    Documented as Gallus's own account, in Sulpitius's Dialogues (III.6, read at its locus for
    this record). Reported at second hand within the frame of a dialogue narrated to Postumianus
    and Sulpitius; what this record carries as load-bearing is the described manner of the
    exorcism, not independent corroboration that any given exorcism occurred.
sources:
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: "Dialogues III.6 (npnf211 div ii.iv.iii.vi, file lines 4900-4909): Martin's manner of
    exorcism - no touch, no rebuke, sackcloth, the doors bolted"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how Martin actually performed an exorcism"
  - "participant asks whether Martin's power was showy or restrained"
  prefer_instead:
  - "participant asks about the possessed themselves, or what happened after - retrieve the fuller Dialogues III.6 narrative"
text: >-
  But if at any time Martin undertook the duty of exorcising the
  demons, he touched no one with his hands, and reproached no one in
  words, as a multitude of expressions is generally rolled forth by the
  clerics; but the possessed, being brought up to him, he ordered all
  others to depart, and the doors being bolted, clothed in sackcloth
  and sprinkled with ashes, he stretched himself on the ground in the
  midst of the church, and turned to prayer.
speaker_or_author: "Gallus, as Sulpitius Severus records his account in the Dialogues"
license: verbatim
modern_lens_note: >-
  This is Martin's own quiet method set against the norm the passage names directly - clerics who
  perform exorcism with a "flood of phrases." No touch, no rebuke, no audience but the possessed
  and the walls: the restraint is the point, and it sits opposite the more public, garment-centered
  power this world's own north-south tension turns on.
modern_rendering: >-
  But whenever Martin took on the duty of driving out demons, he touched no one with his hands.
  He rebuked no one with words, the way the clergy usually pour out a flood of phrases. Instead,
  when the possessed were brought to him, he ordered everyone else to leave. The doors were
  bolted. Dressed in sackcloth and sprinkled with ashes, he stretched himself out on the ground
  in the middle of the church. And he turned to prayer.
relations:
- type: associated-with
  target: gallic.force.power-displayed-disowned
---
Verified directly against cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml. `grep -n
"touched no one with his hands"` returns line 4900; `grep -n "turned to prayer"` returns line
4907. Read with `sed -n '4898,4908p'`, inside `<div4 ... id="ii.iv.iii.vi">`. The quoted span runs
from "But if at any time" through "turned to prayer.", ending at the sentence's own period - one
continuous sentence in the source, joined by semicolons.

Normalization: line breaks joined with single spaces; a page-break tag (`<pb n="49" .../>`)
falling mid-sentence between "to" and "him" was removed with no text lost. No word was added,
dropped, substituted, or reordered.

speaker_or_author matches this world's own established convention for Dialogues III material
(gallic.quote.brictio-horses-and-slaves): Gallus narrates the Martin material in Dialogues II-III,
with Sulpitius himself present as audience.

This span was previously carried, unresolved, inside gallic.force.power-displayed-disowned's own
`description` field. The host record now paraphrases it in its own voice and
points here for the verbatim wording.
