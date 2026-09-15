---
id: alx.dw.original-sin
world_id: alexandria-catechetical
record_type: doctrinal_witness
schema_version: 2
status: draft
register: emic
canon_cells:
- F1-T
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: alx.source.origen-de-principiis
  locus: I-III (Rufinus-mediated)
  license: public-domain
- source_id: alx.source.clement-paidagogos
  locus: I (the physician frame)
  license: public-domain
retrieval:
  tier: 1
  retrieve_when: []
  do_not_retrieve_when: []
text: >-
  Are people born already guilty? We believed something real went
  wrong at the root of humanity. Adam's fall casts its shadow over every soul.
  Death and disorder are inherited, and no one reaches God unwounded. But the
  later Western teaching a modern asker usually means - guilt at birth,
  condemnation at birth - is not how we put it. Our teachers spoke of
  inherited death and weakness, and of a fall that each soul also signs onto
  in its own living. Infant baptism they received as custom, and they
  discussed its reason rather than defining it. Origen wondered about the
  soul's own descent, but as open inquiry, not doctrine. What stays constant
  is the direction. The wound is real, universal, and inherited in its
  effects. That guilt language is not here, and the
  doctor's imagery outweighs the courtroom's.
positions:
- 'a real, universal fall: inherited mortality and disorder'
- each soul's own consent implicated - the fall is ratified, not merely suffered
- healing framed medicinally (the Word as physician) more than juridically
tensions:
- Origen's soul-speculations (transmission-filtered) vs the rule of faith's plain ground
- 'the translational gap: ''original sin'' as the asker means it is Augustine''s later grammar, not this
  world''s'
---
The F1-T cell (original sin / bread-and-cup / faith-alone questions
share the cell; eucharistia's senses carry the second, and the
faith-works question is answered inside the faith-to-gnosis material).

REGISTER TRANSLATION (2026-08-29, the alx pass of the fleet register ruling - see the ijc records' same-day note): spoken field translated in place to plain modern English, translation not summary; every sourced claim, name, and reviewed constraint preserved. Fixed at the record layer, not the prompt (no-fix-on-fix).

BAR SWEEP (2026-08-29, Mark: "much better thats the bar" - see Ministry/Technology/CiC_Register_Bar_2026-08-29.md): text rewritten to the approved sample's level - short sentences, everyday words; every claim, name, quote, and reviewed constraint kept.

CORRECTED 2026-09-08, records/alx audit: this file had two top-level
`retrieval:` keys - an early one (tier: 1, empty triggers) and a later one
(tier: 2, three retrieve_when triggers about infant baptism). YAML
last-wins, so the file was silently shipping as tier-2 retrieval-gated
instead of the intended tier-1 always-available chunk, unlike every other
doctrinal_witness file in this registry (all confirmed tier 1). Merged to
one `retrieval:` block, tier 1, matching sibling DW files' empty-array
pattern. The dropped tier-2 triggers, kept here for documentation only
since no other tier-1 DW file carries live retrieve_when entries: "participant
asks whether you baptised babies, infants or children, or only adults";
"participant asks who could be baptised and at what age"; "participant
asks whether you baptise or baptize babies, infants and children, or only
adults" - all already answered inline by this cell's own text ("Infant
baptism they received as custom, and they discussed its reason rather than
defining it").
