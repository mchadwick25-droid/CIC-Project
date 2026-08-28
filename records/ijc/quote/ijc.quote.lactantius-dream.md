---
id: ijc.quote.lactantius-dream
world_id: imperial-juridical
record_type: quote
schema_version: 2
status: draft
register: emic
canon_cells:
- F3-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: illustrative
  formation_confidence: Contested
  divergence_note: null
sources:
- source_id: ijc.source.lactantius-de-mortibus
  locus: '44 (anf07, ch. XLIV division at line 10612; the quote itself at line 10620)'
  license: public-domain
text: Constantine was directed in a dream to cause the heavenly sign to be delineated on the shields
  of his soldiers, and so to proceed to battle. He did as he had been commanded, and he marked on their
  shields the letter Χ, with a perpendicular line drawn through it and turned round thus at the top,
  being the cipher of Christ.
speaker_or_author: "Lactantius, De Mortibus Persecutorum"
license: verbatim
modern_lens_note: >-
  The described sign ('the letter [Chi], with a perpendicular line drawn through it and turned round
  thus at the top') is the Chi-Rho monogram - a modern reader unfamiliar with that symbol may not
  picture what is actually being described.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how the emperor came to favour the Christians"
  - "participant asks whether the conversion story can be believed"
  do_not_retrieve_when: []
relations:
- {type: illustrates, target: ijc.story.dream-before-battle}
---
Text verified verbatim against the vendored file 2026-08-21. Corrected
at review (Opus quote-fidelity pass, 2026-08-21): the file prints the
actual Greek letter chi (Χ, U+03A7), not a Latin "X" - this record had
silently substituted the Latin letter without disclosing the
substitution. The Greek character is now reproduced as printed; the
file also shows the fuller Chi-Rho ("ΧР") that follows in the same
sentence, not quoted here since this record's span ends at "Christ."
The earlier of the two conversion accounts - a
dream, the night before, on the shields - written within a few years of
the event by a Christian at court. Not reconcilable in detail with
Eusebius's mid-day vision; see ijc.contested.constantine-conversion.
