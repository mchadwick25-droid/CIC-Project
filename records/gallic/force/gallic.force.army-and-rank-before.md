---
id: gallic.force.army-and-rank-before
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
    Documented - the texts' own founding scenes, two voices independently (Vita II, IV, X; Comm. ch.
    1 [2]; Inst. IV.6); Hilary of Arles's Latin on Honoratus's nobility (row 27) at Inferential/Thin
    for wording. Gennadius ch. XIX corroborates the north's founding shape. Reported-Experience
    Status applies to Layer 2's Tours sentences (one hagiographer). The discharge scene's setting is
    the garrison 'of the Vaugiones' (the editorial note identifies Worms), before the episcopate -
    not Tours.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: "ch. II (ii.ii.iii) 'regarded not so much as being a soldier as a monk'; ch. IV (ii.ii.v) the discharge before Caesar as the barbarians rush 'within the two divisions of Gaul'; ch. X nobles 'forced themselves down to this degree of humility'"
  license: public-domain
- source_id: gallic.source.vincent-commonitory
  locus: "ch. 1 [2] (iii.ii): from 'the manifold and deplorable tempests of secular warfare' to 'the harbour of religion'"
  license: public-domain
- source_id: gallic.source.hilary-arles-vita-honorati
  locus: "Honoratus and his brother unable to reach obscurity because their nobility would not permit it (Doc_05 \u00a71.1's rendering, Inferential/Thin)"
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: "IV.6 (iv.iii.iv.vi): the novice's worldly clothes kept by the steward against the day he might want them back; X.3 'a runaway from His service, and a deserter'"
  license: public-domain
- source_id: gallic.source.sulpitius-letters
  locus: "Ep. III: 'the oath of allegiance to Christ'"
  license: public-domain
relations:
- type: precondition-for
  target: gallic.force.renunciation-that-stays
- type: associated-with
  target: gallic.force.barbarian-fiscal-ruin
- type: precondition-for
  target: gallic.gravity.soldier-of-christ
- type: associated-with
  target: gallic.gravity.monk-bishop
- type: associated-with
  target: gallic.quote.martin-refuses-the-donative
- type: associated-with
  target: gallic.quote.vincent-tempests-of-secular-warfare
- type: associated-with
  target: gallic.quote.institutes-opening-soldier-of-christ
- type: associated-with
  target: gallic.quote.cassian-clothes-kept-until-excellence-of-progress
- type: associated-with
  target: gallic.quote.nobles-forced-down-afterwards-made-bishops
name: "The late-Roman army and civil rank as the 'before' of every founding biography"
kind: initiating
matrix_cell: 1A
description: >-
  Each founding story in this world begins with leaving Roman service or Roman rank behind. Martin,
  a soldier, is let go before Caesar just as the barbarians pour into both Gallic provinces at once.
  He tells Caesar plainly: he has served Caesar as a soldier until now, and asks leave to become a
  soldier of God instead - he is Christ's soldier, and it is not lawful for him to fight. Vincent
  comes from what he calls the many sad storms of worldly war, to what he calls the harbour of
  religion. Honoratus and his brother, in Hilary's own Latin, could not stay out of the public eye,
  because their own high birth would not let them. Cassian's junior monk at Marseilles is a man
  whose worldly clothes the steward keeps, until time and trial let the community see the real worth
  of his progress.

  From within, the man who gave things up did not stop being a soldier; he just changed whom he
  served. He had sworn loyalty to Christ, just as he had once sworn it to Caesar. His dress became
  armour, and his day became a campaign; a fault was a fight, and growing cold in the work was
  desertion. What he left behind was kept in a cupboard, in case he ever wanted it back. Rank, too,
  had to be forced down: nobles at Marmoutier, Sulpitius says, forced themselves down to this same
  humility.

  This force gave both houses their own way of speaking about it - plain fact at Tours, more like
  dress worn as a sign at Marseilles - and it gave this world's central gravity its first half, the
  act of giving things up. It made a formed person's sense of who he was a change of loyalty, not a
  change of nature: the north's own life story turns on a discharge, and the south's own manual
  opens by calling a monk a soldier of Christ. This is also why this world's withdrawal stays small
  in scale, and why leaving it means taking an office, not walking away: a man who changes whom he
  serves does not leave service behind. He can still be sent somewhere new.
manifestations:
- "Martin's discharge before Caesar - 'allow me now to become a soldier to God' (Vita IV) - the biography's hinge"
- "Vincent's harbour reached out of 'the tempests of secular warfare' (Comm. ch. 1 [2])"
- "Honoratus's nobility that would not let him reach obscurity (Hilary of Arles, row 27, Inferential/Thin)"
- "The novice's worldly clothes kept in the steward's cupboard (Inst. IV.6)"
- "Nobles at Marmoutier who 'had forced themselves down to this degree of humility' (Vita X)"
---
Grounded in cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml (Sulpitius Severus, John
Cassian, Vincent of Lérins). This description paraphrases the primary sources in its own voice;
their verbatim wording, locus, and speaker attribution are each carried in full in
gallic.quote.martin-refuses-the-donative, gallic.quote.vincent-tempests-of-secular-warfare,
gallic.quote.institutes-opening-soldier-of-christ,
gallic.quote.cassian-clothes-kept-until-excellence-of-progress, and
gallic.quote.nobles-forced-down-afterwards-made-bishops.

This force's relations to this world's other gravities and forces are declared in full in its
relations[] field above, reciprocal edges declared on each target - it is the closest connection in
this world's own matrix to gallic.force.renunciation-that-stays, and only an occasion, not a cause,
for the barbarian pressure it is associated with. Node: both. Canon_cells left empty, matching fleet
convention for gravity/force records.
