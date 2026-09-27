---
id: desert.quote.the-kingdom-is-apatheia
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: [F4-P, F1-I]
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Contested
  divergence_note: "Contested. The Praktikos is securely Evagrius's own work and the wording is verbatim from the vendored file, but three bounds ride with it. Evagrius is this world's most atypical participant by education - a Cappadocian-formed theologian at Kellia, not a Coptic-speaking villager - so his system is the most systematic thing this world produced and the least representative of it. His speculative works were condemned in 553, well outside this world's own window, which shaped what survives and in which language. And the English is Luke Dysinger's, held under the Guide to Evagrius Ponticus's CC BY 4.0 licence, not a public-domain text - see desert.source.evagrius-praktikos."
sources:
- source_id: desert.source.evagrius-praktikos
  locus: "Praktikos chs. 2-3, in Luke Dysinger's English (cic/texts/evagrius_praktikos_dysinger.txt)"
  address: "cic:evagrius_praktikos_dysinger.txt:2-3"
  license: cc-by-4.0
text: "The Kingdom of Heaven is apatheia (dispassion) of the soul together with true knowledge of beings...The Kingdom of God is knowledge of the Holy Trinity exercised according to the capacity of the nous (mind/intellect) and bestowing incorruptibility upon it"
modern_rendering: >-
  The Kingdom of Heaven is apatheia, dispassion of the soul, together with true
  knowledge of beings. ... The Kingdom of God is knowledge of the Holy Trinity. This
  knowledge is exercised according to the capacity of the nous, the mind, and bestows
  incorruption upon it.
speaker_or_author: Evagrius Ponticus, in the Praktikos
license: verbatim
modern_lens_note: "'Apatheia' is not apathy and 'the Kingdom of Heaven' here is not a place or a future reward - both are states of a soul, described in the present. The pairing of the two chapters is Evagrius's own distinction, not a conflation made here: the Kingdom of Heaven is apatheia with true knowledge of beings, the Kingdom of God is knowledge of the Trinity."
retrieval:
  tier: 1
  retrieve_when:
  - "participant asks what the kingdom of heaven meant to this world"
  - "participant asks what apatheia is, or whether you stopped feeling things"
  - "participant asks what this world thought the point of it all was"
relations:
- type: associated-with
  target: desert.term.apatheia
- type: associated-with
  target: desert.dw.god
---
Two consecutive chapters kept together because separating them loses the distinction they are drawn
to make. This is also the sharpest instance of what desert.voice.craft's own thinness note warns
about: the most systematic interior psychology this world produced rests on one unusually educated
participant's own writing, and a participant who takes this as what the desert believed has taken
Evagrius for the movement.

These are two separate, sequentially numbered chapters (2 and 3) of the Praktikos; the `text` field
marks the chapter boundary with an ellipsis rather than joining them with no mark at all. The
record's own gloss already treats them as Evagrius's own paired-but-distinct chapters, not a single
continuous sentence, matching what the text field's punctuation now shows.
