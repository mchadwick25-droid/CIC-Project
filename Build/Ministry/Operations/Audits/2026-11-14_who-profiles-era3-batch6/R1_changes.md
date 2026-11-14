# R1 changes: era 3 batch 6

Round 1 ran in three parts, each by a fresh Opus agent that had not seen the drafting (review) or by the part's drafter (changes). The parts follow, unchanged.

## R1 changes, part A: era 3 batch 6

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

#### Length and readability after the changes

| Profile | Words | Time @162 | FK | Flesch |
|---|---|---|---|---|
| Columbanus (major) | 403 | 2:29 | 7.6 | 67.1 |
| Isidore of Seville (major) | 405 | 2:30 | 7.8 | 64.0 |
| John of Biclaro (recorder) | 325 | 2:00 | 7.9 | 64.6 |

No narrator sentence in any brief runs past 24 words.

## R1 changes: era 3 batch 6, part B

Each part B finding, what was done, and where. Every cited line was opened in its vendored file before the change was made. Audio scripts were rebuilt by script from their briefs (`[calmly] ` at the start, `[warmly] ` before the closing paragraph) and match them once the two tags are removed. `records.json` was edited by a script that re-loaded the file just before writing and changed only `john-moschus`, `babai-the-great` and `severinus-of-noricum`. In `era3/batch5/records.json` only the note of the `henana-of-adiabene` absent detail "A second witness to Babai's doctrinal charges" changed (a one-line diff; indent=1, no trailing newline kept). The README finding (B-M13) was left to the lead, as instructed.

