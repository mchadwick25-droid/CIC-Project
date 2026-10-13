Review round 1, gallic out-of-scope fixes (pass 2), 2026-10-13, reviewer: independent Opus subagent

Verdict: PASS WITH NON-BLOCKING

Scope: commit 76c92c8, 48 files under records/gallic. I compared every changed field with its old version (`76c92c8^`), field by field. Readability scores come from `engine.m1.gates.grade_text`, and the voice budget from `engine.m10.regate.voice_budget`. The texts I checked against are npnf211, npnf203, the Salvian text, and Hilary's `hilary-arles_sermo-de-vita-sancti-honorati_migne-pl50.txt`. Line numbers for npnf211 and npnf203 point to the stripped copies in scratchpad (n211.txt, n203.txt), as in the audit notes. I did not edit anything and made no model calls.

## Findings

1. **gallic.force.renunciation-that-stays, description** - Old: "Marmoutier sits across the river from the bishop's own city"; "across a river or onto an island" - New: both are kept word for word in the full rewrite. - Source: npnf211:1129-1133 "a monastery for himself about two miles outside the city ... the river Loire had shut in the rest of the plain by a bay". Nothing in the source says it is across the river. This commit fixed the same claim in voice_craft identity and in world_core formation_logic ("two miles outside"), but kept it here. - NON-BLOCKING. Replace with "The monastery lay about two miles outside the bishop's own city." and "out of the city, onto an island, or into a desert near the city".

2. **gallic.force.renunciation-that-stays, description** - Old: "gives G9 its field - 'one cannot flee bishops and be made one without a conviction that both are possible'" - New: "It also makes room for the office as a destiny: no one can flee bishops ..." and then, two sentences later, "drawn to the office as a destiny". - Source: G9 is the authority ambivalence. The fugitives-fill-the-sees and court-at-trier rewrites map it that way too. The new wording names the wrong gravity and repeats itself. - NON-BLOCKING. Replace with "It also gives the ambivalence toward authority its ground: no one can flee bishops and be made one without believing both are possible."

3. **gallic.force.egyptian-standard, description; gallic.force.cooling, description** - Old/New (both full rewrites): "No one kept the probation 'even for a year' (Inst. IV.2)" and "one no Gallic monk kept 'unbroken even for a year'". - Source: npnf211:18553-18560 "their untiring perseverance and humility and subjection ... we cannot recollect any one who joined our monasteries keeping it up unbroken even for a year". This is the same overstatement the commit corrected in five other records. "Probation" is also the wrong subject: the source is talking about perseverance. - NON-BLOCKING. egyptian-standard: "Cassian could not recall anyone in Gaul's houses keeping the fathers' perseverance 'unbroken even for a year' (Inst. IV.2)." cooling: "...one Cassian could not recall any monk of theirs keeping 'unbroken even for a year' (IV.2)."

4. **gallic.voice.craft, flavor_notes[3] (the reception note)** - Old/New: "the cold that refits the hours" was left in a note this commit edited. - Source: npnf211:18853-18863 (Inst. IV.11) is about food. Inst. I.10 (16917) is about dress. The one passage about winter hours (III.8, 18274) describes the Egyptian elders' long winter nights, not Gaul's cold. Adjudication already confirmed this as a "hours" Tier A error in force.cold-of-gaul, and the force record was fixed. This is a standing instruction the voice reads. - NON-BLOCKING, since it was not on the named list. Log it in OG-33, or change it to "the cold that refits the dress and the food". That adds one word, making 1499 of 1500, still within budget.

