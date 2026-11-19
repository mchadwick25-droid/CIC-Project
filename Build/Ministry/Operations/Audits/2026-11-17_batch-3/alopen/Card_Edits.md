# Alopen — Card edits

Card: `alopen.card.json`, from `alopen.original.card.json`. Brief: `alopen.brief.txt`. Every other field is word for word the original. Line numbers are the files' own in `cic/texts/`. MAL = `malech_history-of-the-syrian-nation-and-old-evangelical-apostolic-church-of-the-east_1910.txt`; LEGGE = `legge_nestorian-monument-of-hsi-an-fu_trubner1888.txt`; YULE = `marco-polo_book-of-ser-marco-polo-v2_yule-cordier1903.txt`; BUDGE = `yahballaha-sauma_monks-of-kublai-khan_budge1928.txt`.

## New

1. **`briefLength`** (after `role`): "about 1 minute 10 seconds". Evidence: the brief is 181 words by `wc` (177 by the scorer, Recheck.md).
2. **`quotationOriginals`**, one entry. Modern: "Watching the blue clouds, he carried the true sacred books. Watching the way the winds blew, he faced hardships and dangers." (the brief's first sentence, exact). Printed: "Observing the azure clouds, he bore the true sacred books; beholding the direction of the winds, he braved difficulties and dangers." Re-read at MAL 13688–13689, verbatim. Work: the Xi'an stele, tr. A. Wylie, in Malech (1910). No `secondReading`: none is held for this rendering.
3. **`briefReferences`**, five entries: Wylie's stele (MAL 13688–13693, 13744–13751, 14141–14142); Legge's stele, parts II.7–11 (LEGGE 1008–1012, 1231–1236, 1256–1257, 1477, 1633–1640, 1863–1871); Legge's lecture on the edict of 845 (LEGGE 4340–4350, 4358, 4389–4390); Yule and Cordier (YULE 2908–2910, 2929–2931); the census tradition (spoken name, Source_Sheet S5).
4. **`sources.about`**, appended: James Legge's 1888 translation of the stele, with notes and lecture, `cic/texts/legge_nestorian-monument-of-hsi-an-fu_trubner1888.txt`.

## Clearly wrong

5. **`knownFor`.** Old: "The man from Syria who". New: "The man from the far west who". Evidence: Legge's English of the stele has "the kingdom of Ta Ts'in" (LEGGE 1011, 1245) and places his start only in "Ta Ts'in, the Far West from China" (LEGGE 4117–4118); "Syria" is Wylie's rendering (MAL 13687–13688), which the card's own `placeNote` already marks. Brief: "who brought the books of the Church of the East from the far west".
6. **`knownFor`.** Old: "ordered a church built". New: "ordered a monastery built". Evidence: Legge, "built a Ta Ts'in monastery … to accommodate twenty-one priests" (LEGGE 1256–1257, 1477), with his note "Not 'a church;'" (LEGGE 1285); Saeki via Budge, "A Ta-ch'in monastery was built in the capital" (BUDGE 5209–5211). Brief: "Officials built a monastery in the capital for twenty-one priests."
7. **`legacy.traces`, third item.** Old: "… no fewer than three thousand, back to private life." New: "… no fewer than three thousand, back to private life; the edict as James Legge quotes it counts in that number the teachers of the Mu-hu-pi, another foreign religion." Evidence: LEGGE 4346–4350 ("as well those of Ta Ts'in as of Mu-hu-pi, amounting to more than 3,000 persons"), LEGGE 4389–4390; YULE 3291–3292. Brief: "sent more than three thousand foreign teachers, Christians and others, back to ordinary life." Williams's own words (MAL 14249–14252) are kept as his report.

## Left in place

- `legacy.traces`, first item ("churches built in every province … every city was full of churches") and second ("slanders in 713"): Wylie's rendering, attributed to the stele (MAL 13739–13748). Legge has monasteries in every prefecture filling "a hundred cities" (LEGGE 1634–1642) and 712 (LEGGE 1863). A translators' difference, not contradicted; the brief does not speak to it.
- `knownFor` "A decree of 638 ordered": Wylie puts the building inside the decree (MAL 13709–13711); Legge only "thinks" the decree ends before it (LEGGE 1279). Not clearly contradicted.

## Not found

None. Each card claim checked was found at its source, including Kircher's title as Assemani gives it ("Epifeopi magnet legis, quee gubernat regnum Sinte", assemani 35967) and Assemani's 636 (35905, 55233).
