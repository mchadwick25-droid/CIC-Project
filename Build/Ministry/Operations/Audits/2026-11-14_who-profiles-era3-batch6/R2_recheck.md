# R2 recheck: era 3 batch 6

Round 2 was a targeted recheck in three parts, each by a fresh Opus agent that had not seen the drafting or round 1, at full effort. The parts follow, unchanged.

## R2 recheck, part A: era 3 batch 6

Scope: Columbanus, Isidore of Seville and John of Biclaro, with their cards, audio scripts and `records.json` entries. Round 2 of at most 3, a targeted recheck.

### Method

I am a fresh Opus reviewer; I did not draft, review or fix these files in round 1. I read `CLAUDE.md`, the part A sections of `R1_review.md` and `R1_changes.md`, and batch 5's `R2_recheck.md` for shape. I read the changes as a word diff from the drafts R1 reviewed to HEAD (`deb3cc1d`). For the briefs and cards that base is `0863d05b`; it is unchanged at `a55b43c8`, the first commit that holds the merged `records.json`, which I used as the records base. For every R1 finding I opened the cited lines in the vendored file myself and checked who speaks there. I then checked every new or changed string in brief, card, audio and records against its source, and against the writing standard (`CLAUDE.md`, "No AI tells"; `Who_Profile_Pattern.md` item 4). Before accepting the one new absence ("Redemptus's text itself is not held") I searched all of `cic/texts/` for Redemptus/Redemtus, "De obitu Isidori" and the confession's Latin. The only hits are Mommsen, Brehaut and Poschmann, so the absence holds. I edited no profile file, and made no git write, web or paid calls. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines, so paragraphs sit on l.1, 3, 5 and so on.

Mechanical checks, all three:
- Each audio script equals its brief once `[calmly] ` (start) and `[warmly] ` are removed, checked by script. Each has one `[calmly]` at the start and one `[warmly]`, at the start of the closing paragraph. No tag appears in a brief or card.
- `grade_text` passes for all three (table below).
- No narrator sentence runs past 24 words. On the cards, one changed string runs past about 25 words (R2-A-M1); John's `keyWorks` 1 first sentence is 26, which is about 25.
- `briefLength` matches. All three cards and `records.json` parse; every `file` named in the three cards exists.

| Profile | Words | Time @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Columbanus (major) | 403 | 2:29 | 7.6 | 67.1 | within 405 |
| Isidore of Seville (major) | 405 | 2:30 | 7.8 | 64.0 | 405, at the cap |
| John of Biclaro (recorder) | 325 | 2:00 | 7.9 | 64.6 | 325, at the cap |

### 1. R1 findings