5. **gallic.force.renunciation-that-stays and gallic.force.episcopal-recruitment, description; gallic.force.army-and-rank-before, description** - Old: "'he who had refused ... came to him' (Hilary, row 27)" and "'a monk's humility ...' (Hilary on Honoratus)" - New: "Hilary says of Honoratus: 'he who had refused to go to the dignity - the dignity came to him.'" and "Hilary says Honoratus kept 'a monk's humility as entire ...'". - Source: Hilary file lines 714-722, which are rough OCR. The renunciation record's own locus rates this English "Inferential/Thin". The honoratus story's claim_guard forbids quoting this English as Hilary's own words. The rewrites now present a rough rendering as Hilary's quoted speech more plainly than before. gravity.monk-bishop handles the same line correctly. Separately, army-and-rank's "known here only in a rough rendering" refers to the record itself ("here"). - NON-BLOCKING. Drop the quotation marks and add a hedge: "Hilary's sermon, as far as its rough Latin can be read, says the dignity came to the man who had refused to go to it." In army-and-rank, use "Hilary's Latin, which survives only in a rough copy, tells the same of the nobles of Lérins."

6. **gallic.force.transmission-in-ending, description; gallic.force.transmission, description** - Old: "the Dialogues reaching Gennadius 'in two divisions'" listed among accidental losses; "the eyewitness frame itself was re-cut in copying" - New: "Some losses came early and by accident. ... Gennadius knew the Dialogues 'in two divisions.'" The transmission description now ends on a stray line: "Gennadius knew the Dialogues in two divisions." - Source: npnf203:42551 "a sort of dialogue in two divisions" describes how the book is laid out. The gravity.named-example finding confirmed that this does not show a loss or a split, and that record was fixed, but this one still lists it as a loss. - NON-BLOCKING. Delete that sentence from transmission-in-ending's list of losses. Delete the closing sentence of transmission, or move it beside the other Gennadius sentence with no claim of loss.

7. **gallic.story.germanus-scruple-at-morning-service, text** - Old: "it seemed absurd, he said, for the reward of real effort - true chastity, won by hard, sustained toil - not to be credited ..." - New: "Germanus put the trouble plainly. True chastity is won by hard, sustained toil. It seemed absurd, he said, ..." - Source: npnf211:37519-37520 "perfect chastity, which is gained by the earnestness of one's own toil". That is Germanus's premise, which Chaeremon then corrects. Split off before "he said", it reads as the narrator stating it as fact. - NON-BLOCKING. Use "Germanus put the trouble plainly. True chastity, he said, is won by hard, sustained toil. So it seemed absurd for the reward of such real effort not to be credited mainly to the person who put in the work."

8. **gallic.gravity.grace-and-effort, description** - Old: "A reader should not mistake the modest classification for any doubt about what Cassian and Chaeremon actually taught." - New: "That narrow reach is no doubt about what Cassian and Chaeremon actually taught." - The new sentence misreads easily, because "no doubt" is an idiom for "certainly". It is not a source problem. - NON-BLOCKING. Use "That narrow reach casts no doubt on what Cassian and Chaeremon actually taught."

9. **gallic.story.honoratus-and-the-island, absent_detail** - Old: "the fillet that took him off it" ... "how he came to Lerins and how he left it" - New: the first phrase is fixed ("the fillet that made him a presbyter there"), but "and how he left it" stays. It also still calls the presbyterate one of "the island's edges". - Source: Hilary file line 716, "Apparuit illic presbyter". The passage narrates nothing about his leaving. - NON-BLOCKING, because this field is not spoken. Use "...we can tell how the founder came to Lerins and how he was made a presbyter there, and not what he or anyone did there in between."

10. **force and gravity descriptions (arian-scattering, named-exemplar, transmission, transmission-in-ending, unconverted-countryside, gravity.monk-bishop, gravity.named-example)** - Old/New: "Before Ligugé" and "Marmoutier" are kept in the full rewrites. - Source: the world_core cautions name Ligugé and Marmoutier as later editorial place-names that "are not in the ancient texts we have ... Never use them as ours." These fields reach the voice. cold-of-gaul dropped its "Marmoutier", so the commit is now inconsistent. - NON-BLOCKING. This was not named in the findings and it is spread across many records. Log it in Open_Gaps_Tracking as its own item; do not patch it here.

## Changes checked and found sound

