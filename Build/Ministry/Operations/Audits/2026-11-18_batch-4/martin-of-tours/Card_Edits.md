# Card edits: Martin of Tours

Card writer, 2026-11-18. Worked from the census card for `martin-of-tours` (`cic-website/data/world-census.json`, its `card` object), `martin-of-tours.brief.txt` (587 words), `Outline.md` and `Source_Sheet.md`. Output: `martin-of-tours.card.json`. Keys as the census has them; no `briefLength`, which the census check does not allow. Every other field is kept word for word and in order. File abbreviations: NP11 = `cic/texts/npnf211_sulpitius-severus-vincent-lerins-cassian.xml`; GT = `cic/texts/gregory-tours_history-of-the-franks-selections_brehaut1916.txt`.

## New

| # | Old words | New words | Evidence |
|---|---|---|---|
| N1 | (none) | `briefReferences`, after Life 5 and 7: "Life 6: publicly scourged by the Arians and driven from a city; expelled from his monastery at Milan." | Brief: "Arian opponents had him beaten in public and driven from a city, and expelled him from a monastery he had set up at Milan." NP11 942-953 ("publicly scourged ... compelled to leave the city"; "a monastery for himself at Milan"; Auxentius "violently expelled him"). Chapter VI heading NP11 922-924. |
| N2 | (none) | `briefReferences`, after Life 10: "Life 13–15: temples torn down and churches built where they had stood; the crowd at Leprosum that drove him off hurt; the pagans his preaching moved to pull down their own temples." | Brief: "He tore down pagan temples and built churches where they had stood. Sometimes his preaching moved people to pull down their own, but once a crowd drove him off and he was hurt." NP11 1244-1248, 1296-1298, 1319-1323, 1365-1369. |
| N3 | Life 10: "a bishop who kept a monk's life; ... eighty disciples. Life 10 also: many of his monks made bishops." | "a bishop who kept a monk's life and plain dress; ... eighty disciples, who held everything in common. Life 10 also: many of his monks made bishops, and cities that wanted their priests from his monastery." | Brief: "as bishop he kept that plain dress"; "eighty disciples who held everything in common"; "Cities wanted their priests from Martin's monastery". NP11 1119-1125 ("the same homeliness in his garments"), 1139-1140 ("all things were possessed in common"), 1155-1158. |
| N4 | Epistle III: "almost two thousand monks at his funeral, as it was said." | "his last journey, to make peace among quarreling clergy, knowing his end was near; almost two thousand monks at his funeral, as it was said." | Brief: "Old, and knowing his end was near, he went to Candes ... to make peace among quarreling clergy." NP11 2380-2390. |
| N5 | Gregory: "...; Gregory's words at the council in Paris on Maximus and Martin." | "...; his death at Candes, a village of his diocese. Brehaut's note: the Life a model for saints' lives." | Brief: "Candes, a village of his diocese"; "a book a modern historian calls a model for later lives of saints." GT 1470-1477 (Book 1, ch. 48); GT 11933-11936 ("became a model for saints' lives"). The council clause is removed: see W5. |
| N6 | `quotationOriginals[1]`, modern "it was a cruel wrong, ..." | "It was a cruel wrong, never heard of before, for a judge of this world to try a case of the church." | The brief's span starts a sentence with a capital: `he said: "It was a cruel wrong ...`. Only the case of the first letter changes; the words, printed text, Latin, files and lines are the same, so the census entry's `secondReading` ("minor") is copied. |

## Clearly wrong: `briefReferences` that name what the brief no longer says, or quote words it does not hold

| # | Old words | New words | Evidence |
|---|---|---|---|
| W1 | Life 3: "...; the onlookers who laughed and those who groaned." | (clause removed) | The brief has no onlookers. |
| W2 | Life 4: "and Sulpicius's \"who can doubt that this victory was due to the saintly man?\"" | "and Sulpicius's credit to Martin for the peace." | Those words are not in the brief, so they may not stand in quotation marks. Brief: "Sulpicius credits Martin with that peace." NP11 855-856. |
| W3 | "Life 9: Ruricius and the pretended sick wife; the crowds and \"a kind of guard\"." | "Life 9: the bishops who scorned his looks, clothes and hair." | The brief has no Ruricius, no crowds and no "a kind of guard". Brief: "some bishops scorned his poor looks, clothes and hair". NP11 1076-1081. |
| W4 | "Dialogue I (Postumianus): the Life sold in Rome and read in Carthage, Alexandria and Egypt, as Sulpicius claims." | (removed) | The brief does not say where the Life was read. |
| W5 | Gregory: "Gregory's words at the council in Paris on Maximus and Martin." | (removed; see N5) | The brief has no council in Paris. |

## Left alone

- `otherNames`, `knownFor`, `datesNote`, `placeNote`, `role`, `legacy`, `uncertain`, `sources`: nothing in the brief or a held source contradicts them.
- `knownFor` says he pleaded that Priscillian's case "was not for an emperor to judge". `Outline.md` warns the brief off this shorthand in favor of "a judge of this world" (Latin *iudex saeculi*). No source contradicts it: Martin made the plea to the emperor Maximus (NP11 11652-11660), and the brief says the case was tried "before the emperor Maximus". Left in place; flagged here.
- `quotationOriginals[0]` ("I am Christ's soldier. I am not allowed to fight."): modern wording and source unchanged; `secondReading` "same" copied. Re-read NP11 841-842 and Halm 6335-6337.
- `quotationOriginals[1]` re-read at NP11 11657-11660 (the printed words begin on 11658; the range holds them) and Halm 5905-5907.
- The Gregory source title names Book 1, chapters 36 and 48. The tomb references (Perpetuus, Clovis) draw on later books of the same file. The title is incomplete rather than contradicted; left in place.
- `briefReferences` on Life 2, Life 5 and 7, Life 25, the Chronicle, Dialogue III and the census match the brief.

## Not found

None.

## Second readings

- Copied: `quotationOriginals[0]` "same"; `quotationOriginals[1]` "minor" (case of the first letter only).
- Awaiting second reading: none. No span is new.


## Card check fixes applied verbatim, 2026-11-18

- `knownFor`: "not for an emperor to judge" became "not for a judge of this world".
