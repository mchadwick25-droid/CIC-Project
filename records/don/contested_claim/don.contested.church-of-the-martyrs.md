---
id: don.contested.church-of-the-martyrs
world_id: donatism
record_type: contested_claim
schema_version: 2
status: ready
register: etic
canon_cells: []
confidence:
  citation_specificity: B
  verification_state: verified-via-authority
  evidentiary_weight: contested
  formation_confidence: Contested
  divergence_note: null
sources:
- source_id: don.source.passio-marculi
  locus: the whole work - the fullest hagiographic account this corpus holds, and the text both hostile
    witnesses argue against on two different questions
  license: public-domain
- source_id: don.source.optatus-against-the-donatists
  locus: cic/texts/optatus_against-the-donatists.txt, lines 2064-2096 - the argument that the deaths were
    deserved punishment for schism, on the model of Phineas, Moses and Elijah
  license: public-domain
- source_id: don.source.augustine-answer-to-petilian
  locus: Answer to the Letters of Petilian II.45-46 - the separate and different dispute over whether the
    deaths were self-sought, and so whether the word martyr applies at all
  license: public-domain
- source_id: don.source.passio-donati-sermon
  locus: the earliest Donatist-authored text in this corpus; its admonitio describing an annual commemoration
  license: public-domain
- source_id: don.source.deo-laudes-acclamation
  locus: CIL VIII 17732, with 20482, 17368, 18669 - the acclamation cut in stone, never textual to begin
    with
  license: public-domain
claim: >-
  We are the Church of the Martyrs: the pure, persecuted, true church, and what we have suffered is the
  proof that the claim is sincerely held rather than asserted for advantage. Our dead are held by name,
  at the grave, on the appointed day, their accounts read aloud - and the community that produced Marculus
  and Isaac and Maximianus is not the community that surrendered the scriptures.
held_against:
- Optatus concedes the killings and denies their meaning. Arguing on the model of Phineas, Moses and Elijah,
  he reads the deaths of Marculus and Donatus as deserved punishment for schism rather than as martyrdom
  - a rival theology of the same events, not a denial that they happened (don.story.passio-marculi;
  don.source.optatus-against-the-donatists at lines 2064-2096)
- Augustine disputes something else entirely, and the two arguments must not be merged. On the question
  of whether the men threw themselves down or were thrown, he argues that the label martyrdom does not
  apply to a death that was sought - two authors, two arguments, two works
  (don.source.augustine-answer-to-petilian II.45-46; don.figure.augustine)
