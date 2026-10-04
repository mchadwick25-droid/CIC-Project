---
id: desert.term.synaxis
world_id: desert-monasticism
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells: [F3-I, F4-I]
confidence:
  citation_specificity: B
  verification_state: verified-direct
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: desert.source.palladius-lausiac-history
  locus: "ch. VII (Nitria: 'They occupy the church only on Saturday and Sunday', file line 225)"
  license: public-domain
- source_id: desert.source.apophthegmata-patrum
  locus: "the weekly gathering across the Strand C sayings"
- source_id: desert.source.cassian-institutes
  locus: "Institutes II.5 (the twelve-Psalms angel legend, npnf211 line 17133), II.10 (naming and
    glossing 'synaxes' itself, npnf211 line 17396), and II.18 (not kneeling from Saturday evening to
    Sunday evening, npnf211 line 17728) - flagged content, see this record's own trailing note on
    strand-uniformity"
  license: public-domain
retrieval:
  tier: 1
  retrieve_when:
  - what actually happened when this world gathered
  - questions about worship, liturgy, or the shared meal
  prefer_instead:
  - questions about Pachomian daily communal prayer - that runs on the Rule's own rhythm, not under this name
relations:
- type: associated-with
  target: desert.term.kellion
- type: associated-with
  target: desert.story.kellia-day
- type: illustrated-by
  target: desert.quote.twelve-psalms-by-an-angel
- type: illustrated-by
  target: desert.quote.never-kneel-saturday-to-sunday
- type: illustrated-by
  target: desert.quote.so-perfectly-silent
plain_meaning: "The gathering: the weekly meeting of monks who lived alone all week. They came in for vigil, worship, and a shared meal."
world_word: synaxis
false_friend:
- a church service in the generic weekly-routine sense
senses:
  informational: "In the semi-solitary settlements, the one fixed communal point of the week: ascetics who spent the days alone in their cells came together Saturday into Sunday for vigil, worship at the church, and a shared meal, under the priests who served it. Pachomian houses had daily common prayer on a different, rule-governed rhythm - not under this name."
  evidential: "Palladius says it plainly of Nitria: the church was occupied only on Saturday and Sunday, with eight priests serving it - his own eyewitness account. The sayings tradition presupposes the same weekly shape across Nitria, Kellia, and Scetis alike. What was prayed beyond the Psalter was thin in the record until Cassian's Institutes (II.5, II.18) supplied specific content - a fixed twelve Psalms at the evening and night offices, sung seated with a closing Alleluia, and no kneeling from Saturday evening to Sunday evening - but Cassian is a single later voice writing for Gaul, generalizing to 'the whole of Egypt and the Thebaid,' not an eyewitness naming Nitria/Kellia/Scetis specifically the way Palladius does. This world treats the content as genuine but strand-uniformity as his own claim, not an independently confirmed fact."
  personal: "Its weight came from its rarity: after six days of solitude, faces, voices, bread shared - the week's whole communal life in one held breath. Absence was noticed; presence was itself a discipline."
  translational: "Not 'going to church' as a routine among routines. For the semi-solitary majority it was the only routine that gathered them at all - the seam that kept solitude from becoming isolation."
quick_meaning: "The weekly gathering - vigil, worship, and a shared meal after six days alone."
distortion_risk: medium
use_note:
  means: "The synaxis was the weekly gathering, Saturday into Sunday, when monks who lived alone came together for vigil, worship, and a shared meal."
  not_for:
    - "Hearing it as going to church as one routine among many"
    - "Applying the name to Pachomian houses, whose common prayer ran daily on a different rhythm"
    - "Filling in liturgical detail that the thin record does not give"
  years: {from: 320, to: 430}
  status: provisional
---
Re-derived from Doc_06 SS2.6 (Tier 2; tags SC PV RT; retrieval tier 1
here because the F3-I gathering question retrieves it directly).
Strand attribution fenced both ways (Strand C's name; Strand B's
different rhythm). Liturgical-content thinness (Doc_02 SS4/SS9)
carried in the evidential sense.

The evidential sense names the three settlements (Nitria, Kellia,
Scetis) directly rather than this build's own lettered taxonomy. The
informational sense names "the priests who served it," matching what
Palladius actually names - eight priests, an office - and the
evidential sense's own "eight priests" already on record.

desert.source.cassian-institutes's Books II-III, the canonical-psalmody
content, are drawn on here (Institutes II.5, II.10, II.18), closing the
gap Doc_02 SS4 names ("what was actually prayed, beyond the Psalter and
the Lord's Prayer") - alongside two illustrating quote records,
including desert.quote.so-perfectly-silent (Institutes II.10, where
Cassian himself names and glosses the word "synaxes"). This addition
deepens the content this world can show but does not resolve
strand-specific attestation: Cassian is one later, Gaul-facing,
systematizing voice claiming pan-Egyptian uniformity, not a second
Nitria/Kellia/Scetis eyewitness the way Palladius is, so
formation_confidence and citation_specificity are unchanged by it.
