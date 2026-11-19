# R2 recheck: era 3 batch 8

Round 2 ran in two parts, each by a fresh Opus agent that had not seen the drafting or round 1. The parts follow, unchanged.

## R2 recheck, part A: John Climacus, Liberatus of Carthage, Dionysius Exiguus, Marius of Avenches (era 3 Who batch 8)

Reviewer: independent Opus, first sight of these files. I edited no profile file and made no git writes, web, paid or model calls. I used local scripts only. Inputs: R1_review.md parts A and B, R1_changes.md parts A and B, the current batch 8 files, and `records.json`. The changed text was found with `git diff --word-diff` against the first-draft commits (2140b3d5 for the briefs and for the Climacus, Dionysius and Marius cards; 21006995 for the Liberatus card), and card fields were diffed field by field. I opened every cited line again in its vendored file. Every quote and paraphrase in changed text was checked against the file, with OCR noise folded. Scored copies of the suggested brief fixes are in `/tmp/claude-0/-home-user-CIC-Project/9440743b-c163-5ede-bda7-008353992a86/scratchpad/r2A/`.

**Mechanical checks (all four).** I checked by script that each audio file equals its brief plus `[calmly] ` at the start and `[warmly] ` at the start of the last paragraph. All four match, with one tag of each kind. Each card follows Mark's order (name, otherNames, knownFor, dates, place, tradition, role, briefLength, keyWorks, legacy, uncertain, sources), with no empty or null fields and at most three keyWorks. Every `sources` file exists. Each `records.json` entry is identical to its scratchpad record. No brief sentence runs past 24 words.

| Profile | Words | Time @162 | FK | Flesch |
|---|---|---|---|---|
| john-climacus (major, cap about 405) | 403 | 2:29 | 6.5 | 76.0 |
| liberatus-of-carthage | 323 | 2:00 | 8.4 | 61.0 |
| dionysius-exiguus (major, cap about 405) | 403 | 2:29 | 7.9 | 66.0 |
| marius-of-avenches | 328 | 2:01 | 7.4 | 67.0 |

---

### John Climacus

