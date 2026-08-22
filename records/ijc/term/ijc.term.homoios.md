---
id: ijc.term.homoios
world_id: imperial-juridical
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells:
- F1-I
- C-T
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: ijc.source.hilary-de-synodis
  locus: the quoted creed formulae ("like the Father", from npnf209 line 8067)
  license: public-domain
- source_id: ijc.source.auxentius-letter-ulfila
  locus: the fragment (referenced-only; no quotation licensed)
  license: referenced-only
- source_id: ijc.source.socrates-he
  locus: II (the councils of Ariminum and Seleucia; the Constantinople creed of 360)
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - '"Arianism" in connection with this world'
  - what the imperial church believed under Constantius II or Valens
  - why orthodoxy seems to shift with the reigning emperor
  - Ambrose's confrontation with Justina's court
  do_not_retrieve_when:
  - the question is about Arius's own original teaching, which this world's record does not directly reconstruct
relations:
- {type: associated-with, target: ijc.term.homoousios}
- {type: associated-with, target: ijc.term.haeresis}
plain_meaning: '"Like the Father." The confession that the Son is like the Father, as the scriptures say - and no
  further word about shared being. For years the imperial church itself held this, at the emperor''s command.'
world_word: homoios
false_friend:
- '"Arian" as a slur for a fringe, always-defeated heresy - for about two decades this was the establishment,
  not the fringe'
- a simple denial that the Son is divine (its advocates claimed the opposite, on scriptural grounds)
senses:
  informational: 'The Homoian confession: the Son is like the Father, per the scriptures - deliberately
    refusing both "of one substance" and "of a different substance" as words scripture does not use. Under
    Constantius II and again under Valens this was the confession the empire enforced; bishops who refused
    it were removed and exiled.'
  evidential: 'The formulae themselves survive quoted at length by Hilary of Poitiers, a contemporary opponent
    writing to explain them to Gaul; one precious fragment of Homoian self-testimony (a pupil''s letter
    on Ulfila) survives, nearly erased, in a single manuscript. Almost everything else comes through the
    winning side''s later historians - so what Homoians precisely held is reconstructed, and the reconstruction''s
    limits are stated, not hidden.'
  personal: A bishop ordained in those decades could hold this confession because it was the imperial
    church's own establishment at the time, not a formal subscription his ordination required - the hard,
    honest memory is that the line between faithfulness and error ran through the church's own
    establishment, not between the church and outsiders.
  translational: '"Did a council vote Jesus into being God?" - the real history is harder: the disputed
    word was argued, enforced, reversed, and re-enforced across half a century, in both directions, with
    the state''s weight behind whichever confession the reigning emperor held.'
quick_meaning: The teaching that the Son is "like" the Father - for years the empire's own official faith.
---
Rebuilt from the reviewed legacy lexicon (Doc_06 Tier 1;
Lexicon-Chunks/ijclex003_homoios.md) - the binding Homoian-recentering
obligation (Step 0 SS4.1) carried into the lexicon itself. The legacy
chunk's Reported-Experience Status is carried here as the confidence
block (Widely Accepted, not Documented, for the position's internal
logic) plus ijc.contested.homoian-content, which holds the
mechanism-vs-content divergence open as first-class data. Sources
improve on the legacy chunk: Hilary's De Synodis (vendored, this
build's registry append) gives directly quotable access to the
formulae that the unvendorable Auxentius fragment cannot. Hanson (1988)
remains the standard modern reconstruction, referenced here, never
quoted. canon_cells: F1-I (what did you argue about among yourselves;
what did the councils decide), C-T (was Jesus God - this term is the
window's live counter-position).
