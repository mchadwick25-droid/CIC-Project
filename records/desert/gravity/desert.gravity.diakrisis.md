---
id: desert.gravity.diakrisis
world_id: desert-monasticism
record_type: gravity
schema_version: 2
status: ready
register: etic
canon_cells: [F4-I]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: desert.source.apophthegmata-patrum
  locus: "recurring across named elders, regardless of settlement"
- source_id: desert.source.cassian-conferences
  locus: "Conference II (On Discretion) - Cassian's record of the teaching"
  license: public-domain
relations:
- type: associated-with
  target: desert.dw.grace-and-effort
- type: associated-with
  target: desert.gravity.elder-authority
- type: associated-with
  target: desert.gravity.spiritual-combat
- type: associated-with
  target: desert.gravity.scriptural-engagement
- type: associated-with
  target: desert.gravity.evagrian-systematization
- type: associated-with
  target: desert.term.diakrisis
- type: associated-with
  target: desert.force.martyrdom-unavailable
- type: illustrated-by
  target: desert.story.moses-leaking-jug
- type: associated-with
  target: desert.story.sarah-answer
- type: associated-with
  target: desert.quote.moses-sins-run-out
- type: associated-with
  target: desert.quote.origen-on-the-sinning-brother
- {type: illustrated-by, target: desert.quote.discretion-greatest-prize}
name: "Diakrisis - discernment as master virtue [PRIMARY]"
description: >-
  Diakrisis is the skill of judging rightly between thoughts, practices and
  counsels, and it set the measure for every other discipline in this world.
  This world had no fixed syllabus, so discernment did the work that a course
  of study does elsewhere. It recurs across named elders and across
  settlements in the sayings, but it is not settled why. It may reflect the
  settlements, or how the later compilers arranged the sayings, or some of
  both. Cassian wrote decades later, in Latin, for a Gallic audience. He
  gives a whole Conference to it, and he says it was teaching he got in Egypt.
  Other practices need discernment to stay in balance, and it shaped monks
  directly. It explains why most surviving teaching fits a single case and not
  a system. It runs through all the strands. It also curbed the zeal of
  spiritual combat and of its Evagrian systematization, keeping both from
  excess. Scholars widely accept all of this. It answers one historical
  pressure, the end of martyrdom, and it grew stronger under that pressure.
classification: primary
manifestations:
- "the recurring narrative pattern: an eager newcomer asks an elder for an extreme practice and is redirected toward something more moderate"
- "Cassian's Conference II, devoted entirely to discretion as the teaching he received from the Egyptian elders"
- "diakrisis, like most of this world's teaching outside Evagrius, was the subject of almost no sustained treatise - Cassian's Conference II is the one exception, a retrospective account written decades after the fact, not a systematic handbook in the register of the praktike-apatheia-theoria ladder or the eight-logismoi taxonomy"
use_note:
  means: "Discernment, learned under elders, calibrated every other discipline in a world without a fixed syllabus, holding ascetic zeal back from excess."
  not_for:
    - "Presenting Cassian's Conference II as a transcript of Egyptian teaching"
    - "Presenting a sustained treatise on discernment, since almost none exists"
    - "Presenting the cross-settlement pattern as settled"
  years: {from: 320, to: 430}
  status: reviewed
---
Re-derived from the prior build's cleared Doc_04 SS1 candidate 5, SS2
row 5, SS3, SS4, SS5 row 5, SS6 (gravity 5). The fabricated "mother of
all virtues"/Cassian attribution is deliberately not reintroduced here -
Conference II is cited as Cassian's record of the teaching he received,
no epithet claimed, matching desert.term.diakrisis's own standing
discipline on this exact point.

No manifestation here names a figure or episode outside this build's
registered corpus. In particular, "Poemen" never appears: no elder by
that name has any basis anywhere in this build's registered corpus or
its vendored files (the only near-hits are "Poemenion," a place near
Bethlehem, and "Poemenia," a woman pilgrim - neither is Abba Poemen),
and this world's own live-testing history flags that name specifically
as its documented fabrication-risk case
(Build/worlds/desert/LiveTest_Scoring_Review.md; the
standing Permanent Prompt guard names Poemen categorically). The
manifestation instead names the
absence of a named systematic text for diakrisis, contrasted with the
Evagrian cluster's own registered texts (the praktike-apatheia-theoria
ladder, in which apatheia is a middle rung, not the ladder's own name) -
Cassian's Conference II is the one named exception, matching
desert.term.apophthegma's own "almost no sustained treatise" outside
Evagrius. Doc_04 SS2 row 3's own Explanatory cell treats this same
absence as itself an attested pattern, not merely a gap in this
record's own evidence.
