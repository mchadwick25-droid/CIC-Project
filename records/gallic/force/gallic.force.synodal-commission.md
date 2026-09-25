---
id: gallic.force.synodal-commission
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
    Documented that Faustus's De gratia exists and states a synodal commission in its own prologue
    (Engelbrecht 1891, rough OCR). Documented ONLY for three short, OCR-clean fragments ('Studium
    asserendae gratiae'; 'suscipit qui oboedientiam famuli laboris adiungit'; 'synodus Lugdunensis
    exegit'); Inferential/Thin for every other rendered phrase, a normalized reconstruction from
    corrupt OCR corroborated only by Engelbrecht's own Prolegomena paraphrase, not independently
    checkable by grep. The dating (c. 473-475) is a range, Inferential/Thin; the network's
    consolidation across the sees of southern Gaul is Dominant Modern Reconstruction (Mathisen,
    unread). Only the prologue was read; the treatise body, and whether it reports in-window Lérins
    teaching, remain unread. This world's own interpretation of this event as an ending is not
    recoverable from the vendored text.
sources:
- source_id: gallic.source.faustus-de-gratia
  locus: "the prologue to Leontius of Arles (file lines c. 3560-3630): a council gathered 'for the condemning of the error of predestination'; 'Studium asserendae gratiae ... suscipit qui oboedientiam famuli laboris adiungit' (lines 3569-3570, fragments grep-clean); 'synodus Lugdunensis exegit' (line 3628); Engelbrecht's Prolegomena (editorial, lines c. 465-548, 555) on the Lucidus affair and the dating"
  license: public-domain
- source_id: gallic.source.gennadius-de-viris-illustribus
  locus: "ch. LXXXVI: 'the grace of God always invites, precedes and helps our will' - Faustus's doctrine summarized; 'first abbot ... then made bishop of Riez'"
  license: public-domain
- source_id: gallic.source.mathisen-ecclesiastical-factionalism
  locus: "the L\u00e9rins network's consolidation across the sees of southern Gaul - thesis-level, not read; the fact used, not the political reading"
relations:
- type: enabled-by
  target: gallic.force.contest-over-antiquity
- type: enabled-by
  target: gallic.force.fugitives-fill-the-sees
- type: associated-with
  target: gallic.gravity.grace-and-effort
- type: associated-with
  target: gallic.gravity.monk-bishop
- type: associated-with
  target: gallic.gravity.authority-ambivalence
- type: associated-with
  target: gallic.gravity.received-not-invented
- type: associated-with
  target: gallic.quote.gennadius-grace-invites-precedes-and-helps
name: "The synodal commission - the churches absorbing the argument and the network (L\u00e9rins-Marseilles)"
kind: ending
matrix_cell: 3A
description: >-
  This world's real change in kind does not happen around 450. It happens in the 470s. By then, the
  grace argument was no longer carried by monks talking to other monks. It was carried by a bishop
  formed at Lérins, writing at the direct request of two church councils, Arles and Lyons, around
  473 to 475. At the same time, the Lérins network took hold across the churches of southern Gaul.
  Faustus's own opening letter to his book on grace, addressed to Leontius of Arles, states the
  request in the bishop's own voice. Leontius wanted to act against what he judged to be the error
  of predestination. He had gathered a council of the highest bishops, and laid the task, Faustus
  says, on his own weak shoulders. A wrong turn, Faustus says, can fall to either side of the road
  the fathers walked.
  After the council of Arles reached its own decision, new errors came to light, and the synod of
  Lyons then required more additions. Most of this survives only in a rough, uncertain reading of
  damaged Latin text; it cannot be checked directly. Gennadius, writing on his own, sums up the
  book's own teaching plainly: God's grace always invites, goes ahead of, and helps the will, and
  whatever good the will achieves is grace's own gift, not its own reward.

  From within, this did not feel like an ending. The man who had been trained at Lérins to fear
  church office had been seized for it anyway. He now wrote as a bishop, at a council's own order,
  defending the same two-sided faith the founders held: real effort joined to real grace, with no
  swing to either extreme. He named what he opposed, just as the founders had, calling it a novelty
  and an error. What had changed was who spoke, and under whose authority. It was no longer a
  brother in a cell answering questions from the fathers. It was a bishop answering a synod.

  This shift changed the tone of this world's most typical kind of teaching. It moved from formation
  writing for monks to a task carried out for bishops. It also settled, in one direction, an old
  tension in this world between giving up power and holding office: the network that had once fled
  the bishop's chair now became that chair itself. It carried this world's central gravity all the
  way to its own end-state, as the one institution left standing. It carried along with it the same
  trust in received tradition - the argument still pleaded as the fathers' own faith, now under a
  synod's own order. What passed on to the communities that came after was the people, the sees, and
  later the books. What did not pass on was the form itself: the conference addressed to
  brother-monks, and with it the close, formation-based setting where this argument had first been a
  remedy for pride, not a matter for a synod to settle. This ending belongs to the south alone; the
  north's own distinct form did not end this way.
manifestations:
- "Faustus's prologue to Leontius: a council 'of the highest bishops' gathered 'for the condemning of the error of predestination,' the treatise written at its commission (row 24, rough OCR, Inferential/Thin except named fragments)"
- "'He takes up the zeal of asserting grace fitly and wholesomely who joins to it the obedience of labour's servant' - the founders' two-sided shape in a bishop's mouth"
- "Arles's subscription, then 'the synod of Lyons required some things to be added' (line 3628, fragment grep-clean)"
- "Gennadius's summary of the doctrine: grace that 'always invites, precedes and helps our will' (ch. LXXXVI)"
- "The L\u00e9rins network consolidated across the sees of southern Gaul (Mathisen, thesis-level, unread)"
---
Grounded in cic/texts/faustus-riez_de-gratia-and-collected-works_engelbrecht1891.txt (Faustus's
prologue, rough OCR) and cic/texts/npnf203_theodoret-jerome-gennadius-rufinus.xml (Gennadius's
independent summary). This description paraphrases the primary sources in its own voice; Gennadius's
own verbatim wording, locus, and speaker attribution are carried in full in
gallic.quote.gennadius-grace-invites-precedes-and-helps. Faustus's own prologue is
Inferential/Thin for wording beyond its three OCR-clean fragments, disclosed above in
divergence_note, and is paraphrased here rather than quoted for that reason.

This force's relations to this world's other gravities and forces are declared in full in its
relations[] field above, reciprocal edges declared on each target. Node: S. The
`merovingian-gallic-christianity` "seedbed"/"receives" continuity is not decided here. Canon_cells
left empty, matching fleet convention for gravity/force records.
