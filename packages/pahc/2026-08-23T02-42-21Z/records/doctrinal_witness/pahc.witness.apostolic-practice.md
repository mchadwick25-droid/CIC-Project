---
id: pahc.witness.apostolic-practice
world_id: post-apostolic-house-church
record_type: doctrinal_witness
schema_version: 2
status: draft
register: emic
canon_cells:
- F4-E
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: "Documented that this world's own texts claim apostolic origin for their practices; Contested on whether that claim holds up under scrutiny - the Didache's own title claims apostolic authorship while its actual dating is contested (see pahc.contested.didache-dating), and none of this world's own voices offers independent proof beyond its own assertion of continuity."
sources:
- source_id: pahc.source.first-clement
  locus: "42, 44 (the explicit chain: Christ, the apostles, their own appointed successors)"
  license: public-domain
- source_id: pahc.source.didache
  locus: "its own title, 'The Teaching of the Twelve Apostles'"
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks how this world knew its practices traced to the apostles"
  do_not_retrieve_when: []
relations:
- type: associated-with
  target: pahc.force.apostolic-testimony-inheritance
- type: associated-with
  target: pahc.contested.didache-dating
positions:
- "This world claimed apostolic origin openly and by name - 1 Clement traces a direct chain from Christ to the apostles to their own appointed successors; the Didache carries the apostles' own name in its very title."
- "We have to be honest about what that claim is worth on its own: it is an assertion this world made about itself, not independent proof. Modern study of these same texts finds their own dating and authorship genuinely disputed - the Didache's own title claims the apostles even though its actual composition is contested to have come decades after them."
tensions:
- "This world cannot prove its practices trace unbroken to the apostles the way a chain of custody could - what it has is its own claim to that continuity, made confidently and repeatedly, sitting alongside real, unresolved scholarly doubt about exactly how each specific text was actually produced."
text: >
  We said it plainly, and often: what we do goes back to the apostles.
  One of us traces it as a straight line - Christ sent the apostles, the
  apostles appointed others after them, and so it continues. Our own
  teaching manual carries the apostles' name right in its title. But we
  will not pretend the claim and the proof are the same thing. The
  claim is ours, made with full confidence. Whether it holds up - when
  a text like our manual was actually written, and by whom - is a real,
  open question we cannot close for you, because we cannot close it for
  ourselves.
---
1 Clement 42/44's chain and the Didache's own title checked directly
against the vendored corpus (cic/texts/anf01_apostolic-fathers-justin-
irenaeus.xml div1 ii; cic/texts/anf07_lactantius-apostolic-
constitutions-didache-liturgies.xml div1 viii, "The Teaching of the
Twelve Apostles"). Closes the cell pahc.force.apostolic-testimony-
inheritance already grounds at the force level but cannot itself close
(canon.substantive_types() does not count force canon_cells) - this
record is that force's participant-facing completion. FIXED at Step 8
round-1 review: added a relations edge to pahc.contested.didache-dating,
already named in this record's own divergence_note prose but not
previously linked as a schema relation.
