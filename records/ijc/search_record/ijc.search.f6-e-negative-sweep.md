---
id: ijc.search.f6-e-negative-sweep
world_id: imperial-juridical
record_type: search_record
schema_version: 2
status: draft
register: etic
canon_cells:
- F6-E
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Documented
  divergence_note: null
sources: []
query: "Cell F6-E (testimony extracted from enslaved persons under torture; martyrdom-seeking as a death
  wish) - a check of this world's own licensed corpus and its own window boundary, run at review
  (confirmation pass) because no cell-scoped search had been documented for this honest-limited cell"
channel: "grep -in 'tortur|slave|martyr|rack|scourge' against every file already licensed in this
  world's own source records in cic/texts, plus a check of the window boundary itself (312-451) against
  the cell's own subject matter, 2026-08-22"
result: found
found_sources: [ijc.source.lactantius-de-mortibus]
note: "Corrected at a second follow-up confirmation review (2026-08-22): this record originally claimed
  'no other licensed source reaches back before 312' - false. ijc.source.lactantius-de-mortibus is
  licensed whole, not narrowly (contrast ijc.source.augustine-confessions, explicitly 'Book 9 ch. 7 ONLY');
  De Mortibus ch. XXIII, within that license, is a continuous pre-312 narrative and does contain
  torture-extracted testimony from enslaved persons ('the most trusty slaves compelled by pain to bear
  witness against their masters... men were tortured to speak against themselves'), plus martyrdom
  material at ch. XVI. This world's window (312-451) simply does not draw on that material - a deliberate
  scope choice, not an absence of access. CONSEQUENCE: ijc.limit.earlier-windows's honest limit
  stands on its real ground - a window judgment ('those questions belong to the age of persecution, and
  our world begins where that age ends') - not on the stronger and false claim that the material is
  unreachable in the licensed corpus."
---
Added at a follow-up confirmation review (2026-08-22) per that
review's M7 finding - see ijc.search.c-p-negative-sweep for the shared
root-cause statement. This cell's honest_limit differs from the other
four in kind: its absence is a window-boundary fact (this world begins
in 312, the cell's questions concern before), not a corpus-coverage gap
- material on this cell's exact subject matter does sit inside the
licensed corpus (De Mortibus, pre-312), but this world's own window
does not reach for it, which is the honest_limit's real and sufficient
ground.
