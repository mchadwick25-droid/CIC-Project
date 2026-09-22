---
id: ijc.term.communio
world_id: imperial-juridical
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F3-I
- F4-I
- F5-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: null
sources:
- source_id: ijc.source.leo-letters
  locus: Ep. XXVIII and CIV-CVI (communion-standing as the operative category)
  license: public-domain
- source_id: ijc.source.ambrose-epistles
  locus: Ep. LI (exclusion from the offering as episcopal leverage)
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - what "excommunicated" or "in communion" meant in this world
  - how a bishop's authority was actually enforced
  - a specific dispute's mechanics (Damasus and Ursinus, the Canon 28 refusal, the exclusion of an emperor)
  prefer_instead:
  - the question is about the Eucharist as sacramental rite rather than communion as standing with a see
relations:
- {type: associated-with, target: ijc.term.primatus}
- {type: associated-with, target: ijc.term.haeresis}
- {type: associated-with, target: ijc.term.presbeia}
- {type: associated-with, target: ijc.term.imperator-intra-ecclesiam}
- {type: associated-with, target: ijc.term.tomus}
- {type: associated-with, target: ijc.term.basilica}
plain_meaning: 'Communion as standing. To be in communion with a church is to stand where it stands - at its altar,
  and inside its recognition. To be cut off is a public fact with real force.'
world_word: communio
distortion_risk: medium
false_friend:
- communion as only the private reception of the bread and cup
- a merely social or emotional sense of fellowship
senses:
  informational: 'The operative mechanism of church authority in this world: claims bind through who is
    received into fellowship and who is placed outside it. Whole sees, whole regions, and once an emperor
    himself stood inside or outside communion, and the difference carried real force.'
  evidential: 'Leo''s letters use communion-standing as their working category throughout; Ambrose''s letter
    to Theodosius shows a bishop suspending an emperor''s access to the offering as real leverage. The
    record shows the mechanism from both directions: wielded, and refused.'
  personal: 'To be placed outside was to lose the altar and the recognition of the churches at once - the
    record shows people fighting, negotiating, and writing at length to avoid or reverse it, which is
    its own evidence of how much it weighed. What held distant believers together at all was this same
    mechanism working the other way: a letter of communion carried a see''s recognition across hundreds
    of miles, the actual thread connecting congregations who would never meet - the record''s own answer
    to what bound people together across distance.'
  translational: '"Excommunication" here is not a private spiritual note on a membership roll - it is closer
    to losing citizenship in a public body whose recognition made claims real, without ceasing to be a
    sacramental fact.'
quick_meaning: Standing with a church - to be received at its altar and counted as its own, or cut off from both.
---
Rebuilt from the reviewed legacy lexicon (Doc_06 Tier 1;
Lexicon-Chunks/ijclex004_communio.md). Source discipline carried from
the chunk: the contested Damasine decretal block is not cited; Leo's
securely-attested letters anchor the term, with Ambrose Ep. 51 added by
this build as the mechanism's clearest single exercised instance
(registry-supported; the legacy chunk's own Related-Terms already tied
communio to the Ambrosian material). canon_cells: F3-I (who held
authority and how it was enforced), F4-I (when someone wronged the
community, how was it handled - and could they come back: exclusion and
restoration is this world's documented answer-shape). Added at review
(Opus canon-structure pass, 2026-08-21): F5-P (what held distant
believers together) - the same communion-standing mechanism that
excludes also connects; this term was answering the question untagged.