| Finding | Done |
|---|---|
| B-M1 (Moschus: "monks he met") | Taken. Dedication l.3776-3777 ("qui temporibus nostris claruere") and the notice l.24971-24973 ("audisset vel vidisset") confirmed. Brief l.3 and card `knownFor` as worded. A records claim on these lines was added. |
| B-M2 (Moschus: identifiers) | Taken. Brief l.1 "his friend Sophronius, later patriarch of Jerusalem"; l.5 "Photius of Constantinople" (Lipomanus l.3630 confirmed); card `keyWorks` 1 and `dates` "Tiberius II" (l.24460 confirmed). Records claim added. |
| B-M3 (Moschus: length, "long") | Taken for l.1, l.5 (both changes; "non exiguo tempore" for the Jordan only, l.24938-24939, confirmed). For l.7 the proposed "so Sophronius buried him there" puts "there" right after "Sinai", so a listener would hear Sinai. Written instead: "Raiders barred the road to Sinai, so Sophronius buried him at Saint Theodosius." The notice confirms the burial at Saint Theodosius (l.25461-25463). |
| B-M4 (Moschus: the notice's last words) | Taken as worded in card `uncertain`, after "His years". l.25464-25473 confirmed. Records claim added (Dominant Modern Reconstruction). |
| B-M5 (Moschus records: English Meadow note) | Taken as worded. Cotelier's "EX JOHANNIS MOSCHI" heads (l.46158 ff.) and the PG 94 citations "Ex Prato ... Sophronii" (l.91844, 94857, 96433) confirmed. |
| B-B1 (Babai: abbot in the late 500s) | Taken as worded: "Babai was a monk of the Church of the East". Seert l.29652-29653, 29695 and Labourt l.17771-17772 confirmed. |
| B-B2 (Babai: Mari and 'Amr name him; Chabot credited) | Taken. Mari l.13517-13519 ("Mar Babaoo Magno e coenobio Mar Abraliam", "annos docem ot septom") and 'Amr l.13424-13426 confirmed; Chabot's "Comp. 'Amr et Mâri" at l.37361. Card `uncertain` 5 as worded. Records: the absent detail was removed and replaced by a Documented claim (Mari's lines are 13517-13519, not 13514-13517). Mari and 'Amr added to card `sources.about`. |
| B-B3 (Babai: Life of George held whole) | Taken. Braun 1915 l.852-860 (George d. 14 January 615; visitor "608 — 628"), l.12419-12446 (title and Babai's preface) and l.13395-13396 (the resurrection charge), and Hoffmann 1880 l.5596-5612 confirmed. Records absent detail 1, card `keyWorks` 2 and `ownWords` as worded; a records claim on Braun's text was added. |
| B-B4 (Babai: namesakes; Guidi's chronicle) | Taken. Guidi 1903 l.2032-2037, 2051-2058, 2067-2069 and Labourt l.13093-13096 confirmed. Card `uncertain` 6 as worded, with one change: "calls that monk Babai the Little" became "says that monk was called Babai the Little", since the chronicle's "cognominaverunt" has no stated subject. Card `uncertain` 1 got the review's sentence, reworded "tells of a quarrel between his followers and Babai the Little". Records: the Guidi claim and the contested claim "Who Babai bar Nisibnaye was" added; the Book III absent detail now names the chronicle. The chronicle added to `sources.about`. |
| B-B5 (Babai: 612 is Scher's) | Taken as worded in card `legacy.traces` 4. Seert l.29556-29558 and Scher's note l.29565 confirmed. |
| B-M6 (Babai: "the martyr George") | Taken as worded: "His Life of the Izla martyr George". Brief at 404 words. |
| B-M7 (Babai: "lent") | Taken as worded. Labourt l.15764-15766 confirmed. |
| B-M8 (Babai: Labourt's garbled word) | The page image is not held, so the hedge cannot be checked. Card `uncertain` 4 now adds "a word before the dates is lost in the scan of his page"; the records claim's witness and the contested side note the garbled word. |
| B-M9 (Severinus: own name unplaced) | Taken as worded. |
| B-M10 (Severinus: Gisa and Giso) | Taken as worded. Foulke l.2656-2657 and Robinson l.1532 confirmed. |
| B-M11 (Severinus: the grave-opening clue) | Taken as worded. Eugippius l.3964-3966 and Robinson's table l.4866-4871 confirmed. Records claim on the 488 query added. |
| B-M12 (Severinus records: Anonymus Valesianus) | Taken. Mommsen 1892 l.40428-40436 ("de quo ita invenitur in libris vitae beati Severini monachi intra Pannoniam") and l.33502 confirmed; added to the note. |
| B-M13 (README Open-Gaps sentence) | Not touched here: the README finding is the lead's. |
| B-H1 (batch 5 Henana: Life of George held whole) | Taken. The replacement note was written as the review words it. Braun's charges stand at l.13395-13396 inside the cited l.13355-13400, and Hoffmann at l.5596-5612. |
| B-M14 (same note: "lent") | Met by the B-H1 replacement ("made available to him"). |

#### Length and readability after the changes

| Profile | Words | Time @162 | FK | Flesch |
|---|---|---|---|---|
| John Moschus (recorder) | 325 | 2:00 | 7.1 | 68.0 |
| Babai the Great (major) | 404 | 2:30 | 6.8 | 73.0 |
| Severinus of Noricum | 324 | 2:00 | 7.0 | 69.0 |

## R1 changes: era 3 batch 6, part C

Each part C finding, what was done, and where. I opened every cited line in its vendored file before making the change. Audio scripts were rebuilt by script from their briefs (`[calmly] ` at the start, `[warmly] ` before the closing paragraph) and match them once the two tags are removed. `records.json` was edited by one script that re-loaded the file just before writing and changed only `constantius-of-lyon`, `faustus-of-riez`, `gennadius-of-marseilles` and `ruricius-of-limoges` (indent=1, ensure_ascii=False). Constantius's card tradition stays "British and Welsh Christianity", by the coordinator's call.

| Finding | Done |
|---|---|
| C-B1 (Constantius: Krusch's superseded view told as his view) | Taken as worded in card `uncertain` 6 and the records contested claim. Confirmed: Krusch's introduction, `gregory-tours_opera-mgh-srm-1-lat_arndt-krusch1885.txt` l.35826-35829; his note citing Duru's text, l.44304-44306; the addenda, p. 883, l.66229, 66256-66257 ("Iam nullus dubito, quin Vitae scriptor e Gregorio ipso hauserit", OCR "jiuUus"); Levison on Mombritius's text and the interpolated vulgate, with Krusch's p. 883, `constantius-lyon_vita-germani_levison1920.txt` l.659-660, 702-704. |
| C-M1 (Constantius: rendering adds "all", makes the deeds active, runs 27 words) | Taken as worded: "I call God, who knows what is hidden, to witness that I have left out many deeds of my lord Germanus that were known and proved." Levison l.4577-4579 ("Deum testor conscium secretorum, me plura ... agnita et probata tacuisse") confirmed. The records epilogue claim gives the new rendering. |
| C-M2 (Constantius: "Bede, in England" anachronism) | Taken as worded. Levison l.587-589 confirmed. |
| C-M3 (Constantius: length) | Met by C-M1 and C-M2: 323 words. |
| C-M4 (Constantius: "later bishop of Clermont") | Taken: "Sidonius Apollinaris, bishop of Clermont." Dalton HF II.23, `gregory-tours_history-of-the-franks-v2_dalton1927.txt` l.2963-2967, and Levison l.1768-1769 ("paulo post a. 470") confirmed. |
| C-M5 (Constantius card: orders said absent, then given) | Taken as worded in `uncertain` 1 and 2. Rees l.17717-17718 and PL 48 l.20173 confirmed. A records claim was added (tagged Contested). |
| C-M6 (Constantius knownFor: Bede copied parts, not the account) | Taken as worded. Levison l.587-589 confirmed. |
| C-M7 (log the Levison file's truncation) | Not done by me. The brief allows no edits outside batch6/. Passed to the lead for the batch 6 Open-Gaps entry, with the review's two checks: the file ends mid-sentence at l.4579-4580, and the header's stated end (l.9) has no matching line. The missing part is the end of the epilogue and its apparatus on p. 283; the lead is to re-extract p. 283 from archive.org `passionesvitaequesanctorum5`. The records `absent_details` entry is unchanged. |
| F-B1 (Faustus: the scene misreported, Riochatus hid the books) | Taken as worded in the brief, including "a bishop and monk". Barralis, first print l.4757-4772 ("perurbane quae praestantiora portabat operuerit"; "post duos, aut iis amplius menses"; "pernicibus equis insequutus abeuntem"; "quaesitum volumen invenio, produco, lectito, excerpo"), and second print l.5536-5548 confirmed: the two OCR passes agree. Williams, Gildas volume, l.9659-9663, confirmed. Records claim 1 was extended, with all three witnesses (also meets F-M5). |
| F-M1 (Faustus: length) | Taken as worded: the "brushed past his walls" sentence was dropped, and the l.3, l.5 and l.9 cuts were made. 324 words. |
| F-M2 (Faustus: Warfield unintroduced; nested clause) | Taken as worded. `npnf105_augustine-anti-pelagian-writings.xml` l.516-519 ("Professor in the Theological Seminary at Princeton") confirmed. A records claim was added. |
| F-M3 (Faustus: "At last") | Taken through F-M1 ("Then he became bishop of Riez"). |
| F-M4 (Faustus card `place` settles the birthplace) | Taken as worded. Engelbrecht l.146-154 and Avitus l.7378-7379 confirmed. |
| F-M5 (Faustus records: second Barralis print, Williams) | Taken; see F-B1. |
| F-M6 (Faustus: doubled hedge) | Taken as worded: "by the Gothic king Euric, Engelbrecht thinks." Engelbrecht l.322-325 confirmed. |
| G-M1 (Gennadius: the Prosper sentence unclear aloud) | Taken as worded. `npnf203…` l.43666-43669 ("I regard as his also an anonymous book against certain works of Cassianus, which the church of God finds salutary, but which he brands as injurious") confirmed. Both quoted fragments are verbatim. |
| G-M2 (Gennadius: Jackson unintroduced) | Taken as worded, together with the two length merges. Title page l.682-684 confirmed. A records claim was added. |
| G-M3 (Gennadius card: Jackson's is prolegomena, not a note) | Taken as worded. l.3611-3612 (Jackson) and l.43968 (Richardson's endnote) confirmed. |
| G-M4 (Gennadius card: Acta Sanctorum missing from sources) | Taken as worded. `acta-sanctorum_martii-tomus-3-lat-grc_palme1865.txt` l.180635-180636 confirmed. |
| G-M5 (Gennadius records: Scholarios) | Taken. The PG 160 file header l.1-4 was confirmed, and a namesake claim (Documented) was added. |
| R-B1 (Ruricius: the metaphor told as fact) | Taken as worded: "He asks that Faustus's letters be harsher food, fit for a sinner's sickness, in place of the sweet dishes sent so far." Engelbrecht l.20070-20074 and l.20076-20079 ("ne vulneribus meis gratior sit foventis dextera quam secantis") confirmed. The records ep. I.1 claim was extended. |
| R-M1 (Ruricius: 506 is in the acts) | Taken as worded in the brief and card `uncertain` 2. Bruns l.10481-10501 ("habitum era 644 … Anno vicesimo secundo Alarici regis sub die tertio Idus Septembris … Messala v. c. consulem") and PL 67 l.96512-96553 (the prolegomenon; Basnage's view "commentita") confirmed. Records: the 506 claim was retagged Documented, with Bruns as witness. The PL 67 claim and a contested claim, "Why Ruricius missed Agde", were added. Bruns and the PL 67 prolegomenon were added to the card's `sources.about`. |
| R-M2 (Ruricius: Caesarius's pardon left out) | Taken as worded: "Yet he held nothing against him.", with "Ruricius answered" starting a new paragraph. Engelbrecht l.24710-24716 ("nihil pietati vestrae vel potuimus vel debuimus inputare") confirmed. The records Caesarius claim was extended. |
| R-M3 (Ruricius: Krusch unintroduced) | Taken as worded. Krusch stays on the card. |
| R-M4 (Ruricius: length, choppy pair) | Taken as worded. Engelbrecht l.23184-23188 ("ipsi etenim recolere potestis") confirmed. 324 words. |
| R-M5 (Ruricius: held identification of the later signer missed) | Taken as worded in card `uncertain` 5. Leo's index, `venantius-fortunatus_opera-mgh-aa-4-lat_leo-krusch1881.txt` l.53125-53130 ("alter nepos illius interfuit concilio Arverno I. a. 535, Aurelianensi IV. a. 541, V. a. 549", OCR "Huricii", "51)7"), and Maassen l.6019, 8139, 9442 confirmed. A records claim was added and `absent_details` 1 was corrected. |
| R-M6 (Ruricius: 485 rests on Faustus's conditional return year) | Taken as worded in card `uncertain` 1. Engelbrecht l.348-350 ("Quodsi Euricus in causa fuit … anno 485 in patriam hunc rediisse veri simile est") and l.953-959 confirmed. The brief's sentence stands, as the review allows. |
| R-M7 (Ruricius: "Ruricius the elder" not spelled by any source) | Taken: dropped, leaving "Ruricius Lemovicensis". |

None was declined. The one partial is C-M7, which the lead must log because it falls outside the files I may edit.

#### Length and readability after the changes

| Profile | Words | Time @162 | FK | Flesch |
|---|---|---|---|---|
| Constantius of Lyon (recorder) | 323 | 2:00 | 8.0 | 66.1 |
| Faustus of Riez | 324 | 2:00 | 8.1 | 63.1 |
| Gennadius of Marseilles (recorder) | 325 | 2:00 | 8.2 | 64.0 |
| Ruricius of Limoges | 324 | 2:00 | 7.2 | 67.3 |

Narrator sentences past 25 words occur only as lead-ins to quotations or modern renderings. Each `briefLength` stays "about 2 minutes".
