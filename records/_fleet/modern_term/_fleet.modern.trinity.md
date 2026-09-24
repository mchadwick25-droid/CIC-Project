---
id: _fleet.modern.trinity
world_id: _fleet
record_type: modern_term
schema_version: 2
display_terms: ["Trinity", "Trinitarian"]
origin_year: 325
modern_sense: "The developed doctrine that God is three co-equal, co-eternal persons in one being, as formalized at Nicaea and after."
underlying_subject: "how this world's people understood the relation of the Father, the Son, and the Spirit, in their own words"
distinguishing_claim: "The word 'Trinity' itself is older than the doctrine modern_sense names: Theophilus of Antioch uses it first, c. 169-188 CE, for a triad of God, His Word, and His Wisdom (the earliest surviving use); Tertullian uses it in Latin from 208 CE on, arguing one substance in three Persons against a rival reading. The developed doctrine the modern word now names - three co-equal, co-eternal persons in one being - takes shape at Nicaea (325) and after. Whether Theophilus's own triad is the same referent as that later doctrine is a contested scholarly question, not settled here (_fleet.contested.theophilus-triad-referent). Either way, the Facilitator strips the modern label and passes the underlying subject to the voice term-free (spec §5 bridge)."
native_subject_map:
  fix: fix.term.the-three
sources:
- source_id: _fleet.source.theophilus-to-autolycus
  locus: "Book II.15 - \"are types of the Trinity, [Τριάδος] of God, and His Word, and His wisdom\"; editor's note: \"The earliest use of this word 'Trinity'\""
  license: public-domain
- source_id: _fleet.source.tertullian-against-praxeas
  locus: "chapter 2 - \"which distributes the Unity into a Trinity\"; editor's note: \"Probable date not earlier than a.d. 208\""
  license: public-domain
---
Fleet-wide bridge record (Artifact-1 §4). Paired with _fleet.canon.c-t-01 so the
fixture world can exercise the modern-term bridge routing described in Artifact-4 §3
step 3, once M4/M5 runtime exists (stage 5). Not itself a gated M1 record type beyond
schema validation - included now so the fixture world's term coverage
(fix.term.the-three) has a real bridge target to point at.

origin_year names when the modern sense in modern_sense took shape (formalized at
Nicaea, 325, and after) - not when the display word was first attested. The word and
the doctrine it now names have different histories; both are on the record, in
distinguishing_claim and the two vendored sources above, rather than conflated into
one date.
