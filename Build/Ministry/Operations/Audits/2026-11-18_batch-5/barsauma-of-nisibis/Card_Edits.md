# Card edits: Barsauma of Nisibis

Card `barsauma-of-nisibis.card.json` against `Card.existing.json`. Everything not listed is word for word as before.

## Corrections

| Old words | New words | Evidence |
|---|---|---|
| "against the catholicos Babai" (knownFor) | "against the catholicos Babowai" | Mark's ruling on the spelling; the brief uses Babowai throughout. |
| "Babai's successor Acacius" (knownFor) | "Babowai's successor Acacius" | Same. |
| "charges him with Babai's death" (legacy.remembered) | "charges him with Babowai's death" | Same. |
| "That he caused Babai's death rests on later writers" (uncertain) | "That he caused Babowai's death rests on later writers" | Same. |
| "sent Babai's letter to the king unopened" (uncertain) | "sent Babowai's letter to the king unopened" | Same. The claim itself holds: 'Amr, "quin aperiret, eam ad Pherozem transmisit" (AMR 14051-14052). |

No other statement was found wrong. Spot-checked and left in place: Chabot's note on Edessa in 449, the expulsion of 457 and the king's favor (SO 20229-20236); the 435 date in Scher and in Abbeloos and Lamy (CFS 20624-20626; BH 3651-3660); "composa lui aussi beaucoup d'homélies" (CFS 20801); "du fougueux évêque de Nisibe" (SO 34806); Connolly's sentence (CON 4486); Chabot on Maruta's letter (MS 33473-33479); the six letters and the first letter's five bishops (SO 35203-35205).

## New

- **sources.about**: added the Armenian letter of Babken, about 506, in Ter-Minassiantz's German (`cic/texts/ter-minassiantz_armenische-kirche-in-ihren-beziehungen-zu-den-syrischen-kirchen-tu26-deu_1904.txt`). Evidence: the brief's sentence "About 506, Armenian bishops refused the rules Acacius and Barsauma had set up" (TM 36823-36842).
- **briefReferences**: 13 entries, new.
- **quotationOriginals**: 10 entries, one for each quoted span in the brief. All are awaiting second reading (the census card has no `quotationOriginals`, so no `secondReading` could be copied). Lines re-read in the files:

| Modern | File and lines |
|---|---|
| out of ill will and human passion. | SO 20258 |
| Satan stirred up a quarrel | SO 35397-35398 |
| murmurs, blames, charges and testimonies, | SO 35256-35257 |
| concubine, | BH 3758-3762 |
| Now Nisibis is shaken ... the Persians. | SO 35479-35483 |
| like the doctor who amputates, | SO 35509-35510 |
| but only on this point. | SO 20484 |
| the divine assembly, | SO 31682 |
| my lord, | SO 31684 (title Mar only) |
| the blessed Mar Barsauma. | SO 31684-31685 |

## Not found, and open points

- **"my lord"**: no held text glosses Mar. The entry prints "Mar" and says so.
- **Two scan faults** need entries in `tools/quote_scan_readings.json` before the card validates; I did not touch that shared file. In `synodicon-orientale_recueil-de-synodes-nestoriens-syr-fra_chabot1902.txt`: line 35397, scan "Satan 4 suscité", reads "Satan a suscité"; line 31685, scan "Bar CGauma", reads "Bar Çauma".
