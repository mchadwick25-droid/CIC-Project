---
id: desert.quote.pachomian-rule-opening-superscription
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: [F4-I]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Documented for the text itself, matching desert.story.angel-hands-the-tablet's own basis - what
    is documented is that the received Ethiopic recension opens with this superscription; whether an
    angel actually spoke to Pachomius is not a question this record takes a view on.
sources:
- source_id: desert.source.pachomian-corpus
  locus: >-
    Ethiopic recension, Part I, opening superscription, p. 681, in Schodde's English
    (cic/texts/pachomius_rules-ethiopic_schodde1885.txt)
  license: public-domain
text: "In the name of the holy Trinity. The ordinance which the angel of the Lord commanded to Abba Pachomius."
modern_rendering: >-
  This rule begins in the name of the holy Trinity. The angel of the Lord gave it to
  Abba Pachomius as a command.
speaker_or_author: "the Ethiopic rule's own opening superscription"
license: verbatim
modern_lens_note: >-
  No significant modern-lens risk identified: "Trinity," "angel," and "Abba" are terms this world
  itself needs and uses plainly elsewhere; nothing here has drifted into a misleading modern sense.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks where a monastic rule got its authority, or who was entitled to write one"
  - "participant asks how this legislation itself opens, in its own words"
relations:
- type: associated-with
  target: desert.story.angel-hands-the-tablet
- type: associated-with
  target: desert.figure.pachomius
use_note:
  means: "The received Ethiopic recension of the Pachomian rules opens by calling itself the ordinance the angel of the Lord commanded to Abba Pachomius."
  not_for:
    - "a claim that an angel in fact dictated the rule"
    - "the Ethiopic wording as Jerome's Latin Praecepta or a Coptic original"
    - "the angel frame as only Palladius's or Sozomen's packaging, when it stands in the received rule text itself"
  years: {from: 320, to: 346}
  status: reviewed
---
Verified directly against cic/texts/pachomius_rules-ethiopic_schodde1885.txt. `grep -n "In the name of
the holy Trinity"` returns one hit, line 168, immediately following the translator's own bracketed
"[Translation.] PART I." heading and the printed page break marked "[p. 681]" - the received text's own
opening words, before the narrative of the vision begins. No wording added, dropped, substituted, or
reordered.
