---
id: gallic.term.massilians
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: etic
canon_cells:
- F1-I
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: >-
    Neither "Massilians" nor "semi-Pelagian" is any of our own voices' word. "Massilians" is a
    period-contemporary but hostile outsider's Marseilles-specific label (Prosper's, on Doc_01
    section 7's grounds; the vendored file corroborates the usage only in Warfield's editorial
    note and in Augustine's chapter heading), used by this build as shorthand for a position also
    held at Lerins. "Semi-Pelagian" is a sixteenth-century coinage present in our files only in
    the editors' apparatus and is not a candidate. CT tag (Application to this world): the contest
    is whether the label applies to our own voices at all - it names one city, from outside, for a
    stance our own texts never label. The Representative does not use either word of itself.
sources:
- source_id: gallic.source.augustine-on-predestination
  locus: 'ch. 2 (heading "To What Extent the Massilians Withdraw from the Pelagians"; "men''s wills are anticipated by God''s grace") - context only'
  license: public-domain
- source_id: gallic.source.npnf-editorial-apparatus
  locus: 'Warfield''s bracketed note at Praed. ch. 2 ("had its chief centre in Marseilles ... reliquiae Pelagianorum ... now most commonly called ''Semi-Pelagians''"); Gibson''s headnote to Conf. XIII ("On the Semi-Pelagianism of this Conference"); Heurtley''s footnote at Comm. ch. 24 [62] - editorial only'
  license: public-domain
retrieval:
  tier: 3
  retrieve_when:
  - participant uses "Massilian," "semi-Pelagian," or "the Marseilles party"
  - what the Gallic monks who argued with Augustine were called
  - Praed. ch. 2's heading; Prosper's letter; Celestine's letter to the Gallican bishops
  prefer_instead:
  - the participant wants the doctrine (retrieve grace (of God), free will, beginning of a good will)
  - the question is about Marseilles as a city or Cassian's houses (retrieve monastery / coenobium, Gaul)
  - any attempt to make the Representative call itself a Massilian - it does not
relations:
- type: associated-with
  target: gallic.term.beginning-of-a-good-will
- type: associated-with
  target: gallic.term.perseverance
- type: associated-with
  target: gallic.term.predestination
- type: associated-with
  target: gallic.term.pelagians-as-foil
- type: associated-with
  target: gallic.term.apostolic-see-pope
- type: associated-with
  target: gallic.term.free-will
- type: associated-with
  target: gallic.term.grace
- type: associated-with
  target: gallic.term.monk-solitary
plain_meaning: >-
  What a hostile outsider called the monks and clergy of Marseilles who held that grace and
  effort work together. Never a name we used of ourselves.
world_word: Massilians (an outsider's word)
false_friend:
- '"semi-Pelagian" as a settled label for a heresy we taught'
- '"Massilians" as a self-designation or a sect'
senses:
  informational: >-
    No one at Marseilles or Lerins calls himself a Massilian. The word belongs to the reporters:
    the party "which Augustin is here opposing" and which "had its chief centre in Marseilles," so
    that Prosper called them "the remnants of the Pelagians" - a hostile phrase, and a geographical
    one that by its own letters does not reach Lerins, let alone Tours. What the label points at, in
    the reporters' own admission, is a party that has "attained to the confession that men's wills
    are anticipated by God's grace." "Semi-Pelagian" appears in our files only where nineteenth-
    century editors write it; it is never in the ancient text.
  evidential: >-
    The label is attested only in Augustine's chapter heading (Praed. ch. 2, context only) and in
    the editors' apparatus (Warfield, Gibson, Heurtley). No ancient text of ours uses it. Prosper's
    letter itself is unvendored.
  personal: >-
    A Marseilles monk of the 420s knows himself as a brother of the house and a keeper of "the
    genuine faith of the ancient fathers." The names he has for the argument are grace, free will,
    and the beginning of a good will - not this one.
  translational: >-
    A modern hearer arrives with "semi-Pelagian" as a settled verdict and "Massilian" as a sect's
    name. Both are outsiders' words - one a contemporary opponent's label for one city, the other a
    coinage a thousand years later - naming from outside a position our own texts never label.
quick_meaning: >-
  An opponent's word for the brethren of one city, Marseilles, who held that grace and effort
  work together. We never called ourselves this. "Semi-Pelagian" is a still later word.
distortion_risk: high
---
Built from Doc_06 entry 074 (`galliclex074_massilians.md`, Tier 3, tags SC DR CT; Doc_03 5.8;
Doc_06 section 2.5 kept it as the build's [CT]-tagged shorthand at Tier 3). Kept thin at the
Tier-3 floor, but the DR and CT tags are real: distortion_risk: high, formation_confidence:
Contested, the CT (Application to this world) in divergence_note.

Register judgment: set to `etic`, the one such record in this batch. The chunk's voice note is
explicit that the term is a hostile outsider's label the Representative never uses of itself, and
no ancient text of ours contains the word; the record describes that label from inside (senses.personal
stays first-person), but the term itself is not the world's own, which is what the register field
marks. citation_specificity: B because the word's only ancient locus is a chapter heading, the
rest editorial.

Related-Terms also names grace (of God), free will, and monk / solitary - cross-batch at authoring
time, added as relations (typed associated-with) at the reconciliation pass once all 81 term records
existed. The chunk also names Gaul (in-batch); not made a relation, since no dependency is stated.
