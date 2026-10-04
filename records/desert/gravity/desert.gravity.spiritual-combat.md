---
id: desert.gravity.spiritual-combat
world_id: desert-monasticism
record_type: gravity
schema_version: 2
status: ready
register: etic
canon_cells: [F4-P]
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Widely Accepted
  divergence_note: null
sources:
- source_id: desert.source.athanasius-vita-antonii
  locus: "SS8-9 (the tombs), SS12-13 (the fort), SS23 (the general combat teaching)"
  license: public-domain
- source_id: desert.source.apophthegmata-patrum
  locus: "passim - the logismoi as the tradition's ordinary subject"
- source_id: desert.source.evagrius-praktikos
  locus: "the general combat theme, prior to its systematized form (consult-only; vendored excerpt witness via Socrates IV.23)"
relations:
- type: associated-with
  target: desert.quote.christ-worketh-them-not-we
- type: associated-with
  target: desert.quote.the-coming-of-christ-made-thee-weak
- type: associated-with
  target: desert.gravity.elder-authority
- type: associated-with
  target: desert.gravity.diakrisis
- type: precondition-for
  target: desert.gravity.evagrian-systematization
- type: associated-with
  target: desert.term.logismoi
- type: associated-with
  target: desert.figure.antony
- type: associated-with
  target: desert.force.martyrdom-unavailable
- type: illustrated-by
  target: desert.story.antony-tomb-combat
- type: associated-with
  target: desert.quote.antony-not-worsted
- type: illustrated-by
  target: desert.quote.equal-measure-of-strength
- {type: illustrated-by, target: desert.quote.eight-principal-faults}
- {type: illustrated-by, target: desert.quote.ladder-from-compunction}
- {type: illustrated-by, target: desert.quote.arch-drawn-from-the-centre}
- type: illustrated-by
  target: desert.quote.no-one-seize-the-hand
name: "Spiritual combat against tempting thoughts, general form [PRIMARY]"
description: >-
  This is the struggle against logismoi, the tempting or distracting thoughts.
  It was the ordinary subject of this world in every strand. Here it is taken
  in its general form. That is apart from the later Evagrian systematization,
  which rests on one author, so its evidence carries a different risk. The
  general struggle is attested separately in Athanasius's account, in the
  sayings, and in Evagrius's own outline. It recurs in every kind of source.
  It shapes what the teaching says and the short form of the sayings. It
  formed monks, and it explains why so much of what survives looks this way.
  It runs through all three strands. It is most developed in the
  semi-anchoritic one, but it is found in the anchoritic and cenobitic ones
  too. It backs up discernment and elder authority. Scholars widely accept all
  of this. It answers one historical pressure, the end of martyrdom, and it
  grew stronger under that pressure.
classification: primary
manifestations:
- "Antony's demonic assaults at the tombs (Vita SS8-9) and in the fort (SS12-13)"
- "the logismoi as the most common subject of the sayings tradition, recurring across named elders and settlements alike - though how far that cross-settlement pattern reflects the settlements themselves and how far it reflects the sayings' later compilers' own arrangement is not settled"
- "the terse apophthegm form itself read as a combat technique - answer, don't dwell"
use_note:
  means: "The struggle against tempting thoughts was this world's ordinary, cross-strand subject, broader than and prior to Evagrius's single-author systematization of it."
  not_for:
    - "Presenting Evagrius's eight-fold scheme as the general form of the combat"
    - "Hearing the thoughts as clinical symptoms"
    - "Presenting the tomb demons as a neutral incident report"
  years: {from: 270, to: 430}
  status: reviewed
---
Re-derived from the prior build's cleared Doc_04 SS1 candidate 2, SS2
row 2, SS3, SS4, SS5 row 2, SS6 (gravity 2). Deliberately tested apart
from candidate 9 (Evagrian systematization) per Doc_03's own flag that
the systematized register carries single-author concentration risk
this general theme does not - the precondition-for/enabled-by relation
to gravity 9 records that systematization as downstream of, not
identical with, this broader gravity, matching Doc_04 SS2's own
Interaction-test finding ("generates candidate 9 as its Strand-C-
specific systematized form").

The Vita locus and first manifestation cite SS8-9 for the tombs and
SS12-13 for the fort (the edition's own summary line: "How Antony took
up his abode in a ruined fort across the Nile, and how he defeated the
demons"). The second manifestation states the cross-settlement
recurrence claim together with its caveat: the pattern recurs across
named elders and settlements alike in the sayings tradition, though how
far that reflects the settlements themselves and how far it reflects
the sayings' later compilers' own arrangement is not settled.

Step3c: desert.figure.antony added - his own combat at the tombs and
in the fort (Vita SS8-9, SS12-13) is this gravity's own paradigm case,
tested here separately from its own later systematized Evagrian form.

Doc_08: desert.force.martyrdom-unavailable added as a reciprocal
relation, the generating force this description's own closing sentence
already names.
