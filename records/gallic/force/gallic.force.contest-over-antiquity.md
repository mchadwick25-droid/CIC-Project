---
id: gallic.force.contest-over-antiquity
world_id: gallic-monastic-ascetic-christianity
record_type: force
schema_version: 2
status: ready
register: emic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: load-bearing
  formation_confidence: Documented
  divergence_note: >-
    Documented that Vincent quotes Celestine's letter and reads it as he does (Comm. ch. 32 [85],
    his own text); Widely Accepted (editorial) for the letter's original direction - at the bishops
    of southern Gaul for "the connivance of certain bishops of Southern Gaul with the unsound
    teaching of their clergy" (Heurtley's Appendix III). Contested whether that reading shows
    Vincent held the Massilian position: Heurtley reads Vincent's own silence on Augustine's name as
    evidence for the leaning, against his own earlier, stated doubt that "the express enunciation of
    it is nowhere to be found in the Commonitory." The Benedictine editor, Noris, Vossius, Tillemont,
    and Neander are editorial or editorial-quoted, Noris and Tillemont licensed for general
    reference only, not for their own text to be quoted directly. This force is an in-window contest
    over who holds the consent of the fathers, not a later application of the rule against the
    Massilian position; whether any later application exists is outside the vendored record and is
    not asserted.
sources:
- source_id: gallic.source.vincent-commonitory
  locus: "ch. 32 [85] (iii.xxxiii): Celestine's 'Rebuke these people. Restrain their liberty of preaching' and 'let novelty cease to assail antiquity,' read as 'not that antiquity should cease to subvert novelty, but that novelty should cease to assail antiquity'; ch. 26 [69] the heretics who promise grace without labour"
  license: public-domain
- source_id: gallic.source.npnf-editorial-apparatus
  locus: "Heurtley's Appendix III (iii.xxxvii, editorial): the letter's direction; Vincent's handling 'very commonly thought, and with reason, to indicate a Semipelagian leaning'; 'an evident wish to shift the charge of novelty'; Appendix II (iii.xxxvi): Prosper's 'obstinationem suam vetustate defendunt'; Heurtley's Introduction (iii.i): the silence on Augustine's name, and his own stated doubt"
  license: public-domain
- source_id: gallic.source.augustine-letters-221-226-absence
  locus: "Prosper's Ep. 225, unvendored - its 'they defend their obstinacy by antiquity' reaching this build only as Heurtley's Latin quotation"
relations:
- type: enabled-by
  target: gallic.force.africa-and-rome-pressure
- type: precondition-for
  target: gallic.force.synodal-commission
- type: enabled-by
  target: gallic.force.legitimacy-by-reception
- type: associated-with
  target: gallic.gravity.received-not-invented
- type: associated-with
  target: gallic.gravity.grace-and-effort
- type: associated-with
  target: gallic.quote.vincent-celestines-letter-and-its-reading
- type: associated-with
  target: gallic.quote.heurtley-celestines-letter-addressed-to-gaul
- type: associated-with
  target: gallic.quote.heurtley-semipelagian-leaning-reading
name: "The contest over who holds antiquity - the boundary-instrument turned both ways"
kind: ending
matrix_cell: 3B
description: >-
  Vincent's handling of a letter from Rome shows a strange reversal. The same rule that guarded
  the south's position gets turned back against it.

  Vincent quotes Pope Celestine's letter to the Gallican bishops. Celestine writes that these
  men should be rebuked, and their freedom to preach restrained; if that is truly the case, he
  says, then novelty should stop attacking antiquity. Vincent reads this as a verdict for his
  side. Antiquity should not give way to novelty, he says.
  Novelty should stop attacking antiquity instead. The volume's modern editor adds real context
  here. Two of Augustine's allies, Prosper and Hilary, had gone to Rome to complain about the
  clergy of southern Gaul. Celestine's letter was actually directed at those bishops, for
  tolerating unsound teaching among their own clergy. Vincent's handling of it has commonly
  been read as showing sympathy for the very position Rome was writing against. He repeats "if the
  case be so" again and again. To this editor, that reads as an attempt to shift the blame for
  novelty onto his opponents instead.

  So what does this show, at the strength of one editor's reading? The antiquity-versus-novelty
  rule was first turned against the very clergy it was meant to protect, by Celestine's letter.
  Then Vincent turned it back the other way, against Augustine's party. This is not a fracture
  that appears only after this world's story ends. It is a real contest, inside Vincent's
  text, over who actually holds the fathers' consent.

  From inside Lérins, though, there was no contest over the rule itself. There was only its correct
  use. The keeper at Lérins heard Rome say that novelty must give way to antiquity. He knew which
  side was antiquity: his own. To him, the men who had complained to Rome were the real inventors of
  novelty. The letter forbade their liberty to preach, not his. Vincent's text never records
  that his opponents were saying the very same thing about him, in the very same words.

  This shaped what the rule of antiquity became afterward. Detached from any one side, it grew
  quotable by every later party in turn. The position itself went into the historical record under
  its opponents' name for it. By the fifteenth century, an editor tried to cut it out of
  Cassian's text, for the sake of orthodoxy. This world's boundary logic produced its
  sharpest outside pressure. It shaped the very terms in which the world would later be remembered
  by others.
manifestations:
- "Celestine's letter as Vincent quotes it: 'Rebuke these people. Restrain their liberty of preaching'; 'let novelty cease to assail antiquity' (Comm. ch. 32 [85])"
- "Vincent's reversal - 'not that antiquity should cease to subvert novelty, but that novelty should cease to assail antiquity' - read by his editor as 'an evident wish to shift the charge of novelty'"
- "Prosper's 'they defend their obstinacy by antiquity' (Ep. 225, through Heurtley's Appendix II, Latin, editorial)"
- "The letter's direction at the bishops of southern Gaul for their clergy's 'unsound teaching' (Heurtley's Appendix III, editorial)"
- "The rule of antiquity detached from its position and quotable by every later party; the position remembered as 'the remnants of the Pelagians'"
---
Grounded in cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml (Vincent of Lérins, and
the volume's own editorial apparatus). This description paraphrases the primary and editorial
sources in its own voice; their verbatim wording, locus, and speaker attribution are each carried
in full in gallic.quote.vincent-celestines-letter-and-its-reading,
gallic.quote.heurtley-celestines-letter-addressed-to-gaul, and
gallic.quote.heurtley-semipelagian-leaning-reading. Whether Vincent himself held the position Rome
was writing against is Contested, carried in this record's own `divergence_note`, not resolved
here.

This force's own relations to this world's other gravities and forces are declared in full in its
own `relations[]` field above, reciprocal edges declared on each target. Node: S. Canon_cells left
empty, matching fleet convention for gravity/force records.