- Suffering under persecution does not by itself distinguish the two African parties, because for the persecution
  the founding accusation rests on - the empire-wide Diocletianic persecution - the eventual rival suffered
  alongside this communion, before the schism existed at all. Only the later Macarian repression of 347-348
  was suffered AT the rival's own instigation, and it is that second persecution, not the first, that supplies
  the martyrs actually commemorated (Doc_07 SS3A, carried in don.core.donatism's own formation_logic)
- The Passiones are hagiographic in form and this world's own record grades them accordingly - the Passio
  Marculi is Tier 3, its general portrait Contested and corroborated by hostile witnesses only for the
  bare fact of the killing, its visionary and miraculous details carried at Inferential-Thin confidence
  as the tradition's own testimony and never as verified events (don.story.passio-marculi)
- The texts do not date themselves. The Passio Marculi's own heading gives a day and no year, and the 347-348
  Macarian dating rests on standard field literature rather than on the text; for the Passio Donati sermon
  two vendored authorities disagree outright - Mabillon dates the persecution c. 340, Monceaux dates it
  to 12 March 317 with composition c. 320 - and neither is adopted (don.core.donatism cautions 5 and 6)
- Nothing survives of what any of these martyrs said under interrogation in their own words, and no independent
  witness confirms the vision, the fall, or the light. What the hostile record supplies is that they were
  killed, and an argument about whether the killing counts
concedes: >-
  The word martyr is doing contested work here and this communion's own record does not pretend otherwise.
  What the surviving texts establish is a formation ideal - what a finished life looks like, held up for
  a community to be formed by - not a set of verified events, and the ideal is what the texts were written
  to carry. The bare killings are corroborated from two separate hostile directions, but neither hostile
  writer accepts this communion's account of what happened, so that corroboration covers the killing and
  nothing beyond it. And the deepest concession is the one about the word itself: on the founding
  persecution, both African parties were persecuted together, so suffering alone cannot settle which of
  them is the true church - that argument needs the traditio accusation to do the work, and the traditio
  accusation is contested on its own separate ground.
divergence_partners:
- pahc.contested.martyrdom-polycarp-dating (world post-apostolic) - a genuine divergence about what
  martyrdom is FOR, sitting underneath a real methodological convergence. That claim applies the identical
  discipline this one accepts - the narrative is shaped by hagiographic convention throughout, the formation
  ideal is the evidence rather than the staged narrative details as historical reporting - and this record
  does not claim a methodological quarrel where there is none. The divergence is in the work martyrdom
  does. There, martyrdom-meaning forms a community under an outside persecuting power; here it is
  evidence in a legitimacy contest between two rival Christian communions in the same towns, offered
  as proof of which one is the church. That is a different argument being made from the same genre.
- ijc.gravity.sacramental-institutional-tension (world imperial-juridical) - the same martyr material,
  the same century, the same Latin West, put to opposite use. That world's own record has Damasus annexing
  martyr-sanctity to serve Rome's positional claim, and Leo preaching the apostle-martyrs as the ground
  of a see's institutional rank - martyr-standing recruited INTO an institutional and state-adjacent order.
  This claim deploys martyr-standing against the institutionally favoured party, as the evidence that the
  favoured party is not the church. The Imperial and Juridical world carries no contested_claim on
  martyrdom, so this entry names the gravity record where its position actually sits.
relations:
- type: associated-with
  target: don.gravity.church-of-the-martyrs
---
Built for the Table Readiness Round from the cleared Doc_04 SS3.3 (candidate G3, six of six PASS,
classified Primary at SS4, and named there the least Author-Gravity-encumbered Primary in the whole
gravity discovery - a positive finding, not the absence of a caveat) together with Doc_07 SS3A's
two-persecutions structure. Held for don.gravity.church-of-the-martyrs per this step's
Primary-gravity minimum; associated-with recorded reciprocally on that gravity record in the same
pass.

THIS IS THE ONE PRIMARY WHOSE CONTEST IS NOT ABOUT MEDIATION, and the record is built that way on
purpose. Three Donatist-voiced or Donatist-authored texts plus epigraphy that was never textual to
begin with make this gravity's evidentiary base the strongest in this world; contesting it on Author
Gravity grounds would be borrowing a caveat from the neighbouring gravities where it genuinely
applies. What is genuinely contested here is different and sharper: not whether the martyrs are ours
but whether their deaths prove what the claim says they prove. Optatus and Augustine each say no, for
two different reasons, and don.story.passio-marculi already carries the correction (from Doc_09's own
Round 1 review, finding H2) that those two arguments are not a citation chain and must not be merged.
That correction is honoured in held_against above, item by item.

THE TWO-PERSECUTIONS POINT IS THIS WORLD'S OWN, NOT AN OPPONENT'S. Doc_07 SS3A holds the Diocletianic
and Macarian persecutions distinct as a matter of this world's own memory structure - a formed member
can say precisely which persecution grounds the accusation and which grounds the grief. Carried into
held_against and concedes above because the same distinction, stated at the table, is the strongest
thing an opponent can say back: shared suffering in the first persecution is exactly why suffering
alone cannot settle the legitimacy question.

DATING IS CARRIED AS UNSETTLED, NOT RESOLVED. don.core.donatism cautions 5 and 6 govern: no settled
date or author is cited for the Passio Donati anywhere in this record, and the 347-348 Macarian
dating is named as the field's rather than the texts'. canon_cells left empty, matching this world's
records generally.
