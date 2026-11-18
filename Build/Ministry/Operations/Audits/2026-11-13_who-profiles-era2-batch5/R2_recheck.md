# R2 recheck: ten Who profiles, era 2 batch 5

Scope: only what changed, checked against `R1_review.md` and `R1_changes.md`. Text that did not change was not reviewed again. The changes were read as a word diff from `6bd35d2a` (the drafts as R1 saw them) to `a887f3fa`, limited to `Build/Ministry/Features/Church-Family-Tree/Who-Profiles/era2/batch5/`. Every new or changed sentence, quotation, identifier and records.json entry was opened at its line in the vendored file, with XML tags stripped and whitespace collapsed, to confirm who is speaking there: the ancient writer, a document he quotes, the translator, an editor's bracket or a note. The French of Langlois's volume (Koriun, Lazar of Pharp, Moses of Khoren, Langlois's own introduction and notes) was read in the OCR as held. I did not edit the drafts, and I made no paid calls, model-API calls or web requests. Line numbers point to files under `cic/texts/` unless another path is given.

Mechanical checks, all ten:
- Each audio script equals its brief once the opening `[calmly] ` and the single `[warmly] ` are removed (checked by script). Each starts with `[calmly]` and has one `[warmly]`.
- `grade_text` passes for all ten (FK at most 10, Flesch at least 60). Eusebius (60.1), Alexander (60.7) and Ossius (60.7) sit nearest the Flesch floor.
- Brief sentences: no new or changed narrator sentence runs past 25 words. The longest new ones are Cyril l.1 ("Then Nestorius's reply was read and judged…", 23 words, most of the tail quoted) and Mesrop l.5 (the Lazar sentence, 21).
- `briefLength` matches on all ten. All ten cards and `records.json` parse as JSON.

| Profile | Words | Est. length @162 | FK | Flesch | Cap |
|---|---|---|---|---|---|
| Socrates of Constantinople | 326 | 2:01 | 6.9 | 66.8 | 325, unchanged |
| Mesrop Mashtots (MAJOR) | 406 | 2:30 | 7.2 | 68.3 | 405, within "about" (as R1 accepted) |
| Cyril of Alexandria (MAJOR) | 404 | 2:30 | 7.2 | 64.3 | 405, within |
| Sozomen | 321 | 1:59 | 7.4 | 64.2 | 325, within |
| Theodoret of Cyrrhus (MAJOR) | 405 | 2:30 | 8.0 | 61.5 | 405, at the cap |
| Leo of Rome (MAJOR) | 404 | 2:30 | 6.3 | 72.6 | 405, within |
| Koriun | 328 | 2:01 | 6.2 | 74.8 | 325, brief unchanged |
| Alexander of Alexandria | 326 | 2:01 | 7.7 | 60.7 | 325, within "about" |
| Eusebius of Nicomedia (MAJOR) | 395 | 2:26 | 7.6 | 60.1 | 405, within |
| Ossius of Cordoba | 329 | 2:02 | 8.1 | 60.7 | 325, within "about" |

## 1. The 1 R1 blocking finding

| Finding | Status | Evidence |
|---|---|---|
| Ossius B1 (absence claim on his death that Percival's volume contradicts) | RESOLVED | Card `dates` now reads "No ancient source used here gives the year of his death. Henry Percival reports Cave's view that his episcopate ended in 361, and Hefele's that he was dead before the Synod of Gangra". Card `uncertain` #4 adds Pagi's 358. This matches Percival's introduction to Gangra (npnf214 l.8435–8448): "Hefele denies this and says: 'At the time of the Synod of Gangra Hosius was without doubt dead.' … Cave … is of opinion that Hosius's episcopate covered seventy years ending with 361, and (resting on the same opinion) Pagi thinks Hosius may have attended the Synod in 358 on his way back to Spain". The passage is Percival's own voice ("as I have said, Mr. Ffoulkes agrees"), so "Percival reports" is right. The narrowed absence, "no ancient source", holds: no line in Socrates, Sozomen or Athanasius as held gives a death year (searched). The new records `contested_claim` "When he died" quotes Hefele exactly and gives Cave and Pagi as Percival reports them. |

## 2. R1 minor findings

**Mesrop Mashtots**
- M1: RESOLVED, in the drafter's wording, which holds. Lazar of Pharp has Daniel as the man "chez lequel se trouvaient les caractères arméniens", and the study of them "leur démontra qu'elles étaient insuffisantes pour épeler exactement les syllabes de la langue arménienne" (Langlois l.36302–36318). "Could not spell the language exactly" is closer to this than R1's "too few", and the drafter's reason holds. "Langlois, following Luc Indjidji, holds that Mesrop took up work begun long before" matches Langlois's own voice: "Mesrob … ne fut pas le premier … Le savant Luc Indjidji a fait observer … que Mesrob ne fit que reprendre un travail qui avait préoccupé depuis de longues années déjà les lettrés de l'Arménie" (l.3053–3061). The records side for Lazar matches. The trims: "the Armenian district" to "the district" leaves Koghten placed by the next sentence ("Armenian had no letters"). "Then left the court to become a monk" to "then left the court as a monk" compresses Koriun, who has him give up his posts and then become a monk ("se déchargea de tous ses emplois … il se fit moine", l.3452–3461); it changes no claim. The Georgians and Aghouank stay on the card twice, as R1 said.
- M2: RESOLVED. "the first hasty translations were corrected against them; the French supplies Sahak's name in brackets" matches "Ensuite, [Sahag] reprit en sous-œuvre les livres qui avaient été traduits d'abord à la hâte … corrigea les premières versions" (l.3870–3874).
- M3: RESOLVED. "whom Koriun's text calls a man of Samos" in `knownFor`; "Joseph of Baghin" in `legacy.traces` #1, from the Life's note "Joseph de Bagldn" (OCR, l.3679) and the note to Moses, "Joseph était de Baghin" (l.24645).

**Cyril of Alexandria**
- M1: RESOLVED. The acts read Nestorius's letter next, Cyril asks whether it agrees with Nicaea, "[The bishops, then as before, individually express their opinion …]", and only then "All the bishops cried out together … we all anathematize Nestorius as a heretic" (npnf214 l.15829–15845). The brief and the records claim now follow that order. The trim of the peace sentence brings in a loose pronoun (N1).
- M2: RESOLVED. The thesis opener is gone.
- M3: RESOLVED, in the drafter's wording, which holds. Percival: "I would suggest, however, that for those who defend John of Antioch, and criticise the action of St. Cyril, it is the height of inconsistency to deny that the Council adopted the Anathemas", followed by "Bishop Hefele was at first of opinion that the letter was merely read … but he afterwards saw grounds to change his mind" (l.15899–15912). The drafter is right that Percival does not say in his own sentence that the council most likely adopted them; the card now reports what he argues and what he reports, and adds the bracket. "The council's critics" for "those who defend John of Antioch, and criticise the action of St. Cyril" is a fair short form. The records `contested_claim` quotes "those who defend John of Antioch" exactly.
- M4: RESOLVED. "Aëtius, archdeacon of Constantinople" (npnf214 l.19401, 20019).
- The cut "He died in 444" leaves the year on the card `dates` as Blomfield Jackson's, unchanged.

**Sozomen**
- M1: RESOLVED in brief, card and records. The note reads "He probably means that of Alaphion" (npnf202 l.36388), and the card quotes it exactly.

**Theodoret of Cyrrhus**
- M1: RESOLVED. "Nestorius, the deposed bishop of Constantinople" at the first mention, and "of Constantinople" on the card. Nestorius's deposition at Ephesus in 431 is in the held acts (npnf214, as the Cyril profile uses them). The trims ("in his absence"; "Leo restored him, and Chalcedon let him in") change no claim; the acts give the reason in their own words on the card ("because the holy Archbishop Leo had restored the bishopric to him").
- M2: RESOLVED. "Blomfield Jackson: the two 'were substantially at one'" is Jackson's "Yet he and Theodoret were substantially at one" (npnf203 l.2756). Bright, as Jackson quotes him: "uses a good deal of language which is prima facie Nestorian … but he and Cyril were essentially nearer to each other in belief than at the time they would have admitted" (l.2766–2771). Exact.

**Leo of Rome**
- M1: RESOLVED. "In 440, by Feltoe's date, Xystus, bishop of Rome, died. Prosper says Rome's church waited more than forty days for its deacon Leo." Feltoe: "Next year (440) was a momentous one … In his absence Sixtus died" (npnf212 l.460–473). Prosper's entry stands under the consuls "Valentiniano Aug. V et Anatolio", with "a. 440" in Mommsen's margin, and gives "XL amplius diebus" (l.54624–54627). The brief now agrees with its card.

**Koriun**
- M1: RESOLVED, in the drafter's form, which holds. The held scan reads "Mais, poussés par TeuTie, leurs compagnons et leurs condisciples, appelés Léon et Gorioun, se rendirent spontanément à Byzance" (Langlois l.24625–24661, across the page break). Quoting "l'envie" as if verbatim would put a reading in the scan's mouth, so the card's "the held scan reads 'TeuTie', most likely 'l'envie'" is the honest form. "Of those already there" is a fair reading of the context: Joseph and Eznik had gone ahead to Byzantium (l.24609–24622), and Leon and Koriun are "leurs compagnons". Records follow.
- M2: RESOLVED. "Sahak, patriarch of the Armenians"; "Victor Langlois"; "Ghevont, the Leon of the Life by a note in the edition" ("Léon ou Ghévont, prêtre de Yanant", l.3887); "Agathangelos's History of Tiridates". Langlois has "l'Histoire du secrétaire de Tiridate" and then "l'ouvrage d'Agathange" (l.2835–2849). "History of Tiridates" is a gloss, not a title the source gives, but it misleads no one about which work is meant.

**Alexander of Alexandria**
- M1: RESOLVED. "The historians, who all held to Nicaea, tell three stories". No trim was needed at 326 words.
- M2: PARTLY RESOLVED. Arius's letter to Eusebius of Nicomedia, in Theodoret I.4 (npnf203 l.6002–6004), is now named. The new sentence closes the list, though: "From Arius's side, the held sources are Arius's own letter to Eusebius of Nicomedia, kept by Theodoret, and Philostorgius". Other held sources from Arius's side contradict it (N2). R1's own fix wording carried the fault, so this is not the drafter's error.
- M3: RESOLVED. "Kölling, author of a German history of the Arian heresy" (npnf204 l.1352–1354: "Kölling's Geschichte der Arianischen Häresie (1st vol., 1874, 2nd, 1883)").

**Eusebius of Nicomedia**
- M1: RESOLVED. "Sozomen, a church historian of the next century". Sozomen wrote after 443 (per R1's Sozomen checks); Eusebius died about 341.
- M2: RESOLVED. "Socrates of Constantinople", "Theodoret of Cyrrhus", "Paul, bishop of Constantinople" (npnf202 l.5879: Constantius "ejects Paul … and sending for Eusebius of Nicomedia, invests him with the bishopric of Constantinople").
- The cut of Alexander's "pay no attention…" leaves the next sentence clear ("One of his own letters" still points to Eusebius). The records claim was cut to "Took up Arius's cause when Alexander put him out", and its witnesses still stand.

**Ossius of Cordoba**
- M1: RESOLVED. "Socrates says he was beaten until he signed a creed there; Sozomen says so too, 'as it is reported'" (npnf202 l.32899–32901: "he sunk, as it is reported, beneath the blows").
- M2: RESOLVED on the card. "In his Defence of his Flight he speaks of 'repeated stripes above measure', after which 'he yielded to them for a time'" (npnf204 l.36613–36616). The second quotation runs across the editor's bracket "[Apol. Ar. 89, Hist. Ar. 45, 357 a.d.]", which is not Athanasius's text, so leaving it out is right. The brief not taken: HOLDS, as R1 allowed. The new records claim matches the card. Its change to `absent_details` drops a backing (N3).
- M3: RESOLVED. "At the council of Sardica, about 343 by Percival's date" (npnf214 l.930, "Sardica (343 circa)", Percival's general introduction); "says Sozomen, a church historian of the next century". The cut of Socrates's "greatly loved this man" is matched in records.

**README**
- README-M1: RESOLVED. "by Archibald Robertson's notes to Athanasius's account of his detention at Sirmium". The year is now Robertson's, and "exile" is gone. Strictly, the 357 sits in Robertson's introduction to the Defence of his Flight and in his bracket inside the Defence's passage on the lapse (npnf204 l.36364–36365, 36615), which points to History of the Arians 45. The README is internal and names the right witness for the year, so this is an observation, not a finding.

## 3. Not taken or changed wording: judgments

| Item | Drafter's reason | Judgment |
|---|---|---|
| Mesrop M1, "too few" | Lazar says "insuffisantes pour épeler exactement les syllabes" | HOLDS. See §2. |
| Cyril M3, "He thinks the council most likely adopted them" | Percival argues the point and reports Hefele; he does not state it as his own conclusion | HOLDS. See §2. |
| Koriun M1, quoting "poussés par l'envie" | The held scan reads "TeuTie" | HOLDS. Quoting an emended reading as verbatim would be a quotation the vendored file does not contain. |
| Ossius M2, brief left as it is | Each brief sentence is true of its witness | HOLDS, as R1 allowed. |
| Mesrop 406 words; Alexander 326, Koriun 328, Ossius 329 | Within "about" | HOLDS, as R1 and batch 4 accepted. |

## 4. New or changed quotations, checked word for word

All exact, with their speakers confirmed: "insuffisantes pour épeler exactement les syllabes" (Lazar of Pharp, told, not quoted, in the brief; records l.36299–36318). "He probably means that of Alaphion" (Hartranft's note, npnf202 l.36388). "the Acts do not recite that this letter of Cyril's was read, nor do they state that the Anathemas were received" (Percival, npnf214 l.15897–15899, unchanged words). "those who defend John of Antioch" and "merely read" (records, Percival, l.15899–15909). "were substantially at one" (Jackson, npnf203 l.2756). "uses a good deal of language which is prima facie Nestorian" and "were essentially nearer to each other in belief than at the time they would have admitted" (Bright as Jackson quotes him, l.2766–2771). "repeated stripes above measure" and "he yielded to them for a time" (Athanasius, Defence of his Flight 5, npnf204 l.36613–36616, the editor's bracket omitted). "as it is reported" (Sozomen IV.6, npnf202 l.32901). "At the time of the Synod of Gangra Hosius was without doubt dead." (Hefele as Percival quotes him, npnf214 l.8442, across a page break). "TeuTie" (the scan, Langlois l.24626). No quotation fails. No witness swap, no modern date told as resting on an ancient text, and no identification told as settled against a doubting source was found in the changed text.

## 5. New findings in changed text

### New blocking

None.

### New minor

- **N1 (Cyril, brief l.9).** "Nestorius, Cyril's enemy, later charged him with bribery, 'the gold of iniquity.' In 433 he made peace with John. His letter begins, 'Let the heavens rejoice…'" The trim from "In 433 Cyril and John made peace" leaves "he" and "His" with Nestorius as the nearest subject. Read aloud, it says Nestorius made peace with John and wrote the letter. Cyril wrote it (npnf214 l.19428). Fix: "In 433 Cyril made peace with John." (Same word count, 404.)
- **N2 (Alexander, card `uncertain` #1).** "From Arius's side, the held sources are Arius's own letter to Eusebius of Nicomedia, kept by Theodoret, and Philostorgius, who survives only in a hostile summary by Photius." The list is closed, and held files contradict it. Athanasius's De Synodis 16 keeps the letter of Arius and his fellow presbyters and deacons to Alexander himself: "And what they wrote by letter to the blessed Alexander, the Bishop, runs as follows:— To Our Blessed Pope and Bishop, Alexander, the Presbyters and Deacons send health in the Lord" (npnf204 l.57093–57099), after extracts of Arius's Thalia (De Synodis 15). Socrates I.26 keeps Arius and Euzoius's declaration to Constantine (npnf202 l.4859). This is the R1 M2 pattern again, carried by R1's own fix wording. Fix: "From Arius's side, the held sources include Arius's own letter to Eusebius of Nicomedia, kept by Theodoret, and a letter from Arius and his fellow clergy to Alexander himself, kept by Athanasius. Philostorgius, also on that side, survives only in a hostile summary by Photius."
- **N3 (Ossius, `records.json` `absent_details`).** The change to the first absent detail drops its note "Athanasius speaks of conspiracies against unnamed kinsfolk (npnf204 l.36614-36615)". Card `uncertain` #5, unchanged, still says "Athanasius also speaks of conspiracies against his kinsfolk. No source used here names them." That honest limit now has no record behind it. Fix: add an absent detail, "Names of his kinsfolk", with the note "Athanasius speaks of conspiracies against his kinsfolk (npnf204 l.36614-36615); no source used here names them."

Observations, not findings: Mesrop's records claim "Presented the letters to Sahak and King Vramshapuh, who rejoiced as if they were the divine Tables…" (`records.json` l.113) now stands for a sentence cut from the brief. It is not on the card either. It is true and sourced. In Eusebius and Ossius, though, the drafter cut the records claim to match, so the drafter may want to do the same here for consistency. The other new or changed records.json entries match their briefs and cards.

## Summary

| Profile | Words | Time @162 | FK | Flesch | R1 findings resolved | New blocking | New minor |
|---|---|---|---|---|---|---|---|
| Socrates of Constantinople | 326 | 2:01 | 6.9 | 66.8 | – (0) | 0 | 0 |
| Mesrop Mashtots (MAJOR) | 406 | 2:30 | 7.2 | 68.3 | 3 of 3 | 0 | 0 |
| Cyril of Alexandria (MAJOR) | 404 | 2:30 | 7.2 | 64.3 | 4 of 4 | 0 | 1 (N1) |
| Sozomen | 321 | 1:59 | 7.4 | 64.2 | 1 of 1 | 0 | 0 |
| Theodoret of Cyrrhus (MAJOR) | 405 | 2:30 | 8.0 | 61.5 | 2 of 2 | 0 | 0 |
| Leo of Rome (MAJOR) | 404 | 2:30 | 6.3 | 72.6 | 1 of 1 | 0 | 0 |
| Koriun | 328 | 2:01 | 6.2 | 74.8 | 2 of 2 | 0 | 0 |
| Alexander of Alexandria | 326 | 2:01 | 7.7 | 60.7 | 2 of 3, M2 partly | 0 | 1 (N2) |
| Eusebius of Nicomedia (MAJOR) | 395 | 2:26 | 7.6 | 60.1 | 2 of 2 | 0 | 0 |
| Ossius of Cordoba | 329 | 2:02 | 8.1 | 60.7 | B1 and 3 of 3 | 0 | 1 (N3) |
| README | | | | | 1 of 1 | 0 | 0 |
| **Total** | | | | | **B1 resolved; 21 of 22 minor resolved, 1 partly** | **0** | **3 (N1 to N3)** |

The R1 blocking finding is resolved, and 21 of the 22 R1 minor findings are resolved or taken in another form that holds. Alexander M2 is partly resolved: the overlooked letter is now named, but the new list of Arius-side sources is closed and held files contradict it (N2). Every changed-wording and not-taken reason holds against its source. No witness swap, no new wrong attribution, no modern date told as ancient and no dropped hedge was found in the changed text. The changes brought in no new blocking finding and three minor ones: a pronoun left loose by a trim (N1), the closed list (N2), and a records honest limit dropped (N3). Each fix is a one-sentence edit that needs no round 3 review.
