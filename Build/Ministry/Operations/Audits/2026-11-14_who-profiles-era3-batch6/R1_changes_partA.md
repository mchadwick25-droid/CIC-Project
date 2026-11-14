# R1 changes, part A: era 3 batch 6

Each part A finding, what was done, and where. Every cited line was opened in its vendored file before the change was made. Audio scripts were rebuilt by script from their briefs (`[calmly] ` at the start, `[warmly] ` before the closing paragraph) and match them once the two tags are removed. `records.json` was edited by a script that re-loaded the file just before writing and changed only `columbanus`, `isidore-of-seville` and `john-of-biclaro` (indent=1, ensure_ascii=False).

| Finding | Done |
|---|---|
| A-B1 (Columbanus: rendering drops "si boni simus meriti"; "those woods") | Taken, with one wording change. PL 80 l.20758-20765 ("in his silvis silere et vivere", "Capiat nos simul, oro, Gallia, quos capiet regnum coelorum, si boni simus meriti") confirmed. Brief and audio close: "…he had asked to live in silence in the Vosges, by the bones of seventeen dead brothers. "Let Gaul, I pray, hold us together," he wrote, in modern words, "whom the kingdom of heaven will hold, if our merits are good."" The review's "in the Vosges woods" made a 25-word sentence; "woods" was dropped, since the Vosges are the wilderness Jonas names (munro1895 l.362). |
| A-M1 (Columbanus: Nantes is Mabillon's placing) | Taken. PL 80 l.21345 ("hic in vicinia Brittonum") and l.16362-16370, 16380-16382 ("Epistola IV ad suos Luxovienses Namnetis scripta", Mabillon as Gallandi quotes him) confirmed. Brief l.1 as worded ("from near the Bretons"; "He put the news into his letter" removed). Card `keyWorks` 3: "his monks as he waited to be shipped home". Card `uncertain` 6 as worded. Records claim 1 witness extended as worded. |
| A-M2 (Columbanus card `dates` contradicts itself) | Taken: "No early source used here gives his birth year." |
| A-M3 (Columbanus: Ramelen not blessed; 30-word sentence) | Taken as worded. Munro l.664-676 (Donatus raised "from the font"; Ramelen born of the promise) and l.1415-1427 (Ado and Dado blessed as children; note l.1440) confirmed. Records claim reworded to match. |
| A-M4 (Columbanus: "Columbanus of Bobbio") | Taken as worded. Barralis l.36426-36429 confirmed. |
| A-M5 (Columbanus: bare names on the card) | Taken: "Jean Mabillon", "citing Thomas Hodgkin" (`dates`), "James Ussher" and "Melchior Goldast" (`uncertain` 4). `uncertain` 1 keeps "citing Hodgkin", since `dates` now gives the full name first. |
| A-M6 (Columbanus: "poor OCR" on the card; Barralis as author) | Taken as worded. Barralis l.36412-36419 ("EX TOMO SEXTO F. LAVRENTII SVRII") confirmed. |
| A-B2 (Isidore: the Toledo IV canon is about Jews and orders coercion) | Taken as worded in brief, audio and card `legacy.traces` 2. Hispana l.40196-40228 ("De discretione judaeorum"; "De judaeis autem … nemini deinceps ad credendum vim inferre"; "tenere cogantur") confirmed. Records claim now quotes the heading and cites l.40196-40228. |
| A-B3 (Isidore: Seville II "in 619" told as settled) | Taken. Hispana l.59339-59345 (era 657, Sisebut's ninth year), brehaut1912 l.701-702, 718, mansi10 l.57663-57665 and Pagi's note l.59503-59536 (OCR "628", "648" for 618), Alcuin PL 100-101 l.27622-27628 (Vasaeus) and Bruns l.27403 ("618 Hispalense II") confirmed. Brief and audio: "Under King Sisebut, Isidore is named first…". Card: new `uncertain` 5, with the forename left out ("Pagi", as Mansi names him), and "later Spanish chroniclers" in place of "Isidore of Beja and later Spanish writers", since Mommsen calls the "Isidore of Beja" name fictitious (mommsen1894 l.16362-16363). Card `uncertain` 4 drops "in 619". Records: Seville II claim tagged Contested; new `contested_claim` with the three sides as worded. |
| A-B4 (Isidore: Redemptus's account is retold and quoted in Poschmann) | Taken. Poschmann l.15200-15240 confirmed. Card `uncertain` 3 ends as worded; Poschmann added to `sources.about`; records `absent_details` corrected as worded and a Poschmann claim added (Dominant Modern Reconstruction). |
| A-M7 (Isidore: renderings not marked) | Taken as worded: marker sentence after "he pleaded"; quotation marks removed from the Sisebut line; "in Brehaut's English" added to the close; l.5 shortened to "Theodor Mommsen sets his death in 636." |
| A-M8 (Isidore: Cicero is Brehaut's identification) | Taken, split into two sentences for length. Brehaut l.752-753 ("the famous words of the philosopher") and note 24 at l.772-773 confirmed. Records witness corrected. |
| A-M9 (Isidore: Brehaut on the Braulio side) | Taken. Brehaut l.1158-1159 and Lindsay l.337-338 confirmed; sentence added to the card item; records side extended. |
| A-M10 (Isidore: "Redemptus", "Flórez" bare) | Taken: "the cleric Redemptus" (Brehaut l.702-703), "Enrique Flórez". |
| A-M11 (John: "short notice") | Taken as worded in brief and card `uncertain` 1. Mommsen l.19385-19387 ("solito diligentius et plenius") confirmed; records claim added. |
| A-M12 (John: Goiswinth against batch 5's Gosuintha) | Taken. mommsen1894 l.20115 ("Gosuinthae") confirmed. Brief: "Leovigild's queen, Gosuintha." |
| A-M13 (John: "learned Greek and Latin") | Taken as worded. mommsen1894 l.19388 ("Graeca et Latina eruditione nutritus") confirmed. |
| A-M14 (John: renderings not marked) | Taken as worded: both lines told in reported speech. |
| A-M15 (John: "Mariana", "Calmet" bare) | Taken: "Juan de Mariana", "Augustin Calmet". |
| A-B5 (John: the Chronicle does not end with the council) | Taken. mommsen1894 l.20423-20437, 20460-20467 (the Persian king, Argimund's plot and punishment, the reckoning of years) confirmed. `keyWorks` 1 and `knownFor` as worded, `keyWorks` split into two sentences for length. Records claim added. |
| Note: Breviarium Gothicum preface (Toledo IV) | Added, as the review allowed. PL 86 l.474 ("concil. iv Tolet., praeside sancto Isidoro") confirmed. Card `uncertain` 4 and the records' presiding `contested_claim` now include it. |
| Note: Barralis reads the twentieth year | Added to the records' `contested_claim` on his age at leaving (barralis l.36689). |

None was declined. Further changes that follow from the fixes: the briefLength fields read "about 2 minutes 30 seconds" for Columbanus and Isidore. `"date": null` was added to `sources.about` entries with no date, following the batch 5 C-M12 fix. Card sentences that the fixes pushed past 25 words were split (Columbanus `keyWorks` 3, Isidore `legacy.remembered` 2, John `keyWorks` 1 and `uncertain` 4). John `uncertain` 4 now says Ildefonsus has Nonnitus follow "a John", matching `legacy.traces` 3.

### Length and readability after the changes

| Profile | Words | Time @162 | FK | Flesch |
|---|---|---|---|---|
| Columbanus (major) | 403 | 2:29 | 7.6 | 67.1 |
| Isidore of Seville (major) | 405 | 2:30 | 7.8 | 64.0 |
| John of Biclaro (recorder) | 325 | 2:00 | 7.9 | 64.6 |

No narrator sentence in any brief runs past 24 words.
