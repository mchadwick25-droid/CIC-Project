---
id: gallic.quote.salvian-present-judgment-clearly-shown
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
    Documented as Salvian's own text (Gov. VII.10, read at its locus for this record). Named
    Tension as to scale/hyperbole carried per gallic.force.barbarian-fiscal-ruin's own
    divergence_note; not resolved here.
sources:
- source_id: gallic.source.salvian-on-the-government-of-god
  locus: "VII.10 (Sanford p. 201): a defeated Roman general's own captivity read as clear proof of
    present divine judgment"
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - "participant asks for the shortest, plainest statement that judgment is already happening, not just coming"
  prefer_instead:
  - "participant wants the fuller geographic sweep of the same claim - retrieve gallic.quote.salvian-ever-present-judgment-gallic-provinces"
text: >-
  In him, indeed, in addition to his actual misfortune, the present
  judgment of God was clearly shown.
speaker_or_author: Salvian of Marseilles, On the Government of God
license: verbatim
modern_lens_note: >-
  "Present" is the load-bearing word: Salvian is not predicting a coming judgment, he is reading
  an event that already happened - a general captured in the very city he had boasted he would
  conquer - as judgment already carried out.
modern_rendering: >-
  In his case, indeed, God's judgment was clear, right then and there. This came on top of the
  bad luck he actually suffered.
relations:
- type: associated-with
  target: gallic.force.barbarian-fiscal-ruin
- type: associated-with
  target: gallic.gravity.judgment-imminent-present
---
Verified directly against cic/texts/salvian_on-the-government-of-god_sanford1930.txt. `grep -n
"present judgment of God was clearly shown"` returns line 9010; read with `sed -n '8998,9011p'`.
The quoted span is one complete sentence, "In him, indeed..." through "...clearly shown.", ending
at its own period.

Normalization: hard line-wraps rejoined with single spaces. No word was added, dropped,
substituted, or reordered.

This span is referenced by two host records (gallic.force.barbarian-fiscal-ruin and
gallic.gravity.judgment-imminent-present); both now paraphrase it in their own voice and point
here for the verbatim wording. Reciprocal associated-with declared on both.
