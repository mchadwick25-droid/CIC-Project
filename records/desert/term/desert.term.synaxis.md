---
id: desert.term.synaxis
world_id: desert-monasticism
record_type: term
schema_version: 2
status: draft
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
  do_not_retrieve_when:
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
---
Re-derived from Doc_06 SS2.6 (Tier 2; tags SC PV RT; retrieval tier 1
here because the F3-I gathering question retrieves it directly).
Strand attribution fenced both ways (Strand C's name; Strand B's
different rhythm). Liturgical-content thinness (Doc_02 SS4/SS9)
carried in the evidential sense.

Step3a Review Round 1, Finding 1: reworded the evidential sense to
drop "vendored, directly-checked" in favor of in-world evidence talk.

Step3a Review Round 4, Finding S1: the evidential sense's "the Strand
C settlements" used this build's own lettered taxonomy with no legend
in the field - reworded to name the three settlements directly.

Step3a Review Round 5, Finding C6: the informational sense's "resident
elders" substituted for what Palladius actually names - eight priests,
an office - cutting against this lexicon's own office-vs-elder-
authority distinction maintained elsewhere (geron-abba-amma, koinonia).
Corrected to "the priests who served it," matching the evidential
sense's own "eight priests" already on record.

SUPPLEMENTAL SOURCE REVIEW (2026-09-09, this build's own new addition,
not a Doc_02 finding): desert.source.cassian-institutes was already
vendored and compiled for this world but only Book IV (the fear-of-the-
Lord ladder) had been drawn on; Books II-III, the actual canonical-
psalmody content, sat unused despite Doc_02 SS4 naming exactly this gap
("what was actually prayed, beyond the Psalter and the Lord's Prayer").
Added Institutes II.5 and II.18 as sources, with two new illustrating
quote records. Deliberately did NOT upgrade formation_confidence or
citation_specificity on the strength of this addition: Cassian is one
later, Gaul-facing, systematizing voice claiming pan-Egyptian
uniformity, not a second Nitria/Kellia/Scetis eyewitness the way
Palladius is - the thinness this world names is about content, which
this addition genuinely deepens, not about strand-specific attestation,
which it does not resolve.

ROUND-2 ADDITION (2026-09-09, after independent adversarial review):
the review found a better, more directly on-point passage one chapter
away from II.5 - Institutes II.10, where Cassian himself names and
glosses the word "synaxes." Added as desert.quote.so-perfectly-silent.
The review also flagged, as a separate and not-yet-acted-on finding,
that other already-vendored desert sources with a stated purpose
(desert.source.jerome-de-viris, desert.source.jerome-letter-22,
desert.source.athanasius-festal-letters) sit uncited by any record
their own discovery_channel names them for - outside this term's own
scope, logged in this world's own decision log rather than chased here.