- **Twelve story texts.** The 21 record ids are all gone, including the broken lentil id. Every sentence split keeps the facts in their old order and adds nothing. These fixes are correct against the source:
  - discharge: the "whole of Tours's memory" clause is cut.
  - election: "could not easily be drawn out" replaces the stated reluctance (Vita IX).
  - germanus: Honoratus and Eucherius replace Lerins. "Sometimes looks for some effort" matches XIII.13 (38201-38203). The three stages are all God's gift, without taking away free will, and grace and free will "cannot be fully grasped", which matches XIII.18 (38602-38624).
  - archebius: "more than their words" matches 36830-36832, and the pivot is deleted.
  - honoratus: the three Latin strings are removed, and "And then Hilary says:" is used. "As he says he had seen" correctly renders "ut vidimus".
  - paesius: the closer matches the adjudicated wording, and the speakers are correct (21076-21083).
  - raising: "reckoned holy by all ... truly apostolical" now follows 1024-1025 more closely than before.
  - cloak: "the servant's boots" is correct.
  - trier: "more slowly and with less power" matches 5213.
  - The term's senses.personal now reads "Word of it was carried to Augustine in Africa", as adjudicated.
- **world_core.**
  - horizon drops the island placement for Vincent and the word "window", and adds the "all of it at once" constraint.
  - formation_logic matches the corrected fix, in the past tense. It keeps "received from the fathers". Its "progress in any virtue" follows Inst. XII.9 (25035-25038) better than the adjudicated draft did, and "two miles outside" is right (1129).
  - thinness keeps Vincent's reading of the letter, adds nothing unsourced, and fixes "behind the body".
  - cautions keeps all seven constraints: Egypt named as Egypt's; what is Gaul's own; no traffic between the houses, even where the capture stories look alike; the four editorial names; Augustine limited to three treatises, with the named risk; the Antony Life and the Rule of Benedict excluded; and "semi-Pelagian" appearing only in the editors' notes. It moves the morning service to Egypt. "Impossible here" follows Inst. Pref. (16530).
- **voice_craft.**
  - The budget is 1498 of 1500 words, at FK 6.6.
  - The self-reference note is unchanged.
  - guard now matches Vita XXV (1835-1836).
  - The disagreement note now gives Egypt's exorcist rule as Egypt's (39902-39905).
  - "Two miles outside Tours" is supported.
  - Removing the "Current state" body paragraph is correct. The rest of the body is still process narration, and `tools/check_live_commentary.py` should report it.
- **Force and gravity descriptions.**
  - Every Doc, Layer, G-number, cell, node, "Native", "window" and "this record" label is gone.
  - Each named error is fixed and checked against the source: Illyria then Milan (938-953); "Historians" removed; IV.11 food and "coldness of spirit" (18853-18863); "most of Cassian's work"; the straw and threads no longer called relics, replaced by psalms and hymns (2508, 2518); "all the Catholic fathers who have taught perfection of heart" (38602-38603); Vincent's target and the grace dating marked as disputed; the "more than hell" sentence and the III.13 "body" sentence deleted; the Sarabaite cells "calling them monasteries" (42652-42653); the Prosper wording in contest-over-antiquity.
  - Single-quoted source words were checked by script against the texts. All match, apart from footnote breaks and a ligature in the source files.
  - The named-example compression is the adjudicated wording.
  - No field gives a new classification.
- **"Unbroken" loci.** egypt-two-measures, figure.cassian, egypt-as-measure not_for and received-not-invented not_for all now follow IV.2 (18559-18560).
- **Readability.** Every field this commit edited passes FK at or under 10 and FRE at or above 60. The one score below 60 is received-not-invented's description at 59.8, and its text was not changed in this commit.
- **We-voice.** I found no new present-tense practice claims, coined closers, honesty preambles or "historians" in we-voice fields.

## Resolution

Findings 1 to 9 were applied in commit bd4f74f before the package was rebuilt. Finding 10 (the editorial place-names Ligugé and Marmoutier in seven force and gravity descriptions) is logged in Build/worlds/gallic/Open_Gaps_Tracking.md, OG-35, as its own open item.
