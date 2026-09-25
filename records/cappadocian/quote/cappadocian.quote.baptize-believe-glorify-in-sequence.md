---
id: cappadocian.quote.baptize-believe-glorify-in-sequence
world_id: cappadocian-trinitarian
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: cappadocian.source.basil-on-the-holy-spirit
  locus: "On the Holy Spirit, ch. 27, sec. 68 (npnf208_basil-letters-select-works.xml)"
  license: public-domain
text: >-
  They must now instruct us either not to baptize as we have received, or not to believe as we were
  baptized, or not to ascribe glory as we have believed.
speaker_or_author: cappadocian.figure.basil
license: verbatim
modern_lens_note: >-
  A modern reader might hear "we must believe as we are baptized" as meaning belief is judged by ritual
  compliance alone. Basil's own point runs the other way: baptism, belief, and the ascription of glory are
  three public commitments in one unbroken sequence, so rejecting his doxology on the ground that it lacks
  written authority - by his own logic - means also being willing to reject baptism or the confession of
  faith themselves, not merely disagreeing over one word.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks why this world treated baptism, belief, and giving glory as one connected argument"
  - "participant asks what made changing one word in a prayer serious enough to be called heresy"
relations:
- type: associated-with
  target: cappadocian.gravity.triune-confession
modern_rendering: >-
  Now they must teach us one of these things. Either we should not baptize the way baptism was handed
  down to us. Or we should not believe the way we were baptized. Or we should not give glory the way we
  have believed.
---
Verified directly against cic/texts/npnf208_basil-letters-select-works.xml. `grep -n "They must now
instruct us"` returns one hit, line 14168, inside sec. 68 (`id="vii.xxviii-p29"`), within chapter 27
(`id="vii.xxviii"`, "Of the origin of the word 'with,' and what force it has. Also concerning the unwritten
laws of the church."). A distinct excerpt from the same chapter already quoted elsewhere in this world's
record set - cappadocian.quote.what-is-the-written-source (sec. 67) and cappadocian.quote.we-look-to-the-east
(sec. 66) - sharing no sentence or clause with either.

Normalization: the source's own line-wrap breaks inside the passage are joined with single spaces. No
wording added, dropped, substituted, or reordered.
