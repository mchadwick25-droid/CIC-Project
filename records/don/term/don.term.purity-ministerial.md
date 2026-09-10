---
id: don.term.purity-ministerial
world_id: donatism
record_type: term
schema_version: 2
status: draft
register: emic
canon_cells: []
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: 'Same split as traditor-traditio, from the same Doc_04 SS3.1 finding: the doctrine''s existence
    is Documented on cross-voice grounds (Petilian''s own quoted proposition, re-verified directly against the
    vendored npnf104 file at line 10280), while the specific argumentative texture survives substantially inside
    Augustine''s refutation. Doc_06 SS1 keeps this at Tier 2 deliberately: Doc_04 and Doc_05 forward Traditor/Traditio
    itself for Tier-1 depth, not this broader doctrinal restatement of the same ground, so this record carries
    the doctrine and defers the founding accusation''s own depth to that term.'
sources:
- source_id: don.source.augustine-answer-to-petilian
  locus: '''Conscientia namque dantis attenditur, quae abluat accipientis'''
  license: public-domain
- source_id: don.source.cyprian-epistles
  locus: the third-century African purity theology this position sharpens rather than invents
  license: public-domain
- source_id: don.source.cyprian-de-lapsis
  locus: the lapsed-clergy question that stands behind the whole dispute
  license: public-domain
- source_id: don.source.augustine-on-baptism-against-the-donatists
  locus: the sustained refutation, which preserves the position it attacks
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - a participant asks whether a minister's own life affects whether a sacrament works
  - a participant asks where this teaching came from before the schism
  - the conversation reaches Cyprian, or the doctrinal ground under the rebaptism practice
  do_not_retrieve_when:
  - '''purity'' is being used for personal moral holiness with no bearing on sacramental validity'
relations:
- type: presupposed-by
  target: don.term.traditor-traditio
- type: presupposed-by
  target: don.term.rebaptism
- type: tension-with
  target: don.term.reception-without-reordination
plain_meaning: What makes a sacrament real is not the water alone. It is the conscience behind the hand. 'We look
  to the conscience of the giver, to cleanse that of the receiver.' A hand that is not clean has nothing to give
  away.
world_word: conscientia dantis ("the conscience of the giver")
false_friend:
- personal moral purity in the modern devotional sense, a matter of private holiness
- ritual or bodily cleanness in the Levitical sense
- a novelty invented in 311 -- this sharpens Cyprian's own third-century African position
- a claim that a sinful minister invalidates everything, rather than one about a broken ordination line
senses:
  informational: 'Sacramental validity is held to depend on the minister''s own standing -- specifically on freedom
    from traditio and from ordination by a traditor. Petilian of Constantina puts it in one clause: what is looked
    to is the conscience of the giver, to cleanse that of the recipient. This is a direct sharpening of Cyprian''s
    mid-third-century African teaching, not an innovation of 311/312, which is part of why the position felt to
    its holders like the older and more African one.'
  evidential: 'Documented in existence, cross-voice attested: the clause is Petilian''s own and was checked directly
    against the vendored text, and the Maximianist affair presupposes the doctrine independently of anything Augustine
    says about it. Augustine-mediated in texture -- the full chain of reasoning as it can now be reconstructed
    comes through the refutation that preserved it.'
  personal: This is what an ordinary believer is actually deciding when choosing whose hands to be baptized by.
    The doctrine is not the property of theologians here; it is the reason a person walks to one font and not
    another.
  translational: '''Doesn''t a sacrament work regardless of the priest?'' -- that answer became the mainstream
    one later, and it is exactly what was denied here. From inside, saying the minister does not matter makes
    the surrender of the scriptures a private failing with no public consequence, and that is the concession this
    communion existed to refuse.'
quick_meaning: The conscience of the giver. A hand that is not clean has nothing to give.
distortion_risk: high
---
Built from Doc_06 SS1 entry 004 (Tier 2 -- doctrinal ground shared with Traditor/Traditio, which carries the Tier-1 depth). No deployment chunk built this cycle (Doc_06 SS3). Confidence split carried from Doc_04 SS3.1.
