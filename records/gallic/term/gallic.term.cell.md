---
id: gallic.term.cell
world_id: gallic-monastic-ascetic-christianity
record_type: term
schema_version: 2
status: ready
register: emic
canon_cells:
- F4-P
confidence:
  citation_specificity: A
  verification_state: verified-direct
  evidentiary_weight: corroborating
  formation_confidence: Documented
  divergence_note: >-
    Two voices, both nodes. The rule of the cell (not leaving it, alone or with one other) is Cassian's
    Egyptian prescription, and whether any Gallic house kept it is not documented. The Latin cella /
    cellulis reaches us only through the editor's Introduction, in a sentence that is Cardinal Noris's
    (general reference only), not our own Latin as read.
sources:
- source_id: gallic.source.sulpitius-vita-martini
  locus: 'Life of St. Martin ch. X ("a cell constructed of wood"; the caves; "rarely did any one of them go beyond the cell"); ch. XXIV ("as he was praying in his cell"; the purple-robed devil)'
  license: public-domain
- source_id: gallic.source.sulpitius-letters
  locus: 'Letter II ("sitting alone in my cell")'
  license: public-domain
- source_id: gallic.source.sulpitius-dialogues-ii-iii
  locus: 'Dialogues II.11 (the counterfeit''s cell "in the desert"); II.13 ("the door of his cell being closed"; Agnes, Thecla, Mary)'
  license: public-domain
- source_id: gallic.source.cassian-institutes
  locus: 'Institutes II.12, 14, 15 (alone or with one; "some perfectly secure harbour"; "nor does he presume even to leave his cell"); IV.10 ("do not dare to leave their cell"); X.1-2 (accidie, "disgust with the cell," the sun "too slow in setting")'
  license: public-domain
- source_id: gallic.source.cassian-conferences-part-iii
  locus: 'Conferences XVIII.16 ("the doors of our cell or the recesses of the desert"; "no one is more my enemy than my own heart")'
  license: public-domain
retrieval:
  tier: 2
  retrieve_when:
  - where a monk lived, or what a "cell" was
  - whether monks were alone, or why leaving the cell was a fault
  - participant uses "cell," "cave," "hut," "hermitage," or "room"
  - Marmoutier's caves, Martin's closed door, accidie's disgust with the cell, or Cassian's "harbour"
  prefer_instead:
  - the house as a whole (retrieve monastery / coenobium)
  - the prison sense of "cell"
  - the desert hermit's cell as such (retrieve anchorite / hermit)
relations:
- type: associated-with
  target: gallic.term.monk-solitary
- type: associated-with
  target: gallic.term.unceasing-prayer
- type: associated-with
  target: gallic.term.monastery-coenobium
- type: associated-with
  target: gallic.term.anchorite-hermit
- type: associated-with
  target: gallic.term.junior-novice
- type: associated-with
  target: gallic.term.obedience
- type: associated-with
  target: gallic.term.thoughts
- type: associated-with
  target: gallic.term.accidie
- type: associated-with
  target: gallic.term.contemplation
- type: associated-with
  target: gallic.term.angels
- type: associated-with
  target: gallic.term.the-devil-demons
- type: associated-with
  target: gallic.term.illusion
- type: associated-with
  target: gallic.term.kingdom-within
plain_meaning: >-
  The monk's own dwelling, and the place where everything happens to him. There Martin prays,
  receives saints, and is tempted by a purple-robed devil behind a closed door. There Cassian's junior
  may not go out without leave, stays all day at his work, and is assailed at noon by the disease that
  makes him hate the cell itself.
world_word: cell (cella)
false_friend:
- a prison cell
- a bare private bedroom, with solitude as privacy
- a hermitage as retreat from stress
senses:
  informational: >-
    At Tours the cell is what the master has and what the disciples make: Martin "possessed a cell
    constructed of wood," the brethren "formed these out of the rock of the overhanging mountain,
    hollowed into caves," and "rarely did any one of them go beyond the cell, unless when they
    assembled at the place of prayer." What is seen and heard in it is the substance of formation:
    Sulpitius and Gallus keep watch outside "the door of his cell being closed" and hear voices; the
    devil comes "clothed in purple, and with a glittering crown." At Marseilles the cell is a
    discipline before it is a place: a cell "which he inhabits alone, or is allowed to share with only
    one other"; after the office no one "dares to loiter ... nor does he presume even to leave his cell
    throughout the whole day." Labour holds the monk there "like some strong and immoveable anchor,"
    so that the wanderings of the heart, "fastened within the barriers of the cell, may be shut up in
    some perfectly secure harbour." And the cell has its own disease, accidie, which "produces dislike
    of the place, disgust with the cell."
  evidential: >-
    Sulpitius (Life chs. X, XXIV; Letter II; Dialogues II.11, II.13) and Cassian (Institutes II.12-15,
    IV.10, X.1-2; Conferences XVIII.16). The cell-rule is Egyptian by Cassian's framing; Gallic
    observance is undocumented. The Latin lemma reaches us only editorially.
  personal: >-
    The cell keeps the body still so that the heart can be fought. Piamun's warning closes the circle
    for us: patience must not rest "in the doors of our cell or the recesses of the desert," because
    "no one is more my enemy than my own heart." That is why the south treats leaving the cell as a
    fault, and why the north's stories happen behind a closed door.
  translational: >-
    'A cell - like a prison, or a private room?' - neither: it is the one place a monk is, a wooden
    hut or a hollow in the rock he rarely leaves except for prayer, where saints and the devil appear,
    and in the south a harbour whose barriers hold the wandering heart still by labour and rule - with
    its own named affliction at noon.
quick_meaning: >-
  The monk's own hut or cave, rarely left except for prayer - where saints and the devil come, and
  where the wandering heart is held still.
distortion_risk: medium
use_note:
  means: "The cell meant the monk's own dwelling, at Tours a hut or cave rarely left except for prayer, at Marseilles a discipline holding the wandering heart still by labour."
  not_for:
    - "a prison cell, or a bare private bedroom with solitude as privacy"
    - "the house as a whole, which sits in gallic.term.monastery-coenobium"
    - "the noonday hatred of the cell itself, which sits in gallic.term.accidie"
    - "Cassian's rule of never leaving the cell as proven Gallic practice, when whether any Gallic house kept it is not documented"
  years: {from: 397, to: 435}
  status: reviewed
---
Built from Doc_06 entry 016 (Tier 2, promoted from Doc_03's Tier 3 on Doc_05 §1.2; chunk
galliclex016_cell.md; Doc_03 1.5). Register emic. Quotations verified at locus by the build's own
Doc_06 pass; not re-read here. Canon cell F4-P: the cell as harbour and anchor for "the wanderings of
the heart" is this world's own substantive answer to someone who struggles to quiet their mind.

Related-Terms also names the devil / demons, illusion and angels - cross-batch at authoring time,
added as relations (typed associated-with) at the reconciliation pass once all 81 term records
existed.
