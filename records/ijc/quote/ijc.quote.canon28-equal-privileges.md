---
id: ijc.quote.canon28-equal-privileges
world_id: imperial-juridical
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F6-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: ijc.source.chalcedon-acts
  locus: Canon XXVIII (npnf214 lines 22223-22232)
  license: public-domain
text: For the Fathers rightly granted privileges to the throne of old Rome, because it was the royal city.
  And the One Hundred and Fifty most religious Bishops, actuated by the same consideration, gave equal
  privileges...to the most holy throne of New Rome, justly judging that the city which is honoured with
  the Sovereignty and the Senate, and enjoys equal privileges with the old imperial Rome, should in
  ecclesiastical matters also be magnified as she is, and rank next after her
speaker_or_author: "The Council of Chalcedon (451), Canon 28"
license: verbatim
modern_lens_note: >-
  'The Fathers' here means the bishops of an earlier council, a loose conciliar usage - not the
  later, fixed canon of named 'Church Fathers' a modern reader may know from patristics.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how the great cities ranked against each other"
  - "participant asks whether a council could raise one see over another"
relations:
- {type: illustrates, target: ijc.force.leo-rejects-canon-28}
---
Text verified verbatim against the vendored file 2026-08-21 (the
edition's inline Greek gloss "(ἴσα πρεσβεῖα)" after "equal privileges"
omitted from the quotable text; quoted through "rank next after her" -
the canon continues into jurisdictional specifics). The claim's most
consequential sentence: even OLD Rome's privileges are here said to
rest on its having been the royal city - the premise Leo's rejection
letters deny root and branch.

Quote-verbatim gate fix (2026-09-22): the Greek gloss's omission was already disclosed above but not
marked in the `text` field itself, which just skipped straight from "privileges" to "to the most holy
throne" with no gap noted. Added an ellipsis there rather than leaving it silent - the gloss stays
excluded exactly as already decided, now honestly marked.