| Finding | Status | Evidence |
|---|---|---|
| A-B1 (Columbanus: rendering drops "si boni simus meriti") | RESOLVED | Brief l.13 now ends "…whom the kingdom of heaven will hold, if our merits are good." and is marked "in modern words". PL 80 l.20763-20765: "Capiat nos simul, oro, Gallia, quos capiet regnum coelorum, si boni simus meriti." The departure ("the Vosges" for "the Vosges woods") is sound: "in his silvis" (l.20759) is the Luxeuil country, which Jonas calls the Vosges wilderness (munro1895 l.362), and the brief says so at l.7. |
| A-M1 (Columbanus: Nantes is Mabillon's placing) | RESOLVED | Brief l.1: "from near the Bretons"; the letter: "fratres vestri hic in vicinia Brittonum sunt" (PL 80 l.21344-21345). Mabillon, as Gallandi quotes him: "ex ejus Epistola IV ad suos Luxovienses Namnetis scripta" (l.16369-16370). Card `uncertain` 6 and records claim 1 match. |
| A-M2 (Columbanus: `dates` contradicts itself) | RESOLVED | "No early source used here gives his birth year." |
| A-M3 (Columbanus: Ramelen not blessed; 30 words) | RESOLVED | Munro: Donatus raised "from the font" and "founded a monastery under Columban's rule" (l.668-672); Ramelen "founded under his rule a monastery in the Jura" (l.679-680); Ado and Dado blessed as children, each founding a house (l.1418-1427); note "The monastery Jouarre near Meaux" (l.1440). |
| A-M4 (Columbanus: "Columbanus of Bobbio") | RESOLVED | "…from Attala and Eustasius, who followed Columbanus as abbots of Bobbio and Luxeuil." Barralis l.36426-36429. |
| A-M5 (Columbanus: bare names) | RESOLVED | "Jean Mabillon" and "Thomas Hodgkin" in `dates`, "James Ussher" and "Melchior Goldast" in `uncertain` 4. `uncertain` 1 keeps "citing Hodgkin" after the full name in `dates`; sound. |
| A-M6 (Columbanus: "poor OCR"; Barralis as author) | RESOLVED | Title now "…from Laurentius Surius, as printed by Vincentius Barralis…", author "Jonas of Bobbio". Barralis l.36414-36415, "EX TOMO SEXTO F. LAVRENTII SVRII". |
| A-B2 (Isidore: the Toledo IV canon is about Jews and orders coercion) | RESOLVED | Brief l.9: "from then on no Jew should be forced to believe. Jews already forced into baptism under King Sisebut, it added, must be made to keep the faith they had received." Hispana l.40198-40228: "De discretione judaeorum"; "De judaeis autem … nemini deinceps ad credendum vim inferre"; "oportet ut fidem etiam quam vi vel necessitate susceperunt tenere cogantur". Card `legacy.traces` 2 and the records claim match. |
| A-B3 (Isidore: Seville II "in 619" told as settled) | RESOLVED in the brief; the new card item is PARTLY right (R2-A-M2) | Brief l.7: "Under King Sisebut, …". Acts: "HABITUM DIE IDUUM NOVEMBRIUM ANNO NONO REGNI … SISEBUTI" (Hispana l.59339-59343). The new contested claim and the Contested tag are right, and the records keep Pagi's condition. The drafter's two departures are sound. "Pagi" without a forename follows what Mansi prints. "Later Spanish chroniclers" stands in for "Isidore of Beja", since Mommsen calls that name "ficticio" (mommsen1894 l.16362-16363). But the card leaves out Pagi's own condition on 618: R2-A-M2. |
| A-B4 (Isidore: Redemptus's account is held through Poschmann) | RESOLVED | Card `uncertain` 3: "Bernhard Poschmann retells Redemptus's account and quotes its Latin. Isidore, he reports, had himself carried into the church of Saint Vincent and did public penance before the people and two bishops." Poschmann l.15203-15211 (OCR "lief}"): "ließ er sich in die Kirche des hl. Martyrers Vincentius tragen … bekannte er vor allem Volke, vor den anwesenden Klerikern und zwei befreundeten Bischöfen"; "peccavi super numerum arene maris" (l.15212-15215). Source entry added; the records absence and the new claim are right. |
| A-M7 (Isidore: renderings not marked) | RESOLVED | Marker after "he pleaded"; the Sisebut line is in reported speech; l.13 "in Brehaut's English" (brehaut1912 l.3591-3592). |
| A-M8 (Isidore: Cicero is Brehaut's identification) | RESOLVED | "…words of "the philosopher", which Ernest Brehaut traces to Cicero writing to Varro." Brehaut l.752-753 and note 24, l.772-773. |
| A-M9 (Isidore: Brehaut on the Braulio side) | RESOLVED | "Ernest Brehaut calls the preface addressed to Braulio." Brehaut l.1158-1159: "the brief preface, addressed to Braulio". |
| A-M10 (Isidore: "Redemptus", "Flórez" bare) | RESOLVED | "the cleric Redemptus" (Brehaut l.704, "a cleric named Redemptus"); "Enrique Flórez". |
| A-B5 (John: the Chronicle does not end with the council) | RESOLVED | `keyWorks` 1: "Its last year tells of the Third Council of Toledo and a plot against Reccared"; `knownFor`: "runs to King Reccared's fourth year, the year of the Third Council of Toledo". mommsen1894 l.20388-20389 ("ANNO VIII MAVRICII … QVI EST RECCAREDI REGIS IIII ANNVS"), l.20423-20437 and 20460-20467 (the Persian king, Argimund, the reckoning from Adam). |
| A-M11 (John: "short notice") | RESOLVED | Brief l.3: "Isidore's notice of him"; card: "which Theodor Mommsen calls fuller than Isidore's usual". mommsen1894 l.19387-19388: "solito diligentius et plenius enarrans". |
| A-M12 (John: Goiswinth) | RESOLVED | "Gosuintha"; mommsen1894 l.19837, 20339, 20342; batch 5 `reccared` card agrees. |
| A-M13 (John: "learned Greek and Latin") | RESOLVED | "was schooled there in Greek and Latin learning"; l.19390, "Graeca et Latina eruditione nutritus". |
| A-M14 (John: renderings not marked) | RESOLVED | Both lines in reported speech; "vidimus" (l.19930-19931), "ex parte quod oculata fide pervidimus et ex parte quae ex relatu fidelium didicimus" (l.19772-19773). |
| A-M15 (John: "Mariana", "Calmet" bare) | RESOLVED | "Juan de Mariana", "Augustin Calmet". |

The two notes R1 allowed were also taken. Barralis's twentieth year is right: "vigesimum aetatis annum agens" (l.36689). The Breviarium Gothicum preface reads "concil. iv Tolet., praeside sancto Isidoro" (PL 86 l.474), but the card and records name the wrong witness for it (R2-A-M3).

Totals: 5 of 5 blocking resolved (A-B3 with a new minor point on its card item); 15 of 15 minor resolved.

### 2. New findings

No blocking findings. Four minor.

- **R2-A-M1 MINOR (`columbanus.card.json`, `keyWorks` 3 `about`; sentence length, made by the R1 fix).** "six letters under his name: two to Pope Boniface IV, and one each to Pope Gregory the Great, a council of Gallic bishops, a disciple, and his monks as he waited to be shipped home." This runs 35 words (the draft's was 31), past the 25-word bar that R1 applied to the cards (A-M3, A-M4). R1_changes says this field was split for length, but the long first part remains.
  - Fix: "six letters under his name. Two went to Pope Boniface IV, and one each to Pope Gregory the Great, a council of Gallic bishops and a disciple. Another went to his monks as he waited to be shipped home. In several he names himself Columba, a dove"

- **R2-A-M2 MINOR (`isidore-of-seville.card.json`, `uncertain` 5; a scholar's conditional view told flat, made by the A-B3 fix).** "He follows later Spanish chroniclers, who give Sisebut's seventh year, and sets it in 618." Pagi makes 618 depend on the month, and says the month is not clear: "Horum trium Historicorum sententia praeferenda, & haec synodus ad an. 618 retrahenda, si tamen mense Novembri aut Decembri celebrata sit, qua de re non satis liquet" (mansi10 l.59531-59534; OCR "Horum crium", "648", "fity"). The records side keeps the condition; the card drops it. This is the same kind of fault as A-B1, a condition cut from a source.
  - Fix: "He follows later Spanish chroniclers, who give Sisebut's seventh year. That sets it in 618, he says, if it met in November or December, which is not clear."

- **R2-A-M3 MINOR (`isidore-of-seville.card.json`, `uncertain` 4, and `records.json` `isidore-of-seville` claim "Preface to Migne's Breviarium Gothicum" and the contested claim "Whether he presided at Toledo IV"; item 5, a role given in place of a named witness, and the wrong editor).** Card: "The preface to the Breviarium Gothicum in Migne's edition says he did." The preface is Francisco Antonio Lorenzana's own address to the reader: "FRANCISCUS ANTONIUS LORENZANA, … LECTORI SALUTEM" (PL 86 l.385-390). The line it relies on comes within it (l.474), before his next heading at l.669. The file header gives the edition as "opera Fr. Ant. Lorenzana recognitum" (editor, 1775), which Migne reprints (l.1-2). "Migne's edition" makes the reprinter the editor; that is the same kind of swap A-M6 fixed for Barralis. Also, the card cites this preface, and Pagi's note in Mansi 10 (`uncertain` 5), but neither file is in `sources.about`. The Poschmann witness added under A-B4 is listed there.
  - Fix, card `uncertain` 4: "Francisco Antonio Lorenzana, in his preface to the Breviarium Gothicum, says he did."
  - Fix, card `sources.about`, add two entries: `{"title": "Preface to the Breviarium Gothicum, in Patrologia Latina 86", "author": "Francisco Antonio Lorenzana", "date": "1775", "language": "Latin", "file": "cic/texts/mozarabic-liturgy_breviarium-gothicum-pl86-lat_migne1862.txt"}` and `{"title": "Note on the year of the Second Council of Seville, in Sacrorum conciliorum collectio 10 (ed. Giovanni Domenico Mansi)", "author": "Pagi", "language": "Latin", "file": "cic/texts/mansi_sacrorum-conciliorum-collectio-tomus-10-lat_welter-facsimile1901.txt"}`. (Fit the `date` key to whatever R2-A-M4 settles.)
  - Fix, records: the claim reads "Lorenzana's preface to the Breviarium Gothicum, reprinted in PL 86: 'concil. iv Tolet., praeside sancto Isidoro'", witness "mozarabic-liturgy_breviarium-gothicum-pl86-lat_migne1862 l.385-390, 474". In the contested claim's second side, "the preface to the Breviarium Gothicum in PL 86" becomes "Lorenzana's preface to the Breviarium Gothicum, PL 86".

- **R2-A-M4 MINOR (all three cards, `sources`; schema, made by R1).** R1 added `"date": null` to 12 `sources.about` entries (Columbanus 3, Isidore 4, John 5), "following the batch 5 C-M12 fix". The batch README says otherwise: "A field with no content is left out" (`Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/README.md` l.14). Batch 5 ruled both ways, B-M16 (delete a null `date`) and C-M12 (add one). The cards now mix the two forms. The `ownWords` entries with no date omit the key, while the `about` entries carry `null`, as in Isidore `ownWords` 3, 5 and 6 against `about` 1, 3, 4 and 5. The same mix runs through parts B and C. This needs one ruling for the batch, not a per-part fix.
  - Fix (README rule): delete every `"date": null` line from the three cards. If the coordinator rules for C-M12 instead, add `"date": null` to every dateless `ownWords` entry, and amend README l.14 to say a source with no date carries `"date": null`.

Nothing else in the changed text fails the writing bar. I found no new contrast, colon-reveal, tail, triad or unearned adjective. The marker "Their Latin is told here in modern words." follows the batch 4 and 5 form. "Had zeal, but not according to knowledge" is Isidore's own phrase (Romans 10:2) in reported speech, not a narrator's contrast.

### 3. Verdicts

- `columbanus`: CLEAR once R2-A-M1 is applied (minor only; R2-A-M4 batch-wide).
- `isidore-of-seville`: CLEAR once R2-A-M2 and R2-A-M3 are applied (minor only; R2-A-M4 batch-wide).
- `john-of-biclaro`: CLEAR (R2-A-M4 batch-wide only).

No blocking finding remains on part A. The fixes touch cards and records only, so brief lengths and readability scores do not change.

## R2 recheck, part B: John Moschus, Babai the Great, Severinus of Noricum (era 3 batch 6)

#### Method

Scope: `john-moschus`, `babai-the-great` and `severinus-of-noricum` in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/`, with their briefs, cards, audio scripts and `records.json` entries, and the one change to `era3/batch5/records.json`. I am a fresh Opus reviewer. I did not draft these files or fix them. I read the R1 part B review and the part B changes. I read the changes as a word diff from `65412883`, the drafts R1 reviewed, to HEAD (`deb3cc1d`). For `records.json` I compared each of the three entries field by field. I opened every new or changed sentence, quotation and records entry at its line in the vendored file, and checked who is speaking there: the ancient writer, a document he copies, a translator, or an editor's note or heading. Quotations were matched with whitespace collapsed, and OCR passages were read line by line. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines, so paragraphs sit on l.1, 3, 5 and so on. I edited no profile file, made no git commit, model call or web call.

Coordinator rulings applied: Babai the Great is major (about 405 words at most). John Moschus is a recorder at standard length, and Severinus is standard (about 325 words at most each). Severinus's card tradition is the coordinator's call. R1's B-M13 (the README says Severinus's tradition correction "is logged in Open-Gaps") belongs to the lead's Open-Gaps entry, written before merge, and is marked pending.

Mechanical checks, all three:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`, at the start of the closing paragraph. No tag appears in a brief or card.
- `grade_text`, run from the repo root, passes on all three.
- No narrator sentence runs past 25 words. Babai l.13 has 30, of which 24 are Thomas's quoted words.
- All three cards and both `records.json` files parse. Every `file` named in the three cards' sources exists, including the four new Babai entries (Braun 1915, Mari, 'Amr, Guidi).

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| John Moschus (recorder) | 325 | 2:00 | 7.1 | 68.0 | 325, at the cap |
| Babai the Great (major) | 404 | 2:30 | 6.8 | 73.0 | within 405 |
| Severinus of Noricum | 324 | 2:00 | 7.0 | 69.0 | within 325 |

#### 1. R1 findings

| Finding | Status | Evidence |
|---|---|---|
| B-M1 (Moschus: "monks he met") | RESOLVED | Brief l.3 "stories about monks of his time, written for Sophronius"; card `knownFor` "monks of his time, seen on their travels or told to them". Dedication "virtutes sanctorum virorum, qui temporibus no- / stris claruere" (pg87-3 l.3776-3777); notice "si quid de vita ... audisset vel vidisset, id seriptis manda- / ret" (l.24971-24973). New records claim matches. |
| B-M2 (Moschus: identifiers) | RESOLVED | Brief l.1 "Sophronius, later patriarch of Jerusalem"; l.5 "Photius of Constantinople" (Lipomanus, "Photius patriarcha Constantinopolitanus", l.3630); card `keyWorks` 1 is the card's first Photius; `dates` "Tiberius II" ("temporibus / Tiberii II imp.", l.24459-24460). |
| B-M3 (Moschus: length, "long") | RESOLVED | 325 words. l.5 "He lived long in the desert by the Jordan, then at the New Laura" keeps "long" to the Jordan ("non / exiguo tempore", l.24938-24939). The drafter's departure on l.7, "so Sophronius buried him at Saint Theodosius", is sound: R1's "there" would have pointed to Sinai. The notice has him laid "in S. Theodosii cœmeterio" (l.25461-25463). |
| B-M4 (Moschus: the notice's last words) | RESOLVED | Card `uncertain`, "The disciple": notice "reliquumque vitz suæ tempus in eodem cœnobio / tran<egit" (l.25464-25465); Papebroch "nisi alium a So- / phronio Hierosolymitano Moschi socium fuisse / velimus credere (contra totius pene Crece anti- / quitatis congensum ...) ... de longe / maxima vitz reliquæ parte" (l.25466-25471). "Most of the rest of his life" is a fair rendering of "longe maxima parte". |
| B-M5 (Moschus records: English Meadow note) | RESOLVED | Cotelier "EX JOHANNIS MOSCHI" running heads from l.46158 to l.59643; PG 94 "Ex Prato (cap. 45) S. P. V. Sophronii", "Ex Prato S. P. N. Sophronii", "in Prato saneti Sophronii" (l.91844, 94857, 96433). |
| B-B1 (Babai: abbot in the late 500s) | RESOLVED | Brief l.3 "Babai was a monk of the Church of the East". Scher, "en 603/4" (seert l.29695); Labourt, "entre 615 et 620" (labourt1904 l.17771-17772). |
| B-B2 (Babai: Mari and 'Amr; Chabot credited) | RESOLVED | Mari: "Proprio ilaque / patriarcha occlosia oaruit ad annos docem ot septom, oius intoroa guberna- / tionom gorontibus Mar Aba arcliidiacono alquo Mar Babaoo Magno e coe- / nobio Mar Abraliam" (gismondi1899 l.13517-13520). 'Amr: "Sedem / itaque administravit [citra ordinationem ut vicarius] Mar A!ia archidiaconus / una cum Mar iJabae-) ^lngno" (gismondi1896-1897 l.13424-13426). Chabot: "Comp. 'Aur et MÂri dans la Vie du patriarche Grégoire" (chabot1902 l.37361). The drafter's correction of Mari's lines to 13517-13519 is right, though the quotation's last words, "nobio Mar Abraliam", stand on l.13520. The absent detail is gone and a Documented claim replaces it. One long sentence in the new card text: R2-B-M2. |
| B-B3 (Babai: Life of George held) | PARTLY | The false absence is gone. Braun's title "verfaßt vom heiligen Rabban Mär / Bäbai, dem Abte auf dem Berge Izalä" (braun1915 l.12421-12423), the preface (l.12435-12439), the charge (l.13393-13396), Braun's heading "f 14. Jan. 615 ... 608 — 628 unter dem Titel eines / Klostervisitators" (l.852-858) and Hoffmann (l.5596-5612) all check. But R1's own word "whole", taken as worded into card `keyWorks` 2 and two records entries, is false: R2-B-B1. |
| B-B4 (Babai: namesakes; Guidi's chronicle) | RESOLVED | Guidi: "Màr / Babhay filius Nisibenorum" (guidi1903 l.2036-2037); "duo Babhay" (l.2051); "Asseclae, monachi, Mar Babhay magni (maioris) nemini permittebant / ul in suum monasterium intraret, quin anathema diceret in exi- / mium Maàr Babhay nisibenum quem Babhay parvum (minorem)" (l.2053-2055), "cognominaverunt" (l.2064). Budge: "He must be distinguished from / Babhai bar-Nesibhnaye, who flourished under the Catholicus / [Selibha-zekha] (A. D. 713 — 729), and who was famous for his / beautiful voice" (budge1893 l.2070-2073). Abdisho in Badger: "Babai, the Scribe, of Maarra" (badger v2 l.17990). The drafter's "says that monk was called Babai the Little" is a sound departure: "cognominaverunt" has no named subject. The reworded `uncertain` 1 sentence and the line ranges need care: R2-B-M1. |
| B-B5 (Babai: 612 is Scher's) | RESOLVED | Card `legacy.traces` 4. The chronicle gives no year (seert l.29556-29558); "1. En 612" is Scher's note (l.29565). The new clause can attach to the wrong noun: R2-B-M2. |
| B-M6 (Babai: "the martyr George") | RESOLVED | Brief l.7 "His Life of the Izla martyr George". Braun: "Martyrium des Mönches Georg ... Geschrieben von seinem Abte" (braun1915 l.852-854). |
| B-M7 (Babai: "lent") | RESOLVED | Card `keyWorks` 1 "made available to him". Labourt: "Grâce à l'obligeance de M. Chabot, nous sommes en mesure d'adjoindre / à ces textes un traité inédit de Babaï" (labourt1904 l.15764-15765). |
| B-M8 (Babai: Labourt's garbled word) | RESOLVED | The page image is not held, so the drafter's answer, to flag the word on the card, the records claim and the contested side, is sound. The OCR reads "Il mourut âgé de soixante-quinze ans, phone / 'entre 615 et 620" (l.17771-17772). The card's wording of the flag is slightly off: R2-B-M3. |
| B-M9 (Severinus: own name unplaced) | RESOLVED | Brief l.1 "Severinus of Noricum felt a pain in his side". |
| B-M10 (Severinus: Gisa and Giso) | RESOLVED | Card `legacy.traces` 3 "his wife, whom Paul calls Gisa". Paul: "this Feletheus of whom we have spoken and his wife, / whose name was Gisa" (foulke1907 l.2656-2657). |
| B-M11 (Severinus: the grave-opening clue) | RESOLVED | Card `uncertain` 3. Eugippius: "Onoulfus, however, at his brother's command or- / dered all the Romans to migrate to Italy" (robinson1914 l.3927-3928); "for the sixth year of / his burial had already passed" (l.3965-3966). Robinson's table: "487. Odoacer wages war on the Rugii" (l.4866), "488 ? Fredericus returns ... Onoiilfus" (l.4869-4871), and the provincials' withdrawal and the disinterment under the same entry (l.4883-4885). New records claim matches. |
| B-M12 (Severinus records: Anonymus Valesianus) | RESOLVED | "de quo ita invenitur in libris vitae beati Severini monachi intra Pannoniam" (chronica-minora-liber-genealogus mommsen1892 l.40432); "praeter Eugippii vitam Severini editam a. 511. quam citat c. 45" (l.33502). |
| B-M13 (README: "logged in Open-Gaps") | PENDING | For the lead's Open-Gaps entry before merge. `Open-Gaps.md` has no Severinus entry yet, and the README is unchanged since R1. Not a finding. |
| B-H1 (batch 5 Henana: Life of George held) | PARTLY | Only that note changed: `git diff origin/main -- .../era3/batch5/records.json` is one line, the `note` of "A second witness to Babai's doctrinal charges". Checked against its cited files: Labourt's De Unione introduction (labourt1904 l.15764-15768), the quoted passage ending "en sorte qu'il n'y a pas deux Fils ou deux / Fils du Très-Haut" (l.15865-15866), the footnote "D'après le traité De Unione, Henana admettait ..." (l.15816-15820); Chabot "composée par saint Rabban Mar Babai" (chabot1902 l.42080) to "Henana le chaldéen et l'hérétique" (l.42242); Braun's charge "Er leugnet die Auferstehung der Leiber und (lehrt), daß / es eine Erlösung nur für die Seelen gebe" (braun1915 l.13395-13396); Hoffmann "leugnet die Auferstehung der Leiber" (hoffmann1880 l.5603). The Evagrius commentary is named by Braun ("einen Kommentar in die Centimen des Evagrius Pon- / ticus", OCR, l.13856-13857) and is not held: no Evagrius Ponticus file in `cic/texts/` names Babai. All of that is true. One word is not: "held whole in Oskar Braun's German". See R2-B-B1. |
| B-M14 (same note: "lent") | RESOLVED | The note now reads "made available to him". |

#### 2. New findings

**R2-B-B1 BLOCKING (`babai-the-great.card.json` `keyWorks` 2 `about`; `records.json` `babai-the-great` claim "Babai's Life of George, whole in German" and `absent_details` "A Syriac or English text of his own books"; `era3/batch5/records.json` `henana-of-adiabene` note "A second witness to Babai's doctrinal charges"; items 1 and 3; carried from R1's own B-B3 and B-H1 wording).**
- The card says "Oskar Braun translates the whole Life into German". The records say the Life is "held whole in Oskar Braun's German" and "whole in German". The batch 5 note says the same.
- Braun does not translate the whole Life. His own footnotes in the held file say what he leaves out:
  - On the introduction: "Von der sehr langen Einteilung gebe ich nur die wichtig- / sten Gedanken" (braun1915 l.12442-12443). The records already say this.
  - "Das folgende, sachlich belanglose Enkomion auf die Heilige / übergehe ich." (l.13161-13162)
  - "Ein langes Enlromion, worin die Beiden mit den die / Bundeslade aus dem Philisterlande ziehenden Kühen ... verglichen / werden, übergehe ich." (l.13319-13322)
  - "Die folgenden, sachlich inhaltslosen Ausführungen über- / gehe ich." (l.13806-13807)
- All three fall inside the Life, which runs from l.12419 to the end of the volume's acts (it is act XXI, the last).
- So the card tells participants a source is complete when its translator says it is not. That is a false claim about a source on a participant-facing card, and the batch 5 note, which this recheck was asked to confirm as true, still carries it.

Fixes:
- Card `keyWorks` 2 `about`: "a monk of Izla, once a Magian named Mihramgushnasp, put to death under Khosrau. Oskar Braun translates the Life into German, shortening its long introduction and leaving out a few passages he judged of no substance. J.-B. Chabot gives two passages in French, among them the charges against Henana of Adiabene; Scher says Paul Bedjan published the Syriac"
- Records claim: change the opening "Babai's Life of George, whole in German:" to "Babai's Life of George, in Braun's German (the introduction shortened and three passages passed over, braun1915 l.12442-12443, 13161-13162, 13319-13322, 13806-13807):". Leave the rest of the claim and its witness as they stand.
- Records `absent_details` "A Syriac or English text of his own books": replace "The Life of George is held whole in Oskar Braun's German (persian-martyr-acts bkv22 braun1915 l.12419 ff., the introduction abridged, l.12442-12443)" with "The Life of George is held in Oskar Braun's German (persian-martyr-acts bkv22 braun1915 l.12419 ff.), which gives only the main points of the long introduction (l.12442-12443) and passes over two encomia and one passage he calls empty of content (l.13161-13162, 13319-13322, 13806-13807)".
- Batch 5 note: replace "held whole in Oskar Braun's German (persian-martyr-acts bkv22 braun1915 l.12419 ff.; the charges at l.13355-13400)" with "held in Oskar Braun's German, which shortens the introduction and passes over three passages but keeps the charges (persian-martyr-acts bkv22 braun1915 l.12419 ff.; omissions noted at l.12442-12443, 13161-13162, 13319-13322, 13806-13807; the charges at l.13355-13400)". Nothing else in the note changes.

**R2-B-M1 MINOR (`babai-the-great.card.json` `uncertain` 1; `records.json` `babai-the-great` Guidi claim witness, contested claim "Who Babai bar Nisibnaye was", `absent_details` "The scan row's Book III lead"; items 1 and 6; the drafter's rewording of B-B4).**
- The card's new sentence reads: "An anonymous Syriac chronicle that Ignazio Guidi edited also praises him and tells of a quarrel between his followers and Babai the Little."
- The chronicle sets the quarrel between the two men themselves. Satan "iurgia multa magnasque contentiones / excitavit inter duas illas firmissimas religionis turres, duo Babhay, / nec conquievit aut desiit usque ad finem agonis, vitae asceticae, eorum" (guidi1903 l.2050-2052). The followers' ban comes after, as its result (l.2053-2055).
- Labourt, already on the card, reads it the same way: "disputes qui auraient eu lieu entre Babaï le Grand / et un autre Babaï dit le Petit" (labourt1904 l.13093-13094).
- The card's wording moves the quarrel off Babai and onto his monks. That softens what the source says about him.
- Separately, the cited ranges stop short. The quotation ending "cognominaverunt" runs to l.2064, past the cited 2058. The "Scripsit autem ... Mar. Babhay magnus (mator) libros / multos" quotation is at l.2069-2070, not 2067-2069.

Fixes:
- Card `uncertain` 1, the second sentence becomes two: "An anonymous Syriac chronicle that Ignazio Guidi edited also praises him. It tells of a quarrel between him and Babai the Little that lasted to the end of their lives."
- Records Guidi claim, witness: "Anonymous East Syrian chronicle, tr. Guidi (chronica-minora guidi1903 l.2032-2037, 2050-2064, 2069-2070); Labourt (labourt1904 l.13093-13096)". Add to the claim the Satan clause quoted above (l.2050-2052).
- Contested claim "Who Babai bar Nisibnaye was", first side: "(guidi1903 l.2036-2064)" for "(guidi1903 l.2036-2058)".
- `absent_details` "The scan row's Book III lead": "(guidi1903 l.2036-2064)" for "(guidi1903 l.2036-2058)".
- Records Mari/'Amr claim, witness: "mari gismondi1899 l.13517-13520" for "l.13517-13519" (the quotation ends "nobio Mar Abraliam" on l.13520).

**R2-B-M2 MINOR (`babai-the-great.card.json` `uncertain` 5 and 6, `legacy.traces` 4; item 4; long sentences and an attachment fault in new card text).**
- Three new card sentences run well past about 25 words:
  - `uncertain` 5: "The Arabic histories of Mari and 'Amr, in Enrico Gismondi's Latin, say the archdeacon Mar Aba and Mar Babai the Great governed the church while it had no head, and Mari counts seventeen years." (34 words)
  - `uncertain` 6: "The anonymous chronicle Ignazio Guidi edited says that monk was called Babai the Little, and that Babai the Great's followers let no one into their monastery who would not anathematize him." (31)
  - `uncertain` 6: "E. A. Wallis Budge instead puts a Babai bar Nesibhnaye, famous for his voice, under the catholicos Selibha-zekha, the time Thomas gives for Rabban Babai of Gebilta, the singer and founder of schools." (33)
- `legacy.traces` 4, "...join the bishops' debate before Khosrau, which Addai Scher dates to 612, but helped them with his pen", puts "which" right after "Khosrau", so a reader can take the king as what Scher dates. The "but" clause then has to reach back past it.

Fixes (wording otherwise unchanged; sources as in R1):
- `uncertain` 5: "...say the archdeacon Mar Aba and Mar Babai the Great governed the church while it had no head. Mari counts seventeen years. J.-B. Chabot follows them."
- `uncertain` 6: "...The anonymous chronicle Ignazio Guidi edited says that monk was called Babai the Little. Babai the Great's followers, it says, let no one into their monastery who would not anathematize him. E. A. Wallis Budge instead puts a Babai bar Nesibhnaye, famous for his voice, under the catholicos Selibha-zekha. That is the time Thomas gives for Rabban Babai of Gebilta, the singer and founder of schools."
- `legacy.traces` 4: "The Chronicle of Seert says he was too weak and old to join the bishops' debate before Khosrau, but helped them with his pen. Addai Scher dates the debate to 612."

**R2-B-M3 MINOR (`babai-the-great.card.json` `uncertain` 4; item 1; the B-M8 flag).**
- "a word before the dates is lost in the scan of his page" says the page itself is damaged. Nothing shows that. The word is unreadable in the OCR text the Library holds ("phone", labourt1904 l.17771). The page image is not held, so its state is unknown.
- Fix: "J. Labourt puts Dadisho's death between 615 and 620; a word before the dates cannot be read in the Library's text of his page."

I found no misquotation in the new or changed text, no new false absence, and no editor's year told as the ancient writer's beyond those above. Every common name in the changed text has its place or role at first mention: Sophronius, Photius of Constantinople, Tiberius II, Severinus of Noricum, Feletheus, Mari, 'Amr, Ignazio Guidi, Oskar Braun, Babai of Nisibis and Babai the Scribe. The changed brief lines read cleanly in context, with no new AI tells, beat lines or choppy runs.

#### 3. Verdicts

- John Moschus: **CLEAR** (all five R1 points resolved; no new finding).
- Babai the Great: **NOT CLEAR** (R2-B-B1 blocking; R2-B-M1 to R2-B-M3 minor). R1's five blocking points are resolved except for B-B3, which is carried by R2-B-B1.
- Severinus of Noricum: **CLEAR** (B-M9 to B-M12 resolved; B-M13 pending for the lead's Open-Gaps entry).
- Batch 5 `henana-of-adiabene` note: only that note changed, and it is true except for "held whole", which R2-B-B1 fixes. **NOT YET TRUE** until it is applied.

## R2 recheck, part C: era 3 batch 6

### Method

Scope: `constantius-of-lyon`, `faustus-of-riez`, `gennadius-of-marseilles` and `ruricius-of-limoges`, with their briefs, cards, audio scripts and `records.json` entries, in `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era3/batch6/`. I am a fresh Opus reviewer and did not draft or fix these files. This is a targeted recheck: round 2 of at most 3. I read part C of `R1_review.md` and `R1_changes.md`. I then read the changes as a word diff from `65412883` (the drafts R1 reviewed) to HEAD (`deb3cc1d`), with the four `records.json` entries diffed one by one. For each R1 finding I opened the cited lines in the vendored file myself. I then checked every new or changed sentence against its source. For each one I asked who speaks at that line: the ancient writer, an editor, a note or an apparatus. Quotations were checked with whitespace collapsed, and the OCR was read line by line. Untouched text was not re-reviewed. I edited no profile file, and made no git, model or web calls. Line numbers point to files under `cic/texts/` unless another path is given. Brief line numbers count blank lines.

Mechanical checks, all four:
- Each audio script equals its brief once `[calmly] ` and `[warmly] ` are removed (checked by script). Each has one `[calmly]` at the start and one `[warmly]`, at the start of the closing paragraph. Ruricius's brief now has six paragraphs, and the tag sits on the sixth.
- `grade_text` passes for all four. `briefLength` is "about 2 minutes" on all four. All four cards and `records.json` parse, and `records.json` holds the ten batch ids. Every `file` named in the four cards' sources exists.
- Narrator sentences past 25 words are lead-ins to quotations or modern renderings only. Constantius's new rendering runs 26 words by my count (R1 gave 25). That is within "about 25", so I do not raise it.

| Profile | Words | Est. @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Constantius of Lyon (recorder) | 323 | 2:00 | 8.0 | 66.1 | within 325 |
| Faustus of Riez | 324 | 2:00 | 8.1 | 63.1 | within 325 |
| Gennadius of Marseilles (recorder) | 325 | 2:00 | 8.2 | 64.0 | 325, at the cap |
| Ruricius of Limoges | 324 | 2:00 | 7.2 | 67.3 | within 325 |

### 1. R1 findings

| Finding | Status | Evidence |
|---|---|---|
| C-B1 (Constantius: Krusch's superseded view told as his view) | RESOLVED | Card `uncertain` 6 now gives both of Krusch's positions. In the introduction he says "E Constantii Vita S. Germani Autisiodorensis (I, 1) totum caput 29. M. S. Iuliani ad verbum exscripsit" (gregory-tours arndt-krusch1885 l.35826-35827). In the addenda (p.883, head at l.66231) he writes "De Vita S. Germani Autisiodorensis, quae Constantio vulgo attribuitur … Iam nullus dubito, quin Vitae scriptor e Gregorio ipso hauserit" (l.66256-66258). The p.460 l.23 that the addendum corrects is this line of the introduction. Levison: "Opus Constantii primigenium adhuc a solo Mombritio publici iuris factum est … Vita altera admodum interpolata" (l.659-661), and "Textum vulgatum interpolationibus refertum esse, monuerunt etiam B. Krusch, SS. R. Merov. I, 883" (l.703-704). The contested claim now has both sides. Two citation slips in the records (R2-C-M2). One phrase, and the shape of the fixed sentence, need a small fix (R2-C-M1). |
| C-M1 (Constantius: the rendering) | RESOLVED | "I call God, who knows what is hidden, to witness that I have left out many deeds of my lord Germanus that were known and proved." Levison l.4577-4579, "Deum testor conscium secretorum, me plura de domni mei Germani factis agnita et probata tacuisse." "All" is gone, and the passive is kept. The records epilogue claim carries the new rendering. |
| C-M2 (Constantius: "Bede, in England") | RESOLVED | "Bede copied large parts of it almost word for word into his History of the English." Levison l.587-589, "Beda Vitam Germani c. 12-16. et 25-27. magna ex parte ad verbum fere in Historia ecclesiastica gentis Anglorum I, 17-21. descripsit". |
| C-M3 (Constantius: length) | RESOLVED | 323 words. |
| C-M4 (Constantius: "later bishop of Clermont") | RESOLVED | "Sidonius Apollinaris, bishop of Clermont." Records claim on the see stands. Its new parenthesis is review history (R2-C-M7). |
| C-M5 (Constantius: orders said absent, then given) | RESOLVED in substance | `uncertain` 1: "No source used here gives his family, his birth or his death, and the sources disagree on his orders." `uncertain` 2 adds Rees and PL 48. Rees: "the life of Saint Germanus, written by Constantius, a priest of Lyons" (rees 1853 l.17717-17718). PL 48: "quod Constantius presbyter scriptum reliquit" (marius-mercator pl48 l.20173-20174). The PL 48 passage is from a dissertation, not a note (R2-C-M3). Neither book is in the card's sources (R2-C-M4). |
| C-M6 (Constantius `knownFor`) | RESOLVED | "…journeys to Britain, parts of which Bede later copied." Levison l.587-589. |
| C-M7 (log the truncated Levison file in Open-Gaps) | PENDING, not a finding | This falls to the lead's Open-Gaps entry for batch 6, written before merge. Neither `Build/Ministry/Features/Church-Family-Tree/Open-Gaps.md` nor the Library file carries it yet. The file still ends "Et ideo in scribendo succinctum^" and a newline (checked with `od`). |
| F-B1 (Faustus: Riochatus hid the books) | RESOLVED | Brief l.1: "Unrest among the peoples held him at Clermont, where he kept the books hidden. When he left, the bishop there, Sidonius Apollinaris, rode after him and read them." Barralis, first print: "apud oppidum nostrum cum moraretur, donec gentium concitatarum procella defremeret … reliqua vestra dona detexit, ut perurbane quae praestantiora portabat, operuerit … sed post duos, aut iis amplius menses … pernicibus equis insequutus abeuntem … quaesitum volumen invenio, produco, lectito, excerpo" (l.4755-4772). The second print agrees on every word used (l.5532-5548). "A bishop and monk" is "Antistes ac monachus" (l.4751; l.5528-5529). Williams: "This Riocatus is styled bishop and monk — antistes ac monachus" (gildas williams1899 l.9662). Records claim 1 carries all three witnesses (also meets F-M5). |
| F-M1 (Faustus: length) | RESOLVED | 324 words. The cuts read cleanly: "and its abbot from 433, by Engelbrecht's reckoning. Then he became bishop of Riez." "Lucidus later retracted the view…" "praised them". "he wrote to Ruricius of Limoges". |
| F-M2 (Faustus: Warfield introduced) | RESOLVED | "The Princeton scholar Benjamin Warfield calls Faustus the chief champion of what he names semi-Pelagianism. He says the Council of Orange put it down in 529." npnf105 l.519, "PROFESSOR IN THE THEOLOGICAL SEMINARY AT PRINCETON, N.J."; l.954, "its chief champion at a somewhat later day was Faustus of Rhegium (Riez)"; l.957-958, "the 3d of July, 529 … so far as a formal condemnation could reach, semi-Pelagianism was suppressed". |
| F-M3 (Faustus: "At last") | RESOLVED | "Then he became bishop of Riez." |
| F-M4 (Faustus card `place`) | RESOLVED | "Britain, by August Engelbrecht's reading of Avitus of Vienne, who calls him a Briton by birth". |
| F-M5 (Faustus records: second print, Williams) | RESOLVED | See F-B1. |
| F-M6 (Faustus: doubled hedge) | RESOLVED | "In old age Faustus was exiled by the Gothic king Euric, Engelbrecht thinks." |
| G-M1 (Gennadius: the Prosper sentence) | RESOLVED | "Gennadius thinks Prosper of Aquitaine wrote an unsigned book against works of John Cassian. He says Prosper "brands as injurious" works "which the church of God finds salutary"." npnf203 l.43666-43669, "I regard as his also an anonymous book against certain works of Cassianus, which the church of God finds salutary, but which he brands as injurious". Both fragments are verbatim. The reordering keeps the sense, and "He" can only be Gennadius. |
| G-M2 (Gennadius: Jackson introduced) | RESOLVED | "He and Blomfield Jackson, Theodoret's translator in the same volume, give 496 for his death." npnf203 l.682-684; Jackson l.3611-3612, "Gennadius, presbyter of Marseilles, who died in 496". Merge at l.5: "The line drew much comment on his bias, Richardson says, though it almost certainly does not go back to Gennadius." The "though" clause stays inside Richardson's attribution, and his note says "almost certainly does not represent the original form of the text" (l.42864-42865). |
| G-M3 (Gennadius card: note or prolegomena) | RESOLVED | "…given in a note by Richardson and in Blomfield Jackson's prolegomena to Theodoret…". Richardson's endnote "Died 496." is at l.43968. |
| G-M4 (Gennadius card: Acta Sanctorum in sources) | RESOLVED | Entry added. The file exists, and l.180635-180636 read "Gennadius Presbyter Massiliensis, qui sub finem dicti seculi quinti floruit". |
| G-M5 (Gennadius records: Scholarios) | RESOLVED | Namesake claim added. PG 160 header l.1, "Gennadii, Constantinopolitani patriarchae, qui et Georgius Scholarius, Opera omnia". |
| R-B1 (Ruricius: the food metaphor) | RESOLVED | "He asks that Faustus's letters be harsher food, fit for a sinner's sickness, in place of the sweet dishes sent so far." Engelbrecht l.20070-20074, "quoties dignati fueritis ariditatem terrae meae eloquentiae vestrae imbre perfundere, non mihi, sicut nunc fecistis … delicatos et dulces cibos, sed austeriores et aegritudini meae congruos suggeratis"; l.20078-20079, "ne vulneribus meis gratior sit foventis dextera quam secantis". |
| R-M1 (Ruricius: 506 is in the acts) | RESOLVED in brief and card | Brief: "…at Agde under Caesarius of Arles, in 506". Card: "Caesarius's letter names Agde, whose acts date it to 506." Bruns, note 3: "Conc. Agath. viginti quinque episcoporum habitum era 644 [643 JE.], Anno vicesimo secundo Alarici regis sub die tertio Idus Septembris … Messala v. c. consulem habet Corbej." (bruns 1839 l.10498-10501). Caesarius's letter: "Agate" (l.24686). The PL 67 prolegomenon and Basnage are both reported fairly (PL 67 l.96512-96553). In the records, the era figure the claim quotes does not fit 506 (R2-C-M6). |
| R-M2 (Ruricius: Caesarius's pardon) | RESOLVED in substance | "Yet he held nothing against him." Engelbrecht l.24713-24716, "nihil pietati vestrae vel potuimus vel debuimus inputare"; PL 67 l.96517-96518, "partim objurgat, partim excusat Ruricium". "Ruricius answered" now opens a new paragraph. The pronoun is unclear when heard aloud (R2-C-M5). |
| R-M3 (Ruricius: Krusch unintroduced) | RESOLVED | "Engelbrecht thinks he died not long after 507…". Krusch stays on the card (`dates`, `uncertain` 3). |
| R-M4 (Ruricius: length, choppy pair) | RESOLVED | "Caesarius himself, he wrote, had seen him worn out at Bordeaux, and in winter, when he was usually stronger." Engelbrecht l.23186-23188, "ipsi etenim recolere potestis, quam fessum me Burdigala videritis et hoc hieme, quando esse soleo fortior solito". "Each Ruricius founded" reads cleanly. 324 words. |
| R-M5 (Ruricius: the later signer) | RESOLVED | Card `uncertain` 5. Leo's index: "alter nepos illius interfuit concilio Arverno I. a. 535, Aurelianensi IV. a. 541, V. a. 549 per Bantaredum archidiaconum subscripsit" (venantius-fortunatus leo-krusch1881 l.53125-53130, "alter nepos" at l.53128). Maassen l.6019 (under "CONCILIUM ARVERNENSE A. 535", l.6007), l.8139 (under "AURELIANENSE A. 541", l.8109), l.9442 (under "AURELIANENSE A. 549", l.9332). `absent_details` is corrected. Its new aside on the first search is review history (R2-C-M7). |
| R-M6 (Ruricius: 485) | RESOLVED | Card `uncertain` 1. Engelbrecht l.348-350, "Quodsi Euricus in causa fuit, ut Faustus a. 477 in exsilium pelleretur, illo demum mortuo i. e. anno 485 in patriam hunc rediisse veri simile est"; l.954-959, "Epistulae quarta et quinta post Fausti exsilium scriptae sunt, unde Faustus a. 485 rediit, quo eodem anno Ruricius episcopus factus est". |
| R-M7 (Ruricius: "Ruricius the elder") | RESOLVED | `otherNames` now holds only "Ruricius Lemovicensis". |

Totals: all 3 R1 blocking findings resolved. Of the 25 R1 minors, 24 are resolved or resolved in substance, and C-M7 is pending the lead's Open-Gaps entry.

### 2. New findings

No new blocking findings. Seven minor.

**R2-C-M1 MINOR (Constantius card `uncertain` 6; one phrase not true to Levison, a colon-reveal, a run-on sentence).**
Evidence: the fixed item says "In the additions at the end of the same volume he holds the reverse: the writer of that Life…" and closes "Wilhelm Levison holds that Gregory did not know Constantius's Life, since Gregory has Germanus die at Rome, where the Life has Ravenna, and he says the text then in print was a much-interpolated second Life."
- "The text then in print" is not what Levison says. He says the genuine text *was* in print, in Mombritius's edition, though neglected: "Opus Constantii primigenium adhuc a solo Mombritio publici iuris factum est, cuius textus imperfectus omnino neglegebatur postquam Vita altera admodum interpolata … apud Surium Bollandianosque lucem aspexit" (levison1920 l.659-661). His word for the interpolated text is "vulgatum", the common text (l.703).
- The Duru edition Krusch cites is that interpolated text. Duru "editionem Boschianam iteravit" (l.1620-1621), and Levison cites the second Life in Duru (l.599, "Vitae Germani secundae … Duru l. l. I, 57-66"). Saying so makes the link a reader needs.
- "He holds the reverse:" is a colon-reveal (Who_Profile_Pattern checklist item 4). The last sentence runs 41 words.
Fix, replace the item with: "Whether Gregory of Tours knew the Life. In his introduction to Gregory's Miracles, Bruno Krusch says Gregory copied a whole chapter of his Miracles of Julian almost word for word from a Life of Germanus, which he cites in Duru's edition. In the additions at the end of the same volume he reverses this, and holds that the writer of that Life, which he calls the Life commonly given to Constantius, drew on Gregory. Wilhelm Levison holds that Gregory did not know Constantius's Life, since Gregory has Germanus die at Rome, where the Life has Ravenna. Levison also says the text in common use was a much-interpolated second Life, and Duru's edition reprints that second Life." Records, contested claim side 2: add "Duru reprinted the Bollandist text of the second Life (levison1920 l.599, 1620-1621)".

**R2-C-M2 MINOR (Constantius records, contested claim "Whether Gregory of Tours knew the Life of Germanus", side 1; citation lines).**
Evidence: side 1 cites "note l.44305-44306, citing Duru's text" and "(l.66256-66257, p.883…)". At l.44305-44306 the file has "e) s. in te 2." and a blank line. Krusch's note 2 is at l.44307-44310: "Hoc caput Gregorius fere ad verbum cum Vita S. Germani Autisiod. a Constantio composita convenit; lib. I, c. 7, Duru…". "Iam nullus dubito…" is at l.66258, not l.66257, and the page head "ADDENDA ET EMENDANDA. 883" is at l.66231. R1 and R1_changes gave the same numbers, so the slip was copied forward.
Fix: "note l.44307-44310, citing Duru's text" and "(l.66256-66258, p.883, page head l.66231; OCR 'jiuUus', 'nttribuitur')".

**R2-C-M3 MINOR (Constantius card `uncertain` 2 and the new records claim; witness form).**
Evidence: "an unsigned note in Migne's Marius Mercator". The passage "quod Constantius presbyter scriptum reliquit (In Vita S. Germani Altissiodorensis)" (pl48 l.20173-20174) is not a note. It is the running text of Dissertation I, "De primis auctoribus et praecipuis defensoribus haeresis Pelagianae", one of the "Dissertationes septem" in the volume's second appendix (l.18388-18399, 18470-18472). No signature is in the held lines, so "unsigned" stands.
Fix, card: "W. J. Rees and an unsigned dissertation in Migne's Marius Mercator also call him a priest." Records claim: "…an unsigned dissertation (Dissertation I) in Migne's Marius Mercator: 'Constantius presbyter'", with witness "PL 48, appendix 2, Dissertation I (marius-mercator_opera-omnia-lat_migne-pl48 l.20173-20174; heading l.18470-18472)".

**R2-C-M4 MINOR (Constantius card `sources.about`; checklist item 12, the same fault as R1 G-M4).**
Evidence: `uncertain` 2 now cites Rees and PL 48, but `sources.about` lists only Levison's prolegomena, Isidore and Krusch's introduction. Both files exist.
Fix, add to `sources.about`:
`{"title": "Lives of the Cambro-British Saints, notes", "author": "W. J. Rees", "date": "1853", "language": "English", "file": "cic/texts/rees_lives-of-the-cambro-british-saints-lat-eng_1853.txt"}` and
`{"title": "Works of Marius Mercator, appendix 2, Dissertation I (Patrologia Latina 48)", "author": "Unsigned", "date": null, "language": "Latin", "file": "cic/texts/marius-mercator_opera-omnia-lat_migne-pl48.txt"}`.

**R2-C-M5 MINOR (Ruricius brief l.1 and audio; clarity aloud, checklist item 4).**
Evidence: "Ruricius should, he wrote, have sent someone to sign in his place. Yet he held nothing against him." Heard aloud, the paragraph's last named man is Ruricius. So "he held nothing against him" can be taken as Ruricius holding nothing against Caesarius, which reverses the pardon R-M2 put in.
Fix: "Yet Caesarius held nothing against him." Audio script to match. Scored: 324 words, FK 7.3, Flesch 66.8.

**R2-C-M6 MINOR (Ruricius records, claim "Agde 506"; a quoted date that does not fit the claim's year).**
Evidence: the claim, now tagged Documented, quotes "habitum era 644" as the acts' dating of the 506 council (bruns 1839 l.10499). Spanish era 644 is AD 606, and Bruns's variant 643 is 605. What gives 506 is Alaric's twenty-second year and the consul Messala (l.10499-10500). Engelbrecht turns that into 506: "anno enim 506 (sub d. III Idus Septembris Messala u. c. consule …)" (engelbrecht1891 l.2933-2934). The brief and card are sound, but a checker who reads the records will meet a year that contradicts the claim. Bruns's second print of the heading gives the variant as "[543. JE.]" (l.13760), so "644" is probably a slip for 544, but the held text does not settle this.
Fix, add to the claim: "(the era figure as printed, 644, does not fit 506, and Bruns gives the variants 643 and 543; the year rests on the twenty-second year of Alaric and the consul Messala, which Engelbrecht reckons as 506, l.2933-2934)".

**R2-C-M7 MINOR (records, part C ids; review history inside claim text).**
Evidence: five claims and one note now carry the history of round 1 rather than what the source says:
- Constantius: "(the brief now says 'bishop of Clermont' without 'later', R1 C-M4)", and "(R1 C-M1: 'all' dropped, passive 'agnita et probata' kept)".
- Faustus: "(R1 F-B1)".
- Ruricius: "(brief: 'Yet he held nothing against him', R1 R-M2)", "(R1 R-B1; brief now 'He asks that Faustus's letters be harsher food, fit for a sinner's sickness')", and in `absent_details` 1, "(the first search missed the OCR form 'Huricii' there)".

None of the batch 5 records carries such tags. Where each change came from is already in `R1_changes.md`.
Fix: delete the six parentheses or asides. Keep the brief's wording only where a claim needs it to show what the brief renders, as the epilogue claim does: "the brief gives this in Opus's modern English: '…'".

### 3. Verdicts

- Constantius of Lyon: CLEAR on blocking points. Four minor findings to apply (R2-C-M1 to M4), plus the Constantius parts of R2-C-M7. C-M7 is pending the lead's Open-Gaps entry.
- Faustus of Riez: CLEAR. Only the Faustus part of R2-C-M7, a records tidy-up.
- Gennadius of Marseilles: CLEAR.
- Ruricius of Limoges: CLEAR on blocking points. R2-C-M5 (one word in the brief and audio), R2-C-M6 and the Ruricius parts of R2-C-M7 to apply.

None of the new findings is blocking. Each is worded so it can be applied without another review round. A round 3 check, if one is held, needs to look only at the changed strings.
