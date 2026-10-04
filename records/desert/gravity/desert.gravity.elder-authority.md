---
id: desert.gravity.elder-authority
world_id: desert-monasticism
record_type: gravity
schema_version: 2
status: ready
register: etic
canon_cells: [F3-I, F6-P]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: desert.source.apophthegmata-patrum
  locus: "the collection's entire organizing structure - by elder name"
- source_id: desert.source.palladius-lausiac-history
  locus: "elder authority in practice (e.g. Pambo, ch. X); also ch. XXXII, the Tabennesiot rule report grounding this record's Rule-content contrast"
  license: public-domain
- source_id: desert.source.pachomian-corpus
  locus: "the Rule's contrasting office-based model, as Palladius reports it; also the second attesting stream (alongside the Apophthegmata) answering the Rubenson/Antony-literacy Cross-Check question, matching desert.gravity.withdrawal's own use of this source for the identical question"
relations:
- type: associated-with
  target: desert.gravity.withdrawal
- type: associated-with
  target: desert.gravity.spiritual-combat
- type: associated-with
  target: desert.gravity.diakrisis
- type: tension-with
  target: desert.gravity.authority-tension
- type: associated-with
  target: desert.term.geron-abba-amma
- type: associated-with
  target: desert.contested.antony-literacy
- type: associated-with
  target: desert.figure.sarah
- type: associated-with
  target: desert.force.martyrdom-unavailable
- type: illustrated-by
  target: desert.story.sarah-answer
- type: associated-with
  target: desert.quote.sarah-man-among-you
- type: illustrated-by
  target: desert.quote.talida-key-never-taken
name: "Elder-mediated oral authority [PRIMARY]"
description: >-
  Authority here was earned by proven discernment and passed on through a bond
  between two people, in the address of geron, abba or amma. In the anchoritic
  and semi-anchoritic strands it was the main kind of authority. In the
  cenobitic strand it was present but ranked below the Rule. The clearest
  trace of it is the way the sayings are ordered, by the names of elders. But
  that order is the later compilers' own plan, so it does not record how
  authority worked as it was lived. Teaching and training rest on it. It
  explains why there was no tradition of general treatises outside Evagrius.
  It appears in every strand, though its weight differs. It supports
  discernment. Scholars widely accept all of this. It is one side of a
  tension over authority. The other side is the Pachomian Rule's office-based model. It answers one
  historical pressure, the end of martyrdom, and it grew stronger under that
  pressure.
classification: primary
manifestations:
- "the Apophthegmata's alphabetical and systematic organization by named elder - the compilers' own later arrangement, not a neutral record of authority's shape in real time"
- "Palladius's account of Pambo, whose answers were received 'as come from God, so carefully were they framed' (ch. X)"
- "the amma tradition (Syncletica, Theodora, Sarah) as the same authority mode attested for women, thin but genuine in the surviving record"
use_note:
  means: "Authority came through recognized discernment and personal relationship, primary among solitary and semi-solitary monks and structurally secondary to the Rule among the Pachomians."
  not_for:
    - "Presenting the sayings collection's structure as a transcript of how authority worked"
    - "Presenting elder authority as a conferred office"
    - "Presenting amma authority as well documented, when it is thin"
  years: {from: 320, to: 430}
  status: reviewed
---
Re-derived from the prior build's cleared Doc_04 SS1 candidate 3, SS2
row 3, SS3, SS4, SS5 row 3, SS6 (gravity 3). The tension-with relation
to gravity 10 (authority tension) reflects Doc_04's own finding:
gravity 10 is not a third, independent force but the named friction
between this gravity's person-based model and gravity 6's office-based
one, so this record and desert.gravity.koinonia both carry that
relation reciprocally against gravity 10 rather than against each other
directly.

The Rubenson/Antony-literacy Cross-Check tension does not threaten this
gravity's classification: elder authority is independently attested
across the whole Apophthegmata tradition and the Pachomian corpus (both
registered above), not solely through Antony's own characterization by
Athanasius, so its confidence basis does not depend on resolving that
contest - carried in full at desert.contested.antony-literacy.
desert.figure.sarah supplies the one case where the amma tradition
named in the third manifestation is made concrete by surviving material,
rather than only asserted.
