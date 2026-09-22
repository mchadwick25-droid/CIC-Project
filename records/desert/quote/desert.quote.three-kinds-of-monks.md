---
id: desert.quote.three-kinds-of-monks
world_id: desert-monasticism
record_type: quote
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-I
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'Piamun is describing the orders as an anchorite recommending anchoritism, and
    Cassian records it while himself moving toward the cenobitic life he would found in Gaul. The
    three-part scheme is a participant''s account with a preference in it, not a neutral taxonomy.'
sources:
- source_id: desert.source.cassian-conferences
  locus: 'Conference XVIII (Conference of Abbot Piamun), ch. IV, Of the three sorts of monks which there
    are in Egypt (npnf211 line 42454)'
  license: public-domain
text: >-
  There are three kinds of monks in Egypt, of which two are admirable, the third is a poor sort of
  thing and by all means to be avoided. The first is that of the Coenobites, who live together in a
  congregation and are governed by the direction of a single Elder; and of this kind there is the
  largest number of monks dwelling throughout the whole of Egypt. The second is that of the anchorites,
  who were first trained in the Coenobium and then being made perfect in practical life chose the
  recesses of the desert; and in this order we also hope to gain a place. The third is the reprehensible
  one of the Sarabaites.
speaker_or_author: Abbot Piamun, as Cassian records him
license: verbatim
modern_lens_note: >-
  A coenobium is a common house under one elder; an anchorite lives apart. Sarabaites, in Cassian's
  account, are monks under no elder and no rule, living as they please - the word is a slur and he
  means it as one. The claim that anchorites are trained in the coenobium first is contested: it is
  how Cassian's informants ordered it, not how every Egyptian monk actually came to the desert.
retrieval:
  tier: 2
  retrieve_when:
  - "participant asks whether everyone lived the same way or there were different kinds"
  - "participant asks about the difference between living alone and living together"
  - "participant asks whether some ways of living were looked down on"
relations:
- {type: illustrates, target: desert.gravity.withdrawal}
---
Verified verbatim against the vendored file 2026-08-27 at npnf211 line
42454. DISCLOSED: the ANF's inline cross-reference "See the note on c.
vii." follows "Sarabaites" and is excised; the ligature in "Coenobites" is
rendered as "oe" throughout; and TWO COLONS ARE RENDERED AS SEMICOLONS
("a single Elder; and of this kind", "recesses of the desert; and in
this order"), because a colon followed by a space is not legal inside a
YAML plain scalar. That is a punctuation substitution, which is exactly
what the milan-edict review caught being done silently, so it is stated
here. Nothing else is altered.

THIS WORLD'S OWN THREE-STRAND STRUCTURE IS THIS PASSAGE. The build
carries Strand A (anchoritic, Pispir and the inner mountain), Strand B
(cenobitic, Tabennesi and the Pachomian federation) and Strand C
(semi-anchoritic, Nitria, Kellia, Scetis). That division comes from
here. It had been resting on an unreadable corpus and on modern
scholarship; the sentence it derives from was vendored the whole time.

WHAT MAKES IT EVIDENCE RATHER THAN A DIAGRAM, and why the divergence
note matters: Piamun is not neutral. He is an anchorite arguing that the
anchoritic life is the higher one, to a listener who says openly that
"in this order we also hope to gain a place." Cassian then went to Gaul
and founded coenobia. The scheme survives because it is useful, but a
world that presented it as a flat description would be repeating a
recruitment argument as though it were a census.
