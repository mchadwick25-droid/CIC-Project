# R2 recheck, part A: era 3 batch 6

Scope: Columbanus, Isidore of Seville and John of Biclaro, with their cards, audio scripts and `records.json` entries. Round 2 of at most 3, a targeted recheck.

## Method

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

## 1. R1 findings

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

## 2. New findings

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

## 3. Verdicts

- `columbanus`: CLEAR once R2-A-M1 is applied (minor only; R2-A-M4 batch-wide).
- `isidore-of-seville`: CLEAR once R2-A-M2 and R2-A-M3 are applied (minor only; R2-A-M4 batch-wide).
- `john-of-biclaro`: CLEAR (R2-A-M4 batch-wide only).

No blocking finding remains on part A. The fixes touch cards and records only, so brief lengths and readability scores do not change.