| R1 finding | Verdict | Evidence |
|---|---|---|
| A-B1 (ten months told as settled) | RESOLVED | P6 now tells the promise both texts share: "non patiar ut annum hunc absolvas, quin me sequaris", said as John was "morituriens/moriens" (PG88 l.43013-43035; AS Mar. 3 l.210134-210143). Card `uncertain` 6 keeps both readings: "intra decimum … mensem" (PG88 l.43036) and "Intra decimum enim annum" (AS l.210144). |
| A-B2 (Library header in the card) | RESOLVED | The header sentences are gone from `dates` and `uncertain` 2. The header survives only as a records-only side in "When he died", where it is marked "a header, not a source". |
| A-M1 ("Climacus" undefined; no time) | RESOLVED | "from the Greek word for a ladder" (npnf213 l.5363-5364). "places him late in the 500s" matches "Vixit extremo Christi seculo sexto circa annum 580" (PG88 l.41328-41329). Naming Labbe as the witness is better than the review's bare "He lived in the 500s". |
| A-M2 (two Moseses) | RESOLVED | "Later the monks made John abbot by force." Daniel: "ad coenobii praefecturam vi pertraxerunt" (l.42716). |
| A-M3 (saint's Life unmarked; Raithu) | RESOLVED | Taken as worded (AS l.209523-209524). |
| A-M4 (Barmby's point; editors unexplained) | PARTLY | "still alive then" now gives Barmby's point. Ewald and Hartmann are still given no role, and the reordered sentence puts its object late ("date to 600 a letter of …"). See R2-A-M1. |
| A-M5 (Thomas undated) | RESOLVED | "In the 1400s" (kempis l.3). |
| A-M6 (30 March shifted) | RESOLVED | Labbe: "obiit die 30 Martii, ut habet etiam Martyrologium Romanum", after the Menaea (PG88 l.41330-41331). The Bollandists give the Greek memory (AS l.209393-209396). |
| A-M7 (where Labbe's tale comes from; Bellarmine) | RESOLVED, with a new minor | Labbe: "si vera sunt, quae ipse parum cautus refert sub finem capitis XV ex narratione monachi Sinaitae" (l.41392-41394), where "ipse" is Antonius Magister. I searched PG88 l.42940-43060 and AS l.210050-210200 for Petr-, patriarch- and Hierosol-. The only hit is AS l.210179, a footnote about another man, so "does not name Peter" holds. The Bellarmine line is new text and understates Rader. See R2-A-M2. |
| A-M8 (rachanae; "of John's own time") | RESOLVED | npnf213 l.5390-5398. Rader and the Bollandists are now named as the ones who call the monk "synchrono" (PG88 l.42962). |
| A-M9 (Oliger's Franciscans) | RESOLVED, with a new minor | Oliger, "His testimoniis e saec. XIV duo alia adicere liceat saec. XV" (oliger1912 l.1812), supports "the 1300s and 1400s". Bernardino's "Iste liber in nostra familia magnae reputationis habetur" (l.1827-1828) is said of the Climacus. His chronicle is of the Observants (l.1813), so "his Observant friars" holds. The chroniclers name Angelo of Cingoli, though, not Clareno. See R2-A-M3. |
| Length note | RESOLVED | 403 words, 2:29. The silence episode was cut. Keeping Labbe's "If it is true" is right: he says "si vera narravit" (l.41487). |

**Changed sentences checked and found faithful.** These are the A-M1 Labbe sentence, A-M3's Raithu, A-B1's promise, "Labbe reports a form of this tale …" (l.41484-41490), "Barmby … still alive then" (npnf213 l.5356-5357), and in the card `dates`, `uncertain` 1 to 3 and `legacy.traces` 2. The Peter sentence in `uncertain` 2 matches Labbe at l.41474-41490.

#### New findings
- **R2-A-M1 MINOR (brief P6 and audio; item 4; inverted order, and editors given no role).** "Paul Ewald and Ludwig Hartmann date to 600 a letter of Gregory the Great to a John, abbot of Mount Sinai." Delaying the object is hard to follow aloud, and a listener does not learn who Ewald and Hartmann are. The card's own source entry, "Registrum epistolarum XI.2 (ed. Paul Ewald and Ludwig M. Hartmann)", makes them the editors. Fix: "Gregory the Great wrote to a John, abbot of Mount Sinai, in a letter its editors, Paul Ewald and Ludwig Hartmann, date to 600." Scored: 406 words, 2:30, FK 6.6, Flesch 75.6. This is at the cap.
- **R2-A-M2 MINOR (card `dates` and `uncertain` 2; records "When he died"; items 1, 4; Rader's view understated, and two hard sentences).** (a) "Matthew Rader reports that Robert Bellarmine placed him about 530." Rader writes "Proinde vere Bellarminus anno 530 collocavit" (PG88 l.41752), right after refuting Trithemius. He endorses the year ("rightly", "therefore"), and it is "in 530", not "about 530". Fix: "Matthew Rader says Robert Bellarmine was right to place him in 530." Make the same change to the records' Bellarmine side, which reads "about 53…". (b) `dates`, sentence 2, runs to 31 words with clauses nested inside each other. Fix: "Philippe Labbe says he lived about 580. He also argues that he died between 560 and 565, if a Sinai monk's tale, as Antonius Magister retells it, is true." (c) In `uncertain` 2, "with the death of Peter, patriarch of Jerusalem, in it" is clumsy. Fix: "He then turns to the tale as Antonius Magister retells it, which brings in the death of Peter, patriarch of Jerusalem."
- **R2-A-M3 MINOR (card `legacy.traces` 2; item 1; an editor's identification told as the sources' own).** "Franciscan chroniclers … credit the translation to Angelo Clareno." Bartholomew of Pisa names "frater Angelus" "de Cingulo", and elsewhere "Frater Gentilis de Cingulo" (oliger1912 l.1790-1804). Mariano names "Angelus de Cingulo" (l.1845-1848). Bernardino's "[Angelus de Clareno]" is a bracketed editor's insertion (l.1816). Oliger, after Wadding, identifies these men with "Clareno nostro" (l.1800, 1808-1810). The records already say "(of Angelo of Cingoli)". Fix: "Franciscan chroniclers of the 1300s and 1400s, quoted by Livarius Oliger, credit the translation to Angelo of Cingoli, whom Oliger identifies as Angelo Clareno."

#### Verdicts
- John Climacus: CLEAR (0 blocking, 3 minor). All R1 blockings are resolved. The minors should still be applied.

---

### Liberatus of Carthage

| R1 finding | Verdict | Evidence |
|---|---|---|
| A-B3 (Garnier misreported) | RESOLVED | Card `uncertain` 8 now matches Garnier's note: "De suis Africanis loquitur, Reparato …, Firmo Numidici, Primasio Byzaceni concilii primate, Verecundo … et Victore …; Horum primus depositus est … Euchaidam. Tertius ad suam sedem cum muneribus remissus, post damnationem trium capitulorum … Verecundus et Victor e carcere in carcerem traducti, et tandem in monasteria detrusi" (PL68 l.82523-82535). Victor of Tunnuna: "Firmus concilii Numidiae primas donis principis corruptus" (mommsen1894 l.19073-19074). The records claim matches. |
| A-M10 (no caveat in the brief) | RESOLVED | P2: "His life is known almost only from this letter and his book." `uncertain` 1 opens with the same caveat. The records' absence searches support "almost only". |
| A-M11 (second denial dropped) | Declined; the decline holds | The review allowed it, and the brief says nothing false. "This teaching" refers to the one denial the brief tells. The records log the omission (absent_details, PL68 l.81236-81237). |
| A-M12 (a) to (d) | RESOLVED | (a) "who do not tell the truth about their own leaders" is a fair plain rendering of "aliter loquuntur de suis auctoribus quam veritas habet" (l.75553-75560). "Both heresies" settles which two are meant. (b) "The African chronicler Victor of Tunnuna" appears at the first mention, now P5. (c) "who agreed to condemn them" renders "consentientes … in trium damnationem capitulorum" (l.82407-82408). (d) "counts him among the African defenders of the Three Chapters" renders "unus de Africanis trium Capitulorum defensoribus" (l.74958-74962). |
| A-M13 (length) | RESOLVED | 323 words, 2:00. The partiality dispute stays on the card (`uncertain` 6, `remembered` 1). |
| A-M14 (Garnier's reason) | RESOLVED, with a new minor | "non nisi tamen post obitum Joannis … legati solverunt ex Africa" (PL68 l.81390-81395). The new sentence runs long. See R2-A-M5. |
| A-M15 (Chrysaphius in `traces`) | RESOLVED | Deleted. The records claim stays. |
| A-M16 (Mommsen's "just"; Three Chapters) | RESOLVED | "iusto odio exacerbati in Vigilium" (mommsen1894 l.17577). Bossuet: "respecting Theodore of Mopsuestia, Theodoret's writings against Cyril, and the letter of Ibas of Edessa to Maris the Persian" (npnf214 l.22885-22888). The npnf214 source entry was added. |

#### New findings
- **R2-A-B1 BLOCKING (records `absent_details`; brief P4 and card first mention; items 1, 8; a false absence).** The records state: "His first name of the editor Garnier … no held line gives his first name, so the brief and card say 'Garnier'." Held lines do give it. Harles's note in PG 100 says "notat Jo. Garnerius, praef. ad Liberatum" (`nikephoros-cp_opera-with-vita-stephani-iunioris-pg100-grc-lat_migne1860.txt` l.436), which ties Joannes Garnerius to this very preface. PG 50 says "Joannes Garnerius, Dissert. 4, post Marium Mercatorem" (`john-chrysostom_homily-martyr-lucian-grc-lat_migne-pg50.txt` l.7868). Mansi 4 has "Joannes Garnerius" many times (l.10162, 10490 and others). The same batch's Dionysius card already names "Jean Garnier" for the same scholar. The search behind the absence looked only in PL68. Fix: delete that absent_detail. Add a claim: "Jean Garnier: 'Jo. Garnerius, praef. ad Liberatum' (PG100 l.436); 'Joannes Garnerius … post Marium Mercatorem' (PG50 l.7868)", Documented. Brief P4 and audio: "Jean Garnier, whose edition Migne reprints, counts him …". Card, first mention (`dates`): "Jean Garnier says he wrote under Justinian".
- **R2-A-M4 MINOR (brief P5 and audio; item 4; a compressed tag with no clear agent).** "Garnier takes the journey in Liberatus's preface to be this exile, shared to the end." The listener has to work out who shared it, and what "the end" is. Garnier says Liberatus "non nisi post episcopi mortem ab Euchayda recesserit" (PL68 l.75566-75568). Fix: "Garnier takes the journey in Liberatus's preface to be this exile, which Liberatus shared until his bishop died." To hold the length, P2 can drop "in person" ("came to speak for Reparatus"). Agapetus's "ut apud nos agerent verbo" (Avellana l.24976-24977) loses nothing of substance. With R2-A-B1 and this fix, scored: 325 words, 2:00, FK 8.4, Flesch 60.9. That is near the floor, so check again after any other change.
- **R2-A-M5 MINOR (card `uncertain` 3; item 4; a 42-word sentence that names Garnier twice).** Fix: "Garnier reasons that either Liberatus's words are false, which he can hardly believe, or he came to Rome twice. The envoys named in Agapetus's letter, he says, left Africa only after Pope John had died."

#### Verdicts
- Liberatus of Carthage: NOT CLEAR (1 blocking, 2 minor). Every R1 finding is resolved or soundly declined. The one blocking finding is a records false absence that R1 did not catch, and fixing it touches one word in the brief and one in the card.

---

### Dionysius Exiguus

| R1 finding | Verdict | Evidence |
|---|---|---|
| B-B1 (the Nicene ruling passed on without Duchesne) | RESOLVED | Duchesne says Dionysius sets first "une décision du concile de Nicée" (LP1 l.16299-16302). Note 2: "Cette décision n'a jamais existé ; c'est Denys qui l'a déduite … de la lettre de Proterius d'Alexandrie" (l.16343-16345). Also: "il avance que le concile de Nicée avait prescrit l'usage du cycle de dix-neuf ans … une pia fraus mise au service d'un bon comput" (l.30100-30152). The brief, `uncertain` 2 and the new `contested_claim` all match. "A later letter from Alexandria" is fair for Proterius's letter to Leo. |
| B-B2 (thesis opener) | RESOLVED | The brief P11 and `uncertain` 1 now both open "Later writers differ over his part in the count of years from Christ." |
| B-M1 (narrator's "our") | RESOLVED | "That way, he wrote, the start of our hope …" now carries its speaker. |
| B-M2 (logic; canons; "warned") | RESOLVED | "noted that many did not readily accept them" matches "quibus quia plurimi consensum non praebuere facilem, hoc ipsum vestram noluimus ignorare sanctitatem" (pl67 l.11155-11162). Dropping "no reader should think he agreed" holds: the translator and censor sentence carries it (l.27773-27775). |
| B-M3 (tense break) | RESOLVED, with a new minor | "asked … might be helped". "Might" follows correctly from past "asked", for "ut … possimus nunc meritis adjuvari" (pl70 l.83601-83605). The worker's change from "may" holds. The word "then" is a new snag. See R2-A-M6. |
| B-M4 (Hardouin) | RESOLVED | "alii contra Dionysio antiquiorem statuant. In his Joannes Harduinus, aeram vulgarem Christianam, jam seculo v ineunte, in toto orbe Christiano usitatam fuisse, contendit" (pl67 l.36730-36734). Janus then argues against it ("At enim seculi vox tam late patet …", l.36745-36756). |
| B-M5 (the Nestorius version copied) | RESOLVED | "qu'il présente comme la première qui en ait été faite et comme son œuvre personnelle, est tout simplement copiée sur celle de Marius Mercator (Maassen …)" (LP1 l.30095-30099). |
| B-M6 (Petronius's see) | RESOLVED in the records | The absent_detail was added. The Open-Gaps entry is the coordinator's and is still to be made. |
| B-M7 (print-damage note) | RESOLVED | Gone from `dates` and `uncertain` "His years". It stays in the records. |
| B-M8 (`role`) | RESOLVED | "called abbot in some sources". |
| B-M9 ("held"; Plummer under Bede) | RESOLVED | "No source used here …". Bede and Plummer are now separate source entries. |
| B-M10 (tradition placing) | Open with the coordinator | The records mark it as a worker's call awaiting confirmation. This is not a text fault. |

#### New findings
- **R2-A-M6 MINOR (brief P13 and audio; item 4; "then" misleads).** "He asked him then to plead for them …" "Then" can be heard as "at that time", when Dionysius still prayed with them. The prayer is in fact made after his death ("Interveniat pro nobis", pl70 l.83601). "Him" also makes the listener sort out two men. Fix, same length: "He asked Dionysius to plead for them, so that those once upheld by his prayers might be helped by his merits." Scored: 402 words, 2:29, FK 8.0, Flesch 65.6.
- **R2-A-M7 MINOR (records; card `uncertain` "His translations"; item 1; a name with no held line recorded).** The card's "Jean Garnier" rests on no line in the records. The Cave claim has only "contendit Garnerius" (pl67 l.470-472), and the PL48 file header is not a source. The name is held (see R2-A-B1). Fix: add "PG50 l.7868 ('Joannes Garnerius … post Marium Mercatorem')" to the witness of the records' Proclus claim. No card text changes.

#### Verdicts
- Dionysius Exiguus: CLEAR (0 blocking, 2 minor). Both R1 blockings are resolved. The major mark still holds, at 403 words.

---

### Marius of Avenches

| R1 finding | Verdict | Evidence |
|---|---|---|
| B-M11 (length) | PARTLY | 328 words, 2:01. The coordinator kept the Gallandi sentence ("obiisse vero pridie Kalendas Januarias, anno videlicet 596", pl72 l.59566-59568, after Chifflet). The merged scene sentence holds: "ita totum movit, ut egressus utraque ripa" (chron-min-2 l.21584-21587). The brief is still just past 2:00. See R2-A-M8. |
| B-M12 (epitaph as fact; the monks softened) | RESOLVED | "…with his own hands, it says." The monks "tried one night to kill their bishop" renders "noctis tempore episcopum suum Agricolam … occidere nitentes" (chron-min-2 l.21593-21595). |
| B-M13 (a) to (d) | RESOLVED | "Conon gives 581 for his becoming bishop" (l.20718). "a later hand in the annals of Lausanne" renders "adscriptum est manu recentiore ad a. 601" (l.20712-20714). "The bishop's seat" comes with Mommsen's "verisimile est post eum episcopii sedem mutatam esse" (l.20792-20795). "Still" is gone, and "marked his day … with a procession" matches "hodie fit processio ad ecclesiam sancti Marii" (l.20787-20789). |
| B-M14 (unclear "he"; Sigismund; Agricola) | RESOLVED | "Sigismund, king of Burgundy" (dalton1927 l.30446-30447). "constructum" (chron-min-2 l.21183). "He records" follows a sentence whose subject is Marius, so it reads as Marius. Agricola's see is logged in absent_details. |
| B-M15 (a) to (c) | RESOLVED | "in which his part ends" (l.20941-20944). "Mommsen thinks" for "videtur adhibuisse". "tradition counts him among the saints, with his day on the day of his death" for "Qua quidem die Sanctorum ordinibus ascriptus traditur" (pl72 l.59569-59570). |
| B-M16 (Dalton unused; the Aedui) | RESOLVED | `traces` 4: Dalton, "The event is also mentioned by Marius of Aventicum (Chron., year 563)" (dalton1927 l.25592). `uncertain` "Agaune", built or restored, has a matching `contested_claim`. "the people of the diocese of Autun". |

#### New findings
- **R2-A-M8 MINOR (brief P7 and audio; items 4, 10; a thesis opener, and length).** "His years are disputed." opens the paragraph on a label, and the next three sentences show the dispute anyway. Cutting it also brings the brief inside two minutes. Fix: delete "His years are disputed." so P7 begins "From the epitaph and a church Marius dedicated, Mommsen reckons …". Scored: 324 words, 2:00, FK 7.6, Flesch 66.6.

#### Verdicts
- Marius of Avenches: CLEAR (0 blocking, 1 minor).

---

### Summary
- John Climacus: CLEAR (0 blocking, 3 minor).
- Liberatus of Carthage: NOT CLEAR (1 blocking, 2 minor).
- Dionysius Exiguus: CLEAR (0 blocking, 2 minor).
- Marius of Avenches: CLEAR (0 blocking, 1 minor).

Every brief fix above has to be carried into the audio script. Every card or records fix has to be carried to both `records.json` and the scratchpad record.

---

## R2 recheck, part B: Martin of Braga, Brendan of Clonfert, Barhadbeshabba 'Arbaia of Halwan, Theopistus (era 3 Who batch 8)

Reviewer: independent Opus, seeing these files for the first time. I edited no profile file and made no git writes, web, paid or model calls. I used local scripts only.

This was a targeted recheck. I compared each brief and card at HEAD (772e88c2) with its first-draft commit using `git diff --word-diff`. I checked every R1 finding in parts C, D and E against the current text. I opened the vendored lines myself for every sentence or field that changed. I ran `grade_text` and an audio check by script: the audio must equal the brief plus `[calmly] ` at the start and `[warmly] ` before the last paragraph. The script also checked for empty card fields, missing source files and card sentences past 25 words. I checked Barhadbeshabba against batch 1 `narsai` and `barsauma-of-nisibis` and batch 5 `henana-of-adiabene`, and Theopistus against batch 1 `dioscorus-of-alexandria`.

Mechanical results (all four):

| Profile | Words | Time @162 | FK | Flesch | Audio = brief | Card order / empty fields / files |
|---|---|---|---|---|---|---|
| Martin of Braga | 336 | 2:04 | 7.5 | 67.0 | yes | pass / none / all exist |
| Brendan of Clonfert | 331 | 2:03 | 6.5 | 74.4 | yes | pass / none / all exist |
| Barhadbeshabba 'Arbaia of Halwan | 323 | 1:59 | 6.5 | 72.3 | yes | pass / none / all exist |
| Theopistus | 304 | 1:53 | 7.3 | 70.0 | yes | pass / none / all exist |

No narrator sentence in any brief runs past 24 words. The one longer sentence is Connolly's verbatim quote in Barhadbeshabba's brief, at 29 words. Martin and Brendan run a few seconds past 2:00. That is acceptable at this length, and the drafter's reason holds: the time anchors that C-B1 asked for cost about 20 words.

---

### Martin of Braga

| R1 finding | Verdict | Evidence |
|---|---|---|
| C-B1 (no time anchor) | RESOLVED | Brief para 2 now has "about 550" (caspari1883 l.261, "Um 550"), "a people settled in Spain" (Dalton l.26871-26872) and Dumio "near Braga" (caspari l.448-450). The cut of "later bishop of Braga itself" is covered by "Martin, by then bishop of Braga" in para 4. |
| C-B2 (Krusch named for Arndt's note) | RESOLVED | `uncertain` 3 and the Gregory source title now name Wilhelm Arndt. The note is at arndt-krusch1885 l.18215-18217 and ends "R."; the contents are at l.138 and l.140. |
| C-M1 (miracle story unmarked) | RESOLVED | Para 1: "in a book of the miracles of Martin of Tours" (VM I.11, l.46019-46028). |
| C-M2 (Leovigild out of time) | RESOLVED | Deleted from the brief; kept on the card in `uncertain` 7. |
| C-M3 ("in his time") | RESOLVED | "suis temporibus" is at l.18177. |
| C-M4 (Dumio and Galicia) | RESOLVED | Folded into C-B1. |
| C-M5 ("we" turned into "they") | RESOLVED | "their own faults, his among them" renders "in nobis … corrigamus" (Hispana l.56945-56952). The split after "he told the bishops" reads well. |
| C-M6 (one church) | RESOLVED | `uncertain` 6. The Bollandists' "in ecclesia S. Martini Turonensis a Theodomiro Rege constructa" is at acta-sanctorum martii-3 l.31521-31523, and Caspari's "von Chararich erbauten basilica sancti Martini" at l.761. |
| C-M7 (the Mondonedo gloss) | NOT (the fix introduced a new fault) | See R2-B-B1. |
| C-M8 (Childebert II; the Spanish era) | RESOLVED | caspari l.287-289 ("Childeberts des Zweiten oder im Jahre 580"). The Bollandists' "Era DCX, sive anno Christi DLXXII" is at l.31096-31097. |
| C-M9 (witnesses not placed) | RESOLVED | Para 6. Caspari is now introduced in para 2. |
| C-M10 (ownWords, dates, "Old English") | RESOLVED | All three parts are done. |
| C-M11 (long card sentences) | RESOLVED | No changed card sentence passes 25 words. `uncertain` 4 is still 26 words, but it is unchanged and within "about 25". |
| Length (optional cut) | RESOLVED | 336 words. |

Changed text, checked again:
- Para 2's "Gregory says he had gone East to visit the holy places, and was held second to none in learning in his time" matches l.18176-18177.
- Para 4's "spoke first", "the faith was in no doubt in this province" and "the old canons" match Hispana l.56907-56955 ("de unitate et rectitudine fidei in hac provincia nihil est dubium", "antiquorum canonum").
- The new wording in `remembered` 2 (Fortunatus) matches leo-krusch1881 l.10061-10069 and 9810-9814.
- The new wording in `dates` matches the Bollandists (l.30860-30877, "convenit in annum Christi DLXXX").

#### New findings

- **R2-B-B1 BLOCKING (card `place`; records contested claim "Where Dumio was"; items 1, 7; a dispute the held sources do not make).** The C-M7 fix sets Caspari's placing of Dumio near Braga against "a note signed R. … glosses it as Mondonedo", joined by "while". That presents the note as a rival site for Martin's monastery. The note reads "Fuit episcopus, primo Dumiensis monasterii (Mondonedo), tum Bracarensis" (arndt-krusch1885 l.18215). It glosses the see, not the site. The card's own Bollandist source explains why:
  - Monks of Dumio, fleeing the Moors, built a second monastery near Mondonedo and also called it Dumio: "non longe a Mindoniensi urbe exstruxisse aliud monasterium, et Dumiense etiam appellasse" (acta-sanctorum martii-3 l.31812-31817; again at l.32027-32030).
  - Martin's body lay in "ejus antiqua Dumiensi … ecclesia" until it was moved to Braga in 1606 (l.31817-31821).

  No held source places Martin's Dumio at Mondonedo. Fix, `place`: "Pannonia by birth, Gregory of Tours and his own epitaph say; the East, where Gregory says he visited the holy places; Galicia, in the kingdom of the Sueves; the monastery of Dumio, which C. P. Caspari places near Braga; Braga". Add to `uncertain`, after item 5: "Dumio and Mondonedo. A note signed R. in Wilhelm Arndt's edition of Gregory glosses Dumio as Mondonedo. The Bollandists tell how monks of Dumio, fleeing the Moors, built a second monastery near Mondonedo and also called it Dumio. They say Martin's body stayed in the old church of Dumio until it was moved to Braga in 1606." Records: replace the contested claim "Where Dumio was" with a claim that carries the R. note and the Bollandist lines above. This replaces the C-M7 change outright, per "no fix on a fix". It is not a patch on top of it.

- **R2-B-M1 MINOR (card `uncertain` 7; items 1, 7; an editor's tentative year hardened).** "under a year Theodor Mommsen's margin gives as 585". The margin reads "585?" (mommsen1894 l.20237). Fix: "He tells it under a year Theodor Mommsen's margin gives, with a question mark, as 585."

- **R2-B-M2 MINOR (card `uncertain` 8; item 1; a loose verb, new in the R1 split).** "He is said to have met that saint's relics." Gregory says he came into the Galician port "simul cum ipsis pignoribus", at the same time as the relics (l.46022-46023). "Met" is loose, and "is said" has no owner. Fix: "Gregory says he reached Galicia together with that saint's relics, and he wrote verses and his epitaph to him."

- **R2-B-M3 MINOR (card `uncertain` 1; item 4; the split left the sentence ambiguous).** "Gregory of Tours tells of his coming while Martin was still bishop in Galicia." This can be heard as "Martin came while he was bishop". Gregory means that he wrote while Martin was still bishop ("qui ibidem nunc sacerdos habetur", l.46021). Fix: "Gregory of Tours wrote of his coming while Martin was still bishop in Galicia."

#### Verdicts
- Martin of Braga: NOT CLEAR (1 blocking, 3 minor).

---

### Brendan of Clonfert

| R1 finding | Verdict | Evidence |
|---|---|---|
| C-M12 (Adomnan unplaced, undated) | RESOLVED; the decline holds | Huyshe gives "a.d. 679-704" and "ninth abbot" at l.86-88. Columba's death in 597 is at l.77 (title page) and l.11208 ("St. Columba died in 597"). Leaving out "about a century later" is right. It was the narrator's own sum, and giving both years lets the listener see the gap. |
| C-M13 (Brendan / Brenainn) | RESOLVED | "Brenainn" now appears once, as the Life's name form. |
| C-M14 (Welsh annals; "Doom") | RESOLVED in the brief | The sentence is deleted, and "Judgment Day" is used in both brief and card. The card keeps the annals point in `uncertain` 4 (see R2-B-M5). |
| C-M15 (identification rests on more than Huyshe) | PARTLY | The Lismore story was added correctly (stokes l.878-881, "Brenainn maccu Altai was in Clonfert"). The added Williams clause overreaches: R2-B-B2. |
| C-M16 (16 May; York prymer) | RESOLVED | surtees l.4186 "brandani episcopi" against 16; index l.18515 "Brandani Ep., 16 May". O'Flaherty's day is a death day. VII Kal. June is 26 May, which is correct arithmetic. |
| C-M17 (Lismore list) | RESOLVED, with a new label fault | stokes l.21208-21219. See R2-B-M4. |
| C-M18 (Rees's appendix) | RESOLVED | rees1853 l.446-465 ("the three latter, those of St. Aidus, St. Brendanus, and St. Tathan … although natives of Ireland"). |
| C-M19 ("from the 1170s on") | RESOLVED | The held volume is 1172-1378, per its file name and l.760. |
| C-M20 (Mirk's 1403) | RESOLVED | Removed. The new split "Judas was let out of hell's heat at set times, the story says" is fair to Mirk (l.4583-4613). |
| C-M21 (long card sentences) | RESOLVED | `place` is still 26 words, but it is unchanged and within "about 25". |
| Note (Navigatio) | RESOLVED | The records cite huyshe1905 l.5470-5471. |

#### New findings

- **R2-B-B2 BLOCKING (card `uncertain` 2; records contested claim 1; item 1; a witness made to say more than he does).** "A late Lismore story joins the two, setting Brenainn maccu Altai at Clonfert, and Hugh Williams also calls him the Brendan who founded Clonfert." The antecedent of "him" is Brenainn maccu Altai, and the sentence offers Williams as a second witness to the join. Williams writes only "Brendan, who founded Clonfert, and Kieran … were brought up at Clonard" (gildas williams1899 l.9111-9112). He says nothing of Adomnan, Mocu Alti or maccu Altai. That a Brendan founded Clonfert is not in dispute. The question here is whether Adomnan's man is that Brendan, and Williams does not address it. (R1's C-M15 rationale cited Williams for the same point. That reading was also too strong.) Fix: "A late Lismore story joins the two, setting Brenainn maccu Altai at Clonfert." In the records, take Williams out of that contested side. He can stay as a plain claim that a Brendan founded Clonfert.

- **R2-B-M4 MINOR (card `remembered` 3; item 1; a label the source does not use).** "likens him to a long line of saints and patriarchs, from Abraham to Gregory of Rome". The list includes Solomon, "Hieronymus, the prophet", Augustine and Origen (stokes l.21210-21216), and "saints and patriarchs" does not fit Origen or Solomon. Fix: "The Lismore Life likens him to a long line of figures from the Bible and the church, from Abraham to Gregory of Rome, and last to Noah."

- **R2-B-M5 MINOR (card `uncertain` 4; records absent detail 1; item 1; the editor's identification told as the annal's).** "The Annales Cambriae record only the death of Brendan of Birr." The annal reads "Brendan Byror dormitatio" (annales-cambriae l.2501). The gloss of "Byror" as Birr is the editor's (l.893, "abbot of Birre"). R1 C-M14 named this fault for the brief. The card carries the same sentence. Fix: "The Annales Cambriae record only the death of a Brendan 'Byror', whom their editor takes for Brendan of Birr."

#### Verdicts
- Brendan of Clonfert: NOT CLEAR (1 blocking, 2 minor).

---

### Barhadbeshabba 'Arbaia of Halwan

The coordinator's framing holds throughout the brief:
- The bishop of Halwan is the writer of the Cause.
- The History goes to "Barhadbeshabba 'Arbaia, a priest of the school of Nisibis".
- Nau's one-man view is told as his: "He thinks it not impossible …" (po09 l.31601-31602).

This agrees with `narsai.card.json` `uncertain` 1 and its source authors, with `barsauma-of-nisibis.card.json` l.25 and l.51-61, and with batch 5's "Scher says Barhadbeshabba was among them".

| R1 finding | Verdict | Evidence |
|---|---|---|
| D-B1 (History filed as this man's) | RESOLVED | `keyWorks` has only the Cause, and `ownWords` has only the Cause (Scher, Connolly). The History trace is gone. `remembered` 3 gives Abdisho's list to both owners (scher1908 l.16980-16984; po09 l.31558-31561). |
| D-B2 (Seert without its owner; protest without its cause) | RESOLVED | Seert l.28671-28673 (Sabrisho "avait repoussé la parole du métropolitain pour accepter celle de Hnana"), l.28707 ("environ trois cents"), l.28721 and l.28731 ("Ou plutôt Barhadbšabba"), l.28756 ("fut fait métropolitain de Houlwan"). The brief now ends "Scher takes him for the Cause's author". |
| D-B3 (`place` and BO III.2) | RESOLVED | BO III.1 l.30868-30869: "Beth 'Arbaje, seu Ba-Arbaja pago apud Nisibin". |
| D-B4 (display name merges two men) | RESOLVED | `name`: "Barhadbeshabba 'Arbaia of Halwan". The batch 1 form stays first in `otherNames`. |
| D-M1 (length) | RESOLVED | 323 words. |
| D-M2 (spliced sentence; "epithet") | RESOLVED | scher1908 l.16930-16933 ("ainsi que l'indique son surnom"; "sous Hnana d'Adiabène"). |
| D-M3 (26-word sentence) | RESOLVED, and the worker's reorder is sound | Para 4 now reads: "Henana's own church, Scher says, always charged him with leaving Theodore of Mopsuestia's reading of Scripture. Scher thinks the author probably hid the truth to praise him." This matches scher1908 l.21073-21075 ("Il est probable que l'auteur dissimule ici la vérité pour louer son maître … les Nestoriens ont toujours accusé Hnana d'avoir abandonné … les sentences de Théodore"). With the charge first, "the truth" now has its referent, and "him" points to Henana. "Always" is Scher's own word. Both sentences are attributed. |
| D-M4 (Mari, Ishoyahb III unlisted) | RESOLVED | Both are in `about`, and the files exist. |
| D-M5 (bare Sabrisho) | RESOLVED | scher1908 l.16953. |
| D-M6 (garbled `uncertain` 4; emended century) | RESOLVED | `uncertain` 4 now parses, and `dates` ends on 609 to 628. |

#### New findings

- **R2-B-M6 MINOR (brief para 5 and audio; items 4, 8; "the school" with no clear antecedent).** The D-M2 fix shortened para 2 to "studied at Nisibis", and para 3 then names "the schools of Edessa and Nisibis". So when para 5 says "walked out of the school", it does not say which school. Para 6's "from the same school" leans on it in turn. Fix, para 5, sentence 1: "The Chronicle of Seert says some three hundred students walked out of the school of Nisibis when the head of the church took Henana's side." That makes 26 words. If that is too long, split it: "The Chronicle of Seert tells of a walk-out from the school of Nisibis. Some three hundred students left when the head of the church took Henana's side." Carry the change into the audio.

- **R2-B-M7 MINOR (card `dates`, sentence 5; items 1, 7; an identification told as fact).** "A chronicle Ignazio Guidi edited names him in the vacancy after Gregory's death." The chronicle names "Bar Hadhbésabba urbis Holwan" (guidi1903 l.1975-1976). Joining that man to the Cause's author is Scher's and Nau's work, as `uncertain` 1 itself says. Fix: "A chronicle Ignazio Guidi edited names a Bar Hadbeshabba of Halwan in the vacancy after Gregory's death, which François Nau and Scher give as 609 to 628."

- **R2-B-M8 MINOR (card, three fields that changed in R1; item 4; sentences past about 25 words).**
  - `remembered` 3 (36 words). Fix: "Abdisho of Nisibis lists the books of a Barhadbeshabba 'Arbaia. Among them are the Treasures in three volumes, controversies against all sects and a church history. He also lists a work on the followers of Diodore and a commentary on Mark and the Psalms. Addai Scher gives the list to the Cause's author, and François Nau to the History's writer."
  - `uncertain` 4, sentence 3 (28 words). Fix: "He thinks it not impossible that this man is also the bishop of Halwan. If so, he wrote the History young and the Cause in old age."
  - `uncertain` 9, sentence 2 (27 words). Fix: "The Chronicle of Seert and Mari ibn Sulayman name a Barhadbeshabba, monk of Mount Sa'ran. Sabrisho of Lashom, head of the church, wanted him as his successor. J. Labourt thinks the bishop of Holwan is perhaps that man."

  Unchanged card sentences also run long (`knownFor` 28, `keyWorks` 39, `traces` 1 at 27 and 32, `remembered` 1 at 26, `uncertain` 1 at 31). R1 did not raise them. I note them for the drafter and do not count them as a finding.

#### Verdicts
- Barhadbeshabba 'Arbaia of Halwan: CLEAR (0 blocking, 3 minor). The minor fixes should still be applied.

---

### Theopistus

The coordinator's framing holds. The narrator's account is told as the book's account: "the History of Dioscorus says", "by his own account", "the book says", "He says he hid". Nau's view that the book was reworked after 512 sits in para 4, the longest paragraph, with each step hedged as Nau hedges it ("he suggests", "he thinks", "may"). The profile is consistent with batch 1 `dioscorus-of-alexandria`:
- Chalcedon, the exile at Gangra in Paphlagonia, and 454 as Nau's year;
- Nau's date for the present form after 512, and Assemani's charge of fiction;
- the History of the Patriarchs on the missing biography.

The R1 note on the Dioscorus records ("only held account of the exile") remains with the coordinator.

| R1 finding | Verdict | Evidence |
|---|---|---|
| E-B1 (no Chalcedon, exile or death) | RESOLVED | Nau l.441-445 ("A partir de la convocation du concile, Théopiste prétend n'avoir plus quitté Dioscore. A la mort de celui-ci …"); History l.17012-17013 ("je meurs en exil") and l.17022 ("deux mois après sa mort saint Pierre m'envoya une lettre"); Nau l.580-585 ("récits en sa faveur … pouvait se trouver un récit, écrit par Théopiste, de la réunion du concile de Chalcédoine et de l'exil à Gangres"). "By his own account" carries Nau's "prétend". The worker's split of the para 4 sentence keeps "may". |
| E-B2 (Pentapolis told as fact) | RESOLVED | "He says he hid …" matches l.17029-17031. |
| E-B3 (false absence) | RESOLVED | po08 l.447-448 ("écrite par son disciple Théopiste"); PO 13 l.12639. The Duchesne passage (l.15895-15907) names only the panegyric, so "name him only as the History's writer" holds. |
| E-M1 (the scene) | RESOLVED | l.13928-13930 and l.13952-13953. |
| E-M2 (whose vision; 512) | RESOLVED | l.16865-16866 and l.498. |
| E-M3 ("rhetor"; Peter the Iberian) | RESOLVED, as the coordinator directed | "a writer trained in rhetoric" renders "l'un des rhéteurs" (l.587). The Gaza placing is on the card. |
| E-M4 (`place`) | RESOLVED | "la ville de Pentépolis" (l.17029-17030); "Ou plutôt : Dans la Pentapole (Cyrénaïque)" (l.17034). The island is in the History itself ("dans toute l'île de Gangra", l.16609). Paphlagonia is at l.337 and l.801. |
| E-M5 (hedges hardened) | RESOLVED | l.578-579, l.594-595 and l.17175-17176, all as worded. |
| E-M6 ("Jacobites") | RESOLVED; the decline of the gloss holds | No held line glosses "Jacobites" as the card's gloss would. "Later writers of Dioscorus's party" matches `uncertain` 1. |

#### New findings

- **R2-B-M9 MINOR (card `uncertain` 1, sentences 3-4, and `uncertain` 3, 6; item 4; a "those" with no noun, and changed sentences past about 25 words).** E-B1 fixed "among those written in Egypt soon after the death" in the brief. The same phrase, with no noun for "those", is still in the card. Several sentences reworded in R1 also run 30 to 37 words. Fixes:
  - `uncertain` 1, sentences 3-4: "François Nau thinks an account by Theopistus may have been among the stories in Dioscorus's favor written in Egypt soon after his death. He suggests this as the most likely answer for now. After 512, he thinks, a writer trained in rhetoric, of the school of Peter the Iberian, reworked it, probably in Greek, and the Syriac comes from that Greek."
  - `uncertain` 3: "Nau thinks the Syriac seems to be translated from Greek. He cites Greek words carried over, the forms of some names, and Bible passages that seem translated from a Greek text. … A note at the end of the translation reports that Crum found old Coptic fragments matching parts of the History. It says they will help in working out which text is the original."
  - `uncertain` 6, sentence 2: "The archdeacon Peter, his companion in the History, is a different man from Peter the Iberian, bishop of Maiouma near Gaza. Nau explains that the History calls Peter the Iberian by his Iberian name, Nabarnougios."

#### Verdicts
- Theopistus: CLEAR (0 blocking, 1 minor). The minor fix should still be applied.

---

### Summary

| Profile | Verdict | Blocking | Minor |
|---|---|---|---|
| Martin of Braga | NOT CLEAR | 1 (R2-B-B1, the Dumio/Mondonedo dispute created by the C-M7 fix) | 3 |
| Brendan of Clonfert | NOT CLEAR | 1 (R2-B-B2, Williams made a witness to the Mocu Alti join) | 2 |
| Barhadbeshabba 'Arbaia of Halwan | CLEAR | 0 | 3 |
| Theopistus | CLEAR | 0 | 1 |

Both blocking fixes are deletions or a move to `uncertain`, and both touch card and records only. Neither brief changes, so length, readability and audio stay as measured above. Barhadbeshabba's R2-B-M6 is the only brief change proposed, and it adds two words.

Cap note (CLAUDE.md, "Review cycles are capped"): this recheck is the second review file on these documents.

---
