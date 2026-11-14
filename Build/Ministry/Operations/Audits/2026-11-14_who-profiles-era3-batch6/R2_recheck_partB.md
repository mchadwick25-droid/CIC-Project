## R2 recheck, part B: John Moschus, Babai the Great, Severinus of Noricum (era 3 batch 6)

### Method

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

### 1. R1 findings

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

### 2. New findings

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

### 3. Verdicts

- John Moschus: **CLEAR** (all five R1 points resolved; no new finding).
- Babai the Great: **NOT CLEAR** (R2-B-B1 blocking; R2-B-M1 to R2-B-M3 minor). R1's five blocking points are resolved except for B-B3, which is carried by R2-B-B1.
- Severinus of Noricum: **CLEAR** (B-M9 to B-M12 resolved; B-M13 pending for the lead's Open-Gaps entry).
- Batch 5 `henana-of-adiabene` note: only that note changed, and it is true except for "held whole", which R2-B-B1 fixes. **NOT YET TRUE** until it is applied.
